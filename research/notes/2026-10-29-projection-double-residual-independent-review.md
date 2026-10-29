# Independent audit: smooth double residual in the marked quadric source

October 29, 2026. Reviewer: `projection_audit/double_residual_review`.

**Verdict: PASS for the literal characteristic-zero stratum
\(V(q(U))=2c+2R\), with any divisor \(R\ne c\) of class \((1,1)\).**
Every basepoint-free tuple in that stratum fails full singleton inverse
support. This is a reviewed provisional exclusion, not a canonical
promotion or a computation of the full sixteen-parameter projection
locus. The independent reconstruction below checks the actual morphism
implication as well as the binary coefficient calculation.

The audited proof is
[the double-residual note](2026-10-29-projection-double-residual.md),
with [its exact verifier](../computations/stci_projection_double_residual_2026_10_29.m2).
The larger source and admissibility conditions remain those of
[the projection record](2026-10-29-projection-locus.md) and
[R-0004](../results/projection_phase_reduction.md). The divisor degree
calculation is in
[the residual geometry note](2026-10-29-projection-residual-geometry.md).

## Reconstruction of the surface-to-curve implication

Let \(S=\mathbf P^1\times\mathbf P^1\), with marked diagonal
\(c\), and let the four \((2,2)\) sections be basepoint free. The
resulting morphism is finite onto its image: a positive-dimensional
projective fiber would contain a curve of degree zero against the ample
pullback \(\mathcal O_S(2,2)\). Its determinant divisor is assumed
exactly \(E=2c+2R\); in particular neither component is the entire
surface.

On \(E\), the rank-one coordinate matrix defines the two ruling
pullbacks from the smooth target quadric. The first has total degree
eight on \(E\) and degree three on \(c\); the second has total
degree eight and degree one on \(c\). Additivity on the component
cycle gives first and second degrees \((2,6)\) on \(2R\), hence
\((1,3)\) on \(R\). For clarity, the degree-eight assertion follows
from the line-bundle cokernel resolution
\(0\to\mathcal O_S(-2,-2)^2\to\mathcal O_S^2\to i_*L\to0\):
\(\chi(L)=0\), while \(E=(4,4)\) has arithmetic genus nine.
The other ruling has degree \(16-8=8\) on \(E\).

