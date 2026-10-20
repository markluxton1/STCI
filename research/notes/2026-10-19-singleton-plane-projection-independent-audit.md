# Independent audit: a plane normalization with singleton inverse support and no mate

Date: 2026-10-19. Reviewer: `projection_geometry/plane_support`.

**Outcome: PASS for the displayed map and the broader family in Section 5,
their full singleton inverse support, the precise birationality criterion,
and their exclusion of a set-theoretic mate in every positive degree.** This
is an independently reconstructed proof and review evidence, not a
canonical promotion. No canonical result/question record or accepted proof
was edited, and no inherited exclusion was rerun.

## Exact claim, scope, and dependencies

Let `k` be algebraically closed of characteristic zero. Use homogeneous
coordinates `(s:t:z)` on `S=P2`, let `c=(z=0)`, and define

    U0=s^4,   U1=s^3 t,   U2=s t^3+z^4,   U3=t^4+s^3 z,
    f=(U0:U1:U2:U3): P2 -> P3.

Then `f` is the finite birational normalization map of an integral
degree-sixteen hypersurface `X`; its restriction to `c` is an isomorphism
onto the literal embedded rational quartic

    C0=[s^4:s^3t:st^3:t^4].

The full reduced inverse support of `C0` is exactly `c`. Nevertheless,
there is no homogeneous polynomial `G` of any positive degree with
`(X intersect V(G))_red=C0`.

[STCI-R-0002](../results/cartier_singleton_lift.md) identifies the model
`(P2,c a line,H=O(4))` as a necessary possibility under its own hypotheses.
This audit constructs an actual normalization with full singleton support
inside that model, and proves that this carrier has no mate. The proof
below is direct and does not assume a conductor classification, a computed
phase image, or the existence of a mate. The question being informed is
[STCI-Q-0001](../questions/cartier_projection_models.md); that question
remains open for the rest of its projection families.

## 1. Basepoints, finiteness, birationality, and normalization

If `s!=0`, then `U0!=0`. If `s=0`, the last two coordinates are `z^4,t^4`,
which cannot both vanish at a projective point. Thus the four sections
are basepoint free and `f^*O(1)=O_P2(4)`.

Every positive-dimensional fiber of a projective morphism from `P2`
contains a complete curve. On such a curve the pullback of `O(1)` would
have degree zero, contradicting the ampleness of `O(4)`. Hence `f` is
finite onto its image.

On `s!=0`, put `x=t/s`, `y=z/s`. In the target chart `X0!=0` the map is

    (x,y) -> (X1/X0,X2/X0,X3/X0)=(x,x^3+y^4,x^4+y).

The inverse on its image is

    x=X1/X0,   y=X3/X0-(X1/X0)^4.

Thus the map is an isomorphism onto its image on this entire affine chart,
and in particular it is birational. Its image is integral, and the degree
formula gives `deg X=(4 line)^2=16`. A finite birational morphism from the
normal surface `P2` is the normalization of its integral image.

One can also verify the image equation directly:

    F=(X0^3 X3-X1^4)^4-X0^13 (X0^2 X2-X1^3).

Both terms have degree sixteen. Under substitution,

    U0^3 U3-U1^4=s^15 z,
    U0^2 U2-U1^3=s^8 z^4,

so `F(U)=0` identically. As a polynomial in `X2`, its coefficient is
`-X0^15`, while its constant coefficient is not divisible by `X0` because
its restriction at `X0=0` is `X1^16`. The polynomial is therefore primitive
and linear over `k(X0,X1,X3)`, and is irreducible. Consequently `X=V(F)`.

## 2. Literal restriction and full inverse support, including the boundary

At `z=0`, the map is exactly the displayed parametrization of `C0`, with
no projective change of coordinates. That parametrization is a closed
immersion: on `s!=0` its parameter is `X1/X0=t/s`; at `s=0,t=1` the
coordinate `X2/X3=s` gives a nonzero tangent parameter. In particular,
`f|c` is an isomorphism onto `C0`.

On `s!=0`, the equations for `C0` in the target affine chart are

    X2/X0=(X1/X0)^3,   X3/X0=(X1/X0)^4.

The second equation forces `y=0`, and the first then follows. Thus the
inverse support on this chart is exactly `z=0`.

