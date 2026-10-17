#!/usr/bin/env python3
"""Record-only extension checker. This file never runs mathematical sources.

Preflight uses the mutable draft input list. Final sealing requires a separate
root-readiness record and a FROZEN input list, and exclusively creates outputs.
"""
from collections import Counter, deque
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CANONICAL = [
    "README.md", "research/AUDITED_STATE_2026-10-07.md",
    "research/RESEARCH_UPDATE_2026-10-07.md",
    "research/SUCCESSOR_HANDOFF_2026-10-07.md",
    "research/RESEARCH_RECORD.md", "research/LITERATURE_LEDGER.md",
    "research/computations/README.md",
]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
parser = argparse.ArgumentParser()
mode = parser.add_mutually_exclusive_group(required=True)
mode.add_argument("--preflight", action="store_true")
mode.add_argument("--seal-once", action="store_true")
args = parser.parse_args()
started = datetime.now(timezone.utc).isoformat()
issues, checks, bound, edges, unsealed_routes = [], 0, {}, {}, []
def check(test, message):
    global checks
    checks += 1
    if not test:
        issues.append(message)
    return test
def bind(name, expected=None):
    path = ROOT / name
    if not check(path.is_file(), "Missing bound file: " + name):
        return None
    digest = sha(path)
    if name in bound:
        check(bound[name] == digest, "Changed during execution: " + name)
    bound[name] = digest
    if expected is not None:
        check(digest == expected, "Digest mismatch: " + name)
    return digest
def read_json(name, expected=None):
    if bind(name, expected) is None:
        return {}
    try:
        return json.loads((ROOT / name).read_text())
    except (ValueError, OSError) as exc:
        check(False, "JSON unreadable: " + name + ": " + str(exc))
        return {}
def relative(path):
    return path.resolve().relative_to(ROOT).as_posix()
def git(*parts):
    proc = subprocess.run(["git", *parts], cwd=ROOT, capture_output=True, text=True)
    check(proc.returncode == 0, "Read-only git failed: " + " ".join(parts))
    return proc.stdout.strip()

anchor_name = relative(HERE / "prior-seal-trust-anchors.json")
anchors = read_json(anchor_name)
for name, expected in anchors.get("sha256", {}).items():
    bind(name, expected)
prior = read_json(anchors.get("prior_result", "MISSING"))
check(prior.get("status") == "PASS" and prior.get("mode") == "FINAL_SEAL",
      "Prior completed record seal is not PASS FINAL_SEAL")
check(prior.get("mathematical_execution_count") == 0,
      "Prior seal must remain a record-only execution")
old_bindings = prior.get("bound_files_sha256", {})
check(len(old_bindings) == 1203, "Prior binding count differs from 1203")
changed, unchanged_noncanonical = [], 0
for name, expected in old_bindings.items():
    observed = bind(name)
    if name in CANONICAL:
        if observed != expected:
            changed.append(name)
    else:
        if check(observed == expected, "Old noncanonical binding changed: " + name):
            unchanged_noncanonical += 1
check(sorted(changed) == sorted(CANONICAL),
      "Expected exactly the seven canonical bindings to change")
check(unchanged_noncanonical == 1196,
      "Expected all 1196 old noncanonical bindings unchanged")

config_path = HERE / ("accepted-inputs.json" if args.seal_once else "accepted-inputs.DRAFT.json")
config = read_json(relative(config_path))
if args.seal_once:
    check(config.get("status") == "FROZEN", "Final inputs must be FROZEN")
else:
    check(config.get("status") == "DRAFT_NOT_FROZEN", "Preflight must use explicit draft inputs")
check(config.get("record_only_no_mathematical_replays") is True,
      "Input scope does not prohibit mathematical replays")
head_before = git("rev-parse", "HEAD")
check(head_before == config.get("expected_head"), "HEAD differs from specified root HEAD")
canonical_before = {name: bind(name) for name in CANONICAL}
acceptance = config.get("acceptance", "MISSING")
acceptance_digest = bind(acceptance)
for name, expected in config.get("frozen_completed_input_sha256", {}).items():
    bind(name, expected)

