#!/usr/bin/env python3
"""Freeze all default-verifier inputs and replay both fields unchanged."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
SOURCE = ROOT/'research/computations'
SNAPSHOT = OUT/'isolated'
DEST = SNAPSHOT/'research/computations'
DEST.mkdir(parents=True,exist_ok=True)
checker = 'verify_session_localcoh_family2_quadratics_2026_10_08.py'
inputs = {checker}
for case in ('qplus','qminus'):
    certname = f'session_localcoh_family2_{case}_audit_2026_10_08.json'
    inputs.add(certname)
    cert = json.loads((SOURCE/certname).read_text())
    for name,digest in cert['coordinate_sha256'].items():
        assert hashlib.sha256((SOURCE/name).read_bytes()).hexdigest() == digest
        inputs.add(name)
hashes = {}
for name in sorted(inputs):
    data = (SOURCE/name).read_bytes()
    destination = DEST/name
    if destination.exists():
        assert destination.read_bytes() == data, 'Immutable snapshot differs: '+name
    else:
        destination.write_bytes(data)
    hashes[name] = hashlib.sha256(data).hexdigest()
assert hashes[checker] == 'a1168854beed0d56838851710444a5d2d35ef835333f9ab179d2163f23739ea3'
start = time.monotonic()
environment = dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
execution = subprocess.run([sys.executable,str(DEST/checker)],cwd=SNAPSHOT,
                           env=environment,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
log = OUT/'isolated-replay.log'
log.write_bytes(execution.stdout)
after = {name:hashlib.sha256((DEST/name).read_bytes()).hexdigest() for name in sorted(inputs)}
assert hashes == after
record = {'status':'PASS' if execution.returncode == 0 else 'FAILED',
          'returncode':execution.returncode,'elapsed_seconds':time.monotonic()-start,
          'command':[sys.executable,str((DEST/checker).relative_to(ROOT))],
          'input_sha256':hashes,'snapshot_inputs_unchanged':True,
          'log_sha256':hashlib.sha256(execution.stdout).hexdigest(),
          'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(OUT/'isolated-replay-manifest.json').write_text(json.dumps(record,indent=2)+'\n')
print(execution.stdout.decode(),end='')
print(json.dumps(record,indent=2))
assert execution.returncode == 0
