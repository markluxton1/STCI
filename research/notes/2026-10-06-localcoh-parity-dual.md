# A corrected polynomial-dual exclusion for the normalized parity family

Date: 2026-10-06. Status: **PROVED BY AN EXACT POLYNOMIAL IDENTITY** over QQ,
hence over every characteristic-zero extension. This is a family exclusion
inside the finite quartic local-cohomology problem for C0. It does not
resolve the full quartic incidence or the general projective STCI question.

## The family and statement

In the balanced normal frame, take the degree2 normal-dual direction

    nu=(1+t²,c t),

with pure cubic top symbol coefficient h=1. For c≠0 its homogeneous pair
(s²+t²,c st) is coprime and has primitive degree2. The calculation also
includes c=0 as a boundary specialization. The unique nonzero top-lift line
has h constant: the top-image obstruction to h=t has a nonzero constant
component, independent of c. This is checked uniformly by the verifier.

Let a(c,lambda) be the chosen polynomial top lift plus an arbitrary multiple
lambda of the unique T3[-7] section. Every ancestor with this normalized top
symbol has this form. Let L(a) be the74×18 actual quartic multiplication
matrix from the exact tensor, whose target columns are e72 and e73.

There is a polynomial row vector n(c,lambda) over QQ[c,lambda] such that

    n(c,lambda)^T L(a(c,lambda)) = 0,
    n(c,lambda)^T e72 = 1.

Consequently **no quartic multiplier produces u at any point of this
family**, even over an algebraic closure. In particular this family has no
common quartic ancestor for u,v. The assertion includes every lower T3
coefficient and every c; it has no exceptional parameter locus. A nonzero
scalar multiple of the top coefficient is absorbed by scaling the ancestor
and the multiplier, so the h=1 normalization loses no nonzero top lift.

The same saved dual has n^T e73 equal to a linear polynomial in c. The one
dual therefore proves the common-ancestor exclusion through u; it should
not be represented as separately excluding v at that linear polynomial's
root. Separate one-target Groebner runs in the companion research lane
returned the unit ideal for both targets, but that additional v assertion
is not needed for this certificate.

## Exact certificate and verification

The complete polynomial coefficients are saved in
`../computations/localcoh-incidence-parity-dual-2026-10-06.json`. There are24
terms in the30 ancestor-coordinate polynomials and173 terms in the74 dual
entries. Terms are stored as rational coefficients with their c and lambda
exponents, so the identity is portable and inspectable.

Run from the repository root:

    python3 research/computations/localcoh-incidence-parity-dual-2026-10-06.py

This uses only Python's standard library. It checks coordinate-file hashes,
source-basis agreement, the top symbol and its h=t obstruction, contracts
all540 actual quartic products, multiplies the polynomial dual, and verifies
all18 zero identities plus the constant1 target identity. It contains no
Groebner call and no sampling.

The exact discovery/reproduction script is
`../computations/localcoh-incidence-parity-dual-2026-10-06.m2`. Its polynomial
ring has only c,lambda. For the74×18 matrix L it computes the kernel of
transpose L, evaluates its generators on e72, verifies that this evaluated
ideal is the unit ideal, and lifts1 through those generators. The resulting
polynomial dual is also saved in a readable text file with the same basename.
This is a small polynomial module calculation, rather than the unfinished
66-variable full bilinear Groebner attempt. The independent Python identity
check is the mathematical certificate.

## Extension to the nondegenerate unnormalized parity family

The curve has the ambient torus automorphism

    (x,y,z,w) -> (x,l y,l³ z,l⁴ w),     l≠0.

For the balanced normal coordinates U=w-(3/2)tz+(1/2)t⁴ and V=z-t³,
these coordinates scale by l⁴ and l³. Thus the geometric pushforward of a
normal-dual direction (p(t),r(t)) is

    (l⁴ p(t/l), l³ r(t/l)),

up to the immaterial common nonzero scalar used to describe its projective
direction. For p=a0+a2 t² and r=b1 t with a0 a2≠0, divide this pair by
l²a2 and choose l²=a2/a0. The result is

    (1+t²,(b1/a2)t).

Such l exists over an algebraically closed characteristic-zero field. The
pure-top coefficient h remains constant up to a nonzero scalar. Both target
classes are torus eigenvectors (their pullback factors are l^-7 and l^-5),
so existence of an ancestor is preserved up to nonzero target and multiplier
scalings. Therefore the normalized identity excludes the whole primitive
parity family with a0 a2 b1≠0. Cases with a0 a2=0 require separate handling
and are not obtained by this normalization argument.

## Audit provenance and limits

The earlier saved parity monomial-functional script used only the first row
of `basis(4,I)` as if it were the quartic basis. In Macaulay2 that row records
coefficients of one ideal generator, so those products had the wrong degree.
Its asserted vanishing of degree17 coefficients was vacuous. The present
certificate is a corrected proof: it uses the tensor whose quartic columns
sum all four ideal-generator contributions and whose full product span has
exact dimension74=dim E3[-3]. The older faulty script is not part of this
proof.

Validation on Oct6: the complete actual tensor and basis regenerated
byte-identically; Macaulay2 1.26.06 reran the two-variable module calculation;
the standard-library Python verifier checked the polynomial identity. The
remaining degree0/1/2 direction strata and the complete finite quartic
incidence remain separate research tasks.
