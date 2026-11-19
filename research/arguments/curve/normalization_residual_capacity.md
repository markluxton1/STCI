# Residual curves as a corrected hyperplane test

The mechanism is to correct the hyperplane class until it has degree zero
on the known negative residual curves. Every other curve still has positive
degree, so this corrected class measures how much of an actual equation can
vanish along the inverse of the marked curve. The construction below is an
elementary nef-divisor argument, not a new general theory of nef cones.

A **proper containing form** means a homogeneous equation containing the
marked curve and sharing no surface component with the carrier. Unlike a
sole-support mate, it may have a residual intersection curve. All numerical
bounds below concern these actual forms, not arbitrary normal symbols.

## A reusable negative-curve correction

Let \(S\) be a normal integral projective surface over an algebraically
closed field, with an ample Cartier class \(H\). Suppose a nonzero section
\(q\) of \(\mathcal O_S(eH)\), \(e>0\), has complete divisor
\[
 \operatorname{div}(q)=\sum_i a_i\Gamma_i+\sum_j t_jT_j,
 \qquad a_i,t_j>0.
\tag{1}
\]
The curves listed are distinct. Assume every \(T_j\) lies entirely in the
regular locus of \(S\), and its intersection matrix
\(M=(T_j\cdot T_k)\) is negative definite. These curves are then Cartier,
and intersections with distinct effective curves are nonnegative. Put
\(h_j=H\cdot T_j>0\), and define
\[
 c=-M^{-1}h,\qquad P=H+\sum_j c_jT_j.
\tag{2}
\]
All \(c_j\) are strictly positive. Indeed \(-M\) is positive definite
with nonpositive off-diagonal entries. Its quadratic function
\(\frac12x^t(-M)x-h^tx\) has unique minimizer \(c\). Replacing the
negative coordinates of a vector by zero lowers this function: the removed
quadratic block is positive, the cross terms are nonnegative, and the
removed linear terms are positive. Thus \(c\ge0\). A zero coordinate
would make the corresponding entry of \((-M)c\) nonpositive, contradicting
\((-M)c=h>0\).

Consequently \(P\cdot T_j=0\), whereas \(P\cdot Z>0\) for every other
integral curve \(Z\): its hyperplane degree is positive and its intersections
with the \(T_j\) are nonnegative. Thus \(P\) is nef, with null curves
exactly the \(T_j\), and \(P\cdot H>0\). Equation (1) gives
\[
 \sum_i a_i(P\cdot\Gamma_i)=e(P\cdot H).
\tag{3}
\]
Even without a section \(q\), the correction (2) gives the following
inequality; (1) supplies the useful weight normalization (3).
For any nonzero section of \(\mathcal O_S(bH)\) with divisor
\(\sum_i r_i\Gamma_i+E\), where \(E\) is effective and contains no
\(\Gamma_i\), this proves the weighted capacity bound
\[
 \sum_i r_i(P\cdot\Gamma_i)\le b(P\cdot H).
\tag{4}
\]
Equality holds exactly when \(E\) is supported on the \(T_j\).
For fixed \(r_i\), its coefficients are uniquely determined by
intersecting with all \(T_j\), since \(M\) is invertible. Hence there
is at most one such section up to a nonzero scalar: two have the same
Weil divisor, so their ratio and its inverse are regular on the normal
surface and therefore constant by projectivity. This is uniqueness,
not existence of an equation with a proposed divisor.

If \(S\) normalizes an integral hypersurface and \(H\) is the pulled-back
hyperplane class, equality of two restricted degree-\(b\) forms means
polynomial equality modulo the carrier equation. If the curves \(\Gamma_i\)
lie over a marked curve \(C\) with residue degrees \(f_i\), the generic
intersection multiplicity is
\[
 m_C=\sum_i f_i r_i.
\tag{5}
\]
For completeness, localize at the generic point of \(C\). The finite
normalization quotient has finite length. Multiplication by a proper
form on that quotient has kernel and cokernel of equal length. The
normalization exact sequence therefore identifies the length downstairs
with the sum of the valuation lengths upstairs, weighted by the residue
field degrees. Thus (4) controls actual intersection multiplicity whenever
the weights \(P\cdot\Gamma_i\) are known relative to \(f_i\).

