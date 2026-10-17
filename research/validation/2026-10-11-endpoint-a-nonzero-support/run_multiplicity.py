"""Record exact exploratory M2 source, output and process result without theorem flags."""
import datetime
import hashlib
import json
import pathlib
import subprocess
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
OUT = pathlib.Path(__file__).resolve().parent
SOURCE = ROOT / "research/computations/explore_session_endpoint_a_nonzero_multiplicity_2026_10_11.m2"
attempt = OUT / "attempts" / datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
attempt.mkdir(parents=True)
snapshot = attempt / SOURCE.name
snapshot.write_bytes(SOURCE.read_bytes())
command = ["/opt/homebrew/bin/M2", "--script", str(snapshot)]
begin = time.monotonic()
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
try:
    completed = subprocess.run(command, cwd=attempt, capture_output=True, timeout=60)
    stdout, stderr, code = completed.stdout, completed.stderr, completed.returncode
except subprocess.TimeoutExpired as error:
    stdout, stderr, code = error.stdout or b"", error.stderr or b"", None
(attempt / "stdout.txt").write_bytes(stdout)
(attempt / "stderr.txt").write_bytes(stderr)
record = {"scope": "Exploratory exact endpoint a-nonzero polynomial coefficient calculations; no parameter exhaustion or mathematical theorem asserted", "started_utc": started, "elapsed_seconds": time.monotonic()-begin, "command": command, "cwd": str(attempt), "returncode": code, "source": str(SOURCE.relative_to(ROOT)), "snapshot": str(snapshot.relative_to(ROOT)), "source_sha256": hashlib.sha256(snapshot.read_bytes()).hexdigest(), "stdout_sha256": hashlib.sha256(stdout).hexdigest(), "stderr_sha256": hashlib.sha256(stderr).hexdigest()}
(attempt / "execution-record.json").write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps(record, indent=2))
print(stdout.decode(), end="")
print(stderr.decode(), end="")
raise SystemExit(0 if code == 0 else 1)
