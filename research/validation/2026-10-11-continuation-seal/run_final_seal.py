#!/usr/bin/env python3
"""Capture one final record-only checker execution; never run mathematics."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
acceptance = "research/notes/2026-10-11-session-all-quartic-results-acceptance.md"
outputs = ["result.json", "execution-manifest.json", "stdout.txt", "stderr.txt"]
if any((HERE / name).exists() for name in outputs):
    raise SystemExit("Refusing to overwrite final seal or captured execution files.")
sha = lambda path: hashlib.sha256(Path(path).read_bytes()).hexdigest()
checker = HERE / "check_record.py"
checker_before = sha(checker)
command = [sys.executable, str(checker), "--seal-once", "--acceptance", acceptance]
started = datetime.now(timezone.utc).isoformat()
tick = time.monotonic()
process = subprocess.run(command, cwd=ROOT, capture_output=True, timeout=60)
elapsed = time.monotonic() - tick
for filename, data in (("stdout.txt", process.stdout), ("stderr.txt", process.stderr)):
    with (HERE / filename).open("xb") as stream:
        stream.write(data)
result = json.loads((HERE / "result.json").read_text()) if (HERE / "result.json").is_file() else None
checker_after = sha(checker)
passed = (process.returncode == 0 and result is not None
          and result["status"] == "PASS" and result["mode"] == "FINAL_SEAL"
          and checker_before == checker_after == result["checker_sha256"])
manifest = {
    "status": "PASS" if passed else "FAIL",
    "scope": "One final record-integrity checker execution; no mathematical verifier executed",
    "mathematical_verifiers_rerun": False,
    "mathematical_execution_count": 0,
    "command": command,
    "cwd": str(ROOT),
    "started_utc": started,
    "completed_utc": datetime.now(timezone.utc).isoformat(),
    "elapsed_seconds": elapsed,
    "exit_code": process.returncode,
    "acceptance": acceptance,
    "runner_sha256": sha(Path(__file__)),
    "checker_before_sha256": checker_before,
    "checker_after_sha256": checker_after,
    "result_sha256": sha(HERE / "result.json") if result is not None else None,
    "stdout_sha256": sha(HERE / "stdout.txt"),
    "stderr_sha256": sha(HERE / "stderr.txt"),
    "check_count": result["check_count"] if result is not None else None,
    "checked_local_links": result["checked_local_links"] if result is not None else None,
    "head_observed": result["head_observed"] if result is not None else None,
    "bound_file_count": len(result["bound_files_sha256"]) if result is not None else None,
    "result_and_manifest_created_exclusively": True,
}
with (HERE / "execution-manifest.json").open("x") as stream:
    stream.write(json.dumps(manifest, indent=2) + "\n")
sys.stdout.buffer.write(process.stdout)
sys.stderr.buffer.write(process.stderr)
raise SystemExit(0 if passed else 1)
