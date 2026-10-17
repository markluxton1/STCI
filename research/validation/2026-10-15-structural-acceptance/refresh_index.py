#!/usr/bin/env python3
"""Refresh only the small-note integrity index; never run mathematical checks.

The manifest below records written review dispositions, not inferred mathematics.
Run without --write to inspect a candidate. Root stabilization precedes --write.
Only explicitly indexed notes and the predecessor index are read for hashes.
Local-link QA does not recursively hash linked certificates or other witnesses.
"""

import argparse
import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
INDEX = HERE / "index.json"
NOTE_DIR = "research/notes/"
MAX_HASH_BYTES = 512 * 1024
FRESH_QQ_EXECUTION = "research/validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/execution-record.json"


def note(stem):
    return NOTE_DIR + stem + ".md"


# Accepted dispositions come from the named written independent audits.
# Entries with pending audits stay provisional until this manifest is updated.
MANIFEST = [
    ("2026-10-15-generalization-smooth-root-formal-nonexistence",
     "accepted at stated smooth-root formal geometric scope; actual-CI consequence subject to bridge hypotheses",
     ["2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit",
      "2026-10-15-generalization-smooth-root-characteristic-scope-addendum"]),
    ("2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit",
     "accepted full independent audit at stated scope", []),
    ("2026-10-15-generalization-smooth-root-characteristic-scope-addendum",
     "accepted characteristic-free formal geometry and finite embedded-Cartier tower; actual-CI consequence conditional on valid bridge", []),
    ("2026-10-15-generalization-nef-formal-branch-arbitrary-base",
     "accepted Sections 1-4 nef/arbitrary-base extension and Section 5 movement-one corollary at their stated characteristic-zero scopes",
     ["2026-10-15-generalization-nef-formal-branch-arbitrary-base-independent-audit",
      "2026-10-15-generalization-movement-one-formal-roots-independent-audit"]),
    ("2026-10-15-generalization-nef-formal-branch-arbitrary-base-independent-audit",
     "accepted targeted independent audit at stated characteristic-zero scope", []),
    ("2026-10-15-generalization-movement-one-formal-roots-independent-audit",
     "accepted targeted independent audit of Section 5 movement-one formal roots in its stated characteristic-zero scope", []),
    ("2026-10-15-generalization-quintic-h2-a4-unit-and-eleven-generators",
     "accepted remaining-mate Delta1 open and exact eleven-generator localized ideal-sheaf reduction",
     ["2026-10-15-generalization-quintic-h2-eleven-generator-unit-independent-audit"]),
    ("2026-10-15-generalization-quintic-h2-eleven-generator-unit-independent-audit",
     "accepted independent audit of remaining-mate unit and exact coefficient binding", []),
    ("2026-10-15-generalization-quintic-h2-automatic-open-and-ODE",
     "accepted actual localized qhigh unit ideal and equivalent eight-equation shared ODE incidence; no emptiness claim",
     ["2026-10-15-generalization-quintic-h2-automatic-open-ODE-independent-audit"]),
    ("2026-10-15-generalization-quintic-h2-automatic-open-ODE-independent-audit",
     "accepted independent audit of automatic open, unique ODE witnesses and ideal accelerators", []),
    ("2026-10-15-generalization-quintic-h2-unified-spectral-accelerator",
     "accepted localized shared-ODE spectral polynomial ideal membership, including nonreduced bases; no actual-parameter emptiness or descent",
     ["2026-10-15-generalization-quintic-h2-eta-spectral-independent-audit"]),
    ("2026-10-15-generalization-quintic-h2-eta-spectral-independent-audit",
     "accepted independent audit of exact scheme-theoretic spectral accelerator membership", []),
    ("2026-10-15-generalization-effective-rational-phase-bound",
     "accepted explicit-W effective rational-phase bound and Section 9 in-principle composite algorithm for the explicit fixed-three-model rational input; algorithm not run and no numerical actual-family bound",
     ["2026-10-15-generalization-effective-rational-phase-bound-independent-review",
      "2026-10-16-generalization-raw-projection-decision-independent-audit"]),
    ("2026-10-15-generalization-effective-rational-phase-bound-independent-review",
     "accepted independent review of explicit rational W scope and Section 8 addendum for Section 9 fixed-three-model meta-effectivity", []),
    ("2026-10-16-generalization-raw-projection-decision-independent-audit",
     "accepted new-scope independent audit of Section 9 terminating decision algorithm for explicit rational input of the three fixed projection families; no executed family decision or numerical bound", []),
    ("2026-10-15-generalization-inseparable-root-blowup-bridge",
     "accepted arbitrary-characteristic actual-CI bridge under all literal first-relation, joint-leading-symbol, full-initial-CI, smooth-actual-root and gap hypotheses",
     ["2026-10-15-generalization-inseparable-root-blowup-bridge-independent-audit",
      "2026-10-15-generalization-inseparable-root-blowup-local-algebra-review"]),
    ("2026-10-15-generalization-inseparable-root-blowup-bridge-independent-audit",
     "accepted full independent audit of arbitrary-characteristic actual-CI bridge under all literal hypotheses", []),
    ("2026-10-15-generalization-inseparable-root-blowup-local-algebra-review",
     "accepted focused independent review of generic standard-basis, actual divided-ideal and root-prime length arguments in Sections 2-3", []),
    ("2026-10-15-generalization-quadratic-root-global-second-dual-compression",
     "accepted global twenty-five-test dual compression, universal model algorithm and homogeneous smoothness criterion on the full stated basepoint-free locus; no zero-locus exhaustion",
     ["2026-10-15-generalization-quadratic-root-global-second-dual-compression-independent-audit"]),
    ("2026-10-15-generalization-quadratic-root-global-second-dual-compression-independent-audit",
     "accepted independent audit including final companion and universal model algorithm comparison", []),
    ("2026-10-15-generalization-intrinsic-finite-root-family",
     "accepted stated relative finite-family generalization, bounded Hilbert-family construction, nonsplit intersection identities and conditional finite empty-stage consequence",
     ["2026-10-15-generalization-intrinsic-finite-root-family-independent-audit"]),
    ("2026-10-15-generalization-intrinsic-finite-root-family-independent-audit",
     "accepted independent audit of new relative hypotheses and nonsplit numerical inputs; accepted lifting/algebraization theorems are premises", []),
    ("2026-10-15-generalization-quintic-h2-global-monic-ODE-incidence",
     "accepted global monic whole-h2 necessary incidence on delta*E*Delta1 nonzero, original coefficient assembly and ODE/spectral transfer; Delta and K not inverted; no emptiness, projection or mate-existence claim",
     ["2026-10-16-generalization-quintic-h2-global-monic-ODE-independent-audit"]),
    ("2026-10-16-generalization-quintic-h2-global-monic-ODE-independent-audit",
     "accepted independent scope audit of global monic cover, seventeen-equation nine-variable assembly and transferred ODE/spectral algebra", []),
    ("2026-10-16-generalization-quintic-h2-global-QQ-prospect-terminal-record",
     "bounded computation process record only; M2 memory-threshold interruption and closed supervisor, no mathematical result", []),
    ("2026-10-16-generalization-quintic-h2-global-QQ-guard-independent-review",
     "accepted source/runtime-control review with fresh preflight and read-only terminal addendum; no mathematical prospect result", []),
    ("2026-10-15-generalization-quintic-h2-horner-input",
     "exact format validation only; no incidence elimination or exclusion", []),
    ("2026-10-15-session-structural-results-acceptance",
     "integration and acceptance narrative; not an additional mathematical proof", []),
    ("2026-10-16-session-structural-continuation",
     "continuation and successor narrative; not an additional mathematical proof", []),
]

