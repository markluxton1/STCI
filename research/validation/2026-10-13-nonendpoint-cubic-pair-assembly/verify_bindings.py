#!/usr/bin/env python3
"""Bind the cubic-pair proof package; this does not rerun mathematical checks."""
from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
DEST = Path(__file__).resolve().parent
started = datetime.now(timezone.utc).isoformat()
issues = []
inspections = []
files = set()

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def bind(path):
    p = ROOT / path
    if not p.is_file():
        issues.append("missing: " + path)
    else:
        files.add(path)
    return p

def check_hash(path, expected, reason):
    p = bind(path)
    actual = digest(p) if p.is_file() else None
    inspections.append({"path": path, "expected": expected,
                        "actual": actual, "reason": reason})
    if actual != expected:
        issues.append("digest mismatch: " + path)

dependencies = [
    "research/notes/2026-10-12-session-nonendpoint-pole-filtration-and-line-jet.md",
    "research/notes/2026-10-12-session-nonendpoint-pole-filtration-and-line-jet-independent-audit.md",
    "research/notes/2026-10-12-session-nonendpoint-residual-factor-and-genus-reduction.md",
    "research/notes/2026-10-12-session-nonendpoint-residual-factor-and-genus-independent-audit.md",
    "research/notes/2026-10-11-session-dp5-a4-intrinsic-pair-classification.md",
    "research/notes/2026-10-11-session-dp5-a4-explicit-model-independent-audit.md",
    "research/notes/2026-10-12-session-nonendpoint-cubic-pair-contact-reduction.md",
]
for path in dependencies:
    bind(path)

frozen = {
    "research/notes/2026-10-12-session-nonendpoint-cubic-contact-symbolics.md":
        "0b85a793349a0a35c6b9f1b3ea0a677d90d2076d14f2f28257ab5b86c1b1fb4c",
    "research/computations/verify_session_nonendpoint_cubic_contact_2026_10_12.m2":
        "c26395b318525b6b531ebc96f91bc9866fbbb186ae9982f79443c2fb7508bd58",
    "research/notes/2026-10-12-session-sparse-heptic-cubic-pair-classification.md":
        "58ceb45611e48755169b78fc9a3b8d666853c705f1d2281a8f6a80a489a96bc8",
    "research/computations/verify_session_sparse_heptic_cubic_pairs_2026_10_12.m2":
        "1e18cdedcd5ed9a4181f6baf21ff5d959ed7e2a9dfcedaf522e546716809fdeb",
    "research/validation/2026-10-12-sparse-heptic-cubic-pair-classification/manifest.json":
        "f31b48dc7dcc8e36307e9fd5c3407675d80bb5ddc375c362987940c7c5b3c2fa",
    "research/validation/2026-10-12-sparse-heptic-cubic-pair-classification/execution-record.json":
        "30ce05de9892a50aa56331f35d9717c411de01b4f346c785c7c0e6c201a0958d",
}
for path, expected in frozen.items():
    check_hash(path, expected, "frozen companion binding")

sparse_dir = ROOT / "research/validation/2026-10-12-sparse-heptic-cubic-pair-classification"
for item in json.loads((sparse_dir / "manifest.json").read_text())["bound_files"]:
    check_hash(item["path"], item["sha256"], "companion manifest")
sparse_record = json.loads((sparse_dir / "execution-record.json").read_text())
for record in sparse_record["records"]:
    for part in ("source", "stdout", "stderr"):
        check_hash(record[part + "_path"], record[part + "_sha256"],
                   "sparse execution " + record["label"] + " " + part)

contact_dir = ROOT / "research/validation/2026-10-12-nonendpoint-cubic-contact"
contact_records = []
for p in sorted(contact_dir.glob("*/execution-record.json")):
    path = p.relative_to(ROOT).as_posix()
    bind(path)
    record = json.loads(p.read_text())
    contact_records.append(record)
    check_hash(p.parent.joinpath(Path(record["source"]).name).relative_to(ROOT).as_posix(),
               record["source_sha256"], "contact execution source")
    for part in ("stdout", "stderr"):
        check_hash(p.parent.joinpath(part + ".txt").relative_to(ROOT).as_posix(),
                   record[part + "_sha256"], "contact execution " + part)
for p in contact_dir.rglob("*"):
    if p.is_file():
        bind(p.relative_to(ROOT).as_posix())
for p in sparse_dir.rglob("*"):
    if p.is_file():
        bind(p.relative_to(ROOT).as_posix())
bind(Path(__file__).relative_to(ROOT).as_posix())

if len(contact_records) != 5:
    issues.append("expected five captured contact attempts")
if [r["exit_code"] for r in contact_records] != [1, 1, 1, 1, 0]:
    issues.append("contact execution history mismatch")
if [r["observed_pass_markers"] for r in contact_records] != [0, 6, 7, 8, 10]:
    issues.append("contact supporting-marker history mismatch")
if len(sparse_record["records"]) != 7:
    issues.append("expected seven captured sparse attempts")
if [r["exit_code"] for r in sparse_record["records"]] != [1, 1, 0, 0, 0, 0, 0]:
    issues.append("sparse execution history mismatch")

manifest = {
    "schema": "stci-file-binding-manifest-v1",
    "scope": "new owner cubic-pair exclusion and its two supporting checker lineages",
    "mathematical_acceptance": "independent geometric audit outstanding",
    "bound_files": [{"path": path, "sha256": digest(ROOT / path)}
                    for path in sorted(files) if (ROOT / path).is_file()],
}
(DEST / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
owner = "research/notes/2026-10-12-session-nonendpoint-cubic-pair-contact-reduction.md"
result = {
    "status": "PASS_RECORD_BINDING" if not issues else "FAIL_RECORD_BINDING",
    "started_utc": started,
    "finished_utc": datetime.now(timezone.utc).isoformat(),
    "scope": "file integrity and captured execution history; no mathematical verifier rerun",
    "owner_sha256": digest(ROOT / owner),
    "manifest_sha256": digest(DEST / "manifest.json"),
    "bound_file_count": len(manifest["bound_files"]),
    "digest_comparison_count": len(inspections),
    "checker_lineages": 2,
    "captured_contact_attempts": 5,
    "captured_sparse_attempts": 7,
    "failed_captured_attempts": 6,
    "successful_captured_attempts": 6,
    "mathematical_verifier_reruns": 0,
    "issues": issues,
    "inspections": inspections,
}
(DEST / "result.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({k: v for k, v in result.items() if k != "inspections"}, indent=2))
raise SystemExit(1 if issues else 0)
