# A completed double-residual stratum in the marked quadric source

October 29, 2026. Author: `projection_audit`, continuing the independent
review with a new exact incidence calculation. Status: **independently
reviewed provisional scoped exclusion**; see
[the independent geometric and binary-incidence review](2026-10-29-projection-double-residual-independent-review.md).
The ambient sixteen-parameter locus remains open.

## Literal stratum and claim

Use the complete marked smooth-quadric source, field and admissibility
requirements in [the projection record](2026-10-29-projection-locus.md).
Suppose a basepoint-free tuple satisfies

\[
 V(q(U))=2c+2R,
\]

where \(c\) is the diagonal and \(R\ne c\) is an effective divisor of
class \((1,1)\) on the source quadric. Then its full reduced inverse support
of \(C_0\) cannot be \(c\). This excludes the **entire stated
double-residual stratum**, without a birationality assumption on the
surface map. It does not exclude other residual divisor types.

First suppose \(R\) is smooth. The ruling-degree calculation in
[the residual geometry note](2026-10-29-projection-residual-geometry.md)
gives degrees \((2,6)\) on the cycle \(D=2R\), hence degrees
\((1,3)\) on \(R\). Thus the first ruling map from \(R\simeq\mathbf
P^1\) has degree one. Its image \(C'\) is the graph of a degree-three
morphism to the second ruling, and is an irreducible target curve of
class \((3,1)\). Its equation has the form

\[
 H(A,B)=f_3(A_0,A_1)B_0+g_3(A_0,A_1)B_1,
 \qquad \gcd(f_3,g_3)=1.
\]

If full singleton inverse support held, every point of \(C'\cap C_0\)
would have its preimage on \(R\) in \(R\cap c\). The latter has
length two and support of size at most two. Consequently the degree-ten
binary form \(H|_{C_0}\) would have at most two distinct roots. The
following exact binary calculation rules out that possibility for every
irreducible \(H\).

## The required binary incidence is empty for irreducible equations

On the target quadric use
\(A=(s^3:t^3)\), \(B=(s:t)\) for \(C_0\). The restriction of the
eight-dimensional space \(H^0(Q,\mathcal O_Q(3,1))\) is precisely

\[
 W=\langle s^{10-j}t^j:j\in\{0,1,3,4,6,7,9,10\}\rangle.
\]

The eight monomials are distinct, so this restriction is injective.
Membership in \(W\) means that the coefficients with indices
\(j=2,5,8\) vanish. The restriction of a nonzero equation therefore
is nonzero, of degree ten.

First suppose both roots are finite and nonzero in \(s/t\).
Rescaling the source parameter, which preserves the monomial space
\(W\), and exchanging the two root factors give

\[
 P=(s-r t)^m(s-t)^{10-m},\qquad 1\le m\le5,
 \quad r\ne0,1.
\]

For each of the five possible multiplicities, the polynomials in \(r\)
giving its coefficients at indices \(2,5,8\) have greatest common
divisor one in \(\mathbf Q[r]\). Thus they have no simultaneous zero
over any characteristic-zero extension. The exact coefficient extraction
and gcd calculation are in
[the verifier](../computations/stci_projection_double_residual_2026_10_29.m2),
with [saved output](../computations/stci_projection_double_residual_2026_10_29.txt).
These are all parameter values, rather than a finite sample.

The gcd calculations can also be checked directly with quadratic
remainders. At multiplicity one, the first missing coefficient has root
\(r=-4\), where the last is nonzero. At multiplicity two, common zeros
of the first and last would require \(r=-29/16\), where the first is
\(585/256\ne0\). At multiplicity three they would require
\(r=-8/7\), where the monic first quadratic is \(15/49\ne0\).
At multiplicity four they would require \(r=\pm1\), neither a zero
of the first quadratic. At multiplicity five the first quadratic is
proportional to \((2r+1)(r+2)\); the coefficient at index five is
nonzero at both roots (its values are \(-81/32\) and \(81\)).

If there is only one nonendpoint root, its tenth power has nonzero
coefficient at index two, so is not in \(W\).

If one root is the endpoint \(s=0\) and the other is nonendpoint,
write \(P=s^m(s-r t)^{10-m}\), \(r\ne0\). Every coefficient at
indices \(0,\ldots,10-m\) is nonzero. The missing coefficient at
index two forces \(m\ge9\). The only resulting forms are
\(s^9(as+bt)\), including the one-root boundary. Their unique lifts
to \(H^0(Q,\mathcal O(3,1))\) have the factor \(A_0^3\), and
are reducible. The endpoint \(t=0\) is symmetric: the missing index
eight forces multiplicity at least nine and the lift has factor
\(A_1^3\).

Finally, if both roots are the endpoints, the permitted restrictions are
the monomials \(s^{10-j}t^j\) for the eight allowed indices. Each is
the restriction of a single monomial of bidegree \((3,1)\), which has
a positive-degree cubic factor in \(A\), and hence is reducible. This
also includes a single endpoint root.

The cases exhaust all binary degree-ten forms with at most two distinct
roots. No irreducible equation of bidegree \((3,1)\) has such a
restriction. This contradicts the necessary form of \(C'\), proving
the stated stratum empty.

## Reducible residual support is excluded as well

Every effective nonintegral divisor of class \((1,1)\) is the reduced
union \(R=F+G\) of one fiber of each source ruling. Its total first
target ruling degree is one, and global generation makes its degrees
on \(F,G\) nonnegative. Exactly one component consequently has first
ruling degree one. Its \(H\)-degree is two, so its second ruling degree
is one as well. It maps birationally, via its first ruling coordinate,
onto an irreducible target curve of class \((1,1)\).

That source component meets \(c\) in just one point. Full inverse
support would force all four intersections of its target image with
\(C_0\) to be supported at the image of that point. The restriction
of \(H^0(Q,\mathcal O_Q(1,1))\) to \(C_0\) is injective and spans
the binary quartic monomials with indices \(0,1,3,4\). A nonendpoint
fourth power \((s-r t)^4\) has coefficient \(6r^2\ne0\) at the
missing index two. The only one-root forms in this subspace are therefore
the endpoint powers \(s^4,t^4\). Their unique target lifts are
\(A_0B_0,A_1B_1\), both reducible. This contradicts the irreducible
\((1,1)\) target image.

The smooth and reducible cases exhaust effective divisors of class
\((1,1)\). Thus the full stated square-residual stratum is excluded.

## Scope retained

The divisor \(R\) must be different from \(c\); both possible types
of effective \((1,1)\) divisor are included. Other residual divisor
types of class \((2,2)\), and the determinant-order-one stratum, are
not decided here. The argument uses
characteristic zero in its binomial coefficients and gcd certificate.
It neither classifies the full admissible projection locus nor tests
descent on any surviving projection. Within the stated stratum there
are no surviving admissible parameters, so there is no descent survivor
to test.
