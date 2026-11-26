# Constructing CI equations from transverse Chow coefficients

**Status:** research synthesis and elementary comparisons, characteristic zero unless stated otherwise. The organizing principle is a research objective, not a new universal exclusion theorem. Existing proof owners are linked below. The additional product/Grassmannian and centered-section formulas are recorded with their derivations for subsequent independent review.

## 1. The organizing principle: build the equations from the cycle

Start with the unordered configuration
\[
 \sigma=\sum_i n_i[(u_i,v_i)]\in\operatorname{Sym}^m T,\quad
 T=(\mathbf G_m)^2,\quad m=\sum_i n_i,\quad
 C_{u,v}=[s^4:s^3t:u st^3:v t^4].
\]
Write \(z,x,y,w=x_0,x_1,x_2,x_3\), \(A=xy,\ B=zw\),
\(q_i=u_i/v_i\), and \(\eta_i=u_i^2/v_i\).
For fixed degrees \(d,e\) with \(de=4m\), the objective is to describe
the realization locus \(\mathcal R_{d,e}\) of configurations that are
the **entire fundamental cycle** of an actual proper pair \(F_d,G_e\).

Reverse the usual order of investigation. Rather than select a carrier
and seek a mate or compute an invariant after finding \(F,G\), construct
the canonical objects of \(\sigma\) first. Each then specifies
requirements on the unknown equations: ideal memberships and their
Koszul cofactors, prescribed section spaces and line bundles,
determinantal presentations, compatibility of gradients, and gluing
through the coordinate boundary.

The polynomials
\[
 \mathcal C_\sigma(X,Y,W)=\prod_i(X+u_iY+v_iW)^{n_i},\qquad
 H_\sigma(A,B)=\prod_i(A-q_iB)^{n_i}
\]
are the natural coefficient coordinates of this realization problem.
The latter is a specialization of the former:
\[
 H_\sigma(A,B)=\mathcal C_\sigma(0,-B,A)/\mathcal C_\sigma(0,0,1).
\]
The full transverse Chow polynomial determines the cycle but not a
nonreduced scheme realizing it. The realization locus is constructible
(by the proper-pair locus and the Chow-form/resultant morphism);
equations alone need not describe it. The exact reduced-cycle criterion,
including a coprime-pair condition, is already proved in
[transverse Chow coefficients](transverse_chow_moment_realization.md).
The moving nonreduced case is the genuine gap.

**Research objective:** understand the geometry of realization: how an orbit configuration, a family of embedded transverse neighborhoods, and a common global section of two prescribed line bundles fit together. The coefficient relations record this geometry. Spectral balance is one informative test case, not the organizing principle, and obtaining an exclusion is not a prerequisite for useful understanding.

### What the spectrum can and cannot encode

Write \(H=A^m-M_1A^{m-1}B+M_2A^{m-2}B^2-\cdots\).
The character \(q=xy/(zw)\) is distinguished by the relation
\(1+3=0+4\) of longitudinal weights. Under transverse torus translation
all \(q_i\) scale by the same unit, so \(M_j\) scales by its \(j\)-th
power. Vanishing is intrinsic under that symmetry, not under arbitrary
changes of character. The first condition is eigenvalue balance,
\(M_1=\sum n_iq_i=0\). On the small diagonal \(M_1=mq\ne0\) in
characteristic zero; in characteristic dividing \(m\) this separator
does not work. Equivalently,
\([YW^{m-1}]\mathcal C_\sigma=M_1[W^m]\mathcal C_\sigma\).

The full spectral polynomial alone cannot distinguish all configurations.
For example \(F=x^4-z^3w,\ G=y^4-zw^3\) realizes the four reduced
curves \(C_{\zeta,1}\) for \(\zeta^4=1\). The four curves
\(C_{1,\zeta^{-1}}\) have the same \(H=A^4-B^4\) but are all on
the irreducible cubic \(z^2y-x^3=0\). Any quartic containing them
must contain the cubic by degree exhaustion (16 > 12), so there is
no proper (4,4) pair for this second cycle. In fact the existing
[degree-four spectral surjectivity](chow_realization_moment_separation.md)
shows every depressed quartic with nonzero constant term occurs.
No further universal independent equation in just those quartic
spectral coefficients should be sought. The paired information in
\(\mathcal C_\sigma\) is indispensable for full realization.
The reciprocal first moment is not universally zero either.

## 2. The endomorphisms arise from the configuration itself

The projected effective divisor \(D=\sum_i n_i[q_i]\) on
\(\mathbf G_m\) has coordinate ring
\[
 E_D=k[T,T^{-1}]/(P(T)),\qquad P(T)=H(T,1).
\]
Multiplication by \(T\), denoted \(\Phi\), has characteristic polynomial
\(P\), trace \(M_1\), exterior-power traces \(M_j\), and determinant
\(M_m\). Its traces of powers are the spectral power sums (Newton
identities in characteristic zero). Basis change conjugates \(\Phi\);
transverse translation scales it. This gives a direct reason to think
of balance as tracelessness. The projected-divisor algebra is **not**
the actual CI algebra, and repeated eigenvalues need not correspond
to the same Jordan structure there.

On the dense projective torus use
\[
 r=x/z,\quad U=z^2y/x^3,\quad V=z^3w/x^4,\quad
 [z:x:y:w]=[1:r:Ur^3:Vr^4].
\]
Each orbit is \(\mathbf G_m\times\{(u_i,v_i)\}\). The actual CI
restricts to a finite flat rank-\(m\) algebra over \(k[r^{\pm1}]\)
(the support is finite over the base, the nilpotent thickening is
finite, and CM implies torsion-freeness). Its commuting multiplication
operators have
\[
 \det(TI-\mu_{U/V})=P(T),\qquad
 \det(XI+Y\mu_U+W\mu_V)=\mathcal C_\sigma(X,Y,W).
\]
These identities follow by filtering each local generic algebra by
its maximal ideal; they retain multiplicity without requiring an
invariant CI ideal. See the [constant fat-point envelope](full_transverse_chow_pullback_envelope.md)
and the [embedded quotient framework](../../frameworks/embedded-torus-quotients/index.md).
Cayley--Hamilton is available but not the starting point.

