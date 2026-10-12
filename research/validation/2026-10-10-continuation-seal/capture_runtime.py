#!/usr/bin/env python3
"""Capture read-only runtime probes, separately from mathematical executions."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TARGET = HERE / "resume-runtime-observation.json"
if TARGET.exists():
    raise SystemExit("Refusing to overwrite the fixed resume runtime observation.")
commands = [
    ["git", "log", "-1", "--format=%H%n%s"],
    ["/opt/homebrew/bin/M2", "--version"],
    ["/private/tmp/stci-cas-venv/bin/python", "-c",
     "import importlib.util, json, os, sys; print(json.dumps({"
     "'executable': sys.executable, 'resolved_executable': os.path.realpath(sys.executable), "
     "'version': sys.version, 'sympy_available': importlib.util.find_spec('sympy') is not None}))"],
]
rows = []
for command in commands:
    started = datetime.now(timezone.utc).isoformat()
    clock = time.monotonic()
    proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                          timeout=15, check=False)
    rows.append({"command": command, "cwd": str(ROOT), "started_utc": started,
                 "elapsed_seconds": time.monotonic() - clock,
                 "exit_code": proc.returncode, "stdout": proc.stdout,
                 "stderr": proc.stderr})
result = {
    "observed_utc": datetime.now(timezone.utc).isoformat(),
    "scope": "Read-only HEAD, version and module-discovery probes; no mathematical verifier",
    "capture_source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "mathematical_execution_count": 0,
    "observations": rows,
}
TARGET.write_text(json.dumps(result, indent=2) + "\n")
print(f"Captured {len(rows)} read-only runtime probes; no mathematical verifier executed.")
raise SystemExit(0 if all(r["exit_code"] == 0 for r in rows) else 1)
