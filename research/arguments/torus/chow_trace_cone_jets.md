# Trace constraints on one carrier near a projection line

## Scope

Work over an algebraically closed field of characteristic zero. A proper
pair of positive degrees \((a,b)\), with cycle entirely made of
diagonal translates \(C_{u_i,v_i}=[s^4:s^3t:u_i st^3:v_i t^4]\)
of multiplicities \(n_i\), misses the line \(L=V(x_0,x_3)\).
The [existing first moment](chow_arrangement_moments.md#the-first-moment-theorem)
vanishes for invariant ideals, a single eigenform generator, or two
coordinate congruences. The trace here needs a jet of just **one actual
generator**. Its direction on \(L\) can be arbitrary.

Put \(r=x_0,\ s=x_3,\ x=x_1,\ y=x_2\). If \(F\bmod(r^2,s^2)\)
depends only on \(r,s,x\), then
\[
\sum_i n_i u_i/v_i=0.
\]
There is an identical conclusion with \(x,y\) exchanged. Consequently
the same linear Chow-coefficient equation as in the existing theorem
holds on the Chow closure of these presentations.

An oblique linear direction \(\ell=x+c y\), \(c\ne0\), also gives a
first-moment constraint except at one explicitly determined coefficient
of the second equation. If \(F\) depends only on \(r,s,\ell\) modulo
\((r^4,s^2)\) or \((r^2,s^4)\), it excludes sole support even at that
coefficient. The [arbitrary-line theorem](#a-sole-support-test-at-an-arbitrary-disjoint-line)
is the most intrinsic statement: for any \(p\notin C_0\)
and disjoint line \(L'\) through \(p\), **neither**
equation of a hypothetical characteristic-zero sole-support
CI can have a cone jet independent of a complementary fiber
coordinate modulo \(I(L')^5\). It follows from the
nondegenerate trace pairing for a birational projection from \(p\).
The marked-line moments are explicit, computable consequences
that cover additional repeated-support arrangements.

## The trace in a tower of monic equations

Write \(E=k[r,s,x,y]/(F,G)\), which is finite free over \(k[r,s]\) by the
[projection-line argument](fixed_surface_and_endpoint_algebras.md#4-the-plane-pencil-converts-every-admissible-pair-into-one-finite-cover).
Let \(R=k[r,s]/J\) for a homogeneous ideal \(J\subset(r,s)\).
Suppose \(F_R\in R[\ell]\), with coordinates \((\ell,y)\) in the fiber
plane. On \(L\) the restriction is a scalar multiple of \(\ell^a\).
The scalar is nonzero, since a zero restriction and any other
positive-degree binary form have a common point on \(L\).
Since the pair misses \(L\), the coefficient of \(y^b\) in \(G\), in
the coordinates \((\ell,y)\), is also nonzero. Rescale both forms to make
them monic in their indicated variables. There is a tower
\[
R\ \subset\ D=R[\ell]/(F_R)\ \subset\
E_R=D[y]/(G_R).
\]
If \(\lambda\ell+U(r,s)\) is the coefficient of \(y^{b-1}\) in \(G\),
the relative trace of \(y\) over \(D\) is its negative. Transitivity,
and the rank \(b\) of \(E_R\) over \(D\), give
\[
b\,\operatorname{Tr}_{E_R/R}(\ell^j y)
+\operatorname{Tr}_{E_R/R}(\ell^j(\lambda\ell+U))=0
\qquad(j\ge0). \tag{1}
\]
These are identities of the full finite free algebras over \(R\),
including when \(R\) has nilpotents.

## Moments on the marked line

On the reduced generic cone over \(C_{u_i,v_i}\), the element \(t=x/r\)
satisfies \(t^4=s/(r v_i)\), and \(y=r u_i t^3\). Use field trace there
and multiply by \(n_i\), as follows from a composition series of the
generic local algebra. Thus if \(i+3j=4q\), the trace of \(x^i y^j\) is
\[
4r^{i+j-q}s^q \sum_\nu n_\nu u_\nu^j/v_\nu^q,
\]
and it vanishes if \(4\nmid i+3j\). All odd-degree monomials have
zero trace, as do \(x^2,y^2\). Thus \(U\) drops out of (1) for odd \(j\).
Taking \(j=1\) gives
\[
(b+2c\lambda)\operatorname{Tr}(xy)=0,\qquad
\operatorname{Tr}(xy)=4rs\sum_i n_i u_i/v_i.
\]
This proves the coordinate and oblique claims modulo \((r^2,s^2)\).
The exceptional oblique coefficient \(\lambda=-b/(2c)\) says that the
mean of the roots \(y/\ell\) of \(G|_L\) is \(1/(2c)\).

Use \(j=3\) in (1). Among the degree-four terms only
\(\operatorname{Tr}(x^4),\operatorname{Tr}(x^2y^2),\operatorname{Tr}(y^4)\)
can be nonzero. Their base monomials \(r^3s,r^2s^2,rs^3\) are distinct.
The quotient by \((r^4,s^2)\) retains \(r^3s\), giving
\(\lambda\sum_i n_i/v_i=0\). The quotient by \((r^2,s^4)\) instead gives
\(c^3(b+c\lambda)\sum_i n_i u_i^4/v_i^3=0\).
For a single support all three tested moments are nonzero. The second
moment identity forces \(\lambda=-b/(2c)\) for \(c\ne0\), incompatible
with either fourth-degree identity.

For several supports, a sufficiently deep jet excludes every oblique
direction. Let \(d\) be the larger of the numbers of distinct \(1/v_i\)
and distinct \(u_i^4/v_i^3\). If \(J=(r,s)^{4d+1}\), compare in (1)
the two pure-power trace terms at each degree \(4q\), \(1\le q\le d\).
Their base monomials \(r^{3q}s^q,r^qs^{3q}\) each occur for just one
trace in that degree. The equations include
\[
\lambda\sum_i n_i v_i^{-q}=0,\qquad
c^{4q-1}(b+c\lambda)\sum_i n_i(u_i^4/v_i^3)^q=0.
\]
In each sequence some moment is nonzero. The distinct nonzero parameters
give an invertible Vandermonde matrix for powers starting with one, and
the aggregated multiplicities are positive integers. Thus \(\lambda=0\)
and \(b+c\lambda=0\), impossible for \(c\ne0\). In particular an exact
cone generator for a translated cycle has no oblique vertex on \(L\).
The coordinate first moment also holds in characteristic \(p\) when
\(p\nmid 2b\), where \(b\) is the degree of the unrestricted mate.
The oblique exclusions apply if \(p\nmid 2ab\). In that case the
aggregate multiplicities in either Vandermonde argument have nonzero
sum \(ab/4\), which suffices.

## An actual presentation covered by the one-sided test

Set \(U_0=x^4-r^3s,\ V_0=y^4-rs^3,\ W=U_0+V_0\).
For \(N\ge3\), take \(F=U_0^2+r^4W,\ G=W^N\).
This is a proper pair with radical \(\sqrt{(U_0,V_0)}\), whose four
translates have quotient parameters \((u_i,v_i)=(\zeta,1)\),
\(\zeta^4=1\). Their local parameters \(U_0,W\) give multiplicity \(2N\)
on each branch. Modulo \((r^2,s^2)\), \(F=x^8\), so the one-sided test
applies.

The smaller degree generator is unique up to scaling and has three
weights \(4,8,12\). Every minimal mate is a nonzero multiple of
\(G\) plus a polynomial multiple of \(F\). Its restriction to \(L\)
modulo \(x^8\) retains the two terms of \(G|_L=(x^4+y^4)^N\) with
\(x\)-degrees zero and four. A binary eigenform here is a monomial.
Thus no same-degree presentation has an eigenform generator or the
two simultaneous coordinate congruences. The degree-eight part of the
ideal is its non-eigenline \(kF\), so the ideal is non-invariant. The
cycle also has the invariant realization \((U_0^2,V_0^N)\).

## A sole-support test at an arbitrary disjoint line

Let \(p\notin C_0\) and let \(L'\) be any line through \(p\) disjoint
from \(C_0\). Choose linear coordinates \((r,s,\ell,y)\) with
\(L'=V(r,s)\) and \(p=V(r,s,\ell)\). Suppose a proper pair has sole
support \(C_0\). Neither generator can depend only on \(r,s,\ell\)
modulo \((r,s)^5\). Equivalently the directional polar of either
generator along \(p\) cannot lie in \(I(L')^5\).

Indeed the finite-free proof works with this \(r,s\) since the CI
misses \(L'\). If \(F\) has the stated jet, use (1) for \(0\le j\le3\).
The trace identities have ordinary degree at most four, so they hold
over \(k[r,s]\) by homogeneity. Over the base fraction field \(K\),
write \(K_C\) for the reduced function field of the cone over \(C_0\).
It has degree four over \(K\). Projection from \(p\) to the plane
\([r:s:\ell]\) is birational on \(C_0\). Its degree times the degree
of the image is four. The image is nondegenerate, and a conic image
would give a quadric cone through \(C_0\), whose unique containing
quadric is smooth. Hence \(1,\ell,\ell^2,\ell^3\) form a basis of
\(K_C\) over \(K\). The same reasoning uses the affine cones, since
their common scale coordinate \(r\) supplies a transcendental factor.

The CI trace on \(K_C\) is its field trace times \(ab/4\). By (1),
the element \(by+\lambda\ell+U\) in \(K_C\) is orthogonal to the whole
basis for the nondegenerate field trace pairing. Hence that linear
form vanishes on the quartic, contradicting nondegeneracy. This proof
uses only the separable reduced projection, the actual monic equations
over the thickened line, and the nonzero generic multiplicity in the
field. With another nondegenerate curve of degree \(d\) and a
birational projection from \(p\), the same argument works modulo
\((r,s)^{d+1}\). The criterion also applies to any irreducible
factor of either carrier of a hypothetical sole-support pair: the
factor and the other equation are proper, and their positive-degree
cycle is still supported on \(C_0\).

At the marked line with oblique \(\ell\) and
\(\lambda=-b/(2c)\), \(by+\lambda\ell\) is trace-orthogonal to
\(1,\ell,\ell^2\) on the reduced quartic. Thus the trace tests through
ordinary degree three allow this exceptional coefficient. This
calculation concerns the identities and supplies no lift exhibiting
such a cone jet.
