# Independent review of the actual second obstruction at the smooth seed

Date: 2026-10-14. Author: `geometric_locus`.

Status: **THE NEW SECOND CLASS, SPARSE NONZERO PAIRING, AND STATED
FAMILY CONSEQUENCE PASS INDEPENDENT REVIEW.** The full embedded chart is
accepted input. No accepted chart or spectral theorem audit is repeated.
The calculation concerns the first principal relation through normal
degree four, so its stated CI application requires `s>4` and a proved
actual-CI-to-root-curve bridge with the relevant hypotheses.

Reviewed files:

- `2026-10-14-generalization-quadratic-root-second-obstruction.md`;
- `../computations/generalization_quadratic_root_seed_second_obstruction.py`;
- the accepted exact chart as recorded in
  `../computations/generalization_moving_first_relation_operator.py`.

The nonzero scalar below was derived independently by hand from the full
chart. It does not rely on the parent script's row reduction or on its
larger dual certificate.

## 1. The cubic patch and equation unit are consistent

Use the accepted exact chart

    den=z^4+u+(3/2)zv,
    w=(z^3+v)/den,
    a'=z/den-w^3, b'=1/den-w^4,
    u'=a'/2, v'=-3w a'+2b'.

For the seed put

    f0=(z^2+4)u^2+(z^2-8)v^2,
    f1=(1+4w^2)u'^2+(1-8w^2)v'^2.

The first base displacement is

    epsilon=[w-z^-1]_1=-z^-5 u-(1/2)z^-4 v.

Thus `beta=2z epsilon=-2z^-4 u-z^-3 v` and the proposed equation unit
is exactly `L1=h0+beta`, with `h0` the quotient preimage in the first
independent review. In particular, the unit has retained the base motion.

At normal degree three, the accepted derivation and the base factor give

    [z^16 f1]_3=Df0+beta f0.

The leading linear normal transition gives

    [z^16 G1]_3=-32z^-6 u^3+48z^-5 u^2v+64z^-6 uv^2,

for

    G1=-32w u'^3+48u'^2v'+64w u'v'^2.

The previously checked exact identity for `Df0-f0 h0` then proves

    [z^16(f1+G1)]_3-G0-L1 f0=0,

with

    G0=(z/8)u^2v-(3/4)uv^2+(z/8)v^3.

This independently verifies the first patch identity, including its unit.

For a quartic local correction and a second unit `L2`, the degree-four
gluing equation contains `L1 G0+L2 f0`. Therefore the proposed discrepancy

    R4=[z^16(f1+G1)]_4-L1 G0

has the correct sign and all required contributions. The unknown `L2`
is precisely a multiple of `f0` in the quotient target. No additional
`L1^2 f0` term is forced: the free second coefficient belongs to the unit
`1+L1+L2`, and would absorb such a reparameterization of the unit.

## 2. Independent sparse quartic calculation

Only the coefficients of `u^3v` and `uv^3` at powers `z^-3` and `z^-1`
are needed. Write `Uj=[u']_j`. The first two layers are

    U1=z^-7 u,
    U2=-(5/2)z^-11 u^2-3z^-10 uv-(3/8)z^-9 v^2.

To obtain the pure `v^3` coefficient in `U3`, set `u=0` and
`t=z^-3 v`. The full chart gives the exact rational expression

    u'=(z^-3/2)*((1+(3/2)t)^2-(1+t)^3)/(1+(3/2)t)^3.

