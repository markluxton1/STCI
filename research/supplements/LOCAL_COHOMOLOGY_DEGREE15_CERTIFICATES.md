# Complete rational endpoint ancestor exclusions

For the fixed characteristic-zero quartic, primitive degree-two normal-dual directions and pure cubic top h=t, both specified rational endpoint families fail target-u quartic-ancestor incidence for every admissible direction and every affine lower correction. This conclusion uses the accepted actual tensor and coordinate interpretation, not arbitrary formal multipliers. It does not cover p(0)=0 boundary families, nonendpoint top zeros or arbitrary-degree mates.

The first family initially has exceptional factors of degrees 2,4,4,13; exact polynomial duals over the full quotient fields close all 23 geometric roots. The second has exceptional degrees 2,2,3,4,15; the quadratic, cubic, quartic and degree-fifteen identities close all 26 geometric roots. In each case the rank-29 top map shows that the affine correction line is the entire lower-lift fiber; all 18 actual multiplier columns are annihilated identically, with target coordinate one. The projective zero-top stratum is a separate inherited boundary, not a missing affine parameter.

The shared mechanism is a certificate in the cokernel of the actual multiplication morphism. The finite list of exceptional factors is a coverage argument; a normalized left dual at each whole factor closes its full parameter fiber. Generic rank or one successful sample would not establish either assertion.

## Degree-fifteen stratum

This is the completed certificate for the finite degree-fifteen exception stratum of one rational endpoint family. The earlier preparation did not itself exclude the stratum; the original-tensor polynomial dual below does. The result and necessary exact support are presented before the reusable construction.

<a id="2026-10-14-localcoh-degree15-fractionfree-certificate"></a>

## Exact result and scope

**Exact family exclusion, verified in the original tensor.** In the accepted second rational
endpoint family of the quartic-ancestor local-cohomology incidence, every root
of

\[
\begin{aligned}
f_{15}(k)={}&243k^{15}+810k^{14}+2646k^{13}+990k^{12}-9465k^{11}
-54222k^{10}-114414k^9-166406k^8\\
&-34359k^7+301686k^6+897946k^5+1296458k^4
+1345117k^3+811630k^2+285598k-610
\end{aligned}
\]

has no affine lower lift satisfying the actual tensor incidence. The new
certificate is a polynomial vector \(n(k,\lambda)\) with 74 coordinates,
reduced modulo the **entire** polynomial \(f_{15}\), satisfying

\[
 n^T L_{\rm actual}(k,\lambda)=0,\qquad n_{72}=1.
\]

The generated vector actually has degree at most **one** in \(\lambda\).
The inherited general corank-one construction allows degree two. These
identities exclude the target for every affine \(\lambda\), including at all
fifteen algebraic roots; this is not root sampling or a numerical rank test.

The accepted cubic and quartic field certificates are premises and were not
rerun. Combining their seven roots with this new certificate removes all
22 finite exception roots in this specific second rational family. This
statement does not enlarge the accepted quartic-ancestor incidence to
arbitrary carriers, change the other family's scope, or resolve the universal
STCI question. The established projective lower-lift boundary remains an
inherited separate premise.

## Direct original-tensor verification

The retained [normalized dual certificate](../computations/general-localcoh-family2-degree15-corank-one-2026-10-14-attempt06-certificate.json) stores the 74 polynomial coordinates over \(\mathbb Q[k]/(f_{15})\). The [independent verifier](../computations/general_localcoh_family2_degree15_corank_one_certificate_2026_10_14.py) reconstructs the actual 74-by-18 matrix from the retained tensor and rational-family seed. Using standard-library `Fraction` arithmetic, it checks every coefficient of all 18 column identities, the parameter-degree bound and coordinate 72 equal to one. The final identities are sufficient evidence for this exclusion; construction inverses and auxiliary duals are unnecessary premises.

The certificate is bound to the actual tensor, its coordinate bases, top map and second-family seed. Those inputs retain the accepted geometric interpretation and the completeness of the affine lower-lift fiber. The identity check uses the entire quotient polynomial, so it covers every root and every affine lower parameter without numerical sampling. It does not establish the inherited tensor interpretation or the separate projective boundary anew.

Run from the repository root:

```sh
python3 -B research/computations/general_localcoh_family2_degree15_corank_one_certificate_2026_10_14.py --verify --stem general-localcoh-family2-degree15-corank-one-2026-10-14-attempt06
```

The check closes the fifteen-root stratum. Together with the cubic and quartic certificates it closes their combined 22-root exception set; the complete second-family coverage additionally includes the separate quadratic factors and boundary premises described below. Its scope remains the specified ancestor incidence.

