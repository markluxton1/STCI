# Effective rational phase images: Mann partitions and finite mate bounds

Date: 2026-10-15. Owner: `conductor_torsion_geometry`.
Status: **NEW EFFECTIVE STRUCTURAL THEOREM; independent review requested.**
The [full conductor phase-space theorem](2026-10-15-generalization-projection-torsion-coset-reduction.md)
and its [independent review](2026-10-15-generalization-projection-torsion-coset-independent-review.md)
are premises. No accepted proof or computation has been rerun. This note
makes the torsion-coset step effective for an explicitly presented
constructible phase image over `Q`. It does not compute the actual phase
images of the three fixed-C0 projection families.

## 1. The rationality needed by the actual families

All three fixed normalized models can be defined over `Q`: the split
smooth quadric with its diagonal conic, the split quadric cone with its
Cartier conic, and `P2` with its line. The fixed map on that curve is

```
C0=[s^4:s^3 t:s t^3:t^4].
```

Choose rational bases of the relevant section spaces and rational lifts
of these four fixed coordinate sections. Every further lift is obtained
by adding four sections in the rational restriction kernel. Thus the
whole projection parameter family is affine over `Q`, before imposing
admissibility.

The phase-space construction can also be performed over `Q`. Universal
images, quotient inclusions, common ideals, rank strata, full inverse
incidence, and the derivative equations for constant rational functions
are defined by rational algebraic operations. Generic Noether
normalization and primitive-element choices can be made in rational
function fields of rational parameter strata; they do not require
individual geometric branch labels or coefficients from `Qbar`.
Nonzero-minor conditions, all root-ordering variables, and the finite
phase cover are then defined over `Q`. Chevalley image formation gives
a constructible phase image `W` over `Q`.

There is no need to decompose `W` into geometrically irreducible pieces.
An explicit rational constructible presentation has the form

```
W=union_i (Y_i minus B_i),                              (1)
Y_i=V(f_i1,...,f_im_i) subset G_m^D,
B_i closed in Y_i,
```

with all displayed defining equations rational. Such a presentation can
be obtained by elimination from an explicit phase-space model. Its
torsion points, interpreted over `Qbar`, are the same torsion tuples
after embedding into any algebraically closed characteristic-zero
base field. A realized phase over that field is still subject to all
nilpotent and admissibility equations already incorporated into `W`.

This descent statement gives no numerical values for the sizes or
degrees of the uncomputed phase-image equations. It identifies the
arithmetic input once those equations are supplied.

## 2. Imported theorem and primary-source verification

For a nondegenerate rational relation among `s` roots of unity,

```
sum_(j=1)^s a_j zeta_j=0,       a_j in Q^*,
```

where no proper nonempty subsum vanishes, Mann's theorem says that
every ratio `zeta_j/zeta_1` has order dividing

```
P(s)=product_(p prime, p<=s) p.                         (2)
```

