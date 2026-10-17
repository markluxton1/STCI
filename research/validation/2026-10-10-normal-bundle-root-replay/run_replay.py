"""Isolated root replay of the new Jacobian normal-bundle certificate."""
from pathlib import Path
import hashlib
import json
import subprocess
import time

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SOURCE = ROOT / "research/computations/verify_session_quartic_normal_bundle_2026_10_10.m2"
SNAPSHOT = HERE / "snapshot"
SNAPSHOT.mkdir(exist_ok=True)
copy = SNAPSHOT / SOURCE.name
source_bytes = SOURCE.read_bytes()
copy.write_bytes(source_bytes)
command = ["/opt/homebrew/bin/M2", "--script", str(copy)]
start = time.monotonic()
run = subprocess.run(command, cwd=SNAPSHOT, capture_output=True, timeout=60)
elapsed = time.monotonic() - start
stdout = HERE / "stdout.txt"
stderr = HERE / "stderr.txt"
stdout.write_bytes(run.stdout)
stderr.write_bytes(run.stderr)
passed = run.returncode == 0 and b"ALL 8 EXACT CHECKS PASSED" in run.stdout
manifest = {
    "status": "PASS" if passed else "FAIL",
    "source": str(SOURCE.relative_to(ROOT)),
    "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
    "snapshot": str(copy.relative_to(ROOT)),
    "snapshot_sha256": hashlib.sha256(copy.read_bytes()).hexdigest(),
    "command": command,
    "cwd": str(SNAPSHOT),
    "exit_code": run.returncode,
    "elapsed_seconds": elapsed,
    "expected_exact_checks": 8,
    "stdout_sha256": hashlib.sha256(run.stdout).hexdigest(),
    "stderr_sha256": hashlib.sha256(run.stderr).hexdigest(),
    "scope": "Jacobian identities and every-point bundle rank; geometric ribbon proof is separate",
    "source_accounting": "one original source, one replay of it; snapshot is not a new verifier",
}
(HERE / "execution-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
print(json.dumps(manifest, indent=2))
raise SystemExit(0 if passed else 1)
