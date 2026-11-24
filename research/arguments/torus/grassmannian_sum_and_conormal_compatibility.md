# Grassmannian sum pencil and conormal compatibility

**Status:** provisional synthesis of the November 24 discussion; elementary calculations and inherited results, not an independently reviewed new obstruction. Characteristic zero. The subject is the geometry of realization: how a cycle, its embedded infinitesimal neighborhoods, and two global homogeneous equations are related. UM1 is a useful test of this geometry, not the organizing objective. For assertions about actual projective CIs retain the entire-cycle hypothesis, rather than mere containment or a torus-local CI.

This is a companion to [cycle-first coefficient realization](transverse_coefficient_realization_synthesis.md). Its purpose is to interpret the constructions geometrically; the coordinate calculations below record those interpretations and allow comparison. No irreducibility or smoothing statement about the actual realization locus is assumed.

## 0. Geometric reading: from orbits to equations

On the dense projective torus \(U\), the longitudinal action gives the smooth quotient \(\pi:U\to T=(\mathbf G_m)^2\). A point of \(T\) represents an entire orbit, whose closure is a translated quartic. Thus \(\sigma\in\operatorname{Sym}^m T\) is a configuration of curves, and the full paired Chow form is its coefficient presentation. The characters \(q=u/v,\eta=u^2/v\) form a basis of the character lattice of \(T\): \(u=\eta/q,v=\eta/q^2\). Their joint projection preserves the configuration, whereas their separate pushforward divisors can lose the pairing. The various product models and Chow restrictions are observations of this same configuration in different directions.

