# Independent audit: automatic qhigh and the shared logarithmic ODE

Date: 2026-10-15.

Status: **PASS. The coefficient ideal (q5,q6) is the unit ideal on the
declared actual localized domain. The eight ODE equations give an
equivalent incidence scheme, with unique witness coefficients, and
both proposed accelerator equations belong to the same localized
ideal.** The statements hold over nonreduced parameter bases as well
as at geometric points.

The reviewed proposal is
[the automatic-open and ODE note](2026-10-15-generalization-quintic-h2-automatic-open-and-ODE.md).
All previous accepted h2 factor, reciprocal-coordinate, A4, closed-lane
and eleven-generator results are premises. No accepted verifier or
actual coefficient construction was replayed. This audit checks only
the new ideal membership, ODE presentation and its ring-level scope.

## 1. The precise actual ring and the q5 congruence

Let A be the actual finite h2 inverse-map parameter ring over the
characteristic-zero ground field, localized at the previously declared
factors: delta, the cover determinant, the cofactor determinant,
recorded denominator/content scalars and Delta1. These are the
original inverse-map conditions together with the newly justified
necessary Delta1 open. No division by j=Jbar is made.

Use the actual monic factorization

    Fsrc=H*Qactual,       H=t^2+vst+ws^2.

Near A4 use p=s/t. In this chart H=1+vp+wp^2, and write F0,F1 for
the constant and linear coefficients of the actual F(p). The constant
and linear coefficients of Qactual are Qactual6 and Qactual5, so

    Qactual6=F0=-3j Delta1,
    Qactual5=F1-vF0.                                  (1)

This concerns coefficients t^8 and s*t^7 of the homogeneous octic;
the p coefficient is taken in the t=1 chart. The reciprocal source
coordinate introduces no further interchange here.

Put S0=G+3delta^2 and L0=G+delta^2+2B. The accepted actual A4
coefficient identity and literal Delta1 formula give

    Delta1=G*S0*L0+j*Psi,
    Qactual5=-2*S0*Delta1+j*T                         (2)

for regular Psi,T in A. In particular, the second congruence is
valid for the actual source sextic: modulo j, (1) gives
Qactual5=F1=-2G L0 S0^2=-2S0 Delta1. The relation is a congruence
in the ring, not merely an assertion on reduced points of j=0.

For the captured sextic, Q=kappa*Qactual with kappa the recorded
commonDen/delta^4, a unit on this domain. Consequently

    q5=-2*kappa*S0*Delta1 modulo j,
    q6=-3*kappa*Delta1*j=eta*j,       eta a unit.       (3)

This proves the exact captured-q5 scope requested in the new claim.

## 2. An explicit membership proves unimodularity

Equations (2) give the exact identity

    Delta1^2+(G*L0/2)*Qactual5
       =j*[Psi*Delta1+(G*L0/2)*T].                    (4)

Every coefficient is regular in A, and 2 is a unit. Since Delta1
is a unit, (4) proves (j,Qactual5)=A. Multiplication by the units
in (3) then gives

    (q5,q6)=(Qactual5,j)=A.                            (5)

This is equality of ideals, with no radical operation or reducedness
assumption. Equivalently, in the quotient by (q5,q6), relation (3)
first gives j=0 and then S0=0, while (2) makes the unit Delta1
zero, forcing the quotient to be the zero ring. Equation (4)
supplies the direct ideal-membership version of that argument.

Thus a separate saturation or inequation for (q5,q6) is redundant
after this one declared domain localization. This does not say the
ideal is the unit ideal before Delta1 and the original denominator
factors are inverted. The same argument does not require S0 to be
inverted as an additional global domain factor.

## 3. The cubic rank condition has globally unique witnesses

The first two columns sQ,tQ have two fixed coefficient pivots

    A56=q5^2-q4*q6,       A67=q6^2,

with q5^4=A56*(q5^2+q4*q6)+q4^2*A67. By (5), these two pivot
determinants generate the unit ideal. Thus their principal opens
cover the entire localized parameter scheme, including after
quotienting by a nonreduced cubic-rank ideal.

On either pivot open, vanishing of the cubic minors of [sQ,tQ,W]
gives unique coefficients lambda,mu with

    W=lambda*sQ+mu*tQ.                                (6)

