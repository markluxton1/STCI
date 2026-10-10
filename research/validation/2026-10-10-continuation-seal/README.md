# October 10 continuation record audit

This directory is an independent record-integrity audit prepared by
`oct10_record_seal`. It does not execute mathematical verifiers or certify
mathematical proofs. The root-declared acceptance document and its separately
audited arguments govern mathematical status.

Run the standard-library-only checker in the repository root:

```sh
python3 research/validation/2026-10-10-continuation-seal/check_record.py --preliminary
```

The preliminary result is a working observation while root reconciles canonical
files. It must not be used as a frozen final seal. After root declares the
canonical routing ready, the auditor runs:

```sh
python3 research/validation/2026-10-10-continuation-seal/check_record.py --seal-once
```

The final mode refuses to overwrite `result.json`. It binds source, copied
source, execution manifest, raw stream, generated result, failed source and
proof-routing bytes, while observing that the canonical files do not change
during the check. The observed command, exit code and checker/result hashes
are then recorded separately in `execution-manifest.json`.

The older index of **97 distinct source paths / 110 explicit executions**, and
the older integrity seal's **2,006 checks / 313 scoped local links**, remain
historical and unchanged. They do not cover later proof or canonical edits.
The present checker distinguishes exactly two new successful genus-one
Macaulay2 source paths from their root replay copies. Both agents and root ran
these same source paths; the copies add no independent verifier. The scoped
October 10 genus-one histories contain four successful M2 executions including the two
root replays, three failed M2 executions, and one Python import failure before
mathematical checks. Runtime probes and earlier post-seal owner computations
are deliberately outside that scoped accounting. No aggregate 99/118 claim
is made for all repository research.

A separate line-position structural source has 17 exact homogeneous
identities, one observed successful M2 execution, and two recorded development
failures. It is accounted separately from the genus-one histories, and its
source alone gives no mate exclusion. Its passing record is nonisolated and
binds the exact final source; the superseded failed source bytes were not
preserved. That limitation is explicit rather than repaired with guessed
source revisions. Newly arriving secant and bisection notes are recorded with
their individual status headers, while root's acceptance identifies which
scopes have actually been promoted.

`interfaces-namespace-failed-reconstructed.m2` restores the first interface
attempt's bytes by reversing only the recorded identifier repair:
`netCoefficients` becomes `net` at its three occurrences. Its SHA-256 is
`a515598a11636a23cfba3f9af2b2e21b43fd43214f5711e40bf35873fad5903a`, exactly
the original pre-run hash retained in the interface execution record. This is
a mechanical reconstruction matched to that recorded hash, not a claimed
contemporaneous snapshot. It was not rerun during this integrity check.

The repeated-partition audit retains an import-failed Python source, a hashed
parser-failed M2 source and a mechanically reconstructed protected-name source
whose original pre-run hash was not recorded. That latter limitation remains
explicit. Its saved successful stdout is a faithful transcript written after
the execution; independently captured raw subprocess stdout/stderr are
preserved by the root's isolated replay. The two kinds of provenance are not
conflated.

The checker deliberately retains changed-file observations against the October
9 seal. A new seal records the current accepted routing; it does not rewrite
the historical seal or imply its old bound files remain current.
