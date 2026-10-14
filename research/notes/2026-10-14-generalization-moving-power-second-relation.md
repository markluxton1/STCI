# A moving power forces degeneration of the next coprime relation

Date: 2026-10-14. Status: **NEW PROOF; independent audit requested**.
This is a global relation-bundle obstruction, uniform in the two
hypersurface degrees. Accepted normal-layer defect identities and the
accepted movement-gap cost are premises. No previously verified
computation is rerun.

## 1. Hypotheses and the second-relation quotient

Let `C` be a smooth integral projective curve in characteristic zero, with
balanced conormal bundle

    E=N_C^*=H^-1 tensor V,  dim V=2.

Let `M subset V tensor O_C` be a moving line subbundle, with
`e=-deg M>0`, and put `W=H^-1 tensor M`, `L=E/W=H^-1 tensor M^-1`,
after fixing the constant determinant of `V`.

For an embedded thickening let `K_j` be its actual degree-`j` initial
relation sheaf inside `Sym^j E`. Suppose the first generic relation is
`m^r`, `r>=2`, where `m` spans `M`. Suppose the next independent generic
relation has degree `s>r`, is unique modulo first-relation multiples, and
is coprime to `m`. These hypotheses hold when the full generic initial
ideal is the binary regular sequence `(m^r,g_s)` with `r<s`. They are
stronger than merely saying that the next relation is independent: a
relation divisible by `m` is not covered by the coprimality assumption.

First assume the first actual relation is saturated, so `K_r=W^r`.
Its products give the saturated bundle

    P_s=W^r tensor Sym^(s-r)E subset Sym^s E.

Set `g=s-r`. The quotient is, by the characteristic-zero apolar
annihilator calculation,

    A_s=Sym^s E/P_s
       =H^-s tensor M^-(g+1) tensor Sym^(r-1)V.            (1)

It has rank `r`. This identity is proved in
[the moving-power tower](2026-10-14-generalization-moving-power-obstruction-tower.md).

Since `K_s` contains `P_s`, its image in `A_s` is a rank-one actual
relation sheaf `T`. It is torsion-free on the smooth curve and hence a
line bundle, although its inclusion into `A_s` can fail to be saturated.
Evaluation on the quotient normal direction `L` gives a nonzero map

    T -> L^s.                                               (2)

The generic coprimality assumption is exactly what makes (2) nonzero.
Write its effective zero divisor as `D`. Then

    T=L^s(-D)=H^-s tensor M^-s(-D).                         (3)

Combining (1) and (3), the actual nonzero inclusion `T -> A_s` belongs to

    H^0(M^(r-1)(D)) tensor Sym^(r-1)V.                      (4)

Since a line bundle of negative degree has no nonzero global section,
(4) proves the uniform necessary inequality

    deg D >= (r-1)e.                                       (5)

This is a payment at the first coprime independent relation. It remains
present even when the sole-first-relation obstruction groups vanish in
all preceding normal orders.

## 2. A full graded CI in every fiber is impossible

If the full graded algebra has a binary complete-intersection initial
ideal of the same degrees `(r,s)` at every fiber, then the second relation
is coprime to `m` in every fiber. Thus (2) is nowhere zero and `D=0`.
Equation (5) is impossible for `r>=2` and `e>0`.

Consequently:

> On a smooth integral projective curve with balanced split conormal, a
> moving pure-power first relation of order at least two cannot be the
> first generator of a uniform fiberwise graded binary complete
> intersection with a unique later generator.

This statement concerns the **full graded initial algebra in every
fiber**. It does not assert that the ordinary embedded algebra cannot be
locally a complete intersection. Its associated graded algebra can
degenerate at special points. It also does not cover `r=1`: then the
quotient in (1) has rank one and (4) imposes no movement penalty.

## 3. The exact normal-layer defect at the new relation

For the rational balanced case put `C=P1`, `H=O(lambda)`. Let `F_j`
denote the torsion-free quotient of the actual normal layer, and let
`U_j` denote its torsion. The accepted defect convention is

    Delta_j=deg F_j+lambda*j*rank F_j+length U_j
           =-deg K_j-lambda*j*rank K_j.                   (6)

The final expression includes all torsion; it does not identify the
actual layer with its free quotient.

In the saturated-first-relation case, `P_s subset K_s`, and
`K_s/P_s=T`. The degrees in (1)--(3) give

    rank K_s=g+2,
    deg P_s=-lambda*s*(g+1)-r e*(g+1),
    deg T=-lambda*s+s e-deg D.

Therefore (6) gives the exact identity

    Delta_s=e*g*(r-1)+deg D,                              (7)

