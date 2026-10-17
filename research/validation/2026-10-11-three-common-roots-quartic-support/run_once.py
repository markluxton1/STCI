"""Capture one exact independent M2 certificate without rewriting prior runs."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SOURCE = ROOT / "research/computations/verify_session_three_common_roots_residual_quartic_2026_10_11.m2"
RECORD = HERE / "execution-record.json"
if RECORD.exists():
    raise SystemExit("Refusing to overwrite the captured execution record")
SNAPSHOT = HERE / SOURCE.name
shutil.copyfile(SOURCE, SNAPSHOT)
started = datetime.now(timezone.utc).isoformat()
before = time.monotonic()
command = ["/opt/homebrew/bin/M2", "--script", str(SNAPSHOT)]
result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
elapsed = time.monotonic() - before
(HERE / "stdout.txt").write_text(result.stdout)
(HERE / "stderr.txt").write_text(result.stderr)
record = {
    "scope": "One-parameter univariate residual-quartic root-support exclusion, characteristic zero; no geometric conclusion",
    "started_utc": started,
    "finished_utc": datetime.now(timezone.utc).isoformat(),
    "elapsed_seconds": elapsed,
    "command": command,
    "cwd": str(ROOT),
    "source": str(SOURCE.relative_to(ROOT)),
    "snapshot": SNAPSHOT.name,
    "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    "snapshot_sha256": hashlib.sha256(SNAPSHOT.read_bytes()).hexdigest(),
    "returncode": result.returncode,
    "checks": 8 if result.returncode == 0 and "CHECKS=8" in result.stdout else None,
    "stdout": "stdout.txt",
    "stderr": "stderr.txt",
    "status": "PASS" if result.returncode == 0 and "CHECKS=8" in result.stdout else "FAIL",
}
RECORD.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
raise SystemExit(result.returncode)
