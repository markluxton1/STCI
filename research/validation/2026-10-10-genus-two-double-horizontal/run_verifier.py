#!/usr/bin/env python3
"""Record an exact local-algebra companion; failure output is retained."""
import hashlib
import json
from pathlib import Path
import subprocess
import time
from datetime import datetime, timezone

root = Path(__file__).resolve().parents[3]
out = Path(__file__).resolve().parent
source = root / "research/computations/verify_session_genus_two_double_horizontal_2026_10_10.m2"
snapshot = out / "source.m2"
snapshot.write_bytes(source.read_bytes())
command = ["/opt/homebrew/bin/M2", "--script", str(snapshot)]
started = datetime.now(timezone.utc).isoformat()
t0 = time.monotonic()
try:
    result = subprocess.run(command, cwd=out, capture_output=True, timeout=45)
    stdout, stderr = result.stdout, result.stderr
    status = "PASS" if result.returncode == 0 and b"PASS genus-two double-horizontal endpoint identities: 14 checks" in stdout else "FAIL"
    code = result.returncode
except subprocess.TimeoutExpired as error:
    stdout, stderr = error.stdout or b"", error.stderr or b""
    status, code = "TIMEOUT", None
(out / "stdout.txt").write_bytes(stdout)
(out / "stderr.txt").write_bytes(stderr)
record = {
    "status": status,
    "started_utc": started,
    "elapsed_seconds": time.monotonic() - t0,
    "source_path": str(source.relative_to(root)),
    "source_sha256": hashlib.sha256(snapshot.read_bytes()).hexdigest(),
    "command": command,
    "working_directory": str(out),
    "exit_code": code,
    "assertion_count": 14,
    "scope": "Exact polynomial factorization, normality cut, and inverse A3/A5/A7 matrices; geometric resolution and residue arguments are proved in the independent note.",
}
(out / "execution-record.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
if status != "PASS":
    raise SystemExit(1)
