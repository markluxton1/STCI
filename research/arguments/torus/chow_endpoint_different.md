# The endpoint different of a translated cycle

## Statement

Work in characteristic zero with an actual proper pair whose whole
cycle is \(\sum_{i=1}^r n_i[C_{u_i,v_i}]\), with distinct translates and
\(m=\sum n_i\). At \(p_0=[1:0:0:0]\) use affine coordinates
\((x,y,w)=(x_1,x_2,x_3)/x_0\). Let \(E\) be the completed local ring of
the intersection, \(B=E_{\mathrm{red}}\), \(\widetilde B\) its
normalization, and \(\delta=\dim_k(\widetilde B/B)\). The relative
Jacobian
\(\Delta=\det\partial(F,G)/\partial(x,y)\) for the pencil parameter \(w\)
has
\[
\dim_k\frac{(E\Delta):w^\infty}{E\Delta}=3r+2\delta.
\tag{1}
\]
Thus the length equals three exactly for a single translate.
Already a single jet at \(N=m+1\) detects this distinction:
\[
\dim_k E/(\Delta,w^N)=(4m-4)N+3
\quad\Longleftrightarrow\quad r=1.
\tag{2}
\]
The corresponding formulas hold at the opposite endpoint by reversal.
For projection to the tangent coordinate \(x\) in place of \(w\),
the relative Jacobian saturation quotient has length \(2\delta\).
The difference of the two lengths is \(3r\). The tangent Jacobian
ideal itself is saturated with respect to its parameter exactly at
a single support.

## Weighted trace and the different

