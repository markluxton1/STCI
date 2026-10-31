# Actual projections, elliptic targets, and polarization gluing

Work over an algebraically closed field of characteristic zero. The target
is always the fixed embedded curve
\[
C_0=[s^4:s^3t:st^3:t^4]\subset Q=(x_0x_3-x_1x_2=0)\subset\mathbf P^3.
\]
The unrestricted two-equation STCI problem remains open. This chapter treats
an actual projection source and a constructive elliptic interface inside it.
It distinguishes a map with the right restriction on a curve, a finite
normalization with **full** inverse support, and a mate descending to the
image. An isolated additional inverse point already prevents a mate.

The [elliptic double-inverse construction](elliptic_double_inverse_construction.md)
also realizes a different source: its inverse elliptic curve covers \(C_0\)
twice, and one fixed member is a finite birational normalization of an octic.
That member has a projective extra inverse scheme of length twelve. Its full
five-parameter support locus remains open; it is outside the isomorphic-inverse
classification and the diagonal-source exclusions below.

The degree-eight smooth-quadric model is a necessary model only under the
Cartier singleton hypotheses of [R-0002](../results/cartier_singleton_lift.md).
[R-0004](../results/projection_phase_reduction.md) supplies the conditional
full-conductor phase problem; it does not assert that admissible projections
exist. The plane and other cone cases are not classified below.

**Review status.** The determinant, boundary, interpolation, nodal-extension,
spin, and paired-cover arguments have independent source review, reused here
for their unchanged mathematical content. They remain **reviewed provisional
mathematics**, not promoted canonical results. The finite special-target
calculation and balanced discriminant calculations are identified separately
in section 5. The balanced degree-ten chart now has independent exact review;
the degree-twelve chart remains unfinished. The local contact-six example has
exact source computation but less independent review than the contact-five
example. The fixed palindromic
Python replay was rerun successfully during consolidation (Python 3.15.2,
SymPy 1.14.0), reproducing its target PASS and component-gate FAIL. Macaulay2
was unavailable, so its inherited exact executions were not replayed. Independent
review of this corrected consolidation accepted its proof preservation, the new
bounded deductions, and section 9.1 characteristic scopes; requested corrections
are resolved. The qualified computations in section 5 retain their separate
review limitations. No actual admissible carrier or mate has been constructed
by these calculations.

The later October 31 source audit independently reviews the double-inverse
fixed member and its rejection, as stated in its linked proof home. It also
supplies the degree-ten repeated-gcd control incorporated in section 5. These
source executions are reused, without claiming a fresh Macaulay2 run here.
Independent comparison with the complete later source proofs and audits
accepted this integration's proof preservation, support bindings and scopes.

## 1. The actual source and its two determinant strata

Use Segre coordinates \([a:b:c:d]\), \(ad=bc\), on
\(S=\mathbf P^1\times\mathbf P^1\). Put \(z=b-c\), and denote the
marked diagonal by \(c_\Delta=(z=0)\). All four sections of
\(H=\mathcal O_S(2,2)\) with prescribed diagonal restrictions are
\[
 U=(a^2,ab,dc,d^2)+z(A_0,A_1,A_2,A_3),\qquad
 A_i\in\langle a,b,c,d\rangle.                                      \tag{1}
\]
This is the entire affine sixteen-parameter source: the restriction kernel
in each coordinate is \(zH^0(\mathcal O_S(1,1))\). On the diagonal,
\((a,b,c,d)=(s^2,st,st,t^2)\), giving precisely \(C_0\).

Admissibility means basepoint freedom, surface birationality, and
\(f^{-1}(C_0)_{\rm red}=c_\Delta\), including isolated inverse points.
Basepoint freedom already makes the morphism finite onto its integral
image: a positive-dimensional projective fiber would contain a curve of
zero degree against the ample bundle \(H\). A birational image has degree
\(H^2=8\).

For an admissible map a degree-\(b\) mate exists exactly when
\[
 z^{2b}\in\operatorname{span}_k\{U^\alpha:|\alpha|=b\}.                \tag{2}
\]
Indeed its pullback divisor must be \(2b c_\Delta\), and sections with
that divisor differ by a scalar. Conversely (2) gives an actual homogeneous
polynomial \(G_b\); finiteness gives sole zero support \(C_0\) on the
image. Membership itself forces absence of additional inverse points.
Failure at finitely many values of \(b\) is not an all-degree obstruction.

### 1.1 The determinant cokernel measures the ruling degrees

Let \(M=\left(\begin{smallmatrix}U_0&U_1\\U_2&U_3\end{smallmatrix}\right)\).
Assume basepoint freedom. If \(q(U)=\det M\ne0\), write its full divisor
\[
 E=mc_\Delta+D,\qquad D\in|(4-m,4-m)|,\quad c_\Delta\not\subset D.
\]
On \(E\), the matrix has rank exactly one. A unit entry reduces it locally
to \(\operatorname{diag}(1,q(U))\); hence its cokernel is an invertible
sheaf \(L_E\), even on nonreduced components, with resolution
\[
0\to\mathcal O_S(-2,-2)^2\xrightarrow{M}\mathcal O_S^2
 \to i_*L_E\to0.
\]
Thus \(\chi(L_E)=0\). Since \(p_a(E)=9\), \(\deg_E L_E=8\).
On the target quadric write
\[
(x_0,x_1,x_2,x_3)=(A_0B_0,A_0B_1,A_1B_0,A_1B_1).
\]
The cokernel is the first ruling bundle; on the diagonal the factorization
is \((s^3,t^3)^{\mathsf T}(s,t)\), so its degree there is three.
It is globally generated. Degree of a line bundle is additive on a
component cycle (tensor the divisor-union sequences and subtract the
structure-sheaf Euler characteristics), including multiplicities. Therefore
\(\deg_D L_E=8-3m\ge0\). If \(D=0\), the divisor class forces \(m=4\)
and would give \(8=12\). Consequently
\[
 m=1\text{ or }2.                                                    \tag{3}
\]

The identically zero determinant cannot be basepoint free. Otherwise the
map lands in \(Q\), and one ruling pulls back to \(\mathcal O_S(a,b)\)
with \(0\le a,b\le2\) and \(a+b=3\), because its diagonal degree is
three and both rulings are globally generated. The choices \((1,2)\) and
\((2,1)\) have nonzero square, contradicting the square-zero pullback
of a ruling under the finite map to \(Q\).

The two ruling degrees on the full residual cycle are consequently
\[
 (\deg_D A,\deg_D B)=(8-3m,8-m).
\]
The target equation \(C_0:A=B^3\) has class \((1,3)\), so its pullback
section on \(D\) has degree \(32-6m\), equal to 26 or 20. Meanwhile
\(D\cdot c_\Delta=8-2m\), equal to six or four. Full inverse support
requires every zero of that section to lie on \(D\cap c_\Delta\), and
forbids a component of \(D\) mapping into \(C_0\). These numbers do not
by themselves bound off-diagonal length: diagonal contacts can be highly
nontransverse.

### 1.2 First-normal data and the complete order-two normal form

Put \(y=(b+c)/2\), so \(ad=y^2-z^2/4\). There are twelve independent
antisymmetric first-normal coefficients and four symmetric coefficients
multiplying \(z^2\). Using the characteristic-zero splitting in
[R-0020](../results/quartic_conormal_characteristic_jump.md), their map is
\[
H^0(\mathcal O_{c_\Delta}(2))^4\longrightarrow
H^0(N_{C_0/\mathbf P^3}(-2))=H^0(\mathcal O(5))^2.
\]
It is an isomorphism. For a coordinate proof of injectivity, on \(s=1\)
write the four first derivatives as polynomials \(h_i(t)\) of degree at
most two. A tangential variation requires
\[
h_2=3t^2h_1-2t^3h_0,\qquad h_3=4t^3h_1-3t^4h_0.
\]
Degree comparison first gives, for \(h_0=A+Bt+Ct^2\) and
\(h_1=D+Et+Ft^2\), \(C=0,E=2A/3,F=2B/3\), and then
\(D=A=B=0\). Thus all \(h_i\) vanish. Dimensions are twelve on each
side. Intrinsically, the possible tangential generator fails to lift in
the twisted Euler sequence: its connecting class is the nonzero degree
four Euler class in \(H^1(\mathcal O(-2))\).

The derivative-zero boundary consists of the four symmetric \(z^2\)
coefficients and factors through the factor-interchange quotient
\(S\to\operatorname{Sym}^2\mathbf P^1\); it is nonbirational. A
birational candidate has a nonzero pair of quintics, whose common divisor
has degree at most five. This bounds support, not residual multiplicity.

The order-at-least-two determinant condition imposes seven independent
linear conditions. The complete nine-parameter source is
\[
\begin{split}
U={}&(a^2,ay,yd,d^2)+z(V_0,V_1,V_2,V_3)+z^2(h_0,h_1,h_2,h_3),\\
V_0={}&Aa+By,&V_1={}&Ca+Ay+Bd,\\
V_2={}&Da+Ey-Cd,&V_3={}&Dy+Ed.                                      \tag{4}
\end{split}
\]
The first-order determinant is \((ad-y^2)(Ea+Ad)\). The twelve
unconstrained coefficients of \(V_i\) map onto all binary sextics on
\((a,y,d)=(s^2,st,t^2)\), so the five displayed kernel parameters exhaust
it. If \(q(U)=z^2R\), then
\[
R|_{c_\Delta}=(h_3-CD)+(-h_2-CE)t+(C^2-1/4)t^2
 +(-h_1+AC)t^3+(h_0+BC)t^4,                                      \tag{5}
\]
while its normal-ramification scalar quartic is
\(g(t)=D+Et-4Ct^2-At^3-Bt^4\). These are different quartics.
The full determinant identity is in
[the coefficient certificates](../computations/projection_incidence_certificates.m2).

