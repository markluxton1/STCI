# Constructing CI equations from transverse Chow coefficients

**Status:** research synthesis and elementary comparisons, characteristic zero unless stated otherwise. The organizing principle is a research objective, not a new universal exclusion theorem. Existing proof owners are linked below. The additional product/Grassmannian and centered-section formulas are recorded with their derivations for subsequent independent review.

## 1. The organizing principle: build the equations from the cycle

Start with the unordered configuration
\[
 \sigma=\sum_i n_i[(u_i,v_i)]\in\operatorname{Sym}^m T,\quad
 T=(\mathbf G_m)^2,\quad m=\sum_i n_i,\quad
 C_{u,v}=[s^4:s^3t:u st^3:v t^4].
\]
Write \(z,x,y,w=x_0,x_1,x_2,x_3\), \(A=xy,\ B=zw\),
\(q_i=u_i/v_i\), and \(\eta_i=u_i^2/v_i\).
For fixed degrees \(d,e\) with \(de=4m\), the objective is to describe
the realization locus \(\mathcal R_{d,e}\) of configurations that are
the **entire fundamental cycle** of an actual proper pair \(F_d,G_e\).

Reverse the usual order of investigation. Rather than select a carrier
and seek a mate or compute an invariant after finding \(F,G\), construct
the canonical objects of \(\sigma\) first. Each then specifies
requirements on the unknown equations: ideal memberships and their
Koszul cofactors, prescribed section spaces and line bundles,
determinantal presentations, compatibility of gradients, and gluing
through the coordinate boundary.

The polynomials
\[
 \mathcal C_\sigma(X,Y,W)=\prod_i(X+u_iY+v_iW)^{n_i},\qquad
 H_\sigma(A,B)=\prod_i(A-q_iB)^{n_i}
\]
are the natural coefficient coordinates of this realization problem.
The latter is a specialization of the former:
\[
 H_\sigma(A,B)=\mathcal C_\sigma(0,-B,A)/\mathcal C_\sigma(0,0,1).
\]
The full transverse Chow polynomial determines the cycle but not a
nonreduced scheme realizing it. The realization locus is constructible
(by the proper-pair locus and the Chow-form/resultant morphism);
equations alone need not describe it. The exact reduced-cycle criterion,
including a coprime-pair condition, is already proved in
[transverse Chow coefficients](transverse_chow_moment_realization.md).
The moving nonreduced case is the genuine gap.

**Research objective:** understand the geometry of realization: how an orbit configuration, a family of embedded transverse neighborhoods, and a common global section of two prescribed line bundles fit together. The coefficient relations record this geometry. Spectral balance is one informative test case, not the organizing principle, and obtaining an exclusion is not a prerequisite for useful understanding.

### What the spectrum can and cannot encode

Write \(H=A^m-M_1A^{m-1}B+M_2A^{m-2}B^2-\cdots\).
The character \(q=xy/(zw)\) is distinguished by the relation
\(1+3=0+4\) of longitudinal weights. Under transverse torus translation
all \(q_i\) scale by the same unit, so \(M_j\) scales by its \(j\)-th
power. Vanishing is intrinsic under that symmetry, not under arbitrary
changes of character. The first condition is eigenvalue balance,
\(M_1=\sum n_iq_i=0\). On the small diagonal \(M_1=mq\ne0\) in
characteristic zero; in characteristic dividing \(m\) this separator
does not work. Equivalently,
\([YW^{m-1}]\mathcal C_\sigma=M_1[W^m]\mathcal C_\sigma\).

The full spectral polynomial alone cannot distinguish all configurations.
For example \(F=x^4-z^3w,\ G=y^4-zw^3\) realizes the four reduced
curves \(C_{\zeta,1}\) for \(\zeta^4=1\). The four curves
\(C_{1,\zeta^{-1}}\) have the same \(H=A^4-B^4\) but are all on
the irreducible cubic \(z^2y-x^3=0\). Any quartic containing them
must contain the cubic by degree exhaustion (16 > 12), so there is
no proper (4,4) pair for this second cycle. In fact the existing
[degree-four spectral surjectivity](chow_realization_moment_separation.md)
shows every depressed quartic with nonzero constant term occurs.
No further universal independent equation in just those quartic
spectral coefficients should be sought. The paired information in
\(\mathcal C_\sigma\) is indispensable for full realization.
The reciprocal first moment is not universally zero either.

## 2. The endomorphisms arise from the configuration itself

