# Quadric powers, normal directions and incidence controls

Consolidated research material, including open questions and source assessments.

---

<a id="2026-10-05-foundational-frontier-audit"></a>

## Foundational theorem interfaces and source qualifications

The complete [complement-morphism theorem P-029](global_equations_and_constructions.md#p-029-complement-morphisms-and-two-generated-positive-line-bundles), [graded Gorenstein criterion P-035](global_equations_and_constructions.md#p-035-arithmetically-gorenstein-thickening-criterion), and [ordinary/symbolic power theorem on a smooth quadric](../normal-geometry/formal-normal-intersection.md#12-ordinary-ideal-powers-on-a-smooth-quadric-complete-proof) retain their proofs in the focused Arguments. The distinctions below are essential when applying them.

### Complement morphisms and global ACMness

P-029 uses an **integral codimension-two** curve, positivity of the degree of a nonconstant map to \(\mathbf P^1\), and a generating homogeneous pencil; the equal-degree regular-sequence graph has equation \(uG-vF=0\). A reducible support requires additional componentwise arguments.

P-035 requires **arithmetically Gorenstein**, hence Cohen–Macaulay, homogeneous coordinate algebra. The last free module in the Hilbert–Burch resolution has rank \(\mu(J)-1\), giving the canonical-module type. For an lci projective thickening, subcanonicality alone is insufficient: the Rao-module vanishing \(H^1(\mathbf P^3,\mathcal I_X(n))=0\) for every \(n\) is separate.

The smooth-quadric theorem uses a local colon identity and homogeneous lifting by binary monomial products, plus saturation to rule out an embedded vertex prime. Sheaf exactness alone does not establish equality of saturated homogeneous powers. The [finite M2 checks](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_quadric_powers.m2) corroborate, but do not replace, its all-order proof.

### Positive-characteristic carrier scope

The separate [positive-characteristic constructions](../arithmetic/arithmetic_equations_and_jet_gaps.md) and [fixed cone analysis](../arithmetic/arithmetic_equations_and_jet_gaps.md) treat the specified smooth rational quartics and cuspidal carriers, **not** arbitrary projective curves. Their projection argument retains the degree-three separable/characteristic-three inseparable distinction, the characteristic-two ramification case, and the characteristic-three cusp coefficient. The normalization and semigroup descent are characteristic-sensitive; no characteristic-zero specialization follows.

For the explicit quartic cone \(V(x_0x_3^3-x_2^4)\), the full set of mate degrees \(N\) has the following minimum and divisibility:
 
| Characteristic | Necessary and sufficient condition | Minimum |
| --- | --- | --- |
| \(2\) | \(4\mid N\) | \(4\) |
| \(3\) | \(3\mid N\) | \(3\) |
| \(5\) | \(25\mid N\) | \(25\) |
| \(p\ge7\) | \(p\mid N\) | \(p\) |
| \(0\) | no mate | — |

The finite birational normalization \(\mathbf P(1,1,4)\to V(x_0x_3^3-x_2^4)\) sends \([s:t:z]\mapsto[s^4:z:st^3:t^4]\), with inverse support \(z-s^3t=0\). Every degree-\(N\) mate pulls back to a scalar multiple of \((z-s^3t)^N\). By Lucas's theorem, descent is equivalent to the smallest positive base-\(p\) digit exponent \(p^{v_p(N)}\) belonging to the semigroup \(\langle3,4\rangle\); this includes arbitrary non-binomial mates. The characteristic-zero exclusion overlaps the one-binomial-carrier theorem.

### Precise source limitation: ACM-to-STCI

[Robbiano–Valla (1983)](https://doi.org/10.1007/BF02924906), §4, fixes a **monomial** parametrization before its ACM-to-STCI proposition. This inspected proof does not justify an attribution for every ACM space curve. [D'Cruz, Theorem 2.7](https://arxiv.org/html/2003.09101v1), states the broader implication and cites Robbiano–Valla and Stückrad–Vogel; the latter original proof has not been checked here. The broader assertion is **not disproved**, but should be cited with its source qualification. No argument above depends on it.

The unrestricted characteristic-zero rational-quartic STCI problem remains open. Neither finite power checks, positive-characteristic descent, nor a local Gorenstein thickening supplies the missing global homogeneous pair.

---

<a id="2026-10-05-literature-new-routes"></a>

## Literature refresh and a uniform quadric-curve power algebra

Date: 2026-10-05. This note is independent of the shared ledgers. It records
source scopes, a newly reconstructed uniform lemma, reproducible checks, and
the limits of the resulting route. No unrestricted STCI conclusion is claimed.

### 1. Literature status and genuinely stronger existing exclusions

#### General problem and the Macaulay quartic

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

#### Mandal--Zinna: version and affine scope checked again

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

#### Thoma's ONE-binomial-carrier theorem

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

A useful limitation: torus degeneration does not extend this theorem to
arbitrary carriers. A flat limit of a complete-intersection thickening need
not remain a two-generated complete intersection; extra initial generators
and/or common factors of the two initial forms can appear. Properness of a
Hilbert scheme does not make its complete-intersection locus proper.

#### The broad ACM assertion deserves source-level qualification

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

#### A recent discrepancy invariant does not solve this support problem

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

### 2. Uniform theorem for integral curves on a smooth quadric

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

#### Proof with the lifting step made explicit

The [complete proof](../normal-geometry/formal-normal-intersection.md#12-ordinary-ideal-powers-on-a-smooth-quadric-complete-proof)
establishes the colon identity locally and proves that the restriction
sequence

    0 -> script-I^(m-1)(d-2) --q--> script-I^m(d)
      -> O_Q(d-am,d-bm) -> 0                         (1)

is surjective on global sections by lifts in the ordinary power \(I^m\).
For \(d\ge bm\) these lifts use products of degree-\(b\) equations
\(T_0,\ldots,T_{b-a}\) of \(C\) and ambient degree-\((d-bm)\) forms.
The \(T_i\) lift a basis of \(H^0(Q,\mathcal O_Q(b-a,0))\) multiplied by
the Cartier section defining \(C\). For \(d<bm\) the quotient has
no sections. The ruling-line case has the same ordinary and symbolic
power equality because its ideal is generated by two linear forms.

#### Literature connection

Morales--Simis, *Symbolic powers of monomial curves in P3 lying on a quadric
surface*, Communications in Algebra 20 (1992), 1109--1121,
DOI <https://doi.org/10.1080/00927879208824394>, treats the monomial quadric
case. A later original article explicitly recalls its Proposition 2.3 as
normal torsion-freeness for a monomial curve on xy-wz:
<https://citeseerx.ist.psu.edu/document?doi=7e63dd655dbc886de78bc22d6d0b3229da3ec6f0&repid=rep1&type=pdf>.
The author publication list verifies the earlier paper:
<https://www-fourier.univ-grenoble-alpes.fr/~morales/publications-web-Marcel-Morales2014.pdf>.
The exact uniform scope of the 1992 proof was not read in full, so this note
labels its general statement as proved by the linked argument, with
classical overlap explicitly acknowledged.

### 3. Consequences usable at arbitrary normal order

#### Exact carrier lower bound and recursive spanning

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

#### Exact Hilbert function

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

### 4. Exact computation and reproducibility

The companion M2 script `research/computations/verify_quadric_powers.m2` checks C0 powers
m=1,...,6 over QQ and the formula (4) over a range of degrees. It also checks
the analogous (1,4) monomial quintic and a nonmonomial (2,4) quadric divisor.
The finite computations check consistency with the linked proof.

For C0 the observed Betti totals of S/I^m are

    (1, (m+1)^2, 2m(m+1), m^2).

Thus ordinary and symbolic powers coincide while the quotients remain
non-Cohen--Macaulay. Finite generation alone cannot invoke a height-two
projective STCI theorem: the local Cowsik dimension-three result changes its
equation count in dimension four, and stronger CM-symbolic-power criteria
need additional hypotheses that these powers fail.

### 5. Research reassessment

The new structural information removes one source of uncertainty from
arbitrary-order normal calculations and can reduce high-order carrier spaces
to concrete q/product data. It is a useful uniform algebra, not a global
obstruction. The strongest additional literature restriction is that both
carriers for C0 must be nonbinomial in characteristic zero. A new investigation
should use these facts to formulate pair-dependent higher-jet or valuation
conditions, rather than expect finite generation, a torus limit, or a
reduced-discrepancy invariant to settle the problem.


---

<a id="2026-10-06-localcoh-incidence"></a>

## Exact finite quartic incidence specification and recovered direction certificate

The characteristic-zero fixed quartic \(C_0\) has an exact finite incidence model. The fixed-direction exclusion below does not settle the full quartic incidence or unrestricted STCI; the separate parity-family argument gives a stronger direction classification.

### 1. Reproduced coordinates

For S=QQ[x,y,z,w], put q=xw-yz, A=x²z-y³, B=xz²-y²w,
C=yw²-z³ and I=(q,A,B,C). The existing finite-principal-part argument reduces
quartic ancestors to E4[-7], where E4=Ext²(S/I⁴,S), of dimension30. The exact
injection into Ext²(S/(q⁴,B⁴),S) represents these sections by 30 homogeneous
degree13 numerators, modulo (q⁴,B⁴).

The exact [tensor exporter](../../computations/localcoh-incidence-tensor.m2) and its associated basis output fix the coordinate conventions used below.

The quartic basis has18 elements. Its products with the30 ancestors span the
entire74-dimensional E3[-3] piece. Appending the two target numerators
xz(qB)³ and yw(qB)³ does not enlarge that span. These are exact rational rank
computations, not samples.

A degree17 remainder in the fixed quotient initially gives277 occurring
ambient monomials. Exact row-space compression gives74 equations and a
74×542 rational matrix R. Its first540 columns are products. Column18i+j
is the product of ancestor i with quartic j, for i=0,...,29 and j=0,...,17.
The last two columns are precisely the standard vectors e72,e73, using
zero-based row indices. These coordinate conventions are checked by the
Oct6 Python verifier.

### 2. The complete finite incidence, including its open rank conditions

For a=(a0,...,a29), define the74×18 linear matrix

    L(a)[r,j] = sum_i R[r,18i+j] ai.

The complete finite quartic problem is exactly the affine incidence

    L(a) f = e72,     L(a) g = e73,

in30 ancestor coordinates and two18-coordinate multiplier vectors. This is
148 bilinear equations in66 variables, including two nonzero constant
right sides. Consequently a=0 is automatically excluded; no extra
saturation is needed merely to remove the zero ancestor. The basis of E4
already imposes the I⁴-annihilator/support condition, unlike searching all
of the diagonal Cech quotient.

Write N(a) for the first72 rows of L(a), and P(a) for its final two rows.
Existence of f,g is equivalent to

    P(a): ker N(a) -> QQ² being surjective,

or, equivalently,

    rank L(a) = rank N(a) + 2.

Thus rank N(a)≤16 is necessary. The exact projective constructible locus in
P29 is the union of the strata r=0,...,16 with

    rank N(a)=r,     rank L(a)=r+2.

Each stratum requires all (r+1)-minors of N to vanish, some r-minor of N
nonzero, and some (r+2)-minor of L nonzero. For r=0 the nonzero0-minor
condition is vacuous. Discarding these open conditions produces a larger
closed locus and cannot by itself settle incidence. In particular, a
vanishing-minor computation on N alone is not a full incidence exclusion.

Scaling a by a nonzero scalar is absorbed by reciprocal scaling of f,g,
so this specification is naturally projective in the ancestor. Every
solution is ambient-coprime by the separately established low-degree
ancestor exclusion; coprimality is not assumed in the matrix encoding.

### 3. Recovered polynomial dual for a surviving pure-top direction

Use the balanced normal frame and divided-power top-symbol coordinates
c_i[t^j] with i=0,...,3 and j=0,...,7. The checked top map M has shape32×30,
rank29 and a one-dimensional kernel, represented by

    k4=1/4,   k13=-3/4,   k18=1,

with all other k_i zero. These are zero-based coordinates.

Consider the primitive degree2 normal-dual direction

    nu=(1+t²,-2t),

whose homogeneous pair (s²+t²,-2st) is coprime. Its pure cubic symbol with
coefficient h=1 is in the top image. Its coefficient h=t is outside the
image: the augmented top matrix has rank30. Hence this direction admits
exactly a one-dimensional nonzero top-coefficient space. Normalize that
coefficient to1. Every ancestor with this top symbol is then

    a(c)=a*+c k,

where the nonzero entries of a* are

    a0=8/3, a3=-4/3, a8=12, a9=-8, a14=8/3,
    a17=8/3, a27=12, a28=2, a29=1.

Let L0=L(a*) and L1=L(k). The recovered rational vectors n0,n1 of length74
are stored in `localcoh-incidence-2026-10-06-certificate.json`. They satisfy

    n0^T L0 = 0,
    n0^T L1 + n1^T L0 = 0,
    n1^T L1 = 0,

and

    n0^T e72=1, n1^T e72=0,
    n0^T e73=8/11, n1^T e73=0.

Thus n(c)=n0+c n1 satisfies, identically over QQ[c],

    n(c)^T L(a(c))=0,
    n(c)^T e72=1,    n(c)^T e73=8/11.

Neither target lies in the quartic multiplication image for any value of c,
even over an algebraic closure. This excludes every quartic multiplier for
this entire ancestor line. A nonzero scalar multiple of the top symbol
reduces to the same line by scaling the ancestor and multipliers, so the
exclusion holds for all nonzero top coefficients for this fixed direction.

The verifier `../computations/localcoh-incidence-2026-10-06.py` checks these
identities using Python's standard library and exact rational arithmetic;
it needs no Groebner computation. It also checks hashes, basis-coordinate
agreement with the top map, the unique top line, and the two target columns.
The original discovery used two small one-target Groebner computations,
which returned the unit ideal. The saved dual is a directly checkable
certificate of that result.

### 4. Certificate scope and multiplication convention

In Macaulay2, `basis(4,I)` uses the four ideal-generator coordinates: the first row alone is **not** a quartic form. Correct multiplication sums all four generator products. Using only the first row yields degree-14 or degree-15 expressions whose degree-17 coefficient tests vanish vacuously. The tensor exporter uses the correct sum, and its exact rational certificate excludes the specified fixed non-ruling degree-two direction. The full 148-equation incidence and the other low-degree directions remain unresolved; an interrupted Gröbner attempt is not evidence of exclusion.
