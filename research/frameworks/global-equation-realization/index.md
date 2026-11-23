---
id: STCI-F-0006
type: framework
title: Global equation realization for supported intersections
status: proposed
scope: "#scope"
bridges: "#bridges"
relations:
  - kind: uses
    from: [STCI-R-0076, STCI-R-0077, STCI-R-0078]
    to: [STCI-F-0006]
    at: "#bridges"
---
# Global equation realization for supported intersections

## Scope

For the fixed embedded quartic \(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\), organize what it takes for two *actual homogeneous forms* to have a prescribed supported intersection. The characteristic-zero STCI question remains open in unrestricted degree. A local multiple structure, normal symbol, cycle, Chow equation, complement pencil, or abstract bundle section retains only part of a global pair. The [global equations account](../../arguments/equations/global_equations_and_constructions.md) gives the geometric mechanisms; the [actual equation-jet filtration](../../arguments/equations/global_equation_jets.md) tracks their source maps.

For a proper pair of degrees \((a,b)\), the cycle identity \(ab=4m_{C_0}+\deg R\) makes \(m_{C_0}=ab/4\) equivalent to sole support. This is an exact existence reformulation, not an independent multiplicity bound. A viable obstruction must supply a structural restriction on **arbitrary actual pairs**, beyond the classical intersection formula or a change of parameter space.