On `s=0`, the image is `[0:0:z^4:t^4]`. The only point of `C0` with
`X0=0` is `[0:0:0:1]`; its inverse points in this boundary satisfy `z=0`
and `t!=0`. This adds just `(0:1:0)`, already on `c`. Therefore

    (f^{-1}(C0))_red=c

globally, with no isolated inverse point or additional inverse curve.

## 3. All-positive-degree mate obstruction

Suppose that a homogeneous `G` of degree `b>=1` satisfies
`(X intersect V(G))_red=C0`. Its pullback `G(U)` is a nonzero homogeneous
polynomial of degree `4b` whose projective zero support is exactly `c`.
Unique factorization gives

    G(U)=lambda z^(4b),   lambda!=0.

Divide `G` by `lambda`. At `s=0` the identity becomes

    G(0,0,z^4,t^4)=z^(4b).

The substitution `k[Z,T] -> k[z,t]`, `Z->z^4,T->t^4`, is injective, so

    G(0,0,Z,T)=Z^b.                                      (1)

Now differentiate the pullback identity with respect to `s` and set
`s=0`. The derivatives of `U0,U1,U3` vanish at `s=0`, while
`dU2/ds=t^3`. The chain rule and (1) therefore give

    0=t^3 G_X2(0,0,z^4,t^4)=b t^3 z^(4b-4).

This is impossible over a field of characteristic zero for every integer
`b>=1`. The calculation is a uniform proof in `b`; no bounded-degree search
or unexecuted computation is involved. It requires neither irreducibility
of `G` nor any genericity assumption on its coefficients.

## 4. Adversarial checks and exact frontier impact

The most consequential boundary checks are `s=0` and its point `z=0`.
The boundary maps with degree four to the line `X0=X1=0`; its sole point
mapping to the endpoint of `C0` is already on `c`. Thus a proposed general
argument that every plane projection in this model must have a second
inverse point is refuted by this example.

At the reduced boundary, the required restriction `z^(4b)` is compatible
with descent through `(z:t)->(z^4:t^4)`, since it is the pullback of `Z^b`.
The contradiction occurs in the first transverse derivative. Accordingly,
checking only reduced boundary values would miss this obstruction. This
observation does not compute the full conductor ideal or identify an
entire phase image, and no such computation is needed for the proof.

The proof establishes the existence of an actual degree-sixteen
normalization with literal `C0` and full singleton inverse support, and
excludes every mate for that carrier. Section 5 extends the argument to
an explicit parameter family. It does not exclude all maps from
`P2` with polarization `O(4)`, either degree-eight normalization model, or
any non-Cartier/multiple/nonisomorphic lift. It does not settle the
unrestricted characteristic-zero STCI problem.

## 5. Broader audited family and exact birational locus

Fix `alpha!=0`, let `P(s,t,z)` be any homogeneous cubic, and replace the
four sections by

    U0=s^4,   U1=s^3t,   U2=st^3+alpha z^4,   U3=t^4+zP(s,t,z).

These are basepoint free: `U0` handles `s!=0`, while at `s=0` the coordinate
`U2=alpha z^4` handles `z!=0` and `U3=t^4` handles `z=0`. The same ample
pullback argument proves finiteness. The restriction to `c` remains the
literal `C0`. On `s!=0`, membership in `C0` forces
`U2/U0=(U1/U0)^3`, hence `alpha(z/s)^4=0` and `z=0`. On `s=0`, membership
in the endpoint `[0:0:0:1]` likewise forces `z=0`. Thus the full inverse
support is `c` for every member of this family, without a birationality
assumption.

Write uniquely

    P=A3(s,t)+z B2(s,t)+z^2 C1(s,t)+delta z^3,

where the subscripts are the binary degrees. Set `K=k(x)`. On `s=1` the
image function field inside `K(y)` is

    K(y^4,p(y)),
    p(y)=A3(1,x)y+B2(1,x)y^2+C1(1,x)y^3+delta y^4.

The extension `K(y)/K(y^4)` is cyclic Galois with group `mu4`, acting by
`y->zeta y`. Its subgroup fixing `p(y)` is trivial exactly when `A3!=0`
or `C1!=0`. Indeed a nonzero linear or cubic coefficient forces
`zeta=1`; if both vanish and `B2!=0`, the stabilizer is `{1,-1}`; if all
three vanish, it is all of `mu4`. Consequently the finite map has degree

    1 if A3!=0 or C1!=0;
    2 if A3=C1=0 and B2!=0;
    4 if A3=B2=C1=0.

