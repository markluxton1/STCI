#!/usr/bin/env python3
"""Independent October 10 record check; never executes a math verifier.

Run --preliminary while root is reconciling canonical routing. Run --seal-once
after root declares those edits ready. The final mode refuses to overwrite its
own result. This is a provenance and routing check, not proof of mathematics.
"""
from argparse import ArgumentParser
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
HIST = ROOT / "research/validation/2026-10-09-late-continuation-seal"
INDEX = ROOT / "research/validation/2026-10-08-continuation-index/index.json"
REPLAY = ROOT / "research/validation/2026-10-10-genus-one-root-replay"
INTERFACES = ROOT / "research/validation/2026-10-10-genus-one-interfaces"
REPEATED = ROOT / "research/validation/2026-10-10-repeated-partitions-independent-audit"
LINE_POSITIONS = ROOT / "research/validation/2026-10-10-genus-two-line-positions"
CANONICAL = [
    "README.md", "research/AUDITED_STATE_2026-10-07.md",
    "research/RESEARCH_UPDATE_2026-10-07.md", "research/SUCCESSOR_HANDOFF_2026-10-07.md",
    "research/computations/README.md", "research/LITERATURE_LEDGER.md",
    "research/RESEARCH_RECORD.md",
]
RECONCILIATION_EXCEPTIONS = set(CANONICAL) | {
    "research/RESEARCH_RECORD.md", "research/RESEARCH_REPORT.md",
    "research/SUCCESSOR_HANDOFF.md", "research/AUDITED_STATE_2026-10-06.md",
    "research/CODEX_RESUME_2026-10-06.md",
    "research/notes/2026-10-09-session-delpezzo-D5-torsion-filter.md",
}
PROOF_ROUTING = [
    "research/notes/2026-10-09-session-genus-one-delpezzo-reduction.md",
    "research/notes/2026-10-09-session-rational-genus-one-ADE-independent-audit.md",
    "research/notes/2026-10-09-session-delpezzo-D5-torsion-filter.md",
    "research/notes/2026-10-09-session-delpezzo-D5-root-independent-audit.md",
    "research/notes/2026-10-09-session-genus-one-entire-conductor.md",
    "research/notes/2026-10-09-session-genus-one-entire-conductor-algebra-independent-audit.md",
    "research/notes/2026-10-09-session-quadratic-conductor-power-descent.md",
    "research/notes/2026-10-09-session-quadratic-conductor-power-descent-independent-audit.md",
    "research/notes/2026-10-09-session-genus-one-ribbon-net-independent-audit.md",
    "research/notes/2026-10-09-session-genus-one-uniform-projection-adversarial.md",
    "research/notes/2026-10-09-session-ribbon-211-projection-independent-audit.md",
    "research/notes/2026-10-09-session-ribbon-4-root-independent-proof.md",
    "research/notes/2026-10-09-session-ribbon-22-bounded-power-obstruction.md",
    "research/notes/2026-10-09-session-ribbon-repeated-partitions-complete.md",
    "research/notes/2026-10-10-session-genus-one-interface-independent-audit.md",
    "research/notes/2026-10-10-session-ribbon-repeated-partitions-independent-audit.md",
    "research/notes/2026-10-09-session-genus-two-adjoint-conic-model.md",
    "research/notes/2026-10-09-session-genus-two-adjoint-independent-audit.md",
    "research/notes/2026-10-09-session-genus-two-degree-one-counteraudit.md",
    "research/notes/2026-10-09-session-genus-two-nullcurve-mate-independent-audit.md",
    "research/notes/2026-10-10-session-genus-two-entire-conductor-independent-audit.md",
    "research/notes/2026-10-10-session-genus-two-marking-and-section-pause-audit.md",
    "research/notes/2026-10-10-session-genus-two-lambda-one-marked-prime-audit.md",
    "research/notes/2026-10-10-session-genus-two-lambda1-horizontal-line-budget.md",
    "research/notes/2026-10-10-session-genus-two-no-zero-horizontal-independent-audit.md",
    "research/notes/2026-10-10-session-genus-two-blowup-lift-normality-proposed-audit.md",
    "research/notes/2026-10-10-session-genus-two-blowup-lift-normality-independent-audit.md",
]
STATUS_TRACKED = [
    "research/notes/2026-10-10-session-genus-two-conductor-line-position.md",
    "research/notes/2026-10-10-session-genus-two-trisecant-quartic-carriers.md",
    "research/notes/2026-10-10-session-genus-two-endpoint-irreducible-conic-obstruction.md",
    "research/notes/2026-10-10-session-genus-two-nonendpoint-trisecant-conic-obstruction.md",
    "research/notes/2026-10-10-session-genus-two-bisection-even-fiber-exclusion.md",
    "research/notes/2026-10-10-session-genus-two-bisection-second-pencil-independent-audit.md",
]

