# Supported ACM constructions: uniform projection defect and residual-source failure

Date: 2026-10-31. Status: **independently reviewed provisional deductions**;
see the [scoped audit](2026-10-31-acm-construction-selection-audit.md).
No canonical promotion or literature-novelty claim.

The target remains the unrestricted characteristic-zero STCI problem for
\(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\). An actual homogeneous ACM
thickening would be a substantive intermediate construction; an AG
thickening in this codimension would be a CI. The historical weaker
question for this exact quartic is recorded by
[Singh–Walther, Example 3.5 and Question 3.6](https://www.math.utah.edu/~singh/publications/singh_walther_pure.pdf).
That attribution is not a claim that every subsequent publication has
been checked.

The first test below completes a question explicitly left unresolved by
the earlier [projected-power source](2026-10-31-ambient-transport-and-projection.md).
Its non-Gorenstein theorem did not decide ACM. A fresh strategy reviewer
approved this distinct uniform test; the recommendation and stopping rule
were reported before the investigation. No exponent grid was used.

## 1. Every projected power image fails ACM

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

## 2. The defect is an actual missing ambient section

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

## 3. A geometric generalization of the power-source obstruction

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

### 3a. Arbitrary binary mixtures retain the same defect

This is a uniform extension of §3, not a new construction campaign.
Its additional independent review is recorded in the companion audit.
Retain the parameter hypothesis and notation of §3, and let
\(\Phi,\Psi\in k[U,V]\) be homogeneous of positive degrees u,v with
\(\sqrt{(\Phi,\Psi)}=(U,V)\). Assume \(uv\ne0\) in k. Set
\[
B=E/(\Phi(f,g),\Psi(f,g)),\qquad A=\operatorname{image}(S\to B).
\]
Then \(\operatorname{Proj}A\) is not ACM, with the same lower bounds
(1). In particular, **no homogeneous binary mixture with isolated
common zero at the origin repairs the characteristic-zero projected
source**. Taking \(\Phi=U^u,\Psi=V^v\) recovers §§1–3.

The source is an actual complete intersection: substitution preserves
the radical \(\sqrt{(f,g)}\), so the two substituted equations have
height two in the CM hypersurface E. As in §1, B has dimension two,
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
This is the sole new literature input; the projection deduction is
ours, with no literature-novelty claim.

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

## 4. The classical residual link does not supply an ACM thickening

This separate literature test concerns
[Hassanzadeh, Theorems 3.7, 3.16, Corollary 3.19 and Theorem 4.2](https://arxiv.org/html/2409.05705v2).
Return to characteristic zero and write
\[
q=ad-bc,\quad A_3=b^3-a^2c,\quad B_3=b^2d-ac^2,\quad C_3=bd^2-c^3,
\quad P=I_{C_0}=(q,A_3,B_3,C_3).
\]
Let \(I_D=(ac,ad,bc,bd)=(a,b)\cap(c,d)\) and
\(\mathfrak a=(q,B_3)\). These are two skew ruling lines on Q and
their actual link to C0:
\[
\mathfrak a:I_D=P,\qquad
(q,B_3)=(ac,ad,bc,bd)
\begin{pmatrix}0&-c\\1&0\\-1&0\\0&b\end{pmatrix}.                    \tag{7}
\]
In Segre coordinates \(a=xu,b=xv,c=yu,d=yv\), the cubic restricts to
\(xy(xv^3-yu^3)\): its divisor is the two lines plus C0 of class (1,3).
This proves the residual support and multiplicities in (7).

The actual outputs of the proposed operations are:

| Operation | Output | Failure |
| --- | --- | --- |
| Boundary determinant ideal | \(\mathfrak a+I_4(\Phi)=\mathfrak a\) | Retains both residual lines |
| Zeroth Fitting ideal of \(I_D/\mathfrak a\) | \(P\cap\mathfrak m^3\) | Adds only an embedded cone-vertex defect |
| Full Koszul–Fitting ideal | \(P\) | Returns the original non-ACM quartic |

The first row is Hassanzadeh's Theorem 4.2; the 4-by-2 matrix has no
4-by-4 minors. The last row follows from
[Bouça–Hassanzadeh, Proposition 5.9](https://arxiv.org/pdf/1810.05134)
with s=g=2. That equality does not assert that the quotient is CM.

For the middle row an exact presentation after eliminating bc is
\[
M=\begin{pmatrix}
d&b&0&0&-c\\
-c&-a&b&d&0\\
0&0&-a&-c&b
\end{pmatrix}.
\]
Its maximal minors, in column orders
123,124,125,134,135,145,234,235,245,345, are respectively
\[
aq,\ cq,\ -bq,\ dq,\ B_3,\ C_3,\ bq,\ A_3,\ B_3,\ -cq.
\]
They generate \((aq,bq,cq,dq,A_3,B_3,C_3)=P\cap\mathfrak m^3\).
The nonzero class of q is killed by \(\mathfrak m\), so this quotient
has depth zero; saturation recovers P. Its projective scheme is still
the reduced quartic, not a newly constructed thickening.

The theorem hypotheses fail for a visible reason. In the Koszul complex
on \((ac,ad,bc,bd)\), the cycle
\(\eta=bd\,e_1-bc\,e_2\) is a nonzero class in H1. In multidegree abcd,
the only boundary directions are \(\partial e_{14}\) and
\(\partial e_{23}\); their unavoidable e4 and e3 terms prevent a
boundary representation. With \(k_{ij}=\partial(e_i\wedge e_j)\),
\[
a\eta=-b k_{12},\quad
b\eta=-b k_{14}+b k_{23}+a k_{34},\quad
c\eta=-d k_{13}+c k_{23},\quad
d\eta=-d k_{14}+c k_{24}.
\]
Hence H1 has depth zero instead of the required sliding depth at least
one. At \(\mathfrak m\), \(Z_1\) has depth at least two; the sequence
\(0\to B_1\to Z_1\to H_1\to0\) forces depth \(B_1=1\).
Then \(0\to Z_2\to K_2\to B_1\to0\) gives depth \(Z_2=2\) and
projective dimension \(Z_2=2\), exceeding Theorem 3.16's bound one.
Thus the broader cycle hypothesis also fails. Theorem 3.7's s≥r
hypothesis already fails because 2<4.

Varying a proper linking pair while keeping this fixed skew-line source
does not change its failed depth conditions; ordinary direct CI linkage
also preserves ACM status. This is a source limitation, not an exclusion
of all residual constructions.

## 5. What closes and what a new construction must change

The projected powers are now excluded even as ACM constructions, uniformly.
Their new obstruction is an explicit section in the actual embedding,
not just a local canonical-module condition. The generalized parameter
sequence shows that varying the covering quadric alone cannot repair it.
Section 3a closes arbitrary homogeneous binary mixtures as well: their
Jacobian socle replaces the product used for powers and retains the
same ambient-section defect.
The classical residual presentation likewise supplies no ACM thickening:
its three exact outputs respectively retain extra curves, add vertex
torsion, or recover the original deficiency.

Neither conclusion proves that C0 cannot be STCI or support another ACM
thickening. A different thickening containing these images is not excluded.
No operation converting a hypothetical non-Gorenstein ACM thickening
into a supported CI has been supplied by this investigation.

Stop these sources without exponent, neighboring-quadric, or residual-line
classification. Reopening requires a genuinely different embedded operation
that controls both support and the ambient section deficiency, or an
all-pair comparison proving that such a deficiency must survive. An abstract
canonical extension or a specified desired split middle bundle still lacks
that operation. The unrestricted characteristic-zero question remains open.
