# Independent audit: regular formal surfaces with singular movement-two roots

Date: 2026-10-19. Reviewer: `regular_singular_smoothing_audit`.

**Outcome: PASS for the precise conditional nonexistence statement below.**
The new smoothing step is valid. It closes the reduced singular-root case
only when the resulting formal surface is regular at every point of the
whole root. The argument does not establish that an arbitrary all-orders
Cartier lift, or an arbitrary actual complete intersection, has this
regularity property. No canonical result has been changed by this audit.

## 1. Exact scope and authority

Work over an algebraically closed field `k` of characteristic zero with the
fixed rational quartic `C0` and the accepted balanced normal bundle
`N_(C0/P3)=O_P1(7)^2`. Put

    B=Bl_(C0)(P3), E=P1_base x P1_direction,
    O_E(E)=O_E(7,-1), H|E=O_E(4,0).

Let `r>=2`, and let `Z` be a **reduced effective Cartier divisor** of class
`(2,r)` on `E`, finite flat of degree `r` under the first projection
`p:Z->P1_base`. Suppose compatible embedded effective Cartier lifts of
`Z` on every exceptional neighborhood define a formal surface `Vhat` that
is **regular along all of `Z`**. Then such a lift does not exist.

The promoted input [STCI-R-0005](../results/smooth_root_formal_obstruction.md)
concerns a smooth full root; its [accepted independent audit](2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit.md)
supplies the algebraic branch, ruled-model degree, and plane-section
arguments used as premises here. This review checks their new interface
with a singular root and supplies the new smoothing argument. It does
not reopen the inherited proof or its accepted numerical inequalities.
[STCI-R-0011](../results/moving_nonreduced_spectral_root_obstruction.md)
is not needed: ampleness and smoothing below hold for every finite-flat
root of the indicated class, including components of differing slopes.

## 2. Normal line, connectedness, and algebraization

Let `u` be an exceptional equation and `g` a local equation of `Vhat`.
Since `g mod u` cuts out the Cartier divisor `Z` in `E`, `u` remains a
nonzerodivisor on `Vhat`, and

    I_Z O_Vhat=(u,g)O_Vhat=(u),
    N_(Z/Vhat)=O_Z(E)=:N=O_Z(7,-1).

Thus the exceptional topology on `Vhat` is its `Z`-adic topology. In
particular it is a closed formal subscheme of `B` completed along `Z`.
Regularity of `Vhat`, rather than smoothness of `Z`, is the hypothesis
that gives a smooth formal surface over the perfect field `k`.

The exact sequence

    0 -> O_E(-2,-r) -> O_E -> O_Z -> 0

and Kunneth show `H0(O_Z)=k`, because `H0(O_E(-2,-r))` and
`H1(O_E(-2,-r))` vanish. Hence `Z` is connected. Each irreducible component
has class `(a,b)` with `0<=a<=2`; finiteness over the first factor gives
`b>=1`. Consequently

    deg(N|component)=7b-a >= 5.

The normal line is therefore ample on `Z`, without any descent or
equal-slope hypothesis. The finite-projection hypothesis matters here:
a vertical fiber of class `(1,0)` would instead have normal degree `-1`.

