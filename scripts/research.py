#!/usr/bin/env python3
"""Validate research metadata, generate its locator, and resolve stable identifiers.

This checks declared structure, local support and grounding, never mathematical
truth, premise completeness or review sufficiency. Untyped records preserve
source passages without synthesizing accepted proof routes.
"""
from __future__ import annotations

import argparse
import html
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML is required: python3 -m pip install -r scripts/requirements-research.txt")

try:
    from . import check_markdown_links as links
except ImportError:
    import check_markdown_links as links


class UniqueLoader(yaml.SafeLoader):
    """Safe YAML, with duplicate mapping keys rejected at every nesting level."""


def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=True)
        if not isinstance(key, str):
            raise yaml.constructor.ConstructorError(None, None, "mapping keys must be strings", key_node.start_mark)
        if key in result:
            raise yaml.constructor.ConstructorError(None, None, f"duplicate key: {key}", key_node.start_mark)
        result[key] = loader.construct_object(value_node, deep=True)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)
IMAGE = re.compile(r"!\[[^\]]*\]\((<[^>]+>|[^\s)]+)(?:\s+[\"'][^)]*[\"'])?\)")
ID = re.compile(r"STCI-([RAFIQ])-\d{4}\Z")
TYPES = {"result": "R", "argument": "A", "framework": "F", "investigation": "I"}
STATUSES = {
    "argument": {"draft", "complete"},
    "framework": {"proposed", "in_use", "retired"},
    "investigation": {"planned", "active", "complete", "inactive"},
}
EXTRA = {"result": {"statement", "proofs", "supersedes"}, "argument": {"conclusion"},
         "framework": {"bridges"}, "investigation": {"question", "findings"}}
RELATIONS = {
    "uses": ({"result", "argument"}, {"argument", "framework", "investigation"}),
    "motivates": ({"framework"}, {"investigation"}),
    "produces": ({"investigation"}, {"result", "argument"}),
    "informs": ({"investigation", "result", "argument"}, {"framework"}),
    "limits": ({"result"}, {"framework", "investigation"}),
}
LEGACY_QUESTION_STATUSES = {"open", "conditional", "resolved", "superseded"}
LEGACY_FIELDS = {"id", "title", "kind", "status", "scope", "statement", "dependencies", "evidence",
                 "independent_audits", "legacy_ids", "supersedes", "superseded_by",
                 "limitations", "applicable_results"}


@dataclass
class Record:
    path: Path
    data: dict
    legacy: bool = False

    @property
    def id(self):
        return self.data["id"]

    @property
    def type(self):
        return ("result" if self.id.startswith("STCI-R-") else "question") if self.legacy else self.data["type"]


