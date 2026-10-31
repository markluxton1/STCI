# The fixed elliptic target fails polarization: a two-torsion spin defect

October 31, 2026. Status: **independently reviewed provisional result**,
with the [proof, replay and strategy audit](2026-10-31-palindromic-polarization-spin-audit.md).
The fixed candidate's target construction was independently replayed and
passes. Its first component-polarization gate fails. Residue gluing, contact,
carrier construction and mate descent were not attempted after that failure.
The unrestricted characteristic-zero STCI question remains open.

**Subsequent constructive comparison:** the
[paired-cover construction](2026-10-31-paired-elliptic-construction.md)
realizes trivial spin and the actual A,B divisors simultaneously. It
fails the separate node-gluing condition. This verifies that the spin
finding here does not exclude all target constructions.

## 1. Exact question and replay boundary

The [reviewed canonical-extension criterion](2026-10-31-elliptic-canonical-extension.md)
requires, before node gluing, the equality
`L^2 = O_E(Z)` for the proposed palindromic target, where L is the degree-two
bundle of its A-map and Z is its four marked inverse points. This is a
condition on line bundles, not just their degrees. Both smooth-quadric and
cone constructions in that criterion need it.

Use the [existing fixed target](2026-10-30-projection-elliptic-target-palindromic.md):

\[
\eta^2=-4/5,\quad R(t)=t^4+\eta t^3+\eta t+1,\quad
R(t)^5=e_0(t^3)+t e_1(t^3)+t^2e_2(t^3),
\]
\[
S(A)=(\eta A+1)(A+\eta)(A^2-7\eta A+1),\qquad
D(A)=5A^4+\tfrac{28}5\eta A^3+\tfrac{102}{25}A^2+
\tfrac{28}5\eta A+5.
\]

The normalized elliptic curve and second ruling function are

\[
E:y^2=-3D(A),\qquad B=\frac{-e_1(A)+S(A)y}{2e_2(A)}.
\]

The four points satisfy `A=t_i^3`, `B=t_i`, with R(t_i)=0.
All work is in characteristic zero, over Q(eta) followed by algebraic
closure. The two conjugate choices of eta give the same verdict.

The [exact Python replay](../computations/verify_palindromic_picard_gate_2026_10_31.py)
reconstructs the fixed target independently of the inherited Macaulay2
execution. Its [saved output](../computations/palindromic_picard_gate_2026_10_31.json)
records Python 3.15.2 and SymPy 1.14.0. Macaulay2 was not available in this
session; its original script and output remain unchanged. The replay checks:

- R is separable with no root at either parameter endpoint; the target
  equation is primitive of full bidegree (6,2).
- Its discriminant is `-3 S^2 D`, with D a separable quartic. Hence the
  normalization is a smooth elliptic curve, and the target is integral.
- Restriction to the fixed quartic is exactly R(t)^5, and
  `gcd(R(t), discriminant(t^3))=1`. Thus the four target intersections
  are smooth, have exactly one normalized inverse point each, and have
  contact five. There are no extra inverse points at infinity.
- The degree-two A and degree-six B zero/pole divisors are reduced and
  pairwise disjoint. The two doubled roots visible in e_0 or e_2 each
  split into two simple normalized branches: the discriminant has order
  two there and the complementary coefficient is a unit. The four
  remaining roots are simple. At A=0 and infinity the relevant leading
  and constant coefficients are nonzero, so the two ruling boundaries
  do not meet.

Consequently f=B^3/A has degree twenty, fibers `(3^6,1^2)` over zero and
infinity and `(5^4)` over one. Their ramification contributions are
12+12+16=40, all the ramification allowed by Riemann--Hurwitz on E.
No other branch value remains. This is a replay of the fixed target,
not the earlier script's preliminary variable-parameter exploration.

## 2. Exact failure of the component Picard equality

Let H be the sum of the two points at infinity on the quartic model E.
In local coordinates `x=1/A`, `v=y/A^2`, one has `v(0)^2=-15`, so A
has pole order one and y pole order two at each infinity. Therefore

\[
L=\mathcal O_E(H),\qquad
H^0(E,L^2)=\langle1,A,A^2,y\rangle.
\]

The sections are independent and exhaust the four-dimensional space by
elliptic Riemann--Roch. This uses no identification of Z with the branch
divisor of A.

The following exact modular identity gives the correct normalized points:

\[
\frac{2e_2(t^3)t+e_1(t^3)}{S(t^3)}
\equiv\frac{27}{5}t^2(1-t^2)
\equiv\frac{27}{5}(1+\eta t+t^2+\eta t^3)\pmod R.
\tag{1}
\]

The denominator is invertible modulo R. The replay checks (1) and
`y(t)^2+3D(t^3)=0 mod R` separately. Also

\[
A=t^3,\qquad A^2\equiv\frac45+\frac{9\eta}{5}t
-\frac95t^2-\frac\eta5t^3\pmod R.
\]

In the basis `(1,t,t^2,t^3)` of Q(eta)[t]/R, restriction of the four
sections to Z therefore has matrix

\[
\begin{pmatrix}
1&0&4/5&27/5\\
0&0&9\eta/5&27\eta/5\\
0&0&-9/5&27/5\\
0&1&-\eta/5&27\eta/5
\end{pmatrix},\qquad
\det=\frac{486}{25}\eta\ne0.
\tag{2}
\]

