# Conditional (2,12;6,16;2): cubic-model and conductor continuation audit

Date: 2026-10-21. Reviewer: `surface_bound`.

Status: **independent review PASS for the cubic-model interface and the
ramified simple-multiplier exclusion; one incorrect normalization claim
in the separate nodal example is explicitly rejected below**. All results
are reviewed proposals rather than promoted records. No actual pair or
full emptiness result is asserted.

## 1. Scope and reviewed files

The exact actual-pair scope is `C0`, algebraically closed characteristic
zero, degrees `(6,16)`, sole reduced support `C0`, FULL generic coprime
ordinary initial CI `(2,12)`, and ACTUAL saturated movement-two first
relation. The reviewed inputs are:

* [the cubic-image and conductor interface](2026-10-21-conditional-2-12-cubic-image-and-conductor-interface.md);
* [the conductor-ramification proposal](2026-10-21-conditional-2-12-conductor-ramification.md), sections 1--6;
* [the normality and ampleness audit](2026-10-21-conditional-2-12-geometric-audit-and-exceptional-locus.md),
  whose nodal extension was independently reconstructed in
  [the surface continuation](2026-10-21-conditional-2-12-surface-bound-continuation.md).

The singular-root finite bridge remains an explicit reviewed but
unpromoted dependency. The canonical lower-carrier input was read in
[R-0001](../results/quartic_carrier_exclusion.md), including its
**Consequences** paragraph, which expressly includes the earlier
plane/quadric/cubic exclusions and factor reduction. No inherited
carrier proof was rerun.

## 2. Exact cubic model: independent review PASS

I reran

    /opt/homebrew/bin/M2 --script research/computations/conditional_2_12_cubic_image_2026_10_21.m2

with exit code zero. The output verifies dimension four and degree five
for the homogeneous ring, projective smoothness by the Jacobian ideal,
the resolution with ranks `(1,5,5,1)` and shifts `(0,2,3,5)`, and vanishing
of the five displayed quadratic equations after substituting the seven
cubics. The computation is an exact check over `QQ`; it is not an
existence computation for `(F6,G16)`.

The resolution is Cohen--Macaulay of type one and gives
`omega_V=O_V(-2)`. Arithmetic Cohen--Macaulayness also gives connected
`Proj`; smoothness and connectedness imply integrality. The source
cubic map is birational on `q!=0`, where its first four coordinates
recover the original projective point. Its closed three-dimensional
image therefore equals this integral `V`.

On `V`, the four coordinates `y0,...,y3` cut out exactly the smooth conic
`Gamma` with equation `y4*y6-y5^2=0`. The inverse rational projection to
`P3` has this base IDEAL, not just this set-theoretic base locus. Thus
its graph closure is `Bl_Gamma(V)`. The Rees graph embedding of
`Bl_C0(P3)` has the same graph on the dense open, and both closures
are integral reduced schemes; hence they agree scheme-theoretically.
The common pullback divisor of `y0,...,y3` is exactly
`Q'=2H-E=L-H`, because the four remaining factors `x_i` have no common
zero. Consequently the contraction is an isomorphism off `Q'`, and
its contracted curves are precisely the appropriate ruling fibers.

The 23-dimensional sextic source consists of quadratic products of
the seven cubics. Equivalently `h0(V,O_V(2))=28-5=23` matches the full
source. Therefore every actual strict sextic descends as
`D=phi^*T`, with `T in |O_V(2)|`, and adjunction gives `omega_T=O_T`.
The quadric-factor exclusion says `D` has no `Q'` component, so `T`
does not contain the center conic.

The integrality step also passes. If an irreducible factor of `F`
did not contain `C0`, its intersection with the positive-degree mate
would produce a curve outside `C0`. Every factor is thus itself a
supported carrier. R-0001's stated consequences put its degree at
least five. Since `deg F=6`, only one factor with multiplicity one
is possible. Thus `F`, `D`, and `T` are integral under the ACTUAL
supported-pair hypotheses.

**Verdict: PASS.** This supplies the previously unresolved contraction
and descent hypotheses in section 3 of the conductor-ramification
proposal, within its exact actual-pair scope.

## 3. Full conductor duality and component genus: independent review PASS

Let `Y` normalize the integral Gorenstein `T` with `omega_T=O_T`.
Finite duality identifies `omega_Y` with the conductor ideal `I`
inside `O_Y`. Strictly, the `Hom_T` expression is a sheaf on `T`
and equals the pushforward of this `O_Y`-module; the module
identification itself is exact. Normal surface `Y` is Cohen--Macaulay.
The canonical ideal is depth two, so `C=V(I)` is a pure
Cohen--Macaulay curve (unless empty).

Apply `Hom_Y(-,omega_Y)` to
`0->I->O_Y->O_C->0`. Since `End_Y(omega_Y)=O_Y`, the resulting
cokernel is `O_Y/I`; codimension-one duality identifies it with
`omega_C`. Thus `omega_C=O_C`, even when `Y` is not Gorenstein
and the conductor is nonreduced.

