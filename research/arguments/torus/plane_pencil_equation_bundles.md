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


## 5. Transition functions: the spectral framing and the equation bundles

The opposite longitudinal parameter satisfies \(t^-=q/t\). On the moving rank-\(m\) algebra let \(\Phi=\mu_q\). Multiplication by \(t^-\) in the original \(t\)-frame has determinant \(t^{-m}\det\Phi=t^{-m}\prod_i q_i^{n_i}\). This is a norm of a coordinate relation, **not** an identification of the two different plane-family base projections or a transition matrix for the minimal equation bundles. The natural additive invariant occurs instead in the first boundary jet of the spectral determinant:
\[
 \det(1-\epsilon\Phi)=\prod_i(1-\epsilon q_i)^{n_i}
 \equiv1-\epsilon M_1\pmod{\epsilon^2}.
\]
Here \(\epsilon\) is the inverse coordinate at infinity on the spectral projective line, not the longitudinal parameter. The [already-reviewed spectral boundary modulus](spectral_boundary_modulus.md) identifies this with the rigidified line bundle of the divisor \(D_q-m[0]\) in \(\operatorname{Pic}(\mathbf P^1,2\infty)\); its underlying line bundle is always trivial. Thus \(M_1=0\) is exactly first-order **framed** triviality of that line, not ordinary triviality of the equation bundles.

The latter bundles have their own transition matrices. For \(a=b\), local frames of \(J_a\) are related by a rank-two transition matrix. For \(a<b\) there are scalar transitions for the two minimal equation lines, and lifting the higher-degree generator introduces the addition of a degree-\((b-a)\) multiple of the lower one. These are the graded changes of generators, not changes of the transverse spectral coordinates. The standard Birkhoff--Grothendieck theorem (algebraic bundles on \(\mathbf P^1\)) reduces ordinary triviality to vanishing of all splitting degrees. Even triviality of the determinant is insufficient in rank two, as \(O(1)\oplus O(-1)\) shows.

There is nevertheless an actual comparison through evaluation. For \(d\ge a+b-2\), the relative plane-CI Hilbert function gives a surjection \(V_d\to p_*O_\Gamma(d)\), hence
\[
 \det J_d=\det V_d\otimes(\det p_*O_\Gamma(d))^{-1}.
\]
Over the open base on which \(\Gamma=W\sqcup E\), the last determinant factors as \(\det p_*O_W(d)\otimes\det p_*O_E(d)\). Thus changes of evaluation frames on the moving and endpoint-supported neighborhoods contribute jointly to the transition of the equation spaces. The low-degree generator transitions can be recovered from \(J_a,J_b\); for \(a<b\),
\[
 \det J_b=\det V_{b-a}\otimes G_a^{\otimes\operatorname{rk} V_{b-a}}\otimes G_b.
\]
In equal degrees \(J_a\) itself is the generator bundle. The geometric task is to relate the marked spectral determinant transition to these actual equation transitions, including the endpoint-supported evaluation factor and changes of frame. No canonical identification has yet been established.

### Balanced cycle does not trivialize arbitrary fixed-type plane completions

