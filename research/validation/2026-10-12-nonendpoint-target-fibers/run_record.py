"""Capture one accepted checker and separate exploratory source histories."""
from pathlib import Path
import datetime, hashlib, json, subprocess, time
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
SOURCE=ROOT/'research/computations/verify_session_nonendpoint_target_fibers_2026_10_12.m2'
def digest(data):return hashlib.sha256(data).hexdigest()
items=[
    ('scratch-target-fiber-failed.m2',Path('/private/tmp/stci_nonendpoint_target_fiber.m2'),1,'Exploratory determinant/cubic expansion; unsupported three-argument substitute failed during optional coefficient printing.'),
    ('scratch-target-infinity-factor.m2',Path('/private/tmp/stci_nonendpoint_endpoint_fiber.m2'),0,'Exploratory target-infinity resultant factorization.'),
    ('scratch-target-one-factor.m2',Path('/private/tmp/stci_nonendpoint_z1_fiber.m2'),0,'Exploratory target-one resultant factorization.'),
    ('scratch-GJ-zero-factor.m2',Path('/private/tmp/stci_nonendpoint_GJ0_fiber.m2'),0,'Exploratory forced-a subfamily factorization; full G=J=0 exclusion is not claimed.'),
    ('final-source.m2',SOURCE,0,'Accepted supporting source with seventeen exact identity checks; geometric arguments are separate.')
]
executions=[]
for name,original,expected,scope in items:
    snapshot=HERE/name;snapshot.write_bytes(original.read_bytes())
    started=datetime.datetime.now(datetime.timezone.utc).isoformat();before=time.monotonic()
    result=subprocess.run(['/opt/homebrew/bin/M2','--script',str(snapshot)],cwd=ROOT,capture_output=True,timeout=60)
    stdout=HERE/(snapshot.stem+'.stdout.txt');stderr=HERE/(snapshot.stem+'.stderr.txt')
    stdout.write_bytes(result.stdout);stderr.write_bytes(result.stderr)
    executions.append({'source':str(snapshot.relative_to(ROOT)),'source_sha256':digest(snapshot.read_bytes()),'original_source':str(original),'scope':scope,'command':['/opt/homebrew/bin/M2','--script',str(snapshot)],'started_utc':started,'elapsed_seconds':time.monotonic()-before,'exit_code':result.returncode,'expected_exit_code':expected,'stdout':str(stdout.relative_to(ROOT)),'stdout_sha256':digest(result.stdout),'stderr':str(stderr.relative_to(ROOT)),'stderr_sha256':digest(result.stderr)})
    assert result.returncode==expected,(name,result.stderr.decode())
passed=[line for line in result.stdout.decode().splitlines() if line.startswith('PASS ') and not line.startswith('PASS all ')]
assert len(passed)==17
record={'status':'PASS','scope':'Seventeen exact identities supporting the written finite-fiber reduction and bounded subfamily exclusions; neither universal STCI nor full nonendpoint exclusion.','current_source':str(SOURCE.relative_to(ROOT)),'current_source_sha256':digest(SOURCE.read_bytes()),'accepted_mathematical_checker_sources':1,'accepted_identity_checks':17,'exploratory_sources':4,'failed_exploratory_sources_retained':1,'recorded_M2_executions':len(executions),'executions':executions,'runner_sha256':digest(Path(__file__).read_bytes()),'direct_tool_observations':['7f22ba determinant scratch success','d1927d scratch coefficient-print failure','340939 infinity-resultant scratch success','7c45a1 target-one-resultant scratch success','446305 forced-a factorization scratch success','82b881 forced-a special values scratch success','3aead3 final checker pass']}
(HERE/'execution-record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','accepted_identity_checks':17,'accepted_checker_sources':1,'exploratory_sources':4,'failed_exploratory_sources_retained':1,'source_sha256':record['current_source_sha256']}))
