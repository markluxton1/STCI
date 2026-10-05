# Literature refresh and a uniform quadric-curve power algebra

Date: 2026-10-05. This note is independent of the shared ledgers. It records
source scopes, a newly reconstructed uniform lemma, reproducible checks, and
the limits of the resulting route. No unrestricted STCI conclusion is claimed.

## 1. Literature status and genuinely stronger existing exclusions

### General problem and the Macaulay quartic

The checked primary sources still retain the general connected/integral
projective-space-curve problem and the characteristic-zero Macaulay quartic
as open. In particular, Takumi Murayama's 2026 MA665 notes explicitly retain
the Macaulay curve as an open example:
<https://www.math.purdue.edu/~murayama/ma665.pdf>.
The intended parametrization is the usual quartic; the repeated final `s^4`
in the displayed four-dimensional linear system is a typographical error.
The 2019 Hartshorne--Polini primary paper remains useful for its actual
coregularity criteria:
<https://arxiv.org/html/1907.05472v1>.
A search on 2026-10-05 found no subsequent unrestricted resolution. This is
a dated search conclusion, not a proof of absence of unindexed work.

### Mandal--Zinna: version and affine scope checked again

<https://arxiv.org/abs/2511.07589> still lists only v1, submitted 2025-11-10,
and no journal reference. Its abstract asserts a broad theorem for lci
height-two ideals in rings of dimension three. It is distinct from the
published conditional theorem in Journal of Algebra 690 (2026), 101--113,
DOI <https://doi.org/10.1016/j.jalgebra.2025.10.042>.
The published result requires an affine algebra over a characteristic-zero
C1 field, free conormal module, and torsion Grothendieck-group class; its
ring-level variant assumes freeness of stably free rank-three modules.
Neither theorem controls projective infinity, and the homogeneous coordinate
ring has dimension four. No projective transfer is inferred.

### Thoma's ONE-binomial-carrier theorem

A stronger classical exclusion than the ledger's two-binomial-equation
warning is available. Apostolos Thoma, *Monomial Space Curves in P3_k as
Binomial Set Theoretic Complete Intersections*, Proceedings AMS 107 (1989),
55--61, DOI <https://doi.org/10.1090/S0002-9939-1989-0976361-7>, Theorem 3.1,
proves in characteristic zero that a smooth monomial space curve other than
the twisted cubic cannot be an STCI on any binomial carrier. Here the mate
is allowed to be an arbitrary homogeneous polynomial. Thus BOTH carriers of
any characteristic-zero pair for C0 must be nonbinomial.

The original article, uploaded by its author, was checked at
<https://www.researchgate.net/publication/303334542_Monomial_space_curves_in_as_binomial_set_theoretic_complete_intersections>;
its institutional record is
<https://olympias.lib.uoi.gr/jspui/handle/123456789/13047>.
The official AMS PDF returned HTTP 403 through the browsing tool, so the
original author-uploaded theorem is the checked full-text evidence.

A useful limitation: torus degeneration does not promote this theorem to
arbitrary carriers. A flat limit of a complete-intersection thickening need
not remain a two-generated complete intersection; extra initial generators
and/or common factors of the two initial forms can appear. Properness of a
Hilbert scheme does not make its complete-intersection locus proper.

### The broad ACM assertion deserves source-level qualification

Clare D'Cruz, arXiv:2003.09101v1, Theorem 2.7 literally states the broad ACM
space-curve assertion used by the repository:
<https://arxiv.org/html/2003.09101v1>.
Thoma's 1993 primary preprint also lists the assertion, but in a discussion
restricted to monomial curves:
<https://archive.mpim-bonn.mpg.de/948/1/preprint_1993_86.pdf>.
The original Robbiano--Valla chapter was not accessible in full through the
publisher. Thoma's 1989 original introduction explicitly attributes to them
ACM **monomial** space curves. These facts do not disprove the broader
statement, but the original-proof scope has not been reconstructed in this
lane. The safe record is that a modern survey states it, while the original
monomial source chain is narrower. None of the mathematics below uses the
broad assertion.

### A recent discrepancy invariant does not solve this support problem

Bengus-Lasnier--Rangachev, *The Complete Intersection Discrepancy of a Curve I:
Numerical Invariants*, arXiv:2504.09362v1:
<https://arxiv.org/html/2504.09362v1>.
Its residual-intersection formulas assume a containing complete intersection
Z that agrees with X at the generic points of X. That hypothesis is exactly
what fails for a nontrivial STCI thickening. For smooth C the local intrinsic
discrepancy vanishes already, while a nonreduced CI supported on C may still
have arbitrary generic multiplicity. Therefore the new invariant should not
be imported as an obstruction to STCI support without a new nonreduced
extension. The existing formulas are useful for residual curves, not an
unconditional way around the thick-carrier frontier.

## 2. Uniform theorem for integral curves on a smooth quadric

**PROVED HERE; independent adversarial proof audit completed.** No novelty
claim is made. The monomial special case is classical in Morales--Simis
(1992), and the uniform geometric argument below is particularly convenient
for nonmonomial and singular integral curves.

Let k be algebraically closed, of arbitrary characteristic. Let
Q = V_+(q) be a smooth quadric in P3, identified with P1 x P1, and let C be an
integral divisor of class (a,b), with 1 <= a <= b. Let I be its saturated
homogeneous prime ideal. Then, for every m >= 1,

    I^m = (I^m)^sat = I^(m).

In particular the symbolic Rees algebra is the ordinary, finitely generated
Rees algebra. Smoothness of C is unnecessary: an integral divisor on the
smooth surface Q is Cartier, and its embedding in P3 is locally a complete
intersection away from the affine-cone vertex.

### Proof with the lifting step made explicit

