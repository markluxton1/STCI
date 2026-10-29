# Quintic h2: exclusion of the degree-five support-incidence branch

**Result (characteristic zero, necessary incidence only).** On the global monic h2 parameter domain delta*E*Delta1 != 0, the j=0 (degree-five conductor quotient) branch satisfying the conormal common-quadratic, conductor-divisibility, and support ODE equations has no points.

**Proof.** For j=0, the actual primitive source conductor has zero constant coefficient and linear coefficient
`-2*G*(G+3*delta^2)^2*(G+delta^2+2*B)`, a unit on the prescribed open. Write Fsrc=H*Q and H*Q'=(5*x+u)*Q. All roots of Q are roots of H. The simple conductor zero at x=0 therefore forces H(0)=0 and Q(0) nonzero. The two conormal constant equations imply w=a=B=0. Thus H=x*(x+v), v nonzero, and Q=q5*(x+v)^5.

The remaining common-factor equation is
```
R=9*G^2+2*G*delta^3+22*G*delta^2-4*G*delta
  +2*delta^5+12*delta^4-6*delta^3=0,
v=-delta*(delta+1)/(3*G+4*delta^2).
```
The ODE implies q4=5*v*q5 and q3=10*v^2*q5. Set T=3*G+4*delta^2, P=T*(q4-5*v*q5), S=T^2*(q3-10*v^2*q5), using the quotient coefficients from the actual primitive conductor after a=B=j=0. Exact QQ elimination gives
```
Res_G(R,P)=6*delta^13*(delta+1)^2*f(delta)
Res_G(R,S)=-9*delta^15*(delta+1)^4*g(delta)
f=40*delta^5-323*delta^4-2018*delta^3-288*delta^2-600*delta+156
g=128*delta^7+4720*delta^6+600*delta^5-58408*delta^4
  +124123*delta^3+2484*delta^2+44376*delta-11016
gcd(f,g)=1.
```
Since delta != 0 and v != 0 implies delta != -1, the resultants cannot vanish simultaneously. QED.

**Exact source-based verifier:** [verify_quintic_h2_degree_five.py](../computations/verify_quintic_h2_degree_five.py). **Global hypotheses:** [monic incidence](2026-10-15-generalization-quintic-h2-global-monic-ODE-incidence.md). **Working reduction:** [degree-five dossier](quintic-h2-degree-five-support-incidence-working-dossier.md).

**Limit:** This excludes the j=0 branch only. The j != 0, degree-six branch is unresolved. The necessary incidence is not equivalent to STCI existence. The argument does not invert the discriminant of H or inverse-map denominators.
