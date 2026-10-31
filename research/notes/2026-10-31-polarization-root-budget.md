# Polarization roots, cone defects, and residual-budget limits

Date: 2026-10-31. Status: **independently reviewed provisional deductions**;
see the [separate audit](2026-10-31-polarization-root-budget-audit.md).
The actual preserved statement and strategy recommendation were reviewed
after correction of the affinization description. No canonical promotion.

## 1. Question and the unique root on an arbitrary supported CI

Work over an algebraically closed field of characteristic zero. Suppose

\[
Z=V(F_a,G_b)\subset\mathbf P^3,\quad Z_{\rm red}=C_0,
\quad C_0=[s^4:s^3t:st^3:t^4],\quad H=O_Z(1),\quad c=a+b-4.
\]

The inherited [low-degree exclusion](../results/quartic_carrier_exclusion.md)
and factor reduction give a,b≥5. The question here is whether the
[polarization-lifting principle](2026-10-31-finite-pullback-lifting.md)
adds a constraint on **arbitrary** supported pairs, or a means of
constructing them. In the broader residual program a proper intersection
has cycle \(ab=4m+\deg R\); a new defect must be related to actual
attachment or residual data before it can be used as a cost in that budget.

Write J for the nilradical of Z. Logarithm and the unit sequence give

\[
0\longrightarrow H^1(Z,J)\longrightarrow\operatorname{Pic}(Z)
\longrightarrow\operatorname{Pic}(C_0)=\mathbf Z\longrightarrow0.
\tag{1}
\]

Constants lift, so the left map is injective; \(H^2(Z,J)=0\) gives
surjectivity on the right. The kernel is an additive characteristic-zero
vector space. Lift \(O_{\mathbf P^1}(1)\) to a line bundle L0 and divide
the class \(H L_0^{-4}\) by four in this kernel. This gives a unique
isomorphism class L with

\[
L|_{C_0}=O_{\mathbf P^1}(1),\qquad L^4\simeq H.
\tag{2}
\]

The fourth-power identification remains a choice. L is ample. Neither
effectivity nor a two-section pencil follows from (1)–(2).

## 2. The full root algebra is Gorenstein

Choose the identification in (2), and put

\[
A=\bigoplus_{n\in\mathbf Z}H^0(Z,L^n),\qquad
B=\bigoplus_{q\ge0}H^0(Z,H^q)=k[x_0,x_1,x_2,x_3]/(F,G).
\]

The equality for B follows from the CI resolution. It also shows
\(H^0(Z,H^q)=0\) for q<0. Inside A, give \(B_q\) degree 4q, so
\(A^{(4)}=B\) after the usual regrading. Possible negative-degree
nilpotent sections in other congruence classes are retained.

For i=0,1,2,3 define the full section module

\[
M_i=\bigoplus_{q\in\mathbf Z}H^0(Z,L^iH^q).
\]

