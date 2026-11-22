---
id: STCI-R-0022
title: "Quartic-pair exclusion for the fixed characteristic-zero rational quartic"
kind: theorem
scope:
  characteristic: "0"
  curve: "fixed C0=[s^4:s^3t:st^3:t^4]"
  hypotheses:
    - "Algebraically closed field of characteristic zero"
    - "Integral or, more generally, coprime quartic defining equations F,G with reduced intersection C0"
statement: "No two quartic forms F,G satisfy V(F,G)_red=C0. The filtered-contact, surface, and embedded-neighborhood proofs do not invoke the all-degree quartic-carrier exclusion STCI-R-0001."
dependencies:
  - "STCI-R-0001"
  - "STCI-R-0020"
evidence:
  - "research/arguments/normal-geometry/quartic_pair_obstruction.md"
  - "research/arguments/normal-geometry/intrinsic_fourth_extension.md"
  - "research/computations/verify_44_filtered_contact_2026_10_23.py"
  - "research/computations/audit_mf6_e1_primitive_2026_10_07.py"
independent_audits:
  - "research/arguments/normal-geometry/quartic_pair_obstruction.md"
  - "https://github.com/markluxton1/STCI/blob/f2f5c4dbe5bef0eeb5112d402ffeb513133b43bc/research/computations/audit_44_filtered_contact_2026_10_23.py"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Does not exclude mates of degree other than four."
  - "The filtered-contact route uses exact complete-source calculations; the surface route instead uses global characteristic-zero surface theory. Neither follows from symmetric algebra alone."
---
# Quartic-pair exclusion

## Statement

Over an algebraically closed field of characteristic zero, no two homogeneous quartics cut out the fixed embedded smooth rational quartic set-theoretically. Reducible and nonreduced defining equations are included. The asserted radical equality is projective, equivalently equality after saturation of homogeneous ideals.

## Hypotheses and quantifiers

The curve is \(C_0=[s^4:s^3t:st^3:t^4]\), or a projective equivalent. A proper quartic pair with sole support \(C_0\) would have generic transverse length four. This theorem has no assertion about mates of degree other than four or about arbitrary rational quartic embeddings.

## Proof and dependencies

**Canonical shortest proof: reduce to the all-degree quartic-carrier
theorem R-0001.** If two quartics \(F,G\) cut out only \(C_0\)
set-theoretically, their irreducible factors are positive-degree
carriers with the other equation as a sole-support mate. Every
irreducible factor must therefore have degree at least five by
[R-0001 plus the plane/quadric/cubic exclusions](../frameworks/carrier-normalization/degree_exclusions.md#52-factors-and-the-degree-bound),
impossible for a quartic. This proves the present exclusion for
**all** coprime quartic pairs without a separate rank-four
analysis. It is a **corollary** of a strictly stronger theorem,
not an independent replacement proof of R-0001.

**Independent mechanism proofs (preserved, not required for the
shortest result).** The [quartic-pair chapter](../arguments/normal-geometry/quartic_pair_obstruction.md)
establishes the same result **without using R-0001**, and gives
stronger intermediate statements that remain relevant to
higher-degree filtrations and global singularity budgets.
Its common reduction uses R-0020, the unique smooth quadric,
complete-intersection duality and rank-four Gorenstein
algebra, yielding \(L=\mathcal O(-7),\deg D=3\)
or \(L=\mathcal O(-6),D=0\).

The filtered-contact proof enumerates the allowed triples and their complete quartic sources, then proves a nonzero cubic-contact determinant for every nonfactored pencil. Exact source matrices and the retained scripts supply its finite calculation dependencies; orbit exhaustion and uniqueness of the quadratic correction are proved in the chapter.

The surface proof uses the same local data to obtain a first-symbol pencil of degree \(6+2e\), moving germs \(uv-t^4\), and defect germs \(uv-t^{2d_p}\). Their resolution would have independent exceptional rank \(24-\#\operatorname{Supp}D\ge21\). The direct-blowup presentation constructs the chains and proves crepancy; Noether's formula and Hodge theory give exceptional rank at most nineteen. The K3 presentation is another expression of this surface mechanism. Neither surface presentation needs the primitive-triple classification or computer calculations.

## Evidence and verification

The theorem's scope and prior independent reviews of the filtered-contact and K3 proofs remain unchanged. Independent consolidation review reconstructed and accepted the replacement proof, the conditional rank-four pencil budget, the general contact-module lemma and its characteristic scope, and the preservation of the alternative proofs and controls. The computation scripts are necessary only for the finite-source route, not for the direct surface proof; no inherited calculation was rerun for this consolidation.

Within that finite-source route, the
[primitive-triple interpolation proof](../arguments/carriers/sextic_triple_intrinsic_contact.md#quartic-interpolation-from-five-sparse-sections)
now replaces the \(e=1\) full-source dimension ranks. The explicit
quartic equations and contact identities are retained, as is the
separate defective \(e=0\) source calculation. This proof replacement
does not change the exclusion's scope.

## Consequences and limitations

The exclusion itself is subsumed by R-0001; the alternate bounded proofs remain useful because their **mechanisms** (actual-source lifting, intrinsic extensions, and global exceptional-rank budgets) extend beyond this corollary in ways the complete quartic-carrier theorem alone does not describe. They do not resolve unrestricted characteristic-zero STCI. The [independently reconstructed fourth-extension proof](../arguments/normal-geometry/intrinsic_fourth_extension.md) now supplies an embedded-neighborhood argument. It classifies the two allowed saturated quadruple types through their contact-extension classes, leaving only 4C on Q; elementary quadric restriction then rules out a proper quartic pair. This alternative uses exact transition calculations but no source-pencil orbit list or global surface bound. The stronger intermediate classification is recorded as a reviewed mathematical result; it has no separate result ID.
