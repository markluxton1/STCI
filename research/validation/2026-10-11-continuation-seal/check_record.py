#!/usr/bin/env python3
"""Independent October 11 continuation record check; never executes a math verifier.

Run --preliminary while root is reconciling canonical routing. Run --preflight
to exercise final routing gates without freezing, then --seal-once after root
declares those edits ready. The final mode refuses to overwrite its
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
PREPARED = ROOT / "research/validation/2026-10-10-continuation-seal"
HIST = ROOT / "research/validation/2026-10-09-late-continuation-seal"
INDEX = ROOT / "research/validation/2026-10-08-continuation-index/index.json"
REPLAY = ROOT / "research/validation/2026-10-10-genus-one-root-replay"
INTERFACES = ROOT / "research/validation/2026-10-10-genus-one-interfaces"
REPEATED = ROOT / "research/validation/2026-10-10-repeated-partitions-independent-audit"
LINE_POSITIONS = ROOT / "research/validation/2026-10-10-genus-two-line-positions"
NORMAL_BUNDLE = ROOT / "research/validation/2026-10-10-quartic-normal-bundle-independent-audit"
NORMAL_REPLAY = ROOT / "research/validation/2026-10-10-normal-bundle-root-replay"
NONENDPOINT = ROOT / "research/validation/2026-10-10-genus-two-nonendpoint-trisecant-continuation-audit"
ENDPOINT = ROOT / "research/validation/2026-10-10-endpoint-local-ade"
ENDPOINT_REPLAY = ROOT / "research/validation/2026-10-10-endpoint-root-replay"
DOUBLE_HORIZONTAL = ROOT / "research/validation/2026-10-10-genus-two-double-horizontal"
FILTRATION = ROOT / "research/validation/2026-10-11-multiplicity-ten-filtration"
ROOT_READY_QUINTIC_INPUTS = {
    "research/notes/2026-10-11-session-quintic-structural-frontier.md":
        "4e84d1183435f8509df48b6b1d02fb4f00f29736ec8670bb09b2577dc991595b",
    "research/notes/2026-10-11-session-quintic-conormal-and-delpezzo-audit.md":
        "9cf5438894e3fb07f2094b4bcc1280ec0ead01822155d3897aceb73ffc1011fb",
    "research/notes/2026-10-11-session-multiplicity-ten-filtration-audit.md":
        "90bd87fad8cf0f10fe39b4e8d9c3946fc38a3424d497ce3f5ad969c5047221e3",
}
HISTORICAL_TRUST_ANCHORS = {
    "research/validation/2026-10-09-late-continuation-seal/result.json":
        "5644fd5832f641a14d203c9692c05a9864fb11cf15aa9306aeea68e9aee6381a",
    "research/validation/2026-10-09-late-continuation-seal/check_record.py":
        "881db0a3cbeb087d18cbd01bf40eb450a0cea44ce1807350c11886a454d60058",
    "research/validation/2026-10-09-late-continuation-seal/execution-manifest.json":
        "51551d668fc870f8f0bfab18ad3c42f8e95401228f443c4aaa811b1e6ab5a75a",
    "research/validation/2026-10-08-continuation-index/index.json":
        "daeff78d9a57ddb968e0ff910838e41624c03150e490459a0ae876fa71ca23e8",
    "research/notes/2026-10-10-session-results-acceptance.md":
        "497d8500831833674ebaf5fdd3d6686ffacfd7f7d47021087ddfe276999c4696",
}
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
    "research/notes/2026-10-10-session-genus-two-bisection-quadratic-descent.md",
]

parser = ArgumentParser()
mode = parser.add_mutually_exclusive_group(required=True)
mode.add_argument("--preliminary", action="store_true")
mode.add_argument("--preflight", action="store_true")
mode.add_argument("--seal-once", action="store_true")
parser.add_argument("--acceptance", default="research/notes/2026-10-11-session-all-quartic-results-acceptance.md")
args = parser.parse_args()
final_routing = args.seal_once or args.preflight
target = HERE / ("result.json" if args.seal_once else
                 "preflight-result.json" if args.preflight else "preliminary-result.json")
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
        key, digest = relative(path), sha(path)
        if key in bound:
            check(bound[key] == digest, "bound file has not changed since first observation", key)
        else:
            bound[key] = digest
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
head_before_process = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                                     capture_output=True, text=True)
head_before = head_before_process.stdout.strip()
check(head_before_process.returncode == 0, "initial read-only live HEAD observation")
bind(Path(__file__))
bind(HERE / "README.md")
bind(HERE / "validation-scope-review.md")
bind(HERE / "run_final_seal.py")
preparation = read(HERE / "preparation-source.json")
matches(HERE / preparation["snapshot"], preparation["original_sha256"],
        "exact prepared October10 checker preserved before extension")
check(preparation["original_final_result_exists"] is False,
      "prepared October10 checker had not produced a final seal")
matches(ROOT / preparation["original_prepared_checker"], preparation["original_sha256"],
        "prepared October10 checker remains unchanged")
transitive_failure = read(HERE / "transitive-scan-first-failure/observation.json")
for name, digest in transitive_failure["copied_sha256"].items():
    matches(HERE / "transitive-scan-first-failure" / name, digest,
            "first extended transitive-scan failure exact observation bytes")
check(transitive_failure["observed_exit_code"] == 1
      and transitive_failure["mathematical_verifiers_rerun"] is False,
      "transitive scan draft-link and parser observation was not a mathematical failure")
bind(PREPARED / "scope-review-before-reconciliation.md")
bind(PREPARED / "resume-scope-observation-2026-10-10.md")
bind(PREPARED / "checker-coverage-review.md")
draft_link_failure = read(PREPARED / "draft-link-failure-observation/observation.json")
matches(PREPARED / "draft-link-failure-observation/check_record.py",
        draft_link_failure["checker_source_sha256"], "temporary draft-link failure exact checker copy")
matches(PREPARED / "draft-link-failure-observation/preliminary-result.json",
        draft_link_failure["result_sha256"], "temporary draft-link failure result retained")
check(draft_link_failure["observed_exit_code"] == 1
      and draft_link_failure["mathematical_verifiers_rerun"] is False
      and "not a mathematical assertion failure" in draft_link_failure["classification"],
      "temporary incomplete-draft routing failure not misclassified as mathematical failure")
runtime_record = read(PREPARED / "resume-runtime-observation.json")
matches(PREPARED / "capture_runtime.py", runtime_record["capture_source_sha256"],
        "resume read-only runtime capture source bytes")
check(runtime_record["mathematical_execution_count"] == 0,
      "runtime probes add no mathematical execution")
check(len(runtime_record["observations"]) == 3
      and all(r["exit_code"] == 0 for r in runtime_record["observations"]),
      "three read-only runtime probes completed")
python_runtime = json.loads(runtime_record["observations"][2]["stdout"])
check(python_runtime["sympy_available"] is False,
      "resume historical CAS path has no SymPy in observed runtime")
check(runtime_record["observations"][1]["stdout"].strip() == "1.26.06",
      "resume Macaulay2 version observed without mathematical execution")
new_note_paths = [relative(p) for p in sorted((ROOT / "research/notes").glob("2026-10-1[01]*.md"))]
freeze_paths = list(CANONICAL)
if (ROOT / args.acceptance).exists():
    freeze_paths.append(args.acceptance)
canonical_before = {p: sha(bind(ROOT / p)) for p in freeze_paths}

# The older index and seal are historical artifacts, not today's live proof list.
for p, digest in HISTORICAL_TRUST_ANCHORS.items():
    matches(ROOT / p, digest, "independently observed frozen historical trust anchor")
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
d5_live = bind(ROOT / "research/notes/2026-10-09-session-delpezzo-D5-torsion-filter.md")
d5_snapshot = bind(ROOT / "research/validation/2026-10-09-D5-root-audit/proof-snapshots/research/notes/2026-10-09-session-delpezzo-D5-torsion-filter.md")
matches(d5_live, "9364c23bb3feb71c01be32ec7c0d583525660107be9bf36c97c998860a7757ef",
        "D5 current acceptance/routing-only revision matches independently observed bytes")
def d5_mathematical_sections(path):
    text = path.read_text()
    return text[text.index("## 1."):text.index("## 6.")]
check(d5_mathematical_sections(d5_live) == d5_mathematical_sections(d5_snapshot),
      "D5 mathematical proof sections 1 through 5 remain byte-identical to frozen snapshot")
warnings.append("The D5 source's status header and sections 6--7 acceptance/model-coverage routing changed after the historical seal; its mathematical sections 1--5 remain byte-identical. This is a precisely bounded exception, not permission for arbitrary proof edits.")

# New independent M2 companions. Failed attempts are evidence, not passes.
interface_record = read(INTERFACES / "execution-record.json")
matches(ROOT / interface_record["passing_source"], interface_record["passing_source_sha256"],
        "interface passing source bytes")
check([a["exit_code"] for a in interface_record["attempts"]] == [1, 0],
      "both interface attempts retained")
recovered = PREPARED / "interfaces-namespace-failed-reconstructed.m2"
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
historical_source_sum = sum(index["counts"][k] for k in (
    "retained_baseline_distinct_sources", "continuation_distinct_sources",
    "separate_first_endpoint_countercheck_sources_and_executions",
    "separate_principal_independent_sources_and_executions",
    "separate_family2_independent_sources", "explicit_extension_additional_distinct_sources"))
historical_execution_sum = sum(index["counts"][k] for k in (
    "retained_baseline_indexed_executions", "continuation_execution_records",
    "separate_strengthened_veronese_revision_execution",
    "separate_first_endpoint_countercheck_sources_and_executions",
    "separate_principal_independent_sources_and_executions",
    "separate_family2_explicit_executions", "explicit_extension_execution_records"))
check(historical_source_sum == 97 and historical_execution_sum == 110,
      "historical component counts derive exactly 97 distinct sources and 110 indexed executions",
      {"source_components_sum": historical_source_sum,
       "execution_components_sum": historical_execution_sum})

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

# Fresh independent Jacobian certificate, separately replayed by root. Its
# copied source adds an execution, not a mathematical source or a new theorem.
normal_record = read(NORMAL_BUNDLE / "execution-record.json")
normal_manifest = read(NORMAL_REPLAY / "execution-manifest.json")
normal_failure = read(NORMAL_BUNDLE / "namespace-failed-record.json")
matches(ROOT / normal_record["source"], normal_record["source_sha256"],
        "independent normal-bundle passing source bytes")
matches(ROOT / normal_manifest["snapshot"], normal_manifest["snapshot_sha256"],
        "normal-bundle root replay exact snapshot bytes")
check(normal_record["source"] == normal_manifest["source"]
      and normal_record["source_sha256"] == normal_manifest["source_sha256"]
      == normal_manifest["snapshot_sha256"],
      "normal-bundle root and agent use one exact source revision")
check(normal_record["exit_code"] == normal_manifest["exit_code"] == 0
      and normal_manifest["status"] == "PASS"
      and normal_record["expected_check_count"] == normal_manifest["expected_exact_checks"] == 8,
      "normal-bundle two passing execution records declare eight checks")
check(normal_manifest["command"] == ["/opt/homebrew/bin/M2", "--script",
                                    str(ROOT / normal_manifest["snapshot"])],
      "normal-bundle root command uses declared exact snapshot")
check(normal_manifest["cwd"] == str(NORMAL_REPLAY / "snapshot"),
      "normal-bundle root replay uses isolated cwd")
bind(NORMAL_REPLAY / "run_replay.py")
for stream_name in ("stdout", "stderr"):
    stream = NORMAL_REPLAY / f"{stream_name}.txt"
    matches(stream, normal_manifest[f"{stream_name}_sha256"],
            f"normal-bundle root raw {stream_name} bytes")
    agent_stream = bind(NORMAL_BUNDLE / normal_record[stream_name])
    check(stream.read_bytes() == agent_stream.read_bytes(),
          f"normal-bundle root raw {stream_name} equals independently captured agent stream")
check(normal_record["success_marker"].encode() in (NORMAL_REPLAY / "stdout.txt").read_bytes(),
      "normal-bundle raw replay stream contains eight-check terminal PASS")
matches(NORMAL_BUNDLE / normal_failure["source"], normal_failure["sha256"],
        "normal-bundle namespace-failed source bytes retained")
bind(NORMAL_BUNDLE / "namespace-failed-tool-output.txt")
check(normal_failure["exit_code"] == 1
      and "before any assertion" in normal_failure["classification"]
      and "separate stdout and stderr were not captured" in normal_failure["stream_fidelity"],
      "normal-bundle scaffold failure and combined-stream limitation retained")
check(normal_record["source"] not in old_sources | source_paths | {line_record["source"]},
      "normal-bundle certificate source distinct from previously scoped sources")
counts.update({
    "separate_normal_bundle_successful_source_paths": 1,
    "separate_normal_bundle_successful_m2_executions_including_root_replay": 2,
    "separate_normal_bundle_failed_namespace_executions": 1,
    "separate_normal_bundle_exact_identities_and_rank_checks": 8,
    "normal_bundle_root_replay_additional_distinct_sources": 0,
})
warnings.append("Normal-bundle identities and rank checks are separately scoped. The root replay adds one execution of the same source, not a new verifier. A retained namespace failure has combined tool output rather than separately captured streams. The geometric ribbon application requires its separate written proof.")

# The nonendpoint repair changes only protected names in one original symbolic
# checker. It is one checker lineage, not an extra independent proof source.
nonendpoint_record = read(NONENDPOINT / "execution-record.json")
nonendpoint_result = read(NONENDPOINT / "result.json")
nonendpoint_source = Path(nonendpoint_record["source_path"])
matches(nonendpoint_source, nonendpoint_record["source_sha256"],
        "nonendpoint repaired passing source exact bytes")
nonendpoint_original = bind(ROOT / "research/validation/2026-10-10-genus-two-nonendpoint-trisecant-independent-audit/cartan-countercheck.m2")
def rename_nonendpoint_token(match):
    if match.group(1):
        return {b"source": b"chainSource", b"denominator": b"chainDenominator"}[match.group(1)]
    return match.group(0)
repaired_expected = re.sub(rb'"(?:\\.|[^"\\])*"|\b(source|denominator)\b',
                           rename_nonendpoint_token, nonendpoint_original.read_bytes())
repaired_expected = repaired_expected.replace(b'"positive denominator identity"',
                                              b'"positive chainDenominator identity"')
check(nonendpoint_source.read_bytes() == repaired_expected,
      "nonendpoint repair changes only declared identifiers and one printed condition label")
check(nonendpoint_result["status"] == "PASS" and nonendpoint_result["checked_conditions"] == 12,
      "nonendpoint generated result agrees with twelve-check scope")
check(nonendpoint_record["status"] == "PASS" and nonendpoint_record["exit_code"] == 0
      and nonendpoint_record["isolated_replay"] is True
      and nonendpoint_record["new_distinct_mathematical_source"] is False,
      "nonendpoint successful isolated execution preserves one checker lineage")
nonendpoint_attempts = []
for i, record_name in enumerate(nonendpoint_record["preserved_failures"], start=1):
    attempt = read(NONENDPOINT / record_name)
    source = NONENDPOINT / f"attempt{i:02d}-failure-source.m2"
    matches(source, attempt["source_sha256"], "nonendpoint failed source revision exact bytes")
    bind(NONENDPOINT / f"attempt{i:02d}-failure-stdout.txt")
    bind(NONENDPOINT / f"attempt{i:02d}-failure-stderr.txt")
    check(attempt["exit_code"] == 1 and attempt["status"] == "FAIL",
          "nonendpoint failure retained without promotion to a pass")
    nonendpoint_attempts.append(attempt)
for stream in ("stdout.txt", "stderr.txt"):
    bind(NONENDPOINT / stream)
bind(NONENDPOINT / "README.md")
check("12" in (NONENDPOINT / "stdout.txt").read_text()
      and "PASS" in (NONENDPOINT / "stdout.txt").read_text(),
      "nonendpoint raw successful stream has twelve-check terminal marker")
counts.update({
    "separate_nonendpoint_checker_lineages": 1,
    "separate_nonendpoint_successful_execution_of_repaired_revision": 1,
    "separate_nonendpoint_retained_failed_executions": len(nonendpoint_attempts),
    "separate_nonendpoint_exact_symbolic_chain_identities": 12,
    "nonendpoint_namespace_repair_additional_independent_verifiers": 0,
})
warnings.append("The nonendpoint original symbolic source and both protected-name failure revisions survive. The passing executable is a mechanically repaired revision of the same checker, and its retained record declares no additional independent verifier. Twelve chain identities do not independently certify global geometric coverage.")

# Endpoint attempt 4 and attempt 5 are two successful executions of one
# checker lineage. Diagnostics remain separate and are never verifier passes.
endpoint_record = read(ENDPOINT / "execution-record.json")
endpoint_attempts = []
for i, record_name in enumerate(endpoint_record["attempt_records"], start=1):
    row = read(ENDPOINT / record_name)
    snapshot_name = row.get("source_snapshot", "attempt-01-protected-check.m2")
    matches(ENDPOINT / snapshot_name, row["source_sha256"],
            "endpoint contemporaneous attempt source bytes retained")
    if "stdout" in row:
        bind(ENDPOINT / row["stdout"])
        bind(ENDPOINT / row["stderr"])
    else:
        check("not reconstructed raw stdout/stderr" in row["output_kind"],
              "endpoint first namespace failure stream limitation explicitly retained")
    endpoint_attempts.append(row)
check([r["exit_code"] for r in endpoint_attempts] == [1, 1, 1, 0, 0],
      "endpoint five main attempts retain three failures and two passes")
check(endpoint_record["passing_M2_executions"] == 2
      and endpoint_record["failed_M2_executions"] == 3
      and endpoint_record["distinct_mathematical_source_paths"] == 1,
      "endpoint declared main-attempt accounting agrees with rows")
endpoint_final = endpoint_record["final"]
check(endpoint_final == endpoint_attempts[-1], "endpoint final fields equal last exact attempt row")
endpoint_diagnostic = read(ENDPOINT / endpoint_record["diagnostic_record"])
check(endpoint_diagnostic["diagnostic_only"] is True
      and endpoint_diagnostic["not_in_main_attempt_rows"] is True
      and [r["exit_code"] for r in endpoint_diagnostic["records"]] == [0, 1],
      "endpoint startup and failed substitution diagnostics stay outside verifier counts")
for row in endpoint_diagnostic["records"]:
    if "source_snapshot" in row:
        matches(ENDPOINT / row["source_snapshot"], row["source_sha256"],
                "endpoint failed diagnostic source bytes retained")
endpoint_manifest = read(ENDPOINT_REPLAY / "execution-manifest.json")
matches(ROOT / endpoint_manifest["source"], endpoint_manifest["source_sha256"],
        "endpoint final live source bytes")
matches(ROOT / endpoint_manifest["snapshot"], endpoint_manifest["snapshot_sha256"],
        "endpoint root replay exact snapshot bytes")
check(endpoint_final["source_sha256"] == endpoint_manifest["source_sha256"]
      == endpoint_manifest["snapshot_sha256"],
      "endpoint root replay uses the final exact sixteen-check revision")
check(endpoint_manifest["exit_code"] == 0 and endpoint_manifest["status"] == "PASS"
      and endpoint_final["exact_identity_count"] == endpoint_manifest["expected_exact_identities"] == 16,
      "endpoint root replay declared sixteen exact identities and zero exit")
check(endpoint_manifest["command"] == ["/opt/homebrew/bin/M2", "--script", str(ROOT / endpoint_manifest["snapshot"])]
      and endpoint_manifest["cwd"] == str(ENDPOINT_REPLAY / "snapshot"),
      "endpoint root replay command uses exact source in isolated cwd")
bind(ENDPOINT_REPLAY / "run_replay.py")
for stream in ("stdout", "stderr"):
    matches(ENDPOINT_REPLAY / f"{stream}.txt", endpoint_manifest[f"{stream}_sha256"],
            f"endpoint root captured raw {stream} bytes")
    check((ENDPOINT_REPLAY / f"{stream}.txt").read_bytes()
          == (ENDPOINT / endpoint_final[stream]).read_bytes(),
          f"endpoint root raw {stream} equals final agent raw stream")
check("PASS" in (ENDPOINT_REPLAY / "stdout.txt").read_text()
      and "16" in (ENDPOINT_REPLAY / "stdout.txt").read_text(),
      "endpoint root captured terminal sixteen-check PASS marker")
counts.update({
    "separate_endpoint_checker_lineages": 1,
    "separate_endpoint_successful_m2_executions_including_root_replay": 3,
    "separate_endpoint_failed_main_m2_executions": 3,
    "separate_endpoint_failed_substitution_diagnostic_executions": 1,
    "separate_endpoint_startup_warning_diagnostic_executions": 1,
    "separate_endpoint_exact_identities_in_final_revision": 16,
    "endpoint_root_replay_additional_distinct_sources": 0,
})
warnings.append("Endpoint main attempt 4 passed under a mechanically renamed terminal label, and attempt 5 restores that label. The root replays attempt 5 only. The namespace failure has contemporaneous source and tool metadata but no separately retained raw streams. Two diagnostics are retained separately, including an exit-zero startup-warning probe which is not a passing verifier execution.")

# The double-horizontal source has four failed attempts, including an actual
# reversed Cartan-index assertion. Do not flatten that mathematical failure
# into parser/setup-only history.
double_record = read(DOUBLE_HORIZONTAL / "execution-record.json")
matches(ROOT / double_record["source_path"], double_record["source_sha256"],
        "double-horizontal exact passing live source bytes")
matches(DOUBLE_HORIZONTAL / "source.m2", double_record["source_sha256"],
        "double-horizontal execution used exact source snapshot")
check(double_record["exit_code"] == 0 and double_record["status"] == "PASS"
      and double_record["assertion_count"] == 14,
      "double-horizontal fourteen-check successful execution retained")
bind(DOUBLE_HORIZONTAL / "run_verifier.py")
for stream in ("stdout.txt", "stderr.txt"):
    bind(DOUBLE_HORIZONTAL / stream)
double_failures = []
for directory in sorted(DOUBLE_HORIZONTAL.glob("failed-*")):
    row = read(directory / "execution-record.json")
    matches(directory / "source.m2", row["source_sha256"],
            "double-horizontal failed revision exact source bytes")
    bind(directory / "stdout.txt")
    bind(directory / "stderr.txt")
    check(row["status"] == "FAIL" and row["exit_code"] == 1,
          "double-horizontal failed execution status remains failed", relative(directory))
    double_failures.append(row)
check(len(double_failures) == 4, "all four double-horizontal failed execution histories survive")
check("FAIL: A5 internal-node contact budget" in (DOUBLE_HORIZONTAL / "failed-04-reversed-endpoint-index/stderr.txt").read_text(),
      "reversed endpoint-index failure preserved as an actual assertion failure")
check("PASS" in (DOUBLE_HORIZONTAL / "stdout.txt").read_text()
      and "14" in (DOUBLE_HORIZONTAL / "stdout.txt").read_text(),
      "double-horizontal raw fourteen-check PASS marker retained")
counts.update({
    "separate_double_horizontal_checker_lineages": 1,
    "separate_double_horizontal_successful_m2_executions": 1,
    "separate_double_horizontal_retained_failed_m2_executions": 4,
    "separate_double_horizontal_exact_checks": 14,
})
warnings.append("Double-horizontal failed execution 4 was a real reversed endpoint-index assertion, repaired in the accepted final source. Its source and raw streams survive. The passing source has one retained execution; this integrity checker does not manufacture a root mathematical replay.")

# The newly arriving (5,8) enumeration is only necessary numerical data, not
# a classification of structures or a mate exclusion. Bind its exact record
# without executing the Python source or adding it to older M2 scopes.
filtration_record = read(FILTRATION / "execution-record.json")
matches(ROOT / filtration_record["source_path"], filtration_record["source_sha256"],
        "multiplicity-ten necessary-data source exact bytes")
matches(ROOT / filtration_record["stdout_path"], filtration_record["stdout_sha256"],
        "multiplicity-ten captured stdout exact bytes")
matches(ROOT / filtration_record["stderr_path"], filtration_record["stderr_sha256"],
        "multiplicity-ten captured stderr exact bytes")
filtration_output = read(ROOT / filtration_record["stdout_path"])
check(filtration_record["status"] == filtration_output["status"] == "PASS"
      and filtration_record["exit_code"] == 0
      and filtration_record["command"][1] == str(ROOT / filtration_record["source_path"])
      and filtration_record["cwd"] == str(ROOT),
      "multiplicity-ten one captured passing Python execution has exact source command")
check(filtration_record["bounded_triples_checked_for_equivalence"]
      == filtration_output["bounded_triples_checked_for_equivalence"] == 23001,
      "multiplicity-ten observed bounded comparison count agrees in record and stream")
filtration_counts = [r["count_after_P010"] for r in filtration_output["results"]]
check(filtration_counts == filtration_record["necessary_degree_counts_after_P010"] == [198, 97, 13]
      and sum(filtration_counts) == filtration_output["total_necessary_degree_triples_after_P010"] == 308,
      "multiplicity-ten necessary numerical counts agree without an existence or exclusion claim")
check("not a global embedded-structure classification or STCI exclusion" in filtration_record["scope"],
      "multiplicity-ten necessary-data scope boundary explicitly preserved")
counts.update({
    "separate_multiplicity_ten_numerical_source_paths": 1,
    "separate_multiplicity_ten_successful_python_executions": 1,
    "separate_multiplicity_ten_bounded_degree_comparisons": 23001,
    "separate_multiplicity_ten_necessary_counts": filtration_counts,
    "separate_multiplicity_ten_necessary_degree_triples": 308,
    "multiplicity_ten_record_check_additional_mathematical_executions": 0,
})
warnings.append("The multiplicity-ten Python history is separately scoped numerical evidence: 23,001 bounded degree comparisons and 308 necessary triples, not classified embedded structures, global divisor placements, higher-jet exhaustion or a (5,8) exclusion. This checker does not execute it.")
for path, digest in ROOT_READY_QUINTIC_INPUTS.items():
    matches(ROOT / path, digest, "quintic input matches exact frozen hash supplied by root's READY")

blowup_audit = bind(ROOT / "research/notes/2026-10-10-session-genus-two-blowup-lift-normality-independent-audit.md")
blowup_digests = re.findall(r"`([0-9a-f]{64})`", blowup_audit.read_text())
check(len(blowup_digests) >= 2, "normal-T audit has exact owner and conductor input digests")
if len(blowup_digests) >= 2:
    matches(ROOT / "research/notes/2026-10-10-session-genus-two-blowup-lift-normality-proposed-audit.md",
            blowup_digests[0], "normal-T owner proof matches independently audited bytes")
    matches(ROOT / "research/notes/2026-10-10-session-genus-two-entire-conductor-independent-audit.md",
            blowup_digests[1], "normal-T conductor input matches independently audited bytes")
no_b_audit = bind(ROOT / "research/notes/2026-10-10-session-genus-two-no-zero-horizontal-independent-audit.md")
no_b_input_digest = "f6701f0cee494573469d15e6bc18d76b787e8963701a4795c4ba2905f00f2522"
check(no_b_input_digest in no_b_audit.read_text(),
      "no-zero-horizontal audit retains its explicit owner input digest")
matches(ROOT / "research/notes/2026-10-10-session-genus-two-lambda1-horizontal-line-budget.md",
        no_b_input_digest, "no-zero-horizontal owner source matches independently audited bytes")
ribbon_microaudit = bind(ROOT / "research/notes/2026-10-10-session-bisection-ribbon-conormal-microaudit.md")
ribbon_microaudit_digests = re.findall(r"`([0-9a-f]{64})`", ribbon_microaudit.read_text())
check(len(ribbon_microaudit_digests) == 1,
      "ribbon microaudit retains exactly one declared full-bisection input digest")
if len(ribbon_microaudit_digests) == 1:
    matches(ROOT / "research/notes/2026-10-10-session-genus-two-bisection-full-independent-audit.md",
            ribbon_microaudit_digests[0], "full bisection proof matches ribbon microaudit's exact input bytes")

# File routes and local links. This audits target existence, not external sources
# and not whether a referenced theorem has correct hypotheses.
acceptance = ROOT / args.acceptance
all_routing = (list(CANONICAL) + PROOF_ROUTING + STATUS_TRACKED + new_note_paths
               + [relative(HERE / "README.md"),
                  relative(PREPARED / "resume-scope-observation-2026-10-10.md")])
if acceptance.exists():
    all_routing.append(args.acceptance)
elif final_routing:
    check(False, "final October11 acceptance exists", args.acceptance)
else:
    warnings.append("Root acceptance/routing is still pending; this preliminary result cannot be used as a final seal.")

checked_links = 0
broken_links = []
local_link_edges = {}
nonlink_notation_exclusions = []
def mask_markdown_code(text):
    # Preserve character positions/newlines for accurate source-line reporting.
    mask = lambda match: re.sub(r"[^\n]", " ", match.group(0))
    text = re.sub(r"(?ms)^```[^\n]*\n.*?^```[^\n]*$", mask, text)
    return re.sub(r"`[^`\n]*`", mask, text)
all_routing = list(dict.fromkeys(all_routing))
routing_index = 0
while routing_index < len(all_routing):
    p = all_routing[routing_index]
    routing_index += 1
    path = bind(ROOT / p)
    if not path.is_file():
        continue
    text = path.read_text()
    link_text = mask_markdown_code(text)
    for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", link_text):
        target_url = match.group(1).strip().split(" ", 1)[0].strip("<>")
        if (p == "research/notes/2026-10-08-session-scroll-nongorenstein-independent-audit.md"
                and match.group(0) == "[L_i:K](a-k)"):
            nonlink_notation_exclusions.append({
                "file": p, "literal_expression": match.group(0),
                "line": text[:match.start()].count("\n") + 1,
                "reason": "Field-extension degree multiplied by a-k in mathematical prose; not a file citation",
            })
            continue
        parsed = urlparse(target_url)
        if parsed.scheme or target_url.startswith("#"):
            continue
        decoded = unquote(parsed.path)
        candidate = Path(decoded) if decoded.startswith("/") else path.parent / decoded
        local_link_edges.setdefault(p, []).append(str(candidate.resolve()))
        checked_links += 1
        if not candidate.exists():
            detail = {"file": p, "target": target_url, "line": text[:match.start()].count("\n") + 1}
            broken_links.append(detail)
        check(candidate.exists(), "local Markdown link target exists",
              {"file": p, "target": target_url})
        if candidate.is_file() and candidate.resolve().is_relative_to(ROOT):
            bind(candidate.resolve())
            if (candidate.suffix == ".md"
                    and candidate.resolve().is_relative_to(ROOT / "research/notes")):
                note_route = relative(candidate.resolve())
                if note_route not in all_routing:
                    all_routing.append(note_route)

if final_routing and acceptance.exists():
    for p in CANONICAL:
        check(str(acceptance.resolve()) in local_link_edges.get(p, []),
              "canonical file has a Markdown link to exact October11 acceptance", p)
    atext = acceptance.read_text()
    for label, filename in (
        (r"owner SHA-256", "2026-10-10-session-genus-two-endpoint-full-quartic-reduction.md"),
        (r"binding independent-audit SHA-256", "2026-10-10-session-genus-two-endpoint-full-independent-audit.md"),
    ):
        declared = re.search(label + r"\s*`([0-9a-f]{64})`", atext)
        check(declared is not None, "final acceptance declares endpoint proof/audit input digest", filename)
        if declared is not None:
            matches(ROOT / "research/notes" / filename, declared.group(1),
                    "final acceptance endpoint digest matches its exact accepted input")
    acceptance_reachable = set()
    frontier = [str(acceptance.resolve())]
    resolved_routing = {str((ROOT / p).resolve()): p for p in dict.fromkeys(all_routing)}
    while frontier:
        current = frontier.pop()
        if current in acceptance_reachable:
            continue
        acceptance_reachable.add(current)
        routed_path = resolved_routing.get(current)
        if routed_path:
            frontier.extend(local_link_edges.get(routed_path, []))
    for required in (
        "2026-10-10-session-genus-one-interface-independent-audit.md",
        "2026-10-10-session-ribbon-repeated-partitions-independent-audit.md",
        "2026-10-10-session-genus-two-entire-conductor-independent-audit.md",
        "2026-10-10-session-genus-two-marking-and-section-pause-audit.md",
        "2026-10-10-session-genus-two-blowup-lift-normality-independent-audit.md",
        "2026-10-10-session-genus-two-bisection-full-independent-audit.md",
        "2026-10-10-session-genus-two-bisection-second-pencil-independent-audit.md",
        "2026-10-10-session-weighted-ribbon-conormal-independent-audit.md",
        "2026-10-10-session-bisection-ribbon-conormal-microaudit.md",
        "2026-10-10-session-quartic-normal-bundle-independent-audit.md",
        "2026-10-10-session-genus-two-nonendpoint-trisecant-continuation-independent-audit.md",
        "2026-10-10-session-relative-morse-conductor-branches-independent-audit.md",
        "2026-10-10-session-genus-two-endpoint-full-independent-audit.md",
        "2026-10-10-session-genus-two-endpoint-full-quartic-reduction.md",
        "2026-10-10-session-endpoint-local-ade-correction-audit.md",
        "2026-10-10-session-genus-two-endpoint-double-horizontal-independent-audit.md",
        "2026-10-11-session-all-quartic-dependency-assembly-independent-audit.md",
        "2026-10-11-session-quintic-structural-frontier.md",
        "2026-10-11-session-quintic-conormal-and-delpezzo-audit.md",
        "2026-10-11-session-multiplicity-ten-filtration-audit.md",
    ):
        check(str((ROOT / "research/notes" / required).resolve()) in acceptance_reachable,
              "acceptance links directly or through retained proof routing to critical independent audit",
              required)
    state = (ROOT / "research/AUDITED_STATE_2026-10-07.md").read_text()
    check("unresolved" in state and "characteristic-zero" in state,
          "canonical state retains unrestricted open status")

status_headers = {}
for p in sorted(set(STATUS_TRACKED + new_note_paths)):
    if (ROOT / p).exists():
        status_headers[p] = "\n".join((ROOT / p).read_text().splitlines()[:12])

head_process = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True)
head = head_process.stdout.strip()
check(head_process.returncode == 0, "read-only live HEAD observation")
check(head == head_before, "live HEAD unchanged during record check",
      {"before": head_before, "after": head})
if final_routing and acceptance.exists():
    check(head in acceptance.read_text(), "acceptance includes currently observed HEAD", head)
    check(head in (ROOT / "research/SUCCESSOR_HANDOFF_2026-10-07.md").read_text(),
          "successor handoff includes currently observed HEAD", head)
diff = subprocess.run(["git", "diff", "--check"], cwd=ROOT, capture_output=True, text=True)
check(diff.returncode == 0, "git diff --check", diff.stdout + diff.stderr)
canonical_after = {p: sha(ROOT / p) for p in freeze_paths}
check(canonical_after == canonical_before, "canonical files unchanged during this record check")
new_note_paths_after = [relative(p) for p in sorted((ROOT / "research/notes").glob("2026-10-1[01]*.md"))]
check(new_note_paths_after == new_note_paths,
      "October10 and October11 note inventory unchanged during record check")
for p, digest in tuple(bound.items()):
    candidate = ROOT / p
    check(candidate.is_file() and sha(candidate) == digest,
          "every bound file retains its first-observed bytes through check end", p)

result = {
    "status": "PASS" if not issues else "FAIL",
    "mode": "FINAL_SEAL" if args.seal_once else "PREFLIGHT" if args.preflight else "PRELIMINARY",
    "started_utc": started, "completed_utc": datetime.now(timezone.utc).isoformat(),
    "scope": "Record provenance, explicitly scoped execution accounting, local target routing and canonical freeze observation only",
    "does_not_certify": "Mathematical proofs, novelty, all-quartic mate exclusion, higher carrier degrees, positive characteristic or universal STCI resolution",
    "mathematical_verifiers_rerun": False, "head_observed": head,
    "head_before_observed": head_before,
    "checker_sha256": sha(Path(__file__)), "counts": counts,
    "check_count": len(checks), "checked_local_links": checked_links,
    "bound_files_sha256": bound, "canonical_before_sha256": canonical_before,
    "canonical_after_sha256": canonical_after,
    "historically_bound_files_changed_since_oct9_seal": changed_since_old_seal,
    "historically_bound_files_missing_since_oct9_seal": missing_since_old_seal,
    "broken_local_links": broken_links, "issues": issues, "warnings": warnings,
    "nonlink_notation_exclusions": nonlink_notation_exclusions,
    "scoped_local_link_edges": local_link_edges,
    "transitively_scanned_note_routes": all_routing,
    "separately_scoped_new_note_headers": status_headers,
    "october10_and_october11_note_inventory": new_note_paths,
    "read_only_resume_runtime_observation": relative(PREPARED / "resume-runtime-observation.json"),
    "checks": checks,
    "limits": [
        "The historical 97/110 index and 2006/313 seal remain frozen. New records do not retroactively enlarge their scope.",
        "The genus-one execution fields cover only the two independent M2 source histories and their root replays. Line-position and normal-bundle sources have separate fields. No complete all-repository October10 aggregate is asserted; runtime probes and other owner computations are outside these explicitly scoped fields.",
        "Copied sources do not create new verifiers. Replaying 42 and 29 conditions is two more executions, not another 71 independent conditions.",
        "Historical source-byte and log limitations in the older index remain unchanged.",
        "A local link target existing does not verify the mathematical proposition or the external primary source it cites.",
        "The bounded Markdown scan supports ordinary inline destinations outside fenced and inline code. It does not parse reference-style definitions, balanced destination parentheses or escaped delimiters. One exact older plain-prose degree-times-expression [L_i:K](a-k) is explicitly observed as mathematical notation, not silently treated as a missing file or repaired in frozen proof text.",
        "Note status headers are preserved as observations, including historical pending labels; only root's explicit acceptance promotes a mathematical scope.",
        "Every bound file is rehashed at completion. This detects observed mutation during the run, but does not assert that files cannot change after the seal.",
    ],
}
with target.open("x" if args.seal_once else "w") as stream:
    stream.write(json.dumps(result, indent=2) + "\n")
print(f"{result['status']}: {result['mode']}; {len(checks)} record checks, {checked_links} scoped local links; no mathematical verifier rerun")
if issues:
    print(json.dumps(issues, indent=2))
raise SystemExit(0 if not issues else 1)
