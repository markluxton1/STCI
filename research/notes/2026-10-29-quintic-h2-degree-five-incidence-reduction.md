# Quintic h=2: degree-five support-incidence reduction (research checkpoint)

Status: **candidate exclusion; exact resultant identities require a standalone reproducible rerun before promotion to a proved result.** This is an investigation note, not a new authoritative result record.

## Scope

This concerns the *necessary restricted-conductor support incidence* in the characteristic-zero genus-one A4 quintic projection analysis, **not** a proof about the original rational-quartic STCI question. Work on the finite monic exact-gcd-two chart with parameters `delta,a,B,G,j,v,w`, quadratic `H=x^2+vx+w`, primitive source conductor `F_src=H Q`, and the source note's open conditions `delta E Delta1 != 0`. Do not invert the discriminant of H or the inverse-map denominator globally. Coordinate conventions matter: use the actual source-coordinate conductor, not the older shifted coefficient array.

Primary background: [conductor quotient](2026-10-14-generalization-quintic-h2-conductor-quotient.md) and [global monic ODE incidence](2026-10-15-generalization-quintic-h2-global-monic-ODE-incidence.md).

## Degree-five branch

On `j=0`, the leading coefficient of Q vanishes and the ODE support condition takes the form

```
H Q' = (5x+u) Q,   deg Q=5.
```

The conormal cubics have the same leading coefficient G. Their difference is

```
J_c-P = T*x^2 + U*x + V,
T=3G+4*delta^2, U=6B-delta-delta^2, V=a-B.
```

Since `E=G*T !=0`, the common monic quadratic must be

```
H=(J_c-P)/T,   v=U/T, w=V/T.
```

Put `L=6B+delta^2-3delta`, `M=3a-3B+2delta`, `N=L*T-G*U`. Divisibility of the first cubic by H is equivalent to

```
F0=-2*a*T^2-(a-B)*N=0,
F1=M*T^2-G*(a-B)*T-U*N=0.
```

Writing `A=2*T^2+N`, `C=3*T^2-G*T`, these give

```
a=B*N/A,
Phi=B*C*N + A*(-3*B*T^2+2*delta*T^2+G*B*T-U*N)=0.
```

The exceptional `A=0` case is excluded on the declared open set: `F0` forces `B=0`, and elimination of G from the remaining equations yields `576*delta^10*(delta+1)^2`; at `delta=-1` the common zero forces `T=0`. This calculation should be included in the reproducible rerun.

## Local conductor simplification

The candidate exact source-conductor coefficient identity on `j=0` is

```
[x]F_src = -2*G*(G+3*delta^2)^2*(G+delta^2+2*B).
```

It is a unit on the prescribed open set, while `F_src(0)=0`. Assuming these identities, the conductor has a simple zero at zero. Since every root of Q is a root of H by the ODE, a simple root of `H*Q` at zero must come from H but not Q. Thus `w=0`; the two cubic constant-term equations force `a=B=0`.

Then `H=x(x+v)`, `v != 0`, and the degree-five ODE forces

```
Q=q5*(x+v)^5.
```

The remaining common-factor equation becomes

```
R=9*G^2+2*G*delta^3+22*G*delta^2-4*G*delta
  +2*delta^5+12*delta^4-6*delta^3=0,
v=-delta*(delta+1)/(3*G+4*delta^2).
```

## Candidate exact exclusion

Using the saved quotient coefficient convention `Q=sum(q_i*x^i)`, the power condition requires

```
q4=5*v*q5,  q3=10*v^2*q5.
```

A prior exact-arithmetic calculation reported, after specializing `j=a=B=w=0`, clearing denominators, and eliminating G against R,

```
Res_G(R,q4-5*v*q5) = -12*delta^14*(delta+1)^2*f(delta)
Res_G(R,q3-10*v^2*q5) = 24*delta^16*(delta+1)^4*g(delta)
```

up to the explicitly chosen denominator-clearing convention, where

```
f=80*delta^8+1632*delta^7-25031*delta^6-51424*delta^5
  +358707*delta^4+288462*delta^3-103104*delta^2
  -294336*delta+34560

g=384*delta^8-8112*delta^7+7080*delta^6+254915*delta^5
  -1326324*delta^4-270648*delta^3+514152*delta^2
  +988956*delta-112320
```

and `gcd(f,g)=1`. Since `delta !=0` and `v !=0` excludes `delta=-1`, **these identities would exclude the entire degree-five branch**. The result is not promoted until the source expressions, coefficient ordering, denominator clearing and polynomial gcd are independently rerun from a single executable script.

## Next work

1. Reproduce the candidate exclusion directly from the saved exact source conductor and quotient coefficients, with a small exact-arithmetic script and clear assumptions.
2. If verified, promote a short theorem with the script as reusable calculation; do not preserve ordinary calculation mistakes or audit chronology.
3. Then analyze the remaining `j != 0`, degree-six branch. The degree-five result alone does not establish emptiness of the global h=2 incidence.

Repository design: this note is an **investigation dossier checkpoint**. General conductor-annihilation and support lemmas belong in their reusable theorem homes; this note links them and keeps the specialized reduction together.