The image degrees are respectively sixteen, eight, and four. In the first
case the map is the normalization, and realizes the same necessary
degree-sixteen model. This field argument uses characteristic zero and
the algebraically closed ground field, so the fourth roots of unity are
present and the extension is separable.

Finally, every member has the same all-degree mate obstruction, including
the nonbirational members. A hypothetical mate again yields, after scalar
normalization,

    G(U)=z^(4b).

At `s=0` consider the morphism

    P1_(t:z) -> P1_(Z:T),
    (t:z) -> (alpha z^4:t^4+zP(0,t,z)).

It is basepoint free and has pullback `O(4)`, hence is nonconstant and
surjective. Pullback of a nonzero homogeneous polynomial in `(Z,T)` is
therefore nonzero. The restriction identity forces

    G(0,0,Z,T)=(Z/alpha)^b.

In particular `G_X3(0,0,Z,T)=0`. Differentiate with respect to `s` at
`s=0`. The derivatives of `U0,U1` vanish; the derivative of `U2` is `t^3`;
and the potentially nonzero derivative `zP_s(0,t,z)` of `U3` is multiplied
by the identically zero restricted `G_X3`. The resulting identity is

    0=(b/alpha)t^3 z^(4b-4),

which is impossible. This proves a uniform all-positive-degree exclusion
for precisely the displayed family, and an explicit family of actual
degree-sixteen singleton-support normalizations when `A3!=0` or `C1!=0`.
It does not classify arbitrary four-coordinate quartic systems.

**Review status:** independently audited proposal/evidence, pending any
separate canonical promotion decision.

## Addendum: independent audit of the differential lemma and generic local descent

The reviewer separately reconstructed Sections 6--7 of the
[source investigation](2026-10-19-singleton-projection-investigation.md).
**Outcome: PASS**, with the lemma understood for an integral projective
surface and its finite normalization, as in the surrounding investigation.
This addendum supplies independent review evidence; it does not promote a
canonical result or compute a conductor multiplicity.

### A. Differential-kernel obstruction

Let `nu:S->X` and the data `L,H,c,C,Q,m,p,h,v` satisfy the source lemma.
In particular `S` is normal and projective, `c` is a nonzero smooth ample
Cartier curve, `div(Q)=m c`, the full reduced inverse support of `C` is
`c`, and `p` lies outside `c` in the smooth locus. Suppose a nonzero section
`sigma` of `L^b`, with `b>=1`, had zero support exactly `C`.

Its pullback has divisor `r c` for a positive integer `r`. Since this
pullback and `Q^b` are sections of the same line bundle, their divisor
classes give `(r-mb)c~0`. Intersecting with an ample divisor, which has
positive intersection with `c`, proves `r=mb`. Their ratio is a rational
function of divisor zero. Normality implies that this function and its
inverse are globally regular, and projectivity and integrality imply that
it is a nonzero scalar. Hence, in the frame `h^b`, the pullback of `sigma`
is `lambda q^b`, where `q=Q/(nu*h)` and `lambda!=0`.

Every function pulled back from `X` has differential zero on
`ker(dnu_p)`. But on the specified vector `v`,

    d(lambda q^b)_p(v)=lambda b q(p)^(b-1)dq_p(v)!=0.

Here `q(p)!=0` follows from `p` lying outside `c`, and `b!=0` in the field
uses characteristic zero. This proves the obstruction. No smoothness of
`X` at `nu(p)` is needed: its Zariski tangent space and differentials of
local functions suffice. If the frame is changed by a local unit `u` on
`X`, then `q` changes to `q/(nu*u)`; the extra differentiated term vanishes
on `ker(dnu_p)`. Thus the nonvanishing condition is frame independent.

For the primitive map, in source coordinates `(r,y)=(s/z,t/z)` and target
frame `X2`, take `p=(0,1)`. The target affine coordinates are

    a0=r^4/(1+r y^3),
    a1=r^3 y/(1+r y^3),
    w=(y^4+r^3)/(1+r y^3).

At `p`, `da0=da1=0` and `dw=-dr+4dy`. Therefore
`v=partial_r+(1/4)partial_y` belongs to the differential kernel, while
`q=1/(1+r y^3)` has `dq_p(v)=-1`. This point lies outside `c=(z=0)` and
gives a valid local obstruction to descent of every power.

### B. Generic local ring and denominator check

