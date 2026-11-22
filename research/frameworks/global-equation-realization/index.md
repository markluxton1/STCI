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

**A complete fixed-carrier realization theorem takes precedence over the generic lifting discussion.** For an integral carrier \(X\subset\mathbf P^3\) regular at the generic point of the smooth curve \(C\), the [normalized Hodge/APic criterion](../../arguments/carriers/fixed_carrier_descent_and_cartier_models.md#the-normalized-hodge-matrix-and-downstairs-almost-cartier-indices) states that a sole-support mate exists exactly when the actual downstairs almost-Cartier index \(R_X\) is finite and the normalized strict transform has numerical square \(e^2/a\) (\(e=\deg C,a=\deg X\)). This includes nonnormal carriers and arbitrary characteristic. The exact minimum mate degree is \(eR_X/a\); all multiples occur by taking powers. The [normal-carrier extremal-ray theorem](../../arguments/carriers/normal_carrier_divisor_geometry.md#1-a-mate-is-equivalent-to-hodge-index-equality-on-a-normal-hypersurface) is its specialization. There is no separate homogeneous lifting gate once both conditions hold: the Cartier class is a hyperplane multiple and its section lifts. The new broader deduction awaits independent review. A prescribed pair degree still has to satisfy the exact semigroup.

**Normality is a property of the actual generator system.** For a sole-supported pair \((a,b)\), \(a\le b\), the [all-degree Bertini--Serre replacement](../../arguments/carriers/normal_carrier_divisor_geometry.md#47-unequal-degree-pairs-can-acquire-an-actual-normal-carrier) gives a general normal integral \(K_b=\lambda G_b+F_aL_{b-a}\), \(\lambda\ne0\), defining precisely the same ideal together with \(F_a\) if and only if at least one generator has generic order one. In equal degrees both general generators can be chosen normal. This is an actual homogeneous source statement, not a claim that formal structures lift. On the resulting **fixed** normal carrier the Hodge-index equality is sufficient for a mate; do not impose a second independent global lifting test there. Finding a carrier reaching equality with the required defects is the realization problem. For genuinely thick generic CI algebras, no such degree-compatible normal replacement exists, and the full two-generator source test remains essential. The theorem is degree independent and pending independent audit. 

For **upstairs-only** nonnormal data, finite normalization indices
and divisor relations do not establish finite downstairs almost-Cartier
index. Conductor gluing and full inverse support remain essential
computations of the missing condition. For generically thick carriers
the full supported-section descent problem remains separate.
The [extended all-index-at-most-four exclusion](../../arguments/carriers/normal_carrier_symbolic_torsion.md#normality-is-unnecessary-the-actual-almost-cartier-power-theorem)
works before fixed-degree source computations on every generically regular
integral carrier in characteristic zero, subject to independent audit.
The relevant index is downstairs, not upstairs.

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

The [full Chow-polytope rigidity theorem](../../arguments/equations/chow_polytope_rigidity.md) classifies effective one-cycles whose full, unshifted column-weight polytope equals a multiple of that of the fixed quartic, in every characteristic: they are sums of diagonal translates of the quartic. This controls cycle support types only. It neither forces those translates to coincide nor constructs a scheme or a pair with the prescribed Sylvester determinant. The
[quartic realization theorem](../../results/quartic_chow_pencil_classification.md)
adds genuine **non-invariant** equation-pair fibers over fixed Chow
cycles and full flat limits whose endpoint embedded structure is
not recorded by Chow. Its
[Hilbert--Burch first-normal criterion](../../arguments/torus/quartic_chow_pencils.md#hilbert--burch-and-first-normal-interpretation)
keeps actual source data. The
[canonical self-linkage quotient](../../arguments/torus/quartic_chow_pencils.md#self-linkage-and-the-canonical-conormal-quotient)
identifies \(I_Y/I_Z\simeq\omega_Y(-4)\), with the
degree-three source map an isomorphism and the
degree-four kernel the defining pencil. A general Ferrand doubling need not have
two quartic generators. **For this fixed union**, however,
[linkage and canonical-module rigidity](../../arguments/torus/quartic_chow_pencils.md#proof-route)
combine the actual equation space with the canonical
module relations and a residual-line restriction
to prove that all proper quartic pencils are the
exceptional \(\lambda\)-family. This completes the
previously unresolved geometric uniqueness step,
not a general-degree STCI theorem. A
[fixed-carrier multiplicity lattice](../../arguments/torus/fixed_surface_restriction_lifts.md#symmetry-and-the-multiplicity-lattice)
can turn existing mates into new mates, but a corrected sextic
involution bound excludes \((5,4)\) and every remaining unequal
two-support partition on ordinary nodal sextic carriers.
Read backwards, the same fixed-carrier
lattice theorem
[turns the quartic all-mate exclusion into
rank-one multiplicity rigidity](../../arguments/torus/fixed_surface_restriction_lifts.md#reverse-application-single-curve-exclusions-constrain-multi-curve-chow-cycles)
for any two projective translates
on an integral quartic carrier.
Prime cyclic orbits of translates
are forced to have **equal**
multiplicities in every supported
mate cycle. The generic normal
order-one hypothesis needed by
the rational-product theorem is
automatic on such an integral
quartic by restriction to each
translate's unique quadric.
This connects individual STCI
exclusions to Chow **multi-support**
realization without asserting that
such a carrier exists.

Conditional ADE classes and an exceptional-lattice budget refine
the geometry; none covers arbitrary higher-degree equations.

- Restriction of an actual orbit presentation to the two completed endpoints preserves the parameter-annihilation order of each homogeneous torsion class. A class can nevertheless become divisible by the parameter there. This explains how endpoint computations can miss global equation relations even with the correct degree and parameter. [Endpoint detection and its first-layer kernel](../../results/endpoint_equation_torsion.md).
- For a characteristic-zero sole-support pair of degrees \(a\le b\), every nonzero weight component of the smaller equation has surviving powers through \(\lfloor b/a\rfloor\). Their multiplication ranks bound the splitting of the moving quotient. This tests the degrees of actual homogeneous generators even when a proposed image has the prescribed CI polynomial. [Power and splitting bounds](../../results/torus_quotient_movement_bounds.md#proof).
- Actual source spaces at fixed degree and normal order and their successive lifting quotients are computed in [global equation jets](../../arguments/equations/global_equation_jets.md). They show why independently selected sections of \(\mathrm{Sym}^r(I/I^2)\) need not come from equations. Finite compatible-jet existence is not an effective bound on all degrees: no general all-degree cutoff is established from a rank plateau or a finite truncation.
- The [octic/root comparison](../../arguments/spectral/actual_octic_root_lift_comparison.md) has an actual source map and a proper pair of transverse length eight with residual degree 32. This illustrates compatibility without sole support, not a solution to the unrestricted question.
- [Projected thickenings](../../arguments/linkage/projected_thickening_section_defects.md) distinguish an ACM source upstairs from its image in \(\mathbf P^3\): the displayed power and binary-mixture images fail ACM when the positive degree product is nonzero. This does not exclude other projected sources or arbitrary supported thickenings.

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

[R-0079](../../results/quartic_chow_pencil_classification.md) gives
actual defining equations for every geometric pencil in the
\((4,4)\) Chow-polytope fiber **in characteristic zero**.
The characteristic-two specialization is a separate construction,
not an extension of this uniqueness theorem. In every degree the
[trace tower](../../arguments/torus/chow_trace_cone_jets.md#a-sole-support-test-at-an-arbitrary-disjoint-line)
excludes sole support if just one actual generator has a cone jet
through degree four along a disjoint line. The coverage question is
whether further equation constraints force this or another usable
trace identity without a cone hypothesis.

On a fixed, generically regular carrier, the
[multiplicity comparison](../../arguments/torus/fixed_surface_restriction_lifts.md#comparing-multiplicities-on-one-fixed-carrier)
realizes nonnegative integer combinations of actual supported section
cycles by clearing their codimension-one denominators. The two-support
sextic criterion identifies one family in which the carrier symmetry
would supply the needed sections.

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

The [marked finite-index multiplication gate MJ1--MJ4](../../arguments/residuals/blowup_residual_geometry.md#finite-index-rigidity-of-higher-marked-jets)
adds a necessary local test for the primitive-at-marked-point
edge: the prescribed colength must be attained by an
**algebra**, not just a rank-\(c\) lattice. Multiplication
closure reduces to \(q+h\) border products, and for
\(q\ge3\) forces the first base-direction jet to be
linear in the normal parameter modulo its \(q\)-th
power. The endpoint test line yields a specific
second-base-jet coefficient when \(q\ge4\).
These are testable in the *actual* \(V_5\)
section spaces. They do not identify the
remaining nonprimitive mixed or endpoint
realization loci.

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

The [residual-corrected transfer](../../arguments/residuals/blowup_residual_geometry.md#signed-finite-transfer-throughout-the-interior-equality-boundary) identifies the signed top defect on the image quintic even when the actual image intersection includes the conic. Its [local canonical ideal formulation](../../arguments/residuals/blowup_residual_geometry.md#local-canonical-ideal-version-and-several-marked-points) identifies a colon ideal, not merely a genus correction. Neither substitutes for actual common-support realization in the section spaces.

## Coregularity and actual equation filtrations

The [local-cohomology interface](../local-cohomology/index.md#simultaneous-coregularity-versus-geometric-defects)
asks whether full actual equation filtrations detect failure of the
second-element coregularity condition. The pairwise cokernel is
\(H_I^1(S/(f,g))(\deg f)\) under the stated first-coregularity and
vanishing hypotheses. The [actual full-primary attachment quotient comparison](../../arguments/local-cohomology/actual_pair_coregularity.md#actual-attachment-equation-modules-are-the-dual-annihilator-layers) gives its local annihilator layers by canonical duality. The open step is to force their nonvanishing from actual homogeneous equations, or identify a specific filtered lifting obstruction with an attachment quotient. A finite conductor module already supported on \(C\) has zero higher local cohomology and cannot alone supply that argument.
