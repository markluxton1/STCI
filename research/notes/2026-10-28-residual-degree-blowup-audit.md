# Independent audit: residual-degree bounds and equality on the graph

Date: 2026-10-28. Reviewer: `singular_carrier_construction` research agent.
Source: [residual-degree bounds from the
graph](2026-10-28-residual-degree-blowup-bounds.md).
**Outcome: PASS for the new slack identities, equality descriptions,
nef-cone limitation, actual-pair sharpness controls and usefulness region.**
The basic inequalities are inherited reviewed provisional results from
October 19, correctly identified by the source. No canonical promotion,
unrestricted residual-positivity claim or sole-support conclusion follows.

The literal scope is the fixed characteristic-zero quartic C in P3 and
an actual proper pair of degrees a,b with exact normal orders r,s. The
carriers may be reducible or powers. The generic intersection thickness
m is a different number. The residual R is its actual effective weighted
cycle, with C removed at full generic multiplicity.

## 1. Reconstructing the exceptional cycle and the exact slack

Use the already reviewed graph B=Bl_C(P3)=Bl_Gamma(V5), with
H pulled back from P3, E its exceptional divisor, L=3H-E, and
Q'=2H-E=L-H exceptional for the V5 projection. Let W be the proper
intersection of the two strict surfaces. Its components in E and its
actual residual components give

\[
 [W]=Z_E+\widetilde R.
\]

In E=P1_base times P1_direction, take alpha to be the vertical-fiber
divisor class and beta the horizontal-section class. Then
Z_E=u*alpha+n*beta has u,n>=0 and n=m-rs. The latter is the actual-cycle
generic blowup formula, not merely a Chow calculation. Restrictions
H|E=4alpha and L|E=5alpha+beta give

\[
 H\cdot Z_E=4n,\qquad L\cdot Z_E=5n+u.
\]

From the strict divisor classes aH-rE and bH-sE, the independently
checked triple product is

\[
 L\cdot W=3ab-4(as+br)+2rs.
\]

Substitute n=m-rs and m=(ab-delta)/4. The result is exactly

\[
 5\delta-K=4(u+L\cdot\widetilde R),\qquad
 K=16(as+br)-7ab-28rs.
\]

Since L=H+Q' and H·Rtilde=delta, it also gives

