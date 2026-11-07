# Two blowups, actual residual cycles, and supporting nef bounds

Fix C=C0 over an algebraically closed characteristic-zero field. The seven cubics give the established graph B=Bl_C(P3)=Bl_Gamma(V5), where Gamma is a smooth conic. This underlying birational model is verified in [Cheltsov–Przyjalkowski–Shramov, Lemma 6.13](https://arxiv.org/html/1809.09223v1#S6.L13). The explicit cubic-image construction and its exact certificate are retained in the conditional sextic geometric account; the model itself does not require a (6,16) pair. The deductions below have independent review.

## The two blowups and their actual global section dictionary

Write

\[
H=\pi^*\mathcal O_{\mathbf P^3}(1),\quad E=\pi^{-1}(C),
\quad L=3H-E,\quad Q'=2H-E.
\]

The other projection is
\(\phi:B=\operatorname{Bl}_\Gamma V\to V\), with
\(L=\phi^*M\), \(M=\mathcal O_V(1)\), and exceptional divisor \(Q'\).
Its fibers on \(Q'\cong\mathbf P^1\times\mathbf P^1\) are the trisecant
ruling lines of the original quadric \(Q=V(q)\). The useful change of basis is

\[
\boxed{H=L-Q',\qquad E=2L-3Q'.}\tag{1}
\]

## 2. Actual equation spaces become sections with prescribed conic vanishing

Here and below \(I_C^r\) and \(I_\Gamma^e\) are **ideal sheaf powers**.
Their global sections are not being identified silently with an unsaturated
homogeneous ideal power.

**Section dictionary.** For integers \(r\ge0\) and \(a\ge3r\), there is a
natural vector-space identification

\[
\boxed{
H^0(\mathbf P^3,I_C^r(a))
\cong H^0\bigl(V,I_\Gamma^{\,a-3r}(a-2r)\bigr).
}\tag{2}
\]

Indeed the left side is \(H^0(B,aH-rE)\). By (1),

\[
aH-rE=(a-2r)L-(a-3r)Q'.
\]

For the blowup of a smooth codimension-two center,
\(\phi_*\mathcal O_B(-eQ')=I_\Gamma^e\) for \(e\ge0\).
This follows directly on a regular-parameter chart from the Rees algebra;
the same fact for \(\pi\) gave the first equality. The projection formula
proves (2). See also the primary [Stacks blowup construction](https://stacks.math.columbia.edu/tag/01OF).

This correspondence retains actual global constant coefficients. It is not
merely a correspondence between symbols over \(k(C)\).

For completeness the other region has a simple interpretation. If
\(2r\le a\le3r\), put \(k=a-2r\), \(j=3r-a\). Then

\[
H^0(\mathbf P^3,I_C^r(a))\cong H^0(V,\mathcal O_V(k)),
\quad aH-rE=kL+jQ'.\tag{3}
\]

Here \(\phi_*\mathcal O_B(jQ')=\mathcal O_V\): a rational function allowed
to have poles only above a codimension-two subset extends on normal \(V\).
Every section has the fixed factor \(q^j\) downstairs. If \(a<2r\), the
space is zero, since the same calculation leaves a negative multiple of
the ample class \(M\). For example, the familiar spaces of order-two forms
in degrees four, five and six become respectively constants times \(q^2\),
\(q\) times the seven cubics, and all quadric sections of \(V\). These are
checks of the dictionary, not new claims about those previously computed
spaces.

There is an explicit polynomial construction behind (2). Let

\[
(c_0,\ldots,c_6)=(qx_0,qx_1,qx_2,qx_3,
x_0^2x_2-x_1^3,x_0x_2^2-x_1^2x_3,x_2^3-x_1x_3^2).
\]

Take a section \(P\in H^0(V,I_\Gamma^e(k))\). Projective normality of the
inherited cubic model represents it by a degree-\(k\) polynomial in the
\(y_i\). Then

\[
F(x)=\frac{P(c_0(x),\ldots,c_6(x))}{q(x)^e}\tag{4}
\]

is a polynomial of degree \(a=3k-2e\), vanishing to order at least
\(r=k-e\) on \(C\), when \(k\ge e\ge0\). Divisibility by \(q^e\) can be
checked at the generic point of \(Q\), where \(\phi\)'s transverse order to
\(\Gamma\) is the \(q\)-order; polynomial unique factorization then gives
global divisibility. Formula (2) supplies the coordinate-free justification.
No claim about a chosen nonsaturated ideal presentation of
\(I_\Gamma^e(k)\) is required.

If \(P\) has exact generic order \(e\) on \(\Gamma\), then \(F\) has no
quadric factor. If its divisor does not contain the surface \(\Sigma\) of
§3, then \(F\) has exact order \(r\) on \(C\). Conversely, a form of exact
order \(r\) with no quadric factor gives exactly these conditions. Thus this
is an equation-construction dictionary with explicit order checks.

## 3. The original exceptional divisor has a fixed anticanonical image

The image of \(E\), which was not identified in the retrieved source notes,
is particularly useful. Set

\[
\Sigma=V\cap V(y_0y_3-y_1y_2)\subset\mathbf P^6.
\]

**Proposition.** \(\Sigma\) is an integral nonnormal
anticanonical surface on \(V\). Its normalization is the finite birational
map

\[
\nu=\phi|_E:E\cong\mathbf P^1\times\mathbf P^1\longrightarrow\Sigma.
\]

Put \(B_0=E\cap Q'\), to distinguish this curve from the threefold \(B\).
Then

\[
\boxed{\phi^*\Sigma=E+3Q',\quad B_0\sim(1,1)\text{ on }E,
\quad I_{\mathrm{cond},E}=\mathcal O_E(-2B_0).}\tag{5}
\]

The map \(B_0\to\Gamma\) has degree three and, in the displayed coordinates,
is \([s:t]\mapsto[s^3:t^3]\) followed by the conic embedding. In particular
its two totally ramified values retain the marked endpoint geometry of \(C\).

**Proof.** Substitution of the seven cubics gives the literal identity

\[
c_0c_3-c_1c_2=q^3.
\]

The divisor of this section of \(2L=6H-2E\) on the blowup is
\(3Q'+E\). The nonexceptional component is \(E\), with coefficient one;
hence its image is precisely the integral reduced quadratic section
\(\Sigma\), and the equality in (5) is scheme-theoretic at the divisor
level. Since \(K_V=-2M\), adjunction gives \(\omega_\Sigma=\mathcal O_\Sigma\).
The morphism \(\phi\) is an isomorphism off \(Q'\), so \(\Sigma\) is smooth
off \(\Gamma\).

No contracted ruling of \(Q'\) lies in \(E\): its intersection with \(E\)
is its length-three intersection with \(C\) on \(Q\). Thus \(\phi|_E\) has
finite fibers and is finite, as it is proper. It is birational, since it is
an isomorphism outside \(B_0\). Smooth \(E\) is therefore the normalization.

Use the product coordinates on \(E\) given by R-0020 and the lines convention
for \(\mathbf P(N_C)\). Then

\[
H|_E=\mathcal O(4,0),\quad E|_E=\mathcal O(7,-1),
\quad L|_E=\mathcal O(5,1),\quad Q'|_E=\mathcal O(1,1).
\]

The curve \(B_0\) is the section of the normal projective bundle supplied by
the smooth quadric, so is smooth and isomorphic to \(C\). On \(Q'\), take
coordinates with
\(x_0=ua,x_1=ub,x_2=va,x_3=vb\). Then \(C\) has equation
\(va^3-ub^3=0\), and the last three cubic coordinates restrict, after
removing this equation, to \([u^2:uv:v^2]\). This proves the degree-three
map and its endpoint assertion.

Finally finite duality for the normalization of a Gorenstein surface gives

\[
\nu_*\omega_E=
\mathcal Hom_\Sigma(\nu_*\mathcal O_E,\omega_\Sigma),
\]

which, with \(\omega_\Sigma=\mathcal O_\Sigma\), identifies the conductor
ideal on \(E\) with \(\omega_E\cong\mathcal O_E(-2,-2)\). Its support is
contained in the single smooth irreducible curve \(B_0\); an invertible
ideal with this support is \(\mathcal O_E(-dB_0)\). Comparison of classes
forces \(d=2\), proving the full ideal assertion in (5), including the
absence of an additional punctual correction. The finite-duality formula
is the same standard input already independently reconstructed in the
[October 21 review, §2](normalization_conductor_phase2_addendum.md);
see also [Stacks, finite morphisms](https://stacks.math.columbia.edu/tag/0FKW).

At a general point of \(\Gamma\), the three preimages in \(B_0\) are
distinct. The transverse curve singularity of \(\Sigma\) is therefore an
ordinary triple point; \(2B_0\) is the expected conductor on its three
branches. No assertion of this transverse type is made at the ramified
endpoint values.

This produces an actual, explicitly marked nonnormal anticanonical surface
associated to the quartic. It is not a containing surface in the original
\(\mathbf P^3\), and no fixed-carrier STCI result is transported to it.

## 4. Residual curves and the two different ways a curve can disappear

Let \(F_a,G_b\) be an actual proper pair with exact generic normal orders
\(r,s\) along \(C\), and write

\[
[V(F,G)]=m[C]+R.
\]

On \(B\) their strict transforms have classes
\(A=aH-rE\), \(A'=bH-sE\) and have no common surface component. Their
scheme intersection \(W\) is a proper complete-intersection curve. There is
an identity of actual cycles, stronger than an equality of Chow classes:

\[
\boxed{\pi_*[W]=(m-rs)[C]+R.}\tag{6}
\]

Off \(C\), the actual residual cycles agree because \(\pi\) is an
isomorphism. At \(\eta_C\), work in the two-dimensional regular local ring
\(\mathcal O_{\mathbf P^3,\eta_C}\). Its blowup at the maximal ideal has
exceptional \(\mathbf P^1_{k(C)}\). The local blowup intersection formula is

\[
i_{\eta_C}(F,G)
=rs+\sum_{z\in\mathbf P^1_{k(C)}}
[\kappa(z):k(C)]\,i_z(F',G').
\]

This formula follows by separating the exceptional orders \(r,s\) in the
intersection of two plane germs; the exceptional contribution is their
product and the remaining local intersections are those of their strict
transforms. The weighted sum is exactly the coefficient of \(C\) in
\(\pi_*[W]\), proving (6) coefficient by coefficient. The projection formula
and \(\pi_*(E^2)=-[C]\) give a separate check of its Chow class; that check
alone would not prove the actual-cycle assertion.

The components of \(W\) outside \(E\) are precisely the strict transforms
of actual residual components. Components contained in \(E\) can dominate
\(C\) or map to isolated points. Consequently

\[
\boxed{R=0\quad\Longleftrightarrow\quad\operatorname{Supp}W\subset E.}\tag{7}
\]

For (7), use that \(\pi\) is an isomorphism off \(E\) and \(W\) is pure
one-dimensional. This criterion concerns the actual strict-transform
intersection, not the common zeros of two leading symbols alone.

The second projection gives complementary visibility:

| Curve on the graph \(B\) | Image in \(\mathbf P^3\) | Image in \(V\) |
|---|---|---|
| A fiber of \(E\to C\) | A point | A line in \(\Sigma\) |
| A ruling fiber of \(Q'\to\Gamma\) | An actual trisecant line | A point of \(\Gamma\) |
| A curve in \(E\) dominating \(C\) | Thickness along \(C\) | A curve in \(\Sigma\) |
| A curve outside \(E\cup Q'\) | Residual curve | Its birational transform |

Thus even an actual curve in \(\Sigma\) need not be a residual curve in the
original space; conversely an actual residual trisecant can vanish to a point
on \(V\). The weaker condition \(\phi(W)\subset\Sigma\) does **not** replace
(7), since \(\phi^{-1}(\Sigma)=E\cup Q'\). Retain the graph and both
projections whenever residual support matters.

The numerical record of the two polarizations, useful without any generic
coprime-symbol assumption, is

\[
\begin{aligned}
H\cdot W&=ab-4rs,\\
E\cdot W&=4(as+br)-14rs,\\
L\cdot W&=3ab-4(as+br)+2rs,\\
Q'\cdot W&=2ab-4(as+br)+6rs.
\end{aligned}\tag{8}
\]

These follow from \(H^3=1,H^2E=0,HE^2=-4,E^3=-14\).
An intersection number with \(E\) or \(Q'\) is not a point count if \(W\)
has a component in that divisor. Nor does its sign by itself assert a
residual component downstairs.

## 5. General residuals acquire a second constructive description

For a general \((a,b)\) pair, \(a,b\ge4\), use the inherited multiplicity-one
theorem of §1. Then \(W\cong D\) and \(r=s=1\). The corresponding divisors
\(T_a,T_b\) on \(V\) have

\[
T_a\in |(a-2)M|,\quad\operatorname{ord}_\Gamma T_a=a-3,
\qquad
T_b\in |(b-2)M|,\quad\operatorname{ord}_\Gamma T_b=b-3.
\]

Their intersection has a conic-primary component of generic multiplicity
\((a-3)(b-3)\), and residual image \(D'=\phi(W)\) of degree

\[
\boxed{\deg_M D'=3ab-4a-4b+2.}\tag{9}
\]

The multiplicity is the product because the general normal forms along
\(\Gamma\) have no common projective root at its generic point. Equivalently,
subtract (9) from the total \(M\)-degree \(5(a-2)(b-2)\) and divide by the
conic degree two. The general transformed residual is smooth, and isomorphic
to \(D\), for the following reason. On \(Q'\cong Q\), restrictions of the
two strict equations are general sections of
\(\mathcal O_Q(a-1,a-3)\) and \(\mathcal O_Q(b-1,b-3)\); restriction is
surjective by the quadric sequence. Their common zeros are transverse and
finite. No two lie in the same contracted ruling for a general pair: at two
chosen distinct points of one ruling each equation imposes two independent
linear conditions, while the ruling and its two points vary in dimension
three. The four conditions exceed this dimension. At a transverse meeting
with \(Q'\), the blowdown restricted to \(W\) is an immersion in the standard
two-parameter blowup chart. These two facts exclude both identifications and
ramification. Hence \(\phi|_W\) is a closed immersion.

The reduced conic attachment divisor has length

\[
\operatorname{length}(D'\cap\Gamma)
=Q'\cdot W=2ab-4a-4b+6.\tag{10}
\]

This is attachment to **reduced** \(\Gamma\); it is not the attachment length
to the full conic-primary component when \((a-3)(b-3)>1\).

| Original bidegree | \(\deg D\) in \(\mathbf P^3\) | \(\deg_M D'\) on \(V\) | Generic conic multiplicity | Reduced conic attachments |
|---|---:|---:|---:|---:|
| \((4,4)\) | 12 | 18 | 1 | 6 |
| \((5,5)\) | 21 | 37 | 4 | 16 |
| \((5,6)\) | 26 | 48 | 6 | 22 |
| \((6,6)\) | 32 | 62 | 9 | 30 |

These are examples of one formula, not a proposed degree-by-degree agenda.
They show that the same smooth residual curve can be interpreted either as
linked to the quartic in \(\mathbf P^3\), or as linked to a multiple conic on
the quintic del Pezzo threefold. The full primary schemes and attachment
budgets in these two presentations differ.





## Supporting nef bounds, exact slack, and equality controls

Write delta=deg R=ab-4m and K=16(as+br)-7ab-28rs. For arbitrary actual proper pairs the balance below gives 5delta>=K, and delta>=K if no residual component lies on Q. No normality, integral-carrier or saturated-root assumption is imposed.

## 2. Exact slack identities and what makes the bounds strict

On \(B=\operatorname{Bl}_C\mathbf P^3\), put
\(H=\pi^*\mathcal O(1)\), exceptional \(E\), \(L=3H-E\), and
\(Q'=2H-E=L-H\). The second projection
\(\phi:B\to V_5\) contracts precisely the ruling fibers of \(Q'\).

Let \(W\) be the proper intersection of the two strict surfaces. Decompose
its actual effective cycle as

\[
[W]=Z_E+\widetilde R,
\qquad Z_E\subset E,
\]

where \(\widetilde R\) is the strict-transform cycle of the actual
residual. In the product description
\(E=\mathbf P^1_{\rm base}\times\mathbf P^1_{\rm direction}\), write

\[
[Z_E]_E=u\alpha+n\beta,\qquad u,n\ge0,
\quad n=m-rs.
\]

Here \(u\) includes vertical fibers and the direction-degree contributions
of horizontal components. The restrictions
\(H|_E=4\alpha\), \(L|_E=5\alpha+\beta\) give

\[
L\cdot W=3ab-4(as+br)+2rs
=5(m-rs)+u+L\cdot\widetilde R.
\]

After using \(ab=4m+\delta\), this is the exact numerical identity

\[
\boxed{5\delta-K=4\bigl(u+L\cdot\widetilde R\bigr).}\tag{3}
\]

Nefness of \(L\) and effectiveness of \(Z_E\) recover the earlier (1).
Since \(L=H+Q'\), the same identity is

\[
\boxed{\delta-K=4\bigl(u+Q'\cdot\widetilde R\bigr).}\tag{4}
\]

If no residual component lies in \(Q\), the last intersection is
nonnegative, proving the earlier (2). These are equalities of intersection
numbers of specified actual cycles. They do not identify those cycles
with the common zero scheme of the two leading symbols.

In particular equality in (1) holds precisely when \(u=0\) and every
residual component has \(L\)-degree zero. Since \(L\) is pulled back from
an ample bundle on \(V_5\), such components are exactly the curves contracted
by \(\phi\): the trisecant ruling lines on \(Q\), with their actual
multiplicities. Equality in (2), under its no-quadric-component hypothesis,
requires \(u=0\) and \(Q'\cdot\widetilde R=0\). The first statement is
about intersection-cycle geometry; neither equality is an assertion that
every allowable numerical tuple is attained.

For the mixed form, decompose \(R=R_{\rm out}+R_Q\), let
\(\delta_{\rm out}=\deg R_{\rm out}\), and write
\([R_Q]_Q=x\alpha_Q+y\beta_Q\), with \(C\) of type \((1,3)\).
Then \(Q'\cdot\widetilde R_Q=y-x\), so (4) gives the previously known

\[
\boxed{\delta_{\rm out}+5x-3y\ge K.}\tag{5}
\]

The ruling with length-three attachment to \(C\) is precisely what weakens
the universal coefficient from one to five. This is a useful geometric
reason to record residual components rather than just their total degree.

## Nef cone and the limit of first-graph positivity

The real Picard space of \(B\) has basis \(H,L\). Both classes are nef.
A fiber of \(\pi\) has \((H,L)\)-degrees \((0,1)\), while a contracted
ruling of \(\phi\) has degrees \((1,0)\). Thus a nef divisor
\(xH+yL\) must have \(x,y\ge0\), and conversely these inequalities
are sufficient. Consequently

\[
\boxed{\operatorname{Nef}(B)
=\mathbf R_{\ge0}H+\mathbf R_{\ge0}L.}\tag{6}
\]

On the exceptional effective cycle, \(H\)-positivity gives just
\(\delta\ge0\); \(L\)-positivity gives (1). Every other nef divisor on
this first graph gives a nonnegative linear combination of these two
inequalities. Therefore changing to the \(V_5\) presentation does not,
by itself, produce a stronger uniform linear nef bound. Its anticanonical
surface \(\Sigma\) pulls back as \(E+3Q'\sim2L\), so simply intersecting
its class supplies no new nef direction either. Its conductor and marked
curve geometry may matter with additional hypotheses, but not as an
automatic extra positivity assumption.

The inherited moving-root refinement makes the additional data explicit.
Suppose every common horizontal root curve in \(E\) has slope at least
\(\rho\ge0\), meaning direction-degree divided by degree over \(C\)
is at least \(\rho\). Then \(u\ge\rho(m-rs)\). Equations (3)–(4) give

\[
\boxed{
(5+\rho)\delta\ge K+\rho(ab-4rs),
}\tag{7}
\]

and, if there is no residual component on \(Q\),

\[
\boxed{
(1+\rho)\delta\ge K+\rho(ab-4rs).
}\tag{8}
\]

These are rearrangements of the support-sensitive inequality already in
October 19 §2a. They become stronger only when a lower slope has actually
been established for the horizontal support of the actual pair. A moving
first-relation label alone is not that hypothesis. If no horizontal
exceptional cycle occurs, \(m=rs\) already gives the exact residual degree
\(ab-4rs\).

## 4. Uniform actual-pair equality controls

Both coefficients can be attained by actual global constructions. These
controls test the stated generality; they do not construct a sole-support
endpoint or show that every extremal numerical tuple exists.

**Universal coefficient five.** Take

\[
F=q^r,\qquad G=P_s(c_0,\ldots,c_6),
\]

where the \(c_i\) are the seven known cubics and \(P_s\) is a general
degree-\(s\) polynomial section on \(V_5\). The pair has degrees
\(a=2r,b=3s\), exact normal orders \(r,s\), and is proper since
\(q\nmid G\). On \(Q\), after removing \(sC\), its remaining divisor
is of type \((2s,0)\): these are \(2s\) general trisecant ruling fibers.
At \(\eta_C\), the quadric normal direction and the other normal form
are coprime, so \(m=rs\). Consequently

\[
R=r\,(\text{the }2s\text{ ruling fibers}),\quad
\delta=2rs,\quad K=10rs,
\]

and \(5\delta=K\). This is compatible with, and extends by powers, the
earlier smooth-quadric sharpness control. One carrier is allowed to be a
power of the quadric; an integral-carrier restriction would change the scope.

**No-quadric-component coefficient one.** Take general sections
\(P_r\in H^0(V_5,\mathcal O(r))\),
\(P_s'\in H^0(V_5,\mathcal O(s))\) and put

\[
F=P_r(c_0,\ldots,c_6),\qquad G=P_s'(c_0,\ldots,c_6).
\]

Their zero divisors have no common point on \(\Gamma\) for a general
choice: choose the first restriction's finite zero set and choose the
second restriction nonzero at those points. The complete-intersection
curve on smooth \(V_5\) is smooth integral by Bertini. Its pullback \(W\)
therefore avoids \(Q'\). It has no curve component in \(E\), because the
two general divisors intersect the fixed surface \(\Sigma\) properly in
finitely many points. Thus \(m=rs\). The actual pair has

\[
a=3r,\quad b=3s,\quad
\delta=ab-4rs=5rs,\quad K=5rs,
\]

so equality holds in (2), with no residual component on \(Q\).
This also follows from \(W\sim rsL^2\), \(L^3=5\), and
\(Q'\cdot L^2=0\). No small-degree STCI problem has been reopened.

## 5. Integer strengthening, usefulness region, and exact limitations

Because \(\delta=ab-4m\), a valid lower bound must be combined with

\[
\delta\ge0,\qquad \delta\equiv ab\pmod4,
\qquad \delta\le ab-4rs.
\tag{9}
\]

For (1), take the smallest nonnegative integer congruent to \(ab\)
modulo four and at least \(\lceil K/5\rceil\). For (2), use \(K\)
instead. If that lower bound exceeds the last upper bound, the specified
normal-order data cannot occur under the stated residual-location
hypotheses. If \(ab\) is not divisible by four, a positive minimum can
come from arithmetic alone rather than from a new geometric restriction.

| Actual degree/order data | Universal graph bound after congruence | Bound if no component of \(R\) lies on \(Q\) |
|---|---:|---:|
| \(a=b=4,r=s=1\) | 0 | 0 |
| \(a=b=5,r=s=1\) | 1 (arithmetic only) | 1 (arithmetic only) |
| \(a=b=6,r=s=2\) | 4 | 20 |
| \(a=6,b=9,r=2,s=3\) | 6 | 30 |
| \(a=b=8,r=s=2\) | 0 | 0 |

For example, the \((6,6)\) statement with exact orders \((2,2)\) really
does force residual degree at least four universally, and at least twenty
when residual components avoid the quadric. The latter value is attained
by the cubic-generated construction. These are specified-order claims,
not claims about all sextic pairs, whose exact orders can be different.

If neither equation has a quadric factor, restriction to \(Q\) gives
\(a/r\ge3,b/s\ge3\). Put \(\alpha=a/r,\beta=b/s\). Then

\[
\frac K{rs}=16(\alpha+\beta)-7\alpha\beta-28,
\qquad
7\frac K{rs}=60-(7\alpha-16)(7\beta-16).
\]

Thus the unsloped bound is geometrically positive only in the region
\((7\alpha-16)(7\beta-16)<60\); in particular both ratios must be less
than four. For low normal orders in sufficiently high degree it becomes
\(\delta\ge0\), apart from the congruence. The same equations then leave
the unrestricted endpoint unresolved. They must not be presented as a
uniform positive residual bound in characteristic zero.



## 7. Computable order-one corollary: the first-normal gcd supplies the slope

There is a useful explicit application of the **already reviewed**
October 19 common-root-slope inequality. It is not an independent new
normal-carrier mechanism. Suppose \(F_a\) has exact generic order one
along \(C\), while \(G_b\) has exact order \(s\). Write its nonzero first
normal symbol, using the accepted balanced conormal splitting, as a pair
of binary forms

\[
f=(f_0,f_1),\qquad \deg f_i=4a-7.
\]

Let \(d_F\) be the degree of their common zero divisor. Dividing that
common factor leaves a basepoint-free pair of degree

\[
h=4a-7-d_F\ge0.
\]

Consequently the only horizontal component of the zero divisor of \(f\)
on \(E\) is the graph of a degree-\(h\) map between the two projective
lines. The remaining zero divisor consists of the vertical fibers over
the first-normal gcd. Every horizontal exceptional component of the
actual strict-pair intersection must therefore be this graph. Its
intersection multiplicity is retained in \(m-s\), rather than read off
from the first symbols. In the notation of §2,

\[
u\ge h(m-s).
\]

If the graph is not common to the second symbol, there is no horizontal
exceptional component and \(m=s\); the displayed inequality is then
vacuous and remains valid. Thus no unspoken common-root or
\(m>s\) assumption is needed for the following corollary.

Substituting \(r=1,\rho=h\) into (7), with
\(K=16(as+b)-7ab-28s\), gives

\[
\boxed{
\deg R\ge
\frac{b(4a^2-14a+16-a d_F)+4s d_F}
     {4a-2-d_F}.}\tag{10}
\]

Indeed the numerator before substitution is

\[
K+h(ab-4s)
=b\bigl((h-7)a+16\bigr)
 +s(16a-28-4h),
\]

and the two brackets become \(4a^2-14a+16-ad_F\) and \(4d_F\).
The denominator is \(h+5\ge5\). If no component of \(R\) lies on \(Q\),
(8) gives the same numerator with the stronger denominator

\[
\boxed{4a-6-d_F=h+1\ge1.}\tag{11}
\]

As throughout, negative numerical right sides add no lower bound beyond
effectivity; positive values should be strengthened by the congruence in
(9). These are inequalities for the genuine residual of an actual proper
pair. They are available without a normality or Q-Cartier hypothesis on
the degree-\(a\) carrier. Integrality may be imposed for comparison with
the carrier formulas below, but is not needed in this graph argument.

For a carrier regular generically along \(C\), the first-normal gcd gives
\(\deg N_{C/S}=14-4a+d_F\). Replacing a numerical self-intersection by
that upper bound in the normal-sheaf capacity argument gives only the
first term of the numerator in (10). The extra nonnegative term
\(4s d_F\) is already supplied by the inherited moving-root graph
inequality, so the weaker gcd-only capacity bound must not be presented
as a new independent mechanism. An exact Mumford self-intersection can
nevertheless be smaller than \(\deg N_{C/S}\); its sharper quantitative
bound can then improve on (10). Which comparison wins depends on the
actual marked carrier geometry and the mate order.

This corollary makes one part of the needed slope data directly
computable from actual homogeneous coefficients. It neither supplies an
automatic positive numerator for all carriers nor replaces the remaining
higher-normal and full-primary geometry.

## Uniform remaining contact after the first blowup

This is a corollary of (1), not a new independent inequality. Keep the
arbitrary actual-pair hypotheses of §1, and set

\[
p=\frac{rs}{ab},\qquad \theta=\frac{\delta}{ab}.
\]

The local intersection formula gives \(rs\le m\), hence
\(p\le(1-\theta)/4\). AM–GM in (1) gives the degree-independent
necessary condition

\[
\boxed{5\theta\ge32\sqrt p-7-28p.}\tag{12}
\]

The original K bound retains the asymmetry of as and br and is at least
as strong. A positive right side of (12) forces a positive residual
fraction for that actual pair; nonpositive values give no such conclusion.

If the pair is an STCI, then \(\theta=0\), \(m=ab/4\), and
\(0\le\sqrt p\le1/2\). The inequality
\(32\sqrt p-7-28p\le0\) consequently forces
\(\sqrt p\le(8-\sqrt{15})/14\); its other root exceeds 1/2. Thus

\[
\boxed{
\frac{rs}{m}\le\frac{79-16\sqrt{15}}{49},\qquad
\frac{m-rs}{m}\ge\frac{16\sqrt{15}-30}{49}
\simeq0.6524027.
}\tag{13}
\]

Here \(m-rs=n\) is the degree over C of the actual horizontal
exceptional intersection cycle from §2. It measures the generic contact
remaining after the first blowup, including its scheme multiplicities.
It is not the degree of R or the number of distinct normal directions.
Consequently every hypothetical supported pair must concentrate over
65.2 percent of its generic intersection multiplicity in this remaining
contact. Coprime generic leading symbols cannot supply such a pair.
The conclusion is uniform in both degrees and imposes no normality,
integrality, saturation or ordinary-initial-CI assumption.

The reciprocal constant \((79+16\sqrt{15})/49\) already occurs in
the [October 19 filtration investigation, §4](normal_filtration_boundary_obstructions.md)
and [October 20 report](normal_filtration_boundary_obstructions.md).
There it bounds a ratio of relation orders under additional saturated
generic-CI hypotheses. Those relation orders must not be identified with
the chosen-equation orders here. No novelty claim is made for the
constant. The useful extraction is the all-pair geometric interpretation
and its asymptotic search consequence.

**Existence and nonexistence:** a construction must create this much
remaining contact and still realize two global equations with no residual
support. For nonexistence, (13) supplies no upper bound contradicting that
requirement. Repeating first-blowup nef calculations cannot improve it
without new data, by §3. A further direction needs a mechanism controlling
actual higher contact, its movement and attachment, or constructing it
globally; a list of local contact types alone does not do so.



## Characteristic reach and limitation

The actual-cycle pushforward formula and criterion Supp(W) subset E use
regular local blowup intersection and purity, and work in arbitrary
characteristic. The displayed V5 model and finite normalization of Sigma are
asserted here in the inherited characteristic-zero scope. The first-blowup
inequality 5delta>=K and its slope refinement need only globally generated
I_C(3) and the balanced normal bundle, so that same derivation works in
characteristic different from two; it does not require the characteristic-zero
V5 contraction. In characteristic two the exceptional ruled surface comes
from O(8)+O(6), so the product/slope calculation and its constants cannot be
transferred unchanged. The [quartic-carrier STCI in every positive
characteristic](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier)
is compatible with the necessary odd-characteristic inequality; it is not
an exclusion theorem.

## The normalized blowup of the full complete intersection

This is a different blowup from the blowup of the reduced quartic
support used above. Its center is the actual CI ideal. The following
component identity works in every characteristic and allows residual
components, nonreduced components and singular reduced supports.

Let \(Y=V(F_a,G_b)\subset\mathbf P^3\) be any proper complete
intersection over an algebraically closed field, and write
\[
[Y]=\sum_j m_j[C_j]
\]
for its irreducible reduced components and generic lengths. Put
\(B=\operatorname{Bl}_Y\mathbf P^3\), with exceptional Cartier
divisor \(E_Y\), and let \(\nu:\overline B\to B\) be its normalization.
This normalization is finite because B is of finite type over a field.
Write
\[
\nu^*E_Y=\sum_i\rho_iD_i,\qquad \rho_i>0.
\]
Every \(D_i\) maps onto an irreducible component \(E_{Y,j}\) of \((E_Y)_{\rm red}\).
Its center in P3 is C_j, never an isolated point. If
\(f_i=[k(D_i):k(E_{Y,j})]\) for this finite map, then
\[
\boxed{\quad
\sum_{i:\,\nu(D_i)=E_{Y,j}}\rho_i f_i=m_j
\quad\text{for every }j.
\quad}                                                     \tag{14}
\]
The degrees include any inseparable part.

**Proof.** The regular immersion gives
\[
E_Y=\operatorname{Proj}_Y\operatorname{Sym}(\mathcal I_Y/\mathcal I_Y^2).
\]
Thus \(E_Y\) is a projective-line bundle over the full nonreduced Y.
Each \(E_{Y,j}\) is the corresponding projective-line bundle over C_j,
and its coefficient in \([E_Y]\) is \(m_j\). Locally this is just
preservation of the generic Artinian length after a purely
transcendental residue-field extension. No smoothness of C_j
is needed. A finite morphism preserves the dimension of each
closed integral subvariety, so a divisor D_i cannot map into
a fiber or a point of \(E_Y\). Finally the projection formula for
the exceptional Cartier divisor and the finite birational
normalization gives
\[
\nu_*[\nu^*E_Y]=[E_Y].
\]
Comparing coefficients proves (14). The regular-embedding
description is recalled in [Aluffi, §2.2](https://www.math.fsu.edu/~aluffi/archive/paper569.old.pdf).
The same proof applies to an lci curve in any smooth
threefold of finite type over a field. \(\square\)

Consequently,
\[
\sum_i\rho_i f_i\deg C_{j(i)}=ab.                         \tag{15}
\]
For a distinguished component C0, the genuine residual degree is
\[
\deg R=\sum_{j(i)\ne C_0}\rho_i f_i\deg C_{j(i)}.
\tag{16}
\]
These are the existing component degrees expressed on the
normalized blowup, not new lower bounds. Further log resolutions
can introduce divisors centered at points. Equation (14) does
not forbid those valuations or remove punctual defects; it
distinguishes them from the divisors of this normalized blowup
and from residual components downstairs.

### The exceptional-coefficient positivity bound

Over \(\mathbf C\), [Ein–Lazarsfeld, Proposition 3.1](https://arxiv.org/pdf/math/9810004)
applies to an ideal J with \(J\otimes L\) globally generated and
L nef on a smooth projective variety. In dimension three it gives
\(\sum_i\rho_i\deg_L C_{j(i)}\le L^3\), retaining repeated centers.
For \(J=\mathcal I_Y\), \(a\le b\), take \(L=\mathcal O(b)\).
The stronger elementary inequality is already
\[
\sum_i\rho_i\deg_L C_{j(i)}
\le b\sum_i\rho_i f_i\deg C_{j(i)}
=ab^2\le b^3.                                           \tag{17}
\]
Thus the redundancy holds for every proper pair, before imposing
sole support. In the STCI case (14) reads
\(\sum_i\rho_i f_i=ab/4\); the published bound only gives
\(\sum_i\rho_i\le b^2/4\).

Their Remark 3.2 subtracts the number \(n_{\rm out}\) of common points
outside Y of three general sections of \(\mathcal I_Y(b)\).
Here \(n_{\rm out}=b(b-a)^2\). For b>a, write these sections as
\(A_\ell F+\lambda_\ell G\); eliminating G twice gives two
general degree-(b-a) equations, and the remaining equation
has degree b. Their complete intersection avoids Y and has
the displayed degree. For a=b the section space is a pencil,
so \(n_{\rm out}=0\). The improved right side is therefore
\[
b^3-n_{\rm out}=ab(2b-a)\ge ab^2,
\]
still weaker than (17). This \(n_{\rm out}\) counts a different three-section intersection;
it is neither the original residual R nor the generic transverse
Milnor number in the [pencil identity](pencil_milnor_budget.md).

Geometrically, normalization distributes each full CI component's
transverse length among exceptional multiplicities and finite
covering degrees. The checked positivity theorem bounds a sum
that is already controlled by that distribution. It supplies
neither an upper limit on later contact nor a positive residual
degree, and does not strengthen the surviving-contact estimate
above. No valuation-tree classification follows.
