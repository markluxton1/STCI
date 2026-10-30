# Historical mathematical source compilation

Full original mathematical text retained below. Original hypotheses, failures, qualifications and unresolved cases retain their source status; this compilation is not an independent correctness audit.

---

## Source: 2026-10-07-session-normal-carrier-independent-audit.md

# Independent audit of the reduced exceptional normal-quartic exclusion

Date: 2026-10-07. Status: **ACCEPTED PROOF AUDIT under the recorded inputs**.
This audit accepts the new conclusion in
`2026-10-06-session-normal-carrier-progress.md`: a normal quartic carrier
for the fixed C0 in characteristic zero that admits any mate must have
a reducible nonreduced exceptional anticanonical divisor. It does not
exclude those nonreduced configurations, nonnormal carriers, or C0 as STCI.

Later on the same date the nonreduced lane was also independently audited
and excluded. Its separate tree enumeration and Type-D ideal proof are in
`2026-10-07-session-normal-nonreduced-independent-audit.md`. The present
note is retained as the proof of the reduced/irreducible stage.

The independent numerical implementation is
`computations/verify_session_normal_independent_audit.py`, with output
`scratch/session_normal_independent_audit.json`. It does not import the
first normal-carrier companion. It independently constructs every ADE
root matrix, verifies the allowed correction columns and full column
denominators, enumerates the budgeted multisets, and scans every reduced
cycle with a marked passage vertex. It reproduced exactly the five rows
in the proposed note.

## 1. Source and inherited hypotheses

