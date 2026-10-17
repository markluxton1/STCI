# One denominator-free incidence for all remaining homogeneous h2 candidates

Date: 2026-10-15. Status: **GLOBAL COVER AND EXACT INPUT ASSEMBLY;
independently audited** in the
[global monic ODE review](2026-10-16-generalization-quintic-h2-global-monic-ODE-independent-audit.md).
Accepted conormal forms, the actual
conductor octic, the full h2 conductor factor, global Delta1 open, ODE
and spectral reductions are premises. No accepted verifier is replayed.
There is no unit-ideal, projection-existence or mate-existence claim.

## 1. Original parameters retain the inverse-map boundary

Use original parameters `(delta,a,B,G,j)`, with j=Jbar, and source
`x=r/delta`. The accepted corrected normalized conormal cubics are

```
P=G x^3+(6B+delta^2-3delta)x^2+(3a-3B+2delta)x-2a,
Jc=(G+2j)x^3+(6B+3G+5delta^2-3delta)x^2
                    +(3a+3B+delta-delta^2)x-a-B.
```

For a remaining h2 mate candidate, the common factor contains no source
infinity point: the accepted infinity leading equations would force
G=j=0, whose mate lane is already closed. Thus its complete homogeneous
gcd has the unique finite monic representative

```
H=x^2+v x+w.
```

This includes w=0, double finite roots, and every affine degree drop of
the original cubics. Put

```
A=G,                 Bc=6B+delta^2-3delta-vG,
C=G+2j,              Dc=6B+3G+5delta^2-3delta-v(G+2j).
```

The complete common-factor conditions are the four polynomials

```
-2a-w Bc=0,
3a-3B+2delta-v Bc-w A=0,
-a-B-w Dc=0,
3a+3B+delta-delta^2-v Dc-w C=0.                          (1)
```

They assert P=(Ax+Bc)H and Jc=(Cx+Dc)H. Exact homogeneous gcd two
requires the independent-cofactor unit

```
E=A Dc-Bc C
 =G(3G+4delta^2)-2j(6B+delta^2-3delta) != 0.              (2)
```

No determinant of the four-equation coefficient matrix is inverted.
In particular `Delta=v^2-4w=0` and
`K=v^2+6vw+6w^2+2w=0` remain in this system. The latter may be
inconsistent by an accepted theorem; it is not removed by cancellation.

## 2. Define the sextic by monic division of the actual octic

Read the accepted actual conductor polynomial in the target coordinate

```
Fdet(p,1)=sum_(i=0)^8 f_i p^i,        p=1/x.
```

Its source-coordinate form is the fixed-degree octic
`Fsrc(1,x)=sum f_i x^(8-i)`. Define polynomial coefficients recursively,
with q7=q8=0,

```
q_i=f_(6-i)-v q_(i+1)-w q_(i+2),        i=6,5,...,0.
```

Then, identically in the original parameter polynomial ring,

```
Fsrc=H Q+r1*x+r0,
Q=sum_(i=0)^6 q_i x^i,
r1=f7-v q0-w q1,        r0=f8-w q0.                       (3)
```

Add the two equations r0=r1=0. The accepted global conductor factor
theorem ensures these equations for every actual h2 projection. We
impose them explicitly in the incidence; no scheme-theoretic divisibility
on an arbitrary nonreduced conormal-cover base is inferred from that
geometric theorem.

The newly justified globally necessary unit is

```
Delta1=G(G+3delta^2)(G+delta^2+2B)
       +j[(delta^2-5B)G-3B(delta^2+3B)]-B j^2.
```

The one domain for this global monic incidence is

```
delta*E*Delta1 != 0.                                    (4)
```

Here delta and E express the original chart and exact-h2 hypotheses;
Delta1 is necessary under the accepted closed-lane and SUP arguments.
There is no `Delta*K` inverse and no rational-map denominator.

## 3. The same shared ODE and spectral identities hold globally

The accepted exact A4 identities give, for this unscaled actual Q,

```
q6=-3j Delta1,
q5=-2(G+3delta^2)Delta1  modulo j.                        (5)
```