class Repository:
    def __init__(self, root: Path | str):
        self.root = Path(root).resolve()
        self.records: dict[str, Record] = {}
        self.aliases: dict[str, tuple[Record, str]] = {}
        self.errors: list[str] = []
        self.relations: list[tuple[Record, dict]] = []
        self._sections: dict[Path, dict[str, str]] = {}

    def error(self, path, message):
        name = path.relative_to(self.root) if isinstance(path, Path) and path.is_relative_to(self.root) else path
        self.errors.append(f"{name}: {message}")

    def shape(self, value, required, optional, path, label):
        if not isinstance(value, dict):
            self.error(path, f"{label} must be a mapping")
            return False
        for key in sorted(required - value.keys()):
            self.error(path, f"{label} missing {key}")
        for key in sorted(value.keys() - required - optional):
            self.error(path, f"{label} unknown field {key}")
        return True

    def strings(self, value, path, label, nonempty=False, unique=True):
        if not isinstance(value, list) or any(not isinstance(x, str) or not x.strip() for x in value):
            self.error(path, f"{label} must be a list of nonempty strings")
            return []
        if nonempty and not value:
            self.error(path, f"{label} must be nonempty")
        if unique and len(value) != len(set(value)):
            self.error(path, f"{label} has duplicate endpoints/identifiers")
        return value

    def section_bodies(self, path):
        """Use the checker's heading rules to identify nonempty addressed sections."""
        if path in self._sections:
            return self._sections[path]
        raw_lines = path.read_text(encoding="utf-8").splitlines()
        source = links.visible_lines("\n".join(raw_lines))
        if source and source[0] == "---":
            for end in range(1, len(source)):
                if source[end] in {"---", "..."}:
                    source[:end + 1] = [""] * (end + 1)
                    break
        headings, generated, paragraph = [], set(), []
        for index, line in enumerate(source):
            for tag in re.findall(r"<[^>]+>", line):
                for anchor in re.findall(r'''\b(?:id|name)=["']([^"']+)["']''', tag):
                    headings.append((anchor, index, 6))
            match = re.match(r"^ {0,3}(#{1,6})\s+(.+?)(?:\s+#+\s*)?$", line)
            title, level, start = None, None, index
            if match:
                title, level = match.group(2), len(match.group(1))
                paragraph = []
            elif re.fullmatch(r" {0,3}(?:=+|-+)\s*", line):
                if paragraph:
                    title, level = " ".join(x[1] for x in paragraph), 1 if "=" in line else 2
                    start = paragraph[0][0]
                paragraph = []
            elif line.strip() and not re.match(r"^(?: {4}|\t| {0,3}(?:>|[-+*] |\d+[.)] |<))", line):
                paragraph.append((index, line.strip()))
            else:
                paragraph = []
            if title is not None:
                title = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", html.unescape(title))
                title = re.sub(r"<[^>]*>", "", title).lower()
                slug = re.sub(r"[^\w\- ]", "", title, flags=re.UNICODE).replace(" ", "-")
                anchor, occurrence = slug, 0
                while anchor in generated:
                    occurrence += 1
                    anchor = f"{slug}-{occurrence}"
                generated.add(anchor)
                headings.append((anchor, start, level))
        bodies = {}
        for anchor, start, level in headings:
            end = next((i for _, i, depth in headings if i > start and depth <= level), len(source))
            body = [line for line in raw_lines[start + 1:end]
                    if not re.match(r"^ {0,3}#{1,6}\s|^\s*(?:=+|-+)\s*$", line)]
            bodies[anchor] = "\n".join(body).strip()
        self._sections[path] = bodies
        return bodies

    def location(self, raw, owner, label, fragment=False, own=False, remote=False):
        if not isinstance(raw, str) or not raw.strip():
            self.error(owner, f"{label} must be a nonempty local location")
            return None
        try:
            parsed = urlsplit(raw)
        except ValueError as exc:
            self.error(owner, f"{label} malformed location: {exc}")
            return None
        if remote and parsed.scheme in {"http", "https"} and parsed.netloc:
            return None  # disclosed citation, never a verified proof route
        decoded = unquote(parsed.path)
        if (parsed.scheme or parsed.netloc or parsed.query or raw.startswith("//")
                or decoded.startswith(("/", "\\")) or "\\" in decoded
                or ".." in Path(decoded).parts or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", decoded)):
            self.error(owner, f"{label} unsafe/nonlocal location {raw}")
            return None
        target = (self.root / decoded).resolve() if decoded else owner.resolve()
        if not target.is_relative_to(self.root):
            self.error(owner, f"{label} target outside repository: {raw}")
            return None
        if own and (target != owner.resolve() or decoded):
            self.error(owner, f"{label} must be a local #fragment in its owner")
        if not target.is_file():
            self.error(owner, f"{label} missing file {raw}")
            return None
        anchor = unquote(parsed.fragment)
        if fragment and (not anchor or target.suffix.lower() not in {".md", ".markdown"}):
            self.error(owner, f"{label} requires a Markdown section fragment")
            return None
        if anchor:
            if target.suffix.lower() not in {".md", ".markdown"} or anchor not in links.anchors(target):
                self.error(owner, f"{label} missing fragment {raw}")
            elif fragment and not self.section_bodies(target).get(anchor):
                self.error(owner, f"{label} section is empty: {raw}")
        return target

    def index_links(self):
        path = self.root / "research/results/INDEX.md"
        entries = []
        if not path.resolve().is_relative_to(self.root):
            self.error(path, "result index symlink escapes repository")
            return entries
        if path.is_file():
            source = "\n".join(links.visible_lines(path.read_text(encoding="utf-8")))
            for match in links.LINK.finditer(source):
                raw = match.group(1).strip("<>")
                label = match.group(0).split("](", 1)[0]
                identifiers = re.findall(r"STCI-[RQ]-\d{4}", label)
                try:
                    parsed = urlsplit(raw)
                except ValueError as exc:
                    self.error(path, f"malformed index link: {exc}")
                    continue
                decoded = unquote(parsed.path)
                nonlocal_path = (parsed.scheme or parsed.netloc or parsed.query
                    or decoded.startswith(("/", "\\")) or "\\" in decoded
                    or ".." in Path(decoded).parts
                    or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", decoded))
                if nonlocal_path:
                    if identifiers:
                        self.error(path, f"ID-labeled index link must be a local result locator: {raw}")
                    continue
                target = (path.parent / decoded).resolve()
                if target.parent != path.parent or target.suffix != ".md":
                    if identifiers:
                        self.error(path, f"ID-labeled index link must address research/results/*.md: {raw}")
                    continue
                entries.append((target, identifiers))
                if identifiers and parsed.fragment and target.is_file() and unquote(parsed.fragment) not in links.anchors(target):
                    self.error(path, f"index locator missing fragment: {raw}")
        return entries

    def load(self):
        entries = self.index_links()
        prose = {path for path, labels in entries if not labels}
        candidates = set(path for path, _ in entries)
        for folder in ("results", "arguments", "frameworks", "questions"):
            directory = self.root / "research" / folder
            for candidate in directory.rglob("*.md"):
                if folder == "results" and any(part.endswith(".support") for part in candidate.relative_to(directory).parts[:-1]):
                    continue  # Proof attachments are not additional objects.
                candidates.add(candidate)
        candidates.update(p for p in (self.root / "research/investigations").rglob("*.md") if p.name == "index.md")
        candidates.update((self.root / "research/investigations").glob("*.md"))
        for path in sorted(candidates):
            if not path.resolve().is_relative_to(self.root):
                self.error(path, "record symlink escapes repository")
                continue
            try:
                source = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as exc:
                self.error(path, f"cannot read record: {exc}")
                continue
            if not source.startswith("---\n"):
                # Existing navigation is recognized by its explicit prose role,
                # not a permanent list of exempt filenames or IDs.
                legacy_framework = (path == self.root / "research/frameworks/formal-normal-geometry.md"
                    and not re.search(r"^\s*(?:id|type):", source, re.M))
                navigation = path.name in {"INDEX.md", "README.md"} and path.parent in {self.root / "research" / name for name in ("results", "questions", "arguments", "frameworks", "investigations")}
                if (path in prose or legacy_framework or navigation) and not source.startswith("---") and not re.search(r"^\s*(?:id|type):", source, re.M):
                    continue
                self.error(path, "missing YAML front matter")
                continue
            end = re.search(r"^(?:---|\.\.\.)\s*$", source[4:], re.M)
            if not end:
                self.error(path, "unterminated YAML front matter")
                continue
            try:
                data = yaml.load(source[4:4 + end.start()], Loader=UniqueLoader)
            except (yaml.YAMLError, RecursionError, ValueError) as exc:
                self.error(path, f"invalid YAML: {exc}")
                continue
            if not isinstance(data, dict):
                self.error(path, "metadata must be a mapping")
                continue
            rid = data.get("id")
            if not isinstance(rid, str) or not ID.fullmatch(rid):
                self.error(path, "missing/invalid ID")
                continue
            legacy = "type" not in data and rid.startswith(("STCI-R-", "STCI-Q-"))
            record = Record(path, data, legacy)
            if rid in self.records:
                self.error(path, f"duplicate ID {rid}")
            else:
                self.records[rid] = record
        # Enforce the existing index dynamically; no hardcoded record count.
        indexed = set()
        for path, labels in entries:
            if not path.is_file():
                self.error(path, "result index target missing")
            for rid in labels:
                indexed.add(rid)
                if rid not in self.records or self.records[rid].path != path:
                    self.error(path, f"result index ID/path mismatch: {rid}")
        for record in self.records.values():
            if record.legacy and record.type == "result" and record.id not in indexed:
                self.error(record.path, f"legacy result absent from results/INDEX.md: {record.id}")

    def resolve(self, rid, path, label, expected=None):
        record = self.records.get(rid) if isinstance(rid, str) else None
        if record is None and isinstance(rid, str) and rid in self.aliases:
            record = self.aliases[rid][0]
        if record is None:
            self.error(path, f"unknown {label} ID {rid}")
        elif expected and (not isinstance(record.type, str) or record.type not in expected):
            self.error(path, f"{label} {rid} has wrong type {record.type}")
        return record

    def legacy(self, record):
        path, data = record.path, record.data
        allowed = (LEGACY_FIELDS - {"status"}) | {"proofs"} if record.type == "result" else LEGACY_FIELDS
        required = (allowed - {"applicable_results", "proofs"}) if record.type == "result" else {"id", "title", "status", "applicable_results", "evidence"}
        self.shape(data, required, allowed, path, "untyped record")
        if not isinstance(data.get("title"), str) or not data.get("title", "").strip():
            self.error(path, "legacy title must be nonempty")
        expected = "results" if record.type == "result" else "questions"
        if path.parent != self.root / "research" / expected:
            self.error(path, "legacy ID/location mismatch")
        if record.type == "question" and (not isinstance(data.get("status"), str) or data.get("status") not in LEGACY_QUESTION_STATUSES):
            self.error(path, "invalid question status")
        if record.type == "result":
            for key in ("scope", "statement", "kind", "limitations"):
                if key not in data:
                    self.error(path, f"legacy result missing {key}")
            if not isinstance(data.get("kind"), str) or data.get("kind") not in {"theorem", "lemma", "reduction", "certificate"}:
                self.error(path, "invalid legacy kind")
            scope = data.get("scope")
            if not isinstance(scope, dict) or not scope:
                self.error(path, "legacy scope must be a nonempty mapping")
            else:
                self.shape(scope, {"characteristic", "curve", "hypotheses"}, set(), path, "legacy scope")
                for key in ("characteristic", "curve"):
                    if not isinstance(scope.get(key), str) or not scope[key].strip():
                        self.error(path, f"legacy scope {key} must be nonempty text")
                self.strings(scope.get("hypotheses"), path, "legacy hypotheses")
            if not isinstance(data.get("statement"), str) or not data.get("statement", "").strip():
                self.error(path, "legacy statement must be nonempty text")
            self.strings(data.get("limitations"), path, "legacy limitations")
            if "proofs" in data:
                self.proofs(record)
        for key in ("dependencies", "applicable_results", "supersedes", "superseded_by"):
            for rid in self.strings(data.get(key, []), path, f"legacy {key}"):
                self.resolve(rid, path, key, {"result"})
        for key in ("evidence", "independent_audits"):
            for raw in self.strings(data.get(key, []), path, f"legacy {key}", unique=False):
                self.location(raw, path, key, remote=True)
        self.strings(data.get("legacy_ids", []), path, "legacy_ids")

    def object(self, record):
        path, data, kind = record.path, record.data, record.data.get("type")
        if not isinstance(kind, str) or kind not in TYPES:
            self.error(path, f"unknown type {kind}")
            return
        required = {"id", "type", "title", "scope"} | (EXTRA[kind] - {"supersedes"})
        if kind != "result":
            required.add("status")
        self.shape(data, required, {"aliases", "relations", "supersedes"} | EXTRA[kind], path, "record")
        if kind != "result" and "supersedes" in data:
            self.error(path, "supersedes is only allowed on Results")
        if not record.id.startswith(f"STCI-{TYPES[kind]}-"):
            self.error(path, "ID/type mismatch")
        expected = self.root / "research" / {"result": "results", "argument": "arguments", "framework": "frameworks", "investigation": "investigations"}[kind]
        valid_location = (path.parent.parent == expected and path.name == "index.md") if kind == "investigation" else path.parent == expected
        if not valid_location:
            self.error(path, "type/location mismatch")
        if not isinstance(data.get("title"), str) or not data.get("title", "").strip():
            self.error(path, "title must be nonempty text")
        if kind != "result" and (not isinstance(data.get("status"), str) or data.get("status") not in STATUSES[kind]):
            self.error(path, f"invalid {kind} status")
        for key in ["scope"] + sorted(EXTRA[kind] - {"proofs", "supersedes"}):
            self.location(data.get(key), path, key, fragment=True, own=True)
        if kind == "result":
            self.location("#limitations", path, "limitations", fragment=True, own=True)
            self.proofs(record)
            supersedes = self.strings(data.get("supersedes", []), path, "supersedes")
            if supersedes:
                self.location("#supersession", path, "supersession", fragment=True, own=True)
            for rid in supersedes:
                self.resolve(rid, path, "supersedes", {"result"})
        self.research_relations(record)
        self.support_links(record)

    def proofs(self, record):
        path, data = record.path, record.data
        routes = data.get("proofs")
        if not isinstance(routes, list):
            self.error(path, "proofs must be a list")
            return
        names = set()
        for route in routes:
            if not self.shape(route, {"name", "at", "using", "review"}, set(), path, "proof"):
                continue
            name = route.get("name")
            if not isinstance(name, str) or not name.strip():
                self.error(path, "proof name must be nonempty text")
            elif name in names:
                self.error(path, "duplicate proof name")
            else:
                names.add(name)
            target = self.location(route.get("at"), path, "proof at", fragment=True)
            if target:
                owners = [r for r in self.records.values() if r.path.resolve() == target]
                if target != path.resolve() and any(not r.legacy and r.data.get("type") != "argument" for r in owners):
                    self.error(path, "proof at cannot use another typed Result, Framework, or Investigation as its proof owner")
            premises = []
            for rid in self.strings(route.get("using"), path, "proof using"):
                premise = self.resolve(rid, path, "proof using", {"result"})
                if premise:
                    premises.append(premise.id)
                if premise and premise.id == record.id:
                    self.error(path, "proof has direct self-premise")
            if len(premises) != len(set(premises)):
                self.error(path, "proof using repeats a premise through aliases")
            review = route.get("review")
            if self.shape(review, {"state", "at"}, {"basis"}, path, "review"):
                if not isinstance(review.get("state"), str) or review.get("state") not in {"pending", "accepted", "disputed"}:
                    self.error(path, "invalid review state")
                if review.get("state") == "accepted" and (not isinstance(review.get("basis"), str) or review.get("basis") not in {"inherited", "reconstructed"}):
                    self.error(path, "accepted review requires basis: inherited or reconstructed")
                if "basis" in review and (not isinstance(review["basis"], str) or review["basis"] not in {"inherited", "reconstructed"}):
                    self.error(path, "invalid review basis")
                self.location(review.get("at"), path, "review at", fragment=True)

    def research_relations(self, record):
        value = record.data.get("relations", [])
        if not isinstance(value, list):
            self.error(record.path, "relations must be a list")
            return
        for relation in value:
            if not self.shape(relation, {"kind", "from", "to", "at"}, set(), record.path, "relation"):
                continue
            kind = relation.get("kind")
            if not isinstance(kind, str) or kind not in RELATIONS:
                self.error(record.path, f"unknown relation kind {kind}")
                continue
            groups = []
            for key, types in zip(("from", "to"), RELATIONS[kind]):
                group = []
                for rid in self.strings(relation.get(key), record.path, f"relation {key}", nonempty=True):
                    target = self.resolve(rid, record.path, f"relation {key}", types)
                    if target:
                        group.append(target.id)
                if len(group) != len(set(group)):
                    self.error(record.path, f"relation {key} repeats an object through aliases")
                groups.append(group)
            if record.id not in groups[0] + groups[1]:
                self.error(record.path, "relation owner must be incident")
            self.location(relation.get("at"), record.path, "relation at", fragment=True, own=True)
            normalized = dict(relation, **{"from": sorted(groups[0]), "to": sorted(groups[1])})
            self.relations.append((record, normalized))

    def support_links(self, record):
        # Reuse extraction and anchors, but keep roots instance-local. Markdown
        # body links are document-relative; metadata locations are root-relative.
        source = record.path.read_text(encoding="utf-8")
        end = re.search(r"^(?:---|\.\.\.)\s*$", source[4:], re.M)
        source = source[4 + end.end():] if end else source
        visible = "\n".join(links.visible_lines(source))
        for match in list(links.LINK.finditer(visible)) + list(IMAGE.finditer(visible)) + list(links.REFERENCE.finditer(visible)):
            raw = match.group(1).strip("<>")
            try:
                parsed = urlsplit(raw)
            except ValueError as exc:
                self.error(record.path, f"malformed support link: {exc}")
                continue
            if parsed.scheme or parsed.netloc:
                continue  # literature citations are not network-checked
            decoded = unquote(parsed.path)
            if parsed.query or decoded.startswith(("/", "\\")) or "\\" in decoded:
                self.error(record.path, f"unsafe support link {raw}")
                continue
            target = (record.path.parent / decoded).resolve() if decoded else record.path.resolve()
            if not target.is_relative_to(self.root):
                self.error(record.path, f"support link outside repository: {raw}")
            elif not target.is_file():
                self.error(record.path, f"missing linked support {raw}")
            elif parsed.fragment and target.suffix.lower() in {".md", ".markdown"} and unquote(parsed.fragment) not in links.anchors(target):
                self.error(record.path, f"missing linked support fragment {raw}")

    def validate(self):
        self.records, self.aliases, self.errors, self.relations, self._sections = {}, {}, [], [], {}
        if not self.root.is_dir():
            self.error(self.root, "repository root does not exist or is not a directory")
            return self.errors
        if not (self.root / "research").is_dir():
            self.error(self.root, "research directory is missing")
            return self.errors
        self.load()
        for record in self.records.values():
            if record.legacy:
                alias_items = [(alias, "") for alias in self.strings(record.data.get("legacy_ids", []), record.path, "legacy_ids")]
            else:
                aliases = record.data.get("aliases", {})
                if not isinstance(aliases, dict):
                    self.error(record.path, "aliases must be a mapping")
                    continue
                alias_items = aliases.items()
            for alias, fragment in alias_items:
                if not isinstance(alias, str) or not alias.strip():
                    self.error(record.path, "alias must be a nonempty identifier")
                    continue
                if alias in self.records or alias in self.aliases:
                    self.error(record.path, f"duplicate/colliding alias {alias}")
                else:
                    self.aliases[alias] = (record, fragment)
                if not record.legacy:
                    self.location(fragment, record.path, "alias", fragment=True, own=True)
        for record in self.records.values():
            if record.legacy:
                self.legacy(record)
            else:
                self.object(record)
        seen = set()
        motivated = set()
        for owner, relation in self.relations:
            key = (relation["kind"], tuple(relation["from"]), tuple(relation["to"]))
            if key in seen:
                self.error(owner.path, "duplicate grouped relation")
            seen.add(key)
            if relation["kind"] == "motivates":
                motivated.update(relation["to"])
        for record in self.records.values():
            if not record.legacy and record.data.get("type") == "investigation" and record.id not in motivated:
                self.error(record.path, "Investigation requires a Framework motivates relation")
        self.grounding()
        self.supersession()
        return sorted(set(self.errors))

    def grounding(self):
        accepted = []
        for record in self.records.values():
            routes = record.data.get("proofs", [])
            if record.type != "result" or not isinstance(routes, list):
                continue
            for route in routes:
                if not isinstance(route, dict):
                    continue
                review = route.get("review")
                if not isinstance(review, dict) or review.get("state") != "accepted":
                    continue
                using = route.get("using")
                if not isinstance(using, list) or any(not isinstance(rid, str) for rid in using):
                    continue
                premises = {self.aliases[rid][0].id if rid in self.aliases else rid for rid in using}
                accepted.append((record, route.get("name"), premises))

        grounded = set()
        while True:
            ready = {record.id for record, _, premises in accepted if premises <= grounded}
            if ready == grounded:
                break
            grounded = ready
        for record, name, premises in accepted:
            if not premises <= grounded:
                self.error(record.path, f"accepted route {name!r} lacks noncircular accepted prerequisites")

    def supersession(self):
        edges = {}
        for record in self.records.values():
            if record.type != "result":
                continue
            value = record.data.get("supersedes", [])
            edges.setdefault(record.id, [])
            edges[record.id].extend([self.aliases[x][0].id if x in self.aliases else x for x in value if isinstance(x, str)] if isinstance(value, list) else [])
        for record in self.records.values():
            if record.legacy and record.type == "result":
                value = record.data.get("superseded_by", [])
                for newer in value if isinstance(value, list) else []:
                    if isinstance(newer, str) and newer in self.records:
                        edges.setdefault(newer, []).append(record.id)
        done, active = set(), set()
        def visit(rid):
            if rid in active:
                self.error(self.records[rid].path, f"supersession cycle involving {rid}")
                return
            if rid in done:
                return
            active.add(rid)
            for other in edges.get(rid, []):
                if other in edges:
                    visit(other)
            active.remove(rid)
            done.add(rid)
        for rid in sorted(edges):
            visit(rid)

    def checked(self):
        errors = self.validate()
        if errors:
            raise ValueError("\n".join(errors))

    def url(self, record, fragment="", catalog=True):
        base = self.root / "research" if catalog else self.root
        path = record.path.relative_to(base).as_posix()
        suffix = "#" + quote(unquote(fragment[1:]), safe="-._~") if fragment else ""
        return quote(path, safe="/") + suffix

    @staticmethod
    def text(value):
        return str(value).replace("|", "\\|").replace("\n", " ")

    def _legacy_reference_groups(self):
        """Derive navigation from legacy declarations without creating routes."""
        for owner in sorted(self.records.values(), key=lambda x: x.id):
            if not owner.legacy:
                continue
            for field in ("dependencies", "applicable_results"):
                references = owner.data.get(field, [])
                if not references:
                    continue
                targets, labels = [], []
                for identifier in references:
                    target = self.records.get(identifier) or self.aliases[identifier][0]
                    targets.append(target.id)
                    labels.append(identifier if identifier == target.id else f"{identifier} → {target.id}")
                yield owner, field, targets, ", ".join(labels)

    def catalog(self):
        self.checked()
        lines = ["# Research catalog", "", "Generated by `python3 scripts/research.py catalog`; edit the owning records.", "", "This locator checks declared structure, not mathematical truth or review sufficiency.", "Untyped source passages do not synthesize proof-route reviews.", ""]
        for kind in ("result", "argument", "framework", "investigation", "question"):
            records = [r for r in self.records.values() if r.type == kind]
            if not records:
                continue
            heading = "Untyped questions" if kind == "question" else f"{kind.title()}s"
            lines += [f"## {heading}", "", "| ID | Title | Review / activity | Scope / format |", "| --- | --- | --- | --- |"]
            for r in sorted(records, key=lambda x: x.id):
                scope = "untyped record" if r.legacy else f"[scope]({self.url(r, r.data['scope'])})"
                review = self.review_summary(r, catalog=True)
                lines.append(f"| [{r.id}]({self.url(r)}) | {self.text(r.data['title'])} | {self.text(review)} | {scope} |")
            lines.append("")
        if self.aliases:
            lines += ["## Aliases", ""]
            for alias, (r, fragment) in sorted(self.aliases.items()):
                inherited = " (alias to the whole untyped document)" if r.legacy else ""
                lines.append(f"- `{alias}` → [{r.id}]({self.url(r, fragment)}){inherited}")
            lines.append("")
        lines += ["## Proof routes and backlinks", ""]
        for r in sorted(self.records.values(), key=lambda x: x.id):
            if r.legacy:
                for owner, field, _, group in self._legacy_reference_groups():
                    if owner.id == r.id:
                        lines.append(f"- {r.id}: recorded references ({field}) [{group}]; no synthesized accepted route.")
            for route in r.data.get("proofs", []):
                review = route["review"]
                basis = f", {review['basis']}" if "basis" in review else ""
                lines.append(f"- {r.id}: {self.text(route['name'])}; joint premises [{', '.join(route['using'])}]; proof `{route['at']}`; review {review['state']}{basis} at `{review['at']}`.")
        lines.append("")
        lines += ["## Research relationships (grouped)", ""]
        for owner, relation in sorted(self.relations, key=lambda x: (x[1]["kind"], x[1]["from"], x[1]["to"], x[0].id)):
            lines.append(f"- [{', '.join(relation['from'])}] — {relation['kind']} → [{', '.join(relation['to'])}]; [explanation owned by {owner.id}]({self.url(owner, relation['at'])}).")
        lines += ["", "## Object backlinks", ""]
        for r in sorted(self.records.values(), key=lambda x: x.id):
            incoming = [f"recorded reference from {owner.id} ({field} group [{group}])"
                        for owner, field, targets, group in self._legacy_reference_groups() if r.id in targets]
            for conclusion in self.records.values():
                for route in conclusion.data.get("proofs", []):
                    resolved = [self.records.get(x) or (self.aliases[x][0] if x in self.aliases else None) for x in route["using"]]
                    if r in resolved:
                        incoming.append(f"premise of {conclusion.id} ({route['name']})")
                    target = conclusion.path if route["at"].startswith("#") else (self.root / unquote(urlsplit(route["at"]).path)).resolve()
                    if r.path.resolve() == target and r.id != conclusion.id:
                        incoming.append(f"proof owner for {conclusion.id} ({route['name']})")
            for owner, relation in self.relations:
                if r.id in relation["from"] + relation["to"]:
                    incoming.append(f"{relation['kind']}: [{', '.join(relation['from'])}] → [{', '.join(relation['to'])}] (owner {owner.id})")
            superseding = [x.id for x in self.records.values() if r.id in x.data.get("supersedes", [])]
            incoming.extend(f"superseded by {x}" for x in superseding)
            lines.append(f"- {r.id}: {'; '.join(sorted(set(incoming))) if incoming else 'no declared backlinks' }.")
        return "\n".join(lines).rstrip() + "\n"

    def review_summary(self, record, catalog=False):
        summaries = []
        if record.legacy and record.type == "result":
            passages = []
            for field in ("evidence", "independent_audits"):
                values = record.data.get(field, [])
                values = values if isinstance(values, list) else [values] if values else []
                for value in values:
                    if catalog:
                        source = urlsplit(value)
                        target = value if source.scheme else "../" + quote(unquote(source.path), safe="/")
                        if not source.scheme and source.fragment:
                            target += "#" + quote(unquote(source.fragment), safe="-._~")
                        passages.append(f"{field}: [{value}]({target})")
                    else:
                        passages.append(f"{field}: {value}")
            summaries.extend(passages)
        if record.type != "result":
            return record.data["status"]
        routes = record.data.get("proofs", [])
        summaries.extend(f"{route['name']}: {route['review']['state']}" for route in routes)
        if not routes:
            summaries.append("no recorded proof route")
        return "; ".join(summaries)

    def show(self, identifier):
        self.checked()
        r = self.records.get(identifier) or (self.aliases[identifier][0] if identifier in self.aliases else None)
        if r is None:
            raise ValueError(f"Unknown research ID or alias: {identifier}")
        lines = [f"{r.id} — {r.data['title']}", f"Type: {r.type}", f"Format: {'untyped record' if r.legacy else 'typed record'}", f"Review / activity: {self.review_summary(r)}", f"Location: {self.url(r, catalog=False)}"]
        if identifier in self.aliases:
            destination = "whole untyped document" if r.legacy else self.aliases[identifier][1]
            lines.append(f"Alias {identifier}: {destination}")
        if not r.legacy:
            lines.append(f"Scope: {r.data['scope']}")
        for route in r.data.get("proofs", []):
            lines.append(f"Proof {route['name']}: {route['at']}; joint using [{', '.join(route['using'])}]; review {route['review']}")
        if r.legacy:
            for key in ("dependencies", "applicable_results", "evidence", "independent_audits"):
                if key in r.data:
                    lines.append(f"Recorded {key}: {r.data[key]}")
        for owner, field, targets, group in self._legacy_reference_groups():
            if r.id in targets:
                lines.append(f"Recorded reference from {owner.id}: {field} group [{group}] (navigation only; no synthesized proof route)")
        for owner, relation in sorted(self.relations, key=lambda x: (x[1]["kind"], x[0].id)):
            if r.id in relation["from"] + relation["to"]:
                lines.append(f"{relation['kind']}: [{', '.join(relation['from'])}] → [{', '.join(relation['to'])}] at {self.url(owner, relation['at'], catalog=False)}")
        for other in sorted(self.records.values(), key=lambda x: x.id):
            for route in other.data.get("proofs", []):
                premises = [self.records.get(x) or (self.aliases[x][0] if x in self.aliases else None) for x in route["using"]]
                if any(p and p.id == r.id for p in premises):
                    lines.append(f"Premise of {other.id}: {route['name']} (joint premises [{', '.join(route['using'])}])")
                target = other.path if route["at"].startswith("#") else (self.root / unquote(urlsplit(route["at"]).path)).resolve()
                if target == r.path.resolve() and other.id != r.id:
                    lines.append(f"Owns proof for {other.id}: {route['name']} at {route['at']}")
        return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("validate", "catalog", "show"):
        command = commands.add_parser(name)
        command.add_argument("--root", type=Path, default=argparse.SUPPRESS)
        if name == "catalog":
            command.add_argument("--check", action="store_true")
        elif name == "show":
            command.add_argument("identifier")
    args = parser.parse_args(argv)
    repository = Repository(args.root)
    try:
        if args.command == "validate":
            errors = repository.validate()
            if errors:
                print("\n".join(errors), file=sys.stderr)
                return 1
            print(f"Validated {len(repository.records)} research records (declared structure only).")
        elif args.command == "show":
            print(repository.show(args.identifier), end="")
        else:
            content = repository.catalog()
            target = repository.root / "research/CATALOG.md"
            if not target.resolve().is_relative_to(repository.root):
                raise ValueError("research/CATALOG.md resolves outside the repository")
            if args.check:
                if not target.is_file() or target.read_text(encoding="utf-8") != content:
                    print("research/CATALOG.md is absent or stale; run scripts/research.py catalog", file=sys.stderr)
                    return 1
            else:
                if not target.parent.is_dir():
                    raise ValueError("research directory is missing")
                target.write_text(content, encoding="utf-8")
    except (ValueError, OSError, UnicodeError) as exc:
        print(exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
