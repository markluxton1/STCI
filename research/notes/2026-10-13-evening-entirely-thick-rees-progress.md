# Entirely thick presentations: full conormal filtration and socle budget

Date: 2026-10-13. Status: **PROVED necessary structure, pending independent
audit**. This note gives a theorem about the entire complete-intersection
thickening, at every normal order. It does not exclude all entirely thick
presentations and does not resolve the STCI problem. No novelty claim is made.

## 1. Reconstructed frontier and retained boundaries

The current audited record is `research/AUDITED_STATE_2026-10-07.md`, updated
through October 12. The characteristic-zero curve

    C0 = [s^4:s^3 t:s t^3:t^4]

has normal bundle `O_P1(7)^2`. Every integral quartic carrier is now excluded
in characteristic zero, with arbitrary mate degree. The unresolved global
branches include higher-degree order-one carriers and entirely thick pairs.

The October 6 independent thick audit proves, for degrees `a,b` and exact
generic normal orders `p,q`, the first blowup restriction

    W = (u,v),
    u = 7ab/4 + 7pq - 4(aq+bp),
    v = ab/4 - pq,
    u >= 0, v >= 0, a >= 3p, b >= 3q.

At `a=3p,b=4q`, its support consists of constant sections and the quadric
residual binary form has at most `min(p,q)` distinct ruling roots. The
entire `a=3p,b=3q` boundary is already excluded by `u<0`.

The branch inventory recovered the live remote branch
`research/entirely-thick-rees-valuation`, commit
`a843888ce15b06247c576f8f717bec6b7ef5a352`, into
`research/validation/2026-10-13-evening-branch-inventory/remote-snapshots/`.
Its October 7 notes contain the generic Noether cluster reformulation,
the relative blowup budget, marked-root countershields, and the proof of
power saturation in degrees `d>=3m`. Direct inspection verified the
quadric exact sequence and the saturation proof in
`2026-10-07-rational-quartic-power-saturation.md`: there is no hidden
ordinary-power correction at or above degree `3m`.

The recovered notes deliberately reject a comparison between generic
exceptional-cycle coefficient and special repeated-root multiplicity.
This note retains that rejection. The higher data used below is the full
`I_C`-adic algebra of the complete intersection, together with its global
dualizing sheaf. It requires neither constant tangent roots nor clean
normalization/conductor hypotheses.

## 2. A theorem for any smooth support curve

Let `C` be a smooth integral projective curve in `P3` over an algebraically
closed field. Write its degree as `e` and genus as `g`. Let

    Y = V(F_a,G_b),  Y_red = C.

The two surfaces have no common surface component. Thus `Y` is a pure
one-dimensional Cohen--Macaulay Gorenstein complete intersection. Put

    J = I_C O_Y,
    A = O_(Y,eta),
    n = length A = ab/e,
    d = max { j : (J_eta)^j != 0 }.

Here `eta` is the generic point of `C`. The integer `d` is the actual
generic Loewy index of the full thickening; it is not the order of either
chosen equation. Write

    h_j = dim_(k(C)) (J_eta)^j/(J_eta)^(j+1),
    M = sum_(j=0)^d j h_j,
    L_j = J^j/J^(j+1).

Let `T_j` be the torsion subsheaf of `L_j` as an `O_C`-module, and
`B_j=L_j/T_j`. Then `B_j` is a vector bundle of rank `h_j`. Torsion in
these quotients is allowed and must be retained.

Choose a positive real number `lambda` such that every torsion-free
quotient `V` of `Sym^j N_(C/P3)^*` satisfies

    deg V >= -j lambda rank V                    (S)

for every `j>=0`. One elementary sufficient choice is `lambda=deg A0`
for a positive-degree line bundle `A0` with `N_C^* tensor A0` globally
generated: all symmetric powers after twisting by `A0^j` are then
globally generated. Thus the theorem has a choice of `lambda` for every
smooth support curve. In characteristic zero the standard slope theorem
also permits `lambda=mu_max(N_C)`; for semistable `N_C`, this is
`deg N_C/2`. The quartic application below uses its explicit split
normal bundle and does not depend on the slope theorem.

Define

    L = e(a+b-4) - (2g-2),
    Delta_j = deg B_j + j lambda h_j + length T_j,
    Delta = sum Delta_j,
    Asym = nd - 2M.

Then all the following hold:

1. `J^(d+1)=0` on all of `Y`.
2. The global socle along the support is the line bundle

       S_C(Y) = Ann_(O_Y)(J)
              = Hom_(O_Y)(O_C,O_Y)
              = omega_C tensor O_C(4-a-b).

3. `J^d` is a line bundle on `C` and there is an effective divisor `D`
   with

       J^d = S_C(Y)(-D).

4. `Sym^j N_C^*` surjects onto `L_j` for every `j`; hence
   `Delta_j>=0`.
5. The generic Gorenstein algebra satisfies `Asym>=0`.
6. The exact global budget is

       n(lambda d - L) = lambda Asym + 2 Delta.   (B)

In particular

       lambda d >= e(a+b-4) - (2g-2).            (N)

