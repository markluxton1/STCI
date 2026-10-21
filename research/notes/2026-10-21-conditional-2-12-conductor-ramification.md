# Conditional (2,12;6,16;2): conductor control at a ramified simple multiplier zero

Date: 2026-10-21. Author: `conductor_budget` worker.

Status: **new conditional proposal; independent audit requested**. The local
normal-form and conductor computations below are exact. The global exclusion
uses an explicitly stated anticanonical contraction hypothesis in section 3;
that hypothesis is an **unresolved dependency in this note**. No canonical
result record is changed. No global pair, emptiness certificate, or general
nonnormal-surface bound is claimed.

## 1. Exact scope and source boundary

Use the same actual-pair hypotheses as the reviewed but unpromoted
[surface-bound proposal](2026-10-20-conditional-2-12-surface-bound.md): an actual
homogeneous supported pair of degrees `(6,16)`, full generic coprime initial CI
of degrees `(2,12)`, and actual saturated movement-two first relation, over an
algebraically closed field of characteristic zero. The promoted inputs are
[R-0010](../results/saturated_first_relation_normal_flatness.md) and
[R-0011](../results/moving_nonreduced_spectral_root_obstruction.md); the finite
singular-root bridge remains the reviewed, unpromoted dependency in
[the singular-gluing proposal](2026-10-20-conditional-2-12-singular-gluing.md).

Put `B=Bl_C0(P3)`, `L=3H-E`, and `Q'=2H-E=L-H`. The strict sextic is
`D in |2L|`, and `K_D=Q'|D`. In this note **D is assumed integral**. At a root
point above a zero of the base multiplier `alpha`, the actual finite bridge
and invertible generator change give

    F'=A*p+t^10*U,       U a unit,       p=G16/t^2 up to a unit,       (1)

where `t=0` cuts out `E`. On `E`, the coefficient of `p` is `alpha/beta`;
`beta` is a unit at a zero of `alpha`. Thus a simple zero of `alpha` on the
BASE gives `A|E=z` up to a unit, with `z` a local base parameter. This does
not assert that the pullback divisor on the double root cover is reduced.

The reduced root `Z` has bidegree `(2,2)`. The full spectral condition removes
the cuspidal and tangent-component strata, retaining smooth integral,
integral nodal, and two-node reducible roots, with their actual gluing data.
No earlier first or second obstruction computation is repeated here.

