# Nonendpoint pole filtration and ramified-line powers: independent audit

Date: 2026-10-12. Auditor:
`oct11_endpoint_support_global_audit/two_root_contact_audit`.

Status: **PASS: direct independent mathematical reconstruction** of the pole
filtration, actual residual Weil divisor and its numerical partitions, and
the stated entire-line all-power obstruction. No broader nonendpoint or
quintic exclusion is asserted. No new mathematical CAS execution was needed;
the algebraic identities are reconstructed below. Prior records and canonical
files were not edited.

The audited owner note is
[nonendpoint pole filtration and line jet](2026-10-12-session-nonendpoint-pole-filtration-and-line-jet.md),
as read with SHA-256
`ad4459de5a95b12e26a162419082d7b32745323a6781716efdf6cca72767c2a2`.
The only clarification required is that the displayed transverse derivation
annihilates pulled-back target functions **after evaluation at the generic
point of ell**, not identically throughout the two-dimensional chart. This
interpretation is sufficient for the proof and is made explicit in Section 5.

## 1. Accepted inputs, parameters and admissibility

Work over an algebraically closed field `k` of characteristic zero. The
accepted intrinsic genus-one pair consists of the normal degree-five
anticanonical del Pezzo surface `S`, its smooth lifted quartic `c`, and its
unique line `ell`. Its only singular point is A4, on ell. The accepted
[pair classification](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md)
and [coordinate audit](2026-10-11-session-dp5-a4-explicit-model-independent-audit.md)
give the actual divisor identities

    div(U0)=5ell, div(h)=c+ell, H~5ell, c~4ell,
    Q=h^5/U0 in H0(S,4H), div(Q)=5c.

They also give the complete affine complement `S\ell=A2`, with coordinates
`r,t`, and

    T=t+r^2, v=t^2-r^3,
    U0=1, U1=r, U2=r^2, U3=-rt, U4=v-rt, h=T

in the `U0` frame. These are actual coordinates, not a tangent approximation.
The unique residual pair automorphism acts by translation in `r`. Thus two
finite center roots can be translated to `0,delta`, with `delta!=0`; their
difference is a retained parameter. It is twice the signed half-separation
in the midpoint convention, and there is no scaling normalization to one.

For arbitrary constants `a,b,g,d`, the four sections in the owner note
restrict to

    r^4, r^3(r-delta), r(r-delta)^3, (r-delta)^4

on c. They are linearly independent for every `delta!=0` and give the fixed
curve C0 with parameter `z=(r-delta)/r`. The A4 point `r=infinity` maps to
the nonendpoint `z=1`.

The section calculation below holds before imposing center avoidance. Its
interpretation as a normalization projection requires the line center to
avoid `S`. This condition makes the four sections basepoint free and gives
a morphism with pullback polarization `H`. The morphism is finite: a
positive-dimensional projective fiber would contain a curve on which the
ample H has degree zero. Its image spans P3, because the four sections are
independent. Since `H^2=5`, the product of its generic degree and the image
degree is five. The nondegenerate surface image cannot be a plane, so the
generic degree is one and the image is an integral quintic. Normality of S
then identifies this finite birational map with the normalization.

The all-power conclusion also uses the accepted
[quintic structural frontier](2026-10-11-session-quintic-structural-frontier.md):
any hypothetical mate has degree `4k` and pulls back to a nonzero scalar
multiple of `Q^k`. That input is not inferred from the pole calculation.

## 2. The pole filtration is exhaustive, including cancellation strata

On the genuine fourth blowup chart write `B=1+xu`. The accepted section
vector after the common base factor is removed is

    (Z0,Z1,Z2,Z3,Z4,Z5)
      =(u,B,x^2 B^2,xB,x^3 B^2,x^5 B^3).

At the generic point of ell, `x=0` is a uniformizer and `u` is the
transcendental coordinate in the residue field `k(u)`. The resolution is
an isomorphism over this smooth generic point. In particular

    r=Z4/Z5=x^(-2) B^(-1),
    t=Z2/Z5=x^(-3) B^(-1),
    v=Z0/Z5=u x^(-5) B^(-3).

The last expression also follows directly from
`t^2-r^3=x^(-6)B^(-3)(B-1)`. Thus the exact pole orders are `2,3,5`.

The polynomial presentation

    k[r,t]=k[r,v,t]/(t^2-r^3-v)