The effective top-socle defect is visible more precisely as

       deg D <= lambda d - L.

These assertions are independent of any upper bound on the degrees,
normal orders, or higher contact lengths. They apply equally to thick
and order-one presentations of a smooth support curve.

## 3. Proof: purity and the actual socle

Since `Y` is Cohen--Macaulay of pure dimension one and has only the
irreducible support `C`, the only associated point of `O_Y` is `eta`.
Every subsheaf of `O_Y` supported on finitely many closed points is zero.
The sheaf `J^(d+1)` is generically zero, so it is zero everywhere. This
does not assert that the quotients `L_j` are torsion free: a quotient of
a pure sheaf may have zero-dimensional torsion.

For the finite closed immersion `i:C->Y`, duality gives

    Hom_Y(O_C,omega_Y) = omega_C.

Since `omega_Y=O_Y(a+b-4)` is invertible, tensoring this identity by its
inverse gives the stated socle isomorphism. One can obtain the same
identity by the change-of-rings computation of
`Ext^2_(P3)(O_C,omega_(P3))` through the regular sequence `(F,G)`.
Its degree is

    deg S_C(Y) = 2g-2-e(a+b-4) = -L.

The ideal `J^d` is annihilated by `J`, and thus is a subsheaf of this
socle. The generic Artin algebra `A` is Gorenstein and has a
one-dimensional socle; its nonzero highest power `(J_eta)^d` lies in
that socle and therefore equals it. Consequently `J^d` is a rank-one
subsheaf of the socle line bundle. On the smooth curve it is locally
free and has the form `S_C(Y)(-D)` for an effective divisor `D`.

In particular the Loewy index at the generic point is a global
nilpotency bound, but special points can still contribute precisely
through the torsion of intermediate quotients and through `D`.

## 4. Proof: conormal quotients and Euler characteristic

The regular embedding `C->P3` gives

    I_C^j/I_C^(j+1) = Sym^j N_C^*.

Passing to `O_Y` therefore yields a surjection onto `L_j`. Composing
with `L_j->B_j` and applying (S) shows that

    deg B_j + j lambda h_j >= 0.

This proves `Delta_j>=0`, including the torsion length. For `j=d`,
`L_d=J^d` is torsion free and rank one, so

    -L - deg D = deg J^d >= -lambda d,

which gives the top-socle inequality directly.

Riemann--Roch on the support curve and additivity for the filtration
give

    chi(O_Y)
       = sum_j [deg B_j + length T_j + (1-g)h_j]
       = Delta - lambda M + n(1-g).

The complete-intersection genus formula gives

    chi(O_Y) = -ab(a+b-4)/2 = -ne(a+b-4)/2.

Combining them yields the exact relation

    2 Delta = 2 lambda M - n L.                  (E)

## 5. Proof: a Frobenius inequality retaining all higher jets

Choose a coefficient field in the completed generic Artin algebra; this
has residue field `K=k(C)`. Since `A` is Artin Gorenstein, choose a
`K`-linear functional nonzero on its socle. The multiplication pairing
defined by that functional is perfect. For every ideal `U` of `A`,

    dim_K Ann_A(U) = n - dim_K U.

With `m=J_eta`, the identity `m^(d+1)=0` gives

    m^(d-i+1) subset Ann_A(m^i),

and hence

    dim m^i + dim m^(d-i+1) <= n,  1<=i<=d.

Summing over `i` and using

    sum_(i=1)^d dim m^i = sum_j j h_j = M

gives `2M<=nd`. No symmetry of the Hilbert function was assumed:
the associated graded algebra of an Artin Gorenstein algebra can fail
to be Gorenstein. Formula (B) now follows from (E), with
`Asym=nd-2M>=0`.

This is the first-moment consequence of the classical symmetric
decomposition of a local Artin Gorenstein Hilbert function, but the
short pairing proof above avoids assuming that its individual layers
are symmetric.

## 6. Specialization to C0: an integral defect identity

For `C0`, take `lambda=7`, `e=4`, `g=0`. Then

    n=ab/4,
    mu=7d+14-4(a+b),
    Delta_j=deg B_j+7j h_j+length T_j.

The theorem becomes

    n mu = 7 Asym + 2 Delta,
    mu >= 0,
    0 <= deg D <= mu.                           (C0)

Every `Delta_j` is a nonnegative integer. This couples three genuinely
different measurements of the full thickening:

- its generic nonhomogeneous Gorenstein Hilbert function (`Asym`);
- global degree/torsion defects of all normal layers (`Delta`);
- the actual top socle line and its special-point divisor (`D`).

This is more information than the first blowup cycle. It is still a
necessary condition: large Loewy index is permitted, and the local
families already showing unbounded higher contact remain consistent
with it.

## 7. Equality rigidity: a constant graded Artin algebra

Suppose `mu=0`. The identity forces `Asym=0` and every `Delta_j=0`.
Consequently `T_j=0` and `deg B_j=-7j h_j` for all `j`. The bundle
`L_j(7j)` is a globally generated vector bundle of degree zero on `P1`,
so it is trivial. Thus

    L_j = O_P1(-7j) tensor B_j^0

