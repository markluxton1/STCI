#!/usr/bin/env python3
"""Validate canonical STCI result/question metadata without external packages."""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
RECORDS = [ROOT / "research/results", ROOT / "research/questions"]
RESULT_STATUS = {"proved", "exact_reduction", "conditional", "needs_audit", "disputed", "superseded"}
QUESTION_STATUS = {"open", "conditional", "resolved", "superseded"}
KINDS = {"theorem", "lemma", "reduction", "certificate"}

def metadata(path):
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---\n") or "\n---\n" not in content[4:]:
        return None
    front = content.split("\n---\n", 1)[0][4:]
    fields = {}
    current = None
    for line in front.splitlines():
        match = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if match:
            current = match.group(1)
            value = match.group(2).strip()
            fields[current] = [] if value == "" else value.strip('"')
        elif current and line.lstrip().startswith("- "):
            if not isinstance(fields[current], list):
                fields[current] = []
            fields[current].append(line.strip()[2:].strip('"'))
    return fields

def main():
    errors = []
    records = {}
    paths = [p for d in RECORDS for p in d.glob("*.md") if metadata(p) is not None]
    for path in paths:
        data = metadata(path)
        rid = data.get("id")
        if not rid or not re.fullmatch(r"STCI-[RQ]-\d{4}", rid):
            errors.append(f"{path}: missing/invalid ID")
            continue
        if rid in records:
            errors.append(f"{path}: duplicate ID {rid}")
        records[rid] = (path, data)
        result = rid.startswith("STCI-R-")
        if (result and path.parent.name != "results") or (not result and path.parent.name != "questions"):
            errors.append(f"{path}: ID/location mismatch")
        if data.get("status") not in (RESULT_STATUS if result else QUESTION_STATUS):
            errors.append(f"{path}: invalid status")
        if result and data.get("kind") not in KINDS:
            errors.append(f"{path}: invalid kind")
        if result and data.get("status") == "proved":
            if not data.get("evidence") or not data.get("accepted_in"):
                errors.append(f"{path}: proved claim missing evidence or acceptance")
    for rid, (path, data) in records.items():
        for field in ("dependencies", "applicable_results", "supersedes", "superseded_by"):
            value = data.get(field, [])
            if isinstance(value, str):
                value = [] if value == "[]" else [value]
            for target in value:
                if target not in records:
                    errors.append(f"{path}: unknown {field} ID {target}")
        for field in ("evidence", "independent_audits"):
            value = data.get(field, [])
            if isinstance(value, str):
                value = [] if value == "[]" else [value]
            for target in value:
                if target.startswith("http"):
                    continue  # Remote branch evidence is not validated here.
                if target and not (ROOT / target).exists():
                    errors.append(f"{path}: missing {field} path {target}")
    for error in errors:
        print("ERROR:", error)
    print(f"Checked {len(records)} canonical records; {len(errors)} error(s)")
    return int(bool(errors))

if __name__ == "__main__":
    sys.exit(main())
