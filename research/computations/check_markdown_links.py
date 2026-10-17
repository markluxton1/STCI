#!/usr/bin/env python3
"""Audit relative Markdown destinations without network or third-party packages.

Usage: python3 research/computations/check_markdown_links.py [--core]
Default scans all tracked Markdown files. --core scans principal navigation docs.
Exit status is nonzero when a local destination is missing.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
CORE = (
    "README.md", "research/INDEX.md", "research/STATE.md",
    "research/FRONTIER.md", "research/AUTHORITY.md",
    "research/MAINTENANCE.md", "research/archive/README.md",
    "research/results/INDEX.md", "research/open/README.md",
    "research/certificates/README.md", "research/computations/README.md",
    "research/ARTIFACT_POLICY.md",
)
LINK = re.compile(r"(?<!!)\[[^\]]*\]\((<[^>]+>|[^)\s]+)(?:\s+[^)]*)?\)")
REFERENCE = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)", re.MULTILINE)
FENCE = re.compile(r"^\s*(?:`{3,}|~{3,})")
INLINE_CODE = re.compile(r"`[^`\n]*`")


def tracked_markdown() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "--", "*.md"], cwd=ROOT,
        stdout=subprocess.PIPE, check=True,
    )
    return [ROOT / p.decode("utf-8", "surrogateescape")
            for p in result.stdout.split(b"\0") if p]


def destinations(text: str):
    in_fence = False
    for line_no, line in enumerate(text.splitlines(), 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = INLINE_CODE.sub("", line)
        for match in LINK.finditer(line):
            yield line_no, match.group(1)
        for match in REFERENCE.finditer(line):
            yield line_no, match.group(1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--core", action="store_true",
                        help="check only the 12 primary navigation documents")
    args = parser.parse_args()
    files = [ROOT / p for p in CORE] if args.core else tracked_markdown()
    errors = []
    count = 0
    for file in files:
        if not file.is_file():
            errors.append(f"{file.relative_to(ROOT)}: missing source file")
            continue
        for line, raw in destinations(file.read_text(encoding="utf-8", errors="replace")):
            raw = raw.strip("<>")
            parsed = urlsplit(raw)
            if parsed.scheme or parsed.netloc or not parsed.path or raw.startswith("#"):
                continue
            if raw.startswith("//"):
                continue
            path = unquote(parsed.path)
            target = (ROOT / path.lstrip("/") if path.startswith("/")
                      else file.parent / path)
            count += 1
            if not target.exists():
                errors.append(f"{file.relative_to(ROOT)}:{line}: {raw}")
    for error in errors:
        print(error)
    print(f"Checked {count} local destinations in {len(files)} Markdown files; "
          f"{len(errors)} missing.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