Projection from \(L=V(z,w)\) instead has rank \(4m\).
For the finite flat projection onto \([z:w]\), the characteristic
polynomial of multiplication by \(q\) on the generic fiber is \(P^4\).
The polynomial \(P\) itself annihilates the generic algebra, since
each local generic length is \(n_i\). Homogenizing and using
unmixedness gives \(H(xy,zw)\in(F,G)\).

The elementary motivation for trace is summing over a fiber:
on \(z=1\), \(t^4=w/v_i\), \(xy=q_iw\).
Thus \(\operatorname{Tr}(xy)=4zwM_1\). The residue identity is
the corresponding coefficient-extraction operation. For monic
\(f\) with distinct roots \(r_j\), Lagrange interpolation gives
\([t^{\deg f-1}](h\bmod f)=\sum_j h(r_j)/f'(r_j)\);
replacing \(h\) by \(hf'\) recovers the trace. The multivariable
finite-CI version is the standard Scheja--Storch/Grothendieck residue
pairing; see [spectral--Jacobian bridge](spectral_jacobian_first_jet_bridge.md).

The explicit degree-(2m,...,3m) quadric/cubic polar coefficients also
belong to the actual ideal. They constrain construction of the pair.
Use the [polarization proof](weighted_chow_quadric_cubic_polarizations.md)
with its [saturation correction](spectral_interpolation_and_polar_saturation.md):
the two opposite chains give the same dense-torus envelope, and their
syzygy containing \(M_1\) is not an independent obstruction.

## Product geometry and actual global sections

- [Complementary Chow projections and product models](transverse_chow_product_models.md)
  records the fixed quadric, the three Segre restrictions, common equation
  coordinates, and logarithmic differentials.
- [Quadric graph sections, endpoint residues, and global gluing](transverse_chow_quadric_graph_gluing.md)
  records degree exhaustion, the compact graph, corner sections, and
  centered and uncentered dualizing sections. The open comparison uses
  the actual two source equations at both ends.

## 6. Grassmannian sum pencil and return to equations

The [Grassmannian sum and conormal compatibility account](grassmannian_sum_and_conormal_compatibility.md) records the enlarged relative Grassmannian, the direct sum-pencil blowup (without resolving individual spectral pencils), the integral ambient finite fibers, collision relations, the intrinsic conormal graph and the compatible weighted q-form. It distinguishes graph incidence from a canonical lift of nilpotent Plücker data and records the scalar supplied by the actual cycle.

Work backwards geometrically, not by eliminating all structure to reach a single equation. Section 0 of the companion account interprets the orbit quotient, fixed fat-point envelope, moving transverse neighborhoods, the two normal geometries, compatible forms as functorial conormal maps, and the sum graph as the resolution of an observable. The weighted q-form follows from spectral ideal membership and Euler, but its geometric content is the factorization through the projected cycle divisor. The first-normal-jet pairing is an independent presentation of one observable, not the immediate objective of the realization program. No new UM1 coverage is asserted.

## 7. What to carry forward

* Use the existing reduced-cycle evaluation/moment-matrix criterion
  as the constructive model, and the canonical fat-point envelope
  for repeated components. Do not infer scheme structure from trace.
* Reconstruct each intrinsic construction in terms of its geometric objects, maps and forgotten information. Use coefficient relations to express the geometry, and distinguish automatic functorial compatibility from additional global realization information.
* Compare the common homogeneous equation presentation across the
  product models and the three Grassmannian restrictions. Boundary
  compactification is essential; arbitrary spectra occur on the torus.
* Treat the line-bundle/section viewpoint as a source of constructive
  requirements on the unknown pair, not an assertion that every
  compatible list of sections integrates to homogeneous gradients.
  Hartshorne--Serre gives the established subcanonical lci-to-rank-two
  bundle construction; a CI corresponds to a split bundle, and
  prescribing the cycle is weaker than prescribing an lci scheme.
* Use the first moment as one observable for comparing the constructions, not as the definition of progress. Neither centered regularity nor the spectral polynomial recurrences remove the scalar term. No universal first-moment vanishing is proved here.

The current proof boundary is maintained in
[universal first moment proof boundary](universal_first_moment_proof_boundary.md)
and the [corpus synthesis](universal_first_moment_corpus_review.md).
This synthesis records the geometric motivation and interfaces, not a
parallel proof of the established results or a replacement for the
existing open-problem priorities.

### Marked moduli continuation (provisional)

The [marked Chow configuration boundary](marked_chow_configuration_boundary.md) and [endpoint incidence systems](marked_chow_endpoint_incidence.md) record the continuation of the geometric program: distinguish the independent and diagonal Chow quotients, separate the marked longitudinal curves in an ambient family, and determine the boundary from the quotient pencils and the two endpoint linear systems before choosing blowups. The generic four-pencil blown-up surface has an ample log canonical divisor by the direct calculation there. The three- and four-marking tests explain why the cusp and moment hyperplane arise from opposite-endpoint incidence and why toric-vertex incidence is essential beyond delta ranks. The stable extension and source-sensitive compatibility for arbitrary nonreduced CIs remain open; no new UM1 coverage or change in global priorities is asserted.
