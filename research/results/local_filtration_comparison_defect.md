---
id: STCI-R-0030
type: result
title: Local filtered-equation comparison and punctual defect criterion
scope: "#scope"
statement: "#statement"
proofs:
  - name: initial ideals, the DVR length identity, and smooth-carrier straightening
    at: "research/arguments/filtered_equation_comparison.md#local-comparison-and-the-punctual-defect"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Local filtered-equation comparison

## Scope

The comparison itself is local algebra for ideals \(J\subset I\) in a
Noetherian local ring \(R\), in arbitrary characteristic. The geometric
conclusions concern a smooth codimension-two curve \(C\) in a smooth
threefold and a two-generator regular-sequence ideal \(J=(f,g)\subset I_C\).
The generic count assumes a transverse parameter ideal. The length formula
assumes generic vanishing on an integral smooth curve. The smooth-carrier
calculation is equicharacteristic.

## Statement

Write \(S=\operatorname{gr}_I R\), \(S_+=\bigoplus_{n>0}S_n\),
\(H=\operatorname{in}_I(J)\), and \(B=\operatorname{in}_I(IJ)\).
With \(K=I/J\), the full normal graded algebra is
\(\operatorname{gr}_K(R/J)=S/H\).
Give the actual equation module \(D=J/IJ\) the filtration
\[
F^nD=((J\cap I^n)+IJ)/IJ,\qquad n\ge1.
\]
The first conormal map \(\phi:D\to I/I^2\) has kernel \(F^2D\). Then
\(S_+H\subset B\subset H\), and in every degree \(n\ge1\) the quotient map
gives a canonical exact sequence
\[
0\longrightarrow \Delta_n=B_n/(S_+H)_n
\longrightarrow Q_n=H_n/(S_+H)_n
\longrightarrow G_n=\operatorname{gr}_F^nD=H_n/B_n
\longrightarrow0 .
\]
Thus the comparison is invertible in all degrees precisely when \(B=S_+H\).

At a generic transverse point where \(R\) is regular of dimension two,
\(I\) is its maximal ideal and \(J\) is a two-generator parameter ideal,
\(\dim_{\kappa(\eta)}\Delta=\mu(H)-2\). Here \(\mu(H)\) is the minimal
homogeneous generator count over \(\kappa(\eta)\).

If \(\Delta_\eta=0\) along a smooth integral curve, at every closed-point
DVR stalk the torsion modules fit in
\[
0\longrightarrow\Delta_n\longrightarrow\operatorname{tors}Q_n
\longrightarrow\operatorname{tors}G_n\longrightarrow0,
\qquad
\ell(\Delta_n)=\ell(\operatorname{tors}Q_n)-\ell(\operatorname{tors}G_n).
\]
In particular torsion-free \(Q\) and generic vanishing imply \(\Delta=0\).

In the smooth equicharacteristic setting, if either carrier has a nonzero
fiber conormal symbol at \(p\), equivalently is smooth there, then
\(\Delta_p=0\). Thus
\[
\operatorname{Supp}\Delta
\subset C\cap\operatorname{Sing}V(f)\cap\operatorname{Sing}V(g).
\]

## Limitations

The support statement gives a necessary condition for a nonzero defect.
In regular codimension two the
[conormal entry ideal](conormal_entry_annihilator.md) annihilates the
defect scheme-theoretically.
Torsion in \(Q_n\) can survive in \(G_n\), and the length formula uses their
difference, as illustrated by the
[supported quadruple](supported_quadruple_equation_filtration.md).
The local comparison alone gives no global line-bundle
identification or splitting of the first conormal kernel. The
[prescribed characteristic-two quartic](quartic_char2_fourth_equation_kernel.md)
needs the full filtration and compatible chart lifts. The relative
[normal Koszul construction](normal_koszul_comparison_defect.md)
has its own proof and indexing.

Whether \(\Delta\) can be nonzero and punctual with \(\sqrt J=I\) and
\(\Delta_\eta=0\) remains open here. The
[degree-four counterexample](initial_equation_cancellation_counterexample.md)
has nonzero generic defect after adjoining a curve parameter. The
[supported length-five specialization](supported_length_five_defect_specialization.md)
has zero relative defect and nonzero actual defect on the transverse
closed fiber. The relative DVR criterion alone gives no conclusion about
the actual comparison after such a base change. The separate
[normal-flat specialization theorem](normal_flat_comparison_specialization.md)
gives sufficient hypotheses for that identification.

## Review

The Phase 5 nonauthor reviewer accepted this local route after reconstructing
the filtration denominator, the presentation syzygies and Artin–Rees
finiteness, the generic generator count, and the torsion sequence over the
DVR. The reviewer checked the completed-local initial ideals with a
possibly nonunit leading coefficient and faithful-flat descent. This
decision covers the local comparison, count, length and support statements
under their respective hypotheses.

The October 23 independent review checked the quotient denominator, the
direction of comparison, the presentation syzygies and the completed-local
smooth-carrier calculation. It kept the leading coefficient nonzero in the
coefficient domain while allowing it to vanish at the closed point.
[October 23 comparison review](../supplements/IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#filtered-equation-module) ·
[Smooth-carrier review](../supplements/IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#additional-smooth-carrier-proposition)

The October 24 continuation supplies the generic generator excess and the
DVR torsion sequence. The October 26 audit independently checked the local
quotients, generator count, DVR formula and scope of the support condition.
It recorded no fresh executable replay and did not check the global quartic
gluing or the relative spectral sequence in that audit.
[Generic and DVR arguments](../supplements/DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md#4-generic-generator-counts-and-punctual-length) ·
[October 26 audit and decision](../supplements/DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md#local-filtration-audit-and-scope-boundary--2026-10-26)
