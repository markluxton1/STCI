#!/usr/bin/env python3
"""Reconcile retained execution records; no mathematical verifier is rerun.

Counts refer only to these explicitly indexed top-level records. Imported
modules, agent discovery commands and other unindexed executions are not
silently added. Historical failure logs and source revisions survive.
"""
from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
BASE=ROOT/'research/validation/2026-10-06-session'
CONT=ROOT/'research/validation/2026-10-07-continuation'
END=ROOT/'research/validation/2026-10-08-first-endpoint-audit'
PRINCIPAL=ROOT/'research/validation/2026-10-08-principal-e1-d1-audit'
FAMILY2=ROOT/'research/validation/2026-10-08-family2-quadratic-audit'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text())

baseline=read(BASE/'validation-index.json')
rows=read(CONT/'results.json')
strength=read(CONT/'veronese-strengthening-result-2026-10-08.json')
endpoint=read(END/'audit-manifest.json')
principal=read(PRINCIPAL/'audit-manifest.json')
family2=read(FAMILY2/'audit-manifest.json')
latest={row['source']:row for row in rows}
latest[strength['source']]=strength
assert len(latest)==len({row['source'] for row in rows})
assert all(row['status']=='PASS' and row['exit_code']==0 for row in latest.values())

checks=[]
historical_revision_limits=[]
for row in rows+[strength]:
    snapshot=ROOT/row['snapshot_source'] if 'snapshot_source' in row else Path(row['cwd'])/row['source']
    assert snapshot.is_file(), row['source']
    exact_snapshot=sha(snapshot)==row['source_sha256']
    if not exact_snapshot:
        assert row['source']==strength['source'] and row['source_sha256']!=strength['source_sha256']
        assert sha(snapshot)==strength['source_sha256']
        historical_revision_limits.append({
            'source':row['source'],'historical_source_sha256':row['source_sha256'],
            'historical_source_bytes_retained':False,
            'reason':'The former --add copier tested membership only in the initial manifest, so later additions recopied a previously added source from the live tree. Addition manifests2 and3 record the old/new hashes. The old log/hash remain, but its source bytes are not claimed preserved.',
            'current_revision':'Separately snapshotted and freshly verified strengthened source; latest theorem depends on that revision.',
        })
    log=ROOT/row['log']
    assert log.is_file() and sha(log)==row['log_sha256'], row['log']
    checks.append({'source':row['source'],'status':row['status'],
                   'snapshot_source':str(snapshot.relative_to(ROOT)),
                   'recorded_source_sha256':row['source_sha256'],
                   'observed_snapshot_source_sha256':sha(snapshot),
                   'exact_historical_snapshot_retained':exact_snapshot,'log':row['log'],
                   'log_sha256':sha(log)})

all_latest={}
base_hashes=read(BASE/'source-hashes-after.json')['hashes']
for row in baseline['results']:
    name=row['source']; expected=row.get('latest_sha256',row.get('source_sha256',base_hashes.get(name)))
    assert expected and sha(ROOT/name)==expected, name
    assert row.get('latest_status',row['status'])=='PASS', name
    log=row.get('latest_log',row['log'])
    assert (ROOT/log).is_file(),log
    all_latest[name]={'source':name,'source_sha256':expected,'status':'PASS',
                      'evidence':'retained baseline; not rerun in this reconciliation',
                      'log':log,'observed_log_sha256':sha(ROOT/log)}
for name,row in latest.items():
    assert name not in all_latest, 'Unexpected baseline overlap: '+name
    assert sha(ROOT/name)==row['source_sha256'], name
    all_latest[name]={**row,'evidence':'continuation isolated replay; latest source revision'}

# Independent first-family countercheck is a separate source, not another
# execution of each field verifier that it reads.
for group in ('reviewed_source_sha256','artifact_sha256','bound_input_sha256'):
    for name,expected in endpoint[group].items():
        assert sha(ROOT/name)==expected,name
counter='research/validation/2026-10-08-first-endpoint-audit/countercheck.py'
assert endpoint['own_countercheck_exit_code']==0 and counter not in all_latest
all_latest[counter]={'source':counter,'source_sha256':sha(ROOT/counter),
                     'status':'PASS','exit_code':0,
                     'evidence':'independent rational-source/factor completeness companion',
                     'log':'research/validation/2026-10-08-first-endpoint-audit/countercheck.log',
                     'log_sha256':sha(END/'countercheck.log')}

# Four actually completed independent executions; the copied owner/open
# replay is preserved but is not counted as an auditor execution.
for name,expected in principal['retained_files_sha256'].items():
    assert sha(PRINCIPAL/name)==expected,name
    assert sha(ROOT/name)==expected,name
for name,expected in principal['fresh_artifact_sha256'].items():
    assert sha(PRINCIPAL/name)==expected,name
assert all(row['exit_code']==0 for row in principal['fresh_top_level_executions'])
principal_runs=[
    ('coverage-countercheck.py','coverage-countercheck.log',True),
    ('research/computations/verify_mf6_e1_d1_principal_boundaries_2026_10_08.py','boundary-replay.log',False),
    ('research/computations/verify_mf6_e1_d1_principal_boundary_residues_2026_10_08.py','residue-replay.log',False),
    ('residue-input-comparison.py','residue-input-comparison.log',True),
]
for name,log,local in principal_runs:
    source=str((PRINCIPAL/name).relative_to(ROOT)) if local else name
    assert source not in all_latest,source
    assert sha(ROOT/source)==sha(PRINCIPAL/name),source
    all_latest[source]={'source':source,'source_sha256':sha(PRINCIPAL/name),
        'status':'PASS','exit_code':0,'snapshot_source':str((PRINCIPAL/name).relative_to(ROOT)),
        'evidence':'independent principal completeness audit; own fresh execution',
        'log':str((PRINCIPAL/log).relative_to(ROOT)),'log_sha256':sha(PRINCIPAL/log)}