## A reusable corank-one dual construction

The complete general construction, including observability, degree-two duals and the companion sharpness example, is owned by [the local-cohomology dual lemma](POLYNOMIAL_DUALS_AND_AFFINE_PENCILS.md). The formulas below give its degree-fifteen specialization.

<a id="2026-10-14-localcoh-degree15-single-block-strategy"></a>

Let the exact pencil be L_can=(lambda*I_18+A;B), where B is 56 by 18 of rank 17. Choose row set I and column set J of size 17, with missing column l. Embed M^-1=B[I,J]^-1 into an 18 by 56 matrix D, and set E=e_l^T, h=(I_18-DB)e_l. The identities

    MM^-1=M^-1M=I_17,  h_l=1,  Bh=0,  DB=I_18-hE

prove rank 17 over the intended quotient algebra. They make no appeal to modular samples. Any row r with rh=0 has the exact lift rDB=r. If a=Ah and (h,a) has an invertible 2-by-2 minor, choose rows F_h,F_a dual to h,a. Then D_0=(I-hF_h)D satisfies D_0B=I-hF_h. This supplies all required transpose lifts by multiplication. Sixteen linear duals and one quadratic dual test target compatibility; their annihilation identities must be checked coefficient by coefficient in the full quotient. If target evaluations generate the unit ideal in the parameter ring, a Bezout combination gives n^TL=0,n^TU=1. A failed denominator or nonunit minor preserves a stratum; it is not an exclusion.

This is a linear-algebraic separation mechanism: the target defines a class in coker L; a normalized annihilator proves that class is nonzero. Parameter-polynomial identities exclude entire families, while pointwise ranks exclude only the points actually checked. The accepted tensor's geometric interpretation, completeness of the affine lower-lift fiber, and the separate projective boundary remain necessary upstream premises.

## Optional polynomial scaling

<a id="2026-10-14-localcoh-polynomial-scaling-design"></a>

For rational polynomial matrices B whose seed denominators are constants times powers of k-1 and k+1, integer row and column exponents can be chosen so their sums dominate each entry's pole order. Diagonal matrices D,E then give a polynomial matrix P=DBE; negative column exponents are allowed only after exact polynomial cancellation is checked. An exact inverse transports as B^-1=EP^-1D. A minimum-weight exponent cover can reduce determinant scaling degree. In this source matrix it reduces 306 to 152 (77 at k=1,75 at k=-1), with 150 nonzero entries and maximal degree 21. These are representation bounds, not an invertibility claim. A constant two-entry row permits one additional column subtraction and pivot, again without proving the remaining determinant nonzero. The [exact scaling script](../computations/general_localcoh_degree15_polynomial_scaling_design_2026_10_14.py) and [polynomial factors](../validation/2026-10-14-localcoh-degree15-polynomial-scaling-design/selected-block-scaled-polynomials.json) retain the optional construction.

## First rational family: full parameter and exceptional-field coverage

<a id="source-2026-10-08-session-first-endpoint-completeness-auditmd"></a>

The following complete coverage argument was independently reconstructed against the actual tensor in the inherited source state. Its exact coefficient comparisons are supported by [countercheck.py](../validation/2026-10-08-first-endpoint-audit/countercheck.py), which independently binds all four exceptional-field seeds and affine slopes to the rational family. The source interpretation remains an audited premise.

## 2. Precisely which parameters are covered

Write the normalized direction as

```text
p(t)=1+a1*t+a2*t^2,   r(t)=1+b1*t+b2*t^2,
a1=(k^2+3)/(2(1-k^2)),
a2=-(k^2+2k+3)/(2(k+1)^2),
b1=(k-3)(k^2+2k+3)/((k-1)^2(k+1)),
b2=-2(k^2-4k+5)(k^2+2k+3)^2/((k-1)^3(k+1)^3).
```

The parameter chart is `k!=1,-1`. The fixed-degree homogeneous quadratic
resultant is

```text
8*(k^2+2k+3)^2*(9k^4-21k^3+5k^2-31k+134)
 /((k-1)^6*(k+1)^6).
```

Thus an admissible parameter also avoids the roots of
`qk=k^2+2k+3` and `B=9k^4-21k^3+5k^2-31k+134`. Using a four-by-four
Sylvester determinant matters: a dehomogenized resultant alone could
miss a common root at infinity when a leading coefficient vanishes.
The existing geometric audit and all exceptional-field checkers use
the fixed-size homogeneous determinant.

The rational classification covers the normalized finite directions.
On `2a1+1!=0` its inverse is

```text
k=(32a2+16a1^2+12)/(4(2a1+1)^2).
```