For an irreducible reduced conductor component `R` of generic
multiplicity one, finite closed-immersion duality gives
`omega_R=Hom_C(O_R,O_C)=Ann(I_R)`. Its map into `O_R` is
generically nonzero and is injective because the canonical module
of an integral curve is torsion free. Its cokernel is finite;
Euler characteristics yield `2p_a(R)-2<=0`. Nilpotents on other
components do not affect this argument.

The map between the normalizations of `D` and `T` exists by the
universal property of normalization and is proper birational. A
conductor component not contracted by `phi` maps nonconstantly
and properly onto an integral conductor component, hence finitely.
It is birational because the ambient map is an isomorphism off
`Q'`. Therefore arithmetic genus can only increase in its image.
This remains true when the particular singular point lies on `Q'`.

**Verdict: PASS.** No assumption that the whole conductor is reduced,
or that the normalization is Gorenstein, has been inserted.

## 4. Ramified simple-base zeros: independent review PASS

At a smooth ramification point with a simple base zero of `alpha`,
both `A` and `p` are regular in the base coordinate `z`. Factoring
them by their unique roots in `z` and applying the parameter
Morse lemma gives exactly

    F'=x^2-B(w,t),
    B=s(w,t)^2-t^10*u(w,t),    s(w,0)=unit*w^2, u a unit.

The critical section in the centered `z` variable is divisible
by `t^10`; this verifies that the coefficient of `t^10` in the
critical value remains a UNIT. Therefore

    B=(s-t^5*sqrt(u))*(s+t^5*sqrt(u)).

The factors are coprime and each is Weierstrass of degree two in
`w`. Nonnormality forces precisely one to have a double linear
factor `e*d^2`, with `d=w-phi(t)`; the other cannot also be a
square, because its restriction to `d=0` has odd valuation five.

Here the finite normalization calculation IS valid: the double
cover is MONIC in `x`, and its normalization is
`R+R*y`, with `y^2=B_other` and original ring `R+d*R*y`.
The exact conductor is `d*(R+R*y)`. Its curve germ is
`y^2=t^5*unit`, reduced and irreducible, with delta two and
generic multiplicity one. A noncontracted global conductor
component would have arithmetic genus at least two, contradicting
section 3.

If the corresponding singular curve is contracted, it is a ruling
fiber `W` of `Q'`. Its normal bundle is `O+O(-1)` and `D|W=O`.
The nonzero discriminant of the global quadratic normal cone is
then a section of `O_W(2)`. The exact local normal form makes it
vanish to order five at the point, impossible. The parameter `t`
is indeed a uniformizer on `W=(x,d)`.

**Verdict: PASS.** Together with section 2, this removes the
conditional contraction hypothesis from the ramified simple-base
zero exclusion for ACTUAL pairs. It does not establish normality
at repeated base zeros or at nodes where `alpha` vanishes.

## 5. Strengthened exact exceptional locus

Assume `alpha` is squarefree on the base and does not vanish at
a root node. The ramified-simple-zero result removes the only
additional singular-curve contacts beyond the earlier nodal
argument. Every singular curve must then meet `E` solely in the
at most two root nodes, where `alpha` is a unit and the parameter
Morse form is `xy+h(t)`. A singular curve there is unique and
transverse to `E`. Writing `d=H.Sigma>0`, `n=E.Sigma<=2`, actual
support gives `G'.Sigma=10n`, whereas its class gives
`16d-2n=10n`, impossible. Thus `D` is normal and the reviewed
`144>50` obstruction applies.

Every actual pair must therefore satisfy at least one of:

    alpha has a multiple zero on the BASE;
    alpha vanishes at a NODE of the full root.

For smooth full roots, the new necessary equation is simply
`Disc_8(Ncomp(tau))=0`, degree 28 in the original root coefficients.
For nodal strata retain the actual node incidence
`alpha(c)=0, f(c,w)=0, df(c,w)=0`. These are necessary global
realization conditions. Their intersections with the full first,
second, torsion, and actual global sextic lifting conditions
have not been proved empty here.

## 6. Rejected finite-normalization assertion in the nodal caution

Section 7 of the conductor-ramification proposal correctly gives
the local equation

    F=z*w^2-(z-t^3)^2*(z-t^4)=z*p+t^10

and its nonnormal curve. Its subsequent claimed normalization
`y=w/(z-t^3)`, `z*(y^2-1)=-t^4` is NOT finite over the original
surface: at `z=t=w=0` its fiber contains the affine `y`-line.
Thus the assertions there that the finite conductor has two
smooth branches and that the displayed surface is the finite
normalization are rejected. A warning was added above that
historical paragraph rather than deleting it.

A potentially correct finite extension instead adjoins

    v=z*w/(z-t^n),         v^2=z*(z-t^m),
    z*w=(z-t^n)*v,
    v*w=(z-t^n)*(z-t^m),         2n+m=10.

The new generator is integral because its quadratic equation
is monic. Normality and the exact conductor of this extension
require their own verification. They are not assumed in the
exclusions of sections 2--5. In particular, the defective nodal
example supplies no evidence that the remaining global node
stratum survives the conductor test.