Write script-I for the ideal sheaf of C. For every m and d there is a sheaf
exact sequence

    0 -> script-I^(m-1)(d-2) --q--> script-I^m(d)
      -> O_Q(d-am,d-bm) -> 0.                         (1)

At a point of C choose local equations (q,t), where t defines C in Q.
The identities `(q,t)^m:q=(q,t)^(m-1)` and
`(q,t)^m mod q=(t^m)` prove (1), including its kernel. Away from C the same
sequence is immediate.

At m=1,d=b, the quotient is O_Q(b-a,0). Since H1(P3,O(b-2))=0,
degree-b forms in I lift its full section space. Choose lifts
T_0,...,T_(b-a) of a monomial basis of H0(O_Q(b-a,0)).
Their m-fold products span H0(O_Q(m(b-a),0)) in every characteristic.
There is no division by a characteristic-dependent binomial coefficient.

For d<bm the right-hand term of (1) has no global sections. For d>=bm put
n=d-bm. Ambient degree-n forms surject onto H0(O_Q(n,n)), and monomial
multiplication gives the surjection

    H0(O_Q(m(b-a),0)) tensor H0(O_Q(n,n))
        -> H0(O_Q(d-am,d-bm)).                         (2)

Consequently every section of the quotient in (1) has an explicit lift in
the ORDINARY power I^m. This matters: sheaf exactness alone would not prove
surjectivity on global sections.

Inductively suppose all sections of script-I^(m-1)(d-2) lie in the ordinary
power. Subtract the lift just constructed from a section of script-I^m(d).
The difference is q times a section of the preceding sheaf power, hence
belongs to I^m. Starting with m=0 proves
H0(script-I^m(d))=(I^m)_d in every degree, which is precisely saturation.

Off the cone vertex, I is a prime lci ideal. Its associated graded ring is
locally a polynomial algebra over the domain S/I, so its powers are locally
I-primary. All possible embedded associated primes are therefore supported
at the vertex. Saturation excludes that associated prime. Thus I^m is
I-primary, and localization at I gives the symbolic-power equality.

The ruling-line case (a=0 or b=0) is separately a two-linear-form complete
intersection and also has the equality. The proof above is for a,b>0.

### Literature connection

Morales--Simis, *Symbolic powers of monomial curves in P3 lying on a quadric
surface*, Communications in Algebra 20 (1992), 1109--1121,
DOI <https://doi.org/10.1080/00927879208824394>, treats the monomial quadric
case. A later original article explicitly recalls its Proposition 2.3 as
normal torsion-freeness for a monomial curve on xy-wz:
<https://citeseerx.ist.psu.edu/document?doi=7e63dd655dbc886de78bc22d6d0b3229da3ec6f0&repid=rep1&type=pdf>.
The author publication list verifies the earlier paper:
<https://www-fourier.univ-grenoble-alpes.fr/~morales/publications-web-Marcel-Morales2014.pdf>.
The exact uniform scope of the 1992 proof was not read in full, so this note
labels its general statement as proved by the displayed argument, with
classical overlap explicitly acknowledged.

## 3. Consequences usable at arbitrary normal order

### Exact carrier lower bound and recursive spanning

If F vanishes to normal order at least m along C and is not divisible by q,
then deg F >= bm. At equality, F restricted to Q is a linear combination of
m-fold products of the chosen T_i, modulo q I^(m-1).
Every form of arbitrary normal order is described recursively by these
products and q times the preceding power. For the rational quartic a=1,b=3,
this extends the repository's degree-six symbolic-square picture uniformly
to every normal order; there are no additional hidden symbolic generators.

The theorem says nothing about termination of the infinitely-near common
zero set of a pair. In particular, it does not repair a tangent-only blowup
recurrence. Positive-characteristic pairs remain mandatory controls.

### Exact Hilbert function

Surjectivity in (1) gives, with binomial and product terms interpreted as zero
when their required degrees are negative,

    dim (I^m)_d = binom(d-2m+3,3)
       + sum(j=1..m) h0(O_Q(d-2m+(2-a)j,
                           d-2m+(2-b)j)).             (3)

For C0 this becomes

    dim (I^m)_d = binom(d-2m+3,3)
       + sum(1<=j<=m, 2m+j<=d)
           (d-2m+j+1)(d-2m-j+1).                    (4)

The first non-q-divisible degree is 3m, and the corresponding quotient has
dimension 2m+1. In particular m=2 gives the known 23-dimensional sextic
space, with 18-dimensional q-divisible kernel and five-dimensional quotient.

## 4. Exact computation and reproducibility

The companion M2 script `research/computations/verify_quadric_powers.m2` checks C0 powers
m=1,...,6 over QQ and the formula (4) over a range of degrees. It also checks
the analogous (1,4) monomial quintic and a nonmonomial (2,4) quadric divisor.
The finite computations are consistency checks; the theorem is the argument
above, rather than an extrapolation from those checks.

For C0 the observed Betti totals of S/I^m are

    (1, (m+1)^2, 2m(m+1), m^2).

Thus ordinary and symbolic powers coincide while the quotients remain
non-Cohen--Macaulay. Finite generation alone cannot invoke a height-two
projective STCI theorem: the local Cowsik dimension-three result changes its
equation count in dimension four, and stronger CM-symbolic-power criteria
need additional hypotheses that these powers fail.

## 5. Research reassessment

The new structural information removes one source of uncertainty from
arbitrary-order normal calculations and can reduce high-order carrier spaces
to concrete q/product data. It is a useful uniform algebra, not a global
obstruction. The strongest additional literature restriction is that both
carriers for C0 must be nonbinomial in characteristic zero. A new investigation
should use these facts to formulate pair-dependent higher-jet or valuation
conditions, rather than expect finite generation, a torus limit, or a
reduced-discrepancy invariant to settle the problem.