The original bibliographic source is H. B. Mann,
[*On linear relations between roots of unity*, Mathematika 12 (1965),
107--117](https://doi.org/10.1112/S0025579300005210).
The precise statement was verified in the primary research paper
J.-H. Evertse,
[*The number of solutions of linear equations in roots of unity*,
Section 2, p. 3](https://pub.math.leidenuniv.nl/~evertsejh/98-roots.pdf),
which explicitly states Mann's Theorem 1 and supplies the relevant
self-contained cyclotomic argument. No effective toric Manin--Mumford
theorem or height estimate is otherwise imported below.

## 3. An explicit finite list of binomial systems

First take a closed rational set

```
Y=V(f_1,...,f_m) subset G_m^D,
f_j=sum_(a in A_j) c_(j,a) X^a,       c_(j,a) in Q^*.
```

Combine equal monomials and discard zero coefficients. A nonzero
monomial equation makes `Y` empty. A zero polynomial imposes no
condition. Apart from these trivial cases, put

```
S=max_j #A_j,             q=P(S).
```

At a torsion point `zeta in Y`, partition each support `A_j` into
minimal nonempty vanishing blocks. Every block has at least two terms.
For a block `A'`, choose `a_0 in A'`. Mann's theorem gives

```
eta_a=zeta^(a-a_0) in mu_q,
eta_(a_0)=1,        sum_(a in A') c_(j,a) eta_a=0.        (3)
```

There are only finitely many support partitions and finitely many
assignments `eta_a in mu_q`. Enumerate them and retain exactly those
satisfying the finite cyclotomic equalities in (3). Associate to each
simultaneous retained assignment the binomial system

```
X^(a-a_0)=eta_a                                      (4)
```

for every block of every defining polynomial. Minimality need not be
imposed again when enumerating: extra nonminimal assignments remain
harmless.

Every solution of (4), including a nontorsion solution, belongs to `Y`.
Indeed each block of `f_j` becomes `X^(a_0)` times its zero constant
sum in (3). Conversely every torsion point of `Y` occurs in at least
one system (4), by the minimal-block construction. Thus this finite
enumeration gives binomial algebraic sets contained in `Y` and covering
**all** torsion points of `Y`.

All operations here are effective: partitions are finite, `mu_q` lies
in the explicit cyclotomic field `Q(zeta_q)`, and the equalities in (3)
are exact algebraic-number calculations. The enumeration may be very
large; no practical complexity claim is made.

## 4. Smith normal form gives the cosets and their orders

For one system (4), let `L subset Z^D` be generated by its character
rows `a-a_0`, of rank `r`. First check consistency: the assigned
right-hand sides must define a homomorphism

```
chi:L -> mu_q.
```

This is checked by integer relations among the finitely many rows.
Reject inconsistent systems. Smith normal form then turns every
consistent system, by an integer torus automorphism, into

```
y_i^(s_i)=theta_i,  1<=i<=r,
s_1 | ... | s_r,          theta_i in mu_q,              (5)
```

with the remaining `D-r` coordinates free. The right-hand sides remain
in `mu_q` because all changes take integer products of the old ones.
The equations split into finitely many connected torsion cosets.
Choose the free coordinates equal to one; every component then has a
torsion representative `tau` satisfying

```
ord(tau) divides q s_r,
s_r=exp(L^sat/L).                                      (6)
```

For rank zero use `s_r=1`: the consistent system is the entire torus.
The unimodular torus automorphism preserves torsion order.
Thus (3)--(6) are an effective finite torsion-coset covering of `Y`;
they replace the abstract existence statement from Laurent in this
rational setting.

## 5. A degree bound independent of coefficient heights

For each Laurent polynomial, multiply by a monomial so its support
has coordinatewise minimum zero, and let `d>=1` be the largest
resulting ordinary total degree. This changes no torus zero locus or
row difference. Every character row of a system lies in

```
d(Delta_D-Delta_D),       Delta_D=conv(0,e_1,...,e_D).
```

Every rank-`r` minor of its row matrix has absolute value at most
`d^r`. To prove this, project to the selected `r` coordinates. Each
row remains in `d(Delta_r-Delta_r)`. Multilinearity reduces the maximum
absolute determinant to rows `d(e_i-e_j)`, with `e_0=0`. These are rows
of a directed incidence matrix with one vertex column removed. Every
square minor of that matrix is `0` or `+/-1`: induct on its size using
a row with at most one nonzero entry, or observe that when every row
has two opposite entries the columns sum to zero. This proves the bound.

The greatest common divisor of nonzero rank-`r` minors is
`s_1 ... s_r`. Therefore

```
s_r <= s_1 ... s_r <= d^r.                             (7)
```

In particular every listed zero-dimensional torsion coset is a point
whose order is at most

```
B_phase=P(S) d^D.                                     (8)
```

This is a numerical upper bound, not a divisibility assertion by
`P(S)d^D`. A common annihilating exponent can instead be taken as
`P(S) lcm(1,...,d^D)`, or computed more sharply as the least common
multiple of the actual integers `P(S)s_r`.

The exponent growth `d^r` in (7) cannot be replaced by `d` in general.
The degree-`d` binomial chain

```
x_i^d=x_(i+1) (i<r),       x_r^d=1
```

has Smith invariants `(1,...,1,d^r)`. Its zero-dimensional points
can have exact order `d^r`.

The bound uses monomial support and integer exponent geometry; it
does not use coefficient height. If only `d,D` are known, the rough
support bound `S<=binomial(D+d,D)` gives the computable alternative

```
B_phase <= P(binomial(D+d,D)) d^D.                    (9)
```

## 6. The constructible boundary remains part of the certificate

Apply Sections 3--5 separately to each `Y_i` in (1). For each listed
connected torsion coset `K subset Y_i`, test whether `K subset B_i`.
This is effective over its computed cyclotomic field: substitute the
monomial parameterization of `K` into the defining equations of `B_i`
and compare Laurent coefficients. Equivalently, perform exact ideal
membership in its binomial prime ideal.

If `K subset B_i`, discard it. Otherwise retain

```
V=K minus B_i,
```

a nonempty relatively open subset of `K`. The finite list of these
pieces has exactly the torsion points of `W`. A retained positive-
dimensional coset has torsion points of unbounded order, since torsion
is dense and only finitely many torus points have bounded order.
A zero-dimensional retained coset contributes its single torsion
point. This proves an effective version of the earlier envelope.

The resulting finite certificate has three possible outcomes:

- No piece survives: `W` has no torsion point, so the projection family
  has no mate in any degree.
- A positive-dimensional coset survives: least mate degrees are
  unbounded across actual carriers in the family.
- Every surviving coset has dimension zero: every phase order is
  bounded by the maximum of the explicit bounds (8) for the rational
  pieces. In particular, deleting all positive-dimensional cosets
  certifies an explicit finite bound.

An isolated torsion point may lie inside a positive-dimensional
`Y_i`. The construction still finds it through a full-rank binomial
system. No inference `phi(order)<=deg(Y_i)` is made. For example,
the curve `x+y=1` has isolated torsion points of order six, captured
by the two-term-ratio equations in the three-term relation.

## 7. The explicit mate-degree consequence

Let `B` be the maximum computed phase-order bound (8) after all
positive-dimensional cosets have been certified deleted. The accepted
full-conductor theorem gives, on every mate-admitting carrier,

```
b_min <= e ceil(M/e),       e<=B.
```

Since `e ceil(M/e)<=M+e-1`, there is the explicit uniform bound

```
b_min <= B+M-1.                                       (10)
```

Thus one can use `B+4` for either quadric family and `B+12` for the
plane family. The sharper exact maximum

```
max_(1<=e<=B) e ceil(M/e)
```

is also computable, or one can use only the finitely many exact orders
of the surviving zero-dimensional cosets. On the generically regular
subfamily the exact least mate degree is `e`, so `B` itself suffices.

This bound is obtained from a finite algebraic/cyclotomic certificate,
not by scanning mate degrees. If no torsion coset survives, a mate-
degree bound is unnecessary because nonexistence is certified.

## 8. Present boundary of effectivity and scope

For the actual three fixed-C0 families, rationality removes an
arithmetic height obstruction: once a rational constructible image
presentation (1) is available, every step above terminates through
finite exact algebraic operations and has an explicit order bound.
The currently unavailable input is the presentation itself, including
the full nilpotent equations, its elimination degrees and supports,
and the boundary equations. The earlier finite-type existence theorem
does not supply numerical values of `D,d,S` merely from the contact
budgets `140,765`. Consequently no numerical uniform mate-degree
bound for the three families is asserted here.

The rationality condition is substantive for this particular formula.
For coefficients in a general number field, Mann's rational primorial
bound cannot be reused without a field-dependent replacement. For
instance `X-zeta_N` has two terms and degree one over `Q(zeta_N)`, but
its point has order `N`. This note imports no quantitative number-field
replacement. That issue does not obstruct the three rational fixed-C0
families, because their entire constructible phase images, rather than
individually chosen geometric components, can be kept over `Q`.

The theorem treats all torsion orders at once, but does not compute a
surviving phase or exclude the actual families. The unrestricted
fixed-C0 and universal integral-curve STCI questions remain open.

