"""Save actual execution streams and hashes without external libraries."""

import datetime
import hashlib
import json
import pathlib
import subprocess
import sys
import time

directory = pathlib.Path(__file__).resolve().parent
source = directory / "verify_first_jets.py"
command = [sys.executable, "-B", str(source)]
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
before = time.monotonic()
result = subprocess.run(command, cwd=directory, capture_output=True, timeout=30)
elapsed = time.monotonic()-before
(directory / "stdout.txt").write_bytes(result.stdout)
(directory / "stderr.txt").write_bytes(result.stderr)
parsed = json.loads(result.stdout)
assert result.returncode == 0 and parsed["status"] == "PASS"
record = {
    "status": "PASS", "started_utc": started, "elapsed_seconds": elapsed,
    "command": command, "cwd": str(directory), "returncode": result.returncode,
    "source": str(source), "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "stdout": "stdout.txt", "stdout_sha256": hashlib.sha256(result.stdout).hexdigest(),
    "stderr": "stderr.txt", "stderr_sha256": hashlib.sha256(result.stderr).hexdigest(),
    "exact_checks": parsed["exact_checks"], "scope": parsed["scope"],
}
(directory / "execution-record.json").write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps(record, indent=2))