For an actual finite birational member with smooth normalization \(S\)
and degree-eight hypersurface image \(X\), the conductor divisor on \(S\)
has class
\[
\mathfrak C=\nu^*K_X-K_S=4(2,2)+(2,2)=(10,10).
\]
Here finite duality for the Gorenstein hypersurface identifies the
conductor ideal on the smooth normalization with the invertible sheaf
\(\omega_S\otimes\nu^*\omega_X^{-1}=\mathcal O_S(-\mathfrak C)\).
Thus its contact with the marked diagonal has degree twenty. Comparing
concentration of this full conductor contact with common roots of the
normal quintic pair is an unresolved interface. Their root-support bound
alone does not bound these conductor multiplicities; the explicit local
controls in section 2.3 warn against making that inference.

### 1.3 The full fiberwise inverse and descent tests

For the whole sixteen-parameter source (1), the order-one open is a union
of seven principal opens: the binary sextic
\[
 t^4A_0(s^2,st,st,t^2)+s^4A_3(s^2,st,st,t^2)
 -st^3A_1(s^2,st,st,t^2)-s^3tA_2(s^2,st,st,t^2)
\]
has at least one nonzero coefficient. Inverting the product of all seven
coefficients would discard valid order-one parameters.

The affine chart \(z=1\), \(b=y+1/2,c=y-1/2\), meets every projective
point off the diagonal. For the four literal generators
\[
 q=x_0x_3-x_1x_2,\quad c_0=x_0^2x_2-x_1^3,\quad
 c_1=x_0x_2^2-x_1^2x_3,\quad c_2=x_2^3-x_1x_3^2,
\]
the specialized inverse ideal is
\[
 J=(ad-y^2+1/4,q(U),c_0(U),c_1(U),c_2(U)).
\]
It must be the unit ideal. This retains isolated points and basepoints:
a basepoint also zeros all four pulled-back generators, while the diagonal
restriction has none. The equivalent homogeneous test saturates by \(z\)
and the source irrelevant ideal. Parameter-fraction-field calculations
alone test the generic fiber; every exceptional support and rank stratum
remains part of the constructible problem. After this support test,
birationality and degree-eight image remain separate requirements.

For a surviving member, expand the columns \(U^\alpha\), \(|\alpha|=b\),
and \(z^{2b}\) in a complete degree-\(2b\) Segre-ring basis. Equation (2)
is equality of the original and augmented ranks. Each original rank stratum
requires its own nonzero minor and augmented-minor equations; failure on one
chosen maximal-minor open does not cover the family. This actual coordinate
subalgebra test includes conductor descent. Neither it nor the order-one
support-unit locus has been computed for the full sixteen parameters.


## 2. Uniform excluded coefficient loci and why local counts are insufficient

The following are proper subfamilies of (1); no coordinate-normalization
argument makes them exhaustive.

* If \(U_0=a^2\), \(U_1=a(pb+(1-p)c)\), while all eight coefficients
  of \(A_2,A_3\) vary, the locus is empty. Write
  \(A_2=e_0a+e_1b+e_2c+e_3d\). On the two endpoint fibers its third
  coordinate is \(c((1-e_3)d-e_2c)\) and \(b(e_1b+e_3d)\).
  Avoiding off-diagonal zeros forces respectively \(e_3=1,e_2\ne0\)
  and \(e_3=0,e_1\ne0\). An identically zero restriction also fails.
  At a forbidden zero the fourth coordinate gives either a basepoint or
  an extra endpoint inverse point. The contradiction is independent of \(p\).

* For \(L=pb+(1-p)c\), the family
  \(U=(a^2+Az^2,aL,dL,d^2+Dz^2)\) is empty. If \(AD=0\), the
  off-diagonal points with \(a=d=0\) give basepoints or endpoints.
  Otherwise choose \(r^4=D/A\), and put
  \[
  a=w^2,\quad d=w^2r^2,\quad
  b=r(w^2+A)+w(1-p),\quad c=r(w^2+A)-wp.
  \]
  Then \(z=w\), \(U=w^2(w^2+A)(1,r,r^3,r^4)\), and the Segre
  equation is
  \[
  (1-2p)rw^3+(2Ar^2-p(1-p))w^2+(1-2p)rAw+A^2r^2=0.
  \]
  For \(p\ne1/2\) it is a cubic with nonzero constant; for \(p=1/2\)
  choose one of the opposite values of \(r^2\) for which its quadratic
  coefficient is nonzero. Either way it has a nonzero root and gives a
  forbidden source point. The scalar may vanish, in which case it is a
  basepoint, not an escape.

* Inside (4), the entire locus \(q(U)=\kappa z^2ad\), \(\kappa\ne0\),
  is empty. In the notation
  \((A,B,C,D,E)=(l_0,m_0,l_1,l_2,m_2)\), exact coefficient comparison
  and saturation by \(\kappa\) give
  \[
  l_0=m_2=h_1=h_2=0,\quad h_0=-m_0l_1,\quad h_3=l_1l_2,
  \quad\kappa=l_1^2-1/4,\quad m_0l_2=0.
  \]
  At \(a=d=0,y=\pm z/2\), the tuple is
  \(z^2(m_0(\pm1/2-l_1),0,0,l_2(\pm1/2+l_1))\).
  Both branches of \(m_0l_2=0\) give a basepoint or an extra endpoint;
  the displayed coefficients are nonzero when needed because \(\kappa\ne0\).
  This exact saturation is supported by the coefficient certificates.

### 2.1 A full four-parameter order-one family

For arbitrary \(A,D,C,E\), the locus
\[
U=(a^2+Aaz+Cz^2,ay,dy,d^2+Ddz+Ez^2)                              \tag{6}
\]
is empty. Its first determinant coefficient is \(ad(Ad+Da)\), so it
contains genuine order-one maps when \((A,D)\ne(0,0)\). If \(CE=0\),
use \(a=d=0,y=\pm z/2\). Otherwise scale \(z=1\), and set
\[
\begin{gathered}
F=CD^2-A^2E,\quad N=Cw^2-E,\quad V=w(D-Aw),\quad K=CDw-AE,\\
P(w)=N^2((8CD+A)w-(8AE+D))+4w(D-Aw)K^2.
\end{gathered}
\]
When \(F\ne0\), \(P\) has a nonzero root avoiding \(NV=0\).
Its extreme coefficients are \(-E^2(8AE+D)\) and \(C^2(8CD+A)\),
which cannot both vanish unless \(F=0\). If the constant coefficient
vanishes, \(D=-8AE\), and the coefficient of \(w^4\) is
\(-4AD^2C^2\ne0\), so the quintic is not a pure monomial. If its
leading coefficient vanishes, \(A=-8CD\), and its \(w\) coefficient
is \(4A^2DE^2\ne0\). These cases guarantee a nonzero root. At a
nonzero root of \(N\), \(P=4C^2w^3(D-Aw)^3\ne0\); at a root of
\(D-Aw\), \(P=8AN^3\ne0\). Thus the root avoids the denominators.
Choose \(r^2=w\), and put
\[
a=N/V,\quad d=wa,\quad y=r(a+A+C/a).
\]
The target tuple is proportional to \((1,r,r^3,r^4)\), and
\[
4N^2(D-Aw)(y^2-ad-1/4)=P(w).
\]
It is therefore an actual off-diagonal source point, either a basepoint
or an extra inverse point.

If \(F=0\), choose \(w\ne0\) with \(D=Aw,E=Cw^2\). For \(A=0\),
choose the sign of \(w^2=E/C\) so that \(8wC\ne1\). The equation
\[
4w(Aa+C)(2a^2+Aa+C)-a^2=0
\]
has nonzero constant and is a nonconstant cubic when \(A\ne0\), or a
nonconstant quadratic for that choice when \(A=0\). A nonzero root,
with the same \(d,y\), gives the witness. This includes every boundary.
The independent rational identity block in the coefficient certificates
supports the construction; root existence is the argument just given.

On the complete order-one source there is also a cycle obstruction:
\(q(U)\) cannot have divisor \(c_\Delta+3R\), \(R\in|(1,1)|\),
\(R\ne c_\Delta\). Degree additivity would give \(3\deg_R L_E=5\).
More generally the gcd of residual component multiplicities divides five.

### 2.2 A five-parameter order-two contact contradiction

The whole slice
\[
U=(a^2+h_0z^2,\ a(y+\gamma z)+h_1z^2,
 d(y-\gamma z)+h_2z^2,\ d^2+h_3z^2)                            \tag{7}
\]
is inadmissible. For \(\gamma=0\) it is symmetric and nonbirational.
For \(\gamma\ne0\), basepoint freedom and full inverse support already
contradict each other. Its determinant is \(z^2R\), with
\[
R=(\gamma^2-1/4)ad+h_3a^2+h_0d^2-h_2a(y+\gamma z)
-h_1d(y-\gamma z)+(h_0h_3-h_1h_2)z^2.
\]
If \(R|_{c_\Delta}=0\), then all \(h_i=0,\gamma^2=1/4\), giving
basepoints. Otherwise its residual \(D\) has class \((2,2)\). On
\(a=1\), \(d=y^2-z^2/4\), the cubic
\(H_0=U_0^2U_2-U_1^3\) has first coefficient \(-4\gamma y^2z\).
Away from the two diagonal endpoints the pulled-back curve ideal is
therefore \((z)\), so its contact on \(D\) is just the intersection
length with the diagonal.

