#!/usr/bin/env python3
"""Freeze and separately replay the owner and independent family checkers."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
SNAPSHOT = OUT/'isolated'
owner = Path('computations/verify_singular_delpezzo_four_A1_family_2026_10_09.py')
independent = Path('research/validation/2026-10-09-four-A1-family-audit/countercheck.py')
owner_note = Path('research/notes/2026-10-09-session-singular-delpezzo-four-A1-family.md')
inputs = (owner,independent,owner_note)
h = lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
hashes = {}
for relative in inputs:
    original,copy = ROOT/relative,SNAPSHOT/relative
    copy.parent.mkdir(parents=True,exist_ok=True)
    data = original.read_bytes()
    if copy.exists():
        assert copy.read_bytes()==data,'Immutable snapshot differs: '+str(relative)
    else:
        copy.write_bytes(data)
    hashes[str(relative)] = h(copy)
assert hashes[str(owner)] == '0e72ced585c9e1135648b5e9a278c09964c6677009f50554aac46a68d3b6cef4'
(SNAPSHOT/'research/scratch').mkdir(parents=True,exist_ok=True)
records = []
environment = dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
for label,source,report in (
    ('owner',owner,Path('research/scratch/session-singular-delpezzo-four-A1-family-2026-10-09.json')),
    ('independent',independent,Path('research/validation/2026-10-09-four-A1-family-audit/countercheck-result.json')),
):
    start=time.monotonic()
    run=subprocess.run([sys.executable,str(SNAPSHOT/source)],cwd=SNAPSHOT,env=environment,
                       stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    log=OUT/(label+'-isolated-replay.log')
    log.write_bytes(run.stdout)
    assert run.returncode==0,(label,run.stdout.decode())
    assert (SNAPSHOT/report).read_bytes()==(ROOT/report).read_bytes(),label+' deterministic report differs'
    records.append({'label':label,'source':str(source),'source_sha256':hashes[str(source)],
                    'exit_code':run.returncode,'elapsed_seconds':time.monotonic()-start,
                    'log_sha256':h(log),'report':str(report),'report_sha256':h(SNAPSHOT/report),
                    'report_identical_to_frozen_repo_result':True})
for relative in inputs:
    assert h(SNAPSHOT/relative)==hashes[str(relative)]
result={'status':'PASS','scope':'Uniform four-A1 family polynomial controls; geometry separately audited',
        'snapshot_input_sha256':hashes,'snapshot_inputs_unchanged':True,'executions':records,
        'driver_sha256':h(Path(__file__))}
(OUT/'isolated-replay-manifest.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
