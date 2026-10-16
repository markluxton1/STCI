# Independent audit: one eta spectral accelerator for the shared ODE

Date: 2026-10-15.

Status: **PASS. The proposed single spectral polynomial belongs to
the localized shared ODE ideal, with exact scheme-theoretic scope,
including nonreduced parameter rings.** The accepted ODE presentation,
coefficient unimodularity, derived degree equation and degree-six
Hamiltonian characteristic polynomial are premises and were not
replayed.

This note audits only the new degree-five spectral input and its
combination with the accepted shared ODE. It gives no actual-parameter
emptiness or conductor-descent conclusion.

The reviewed proposal is
[the unified spectral-accelerator note](2026-10-15-generalization-quintic-h2-unified-spectral-accelerator.md).

## 1. Ring, sign conventions and the proposed polynomial

Let A be the actual coefficient ring on the accepted localized finite
inverse-map domain, and let

    B=A[d,u]/I_ODE

be the shared ODE quotient, with any previously appended equations
already proved to belong to the same ideal. In particular, over this
characteristic-zero field algebra,

    h=x^2+vx+w,       h*q'=(dx+u)q,
    (q5,q6)=B,
    (d-5)(d-6)=0.                                     (1)

The q_i are the captured sextic coefficients. All original actual-map
and projection conditions remain. No domain or support statement
outside that localization is inferred here.

Put

    eta=dv-2u,       Delta=v^2-4w,
    P6(T)=T*(T^2-4Delta)*(T^2-16Delta)*(T^2-36Delta),
    P5(T)=(T^2-Delta)*(T^2-9Delta)*(T^2-25Delta).

The new accelerator is the one polynomial

    P=(d-5)*P6(eta)+(6-d)*P5(eta).                    (2)

The sign of eta corresponds to D_H=H_t partial_s-H_s partial_t,
with H=t^2+vst+ws^2. Reversing that derivation would reverse the
eigenvalue sign; no such convention change is made here.

## 2. The new degree-five characteristic polynomial

On the degree-one coordinate basis (s,t), the coefficient matrix of
D_H is

    M=[ v   -2w ]
      [ 2    -v ],       M^2=Delta*Id.

Over the universal ring QQ[v,w], on the dense locus Delta nonzero
and after adjoining a square root rho of Delta, the eigenvalues on
the two-dimensional representation are rho and -rho. On degree-five
binary forms the derivation therefore has eigenvalues

    5rho, 3rho, rho, -rho, -3rho, -5rho.

Their characteristic polynomial is exactly P5(T). Both the matrix
characteristic polynomial and this displayed expression are
polynomial in v,w, so equality on the dense locus is a universal
polynomial identity. It specializes under every coefficient-ring
map, including Delta=0 and nonreduced bases. In particular, using
P5 does not require a discriminant inversion beyond those already
present in the actual coefficient chart.

The analogous degree-six characteristic polynomial P6 is an accepted
premise. The new proof does not rerun its computation or its audit.
Cayley--Hamilton applies to each of these operator matrices over
every commutative coefficient ring.

## 3. The two weights are combined by exact central idempotents

In B define

    e6=d-5,       e5=6-d.

Equation (1) gives

    e6+e5=1,       e6*e5=0,
    e6^2=e6,       e5^2=e5,
    d*e6=6e6,      d*e5=5e5.                          (3)

These are identities in the full quotient, not decompositions only
of its reduced point set. They therefore apply if B has nilpotents.
They supply a proof of the one polynomial (2); they do not require
running separate parameter or factor computations.

In the component ring e6*B, the ODE degree is six. Homogenizing and
using Euler's identity in degree six gives

    s D_H Q=6H_tQ-2H Q_t
           =[(6v-2u)s+2(6-d)t]Q.

Here d=6, so cancellation of the polynomial variable s gives

    D_H Q=eta Q            in the e6 component.        (4)

The variable s is not a zero divisor in a polynomial ring over any
base; this cancellation makes no reducedness assumption.