At \(p_0=(1,0,0,0)\), membership in \(D\) means \(h_3=0\), and
full inverse support forces \(h_2\ne0\): otherwise on
\(d=0,z=1,y=\pm1/2\) one solves
\(a(\pm1/2+\gamma)+h_1=0\), producing an endpoint or basepoint.
The two linear coefficients differ by one. When \(h_2\ne0\),
\[
R=-h_2(y+\gamma z)+O((y,z)^2),\qquad
H_0=h_2z^2+O((y,z)^3).
\]
Thus \(D\) is smooth transverse to the diagonal there, with contact two
instead of one. At the other endpoint, similarly \(h_0=0\) forces
\(h_1\ne0\), and on \(d=1\)
\[
R=-h_1(y-\gamma z)+O((y,z)^2),\quad
U_2^3-U_1U_3^2=-h_1z^2+O((y,z)^3).
\]
The same contact conclusion holds, including \(\gamma=\pm1/2\).
If no component maps into \(C_0\), its defining section on the Cartier
curve \(D\) is a nonzerodivisor: \(D\) is Cohen--Macaulay without
embedded associated points. Its zero scheme has degree twenty even for
nonreduced \(D\). Full support would place that length on the diagonal,
where the preceding local argument totals at most \(4+2=6\). This is
impossible. The four other antisymmetric parameters in (4) are not covered.

### 2.3 Actual inverse schemes and a warning about normal ramification

A simple early pencil \((a^2+z^2,ab,dc,d^2+\lambda z^2)\) fails at
\(a=1,b=0,c^2=-1,d=0\): it gives extra inverse points when
\(\lambda\ne0\), basepoints when \(\lambda=0\).
The middle-coordinate perturbation
\[
U=(a^2+z^2,ab+z^2,dc+2z^2,d^2+3z^2)                            \tag{8}
\]
is basepoint free. Off the diagonal scale \(z=1\). From \(U_0=U_1=0\)
one gets \(a^2=-1,b=a,d=c\), whence \(U_3-U_2=1\).
Nevertheless its off-diagonal inverse scheme is zero-dimensional of
length sixteen, by [the exact ideal calculation](../computations/projection_inverse_example.m2)
using all four generators of \(I_{C_0}\). Sixteen is a scheme length,
not a count of distinct points. The actual finite image has no mate in
any degree: the pullback zero divisor of a nonzero section on smooth \(S\)
cannot have isolated zero points in addition to its curve support.

Nor can first-normal root multiplicities alone bound all diagonal contact.
With \(i^2=-1\), take
\[
U=(a^2,ay,yd+zy+iz^2/4,
 d^2+z(-10iy-2d)+5z^2/2).                                      \tag{9}
\]
At \(a=1,y=x,d=x^2-z^2/4\), remove the common diagonal factor from
the graph equations of \(C_0\). The remaining equations are
\[
H_2=x(1-z/4)+iz/4,\quad
H_3=-10ix-2x^2-x^2z/2+z^3/16+z^2/2+5z/2.
\]
The normal pair at \(z=0\) has common order one at \(x=0\), but
\[
(1-z/4)^2H_3\left(-\frac{iz}{4(1-z/4)},z\right)=z^5/256.
\]
Thus the residual contact length is five. The tuple is basepoint free:
on \(a=0,z=1,y=\pm1/2\), solving \(U_2=0\) gives
\(d=-1\mp i/2\), where \(U_3=21/4\mp3i\ne0\); \(z=0\) is
immediate. It is birational: over \(k(x)\), its second ratio is quadratic
in \(z\), with involution \(z\mapsto-4x/(i-x)-z\); the third ratio is
not invariant, as its difference at \(x=1\) has cubic coefficient
\((3+i)/2\ne0\). Its determinant has order one. The off-diagonal
inverse scheme has two support points, length four at each, so it is
still inadmissible. This refutes a factor-four local bound for arbitrary
members, not a bound that additionally uses global sole support.

A stronger control has contact six. With \(\rho^2=5\), put
\[
A=5\rho/16,\ L=\rho/10,\ B=-8\rho/15,\ C=-1/2,\ M=-4/15,
\]
and replace the last two coordinates by
\(yd+z(y+Ad)+Lz^2\), \(d^2+z(By+Cd)+Mz^2\). Its residual equations are
\[
K_2=Ax^2+x(1-z/4)+Lz-Az^2/4,\quad
K_3=Bx+Cx^2-x^2z/2+z^3/16-Cz^2/4+Mz.
\]
The first is smooth. On its branch,
\(K_3=-9z^6/65536+O(z^7)\); the exact quotient has length six and
is supported at the origin. The normal gcd remains simple. The tuple is
basepoint free by saturated ideal calculation; birationality follows
because the last two ratios have degrees three and four in \(z\), so
their common function-field index divides both. Its off-diagonal inverse
scheme again has length eight. The essential exact calculations, including
the independently checked contact-five support refinement, survive in
[the local-contact script](../computations/projection_local_contacts.m2).
No maximal local-contact theorem is claimed.

## 3. The complete bad boundary of the order-two residual

Assume \(f^*Q=2c_\Delta+D\), with basepoint-free \(U\),
\(D\in|(2,2)|\), and full inverse support \(c_\Delta\).
Then **\(D\) is smooth and irreducible**. This theorem concerns the
complete nine-parameter order-two source, not a coefficient slice, and
does not require surface birationality.

Here is the full boundary argument. If \(T\) is a smooth curve of genus
\(g\), and \(A,B:T\to\mathbf P^1\) have degrees \(a=1\) or 2 and
\(b>0\), then
\[
\#\{A=B^3\}\ge b-a+2-2g.                                      \tag{10}
\]
To retain all boundary coincidences, put \(F=B^3/A\), let \(n_A,n_B\)
count distinct zeros and poles, let \(r\) count common boundary points,
and let \(s=\sum_{\rm same}|\operatorname{ord}A|\) over same-sign
overlaps. Since an \(A\)-order is at most two while a nonzero
\(B^3\)-order is at least three, no overlap disappears entirely. Thus
\(d=\deg F=3b+a-s\) and
\(n_0(F)+n_\infty(F)=n_A+n_B-r\). Ramification in the three fibers
\(0,1,\infty\) gives
\[
\#F^{-1}(1)\ge b-a+2-2g+(2b-n_B)
 +\sum_{\operatorname{Supp}\operatorname{div}A}(e_P-1)+r-s.
\]
The last correction is nonnegative pointwise: at a same-sign overlap it
is \((e_P-1)+1-e_P=0\), at an opposite-sign overlap it is \(e_P\),
and otherwise \(e_P-1\). These are genuine nonboundary solutions;
endpoint equalities can only add solutions. This proves (10).

For an integral residual component \(K\), let \(n=c_\Delta\cdot K\)
and let \(a,b\) be its ruling degrees on the normalization. Then
\(a+b=2n\). The pulled-back diagonal has degree \(n\), so full support
permits at most \(n\) normalized inverse points. A singular integral
\((2,2)\) curve has rational normalization, and degrees \((2,6)\);
(10) gives at least six points versus four allowed. It is excluded.

If \(D\) is reducible or nonreduced, every proper integral component is
smooth rational: its class is a ruling, \((1,1),(1,2)\), or \((2,1)\).
A component with \(a=1\) has \(b=2n-1\) and at least \(2n>n\)
inverse points by (10), so is impossible. Since the component-cycle first
ruling degree sums to two, there is exactly one component \(T\) with
\(a=2\), of multiplicity one; all others have \(a=0\). If
\(c_\Delta\cdot T\ge3\), (10) gives \(2n-2>n\). Thus \(T\) is a
ruling or a \((1,1)\) curve. The ruling case has \(b=0\) and is kept;
it is not passed to the positive-\(b\) lemma.

For another component \(K\), \(A=\alpha\) is constant and \(B\) has
degree \(2n\). If \(\alpha\in k^*\), the three distinct fibers
\(B^3=\alpha\), confined to at most \(n\) points, contribute at least
\(6n-n=5n\) ramification units, exceeding \(4n-2\). Thus
\(\alpha=0\) or \(\infty\), and \(K\cap c_\Delta\) is supported
at the corresponding unique endpoint \(P\). If \(n\ge2\), the smooth
curves \(K,c_\Delta\) are tangent at \(P\). A regular target endpoint
coordinate for \(B\) has nonzero derivative on \(c_\Delta\), hence on
\(K\); but full support requires its entire degree-\(2n\) fiber at
\(P\). This contradiction forces \(n=1\). Every such \(K\) is an
endpoint ruling fiber, and its \(B\)-derivative at \(P\) vanishes.

If \(T\) is \((1,1)\), its complement contains one fiber of each
ruling. If \(T\) is a ruling, the complement has class \((1,2)\) or
\((2,1)\), counted with multiplicities, and again contains both ruling
types. Those fibers meet, so their constant \(A\)-values agree; they
pass through the same endpoint \(P\). Their transverse tangent directions
span \(T_PS\), so the regular \(B\)-coordinate has zero differential
on \(S\) at \(P\), contradicting its nonzero derivative on the diagonal.
This includes repeated fibers and exhausts all bad boundaries.

### 3.1 A different binary proof for the square residual