Modulo the top-image equation, this recovers both `a1` and `a2`, and
`k^2-1=-4/(2a1+1)`. The only omitted normalization point at
`2a1+1=0`, equivalently the limit `k=infinity`, is
`(a1,a2,b1,b2)=(-1/2,-1/2,1,-2)`. Its quadratics share `1-t`, so it is
nonprimitive. Neither `k=+/-1` nor `k=infinity` leaves an admissible
first-family point unexamined. The second choice of `b2` and the separate
`p(0)=0` boundary branches belong to the other families and remain outside
this conclusion.

For any admissible `k`, the actual top map `M` has shape `32x30` and rank
29. Its rational nonzero kernel vector `k0` spans its kernel. Consequently
all lifts of the fixed nonzero top are exactly

```text
alpha(k,lambda)=a*(k)+lambda*k0,   lambda in the base field.
```

The rank remains 29 after extension to any characteristic-zero field.
The pure-top check compares all 32 coefficients of
`t*p^i*r^(3-i)`, `i=0,1,2,3`, through degree seven. It verifies both the
constant seed and the vanishing top of the entire `lambda` direction.
This is the whole affine fibre, including every specialization of
`lambda`. A projective point `lambda=infinity` would have zero top after
projective rescaling and is not a lift of this fixed nonzero top. It
belongs to a different stratum; it is not an omitted point of this affine
fibre. Nonzero scalar multiples of `h=t` are absorbed by ancestor scaling
as in the geometric classification.

## 3. Exhaustive partition of the generic denominator

The generic certificate uses the cleared ancestor

```text
alpha_cleared=120*(k-1)^9*(k+1)^9*alpha(k,lambda).
```

This scalar is nonzero throughout the admissible chart. Its exact dual
target value, independent of `lambda`, is

```text
D=89514547200*(k-1)^14*(k+1)^11*Q2^5*qk^8*B*Q1*Q3*Q13,
Q2=k^2-4k+5,
Q1=3k^4-9k^3-19k^2-43k-4,
Q3=13k^4+26k^3+34k^2+6k-7,
Q13=729k^13+1620k^12+2889k^11-11268k^10-26574k^9-39642k^8
    +94014k^7+272968k^6+454897k^5+62256k^4-571463k^3
    -1210068k^2-966908k-379834.
```

The new independent countercheck reconstructs this polynomial exactly
from `dual_on_u`, verifies its degree is 76, and verifies all 30 cleared
ancestor coordinates against the rational seed and kernel. It also
checks every one of the eight distinct displayed factors is squarefree
over `QQ`, and that they are pairwise coprime. The factor multiplicities
are retained rather than replaced by a reduced zero locus.

| Factor | Multiplicity in D | Geometric treatment |
|---|---:|---|
| `k-1` | 14 | Outside the rational chart |
| `k+1` | 11 | Outside the rational chart |
| `qk` | 8 | Nonprimitive homogeneous direction |
| `B` | 1 | Nonprimitive homogeneous direction |
| `Q2` | 5 | Exact dual at both geometric roots, every `lambda` |
| `Q1` | 1 | Exact dual at all four geometric roots, every `lambda` |
| `Q3` | 1 | Exact dual at all four geometric roots, every `lambda` |
| `Q13` | 1 | Exact dual at all thirteen geometric roots, every `lambda` |

There is therefore no additional denominator locus. Off its roots the
generic dual gives `n^T L(alpha_cleared)=0` and `n^T u=D!=0`. Since
ancestor clearing is by a nonzero scalar, this excludes the original
ancestor as well. Every root that survives chart and primitivity tests
lies in exactly one of the four exceptional-field loci below.

## 4. Audit of the exceptional-field arithmetic

The explicit saved duals distinguish the constructions: the [Q1 checker](../computations/verify_session_localcoh_q1_dual_2026_10_07.py), [Q3 checker](../computations/verify_session_localcoh_q3_dual_2026_10_07.py), and [Q13 checker](../computations/verify_session_localcoh_q13_dual_2026_10_07.py) verify lambda-degree bounds 2, 1 and 2 respectively. Each saved vector has 26 nonzero entries; the linear Q3 certificate is a distinct stronger bound within the same exact all-lambda proof.

The Q1, Q2, Q3, and Q13 default checkers use exact `Fraction` arithmetic
in `K[lambda]`, with `K=QQ[k]/Qi`, and dictionaries for polynomial powers
of `lambda`. Convolution followed by descending reduction implements
the appropriate power-basis multiplication. In particular the Q3
relation is
`k^4=-2k^3-(34/13)k^2-(6/13)k+7/13`, exactly the relation from `Q3`.
For Q13 the lower coefficients divided by the leading coefficient 729
give the reduction relation; rational inverses are computed by solving
the exact multiplication matrix and their products are asserted to be
one. The Q13 rational-expression parser admits only integers, `k`,
rational arithmetic, and nonnegative integral powers.

