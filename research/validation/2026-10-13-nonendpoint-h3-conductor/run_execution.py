from pathlib import Path
import datetime, hashlib, json, subprocess, time, sys

folder = Path(__file__).resolve().parent
root = folder.parents[2]
source = root / 'research/computations/verify_session_nonendpoint_h3_conductor_2026_10_13.m2'
number = len(list(folder.glob('attempt-*'))) + 1
attempt = folder / f'attempt-{number:02d}'
attempt.mkdir()
snapshot = attempt / source.name
snapshot.write_bytes(source.read_bytes())
command = ['/opt/homebrew/bin/M2', '--script', str(snapshot)]
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
start = time.monotonic()
stdout,stderr = attempt / 'stdout.txt',attempt / 'stderr.txt'
with stdout.open('wb') as out, stderr.open('wb') as err:
    proc = subprocess.run(command, cwd=root, stdout=out, stderr=err)
elapsed = time.monotonic()-start
out_bytes,err_bytes=stdout.read_bytes(),stderr.read_bytes()
record = {'scope':'Exact h3 proportionality identities and a bounded two-parameter actual conductor probe; no global support or admissibility inference.', 'source': str(source.relative_to(root)), 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(), 'snapshot':snapshot.name, 'snapshot_sha256':hashlib.sha256(snapshot.read_bytes()).hexdigest(), 'command':command, 'started_utc':started, 'elapsed_seconds':elapsed, 'exit_code':proc.returncode, 'stdout':'stdout.txt', 'stdout_sha256':hashlib.sha256(out_bytes).hexdigest(), 'stderr':'stderr.txt', 'stderr_sha256':hashlib.sha256(err_bytes).hexdigest(), 'exact_checks':out_bytes.decode().count('PASS ') if proc.returncode==0 else None, 'copy_scope':'One source and one execution snapshot, not two independent implementations.'}
(attempt / 'execution-record.json').write_text(json.dumps(record,indent=2)+'\n')
(folder / 'execution-record.json').write_text(json.dumps({'scope':record['scope'],'latest_attempt':str(attempt.relative_to(folder)), 'latest_record':str((attempt/'execution-record.json').relative_to(folder)), 'exit_code':proc.returncode,'source_sha256':record['source_sha256'],'exact_checks':record['exact_checks']},indent=2)+'\n')
print(json.dumps(record,indent=2))
print(out_bytes.decode())
print(err_bytes.decode())
sys.exit(proc.returncode)
