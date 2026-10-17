# Exact low pole spaces on the degree-five A4 normalization

Date: 2026-10-11. Owner: `oct11_nonendpoint_quadric_structure/nonendpoint_pole_spaces`.

Status: **DIRECT PROOF; PARENT REVIEW PENDING**. No mathematical CAS run is
claimed or required for the proof below. This note supplies the entire pole
filtration, its section spaces through degree six, and the possible degree
partitions of a residual divisor. It does not exclude any remaining projection
family or bound higher contact multiplicities.

Work over an algebraically closed field of characteristic zero. The normal
anticanonical degree-five surface S, its unique line ell, the complete smooth
quartic c, and the plane model are those of the
[intrinsic pair classification](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md).
In particular H is ample, `H~5ell`, `c~4ell`, and the actual section U0 of H has
divisor 5ell. The
[explicit-model audit](2026-10-11-session-dp5-a4-explicit-model-independent-audit.md)
verifies the global model and its chart `U0!=0`.

## 1. The entire reflexive section filtration

The complement `S\ell={U0!=0}` is the affine plane with coordinates

    r=x/y, t=z/y=T-r^2.

All functions regular on this complement are consequently `k[r,t]`. Introduce

    v=t^2-r^3=Z0/U0.

At the generic point of ell, use the fourth blowup chart with coordinates
`x,u`, and set `A=1+xu`. The six anticanonical cubics, after the common base
factor has been removed, are exactly

    [Z0:Z1:Z2:Z3:Z4:Z5]
      =[u:A:x^2 A^2:x A:x^3 A^2:x^5 A^3].

Therefore the following are identities in the function field, not merely
first-order approximations:

    r=x^(-2) A^(-1),
    t=x^(-3) A^(-1),
    v=u x^(-5) A^(-3).                         (1)

In particular their exact pole orders along ell are 2,3,5. The last equality
follows from `t^2-r^3=x^(-6) A^(-3)(A-1)`. It records the cancellation that
a weight assignment to r and T alone would miss.

Every polynomial in `k[r,t]` has a unique expression as a finite k-linear
combination of monomials

    r^i t^j v^k,   i,k>=0, j in {0,1}.         (2)

Indeed the presentation

    k[r,t]=k[r,v,t]/(t^2-r^3-v)

is free with basis 1,t over `k[r,v]`, because its relation is monic quadratic
in t. The substitutions in (1) give exact pole weight

    w(i,j,k)=2i+3j+5k                         (3)

and leading coefficient `u^k`. In a sum of terms of maximal weight w, there
is at most one monomial with any fixed k: the equation
`2i+3j=w-5k`, with j equal to 0 or 1, determines j by parity and then i.
Consequently that sum has leading coefficient a nonzero polynomial
`sum a_k u^k` in the residue field k(u). No cancellation of the highest pole
weight is possible. Thus (3) computes the exact ell-valuation of every
polynomial written in its unique normal form (2).

For all n>=0, including n for which nell is not Cartier,

    H0(S,O_S(nell))
      = span_k{r^i t^j v^k : j in {0,1}, 2i+3j+5k<=n}.           (4)

Here `O_S(nell)` is the reflexive divisorial sheaf. To justify the global
equality, a section is a rational function f with `div(f)+nell>=0`. It is
regular on `S\ell`, hence lies in `k[r,t]`; conversely a polynomial with
ell-order at least -n has no negative coefficient at any prime divisor.
On a normal surface those codimension-one conditions are exactly the
definition of the reflexive divisorial sheaf. The A4 point on ell creates
no additional codimension-two extension condition.

## 2. The complete spaces through degree six

| n | Basis of H0(S,O_S(nell)) | Dimension |
| --- | --- | --- |
| 0 | 1 | 1 |
| 1 | 1 | 1 |
| 2 | 1,r | 2 |
| 3 | 1,r,t | 3 |
| 4 | 1,r,t,r^2 | 4 |
| 5 | 1,r,t,r^2,rt,v | 6 |
| 6 | 1,r,t,r^2,rt,v,r^3 | 7 |

For comparison with the intrinsic anticanonical coordinates,

    U1/U0=r, U2/U0=r^2, U3/U0=-rt,
    U4/U0=v-rt, hsec/U0=r^2+t.                (5)

Thus the n=5 row recovers all six anticanonical sections, and the n=4 row
contains the function `T=r^2+t` defining c off ell.

## 3. Class group and possible residual component degrees

The localization sequence for Weil divisor classes gives

    Z[ell] -> Cl(S) -> Cl(S\ell)=Cl(A2)=0.

There is no nonzero relation on ell. If m ell were principal, intersection
with the ample Cartier divisor H would give `m(H.ell)=m=0`. Hence

    Cl(S)=Z[ell].                             (6)

For an integral prime P, write `[P]=m[ell]`. Then `H.P=m`, so m is its
positive projective degree. If m=1, P is linearly equivalent to ell and is
the divisor of a section of `O_S(ell)`. Since the n=1 row is one dimensional,
the only such effective prime is ell itself. Every other integral prime
therefore has degree at least two. This also directly proves uniqueness of
the degree-one prime from the pole calculation.

Suppose an actual quadric section q has

    div(q)=c+D, and ell is not a component of D.

Its residual divisor D has class `2H-c=6ell` and degree six. Formula (6)
and positivity restrict the multiset of prime degrees, with multiplicities,
to exactly

    6; 4+2; 3+3; 2+2+2.                     (7)

These are possible partitions, not assertions that every projection realizes
each partition. Multiplicities and coincidences remain included; for example
3+3 can be twice the same cubic prime, and 2+2+2 can contain repeated conics.
The assumption excluding ell must be checked for the projection under study.

The residual section has a particularly small exact normal form. Since
`div(hsec)=c+ell` and `div(U0)=5ell`, the rational function

    f=q/(hsec U0)

has divisor `D-6ell`. It belongs to the n=6 row and has exact pole order six
because D does not contain ell. Accordingly

    f=alpha r^3+beta v+gamma rt+delta r^2+epsilon t+zeta r+eta,
    alpha!=0.                               (8)

Equivalently, as a polynomial on the affine plane,

    f=beta t^2+gamma rt+epsilon t
        +(alpha-beta)r^3+delta r^2+zeta r+eta. (9)

The coefficient alpha, rather than either coefficient of t^2 or r^3 taken
separately, detects pole order six. This follows from the cancellation in
(1), and is essential on parameter strata where `alpha=beta`.

## 4. Exact forms of the low-degree prime components

The same normal form gives a useful exhaustive list for degrees two through
four. A prime of degree m other than ell is the closure of the affine zero
divisor of a polynomial with exact pole order m. There are no prime divisors
hidden solely at the singular point.

* Degree two: after scalar normalization the polynomial is `r-r0`. Its affine
  zero curve is a line in A2, integral and reduced, so its closure is the
  degree-two prime.
* Degree three: its polynomial is `t+B r+C`, again after scalar normalization.
  It is a graph, integral and reduced, and has exact pole order three.
* Degree four: its polynomial is `r^2+B t+C r+D`, after scalar normalization.
  It is an integral degree-four prime precisely when B is nonzero: then it is
  a graph over r. If B is zero, it factors over the algebraically closed field
  as a product of two polynomials `r-r0`, with repetition allowed, so is a sum
  of degree-two divisors instead.

Thus factoring the seven-dimensional form (8) decides the partitions in (7)
without treating either r or T as independent weighted variables. It supplies
no higher-contact bound at the singular point or at projection ramification
points.
