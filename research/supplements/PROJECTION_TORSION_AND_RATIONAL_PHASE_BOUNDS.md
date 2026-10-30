# projection torsion and rational phase bounds

Permanent complete mathematical dossier with exact assumptions, projection and torsion calculations, phase restrictions, arbitrary-base scope and limitations preserved.

---

## 2026-10-15-generalization-projection-torsion-coset-reduction

# Full conductor phase spaces and finite torsion-coset envelopes

Date: 2026-10-15. Owner: `conductor_torsion_geometry`.
Status: **NEW STRUCTURAL THEOREM; independent review passed** in the
[written independent review](2026-10-15-generalization-projection-torsion-coset-independent-review.md).
The accepted conductor, Cartier-lift, contact-divisor, and conductor-budget
theorems are premises. No accepted proof or computational certificate has
been rerun. This note supplies the family-specialization details needed by
the pending [finite-phase proposal](2026-10-14-generalization-projection-finite-phase-space.md),
then isolates the remaining arithmetic geometry by Laurent's theorem.
It does not exclude or construct a mate in any of the three fixed-C0
projection families.

## 1. Statement: one finite-type family replaces every mate power

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
degree-sixteen plane models, with `H=2c,2c,4c` respectively. Their actual
projection-family equations remain to be supplied. No non-Cartier lift,
multiple inverse lift, higher-degree inverse lift, or arbitrary normal
surface family is added to the accepted classification.

## 2. Why the family uses the actual normalization on every stratum

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

## 3. Full conductor quotients survive specialization

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
[actual-conductor duality formula](2026-10-14-generalization-projection-conductor-budget-independent-review.md)
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

## 4. The logarithmic defects are bounded algebraic equations

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
algebra. Refine by ranks and chosen nonzero minors to obtain its basis.
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

## 5. Constancy, phases, and the finite cover

Let `chi_rho(Z)` be the characteristic polynomial of multiplication by
`rho` on the etale `F`-algebra `D_A`. Since `k` is algebraically closed,

```
rho torsion iff every root of chi_rho is in mu_infinity(k). (7)
```

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

## 6. Laurent's theorem gives a finite torsion-coset envelope

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

## 7. Exact bounded-or-unbounded alternative for least mate degrees

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

## 8. Scope and the next bridge

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



---

## 2026-10-15-generalization-projection-torsion-coset-independent-review

# Independent review of the full conductor torsion-coset reduction

Date: 2026-10-15. Reviewer: `phase_family_audit`.
Result: **PASS, after the small corrections recorded below.**

Reviewed the complete [theorem note](2026-10-15-generalization-projection-torsion-coset-reduction.md).
The accepted conductor, Cartier-lift, contact-divisor, and conductor-budget
results were treated as premises. No accepted proof, inherited certificate,
or CAS computation was rerun. A separate `etale_matrix_check` independently
checked the finite-algebra construction and the torsion-coset/degree step.

## 1. The family-specialization bridge passes

The revised argument retains the actual fibre image by flattening
`B/O_X`, then spreads a common ideal `J` and preserves the quotient
inclusions by flatness. It does not require formation of the largest
conductor to commute with specialization. Membership modulo a smaller
common ideal is exact.

The essential repair to the earlier proposal is now explicit: choose
Noether normalization on the entire generic affine quotient algebra and
spread its monic finiteness equations **before** tensoring with `k(x)`.
Every one-dimensional fibre component of an algebra finite over `R[x]`
dominates `A1_k`, so that tensoring retains every generic conductor curve,
with its complete Artinian algebra and all nilpotent layers. Finite
presentations and a polynomial denominator whose specialization stays
nonzero ensure that the specialized matrices are the actual localized
fibre quotients. Recursion on the closed parameter complement is finite.
Zero-dimensional support may disappear because the accepted
Cohen--Macaulay generic-to-global theorem supplies global descent.