The global canonical-ideal facts used below are specializations of finite
duality and codimension-one adjunction. A primary reference is Miles Reid,
[Nonnormal del Pezzo Surfaces, section 2](https://ems.press/content/serial-article-files/40537).
Only those general duality facts are used; the del Pezzo classification and
its antiample hypotheses are not transferred to the present situation.

## 2. The conductor of a Gorenstein surface with trivial dualizing sheaf

Let `T` be an integral projective Gorenstein surface with `omega_T=O_T`, and
let `nu:Y->T` be its normalization. Write `I` for its conductor ideal, viewed
as an ideal in `O_Y`, and let `C=V(I) subset Y` be the full conductor SCHEME.
A normal surface is Cohen--Macaulay. Finite duality gives

    omega_Y = Hom_T(nu_*O_Y,omega_T) = I.                       (2)

The last equality is the equality inside the common rational function field:
`Hom_T(nu_*O_Y,O_T)` consists precisely of multipliers carrying `O_Y` into
`O_T`, namely the conductor. The quotient sequence

    0 -> omega_Y -> O_Y -> O_C -> 0                            (3)

shows that `C` is a Cohen--Macaulay curve. Applying `Hom_Y(-,omega_Y)`, and
using `Hom_Y(omega_Y,omega_Y)=O_Y`, yields

    omega_C = Ext^1_Y(O_C,omega_Y) = O_C.                       (4)

This argument does not require `Y` to be Gorenstein, or `C` to be reduced.
If the conductor is empty there is no assertion about a curve.

A useful consequence concerns a reduced irreducible component `R` of `C`
whose generic multiplicity in `C` is ONE. Finite duality for `R->C` gives

    omega_R = Hom_C(O_R,omega_C) = Ann_C(I_R) subset O_C.

Composing with `O_C->O_R` gives a generically nonzero map

    omega_R -> O_R.                                          (5)

It is injective: its kernel would be a zero-dimensional torsion subsheaf of
the torsion-free rank-one canonical module on the integral curve `R`.
Its cokernel has finite length, so Euler characteristics give

    2*p_a(R)-2 = -length(coker(5)) <= 0.

Therefore

> Every generic-multiplicity-one conductor component of an integral
> projective Gorenstein surface with trivial dualizing sheaf has
> arithmetic genus at most one. In particular it cannot have an
> intrinsically unibranch singular point of delta-invariant two.

Other conductor components may be nonreduced; they do not invalidate (5).
This is stronger than assuming that the whole conductor is reduced.

## 3. Explicit global contraction hypothesis

For the application below, assume a morphism

    psi:B -> Y0

with ALL the following properties:

* `Y0` is a smooth projective threefold, with an ample class `M`;
* `psi` is birational and is an isomorphism off `Q'`;
* `Q'=P1 x P1`, with normal bundle `O(1,-1)`, is its exceptional divisor;
  `psi` contracts exactly the ruling fibers on which `L|Q'=O(2,0)` has
  degree zero;
* `psi^*M=L`, `K_Y0=-2M`, and the integral `D in |2L|` is the pullback of
  an integral `T in |2M|`.

Then `T` is Gorenstein with trivial dualizing sheaf. The expected target is
the degree-five del Pezzo threefold in `P6`. **This note does not establish
that contraction or the descent of every section of `2L`. They are required
bridges, not consequences of the numerical identities alone.**

Let `Y_D` and `Y_T` be the normalizations of `D` and `T`. The morphism
`Y_D->T` factors through a proper birational map `Y_D->Y_T`. A conductor
component `R_D` whose image curve in `B` is not contracted by `psi` maps
finite birationally onto a conductor component `R_T`: away from `Q'` the
ambient morphism is an isomorphism. Generic conductor multiplicity one is
preserved. For proper integral curves a finite birational map gives

    p_a(R_T) >= p_a(R_D).                                    (6)

Consequently the genus bound of section 2 applies to every such
NONCONTRACTED component. Contracted exceptional ruling fibers require a
separate argument; section 5 supplies one for the particular local germ
arising below.

## 4. Exact local normal form at a ramified simple base zero

Assume `Z` is smooth at `x`, its degree-two map to the base is ramified
there, and `alpha` has a simple zero on the base. In completed local
coordinates one may arrange

    A|t=0 = z times a unit,       p|t=0 = (z-w^2) times a unit.

Both `A` and `p` are regular in `z`. By formal Weierstrass division,

    A=a*(z-a0(w,t)),       p=b*(z-p0(w,t)),

where `a,b` are units, `a0(w,0)=0`, and `p0(w,0)=w^2` after the allowed
coordinate choices. Divide (1) by `ab`, center the `z` coordinate, and put
`s=(p0-a0)/2`. This gives

    F'=z_c^2-s(w,t)^2+t^10*V(z_c,w,t),       V a unit.

Its `z_c`-critical section `c(w,t)` lies in `(t^10)`. Parameter-dependent
formal completion of the square gives an actual formal coordinate `x` and
unit `u(w,t)` with

    F'=x^2-B(w,t),
    B=s(w,t)^2-t^10*u(w,t),       s(w,0)=w^2/2.              (7)

Indeed the critical value differs from `-s^2` by `t^10` times a unit;
`c^2/t^10` is divisible by `t^10`, so the unit remains a unit. Formal square
roots of units exist in characteristic zero over the algebraically closed
field. Hence

    B=B_-*B_+,       B_-=s-t^5*sqrt(u),   B_+=s+t^5*sqrt(u). (8)

Each factor is Weierstrass of degree TWO in `w`. They have no common
irreducible factor: any common factor would divide `t^5`, but neither
factor is divisible by `t`.

A double-cover hypersurface `x^2=B` in characteristic zero is normal
exactly when `B` is squarefree. Thus nonnormality at this germ forces one
factor, say `B_-`, to have the form

    B_-=e*d^2,       d=w-phi(t),       e a unit.              (9)

The other factor cannot also be a square. If `B_+=e2*d2^2`, restriction to
`d=0` would make `t^5` times a unit a square in `k[[t]]`, impossible because
its valuation is odd. It follows that `B_+` is reduced, and

    B_+|d=0 = t^5 times a unit.                              (10)

After absorbing `sqrt(e)`, the normalization is

    Y_local: y^2=B_+(w,t),       x=d*sqrt(e)*y.

This is normal, because `B_+` is reduced. Write `R=k[[w,t]]`; the original
ring and its normalization have presentations

    R + d*R*y  subset  R + R*y.

Their conductor is EXACTLY `d*(R+R*y)`: multiplication by `y` forces both
coefficients of a conductor element to be divisible by `d`. Consequently
the conductor curve germ is

    d=0,       y^2=t^5 times a unit.                         (11)

It is reduced, irreducible, of generic multiplicity ONE, and has
`delta=2`. Thus its global reduced conductor component has arithmetic
genus at least two.

Under the contraction hypothesis of section 3, if the corresponding
nonnormal curve is not contracted, (6) and the genus-one bound contradict
(11). This argument includes the case where the particular point lies on
`Q'`; a noncontracted conductor curve still maps finite birationally.

## 5. The contracted ruling-fiber case

Suppose the nonnormal curve in section 4 is a ruling fiber `W` contracted
by `psi`. On `B` one has

    N_(W/Q')=O_W,       N_(Q'/B)|W=O_W(-1).

The normal sequence splits since `H^1(P1,O(1))=0`, so

    N_(W/B)=O_W + O_W(-1),       O_B(D)|W=O_W.                (12)

The equation of `D` vanishes to order at least two along `W`. Its quadratic
normal cone is a global section of
`Sym^2(N_(W/B)^*) tensor O_B(D)|W`. Its discriminant is therefore a section

    disc(q2) in H^0(W,(det N_(W/B)^*)^2 tensor O_B(2D)|W)
             = H^0(P1,O(2)).                               (13)

The local normal form (9)--(10) is an ordinary transverse double crossing at
the generic point of `W`, so this discriminant is nonzero. In the local
coordinates `(x,d)` normal to `W`, its quadratic form is

    q2=x^2-t^5*unit*d^2.

Here `t` is a uniformizer on `W`, since `W=(x,d)` and `d=w-phi(t)`. The
discriminant thus vanishes to order FIVE at the point. That contradicts
(13), whose total zero degree is two. This excludes the contracted case
without applying the anticanonical conductor genus bound to a contracted
curve.

Combining sections 4 and 5 gives the following conditional conclusion:

> Subject to the contraction bridge in section 3, no nonnormal curve of
> the integral strict sextic can pass through a smooth ramification
> point of the root where alpha has a simple zero on the base.

At a smooth UNRAMIFIED root over a simple base zero, `(A,p,t)` are regular
coordinates; the germ is an isolated `A9` singularity. It contributes no
nonnormal curve. Thus the word "ramified" is now removed from the generic
simple-base-zero exception, but repeated base zeros and root nodes remain.

## 6. Conditional residual locus with squarefree alpha

The following consequence uses only the actual finite bridge, the local
conclusion above, the ampleness of `G'=16H-2E=10H+2L`, and the preceding
normal-strict-sextic exclusion. Ampleness follows if `H` and `L` give the
closed graph embedding into `P3 x P6`; that graph property is part of the
same geometric bridge and must be checked separately.

Suppose `alpha` is squarefree on the BASE and is nonzero at every singular
point of `Z`. Along `E` away from `Z`, the equation `F'|E=alpha*f` has
nonzero derivative in the base direction whenever it vanishes; hence `D`
is smooth there. At smooth root points over `alpha=0`, sections 4--5 and
the unramified `A9` calculation exclude any nonnormal curve. At smooth
root points where `alpha` is a unit, `D` is smooth.

A nonnormal curve `Sigma` would therefore meet `E` only at root nodes where
`alpha` is a unit. It cannot be contained in `E`, since the preceding
singular points in `E` are finite. At such a node one may take `p=F'`, and
parameter-dependent Morse coordinates give

    p=X*Y+h(t).

A singular curve exists there only if `h=0` identically, and its local
parameter is then `t`. Thus every such intersection with `E` is transverse.
There are at most two root nodes in the retained spectral strata. Put

    d=H.Sigma,       n=E.Sigma,       1<=n<=2.

The strict second equation restricts to `t^10` times a unit at each node,
and its intersection with `D` has sole support `Z`; hence

    (16H-2E).Sigma=10*n.

It follows that `16d=12n`, or `4d=3n`, impossible for integral `d>=1` and
`n=1,2`. A curve with `H.Sigma=0` would lie in an exceptional `E`-fiber,
already excluded. Thus `D` has no nonnormal curve, so its integral
hypersurface is normal. The existing normal-strict-sextic exclusion then
applies.

Accordingly, conditional on the geometric bridges and the normal-surface
proposal, an actual pair with integral strict sextic must satisfy at least
one of

    alpha has a repeated zero on the base;
    alpha vanishes at a root node.                           (14)

This is an exact exceptional-locus restriction, not a proof that its
remaining locus is empty. In particular it does not replace the actual
nodal or two-node gluing conditions by normalization data.

## 7. Exact local escape at a root node

The local calculations do not remove the second stratum in (14). For
example

    F=z*w^2-(z-t^3)^2*(z-t^4)
      = z*p+t^10,

where

    p=w^2-z^2+z*t^4+2*z*t^3-2*t^7-t^6.

On `t=0`, the full root is the ordinary node `p=w^2-z^2`, and the base
multiplier is the simple zero `alpha=z`. The surface is nonnormal along

    W: w=0, z=t^3,

which leaves `E`. Its normalization is obtained with

    y=w/(z-t^3),       z*(y^2-1)=-t^4.

The conductor has `z=t^3`, and therefore `y^2=1-t`. It has two smooth local
branches at `t=0`, so the delta-two cusp obstruction does not apply. The
normalization has `A3` singularities at `y=+1` and `y=-1` over that point.
This is a LOCAL caution only. It is not a sextic with global
`k`-coefficients, does not assert any first/second/spectral incidence point,
and provides no degree-twelve standard-basis certificate or supported
complete intersection.

Repeated zeros of `alpha` are likewise genuinely unresolved. A gap-ten
term alone does not force transverse singularity `z^m+t^10` along a
nonnormal curve. For example `p*(z^2+t^2)+t^10` has a generic ordinary
double transverse singularity along `z=t=0`, with conductor cost two,
rather than the cost ten of `p*z^2+t^10`. A conductor-degree budget by
itself does not exclude these strata.

## 8. Evidence and next interface

The finite-duality, genus, and formal-normal-form arguments in this file
are new proposals. The geometric contraction and section-descent bridge
in section 3 is explicitly unresolved here. A separate independent audit
is requested before these conclusions are used in an actual-pair
exclusion. No existing normal-surface proof, accepted incidence proof,
canonical result metadata, or historical record has been edited.

The new target is the precise residual condition (14), retaining the
forced norm multiplier, all first and second obstruction equations, the
full spectral gluing, and actual global coefficient lifting conditions.
Neither a finite computation nor the local examples in section 7 prove
that residual condition realizable.