parser = ArgumentParser()
mode = parser.add_mutually_exclusive_group(required=True)
mode.add_argument("--preliminary", action="store_true")
mode.add_argument("--seal-once", action="store_true")
parser.add_argument("--acceptance", default="research/notes/2026-10-10-session-results-acceptance.md")
args = parser.parse_args()
target = HERE / ("result.json" if args.seal_once else "preliminary-result.json")
if args.seal_once and target.exists():
    raise SystemExit("Refusing to overwrite frozen result.json; use a distinct later seal directory.")

sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
relative = lambda p: str(Path(p).relative_to(ROOT))
checks, issues, warnings, bound = [], [], [], {}

def check(condition, label, detail=None):
    item = {"check": label, "passed": bool(condition), "detail": detail}
    checks.append(item)
    if not condition:
        issues.append(item)

def bind(path):
    path = Path(path)
    check(path.is_file(), "file exists", relative(path))
    if path.is_file():
        bound[relative(path)] = sha(path)
    return path

def read(path):
    return json.loads(bind(path).read_text())

def matches(path, expected, label):
    path = bind(path)
    if path.is_file():
        observed = sha(path)
        check(observed == expected, label,
              {"path": relative(path), "expected": expected, "observed": observed})

started = datetime.now(timezone.utc).isoformat()
bind(Path(__file__))
bind(HERE / "README.md")
bind(HERE / "scope-review-before-reconciliation.md")
freeze_paths = list(CANONICAL)
if (ROOT / args.acceptance).exists():
    freeze_paths.append(args.acceptance)
canonical_before = {p: sha(bind(ROOT / p)) for p in freeze_paths}

# The older index and seal are historical artifacts, not today's live proof list.
index = read(INDEX)
old = read(HIST / "result.json")
old_manifest = read(HIST / "execution-manifest.json")
matches(HIST / "result.json", old_manifest["result_sha256"], "historical seal result bytes")
matches(HIST / "check_record.py", old_manifest["auditor_source_sha256"], "historical seal checker bytes")
matches(INDEX, old["bound_files_sha256"][relative(INDEX)], "frozen historical index bytes")
check(index["counts"]["combined_distinct_top_level_sources"] == 97,
      "historical 97 sources unchanged")
check(index["counts"]["combined_explicitly_indexed_executions"] == 110,
      "historical 110 executions unchanged")
check(old["check_count"] == 2006 and old["checked_local_links"] == 313,
      "historical 2006 checks and 313 scoped links unchanged")
old_sources = {r["source"] for r in index["latest_source_results"]}
check(len(old_sources) == len(index["latest_source_results"]) == 97,
      "historical latest result paths are distinct")
for row in index["latest_source_results"]:
    check(row["status"] == "PASS" and row.get("exit_code", 0) == 0,
          "historical latest execution status retained", row["source"])
    matches(ROOT / row["source"], row["source_sha256"], "historical latest mathematical source still matches")
    matches(ROOT / row["log"], row.get("log_sha256", row.get("observed_log_sha256")),
            "historical latest retained log still matches its recorded digest")
    if "snapshot_source" in row:
        matches(ROOT / row["snapshot_source"], row["source_sha256"],
                "historical latest source snapshot still matches")
changed_since_old_seal = []
missing_since_old_seal = []
for p, digest in old["bound_files_sha256"].items():
    candidate = ROOT / p
    if candidate.is_file() and sha(candidate) != digest:
        changed_since_old_seal.append(p)
    elif not candidate.is_file():
        missing_since_old_seal.append(p)
    if p not in RECONCILIATION_EXCEPTIONS:
        matches(candidate, digest, "noncanonical historical bound file remains unchanged")
    else:
        bind(candidate)
check(not missing_since_old_seal, "historically bound files still exist", missing_since_old_seal)

# New independent M2 companions. Failed attempts are evidence, not passes.
interface_record = read(INTERFACES / "execution-record.json")
matches(ROOT / interface_record["passing_source"], interface_record["passing_source_sha256"],
        "interface passing source bytes")
check([a["exit_code"] for a in interface_record["attempts"]] == [1, 0],
      "both interface attempts retained")