for constant vector spaces `B_j^0` of dimension `h_j`.

After these twists, every multiplication map has constant coefficients:
it is a map between trivial bundles on the complete connected curve
`P1`. The surjections from `Sym^j N_C^*` also have constant matrices.
Therefore there is a graded Artin quotient `B` of `k[x,y]` with

    gr_J(O_Y) = direct_sum_j O_P1(-7j) tensor B_j.

At the generic point, equality in the summed Frobenius inequalities
forces equality in each individual inequality:

    m^(d-i+1) = Ann_A(m^i),  1<=i<=d.

The resulting pairings

    (m^i/m^(i+1)) x (m^(d-i)/m^(d-i+1)) -> m^d

are perfect. This proves that the associated graded algebra, and hence
the constant algebra `B`, is Gorenstein. In the entirely thick branch,
its embedding dimension is two. A graded Artin Gorenstein quotient of
`k[x,y]` is a homogeneous complete intersection, say of degrees `r,s`.
Thus equality imposes the exact relations

    ab = 4rs,
    d = r+s-2,
    4(a+b) = 7(r+s).                            (R)

The degrees `r,s` are the degrees of generators of the full initial
ideal, not necessarily the normal orders `p,q` of the chosen pair.
For example, a cancellation between chosen equations can expose the
second generator at a higher normal order. Identifying `(r,s)` with
`(p,q)` would discard the very higher-jet phenomenon this theorem
retains.

Equality is therefore a rigid boundary with a constant Gorenstein
normal algebra. This does not imply that the filtered algebra itself
is constant, or that its embedded formal neighborhood splits. Those
would require further extension/embedding arguments.

## 8. Explicit remaining equality data and limitations

The smallest thick degree pair surviving the old scalar inequalities is
`(a,b,p,q)=(6,8,2,2)`. Here `n=12` and the new theorem requires `d>=6`.
If `d=6`, equality forces a constant graded complete intersection of
degrees `(r,s)=(2,6)` and no normal-layer torsion or degree defects.
The alternative factorization `(3,4)` has socle degree five and is
incompatible with `d=6`.

This is an exact dichotomy for the full `(6,8)` thickening:

1. a very rigid constant graded `(2,6)` algebra at Loewy index six; or
2. a higher Loewy index with the defect budget in (C0).

Neither branch is excluded here. At equality the original two quadratic
symbols can be scalar multiples of the same constant quadratic
direction; their scalar coefficients can have complementary zero
divisors. Their cancellation produces the degree-six initial generator.
One must not assume that a global regular change of the original
homogeneous generators realizes that cancellation.

The result supplies no uniform bound on `d` or on `a,b`. It introduces
no tangent-only multiplicity cap, no generic-to-special root comparison,
and no assumption that the graded algebra is Gorenstein away from the
equality boundary.

## 9. Continuation targets

The useful next step is to analyze the full filtered deformation of the
constant graded complete intersection on the equality boundary, or to
bound the allowable global defect `Delta` using actual homogeneous
generation. This is a structural theorem before any computation.

For `(6,8)`, compare the global exact generator filtration

    0 -> O(-42) -> O(-24) + O(-32) -> O(-14) -> 0

suggested by a graded `(2,6)` model, with the actual sextic normal-image
constraints and the global embedded filtered deformation. The exact
sequence is a proposed next bridge, not established in this note.

For larger degrees, retain the entire nonnegative budget rather than
enumerating first symbols: every candidate generic Hilbert function
must satisfy its exact arithmetic, and every special-point repair must
pay the corresponding degree/torsion defect. There is no finite generic
Hilbert-function classification claimed uniformly in the degrees.

## 10. Provenance and standard inputs

The proof above derives the numerical budget and equality statement
directly. Standard inputs were checked against primary sources:

- Stacks Project, [regular immersions, Lemma 31.22.5](https://stacks.math.columbia.edu/tag/0638),
  for the symmetric conormal associated graded of a regular embedding.
- Stacks Project, [Duality for curves](https://stacks.math.columbia.edu/tag/0E31),
  and [finite-morphism duality, Remark 48.20.12](https://stacks.math.columbia.edu/tag/0AX4),
  for the actual socle line via the finite closed immersion.
- Iarrobino and Macias Marques,
  [Symmetric Decomposition of the Associated Graded Algebra of an Artinian
  Gorenstein Algebra](https://arxiv.org/abs/1812.03586), for the literature
  context behind nonhomogeneous Gorenstein Hilbert functions. Its
  symmetric-decomposition theorem is not needed for the elementary
  pairing proof in Section 5.

Memory was used only to route the higher-jet failure shield and the
existing first-normal-transverse boundary, then replaced by current
repository inspection: `/Users/markluxton/.codex/memories/MEMORY.md`,
lines 164--171. The older checkout-specific canonical state was not
transferred here. The memory rollout id is
`01a02fb1-2af7-7fa3-897c-9d6527951ac9`.