ADDITIONAL_LINK_SOURCES = [
    "research/AUDITED_STATE_2026-10-14.md",
    "research/SUCCESSOR_HANDOFF_2026-10-14.md",
    "research/RESEARCH_RECORD.md",
    "README.md",
]

PENDING = [
    "Actual phase images and their surviving torsion cosets",
    "Remaining quintic incidence, other carrier strata, and global STCI obligations",
]

SCOPE_BINDINGS = [
    {"path": note("2026-10-15-generalization-nef-formal-branch-arbitrary-base"),
     "scope": "Sections 1-4, stated characteristic-zero nef/arbitrary-base extension",
     "status": "accepted",
     "authority": note("2026-10-15-generalization-nef-formal-branch-arbitrary-base-independent-audit")},
    {"path": note("2026-10-15-generalization-nef-formal-branch-arbitrary-base"),
     "scope": "New Section 5 movement-one corollary",
     "status": "accepted at stated characteristic-zero scope",
     "authority": note("2026-10-15-generalization-movement-one-formal-roots-independent-audit")},
    {"path": note("2026-10-15-generalization-effective-rational-phase-bound"),
     "scope": "Effective bound given explicit rational constructible phase image W",
     "status": "accepted",
     "authority": note("2026-10-15-generalization-effective-rational-phase-bound-independent-review")},
    {"path": note("2026-10-15-generalization-effective-rational-phase-bound"),
     "scope": "Section 9 in-principle terminating composite algorithm from the explicit fixed-three-model rational input; never run",
     "status": "accepted by Section 8 review addendum",
     "authority": note("2026-10-15-generalization-effective-rational-phase-bound-independent-review")},
]