The fields really are fields. Q2 has discriminant `-4`, hence is
irreducible over `QQ`. The other checkers prove irreducibility through
degree-preserving finite-field reductions and complete Rabin conditions:

| Polynomial | Prime | Monic coefficients in ascending order | Conditions |
|---|---:|---|---|
| Q1 | 23 | `[14,1,9,20,1]` | `x^(23^4)=x`, `gcd(f,x^(23^2)-x)=1` |
| Q3 | 17 | `[6,7,0,2,1]` | `x^(17^4)=x`, `gcd(f,x^(17^2)-x)=1` |
| Q13 | 53 | `[15,43,6,38,30,45,19,21,8,22,31,2,14,1]` | `x^(53^13)=x`, `gcd(f,x^53-x)=1` |

These are the complete tests: the first identity puts every irreducible
factor degree among the divisors of the total degree; for degree four
the gcd condition removes degrees one and two, and for prime degree
thirteen it removes degree one. The first identity also rules out
repeated factors. The integer leading coefficients survive reduction,
so irreducibility lifts to `QQ` by the usual primitive-polynomial
argument. The independent countercheck recomputes the monic reductions
and both conditions with SymPy's separate `galoistools` implementation;
it does not invoke the saved verifier bodies. All conditions passed.

In characteristic zero each `Qi` is separable. Its `deg(Qi)` embeddings
into an algebraically closed characteristic-zero field correspond to
all its geometric roots. Exact polynomial identities over `K[lambda]`
transport through every embedding. A nonzero denominator inverted in
`K` remains nonzero under every such embedding. There are no
`lambda`-denominators: the duals are polynomials, with entry 72 exactly
one, so specialization introduces no exceptional lower-parameter values.

## 5. Actual tensor, full lifts, and direct source binding

The retained tensor has header `30 18 74 542`: thirty ancestor coordinates,
eighteen actual quartic multiplier coordinates, seventy-four quotient
coordinates, and `30*18+2` columns. All exceptional-field checkers read
this tensor, assert the two final columns are `e72` and `e73`, and check
all eighteen identities

```text
sum(row=0..73) n[row](lambda) *
    sum(i=0..29) tensor[row,18*i+col]*alpha[i](lambda) = 0,
for col=0..17,
n[72](lambda)=1.
```

Thus if `L(alpha)*x=u` for any eighteen-coordinate multiplier vector,
left multiplication by `n` would give `0=1`. This argument is valid for
every `lambda` and every field embedding. It does not require trusting
the saved Macaulay2 module command, its evaluation ideal, or the claim
that the returned row spans an entire kernel. One correct exact row is
enough. Failure to reach `u` also rules out the stronger incidence that
requires both target eigenclasses.

The Q3 and Q13 source loops, field relations, irreducibility tests,
target checks, all 32 pure-top coefficient checks, rank-29 Gaussian
elimination, homogeneous resultants, and all eighteen tensor identities
were inspected rather than inferred from terminal success messages.
Q1 and Q2 follow the same complete identity pattern. Every coefficient
certificate binds the actual tensor, bases, top map, rational seed,
saved full dual, and auxiliary generation records by SHA256.

One provenance limitation needed an explicit additional check: the
default Q1/Q2/Q3 verifiers validate the saved field direction and pure-top
lift but do not themselves derive every constant seed/direction
coefficient from the rational first-family expressions. Hash binding
alone does not establish that derivation. The Q13 default verifier does
derive those coefficients directly. The new independent countercheck
supplies the missing direct comparison for **all four** fields: all
thirty seed coefficients, all thirty lower slopes, and all six direction
coefficients match the rational first-family source after exact modular
reduction. Every rational denominator is checked nonzero and inverted.
This closes the provenance limitation without editing the existing
checkers or relying on a fresh regeneration of their inputs.


## Second rational family: cubic and quartic exception strata

<a id="source-2026-10-13-evening-localcoh-exception-fieldsmd"></a>

## Exact result currently completed

**PROVED under the audited actual multiplication tensor and coordinate bases:**
every root of both factors

```text
f3=3*k^3+4*k^2+9*k-4
f4=13*k^4+10*k^3+2*k^2-42*k-7
```

is excluded for **every** affine lower-lift parameter `lambda`. These account
for seven of the 22 geometric parameter points still retained after the
accepted generic and quadratic calculations. The degree-fifteen stratum is closed by the exact original-tensor certificate above.

