# Independent audit: the full tropical conductor boundary

Date: 2026-10-31. Reviewer: `tropical_conductor_audit`, independently of
the proposal author. Scope: Sections 1–5, equations (1)–(7), and the
geometric and epistemic limitations of
[the conductor proposal](2026-10-31-tropical-conductor.md).
Outcome: **no material mathematical correction required; independently
reviewed provisional deductions, with no canonical promotion**.

The exact input is a proper homogeneous CI `Z=V(F_a,G_b)` with sole
reduced support `C=[s^4:s^3t:st^3:t^4]` over an algebraically closed
field, together with its full saturated finite modification `rho:W→Z`
and rank-`m=ab/4` projection `pi:W→P1`. The construction and endpoint
algebra identifications are the reviewed input of
[the descent note](2026-10-31-tropical-descent.md) and
[its audit](2026-10-31-tropical-descent-audit.md). This audit checks the
duality and conductor deductions from those objects; it does not reopen
the independent characteristic-zero movement proof or inherited formal
algebraization results. The conductor assertions work in every
characteristic. Only the additional assertion `e=deg(pi_*O_W)>0` uses
the descent note's characteristic-zero input.

## 1. Arbitrary nonreduced finite modifications

At an endpoint use the actual target parameter, t at zero and z at
infinity. Write `R=k[[t]]` and `K=k((t))` in the following argument.
The completed rings `A⊂B` are finite free R-modules of the same rank,
their quotient has finite length, and
`Q=A⊗_R K=B⊗_R K` is their common generic Artin algebra. A is a
one-dimensional Gorenstein local ring because Z is a CI. None of this
requires B to be Gorenstein or Q to be reduced.

Any A-linear map `f:B→A` extends over K to a Q-linear endomorphism of
Q, hence is multiplication by `q=f(1)∈A`. Conversely multiplication by
q defines such a map exactly when `qB⊂A`. This identifies

`Hom_A(B,A) = (A:_Q B) = c`

as B-modules, where c is the actual conductor. Its compatibility with
the B-action follows directly from multiplication in Q. This argument
does not use a field-valued generic point or a normalization theorem.

For the global assertion, finite duality between the CM curves gives
`omega_W ≅ Hom_Z(rho_*O_W,omega_Z)`, interpreted as an O_W-module.
Since `omega_Z=O_Z(a+b−4)` is invertible, this is
`c⊗rho^*omega_Z`. The four specified projective sections of
`pi^*O(4)` have no common zero, including both endpoints, so
`rho^*O_Z(1)=pi^*O(4)`. Finally finite duality over P1 identifies
`pi_*omega_W=Bcal^vee⊗O(−2)` as Bcal-modules. Therefore

`pi_*c ≅ Bcal^vee⊗O(14−4a−4b) = Bcal^vee⊗O(−L)`.

The twist and its sign check. The result identifies a canonical module
with an ideal after the stated twist; it does not turn that module into
an invertible sheaf. In particular it provides no automatic Gorenstein
property for W.

## 2. Frobenius lattice and the complete boundary pairing

Since R is a DVR and A is finite free and Gorenstein, its relative
canonical module `Hom_R(A,R)` is free of rank one as an A-module.
Choose a generator lambda. The map
`a↦(a'↦lambda(aa'))` is consequently an isomorphism from A to its
R-dual. Lambda here is a chosen Frobenius functional, **not** the
algebra trace, which need not be nondegenerate on a nonreduced algebra.
Its K-linear extension to Q is well-defined and has nondegenerate
product pairing. Thus the dual lattice of A inside Q is exactly A.

For a lattice M in Q write
`M^#={q∈Q : lambda(qM)⊂R}`. If `q∈B^#`, then `A⊂B` gives
`q∈A^#=A`. For every b in B and a in A, `ba∈B`, so
`lambda(qba)∈R`, proving `qb∈A^#=A`. Hence `B^#=c`.
Conversely c plainly satisfies this condition. Dualizing an inclusion
of free DVR lattices preserves its index, so

`length_R(A/c)=length_R(B/A)=delta`,
`length_R(B/c)=2delta`.

This also verifies the proposed Ext explanation: B is maximal CM as an
A-module, and higher Ext into the canonical module A vanishes. No
Gorenstein hypothesis on B enters.