def small_digest(relative):
    path = REPO / relative
    size = path.stat().st_size
    if size > MAX_HASH_BYTES:
        raise ValueError(f"Refusing large-file hash: {relative} ({size} bytes)")
    payload = path.read_bytes()
    return hashlib.sha256(payload).hexdigest(), size


def execution_snapshot(relative):
    """Bind a small execution record without reading or hashing its inputs."""
    digest, size = small_digest(relative)
    source = json.loads((REPO / relative).read_text())
    fields = ("status", "started_utc", "finished_utc", "completed_utc", "exit_code",
              "actual_exit_code", "stop_reason", "elapsed_wall_seconds", "cpu_seconds",
              "peak_resident_bytes", "peak_footprint_bytes", "rss_stop_bytes",
              "rss_poll_seconds", "rss_guard_kind", "cleanup", "scope",
              "timeout_seconds", "stdout_sha256", "stderr_sha256", "actual_M2_started",
              "m2_started", "review_status", "reviewer", "domain", "wall_seconds",
              "cpu_seconds_soft_hard", "runner_sha256", "driver_sha256", "source_sha256",
              "prior_generic_runner_checkpoint", "prior_generic_runner_sha256",
              "prior_generic_runner_snapshot")
    return {"path": relative, "sha256": digest, "bytes": size,
            **{key: source[key] for key in fields if key in source},
            "integrity_scope": "execution metadata only; input/output witnesses not rehashed; not mathematical verification"}


def outside_code(source):
    """Keep line numbers while removing fenced, indented and inline code."""
    lines, fence = [], None
    for line in source.splitlines(keepends=True):
        match = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence):
                fence = None
            lines.append("\n" if line.endswith("\n") else "")
            continue
        if match:
            fence = match[1]
            lines.append("\n" if line.endswith("\n") else "")
            continue
        if line.startswith("    ") or line.startswith("\t"):
            lines.append("\n" if line.endswith("\n") else "")
            continue
        lines.append(line)
    text = "".join(lines)
    # A code span is delimited by equal backtick runs, including across lines.
    text = re.sub(r"(`+)(?!`)([\s\S]*?)(?<!`)\1(?!`)",
                  lambda m: re.sub(r"[^\n]", " ", m[0]), text)
    # Explicit mathematical spans are not Markdown links.
    for pattern in (r"\$\$[\s\S]*?\$\$", r"(?<!\\)\$(?:\\.|[^$\n])*?\$",
                    r"\\\[[\s\S]*?\\\]", r"\\\([\s\S]*?\\\)"):
        text = re.sub(pattern, lambda m: re.sub(r"[^\n]", " ", m[0]), text)
    return text


