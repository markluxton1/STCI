"""Isolated root replay of the actual endpoint local algebra certificate."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import time

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SOURCE = ROOT / "research/computations/verify_session_endpoint_local_ade_2026_10_10.m2"
SNAPSHOT = HERE / "snapshot"
SNAPSHOT.mkdir(exist_ok=True)
source_bytes = SOURCE.read_bytes()
copy = SNAPSHOT / SOURCE.name
copy.write_bytes(source_bytes)
command = ["/opt/homebrew/bin/M2", "--script", str(copy)]
observed = datetime.now(timezone.utc).isoformat()
start = time.monotonic()
run = subprocess.run(command, cwd=SNAPSHOT, capture_output=True, timeout=60)
elapsed = time.monotonic() - start
(HERE / "stdout.txt").write_bytes(run.stdout)
(HERE / "stderr.txt").write_bytes(run.stderr)
passed = run.returncode == 0 and b"endpoint-local-ADE exact identities: 16" in run.stdout
manifest = {
    "status": "PASS" if passed else "FAIL",
    "timestamp_utc": observed,
    "source": str(SOURCE.relative_to(ROOT)),
    "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
    "snapshot": str(copy.relative_to(ROOT)),
    "snapshot_sha256": hashlib.sha256(copy.read_bytes()).hexdigest(),
    "command": command,
    "cwd": str(SNAPSHOT),
    "exit_code": run.returncode,
    "elapsed_seconds": elapsed,
    "expected_exact_identities": 16,
    "stdout_sha256": hashlib.sha256(run.stdout).hexdigest(),
    "stderr_sha256": hashlib.sha256(run.stderr).hexdigest(),
    "scope": "Exact full local equation, factorization and Cartan identities; geometric coverage is a separate proof",
    "source_accounting": "one replay of the existing original source; copied bytes add no mathematical verifier",
}
(HERE / "execution-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
print(json.dumps(manifest, indent=2))
raise SystemExit(0 if passed else 1)
