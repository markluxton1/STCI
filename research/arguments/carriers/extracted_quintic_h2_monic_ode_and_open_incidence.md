# Quintic h=2: monic ODE and admissible open incidence

## Integration guide: the actual open and the differential equations

This dossier studies the quintic h=2 incidence scheme on the stated nonvanishing open, including the reduction to a shared logarithmic ODE and its coefficient equations. The [spectral and generator dossier](../spectral/spectral_pushforward_boundary.md#quintic-h2-spectral-operators-determinant-generators-and-actual-coefficient-units) reorganizes these same equations to expose linear-algebra structure; that is a computational acceleration, not an independent proof of global support exclusion. The [degree-five incidence frontier](#denominator-free-incidence-for-all-remaining-homogeneous-h2-candidates) records a degree-five branch that remains unresolved: the proposed exclusion confuses the reciprocal determinant coordinate with the actual source coordinate and does not justify its pure-power reduction. Replaying those resultants alone cannot settle the branch. Preserve the open-set assumptions and the separate audit of the ODE equivalence.

---


---

<a id="2026-10-15-generalization-quintic-h2-automatic-open-ODE-independent-audit"></a>

## Automatic high-coefficient open and shared logarithmic ODE

Date: 2026-10-15.

Status: **PASS. The coefficient ideal (q5,q6) is the unit ideal on the
declared actual localized domain. The eight ODE equations give an
equivalent incidence scheme, with unique witness coefficients, and
both proposed accelerator equations belong to the same localized
ideal.** The statements hold over nonreduced parameter bases as well
as at geometric points.

The full automatic-open and ODE proof is consolidated below.
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
necessary Delta1 open. No division by j=Jbar is made. The cover determinant is a condition for this inverse-map chart, not a globally necessary condition on every remaining mate; its vanishing boundary remains in the separate global monic system below.

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

At geometric points, d=6 denotes a degree-six sextic without an infinity root, while d=5 denotes degree five with the allowed simple infinity root at the prescribed A4 point. This interpretation does not split the global computation into separately assumed branches.

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

The [universal source](https://github.com/markluxton1/STCI/blob/add6e1664e6d9db84e67fb0276a318a804b3d2f8/research/computations/generalization_quintic_h2_localized_ode_2026_10_15.m2) checks membership identity (4) using independent symbols, all eight coefficients (8), both identities (9) and the two Hamiltonian action identities. It does not substitute or reconstruct the actual conductor map. Localization, captured-q5 identification and gluing require the written proofs above, not a finite sample or rank experiment.

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


---

<a id="2026-10-15-generalization-quintic-h2-global-monic-ODE-incidence"></a>

## Denominator-free incidence for all remaining homogeneous h=2 candidates

Date: 2026-10-15. Status: **GLOBAL COVER AND EXACT INPUT ASSEMBLY;
independently audited** in the
[global monic ODE review](normalization_conductor_phase2_addendum.md#separate-finite-root-arithmetic-and-quintic-boundaries).
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

The new [assembly source](https://github.com/markluxton1/STCI/blob/add6e1664e6d9db84e67fb0276a318a804b3d2f8/research/computations/generalization_quintic_h2_global_monic_ode_export_2026_10_15_attempt02.m2)
reads the accepted primitive octic once and forms the original-parameter
model. It asserts (2) and the new literal quotient/remainder identity
(3), writes all equation groups, all seven actual q_i, the single domain
unit and the equation degrees. The degrees are

```
3,3,3,3,13,13,14,13,12,11,10,9,8,7,2,2,8.
```

The retained exact seventeen-entry equation row and domain polynomial are the complete saved model. The assembly source specifies their construction from the actual octic; no Gröbner basis, saturation, resultant or emptiness conclusion follows from assembling this input.

The [input file](https://github.com/markluxton1/STCI/blob/bb5b1d5348097028738db196c262fe44b81b69ca/research/computations/generalization_quintic_h2_global_monic_ode_input_2026_10_16.m2) reads the completed model over QQ and exposes `h2GlobalRing`, `h2GlobalEquations`, `h2GlobalIdeal` and `h2GlobalDomainUnit`. It checks the seventeen-entry matrix in the nine-variable ring and constructs the unsaturated ideal only; it does not execute domain localization or a Gröbner computation.

The outstanding shared h2 task can therefore be stated globally: prove
this one incidence empty after (4), or describe its actual admissible
survivors and test the full fibers and conductor. A finite inverse-map
calculation may be useful, but its `Delta*K!=0` conclusion must not be
reported as closure of this global seventeen-equation problem.

## Required evidence for an exclusion

The global seventeen-equation incidence remains unresolved. The scheme-level ODE equivalence uses unimodularity only after localization at the actual domain `delta*E*Delta1`; the degree-five H2 branch and omitted projection boundaries remain outside any claimed exclusion. An exclusion by saturation must use the original domain δEΔ1, without silently adding a cover discriminant, K, coefficient or j inverse. A unit-ideal output needs an exact identity in the declared original generators and complete coverage of the stated boundary. A bounded attempt or its process-control checks supplies neither.


### Archived exact certificate: `research/computations/generalization_quintic_h2_global_monic_ode_export_2026_10_15_attempt02.m2`

Original source retained verbatim, with its limitations and original relative-path assumptions.

<details><summary>Original Macaulay2 source</summary>

```macaulay2
-- NEW denominator-free global monic h2 incidence export; no GB/saturation.
-- Accepted actual primitive conductor is an input, not reconstructed.
outDir="research/validation/2026-10-15-quintic-h2-global-monic-ode/attempt-02-name-repair";
save=(label,f)->((outDir|"/"|label|".txt") << toString f << close);
base=QQ[delta,a,B,G,J,vH2,wH2,h2DGlobal,h2EtaGlobal];
actual=base[p];
F=value get "research/validation/2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/primitive-polynomial.txt";
f=apply(toList(0..8),i->lift(coefficient(p^i,F),base));
q=new MutableList from toList(7:0_base);
qi=i->if i<0 or i>6 then 0_base else q#i;
scan(reverse toList(0..6),i->q#i=f#(6-i)-vH2*qi(i+1)-wH2*qi(i+2));
q=toList q;
frem={f#8-wH2*qi(0),f#7-vH2*qi(0)-wH2*qi(1)};
Plead=G; Pconstant=6*B+delta^2-3*delta-vH2*G;
Jlead=G+2*J; Jconstant=6*B+3*G+5*delta^2-3*delta-vH2*(G+2*J);
h2CoverEquations={-2*a-wH2*Pconstant,
       3*a-3*B+2*delta-vH2*Pconstant-wH2*Plead,
       -a-B-wH2*Jconstant,
       3*a+3*B+delta-delta^2-vH2*Jconstant-wH2*Jlead};
cofactorDet=Plead*Jconstant-Pconstant*Jlead;
assert(cofactorDet==G*(3*G+4*delta^2)-2*J*(6*B+delta^2-3*delta));
delta1=G*(G+3*delta^2)*(G+delta^2+2*B)+J*((delta^2-5*B)*G-3*B*(delta^2+3*B))-B*J^2;
domainUnit=delta*cofactorDet*delta1;
disc=vH2^2-4*wH2;
ode=apply(toList(0..7),i->2*wH2*(i+1)*qi(i+1)+((2*i-h2DGlobal)*vH2+h2EtaGlobal)*qi(i)+2*(i-1-h2DGlobal)*qi(i-1));
poly6=h2EtaGlobal*(h2EtaGlobal^2-4*disc)*(h2EtaGlobal^2-16*disc)*(h2EtaGlobal^2-36*disc);
poly5=(h2EtaGlobal^2-disc)*(h2EtaGlobal^2-9*disc)*(h2EtaGlobal^2-25*disc);
accelerators={(h2DGlobal-5)*(h2DGlobal-6),J*(h2DGlobal-6),(h2DGlobal-5)*poly6+(6-h2DGlobal)*poly5};
allEquations=join(h2CoverEquations,frem,ode,accelerators);
save("h2CoverEquations-four-equations",matrix{h2CoverEquations});
save("conductor-two-remainders",matrix{frem});
save("ODE-eight-equations",matrix{ode});
save("derived-three-accelerators",matrix{accelerators});
save("global-seventeen-equations",matrix{allEquations});
save("global-domain-unit",domainUnit);
save("actual-Q-coefficients",matrix{q});
scan(toList(0..6),i->save("actual-Q-coefficient-"|toString i,qi(i)));
-- The following is only the new export's division identity, not a claim
-- that the two remainders vanish on arbitrary parameter tuples.
h2SourceRing=base[xH2];
H=xH2^2+vH2*xH2+wH2;
Q=sum(toList(0..6),i->sub(qi(i),h2SourceRing)*xH2^i);
Fsource=sum(toList(0..8),i->sub(f#i,h2SourceRing)*xH2^(8-i));
assert(Fsource==H*Q+sub(frem#1,h2SourceRing)*xH2+sub(frem#0,h2SourceRing));
save("equation-degrees",apply(allEquations,g->first degree g));
print "PASS new monic quotient/remainder export and exact cofactor-determinant formula";
print("COMPLETE GLOBAL denominator-free monic h2 ODE incidence: "|toString(#allEquations)|" equations, delta*cofactor*Delta1 unit; no h2CoverEquations determinant inverted");
exit 0;
```
</details>


### Archived exact certificate: `research/computations/generalization_quintic_h2_localized_ode_2026_10_15.m2`

Original source retained verbatim, with its limitations and original relative-path assumptions.

<details><summary>Original Macaulay2 source</summary>

```macaulay2
-- NEW universal identities for automatic qhigh and a lower-degree ODE incidence.
-- Accepted A4 coefficient and actual scalar identities are premises, not rerun.
outDir="research/validation/2026-10-15-quintic-h2-localized-ode/attempt-01";
save=(label,f)->((outDir|"/"|label|".txt") << toString f << close);
A=QQ[gVal,sVal,lVal,jVal,psiVal,tVal];
deltaOne=gVal*sVal*lVal+jVal*psiVal;
qFive=-2*sVal*deltaOne+jVal*tVal;
membershipWitness=psiVal*deltaOne+(gVal*lVal/2)*tVal;
assert(deltaOne^2+(gVal*lVal/2)*qFive==jVal*membershipWitness);
save("automatic-qhigh-membership-witness",membershipWitness);
print "PASS Delta1^2 belongs to ideal(j,Qactual5), with explicit universal identity";
B=QQ[q0,q1,q2,q3,q4,q5,q6,v,w,d,u];
qf={q0,q1,q2,q3,q4,q5,q6};
qi=i->if i<0 or i>6 then 0_B else qf#i;
polyRing=B[z];
q=sum(toList(0..6),i->qi(i)*z^i);
h=z^2+v*z+w;
ode=h*diff(z,q)-(d*z+u)*q;
ec=apply(toList(0..7),i->w*(i+1)*qi(i+1)+(v*i-u)*qi(i)+(i-1-d)*qi(i-1));
assert(ode==sum(toList(0..7),i->ec#i*z^i));
assert(ec#7==(6-d)*q6);
assert(ec#6==(5-d)*q5+(6*v-u)*q6);
dp=(d-5)*(d-6);
assert(dp*q5==(6-d)*ec#6-(6*v-u)*ec#7);
assert(dp*q6==-(d-5)*ec#7);
quadAction=6*diff(z,h)*q-2*h*diff(z,q);
cubicAction=6*diff(z,h)*q-3*h*diff(z,q);
assert(quadAction==((12-2*d)*z+6*v-2*u)*q-2*ode);
assert(cubicAction==((12-3*d)*z+6*v-3*u)*q-3*ode);
save("eight-universal-ODE-generators",matrix{ec});
save("derived-degree-polynomial",dp);
print "PASS all eight ODE coefficients, top-degree identities, and both Hamiltonian action identities";
print "COMPLETE new universal localized ODE identities; no actual-coefficient elimination";
exit 0;
```
</details>
