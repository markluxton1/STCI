# A single spectral accelerator for the shared logarithmic ODE

Date: 2026-10-15. Owner: `quintic_shared_incidence/support_structural`.
Status: **STRUCTURAL CONSEQUENCE AND EXACT UNIVERSAL CHECK; independently
audited** in the
[eta spectral review](2026-10-15-generalization-quintic-h2-eta-spectral-independent-audit.md).
The accepted automatic-open and ODE
scheme theorem, its degree polynomial, and the accepted Sym6
characteristic polynomial are premises. None is replayed. This note
computes only the new Sym5 characteristic and new universal residual
identities, with no actual-parameter Groebner computation.

## 1. Scope and the proposed single polynomial

Use the declared actual finite h=2 inverse-map domain, retaining its
delta, cover-determinant, cofactor-determinant and recorded scalar
units, together with the justified Delta1 open. Only Delta1 is a
globally necessary new remaining-mate open; the other localizations
specify the chart under investigation. The accepted
[automatic-open/ODE audit](2026-10-15-generalization-quintic-h2-automatic-open-ODE-independent-audit.md)
gives (q5,q6)=A in this localized parameter ring A.

Adjoin d,u and let I be the eight-coefficient ideal of

    h(z)q'(z)=(dz+u)q(z),
    h=z^2+vz+w,       q=sum_(i=0)^6 q_i z^i.

The accepted theorem proves

    (d-5)(d-6) belongs to I,
    j(d-6) belongs to I,

as exact localized ideal memberships, including over nonreduced
parameter bases. Put

    Delta=v^2-4w,            eta=dv-2u,
    P6(X)=X(X^2-4Delta)(X^2-16Delta)(X^2-36Delta),
    P5(X)=(X^2-Delta)(X^2-9Delta)(X^2-25Delta).

Then the new single accelerator is

    P=(d-5)P6(eta)+(6-d)P5(eta),                         (1)

and the claim proved below is

    P belongs to I.                                     (2)

Thus (1) may be appended to the same ODE ideal without changing
its localized scheme. It neither splits the d values into separate
computations nor divides by j. No eigenvalue or root partition is
selected.

## 2. The new degree-five representation identity

For H=t^2+vst+ws^2, the Hamiltonian action D_H on a degree-n
form with coefficient vector a=(a0,...,an) is the matrix A_n with

    (A_n a)_i=(n-2i)v*a_i+(2n-2i+2)a_(i-1)
                         -2(i+1)w*a_(i+1).              (3)

In particular the new degree-five matrix is

    A5 = [ 5v  -2w    0    0    0     0 ]
         [ 10   3v  -4w    0    0     0 ]
         [  0    8    v  -6w    0     0 ]
         [  0    0    6   -v  -8w     0 ]
         [  0    0    0    4  -3v  -10w ]
         [  0    0    0    0    2    -5v ].

Its characteristic polynomial is P5(X). For a structural derivation,
the two-dimensional action has matrix

    [ v  -2w ]
    [ 2   -v ],

whose square is Delta times the identity. Over the square-root
extension on the dense Delta-nonzero locus its eigenvalues are
plus and minus sqrt(Delta). The fifth symmetric power has weights
5,3,1,-1,-3,-5, giving P5(X). This is an identity over QQ[v,w],
so polynomial continuation proves it also at Delta=0. There it
is X^6; no repeated-root boundary was divided away in this
representation theorem.

The new exact source independently checks det(X*Id-A5)=P5(X)
and the corresponding six-by-six Cayley-Hamilton product. The
degree-six characteristic P6 is the previously accepted premise,
not recalculated in that source.

## 3. One idempotent argument proves the ideal consequence

Work in the quotient B=A[d,u]/I. Set

    e6=d-5,       e5=6-d.

Because the accepted degree polynomial is zero in B,

    e6+e5=1,       e6*e5=0,       e6^2=e6,       e5^2=e5.

These are algebraic idempotents over B even if B is nonreduced.
They are used simultaneously in the proof; no separately computed
parameter ideals are introduced.

Let q6vec=(q0,...,q6)^transpose. Directly from the eight ODE
coefficients E_i, one has the exact identity before quotienting

    e6*(A6-eta*Id)*q6vec
      =-2e6*(E0,...,E6)^transpose
        -(d-5)(d-6)*(2q_(i-1)+v*q_i)_(i=0..6).          (4)

Thus e6*q6vec is an eta eigenvector of A6 over B. The accepted
Cayley-Hamilton identity P6(A6)=0 yields

    e6*P6(eta)*q_i=0,       0<=i<=6.                     (5)

For the degree-five part, the top ODE coefficient is

    E7=(6-d)q6=e5*q6,

so the e5 component has no coefficient of z^6. Put
q5vec=(q0,...,q5)^transpose. A second exact identity is

    e5*(A5-eta*Id)*q5vec
      =-2e5*(E0,...,E5)^transpose
        +(d-5)(d-6)*(2q_(i-1)+v*q_i)_(i=0..5)
        +12w*E7*(0,0,0,0,0,1)^transpose.                (6)

Consequently e5*q5vec is an eta eigenvector of A5 over B. The
new Cayley-Hamilton identity gives

    e5*P5(eta)*q_i=0,       0<=i<=5.

The same equation for i=6 follows from e5*q6=0. Adding to (5)
proves P*q_i=0 for all seven coefficients. The accepted exact
unit ideal (q5,q6)=A remains the unit ideal after passing to B,
so P=0 in B. This is (2), with no reduction to field-valued points,
no radical operation, and no cancellation by a coefficient or by j.

The proof uses Cayley-Hamilton over a commutative coefficient ring.
The eigen-residual identities and idempotents therefore preserve
nilpotents and zero divisors in the parameter quotient.

## 4. Exact supporting arithmetic and limitation

The new [source](../computations/generalization_quintic_h2_unified_spectral_accelerator_2026_10_15.m2)
checks only the new Sym5 determinant and Cayley-Hamilton identity,
the idempotent identities modulo the known degree polynomial,
and both projected residual formulas (4),(6). The source constructs
A6 only to check the new ODE residual relation; it does not compute
its determinant, characteristic polynomial, or Cayley-Hamilton
identity. The accepted Sym6 polynomial remains a premise.

The [new execution record](../validation/2026-10-15-quintic-h2-unified-spectral-accelerator/attempt-01/execution-record.json)
stores the source and output. The actual captured conductor map is
not substituted. A successful universal check supports the displayed
identities; the written quotient-ring argument supplies the exact
localized ideal implication.

Equation (1) is a derived accelerator for one shared support ideal.
It is not an actual-parameter unit-ideal witness, an emptiness result,
or a conductor power-descent theorem. All original finite inverse-map
domain and actual-projection hypotheses remain in force.