It is finite over B: the positive tail is finite by the section-module
construction, and the negative tail vanishes by Serre duality and Serre
vanishing. Full section modules have zeroth and first local cohomology
at the cone vertex equal to zero. Since B has dimension two, every M_i
is maximal Cohen–Macaulay. Away from the vertex it comes from a line
bundle on Z. Thus A is a finite Cohen–Macaulay B-algebra. This uses the
sheaf/section-module construction on the nonreduced scheme, not normality;
see [Stacks, §28.29](https://stacks.math.columbia.edu/tag/01QG).

On the punctured cone, the induced finite map is

\[
L^{-1,\times}\longrightarrow H^{-1,\times},\qquad z\longmapsto z^4,
\]

a \(\mu_4\)-torsor, finite étale over the nonreduced base. The grading
action gives the global homogeneous functional
\(t=4\operatorname{pr}_{A^{\mu_4}}:A\to B\). Its pairing

\[
A\longrightarrow\operatorname{Hom}_B(A,B),\qquad
u\longmapsto[v\mapsto t(uv)]
\tag{3}
\]

is the perfect étale trace pairing off the vertex. Both sides of (3)
are maximal Cohen–Macaulay B-modules; for the right side use that B is
Gorenstein. Sections of each extend across the vertex by depth two.
Consequently (3) is an isomorphism globally. This argument uses the
actual pairing and local cohomology, avoiding a normal-domain reflexive
extension theorem.

In the A-grading \(\omega_B=B(4c)\). Finite duality now gives

\[
\boxed{\omega_A=\operatorname{Hom}_B(A,\omega_B)\simeq A(4c).}
\tag{4}
\]

Thus the full root algebra is Gorenstein. No assertion that A is a
complete intersection, or that its reduction is Cohen–Macaulay or normal,
follows from this calculation.

## 3. The reduced cover retains a vertex defect and restricted linear series

Restriction to C0 has nilpotent kernel and embeds
\(A_{\rm red}\) into k[s,t]. Serre vanishing makes restriction onto
\(H^0(C_0,O(n))\) surjective for n sufficiently large. Therefore

\[
\overline{A_{\rm red}}=k[s,t],\qquad
D=k[s,t]/A_{\rm red}
\]

has finite length. Degreewise restriction, or exactness of the
\(\mu_4\)-invariants, gives

\[
(A_{\rm red})^{(4)}=B_{\rm red}=k[s^4,s^3t,st^3,t^4].
\]

It follows that

\[
D_4=k\,[s^2t^2],\qquad D_{4q}=0\quad(q\ne1).
\tag{5}
\]

For q≥2, sums of q exponents from {0,1,3,4} fill {0,...,4q}; this
also verifies the positive-degree assertion directly. The affine reduced
root model \(\operatorname{Spec}A_{\rm red}\) retains D at the vertex,
although its puncture is the smooth punctured plane. Affinizing that
puncture, or normalizing this affine model, replaces it by the plane and
deletes the information under investigation. Thus taking global sections
of the nonreduced punctured cover and then reducing need not agree with
taking global sections after reduction.

More explicitly, the restriction sequence on Z identifies

\[
D_n\simeq\operatorname{im}\bigl[
H^0(C_0,O(n))\longrightarrow H^1(Z,J\otimes L^n)\bigr].
\tag{5a}
\]

The vertex defect measures failure of sections to extend through the
nilpotent structure. Formula (5a) does not make it an attachment length
or an additional term in the projective residual cycle.

There are useful uniform constraints on reduced root sections. Let
\(V_i=\operatorname{im}(H^0(Z,L^i)\to H^0(\mathbf P^1,O(i)))\).
Then

\[
V_1\in\{0,ks,kt\},\qquad \dim V_2\le1.
\tag{6}
\]

Indeed \((\alpha s+\beta t)^4\in V_4\) has zero middle coefficient,
so \(6\alpha^2\beta^2=0\); a vector space in the union of the two
coordinate lines lies in one of them. Also multiplication sends
\(V_2V_2\) into V4. The middle-coefficient pairing on binary quadratics
is

\[
\langle(a,b,c),(a',b',c')\rangle=ac'+bb'+ca'.
\]

It is nondegenerate in dimension three, so a totally isotropic subspace
has dimension at most one. Geometrically, the squares permitted by the
missing coordinate form a smooth conic in the projective plane of binary
quadratics, which contains no projective line. A nonzero reduced section
of L has its zero at one of the two marked endpoints. These statements
constrain the **images** of sections; they neither bound all nilpotent
sections nor force either image to be nonzero.

The checked cyclic-cover theory does not remove D. In particular
[Tomari–Watanabe, §3](https://www.jstage.jst.go.jp/article/kodaimath1978/24/3/24_3_436/_pdf/-char/en)
assumes normal graded domains in its cyclic/Veronese structure results.
Those hypotheses are unavailable for this nonreduced root algebra.

## 4. An existing characteristic-zero CI tests the proposed inference

Use the inherited twisted-cubic pair from the
[torsion benchmark audit](2026-10-27-char0-torsion-benchmark-audit.md):

\[
Z_T=V(y_0y_2-y_1^2,\ y_2^3-2y_1y_2y_3+y_0y_3^2).
\]

It is a primitive double of the twisted cubic on both endpoint charts,
with nilradical \(O_{\mathbf P^1}(-5)\) and
\(\omega_{Z_T}=O_{Z_T}(1)\). Thus it is a canonical genus-four ribbon.
This is the line-bundle/canonical-ribbon geometry studied by
[Bayer–Eisenbud, §§4–5](https://www.math.columbia.edu/~bayer/papers/Ribbons_BE95.pdf).

Its unique cubic polarization root M can be checked explicitly. On
y0=1 use \(u=y_1,\epsilon=y_3-u^3\), with \(\epsilon^2=0\).
On y3=1 use \(v=y_2,\eta=y_1-v^2\), with \(\eta^2=0\). The overlap
and a compatible M-transition are

\[
v=u^{-1}-u^{-4}\epsilon,\quad\eta=u^{-5}\epsilon,\quad
m_\infty=(u+\tfrac13u^{-2}\epsilon)m_0.
\]

For a reduced section \(\sum_{j=0}^n a_jv^j\) of M^n, the required
nilpotent correction on the u-chart is

\[
\epsilon\sum_{j=0}^n a_j(\tfrac n3-j)u^{n-j-3}.
\tag{7}
\]

Corrections from that chart have nonnegative exponents; those from the
v-chart have exponents at most n−5. Formula (7) gives
\(h^0(M)=0\), \(h^0(M^2)=1\), and full restriction onto O(n) for
every n≥3. For n=3 the one potentially obstructed coefficient has
multiplier zero. For n≥4 the exponent ranges cover every term. There
are no negative-degree sections, since both the reduced and nilpotent
layers have negative degree there.

The corresponding root algebra therefore has normalization defect of
dimension two in each of degrees one and two, and zero elsewhere.
Its third-Veronese defect is zero. The argument of §2 with three in
place of four makes this actual root algebra Cohen–Macaulay and Gorenstein.
It nevertheless has nonnormal reduction and an ample root with no
sections. This uses a known STCI, with R=0; no new example family was
searched. It does **not** realize the quartic's nonzero invariant defect
in (5).

## 5. What this adds to the residual and existence programs

The package applies to arbitrary hypothetical supported CI pairs, not
only the entirely thick branch. It organizes their full polarization
root, equivariant nilpotent algebra and missing coordinate. The earlier
[linear-series result](2026-10-30-four-streams-linear-series.md) already
proves failure of that coordinate to lift on the first neighborhood and
in the stated entirely thick limits. Neither result forces the coordinate
to lift on a global CI. The present package adds (4)–(6), but no
incompatibility between them.

For a general proper intersection \(Y=V(F,G)\) with cycle
\([Y]=m[C_0]+R\), its C0-primary part W still admits the abstract
Picard/root argument. Its full hyperplane section ring need not equal
its embedded coordinate ring, and its dualizing sheaf need not be H^c.
One cannot transfer the identification B=S/(F,G) or the Gorenstein
conclusion (4) to that primary part without additional evidence.

In particular D is a defect at the **cone vertex**, not a residual curve
or an established attachment cost. No comparison with \(\deg R\) has
been obtained. The known control shows that some such defects coexist
with R=0, while retaining the distinction between its zero invariant
defect and (5). This respects the purpose of the
[residual-degree](2026-10-28-residual-degree-synthesis.md) and
[absorption](2026-10-27-arbitrary-degree-absorption-synthesis.md) programs:
constraints become a residual bound only after the allowed concentration
on C and the actual attachment terms are controlled.

**Disposition:** stop the bare root-algebra approach here. A new exclusion
would need an additional theorem controlling the invariant defect and
its nilpotent extension using the two global equations. A construction
would need an actual extension whose fourth Veronese has the four required
generators and two regular-sequence relations. These are missing inputs,
not supplied methods or assigned campaigns. No root-cover classification,
semigroup list or new example sequence follows. C0 may be an STCI.

The structural selection used a fresh `gpt-6-astra/xhigh` worker and
bounded repository retrieval used `gpt-6-luna/high`. A fresh
`gpt-6.1-sol/high` reviewer reconstructed the module/duality argument and
the existing-ribbon calculation, replacing an imprecise extension shortcut
by the explicit trace pairing (3). The review recommendation and stopping
condition were reported before verification. No numerical computation
or canonical promotion was performed.