The Macaulay2 computations returned target evaluation ideal `(1)` over each
number-field polynomial ring `K[lambda]` and a polynomial left dual `n` with

```text
n^T L(a*(k)+lambda*k0)=0,
n^T u=1.
```

The cubic dual has 26 nonzero entries and degree at most two in `lambda`.
The quartic dual has 26 nonzero entries and degree at most one in `lambda`.
Consequently these certificates exclude the entire affine lower-lift fibers;
they are not ranks or point samples.

## Full-fiber verification and logical scope

The new standard-library verifier
[`evening_localcoh_family2_exception_fields_2026_10_13.py`](../computations/evening_localcoh_family2_exception_fields_2026_10_13.py)
uses `Fraction`, exact polynomial division, and a restricted AST expression
parser. It works in the quotient `QQ[k]/(f)` represented by coefficient
vectors and separately in its polynomial variable `lambda`. Its certificate
verification rederives every source denominator inverse, all rational
direction expressions, all 30 seed coefficients, the affine slope vector,
and both primitive homogeneous directions. It checks:

1. The actual 32-by-30 top matrix has rank 29 over `QQ`.
2. The specified slope vector is nonzero and every seed plus `lambda*k0`
   satisfies all 32 pure-top identities. Since the top map has one-dimensional
   kernel, this gives every possible affine lift of the specified top.
3. The factor is square-free, so its degree counts distinct geometric roots.
4. The homogeneous Sylvester determinant matches the rational source
   resultant and is a **unit** modulo the factor, so every root has a
   primitive direction and no omitted nonprimitive stratum.
5. The actual tensor target columns are `e72,e73`, the dual coordinate
   `n72` is the constant one, and all eighteen entries of `n^T L` vanish
   identically as polynomials in `lambda` modulo the full factor.

The last identities imply exclusion after every homomorphism from the
quotient into an algebraically closed field of characteristic zero. Thus
coverage of all roots does not depend on accepting a numerical embedding,
a sampled rank, or even the Macaulay2 factorization result. The exact
Macaulay2 `factor` output also reports both factors as irreducible, but the
independent verification only needs square-freeness and the explicitly
checked unit inversions.

The actual tensor and coordinate sources are unchanged and SHA-256-bound
inside each certificate. They are the same tensor sources accepted in the
[previous independent quadratic audit](LOCAL_COHOMOLOGY_DEGREE15_CERTIFICATES.md).
This certificate inherits that audited coordinate interpretation; it does
not reconstruct the ambient quotient basis from fresh geometric generators.


The standard-library verifier above reads the saved exact cubic/quartic certificates under the stems evening-localcoh-family2-cubic-2026-10-13 and evening-localcoh-family2-quartic-2026-10-13. Its default invocation with `cubic quartic` verifies the complete identities; regeneration of kernel generators is unnecessary for checking a saved normalized left dual. One alternative generation method writes L=L0+lambda*L1 and n=n0+lambda*n1+lambda²*n2, equates the four polynomial coefficients of n^TL to zero, and sets the constant target coefficient to one and the other two to zero. This yields a 75-by-222 exact linear system over QQ[k]/(f15). It is a construction method, not additional proof beyond a verified dual.

## Second-family generic coverage and actual tensor meaning

<a id="source-2026-10-08-session-localcoh-family2-genericmd"></a>

## The exact generic denominator locus

**PROVED under the audited actual multiplication tensor and coordinate
bases:** the second rational endpoint family excludes target `u`, for
every lower-correction parameter `lambda`, away from the displayed
denominator roots. After removing chart poles and nonprimitive directions,
the following five square-free, pairwise-coprime factors retain exactly
26 primitive geometric parameter points:

```text
k^2+1
k^2-2k-1
3k^3+4k^2+9k-4
13k^4+10k^3+2k^2-42k-7
243k^15+810k^14+2646k^13+990k^12-9465k^11-54222k^10
 -114414k^9-166406k^8-34359k^7+301686k^6+897946k^5
 +1296458k^4+1345117k^3+811630k^2+285598k-610
```

Each retained parameter point still has its complete affine `lambda`
fibre. These are exceptions to this certificate, with no implication
that they support an ancestor or even an actual rank jump. The full factor fibers are closed by the quadratic, cubic, quartic and degree-fifteen certificates in this owner.

## Actual direction and complete affine family

The independently classified second family has

```text
p=1+(k^2+3)/(2-2k^2)*t
     -(k^2+2k+3)/(2(k+1)^2)*t^2,
r=1+(k-3)(k^2+2k+3)/((k-1)^2(k+1))*t
     -2(k^2+1)(k^2-2k-1)(k^2+2k+3)/((k-1)^3(k+1)^3)*t^2.
```

