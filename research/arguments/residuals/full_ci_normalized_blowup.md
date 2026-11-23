# The normalized blowup of a full complete intersection

This account owns the full-CI Rees blowup, with its setup stated below. For comparison, the [reduced-support two-blowup dictionary](blowup_residual_geometry.md#the-two-blowups-and-their-actual-global-section-dictionary) and [normalized carrier-branch comparison](blowup_residual_geometry.md#relation-to-actual-normalized-carrier-branches) concern different blowups.

## The normalized blowup of the full complete intersection

This is a different blowup from the blowup of the reduced quartic
support used above. Its center is the actual CI ideal. The following
component identity works in every characteristic and allows residual
components, nonreduced components and singular reduced supports.

Let \(Y=V(F_a,G_b)\subset\mathbf P^3\) be any proper complete
intersection over an algebraically closed field, and write
\[
[Y]=\sum_j m_j[C_j]
\]
for its irreducible reduced components and generic lengths. Put
\(B=\operatorname{Bl}_Y\mathbf P^3\), with exceptional Cartier
divisor \(E_Y\), and let \(\nu:\overline B\to B\) be its normalization.
This normalization is finite because B is of finite type over a field.
Write
\[
\nu^*E_Y=\sum_i\rho_iD_i,\qquad \rho_i>0.
\]
Every \(D_i\) maps onto an irreducible component \(E_{Y,j}\) of \((E_Y)_{\rm red}\).
Its center in P3 is C_j, never an isolated point. If
\(f_i=[k(D_i):k(E_{Y,j})]\) for this finite map, then
\[
\boxed{\quad
\sum_{i:\,\nu(D_i)=E_{Y,j}}\rho_i f_i=m_j
\quad\text{for every }j.
\quad}                                                     \tag{14}
\]
The degrees include any inseparable part.

**Proof.** The regular immersion gives
\[
E_Y=\operatorname{Proj}_Y\operatorname{Sym}(\mathcal I_Y/\mathcal I_Y^2).
\]
Thus \(E_Y\) is a projective-line bundle over the full nonreduced Y.
Each \(E_{Y,j}\) is the corresponding projective-line bundle over C_j,
and its coefficient in \([E_Y]\) is \(m_j\). Locally this is just
preservation of the generic Artinian length after a purely
transcendental residue-field extension. No smoothness of C_j
is needed. A finite morphism preserves the dimension of each
closed integral subvariety, so a divisor D_i cannot map into
a fiber or a point of \(E_Y\). Finally the projection formula for
the exceptional Cartier divisor and the finite birational
normalization gives
\[
\nu_*[\nu^*E_Y]=[E_Y].
\]
Comparing coefficients proves (14). The regular-embedding
description is recalled in [Aluffi, §2.2](https://www.math.fsu.edu/~aluffi/archive/paper569.old.pdf).
The same proof applies to an lci curve in any smooth
threefold of finite type over a field. \(\square\)

Consequently,
\[
\sum_i\rho_i f_i\deg C_{j(i)}=ab.                         \tag{15}
\]
For a distinguished component C0, the genuine residual degree is
\[
\deg R=\sum_{j(i)\ne C_0}\rho_i f_i\deg C_{j(i)}.
\tag{16}
\]
These are the existing component degrees expressed on the
normalized blowup, not new lower bounds. Further log resolutions
can introduce divisors centered at points. Equation (14) does
not forbid those valuations or remove punctual defects; it
distinguishes them from the divisors of this normalized blowup
and from residual components downstairs.

### The exceptional-coefficient positivity bound

Over \(\mathbf C\), [Ein–Lazarsfeld, Proposition 3.1](https://arxiv.org/pdf/math/9810004)
applies to an ideal J with \(J\otimes L\) globally generated and
L nef on a smooth projective variety. In dimension three it gives
\(\sum_i\rho_i\deg_L C_{j(i)}\le L^3\), retaining repeated centers.
For \(J=\mathcal I_Y\), \(a\le b\), take \(L=\mathcal O(b)\).
The stronger elementary inequality is already
\[
\sum_i\rho_i\deg_L C_{j(i)}
\le b\sum_i\rho_i f_i\deg C_{j(i)}
=ab^2\le b^3.                                           \tag{17}
\]
Thus the redundancy holds for every proper pair, before imposing
sole support. In the STCI case (14) reads
\(\sum_i\rho_i f_i=ab/4\); the published bound only gives
\(\sum_i\rho_i\le b^2/4\).

Their Remark 3.2 subtracts the number \(n_{\rm out}\) of common points
outside Y of three general sections of \(\mathcal I_Y(b)\).
Here \(n_{\rm out}=b(b-a)^2\). For b>a, write these sections as
\(A_\ell F+\lambda_\ell G\); eliminating G twice gives two
general degree-(b-a) equations, and the remaining equation
has degree b. Their complete intersection avoids Y and has
the displayed degree. For a=b the section space is a pencil,
so \(n_{\rm out}=0\). The improved right side is therefore
\[
b^3-n_{\rm out}=ab(2b-a)\ge ab^2,
\]
still weaker than (17). This \(n_{\rm out}\) counts a different three-section intersection;
it is neither the original residual R nor the generic transverse
Milnor number in the [pencil identity](../carriers/pencil_milnor_budget.md).

Geometrically, normalization distributes each full CI component's
transverse length among exceptional multiplicities and finite
covering degrees. The checked positivity theorem bounds a sum
that is already controlled by that distribution. It supplies
neither an upper limit on later contact nor a positive residual
degree, and does not strengthen the surviving-contact estimate
above. No valuation-tree classification follows.
