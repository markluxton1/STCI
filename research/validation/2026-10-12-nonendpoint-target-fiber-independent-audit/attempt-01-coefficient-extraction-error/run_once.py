from pathlib import Path
import datetime, hashlib, json, subprocess, time

here = Path(__file__).resolve().parent
source = here / 'verify_proof_gaps.m2'
command = ['/opt/homebrew/bin/M2', '--script', str(source)]
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
t0 = time.monotonic()
process = subprocess.run(command, cwd=here, capture_output=True)
elapsed = time.monotonic() - t0
(here / 'stdout.txt').write_bytes(process.stdout)
(here / 'stderr.txt').write_bytes(process.stderr)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
record = {'status': 'PASS' if process.returncode == 0 else 'FAIL',
          'started_utc': started, 'elapsed_seconds': elapsed,
          'command': command, 'cwd': str(here), 'returncode': process.returncode,
          'source': str(source), 'source_sha256': sha(source),
          'stdout': 'stdout.txt', 'stdout_sha256': sha(here / 'stdout.txt'),
          'stderr': 'stderr.txt', 'stderr_sha256': sha(here / 'stderr.txt'),
          'intended_exact_checks': 11,
          'scope': 'Leading coefficients, boundary value, root-count remainder and specialization checks omitted from owner identity assertions; no full-family exclusion'}
(here / 'execution-record.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
print(process.stdout.decode(), end='')
print(process.stderr.decode(), end='')
raise SystemExit(process.returncode)
