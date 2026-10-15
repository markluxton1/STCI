# The second ambient obstruction is nonzero on the smooth torsion-two seed

Date: 2026-10-14. Author: `universal_root_obstruction`.
Status: **NEW EXACT ACTUAL-CHART CALCULATION; independent review in progress**.
The accepted embedded chart is an input. The accepted spectral obstruction
interpretation is an input. This note computes one new higher class,
without retesting accepted chart or conormal statements.

## 1. The hierarchy detects geometry that both first tests permit

The [universal quadratic incidence note](2026-10-14-generalization-quadratic-root-universal-incidence.md)
constructs the actual first obstruction scheme `K`, proves it is smooth
of dimension four at the seed

    f=(z²+4)u²+(z²−8)v²,

and proves that this smooth elliptic root curve has ruling-difference
line bundle of exact order two. Hence both the actual first ambient
obstruction and the accepted spectral descent condition permit this
seed. Its **second** ambient obstruction is nonzero.

The second obstruction is relevant when no independent relation has yet
appeared by normal degree four, namely when the next relation degree
`s` satisfies `s>4`. In particular this includes the accepted numerical
abstract families with `s=8` and `s=12`. At `s=4`, the second relation
changes the target; the computation below does not give an exclusion.

This is a statement about the actual ambient first-relation lifting
problem. It becomes a necessary condition for actual supported complete
intersections only within a proved actual-CI-to-root-curve bridge and its
hypotheses. No unrestricted actual CI or STCI conclusion is asserted.

## 2. Retain the full chart, base motion, and equation unit

Use the accepted exact normal chart, with

```
den = z⁴+u+(3/2)zv,
w   = (z³+v)/den,
a'  = z/den−w³,
b'  = 1/den−w⁴,
u'  = a'/2,
v'  = −3w a'+2b'.
```

Its reduced base transition is `w=z^-1`; its first normal transition is
`u'=z^-7u`, `v'=z^-7v`. Set

```
f0=(z²+4)u²+(z²−8)v²,
f1=(1+4w²)u'²+(1−8w²)v'².
```

For the equation transition factor normalized by `z^-16`, choose the
first normal unit coefficient

    L1=(−5z^-4−8z^-6)u+(−(1/8)z^-1−(11/2)z^-3)v.

The first compatible cubic corrections can be chosen as

```
G0=(z/8)u²v−(3/4)uv²+(z/8)v³,
G1=−32w u'³+48u'²v'+64w u'v'².
```

Substitution into the accepted exact chart gives the literal identity
in normal degree three

    [ z¹⁶(f1+G1) ]_3 − G0 − L1*f0 = 0.                (1)

The unit `L1` differs from the quotient preimage `h` in the first-incidence
note by `2z*epsilon`, where `epsilon=[w−z^-1]_1`. This is the first
variation of `z²w²`. Keeping this term, rather than replacing `L1` by
`h`, is necessary in normal degree four. The nonlinear base coordinate
`w` is retained in both `f1` and `G1` throughout the substitution.

Let

    R4=[ z¹⁶(f1+G1) ]_4 − L1*G0.                    (2)

The terms subtracted in (2) come from the product of the first unit and
the first local correction. Unknown second unit coefficients multiply
`f0`; unknown quartic local corrections are Cech coboundaries. Thus the
second actual class is exactly the Laurent projection of (2), modulo
those multiples and coboundaries.

## 3. One sparse Serre-dual pairing proves nonvanishing

The second target is

    H1(Z,O_Z(-12,4))
      =coker[ H1(O(-14,2)) --f0--> H1(O(-12,4)) ],

with dimensions `39 -> 55 -> 16`. Use powers `z^-11,...,z^-1` in the
middle group, and `z^-13,...,z^-1` in the source. The multiplication map
is injective, since its kernel is `H0(Z,O_Z(-12,4))=0`.

Write `R4=sum_(i=0)^4 r_i(z) u^(4-i)v^i`. Only four coefficients are
needed for a nonzero dual pairing:

