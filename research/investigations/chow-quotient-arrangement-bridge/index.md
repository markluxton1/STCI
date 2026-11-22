# Chow quotient, arrangement blow-ups, and the \(V_5\) bridge

**Type:** investigation / cross-framework mathematical synthesis.  
**Status:** explicit quotient fan, normalized toric graph fan with two endpoint sections, and endpoint-Hilbert calculation completed; complementary (V_5) contraction across the boundary and general two-equation realization not constructed.  
**Scope:** fixed smooth rational quartic \(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\); prioritize geometry and actual equations, not new infrastructure. No STCI claim in characteristic zero.

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
The fan itself is toric and needs no speculative construction. The [normalized graph fan](../../arguments/torus/chow_quotient_fan_and_blowup_comparison.md#5-the-normalized-graph-fan-and-its-two-global-endpoint-sections) has **eight rays and twelve maximal cones**, with two disjoint toric divisors mapping isomorphically to the quotient surface and contracting to (p_0,p_\infty). These global endpoint sections carry the least/highest weight-coefficient restrictions of any homogeneous equation. The boundary **scheme ideals** of the universal family, and in particular possible embedded structures, are *not* fixed by these four cycle identities.

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

**A. Boundary universal family.** The normalized toric graph fan \(W\) is now explicit (eight rays, twelve cones), including the two endpoint sections. Determine its **scheme-theoretic Chow fiber ideals** over each ray and fixed point, flatness, and any needed smooth toric refinement. Compare the graph with a *flat* Hilbert or log-map refinement rather than equating their moduli meanings. A boundary cycle does not determine a boundary embedded scheme.

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
