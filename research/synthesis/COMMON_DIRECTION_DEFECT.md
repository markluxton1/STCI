# Common-direction divisor and special-fiber defect: a surface-level lemma

Date: 2026-10-17. **Status: elementary geometric lemma and proposed interface; not a new STCI exclusion.**

## Setup

Let \(C\) be a smooth integral projective curve, \(\pi:E=\mathbf P_C(N)\to C\) a smooth ruled surface, and \(a,b\) nonzero sections of invertible sheaves \(L_a,L_b\) on \(E\). In the STCI application these are the restrictions of the individually divided strict-transform equations to \(E\), i.e. their leading normal forms, with the appropriate twists. Assume their generic restrictions to \(E_\eta\cong\mathbf P^1_{k(C)}\) have a common zero over an algebraic closure.

Let \(D_a=\operatorname{div}(a)\), \(D_b=\operatorname{div}(b)\) be effective Cartier divisors on the smooth surface \(E\). Define their **divisorial gcd**
\[
D=\sum_{\Gamma\subset E}\min\{\operatorname{ord}_\Gamma(a),\operatorname{ord}_\Gamma(b)\}\,\Gamma.
\]
Write \(D=D_{\mathrm{hor}}+D_{\mathrm{vert}}\) by separating components dominating \(C\) from fiber components.

## Lemma 1: the horizontal common-direction divisor is finite flat

If \(D_{\mathrm{hor}}\ne0\), then its effective Cartier divisor structure is **finite and flat over \(C\)**. Its degree over \(C\) is the degree, with multiplicity, of the gcd of the two generic binary forms.

**Proof.** A divisor on a smooth surface is Cartier. The horizontal divisor has no fiber component. Every fiber of its support is zero-dimensional: if a fiber had a one-dimensional component, that component would be the whole irreducible fiber of the \(\mathbf P^1\)-bundle and thus a vertical component. Hence the projective map \(D_{\mathrm{hor}}\to C\) is proper and quasi-finite, so finite. The effective Cartier divisor is Cohen–Macaulay of pure dimension one; over the regular one-dimensional base its local rings are torsion-free as modules over the base DVR (the uniformizer is not contained in any associated prime). Finite torsion-free modules over a DVR are flat. The generic fiber length is constant. \(\square\)

This supplies a **canonical flat closure of the generic common-direction divisor** on \(E\), without requiring its fibers to be reduced, smooth, or étale. The scheme-theoretic intersection \(V(a,b)\), however, can be larger.

## Lemma 2: the residual common zero locus is zero-dimensional

Subtract the divisorial gcd locally, writing \(a=h a'\), \(b=h b'\) in a regular local trivialization. The residual pair \((a',b')\) has no common divisorial component. Consequently its common zero subscheme \(T=V(a',b')\) is either empty or zero-dimensional on \(E\). In particular \(T\) is supported over finitely many points of \(C\).

**Proof.** The regular local rings of the smooth surface are factorial. Taking the common prime-divisor multiplicities from both local equations leaves a pair with no common height-one prime. Any remaining common zero ideal has height at least two. As \(E\) is projective, the resulting zero-dimensional locus is finite. The residual ideal glues globally after dividing by the canonical section of \(\mathcal O_E(D)\). \(\square\)

Thus the first-symbol geometry has two **different** sources of special behavior: vertical common divisors \(D_{\mathrm{vert}}\), and residual zero-dimensional intersections \(T\). Neither is visible from the generic gcd alone.

## Example: a vertical fiber and a residual point

On an affine ruled chart with base parameter \(t\) and fiber coordinate \(z\), take
\[
a=t z,\qquad b=t(z+t).
\]
The divisorial gcd is the vertical fiber \(t=0\); after division the residual pair is \((z,z+t)\), with a residual intersection at \((t,z)=(0,0)\). Over the generic point \(t\ne0\), the two equations have no common root. This example demonstrates the separation of vertical and zero-dimensional defects, but is **not** an STCI example and does not satisfy the generic-common-factor hypothesis.

For a generic common direction and an additional residual point, take
\[
a=z(z-t),\qquad b=z(z+t).
\]
Here \(D_{\mathrm{hor}}=(z=0)\) is a flat section and the residual pair \((z-t,z+t)\) has a zero-dimensional common zero at \(t=z=0\) in characteristic different from two. The original intersection has a thicker special-point structure than the flat horizontal gcd alone.

## Relation to the actual-CI bridge

In the equal-order, everywhere-generated saturated line-relation situation of [STCI-R-0006](../results/actual_ci_smooth_root_bridge.md), both leading sections are scalar multiples of one global root form, with scalar coefficients having no common zero. Then their common zero subscheme on \(E\) is precisely the root divisor, and no vertical fiber or residual point is contributed by coefficient base points. The further **smoothness** and **full-initial-ideal** hypotheses of STCI-R-0006 are still independent.

For arbitrary actual equations, \(D_{\mathrm{hor}}\) is a useful canonical first object, but its finite flatness **does not** imply that it is the saturated first full-initial-ideal relation, that a second graded generator exists globally, or that the strict-transform intersection is primitive.

## Proposed next step (OPEN)

Compare the divisor \(D_{\mathrm{hor}}\), the vertical part \(D_{\mathrm{vert}}\), and residual scheme \(T\) with the *full* initial ideal and its saturation on \(C\). Prove a precise formula, if one exists, for how vertical and residual defects affect the intersection of the original strict-transform divisors. This requires the higher normal terms of \(F,G\): the two first symbols alone cannot determine the exceptional intersection multiplicity.

**Scope warning:** the decomposition here is on the ruled surface \(E\), not an asserted decomposition of the threefold intersection \(D_F\cap D_G\), nor a theorem excluding any STCI pair.
