# Complementary Chow projections and product models

**Status.** Provisional calculations in characteristic zero. Use the
[coefficient realization notation](transverse_coefficient_realization_synthesis.md).
The [trace investigation](../../investigations/trace-residue-projection-geometry/projection_resultants.md)
records the complementary resultant formulas and their first source jets.
Here the product and Grassmannian models compare the same homogeneous
equations across all three projections. Extending these models across the
exceptional boundary with the actual nonreduced structure remains open.

## 3. Product geometry: a fixed quadric and the q-translation

Use the product coordinates
\[
 a=x/z,\quad b=y/z,\quad q=xy/(zw),\qquad
 [z:x:y:w]=[1:a:b:ab/q].
\]
Over nonzero \(q\), the graph of the quadric pencil is
\(\mathbf P^1_a\times\mathbf P^1_b\times\mathbf G_m\);
its slice is the Segre quadric \(Q_q\).
The orbit closure in the slice is \(b=ua^3\), of multidegree
\((1,3,0)\) as a map from its normalization.
Distinct \(q\)'s are separated by this graph; at a fixed \(q\),
distinct \(u\)'s meet with length three at each of the two corners.
Three successive point blowups at either corner turn the local
cubic graphs into separated fibers with parameter \(u\) or its
reciprocal; self-intersection drops from six to zero.

The six elementary coordinate projections have ratios
\[
 (r_{01},r_{02},r_{03},r_{12},r_{13},r_{23})
  =(a,b,ab/q,b/a,b/q,a/q)
\]
and degrees \((1,3,4,2,3,1)\) on the normalization.
Triangle identities are \(r_{ij}r_{jk}=r_{ik}\).
Opposite edges recover \(q=r_{01}/r_{23}=r_{02}/r_{13}\),
and \(r_{12}^2/r_{03}=\eta\).
Any spanning tree of the four coordinate vertices gives a birational
three-ratio product model (six elementary ratios, sixteen labeled
spanning trees, not six trees). For example the successive-ratio
model has multidegree (1,2,1). The blowup of four coordinate points
followed by the six strict coordinate lines, the standard
permutohedral toric threefold, resolves all six elementary ratios.
The pullback of \(O(1)\) under \(r_{ij}\) has class
\(H-E_k-E_l-E_{kl}\) for complementary indices \(k,l\), with total
pullback convention for the point classes. A further fan refinement
may be needed for the \(q\)-character itself. This resolution is
distinct from the normalized Chow quotient: see
[quotient fan and blowup comparison](chow_quotient_fan_and_blowup_comparison.md).

For a homogeneous degree-\(d\) form, the product dictionary is
\[
 F(1,a,b,ab/q)=\sum_{r,s=0}^{d} a^rb^sf_{rs}(q),\qquad
 f_{rs}(q)=\sum_{\ell=\max(0,r+s-d)}^{\min(r,s)}
 c_{d-r-s+\ell,r-\ell,s-\ell,\ell}q^{-\ell}.
\]
It follows term by term from the monomial substitution.
The boundary coefficients of the bidegree square have only one
allowed Laurent power of \(q\). Homogenization uses a subsystem of
\(O(d,d,d)\), with base loci at boundary \(q\)-values.
For a generic nonzero quadric parameter not among the \(q_i\), the
restricted pair of bidegrees (d,d),(e,e) intersects at the two
corners with length \(4m\) each: intersect the CM curve with the
quadric, using additivity of Cartier intersection multiplicities
and order four on each normalized component at each endpoint.
At \(q_i\) the restrictions have common curves.
The strict transform of an actual pair need not remain a CI;
exceptional components and thickening data must be accounted for.

This explains why arbitrary spectra are easy on the open torus:
\(U=u_0,\ P(q)=0\). Homogenize by \(F=z^2y-u_0x^3\) and
\(G=H(xy,zw)\). On the quadric with Segre coordinates
\(z=a_0b_0,\ x=a_1b_0,\ y=a_0b_1,\ w=a_1b_1/q_i\),
\(F=b_0^2(a_0^3b_1-u_0a_1^3b_0)\).
Thus the intersection has the desired cycle plus \(2m\) times the
line \(z=x=0\). The obstruction must use projective extension,
not just the existence of a torus algebra with prescribed norm.

## 4. Three Segre surfaces in Gr(2,4)