Even requiring all fibers to be plane CIs with the specified dense-torus cycle and endpoint multiplicity is insufficient in general. An illustrative type \((1,8)\) completion has \(m=2\). Choose two curves \(C_{u,1},C_{u,-1}\), \(u\ne0\), in characteristic zero, so \(M_1=u-u=0\). In the plane bundle of Section 1 use unscaled fiber coordinates \([R:Y:W]\mapsto[sR:tR:Y:W]\). The relative line
\[
 s^2Y-u t^3R=0
\]
is a nowhere-zero family of linear equations: its coefficients define the injection \(O(-2)\to V_1=O(1)\oplus O^2\) with entries \((-u t^3,s^2,0)\). Its zero surface is a smooth ruled surface over the base (projectivization of the rank-two kernel of the corresponding everywhere-surjective map \(E\to O(2)\)). On this surface the two orbit sections \([R:Y:W]=[s^3:u st^3:\pm t^4]\) and the fixed section \([0:0:1]\) exist at every base point. Take the relative effective Cartier divisor consisting of the sum of the first two sections and six times the fixed section. By standard relative divisor theory (Stacks [44.3.2](https://stacks.math.columbia.edu/tag/0B9E)) it is finite flat of degree eight. Each fiber is a degree-eight divisor on a line, hence is a plane CI of type \((1,8)\), including the endpoints where sections collide. On the dense base it has exactly the desired two moving points and a length-six endpoint piece. Its minimal linear equation bundle is \(G_1=O(-2)\), not trivial. The example is a relative plane family, **not** an actual projective CI, and is in low degrees; it does not rule out a stronger statement for a more constrained canonical completion or a narrower degree range. It shows why the spectral determinant alone is not sufficient for the general equation-bundle criterion.

There is also a prior example at type \((4,4)\) of a balanced reduced configuration that does not admit a global pair (same-u fourth-root cycle in the [coefficient synthesis](transverse_coefficient_realization_synthesis.md#what-the-spectrum-can-and-cannot-encode)). This excludes a blanket claim of sufficiency from the first moment alone without requiring the above relative completion. The positive question remains: is there a geometrically distinguished completion or a marked determinant comparison in which the residual transition is exactly the spectral first jet? Preserve the distinction between this question and universal UM1. The new relative example and transition comparisons are provisional pending independent review.


## 6. An actual equation-side transition: the Koszul cofactor torsor

The [established first-jet residue formula](spectral_jacobian_first_jet_bridge.md#4-the-first-moment-is-a-perfect-residue-pairing-of-first-jets) supplies an exact equation-side geometric interpretation of the marked spectral scalar. Work in characteristic zero, with an actual proper homogeneous CI \(Z=V(F_a,G_b)\) whose entire cycle is translated quartics. Let \(L=V(z,w)\) be the disjoint projection line, write
\[
 F=f+zp+wq'+\cdots,\qquad G=g+zr+ws+\cdots,\qquad P=ps-q'r.
\]
Here \(r,s\) in the jet expansion denote coefficients, not longitudinal parameters. The twisted Koszul sequence on \(L\) is
\[
 0\to O_L(-2)\xrightarrow{(-g,f)}
 O_L(b-2)\oplus O_L(a-2)\xrightarrow{(f,g)}O_L(a+b-2)\to0 .
\]
Use the coordinate identification \(O_L(-2)\simeq\omega_L\) and the ordered Koszul orientation from the residue proof. The sheaf of cofactor presentations of \(P\) is the torsor of lifts of this section through the last surjection. On \(D(f),D(g)\), choose \((P/f,0),(0,P/g)\). Their difference is \(P(-g,f)/(fg)\). Thus the translation cocycle in the kernel, expressed as a differential, is
\[
 \gamma_{fg}=\frac{P}{fg}(x\,dy-y\,dx).
\]
The order of the Cech cover and the identification of the kernel with \(\omega_L\) are taken consistently with the Serre-trace orientation. The class is the connecting image \(\delta(P)\). The standard classification of additive sheaf torsors by \(H^1\) ([Stacks 20.4](https://stacks.math.columbia.edu/tag/02FN)) gives the geometric interpretation. With the normalized Serre-trace generator represented by the logarithmic cocycle \(d\xi/\xi\), \(\xi=y/x\), one has
\[
 [\gamma_{fg}]=2M_1[d\xi/\xi],\qquad
 M_1=0\iff \text{the cofactor torsor is trivial}.
\]
When it is trivial its global section is unique, since \(H^0(L,\omega_L)=0\). This is an interpretation of the existing equality, not a new proof of vanishing. The class is constructed from the actual normal equation jets, not independently prescribed from the cycle.

There is also a natural multiplicative version. Let \(L^{(1)}\) be the first infinitesimal neighborhood of the zero section in the total space of \(T_L\); its algebra over \(L\) is \(O_L\oplus\omega_L\), with square-zero second summand. The unit subgroup \(1+\omega_L\) identifies with the additive sheaf \(\omega_L\). Glue a line bundle on \(L^{(1)}\), trivialized on \(L\), by \(1+\gamma_{fg}\). Its isomorphism class lies in the kernel of \(\operatorname{Pic}(L^{(1)})\to\operatorname{Pic}(L)\), canonically \(H^1(L,\omega_L)\) by the split unit sequence. In standard charts its cocycle class is represented by \(1+2M_1 d\xi/\xi\), where the differential denotes a square-zero ideal section. The line is trivial precisely when \(M_1=0\). Equivalently, pull the Koszul sequence back along \(P:O_L\to O_L(a+b-2)\) to obtain an extension of \(O_L\) by \(\omega_L\); its splitting is the same condition. Do not call the underlying rank-two extension bundle trivial when the extension splits: it then equals \(O\oplus O(-2)\). These are standard geometric realizations of the cohomology class. The split ribbon is a natural auxiliary scheme, not an assertion that it is the first neighborhood of \(L\) in \(\mathbf P^3\).

## 7. Why the longitudinal logarithmic form is the same scalar

Use the actual finite flat projection \(\pi:Z\to B=\mathbf P^1_{[z:w]}\), disjoint from \(L\), of degree \(4m\). Put \(R=w/z\), \(D_B=[0]+[\infty]\), \(D_Z=\pi^*D_B\), and \(\mathcal A=\pi_*O_Z\). Here \(D_Z\) is the full Cartier endpoint divisor, not just the reduced points. Finite duality and adjunction give
\[
 \pi_*\omega_Z(D_Z)=\mathcal A^\vee\otimes\omega_B(D_B),
 \qquad \omega_Z(D_Z)=O_Z(a+b-2).
\]
The duality trace of a functional is evaluation at \(1\) (Stacks [49.15](https://stacks.math.columbia.edu/tag/0DWM), [48.20](https://stacks.math.columbia.edu/tag/0AU5)). On the punctured base the functional \(\lambda_q(h)=\operatorname{Tr}_{\mathcal A/O_B}(qh)\) gives the section \(\lambda_q\,dR/R\). The [spectral--Jacobian identity](spectral_jacobian_first_jet_bridge.md) and relative Jacobian trace formula extend \(\lambda_q\) as a section of \(\mathcal A^\vee\) over the endpoints, even when \(q\) is not itself regular there. In the adjunction convention the homogeneous expression
\[
 \omega=(x\,dy-y\,dx)/(zw)
\]
under the fundamental-class map is \(\frac12\lambda_q\,dR/R\): the relative Jacobian corresponds to the multiplication trace, and \(qD_{12}=2D_{03}\). On each reduced normalization \(R=v_i t^4\), so \(dR/R=4dt/t\) and its weighted branch expression is \(2n_i q_i\,dt/t\). The fundamental-class interpretation is essential for nonreduced schemes; no ordinary differential on the reduction is being identified with the full dualizing sheaf.

The finite duality trace therefore gives exactly
\[
 \operatorname{Tr}^{\mathrm{dual}}_\pi(\omega)
 =\frac12\lambda_q(1)\frac{dR}{R}
 =2M_1\frac{dR}{R}.
\]
Consequently its logarithmic coefficient at zero agrees with the Serre trace of the actual cofactor torsor on \(L\), and its coefficient at infinity is opposite. The ordinary residue theorem does not force either individually to vanish. The [centered-section account](transverse_coefficient_realization_synthesis.md#centered-differential-and-scalar-part-of-the-spectrum) already proves that \(\omega\) is regular iff \(M_1=0\) for these actual CIs, a stronger statement than just taking its aggregate trace.

On the same punctured base the first-order norm is
\[
 \operatorname{Nm}_{\pi}(1-\epsilon q)
 =1-\epsilon\lambda_q(1)=1-4M_1\epsilon\quad(\epsilon^2=0).
\]
On the separated rank-\(m\) longitudinal algebra it is \(1-M_1\epsilon\) instead. This is the usual determinant/trace relation for finite locally free norms ([Stacks 31.18.6](https://stacks.math.columbia.edu/tag/0BD2)). It agrees with the first jet of the already-reviewed spectral framing in Section 5. Thus the norm, longitudinal log coefficient and actual cofactor transition all compute the same scalar with their known factors of 4 and 2. The three bases (spectral line, longitudinal projection line and disjoint center line) remain distinct. The comparison uses their canonical trace coordinates, not an identification of their vector bundles or their local transition functions.

**Geometric consequence and limitation.** We now have a line whose triviality detects the sum and whose cocycle comes directly from actual equations. This answers the marked-transition question for the first-jet cofactor presentation. It does not identify this line with either minimal generator bundle of Section 3, and those generator bundles are already trivial for an actual global pair. The remaining meaningful comparison is to understand whether the cofactor framing is induced by the same global degree-labeled presentation through the opposite pencil and its endpoint geometry, or is extra information independent of ordinary generation. The torsor and ribbon interpretations use standard cohomology; the comparisons are a provisional synthesis of existing identities, pending independent review, not new UM1 coverage.
