from pathlib import Path
import hashlib, json, subprocess, datetime, sys

root = Path(__file__).resolve().parents[3]
folder = Path(__file__).resolve().parent
source = root / 'research/computations/verify_session_endpoint_three_common_roots_2026_10_11.m2'
index = len(list(folder.glob('execution-*.json'))) + 1
stem = f'execution-{index:02d}'
raw = source.read_bytes()
(folder / f'{stem}.m2').write_bytes(raw)
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
proc = subprocess.run(['/opt/homebrew/bin/M2', '--script', str(folder / f'{stem}.m2')], capture_output=True, cwd=root)
(folder / f'{stem}.stdout.txt').write_bytes(proc.stdout)
(folder / f'{stem}.stderr.txt').write_bytes(proc.stderr)
record = {'started_utc': started, 'source': str(source.relative_to(root)), 'source_sha256': hashlib.sha256(raw).hexdigest(), 'exit_code': proc.returncode, 'snapshot': f'{stem}.m2', 'stdout': f'{stem}.stdout.txt', 'stderr': f'{stem}.stderr.txt', 'scope': 'Exact univariate U-divides-V support algebra, not an STCI theorem.'}
(folder / f'{stem}.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
print(proc.stdout.decode())
print(proc.stderr.decode())
sys.exit(proc.returncode)