recovered = HERE / "interfaces-namespace-failed-reconstructed.m2"
matches(recovered, interface_record["attempts"][0]["source_sha256"],
        "reconstructed interface namespace failure equals original recorded pre-run hash")
passing_bytes = (ROOT / interface_record["passing_source"]).read_bytes()
check(recovered.read_bytes() == passing_bytes.replace(b"netCoefficients", b"net"),
      "interface failed source reconstructed by only the recorded identifier reversal")
warnings.append("The recovered interface failed source is a mechanical reconstruction matched to its recorded pre-run SHA, not a contemporaneous snapshot.")

repeated_record = read(REPEATED / "execution-record.json")
for row in repeated_record["frozen_files"]:
    matches(ROOT / row["path"], row["sha256"], "independent repeated-audit bound file")
repeated_result = read(REPEATED / "result.json")
failures = read(REPEATED / "failed-attempts.json")
check(repeated_record["status"] == repeated_result["status"] == "PASS"
      and repeated_record["exit_code"] == 0
      and repeated_record["checked_conditions"] == repeated_result["checked_conditions"] == 29,
      "independent repeated-audit passing fields agree")
check(len(failures["attempts"]) == 3 and all(a["exit_code"] == 1 for a in failures["attempts"]),
      "three failed repeated-audit attempts retained")
check(failures["mathematical_assertion_failures"] == [],
      "failed setup attempts not misclassified as mathematical assertion failures")
for attempt in failures["attempts"]:
    failed_source = bind(REPEATED / attempt["retained_source"])
    if "retained_source_sha256" in attempt:
        matches(failed_source, attempt["retained_source_sha256"], "failed repeated source digest")
namespace_provenance = failures["attempts"][1]["source_provenance"]
check("reconstructed" in namespace_provenance and "No original pre-run source hash" in namespace_provenance,
      "namespace reconstruction limitation explicitly preserved")
warnings.append("Repeated-audit protected-name source was mechanically reconstructed without an original pre-run hash; the parser-failed source was retained and hashed.")
warnings.append("Agent successful-stdout.txt is a faithful saved transcript after the run. Raw captured subprocess streams are in the separate root replay.")
warnings.append("The earlier [211] note's checker attribution is superseded by the October10 interface audit. Historical PASS runs are not retroactively represented as checking identities absent from that source.")

# Root ran exact copies in a separate working directory. Copies are not verifiers.
manifest = read(REPLAY / "execution-manifest.json")
matches(REPLAY / "run_replay.py", manifest["runner_sha256"], "root replay runner bytes")
check(manifest["status"] == "PASS" and len(manifest["executions"]) == 2,
      "two root-observed isolated replays pass")
source_paths = set()
for row in manifest["executions"]:
    source_paths.add(row["source_path"])
    matches(ROOT / row["source_path"], row["source_sha256"], "root replay live source bytes")
    matches(ROOT / row["snapshot_source"], row["snapshot_sha256"], "root replay snapshot source bytes")
    check(row["source_sha256"] == row["snapshot_sha256"], "root replay copies exact source bytes")
    check(row["command"] == ["/opt/homebrew/bin/M2", "--script", str(ROOT / row["snapshot_source"])],
          "root replay command uses its declared snapshot")
    check(row["cwd"] == str(REPLAY / "snapshot"), "root replay isolated cwd")
    matches(ROOT / row["stdout_path"], row["stdout_sha256"], "root replay captured stdout bytes")
    matches(ROOT / row["stderr_path"], row["stderr_sha256"], "root replay captured stderr bytes")
    stdout = (ROOT / row["stdout_path"]).read_bytes()
    check(row["exit_code"] == 0 and row["status"] == "PASS"
          and row["expected_terminal_text"].encode() in stdout,
          "root replay terminal PASS observed in raw stream", row["name"])
check(len(source_paths) == 2 and not source_paths.intersection(old_sources),
      "two new mathematical source paths relative to the historical 97-source index")
check(manifest["new_distinct_sources"] == 2 and manifest["new_explicit_executions"] == 2,
      "replay declared counts interpreted relative to old index only")
check(manifest["executions"][0]["source_sha256"] == interface_record["passing_source_sha256"],
      "root interface replay is the independently run source")
matches(REPLAY / "snapshot/research/validation/2026-10-10-repeated-partitions-independent-audit/result.json",
        sha(REPEATED / "result.json"), "isolated repeated replay regenerates exact declared result")