Negative definiteness, complete divisor (1), and regularity along every
test curve are substantive hypotheses. A residual curve merely occurring
on a quadric does not establish them. This construction is not asserted
for arbitrary singular or reducible residual schemes.

### Checking negativity from the two quadric rulings

There is a useful test beyond disjoint residual curves. Suppose the setting
comes from the marked quartic on its smooth quadric, with complete divisor
\(\operatorname{div}(q)=\Gamma+\sum_jT_j\sim2H\), all coefficients one.
Assume the strict residual curves lie in the regular locus, map birationally
to their images of bidegree \((\alpha_j,\beta_j)\) on the quadric, and
have verified simple attachments giving
\(\Gamma\cdot T_j=C\cdot T_j=3\alpha_j+\beta_j\).
Then the row sum of their intersection matrix is
\[
 \sum_k M_{jk}=2H\cdot T_j-\Gamma\cdot T_j
 =\beta_j-\alpha_j.
\]
If \(\alpha_j\ge\beta_j\) for all \(j\), and each connected component
of the intersection graph contains a strict inequality, then \(M\) is
negative definite. Indeed
\[
 x^t(-M)x=\sum_j(\alpha_j-\beta_j)x_j^2+
 \sum_{j<k}M_{jk}(x_j-x_k)^2.
\]
Vanishing forces a constant on each graph component and then forces that
constant to be zero. This verifies the hypothesis of (2) even for
intersecting residual curves with the stated regularity and attachment
properties. A whole balanced component instead gives a nonzero null
vector, explaining exactly why this negativity test fails there. No such
attachment or Cartier hypotheses are inferred merely from bidegrees.

## Sharp half-contact bound on the ordinary full-source open

