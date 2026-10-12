# Endpoint quintic factor and seven-contact excess: independent audit

Date: 2026-10-11. Auditor: `oct11_quartic_assembly_audit/degree_factor_audit`.
Status: **EXACT POLYNOMIAL CHECKS AND DIRECT LENGTH-PROOF AUDIT**.
The separately delegated `finite_curve_length_lemma` reconstructed both
local exact sequences without using the author's proof as a premise.
This note changes no frozen note or canonical frontier file.

Scope: the explicit endpoint projection in the
[factor reduction](2026-10-11-session-quintic-endpoint-quadric-factor-reduction.md),
with center disjoint from S and coefficient a!=0. The
[explicit-model audit](2026-10-11-session-dp5-a4-explicit-model-independent-audit.md)
and [intrinsic-pair classification](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md)
provide the actual degree-five A4 model and the endpoint-versus-nonendpoint
projection distinction. This audit does not extend the endpoint equations
to nonendpoint projection centers, does not treat a=0, and gives no
upper bound for an excess-contact order.

## 1. Actual quadric factor and projective normalization

Use the six actual anticanonical coordinates in the stated affine chart:

    U0=1, U1=r, U2=r^2,
    U3=r^3-rT, U4=r^4-(2r^2+r)T+T^2, h=T.

For the four projection sections

    X0=U0+aT, X1=U1+bT, X2=U3+gT, X3=U4+dT,

direct expansion in Z[r,T,a,b,g,d] gives

    X0*X3-X1*X2=T*K,
    K=aU4-bU3-U2-(1+g)U1+dU0+(1+ad-bg)T.

This proves the displayed actual-section identity, including its T^2
and T^3 terms. On c, the pullback X0 is one, so X0=1+aT is a unit
in a neighborhood of each finite contact. The genuine projective
affine coordinates there are X1/X0,X2/X0,X3/X0; omitting this
division would generally produce wrong first-normal coefficients.

After clearing the unit denominators, the cubic and quartic residuals
are

    (X2/X0)-(X1/X0)^3 = A_pull/X0^3,
    (X3/X0)-(X1/X0)^4 = quartic_pull/X0^4,
    A_pull=X0^2*X2-X1^3,
    quartic_pull=X0^3*X3-X1^4.

Their coefficients of T are exactly

    U(r)=g-r-3br^2+2ar^3,
    V(r)=d-r-2r^2-4br^3+3ar^4.

The projective normalization contributes no further factor to these
first coefficients because the residual constant terms vanish and
X0|c=1. Their full first-normal rank condition is therefore U=V=0.

The additional exact identities are

    W(r):=K(r,0)=ar^4-br^3-r^2-(1+g)r+d=V-rU,
    A_pull=T*(U+T*P1+T^2*P2),
    P1=a^2r^3+2a(g-r)-3rb^2,
    P2=a^2(g-r)-b^3.

They retain the actual transverse variable T. No replacement of
higher contact by first-normal vanishing is made.

## 2. Residual curves and genus comparison

The author's a!=0 hypothesis makes D_K avoid the sole A4 point,
because K restricts there to aU4. The root lattice is the full
orthogonal A4 in the unimodular plane-blowup Picard lattice; quotienting
gives Cl(S)=Z[ell], with H=5ell. A prime avoiding A4 is Cartier, and
the local class of ell has order five, so its positive H-degree is
a positive multiple of five. Since H.D_K=5, the Cartier divisor
D_K is a single prime with multiplicity one. Thus D_K is an
integral CM curve, possibly singular, and Cartier adjunction gives
arithmetic genus one.

The projection is finite and birational on S. On D_K its degree
divides five. The only alternative to degree one would give a line
image. The restriction kernel of H0(S,H) onto D_K is the single
span of K; hence the four projection sections retain rank at least
three, excluding a line image. Thus D_K->R is finite birational.

On Q the three distinct integral curves C0, pi(ell), R have total
degree 4+1+5=10. They exhaust the quintic section of Q with
multiplicity one. The line pi(ell) is the endpoint ruling, so the
residual class is (3,2), and its arithmetic genus is two. Consequently

    0 -> O_R -> pi_*O_D_K -> F -> 0

has finite cokernel of length one. This comparison remains valid for
singular D_K or R. None of these statements calls D_K a normalization.

## 3. Finite birational pullback preserves the local contact length

