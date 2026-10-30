# Quintic endpoint: residual support and local excess obstructions

## Integration guide: residual support, excess, and projective boundary

The constituent arguments separate a **proposed full-support exclusion** (whose independent global audit is pending in the retained source), explicit residual-root classifications, and higher-jet or excess-intersection tests. The [endpoint jet/power-descent dossier](QUINTIC_ENDPOINT_JETS_AND_POWER_DESCENT.md) supplies a different all-power obstruction on its own locus; [carrier factor and conormal geometry](QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md) supplies structural restrictions. Local excess and projective-boundary support must both be checked before asserting an actual mate exclusion. Preserve the proposed/proved/audited labels of each section.

---


Complete mathematical arguments, exact projective-boundary treatment, root classifications, and higher-jet calculations. This is not an assertion of a broader exclusion beyond the hypotheses of the constituent proofs.

---

## 1. endpoint a nonzero full support exclusion

# Endpoint quintic projections with a nonzero: complete support exclusion

Date: 2026-10-11 (executions continued through 2026-10-12 UTC).
Author: `oct11_endpoint_a_nonzero_support`.
Status: **COMPLETE PROOF PROPOSED, pending independent global audit**.

Work over an algebraically closed field of characteristic zero. This proof
concerns only the displayed endpoint projection of the degree-five A4
normalization. The applicability to that intrinsic endpoint lane uses the
[pair classification](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md)
and the [explicit model audit](2026-10-11-session-dp5-a4-explicit-model-independent-audit.md).
It does not exclude nonendpoint projections or all quintic surfaces.
The [quadric-factor audit](2026-10-11-session-quintic-endpoint-factor-independent-audit.md)
supplies the preceding geometric reductions, but the proof below establishes
an actual off-curve inverse point rather than relying on a first-normal
contact count. No frozen canonical source or existing seal is changed.

## 1. Claim and projective boundary

On the actual open normalization chart S minus ell=A2(r,T), let c be T=0
and consider

    X0=1+aT,
    X1=r+bT,
    X2=r^3+(g-r)T,
    X3=r^4+(d-2r^2-r)T+T^2,             a!=0.

Assume the projection center is disjoint from S. Then at least one point
off c maps into fixed C0. Consequently the full inverse-support condition
required by a mate fails in every mate degree.

Define the two parameter polynomials

    Cb=a^2*g-a*b-b^3,
    Db=a^3*d-a^2*b-2*a*b^2-b^4-a^2.

At (r,T)=(b/a,-1/a), the first two X coordinates vanish, while
X2=-Cb/a^3 and X3=-Db/a^4. If Cb=0 and Db=0 the point is a
projection base point, forbidden by center avoidance. If Cb=0 and Db!=0
it is an actual off-c point mapping to C0 at infinity, [0:0:0:1].
Thus a hypothetical full-support projection must have Cb!=0. No saturation
at X0 discards this boundary; it has been settled explicitly.

## 2. Exact target-parameter residual equations

For a finite target point [1:z:z^3:z^4], the equation X1=z X0 gives
r=z+(az-b)T. Put

    A=az-b,
    U=2az^3-3bz^2-z+g,
    V=3az^4-4bz^3-2z^2-z+d,
    h=az^3+z-g-1,
    J=A V-(Az-1)U.

After substitution, the remaining two equations, with their common factor
T removed, are

    P=U+(3zA^2-A)T+A^3 T^2,
    R=V+(6z^2A^2-4zA-A+1)T+(4zA^3-2A^2)T^2+A^4 T^3.

The exact linear remainder is

    A R-(A^2 T+Az-1)P=A^2 h T+J.

Define the target septic

    E=J^2-(3zA-1)hJ+A U h^2.

Its leading coefficient is a Cb, so Cb!=0 makes its degree exactly seven.
The fixed-degree Sylvester identity is Res_T(P,R)=A^7 E, as checked in
the separately preserved [subresultant source](../computations/verify_session_quintic_endpoint_subresultant_2026_10_11.m2).
We use the explicit remainder to retain all exceptional fibers.

At A=0 one has E=az^3+z-g. There z=b/a and
a^2 E=b^3+ab-a^2g=-Cb, so no septic root has A=0.
Also the exact cleared evaluation is

    a^2 P(-1/a)=Cb.

Thus no common residual solution can have X0=1+aT=0 on Cb!=0.
Every residual solution constructed below is a genuine finite target
fiber with a defined image.

## 3. Every septic root is a common U,V root under full support

Suppose the projection has no off-c inverse point over C0. Let rho be a
root of E. By the preceding section A(rho)!=0.

If h(rho)!=0, the actual value T=-J/(A^2 h) solves P=0, because

    A^4 h^2 P(-J/(A^2 h))=A^3 E.

The linear remainder then gives R=0. The X0 boundary is impossible, so
absence of an off-c inverse point forces T=0. Consequently U(rho)=V(rho)=0.

