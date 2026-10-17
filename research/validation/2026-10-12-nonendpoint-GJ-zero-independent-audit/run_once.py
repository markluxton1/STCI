from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import sys

base = Path(__file__).resolve().parent
root = base.parents[2]
source = base/'verify_fraction_certificates.py'
certificates = root/'research/validation/2026-10-12-nonendpoint-GJ-zero-normalized-lead/twenty-one-polynomial-bezout-certificates.txt'
owner_note = root/'research/notes/2026-10-12-session-nonendpoint-GJ-zero-full-support-exclusion.md'
owner_source = root/'research/computations/verify_session_nonendpoint_GJ_zero_profile_exclusion_2026_10_12.m2'
owner_record = root/'research/validation/2026-10-12-nonendpoint-GJ-zero-normalized-lead/execution-record.json'
started = datetime.datetime.now(datetime.timezone.utc)
attempt = base/'attempts'/started.strftime('%Y%m%dT%H%M%S%fZ')
attempt.mkdir(parents=True, exist_ok=False)
snapshot = attempt/source.name
snapshot.write_bytes(source.read_bytes())
cert_snapshot = attempt/'owner-certificate-input.txt'
cert_snapshot.write_bytes(certificates.read_bytes())
command = [sys.executable, str(snapshot), str(cert_snapshot)]
run = subprocess.run(command, capture_output=True)
(attempt/'stdout.txt').write_bytes(run.stdout)
(attempt/'stderr.txt').write_bytes(run.stderr)
try:
    summary = json.loads(run.stdout)
except Exception:
    summary = {}
record = {
    'status':'PASS' if run.returncode==0 and summary.get('status')=='PASS' else 'FAIL',
    'started_utc':started.isoformat(),
    'finished_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'command':command,
    'exit_code':run.returncode,
    'source':str(snapshot.relative_to(root)),
    'source_sha256':hashlib.sha256(snapshot.read_bytes()).hexdigest(),
    'certificate_input':str(cert_snapshot.relative_to(root)),
    'certificate_input_sha256':hashlib.sha256(cert_snapshot.read_bytes()).hexdigest(),
    'stdout':str((attempt/'stdout.txt').relative_to(root)),
    'stdout_sha256':hashlib.sha256(run.stdout).hexdigest(),
    'stderr':str((attempt/'stderr.txt').relative_to(root)),
    'stderr_sha256':hashlib.sha256(run.stderr).hexdigest(),
    'owner_bindings':[
        {'path':str(f.relative_to(root)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()}
        for f in (owner_note,owner_source,owner_record,certificates)
    ],
    'result_summary':{k:v for k,v in summary.items() if k!='check_labels'},
    'scope':'Independent direct Fraction verification of exported polynomial certificate products and actual fiber identities, with no Groebner or saturation computation.'
}
(attempt/'execution-record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'attempt':str(attempt),'status':record['status'],'exit_code':run.returncode,'checks_passed':summary.get('checks_passed')},indent=2))
if run.returncode:
    print(run.stdout.decode(errors='replace'))
    print(run.stderr.decode(errors='replace'))
