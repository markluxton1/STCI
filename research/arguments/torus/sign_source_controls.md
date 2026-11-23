# Actual controls for sign-breaking equation sources

These controls retain the actual homogeneous equations. The
[source comparison](sign_symmetry_and_actual_sources.md) owns the product
norm and fiber-product theorem. The cycle and parity calculations below
were independently reconstructed during the renewed November 23 synthesis.

## 1. Breaking ideal symmetry while retaining an eigen generator

Work over an algebraically closed field of characteristic different from two,
with coordinates and sign involution as in the source account.
Sign breaking itself is possible with a full translated cycle. Let \(F,G\)
be any coprime sign-even quartics with full translated CI cycle, and let
\(H\ne0\) be a sign-odd quartic. The known exceptional quartic pencils
supply such \(F,G\). Then
\[
                       J_H=(F^2+HG,G^2)                     \tag{AS7}
\]
is a proper \((8,8)\) CI with radical \(\sqrt{(F,G)}\). Successive
Cartier-intersection additivity gives
\([V(F^2+HG,G^2)]=2[V(F^2+HG,G)]=4[V(F,G)]\), including
repeated original components.
For the exceptional doubled pair the cycle is
\(8[C_{1,1}]+8[C_{1,-1}]\), with moment zero.

The ideal is not sign invariant. Otherwise its degree-eight part would
contain \(HG\), so
\(HG=\alpha(F^2+HG)+\beta G^2\). Reducing modulo \(G\) and using
coprimality gives \(\alpha=0\); cancellation then gives \(H=\beta G\),
contradicting the opposite signs. Yet \(G^2\) is still an actual
sign-eigen generator, so the one-equation norm criterion covers its moment. This is an actual
non-invariant source, not an escape from the one-generator criterion.

## 2. Breaking both parity projections of the source pencil

The one-eigen-generator condition can also be escaped by actual
zero-moment thickenings. In the same notation put
\[
 A=F^2+HG,\qquad B_0=G^2,\qquad
 J_2=(A^2,B_0^2+B_0A).                              \tag{AS7b}
\]
This is a proper \((16,16)\) CI with the same radical. Applying Cartier
additivity first modulo \(A\), and then the preceding calculation,
gives \([V(J_2)]=4[V(A,B_0)]=16[V(F,G)]\).
Its two odd parts are \(2F^2HG\) and \(HG^3\), which are linearly
independent since \(F,G\) are coprime. Its even parts are
\(F^4+H^2G^2\) and \(G^4+G^2F^2\). They are independent: reduction
modulo \(G\) makes the coefficient of the first zero, and the second
is nonzero. Thus both parity projections of the degree-sixteen source
plane have rank two. The plane has no sign-eigen member. Nevertheless
its exceptional-pair cycle still has zero moment.

These are nonminimal sources with explicit equation factorizations. For
a minimal degree-product nonzero-moment counterexample, Cartier additivity
and factor descent instead force integral actual generators. This does
not make every integral presentation primitive, nor remove the entirely
thick alternative. The source-plane parity test is necessary, not sufficient.

### A control with noncoincident first-normal lines

The degree-eight control (AS7), wherever it is generically curvilinear,
has first-normal line spanned by \(dG\); its sign transform has the same
line. The entirely thick control (AS7b) has no first-order normal line.
To test the noncoincident case in characteristic zero, take
\[
 F_4=x^4-z^3w,\qquad
 G_8=(y^4-zw^3)(y^4-czw^3),\qquad H_4=z^3x,
 \qquad c\ne0,1.
\]
The reduced CI \((F_4,G_8)\) has eight translated components
\(C_{u,1}\), with \(u^4=1\) or \(u^4=c\), and is generically
transverse along each. Their degrees exhaust the intersection degree
\(32\). For every \(n\ge2\),
\[
                   (G_8+H_4F_4,\ F_4^n)                    \tag{AS7c}
\]
is a proper CI of type \((8,4n)\), with \(n\) times that reduced
cycle. Its moment is zero, also forced by the sign-eigen generator
\(F_4^n\). Its generic first-normal line and its sign transform are
spanned by \(dG_8+H_4dF_4\) and \(dG_8-H_4dF_4\); their wedge
is nonzero because \(H_4\) is generically nonzero and the reduced
pair is transverse. Thus noncoincidence itself is compatible with zero
moment. This is an arrangement control, not a sole-support candidate or
a minimal nonzero-moment source; endpoint attachments still belong in its
actual parity-part quotient. The construction and normal-line check
were independently reconstructed in the drafting-agent response review.

## 3. A parity homotopy preserving the central binary CI

