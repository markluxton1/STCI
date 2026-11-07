#!/usr/bin/env python3
"""Compatibility entry point for the shared research-record validator."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]


def main():
    sys.path.insert(0, str(ROOT))
    try:
        from scripts.research import Repository
    except ImportError as exc:
        print(f"ERROR: research validator unavailable: {exc}")
        return 1

    repository = Repository(ROOT)
    errors = repository.validate()
    for error in errors:
        print("ERROR:", error)
    print(f"Checked {len(repository.records)} research records; {len(errors)} error(s)")
    return int(bool(errors))


if __name__ == "__main__":
    sys.exit(main())