\[
 \delta-K=4(u+Q'\cdot\widetilde R).
\]

These are the claimed exact numerical identities. They retain
horizontal thickness and any vertical exceptional fibers inside u,n;
no vertical curve is declared to be a residual downstairs.

Nefness of L gives 5delta>=K. If no actual residual component lies on
Q, the effective Cartier divisor Q' has nonnegative intersection with
each residual strict transform, giving delta>=K. The hypotheses for
the two coefficients are therefore different and remain necessary.

Equality in the coefficient-five bound requires precisely u=0 and
L·Rtilde=0. L is pulled back from an ample polarization on V5, so
every residual component is then a contracted ruling of Q'. Its image
in P3 is an actual trisecant line. Under the no-quadric-component
hypothesis, equality in the coefficient-one bound requires u=0 and
Q'·Rtilde=0. These are correct numerical equality criteria, not general
existence assertions for arbitrary tuples.

For residual components on Q, source conventions C=(1,3) and
R_Q=(x,y) give Q'|Q=(1,-1), hence Q'·Rtilde_Q=y-x.
Substitution into the second identity gives

\[
 \delta_{\mathrm{out}}+5x-3y\ge K,
\]

with nonnegative omitted contributions from u and the outside residual.
The ruling distinction and signs in the mixed inequality are correct.

## 2. Nef-cone boundary and common-root slopes

The real Picard space has basis H,L. Their nefness is inherited from
the two morphisms. A fiber of the P3 blowup has (H,L) degrees (0,1),
and a ruling contracted to V5 has degrees (1,0). Thus any nef xH+yL
requires x,y>=0; conversely every such combination is nef. This proves
the exact cone claimed by the source.

Subtracting the exceptional-cycle contributions for xH+yL consequently
produces a nonnegative combination of delta>=0 and 5delta>=K. There
is no missing third nef direction on this particular graph. In
particular Sigma pulls back as E+3Q'=2L, so its numerical class does
not furnish one. This does not limit what conductor, marked geometry,
or additional blowups can prove after new information is supplied.

If actual horizontal common-root curves have slope at least rho, their
direction degrees give u>=rho(m-rs). Substituting this into the two
slack identities and using 4m=ab-delta yields precisely

\[
 (5+\rho)\delta\ge K+\rho(ab-4rs),
\]

and, in the no-quadric-component case,

\[
 (1+\rho)\delta\ge K+\rho(ab-4rs).
\]

The source correctly requires a slope statement about the actual
horizontal support. A label on a first relation does not establish it.
If there is no horizontal exceptional cycle, n=0 gives m=rs and the
residual degree is already exactly ab-4rs.

## 3. Both sharpness families are actual global pairs

For F=q^r and G=P_s(c_0,...,c_6), degrees are 2r,3s. General P_s
does not vanish identically on Gamma or Sigma, so G is not divisible
by q and has exact C-order s. On Q its restriction, after sC is
removed, is a general divisor of type (2s,0), hence 2s distinct
trisecant ruling fibers. The generic initial polynomial of G is
not divisible by the quadric's normal linear form, so intersection
with its r-th power has generic length rs. The actual cycle is
rsC plus r times those 2s lines. Therefore

\[
 \delta=2rs,\qquad K=10rs,
\]

and equality holds in the coefficient-five estimate. The first
carrier is allowed to be a power because this estimate imposes no
integrality assumption. The example would not test an integral-carrier
theorem with different hypotheses.

For F=P_r(c) and G=P'_s(c), choose general hypersurface sections of
degrees r,s on V5. Their restrictions to the conic have disjoint zero
sets, so their complete-intersection curve avoids Gamma and its
pullback avoids Q'. Two general divisors meet the fixed Sigma in
finitely many points, so W has no curve component in E. Bertini on
the smooth threefold gives a smooth integral curve. The resulting
actual pair is proper and has exact normal orders r,s and m=rs.
Thus

\[
 a=3r,\quad b=3s,\quad \delta=5rs,\quad K=5rs.
\]

There is no quadric residual component and the coefficient-one bound
is attained. These existence arguments use actual global cubic
substitutions and the inherited section dictionary, rather than
function-field coefficients or a numerical class alone.

## 4. Integer bounds and the region where geometry is positive

The restrictions delta>=0, delta congruent to ab modulo four, and
delta<=ab-4rs follow respectively from effectivity, the Bezout degree
identity, and m>=rs. Combining congruence with the ceiling of K/5 or
K is correct. I recalculated all five rows of the source's table:
the pairs of lower bounds are (0,0), (1,1), (4,20), (6,30), and
(0,0), respectively. The (5,5;1,1) value is arithmetic only, as
the source states. A lower bound exceeding ab-4rs rules out that
specified collection of order and residual-location hypotheses.

If neither equation has a quadric factor, its nonzero restriction to
Q vanishes at least rC or sC, respectively. Nonzero sections of the
resulting bidegree bundles require a/r>=3 and b/s>=3. Writing these
ratios as alpha,beta gives

\[
 7K/(rs)=60-(7\alpha-16)(7\beta-16).
\]

Thus geometric positivity of this unsloped estimate is exactly the
stated product inequality. If either ratio is at least four, the
product is at least 12*5=60; both must be below four for strict
positivity. This verifies the source's explanation of why large
degrees at low normal order make this particular bound trivial.

## 5. Evidence and scope retained

The two-projection model and the actual-cycle proof were independently
reviewed earlier in [today's blowup
audit](2026-10-28-blowup-residual-audit.md). The prior October 19
inequalities are explicitly attributed and were not relabelled as
new results. Standard primary ingredients were checked in the live
session, including [Stacks blowups](https://stacks.math.columbia.edu/tag/01OF)
and the literal fixed-quartic model in [Cheltsov–Przyjalkowski–Shramov,
Lemma 6.13](https://arxiv.org/html/1809.09223v1#S6.L13).

No mathematical correction was needed in this audit. The useful
conclusion is quantitative and support-sensitive: exact normal
orders, the quadric portion of the genuine residual, and actual
root slopes determine what the graph inequalities say. They do not
give a positive residual degree for every characteristic-zero pair.
The no-integral-carrier scope, different equality mechanisms, and
limits of nef-only reasoning must accompany any later summary.