The audit refreshed [Ishii--Nakayama's primary preprint](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1370.pdf). It explicitly
uses the minimal resolution and an effective exceptional anticanonical
divisor; its classification includes the rational B1/B2/B3/D cases used
in the note. Proposition 1.1 supplies connectedness when the resolution
is rational. These source inputs, the existing exclusions of rational
and positive-genus ruled carriers, the checked C0 normal bundle, Jaffe's
smooth curve--ADE table, and the rational-resolution denominator
compression theorem remain explicit dependencies. This audit does not
claim to reprove the source classifications.

The geometric arguments below are new direct checks. The exact numerical
scan checks consequences of those arguments and the stated source table,
rather than using numerical agreement to certify the geometric inputs.

## 2. Smooth passage through an exceptional fibre

The passage lemma is valid even on a smooth resolution that has singular
exceptional prime curves or intersections that are not simple normal
crossings. The rational lift of a smooth curve C to the resolution
extends over each missing point by properness and the DVR valuative
criterion. It is a section of the base change over C, so its image c is
isomorphic to C as a closed subscheme.

At its unique point over a surface singularity p, every f in m_(S,p)
pulls back to a function vanishing on every exceptional prime over p.
The regular local ring of the resolution is factorial. The product of
the distinct local prime equations therefore divides the pullback.
After restriction to c, its order is at least the sum of the local
intersection lengths with these primes. The quotient map O_(S,p)->O_(C,p)
is onto and supplies an f restricting to a uniformizer. Thus the sum is
at most one. It is positive because the lift lies in the exceptional
fibre, and consequently equals one.

Each nonzero intersection length is integral and positive. The sole
prime met is smooth at that point, because a singular plane-curve germ
on a smooth surface has multiplicity at least two and cannot have
intersection length one with a smooth curve. The passage is transverse
and avoids every other exceptional prime. Hence the passage vector
really is a standard basis vector, rather than an arbitrary nonnegative
vector. No transversality hypothesis was inserted into the numerical
enumeration.

For the minimal rational resolution, the coefficient-zero exceptional
primes have arithmetic genus zero, square -2, and are disjoint from the
support of E. This follows from adjunction and relative nefness of K.
Connectedness of E and of each exceptional fibre therefore identify one
nonrational fibre with the full support of E; the other fibres are ADE.
The prior avoidance exclusion forces C through the nonrational fibre.

## 3. Passage arithmetic and irreducible support

Let A be minus the full exceptional intersection matrix, a its
anticanonical coefficient vector, and m the smooth passage vector.
Set z=A^(-1)m, t=a^T*m, q=m^T*A^(-1)*m, d=a^T*A*a.
Adjunction gives c^2=t-2. The mate relation gives c+Z numerically H
with square four and exceptional orthogonality, so t+q=6.
Cauchy--Schwarz in the positive definite A form gives

    t^2 <= d*(6-t).

The integer candidates are t<=2 for d=1,2 and t<=3 for d=3.
The equality cases (d,t)=(1,2),(3,3) force z=2a,a respectively.
Their denominator is one; the already checked global compression theorem
would give a plane mate, impossible for C0. Thus the retained t ranges
are exactly the ones stated in the proposed note.

If E=aP has irreducible support, d=a^2*(-P^2)<=3 forces a=1.
Adjunction gives arithmetic genus one for P. The passage lemma gives
t=1, even when P is a singular rational prime curve. Its correction is
P/d, contributing 1/d. The required ADE correction is 5-1/d and its
available rank is at most 8+d.

The new order-two lower bound at the nonrational hypersurface point is
valid in characteristic zero. Straighten C to the t axis. Common
first-normal order one would give a quadratic term t*(a*x+b*y)+Q(x,y)
with (a,b) nonzero; this quadratic form has rank at least two. Formal
splitting gives a node, or uv+h(w). Isolation forces h nonzero; a
one-variable change makes it a power, giving a rational A_n point.
This contradicts nonrationality. Therefore at most seven normal zeros
remain for ADE points.

Every allowed ADE pair satisfies q_i<=n_i*s_i/(n_i+s_i).
Summed Cauchy--Schwarz gives q_ADE<=N*P/(N+P). With
N<=8+d,P<=7 the exact gaps against 5-1/d are 1/16,13/34,7/18
for d=1,2,3. All are positive. This excludes every irreducible E,
including irreducible singular genus-one divisors.

## 4. Reduced support and independent enumeration

When E is reduced and connected with at least two components,
adjunction says that each component's total intersection with the
others is 2-2*p_a. Connectedness makes this positive, so every
component has arithmetic genus zero and is a smooth rational curve.
The resulting connected degree-two intersection multigraph is a cycle:
two vertices have an intersection of two, or at least three vertices
have the usual cyclic edges of weight one. Coincident intersection
points and tangencies are allowed by this matrix argument. The passage
lemma ensures that the marked smooth curve never passes through them.

Minimality gives each diagonal b_i>=2. The reduced coefficient vector
and E^2=-d give sum(b_i-2)=d. The rank bound is k<=9+d.
Thus weak compositions of d into k entries generate all permitted cycle
matrices. Their positive definiteness follows by adding a nonzero
nonnegative diagonal correction to the positive semidefinite cycle
Laplacian. Connectedness makes its constant-vector kernel disappear.

The independent checker built 1033 ADE multisets under total root rank
at most eleven and total first-normal order at most seven. It computes
the allowed A,D,E corrections and indices from complete inverse root
columns, including spin indices in odd D_n. For each cycle it checks all
marked columns and all applicable smaller rank budgets. It finds exactly:

| d | Diagonals starting at the marked prime | q_irr | ADE multiset | Full correction denominator |
|---:|---|---:|---|---:|
| 1 | (2,3) | 3/2 | seven A1 | 2 |
| 1 | (2,3) | 3/2 | five A1 and A3 at its middle vertex | 2 |
| 1 | (2,2,3,2) | 2 | six A1 | 2 |
| 2 | (2,2,4,2) | 3/2 | seven A1 | 2 |
| 3 | (2,2,5,2) | 4/3 | six A1 and A2 at an end vertex | 6 |

The first four denominators give actual degree-two mates by rational
resolution compression and are excluded by the fixed C0 quadric
argument. Full column denominators were used: the denominator of q_irr
alone would give an incorrect index in some marked cycle columns.

## 5. The remaining row and normal-sheaf defect

The final row spends all seven available ADE normal orders. Together
with the nonrational point's lower bound two, this uses the total normal
order nine, forcing e=0. The available global normal-sheaf defect is
deg N_(C/S)-(C#)^2=7-4=3.

Each of its six A1 passages contributes 1/2. The A2 contribution 1/3
is checked directly. On xy=z^3 with C=(x,z), the ordinary point blowup
is smooth. The y chart has y=t,z=t*u,x=t^2*u^3 and pulled-back ideal
(t*u). The z chart has x=z*X,y=z*Y,z=X*Y and ideal (X*Y). Therefore
the ideal exceptional coefficients are both one. The numerical inverse
column has coefficient 2/3 at the end met by the strict curve, so the
normal-sheaf defect there is 1-2/3=1/3. The source smooth A2 pair
classification identifies the two symmetric ends; no additional pair
was omitted.

The ideal-principalization comparison makes all other point
contributions nonnegative, independently of normality at all support
points in its more general theorem. Here the carrier is normal. Hence
the row would require

    3 >= 6/2+1/3=10/3,

which is impossible. This completes the independent audit of the reduced
exceptional exclusion.

## 6. Validation and remaining hypothesis boundary

The independent scan returned exactly five configurations with degrees
2,2,2,2,6. Reproduction:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python research/computations/verify_session_normal_independent_audit.py
```

The finite calculation does not prove existence of any configuration;
over-enumeration is harmless for these exclusions. The result retains
the source characteristic-zero classification and the previously proved
global rational-resolution compression as dependencies. It gives no
classification or exclusion of reducible nonreduced E, whose multiplicity
vector requires a separate graph and discrepancy analysis.


---

## Source: 2026-10-07-session-normal-global-adversarial.md

# Global adversarial audit of the normal-quartic carrier exclusion

Date: 2026-10-07. Status: **ACCEPTED under the recorded classification,
ADE-pair and prior small-mate exclusion inputs**. This audit found no
gap in the global geometry of the normal-quartic argument. It does not
replace the two independent numerical enumerations by a third run.

The audited statement is precisely:

> Over every algebraically closed field of characteristic zero, an
> integral normal quartic surface containing the fixed smooth curve
> C0=[s^4:s^3t:st^3:t^4] cannot participate in a set-theoretic
> complete-intersection presentation of C0, in any mate degree.

This statement does not say that C0 is not a set-theoretic complete
intersection. Nonnormal quartics, higher carrier degrees and the
entirely-thick branches retain their separate unresolved status.

The central proof is
`2026-10-06-session-normal-carrier-progress.md`; the numerical proof
audits are `2026-10-07-session-normal-carrier-independent-audit.md`
and `2026-10-07-session-normal-nonreduced-independent-audit.md`.
The present audit reread those notes, the normal-resolution compression
proof, the earlier normal-quartic classification reduction and the
normal-sheaf defect proof. It refreshed the published primary source.

## 1. Coverage of the surface classification

The [published Ishii–Nakayama paper](https://www.jstage.jst.go.jp/article/jmath1948/56/3/56_3_941/_pdf)
was checked at §1.1, §2.4, the Main Theorem, and §3.3.2–3.4.
The Main Theorem on printed p.955 gives exhaustive constructions.
Rational resolutions have types B1, B2, B3 or D. A possible apparent
exception is the rational ruled case considered during §3.3.2:
printed p.963 explicitly contracts its distinguished section and
identifies its separation with Type D. It supplies no omitted rational
Type-C class. The positive-genus ruled cases have hyperplane degree at
most three on the ruling; the cone case has degree one.

The distinction between a rational singularity and a rational *whole
resolution* is respected. Jaffe's accepted rational-singularity theorem
disposes of the K3/ADE quartics. On a resolution ruled over a
positive-genus curve, any morphism from the rational curve c to the base
is constant. Thus c is a component of a fiber. Nefness of H and its
fiber degree at most three forbid H.c=4, even on a reducible special
fiber. This does not require a mate and does not confuse a rational
component of a fiber with a section over the positive-genus base.

The remaining rational minimal resolutions have K_M linearly equivalent
to -E, with E effective and exceptional, d=-E^2 in {1,2,3}, and
Picard number 10+d. No assumption that E is reduced is introduced.

## 2. The strict curve and the actual passage vector

The rational lift C --> M is defined at the generic point, since a
normal surface is regular at the generic point of C and its singular
locus is finite. Properness of M -> S extends the lift at every point
of the smooth curve by the DVR valuative criterion. The resulting map
is a section of M x_S C -> C. Its image c is a closed embedded copy of
C; the image in M is the strict transform. Consequently c is smooth
rational, and exactly one point of c lies above each point of C.

At a singular point p, every f in m_(S,p) vanishes along every
exceptional prime in its fiber after pullback. In the regular local ring
of M at the point of c, the product of the distinct prime local
equations divides this pullback. Intersection multiplicities with c are
therefore bounded above by the order of f|C. The closed immersion
C -> S makes O_(S,p) -> O_(C,p) surjective, so there is an f whose
restriction is a uniformizer and has order one. The exceptional fiber
is nonempty at that lifted point. Hence the sum of the intersection
lengths is exactly one.

This proves, rather than assumes, that c meets precisely one
exceptional prime transversely at a smooth point away from other
primes. A singular prime germ or a crossing cannot contribute length
one to the required sum. It also proves that the vector m used in
the correction calculation is a standard basis vector at each
singular point. It is not permissible to replace it by an arbitrary
nonnegative vector; the enumerations do not do so.

## 3. Why coefficient-zero exceptional curves do not hide another fiber

For any exceptional prime P on the minimal resolution, let b=-P^2>0.
Adjunction gives K_M.P=b+2p_a(P)-2. This is nonnegative: the only
negative possibility is a smooth rational (-1)-curve, forbidden by
minimality. If the coefficient of P in E is zero, then
K_M.P=-E.P<=0 because distinct effective curves intersect
nonnegatively. Equality follows, forcing b=2 and p_a(P)=0.
Furthermore E.P=0 forces P to be disjoint from every positive
coefficient component of E.

Since E is connected on the rational surface and exceptional fibers
of a proper resolution of a normal surface are connected, its support
is the full exceptional fiber of one nonrational singular point.
Every other fiber consists only of coefficient-zero (-2)-curves and
has zero canonical discrepancy. The accepted Gorenstein surface
classification identifies these fibers with ADE fibers. Thus the
decomposition into one E-fiber and separate ADE fibers is justified;
there is no attached discrepancy-zero curve omitted from the E matrix.

The prior avoidance argument uses the same distinction correctly:
if c avoids E, its square is -2 and its mate correction has square
six; the ADE rank bound then contradicts that correction. Hence a
hypothetical mate forces an actual passage through E.

## 4. Numerical pullback, compression and necessity

An ambient mate of degree b restricts to an effective Cartier divisor
whose full support is C. Because both C and S have degree four, that
divisor is bC. On M its pullback is b*c plus integral exceptional
coefficients. Its intersection with each exceptional prime is zero.
Thus those coefficients are b times the unique numerical correction
Z, and c+Z is numerically equivalent to H.

Write A for minus the full exceptional intersection matrix,
z=A^-1*m, t=c.E and q=m^T*A^-1*m. Adjunction gives c^2=t-2;
orthogonality and H^2=4 give t+q=6. The Cauchy inequality
t^2<=d*q follows in the *full* positive definite matrix, including
the separate ADE blocks and the zero coefficients of E on them.
Equality forces z to be proportional to the coefficient vector of E;
its stated proportionalities are integral, so the plane compression
in the equality cases is valid.

Compression is conditional on the original mate and uses the
rationality of the entire resolution. If n clears every coefficient
of Z, then n(H-c-Z) is an integral numerically trivial divisor on M.
On a smooth projective rational surface numerical equivalence equals
linear equivalence: this holds on a minimal rational surface and is
preserved by each blowup. Pushing a principal divisor down gives
nC linearly equivalent to nH on the normal S. In particular nC is
effective Cartier. Its section lifts to an ambient form by
H^1(P^3,O(n-4))=0. This gives an actual degree-n mate with full
support C, so the accepted small-mate exclusions apply.

This step neither asserts that numerical coincidence constructs a mate
on an arbitrary carrier nor cancels torsion on a nonrational surface.
The use of the *full inverse-column denominator*, including the ADE
blocks, is essential. Extra exceptional fibers not met by c have zero
correction and do not change that denominator.

## 5. The reduced and nonreduced reductions are necessary supersets

For an irreducible E=aP, the integer d=a^2*(-P^2)<=3 forces a=1.
The passage lemma applies even if the arithmetic-genus-one prime is
nodal or cuspidal: c cannot meet its singular point. The nonrational
point uses at least two first-normal orders. Indeed order one would
give a quadratic term x*(a*y+b*z)+Q(y,z) with (a,b) nonzero after
straightening C. Its rank is at least two because the x-axis is
contained in the hypersurface. Formal splitting produces an A_n
isolated singularity, contrary to nonrationality. Thus the stated
ADE budget at most seven is justified without a cusp classification.

For reduced reducible E, component adjunction gives a connected
degree-two intersection multigraph. Arithmetic genus and connectedness
force smooth rational primes and the stated cycle matrices, including
the two-component intersection-two case. Tangencies are not silently
discarded: only the matrix is used, and smooth passage avoids their
intersection points. The independent enumeration eliminates the
necessary cycle/ADE superset. Its last row is excluded by the accepted
normal-sheaf defect formula; the direct A2 chart calculation genuinely
principalizes the curve ideal and gives the contribution 1/3. Together
with six node contributions 1/2, this exceeds the global allowance
three. Further point contributions are nonnegative.

For nonreduced E, each proper effective D<E has
H1(O_D)=H0(O_M(D-E))^*=0 on the rational M. The reduced support is a
proper connected subdivisor, so has arithmetic genus zero. Prime
adjunction and connectedness force a smooth rational SNC tree with
unit intersection edges; a triple meeting would give a triangle and
is impossible. Minimality gives b_i>=2. The equations
A*a=b-2 and d=sum a_i*(b_i-2)<=3 imply total diagonal excess at most
three and at most 9+d vertices. This is the finite necessary graph
space used by both enumerations. No geometric realizability of a
retained graph is assumed. The independently verified surviving
property d=3,t=2 is therefore a legitimate necessary restriction.

## 6. Type D is an ideal calculation, not just a divisor-class prediction

The published source on p.955 provides the Type-D hyperplane basis:
xi0=phi4 and xi1,xi2,xi3=phi3*rho^*(x,y,z), where phi3 defines the
entire divisor E and phi4 defines D. Condition C makes D disjoint
from E. The source identifies its image as p=(1:0:0:0).

Consequently xi0 is a unit near E in a local trivialization of H.
The three affine coordinates of S at p pull back to
(phi3/phi4)*rho^*(x,y,z). The latter coordinate sections have no
common zero on M; locally one is a unit. Therefore the pulled-back
maximal ideal is exactly the invertible ideal O_M(-E), with all
multiplicities retained. This is stronger than equality of reduced
zero sets and is the required conclusion.

Restriction to the embedded smooth c takes the maximal ideal of p to
the order-one maximal ideal of the curve. Restricting O_M(-E) has order
c.E. Thus t=1 for *every* smooth curve through this Type-D point.
The d=3 classification is exhaustive, so this contradicts every
remaining nonreduced graph row t=2. No assumption about the first-normal
Jacobian order of a coefficient-two passage is used.

## 7. Transfer to every algebraically closed characteristic-zero field

Let a hypothetical pair and its normal integral quartic carrier exist
over such a field K. Descend its finitely many coefficients together
with finite radical-equality witnesses to a finitely generated subfield
k0: F and G belong to the fixed ideal of C0, and a positive power of
each generator of that ideal belongs to (F,G). These are polynomial
identities and survive every field extension.

An algebraic closure k0bar embeds into K. Since the carrier becomes
integral and normal over K, faithful-flat descent gives those
properties over k0bar. Thus it is geometrically integral and normal
over k0. The field k0 embeds into C, and that embedding extends to
k0bar. Base changing to C preserves geometric integrality and normality,
as well as the finite radical-equality identities. C0 itself is defined
over Q and remains the same smooth quartic. This produces the forbidden
complex pair.

This argument does not specialize arbitrary parameters, infer a
resolution's rationality after specialization, or impose an
uncountability hypothesis on K. The classification and the analytic
ADE inputs may therefore be used over C and transported by
contradiction. Characteristic p is outside this statement.

## 8. Audit decision and remaining scope

The global implications are accepted with their explicit antecedents:
the primary normal-quartic classification; Jaffe's rational-singularity
and smooth ADE-pair inputs; the audited C0 normal bundle; the prior
mate-degree exclusions through five; the normal-sheaf comparison; and
the two independent finite cycle/tree enumerations. Agreement of
agents or scripts is not substituted for any of these geometric inputs.

The classification coverage, smooth passage, coefficient-zero
separation, denominator compression, Type-D ideal equality and field
transfer each survive the adversarial checks above. No actual gap was
found. The conclusion remains confined to integral normal quartic
carriers of fixed C0 in characteristic zero, with no global STCI or
novelty claim.


---

## Source: 2026-10-07-session-normal-nonreduced-independent-audit.md

# Independent nonreduced-tree and Type-D audit: normal quartic exclusion

Date: 2026-10-07. Status: **ACCEPTED under the stated source and prior
exclusion inputs**. This completes the normal quartic lane for the fixed
characteristic-zero curve C0. It does not exclude nonnormal quartics,
higher-degree minimum carriers, or the entirely-thick branch, and it does
not prove that C0 is not STCI.

## 1. Accepted conclusion and dependencies

Combining the independently audited reduced/irreducible exceptional
exclusions with the argument below gives:

**No integral normal quartic surface in P3 is a carrier of a
set-theoretic complete-intersection presentation of the fixed
C0=[s^4:s^3*t:s*t^3:t^4] in characteristic zero.**

The inherited inputs are: the audited rational and positive-genus ruled
normal-carrier exclusions; the normal-quartic rational-resolution source
classification with d=-E^2 in {1,2,3}, Picard number 10+d, and K=-E;
the rational-resolution numerical-denominator compression theorem;
Jaffe's smooth-curve ADE correction/order/index data; the fixed C0
normal bundle; and the already checked mate exclusions of degrees one
through five on a quartic carrier. None is replaced by agreement between
two numerical scans.

The prior reduced-divisor proof is audited separately in
`2026-10-07-session-normal-carrier-independent-audit.md`. The primary
source for the final geometric step is
[Ishii--Nakayama, section 2.4, printed p.23](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1370.pdf).
That page explicitly supplies the Type-D hyperplane section basis used
below. The source's main theorem and section 3.4 make Type D exhaustive
for the rational d=3 case. Characteristic-zero field transfer remains the
recorded source-spreading input; the local and graph arguments below
themselves are algebraic.

## 2. Why a nonreduced anticanonical support is a rational SNC tree

On the smooth projective rational surface M, take any proper nonzero
effective subdivisor 0<D<E. The exact sequence for D and
H1(O_M)=H2(O_M)=0 give

    H1(O_D)=H2(O_M(-D))=H0(O_M(D-E))^*=0.

The final vanishing follows because E-D is nonzero effective: a section
of its negative ideal is a global regular function on a proper connected
surface vanishing on a nonempty divisor and hence zero. This checks
cohomology, rather than only arithmetic genus.

Every prime in reducible E is a proper subdivisor, so it has arithmetic
genus zero and is smooth rational. For nonreduced E, the connected
reduced support R is also proper; it has H1(O_R)=0 and arithmetic
genus zero. Adjunction and the prime genus equalities imply that the sum
of pairwise intersection lengths equals k-1. A connected graph with k
vertices has at least k-1 edges, each of positive integral intersection
length. Equality forces a tree with every edge of length one. Therefore
all crossings are transverse and no three primes meet at one point,
which would create a triangle. The support is a rational simple normal
crossing tree.

For its intersection matrix A, diagonal entries b_i=-E_i^2 are at least
two by minimality, and edges have A_ij=-1. Its positive integer
coefficient vector a obeys

    A*a=beta,   beta_i=b_i-2>=0,
    d=a^T*A*a=sum a_i*beta_i in {1,2,3},
    k<=9+d<=12,   sum beta_i<=d<=3.                   (T)

There must be a coefficient greater than one, as this is the nonreduced
case. The previous smooth-passage and Cauchy argument permits selected
coefficient t=a_j=1 for d=1, and t=1 or 2 for d=2,3. Its irrational
correction q is the marked diagonal of A^-1. The ADE points on C must
have root rank at most 9+d-k, first-normal order at most seven, and
correction

    q_ADE=6-t-q.

These are all necessary conditions, so numerical over-enumeration cannot
invalidate an exclusion obtained by eliminating the entire allowed set.

## 3. Independent exact enumeration with a different representation

The first companion enumerates free trees by attaching leaves and solves
their matrices by rational Schur elimination. The independent source
`computations/verify_session_nonreduced_independent_audit.py` uses neither
that source nor its output. Its tree and linear-algebra representations
are different:

1. Rooted trees are built recursively as unordered multisets of smaller
   rooted trees. Every rooted tree is covered uniquely by its children's
   multiset. The center or pair of centers gives a canonical free-tree
   code. This produces the free-tree counts
   1,1,2,3,6,11,23,47,106,235,551 for sizes two through twelve.
2. For each tree and every weak diagonal excess of total one, two, or
   three, it computes det(A+xI) as an integer polynomial by matchings.
   A determinant permutation on a tree has only fixed points and
   edge transpositions, yielding

       det(A+xI)=sum_matchings (-1)^|M| *
                    product_unmatched_vertices (b_i+x).

   The recursive matching computation uses no floating arithmetic.
   Because A is symmetric all roots of this polynomial are real.
   Positive definiteness is equivalent to positivity of every
   coefficient: it is necessary when all eigenvalues are positive;
   conversely positive coefficients forbid a root at any x>=0 and
   hence forbid a nonpositive eigenvalue.
3. It computes inverse entries by a tree adjugate identity, not by
   elimination. If P_ij is the unique vertex path from i to j, then

       (A^-1)_ij=det(A with P_ij deleted)/det(A).       (I)

   The deleted matrix is a forest; its determinant is again evaluated
   by integer matchings. For i=j this is the usual principal cofactor.
   For i!=j, expanding the mixed cofactor forces the unique path;
   off-diagonal factors -1 and cofactor signs cancel, and every
   remaining permutation is a matching on the complementary forest.
   This proves (I). The program checks A*a=beta for every retained
   vector and A*z=e_j for every retained correction column.
4. It computes the allowed ADE corrections and full inverse-column
   denominators from the separate independent root-matrix source
   `verify_session_normal_independent_audit.py`. All component multisets
   within the rank/order budget are generated, then compressed only by
   the numerical state (rank,order,q,index). This compression is safe
   because these are exactly the invariants used by the necessary
   conditions. It does not identify distinct geometries as surfaces.

The run checks 381802 diagonal modifications, of which 80845 are positive
definite before the integrality and d filters. It finds 195 weighted
tree canonical cycles satisfying (T), and twelve marked-vertex/ADE
numerical rows after excluding compressed mate degrees at most five.
Every remaining row has

    d=3,   t=2.                                     (S)

There are no surviving d=1, d=2, or d=3,t=1 rows. An initial audit that
kept distinct ADE component names returned nineteen raw rows. This was
a representational multiplicity: quotienting by the four numerical
state invariants gives the twelve rows above. The code now performs that
compression explicitly. The decisive property (S) is independent of the
choice of representative component names.

Saved evidence is `scratch/session_nonreduced_independent_audit.json`.
It retains all 195 graph/cycle records and all surviving marked rows.
The exact assertions check the counts and the d=3,t=2 property. They
do not claim realizability of any numerical graph by a quartic surface.

## 4. Type D forces the incompatible coefficient t=1

The primary source constructs a Type-D resolution by separating a
smooth plane quartic B and an effective plane cubic G with
rho:M->P2. It gives the hyperplane section basis

    xi0=phi4,    xi1=phi3*rho^*x,
    xi2=phi3*rho^*y,    xi3=phi3*rho^*z,

where phi3 defines E and phi4 defines the hyperplane divisor H. The
source also identifies sigma(E) with p=(1:0:0:0). The separation has
H disjoint from E, so xi0=phi4 is a unit along the full E.

On the patch X0!=0 containing p, its maximal ideal is generated by
X1/X0,X2/X0,X3/X0. Their pullbacks are

    (phi3/phi4)*rho^*(x,y,z).

The three plane-coordinate sections generate rho^*O_P2(1) at every
point. In a local trivialization at least one is a unit. Consequently
the pulled-back maximal ideal equals the invertible ideal

    m_p*O_M=O_M(-E)                                  (D)

near E, including its multiplicities. This conclusion checks the ideal,
not merely the common reduced zero set or numerical class H-E.

For any smooth embedded C through p, the ideal m_(S,p) maps onto
m_(C,p). The strict transform c is isomorphic to C, so restriction of
the left side of (D) to c has order one. Restriction of the right side
has order c.E=t. Thus

    t=1                                             (P)

for every such Type-D smooth passage. This applies to reducible or
nonreduced E without requiring an extra simple-normal-crossing model.

The source classifies the rational d=3 surface as Type D. Therefore
every row (S) contradicts (P). The remaining nonreduced normal lane is
excluded. Together with the earlier reduced and inherited normal
exclusions, this proves the stated normal-quartic conclusion for C0.

## 5. Reproduction, checkpoints, and frontier boundary

The independent run completed and passed on 2026-10-07:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python research/computations/verify_session_nonreduced_independent_audit.py
```

The previous parent task of saturating the rank-one fourth-obstruction
Hankel locus was paused for this audit. Its six minors and degree-sixteen
Hankel determinant remain recorded in
`scratch/session_uniform_e2_hankel.json`; no rank-one saturation or
universal e=2 exclusion was proved during this pivot. That quotient
incidence concerns arbitrary quartic carriers and remains meaningful
for nonnormal carriers. It must not be declared closed by the normal
surface theorem.

The conclusion excludes a defined carrier class in every mate degree.
It leaves nonnormal quartics and all higher minimum carrier degrees,
including the entirely-thick global branch, open. The universal STCI
problem and the complete C0 problem remain unresolved.


---

## Source: 2026-10-07-session-ramification-scheme-counterexample.md

# Full inverse support does not force containment of nonreduced ramification

Date: 2026-10-07. Status: **PROVED exact local counterexample**. This
blocks a proposed local extension of the ordinary projected-Veronese
argument. It does not exhibit an STCI presentation of C0, nor assert
that this germ occurs on a semi-log-canonical Veronese projection.

Let k be algebraically closed of characteristic zero and consider

    X: X^2+Y^2(Y+Z^2)=0,
    B=k[w,z],
    nu(w,z)=(X,Y,Z)=(-w^3-wz^2,-w^2-z^2,z).

The map is finite and birational: w satisfies w^2+Y+Z^2=0, and
w=X/Y in the common function field. B is the normalization. Its
conductor is YB, the reduced nodal divisor w^2+z^2=0. Indeed with
A0=k[Y,Z] one has B=A0+ A0 w and A=A0+Y A0 w. Modulo YB the inclusion
is k[z] in k[z,w]/(w^2+z^2). A conductor element must belong to k[z],
and multiplying it by w must again belong to k[z]; freeness over k[z]
forces that element to be zero. Thus the upstairs conductor is exactly
YB, rather than an inferred reduced support.

The coordinate change P=X+iYZ, Q=Y, R=2iZ gives

    P^2+Q^3-PQR=X^2+Y^3+Y^2Z^2.

This is the T_(2,3,infinity) degenerate cusp. It occurs in the strictly
semi-log-canonical list in
[Ducat, Table 1, p.9](https://d-nb.info/1317691679/34).
Equivalently the normalized pair consists of a smooth surface and a
reduced nodal conductor, and the original hypersurface is nodal in
codimension one. The example is not excluded by an slc hypothesis.

## 1. Smooth image and the complete pulled-back curve ideal

Let C be the smooth curve

    X=-2Z^3, Y=-2Z^2,

with parameter Z. Its lift c is w=z. Exact substitution gives

    nu*I_C=(w-z)(w+z,z^2).

The cofactor's support is the origin, already lying on c. Therefore
the entire reduced inverse image is exactly c, with no additional
isolated point and no additional curve. The map c->C is an isomorphism.
This example satisfies both smooth embedded image and full inverse
support, the two hypotheses under examination.

## 2. The actual differential/Fitting ramification scheme

Because dZ=dz, the relative cotangent module is generated by dw with
relations

    (-3w^2-z^2)dw=0, -2w dw=0.

Hence

    Omega_(B/A)=B/(w,z^2) dw,
    I_R=Fitt_0(Omega_(B/A))=(w,z^2).

The same ideal is generated by the two-by-two minors of the three-by-two
derivative matrix of nu. It is a length-two scheme at the singleton
normalization fiber. Its support lies on c, but its full scheme does
not: the equation w-z of c maps to -z, a nonzero element of B/I_R.
Thus **R is not a subscheme of c**.

Scheme-theoretic containment of R cannot be deduced from smoothness of
the image and full inverse support. The no-conic Hilbert-Burch argument
for reduced ordinary pinches therefore does not automatically extend
to nonreduced ramification by replacing support with scheme containment.

## 3. Correct valuation information in this germ

More generally take a lift c_f:w=f(z), with f in z k[[z]] and
f^2+z^2 nonzero. Its image is smooth because Z=z remains a parameter.
Its complete pulled-back ideal is

    (w-f)(w+f,Y_f), Y_f=-(f^2+z^2),

and again its full reduced support is c_f. Write h=ord_z(f), with
h=infinity if f=0, and r=ord_z(f^2+z^2). Then

    length(R intersect c_f)=min(h,2),
    R subset c_f iff h>=2.

The containment condition is an additional tangent condition. Smooth
image and full support permit h=1. Taking f=iz+z^k gives arbitrarily
large r=k+1 while the ramification intersection length remains one.

There is useful information without the false inclusion. Exact
Jacobian substitution gives

    J_X B=(Y) I_R.

For this embedded smooth image, the tangential derivative is a
combination of the two transverse derivatives. Their common vanishing
order is therefore

    s=r+min(h,2).

This valuation identity keeps conductor contact and ramification
intersection separate. It is proved for this local model; it is not
asserted as a general normalization formula without further hypotheses.

The [exact verifier](../computations/verify_session_ramification_counterexample.py)
reconstructs the Fitting ideal from the derivative matrix, the complete
curve preimage, the failed containment, the Jacobian product and the
explicit degenerate-cusp coordinate transformation.


---

## Source: 2026-10-07-session-socle-bridge-adversarial-audit.md

# Independent frame audit of the corrected primitive-e=1 ancestor bridge

Date: 2026-10-07. Scope: the fixed characteristic-zero curve
`C0=[s^4:s^3t:st^3:t^4]`, quartic multipliers, and the stratum
`e=1,D2=0`. Status: **PROVED CONDITIONAL ON THE ACCEPTED ANTECEDENTS**
listed below. The corrected two-target argument passes an independent
geometric audit. The old single-multiplier pole argument does not pass.
This note makes no assertion that C0 is not a set-theoretic complete
intersection or that the whole quartic ancestor incidence is empty.

## 1. Verdict, dependencies, and the rejected implication

Assume the accepted quartic-ancestor finite bound and generic-length
theorem: an ancestor with `F*alpha=u,G*alpha=v` defines a pure finite-flat
CM quadruple `Z`, generically curvilinear, with saturated pieces

```text
E1=L=O(e-7), E2=L^2(D2), E3=L^3(D3).
```

Assume also the audited socle-pencil theorem in Section 2 of
[`2026-10-06-session-localcoh-progress.md`](2026-10-06-session-localcoh-progress.md),
the complete primitive-e=1 triple directions and quartic fibres in
[`2026-10-07-session-mf6-e1-independent-audit.md`](OCT7_MF6_AND_NONNORMAL_STRUCTURES.md#source-2026-10-07-session-mf6-e1-independent-auditmd),
and P-037's all-stage exclusion of multiplier degrees at most three.
The socle theorem gives `E3=O(-14)`. Thus `e=1` means
`L=O(-6),degD3=4`.

Under these antecedents, **there is no common quartic ancestor with
`e=1,D2=0`**. The proof below uses both target equations together.

The earlier proposed bridge used the false implication that a multiplier
containing the canonical triple also vanishes in `OZ`. In fact its image
is a nonzero socle element, because its alpha-image is one of the targets.
Consequently `h*a=T*tau` cannot be used for one multiplier. The valid
equation is `h*a-T*tau=f`, retaining its actual target image `f`.
The single-multiplier cubic pole bound is therefore not an ancestor
obstruction. Its use in an actual complete-intersection quotient is a
different argument, with a different vanishing hypothesis.

## 2. The canonical triple and its actual quotient frame

Since the two targets lie in the first inverse-system socle, the images
of `F,G` in `OZ` lie in the saturated socle `E3`. One may first verify
this generically and then use the torsion-free lower filtration quotients
to extend it to every curve point. Hence both quartics contain

```text
Z3=Spec(OZ/E3).
```

When `D2=0`, multiplication `L^2 -> E2` is an isomorphism. Locally
over a completed smooth support DVR, a normal lift `ell` of a generator
of `L` has square generating `E2`. Nakayama on the three successive
rank-one pieces shows that `1,ell,ell^2` generate the canonical triple.
Its embedded transverse algebra is primitive. No curvilinear assertion
about the quadruple's special fibre is needed.

On `x0=1` the actual ambient normal coordinates are

```text
z=x1, x2=z^3+V, x3=z^4+U+3zV/2.
```

The balanced conormal coordinates satisfy to first order on the opposite
ambient chart

```text
U'=z^-7 U, V'=z^-7 V.
```

For `L=O(-6)`, write its quotient direction `U=A(z)*ell,V=B(z)*ell`
with the classified linear polynomials `A,B`. This is the actual
balanced quotient frame: a linear coefficient multiplies an `O(-6)`
frame to give the `O(-7)` normal coordinate. It is not an arbitrary
formal transverse variable.

For the principal orbit, `A=1+z,B=-2-8z`, use

```text
ell=4U/3+V/6, m=B*U-A*V.
```

On the other chart the Bezout lift is `ell'=-U'/3-V'/6`. Substituting
the quotient values gives `ell'=z^-6*ell` to first order. Likewise
`m'=(-8-2/z)U'-(1+1/z)V'=z^-8*m` to first order.
For either algebraic orbit, `A=r*z,B=1`, use `ell=V,m=U-r*z*V`.
The opposite-chart lift is `ell'=U'/r`, whose quotient value is again
`z^-6*ell`; and `m'=U'/z-r*V'=z^-8*m` to first order.
These identities are checked directly in the independent verifier.

Higher-order changes of a lift of `L` differ by saturated degree at
least two. Cubing them changes `ell^3` only in saturated degree at least
four, which is zero on the quadruple. The moving support coordinate
has its first difference from `1/z` in normal degree one; multiplying
that difference by `ell^3` is again degree at least four. Thus these
nonlinear transitions do not change the global cubic multiplication
map `L^3 -> E3`.

## 3. The target normalization and the global degree-four coefficient

The ancestor induces the isomorphism

```text
E3 -> omega_C(-3)=O(-14).
```

The isomorphism is the accepted socle-pencil theorem, rather than a
choice of a possibly meromorphic socle generator. Choose the regular
finite-chart socle frame `w` by pulling back the standard frame of
`omega_C(-3)` through this isomorphism. After twisting by the ambient
quartic, its target space is

```text
E3(4) -> omega_C(1)=O(2).
```

To verify its scalar coordinates, in the balanced normal frame

```text
q=U+zV/2, B=-z^2U+z^3V/2+V^2.
```

Their first-normal determinant is `z^3`. The restrictions of the raw
target numerators `x0*x2,x1*x3` are `z^3,z^5`; the normalized residue
coefficients are therefore exactly `1,z^2`. The same regular sections
extend at `z=0`: one computes the equality on the dense chart where the
determinant is nonzero, then uses the regular balanced residue frame
and torsion-freeness. The homogeneous pencil is `(s^2,t^2)` and has no
common zero. The raw numerators alone would give an incorrect endpoint
frame.

Multiplication gives a global line-bundle map

```text
L^3=O(-18) -> E3=O(-14).
```

Write `ell^3=tau(z)*w` on the finite chart. Then `tau` is a polynomial
of degree at most four. Explicitly, `ell'=z^-6*ell` modulo irrelevant
higher terms and `w'=z^-14*w`, so
`tau'(1/z)=z^-4*tau(z)`. Regularity at both endpoints gives the degree
bound. This is the crucial geometric constraint on the coefficient;
it cannot be assumed for an arbitrary chosen formal socle frame.

If `F0,F1` are a basis of the complete two-dimensional quartic fibre,
their alpha-images `f0,f1` lie in `span(1,z^2)` and form a basis of that
pencil: the given `F,G` are independent and their images are `u,v`.
Consequently the two images have no common projective zero.
Actual ambient torus normalization preserves this property and this
pencil, since the targets are two torus eigenvectors. Only those actual
torus transformations are used in the orbit classification.

## 4. Correct multiplier identities

In a primitive triple chart choose its regular quadratic correction
`gamma` so that `m+gamma*ell^2=0` in `OZ3`. In the quadruple write

```text
m+gamma*ell^2=a(z)*w, ell^3=tau(z)*w.
```

Both coefficients are regular on that chart. If a quartic's jet is

```text
F=h*m+gamma*h*ell^2+E*m*ell+K*ell^3+higher terms,
T=gamma*E-K,
```

then `m*ell=-gamma*ell^3`: the extra term `a*w*ell` is zero because
`E3` is annihilated by the curve ideal. Terms of saturated degree four
also vanish. Hence its actual image in `E3(4)` is

```text
f=h*a-T*tau.
```

For a basis `F0,F1`, eliminate the unrestricted local coefficient `a`:

```text
h1*f0-h0*f1=(h0*T1-h1*T0)*tau.
```

There is no assumption that either quartic annihilates `OZ`.

## 5. Principal orbit: two finite points contradict the target pencil

Put `P=4z^2+2z+1`. The accepted quartic jets give

```text
h0=P*z^3/16,
h1=P*(64z^6+8z^3+1)/1024,
h0*T1-h1*T0=(2z-1)^3*(2z+1)*P/256.
```

The determinant identity is independently recomputed from the explicit
`T0,T1`. Cancelling the nonzero polynomial `P` from the identity of
regular functions gives

```text
(64z^6+8z^3+1)*f0-64z^3*f1
    =4*(2z-1)^3*(2z+1)*tau.
```

At `z=1/2` it says `3*f0-8*f1=0`; at `z=-1/2` it says
`f0+8*f1=0`. Every section in `span(1,z^2)` has the same value at
these two points in the fixed finite-chart frame. The two linear
equations therefore force both `f0,f1` to vanish at both points.
This contradicts the basepoint-free pencil. Both points are finite,
and `P` is nonzero at them, so no endpoint or denominator issue occurs.

As a redundant stronger algebra check, the complete polynomial
coefficient system with `deg(tau)<=4` has a one-dimensional solution
space. Its target part is

```text
f0=c*(z^2-1/4), f1=(3/8)*f0.
```

It has rank one and cannot be the required target basis. The two-point
proof already supplies the contradiction without this stronger check.

## 6. Algebraic orbits: the global degrees contradict either target basis

For either root `12r^2+4r+3=0`, the accepted complete pencil has

```text
h0=1,T0=0, h1=(2r+2/3)*z^8,T1=(8r/9)*z^3.
```

Both displayed constants are nonzero. The first equation gives
`a=f0`; the second therefore reads

```text
f1=(2r+2/3)*z^8*f0-(8r/9)*z^3*tau.
```

If `f0` is nonzero its first term has degree at least eight, whereas
the second term has degree at most seven and `f1` has degree at most
two. Thus `f0=0`, already contradicting independence of the two target
images. In fact the remaining equation, with a right side divisible
by `z^3` and left side of degree at most two, forces `tau=f1=0` too.
The exact coefficient matrix has rank nine over `Q(sqrt(-2))`, confirming
the zero solution for both geometric conjugates. The degree argument
itself proves the contradiction.

## 7. Quadric-factor orbit and reproducibility

In the fourth orbit `A=-z/2,B=1`, the complete quartic fibre is
`q*H0(P3,O(2))`. Both multiplier equations then make `q*alpha` a common
ancestor with degree-two multipliers. P-037 excludes it. This is the
correct ancestor obstruction for this fibre; the STCI divisor-class
argument on the quadric is not being substituted for it.

The four primitive triple orbits are exhausted, proving the stated
conditional quartic-ancestor exclusion. Positive `D2` makes the
canonical triple defective and remains outside this argument. Other
values of `e`, multiplier degrees beyond four, and the universal STCI
question also remain outside it.

Run the independent exact frame and coefficient checks with

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/computations/audit_session_socle_bridge_frames_2026_10_07.py
```

Its source imports no other research verifier or generated JSON. It
checks the determinant-normalized targets, actual first-order quotient
frames, principal cubic determinant, two-point equations, full principal
coefficient rank and both-conjugate algebraic coefficient rank. The
durable JSON carries the source hash. These exact identities support the
geometric proof above; they do not prove the listed antecedents.


---

## Source: 2026-10-07-session-veronese-pencil-classification.md

# Finite Veronese projections: no quartic mate in any degree

Date: 2026-10-07; strengthened on 2026-10-08. Status: **PROVED HERE,
with independent adversarial audit accepted**. Exact normal-form
and descent identities have passed the
companion verifier. Exhaustiveness is proved by the linear-algebra
argument below, not by a parameter search. No canonical state is edited
by this note, and no novelty claim is made.

The [independent Oct8 audit](OCT8_SCROLL_GORENSTEIN_AND_SINGULAR_AUDITS.md#source-2026-10-08-session-veronese-allmate-independent-auditmd)
checks the classification, full inverse support, exceptional fibers,
global constant multiplier and arbitrary-degree first conductor jet.

## Statement and scope

Let k be algebraically closed of characteristic zero. Let nu:P2->X be
a finite birational morphism onto an integral quartic in P3, with
nu*O_X(1)=O_P2(2). If C is a smooth rational curve of degree four on X,
there is **no homogeneous form G of any positive degree b** such that
X intersect V(G) has set-theoretic support C.

This excludes every quartic carrier with this normalization and
polarization, including its non-slc degenerations. It does not classify
all nonnormal quartics and does not extend to singular normalizations.
No novelty claim is made. The earlier slc consequence survives as a
subsidiary classification: if X has ordinary double crossings in
codimension one, it is projectively equivalent to the Roman surface.

Semi-log-canonical varieties require ordinary normal crossings in
codimension one; see
[Fujino, Fundamental theorems for semi log canonical pairs, Definition 2.3](https://www.math.kyoto-u.ac.jp/~fujino/fund-slc5.pdf).
Only this necessary condition is used to reject the Jordan cases.

## 1. Precise tensor and pencil convention

Let V=k^3. The quadratic Veronese is [v]->[v v^T] in P(Sym^2 V)=P5.
A quadratic form q(v)=v^T Q v is a covector on Sym^2 V by the pairing
trace(P Q). Off-diagonal coefficients of the symmetric matrix Q are
half the coefficients of the corresponding cross terms of q.

The four independent quadratic sections defining nu span a
four-dimensional space W of covectors. Its annihilator L=W^perp is
two-dimensional in Sym^2 V. The projection center is the line P(L).
Choose a basis of L and write its symmetric matrix pencil M(s,t)=sA+tB.
Basepoint freeness says that P(L) misses the Veronese: **no nonzero pencil
member has rank one**. Rank-one symmetric matrices over k are precisely
the nonzero scalar multiples of v v^T. The finite normalization is
basepoint free, so this condition holds here.

Changing coordinates of P2 acts on the center matrices by congruence.
Changing the pencil basis makes a linear substitution in (s,t).
Changing the basis of W is an ambient projective coordinate change.
We keep all three permitted operations explicit below.

## 2. The regular pencil: self-adjoint Jordan possibilities

Suppose some pencil member A is invertible. The operator T=A^(-1)B
is self-adjoint for the nondegenerate symmetric form g with matrix A.
Generalized eigenspaces for distinct eigenvalues are orthogonal and
nondegenerate. Indeed the relatively prime powers of (T-lambda) and
(T-mu) give the orthogonality by self-adjointness; the direct-sum
decomposition and nondegeneracy of g give nondegeneracy on each summand.

There are only the Jordan partitions of a three-dimensional space.
If T is diagonalizable, choose an orthogonal eigenbasis and scale its
vectors to obtain A=I and B diagonal. If two eigenvalues coincide,
B-lambda A has rank one, unless B=lambda A makes L one-dimensional.
Both possibilities are forbidden. Therefore the diagonalizable case
has three distinct eigenvalues.

In this case W contains the three cross quadrics xy,xz,yz. Its remaining
diagonal quadric has coefficients proportional to

    (lambda2-lambda3, lambda3-lambda1, lambda1-lambda2).

Every coefficient is nonzero. Rescaling the three source coordinates
by square roots and rescaling the ambient basis gives exactly

    [x:y:z] -> [yz:zx:xy:x^2+y^2+z^2],

the standard Roman normalization.

For a Jordan block of size two, choose v with Nv=e, where N is the
nilpotent part. Then g(e,e)=0 and g(e,v)!=0. Scale the chain and replace
v by v-g(v,v)e/(2g(e,v)) to make its Gram matrix the antidiagonal
two-by-two matrix. The one-dimensional distinct-eigenvalue summand can
be scaled to Gram value one. If its eigenvalue equals that of the
Jordan block, B-lambda A has rank one and is forbidden. If the eigenvalues
are distinct, a pencil basis change moves them to zero and one. Swapping
the two chain coordinates if needed gives the following center matrices.
If that pencil change rescales the nonzero nilpotent coefficient, a
chain congruence diag(c,c^(-1)) preserves the antidiagonal Gram matrix
and removes that coefficient using a square root in k:

    A2=[[0,1,0],[1,0,0],[0,0,1]],
    B2=[[1,0,0],[0,0,0],[0,0,1]].

Their annihilator is spanned by

    q2=[y^2,xz,yz,z^2-xy-x^2].

For a single Jordan block of size three, put e0=N^2v,e1=Nv,e2=v.
Self-adjointness gives

    g(e0,e0)=g(e0,e1)=0,
    g(e0,e2)=g(e1,e1)=gamma!=0.

The nonzero gamma follows from nondegeneracy: otherwise e0 would be
orthogonal to the whole space. Write delta=g(e1,e2), epsilon=g(e2,e2).
Replacing v by v+a Nv+b N^2v changes delta to delta+2a gamma and epsilon
to epsilon+2a delta+(a^2+2b)gamma. Choose a,b to kill both and rescale
gamma to one. Thus the Gram matrix is the antidiagonal three-by-three
matrix, while T is the single Jordan block. Subtracting its eigenvalue
times A from B gives

    A3=[[0,0,1],[0,1,0],[1,0,0]],
    B3=[[0,0,0],[0,0,1],[0,1,0]].

The annihilator is spanned by

    q3=[x^2,xy,z^2,y^2-xz].

These are all regular-pencil cases. The chain changes just supplied
prove the small-dimensional self-adjoint normal forms directly.

## 3. Jordan size two: a doubled conductor

The q2 forms have no common zero: y=0 from y^2, then xz=0, and
z^2-x^2 excludes either coordinate vertex. Therefore their map is finite.
On y z!=0 its coordinates recover x/y=b/c and z/y=c/a, so it is
birational. Substitution gives the irreducible image equation

    F2=c^4-a d c^2-a^2bc-a^2b^2=0.

It is primitive linear in d, hence irreducible. The line Gamma:a=c=0
is singular. At its generic point take b=1 and d=D, with coefficient
field k(D). The transverse equation has lowest homogeneous part -a^2.
An ordinary node has a quadratic initial form with two distinct lines
after algebraic closure of the coefficient field. A square initial
form cannot become such a node. Thus this image fails the necessary
codimension-one normal-crossing condition for slc.

One can see the conductor multiplicity directly. Put a=eta c^2+...
in the transverse equation. The first coefficient is

    1-D eta-eta^2=0.

At the generic point its two roots are distinct, since D^2+4!=0.
Hensel expansion gives two smooth branches a=f_+(c),a=f_-(c), whose
difference has order two. The completed curve ring over the algebraic
closure of k(D) sits in k(D)^alg[[c]]^2 as pairs congruent modulo
c^2. Its normalization conductor is c^2 on each branch. Equivalently
the upstairs conductor has generic multiplicity two on y=0.

This is not a nonordinary isolated point with a reduced generic
conductor: the whole generic double curve is non-slc.

## 4. Jordan size three: a tripled conductor

The q3 forms have no common zero: x=0 leaves z^2 and y^2. On x!=0
they recover y/x=b/a and z/x=(b/a)^2-d/a, so the map is finite and
birational. The irreducible image equation is

    F3=(b^2-a d)^2-a^3 c=0,

primitive linear in c. Its singular line Gamma:a=b=0 has, on c=1,d=D,
transverse initial form D^2a^2, again a square at the generic point.
It is not an ordinary double crossing.

For its conductor, expand

    a=b^2/D+epsilon b^3+... .

The first nontrivial coefficient is

    D^2 epsilon^2-D^(-3)=0.

The two roots are distinct and nonzero generically. The two smooth
branches have difference of order three in b. Their normalization
conductor is b^3 on each branch; upstairs it has generic multiplicity
three on x=0. Hence this image is also non-slc along a curve.

The pair-congruence conductor calculation used in these two cases is
elementary: for two graph branches a=f_+(b),a=f_-(b), the image of the
quotient by their product in the direct sum of the two branch rings
consists of pairs whose difference belongs to (f_+-f_-). Its conductor
on either branch is that ideal. Higher-order coefficients do not change
the exponents two and three found above.

The full upstairs conductor divisors in these coordinates are

    D2=2{y=0}+{z=0},        D3=3{x=0}.                       (4.1)

Here is also a global check of the multiplicities. A quartic hypersurface
has omega_X=O_X. Finite duality identifies Hom_X(nu_*O_P2,O_X)
with nu_*omega_P2, so the conductor upstairs is the invertible ideal
O_P2(-3). The Hom module is indeed the conductor: in the common
function field an O_X-linear map is multiplication by a rational
function h, and its image lies in O_X precisely when h O_P2 lies
in O_X. The finite-duality input is recorded in
[Stacks, finite morphisms](https://stacks.math.columbia.edu/tag/0FKW)
and [normalized finite-map duality](https://stacks.math.columbia.edu/tag/0A7M),
Lemma 47.16.1. The inverse in section 3 is an isomorphism away from
y z=0, whose images are lines; both those lines have generically
two normalization preimages. The multiplicity two on y=0 leaves
multiplicity one on z=0 because the total degree is three.
Section 4's inverse is an isomorphism away from x=0, so its
single conductor support has multiplicity three. The no-mate
arguments below require only the first conductor jet of D3.

## 5. Every-member-singular pencil: direct Kronecker reduction

Now assume det M(s,t) is identically zero. Every nonzero member has
rank exactly two by the center condition. The adjugate is a nonzero
rank-one symmetric matrix of homogeneous quadratic polynomials.
Over the UFD k[s,t], it can be written

    adj M=h(s,t) v(s,t) v(s,t)^T,

where the entries of v are homogeneous of a common degree r and have
no common polynomial factor, and h is polynomial of degree 2-2r.
For completeness, start with a nonzero column, divide its entry gcd
to obtain v, and use rank one to express all columns as polynomial
multiples of v. The multiples are polynomial because a denominator
would divide every entry of primitive v. Symmetry makes the multiplier
row proportional to v, and the same denominator argument makes the
factor h polynomial.

The adjugate never vanishes at a point of P1, since rank M is always two.
Therefore h is nowhere zero, hence has degree zero. It follows that
r=1. The two coefficient vectors of v are independent; otherwise its
entries would share a linear factor. A source coordinate change gives
v=(s,t,0). Write M=sA+tB. The identity Mv=0 gives

    Ae1=0, Be2=0, Ae2=-Be1.

Symmetry forces

    M=[[0,0,-kappa t],[0,0,kappa s],
       [-kappa t,kappa s,alpha s+beta t]],

with kappa!=0, since otherwise its rank would be at most one. Rescale
kappa to one, then replace the third basis vector by itself plus
(beta/2)e1-(alpha/2)e2. This removes the lower diagonal entry.
Permuting coordinates gives the Kronecker pencil

    [[0,s,t],[s,0,0],[t,0,0]].

Its annihilator is [x^2,y^2,yz,z^2]. The image lies on the quadric
bd-c^2=0 and the map has generic degree two, via x->-x. It is not
birational onto a quartic and cannot be the normalization under study.
The reduction therefore has no omitted singular-pencil stratum.

## 6. A mate would pull back to a power of one conic

The three birational quartic types above have singular loci supported
on lines, as follows directly from their equations or inverses. A smooth
integral degree-four curve C cannot be contained in such a locus. Thus
nu is an isomorphism at the generic point of C. Its inverse image has
one reduced curve component c mapping finitely and birationally to C.
Because C is normal, this finite birational map is an isomorphism:
locally a finite ring between O_C and its fraction field is O_C.

If a mate G exists, nu*G is a nonzero section of O_P2(2b). Its zero
set is the full inverse image of C. A principal divisor on the smooth
surface P2 has no isolated components. Hence the full reduced inverse
image is c, with no additional isolated points. Every normalization
fiber over C is a singleton, because c->C is an isomorphism. Write
div(nu*G)=m c. The degree of nu*O_C(1)=O_P2(2)|c equals four, so c
has plane degree two. Comparing degrees then gives m=b. In homogeneous
coordinates this means

    nu*G = constant * f^b,

where f is the irreducible quadratic equation of the smooth conic c.
This is a full-support assertion, not just a statement about the
strict transform of C. It is what permits the following fiber and
descent tests.

## 7. Roman type: the six allowed points cannot lie on a conic

For [yz:zx:xy:x^2+y^2+z^2], each coordinate axis maps two-to-one to
a conductor line. The only singleton fibers on these axes are

    [0:1:+/-1], [1:0:+/-1], [1:+/-1:0].

The three coordinate vertices have a common image and cannot belong
to c. At each listed point, the derivative in the axis direction
vanishes and the derivative normal to the axis is nonzero. Since the
embedded image C is smooth, c must meet each axis transversely there.
Consequently its two intersections with each axis are that axis's
two listed points. A conic would have to contain all six.

For a quadratic form A x^2+B y^2+C z^2+D xy+E xz+F yz, evaluation
at these six points gives D=E=F=0 and A+B=A+C=B+C=0. In
characteristic zero all six coefficients vanish. This contradicts
the nonzero equation f. This also reproduces the
[independent Roman argument](OCT7_MF6_AND_NONNORMAL_STRUCTURES.md#source-2026-10-07-session-nonnormal-structural-progressmd).

## 8. Jordan size two: only one allowed point on one conductor line

Use the q2 coordinates fixed in section 2. On the line z=0 and the
chart y=1, writing r=x/y, the projection is

    r -> [1:0:0:-r-r^2].

Its fiber involution is r->-1-r; the only finite singleton is
p=[-1/2:1:0]. The point at infinity [1:0:0] has the same image
[0:0:0:1] as [0:0:1], so its full normalization fiber is not a
singleton either. The mate's full support therefore forces
c intersect {z=0} to have support only p.

Near p, put y=1, x=-1/2+v. In the a=1 target chart the map becomes

    (v,z) -> ((-1/2+v)z, z, z^2+1/4-v^2).

Its derivative at p depends only on the z derivative. Smoothness of
the embedded image C forces z to be a local parameter on c, hence
the intersection with z=0 is transverse and has multiplicity one.
But a conic not containing that line has total intersection degree
two. There is no other allowed point and no second multiplicity at p.
This excludes the Jordan-size-two carrier in every mate degree,
without a semi-log-canonical assumption.

## 9. Jordan size three: the first conductor jet forbids a conic power

For q3=[x^2:xy:z^2:y^2-xz], the line x=0 maps by
[y:z]->[z^2:y^2]. Its only singleton fibers are
p=[0:0:1] and q=[0:1:0]. At p the z=1 affine map is

    (x,y) -> (x^2, xy, y^2-x),

whose differential is nonzero only in the x direction. At q, use
y=1 and the target chart d=1-xz: the derivative of b/d=x/(1-xz)
is nonzero only in the x direction; the other two chart coordinates
have zero differential. Smoothness of C again forces transverse
intersection of c with x=0 at either point. Degree two and the
singleton fiber condition therefore force c to pass through both.

It follows that the homogeneous equation of c has the form

    f=alpha x^2+beta xy+gamma xz+delta yz, with delta!=0.       (9.1)

Indeed the coefficients of y^2 and z^2 vanish at q and p, and
delta=0 would make f divisible by x, contradicting irreducibility.
On z=1 put B=k[x,y], and let

    A=k[x^2,xy,y^2-x] subset B

be the affine target ring. The mate's pullback is a nonzero constant
multiple of f^b and must belong to A. We show it cannot, using only
the first infinitesimal neighborhood of the generic conductor line.

In the ring R=k(y)[x]/(x^2), define the involution

    iota(x)=-x, iota(y)=-y+x/y.                              (9.2)

Substitution gives iota^2=identity and fixes x^2,xy,y^2-x modulo
x^2. Thus the image of every element of A in R is iota-invariant.
For (9.1) on z=1,

    f = delta y+x(beta y+gamma)                    modulo x^2,
    iota(f) = -delta y+x(delta/y+beta y-gamma)      modulo x^2.

Comparing the constant term of f^b and iota(f)^b forces b even,
since delta!=0 and the characteristic is zero. For positive even b,
comparison of the x coefficients gives

    b(delta y)^(b-1) * (2 beta y+delta/y)=0 in k(y).

The prefactor is nonzero. Therefore 2 beta y^2+delta would vanish
identically, forcing beta=delta=0. This contradicts delta!=0.
No power f^b descends, so this carrier also has no mate in any degree.

This uses an actual conductor jet; the reduced fiber condition alone
would allow the conic through p and q. It does not assert that an
arbitrary ramification scheme lies on c. Characteristic zero is
essential here: when the exponent is divisible by the positive
characteristic, the displayed derivative comparison loses its force.

## 10. Conclusion and continuation boundary

The pencil classification exhausts all finite birational quartic maps
from (P2,O(2)). The Roman and Jordan-size-two cases are excluded by
the full normalization fibers and smooth conic intersections. The
Jordan-size-three case additionally uses the first conductor jet.
Thus all three cases are excluded in every mate degree. The independent
audit linked above accepts the complete scope and proof.

The subsidiary slc classification remains valid: its only possible
type is Roman, because the Jordan cases have nonreduced conductors
**generically**. The stronger no-mate proof does not rely on slc.
It does not repair the false general R subset c implication:
the [local slc counterexample](#source-2026-10-07-session-ramification-scheme-counterexamplemd)
still stands for other normalized surfaces. Other nonnormal quartic
classes and singular normalizations remain outside this theorem.

The [exact verifier](../computations/verify_session_veronese_pencils.py)
checks the tensor annihilator convention, canonical center determinants,
image equations and dense rational inverses, generic square tangent
cones, conductor branch-separation exponents, singleton-fiber and
transversality controls, and the first-jet involution and coefficient
obstruction. Exhaustiveness and
the no-mate deduction are the arguments above, not consequences of a
PASS line alone.


---

## Source: 2026-10-07-session-veronese-singular-pencil.md

# Singular centers of Veronese projections: an exact classification

Status: **PROVED HERE**, independently of a classification citation. The proof
works over every algebraically closed field, including characteristic two.
This note concerns the singular-pencil stratum of projection centers. It does
not classify centers whose determinant polynomial is nonzero.

Let the Veronese surface in projective five-space be represented by rank-one
symmetric matrices `vv^T`, with coordinates
`[x^2:xy:y^2:xz:yz:z^2]`. A projection to projective three-space has a line as
its center. A basepoint-free projection has a center disjoint from the
Veronese surface, so that no nonzero matrix in its two-dimensional matrix
space has rank one.

Suppose the center is a symmetric pencil `M(s,t)=sA+tB` whose determinant
vanishes identically. Every member then has rank exactly two. The matrices
`A,B` are linearly independent, because they span a line in projective space.

## 1. The kernel map has degree one

Work in the unique factorization domain `R=k[s,t]`. Choose a nonzero column of
the adjugate matrix and divide its entries by their homogeneous greatest
common divisor. The resulting kernel vector `v` is primitive and homogeneous,
with all nonzero entries of the same degree `e`. Since the pencil has rank two
over the fraction field, every column of its adjugate is a rational multiple
of `v`. Such a multiple is polynomial: the denominator of a rational scalar
in lowest terms would divide every component of `v`, contradicting
primitivity. Thus `adj(M)=v p^T` for a polynomial vector `p`.

The adjugate is symmetric. Its symmetry gives `v_i p_j=v_j p_i`, so `p` is
a rational scalar multiple of `v`; the same primitive-vector argument makes
that scalar polynomial. Consequently

`adj(M)=h(s,t) v(s,t) v(s,t)^T`.

The entries of the adjugate have degree two, hence `deg(h)=2-2e`.
Primitivity of a homogeneous vector over `k[s,t]` means that its entries have
no common zero in projective one-space: a common zero would supply a common
linear factor. Since every member has rank two, the adjugate is nonzero at
every point of projective one-space. Therefore the homogeneous polynomial
`h` has no projective zero. Algebraic closedness forces `h` to be a nonzero
constant. It follows that `e=1`.

Write `v=s u+t w`. The vectors `u,w` are linearly independent, for otherwise
all entries of `v` would have a common linear factor. A constant change of
basis puts the kernel vector in the form `(s,t,0)^T`.

## 2. The complete matrix normal form

The identity `M(s,t)(s,t,0)^T=0` gives

`A e_1=0`, `B e_2=0`, and `A e_2+B e_1=0`.

Symmetry then forces

`M(s,t)=[[0,0,-b*t],[0,0,b*s],[-b*t,b*s,c*s+d*t]]`.

Here `b` is nonzero: otherwise every member would have rank at most one.
Rescaling and reparametrizing the pencil yields the normal form

`M(s,t)=[[0,0,t],[0,0,s],[t,s,alpha*s+beta*t]]`.                 (1)

This form is valid in every characteristic. In characteristic different
from two, replacing the third basis vector by itself plus a suitable linear
combination of the first two removes `alpha,beta`. Thus the usual singular
Kronecker pencil is the only congruence class in that characteristic.
In characteristic two the displayed diagonal terms need not be removable;
no assertion of a single congruence class is being made there.

For reference, the adjugate of (1) is

`-[s,-t,0]^T [s,-t,0]`,

and a nonzero `(s,t)` gives rank two. Both identities remain valid in
characteristic two, with the usual interpretation of the minus signs.

## 3. The projection has degree two and a quadric image

The line (1) in the six ambient Veronese coordinates is

`[0:0:0:t:s:alpha*s+beta*t]`.

Its four-dimensional annihilator therefore gives the projection

`[x:y:z] -> [x^2:xy:y^2:z^2-beta*x*z-alpha*y*z]`.              (2)

This map is basepoint-free. Its first three coordinates can vanish
simultaneously only when `x=y=0`, in which case the fourth is `z^2 != 0`.
The image satisfies the quadric equation `ac=b^2` in coordinates
`[a:b:c:d]`.

On `x != 0`, put `u=y/x` and `v=z/x`. Formula (2) becomes

`[1:u:u^2:w]`, where `w=v^2-(beta+alpha*u)*v`.

The induced extension `k(u,w) subset k(u,v)` has degree two. Indeed
`T^2-(beta+alpha*u)*T-w` is irreducible over `k(u,w)`: in
`k(u)[T,w]` it is linear and monic up to sign in `w`, its quotient is the
domain `k(u)[T]`, and Gauss's lemma applies when it is regarded as a primitive
polynomial over `k(u)[w]`. Thus the image is the entire quadric surface and
the generic degree is two.

The morphism is finite. The pullback of the hyperplane line bundle is
`O_P2(2)`, an ample line bundle, so no curve can be contracted. Alternatively,
the affine formula above is a monic quadratic finite map, and the analogous
`y != 0` chart together with the single preimage of the quadric vertex covers
all fibers.

In characteristic different from two, completing the square in the fourth
coordinate and adding a linear combination of the first three coordinates
reduces (2) to `[x^2:xy:y^2:z^2]`. In characteristic two, (2) is generically
separable if `(alpha,beta) != (0,0)`, and purely inseparable of degree two
otherwise. The image has degree two in either case.

**Consequence.** A basepoint-free projection of the Veronese surface whose
center is an identically singular symmetric pencil cannot have an integral
quartic surface as its image, and cannot realize the normalization map of
such a quartic surface. This disposes of the entire singular-pencil stratum;
it is not an argument about nonsingular determinant pencils.

## Reproduction

`research/computations/verify_session_veronese_singular_pencil.py` checks the
generic symbolic adjugate, the rank-two minors, the annihilator coordinates,
the target quadric equation, and the coordinate change in characteristic
different from two. The degree and exhaustiveness arguments above are
mathematical proofs, not consequences of a sampling computation.
