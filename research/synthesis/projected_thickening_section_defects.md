# Projected thickenings and missing homogeneous sections

**Scope and status.** Independently reviewed provisional mathematical deductions; no canonical result is promoted. The fixed curve is C0 over an algebraically closed field. The stated parameter-sequence and binary-mixture generalizations hold over any field. The characteristic hypothesis is that the positive binary degrees u,v have nonzero product in the field; characteristic two with odd u,v is included. This settles the previously undecided ACM question for these actual projected schemes. It does not cover arbitrary supported thickenings or arbitrary primary lifts. Characteristic-zero STCI remains open.

The target of this construction test is a homogeneous ACM thickening in the fixed downstairs \(\mathbf P^3\). It is weaker than an AG thickening there, which in codimension two would be a complete intersection. [Singh–Walther, Example 3.5 and Question 3.6](https://www.math.utah.edu/~singh/publications/singh_walther_pure.pdf) ask the still weaker historical question whether the exact quartic ideal is the radical of an ideal with CM quotient, without requiring homogeneity. This attribution does not assert that every later publication has been checked. The CI sources here, and the basic-double-link ACM schemes in the [supported-linkage account](supported_linkage_operations.md), live upstairs on \(Q_3\subset\mathbf P^4\). Their ACM property alone supplies no ACM conclusion about their four-coordinate images in \(\mathbf P^3\); the theorem below proves failure for the displayed power and binary-mixture images.

## Uniform failure of ACM for the actual power images

Let k be an algebraically closed field, let \(u,v>0\), and assume
\(uv\ne0\) in k. Put
\[
S=k[a,b,c,d],\quad r=2bc-ad,\quad
E=S[z]/(z^2-r),\quad f=b^2-az,\quad g=c^2-dz.
\]
Define the actual source and its four-coordinate image by
\[
B_{uv}=E/(f^u,g^v),\qquad
A_{uv}=\operatorname{image}(S\longrightarrow B_{uv}),\qquad
Y_{uv}=\operatorname{Proj}A_{uv}.
\]
Their reduced supports are the rational normal quartic upstairs and C0
downstairs. The source is a complete intersection and the projection is
finite. These facts hold in every characteristic: on \(a\ne0\), the
reduced equations give \(z=b^2/a,\ c=b^3/a^2,\ d=b^4/a^3\); on \(a=0\),
they give \(b=c=z=0\). Hence the three equations have height three.

**Theorem.** Every \(Y_{uv}\) with \(uv\ne0\) in k is not ACM. In
particular, no member of this entire characteristic-zero family is ACM.
More precisely, if \(e=2u+2v-3\), then
\[
\dim H^1(\mathbf P^3,\mathcal I_{Y_{uv}}(e))\ge1,\quad
\dim H^1(\mathbf P^3,\mathcal I_{Y_{uv}}(e+1))\ge2,\quad
\dim H^1(\mathbf P^3,\mathcal I_{Y_{uv}}(e+2))\ge1.                    \tag{1}
\]
These are lower bounds, not a computation of the whole Rao module.

Reduce the power relations using the monic quadratic equation:
\[
f^u=P_u+Q_uz,\qquad g^v=R_v+T_vz,\qquad
K_{uv}=(P_u,Q_u,R_v,T_v)\subset S.
\]
The four S-module relation vectors of B are
\[
(P_u,Q_u),\ (rQ_u,P_u),\ (R_v,T_v),\ (rT_v,R_v).
\]
Quotienting by the image of the first generator, 1, gives
\[
B_{uv}/A_{uv}\simeq(S/K_{uv})(-1).                                  \tag{2}
\]
Since B is a dimension-two CI and \(\sqrt{S_+B}=B_+\),
\[
H^0_{S_+}(B)=H^1_{S_+}(B)=0,\qquad
H^1_{S_+}(A)\simeq H^0_{S_+}(B/A).                                 \tag{3}
\]
Also \(H^0_{S_+}(A)=0\), so the image ideal is saturated. Thus (3)
measures the actual image curve's Rao module, not an unsaturated
presentation artifact. Neither (2) nor (3) requires generic equality of
the full source and image schemes.

Every odd binomial term contains a, respectively d. Write
\[
Q_u=a q_u,\qquad T_v=d t_v,\qquad H_{uv}=q_ut_v.                      \tag{4}
\]
Both quotients in (4) are polynomials. Their reductions are
\[
q_u\equiv-u b^{2u-2}\pmod{(a)},\qquad
t_v\equiv-v c^{2v-2}\pmod{(d)}.
\]
The class H is annihilated modulo K by a and d. Since
\(P_u-b^{2u}\in(a)\) and \(R_v-c^{2v}\in(d)\), it is also annihilated by
\(b^{2u}\) and \(c^{2v}\). Consequently
\[
(a,d,b^{2u},c^{2v})H_{uv}\subset K_{uv},                            \tag{5}
\]
and its cyclic submodule has finite length at the irrelevant vertex.

It is nonzero. Modulo \((a,d)\), the ideal K becomes
\((b^{2u},c^{2v})\), whereas H becomes
\[
uv\,b^{2u-2}c^{2v-2}\ne0
\quad\hbox{in }k[b,c]/(b^{2u},c^{2v}).
\]
Thus \(H_{uv}\in K_{uv}^{\mathrm{sat}}\setminus K_{uv}\). Equations
(2)–(3) prove the theorem. Moreover H, bH, cH and bcH all survive,
independently in their degrees, by the same reduction. The grading
shift in (2) gives (1). This does not assert that \(b^2H,c^2H\) vanish
or identify the exact annihilator of H.

## The defect is an actual missing ambient section

The source section \(H_{uv}z\) has degree \(e=2u+2v-3\). The two
relations give
\[
aH_{uv}z=-P_ut_v,\qquad dH_{uv}z=-q_uR_v.
\]
Therefore it is represented on the target charts by
\[
-P_ut_v/a\quad\hbox{on }D_+(a),\qquad
-q_uR_v/d\quad\hbox{on }D_+(d).                                    \tag{6}
\]
These charts cover Y because they cover its reduced support C0.
Their representatives agree after injection into B, hence agree on Y.
They define a global section of \(\mathcal O_Y(e)\).

That section cannot come from an ambient degree-e polynomial: such
membership in \(A_e\) would say that \(H_{uv}=0\) in \(S/K_{uv}\),
contrary to the proof. There is no hidden difference supported only
at the cone vertex of B, since \(H^0_{S_+}(B)=0\).

This is the geometric obstruction: the section \(H_{uv}z\) has local
representatives in the retained coordinates, but lies outside their
global section ring. Raising the two source equations independently does
not remove it. The theorem concerns global ACMness, independently
of the earlier local non-Gorenstein conductor obstruction. It creates
no residual component; the reduced image remains exactly C0.

The proof uses no division by two. It remains valid in characteristic
p when \(p\nmid uv\), including characteristic two with odd u,v.
In that characteristic the covering quadric is singular, but monic
finiteness, the source regular sequence and (2)–(3) persist. The older
generic-birational conductor argument is not being extended here.
The known characteristic-two CI images at \(u=v=2^j,\ j\ge1\), fall
outside \(uv\ne0\); no conflict or conclusion about the remaining
characteristic-divisible powers follows.

## Parameter-sequence generalization

The particular r is not essential. Let \(S=k[x_0,x_1,x_2,x_3]\), let
\(\ell_1,\ell_2\) be linear forms, and let X,Y,R be quadratic forms.
Assume \((\ell_1,\ell_2,X,Y)\) is a homogeneous system of parameters.
In \(E=S[z]/(z^2-R)\), with z of degree one, impose
\[
(X-\ell_1z)^u,\qquad (Y-\ell_2z)^v.
\]
Over **any field** with \(uv\ne0\), its four-coordinate image is not ACM,
with the same Rao lower bounds (1).

Indeed E is CM of dimension four. Modulo
\(f,g,\ell_1,\ell_2\), it is a monic finite algebra over the Artinian
ring \(S/(\ell_1,\ell_2,X,Y)\). These four elements are a parameter
sequence and hence a regular sequence; B is again a dimension-two CI.
Writing \(Q_u=\ell_1q_u,\ T_v=\ell_2t_v\), the class H is annihilated
by \((\ell_1,\ell_2,X^u,Y^v)\).

In \(\bar S=S/(\ell_1,\ell_2)\simeq k[t_1,t_2]\), the two quadrics
\(\bar X,\bar Y\) form a regular sequence. The colon identity
\[
((\bar X^u,\bar Y^v):\bar X^{u-1}\bar Y^{v-1})
=(\bar X,\bar Y)
\]
proves that \(\bar H=uv\,\bar X^{u-1}\bar Y^{v-1}\) survives, and its
cyclic image has the shifted Hilbert function \(1,2,1\).
The previous torsion and section arguments apply.

For u=v=1 the projection is an isomorphism of the projective schemes:
z is recovered on the two charts from \(X/\ell_1\) and \(Y/\ell_2\).
The parameter hypothesis guarantees that those charts cover the image.
The subsequent power projections may change their nilpotent structures,
but this lost-coordinate obstruction persists. In particular changing
R alone cannot repair this source. The underlying curve can change
with R; no assertion that all these generalized images have support C0
is intended.

## Arbitrary binary mixtures retain the same defect

Retain the parameter hypothesis and notation of the preceding generalization, and let
\(\Phi,\Psi\in k[U,V]\) be homogeneous of positive degrees u,v with
\(\sqrt{(\Phi,\Psi)}=(U,V)\). Assume \(uv\ne0\) in k. Set
\[
B=E/(\Phi(f,g),\Psi(f,g)),\qquad A=\operatorname{image}(S\to B).
\]
Then \(\operatorname{Proj}A\) is not ACM, with the same lower bounds
(1). In particular, **no homogeneous binary mixture with isolated
common zero at the origin repairs the characteristic-zero projected
source**. Taking \(\Phi=U^u,\Psi=V^v\) recovers the independent-power source.

The source is an actual complete intersection: substitution preserves
the radical \(\sqrt{(f,g)}\), so the two substituted equations have
height two in the CM hypersurface E. As in the power-image calculation, B has dimension two,
the finite image ideal is saturated, and the coefficient description
and local-cohomology comparison (2)–(3) hold. Generic birationality
of the full nonreduced source and image is not required.

Write the unique reductions in the free S-basis \(1,z\) as
\[
\Phi(f,g)=P+Qz,\qquad \Psi(f,g)=P'+Tz,\qquad K=(P,Q,P',T).
\]
Expand the polynomials before reducing powers of z. Their odd
coefficients have decompositions
\[
Q=\ell_1\alpha+\ell_2\beta,\qquad
T=\ell_1\gamma+\ell_2\delta,
\]
chosen so that, modulo \((\ell_1,\ell_2)\),
\[
(\alpha,\beta)=-(\Phi_U,\Phi_V)(\bar X,\bar Y),\qquad
(\gamma,\delta)=-(\Psi_U,\Psi_V)(\bar X,\bar Y).
\]
Indeed the terms linear in \(\ell_1,\ell_2\) are the displayed first
derivatives times \(-z\); every other odd term has coefficient in
\((\ell_1,\ell_2)^3\). Assigning those higher terms to either displayed
factor supplies the required polynomial decompositions in every
characteristic.