The narrower case \(D=2R\), \(R\in|(1,1)|\), has an independent
useful mechanism. For smooth \(R\), ruling degrees are \((1,3)\),
so its image is an irreducible target curve of class \((3,1)\), a graph
with coprime cubic coefficients. It could meet \(C_0\) in at most two
points, since \(R\cdot c_\Delta=2\). The restriction of its equation
is a binary degree-ten form in the monomial space with indices
\(0,1,3,4,6,7,9,10\). A form with two nonendpoint roots reduces to
\((s-rt)^m(s-t)^{10-m}\), \(1\le m\le5\), \(r\ne0,1\).
The three missing coefficients at indices \(2,5,8\) have gcd one in
\(\mathbf Q[r]\) for every \(m\). The small exact gcd calculation is
in the coefficient certificates. For an endpoint and a nonendpoint root,
the missing coefficient nearest that endpoint forces multiplicity at
least nine; its unique lift has a cubic ruling factor. For two endpoints,
the allowed monomials also lift reducibly. A single nonendpoint tenth
power has a nonzero missing coefficient. Thus no irreducible equation
has this contact support.

If \(R\) is reducible, one of its two ruling fibers has target ruling
degrees \((1,1)\), giving an irreducible graph conic with contact at one
point. Its binary quartic restriction misses index two; a fourth power
can miss that coefficient only at an endpoint. Its unique endpoint lift
is \(A_0B_0\) or \(A_1B_1\), reducible. This separately excludes the
whole square-residual stratum. It exposes restricted equation-space
interpolation rather than the component-degree/endpoint differential
mechanism of the full boundary proof.

## 4. The surviving elliptic incidence and actual source interpolation

On a prospective birational admissible order-two map, \(D\) is now a
smooth elliptic curve. Its ruling functions have degrees \((2,6)\).
Put \(Z=D\cap c_\Delta\). Full support allows at most four inverse
points. In fact all four are distinct, finite and nonzero in the marked
parameter, and all ruling zero/pole divisors are reduced and pairwise
disjoint.

For completeness, let
\(\delta_A=4-n_A,\delta_B=12-n_B\), and let \(S_0,O_0\) count same-
and opposite-sign boundary overlaps. Put
\(C_1=\sum_{\rm same}|\operatorname{ord}A|\). As in section 3,
\[
\deg(B^3/A)=20-C_1,\qquad n_0+n_\infty=16-\delta_A-\delta_B-S_0-O_0.
\]
Riemann--Hurwitz gives at least
\(4+\delta_A+\delta_B+S_0+O_0-C_1\) points over one. Same-sign
boundary overlaps are additional projective solutions of \(A=B^3\),
so the actual inverse support has size at least
\[
4+\delta_A+\delta_B+O_0+
 \sum_{\rm same}(2-|\operatorname{ord}A|).
\]
Every term is nonnegative. At most four forces \(\delta_A=\delta_B=O_0=0\),
then every \(A\)-order is one, forcing \(S_0=0\). Equality throughout
shows \(F=B^3/A\) is a degree-twenty cover with partitions
\((3^6,1^2)\) over zero and infinity, four points over one, and no other
branch values. These three fibers exhaust its forty ramification units.
This is a finite passport restriction, not an enumeration or an extension
theorem.

The analogous smooth order-one boundary has residual class \((3,3)\),
genus four, and ruling degrees \((5,7)\). Under the additional reduced,
pairwise disjoint zero/pole hypotheses, \(B^3/A\) has degree 26 and
partitions \((3^7,1^5)\) over zero and infinity. Those two fibers
contribute 28 ramification units; concentration over one on at most six
points contributes at least twenty. Riemann--Hurwitz permits 58 in total,
leaving up to ten units elsewhere. Thus the same count does **not** give a
three-branch-value reduction in order one; colliding boundary divisors
also require separate treatment.

### 4.1 A double residual image forces global symmetry

