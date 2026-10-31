# Actual phase families, rational torsion bounds, and nef formal branches

The first two parts concern every mate power in one fixed **actual** projection
family: they construct its full-conductor phase image and analyze its torsion
points. The final part is an independent geometric formal-branch criterion; it
is not a consequence of torsion-coset arithmetic. All substantive statements
retain their exact characteristic-zero and family hypotheses.

**Review.** The family specialization, torsion-coset, effective rational and
nef-scope arguments have inherited independent review. Mathematical corrections
from those audits are integrated below; no separate audit narrative is needed.
No phase image, Mann partition enumeration, or family-wide decision has been
executed for the three fixed-C0 families. Independent replacement review
accepted the corrected proof preservation and scope; no material finding remains.

<a id="actual-families-and-their-finite-phase-image"></a>
<a id="2026-10-15-generalization-projection-torsion-coset-reduction"></a>
<a id="2026-10-15-generalization-projection-torsion-coset-independent-review"></a>

## Actual families and their finite phase image

### 1. Statement: one finite-type family replaces every mate power

Work over an algebraically closed characteristic-zero field `k`. Fix a
normal integral projective surface `S`, an ample line bundle `H`, and a
smooth ample Cartier curve `c`. Assume there is a section `Q` of `H` with

```
div(Q)=m c,  m>0.
```

Let a finite-type parameter scheme `T` supply four sections of `H`, whose
restrictions to `c` give a fixed embedded curve `C subset P3`. Retain the
parameters satisfying all of the following conditions:

- the four sections are basepoint free;
- the resulting map `f_t:S -> X_t subset P3` is finite and birational,
  and `X_t` is an integral hypersurface;
- the **full** reduced inverse support of `C` is `c`, including absence
  of isolated inverse points outside `c`.

The retained parameter set is constructible. Every `S -> X_t` is the
actual normalization, since `S` is normal and the map is finite birational.
After a finite locally closed stratification of that set, there are a
constructible subset `T_0`, a finite surjective map, and a morphism

```
pi: Z -> T_0,       z: Z -> G_m^D,                       (1)
```

such that a carrier `X_t` has a mate for `C` if and only if a point above
`t` has a torsion phase tuple `z`. This is equivalent to every point
above `t` having a torsion phase tuple. The subset `T_0` retains the
entire nilpotent conductor equations, not just reduced conductor data.

Here a constructible set means a finite disjoint union of locally closed
reduced schemes. Variable phase dimensions can be padded by coordinates
equal to one, so a single integer `D` works in (1).

Put `W=z(Z)`, a constructible subset of the fixed torus. There are finitely
many torsion cosets `K_j=xi_j H_j`, each with `xi_j` a torsion point and
`H_j` a connected subtorus, and nonempty relatively open subsets
`V_j subset K_j`, such that

```
W(k) intersect Tor(G_m^D) = union_j (V_j(k) intersect Tor(G_m^D)). (2)
```

Every `V_j` is contained in `W`. Thus the entire all-power mate problem in
this family is the pullback of finitely many open pieces of torsion
cosets. This assertion does **not** make the torsion set or mate locus
constructible, and does not give computed equations for `W` or the cosets.

For the three accepted fixed-C0 Cartier-lift models the hypotheses are
the fixed degree-eight smooth quadric, degree-eight quadric cone, and
degree-sixteen plane models, with `H=2c,2c,4c` respectively. Their actual admissible parameter loci and phase images remain to be
computed; complete affine lift sources do not by themselves establish
admissibility or mate descent. No non-Cartier lift,
multiple inverse lift, higher-degree inverse lift, or arbitrary normal
surface family is added to the accepted classification.

### 2. Why the family uses the actual normalization on every stratum

Basepoint freeness is open: project the closed basepoint incidence from
the proper source `S times T`. On this open set the universal morphism
`f:S times T -> P3 times T` is proper. No fibre of a fibre map can contain
a curve, since the pullback of `O(1)` is ample. Hence `f` is quasi-finite
and proper, and therefore finite onto its scheme-theoretic image `X`.

On a dense open of every irreducible parameter stratum, flatten the
coherent image and quotient modules. In particular require flatness of
`f_*O_(S times T)/O_X` over the parameter base. Then

