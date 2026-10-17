# Independent read-only source and record review

Reviewer: delegated agent `review_horner` under the Horner-input task.
No edits, CAS computations, elimination, or accepted-verifier runs were
performed by this reviewer. The owner copied this received report into the
validation record.

The exporter recursion correctly groups terms in descending
`(deltaPar,vPar,wPar)` order, uses full rational coefficients, applies each
exponent gap, and retains the final minimum-exponent factor. It handles a
zero polynomial explicitly and reparses the actual written output before
comparing it with the corresponding input.

The reviewer independently recomputed the saved manifest hashes without
running CAS code. All matched: current exporter source and captured
`source.c`, current runner, all twelve prepared input files, all twelve
generated Horner files, and the captured Macaulay2 source hash. Twelve
per-generator load records exist.

The execution records show exact export completed with exit code zero in
0.502 seconds, with twelve `exact_equal=true` rows. Macaulay2 loaded all
twelve expressions over QQ with the expected degree and term count,
completed with exit code zero in 7.802 seconds, produced empty stderr, and
left the final stage `complete-load-only`.

The evidence supports exact FLINT format preservation plus successful M2
import. The M2 check compares degree and term count; it does not independently
compare every coefficient across engines.

Maintenance caution: required operations, including parsing, occur inside
`assert`. The recorded compile command has no `-DNDEBUG`, so those operations
executed. Future builds must preserve assertions or replace these with
explicit checked calls.
