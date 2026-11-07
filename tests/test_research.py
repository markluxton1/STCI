"""Behavioral controls for coexistence, typed research, and proof grounding.

Every repository here is synthetic. Passing these tests checks declared
structure, never the truth or completeness of a mathematical proof.
"""
import copy
import contextlib
import io
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/research.py"
sys.path.insert(0, str(ROOT))
spec = importlib.util.spec_from_file_location("scripts.research", SCRIPT)
research = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = research
spec.loader.exec_module(research)

DIRECTORIES = {"result": "results", "argument": "arguments", "framework": "frameworks", "investigation": "investigations"}
PREFIXES = {"result": "R", "argument": "A", "framework": "F", "investigation": "I"}
BODY = """# Synthetic object

## Scope
Over a specified field and fixed family.

## Statement
If the stated hypotheses hold, the claimed conclusion follows.

## Proof
The synthetic proof is included here.

## Review
Reconstruction review of the named route: its exact conditional scope was read.
No scientific certificate was executed. This is a fixture, not source review.

## Limitations
This claim concerns only the specified family.

## Conclusion
The argument concludes within its stated scope.

## Bridges
A possible strategy and its missing implication.

## Question
The mathematical question remains open.

## Findings
The activity is complete but the question remains open.

## Purpose
This framework motivates the activity, which informs its revision.

## Evidence
"""


def route(using=(), state="accepted"):
    return {"name": "local", "at": "#proof", "using": list(using),
            "review": {"state": state, "basis": "reconstructed", "at": "#review"}}


def record(kind="result", number=1, **changes):
    data = {"id": f"STCI-{PREFIXES[kind]}-{number:04d}", "type": kind,
            "title": "Synthetic " + kind, "scope": "#scope"}
    if kind != "result":
        data["status"] = {"argument": "complete", "framework": "in_use", "investigation": "complete"}[kind]
    data.update({"result": {"statement": "#statement", "proofs": [route()]},
                 "argument": {"conclusion": "#conclusion"},
                 "framework": {"bridges": "#bridges"},
                 "investigation": {"question": "#question", "findings": "#findings"}}[kind])
    data.update(changes)
    return data


class ResearchTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        for directory in (*DIRECTORIES.values(), "questions"):
            (self.root / "research" / directory).mkdir(parents=True)
        self.write("research/results/INDEX.md", "# Legacy results\n")

    def write(self, path, content):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        return target

    def put(self, data, body=BODY, path=None):
        if path is None:
            default = f"research/{DIRECTORIES[data['type']]}/{data['id']}"
            path = default + "/index.md" if data["type"] == "investigation" else default + ".md"
        return self.write(path, "---\n" + yaml.safe_dump(data, sort_keys=False) + "---\n\n" + body)

    def errors(self):
        return research.Repository(self.root).validate()

    def valid(self):
        self.assertEqual([], self.errors())

    def invalid(self):
        errors = self.errors()
        self.assertTrue(errors, "Invalid synthetic repository was accepted")
        self.assertTrue(all(isinstance(e, str) and e.strip() for e in errors), errors)

    def run_stdlib_validator(self, command="validate_records.py"):
        path = ROOT / "research/computations" / command
        validator_spec = importlib.util.spec_from_file_location("legacy_record_validator", path)
        validator = importlib.util.module_from_spec(validator_spec)
        validator_spec.loader.exec_module(validator)
        validator.ROOT = self.root
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            status = validator.main()
        return status, output.getvalue()

    def test_legacy_validator_coexists_with_typed_records_and_keeps_legacy_checks(self):
        legacy = self.legacy()
        legacy["dependencies"] = ["typed-result-alias"]
        legacy_path = self.root / "research/results/legacy.md"
        legacy_body = "---\n" + yaml.safe_dump(legacy) + "---\n# Legacy\n"
        legacy_path.write_text(legacy_body)
        self.put(record(aliases={"typed-result-alias": "#statement"}))
        status, output = self.run_stdlib_validator()
        self.assertEqual(0, status, output)
        self.assertIn("Checked 2 research records; 0 error(s)", output)

        # YAML permits quoted keys; detection must use the same YAML parser.
        typed_path = self.root / "research/results/STCI-R-0001.md"
        typed_original = typed_path.read_text()
        typed_path.write_text(typed_original.replace("type: result", '"type": result'))
        status, output = self.run_stdlib_validator()
        self.assertEqual(0, status, output)
        typed_path.write_text(typed_original)

        legacy["dependencies"] = ["STCI-R-9999"]
        legacy_path.write_text("---\n" + yaml.safe_dump(legacy) + "---\n# Legacy\n")
        status, output = self.run_stdlib_validator()
        self.assertNotEqual(0, status)
        self.assertIn("unknown dependencies ID STCI-R-9999", output)
        legacy["dependencies"] = ["typed-result-alias"]
        legacy_path.write_text("---\n" + yaml.safe_dump(legacy) + "---\n# Legacy\n")

        typed_path.write_text(typed_original.replace("type: result", "type: mystery"))
        status, output = self.run_stdlib_validator()
        self.assertNotEqual(0, status)
        self.assertIn("unknown type", output)
        typed_path.write_text(typed_original)

        # Untyped Results reject an overall status just as typed Results do.
        legacy_path.write_text(legacy_path.read_text().replace("kind: theorem", "kind: theorem\nstatus: proved"))
        status, output = self.run_stdlib_validator()
        self.assertNotEqual(0, status)
        self.assertIn("unknown field status", output)

    def test_all_types_and_open_question_in_completed_investigation(self):
        for kind in DIRECTORIES:
            data = record(kind)
            if kind == "framework":
                data["relations"] = [self.relation("motivates", ["STCI-F-0001"], ["STCI-I-0001"])]
                data["aliases"] = {"STCI-Q-0010": "#question"}
            self.put(data)
        self.valid()

    def test_both_compatibility_commands_share_dynamic_validation(self):
        self.legacy()
        self.put(record())
        before = self.snapshot()
        for command in ("validate_records.py", "validate_result_records.py"):
            with self.subTest(command=command):
                status, output = self.run_stdlib_validator(command)
                self.assertEqual(0, status, output)
                self.assertIn("Checked 2 research records; 0 error(s)", output)
        self.assertEqual(before, self.snapshot())
        self.put(record(status="established"))
        for command in ("validate_records.py", "validate_result_records.py"):
            with self.subTest(command=command):
                status, output = self.run_stdlib_validator(command)
                self.assertNotEqual(0, status)
                self.assertIn("unknown field status", output)

    def test_result_output_shows_scoped_route_review(self):
        self.legacy()
        data = record()
        self.put(data)
        self.valid()
        repo = research.Repository(self.root)
        shown = repo.show(data["id"])
        catalog = repo.catalog()
        for output in (shown, catalog):
            self.assertIn("local: accepted", output)
            self.assertNotIn("noncircular grounding:", output)
            for forbidden in ("established", "provisional", "promoted", "canonical", "authority"):
                self.assertNotIn(forbidden, output.lower())
        self.assertNotIn("Status:", shown)
        untyped = repo.show("STCI-R-0090")
        self.assertIn("independent_audits: research/legacy.md", untyped)
        self.assertNotIn("accepted_in", untyped)
        self.assertIn("[research/legacy.md](../research/legacy.md)", catalog)
        self.assertNotIn("status", untyped.lower())
        self.assertNotIn("source label", catalog.lower())
        for state in (None, "provisional", "established", "disputed", "superseded"):
            self.put(record(status=state))
            self.assertTrue(any("unknown field status" in error for error in self.errors()))
        self.put(record())
        data = self.legacy()
        for state in (None, "proved", "conditional", "needs_audit", "superseded"):
            data["status"] = state
            self.write("research/results/legacy.md", "---\n" + yaml.safe_dump(data) + "---\n# Untyped\n")
            self.assertTrue(any("unknown field status" in error for error in self.errors()))
        for key in ("source_status", "source_classification"):
            with self.subTest(field=key):
                self.legacy()
                self.put(record(**{key: "proved"}))
                self.assertTrue(any(f"unknown field {key}" in error for error in self.errors()))
                self.put(record())
                data = {**self.legacy(), key: "proved"}
                self.write("research/results/legacy.md", "---\n" + yaml.safe_dump(data) + "---\n# Untyped\n")
                self.assertTrue(any(f"unknown field {key}" in error for error in self.errors()))

    def test_untyped_review_passage_links_preserve_encoded_paths_and_fragments(self):
        data = self.legacy()
        self.write("research/review # source(1).md", "# Review\nThe exact reviewed passage.\n")
        source = "research/review%20%23%20source%281%29.md#review"
        data["evidence"] = [source]
        data["independent_audits"] = [source]
        self.write("research/results/legacy.md", "---\n" + yaml.safe_dump(data) + "---\n# Untyped\n")
        self.valid()
        catalog = self.write("research/CATALOG.md", research.Repository(self.root).catalog())
        self.assertIn("../research/review%20%23%20source%281%29.md#review", catalog.read_text())
        with patch.object(research.links, "ROOT", self.root):
            self.assertEqual([], research.links.check_file(catalog, True))

    def test_activity_status_vocabularies_remain_unchanged(self):
        self.put(record("framework", relations=[self.relation("motivates", ["STCI-F-0001"], ["STCI-I-0001"])]))
        self.put(record("investigation"))
        for kind, states in research.STATUSES.items():
            for state in states:
                with self.subTest(kind=kind, state=state):
                    data = record(kind, status=state)
                    if kind == "framework":
                        data["relations"] = [self.relation("motivates", ["STCI-F-0001"], ["STCI-I-0001"])]
                    self.put(data)
                    self.valid()
            data = record(kind, status="invalid-activity")
            self.put(data)
            self.invalid()
            data["status"] = next(iter(states))
            if kind == "framework":
                data["relations"] = [self.relation("motivates", ["STCI-F-0001"], ["STCI-I-0001"])]
            self.put(data)

    def test_authoring_templates_instantiate_with_pending_reviews(self):
        for kind, directory in DIRECTORIES.items():
            with self.subTest(kind=kind):
                source = (ROOT / "scripts/templates" / f"{kind}.md").read_text(encoding="utf-8")
                for prefix in PREFIXES.values():
                    source = source.replace(f"STCI-{prefix}-0000", f"STCI-{prefix}-0701")
                self.assertTrue(source.startswith("---\n"))
                front, body = source[4:].split("\n---\n", 1)
                data = yaml.safe_load(front)
                self.assertEqual(kind, data["type"])
                if kind == "result":
                    self.assertNotIn("status", data)
                    self.assertTrue(data["proofs"])
                    self.assertTrue(all(p["review"]["state"] == "pending" for p in data["proofs"]))
                else:
                    self.assertEqual({"argument": "draft", "framework": "proposed",
                                      "investigation": "planned"}[kind], data["status"])
                default = f"research/{directory}/synthetic-template"
                target = default + "/index.md" if kind == "investigation" else default + ".md"
                self.write(target, source)
        self.valid()

    @staticmethod
    def relation(kind, sources, targets, at="#purpose"):
        return {"kind": kind, "from": sources, "to": targets, "at": at}

    def test_schema_controls(self):
        good = record()
        self.put(good)
        self.valid()
        mutations = [(field, None) for field in ("id", "type", "title", "scope", "statement", "proofs")]
        mutations += [("id", "STCI-R-nope"), ("type", "question"), ("status", "proved"),
                      ("title", []), ("scope", {}), ("scope", "#absent"),
                      ("statement", 7), ("proofs", {}), ("proofs", None)]
        for field, value in mutations:
            with self.subTest(field=field, value=value):
                bad = copy.deepcopy(good)
                if value is None:
                    del bad[field]
                else:
                    bad[field] = value
                self.put(bad, path="research/results/STCI-R-0001.md")
                self.invalid()
        self.put(good, body=BODY.replace("Over a specified field and fixed family.", ""))
        self.invalid()
        self.put(good, body=BODY.replace("## Limitations", "## Other qualifications"))
        self.invalid()
        self.put(good)
        self.put(record("argument"), path="research/frameworks/misplaced.md")
        self.invalid()

    def test_new_object_discovery_cannot_hide_malformed_metadata(self):
        data = record("argument")
        path = self.put(data)
        self.valid()
        for content in ("---\ntype: [unterminated\n---\n# Broken\n", "# Missing metadata\n"):
            with self.subTest(content=content):
                path.write_text(content)
                self.invalid()
        self.put(data)
        self.put(record("investigation"), path="research/investigations/wrong-level.md")
        self.invalid()

    def test_navigation_files_remain_prose_but_cannot_hide_records(self):
        for directory in DIRECTORIES.values():
            for name in ("README.md", "INDEX.md"):
                with self.subTest(directory=directory, name=name):
                    path = self.write(f"research/{directory}/{name}", "# Reading routes\nPlain navigation.\n")
                    self.valid()
                    for bad in ("---\nid: [broken\n---\n", "---\ntype: result\n---\n", "id: STCI-R-broken\n"):
                        path.write_text(bad)
                        self.invalid()
                    path.write_text("# Reading routes\nPlain navigation.\n")

    def test_nested_object_locations_and_attachment_boundaries(self):
        self.put(record())
        self.put(record("argument"))
        self.put(record("framework", relations=[self.relation("motivates", ["STCI-F-0001"], ["STCI-I-0001"])]))
        self.put(record("investigation"))
        self.write("research/results/synthetic.support/explanation.md", "# Certificate explanation\nNot an object.\n")
        self.write("research/investigations/STCI-I-0001/notes.md", "# Exploratory notes\nNot an object.\n")
        self.valid()
        for kind, path in (("result", "research/results/nested/claim.md"),
                           ("argument", "research/arguments/nested/development.md"),
                           ("framework", "research/frameworks/nested/strategy.md"),
                           ("investigation", "research/investigations/activity/nested/index.md")):
            with self.subTest(kind=kind):
                misplaced = self.put(record(kind, 2), path=path)
                self.invalid()
                misplaced.unlink()
                self.valid()

    def test_repository_root_must_exist_and_contain_research(self):
        self.valid()
        for root in (self.root / "absent", self.root / "empty"):
            with self.subTest(root=root.name):
                if root.name == "empty":
                    root.mkdir()
                self.assertTrue(research.Repository(root).validate())

    def test_type_specific_fields_and_statuses(self):
        for kind, field in (("argument", "conclusion"), ("framework", "bridges"), ("investigation", "question"), ("investigation", "findings")):
            with self.subTest(kind=kind, field=field):
                data = record(kind)
                if kind == "investigation":
                    self.put(record("framework", relations=[self.relation("motivates", ["STCI-F-0001"], ["STCI-I-0001"])]))
                path = self.put(data)
                self.valid()
                del data[field]
                self.put(data)
                self.invalid()
                path.unlink()
                for p in (self.root / "research/frameworks").glob("*.md"):
                    p.unlink()
        self.put(record(proofs=[]))
        self.valid()
        for kind in ("argument", "framework"):
            path = self.put(record(kind, status="established"))
            self.invalid()
            path.unlink()

    def test_duplicate_keys_ids_and_aliases(self):
        original = record(aliases={"STCI-Q-0010": "#question"})
        path = self.put(original)
        self.valid()
        text = path.read_text()
        path.write_text(text.replace("type: result", "type: result\ntype: result"))
        self.invalid()
        self.put(original)
        duplicate = self.put(original, path="research/results/duplicate.md")
        self.invalid()
        duplicate.unlink()
        other = record(number=2, aliases={"STCI-Q-0010": "#question"})
        self.put(other)
        self.invalid()
        other["aliases"] = {"STCI-R-0001": "#statement"}
        self.put(other)
        self.invalid()
        other["aliases"] = {"STCI-Q-0011": "#absent"}
        self.put(other)
        self.invalid()
        other["aliases"] = {"STCI-Q-0011": "#question"}
        path = self.put(other)
        self.valid()
        text = path.read_text()
        path.write_text(text.replace("  STCI-Q-0011: '#question'", "  STCI-Q-0011: '#question'\n  STCI-Q-0011: '#statement'"))
        self.invalid()

    def test_proof_locations_review_and_linked_support(self):
        good = record()
        self.put(good)
        self.valid()
        alternatives = ["#absent", "research/arguments/absent.md#proof", "https://example.invalid/proof#proof"]
        for at in alternatives:
            with self.subTest(at=at):
                data = copy.deepcopy(good)
                data["proofs"][0]["at"] = at
                self.put(data)
                self.invalid()
        for field, value in (("state", "unknown"), ("at", "#absent"), ("basis", "guess")):
            with self.subTest(review=field):
                data = copy.deepcopy(good)
                data["proofs"][0]["review"][field] = value
                self.put(data)
                self.invalid()
        for missing in ("review", "name", "at", "using"):
            data = copy.deepcopy(good)
            del data["proofs"][0][missing]
            self.put(data)
            self.invalid()
        for missing in ("at", "basis", "state"):
            data = copy.deepcopy(good)
            del data["proofs"][0]["review"][missing]
            self.put(data)
            self.invalid()
        self.put(good, body=BODY.replace("Reconstruction review of the named route: its exact conditional scope was read.\nNo scientific certificate was executed. This is a fixture, not source review.", ""))
        self.invalid()
        self.write("research/results/certificate.txt", "Exact synthetic identity\n")
        self.put(good, body=BODY + "[certificate](certificate.txt)\n")
        self.valid()
        (self.root / "research/results/certificate.txt").unlink()
        self.invalid()
        self.put(record("argument"))
        data = copy.deepcopy(good)
        data["proofs"][0]["at"] = "research/arguments/STCI-A-0001.md#conclusion"
        self.put(data)
        self.valid()
        self.put(record("framework"))
        data["proofs"][0]["at"] = "research/frameworks/STCI-F-0001.md#bridges"
        self.put(data)
        self.invalid()

    def test_unreviewed_proposals_and_malformed_routes(self):
        self.put(record())
        self.valid()
        for proofs in ([], [route(state="pending")], [route(state="disputed")]):
            with self.subTest(proofs=proofs):
                self.put(record(proofs=proofs))
                self.valid()
        for proofs in (["not a route"], [{**route(), "using": {"STCI-R-0001": True}}]):
            with self.subTest(proofs=proofs):
                self.put(record(proofs=proofs))
                self.invalid()

    def test_strict_yaml_and_unknown_fields(self):
        path = self.put(record())
        self.valid()
        unknown = record()
        unknown["statuz"] = "established"
        self.put(unknown)
        self.invalid()
        for front in ("[not, a, mapping]", "!!python/object/apply:os.system ['false']"):
            with self.subTest(front=front):
                path.write_text("---\n" + front + "\n---\n" + BODY)
                self.invalid()
        two = [route(), {**route(), "name": "alternative"}]
        self.put(record(proofs=two))
        self.valid()
        two[1]["name"] = "local"
        self.put(record(proofs=two))
        self.invalid()

    def test_malformed_referenced_type_reports_errors_without_crashing(self):
        self.put(record(number=2))
        self.put(record(proofs=[route(["STCI-R-0002"])]))
        self.valid()
        framework = record("framework")
        self.put(framework)
        self.put(record(proofs=[route(["STCI-F-0001"])]))
        self.invalid()
        for kind in ([], {}):
            with self.subTest(kind=kind):
                malformed = copy.deepcopy(framework)
                malformed["type"] = kind
                self.put(malformed, path="research/frameworks/STCI-F-0001.md")
                self.invalid()
                result = self.cli("validate")
                self.assertNotEqual(0, result.returncode)
                self.assertNotIn("Traceback", result.stdout + result.stderr)

    def test_supersession_requires_scope_bridge_and_result_targets(self):
        self.put(record(number=1))
        replacement = record(number=2, supersedes=["STCI-R-0001"])
        bridge = BODY + "\n## Supersession\nThe synthetic replacement preserves the original scope and corrects the stated conclusion.\n"
        self.put(replacement, body=bridge)
        self.put(record(number=3, proofs=[route(["STCI-R-0001"])]))
        self.valid()
        self.put(replacement)
        self.invalid()
        self.put(record("argument"))
        for targets in (["STCI-R-9999"], ["STCI-A-0001"]):
            with self.subTest(targets=targets):
                self.put(record(number=2, supersedes=targets), body=bridge)
                self.invalid()
        self.put(replacement, body=bridge)
        self.put(record(number=1, supersedes=["STCI-R-0002"]), body=bridge)
        self.invalid()

    def test_path_containment_decoding_and_symlinks(self):
        with tempfile.TemporaryDirectory() as outside:
            external = Path(outside).resolve() / "proof.md"
            external.write_text(BODY)
            (self.root / "escape.md").symlink_to(external)
            self.put(record("argument"))
            (self.root / "inside.md").symlink_to(self.root / "research/arguments/STCI-A-0001.md")
            for at in ("../" + external.parent.name + "/proof.md#proof", "%2e%2e/" + external.parent.name + "/proof.md#proof", "escape.md#proof"):
                with self.subTest(at=at):
                    data = record()
                    data["proofs"][0]["at"] = at
                    self.put(data)
                    self.invalid()

    def test_encoded_proof_review_basis_and_alias_premise(self):
        self.put(record("argument"), path="research/arguments/local proof.md")
        dependency = record(number=2, aliases={"old-local-result": "#statement"})
        self.put(dependency)
        data = record(proofs=[route(["old-local-result"])])
        data["proofs"][0]["at"] = "research/arguments/local%20proof.md#proof"
        data["proofs"][0]["review"]["basis"] = "inherited"
        self.put(data)
        self.valid()
        self.put(record("framework", aliases={"old-local-result": "#bridges"}))
        self.invalid()

    def test_image_proof_support_is_local_and_fenced_examples_are_ignored(self):
        support = self.write("research/results/image support.png", "synthetic image fixture")
        data = record()
        body = BODY + "![support](image%20support.png)\n![remote](https://example.invalid/unfetched.png)\n"
        self.put(data, body=body)
        self.valid()
        support.unlink()
        self.invalid()
        self.put(data, body=BODY + "```markdown\n![example](absent.png)\n```\n")
        self.valid()
        with tempfile.TemporaryDirectory() as outside:
            external = Path(outside).resolve() / "external.png"
            external.write_bytes(b"synthetic")
            (self.root / "research/results/escape.png").symlink_to(external)
            self.put(data, body=BODY + "![escape](escape.png)\n")
            self.invalid()

    def test_grounding_joint_premises_alternatives_and_cycles(self):
        self.put(record(number=1))
        self.put(record(number=2))
        consumer = record(number=3, proofs=[route(["STCI-R-0001", "STCI-R-0002"])])
        self.put(consumer)
        self.valid()
        for premises in ("STCI-R-0001", ["STCI-R-9999"], ["STCI-R-0003"], ["STCI-A-0001"]):
            with self.subTest(premises=premises):
                bad = copy.deepcopy(consumer)
                bad["proofs"][0]["using"] = premises
                self.put(bad)
                self.invalid()
        for proofs in ([], [route(state="pending")], [route(state="disputed")]):
            self.put(record(number=2, proofs=proofs))
            self.put(consumer)
            self.invalid()
        self.put(record(number=2))
        self.put(record(number=1, proofs=[route(["STCI-R-0003"])]))
        self.put(consumer)
        self.invalid()
        consumer["proofs"].append({**route(["STCI-R-0002"]), "name": "independent"})
        self.put(consumer)
        self.valid()
        consumer["proofs"][1]["review"]["state"] = "pending"
        self.put(consumer)
        self.invalid()
        self.put(record(number=1))
        self.put(consumer)
        self.valid()  # An unchecked alternative does not invalidate the accepted route.
        self.put(record(number=2, proofs=[route(state="pending")]))
        consumer["proofs"][1] = {**route(), "name": "independent"}
        self.put(consumer)
        self.assertTrue(any("accepted route 'local' lacks noncircular accepted prerequisites" in error
                            for error in self.errors()))
        consumer["proofs"][0]["review"]["state"] = "pending"
        self.put(consumer)
        self.valid()

    def test_research_relations_cycles_groups_ownership_and_motivation(self):
        motivation = self.relation("motivates", ["STCI-F-0001", "STCI-F-0002"], ["STCI-I-0001"])
        framework = record("framework", relations=[motivation])
        self.put(framework)
        self.put(record("framework", 2))
        investigation = record("investigation", relations=[self.relation("informs", ["STCI-I-0001"], ["STCI-F-0001"])])
        self.put(investigation)
        self.valid()
        for field, value in (("from", []), ("to", []), ("from", "STCI-F-0001"), ("to", ["STCI-R-0001"]), ("kind", "implies"), ("at", "#absent")):
            with self.subTest(field=field, value=value):
                bad = copy.deepcopy(framework)
                bad["relations"][0][field] = value
                self.put(bad)
                self.invalid()
        self.put(record("framework"))
        self.invalid()  # Complete investigations still require motivation.
        self.put(framework)
        self.put(record(relations=[motivation]))
        self.invalid()  # The Result is not incident to this edge.

    def test_relation_vocabulary_and_owner_local_passage(self):
        self.put(record("framework", relations=[self.relation("motivates", ["STCI-F-0001"], ["STCI-I-0001"])]))
        self.put(record("investigation"))
        self.put(record("argument"))
        examples = (("uses", ["STCI-R-0001"], ["STCI-A-0001", "STCI-F-0001", "STCI-I-0001"]),
                    ("produces", ["STCI-I-0001"], ["STCI-R-0001", "STCI-A-0001"]),
                    ("informs", ["STCI-R-0001", "STCI-A-0001"], ["STCI-F-0001"]),
                    ("limits", ["STCI-R-0001"], ["STCI-F-0001", "STCI-I-0001"]))
        for kind, sources, targets in examples:
            with self.subTest(kind=kind):
                edge = self.relation(kind, sources, targets)
                self.put(record(relations=[edge]))
                self.valid()
                edge["at"] = "research/arguments/STCI-A-0001.md#purpose"
                self.put(record(relations=[edge]))
                self.invalid()
                edge["at"] = "#purpose"
                edge["from"] = ["STCI-F-0001"]
                self.put(record(relations=[edge]))
                self.invalid()

    def test_grouped_relations_and_aliases_cannot_repeat_endpoints(self):
        self.put(record("framework", aliases={"strategy-alias": "#bridges"}))
        self.put(record("argument"))
        edge = self.relation("uses", ["STCI-R-0001"], ["STCI-F-0001", "STCI-A-0001"])
        self.put(record(relations=[edge]))
        self.valid()
        self.put(record(relations=[edge, copy.deepcopy(edge)]))
        self.invalid()
        for targets in (["STCI-F-0001", "STCI-F-0001"], ["STCI-F-0001", "strategy-alias"]):
            with self.subTest(targets=targets):
                self.put(record(relations=[self.relation("uses", ["STCI-R-0001"], targets)]))
                self.invalid()
        self.put(record(number=2, aliases={"premise-alias": "#statement"}))
        self.put(record(proofs=[route(["premise-alias"])]))
        self.valid()
        self.put(record(proofs=[route(["STCI-R-0002", "premise-alias"])]))
        self.invalid()

    def legacy(self):
        data = {"id": "STCI-R-0090", "title": "Legacy conditional fact", "kind": "theorem",
                "scope": {"characteristic": "zero", "curve": "fixed smooth curve", "hypotheses": ["The stated assumption"]},
                "statement": "Original statement.", "limitations": ["Only the specified setting"],
                "evidence": ["research/legacy.md"], "dependencies": [],
                "independent_audits": ["research/legacy.md"], "legacy_ids": [], "supersedes": [], "superseded_by": []}
        self.write("research/legacy.md", "# Legacy evidence\nOriginal source review.\n")
        self.write("research/results/INDEX.md", "# Results\n[STCI-R-0090](legacy.md)\n")
        self.write("research/results/legacy.md", "---\n" + yaml.safe_dump(data) + "---\n# Legacy\n")
        return data

    def test_untyped_union_source_passages_and_no_synthesized_route(self):
        self.legacy()
        self.put(record("framework", aliases={"STCI-Q-0010": "#question"}, relations=[self.relation("limits", ["STCI-R-0090"], ["STCI-F-0001"]) ]))
        self.valid()
        before = (self.root / "research/results/legacy.md").read_bytes()
        shown = research.Repository(self.root).show("STCI-R-0090")
        self.assertIn("Recorded independent_audits: ['research/legacy.md']", shown)
        self.assertIn("STCI-Q-0010", research.Repository(self.root).show("STCI-Q-0010"))
        self.assertEqual(before, (self.root / "research/results/legacy.md").read_bytes())
        self.put(record(proofs=[route(["STCI-R-0090"])]))
        self.invalid()
        self.put(record(proofs=[route(["STCI-R-0090"], state="pending")]))
        self.valid()
        self.put(record(number=90))
        self.invalid()

    def test_explicit_reviewed_routes_ground_across_both_result_formats(self):
        untyped = self.legacy()
        path = self.root / "research/results/legacy.md"

        def write_untyped():
            path.write_text("---\n" + yaml.safe_dump(untyped) + "---\n" + BODY)

        untyped["proofs"] = [route()]
        write_untyped()
        self.put(record(proofs=[route([untyped["id"]])]))
        self.valid()
        repo = research.Repository(self.root)
        shown = repo.show(untyped["id"])
        self.assertIn("local: accepted", shown)
        self.assertIn("Premise of STCI-R-0001", shown)
        self.assertIn("STCI-R-0090: local; joint premises []", repo.catalog())
        for proofs in (None, [], [route(state="pending")], [route(state="disputed")]):
            with self.subTest(untyped_proofs=proofs):
                if proofs is None:
                    untyped.pop("proofs", None)
                else:
                    untyped["proofs"] = proofs
                write_untyped()
                self.invalid()  # Evidence/audit lists do not create an accepted route.

        self.put(record())
        untyped["proofs"] = [route(["STCI-R-0001"])]
        write_untyped()
        self.valid()
        self.assertIn("Premise of STCI-R-0090", research.Repository(self.root).show("STCI-R-0001"))
        for state in ("pending", "disputed"):
            self.put(record(proofs=[route(state=state)]))
            self.invalid()
        self.put(record(proofs=[route([untyped["id"]])]))
        self.invalid()  # A cross-format cycle cannot ground itself.
        untyped["proofs"].append({**route(), "name": "independent"})
        write_untyped()
        self.valid()

    def test_untyped_explicit_routes_use_same_proof_and_review_checks(self):
        untyped = self.legacy()
        path = self.root / "research/results/legacy.md"

        def put_untyped(proofs):
            untyped["proofs"] = proofs
            path.write_text("---\n" + yaml.safe_dump(untyped) + "---\n" + BODY)

        self.put(record("argument"))
        proof = route()
        proof["at"] = "research/arguments/STCI-A-0001.md#proof"
        put_untyped([proof])
        self.valid()
        self.assertIn("Owns proof for STCI-R-0090", research.Repository(self.root).show("STCI-A-0001"))
        for proofs in ({}, ["not a route"], [route([untyped["id"]])],
                       [{**proof, "at": "#absent"}], [{**proof, "review": {"state": "accepted", "at": "#review"}}]):
            with self.subTest(proofs=proofs):
                put_untyped(proofs)
                self.invalid()
        put_untyped([proof])
        untyped["accepted_in"] = "research/legacy.md"
        path.write_text("---\n" + yaml.safe_dump(untyped) + "---\n" + BODY)
        self.assertTrue(any("unknown field accepted_in" in error for error in self.errors()))

    def test_reviewed_proof_in_existing_untyped_exposition_grounds_consumer(self):
        untyped = self.legacy()
        proof = route()
        proof["at"] = "research/synthesis/source.md#proof"
        untyped["proofs"] = [proof]
        self.write("research/results/legacy.md", "---\n" + yaml.safe_dump(untyped) + "---\n" + BODY)
        source = self.write("research/synthesis/source.md", "# Existing mathematical exposition\n\n## Proof\nComplete synthetic argument for the exact stated scope.\n")
        consumer = record(proofs=[route([untyped["id"]])])
        self.put(consumer)
        self.valid()
        self.assertIn("local: accepted", research.Repository(self.root).show(consumer["id"]))
        for location in ("research/synthesis/missing.md#proof", "research/synthesis/source.md#absent",
                         "research/synthesis/source.md", "https://example.invalid/proof.md#proof"):
            with self.subTest(location=location):
                untyped["proofs"][0]["at"] = location
                self.write("research/results/legacy.md", "---\n" + yaml.safe_dump(untyped) + "---\n" + BODY)
                self.invalid()
        untyped["proofs"][0]["at"] = "research/synthesis/source.md#proof"
        self.write("research/results/legacy.md", "---\n" + yaml.safe_dump(untyped) + "---\n" + BODY)
        source.write_text("# Exposition\n\n## Proof\n\n## Scope\nSpecified family.\n")
        self.invalid()
        source.write_text("# Exposition\n\n## Proof\nComplete synthetic argument.\n")
        self.valid()

        for kind, fragment in (("result", "#proof"), ("framework", "#bridges"), ("investigation", "#findings")):
            with self.subTest(typed_owner=kind):
                owner = record(kind, number=2)
                owner_path = self.put(owner)
                if kind == "investigation":
                    self.put(record("framework", number=2, relations=[self.relation("motivates", ["STCI-F-0002"], ["STCI-I-0002"])]))
                untyped["proofs"][0]["at"] = owner_path.relative_to(self.root).as_posix() + fragment
                self.write("research/results/legacy.md", "---\n" + yaml.safe_dump(untyped) + "---\n" + BODY)
                self.assertTrue(any("proof at cannot use another typed" in error for error in self.errors()))

    def test_malformed_legacy_indexed_records_do_not_disappear(self):
        self.legacy()
        self.valid()
        path = self.root / "research/results/legacy.md"
        original = path.read_text()
        for bad in (original.replace("kind: theorem", "kind: banana"), original.replace("kind: theorem", "kind: theorem\nstatus: proved"),
                    "---\nid: [unterminated\n---\n", "# No metadata\n"):
            with self.subTest(bad=bad[:70]):
                path.write_text(bad)
                self.invalid()
        path.write_text(original)
        self.write("research/questions/question.md", "---\nid: STCI-Q-0001\ntitle: Legacy question\nstatus: open\napplicable_results: [STCI-R-0090]\nevidence: [research/legacy.md]\n---\n# Question\n")
        self.valid()
        self.write("research/questions/question.md", "---\nid: STCI-Q-0001\nstatus: invented\n---\n# Question\n")
        self.invalid()

    def test_legacy_required_fields_and_index_consistency(self):
        legacy = self.legacy()
        self.valid()
        for field in legacy:
            with self.subTest(field=field):
                bad = copy.deepcopy(legacy)
                del bad[field]
                self.write("research/results/legacy.md", "---\n" + yaml.safe_dump(bad) + "---\n# Legacy\n")
                self.invalid()
        self.legacy()
        self.write("research/results/INDEX.md", "# Results\n[STCI-R-0091](legacy.md)\n")
        self.invalid()

    def test_legacy_question_required_fields(self):
        self.legacy()
        question = {"id": "STCI-Q-0001", "title": "Original open question", "status": "open",
                    "applicable_results": ["STCI-R-0090"], "evidence": ["research/legacy.md"]}
        self.write("research/questions/question.md", "---\n" + yaml.safe_dump(question) + "---\n# Question\n")
        self.valid()
        for field in question:
            with self.subTest(field=field):
                bad = copy.deepcopy(question)
                del bad[field]
                self.write("research/questions/question.md", "---\n" + yaml.safe_dump(bad) + "---\n# Question\n")
                self.invalid()

    def test_legacy_index_locators_and_dynamic_union(self):
        self.legacy()
        self.put(record(number=91))
        valid_index = "# Results\n[STCI-R-0090](legacy.md)\n[STCI-R-0091](STCI-R-0091.md)\n"
        index = self.write("research/results/INDEX.md", valid_index)
        self.valid()
        self.write("research/elsewhere.md", "# Not a result record location\n")
        for locator in ("https://example.invalid/legacy.md", "../../../../escape.md", "../elsewhere.md", "missing.md"):
            with self.subTest(locator=locator):
                index.write_text(f"# Results\n[STCI-R-0090]({locator})\n[STCI-R-0091](STCI-R-0091.md)\n")
                self.invalid()
        for text in ("", "# Empty results index\n"):
            index.write_text(text)
            self.invalid()
        index.unlink()
        self.invalid()
        index.write_text(valid_index)
        self.valid()

    def test_legacy_whole_document_aliases_resolve_without_synthesized_routes(self):
        legacy = self.legacy()
        legacy["legacy_ids"] = ["inherited-old-id"]
        path = self.write("research/results/legacy.md", "---\n" + yaml.safe_dump(legacy) + "---\n# Legacy\n")
        self.put(record(proofs=[route(["inherited-old-id"], state="pending")]))
        self.valid()
        shown = research.Repository(self.root).show("inherited-old-id")
        self.assertIn("STCI-R-0090", shown)
        self.assertIn("whole untyped document", shown.lower())
        self.assertIn("research/results/legacy.md", shown)
        self.assertNotIn("research/results/legacy.md#", shown)
        self.assertFalse(any(line.startswith("Proof ") for line in shown.splitlines()))
        self.put(record(proofs=[route(["inherited-old-id"])]))
        self.invalid()
        self.put(record())
        for aliases in (["STCI-R-0001"], ["STCI-R-0090"]):
            with self.subTest(aliases=aliases):
                legacy["legacy_ids"] = aliases
                path.write_text("---\n" + yaml.safe_dump(legacy) + "---\n# Legacy\n")
                self.invalid()
        legacy["legacy_ids"] = ["inherited-old-id"]
        path.write_text("---\n" + yaml.safe_dump(legacy) + "---\n# Legacy\n")
        self.put(record(aliases={"inherited-old-id": "#statement"}))
        self.invalid()
        self.put(record())
        second = copy.deepcopy(legacy)
        second["id"] = "STCI-R-0092"
        self.write("research/results/second.md", "---\n" + yaml.safe_dump(second) + "---\n# Second\n")
        self.write("research/results/INDEX.md", "# Results\n[STCI-R-0090](legacy.md)\n[STCI-R-0092](second.md)\n")
        self.invalid()

    def test_untyped_reference_cycles_are_navigation_and_only_proof_routes_ground(self):
        legacy = self.legacy()
        second = copy.deepcopy(legacy)
        second["id"] = "STCI-R-0092"
        second["dependencies"] = ["STCI-R-0090"]
        self.write("research/results/second.md", "---\n" + yaml.safe_dump(second) + "---\n# Second\n")
        self.write("research/results/INDEX.md", "# Results\n[STCI-R-0090](legacy.md)\n[STCI-R-0092](second.md)\n")
        self.valid()
        for premises in (["STCI-R-0090"], ["STCI-R-0092"]):
            with self.subTest(premises=premises):
                legacy["dependencies"] = premises
                self.write("research/results/legacy.md", "---\n" + yaml.safe_dump(legacy) + "---\n# Legacy\n")
                self.valid()
        self.assertIn("recorded references (dependencies)", research.Repository(self.root).catalog())
        legacy["proofs"] = [route([second["id"]])]
        second["proofs"] = [route([legacy["id"]])]
        for data, filename in ((legacy, "legacy.md"), (second, "second.md")):
            self.write("research/results/" + filename, "---\n" + yaml.safe_dump(data) + "---\n" + BODY)
        self.invalid()  # Accepted routes cannot ground one another circularly.
        second["proofs"].append({**route(), "name": "independent"})
        self.write("research/results/second.md", "---\n" + yaml.safe_dump(second) + "---\n" + BODY)
        self.valid()
        self.assertIn("local: accepted", research.Repository(self.root).show(legacy["id"]))

    def test_catalog_links_encode_legal_filenames_and_detect_missing_targets(self):
        target = self.put(record(), path="research/results/local # proof(1).md")
        self.valid()
        expected = research.Repository(self.root).catalog()
        catalog = self.write("research/CATALOG.md", expected)
        self.assertIn("local%20%23%20proof%281%29.md", expected)
        with patch.object(research.links, "ROOT", self.root):
            self.assertEqual([], research.links.check_file(catalog, True))
            target.unlink()
            self.assertTrue(research.links.check_file(catalog, True))
        self.assertNotEqual(0, self.cli("catalog", "--check").returncode)

    def test_inherited_backlinks_resolve_aliases_without_inventing_routes(self):
        legacy = self.legacy()
        self.put(record(number=1, aliases={"old-premise": "#statement"}))
        self.put(record(number=2))
        self.put(record(number=3))
        legacy["dependencies"] = ["old-premise", "STCI-R-0002"]
        self.write("research/results/legacy.md", "---\n" + yaml.safe_dump(legacy) + "---\n# Legacy\n")
        question = {"id": "STCI-Q-0001", "title": "Inherited question", "status": "open",
                    "applicable_results": ["STCI-R-0001", "STCI-R-0002"], "evidence": ["research/legacy.md"]}
        self.write("research/questions/question.md", "---\n" + yaml.safe_dump(question) + "---\n# Question\n")
        self.valid()
        before = self.snapshot()
        repo = research.Repository(self.root)
        for target in ("STCI-R-0001", "old-premise", "STCI-R-0002"):
            with self.subTest(target=target):
                shown = repo.show(target)
                for consumer in ("STCI-R-0090", "STCI-Q-0001"):
                    inherited = [line for line in shown.splitlines() if consumer in line]
                    self.assertTrue(inherited, shown)
                    self.assertTrue(all("recorded" in line.lower() for line in inherited), inherited)
        unrelated = repo.show("STCI-R-0003")
        self.assertNotIn("STCI-R-0090", unrelated)
        self.assertNotIn("STCI-Q-0001", unrelated)
        old_shown = repo.show("STCI-R-0090")
        self.assertIn(str(legacy["dependencies"]), old_shown)
        self.assertFalse(any(line.startswith("Proof ") for line in old_shown.splitlines()))
        catalog = repo.catalog()
        self.assertIn("## Untyped questions", catalog)
        self.assertIn("[old-premise → STCI-R-0001, STCI-R-0002]", catalog)
        backlinks = catalog.split("## Object backlinks", 1)[1]
        for target in ("STCI-R-0001", "STCI-R-0002"):
            line = next(line for line in backlinks.splitlines() if line.startswith(f"- {target}:"))
            self.assertIn("STCI-R-0090", line)
            self.assertIn("STCI-Q-0001", line)
            self.assertIn("recorded", line.lower())
        line = next(line for line in backlinks.splitlines() if line.startswith("- STCI-R-0003:"))
        self.assertNotIn("STCI-R-0090", line)
        self.assertNotIn("STCI-Q-0001", line)
        self.assertEqual(before, self.snapshot())

    def cli(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.root), *args], capture_output=True, text=True)

    def snapshot(self):
        return {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}

    def test_catalog_determinism_staleness_and_read_only_cli(self):
        self.put(record(number=2))
        self.put(record(number=1))
        repo = research.Repository(self.root)
        expected = repo.catalog()
        self.assertEqual(expected, repo.catalog())
        original_glob = Path.glob
        def reverse_glob(path, pattern, *args, **kwargs):
            return iter(reversed(list(original_glob(path, pattern, *args, **kwargs))))
        with patch.object(Path, "glob", reverse_glob):
            self.assertEqual(expected, research.Repository(self.root).catalog())
        self.assertLess(expected.index("STCI-R-0001"), expected.index("STCI-R-0002"))
        before = self.snapshot()
        for args in (("validate",), ("show", "STCI-R-0001")):
            with self.subTest(args=args):
                result = self.cli(*args)
                self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual(before, self.snapshot())
        self.assertNotEqual(0, self.cli("show", "STCI-R-9999").returncode)
        self.assertEqual(0, self.cli("catalog").returncode)
        catalog = self.root / "research/CATALOG.md"
        self.assertEqual(expected, catalog.read_text())
        self.assertEqual(0, self.cli("catalog", "--check").returncode)
        catalog.write_text(expected + "\nStale edit.\n")
        before = self.snapshot()
        self.assertNotEqual(0, self.cli("catalog", "--check").returncode)
        self.assertEqual(before, self.snapshot())
        self.put(record(status="unknown"))
        self.assertNotEqual(0, self.cli("validate").returncode)


if __name__ == "__main__":
    unittest.main()