The projected effective divisor \(D=\sum_i n_i[q_i]\) on
\(\mathbf G_m\) has coordinate ring
\[
 E_D=k[T,T^{-1}]/(P(T)),\qquad P(T)=H(T,1).
\]
Multiplication by \(T\), denoted \(\Phi\), has characteristic polynomial
\(P\), trace \(M_1\), exterior-power traces \(M_j\), and determinant
\(M_m\). Its traces of powers are the spectral power sums (Newton
identities in characteristic zero). Basis change conjugates \(\Phi\);
transverse translation scales it. This gives a direct reason to think
of balance as tracelessness. The projected-divisor algebra is **not**
the actual CI algebra, and repeated eigenvalues need not correspond
to the same Jordan structure there.

On the dense projective torus use
\[
 r=x/z,\quad U=z^2y/x^3,\quad V=z^3w/x^4,\quad
 [z:x:y:w]=[1:r:Ur^3:Vr^4].
\]
Each orbit is \(\mathbf G_m\times\{(u_i,v_i)\}\). The actual CI
restricts to a finite flat rank-\(m\) algebra over \(k[r^{\pm1}]\)
(the support is finite over the base, the nilpotent thickening is
finite, and CM implies torsion-freeness). Its commuting multiplication
operators have
\[
 \det(TI-\mu_{U/V})=P(T),\qquad
 \det(XI+Y\mu_U+W\mu_V)=\mathcal C_\sigma(X,Y,W).
\]
These identities follow by filtering each local generic algebra by
its maximal ideal; they retain multiplicity without requiring an
invariant CI ideal. See the [constant fat-point envelope](full_transverse_chow_pullback_envelope.md)
and the [embedded quotient framework](../../frameworks/embedded-torus-quotients/index.md).
Cayley--Hamilton is available but not the starting point.

Projection from \(L=V(z,w)\) instead has rank \(4m\).
For the finite flat projection onto \([z:w]\), the characteristic
polynomial of multiplication by \(q\) on the generic fiber is \(P^4\).
The polynomial \(P\) itself annihilates the generic algebra, since
each local generic length is \(n_i\). Homogenizing and using
unmixedness gives \(H(xy,zw)\in(F,G)\).

