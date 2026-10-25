# Deformation laboratory for complete intersections through the fixed quartic

Date: 2026-10-25. Status: exploratory contribution to the [main notebook](2026-10-25-ci-cycle-geometry-notebook.md). New calculations below are provisional research evidence; no canonical theorem or frontier record changes. The elementary calculations have reproducible scripts; the [independent audit](2026-10-25-ci-cycle-exploration-audit.md) separately reconstructs the deformation argument and exact global-source differential rank.

Throughout the main discussion, \(k\) is algebraically closed of characteristic zero,

\[
C=[s^4:s^3t:st^3:t^4],\quad
F=x_1^4-x_0^3x_3,\quad G=x_2^4-x_0x_3^3,
\quad Z=V(F,G).
\]

Write \(p=[1:0:0:0]\) and \(q=[0:0:0:1]\).

The question is how complete intersections containing the *fixed embedded curve* \(C\) can move, and how much of their geometry is recorded by their attachment to \(C\). It is not an STCI question.

The accepted premise [STCI-R-0021](../results/quartic_mu4_degeneration.md) identifies the four components of this prescribed \(Z\), its two endpoints, its flat integral model, and its characteristic-two collapse. Its linked source note supplies the local endpoint equation and boundary \(9p+9q\). [STCI-R-0020](../results/quartic_conormal_characteristic_jump.md) supplies the characteristic-zero splitting \(N^*_{C/\mathbf P^3}=\mathcal O_{\mathbf P^1}(-7)^2\). These records have their stated fixed-curve scopes. The argument here uses no carrier exclusion.

## 1. A simple parameter space with room to move

Put

\[
V=H^0(\mathbf P^3,I_C(4)).
\]

A quartic vanishing on the reduced curve vanishes scheme-theoretically on \(C\); thus this space parametrizes all quartic equations relevant to the fixed-\(C\) question. Restricting degree-four monomials to \(C\) gives all binary monomials of degree 16, so

\[
\dim V=35-17=18.
\]

This is also visible in the accepted quartic-symbol computation. Ordered independent equations form an open set in \(V^2\); after removing their choice of basis, the natural parameter space is

\[
\operatorname{Gr}(2,V)=\operatorname{Gr}(2,18),\qquad\dim=32.
\]

Remove the closed locus of pencils with a common surface component. On the resulting open set \(U\), every pair is a regular sequence and has the Koszul resolution of a \((4,4)\) complete intersection. The universal family is flat, with

\[
P_Z(n)=16n-32,\qquad p_a(Z)=33,\qquad\omega_Z\simeq\mathcal O_Z(4).
\]

