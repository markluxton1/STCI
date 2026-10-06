# Rational-resolution carriers: numerical denominator compression

Date: 2026-10-06. Status: proved conditional compression theorem and a
finite normal-quartic mate bound. The condition is that a mate exists on
the specified normal carrier. Numerical coincidence alone is not promoted
to a global construction on an unspecified surface.

## 1. Compression on a normal surface with rational resolution

Let `S⊂P^3` be an integral normal surface of degree `a`, and suppose its
smooth projective resolution `sigma:M→S` is rational. Let `C⊂S` be an
integral curve of degree `delta`, with strict transform `c`. Write
`H=sigma^*O_S(1)`. Suppose an ambient degree-`b` surface cuts out `C`
set-theoretically on `S`. Its divisor is `rC`, where `r delta=ab`.

Let `Cbar=c+Z` be the numerical pullback, characterized by orthogonality
to every exceptional curve. Pulling back the Cartier relation `rC~bH`
gives `Cbar≡(delta/a)H`.

Choose the least positive integer `n` which clears the coefficient
denominators of `Z` and of `delta/a`. Then

`D=n((delta/a)H-c-Z)`

is an integral divisor numerically equivalent to zero. A smooth rational
projective surface has torsion-free Picard group, with numerical
equivalence equal to linear equivalence. For example this follows on a
minimal rational model (`P^2` or a Hirzebruch surface), and each blowup
adds one free exceptional summand. Thus `D` is principal on `M`.

Push its principal divisor down to the normal surface `S`. The rational
function field is unchanged, and exceptional divisors disappear. Hence

`nC~(n delta/a)H` on `S`.

This is an actual Weil-divisor linear equivalence to a Cartier divisor,
not merely numerical equivalence. In particular `nC` is effective
Cartier, and its canonical section is a section of
`O_S(n delta/a)`. It lifts to a homogeneous ambient form, because the
restriction sequence and `H^1(P^3,O(t))=0` give surjectivity of
`H^0(P^3,O(n delta/a))→H^0(S,O_S(n delta/a))`. The lift supplies a mate
of degree `n delta/a` supported exactly on `C`.

This proves the **numerical-denominator compression theorem**. For
`a=delta=4`, its conclusion is simply `nC~nH`, with a mate of degree `n`.
Moreover any mate degree `b` clears the coefficients of `Z`: its Cartier
divisor pullback has integral exceptional coefficients. Thus `n|b`, and
`n` is the least mate degree for this fixed normal quartic carrier.

The proof uses rationality of the entire resolution. It cannot cancel a
torsion scalar in an arbitrary local class group. A cusp or elliptic
local Picard group may have further torsion in general, but under the
global mate hypothesis and rational-resolution condition the linear
equivalence above removes that possible inflation.

For `C0` in characteristic zero the known exclusions of degrees `(4,4)`
and `(4,5)`, together with the unique-quadric and all-cubic exclusions,
force this compressed degree to be at least six. The all-cubic theorem
also eliminates a reducible compressed mate having a cubic component.

## 2. Uniform bound for the remaining normal quartic carriers

The source classification and its hypotheses are recorded in
`research/notes/2026-10-05-normal-quartic-carriers.md`: a surviving normal
quartic carrier for a smooth rational quartic has rational resolution
with `K_M=-E`, where `E` is a nonzero effective exceptional divisor.
Ishii–Nakayama's exhaustive types give

| `d=-E^2` | Rational types | `rho(M)` |
|---:|---|---:|
| 1 | B2, B3 | 11 |
| 2 | B1 | 12 |
| 3 | D | 13 |

Let `E_1,...,E_r` be **all** exceptional prime curves and put
`A_ij=-E_i.E_j`, `b_i=A_ii=-E_i^2`, and `E=sum a_i E_i`, with
nonnegative integral `a_i`. The matrix `A` is positive definite. All
exceptional classes are independent and orthogonal to `H`, so
`r≤rho(M)-1=9+d`.