The elementary motivation for trace is summing over a fiber:
on \(z=1\), \(t^4=w/v_i\), \(xy=q_iw\).
Thus \(\operatorname{Tr}(xy)=4zwM_1\). The residue identity is
the corresponding coefficient-extraction operation. For monic
\(f\) with distinct roots \(r_j\), Lagrange interpolation gives
\([t^{\deg f-1}](h\bmod f)=\sum_j h(r_j)/f'(r_j)\);
replacing \(h\) by \(hf'\) recovers the trace. The multivariable
finite-CI version is the standard Scheja--Storch/Grothendieck residue
pairing; see [spectral--Jacobian bridge](spectral_jacobian_first_jet_bridge.md).

The explicit degree-(2m,...,3m) quadric/cubic polar coefficients also
belong to the actual ideal. They constrain construction of the pair.
Use the [polarization proof](weighted_chow_quadric_cubic_polarizations.md)
with its [saturation correction](spectral_interpolation_and_polar_saturation.md):
the two opposite chains give the same dense-torus envelope, and their
syzygy containing \(M_1\) is not an independent obstruction.

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
Up to nonzero scalar the restrictions are
\[
\begin{aligned}
 R_\sigma|_{\Sigma_{01|23}}&=A_1^{3m}B_0^{3m}H(A_1B_0,A_0B_1),\\
 R_\sigma|_{\Sigma_{02|13}}&=A_1^mB_0^mH(A_1B_0,A_0B_1)^3,\\
 R_\sigma|_{\Sigma_{03|12}}&=(A_0A_1)^m
 K_\sigma(A_0B_1^2,A_1B_0^2)^2 .
\end{aligned}
\]
Derivation: substitute the parametrization into
\(A_0x_j-A_1x_i\) and \(B_0x_l-B_1x_k\) and take their binary
resultant. For the first pairing the two factors are
\(s^3(A_0t-A_1s),\,t^3(vB_0t-uB_1s)\);
for the second they are
\(s(A_0ut^3-A_1s^3),\,t(B_0vt^3-B_1s^3)\);
for the third they are
\(vA_0t^4-A_1s^4,\,st(uB_0t^2-B_1s^2)\).
Multiplicativity gives the displayed endpoint monomials and
spectral factors. All have bidegree (4m,4m).
The exponents 1,3,2 are the degrees onto the respective
projected images. These are Chow-cycle identities, also valid
with multiplicities, not assertions about exceptional schemes.

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

At the disjoint line \(L=V(z,w)\), put
\(z=\alpha x+\beta y,\ w=\gamma x+\delta y\).
The two opposite families give the exact restrictions
\(R(\alpha,0,0,\delta)=H(1,\alpha\delta)\) and
\(R(0,\beta,\gamma,0)=H(1,\beta\gamma)^3\)
after normalizing \(R(L)=1\). Weight symmetry eliminates all
other terms of degree at most two. Hence
\(R=1-M_1(\alpha\delta+3\beta\gamma)+O(3)\).
The ruling degrees explain the two Hessian coefficients.
The [existing Chow/first-jet comparison](transverse_chow_moment_realization.md)
identifies the equation-side coefficient; no Hessian vanishing
for arbitrary proper pairs is proved.



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


### Minimal weighted logarithmic comparison for the first moment

For this scalar the full nonreduced conormal module is unnecessary. Work with the normalized reduced graphs and their generic multiplicities \(n_i\). The same rational differential in the independent products is
\[
 \theta=q\,d\log r
 =\frac ab\,d\log a
 =\frac de\,d\log r
 =\frac{r^2h}{p}\,d\log r .
\]
Its weighted branch tuple is \((n_iq_i\,dr/r)_i\). For any of the six elementary coordinate projections, the restriction to the normalization of a branch is \(T=c_i r^k\), with \(k=1,3,4,2,3,1\) respectively. In characteristic zero its function-field differential trace sends \(q_i\,dr/r=(q_i/k)dT/T\) to \(q_i\,dT/T\): the separable extension has degree \(k\). Thus all six weighted traces are \(M_1\,dT/T\). This comparison uses only the cycle, not its scheme structure or a putative finite morphism on the original projective curve at a base point.

By Rosenlicht's residue criterion for a reduced curve (e.g. https://doi.org/10.1007/s11565-024-00495-8), a tuple with at most simple poles is regular dualizing precisely when the coefficients sum to zero at each group of branches meeting at a point. In the three independent product models I, II, III, all reduced graphs meet at the same two corners, and do not meet away from them. Thus regularity of this weighted tuple in any one of the three is equivalent to regularity in all three, equivalent to \(M_1=0\). Intersecting those particular regularity conditions gives no stronger first-moment equation. In the fixed-quadric product \((r,B,q)\), however, different values of \(q\) are separated at the endpoints. The sums at the corners of the \(q=c\) slice are \(\pm c\sum_{q_i=c} n_i\). They are nonzero in characteristic zero whenever that slice occurs. Regularity on the separated model would therefore be too strong even for balanced realizations. The relevant phenomenon is cancellation under contraction, not ordinary pullback regularity across all exceptional divisors. Dualizing pushforward/trace, rather than an assumed pullback of regular dualizing forms, is the appropriate direction. This distinction concerns weighted simple-pole tuples on reduced supports, and finite duality supplies the interpretation on any realizing CM thickening as in the preceding section.

All the monomial transitions and the graph defining equations are compatible for the single graph \(C_{u,v}\), where \(M_1=q\ne0\). In particular these transitions alone do not force regularity of the weighted tuple. Even the two homogeneous equations \(z^2y-u x^3,\ z^3w-vx^4\) define that graph on the dense torus; their projective intersection also contains the coordinate line \(z=x=0\) (residual cycle degree eight by Bezout, since on \(z\ne0\) the intersection is the reduced quartic chart). They are not a proper realization of the sole graph as the entire cycle. The minimal outstanding implication is from actual global proper two-equation realization without boundary or other residual cycles to the weighted residue cancellation at a single contracted endpoint. This is the known UM1 gap, not a new theorem; no thick-structure classification is required to state or check that target. Conversely one cannot infer it from the weighted cycle alone. Provisional pending review.


### Degree exhaustion in the fixed-quadric product

The equality \(ab=4m\) gives a particularly elementary form of the complete-cycle hypothesis. On a nonspectral nonzero quadric, the restrictions of \(F_a,G_b\) have bidegrees \((a,a),(b,b)\), and their intersection number \(2ab=8m\) is exhausted by the two corner lengths \(ab\) each. On the product over \(\mathbf G_{m,q}\), the intersection cycle of these restrictions (viewed as divisors of the threefold) consists precisely of the graph cycles with weights \(n_i\) and the two constant corner sections with coefficients \(ab\). Indeed away from the four base edges of the quadric pencil the map to projective space is locally an isomorphism, and along the edges the original CI meets only the two endpoints; the generic transverse slice gives the corner coefficients. This cycle statement does not prescribe the schemes along those sections.

Fix a general \(A\ne0,\infty\). Compactifying its slice to \(\mathbf P^1_B\times\mathbf P^1_q\), the inverse rational map in homogeneous coordinates is
\[
 [z:x:y:w]=[Q_0B_0:Q_0AB_0:Q_0B_1:Q_1AB_1].
\]
The two substituted forms have bidegrees \((a,a),(b,b)\). Their binary resultant in \(B\) is homogeneous of degree \(2ab\) in \([Q_0:Q_1]\). It is nonzero at \(Q_1=0\), since the resulting joining line in the plane \(w=0\) misses \(Z\). For nonzero finite \(q\), each graph meets the slice once, and multiplicativity of the existing Chow/resultant identity (Section 4) gives the roots \(q_i\) with multiplicities \(n_i\). The remaining root is \(q=0\), where there is a common collapsed boundary fiber. Consequently with monic normalization in the affine parameter \(q\),
\[
 R_A(q)=q^{2ab-m}H(q)=q^{7m}H(q),\qquad H(q)=\prod_i(q-q_i)^{n_i}.
\]
Fixing a general \(B\ne0,\infty\) instead gives the symmetric substitution \([Q_0 A_0:Q_0 A_1:Q_0 B A_0:Q_1 B A_1]\); each graph meets the slice three times in characteristic zero. The analogous resultant in \(A\) is
\[
 R_B(q)=q^{2ab-3m}H(q)^3=q^{5m}H(q)^3 .
\]
This is exactly the already-proved pair of ruling Chow restrictions, read with the homogenizing factors of the product model. The normalization is separately by the nonzero value at infinity. Neither resultant degree is the length of the moving zero-dimensional scheme alone, because the degenerate quadric contributes a common boundary fiber.

The first subleading coefficients are \(-M_1\) and \(-3M_1\) respectively. Degree exhaustion fixes the large root multiplicities at zero, and fixes the degrees of the remaining factors, but imposes no vanishing of the subleading coefficient by itself. In particular both monic factorizations are algebraically consistent for arbitrary monic \(H\) of degree \(m\) with nonzero constant term. The genuine remaining question is whether being the two resultant presentations of the **same global pair** implies the vanishing of that coefficient, in addition to the already automatic relation \(R_A^3=q^{16m}R_B\). This recovers the existing Chow/first-jet gate in a simple product/Bezout picture; no new independent moment condition follows. Provisional synthesis.

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

## 6. Grassmannian sum pencil and return to equations

The [Grassmannian sum and conormal compatibility account](grassmannian_sum_and_conormal_compatibility.md) records the enlarged relative Grassmannian, the direct sum-pencil blowup (without resolving individual spectral pencils), the integral ambient finite fibers, collision relations, the intrinsic conormal graph and the compatible weighted q-form. It distinguishes graph incidence from a canonical lift of nilpotent Plücker data and records the scalar supplied by the actual cycle.

Work backwards geometrically, not by eliminating all structure to reach a single equation. Section 0 of the companion account interprets the orbit quotient, fixed fat-point envelope, moving transverse neighborhoods, the two normal geometries, compatible forms as functorial conormal maps, and the sum graph as the resolution of an observable. The weighted q-form follows from spectral ideal membership and Euler, but its geometric content is the factorization through the projected cycle divisor. The first-normal-jet pairing is an independent presentation of one observable, not the immediate objective of the realization program. No new UM1 coverage is asserted.

## 7. What to carry forward

* Use the existing reduced-cycle evaluation/moment-matrix criterion
  as the constructive model, and the canonical fat-point envelope
  for repeated components. Do not infer scheme structure from trace.
* Reconstruct each intrinsic construction in terms of its geometric objects, maps and forgotten information. Use coefficient relations to express the geometry, and distinguish automatic functorial compatibility from additional global realization information.
* Compare the common homogeneous equation presentation across the
  product models and the three Grassmannian restrictions. Boundary
  compactification is essential; arbitrary spectra occur on the torus.
* Treat the line-bundle/section viewpoint as a source of constructive
  requirements on the unknown pair, not an assertion that every
  compatible list of sections integrates to homogeneous gradients.
  Hartshorne--Serre gives the established subcanonical lci-to-rank-two
  bundle construction; a CI corresponds to a split bundle, and
  prescribing the cycle is weaker than prescribing an lci scheme.
* Use the first moment as one observable for comparing the constructions, not as the definition of progress. Neither centered regularity nor the spectral polynomial recurrences remove the scalar term. No universal first-moment vanishing is proved here.

The current proof boundary is maintained in
[universal first moment proof boundary](universal_first_moment_proof_boundary.md)
and the [corpus synthesis](universal_first_moment_corpus_review.md).
This synthesis records the geometric motivation and interfaces, not a
parallel proof of the established results or a replacement for the
existing open-problem priorities.