A smooth \((1,1)\) curve \(R\) is isomorphic to \(\mathbf P^1\).
Its first ruling map has degree one, so is an isomorphism. The image
\(C'\) is therefore the graph of a degree-three morphism in the other
ruling. This checks the orientation: the first projection degree is one,
the second projection degree is three, and its divisor class on the
target quadric is \((3,1)\). Its equation is linear in \(B\), with
coprime cubic coefficients in \(A\). In particular it is irreducible
and distinct from \(C_0\), whose class is \((1,3)\).

If the full reduced inverse of \(C_0\) were \(c\), each point of
\(R\) mapping to \(C_0\) would lie in \(R\cap c\). The graph
description makes \(R\to C'\) an isomorphism; consequently
\(C'\cap C_0\) has at most two points, since \(R\cdot c=2\).
Tangency of \(R\) and \(c\) only decreases this support count and
is retained. The scheme intersection has total degree
\((3,1)\cdot(1,3)=10\); its pullback to the embedded parametrization
of \(C_0\) is a nonzero binary degree-ten form with at most two roots.
No surface birationality hypothesis is used.

## Independent binary calculation

Substitution \(A=(s^3:t^3),B=(s:t)\) sends the monomial basis of
\(H^0(Q,\mathcal O(3,1))\) to eight distinct monomials. Their
\(t\)-indices are exactly \(0,1,3,4,6,7,9,10\), so the
restriction map is injective and its image misses indices \(2,5,8\).

When both roots are finite and nonzero, rescaling \(t/s\), and then
exchanging the two root factors if necessary, reduces the binary form
up to a nonzero scalar to
\((s-r t)^m(s-t)^{10-m}\), with \(1\le m\le5\) and
\(r\ne0,1\). These transformations preserve the monomial image
space. I independently checked the following elimination of the three
missing coefficients:

- At \(m=1\), the index-two coefficient forces \(r=-4\), where
  the index-eight coefficient is nonzero.
- At \(m=2\), the first and last missing coefficients would force
  \(r=-29/16\); the first then equals \(585/256\ne0\).
- At \(m=3\), after removing the nonzero \(r\) factor from the
  last coefficient, the two quadratic equations force \(r=-8/7\).
  The monic first quadratic there equals \(15/49\ne0\).
- At \(m=4\), removing the nonzero \(r^2\) factor from the last
  coefficient and subtracting the quadratics forces \(r^2=1\).
  Neither value is a root of the first quadratic.
- At \(m=5\), the first coefficient is
  \(5(2r+1)(r+2)\). The index-five coefficient has nonzero values
  \(-81/32\) and \(81\) at \(r=-1/2,-2\), respectively.

Thus there is no two-root form with both roots finite and nonzero.
The one-root form at such a point is a tenth power with nonzero
index-two coefficient, so is also excluded. The exact verifier was run
independently and returned gcd one in \(\mathbf Q[r]\) in each of
the five cases, followed by its expected pass messages and exit zero.

For an endpoint root and a nonendpoint root, the nonzero coefficient
indices form an interval. If the endpoint is \(s=0\), avoiding index
two forces endpoint multiplicity at least nine. If it is \(t=0\),
avoiding index eight gives the same conclusion. The surviving forms
are \(s^9(as+bt)\) or \(t^9(as+bt)\). Their unique bidegree
\((3,1)\) lifts have a factor \(A_0^3\) or \(A_1^3\),
respectively, and hence are reducible. If both roots are endpoints,
the surviving forms are single permitted monomials; their unique lifts
again have a nonconstant cubic factor in \(A\). Single endpoint
roots are included in these cases.

This exhausts distinct and repeated roots, endpoints and their
complements. No irreducible bidegree \((3,1)\) equation restricts to
a form with support on at most two points. The contradiction proves
the stated double-residual exclusion.

## Boundaries and authority

The binary degree-ten computation applies to all parameters satisfying
the literal divisor condition with smooth \(R\ne c\), including all
possible tangencies of \(R\) with \(c\). The separate geometric
extension below covers reducible \(R\). Other residual \((2,2)\)
divisors, the order-one determinant stratum, and the cone and plane source
models remain outside the result. Its binomial coefficient
argument is stated only in characteristic zero. There are no admissible
survivors within this stratum and thus no descent survivor to test here.
The full projection locus and descent on any genuinely surviving strata
remain open tasks; this reviewed exclusion does not close them.

## Independently checked extension to the whole residual-square locus

The same exclusion extends to reducible \(R\), and therefore to every
divisor \(R\ne c\) of class \((1,1)\). Such a divisor is either
smooth or the union \(F+G\) of a fiber from each source ruling; an
irreducible singular case is impossible for an arithmetic-genus-zero
\((1,1)\) curve.

In the reducible case the first target ruling degree on \(R\) is one,
so global generation makes its degrees on \(F,G\) nonnegative integers
with sum one. On whichever component it is one, the second ruling degree
is also one: each source ruling fiber has degree two against
\(H=(2,2)\). That component consequently maps isomorphically onto an
irreducible target graph conic of class \((1,1)\). Full singleton inverse
support would make its intersection with \(C_0\) supported at the
single image of its source intersection with \(c\).

An equation of target class \((1,1)\) restricts on \(C_0\) to a binary
quartic with monomial indices \(0,1,3,4\); its coefficient at index two
is zero. If that quartic has a single root, it is a nonzero scalar
multiple of \((as+bt)^4\). Its missing coefficient equals
\(6a^2b^2\), so in characteristic zero one of \(a,b\) is zero.
The restriction is then \(s^4\) or \(t^4\). The restriction map is
injective on this four-dimensional equation space, and its unique lifts
are \(A_0B_0\) and \(A_1B_1\), both reducible. This contradicts the
irreducible graph conic.

Thus the entire determinant-order-two residual-square stratum
\(V(q(U))=2c+2R\), \(R\in|(1,1)|\), \(R\ne c\), has no
basepoint-free full-singleton tuple. This extension is a separate new
geometric deduction, independently reconstructed here and reported to
the author and root agent. It still leaves nonsquare \((2,2)\)
residual divisors and the order-one determinant stratum unresolved.
