# The Delta1 open removes qhigh saturation and gives eight linear action equations

Date: 2026-10-15. Owner: `quintic_shared_incidence/support_structural`.
Status: **PASS [INDEPENDENT AUDIT](2026-10-15-generalization-quintic-h2-automatic-open-ODE-independent-audit.md)
for automatic qhigh, the equivalent ODE incidence scheme, and both
derived accelerator equations on the declared localized domain.**
The accepted eleven-generator presentation, intrinsic A4 coefficients,
the new all-remaining-mate Delta1 open, and the exact captured scalar
binding are premises. No accepted verifier or actual coefficient
construction is replayed. There is no incidence-emptiness assertion.

## 1. The coefficient ideal (q5,q6) is already the unit ideal

Let A be the actual finite h=2 inverse-map parameter ring after the
declared localizations: delta, the cover determinant, cofactor
determinant, recorded denominator/content scalars, and Delta1 are
units. Delta1 nonzero is a globally necessary condition for all
remaining mate candidates under the accepted closures and SUP
consequences. The other listed localizations specify the declared
finite inverse-map chart; in particular its nonzero cover determinant
is not a globally necessary condition on all remaining mates.
The new [eleven-generator unit audit](2026-10-15-generalization-quintic-h2-eleven-generator-unit-independent-audit.md)
justifies the Delta1 localization and exact relation q6=unit*j.

First use the actual unscaled monic factorization Fsrc=H*Qactual,
H=t^2+vst+ws^2. Put

    S=G+3delta^2,        L=G+delta^2+2B,        A1=Delta1.

The accepted exact A4 formulas imply polynomial identities of the form

    A1=G*S*L+j*Psi,
    Qactual5=-2*S*A1+j*T.                                (1)

The second follows without computing another conductor coefficient:
the coefficient of t^7 in Fsrc is the coefficient F1 of p in the
target polynomial, while F0=-3j*A1 and
Qactual5=F1-v*F0. Modulo j the accepted F1 identity is
-2G*L*S^2=-2S*A1. Hence the displayed polynomial T exists in the
localized parameter ring. The first identity is simply the accepted
literal expression for Delta1 separated into its j-independent part.

Equations (1) give the explicit ideal membership

    A1^2+(G*L/2)*Qactual5
      =j*[Psi*A1+(G*L/2)*T].                            (2)

Since A1 is a unit, (j,Qactual5) is the unit ideal. The captured
sextic differs from Qactual by a common unit kappa in this ring,
and its top coefficient is q6=-3*kappa*A1*j. Consequently

    (q5,q6)=(Qactual5,j)=A.                              (3)

This is an exact ideal equality, valid over nonreduced parameter
bases. It neither divides by j nor uses a field-valued contradiction.
Thus the qhigh saturation is redundant after the one declared domain
localization. In particular the accepted eleven-generator support
ideal equals the full shared rank ideal there, without a second
saturation by (q5,q6). No condition G+3delta^2 nonzero is imposed
globally; that factor was used only inside the polynomial identity.

## 2. Replace expanded cubic minors by a first-order polynomial ODE

On the finite monic chart s=1, write

    h(z)=z^2+v*z+w,       q(z)=sum_(i=0)^6 q_i*z^i.

The entire cubic rank condition is equivalent, on the same localized
domain, to the existence of two scalars d,u such that

    h(z)*q'(z)=(d*z+u)*q(z).                             (4)

Indeed the cubic Hamiltonian action is

    D_(sH)Q|_(s=1)=6h'*q-3h*q'.

Saying this is a linear polynomial times q is equivalent to (4),
by an invertible affine linear change of the two witness scalars.
The first two columns sQ,tQ have rank two because (q5,q6)=A;
locally one of the fixed pivot determinants from the accepted
twelve-generator reduction is a unit. Hence the witness scalars
are unique on each pivot open and glue. Introducing d,u therefore
gives an equivalent incidence scheme, rather than an uncontrolled
projection or a sufficient-only condition.

The eight coefficient equations of (4) are

    E_i=w(i+1)q_(i+1)+(vi-u)q_i+(i-1-d)q_(i-1)=0,
    i=0,...,7,                                            (5)

where out-of-range coefficients vanish. They are linear in the
captured q_i and in each new action witness. After substituting the
actual coefficient map they avoid products of three long coefficient
polynomials, which produced the degree-52 cubic minors. There are
two extra variables, so a faster global computation is a prospect,
not a claim made by the reduction.

## 3. Two useful low-degree consequences belong to the same ideal

The top two equations are

    E7=(6-d)q6,
    E6=(5-d)q5+(6v-u)q6.

For P=(d-5)(d-6), exact polynomial identities give

    P*q5=(6-d)E6-(6v-u)E7,
    P*q6=-(d-5)E7.                                      (6)

Because (q5,q6)=A, (6) proves P belongs to the ODE ideal. It can
be appended as a derived low-degree equation without changing the
localized scheme. Similarly q6=unit*j makes E7 equivalent, up to
a unit and sign, to

    j*(d-6)=0.                                          (7)

Neither equation is used to split the computation. The one ODE
system keeps both intrinsic A4 contact alternatives: d=6 when the
sextic has no infinity root, and d=5 when it has the allowed simple
infinity root. No finite-root partition is selected or enumerated.

For comparison with the previous quadratic action, the exact identity

    D_H Q|_(s=1)
      =[(12-2d)z+6v-2u]*q-2*[h*q'-(dz+u)q]

shows directly why (7) retains the former first-rank equations.
The previously captured norm product may still be appended as one
necessary constraint, with no factor branching. It is not required
to justify the scheme equivalence of (4) and the cubic rank ideal.

## 4. New supporting arithmetic and remaining obligation

The new [universal identity source](../computations/generalization_quintic_h2_localized_ode_2026_10_15.m2)
checks (2) formally from (1), all eight coefficient formulas (5),
both top-degree identities (6), and the two Hamiltonian action
identities. It uses independent coefficient symbols and never
substitutes or reconstructs the actual conductor map. Its
[captured execution](../validation/2026-10-15-quintic-h2-localized-ode/attempt-01/execution-record.json)
records source and output. This source verifies the new displayed
polynomial identities; the localization and scheme statements have
the written proofs above.

The next computation can therefore use either the eleven selected
cubic generators or the eight low-degree ODE equations with their
two witness variables, under a single declared domain saturation.
The new degree polynomial and retained-j equation are available as
derived accelerators. Neither presentation supplies a unit-ideal
certificate, full inverse support, or nonlinear conductor descent.
