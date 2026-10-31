#!/usr/bin/env python3
"""Check local Markdown links without modifying files or accessing the network.

Usage: python3 scripts/check_markdown_links.py [path ...]
Default: all current tracked and nonignored untracked Markdown files under the repository root.
External URLs are not fetched. Local target existence is checked; --anchors
also checks Markdown heading fragments and explicit HTML anchor IDs.
"""
from __future__ import annotations

import argparse
import html
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]*\]\((<[^>]+>|[^\s)]+)(?:\s+[\"'][^)]*[\"'])?\)")
REFERENCE = re.compile(r"^\s*\[[^\]]+\]:\s*(<[^>]+>|\S+)", re.MULTILINE)
CODE_FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")


def tracked_markdown() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z", "--", "*.md", "*.markdown"],
        cwd=ROOT, capture_output=True, check=True,
    )
    return sorted({ROOT / p.decode() for p in result.stdout.split(b"\0")
                   if p and (ROOT / p.decode()).is_file()})


def visible_lines(source: str) -> list[str]:
    """Blank fenced code while retaining source line numbers."""
    lines = []
    fence = None
    for line in source.splitlines():
        match = CODE_FENCE.match(line)
        if fence:
            if (match and match.group(1)[0] == fence[0]
                    and len(match.group(1)) >= len(fence)
                    and not match.group(2).strip()):
                fence = None
            lines.append("")
        elif match and not (match.group(1)[0] == "`" and "`" in match.group(2)):
            fence = match.group(1)
            lines.append("")
        else:
            lines.append(line)
    return lines


def anchors(path: Path) -> set[str]:
    """GitHub-style heading IDs, including repeated headings and explicit IDs."""
    ids: set[str] = set()
    generated: set[str] = set()

    def add_heading(title: str) -> None:
        title = html.unescape(title)
        title = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", title)
        title = re.sub(r"<[^>]*>", "", title).lower()
        slug = re.sub(r"[^\w\- ]", "", title, flags=re.UNICODE).replace(" ", "-")
        candidate = slug
        occurrence = 0
        while candidate in generated:
            occurrence += 1
            candidate = f"{slug}-{occurrence}"
        generated.add(candidate)
        ids.add(candidate)

    lines = visible_lines(path.read_text(encoding="utf-8"))
    # GitHub front matter is metadata, not a Setext heading or HTML anchor.
    if lines and lines[0] == "---":
        for end in range(1, len(lines)):
            if lines[end] in {"---", "..."}:
                lines[:end + 1] = [""] * (end + 1)
                break
    paragraph: list[str] = []
    for line in lines:
        for tag in re.findall(r"<[^>]+>", line):
            ids.update(re.findall(r'''\b(?:id|name)=["']([^"']+)["']''', tag))
        heading = re.match(r"^ {0,3}#{1,6}\s+(.+?)(?:\s+#+\s*)?$", line)
        if heading:
            add_heading(heading.group(1))
            paragraph = []
        elif re.fullmatch(r" {0,3}(?:=+|-+)\s*", line):
            if paragraph:
                add_heading(" ".join(paragraph))
            paragraph = []
        elif line.strip() and not re.match(r"^(?: {4}|\t| {0,3}(?:>|[-+*] |\d+[.)] |<))", line):
            paragraph.append(line.strip())
        else:
            paragraph = []
    return ids


def check_file(path: Path, check_anchors: bool = False) -> list[str]:
    try:
        source = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"{path.relative_to(ROOT)}: cannot read: {exc}"]
    errors: list[str] = []
    # Avoid false positives from fenced code examples.
    text = "\n".join(visible_lines(source))
    for match in list(LINK.finditer(text)) + list(REFERENCE.finditer(text)):
        raw = match.group(1).strip("<>")
        if raw.startswith(("mailto:", "data:")):
            continue
        parsed = urlsplit(raw)
        if parsed.scheme or parsed.netloc or raw.startswith("//"):
            continue
        target = unquote(parsed.path)
        if not target and not parsed.fragment:
            continue
        if target.startswith("/"):
            # Site-root-relative links are not repository-relative.
            continue
        resolved = (path.parent / target).resolve() if target else path
        if not resolved.is_relative_to(ROOT):
            errors.append(f"{path.relative_to(ROOT)}: target outside repo: {raw}")
        elif not resolved.exists():
            line = text.count("\n", 0, match.start()) + 1
            errors.append(f"{path.relative_to(ROOT)}:{line}: missing {raw}")
        elif check_anchors and parsed.fragment and resolved.suffix in {".md", ".markdown"}:
            line = text.count("\n", 0, match.start()) + 1
            try:
                target_anchors = anchors(resolved)
            except (OSError, UnicodeError) as exc:
                errors.append(f"{path.relative_to(ROOT)}:{line}: cannot read anchor target {raw}: {exc}")
                continue
            if unquote(parsed.fragment) not in target_anchors:
                errors.append(f"{path.relative_to(ROOT)}:{line}: missing anchor {raw}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--anchors", action="store_true", help="also check local Markdown fragments")
    args = parser.parse_args()
    paths = [(ROOT / p).resolve() for p in args.paths] if args.paths else tracked_markdown()
    errors = [err for p in paths for err in check_file(p, args.anchors)]
    for error in errors:
        print(error)
    print(f"Checked {len(paths)} Markdown files; {len(errors)} local-link issues.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