The resolution is minimal. Therefore `K_M.E_i≥0`: an exceptional curve
with negative canonical intersection would be a smooth rational
`(-1)` curve, contradicting minimality. Adjunction, including arithmetic
genus for a possibly singular exceptional prime curve, gives

`(A a)_i=K_M.E_i=b_i+2p_a(E_i)-2≥0`.

For `a_i=0`, one also has `K_M.E_i=-E.E_i≤0`, since distinct curves
have nonnegative intersection. Thus the displayed term is zero; `b_i>0`
forces `p_a(E_i)=0,b_i=2`. Such a curve is disjoint from the support of
`E`. In particular every vertex with `b_i>2` has `a_i≥1`.

Multiplying the displayed adjunction equation by `a_i` and summing gives

`d=a^T A a=sum a_i(b_i+2p_a(E_i)-2)`.

Every summand is nonnegative. Each vertex with `b_i>2` contributes at
least `b_i-2`. Consequently

`sum (b_i-2)_+≤d`.

For every positive integer `b`,
`b≤2(3/2)^((b-2)_+)`. Equality holds for `b=2,3`, and the inequality
then follows successively since `(b+1)/b≤3/2`. Hadamard's determinant
inequality now gives

`det A≤prod b_i≤2^r(3/2)^d≤2^(9+d)(3/2)^d=512·3^d`.

The exceptional correction has coefficient vector `A^(-1)m`, where
`m_i=c.E_i` are integers. By the adjugate formula, its denominator `n`
divides `det A`. Section 1 turns that denominator into an actual mate.
Therefore the least mate degree for the fixed carrier satisfies

| `d` | Uniform compressed mate bound |
|---:|---:|
| 1 | `n≤1536` |
| 2 | `n≤4608` |
| 3 | `n≤13824` |

**Bounded conclusion.** Every hypothetical normal quartic carrier for
`C0` in characteristic zero admits a mate of degree between 6 and 13824,
with the sharper row bound determined by `-E^2`. The simple-elliptic
case is already excluded in the companion note. The bound also covers
singular, reducible and nonreduced anticanonical `E`; it does not require
a reduced cusp cycle, a first-normal ratio assumption, or any prediction
of the precise local Cartier index before a mate is known.

This supplies a finite degree reduction for **normal quartic carriers**.
It does not bound mates on nonnormal quartic carriers or minimum carrier
degrees above four. It is a large theoretical bound, not an enumeration
of all coefficients or a practical exhaustive search already performed.

## 3. A small cusp numerical survivor is killed by the compression

A reduced rational cycle with intersection matrix

`A=[[3,-1,0,-1],[-1,2,-1,0],[0,-1,2,-1],[-1,0,-1,2]]`

has `E=sum E_i`, `E^2=-1`, and determinant four. A smooth-curve
intersection vector meeting the vertex opposite the `(-3)` vertex would
be `m=(0,0,1,0)`. The correction is

`A^(-1)m=(1,3/2,2,3/2)` and `m^T A^(-1)m=2`.

Adding six independent `A1` intersections gives total correction five,
with numerical denominator two. If this configuration belonged to an
actual mate-compatible rational normal quartic, §1 would produce a
quadric mate, contradicting the unique-quadric obstruction.

This is an exact numerical illustration, not a claim that the specified
smooth curve passage or first-normal order exists on a quartic. In
particular assigning a local first-normal order of three at this cusp
has not been justified. The point is that a numerical configuration
which survives a coarse genus/rank budget may still be eliminated by
global denominator compression.

Exact companion:
`research/computations/verify_normal_rational_carrier_compression.py`.
It checks this matrix, the correction denominator and the three uniform
determinant bounds. It returned `PASS` under
`/private/tmp/stci-cas-venv/bin/python`; output is saved in
`research/computations/normal_rational_carrier_compression_2026-10-06.json`.
Its output does not verify the cited classification
or the global Picard and divisor arguments, which are proved above.
