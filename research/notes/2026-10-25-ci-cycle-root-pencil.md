# A root pencil through the four-quartic configuration

Date: 2026-10-25. **Exploratory contribution; not canonically promoted.**
This note studies actual complete intersections containing the fixed embedded
curve, and introduces a small laboratory for contact, component multiplicity,
and a possible elliptic moduli invariant. It is not an STCI argument.

## Inputs, conventions, and status

Work over an algebraically closed field of characteristic zero until a change
is explicitly stated. Let

\[
C=[s^4:s^3t:st^3:t^4],\quad
F=x_1^4-x_0^3x_3,\quad
G=x_2^4-x_0x_3^3,\quad Q=x_0x_3-x_1x_2.
\]

The established input is [STCI-R-0021](../results/quartic_mu4_degeneration.md),
with its [source discussion](2026-10-23-quartic-characteristic-conormal.md):
\(V(F,G)\) is the reduced union of the four \(C_\zeta\) in characteristic
zero and has reduced support \(C\), generic multiplicity four, in
characteristic two. The common ruled-surface picture in
[the October 24 synthesis](2026-10-24-p4-ruled-surfaces-synthesis.md) is
reviewed provisional evidence; none of its global claims is needed below.

The family, discriminant, and elliptic interpretation below are fresh
exploratory calculations. The [exact verifier](../computations/verify_ci_cycle_root_pencil_2026_10_25.py)
and its [JSON output](../computations/ci_cycle_root_pencil_2026_10_25.json)
check thirteen polynomial identities using Python's standard library. Those
identities do not themselves prove any global extremality principle.
Independent notebook review is recorded separately by the notebook owner.

## 1. A deformation that keeps the four sheets

Consider the actual homogeneous quartics

\[
G_a=G+a x_3^2Q
=x_2^4-a x_1x_2x_3^2+(a-1)x_0x_3^3.
\tag{1}
\]

Every \(G_a\) vanishes on \(C\). On \(x_0=1\), put \(u=x_1\), \(y=x_2\)
and eliminate \(x_3=u^4\) using \(F\). Then

\[
G_a=y^4-a u^9y+(a-1)u^{12}.
\]

For \(u\ne0\), the substitution \(y=zu^3\) gives the root polynomial

\[
f_a(z)=z^4-a z+a-1
=(z-1)(z^3+z^2+z+1-a).
\tag{2}
\]

The marked root \(z=1\) is exactly the retained curve \(C\). Each other
root \(\lambda\ne0\) gives the smooth rational quartic

\[
C_\lambda=[s^4:s^3t:\lambda st^3:t^4].
\]

If all four roots are distinct and nonzero, these curves are projectively
equivalent by scaling \(x_2\), and their union exhausts the complete
intersection by degree and complete-intersection purity. This is a
four-sheet family, not a picture of exceptional fibers.

The affine family is flat. Over \(k[a,x_0,x_3]\), use a monomial order in
\(x_1,x_2\) refining total degree; the two monic relations have leading
monomials \(x_1^4,x_2^4\). The relatively prime leading monomials give a
monic Gröbner basis and the quotient is free on
\(x_1^ix_2^j\), \(0\le i,j<4\). In particular, every graded piece is
flat over \(k[a]\). Projectivizing the pencil adds the member at infinity;
every member remains a proper \((4,4)\) intersection, so the same Hilbert
polynomial persists there.

One could initially suspect that the \(\mu_4\) arrangement is isolated among
four smooth conjugate quartics with two concentrated contact points. This
family shows a continuous deformation of precisely that picture.
The roots of unity are a symmetric point within it.

## 2. The boundary stays fixed while the roots move

At \(p=[1:0:0:0]\), the surface \(F=0\) is smooth. Branches are
\(y=\lambda u^3\); distinct roots have pairwise intersection multiplicity
three. At \(q=[0:0:0:1]\), \(G_a=0\) is smooth whenever \(a\ne1\), because
its derivative with respect to \(x_0\) is \(a-1\). Using \(x_2\) as a local
parameter, the curves have

\[
x_1=\lambda^{-3}x_2^3,\qquad x_0=\lambda^{-4}x_2^4.
\]

The coefficients \(\lambda^{-3}\) are distinct for distinct roots when
\(a\ne1\). Indeed, if \(\eta=\omega\lambda\), \(\omega^3=1\), equations
\(f_a(\lambda)=f_a(\eta)=0\) imply
\((1-a)(\omega-1)=0\). Thus all six pair contacts at each endpoint
remain three throughout the open four-smooth-component locus.