There is a canonical parity projection for every proper pair
\((F_a,G_b)\) through the fixed quartic and avoiding \(V(z,w)\). Set
\[
 F_{\rm st}=\tfrac12(F+(-1)^a\tau F),\quad F_{\rm op}=F-F_{\rm st},
 \qquad
 G_{\rm st}=\tfrac12(G+(-1)^b\tau G),\quad G_{\rm op}=G-G_{\rm st}.
\]
All four forms contain \(C\). For every \(\lambda\in k\),
\[
                  (F_{\rm st}+\lambda F_{\rm op},
                   G_{\rm st}+\lambda G_{\rm op})              \tag{AS8}
\]
has the same central binary regular sequence \((f_0,g_0)\) as the
original pair. Here \(B=k[z,w]\), with the standard grading and fixed
sign involution of the source account. It is therefore a proper
finite-\(B\)-flat homogeneous CI of the same degrees. At \(\lambda=0\) its ideal is sign invariant;
in characteristic zero it necessarily has residual support. Thus parity
projection retains a genuine CI source and its central Gorenstein point,
but can lose sole support. The basis-independent matrix differential
for (AS8) scales by \(\lambda^2\), because both first normal equation
layers do and its [integral residue formula](../arithmetic/integral_first_jet_lifting.md)
is bilinear in those layers. In characteristic zero this is the
[Hilbert pullback form](chow_hilbert_symplectic_form.md#1-an-exact-pullback-formula). This does not identify a moment for the arbitrary residual
cycles in this family.


If the original member has sole support \(C_{u,v}\), and
\(m=ab/4\ne0\) in the field, the differential coefficient at one is
\(2m(u/v)\ne0\). Every sole-supported member has that same coefficient.
Quadratic scaling therefore proves that **precisely** \(\lambda=\pm1\)
have sole support; every other member has a genuine residual curve.
The statement requires characteristic different from two. It assigns
no translated-cycle moment to the residual members.

For every \(\lambda\ne0\), the actual parity-part ideal is constant:
\[
 J_\lambda+\tau J_\lambda
 =(F_{\rm st},F_{\rm op},G_{\rm st},G_{\rm op}).       \tag{AS9}
\]
Its quotient algebra, saturation torsion, full module structure and
\(B\)-head are thus fixed while the differential coefficient varies.
They cannot by themselves determine that coefficient on all actual CI
sources. Conditionally on a sole-supported member, they do not determine
sole support either. One must retain the varying factors \(S/J_\lambda\),
\(S/\tau J_\lambda\) and their marked maps in the fiber product. This
is not an example of two translated-cycle sources with different moments.

## 4. The reduced quartet has directional Hilbert indeterminacy

There is a geometric explanation of the reduced quartic's cyclic defect,
valid in characteristic different from two. Its coordinate algebra and
free hull over \(B=k[z,w]\) are
\[
 E=B\,1\oplus Bx\oplus By\oplus(z,w)B\,h,
 \qquad N=B\,1\oplus Bx\oplus By\oplus Bh,
\]
where \(h=s^2t^2\), \(x^2=zh\), \(y^2=wh\),
\(xy=zw\), \(xh=zy\), \(yh=wx\), \(h^2=zw\).
On \(\operatorname{Bl}_0\mathbf A^2\), take the **image** of the
pulled-back \(E\) in the pulled-back \(N\), before taking a fiber.
The ideal \((z,w)\) becomes invertible, so this image is locally free
of rank four and is generated as an algebra by \(x,y\).

On the chart \(w=tz\), its basis is \((1,x,y,x^2=zh)\), with ideal
\[
 (xy-tz^2,\ y^2-tx^2,\ x^3-z^2y).                    \tag{AS10}
\]
The relations give \(x\cdot x^2=z^2y\),
\(y\cdot x^2=tz^2x\), \((x^2)^2=tz^4\), so the basis is closed
under multiplication; independence follows inside the generic free hull.
The other chart is symmetric and agrees because \(y^2=tx^2\).
The basis vector \(zh\) remains nonzero in the image's special fiber:
its image in the special fiber of the larger free hull is zero, and
interchanging image formation and base change would lose it.

Along the exceptional line the ideals are
\((xy,y^2-tx^2,x^3)\). For \(t\ne0\) these are binary \((2,2)\)
CIs. At zero and infinity they are nongorenstein, and the family of
punctual Hilbert points is nonconstant. Its tautological bundle on this
exceptional line is \(\mathcal O^3\oplus\mathcal O(1)\), since
\((z,w)\mathcal O_{\mathrm{Bl}}=\mathcal O(-E_{\mathrm{exc}})\).
This is the direction line \(\mathbf P^1_{[z:w]}\) at the projection-base
origin, not the intrinsic orbit-parameter line in R-0070/R-0072.
The generic quartet is reduced,
so its Chow cycle determines its Hilbert point uniquely. Any Hilbert lift
of the same cycle map on \(\mathbf A^2\) would, after pullback to the
blowup, agree with this family by separatedness. But its exceptional
restriction would be constant, a contradiction. Thus the reduced cycle
map has no such Hilbert lift, even without imposing homogeneity or a
particular central ideal on a proposed lift.

This independently reconstructed control explains the missing section by
an explicit directional family. Repeated generic cycles admit additional
punctual Hilbert moduli, so uniqueness fails there. It gives no exclusion
of arbitrary repeated lifts; whether those extra moduli can remove this
directional indeterminacy is genuine new research, not a consequence of
the reduced control.

The reduced obstruction cannot be applied componentwise to an arrangement.
The [four-quartet CI](../../results/quartic_mu4_degeneration.md)
\((x^4-z^3w,y^4-zw^3)\) is a simultaneous finite-flat cyclic lift of
four reduced translated components in characteristic zero, although each
component has the individual indeterminacy above. The generic idempotents
separating the quartets need not extend through their common central
collision. Collective gluing is therefore essential even before repeated
cycles introduce nonunique generic Hilbert moduli.
