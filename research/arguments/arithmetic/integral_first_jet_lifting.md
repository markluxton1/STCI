# Integral first equation jets and supported mixed-characteristic traits

**Review (November 23, 2026).** Independent correctness reconstruction checked
the integral residue identity, the product of the two first-jet coefficient
ideals, the trait valuation consequence, the non-eigen \((16,p)\) application,
and the differential calculation on the ramified \((7,8)\) control. The
characteristic-zero matrix/residue formula is inherited from
[the Hilbert-scheme calculation](../torus/chow_hilbert_symplectic_form.md#1-an-exact-pullback-formula).
No finite-Witt-vector extension is asserted here.

## The integral source identity

Write \((z,x,y,w)=(x_0,x_1,x_2,x_3)\) and let \(L=V(z,w)\).
Take the universal pair of homogeneous forms of degrees \((a,b)\), on the
integral open where their binary restrictions \(f_0,g_0\) have invertible
resultant. The intersection is finite flat over the \((z,w)\)-plane. On
homogeneous basis charts let \(X,Y\) be the commuting multiplication
matrices of \(x,y\), and differentiate only in \(z,w\), holding all
equation coefficients fixed. Write
\[
 \begin{aligned}
 F&=f_0+zp+wq\pmod{(z,w)^2},\\
 G&=g_0+zr+ws\pmod{(z,w)^2}.
 \end{aligned}
\]
Here \(p,q\) are binary forms of degree \(a-1\), and \(r,s\) have
degree \(b-1\). Then
\[
 \boxed{\quad
 \operatorname{Tr}(dX\wedge dY)
   =\Theta(F,G)\,dz\wedge dw,\qquad
 \Theta(F,G)=\operatorname{Res}_{f_0,g_0}(ps-qr).
 \quad}                                                     \tag{IJ1}
\]
This is an identity over the universal coefficient ring over \(\mathbf Z\),
and therefore persists under its base changes. It does not require a
translated cycle, curve containment, or a symmetric ideal.

**Proof.** The residue functional is integral. On
\(\mathbf P^1\) over the resultant-open coefficient ring, use the twisted
binary Koszul sequence
\[
 0\longrightarrow\mathcal O(-2)
 \longrightarrow\mathcal O(b-2)\oplus\mathcal O(a-2)
 \longrightarrow\mathcal O(a+b-2)\longrightarrow0.
\]
Its connecting map followed by the Serre trace on
\(H^1(\mathcal O(-2))\) defines the residue. Choose the orientation with
\(\operatorname{Res}_{x^a,y^b}(x^{a-1}y^{b-1})=1\).
No integer, including \(2\), \(a\), or \(b\), is inverted.

Homogeneous basis charts invert only coefficient minors; their universal
rings are localizations of polynomial rings over \(\mathbf Z\), hence
torsion-free. The matrix differential is independent of the basis because
\(X,Y\) commute. Grading makes its coefficient constant in \(z,w\): both
the trace form and \(dz\wedge dw\) have total degree two. In characteristic
zero, the established matrix/residue identity and evaluation at \(z=w=0\)
give (IJ1). Both sides are regular over the integral basis chart, so
torsion-freeness proves the equality before tensoring with \(\mathbf Q\).
The basis-independent identities agree on overlaps. \(\square\)

Let \(\mathfrak l_F\) be the ideal of coefficients of \(p,q\), and
\(\mathfrak l_G\) the ideal of coefficients of \(r,s\). Linearity of the
integral residue in its numerator gives the stronger source statement
\[
              \boxed{\Theta(F,G)\in\mathfrak l_F\mathfrak l_G.}
                                                               \tag{IJ2}
\]
Each equation must therefore supply a first base-normal jet to make this
differential nonzero. This specifies two actual homogeneous source ideals,
rather than the union of all coefficients breaking a torus symmetry.

## The necessary equation on an actual supported trait

Let \(R\) be a mixed-characteristic DVR with uniformizer \(\pi\), residue
characteristic \(p\), and fraction field \(K\). Let \(F,G\) be homogeneous
forms over \(R\), with the binary resultant above a unit. Assume their
characteristic-zero generic intersection has sole geometric reduced support
the fixed quartic \(C_0\). Its generic multiplicity is \(m=ab/4\).
Let \(L_F,L_G\subset R\) be the evaluated first-jet coefficient ideals.
Then
\[
 \boxed{\qquad \frac{ab}{2}=2m=\Theta(F,G)\in L_F L_G.\qquad}    \tag{IJ3}
\]
Indeed, on the characteristic-zero generic fiber the
[full-cycle formula](../torus/chow_acm_parity_vanishing.md#2-a-basis-independent-matrix-differential)
is \(\operatorname{Tr}(dX\wedge dY)=2m\,dz\wedge dw\), including generic
nilpotents. Injectivity of \(R\to K\) returns this equality to \(R\), and
(IJ2) applies. In particular both ideals are nonzero and
\[
 \boxed{\quad
 v_\pi(L_F)+v_\pi(L_G)\le v_\pi(ab/2)
 =v_\pi(p)\bigl(v_p(ab)-[p=2]\bigr).
 \quad}                                                     \tag{IJ4}
\]
The bracket is the ordinary integer indicator. Proper special support on
\(C_0\) guarantees the required unit resultant, since the projection center
\(L\) misses \(C_0\).

For the sign action \(\tau(z,w,x,y)=(z,w,-x,-y)\), every first-jet
coefficient has the opposite sign from the corresponding binary restriction.
Thus \(L_F,L_G\) are contained in the respective ideals of coefficients
breaking those signs. The actual first-jet product is the more precise
condition. In residue characteristic two the reduced action of \(\tau\)
is the identity; (IJ3)--(IJ4) still follow from the integral identity and
the characteristic-zero generic fiber. They are not deduced from a
characteristic-two sign decomposition.

No assertion that nilpotent matrices over an Artin ring have zero trace
enters this proof. Replacing the actual trait by a finite lift would require
an additional justification of the full-cycle equality over that base.

## A non-eigen source detected by the first jets

Consider the actual non-binomial degree-\((16,p)\) construction for
\(p\ge43\) in
[the equation-source owner](arithmetic_equations_and_jet_gaps.md#4-explicit-degree-p-mates-and-exact-minimum-for-p-at-least-43).
Its first equation is
\[
 A=x_0^3x_3-x_1^4,\qquad B=x_0^2x_2-x_1^3,\qquad
 F=A^4-x_0^{13}B.
\]
It satisfies \(F\equiv x_1^{16}\pmod{(x_0,x_3)^2}\). The displayed
mate \(G_p=x_2^p-P_p\) also has no first base-normal jets. In the owner's
notation, a term of \(P_p\), with \(j=4h+\ell\), \(0\le\ell<4\),
has base order at least
\[
 E+n-3h-4\ell
 \ge E+\frac n4-\frac{13\ell}4
 \ge E+\frac n4-\frac{39}4>1.
\]
Here \(4h+\ell\le n\), \(E\ge9\), and \(n\ge32\). Expanding
\(A,B\) can only increase that base order. Hence
\(G_p\equiv x_2^p\pmod{(x_0,x_3)^2}\).

For any actual supported trait through this specified special pair,
\(L_F,L_G\subset(\pi)\), whereas \(ab/2=8p\). Formula (IJ4) forces
\[
                         v_\pi(p)\ge2.                       \tag{IJ5}
\]
In particular there is no unramified supported trait through these points,
even when both lifted equations vary arbitrarily. This application does
not assume either special equation is a torus eigenform. Arbitrary
ramification remains unresolved; no strong \(W_2\) nonlifting or exact
finite-precision result for this source is claimed.

## Relation to the earlier trace test

For odd residue characteristic, (IJ3) implies the previous quadratic
valuation bound near eigenpairs, and retains the separate depths of the
two first-jet ideals. The older trace theorem has its own independently
proved strong \(W_2\) statement under its additional hypotheses. Neither
result supplies a supported trait when its necessary valuations permit one.

The [ramified degree-\((7,8)\) control](mixed_characteristic_trace_obstruction.md#a-ramified-pair-that-passes-the-first-trace-and-retains-residual-support)
has zero entire first scalar trace but fails (IJ3). The difference is
substantive: scalar trace and this matrix differential encode the same
moment only after the entire translated-cycle hypothesis is established.