Use primal Plücker coordinates \(p_{ij}\). The lines joining points
on two complementary coordinate lines form a Segre surface
\(\Sigma_{ij|kl}=V(p_{ij},p_{kl})\cap\operatorname{Gr}(2,4)\).
For each pairing use coordinates \([A_0:A_1]=[x_i:x_j]\) and
\([B_0:B_1]=[x_k:x_l]\) on the two factors. Let \(R_\sigma\) be
the full projective Chow form, and
\(K_\sigma(U,V)=\prod_i(U-\eta_i V)^{n_i}\).
The [three homogeneous restrictions](../../investigations/trace-residue-projection-geometry/projection_resultants.md#homogeneous-chow-restriction-formulas)
give the endpoint monomials and the two spectral polynomials on these
Segre surfaces. The exponents of the spectral factors are the mapping
degrees \(1,3,2\) onto the respective projected images.

For an actual CI the same Chow form is the determinant of the
Sylvester map on every line \(\ell\):
\[
 H^0(O_\ell(e-1))\oplus H^0(O_\ell(d-1))
 \longrightarrow H^0(O_\ell(d+e-1)),\quad
 (P,Q)\longmapsto PF|_\ell+QG|_\ell .
\]
Thus the same unknown pair must produce all three factorizations,
not three independently chosen resultants. The exact general
criterion is existence of such a resultant presentation by a
proper pair; our task is to extract simpler coefficient conditions.
Compatibility of the three restrictions as sections of the Chow
line bundle alone is automatic for every cycle and cannot obstruct CI.
A useful further condition must use the common equation presentation.

The [quadratic Chow variation at the disjoint line](../../investigations/trace-residue-projection-geometry/projection_resultants.md#common-center-lvzw)
weights the two opposite graph charts in the ratio \(1:3\).
That cycle-level identity is automatic. Additional constraints would
have to use the common equation presentation.

## 4a. The six-line configuration: two rulings and a secant projection

The complementary-pair geometry has a direct common surface interpretation. Write \(L_{ij}\) for the span of coordinate vertices \(i,j\), not the line cut out by those coordinates. Projection from \(L_{ij}\) to the opposite coordinate line has degree \(d\) on each normalized translated quartic; its base divisor has orders \(c_0,c_\infty\) at the endpoints:

| Center | \(d\) | \(c_0\) | \(c_\infty\) |
|---|---:|---:|---:|
| \(L_{01}\) | 1 | 3 | 0 |
| \(L_{23}\) | 1 | 0 | 3 |
| \(L_{02}\) | 3 | 1 | 0 |
| \(L_{13}\) | 3 | 0 | 1 |
| \(L_{03}\) | 2 | 1 | 1 |
| \(L_{12}\) | 4 | 0 | 0 |

These are just the orders of the two complementary coordinate sections of \(O_{\mathbf P^1}(4)\) after removing their common factor, so \(d+c_0+c_\infty=4\). For a full translated cycle of multiplicity \(m\), a generic plane through the center meets it in a moving part of length \(dm\) and fixed endpoint parts of lengths \(c_0m,c_\infty m\), by the Cartier intersection formula (Stacks [43.16](https://stacks.math.columbia.edu/tag/0B01)). On the blowup of a complementary skew pair, the **full inverse image** of an actual CI is still a proper intersection of the two total pullback divisors: away from the centers it is the original curve and over the finitely many endpoint points it has fibers of dimension one. Its cycle consists of the strict transforms with original multiplicities plus exceptional fibers over the endpoint points on the centers, with coefficients \(c_pm\) from the table. Indeed intersect with a generic plane-pencil fiber for the projection from that center; the exceptional fiber maps isomorphically to the pencil base, and the strict transforms avoid the fixed endpoint in a generic such slice. This proves the coefficients by the preceding plane length calculation. This concerns the pairwise line blowups, not the full inverse image on the common resolution after blowing up points, which can contain exceptional surfaces. The product of the two projections gives the joining-line bundle over \(L_{ij}\times L_{kl}\) (the projective bundle of lines in \(O(-1,0)\oplus O(0,-1)\)); its projection of the full CI cycle is the Chow restriction in Section 4. Generic degree of a reduced component onto its projected image is not the scheme-theoretic fiber length of an arbitrary nonreduced thickening.

On a fixed smooth quadric \(Q_c=V(xy-czw)\), use the dense Segre chart
\[
 [z:x:y:w]=[1:A:B:AB/c].
\]
Here the first complementary pair \(01|23\) produces precisely the ruling \(A=\mathrm{constant}\): the joining line runs from \([1:A:0:0]\) to \([0:0:1:A/c]\). The second \(02|13\) produces the other ruling \(B=\mathrm{constant}\). The third \(03|12\) produces secants: on the torus its two coordinates are
\[
 R=AB/c,\quad S=B/A,\qquad A^2=cR/S,\quad B^2=cRS .
\]
The two preimages are exchanged by the simultaneous sign involution \((A,B)\mapsto(-A,-B)\) (characteristic not two). For \(B=uA^3\), \(S^2/R=uc=\eta\) when \(q=c=u/v\). Thus on a common quadric the three line models are the two rulings and a two-to-one secant projection, not three unrelated observations. The projection degree two holds on the torus; the rational map has boundary base loci and its exceptional structure must not be treated as an everywhere finite quotient of \(Q_c\). At the scheme level the sign involution preserves the cycle, but need not preserve an arbitrary thick CI ideal. Compare the existing [sign-symmetry theorem](chow_acm_parity_vanishing.md) and [actual source comparison](sign_symmetry_and_actual_sources.md). The fixed quadric and the two-to-one projection explain why \(q,\eta\) jointly encode the orbit, while separate projected spectra can forget pairing and thick structure.

### Common coordinate planes and what line data does not see

The four coordinate planes give a particularly elementary comparison of the three pencil descriptions: every coordinate plane contains three edges, and is a special member of each of their plane pencils. An actual full translated-cycle CI cuts each plane in a finite plane CI of length \(4m\), with lengths at \(p_0,p_\infty\) respectively:
\[
 z=0:(0,4m),\quad x=0:(m,3m),\quad
 y=0:(3m,m),\quad w=0:(4m,0).
\]
This follows directly from the four coordinate orders on the normalization. The restriction of the two equations to an edge is common to the two adjacent plane sections. In particular the two planes \(z=0\) and \(w=0\) share the disjoint edge \(L_{12}\), and the first-normal-jet comparison there is the alternating comparison of the first layers of those two plane restrictions, not isolated data on that edge. The generic pencil contact at a fixed endpoint is not in general the length of the scheme-theoretic intersection with the center edge: in a local ring \(A_p=O_{Z,p}\) the latter is a quotient by both center equations, whereas the former is a quotient by one generic linear combination. The inequality follows from that surjection.

The established [first-jet flexibility family](sole_support_first_jet_gate.md) is a useful concrete control for this whole configuration. At \((4,4)\) take \(Q=zw-xy\) and
\[
 F=x^4-z^3w+\lambda zQx,\quad G=y^4-zw^3+\mu wQy.
\]
For all \(\lambda,\mu\), the restrictions of both forms on **all six edges** are identical to those of the invariant binomial pair (\(\lambda=\mu=0\)): every perturbing monomial uses at least three distinct coordinates. All four coordinate-plane intersection cycles also have exactly the prescribed lengths with \(m=4\). On \(z=0\) the first form is \(x^4\), and its common zero with the second is only \(p_\infty\); on \(w=0\) the second is \(y^4\), and their common zero is only \(p_0\). Both lengths are sixteen by Bezout. On \(x=0\), the first form is \(-z^3w\); restriction of the second to \(z=0\) or \(w=0\) there is \(y^4\). Cartier intersection additivity gives lengths \(4\) at \(p_0\), \(12\) at \(p_\infty\). On \(y=0\) the second is \(-zw^3\), and the same argument with \(x^4\) gives \(12,4\). Yet the cofactor transition on the disjoint edge is \(\lambda\mu\,d(y/x)/(y/x)\) (Section 9 of [plane-pencil account](plane_pencil_equation_bundles.md)). In particular for \(\lambda\mu\ne0\) these are not full translated-cycle pairs: on substituting \([1:t:ut^3:vt^4]\), the first equation requires \(v=u=1\) for an entire translated component, while the generic length along that component is one by the existing flexibility calculation. All six edge restrictions and the four special-plane *cycles*, even jointly, fail to determine the geometry of the moving intersections. The full plane schemes are not claimed equal.

We can see exactly where the missing intersection goes on the common quadrics. For \(q=c\ne0,1\), use the torus coordinates \(t,u,v\) with \(u=cv\) in this control. The two equations, divided by their nonzero torus monomials, become
\[
 1-v+\lambda t v(1-c)=0,\qquad
 c^4v-1+\mu c(1-c)/t=0 .
\]
Eliminate \(v\):
\[
 c^4t=(t-\mu c(1-c))(1-\lambda t(1-c)).
\]
For \(\lambda\mu\ne0\) this is a quadratic in \(t\) with nonzero leading and constant coefficients for every \(c\ne0,1\). Its roots over an algebraically closed field are nonzero, and none zeros \(1-\lambda t(1-c)\) (the left hand side would be nonzero). They give actual intersection points in the torus of every such \(Q_c\). By contrast for the invariant pair the only smooth-quadric fibers with torus intersections are \(c^4=1\); there the torus common loci are the translated quartics. The two ruling descriptions see the same off-endpoint points, and the third observes their secant projections. This is an elementary control, not a new obstruction: it identifies the geometric information lost by looking only at the edges and special-plane lengths.

The constructive comparison is therefore to keep the **same two restricted curves on the varying quadrics**, including their actual common schemes, and use the two rulings to compare them with the secant observation. The prescribed full translated-cycle geometry says that for \(c\) outside its spectrum the common scheme of the two restricted curves is entirely at the two corners (length \(4m\) each, as in Section 3). For spectral fibers the common curves and their residual/embedded scheme structures must be retained. This comparison returns to the existing product dictionary without requiring another auxiliary bundle. The standard blowup and intersection inputs plus the explicit control establish the stated comparisons; there is no general reconstruction or new universal moment vanishing. Provisional pending independent review.


### Three independent complementary-pair product models

The two opposite ratios together with their quotient character are dependent: \((r_{01},r_{23},q)\), \((r_{02},r_{13},q)\), \((r_{03},r_{12},\eta)\) describe projected images, not birational ambient product coordinates. In particular their separate spectra forget the paired configuration. Complete each opposite pair to a spanning tree as in Section 3, keeping a degree-one parameter. One convenient (not unique) choice is
\[
 \begin{array}{c|c|c}
 &\text{coordinates}& C_{u,v}\text{ on the dense torus}\\
 I&(a,b,c)=(x/z,w/y,y/z)&(r,(v/u)r,ur^3)\\
 II&(d,e,r)=(y/z,w/x,x/z)&(ur^3,vr^3,r)\\
 III&(p,h,r)=(w/z,y/x,x/z)&(vr^4,ur^2,r).
 \end{array}
\]
The homogeneous graph parametrizations are respectively
\[
 ([s:t],[us:vt],[s^3:ut^3]),\quad
 ([s^3:ut^3],[s^3:vt^3],[s:t]),\quad
 ([s^4:vt^4],[s^2:ut^2],[s:t]).
\]
The inverse ambient maps are \([1:a:c:bc]\), \([1:r:d:re]\), \([1:r:rh:p]\); thus the transitions are
\[
 I\to II:(c,bc/a,a),\quad I\to III:(bc,c/a,a),\quad
 II\to III:(re,d/r,r).
\]
These are monomial torus isomorphisms (unimodular changes of character basis), rational maps on the products, and resolve on the already-described common toric modification. They commute on the dense torus and the individual curve maps extend on their normalizations. Do not infer everywhere-defined product automorphisms or identical closures of arbitrary thick schemes. Each individual reduced graph is a CI of its two graph equations, but the sum of graphs with cycle multiplicities is not a specification of an actual thick scheme.

In model II, in homogeneous coordinates \(D,E,R\) on the factors, a single graph is defined by \(D_1R_0^3=uD_0R_1^3,\ E_1R_0^3=vE_0R_1^3\). Model I has \(uB_1A_0=vB_0A_1,\ C_1A_0^3=uC_0A_1^3\); model III has \(P_1R_0^4=vP_0R_1^4,\ H_1R_0^2=uH_0R_1^2\). Thus the full translated cycle in each product is the sum of these explicit graphs with coefficients \(n_i\).

On the common longitudinal fiber \(r\ne0\), the paired coordinates in II are \(d/r^3=u,\ e/r^3=v\). The fiber Chow polynomial in \(d,e\) is
\[
 \prod_i(X+u_i r^3Y+v_i r^3Z)^{n_i}=\mathcal C_\sigma(X,r^3Y,r^3Z).
\]
In I use \((c/a^3,bc/a^4)\), and in III use \((h/r^2,p/r^4)\), to obtain the identical normalized paired polynomial. The same characters in the three product models are
\[
 q=a/b=d/e=r^2h/p,\qquad
 \eta=c/(a^2b)=d^2/(r^3e)=h^2/p.
\]
These give the same weighted moment \(M_1\) and the two marginal spectral polynomials \(H,K\); the full paired polynomial is needed to preserve pairing. Projection to the two opposite factors alone gives image graphs of bidegrees \((1,1),(1,1),(1,2)\) (with the latter ordering interpreted as degree in the first and second variables of the equation), with generic mapping degrees \(1,3,2\), respectively; equivalently the last image equation is linear in \(p\) and quadratic in \(h\). These are not the multidegrees of the three embedded graphs above.

An actual degree-\(D\) homogeneous polynomial \(F\) has the three torus expressions \(F(1,a,c,bc), F(1,r,d,re), F(1,r,rh,p)\). They agree by substitution, and their allowed monomials are indexed by the same ordinary-degree-\(D\) tetrahedron; homogenize separately and track exceptional factors on the common blowup. This is the concrete common-equation constraint, stronger than choosing unrelated graph equations on each product. The dense-torus dictionary and cycle images are explicit; boundary descent of a realizing scheme remains the missing part. No new sufficiency or moment theorem asserted.


### The common logarithmic differential geometry

For a smooth toric compactification with its full toric boundary \(D\), the standard character-lattice description is \(\Omega^1(\log D)=O\otimes_{\mathbb Z}M\) (Danilov, *The Geometry of Toric Varieties*, and Cox--Little--Schenck, *Toric Varieties*, Chapter 8). Thus toric refinements identify the pulled-back logarithmic cotangent bundles. With \(\ell=d\log r,\alpha=d\log U,\beta=d\log V\), the three product bases are
\[
 I:(\ell,\ell+\beta-\alpha,3\ell+\alpha),\quad
 II:(3\ell+\alpha,3\ell+\beta,\ell),\quad
 III:(4\ell+\beta,2\ell+\alpha,\ell).
\]
The fixed quadric product gives \((\ell,3\ell+\alpha,\alpha-\beta)\). In particular the character basis \((r,q,\eta)\) has \(d\log q=\alpha-\beta,\ d\log\eta=2\alpha-\beta\), and
\[
 \ell\wedge d\log q\wedge d\log\eta=\ell\wedge\alpha\wedge\beta.
\]
On an individual reduced graph the two transverse forms vanish after restriction to ordinary differentials on the curve and form a normal covector basis before restriction. On nonreduced schemes they need not vanish. This describes the log-normal geometry, not ordinary conormal lattices at the boundary.

The earlier differential is exactly \(q\,d\log(y/x)=q(2\ell+\alpha)\) on the torus, with weighted fundamental-class branch expression \(2n_iq_i\ell\). The same construction can be read cycle-first: for any Laurent polynomial \(\varphi(U,V)\) assign the branch tuple \((n_i\varphi(u_i,v_i)\,dr/r)_i\). On the reduced union of the distinct graphs in projective space, Rosenlicht's residue criterion says that this tuple is a regular dualizing differential iff \(\sum_i n_i\varphi(u_i,v_i)=0\). Indeed only the two endpoints are shared, the poles are simple, and a regular germ takes the same value on every branch above an endpoint. This is the standard reduced-curve theorem (Rosenlicht; see also https://doi.org/10.1007/s11565-024-00495-8), not a CI-specific vanishing theorem. For a CM thickening, finite duality for the closed immersion of its reduction identifies the latter's dualizing sheaf with \(\operatorname{Hom}_{O_Z}(O_{Z_{\mathrm{red}}},\omega_Z)\subset\omega_Z\). Hence the regular tuples yield regular dualizing sections on a realizing thickening too; they are not arbitrary Kähler forms on it. In characteristic zero, interpolation in the two transverse characters gives all tuples of coefficients with sum zero, a space of dimension number of distinct components minus one. This simple-pole subspace depends on the support and the marked endpoints, not on higher transverse nilpotent motion. The first moment is the instance \(\varphi=2q\). This explains precisely which part of logarithmic gluing follows from the classical residue criterion and which additional boundary information is required for realization. No new universal moment vanishing is claimed.
