#!/usr/bin/env python3
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
import hashlib,json,os,subprocess,time
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
SNAP=OUT/'isolated-additional-2026-10-07'
ENV={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','PATH':'/opt/homebrew/bin:'+os.environ.get('PATH','')}
SOURCES=['research/computations/audit_dx1_saturation_2026_10_07.py','research/computations/verify_session_normal_carrier_progress.py','research/computations/verify_session_normal_independent_audit.py']
def run(source):
 command=['/private/tmp/stci-cas-venv/bin/python',source]
 log=OUT/(Path(source).stem+'_validation_2026_10_07.log')
 started=time.time()
 done=subprocess.run(command,cwd=SNAP,env=ENV,capture_output=True,text=True,timeout=1200)
 log.write_text('Command: '+' '.join(command)+'\nCWD: '+str(SNAP)+'\n\n'+done.stdout+done.stderr)
 item={'source':source,'source_sha256':hashlib.sha256((SNAP/source).read_bytes()).hexdigest(),'command':command,'cwd':str(SNAP),'isolated':True,'status':'PASS' if done.returncode==0 else 'FAILED','exit_code':done.returncode,'elapsed_seconds':round(time.time()-started,3),'log':str(log.relative_to(ROOT))}
 if done.returncode==0 and Path(source).name=='verify_session_normal_carrier_progress.py':
  output=SNAP/'research/computations/session_normal_carrier_progress_2026-10-07.json'
  data=json.loads(done.stdout);output.write_text(done.stdout)
  prior=ROOT/'research/computations/session_normal_carrier_progress_2026-10-07.json'
  item['output_sha256']=hashlib.sha256(output.read_bytes()).hexdigest();item['prior_output_sha256']=hashlib.sha256(prior.read_bytes()).hexdigest();item['output_equal_prior']=data==json.loads(prior.read_text())
 if done.returncode==0 and Path(source).name=='verify_session_normal_independent_audit.py':
  output=SNAP/'research/scratch/session_normal_independent_audit.json';prior=ROOT/'research/scratch/session_normal_independent_audit.json'
  item['output_sha256']=hashlib.sha256(output.read_bytes()).hexdigest();item['prior_output_sha256']=hashlib.sha256(prior.read_bytes()).hexdigest();item['output_equal_prior']=json.loads(output.read_text())==json.loads(prior.read_text())
 if done.returncode==0 and Path(source).name=='audit_dx1_saturation_2026_10_07.py':
  generated=['research/computations/verify_dx1_saturation_2026_10_07.m2','research/computations/dx1_saturation_audit_2026_10_07.json','research/computations/verify_dx1_saturation_2026_10_07.out']
  item['generated_hashes']={p:hashlib.sha256((SNAP/p).read_bytes()).hexdigest() for p in generated}
  item['generated_equal_prior']={p:(SNAP/p).read_bytes()==(ROOT/p).read_bytes() for p in generated if (ROOT/p).exists()}
 print(json.dumps(item),flush=True);return item
results=[]
with ThreadPoolExecutor(max_workers=2) as pool:
 for job in as_completed([pool.submit(run,p) for p in SOURCES]):
  results.append(job.result());(OUT/'additional-results-2026-10-07.json').write_text(json.dumps(results,indent=2)+'\n')
print('COMPLETE: '+str(len(results))+' additional distinct-source executions.',flush=True)
