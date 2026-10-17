"""Read-only provenance inventory. This script executes no mathematical source."""
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[3]
DEST = Path(__file__).resolve().parent / "endpoint-execution-coverage.json"
NAMES = [
    "2026-10-11-endpoint-a-nonzero-support",
    "2026-10-11-endpoint-support-global-audit",
    "2026-10-11-endpoint-three-common-roots",
    "2026-10-11-three-common-roots-quartic-support",
    "2026-10-11-quintic-endpoint-a-nonzero-local-excess",
    "2026-10-11-quintic-endpoint-factor-audit",
    "2026-10-11-quintic-endpoint-ell-first-jet-audit",
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve(value, folder):
    path = Path(value)
    if path.is_absolute():
        return path
    if str(path).startswith("research/"):
        return BASE / path
    return folder / path


def rel(path):
    return str(path.relative_to(BASE))


def file_info(path, expected=None, recorded_by=None):
    exists = path.is_file()
    actual = digest(path) if exists else None
    return {
        "path": rel(path),
        "exists": exists,
        "bytes_observed": path.stat().st_size if exists else None,
        "sha256_observed": actual,
        "sha256_preexisting_record": expected,
        "preexisting_binding_record": recorded_by,
        "binding_status": (
            "MATCH" if expected is not None and expected == actual
            else "UNBOUND_IN_ATTEMPT_RECORD" if expected is None and exists
            else "MISMATCH_OR_MISSING"
        ),
    }


def classify(code, stderr):
    if code == 0:
        return "completed_exit_zero"
    text = stderr.read_text() if stderr.exists() else ""
    if "assertion failed" in text or "error: FAIL" in text:
        return "actual_assertion_failure"
    return "setup_or_export_failure"


rows = []
all_files = {}
issues = []
duplicate_views = []
source_families = set()
for name in NAMES:
    folder = BASE / "research/validation" / name
    aggregate_path = folder / "execution-record.json"
    aggregate = json.loads(aggregate_path.read_text()) if aggregate_path.exists() else {}
    indexed_bindings = {}
    for entry in aggregate.get("files", []):
        path = resolve(entry["path"], folder)
        indexed_bindings[rel(path)] = (entry["sha256"], rel(aggregate_path))
        if not path.exists() or digest(path) != entry["sha256"]:
            issues.append({"kind": "aggregate_file_binding", "path": rel(path)})
        if path.exists() and "bytes" in entry and path.stat().st_size != entry["bytes"]:
            issues.append({"kind": "aggregate_byte_binding", "path": rel(path)})

    if "executions" in aggregate:
        attempts = [(aggregate_path, row, folder) for row in aggregate["executions"]]
    else:
        attempts = []
        for record in sorted(folder.rglob("*.json")):
            data = json.loads(record.read_text())
            if not record.name.startswith("execution"):
                continue
            if any(isinstance(data.get(k), list) for k in ("attempts", "executions", "captured_executions")):
                continue
            if not any(k in data for k in ("returncode", "return_code", "exit_code")):
                continue
            attempts.append((record, data, record.parent))

    for record, data, attempt_folder in attempts:
        code = data.get("returncode", data.get("return_code", data.get("exit_code")))
        if "source_path" in data:
            source = resolve(data["source_path"], folder)
            out = resolve(data["stdout_path"], folder)
            err = resolve(data["stderr_path"], folder)
            family = folder / "two-root-contact-target.m2"
        else:
            source = resolve(data.get("snapshot", data.get("source")), attempt_folder)
            out = resolve(data.get("stdout", "stdout.txt"), attempt_folder)
            err = resolve(data.get("stderr", "stderr.txt"), attempt_folder)
            family = resolve(data.get("current_source", data.get("source")), attempt_folder)
            if name.endswith("local-excess"):
                family = resolve(aggregate["current_source"], folder)
        source_families.add(rel(family))
        bindings = {}
        for label, path, declared in [
            ("source_snapshot", source, data.get("snapshot_sha256", data.get("source_sha256"))),
            ("stdout", out, data.get("stdout_sha256")),
            ("stderr", err, data.get("stderr_sha256")),
        ]:
            bound_by = rel(record) if declared is not None else None
            if declared is None and rel(path) in indexed_bindings:
                declared, bound_by = indexed_bindings[rel(path)]
            info = file_info(path, declared, bound_by)
            bindings[label] = info
            if info["binding_status"] == "MISMATCH_OR_MISSING":
                issues.append({"kind": "attempt_binding", "path": rel(path), "record": rel(record)})
        rows.append({
            "history": name,
            "record": rel(record),
            "source_family": rel(family),
            "return_code": code,
            "classification": classify(code, err),
            "started_utc": data.get("started_utc", data.get("started_at")),
            "command_recorded": data.get("command"),
            "scope_recorded": data.get("scope", aggregate.get("scope")),
            "bindings": bindings,
        })
    if "attempts" in aggregate:
        duplicate_views.append({"aggregate": rel(aggregate_path), "kind": "attempts_duplicate_per_attempt_records", "rows": len(aggregate["attempts"])})
        for data in aggregate["attempts"]:
            recorded = json.loads(resolve(data["record"], folder).read_text())
            copy = {k: v for k, v in data.items() if k != "record"}
            if copy != recorded:
                issues.append({"kind": "aggregate_attempt_disagreement", "path": data["record"]})
    if "captured_executions" in aggregate:
        duplicate_views.append({"aggregate": rel(aggregate_path), "kind": "captured_executions_duplicate_per_attempt_records", "rows": len(aggregate["captured_executions"])})
        for index, data in enumerate(aggregate["captured_executions"], 1):
            record = folder / f"execution-{index:02d}.json"
            if json.loads(record.read_text()) != data:
                issues.append({"kind": "aggregate_attempt_disagreement", "path": rel(record)})
    for path in sorted(folder.rglob("*")):
        if path.is_file():
            all_files[rel(path)] = {"bytes": path.stat().st_size, "sha256": digest(path)}
    for family in source_families:
        path = BASE / family
        if path.is_file():
            all_files[family] = {"bytes": path.stat().st_size, "sha256": digest(path)}

counts = Counter(row["classification"] for row in rows)
language = Counter("M2" if row["bindings"]["source_snapshot"]["path"].endswith(".m2") else "Python" for row in rows)
unbound = [info["path"] for row in rows for info in row["bindings"].values() if info["binding_status"] == "UNBOUND_IN_ATTEMPT_RECORD"]
local = BASE / "research/validation/2026-10-11-quintic-endpoint-a-nonzero-local-excess/execution-record.json"
local_data = json.loads(local.read_text())
report = {
    "scope": "Read-only provenance and byte inventory; zero mathematical executions or theorem audits performed by this script.",
    "observed_utc": datetime.now(timezone.utc).isoformat(),
    "captured_execution_count": len(rows),
    "captured_languages": dict(language),
    "captured_classifications": dict(counts),
    "logical_source_paths": sorted(source_families),
    "logical_source_path_count": len(source_families),
    "unique_captured_snapshot_hashes": len({row["bindings"]["source_snapshot"]["sha256_observed"] for row in rows}),
    "duplicate_record_views": duplicate_views,
    "separately_named_local_excess_direct_tool_observations": local_data["direct_tool_observations"],
    "direct_tool_observation_caveat": "Five earlier direct tool events are distinct from the four byte-bound replay rows. Full original raw streams are not locally bound; they must remain separately labeled observations.",
    "newly_observed_stream_bindings_not_in_preexisting_records": unbound,
    "issues": issues,
    "attempts": rows,
    "observed_files": [{"path": path, **info} for path, info in sorted(all_files.items())],
    "forthcoming_power_jet_record": "Not included. At inventory time no separate a=b=0 power-jet execution folder was present. The existing power-jet audit note cites the 12-check ell-first-jet record and says no additional mathematical execution was needed.",
}
DEST.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({"record_only": True, "captured_executions": len(rows), "classifications": dict(counts), "logical_source_paths": len(source_families), "observed_files": len(all_files), "issues": issues, "output": rel(DEST)}, indent=2))
