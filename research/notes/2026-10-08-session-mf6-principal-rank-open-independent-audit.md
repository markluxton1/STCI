# Principal e=1,d2=1 quartic rank: independent open-chart audit

Date: 2026-10-08. Fixed `C0=[s^4:s^3t:st^3:t^4]`, characteristic
zero. Status: **PROVED HERE, exact polynomial certificate on the stated
open**. This does not exclude a quartic with a higher-degree mate.
The chart complement is separately owned by the principal-boundary audit.

For the quotient direction `A=1+r z`, `B=1+p z`, write

```
H = 8p^3 -(64r^2+128r+16)p^2
    +(96r^4+512r^3+592r^2+128r+6)p
    -(576r^6+960r^5+880r^4+544r^3+220r^2+60r+9),
P = 2p+12r^2+16r+9,
T = 2p-4r^2-4r-1,
S = p-2r-1,
Q = 12r^2+20r+11.
```

The theorem is that the complete vector space of ambient quartic forms
containing the associated genuine triple has dimension exactly one on

```
U = {H=0, p P (p-r) (2r-1) T != 0}.
```

Thus this entire open cannot supply two independent quartic ancestors.
A unique quartic can still serve as one carrier in an STCI pair; that
question is not settled by this calculation.

## 1. Complete ambient first-normal space and the exact frame

The standalone verifier
[`verify_session_mf6_principal_rank_open_2026_10_08.py`](../computations/verify_session_mf6_principal_rank_open_2026_10_08.py)
reconstructs the first and second normal equations from eighteen
independent actual quartic forms. Their coefficient rank is eighteen,
and all vanish on `C0`; the thirty-five quartic monomials restrict to
all seventeen powers `z^0,...,z^16`. Consequently these forms constitute
the entire degree-four ideal space, rather than a sampled subspace.

Using the normal chart

```
x0=1, x1=z, x2=z^3+V, x3=z^4+U+(3/2)zV,
U= -r m/(p-r)+(1+rz)y,
V= -p m/(p-r)+(1+pz)y,
```

the first normal matrix `M1` has shape `11 x 18`. Its columns
`0,1,2,3,4,5,6,11,12,14,15` have determinant

```
p^4(p-r)(2r-1)T^2 / 256.
```

It therefore has rank eleven everywhere on `U`. The seven columns
`N` saved in the reconstruction, after dividing each by its separately
recorded polynomial gcd, lie in `ker(M1)`. The free rows
`7,8,9,10,13,16,17` are diagonal, with diagonal entries

```
-(2r-1)T^2/256,
-(2r-1)T/128,
-(2r-1)T^2/256,
-1/32,
-p(2r-1)T^2/256,
-p^3(2r-1)T^2/256,
-p^4(2r-1)T^2/256.
```

Their determinant is `-p^8(2r-1)^6T^11/2^52`, a unit on `U`.
Thus these seven columns form the complete first-normal kernel in
every fiber of this open, with no generic-only frame assumption.

Let `h2` be the accepted quadratic cocycle,

```
h2 = -(2A+zB)(12A^2+3z^2B^2+4z^2(A'B-AB'))/(8z^5).
```

Its three negative Laurent coefficients satisfy `64(c1c3-c2^2)=H`.
Choose

```
delta = -8c2+8c1z = (2r+1)(8p+12r^2+4r+3)-pPz,
Gamma = polynomial part of delta*h2.
```

The exact identity `Res_z(delta,Gamma)=p^4P^4/8` gives triple flatness
on this chart. If a quartic's first normal coefficient in `m` is `h`
and its quadratic coefficient in `y` is `q2`, the second contact
condition is `delta*q2-Gamma*h=0`. Multiplying by the unit `p-r`
produces the saved complete matrix `M2`.

On `H=0`, the product `M2*N` has its last five rows zero; its seventh
row is a multiple of `H`. Divide the first six rows by
`p-r,p-r,p-r,p-r,p(p-r),p^2(p-r)`, respectively. The resulting
`6 x 7` polynomial matrix is denoted `D`. Every row division is by a
unit on `U`. Its rank is the actual contact rank of the complete
first-normal kernel.

## 2. Factor before reduction; only two residual norms are needed

The independent raw-factor computation retained all seven actual
cofactors, instead of reducing matrix entries modulo `H` before taking
determinants. The latter operation produces degree-fifty expressions,
although it is algebraically correct. For cofactors obtained by omitting
columns six and five, respectively, the exact factorization is

```
M6 = (27/2^51) p^5(2r-1)^4(2r+1)^3 S^3 T^7 R6,
M5 = (27/2^51) p^5(2r-1)^4(2r+1)^3 S^3 T^7 R5.
```

