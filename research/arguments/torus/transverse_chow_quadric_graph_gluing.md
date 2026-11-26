# Quadric graph sections, endpoint residues, and global gluing

**Status.** Provisional calculations in characteristic zero, using the
[coefficient realization notation](transverse_coefficient_realization_synthesis.md).
The [product models](transverse_chow_product_models.md) define the
complementary projections and logarithmic coordinates. The
[trace investigation](../../investigations/trace-residue-projection-geometry/index.md)
gives complementary checks on endpoint responses for an actual pair.

The remaining proof audit should compare the full corner section schemes,
the finite-duality identifications and residue signs, and the first
conductor layer for nonreduced sections under the opposite parameter.
Global reciprocity gives one relation between the two endpoint residues.
Deriving separate vanishing for the distinguished uncentered section
requires an additional condition on the actual equations.

### Minimal weighted logarithmic comparison for the first moment

For this scalar the full nonreduced conormal module is unnecessary. Work with the normalized reduced graphs and their generic multiplicities \(n_i\). The same rational differential in the independent products is
\[
 \theta=q\,d\log r
 =\frac ab\,d\log a
 =\frac de\,d\log r
 =\frac{r^2h}{p}\,d\log r .
\]
Its weighted branch tuple is \((n_iq_i\,dr/r)_i\). For any of the six elementary coordinate projections, the restriction to the normalization of a branch is \(T=c_i r^k\), with \(k=1,3,4,2,3,1\) respectively. In characteristic zero its function-field differential trace sends \(q_i\,dr/r=(q_i/k)dT/T\) to \(q_i\,dT/T\): the separable extension has degree \(k\). Thus all six weighted traces are \(M_1\,dT/T\). This comparison uses only the cycle, not its scheme structure or a putative finite morphism on the original projective curve at a base point.

By Rosenlicht's residue criterion for a reduced curve (e.g. https://doi.org/10.1007/s11565-024-00495-8), a tuple with at most simple poles is regular dualizing precisely when the coefficients sum to zero at each group of branches meeting at a point. In the three independent product models I, II, III, all reduced graphs meet at the same two corners, and do not meet away from them. Thus regularity of this weighted tuple in any one of the three is equivalent to regularity in all three, equivalent to \(M_1=0\). Intersecting those particular regularity conditions gives no stronger first-moment equation. In the fixed-quadric product \((r,B,q)\), however, different values of \(q\) are separated at the endpoints. The sums at the corners of the \(q=c\) slice are \(\pm c\sum_{q_i=c} n_i\). They are nonzero in characteristic zero whenever that slice occurs. Regularity on the separated model would therefore be too strong even for balanced realizations. The relevant phenomenon is cancellation under contraction, not ordinary pullback regularity across all exceptional divisors. Dualizing pushforward/trace, rather than an assumed pullback of regular dualizing forms, is the appropriate direction. This distinction concerns weighted simple-pole tuples on reduced supports, and finite duality supplies the interpretation on any realizing CM thickening as in the [common logarithmic geometry](transverse_chow_product_models.md#the-common-logarithmic-differential-geometry).

All the monomial transitions and the graph defining equations are compatible for the single graph \(C_{u,v}\), where \(M_1=q\ne0\). In particular these transitions alone do not force regularity of the weighted tuple. Even the two homogeneous equations \(z^2y-u x^3,\ z^3w-vx^4\) define that graph on the dense torus; their projective intersection also contains the coordinate line \(z=x=0\) (residual cycle degree eight by Bezout, since on \(z\ne0\) the intersection is the reduced quartic chart). They are not a proper realization of the sole graph as the entire cycle. The minimal outstanding implication is from actual global proper two-equation realization without boundary or other residual cycles to the weighted residue cancellation at a single contracted endpoint. This is the known UM1 gap, not a new theorem; no thick-structure classification is required to state or check that target. Conversely one cannot infer it from the weighted cycle alone. Provisional pending review.


### Degree exhaustion in the fixed-quadric product

The equality \(ab=4m\) gives a particularly elementary form of the complete-cycle hypothesis. On a nonspectral nonzero quadric, the restrictions of \(F_a,G_b\) have bidegrees \((a,a),(b,b)\), and their intersection number \(2ab=8m\) is exhausted by the two corner lengths \(ab\) each. On the product over \(\mathbf G_{m,q}\), the intersection cycle of these restrictions (viewed as divisors of the threefold) consists precisely of the graph cycles with weights \(n_i\) and the two constant corner sections with coefficients \(ab\). Indeed away from the four base edges of the quadric pencil the map to projective space is locally an isomorphism, and along the edges the original CI meets only the two endpoints; the generic transverse slice gives the corner coefficients. This cycle statement does not prescribe the schemes along those sections.