check((REPLAY / "interfaces-211.stdout.txt").read_text()
      == interface_record["attempts"][-1]["stdout"],
      "root raw interface stdout equals independently recorded successful stdout")
check((REPLAY / "repeated-partitions.stdout.txt").read_bytes()
      == (REPEATED / "successful-stdout.txt").read_bytes(),
      "root raw repeated stdout equals independently saved transcript")

# Scope is explicit: count only these two successful-source histories, not probes
# or owner Python sources written before October 10. Do not add them to 97/110.
scoped_attempts = (interface_record["attempts"] + failures["attempts"]
                   + [repeated_record] + manifest["executions"])
def command_text(row):
    command = row["command"]
    return " ".join(command) if isinstance(command, list) else command
m2_attempts = [r for r in scoped_attempts if "/opt/homebrew/bin/M2 " in command_text(r)]
import_failed = [r for r in scoped_attempts if "countercheck.py" in command_text(r)]
check(len(scoped_attempts) == 8 and len(m2_attempts) == 7 and len(import_failed) == 1,
      "scoped process accounting derived from explicit retained attempt rows")
counts = {
    "historical_distinct_sources": 97, "historical_explicit_executions": 110,
    "historical_integrity_checks": 2006, "historical_scoped_local_links": 313,
    "oct10_scoped_distinct_successful_mathematical_source_paths": len(source_paths),
    "oct10_scoped_successful_m2_executions_including_replays": sum(r["exit_code"] == 0 for r in m2_attempts),
    "oct10_scoped_failed_m2_executions": sum(r["exit_code"] != 0 for r in m2_attempts),
    "oct10_scoped_import_failed_python_execution": len(import_failed),
    "oct10_scoped_total_recorded_attempts_including_import_failure": len(scoped_attempts),
    "root_replays_additional_distinct_sources_beyond_agent_runs": 0,
    "root_replay_additional_successful_executions": sum(r["exit_code"] == 0 for r in manifest["executions"]),
    "oct10_independent_conditions": {"interfaces_211": 42, "repeated_partitions": 29},
}

# This is a separate structural identity source, not another genus-one verifier
# or a mate exclusion. Its record expressly lacks superseded failed bytes.
line_record = read(LINE_POSITIONS / "execution-record.json")
matches(ROOT / line_record["source"], line_record["source_sha256"],
        "line-position structural source bytes")
check(line_record["status"] == "PASS" and line_record["execution"]["exit_code"] == 0
      and "17 checks" in line_record["execution"]["stdout"],
      "line-position observed structural identity pass")
check(len(line_record["development_failures"]) == 2
      and all(r["exit_code"] == 1 for r in line_record["development_failures"]),
      "line-position two development failures explicitly retained")
check("does not claim that superseded development source bytes were preserved"
      in line_record["provenance_boundary"],
      "line-position historical source-byte limitation explicit")
check(line_record["source"] not in source_paths | old_sources,
      "line-position source is distinct from genus-one controls and historical index")
counts["separate_line_position_structural_source_paths"] = 1
counts["separate_line_position_passing_executions"] = 1
counts["separate_line_position_failed_development_executions"] = 2
counts["separate_line_position_exact_identities"] = 17
warnings.append("Line-position identities have an observed nonisolated passing record; two development failures survive in the record, but their superseded source bytes were not preserved. This source alone asserts no mate exclusion.")

blowup_audit = bind(ROOT / "research/notes/2026-10-10-session-genus-two-blowup-lift-normality-independent-audit.md")
blowup_digests = re.findall(r"`([0-9a-f]{64})`", blowup_audit.read_text())
check(len(blowup_digests) >= 2, "normal-T audit has exact owner and conductor input digests")
if len(blowup_digests) >= 2:
    matches(ROOT / "research/notes/2026-10-10-session-genus-two-blowup-lift-normality-proposed-audit.md",
            blowup_digests[0], "normal-T owner proof matches independently audited bytes")
    matches(ROOT / "research/notes/2026-10-10-session-genus-two-entire-conductor-independent-audit.md",
            blowup_digests[1], "normal-T conductor input matches independently audited bytes")

# File routes and local links. This audits target existence, not external sources
# and not whether a referenced theorem has correct hypotheses.
acceptance = ROOT / args.acceptance
all_routing = list(CANONICAL) + PROOF_ROUTING + STATUS_TRACKED
if acceptance.exists():
    all_routing.append(args.acceptance)
elif args.seal_once:
    check(False, "final October10 acceptance exists", args.acceptance)
