# Residual-degree continuation: proof and scope validation

Date: 2026-10-28. Branch:
`codex/intersections-containing-quartic-2026-10-27`.
The [quantitative synthesis](../../notes/2026-10-28-residual-degree-synthesis.md)
answers which parts of the containing-intersection work give lower bounds
on the **genuine** residual degree. All new deductions remain provisional;
canonical result/question records are not promoted or rewritten.

## Source and review matrix

| Source | Independent review | Scope |
|---|---|---|
| [Graph/order bounds](../../notes/2026-10-28-residual-degree-blowup-bounds.md) | [Singular-carrier agent](../../notes/2026-10-28-residual-degree-blowup-audit.md) | Earlier October 19 inequalities retrieved; new slack, equality, sharpness and nef-cone interpretation |
| [Normal-carrier capacity](../../notes/2026-10-28-residual-degree-singular-carriers.md) | [Blowup agent](../../notes/2026-10-28-residual-degree-singular-audit.md) | Effective Mumford pullback, no Q-Cartier hypothesis, marked A-type and general adjunction corrections |
| [Normalization and first-normal data](../../notes/2026-10-28-residual-degree-normalization.md) | [Separate normalization audit](../../notes/2026-10-28-residual-degree-normalization-audit.md) | Singleton inverse, isolated inverse points, multibranch valuation constraints and first-normal gcd corollary |
| [Marked attachment detector](../../notes/2026-10-28-residual-degree-attachment-detector.md) | [Liaison agent](../../notes/2026-10-28-residual-degree-attachment-audit.md) | Any characteristic; full nonreduced residual scheme; sharp actual fixed-quartic control |
| [Full attachment and low-degree residuals](../../notes/2026-10-28-residual-degree-liaison-budgets.md) | [Root reconstruction](../../notes/2026-10-28-residual-degree-liaison-audit.md) | Reduced/cohomological bounds, actual equation restriction on double lines and ribbons, primary syzygy filters |
| [Integrated interpretation](../../notes/2026-10-28-residual-degree-synthesis.md) | [Separate integration audit](../../notes/2026-10-28-residual-degree-integration-audit.md) | Literal characteristic, denominator, marked/full attachment, residual/once-link and positivity scopes |

Final review decisions and any addenda are recorded in those audits; a
link or inclusion in this table does not independently establish a claim.

## Mathematical controls

The proofs retain the following controls and limitations:

- The universal marked attachment bound has an actual sharp family on
  \(Q\): \(\delta=2s\), marked length \(6s\), full length \(6s^2\).
  This explicitly falsifies substitution of the full length into the
  marked inequality.
- The normal capacity formula recovers the inherited smooth-along-\(C\)
  result. Its general-curve version permits the known characteristic-zero
  twisted-cubic cone example with zero residual and zero Hodge gap; it
  is not an automatic nonexistence theorem.
- The graph's nef cone has only the two known generating directions.
  Both residual-degree coefficients have exact homogeneous sharpness
  families. Changing presentation to \(V_5\) alone adds no automatic
  stronger linear nef inequality.
- Double-line ribbons have unbounded negative genus as abstract curve
  candidates, but actual fixed-degree equations restrict their nilpotent
  parameter. The source never equates all candidates with realized
  residuals through the fixed quartic.
- A first-normal gcd bound is a computable corollary, and the inherited
  graph slope refinement can strengthen it. Fine numerical self-intersection
  may improve it further. No uniformly strongest or uniformly positive
  bound is asserted.

These are symbolic geometric proofs and actual-family controls. No finite
sample is substituted for an all-degree theorem. No new computation was
needed and inherited certificates were not rerun.

## Literature, authority and final repository checks

Primary surface intersection, numerical pullback, Cartier degree and ribbon
sources were inspected live and are linked in the source notes. The
October 19 graph bounds were found before being reinterpreted; the
October 17 pending Hodge-boundary sufficiency claim was located and is
explicitly not used. Literature originality was not established.

The normal-carrier source and audit work over the complex numbers. The
normalization extension separately states its algebraically closed
characteristic-zero proof, while the marked bound is characteristic
independent. These scopes remain explicit in the synthesis.

All source audits and the independent integration review are saved. The
final sweep checked **375 local Markdown targets in 20 files, with zero
missing targets**. A pre-existing whitespace-only blank in the modified
MAP was cleaned during the whitespace sweep. Canonical metadata reports
**37 records, zero errors**. The final text and tracked-diff whitespace
checks pass. No canonical promotion is part of those delivery checks.