Equivalently, vanishing of `a+bA+cA^2+dy` at all four points forces
`c+3d=0` and `-c+3d=0` from the coefficients of t and t^2. Thus c=d=0,
and then a=b=0. Since R is separable, quotient-ring vanishing is exactly
vanishing at the four marked points, including after algebraic closure.
Hence

\[
H^0(E,L^2(-Z))=0,\qquad\boxed{L^2\not\simeq\mathcal O_E(Z).}
\]

Geometrically, |2L| embeds E as an elliptic normal quartic on the cone
`X0 X2-X1^2=0`. Its four marked points are not coplanar, so cannot be
the required hyperplane section. This is a failure before node gluing,
not a failure of a particular basis of global coordinate sections.
The abstract canonical quadric constructed from the marked nodal curve
must not be confused with this |2L| cone; the equality that would identify
their component polarizations has just failed.

More generally, on a smooth quartic double cover `y^2=f_4(A)`, four finite
points with distinct A-coordinates satisfy `Z~2L` precisely when their
y-coordinates interpolate a polynomial of degree at most two in A.
This is the same hyperplane-section criterion, not a classification of
other STCI candidates.

## 3. The residual torsion is the cover's spin structure

This extraction applies to any smooth elliptic target with the stated
reduced disjoint boundaries and the **complete** `(5^4)` contact fiber.
Put `Zeta=O_E(Z)` and `M=B^*O(1)`. The boundary/Riemann--Hurwitz calculation
in the [existing audit](2026-10-30-projection-elliptic-target-incidence-audit.md)
gives `M=L Zeta` without assuming a source. The fiber f^*(1)=5Z gives
`Zeta^5=L M^3`. Thus

\[
\mathcal Z^2=L^4,\qquad
\delta:=L^2\mathcal Z^{-1}\in\operatorname{Pic}^0(E)[2].
\tag{3}
\]

One cannot cancel multiplication by two in the Picard group. Calculation
(2) proves that delta is a **nontrivial** two-torsion bundle for this target.

All local ramification indices of f are odd. Its induced theta characteristic
is

\[
\theta_f=f^*\mathcal O_{\mathbf P^1}(-1)
\otimes\mathcal O_E(R_f/2),\qquad \theta_f^2=\omega_E.
\]

Writing B_0 and B_infinity for the reduced boundary divisors gives
`R_f/2=B_0+B_infinity+2Z`. Consequently

\[
\theta_f=(LM^3)^{-1}M^2\mathcal Z^2
=\mathcal ZL^{-2}=\delta^{-1}=\delta.
\tag{4}
\]

This is the standard odd-ramification pullback of a theta characteristic:
[Eskin–Okounkov–Pandharipande, *The theta characteristic of a branched
covering*, §§1.1.1–1.1.2](https://arxiv.org/pdf/math/0312186) defines it
through half the divisor of a pulled-back differential and defines parity
as h^0 modulo two. The opening construction permits a rational target;
their subsequent torus-cover enumeration is not being applied here.

On E the trivial theta characteristic has h^0=1 and is odd; every
nontrivial degree-zero theta characteristic has h^0=0 and is even. Thus
within these hypotheses the component gate requires **odd induced spin**.
The fixed target has even spin. Equivalently, for a nonzero holomorphic
differential omega on E, `df/omega` is not a meromorphic square. Its even
local orders permit local square roots, but the global two-torsion class
prevents a global one.

## 4. Effect on the unrestricted question and stopping decision

The selected target is closed for this construction at its first Picard
gate. No residue, contact, carrier or mate computation is needed for it.
This excludes its extension through the stated smooth or cone source
criterion; it is not a theorem about all degree-eight carriers or all
characteristic-zero STCI equations.

The reusable finding is that complete contact data can determine only a
squared polarization; here the remaining ambiguity has a precise spin
interpretation. A future constructive input in this balanced elliptic
class would need trivial/odd induced spin, followed by the separate node
gluing and contact tests. Odd spin alone would not construct a carrier.
The passport has not been shown to force even spin for every cover.
There is also no reduction of arbitrary defining pairs to these reduced
elliptic covers; the nonreduced plane-pencil CI is a different object.

Do not start a new cover enumeration from this failure. No further fixed
target is recommended by this result. Reopening the balanced elliptic
construction would require a mechanism controlling the spin class and
the actual functions A,B, rather than selecting another contact partition
and hoping its untested polarization descends. A claim of unrestricted
nonexistence would require an additional arbitrary-pair reduction that
has not been established.

## 5. Verification and review status

The focused worker used exact standard-library rational arithmetic over
Q(eta) to derive (1)–(2). The lead independently rebuilt the target and
the gate in SymPy; the displayed matrix and determinant agree. The saved
script output distinguishes the passing target replay, failing Picard
gate, and deliberately unperformed later gates. Numerical approximation
was not used. This agreement is calculation evidence, not a substitute
for an independent review of its geometric implications.

A fresh `gpt-6.1-sol/high` reviewer reconstructed the full target support
and normalization boundaries, Picard matrix and hyperplane interpretation,
two-torsion and spin identities, and their scope. The reviewer inspected
the actual verifier predicates, checked the primary spin source, and
reran the exact verifier successfully with the same saved conclusions.
No material defect was found. The reviewer supports stopping this target
without starting another enumeration. The linked audit distinguishes
the passing target replay, failing gate, and unperformed later tests.
Both the focused worker and reviewer completed their assignments; neither
continued into other candidates. No canonical result has been promoted.