else:
    warnings.append("Root acceptance/routing is still pending; this preliminary result cannot be used as a final seal.")

checked_links = 0
broken_links = []
for p in dict.fromkeys(all_routing):
    path = bind(ROOT / p)
    if not path.is_file():
        continue
    text = path.read_text()
    for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", text):
        target_url = match.group(1).strip().split(" ", 1)[0].strip("<>")
        parsed = urlparse(target_url)
        if parsed.scheme or target_url.startswith("#"):
            continue
        decoded = unquote(parsed.path)
        candidate = Path(decoded) if decoded.startswith("/") else path.parent / decoded
        checked_links += 1
        if not candidate.exists():
            detail = {"file": p, "target": target_url, "line": text[:match.start()].count("\n") + 1}
            broken_links.append(detail)
        check(candidate.exists(), "local Markdown link target exists",
              {"file": p, "target": target_url})

if args.seal_once and acceptance.exists():
    for p in CANONICAL:
        check(Path(args.acceptance).name in (ROOT / p).read_text(),
              "canonical file routes to October10 acceptance", p)
    atext = acceptance.read_text()
    for required in (
        "2026-10-10-session-genus-one-interface-independent-audit.md",
        "2026-10-10-session-ribbon-repeated-partitions-independent-audit.md",
        "2026-10-10-session-genus-two-entire-conductor-independent-audit.md",
        "2026-10-10-session-genus-two-marking-and-section-pause-audit.md",
        "2026-10-10-session-genus-two-blowup-lift-normality-independent-audit.md",
    ):
        check(required in atext, "acceptance routes to critical independent audit", required)
    state = (ROOT / "research/AUDITED_STATE_2026-10-07.md").read_text()
    check("unresolved" in state and "characteristic-zero" in state,
          "canonical state retains unrestricted open status")

status_headers = {}
for p in STATUS_TRACKED:
    if (ROOT / p).exists():
        status_headers[p] = "\n".join((ROOT / p).read_text().splitlines()[:12])

head_process = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True)
head = head_process.stdout.strip()
check(head_process.returncode == 0, "read-only live HEAD observation")
diff = subprocess.run(["git", "diff", "--check"], cwd=ROOT, capture_output=True, text=True)
check(diff.returncode == 0, "git diff --check", diff.stdout + diff.stderr)
canonical_after = {p: sha(ROOT / p) for p in freeze_paths}
check(canonical_after == canonical_before, "canonical files unchanged during this record check")

result = {
    "status": "PASS" if not issues else "FAIL",
    "mode": "FINAL_SEAL" if args.seal_once else "PRELIMINARY",
    "started_utc": started, "completed_utc": datetime.now(timezone.utc).isoformat(),
    "scope": "Record provenance, explicitly scoped execution accounting, local target routing and canonical freeze observation only",
    "does_not_certify": "Mathematical proofs, novelty, genus-two mate exclusion, higher carrier degrees, positive characteristic or universal STCI resolution",
    "mathematical_verifiers_rerun": False, "head_observed": head,
    "checker_sha256": sha(Path(__file__)), "counts": counts,
    "check_count": len(checks), "checked_local_links": checked_links,
    "bound_files_sha256": bound, "canonical_before_sha256": canonical_before,
    "canonical_after_sha256": canonical_after,
    "historically_bound_files_changed_since_oct9_seal": changed_since_old_seal,
    "historically_bound_files_missing_since_oct9_seal": missing_since_old_seal,
    "broken_local_links": broken_links, "issues": issues, "warnings": warnings,
    "separately_scoped_new_note_headers": status_headers,
    "checks": checks,
    "limits": [
        "The historical 97/110 index and 2006/313 seal remain frozen. New records do not retroactively enlarge their scope.",
        "October10 counts cover only the two independent M2 mathematical source histories and root replays. Runtime import/version probes and earlier post-seal owner computations are not counted.",
        "Copied sources do not create new verifiers. Replaying 42 and 29 conditions is two more executions, not another 71 independent conditions.",
        "Historical source-byte and log limitations in the older index remain unchanged.",
        "A local link target existing does not verify the mathematical proposition or the external primary source it cites.",
    ],
}
target.write_text(json.dumps(result, indent=2) + "\n")
print(f"{result['status']}: {result['mode']}; {len(checks)} record checks, {checked_links} scoped local links; no mathematical verifier rerun")
if issues:
    print(json.dumps(issues, indent=2))
raise SystemExit(0 if not issues else 1)
