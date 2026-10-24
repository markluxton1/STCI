# Marked-embedding Delta continuation: new validation

Date: 2026-10-24. Scope: the [marked-embedding report](../../notes/2026-10-24-delta-embedding-geometry-report.md), its linked local proofs and independent reviews. No sole-support hypothesis is imposed in the general investigation.

These are **new finite checks**, not replays of the merged October 23–24 scripts. The general statements depend on the displayed proofs and independent reconstruction, not on agreement of samples. No global projective realization, arbitrary-parameter theorem, sheaf reconstruction, or STCI consequence follows from these computations.

## Exact computations

Run from the repository root:

```sh
M2 --script research/computations/verify_delta_conormal_annihilator_2026_10_24.m2
M2 --script research/computations/verify_delta_rees_equation_module_2026_10_24.m2
python3 research/computations/validate_records.py
git diff --check
```

| Check | Actual outcome | Captured output |
|---|---|---|
| Annihilator family, `r=1,2,3` | All three full-Rees samples pass; exact annihilator powers checked | [Macaulay2 log](conormal-annihilator-m2.log) |
| Equation-module family, `(a,b)=(2,4),(3,4),(2,5),(4,5)`, and labelled carrier square | All five samples pass; full saturated ideals and full syzygy modules independently computed before section restriction | [Macaulay2 log](rees-equation-module-m2.log) |
| Canonical metadata | 23 records checked; zero errors; no canonical records changed | [Validator log](canonical-records.log) |
| New note and navigation links, whitespace | Targeted local links and new text checked; tracked diff has no whitespace errors | [Integration log](integration.log) |

Macaulay2 is the locally available `/opt/homebrew/bin/M2`. The equation-module script retains the target module of the generator matrix when comparing syzygy images; otherwise different grading shifts can make equal underlying relations compare unequal as embedded graded modules.

## Proof review boundary

- [Annihilator proof](../../notes/2026-10-24-delta-conormal-annihilator-proposal.md): proposing agent and two independent reviewers reconstructed the elementary determinant/Koszul argument; the [separate audit](../../notes/2026-10-24-delta-annihilator-review.md) records the weaker hypotheses.
- [Rees proof](../../notes/2026-10-24-delta-rees-specialization-proposal.md): the [separate audit](../../notes/2026-10-24-delta-rees-specialization-review.md) independently reconstructs the torsion kernel, exact specialization, flatness qualification, full family ideal and syzygies.
- [Normal geometry](../../notes/2026-10-24-delta-normal-geometry-proposal.md) and [base change](../../notes/2026-10-24-delta-base-change-proposal.md): their review sections identify the independent reviewers, hypotheses tested, and precise conclusions. General proofs are algebraic; inherited example calculations are cited as premises and not represented as new replays.

These are agent proof audits, not human referee acceptance or canonical promotion.

## Development repairs

The annihilator script initially used protected Macaulay2 identifiers; descriptive names replaced them. The first equation-module run compared syzygy images with different target grading shifts, producing an assertion failure. Retaining the actual target module corrected the comparison; the relations and saturated ideals were unchanged. Only the final successful runs are counted in the table. No failed development run is treated as a mathematical counterexample or certificate.
