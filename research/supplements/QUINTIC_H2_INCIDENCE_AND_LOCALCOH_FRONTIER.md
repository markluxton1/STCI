# Quintic H2: the degree-five necessary incidence and its open boundary

**Status:** the `j=0` degree-five branch remains unresolved by the proposed
exclusions. Independent source-coordinate review found an upstream reduction
gap in both attempted eliminations and a reciprocal-coordinate error in the
later verifier. The reviewed common-factor, actual conductor-divisibility,
open-domain and logarithmic ODE reductions remain valid. They do not certify
emptiness or construct a projection or an STCI.

The complete abstract theorem formerly embedded here has a focused home in
[polynomial duals and observable affine pencils](POLYNOMIAL_DUALS_AND_AFFINE_PENCILS.md).
It treats arbitrary fields, observation rank/depth, parameter strata and exact
determinantal fallback; it does not supply rank or emptiness for this family.

<a id="source-2026-10-29-quintic-h2-degree-five-incidence-reductionmd"></a>
<a id="source-quintic-h2-degree-five-support-incidence-working-dossiermd"></a>
## Actual coordinates, domain and common-factor equations

Work over an algebraically closed characteristic-zero field. The global
monic exact-gcd-two incidence has parameters `delta,a,B,G,j,v,w` and
`H=x²+vx+w`, on the original open `delta E Delta1 != 0`. Keep repeated
roots of `H` and the inverse-map boundary. The full
[monic ODE proof](QUINTIC_H2_MONIC_ODE_AND_OPEN_INCIDENCE.md#2026-10-15-generalization-quintic-h2-global-monic-ode-incidence)
retains all seventeen equations in nine variables, without inverting the
discriminant or the inverse-map denominator. The
[spectral/generator identities](QUINTIC_H2_SPECTRAL_AND_GENERATOR_SYSTEM.md)
compress those equations; they are not an independent emptiness certificate.

Use the actual source coordinate `x=r/delta=T/S`. The primitive determinant
polynomial is in the reciprocal coordinate `p=delta/r=S/T=1/x`:

```
Fdet(p,1)=sum f_i p^i,
Fsrc(1,x)=x^8 Fdet(1/x,1),
Fsrc=H Q.
```

This is the [reviewed coordinate correction](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-14-generalization-quintic-h2-coordinate-correction-and-sextic-incidence).
The original exact input remains
[primitive-polynomial.txt](../validation/2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/primitive-polynomial.txt).
In the reciprocal chart, the same homogeneous quadratic factor is
`1+vp+wp²`, rather than `p²+vp+w`.

On `j=0` the conormal cubics in `x` are

```
P  = G*x³+(6*B+delta²-3*delta)*x²
       +(3*a-3*B+2*delta)*x-2*a,
Jc = G*x³+(6*B+3*G+5*delta²-3*delta)*x²
       +(3*a+3*B+delta-delta²)*x-a-B.
```

Set

```
T=3*G+4*delta²,
U=6*B-delta-delta²,  V=a-B,
L=6*B+delta²-3*delta,  M=3*a-3*B+2*delta,
N=L*T-G*U.
```

The cofactor determinant is `E=G*T`, so `G,T` are units. Since
`Jc-P=T*x²+U*x+V`, the common monic quadratic is forced to be

```
v=U/T,  w=V/T.
```

Divisibility of both cubics is equivalent to the two remainder equations

```
F0=-2*a*T²-V*N=0,
F1=M*T²-G*V*T-U*N=0.
```

Writing `A=2*T²+N`, `C=3*T²-G*T` gives, on the additional chart `A != 0`,

```
a=B*N/A,
Phi=B*C*N+A*(-3*B*T²+2*delta*T²+G*B*T-U*N)=0.
```

This rational chart does not authorize dropping `A=0`. The original source
also reports an auxiliary elimination on `A=0`: `F0` forces `B=0`, and
eliminating `G` from the remaining equations gives
`576*delta^10*(delta+1)²`; at `delta=-1` it reports `T=0`. That reported
auxiliary calculation has not been independently replayed here and is not
used to replace the full two remainder equations or globally invert `A`.
The original admissible open specializes to

```
delta*G*T*(G+3*delta²)*(G+delta²+2*B) != 0.
```

## The valid degree-five ODE and fixed A4 zero

The exact source quotient recursion is

```
q6=f0,
q_i=f_(6-i)-v*q_(i+1)-w*q_(i+2),
Q=sum q_i*x^i.
```

In particular `q6=f0=-3j Delta1`. On `j=0`, `q6=0` and

```
q5=f1=-2*(G+3*delta²)*Delta1
     =-2*G*(G+3*delta²)²*(G+delta²+2*B).
```

Thus `q5` is a unit on the prescribed open and the affine quotient has
exact degree five. The necessary source-support equation is

```
H Q'=(5x+u)Q.
```

It implies that each finite root of `Q` lies among the roots of `H`.
The homogeneous sextic quotient also has its fixed simple A4 zero, at
`S=0`, equivalently `p=0` and `x=infinity`. A degree-five affine quotient
is compatible with a monic quadratic `H` avoiding that point. This fixed
zero supplies no equation `H(0)=0` in the source affine chart.

<a id="source-quintic-h2-degree-five-exclusionmd"></a>
<a id="source-quintic-h2-research-next-stepsmd"></a>
## Why the proposed eliminations do not close the branch

The proposed reductions treated `Fdet(0)=0` and its unit linear
coefficient as a simple conductor zero at source `x=0`. They concern
A4 at source infinity. Consequently they do not justify `w=0`, `a=B=0`
or the special pure-power form `Q=q5(x+v)^5`. The earlier candidate
resultants of degrees eight and eight therefore do not exclude the
complete incidence, regardless of whether their polynomial identities
hold on an additionally restricted locus.

The later calculation also extracted `q5=f7`, followed by `q4` from
`f6` and `q3` from `f5`, directly from the unreversed determinant.
After `a=B=j=0` it used `q5=delta^7`. The actual source recursion instead
uses `f1,f2,f3`, with the displayed unit `q5`. Its degree-five/degree-seven
resultants are therefore not a certificate for the stated actual-source
incidence. A successful execution of that calculation would not repair
the earlier unsupported specialization.

Both exclusion claims are withdrawn. No executed certificate of emptiness
for the complete degree-five incidence is supplied here. A repaired
exclusion needs either a valid reduction of the full original incidence or
a direct certificate over it, retaining all prescribed opens, repeated
roots and inverse-map boundary cases. Merely replaying the two proposed
resultants is insufficient. The degree-six `j != 0` branch and nonlinear
conductor-power descent also remain unresolved.

## Review scope

Independent review compared the actual primitive input, source-coordinate
correction, full monic coefficient recursion and both proposed elimination
accounts. It found the coordinate and reduction gaps above without running
the invalid verifier. Consolidation retains the valid necessary equations
and the distinct polynomial-dual theorem; it does not infer nonemptiness,
new rank facts or a broader STCI conclusion.


### Archived exact certificate: `research/computations/verify_session_nonendpoint_h2_classification_2026_10_13.m2`

Original source retained verbatim, with original limitations and relative-path assumptions.

<details><summary>Original Macaulay2 source</summary>

```macaulay2
-- Complete homogeneous quadratic common-factor cover for the corrected pair.
-- These exact identities do not assert a mate or exhaust conductor descent.
R0=QQ[sepD,aa,bb,gg,parD,rr,zz];
po=((gg-3*bb+2*aa)*rr^3+(6*sepD*(bb-aa)+sepD^3-3*sepD^2)*rr^2
 +(sepD^2*(6*aa-3*bb)+2*sepD^3)*rr-2*aa*sepD^3);
jo=((2*parD-3*gg+bb)*rr^3+(3*sepD*(gg-bb)+5*sepD^3-3*sepD^2)*rr^2
 +(3*bb*sepD^2+sepD^3-sepD^4)*rr-bb*sepD^3);
pn=((gg-3*bb+2*aa)*zz^3+(6*(bb-aa)+sepD^2-3*sepD)*zz^2
 +(6*aa-3*bb+2*sepD)*zz-2*aa);
jn=((2*parD-3*gg+bb)*zz^3+(3*(gg-bb)+5*sepD^2-3*sepD)*zz^2
 +(3*bb+sepD-sepD^2)*zz-bb);
assert(substitute(po,{rr=>sepD*zz})==sepD^3*pn);
print "PASS 1: literal normalized P, with every delta factor retained";
assert(substitute(jo,{rr=>sepD*zz})==sepD^3*jn);
print "PASS 2: literal normalized J, with every delta factor retained";
p0=-2*aa; p1=6*aa-3*bb+2*sepD;
p2=6*(bb-aa)+sepD^2-3*sepD; p3=gg-3*bb+2*aa;
j0=-bb; j1=3*bb+sepD-sepD^2;
j2=3*(gg-bb)+5*sepD^2-3*sepD; j3=2*parD-3*gg+bb;
assert(p1+3*p0-3*j0==2*sepD and p2-3*p0+6*j0==sepD^2-3*sepD
 and j1+3*j0==sepD-sepD^2
 and j2-3*p3-3*p0+6*j0==5*sepD^2-3*sepD);
print "PASS 3: four complete affine coefficient constraints";
assert(substitute(pn,{sepD=>-1,aa=>0,bb=>-2/3,gg=>-2})==0
 and substitute(jn,{sepD=>1,bb=>0,gg=>-2/3,parD=>-1})==0);
print "PASS 4: zero-cubic boundary signs, not part of exact h2";

Rn=QQ[del,v,w,ca,cb,cc,cd,z];
mn=matrix{{w,v+3*w,0,-3*w},{v,1-3*w,0,6*w},{0,0,w,v+3*w},{-3,-3*w,v,1+6*w}};
rhsn=del*matrix{{2},{del-3},{1-del},{5*del-3}};
vec=matrix{{ca},{cb},{cc},{cd}};
hm=z^2+v*z+w;
pairP=(ca*z+cb)*hm; pairJ=(cc*z+cd)*hm;
cons=matrix{{ca*w+cb*v+3*cb*w-3*cd*w},
 {ca*v+cb-3*cb*w+6*cd*w},
 {cc*w+cd*v+3*cd*w},
 {cc*v+cd-3*ca-3*cb*w+6*cd*w}};
assert(mn*vec==cons);
print "PASS 5: exact finite-H coefficient matrix";
quadK=v^2+2*w+6*v*w+6*w^2;
assert(det mn==(v^2-4*w)*quadK);
print "PASS 6: determinant separates repeated H and exceptional conic";
aaRec=-cb*w/2; bbRec=-cd*w; ggRec=ca+3*bbRec-2*aaRec;
ddRec=(cc+3*ggRec-bbRec)/2;
npRec=((ggRec-3*bbRec+2*aaRec)*z^3+(6*(bbRec-aaRec)+del^2-3*del)*z^2
 +(6*aaRec-3*bbRec+2*del)*z-2*aaRec);
njRec=((2*ddRec-3*ggRec+bbRec)*z^3+(3*(ggRec-bbRec)+5*del^2-3*del)*z^2
 +(3*bbRec+del-del^2)*z-bbRec);
rowDef=mn*vec-rhsn;
assert(npRec-pairP==-rowDef_(1,0)*z^2-rowDef_(0,0)*z
 and njRec-pairJ==-rowDef_(3,0)*z^2-rowDef_(2,0)*z);
print "PASS 7: recovering actual a,b,g,d loses no coefficient constraint";
aug=mn|rhsn;
assert(substitute(det submatrix(mn,{0,1,2},{0,1,2}),{w=>v^2/4})
 ==-3*v^4*(v+2)^2/64);
print "PASS 8: repeated-H rank is three away from roots zero and one";
repComp=del*v^2+2*del*v-2*v-2;
assert(substitute(det submatrix(aug,{0,1,2,3},{0,2,3,4}),{w=>v^2/4})
 ==-3*del*v^3*(v+2)*repComp/8);
assert(substitute(quadK,{w=>v^2/4})==3*v^2*(v+2)^2/8);
print "PASS 9: repeated-H compatibility and exceptional-conic intersection";
badZero=substitute(mn,{v=>0,w=>0});
badOne=substitute(mn,{v=>-2,w=>1});
assert(all(flatten entries submatrix(badZero,{0},{0,1,2,3}),val->val==0));
assert(all(flatten entries(submatrix(badOne,{1},{0,1,2,3})+2*submatrix(badOne,{0},{0,1,2,3})),val->val==0)
 and all(flatten entries(submatrix(badOne,{3},{0,1,2,3})+3*submatrix(badOne,{0},{0,1,2,3})
 +2*submatrix(badOne,{2},{0,1,2,3})),val->val==0));
print "PASS 10: bad double-root charts have the stated incompatible row relations";

Kp=QQ[delK,tpar]; Fk=frac Kp; denK=tpar^2+6*tpar+6;
toK=map(Fk,Rn,{delK,-2*tpar/denK,-2/denK,0,0,0,0,0});
assert(toK quadK==0);
assert(det submatrix(toK aug,{0,1,2,3},{0,2,3,4})==-24*delK*(tpar+2)/denK^2);
print "PASS 11: the complete exceptional conic has no consistent factor pair";

Ri=QQ[delI,rhoI,ai,bi,zi];
mi=matrix{{-6*rhoI^2+6*rhoI-2,6*rhoI^2-3*rhoI},
 {-6*rhoI^2,6*rhoI^2+3*rhoI-1}};
rhsi=-delI*matrix{{(delI-3)*rhoI^2+2*rhoI},
 {(5*delI-3)*rhoI^2+(1-delI)*rhoI}};
infT=6*rhoI^2-6*rhoI+1;
assert(det mi==2*infT);
print "PASS 12: infinity-plus-finite matrix determinant";
augi=mi|rhsi;
assert(det submatrix(augi,{0,1},{1,2})==-2*rhoI*delI*infT*(2*delI*rhoI+1)
 and det submatrix(augi,{0,1},{0,2})==2*rhoI*delI*infT*(2*delI*rhoI-delI+1));
print "PASS 13: Cramer numerators retain the two exceptional infinity roots";
ai0=delI*rhoI*(2*delI*rhoI+1);
bi0=delI*rhoI*(2*delI*rhoI-delI+1);
assert(all(flatten entries(mi*matrix{{ai0},{bi0}}-rhsi),val->val==0));
print "PASS 14: exact particular solution in every infinity chart";
assert(all(flatten entries(mi*matrix{{3*rhoI-1},{1}}),val->val%ideal(infT)==0));
assert(mi_(0,0)%ideal(infT)==-1_Ri);
print "PASS 15: exceptional infinity charts have a one-dimensional solution fiber";
pq=(6*(bi-ai)+delI^2-3*delI)*zi^2+(6*ai-3*bi+2*delI)*zi-2*ai;
jq=(6*(bi-ai)+5*delI^2-3*delI)*zi^2+(3*bi+delI-delI^2)*zi-bi;
assert((6*(bi-ai)+5*delI^2-3*delI)-(6*(bi-ai)+delI^2-3*delI)==4*delI^2);
print "PASS 16: a double root at infinity is impossible for nonzero delta";
assert(substitute(pq,{ai=>ai0,bi=>bi0,zi=>rhoI})==0
 and substitute(jq,{ai=>ai0,bi=>bi0,zi=>rhoI})==0);
print "PASS 17: both literal quadratic restrictions vanish at the claimed finite root";
print "PASS ALL: 17 exact structural identities; conductor-support incidence remains necessary only";
```
</details>
