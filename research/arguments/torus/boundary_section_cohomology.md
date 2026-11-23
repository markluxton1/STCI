# Section cohomology of pure torus boundaries

This account retains the cohomology and section hull of the **pure**
constant-orbit image in an intrinsic Hilbert limit. The finite endpoint
correction and the finite section defect are different objects. The
[endpoint theorem](../../results/intrinsic_limits_endpoint_fibers.md)
identifies the pure image and its embedded correction; the
[flat-boundary inequality](../torus_hilbert_boundary.md#pure-quotient-cohomology-is-a-flat-boundary-obstruction)
supplies the necessary cohomology comparison used here.

**Review.** The finite-kernel cohomology comparison and its original
Cartier controls were independently reconstructed in the linked proof.
The all-degree diagonal exclusion below and its \((6,6)\), \((5,8)\)
consequences were independently reconstructed during the November 23,
2026 branch synthesis. The interpolation and splitting formulas below
were also independently reconstructed in the written-state geometry review.
The diagonal identification and cohomological statements are characteristic
free; this does not extend the separate involutivity theorem's scope.

## 1. The constant image gives a two-lattice interpolation map

Let \(k\) be algebraically closed, in any characteristic, and let
\(B=k[u^{\pm1},v^{\pm1}]/K\) have finite length \(n\), with its named
units. Write \(Y_B\) for its pure projective orbit image and
\(\nu:\mathbf P^1_B\to Y_B\) for the finite modification. The
[finite-image proof](../torus_embedded_quotients.md#endpoint-defects-and-hilbert-polynomial)
gives
\[
0\longrightarrow\mathcal O_{Y_B}(d)
 \longrightarrow\nu_*\mathcal O_{\mathbf P^1_B}(4d)
 \longrightarrow Q_0(d)\oplus Q_\infty(d)\longrightarrow0,
\qquad \ell(Q_i(d))=D_i(B).                         \tag{BC1}
\]
Here \(Q_i(d)\) denotes the twisted image cokernel, not just a vector
space with the indicated dimension. For \(d\ge0\), the middle sheaf
has zero \(H^1\), so
\[
\boxed{\quad
H^1(Y_B,\mathcal O_{Y_B}(d))=
\operatorname{coker}\!\left[
B\otimes_k H^0(\mathbf P^1,\mathcal O(4d))
 \xrightarrow{\operatorname{ev}_d}
 H^0(Q_0(d)\oplus Q_\infty(d))\right].\quad}         \tag{BC2}
\]

The map is restriction modulo the two actual endpoint image lattices.
At zero these use \(r^3u,r^4v\); at infinity they use
\(z^3v^2/u^3,z^4v^3/u^4\), with \(z=(u/v)r^{-1}\).
The transition of the degree-four polarization must also be retained.
Thus the same embedded algebra supplies both ends of one interpolation
problem. The scalar sum \(D_0(B)+D_\infty(B)\) gives the target dimension,
but does not determine the rank of \(\operatorname{ev}_d\).

If \(Y_B\) is the pure quotient of a flat CI\((a,b)\) boundary, then
for every \(d\ge0\), (BC2) must have cokernel dimension at least
\(h^1(\mathcal O_{X_{a,b}}(d))\). This is a test on the actual
endpoint algebra, available without reconstructing all generators of the
full limit. Passing it does not supply those generators.

## 2. The whole section-hull profile is constrained

More generally, let \(Y\) be a pure curve whose support avoids
\(V(x_0,x_3)\) and whose finite projection
\(\pi:Y\to\mathbf P^1_{[x_0:x_3]}\) has every component dominating the
base. Purity makes \(\pi_*\mathcal O_Y\) torsion-free, hence locally
free on this smooth curve. Write
\[
\pi_*\mathcal O_Y=\bigoplus_i\mathcal O_{\mathbf P^1}(-d_i).
\]
Since \(\mathcal O_Y(1)=\pi^*\mathcal O_{\mathbf P^1}(1)\), finiteness
of \(\pi\) and the projection formula give, for every integer \(d\),
\[
h^1(\mathcal O_Y(d))=\sum_i\max(d_i-d-1,0).           \tag{BC3}
\]
Equivalently these are the generator degrees of the free section hull
\(N=\bigoplus_d H^0(Y,\mathcal O_Y(d))\) over
\(A=k[x_0,x_3]\), so \(N=\bigoplus_i A(-d_i)\).

Suppose \(Y\) is the pure quotient of a flat CI\((a,b)\) limit \(L\),
with finite kernel \(T\) and \(t=\ell(T)\). Let \(c_i\) be the
CI section-module degrees: their multiplicities are the coefficients of
\((1+q+\cdots+q^{a-1})(1+q+\cdots+q^{b-1})\).
The finite-kernel comparison and flat semicontinuity give
\[
\boxed{\quad
\sum_i\max(d_i-d-1,0)\ \ge
\sum_i\max(c_i-d-1,0)\qquad(d\in\mathbf Z).
\quad}                                                   \tag{BC4}
\]
Comparison of Euler characteristics also gives
\[
\sum_i d_i=\sum_i c_i+t
 =\frac{ab(a+b-2)}2+t.                              \tag{BC5}
\]
The rank is \(ab\) on each side. The sum in (BC5) retains only one
part of the profile inequality (BC4).

For a saturated coordinate algebra \(E=S/I_Y\), the finite quotient
\(D=N/E\) is the section/Rao defect. For an entire translated cycle,
in characteristic different from two, actual sign invariance and nonzero
first moment additionally require opposite signs among equal-degree
generators of \(N\), including a nonstandard-sign class
in \(D/(x_0,x_3)D\); see the
[section-parity proof](chow_section_parity_defect.md).
This vertex defect is distinct from \(T\), which is supported at
projective endpoints in the intrinsic-limit application; for the general
finite-kernel comparison above, \(T\) can have other finite support.
In characteristic different from two, for every constant image supported
on a single translated quartic with \(n\ne0\) in \(k\), the parity condition is automatic: its invariant
pure cycle has nonzero moment. In particular every sole-support constant
image in characteristic zero is non-ACM and has that section-head class,
without any CI-origin hypothesis. It is a structural description, not an
additional endpoint filter. The CI-specific test is (BC4), or a restriction
on the actual source inducing this section algebra and its multiplication.
The full limit's separate contact condition is the
[endpoint conormal map](../torus_hilbert_boundary.md#involutivity-persists-through-the-full-torus-boundary).

## 3. Diagonal endpoint algebras can fail despite finite correction

Work in any characteristic and suppose \(a,b\ge2\),
\(n=ab/4\in\mathbf Z\), \(n\ge2\). For the diagonal algebra
\[
B_n=k[\epsilon]/(\epsilon^n),\qquad u=v=1+\epsilon,
\]
the pure constant image is exactly \(nC\subset Q\), by the
[Cartier identification](../torus_embedded_quotients.md#the-diagonal-quotient-recovers-the-cartier-multiples-nc).
This part of that argument uses no characteristic assumption: on
\(x_0=1\), the normal coordinate \(A=x_2-r^3\) maps to
\(r^3\epsilon\), and independence of \(1,\epsilon,\ldots,\epsilon^{n-1}\)
over \(k[r]\) makes its kernel exactly \((A^n)\); the opposite chart agrees.
On \(Q\simeq\mathbf P^1\times\mathbf P^1\), take
\(C=(3,1)\) and \(H=(1,1)\). The divisor sequence and Künneth give
\[
h^1(\mathcal O_{nC}(d))=
\begin{cases}
(3n-d-1)(n-d-1),&0\le d\le n-2,\\
0,&d\ge n-1.
\end{cases}                                           \tag{BC6}
\]
Indeed this is \(h^2(\mathcal O_Q(d-3n,d-n))\) for \(d\ge0\).
At \(d=a+b-4\), CI adjunction gives
\(h^1(\mathcal O_{X_{a,b}}(d))=h^0(\mathcal O_{X_{a,b}})=1\).
Consequently
\[
\boxed{\quad n\le a+b-3\ \Longrightarrow
B_n\text{ is not an endpoint algebra of a sole-supported CI}(a,b).
\quad}                                                  \tag{BC7}
\]
This uses R-0070 to identify the pure quotient of either full intrinsic
limit, followed by (BC4). An arbitrary finite endpoint correction cannot
repair the zero \(H^1\) in (BC6).

The pure polynomial is \(P_{nC}(d)=4nd+4n-3n^2\). A finite correction
to the CI polynomial would have to have length
\[
t=n(3n+4-2a-2b).                                    \tag{BC8}
\]
Thus the exclusion is stronger than requiring the pure and CI polynomials
to coincide. Among \(a\le b\), \(a,b\ge5\), and \(4\mid ab\), the
inequality in (BC7) is equivalent to \((a-4)(b-4)\le4\), and leaves
exactly the following cases:

| CI type | Diagonal endpoint algebra excluded | Required correction length |
| --- | --- | ---: |
| \((6,6)\) | \(B_9\) | 63 |
| \((5,8)\) | \(B_{10}\) | 80 |

For sextic pairs this excludes exact diagonal contact \(v=u\) in the
length-nine endpoint algebra. It does not exclude the order-eight quadric
direction or all higher-order departures from the diagonal. For larger
types failing \(n\le a+b-3\), this argument alone gives no exclusion;
the actual sources and endpoint correction still matter. The complete
diagonal profile below shows that (BC4) gives no further exclusions.

## 4. The complete diagonal profile

The diagonal section hull has the following splitting degrees:
\[
N_{nC}=A\ \oplus\!
 \bigoplus_{j=1}^{n-1} A(-j)^{\oplus2}
 \ \oplus\ A(-n)^{\oplus(2n+1)}.                    \tag{BC9}
\]
Indeed (BC6), \(H^0(\mathcal O_{nC}(d))=0\) for \(d<0\), and
\(P_{nC}(d)=4nd+4n-3n^2\) determine all section dimensions. The negative-twist
vanishing follows by injection into the finite modification
\(\mathbf P^1_{B_n}\). Successive second differences, or substitution
in (BC3), give (BC9). The rank is \(4n\) and the sum of the shifts is
\(3n^2\), as required by \(P_{nC}\).

Put \(c=a+b-2\). If \(n\ge c\), the sorted diagonal shifts dominate
the CI shifts \(i+j\), \(0\le i<a\), \(0\le j<b\), term by term.
To check this, below degree \(n\) the diagonal has \(1+2k\) shifts
at most \(k\). For \(0\le k<c\), the CI has at least that many:
its degree-zero coefficient is one and all coefficients in degrees
\(1,\ldots,c-1\) are at least two. For \(c\le k<n\), all \(4n\)
CI shifts are already at most \(k\). At degree \(n\) both lists
are exhausted. These cumulative counts prove the claimed dominance.
Every summand in (BC4) is increasing in its shift, so **all** the profile
inequalities hold when \(n\ge a+b-2\).

The integer alternatives \(n\le a+b-3\) and \(n\ge a+b-2\) are
exhaustive. Hence (BC7) is the exact exclusion range of the complete
cohomology profile for diagonal endpoint algebras, in every characteristic.
Passing that profile still supplies no compatible endpoint correction,
contact map, or actual homogeneous CI source. Testing more twists of the
same diagonal model cannot improve this obstruction.