`R6` and `R5` are the completely recorded residual polynomials of
total degrees twenty and twenty-one in
[`audit-mf6-e1-principal-raw-minors-2026-10-08.json`](../scratch/audit-mf6-e1-principal-raw-minors-2026-10-08.json).
The verifier independently recomputes every cofactor, checks these
factor identities and all five others, and compares their reductions
with the previously saved seven-cofactor remainders.

The factor `2r+1` is a unit on `U`, for the precise reason

```
H(p,-1/2)=8p(p+2)^2,
P(p,-1/2)=2(p+2).
```

Both possible points violate `pP!=0`. An earlier informal message
incorrectly gave `H(p,-1/2)=8(p+2)^3`; the corrected identity above is
checked directly by the verifier and is the one used in the proof.

On `S!=0`, every displayed prefactor of `M6,M5` is a unit. If their
residuals vanish simultaneously at a point of `H`, then both exact
resultants in `p` vanish at its `r` coordinate. Their gcd is

```
const * (2r-1)^16(2r+1)^26 Q^5,
const = 175495605123022848.
```

The full factorizations are

```
Res_p(H,R6) = const * (2r-1)^16(2r+1)^26 Q^6 F12,
Res_p(H,R5) = -8const * (2r-1)^16(2r+1)^27 Q^5 F16,
```

where

```
F12 = 626688r^12+2113536r^11+7473152r^10+9351168r^9
      +16506624r^8+15984640r^7+7622400r^6+3220992r^5
      +1515632r^4+554304r^3+123528r^2+14832r+801,

F16 = 518455296r^16-3247570944r^15-13217169408r^14
      -31615975424r^13-48489316352r^12-51974971392r^11
      -40950489088r^10-25317873664r^9-13339307520r^8
      -6235899392r^7-2459068928r^6-740795520r^5
      -157172544r^4-21102432r^3-1591200r^2-59976r-8577.
```

The verifier checks the exact resultant gcd, including all possible
cross-factor common roots; this is stronger than separate informal
coprimality assertions about `F12,F16`.

The roots `r=+/-1/2` have already been removed on `U`. At a root of
`Q`, use `K=QQ(sqrt(-2))` and
`r=(-5+2sqrt(-2))/6`. Direct Euclidean division in `K[p]` yields

```
gcd(H,R6,R5)=p-(2r+1).
```

The checker verifies an extended-Euclidean identity and divisibility,
so this is a complete exact fiber calculation. Its conjugate covers
the other root of `Q`. But `p=2r+1` on `Q=0` implies `P=0`.
Therefore neither quadratic fiber contains a common residual zero
on `U`. This proves that the two cofactors cannot vanish simultaneously
on `U` intersected with `S!=0`.

## 3. Retain and cover the nonunit factor S

`S` is not a unit and was never silently cancelled. Its entire fiber
on `H` is given by

```
H(2r+1,r)=-(2r-1)^2(2r+1)(6r+1)Q,
P(2r+1,r)=Q.
```

The roots `r=+/-1/2` and `Q=0` violate the defining open conditions.
The sole remaining point is `r=-1/6,p=2/3`, with `P=8`.
At that point, the actual cofactor omitting column four is

```
1073741824 / 36472996377170786403 != 0.
```

This independently covers the retained `S=0` branch. Consequently
`rank(D)=6` everywhere on all of `U`. Since `rank(M1)=11` and the
first-normal kernel has dimension seven, the complete quartic matrix
has rank seventeen and its kernel has dimension one.

## 4. Evidence and exact remaining scope

The source and raw inputs are bound by SHA-256 in
[`session-mf6-principal-rank-open-audit-2026-10-08.json`](../scratch/session-mf6-principal-rank-open-audit-2026-10-08.json),
with the successful terminal transcript in
[`session-mf6-principal-rank-open-audit-2026-10-08.out`](../scratch/session-mf6-principal-rank-open-audit-2026-10-08.out).
The independent raw-factor explorer and norm explorer are preserved
beside their outputs. Three preliminary verifier runs were corrected:
one transcribed the free determinant denominator as `2^53` rather
than `2^52`; two used structural SymPy equality instead of
expanded polynomial equality (a cofactor remainder and the linear P specialization). Their failed transcripts are retained.
None of these failed runs entered the resultant/fiber argument.

This theorem covers only the displayed principal flat chart with
`a0=b0=1`, including every parameter of that chart, rather than merely
a generic rank computation. The `P=0` alternate-killing-section fibers,
`r=1/2` frame degenerations, `b0=0`, and the earlier endpoint orbits
must still be reconciled by their complete ambient quartic calculations
before asserting a theorem for the whole principal triple incidence.
The existence or nonexistence of an STCI mate for the remaining unique
quartic carriers is a separate problem and is not claimed here.