Each component has conductor boundary \(9p+9q\). Both endpoint delta
invariants remain eighteen. In particular, this boundary and the total
delta invariant cannot recover the root arrangement.

Along the marked \(C\), the first-normal determinant has the particularly
simple parameter dependence

\[
\det(dF,dG_a)|_C\ \doteq\ (4-a)s^9t^9.
\tag{3}
\]

Here \(\doteq\) allows a fixed nonzero scalar and a choice of determinant
trivialization. On the first chart it is the derivative
\(\partial G_a/\partial y|_{y=u^3}=(4-a)u^9\). The homogeneous determinant
is a section of \(\mathcal O_{\mathbf P^1}(18)\). For \(a\ne4\) its divisor
is always \(9p+9q\). At \(a=4\) the section is zero everywhere; it has no
finite zero divisor there.

This suggests keeping two distinct data: the **location and order of
contact on the base curve**, and the **configuration of separated sheets
seen after resolving that contact**.

## 3. Three ways the pencil leaves the open arrangement

The polynomial discriminant is

\[
\operatorname{disc}(f_a)
=256(a-1)^3-27a^4
=(a-4)^2(-27a^2+40a-16).
\tag{4}
\]

The exceptional parameters have different geometric meanings.

* **\(a=4\): collision with the marked sheet.** Here
  \[
  f_4(z)=(z-1)^2(z^2+2z+3).
  \]
  The fundamental cycle is
  \[
  2C+C_{-1+i\sqrt2}+C_{-1-i\sqrt2}.
  \]
  This is an explicit characteristic-zero deformation that transfers
  one quartic's worth of residual degree onto \(C\). The reduced support
  has three quartics; its conductor boundary on the marked component
  would be \(6p+6q\), whereas the full nonreduced scheme has the original
  Hilbert polynomial. The old \(9p+9q\) formula must not be applied to
  this reduced support.
* **\(27a^2-40a+16=0\): collision among residual sheets.** These parameters
  are \((20\pm4i\sqrt2)/27\). The marked root is simple, while two residual
  roots coincide. Equation (3) still supplies the degree-eighteen
  determinant boundary, even though the total curve is nonreduced.
* **\(a=1\): a root reaches zero.** Then \(f_1(z)=z(z^3-1)\); the root
  polynomial remains separable. But \(C_0\), interpreted here as the
  \(\lambda=0\) member rather than the repository name for the fixed
  quartic, has parametrization \([s^4:s^3t:0:t^4]\). It is a plane quartic
  with a \((3,4)\) cusp at \(q\), not a smooth conjugate of \(C\).
  Thus a root discriminant alone misses a geometric boundary of the
  embedded four-smooth-component arrangement.

At the projective pencil parameter **\(a=\infty\)**, the second equation is
\(x_3^2Q\). This gives a more drastic boundary, with cycle

\[
[C]+3[L_a]+9[L_d],\qquad
L_a=V(x_0,x_1),\quad L_d=V(x_1,x_3).
\tag{5}
\]

One can see this directly on \(Q\): write
\(x_0=ac,x_1=ad,x_2=bc,x_3=bd\), temporarily using \(a,b,c,d\) as Segre
coordinates unrelated to the pencil parameter. Then
\(F=a^3d(ad^3-bc^3)\); the last factor cuts out \(C\), giving
\(F\cap Q=C+3L_a+L_d\). Also \(F\cap\{x_3=0\}=4L_d\), so the doubled
plane contributes another \(8L_d\). The two residual lines meet at
\([0:0:1:0]\), away from \(C\).

The determinant boundary along \(C\) is still \(9p+9q\) at this infinity
member. A fixed boundary can coexist with changes from three smooth
residual quartics to two lines with large multiplicities and additional
incidence away from \(C\). This is a useful limitation, not a reason to
abandon the boundary viewpoint.

## 4. An elliptic curve hidden in the separated sheet configuration

Resolving the common order-three tangency exposes four marked directions
with coordinates \(\lambda\). Their unordered cross-ratio is summarized
by the double cover

\[
E_a:\quad w^2=f_a(z).
\tag{6}
\]

When the discriminant is nonzero this has a smooth projective completion
of genus one. The root \(z=1\) supplies a rational branch point, hence an
elliptic origin after completion. Its modulus is

