# Genus-two ruled, plane, and proximity markings

These independently accepted markings retain the actual centers and
embedded-curve hypotheses. They do not assert that every abstract root
configuration is realized. The full fixed-C0 quartic-mate problem is
closed by [the complete carrier proof](quartic_carrier_proof.md);
the bounded marking and counterexamples below are its reusable geometry.

The [entire conductor](genus_two_entire_conductor_proof.md) and [ambient conic model](genus_two_ambient_conic_model_proof.md) establish, over an algebraically closed characteristic-zero field,

    M smooth rational; L nef, big and globally generated;
    L^2=4, K.L=-2, K^2=0, h0(L)=4;
    f=K+L is a connected basepoint-free rational conic pencil.

The complete |L| image is the actual integral quartic X. Its
normalization resolution sigma contracts exactly the L-null
primes: vertical (-2)-curves and at most two disjoint horizontal
(-3)-sections. A mate retains both (lambda,q)=(0,4) and (1,3).

## 1. The eight-blowup ruled marking passes

Contract vertical (-1)-curves of the rational fibration until it
is relatively minimal. A smooth relatively minimal rational
fibration over P1 is a P1-bundle, hence a Hirzebruch surface F_n.
The morphism M->F_n is a sequence of point blowups, with
infinitely near centers allowed. K_M^2=0 and K_Fn^2=8 give exactly
eight blowups.

At each step the ruling class pulls back. The canonical blowup
formula therefore preserves the actual identity L=f-K. The
vertical (-1)-curve being contracted has L-degree one, so the
corresponding multiplicity is one. Nefness of the pushed-down
L follows by intersecting the strict transform of any curve
and adding the nonnegative center multiplicity. On F_n, with
C_min^2=-n, the resulting class is

    L0=2C_min+(n+3)f.

Its intersection with C_min is 3-n. Nefness gives 0<=n<=3. Using
the total transforms e1,...,e8 gives the exact integral marking

    L=2C_min+(n+3)f-sum e_i.

The point centers need not be distinct proper points. A claim
about their geometric position requires a separate proximity
argument; none is hidden in the total-transform formula.

## 2. The vertical lattice is D8 exactly

In this marking an integral class perpendicular to f has the
form v=b f-sum d_i e_i. Orthogonality to L says

    2b=sum d_i,

and v^2=-sum d_i^2. Thus f-perpendicular intersect
L-perpendicular is precisely the negative D8 lattice, identified
with integer eight-tuples of even sum. The norm-two vectors are
the 112 signed pairs +/-u_i+/-u_j, corresponding to

    +/- (e_i-e_j),     +/- (f-e_i-e_j).

Every vertical exceptional prime is a root. Distinct such
effective primes have nonnegative intersection; their numerical
classes cannot coincide or be negatives, because that would
give negative intersection or an effective numerically-zero
sum. Their intersections are therefore zero or one. They give
an actual negative-definite root configuration, of rank at most
eight. The signed-coordinate argument for root subsystems
applies, retaining A and D blocks. This does not assert that
every abstract embedded root configuration is geometrically
realized by the given eight centers.

## 3. The mate section has a nine-point plane marking

