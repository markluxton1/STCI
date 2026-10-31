# A moving power forces degeneration of the next coprime relation

Status: **Proved and independently reconstructed under the hypotheses below.** The current proof retains the audit's determinant factors, torsion accounting, arbitrary-curve degree identities and gap-one scope.
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
[the moving-power tower](MOVING_POWER_AND_SPECTRAL_ROOTS.md#2026-10-14-generalization-moving-power-obstruction-tower).

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

The degree identities (6), (7) and (11), including their torsion accounting, hold on any smooth projective support curve with lambda=deg H in the balanced constant-V setting. The subsequent numerical C0 socle budget has its additional fixed-curve hypotheses. The next relation can occur with gap g=s-r=1; no assumption g>=2 is made.

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

The independent reconstruction retains an additional nonnegative old-multiple term. With tau=length(P_s/B_s) as in(11), one has the sharper combined bounds

    Delta >= r*e*g*(g+1)/2+delta_0+e*(r-1)*(g+1)+tau,
    n*mu >= 7*Asym+r*e*g*(g+1)+2*delta_0
            +2*e*(r-1)*(g+1)+2*tau.

They follow by retaining tau in the exact degree-s identity rather than discarding it. If the first actual relation is saturated then tau=0. Constant det(V) factors may be fixed once as at the start; without that choice the quotient A_s has det(V)^(g+1) and Hom(T,A_s) has det(V)^(1-r), both of degree zero. This accounts for the independent audit's determinant convention and leaves every numerical bound unchanged.

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

- [Normal-layer and socle budget](SOCLE_AND_LOEWY_BOUNDS.md#source-2026-10-13-evening-entirely-thick-rees-progressmd).
- [Movement-gap cost audit](MOVING_POWER_SECOND_RELATION.md#source-2026-10-14-generalization-moving-relation-gap-cost-independent-auditmd).

New structural input:

- [Moving-power quotient and obstruction tower](MOVING_POWER_AND_SPECTRAL_ROOTS.md#2026-10-14-generalization-moving-power-obstruction-tower).
- [Independent tower audit](MOVING_POWER_AND_SPECTRAL_ROOTS.md#2026-10-14-generalization-moving-purepower-tower-independent-audit).

The independently reconstructed proof retained here establishes the second-relation evaluation, exact torsion-inclusive degree
identity and the combined defect bound under their stated hypotheses.
The full written proofs, rather than agreement alone, establish these claims.

The first-relation tower and the new payment address different stages:
movement can eliminate first-relation cohomology obstructions, while
the next coprime relation must then degenerate somewhere. The remaining
research question is whether the exact global socle identity and the
later relation filtration force a contradiction after retaining all
such degeneration divisors.

---

## Source: 2026-10-14-generalization-first-relation-pole-budget-independent-audit.md

# Independent review of the constant-relation pole budget

Date: 2026-10-14, America/New_York. Reviewer: root.
Status: **PROVED under the explicit hypotheses below**. This reviews new
Section 6 of [the thick extension](RELATION_LIFTING_AND_GAP_COSTS.md#source-2026-10-13-generalization-thick-equality-extensionmd).
The previously accepted quadratic transition and apolar annihilator
classification are inputs; their calculations were not repeated.

## 1. Hypotheses and verdict

Work in characteristic zero on fixed
`C0=[s^4:s^3t:st^3:t^4]`, with `N_C0=O(7)^2`. Let `Q` be an actual
embedded ideal defining a thickening, and write

```
K_j = ker(Sym^j N_C0^* -> gr_j(O_Y)).
```

Suppose the first generic relation has degree `r`, its generic direction
is a constant nonzero binary form `f`, and there is no independent
relation in degree `r+1`. Suppose its actual line sheaf is

```
K_r = O(-7r) f(-D),  D effective, delta=deg D.
```

The conclusion is correct: the section cutting out `D` annihilates the
accepted primitive-triple obstruction `h_m` for **each** linear factor
`m` of `f`. This retains the multiplicity of every factor and the full
special-point divisor; it does not discard poles or claim the generic
direction is constant in other cases.

## 2. Saturation is the crucial step

The generic degree-`r+1` relation space is `f V`, where `V=k^2`.
The constant subbundle `O(-7(r+1)) tensor f V` has a locally free
quotient in the ambient symmetric conormal bundle. Composing the
inclusion of `K_(r+1)` with that quotient gives a generically zero
map from a vector bundle to a vector bundle on an integral smooth
curve. It is zero everywhere. Therefore every actual next-order
relation lies in the saturated constant span `f V`, even where
`K_(r+1)` has a modified lattice.

It is consequently legitimate to test a lifted degree-`r` generator
in the quotient `W=Sym^(r+1)V/f V`. No assertion that the actual
relation lattice equals its saturation is needed.

## 3. The obstruction has the stated twist

Choose local normal coordinates and a local generator `h` of the
divisor ideal of `D`. A lift of the initial relation `h f` changes in
next normal order by `h D_ambient(f)`. Differentiating `h` under
motion of the support coordinate contributes a multiple of `f` times
a linear normal coordinate. Changing the scalar gluing unit has the
same form. Both contributions vanish in `W`. Local next-order
corrections change the resulting cocycle by a coboundary.

The correction bundle is intrinsically

```
Hom(K_r, O(-7(r+1)) tensor W) = O(D-7) tensor W.
```

Thus the necessary obstruction is the image of the quadratic ambient
transition class under multiplication by the global section of
`O(D)` cutting out `D`, in `H^1(O(D-7)) tensor W`. This explains the
positive divisor twist, rather than merely assigning it by analogy
with the linear case. On `P1`, this is `H^1(O(delta-7)) tensor W`.

## 4. Factor extraction and consequences

Write `f=m^t H(m,ell)` with `H(0,1)!=0`. The coefficient functional
extracting `m^(t-1) ell^(r+2-t)` vanishes on `f V`, so it defines a
constant map from `W` to `k`. The Leibniz rule sends the obstruction
to

```
t H(0,1) D h_m.
```

Both scalar factors are nonzero in characteristic zero. An actual
embedded lift therefore requires `D h_m=0` for every factor `m`.

The imported apolar classification gives the following necessary
conditions uniformly in `r`:

- `delta<=1` is impossible.
- At `delta=2`, `f` is a power of one pure endpoint direction and
  `D` is its doubled endpoint.
- At `delta=3`, `f` is still a power of one direction. A mixed
  `m=U+theta V` requires exactly `D=div(st(t+2theta s))`;
  an endpoint requires its doubled endpoint plus one point.
- If `f` has two distinct factors, `delta>=4`.

These use the established facts that a mixed direction has no
annihilator below degree three and a unique degree-three annihilator,
while the endpoints require divisibility by their respective squared
coordinates. Distinct mixed directions have distinct degree-three
divisors, and a mixed degree-three divisor has only simple endpoint
zeros. A divisor annihilating both endpoints has degree at least four.
No accepted rank calculation was rerun.

This theorem is necessary structure. It does not assert existence
of any remaining power relation, control higher obstructions, handle
moving binary directions, or exclude positive-defect STCI
presentations. In positive characteristic the factor multiplicity
`t` can vanish, so the argument is not transferred there.

---

## Source: 2026-10-14-generalization-moving-relation-gap-cost-independent-audit.md

# Independent audit: movement and saturation of the first normal relation

Date: 2026-10-14. Reviewer: root. Status: **PROVED** under the stated
balanced-normal and generic relation-rank hypotheses. This reviews new
Section 7 of [the thick extension](RELATION_LIFTING_AND_GAP_COSTS.md#source-2026-10-13-generalization-thick-equality-extensionmd).
It does not replay a previously accepted statement or computation.

Let `N_C=H tensor k^2` on a smooth integral projective curve, and let
the unique first generic initial relation have degree r. Write its
saturated line bundle and actual relation line as

```
W=H^-r tensor A^-1,    K_r=W(-D).
```

Here A is the pullback of `O(1)` by the projective binary-relation
direction map, so it is globally generated. Put `epsilon=deg A>=0`
and `delta=deg D>=0`. Let s>r be the next independent generic
relation degree. For every r<=j<s, the generic relation space is
the first relation times all normal forms of degree j-r.

Multiplication by a nonzero binary form on every fiber is injective.
Consequently

```
A_j=W tensor Sym^(j-r)N_C^*
```

injects into `Sym^j N_C^*` with constant fiber rank and locally free
cokernel. Its image is saturated. Since its generic span equals
that of K_j, it is exactly the saturation of K_j. Products of actual
degree-r relations give the other inclusion, hence

```
A_j(-D) subset K_j subset A_j.
```

Set `t_j=length(A_j/K_j)`. On a curve the inclusions give

```
0<=t_j<=(j-r+1)delta,   t_r=delta.
```

Since `rank A_j=j-r+1` and its degree is
`-(j-r+1)(j deg H+epsilon)`, the exact kernel/quotient degree formula
gives

```
Delta_j=(j-r+1)epsilon+t_j.
```

This retains the torsion of the actual normal-layer quotient. Summing
these identities, and using nonnegativity of the other layer defects,
proves

```
Delta >= epsilon(s-r)(s-r+1)/2 + delta.
```

For C0 the accepted exact socle budget therefore gives

```
n mu >= 7 Asym+epsilon(s-r)(s-r+1)+2delta.
```

No generic Gorenstein associated graded hypothesis is needed for this
inequality. A moving direction has epsilon>=1; a constant direction
has epsilon=0. On the constant branch, the separately accepted pole
constraints apply when s>=r+2. If s=r+1, the next independent relation
can absorb the quadratic obstruction; no such pole lower bound is
claimed there. This qualification was requested during review.

Thus movement pays a quadratic cost in the gap before the next
independent relation, while saturation pays its effective-divisor
cost. These are necessary global compatibility constraints and do not
bound all carrier degrees or all possible Loewy indices. The separate
moving-base differential operator in the owner note is a new exact
reduction with its own evidence; it is not used in this proof.

## Positive-characteristic reach of the pure-power mechanism

The apolar quotient formula in a **fixed total degree at mosts** has the same proof in characteristicp>s: every factorial in the ordinary symmetric pairing is a unit. Consequently the independently reconstructed saturated-duality/negative-degree-Hom proof excludes an actual lci thickening on any smooth projective base curve with balanced conormal, positive moving direction, actual saturated pure-power first relation m^r, and full generic coprime binary-CI initial degrees2<=r<s, whenp>s. The proof uses the actual surjection at degrees; first-relation jet lifting alone does not supply it. This is a source-level extension, with no canonical metadata promotion.

On a rational base the [prime-to-characteristic spectral descent theorem](FIRST_RELATION_AND_SPECTRAL_ROOTS.md#prime-to-characteristic-spectral-descent-excludes-repeated-moving-components) gives the stronger necessary restriction p|s for such a moving pure-power actual model: normal flatness supplies descent on the full repeated root, and descent withp∤s would force that root reduced. Forp|s Frobenius can kill nilpotent Picard obstructions, so neither argument gives a blanket positive-characteristic exclusion. The rational-base strengthening must not be asserted for every base genus merely from the doubled-divisor calculation onP1×P1.
