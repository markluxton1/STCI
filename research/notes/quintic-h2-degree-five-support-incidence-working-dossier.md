# Quintic h2: degree-five support-incidence reduction (working dossier)

**Status:** mathematical reduction with a **provisional computational exclusion**; not a promoted theorem. Characteristic zero. This note records the current argument and the exact verification still required, not a history of attempts.

## Question and scope

For the quintic h2 projection/mate investigation, determine whether the *necessary* common-conormal-quadratic, conductor-divisibility, and conductor-support ODE incidence has points. Even a point of this incidence would **not** by itself produce a projection or an STCI: inverse fibers, center avoidance, and nonlinear conductor descent remain additional conditions.

The global, denominator-free formulation and its hypotheses are in [the monic ODE incidence note](2026-10-15-generalization-quintic-h2-global-monic-ODE-incidence.md). This dossier treats the **degree-five branch** `j=0`; the degree-six branch `j != 0` remains open. Keep the global open `delta * E * Delta1 != 0`; do not invert the discriminant of H or inverse-map denominators.

## Exact common-factor reduction for j=0

In source coordinate `x=r/delta`, the conormal cubics are

```text
P  = G*x^3 + (6*B+delta^2-3*delta)*x^2
     + (3*a-3*B+2*delta)*x - 2*a
Jc = G*x^3 + (6*B+3*G+5*delta^2-3*delta)*x^2
     + (3*a+3*B+delta-delta^2)*x - a-B.
```

Set
```text
T=3*G+4*delta^2,
U=6*B-delta-delta^2,
V=a-B,
L=6*B+delta^2-3*delta,
M=3*a-3*B+2*delta,
N=L*T-G*U.
```
On `j=0`, the cofactor determinant is `E=G*T`, so `G,T` are units. Since `Jc-P=T*x^2+U*x+V`, the common monic quadratic must be
```text
H=x^2+v*x+w,  v=U/T,  w=V/T.
```
Divisibility of both cubics is equivalent to the two remainder equations
```text
F0=-2*a*T^2 - V*N = 0,
F1=M*T^2 - G*V*T - U*N = 0.
```
Put `A=2*T^2+N` and `C=3*T^2-G*T`. Then `F0=-A*a+B*N` and `F1=C*a-3*B*T^2+2*delta*T^2+G*B*T-U*N`. Where `A` is invertible,
```text
a=B*N/A,
Phi=B*C*N + A*(-3*B*T^2+2*delta*T^2+G*B*T-U*N)=0.
```
The admissible open specializes to
```text
delta*G*T*(G+3*delta^2)*(G+delta^2+2*B) != 0.
```
The claim that `A` is a unit on this locus follows by examining `A=0`: `F0` forces `B=0`, and the resultant of the remaining equations restricts `delta` to `0,-1`; `delta=0` is excluded and the `delta=-1` solution forces `T=0`. This argument should be encoded in a small exact symbolic test before promotion.

## Conductor/ODE restriction and provisional exclusion

Write the actual primitive source conductor as `Fsrc=H*Q`. On the degree-five branch, `Q` has degree five, and the support ODE is
```text
H*Q'=(5*x+u)*Q.
```
On the admissible `j=0` open, the source-conductor linear coefficient was calculated as
```text
[x]Fsrc = -2*G*(G+3*delta^2)^2*(G+delta^2+2*B),
```
which is a unit. Since `Fsrc(0)=0` is a simple zero and all roots of `Q` lie among roots of `H`, the zero cannot come from `Q`; hence `w=0` and `Q(0) != 0`. The two cubic constant remainders give `a=B=0`. Then `H=x*(x+v)`, with `v != 0`, and the ODE forces `Q=q5*(x+v)^5`. Thus
```text
q4=5*v*q5,  q3=10*v^2*q5.
```
With `a=B=j=w=0`, the remaining conormal equation is
```text
R=9*G^2+2*G*delta^3+22*G*delta^2-4*G*delta
  +2*delta^5+12*delta^4-6*delta^3=0,
v=-delta*(delta+1)/(3*G+4*delta^2).
```
A previous exact-symbolic computation of the two quotient-coefficient resultants reported (up to nonzero constants/denominator clearing) factors `delta^14*(delta+1)^2*f(delta)` and `delta^16*(delta+1)^4*g(delta)`, where
```text
f=80*delta^8+1632*delta^7-25031*delta^6-51424*delta^5
  +358707*delta^4+288462*delta^3-103104*delta^2
  -294336*delta+34560
g=384*delta^8-8112*delta^7+7080*delta^6+254915*delta^5
  -1326324*delta^4-270648*delta^3+514152*delta^2
  +988956*delta-112320
```
and `gcd(f,g)=1`. Because `delta != 0` and `v != 0` excludes `delta=-1`, these identities **would** prove the degree-five incidence empty.

**Verification boundary:** the exact source quotient-coefficient expressions, denominator-clearing factors, and both resultant identities have **not been independently replayed in this dossier**. Do not cite the exclusion as an established result or remove the degree-five branch from authoritative global systems until that replay succeeds. In particular, verify the claimed conductor linear coefficient from the original octic and confirm that the saved `q_i` index convention matches `Q=sum(q_i*x^i)`.

## Next work

1. Build a compact exact-arithmetic script that loads the authoritative conductor/quotient input, specializes `j=a=B=w=0`, and checks the two resultant identities and `gcd(f,g)=1`.
2. If verified, promote a concise degree-five exclusion theorem with its exact domain and link to the script.
3. Only then investigate the degree-six branch `j != 0`; retain discriminant-zero and inverse-map boundary cases.

This is an investigation dossier, not an audit log. Ordinary correction history is intentionally omitted.
