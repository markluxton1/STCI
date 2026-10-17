"""Root-observed replay of the two new independent genus-one companions.

Copies exact source bytes, executes in a separate snapshot cwd, and retains
actual subprocess streams. This certifies identities, not geometric inputs.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import time

record = Path(__file__).resolve().parent
repo = record.parents[2]
snapshot = record / "snapshot"
cases = [
    ("interfaces-211", "research/computations/verify_session_genus_one_211_interfaces_2026_10_10.m2",
     "PASS: 42 exact [211] interface identities over QQ"),
    ("repeated-partitions", "research/validation/2026-10-10-repeated-partitions-independent-audit/countercheck.m2",
     "PASS: 29 independent exact conditions"),
]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
started = datetime.now(timezone.utc).isoformat()
snapshot.mkdir(parents=True, exist_ok=True)
prepared = []
for name, relative, expected in cases:
    source = repo / relative
    copied = snapshot / relative
    copied.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, copied)
    prepared.append((name, relative, copied, expected, sha(source)))

def execute(item):
    name, relative, copied, expected, source_hash = item
    command = ["/opt/homebrew/bin/M2", "--script", str(copied)]
    t0 = time.monotonic()
    process = subprocess.run(command, cwd=snapshot, capture_output=True, timeout=60)
    elapsed = time.monotonic() - t0
    stdout = record / (name + ".stdout.txt")
    stderr = record / (name + ".stderr.txt")
    stdout.write_bytes(process.stdout)
    stderr.write_bytes(process.stderr)
    passed = process.returncode == 0 and expected.encode() in process.stdout
    return {
        "name": name, "source_path": relative, "source_sha256": source_hash,
        "snapshot_source": str(copied.relative_to(repo)), "snapshot_sha256": sha(copied),
        "command": command, "cwd": str(snapshot), "exit_code": process.returncode,
        "elapsed_seconds": elapsed, "expected_terminal_text": expected,
        "status": "PASS" if passed else "FAIL", "stdout_path": str(stdout.relative_to(repo)),
        "stdout_sha256": sha(stdout), "stderr_path": str(stderr.relative_to(repo)),
        "stderr_sha256": sha(stderr),
    }

with ThreadPoolExecutor(max_workers=2) as pool:
    executions = list(pool.map(execute, prepared))
manifest = {
    "started_utc": started, "completed_utc": datetime.now(timezone.utc).isoformat(),
    "status": "PASS" if all(x["status"] == "PASS" for x in executions) else "FAIL",
    "scope": "Isolated exact replay of independent [211] identities and repeated-partition ideal/conductor certificates",
    "does_not_certify": "Geometric interface hypotheses, novelty, genus-two exclusions, or unrestricted STCI",
    "runner_sha256": sha(Path(__file__)), "executions": executions,
    "new_distinct_sources": 2, "new_explicit_executions": 2,
    "historical_97_source_110_execution_index": "unchanged; these replays are additional records",
}
target = record / "execution-manifest.json"
target.write_text(json.dumps(manifest, indent=2) + "\n")
print(manifest["status"] + ": two isolated exact genus-one replays; counts 42 and 29")
raise SystemExit(0 if manifest["status"] == "PASS" else 1)
