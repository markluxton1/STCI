# Independent audit of the twenty-five global second-obstruction tests

Date: 2026-10-15. Author: `geometric_locus`.

Status: **THE GLOBAL COMPRESSION, UNIVERSAL MODEL ALGORITHM, AND
HOMOGENEOUS SMOOTHNESS CRITERION PASS INDEPENDENT REVIEW.** Accepted first and second obstruction
constructions are inputs. No accepted seed computation, verifier, or
profile calculation is repeated. This audit uses bundle duality,
Laplace identities, and a local double-cover calculation.

Companion note:
`2026-10-15-generalization-quadratic-root-global-second-dual-compression.md`.
The final companion note and
`../computations/generalization_quadratic_root_global_second_model.py`
were read after this mathematical audit was drafted. Their algorithm
was compared with the proof; no old verifier, seed test, or CAS was run.

## 1. The correct dual bundle on the whole basepoint-free locus

Fix a homogeneous basepoint-free triple `a,b,c` of degree two on `P1`.
Let `f=a u^2+b uv+c v^2` and consider

              [ a b c 0 0 ]
    T_f =     [ 0 a b c 0 ] : O^5 -> O(2)^3.
              [ 0 0 a b c ]

At every base point this is the transpose of multiplication by the
nonzero binary quadratic `f` from binary quadratics to binary quartics.
Multiplication by a nonzero polynomial is injective, so the fiber rank
is three everywhere. Therefore

    0 -> W -> O^5 -> O(2)^3 -> 0

is exact with `W` a rank-two vector bundle and `det W=O(-6)`.
Neither smoothness nor reducedness of the root divisor is needed.

The second Cech target has quartic coefficients and powers
`z^-11,...,z^-1`. Its dual consists of five polynomials of degree at
most ten. An element annihilates multiplication by `f` exactly when

    a q0+b q1+c q2=0,
    a q1+b q2+c q3=0,
    a q2+b q3+c q4=0.

Thus the full sixteen-dimensional dual obstruction space is
`H0(P1,W(10))`, with the monomial-dual pairing given by the coefficient
of `z^-1` in `sum q_i r_i`. There are no binomial factors in these
formulas for the specified coefficient bases.

## 2. Rank-two duality supplies a global generating presentation

For a rank-two bundle, the exterior pairing gives a canonical
isomorphism

    W^* = W tensor (det W)^-1 = W(6).

Dualizing the exact sequence in Section 1 and using this isomorphism
gives

    0 -> O(-2)^3 -> O^5 -> W(6) -> 0.

Twisting by `O(4)` gives

    0 -> O(2)^3 -> O(4)^5 -> W(10) -> 0.              (1)

Since `H1(P1,O(2))=0`, global sections of (1) are surjective onto
`H0(W(10))`. In particular the twenty-five sections obtained from the
five displayed generators and the five degree-four base monomials
span the entire dual obstruction space. The kernel on global sections
has dimension nine and the target has dimension `25-9=16`.

This proves spanning uniformly; no splitting choice, minor
localization, or denominator is used. It therefore includes splitting
jumps, repeated direction factors, singular roots, and nonreduced
roots, subject only to the basepoint-free hypothesis.

## 3. The signed complementary minors give those five generators

Index rows and columns of a skew five-by-five matrix `K` by
`0,...,4`. For `i<j`, put

    K_ij=(-1)^(i+j+1) det(T_f with columns i,j omitted),
    K_ji=-K_ij, K_ii=0.                              (2)

Every nonzero entry is a homogeneous degree-six base polynomial and a
homogeneous cubic in the equation coefficients. The Laplace expansion
of a four-by-four determinant with one repeated row gives `T_f K=0`.
Thus each column is a section of `W(6)`.

These are exactly the five generators in the dual presentation, up
to the harmless common sign from choosing the determinant orientation.
Indeed the complementary-minor bivector is the exterior dual of the
three rows of `T_f`; contraction identifies the quotient of `O^5`
by the transpose image with `W tensor (det W)^-1`. At a local frame
where `T_f=[I3 | 0]`, formula (2) has `K_34=1`, `K_43=-1`, and all
other entries zero. It is the required nondegenerate rank-two
alternating pairing on the kernel. Change of frames proves the
identification everywhere.

Formula (2), together with skew symmetry, is necessary: assigning
the same complementary-minor sign to both `K_ij` and `K_ji` would
generally destroy the kernel identity. An overall common sign, or
using rows in place of columns with the corresponding sign, does not
change the zero tests.

On the affine base chart, the twenty-five full dual generators are

    z^k K_column_i, 0<=i<=4, 0<=k<=4.

Homogeneously, `z^k` means the basis
`Z1^k Z0^(4-k)` of `H0(O(4))`; consequently the construction includes
base infinity.

## 4. Exact equivalence with the second class and parameter degrees

Let `R4=sum r_i(z)u^(4-i)v^i` be the actual second discrepancy after
retaining the accepted first cubic correction and equation unit.
Its second class vanishes if and only if all twenty-five scalars

    coefficient_z^-1[ z^k sum_j K_ji r_j ]

vanish. One direction follows because every displayed vector
annihilates multiplication and coboundaries. The converse follows
from the spanning theorem of Section 2 and nondegeneracy of the
finite-dimensional Cech/Serre pairing. This removes the thirty-nine
unknown quartic unit coefficients without replacing the quotient
by a smaller test space.

On projective coefficient space, each `K` entry has coefficient degree
three. Thus there is a fiberwise surjective bundle map

    25 O(-3) -> Q2^*.

Pairing with the accepted canonical section in `Q2(1)` produces
twenty-five sections of `O(4)` on the first compatibility incidence.
When that incidence is written with equation coefficients `f` and
the unique first correction coordinates `h`, these tests can be
written polynomially in `f,h` after the actual first-patch formulas
are exported. The bundle argument does not require a choice of
quartic correction variables. It does not itself compute the
universal `R4` or prove that the twenty-five equations have no smooth
solutions.