The uniqueness makes these coefficients agree on overlaps. They
therefore glue to global elements of the affine quotient ring.
This proves that adjoining the two witness coefficients in (6)
gives an incidence scheme isomorphic to the cubic determinantal
scheme, rather than only a projection with the same field-valued
points. No global pivot coefficient is arbitrarily chosen.

For H=t^2+vst+ws^2 and Q of degree six, the exact homogeneous action
identity is

    W=D_(sH)Q=6H_t Q-3H Q_t.

Thus set u=(6v-lambda)/3 and d=(12-mu)/3. The characteristic-zero
ground field makes 3 invertible. Equation (6) is exactly

    H Q_t=(us+dt)Q,                                   (7)

and the correspondence between (lambda,mu) and (u,d) is invertible.
The ODE witnesses are therefore globally unique as well. This
argument uses algebras over the stated field; mere torsion-free
characteristic zero, without 3 invertible, would not suffice.

## 4. All eight coefficients and the accelerators

On s=1, write h=x^2+vx+w and q=sum_(i=0)^6 q_i*x^i. Equation (7)
becomes h*q'=(dx+u)q. Its coefficients are precisely

    E_i=w(i+1)q_(i+1)+(vi-u)q_i+(i-1-d)q_(i-1),
    0<=i<=7,                                          (8)

with out-of-range coefficients zero. Fixed-degree homogenization
keeps the eighth equation even when q6 vanishes. The top equations
are

    E7=(6-d)q6,
    E6=(6v-u)q6+(5-d)q5.

For P=(d-5)(d-6), direct polynomial identities give

    P*q5=(6-d)*E6-(6v-u)*E7,
    P*q6=-(d-5)*E7.                                  (9)

Using a Bezout identity for (5), these imply P belongs to the ODE
ideal itself. There is no cancellation by either q5 or q6. Relation
q6=eta*j with eta a unit likewise gives

    j*(d-6)=-eta^(-1)*E7.                             (10)

Both proposed accelerators may therefore be appended without
changing the localized ideal or scheme. They are retained as
equations in one system; no decomposition by values of d or j is
needed to prove or use their membership.

## 5. The first rank condition is automatic scheme-theoretically

The homogeneous quadratic action R=D_HQ satisfies

    sR=6H_tQ-2H Q_t.

Using (7), the ODE ideal gives

    sR=[(6v-2u)s+2(6-d)t]Q.

Multiply by j and apply (10). Then

    s*[jR-j*(6v-2u)Q]=0.

Multiplication by the polynomial variable s is injective over every
coefficient ring, including one with nilpotents or zero divisors.
Consequently

    jR=j*(6v-2u)Q.                                   (11)

All minors of [Q,jR] vanish in the ODE quotient. Thus the ODE
scheme retains the full shared quadratic/cubic rank incidence,
with no separate first-rank equations. Conversely the full shared
rank equations include the cubic rank condition, which gives the
unique ODE witnesses by section 3. This proves the claimed exact
scheme presentation on the stated actual localized domain.

## 6. New arithmetic evidence and limitations

The new
[universal source](../computations/generalization_quintic_h2_localized_ode_2026_10_15.m2)
and its
[passing attempt-01 record](../validation/2026-10-15-quintic-h2-localized-ode/attempt-01/execution-record.json)
were read. The source checks the membership identity (4) using
independent symbols, all eight coefficients (8), both identities
(9), and the two Hamiltonian action identities. Its exit code is
zero, stderr is empty, and stdout records all stated groups passing.
It does not substitute or reconstruct the actual conductor map.
The localization, captured-q5 identification and gluing arguments
are the written proofs above, rather than consequences of a finite
sample or CAS rank experiment.

All original actual-map unit and projection hypotheses remain in
force. In a polynomial computation they can be enforced by one
inverse of their product, including the justified Delta1 numerator.
The high-coefficient saturation adds no condition on that domain.
Appending a previously proved necessary norm product also does not
affect the equivalence of the underlying support presentations.

This audit proves the reduction and exact accelerator membership.
It proves no actual-parameter unit ideal, no characteristic-zero
emptiness from a finite-field prospect, no implication from support
to full inverse support, and no nonlinear conductor descent.