Define the homogeneous polynomial
\[
H=\alpha\delta-\beta\gamma,\qquad \deg H=2u+2v-4.
\]
The adjugate identities give
\[
\ell_1H=\delta Q-\beta T,\qquad
\ell_2H=\alpha T-\gamma Q.
\]
Thus \((\ell_1,\ell_2,P,P')H\subset K\). This annihilating ideal is
irrelevant-primary: modulo the two linear forms its remaining equations
are \(\Phi(\bar X,\bar Y),\Psi(\bar X,\bar Y)\), whose radical is
\(\sqrt{(\bar X,\bar Y)}=(t_1,t_2)\) in
\(\bar S=k[t_1,t_2]\). Hence H is irrelevant torsion modulo K.

For nonvanishing, let
\[
C_{\Phi,\Psi}=k[U,V]/(\Phi,\Psi),\qquad
J=\Phi_U\Psi_V-\Phi_V\Psi_U.
\]
This local Artinian CI has length uv. Its Jacobian J generates its
one-dimensional socle when uv is nonzero in k, by
[Eisenbud–Ulrich, Appendix Theorem A.5, printed p.224](https://www.math.purdue.edu/~bulrich/papers/published%20version%20of%20Duality%20for%20Residual%20Intersections.pdf).
This supplies the precise socle input for the direct projection deduction;
no literature-novelty claim is made.

The parameter quadrics \(\bar X,\bar Y\) make \(\bar S\) a finite
free module over \(k[U,V]\), with \(U\mapsto\bar X,V\mapsto\bar Y\).
For example, lift a homogeneous k-basis of
\(\bar S/(\bar X,\bar Y)\). Graded Nakayama gives generators; the
regular-sequence Hilbert series proves that there are no relations.
The basis degrees are \(0,1,1,2\). Tensoring the socle inclusion
\(kJ\hookrightarrow C_{\Phi,\Psi}\) with this free module therefore
gives an inclusion
\[
\bigl(\bar S/(\bar X,\bar Y)\bigr)(-2u-2v+4)
\ \hookrightarrow\
\bar S/(\Phi(\bar X,\bar Y),\Psi(\bar X,\bar Y)).
\]
Its image is generated by \(J(\bar X,\bar Y)=\bar H\). In particular
H is nonzero modulo K. Its cyclic reduction has shifted Hilbert
function \(1,2,1\); lifting these four independent classes and using
\(B/A=(S/K)(-1)\) proves (1). This is a lower bound, not an
identification of the full Rao module or of H's annihilator in S/K.

The geometric meaning remains explicit. The two charts
\(D_+(\ell_1),D_+(\ell_2)\) cover the image: their simultaneous
vanishing on B would also impose \(\bar X=\bar Y=0\), leaving no
projective point. On these charts \(Hz\) has retained-coordinate
representatives
\[
\frac{-\delta P+\beta P'}{\ell_1},\qquad
\frac{\gamma P-\alpha P'}{\ell_2}.
\]
They agree in B and hence on the image. They define a global section
of degree \(2u+2v-3\), but no ambient polynomial represents it
because H is nonzero modulo K. The Jacobian records the socle of
the finite binary complete-intersection algebra used to thicken the
source; the adjugate turns it into this ambient-section failure.
The theorem does not require interpreting that auxiliary binary
algebra as the entire generic transverse algebra of the curve.

For the original X=b², Y=c², \(\ell_1=a,\ell_2=d\), R=2bc-ad,
all these images retain exactly the support C0. The generalized
parameter version may change that support. Characteristic two is
included when uv is odd; nothing here treats characteristic dividing
uv. Mixing the binary relations or changing R within this construction
cannot repair the defect. Neither arbitrary supported thickenings nor
arbitrary defining pairs have been reduced to this construction.

## The missing sections need not survive a quotient with the same reduced curve

Let \(B_D\) be the homogeneous coordinate ring of the rational normal quartic upstairs, and let \(A_{C_0}\) be the four-coordinate ring of its projected reduced quartic. Then
\[
B_D/A_{C_0}=k(-1).
\tag{8}
\]
Indeed the only omitted degree-one monomial is \(z=s^2t^2\). Products of the retained quartics, whose t-exponents are \(0,1,3,4\), give every degree-eight monomial: their two-fold sumset is \(\{0,1,\ldots,8\}\). Inductively, if the n-fold sumset contains every integer from 0 to 4n, adding \(0,1,3,4\) gives every integer from 0 to \(4n+4\). Hence the retained coordinates generate all sections in degrees n≥2. They also contain the constants, proving (8).

Reduction of a power or binary-mixture source to D induces a map from its source/image quotient to (8). The exhibited section class \(Hz\) has degree \(2u+2v-3>1\) whenever \(u+v>2\), so it maps to zero. The degree-one case u=v=1 is explicitly excepted. Thus the actual high-degree obstruction can disappear in a quotient retaining the same reduced curve; its persistence cannot be assumed from support alone.

For an arbitrary hypothetical supported CI, its primary lift need not have this two-equation presentation or be ACM. Moreover its downstairs coordinate ring A is CM, so the exact sequence \(0\to A\to B\to B/A\to0\), with \(H^0_{\mathfrak m}(B)=0\), forces \(H^0_{\mathfrak m}(B/A)=0\). Requesting a nonzero class in that group states a contradiction target; it does not independently produce such a class. The family theorem supplies no all-pair persistence map, no upper conductor-boundary budget, and no positive residual-degree estimate.

## Torus-equivariant grading of the quadratic cover, missing sections, and conductor norm

*(Authored by Gemini on `evaluate_toric_integration_stci`; independently reviewed by Gemini subagent and verified in [`verify_toric_conductor_and_endpoint_defects.py`](../computations/verify_toric_conductor_and_endpoint_defects.py).)*

Under the curve's preserving \(\mathbf G_m\)-action \(T\) with centered weights \(\operatorname{wt}(a, b, c, d) = (-2, -1, 1, 2)\) (uncentered \((0, 1, 3, 4)\)), the branch quadric \(r = 2bc - ad\) has centered weight \(0\) (uncentered weight \(4\)). Assigning \(z\) **centered weight \(0\)** (uncentered weight \(2\), matching \(z = s^2 t^2\) on the rational normal quartic \(D \subset \mathbf P^4\)) makes \(E = S[z]/(z^2 - r)\), the finite double cover \(\pi: Q_3 = \operatorname{Proj} E \to \mathbf P^3\), and the involution \(\sigma(z) = -z\) **strictly \(T\)-equivariant** in every characteristic:

1. **\(T\)-weight structure of the power source and missing Rao classes:**
   In \(E = S[z]/(z^2 - r)\), the upstairs complete-intersection generators \(f = b^2 - az\) and \(g = c^2 - dz\) are \(T\)-eigenforms of centered weights \(-2\) and \(+2\), respectively. For \(f^u = P_u + Q_u z\) and \(g^v = R_v + T_v z\) (\(Q_u = a q_u, T_v = d t_v\)):
   - \(P_u, Q_u\) have centered weight \(-2u\), and \(q_u\) has centered weight \(-2(u - 1)\);
   - \(R_v, T_v\) have centered weight \(+2v\), and \(t_v\) has centered weight \(+2(v - 1)\);
   - The Jacobian-socle polynomial \(H_{uv} = q_u t_v\) (of degree \(2u + 2v - 4\)) and the missing ambient section \(H_{uv} z \in (B_{uv}/A_{uv})_{2u+2v-3}\) are **\(T\)-eigenforms of centered weight \(2(v - u)\)** (centered weight \(0\) in the symmetric case \(u = v\)).
   Because the basis \(1, b, c, bc\) of \(\bar S / (\bar X, \bar Y) = k[b, c]/(b^2, c^2)\) has degrees \((0, 1, 1, 2)\) and centered weights \((0, -1, +1, 0)\), the \(4\)-dimensional injected irrelevant-torsion / Rao submodule in \(H^1(\mathbf P^3, \mathcal I_{Y_{uv}}(*))\) decomposes into exact \(T\)-weight lines:
   - Degree \(e = 2u + 2v - 3\) (\(\dim \ge 1\), spanned by \(H_{uv} z\)): centered weight **\(2(v - u)\)**;
   - Degree \(e + 1 = 2u + 2v - 2\) (\(\dim \ge 2\), spanned by \(b H_{uv} z, c H_{uv} z\)): centered weights **\(2(v - u) - 1\) and \(2(v - u) + 1\)**;
   - Degree \(e + 2 = 2u + 2v - 1\) (\(\dim \ge 1\), spanned by \(bc H_{uv} z\)): centered weight **\(2(v - u)\)**.
   For the reduced curve (\(u = v = 1\)), \(B_D / A_{C_0} = k(-1)_{[0]}\) is spanned by \(z\) in degree \(1\) and centered weight \(0\).

2. **\(T\)-graded conductor boundary and ambient quadratic norm:**
   In the [separated quadratic-cover conductor setting](quadratic_covers_and_conductor_descent.md#81-ambient-quadratic-norms-force-conductor-postulation) (\(\operatorname{char} k \ne 2\)), for any \(T\)-invariant thickening \(J_0 \subset I_{C_0}\), the conductor ideal \(J_\Delta = \{h \in S : h z \in A\}\) and boundary quotient \(T_\Delta = S / J_\Delta\) are \(T\)-graded. Because \(\operatorname{wt}(z) = \operatorname{wt}(r) = 0\), any homogeneous weight vector \(h \in (J_\Delta)_d[w]\) lifts \(h z \in A_{d+1}[w]\) to \(P \in S_{d+1}[w]\) of the **same centered weight \(w\)**, and its ambient quadratic norm
   \[
     P^2 - r h^2 \in (J_0)_{2d+2}[2w]
   \]
   lies in degree \(2d + 2\) and even centered weight \(2w\). On the frontier degree rows \((6,6)\), \((5,8)\), \((8,8)\), and \((6,16)\) (with \(q = \lceil \alpha/2\rceil - 1\)), the postulation bound \(\delta \ge \alpha + \beta - 3 + 2\bigl[\binom{q+2}{3} - q\bigr]\) gives \(\delta \ge 13, 14, 27, 23\), respectively.

## Independent reconstruction and scope

The result describes the section ring of these actual projections, not only a
failed STCI attempt. A different downstairs ACM construction must eliminate or
avoid the exhibited ambient-section defect through different source or
multiplication data. The quotient example above explains why a general
persistence theorem would require a new comparison. The parameter-sequence
formulation makes the mechanism available for other finite projections while
keeping its degree-product and presentation hypotheses explicit.

Independent review reconstructed the irrelevant-torsion witness, the actual missing section, the parameter-sequence generalization and the binary Jacobian-socle argument, checking its precise nonzero-degree-product hypothesis against the primary socle theorem. The lower bounds describe three Rao degrees, not the full module. Reduction to the rational normal quartic kills the exhibited higher-degree classes, so no support-only persistence argument transfers this source obstruction to arbitrary primary lifts. The characteristic-divisible cases, including the stated Frobenius sources, remain outside the theorem.
