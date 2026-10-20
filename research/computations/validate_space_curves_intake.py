#!/usr/bin/env python3
"""Check the selective Space Curves import; this does not validate mathematics."""

import hashlib
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / "research/archive/space-curves-2026-10-19"


def main():
    manifest = json.loads((PACKET / "manifest.json").read_text())
    inventory = json.loads((PACKET / "source-artifact-inventory.json").read_text())
    sources = {s["id"]: s for s in manifest["sources"]}
    errors = []
    seen = set()
    counts = dict.fromkeys(sources, 0)
    if len(sources) != 6 or len(inventory) != 6:
        errors.append("Expected six distinct donor inventories")
    for item in manifest["files"]:
        relative = Path(item["destination_path"])
        path = ROOT / relative
        if relative.is_absolute() or not path.resolve().is_relative_to(PACKET):
            errors.append(f"Destination escapes packet: {relative}")
            continue
        if str(relative) in seen:
            errors.append(f"Duplicate destination: {relative}")
        seen.add(str(relative))
        source_id = item["source_id"]
        if source_id not in sources:
            errors.append(f"Unknown donor: {source_id}")
            continue
        counts[source_id] += 1
        expected = PACKET / source_id / item["source_path"]
        if path != expected or not item["copied_verbatim"]:
            errors.append(f"Source mapping mismatch: {relative}")
        if not path.is_file() or path.is_symlink():
            errors.append(f"Missing/nonregular snapshot: {relative}")
            continue
        data = path.read_bytes()
        if len(data) != item["bytes"] or hashlib.sha256(data).hexdigest() != item["sha256"]:
            errors.append(f"Byte/hash mismatch: {relative}")
        if item["source_tracked_at_head"]:
            errors.append(f"Review README's untracked-file statement: {relative}")
    for source_id, source in sources.items():
        if counts[source_id] != source["imported_file_count"]:
            errors.append(f"File count mismatch: {source_id}")
    for source in inventory:
        source_id = source["source_id"]
        if source_id not in sources or source["artifact_count"] != len(source["artifacts"]):
            errors.append(f"Inventory mismatch: {source_id}")
        for artifact in source["artifacts"]:
            relative = str((PACKET / source_id / artifact["path"]).relative_to(ROOT))
            if artifact["imported"] != (relative in seen):
                errors.append(f"Inventory import flag mismatch: {relative}")
            if artifact["imported"]:
                digest = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
                if digest != artifact["sha256"]:
                    errors.append(f"Inventory hash mismatch: {relative}")
    actual = {
        str(p.relative_to(ROOT))
        for source_id in sources
        for p in (PACKET / source_id).rglob("*")
        if p.is_file()
    }
    if actual != seen:
        errors.append(f"Unregistered/missing donor files: {sorted(actual.symmetric_difference(seen))}")
    for error in errors:
        print("ERROR:", error)
    print(f"Checked {len(sources)} donors, {len(seen)} verbatim snapshots; {len(errors)} error(s)")
    print("Checks establish import integrity, not mathematical validity or promotion.")
    return int(bool(errors))


if __name__ == "__main__":
    sys.exit(main())