The parameter twists in the companion note agree with this statement.
Write `H=O_U(1)`. The universal map is
`O^5 -> (O(2) tensor H)^{direct sum 3}`,
so `det W=O(-6) tensor H^-3`. Rank-two duality gives
`W^*=W(6) tensor H^3`. The pushed-forward generating presentation is

    O_U^25 -> p_*W(10) tensor H^3 -> 0.

Here `Q2^*=p_*W(10)`. The actual obstruction bundle is
`V2=Q2 tensor H`, so its dual is `p_*W(10) tensor H^-1`.
Twisting the last surjection by `H^-4` gives exactly the companion
note's `25 H^-4 -> V2^*`. This is the same as the earlier
`25 H^-3 -> Q2^*`; it introduces no extra coefficient factor or
denominator. In particular the scalar tests have coefficient degree
four, as required.

## 5. The homogeneous quartic discriminant detects smoothness

Let

    Delta=b^2-4ac in H0(P1,O(4)).

For a basepoint-free triple over an algebraically closed field of
characteristic zero, the root divisor `Z_f` is smooth if and only if
the homogeneous binary quartic `Delta` has four distinct zeros, or
equivalently its binary-quartic discriminant is nonzero.

To see this locally, first suppose `a` is a unit. The fiber point
`v=0` is absent there, and the equation in `x=u/v` becomes

    y^2=Delta, y=2a x+b.

The analogous chart works when `c` is a unit. At a zero of `Delta`,
basepoint freeness forces at least one of `a,c` to be a unit, so
these charts cover every possible ramification point. The double
cover is smooth at such a point exactly when the local vanishing
order of `Delta` is one: in the local equation `y^2-Delta(t)=0`,
the fiber derivative vanishes at `y=0`, and the base derivative is
nonzero precisely for a simple zero. Away from `Delta=0`, the cover
is etale and smooth. If only `b` is a unit and `a=c=0` at a base
point, then `Delta=b^2` is nonzero there and the two direction roots
are distinct, so no omitted singularity occurs.

This argument uses a local parameter at every point of the base,
including infinity. The quartic must remain homogeneous: dropping
its apparent affine degree and ignoring its zero at infinity would
not be a valid smoothness test. An identically zero discriminant
section gives a generically nonreduced cover and is excluded.

Conversely, a common base zero of `a,b,c` forces `Delta` to vanish
to order at least two there. Thus a nonzero binary-quartic
discriminant already implies basepoint freeness. The entire smooth
`(2,2)` open is consequently described by this one nonvanishing
condition. The discriminant has degree six in the quartic
coefficients and degree twelve in the original nine coefficients.

The companion note's raw-coefficient formulas

    I=12d4d0-3d3d1+d2^2,
    J=72d4d2d0+9d3d2d1-27d4d1^2-27d3^2d0-2d2^3,
    Disc=(4I^3-J^2)/27

use the correct binary-quartic normalization for
`d0Y^4+d1XY^3+d2X^2Y^2+d3X^3Y+d4X^4`. They do not require
`d4!=0`. In particular a simple root at infinity is retained.

## 6. The universal model algorithm matches the geometric construction

The new generator was inspected without executing it. Its coefficient
ring uses exact rational sparse polynomials; its normal monomials are
truncated only above total normal degree four. The inverse of
`z^4+u+(3/2)zv` is expanded through the fourth power of its linear
correction, which is sufficient for all retained terms. The accepted
chart substitutions for `w,u',v'` are implemented literally.

For coefficient `a_j,b_j,c_j`, the reversed second-chart base factor
is `w^(2-j)`. The generator uses this factor and normalizes by `z^16`.
Its first discrepancy is exactly

    S3=[z^16 f1]_3-(h+beta)f.

The sixteen middle coefficients give the first incidence. Its
nonnegative part is `G0`. A negative term `p z^k u^i v^j`, with
`k<=-5`, gives the second-chart correction
`-p w^(-k-5)u'^i v'^j`. Since `i+j=3`, its normalized leading pullback
is precisely `-p z^k u^i v^j`. Thus the generator's first-patch split
has the correct sign and exponent. The finite support is from `-6`
through `1`, so the two local cubic corrections have base degree at
most one, as claimed.

The quartic representative is then

    pr_-11..-1([z^16(f1+G1)]_4-(h+beta)G0),

which retains nonlinear base motion, the first equation unit, and
its product with the first correction. Unknown second units and
quartic local coboundaries are exactly the terms removed by the dual
quotient. The code forms the signed complementary minors of `T_f`
and pairs their columns after shifts `0,...,4` using coefficient
index `-1-shift-z`. This is the required residue and accounts for
all twenty-five tests.

The resulting discrepancy is linear in the coefficients of `f` and
has degree at most two in `h`. Its pairing with the cubic Plucker
vectors therefore has coefficient degree four in `f`, degree at
most two in `h`, and total degree at most six. The first equations
are linear in `f` and affine linear in `h` (equivalently a bilinear
term minus a linear term). Finally the generator appends
`smoothInverse*Disc-1`, which represents precisely the homogeneous
smooth open. No coefficient chart is omitted. This verifies the
algorithmic model underlying the proposed single global elimination;
it does not evaluate that elimination.

## 7. Scope

The twenty-five equations are a globally valid replacement of the
second quotient-membership test, not a proof of emptiness. The
accepted formal nonexistence theorem supplies an existential finite
empty stage; it does not imply that this second stage is empty.
Any effective elimination must still retain the homogeneous smooth
open and the actual first cubic patches and equation units.

No commit or memory update was made.