On `D=B/c`, define `epsilon(b mod c)` to be the coefficient of t^(-1)
in lambda(b). It is well-defined because `lambda(c)⊂R`. To check the
radical, suppose epsilon(bb') is zero for every b' in B. Applying the
same condition to `t^j b'`, for each `j≥0`, detects the coefficient
of t^(-1−j) in lambda(bb'). Thus **all** negative coefficients vanish,
`lambda(bB)⊂R`, and `b∈B^#=c`. This proves perfection of the entire
k-pairing on D, and therefore the Artinian Gorenstein assertion.

The image `E=A/c` is a unital subalgebra, epsilon vanishes on it, and
multiplication of two E-elements stays in E. Hence E is isotropic.
Its dimension is half that of D, giving `E=E^perp` in every
characteristic, including characteristic two. It is not being treated
as an ideal of D. Finally the inverse image of E in B is literally A:
if b has the same residue as a in A, then `b−a∈c⊂A`.
Consequently `A=B×_D E`. When delta is zero these boundary statements
have the empty-scheme interpretation specified in the proposal.

## 3. Independent reconstruction of the non-Gorenstein control

For `A=R[x,y]/(x²+y²,xy)`, the basis `1,x,y,y²` has multiplication
`x²=−y²`, `xy=0`, and `y³=0`. Under `x=t³U`, `y=t⁴V`, the
generic relations give `U²=−t²V²`, `UV=0`, and `V³=0`.
The proposed quotient B has the free R-basis `1,U,V,V²` with precisely
these multiplication rules. They define a consistent associative
algebra, so there are no further basis relations. It agrees with A
after inverting t and has no t-torsion. This verifies that it is the
full saturated contraction, rather than a quotient obtained by
individually dividing equations.

In this basis the A-lattice is exactly

`R ⊕ Rt³U ⊕ Rt⁴V ⊕ Rt⁸V²`.

The only omitted generator product, `x²=−y²`, supplies no smaller
lattice exponent. Thus delta is `0+3+4+8=15`.

For `q=a+bU+cV+dV²` already in A, multiplication by U requires
`a∈t³R` and `b∈t⁶R`; multiplication by V requires
`a∈t⁴R` and `c∈t⁸R`; multiplication by V² requires
`a∈t⁸R`. Together with membership in A these are exactly the
coefficient bounds `(8,6,8,8)`. Therefore

`c=Rt⁸ ⊕ Rt⁶U ⊕ Rt⁸V ⊕ Rt⁸V² = (t⁸,t⁶U)B`,
`length(D)=8+6+8+8=30`.

Modulo t the maximal ideal of B has socle spanned by U and V²;
the special fiber has type two. Since t is regular, this proves B
is not Gorenstein. For D, annihilation by t first restricts a possible
socle element to the span of `t⁷,t⁵U,t⁷V,t⁷V²`.
Multiplication by U excludes `t⁵U`, and multiplication by V excludes
`t⁷` and `t⁷V`. The remaining socle is exactly `k t⁷V²`.
The coefficient functional on this monomial kills E, whose basis has
8 constant, 3 U, and 4 V terms. A nonzero functional on the socle of
an Artinian local Gorenstein algebra has perfect product pairing,
which independently verifies the claimed explicit functional.
All signs and coefficients remain valid in characteristic two.

Geometrically, the upstairs transverse fiber changes from a length-four
CI to a length-four punctual scheme with a two-dimensional socle. The
30-dimensional conductor boundary still has its own perfect pairing
and the 15-dimensional subalgebra of descending functions. Thus local
Gorenstein contraction does not force the saturated source to be
Gorenstein. This example is local; no homogeneous projective realization
on C, and no counterexample to the movement assertion, follows from it.

## 4. Source scope, numerical meaning and disposition

The checked finite-map input is [Stacks, Section 49.2, especially its
finite-map definition and Lemma 49.2.12](https://stacks.math.columbia.edu/tag/0BUK).
It uses Hom for finite maps and does not impose reducedness.
[Elias, Section 2, Lemma 2.1 and Proposition 2.2](https://arxiv.org/pdf/1309.5193)
are stated for one-dimensional CM local rings. Together they give the
canonical-ideal quotient formulation used as background here; the
paper's later formulas about reduced curve normalization are not
inputs to this audit.

I checked [Battistella–Carocci, Section 2.3.1, Proposition 2.6 and
Corollary 2.7](https://arxiv.org/pdf/2008.13506): their Noether formula
assumes both curves Gorenstein. The proposal correctly keeps that
hypothesis separate from the present source W; the local proof above
provides the stronger module statement actually needed. Their global
convention permits nonreduced S1 curves.
[Ferrand's conductor pullback and pinching framework](https://www.numdam.org/article/BSMF_2003__131_4_553_0.pdf)
works for general ring fiber products, with no reducedness requirement;
the inverse-image argument above already proves the specific pullback.

Taking degrees of the verified Bcal-module identity gives
`length(Bcal/pi_*c)=2e+mL`. Its left side is the sum of the two
boundary lengths, namely `2(delta0+deltaInfinity)`. Hence this is
exactly twice the existing descent genus identity, not an independent
numerical obstruction.

The retained geometric datum is the complete finite conductor scheme
in W, its map to the conductor scheme in Z, and its compatible
self-orthogonal algebra of descending functions. This is stronger data
than a length, but its existence is a classical duality consequence
of the hypothesized finite modification. No incompatibility with
positive embedded movement or with an actual homogeneous two-equation
image has been established. Carrier-normalization conductor results
and normal-filtration socle results involve different objects and are
not silently transferred to W.

No required correction or material unresolved local-duality condition
remains in the reviewed proposal. The global homogeneous-realization
bridge remains open. No computer algebra, inherited certificate rerun,
whole-repository audit, literature-priority claim, or canonical
promotion was performed.
