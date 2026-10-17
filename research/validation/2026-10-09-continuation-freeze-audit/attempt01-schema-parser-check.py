#!/usr/bin/env python3
"""Read-only independent integrity check of the October 9 frozen record.

This script checks provenance, explicit counts and local links. It never
executes a mathematical verifier or changes a canonical research document.
Its own dated JSON is an integrity record, not a mathematical proof.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import subprocess
from urllib.parse import unquote, urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
INDEX = ROOT / 'research/validation/2026-10-08-continuation-index/index.json'
BASE = ROOT / 'research/validation/2026-10-06-session'
CONT = ROOT / 'research/validation/2026-10-07-continuation'
END = ROOT / 'research/validation/2026-10-08-first-endpoint-audit'
PRINCIPAL = ROOT / 'research/validation/2026-10-08-principal-e1-d1-audit'
FAMILY2 = ROOT / 'research/validation/2026-10-08-family2-quadratic-audit'

CANONICAL = [
    'README.md', 'research/AUDITED_STATE_2026-10-07.md',
    'research/RESEARCH_UPDATE_2026-10-07.md',
    'research/SUCCESSOR_HANDOFF_2026-10-07.md',
    'research/computations/README.md',
    'research/notes/2026-10-08-session-checkpoint.md',
    'research/notes/2026-10-08-session-late-results-acceptance.md',
]
PROOF_ROUTING = [
    'research/notes/2026-10-08-session-new-results-acceptance.md',
    'research/notes/2026-10-08-session-principal-e1-d1-independent-completeness-audit.md',
    'research/notes/2026-10-08-session-scroll-nongorenstein-independent-audit.md',
    'research/notes/2026-10-08-session-scroll-artin-independent-audit.md',
    'research/notes/2026-10-08-session-localcoh-family2-quadratic-independent-audit.md',
    'research/RESEARCH_RECORD.md', 'research/RESEARCH_REPORT.md',
    'research/SUCCESSOR_HANDOFF.md',
]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
read = lambda p: json.loads(p.read_text())
issues = []
checks = []
bound = {}

def check(condition, label, detail=None):
    checks.append({'check': label, 'passed': bool(condition), 'detail': detail})
    if not condition:
        issues.append({'check': label, 'detail': detail})

def bind(p):
    p = Path(p)
    check(p.is_file(), 'file exists', str(p))
    if p.is_file():
        bound[str(p.relative_to(ROOT))] = sha(p)
    return p

def matches(p, expected, label):
    p = bind(p)
    if p.is_file():
        check(sha(p) == expected, label, {'file': str(p.relative_to(ROOT)),
                                        'expected': expected, 'observed': sha(p)})

start = datetime.now(timezone.utc).isoformat()
canonical_before = {p: sha(bind(ROOT/p)) for p in CANONICAL}
index = read(bind(INDEX))
baseline = read(bind(BASE/'validation-index.json'))
continuation = read(bind(CONT/'results.json'))
strength = read(bind(CONT/'veronese-strengthening-result-2026-10-08.json'))
endpoint = read(bind(END/'audit-manifest.json'))
principal = read(bind(PRINCIPAL/'audit-manifest.json'))
family2 = read(bind(FAMILY2/'audit-manifest.json'))

# Reconstruct counts from the actual constituent records. An imported
# helper or a copied owner log is not another top-level execution.
base_sources = {r['source'] for r in baseline['results']}
central_sources = {r['source'] for r in continuation}
check(strength['source'] in central_sources,
      'strengthened Veronese is a source revision, not an extra source')
principal_sources = set()
for row in principal['fresh_top_level_executions']:
    source = row['source'].split(' --', 1)[0]
    if not source.startswith('research/'):
        source = str((PRINCIPAL/source).relative_to(ROOT))
    principal_sources.add(source)
    check(row['exit_code'] == 0, 'independent principal execution exit zero', source)
family_sources = {
    'research/computations/verify_session_localcoh_family2_quadratics_2026_10_08.py',
    str((FAMILY2/'countercheck.py').relative_to(ROOT)),
    str((FAMILY2/'actual-tensor-reconstruction.m2').relative_to(ROOT)),
}
first_sources = {str((END/'countercheck.py').relative_to(ROOT))}
source_groups = [base_sources, central_sources, first_sources, principal_sources, family_sources]
union = set().union(*source_groups)
check(sum(map(len, source_groups)) == len(union), 'independent source groups are disjoint')
base_runs = (baseline['initial_source_checks'] + baseline['source_repair_reruns']
             + baseline['diagnostic_compatibility_copy_runs']
             + baseline['source_completion_reruns'])
check(base_runs == baseline['complete_top_level_verifier_exporter_executions'],
      'baseline count agrees with explicit retained decomposition')
family_tensor_history = []
for prefix in ('attempt01-', 'attempt02-', 'attempt03-pass-', ''):
    result = read(bind(FAMILY2/(prefix+'actual-tensor-reconstruction-result.json')))
    matches(FAMILY2/(prefix+'actual-tensor-reconstruction.m2'), result['source_sha256'],
            'retained family2 tensor source revision')
    matches(FAMILY2/(prefix+'actual-tensor-reconstruction.log'), result['log_sha256'],
            'retained family2 tensor execution log')
    family_tensor_history.append({'prefix': prefix, 'status': result['status'],
                                 'exit_code': result['exit_code']})
counts = {
    'baseline_unique_source_paths': len(base_sources),
    'baseline_explicit_execution_records': base_runs,
    'central_unique_source_paths': len(central_sources),
    'central_explicit_execution_records': len(continuation),
    'central_plus_strengthening_distinct_source_revisions':
        len({(r['source'], r['source_sha256']) for r in continuation+[strength]}),
    'strengthened_veronese_additional_execution_records': 1,
    'first_endpoint_independent_source_paths_and_executions': len(first_sources),
    'principal_independent_source_paths_and_executions': len(principal_sources),
    'family2_independent_unique_source_paths': len(family_sources),
    'family2_explicit_execution_records': len(family_tensor_history)+2,
    'combined_unique_source_paths': len(union),
    'combined_explicit_execution_records':
        base_runs+len(continuation)+1+len(first_sources)
        +len(principal['fresh_top_level_executions'])+len(family_tensor_history)+2,
}
check(counts['combined_unique_source_paths'] ==
      index['counts']['combined_distinct_top_level_sources'], 'combined source count')
check(counts['combined_explicit_execution_records'] ==
      index['counts']['combined_explicitly_indexed_executions'], 'combined execution count')

# Check every latest source and log byte hash. Baseline log digests were
# first sealed during reconciliation; they are not invented original hashes.
latest = index['latest_source_results']
check({r['source'] for r in latest} == union, 'latest result set equals independently reconstructed source union')
check(len(latest) == len(union), 'latest result paths are unique')
for row in latest:
    check(row['status'] == 'PASS' and row.get('exit_code', 0) == 0,
          'latest execution passes', row['source'])
    matches(ROOT/row['source'], row['source_sha256'], 'current latest source hash')
    matches(ROOT/row['log'], row.get('log_sha256', row.get('observed_log_sha256')),
            'latest retained log hash')
    if 'snapshot_source' in row:
        matches(ROOT/row['snapshot_source'], row['source_sha256'], 'latest explicit source snapshot hash')
for name, expected in index['metadata_sha256'].items():
    matches(ROOT/name, expected, 'indexed metadata hash')

# Check retained historical source bytes and logs, permitting only the
# documented overwritten former Veronese revision. Its old log survives.
limits = {(r['source'], r['historical_source_sha256'])
          for r in index['historical_revision_limits']}
historical_byte_losses = []
for row in continuation+[strength]:
    snap = ROOT/row['snapshot_source'] if 'snapshot_source' in row else Path(row['cwd'])/row['source']
    snap = bind(snap)
    if snap.is_file() and sha(snap) != row['source_sha256']:
        check((row['source'], row['source_sha256']) in limits,
              'historical source mismatch is explicitly disclosed', row['source'])
        check(sha(snap) == strength['source_sha256'],
              'overwritten historical source is exact accepted strengthened revision')
        historical_byte_losses.append({'source': row['source'],
                                      'lost_sha256': row['source_sha256']})
    elif snap.is_file():
        check(True, 'historical source bytes match', row['source'])
    matches(ROOT/row['log'], row['log_sha256'], 'historical continuation log hash')
check(len(historical_byte_losses) == len(limits) == 1,
      'exactly the one declared historical Veronese byte loss')
failed = [r for r in continuation if r['status'] == 'FAILED']
check(len(failed) == 2, 'both central historical failures retained')
conormal = [r for r in continuation if 'conormal_splitting' in r['source']]
check(len(conormal) == 2 and [r['status'] for r in conormal] == ['FAILED', 'PASS']
      and len({r['source_sha256'] for r in conormal}) == 1,
      'conormal repair is input closure with unchanged source bytes')
check('FileNotFoundError' in (ROOT/conormal[0]['log']).read_text(),
      'original conormal missing-input failure remains visible')
closure = read(bind(CONT/'conormal-completed-input-closure-2026-10-08.json'))
for name, expected in closure.items():
    matches(CONT/'isolated'/name, expected, 'conormal completed provenance input closure')
snapshot = read(bind(CONT/'snapshot-final-hashes.json'))
for name, expected in snapshot.items():
    matches(CONT/'isolated'/name, expected, 'declared current snapshot hash')

# Independently check the bound coefficient/input audit manifests too.
for key in ('reviewed_source_sha256', 'artifact_sha256', 'certificate_sha256', 'bound_input_sha256'):
    for name, expected in endpoint[key].items():
        matches(ROOT/name, expected, 'first endpoint bound '+key)
for name, expected in principal['retained_files_sha256'].items():
    matches(PRINCIPAL/name, expected, 'principal retained audit source/input')
    matches(ROOT/name, expected, 'principal source/input agrees with live tree')
for name, expected in principal['fresh_artifact_sha256'].items():
    matches(PRINCIPAL/name, expected, 'principal fresh artifact')
for key in ('proof_records_sha256', 'countercheck_input_sha256'):
    for name, expected in family2[key].items():
        matches(ROOT/name, expected, 'family2 '+key)
for name, expected in family2['isolated_replay_input_sha256'].items():
    matches(FAMILY2/'isolated/research/computations'/name, expected, 'family2 frozen replay input')
check(family2['remaining_family2_geometric_points'] == 22
      and family2['remaining_family2_exception_degrees'] == [3, 4, 15],
      'accepted family2 manifest retains 22 points and all lift fibres')

# Current routing and the directly relevant proof notes only. Historical
# research bodies are not recertified merely because their current notice
# routes correctly.
links = []
for name in CANONICAL+PROOF_ROUTING:
    path = bind(ROOT/name)
    content = path.read_text()
    if name in {'research/RESEARCH_RECORD.md', 'research/RESEARCH_REPORT.md',
                'research/SUCCESSOR_HANDOFF.md'}:
        content = '\n'.join(content.splitlines()[:6])
    for match in re.finditer(r'\]\(([^\n]+?)\)', content):
        target = match.group(1).strip()
        if target.startswith('<'):
            target = target[1:target.index('>')]
        else:
            target = target.split(' "', 1)[0]
        if not target or target.startswith('#') or urlparse(target).scheme:
            continue
        target = unquote(target.split('#', 1)[0])
        target = re.sub(r':\d+$', '', target)
        resolved = path.parent/target
        record = {'file': name, 'target': target, 'exists': resolved.is_file()}
        links.append(record)
        check(record['exists'], 'relative file link exists', record)

diff = subprocess.run(['git', 'diff', '--check'], cwd=ROOT,
                      text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
check(diff.returncode == 0, 'git diff --check', diff.stdout)
canonical_after = {p: sha(ROOT/p) for p in CANONICAL}
check(canonical_before == canonical_after, 'canonical files unchanged throughout frozen check')
report = {
    'started_utc': start, 'completed_utc': datetime.now(timezone.utc).isoformat(),
    'status': 'PASS' if not issues else 'FAILED',
    'scope': 'Independent record integrity, explicit indexed counts and current local routing; no mathematical verifier rerun and no new mathematical acceptance.',
    'counts': counts, 'canonical_sha256': canonical_after,
    'bound_files_sha256': bound, 'check_count': len(checks),
    'checked_local_links': len(links), 'missing_local_links': [r for r in links if not r['exists']],
    'historical_byte_losses': historical_byte_losses,
    'central_historical_failure_count': len(failed),
    'family2_tensor_execution_history': family_tensor_history,
    'issues': issues, 'checks': checks,
    'limits': [
        'Only explicitly indexed top-level executions are counted; imported helpers, agent searches and unindexed discovery runs are excluded.',
        'A missing superseded Veronese source revision remains a historical reproducibility limitation; its original log/hash and a separately snapshotted latest passing revision survive.',
        'Retained baseline logs without original recorded hashes are checked against the later observed seal, not retroactively asserted original hashes.',
        'Execution and provenance checks do not prove geometric hypotheses or exhaust unrecorded parameter strata.',
        'These hashes seal the root-declared frozen canonical files at this timestamp, not later proposed agent work.',
    ],
}
(HERE/'result.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({k: report[k] for k in ('status', 'counts', 'check_count',
                                       'checked_local_links', 'issues')}, indent=2))
raise SystemExit(bool(issues))
