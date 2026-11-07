# Canonical projection sections and their endpoint poles

**Status, October 31, 2026: independently reviewed theorem and
local control.** Over an algebraically closed field, fix
\(C=[s^4:s^3t:st^3:t^4]\), and let \(Z=V(F_a,G_b)\) be a proper
homogeneous complete intersection with \(Z_{\mathrm{red}}=C\). Write
\(m=ab/4\). This note applies in characteristic zero or odd characteristic;
it does not require \(p\nmid m\).

The [finite projection algebra](../synthesis/fixed_surface_and_endpoint_algebras.md)
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
For \(j=1,2,3\),
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
[tame Jacobian conclusions](../synthesis/contact_jacobians_and_hamiltonian_actions.md#exact-characteristic-boundaries)
therefore cannot reduce all pairs to the curvilinear case. No identification
of the section's pole defect with a saturated normal-filtration socle
divisor is made; such a comparison would require a separate proof.

## Independent review

An independent reconstruction accepted the canonical section, the
arbitrary-pair bound (1), and the exact local pole order in the stated
characteristics. It checked purity and global nilpotence, the integral
recursive fourth root without factorial inversion, the base-coordinate
pole order and the module-versus-algebra distinction, and local sharpness
through the last nonzero nilpotent coefficient. It also checked the
noncurvilinear Jacobian example. No global homogeneous STCI realization or
identification with a normal-filtration defect is asserted or reviewed.