Its actual quartic lift is the complete affine line
`a*(k)+lambda*k0`, where the 32-by-30 pure-top map has rank 29 and `k0`
is its nonzero kernel vector. The clearing factors are

```text
B=2(k-1)^3(k+1)^3                  [direction denominator]
A=120(k-1)^9(k+1)^9               [ancestor denominator].
```

The certificate stores `alpha=A*(a*+lambda*k0)`, along with
`P=B*p` and `R=B*r`. Its standard-library verifier checks all four
rational direction formulas by polynomial cross-multiplication, the
rank-29 top map, and the coefficient of `lambda` in each of the thirty
ancestor coordinates. It verifies all 32 cleared pure-top identities

```text
B^3 * M(alpha) = A * coefficients(t*P^i*R^(3-i)), i=0,1,2,3.
```

Since `A` and `B` are nonzero on the retained chart, these checks prove
coverage of the entire affine lift fibre at every retained parameter.

## Exact polynomial dual

The saved full 74-by-18 module calculation over `QQ(k)[lambda]` returned
target evaluation ideal `(1)` and a complete polynomial left dual. The
cleared dual has 26 nonzero entries and degree at most two in `lambda`.
Its exact target value is

```text
D=89514547200*(k-1)^15*(k+1)^12*(k^2+1)^5*(k^2-2k-1)^5
 *(k^2+2k+3)^4*(3k^3+4k^2+9k-4)
 *(3k^4-2k^3-6k^2-18k-9)*(13k^4+10k^3+2k^2-42k-7)
 *(243k^15+810k^14+2646k^13+990k^12-9465k^11-54222k^10
   -114414k^9-166406k^8-34359k^7+301686k^6+897946k^5
   +1296458k^4+1345117k^3+811630k^2+285598k-610).
```

The verifier checks all eighteen actual tensor-column identities
`n^T L(alpha)=0` over `QQ[k,lambda]` and `n^T u=D`. It also checks
the actual target columns in the stored tensor are `e72,e73`.
Therefore target `u` cannot lie in the multiplier image wherever `D!=0`,
for every value of `lambda`.

A fixed four-by-four homogeneous Sylvester determinant gives

```text
Res_hom(p,r)=-8*(k^2+2k+3)*(3k^4-2k^3-6k^2-18k-9)
             /((k-1)^5*(k+1)^6).
```

Thus `k=+/-1` are chart poles, while the roots of `k^2+2k+3` and
`3k^4-2k^3-6k^2-18k-9` are nonprimitive. The independent verifier
reconstructs the full factorization of `D`; verifies the five remaining
factors are square-free and pairwise coprime; and verifies they are
coprime to both the chart factor and the homogeneous resultant numerator.
This establishes the precise count and scope of the retained 26 points.


<a id="source-2026-10-08-session-localcoh-family2-quadraticsmd"></a>

## Exact fields and independent coefficient reconstruction

The two computations use

```text
Kplus=QQ[k]/(k^2+1),       k^2=-1,       discriminant=-4;
Kminus=QQ[k]/(k^2-2k-1),  k^2=2k+1,     discriminant=8.
```

Both quadratics are irreducible over `QQ`, since their discriminants
are nonzero rational nonsquares. A single standard-library verifier
implements exact arithmetic in both fields with rational coefficient
pairs. For `k^2=c+d*k`, it inverts `a+b*k` by the explicit formula

```text
(a+b*k)^(-1) = (a+d*b-b*k)/(a^2+d*a*b-c*b^2).
```

Every rational source denominator is checked by this norm formula to
be a field unit. A restricted AST parser, with no `eval`, reconstructs
all source expressions directly in the quadratic field and its
polynomial ring in `lambda`. On every default verification run, it
rederives all thirty saved seed coefficients, all thirty lower slopes,
and the four direction coefficients from the family2 rational expressions.
It compares them exactly with the certificate; it does not merely trust
a previously reduced coefficient table or a point sample.

The explicit direction formulas checked are

```text
p=1+(k^2+3)/(2-2k^2)*t
     -(k^2+2k+3)/(2(k+1)^2)*t^2,
r=1+(k-3)(k^2+2k+3)/((k-1)^2(k+1))*t
     -2(k^2+1)(k^2-2k-1)(k^2+2k+3)/((k-1)^3(k+1)^3)*t^2.
```

In both fields the verifier checks all 32 actual pure-top identities,
the rank-29 top map, and that the coefficient of `lambda` in the lift
is the exact nonzero kernel vector. Thus the full affine lift fibre is
covered. Its fixed four-by-four Sylvester determinant confirms the
homogeneous direction is primitive, even though `r` loses its quadratic
coefficient at these parameter values.

