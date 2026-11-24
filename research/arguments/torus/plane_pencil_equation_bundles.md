# Plane pencils and the global equation bundles

**Status:** provisional geometric comparison, not a new exclusion. The aim is to explain how the transverse families and two projective equations are related. The standard inputs are the projective bundle formula (Stacks [01OA](https://stacks.math.columbia.edu/tag/01OA), [01XX](https://stacks.math.columbia.edu/tag/01XX)), constant-rank evaluation and the Koszul resolution of a plane CI. The generator-bundle observation below is an elementary specialization to this plane pencil; no novelty in general relative CI theory is claimed. Compare the [transverse motion account](transverse_neighborhood_motion_and_conormal.md), [cycle-first synthesis](transverse_coefficient_realization_synthesis.md), [special plane sections](../curve/special_plane_and_line_sections.md), and [existing movement theorem R-0072](../../results/torus_quotient_movement_bounds.md), which already compares equations along the longitudinal torus. No extension of its sole-support bounds is asserted.

## 1. The projective completion of transverse slices

Write \(z,x,y,w=x_0,x_1,x_2,x_3\). The plane pencil through \(L_{23}\) has incidence space
\[
 P=V(sx-tz)\subset\mathbf P^3\times\mathbf P^1_{[s:t]}.
\]
This is the blowup of the base line and the plane bundle of lines in
\(E=O(-1)\oplus O^2\) over \(B=\mathbf P^1\), with projections \(\rho,p\). Let \(O_P(1)=\rho^*O_{\mathbf P^3}(1)\). Fiber coordinates can be written \([R:U:V]\mapsto[sR:tR:U:V]\), with the \(R\) coordinate transforming with the base frame. On \(s=1,t\ne0\), normalize by the longitudinal action, writing the map instead as
\[
 [R:U:V]\mapsto[R:tR:t^3U:t^4V].
\]
The moving transverse torus is the open \(RUV\ne0\) of this fixed plane.

For an actual proper CI \(Z=V(F_a,G_b)\) with full cycle \(\sum n_i[C_{u_i,v_i}]\), \(m=ab/4=\sum n_i\), the full incidence \(\Gamma=P\times_{\mathbf P^3}Z\) is a finite flat plane-CI family of length \(ab\). No plane contains any support curve, so every fiber is a proper plane CI with constant length; alternatively the relative regular sequence and flatness follow from the fiberwise flatness criterion. Over the dense base torus the normalized plane fiber decomposes as the open-and-closed union
\[
 \Gamma_t=W_t\sqcup E_t,\qquad
 \ell W_t=m,\quad\ell E_t=3m .
\]
Indeed \(sx-tz\) cuts each orbit closure in one moving point \([1:u_i:v_i]\) and three times \(p_\infty=[0:0:1]\) in the plane coordinates. Multiplicities follow by Cartier intersection on the pure CI. The moving part is the actual transverse neighborhood family, not just its cycle. The complementary part has fixed support but may have moving infinitesimal structure. It is not a residual curve of \(Z\). At \(t=0\) the two supports are still distinct; at infinity they coalesce. Do not infer that the closures are disjoint there or that their naive union recovers the entire family.

These two pieces are residual to each other in the plane CI in the standard zero-dimensional liaison sense (their ideals in the CI algebra are complementary idempotent ideals). Thus the classical Cayley--Bacharach residual duality applies on each such fiber, including thick structures. For \(k=a+b-3\) and integer \(d\),
\[
 h^0(I_{E_t}(d))-h^0(I_{\Gamma_t}(d))
 =h^1(I_{W_t}(k-d)).
\]
See Eisenbud--Green--Harris, [Cayley--Bacharach theorems and conjectures, CB7](https://doi.org/10.1090/s0273-0979-96-00666-0). This interprets the endpoint piece as a complementary part of the same projective linear systems; it is not an independent new constraint forcing any moment. The key point is to keep the entire plane family, not to assume the length-\(m\) piece itself is a plane CI of degrees \(a,b\).

## 2. A global polynomial is a section of the plane linear-system bundle

The degree-\(d\) plane equations form the bundle
\[
 V_d=p_*O_P(d)=\operatorname{Sym}^d(E^\vee)
 =\bigoplus_{j,k\ge0,\ j+k\le d} O_B(d-j-k).
\]
Set \(V_d=0\) for negative \(d\). Pullback gives the isomorphism
\[
 H^0(\mathbf P^3,O(d))\xrightarrow{\sim} H^0(B,V_d).
\]
Indeed a coefficient of \(R^{d-j-k}U^jV^k\) is a homogeneous binary form of degree \(d-j-k\) in \(s,t\), exactly the coefficient of \(y^jw^k\) in a homogeneous form in \(z,x,y,w\). In the normalized torus frame the coefficient is
\[
 t^{3j+4k}\sum_{\ell=0}^{d-j-k}c_{d-j-k-\ell,\ell,j,k}t^\ell.
\]
The degree bounds record regularity in the projective pencil; this is not an arbitrary family of plane polynomials. The torus action on the same two global equations gives the entire path of plane intersections.

## 3. The generator bundles: local plane CI versus global projective CI

Let \(\Gamma\subset P\) now be **any** finite flat family with every geometric fiber a plane CI of the same type \(a\le b\). No support hypothesis is needed for the following comparison. Let
\[
 J_d=\ker(V_d\to p_*O_\Gamma(d)).
\]
Since the fiber Hilbert functions of a fixed-type plane CI are constant, evaluation has constant rank and \(J_d\) is a subbundle whose fiber is the degree-\(d\) ideal space. This is just constant-rank linear algebra on the smooth reduced base. Use the intrinsic bundles of minimal-degree generators:
\[
 G_a=J_a,\qquad
 G_b=J_b/(V_{b-a}J_a)\quad (a<b).
\]
For \(a<b\) both are lines: multiplication \(V_{b-a}\otimes J_a\to J_b\) is fiberwise injective of constant rank by the plane polynomial domain, with one-dimensional quotient by the CI Hilbert function. For \(a=b\) use only \(G_a=J_a\), a rank-two bundle.

**Elementary global-presentation criterion (provisional proof):** the entire family \(\Gamma\) is the pullback of one proper degree-\((a,b)\) CI pair on \(\mathbf P^3\) iff the indicated minimal generator bundles are trivial.

Necessity: the two fixed global equations restrict to a basis of the fiber minimal generators (or of their degree-labeled classes); they therefore trivialize the generator bundles.

Sufficiency if \(a=b\): take a global frame of \(J_a\). If \(a<b\), choose a nowhere-zero generator of \(G_a\) and lift a nowhere-zero generator of \(G_b\) through
\[
 0\to V_{b-a}\otimes G_a\to J_b\to G_b\to0.
\]
The lift exists because \(G_a=O_B\) and all summands of \(V_{b-a}\) have nonnegative degree, so \(H^1(B,V_{b-a})=0\). The two sections give the prescribed generating pair on every plane fiber. They come from homogeneous forms on \(\mathbf P^3\) by Section 2. Their ideal equals the ideal of \(\Gamma\) on \(P\): the quotient of the latter ideal by the generated ideal vanishes on every fiber, by flatness of \(\Gamma/B\) (which identifies the fiber ideal) and Nakayama. The forms are proper on \(\mathbf P^3\), since a common surface would give a positive-dimensional intersection in a general plane of the pencil. This proves the equivalence. No claim that every moving length-\(m\) family admits the required plane-CI completion is made.

The geometric distinction is now explicit: the two local equations can twist as the plane moves. Their degree-labeled generator bundles measure this twisting; triviality means the plane equations can be chosen as one global pair. The larger conormal graph describes the differentials of those same equations, and its equation bundle is obtained from the global degree-labeled generators when this triviality holds. This is stronger information than merely having fiberwise normal planes or conormal compatibility. It is an exact comparison for the entire plane family, not a criterion involving only its cycle or the moving part.

For an actual pair, the ideal bundle of the full plane family has the familiar degree-wise sequence
\[
 0\to V_{d-a-b}\to V_{d-a}\oplus V_{d-b}\to J_d\to0,
\]
from the relative Koszul resolution and \(R^1p_*O_P(j)=0\) for all \(j\). It displays the global source as a degree-labeled linear-system family. There is no need to reconstruct independent equations in each transverse chart.

## 4. What to compare next

The constructive realization question now has two geometric parts: complete the moving transverse neighborhoods to the full plane-CI family by the endpoint-supported part, and understand whether its minimal equation bundles are trivial. The opposite pencil through \(L_{01}\) supplies the complementary observation of the same global equations. Its base parameter \(t^-=q/t\) differs by a transverse character, so do not identify the full plane fibers of the two pencils over a single common base; compare their incidence maps to projective space.

This is a way to organize the previously studied quotient, normal graph, Chow restrictions and endpoint contraction without reducing them to an obstruction. The criterion is conditional on fixed-type plane-CI fibers at **all** base points, and says nothing by itself about existence of such a completion or triviality of its equation bundles. No first-moment theorem or new STCI coverage is asserted. Independent review of the new synthesis remains outstanding.