def markdown_targets(source):
    text = outside_code(source)
    definitions = {}
    for match in re.finditer(r"(?m)^ {0,3}\[([^\]\n]+)\]:\s*(<[^>\n]+>|\S+)", text):
        definitions[" ".join(match[1].split()).casefold()] = match[2].strip("<>")
    # Start at a genuine bracket, rather than a matrix or escaped math delimiter.
    consumed_to = 0
    for match in re.finditer(r"(?<![!\\])\[(?:\\.|[^\]\\])*\]", text):
        if match.start() < consumed_to:
            continue
        end, target = match.end(), None
        line_start = text.rfind("\n", 0, match.start()) + 1
        if (text[end:end + 1] == ":" and
                re.fullmatch(r" {0,3}", text[line_start:match.start()])):
            continue  # A reference definition is not a link occurrence.
        if end < len(text) and text[end] == "(":
            pos = end + 1
            while pos < len(text) and text[pos].isspace():
                pos += 1
            if pos < len(text) and text[pos] == "<":
                close = text.find(">", pos + 1)
                if close != -1:
                    target = text[pos + 1:close]
            else:
                start, depth = pos, 0
                while pos < len(text):
                    char = text[pos]
                    if char == "\\" and pos + 1 < len(text):
                        pos += 2
                        continue
                    if char == "(":
                        depth += 1
                    elif char == ")":
                        if depth == 0:
                            break
                        depth -= 1
                    if char.isspace() and depth == 0:
                        break
                    pos += 1
                target = text[start:pos]
        elif end < len(text) and text[end] == "[":
            close = text.find("]", end + 1)
            if close != -1:
                label = text[end + 1:close] or match[0][1:-1]
                target = definitions.get(" ".join(label.split()).casefold())
                consumed_to = close + 1
        else:
            target = definitions.get(" ".join(match[0][1:-1].split()).casefold())
        if target:
            yield text.count("\n", 0, match.start()) + 1, target


def link_qa(records):
    checked, broken, per_source = 0, [], []
    for record in records:
        path = REPO / record["path"]
        if path.suffix != ".md":
            continue
        source_checked = 0
        for line, target in markdown_targets(path.read_text()):
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            checked += 1
            source_checked += 1
            destination = Path(unquote(parts.path))
            if not destination.is_absolute():
                destination = path.parent / destination
            if not destination.exists():
                broken.append({"source": record["path"], "line": line, "target": target})
        per_source.append({"path": record["path"], "local_links_checked": source_checked})
    return checked, broken, per_source


