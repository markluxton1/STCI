# Genus-two lambda-one line budget: free chains and integral pullback cycles

Date: 2026-10-10. Owner: `lambda1_horizontal_line_budget`, with independent
checks by `plane_proximity_audit` and `anti_nef_star_bound`.

Status at the requested pause: **PROVED HERE, bounded conditional one-line
exclusion; TWO-LINE ARGUMENT SUPPLIED FOR PARENT AUDIT**. No canonical
frontier file is edited. The global genus-two mate lane remains **OPEN**:
this note assumes the absence of the degree-zero horizontal exceptional
prime, and the parent has not yet accepted complete graph coverage or
promoted the two-line argument. Independent agreement is not itself a
proof of a broader exclusion.

The starting reductions are sections 7--8 of
[the adjoint conic model](2026-10-09-session-genus-two-adjoint-conic-model.md)
and sections 2--5 of
[the null-curve audit](2026-10-09-session-genus-two-nullcurve-mate-independent-audit.md).
In the retained noncrepant mate stratum the marked plane model is

    M -> P2,     c# = h,
    L = 4h - 2e0 - sum_{i=1}^8 e_i,
    f = h - e0,
    Z = L - h = 3h - 2e0 - sum_{i=1}^8 e_i,
    Z effective rational sigma-exceptional,
    K.Z = 1,     Z^2 = -3.

Every sigma-exceptional prime is a vertical (-2) curve or a horizontal
(-3) section. At most two horizontal primes exist and they are disjoint.
Smooth embedded descent of c implies h.E is zero or one for every
exceptional prime and at most one h-positive prime occurs in each
connected sigma-exceptional fiber. Hence every proper plane prime in
the exceptional locus is a line. Its possible classes are

    horizontal: H = h - e_i1 - e_i2 - e_i3 - e_i4,
    vertical:   V = h - e0 - e_i - e_j.

Here and below the e_i are total-transform classes; the four or two
simple centers can be infinitely near. A line has multiplicity one at
every center it passes through. This note makes the explicit additional
assumption:

    no horizontal h-degree-zero prime E0 = e0 - e_i - e_j exists.

The missing E0 case is outside the scope of this note.

## 1. The plane blowup clusters are free chains under this assumption

For the strict exceptional prime over a center p_i, write

    D_i = e_i - sum_{p_j proximate to p_i} e_j.

Nefness of L gives

    L.D_i = m_i - sum_{p_j proximate to p_i} m_j >= 0,
    m0 = 2,     m_i = 1 for i > 0.

Thus every simple center has at most one proximate child. The double
center p0 cannot be infinitely near a simple center: its contribution
two would exceed that ancestor's multiplicity one. It is therefore a
proper plane point. It has at most two proximate children. If it had
two, its strict exceptional curve would be exactly the excluded
horizontal (-3) prime E0. Consequently it too has at most one child.

No satellite center can occur. Creating a center at the intersection
of two exceptional curves requires the older of those two curves to
have one child that created the younger curve and a second child at
the satellite point. This contradicts the one-child bound. Each
proper-root cluster is consequently an unbranched chain of free
centers. For a simple-root cluster of length N, its null exceptional
primes are D_1,...,D_(N-1), forming A_(N-1); the last exceptional curve
has L-degree one and is absent from the sigma-exceptional locus.
The analogous e0-rooted cluster cannot meet a horizontal proper line,
since that line avoids p0.

## 2. An integer anti-nef cycle with contact coefficient one is necessary

Let p be a singular point of S lying on the smooth embedded curve c.
Choose a local regular function a on S whose restriction to c is a
uniformizer. On the resolution, its exceptional part above p is an
effective integral cycle Y with positive coefficient at every prime
in that connected fiber. If D is the remaining effective proper
transform divisor, then

    0 = div(a).E = Y.E + D.E

for every exceptional prime E, so Y.E <= 0. Since c# meets its unique
contact prime transversely and the restriction of a has order one,
the coefficient of Y at that contact prime is exactly one. This is
stronger than the singleton/transversality condition alone.

The following integer chain lemma is useful. Suppose a (-3) contact
prime H, with y_H=1, meets node s of an A_(s+t-1) chain, where s,t >= 1.
Let its coefficients be y_j, with artificial endpoints
y_0=y_(s+t)=0, and put d_j=y_j-y_(j-1). The anti-nef inequalities imply

    d_j >= d_(j+1) away from j=s,
    d_s - d_(s+1) >= 1 at j=s.

Because the d_j are integers, either d_s >= 1 or d_(s+1) <= -1. In the
first case monotonicity gives y_s >= s. In the second it gives
y_s >= t. Therefore

    y_s >= min(s,t).

At H the anti-nef inequality is

    sum of the coefficients at its neighboring chain nodes <= 3.

## 3. Exact accounting for a single horizontal proper line

Assume H is the only horizontal prime. Its coefficient a_H in Z is
one because K.Z=1 and every other exceptional prime has K-degree zero.
At each proper root on H, let s >= 1 be the consecutive centers along
H and let t >= 0 be the subsequent centers off H. A chain that has
left H cannot return to it. There are exactly four on-H centers in
total, and at most four off-H centers:

    sum s = 4,     sum t <= 4.

