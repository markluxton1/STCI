# Exceptional quartic carrier geometry

This file owns the fixed-carrier geometry attached to the exceptional quartic
pencils classified in [Quartic pencils with the fixed Chow polytope](quartic_chow_pencils.md).
Work in characteristic zero unless a statement says otherwise. Normalize the
support to \(C_\pm=C_{1,\pm1}\), put
\[
A=x_1^3-x_0^2x_2,\qquad B=x_2^3-x_1x_3^2,\qquad
D=x_1^2x_2^2-x_0^2x_3^2,
\]
and write the exceptional family as
\[
F_\lambda=\lambda x_2A+x_1B,\qquad
G_\lambda=D+\lambda x_1A+\lambda^{-1}x_2B. \tag{1}
\]
The classification and uniqueness of this family remain in the canonical
[liaison/canonical-module proof](quartic_chow_pencils.md#two-translates-with-coinciding-cubic-jets).

## Two-sided contact and the nodal even-eight carrier

Two distinct translates have the same cubic graph coefficient at
\(p_0\) exactly when their \(u\)-parameters agree. Reversal sends
\(u\) to \(u'=v^2/u^3\), so matching cubic coefficients at **both**
endpoints gives \(u_1=u_2\) and \(v_1^2=v_2^2\).
In characteristic different from two, distinctness is equivalent
to \(v_2=-v_1\). Thus the exceptional support is exactly the
two-support configuration with coincident endpoint cubic jets in
both directions. The [endpoint different](chow_endpoint_different.md)
measures the resulting normalization-colength jump from \(3\)
to \(4\), and different-saturation length from \(12\) to \(14\).

The carrier \(T=V(G_1)\) in characteristic zero has a classical
K3-surface description. Put
\[
 P=x_1x_2+x_0^2,\qquad Q=x_1x_2+x_3^2,\qquad
 R=x_1^2+x_2^2.
\]
Direct expansion gives \(G_1=R^2-PQ\). Its singular locus consists
of the eight reduced solutions of \(P=Q=R=0\) and the two
marked endpoints \(p_0,p_\infty\). At each of the first eight
the three quadrics are local parameters and the equation is
\(R^2-PQ\); at the endpoints the tangent quadratic is,
up to sign, \(x_1x_2+x_3^2\) or \(x_1x_2+x_0^2\) in the
corresponding affine chart. All ten singularities are ordinary
nodes, and the minimal resolution \(\pi:X\to T\) is a K3 surface.

Let \(h=\pi^*H\), let \(\Gamma_\pm\) denote the strict transforms of
\(C_\pm\), write \(E_0,E_\infty\) for the endpoint exceptional curves
and \(E_1,\dots,E_8\) for the others. Since
\(F_1|_T=2C_++2C_-\), its Cartier pullback is \(4h\).
The order of \(F_1\) at each of the eight interior nodes is one:
indeed
\(F_1=2x_1x_2R-x_2^2P-x_1^2Q\) and \(x_1x_2\ne0\) there.
At \(p_0,p_\infty\) its quadratic initial form is respectively
\(-x_2^2\) and \(-x_1^2\); the order on each exceptional curve
is two. The total-transform equality gives
\[
 4h\sim 2\Gamma_++2\Gamma_-+2E_0+2E_\infty
                 +\sum_{i=1}^8 E_i,
 \qquad
 \boxed{\ \sum_{i=1}^8E_i\sim
 2(2h-\Gamma_+-\Gamma_--E_0-E_\infty).\ } \tag{E8}
\]
Thus the *interior eight* are an even eight on the resolved K3;
the endpoint exceptional curves contribute integral corrections.
The image of the half-eight under
\(\operatorname{Pic}(X)\to\operatorname{Cl}(T)\) is
\(2H-C_+-C_-\). Equivalently,
\[
 2(C_++C_--2H)=0\quad\text{in }\operatorname{Cl}(T).
\]
This is nonzero two-torsion: if \(C_++C_-\sim2H\),
a section of \(\mathcal O_T(2)\) would cut out both curves;
it lifts to an ambient quadric, contrary to their distinct unique
containing quadrics. This is precisely the even-eight class, not
an additional unrelated torsion phenomenon.
The direct identity (E8) is the proof; for the established framework
see [Barth, *Even Sets of Eight Rational Curves on a K3-surface*](https://doi.org/10.1007/978-3-642-56202-0_1)
and [Casnati--Catanese, *Even sets of nodes are bundle symmetric*](https://arxiv.org/abs/alg-geom/9602024).
The symmetric determinant here has **quadratic** entries, and
is not thereby a linear quartic symmetroid.

This explains doubled divisors on an exceptional
**fixed carrier**; by itself it does not classify the
moving \(\lambda\)-orbit. The orbit's uniqueness is now
proved separately by [liaison and canonical-module rigidity](quartic_chow_pencils.md#two-translates-with-coinciding-cubic-jets).
The two geometric mechanisms are complementary.

## All mate degrees on a retained exceptional carrier

In characteristic zero, fix any nonzero member \(T\) of an exceptional
pencil (1), and choose an independent member \(T'\) from that pencil.
The proper pairs \((T,Q_b)\) whose whole cycles are made of translates
are exactly
\[
b=4j,\qquad Q_b|_{V(T)}=c\,(T'|_{V(T)})^j,\qquad
j\ge1,\quad c\ne0.
\tag{5}
\]
Their cycles are \(2j[C_{1,1}]+2j[C_{1,-1}]\).
In degree four this recovers the original pencil from any one of its
nonzero members and the condition on the mate's cycle.

In fact the disjoint weight sets in (1) show that the only translates
lying on \(T\) are \(C_{1,\pm1}\). Either a nonzero \(F_\lambda\) part
or the \(G_\lambda\) part forces both \(A=B=0\) on any contained
translate. Also \(T\) is integral. A plane factor is impossible by
properness with \(T'\) and the translated support. A reducible quartic
without a plane factor would have a quadric factor. Such a factor
contains one of the translates from its positive-degree intersection
with \(T'\), and is therefore that translate's unique smooth quadric.
An effective sum of its translated curves, all of the same ruling
class \((1,3)\), cannot be the hypersurface section by \(T'\).

The surface \(V(T)\) is regular at the two generic points.
The first-normal rows from the [properness and generic-cycle calculation](quartic_chow_pencils.md#properness-and-generic-cycle) are proportional on
each component, with quotient
\[
 \frac{\operatorname{in}_1(G_\lambda)}
      {\operatorname{in}_1(F_\lambda)}
 =\frac{\lambda^{-1}x_2+x_0^2/x_1}{x_1}
 =t^{-2}+\lambda^{-1}t^2
 \quad\text{on }C_\pm\cap\{x_0=1\}.
\]
This rational function is nonconstant in characteristic zero.
Hence no nonzero constant linear combination of
\(F_\lambda,G_\lambda\) can lose its first normal symbol
identically along either component. Every retained carrier
is therefore regular at both generic points.
It is also \(S_2\), being a hypersurface.

Write the cycle of \(Q_b\) on this surface as \(n_+[C_{1,1}]+
n_-[C_{1,-1}]\), allowing zero, so \(b=n_++n_-\). If \(n_+>n_-\),
the rational section \(Q_b^2/(T')^{n_-}\) of degree \(2(n_+-n_-)\)
is regular in codimension one. This follows from the orders on the
two regular branches and from \(T'\) being a unit off their support
in every other codimension-one local ring, in a local trivialization.
The \(S_2\) property extends the section. It lifts to an ambient form
by \(H^1(\mathbf P^3,\mathcal O(d-4))=0\) in its degree \(d\).
Its cycle on \(V(T)\) is supported on the plus translate alone,
contradicting the
[quartic-carrier exclusion](../../results/quartic_carrier_exclusion.md).
The opposite inequality is excluded by exchanging the signs.

If the common multiplicity is odd, \(2j+1\), divide \(Q_b\) by
\((T')^j\) and extend by the same argument. The resulting degree-two
section lifts to a quadric through both translates, impossible since
their unique quadrics are distinct. For common multiplicity \(2j\)
the ratio \(Q_b/(T')^j\) is an everywhere invertible regular function
by the same codimension-one argument applied to the ratio and its
inverse. It is constant by projectivity and integrality. Conversely
each restriction in (5) is nonzero and has the asserted cycle.
