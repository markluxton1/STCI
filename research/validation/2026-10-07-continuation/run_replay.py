#!/usr/bin/env python3
"""Replay newly completed certificates in an immutable input snapshot.

This is a continuation suite, not a rerun of the preceding 55-source
baseline. Imported or nested checks are recorded as dependencies, not as
additional independent top-level certificates. Use --add SOURCE to append
a later completed verifier after copying its current input closure.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SNAP = HERE / 'isolated'
PYTHON = '/private/tmp/stci-cas-venv/bin/python'
ENV = {**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'}
INITIAL = [
    'verify_session_nonreduced_independent_audit.py',
    'verify_mf6_e1_primitive_type04.py',
    'audit_mf6_e1_primitive_2026_10_07.py',
    'verify_session_nonnormal_mf6_fiber_obstruction.py',
    'session-localcoh-corners.py',
    'audit_session_localcoh_endpoint_2026_10_07.py',
    'verify_session_localcoh_q2_dual_2026_10_07.py',
    'verify_session_nonnormal_structural.py',
    'verify_mf6_e1_defective_structural.py',
]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def snapshot():
    destination = SNAP / 'research/computations'
    if destination.exists():
        raise RuntimeError('Initial snapshot already exists; use --add for later sources.')
    shutil.copytree(ROOT / 'research/computations', destination,
                    ignore=shutil.ignore_patterns('__pycache__'))
    (SNAP / 'research/scratch').mkdir(parents=True, exist_ok=True)
    manifest = {str(p.relative_to(SNAP)): sha(p)
                for p in sorted(destination.rglob('*')) if p.is_file()}
    (HERE / 'input-manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')

def run(name):
    source = 'research/computations/' + name
    command = [PYTHON, source]
    started = time.time()
    completed = subprocess.run(command, cwd=SNAP, env=ENV,
                               capture_output=True, text=True, timeout=1200)
    log = HERE / (Path(name).stem + '.log')
    log.write_text('Command: '+' '.join(command)+'\nCWD: '+str(SNAP)+'\n\n'
                   +completed.stdout+completed.stderr)
    result = {
        'source': source, 'source_sha256': sha(SNAP/source),
        'command': command, 'cwd': str(SNAP), 'isolated': True,
        'status': 'PASS' if completed.returncode == 0 else 'FAILED',
        'exit_code': completed.returncode,
        'elapsed_seconds': round(time.time()-started, 3),
        'log': str(log.relative_to(ROOT)), 'log_sha256': sha(log),
    }
    print(json.dumps(result), flush=True)
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--add', action='append', default=[])
    arguments = parser.parse_args()
    if arguments.add:
        if not SNAP.exists():
            raise RuntimeError('Create initial snapshot first.')
        names = arguments.add
        prior = json.loads((HERE/'results.json').read_text())
        if any(item['source'].rsplit('/', 1)[-1] in names for item in prior):
            raise RuntimeError('A requested top-level source already has a replay record.')
        # Copy only newly needed files or explicitly changed source inputs.
        # Keep the previous snapshot manifest and log a separate addition manifest.
        added = {}
        for path in sorted((ROOT/'research/computations').rglob('*')):
            if not path.is_file() or '__pycache__' in path.parts:
                continue
            relative = str(path.relative_to(ROOT))
            target = SNAP/relative
            if not target.exists() or path.name in names:
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(path, target)
                added[relative] = sha(target)
        ordinal = len(list(HERE.glob('addition-manifest-*.json')))+1
        (HERE/f'addition-manifest-{ordinal}.json').write_text(json.dumps(added, indent=2)+'\n')
    else:
        snapshot()
        names, prior = INITIAL, []
    with ThreadPoolExecutor(max_workers=2) as pool:
        for future in as_completed([pool.submit(run, name) for name in names]):
            prior.append(future.result())
            (HERE/'results.json').write_text(json.dumps(prior, indent=2)+'\n')
    outputs = {str(p.relative_to(SNAP)): sha(p)
               for p in sorted(SNAP.rglob('*')) if p.is_file()}
    (HERE/'snapshot-final-hashes.json').write_text(json.dumps(outputs, indent=2)+'\n')
    latest = {item['source']: item for item in prior}
    print('COMPLETE:', len(names), 'new top-level sources;',
          len(prior), 'total continuation replay records;',
          len(latest), 'distinct sources.', flush=True)
    if any(item['status'] != 'PASS' for item in latest.values()):
        raise SystemExit(1)

if __name__ == '__main__':
    main()
