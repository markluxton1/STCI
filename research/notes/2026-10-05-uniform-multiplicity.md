# Uniform quasiprimitive restrictions with a quartic carrier

Status: proved numerical consequences of checked quasiprimitive Gorenstein
duality; exact exploratory calculation for the primitive `(4,7)` branch.
Work in characteristic zero with a smooth rational quartic
`C ⊂ P³`; the formal computations below use
`C0=[s⁴:s³t:st³:t⁴]`. These restrictions do not address pairs whose
two carriers have degree at least six and are thick along the whole curve.

## Checked duality input

The full, unbounded multiplicity statement is justified by Nicolae Manolache,
[Duality for Gorenstein multiple structures on smooth algebraic varieties,
Rev. Roumaine Math. Pures Appl. 68 (2023), 141–148](https://imar.ro/journals/Revue_Mathematique/pdfs/2023/1-2/10.pdf),
theorem on p.143, embedded specialization and Remarks 1–2 on pp.144–145.
The preprint is [arXiv:0706.2204](https://arxiv.org/pdf/0706.2204).
For curves the free-type condition is automatic. Quasiprimitivity makes the
three canonical filtrations coincide. The original Boratyński article was
not independently fetched in this investigation.

An independent local check removes any reliance on a finite-multiplicity
classification. Complete at a support point, put `A=k[[t]]`, and let `B` be
the local finite flat Gorenstein algebra. Quasiprimitivity gives
`B⊗K ≅ K[z]/(z^n)`, `K=Frac(A)`. Its saturated BF ideals are
`B_i=B∩z^i B_K`. They satisfy `ann(B_i)=B_{n-i}`: this holds generically,
and torsionfreeness detects equality inside `B`. A perfect Gorenstein
multiplication functional `B→A` has orthogonal complement of each ideal
equal to its annihilator. Passing to successive quotients gives perfect
pairings

`E_i ⊗ E_{n-1-i} ≅ E_{n-1}`.

Writing `L=E_1`, the iterated multiplication `L^i→E_i` has a canonical
effective zero divisor `D_i`, so `E_i=L^i(D_i)`, with `D_0=D_1=0`.
Associativity and perfect complementary multiplication give actual divisor
identities and inequalities

`D_i+D_j ≤ D_{i+j}`, and `D_i+D_{n-1-i}=D_{n-1}`.

The top piece is the annihilator of the support ideal. CM duality therefore
gives `E_{n-1}=ω_C⊗(ω_X|C)^(-1)`. None of these statements assumes the
multiple curve is primitive everywhere.

## Proved uniform bounds for `(4,b)`

Suppose `X=V(F_4,G_b)` is supported on `C`, with `b≥4`. The quartic has
normal order one generically by project result P-011. The generic transverse
CI is therefore curvilinear of length `b`, so `X` is quasiprimitive.
Adjunction and `O_C(1)=O_P1(4)` give

`deg E_{b-1}=-4b-2`.

The quotient `O(-7)^2→L` has `deg L=e-7`, where `e≥0` is the degree of
its basepoint-free pair of binary forms. Hence, putting `s=b-1`,

`deg D_s = (3-e)s-6 = (3-e)b+e-9`.

Effectivity implies **`e≤2` for every `b≥4`**, with `e≤1` when `b≤6`.
Thus arbitrarily large mate degree does not produce arbitrarily complicated
horizontal normal directions. The exact top-defect degrees are

| e | deg L | deg D_(b-1) |
|---|---|---|
| 0 | -7 | 3b-9 |
| 1 | -6 | 2b-8 |
| 2 | -5 | b-7 |

More strongly the **first defect degrees remain uniformly bounded**:

| e | permitted deg D_2 | upper bound for deg D_3 |
|---|---|---|
| 0 | 1 through 5 | 8 |
| 1 | 0 through 3 | 5 |
| 2 | 0 or 1 | 2 |

To prove the second column, put `s=2q+r`, `r∈{0,1}`. Superadditivity
gives `q deg D_2≤(3-e)s-6`, which is strictly less than
`q·2(3-e)` for `e=0,1,2`. Thus `deg D_2≤2(3-e)-1`.
For `e=0`, `D_2=0` would give the prohibited primitive triple of
conormal type `O(-7)` from P-010, giving the positive lower bound.
For the third column write `s=3q+r`. If `e=1,2`, the remainder
`(3-e)r-6` is negative, giving `deg D_3≤3(3-e)-1`.
For `e=0,r=2`, use the stronger inequality
`q deg D_3+deg D_2≤deg D_s`; the positive lower bound for `deg D_2`
again yields `deg D_3≤8`.

This is a useful uniform reduction, not an upper bound on `b`. In particular,
it suggests classifying admissible embedded triples and quadruples with
these few defect degrees before repeating higher-multiplicity numerics.
For `e=2,b=7` the top defect is zero and the whole structure is primitive;
for `e=2,b=8` one has `D_2=D_3=0`, so the canonical quadruple is primitive.
An obstruction to primitive quadruples of type `O(-5)` would thus close both
these branches and potentially larger cases with small early defects.

## A tempting false first-normal identity

The identity `A=D_top`, where `A` is the common vertical Fitting divisor
of the defining differentials, is false in arbitrary multiplicity. Over
`A=k[[t]]`, take the finite flat CI

`B=A[[x,y]]/(tx-y^r,x^s)`, with `r,s≥2`.

It has rank `n=rs`, generic curvilinear algebra, and radical `(x,y)`.
The first-normal image is `t·x`, so `A=[t=0]`. The basis
`x^i y^j`, `0≤i<s, 0≤j<r`, identifies

`D_k=floor(k/r)[t=0]`.

In particular `D_top=(s-1)[t=0]`. Complementary divisor duality is satisfied,
but the differential divisor only equals the top defect when `s=2`.
The example is a local finite flat model, not a global projective candidate.

## Exact primitive-fourth calculation, exploratory status

The script
`research/scratch/primitive47/obstruction.py` computes the obstruction to
extending the unique primitive triple of type `L=O(-5)` to a primitive
quadruple on `C0`. Input is a coprime pair of binary quadratics `A,B`,
describing the quotient `u↦A,v↦B` in the repository's split normal frame.
Set `m=Bu-Av` and choose polynomial Bezout coefficients to get a quotient
coordinate `ell`. The kernel line is `M=O(-9)`.

Since `Hom(M,L²)=O(-1)`, the primitive triple extension has no obstruction
and no free extension parameter. Its quadratic gluing correction is the
unique Laurent splitting of the moving-coordinate cocycle. The next
obstruction lies in `H¹(Hom(M,L³))=H¹(O(-6))` and has five Laurent
coordinates. All coefficient functions on the second chart are evaluated
at the exact moving coordinate `W=(z³+a)/(z⁴+b)` before truncation.

For example the quotient `A=z²,B=1` has fourth obstruction coordinates

`(-35,-3,15,-3/4,-35/16)`.

This nonzero vector excludes primitive quadruples, and hence primitive
seventuples, **for that particular quotient direction**. Several additional
sample pairs also give nonzero vectors. The calculation has not yet
classified all coprime quadratic pairs and is not a no-`(4,7)` theorem.

## Supersession note: later 2026-10-05 full e=2 calculation

The forward-looking sentence above suggesting that a universal primitive-
quadruple obstruction of type (O(-5)) might close the (e=2) branches is
now **superseded**. The generic four-parameter obstruction was subsequently
regenerated and the universal implication
[
Omega=0Longrightarrowoperatorname{Res}(A,B)=0
]
was **FALSIFIED** by the explicit basepoint-free family
[
A=z^2-	frac12z+x,qquad B=1-2z+x^{-1}z^2,
qquad x
e0,	frac14.
]
The exploratory sample computations in this note remain historically valid
for the quotient directions they actually test. See
`2026-10-05-e2-full-obstruction.md` for the corrected current frontier.
