# Independent audit of the quadric-normalization fourfold-line families

Date: 2026-10-19. Reviewer: `carrier_model_audit`, with a separate
Section 5 microaudit by `inverse_branch_microaudit`.

**Outcome: PASS for the two explicitly stated families and their all-degree
mate exclusions.** This is independent review evidence for the
[source proposal](2026-10-19-quadric-antidiagonal-fourfold-line-proposal.md),
not a canonical promotion. No accepted mathematics or canonical record was
edited, and no inherited quartic proof or certificate was rerun.

## Scope and dependencies

The checked ground field is algebraically closed of characteristic zero.
The literal embedded curve is

    C0=[s^4:s^3t:st^3:t^4] in P3.

The source surface is the smooth quadric `S=P1_(s:t) x P1_(u:v)`, with
diagonal `c=(sv-tu=0)` and polarization `H=O(2,2)`. The review covers:

1. Family (1) of the proposal, for precisely
   `kappa!=0` and `kappa^3!=-1/64`.
2. Companion family (A1), for every `gamma!=0`.

For each, the four displayed sections define an actual finite
normalization of an integral degree-eight hypersurface. The diagonal maps
isomorphically to `C0`, but the full reduced inverse support contains
isolated points outside `c`, excluding a mate in every positive degree.
The antidiagonal is an actual conductor prime mapping with residual degree
four to the line `(X1=X2=0)` downstairs.

[STCI-R-0002](../results/cartier_singleton_lift.md) is used only to identify
the relevant necessary normalization model; neither family meets its full
singleton-support hypothesis.
[STCI-R-0003](../results/fixed_carrier_conductor_criterion.md) supplies the
promoted isolated-inverse-point obstruction. This review also reconstructs
that elementary obstruction directly, without invoking the remaining
conductor descent lattice theorem. The balanced first-jet formulas are read
from Section 4 of the
[October 14 projection note](2026-10-14-generalization-projection-contact-phase-criterion.md).
The projection-phase reduction is not needed as a premise.

## 1. Basepoint-free locus and finiteness of the kappa family

Write `p=sv+tu`, `q=sv-tu`. Vanishing of both middle coordinates gives
either `p=0`, or `su=tv=0`. The latter locus consists of exactly the two
cross-corners

    ((0:1),(1:0)),       ((1:0),(0:1)).

At both, `q!=0`, and `U3=kappa q^2`. Thus these are not basepoints when
`kappa!=0`; both are basepoints when `kappa=0`.

The antidiagonal `D=(p=0)` is parametrized globally by
`(s:t)=(a:b), (u:v)=(a:-b)`. Its nonzero coordinate candidates are exactly

    U0=a^4+ab^3,           U3=b^4+4kappa a^2b^2.

At `a=0` or `b=0`, one of these is nonzero. Otherwise putting `x=b/a`
gives a simultaneous zero precisely when

    x^3=-1,               x^2=-4kappa.

These imply `kappa^3=-1/64`; conversely `x=1/(4kappa)` solves both
equations on that parameter locus. Hence the two stated exclusions are
the exact basepoint-free conditions, including all boundary charts.

The resulting projective morphism pulls back `O(1)` to the ample bundle
`O(2,2)`. A positive-dimensional fiber would contain a complete curve on
which this ample bundle has degree zero, which is impossible. Properness
and zero-dimensional fibers therefore give finiteness.

## 2. Birationality and degree of the kappa family

On `s=u=1`, set `x=t`, `y=v`, `r=xy`, `d=y-x`, `P=x+y`. Direct
substitution independently gives

    (U0,U1,U2,U3)=(1+dr/2,P/2,rP/2,r^2+kappa d^2).

For `z_i=Ui/U0`, `lambda=U0`, and `r z1!=0`, one has

    r=z2/z1,  P=2lambda z1,  d=2(lambda-1)/r.

Using `P^2-d^2=4r` produces

    (1-r^2 z1^2)lambda^2-2lambda+1+r^3=0.

The fourth coordinate then gives

    4kappa z1^2 lambda^2-z3 lambda+r^2-4kappa r=0.

Eliminating the quadratic term yields exactly formula (5) of the source,
with denominator `(1-r^2z1^2)z3-8kappa z1^2`. At `x=0,y=1`, this
rational function is defined and equals `-kappa`. Although `r=0` there,
this evaluation is used solely to prove nonidentity of the denominator;
it is not asserted to lie in the inverse chart. Because `S` is integral,
the simultaneous nonvanishing inverse conditions have a nonempty dense
intersection. Recovering `x=(P-d)/2`, `y=(P+d)/2` proves birationality for
every nonzero `kappa`; no further exceptional parameter occurs.

The finite birational morphism from normal `S` is the finite normalization
of its integral image. Finiteness makes the image a surface, hence an
integral hypersurface in `P3`. The degree formula gives
`deg X=H^2=(2,2)^2=8`.

## 3. Full inverse-support obstruction in the kappa family

Restriction to `c` gives the prescribed four quartic coordinates. The
parametrization of `C0` is an isomorphism: on the two endpoint charts its
local parameters are respectively `X1/X0=t/s` and `X2/X3=s/t`.

On `D`, the two degree-four sections above have no common zero on the
admissible parameter locus. They define a degree-four map to
`L=(X1=X2=0)`. Characteristic zero ensures four distinct geometric points
in its generic fiber. Its degree-four residue extension means the finite
normalization is not an isomorphism at the generic point of `L`; therefore
`D` belongs to the actual conductor support. This is a curve on `S`
mapping to a curve on `X`, not a vertical exceptional divisor.

