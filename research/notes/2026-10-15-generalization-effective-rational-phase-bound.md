# Effective rational phase images: Mann partitions and finite mate bounds

Date: 2026-10-15. Owner: `conductor_torsion_geometry`.
Status: **NEW EFFECTIVE STRUCTURAL THEOREM; independent review PASS.**
See the [independent review](2026-10-15-generalization-effective-rational-phase-bound-independent-review.md).
The [full conductor phase-space theorem](2026-10-15-generalization-projection-torsion-coset-reduction.md)
and its [independent review](2026-10-15-generalization-projection-torsion-coset-independent-review.md)
are premises. No accepted proof or computation has been rerun. This note
makes the torsion-coset step effective for an explicitly presented
constructible phase image over `Q`. It does not compute the actual phase
images of the three fixed-C0 projection families. The finite Mann and
boundary enumerations described below have not been executed for them.

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
normalization, primitive-element, and matrix choices can be made over
`K(x)`, where `K=Frac(A)` is the function field of a `Q`-defined integral
parameter stratum with rationally presented coordinate ring `A`.
Such strata need not be rational varieties: no identification
`K=Q(T)` is assumed. Primitive elements are used for finite separable
reduced residual algebras; the nonreduced conductor quotient remains
encoded by its bases and multiplication matrices. The finitely many
matrix coefficients spread to rational-function presentations over
localizations of `A`. Denominators in `x` and their zero loci retain
the treatment supplied by the accepted full-conductor construction;
coefficient specialization and rank exceptions remain in its finite
stratification. All root-ordering and splitting choices are recorded by algebraic variables
and equations over these rings, rather than by individually chosen
geometric branch labels. Consequently the full phase cover and its map
are defined over `Q`. Chevalley image formation gives a constructible
phase image `W` over `Q`.

There is no need to decompose `W` into geometrically irreducible pieces.
An explicit rational constructible presentation has the form

```
W=union_i (Y_i minus B_i),                              (1)
Y_i=V(f_i1,...,f_im_i) subset G_m^D,
B_i closed in Y_i,
```