The finite flat pencil has degree \(4m\) and its fiber over \(w=0\)
has just \(p_0\) in its support. Completing there gives the finite
free complete intersection \(E\) over \(R=k[[w]]\). Its \(R\)-dual is a
free rank-one \(E\)-module. The relative Kähler different is
\(E\Delta\), and its action on the dual gives
\[
\Delta E^\vee=E\operatorname{Tr}_{E/R}.
\]
These are the relative CI equality of the Kähler and Noether differents
and the finite free trace identity. They apply to the actual
dehomogenized regular pair in the polynomial ring over the completed base.
[Eisenbud–Ulrich, Theorems 8.1 and 8.3 in the author manuscript](https://www.math.purdue.edu/~bulrich/papers/Duality-and-Socle-180119.pdf).

The trace Gram map factors through \(B\) as the weighted pairing
\(\Gamma(z)(z')=\sum_i n_i\operatorname{Tr}_i(z_i z_i')\) on the reduced
generic fields, by trace additivity across the nilpotent layers.
All \(n_i\) are units in \(k\). The pairing is nondegenerate generically.
As \(E\to B\) is a surjection of finite free \(R\)-modules,
\(B^\vee\subset E^\vee\) is saturated. It follows that the saturation
of the image of the trace Gram map is \(B^\vee\), and its saturation
quotient is \(B^\vee/\Gamma(B)\). This identifies the saturation of
\(E\Delta\) with the annihilator of the nilradical under the duality.

On each normalized branch, \(w=v_i x^4\). Over \(k[[w]]\), the basis
\(1,x,x^2,x^3\) gives elementary exponents \(0,1,1,1\) for its
weighted trace pairing, since \(4n_i\) and \(v_i\) are units.
Passing from \(\widetilde B\) to the lattice \(B\) contributes
\(2\delta\) to the determinant valuation, proving (1). For the tangent
projection the normalization is a sum of copies of \(k[[x]]\), whose
weighted trace is unimodular. The same calculation gives \(2\delta\)
with \(\det\partial(F,G)/\partial(y,w)\). Finiteness over \(k[[x]]\)
holds since the reduced branches are graphs, and purity gives
flatness over that base. One can apply the different identity by
starting on the affine chart, where both normal coordinates are
integral over \(k[x]\) on the reduction and hence on the full ring,
and then completing at \(x=0\).

The pencil calculation uses invertibility of \(4\) and all \(n_i\).
The tangent calculation only uses invertibility of all \(n_i\).

### Classical discriminant and index interpretation

The number \(3r+2\delta\) is a specialization of classical
discriminant/index theory, not a new identity for arbitrary finite
algebras. When the normalized branches instead have tame parameter
\(w=v_i x^d\) with \(d\) invertible and all generic multiplicities
invertible in \(k\), the discriminant of each normalized branch over
\(k[[w]]\) has valuation \(d-1\). For a finite reduced order
\(B\subset\widetilde B\), the lattice-index formula gives
\[
 v_w(\operatorname{disc}(B/k[[w]]))
 =r(d-1)+2\operatorname{length}(\widetilde B/B).
\]
The relative complete-intersection Jacobian and trace-duality
identification is what makes this invariant accessible directly
from an **actual equation pair** in the quartic problem.
The proof above treats \(d=4\); the one-dimensional formula
alone does not establish the quartic's specific finite jet
threshold \(N=m+1\) for general \(d\).
This is the classical different/discriminant viewpoint
underlying [Eisenbud--Ulrich](https://www.math.purdue.edu/~bulrich/papers/Duality-and-Socle-180119.pdf)
and standard orders in separable extensions of DVRs.

The value \(3r+2\delta\) is determined by the reduced support
and its endpoint normalization lattice, with multiplicities used
only through the invertibility hypotheses. It is **not** a
complete invariant of the nonreduced Hilbert lift. For two
translated quartics, distinct cubic jets give \(\delta=3\)
and length \(12\), whereas coincidence at both ends in the
exceptional pair gives \(\delta=4\) and length \(14\).
The numerical change by two equals the embedded length in the
separate *flat torus limits* of the exceptional pencil, but
nothing here identifies the two quantities or proves a
conservation law. The former is a different of the original
finite CI, the latter an embedded correction of its limit.

## Colength and finite detection

The tangent-coordinate description \(y=u_i x^3,\ w=v_i x^4\)
computes \(\delta\). Choose independent vectors
\((u_i^\alpha v_i^\beta)_i\) greedily in ascending weight
\(3\alpha+4\beta\), with selected weights \(d_1,\ldots,d_r\).
The vectors form a constant basis of the normalization over \(k[[x]]\).
Multiplied by \(x^{d_j}\) they form a lattice basis of \(B\), since
each remaining monomial vector is a combination of selected vectors
of no greater weight. The lattice is complete and hence contains
the sums of the converging formal series. It follows that
\(\delta=\sum_j d_j\). Powers of a general linear combination of
\(u,v\) separate the \(r\) distinct points by Vandermonde interpolation.
Monomials of ordinary degree at most \(j-1\) have weight at most
\(4(j-1)\). Thus \(d_j\le4(j-1)\) and \(\delta\le2r(r-1)\).

The free rank of \(E/(\Delta)\) over \(k[[w]]\) is \(4m-4r\).
Its torsion has length \(3r+2\delta\). For \(r=1\) its torsion has
three factors of exponent one. For \(r>1\) and \(N\ge r+1\),
\[
\dim_k E/(\Delta,w^N)
\le (4m-4r)N+3r+4r(r-1)<(4m-4)N+3.
\]
This proves (2) since \(r\le m\). To recover \(r,\delta\) separately,
use two consecutive depths at least \(2m-1\). In fact
\(w^{r-1}\widetilde B\subset B\) by the lattice bound, and
\(\Gamma(\widetilde B)\supset w\widetilde B^\vee\). Dualizing the
lattice inclusion gives \(B^\vee\subset w^{-(r-1)}\widetilde B^\vee\).
Together these show \(w^{2r-1}B^\vee\subset\Gamma(B)\), so the
constant term of the jet length has stabilized by that depth.

For the [exceptional quartic pencils](quartic_chow_pencils.md#classification),
the two \(u_i\) coincide and the \(v_i\) are opposite, so the greedy
weights are \(0,4\) at both endpoints. Their different saturation
length is fourteen. Two-support invariant quartic pencils have
distinct cubic graph coefficients at both ends and weights \(0,3\),
giving length twelve. These refer to the **original** proper pairs
at the two projection fibers. The [embedded length two](quartic_hilbert_chow_limits.md#chow-closure-and-full-opposite-limits)
instead belongs to their flat torus limits. Formula (2) tests an
already given Chow-matched pair. A global equation bound ruling out
the single-translate value in arbitrary degrees is still open.
