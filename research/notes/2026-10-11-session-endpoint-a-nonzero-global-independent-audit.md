# Independent global audit: complete endpoint a-nonzero support exclusion

Date: 2026-10-11, with recorded executions on 2026-10-12 UTC.
Auditor: `oct11_endpoint_support_global_audit`.
Status: **PROVED HERE; COMPLETE INDEPENDENT GLOBAL AUDIT PASS** for the
stated intrinsic endpoint lane and `a != 0`. No unresolved parameter stratum
remains within that scope. This is not an exclusion of nonendpoint
projections, all quintic carriers, or unrestricted STCI presentations.

The owner proof is
[the endpoint a-nonzero full-support exclusion](2026-10-11-session-endpoint-a-nonzero-full-support-exclusion.md).
I reconstructed the projective implication and the target residual equations
independently, and delegated an independent reconstruction of the contact
orders to
[the two-common-root target audit](2026-10-11-session-endpoint-two-common-roots-target-contact-independent-audit.md).
I read its final note, source, execution record, and the separate
[direct-r local-excess proof](2026-10-11-session-quintic-endpoint-a-nonzero-local-excess-bound.md).
The latter gives a second route through actual intersection lengths, but the
global argument below does not require its geometric length identification.
The proof also uses the independently implemented
[original-variable residual-quartic certificate](2026-10-11-session-three-common-roots-residual-quartic-independent-audit.md)
and its
[shifted-variable replay](2026-10-11-session-endpoint-three-common-roots-shifted-replay.md).
Agent agreement alone is not used as a proof.

## 1. Exact statement and the mate implication

Work over an algebraically closed field of characteristic zero. The normal
degree-five anticanonical del Pezzo surface `S` and smooth lifted quartic `c`
are the actual pair in the accepted
[quintic structural frontier](2026-10-11-session-quintic-structural-frontier.md),
with the exhaustive
[intrinsic pair classification](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md)
and its
[explicit-model audit](2026-10-11-session-dp5-a4-explicit-model-independent-audit.md).
The unique line is `ell`; the only surface singularity is A4. Its actual
anticanonical sections satisfy `div(U0)=5ell`, `div(hsec)=c+ell`.
Consequently `S minus ell` is the complete open chart `A2(r,T)`, with
`c:T=0` there.

In the endpoint lane the actual four projection sections are

    X0=1+aT,
    X1=r+bT,
    X2=r^3+(g-r)T,
    X3=r^4+(d-r-2r^2)T+T^2.

Assume `a != 0` and that the line center avoids S. The claim is that some
actual point of S outside c maps into

    C0=[s^4:s^3t:st^3:t^4].

This suffices to exclude a mate of every positive degree. As independently
proved in the structural frontier, an integral quintic is regular at the
generic point of C0: twice C0 on its unique quadric would leave the
noneffective class `(3,-1)`. Thus c is the unique dominating curve over C0.
For a mate G, the actual normalized divisor is `5k c` with `deg(G)=4k`.
The zero set of its pullback is therefore c. Every point over C0 must vanish
under that pullback, giving the necessary full inverse-support condition

    (pi^(-1)(C0))_red=c.

This argument concerns actual support, including isolated inverse points.
It does not replace that condition by equality of the dominating curve only.

On ell the projection is `[0:0:U3:U4]`, an isomorphism onto the line
`X0=X1=0`. That target line meets C0 set-theoretically only at
`[0:0:0:1]`; its preimage on ell is the A4 point, which lies on c. Thus
the open-chart argument below loses no possible extra endpoint fiber by
ignoring ell. More importantly, the contradiction constructs its extra
point in the actual A2 chart itself.

## 2. The projective infinity fiber is settled before division

Put

    Cb=a^2 g-ab-b^3,
    Db=a^3 d-b^4-2ab^2-a^2 b-a^2.

The actual affine point `(r,T)=(b/a,-1/a)` lies off c. Its projection has

    X0=X1=0, X2=-Cb/a^3, X3=-Db/a^4.

If Cb=Db=0 this is a base point, contrary to center avoidance. If Cb=0
and Db is nonzero, it maps to the actual endpoint `[0:0:0:1]` of C0.
Hence full inverse support forces `Cb != 0`. This proves the discarded
chart boundary impossible; it is not an unexamined saturation condition.