Its numerator is `-(3/4)t^2-t^3`. Expanding the denominator to the
needed order gives

    [u']_(v^3)=(19/16)z^-12 v^3.

Consequently the `uv^3,z^-3` coefficient of `z^16[u'^2]_4` is

    2*(19/16)+2*(-3)*(-3/8)=37/8.              (1)

No other normalized term contributes to the four required coefficients.
This can be checked without expanding their full polynomials. Give
`z,u,v` weights `1,0,-1`. At normal degree `n`, the weights of `w,u',v'`
are respectively `-1-4n,-3-4n,-4-4n`. In normal degree four, the weights
of the four terms of `z^16 f1` are

    u'^2: -6,    4w^2u'^2: -8,
    v'^2: -8,   -8w^2v'^2: -10.

For `u^3v` these allow powers at most `z^-5`; for `uv^3` only the first
term reaches `z^-3`, as computed in (1), and none reaches `z^-1`.
The three normalized `G1` terms have weights `-10,-10,-12`, so they
cannot contribute to these four coefficients either.

Finally multiply the explicit `L1` and `G0`. Their contributions give

```
                         z^-3 coefficient    z^-1 coefficient
R4: u^3v                      5/8                   0
R4: uv^3          37/8-(-5/8+33/8)=9/8          -3/32.
```

This derives all four coefficients in the main note directly from the
full chart and the first patch data.

## 3. The scalar is a valid quotient obstruction

The second target is the Cech quotient

    H1(O(-14,2)) --f0--> H1(O(-12,4)),

with target powers `z^-11,...,z^-1`. Its Serre dual has five polynomial
entries of degree at most ten. Let `a=z^2+4`, `c=z^2-8`. The vector

    q=(0,-c,0,a,0)

belongs to this dual space and annihilates multiplication by `f0`.
Indeed the odd source monomial `uv` gives `-ac+ca=0`, while the two
even source monomials pair with zero entries. Thus

    lambda(R)=coefficient_z^-1(-c R_u3v+a R_uv3)

is a well-defined functional on the cokernel. Its degree-two entries
also annihilate removed Cech powers: powers below `-11` cannot be
shifted to `-1`, and nonnegative powers cannot contribute.

The four checked coefficients give

    lambda(R4)=-(5/8)+(9/8)+4*(-3/32)=1/8 != 0.

This proves nonvanishing of the actual second ambient class. The
multiplication map has rank thirty-nine by the constant-rank argument
below; adjoining a single vector with this nonzero pairing therefore
raises the rank to forty. A full row reduction is not needed for this
conclusion.

## 4. The stated family consequence is valid

On the entire basepoint-free open, the possible difference between two
first Cartier lifts is a section of `O_Z(-5,3)`. The first review proved
that its `H0` vanishes everywhere there, using the globally generated
rank-two pushforward of degree four. Thus the first lift is unique as
an ideal, even though its local equations can differ by units. The
first compatibility scheme is the scheme-theoretic zero locus of the
first obstruction, so local first lifts exist over it and their
uniqueness glues them. This also applies to its nonreduced parameter
structure by the relative cohomology/base-change statement with zero
`H0` and constant-rank presentations.

The second multiplication map has constant rank on this same open.
The finite-flat pushforward has an exact sequence

    0 -> O(-2)^3 -> O^5 -> E4=pi_*O_Z(0,4) -> 0.

The bundle `E4` is globally generated, rank two, degree six. Its
splitting degrees lie between zero and six; after twisting by `O(-12)`
neither has sections. This proves injectivity of the thirty-nine-column
second multiplication map for every basepoint-free coefficient point.

Over projective coefficient space, the universal root equation has
coefficient twist `O(1)`. Hence the natural exact presentation is

    39 O_K(-1) --f--> 55 O_K -> Q2 -> 0,

with `Q2` locally free of rank sixteen. The normalized discrepancy
scales linearly with the universal equation. Its canonical second
obstruction is accordingly a section of `Q2 tensor O_K(1)`, as stated
in the main note. Uniqueness of the first ideal ensures that local
choices of first equations and units give the same quotient section.

At the smooth seed this section is nonzero. The first compatibility
scheme is smooth of dimension four there, so there is a unique
irreducible component through that point. The section is not identically
zero on that component; its nonvanishing locus is a nonempty open
subset and contains the generic point. This proves generic failure
of the second lifting step on that component. It does not prove that
the second zero locus is empty and does not assert torsion throughout
the component.

For `s>4`, no independent second relation has entered by this normal
degree, so the first-principal-ideal obstruction is relevant to the
stated bridge lane. For `s=4` the target can change, and no exclusion
was proved. The result leaves higher zero loci, their intersections
with torsion strata, later ambient extensions, and actual polynomial
realization unresolved.

No commit or memory update was made.