if args.seal_once:
    ready = read_json(relative(HERE / "root-readiness.json"))
    check(ready.get("ready_for_final_record_seal") is True,
          "Root has not authorized final record seal")
    check(ready.get("acceptance_sha256") == acceptance_digest,
          "Acceptance differs from root freeze snapshot")
    check(ready.get("canonical_sha256") == canonical_before,
          "Canonical files differ from root freeze snapshot")
    check(ready.get("head") == head_before, "Root readiness HEAD mismatch")
    check(ready.get("accepted_inputs_sha256") == sha(config_path),
          "Accepted input list differs from root freeze snapshot")
    check(ready.get("record_integrity_is_not_mathematical_truth") is True,
          "Root readiness must retain mathematical scope boundary")

# Inline Markdown only, with code masked. Unknown/live notes are checked for
# existence but deliberately not read or hash-bound as completed proof inputs.
link_pattern = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)")
def local_links(name):
    text = (ROOT / name).read_text()
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", "", text)
    found = []
    for match in link_pattern.finditer(text):
        target = match.group(1).strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target) or target.startswith("#"):
            continue
        from urllib.parse import unquote
        target = unquote(target.split("#", 1)[0])
        # Historical algebra notation is not a route.
        if name.endswith("2026-10-08-session-scroll-nongorenstein-independent-audit.md") and target == "a-k":
            continue
        path = ((ROOT / name).parent / target).resolve()
        try:
            route = relative(path)
        except ValueError:
            check(False, "Local route leaves repository: " + name + " -> " + target)
            continue
        check(path.exists(), "Broken inline local route: " + name + " -> " + route)
        found.append(route)
    return sorted(set(found))

frozen_inputs = set(config.get("frozen_completed_input_sha256", {}))
scannable = set(old_bindings) | frozen_inputs | set(CANONICAL) | {acceptance}
queue, seen = deque(CANONICAL + [acceptance]), set()
while queue:
    name = queue.popleft()
    if name in seen or not (ROOT / name).is_file() or not name.endswith(".md"):
        continue
    seen.add(name)
    found = local_links(name)
    edges[name] = found
    for route in found:
        if route in scannable and route.endswith(".md"):
            queue.append(route)
        elif route not in scannable:
            unsealed_routes.append({"from": name, "to": route,
                                    "scope": "route existence only; outside completed input seal"})
for name in CANONICAL:
    check(acceptance in edges.get(name, []), "Canonical lacks acceptance route: " + name)
reachable = set()
queue = deque([acceptance])
while queue:
    name = queue.popleft()
    if name in reachable:
        continue
    reachable.add(name)
    queue.extend(edges.get(name, []))
for name in config.get("required_audited_routes", []):
    check(name in reachable, "Completed written input not reachable from acceptance: " + name)

# Validate declared execution/source/raw hashes without executing the sources.
# Field matching is exact when a path is declared; pathless hash fields use a
# same-history digest lookup and are explicitly recorded as such.
execution_rows, digest_checks = [], []
def resolve_record_path(value, record):
    if not isinstance(value, str):
        return None
    path = Path(value)
    candidates = [path] if path.is_absolute() else [ROOT / path, record.parent / path]
    for candidate in candidates:
        if candidate.is_file():
            try:
                return relative(candidate)
            except ValueError:
                pass
    return None
def inspect(value, record, group_files, trail=""):
    if isinstance(value, list):
        for i, item in enumerate(value):
            inspect(item, record, group_files, trail + f"[{i}]")
    elif isinstance(value, dict):
        if isinstance(value.get("exit_code"), int):
            execution_rows.append({"record": relative(record), "field": trail,
                "exit_code": value["exit_code"], "command": value.get("command"),
                "start": value.get("started_utc", value.get("start_utc")),
                "scope": value.get("scope"),
                "expected_exit_code": value.get("expected_exit_code")})
            if "expected_exit_code" in value:
                check(value["exit_code"] == value["expected_exit_code"],
                      "Recorded exit differs from declared expected exit: " + relative(record) + trail)
        if "path" in value and "sha256" in value:
            path = resolve_record_path(value["path"], record)
            if check(path is not None, "Missing declared path/hash: " + relative(record) + trail):
                bind(path, value["sha256"])
        for key, expected in value.items():
            if key.endswith("_sha256") and isinstance(expected, str) and re.fullmatch(r"[0-9a-f]{64}", expected):
                stem = key[:-7]
                candidate = value.get(stem, value.get(stem + "_path", value.get(stem + "_snapshot")))
                path = resolve_record_path(candidate, record)
                if path is None and stem in ("source", "current_source"):
                    path = resolve_record_path(value.get("source_path"), record)
                if path is None and stem in ("source", "stdout", "stderr"):
                    defaults = [stem + ".m2", stem + ".py", stem + ".txt"]
                    matches = [relative(record.parent / p) for p in defaults if (record.parent / p).is_file()]
                    path = next((p for p in matches if sha(ROOT / p) == expected), None)
                kind = "declared path"
                if path is None:
                    path = next((p for p in group_files if bound.get(p) == expected), None)
                    kind = "same-history digest lookup; no matching explicit path field"
                check(path is not None, "Unresolved declared digest: " + relative(record) + trail + "." + key)
                if path is not None:
                    bind(path, expected)
                digest_checks.append({"record": relative(record), "field": trail + "." + key,
                                      "bound_path": path, "resolution": kind})
            if isinstance(expected, (dict, list)):
                inspect(expected, record, group_files, trail + "." + key)

