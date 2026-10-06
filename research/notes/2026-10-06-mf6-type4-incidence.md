# Remaining e=0 type (d2,d3)=(4,5): exact triple/quartic incidence

Date: 2026-10-06. Characteristic zero; monomial quartic C0. Status:
**proved parameter reduction; exact exploratory quartic and cubic data;
exceptional loci remain open.** No exclusion of this complete defect type
is claimed. The established low-defect and type-three exclusions are in
`2026-10-05-mf6-further-audit.md`, independently audited in
`2026-10-06-mf6-type3-independent-audit.md`.

## Every possible degree-four triple

The two pure constant quotient directions fail flatness for d2=4: their
killing section has an additional degree-two factor common to delta and
gamma. Thus normalize every possible mixed constant quotient to
`m=U+V,ell=V`, using the torus as in the type-three proof.

Multiplication of the exact h2 cocycle by a section delta of O(4) must
kill both Laurent coordinates of `H1(O(-3))`. Its complete kernel is

    delta=A(z^2+2z)+B(z^3-4z)+C(z^4+8z+16),
    gamma_U=3[A+B(z-2)+C(z^2-2z+4)]/8,
    gamma_V=6Aw+6B(1-2w)+48Cw^2.

If C=0, delta and gamma are the degree-three triple data multiplied by
the homogeneous linear section `A+B(z-2)`. That section has a zero,
including infinity if B=0, so the proposed triple is not flat.

If C!=0, normalize C=1 and write

    delta=A(z^2+2z)+B(z^3-4z)+z^4+8z+16,
    R=A+B(z-2)+z^2-2z+4, gamma_U=3R/8.

The elementary identity `delta=z(z+2)R+16` gives the exact resultant
`Res_z(delta,R)=256`, independent of A,B. Thus
there is no finite common zero. At infinity delta_V has value one, so
every point `(A,B)` gives a flat embedded triple. Its D2 divisor is the
degree-four zero divisor of delta and has no infinity component. This
exhausts the triple parameter space rather than selecting a generic chart.

## Complete quartic equation and its cubic-pole constraint

Let `F=sum c_i F_i` range over the complete eight-dimensional quartic
space with first normal form `h(U+V)`; the basis is derived from the
18-dimensional `I_C(4)` by the preceding verifiers. Write

    Q=coeff_y^2 F(m=0,y),
    E=coeff_my F(m,y), K=coeff_y^3 F(m,y).

Containing the specified triple requires exactly the quadratic identity

    delta Q+(3/8)R h=0.

The resulting coefficient matrix is 13 by 8, affine in A,B. It has rank
seven over Q(A,B), so its generic solution space is a unique quartic up
to scalar. The exact polynomial kernel vector, full coefficient matrix,
and the resulting polynomials S,T are preserved in
`research/scratch/mf6_type4_incidence.json`. The script
`research/scratch/explore_mf6_type4.py` derives these data using
fraction-free polynomial-domain operations and checks every kernel
equation exactly. Rank-drop parameter loci have not been classified;
the generic kernel must not be called the complete quartic family there.

Since delta and R are coprime, the quadratic identity forces `h=delta S`.
S is a section of O(5). The formal cubic coefficient of the quartic is

    f2=3R/(8delta),
    f3=-(3R E+8delta K)/(8delta^2 S)=-T/(8delta^2 S).

At every finite point the third-piece DVR lattice lemma from the preceding
note gives the exact coefficientwise formula

    ord(D3-D2)=max(0,ord S-ord T).

This also holds at finite multiple roots of delta, because R is a unit
there and its pole order in f2 is exactly ord delta. The target d3=5
permits only one total unit of this excess. Therefore every candidate
requires that all but at most one of the finite zeros of S cancel in T.
An additional infinity contribution must be calculated with the moving
second frame whenever S has an infinity zero. It cannot be guessed by
the affine polynomial degrees.

At A=B=0 the matrix has rank seven and its S polynomial, up to scale, is

    41z^5+28z^4+56z^3+176z^2-80z+704.

Its gcd with T is exactly one. Thus the local cubic calculation forces
at least five excess units and d3>=9, excluding this parameter. More
generally, rank seven, a nonzero leading coefficient of S, and coprimality
of S,T are open conditions. This exact point proves that the generic
degree-four triple/quartic incidence is excluded; the surviving possible
parameters lie in a proper algebraic exceptional locus. Additional exact
sample parameters also have gcd one but do not constitute a universal
exclusion.

## Continuation and failed computational shortcuts

The required next calculation is the rank-drop boundary together with
the subresultant conditions `deg gcd(S,T)>=deg S-1`, followed by the direct
infinity chart. Both boundaries are necessary: a generic nullspace vector
does not identify every special solution, and affine loss of degree in S
can hide an infinity pole.

Run

    /private/tmp/stci-cas-venv/bin/python research/scratch/explore_mf6_type4.py

to reconstruct the exact generic incidence. The optional `--resultant`
attempt computes `Res_z(S,T)` as a polynomial in A,B; it may be expensive
and is not required to reproduce the proved reductions. Initial direct
symbolic `Matrix.rank()/nullspace()` operations expanded rational
expressions unnecessarily; polynomial-domain `DomainMatrix.nullspace()`
gave the same exact kernel rapidly. The full generic resultant attempt
was interrupted after several minutes of coefficient growth; no resultant
answer is recorded or claimed. The exact S,T inputs are preserved. This
distinction affects computation cost, not the scope of the result.

`research/scratch/mf6_type4_resultant.m2` preserves the same exact S,T input
for an alternative Macaulay2 resultant attempt. That attempt was also
interrupted without a returned result. There is no pending computation
and no resultant output to treat as evidence. A more useful next attempt
may compute the high-gcd subresultant ideal directly, instead of expanding
the full degree-zero resultant.

The type `(4,5)` still contributes the nonregular coarse pole lengths
3 and 4. The e=1 types `(0,4),(1,3),(2,2)` still contribute pole lengths
4, 5, and 6 as detailed in the preceding note.
