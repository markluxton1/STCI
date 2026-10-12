#!/usr/bin/env python3
"""Preserve exact endpoint coefficient execution and its full raw output."""
from pathlib import Path
import hashlib, json, subprocess, datetime, shutil

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SOURCE = ROOT / 'research/computations/verify_session_quintic_endpoint_fiber_coefficients_2026_10_11.m2'
attempts = HERE / 'attempts'
attempts.mkdir(parents=True, exist_ok=True)
serial = 1 + len(list(attempts.glob('*/execution.json')))
destination = attempts / f'{serial:02d}'
destination.mkdir()
copy = destination / SOURCE.name
shutil.copy2(SOURCE, copy)
command = ['/opt/homebrew/bin/M2', '--script', str(copy)]
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
try:
    result = subprocess.run(command, cwd=destination, capture_output=True, text=True, timeout=60)
    exit_code = result.returncode
    stdout, stderr = result.stdout, result.stderr
except subprocess.TimeoutExpired as exc:
    exit_code = None
    stdout, stderr = exc.stdout or b'', exc.stderr or b''
    stdout = stdout.decode() if isinstance(stdout, bytes) else stdout
    stderr = stderr.decode() if isinstance(stderr, bytes) else stderr
(destination / 'stdout.txt').write_text(stdout)
(destination / 'stderr.txt').write_text(stderr)
record = {'scope':'endpoint A4 placement only; coefficient identities, no parameter exhaustion',
          'source':str(SOURCE.relative_to(ROOT)), 'source_sha256':hashlib.sha256(copy.read_bytes()).hexdigest(),
          'command':command, 'started_utc':started, 'exit_code':exit_code,
          'stdout_sha256':hashlib.sha256(stdout.encode()).hexdigest(),
          'stderr_sha256':hashlib.sha256(stderr.encode()).hexdigest()}
(destination / 'execution.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
print(stdout)
print(stderr)
raise SystemExit(0 if exit_code == 0 else 1)
