# An explicit degree-eight quadric-normalization family with a fourfold residual line

Date: 2026-10-19. Author: `carrier_models`.
Status: **INDEPENDENTLY REVIEWED PROPOSAL; audit PASS; not promoted.**
Review: [separate carrier audit](2026-10-19-quadric-antidiagonal-fourfold-line-independent-audit.md).

## Exact question and scope

Work over an algebraically closed field `k` of characteristic zero. The embedded curve is the literal fixed curve

    C0=[s^4:s^3 t:s t^3:t^4] in P3.

This note constructs actual integral degree-eight hypersurfaces whose finite normalization is the smooth quadric `S=P1 x P1`, with polarization `H=O(2,2)` and with a diagonal curve `c` mapped isomorphically to `C0`. It then proves that every basepoint-free member of this particular one-parameter family has **extra inverse points of C0**, so no member has a set-theoretic mate for C0 in any degree.

This is a completed exclusion for the explicitly defined subfamily below, not an exclusion of all smooth-quadric projections or of either other normalization model in STCI-R-0002. It supplies an actual residual-conductor construction illustrating why full inverse support is an essential extra condition in STCI-Q-0001.

Dependencies used as navigation/premises: [STCI-R-0002](../results/cartier_singleton_lift.md), [STCI-R-0003](../results/fixed_carrier_conductor_criterion.md), [STCI-Q-0001](../questions/cartier_projection_models.md), and the literal universal projection family in [the October 14 contact-phase note, Section 4](2026-10-14-generalization-projection-contact-phase-criterion.md). The argument below is elementary and does not rerun an inherited certificate or use the phase-reduction conclusion.

## 1. The family

On `S=P1_(s:t) x P1_(u:v)` write

    q=sv-tu,                 c=(q=0),
    p=sv+tu.

For `kappa in k` put

    U0=s^2 u^2 + (1/2) q t v,
    U1=(1/2) s u p,
    U2=(1/2) t v p,
    U3=t^2 v^2 + kappa q^2.                         (1)

All four sections have bidegree `(2,2)`. Restriction to `c`, using `(u:v)=(s:t)`, gives exactly the four displayed coordinates of `C0`.

**Proposition.** If

    kappa != 0,          kappa^3 != -1/64,             (2)

then (1) gives a basepoint-free finite birational morphism

    f_kappa:S -> X_kappa subset P3,

where `X_kappa` is an integral degree-eight hypersurface and `f_kappa` is its finite normalization. The full inverse support of `C0` contains at least five distinct points outside `c`. Consequently no homogeneous form can cut out exactly `C0` set-theoretically on `X_kappa`.

The particularly simple member `kappa=1` satisfies (2). In the balanced first-normal-jet coordinates of the October 14 contact-phase note, this family has `A(x)=x^5`, `B(x)=0`: here `L0|c=x^2/2` and the other three `L_i|c` vanish. Thus it lies in the maximal degree-five common-zero stratum, with its entire differential degeneracy concentrated at `t=0`. The calculation below uses the actual projection, rather than inferring inverse support from these first jets.

## 2. Basepoint-freeness, including the boundary charts

If `U1=U2=0`, either `p=0` or `su=tv=0`.

In the second case the only possible points of `S` are

    ((0:1),(1:0)),        ((1:0),(0:1)).

At either point `q!=0` and `U3=kappa q^2!=0` when `kappa!=0`.

The curve `D=(p=0)` is a smooth `(1,1)` curve with parametrization

    (s:t)=(a:b),         (u:v)=(a:-b).

On `D` the four sections become

    U0=a^4+a b^3,
    U1=U2=0,
    U3=b^4+4 kappa a^2 b^2.                         (3)

At `a=0` the last section is nonzero, and at `b=0` the first is nonzero. At any other simultaneous zero set `x=b/a`. The necessary and sufficient equations are

    x^3=-1,             x^2=-4 kappa.

They have a solution exactly when `kappa^3=-1/64`. Indeed the forward implication follows on cubing the second equation; conversely `x=1/(4 kappa)` satisfies both when this relation holds. This proves basepoint-freeness under (2), with no chart omitted. Since `f_kappa^*O(1)=H` is ample, a curve cannot be contracted, so the morphism is finite.

## 3. An explicit rational inverse on a dense open set

Work on `s=u=1` and put

    x=t,       y=v,      r=xy,      d=y-x,      P=x+y.

Then

    (U0,U1,U2,U3)=(1+dr/2, P/2, rP/2, r^2+kappa d^2). (4)

