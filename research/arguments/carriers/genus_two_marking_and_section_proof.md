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
a complete lambda=1 exclusion in this pause record. The case
with e0-e_i-e_j present still requires separate coverage,
including its possible unique satellite and the entire
connected fiber containing the contact vertical line.

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

## 7. Scope

The proved conclusions are the ruled marking, \(D_8\) lattice, plane marking, optional \(F_3\) model, and proximity restrictions. The [free-chain argument](#8-free-chain-proof-when-the-marked-prime-is-absent) excludes the absent-\(E_0\) case; the ambient-conductor proofs handle its remaining trisecants. Numerical class lists alone do **not** establish prime effectivity or normalization descent. Intersection calculations extend to other characteristics only when the same actual rational marked model exists; the lattice gives no positive-characteristic STCI conclusion.

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
