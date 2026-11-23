# Chow quotient, arrangement blow-ups, and the \(V_5\) bridge

**Type:** investigation / cross-framework mathematical synthesis.  
**Status:** explicit quotient fan, normalized toric graph fan with two endpoint sections, and endpoint-Hilbert calculation completed; complementary (V_5) contraction across the boundary and general two-equation realization not constructed.  
**Scope:** fixed smooth rational quartic \(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\); prioritize geometry and actual equations, not new infrastructure. No STCI claim in characteristic zero.


## Central target, with arbitrary translated residual components allowed

**UM1 (conjecture, not proved):** For any proper actual
two-surface CI \(Z=V(F_a,G_b)\) in characteristic
zero, if its **entire fundamental cycle** is
\[
 [Z]=\sum_i n_i[C_{u_i,v_i}],\qquad
 n_i>0,\qquad \sum_i n_i=ab/4,
\]
then \(\sum_i n_i u_i/v_i=0\).
There may be multiple **residual translated
quartics**, including nonreduced components.
There may be **no additional
nontranslated curve components**.
The sole-support case \(m[C]\) is only
the diagonal counterfactual; it would
contradict UM1 in characteristic zero.

**Actual-equation reduction.** Such a pair has
\(H_Z(x_1x_2,x_0x_3)\in(F,G)\), where
\(H_Z(A,B)=\prod_i(A-(u_i/v_i)B)^{n_i}\).
It also satisfies
\(A M_{12}-2B M_{03}\in(F,G)\).
For first normal equation layers
\(F=f_0+x_0p+x_3q+\cdots\),
\(G=g_0+x_0r+x_3s+\cdots\)
along the disjoint line \(L=V(x_0,x_3)\),
the exact consequence of translated
support is
\[
 2M_1=\operatorname{Res}_{f_0,g_0}(ps-qr).
\]
Thus UM1 is **equivalent to first-jet
isotropy on the joint actual-equation
incidence with all components translated**.
This isotropy does **not** follow from
the regular-sequence condition alone.
In particular, restricting the mixed
Jacobian identity to \(L\) gives only
\(x_1x_2 J(f_0,g_0)\equiv0\pmod{(f_0,g_0)}\);
this is automatic because the Jacobian
generates the binary CI's socle.
One must exploit the **entire spectral
and global support** constraint, beyond
that tautological restriction. The
stronger sole-support power test
\(I_C^m\subset(F,G)\) is an independent
*special-case equivalence*, not a
substitute for UM1 and not a premise
for the general translated-cycle proof.

The [recognized proof scopes](../../arguments/torus/chow_arrangement_moments.md)
cover actual invariant ideals,
eigenform generators and certain
congruences; selected low-degree cases
on this PR still await review.
The general non-invariant nonreduced
case remains an open mathematical
implication, not established by the
new residue/Poisson bridge.

### The elementary coefficient of the full two-torus Chow form