## 3. Every root of the exact septic gives a residual fiber

For a finite target point `[1:z:z^3:z^4]`, its second-coordinate equation
gives `r=z+AT`, where

    A=az-b,
    U=2az^3-3bz^2-z+g,
    V=3az^4-4bz^3-2z^2-z+d,
    H=az^3+z-g-1,
    J=AV-(Az-1)U.

Substitution in the last two target-coordinate equations gives exactly

    X2-z^3 X0=T P,
    X3-z^4 X0=T R,
    P=U+A(3zA-1)T+A^3 T^2,
    R=V+(6z^2 A^2-4zA-A+1)T+(4zA^3-2A^2)T^2+A^4 T^3.

The exact linear elimination identity is

    A R-(A^2 T+Az-1)P=J+A^2 H T.

Define

    E=J^2-(3zA-1)HJ+AUH^2.

Direct expansion, independently checked, gives degree seven in z and
leading coefficient `a Cb`. Thus its degree stays exactly seven for every
parameter value now under consideration, and no root at infinity can
absorb a missing finite degree.

At `A=0`, the exact specialization is `E=az^3+z-g=-Cb/a^2`, so no
root of E is lost by division by A. Also the cleared identity

    a^2 P(-1/a)=Cb

proves that no residual P,R solution has `X0=0` on the present locus.

If `E(rho)=0` with `H(rho) != 0`, put
`T=-J/(A^2 H)` and `r=rho+AT`. The identity

    A H^2 P-E
      =(A^2 H T+J)(A^2 H T-J+(3zA-1)H)

gives `P=0`; the linear identity gives `R=0`. Since `X0 != 0`, this is
a defined point mapping to the specified finite point of C0. Under full
inverse support it must have `T=0`, which forces `U(rho)=V(rho)=0`.

If `H(rho)=0`, then `E(rho)=0` forces `J(rho)=0`. Every root of the
genuine quadratic P is then a root of R. None can have `X0=0`. Under full
inverse support all these roots must be zero, so `U=0` and `3rho A=1`.
At a common root the identity `H=3rho^2 A-1-U` now gives `rho=1`,
`A=1/3`. Then `V=0` as well, giving the complete exceptional family

    b=a-1/3, g=a, d=a+5/3.

The exact expansion of E at z=1 has first nonzero coefficient `1/9` in
degree two, independently of a. Thus this exceptional compatible root has
order exactly two. Every other H-zero septic fiber already gives an
off-curve point.

We have proved the global necessary support assertion:

    Supp(E) is contained in the common geometric roots of U,V.

The cubic U has leading coefficient `2a != 0`, so that support has at most
three distinct points.

## 4. Full higher coefficients give order at most four

At a common root rho put `w=a rho-b`, `q=w rho`. The equations U=V=0
give the exhaustive substitution

    b=a rho-w,
    g=a rho^3-3w rho^2+rho,
    d=a rho^4-4w rho^3+2rho^2+rho.

The exact identity

    Cb=w*(a(1-3q)+w^2)

excludes `w=0`; this is the `k=b-a rho=0` stratum in the opposite
sign convention. If `c_j` is the coefficient of `(z-rho)^j` in E,

    H(rho)=3w rho^2-1,
    c1=-H(rho)*(6q^2-6q+1+3wq).

The H-zero case was settled above with compatible order exactly two.
In the remaining case, order at least two forces

    D=6q^2-6q+1,
    w=-D/(3q), rho=q/w.

Here `q != 0` and `D != 0`: otherwise the defining equation would be
one or would force w=0. Furthermore

    H(rho)=-(3q-1)(3q^2+3q-1)/D.

Hence `3q-1` and `B=3q^2+3q-1` are nonzero on this branch. In these
parameters c2 is affine linear in a with nonzero slope

    -3q B(3q-1)^2/D^2.

Order at least three therefore forces exactly

    a=-D^2*(54q^4-72q^3+15q^2-3q+1)/(27q^3(3q-1)^2).

The final coefficients c3,c4 and their explicit numerator polynomials are
displayed in the
[independent target-contact audit](2026-10-11-session-endpoint-two-common-roots-target-contact-independent-audit.md).
I inspected that proof and its source. It derives the coefficients from E
itself and proves the exact polynomial gcd statements

    gcd(num(c3),num(c4)) is a nonzero rational multiple of D,
    gcd(num(c3),num(Delta)) is a nonzero rational multiple of D,