For a birational member of the broader family, let `D=(s=0)`, and work in
the source chart `z=1` with coordinates `r=s/z,y=t/z`. The source local
ring at the generic point of `D` is the DVR

    B=k[r,y]_(r)=k(y)[r]_(r),    E=B/(r)=k(y).

The target affine coordinate ring in the chart `X2!=0` is the subring
`A=k[a0,a1,w]` of its function field, with

    a0=r^4/(alpha+r y^3),
    a1=r^3 y/(alpha+r y^3),
    w=(y^4+P(r,y,1))/(alpha+r y^3).

The image line `ell` has prime `p=(a0,a1)` and `A/p=k[w]`: it is indeed
the entire line, because the boundary morphism to it is surjective. Its
residue coordinate pulls back to

    w0=g(y)/alpha,    g(y)=y^4+P(0,y,1).

The polynomial `g` has degree exactly four because `P` has total degree
three. Thus `w0` is transcendental over `k`, and the target residue field
`K=k(w0)` embeds in `E` with degree four. The nontrivial residue extension
proves nonnormality at the generic point of `ell`, so `D` is a conductor
prime. Also `f^{-1}(ell)` has reduced support only `D`, since `U0=s^4`;
there is no second inverse prime over the generic point of the line.

Take an arbitrary element of the target local ring `A_p`. Write it as

    N(a0,a1,w)/M(a0,a1,w),    M notin p,

using polynomial representatives. The denominator's restriction
`M(0,0,W)` is a nonzero polynomial. Substitution `W=w0` is injective, so
this denominator has nonzero residue and is invertible in `B/(r^2)`.
Because `a0,a1` vanish modulo `r^2`, the image of this localized element
in `B/(r^2)` is exactly

    R(w),    R(W)=N(0,0,W)/M(0,0,W) in k(W).

This establishes the asserted form for all localized elements, including
those with denominators; no polynomial-only assumption is hidden. If its
residue is the constant `alpha^(-b)`, injectivity of `k(W)->E`,
`W->w0`, forces the rational function `R` itself to be that constant.
Consequently the element has zero coefficient of `r` modulo `r^2`.

In contrast,

    q^b=(alpha+r y^3)^(-b)
       =alpha^(-b)-b alpha^(-b-1)y^3 r mod r^2,

has nonzero linear coefficient for every positive `b`. Thus `q^b` is not
in `A_p`, even though its residue `alpha^(-b)` lies in `K*` and is the
identity class of `E*/K*`. This is an exact first-order obstruction at the
actual generic conductor prime. It does not require knowing which power
of `(r)` equals or lies in the conductor ideal.

For the primitive member the affine chart `s!=0` is an isomorphism, by
the explicit inverse already checked. The generic nonnormality along
`D`, together with this isomorphism off `D`, proves that the entire
conductor support upstairs is `D`. No scheme multiplicity is inferred,
and no analogous entire-support assertion is justified here for arbitrary
`P`.

The differential lemma and this generic local calculation are therefore
independently reviewed with the literal hypotheses above. Their scope is
an obstruction and an explicit family calculation, not a computation of
the full plane-model phase image or a general exclusion of that model.

## Closing independent review of the two-fixed-coordinate sublane

Reviewer: root investigator, independently reconstructing Section 5a of
the proposal after its author stopped work. Outcome: PASS under the literal
basepoint-free, full-singleton-support, characteristic-zero hypotheses.

On s=0, a point with z nonzero and A3(0,t,z)=0 would have U0=U1=U2=0.
Basepoint freeness then gives U3 nonzero, so its image would be the C0
endpoint, contrary to the assumed full inverse support. Therefore the
polynomial A3(0,t,1) has no zero over the algebraically closed ground field.
It is a nonzero constant alpha, proving A3(0,t,z)=alpha z^3. Thus
U2=st^3+alpha z^4+szC2. The boundary morphism is basepoint free with
pullback O(4), hence surjective onto the target line. A hypothetical mate
forces G(0,0,Z,T)=(Z/alpha)^b. Its X3 derivative is zero on the line,
while its X2 derivative gives (b/alpha)z^(4b-4). The chain rule in s
therefore forces that nonzero factor times t^3+zC2(0,t,z) to vanish.
The latter polynomial has t^3 coefficient one and cannot be zero.
This excludes every positive mate degree throughout this exact sublane.

This check does not put arbitrary plane projections into that coordinate
sublane, classify its support-admissible locus, or remove the hypotheses.