and (5) implies

    Delta_s >= e*(r-1)*(g+1).                             (8)

Here is the explicit torsion accounting. Write the saturation of `T`
inside `A_s` as `T_sat`, with

    T=T_sat(-E_s),  eta=deg E_s,
    T_sat=L^s(-D_sat).

Then `D=D_sat+E_s`. The actual degree-`s` normal layer has torsion of
length `eta`, while its free quotient is `A_s/T_sat`. Its free degree
in (6) contributes `e*g*(r-1)+deg D_sat`; adding the torsion contributes
`eta` and recovers (7). Thus no special-point length is omitted. The
nonzero map `T_sat -> A_s` also implies
`deg D_sat >= (r-1)e`, so (8) is not obtained merely from failure of the
actual image to saturate.

The earlier movement-gap theorem gives

    sum_(r<=j<s) Delta_j = r e*g*(g+1)/2

when the first actual relation is saturated. Adding the new order gives

    Delta >= r e*g*(g+1)/2 + e*(r-1)*(g+1).                (9)

For `C0`, the accepted full socle budget consequently strengthens to

    n mu >= 7 Asym
              +r e*g*(g+1)+2e*(r-1)*(g+1).              (10)

This is a necessary inequality. It does not bound all possible Loewy
indices or exclude every entirely thick presentation.

## 4. Retaining a divisor in the first relation

The argument also retains a nonsaturated first actual relation. Suppose

    K_r=W^r(-D_0),  delta_0=deg D_0,

with the same generic pure-power direction and same next coprime rank-one
relation. The saturation `P_s` above still exists, and

    P_s(-D_0) subset B_s=K_s intersect P_s subset P_s.

Set `tau=length(P_s/B_s)`, so `0<=tau<=(g+1)delta_0`.
The rank-one image `T=K_s/B_s subset A_s` again has the form (3) and
satisfies (5). Exactness now gives

    Delta_s=e*g*(r-1)+deg D+tau.                          (11)

If `T=T_sat(-E_s)` as above, the torsion in the actual normal layer has
length `tau+eta`. Indeed there is an exact sequence

    0 -> P_s/B_s -> Sym^s E/K_s -> A_s/T -> 0,

and the free quotient is `A_s/T_sat`. Over each local discrete valuation
ring the free quotient splits off, so the two finite lengths add.
Thus (11) includes every torsion contribution.

Using the accepted previous-order gap cost, one obtains

    Delta >= r e*g*(g+1)/2+delta_0
                 +e*(r-1)*(g+1),                        (12)

and for `C0`

    n mu >= 7 Asym+r e*g*(g+1)
                   +2delta_0+2e*(r-1)*(g+1).             (13)

The movement degree of the first degree-`r` binary relation is
`epsilon=r e`, rather than `e`. Both degrees are specified here to avoid
conflating the moving direction with the binary-relation map.

## 5. The minimum payment has a geometric support restriction

At equality in (5), `M^(r-1)(D)` has degree zero and a nonzero section,
so it is the trivial line bundle. Under (1), the inclusion in (4) is
therefore a fixed vector of the constant space `Sym^(r-1)V`.
The dual of evaluation (2), after cancelling the common line factors,
is the Veronese map of the annihilator direction of `m`. Consequently
the minimum divisor `D` is the pullback of the zero divisor of one
constant binary form of degree `r-1` under the direction map
`C -> P(V)`, followed by the constant determinant identification with
the dual projective line. Every multiplicity is retained.

This describes the equality support at the relation-bundle level.
It does not assert that every such divisor comes from an embedded
complete-intersection thickening.

## 6. Provenance and audit status

Accepted inputs:

- [Normal-layer and socle budget](2026-10-13-evening-entirely-thick-rees-progress.md).
- [Movement-gap cost audit](2026-10-14-generalization-moving-relation-gap-cost-independent-audit.md).

New structural input:

- [Moving-power quotient and obstruction tower](2026-10-14-generalization-moving-power-obstruction-tower.md).
- [Independent tower audit](2026-10-14-generalization-moving-purepower-tower-independent-audit.md).

An independent review of this note's second-relation evaluation and
exact torsion-inclusive defect formulas has been requested. This note
must not be promoted beyond its written audit status until that review
is complete.

The first-relation tower and the new payment address different stages:
movement can eliminate first-relation cohomology obstructions, while
the next coprime relation must then degenerate somewhere. The remaining
research question is whether the exact global socle identity and the
later relation filtration force a contradiction after retaining all
such degeneration divisors.

No memory file, external source, large CAS computation, or commit was
needed for this new proof.
