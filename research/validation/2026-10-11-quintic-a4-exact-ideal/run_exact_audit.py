"""Capture exact M2 outputs; preserve earlier scaffold versions and observations.

This is a stdlib-only evidence runner. It does not count copied/reconstructed
source versions as new distinct mathematical verifiers. Failed replays are
deliberate captures of the retained source, not fresh mathematical attempts.
"""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import time

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SOURCE = ROOT / "research/computations/verify_session_quintic_a4_exact_ideal_2026_10_11.m2"
M2 = "/opt/homebrew/bin/M2"

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def relative(path):
    return str(path.relative_to(ROOT))

record_path = HERE / "execution-record.json"
if record_path.exists():
    raise SystemExit("Refusing to overwrite the frozen execution record")

attempts = HERE / "attempts"
probe = Path("/private/tmp/stci-quintic-a4-probe.m2").read_text()
(attempts / "10-exploratory-complete-pass.m2").write_text(probe)
before_base = probe.split("baseIdeal =")[0] + "exit 0;\n"
(attempts / "09-exploratory-before-base-pass.m2").write_text(before_base)
before_curve = before_base.split("Eline =")[0] + "exit 0;\n"
(attempts / "08-exploratory-before-curve-pass.m2").write_text(before_curve)
(attempts / "11-complex-index-diagnostic-failure.m2").write_bytes(
    Path("/private/tmp/stci-quintic-a4-resolution-probe.m2").read_bytes())
(attempts / "12-explicit-section-probe-pass.m2").write_bytes(
    Path("/private/tmp/stci-quintic-a4-section-probe.m2").read_bytes())
snapshot = HERE / "snapshot" / SOURCE.name
snapshot.write_bytes(SOURCE.read_bytes())

observed = [
    ("5b5743", 1, "01-resolution-api-failure.m2", "exploratory resolution API failure", 0.571490458),
    ("de025f", 0, "08-exploratory-before-curve-pass.m2", "kernel, degree, singular saturation probe", 0.612083167),
    ("a001ef", 0, "09-exploratory-before-base-pass.m2", "adds quartic/line intersection probe", 0.623185792),
    ("19c633", 0, "10-exploratory-complete-pass.m2", "adds projective base cluster probe", 0.640785792),
    ("a4b241", 1, "02-protected-resolution-failure.m2", "protected resolution variable", 0.523201),
    ("e0926b", 1, "03-precedence-failure.m2", "wrong complex term accessor", 0.5154705),
    ("0485d0", 1, "04-complex-index-failure.m2", "same complex accessor after parentheses repair", 0.518808417),
    ("0477bf", 1, "11-complex-index-diagnostic-failure.m2", "diagnostic confirms Complex uses underscore term access", 0.517777792),
    ("470227", 0, "06-before-explicit-section-pass.m2", "64-condition verifier before adding Q", 0.6309055),
    ("30e76a", 1, "05-section-lift-api-failure.m2", "matrix lift API mismatch", 0.713606583),
    ("addeb0", 0, "12-explicit-section-probe-pass.m2", "exact polynomial quotient and radical support", 0.635732125),
    ("ed7359", 1, "07-section-multiline-failure.m2", "unparenthesized multiline section assignment", 0.644927334),
    ("c7b8fd", 0, None, "final 72-condition verifier console execution", 0.766909541),
]
tool_observations = []
for chunk, code, source_name, purpose, seconds in observed:
    p = snapshot if source_name is None else attempts / source_name
    tool_observations.append({
        "tool_chunk_id": chunk, "exit_code": code,
        "source": relative(p), "source_sha256": sha(p),
        "purpose": purpose, "wall_time_seconds": seconds,
        "evidence_kind": "observed exec_command result; not captured subprocess output",
        "source_reconstruction": (
            "mechanically reconstructed from retained complete exploratory script by deleting later additions"
            if source_name in {"08-exploratory-before-curve-pass.m2", "09-exploratory-before-base-pass.m2"}
            else "retained exact source or frozen exact final snapshot"),
    })

jobs = [
    ("failure-replay-01", attempts / "01-resolution-api-failure.m2", 1),
    ("failure-replay-02", attempts / "02-protected-resolution-failure.m2", 1),
    ("failure-replay-03", attempts / "03-precedence-failure.m2", 1),
    ("failure-replay-04", attempts / "04-complex-index-failure.m2", 1),
    ("failure-replay-05", attempts / "05-section-lift-api-failure.m2", 1),
    ("failure-replay-07", attempts / "07-section-multiline-failure.m2", 1),
    ("final-captured", snapshot, 0),
]
executions = []
for name, source, expected in jobs:
    command = [M2, "--script", str(source)]
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    tick = time.monotonic()
    completed = subprocess.run(command, cwd=HERE, text=False,
                               capture_output=True, timeout=60)
    seconds = time.monotonic()-tick
    stdout_path = HERE / (name+".stdout.log")
    stderr_path = HERE / (name+".stderr.log")
    stdout_path.write_bytes(completed.stdout)
    stderr_path.write_bytes(completed.stderr)
    row = {
        "name": name, "command": command, "cwd": str(HERE),
        "started_utc": started, "wall_time_seconds": seconds,
        "source": relative(source), "source_sha256": sha(source),
        "exit_code": completed.returncode, "expected_exit_code": expected,
        "stdout": relative(stdout_path), "stdout_sha256": sha(stdout_path),
        "stderr": relative(stderr_path), "stderr_sha256": sha(stderr_path),
        "purpose": "capture retained failure" if expected else "capture final mathematical verifier",
    }
    executions.append(row)
    print(name, completed.returncode, f"{seconds:.6f}s", flush=True)
    if completed.returncode != expected:
        raise SystemExit("Unexpected retained source behavior: "+name)

final_stdout = (HERE / "final-captured.stdout.log").read_text()
if "PASS: 72 exact quintic A4 model conditions over QQ" not in final_stdout:
    raise SystemExit("Missing exact final PASS marker")
record = {
    "status": "PASS: exact model audit; every retained failure reproduced",
    "scope": "literal six-cubic dP5 A4 model; not all quintic carriers or projection parameters",
    "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "runtime": subprocess.run([M2,"--version"],capture_output=True,text=True).stdout.strip(),
    "primary_source": relative(SOURCE), "primary_source_sha256": sha(SOURCE),
    "snapshot": relative(snapshot), "snapshot_sha256": sha(snapshot),
    "runner": relative(Path(__file__).resolve()), "runner_sha256": sha(Path(__file__).resolve()),
    "mathematical_conditions": 72,
    "distinct_final_mathematical_verifier_paths": 1,
    "original_tool_executions": tool_observations,
    "captured_executions": executions,
    "explicit_M2_script_executions_in_this_record": len(observed)+len(executions),
    "passing_M2_script_executions_in_this_record": sum(r[1]==0 for r in observed)+sum(r[2]==0 for r in jobs),
    "counting_note": "Version snapshots, probes, failed scaffolds, and replays are disclosed; no copied source is counted as an additional final mathematical verifier. The independent 20-condition local-chart child has its own record and is not included here.",
}
record_path.write_text(json.dumps(record,indent=2)+"\n")
print(record["status"])
