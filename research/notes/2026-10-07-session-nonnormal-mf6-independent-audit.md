# Independent arbitrary-degree exclusion for four MF6 boundary carriers

Date: 2026-10-07. Status: **PROVED under the displayed coefficient and
characteristic hypotheses; independent algebraic audit**. This is a
fixed-carrier exclusion. It makes no claim that all nonnormal quartic
carriers, or the unrestricted C0 problem, have been excluded.

Let k be algebraically closed of characteristic zero, let

    P(b)=3b^2-2b+1=0, a=b+1,
    F0(b)=x0^3 x3-a x0^2 x1 x2+b x1^4,
    C0=[s^4:s^3t:st^3:t^4].

Neither b nor a vanishes. The two choices of b, and their coordinate
reversals, give the four carriers audited here. This note audits the
obstruction independently of the jet classification that produced them.

## 1. Finite birational normalization on the affine chart

On x3=1 put v=x2 and define a homomorphism into B=k[u,v] by

    x2=v,
    x1=u^2(a v-u)/b,
    x0=u x1.

Substitution annihilates F0. The affine F0 is primitive linear in x2:
the coefficient -a x0^2 x1 has greatest common divisor one with
x0^3+b x1^4. Therefore F0 is irreducible. The map's image has dimension
two: v is in the image, u is algebraic over its fraction field by the
monic equation below, and B has transcendence degree two. Thus its kernel
is exactly (F0), and its image is the coordinate ring A of this affine
surface.

The equation

    u^3-a v u^2+b x1=0

shows that B=A[u] is finite over A. On the dense open x1!=0 one has
u=x0/x1, so the map is birational. B is integrally closed. Moreover every
element of the common fraction field integral over A is integral over B
and hence belongs to B. Consequently B is exactly the normalization of
A. The argument uses a genuine finite normalization, rather than an
unverified parametrization.

## 2. The full inverse image of C0

On this chart I(C0)=(x1-v^3,x0-v^4). Write

    K=u^2-buv-bv^2.

The exact pullbacks satisfy

    x1-v^3=-(u-v)K/b,
    x0-v^4=u(x1-v^3)+(u-v)v^3.

Hence the full pulled-back ideal is (u-v)(K,v^3). The cofactor ideal
(K,v^3) has radical (u,v), since v=0 forces K=u^2. That residual point
already lies on u=v. Thus the **entire** reduced inverse image of C0 on
this affine chart is the diagonal u=v. No isolated point or additional
curve has been dropped. The diagonal maps isomorphically to C0 here:
its coordinates are (v^4,v^3,v).

## 3. A mate would violate equality on a normalization fiber

Suppose a homogeneous surface G of any positive degree is an STCI mate
for F0 and C0. Its affine restriction pulls back to a nonzero polynomial
g in B. It cannot vanish identically: this affine open is dense in the
integral carrier and a mate cannot contain that whole carrier. The
support equality from section 2 gives V(g)=V(v-u). Unique factorization
in k[u,v], and the fact that its only units are nonzero constants, force

    g=c(v-u)^n, c in k*, n>0.

For every v the two normalization points (0,v) and (a v,v) have exactly
the same original coordinates (0,0,v). Since g belongs to the original
coordinate ring A, it has equal values at these points. Therefore

    c v^n=c(-b v)^n, and (-b)^n=1.

The polynomial P is irreducible over Q, has discriminant -8, and its
other root is b*=2/3-b. Its quadratic-field norm is b b*=1/3.
Conjugating b^n=(-1)^n and multiplying yields (1/3)^n=1. This is
impossible for a positive integer n in characteristic zero. The
conjugation is used only inside Q(b); no automorphism of the whole
algebraically closed field is assumed.

Thus F0(b) admits no mate of any degree. This is stronger than the
degree-six cubic-defect obstruction for these particular carriers.

## 4. The other two carriers and exact verification

The displayed second pencil member is

    F1(b)=x0 x3^3+(b-5/3)x1 x2 x3^2+(2/3-b)x2^4.

It is exactly the coordinate reversal of F0(b*), interchanging
(x0,x1,x2,x3) with (x3,x2,x1,x0). The reversal preserves C0 by
interchanging s and t. Both roots b* again satisfy P. Therefore the
same obstruction excludes both F1 carriers.

The companion
[exact verifier](../computations/verify_session_nonnormal_mf6_fiber_obstruction.py)
checks the monic equation, pullback, primitive coefficient gcd,
full-support ideal identities, duplicate fiber coordinates, quadratic
norm and exact reversal identity. The argument for arbitrary n is the
symbolic norm proof in section 3, not a finite power search.

These statements require characteristic zero. Reduction modulo primes
can make b a root of unity; that possibility is intentionally retained.
The obstruction does not cover a general member alpha F0+beta F1 with
alpha beta!=0, or a different nonnormal carrier on C0.