## Full polynomial duals

Separate reduced 74-by-18 modules were generated from the actual tensor,
using the directly reconstructed field coefficients. In each field,
Macaulay2 computed the full polynomial left-kernel module over `K[lambda]`
and returned target evaluation ideal `(1)`. The resulting duals each have
27 nonzero entries and degree at most two in `lambda`.

The independent verifier checks every coefficient of all eighteen
identities `n^T L(a*+lambda*k0)=0`, and checks `n^T u=1`. It checks the
actual target columns in the tensor are `e72,e73`, so the target evaluation
is tied to the same actual multiplier incidence. Since the fields are
quadratic and separable in characteristic zero, these identities hold
through both embeddings of each field into an algebraic closure. No
specialization or generic-rank extrapolation enters the conclusion.


<a id="source-2026-10-08-session-localcoh-family2-quadratic-independent-auditmd"></a>

## Actual forms, top map, and complete parameter fibre

The independent
[`countercheck.py`](../validation/2026-10-08-family2-quadratic-audit/countercheck.py)
parses the displayed stage-four ancestor numerators and quartic forms in
[`localcoh-incidence-bases.txt`](../computations/localcoh-incidence-bases.txt).
It verifies the quartics are the following **actual degree-four forms**:

```text
q=xw-yz, A=x^2z-y^3, B=xz^2-y^2w, C=yw^2-z^3;
q*(x^2,xy,xw,yz,zw,w^2),
A*(x,y,z,w), B*(x,y,z,w), C*(x,y,z,w).
```

They all vanish on `C0` and have independent coefficient vectors of rank
18. The restriction of the 35 degree-four monomials to `C0` has rank 17,
so the displayed forms span exactly the full degree-four ideal piece.
They are not four-coordinate generator rows mistaken for polynomial forms.

The checker independently substitutes `x=1,y=t,z=t^3+a,w=t^4+ta+q`
in every actual ancestor numerator. It extracts its normal-order-three
part, converts it to the previously audited balanced normal coordinates,
and computes all four degree-six residues. All thirty top columns match
the saved top map literally. The resulting `32x30` matrix has rank 29.
Its nonzero rational kernel vector is exactly the lower slope in the
family2 seed. Consequently every lift of the specified nonzero pure top
is the full affine line

```text
alpha(k,lambda)=a*(k)+lambda*k0.
```

At each quadratic field, all thirty constant seed coefficients and all
thirty slopes are compared directly to the rational family2 source, and
all six direction coefficients are compared to the same source. Every
source denominator is inverted only after checking it is a unit modulo
the defining quadratic. All 32 coefficients of the specified actual
normalization `t*p^i*r^(3-i)`, `i=0,1,2,3`, match the top of `alpha`.
Thus no lower parameter is lost through sampling or a generic-rank
argument. The projective limit with zero top is a different stratum,
not a lift of this fixed nonzero top.

The independent fixed-size homogeneous Sylvester determinant is nonzero
in each field even though `r` loses its quadratic coefficient there:

| Field | Chosen exact embedding | Homogeneous resultant |
|---|---|---|
| `QQ[k]/(k^2+1)` | `k=i` | `-8i` |
| `QQ[k]/(k^2-2k-1)` | `k=1+sqrt(2)` | `-96+68sqrt(2)` |

The second norm is `-32`, so neither conjugate resultant vanishes. Both
quadratics are coprime to the chart-pole factor and homogeneous
nonprimitive factors. These four parameters are admissible primitive
directions, not excluded chart or normalization points.

## Fresh reconstruction of the complete actual tensor

The independent
[`actual-tensor-reconstruction.m2`](../validation/2026-10-08-family2-quadratic-audit/actual-tensor-reconstruction.m2)
rebuilds the ancestor space from the Ext map, verifies that it has
dimension 30 and that the map is injective in degree `-7`, and sums all
four ideal-generator contributions to obtain actual quartic forms.
Every one of its thirty degree-thirteen ancestor polynomial entries and
eighteen quartic polynomial entries agrees literally with the frozen
displayed bases. It additionally verifies `I^4*h subset (q^4,B^4)` for
each ancestor and every generator of `I^4`.

All 540 actual ancestor-times-quartic product columns and the two target
columns are reduced modulo `(q^4,B^4)` afresh. Their full coefficient
matrix has rank 74, the product-only matrix already has rank 74, and
the independent compressed matrix is **literally equal** to the retained
`74x542` tensor. The union of the uncompressed coefficient rows and stored
rows also has rank 74. Thus no quotient equation or target row was lost
through compression. The entire degree `-3` stage-three Ext image is
independently reconstructed in the same quotient, its injection is
verified, and its union with the 540 product columns has rank 74. This
establishes actual equality with the complete next-stage image, beyond
merely matching its abstract dimension.


