# A uniform conductor contact graph for Cartier normalization lifts

Date: 2026-10-14. Owner: `global_phase_duality`. Status: **NEW WRITTEN
STRUCTURAL THEOREM; independent review requested**. The accepted
[Cartier-lift classification](2026-10-14-generalization-cartier-lift-independent-audit.md),
[projective contact criterion](2026-10-14-generalization-projection-contact-phase-criterion.md),
and its uniform fiber-degree bound are premises, not computations to replay.
The new input is the actual canonical conductor ideal from the
[conductor--Jacobian bridge](2026-10-14-generalization-projection-conductor-jacobian-bridge.md).

## 1. General theorem

Let `nu:S->X subset P3` be a finite birational normalization of an
integral degree-`a` hypersurface over an algebraically closed field of
characteristic zero. Let `C subset X` be a smooth degree-`d`, genus-`g`
curve with full reduced inverse image a
single smooth ample Cartier curve `c`, mapped isomorphically to `C`.
Assume `X` is regular at the generic point of `C`. The Cartier-lift
lemma makes `S` regular along `c`. Put `H=nu*O_X(1)` and `k=c^2`.

Finite duality identifies the **actual** upstairs conductor ideal with
`omega_S tensor nu*omega_X^(-1)`. A normal surface is Cohen--Macaulay,
and its canonical sheaf is rank-one reflexive. Thus the conductor is
the divisorial ideal of an effective Weil divisor `B`:

    conductor O_S = O_S(-B),
    B ~ (a-4)H-K_S,
    N := B.c = d(a-4)+k-(2g-2).                    (1)

This statement identifies the actual ideal, not only its double dual;
there is no discarded zero-dimensional ideal defect. Globally `B`
need not be Cartier. It is Cartier near `c`, because `S` is regular
there, and this is enough to define `B|c` and its degree. Adjunction
near `c` proves the formula for `N`. If `S` is Gorenstein, `B` is
Cartier globally.

Write its effective Weil divisor as `B=sum_i m_i D_i`, with the `D_i`
distinct prime curves and `m_i>=1`. No `D_i` equals `c`, because the
normalization is an isomorphism at the generic point of `C`. Then

    sum_i m_i (D_i.c) = N.                          (2)

Every `D_i.c` is a strictly positive integer since `c` is ample.
Consequently:

* There are at most `N` prime conductor curves, and each generic
  conductor multiplicity `m_i` is at most `N`.
* If `D_i^nor` is the normalization of `D_i`, the sum of the vanishing
  orders of `c` on all its branches is `D_i.c`. Thus every such branch
  contact order, and the number of branches meeting `c`, is at most
  `N`; their sum with weights `m_i` is exactly `N`.
* The exact first-symbol bridge is

      Z(F_1) = B|c + A,                             (3)

  where `A` is the entire zero divisor of the normalization normal
  differential. In particular (2) concerns the full conductor contact,
  including multiplicities, rather than only its reduced support.

Here `F_1` is the actual first normal symbol of the carrier equation.
Identity (3) is conditional on the new bridge proof; the contact graph
bounds (1)--(2) use finite duality directly and do not depend on (3).

## 2. A bound on the entire off-diagonal pair correspondence

For every image conductor curve `Delta subset X`, let

    K=k(Delta),    E=product_(i over Delta) E_i,
    E_i=k(D_i),   d_Delta=sum_i [E_i:K].

The accepted fiber-degree argument gives `d_Delta<=a`. Characteristic
zero makes each extension separable. Fix a prime `D_i` over `Delta`.
The reduced generic algebra of all pairs with first entry on `D_i` is

    E_i tensor_K E,

of rank `d_Delta` over `E_i`. Its diagonal component is one factor
`E_i`, of rank one. Removing it leaves total rank `d_Delta-1`.
Normalizing and taking projective closures therefore gives finitely
many integral off-diagonal pair curves `T`, with finite first projection
`p_1:T->D_i`, satisfying the exact equality

    sum_(T with first image D_i) deg(p_1) = d_Delta-1 <= a-1. (4)