Let `z_i=Ui/U0` be the target affine coordinates for `i=1,2,3`, and let `lambda=U0`. On the dense open set with `r z1!=0`,

    r=z2/z1,          P=2 lambda z1,
    d=2(lambda-1)/r.

The identity `P^2-d^2=4r` and the last coordinate of (4) give

    (1-r^2 z1^2) lambda^2 -2 lambda +1+r^3=0,
    4 kappa z1^2 lambda^2-z3 lambda+r^2-4 kappa r=0.

Set `A=1-r^2 z1^2`. Eliminating `lambda^2` yields

    lambda = [A(r^2-4 kappa r)-4 kappa z1^2(1+r^3)]
             /[A z3-8 kappa z1^2].                   (5)

The denominator is not identically zero on `S`: at `x=0,y=1` its value is `-kappa`. Evaluating there is only a nonidentity check; the actual inverse is used on the dense open set where all displayed denominators are nonzero. Finally

    x=(P-d)/2,            y=(P+d)/2.

Thus `f_kappa` is birational for every nonzero `kappa`. On (2) it is finite birational from the normal surface `S`, hence is the normalization of its integral image. The image is a surface in `P3`, therefore an integral hypersurface, and its degree is

    H^2 / deg(f_kappa) = (2,2)^2 = 8.

## 4. The residual fourfold line and five forced extra inverse points

The curve `D` maps to the line

    L=(X1=X2=0) subset P3.

By (3) and basepoint-freeness, `f_kappa|D:D=P1 -> L=P1` has pullback `O_L(1)=O_P1(4)` and consequently degree four. Its generic fiber therefore has four geometric points in characteristic zero. In particular `D` is an actual off-`c` conductor prime over `L`, with residual field degree four. This is residual geometry on the actual projective carrier, not an exceptional divisor of a blowup.

The diagonal and antidiagonal meet only at `b=0` and `a=0`. But the two points

    b^2+4 kappa a^2=0,       ab!=0,

also have `U1=U2=U3=0` and `U0!=0`. They are distinct, lie outside `c`, and both map to the endpoint `[1:0:0:0]` of `C0`.

Likewise the three distinct points

    a^3+b^3=0,              ab!=0,

have `U0=U1=U2=0` and `U3!=0`. They lie outside `c` and map to the other endpoint `[0:0:0:1]` of `C0`. The nonvanishing assertions follow from the already established absence of common zeros. Thus at least five distinct extra normalization points occur for every admissible parameter (2).

## 5. Why this excludes every mate degree on these carriers

We first verify that `c` is the **only inverse prime** over `C0`; finite birationality alone would not justify this statement. Apply (4) to a generic target point `[1:z:z^3:z^4]` with `z!=0`. Then `r=z^2`. If the inverse point is off the diagonal, `d!=0` and `lambda!=1`. The identities in Section 3 reduce to

    r=4 kappa(lambda+1),
    lambda-1=64 kappa^3(lambda+1)^4,
    z^2=r.                                             (6)

For completeness, `U3=lambda z^4` first gives `kappa d^2=(lambda-1)r^2`, while `P=2 lambda z` gives `d^2=4r(lambda^2-1)`. Cancelling `lambda-1` gives the first equation of (6); using `d=2(lambda-1)/r` then gives the second. Thus only finitely many constants `lambda`, and consequently only finitely many target values `z`, admit off-diagonal inverse points. Boundary points with `s u=0` have `U1=0`, so cannot map to a generic point of `C0`. The sole inverse prime over `C0` is therefore `c`; every extra inverse point is isolated.

Suppose an ambient form `G` of positive degree `b` cuts out exactly `C0` on `X_kappa`. Its nonzero pullback section has an effective Cartier zero divisor on the smooth integral surface `S`. Its support must equal the entire inverse support of `C0`. Since a principal zero locus on a smooth surface has pure codimension one, this support cannot contain isolated points. Equivalently, since `c` is the sole inverse prime, the pullback divisor would be `m c`; the class relation `m c~bH=2b c` gives `m=2b`, so its support would omit the five explicit isolated points from Section 4. This is impossible. The exclusion holds in every positive mate degree.

## 6. Frontier impact and remaining boundary

This produces actual degree-eight carriers with the expected normalization and polarization and an isomorphic diagonal lift, together with an explicit residual conductor prime. The extra inverse points prevent full singleton support and hence exclude a mate in all degrees on this subfamily.

