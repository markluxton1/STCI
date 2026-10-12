#!/usr/bin/env python3
"""Scoped read-only record checker. Does not execute mathematical sources."""
from argparse import ArgumentParser
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CANONICAL = ["README.md", "research/AUDITED_STATE_2026-10-07.md",
             "research/RESEARCH_UPDATE_2026-10-07.md",
             "research/SUCCESSOR_HANDOFF_2026-10-07.md",
             "research/RESEARCH_RECORD.md", "research/LITERATURE_LEDGER.md",
             "research/computations/README.md"]
parser = ArgumentParser()
mode = parser.add_mutually_exclusive_group(required=True)
mode.add_argument("--preflight", action="store_true")
mode.add_argument("--seal-once", action="store_true")
parser.add_argument("--acceptance", default="research/notes/2026-10-11-session-quintic-continuation-results-acceptance.md")
args = parser.parse_args()
target = HERE / ("result.json" if args.seal_once else "preflight-result.json")
if args.seal_once and target.exists():
    raise SystemExit("Refusing to overwrite the frozen final record.")
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
rel = lambda p: str(Path(p).resolve().relative_to(ROOT))
checks, issues, bound, edges = [], [], {}, {}
started = datetime.now(timezone.utc).isoformat()

def check(value, label, detail=None):
    row = {"check": label, "passed": bool(value), "detail": detail}
    checks.append(row)
    if not value:
        issues.append(row)

def bind(path):
    path = Path(path)
    check(path.is_file(), "file exists", rel(path))
    if path.is_file():
        key, digest = rel(path), sha(path)
        check(key not in bound or bound[key] == digest,
              "first-observed file bytes remain stable", key)
        bound[key] = digest
    return path

def read(path):
    return json.loads(bind(path).read_text())

def matches(path, expected, label):
    path = bind(path)
    if path.is_file():
        check(sha(path) == expected, label, rel(path))

def git(*values):
    p = subprocess.run(["git", *values], cwd=ROOT, capture_output=True, text=True)
    check(p.returncode == 0, "read-only Git command", list(values))
    return p.stdout.strip()

head = git("rev-parse", "HEAD")
bind(Path(__file__))
for name in ["README.md", "run_final_seal.py", "check_record.py",
             "prepared-prior-checker.py", "independent-coverage-review.md",
             "audit_endpoint_histories.py", "worker-stop-observation.json"]:
    bind(HERE / name)
readiness = read(HERE / "root-readiness.json")
check(readiness["ready"] is True, "explicit root readiness recorded")
check(readiness["head"] == head, "readiness matches current HEAD")
check(readiness["acceptance"] == args.acceptance, "readiness uses exact acceptance")
canonical_before = {p: sha(bind(ROOT / p)) for p in CANONICAL}
check(canonical_before == readiness["canonical_sha256"], "ready canonical snapshot matches")
acceptance = bind(ROOT / args.acceptance)
matches(acceptance, readiness["acceptance_sha256"], "ready acceptance bytes")

# Preserve every preceding binding except the seven explicitly reconciled canonicals.
anchors = read(HERE / "prior-seal-trust-anchors.json")
for path, expected in anchors["anchors"].items():
    matches(ROOT / path, expected, "frozen prior seal trust anchor")
prior = read(ROOT / "research/validation/2026-10-11-continuation-seal/result.json")
check(prior["status"] == "PASS" and prior["check_count"] == 5747
      and prior["checked_local_links"] == 773
      and len(prior["bound_files_sha256"]) == 921, "prior scoped seal preserved")
git("merge-base", "--is-ancestor", prior["head_observed"], head)
changed_canonical = []
for path, expected in prior["bound_files_sha256"].items():
    if path in CANONICAL:
        bind(ROOT / path)
        if sha(ROOT / path) != expected:
            changed_canonical.append(path)
    else:
        matches(ROOT / path, expected, "all prior noncanonical bound bytes unchanged")

accepted = read(HERE / "accepted-inputs.json")
for path, row in accepted["inputs"].items():
    matches(ROOT / path, row["sha256"], "exact root-reviewed proof version")
check("OPEN" in acceptance.read_text() and "nonendpoint" in acceptance.read_text(),
      "acceptance retains open unrestricted and nonendpoint scope")