history_coverage = []
for directory in config.get("completed_evidence_directories", []):
    group_files = sorted(p for p in frozen_inputs if p.startswith(directory + "/"))
    for name in group_files:
        if name.endswith(".json"):
            inspect(json.loads((ROOT / name).read_text()), ROOT / name, group_files)
    history_coverage.append({"directory": directory, "bound_files": len(group_files)})

head_after = git("rev-parse", "HEAD")
check(head_before == head_after, "HEAD changed during record check")
canonical_after = {name: sha(ROOT / name) for name in CANONICAL}
check(canonical_before == canonical_after, "Canonical file changed during record check")
for name, expected in list(bound.items()):
    check((ROOT / name).is_file() and sha(ROOT / name) == expected,
          "Bound file changed during final stability pass: " + name)
result = {
    "status": "PASS" if not issues else "FAIL",
    "mode": "FINAL_SEAL" if args.seal_once else "DRAFT_PREFLIGHT_NOT_A_FINAL_SEAL",
    "started_utc": started, "completed_utc": datetime.now(timezone.utc).isoformat(),
    "scope": "Record bytes, declared execution/source/raw provenance, inline local routing, stability only",
    "does_not_certify": ["mathematical truth", "independence of checker lineages",
                         "novelty", "global STCI resolution", "unlisted or live research"],
    "mathematical_verifiers_rerun": False, "mathematical_execution_count": 0,
    "checker_sha256": sha(Path(__file__)), "head_observed": head_before,
    "check_count": checks, "checked_local_links": sum(map(len, edges.values())),
    "prior_binding_count": len(old_bindings), "unchanged_prior_noncanonical_count": unchanged_noncanonical,
    "changed_prior_canonical_bindings": changed,
    "canonical_before_sha256": canonical_before, "canonical_after_sha256": canonical_after,
    "acceptance_sha256_observed": acceptance_digest,
    "bound_files_sha256": bound, "required_audited_routes": config.get("required_audited_routes", []),
    "history_coverage": history_coverage, "declared_digest_checks": digest_checks,
    "captured_execution_metadata_rows": execution_rows,
    "execution_metadata_exit_counts": dict(Counter(str(r["exit_code"]) for r in execution_rows)),
    "execution_row_count_is_not_independent_checker_count": True,
    "scoped_local_link_edges": edges, "outside_completed_scope_route_existence": unsealed_routes,
    "excluded_pending_or_live_work": config.get("excluded_pending_or_live_work", []),
    "issues": issues,
    "limits": ["Draft acceptance and canonicals may change after preflight.",
               "No mathematical verifier or historical checker was executed.",
               "Only inline Markdown links outside fenced and inline code were scanned; reference-style links and nested-parenthesis destinations are outside parser coverage.",
               "Unknown/live linked files are checked only for existence, without proof-content or hash binding.",
               "Source-history and direct-tool observations retain their declared historical scopes; a captured replay does not restore originally missing raw output.",
               "Recorded exit rows may repeat an execution in an aggregate record; they are not checker-lineage or fresh-execution counts."],
}
output = HERE / ("result.json" if args.seal_once else "preflight-result.json")
with output.open("x" if args.seal_once else "w") as stream:
    stream.write(json.dumps(result, indent=2) + "\n")
print(json.dumps({k: result[k] for k in ["status", "mode", "check_count", "checked_local_links",
    "prior_binding_count", "unchanged_prior_noncanonical_count", "mathematical_execution_count", "issues"]}, indent=2))
raise SystemExit(0 if not issues else 1)