is free with basis `1,t` over `k[r,v]`, since the relation is monic in t.
Consequently every polynomial has a unique normal form as a finite linear
combination of `r^i t^j v^m`, with `i,m>=0` and `j=0,1`. Such a monomial
has exact pole weight `2i+3j+5m` and leading coefficient `u^m`.

At a fixed maximal weight, there is at most one monomial for each m:
`2i+3j=weight-5m` determines j by parity and then determines i. Its leading
coefficients therefore form distinct powers of u. A nonzero linear
combination cannot cancel all of them in `k(u)`. This treats the actual
cancellation in `t^2-r^3`; assigning independent weights to r and T would
not give an exhaustive argument.

For every `n>=0`, the resulting global section space is exactly

    H0(S,O_S(nell))
      =span_k{r^i t^j v^m : j=0,1 and 2i+3j+5m<=n}.

Indeed any divisorial section has no codimension-one pole on `S\ell=A2`
and is therefore a polynomial there. Conversely a polynomial satisfying
the ell bound has no negative divisor coefficient anywhere else. On the
normal S these are precisely the conditions for the reflexive Weil-divisor
sheaf. There is no additional codimension-two condition at A4. In particular

    H0(S,O_S(6ell))=span{1,r,t,r^2,rt,v,r^3}.

This also independently confirms the written
[low-pole-spaces proof](2026-10-11-session-a4-low-pole-spaces.md). Neither
6ell nor its sheaf is being asserted to be Cartier.

## 3. The residual divisor is actual and has exactly the stated partitions

For a direct reconstruction set

    p=v-rt, A=a+d-b-g, Bpar=ad-bg,
    L1=delta rt,
    L2=3delta rt+3delta^2 r^2-delta^3 r,
    L3=4delta rt+6delta^2 r^2-4delta^3 r+delta^4.

Then `X0=p+aT`, `X1=p+L1+bT`, `X2=p+L2+gT`,
`X3=p+L3+dT`, and direct multiplication gives

    q=p(L3-L1-L2)-L1 L2
      +T*(A p+aL3-bL2-gL1)+Bpar*T^2.

The first two terms are exactly

    T*(-3delta^2 r^3-3delta^3 rt+3delta^3 r^2
        +delta^4 t-delta^4 r).

This reconstructs the owner's full formula `q/U0^2=T F` without appealing
to the previous checker. Here

    F=A v-3delta^2 r^3
      +((4a-3b-g)delta-3delta^3-A)rt
      +(Bpar+(6a-3b)delta^2+3delta^3)r^2
      +(Bpar+delta^4)t
      +((-4a+b)delta^3-delta^4)r+a delta^4.

Its only normal-form weight-six monomial is `-3delta^2 r^3`. It has exact
pole order six, including the parameter strata where the coefficient of
`r^3` after expanding v into `t^2-r^3` happens to vanish.

The rational function `T=h/U0` has divisor `c-4ell`. Since the actual
Cartier section q of `2H` is represented by `TF` in the U0 frame,

    div(q)=div(T)+div(F)+2div(U0)=c+D,
    D=div(F)+6ell.

This D is an effective Weil divisor of degree six. Its ell coefficient is
zero, because the F pole has exact order six. The raw fourth-chart section
restriction also gives

    q|_(x=0)=(u-1)(u-1+4delta)
             -(u-1+delta)(u-1+3delta)=-3delta^2.

This is nonzero in the affine fourth-chart frame and at the generic point
of ell. It proves that ell is not a component, not that q has no point
intersection with ell at the omitted A4 point. No point-disjointness is
used in the argument.

For completeness, the localization sequence and `Cl(A2)=0` show that
`Cl(S)` is generated by ell. There is no relation: intersecting a
principal multiple `m ell` with the ample Cartier H gives `m=0`, because
`H.ell=1`. Hence `Cl(S)=Z[ell]`, and the class of any prime has coefficient
equal to its positive integral H-degree. The pole-filtration space for
`O_S(ell)` consists only of constants, so ell is the sole degree-one prime.
All prime components of D thus have degree at least two, and a total of
six permits exactly

    6; 4+2; 3+3; 2+2+2.

These are numerical partitions with multiplicities, not realization or
genus statements. D may contain c as the degree-four member; no assumption
that D is reduced or disjoint from c is required or established.