# The independent five-history review retains original metadata versus replays.
inventory = read(HERE / "independent-hash-inventory.json")
check(inventory["declared_hash_bindings_independently_checked"] == 77
      and inventory["declared_hash_mismatches"] == 0,
      "independent declared comparison scope retained")
check(inventory["scoped_observed_M2_script_executions"] == 35
      and inventory["original_metadata_only_execution_rows"] == 14
      and inventory["captured_raw_stream_execution_rows"] == 21,
      "independent execution provenance categories preserved")
for path, info in inventory["files"].items():
    matches(ROOT / path, info["sha256"], "independent observed inventory bytes")
    check((ROOT / path).stat().st_size == info["bytes"], "inventory byte size", path)

# A separately reconstructed endpoint inventory checks actual recorded attempts,
# including declared and newly observed raw-stream bindings without conflation.
endpoint = read(HERE / "endpoint-execution-coverage.json")
check(not endpoint["issues"], "endpoint inventory has no binding mismatch")
check(endpoint["captured_execution_count"] == len(endpoint["attempts"]) == 28,
      "endpoint captured execution count")
for info in endpoint["observed_files"]:
    matches(ROOT / info["path"], info["sha256"], "endpoint observed file bytes")
for row in endpoint["attempts"]:
    check(row["return_code"] in (0, 1), "endpoint actual exit status retained", row["record"])
    for info in row["bindings"].values():
        path = ROOT / info["path"]
        matches(path, info["sha256_observed"], "endpoint observed attempt binding")
        if info["sha256_preexisting_record"] is not None:
            matches(path, info["sha256_preexisting_record"], "endpoint original declared binding")
        else:
            check(info["binding_status"] == "UNBOUND_IN_ATTEMPT_RECORD",
                  "missing original binding remains explicitly disclosed", info["path"])
check(Counter(r["classification"] for r in endpoint["attempts"])
      == Counter(endpoint["captured_classifications"]), "endpoint classifications reconciled")
check(len(endpoint["separately_named_local_excess_direct_tool_observations"]) == 5,
      "five weaker direct tool observations not merged into captured executions")

# Root's nonendpoint repairs are a separate five-attempt, one-lineage history.
nonendpoint_folder = ROOT / "research/validation/2026-10-11-quintic-nonendpoint-structure"
nonendpoint_rows = []
for record in sorted(nonendpoint_folder.glob("attempt-*/execution-record.json")):
    row = read(record)
    snapshot = ROOT / row.get("snapshot", row.get("executed_source"))
    matches(snapshot, row["source_sha256"], "nonendpoint exact executed source")
    if "snapshot_sha256" in row:
        matches(snapshot, row["snapshot_sha256"], "nonendpoint copied snapshot")
    for stream in ("stdout", "stderr"):
        matches(record.parent / (stream + ".txt"), row[stream + "_sha256"],
                "nonendpoint original captured raw stream")
    nonendpoint_rows.append({"record": rel(record), "exit_code": row["exit_code"]})
check(len(nonendpoint_rows) == 5 and Counter(r["exit_code"] for r in nonendpoint_rows)
      == Counter({1: 4, 0: 1}), "five nonendpoint attempts retain four failures and one pass")
final_nonendpoint = nonendpoint_folder / "attempt-05-root-name-repair"
check("PASS ALL: 7 supporting checks" in (final_nonendpoint / "stdout.txt").read_text(),
      "seven nonendpoint conditions plus distinct final label")
final_record = json.loads((final_nonendpoint / "execution-record.json").read_text())
matches(ROOT / final_record["source"], final_record["source_sha256"],
        "current nonendpoint repaired source equals passing version")

# Scan current canonical routes and their transitive proof notes, masking code.
queue = list(CANONICAL) + [args.acceptance]
scanned, checked_links, excluded_notation = set(), 0, []
while queue:
    path_string = queue.pop(0)
    if path_string in scanned:
        continue
    scanned.add(path_string)
    path = bind(ROOT / path_string)
    text = path.read_text()
    mask = lambda m: re.sub(r"[^\n]", " ", m.group(0))
    text = re.sub(r"(?ms)^```[^\n]*\n.*?^```[^\n]*$", mask, text)
    text = re.sub(r"`[^`\n]*`", mask, text)
    for m in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", text):
        if (path.name == "2026-10-08-session-scroll-nongorenstein-independent-audit.md"
                and m.group(0) == "[L_i:K](a-k)"):
            excluded_notation.append({"file": path_string, "expression": m.group(0)})
            continue
        url = m.group(1).strip().strip("<>")
        parsed = urlparse(url)
        if parsed.scheme or url.startswith("#"):
            continue
        target_path = Path(unquote(parsed.path))
        target_path = target_path if target_path.is_absolute() else path.parent / target_path
        target_path = target_path.resolve()
        checked_links += 1
        check(target_path.exists(), "local Markdown target exists", {"from": path_string, "to": str(target_path)})
        edges.setdefault(path_string, []).append(str(target_path))
        if target_path.is_file() and target_path.is_relative_to(ROOT):
            bind(target_path)
            if target_path.suffix == ".md" and target_path.is_relative_to(ROOT / "research/notes"):
                queue.append(rel(target_path))