The fundamental object is the labelled map
\(\mathcal O_{\mathbf P^3}(-a)\oplus\mathcal O_{\mathbf P^3}(-b)\to I_{C_0}\)
whose components are the equations. Its image must define a proper complete intersection and have no residual support if the goal is STCI. The [Sylvester Hom identity](../../arguments/equations/chow_bundle_maps.md#the-prescribed-sylvester-bundles-already-retain-the-equations) recovers forms directly from a map of the prescribed bundles; the required nonzero Chow-power determinant is still an existence condition. The [complement calculation](../../arguments/equations/complement_section_obstructions.md) distinguishes the checked continuous and primary algebraic conditions from actual homogeneous section realization. The [Chow/bundle and complement criteria](../../arguments/equations/global_equations_and_constructions.md#geometric-orientation-the-locus-of-globally-presented-multiple-curves) are equivalent formulations or necessary shadows only when their stated hypotheses hold; a cycle identity or a section on the complement does not by itself provide homogeneous lifts with the required base locus.

## Interfaces

[Formal normal geometry](../formal-normal-geometry/index.md) concerns local
compatibility; [carrier normalization](../carrier-normalization/index.md)
requires full inverse support and conductor descent; and
[residual construction](../residual-construction/index.md) tracks residual
cycles. None alone supplies a proper homogeneous pair with sole support.
[Projection and liaison](projection_and_liaison.md) studies supported ACM
sources and section defects.

Two distinct equation questions survive passage to a thickening. The
[radical-power lemma](../../arguments/torus/equivariant_set_theoretic_descent.md)
preserves the least number of set-theoretic homogeneous equations inside
any same-radical ideal, while it gives no bound on their degrees and does
not generate that ideal. For an unequal-degree search, the
[actual pair quotient](../../arguments/torus/equation_pair_rank_and_weights.md)
removes the redundant replacement \(G\mapsto G+HF\). Its bundle dimension
and weight data describe available equations; properness, higher contact
and terminal support remain conditions on those equations.

## Available mathematics and controls

The [full Chow-polytope rigidity theorem](../../arguments/equations/chow_polytope_rigidity.md) classifies effective one-cycles whose full, unshifted column-weight polytope equals a multiple of that of the fixed quartic, in every characteristic: they are sums of diagonal translates of the quartic. This controls cycle support types only. It neither forces those translates to coincide nor constructs a scheme or a pair with the prescribed Sylvester determinant.

- Restriction of an actual orbit presentation to the two completed endpoints preserves the parameter-annihilation order of each homogeneous torsion class. A class can nevertheless become divisible by the parameter there. This explains how endpoint computations can miss global equation relations even with the correct degree and parameter. [Endpoint detection and its first-layer kernel](../../results/endpoint_equation_torsion.md).
- For a characteristic-zero sole-support pair of degrees \(a\le b\), every nonzero weight component of the smaller equation has surviving powers through \(\lfloor b/a\rfloor\). Their multiplication ranks bound the splitting of the moving quotient. This tests the degrees of actual homogeneous generators even when a proposed image has the prescribed CI polynomial. [Power and splitting bounds](../../results/torus_quotient_movement_bounds.md#proof).
- Actual source spaces at fixed degree and normal order and their successive lifting quotients are computed in [global equation jets](../../arguments/equations/global_equation_jets.md). They show why independently selected sections of \(\mathrm{Sym}^r(I/I^2)\) need not come from equations. Finite compatible-jet existence is not an effective bound on all degrees: no general all-degree cutoff is established from a rank plateau or a finite truncation.
- The [octic/root comparison](../../arguments/spectral/actual_octic_root_lift_comparison.md) has an actual source map and a proper pair of transverse length eight with residual degree 32. This illustrates compatibility without sole support, not a solution to the unrestricted question.
- [Projected thickenings](../../arguments/linkage/projected_thickening_section_defects.md) distinguish an ACM source upstairs from its image in \(\mathbf P^3\): the displayed power and binary-mixture images fail ACM when the positive degree product is nonzero. This does not exclude other projected sources or arbitrary supported thickenings.

### Spectral–Jacobian first-jet gate (PR #173; review pending)

For any **actual proper pair** with whole translated quartic cycle,
[spectral–Jacobian duality](../../arguments/torus/spectral_jacobian_first_jet_bridge.md)
proves \(A M_{12}-2B M_{03}\in(F,G)\), where
\(A=x_1x_2\), \(B=x_0x_3\). Together with the canonical spectral
membership \(H(A,B)\in(F,G)\), this gives a **converse recognition test**
for translated reduced support, provided the pair misses the
canonically disjoint line \(V(x_0,x_3)\).
Its first moment is \(M_1=\tfrac12\operatorname{Res}_{f_0,g_0}(ps-qr)\),
an alternating perfect Gorenstein pairing of the actual first normal
jets of the equations along that line. The universal obstruction is
now the assertion that the image of the **joint complete spectral-
Jacobian equation incidence** has isotropic first jets. No such
isotropy theorem is established; a proper pair merely containing
\(C\) can have nonzero pairing and residual degree twelve.

### Sole-support jet requirement and why it does not suffice

For a hypothetical characteristic-zero STCI,
[the accepted Poisson identity restricted to the disjoint line](../../arguments/torus/sole_support_first_jet_gate.md)
forces the first normal jets to have **nonzero**
Macaulay/Serre symplectic pairing \(\Omega=ab/2\).
This congruence occupies the one-dimensional socle
of \(k[x_1,x_2]/(f_0,g_0)\). An explicit family of
proper global containing pairs realizes that pairing
for every \(a,b\ge4\) and has a residual curve,
so the scalar by itself cannot exclude STCI.

The scheme-theoretic power condition \(Q^m\in(F,G)\)
is tautological after truncation by the disjoint
line's \(r_*=(a-2)(b-2)/2\)-th ideal power,
by the graded free fiber-basis bound. In bidegree
\((6,6)\), the first potentially restrictive
normal coefficient is order eight, not order one
or two. Higher-order global compatibility can still
constrain the first jets indirectly; no complete
jet realization criterion is claimed.

### First power obstruction as a homogeneous spectral coefficient map

The [STCI jet gate](../../arguments/torus/sole_support_first_jet_gate.md)
identifies a canonical leading obstruction to
\(Q^m\in(F,G)\) for a hypothetical sole-support
pair: a binary form
\(\mathfrak o_{r_*}\) in
\(H^1(L,\omega_L)\otimes
\operatorname{Sym}^{r_*}\langle x_0,x_3\rangle\),
where \(r_*=(a-2)(b-2)/2\) and
\(L=V(x_0,x_3)\).
It is the first nonautomatic normal-degree
part of the class \([Q^m]\) in the actual
CI algebra. The same construction gives a
**linear map on every full homogeneous
spectral form** \(H(A,B)\) of degree \(m\);
realized translated arrangements must put
their spectrum in its kernel.
For the restricted quartic test family
the first power class requires
\(\lambda\mu=4\), incompatible with the
sole-support Poisson requirement
\(\lambda\mu=8\). This locates a real
interaction between the two equations
without promoting the family check
into a general low-degree exclusion.

### Complete residue detection of set-theoretic support

The [exact power/residue criterion](../../arguments/torus/sole_support_first_jet_gate.md#full-exact-stci-jet-criterion-ideal-powers-and-the-perfect-residue-pairing)
uses the accepted
\(I_C^m\subset(F,G)\) bound
for an actual supported CI.
For a proper pair \(F,G\in I_C\),
the converse holds, so STCI
is equivalent to this ideal-power
membership. The ideal
\(I_C=(Q,U,W,V)\) has one
quadric and three cubic
generators. Its \(m\)th ordinary
power has explicit monomial
generators; perfect finite flat
Gorenstein duality reduces their
membership to finitely many
relative residue vanishings
\(\mathcal R_{F,G}(g e)=0\),
for every generator \(g\)
and every element \(e\) of a
graded \(k[x_0,x_3]\)-basis
of the **actual** CI algebra.
This gives a precise necessary
**and sufficient** coefficient
gate for each bidegree, without
selecting a carrier.
The scalar first-jet condition,
the first spectral-power
residue and the first
normal-jet pairing are
only partial rows of this
full perfect pairing; explicit
quartics pass them and have
residual support.
The algebraic elimination of
actual equation coefficients
to obtain an all-degree
contradiction remains open.

### Two opposite full-Chow coefficient systems as actual equation constraints

The [canonical full-Chow pullback envelope](../../arguments/torus/full_transverse_chow_pullback_envelope.md)
takes the *entire paired* transverse Chow
form \(\mathcal C_\sigma\), not just its
ratio-spectrum. The degree-four
weight-four torus-quotient sections
\((D,P,R)=(x_1^4,x_0^2x_1x_2,
x_0^3x_3)\), and their reversed
weight-twelve counterparts, yield
\(2(m+1)\) explicit degree-\(4m\)
polynomials **in every proper
CI ideal realizing** \(\sigma\).
Their two coefficient ideals coincide
with \(\cap_i I_{C_i}^{n_i}\)
on the dense torus; their sum has
radical the exact union of translated
quartics, with no extra coordinate
curve. The inclusion is a **necessary
all-degree source condition** retaining
the full pairing of transverse
parameters; for reduced cycles and
\(ab=4m\), it is also sufficient
for degree exhaustion. For repeated
cycles the full local lengths
\(n_i\) remain essential.

The coefficient algebra is the
constant normal-fat-point ring
of length
\(N=\sum_i\binom{n_i+1}{2}\).
Every actual CI selects a moving
flat quotient of rank \(m\),
with kernel rank
\(\delta=\sum_i\binom{n_i}{2}\).
The norm of \(X+uY+vZ\) in that
quotient is exactly
\(\mathcal C_\sigma\), and the
trace of \(u/v\) is \(M_1\).
This accounts for the already
proved invariant reduced case
(\(\delta=0\)), and isolates the
nonreduced moving-quotient and
two-endpoint gluing gap.
It does **not** prove universal
moment vanishing, a uniform
degree cutoff, or that the
necessary source inclusions
admit a two-generator
proper quotient.

### Sharper full-paired Chow constraints from quadratic and cubic surfaces

The [opposite (2,3) Chow polarizations](../../arguments/torus/weighted_chow_quadric_cubic_polarizations.md) replace the earlier raw degree-\(ab=4m\) full-Chow equations by **\(2m+1\) homogeneous equation constraints in degrees \(2m\) through \(3m\)**. The shared lowest term is the actual quadric-spectrum polynomial \(H_\sigma\); the two opposite chains come from cubic carriers with residual divisors \(2L_{01}\) and \(2L_{23}\) on the respective smooth quadrics. Their combined coefficient ideal has exactly the prescribed translated reduced support, and recovers the same canonical fat-point envelope on the dense torus.

The first normalized polars satisfy
\[
 x_2^2E_++x_0^2E_-+
 x_1H_\sigma(m x_1x_2+M_1x_0x_3)=0.
\]
This is a **specific cross-polar source syzygy** for every whole translated-cycle CI (and every abstract cycle), so a proposed proof of UM1 must extract an *additional two-generator global cofactor constraint* rather than divide the common factor \(H_\sigma\) in the CI ring. No new universal vanishing, proper-pair degree bound, or nonexistence theorem is asserted.

## Bridges

An osculating quadric puts the entire quadratic conductor at one general
point. Its principal parts map takes actual degree-\(d\) polynomials
to a finite transverse jet space and computes their boundary kernel.
For a proposed pair this kernel must consist of multiples of the
smaller integral equation when \(2d+2<b\).
[One-point homogeneous test](../../results/moving_quadratic_conductors.md).

For degrees \((3p,4q)\) and exact normal orders \((p,q)\), connectedness
reduces the characteristic-zero equation question to either of two
marked rational quintics on \(V_5\). A proper pair of divisors of
classes \(pM,2qM\) must have the prescribed conic orders, meet on the
chosen quintic alone, and retain a nonzero order-\(q\) symbol at its
one conic contact. These conditions, with the exact-order hypotheses
in the proof, also recover a defining pair in \(\mathbf P^3\).
[Section and conic-fiber criterion](../../arguments/residuals/blowup_residual_geometry.md#actual-equations-on-the-zero-direction-edge).

For the explicit elliptic double-cover family, a candidate consists of
a smooth basepoint-free fiber mapping birationally onto an octic.
First, its length-twelve residual zero scheme must be supported on the
marked elliptic curve. Then, for some \(b>0\), one must express
\(Q_0^b\) as a degree-\(b\) polynomial in the four projection sections
in the coordinate ring of that fiber. The polynomial and the implicit
octic would cut out the fixed quartic set-theoretically. The completed
characteristic-zero line fails at the support step. [Support theorem](../../results/elliptic_inverse_support.md) ·
[Descent equation (8)](../../arguments/carriers/elliptic_double_inverse_construction.md#5-fiberwise-support-and-actual-descending-equations) ·
[Tested line](../../investigations/stci-equation-search/index.md#findings)

The unresolved implication is from compatible local/normalized data to two homogeneous sections whose full intersection is supported exactly on \(C_0\). A viable bridge must identify the actual source spaces, lift every required jet through their quotient maps, handle base points and conductor gluing, and then prove properness and eliminate residual components. Conversely, a universal obstruction must cover all equation degrees; the existing fixed-degree calculations and actual jets do not supply an effective all-degree bound.

For witness bounds and fixed-degree tests, see [exact finite certificates](../../arguments/equations/bounded_equation_certificates.md). A separate question asks how an actual equation obstruction changes as the [embedding varies](bounded_equation_search.md). Use [projection and liaison](projection_and_liaison.md) for the companion construction interface. The shared literature records the hypotheses for
[Chow and determinantal representations](../../literature/README.md#chow-forms-and-global-determinant-representations)
and for [affine results and the projective gap](../../literature/README.md#affine-lci-theorems-and-the-projective-gap).

The canonical [R-0074](../../results/chow_polytope_rigidity.md) classifies **all** effective cycles in this rigid Chow-polytope fiber; invariance is deduced, not assumed. Its [proper-pair reformulation](../../arguments/equations/chow_polytope_rigidity.md#proper-surface-pairs-and-the-remaining-equation-question) is a classical resultant coefficient condition, not a criterion in the Newton polytopes of the equations alone. The [R-0050 integration](../../arguments/equations/chow_polytope_rigidity.md#eigenpairs-and-transverse-finite-quotients) keeps boundary exclusion and binomial-only subgroup structure explicit.

The [H16 cycle parameterization](../../arguments/equations/chow_polytope_rigidity.md#set-level-symmetric-power-fiber-h16) is set-theoretic and supplies neither homogeneous equations nor scheme structure. The [proof-dependency inventory](../../investigations/proof-audit/README.md) separates essential computations from evidence, and records the geometric R-0024 rank replacement.

The [clean common-quadric boundary](../../arguments/equations/common_quadric_chow_boundary.md)
determines the full special scheme in every degree \(a,b\ge3\), for
any smooth \((1,3)\) curve and in every characteristic, under coprime
cofactors and nonzero first cancellation on \(Q\). Regular
cofactor restrictions give a residual source of dimension
\(a(a-2)+b(b-2)\). More generally, write nonzero restrictions as
\(\alpha=h\alpha'\), \(\beta=h\beta'\), with the common divisor
\(h\) of class \((h_1,h_2)\), and put \(Z'=V_Q(\alpha',\beta')\).
The [normal cancellation calculation](../../arguments/equations/common_quadric_chow_boundary.md#normal-cancellation-at-restriction-rank-drops)
gives kernel dimension \((h_1+2)h_2\) and exact image
\[
 h\,H^0\!\left(Q,\mathcal I_{Z'/Q}
            (a+b-3-h_1,a+b-5-h_2)\right).
\]
For \(h_2=0\), including regular restrictions and common trisecant
ruling factors, the
[ordinary-blowup theorem](../../arguments/equations/common_quadric_resultant_blowup.md)
identifies the coefficient base ideal as the square of the center ideal,
and the whole local graph as the ordinary blowup. These center points are
outside the closure of fixed-degree sole-support pairs, even for arcs with
higher contact with the center. If \(h_2>0\), the coefficient ideal
is not that square; its graph and deeper cancellation remain unresolved.
Zero restrictions, common ambient cofactors and other global resultant
strata also remain outside this graph classification.
The balanced effective quadric subcycle rules out constant sole support
throughout the broader special-ideal scope, including restriction rank
drops. For the fixed monomial quartic it also rules out exact
Chow-polytope membership. This does not decide the closure of varying
translate arrangements.

[H17](../../arguments/torus/boundary_reconstruction_and_defects.md) gives a linear obstruction and torsor for lifting labeled boundary equations through C, a separate torus-support defect, and bounded-degree embedded CI reconstruction. Compatibility of lifts is not sole-support realization; the finite-order counterexample does not apply to all marked filtrations or fixed-degree full formal data.

The [H17 fixed-degree realization criterion](../../arguments/torus/boundary_reconstruction_and_defects.md#exact-fixed-degree-realization-of-embedded-facet-schemes) reduces a specified compatible embedded facet diagram to finite homogeneous polynomial feasibility using an ordinary power of I_C. It is an exact criterion, not a proof of automatic existence or an efficient all-degree search.

The [translate and fixed-surface interface](../../arguments/torus/fixed_surface_restriction_lifts.md)
expresses containment by arbitrary forms as coefficient evaluation at the
chosen \((u,v)\), with joint transverse lengths retaining multiplicities.
Restricted syzygies recover the abstract first annihilator of the surface
equation; its embedded normal extensions remain necessary. On the toric
quartic, a hypothetical characteristic-zero sole-support \(C_0\) pair of degrees \(a\le b\)
can contain a power \(A^N\) only with \(4N>b\). No upper bound meeting
that threshold, or automatic extension of scalar semigroup descent to
the relation module, is established.

### What the equality-boundary correspondence leaves to realization

The [actual marked section spaces](../../arguments/residuals/blowup_residual_geometry.md#the-marked-correspondence-on-the-whole-equality-boundary)
on (V_5) give a fixed geometric incidence question in each allowed
bidegree. An appropriate conic resultant is necessary but does not
realize a proper pair: the common support off the conic and absence
of a whole marked fiber must still be tested in the *same* section
spaces. Neither a formal contact lift nor a separate choice of
boundary data supplies that pair. An endpoint and an interior slope
are distinct tests; a result on either should say which realization
condition it actually decides.

## Coregularity and actual equation filtrations

The [local-cohomology interface](../local-cohomology/index.md#simultaneous-coregularity-versus-geometric-defects)
asks whether full actual equation filtrations detect failure of the
second-element coregularity condition. The pairwise cokernel is
\(H_I^1(S/(f,g))(\deg f)\) under the stated first-coregularity and
vanishing hypotheses. A comparison from the full filtered equation module
to this actual-intersection module remains open; a finite conductor module
already supported on \(C\) has zero higher local cohomology and cannot
alone supply that comparison.