The second identity follows from q5=f1-vq6 and the accepted first A4
coefficient. In the quotient by (q5,q6), the unit Delta1 forces j=0,
then G+3delta^2=0 by (5), and finally Delta1=0 from its j=0
factorization. Thus `(q5,q6)` is the unit ideal on (4), including
nonreduced coefficient bases. No inverse-map scalar is needed here.

Adjoin the two witnesses d,eta, with eta=dv-2u. The eight equations are

```
2w(i+1)q_(i+1)+[(2i-d)v+eta]q_i
                         +2(i-1-d)q_(i-1)=0,  i=0,...,7, (6)
```

where out-of-range coefficients vanish. They are twice the coefficients
of `H q'=(dx+u)q`. The independently reviewed ODE and spectral proofs
use only monic H, (5), the Delta1 unit and coefficient unimodularity;
their algebra does not use rational inversion or `Delta*K!=0`.
Consequently the same derived accelerator equations are available:

```
(d-5)(d-6)=0,          j(d-6)=0,
(d-5)P6(eta)+(6-d)P5(eta)=0,                             (7)
P6(X)=X(X^2-4Delta)(X^2-16Delta)(X^2-36Delta),
P5(X)=(X^2-Delta)(X^2-9Delta)(X^2-25Delta).
```

Equations (1), r0=r1=0, and (6) give fourteen equations in the nine
variables `(delta,a,B,G,j,v,w,d,eta)`. Appending (7) gives the saved
seventeen-equation presentation. It uses one domain saturation by (4)
and no qhigh saturation, root partition, norm-factor branch or separate
degree computation.

On actual admissible projections satisfying the stated h2 hypotheses,
this system expresses exactly the accepted restricted-conductor support
obligation, with the intrinsic A4 allowance retained. It does not express
center avoidance, full inverse support at every original fiber, or full
nonlinear conductor power descent. A surviving algebraic parameter is
not thereby a mate.

## 4. Exact new assembly and continuation boundary

The new [assembly source](../computations/generalization_quintic_h2_global_monic_ode_export_2026_10_15_attempt02.m2)
reads the accepted primitive octic once and forms the original-parameter
model. It asserts (2) and the new literal quotient/remainder identity
(3), writes all equation groups, all seven actual q_i, the single domain
unit and the equation degrees. The degrees are

```
3,3,3,3,13,13,14,13,12,11,10,9,8,7,2,2,8.
```

Its mathematical assembly and both assertions passed, but its final
informational equation-count print failed. Those complete coefficient
outputs are preserved in attempt02. The initial protected-variable
failure and the first postprocessing path mismatch also remain separate.
The [completion script](../computations/generalization_quintic_h2_global_monic_ode_completion_2026_10_15.py)
reuses the written outputs, verifies exact concatenation of the four
groups into seventeen entries, verifies the seven-entry Q vector, and
binds every input by SHA256. It does not reread the primitive polynomial
or reconstruct the model. Its final
[completion record](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-04-completion/execution-record.json)
has exit zero and empty stderr. No Groebner basis, saturation, resultant
or emptiness search was launched for this global input.

The currently runnable/loadable
[input file](../computations/generalization_quintic_h2_global_monic_ode_input_2026_10_16.m2)
reads that completed saved model over QQ and exposes
`h2GlobalRing`, `h2GlobalEquations`, `h2GlobalIdeal`, and
`h2GlobalDomainUnit`. Its separate
[load-only record](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-05-load-only/execution-record.json)
has exit zero, empty stderr and both model-input hashes. It verifies
the seventeen-entry matrix in the nine-variable ring and constructs
the unsaturated ideal only. It does not execute the domain localization
or any Groebner computation. The load process exited normally and was
reaped; no global-model CAS process remains live.

The outstanding shared h2 task can therefore be stated globally: prove
this one incidence empty after (4), or describe its actual admissible
survivors and test the full fibers and conductor. A finite inverse-map
calculation may be useful, but its `Delta*K!=0` conclusion must not be
reported as closure of this global seventeen-equation problem.