for path in CANONICAL:
    check(str(acceptance.resolve()) in edges.get(path, []),
          "canonical links to exact new acceptance", path)
reachable, work = set(), [args.acceptance]
while work:
    path = work.pop()
    if path in reachable:
        continue
    reachable.add(path)
    for dest in edges.get(path, []):
        dp = Path(dest)
        if dp.is_relative_to(ROOT):
            work.append(rel(dp))
for path in accepted["required_audited_routes"]:
    check(path in reachable, "acceptance reaches required proof/audit", path)
check(head in acceptance.read_text()
      and head in (ROOT / "research/SUCCESSOR_HANDOFF_2026-10-07.md").read_text(),
      "acceptance and handoff identify current HEAD")
git("diff", "--check")
check(git("rev-parse", "HEAD") == head, "HEAD unchanged during record check")
canonical_after = {p: sha(ROOT / p) for p in CANONICAL}
check(canonical_after == canonical_before, "canonical bytes stable during check")
for path, expected in list(bound.items()):
    check((ROOT / path).is_file() and sha(ROOT / path) == expected,
          "all bound bytes stable at completion", path)
result = {
    "status": "PASS" if not issues else "FAIL",
    "mode": "FINAL_SEAL" if args.seal_once else "PREFLIGHT",
    "started_utc": started, "completed_utc": datetime.now(timezone.utc).isoformat(),
    "scope": "Record bytes, disclosed execution provenance, local routing and stability only",
    "does_not_certify": "Mathematical truth, novelty, nonendpoint exhaustion or universal STCI resolution",
    "mathematical_verifiers_rerun": False, "mathematical_execution_count": 0,
    "checker_sha256": sha(Path(__file__)), "head_observed": head,
    "check_count": len(checks), "checked_local_links": checked_links,
    "bound_files_sha256": bound, "canonical_before_sha256": canonical_before,
    "canonical_after_sha256": canonical_after,
    "changed_prior_canonical_bindings": changed_canonical,
    "counts": {"prior_checks": 5747, "prior_links": 773, "prior_files": 921,
               "independent_review_declared_comparisons": 77,
               "independent_review_observed_files": len(inventory["files"]),
               "independent_review_scoped_executions": 35,
               "endpoint_captured_executions": 28,
               "endpoint_direct_tool_observations_separate": 5,
               "nonendpoint_captured_executions": 5,
               "nonendpoint_final_conditions": 7},
    "issues": issues, "scoped_local_link_edges": edges,
    "required_audited_routes": accepted["required_audited_routes"],
    "transitively_scanned_notes": sorted(scanned),
    "notation_exclusions": excluded_notation,
    "limits": ["No mathematical verifier is run by this checker.",
               "Inventory categories are separately scoped, not an aggregate theorem or independent-verifier count.",
               "Original metadata-only rows, reconstructed sources and absent original raw-stream hashes retain their disclosed limits.",
               "The prior seal is historical; only seven named canonical files are reconciled here.",
               "The interrupted draft checker is retained, not represented as finally executed.",
               "Inline Markdown links are checked outside code; reference-style links and balanced-parenthesis destinations are not parsed.",
               "The nonendpoint direct proof still requires a separate mathematical audit."]}
with target.open("x" if args.seal_once else "w") as stream:
    stream.write(json.dumps(result, indent=2) + "\n")
print(f"{result['status']}: {result['mode']}; {len(checks)} record checks, {checked_links} links; no mathematical execution")
if issues:
    print(json.dumps(issues, indent=2))
raise SystemExit(0 if not issues else 1)