The two roots of `b^2+4kappa a^2=0` give two distinct off-diagonal points
on `D` over `[1:0:0:0]`. The three roots of `a^3+b^3=0` give three
distinct off-diagonal points on `D` over `[0:0:0:1]`. Each has `ab!=0`,
and the other nonzero coordinate follows from basepoint-freeness. Thus the
claimed lower bound of five is valid for every admissible `kappa`.
Additionally, the two cross-corners from Section 1 also map to
`[0:0:0:1]`, giving seven forced endpoint extras. The source's lower bound
does not claim an exact total count.

To check that no other inverse curve absorbs these points, take any
nonendpoint target `[1:z:z^3:z^4]`. Then `z!=0`, `U1,U2!=0`, so all four
source coordinates are nonzero, and the affine calculation applies. For
an off-diagonal inverse point one has `r=z^2`, `d!=0`, `lambda!=1`, and

    kappa d^2=(lambda-1)r^2,
    d^2=4r(lambda^2-1),
    d=2(lambda-1)/r.

Cancelling only the already nonzero factors gives

    r=4kappa(lambda+1),
    lambda-1=64kappa^3(lambda+1)^4,
    z^2=r.

The polynomial in `lambda` is nonzero for every `kappa!=0`. It admits
only finitely many values of `lambda`, and then only finitely many `z`.
Boundary points with `su=0` have `U1=0` and cannot lie over a nonendpoint.
Every curve in the inverse support of `C0` must map onto `C0`, because
the morphism is finite. Hence `c` is the sole curve component, and the
extra points outside it are isolated in the full inverse support. This
argument is uniform on the entire stated parameter locus.

## 4. Companion family: exact full inverse support

For (A1), `V3=0` forces `t=0` or `v=0`. At `t=0`, the equation `V1=0`
forces `uv=0`; the respective nonzero coordinates are `s^2u^2` or
`gamma s^2v^2`. At `v=0`, the two cases similarly give `s^2u^2` or
`gamma t^2u^2`. Thus every `gamma!=0` is basepoint-free, with no further
condition. Ampleness again gives finiteness.

On the affine chart the coordinates are

    (1+dr/2+gamma d^2,P/2,rP/2,r^2).

Recover successively

    r=z2/z1, lambda=r^2/z3, P=2lambda z1,
    D=P^2-4r, d=2(lambda-1-gamma D)/r.

Since `D=d^2` on the image, this proves the rational inverse (A2)
without any square-root choice. Its nonvanishing conditions are dense;
for example `x=y=1` satisfies them for every `gamma`. Thus every
`gamma!=0` gives the claimed degree-eight integral carrier and finite
normalization.

For every nonendpoint point `[1:z:z^3:z^4]`, these identities force
`r=z^2`, `lambda=1`, `P=2z`, `D=d=0`. Its unique inverse point is on
`c`; the boundary cannot occur because `V1,V2` are nonzero.

Over `[1:0:0:0]`, the preceding boundary calculation gives exactly the
diagonal endpoint and the two cross-corners. Over `[0:0:0:1]`, `tv!=0`
and `V2=0` force `p=0`; the antidiagonal parametrization gives exactly
the diagonal endpoint `a=0` and the roots

    1+4gamma x^2+x^3=0,           x=b/a.

All roots are finite and nonzero. The discriminant is
`-256gamma^3-27`. If it vanishes, the repeated root is `x=-8gamma/3`,
and the second derivative there is `-8gamma!=0`, so it is exactly
double. There are therefore exactly three distinct extra points from
this cubic, or exactly two when `gamma^3=-27/256`. Together with the two
cross-corners, this proves the asserted entire reduced inverse support:
five isolated extras ordinarily, and four on the exceptional parameter
locus. In particular `gamma=1` has exactly five.

On `D`, the sections `a^4+ab^3+4gamma a^2b^2` and `b^4` have no common
zero. The degree-four map to `L` and the conductor-prime conclusion
follow exactly as in Section 3.

## 5. Every mate degree and the precise frontier boundary

If a homogeneous form `G` of positive degree `b` cut out exactly `C0`
on either carrier, its restriction and pullback would be nonzero sections.
The zero support of the pullback on smooth `S` would be the complete
inverse support of `C0`, including its isolated points. A nonzero section
of a line bundle on a smooth integral surface defines an effective
Cartier divisor, whose support has pure codimension one. This is
impossible. Equivalently, since `c` is the only inverse curve, the
pullback divisor must be `m c`; in `Pic(S)=Z^2`, comparison with
`bH=(2b,2b)` gives `m=2b`, and this divisor misses every off-`c` point.
Thus the exclusions hold in every positive mate degree.

The first-jet claim also checks directly: in both families
`L0|c=x^2/2`, while `L1|c=L2|c=L3|c=0`. The balanced formulas give
`A=x^5`, `B=0`, with homogeneous common-zero divisor `5(t=0)`.
The inverse-support conclusions above use the actual maps and do not
follow merely from these jets.

These explicit subfamilies provide actual carrier constructions and
completed, reviewed all-degree exclusions within their stated parameter
sets. They neither exhaust the sixteen-parameter smooth-quadric family
nor decide either other model in STCI-R-0002. No surviving full-support
conductor phase image is computed. STCI-Q-0001 and the unrestricted
characteristic-zero question remain open. Canonical promotion, if any,
requires its own recorded scope-preserving change.

## Verification record

The reviewer independently reconstructed every displayed identity,
boundary alternative, parameter exception, and divisor-support argument
above. The separate microaudit independently confirmed the kappa-family
inverse-prime calculation and all-degree obstruction. No CAS calculation
or finite numerical sample is used as a mathematical premise, and none
of the conclusions relies on rerunning an inherited proof.