This includes conjugate pairs on one irreducible conductor curve as
well as pairs between different conductor curves. When `E=K` there
are no off-diagonal curves, consistent with (4). Generic nilpotents
are deliberately absent from this pair construction, but are retained
in the conductor divisor `B` and in the final full descent condition.

Pullback of the Cartier divisor `c` to each proper normal curve `T`
has total degree `deg(p_1)(D_i.c)`. Summing (4) over all first images
and then using (2) gives the uniform bound

    sum_T deg(p_1*c)
      = sum_i (d_(image D_i)-1)(D_i.c)
      <= (a-1) sum_i D_i.c
      <= (a-1)N.                                    (5)

The index `T` in (5) means the integral components of the **ordered**
off-diagonal pair correspondence. In particular a component invariant
under exchange is counted once as an integral component, rather than
being artificially doubled. The equality is the decomposition of
the finite algebra over each fixed first image, so there is no missing
conjugate-pair degree or extra factor of two.

Because `c` is ample, every `p_1*c` is a nonzero effective divisor.
Hence (5) bounds all of the following by `(a-1)N`: the number of pair
components, the number of their contact branches counted with
multiplicity, and any single contact order on their normalizations.
These quantities were not bounded by the size of the degeneracy
support alone.

## 3. The three surviving fixed-C0 models

The accepted normal splitting `N_C0/P3=O(7)^2` and transverse theorem
place every conductor contact in the support of `A`, whose degree
is at most five or six. Equations (1)--(5) supply the additional
global weighted bounds:

| Normalization and polarization | `B` class | `N=B.c` | `deg A` bound | Ordered pair contact budget |
| --- | --- | ---: | ---: | ---: |
| `P1 x P1`, `H=(2,2)`, `c=(1,1)` | `(10,10)` | 20 | 5 | 140 |
| Quadric cone, `H=2c`, `c` a smooth conic | `10c` | 20 | 5 | 140 |
| `P2`, `H=4h`, `c=h` | `51h` | 51 | 6 | 765 |

The quadric cone is Gorenstein, and `c` avoids its vertex. Thus its
global conductor class is Cartier and its local contact calculation
occurs entirely in the smooth locus. No resolution at the vertex is
being silently inserted.

These inequalities put the incidence into finitely many **combinatorial
weighted contact graph types**. Vertices can record the at most five or
six sites on `c`, the prime conductor branches and their positive
integer weights. Edges record ordered pair branches and their positive
contact orders, with total edge weight bounded by 140 or 765. The
actual curves, contact locations, correspondence maps and leading
coefficients still vary in families. Finitely many graph types do not
mean finitely many projection parameters or finitely many phase values.

## 4. Consequence for the general strategy and retained boundaries

The accepted projective criterion requires, on every pair curve `T`,
equality of the entire divisors `p_1*c` and `p_2*c`, followed by a
root-of-unity test on the resulting constant ratio. The new theorem
bounds the amount of integer contact data needed to formulate these
tests uniformly on each normalization model. It does not require
enumerating possible mate powers.

There is still no bound here on the order of a split scalar phase.
Even one edge with contact order one can carry an arbitrary-order
root of unity in the local split model. Canonical conductor duality
constrains that edge's integer contact data, not its scalar label.
The entire nilpotent logarithmic conductor defect must also vanish;
the reduced correspondence and (1)--(5) do not prove this vanishing.

The theorem applies more generally to any smooth ample Cartier lift
on a normal projective-hypersurface normalization, with the uniform
quantity `N` in (1). Global Gorensteinness is unnecessary: the actual
reflexive conductor ideal and smoothness along `c` suffice. For
non-Cartier lifts the contact divisor needs replacement; for a lift
through singular points of the normalization the local bridge needs
replacement; and for carriers generically
singular along `C`, the conductor can contain `c`, so its restriction
in (2) is not defined as an effective finite divisor. Those strata
are not covered by this theorem. It does not resolve the universal
integral-curve STCI problem or the unrestricted fixed-C0 problem.

No accepted certificate was rerun and no large CAS job was launched.