```
O_(X_t) -> (f_t)_*O_S
```

is injective after base change, and `X_t` is the scheme-theoretic image
of `f_t`. The image of an integral `S` is integral with this scheme
structure. Stratify so the Hilbert polynomial of `X_t` is constant.
The finite map has generic degree

```
deg(f_t)=H^2/deg(X_t),
```

so degree one is a union of these strata. A surface in `P3` is a
hypersurface. This supplies constructibility of the finite-birational
hypersurface condition while preserving the actual fibre image.

Finally form the closed inverse incidence `f^{-1}(C times T)` and delete
`c times T`. Its image in `T` is constructible by Chevalley; remove that
image. This removes every extra inverse point, including isolated ones.
The prescribed restriction of `f` to `c` already supplies the required
inverse curve. These operations give the admissible constructible set.

No simultaneous-normalization theorem is being assumed: the source is
fixed, and finite birationality proves that its map is the normalization
separately on each retained fibre.

### 3. Full conductor quotients survive specialization

The following details close a specialization gap in an informal use of
generic rational multiplication tables. Spreading only a generic
`k(T)(x)` basis would not by itself rule out extra conductor components
on specialized fibres.

Write `A=O_X` and `B=f_*O_(S times T)` on a parameter stratum. At its
generic point choose a nonzero **common conductor ideal** `J`: it is an
ideal of `B` contained in `A`. Spread its finite generators and the
finite identities `JB subset A`, shrinking the parameter base. Flatten
the relevant coherent quotient modules so that

```
A_t subset B_t,       A_t/J_t subset B_t/J_t             (3)
```

are the actual fibre inclusions, and `J_t` is still a common ideal.
Shrink also so `Supp(B_t/J_t)` has dimension at most one on every fibre.
This is possible because the generic ideal is nonzero and the support
is projective over the parameter base.

The ideal `J_t` need not equal the fibre's largest conductor ideal. That
causes no loss: membership is exactly tested modulo any common ideal,

```
b in A_t iff b mod J_t belongs to A_t/J_t.               (4)
```

