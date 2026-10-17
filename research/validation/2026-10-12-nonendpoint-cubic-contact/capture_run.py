from pathlib import Path
import subprocess, hashlib, json, datetime

root = Path('/Users/markluxton/Projects/STCI')
src = root/'research/computations/verify_session_nonendpoint_cubic_contact_2026_10_12.m2'
now = datetime.datetime.now(datetime.timezone.utc)
out = root/'research/validation/2026-10-12-nonendpoint-cubic-contact'/now.strftime('%Y%m%dT%H%M%S%fZ')
out.mkdir(parents=True)
copy = out/src.name
copy.write_bytes(src.read_bytes())
start = datetime.datetime.now(datetime.timezone.utc)
command = ['/opt/homebrew/bin/M2', '--script', str(copy)]
p = subprocess.run(command, cwd=root, capture_output=True)
end = datetime.datetime.now(datetime.timezone.utc)
(out/'stdout.txt').write_bytes(p.stdout)
(out/'stderr.txt').write_bytes(p.stderr)
sha = lambda data: hashlib.sha256(data).hexdigest()
record = {
    'status': 'PASS' if p.returncode == 0 and b'PASS ALL: 10' in p.stdout else 'FAIL',
    'exit_code': p.returncode,
    'source': str(src.relative_to(root)),
    'source_sha256': sha(copy.read_bytes()),
    'command': command,
    'start_utc': start.isoformat(),
    'end_utc': end.isoformat(),
    'stdout_sha256': sha(p.stdout),
    'stderr_sha256': sha(p.stderr),
    'observed_pass_markers': sum(line.startswith(b'PASS ') and b'PASS ALL' not in line for line in p.stdout.splitlines()),
    'intended_supporting_condition_count': 10,
    'scope': 'Supporting cubic-restriction/contact identities only; no parameter-space exhaustion',
}
(out/'execution-record.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps({'folder': str(out.relative_to(root)), **record}, indent=2))
print(p.stdout.decode())
print(p.stderr.decode())
