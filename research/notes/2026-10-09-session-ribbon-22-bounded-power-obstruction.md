# A bounded all-power obstruction for the surviving displayed [2,2] pencil

Date: 2026-10-09. Author: root. Status: **PROVED HERE for the displayed
pencil**, under the accepted genus-one ribbon and actual-conductor
hypotheses. This does not assert that every [2,2] candidate has this pencil.
The complete genus-one lane and the unrestricted STCI question remain OPEN.

Use x,y,v,w for the retained coordinates x0,x1,x2,x3 and z for Y2.
Let E0,...,E5 be the six actual RNC quadrics in the entire-conductor note.
The pencil is

    Q1=2E1+E3-E4,
    Q2=E0-2E1-E2/2+E4+E5/4.

The independent paused worker reported a reduction to this pencil; that
coverage assertion is not used here. Assume the surface is the integral
normal CI projection in the accepted conductor theorem. The three quadrics
Q1,Q2,E3 are independent in the ribbon net with direction (1,0,2), whose
discriminant is nonzero. Consequently Q=E3 has divisor exactly 2c on S.

Write Q1=-z^2+A z+R1 and Q2=Lz+R. Direct expansion gives

    A=-2y+v, R1=2xv+yv-yw,
    L=x+2y-v+w/4,
    R=-y^2-2xv-(xw-yv)/2+yw-v^2/4.

On S the third quadric is Q=ell z+q, where ell=2y-v and q=-2xv+yw.
The entire downstairs conductor is Gamma=V(L,R). Eliminating x by
x=-2y+v-w/4 gives its plane equation

    Rc=-y^2+(9/2)yv+2yw-(9/4)v^2+w^2/8.

The determinant of its symmetric matrix is 243/128, so Gamma is a smooth
integral conic. Its entire upstairs algebra is

    O_Gamma[z]/(z^2-Az-R1),     sigma(z)=A-z.

The trace T and norm N of Q in this algebra are

    T=2q+A ell,     N=q^2+Aq ell-R1 ell^2.

Reduce T^2 and N modulo Rc using lexicographic order y,v,w. The two
coefficients indexed by yv^3 and yv^2w are respectively

    T^2: (114,336),       N: (1,4).

Their determinant is 120. Thus T^2 and N are not proportional over k as
sections on the entire conic, and N is nonzero at its generic point.

If Q^n descended for any n>0, in the generic quadratic algebra its unit
ratio r=sigma(Q)/Q would satisfy r^n=1. In a quadratic field extension it
is a constant root of unity; in a split algebra the two constants are
reciprocal. In a nonreduced generic quadratic algebra the same conclusion
follows from the separability of X^n-1 in characteristic zero. In every
case r+r^(-1) is a scalar, so

    T^2/N = 2+r+r^(-1)

is constant. This contradicts the coefficient minor. Therefore no positive
power of Q descends through the actual conductor. A hypothetical mate has
even degree 2n and pullback a scalar multiple of Q^n, so this pencil admits
no mate in any degree under the stated geometric hypotheses.

This uses the full quadratic algebra, not even-valuation claims at singular
surface points. It also requires no bound on n and no nonsplit assumption.

The exact companion is
`research/computations/verify_session_ribbon_22_bounded_2026_10_09.py`.
During reconstruction a scratch assertion used the wrong sign for Q1 in
the reduction Q=ell z+q; it failed immediately. The corrected identity is
E3-Q1=ell z+q, and the failed scratch run was not treated as evidence.
The bounded checker below verifies this sign before computing the minor.
The complete [2,2] reduction, endpoint charts, and remaining partitions
[4] and [3,1] are separate continuation obligations.