In the retained (lambda,q)=(1,3) stratum, c# is a smooth P1 of
square one. The exact restriction sequence

    0 -> O_M -> O_M(c#) -> O_P1(1) -> 0

and H1(O_M)=0 give h0(c#)=3 and surjectivity onto O_P1(1).
This system has no base point on c#, and its canonical section
is nonzero away from c#. Hence |c#| is globally generated.
Its positive square makes its image two-dimensional in P2;
the degree formula c#^2=1 forces generic degree one. It is a
birational morphism to P2, factored into nine point blowups.

Let h be the pulled-back plane line class, so c#=h, and use
the nine total exceptional classes. Successive nef pushdowns
give integral multiplicities m_i>=0 in L=4h-sum m_i e_i. The
intersection equalities are

    sum m_i=10,     sum m_i^2=12.

Thus sum m_i(m_i-1)=2; exactly one m_i is two and the other
eight are one. This proves the owner's marked plane reduction

    L=4h-2e0-sum_{i=1}^8 e_i,
    f=h-e0,     c#=h,
    Z=3h-2e0-sum_{i=1}^8 e_i.

The last identity is an integral class identity. The actual
effective exceptional representative of Z can have fractional
prime coefficients; no integral-effectivity conclusion is made.

The double center is a proper point of P2. If it were proximate
to an earlier simple center, the proper exceptional prime of
that simple center would have L-degree at most 1-2<0. This
contradicts nefness. Independent proper blowups can be reordered
to blow up this double point first, so f is the actual pencil of
lines through a proper point p0, not only an abstract class.

The actual member c# maps isomorphically onto a line avoiding
all proper point centers: passing through a center would lower
the strict-transform class from h, while a total transform would
be reducible. It consequently avoids all exceptional primes
of this plane blowup map, including infinitely near ones.

## 4. The optional F3 model preserving a horizontal section also passes

Let E be any horizontal sigma-exceptional (-3)-section. The
rational fibration can be made relatively minimal by contracting
vertical (-1)-curves disjoint from E. Indeed, if a reducible fiber
had no such curve, E.F=1 would force all its (-1)-components
to consist of one multiplicity-one curve meeting E. Every other
rational fiber component has self-intersection at most -2 and
nonnegative canonical degree. Summing canonical intersections
would give K.F>=-1, contrary to K.F=-2. Thus an available
(-1)-component is disjoint from E. This argument continues after
each contraction.

The resulting ruled model preserves E^2=-3, and all contracted
centers are away from its transform. Nef L pushes down as in
section 1 and restricts the Hirzebruch index to n<=3. A section
of F_n with negative self-intersection -3 must be its negative
section, so the resulting model is F3 and E=C_min. There are
eight blowups, all away from that negative section, and

    L0=2C_min+6f.

In the mate section stratum, push c# down to a section
C_min+b f. Each of the centers lying on its successive strict
transform has multiplicity one. If their number is N_c, then

    c#^2=-3+2b-N_c=1,
    c#.E=b-3.

Smooth embeddedness of c forces c#.E to be zero or one by the
accepted local uniformizer argument. Thus b=3 or 4, with
N_c=2 or 4 respectively. This is a valid bounded model
observation; it does not eliminate either possibility.

One must not infer that the negative section is disjoint from
all vertical null curves simply because the blowup centers
avoid it. For example, blowing up two points away from E on one
fiber makes that fiber's strict transform a null (-2)-curve
which still meets E. This invalid inference was considered as
an informal lead and rejected before relying on the claim.

## 5. Plane proximity and the stronger local condition

A bounded child audit checks the marked-prime list separately.
Nefness gives each simple center at most one directly proximate
child and the double center at most two. The possible positive
plane-degree sigma-exceptional primes are vertical lines
h-e0-e_i-e_j and horizontal lines h-sum_{four}e_i; positive
degree horizontal conics and cubics would have h.E=2 or 3 and
are excluded by smooth embeddedness. The degree-zero vertical
primes are proper exceptional (-2)-curves, and the possible
degree-zero horizontal prime is e0-e_i-e_j. These prime claims
and the unique possible satellite point are recorded in that
child's separate note before any global graph exhaustion.

There is at most one positive-h-degree prime in each connected
sigma-exceptional fiber. Otherwise c# would meet that fiber
twice or meet multiple local branches at one point, contradicting
its isomorphism onto the smooth embedded c. For the contact
prime of such a fiber there is an additional exact condition:
a regular function restricting to a uniformizer of c pulls back
with an integer positive exceptional cycle Y, anti-nef on every
exceptional prime, and coefficient one on the contact prime.
This is stronger than merely being transverse to that prime.

The proper-horizontal-line cases, with the degree-zero
horizontal prime absent, are being examined by a bounded
free-chain/Schur-complement argument. They are not claimed as
a complete lambda=1 exclusion in this pause record. The case with e0-e_i-e_j present is **not settled by this plane-marking argument**: its possible unique satellite and entire connected contact fiber require the separate ambient-conductor proof. The complete quartic-carrier exclusion is established by the linked ambient proofs, so this is a limitation of the marking method, not an open mate case.

## 6. Counterexamples to shortcuts

* Counting only the centers after a proper line leaves its
  cluster does not count all null root vertices. A cluster with
  s centers on that line and t off it has A_(s+t-1), attached
  at node s; its Schur contribution is st/(s+t). Four on-line
  and four off-line centers give A7 attached in the middle,
  not an arm of length four. Thus a naive four-unused-centers
  estimate is false.
* Two distinct proper horizontal lines sharing their one plane
  intersection can yield a null A3 predecessor chain attached
  to one of them. Its correction coefficient can be 4/9,
  contradicting a proposed individual bound of 2/5. A valid
  total coefficient estimate must include this shared chain.
* The degree-zero horizontal prime can attach to an internal
  vertex of an A-chain after the unique possible satellite.
  Therefore treating every such graph as a three-arm star
  centered at the (-3)-prime misses an allowed proximity
  pattern. The earlier star-response bound was only conditional
  and was not accepted.
* q=4 is not a genus-two identity without lambda=0. The general
  identity q+lambda=4 retains both lambda=0 and lambda=1.

## 7. Logical scope

The ruled marking, \(D_8\) lattice, plane marking, optional \(F_3\) model, and proximity restrictions are proved. The [free-chain argument](#8-free-chain-proof-when-the-marked-prime-is-absent) excludes the absent-\(E_0\) case; other trisecants require ambient-conductor arguments. Numerical classes alone establish neither prime effectivity nor descent. The characteristic-zero carrier conclusion does not automatically extend to positive characteristic.

## 8. Free-chain proof when the marked prime is absent

Assume that the horizontal prime \(B=e_0-e_i-e_j\) of plane degree zero
is absent. In the plane marking below there is one double center \(p_0\)
and eight simple centers. For the strict exceptional curve
\(D_i=e_i-\sum_{j\succ i}e_j\), nefness gives
\(L\cdot D_i=m_i-\sum_{j\succ i}m_j\ge0\), where \(j\succ i\)
denotes a proximate center, \(m_0=2\) and \(m_i=1\) for \(i>0\).
Each simple center has at most one proximate child. The double center
must be proper and can have at most one proximate child, since two would
produce \(B\). A satellite would require two proximate children at the
older of its two exceptional curves. The clusters are therefore free
chains. A simple cluster with \(N\) centers has null prefix
\(A_{N-1}\), ending at the last center of positive \(L\)-degree.
The chain rooted at \(p_0\) cannot meet a horizontal proper line, which
avoids \(p_0\).

Smooth embedded descent permits at most one \(h\)-positive prime per
connected exceptional graph. The \(h\)-positive exceptional primes
are proper lines. A horizontal one passes through four simple centers
and a vertical one passes through \(p_0\) and two simple centers.
Once a free chain leaves a line it cannot return, since the next center
lies at a different point of the previous exceptional divisor.

At a singular point on the smooth downstairs curve, choose a local
function on \(S\) restricting to a uniformizer on that curve. The
exceptional part \(Y\) of its full pullback has positive integral
coefficients. The proper part has nonnegative intersection with every
exceptional prime, so \(Y\) is anti-nef. The unique transverse contact
has coefficient one, since the pullback has order one on the strict
curve. When a contacted \((-3)\)-curve \(H\) meets the \(s\)-th vertex
of an \(A_{s+t-1}\) chain, write its chain coefficients as \(y_j\),
with \(y_0=y_{s+t}=0\). The differences
\(d_j=y_j-y_{j-1}\) are nonincreasing and have a drop of at least one
at \(s\). Since they are integral, either \(d_s\ge1\) or
\(d_{s+1}\le-1\), so \(y_s\ge\min(s,t)\). At \(H\), the sum of
neighbor coefficients must be at most three.

For a single horizontal line \(H\), a chain of \(s\) centers on it
followed by \(t>0\) centers off it contributes \(st/(s+t)\) to the
Schur complement at \(H\); for \(t=0\) the terminal curve has
positive \(L\)-degree and the cluster contributes no arm. The unique
horizontal line has coefficient one in \(Z\). Its equation
\(Z\cdot H=-1\) and the homogeneous chain equations require the
contributions to sum to two. For the attached clusters
\(A=\sum s\le4\) and \(T=\sum t\le4\).
Cauchy gives \(\sum st/(s+t)\le AT/(A+T)\le2\), with equality only
when \(A=T=4\) and each \(s=t\). The integer chain test then requires
a sum of neighboring coefficients at least four, contradicting three.

Two disjoint horizontal proper lines on the resolution share exactly one
simple plane center and together use seven of the eight simple centers.
The shared cluster follows at most one line, say \(H_1\). It cannot leave
that line, since the resulting null chain would connect both
\(h\)-positive lines in one exceptional graph. Hence its null prefix is an
endpoint \(A_k\) arm on \(H_2\), with \(k\le3\). The one center
outside the lines can create at most one additional endpoint \(A_s\) arm,
\(s\le3\), with the sharper restriction \(s\le3-k\) if the arm is on
\(H_1\). It cannot attach in the shared cluster. The two contributions
are at most \(3/4\) each. The sum of the two horizontal coefficients
\(1/(3-d_i)\), where \(d_i\) is the sum of arms on that line, is at most
\(8/9\) when the arms are split and at most one when they are on the
same line. The required \(K_M\cdot Z=1\) forces the latter bound to
be attained, with \(k=s=3\).

The equality configuration uses two clusters. The shared root follows
\(H_1\) for three more centers. A second root on \(H_2\) follows that
line for two more centers and takes the only center off both lines.
A vertical exceptional line through \(p_0\) cannot contain both
roots, whose joining line is \(H_2\), and cannot contain later centers
at either root because its direction differs from that of the first
child. There is no vertical exceptional proper line. The two horizontal
lines therefore give \(h\cdot Z=1\), contrary to \(h\cdot Z=3\).

Two preliminary bounds fail. Four consecutive on-line centers followed
by four off-line centers give an \(A_7\) arm attached at its middle,
not a four-vertex bound. Its rational coefficient at \(H\) can be
one, but the integral anti-nef cycle requires a neighboring coefficient
of at least four. In the two-line case a shared root followed by three
centers on \(H_1\) gives an \(A_3\) arm on \(H_2\), allowing coefficient
\(4/9\) there and \(1/3\) on the isolated line, so the proposed individual
bound \(2/5\) fails. A second \(A_3\) arm can arise from the remaining
off-line center; the proposed total bound \(19/21\) misses this case.

Independent review accepted both line cases under the characteristic-zero
marked section and smooth descent hypotheses with \(B\) absent. The
integer recurrences and intersection inequalities alone remain available
when those geometric inputs are established in another characteristic.


---

## Exceptional-prime class and proximity classification

### Exceptional prime classes in the lambda-one plane marking

This bounded proximity classification is conditional on the marked-section hypotheses. It supplies necessary constraints, not a standalone mate exclusion; the full carrier theorem is established separately.

#### 1. Hypotheses and total-transform convention

Work over an algebraically closed field of characteristic zero. Keep
the hypotheses of the accepted genus-two nullcurve audit: sigma:M->S
is a resolution of a normal surface; the nef divisor L is pulled back
from an ample divisor on S; and its complete map is birational onto
the actual integral quartic. In the lambda-one stratum the actual
smooth lifted curve c# maps isomorphically to a smooth embedded curve
c in S. Its complete system supplies a birational morphism

    q:M->P2,

consisting of nine successive point blowups, possibly infinitely near.
The actual c# is a smooth member of class h, mapping to a line that
avoids the blowup centers. Use the total exceptional classes e0,...,e8,
so

    h^2=1, e_i^2=-1, h.e_i=e_i.e_j=0 for i!=j,
    K=-3h+sum_{i=0}^8 e_i,
    L=4h-2e0-sum_{i=1}^8 e_i,
    f=K+L=h-e0,             c#=h.

Every sigma-exceptional prime is assumed already proved to be either
a vertical smooth rational (-2)-curve, with f.E=0, or a horizontal
smooth rational (-3)-section, with f.E=1. There are at most two
horizontal primes, and they are pairwise disjoint. Every such prime
has L.E=0. The classification below starts with these proved inputs.

For a blowup center p_a, let P(a) be the set of later centers lying on
the then-current strict transform of the exceptional curve born at
p_a. These are the centers directly proximate to p_a, not all indirect
descendants. The final prime strict transform is exactly

    F_a=e_a-sum_{j in P(a)} e_j.                 (1)

Each coefficient in this subtraction is one because the strict
exceptional curve remains smooth. A satellite center belongs to two
different sets P(a) and contributes once to each respective formula;
it does not contribute twice to one prime. This follows inductively
from the strict-transform formula for one blowup. For a primary
reference on these conventions and the corresponding proximity
inequalities, see [Calabri--Ciliberto, On Cremona contractibility,
section 2, p. 392, equation (2)](https://seminariomatematico.polito.it/rendiconti/71-34/0.pdf).

#### 2. Nefness forces the double center to be proper and controls satellites

Write m0=2 and m_a=1 for a>=1. Formula (1) gives

    L.F_a=m_a-sum_{j in P(a)} m_j >= 0.         (2)

If p0 were infinitely near, it would be proximate to some earlier
center p_a with a!=0. Then L.F_a<=1-2<0, contrary to nefness.
Thus p0 is a proper point of P2. Independent proper-center branches
can be reordered to blow up p0 first. Consequently f=h-e0 is the
actual pulled-back pencil of lines through this proper point.

After this observation every member of P(a) is a simple center. If
r_a=|P(a)|, (2) becomes

    r0<=2,                  r_a<=1 for every a>=1.              (3)

There is at most one satellite center in the entire marking. Indeed,
suppose a center p_j lies at the intersection of two older strict
exceptionals F_a,F_b, with p_a earlier than p_b. Their intersection
could exist only if the creation point p_b lay on the strict transform
of F_a: subsequent blowups can remove an intersection of two old
strict transforms, but cannot create one. Thus both p_b and p_j are
directly proximate to p_a. Inequality (3) forces a=0. Such a satellite
is therefore the second direct child of p0, at the intersection of
the p0 exceptional and the exceptional of its first child p_i.
It exhausts p0's two-child budget; no further satellite is possible.

The branches over all other proper points consist of free chains.
Over p0 there are at most two free branches, or the single pattern

    first child i proximate to 0,
    satellite j proximate to both 0 and i,
    later free chain starting at j.

This is a necessary proximity restriction, without a realizability
assertion for the complete marked linear system.

#### 3. Degree-zero exceptional primes

Since p0 is proper, (1) gives

    F_a^2=-1-r_a,
    f.F_0=1,                f.F_a=0 for a>=1,
    L.F_0=2-r0,             L.F_a=1-r_a for a>=1.

Accordingly the degree-zero sigma-exceptional primes have precisely
the following forms, with the proximity relations required by (1):

    R_ab=e_a-e_b,            a,b in {1,...,8}, P(a)={b};
    B_A=e0-e_i-e_j,          A={i,j}=P(0), r0=2.

The R_ab are vertical (-2)-curves. The unique possible B_A is a
horizontal (-3)-section. In particular there cannot be two distinct
degree-zero horizontal primes.

The graph on degree-zero vertical primes alone is a disjoint union
of A-chains: every simple center has at most one direct child, and
the satellite restriction prevents a child from having two simple
parents. For two consecutive chain roots their intersection is one,
and all other distinct roots on that chain have intersection zero.

If p0 has two free children i,j, B_A can attach to the initial root
of each of their two chains. If j is the satellite child of 0 and i,
then

    B_A.R_ij=0,
    B_A.R_jk=1 if the later child k of j exists.

Thus B_A attaches to the second vertex of the chain i->j->k->...,
rather than to R_ij. This can make that second vertical vertex
trivalent if the chain continues. If j has no child, R_ij and B_A
are disjoint components of the degree-zero sigma-exceptional locus.

#### 4. Positive plane degree: complete arithmetic classification

If a prime E has d=h.E>0, its plane image is an integral plane curve
of degree d and E is its strict transform. Write

    E=d h-sum_{a=0}^8 b_a e_a,          b_a>=0 integral.         (4)

Here b_a is the actual multiplicity of the successive strict transform
at p_a. This nonnegativity holds for infinitely near and satellite
centers as well. It does not apply to degree-zero F_a: in the notation
of (4), that prime has b_a=-1 at its creation index.

For every positive-degree prime, the additional proximity constraints
are

    b_a >= sum_{j in P(a)} b_j,                              (5)

because E.F_a>=0 for the distinct primes E and F_a. These inequalities
remain necessary after the following arithmetic classification.

If E is vertical, f.E=0 and E^2=-2 give

    b0=d,
    sum_{a=1}^8 b_a=2d,
    sum_{a=1}^8 b_a^2=2.

The last equality forces two entries to be one and all others zero;
their sum then forces d=1. The only possible positive-degree vertical
prime class is therefore

    V_P=h-e0-e_i-e_j,       P={i,j} subset {1,...,8}.          (6)

It is the strict transform of an actual plane line through p0.

If E is horizontal, f.E=1 and E^2=-3 give

    b0=d-1,
    sum_{a=1}^8 b_a=2d+2,
    sum_{a=1}^8 b_a^2=2d+2.

Nonnegative integrality forces every b_a for a>=1 to be zero or one.
There are 2d+2 ones among eight entries, so 1<=d<=3. The exhaustive
arithmetic list is

    d=1: h-sum_{a in T} e_a,              |T|=4;
    d=2: 2h-e0-sum_{a in T} e_a,          |T|=6;
    d=3: 3h-2e0-sum_{a=1}^8 e_a.

No prime-effectivity or incidence claim is implicit in this list.
Adjunction imposes no extra equation here: K.E=f.E follows from
L.E=0 and f=K+L, and the displayed squares already give genus zero.

#### 5. Embedded smoothness excludes the conic and cubic and limits components

The assumption that c#->c is an isomorphism to a smooth embedded
curve supplies more than a numerical divisor identity. Let p be a
singular point of S lying on c, and P the unique point of c# above p.
Choose a local function a in the maximal ideal of O_(S,p) whose
restriction to c is a uniformizer; such a function exists because
O_(S,p)->O_(c,p) is surjective. Its pullback has positive order along
every exceptional prime above p. The smooth local ring O_(M,P) is
factorial. Restriction to c# has order exactly one, hence

    1 >= sum of local intersection multiplicities of c#
         with exceptional branches through P.

It follows that exactly one exceptional prime passes through P,
that c# meets it transversely, and that no other point of that
exceptional fiber meets c#. Every connected exceptional graph is
contained in one fiber of sigma; thus it has at most one vertex E
with c#.E>0. In particular

    h.E=c#.E is either zero or one for every exceptional prime.

The horizontal conic and cubic in section 4 have h-degree two and
three and are excluded. All surviving positive-degree exceptional
primes are therefore plane lines: (6), with square -2, or

    H_T=h-sum_{a in T} e_a,              |T|=4, square -3.     (7)

Each connected sigma-exceptional graph has at most one such line
vertex. Consequently distinct positive-degree exceptional primes
are pairwise disjoint, and they cannot be connected even through
degree-zero exceptional vertices.

#### 6. Explicit necessary intersection and graph restrictions

For a chain root R_ab=e_a-e_b, intersections with V_P,H_T,B_A are

    V_P.R_ab = 1_(a in P)-1_(b in P),
    H_T.R_ab = 1_(a in T)-1_(b in T),
    B_A.R_ab = 1_(a in A)-1_(b in A).

They must be nonnegative; an entry one gives a single transverse
intersection because both primes are smooth. This enforces the
prefix conditions along the corresponding proximity chains. The
complete root-root formula is

    R_ab.R_cd=-delta_ac+delta_ad+delta_bc-delta_bd.

For distinct positive-degree vertices, the preceding disjointness
condition gives

    V_P.V_Q=-|P intersection Q|=0,
    H_T.V_P=1-|T intersection P|=0,
    H_T.H_U=1-|T intersection U|=0.

Thus vertical line supports are pairwise disjoint, each horizontal
line support meets each vertical line support in exactly one index,
and two horizontal line supports meet in exactly one index. There
are at most four positive-degree vertical primes, because their
two-element supports are disjoint in an eight-element set. This is
an upper bound, not an existence statement.

For the possible degree-zero horizontal B_A,

    B_A.V_P=1-|A intersection P| >=0,
    B_A.H_T=-|A intersection T|=0.

The second equality is forced already by nonnegative prime
intersection, consistently with horizontal disjointness. More
strongly, (5) and the zero multiplicity of H_T at p0 show that H_T
passes through no center above p0. Its exceptional graph component
therefore contains no B_A. A component containing B_A may contain
at most one positive-degree vertical line. Two or more V_P with
A intersection P empty would each meet B_A and violate this rule.

There is at most one B_A and at most two horizontal vertices in
total. If B_A exists, at most one H_T can exist; otherwise at most
two H_T can exist. Distinct horizontal vertices have no direct edge.
Each final graph is assembled from the degree-zero chains and the
possible B_A described in section 3, with at most one plane-line
vertex per connected component. Every edge permitted by the marked
intersection formulas has multiplicity one. A horizontal section
also meets at most one component of any given f-fiber, at a smooth
point of that fiber, since its total fiber intersection is one.

#### 7. Caveats and invalid shortcuts

Subtracting **all** descendants from an exceptional class is false: for a free chain \(p_b\succ p_a,\ p_c\succ p_b\), the final \(a\)-prime is \(e_a-e_b\), not \(e_a-e_b-e_c\). For a satellite \(j\) proximate to \(0,i\), the strict primes \(e_0-e_i-e_j\) and \(e_i-e_j\) have intersection zero; neither carries coefficient two at \(e_j\). Degree-zero primes need not satisfy the nonnegative \(b_a\) condition, and \(h\cdot E\le1\) cannot follow from numerical \(c^\#=h\) without the actual smooth embedded curve and isomorphism hypotheses.

The arithmetic class list, proper double center, proximity budget, at-most-one-satellite bound, and graph restrictions are conditional necessary results. The local blowup examples are not globally realized quartic configurations. Effectivity, incidence, full graph realization, conductor descent, and existence/exclusion of a mate are not proved here. No \(\lambda=1\) exclusion is claimed.

