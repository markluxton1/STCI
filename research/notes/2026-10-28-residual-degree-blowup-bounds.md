# Residual-degree bounds from the graph: retrieved inequalities and equality geometry

Date: 2026-10-28. Author: `blowup_linear_systems` research agent.
Status: **independently reviewed provisional consolidation and geometric
interpretations**; see the [separate audit](2026-10-28-residual-degree-blowup-audit.md),
including its order-one addendum. The basic inequalities were already proved
and independently reviewed on October 19. They are not new results of this
pass, and neither they nor the present interpretation is a canonical
unrestricted residual-positivity theorem.

## 1. Exact question and the earlier result that already answers part of it

Over an algebraically closed field of characteristic zero fix
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\). For an actual homogeneous
pair of degrees \(a,b\), with no common surface component and both containing
\(C\), write

\[
[V(F_a,G_b)]=m[C]+R,\qquad \delta=\deg R=ab-4m.
\]

Let \(r,s\ge1\) be the exact generic orders of the two chosen equations
along \(I_C\). They are not the thickness \(m\). No integral-carrier,
normality, saturated-root, or generic coprime-symbol hypothesis is imposed.

Retrieval followed INDEX and MAP, then found the precise relevant result
in [October 19, exceptional cycle balance, §2](2026-10-19-exceptional-cycle-balance-and-vertical-counterexamples.md),
with [independent audit](2026-10-19-exceptional-cycle-and-vertical-family-independent-audit.md).
That reviewed provisional note already proves

\[
\boxed{5\delta\ge K,\qquad
K=16(as+br)-7ab-28rs.}\tag{1}
\]

If no component of the actual residual \(R\) lies on the unique smooth
quadric \(Q\) containing \(C\), it already proves the stronger bound

\[
\boxed{\delta\ge K.}\tag{2}
\]

The note also gives the mixed-ruling and common-root-slope refinements.
Thus the new graph interpretation must not be advertised as a discovery
of (1) or (2). The present contribution is a direct equality/slack
description, the optimality boundary of nef-only reasoning on this graph,
and uniform actual-pair sharpness controls for both coefficients.

The inputs from today's [two-projection note](2026-10-28-blowup-residual-geometry.md)
and [independent audit](2026-10-28-blowup-residual-audit.md) are the actual-cycle
decomposition on the graph and the second contraction to \(V_5\). The
balanced normal bundle is promoted [R-0020](../results/quartic_conormal_characteristic_jump.md).
No accepted proof or inherited verifier was rerun.

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

## 3. How much can the new nef model improve without additional data?

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

## 6. Literature check and next use

The live search checked residual-intersection, blowup, and rational-quartic
terminology. Primary material consulted includes
[Stacks, computing intersection multiplicities](https://stacks.math.columbia.edu/tag/0B01),
[Stacks, blowups](https://stacks.math.columbia.edu/tag/01OF), and the already
identified [Fano-model Lemma 6.13](https://arxiv.org/html/1809.09223v1#S6.L13).
These support the standard intersection/contraction ingredients. The exact
basic residual inequalities were found in the repository before being
re-derived through the new graph picture. No claim of literature novelty or
exhaustive literature coverage is made.

The practical next step is to report \((a,b;r,s)\) and the quadric part of
the actual residual for each construction. If a common-root slope is known,
include it and use (7) or (8). The amount of geometric input is then visible
in the bound. A universally positive answer depending only on arbitrary
large degrees would require additional mathematics; it does not follow
from these first-graph nef inequalities.

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
