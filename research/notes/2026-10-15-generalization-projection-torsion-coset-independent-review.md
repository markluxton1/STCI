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