## 4. The rank-one equations exhaust entire-line ramification

In the same fourth chart, the four section values on ell are

    s=(u-1,u-1+delta,u-1+3delta,u-1+4delta),

their u derivatives are `(1,1,1,1)`, and their x derivatives are

    e=(a-u, b-u+delta u,
       g-u+3delta u+3delta^2,
       d-u+4delta u+6delta^2).

Set

    R2=g+3delta^2+2a-3b,
    R3=d+6delta^2+3a-4b.

Subtracting the first column from the others in the matrix with rows
`s,(1,1,1,1),e` gives its four ordered three-column determinants as

    -delta R2, -delta R3,
    delta(4R2-3R3), delta(3R2-2R3).

Thus their ideal is exactly `(delta R2,delta R3)`. The first two rows
are independent because `delta!=0`, so the projective differential has
rank at least one. Its rank at the generic point of ell is one exactly
when `R2=R3=0`; it otherwise has rank two. This is an exhaustion for
the stated entire-line rank condition, not for isolated ramification.

## 5. Frame-correct derivation and the obstruction to every positive power

Assume `R2=R3=0` and put `lambda=(b-a)/delta`. Define the polynomial

    C(u)=u^2+lambda u-lambda-a.

The needed derivation is the k-derivation from the local ring at the generic
point of ell into its residue field given by

    D(f)=[partial_x f+C(u) partial_u f]_(x=0).

It is transverse: `D(x)=1`. It is therefore not a derivation of the
residue field itself, and need not kill the target functions away from ell.
In the patch `X0!=0`, which contains the generic point since
`X0|ell=u-1`, direct quotient differentiation gives

    D(X1/X0)=0,
    D(X2/X0)=R2/(u-1),
    D(X3/X0)=R3/(u-1).

Hence all three values vanish on the retained rank-one locus. Chain and
quotient rules make D vanish on any downstairs local function pulled
back to this point. For the mate argument it already suffices that it
vanish on every polynomial in the three affine ratios.

The raw actual section Q in the fourth-chart H-frame is

    Qraw=(1+xu)^2(1+x+x^2u)^5.

It is a unit at generic ell, with value one and x derivative `2u+5`.
The normalized function

    q0=Qraw/X0raw^4

is invariant under changing the local H-frame. Its value is `(u-1)^(-4)`.
Also

    D(X0raw)/X0raw=(a-u+C(u))/(u-1)=u+lambda.

The quotient rule therefore yields

    D(q0)/q0=5-2u-4lambda,
    D(q0^k)=k*q0^k|ell*(5-2u-4lambda), for every k>=1.

The last value is nonzero in `k(u)`, since k has characteristic zero,
u is transcendental, and its linear coefficient is `-2k`. No analytic
logarithm, conductor flatness or reduced-branch assumption is involved.

If an ambient mate of degree `4k` existed, the accepted normalization
divisor argument would make its pulled section a nonzero scalar times
`Q^k`. Dividing by the actual pulled target frame `X0^(4k)` would express
that scalar times `q0^k` as a polynomial in the target affine ratios.
Its D value would then vanish, contradicting the preceding formula.
This proves the claimed exclusion for every positive k on this precise
admissible ramified-line subfamily.

## 6. Audit outcome and evidence boundary

The owner's structural claims and bounded all-power exclusion **PASS**.
The generic rank-two nonendpoint projection family remains open. In
particular this audit supplies no exclusion from a first derivative at
isolated points, no exhaustion of residual component genera, no universal
conductor descent result and no conclusion for all quintic carriers.

The owner supporting source has SHA-256
`24ae9f4b3b2092bf7870f4f09e17307b2feda84000ad91eb6087c022b4892738`.
I inspected its actual source, the
[recorded repaired execution](../validation/2026-10-11-quintic-nonendpoint-structure/attempt-05-root-name-repair/execution-record.json)
and both raw streams. A fresh read-only hash comparison matched the source,
execution snapshot, stdout and stderr to that record. It returned exit zero
and seven supporting conditions; the eighth printed PASS line is the final
label. This audit does not count that historical execution as a fresh
mathematical verifier, and no redundant CAS run was performed.

The independent evidence supplied here is the written reconstruction of
the full filtration, divisor, minors, frame and derivation. All prior
attempts, failure explanations and seal-bound files remain unchanged.
