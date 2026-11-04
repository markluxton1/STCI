#!/usr/bin/env python3
"""Compatibility entry point for validating legacy and typed research records."""
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
    legacy_count = sum(record.legacy for record in repository.records.values())
    print(f"Checked {legacy_count} legacy canonical records; {len(errors)} error(s)")
    return int(bool(errors))


if __name__ == "__main__":
    sys.exit(main())
