# Independent coverage review for the October 11 record seal

Reviewer: `oct11_record_seal/seal_coverage_review`. Review date: 2026-10-11.
Scope: current file inventory, source and stream provenance, execution
accounting, and mathematical-audit routing only. No mathematical verifier
was executed and no canonical research note was edited. This review is
an observation during preparation, not the final record seal or a new
mathematical acceptance.

## Execution histories and distinct-source accounting

| Companion | Mathematical checkers | Observed main executions | Separate diagnostics | Formula/check count |
| --- | ---: | --- | --- | ---: |
| Nonendpoint A-chain | 1 | 2 FAIL, 1 PASS in the continuation audit | none observed | 12 |
| Endpoint local ADE | 1 | 3 FAIL, 2 PASS in the owner history; 1 additional root replay PASS | 1 failed debug script; 1 exit-zero startup-warning probe | 16 |
| Doubled horizontal | 1 | 4 FAIL, 1 PASS in the owner history | none observed | 14 |

These are three mathematical checkers, with thirteen owner/continuation
main attempts and one further endpoint root replay at this observation.
Source versions, snapshots and replays do not create additional
mathematical checkers. Formula counts are the assertions in the successful
versions; they are not the number of independent geometric propositions
or a parameter-space exhaustion. The historical 97-source/110-execution
index is unchanged. A new root replay of the doubled-horizontal checker
was not present at this initial review and must be accounted separately
if it is subsequently created.

### Nonendpoint, 12 identities

The original independently supplied source is
`../2026-10-10-genus-two-nonendpoint-trisecant-independent-audit/cartan-countercheck.m2`,
SHA-256 `51d19f313af8381ac1526eb2c67df5c75f142835d13b4595ce35f1adf9bb66e4`.
No separate successful execution of those original bytes is asserted.
The continuation directory retains two failed sources, their raw streams
and execution metadata, then the passing repaired source
`cartan-countercheck.repaired.m2`, SHA-256
`6a8b08f36f28c37865a2fd6708652e1d857fb2695c023687940186b2f91f4c7a`.
The mathematical expressions are unchanged: protected identifiers were
renamed `source -> chainSource` and `denominator -> chainDenominator`;
one printed label was also changed. A global substring replacement is
not an exact reconstruction because other labels contain the word
`source`; a token-aware replacement or a direct diff is appropriate.

The attempt-one record's `source_snapshot` value names the temporary
`cartan-countercheck.snapshot.m2`, whereas the retained file is
`attempt01-failure-source.m2`. The attempt-two record's `source_path`
is the final repaired path, which later acquired different bytes;
its contemporaneous source is `attempt02-failure-source.m2`, hash
`c79b816a6b1e88fdd6baf2418a4550c0ea1d0e0e33e7b1a9c077af27aa569a0e`.
Thus the seal must bind each retained failure snapshot to its own
recorded hash rather than interpreting a historical command path as
the retained source. Temporary working directories were removed after
their evidence was copied. Their commands and isolation are historical
observations, not live process handles.

### Endpoint, 16 identities

The successful current source and root copy have SHA-256
`cbe568f673086ed5f4084aedba3e4075470938c5b0bef223de75f7d65c8337d4`.
Attempt four passed with mechanically corrupted printed `PAendpointS`
labels; attempt five restores `PASS`, without changing mathematical
expressions. Both are observed successful executions. The owner's
aggregate `execution-record.json` repeats final attempt five and does
not denote another execution.

Attempt one retains its exact source and observed tool chunk/exit/error
metadata, but has no separately captured raw stdout or stderr files.
Attempts two through five retain their exact source copies and raw
streams. The root replay has exact original/snapshot hashes, command,
isolated cwd, exit zero and raw-stream SHA-256 values. Diagnostics are
separately identified in `diagnostic-record.json`: one failed script
locates the multiline parsing error; the other probe exits zero with
startup documentation-index warnings. Neither is a successful main
mathematical-verifier execution. Their retained metadata is weaker than
full independently captured streams and must remain labeled as such.

### Doubled horizontal, 14 identities

The successful current source and retained owner copy have SHA-256
`a6f67f5d11e1d964cabc2ef2dc0d6e10b32931b143d81b2b05ccebc3dc14f887`.
All four failures preserve source, stdout, stderr, command, timing,
exit status and source hash. The final repair changes the selected
inverse-Cartan endpoint column from columns 4 and 6 to column 0.
Therefore failure four is an actual incorrect-orientation assertion,
not merely a protected-name or parser scaffold failure. Its retained
stream shows the first twelve checks passing and the A5 assertion
failing. The final successful checker has all fourteen checks.

## Required proof routing

October 11 root acceptance should reach the new independent whole-quartic
dependency audit when it is saved. It was not present at this inventory;
an active agent name is not a durable accepted proof. The final audit
must retain the fixed `C0`, characteristic-zero, quartic-carrier and
arbitrary-positive-mate-degree quantifiers, while leaving unrestricted
higher-degree and universal questions open.

The binding genus-two audit chain must include:

* [Bisection full independent audit](../../notes/2026-10-10-session-genus-two-bisection-full-independent-audit.md),
  its [second-pencil compression audit](../../notes/2026-10-10-session-genus-two-bisection-second-pencil-independent-audit.md),
  the [weighted ribbon conormal audit](../../notes/2026-10-10-session-weighted-ribbon-conormal-independent-audit.md),
  the [ribbon microaudit](../../notes/2026-10-10-session-bisection-ribbon-conormal-microaudit.md),
  and the [normal-bundle audit](../../notes/2026-10-10-session-quartic-normal-bundle-independent-audit.md).
  Older split-cover/root-of-unity and blowup-partition reductions are
  preserved intermediate necessary conditions, superseded by the full
  Cartier-ribbon contradiction.
* [Nonendpoint continuation coverage audit](../../notes/2026-10-10-session-genus-two-nonendpoint-trisecant-continuation-independent-audit.md)
  and [relative Morse branch-preservation audit](../../notes/2026-10-10-session-relative-morse-conductor-branches-independent-audit.md),
  reaching the actual normal conic model, entire conductor, marked-prime
  classification and no-degree-zero-horizontal exclusion. Twelve
  algebra identities do not supply those geometric hypotheses.
* [Endpoint full independent coverage audit](../../notes/2026-10-10-session-genus-two-endpoint-full-independent-audit.md),
  reaching the [full quartic family](../../notes/2026-10-10-session-genus-two-endpoint-full-quartic-reduction.md),
  the [local ADE correction audit](../../notes/2026-10-10-session-endpoint-local-ade-correction-audit.md),
  the [doubled-horizontal arbitrary-ADE audit](../../notes/2026-10-10-session-genus-two-endpoint-double-horizontal-independent-audit.md),
  and the [carrier ideal proof](../../notes/2026-10-10-session-genus-two-trisecant-quartic-carriers.md).
  The older irreducible-residual endpoint note is explicitly insufficient
  as a complete endpoint exhaustion certificate. The full audit repairs
  the zero-coefficient second horizontal/infinity boundary and retains
  all multiplicities before exclusion.

The earlier root acceptances and their transitive genus-zero, genus-one,
normal, smooth-normalization and rationality audits remain required for
the all-quartic conclusion. Historical `pending` owner headers should be
preserved and interpreted through explicit later root acceptance, rather
than silently rewritten or taken as current root conclusions.

This review verifies provenance distinctions and routing needs only.
A final link/hash seal establishes the bound bytes and destinations;
it does not itself prove the mathematical implications or novelty.