Let q be a point of R intersect C0. Set

    A=O_R,q, B=(pi_*O_D_K)_q, F=B/A.

The local Cartier equation phi of C0 on smooth Q is a nonzero element
on the distinct integral curve R. It is a nonzerodivisor on A and B.
Multiplication by phi in the exact sequence above gives

    0 -> ker(phi:F->F) -> A/(phi) -> B/(phi)
       -> coker(phi:F->F) -> 0.

Every endomorphism of a finite-length module has kernel and cokernel
of equal length. Therefore

    length A/(phi) = length B/(phi)
      = sum_(p over q) length O_D_K,p/(pi*phi).

The last equality has no residue-degree weights because k is
algebraically closed. It does not require either curve to be smooth.

**Wording clarification to the source.** Phi is a nonzerodivisor
on the two curve rings, not on the finite cokernel F. A nonunit
cannot act injectively on a nonzero finite-length module. The proof
correctly permits phi to kill part or all of F; kernel and cokernel
then cancel exactly. This clarification does not change the conclusion.

## 4. Scheme divisibility, nonnegative excess, and the exact total seven

Under the full inverse-support condition, every point above R intersect
C0 lies in D_K intersect c. Near such a point S is smooth, since
D_K avoids A4, and c has a local Cartier equation t.

Lift phi from Q to a local regular ambient function on P3, and pull
it back to S. The actual morphism c->C0 makes the pullback vanish
scheme-theoretically on c. It therefore belongs to I_c=(t), and
restriction to D_K gives

    pi*phi=t*v in B_p=O_D_K,p.

Different ambient lifts differ by a multiple of the quadric equation,
whose pullback vanishes on D_K, so the restricted function is well
defined. The actual morphism supplies ideal containment; full reduced
support alone would not. For example t=z^2 and phi=z have identical
zero support in k[[z]], but phi is not divisible by t.

The ring B_p is a one-dimensional domain. The three elements t,v,tv
are nonzero, and the supported quotients have finite length. Cancellation
proves exactness of

    0 -> B_p/(v) --times t--> B_p/(tv) -> B_p/(t) -> 0.

Thus each local excess

    length B_p/(pi*phi)-length B_p/(t)=length B_p/(v)

is nonnegative. Full inverse support ensures that every zero of the
pulled equation, including every zero of v, is among D_K intersect c.
Summing over all contacts and using section 3 gives

    sum contact lengths = R.C0=11,
    sum actual c-intersection lengths = D_K.c=4,
    sum excess lengths = 7.

This proves the claimed necessary reduction even with singular
residual curves. The finite cokernel's length one does not bound
the excess, and the result is not yet a contradiction.

## 5. A bounded first-normal consequence, without a jet-order bound

All D_K intersect c points are in the finite r-chart because D_K
avoids the A4 point, which is the sole point at infinity of c.
On Q in X0!=0 a local equation of C0 is

    (X2/X0)-(X1/X0)^3.

Section 1 therefore identifies v, up to a unit, with
U+T*P1+T^2*P2 on D_K. If U(r_p)!=0 then v is a unit and
the local excess is zero. A point with positive excess consequently
has W(r_p)=U(r_p)=V(r_p)=0. Since a!=0, U is a degree-three
polynomial, so at most three finite points can carry the excess.
In particular coprime U,V exclude a mate under the full-support
hypothesis in this endpoint a!=0 lane.

This does not bound the excess at a common root. Repeated roots,
singular D_K, tangential intersection with c and higher terms of
the actual projection remain relevant. A seven-versus-three point
count would be invalid: seven counts length, not distinct points.

## 6. Execution evidence

The independent standard-library
[source](../validation/2026-10-11-quintic-endpoint-factor-audit/verify_polynomials.py)
passes seven exact sparse-polynomial identities over
Z[r,T,a,b,g,d]. Its SHA-256 is
`871099f080b3a69c58f15e6a6bd6a9475fd5cdfbba03008482ff7f23070de8ec`.
The actual exit-zero execution, command, interpreter path, elapsed
time and raw stream hashes are preserved in the
[execution record](../validation/2026-10-11-quintic-endpoint-factor-audit/execution-record.json).
The recording wrapper is not an additional mathematical verifier.
The ring-length proofs above, rather than these polynomial checks,
supply the contact-length quantifiers.
