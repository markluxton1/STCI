# Canonical projection sections and their endpoint poles

**Status, October 31, 2026: independently reviewed theorem and
local control.** Over an algebraically closed field, fix
\(C=[s^4:s^3t:st^3:t^4]\), and let \(Z=V(F_a,G_b)\) be a proper
homogeneous complete intersection with \(Z_{\mathrm{red}}=C\). Write
\(m=ab/4\). This note applies in characteristic zero or odd characteristic;
it does not require \(p\nmid m\).

The [finite projection algebra](../torus/fixed_surface_and_endpoint_algebras.md)
gives a finite flat map \(\pi:Z\to B=\mathbf P^1\) by \([x_0:x_3]\),
of rank \(ab=4m\). Its reduction is
\(f:C\to B\), \([s:t]\mapsto[s^4:t^4]\). Set
\(\mathcal E=\pi_*\mathcal O_Z\), \(\mathcal R=f_*\mathcal O_C\),
and let \(0,\infty\in B\) denote the two branch points.

## The section over the unramified open and a uniform pole bound

On \(B^\circ=B\setminus\{0,\infty\}\), there is a unique
\(\mathcal O_{B^\circ}\)-algebra section
\[
 \sigma:\mathcal R|_{B^\circ}\longrightarrow\mathcal E|_{B^\circ}
\]
of the nilpotent quotient \(\mathcal E\twoheadrightarrow\mathcal R\).
Indeed \(f\) is finite étale there, so its algebra lifts uniquely across
nilpotent ideals by [formal étaleness](https://stacks.math.columbia.edu/tag/00UP).

Viewed as a rational map of vector bundles, this section has pole order at
most \(m-1\) at each branch point:
\[
 \boxed{\sigma(\mathcal R)\subset
 \mathcal E\bigl((m-1)(0+\infty)\bigr).}
\tag{1}
\]
The twist in (1) is a statement about modules inside the meromorphic
algebra. It is not an algebra structure on the twisted vector bundle or a
regular algebra section across the branch points.

To prove (1), put \(\mathcal N=\mathcal I_C\mathcal O_Z\).
At the generic point of \(C\), the transverse Artin algebra has length
\(m\), so \(\mathcal N^m=0\) there. Any residual image of
\(\mathcal N^m\) would be a finite-support submodule of the pure
one-dimensional Cohen–Macaulay sheaf \(\mathcal O_Z\), which is impossible.
Thus \(\mathcal N^m=0\) everywhere on \(Z\).

On \(x_0=1\), write \(z=x_3\), \(x=x_1\), and \(r=z-x^4\).
Then \(r\in\mathcal N\) and \(r^m=0\). On \(z\ne0\), \(x\)
is invertible, since \(x^4=z-r\). The image of the reduced parameter
\(t\) under \(\sigma\) is
\[
 T=x\left(1+\frac r{x^4}\right)^{1/4}
   =\sum_{h=0}^{m-1}\binom{1/4}{h}x^{1-4h}r^h.
\tag{2}
\]
The coefficients are interpreted in \(\mathbf Z[1/2]\), not by dividing
by \(h!\) in the ground field. The unique formal solution
\(H(v)^4=1+v\), \(H(0)=1\), is constructed recursively by division only
by four. It lies in \(\mathbf Z[1/2][[v]]\), and over \(\mathbf Q\)
its coefficients are the displayed binomial coefficients. Hence (2) is
valid in every odd characteristic, even when \(p\le m\).

It satisfies \(T^4=z\) and reduces to \(x\) on \(C\), so formal
étaleness identifies it with the canonical section. Locally at zero,
\(\mathcal R\) has basis \(1,t,t^2,t^3\) over \(\mathcal O_B\).
For \(j=1,2,3\), the identities below are taken in the
nilpotent algebra, not in an ordinary function-field extension:
\[
 z^{m-1}T^j=
 \sum_{h=0}^{m-1}\binom{m-1+j/4}{h}
 x^{4(m-1)+j-4h}r^h.
\tag{3}
\]
All exponents of \(x\) are nonnegative. The same recursive-root argument
puts these coefficients in \(\mathbf Z[1/2]\). Thus every basis vector
has pole order at most \(m-1\) in the base coordinate \(z\).
At infinity use \(x=x_2/x_3\), \(z=x_0/x_3\), and the reduced parameter
\(s/t\). The identical argument proves the other endpoint bound.
Uniqueness makes the two sections agree on the overlap.


## The canonical projection order

**Scoped independent reconstruction (November 23, 2026).** The order construction,
normalization sequence, splitting and both bounds below were independently
checked against the actual finite-cover hypotheses. The rational section above
has a canonical saturated order inside the actual finite algebra. This
packages the two endpoint failures into one global object rather than two
separate pole calculations.

Put \(K=k(B)\).  Extend the unique section on \(B^\circ\) to the generic
point,
\[
 \sigma_K:\mathcal R_K\hookrightarrow\mathcal E_K,
\]
and define, sheafwise on \(B\),
\[
 \boxed{\mathcal A=
 \mathcal E\cap\sigma_K(\mathcal R_K)\subset\mathcal E_K.}
 \tag{4a}
\]
Equivalently, \(\mathcal A\) is the saturation in \(\mathcal E\) of the
image of \(\mathcal R|_{B^\circ}\).  Then:

1. \(\mathcal A\) is a finite locally free rank-four
   \(\mathcal O_B\)-subalgebra of \(\mathcal E\), equal to
   \(\sigma(\mathcal R)\) over \(B^\circ\).
2. Reduction \(\rho:\mathcal E\twoheadrightarrow\mathcal R\) restricts
   injectively to \(\mathcal A\).  Via this map,
   \[
      \mathcal O_B\subset\mathcal A\subset\mathcal R,
      \qquad
      \mathcal R/\mathcal A
      \text{ is supported on }\{0,\infty\}.             \tag{4b}
   \]
3. If
   \[
      \delta=\operatorname{length}_B(\mathcal R/\mathcal A),
   \]
   then the finite curve \(C_{\mathcal A}=\operatorname{Spec}_B\mathcal A\)
   is an integral rational curve whose normalization is \(C\), and
   \[
      \boxed{p_a(C_{\mathcal A})=\delta.}                \tag{4c}
   \]
4. For every hypothetical supported complete intersection with
   \(a,b\ge2\),
   \[
      \boxed{1\le\delta\le6(m-1).}                       \tag{4d}
   \]

Here the lower bound is the global missing-section obstruction in a
normalization/order form; it is not a new STCI exclusion.  The upper bound
is the endpoint pole theorem above.

**Proof.**  On the smooth base curve, the intersection in (4a) is a
coherent torsion-free lattice of rank four, hence locally free.  It contains
the unit and is closed under multiplication because both
\(\mathcal E\) and \(\sigma_K(\mathcal R_K)\) are subalgebras of
\(\mathcal E_K\).  Since
\(\rho_K\circ\sigma_K=\mathrm{id}_{\mathcal R_K}\), the kernel of
\(\rho|\mathcal A\) is generically zero.  Torsion-freeness makes it zero
everywhere, proving (4b).  The identified algebra is a subalgebra of the
normal integral algebra \(\mathcal R\) with the same function field and is
equal to it away from the two marked points.  Thus
\(C\to C_{\mathcal A}\) is its finite normalization.  This is the standard
normalization/order situation; compare
[Stacks, normalization](https://stacks.math.columbia.edu/tag/0BXR).

The normalization sequence
\[
 0\longrightarrow\mathcal A\longrightarrow\mathcal R
 \longrightarrow\mathcal Q\longrightarrow0,
 \qquad \operatorname{length}\mathcal Q=\delta,
\]
has \(\chi(\mathcal R)=\chi(\mathcal O_C)=1\).  Since
\(C_{\mathcal A}\) is integral and proper,
\(H^0(C_{\mathcal A},\mathcal O)=k\), so
\(\chi(\mathcal A)=1-\delta\) gives (4c).  This is the usual
normalization-defect formula for the arithmetic genus.

For the lower bound, first determine the fixed reduced algebra bundle.
Projection formula and the degree-four map give
\[
 \mathcal R=f_*\mathcal O_C
 \simeq\mathcal O_B\oplus\mathcal O_B(-1)^{\oplus3}.    \tag{4e}
\]
Indeed the unit splits off \(\mathcal O_B\): in the present
characteristic \(4\) is invertible, so one quarter of the finite-cover trace
is an \(\mathcal O_B\)-linear retraction onto the unit summand.
Moreover
\(\deg\mathcal R=\chi(\mathcal O_C)-4\chi(\mathcal O_B)=-3\), while
\(h^0(\mathcal R)=1\) forces the remaining three summands to have negative
degree.  Their degrees therefore sum to \(-3\), so each is \(-1\).
Hence
\[
 \deg\mathcal A=\deg\mathcal R-\delta=-3-\delta.        \tag{4f}
\]
On the other hand the actual CI cover has
\[
 \mathcal E\simeq
 \bigoplus_{0\le i<a,\ 0\le j<b}\mathcal O_B(-i-j).
\]
For \(a,b\ge2\), the four largest summand degrees are
\(0,-1,-1,-2\).  Since
\(\det\mathcal A\hookrightarrow\bigwedge^4\mathcal E\), and the largest
line-bundle degree occurring in that exterior power is \(-4\),
\[
 \deg\mathcal A\le-4.
\]
Together with (4f) this gives \(\delta\ge1\).  Equality
\(\delta=0\) would be exactly a regular algebra section and hence the
pencil-compatible retraction already excluded by the missing fifth
hyperplane section.

For the upper bound, work at either marked point with base uniformizer
\(z\) and normalized basis \(1,t,t^2,t^3\) of \(\mathcal R\).  Equations
(2)--(3) show
\[
 1,\quad z^{m-1}t,\quad z^{m-1}t^2,\quad z^{m-1}t^3
 \in\mathcal A
\]
under the identification (4b).  The sublattice generated by these four
elements has index \(3(m-1)\) in \(\mathcal R\).  Therefore the local
normalization defect is at most \(3(m-1)\) at each end, giving
\(\delta\le6(m-1)\).

The conductor
\[
 \mathfrak c=\operatorname{Ann}_{\mathcal A}
             (\mathcal R/\mathcal A)
\]
is a canonical ideal equal to \(\mathcal A\) away from the endpoints.
The finite-length quotients \(\mathcal A/\mathfrak c\) and
\(\mathcal R/\mathfrak c\), and the finer elementary divisors,
may retain information lost by the scalar
\(\delta\).  No bound here connects them to residual projective support;
the local model below shows that large endpoint pole defects are compatible
with local complete intersections.  The value of \(\mathcal A\) is instead
that it is one global algebra built from the same actual pair and both
endpoints, so any future comparison with the two equation filtrations has
a canonical target.

## A local complete intersection with the full pole order

For \(m\ge2\), let
\[
 A=k[[z]],\qquad
 B_m=A[x]/\bigl((x^4-z)^m\bigr).
\tag{4}
\]
This is finite free of rank \(4m\) over \(A\), by its monic equation.
It is a local complete intersection with smooth reduced support
\(A[x]/(x^4-z)\simeq k[[x]]\). It can also be realized as a codimension-two
local complete intersection by adjoining a variable \(y\) and the equation
\(y=0\). Put \(r=z-x^4\); as a completed local ring it is
\(k[[x,r]]/(r^m)\).

The section over \(z\ne0\) is (2). For \(m=2\),
\[
 T=x+\frac{r}{4x^3}.
\]
It does not extend over zero in any odd characteristic. An integral lift
of the reduced parameter would be \(x+r h(x)\); its fourth power equals
\(z=x^4+r\) only if \(4x^3h(x)=1\), impossible in \(k[[x]]\).
Thus even a generically double, locally split thickening with \(p>2\)
need not admit a section over the ramified projection base.

More generally the pole bound \(m-1\) is exact for (4) in characteristic
zero and in characteristic \(p>4m\). Expanding
\[
 z^{m-2}T=
 \sum_{h=0}^{m-1}\binom{m-2+1/4}{h}
 x^{4(m-2)+1-4h}r^h
\tag{5}
\]
gives a last term
\(\binom{m-2+1/4}{m-1}x^{-3}r^{m-1}\).
Its coefficient is nonzero in the stated characteristics: its numerator
factors are nonzero integers of absolute value below \(4m\), and its
denominator divides \(4^{m-1}(m-1)!\). Earlier terms have nonnegative
\(x\)-exponents. Uniqueness of the \(r\)-expansion in
\(k((x))[r]/(r^m)\) therefore proves that (5) is not in \(B_m\).

## Consequence for the degree-growth strategy

The canonical unramified section and its bound (1) are available for
arbitrary actual supported pairs. They do not force a regular global
retraction. The local model attains the pole bound even for arbitrarily
large characteristic compared with its transverse length; tameness alone
cannot remove this endpoint obstruction. This is a local control, not a
projective STCI construction for the quartic.

Likewise a nonzero Artinian complete-intersection Jacobian does not imply
curvilinearity: \(k[u,v]/(u^2,v^2)\) has nonzero socle generator \(4uv\)
in every odd characteristic and has embedding dimension two. The
[tame Jacobian conclusions](../torus/contact_jacobians_and_hamiltonian_actions.md#exact-characteristic-boundaries)
therefore cannot reduce all pairs to the curvilinear case. No identification
of the section's pole defect with a saturated normal-filtration socle
divisor is made; such a comparison would require a separate proof.
