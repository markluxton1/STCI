"""Run and preserve the independently named endpoint identity checker."""
from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import subprocess
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
OUT = pathlib.Path(__file__).resolve().parent
SOURCE = ROOT / "research/computations/verify_session_quintic_endpoint_subresultant_2026_10_11.m2"
COMMAND = ["/opt/homebrew/bin/M2", "--script", str(SOURCE)]
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
begin = time.monotonic()
completed = subprocess.run(COMMAND, cwd=OUT, capture_output=True, timeout=60)
(OUT / "stdout.txt").write_bytes(completed.stdout)
(OUT / "stderr.txt").write_bytes(completed.stderr)
record = {
    "scope": "Exact QQ polynomial identities for the supplied endpoint P,R; no parameter exhaustion or STCI theorem.",
    "command": COMMAND,
    "cwd": str(OUT),
    "started_utc": started,
    "elapsed_seconds": time.monotonic() - begin,
    "returncode": completed.returncode,
    "source": str(SOURCE.relative_to(ROOT)),
    "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    "stdout_sha256": hashlib.sha256(completed.stdout).hexdigest(),
    "stderr_sha256": hashlib.sha256(completed.stderr).hexdigest(),
    "pass_marker": "PASS independent endpoint subresultant identities: 18 checks",
}
record["passed"] = completed.returncode == 0 and record["pass_marker"] in completed.stdout.decode()
(OUT / "execution-record.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
print(completed.stdout.decode(), end="")
if completed.stderr:
    print(completed.stderr.decode(), end="")
raise SystemExit(0 if record["passed"] else 1)