The [canonical fat-point envelope](full_transverse_chow_pullback_envelope.md) associates to the cycle the finite scheme \(T_\sigma=V(\bigcap_i\mathfrak m_i^{n_i})\subset T\). Choosing the longitudinal coordinate \(t=x/z\), the actual scheme on \(U\) is a finite flat degree-\(m\) family over \(\mathbf G_m\) inside \(\mathbf G_m\times T_\sigma\). Its support is fixed but its embedded transverse neighborhoods can move. The norm of a transverse character counts that character with multiplicity; it is not a description of the moving scheme. See the [embedded quotient framework](../../frameworks/embedded-torus-quotients/index.md) and Stacks Project, [finite locally free norm](https://stacks.math.columbia.edu/tag/0BD2).

The first normal geometry is the conormal plane to a quotient fiber, \(\pi^*\Omega_T\subset\Omega_U\), or its Euler-twisted realization in the dual four-space. The second is the map from the abstract infinitesimal equations \(I_Z/I_Z^2\) into \(\Omega_U|_Z\). Its graph remembers the entire map, even where its image is not a subbundle. In particular, projecting the actual differential to \(\Omega_{U/T}|_Z\) measures how the equations change along the orbit; the corresponding map evaluates a local equation on the longitudinal derivation. It vanishes when the ideal is invariant, and does not follow merely from invariance of the support. The wedge of the two differentials can lose such variation when its coefficients lie in the socle.

For a concrete illustration, use coordinates \((t,q,\eta)\) on \(U\) and fix nonzero \(q_0,\eta_0\). The two length-two constant families with ideals
\[
 (q-q_0,(\eta-\eta_0)^2),\qquad
 ((q-q_0)^2,\eta-\eta_0)
\]
have the same cycle and the same projected norm polynomial \((Q-q_0)^2\). In the first, the actual scheme lies in the quadric fiber \(q=q_0\); in the second, it does so only on reduction. The unweighted form \(dq\) is conormal-compatible in the first but not the second (characteristic zero), since its class in the second Kähler module is nonzero. The weighted form \(2(q-q_0)dq\) has a conormal lift in both. The same spectral polynomial has quite different infinitesimal meanings. A moving illustration is \(((q-q_0)^2,\,\eta-\eta_0-t(q-q_0))\): writing \(\epsilon=q-q_0\), its differentials are \(2\epsilon\,dq\) and \(d\eta-t\,dq-\epsilon\,dt\), so their wedge loses the longitudinal term by \(\epsilon^2=0\). These are illustrative torus-local families, not claims of homogeneous projective CI realization.

The compatible weighted form is best understood as functoriality of conormal sheaves. The projected cycle is the effective divisor \(D_q\) in \(\mathbf G_m\) with equation \(H(Q,1)\). The actual map \(Z\cap U\to\mathbf G_m\) factors through that divisor by the spectral membership theorem. Pulling back its defining conormal class gives a class in \(I_Z/I_Z^2\), whose differential is \(H'(q)dq\). This is a commuting conormal diagram, not an extra independent relation. The same interpretation applies to the whole fat-point envelope: its conormal maps to that of the actual scheme. The established conormal functoriality and exact sequences are [Stacks 29.32](https://stacks.math.columbia.edu/tag/01R1) and [37.63](https://stacks.math.columbia.edu/tag/06BB). An unweighted form asks a stronger question about actual infinitesimal directions; the cycle supplies only its weighted lift in general.

The blowup of the sum pencil is a different kind of geometry: it records the value of an observable when the raw normal-coordinate projection becomes indeterminate. It is not a moduli space of the transverse neighborhoods. The exceptional \(\mathbf P^1\) is precisely the ambiguity of this observable at a base point, not a classification of thickening directions. The cycle supplies a distinguished value there. On the cycle space itself the sum is already regular; compactification is necessary only for the Plücker-coordinate presentation.

Finally, a degree-\((a,b)\) CI is the zero locus of a regular section of \(O(a)\oplus O(b)\) on projective space. This adds global information beyond the family of transverse neighborhoods and the conormal graph: the same section extends across both contracted endpoints, with those prescribed line bundles and no residual curve. The graph on the dense torus does not by itself recover such a section. The [endpoint modification and duality account](tropical_thickenings_and_endpoint_duality.md) records that distinction in terms of the finite modification and endpoint functions; see also the companion coefficient synthesis for the three product models.

**Geometric questions to carry forward:** Which information about a moving neighborhood is visible in the conormal graph, its exterior square, and the two projected divisors? How do the conormal classes supplied by the common envelope relate to the actual rank-two equation bundle? What is preserved when the separated endpoint model is contracted to projective space? How do the different projection descriptions express the same global section? These are questions about realization, whether or not an obstruction follows. The sum fiber provides one concrete observable with which to compare answers.

The [shape and motion comparison](transverse_neighborhood_motion_and_conormal.md) develops the first geometric question: the longitudinal conormal component is the second fundamental form of the moving kernel in the fixed fat-point envelope. It distinguishes embedded motion from abstract first-order deformation, and interprets full compatibility of transverse forms through the kernel of that longitudinal map. The rotating double and changing length-four examples explain what the exterior square forgets. The next interface is its behavior under the endpoint contractions.

## 1. Universal construction: resolve only the sum

Let \(W=K\oplus V^*\) with dimensions 2 and 4, and \(G=\operatorname{Gr}(2,W)\). Choose the ordered coordinates of \(W\) to consist of the two auxiliary directions followed by \(z,x,y,w\) covector directions. On \(G^m\) write the Plücker coordinates of factor \(i\) as \(P_{jk}^{(i)}\), \(1\le j<k\le6\). Put
\[
 A_i=2P_{36}^{(i)},\quad B_i=P_{45}^{(i)},\quad
 D=\prod_iB_i,\quad N=\sum_i A_i\prod_{j\ne i}B_j.
\]
Both \(D,N\) are sections of \(\boxtimes_i O_G(1)\).
The universal sum pencil is \([N:D]\); it is not necessary to resolve any of the individual pencils \([A_i:B_i]\).

Set-theoretically its base locus is
\[
 V(N,D)=\bigcup_i V(A_i,B_i)\ \cup\
 \bigcup_{i<j}V(B_i,B_j).
\]
Indeed, if precisely one denominator is zero, the numerator vanishes exactly when its numerator is zero. Each \(V(B_i)\) is an integral Schubert divisor, and \(N\) does not vanish identically on it (choose \(A_i\ne0\) and all other denominators nonzero). Thus the two local equations form a regular sequence along their common zero set in the smooth product. The blowup uses the **ideal** \((N,D)\), not its radical. The Rees algebra of a regular sequence of length two is its symmetric algebra (standard linear-type theorem); hence the graph blowup is
\[
 \widehat X_m=V(TN-SD)\subset G^m\times\mathbf P^1_{[S:T]}.
\]
The projection to \([S:T]\) is the desired map. See Stacks Project, [Blowing up](https://stacks.math.columbia.edu/tag/01OF); the graph equation uses the additional regular-sequence hypothesis. This resolves a rational map, not necessarily the singularities of its graph.

The zero fiber is precisely \(V(N)\times\{[0:1]\}\); the infinity fiber is \(V(D)\times\{[1:0]\}\). Every finite fiber is integral of dimension \(8m-1\). On the chart \(B_i\ne0\) the Plücker relation
\[
 P_{36}P_{45}=P_{35}P_{46}-P_{34}P_{56}
\]
makes the fiber over \(\lambda\) an affine quadric
\[
 2\sum_i(u_iv_i-r_is_i)=\lambda
\]
times affine \(4m\)-space, with \(u=P_{35}/P_{45}\), \(v=P_{46}/P_{45}\), \(r=P_{34}/P_{45}\), \(s=P_{56}/P_{45}\). These are four independent graph-chart coordinates per factor. The quadric is irreducible and generically reduced by rank \(4m\ge4\). No component lies in \(D=0\), because there it would be contained in the codimension-two base locus, whereas the fiber is a Cartier hypersurface in the smooth product. The hypersurface is CM, so generic reducedness gives reducedness. This argument includes \(m=1\).

Permutation invariance gives an unordered version by finite symmetric-group quotient; no assertion that arbitrary blowups commute with that quotient is needed.

The full universal polynomial is
\[
 \mathscr H(U,V)=\prod_i(B_iU-A_iV)=DU^m-NU^{m-1}V+V^2\mathscr K.
\]
The graph equation gives \(T\mathscr H=TD U^m-SD U^{m-1}V+TV^2\mathscr K\). The sum blowup resolves the first coefficient ratio, not necessarily all normalized coefficients.

## 2. Collision strata and the ordinary configuration space

Equal spectral values on \(D\ne0\) are expressed by \(A_iB_j-A_jB_i=0\). For a partition into blocks \(I_\alpha\) of sizes \(m_\alpha\), choose one representative \(i_\alpha\). On the closure of this collision locus in the graph one has
\[
 T\sum_\alpha m_\alpha A_{i_\alpha}
 \prod_{\beta\ne\alpha} B_{i_\beta}
 =S\prod_\alpha B_{i_\alpha}.
\]
This holds for every choice of representatives: cancel on \(D\ne0\) and take closure. The correct closure ideal is obtained by saturation by \(D\), not by retaining all components of the naive equations. If distinct blocks must remain distinct, use the corresponding open conditions too.

For the single-block diagonal the closure is exactly
\[
 mTA_i=SB_i\quad(1\le i\le m).
\]
These equations imply the graph equation. The family over \(\mathbf P^1\) is a fiber product of flat hyperplane-pencil families with geometrically integral fibers (nonzero finite fibers by the same quadric calculation, zero and infinity Schubert divisors). It is integral and the open \(D\ne0\) is dense. Its dimension is \(7m+1\). At \(S=0\) the intersection is the product of the divisors \(A_i=0\); the intersection is entirely outside the nonzero spectral diagonal.

On the open with finite nonzero spectra, a partition into \(r\) distinct values has dimension \(7m+r\); its nonempty balanced part has dimension \(7m+r-1\). The latter is irreducible since the hyperplane \(\sum_\alpha m_\alpha q_\alpha=0\) is integral and deleting collisions and zero coordinates is open. Some partitions have empty balanced open (e.g. \(r=1\)). The fibers of the individual pencils on this open are isomorphic by scaling a column.

On the cycle space itself the same calculation is much simpler: change the two torus coordinates from \((u,v)\) to \((q=u/v,v)\). The balanced locus of ordered cycles is the open hyperplane \(\sum_iq_i=0\) times \((\mathbf G_m)^m\), integral of dimension \(2m-1\) for \(m\ge2\). It descends to the symmetric product. Modulo common scaling the distinct spectral configurations are \(M_{0,m+2}\), with two marked points \(0,\infty\). The coordinates \([q_1:\cdots:q_m]\) give the Kapranov projective model with coordinate vertices and the all-ones point as the initial centers (Kapranov, [Chow quotients of Grassmannians I](https://arxiv.org/abs/alg-geom/9210002)). The hyperplane \(\sum_i q_i=0\) misses the all-ones point in characteristic zero. This is useful collision geometry, not an implication of CI realization. The sum pencil does not require the full Kapranov or permutohedral resolution.

## 3. Universal normal incidence

For a prescribed two-plane \(N_p\subset V^*\), the last exterior-power component of a Plücker bivector must lie in \(\det N_p\):
\[
 Y_p=G\cap\mathbf P(\det K\oplus(K\otimes V^*)\oplus\det N_p).
\]
These are five homogeneous linear conditions on the Plücker coordinates. Set-theoretically the locus is the union of \(\operatorname{Gr}(2,K\oplus N_p)\) and the Schubert locus \(\{L:\dim(L\cap K)\ge1\}\). Indeed, projection to \(V^*\) either has rank two with image \(N_p\), or has rank at most one and zero exterior square. Dimensions are 4 and 5, with intersection dimension 3.

When the projection to \(V^*\) lies in a fixed three-plane \(H_p\supset N_p\), the ambient reduces to \(\operatorname{Gr}(2,K\oplus H_p)\simeq\operatorname{Gr}(2,5)\). In adapted coordinates with \(N_p\) spanned by directions 3 and 4 and \(H_p\) by 3,4,5, the equations are \(P_{35}=P_{45}=0\). The same two components now both have dimension 4. Their intersection has dimension 3. Scheme-theoretically this is the union: the two equations form a complete intersection; each component is generically reduced (on full-rank projection the two equations eliminate the fifth column; on generic rank-one projection outside \(N_p\) they eliminate its two independent transverse rank defects). CM and generic reducedness imply reducedness. Equivalently the component ideals are
\[
 (P_{15},P_{25},P_{35},P_{45}),\qquad
 (P_{34},P_{35},P_{45}).
\]
The Plücker relations imply \(P_{15}P_{34}=P_{25}P_{34}=0\) modulo the two equations. Do not infer that a nonreduced test scheme factors through either individual component.

A compatible vector \(\eta\in W\) satisfies \(\eta\wedge P=0\), the ordinary tautological incidence (or flag variety when the vector spans a line). This equation retains mixed Plücker coordinates even when the last six vanish. Its zero locus over \(G\) is the total space of the tautological bundle, not a new independent obstruction. For arrangements the total space of the direct sum of the tautological bundles pulls back to the sum graph.

## 4. Restrict only now: the translated quartic and actual conormal map

Let \(Z=V(F_a,G_b)\), with entire cycle \(\sum_\nu n_\nu[C_{u_\nu,v_\nu}]\), \(m=ab/4=\sum n_\nu\). Coordinates \(z,x,y,w\) as above. On the coordinate torus put \(X=xy,\ Y=zw,\ q=X/Y\). The fixed geometric normal plane is the annihilator of the Euler and longitudinal vectors
\[
 (z,x,y,w),\qquad (0,x,3y,4w).
\]
It has basis \(d\log(z^2y/x^3),d\log(z^3w/x^4)\). If \(D_{ij}\) denote the six dual Plücker entries (indices 0 through 3), wedge compatibility is
\[
 zxD_{01}=-zyD_{02}/3=zwD_{03}/2=xyD_{12}/4
 =-xwD_{13}/3=ywD_{23}.
\]
These follow by taking the exterior square of the displayed basis. In particular \(2zwD_{03}=xyD_{12}\). The [contact Jacobian argument](contact_jacobians_and_hamiltonian_actions.md) and [spectral--Jacobian bridge](spectral_jacobian_first_jet_bridge.md) establish the actual identity including generic thickening. Unmixedness extends the homogeneous identities from the dense coordinate torus. The intrinsic plane comes from the orbit, not a projectivization of nilpotent minors.

The primal tangent coordinates are \((zx,3zy,4zw,2xy,3xw,yw)\); duality uses complementary signed coordinates. Rescale the primal coordinates by the longitudinal weight differences to obtain the square-free products \(x_ix_j\). Their toric threefold is the octahedral orbit closure defined by equality of the three complementary products. In the dual six coordinates the corresponding complementary products have ratio \(1:9:8\); interpreted as equations these are \(V=9U,\ W=8U\), with \(U=P_{34}P_{56}, V=P_{35}P_{46}, W=P_{36}P_{45}\). The toric component is the closure from the nonzero Plücker torus, not necessarily a description of all degenerate graph points. See the companion coefficient synthesis for coordinate-line projections, three product models and their blowup dictionary. None of these pointwise equations couples the different factors.

Canonically set \(E=(I_Z/I_Z^2)(1)\) and let
\[
 \phi:E\to\Omega_{\mathbf P^3}(1)|_Z\to V^*\otimes O_Z
\]
be the conormal map (Stacks Project, [conormal sheaf and exact sequence](https://stacks.math.columbia.edu/tag/01R1)). Its graph is a rank-two direct summand of \(E\oplus V^*\), hence gives a section of the relative \(\operatorname{Gr}_Z(2,E\oplus V^*)\), including on thick schemes. In frames it is the matrix \((I_2\mid dF,dG)\), with the gradients as rows. More general auxiliary columns are allowed where the whole matrix has rank two; the graph is the canonical choice and does land in the graph chart. The relative Grassmannian is not globally a fixed \(G\) without a trivialization of \(E\). The following contractions are nevertheless global because only the trivial \(V^*\) summand is used.

Let \(\mathcal L=(\det E)^\vee\), \(\Theta=\wedge^2\phi\in H^0(Z,\mathcal L\otimes\wedge^2 V^*)\), and take
\[
 \alpha=2e_z\wedge e_w,\quad\beta=e_x\wedge e_y,\quad
 A=\langle\alpha,\Theta\rangle,\quad B=\langle\beta,\Theta\rangle .
\]
These are the two canonical Plücker sections. The pencil pulls back as the tensor sections
\[
 N_\Theta=\sum_i B_1\otimes\cdots\otimes A_i\otimes\cdots\otimes B_m,
 \quad D_\Theta=\bigotimes_iB_i.
\]
On the generic transverse local Artin algebra of a component, \(A=q_\nu B\), because the Jacobian \(B\) generates the socle and \(q-q_\nu\) is nilpotent. In characteristic zero the socle Jacobian is nonzero (Scheja--Storch; see the bridge proof). Take independent tensor factors over a common generic base field, repeating each component \(n_\nu\) times. Then
\[
 N_\Theta=M_1 D_\Theta,\quad M_1=\sum_\nu n_\nu q_\nu,\qquad D_\Theta\ne0.
\]
This is an evaluation test, not a canonical construction of an arrangement of \(m\) reduced graph points. The actual generic algebra supplies a norm and multiplicities, not a distinguished labeling of infinitesimal sheets. Tensoring independent copies keeps the socle products nonzero; multiplying them within one local algebra would not. The equality is valid without reducedness.

A crucial boundary distinction: if \(D_\Theta\) is nilpotent, the equation \(TN_\Theta=SD_\Theta\) does not uniquely determine a lift over the nonreduced algebra. The scalar cycle value \([M_1:1]\) supplies a lift to the graph; the universal property of blowing up does not automatically lift a morphism with nilpotent base ideal. At geometric points where all relevant minors vanish, the graph equation alone leaves the whole exceptional \(\mathbf P^1\). With the actual cycle scalar supplied, \(N_\Theta=0\) is equivalent to \(M_1=0\), and hence to \(S=0\). Without it, \(N=0\) alone is insufficient to force \(S=0\) on the blowup.

## 5. Compatible q-form and the cycle polynomial

Use the intrinsic one-form
\[
 \omega_q=Y\,dX-X\,dY\in H^0(\mathbf P^3,\Omega(4)).
\]
On the dense torus \(\omega_q/(XY)=d\log q\).
The wedge condition with \(\Theta\) together with Euler contraction has the elementary linear solution
\[
 (zxD_{01},zyD_{02},zwD_{03},xyD_{12},xwD_{13},ywD_{23})
 =(r,s,-r-s,r-s,s,r).
\]
This follows by expanding the logarithmic wedge with coefficient vector \((-1,1,1,-1)\) and contracting with the all-ones Euler vector. Longitudinal contraction imposes \(s=-3r\). Thus the q-form and Euler conditions alone leave two parameters, and the longitudinal condition leaves one. These are equations in the exterior-power module and do not require ratios of minors.

For the full graph, a compatible pair \((e,\omega)\) is precisely one with \(\omega=\phi(e)\) (allow twists). Write the full Plücker inclusion as \(P=P_0+P_1+\Theta\), with components in \(\det E,\ E\otimes V^*,\ \wedge^2V^*\), viewed as maps out of \(\det E\). The equation \((e,\omega)\wedge P=0\) splits into
\[
 e\wedge P_1+\omega\wedge P_0=0,\quad
 e\wedge\Theta+\omega\wedge P_1=0,\quad
 \omega\wedge\Theta=0 .
\]
In the graph, \(P_0\) is the identity, so the first equation implies the other two. Mere wedge compatibility with \(\Theta\) is weaker. An unweighted lift of \(d q\) on the torus exists iff its class in \(\Omega_Z\) is zero; this is not automatic for moving or nonreduced structures.

The cycle gives the global equation
\[
 H(U,V)=\prod_\nu(U-q_\nu V)^{n_\nu}
 =U^m-M_1 U^{m-1}V+V^2K(U,V).
\]
The established membership \(H(X,Y)\in I_Z\) follows from the generic length bound and unmixedness. Its conormal class has degree \(2m\). Euler's polynomial identity gives
\[
 Y\,dH(X,Y)=H_U(X,Y)\omega_q+mH(X,Y)dY.
\]
Consequently \(\phi(Y[H])=H_U\omega_q\) on \(Z\), with both sides in twist \(2m+1\) of the source and target of \(\phi\). This is the canonical full graph compatibility
\[
 (Y[H],H_U\omega_q)\wedge P=0.
\]
On the finite cycle lift \(M_1=S/T\), substitute
\[
 \Psi=H_U=mX^{m-1}-(m-1)(S/T)X^{m-2}Y+Y^2K_U(X,Y)
\]
(for \(m=1\) use \(H_U=1\)). The three exterior-power equations above hold with \(e=Y[H]\), \(\omega=\Psi\omega_q\), alongside \(TN=SD\). This is the combined construction. It is a consequence of membership and Euler's identity, not independent equations forcing the coefficient \(S\) to vanish. On the coordinate torus the CI \((h(q),v-v_0)\) has the compatible form \(h'(q)dq\) for any monic polynomial \(h\) with nonzero roots. Its arbitrary first coefficient is a negative control against a purely local or formal argument.

## 6. Equation-level comparison: spectral balance as one test

The entire large construction reduces to the following objects:

* The cycle determines \(H\) and the paired Chow polynomial. Its first coefficient is \(-M_1\).
* The actual homogeneous equations determine the conormal map, and its wedge determines the two sections \(A=2D_{03}, B=D_{12}\). Their relation \(A=qB\) on the dense torus is already proved.
* The full cycle gives the weighted compatible q-form by differentiating its actual ideal membership. No new equation-source restriction follows from that differentiation alone.
* The universal sum graph records the same first coefficient; the desired vanishing is exactly \(M_1=0\), not a new automatic consequence of graph compatibility.

There is a particularly concrete global comparison. Use the disjoint line \(L=V(z,w)\). Write \(F=f+zp+wq'+\cdots,\ G=g+zr+ws+\cdots\) where \(f,g\) are coprime binary forms of degrees \(a,b\). The binary CI quotient in degree \(a+b-2\) is one-dimensional. Let \(\Delta(P)\) be the determinant of the multiplication map
\[
 k[x,y]_{b-2}\oplus k[x,y]_{a-2}\to k[x,y]_{a+b-2},
 \quad(h,j)\mapsto fh+gj,
\]
with one extra column \(P\). Choose bases consistently; ratios are canonical. The Jacobian class \(D_{12}|_L\) is nonzero. The established residue identity in the spectral--Jacobian bridge gives
\[
 2M_1=ab\,\frac{\Delta(D_{03}|_L)}{\Delta(D_{12}|_L)}
       =\operatorname{Res}_{f,g}(ps-q'r).
\]
Thus on the cycle lift \(2S\Delta(D_{12}|_L)=abT\Delta(D_{03}|_L)\). Here \(\Delta\) uses the **unscaled** \(D_{03}\); using \(A=2D_{03}\) changes the factor of two. The target is exactly \(ps-q'r\in(f,g)\). This is the same one-dimensional Serre pairing from the [proof boundary](universal_first_moment_proof_boundary.md), not a fresh vanishing theorem.

The common global source of all minors can be encoded by a rank-one tensor \(c=F\otimes G\) in \(R_a\otimes R_b\), with the Segre rank-one equations. The six maps to \(R_{a+b-2}\) are linear on tensor coefficients:
\[
 x^\mu\otimes x^\nu\mapsto
 (\mu_i\nu_j-\mu_j\nu_i)x^{\mu+\nu-e_i-e_j}.
\]
When \(a=b\), these factor through the exterior square, so the pencil Grassmannian is natural. This source condition by itself does not impose the residue vanishing: pairs containing selected curves can have residual components. For example \(xy-zw,\ x^4-z^3w\) have \(2D_{03}=D_{12}=-4x^4\) on \(C\) but a residual line cycle. The full homogeneous ideal and cycle conditions are essential.

The binary pairing is a useful concrete check of any proposed geometric explanation of spectral balance, not the goal of the realization program. The [polar saturation analysis](spectral_interpolation_and_polar_saturation.md) shows that opposite first-polar identities are redundant for that particular vanishing question; they may still provide different geometric views of the same object. The balanced ambient fiber is integral; that does not prove inclusion of actual CI realizations.

The alternative direct trace formulation is \(\operatorname{Tr}_{E_0/k[z,w]}(xy)=4zw M_1\), \(E_0=k[z,x,y,w]/(F,G)\) finite graded free. This is another presentation of the same observable; a geometric account of realization need not be reduced to explaining its vanishing. Universal vanishing remains open; existing symmetry, residual and low-degree coverage remains unchanged. This account requires independent review before any new claim is promoted.