The generic degree of \(D\to f(D)\) divides \(\gcd(2,6)=2\).
If it is two, then \(B=R(A)\) for a degree-three rational function.
On the \(A\)-line the equation \(t=R(t)^3\) has at least four distinct
solutions by the degree-one case of (10). Full support allows four points
on \(D\), so these four values each have only one inverse point under
the double cover \(A\): they are exactly its branch values, and \(Z\)
is its ramification divisor. Write
\[
L=A^*\mathcal O(1),\quad P=\mathcal O_D(1,0),\quad P'=\mathcal O_D(0,1).
\]
Then \(PP'=\mathcal O_D(Z)=L^2\). For the deck involution \(\iota\),
\(\iota^*P=L^2P^{-1}=P'\), by the elliptic group law
\(x\mapsto\ell-x\). The complete source ruling pencils therefore give
\(u\iota=g v,v\iota=g^{-1}u\). At the four fixed points, \(u=v\)
with distinct values; thus \(g=1\). The involution is source factor
interchange \(\sigma\) on \(D\).

The target tuples \(\sigma^*U|_D\) and \(U|_D\) differ by a constant
scalar. The standard interchange linearization is \(+1\) at a diagonal
point, so basepoint freedom forces that scalar to be one. Each odd part
\(U_i-\sigma^*U_i\) vanishes on \(D\), hence is a scalar multiple
of its defining \((2,2)\) section. The odd part also vanishes on the
diagonal, while the defining section does not vanish there identically
because \(D\) is irreducible and distinct from the diagonal. Therefore
each scalar is zero, and all odd parts vanish globally. The whole surface map factors
through \(S/\sigma=\mathbf P^2\) and is not birational.
The remaining residual map is therefore birational onto an integral
curve \(C'\) of target class \((6,2)\).

### 4.2 Picard identities use the actual source polarization

Let \(\mathcal Z=\mathcal O_D(Z)\), \(L=A^*\mathcal O(1)\), and
\(M=B^*\mathcal O(1)\). The actual source gives \(LM=\mathcal Z^2\).
If \(T=F^{-1}(1)\) with multiplicities, \(\mathcal O_D(T)=LM^3\).
Ramification over zero and infinity has class \(M^4\), and ramification
over one has class \(LM^3\mathcal Z^{-1}\). Since \(\omega_D=1\),
Riemann--Hurwitz gives
\[
M^4LM^3\mathcal Z^{-1}=(LM^3)^2,
\quad M=L\mathcal Z,
\quad \boxed{\mathcal Z=L^2,\ M=L^3}.                             \tag{11}
\]
No multiplication-by-two cancellation in a Picard group is used. The
first identity \(M=L\mathcal Z\) holds for the abstract target passport;
the boxed identities additionally use the actual source polarization.
They do not identify \(Z\) with the branch divisor of \(A\).

### 4.3 The four marked points must span the target space

Suppose the distinct marked parameters are roots of
\(R_Z(t)=t^4+at^3+bt^2+ct+d\), \(d\ne0\). Then \(b\ne0\).
If \(b=0\), at a mark \(A=t^3\) and
\(t(A+c)=-(aA+d)\). If \(d-ac\ne0\), the degree-two function
\(a'=-(aA+d)/(A+c)\) is finite there and equals \(t\) at all four
marks. If \(d=ac\), the factorization
\((t+a)(t^3+c)\) gives three distinct marks in one degree-two \(A\)-fiber,
already impossible.

In the nondegenerate case a degree-two interpolation lemma applies.
If \(a'\) has bundle \(L\), \(L^2=\mathcal O(Z)\), and another
degree-two function \(u\) agrees with it at the four distinct finite
values, either \(u=a'\), or \(u-a'\) has four zeros and at most four
poles. Equality forces no pole cancellation and gives
\(P L=\mathcal O(Z)=L^2\), where \(P\) is the bundle of \(u\).
Thus \(P=L\). Every degree-two function from that complete pencil is
a Möbius transform of \(a'\); agreement at the distinct values forces
identity. Apply this to both source rulings \(u,v\): both equal \(a'\),
contradicting the embedded \((2,2)\) curve.

A hyperplane restricts on \(C_0\) to the quartic space missing the
\(s^2t^2\) coefficient. Hence \(b=0\) means exactly that the four
marked target points are coplanar. The obstruction retains their actual
source pencils, rather than just degrees. In (5) it implies
\(C^2\ne1/4\). It holds for every distribution of the twenty contacts;
it does not settle the nonzero-middle-coefficient source.

## 5. Exact target equations, constructive controls, and incomplete charts

The equation of a primitive residual image is
\[
e_0(A)+Be_1(A)+B^2e_2(A)=0,\qquad \deg e_i\le6.
\]
Restriction \(A=t^3,B=t\) is an isomorphism onto binary forms of degree
twenty: group the coefficients by their exponent modulo three. Thus the
target is determined by
\(P(t)=\prod_{i=1}^4(t-t_i)^{n_i}\), \(t_i\in k^*\) distinct,
\(n_i>0,\sum n_i=20\), with one support parameter normalized by the
torus. Its discriminant \(\Delta=e_1^2-4e_0e_2\) must have odd
squarefree part of degree three or four for elliptic normalization. An
integral actual \((6,2)\) equation also needs a primitive coefficient
triple and full bidegree. Four target points can split into more than four
normalization points; this must be counted explicitly.

Two distinct target controls survive; only the second needs the finite
[enumeration script](../computations/projection_elliptic_finite_targets.m2):

1. A rational degree-ten Padé map with
   \(p=7x^3+42x^2+30x+2\), \(q=2x^3+30x^2+42x+7\) satisfies the exact identities
   \[
   p^3-xq^3=-(x-1)^7(x+1)(x+8)(8x+1),
   \]
   \[
   3x(p'q-pq')-pq=-14(x-1)^6.
   \]
   Put \(c=(x+1)(x+8)(8x+1)\), a separable cubic coprime to
   \((x-1)pq\); \(p,q\) themselves are coprime and separable.
   On \(y^2=(x-1)c(x)\), take \(A=x,B=p/q\).
   Its contact fiber has multiplicities \((14,2,2,2)\), degree twenty;
   the other fibers have the required \((3^6,1^2)\) pattern. The displayed
   derivative numerator shows that there are no additional critical values. This is a
   genuine elliptic target-map construction with degree-two image. It
   cannot give a birational surface projection by section 4.1. It is
   retained as a construction, not discarded because that later gate fails.
2. For target support \(\{0,\infty,1,-1\}\), all 1771 exponent tuples
   \((a,b,c,d)\), sum twenty, are exhausted by
   \(P=t^a(t-1)^c(t+1)^d\). Exactly 171 have primitive actual bidegree.
   The only elliptic cases are \((2,2,4,12),(2,2,8,8),(2,2,12,4)\),
   with odd discriminant degrees 3, 4, 3. Their normalized inverse counts
   are six, eight, six. At each finite target point the quadratic has a
   repeated target \(B\)-value; an even discriminant order splits it into
   two normalized points, an odd order gives one. Reverse degree-six
   polynomials at infinity, where the discriminant order is
   \(12-\deg\Delta\). Thus this entire special four-root locus fails.
   Scaling gives the same exclusion for \(\{0,\infty,r,-r\}\).

The Padé identities and coprimalities were checked by fresh exact SymPy
arithmetic during consolidation; their displayed factorizations are a
small direct proof. The special-root enumeration has inherited execution
evidence and originally had **independent review pending**.
Its endpoint support is also excluded by the stronger reduced-boundary
argument in section 4, but its explicit normalization examples remain
informative. No arbitrary four-point target enumeration was completed.

For balanced contact \((5,5,5,5)\), normalize
\(P=(t^4+at^3+bt^2+ct+1)^5\). Its discriminant is binary degree twelve.
On an actual elliptic survivor its square factor has binary degree four,
and its remaining branch quartic is separable and avoids the \(A\)-endpoints.
[The balanced-discriminant script](../computations/projection_balanced_discriminant.m2)
retains the smallest completed algebraic calculations:

* Square-factor affine degrees zero, one, and two, with discriminant
degrees at most four, six, and eight, give the unit ideal after saturation
by the support discriminant. These are inherited exact execution claims,
not an independently reviewed classification of balanced contact.
* On the nonzero-middle locus, vanishing of the top degree-twelve and
degree-eleven coefficients forces
\(b=-3a^2/4,c=(7a^4+40)/(20a),a\ne0\). Scale \(t=ay\) and put
\(\lambda=a^4\); the support is proportional to
\[
20\lambda y^4+20\lambda y^3-15\lambda y^2+(7\lambda+40)y+20.
\]
The discriminant resultant has six nonconstant irreducible parameter
factors of degrees \(1,2,2,3,12,14\). One linear and one quadratic
factor are degenerate support or lower discriminant degree. Exact number-
field gcd decomposition gives odd discriminant degree eight for each
remaining factor; away from them the degree-ten discriminant is squarefree.
Hence no elliptic normalization occurs on this degree-ten chart. The
October 31 independent review reconstructs this calculation with fresh
coefficient formation, a fresh resultant and a derivative-gcd layer count;
the [independently executed control](../computations/stci_closeout_degree_ten_independent_2026_10_31.m2)
and [captured successful output](../computations/stci_closeout_degree_ten_independent_2026_10_31.txt)
are retained. The linear factor is \(\lambda\), already excluded, and the
degree-lowering factor is \(169\lambda^2+280\lambda-800\). At every
nondegenerate exceptional factor of degrees \(2,3,12,14\), successive
derivative-gcd degrees are \((10,1,0)\): one double root and eight simple
roots, hence odd part degree eight and genus three. Away from the resultant
locus the degree-ten discriminant is squarefree and gives genus four.
This is **independently reviewed provisional exclusion of that exact chart**,
not an exclusion of all balanced contacts or primitive elliptic targets.

Reciprocal support supplies a useful smaller coefficient model, without
a classification claim. For \(R=t^4+at^3+bt^2+at+1\), coefficient
reversal swaps \(e_0,e_2\) and preserves the appropriate reciprocal
\(e_1\), so \(\Delta(A)=A^{12}\Delta(1/A)\). Write its coefficients
as \(d_i=d_{12-i}\). Then
\[
A^{-6}\Delta(A)=d_6+\sum_{i=1}^6d_{6+i}C_i(A+A^{-1}),\quad
C_0=2,\ C_1=z,\ C_i=zC_{i-1}-C_{i-2}.
\]
Thus a reciprocal degree-twelve discriminant reduces to degree six in the
quotient coordinate \(A+A^{-1}\). This accounts for the symbolic
palindromic preprocessing without confusing it with a completed genus-one
locus. Geometrically the quadratic discriminant records the branch
normalization of the double cover to the \(A\)-line; its odd part, not
its radical, determines genus. Its even factors instead record coincident
branches in the chosen singular target equation. An integral \((6,2)\)
image has arithmetic genus five, so elliptic normalization requires total
singularity defect four; the discriminant method tracks this through the
actual equation rather than presuming a generic singularity type.

The affine square-quartic/degree-twelve chart is **unfinished**. Its exact
necessary incidence is as follows. Over
\(B=\mathbf Q[a,b,c,s_0,s_1,s_2,s_3]\), put
\[
 R=t^4+at^3+bt^2+ct+1,\qquad
 S_4(A)=A^4+s_3A^3+s_2A^2+s_1A+s_0,
\]
regroup \(R^5\) into \(e_0,e_1,e_2\), and set
\[
 I=\bigl([A^j]\operatorname{rem}(e_1^2-4e_0e_2,S_4^2):0\le j\le7\bigr).
\]
The saturation by \(b\operatorname{Disc}(R)\) never returned in the
source calculation. The literal degree-twelve chart additionally retains
\(4b+3a^2\ne0\). One must not invert \(s_0\) or a convenient coefficient
minor: the square factor may pass through \(A=0\). A surviving quotient
\(D_4=\Delta/S_4^2\) must be a separable quartic, with nonzero constant
and leading coefficients. Primitive actual bidegree, reduced disjoint
normalized ruling boundaries, exactly four normalized inverse points and
source extension remain additional tests. The binary formulation retains
square factors at infinity; this monic affine chart does not by itself.

Eligible affine discriminant degrees are even on the surviving boundary
stratum: the degree-two \(A\)-map has reduced zero and pole divisors and
therefore no branch over \(0,\infty\). In the binary degree-twelve
discriminant, odd order at infinity would contradict this. The completed
lower charts and independently reviewed degree-ten result consequently
leave this degree-twelve chart distinct. No emptiness, dimension or component
classification is claimed for it, and other contact distributions still need
their own binary discriminant and normalized inverse-point analysis.

## 6. Reconstructing an actual source from a marked elliptic target

This is a sufficient construction criterion, with a converse for the
surviving smooth order-two source. It also handles specified cone members;
it is not a classification of all cone projections.

Take a smooth elliptic curve \(E\), four distinct points \(Z=\sum P_i\),
and \(h_E:E\to Q\) birational onto an integral \(C'\ne C_0\), with
\(h_E^{-1}(C_0)_{\rm red}=Z\). Suppose
\(h_E(P_i)=C_0(t_i)\), with distinct \(t_i\in k^*\), and impose the
**component polarization**
\[
h_E^*\mathcal O_Q(1,1)\simeq\mathcal O_E(2Z).                    \tag{12}
\]
Glue \(P_i\) to \(t_i\) on \(c=\mathbf P^1_t\). The resulting nodal
curve \(Y=E\cup c\) has arithmetic genus four. The target maps agree at
the nodes and define \(h:Y\to Q\). Its dualizing bundle restricts as
\[
\omega_Y|_E=\omega_E(Z)=\mathcal O_E(Z),\qquad
\omega_Y|_c=\omega_c(\sum t_i)=\mathcal O_c(2).                  \tag{13}
\]

### 6.1 The canonical nodal union determines the quadric

The canonical map embeds \(Y\) in \(\mathbf P^3\) as an elliptic
normal quartic and a smooth plane conic meeting transversely at the four
marks. Exactly one quadric \(S_Y\) contains them, and it is integral,
possibly a cone.

To prove this directly for the reducible curve, \(h^0(\omega_Y)=4\).
Restriction to \(E\) has kernel \(H^0(\omega_c)=0\), so is an
isomorphism onto the complete degree-four series, which separates every
length-two subscheme by elliptic Riemann--Roch. Restriction to \(c\)
has kernel \(H^0(\omega_E)\), of dimension one, hence is the complete
conic series. The section defining its plane cuts exactly the reduced
\(Z\) on \(E\), so there are no further intersections and the elliptic
tangents are transverse to that plane. This gives the embedded nodal union.

The quadrics through the elliptic normal quartic restrict isomorphically
to the pencil of plane conics through \(Z\), using
\(H^0(\mathcal I_E(1))=H^1(\mathcal I_E(1))=0\). No three of the
four points are collinear, by Riemann--Roch with degree-one remainder.
The chosen conic therefore selects exactly one quadric. A reducible or
double-plane quadric cannot contain the integral nonplanar \(E\).
If smooth, \(S_Y=\mathbf P^1\times\mathbf P^1\), \(c\) has class
\((1,1)\), and degree and genus give \(E\) class \((2,2)\).
In either case a second independent quadric through \(E\) cuts it
scheme-theoretically: the proper complete intersection is unmixed of
degree four and already contains the integral degree-four curve. Hence
\(E\) is Cartier of class \(\mathcal O_{S_Y}(2)\). On a cone its vertex
cannot lie on smooth \(E\), by the two-quadric Jacobian, and the smooth
plane conic also avoids the vertex. Thus \(Y\) is Cartier in
\(|\mathcal O_{S_Y}(3)|\). The source quadric and its ruling pencil(s)
are determined by the marked nodal union, not tunable extra choices.

The closed-node gluing is a scheme pushout: the finite reduced node
scheme maps by closed immersions to the two projective components, meeting
the hypotheses in [Stacks, 0ECH](https://stacks.math.columbia.edu/tag/0ECH).
The proof above checks the particular canonical geometry directly; it
does not apply a smooth genus-four theorem to a reducible curve.

### 6.2 Node gluing is an additional torus class

Put \(\mathcal H=h^*\mathcal O_Q(1,1)\). Under (12),
\[
\kappa(Y,h)=[\mathcal H\omega_Y^{-2}]
\in\ker(\operatorname{Pic}Y\to\operatorname{Pic}E\times\operatorname{Pic}c)
\simeq(k^*)^4/k^*\simeq(k^*)^3.                                 \tag{14}
\]
Four fiber identifications at nodes have one common rescaling. Component
isomorphism does not fix these scalars; projective agreement of the maps
at the nodes does not make \(\kappa\) trivial.

There is an explicit residue formula. Let \(R(t)=\prod(t-t_i)\).
Represent \(x_0|_c\) in \(\omega_c^2(2\sum t_i)\) by
\(\tau_c=(dt)^2/R(t)^2\); as a section its divisor is \(4\infty\),
as required. Choose any component isomorphism on \(E\), and let
\(\tau_E\) represent \(h_E^*x_0\). Let \(r_i\ne0\) be its
quadratic residue, the coefficient of \((du/u)^2\) at \(P_i\).
It is independent of local parameter: replacing \(u\) by
\(au+O(u^2)\) changes \(du/u\) by a regular differential.
The dualizing generator of \(k[[u,v]]/(uv)\) restricts as
\((du/u,-dv/v)\); its square has equal leading coefficients.
The other three coordinates have matching ratios to \(x_0\) at each
node. Therefore
\[
\boxed{\kappa=1\quad\Longleftrightarrow\quad
 r_1R'(t_1)^2=\cdots=r_4R'(t_4)^2.}                             \tag{15}
\]
The component isomorphism rescales all four equally. This local algebra
proves the formula in characteristic zero; the quadratic-residue
interpretation also appears in [Wolpert, §2](https://arxiv.org/pdf/1204.3680),
whose complex analytic deformation results are not imported here.

### 6.3 Unique section recovery and the first-normal condition

If \(\kappa=1\), adjunction on either Gorenstein quadric gives
\(\omega_Y=\mathcal O_{S_Y}(1)|_Y\). The sequence
\[
0\to\mathcal O_{S_Y}(-1)\to\mathcal O_{S_Y}(2)\to\omega_Y^2\to0
\]
gives an isomorphism on global sections, because \(H^0=H^1=0\) for
its left term. This holds on the cone as well: use the hypersurface
sequence in \(\mathbf P^3\) and projective-space cohomology. All four
target sections extend uniquely, up to one common scalar, to \(U_i\).
Normalize that scalar to recover the literal parametrization on \(c\).
There is no adjustable extension space remaining for this fixed input.

Since the determinant vanishes on \(c\cup E\),
\[
q(U)=\Delta d_E r,\qquad r\in H^0(S_Y,\mathcal O_{S_Y}(1)),
\]
where \(\Delta\) cuts the conic and \(d_E\) cuts the elliptic quadric
section. The remaining contact condition is exactly
\[
r=\lambda\Delta,\qquad\lambda\ne0.                             \tag{16}
\]
Restriction \(r|_c\) has three binary-quadratic coordinates. No
independence or flexibility of these conditions in the target incidence
has been proved, and (15) is not known to imply (16).

If (12), (15), and (16) hold, the recovered tuple defines an **actual
admissible degree-eight carrier**. A common zero must lie on
\(q(U)=0\), whose reduced support is \(c\cup E\), where the tuple is
the prescribed morphism and has no common zero. This also checks the
cone vertex, outside that union. Ampleness makes the morphism finite.
For generic degree \(e\), projection of the target quadric divisor gives
\[
e[X\cap Q]=2[C_0]+[C'].
\]
The coefficient one at \(C'\), using birationality of \(h_E\), forces
\(e=1\). Every inverse point of \(C_0\) lies on \(c\cup E\), and
those on \(E\) belong to \(Z\subset c\). This proves full inverse
support, including isolated points. The image degree is eight.
Conversely every surviving smooth-source order-two admissible map gives
these data. The same converse holds for cone-source members with smooth
Cartier primitive residual and transverse four-point intersection.

This theorem constructs a normalization if all gates succeed. A mate
still requires the actual image's full conductor descent, or (2) in the
smooth-source coordinates. Reduced nodal gluing is not the full
conductor phase. The same component-versus-gluing distinction is formalized
for normalization/conductor squares by
[Ferrand, §2.2](https://www.numdam.org/article/BSMF_2003__131_4_553_0.pdf);
its patching theorem retains the full conductor schemes and does not
produce a suitable target or mate.

## 7. A balanced target passes the incidence and fails component polarization

Choose \(\eta^2=-4/5\), set
\(R=t^4+\eta t^3+\eta t+1\), and recover \(e_i\) by grouping the
coefficients of \(R^5\) modulo three. This gives a primitive actual
\((6,2)\) target curve. Its discriminant is
\[
\Delta=-3S(A)^2D(A),\quad
S=(\eta A+1)(A+\eta)(A^2-7\eta A+1),
\]
\[
D=5A^4+\frac{28}{5}\eta A^3+\frac{102}{25}A^2+
 \frac{28}{5}\eta A+5.
\]
The quartic is separable, so the normalization is elliptic:
\[
E:y^2=-3D(A),\qquad B=\frac{-e_1(A)+S(A)y}{2e_2(A)}.
\]
Restriction is \(R^5\), and \(\gcd(R(t),\Delta(t^3))=1\), so the
four target contacts are smooth and have precisely one normalized inverse
point each, with order five. The ruling boundaries are reduced and
pairwise disjoint, including the doubled roots visible in \(e_0,e_2\):
there \(\Delta\) has exact order two and the complementary coefficient
is a unit, giving two branches with distinct nonzero linear slopes.
The remaining boundary roots are simple. At \(A=0,\infty\), \(B\)
is finite nonzero on both normalized branches. The exact independent
[SymPy verifier](../computations/projection_palindromic_picard.py) checks
these assertions and reconstructs the target from \(R^5\).

Nevertheless (12) fails. Let \(H\) be the two infinities of the quartic
model, so \(L=\mathcal O_E(H)\) and
\(H^0(E,L^2)=\langle1,A,A^2,y\rangle\), by the pole orders and
elliptic Riemann--Roch. At the marks \(A=t^3\), the normalized coordinate is
\[
y\equiv\frac{27}{5}t^2(1-t^2)
\equiv\frac{27}{5}(1+\eta t+t^2+\eta t^3)\pmod R.
\]
Also \(A^2\equiv4/5+(9\eta/5)t-(9/5)t^2-(\eta/5)t^3\). Thus the
evaluation matrix of \((1,A,A^2,y)\) in \((1,t,t^2,t^3)\) is
\[
\begin{pmatrix}
1&0&4/5&27/5\\0&0&9\eta/5&27\eta/5\\
0&0&-9/5&27/5\\0&1&-\eta/5&27\eta/5
\end{pmatrix},\qquad\det=486\eta/25\ne0.
\]
Therefore \(H^0(L^2(-Z))=0\), so \(L^2\ne\mathcal O_E(Z)\).
The target passport gives \(M=L\mathcal Z\), and hence this is exactly
the failure of \(LM=\mathcal Z^2\). Geometrically the four marks do not
form a hyperplane section in the elliptic normal quartic \(|2L|\).
Its cone \(X_0X_2-X_1^2=0\) is not the nodal canonical quadric before
the component polarizations have been identified.

More generally, on a smooth quartic model \(y^2=f_4(A)\), with \(L\)
the degree-two \(A\)-fiber bundle, four finite marks with distinct
\(A\)-coordinates satisfy \(L^2=\mathcal O_E(Z)\) exactly when their
normalized \(y\)-values agree with a polynomial of degree at most two
in \(A\). Indeed, a section of \(\langle1,A,A^2,y\rangle\) vanishing
at all four marks must have nonzero \(y\)-coefficient, since a nonzero
quadratic polynomial cannot vanish at four distinct \(A\)-values.
Conversely that interpolating quadratic gives a nonzero section vanishing
at all four marks, and degree four forces its divisor to be exactly \(Z\).
This is a reusable component-polarization test, not an assertion that the
marked values in the present example pass it.

There is a useful general extraction for this balanced passport.
From \(F^{-1}(1)=5Z\) and \(M=L\mathcal Z\),
\(\mathcal Z^5=LM^3\), giving
\[
\delta=L^2\mathcal Z^{-1}\in\operatorname{Pic}^0(E)[2].
\]
One cannot cancel multiplication by two. All ramification indices are odd,
and the induced theta characteristic is
\[
\theta_F=F^*\mathcal O_{\mathbf P^1}(-1)\otimes\mathcal O_E(R_F/2)
=(LM^3)^{-1}M^2\mathcal Z^2=\delta.
\]
This is the odd-ramification pullback defined in
[Eskin--Okounkov--Pandharipande, §§1.1.1–1.1.2](https://arxiv.org/pdf/math/0312186).
On an elliptic curve the trivial degree-zero theta characteristic has
one section, while the other three have none. The component gate is
therefore equivalent to odd induced spin within this balanced class.
This example has nontrivial/even spin; local square roots of
\(dF/\omega_E\) exist but do not glue to a meromorphic square.
It fails before node residues, section recovery, source contact, or mate
descent. Those later gates were not run. Neither its passport nor even
spin has been proved universal for all elliptic targets.

## 8. A paired elliptic construction clears the component gate and fails node gluing

This gives actual functions with trivial spin and principal ruling divisors.
Spin alone would not suffice: if
\(\operatorname{div}(F)=3D_0+U_0-3D_\infty-U_\infty\), with boundary
degrees six and two, the class \(\beta=[D_0-D_\infty]\) obstructs a
function \(B\) with that divisor. Existence of \(A\) only forces
\(3\beta=0\). When \(\beta=0\), \(A=B^3/F\) supplies both rulings.
The following base change controls those divisors explicitly.

Set
\[
a=-7+4\sqrt3,\quad u=(a-1)/4=-2+\sqrt3,\quad s=2\sqrt6/3,
\]
so \(u^2=-a\), \(s^2=8/3\). Put
\[
F_0(x)=(x-1)^3(x-a),\quad r=F_0/x^2,\quad R_0=r(u),
\]
\[
D=-6F_0+R_0(2s+3)x^2,\qquad
N=12sF_0-3R_0(2s+3)x^2,\qquad q=N/D.                            \tag{17}
\]
Here \(q\) is an auxiliary rational map, not the target quadric equation.
Direct differentiation gives
\(r'=2(x-1)^2(x-u)^2/x^3\). Its branch fibers are \((3,1)\),
\((3,1)\), \((2,2)\) over \(0,R_0,\infty\), which postcomposition
sends to \(-3,3,-2s\). They are distinct and avoid \(2s\), so \(q\)
is unramified over \(2s\) and infinity.

Normalize
\[
h+s^2/h=q(x).                                                     \tag{18}
\]
The double cover \(x:E\to\mathbf P^1\) branches at the four simple
points \(q=2s\); its even discriminant orders at \(q=-2s\) and the
simple poles add no branches. Thus \(E\) is smooth connected elliptic.
The involution \(h\mapsto s^2/h\) has the four points \(h=s\) as its
fixed set. The degree-four map \(h\) has two index-three ramification
points over \(x=1\) and two over \(x=u\), exhausting its eight
ramification units. At the normalized points over \(q=\pm2s\),
\(h\mp s\) is a uniformizer and adds no ramification for \(h\).

Define
\[
g(z)=\frac{(z-1)^3(3z^2+9z+8)}{(z+1)^3(3z^2-9z+8)},\quad
F=g(h),\quad T(x)=\frac{x-1}{x-u},
\]
\[
B=T(x)\frac{h-1}{h+1},\qquad A=T(x)^3\frac{q-3}{q+3}.
\]
The odd-cover ramification can be checked without a branching
assumption. Put
\[
P(z)=(3z^5-10z^3+15z)/15,\qquad P'(z)=(z^2-1)^2.
\]
Then \(g=(P-8/15)/(P+8/15)\), so its only ramification indices are
three at \(z=1,-1\), and five at infinity. Its fiber over one is exactly
five times infinity. Consequently composition with the degree-four
\(h\)-map gives exactly the claimed \(5Z\) contact fiber; its other
ramification is read from the explicit factors below.

The quotient coordinate \(z+s^2/z\) pairs the two roots of each
quadratic in \(g\), giving
\(F=((h-1)/(h+1))^3(q+3)/(q-3)=B^3/A\).
The remaining simple point of \(r=R_0\) is \(v=u+4\), and cancellation
of the triple factors gives
\[
A=c_A(x-v)/(x-a),\quad c_A\ne0.
\]
Thus \(\deg A=2\). The zeros of \(B\) are the four simple \(h=1\)
points and the two \(x=1\) points; its poles are the four \(h=-1\)
points and the two \(x=u\) points. All are distinct. The \(A\)-boundary
fibers \(x=v,a\) are reduced and disjoint from them. The \(h=\pm1\)
values correspond to \(q=\pm11/3\), unramified and distinct from all
three branch values; infinity adds no collision. The two functions recover
\(x\) and then \(h\), so their target map is birational onto an integral
\((6,2)\) curve.

Let \(H_x\) be the degree-two fiber class and \(H_h\) the degree-four
fiber class. Choose a fixed point of the involution as origin. Its fixed
point divisor is all four two-torsion points, of class \(4O\), while
\(H_x=2O\); hence \(H_h=2H_x\). Half the ramification divisor of \(h\)
is also two \(x\)-fibers, so its spin is trivial. More concretely the
actual divisors above give
\[
L=\mathcal O_E(H_x),\quad M=L^3,\quad
Z=h^{-1}(\infty),\quad\mathcal O_E(Z)=L^2.                       \tag{19}
\]
The degree-twenty map has fibers \((3^6,1^2)\) over zero and infinity,
and \(5Z\) over one. The four marks lie over the four distinct roots
\(x_i\) of \(D\), with \(t_i=T(x_i)\), \(A(P_i)=t_i^3\).
They are distinct finite nonzero parameters. The \(A\)-map is unramified
there, its values are distinct, so these are smooth target contacts of
order five, with no additional normalized inverse points. This supplies
the full input of section 6 and (12), not just a passport.
The canonical source quadric is a cone: \(T\) is a Möbius function of
\(A\); if it were smooth, the interpolation lemma would identify both
source ruling pencils and destroy the embedding.

The pairing idea is consistent with the explicit elliptic odd-cover
framework in [Moschetti--Pirola, §§2–3 and 5](https://arxiv.org/html/2011.12159v1).
That paper's results are over the complex numbers; no general involution-
lifting theorem, prescribed-fiber existence theorem, or monodromy argument
is needed for the algebraic construction (17)–(19).

### 8.1 The exact residue obstruction

A smooth quartic model of (18) is
\[
Y_0=(2h-q)D/x,\quad
Y_0^2=\frac{N^2-4s^2D^2}{x^2}
=\frac53R_0\bigl(24sF_0-R_0(2s+3)^2x^2\bigr).                  \tag{20}
\]
Its right side is separable quartic with nonzero constant and leading
coefficients; \(x=0,\infty\) each have two unramified branches.
With \(H_\infty=x^*(\infty)\),
\[
\operatorname{div}(Y_0)=\operatorname{Ram}_x-2H_\infty,
\qquad \operatorname{div}(h-s)=\operatorname{Ram}_x-Z.
\]
The target section \(x_0\) has zero divisor
\(x^*(a)+x^*(u)+h^*(-1)\). Its representing quadratic differential,
up to one scalar, is
\[
\tau_E=(x-a)(x-u)(h+1)(h-s)\,dx^2/Y_0^3.                         \tag{21}
\]
Direct addition of those full divisors, including the two infinities,
gives \(\operatorname{div}(\tau_E)=\operatorname{div}(h_E^*x_0)-2Z\);
this verifies the actual component identification, not just its degree.

At the marked branch \(h=\infty\) over \(x_i\),
\(Y_0(P_i)=N(x_i)/x_i\) and
\(h\sim N(x_i)/(D'(x_i)(x-x_i))\). The opposite sign is the unmarked
\(h=0\) branch. The residue of (21) is
\[
\rho_i=\frac{x_i^3(x_i-a)(x_i-u)}{N(x_i)D'(x_i)^2}.
\]
For \(R_{\rm mark}(t)=\prod(t-t_i)\), the Möbius marking gives
\[
R_{\rm mark}(T(x))=c\frac{D(x)}{(x-u)^4},\quad
R_{\rm mark}'(t_i)=\frac{cD'(x_i)}{(1-u)(x_i-u)^2},\qquad c\ne0.
\]
At a root of \(D\), \(N(x_i)=5R_0x_i^2/3\). Thus the four entries
\(\rho_iR_{\rm mark}'(t_i)^2\) differ by a common nonzero factor from
\[
J(x_i),\qquad J(x)=\frac{x(x-a)}{(x-u)^3}.
\]
They cannot all agree: otherwise a polynomial
\(x(x-a)-\lambda(x-u)^3\), of degree at most three, would vanish at
the four distinct \(x_i\), and would have to vanish identically, which
its coefficients forbid. Therefore \(\kappa\ne1\).

This target passes component polarization and fails actual node gluing.
No section recovery, first-normal determinant test, carrier construction,
or full-conductor mate test was performed after that failure. The proof
uses exact divisors and local expansions; no numerical sample or new
candidate enumeration is necessary. Its independent source review covers
both the positive construction and the residue calculation.

## 9. Synthesis: what is shared, what is still missing

The recurring mechanism is **compatibility with a fixed polarization and
its actual sections**, at several different geometric levels. The
rank-one determinant converts the actual four sections into ruling bundles
on a potentially nonreduced divisor. Riemann--Hurwitz then detects how much
contact can be concentrated, while elliptic Picard identities retain what
numerical degrees forget. Canonical reconstruction makes the source
intrinsic to the marked nodal union. Its extension problem splits into
three genuinely different gates:

\[
\text{component Picard identity}\quad\longrightarrow\quad
\text{node gluing in }(k^*)^3\quad\longrightarrow\quad
\text{nonzero first-normal determinant}.
\]
These arrows mean successive requirements, not that one implies the next.
The balanced palindromic example fails at the finite two-torsion defect;
the paired example removes that defect and fails in the gluing torus.
They are different failures. Even success at all three would produce an
actual carrier, after which full-conductor descent remains another problem.
Ferrand patching explains the common descent architecture, but no equality
between the nodal class and the surface conductor phase has been proved.

The boundary proof isolates the essential characteristic-zero input:
separable Riemann--Hurwitz and the cubic exponent dominating every
first-ruling zero/pole order (at most two). For other graph equations or
larger ruling degree, cancellation can erase boundary points, so (10) and
the clean passport equality require a new analysis. The canonical extension
theorem itself does not require balanced contact or a passport enumeration;
it only requires its stated target map, four nodes, component polarization,
gluing, and determinant. This broadens the **construction interface** within
its stated genus-four geometry, without broadening an exclusion theorem.

A concrete possible construction should therefore build the elliptic
sections as quadratic differentials whose four residues already match the
marked rational component, while controlling \(A,B\) and their complete
inverse divisor. Odd spin alone does not control the three-torsion ruling
divisor issue, node gluing, or the first-normal determinant. Conversely,
for a target on which the actual residue ratio descends to a nonconstant
map \(J\) of degree \(d\), more than \(d\) distinct marks cannot all
have the same gluing value. The paired construction is an exact instance
with \(d=3\), not a general proof that every target has such a low-degree
ratio.

The remaining bounded tests are precise: solve the general order-one
contact-26 incidence; on order two solve the primitive elliptic target
incidence outside the excluded support locus, then the component, residue,
and determinant gates; and on an actual admissible image solve full mate
descent. No degree bound or exhaustive reduction sends arbitrary STCI
pairs to this interface. Both possible outcomes of the unrestricted
existence problem remain visible.

There is also an actual higher-degree inverse source, rather than only a
logical exception to these tests. The [five-parameter elliptic double inverse](elliptic_double_inverse_construction.md)
has complete global coordinate lifts and a fixed birational octic member.
Its first unresolved condition is absence of extra inverse support on a
smooth, basepoint-free birational stratum, followed by pure-power descent.
Its length-twelve fixed-member failure neither excludes that whole family
nor transfers the rational-diagonal symmetry argument to it.

### 9.1 What extends to positive characteristic

The fixed curve is an STCI on a quartic carrier in **every** positive
characteristic; the [explicit construction and its exact scope](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier)
belong alongside the characteristic-zero carrier exclusion. The present
restricted degree-eight interface neither contradicts that construction nor
covers every possible carrier. The different mechanisms have different
characteristic boundaries:

| Mechanism | What its proof actually permits |
| --- | --- |
| Complete Segre source, ampleness/finiteness, membership (2), matrix-cokernel degrees, determinant orders (3) | These use line bundles, Euler characteristics, and intersection degrees, and hold over an algebraically closed field in every characteristic. The Segre-coordinate nine-parameter endpoint contradiction also uses only the incompatible conditions \(e_3=0,1\), so persists. |
| Symmetric coordinates and first-normal isomorphism | The coordinates \(y=(b+c)/2\), normal form (4), and the balanced normal splitting need \(2\) invertible. The Euler-class argument uses degree four, nonzero precisely away from characteristic two; it does not require dividing by three. In characteristic two the conormal splitting changes as stated in R-0020, so these parameter descriptions cannot be imported. |
| Riemann--Hurwitz support inequalities | For separable quotient functions the same lower bounds follow using the different divisor, whose coefficient is at least \(e_P-1\). The equality/passport arguments additionally force that no wild different or further ramification remains. Each quotient's separability and boundary cancellation must therefore be checked in the proposed characteristic; the characteristic-zero boundary theorem is not claimed here without those checks. In particular indices three or five in the displayed passports cannot be presumed tame at those primes. |
| Elliptic interpolation and component Picard identities | Riemann--Roch, the degree-two interpolation proof, and Picard cancellation without extracting roots are characteristic independent once their stated smooth-curve, four-distinct-mark, and ramification-divisor inputs hold. A degree-two map from the smooth elliptic curve to \(\mathbf P^1\) is necessarily separable even in characteristic two: a purely inseparable one would factor through Frobenius followed by a degree-one map from a genus-one Frobenius twist to \(\mathbf P^1\), impossible by genus. In characteristic two, wild different and the changed branch-point geometry prevent importing the four-reduced-branch-point argument of section 4.1 unchanged. |
| Canonical nodal reconstruction, gluing torus, unique section recovery, admissibility criterion | The direct proof of section 6 works algebraically in any characteristic for its stated smooth elliptic input, four distinct ordinary nodes, actual component polarization, and the nonzero determinant condition. It uses no separability theorem or division by two. The local generator \((du/u,-dv/v)\) and its squared matching rule remain valid in characteristic two. This is a conditional source-construction theorem, not existence of input data in a new characteristic. |
| Two-torsion/spin interpretation | The elliptic count of four square roots and the finite two-torsion picture use characteristic different from two. The odd-ramification theta construction requires a separable tame cover with odd indices so its actual different divisor is the one being halved. Neither a characteristic-two square-root count nor wild spin extension is inferred. |
| The two explicit elliptic examples and rational certificates | These were verified over characteristic-zero number fields. Their constants, separability, nonvanishing, normalized branch counts, and evaluation determinants require new reduction checks at a prime. For example the palindromic determinant \(486\eta/25\) and its model do not support the same conclusion at 2, 3, or 5; the paired construction has denominators and quadratic radicals at these primes. No uniform good-prime classification is asserted. |

The useful characteristic-independent architecture is to retain actual
line bundles, node identifications, and full inverse support. The specific
characteristic-zero obstructions often use separability or a nonvanishing
integer coefficient. On the later full conductor, nilpotent units can
have their defects removed by Frobenius powers in positive characteristic;
there is no characteristic-zero torsion-rigidity inference valid for them
in all characteristics. Reduced nodal gluing instead lies in a torus,
so the nilpotent Frobenius mechanism and its three scalar equations are
different descent phenomena.

**Provenance.** This mathematical home consolidates the actual projection
and elliptic-gluing family at source snapshot `76804e6`, including distinct
arguments in its audits and exact scripts. Source review is reused only
for unchanged scoped claims. Historical logs and candidate-selection
narratives have no mathematical role in the statements above.

## Ambient coincidence and local conductor phase

The following restrictions concern prescribed normalization or pinching
data. They do not construct a conductor, its full finite algebra, or
four sections descending to the required embedded surface.

**One ambient symmetry.** Let \(k\) be algebraically closed, and let
\(f:\mathbf P^2\dashrightarrow\mathbf P^3\) be birational onto its
image, represented by homogeneous forms \(F_0,\ldots,F_3\) of degree
\(d>0\) with no common divisorial factor. Suppose a single nonidentity
\(\sigma\in\operatorname{PGL}_3(k)\) satisfies
\(f(p)=f(\sigma p)\) on a dense open subset of each irreducible
component of a reduced divisor \(D\subset\mathbf P^2\). Then
\[
 \deg D\le2d.
 \tag{P1}
\]
Choose a linear representative for \(\sigma\). Every crossminor
\[
 F_i(F_j\circ\sigma)-F_j(F_i\circ\sigma)
\]
is a homogeneous form of degree \(2d\) vanishing on \(D\). The
squarefree defining equation of \(D\) divides every crossminor. If
\(\deg D>2d\), all crossminors vanish identically. Hence
\(f=f\circ\sigma\) as rational maps. Composing with a rational inverse
to the birational map onto its image forces \(\sigma=\mathrm{id}\),
a contradiction. This proves the coincidence bound, in every characteristic.

For quartic forms the bound is eight. A multiplicity-weighted conductor
class, such as \(51L\), does not determine its reduced degree. The
argument applies to one ambient automorphism: components paired by
different automorphisms cannot have their degrees added in that bound.
A conductor deck map need not extend to a projective automorphism of
\(\mathbf P^2\), so the lemma does not bound a general conductor.

**Local tame phase.** Let \(B\subset\mathbf P^2_k\) be an integral
curve, smooth at \(p\in B\cap L\), where \(L=(z=0)\) and \(B\ne L\).
Suppose an automorphism \(\tau\) of \(B\) has finite order \(e\), fixes
\(p\), and acts on the one-dimensional cotangent space at \(p\) by a
primitive \(e\)-th root \(\xi\in k\). Assume \(k\) algebraically
closed and \(\operatorname{char}k\nmid e\); characteristic zero is
included. Let \(F_i\) be a quartic form nonzero at \(p\), put
\[
 q=(z^4/F_i)|_B\in k(B),\qquad k_p=\operatorname{ord}_p(z|_B)>0,
\]
where the order uses any local trivialization of the hyperplane line
bundle. If \(q^b\) is \(\tau\)-invariant for some \(b>0\), then
\[
 \frac{e}{\gcd(e,4k_p)}\mid b.
 \tag{P2}
\]
Indeed \(q\ne0\) and \(\operatorname{ord}_p(q)=4k_p\).
Invariance gives \((\tau^*q/q)^b=1\) in \(k(B)\). Since \(k\) is
algebraically closed, \(\tau^*q/q\) is a constant root of unity.
Choose a local parameter \(t\) at \(p\). The cotangent action says
\(\tau^*t=\xi t+O(t^2)\), so comparison of leading terms of \(q\)
gives \(\tau^*q/q=\xi^{4k_p}\). Its order is
\(e/\gcd(e,4k_p)\), proving the stated divisibility.

The existence of a primitive root of order \(e\) and the faithful
cotangent action are explicit tame hypotheses. No assertion for wild
inertia with nonfaithful cotangent action follows. The lemma also
supplies neither the automorphism nor compatible global sections,
admissibility, or nilpotent-conductor descent. It is a conditional
consequence within the full phase criterion, without a replacement
for that criterion.

The two conditional lemmas were independently reconstructed with their reduced-divisor, single-automorphism, birationality and tame-cotangent hypotheses. Neither supplies the missing conductor or globally descending sections.
