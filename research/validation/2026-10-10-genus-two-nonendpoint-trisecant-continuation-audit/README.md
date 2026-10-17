# Isolated continuation replay of the all-length A-chain identities

This directory retains two infrastructure failures and the final passing
isolated replay. The mathematical source was supplied by the preceding
independent coverage worker at
`research/validation/2026-10-10-genus-two-nonendpoint-trisecant-independent-audit/cartan-countercheck.m2`.
It was copied into a temporary working directory and run with
`/opt/homebrew/bin/M2 --script`; all generated output was copied back here.

* `attempt01-failure-source.m2` is the initial source, hash
  `51d19f313af8381ac1526eb2c67df5c75f142835d13b4595ce35f1adf9bb66e4`.
  It passed six identities, then failed on assignment to protected
  Macaulay2 identifier `source`.
* `attempt02-failure-source.m2` renames that identifier to `chainSource`,
  hash `c79b816a6b1e88fdd6baf2418a4550c0ea1d0e0e33e7b1a9c077af27aa569a0e`.
  It passed nine identities, then failed on assignment to protected
  identifier `denominator`.
* `cartan-countercheck.repaired.m2` also renames `denominator` to
  `chainDenominator`, hash
  `6a8b08f36f28c37865a2fd6708652e1d857fb2695c023687940186b2f91f4c7a`.
  It passed all **12 symbolic identities**, exit zero. The exact command,
  isolated cwd, observed timestamp, source hash and timings are in
  `execution-record.json`; `stdout.txt`, `stderr.txt` and `result.json`
  preserve the output.

The two renamings change no mathematical expression. Each attempt has
its full stdout, stderr and metadata. The temporary working directories
were removed after their evidence was copied. To rerun the final checker
in an isolated directory, create the relative output directory named
inside its final `openOut` statement before invoking Macaulay2.

The original attempt and both repaired versions count as **one
mathematical checker**, with three observed executions in this directory.
This directory does not change the historical 97-source/110-execution
index. Its `new_distinct_mathematical_source=false` metadata means that
the continuation replay is a version/replay of the independently supplied
checker, not an additional mathematical source.

The geometric attachment, full divisor coverage and integer-parameter
inequalities are proved separately in
[the continuation independent audit](../../notes/2026-10-10-session-genus-two-nonendpoint-trisecant-continuation-independent-audit.md).
These exact identities do not cover endpoint trisecants, lambda zero,
arbitrary carrier degrees or the universal STCI theorem.
