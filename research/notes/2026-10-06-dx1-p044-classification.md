> **SUPERSEDED STATUS NOTICE (2026-10-06 cleanup):** The residual saturation calculation requested below was subsequently completed exactly. The Macaulay2 unit-ideal/saturation certificate in `research/computations/session_dx1_saturation_2026_10_06.m2` and its recorded output closes the residual open set. Together with the audited boundary calculation, the basepoint-free P-044 locus on the dx=1 slice is exactly P-045. This note is retained as provenance for the pre-certificate argument and its identified gap; do not use its OPEN conclusion as current status. See `research/AUDITED_STATE_2026-10-06.md`, Section G.

# dx=1 P-044 classification

Date: 2026-10-06

Status: **OPEN pending one residual saturation calculation.** Independent audit found a genuine gap in the previous residual-open argument: coprimality of two multivariate resultant factors does not imply that their common affine zero set is empty.

On the slice
[
d=x^{-1},qquad u=bx-a,
]
the resultant is
[
Delta=u^2/x.
]
Thus the basepoint-free locus is (D(xu)).

The exact P-044 coordinates specialize as (G_i=uQ_i). Two coordinates have
[
Q_2=(2a+1)R_2,qquad Q_4=2(b+2)R_4.
]

## Audited boundary pieces

On (b=-2), the exact residual calculation shows that every extra common zero has (u=0), hence (Delta=0). Therefore on (D(Delta)),
[
b=-2, P	ext{-044}Longrightarrow a=-1/2.
]

On (a=-1/2), the dedicated exact verifier shows
[
P	ext{-044}Longrightarrow b=-2quad	ext{or}quad u=0.
]
The second alternative lies on (Delta=0). Hence the basepoint-free part of this boundary is exactly P-045.

## Residual open set: still open

On
[
D!left(xu(2a+1)(b+2)ight),
]
P-044 implies
[
R_2=R_4=Q_5=0.
]
After (b=(a+u)/x), exact elimination gives
[
operatorname{Res}_u(R_2,R_4)=-36x(2a+1)P_{24}(a,x),
]
[
operatorname{Res}_u(R_2,Q_5)=-36x^2(2a+1)^2P_{25}(a,x),
]
and
[
gcd(P_{24},P_{25})=1quad	ext{in }mathbf Q[a,x].
]

These identities are exact, but the former conclusion that they prove emptiness was invalid: two coprime multivariate polynomials can have isolated common zeros. The independent audit found such resultant intersections, including ((a,x)=(-1,1/4)) and ((-3/2,1/4)); those sampled points lift only to (u=0) and hence are not counterexamples, but they demonstrate the logical gap.

The required repair is an exact certificate that
[
V(R_2,R_4,Q_5)cap D!left(xu(2a+1)(a+u+2x)ight)=arnothing,
]
equivalently that the corresponding saturated ideal is the unit ideal. Direct SymPy Gröbner/Rabinowitsch attempts timed out on 2026-10-06, so no replacement certificate is claimed here.

Therefore the complete classification
[
d=x^{-1},quadDelta
e0,quad P	ext{-044}
iff
a=-rac12,quad b=-2
]
is **not yet proved**.

Consequently the no-carrier statement on the whole (dx=1) slice is also **OPEN pending this residual calculation**. Its final implication remains valid: if the classification is repaired, P-045's cubic-factor theorem excludes a quartic carrier.

Verifier/diagnostic:
`research/computations/verify_dx1_p044_residual.py`.

Boundary verifier:
`research/computations/verify_dx1_a_half_boundary.py`.