If h(rho)=0, the equation E=0 gives J(rho)=0. The linear remainder
now shows every root of the quadratic P solves R. Its leading coefficient
A^3 is nonzero, and no root can have X0=0. Therefore all its roots must
be T=0. This requires U=0 and 3rho A-1=0. The identity
h=3rho^2 A-1-U gives rho=1 and A=1/3. J=0 then gives V=0, hence

    b=a-1/3,       g=a,       d=a+5/3.

At this exceptional contact the first two coefficients of E at z=1
vanish and its quadratic coefficient is exactly 1/9. The septic root
therefore has order exactly two. Every other h-zero septic fiber already
contains an off-c point.

Thus under full support all seven roots counted with multiplicity must
lie among the common geometric roots of U,V. There are at most three such
points, since U has degree exactly three.

## 4. Actual higher jets bound each root by four

At a common root rho, set k=a rho-b. The coefficient of z-rho in E is

    -(3rho^2 k-1)*(6rho^2 k^2+3rho k^2-6rho k+1).

We have already settled h=0, where the only support-compatible root has
order two. Assume h=3rho^2 k-1!=0. A repeated septic root must satisfy

    6rho^2 k^2+3rho k^2-6rho k+1=0.

In particular rho and k are nonzero. Put q=k rho and

    D=6q^2-6q+1,       B=3q^2+3q-1.

The repeated-root condition is equivalent to

    k=-D/(3q),       rho=q/k.

Here q,D are nonzero. Moreover

    h=-(3q-1)B/D,

so h!=0 excludes both 3q-1=0 and B=0. At fixed q, the coefficient
e2 of (z-rho)^2 is linear in a, and its a coefficient is

    -3q B(3q-1)^2/D^2.

It is nonzero throughout this remaining stratum. Thus order at least
three forces the unique value

    a=-D^2*(54q^4-72q^3+15q^2-3q+1)/(27q^3(3q-1)^2).

At this value the next two coefficients are

    e3=-B D N9/(81q^4(3q-1)^3),
    e4=-D^2 N11/(81q^4(3q-1)^3),

where

    N9=8748q^9-20412q^8+18954q^7-8262q^6+1458q^5
       -252q^4+180q^3-66q^2+12q-1,

    N11=17496q^11-46656q^10+39366q^9-16848q^8+12123q^7
        -12231q^6+8316q^5-2934q^4+612q^3-129q^2+25q-2.

Exact polynomial arithmetic gives

    gcd(numerator(e3),numerator(e4))=D       up to nonzero scalars.

D!=0 makes simultaneous vanishing impossible. Thus every support-compatible
septic root has order at most four. This is a bound obtained from the
full third and fourth jets of the actual residual equation, not from
first-normal data. An earlier provisional message saying order at most
three was incorrect and was withdrawn before acceptance: N9 can vanish,
so order four must be retained.

## 5. An order-four root prevents every second common point

At a common root rho the exact polynomials after removing z-rho are

    U/(z-rho)=2a(z^2+rho z+rho^2)-3b(z+rho)-1,

    V/(z-rho)=3a(z^3+rho z^2+rho^2 z+rho^3)
              -4b(z^2+rho z+rho^2)-2(z+rho)-1.

At the unique a value in the preceding section, form their degree-(2,3)
Sylvester determinant Delta over QQ(q). Exact arithmetic gives

    gcd(numerator(e3),numerator(Delta))=D     up to nonzero scalars.

Consequently an order-four root (which requires e3=0) has Delta!=0.
The two quotient polynomials share no root. In particular U,V have no
second common geometric point. This also retains repeated roots at rho;
none were removed by a squarefree assumption.

There cannot be just one common point under full support: its order is at
most four but E has degree seven. There cannot be just two common points:
an order-four point would prohibit the second, while otherwise their total
order is at most six. The only remaining possibility is three distinct
common roots.

## 6. The three-common-root family is excluded

Three distinct common roots force U to divide V. Direct long division gives

    a=3b^2/2,       g=1/(9b)-2/3,       d=1/(54b^2)-1/(9b),

