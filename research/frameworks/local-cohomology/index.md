---
id: STCI-F-0009
type: framework
title: Local cohomology and simultaneous ancestors
status: in_use
scope: "#scope"
bridges: "#bridges"
---
# Local cohomology and simultaneous ancestors

## Scope

For \(S=k[x,y,z,w]\), \(I=I_{C_0}\), and \(M=H_I^2(S)\), multiplication
in \(M\) retains normal principal parts that are invisible to the reduced
curve. The [local cohomology and conormal account](../../arguments/local-cohomology/local_cohomology_conormal_geometry.md)
relates this module to transverse jets. One obstruction strategy would
show that \(M\), in characteristic zero, is not quasi-cyclic; the
[literature on Hellus–Hübl](../../literature/README.md#hellus--hübl-2016)
gives the context for using two global equations in this comparison.
One can also ask a bounded question about two specified socle targets
and actual multipliers of a fixed degree.

In the fixed quartic multiplier problem, the
[finite direction reduction](../../results/quartic_ancestor_direction_reduction.md)
uses a quadratic moment of the common normal direction together with the
full actual multiplication tensor. It excludes primitive directions of
degrees zero and two and the linear endpoint boundary. The surviving
directions lie on a line and a degree-twelve curve; solving the top
coefficient condition on them leaves two distinct lower target equations
and ambient coprimality. The
[full two-target question](open_quartic_ancestors.md) gives the
normalization, the exact remaining conditions, and the independent
all-stage and endpoint controls.

## Mathematical scope and interfaces

The [finite direction reduction](../../results/quartic_ancestor_direction_reduction.md)
applies to the specified quartic test; the
[two-target equations](open_quartic_ancestors.md) remain unresolved.
The [polynomial-dual argument](../../arguments/local-cohomology/polynomial_duals_and_affine_pencils.md)
and [all-stage obstructions](../../arguments/local-cohomology/local_cohomology_ancestor_obstructions.md)
apply to their stated families, not arbitrary multipliers.
[Formal normal geometry](../formal-normal-geometry/index.md) shares
normal directions, filtrations, and embedded-structure questions;
[residual construction](../residual-construction/index.md) provides a
complementary geometric interpretation when actual multipliers give
proper pairs. The formulations are related without being equivalent.

### The quartic ancestor remainder leaves translated-cycle incidence

A proper positive answer in the bounded quartic common-ancestor source
has marked generic length three and residual degree four, by its
[owning source calculation](../../arguments/local-cohomology/direction_and_apolarity.md).
That residual cannot be a translated quartic: otherwise the entire
\((4,4)\) cycle would have partition \((3,1)\), excluded by the
[quartic-pencil classification](../../results/quartic_chow_pencil_classification.md).
Thus the new full-translated-cycle moment and sign-source theorems do not
directly test this remainder. Its relative-extension and multiplication
tensor question retains independent content; this is a coverage separation,
not a new vanishing theorem for the ancestor module.

## Bridges

Work on the two surviving interior components in the actual equation
tensor. Preserve the full kernel of top-and-quadratic data because different
kernel vectors can admit different lower corrections. The
[polynomial-dual technique](../../arguments/local-cohomology/polynomial_duals_and_affine_pencils.md)
and the [all-stage examples](../../arguments/local-cohomology/local_cohomology_ancestor_obstructions.md)
give mechanisms for excluding declared families while retaining all
allowed lifts. A higher-degree multiplier brings different source and
principal-part spaces; the fixed quartic test cannot supply full-module
coverage.

A common ancestor and an embedded thickening are different realizations.
Even a positive quartic ancestor answer has a residual consequence: the
[generic-length calculation](../../arguments/local-cohomology/direction_and_apolarity.md#2026-10-05-localcoh-generic-length)
gives a residual cycle of degree four for any such pair. The characteristic-zero quartic carrier theorem does not answer
this fixed two-target question.

### Does the conductor quotient retain the two targets?

For an actual supported CI in the separated quadratic cover, the
[conductor contains the relative socle](../../arguments/linkage/endpoint_lattice_capacity.md#fixed-local-cohomology-targets-and-what-they-cannot-see). Thus the two fixed socle targets become zero in the conductor quotient; it cannot supply the separating covector directly. A transport must keep the full multiplication image and the actual target values, for example through the degree-and-contact shift, rather than identify the targets with conductor classes. The first five added multiplier directions on the quartic shift still need to be evaluated.

For a full primary triple with generic curvilinearity the [BF triple and actual-pair attachment TR1--TR4](../../arguments/residuals/layerwise_attachment_and_triples.md#triples-the-full-attachment-has-only-two-independent-divisors) shows its actual first attachment quotient has length divisor \(D_2+\eta\), where \(D_2\) is exactly the conormal-torsion divisor and \(\eta\) the determinant divisor of the two actual equations. LC-A1 identifies the dual of this module with the first local annihilator layer of the actual intersection local cohomology. This is a concrete reconciliation of intrinsic and actual-equation defects, subject to the Hartshorne--Polini first-coregularity condition when interpreting it as a second-element obstruction. It does not prove the first quotient is nonzero in all homogeneous degree pairs.

## Simultaneous coregularity versus geometric defects

Put \(S=k[x_0,x_1,x_2,x_3]\), \(I=I_C\), and \(M=H_I^2(S)\).
For a homogeneous regular pair \(f,g\in I\), Hartshorne–Polini's
[criterion and higher-vanishing hypotheses](../../arguments/equations/global_equations_and_constructions.md#homogeneous-local-cohomology-and-the-second-equation)
identify sole support with ordered simultaneous coregularity:
\[
 fM=M,\qquad g(0:_M f)=0:_M f.
\]
Once \(fM=M\), put \(K_f=0:_M f\). The second condition is exactly
\(\mathcal D(f,g):=K_f/gK_f=0\). This quotient need not be
finite-dimensional. Under \(H_I^1(S)=H_I^3(S)=0\), the
[actual-pair calculation](../../arguments/local-cohomology/actual_pair_coregularity.md)
identifies it with \(H_I^1(S/(f,g))(\deg f)\): functions on the
residual complement that fail to extend. Finite modules supported on
the cone over \(C\) have zero higher \(I\)-local cohomology. Applying
that functor to a conductor already supported there cannot alone give a
nonzero detector.

Without first-element coregularity, the same calculation gives an exact
sequence with \(\mathcal D(f,g)(-\deg f)\) as submodule of
\(H_I^1(S/(f,g))\) and quotient
\((0:_{M/fM}g)(-\deg g)\). It isolates the contribution removed
by the first-coregularity hypothesis without identifying either term
with a finite conductor module.

For the actual full-primary ideal \(J\) of a proper pair with ideal
\(L=(f,g)\), the
[attachment equation quotients](../../arguments/local-cohomology/actual_pair_coregularity.md#actual-attachment-equation-modules-are-the-dual-annihilator-layers)
\(Q_n=J/(L+I^nJ)\) identify, with the adjunction twist and at
projective attachment points, the Matlis duals of the \(I^n\)-annihilator
layers of the actual-CI local cohomology. The first layer detects residual
attachment, and connectedness gives the global vanishing equivalence for
actual proper pairs. Under first-element coregularity this detects the
second condition. The linked proof retains its own review scope. It
does not identify the entire graded module at the cone vertex or
arbitrary intrinsic filtered lifting defects with \(Q_n\). In fact
[local controls](../../arguments/normal-geometry/source_specialization_and_linkage.md#normal-cancellation-is-not-actual-residual-attachment)
separate the vanishing of normal cancellation \(\Delta\) and of
\(Q_1\) in both directions. The remaining question is which actual
homogeneous-source or geometric constraints force \(Q_1\ne0\),
rather than an unrestricted local identification of these modules.
The bounded common-ancestor calculations do not prove nonvanishing for
all pairs or non-quasi-cyclicity of \(M\); failure for one ordered pair
does not exclude all coregular pairs. The existing individually-coregular
counterexample in the linked proof account explains why the pairwise
condition matters.

### Section parity and actual-family specialization

The finite section/Rao defect required by a nonzero first moment on an
invariant pure hull is a different cohomology module. The reduced quartic
has nonzero section defect \(kh\), but
\(H_I^1(S/I)=0\), since \(I\) annihilates its coordinate ring.
Conversely a projective CI has zero Rao module while a genuine residual
attachment gives nonzero relative local cohomology. The
[support controls](../../arguments/normal-geometry/source_specialization_and_linkage.md#section-parity-and-relative-coregularity-have-different-supports)
exclude substituting one detector for the other.

There is nevertheless an exact actual-family comparison. For a flat
graded family \(A\) over a parameter DVR and its special pure quotient
\(0\to T\to A_0\to E\to0\), the
[section-specialization sequences](../../arguments/normal-geometry/source_specialization_and_linkage.md#sections-after-the-pure-hull-correction)
express the finite \(H^1_{(z,w)}(E)\) as a quotient of
\(H^1_{(z,w)}(A_0)\), corrected by \(H^1_{(z,w)}(T)\), and relate
that middle module to the family cohomology and its parameter torsion.
The removed projective embedded structure \(T\) can have dimension one
over \(k[z,w]\), despite the finite length of the final Rao defect.
Parameter-character twists must be retained in weighted equivariant
families. These sequences locate the required parity class in actual
family sources without proving that it cannot survive. They complement
the relative attachment and common-ancestor questions, rather than
answering them.
