# October 11 continuation record integrity seal

This directory extends the prepared October 10 record checker without editing
that draft or pretending it had previously been finally sealed. The exact
prepared checker snapshot and SHA-256 are retained in
[preparation-source.json](preparation-source.json) and
[prepared-oct10-checker.py](prepared-oct10-checker.py).

This checker executes **no mathematical verifier**. It checks retained source
bytes, explicit execution accounting, raw stream provenance, local link targets,
accepted proof routing and the stability of the observed canonical files and
Git HEAD. Mathematical status comes from the root's explicit acceptance and the
separate written mathematical audits. A record PASS does not prove the
all-quartic theorem or resolve unrestricted set-theoretic complete intersection.

The parent must first declare canonical edits ready. Before that declaration,
the auditor may run `--preliminary` or `--preflight`, writing replaceable
observations only. The final command is:

```sh
python3 research/validation/2026-10-11-continuation-seal/check_record.py --seal-once --acceptance research/notes/2026-10-11-session-all-quartic-results-acceptance.md
```

Final mode exclusively creates `result.json` and refuses to overwrite it. A
separate execution manifest records the observed command, exit status and exact
checker/result digests. Existing historical seals remain unchanged.

After the preflight passes and the parent declares READY, the auditor uses
[run_final_seal.py](run_final_seal.py) to invoke that exact final mode and
exclusively capture `stdout.txt`, `stderr.txt` and `execution-manifest.json`.
The wrapper records its own source digest and the checker digest before and
after execution; a changed checker cannot yield its PASS. This remains a
single record-only execution, with zero mathematical executions.

The historical **97 source paths / 110 explicitly indexed executions** and
**2,006 integrity checks / 313 scoped local links** are checked against their
frozen bytes. No new aggregate all-repository count is claimed. New histories
are scoped separately:

- Genus-one interfaces and repeated partitions: two successful source paths;
  four passing M2 executions including root's two replays, three failed M2
  executions and one import-failed Python execution. The independent scopes
  are 42 and 29 conditions. Copied sources add no verifier.
- Line positions: 17 structural identities, one passing execution and two
  recorded development failures. Failed superseded source bytes were not saved;
  that limitation remains explicit. These identities alone exclude no mate.
- Normal bundle: eight identities/rank checks; one original passing source,
  two successful executions including the isolated root replay, and one retained
  namespace failure whose stream provenance is combined tool output.
- Nonendpoint trisecant: twelve symbolic all-length chain identities, one
  successful execution of a protected-name repair and two failed executions.
  The repair is one original checker lineage, including one printed-label
  adjustment, and is not an additional independent verifier. The failed
  revisions and captured streams survive.
- Endpoint local ADE: sixteen identities in the final revision. Five main
  attempts comprise three failures and two passes; the isolated root replay
  adds a third successful execution. The aggregate execution record duplicates
  final attempt 5 and is not counted as another execution. The first failure
  has contemporaneous source and tool metadata, with no separate raw streams.
  One failed debug script and one exit-zero startup-warning probe are separately
  retained diagnostics, not passing verifier executions.
- Endpoint double-horizontal: fourteen checks, one passing execution and four
  retained failures. Failure 4 is a genuine inverse-Cartan assertion with the
  endpoint index reversed; its repair changes that mathematical assertion.
  Its source and raw streams remain evidence of the failed attempt. No root
  mathematical replay is invented.
- Multiplicity ten in degree `(5,8)`: one passing standard-library Python
  execution with exact source and raw-stream digests. Its 23,001 bounded
  degree comparisons leave 198/97/13 necessary degree triples, 308 total.
  This is separately scoped necessary numerical evidence; it does not classify
  embedded structures, full defect-divisor placements or higher jets, and it
  does not exclude `(5,8)`. The integrity checker does not rerun that source.

All October 10 and October 11 note headers are retained as observations.
Historical pending labels in preserved owner notes remain unchanged; the
latest acceptance identifies which scopes were promoted. Local Markdown
targets are checked for existence, and critical independent audits must be
transitively reachable from the final acceptance. This is not an external
primary-source or mathematical hypothesis audit.

The earlier prepared directory retains its provenance notes, runtime probes,
temporary arriving-draft link failure and precisely disclosed reconstruction
limitations. Its read-only runtime observations add zero mathematical
executions. Dates in that runtime record remain dates of observation, not a
claim about future capacity or dependency availability.

The [independent coverage review](validation-scope-review.md) records source,
stream, diagnostic and proof-routing distinctions before the final seal.
The checker follows linked Markdown notes transitively within
`research/notes`, so the accepted chain reaches earlier dated proofs rather
than treating the mere existence of a linked intermediate note as exhaustion.

The first extended transitive scan is retained in
[transitive-scan-first-failure/observation.json](transitive-scan-first-failure/observation.json).
It found an arriving multiplicity-ten draft's missing execution record,
three fenced-code applications misread by the previous regex, and the older
plain mathematical factor `[L_i:K](a-k)`. The repaired scan ignores code,
and explicitly records that exact factor as notation, without modifying
historical mathematical proof bytes. The failure snapshot is retained;
a repaired PASS does not erase it.