with b!=0. In this family Cb=-3b^3(2b+3)/4, so b!=-3/2 as well.
Write E=U S. The [independent shifted-variable support certificate](2026-10-11-session-endpoint-three-common-roots-shifted-replay.md)
proves S is a genuine quartic and cannot have all its roots among the roots
of U: its collision resultant with U and its derivative resultant have
coprime parameter factors. The separate
[original-variable audit](OCT11_12_QUINTIC_NONENDPOINT_AND_FILTRATIONS.md#source-2026-10-11-session-three-common-roots-residual-quartic-independent-auditmd)
reconstructs the same certificate. The contradiction retains repeated
roots and all allowed parameters, with no unresolved finite exceptional set.

The three cases for the number of common geometric roots are exhaustive.
Thus the supposition of full inverse support is impossible. There is an
actual off-c point over C0 for every admissible displayed a!=0 endpoint
projection, and no mate in any degree can exist for that projection.

## 7. Evidence and scope

The dedicated [target-jet checker](../computations/verify_session_endpoint_a_nonzero_target_jets_2026_10_11.m2)
passes sixteen exact assertions. They check the leading coefficient,
projective boundary evaluations, exceptional h-zero root order, first
jet, rational parameter reduction, solved second jet, exact third/fourth
jets, and both polynomial-gcd certificates. Its source hash and actual
execution, including the failed coefficient-ring comparison development
attempt, are preserved in the
[execution record](../validation/2026-10-11-endpoint-a-nonzero-support/execution-record.json).
Earlier exploratory coefficient outputs and a fraction-field construction
failure are preserved separately in the same attempt history; they are
leads, not additional certificate implementations.

This is a proposed complete support proof for a!=0 in the intrinsic
endpoint lane. Independent global proof audit must verify the rational
coefficient quantifiers and the exceptional fibers before canonical
promotion. The a=0 support/jet lanes, the nonendpoint parameter family,
other sectional genera and unrestricted quintic/higher carrier degrees
remain separate mathematical obligations.


---

## 2. endpoint a nonzero global independent audit

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
[the two-common-root target audit](OCT11_QUARTIC_DEPENDENCIES_AND_DP5_ENDPOINTS.md#source-2026-10-11-session-endpoint-two-common-roots-target-contact-independent-auditmd).
I read its final note, source, execution record, and the separate
[direct-r local-excess proof](2026-10-11-session-quintic-endpoint-a-nonzero-local-excess-bound.md).
The latter gives a second route through actual intersection lengths, but the
global argument below does not require its geometric length identification.
The proof also uses the independently implemented
[original-variable residual-quartic certificate](OCT11_12_QUINTIC_NONENDPOINT_AND_FILTRATIONS.md#source-2026-10-11-session-three-common-roots-residual-quartic-independent-auditmd)
and its
[shifted-variable replay](2026-10-11-session-endpoint-three-common-roots-shifted-replay.md).
Agent agreement alone is not used as a proof.

## 1. Exact statement and the mate implication

Work over an algebraically closed field of characteristic zero. The normal
degree-five anticanonical del Pezzo surface `S` and smooth lifted quartic `c`
are the actual pair in the accepted
[quintic structural frontier](OCT11_12_QUINTIC_NONENDPOINT_AND_FILTRATIONS.md#source-2026-10-11-session-quintic-structural-frontiermd),
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
[independent target-contact audit](OCT11_QUARTIC_DEPENDENCIES_AND_DP5_ENDPOINTS.md#source-2026-10-11-session-endpoint-two-common-roots-target-contact-independent-auditmd).
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
[original-variable audit](OCT11_12_QUINTIC_NONENDPOINT_AND_FILTRATIONS.md#source-2026-10-11-session-three-common-roots-residual-quartic-independent-auditmd)
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


---

## 3. quintic endpoint a0 polynomial support independent audit

# Independent polynomial-support audit: endpoint a=0, b!=0 is excluded

Date: 2026-10-11. Auditor: `oct11_quartic_assembly_audit`.
Status: **DIRECT COMPLETE PROOF AUDIT PASS for the displayed affine family**.
The applicability to the entire intrinsic endpoint lane uses the separately
recorded A4 pair and projection-center classification. This note does not
exclude a!=0, a=b=0, nonendpoint projections, other quintic normalizations
or the unrestricted STCI problem. No frozen source, canonical record or
integrity seal is edited.

The source audited in full is the [root's a0 support proof](2026-10-11-session-quintic-endpoint-a0-support-exclusion.md).
The [explicit model](2026-10-11-session-dp5-a4-explicit-model-independent-audit.md)
and [intrinsic pair classification](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md)
supply the normalization chart and the limited endpoint scope. Work over
an algebraically closed characteristic-zero field.

## 1. Actual residual equations and their degree-six elimination

On the actual open S minus ell=A2(r,T), the projection with a=0 is

    X0=1, X1=r+bT,
    X2=r^3+(g-r)T,
    X3=r^4+(d-2r^2-r)T+T^2,       b!=0.

The affine C0 ideal is generated by
`A=X2-X1^3` and `q=X3-X1 X2`: q together with A also generates
`X3-X1^4`. Thus the complete inverse-image test on this chart is exactly

    A=T(P-3rb^2 T-b^3 T^2), q=T(N+MT),
    P=-3br^2-r+g,
    N=-br^3-r^2-(1+g)r+d,
    M=br+1-bg.

No projective denominator is present because X0=1. An off-c point is an
actual solution of the two residual equations with T!=0, not a formal
infinitesimal point or a projection base point.

Set `R=P M^2+3rb^2 N M-b^3 N^2`. Direct leading-coefficient bookkeeping gives

    [r^6]R=-b^5,
    [r^5]R=-2b^4-3b^4=-5b^4,
    [r^4]R=-b^3(1+2b+2bg)-3b^3(2-bg)-3b^3
            =-b^3(10+2b-bg).

The three contributions to the last line come respectively from -b^3 N^2,
3rb^2 N M and P M^2. In particular R has exact degree six for every b!=0.
These equalities are direct coefficient identities, not observations at
sample parameters.

## 2. The denominator-zero fiber is retained, not saturated away

If a root r0 of R has M(r0)=0, its defining identity gives N(r0)=0.
The second residual equation then holds for every T. The first is a
quadratic in T with nonzero leading coefficient -b^3.

If P(r0)!=0, both quadratic roots are nonzero, giving an off-c point.
If P(r0)=0, the quadratic is `T(-3r0 b^2-b^3 T)`. Its other root is
nonzero because r0 cannot be zero: M(0)=0 would give g=1/b, hence
P(0)=g!=0. This also gives an off-c point.

Consequently, if no off-c point existed, every root of R would have M!=0.
At such a root the actual value `T=-N/M` solves both residual equations,
since substitution into the first gives R/M^2. Absence of off-c points
would force T=0, and therefore N=P=0. Hence every geometric root of R
would have to lie in the common zero set of P,N, with M nonzero there.

P has exact degree two, so that common zero set is empty, has one point,
or has two distinct points. The empty case is impossible because R is a
nonconstant polynomial over an algebraically closed field. The other two
cases are excluded below.

## 3. One common geometric root gives incompatible coefficients

Suppose the common zero set consists of rho, including the case where P
has a repeated root. The degree and leading coefficient force

    R=-b^5(r-rho)^6.

Comparing its r^5 coefficient gives `w=b rho=-5/6`. From P(rho)=0,

    bg=w+3w^2=5/4,       M(rho)=1-3w^2=-13/12.

Comparing r^4 coefficients gives

    10+2b-bg=15w^2=125/12,       b=5/6.

Now differentiate the actual defining R at a common P=N=0 root:

    R'=P'M^2+3rb^2 N'M.

At rho, `P'=-1-6w` and `N'=-1-(3w+6w^2)/b`. Substituting
`M=1-3w^2` gives the exact identity

    R'(rho)=-M(rho)[6w^2+(6+3b)w+1].

The alleged sixth power has derivative zero there. With w=-5/6 and M!=0,
this equation instead gives `1/6-5b/2=0`, or b=1/15. This contradicts
b=5/6. It treats all one-geometric-root gcd patterns without an assumed
simple ramification or a bound on the root multiplicity.

## 4. Two common roots reduce to one impossible quartic root

If P,N have two common distinct roots, then P divides N. Its leading
terms determine the quotient, and comparing the remaining coefficients
gives exactly

    N=(r/3+2/(9b))P,
    g=1/(6b)-3/4,       d=2g/(9b).

Put `w=br`, `gamma=bg`, `p=gamma-w-3w^2=bP` and
`m=1-gamma+w=M`. Substitution in R gives the actual factorization

    R=P S,
    S=m^2+(w^2+2w/3)m-p(w/3+2/9)^2.

Its leading coefficients are

    [w^4]S=1/3,
    [w^3]S=1+5/9=14/9.

Thus S is a nonconstant quartic for all these parameters. The necessary
root condition from Section 2 makes each root of S a root of p, with m
nonzero. At a root of p one has gamma=w+3w^2, and the displayed S reduces
exactly to

    S=(1-3w^2)(1-2w^2+2w/3).

The first factor is m, which is nonzero by the denominator-fiber analysis.
Every root of S must therefore also be a root of
`J=1-2w^2+2w/3`. The two distinct roots of p have sum -1/3, whereas the
two roots of J have sum 1/3. These quadratics cannot share both roots.
Their common geometric zero set consequently has at most one point.

Since S has degree four, it must have exactly one root w0 and therefore
`S=(1/3)(w-w0)^4`. Its w^3 coefficient gives w0=-7/6. But direct
substitution gives `J(-7/6)=-5/2`, which is nonzero. This contradicts the
required root condition and exhausts the two-common-root case.

## 5. Complete conclusion and bounded attribution

All possible common-zero patterns of P,N are contradicted. Hence the
displayed affine map has an actual point T!=0 above C0 for every b!=0
and all g,d. For an admissible finite normalization projection that point
violates the full inverse-support condition required by a mate in any
degree. The proof does not require a reduced conductor, a flat conductor
cover, a bounded descending exponent, or any generic parameter condition
beyond b!=0.

This direct audit independently reconstructs the denominator-zero fiber,
the three leading elimination coefficients, the one-root derivative and
coefficient incompatibility, the exact P|N quotient, and the S/J root
contradiction. No new script, symbolic run or numerical count is claimed;
the coefficient calculations are included explicitly as the proof.

The entire endpoint family does not close here. The a=b=0 jet-descent
problem, the a!=0 seven-excess contact reduction and the nonendpoint
projection-center parameter retain their separately recorded status. In
particular this support proof does not substitute for the intrinsic pair
classification or establish an unrestricted quintic-carrier theorem.


---

## 4. quintic endpoint a0 support exclusion

# Endpoint quintic projections with a=0,b!=0: complete full-support exclusion

Date: 2026-10-11. Author: root.

Status: **DIRECT COMPLETE ALGEBRAIC PROOF for the displayed family;
pending independent proof and coefficient audit**. Characteristic zero,
algebraically closed field. This is the endpoint placement of the A4
point on fixed C0, in the intrinsic affine normalization chart. It is
not the nonendpoint placement and it does not treat a!=0.
No mathematical execution is claimed by this note.

## 1. Claim and actual affine inverse image

Use the affine normalization chart S minus ell=A2(r,T), with c:T=0,
and the endpoint projection

    X0=1,
    X1=r+bT,
    X2=r^3+(g-r)T,
    X3=r^4+(d-2r^2-r)T+T^2,             b!=0.

For every b!=0,g,d this map sends at least one point with T!=0 to
the affine C0=[1:z:z^3:z^4]. Consequently any admissible finite
normalization projection in this family fails the full inverse-support
condition forced by a mate, in every mate degree.

The affine ideal of C0 is generated by A=X2-X1^3 and
q=X3-X1 X2. Exact expansion gives

    A=T(P-3rb^2T-b^3T^2),
    q=T(N+MT),
    P=g-r-3br^2,
    N=d-r^2-(1+g)r-br^3,
    M=1-bg+br.

Thus the problem is whether the two residual equations have a point
with T!=0. Put

    R=P M^2+3rb^2 N M-b^3N^2.             (1)

Its leading term is -b^5 r^6, so R has six roots counted with
multiplicity. Its next two coefficients are

    [r^5]R=-5b^4,
    [r^4]R=-b^3(10+2b-bg).                (2)

## 2. Denominator zero never conceals a successful residual fiber

If M(r0)=0 and R(r0)=0, then (1) gives N(r0)=0. At r=r0 the
second residual equation vanishes for every T. The first has degree
two with nonzero leading coefficient -b^3. If P(r0)!=0, its roots
are nonzero. If P(r0)=0, it is

    T(-3r0 b^2-b^3T).

Here r0!=0: M(0)=0 would give g=1/b and P(0)=g!=0. Hence it
again has a nonzero root. Every root of R at M=0 therefore gives
an actual off-c inverse point.

Suppose for contradiction that no off-c inverse point exists.
Every root r0 of R must then have M(r0)!=0, and setting
T=-N/M solves both residual equations. The absence of off-c
points forces N(r0)=0, hence P(r0)=0. Therefore

    every root of R lies in the common zero set of P and N,
    and M is nonzero at every root of R.          (3)

Since P has degree two, its gcd with N has degree zero, one or two.
Degree zero contradicts the existence of roots of R immediately.

## 3. A single common root is impossible

If the common zero set consists of just rho (including a double root
of P), (3) and the leading coefficient force

    R=-b^5(r-rho)^6.

The r^5 coefficient in (2) gives w=b rho=-5/6. From P(rho)=0,

    g=rho+3b rho^2=5/(4b), M(rho)=-13/12.

Comparing r^4 coefficients gives

    10+2b-bg=15w^2=125/12,
    b=5/6.                                    (4)

But differentiating (1) at the common root, using P=N=0, gives

    R'(rho)=-M(rho)[6w^2+(6+3b)w+1].

The alleged sixth power has R'(rho)=0. With w=-5/6 and M!=0
this instead forces b=1/15, contradicting (4).

This covers every degree-one gcd and a degree-two gcd with just one
geometric root. It does not assume simple projection ramification.

## 4. Two common roots are impossible

The only remaining case is P|N with two distinct roots. Polynomial
division gives the necessary identities

    g=1/(6b)-3/4, d=2g/(9b),
    N=(r/3+2/(9b))P.

Set w=br, gamma=bg and

    p=gamma-w-3w^2, m=1-gamma+w.

Equation (1) factors as R=P S, where

    S=m^2+(w^2+2w/3)m-p(w/3+2/9)^2.       (5)

S is a quartic, with

    [w^4]S=1/3, [w^3]S=14/9.              (6)

Every root of S must be a root of p by (3), and none may have m=0.
At a root of p, gamma=w+3w^2 and (5) becomes

    S=(1-3w^2)(1-2w^2+2w/3).

The first factor is exactly m at that root, and is nonzero by (3).
Thus every root of S must be a common root of p and

    J=1-2w^2+2w/3.

The two roots of p have sum -1/3, while the two roots of J have
sum 1/3. These quadratics cannot share both roots. Hence S must
have just one geometric root w0, and (6) forces

    S=(1/3)(w-w0)^4, w0=-7/6.

Yet J(-7/6)=-5/2 is nonzero. This contradiction exhausts the
last case. The argument proves existence of an off-c affine inverse
point for every displayed b!=0,g,d.

## 5. Scope and continuation

For an actual STCI mate on a finite normalization, the reduced full
inverse image of C0 must be its unique lifted curve c. The off-c point
above violates that condition, regardless of mate degree or any
conductor reducedness/flatness hypothesis. All displayed affine
points have X0=1, so none can be discarded as an infinity point or
a projection base point.

The companion a=b=0 family requires an arbitrary-power jet
obstruction at the unique line ell; no claim about it is derived
from this polynomial support proof. The endpoint a!=0 family and
the nonendpoint delta family remain separate obligations.

The [intrinsic pair classification](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md)
states the endpoint/nonendpoint distinction. Its written geometric
exhaustion and the explicit affine-model audit, rather than this
degree-six computation, supply the global normalization applicability.


---

## 5. endpoint three common roots shifted replay

# Endpoint three-common-root family: shifted-variable support certificate

Status: **PROVED, exact univariate algebra in characteristic zero.** This
note excludes the polynomial support condition in the corrected `U | V`
family. The parent's geometric identification of that condition and the
other common-root strata are separate obligations.

## Correct family and sign correction

For

\[
U=2az^3-3bz^2-z+g,\qquad
V=3az^4-4bz^3-2z^2-z+d,
\]

with `a != 0`, ordinary long division gives

\[
V-\left(\frac32z+\frac b{4a}\right)U
=\left(-\frac12+\frac{3b^2}{4a}\right)z^2
 +\left(-1-\frac32g+\frac b{4a}\right)z
 +d-\frac{bg}{4a}.
\]

Thus `U | V` requires and is equivalent to

\[
a=\frac32b^2,\qquad
g=\frac1{9b}-\frac23,\qquad
d=\frac1{54b^2}-\frac1{9b},\qquad b\ne0.
\]

The initially supplied negative sign for `a` was an exploratory error and
is rejected. It gives a nonzero `z^2` remainder. The corrected family has

\[
C_b=a^2g-ab-b^3=-\frac34b^3(2b+3).
\]

The admissible locus `C_b != 0` is therefore exactly `b != 0,-3/2`.

## Cleared polynomials and incompatible necessary resultants

Set

\[
A=az-b,\quad h=az^3+z-g-1,\quad J=AV-(Az-1)U,
\quad E=J^2-(3zA-1)hJ+AUh^2.
\]

Because `U | V`, one has `U | J` and `U | E`. Write `S=E/U`.
The change of variable `x=3bz-1` is invertible for every allowed parameter.
The exact cleared expressions are

\[
p=9bU=x^3-6x-6b-4,
\]

\[
\begin{aligned}
q=432bS={}&-(4b+6)x^4-(14b+9)x^3-48bx^2\\
&+(24b^2-26b+15)x-24b^2-340b.
\end{aligned}
\]

Hence `p` has degree three and `q` has degree four on the entire allowed
locus. Direct exact determinants of the two degree-seven Sylvester matrices
give

\[
\operatorname{Res}_x(p,q)=-1458R(b),\qquad
\operatorname{Res}_x(q,q')=7776D(b),
\]

where

\[
R=(12b^2+116b+3)(72b^4+252b^3+1126b^2+513b+54),
\]

\[
\begin{aligned}
D={}&(2b+3)(2b^2+9b+15)^2\\
&\cdot(9216b^6-208896b^5-2002096b^4-2800992b^3
-117672b^2+72b+45).
\end{aligned}
\]

Exact polynomial arithmetic in `QQ[b]` gives `gcd(R,D)=1`.

If every root of `q` were a root of `p`, they would share at least one root,
and the quartic `q` would have a repeated root because its distinct roots
would lie among at most three cubic roots. Both resultants would vanish.
Their nonzero constant factors and the coprimality of `R,D` make that
impossible. Thus **there is no allowed parameter with
`Supp(S) subset Supp(U)`**, including parameters with repeated roots of `U`.
Since `E=US`, this also proves that `E` has a root outside `U` throughout
the allowed family. There is no exceptional finite parameter set.

## Independent computation and preserved execution history

The source
[verify_session_endpoint_three_common_roots_2026_10_11.m2](../computations/verify_session_endpoint_three_common_roots_2026_10_11.m2)
has SHA-256
`31597e4c2057fabb87f9aaf76fdd562f1d5753cf75141dc0f85dfc3041eb97a1`.
Its final captured execution passes **nine exact assertions**: the two
divisibilities, the shifted cubic, the quotient, the carrier coefficient,
the shifted quartic, both resultant identities and their coprimality.

The [execution record](../validation/2026-10-11-endpoint-three-common-roots/execution-record.json)
retains five captured source snapshots with stdout and stderr. The first
failure is a fraction-field construction error; the second is an unsupported
generic polynomial-gcd call; the third is a coefficient-ring construction
error caught by a failed resultant assertion. In that third attempt,
`coefficient(x^k, f)` in `QQ[b,x]` discarded terms with positive powers of
`b`. The final construction uses `QQ[b][x]`, retaining the full coefficient
polynomials. Attempt four passes the development assertions; attempt five
passes the final nine assertions and checks the exact nonzero resultant
constants. All failures remain preserved. An initial uncaptured invocation
of the same failed source as attempt one appears in the tool transcript;
it supplies no additional certificate.

The separate
[residual-quartic independent audit](OCT11_12_QUINTIC_NONENDPOINT_AND_FILTRATIONS.md#source-2026-10-11-session-three-common-roots-residual-quartic-independent-auditmd)
works directly in the original variable `z` and obtains the same parameter
factors, with its own captured eight-assertion source. The two sources are
independent implementations of this algebraic certificate; execution
snapshots of either source are copies, not additional implementations.


---

## 6. quintic endpoint a nonzero local excess bound

# Endpoint a!=0: full-jet excess bound and exclusion with at most two contacts

Date: 2026-10-11. Author: `oct11_endpoint_a_nonzero_support/a_nonzero_local_excess`.
Status: **DIRECT LOCAL-INTERSECTION PROOF WITH EXACT ALGEBRAIC CERTIFICATES;
pending independent audit**. This note changes no canonical or frozen record.
It proves the displayed endpoint a!=0 full-support condition impossible when
U and W have at most two distinct common roots. It does not by itself treat
the three-common-root stratum or nonendpoint projection centers.

## 1. Scope and retained transverse equations

Use the actual endpoint projection and center-avoidance hypotheses in the
[quadric-factor reduction](2026-10-11-session-quintic-endpoint-quadric-factor-reduction.md)
and its [independent audit](2026-10-11-session-quintic-endpoint-factor-independent-audit.md).
On the smooth affine normalization chart the coordinates are

    X0=1+aT, X1=r+bT,
    X2=r^3+(g-r)T, X3=r^4+(d-2r^2-r)T+T^2.

Work over an algebraically closed field of characteristic zero, with a!=0,
and assume for contradiction full reduced inverse support of C0 is c:T=0.
The two exact residual equations are

    K=ar^4-br^3-r^2-(1+g)r+d
      +T*(1+ad-bg-2ar^2-ar+br)+aT^2,
    E=U+T*P1+T^2*P2,
    U=g-r-3br^2+2ar^3,
    W=K(r,0)=ar^4-br^3-r^2-(1+g)r+d,
    P1=a^2r^3+2a(g-r)-3b^2r,
    P2=a^2(g-r)-b^3.

Indeed q pulls back to TK and X0^2 X2-X1^3 pulls back to TE. These
identities retain every transverse term. The factor audit proves that
the total excess intersection length length(O_D/(E)) is seven, all
supported at finite common roots of U and W, where D=V(K) is integral.
The present proof bounds these actual excess lengths, not their first jets.

## 2. Endpoint avoidance and the resultant's harmless chart factor

Put Cb=a^2g-ab-b^3. If Cb=0, the actual affine point

    r=b/a, T=-1/a

has X0=X1=X2=0. If also X3=0 it is a projection base point, contradicting
center avoidance. Otherwise it maps to the endpoint [0:0:0:1] of C0
and lies off c, contradicting full inverse support. Thus Cb!=0.

The exact resultant in the actual transverse variable factors as

    Res_T(K,E)=(ar-b)^2 H(r),
    deg H=7, [r^7]H=-a^4.

The square factor arises from the point with X0=X1=0 in the cubic-plus-
quadric target equations; those two equations alone also vanish along
the target line X0=X1=0. The factor is not silently interpreted as C0.

At a common root rho of U and W, set w=a rho-b. Substitution of U(rho)=0
gives the exact identity

    Cb=w*(a+w^2-3aw rho).

Consequently w!=0 at every possible excess support point. The factor
(ar-b)^2 is therefore a unit near rho and can be removed there.

The order of H at rho equals the total local intersection length of K,E
in the r-fiber over rho. To justify this even when D is singular, K/a is
monic quadratic in T. Over the DVR k[[r-rho]] the algebra defined by K/a
is free of rank two, and the resultant is, up to a nonzero scalar, the
determinant of multiplication by E. When the resultant is not identically
zero, the determinant's valuation is the length of its cokernel. Splitting
the finite fiber gives the sum of the local intersection lengths. H has
nonzero leading coefficient, so this finiteness condition holds.

Under full support, any common point of K,E in this fiber with T!=0 and
X0!=0 would map to affine C0 and is excluded. A point with X0=0 must have
X1=0 to satisfy the pulled cubic, hence r=b/a; this does not occur at rho
because w!=0. Thus the only supported common point in the rho-fiber is
(rho,0), and ord_rho H is exactly the actual excess length at that point.
This includes a double K-root at T=0 and singular D.

## 3. The second transverse root excludes one derivative factor

Write r=rho+s. The equations U(rho)=W(rho)=0 determine

    g=rho+3b rho^2-2a rho^3,
    d=rho+2rho^2+4b rho^3-3a rho^4.

At s=0 the full equations become

    K=T*(M+aT), E=T*(P1+P2T),
    M=1-3rho^2w^2,
    P1=-3rho w^2, P2=-w^2*(3a rho-w).

Define

    S1=1+3w rho^2*(3a rho-w),
    S2=1-6w rho+3w^2rho*(2rho+1).

Exact expansion of H gives

    [s]H(rho+s)=-w S1 S2,
    aP1-MP2=-w^3 S1.

If S1=0 then rho!=0, since S1=1 at rho=0. Also M!=0: if M=0,
the second identity gives aP1=0, impossible with a,w,rho all nonzero.
The second K-root T=-M/a is therefore nonzero and is also an E-root.
At this point X0=1-M=3rho^2w^2!=0, so it is an actual off-c point
mapping to affine C0. Full support consequently forces S1!=0.

Thus an excess length at least two requires S2=0. S2 is the exact
Jacobian determinant of K,E at (rho,0), but only serves here to
parametrize the higher-jet analysis that follows; no order bound is
inferred from this determinant alone.

## 4. All multiple-contact parameters and their higher coefficients

Assume S2=0 and put q=w rho. Necessarily q!=0. Solving S2 gives

    D=6q^2-6q+1,
    w=-D/(3q), rho=q/w.

D!=0 because w!=0. These formulas exhaust S2=0, including singular
residual-curve cases; they impose no smoothness assumption on D_K.

Let c_j=[s^j]H(rho+s). The exact coefficient c_2/S1 is

    ((243q^5-162q^4+27q^3)*a
      +1944q^8-6480q^7+8316q^6-5292q^5+1890q^4
      -468q^3+99q^2-15q+1)/(81q^4).

At q=1/3 this expression is -1/27 for every a. Hence that entire
exceptional parameter case has excess length exactly two. In particular
it is not lost by division by 3q-1.

For q!=1/3, excess length at least three forces the unique value

    a=-D^2 A4/(27q^3(3q-1)^2),
    A4=54q^4-72q^3+15q^2-3q+1.

At this value the exact next coefficient and the remaining unit factor are

    c_3=D^3 N6 N9/(2187q^7(3q-1)^4),
    S1=-N6/(3q-1)^2,
    N6=162q^6-216q^5+72q^4-27q^3-3q^2+6q-1,
    N9=8748q^9-20412q^8+18954q^7-8262q^6+1458q^5
       -252q^4+180q^3-66q^2+12q-1.

The retained denominator conditions q!=0,D!=0,q!=1/3 and S1!=0
are all explicit. The original a!=0 and Cb!=0 remain in force;
excluding further parameter values cannot weaken the bound below.

## 5. Exact certificates prove order at most four and uniqueness at order four

Let J be the resultant in s of the two quotient polynomials

    U(rho+s)/s, W(rho+s)/s.

After substituting the forced a from Section 4, compute c_3,c_4,J as
elements of QQ(q), retaining their actual numerators. The exact identities are

    gcd(num c_3,num c_4)=D^3,
    gcd(num c_3,num J)=D^3.

These are not numerical samples. The [fourteen-check M2 source](../computations/verify_session_quintic_endpoint_a_nonzero_local_excess_2026_10_11.m2)
derives both numerators directly from the retained full equations and
exports their rational coefficient lists. The independently generated
[Bezout certificates](../validation/2026-10-11-quintic-endpoint-a-nonzero-local-excess/bezout-certificates.json)
give, for each displayed pair, explicit polynomial multipliers over QQ
whose combination is D^3. A standard-library Fraction verifier multiplies
the exported polynomials and checks both identities exactly. Thus neither
pair can simultaneously vanish when D!=0.

If the excess length were at least five, then c_3=c_4=0, contradicting
the first certificate. Therefore every excess length is at most four.

If an excess length is four, then c_3=0. The second certificate forces
J!=0. Consequently the two quotient polynomials have no common root
over the algebraically closed field. Any other common U,W root would
give such a root; even an additional common multiplicity at rho would
do so at s=0. Thus an order-four excess forces rho to be the only common
root of U,W, with no additional common multiplicity.

## 6. Consequence for at most two distinct common roots

If there are no common roots, the necessary seven-excess condition fails.
If there is just one common root, its excess is at most four, again less
than seven. If there are two distinct common roots, neither can have
excess four, since that would force it to be the only common root.
Each then has excess at most three, for a total at most six. This is
also less than seven. Repeated roots and singular residual curves are
already covered by actual intersection lengths in Sections 2--5.

Hence full inverse support is impossible throughout the endpoint a!=0
family with at most two distinct common U,W roots. The three-distinct-
common-root family remains a separate obligation in this note.

## 7. Execution provenance and failure corrections

The [execution record](../validation/2026-10-11-quintic-endpoint-a-nonzero-local-excess/execution-record.json)
binds the final checker source, its snapshot, commands, raw streams,
four recorded source-version executions, and the two Bezout checks.
The source has SHA-256
`84d8ffa69ff8e74f971112cc3a8e18efe33832af8c6ed5ab0bd0a8b26c67fccd`.
The recorded final run returned zero with fourteen passing M2 checks.
There is one mathematical M2 checker; its recorded replays and source
copies do not constitute additional distinct checker results.

Three failed source versions are preserved. The first two assertions
failed because unparenthesized multiline M2 assignments silently omitted
the following-line terms. An initial tentative quotient-ring diagnosis
was superseded by inspection of the actual parsed equations. Parentheses
repaired the source; the fraction-field presentation was retained and
every resulting rational identity is interpreted with the explicit
nonzero conditions above. The third version passed all fourteen checks
but failed while exporting coefficients because q had the wrong ring
binding. Rebinding to QQ[q] repaired only that export.

Earlier scratch resultant and parameter scripts are exploratory leads,
not additional accepted theorem certificates. The source's exact identities
and Bezout certificates support the algebraic calculations; the preceding
local determinant and support arguments supply the geometric quantifiers.