Fix a general \(A\ne0,\infty\). Compactifying its slice to \(\mathbf P^1_B\times\mathbf P^1_q\), the inverse rational map in homogeneous coordinates is
\[
 [z:x:y:w]=[Q_0B_0:Q_0AB_0:Q_0B_1:Q_1AB_1].
\]
The two substituted forms have bidegrees \((a,a),(b,b)\). Their binary resultant in \(B\) is homogeneous of degree \(2ab\) in \([Q_0:Q_1]\). It is nonzero at \(Q_1=0\), since the resulting joining line in the plane \(w=0\) misses \(Z\). For nonzero finite \(q\), each graph meets the slice once, and multiplicativity of the [Chow/resultant identity](transverse_chow_product_models.md#4-three-segre-surfaces-in-gr24) gives the roots \(q_i\) with multiplicities \(n_i\). The remaining root is \(q=0\), where there is a common collapsed boundary fiber. Consequently with monic normalization in the affine parameter \(q\),
\[
 R_A(q)=q^{2ab-m}H(q)=q^{7m}H(q),\qquad H(q)=\prod_i(q-q_i)^{n_i}.
\]
Fixing a general \(B\ne0,\infty\) instead gives the symmetric substitution \([Q_0 A_0:Q_0 A_1:Q_0 B A_0:Q_1 B A_1]\); each graph meets the slice three times in characteristic zero. The analogous resultant in \(A\) is
\[
 R_B(q)=q^{2ab-3m}H(q)^3=q^{5m}H(q)^3 .
\]
This is exactly the already-proved pair of ruling Chow restrictions, read with the homogenizing factors of the product model. The normalization is separately by the nonzero value at infinity. Neither resultant degree is the length of the moving zero-dimensional scheme alone, because the degenerate quadric contributes a common boundary fiber.

The first subleading coefficients are \(-M_1\) and \(-3M_1\) respectively. Degree exhaustion fixes the large root multiplicities at zero, and fixes the degrees of the remaining factors, but imposes no vanishing of the subleading coefficient by itself. In particular both monic factorizations are algebraically consistent for arbitrary monic \(H\) of degree \(m\) with nonzero constant term. The genuine remaining question is whether being the two resultant presentations of the **same global pair** implies the vanishing of that coefficient, in addition to the already automatic relation \(R_A^3=q^{16m}R_B\). This recovers the existing Chow/first-jet gate in a simple product/Bezout picture; no new independent moment condition follows. Provisional synthesis.


### Complete corner sections and the explicit logarithmic lift

Use the actual compact graph of the quadric pencil (rather than naively homogenizing the inverse Segre product, which has extra base loci):
\[
 X=V(Q_1xy-Q_0zw)\subset\mathbf P^3\times\mathbf P^1_Q,\qquad
 Y=X\times_{\mathbf P^3} Z,\quad Z=V(F_a,G_b),\quad q=Q_0/Q_1 .
\]
The pencil graph construction is classical (SGA 7, XVIII.3, https://grothendiecksga.com/read/sga7/en/18-3.html). The following comparison uses only adjunction, the cohomology of the projective line, finite duality for the inclusion of a reduced curve in a CM curve (Stacks, https://stacks.math.columbia.edu/tag/0E31 and Duality for Schemes, closed-immersion duality), and Rosenlicht's criterion (Altman--Kleiman VIII.1.16; see https://doi.org/10.1007/s11565-024-00495-8). These are standard inputs; there is no new universal moment vanishing.

The equation of \(Y\) is a nonzerodivisor on \(Z\times\mathbf P^1\), since it is nonzero generically on every surface component \(C_i\times\mathbf P^1\) and that product is CM. Thus \(Y\) is a pure lci curve, and is the proper intersection of the two pulled-back divisors in \(X\). The full inverse image, not merely the closure of the torus intersection, has cycle
\[
 [Y]=\sum_i n_i[\Gamma_i]+ab[E_0]+ab[E_\infty],
 \qquad \Gamma_i=C_i\times\{q_i\},\quad E_j=\{p_j\}\times\mathbf P^1 .
\]
There are no other components: away from \(p_0,p_\infty\) the pencil is defined on the given support; over those points its fibers are complete projective lines. At a generic nonspectral \(q\), each corner length is \(4m=ab\) by intersecting the original cycle with \(Q_q\). This uses the entire-cycle hypothesis, not just containment.

On the normalization of the reduced union \(Y_{\rm red}\), prescribe
\[
 \theta_i=n_iq_i\,dr/r,\qquad
 \theta_0=\left(m-qH'(q)/H(q)\right)dq
       =-\sum_i\frac{n_iq_i}{q-q_i}dq,\qquad
 \theta_\infty=-\theta_0 .
\]
The two corner forms have exactly the negative of the moving-component residue sums at each spectral attachment, even when several graphs have the same \(q\). At any such point a regular function has the same value on all incident branches, so the simple-pole tuple satisfies the full Rosenlicht criterion, independently of contact orders. It is regular at \(q=0\); at \(q=\infty\) the two residues are \(+M_1,-M_1\). Thus writing \(D_\infty=Y\cap\{Q_1=0\}\), an effective Cartier divisor (no component of \(Y\) lies in that fiber), this constructs a section of \(\omega_{Y_{\rm red}}(D_\infty|_{Y_{\rm red}})\). Finite duality identifies it with a section of \(\omega_Y(D_\infty)\) annihilated by the nilradical. The corner differential is determined uniquely among forms with at most simple poles at the attachments and at infinity and no other poles, since a regular differential on \(\mathbf P^1\) is zero. The prescribed weights are already the fundamental-class branch weights; do not multiply the corner coefficients by \(ab\) again after embedding the reduced dualizing sheaf into the full one.

This lift can be identified directly with the actual global equation presentation. Put \(\pi:Y\to Z\). The exact sequence on \(Z\times\mathbf P^1\) is
\[
 0\to O_Z(-2)\boxtimes O(-1)
 \xrightarrow{Q_1xy-Q_0zw}O\to O_Y\to0.
\]
Consequently \(\pi_*O_Y=O_Z\), \(R^1\pi_*O_Y=0\). Adjunction gives
\(\omega_Y=\omega_Z(2)\boxtimes O(-1)|_Y\), and hence
\[
 \pi_*\omega_Y(D_\infty)=\omega_Z(2),\qquad
 \pi_*\omega_Y=\omega_Z .
\]
For the second identity apply the projection to
\(0\to\omega_Z\boxtimes O(-2)\to\omega_Z(2)\boxtimes O(-1)\to\omega_Y\to0\).
Explicitly, the regular section
\[
 e=\frac{xy}{Q_0}=\frac{zw}{Q_1}
 \quad\text{of }O_Y(2,-1)
\]
identifies \(\omega_Z\) with \(\pi_*\omega_Y\) by pullback and multiplication by \(e\): the difference of the two local lifts is the graph equation divided by \(Q_0Q_1\), so the connecting homomorphism gives the generator of \(H^1(O(-2))\) (choose the matching orientation). Multiplication by \(Q_1\), the inclusion into the twisted dualizing bundle, therefore becomes exactly multiplication by \(zw\) on \(Z\).

Under the twisted identification the constructed form corresponds to
\[
 P=\tfrac12\,c_Z(x\,dy-y\,dx)\in H^0(Z,\omega_Z(2)),
\]
where \(c_Z\) is the fundamental class map, or \(P=D_{03}/2\) in the existing ordered adjunction convention. Indeed on the dense moving locus the identification of a section with its actual differential divides its numerator by \(zw\), and \(c_Z(xdy-ydx)/(2zw)\) has the prescribed weighted branch expression. Push the graph section forward via the displayed identification with \(\omega_Z(2)\). On each generic point of \(Z\), the two numerator sections agree by the reduced-dualizing inclusion and the generic multiplicity formula for the fundamental class. Purity of \(Z\) gives equality as sections on \(Z\). In particular the constructed section is not an arbitrary auxiliary differential: it is the actual equation numerator on the compact graph with its natural twist.

The entire remaining obstruction is removal of the twist:
\[
 \theta\in H^0(Y,\omega_Y)
 \ \Longleftrightarrow\ M_1=0
 \ \Longleftrightarrow\
 P\in zw H^0(Z,\omega_Z).
\]
The first equivalence uses the explicit residues on the reduced corner sections and their inclusion in \(\omega_Y\): a regular lift annihilating the nilradical must come from \(\omega_{Y_{\rm red}}\). The second is the explicit multiplication comparison above. In particular the condition is scheme-theoretic vanishing of the numerator on the degenerate fiber \(D_\infty=Z\cap V(zw)\), not mere vanishing at the two underlying points. Each of these endpoint pieces has length \(ab\). The earlier [endpoint socle comparison](#centered-differential-and-scalar-part-of-the-spectrum) expresses the \(p_0\) restriction as \(\bar P=(M_1/ab)\bar D_{12}\). The degree equality fixes the length and the normalization, not the scalar. The global residue theorem on the full curve only sees the opposite residues canceling. Choosing instead to put the permitted poles at \(q=0\) adds \(M_1dq/q\) on \(E_0\) and its negative on \(E_\infty\), leaving the moving restrictions unchanged. So a different chart or permitted boundary divisor does not remove the missing condition.

This closes the requested construction of a differential on the full intersection with all attachment residues canceled and identifies its actual global equation numerator; it localizes the unresolved regularity to the two complete corner sections over one degenerate quadric. It does not show that the actual CI forces that numerator to vanish on this fiber. A further argument must use more than the length count or global existence of the twisted section. Provisional pending independent review.


### Endpoint plane deformation: the residue generating function and the degree budget

Near \(p_0\), in \(z=1\), write \(\lambda=1/q\) for the pencil parameter (distinct from the character \(q_i\)). The equations of the slice \(w=\lambda xy\) are
\[
 f_\lambda=F(1,x,y,\lambda xy),\quad g_\lambda=G(1,x,y,\lambda xy).
\]
For \(\lambda\ne 1/q_i\) their common affine zero is the origin, with local intersection length \(ab\); this includes \(\lambda=0\). The first variation at zero is \(xy(F_w,G_w)|_{w=0}\). Define \(\mathcal R_\lambda(T)\) to be the local plane Grothendieck residue of the numerator \(T(1,x,y,\lambda xy)\) with respect to the ordered equations \((f_\lambda,g_\lambda)\). Put \(P=D_{03}/2\), \(J=D_{12}\), and \(K(\lambda)=\prod_i(1-\lambda q_i)^{n_i}\). Then the explicit corner differential of the preceding section and adjunction give
\[
 \mathcal R_\lambda(P)=\sum_i\frac{n_iq_i}{1-\lambda q_i}
   =-\frac{K'(\lambda)}{K(\lambda)},\qquad
 \mathcal R_\lambda(J)=4\sum_i\frac{n_i}{1-\lambda q_i}.
\]
For clarity, the residue on the plane slice is the residue at \(p_0\) on \(Z\) of the adjunction differential represented by \(T/(w-\lambda xy)\). This is the standard iterated complete-intersection residue with the third equation \(w-\lambda xy\), whose derivative in \(w\) is one. On the normalization the weighted branch expressions of \(P/w\) and \(J/w\) are \(n_iq_i\,dr/r\) and \(4n_i\,dr/r\) respectively by the fundamental-class and finite trace formulas. Multiplication by \(w/(w-\lambda xy)\) on these socle-supported forms multiplies the branch by \(1/(1-\lambda q_i)\). Summing the residues proves the formulas without assuming that this rational multiplier is a regular function at the endpoint or that the thickening is reduced. This is the classical local residue/duality formalism (Cattani--Dickenstein--Sturmfels, [Computing Multidimensional Residues](https://arxiv.org/abs/alg-geom/9404011)), applied to the actual pencil deformation.

In particular the corner differential in the parameter \(\lambda\) is \(\mathcal R_\lambda(P)d\lambda/\lambda\), with residue \(+M_1\), by substituting \(q=1/\lambda\) in \(\theta_0\). The Taylor coefficients of \(\mathcal R_\lambda(P)\) are the power sums \(M_{j+1}=\sum_i n_iq_i^{j+1}\). Thus the actual local plane residue family recovers the whole spectral logarithmic derivative, not only the endpoint value.

The Jacobian of the substituted pair is exactly \(J+\lambda(xD_{13}-yD_{23})\) in \(z=1\). The componentwise tangent-minor identities from the spectral--Jacobian bridge give \(xD_{13}-yD_{23}=-2D_{03}=-4P\) modulo the actual ideal (use purity and the generic socle calculation). Consequently the degree budget says
\[
 ab=\mathcal R_\lambda(J-4\lambda P).
\]
This is also immediate from the two spectral sums. Differentiating at zero gives \((d/d\lambda)\mathcal R_\lambda(J)|_0=4M_1\), **not** a vanishing: the residue of the changing plane Jacobian is constant, but the residue of the original projective minor \(J\) need not be. Constant length alone cannot be used to identify these two numerators.

An exact control within the same substitution geometry is \(F=x^2-zy,\ G=y^2-wx\), the previously established twisted-cubic-plus-line example in [the Hilbert symplectic account](chow_hilbert_symplectic_form.md). Its graph has both corner sections with generic length \(4\) and its local plane family is \((x^2-y,y^2-\lambda x^2y)\), equivalent to \((x^2-y,(1-\lambda)x^4)\). For every \(\lambda\ne1\) the length is four, all at the origin. Here \(P=xy/2\) and the plane Jacobian modulo the ideal is \(4(1-\lambda)xy\). Hence \(\mathcal R_\lambda(P)=1/(2(1-\lambda))\), nonzero at zero. The example contains a twisted cubic and the coordinate line \(x=y=0\) (a moving component over \(q=0\) in the compact graph), not an entire translated-quartic cycle. It disproves using just the fixed local length and the special \(w=\lambda xy\) deformation, even for actual global homogeneous pairs. The distinct quartic hypothesis and the absence of any such degenerate-fiber moving component remain relevant; the control is not a counterexample to UM1.

This is a direct local plane implementation of the corner differential, with all higher spectral moments available. It isolates an additional comparison needed for a proof: why the residue of the original minor \(J\), not the moving plane Jacobian, would be stationary at \(\lambda=0\) under the complete translated-quartic cycle hypothesis. No such stationarity theorem has been shown. In particular the Euler--Jacobi vanishing theorem cannot simply be applied to \(P\) at \(\lambda=0\), because its degree is the critical \(a+b-2\), not strictly below it. Provisional pending independent review.


### Opposite degeneration and a reduced numerical control

Compare the two degenerate quadric charts using the same intrinsic numerator \(P=\tfrac12 c_Z(x\,dy-y\,dx)\). On \(z=1\) put
\[
 S(q)=\operatorname{Res}_{p_0;F,G,xy-qw}(P)
\]
with the iterated residue orientation matching the preceding plane-residue family. Here the notation for \(P\) as a polynomial uses actual ordered adjunction; intrinsically this is the residue of the dualizing differential \(P/(xy-qw)\) on \(Z\). The standard residue transformation law and the weighted normalized branch expressions give
\[
 S(q)=\sum_i\frac{n_iq_i}{q_i-q}
     =-q^{-1}\mathcal R_{1/q}(P).
\]
At \(q=0\), the degenerate quadric is the union of \(x=0,y=0\), and
\[
 P/(xy)=\tfrac12(dy/y-dx/x),\qquad
 S(0)=\tfrac12(3m-m)=m .
\]
All formulas involving Kähler differentials here mean their fundamental-class images. The two component plane intersection lengths are \(m,3m\), summing to \(ab\), and both contributions to the differential residue are the indicated signed halves. At infinity \(S=-M_1/q+O(q^{-2})\). Thus degree exhaustion plus the known weighted identities give the value at zero and a zero at infinity. The wanted stationarity is exactly a zero of order **at least two** at infinity; the value at zero supplies no independent cancellation. In fact \(S'(0)=\sum n_i/q_i\), the reciprocal first moment, already known not to vanish universally. The opposite residue formula is valid away from the spectral parameters and uses the same classical residue duality as the preceding section, not a new residue theorem.

There is a useful entirely reduced control for the proposed implication from local geometry and numerical degree exhaustion. Take four distinct translates on \(Q_1\), with \(u_i=v_i\ne0\) pairwise distinct, and let \(D\) be their reduced union, a Cartier divisor of type \((4,12)\) on the smooth quadric (ordering the rulings so each quartic has type \((1,3)\)). It has the prescribed entire cycle \(m=4\), no components on either degenerate quadric, and is a projective lci. Its degree is sixteen and its arithmetic genus is \((4-1)(12-1)=33\), exactly those of a \((4,4)\) CI. The genus formula is classical Cartier adjunction on \(Q\) (Stacks [48.14.1](https://stacks.math.columbia.edu/tag/0B4B)). In particular this matches the full Hilbert polynomial, not just the degree. Its local equations near \(p_0\) are
\[
 w-xy,\quad \prod_{i=1}^4(y-u_i x^3)
\]
in \(z=1\). On \(w=\lambda xy\) for \(\lambda\ne1\) the local intersection length is \(4+12=16\), using the two axes. All nonspectral quadric slices have the prescribed lengths sixteen at each corner by Cartier intersection multiplicity. Both degenerate quadric fibers meet the curve in the prescribed endpoint supports and lengths, and the compact graph has exactly the same cycle prescription as above, with sixteen times each corner section. Its weighted logarithmic numerator has \(S(q)=4/(1-q)\) and \(M_1=4\), so the required order-two vanishing fails. These are actual local two-equation presentations and actual global locally CI schemes, but not one global homogeneous pair of type \((4,4)\).

The failure of global presentation is completely visible: any quartic vanishing on \(D\) contains the quadric, since a \((4,4)\) divisor on \(Q\) cannot contain a \((4,12)\) divisor. The global adjunction distinction is also exact:
\[
 \omega_D=O_D(2,10),\qquad
 \omega_D\otimes O_D(-4)=O_D(-2,6),
\]
and the latter is nontrivial since
\(0\to O_Q(-6,-6)\to O_Q(-2,6)\to O_D(-2,6)\to0\)
gives \(H^0(O_D(-2,6))=0\) by the cohomology of the product. Similarly \(h^1(I_D(4))=h^1(O_Q(0,-8))=7\), via the ideal sequence of \(Q\). These are standard quadric-divisor computations (Hartshorne, *Algebraic Geometry*, III Ex. 5.6 for ACM curves on quadrics; the genus and canonical comparison follow directly from adjunction). This is not a candidate counterexample to UM1, nor a new low-degree exclusion. It demonstrates even in the reduced case that local lci, matching endpoint deformation lengths and corner cycles, absence of degenerate moving components and even the entire CI Hilbert polynomial cannot force the double zero. A successful use of the global two-equation hypothesis must retain genuine global equation/section compatibility (not only numerical adjunction or local residue conservation). The example is a control, not a proposal to classify quadric carriers. No new universal vanishing established; provisional pending review.


### Global section gluing: from the Hilbert polynomial to the actual graded maps

The [endpoint delta theorem](arrangement_endpoint_delta.md) gives the two coefficient filtrations \(W_j^0,W_j^\infty\subset k^m\) for a distinct reduced configuration. Classical inputs are the normalization sequence, the Koszul resolution of a projective CI, and Serre duality; see Hartshorne, *Algebraic Geometry*, III §§5, 7, and Rosenlicht's residue criterion in [Gorenstein curve singularities of genus three, §1.3.1](https://doi.org/10.1007/s11565-024-00495-8). The existing reduced-cycle invariant-ideal theorem already proves the first moment for reduced CIs. The point here is to read graded global sections as actual two-endpoint gluing conditions, not to reprove that theorem.

For \(d\ge0\), write a normalized section of \(O_Z(d)\) on branch \(i\) in the \(z^d\)-frame as \(\sum_{j=0}^{4d}c_{ij}r^j\). Since \(w/z=v_i r^4\) and \(r^-=q_i/r\), the coefficient in the opposite frame is \(c_{ij}v_i^{-d}q_i^{j-4d}\) at order \(4d-j\). Therefore the complete space of global sections is the direct sum over \(0\le j\le4d\) of
\[
 L_{d,j}=W_j^0\cap\left(\mathbf v^d\mathbf q^{4d-j} W_{4d-j}^\infty\right)\subset k^m.
\]
Here and below multiplication by the displayed invertible vectors is componentwise. The actual ambient degree-\(d\) weight-\(j\) span is
\[
 V_{d,j}=\operatorname{span}\{\mathbf u^b\mathbf v^c:
 b,c\ge0,\ 3b+4c\le j,\ 2b+3c\ge j-d\}.
\]
Indeed the exponents of \(x\) and \(z\) in the corresponding ambient monomial are \(j-3b-4c\) and \(d-j+2b+3c\), respectively. Every such monomial belongs to \(L_{d,j}\). For a reduced union, the ACM condition is exactly equality of these two spaces for all \(d\ge0,j\); the ideal restriction sequence proves this, since \(H^1(P^3,O(d))=0\) and negative-degree sections vanish on the normalized curves. A CI further prescribes the Hilbert series \((1-T^a)(1-T^b)/(1-T)^4\). This is an exact check in the existing coefficient model, not a sufficient claim based on the Hilbert polynomial alone.

For instance compare the two four-point configurations \((u,v)=(\zeta,1)\) and \((\zeta,\zeta)\) as \(\zeta^4=1\), in characteristic zero. Their endpoint rank profiles and arithmetic genera agree (\(\delta_0=\delta_\infty=18,\ p_a=33\)). At \(d=2,j=4\), \(W_4^0=\langle1,\mathbf u,\mathbf v\rangle\), and the transported opposite span is \(\langle\boldsymbol\eta^2,\mathbf u,\mathbf v\rangle\), where \(\eta=u^2/v\). The balanced example has \(L_{2,4}=\langle1,\mathbf u\rangle\) of dimension two, while the unbalanced example has \(L_{2,4}=\langle\mathbf u\rangle\) of dimension one. These are the spans of \(zw,xy\), independent in the former but equal in the latter. The known (4,4) binomial CI has \(h^0(O_Z(d))=1,4,10,20,33,48,64\) for \(d=0,\ldots,6\). The latter is a divisor of type (4,12) on \(Q_1\), whose standard ideal sequence on the quadric gives \(1,4,9,16,32,48,64\). Both have polynomial \(16d-32\). They differ already in degree two, and at canonical degree four.

For an arbitrary actual CM thickening the same *global* matching operation is available without separating branches into a constant coefficient algebra. Let \(\rho:W\to Z\) be the finite separated modification, \(B=\pi_*O_W\) on the longitudinal \(P^1\), and \(e=\deg B\); use the [endpoint comparison](tropical_thickenings_and_endpoint_duality.md) and the [arrangement endpoint contraction](transverse_neighborhood_motion_and_conormal.md) on the two finite image charts. The pullback of \(O_Z(d)\) is \(\pi^*O(4d)\) (the two frames have transition \(V^d r^{4d}\), with \(V\) a global unit on \(W\)). Thus for \(d\ge0\) the kernel of the map from \(H^0(P^1,B(4d))\) to the two endpoint discrepancy quotients is exactly \(H^0(Z,O_Z(d))\). Global generation gives \(H^1(B(4d))=0\). The dimension of the source is \(m(4d+1)+e\), and the total dimension of the target is \(e+m(2a+2b-7)\) for an actual CI. The constant algebra coefficient decomposition above need not hold for this moving \(B\). The gluing map itself, not its dimensions, is the common object.

There is an especially direct check in canonical degree \(s=a+b-4\). Use the actual divisor \(D=V(zw)\cap Z\) of degree \(8m\), with two endpoint pieces of length \(4m\) each. By the actual CI adjunction identification and Serre duality,
\[
 0\to H^0(\omega_Z)\to H^0(\omega_Z(2))\to
 H^0(\omega_Z(2)|_D)\xrightarrow{\partial} k\to0 .
\]
Here the inclusion is multiplication by \(zw\) and \(H^1(\omega_Z(2))=0\), since \(H^0(O_Z(-2))=0\) by the CI resolution. The last \(k=H^1(\omega_Z)\) is one-dimensional since \(H^0(O_Z)=k\). The connecting map is the sum of the two local residue functionals (the global residue theorem). In particular the global canonical gluing imposes *one* relation on these restrictions, not separate zero restrictions at the endpoints. Our numerator \(P\in H^0(\omega_Z(2))\) has endpoint residues \(M_1,-M_1\), which already obey that relation. This explains why even using the canonical Hilbert function, without further information on the specific numerator, does not turn the global residue condition into separate endpoint vanishing. No proof of arbitrary first-moment vanishing is claimed. Provisional synthesis; independent review still needed.

## 5. Global sections as requirements on F,G

For a proper CI \(Z\) of the stated cycle, adjunction gives
\(\omega_Z=O_Z(d+e-4)\); its fundamental class map sends the
six homogeneous differential expressions
\(x_i\,dx_j-x_j\,dx_i\) to sections of \(\omega_Z(2)\).
In an adjunction trivialization they are the complementary signed
minors \(D_{kl}\) of the matrix of gradients of \(F,G\).
A realization must give these sections homogeneous polynomial
lifts of degree \(d+e-2\), and realize them by actual gradients,
not merely by a matrix satisfying Plücker relations.
The sections depend on the realizing scheme and adjunction
identification; the cycle alone determines their weighted
normalization-side fundamental-class expressions, not a canonical
ambient polynomial lift or the nonreduced dualizing sheaf.

The tangent Plücker coordinates of the orbit are
\[
 (zx,3zy,4zw,2xy,3xw,yw),
 \qquad q=2p_{12}/p_{03}.
\]
The hyperplane sections \(2p_{12}-qp_{03}=0\) are Lagrangian
Grassmannians for \(dx\wedge dy-(q/2)dz\wedge dw\).
Their common base is \(\Sigma_{03|12}\).
The established [contact geometry](contact_jacobians_and_hamiltonian_actions.md)
and [intrinsic quadric spectrum](quadric_pencil_spectral_intrinsic_geometry.md)
connect the sole-support Poisson identity to the longitudinal
torus via the Hamiltonian of \(xy-qzw\). Involutivity does not
imply this Hamiltonian preserves the actual CI ideal.
Plücker products may be zero on generic thickened components
because the minors lie in the generic socles.

### Centered differential and scalar part of the spectrum

Put \(J=D_{12}\), \(q=xy/(zw)\) in the total quotient ring.
The established spectral--Jacobian identity is \(qJ=2D_{03}\).
Under finite-flat duality for \(\pi:Z\to\mathbf P^1_{[z:w]}\),
\(\pi_*\omega_Z(2)=(\pi_*O_Z)^\vee\); the section \(J\) corresponds
to trace. The homogeneous coordinate ring is graded free over
\(k[z,w]\) with a basis lifting the monomials of
\(k[x,y]/(F|_L,G|_L)\); its degree distribution is the binary CI
Hilbert series. On a monomial lift \(x^r y^s\), generic fiber
summation gives
\[
 \operatorname{Tr}(q^\ell x^r y^s)=
 4z^{r+s-j}w^j\sum_i n_i q_i^\ell u_i^s/v_i^j,
 \quad j=(r+3s)/4\in\mathbf Z,
\]
and zero if \(j\) is not integral. For positive \(r+s\) every
nonzero entry is divisible by \(zw\); the degree-zero basis entry
is the sole exception. Therefore, in characteristic zero,
\[
 qJ=(M_1/m)J+zw\,S,\quad S\in H^0(Z,\omega_Z)
\]
in the adjunction identification. More generally, for any polynomial
\(p\) replace \(q\) by \(p(q)\) and \(M_1/m\) by
\(\operatorname{Tr}(p(\Phi))/m\). Regularity of the resulting
numerators follows directly from the trace coordinates and
duality, without assuming \(q\) regular at the endpoints.

The centered differential
\[
 \frac{x\,dy-y\,dx}{zw}
 -\frac{M_1}{2m}\frac{z\,dw-w\,dz}{zw}
\]
is consequently regular in \(\omega_Z\). On each normalized branch
the first term is \(2q_i\,dt/t\), and the second removes the
mean eigenvalue. This is the geometric version of separating an
endomorphism into its scalar and traceless parts. A coordinate
of the regular section \(S\), evaluated on \(xy\) via the duality
pairing, is \(4(\sum n_iq_i^2-M_1^2/m)\), a centered second moment.
For sole support \(S=0\), since trace kills the generic nilpotent
part and the mean equals the sole eigenvalue.

The **uncentered** differential is regular iff \(M_1=0\) for
such a CI. Its endpoint residues are \(2M_1,-2M_1\).
The global residue theorem gives no obstruction, since they
already sum to zero. At \(p_0\), write
\(F(1,x,y,w)=f+w f_1+\cdots,\ G=g+w g_1+\cdots\).
Euler gives the endpoint numerator
\(D_{03}=f_1(xg_x+yg_y)-g_1(xf_x+yf_y)\) modulo \((f,g)\).
It lies in the one-dimensional socle and equals
\((M_1/(2m))(f_xg_y-f_yg_x)\) there, by the same trace pairing.
Thus regularity at either endpoint, the Hessian vanishing, and
the first normal jet residue on the disjoint line are equivalent
to spectral balance, not proofs of it. The exact first-jet
Macaulay pairing is in [spectral--Jacobian bridge](spectral_jacobian_first_jet_bridge.md).
A single local smooth branch \(y=ux^3,w=vx^4\) has all the local
spectral identities yet a pole \(2q\,dx/x\); the missing input is global.
