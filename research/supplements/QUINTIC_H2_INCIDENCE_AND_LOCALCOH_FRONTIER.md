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
