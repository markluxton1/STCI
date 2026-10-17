# Completeness audit of the first rational endpoint family

Date: 2026-10-08. Auditor: the verification agent, independently of the
certificate-producing agents. Scope: characteristic zero, the fixed curve
`C0=[s^4:s^3t:st^3:t^4]`, primitive degree-two normal-dual direction,
pure cubic top coefficient `h=t`, and the **first** rational endpoint
family in the audited classification. No pre-existing dual, coefficient
certificate, checker, or canonical research record was edited for this
audit.

## 1. Verdict

**PROVED under the previously audited actual top map, coordinate bases,
and multiplication tensor:** every admissible direction parameter in
the first rational endpoint family, with its entire affine line of
quartic lower corrections, fails the target-`u` multiplication incidence.
There are no remaining direction or lower-parameter exceptions in this
family. This conclusion uses the geometric coverage argument, the generic
polynomial dual, all four exact exceptional-field duals, and the direct
cross-artifact checks preserved with this audit; it does not follow from
a generic rank calculation or from a printed `PASS` alone.

The older independent checkpoint
[`2026-10-07-session-localcoh-independent-audit.md`](2026-10-07-session-localcoh-independent-audit.md)
retained 21 first-family geometric points after the quadratic exception
was closed. Its first-family exception list is superseded by the Q1, Q3,
and Q13 certificates and this combined audit. The complete exceptional
partition initially contained 23 geometric points, counting the two Q2
roots; all 23 are now covered, each for every lower parameter `lambda`.

This proves a family exclusion. It does not exclude the other three
classified endpoint families, nonendpoint top-zero strata, every quartic
ancestor, or every degree pair. The global STCI question and the
unrestricted status of `C0` remain open. Positive characteristic is not
covered by the rational arithmetic in this record.

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

## 6. Durable replay record

The new independent source is
[`countercheck.py`](../validation/2026-10-08-first-endpoint-audit/countercheck.py).
It is self-contained apart from the retained repository inputs and
SymPy, writes one deterministic JSON result, and invokes neither the
saved exceptional verifier bodies nor any generator. The final run
completed with exit code zero. Reproduce it from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/validation/2026-10-08-first-endpoint-audit/countercheck.py \
  > research/validation/2026-10-08-first-endpoint-audit/countercheck.log
```

Its
[`countercheck-result.json`](../validation/2026-10-08-first-endpoint-audit/countercheck-result.json)
contains the full factor partition, multiplicities, finite reductions,
all four coefficient-comparison results, and the hashes of every input.
The output
[`countercheck.log`](../validation/2026-10-08-first-endpoint-audit/countercheck.log)
is byte-identical to that JSON. Source SHA256:

```text
4fb9d7cf4b0a119bc8bfd0b1d5bb3a4bece08948bb9d44f505d3091ce2e74df0
```

Result/log SHA256:

```text
d5197c04be2c9fcb567c49b46fa8342345af4bc5dd7b0a3f965c07b61b57d34d
```

The reviewed source hashes and all coefficient-certificate hashes are
preserved in
[`audit-manifest.json`](../validation/2026-10-08-first-endpoint-audit/audit-manifest.json).
The original field proofs and their generation/replay routes are
preserved in the
[Q1 note](2026-10-07-session-localcoh-q1-exception.md),
[Q3 note](2026-10-07-session-localcoh-q3-exception.md), and
[Q13 note](2026-10-07-session-localcoh-q13-exception.md), with Q2 in the
[independent endpoint audit](2026-10-07-session-localcoh-independent-audit.md).
Root's central continuation validation records the full current checker
replays separately. This additional countercheck concerns parameter
coverage and source binding; it does not duplicate or substitute for
the eighteen-column tensor replay.

The next unresolved endpoint work starts with the second rational family
or one of the two `p(0)=0` boundary families. The first family should no
longer be listed as retaining Q1, Q3, or Q13 exceptions.