def refresh():
    old_bytes = INDEX.read_bytes()
    index = json.loads(old_bytes)
    before = copy.deepcopy(index)
    now = datetime.now(timezone.utc).isoformat()
    records = index["records"]
    by_path = {r["path"]: r for r in records}
    if len(by_path) != len(records):
        raise ValueError("Existing index has duplicate paths")
    missing = []
    for stem, status, audits in MANIFEST:
        relative = note(stem)
        if not (REPO / relative).exists():
            missing.append({"path": relative, "intended_status": status})
            continue
        record = by_path.get(relative)
        if record is None:
            record = {"key": stem, "status": status, "path": relative}
            record["status_history"] = [{"status": status, "recorded_utc": now,
                                         "basis": "explicit written-review manifest"}]
            records.append(record)
            by_path[relative] = record
        elif record["status"] != status:
            history = record.setdefault("status_history", [{
                "status": record["status"],
                "recorded_utc": index.get("refreshed_utc", index["created_utc"]),
                "basis": "retained pre-refresh index disposition"}])
            history.append({"status": status, "recorded_utc": now,
                            "basis": "explicit written-review manifest"})
            record["status"] = status
        if audits:
            record["status_authorities"] = [note(audit) for audit in audits]
        record["classification_basis"] = "written note/review disposition only; no mathematical verifier run"

    # Preserve all prior records and any prior status histories.
    assert all(any(r["key"] == old["key"] and r["path"] == old["path"]
                   for r in records) for old in before["records"])
    for record in records:
        digest, size = small_digest(record["path"])
        if "sha256" in record and (record["sha256"], record.get("bytes")) != (digest, size):
            record.setdefault("digest_history", []).append({
                "sha256": record["sha256"], "bytes": record.get("bytes"),
                "recorded_utc": index.get("refreshed_utc", index["created_utc"])})
        record.update(sha256=digest, bytes=size)
    predecessor_hash, _ = small_digest(index["predecessor_index"])
    if predecessor_hash != index.get("predecessor_sha256"):
        index.setdefault("predecessor_digest_history", []).append({
            "sha256": index.get("predecessor_sha256"),
            "recorded_utc": index.get("refreshed_utc", index["created_utc"])})
    index["predecessor_sha256"] = predecessor_hash
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    if head != index.get("observed_head"):
        index.setdefault("observed_head_history", []).append({
            "head": index.get("observed_head"),
            "recorded_utc": index.get("refreshed_utc", index["created_utc"])})
    index["observed_head"] = head
    index["observed_head_title"] = subprocess.check_output(
        ["git", "log", "-1", "--format=%s"], cwd=REPO, text=True).strip()
    index["head_observation_scope"] = "read-only external checkpoint observation; this refresh creates no commit"
    index["refreshed_utc"] = now
    index["previous_index_sha256"] = hashlib.sha256(old_bytes).hexdigest()
    index["record_count"] = len(records)
    index["retained_pre_refresh_record_count"] = len(before["records"])
    index["pending_bindings"] = missing
    if index.get("pending") != PENDING:
        index.setdefault("pending_history", []).append({
            "recorded_utc": before.get("refreshed_utc", before["created_utc"]),
            "items": before.get("pending", [])})
    index["pending"] = PENDING
    index["scope_bindings"] = SCOPE_BINDINGS
    index["computations"]["quintic_attempt07_low_degree_ODE"] = {
        "execution_record": "research/validation/2026-10-15-quintic-h2-unified-incidence/attempt-07-low-degree-ode-name-repair/execution-record.json",
        "status": "terminal interrupted-timeout", "exit_code": -15,
        "finished_utc": "2026-10-15T19:16:10.802045+00:00",
        "result": "empty stdout/stderr; no incidence elimination result",
        "restart": "do not restart old attempts unchanged"}
    index["computations"]["quintic_attempt08_spectral_ODE"] = {
        "execution_record": "research/validation/2026-10-15-quintic-h2-unified-incidence/attempt-08-spectral-ode-prospect/execution-record.json",
        "status": "terminal interrupted-timeout", "exit_code": -15,
        "finished_utc": "2026-10-16T01:19:03.590742+00:00",
        "result": "empty stdout/stderr; no incidence elimination result",
        "restart": "do not restart old attempts unchanged"}
    process_paths = [
        index["computations"]["quintic_attempt07_low_degree_ODE"]["execution_record"],
        index["computations"]["quintic_attempt08_spectral_ODE"]["execution_record"],
        "research/validation/2026-10-15-quintic-h2-global-monic-ode/attempt-04-completion/execution-record.json",
        "research/validation/2026-10-15-quintic-h2-global-monic-ode/attempt-05-load-only/execution-record.json",
        FRESH_QQ_EXECUTION,
        "research/validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/standalone-preflight-record.json",
        "research/validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/preflight-record.json",
        "research/validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/prelaunch-source-review.json",
    ]
    index["process_records"] = [execution_snapshot(path) for path in process_paths
                                if (REPO / path).exists()]
    fresh_qq = next((record for record in index["process_records"]
                     if record["path"] == FRESH_QQ_EXECUTION), None)
    if fresh_qq:
        stage_path = str(Path(FRESH_QQ_EXECUTION).with_name("stage.txt"))
        stage = (REPO / stage_path).read_text().strip()
        stage_digest, stage_size = small_digest(stage_path)
        index["computations"]["quintic_global_monic_attempt06_QQ"] = {
            "execution_record": FRESH_QQ_EXECUTION,
            "lineage": "NEW whole-h2 global QQ prospect; distinct from old unified-incidence attempt06",
            **{field: fresh_qq[field] for field in
               ("status", "exit_code", "actual_exit_code", "started_utc", "finished_utc",
                "scope", "stop_reason", "elapsed_wall_seconds", "cpu_seconds",
                "peak_resident_bytes", "peak_footprint_bytes", "rss_stop_bytes",
                "rss_poll_seconds", "rss_guard_kind", "cleanup")
               if field in fresh_qq},
            "stage": stage,
            "stage_record": {"path": stage_path, "sha256": stage_digest, "bytes": stage_size},
            "result": "memory-threshold interruption before global saturation completed; no incidence result",
            "interpretation": "polled memory stop, not a 120-second wall timeout",
            "process_note": note("2026-10-16-generalization-quintic-h2-global-QQ-prospect-terminal-record"),
            "guard_review": note("2026-10-16-generalization-quintic-h2-global-QQ-guard-independent-review"),
            "supervisor": {"tool_handle": 82234, "closed": True, "exit_code": 0,
                           "scope": "successful handling of bounded interruption; not an M2 success code"},
            "restart": "do not restart old attempts unchanged"}
    link_sources = [{"path": path} for path in dict.fromkeys(
        [record["path"] for record in records] + ADDITIONAL_LINK_SOURCES)]
    checked, broken, per_source = link_qa(link_sources)
    index.setdefault("integrity_refresh_history", []).append({
        "recorded_utc": before.get("refreshed_utc", before["created_utc"]),
        "source_index_sha256": hashlib.sha256(old_bytes).hexdigest(),
        "record_count": len(before["records"]),
        "local_links_checked": before.get("local_links_checked"),
        "broken_local_links": before.get("broken_local_links", []),
        "link_check_scope": before.get("link_check_scope"),
        "scope": "retained prior document-integrity metadata; not mathematical verification"})
    index["local_links_checked"] = checked
    index["broken_local_links"] = broken
    index["link_check_sources"] = per_source
    index["link_check_source_count"] = len(per_source)
    index["link_check_source_scope"] = "All indexed small-note records plus explicitly listed audited frontier, successor handoff, research record and repository README; canonical files are link-checked only, not hashed"
    index["link_check_scope"] = "Markdown links outside fenced, indented and inline code; explicit math spans excluded; destination existence only"
    index["accepted_verifiers_replayed"] = False
    refresh_source = str(Path(__file__).resolve().relative_to(REPO))
    source_digest, source_size = small_digest(refresh_source)
    index["refresh_tool"] = {"path": refresh_source, "sha256": source_digest,
                             "bytes": source_size, "scope": "document metadata only"}
    index["hash_scope"] = "Explicit small note records, small execution records, refresh source and predecessor source index only; no large accepted certificate, process input or linked target hashed"
    return index


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write after root stabilization")
    args = parser.parse_args()
    index = refresh()
    if args.write:
        source = json.loads((REPO / FRESH_QQ_EXECUTION).read_text())
        exit_code = source.get("actual_exit_code", source.get("exit_code"))
        if exit_code is None or not source.get("finished_utc"):
            raise ValueError("Refusing final write before fresh whole-h2 QQ attempt06 has a terminal execution record")
        INDEX.write_text(json.dumps(index, indent=2) + "\n")
    print(json.dumps({"written": args.write, "records": index["record_count"],
                      "observed_head": index["observed_head"],
                      "local_links_checked": index["local_links_checked"],
                      "broken_local_links": index["broken_local_links"],
                      "pending_bindings": index["pending_bindings"],
                      "accepted_verifiers_replayed": False}, indent=2))


if __name__ == "__main__":
    main()
