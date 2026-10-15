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

