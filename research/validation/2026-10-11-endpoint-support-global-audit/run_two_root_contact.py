from pathlib import Path
import datetime
import hashlib
import json
import subprocess

base = Path(__file__).resolve().parent
source = base / 'two-root-contact-target.m2'
start = datetime.datetime.now(datetime.timezone.utc)
attempt = base / 'two-root-contact-attempts' / start.strftime('%Y%m%dT%H%M%S%fZ')
attempt.mkdir(parents=True, exist_ok=False)
snapshot = attempt / source.name
snapshot.write_bytes(source.read_bytes())
command = ['/opt/homebrew/bin/M2', '--script', str(snapshot)]
run = subprocess.run(command, capture_output=True)
(attempt / 'stdout.txt').write_bytes(run.stdout)
(attempt / 'stderr.txt').write_bytes(run.stderr)
record = {
    'status': 'PASS' if run.returncode == 0 and b'PASS_COUNT=14' in run.stdout else 'FAIL',
    'started_at': start.isoformat(),
    'finished_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'command': command,
    'return_code': run.returncode,
    'source_path': str(snapshot.relative_to(base)),
    'source_sha256': hashlib.sha256(snapshot.read_bytes()).hexdigest(),
    'stdout_path': str((attempt / 'stdout.txt').relative_to(base)),
    'stdout_sha256': hashlib.sha256(run.stdout).hexdigest(),
    'stderr_path': str((attempt / 'stderr.txt').relative_to(base)),
    'stderr_sha256': hashlib.sha256(run.stderr).hexdigest(),
    'assertions_expected': 14,
    'scope': 'Independent univariate target-septic two-root contact identities; no global geometric exhaustion asserted by execution.'
}
(attempt / 'execution-record.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'attempt': str(attempt), 'status': record['status'], 'return_code': run.returncode}, indent=2))
print(run.stdout.decode(errors='replace'))
print(run.stderr.decode(errors='replace'))