The [generic certificate/verifier](../computations/verify_session_localcoh_family2_generic_2026_10_08.py), [quadratic certificates/verifier](../computations/verify_session_localcoh_family2_quadratics_2026_10_08.py) and [independent quadratic countercheck](../validation/2026-10-08-family2-quadratic-audit/countercheck.py) supply exact support for these assertions. Their raw inputs are part of the proof dependency closure. Source hashes and successful process records alone do not establish that the tensor represents the complete actual incidence; the Ext and polynomial reconstruction above does.

## Characteristic of the tensor and dual certificates

An exact annihilator identity nᵀL=0,nᵀu=1 excludes the target over any coefficient algebra in which it is defined. The certificates here, however, use the characteristic-zero balanced frame, rational denominators, polynomial quotient units and rank29 source coverage. Reduction modulo a prime requires verifying that the geometric tensor still represents the same complete actual source and that every cleared denominator and normalized target unit survives; the present rational certificates do not establish those checks. In particular characteristic2 changes the conormal splitting. Polynomial duality as a mechanism extends, whereas these particular family exclusions retain their audited characteristic-zero scope. [the every-positive-characteristic quartic-carrier construction](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier) shows why a universal positive-characteristic nonexistence conclusion would be false.


---

## Source: 2026-10-14-generalization-localcoh-pencil-independent-review.md

# Independent review of the observable corank-one pencil theorem

Date: 2026-10-14. Reviewer: root. Status: **PROVED under the stated exact
rank hypotheses**. This reviews the new abstract theorem in
[the polynomial-dual note](POLYNOMIAL_DUALS_AND_AFFINE_PENCILS.md), not
any previously accepted tensor computation.

For a field `K`, consider `L(lambda)=(lambda I_q+A; B)` with
`rank B=q-1` and `rank(B;BA)=q`. These hypotheses give a generator
`h` of `ker B` with `h,Ah` independent. If the lower target is outside
`im B`, a constant normalized left dual excludes it. Otherwise choose
`Bc=w`. Every prospective solution has the form `c+t h`. After a
constant basis change making `h=e1,Ah=e2`, and choosing `c1=0`, its
top equation is exactly

```
t(lambda e1+e2)=p-lambda c,  p=v-Ac.
```

Eliminating `t` gives the `q-2` linear equations
`p_j-lambda c_j=0` for `j>=3`, and the single quadratic
`p1-lambda p2+lambda^2 c2=0`. The direction `lambda e1+e2` never
vanishes, so these equations are sufficient as well as necessary,
including every finite geometric parameter value.

For a matrix `D` with `DB=diag(0,1,...,1)` and `Dw=c`, each row
`t` annihilating `lambda h+Ah` defines the left dual

```
(t, -t(lambda I_q+A)D).
```

Direct multiplication gives zero on `L`, and evaluation on the target
gives `t(p-lambda c)`. Rows `e_j` give the linear residuals with dual
degree at most one; `e1-lambda e2` gives the quadratic with dual
degree at most two. If the linear residual ideal is the unit ideal,
constant coefficients already produce one. If it has a common
linear factor, division of the quadratic by that factor gives the
stated Bezout identity with coefficient degree at most one. If all
linear residuals vanish identically, exclusion requires the quadratic
to be a nonzero constant. Thus full geometric exclusion is equivalent
to a normalized polynomial dual of degree at most two. The bound is
complete on this locus, not a guess about a syzygy search.

I also checked the note's rank-drop counterexample and determinantal
fallback. At an unobservable point the specialized left kernel can
grow, and normalized global polynomial duals need not detect an
exclusion there. The rank-stratified minor ideals retain this
exception. Over a parameter ring, the field rank hypotheses and any
pivots must be certified throughout the stratum; a generic matrix
calculation is insufficient.

This review accepts the abstract algebra and its finite-dimensional
reduction. It does not certify any particular family-two exceptional
field computation, any unrecorded rank stratum, the projective lift
at infinity, or the full ancestor incidence. Those applications have
separate evidence records.

## Current exact verification

The saved degree-fifteen certificate was verified successfully in the consolidated tree: all18 original-tensor polynomial column identities vanish modulo the entire degree-fifteen polynomial, the dual has degree at most2 in the affine parameter, and coordinate72 is exactly1. The mathematical inputs and source hashes are retained; absent process metadata is not a prerequisite for this identity check. This is a replay of the normalized dual against its complete actual tensor, not a fresh reconstruction of that tensor or a rerun of every inherited family computation.