# The new field countercheck and literal tensor reconstruction are own
# executions; wrappers and producing-agent field searches are not added.
assert family2['status']=='PASS'
for group in ('proof_records_sha256','countercheck_input_sha256'):
    for name,expected in family2[group].items():
        assert sha(ROOT/name)==expected,name
for name,expected in family2['isolated_replay_input_sha256'].items():
    assert sha(FAMILY2/'isolated/research/computations'/name)==expected,name
family2_runs=[
    ('research/computations/verify_session_localcoh_family2_quadratics_2026_10_08.py',
     FAMILY2/'isolated/research/computations/verify_session_localcoh_family2_quadratics_2026_10_08.py',
     FAMILY2/'isolated-replay.log'),
    (str((FAMILY2/'countercheck.py').relative_to(ROOT)),FAMILY2/'countercheck.py',FAMILY2/'countercheck.log'),
    (str((FAMILY2/'actual-tensor-reconstruction.m2').relative_to(ROOT)),
     FAMILY2/'actual-tensor-reconstruction.m2',FAMILY2/'actual-tensor-reconstruction.log'),
]
for name,snapshot,log in family2_runs:
    assert name not in all_latest and sha(ROOT/name)==sha(snapshot),name
    all_latest[name]={'source':name,'source_sha256':sha(snapshot),'status':'PASS','exit_code':0,
        'snapshot_source':str(snapshot.relative_to(ROOT)),
        'evidence':'independent family2 quadratic audit; exact fields and literal actual tensor',
        'log':str(log.relative_to(ROOT)),'log_sha256':sha(log)}
family2_history=[]
for prefix in ('attempt01-','attempt02-','attempt03-pass-',''):
    result=read(FAMILY2/(prefix+'actual-tensor-reconstruction-result.json'))
    source=FAMILY2/(prefix+'actual-tensor-reconstruction.m2')
    log=FAMILY2/(prefix+'actual-tensor-reconstruction.log')
    assert sha(source)==result['source_sha256'] and sha(log)==result['log_sha256']
    family2_history.append({**result,'snapshot_source':str(source.relative_to(ROOT)),
        'log':str(log.relative_to(ROOT))})

snapshot_manifest=read(CONT/'snapshot-final-hashes.json')
for name,expected in snapshot_manifest.items():
    assert sha(CONT/'isolated'/name)==expected,name
closure=read(CONT/'conormal-completed-input-closure-2026-10-08.json')
note='research/notes/2026-10-07-session-localcoh-conormal-splitting.md'
assert sha(CONT/'isolated'/note)==closure[note]

metadata=[BASE/'validation-index.json',CONT/'results.json',
          CONT/'veronese-strengthening-result-2026-10-08.json',
          CONT/'conormal-completed-input-closure-2026-10-08.json',
          CONT/'elliptic-source-repair-2026-10-08.json',
          CONT/'input-manifest.json',CONT/'snapshot-final-hashes.json',END/'audit-manifest.json',
          PRINCIPAL/'audit-manifest.json',FAMILY2/'audit-manifest.json']
metadata+=sorted(CONT.glob('addition-manifest-*.json'))
report={
    'created_utc':datetime.now(timezone.utc).isoformat(),
    'status':'PASS: latest source revisions, execution logs and declared current snapshot hashes agree; one superseded historical source-byte loss is explicitly retained as a limitation',
    'scope':'Record integrity and explicit latest execution status only; not independent proof of the mathematical conclusions',
    'counts':{
        'retained_baseline_distinct_sources':len(baseline['results']),
        'retained_baseline_indexed_executions':baseline['complete_top_level_verifier_exporter_executions'],
        'continuation_distinct_sources':len(latest),
        'continuation_execution_records':len(rows),
        'continuation_historical_failed_records':sum(row['status']=='FAILED' for row in rows),
        'separate_strengthened_veronese_revision_execution':1,
        'separate_first_endpoint_countercheck_sources_and_executions':1,
        'separate_principal_independent_sources_and_executions':len(principal_runs),
        'separate_family2_independent_sources':len(family2_runs),
        'separate_family2_explicit_executions':len(family2_history)+2,
        'combined_distinct_top_level_sources':len(all_latest),
        'combined_latest_pass':len(all_latest),
        'combined_explicitly_indexed_executions':baseline['complete_top_level_verifier_exporter_executions']+len(rows)+2+len(principal_runs)+len(family2_history)+2,
        'continuation_distinct_source_revisions':len({(row['source'],row['source_sha256']) for row in rows+[strength]}),
    },
    'historical_failures':[row for row in rows if row['status']=='FAILED'],
    'family2_tensor_execution_history':family2_history,
    'historical_revision_limits':historical_revision_limits,
    'metadata_sha256':{str(p.relative_to(ROOT)):sha(p) for p in metadata},
    'execution_integrity_checks':checks,
    'latest_source_results':list(all_latest.values()),
    'snapshot_final_manifest_verified_files':len(snapshot_manifest),
    'limits':['Baseline historical logs without recorded hashes are sealed as observed now, not retroactively claimed to have original log hashes.',
              'Independent e1,d2=4 source-byte replay is retained as supplementary evidence and not inflated into another distinct source.',
              'Nested/imported checks and unindexed agent discovery runs are excluded from these execution counts.',
              'An exact identity certificate does not prove unrecorded geometric hypotheses or cover an unstated parameter stratum.']
}
(HERE/'index.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':report['status'],'counts':report['counts'],
                  'verified_snapshot_files':len(snapshot_manifest)},indent=2))