The calculation does not prove that full-support parameters are absent from the sixteen-parameter smooth-quadric family. It does not test the quadric-cone or plane families and does not compute any surviving conductor phase image. It leaves STCI-Q-0001 and the unrestricted fixed-`C0` STCI question open. The proposition remains unpromoted until independent review reconstructs the basepoint calculation, rational inverse, generic inverse-prime calculation (6), and all-degree support argument.

## Verification record

No inherited mathematical certificate was rerun. All displayed identities are exact polynomial/rational identities proved above. A planned SymPy convenience check was not executed because neither the system Python nor the bundled Python has SymPy and the older `/private/tmp/stci-cas-venv` interpreter is absent in this session; no mathematical assertion depends on that attempted check.

## Appendix A. A simpler companion family with the entire inverse support computed

The following companion family has no exceptional parameter condition beyond `gamma!=0`:

    V0=s^2 u^2 +(1/2)q t v + gamma q^2,
    V1=(1/2)s u p,
    V2=(1/2)t v p,
    V3=t^2 v^2,                         gamma!=0.       (A1)

Again the diagonal maps to the literal `C0`, with balanced first jets `A=x^5,B=0`. This appendix is a second provisional proposition with an especially direct inverse-support calculation.

**Basepoint-freeness.** Since `V3=0` forces `t=0` or `v=0`, it is enough to consider those two boundaries. If `t=0`, the equation `V1=0` forces `uv=0`. At `v=0`, `V0=s^2u^2!=0`; at `u=0`, `V0=gamma s^2v^2!=0`. The argument at `v=0` is symmetric: its two boundary possibilities give either `V0=s^2u^2!=0` or `V0=gamma t^2u^2!=0`. Thus (A1) has no basepoint. As before ampleness makes the map finite.

**Birationality.** On `s=u=1`, with `r=xy`, `P=x+y`, `d=y-x`, the coordinates are

    (V0,V1,V2,V3)=(1+dr/2+gamma d^2, P/2, rP/2, r^2).

For target ratios `z_i=Vi/V0` and `lambda=V0`, an explicit rational inverse on a dense open set is

    r=z2/z1,                 lambda=r^2/z3,
    P=2 lambda z1,           D=P^2-4r,
    d=2(lambda-1-gamma D)/r,
    x=(P-d)/2,               y=(P+d)/2.                (A2)

Here `D=d^2` on the actual image; there is no extraction of a square root in the inverse. Thus the finite map is birational, its image is an integral degree-eight hypersurface, and `S` is its actual normalization.

**Entire inverse support.** For a target point `[1:z:z^3:z^4]` with `z!=0`, equations (A2) force

    r=z^2,       lambda=1,       P=2z,       D=0,       d=0.

Boundary points with `su=0` have `V1=0` and cannot map to such a point. Consequently the unique inverse point of every nonendpoint point of `C0` is its point on `c`.

Over `[1:0:0:0]`, the equation `V3=0` again forces `t=0` or `v=0`, and direct substitution gives precisely three inverse points: the diagonal point at `t=v=0`, and the two off-diagonal corners

    A=((1:0),(0:1)),         B=((0:1),(1:0)).

Both corners have image `[1:0:0:0]` because only `V0=gamma q^2` is nonzero there.

Over `[0:0:0:1]`, one has `tv!=0` and `V2=0`, so `p=0`. Parametrize `D=(p=0)` by `(s:t)=(a:b),(u:v)=(a:-b)`. Then

    (V0,V1,V2,V3)=(a^4+a b^3+4gamma a^2b^2,0,0,b^4).

The point `a=0` is the diagonal inverse point at infinity. The remaining inverse points are exactly the roots, with `x=b/a`, of

    1+4gamma x^2+x^3=0.                              (A3)

Every root is finite and nonzero, hence lies outside `c`. There are three distinct such points unless `256gamma^3+27=0`, when there are two distinct points (one double root). A triple root is impossible: the polynomial has nonzero constant term and zero linear coefficient. Thus the full reduced inverse support is exactly `c`, the two corners, and the two or three points from (A3). In particular for `gamma=1` it is exactly `c` plus five isolated extra points.

The same pure-divisor argument from Section 5 excludes a mate in every positive degree on every carrier in (A1). The antidiagonal again maps with degree four to `L`, since its two nonzero coordinate sections in the displayed formula have degree four and no common root. Hence it is an actual conductor prime with residual field degree four.

**Audit target.** The cleanest single explicit example is `gamma=1` in (A1), for which the full inverse support has the exact five isolated points just described. The first family (1), with condition (2), and the companion family (A1), with `gamma!=0`, are the two claims of this note. No larger projection-parameter claim is proposed.
