#!/usr/bin/env python3
"""Check local Markdown links without modifying files or accessing the network.

Usage: python3 scripts/check_markdown_links.py [path ...]
Default: all tracked Markdown files under the repository root.
External URLs, anchors within documents, and non-Markdown link targets
are not fetched; local target existence is checked.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]*\]\((<[^>]+>|[^\s)]+)(?:\s+[\"'][^)]*[\"'])?\)")
REFERENCE = re.compile(r"^\s*\[[^\]]+\]:\s*(<[^>]+>|\S+)", re.MULTILINE)
CODE_FENCE = re.compile(r"^\s*(```|~~~)")


def tracked_markdown() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "--", "*.md", "*.markdown"],
        cwd=ROOT, capture_output=True, check=True,
    )
    return [ROOT / p.decode() for p in result.stdout.split(b"\0") if p]


def check_file(path: Path) -> list[str]:
    try:
        source = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"{path.relative_to(ROOT)}: cannot read: {exc}"]
    errors: list[str] = []
    # Avoid false positives from fenced code examples.
    active = False
    lines = []
    for line in source.splitlines():
        if CODE_FENCE.match(line):
            active = not active
            lines.append("")
        else:
            lines.append("" if active else line)
    text = "\n".join(lines)
    for match in list(LINK.finditer(text)) + list(REFERENCE.finditer(text)):
        raw = match.group(1).strip("<>")
        if raw.startswith(("#", "mailto:", "data:")):
            continue
        parsed = urlsplit(raw)
        if parsed.scheme or parsed.netloc or raw.startswith("//"):
            continue
        target = unquote(parsed.path)
        if not target:
            continue
        if target.startswith("/"):
            # Site-root-relative links are not repository-relative.
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.is_relative_to(ROOT):
            errors.append(f"{path.relative_to(ROOT)}: target outside repo: {raw}")
        elif not resolved.exists():
            line = text.count("\n", 0, match.start()) + 1
            errors.append(f"{path.relative_to(ROOT)}:{line}: missing {raw}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path)
    args = parser.parse_args()
    paths = [(ROOT / p).resolve() for p in args.paths] if args.paths else tracked_markdown()
    errors = [err for p in paths for err in check_file(p)]
    for error in errors:
        print(error)
    print(f"Checked {len(paths)} Markdown files; {len(errors)} local-link issues.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
