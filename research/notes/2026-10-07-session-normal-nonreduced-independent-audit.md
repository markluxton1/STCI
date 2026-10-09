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