The generic-`C` quotient models separately give a uniform threshold
`M>=1`; `Q` is nilpotent on their upstairs factors, with exponent bounded
by the finite matrix dimension. Thus the argument does not infer a
threshold over `C` from reduced contacts or from off-`C` models alone.

The note's additional explicit thresholds also pass. The accepted
actual-conductor duality formula does not use generic regularity along
`C`: that hypothesis enters the separate exclusion of `c` as a conductor
component. For `r=ord_c(B)`, the effective divisor `B-r c` has nonnegative
intersection with ample `H`. Consequently `r<=10` in both quadric
models and `r<=51` in the plane model. Since `ord_c(Q)=2,2,4`, actual
conductor membership holds for every exponent at least `5,5,13`.
These explicit thresholds may replace `M` in the degree bound, including
on the generically singular boundary. They bound the actual conductor,
not an arbitrary smaller auxiliary ideal `J`.

## 2. The exponent-free algebraic locus and finite phase cover pass

For finite commutative `F=k(x)`-algebras `A subset B`, the compatible
canonical etale splittings and finite logarithm give

```
u^n in A iff w in N_A and rho^n=1,
rho=(v tensor 1)/(1 tensor v) in (E tensor_K E)^*.
```

The inclusion `K -> E` is faithfully flat even for products, so its
equalizer gives the displayed exact criterion. The least exponent, when
it exists, is the order of `rho`. The canonical-subalgebra compatibility
is also stated in [Stacks, Section 15.107](https://stacks.math.columbia.edu/tag/0CKQ).

Trace ranks, primitive-element basis determinants, discriminants, finite
Newton lifting, and logarithms produce bounded rational-matrix equations
on finitely many strata. In particular the nilpotent equations specialize
correctly. Coefficientwise `partial_x f=0` imposes constancy in
characteristic zero. The root-ordering algebra is finite and surjective;
repeated roots and products of models introduce no defect. Padding by
ones gives one fixed torus and preserves exact phase order.

## 3. The constructible torsion-coset envelope and degree dichotomy pass

Laurent's theorem is used only for the finite torsion-coset covering of a
closed torus subvariety. Its statement and attribution were checked in
the cited [primary-author account, Section 5, pp. 217--218](https://www.numdam.org/item/AST_1991__198-199-200__209_0.pdf).
For a locally closed piece `U_i` of `W`, intersecting each covering coset
with `U_i` gives a relatively open subset contained in the actual image.
Discarding empty intersections preserves the deleted admissibility and
nilpotent boundary. Torsion density then gives exactly the asserted
finite closed envelope. The transfer from the complex theorem to any
algebraically closed characteristic-zero field is valid: use a finitely
generated coefficient field, its algebraic closure, and an embedding into
`C`; torsion cosets are defined by integer characters and roots of unity.

Under the stated hypothesis `Q in H^0(S,H)`, every degree-`b` mate pulls
back to a scalar multiple of `Q^b`: intersection with `H` fixes its
divisor multiplicity to be `bm`, and proper normality makes the ratio a
scalar. Thus every mate degree is divisible by its phase order `e`.
Every multiple of `e` at least `M` descends. This proves both the exact
minimum when the carrier is generically regular along `C` and the
general bound `b_min <= e ceil(M/e)`.

The complete degree-set refinement also follows: all positive multiples
of `e` at least the actual-conductor threshold `M` occur, and the only
remaining possibilities are finitely many actual descents below `M`.
Thus `e>=M` implies `b_min=e` without generic regularity along `C`.
The numerical thresholds `5,5,13` apply here as above.

A positive-dimensional retained torsion coset supplies realized torsion
tuples of unbounded order, hence unbounded **least** mate degrees on
actual carriers. Zero-dimensional retained cosets supply finitely many
orders; the uniform threshold bounds all least mate degrees. Repeated
parameterizations of a fixed carrier cannot create this unboundedness,
because each realized phase order is at most that carrier's least mate
degree.

## 4. Corrections and scope

Three small corrections were applied during this review:

- Generic affine quotient charts of dimension zero or with empty support
  are omitted after shrinking so they have no fibre curves; the closed
  complement is still treated recursively. This avoids attempting
  one-variable Noether normalization on a zero-dimensional algebra.
- The threshold is explicitly chosen `M>=1`, including when no conductor
  component lies over `C`.
- The optional claim that an arbitrary section of `H^(b_0)` permits
  multiplication of **least** mate degrees by `b_0` was removed. It needs
  a primitive Cartier-ray hypothesis. For example on a smooth quadric,
  `Q=L^2` for a hyperplane section has phase order one, but `L` already
  supplies a degree-one mate. The main theorem assumes base degree one
  and is unaffected.

No remaining mathematical blocker was found within the stated bounded
family scope. This is a structural existence theorem, not an effective
construction of `W` or its torsion cosets, and not a decision about any
of the three actual fixed-C0 projection families. It neither expands the
accepted Cartier-lift classification nor resolves the unrestricted
fixed-C0 or universal projective-curve STCI problem.


---

## 2026-10-15-generalization-effective-rational-phase-bound

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



---

## 2026-10-15-generalization-effective-rational-phase-bound-independent-review

# Independent review: effective rational phase images

Date: 2026-10-15. Reviewer: `mann_bound_audit`.
Verdict: **PASS for the new effective theorem, with the descent and
degenerate-case clarifications recorded below incorporated in the note.**

Reviewed:
[Effective rational phase images: Mann partitions and finite mate bounds](2026-10-15-generalization-effective-rational-phase-bound.md).
The [full-conductor phase-space theorem](2026-10-15-generalization-projection-torsion-coset-reduction.md)
and its existing independent review are accepted premises. This audit
does not replay their proofs or their computations. It checks the new
rational descent, finite arithmetic construction, order estimates,
constructible boundary certificate, and resulting mate-degree bound.
No actual phase image, Mann partition list, or boundary-containment
list was enumerated, and no CAS computation or old proof check was
performed. The finite algorithm is established as a mathematical
procedure, with no claim that it has been run on these families.

## 1. Rational descent and the meaning of the image

The fixed normalized models, fixed coordinate sections of `C0`, section
spaces, restriction maps, and lift kernels are defined over `Q`.
Rational bases and lifts therefore give the full prescribed projection
families over `Q`. This concerns the whole family, not a subfamily
obtained by fixing transcendental coefficients.

The accepted phase construction can retain that field of definition.
On a `Q`-defined integral parameter stratum with coordinate ring `A`,
use `K=Frac(A)` and perform the generic matrix and normalization choices
over `K(x)`. Such a stratum need not be rational or geometrically
integral; no identification `K=Q(T)` is needed. Coefficients of the
finitely many rational functions can be represented in localizations
of `A`. Denominators involving `x` retain their zero-locus treatment
from the accepted construction; merely localizing `A` would not make
those polynomials invertible at every point. Exceptional coefficient
and rank strata must also remain in the finite construction.

Primitive-element choices apply to the relevant finite separable
reduced residual algebras. They do not imply that the full nonreduced
conductor algebra is monogenic. Keeping its bases, multiplication
matrices, and nilpotent equations avoids that unsupported inference.
All algebraic root orderings or splitting choices must remain as
variables and incidence equations, with all allowed choices present.
Selecting one geometric branch over `Qbar` and discarding conjugate
choices would not justify the stated descent. The corrected note makes
these distinctions explicit.

Chevalley's theorem then gives a constructible geometric image over
`Q`. An explicit constructible presentation can use `Q`-defined closed
sets and their closed boundaries without passing to geometrically
irreducible components. This is the image on geometric points, not an
assertion that images of `Q`-rational points exhaust `W(Q)`.

The field-extension assertion is correct. A torsion tuple `zeta` is
defined over `Qbar`. Its phase fibre is finite type over `Qbar`.
Nonemptiness after an algebraically closed extension implies
nonemptiness before extension by faithful flatness, and a nonempty
finite-type scheme over `Qbar` has a `Qbar`-point. Conversely, a
`Qbar`-point persists after extension. Thus the realized torsion tuples
and their orders are unchanged. This does not descend each particular
transcendental carrier that originally realized a tuple.

## 2. Imported arithmetic statement and partition coverage

I independently opened Evertse's
[author's version, Section 2, p. 3](https://pub.math.leidenuniv.nl/~evertsejh/98-roots.pdf).
It states the homogeneous rational form of Mann's theorem needed here:
a nondegenerate relation of length `s` has all root ratios annihilated
by the product of primes at most `s`. The cited published article is
J.-H. Evertse, *Acta Arithmetica* 89(1) (1999), 45--51,
[DOI 10.4064/aa-89-1-45-51](https://doi.org/10.4064/aa-89-1-45-51).
The page reference is to the author's version. Mann's original
bibliographic reference is supplied in the note; this audit did not
read his original full text.

At a torsion zero of each rational Laurent polynomial, the support
can be partitioned into minimal vanishing blocks. The normalized root
ratios for a block of size `s` belong to `mu_P(s)`, hence to `mu_q`
for `q=P(S)`, where `S` is the largest displayed support size.
Enumerating all support partitions and all assignments in that finite
cyclotomic group therefore covers every torsion zero.

The converse needed by the construction also holds: a retained
assignment makes every block sum vanish identically on its associated
binomial solution set. Thus that entire set, including its nontorsion
points, lies in `Y`. Minimality need not be checked again during
enumeration. Extra nonminimal assignments cannot add points outside
`Y`. Coefficient cancellations are removed before support sizes are
measured, and monomial equations are correctly recognized as empty
torus loci.

All tests in this stage are finite exact operations in an explicit
cyclotomic field. The note claims termination, not practical speed.
The rational coefficient hypothesis is essential to this particular
primorial formula; `X-zeta_N` over `Q(zeta_N)` gives the stated
counterexample to a field-independent reuse of the same bound.

## 3. Consistency, Smith normal form, and connected components

An assignment of roots to generating rows must first respect every
integer relation among those rows. This is exactly the requirement
that it induce a homomorphism `L -> mu_q`. The note correctly rejects
inconsistent systems. There are finitely many generating relations
to test, obtainable by integer linear algebra.

For a consistent system, Smith normal form and the corresponding
integer torus automorphism yield

```
y_i^(s_i)=theta_i,   theta_i in mu_q,   s_1 | ... | s_r.
```

Every connected component fixes those first `r` coordinates and leaves
the others free. Choosing the free coordinates equal to one gives a
representative whose order divides `q s_r`: each fixed coordinate is
annihilated by `q s_i`, and all those integers divide `q s_r`.
Unimodular monomial changes preserve point order. The equality
`s_r=exp(L^sat/L)` is the correct lattice invariant.

This bounds a chosen representative of every component. It bounds
every point only when the component has dimension zero. A positive-
dimensional component has torsion points of arbitrarily large order;
the review found no confusion between these statements in the note.

## 4. The sharp minor bound and its numerical interpretation

After the separate monomial shifts, a support of total degree at most
`d` lies in `d Delta_D`. Thus every character difference lies in
`d(Delta_D-Delta_D)`, including differences coming from different
partition blocks. Projecting to any selected `r` coordinates preserves
this containment.

Multilinearity expresses each selected determinant as a convex
combination of determinants with rows `d(e_i-e_j)`, allowing `e_0=0`.
After removing the factor `d^r`, these are reduced directed-incidence
matrices. Their square determinants have absolute value at most one:
expand along a row with at most one nonzero entry, or, if every row
has two opposite entries, use the zero column sum. Therefore every
rank-`r` minor has absolute value at most `d^r`.

The gcd of the nonzero maximal minors equals `s_1 ... s_r`, so

```
s_r <= s_1 ... s_r <= d^r.
```

The binomial chain in the note proves sharpness. Its determinant is
`d^r`, while for every smaller size the shifted consecutive minor is
`+/-1`. Its Smith invariants are consequently `(1,...,1,d^r)`, and
primitive `d^r`-th roots give points of that exact order. A separate
independent arithmetic subaudit confirmed this argument.

For a zero-dimensional coset, `r=D`; hence
`ord(zeta)<=P(S)d^D`. The draft expressly treats this as a numerical
upper bound. It does not incorrectly infer divisibility by
`P(S)d^D`. Its common-exponent alternative using an lcm is valid.
The monomial-count bound `S<=binomial(D+d,D)` is also valid after the
support shifts.

## 5. Constructible boundary and the three outcomes

For each connected coset `K` contained in `Y_i`, containment
`K subset B_i` is equivalent to the vanishing of every defining
equation of `B_i` after restriction to `K`. A computed monomial
parameterization or membership in the binomial prime ideal over its
computed cyclotomic field gives an exact finite test.

If containment fails, `K minus B_i` is nonempty open in the irreducible
coset `K`. Torsion is Zariski dense in `K`, so this piece has torsion
points; when `dim K>0`, their orders are unbounded because only
finitely many ambient torus points have bounded order. If `dim K=0`,
the retained piece is its one point. Thus the finite list has exactly
the torsion points of the actual constructible set, with its deleted
boundary retained in the certificate.

The three alternatives are exhaustive. No surviving piece certifies
no torsion. A surviving positive-dimensional coset certifies
unbounded phase orders. Otherwise finitely many point cosets survive,
each with the explicit numerical bound. The dimension of the closed
set `Y_i` alone is not used; isolated torsion points inside a curve are
captured by full-rank binomial systems. The example `x+y=1` is
consistent with this distinction.

The mate interpretations of these alternatives use the accepted exact
phase obstruction, including the fact that every mate degree is a
positive multiple of the phase order. They do not follow from torsion
density alone.

## 6. Mate bound and degenerate cases

For a nonempty finite surviving torsion set, let `B` bound its orders.
The accepted effectivity premise gives

```
b_min <= e ceil(M/e),   1<=e<=B.
```

For positive integers `e,M`, the least multiple of `e` at least `M`
is at most `M+e-1`. Therefore `b_min<=B+M-1`. The substitutions
`M=5,5,13` yield `B+4,B+4,B+12`. Using the exact finite set of point
orders gives the sharper maximum stated in the note. If no point
survives, nonexistence is the conclusion and no empty maximum or
mate-degree bound is needed.

The incorporated conventions close the remaining edge cases:

- With no remaining equations, `S=0`, `q=P(0)=1`, and the single
  empty binomial system is the whole torus.
- The degree parameter is `d=max(1, shifted degrees)`, with `d=1`
  when the equation list is empty.
- A nonzero monomial or constant equation makes the torus locus empty.
- Rank zero uses the trivial finite-group exponent one.
- For `D=0`, the ambient torus has its one point of order one;
  preprocessing and the boundary test decide whether it survives.

## 7. Limits of this PASS

This is a proved effective reduction for an explicitly supplied
`Q`-constructible phase image, conditional on the accepted geometric
phase theorem used as a premise. It provides a finite algebraic and
cyclotomic certificate procedure and explicit order/mate bounds once
the image equations and boundary are known. It supplies neither those
equations nor numerical values of their degrees and supports for the
three actual families. It does not compute a surviving torsion phase,
exclude any entire actual family, or settle the unrestricted fixed-C0
or universal STCI question. The contact budgets alone are not promoted
to numerical phase-image bounds.

No further mathematical correction is required within this stated
scope. The note remains a new independently reviewed result awaiting
the ordinary repository integration of its proof and this review.

## 8. Addendum: the Section 9 meta-effectivity corollary

Verdict: **PASS for the explicit fixed-three-model input stated in
Section 9.** This addendum audits algorithmic accessibility of the
accepted geometric construction, not its geometric proof again.

The strengthened statement is justified by more than the abstract
existence of a finite-type phase space. It specifies finite rational
polynomial/section/module input and supplies the following effective
chain.

- On a `Q`-prime parameter piece, computations over
  `K=Frac(R)` and `K(x)` are exact and decidable from a presentation
  of `R`. The piece need not be a rational variety.
- The three fixed source section rings have explicit finite normal
  graded presentations. Image equations, finite-module relations,
  syzygies, annihilators and common ideals are therefore computations
  in presented polynomial/module data. The finiteness hypotheses are
  those of the accepted admissible normalization charts.
- Noether coordinates, finite bases and reduced separable primitive
  elements can be found by exact algorithms or by dovetailed searches
  for finite certificates. The accepted generic existence assertions
  guarantee eventual success. No class-group oracle is introduced.
- Spreading also controls the relevant module exact sequences. The
  monic module Groebner basis argument is valid: retaining both basis
  generation directions and the Buchberger reductions, and then
  clearing their finitely many coefficient denominators, gives a
  monic basis after localization. Its standard module monomials are
  free over the localized parameter ring. Applying this to the
  relevant cokernels preserves fibre kernels and inclusions. Clearing
  displayed matrix entries alone would not prove that assertion.
- Primary decomposition of `V(h)` gives finitely many computable
  `Q`-prime components of strictly smaller dimension. Recursing on
  all of them yields a finite tree and retains every exceptional
  stratum. The conductor quotient's monic finiteness identities and
  its denominator zero loci remain subject to the accepted full
  construction.
- Effective algebraically closed field quantifier elimination gives
  the geometric constructible image, including its open conditions;
  computing its closure alone would be insufficient. The already
  audited Mann/SNF/boundary procedure then terminates on that image.

I also independently opened the Derksen--Kemper primary paper linked
in Section 9. Its Theorem 2.13 and Algorithm 2.14 explicitly compute
a generic-freeness localization using a Groebner basis over the
fraction field, on pp. 2114--2115. That displayed result concerns a
domain ring inclusion. The note correctly gives its own monic module
argument for the more general module and base-change control needed
here, rather than attributing that entire argument to the displayed
ring-only algorithm.

There is consequently no additional unproved algorithmic bridge in
the proposed composite procedure within this precise input scope.
It is legitimate to state an in-principle terminating decision
algorithm from the explicit projection-family input, rather than
requiring a phase-image presentation as a separate input. The output
decides existence of any mate-admitting carrier and distinguishes
unbounded least mate degrees from the finite-bound case. The
geometric implications continue to use the accepted phase theorem
as a premise.

No such composite algorithm has been run here. This addendum gives
no practical complexity estimate, equations for an actual phase
image, numerical bound for the three whole families, or decision
which alternative holds for those families. No CAS or accepted-proof
replay was performed.


---

## 2026-10-15-generalization-nef-formal-branch-arbitrary-base

# Nef polarizations bound formal surface branches over arbitrary smooth curves

Date: 2026-10-15. Author: `formal_algebraization_route`.
Status: **SCOPE GENERALIZATION; targeted independent audit passes**.
The [independent scope audit](2026-10-15-generalization-nef-formal-branch-arbitrary-base-independent-audit.md)
passes the intrinsic nef formulation, exact normal-bundle hypothesis,
new genus/degree expressions, and resulting numerical criterion.
The separate [movement-one audit](2026-10-15-generalization-movement-one-formal-roots-independent-audit.md)
also passes the new corollary in Section 5.
The independently audited branch-algebraization/ruled-surface argument in
[smooth-root formal nonexistence](2026-10-15-generalization-smooth-root-formal-nonexistence.md)
is a premise. This note isolates its intrinsic form and computes the new
genus and degree expressions when the base curve is not rational. It does
not replay that proof or any accepted CAS certificate.

## 1. The underlying geometric criterion is independent of the blowup

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
in (2). This repackaging requires neither a rational base curve nor a
blowup presentation. The condition `d>0` is automatic for ample `A`.

For a merely nef `A`, its square on the algebraic surface closure may
vanish; no positive-degree contradiction may then be inferred. A general
nef line bundle need not define a contraction or a morphism.
The blowup application below proves positivity separately.

The imported primary inputs are [Bost, Theorem 3.5 and Corollary 3.8](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf)
and [Hartshorne, Theorem 4.1, with the neighborhood-equivalence definition
in Section 0](https://www.numdam.org/item/PMIHES_1969__36__111_0.pdf).
Their exact hypotheses and the branch-normalization details are covered
by the [accepted full audit](2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit.md).

## 2. Apply it over a smooth curve of any genus

Let `C subset P3` be smooth of degree `e` and genus `gamma`. Assume the
actual normal bundle has the form

    N_(C/P3)=L direct_sum L,     deg L=lambda.            (3)

This is a specific vector-bundle hypothesis. Equal numerical slopes,
semistability, or a decomposition into two line bundles of the same
degree do not imply (3). Equivalently, the associated projective bundle
must be trivial as a `P1`-bundle **over `C`**.

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

## 3. One numerical condition incorporates the higher-genus cases

By (4)--(6), threshold (7) is exactly

    (2e-3gamma+3-4epsilon)*r+3epsilon-9>0.               (10)

If also

    (e+gamma-1)*r>=epsilon,                             (11)

then `nu>=h`, so the maximum in (8) is attained at `a=1` and gives

    1<=d<=(1-gamma)*r+epsilon.                          (12)

Writing `D=(1-gamma)*r+epsilon`, all formal lifts in this scope therefore
obey the single opposing pair of inequalities

    D>=1,
    (D-1)(D-2)>=e*r*(r-1).                             (13)

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

## 4. Scope retained

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

The arbitrary-characteristic extension is left to the separately
reviewed scope statement for the underlying geometric argument. The
present note fixes characteristic zero. No accepted theorem or
computation was replayed, and no canonical record or commit was changed.

## 5. Independently audited movement-one corollary

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


---

## 2026-10-15-generalization-nef-formal-branch-arbitrary-base-independent-audit

# Independent targeted audit: nef polarizations and arbitrary base genus

Date: 2026-10-15. Reviewer: `g3_branch_uniqueness`.

**Verdict: PASS for the stated new characteristic-zero scope.** This is a targeted review of the new intrinsic formulation, vector-bundle hypothesis, adjunction and degree formulas, passage to inequality (13), and conditional movement-two consequence. The already audited branch-algebraization, normalization, ruled-neighborhood, square-comparison, and plane-multiplicity arguments are premises and were not re-audited. No CAS computation or accepted verifier was rerun.

Reviewed artifact: [nef formal branches over arbitrary bases](2026-10-15-generalization-nef-formal-branch-arbitrary-base.md).

Reviewed SHA-256:

`9f37b173480e1e933702ead3fb53f0fe8bd3e68c073f26db00a083269d221984`.

## Intrinsic nef-polarization statement

The repackaging in Section 1 is valid. For the resolution `f:T->W` supplied by the imported branch lemma, the pullback `H=f^*(A|W)` is nef and satisfies `H.Z=A.Z=h` and `H^2=A^2.W=d` by projection. These are exactly the numerical inputs used by that lemma; no rational base or blowup presentation is used in them. Its ruled-model nef class has integer fiber degree `a>=0`. If `a=0`, its square is zero, contradicting the square comparison when `d>0`; hence `a>=1`. Thus the imported bound applies without an additional positivity assumption on the ambient nef line bundle.

The condition `d>0` is essential and is correctly retained. An ample `A` satisfies it on every integral surface. For merely nef `A`, no contradiction is claimed when `d=0`. The sentence about contraction is only an example of vanishing square; a general nef line bundle need not define a contraction. This does not affect the stated criterion.

## Exact normal bundle and new intersection formulas

The actual isomorphism `N_(C/P3)=L direct_sum L` is the correct hypothesis. The distinction from numerical balance in Section 2 is necessary. Conversely, a trivialization of `P(N)` over `C` makes its relative degree-one tautological bundle of the form `Q boxtimes O(1)`; relative pushforward recovers two identical line summands, with duals adjusted to the projectivization convention. Thus the stated equivalence with triviality as a `P1`-bundle over `C` is valid.

The Euler sequence gives `deg(T_P3|C)=4e`; the tangent sequence then gives `deg N=4e-(2-2gamma)`. Under the exact direct-sum hypothesis this yields

`lambda=2e+gamma-1`.

On `C x P1`, divisor intersections are

`(M boxtimes O(r))^2=2epsilon*r`,

`K_E.Z=r(2gamma-2)-2epsilon`.

Adjunction gives

`2g_Z-2=2epsilon*r+r(2gamma-2)-2epsilon`,

which is equivalent to the stated

`g_Z=r*gamma+(epsilon-1)(r-1)`.

Since `O_E(E)=L boxtimes O(-1)`, its degree on `Z` is `lambda*r-epsilon`; the hyperplane restriction is pulled back from a line bundle of degree `e` on `C`, so its degree on `Z` is `e*r`. Equations (4)--(6) are therefore correct. The formulas use the actual line bundles and intersection numbers, not a separability argument.

The accepted plane-multiplicity argument extends to this setting without a change: its number of imposed plane points is the degree `e` of `C`, and the root's fiber degree remains `r`. The genus of `C` does not appear in it.

## Numerical deductions and inequality (13)

Direct substitution gives

`nu-4g_Z-5=(2e-3gamma+3-4epsilon)*r+3epsilon-9`,

and

`nu-h=(e+gamma-1)*r-epsilon`.

Thus (10) and (11) are exactly the stated conditions. When `nu>=h`, for every integer `a>=1`,

`[2ah-nu*a^2]-[2h-nu]=(a-1)[2h-nu(a+1)]<=0`.

Consequently the maximum occurs at `a=1`, with value

`D=2h-nu=(1-gamma)*r+epsilon`.

The passage from the existence of an integer `1<=d<=D` satisfying (9) to (13) is correct, including the small-degree cases. All quantities are integers, and `P(k)=(k-1)(k-2)` is nondecreasing on the positive integers: `P(k+1)-P(k)=2(k-1)>=0`. In particular `P(1)=P(2)=0`. Therefore `P(D)>=P(d)>=e*r*(r-1)`. The separate requirement `D>=1` is necessary and is explicitly present. Inequality (13) is used only as a necessary condition, as it should be.

For `epsilon=2`, `e>=4`, and `r>=2`, condition (11) follows from `(e+gamma-1)r>=6>2`. Assuming (10), `gamma=1` gives `1<=d<=2`, incompatible with the positive right side of (9). For `gamma>=2`, `D=2-(gamma-1)r<=0`, contradicting `d>=1`. The positive-genus movement-two corollary is therefore valid with its high-self-intersection condition retained.

## Scope of this pass

This pass establishes no existence claim for curves with normal bundle `L direct_sum L`, no arbitrary-characteristic extension, no actual-CI exclusion beyond the imported bridge hypotheses, and no finite-tower representability or uniqueness statement over higher-genus Picard parameter spaces. Section 4 correctly preserves all of these boundaries. The original research problem is not concluded by this scope extension.
