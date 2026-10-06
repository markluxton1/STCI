#!/usr/bin/env python3
"""Live exact verification runner; records command, exit status, and source hash.

Existing repository sources are not changed. Three generator-driving primitive
checks are run sequentially in the saved isolated repository snapshot.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import hashlib, json, os, subprocess, time
ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
PYTHON = '/private/tmp/stci-cas-venv/bin/python'
M2 = '/opt/homebrew/bin/M2'
ENV = {**os.environ, 'PYTHONDONTWRITEBYTECODE':'1', 'PATH':'/opt/homebrew/bin:'+os.environ.get('PATH','')}
ISOLATED = OUT/'isolated'
listing=json.loads((OUT/'readme-verifier-list.json').read_text())
regenerating={'verify_primitive_quadruple_universal.py','verify_primitive_triple_parity.py','verify_primitive_quartic_factor_audit.py'}
ordinary=[name for name in listing['readme_python'] if Path(name).name not in regenerating]
ordinary += ['research/scratch/degree6/verify_mixed45_reduction.py','research/computations/verify_localcoh_finite_principal_parts.m2','research/computations/verify_quadric_powers.m2']
results=[]

def run(source, isolated=False, timeout=1800):
 root=ISOLATED if isolated else ROOT
 command=([M2,'--script'] if source.endswith('.m2') else [PYTHON])+[source]
 log=OUT/(Path(source).stem+'.log')
 started=time.time()
 with log.open('w') as f:
  f.write('Command: '+' '.join(command)+'\nCWD: '+str(root)+'\n\n'); f.flush()
  try:
   done=subprocess.run(command,cwd=root,env=ENV,stdout=f,stderr=subprocess.STDOUT,timeout=timeout)
   status='PASS' if done.returncode==0 else 'FAILED'; code=done.returncode
  except subprocess.TimeoutExpired:
   status='TIMEOUT';code=None
  f.write('\nRunner status: '+status+'\n'); f.flush()
 item={'source':source,'source_sha256':hashlib.sha256((ROOT/source).read_bytes()).hexdigest(),'command':command,'cwd':str(root),'isolated':isolated,'status':status,'exit_code':code,'elapsed_seconds':round(time.time()-started,3),'log':str(log.relative_to(ROOT))}
 print(json.dumps(item),flush=True)
 return item

with ThreadPoolExecutor(max_workers=3) as pool:
 jobs=[pool.submit(run,name) for name in ordinary]
 for job in as_completed(jobs):
  results.append(job.result())
  (OUT/'suite-results.json').write_text(json.dumps(results,indent=2)+'\n')
for name in ['verify_primitive_quadruple_universal.py','verify_primitive_quartic_factor_audit.py','verify_primitive_triple_parity.py']:
 results.append(run('research/computations/'+name,True))
 (OUT/'suite-results.json').write_text(json.dumps(results,indent=2)+'\n')
print('COMPLETE: '+str(len(results))+' source executions.',flush=True)
