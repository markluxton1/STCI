# Arbitrary-degree absorption continuation: validation and scope

Date: 2026-10-27. Continued on codex/intersections-containing-quartic-2026-10-27.
This validates the [arbitrary-degree synthesis](../../notes/2026-10-27-arbitrary-degree-absorption-synthesis.md).
All new source deductions remain reviewed provisional evidence; no canonical promotion.

## Independent reviews

- [Deformation audit](../../notes/2026-10-27-absorption-deformation-audit.md): reconstructs smooth-carrier arbitrary finite transfer, sufficient degree threshold, actual hypersurface lifts, Cartier residual gluing, the smooth-along-C capacity bound, general-curve template, normal Cartier-multiple extension and weak normal divisorial-ideal extension. The last statement has separate review in section 8.
- [Attachment-module audit](../../notes/2026-10-27-absorption-attachment-module-audit.md): reconstructs full-primary support, torsion correction, non-Gorenstein canonical-module restriction length and combined full-attachment budget.
- [Flag audit](../../notes/2026-10-27-absorption-flag-tangent-audit.md) and [formal addendum](../../notes/2026-10-27-absorption-formal-addendum-audit.md): reconstruct marked Quot motion, actual-pair tangent compatibility, Artin small-extension lifting, fixed-quartic ribbon control and failure of flat full-primary extraction across absorption.
- [Conductor audit](../../notes/2026-10-27-absorption-characteristic-conductor-audit.md): reconstructs all-N Frobenius exponent calculation, finite-versus-formal quantifiers, semi-invariant descent and conditional positive-cone cancellation.
- [Integration audit](../../notes/2026-10-27-absorption-integration-audit.md): checks the main synthesis and source hypotheses. The later weak non-Q-Cartier normal extension is covered by the separate deformation audit, not silently added to its original scope.

## Corrections incorporated

The finite invariant-quotient lemma now assumes a finitely generated normal k-domain, which justifies finiteness over invariants.

The ribbon control explicitly uses Ext1 on C. The ambient Ext1 on the threefold need not vanish and has additional normal contributions; the source no longer leaves these categories ambiguous. The formal note's arbitrary-curve/arbitrary-characteristic scope applies to sections 2–4; its section 5 is explicitly the fixed characteristic-zero quartic control.

The capacity-bound equality control includes the actual Segre factorization determining the double ruling, rather than inferring multiplicities from divisor classes.

Full thick attachment and reduced-marked attachment remain distinct. The normal marked nilpotent ideal is not identified with the entire nilradical.

## Exact new computation

The [new local M2 verifier](../../computations/verify_attachment_module_nonlci_2026_10_27.m2) and [saved output](../../computations/attachment_module_nonlci_2026_10_27.txt) pass over Q, F2 and F3. They check primary extraction, residual linkage, a Hilbert--Burch presentation, equation-module torsion, Fitting ideal and marked attachment length. The accompanying audit supplies an all-characteristic symbolic proof. The example is a falsification of a determinant-only general detector, not a homogeneous construction for the fixed quartic or a finite extrapolation to a theorem.

The general deformation construction and capacity theorem use proofs; no list of degree cases or inherited certificate reruns was substituted for them.

## Repository validation

- Canonical validator: Checked 37 canonical records; 0 errors.
- Targeted local Markdown links: 422 targets in 24 files; 0 missing, after correcting two unintended formal-group Markdown links.
- Whitespace: checked before staging and on the staged changes.
- Canonical result and question records: not changed.
- The unrelated pre-existing file-manifest.txt: excluded from this research change.

Primary source versions and scope limits for the discrepancy papers are retained in the [focused literature record](../../notes/2026-10-27-absorption-discrepancy-literature.md). That record does not claim exhaustive coverage or a new STCI theorem.
