# Bounded audit: exceptional prime classes in the lambda-one plane marking

Date: 2026-10-10. Auditor: degree-one-anticanonical counteraudit agent.
Status: **PROVED HERE / accepted bounded structural classification**.
No canonical frontier file or computation script was edited. This note
does not exclude the lambda-one stratum or assert that any listed
configuration is realized by an actual quartic normalization or mate.

## 1. Hypotheses and total-transform convention

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

## 2. Nefness forces the double center to be proper and controls satellites

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

## 3. Degree-zero exceptional primes

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

## 4. Positive plane degree: complete arithmetic classification

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

## 5. Embedded smoothness excludes the conic and cubic and limits components

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

## 6. Explicit necessary intersection and graph restrictions

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

## 7. Caveats, useful counterexamples to shortcuts, and freeze boundary

The formula subtracting all descendants is false. In a free chain
p_b proximate to p_a, p_c proximate only to p_b, the final strict
transform of the a-exceptional has class e_a-e_b, not e_a-e_b-e_c.
At the allowed satellite pattern j proximate to 0 and i, the classes
are e0-e_i-e_j and e_i-e_j, with intersection zero; coefficient two
at e_j in either individual prime would be incorrect. These are
local blowup illustrations of the formulas, not claimed realized
quartic configurations.

Applying nonnegative b_a to degree-zero primes would likewise be
incorrect. Applying h.E<=1 using only numerical equivalence c#=h,
without the smooth embedded curve and isomorphism hypotheses, would
also be unjustified. Those geometric hypotheses are essential to
section 5.

The class list, proper-double-center conclusion, proximity budget,
at-most-one-satellite restriction, and graph restrictions are accepted.
The arithmetic class list was independently checked by a second
bounded audit. Agreement is provenance; the proofs are the explicit
intersection and multiplicity arguments above. Actual incidence,
prime effectivity, full graph realization, normalization/conductor
descent, and existence or exclusion of a mate remain separate work.
No lambda-one exclusion is claimed. This note is frozen for the
requested pause closure after its content and hash are reported.
