"""Capture exact G=J=0 profile proof source, certificates and failed drafts."""
from pathlib import Path
import datetime, hashlib, json, subprocess, time
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
SOURCE=ROOT/'research/computations/verify_session_nonendpoint_GJ_zero_profile_exclusion_2026_10_12.m2'
def digest(data):return hashlib.sha256(data).hexdigest()
failed_names=[
    ('failed-exploratory-source.m2','Exploratory normalization coefficient export failed before resetting polynomial-ring variables.'),
    ('failed-profile-source.m2','Exploratory profile loop used protected/reserved profile syntax.'),
    ('failed-certificate-list-source.m2','Exploratory certificate generator concatenated a Sequence and List.'),
    ('failed-certificate-lift-source.m2','Exploratory certificate generator used unsupported lift(Matrix,Matrix).'),
    ('failed-checker-coefficient-source.m2','Checker draft attempted coefficient extraction in a fraction field.'),
    ('failed-checker-multivariable-coefficient-source.m2','Checker draft extracted a multivariate monomial coefficient instead of a univariate coefficient over its parameter ring.'),
    ('failed-checker-reserved-dd-source.m2','Checker draft used the protected M2 variable dd for the modulus.')
]
items=[(name,HERE/name,1,scope) for name,scope in failed_names]+[
    ('scratch-normalized-quintic.m2',Path('/private/tmp/stci_nonendpoint_GJ0_normalized.m2'),0,'Exploratory exact normalization factorization.'),
    ('scratch-saturated-21-profiles.m2',Path('/private/tmp/stci_nonendpoint_GJ0_21profiles.m2'),0,'Exploratory 21-profile saturation; superseded by unsaturated polynomial Bezout certificates.'),
    ('scratch-inverse-variable-certificates.m2',Path('/private/tmp/stci_nonendpoint_GJ0_certificate_probe.m2'),0,'Exploratory inverse-variable polynomial certificates; every inverse-variable coefficient is zero.'),
    ('final-source.m2',SOURCE,0,'Accepted exact checker: ten structural checks and twenty-one unsaturated polynomial Bezout certificate identities.')
]
executions=[]
for name,original,expected,scope in items:
    snapshot=HERE/name
    source_bytes=original.read_bytes()
    snapshot.write_bytes(source_bytes)
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    before=time.monotonic()
    cmd=['/opt/homebrew/bin/M2','--script',str(snapshot)]
    result=subprocess.run(cmd,cwd=ROOT,capture_output=True,timeout=60)
    stdout=HERE/(snapshot.stem+'.stdout.txt')
    stderr=HERE/(snapshot.stem+'.stderr.txt')
    stdout.write_bytes(result.stdout)
    stderr.write_bytes(result.stderr)
    executions.append({'source':str(snapshot.relative_to(ROOT)),
        'source_sha256':digest(source_bytes),'original_source':str(original),
        'scope':scope,'command':cmd,'started_utc':started,
        'elapsed_seconds':time.monotonic()-before,'exit_code':result.returncode,
        'expected_exit_code':expected,'stdout':str(stdout.relative_to(ROOT)),
        'stdout_sha256':digest(result.stdout),'stderr':str(stderr.relative_to(ROOT)),
        'stderr_sha256':digest(result.stderr)})
    assert result.returncode==expected,(name,result.stderr.decode())
lines=result.stdout.decode().splitlines()
structural=[line for line in lines if line.startswith('PASS ') and not line.startswith(('PASS profile ','PASS all '))]
profiles=[line for line in lines if line.startswith('PASS profile ')]
certificates=[line for line in lines if line.startswith('CERTIFICATE ')]
assert (len(structural),len(profiles),len(certificates))==(10,21,21)
certificate_file=HERE/'twenty-one-polynomial-bezout-certificates.txt'
certificate_file.write_text('\n'.join(certificates)+'\n')
record={'status':'PASS','mathematical_audit_status':'pending independent audit',
    'scope':'Complete G=J=0 nonendpoint projection subfamily exclusion over algebraically closed characteristic-zero fields, conditional on the written full-support and center-avoidance geometry. Does not exclude the entire nonendpoint family or solve STCI.',
    'current_source':str(SOURCE.relative_to(ROOT)),
    'current_source_sha256':digest(SOURCE.read_bytes()),
    'accepted_mathematical_checker_sources':1,'accepted_structural_checks':10,
    'accepted_polynomial_bezout_certificates':21,
    'certificate_file':str(certificate_file.relative_to(ROOT)),
    'certificate_file_sha256':digest(certificate_file.read_bytes()),
    'failed_source_versions_retained':len(failed_names),
    'successful_exploratory_sources':3,'recorded_M2_executions':len(executions),
    'executions':executions,'runner_sha256':digest(Path(__file__).read_bytes()),
    'direct_tool_observations':[
        '2946ef saturated 21-profile exploratory pass',
        'a20e58 certificate Sequence/List API failure',
        'c47877 unsupported lift(Matrix,Matrix) failure',
        'a988f4 inverse-variable certificates multiply to 1',
        '20a81a printed certificate vectors; inverse coefficient always zero',
        '3b317a draft fraction-field coefficient failure',
        '612099 draft multivariate coefficient assertion failure',
        'a9173d protected dd variable failure after seven structural groups',
        'a28019 final ten structural plus twenty-one polynomial certificate pass'
    ]}
(HERE/'execution-record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','accepted_structural_checks':10,
    'accepted_polynomial_bezout_certificates':21,
    'failed_versions_retained':len(failed_names),'executions':len(executions),
    'source_sha256':record['current_source_sha256'],
    'certificate_file_sha256':record['certificate_file_sha256']}))