[Bost, Corollary 3.8, printed p. 188](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf#page=28)
allows a proper connected lci scheme of definition in a smooth formal
scheme and assumes its normal bundle ample; it does not require that
scheme of definition to be smooth. It gives an integral algebraic
closure `W` of dimension two containing the formal branch. The dimension
condition is `dim Z>=1`; the PDF text extraction renders its sign
incorrectly. This is the appropriate variant for singular `Z`.

## 3. Normalization still preserves the entire singular root

At a closed point `z` of `Z`, the maximal-ideal completion of the chosen
formal surface is regular of dimension two. It is a minimal completed
branch of the integral algebraic surface `W`. Excellence identifies the
completed normalization factors of `W` with the normalizations of its
completed branches. The selected branch is already normal and regular.
See [Stacks, Lemma 15.110.8 and its proof](https://stacks.math.columbia.edu/tag/0C2E).

The compatibility argument in the accepted smooth-root audit uses only
normality of the formal surface. On a normal-domain formal chart with
ring `R`, the algebraic coordinate domain of `W` injects into `R` through
the chosen minimal branch. Every element of its finite integral closure
maps into `Frac(R)` and is integral over `R`, hence belongs to `R`.
Uniqueness makes these maps agree on overlaps. The resulting morphism
`Vhat->Wnu` reduces to a section

    Z -> Wnu x_W Z -> Z.

Because normalization is finite, this section is a closed immersion.
Its image is a copy of the original `Z`, including its singularities,
and `Wnu` is regular along it. The formal neighborhood of that image is
the selected branch. This does not identify any additional branch of
`W` with it.

Resolve the projective normalization away from this regular neighborhood,
obtaining a smooth projective surface `T` containing the unchanged
Cartier curve `Z`. Resolution preserving a regular open is available
for surfaces; see [Stacks, Resolution](https://stacks.math.columbia.edu/tag/0BGJ)
and the accepted branch audit cited above. If `S` is the integral image
surface in `P3` and `H` is its hyperplane pullback to `T`, then

    Z^2=deg N=7r-2,   p_a(Z)=r-1,
    H.Z=4r,          H^2=d=deg S>0.

`W` is not `E`, since `u` is nonzero on the formal surface. Thus `W` is
the strict transform of `S` and the map to `S` is birational. `H` is nef.

## 4. Independent cohomology calculation

The divisor sequence tensored by `O_E(7,-1)` is

    0 -> O_E(5,-r-1) -> O_E(7,-1) -> i_*N -> 0.

Push this sequence along the first projection `p_E:E->P1`. Both direct
images of `O_E(7,-1)` vanish, while

    R1(p_E)_* O_E(5,-r-1)=O_P1(5) tensor H1(P1,O(-r-1)).

Since the latter vector space has dimension `r`, this gives the stronger
identity

    p_*N = O_P1(5)^r.                                      (1)

In particular

    H1(Z,N)=0,  H1(Z,N tensor p^*O_P1(-1))=0,
    h0(Z,N)=6r.

For a finite morphism, `p^*p_*N -> N` is surjective: on affine rings it
is the multiplication map `B tensor_A M -> M`. Equation (1) therefore
proves that `N` is globally generated. These assertions do not assume
that `Z` is integral or nonsingular. Equivalently, the two proposed
Kunneth computations have kernels `O_E(5,-r-1)` and
`O_E(4,-r-1)` respectively and give the same vanishings.

## 5. Smoothing on the fixed algebraic surface

This is the new step. Embedded deformations of the Cartier curve `Z` in
the smooth surface `T` have tangent space `H0(N)` and obstruction space
`H1(N)`. Local lifts exist by lifting a regular sequence. Thus the Hilbert
scheme of `T` is smooth at `[Z]`. For a source that explicitly covers a
singular lci subscheme, use [Hartshorne, *Lectures on Deformation Theory*,
Theorem 6.3 and its following remark, and Theorem 9.3](https://math.berkeley.edu/~robin/math274root.pdf#page=42).
The introductory Theorem 1.1 alone assumes a nonsingular subscheme and
would not by itself justify this application.

Choose a smooth integral neighborhood `A` of `[Z]` in the Hilbert scheme,
and let `U subset T x A` be its universal curve. After shrinking `A`, it
is a relative effective Cartier divisor. Locally, the universal ideal
reduces to the principal Cartier ideal `(f)` on the central fiber;
flatness and Nakayama lift its generator to a local equation `F`.
Properness lets these local neighborhoods cover every nearby fiber.
The relative Cartier criterion is [Stacks, Lemma 31.19.9](https://stacks.math.columbia.edu/tag/062Y).

At a closed point `z` of the central `Z`, choose parameters `t_j` on `A`
whose tangent vectors form a basis of `H0(N)`. Modulo the central ideal,
the coefficients `partial F/partial t_j` are precisely the evaluations
of those normal sections. Global generation gives one with nonzero value
at `z`. Hence `F` is not in the square of the maximal ideal of the smooth
ambient `T x A`, and `U` is regular, equivalently smooth over `k`, at `z`.
This also covers the original singular points of `Z`.

The nonsmooth locus of `U` over `k` is closed. Its image in `A` is closed
because `U->A` is proper, and it misses `[Z]`. Shrink `A` again to make
all of `U` smooth over `k`. The generic fiber of `U->A` is regular,
since its local rings are localizations of regular local rings of `U`.
Its field `k(A)` is perfect in characteristic zero, so this generic
fiber is smooth. The nonsmooth locus of the morphism `U->A` consequently
has proper closed image. There is a nonempty open of smooth fibers.
Here one must distinguish smoothness of the total space over `k` from
smoothness of its map to `A`; generic smoothness and properness supply
the latter only over a dense open. For the field-smoothness criterion see
[Stacks, Lemma 33.25.2](https://stacks.math.columbia.edu/tag/04QP).

Since `h0(O_Z)=1`, upper semicontinuity gives `h0(O_(U_a))<=1` near
`[Z]`; the fibers are nonempty, so this equals one. A smooth proper fiber
over algebraically closed `k` is therefore connected and integral.
See [Stacks, Lemma 36.32.1](https://stacks.math.columbia.edu/tag/0BDN).
Thus a nearby smooth connected curve `Z_a subset T` exists. The universal
Cartier family over connected `A` makes it algebraically equivalent to
`Z`, so

    Z_a^2=7r-2,   g(Z_a)=r-1,   H.Z_a=4r.                 (2)

No claim that this smoothed curve lies on the original exceptional
divisor, or that it yields a new embedded formal lift in `B`, is needed.
Its only role is to permit the established ruled-surface numerical
argument on `T` with the invariants (2).

## 6. Numerical contradiction and boundary

For `r>=2`,

    7r-2 > 4(r-1)+5.

Apply the accepted high-self-intersection and nef-divisor argument to
`Z_a subset T`. [Hartshorne, *Curves with high self-intersection on
algebraic surfaces*, Theorem 4.1](https://www.numdam.org/item/PMIHES_1969__36__111_0.pdf#page=12)
gives the ruled model near this smooth curve; the accepted intersection
argument gives

    d <= max_(a integer >=1) [8ra-(7r-2)a^2] = r+2.        (3)

For the opposing bound, use the **original** `Z`, not its smoothing.
Formal containment in `W` reduces modulo `u` to scheme-theoretic
containment `Z subset W|E`. The difference is effective on the smooth
surface `E`. Its generic fiber degree shows that the generic
multiplicity `m` of `S` along `C0` satisfies `m>=r`. Extra exceptional
components or other branches can only add effective fiber degree.
The accepted general-plane-section argument now gives

    (d-1)(d-2) >= 4m(m-1) >= 4r(r-1).                   (4)

But (3) gives `(d-1)(d-2)<=r(r+1)`, and

    4r(r-1)-r(r+1)=r(3r-5)>0  for every r>=2.

This contradiction passes the proposed exclusion.

The added hypothesis is regularity of the **whole formal surface**.
At a singular point of the reduced root, smoothness of the ambient
threefold and the Cartier property of the formal equation alone do
not imply it. If the formal equation is locally `g=f+u*a+...` with
`df=0` on `E`, regularity requires a nonzero linear contribution in
the transverse direction, for example `a(z)!=0`. The audit does not
prove that contribution exists for every root lift. Singular formal
surfaces remain outside this theorem, as do arbitrary actual complete
intersections without a bridge to the stated formal object.

The proof of Sections 2--6 in fact does not use reducedness once a
finite-flat effective Cartier `Z` of class `(2,r)` and a regular formal
surface are supplied: the component ampleness criterion, sequence (1),
and universal-family smoothing still apply. This is a transparent
scope strengthening of the argument, not a claim that nonreduced roots
in the actual STCI problem satisfy its regularity hypothesis.

## Review record

The reviewer independently reconstructed the normalization and smoothing
interfaces and both cohomology calculations. A separate subreviewer,
`smoothing_check`, checked the Hilbert universal-family argument and the
primary deformation, relative Cartier, and semicontinuity references.
No exact-CAS calculation, inherited proof rerun, canonical promotion,
or git operation was used. The regularity boundary is unresolved by
this argument and must survive any later result promotion.