```
                  coefficient z^-3     coefficient z^-1
r1  (u³v)              5/8                    0
r3  (uv³)              9/8                  −3/32.
```

These coefficients follow from the exact substitution in (2). The
companion script also records every other quartic coefficient, so this
is a bounded computation with full retained output.

Put `a=z²+4`, `c=z²−8` and define

    lambda(r)=coefficient_z^-1[−c*r1+a*r3].           (3)

The polynomial dual vector is `(0,−c,0,a,0)`. It annihilates every
multiple of `f0` by a binary quadratic: on the odd source monomial `uv`
the coefficient is `a*(−c)+c*a=0`, while the other two source monomials
have only even target powers. The degree of each dual polynomial is two,
within the allowed degree ten. Therefore it also annihilates the full
Cech image of `H1(O(-14,2))`. It ignores all removed Cech coboundaries.

Using the displayed four coefficients gives

    lambda(R4)=−5/8+9/8−3/8=1/8 != 0.              (4)

Hence the actual second ambient class is nonzero. The complete rational
matrix calculation independently records multiplication rank `39` and
augmented rank `40`; the sparse identity (3)--(4) is already a proof.

## 4. This is a universal higher-obstruction mechanism on K

The seed calculation has a family-level consequence; it need not lead
to a list of further seeds. On the basepoint-free universal first
compatibility scheme `K`, the first compatible Cartier ideal is unique:
its possible differences lie in `H0(Z,O_Z(-5,3))`, which vanishes on
this entire open. The first corrections therefore glue, up to their
equation units, into the universal first lift.

Consequently there is a canonical second obstruction section over `K`.
Its rank-sixteen vector bundle is the relative version of

    coker[ H1(O(-14,2)) --f--> H1(O(-12,4)) ].

More precisely, on projective coefficient space the exact sequence is

    H1(O(-14,2)) tensor O_K(-1)
       --f--> H1(O(-12,4)) tensor O_K -> Q2 -> 0,

and the obstruction section has values in `Q2 tensor O_K(1)`.
The universal equation contributes the coefficient-space `O(1)` factor.
The multiplication map has constant rank thirty-nine: `pi_*O_Z(4)` is
globally generated of rank two and degree six, so twisting it by
`O(-12)` has no sections. Thus the cokernel is genuinely a vector
bundle, without deleting exceptional coefficient strata inside the
basepoint-free open.

The first class defines `K`; the second class is a section on `K`, not
another unrelated scalar test on the original parameter space. Its
nonzero value (4) proves that it is not identically zero on the
four-dimensional component through the smooth seed. Nonvanishing is
open, so a nonempty open subset of that component, and hence its
generic point, fails the second lifting step. The second zero locus on
that component remains to be determined. A rank-sixteen target on a
four-dimensional component does not by itself prove that zero locus is
empty, and no such claim is made.

This gives the structural next problem: describe the common zero scheme
of the actual higher-obstruction sections on `K`, intersected with the
spectral torsion loci, while retaining all equation-unit and second
relation extensions. The present computation proves that the hierarchy
adds a genuine obstruction after both the first class and Picard torsion
have passed. No additional seed or carrier-degree enumeration is needed
for that conclusion.

## 5. Exact artifacts and boundaries

- [Standard-library exact verifier](../computations/generalization_quadratic_root_seed_second_obstruction.py).
- [Full rational output and sparse dual certificate](../computations/generalization_quadratic_root_seed_second_obstruction.json).

Run with `python3 research/computations/generalization_quadratic_root_seed_second_obstruction.py`.
The verifier computes the accepted chart to normal degree four, verifies
(1), retains both the equation unit and nonlinear base motion in (2),
checks the full multiplication rank, and proves the simple pairing (4)
exactly. It does not sample, use floating point, or invoke a large CAS.

The seed has not been lifted through second exceptional order, so it
supplies no formal or projective CI construction. The result excludes
this first-relation seed from a first-principal-ideal lift through normal
degree four when `s>4`; it does not exclude every smooth root divisor,
every torsion order, or unrestricted `C0`. No commit or memory update
was made.
