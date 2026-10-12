"""Record M2 source histories and independently check two Bezout identities."""
from pathlib import Path
from fractions import Fraction
import datetime, hashlib, json, subprocess, time

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
SOURCE=ROOT/'research/computations/verify_session_quintic_endpoint_a_nonzero_local_excess_2026_10_11.m2'
M2='/opt/homebrew/bin/M2'
def digest(data): return hashlib.sha256(data).hexdigest()
def trim(p):
    p=list(p)
    while p and p[-1]==0: p.pop()
    return p
def plus(p,q):
    return trim([(p[j] if j<len(p) else 0)+(q[j] if j<len(q) else 0) for j in range(max(len(p),len(q)))])
def scale(p,c): return trim([c*x for x in p])
def mul(p,q):
    if not p or not q: return []
    r=[Fraction(0)]*(len(p)+len(q)-1)
    for j,x in enumerate(p):
        for k,y in enumerate(q): r[j+k]+=x*y
    return trim(r)
def divrem(p,q):
    p=trim(p);q=trim(q);out=[Fraction(0)]*max(0,len(p)-len(q)+1)
    while p and len(p)>=len(q):
        k=len(p)-len(q);c=p[-1]/q[-1];out[k]=c
        p=plus(p,[Fraction(0)]*k+scale(q,-c))
    return trim(out),p
def xgcd(p,q):
    old_r,r=p,q;old_s,s=[Fraction(1)],[];old_t,t=[],[Fraction(1)]
    while r:
        quot,rem=divrem(old_r,r)
        old_r,r=r,rem
        old_s,s=s,plus(old_s,scale(mul(quot,s),-1))
        old_t,t=t,plus(old_t,scale(mul(quot,t),-1))
    c=1/old_r[-1]
    return scale(old_r,c),scale(old_s,c),scale(old_t,c)
def serial(p): return [str(x) for x in p]

run_records=[]
for name,expected in [('initial-failed-source.m2',1),('second-failed-source.m2',1),('third-failed-source.m2',1),('final-source.m2',0)]:
    p=HERE/name
    if name=='final-source.m2':p.write_bytes(SOURCE.read_bytes())
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    before=time.monotonic()
    result=subprocess.run([M2,'--script',str(p)],cwd=ROOT,capture_output=True,timeout=60)
    elapsed=time.monotonic()-before
    stdout_path=HERE/(p.stem+'.stdout.txt');stderr_path=HERE/(p.stem+'.stderr.txt')
    stdout_path.write_bytes(result.stdout);stderr_path.write_bytes(result.stderr)
    run_records.append({'source':str(p.relative_to(ROOT)),'source_sha256':digest(p.read_bytes()),'command':[M2,'--script',str(p)],'started_utc':started,'elapsed_seconds':elapsed,'exit_code':result.returncode,'expected_exit_code':expected,'stdout':str(stdout_path.relative_to(ROOT)),'stdout_sha256':digest(result.stdout),'stderr':str(stderr_path.relative_to(ROOT)),'stderr_sha256':digest(result.stderr)})
    assert result.returncode==expected,(name,result.stderr.decode())

out=result.stdout.decode()
markers=[line for line in out.splitlines() if line.startswith('PASS ') and not line.startswith('PASS all ')]
assert len(markers)==14
coeffs={}
for line in out.splitlines():
    if line.startswith('COEFF'):
        name,raw=line.split('=',1)
        coeffs[name]=[Fraction(int(x)) for x in raw.strip('()').split(',')]
target=[Fraction(x) for x in [1,-18,126,-432,756,-648,216]]
certificates=[]
for name in ['COEFF4','COEFFMORE']:
    gcd,u,v=xgcd(coeffs['COEFF3'],coeffs[name])
    assert gcd==scale(target,Fraction(1,216))
    u=scale(u,216);v=scale(v,216)
    assert plus(mul(u,coeffs['COEFF3']),mul(v,coeffs[name]))==target
    certificates.append({'left':'COEFF3','right':name,'left_polynomial':serial(coeffs['COEFF3']),'right_polynomial':serial(coeffs[name]),'left_multiplier':serial(u),'right_multiplier':serial(v),'target_D_cubed':serial(target),'identity_verified':True})
cert_path=HERE/'bezout-certificates.json'
cert_path.write_text(json.dumps({'coefficient_order':'ascending powers of q','field':'QQ','certificates':certificates},indent=2)+'\n')
record={'status':'PASS','scope':'Fourteen exact M2 identities and two rational Bezout checks; no universal geometric assertion is inferred from execution alone.','current_source':str(SOURCE.relative_to(ROOT)),'current_source_sha256':digest(SOURCE.read_bytes()),'mathematical_M2_checks':14,'independent_Bezout_identity_checks':2,'M2_checker_sources':1,'source_versions_recorded':4,'recorded_M2_executions':4,'failed_versions_retained':3,'executions':run_records,'bezout_certificate':str(cert_path.relative_to(ROOT)),'bezout_certificate_sha256':digest(cert_path.read_bytes()),'runner_sha256':digest(Path(__file__).read_bytes()),'direct_tool_observations':['313a51 failure','f124b6 failure','7bdfad first pass before coefficient export','e7a1c6 export failure after 14 checks','4b51fe final-source pass']}
(HERE/'execution-record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'M2_checks':14,'Bezout_identity_checks':2,'recorded_runs':4,'failed_versions_retained':3,'source_sha256':record['current_source_sha256']}))