\[
j(E_a)=1728\,
\frac{256(a-1)^3}{256(a-1)^3-27a^4}.
\tag{7}
\]

For a quick independent derivation, put \(z=1+1/x\) and
\(y=w/(z-1)^2\). The equation becomes

\[
y^2=(4-a)x^3+6x^2+4x+1.
\]

For \(b=4-a\ne0\), set \(X=bx,Y=by\). The cubic is
\(Y^2=X^3+6X^2+4bX+b^2\), with
\(c_4=192(a-1)\), \(c_6=-864a^2\), and
\(\Delta_E=16\operatorname{disc}(f_a)\), giving (7).
Classical binary-quartic invariants also yield this directly: here
\(I=12(a-1)\) and \(J=-27a^2\). The normalization of \(I,J\) and their
quartic discriminant is documented in
[Bhargava–Shankar, pp. 195–196](https://annals.math.princeton.edu/wp-content/uploads/annals-v181-n1-p03-p.pdf).
The calculation here concerns only their elementary invariant formulas.

At the distinguished member, \(a=0\), one has \(j=1728\). Thus the
square of fourth roots of unity gives the elliptic double cover with
extra order-four symmetry. At \(a=1\), one has \(j=0\), despite the
singular embedded \(\lambda=0\) quartic. At \(a=4\) and the two residual
collision parameters, \(E_a\) degenerates.

**Interpretation to explore.** The endpoint boundary measures how much
contact was compressed, whereas the elliptic modulus measures the
relative positions of sheets after that contact has been separated.
The distinguished arrangement is a symmetry point in this moduli
coordinate, and a continuous family shares its boundary. One should not
claim from this that an elliptic curve is canonically attached to every
complete intersection containing \(C\). In this laboratory we chose the
fixed carrier \(F\), the order-three separation, and one endpoint.
The two endpoints do supply the same modulus on this open pencil. Indeed,
for a root \(\lambda\),
\[
\lambda^{-3}=\frac{\lambda}{a\lambda+1-a}.
\]
For \(a\ne1\) this is a Möbius transformation of the coefficient line,
so the four \(\lambda\) and the four \(\lambda^{-3}\) have the same
unordered cross-ratio. How this agreement changes when \(F\) moves is a
next question.

An affine change of the leading coefficient \(\lambda\) under a local
coordinate change is a projective transformation of its line, so its
cross-ratio is a sensible local analytic diagnostic on the equal-contact
stratum. The double cover forgets labelling and retains its coarse
cross-ratio modulus. This is promising extra data, not a complete local
or embedded classification.

## 5. Why this is a useful laboratory, and what it cannot decide

The member \(a=4\) makes a concrete distinction between several kinds of
proximity. Normalized cycle mass carried by \(C\) grows from \(1/4\) to
\(1/2\); the generic transverse length on \(C\) grows from one to two;
the reduced support loses one component; and the degree-eighteen
first-normal boundary ceases to be a divisor. These changes occur in a
flat family with fixed Hilbert polynomial \(16n-32\). Thus they are
compatible but genuinely different observables.

At \(a=\infty\), the normalized mass carried by \(C\) remains \(1/4\),
the determinant boundary is unchanged, and the residual geometry changes
radically. At general finite \(a\), the same boundary and contact orders
coexist with a varying elliptic modulus. Together these comparisons
argue for a vector of invariants or a stratification, rather than one
universal distance.

In characteristic two the formula reduces to
\(f_a(z)=z^4+a z+a+1\). Its derivative is \(a\). Therefore the special
member \(a=0\) is \((z+1)^4\), whereas generic \(a\ne0\) has four distinct
geometric roots. The characteristic-zero collision parameter \(4\)
reduces to the same special parameter \(0\). The rational formula (7)
is not a useful characteristic-two invariant of this double cover:
\(w^2=f_a(z)\) is an inseparable equation there. A characteristic-two
analogue would need an appropriate separable cover or a different moduli
construction, not reduction of this formula.

Promising next experiments are: test the agreement of the endpoint moduli
when the carrier moves; map this pencil into the full determinant-boundary
fiber in \(\operatorname{Gr}(2,H^0(I_C(4)))\); compute residual schemes at
the three collision values with their nilpotent structures; and trace
the four-sheet moduli under a deformation that moves the boundary points.
Nothing here closes or reopens a canonical STCI question.
