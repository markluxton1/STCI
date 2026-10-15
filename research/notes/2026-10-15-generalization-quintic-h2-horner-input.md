# Exact Horner input for the captured H2 generators

Status: **EXACT FORMAT VALIDATION**. This note changes the serialization of
already prepared polynomials. It proves no new exclusion and does not compute
a Gröbner basis, saturation, dimension, or elimination ideal.

The prepared inputs are the twelve `normalized-generator-0.txt` through
`normalized-generator-11.txt` files in
`research/validation/2026-10-15-quintic-h2-unified-incidence/attempt-04-flint-preparation`.
Their underlying construction and unit-factor divisions are treated as
premises here; neither was rerun. The preceding flat-expression modular
prospect did not reach its first post-import stage within its 45-second
bound. This motivated a format-only input repair.

## Export and exact preservation

The new source
`research/computations/generalization_quintic_h2_horner_input_2026_10_15.c`
reads each explicitly listed input in `QQ[deltaPar,vPar,wPar]` using FLINT,
extracts its full rational coefficients and exponent triples, sorts the
triples lexicographically, and emits nested Horner expressions with outer
variable `deltaPar`, then `vPar`, then `wPar`. Exponent gaps and final powers
are retained. Signed rational coefficients are parenthesized.

For exponents `e0 > e1 > ... > er`, each layer is

    (...((c0*x^(e0-e1)+c1)*x^(e1-e2)+c2)...+cr)*x^er.

The source reparses the actual emitted text and checks exact FLINT equality
against its corresponding input before recording success. All twelve exact
checks passed in 0.502 seconds. The files total 3,566,339 bytes in their
original form and 2,253,870 bytes in Horner form. More consequentially, the
nested evaluation avoids building a polynomial from one long flat sum.

The successful source snapshot, per-file degrees, term counts, byte counts,
input/output SHA256 hashes, compilation invocation and raw streams are in

`research/validation/2026-10-15-h2-horner-input/attempt-03-exact-export-trim-repair`.

## Bounded Macaulay2 load-only check

A fresh Macaulay2 process declared exactly `QQ[deltaPar,vPar,wPar]` and loaded
only the twelve new Horner expressions. After each load it asserted the
FLINT degree and exact term count. All twelve passed in 7.802 seconds under
a 45-second external timeout. Its source, stage markers, per-generator
metadata, execution record and raw streams are in

`research/validation/2026-10-15-h2-horner-input/attempt-04-qq-load-only`.

The checked term counts, in generator order, are
`2984,6629,6845,7016,7191,7303,6082,6278,6459,6622,6736,6580`.
The checked total degrees are
`37,52,52,52,52,52,50,50,50,50,50,49`.

This is a successful cross-engine import check. Exact preservation is
supplied by the FLINT text round trip. The timings are observations of these
runs, not a controlled benchmark against the earlier modular prospect.

## Preserved failure and reuse

Attempt 01 failed before export because FLINT's pretty parser rejected the
trailing newline in the captured input text. Its source snapshot and actual
assertion failure are retained. The repair trims trailing whitespace only;
original input bytes and hashes remain recorded. Attempt 02 was reserved by
that runner invocation but never started Macaulay2, as its `NOT_RUN.md`
explains. The successful repaired executions are attempts 03 and 04.

The reusable exporter accepts arbitrary explicitly listed three-variable
polynomial files, in the required output order:

    /private/tmp/stci-h2-horner-input-2026-10-15 OUTPUT_DIR INPUT_FILE [INPUT_FILE ...]

The executable is temporary. Its source is authoritative; compile using the
saved invocation or the bundled runner
`research/computations/run_quintic_h2_horner_input_2026_10_15.py`.
Compile this source with assertions enabled: some required parser and I/O
calls occur inside `assert`. The recorded compilation does not define
`NDEBUG`; a future build using `-DNDEBUG` is unsupported.
The runner preserves its fixed attempt directories and intentionally refuses
to overwrite them. For a new generator list, use a new validation directory
and the exporter directly. Output names are `horner-generator-0.txt`, etc.,
in explicit command-line input order. No generator is recomputed or
normalized by this exporter.

An independent read-only implementation and record review passed. It checked
the Horner recurrence and rational coefficient extraction, recomputed all
input/output/source manifest hashes, and inspected the complete M2 import
records without running CAS. Its report is saved as
`research/validation/2026-10-15-h2-horner-input/independent-read-only-review.md`.
This review is not a second polynomial verifier or an incidence certificate.
The geometric common-root/conductor incidence remains unresolved by this
format validation.