where `Delta=Res_z(U/(z-rho),V/(z-rho))` at the same forced parameters.
All rational denominators are products of nonzero rational constants,
powers of q and powers of `3q-1`; none vanishes on the branch. The quotient
polynomials have their actual degrees two and three since `a != 0`.
These are exact coprimality assertions valid after every allowed algebraic
specialization, not generic-rank checks or numerical samples.

Since D is nonzero, c3 and c4 cannot both vanish. Thus every compatible
root has order at most four. If its order is four, then c3=0 forces
`Delta != 0`, so there can be no other common U,V root. The assertion also
includes an additional common multiplicity at rho: that would make the
two quotients share rho and force their resultant to vanish.

This is the corrected bound. The preliminary bound of three was false and
is not used. No order estimate is inferred from first-normal degree.

## 5. Exhaustion of the number of common roots

There are four possible counts of distinct common roots of U,V:

* Zero: a nonconstant degree-seven E cannot have support in the empty set.
* One: its order is at most four, less than seven.
* Two: neither can have order four, because that would prohibit the second.
  Their orders are therefore at most three each, totaling at most six.
* Three: all cubic roots are distinct, so U divides V. Long division forces
  `a=3b^2/2`, `g=1/(9b)-2/3`, `d=1/(54b^2)-1/(9b)`, with b nonzero.

In the final case `Cb=-3b^3(2b+3)/4`, so `b != -3/2`. Write E=US.
The residual S has degree exactly four throughout this locus. The
[original-variable audit](2026-10-11-session-three-common-roots-residual-quartic-independent-audit.md)
and its independent
[shifted-variable certificate](2026-10-11-session-endpoint-three-common-roots-shifted-replay.md)
give exact incompatible resultants: if every root of S were a root of U,
the two polynomials would share a root, while S would have a repeated root
because a quartic is supported at at most three points. Their resultant
and the derivative resultant of S would both vanish, but their retained
parameter factors are coprime in QQ[b]. Their leading coefficients stay
nonzero on `b != 0,-3/2`. Thus there is no missing degree-drop or repeated-
root exception. The corrected positive sign in `a=3b^2/2` is essential;
the earlier exploratory negative sign is explicitly rejected.

Every possible common-root count contradicts the necessary support
assertion. Consequently every admissible displayed endpoint projection with
`a != 0` has an actual point outside c mapping into C0. Its mate is excluded
in every degree.

## 6. Independent evidence and bounded acceptance

My separately written
[geometry checker](../validation/2026-10-11-endpoint-support-global-audit/verify_geometry.m2)
has SHA-256
`5e786b80c301f98a0aa34a360190d4596fbe52d9ae8e9e0df0e9050e1adc4de2`.
Its final execution passed **16 exact identities**. The
[captured execution](../validation/2026-10-11-endpoint-support-global-audit/attempts/20261012T000749690971Z/execution-record.json)
binds the source snapshot and raw stdout/stderr. Four earlier failed
development versions are retained: a protected variable name, a parsed
multiline omission, a nested-ring fraction-field construction, and an
incompatible ring substitution. The final source uses a flat polynomial
ring and cleared polynomial evaluations throughout. No failed execution
supplies an accepted certificate.

The delegated independent target-contact source has SHA-256
`c08e6512379953227600fb176164148d52acd3ce3fe7e9ec00a51b5526d5c5db`.
It passed **14 exact assertions** in
[its final captured execution](../validation/2026-10-11-endpoint-support-global-audit/two-root-contact-attempts/20261012T000753990549Z/execution-record.json).
Its prior successful development execution and intermediate failed
total-degree assertion remain preserved. These are executions of one
source, not distinct mathematical cases. The original-variable and shifted-
variable quartic certificates have their own eight- and nine-assertion
records linked above. I inspected the actual proof, final sources and
records; no audit here is based merely on the agents' final messages.

The global audit passes. Its acceptance covers only `a != 0` in the intrinsic
endpoint genus-one A4 lane. The two `a=0` subfamilies require their separate
support and jet arguments; the nonendpoint lane retains its extra modulus.
Other quintic normalizations, higher carriers and the universal STCI problem
remain open. This audit edits no prior frozen proof, canonical record or
existing evidence seal.