with all displayed defining equations rational. Such a presentation can
be obtained by elimination from an explicit phase-space model. Here
`W` is the geometric image, not the image of `Q`-rational parameter
points. Every torsion tuple is defined over `Qbar`. Its finite-type
fibre is nonempty over `Qbar` if and only if it is nonempty after an
algebraically closed characteristic-zero field extension; this follows
from faithful flatness and the Nullstellensatz. Thus the realized
torsion tuples are unchanged after such an extension, with every
nilpotent and admissibility equation retained. This does not assert
that every original carrier with transcendental coefficients descends
to `Qbar`.

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
Acta Arithmetica 89(1) (1999), 45--51,
author's version, Section 2, p. 3](https://pub.math.leidenuniv.nl/~evertsejh/98-roots.pdf)
([published DOI](https://doi.org/10.4064/aa-89-1-45-51)),
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
condition. If no equation remains, take `S=0`, `q=P(0)=1` (the empty
prime product), and enumerate the single empty binomial system; its
solution set is the whole torus. In the nonempty-equation case put

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
has coordinatewise minimum zero, and set `d` equal to the maximum of
one and all resulting ordinary total degrees. If no equation remains,
take `d=1`. This changes no torus zero locus or row difference. Every
character row of a system lies in

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

For `D=0`, the torus is its single point, of order one. All defining
polynomials are constants, so the preceding preprocessing decides
whether `Y` is empty or this point. The conventions `q=d=1` in the
latter case give `B_phase=1`, and the boundary test below decides
whether that point is retained.

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

Assume at least one piece survives and all positive-dimensional
cosets have been certified deleted. Let `B` be the maximum computed
phase-order bound (8) for the surviving zero-dimensional pieces.
The accepted full-conductor theorem gives, on every mate-admitting carrier,

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
The presentation not yet available in this research record includes
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
No Mann partition enumeration or boundary-containment enumeration has
been executed in this note; the finite procedure is proved here.

## 9. Meta-effectivity from explicit projection-family input

Status: **PASS for the precise explicit rational fixed-model input below**
in the separate [2026-10-16 raw-input scope audit](2026-10-16-generalization-raw-projection-decision-independent-audit.md).
This adds an algorithm-existence corollary to the accepted explicit-phase-image
decision theorem; no actual phase image has been computed.

For the three fixed normalized models, the need to supply a phase-image
presentation in Sections 3--8 can be removed at the level of
in-principle computability. The following corollary algorithmizes the
accepted phase construction; it is not inferred merely from the
existence of some finite-type phase space.

**Corollary.** Give one of the three fixed `Q`-models, its prescribed
curve and polarization, and an explicit finite algebraic presentation
of a projection family: finitely many rational polynomial section
coefficients in finitely many parameters, with any additional
`Q`-constructible parameter restrictions. The fixed section rings are
available through the usual Veronese/Segre/quadric presentations.
The four sections have the prescribed fixed restrictions to `c`, or
the finite coefficient equations imposing those restrictions are
included as an initial parameter condition.
Within the admissibility and fixed-normalization scope of the accepted
phase theorem, there is a terminating exact algorithm which constructs
a rational phase-space/image presentation and returns one of the
three alternatives in Section 6. Thus it decides whether any actual
carrier in this input family admits a mate. If such carriers exist,
it decides whether their least mate degrees are unbounded; in the
bounded case it computes a valid uniform bound as in Section 7.

Here input means finite polynomial and module data over `Q`, not an
arbitrary variety or carrier supplied without a computable field
presentation. The corollary does not require an oracle for arbitrary
divisor class groups or for functions on unspecified varieties.

**Proof of meta-effectivity.** Begin with effective decomposition of
the parameter presentation into `Q`-defined integral locally closed
pieces. A piece has a computably presented domain `R` and function
field `K=Frac(R)`; equality and arithmetic in `K` and `K(x)` are
decidable by polynomial ideal membership. Their possible algebraic
constant fields cause no need to identify `K` with a purely
transcendental field.

The admissible parameter locus is also computed, rather than supplied
by an oracle. Basepoint incidence and the full inverse-support
condition are polynomial incidence formulas; effective quantifier
elimination computes their constructible parameter loci. On the
basepoint-free locus, ampleness gives the accepted finiteness of the
source map. Compute its generic image ideal by elimination and its
Hilbert polynomial from a homogeneous Groebner basis. Retain the
leading monomials by the same monic-basis localization used below.
The exactness and generic freeness localization described below
preserves the fibre image and
Hilbert polynomial on a computed open. The image degree then gives
the generic map degree `H^2/deg(X_t)`; keep degree-one opens and
recurse on their closed complements, as below. This computes the
finite-birational locus. Integral fibre images are hypersurfaces
because they are surfaces in `P3`. The additional input parameter
restrictions are retained in these constructible operations.

The generic image rings have finite presentations obtained by
elimination from the specified section maps. The source section ring
is an explicit finitely presented normal graded algebra for these fixed models.
On the admissible finite normalization charts, its finite module
structure over the image ring can be constructed by exact algebra,
or by searching for and checking the monic integrality identities and
finite generators whose existence is part of the accepted setting.
Kernels, quotient inclusions, intersections, and common conductor
ideals are computable by syzygies and annihilators; for a finite
inclusion `A subset B`, the conductor is obtained from
`Ann_A(B/A)`. These are operations on finitely presented modules, not
unbounded searches through possible mate powers.

The further generic choices have finite verifiable certificates.
Relative Noether coordinates are certified by the monic finiteness
identities for the full conductor quotient. Bases and their
multiplication tables are certified by module identities and nonzero
minors. Primitive elements of finite separable reduced residual
algebras are certified by their powers forming a basis, together with
the relevant separability/rank tests. They are not used to replace
the nonreduced conductor quotient. One can use standard exact
algorithms or dovetail the enumeration of candidate choices and finite
certificates. The generic existence assertions in the accepted
construction ensure that a certificate is eventually found. All
candidate data lie in the computable fields `K` or `K(x)`.

Spreading these certificates requires more than clearing the
denominators of displayed identities. Fibre kernels, inclusions and
the common ideal must retain their specified exactness. The needed
generic freeness is itself effective. To see the module version
directly, present a relevant finite module as

```
M=R[u_1,...,u_n]^a/N.
```

Compute a module Groebner basis of `N` over `K[u_1,...,u_n]` and make
it monic. Record the finite expressions generating that basis from
the original relation generators, the reverse generation identities,
and its Buchberger reductions. Invert the product `h` of all nonzero
coefficient denominators appearing in these data. Then the same
monic basis generates `N_h` and has the same reduction identities
over `R_h[u_1,...,u_n]`. The standard module monomials give an
`R_h`-basis of `M_h`, possibly infinite. In particular `M_h` is flat
over `R_h`.

Apply this to the finite collection of relevant modules and
cokernels, and multiply their localization elements. Flatness of the
appropriate cokernels preserves the kernel and inclusion sequences
after every residue-field specialization. This supplies the
base-change control required by the accepted construction's common
ideal and matrix presentations. Nonzero-minor and coefficient-rank
conditions are treated at the same time. Polynomials in `x` do not
thereby become invertible at all source points: their zero loci
retain the accepted full-conductor treatment, with the monic
finiteness certificate for the entire quotient kept before
rational-function localization.

For a primary-source example of the underlying constructive generic
freeness method, see H. Derksen and G. Kemper,
[*Computing invariants of algebraic groups in arbitrary characteristic*,
Advances in Mathematics 217 (2008), 2089--2129, Theorem 2.13 and
Algorithm 2.14, pp. 2114--2115](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/05/A.I.a.28.pdf)
([DOI](https://doi.org/10.1016/j.aim.2007.08.016)). Their displayed
algorithm treats a ring inclusion of domains; the monic module-basis
argument above supplies the finitely presented module version needed
here.

At each integral parameter piece the finite certificates hold on a
computed nonempty open `D(h)`. Decompose its closed complement
`V(h)` into its finitely many `Q`-prime components and repeat the
generic construction there. Each has strictly smaller dimension
than the current integral piece. This gives a finite recursion tree:
the depth is bounded by the initial parameter dimension, and each
vertex has finitely many children computed by primary decomposition.
All exceptional strata are retained; none is discarded because a
denominator or rank changes there.

The remaining derivative, constant-ratio, nilpotent, root-ordering,
and full inverse-incidence equations of the accepted construction
are finite algebraic operations on these presentations. They give
an explicit finite-type map over `Q`. Effective elimination with
quantifier elimination over algebraically closed fields produces its
actual constructible image, including the nonvanishing conditions
and deleted boundaries. Taking only the elimination closure would
not suffice.

Finally run the finite Mann partitions, cyclotomic equalities, Smith
normal forms, and boundary tests proved in Sections 3--6. Those
steps terminate and give exactly the three alternatives. The accepted
phase-order/mate theorem and Section 7 identify their mate-degree
consequences. This proves the corollary without revisiting the
geometric correctness of the accepted construction.

This is an algorithm-existence and termination result. No step of
this composite construction or of the Mann/boundary enumeration has
been executed for the actual three families in this note. No
practical complexity or numerical mate bound follows before the
required calculations are carried out. In particular this corollary
does not identify which alternative holds for any of the three
whole families, and does not settle the unrestricted fixed-C0 or
universal questions.