When t=0, H meets the final positive-L-degree exceptional curve, so
that cluster does not attach to its sigma-exceptional fiber. When
t>0, the entire null chain A_(s+t-1) remains present and meets H at
node s. In particular the earlier on-H null curves must not be
discarded from the connected fiber. A vertical proper line cannot
belong to that same fiber, because it too has h-degree one.

Solving the A-chain intersection equations, its contribution to the
Schur complement at H is

    d(s,t) = s*t/(s+t).

The mate equations Z.H=-1 and Z.D_j=0 consequently give

    a_H = 1 / (3 - sum d(s,t)).

Since a_H=1, the sum of these contributions must be two. Put
A=sum s and B=sum t over the attached clusters only. Then A<=4 and
B<=4. The elementary Cauchy inequality gives

    sum s*t/(s+t)
      = A - sum s^2/(s+t)
      <= A - A^2/(A+B)
      = A*B/(A+B)
      <= 2.

Equality two forces A=B=4, and equality in Cauchy forces t=s in every
attached cluster. But the integer chain lemma then gives

    sum y_contact-neighbor >= sum s = 4,

contrary to the anti-nef bound three at H. This excludes the single
horizontal proper-line case under the stated absence of E0. It does
not use a classification of the other vertical exceptional fibers.

## 4. Two horizontal proper lines: revised argument for parent audit

Assume two horizontal proper lines H1,H2 exist. Their disjointness on
M and their plane intersection number one imply that they share
exactly one simple blowup center. It is their original plane
intersection P; after its blowup their tangent directions separate.
Their union therefore uses seven distinct simple centers, leaving
at most one of the eight simple centers outside that union.

The shared cluster can follow at most one line, say H1. If it has k
descendants along H1, then k<=3. It cannot later leave H1: such an
off-line continuation makes all the intervening exceptional curves
null, and the resulting chain connects both H1 and H2 in one
sigma-fiber. That violates the one h-positive prime per fiber rule.
Thus the shared cluster stops at its positive-L-degree terminal
curve. Its null prefix is an endpoint A_k arm on H2, contributing

    delta_k = k/(k+1) <= 3/4.

The one possible center outside the union can produce at most one
additional arm on a horizontal line. If its proper-root cluster has
s preceding on-line centers, the arm is endpoint A_s, rather than
necessarily A1; s<=3. It contributes delta_s<=3/4. If it is attached
to H1, the sharper resource constraint s<=3-k also holds. A center
off both lines in the shared cluster would connect H1,H2 and is
forbidden. Other center placements create no arm on either line.
Vertical proper primes cannot be present in either horizontal fiber.

Each horizontal coefficient is 1/(3-d_i), where d_i is the sum of
these chain contributions in that fiber. If the two contributions
are split between H1 and H2, each d_i<=3/4, so

    a_H1 + a_H2 <= 2/(3-3/4) = 8/9 < 1.

If both are concentrated on H2, then

    a_H1 + a_H2 <= 1/3 + 1/(3-3/4-3/4) = 1.

Equality requires k=s=3. The condition K.Z=1 thus leaves only this
equality configuration. It uses all eight centers in two clusters:

* P=H1 intersect H2, followed by three centers along H1;
* another proper root Q on H2, followed by two further centers along
  H2 and the sole center off H2.

Both proper roots P,Q lie on H2. A vertical proper line V through p0
cannot contain both, because their joining line is H2 and H2 avoids
p0. At either root the first child follows H1 or H2; V has a different
tangent direction, so V cannot contain any later center there.
Consequently V contains at most one simple center and cannot be a
null vertical line, which requires two.

There are therefore no vertical proper exceptional lines in this
equality configuration. All remaining exceptional primes have
h-degree zero. This contradicts the marked correction identity:

    h.Z = 3,

because its proposed exceptional representative has
h.Z=a_H1+a_H2=1. This supplies a two-line exclusion argument for
parent review. The free-chain coverage and equality geometry must
be checked before promoting a complete exclusion of the no-E0
subcase into the canonical frontier.

## 5. Failed preliminary shortcuts retained for continuation

Two tempting shorter bounds were incorrect.

First, four centers on H plus four remaining centers do not mean
there are at most four null vertices in H's fiber. Four consecutive
on-H centers followed by four off-H centers give an A7 chain with
H attached at its middle. Its Schur contribution is two and its
rational correction coefficient would be one. It fails the integer
anti-nef contact test: the middle coefficient of a coefficient-one
pullback cycle must be at least four, exceeding the bound three at
H. Thus this is a counterexample to the naive vertex count, not a
counterexample to the corrected proof in section 3.

Second, in the two-line case the individual bound a_H<=2/5 is false.
The shared root followed by three centers along H1 creates A3 on H2,
whose coefficient can be 4/9, while the isolated H1 coefficient is
1/3. An additional off-line center at a cluster with three on-line
centers can create another A3, so the former proposed total bound
19/21 also lacks graph coverage. The valid preliminary total bound
in section 4 is one, with its equality configuration excluded using
the full marked class h.Z=3.

## 6. Pause boundary

The one-line conditional proof is ready for exact audit. The two-line
argument is written out and supplied for parent audit; its status
has not been promoted during the pause. The h-degree-zero horizontal
prime E0 case is untouched. No conductor classification, descent of
mate sections, exhaustive genus-two theorem, or global STCI conclusion
is asserted here. Resume by checking the chain coverage and two-line
equality configuration against the parent's E0 analysis, while
preserving the integral uniformizer-cycle condition.
