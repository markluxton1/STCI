"""Record every attempt; source snapshots are copies, not new certificates."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import time

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SOURCE = ROOT / 'research/computations/verify_session_quintic_a4_pair_classification_2026_10_11.m2'
previous = sorted(HERE.glob('attempt-*'))
attempt = HERE / f'attempt-{len(previous)+1:02d}'
attempt.mkdir()
data = SOURCE.read_bytes()
snapshot = attempt / SOURCE.name
snapshot.write_bytes(data)
command = ['/opt/homebrew/bin/M2', '--script', str(snapshot)]
started = datetime.now(timezone.utc).isoformat()
t0 = time.monotonic()
run = subprocess.run(command, cwd=attempt, capture_output=True, timeout=60)
elapsed = time.monotonic()-t0
(attempt/'stdout.txt').write_bytes(run.stdout)
(attempt/'stderr.txt').write_bytes(run.stderr)
record = {
    'status': 'PASS' if run.returncode == 0 and b'ALL 15 EXACT CHECKS PASSED' in run.stdout else 'FAIL',
    'started_utc': started, 'exit_code':run.returncode, 'elapsed_seconds':elapsed,
    'source':str(SOURCE.relative_to(ROOT)),
    'source_sha256':hashlib.sha256(data).hexdigest(),
    'snapshot':str(snapshot.relative_to(ROOT)),
    'command':command, 'expected_exact_checks':15,
    'stdout_sha256':hashlib.sha256(run.stdout).hexdigest(),
    'stderr_sha256':hashlib.sha256(run.stderr).hexdigest(),
    'scope':'Exact lattice, conic, automorphism, and center formulas; geometric contraction exhaustion is a separate written proof',
    'source_accounting':'one source; all snapshots and attempts retained',
}
(attempt/'execution-record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
print(run.stdout.decode())
print(run.stderr.decode())
raise SystemExit(0 if record['status']=='PASS' else 1)
