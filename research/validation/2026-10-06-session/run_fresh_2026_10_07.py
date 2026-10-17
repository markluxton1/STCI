#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,os,subprocess,time
from concurrent.futures import ThreadPoolExecutor,as_completed
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent
ENV={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','PATH':'/opt/homebrew/bin:'+os.environ.get('PATH','')}
SOURCES=['research/computations/verify_mf6_infinity_universal.py','research/computations/session_dx1_compact_certificate_2026_10_06.m2','research/computations/verify_session_dx1_independent_2026_10_06.py','research/computations/session_dx1_boundary_2026_10_06.m2']
def run(source):
 cmd=(['/opt/homebrew/bin/M2','--script'] if source.endswith('.m2') else ['/private/tmp/stci-cas-venv/bin/python'])+[source]
 log=OUT/(Path(source).stem+'_2026_10_07.log');start=time.time()
 with log.open('w') as f:
  f.write('Command: '+' '.join(cmd)+'\nCWD: '+str(ROOT)+'\n\n');f.flush()
  result=subprocess.run(cmd,cwd=ROOT,env=ENV,stdout=f,stderr=subprocess.STDOUT,timeout=1200)
 item={'source':source,'source_sha256':hashlib.sha256((ROOT/source).read_bytes()).hexdigest(),'command':cmd,'cwd':str(ROOT),'status':'PASS' if result.returncode==0 else 'FAILED','exit_code':result.returncode,'elapsed_seconds':round(time.time()-start,3),'log':str(log.relative_to(ROOT))};print(json.dumps(item),flush=True);return item
results=[]
with ThreadPoolExecutor(max_workers=2) as pool:
 for job in as_completed([pool.submit(run,p) for p in SOURCES]):
  results.append(job.result());(OUT/'fresh-results-2026-10-07.json').write_text(json.dumps(results,indent=2)+'\n')
print('COMPLETE: '+str(len(results))+' fresh executions.',flush=True)
