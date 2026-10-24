# Special lines and planes: validation and independent-review record

Date: 2026-10-24.
Scope: the fixed curve [s^4:s^3t:st^3:t^4] over an algebraically closed
field of characteristic zero.
Status: **reviewed exploratory proposal; no canonical promotion or new
STCI exclusion**.

## Research artifact and independent audits

- [Self-contained research note](../../notes/2026-10-24-special-lines-planes-research-note.md)
- [Independent geometry audit](../../notes/2026-10-24-special-lines-planes-geometry-audit.md)
- [Independent STCI scope audit](../../notes/2026-10-24-special-lines-planes-stci-audit.md)
- [Independent osculating normal-count reconstruction](../../notes/2026-10-24-osculating-normal-count-review.md)

The geometry audit found a substantive omitted-components error in the
initial dual singular-locus description. The corrected reduced singular
locus consists of the osculating quartic, bitangent quartic, and two
endpoint pencil lines. The audit reconstructs all four components and
explains why checking only the original two parametrizations could not
establish completeness. The corrected script additionally checks both
endpoint pencils. The original failure is retained in the audit and
dual-incidence derivation; it is not erased by a PASS label.

The normal-count support note had a scalar sign reversed in its displayed
quadric factorization of the diagnostic cubic. It was corrected to
(a^2-b^2)(bc^3-ad^3), matching the main note and exact expansion.
Its divisor and all conclusions were unaffected.

The STCI audit independently reconstructs the local parameter-length
formula, smooth-carrier adjunction, residual conditions, normal-count
qualifications, and finite-flat incidence identities. A wording refinement
distinguishes absence of a forced singularity at a section's concentration
point from the global requirement for singularities somewhere on the curve.

## Exact new computation

Source: [verify_special_lines_planes_2026_10_24.py](../../computations/verify_special_lines_planes_2026_10_24.py).
Environment actually used: Python 3 with SymPy 1.14.0, through the existing
temporary interpreter /tmp/stci-z4-env/bin/python. No new packages were
installed. Any Python 3 interpreter with SymPy can run the script.

From the repository root:

    /tmp/stci-z4-env/bin/python research/computations/verify_special_lines_planes_2026_10_24.py
    python3 research/computations/validate_records.py
    git diff --cached --check

The deterministic [checks.json](checks.json) records eleven PASS groups:
quadric uniqueness; homogeneous osculation; bitangency; the corrected dual
components and quartic endpoint intersection; tangent/secant determinants;
the paired-secant cubic and its normal symbols; its residual quadric
divisor; polarity; the smooth-along-C cubic with six coincidences; its
proper residual pair; and local smooth-surface section examples.

All decisive coefficient calculations expand the full polynomial before
extraction. The script uses exact arithmetic and returns nonzero on a failed
assertion. Its finite tests of local examples supplement the general
proofs, without proving a global STCI existence/nonexistence statement or
an exhaustive classification by computation.

Canonical metadata validation returned:

    Checked 23 canonical records; 0 error(s)

The accepted conormal-splitting and degree-four exclusion computations
were not rerun. No files under the canonical results or questions
directories were changed.

## Branch and preservation boundary

Research branch: codex/special-lines-planes-2026-10-24.
Base: d024e2b3eeaae4e439e622baf8259a10b83a5279, the current clean
codex/delta-embedding-geometry-2026-10-24 checkout at the start of the
investigation. This is a separate local research branch, without an
assertion that its base is main. Publication and canonical promotion
are outside this change.

The companion [manifest](manifest.json) records SHA-256 hashes of the delivered note,
supporting evidence, audits, script, and JSON. Hashes preserve the reviewed
file identity; they do not certify mathematical truth.