In e5*B, the top ODE equation E7=(6-d)q6 gives q6=0. Thus the
homogeneous sextic is s*Q5, with

    Q5=sum_(i=0)^5 q_i*s^(5-i)*t^i.

After cancellation of s, its ODE is H*(Q5)_t=(us+5t)Q5. Euler's
identity in degree five now gives

    D_H Q5=(5v-2u)Q5=eta Q5.                           (5)

There is no missing eigenvalue shift: Q5 has degree five, while the
original degree-six form retains its additional factor s. In this
component q6 is zero, and q5, rather than q6, is a unit by (1).

## 4. Cayley--Hamilton gives scalar membership, not just annihilation

Apply the accepted degree-six Cayley--Hamilton identity to (4).
It gives P6(eta) times every coefficient of Q equal to zero in e6*B.
The coefficients q5,q6 generate the unit ideal in that component,
because their unit-ideal relation in (1) survives multiplication by
e6. Hence

    e6*P6(eta)=0.                                     (6)

Apply the new degree-five identity to (5). It gives P5(eta) times
every coefficient of Q5 equal to zero in e5*B. Here q6=0 and
(q5,q6) is the unit ideal, so q5 is a unit. Therefore

    e5*P5(eta)=0.                                     (7)

Adding (6)-(7) proves P=0 in B. Equivalently,

    P belongs to I_ODE in the declared localized ring. (8)

No radical or reduced quotient is used in this conclusion. The
unimodularity is essential: a polynomial annihilating a coefficient
vector would not generally have to vanish as a scalar if that
vector's coefficient ideal were proper. Here (1) supplies precisely
the additional input needed for exact ideal membership.

The argument never divides by j, chooses a root of H, or discards
the intrinsic A4 allowance. The single accelerator (2) retains both
parts of the shared ODE, including its entire retained j=0 locus.
Adding it to a polynomial computation with the declared domain
inverse leaves the localized ideal and scheme unchanged. Adding it
without enforcing that domain would be a different claim.

## 5. New exact capture and prepared actual run

The new
[universal source](../computations/generalization_quintic_h2_unified_spectral_accelerator_2026_10_15.m2)
and its
[passing attempt-01 record](../validation/2026-10-15-quintic-h2-unified-spectral-accelerator/attempt-01/execution-record.json)
were read. The source and frozen-source digests match the recorded
digest. Exit is zero, stderr is empty, and stdout records both the
new degree-five determinant/Cayley--Hamilton identity and the
idempotent/projected-residual checks passing. It computes no
degree-six characteristic polynomial or degree-six Cayley--Hamilton
product; that accepted theorem remains a premise.

The projected residual formulas have the correct extra boundary
term. For b_i=2q_(i-1)+v*q_i and Dpoly=(d-5)(d-6), the degree-six
residual is

    e6*(A6-eta*Id)q6vec=-2e6*E6vec-Dpoly*b6vec.

The degree-five residual is

    e5*(A5-eta*Id)q5vec=-2e5*E5vec+Dpoly*b5vec
                          +12w*E7*last_basis_vector.

The last term accounts precisely for q6 occurring in E5 but not
in the degree-five matrix. It vanishes in the ODE quotient because
E7=e5*q6. Thus the new universal exact checks agree with the
independent homogeneous proof in sections 3-4.

The prepared shared actual prospect uses eta in place of u. Its
coefficients are exactly twice (8) of the accepted ODE audit after
the invertible substitution u=(dv-eta)/2:

    2w(i+1)q_(i+1)+[(2i-d)v+eta]q_i
                          +2(i-1-d)q_(i-1).

It adds the one polynomial (2), the accepted derived degree and
retained-j equations, and the previously necessary norm product.
It retains the original domain product and introduces no root,
norm-factor or j partition. This audit approves the mathematical
equivalence of that prepared presentation; it records no result
from its actual-parameter computation.

The remaining mathematical obligation is still actual-parameter
incidence and full conductor descent. This spectral identity alone
does not prove an empty locus, and agreement in finite characteristic
would not by itself prove characteristic-zero emptiness.