The [full transverse Chow coefficient comparison](../../arguments/torus/transverse_chow_moment_realization.md#11-the-first-moment-is-already-a-linear-full-chow-coefficient)
now records, directly in the paired coordinates,
\[
 \mathcal C_\sigma(X,Y,Z)
  =\prod_i(X+u_iY+v_iZ)^{n_i},\qquad
 \boxed{[YZ^{m-1}]\mathcal C_\sigma
  =[Z^m]\mathcal C_\sigma\,M_1.}
\]
This is an **elementary multisymmetric coefficient**,
a linear projective Chow hyperplane on the full
two-dimensional arrangement—not a quotient
trace condition requiring denominators.
The toric parameter plane \([W:U:V]=[1:u:v]\)
makes \(\xi=U/V\) the parameter of **lines**
\(U-\xi V=0\) and
\(\eta=U^2/(WV)\) the parameter of **conics**
\(U^2-\eta WV=0\).
They meet in one interior point representing
the translated quartic (and one fixed boundary
point), so this rephrases complete paired
realization as line/conic incidence.

For a proper *actual* pair
\(F_a,G_b\) with this entire cycle,
restriction to the moving line family
\(x_3=x_0,\ x_0+yx_1+zx_2=0\)
gives a binary Sylvester resultant
\(\mathscr R_{F,G}(y,z)\) with
\[
 \boxed{
 M_1=\frac{[YZ^{m-1}]\mathcal C_\sigma}
           {[Z^m]\mathcal C_\sigma}
   =-\frac14\frac{[yz]\mathscr R_{F,G}}
                   {\mathscr R_{F,G}(0,0)}
   =\frac12\operatorname{Res}_{f_0,g_0}(ps-qr).
 }
\]
Thus the **elementary symmetric coefficient**,
the **mixed polar of the actual CI resultant**,
and the **first-jet Serre pairing** are
literally the same obstruction on the
full translated-cycle incidence.
None of these exact identifications
proves its vanishing in the general
non-invariant nonreduced case.
The required theorem is that the
**same actual two defining equations**
realizing a full translated arrangement
make this distinguished resultant
coefficient zero. The projective
hyperplane and the resultant side
offer two complementary algebraic
formulations of the one unresolved
identity.

### Explicit resultant factors: the full two-torus data

The [two-step toric norm computation](../../arguments/torus/transverse_chow_moment_realization.md#12-the-complete-ci-resultant-as-a-product-of-two-step-toric-norms)
writes the **entire normalized actual CI line
resultant** as
\[
 \widehat{\mathscr R}_{F,G}(y,z)
 =\prod_i
  \left[(1-2\xi_i yz)^2-
      \frac{\xi_i^2}{\eta_i}
       (y^2+\eta_i z^2)^2\right]^{n_i},
 \qquad
 \xi_i=\frac{u_i}{v_i},\
 \eta_i=\frac{u_i^2}{v_i}.
\]
Each factor is a composition of **two quadratic
norms** along \(t\mapsto-t\) on
the four-point plane section, with
\(X_iY_i=\xi_i\), \(Y_i^2=\eta_iX_i^2\).
A single factor
\(1+A yz+B y^4+C y^2z^2+D z^4\)
satisfies the two **toric equations**
\(A^2=8C,\ C^2=4BD\).
Consequently the translated arrangement
maps to the multiplicative Chow image
of this explicit toric surface inside
the line-resultant space. The target
\(M_1=0\) is simply the **first
elementary symmetric equation** on
the \(yz\)-coefficients of these factors:
\([yz]\widehat{\mathscr R}=-4\sum_i n_i\xi_i\).
The \(y^4\) and \(z^4\) axis spectra
respectively record \(\xi_i^2/\eta_i\)
and \(\xi_i^2\eta_i\); their
**paired products** are \(\xi_i^4\),
so the mixed coefficient is what
retains the fourth-root phase and
the pairing of the two torus characters.
The full product formula alone does
not force this coefficient to vanish;
the missing step is a restriction
imposed by its **actual two-equation
Sylvester resultant realization**.

### New common carrier-free realization object: the full-Chow envelope

The [opposite quartic Chow-envelope theorem](../../arguments/torus/full_transverse_chow_pullback_envelope.md)
strengthens the previous single-resultant
factorization. The *same full*
\(\mathcal C_\sigma=\prod_i(X+u_iY+v_iZ)^{n_i}\)
has two **homogeneous quartic pullbacks**
through the weight-four and weight-twelve
three-monomial quotient maps. Each
produces \(m+1\) degree-\(4m\)
equations lying in every proper
actual CI ideal realizing \(\sigma\).
On the dense ambient torus the
coefficient ideals both equal the
canonical fat-point ideal
\(\cap_i I_{C_i}^{n_i}\);
their **sum** has radical
\(I_{\cup_i C_i}\) globally, because
their two distinct pairs of base
coordinate lines meet only at
\(p_0,p_\infty\).
These facts retain **both paired torus
coordinates** and arbitrary repeated
components, rather than one quadric
pencil spectrum.

The corresponding constant fat-point
algebra has length
\(N=\sum\binom{n_i+1}{2}\).
Any realizing CI selects a finite-flat
rank-\(m\) **moving algebra quotient**
over the orbit coordinate, whose kernel
has rank
\(\delta=\sum\binom{n_i}{2}\).
For \(\delta=0\), invariance is
forced and UM1 is already covered.
For a double component the moving
choice is a tangent line, i.e. a
\(\mathbf P^1\)-valued rational map;
higher multiplicities give
punctual-Hilbert quotient choices.
Its **norm** is exactly
\(\mathcal C_\sigma\) and its
**trace of \(u/v\)** is \(M_1\).
Thus the missing all-degree theorem
is sharply localized to **which
moving fat-envelope quotients can
extend simultaneously across
both orbit endpoints and arise
from two global homogeneous
surface generators**. This
identifies the actual loss of
information between cycle
coefficients and CI structure,
rather than replacing it with
a carrier-by-carrier mate search.
No trace vanishing follows
from the quotient condition alone.

### Sharper full-Chow interface: opposite (2,3) rulings and an \(M_1\) syzygy

The [opposite-ruling Chow polarizations](../../arguments/torus/weighted_chow_quadric_cubic_polarizations.md) improve the former degree-\(4m\) full-Chow pullbacks. Let \(Q_i=x_1x_2-\xi_i x_0x_3\), \(T_i^+=x_0^2x_2-u_i x_1^3\), \(T_i^-=x_1x_3^2-(v_i^2/u_i^3)x_2^3\). On \(Q_i\), their divisors are \(C_i+2L_{01}\) and \(C_i+2L_{23}\); the residual ruling lines are skew. Both degree-\((2m,\ldots,3m)\) coefficient chains of \(\prod_i(\lambda Q_i+\mu T_i^\pm)^{n_i}\) are actual ideal members in every proper translated-cycle CI. Their **sum has radical exactly the translated support**, and generically recovers the same full Chow fat-point envelope, with no single-carrier choice.

The normalized first cubic polars satisfy the **exact degree-\((2m+3)\) global syzygy**
\[
 x_2^2E_++x_0^2E_-+
 x_1 H_\sigma\bigl(m x_1x_2+M_1(\sigma)x_0x_3\bigr)=0,
 \quad H_\sigma=\prod_i Q_i^{n_i}.
\]
This exposes the first elementary symmetric function as the coefficient in the **comparison quadric between the two residual rulings**. It is a stronger concrete source of a possible all-degree compatibility theorem than either the one-plane resultant or the degree-\(4m\) Chow envelope alone. However the polynomial syzygy holds for all **unrealized** cycles as well, so **global two-generation has not been shown to force its \(M_1\) coefficient to vanish**. The restricted characteristic-zero UM1 conjecture is unchanged.

## Primary Chow realization and first-moment separation

For repeated curves the primary space remains the unordered cycle space
\(\operatorname{Sym}^m T\), with its multiplication-of-Chow-forms map.
The Hilbert or moving transverse-algebra lift is auxiliary, not a
replacement for the cycle space. Forgetful maps are not required at
this stage. The [moment separation argument](../../arguments/torus/chow_realization_moment_separation.md)
records the unrestricted resultant incidence, the normalized projective
product locus, and the power locus \(m[C_z]\).

The proposed low-degree proofs awaiting independent review use an
irreducible extreme component to obtain a proper invariant initial
complete intersection with unchanged Chow point. They give the entire
(3,4) cycle locus by two constant-character families cut by
\(M_1=\sum n_i u_i/v_i=0\), and cover every (4,4) multiple-support
realization by this degeneration or the exceptional opposite-parameter
linkage argument. The (4,4) small diagonal is independently excluded
by R-0022; a direct proof of the moment identity on that diagonal remains
missing. In all degrees the moment hypersurface is disjoint from the
interior small diagonal in characteristic zero. Projective boundary
power cycles can be common limits.

The next mathematical question of this activity is coverage of the
moment identity for unrestricted proper pairs, not a forced construction
of marked Hilbert forgetful morphisms. Preserve the distinction between
the proper-CI cycle image and its projective closure.

The [cross-branch universal first-moment synthesis](../../arguments/torus/universal_first_moment_proof_boundary.md)
compares main and PRs #171--#173. The existing all-degree trace and
six-layer residue formula give an exact source target; exceptional
non-invariant quartic cycles and same-ideal toric cancellations prohibit
an unqualified invariant-degeneration proof. The normal-carrier replacement
splits generically curvilinear from entirely-thick cases without covering
the latter. The priority is a joint source/cycle identity forcing the
mixed trace to vanish, not additional arrangement classification.
This synthesis contains no new all-degree theorem and is not an
independent mathematical review.

The broader [nine-Framework and literature reassessment](../../arguments/torus/universal_first_moment_corpus_review.md)
and the [complete 84-Result crosswalk](../../arguments/torus/universal_first_moment_result_crosswalk.md)
now assess every Result on main by its precise relationship to the
first moment: direct proof input, bridge needing an additional theorem,
negative control, or currently independent background. This reorients
carrier, spectral, normal-filtration, residual, arithmetic, and local
cohomology results around their **missing map to the mixed trace**
rather than assuming those frameworks prove or even determine it.
The October 2026 Brevik--Nollet very-general thick-carrier Picard
theorem is recorded in [literature](../../literature/README.md#brevik--nollet-october-2026-very-general-thick-carriers),
with its special-carrier and non-Cartier limitations. The first
priority remains a joint actual-equation/Chow-matched source identity;
a speculative relative divisor-cycle functional is the most distinct
geometric alternative, not an established obstruction.


The [intrinsic quadric-spectrum and opposite-projection comparison](../../arguments/torus/quadric_pencil_spectral_intrinsic_geometry.md)
starts from the Segre graph (C\subset Q\subset\mathbf P^3), explains
why (q=u/v) labels a unique containing quadric **and** an associated
contact structure, identifies the first moment as the trace of the
projected effective divisor, and compares degree-four and resolved
degree-two projections. It also distinguishes the canonical spectral
form from the complete Chow form and from a minimal nilpotent equation.
Kalinin's existing Legendrian-on-quadric classification is the
literature benchmark. No new moment vanishing is inferred.

## Iteration: from quadric spectrum and actual Jacobians to a Serre-duality class

The [new complete argument](../../arguments/torus/spectral_jacobian_first_jet_bridge.md)
integrates the main-branch *actual Jacobian/socle theorem* with
the spectral form and all-degree trace identities. The two independent
characters of the transverse quotient are
\[
 \xi=\frac{x_1x_2}{x_0x_3}=\frac uv,\qquad
 \eta=\frac{x_0x_2^2}{x_1^2x_3}=\frac{u^2}v .
\]
They determine a unique quadric and a cubic scroll, and
\[
 Q_\xi\cap R_\eta=C_{\eta/\xi,\eta/\xi^2}+L_{01}+L_{23}
\]
as actual intersection cycles. For any proper CI with *entire*
translated-quartic cycle, the actual Jacobian minors obey
\[
 x_1x_2 M_{12}-2x_0x_3 M_{03}\in(F,G).
\]
Combined with the existing spectral equation \(H(A,B)\in(F,G)\),
this provides a **converse recognition criterion** for translated
reduced support, when \(Y\cap V(x_0,x_3)=\varnothing\).
For the first moment, the same identity and classical residue/duality
give the much smaller exact test
\[
 \boxed{2M_1
 =\operatorname{Res}_{f_0,g_0}(ps-qr)
 =\operatorname{Tr}_{L}\partial_{f_0,g_0}(ps-qr).}
\]
The right side is the Serre trace on \(L\simeq\mathbf P^1\)
of the Koszul connecting class of the **first normal jets** of
the actual pair. Equivalently it is a perfect alternating
Macaulay pairing on a symplectic space of dimension
\(2\min(a,b)\). This supersedes the general six-layer trace
formula as the *shortest expression* **once** translated support
is known; the six-layer formula remains necessary for
arbitrary proper pairs.

**Present result:** the geometry and reduction above, plus a
proper quartic containing pair with nonzero pairing and residual
degree twelve. **Still missing:** proof that the image of the
full actual-equation incidence satisfying both recognition
conditions is isotropic under this perfect pairing. The pairing
itself is not zero for arbitrary containing pairs. This is now the
preferred precise joint-source gate for UM1; it avoids the false
assumptions that non-invariant pairs can be torus-diagonalized
or that an intrinsic Hilbert limit remains a two-generator CI.

**Review status:** proposed new argument, not independently
six-perspective reviewed. No unrestricted STCI theorem.

### Sole-support jet tower: a complete duality criterion and tested limits

The [sole-support jet and residue argument](../../arguments/torus/sole_support_first_jet_gate.md)
compares two established **actual-equation**
consequences for a hypothetical characteristic-zero
STCI \(J=(F_a,G_b)\), \(m=ab/4\):
\[
 M_{12}-2M_{03}\in J,\qquad I_C^m\subset J.
\]
The first requires a **nonzero** first-normal
Macaulay/Serre pairing
\(\Omega(v_0,v_3)=ab/2\).
It is achievable for global containing
pairs of every bidegree \(a,b\ge4\),
without eliminating their residual curves.

The unique minimum-degree member of \(I_C^m\)
is \(Q^m\). For \(L=V(x_0,x_3)\),
its first potentially nonautomatic
normal coefficient occurs at
\[
 r_*=(a-2)(b-2)/2;
 \qquad
 [Q^m]_{r_*}
 =\mathcal R_{F,G}(Q^m)\in
 H^1(L,\omega_L)\otimes
 \operatorname{Sym}^{r_*}\langle x_0,x_3\rangle .
\]
The same **relative Grothendieck residue**
also yields
\(\mathcal R_{F,G}(M_{03})=ab/2\).
The linear map
\(H(A,B)\mapsto\mathcal R_{F,G}(H(A,B))\)
annihilates each realized entire-cycle
spectral form. This is a joint source/Chow
coefficient condition, not full ideal membership;
in \((6,6)\) the first power class is an
octavic, at normal order eight.

In a restricted \((4,4)\) first-jet family,
the sole-support Poisson and first power
conditions demand incompatible
\(\lambda\mu=8\) and \(4\).
But the stronger [explicit global negative
control](../../arguments/torus/sole_support_first_jet_gate.md#a-stronger-negative-control-both-leading-stci-conditions-can-hold)
passes **both** leading residue requirements
while retaining a residual degree-twelve curve.
Indeed \(\mathcal R_{F,G}(Q^4)=0\),
but \(\mathcal R_{F,G}(x_1Q^4)=2x_0^2x_3\)
and \(\mathcal R_{F,G}(x_2Q^4)=12x_0x_3^2\);
the full Poisson identity fails at the
next normal order as well.

The **complete** condition is the [necessary-and-
sufficient ideal-power/perfect-residue criterion](../../arguments/torus/sole_support_first_jet_gate.md#full-exact-stci-jet-criterion-ideal-powers-and-the-perfect-residue-pairing):
for a proper pair \(F,G\in I_C\),
STCI is equivalent to \(I_C^m\subset J\),
or to \(\mathcal R_{F,G}(ge)=0\)
for every explicit monomial generator
\(g=Q^{m-j}U^\alpha W^\beta V^\gamma\)
of \(I_C^m\) and every element \(e\)
of a finite \(k[x_0,x_3]\)-basis of
\(S/J\). Finite flat **Gorenstein duality**
makes that pairing perfect, so it detects
the *actual* ideal rather than one trace.
This is an all-degree **equivalent algebraic
formulation**, not an all-degree
nonexistence theorem or an elimination
of the source coefficients. The precise
research gap is whether these jointly
realized source equations have a solution
for any bidegree in characteristic zero.
All new specializations remain **pending
independent mathematical review**.

## Motivation and the three genuinely different parameter spaces

The [full Chow-polytope rigidity theorem R-0074](../../results/chow_polytope_rigidity.md) says that the cycles with full column-weight polytope \(mP_C\) are exactly effective sums of \(m\) diagonal translates of \(C\). This is a strong **cycle** classification, not a classification of reduced unions, their blow-ups, or equations.

The arrangement problem starts from an unordered finite configuration \(Z\in\operatorname{Sym}^m T\), \(T=(\mathbf G_m)^2\), and asks:

1. Which degree-\(d\) hypersurfaces contain its orbit-curve arrangement?
2. Which proper pairs of degrees \((a,b)\) realize exactly the intended *support* or the more restrictive *reduced fundamental cycle*?
3. Which boundary/endpoint conditions distinguish actual embedded realizations from configurations allowed by Chow data?
4. Can the \(V_5\) complementary contraction for a single curve be recognized in an appropriate family of blow-ups?

These correspond to distinct moduli operations: the toric **Chow quotient** of \(\mathbf P^3\) by \(H\) parametrizes completed orbit **cycles**; a Hilbert functor parametrizes **embedded schemes with fixed polynomial**; an equation-incidence locus parametrizes **actual sections and proper pairs**. Do not identify the three.

## Solved input: an explicit compactified quotient

The [quotient-fan calculation](../../arguments/torus/chow_quotient_fan_and_blowup_comparison.md) applies Kapranov–Sturmfels–Zelevinsky to weights \(0,1,3,4\). The normalized quotient surface has fan rays
\[
 (1,0),\ (2,3),\ (0,1),\ (-3,-4)
\]
in the valuation lattice of
\[
 U=x_0^2x_2/x_1^3,\quad V=x_0^3x_3/x_1^4.
\]
Its four fixed cycles are
\[
 4L_{03},\quad L_{01}+3L_{13},\quad
 3L_{02}+L_{23},\quad L_{01}+2L_{12}+L_{23}.
\]
The fan itself is toric and needs no speculative construction. The Chow orbit resultant has six exponent pairs with Newton quadrilateral vertices ((0,3),(0,4),(4,1),(3,1)); its four vertex coefficients are precisely the Chow forms of the four fixed cycles, giving a direct Newton-duality check. The [normalized graph fan](../../arguments/torus/chow_quotient_fan_and_blowup_comparison.md#5-the-normalized-graph-fan-and-its-two-global-endpoint-sections) has **eight rays and twelve maximal cones**, with two disjoint toric divisors mapping isomorphically to the quotient surface and contracting to (p_0,p_\infty). These global endpoint sections carry the least/highest weight-coefficient restrictions of any homogeneous equation. The boundary **scheme ideals** of the universal family, and in particular possible embedded structures, are *not* fixed by these four cycle identities.

Over the open quotient torus, each \(C_{u,v}\) is the image of
\([s:t]\mapsto[s^4:s^3t:u st^3:v t^4]\). There is a section at \(r=1\) on the dense ambient torus. This section and the graph family over \(T\) are standard; extension across the toric boundary requires checking the chosen graph/refinement. In characteristic zero Chen–Satriano gives a stable-log-map interpretation of the normalized rank-one Chow quotient [arXiv:1201.3406](https://arxiv.org/abs/1201.3406).

## Solved input: endpoint-stratified Hilbert data

The [endpoint rank/delta calculation](../../arguments/torus/arrangement_endpoint_delta.md) computes, for the *reduced union* \(A_Z\) of \(m\) distinct translates,
\[
 P_{A_Z}(d)=4m\,d+m-\delta_0(Z)-\delta_\infty(Z),
\]
where the two defects are explicit finite sums of ranks of weighted monomial-evaluation matrices of weights \(3,4\). The second uses the unimodular change of parameters
\[
 (u,v)\mapsto(\alpha,\beta)=(v^2/u^3,\ v^3/u^4).
\]

This explains immediately why a universal **flat** Hilbert family over the entire distinct-configuration locus cannot be assumed. Even two distinct curves have endpoint intersection lengths \(3\) or \(4\) depending on their parameters. For four general translates, the reduced union has polynomial \(16d-22\), rather than the \((4,4)\) CI polynomial \(16d-32\). For four distinct translates realized by the standard complementary eigenquartic equations, the endpoint defects are \(18\) and \(18\), giving precisely \(16d-32\).

Thus Chow-admissible configurations are much more plentiful than the possible reduced-CI configurations, *before* asking about explicit equations. This is a genuine interface between Chow rigidity and embedded endpoint geometry.

### A complete two-endpoint incidence model in bidegree \((4,4)\)

The [dual-line criterion](../../arguments/torus/arrangement_endpoint_delta.md#the-reduced-44-locus-as-two-affine-line-incidence-conditions) repackages the repository's already-proved reduced-quartic realization theorem: for four **distinct** orbit parameters, the reduced union is a \((4,4)\) CI exactly when \(Z\) lies on an affine line \(v=A+Bu\) with \(A\ne0\), while the opposite configuration \(Z^\vee\) lies on a second line \(\beta=C+D\alpha\) with \(C\ne0\). The two lines yield actual quartic generators, and Bézout with the boundary check proves sufficiency. This gives a geometric explanation for the four-dimensional realization locus and the endpoint defects \(18+18\); its necessity uses the established eigenform-generator lifting theorem, so it must **not** be extended to arbitrary nonreduced STCI presentations without proof.

This is a particularly promising template for arbitrary degrees: find the allowed projective linear series on the **two global endpoint sections** of the normalized graph, then ask whether they arise from the *same two homogeneous equations*. The point is to uncover a common global realization law, not to extrapolate a low-degree line criterion formally.

## Symmetric marked realization, forgetful maps, and compactification

The [marked arrangement and forgetful geometry](../../arguments/torus/marked_arrangement_forgetful_geometry.md)
develops the configuration-first, Kapranov-inspired direction. No translated
component is normalized to \(C_0\); all labels remain symmetric. In the full
reduced \((4,4)\) locus the unique weight-four carrier is \(v=A+Bu\),
\(A\ne0\). With \(q=u/v\), the root constraints are exactly
\[
 e_1(q)=0,\qquad e_2(q)-B e_3(q)+B^2e_4(q)=0,
\]
including \(B=0\). On \(B\ne0\) the three intrinsic boundary marks give a
seven-pointed rational carrier with normalized root coordinates \(x_i=1-Bq_i\),
satisfying \(\sum x_i=4,\ \prod x_i=1\).

The four forgetful maps to extendible triples are isomorphisms onto their
open images: the missing \(q\)-mark is minus the sum of the retained three.
More strongly, any two different triple-image conditions already determine
the entire reduced quartic realization locus on the distinct-configuration
open. Pair-image conditions are generically insufficient. This is an
explicit pullback characterization, not just recovery of a configuration
from its markings.

As a secondary model for this special carrier, the closure of the abstract three-boundary-mark chart in
\(\overline M_{0,7}\) inherits a stable marked universal curve, and the
product of its four forgetful maps is a closed embedding by the established
anchored cross-ratio theorem. Whether the compactified locus equals the
intersection of the inverse images of the compactified triple loci is
a separate open boundary question. The full framed torus configuration,
including the \(B=0\) carrier chart, needs additional compactification data.
Hilbert-of-points tautological evaluation maps, nested Hilbert schemes,
Fulton–MacPherson ordered configurations, and relative Hilbert schemes
of moving quotient carrier curves provide the candidate ambient
constructions, not an already-proven universal flat CI compactification.

## The arrangement-first compactification program

**Priority:** first compactify the space of all arrangements, independently of the degrees of the two defining surfaces and independently of the choice of a carrier. The complete-intersection locus is a distinguished sublocus of that space. Keep all arrangement labels symmetric; do not fix a translate as \(C_0\). Quotient by simultaneous ambient automorphisms only after constructing the geometry. The marked rational-carrier and K3 models are useful tests of the resulting geometry, not the choice of ambient moduli space.

### A projective configuration compactification with all forgetful maps

Laurent Evain, [*Compactifications des espaces de configuration dans les schémas de Hilbert*](https://www.numdam.org/articles/10.24033/bsmf.2495/), Bull. SMF 133 (2005), 497–539 (also [arXiv:math/0107041](https://arxiv.org/abs/math/0107041)), develops precisely the existing approach of compactifying configurations by products of Hilbert schemes. Use the following elementary subset-union member of that approach.

Let \(S\) be a projective compactification of the quotient torus \(T\) with a morphism to its orbit Chow closure, for example the normalized Chow quotient already calculated above. If a flat family of single orbit-curve schemes is desired, take the graph closure of the map from \(T\) to \(\operatorname{Hilb}_{4d+1}(\mathbf P^3)\) over \(S\), and, if useful, a smooth equivariant projective refinement. Denote this refined surface by \(S'\) and its universal single-curve family by \(\mathscr C\subset\mathbf P^3\times S'\).

For a finite ordered label set \(J\), let
\[
 \mathcal X_J=\overline{\left\{
 \bigl(\{z_i:i\in I\}\bigr)_{\varnothing\ne I\subseteq J}:
 (z_i)_{i\in J}\in\operatorname{Conf}_J(T)
 \right\}}
 \ \subseteq\prod_{\varnothing\ne I\subseteq J}\operatorname{Hilb}^{|I|}(S').
\]
Take the reduced closure, and use the same \(S'\) for all finite label sets. The singleton factors recover the ordered positions. The full-set factor remembers the limiting length-\(|J|\) scheme. All subset factors preserve further collision data. Projection onto the factors indexed by subsets of \(K\subseteq J\) extends the forgetful map to a proper surjective morphism \(\mathcal X_J\to\mathcal X_K\): it agrees with deletion on the dense distinct locus and its image is closed. These morphisms compose as expected; relabeling gives the symmetric group action. No arrangement mark is preferred. Over the distinct locus the graph is isomorphic to the original configuration space.

This is an available projective model, not a claim that it is minimal, smooth, or identical to a Fulton–MacPherson compactification. The latter can be compared or added if disjoint markings on expanded surfaces are required. Evain's work is the first reference for more refined enrichments, structural geometry and redundant factors.

### The universal family: distinguish a flat source from its embedded image

Every subset factor supplies a universal finite flat scheme \(\mathscr Z_I\subset S'\times\mathcal X_J\) of degree \(|I|\). For \(I\subseteq K\) there are canonical inclusions \(\mathscr Z_I\subseteq\mathscr Z_K\), since inclusion of finite subschemes is a closed Hilbert-incidence condition. On collision the union of the singleton sections need not equal the full-set scheme: the latter retains infinitesimal directions.

Pull back \(\mathscr C\to S'\) along \(\mathscr Z_I\to S'\):
\[
 \mathscr D_I=\mathscr C\times_{S'}\mathscr Z_I
       \longrightarrow\mathcal X_J,\qquad
 \mathscr D_I\longrightarrow\mathbf P^3\times\mathcal X_J.
\]
The first morphism is flat and projective, by base change and composition of flat morphisms. On the distinct locus the source consists of \(|I|\) separate copies of the individual curves in each fiber; the map to \(\mathbf P^3\) identifies their common endpoints. On collision the source retains the finite transverse scheme and maps to the corresponding thickened or degenerate curve. Both source families and morphisms to \(\mathbf P^3\) are compatible with subset inclusions, relabeling and forgetful maps.

This already constructs a compactification carrying a universal **family of maps from arrangements**, with all forgetful morphisms. It does **not** construct a single flat family of the embedded reduced unions everywhere: their Hilbert polynomials vary even over distinct configurations, as proved above. Nor does taking scheme-theoretic images commute automatically with base change. To obtain actual embedded flat unions, restrict to a common endpoint-rank/Hilbert-polynomial stratum for every subset and close the graph of its maps to the corresponding curve Hilbert schemes. Projection preserves subset forgetfulness into the respective smaller stratum closures. Compare these Hilbert refinements with \(\mathcal X_J\) and with the relative Rees blow-ups; none of these identifications is automatic.

### The equation spaces and the realization loci

Over the part of \(\mathcal X_J\) where the entire finite scheme \(\mathscr Z_J\) lies in \(T\), the explicit parametrization \(\mathscr C|_T\simeq\mathbf P^1\times T\) identifies the pullback of \(\mathcal O_{\mathbf P^3}(d)\) with \(\mathcal O_{\mathbf P^1}(4d)\). Restriction gives the global map
\[
 S_d\otimes\mathcal O_{\mathcal X_J}
 \longrightarrow
 H^0(\mathbf P^1,\mathcal O(4d))\otimes
 p_*\mathcal O_{\mathscr Z_J},
\]
where \(p:\mathscr Z_J\to\mathcal X_J\) is finite flat. The target has rank \((4d+1)|J|\), and over the distinct locus the fiber kernel is exactly \(K_d(Z)\). At collisions this records the equations that vanish on the family of curves over the length-\(|J|\) transverse scheme; it does not parametrize every possible embedded non-invariant thickening. Across the toric boundary, use tautological evaluation for each monomial weight system on an appropriate refinement, or for sufficiently large degree use the flat single-curve family and relative cohomology and base change. The resulting incidence and Grassmannian maps need not have constant ranks. Take their graph closures or rank strata as required, not an assumed globally locally free kernel.

For \(m=ab/4\), define \(\mathcal R_{a,b}^{\rm red}\) inside the ordered distinct locus by the established weightwise evaluation and coprimality conditions. Take its closure in the configuration model or a Hilbert/Grassmannian refinement. For \((4,4)\) the criterion is the pair of lines in the two weight-space embeddings, with the boundary coefficient opens, not merely one collinearity. The two-triple reconstruction in the marked-arrangement argument is an explicit first example of compatibility under forgetting.

### The deepest diagonal and the precise STCI target

There is a natural projective cycle map
\[
 \kappa_J:\mathcal X_J\longrightarrow
 \operatorname{Sym}^{|J|}(S')\longrightarrow
 \operatorname{Chow}_{1,4|J|}(\mathbf P^3)
\]
given by the Hilbert–Chow map of the full-set factor followed by the sum of the single-orbit Chow cycles. Define the interior full-collision stratum as the preimage of cycles \(|J|[C_z]\), \(z\in T\); all finite transverse schemes supported at \(z\) and additional collision data remain in that preimage. This is a better target than choosing a single labeled translate. The fixed cycle \(m[C_0]\) is one member of this symmetric condition.

**Already proved in characteristic zero:** the [Chow trace-moment theorem](../../arguments/torus/chow_arrangement_moments.md) supplies a regular condition \(\sum u_i/v_i=0\) on every reduced CI configuration and a linear Chow-coordinate separator on its projective Chow closure. Every interior deepest diagonal has moment \(m u/v\ne0\). Consequently the closure of \(\mathcal R_{a,b}^{\rm red}\) in any configuration refinement with this cycle map misses the entire interior full-collision stratum. The same is true of the eigenform-covered repeated-cycle loci in the theorem's stated scope. This is a useful test of the compactification, but does not solve unrestricted STCI: a non-invariant proper CI supported on a repeated cycle might not belong to the closure of the reduced arrangement locus. The subsequent central problem is the existence and coverage of such additional actual equation-incidence strata, not reproving the trace separation of reduced collisions.

The residual transverse torus acts simultaneously on the configuration; it commutes with the label permutations. Keep that action rather than choosing one label as the origin. Later compare quotient by simultaneous translations, coordinate reversal, and the equivalence relation induced by \(\operatorname{PGL}_4\) on the actual embedded cycles and their Hilbert lifts. An arbitrary ambient automorphism need not preserve the fixed-coordinate arrangement slice. Do not conflate abstract marked-carrier moduli with ambient projective equivalence.

### Immediate next work, in order

1. Instantiate the all-subsets Hilbert compactification first over \(T\), compare it with the toric boundary single-curve refinement, and identify the finite transverse collision strata and their forgetful maps.
2. Study the extension of the two weight-space evaluation maps, their rank strata and properness conditions on this space, starting with \((4,4)\) as a test; examine the general \((a,b)\) partial-configuration reconstruction mechanism rather than imposing a rational carrier.
3. Compare the resulting source families with the actual embedded Hilbert limits and relative ideal blow-ups, and distinguish the reduced realization closure from additional non-invariant repeated-cycle lifts.
4. Only then make the residual automorphism quotient. The [mirror quartic K3 and the natural maps to \(M_{0,5}\) and \(M_{0,4}\)](../../arguments/torus/marked_arrangement_forgetful_geometry.md#6-the-quartic-marked-root-surface-is-a-known-mirror-quartic-k3-model) are useful descriptions of the special quartic realization locus after separating framing parameters; they do not dictate the compactification of all arrangements.

## Constructed families of arrangement blow-ups

The actual family proposed in this discussion is now constructed and analyzed in
[relative arrangement blow-ups and the smooth separated model](../../arguments/torus/relative_arrangement_blowup_family.md).
This is **not** merely an analogy: there are two explicit relative blow-up schemes, and they are not identified without an additional principalization argument.

On the ordered distinct-configuration space \(B_m=\operatorname{Conf}_m(T)\), let
\[
 \mathcal I_m=\bigcap_i \mathcal I_{\mathcal C_i}
 \subset\mathcal O_{\mathbf P^3\times B_m},\qquad
 \mathcal X_m^{\rm Rees}
 =\operatorname{Proj}_{\mathbf P^3\times B_m}
     \bigoplus_{n\ge0}\mathcal I_m^n.
\]
This is the **direct family of blow-ups of the arrangement ideal**. Its fiber is not automatically
\(\operatorname{Bl}_{I_{A_Z}}\mathbf P^3\): taking intersections of ideals and forming Rees powers
can both fail to commute with specialization. The exact finite endpoint-evaluation matrices
give determinantal strata on which the *reduced union* does specialize correctly and is
Hilbert flat. For the Rees blow-up itself, one still needs normal-flatness/base-change
control of all powers of \(\mathcal I_m\).

There is also a **fully constructed smooth family of fiberwise blow-ups**.
Choose a smooth toric resolution \(W'\to\mathbf P^3\) of the normalized quotient graph.
Over its open quotient surface \(T\), the map is
\(\mathbf P^1\times T\to T\); the \(m\) lifted orbit curves over a distinct
configuration are *disjoint fibers*. Blow up their relative disjoint union:
\[
 \widehat{\mathcal W}_m
 =\operatorname{Bl}_{\coprod_i \widetilde{\mathcal C}_i}
       (W'\times B_m)\longrightarrow B_m.
\]
This is **smooth and projective** over \(B_m\), with the correct blow-up on every
fiber. The exceptional divisors are \(m\) disjoint copies of
\(\mathbf P^1\times\mathbf P^1\) in each fiber.

**Exact equation dictionary.** If \(H\) is the pullback of a hyperplane
from \(\mathbf P^3\) and \(\widetilde E_Z=\sum_i\widetilde E_i\), then
\[
 \boxed{H^0(\mathbf P^3,I_{A_Z}(d))
   \cong H^0(\widehat W_Z,dH-\widetilde E_Z)}
\]
for every \(d\). The proof is the direct-image identity
\(\psi_*I_{\coprod_i\widetilde C_i}=I_{A_Z}\) under
\(W'\xrightarrow{\psi}\mathbf P^3\), followed by the
regular-center blow-up pushforward. Thus the smooth family loses **no
containing equations**; however its divisor intersections still require
testing actual residual and boundary support.

**Normal geometry of the contraction.** The differential on the
normal bundles along any lifted orbit curve is
\[
 \mathcal O_{\mathbf P^1}^{\oplus2}
 \longrightarrow N_{C_z/\mathbf P^3}.
\]
It has local invariant factors \((3,4)\) at *both* endpoints,
hence determinant divisor \(7p_0+7p_\infty\).
This is a characteristic-independent calculation in the
\(u,v\) and opposite-endpoint coordinates, and explains the
existing normal-frame determinant as the contraction defect
between the separated blow-up model and the embedded quartic.

Finally the **actual pair-incidence family** is explicit:
on constant-rank strata the containing-equation kernels
\(\mathcal K_a,\mathcal K_b\) are vector bundles and
\(\mathbf P(\mathcal K_a)\times_{B_m}\mathbf P(\mathcal K_b)\)
parametrizes pairs containing the reduced arrangement. Its
coprime open is precisely the reduced CI realization locus
when \(ab=4m\), by the existing degree-exhaustion argument.
For nonreduced STCI support this equivalence does not hold.

**The direct family is no longer purely formal.** The [completed
two-curve model](../../arguments/torus/relative_arrangement_blowup_family.md#7-direct-fiberwise-rees-blow-ups-a-completed-two-curve-model)
shows that each pair of distinct curves has a local complete-intersection
union at both endpoints. After stratifying by whether \(u_1=u_2\)
and \(\alpha_1=\alpha_2\), all Rees powers commute with specialization:
the fiber of the *direct* relative blow-up is genuinely
\(\operatorname{Bl}_{C_{z_1}\cup C_{z_2}}\mathbf P^3\).
The local blow-up is an explicit isolated threefold hypersurface
\[
  y(y-ar^c)=\lambda z,\qquad c=3\text{ or }4,
\]
with the contact exponent determined by the endpoint strata. In
characteristic zero this is an isolated \(cA_1\) threefold singularity
with special surface sections of type \(A_{2c-1}\).
For higher \(m\), the [dual-planar local CI families](../../arguments/torus/relative_arrangement_blowup_family.md#8-a-higher-m-planar-locus-and-a-rigidity-threshold)
also have fiberwise direct blow-ups. Their two affine-line equations
impose an unexpected rigidity: for \(m\ge5\), every simultaneously
dual-planar configuration with distinct projected coordinates lies
on the same quadric \(V=BU\). Thus an all-degree classification
of arrangements will necessarily need richer quotient curves beyond
this simplest two-line geometry.

The genuinely unresolved comparison is now sharply located:
whether the pullback of \(I_{A_Z}\) to \(\widehat W_Z\) is invertible;
if not, which additional exceptional modifications make it so,
and which movable divisor classes admit complementary contractions?
For \(m=1\), the direct family is the trivial family of classical
\(\operatorname{Bl}_C\mathbf P^3\) and its \(V_5\) link.
For \(m>1\), the smooth separated family is **not** claimed
to be a family of \(V_5\) links.

## Divisors on arrangement blow-ups

For a prescribed reduced arrangement let
\[
 A_Z=\bigcup_{z\in Z}C_z,\quad
 \pi_Z:X_Z=\operatorname{Bl}_{I_{A_Z}}\mathbf P^3\to\mathbf P^3,
 \quad E_Z\text{ its exceptional Cartier divisor}.
\]
The blow-up universal property and Rees algebra give, for \(d\ge0\),
\[
 K_d(Z)=H^0(\mathbf P^3,I_{A_Z}(d))
       =H^0(X_Z,\mathcal O_{X_Z}(dH-E_Z)),\quad H=\pi_Z^*O(1).
\]
This is a description of the prescribed **base ideal**, not an assertion that \(dH-E_Z\) is base-point-free. When the branches have high-order common contacts, \(X_Z\) may be singular; there is no automatic Mori contraction complementary to \(\pi_Z\).

On the dense coordinate torus \(\Omega\simeq\mathbf G_m\times T\), an exact algebraic presentation of the arrangement is
\[
 q^{-1}(Z)=\operatorname{Spec}
 k[r^{\pm1},U^{\pm1},V^{\pm1}]/J_Z,
\]
where \(J_Z\subset k[U^{\pm1},V^{\pm1}]\) is the radical ideal of the finite reduced set. Its **scheme-theoretic closure** in \(\mathbf P^3\) is \(A_Z\): clear Laurent denominators to homogeneous equations and saturate by \(x_0x_1x_2x_3\). This recovers the *reduced union ideal*, not its potential CI thickening or a flat specialization of collisions. It gives a direct route from quotient equations to the blow-up center.

For arbitrary degree \(d\), the existing [actual restriction calculation](../../arguments/torus/fixed_surface_restriction_lifts.md) states
\[
 F(1,r,Ur^3,Vr^4)=\sum_w r^w f_w(U,V),\qquad
 F\in K_d(Z)\iff f_w|_Z=0\quad\forall w.
\]
All \(f_w\) must be retained; a general surface is not a torus eigenform. The locus of **entire orbit curves** contained in \(F\) is \(D_F=V(f_w:w)\subset T\). A surface can have many other points in its intersection with a mate; intersecting just \(D_F\) and \(D_G\) does not rule out non-orbit residual curves.

The global realization question is: which pairs of sections of
\(aH-E_Z\) and \(bH-E_Z\) yield coprime projective equations with *exactly* the prescribed generic multiplicities and no other positive-dimensional support? These are joint conditions, not a consequence of two separate containment spaces.

For a **reduced** CI arrangement with \(ab=4m\), the usual complete-intersection Hilbert polynomial and the delta formula imply the necessary numerical identity
\[
 \boxed{\delta_0(Z)+\delta_\infty(Z)
       =m\,[2(a+b)-7].}\tag{*}
\]
(Indeed \(P_{\rm CI}(n)=ab\,n+ab(4-a-b)/2\).) For general STCI support with nonreduced multiplicities, (*) need not hold for the reduced union: the cycle and scheme must instead be computed from the actual pair.

## Hyperosculating-plane support and the graph endpoint sections

The two hyperosculating planes are \(H_0=V(x_3)\) and \(H_\infty=V(x_0)\). Every orbit closure \(C_{u,v}\) meets \(H_0\) only at \(p_0\) and \(H_\infty\) only at \(p_\infty\). Therefore for a proposed proper pair with exact set-theoretic support \(A_Z\), the necessary boundary tests are
\[
 \operatorname{Supp}(V(F,G)\cap H_0)=\{p_0\},\qquad
 \operatorname{Supp}(V(F,G)\cap H_\infty)=\{p_\infty\}. \tag{H}
\]
These are tests on **actual projective equations**, not just the Laurent quotient. They are not sufficient: a residual coordinate line \(L_{03}=V(x_1,x_2)\), for example, meets those planes only at the same endpoints and would escape (H). Generic transverse local lengths together with degree exhaustion, or a direct global residual-support argument, remain essential.

The normalized toric quotient graph separates these points into the global sections \(D_h,D_{-h}\simeq S\) (where \(h=(1,3,4)\)); the first/last nonzero weight coefficients of \(F\) restrict to the leading equation sections there. The numerical endpoint defects and the quotient-line conditions are likewise attached to these two opposite marked ends. A proposed geometric *replacement* for repeated special-case boundary checks should compare the full restrictions and their ideals on both sections, **plus** what is left in the complement. It must not reduce either end to a scalar order or assume that (H) detects every residual curve.

## The \(V_5\) comparison: strong bridge and a sharp obstruction

The established [two-blowup section dictionary](../../arguments/residuals/blowup_residual_geometry.md) provides, for one curve in characteristic zero,
\[
 B=\operatorname{Bl}_{C}\mathbf P^3
   =\operatorname{Bl}_{\Gamma}V_5,\quad
 L=3H-E,\quad Q'=2H-E,\quad
 H=L-Q',\ E=2L-3Q'.
\]
In particular for \(a\ge3r\), the existing theorem identifies
\[
 H^0(\mathbf P^3,I_C^r(a))
 \cong H^0(V_5,I_\Gamma^{a-3r}(a-2r)).
\]
The link is *globally trivial* as the single translate \(C_{u,v}\) varies over the open torus (via diagonal coordinate automorphisms).

But **the blow-up of \(C\) does not resolve the rational quotient**. The [explicit arc calculation](../../arguments/torus/chow_quotient_fan_and_blowup_comparison.md#4-graph-of-the-rational-quotient-versus-the-v_5-contraction) gives the same exceptional direction at \(p_0\) for distinct quotient parameters \(u\ne1\). Hence \(B\to S\) extending \(q\) cannot exist. The toric normalization of the quotient graph and the non-toric blow-up \(B\) have a common refinement after principalization, but one is not the other. No new \(V_5\) contraction for an arbitrary arrangement is asserted.

## The distinguished quartic and its mates

For \(F_4=x_1^4-x_0^3x_3\), the quotient restriction is \(r^4(1-V)\); thus \(D_{F_4}=\{V=1\}\). Its familiar characteristic-positive mate \(G_4=x_2^4-x_0x_3^3\) restricts to \(r^{12}(U^4-V^3)\). In characteristic two the quotient length four concentrates at \((1,1)\); in characteristic zero it consists of four distinct translates, and their **reduced** union is a proper \((4,4)\) CI, as the endpoint defects also confirm.

The key caveat is that positive-dimensional translate locus **does not characterize** \(F_4\). For example
\[
 x_1^4+x_0^2x_1x_2+x_0^3x_3
\]
is an irreducible weight-four quartic (linear in \(x_3\), with coprime leading and constant coefficients) and contains every translate with \(1+U+V=0\). A meaningful rigidity statement needs the exact endpoint/normalization, mate-realization, or characteristic conditions. The [fixed-carrier theorem](../../arguments/torus/fixed_carrier_chow_arrangements.md) already classifies its specified *other* quartic carrier \(x_2^4-x_0x_3^3\) and mates via semigroup gaps \(1,2,5\); it must not be rediscovered under another label.

## Precise next tests (not claimed complete)

**A. Boundary universal family.** Use the arrangement-first compactification above and its universal source family as the primary comparison. The normalized toric graph fan \(W\) is now explicit (eight rays, twelve cones), including the two endpoint sections. Determine its **scheme-theoretic Chow fiber ideals** over each ray and fixed point, flatness, and any needed smooth toric refinement. Compare the graph with a *flat* Hilbert or log-map refinement rather than equating their moduli meanings. A boundary cycle does not determine a boundary embedded scheme.

**B. Common refinement and contractions.** Principalize \(I_C\) on the now-explicit \(W\), record its interaction with the two global endpoint sections and the two exceptional divisors over coordinate lines, and compute the transforms of \(3H-E\) and the contracted quadric \(2H-E\). Decide whether any meaningful \(V_5\) contraction persists after degeneration. The correct proof goal is a morphism/divisor calculation, not a verbal analogy with Sarkisov links.

**C. Configuration strata and equations.** Use the two exact endpoint rank matrices to stratify \(\operatorname{Sym}^mT\) by \(P_{A_Z}\), then restrict the weight-coefficient evaluation matrices of \(K_a(Z),K_b(Z)\). For candidate reduced CI types check (*) first, followed by coprimality and degree exhaustion. For repeated cycles or nonreduced supports, replace reduced-union criteria by the actual generic transverse local algebras and both endpoint images.

**D. Carrier geometry.** Classify the irreducible low-degree surfaces whose \(D_F\) is a curve, *modulo* the full diagonal torus, and characterize which admit proper mates with no additional support. Compare the classification with the proven eigenquartic realization locus and the root-polynomial gap criteria, without proposing uniqueness of \(F_4\) under insufficient hypotheses.

## Cross-framework implications and limitations

- **Chow polytope rigidity:** determines possible fundamental cycles, not their Hilbert polynomials or multiplicity structures. The endpoint formula supplies the missing concrete scheme-level filter.
- **Embedded torus quotients / formal normals:** the quotient \(Z\) and the two opposite-endpoint evaluation filtrations are different levels of information; neither alone determines joint generic intersection length of arbitrary actual generators.
- **Global equation realization:** \(K_d(Z)\) and divisors \(dH-E_Z\) give a geometric parameter source; the actual two-section incidence and residual support are the hard remaining conditions.
- **Residual construction/\(V_5\):** one-curve contractions are established, but there is a genuine obstruction to naively identifying the orbit-quotient graph with the classical blow-up.
- **Arithmetic:** in characteristic \(p\), Frobenius can turn several quotient points into one nonreduced root scheme. The reduced-union endpoint formula is not a substitute for its nilpotent quotient and endpoint thickening.

**Assessment:** the biggest completed mathematical gain is the exact endpoint Hilbert stratification and its reconciliation with the known quartic eigenpair realizations. The quotient fan is an explicit and useful established-theory computation. The genuinely new work still required is the graph-versus-Hilbert boundary comparison and the joint equations/contractions on suitable refined spaces. No degree-independent obstruction follows at present.