Use finitely many target affine charts; away from `C`, refine by
principal opens from generators of its fixed ideal. If a chart's generic
quotient support has dimension zero or is empty, shrink the parameter
base so that all its fibres have no one-dimensional support, and omit
that chart from the generic-curve tests; the closed complement is handled
recursively. This uses [generic constancy of fibre dimension](https://stacks.math.columbia.edu/tag/05F7).
On each remaining chart, at the generic
parameter choose a Noether-normalization coordinate
`x in A/J`. Crucially, spread the finitely many **monic integrality
equations on the entire chart algebra** before passing to `k(x)`.
After shrinking the parameter stratum, both quotient algebras are finite
over `R[x]`, where `R` is the coordinate ring of the stratum.

Every one-dimensional component of every fibre of such a finite
`R[x]`-algebra dominates `A1_k`: a finite map preserves the dimension
of a component, so its image cannot be a point. Consequently tensoring
with `k(x)` retains the full Artinian local algebra at **every** generic
conductor curve of that fibre. It cannot discard a specialized curve
because its chosen coordinate happened to become constant.

Finite presentations now give generic bases and multiplication tables.
Invert a polynomial `h(x,t)` so these bases represent the quotient
algebras, and shrink the parameter stratum so `h(x,t)` is nonzero as a
polynomial in `x` for every remaining `t`. After tensoring with `k(x)`,
the specialized tables are precisely the localized fibre algebras in
(3). Their sizes are fixed on this stratum.

Repeat on the closed complement. The dimension of the parameter base
drops, so only finitely many strata are needed. This is relative
Noether normalization followed by generic freeness, not an assumption
that normalization or the largest conductor commutes with arbitrary
specialization.

Zero-dimensional support of a smaller common ideal may disappear when
tensoring with `k(x)`. It supplies no missing global descent condition:
the accepted Cohen--Macaulay conductor theorem says that the quotient
`nu_*O_S/O_X` has no associated closed points. Actual generic membership
on every conductor curve already implies global membership. A smaller
common ideal introduces no new obligation because of (4).

For a uniform threshold over `C`, carry out the same finite-presentation
and rank-stratification construction on charts meeting the generic point
of `C`, retaining components with image `C`. The section `Q` is nilpotent
in every such full quotient, because it vanishes on every inverse branch.
Its nilpotence exponent is at most the matrix dimension. The finitely
many strata therefore give one finite bound `M>=1` such that `Q^n` enters
these common ideals for every `n>=M`. This bound uses the actual
finite-type algebra presentations; it is not inferred from reduced
contact graphs, a fixed surface degree, or an unspecified formal family.

In the three fixed-C0 models, the accepted
[actual-conductor duality formula](PROJECTION_CONDUCTOR_CONTACT_AND_PHASE.md#2026-10-14-generalization-projection-conductor-budget-independent-review)
gives a sharper explicit threshold. Write the actual upstairs conductor
as `O_S(-B)`, with `B~(a-4)H-K_S`. This part of duality requires the
Gorenstein normalization and hypersurface image, but not generic
regularity along `C`; that regularity was used separately to exclude
`c` from `B` in the contact budget. If `r=ord_c(B)`, effectivity of
`B-r c` and ampleness of `H` give `r(c.H)<=B.H`. Both quadric models
have `B~10c` and `ord_c(Q)=2`, so `r<=10` and `Q^n` belongs to the
actual conductor at the generic point of `C` for every `n>=5`.
The plane model has `B~51h`, `c=h`, and `ord_c(Q)=4`, so `r<=51`
and `n>=13` suffices. Thus the degree bound (8) may use `M=5` for
the quadric models and `M=13` for the plane model, even on the
generically singular boundary along `C`. These values certify actual
conductor membership; they need not put `Q^n` in an auxiliary smaller
common ideal `J`, and no such assertion is needed for descent.

### 4. The logarithmic defects are bounded algebraic equations

Here is the relevant finite-algebra construction. Let `F=k(x)` and let
`A subset B` be one of the resulting finite-dimensional commutative
`F`-algebra inclusions, allowing products. Write `N_A,N_B` for their
nilradicals. Characteristic zero makes the residue algebras finite
etale. Their unique etale lifts give compatible subalgebras

```
A=K direct_sum N_A,       B=E direct_sum N_B.
```

For a unit `u` representing `Q` in a target frame, write uniquely

```
u=v exp(w),       v in E^*, w in N_B.
```

Then for every positive integer `n`,

```
u^n in A iff w in N_A and v^n in K.                     (5)
```

Indeed the etale and nilpotent parts of `u^n` are `v^n` and `nw`;
characteristic zero gives `nw in N_A iff w in N_A`. Put

```
D_A=E tensor_K E,        rho=(v tensor 1)/(1 tensor v).
```

The injective finite etale map `K -> E` is faithfully flat, including
when both are products. Its equalizer identity gives

```
v^n in K iff rho^n=1.                                  (6)
```

Thus eventual descent is exactly a nilpotent equation `w in N_A`
together with a residual torsion test. Once eventual descent holds,
the least exponent at this model is the exact order of `rho`.

All nilpotent equations in (5) have a bounded finite presentation on
each matrix stratum. To make that precise, the radical of the trace
pairing is the nilradical of a finite commutative characteristic-zero
algebra. After algebraic closure, decompose into Artinian local factors:
on a factor of length l, the trace of multiplication by ab is l times
the product of the residues of a,b. Since l is nonzero in characteristic
zero, the pairing radical is exactly its maximal ideal. Descending this
identity gives the stated nilradical. Refine by ranks and chosen nonzero minors to obtain its basis.
For an etale reduction, choose a primitive element and retain both
its discriminant and the determinant certifying that its powers span
the reduction. Finite Newton lifting recovers its canonical etale lift;
the number of steps is bounded by the algebra dimension. Finite
logarithm then computes `w`, and a matrix membership test imposes
`w in N_A`. The chosen determinants ensure that the procedure
specializes correctly throughout the stratum.

After denominators are cleared, these are closed algebraic conditions
within each chosen rational-matrix stratum. Their union over finitely
many strata is constructible. There is no claim that the union is
closed in the original projection parameter space. In particular,
no global-mate uniqueness argument or noetherian stabilization of an
unbounded list of powers is needed for the nilpotent conductor step.

### 5. Constancy, phases, and the finite cover

Let `chi_rho(Z)` be the characteristic polynomial of multiplication by
`rho` on the etale `F`-algebra `D_A`. Since `k` is algebraically closed,

```
rho torsion iff every root of chi_rho is in mu_infinity(k). (7)
```

Repeated roots of the characteristic polynomial are allowed. The minimal
polynomial is squarefree because D_A is etale; if all characteristic roots
are killed by n, that minimal polynomial divides Z^n−1, hence rho^n=1.
Conversely rho^n=1 forces every geometric eigenvalue to be an n-th root
of unity. Thus characteristic roots suffice without falsely assuming the
characteristic polynomial itself squarefree.

Its intermediate constancy condition says that every coefficient
belongs to `k subset k(x)`. This is algebraic in the parameters: for
each rational coefficient `f(x,t)`, clear the denominators of
`partial_x f=0` and set all numerator coefficients to zero. In
characteristic zero the derivative kernel of `k(x)` is `k`.
Refine by a nonzero denominator coefficient so the resulting constant
is a regular parameter function.

On the locus satisfying all constancy and nilpotent equations, adjoin
an ordering `z_1,...,z_d` of the roots of `chi_rho`. The elementary
symmetric equations give a finite surjective phase cover: each `z_i`
satisfies a monic polynomial, its inverse is integral because the
constant term is a unit, and algebraic closedness supplies all root
orderings on `k`-points. Repeated roots are retained, and the cover
need not be etale. Take the product for all quotient models and pad
by ones. This produces (1).

The accepted generic-to-global theorem, followed by ambient lifting
on a hypersurface, proves the exact mate criterion. Components with
image `C` require only the bounded vanishing threshold `M`. Off `C`,
(5)--(7) retain the full conductor obstruction. The order of a phase
tuple is the least common multiple of all of its coordinate orders.
Root orderings and repeated duplicate tests do not alter that number.

Every possible mate is included in this one ray. A degree-`b` mate
pulls back to a divisor `n c` linearly equivalent to `bH=bm c`.
Intersection with `H` forces `n=bm`. Its section is therefore a scalar
multiple of `Q^b`, since the ratio has zero divisor on a normal integral
projective surface and is a constant. Thus the construction has not
chosen a special subclass of mate sections.

When `X_t` is generically regular along `C`, its least mate degree is
exactly this phase order `e(t)`. Without that regularity, every mate
degree is a multiple of `e(t)`, and

```
b_min(t) <= e(t) ceil(M/e(t)).                           (8)
```

More precisely, on every mate-admitting carrier its complete mate-degree
set is

```
(e(t) Z_{>0} intersect [M,infinity)) union F_t,
F_t subset e(t) Z_{>0} intersect {1,...,M-1},
```

where `F_t` records the finitely many actual descents of these low powers
of `Q`. The off-`C` condition is already satisfied for every multiple
of `e(t)`; only actual membership over `C` can remove a low degree.
Consequently `e(t)>=M` gives `b_min(t)=e(t)` even when the carrier is
generically singular along `C`. The explicit choices `M=5,5,13` apply
to the three fixed-C0 models as in Section 3. None of these claims
requires a low power to enter an auxiliary smaller common ideal.

This statement uses that `Q` is a section of `H`, hence has upstairs
base degree one, as in all three fixed-C0 models.
It does not justify multiplying least mate degrees by b0 for an arbitrary
section Q of H^b0 without a primitive Cartier-ray hypothesis. On a smooth
quadric take Q=l² for a hyperplane section l: the phase order is one,
but l already supplies a degree-one mate, so the proposed multiplication
rule would give the wrong minimum.

### 6. Laurent's theorem gives a finite torsion-coset envelope

The external input is Laurent's theorem for a closed subvariety `Y`
of a characteristic-zero torus: its torsion points are contained in
finitely many torsion translates of connected subtori that lie in `Y`.
The original reference is Michel Laurent, *Equations diophantiennes
exponentielles*, Invent. Math. 78 (1984), 299--327. This theorem and
the reference were verified in Laurent's own
[1991 primary-author account, Section 5, pp. 217--218](https://www.numdam.org/item/AST_1991__198-199-200__209_0.pdf).
Only this theorem is imported; no effectiveness assertion is imported.

Decompose the constructible image into finitely many locally closed
irreducible sets

```
W=union_i U_i,        U_i open in Y_i=closure(U_i).
```

Apply Laurent's theorem to `Y_i`, obtaining finitely many torsion
cosets `K_ij subset Y_i` covering all torsion points of `Y_i`.
Discard those with `K_ij intersect U_i` empty, and put

```
V_ij=K_ij intersect U_i.
```

Every retained `V_ij` is a nonempty relatively open subset of its
torsion coset and lies in `W`. The two containments in (2) follow
immediately: every torsion point of `W` lies in some `U_i` and then
some `K_ij`; conversely every torsion point of `V_ij` lies in `W`.
The deleted boundary must be retained; taking only `closure(W)`
would create spurious phases excluded by nilpotent or admissibility
conditions.

Laurent's complex theorem suffices for any algebraically closed
characteristic-zero `k`: the finitely many defining coefficients lie
in a field finitely generated over `Q`, which embeds in `C` after
choosing an algebraic closure. Torsion cosets are defined by integer
characters and roots of unity. Their containment equations therefore
transfer back through that embedding, and every torsion tuple already
has coordinates algebraic over `Q`.

Torsion points are Zariski dense in every torus and hence in every
torsion coset. One proof identifies a torus with `G_m^r` and uses the
fact that a Laurent polynomial vanishing on every product of roots
of unity is zero, by induction on `r`. Thus they are also dense in
each nonempty `V_ij`. Consequently

```
closure(W intersect Tor(G_m^D))=union of retained K_ij.  (9)
```

This is a finite closed torsion-coset envelope for the admissible
torsion phases. It is a structural existence theorem, and does not
by itself compute the envelope from the three projection families.

### 7. Exact bounded-or-unbounded alternative for least mate degrees

Equations (2) and (8) yield the following family-wide dichotomy.

- If every retained `K_ij` has dimension zero, only finitely many
  torsion phase tuples occur. Their orders form a finite set. Thus,
  using the uniform `M`, least mate degrees on all mate-admitting
  carriers in this fixed family are uniformly bounded.
- If at least one retained `K_ij` has positive dimension, its nonempty
  open subset contains infinitely many torsion points. Only finitely
  many torus points have order at most any fixed integer; phase
  orders are therefore unbounded. Every such tuple is realized in
  `W`, hence by an admissible parameter in `T_0`, and every mate on
  that parameter has degree at least its phase order. Least mate
  degrees are unbounded across the family.

If no coset survives, the entire family has no mate in any degree.
These alternatives concern variation **between actual carriers**.
On an individual mate-admitting carrier, all sufficiently divisible
powers already give further mates; that elementary unbounded sequence
is distinct from unbounded *least* mate degrees as carriers vary.

Positive dimension of `W` alone is insufficient: the image
`(lambda,2 lambda)` in `G_m^2` contains no torsion point. Even existence
of a positive-dimensional torsion coset in `closure(W)` is insufficient
if the admissible constructible image deletes it completely.

### 8. Scope and the next bridge

This result treats all exponents through one finite-type algebraic
phase image with full nilpotent equations. It strengthens a finite
list of bounded integer contact graphs: those graphs do not constrain
relative phase orders, whereas the torsion-coset envelope classifies
how unbounded orders can occur in the **actual algebraic family**.
No graph-by-graph enumeration is required for the theorem.

The next mathematical bridge is to obtain equations for the image
`W`, or enough character relations and nonvanishing conditions to
determine its surviving torsion cosets, after imposing the entire
logarithmic defects and all admissibility conditions. Neither contact
equality alone nor a torus dimension count supplies that bridge.

The universal integral-projective-curve STCI problem and the
unrestricted characteristic-zero fixed-C0 problem remain open.

<a id="2026-10-15-generalization-effective-rational-phase-bound"></a>
<a id="2026-10-15-generalization-effective-rational-phase-bound-independent-review"></a>

## Effective rational torsion images and mate bounds

### 1. The rationality needed by the actual families

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

### 2. Imported theorem and primary-source verification

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

### 3. An explicit finite list of binomial systems

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

### 4. Smith normal form gives the cosets and their orders

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

### 5. A degree bound independent of coefficient heights

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

has Smith invariants `(1,...,1,d^r)`: its determinant is d^r,
while for every smaller size a shifted consecutive minor is +/-1.
Its zero-dimensional points can have exact order `d^r`.

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

### 6. The constructible boundary remains part of the certificate

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

### 7. The explicit mate-degree consequence

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

### 8. Present boundary of effectivity and scope

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



## From explicit projection input to a decision procedure

For explicit finite rational polynomial/section/module data on one of the
three fixed normalization models, an in-principle terminating algorithm also
constructs admissibility and the actual phase image before applying the Mann
procedure. Prescribed restrictions on c must hold or be imposed as coefficient
equations, and all Q-constructible parameter restrictions remain in the input.
The [full raw-input proof](EFFECTIVE_PROJECTION_PHASE_DECISION.md) owns effective
module generic freeness, the monic-basis base-change argument, and recursion on
all exceptional closed strata. It does not assume a rational function field
for a parameter piece or an oracle for class groups; root orderings remain
algebraic variables rather than chosen geometric branch labels.

This is algorithm existence and termination, not an executed calculation of
W, a complexity estimate, a numerical bound for the whole fixed-C0 families,
or a decision which outcome holds for them. It is not an arbitrary-normalization
or noncomputable-coefficient theorem. Its geometric conclusions still depend
on the exact admissible normalization and full-conductor family theorem above.


<a id="2026-10-15-generalization-nef-formal-branch-arbitrary-base"></a>
<a id="2026-10-15-generalization-nef-formal-branch-arbitrary-base-independent-audit"></a>

## Nef polarizations and formal branches over arbitrary smooth bases

### 1. The underlying geometric criterion is independent of the blowup

Let `X` be a smooth projective threefold over an algebraically closed
field of characteristic zero. Let `Z` be a smooth connected projective
curve of genus `g`. Suppose there is a smooth embedded formal surface
`Vhat subset Xhat_Z`, with reduced scheme of definition `Z`, and put

    nu=deg N_(Z/Vhat).

Assume

    nu>4g+5.                                             (1)

Let `A` be a nef line bundle on `X`, and put `h=A.Z`. The audited
argument gives an integral algebraic surface closure `W subset X` and a
projective resolution of its chosen branch preserving `Z`. If

    d=A^2.W>0,

then necessarily

    d<=max_(a integer,a>=1)(2ah-nu*a^2).                 (2)

For completeness, the already audited argument uses Bost's geometric
formal algebraicity theorem to algebraize the branch, excellence to
preserve its smooth formal neighborhood after normalization, and
Hartshorne's high-self-intersection theorem to replace that neighborhood
by a section of a geometrically ruled surface. Pushforward of the nef
class to that model has numerical class `a Z0+b f`, with `a>=1`,
`a*nu+b=h`, and square at least `d`; its square is exactly the expression
in (2). A fiber degree a=0 would give square zero, contradicting the
square comparison when d>0; this proves a>=1 rather than assuming it. This repackaging requires neither a rational base curve nor a
blowup presentation. The condition `d>0` is automatic for ample `A`.

For a merely nef `A`, its square on the algebraic surface closure may
vanish; no positive-degree contradiction may then be inferred. A general
nef line bundle need not define a contraction or a morphism.
The blowup application below proves positivity separately.

The imported primary inputs are [Bost, Theorem 3.5 and Corollary 3.8](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf)
and [Hartshorne, Theorem 4.1, with the neighborhood-equivalence definition
in Section 0](https://www.numdam.org/item/PMIHES_1969__36__111_0.pdf).
Their exact hypotheses and the branch-normalization details are covered
by the [accepted full audit](FINITE_ROOT_FAMILIES_AND_SMOOTH_OBSTRUCTIONS.md#2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit).

### 2. Apply it over a smooth curve of any genus

Let `C subset P3` be smooth of degree `e` and genus `gamma`. Assume the
actual normal bundle has the form

    N_(C/P3)=L direct_sum L,     deg L=lambda.            (3)

This is a specific vector-bundle hypothesis. Equal numerical slopes,
semistability, or a decomposition into two line bundles of the same
degree do not imply (3). Equivalently, the associated projective bundle
must be trivial as a `P1`-bundle **over `C`**. Conversely its degree-one
tautological bundle in a product trivialization is Q boxtimes O(1);
relative pushforward recovers two identical line summands. This is why
triviality over C gives the actual vector-bundle condition, not only slopes.

The tangent and Euler sequences give

    2lambda=4e+2gamma-2,
    lambda=2e+gamma-1.                                   (4)

On `B=Bl_C(P3)`, write

    E=C x P1,
    O_E(-E)=L^(-1) boxtimes O(1).

Let `M` be a line bundle on `C`, of degree `epsilon`, and let

    Z in |M boxtimes O(r)|

be smooth, connected, and finite over `C` of degree `r`. Consider a
compatible embedded Cartier lift of this root through every exceptional
neighborhood of `E`, with all local equation units retained.

Exactly as in the accepted rational-base theorem, it gives a smooth
formal surface `Vhat` along `Z`, transverse to `E`, and

    N_(Z/Vhat)=O_Z(E).

The product intersection and adjunction calculations are now

    Z^2_E=2epsilon*r,
    K_E.Z=r(2gamma-2)-2epsilon,
    g_Z=r*gamma+(epsilon-1)(r-1),                        (5)
    nu=lambda*r-epsilon,
    h=e*r.                                              (6)

The arithmetic genus in (5) replaces the rational-base formula. It
retains the actual genus of the base and requires no separability
assumption on the degree-`r` map for these intersection identities.

If

    nu>4g_Z+5,                                          (7)

the intrinsic criterion applies. As before, the algebraic surface closure
is not `E`, so it maps birationally to an integral surface `S subset P3`.
For the nef pullback `A` of a hyperplane, `d=A^2.W=deg S>0` and
`A.Z=h`. Thus there must be an integer `d>=1` with

    d<=max_(a integer,a>=1)(2ah-nu*a^2),                 (8)
    (d-1)(d-2)>=e*r*(r-1).                             (9)

Equation (9) is the accepted multiplicity/plane-adjunction argument:
the actual exceptional intersection contains `Z`, so `S` has generic
order at least `r` along `C`. A general plane meets `C` transversely in
`e` distinct points, and blowing up those plane points lowers the
arithmetic genus by at least `e*r*(r-1)/2`. Its integral strict transform
has nonnegative arithmetic genus. The base genus `gamma` does not enter
this plane calculation.

### 3. One numerical condition incorporates the higher-genus cases

By (4)--(6), threshold (7) is exactly

    (2e-3gamma+3-4epsilon)*r+3epsilon-9>0.               (10)

If also

    (e+gamma-1)*r>=epsilon,                             (11)

then `nu>=h`, so the maximum in (8) is attained at `a=1` and gives

    1<=d<=(1-gamma)*r+epsilon.                          (12)

For a>=1 the exact difference from a=1 is
(a-1)[2h-nu(a+1)]<=0. Writing `D=(1-gamma)*r+epsilon`, all formal lifts in this scope therefore
obey the single opposing pair of inequalities

    D>=1,
    (D-1)(D-2)>=e*r*(r-1).                             (13)

The implication uses that (d-1)(d-2) is nondecreasing for positive
integers d: its successive difference is 2(d-1), including d=1,2.
The right side can be positive even when the permitted algebraic degree
`D` is very small. In positive genus, the term `(1-gamma)r` strengthens
the upper bound. Any parameters satisfying (10)--(11) but contradicting
(13) have no all-orders smooth embedded Cartier lift. This states the
general criterion directly instead of splitting it into degree or
root-order profiles.

For `gamma=0`, (10)--(13) recover the accepted rational-base criterion.
For `epsilon=2`, `e>=4`, and `r>=2`, condition (11) holds for every
`gamma>=0`. Whenever (10) holds, every `gamma>=1` is already impossible:
for `gamma=1`, (12) gives `d<=2`, contradicting the positive right side
of (9); for `gamma>=2`, (12) gives `d<=0`. Together with the accepted
rational case, this excludes every smooth movement-two formal root
satisfying the high-self-intersection threshold, regardless of the base
genus, under the specific normal-bundle hypothesis (3).

### 4. Scope retained

This is a necessary condition for an infinite formal first-relation
lift, not an exclusion of every finite-gap supported complete
intersection. The actual-CI-to-root bridge still requires all of its
accepted saturation, joint-leading-generation, smoothness, and generic
initial-regular-sequence hypotheses. No claim is made that (3) holds for
an arbitrary smooth space curve.

The line bundle `M` and its sections are actual data on `C`, not only an
integer degree. The numerical obstruction is uniform in those data,
but it does not construct a finite-type family over varying Picard
schemes or assert a new explicit finite cutoff. The accepted formal
finite-tower theorem was proved for its specified rational-base
coefficient open; transferring its representability and all-order
uniqueness to this larger setting requires stating the corresponding
relative family and cohomology hypotheses.

The arbitrary-characteristic extension is left to the separately reviewed scope statement for the underlying geometric argument. The present note fixes characteristic zero.

### 5. Independently audited movement-one corollary

For a balanced smooth rational space curve of degree `e>=3`, there is
no all-orders smooth root of class `(1,r)` with `r>=2`. Indeed its genus
is zero, `nu=(2e-1)r-1>5`, and `nu>=h=er`. The audited criterion gives
`d<=r+1`, whereas plane adjunction requires

    (d-1)(d-2)>=e*r*(r-1).

The upper bound makes the left side at most `r(r-1)`, contradicting
`e>=3` and `r>=2`. This excludes every first normal order in that family
simultaneously.

For first normal order `r=1` and degree `e>=4`, every all-orders smooth
root of class `(1,1)` is the actual strict-transform germ of a quadric
containing `C` and smooth along `C`. Here `nu=2e-2>5`, so the criterion
gives an integral surface closure of degree at most two. A plane cannot
contain this smooth rational curve: a smooth rational plane curve has
degree at most two. Hence its closure is a quadric `Q`.

The generic order `m` of `Q` along `C` is one. One way to see this
without a classification of quadrics is plane adjunction: `m>=2` would
force `0=(2-1)(2-2)>=e*m*(m-1)>0`. Its strict transform `W` therefore
restricts to an effective divisor on `E=P1 x P1` of class

    (2e-(2e-1),1)=(1,1).

It contains the given integral `Z` in that same class, so `W|E=Z`
scheme-theoretically. Smoothness of this full divisor makes `W` smooth
and transverse to `E` all along `Z`. Thus its formal completion along
`Z` is already the selected formal branch; away from `Z` on `E`, both
divisor ideals are units. Consequently the whole formal divisor on
`Bhat_E` is the strict-transform germ of `Q`, not merely an unspecified
branch of a larger-degree surface. The finite exceptional intersection
also says the ordinary first normal symbol of `Q` is nowhere zero on
`C`, equivalently `Q` is smooth along `C`.

Conversely, a quadric containing `C` and smooth along `C` has normal
order one, and its strict transform has this smooth finite `(1,1)`
root and provides all exceptional lifts. The corollary classifies the
all-orders movement-one roots in this scope; it gives no new explicit
finite cutoff and does not replay the stronger accepted finite-jet
quadric rigidity for `C0`.

## Characteristic boundary

Laurent's characteristic-zero torsion theorem, Mann's rational cyclotomic bound,
trace-radical/nilpotent logarithm construction, and derivative constancy criterion
are used in exactly their stated setting. The argument does not give the same
phase-space decision theorem in positive characteristic. Its need for rational
coefficients is substantive even among characteristic-zero fields. The nef
intersection identities use actual bundles and adjunction and do not require
separability of Z->C, but the formal algebraization/high-self-intersection
argument is imported with its stated characteristic-zero hypotheses; no new
arbitrary-characteristic algebraization or higher-genus finite-tower theorem
is claimed. The [positive-characteristic fixed-quartic constructions](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md)
are separate and consistent with these restricted characteristic-zero methods.
