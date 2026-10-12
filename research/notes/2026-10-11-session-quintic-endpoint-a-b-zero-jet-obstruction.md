# Endpoint a=b=0: a generic-line differential excludes every mate power

Date: 2026-10-11. Author: root.

Status: **DIRECT ALL-POWER PROOF; independent audit requested**. Work over
an algebraically closed field of characteristic zero. This note concerns
the a=b=0 boundary of the endpoint projection family, with arbitrary g,d.
It does not cover the nonendpoint modulus, the a!=0 family, or all quintic
normalizations. No mathematical execution is claimed here.

## 1. Imported geometric scope

Use the [quintic structural frontier](2026-10-11-session-quintic-structural-frontier.md),
its [independent audit](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md),
the [intrinsic pair classification](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md)
and the [explicit-model audit](2026-10-11-session-dp5-a4-explicit-model-independent-audit.md).
These give the normal degree-five del Pezzo surface S, its single A4
singularity, the lifted curve c, and the unique line ell. In anticanonical
coordinates put

    U0=Z5, U1=Z4, U2=Z3, U3=-Z1, U4=Z0-Z1,
    h=Z2+Z3, Q=h^5/U0 in H0(S,4H), div(Q)=5c.

Every hypothetical mate in this lane has degree 4k for k a positive
integer, and its pullback is a nonzero scalar multiple of Q^k. The global
all-quartic exclusion already makes k>=2, but the obstruction below
works for every k>=1. The normalized endpoint projection with a=b=0 is

    X0=U0, X1=U1, X2=U3+g h, X3=U4+d h.

Only projections whose line center avoids S need be considered. Such a
projection is finite birational onto an integral quintic hypersurface.
For the argument below, the map is defined near every generic point of
ell regardless of g,d, since X2=-1 there in the displayed chart.

## 2. A genuine smooth chart at the generic point of ell

The fourth blowup chart in the explicit-model audit has smooth coordinates
(x,r) and anticanonical section vector

    Z=(r, 1+xr, x^2(1+xr)^2, x(1+xr),
       x^3(1+xr)^2, x^5(1+xr)^3).

The strict ell is x=0; the blowup map to S is an isomorphism near its
generic point. The exceptional A4 chain meets ell at only one closed
point and therefore does not affect this generic smooth chart. With
B=1+xr and C=1+x+x^2r, the exact sections in this trivialization are

    h=x B C,
    X0=x^5 B^3,
    X1=x^3 B^2,
    X2=B(-1+g x C),
    X3=r-B+d x B C,
    Q=B^2 C^5.

The last equality follows from the actual section quotient h^5/U0,
not from a guess at its vanishing order. In particular Q restricts to
one along x=0 and is a unit at the generic point of ell.

## 3. The map has a transverse differential kernel

Use the actual downstairs affine patch X2!=0. Its three coordinate
functions pull back to

    Y0=X0/X2, Y1=X1/X2, Y3=X3/X2.

Modulo x^2 their exact expansions give

    Y0=0 mod x^2, Y1=0 mod x^2,
    Y3=1-r+A(r)x mod x^2,
    A(r)=r^2-g r+g-d.

Thus at the generic point of ell the differential has rank exactly one:
the r derivative of Y3 is -1, while both first derivatives of Y0,Y1
are zero. Over its residue field k(r), the transverse tangent vector

    v=partial_x+A(r) partial_r

annihilates the differential of all three downstairs coordinates. Every
regular function pulled back from the downstairs affine patch has
differential zero on v, by the chain rule. This remains true on any
singular image hypersurface: it is a statement about the actual morphism
to affine three-space, not a smoothness hypothesis on X.

## 4. The actual degree-four section has a nonzero transverse jet

Trivialize the pullback of O_X(4) by the actual coordinate X2^4. The
local function associated to Q is

    q=Q/X2^4=B^(-2) C^5 (-1+g x C)^(-4).

The inverse factors are units near the generic point of ell. Expanding
only their first order, with no omitted higher-order assertion, gives

    q=1+(5-2r+4g)x mod x^2.

Therefore q|ell=1, partial_r(q)|ell=0, and

    v(q)|ell=5-2r+4g,
    v(q^k)|ell=k(5-2r+4g).

For every fixed g and every positive integer k, this is a nonzero element
of k(r): the r coefficient is -2k, which is nonzero in characteristic
zero. It is immaterial that the expression can vanish at one closed
point of ell; it does not vanish at the generic point.

If a mate G of degree 4k existed, then in the patch X2!=0 its regular
function G/X2^(4k) would pull back to a nonzero scalar multiple of q^k.
Section 3 makes the differential of that function zero on v, whereas
the displayed identity makes it nonzero. This contradiction proves:

**Every admissible endpoint projection with a=b=0, for all g,d, admits
no mate in any positive degree.**

## 5. Why this is an all-power obstruction, and the retained boundary

The argument detects one actual necessary differential for a descended
section. It does not infer a bound on higher contact multiplicities from
first-normal data. The nonzero unit value q|ell=1 and characteristic zero
make the same obstruction persist under every power, by the exact chain
rule. No reduced, flat, Gorenstein or ordinary conductor-cover hypothesis
is used. No tensor-equalizer sufficiency is asserted.

The separate [a=0,b!=0 support proof](2026-10-11-session-quintic-endpoint-a0-support-exclusion.md)
and its [completed independent audit](2026-10-11-session-quintic-endpoint-a0-polynomial-support-independent-audit.md)
treat the other a=0 boundary. Combining them after this note is audited
would close the entire a=0 endpoint family. The a!=0 common-root support
problem and the extra nonendpoint modulus remain separate.