Thus there is one irreducible local laboratory containing the distinguished configuration and many other configurations, even before allowing different equation degrees. The flat-family/Hilbert-scheme interpretation is standard; compare [Stacks, fixed Hilbert polynomial](https://stacks.math.columbia.edu/tag/0DNF). None of this means reduced support or normalization is constant.

A basis-free pencil parametrization matters: a path of ordered pairs obtained by an invertible linear recombination can look like a deformation while defining the identical curve. Passing to the Grassmannian removes that redundancy.

## 2. The generic picture: the four quartics can become \(C\) plus one genus 16 curve

A useful comparison configuration is

\[
Z_{\mathrm{gen}}=C\cup D,\qquad
\deg D=12,\quad g(D)=16,
\]

with \(D\) smooth and connected, meeting \(C\) transversely at 18 distinct points. This is the general picture in \(U\), rather than an assertion about every pair or every subfamily with fixed boundary.

Here is a compact geometric justification, also explaining why the general residual curve can be smooth. The ideal sheaf is generated in degrees at most 3, with equations

\[
Q=x_0x_3-x_1x_2,\quad
A=x_1^3-x_0^2x_2,\quad
B=x_0x_2^2-x_1^2x_3,\quad
D_3=x_2^3-x_1x_3^2.
\]

The accompanying Macaulay2 experiment checks that these generate the actual ideal. Hence \(I_C(3)\) is globally generated and \(h^0(I_C(3))=20-13=7\). On the smooth blowup \(B_C=\operatorname{Bl}_C\mathbf P^3\), write \(H\) for the pulled back hyperplane and \(E\) for the exceptional divisor. The graph construction embeds \(B_C\) into \(\mathbf P^3\times\mathbf P^6\) using \(H\) and \(3H-E\); the Segre polarization is \(4H-E\). In particular \(4H-E\) is very ample. Two general members therefore intersect in a smooth irreducible curve upstairs. Standard ingredients are the [Rees-algebra construction of the blowup](https://stacks.math.columbia.edu/tag/01OF), [Bertini smoothness](https://stacks.math.columbia.edu/tag/0FD4), and [Bertini irreducibility](https://stacks.math.columbia.edu/tag/0G4C).

The determinant calculation in the next section shows that a general pair has 18 simple attachment points on \(C\). Upstairs the residual curve crosses \(E\) at one point above each. Blowing down preserves smoothness at such a transverse crossing, and produces a transverse node with \(C\). This gives the claimed generic picture. This explanation is a new unpromoted geometric deduction, not a claim copied from a canonical record.

For the numerical values, work on a smooth quartic surface \(S\) containing \(C\). Adjunction gives \(K_S=0\) and \(C^2=-2\). The residual divisor class is

\[
D\sim4H-C,\qquad H^2=4,\quad H\cdot C=4.
\]

Consequently

\[
H\cdot D=12,\qquad D^2=30,\qquad p_a(D)=16,
\qquad C\cdot D=18.
\]

The genus bookkeeping is transparent:

\[
p_a(C\cup D)=0+16+18-1=33.
\]

At the distinguished point, \(D=C_{-1}\cup C_i\cup C_{-i}\) is three rational quartics. Its two endpoint singularities each have delta invariant 9, giving

\[
p_a(D)=18-3+1=16.
\]

So the residual genus 16 can migrate from singular gluing into the genus of one smooth component. The total arithmetic genus does not choose between these pictures. A normalization-based measure would see a dramatic change.

Over \(\mathbf C\), the generic nodal union has first Betti number \(2\cdot16+17=49\): the dual graph has two vertices and 18 edges. The distinguished reduced union has four spheres joined at two points, with incidence graph of first Betti number 3. These are different underlying topological curves in one flat family. The apparent loss of topology at the special fiber is carried by its more severe singularities, not a failure of flatness.

## 3. The attachment-divisor map is locally flexible even at \(Z\)

The first-normal parts of a pencil give a determinant section

\[
\det\bigl(N^*_{C/\mathbf P^3}(4)\bigr)
=\mathcal O_{\mathbf P^1}(18).
\]

When that section is nonzero, its zero divisor is an attachment diagnostic. On the reduced residual-component locus it is the intersection divisor \(C\cap D\), including intersection multiplicities. This defines a rational map, regular near the distinguished characteristic-zero point,

\[
\beta:U\dashrightarrow
\mathbf P H^0(\mathbf P^1,\mathcal O(18))
\simeq\operatorname{Sym}^{18}\mathbf P^1.
\]

The point \(Z\) maps to \(9p+9q\). The target has dimension 18.

**New calculation.** The differential of \(\beta\) at \(\langle F,G\rangle\) is surjective. Its tangent kernel therefore has dimension 14. This is stronger than the observation that some perturbations split endpoint contact: every infinitesimal degree 18 divisor direction is available through actual global quartics at this very pencil.

Use \(x_0=1\), \(u=x_1\), \(X=x_3-u^4\), \(Y=x_2-u^3\). Write a first-normal section as \(A(u)X+B(u)Y\). The two fixed equations have symbols

\[
f=(-1,0),\qquad g=(-3u^8,4u^9).
\]

For actual quartic perturbations \(h,k\in V\), the affine determinant derivative is

\[
\delta\det=4u^9A_h+3u^8B_h-B_k.
\]

The \(k\)-terms span \(1,u,\ldots,u^{10}\); the \(h\)-terms span \(u^8,\ldots,u^{18}\). Together they span all 19 coefficients. The reproducible Python script constructs an integral basis of \(V\) from differences of homogeneous monomials of equal parameter weight and verifies these ranks over \(\mathbf Q\). In particular it respects global \(k\)-coefficient constraints. It does not replace \(V\) by arbitrary \(k(C)\)-valued sections.

After quotienting the scalar determinant direction and the changes of basis of the pencil, the projective differential has rank 18. In characteristic zero this also gives the usual local smoothness interpretation: arbitrary sufficiently small formal/analytic movements of the boundary lift locally to movements of the pair. This is not a statement that every global degree 18 divisor has already been realized, nor a classification of the 14-dimensional fibers.

The striking research implication is that the endpoint concentration is not infinitesimally locked into the complete-intersection equations. It is a highly special divisor configuration inside a locally full-dimensional boundary space.

## 4. One visible perturbation: dissolve one endpoint bouquet

Keep \(F\) fixed and move only the other equation:

\[
G_\lambda=G+\lambda Qx_0^2.
\]

This is a global homogeneous quartic family containing \(C\). Since \(F\) is irreducible and the equations have equal degree without being proportional, it is a proper complete intersection for every \(\lambda\), and the constant Koszul resolution gives a flat family.

On the preceding affine chart \(F=0\) sets \(X=0\), and the actual second equation factors as

\[
G_\lambda|_{F=0}
=Y\left(Y^3+4u^3Y^2+6u^6Y+4u^9-\lambda u\right).
\]

For \(\lambda\ne0\), its residual curve is smooth at \(p\): its local equation has nonzero \(u\)-derivative \(-\lambda\). It meets \(C=(Y=0)\) transversely there. The attachment divisor becomes

\[
\operatorname{div}(s^9t(4t^8-\lambda s^8))
=9q+p+\sum_{u^8=\lambda/4}[u].
\]

The eight displayed finite points are distinct in characteristic zero. Thus nine units of endpoint contact unfold into one retained simple intersection plus eight mobile simple intersections. The opposite endpoint retains multiplicity 9 because \(F\) remains fixed. This asymmetric family is useful precisely because every feature is visible in one polynomial. It is not claimed to have globally smooth residual curve: the other endpoint is deliberately constrained.

At \(\lambda=1\), a finite Macaulay2 check computes the saturated residual by the actual colon ideal, finds degree 12 and Hilbert polynomial \(12n-15\), and checks length 18 of its attachment scheme to \(C\). These are finite coordinate checks, not a smoothness or irreducibility certification.

## 5. What the 14-dimensional boundary fiber hides

Surjective boundary differential leaves considerable room for equations to change while the attachment divisor stays \(9p+9q\). This is promising for comparing different sorts of proximity, but dangerous if one treats the divisor as a complete invariant.

For example, adding a multiple of \(Q^2\) to \(G\) changes no first-normal section at all. With \(F\) fixed, the residual local equation becomes

\[
Y^3+4u^3Y^2+(6u^6+\lambda u^2)Y+4u^9=0.
\]

It is still singular at \(p\). Thus a deformation invisible to the attachment divisor can change higher contact, yet need not release the endpoint singularity. One must calculate those higher terms rather than assuming that a generic member of a fixed-boundary fiber has a smooth residual branch with order 9 tangency. That is an experiment still to do.

The complementary root-pencil experiment in the main notebook keeps a four-quartic arrangement while varying its residual cross-ratio and occasionally its component multiplicities. Together these suggest that \(\beta^{-1}(9p+9q)\) has interesting internal strata: symmetry, branch count, normalization genus, tangency trees, and nonreduced components can vary even when the boundary divisor does not.

A useful next computation would choose a local 14-parameter slice to this fiber at \(Z\), compute jets of the two endpoint residual equations, and determine which branch-splitting and smoothing directions actually occur. This is a finite geometry experiment before any global extremality claim.

## 6. Experiments worth doing next

1. **Boundary lifting beyond first order.** Pick a one-parameter binary form splitting all 18 zeros, lift its first jet using the rank calculation, and solve successively for actual global quartics. The local smoothness calculation predicts no formal obstruction at \(Z\); an explicit low-degree lift would make the geometry visible.
2. **One verified generic residual.** Choose a reproducible rational pair near \(F,G\), compute its residual ideal, and check smoothness and irreducibility globally. The Bertini argument predicts the outcome; an example would provide a useful picture and numerical companion.
3. **Topology inside a boundary fiber.** Follow a family with fixed \(9p+9q\), compute endpoint Puiseux data, and compare residual normalization genus. The determinant alone cannot answer this.
4. **Blowup intersection picture.** Draw the moving 18 points on the exceptional ruled surface, including their positions within its fibers. Their projection to \(C\) is \(\beta\); their fiber coordinates and higher neighborhoods retain information lost by the divisor.
5. **Characteristic-two comparison.** Repeat the differential calculation after reduction, remembering that the determinant of the prescribed pair is then identically zero. The characteristic-zero boundary map does not extend to a degree 18 effective divisor at that point by merely substituting \(2=0\). One should retain the two-row normal map or its Fitting ideal before taking determinants.

## Reproducible evidence and review scope

Run from the repository root:

```sh
python3 research/computations/explore_ci_contact_deformations_2026_10_25.py
/opt/homebrew/bin/M2 --script research/computations/explore_ci_residual_pencil_2026_10_25.m2
```

The Python script checks the exact rational differential ranks, its support decomposition, and the displayed boundary of the asymmetric pencil. The Macaulay2 script checks the actual ideal generators, residual Hilbert polynomials, and one attachment length. Both passed on 2026-10-25. They do not classify all pencils, analyze every fixed-boundary fiber, or promote these observations.

The [independent audit](2026-10-25-ci-cycle-exploration-audit.md) reconstructs the generic-smooth-residual explanation, determinant-map interpretation, and local-smoothness inference. They remain exploratory and unpromoted. There is no canonical authority gap for the prescribed four-component family itself: it is covered by STCI-R-0021. There is an authority distinction for the present deductions: these are exploratory unpromoted notes. No accepted mathematics is edited and no unrestricted frontier question changes.
