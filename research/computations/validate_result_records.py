#!/usr/bin/env python3
"""Validate canonical result metadata and local evidence paths.

Run at repository root: python research/computations/validate_result_records.py
Requires PyYAML (pip install pyyaml). No network or computer algebra required.
Historical GitHub URLs are resolved to their local research/ paths where present;
this verifies availability, not the validity of a historical branch URL.
"""
from pathlib import Path
import re
import sys
from urllib.parse import urlparse
try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = Path(__file__).resolve().parents[2]
INDEX = ROOT / "research/results/INDEX.md"
REQUIRED = {"id","title","kind","status","scope","statement","dependencies",
            "evidence","independent_audits","accepted_in","legacy_ids",
            "supersedes","superseded_by","limitations"}
KINDS = {"theorem","lemma","reduction","certificate"}
STATUSES = {"proved","exact_reduction","conditional","needs_audit","disputed","superseded"}
errors = []
warnings = []
entries = re.findall(r"\[STCI-R-(\d{4})[^\]]*\]\(([^)]+\.md)\)", INDEX.read_text())
records = {}
def check_source(value, record, field):
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{record}: empty/non-string {field} reference")
        return
    if value.startswith("https://github.com/"):
        u = urlparse(value)
        match = re.match(r"/markluxton1/STCI/blob/.+?/(research/.+)", u.path)
        if not match:
            warnings.append(f"{record}: external/unrecognized source {value}")
            return
        target = ROOT / match.group(1)
        warnings.append(f"{record}: historical-branch URL should be stabilized: {value}")
    else:
        target = ROOT / value
    if not target.is_file():
        errors.append(f"{record}: missing {field} target {value}")

for number, relative in entries:
    ident = "STCI-R-" + number
    path = ROOT / "research/results" / relative
    if not path.is_file():
        errors.append(f"{ident}: index target missing {path}")
        continue
    text = path.read_text()
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        errors.append(f"{ident}: missing YAML front matter")
        continue
    try:
        obj = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        errors.append(f"{ident}: invalid YAML: {exc}")
        continue
    if not isinstance(obj, dict):
        errors.append(f"{ident}: YAML root is not a mapping")
        continue
    if ident in records:
        errors.append(f"{ident}: duplicate index ID")
    records[ident] = obj
    if obj.get("id") != ident:
        errors.append(f"{ident}: metadata ID mismatch {obj.get('id')}")
    for key in sorted(REQUIRED - set(obj)):
        errors.append(f"{ident}: missing field {key}")
    if obj.get("kind") not in KINDS:
        errors.append(f"{ident}: invalid kind")
    if obj.get("status") not in STATUSES:
        errors.append(f"{ident}: invalid status")
    if not isinstance(obj.get("scope"), dict):
        errors.append(f"{ident}: scope must be mapping")
    for key in ("dependencies","evidence","independent_audits","legacy_ids","supersedes","superseded_by","limitations"):
        if not isinstance(obj.get(key), list):
            errors.append(f"{ident}: {key} must be list")
    for key in ("evidence","independent_audits"):
        for value in obj.get(key, []) if isinstance(obj.get(key), list) else []:
            check_source(value, ident, key)
    if obj.get("accepted_in"):
        check_source(obj["accepted_in"], ident, "accepted_in")
    else:
        warnings.append(f"{ident}: no recorded acceptance")
    if obj.get("status") == "proved" and not obj.get("evidence"):
        errors.append(f"{ident}: proved record has no evidence")
    if obj.get("status") == "proved" and not obj.get("independent_audits"):
        warnings.append(f"{ident}: proved record has no listed independent audit")

if len(entries) != 36:
    errors.append(f"Expected 36 index entries; found {len(entries)}")
expected = {"STCI-R-%04d" % n for n in range(1,37)}
for missing in sorted(expected - set(records)):
    errors.append(f"Missing canonical record: {missing}")
graph = {}
for ident, obj in records.items():
    deps = obj.get("dependencies", [])
    graph[ident] = deps if isinstance(deps, list) else []
    for dep in graph[ident]:
        if dep not in records:
            errors.append(f"{ident}: unresolved dependency {dep}")
    for key in ("supersedes","superseded_by"):
        for dep in obj.get(key, []) if isinstance(obj.get(key), list) else []:
            if dep.startswith("STCI-R-") and dep not in records:
                errors.append(f"{ident}: unresolved {key} ID {dep}")
visited, active = set(), set()
def visit(node):
    if node in active:
        errors.append(f"Dependency cycle through {node}")
        return
    if node in visited:
        return
    active.add(node)
    for dep in graph.get(node, []):
        if dep in graph:
            visit(dep)
    active.remove(node)
    visited.add(node)
for node in graph:
    visit(node)
print(f"Checked {len(records)} result records; {len(errors)} errors; {len(warnings)} warnings")
for error in errors:
    print("ERROR:", error)
for warning in warnings:
    print("WARN:", warning)
sys.exit(1 if errors else 0)