Work in characteristic zero with
\(C=[s^4:s^3t:st^3:t^4]\), its smooth quadric \(Q=V(q)\), and the
[nonempty full-source open](carrier_test_curves.md#3-a-nonempty-dense-open-subset-of-every-full-actual-source-is-excluded)
of degree-\(a\), order-\(m\) carriers, \(m\ge1\), \(a\ge3m\).
Precisely, the normal root is a smooth irreducible degree-\(m\) cover
of \(C\). The quadric restriction is \(mC+T\), where \(T\) has class
\((a-m,a-3m)\); for \(a>3m\) it is smooth irreducible, and for
\(a=3m\) it consists of \(2m\) disjoint nonendpoint ruling lines.
All attachments to \(C\) are transverse and correspond to simple normal
roots. The cited construction establishes these conditions on a nonempty
open of the actual homogeneous source, not the entire abstract symbol space.

These carriers are integral without an additional rank computation.
Every homogeneous factor restricts nontrivially to \(Q\). A factor not
containing \(C\) would restrict to a divisor supported only on \(T\).
In the irreducible case its bidegree is a multiple of the unequal pair
\((a-m,a-3m)\); in the critical case all its components lie in one ruling.
Neither can equal \((d,d)\) for a positive-degree factor. Every factor
therefore contains \(C\), whereas irreducibility of the generic normal
symbol permits only one such factor, with multiplicity one.

On the finite normalization, let \(\Gamma\) be the prime over \(C\),
of residue degree \(m\). The normalization is regular along the strict
transform of \(T\). Away from \(C\), the smooth reduced quadric
restriction makes the carrier smooth. At an attachment the simple normal
root selects a smooth sheet; transversality gives a reduced intersection
with \(\Gamma\). In particular the complete quadric divisor is
\[
 \operatorname{div}(\nu^*q)=\Gamma+T\sim2H.
\tag{6}
\]
The restriction to \(Q\) is exactly \(mC+T\), with \(T\) not containing
\(C\), so the order-\(m\) symbol is nonzero on the quadric direction.
In the generic blowup chart its reduced separable degree-\(m\) root
therefore makes \(q\) a uniformizer on the inverse branch. It also has
order one along the reduced residual. Finite normalization adds no divisorial
components over isolated points.

For \(a>3m\), the known bidegrees and attachments give
\[
 H\cdot T=2a-4m,\qquad \Gamma\cdot T=4a-6m,
 \qquad T^2=-2m.
\]
The last equality is (6) intersected with \(T\). Thus the correction is
\(P=H+(a-2m)T/m\). At \(a=3m\), each disjoint line has
\(H\cdot L=1\), \(\Gamma\cdot L=3\), \(L^2=-1\), so
\(P=H+\sum L\). In either case (3) reads
\(P\cdot\Gamma=2P\cdot H\). A proper degree-\(b\) containing form
therefore has generic branch order
\[
 r\le\lfloor b/2\rfloor,\qquad
 \boxed{m_C\le m\lfloor b/2\rfloor,\quad
 \deg R\ge ab-4m\lfloor b/2\rfloor.}
\tag{7}
\]
This explains the factor one-half: the corrected class annihilates precisely
the residual part of the quadric divisor, leaving twice the hyperplane
capacity on the single inverse prime.

The bounds are sharp for every \(b\ge2\): take \(q^{b/2}\) when
\(b\) is even, and \(q^{(b-1)/2}\ell\) when \(b\) is odd, with
\(\ell\) a linear form not vanishing identically on \(C\).
No linear form contains this nondegenerate curve. In even degree every
equality form is proportional to \(q^{b/2}\) modulo the carrier: (4)
is equality, and the uniqueness statement after it applies to the known
section \(q^{b/2}\). The low odd-degree window is classified below; no general odd-degree
equality classification is asserted.
These are sharp quantitative bounds on the stated open, not on its special
closed complement and not on all possible carriers.

### An actual-source description of low odd-degree maximizers

There is also a limited odd-degree classification on this same open. Write
\(b=2r+1\), with \(1\le r\le m\). A proper containing form has maximal
branch order \(r\) exactly when it belongs to the actual source
\[
 q^{r-1}H^0(\mathbf P^3,\mathcal I_C(3)).
\tag{8}
\]
The word proper excludes a form vanishing on the carrier.

Indeed if a form of branch order at least \(r\) had ordinary generic
normal order \(d<r\), its nonzero first symbol of degree \(d<m\)
would have to vanish on the irreducible degree-\(m\) normal root. That
is impossible over \(k(C)\). Thus its ordinary order is at least \(r\),
and it lies in the ideal-sheaf power \(\mathcal I_C^r\) globally:
successive lower symbols are sections of vector bundles on the integral
curve and vanish if they vanish generically. For \(r\ge2\), restriction
to the quadric in degree \(2r+1\) has quotient
\(\mathcal O_Q(r+1,1-r)\), with no global sections. The
[quadric flag sequence](../equations/global_equation_jets.md#exact-homogeneous-equation-spaces-and-fixed-quadric-restrictions)
therefore divides every such form by \(q\), leaving
\(H^0(\mathcal I_C^{r-1}(2r-1))\). Iteration gives exactly (8).
Conversely \(q\) has branch order one, and every cubic through \(C\)
has branch order at least one. A proper form in (8) consequently attains
order \(r\), since (7) rules out a larger order. This describes all
proper cubic maximizers when \(r=1\); it makes no classification claim
for odd degrees greater than \(2m+1\).

## Related boundary mechanisms

For the squarefree split graded family, the same correction applies separately
to each normalization component; the [full application](carrier_test_curves.md#a-sharp-residual-bound-for-the-split-graded-family) retains distinct branch orders, odd-characteristic attachments and necessary descent constraints.
The [fixed-sextic boundary valuation proof](../../results/ci_fixed_sextic_jet_rigidity.md) gives a complementary weighted boundary inequality with an exact nonnegative loss identity. Neither mechanism is asserted for an unspecified carrier without its geometric or regular-function hypotheses.
