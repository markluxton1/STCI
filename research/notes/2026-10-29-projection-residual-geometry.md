# Residual geometry of the marked smooth-quadric projection source

October 29, 2026. Status: **provisional geometric reduction**, independently
derived by `projection_geometry`; not a computation of the admissible locus
and not a promoted result. This note uses the marked source in the
[candidate record](2026-10-28-stci-search-candidates.md), Section 4. Its
purpose is to separate the possible determinant strata before solving
their remaining contact equations.

Work over an algebraically closed characteristic-zero field. Put
\(S=\mathbf P^1\times\mathbf P^1\), \(c=(\Delta=0)\) the diagonal,
\(H=\mathcal O_S(2,2)\), and
\[
U_i=B_i+\Delta A_i,
\qquad A_i\in H^0(S,\mathcal O_S(1,1)),
\]
with the four fixed restrictions
\((s^4,s^3t,st^3,t^4)\) on \(c\). Assume throughout that the four
sections are basepoint free. Thus \(f:S\to\mathbf P^3\) is finite onto
its integral image, since \(H\) is ample. Let
\[
Q=(x_0x_3-x_1x_2=0),\qquad
M=\begin{pmatrix}U_0&U_1\\U_2&U_3\end{pmatrix}.
\]
The target quadric is identified with \(\mathbf P^1_A\times
\mathbf P^1_B\) by
\(x_0=A_0B_0,x_1=A_0B_1,x_2=A_1B_0,x_3=A_1B_1\).
The target curve has equation
\(A_1B_0^3-A_0B_1^3=0\), of bidegree \((1,3)\).

## 1. Only determinant orders one and two can survive

Suppose \(q(U)=\det M\ne0\). Let
\[
E=V(q(U))=m c+D,
\quad D\in|\mathcal O_S(4-m,4-m)|,
\quad c\not\subset D,
\]
where \(m\ge1\) is maximal. The divisor \(D\) can be reducible or
nonreduced. Since \(M\) has rank one everywhere on \(E\) (rank zero
would be a basepoint), its cokernel is an invertible sheaf \(L\) on
the full scheme \(E\). Locally, a unit matrix entry reduces the matrix
by row and column operations to \(\operatorname{diag}(1,q(U))\), proving
this assertion also on nonreduced components. There is a resolution
\[
0\longrightarrow\mathcal O_S(-2,-2)^{\oplus2}
\xrightarrow{M}\mathcal O_S^{\oplus2}
\longrightarrow i_*L\longrightarrow0.
\]
Consequently
\(\chi(L)=2\chi(\mathcal O_S)-2\chi(\mathcal O_S(-2,-2))=0\).
As \(p_a(E)=9\), the degree defined by Euler characteristics is
\(\deg_E L=8\). The line bundle \(L\) is the pullback of
\(\mathcal O_{\mathbf P^1_A}(1)\): its quotient presentation is
\(\mathcal O_E^{\oplus2}/\langle(A_0,A_1)\rangle\). In particular it
is globally generated. On \(c\), the rank-one factorization is
\[
M|_c=\binom{s^3}{t^3}(s\ t),
\qquad L|_c=\mathcal O_{\mathbf P^1}(3).
\]

Degree of an invertible sheaf on a projective curve is additive on its
component cycle. This follows either from the cycle definition or by
tensoring the divisor-union exact sequences and subtracting the same
Euler-characteristic calculation for the structure sheaves. Hence it
remains valid for \(mc\) and arbitrary nonreduced \(D\), and gives
\[
\deg_D L=8-3m.
\]
Global generation makes this degree nonnegative on every nonzero
effective component. If \(D=0\), then \(m=4\) by its divisor class,
whereas the degree identity would give \(8=12\), also impossible.
Therefore
\[
\boxed{m\in\{1,2\}.}
\]
In particular, a basepoint-free tuple with
\(q(U)\in\Delta^3H^0(\mathcal O_S(1,1))\) must have \(q(U)=0\).
This is an exact exclusion of higher determinant-order strata, not a
genericity assumption.

## 2. The identically zero determinant stratum has basepoints

If \(q(U)=0\), the map lands in \(Q\). Write
\(f^*\mathcal O_Q(1,0)=\mathcal O_S(a,b)\). Both ruling pullbacks are
globally generated and sum to \(H\), so \(0\le a,b\le2\). Their
restrictions to \(c\) have degrees three and one, giving \(a+b=3\).
Thus \((a,b)=(1,2)\) or \((2,1)\). Since the target curve has class
\((1,3)\), its scheme pullback is a divisor of class
\[
(a,b)+3(2-a,2-b)=(4,2)\quad\hbox{or}\quad(2,4).
\]
Neither can be supported solely on \(c\), since every divisor supported
on that irreducible curve has equal ruling degrees. There is in fact a
stronger contradiction to basepoint freedom: a pullback of a ruling has
self-intersection zero, whereas \(\mathcal O_S(1,2)^2=
\mathcal O_S(2,1)^2=4\). The morphism to \(Q\) would be finite onto
\(Q\), by ampleness of \(H\), so this contradicts the intersection
projection formula. Hence the identically zero determinant stratum has
no basepoint-free tuples. The stronger argument was independently
supplied by reviewer `projection_audit`.

## 3. Exact remaining residual-contact conditions

For \(m=1,2\), the two ruling pullbacks on \(D\) have degrees
\[
\deg_D f^*\mathcal O_Q(1,0)=8-3m,
\qquad
\deg_D f^*\mathcal O_Q(0,1)=8-m.
\]
The second equality follows from
\(\deg_DH=H\cdot D=16-4m\). The section defining the target curve
therefore restricts to a section of degree
\[
(8-3m)+3(8-m)=32-6m,
\]
namely 26 on the \(m=1\) stratum and 20 on the \(m=2\) stratum.
The scheme \(D\cap c\) has length \(c\cdot D=8-2m\), namely six or
four. Full inverse support requires the zero support of that restricted
section to lie entirely in this scheme's support. It also requires that
no component of \(D\) map into the target curve, since such a component
would itself be unwanted inverse support.

On a reduced residual component not mapping into the target curve the
section has its usual zero divisor, so the preceding numbers give the
total contact degree summed with the component multiplicities. For
nonreduced \(D\), support avoidance must be tested in the full residual
coordinate ring or after restriction to its reduction; the degree count
does not replace that algebraic test. In particular, the count does not
assert transverse contact at the diagonal, and cannot itself subtract
six or four to claim a universal off-diagonal length.

Thus there are only two possible nontrivial determinant strata, but on
each one a large, explicitly bounded contact incidence remains. Neither
this argument nor the degree calculation decides its emptiness. Full
inverse support, birationality, and the later pure-power descent test
remain separate conditions.

## 4. First-normal differential and the symmetric boundary

In characteristic zero the first-normal derivative map for this affine
source is an isomorphism on its twelve antisymmetric parameters:
\[
H^0(\mathcal O_c(2))^{\oplus4}
\xrightarrow{\sim}
H^0(N_{C/\mathbf P^3}\otimes\mathcal O_c(-2))
=H^0(\mathcal O_c(5))^{\oplus2}.
\]
Here antisymmetric means under interchanging the two source factors;
an antisymmetric \((2,2)\) section is \(\Delta\) times a symmetric
\((1,1)\) section. The normal-bundle splitting is the promoted
[R-0020](../results/quartic_conormal_characteristic_jump.md).

To check injectivity, a kernel element would give a tangential normal
derivative in
\(H^0(T_c\otimes N_{c/S}^{-1})=H^0(\mathcal O_c)=k\). The Euler
sequence on the embedded curve, tensored by \(\mathcal O_c(-2)\), is
\[
0\to\mathcal O_c(-2)\to\mathcal O_c(2)^{\oplus4}
\to T_{\mathbf P^3}|_C\otimes\mathcal O_c(-2)\to0.
\]
The tangent generator maps under its connecting homomorphism to the
extension class of the pulled-back Euler sequence on \(c\), a nonzero
multiple of \(\deg\mathcal O_C(1)=4\) in
\(H^1(\mathcal O_c(-2))\). It consequently does not lift to the middle
term. The kernel is zero, and dimensions on both sides are twelve.

There is also a direct coordinate check of the kernel assertion. On an
affine diagonal chart, write the four antisymmetric first derivatives as
arbitrary polynomials \(h_i(t)\) of degree at most two. After the
projective normalization by the first coordinate, two normal derivative
polynomials can be chosen as
\[
A=h_2-3t^2h_1+2t^3h_0,
\qquad
B=h_3-\tfrac32t h_2+\tfrac12t^3h_1.
\]
They have degree at most five. These are the usual affine normal
coordinates \(x_2-x_1^3\) and \(x_3-x_1^4\), after taking the second
minus \(3t/2\) times the first. If \(A=B=0\), comparison successively
of degrees five, four, and three in \(A\), then degrees five and four in
\(B\), reduces \(h_0\) to zero and \(h_1\) to a constant. The remaining
degree-three coefficient in \(B\) is minus four times that constant, so
all four \(h_i\) vanish. This directly proves injectivity over the
stated characteristic-zero field without using a dimension heuristic.

It follows that identically zero first-normal derivative means all four
sections are symmetric. For each fixed binary-quartic restriction the
symmetric lift is unique up to a scalar multiple of \(\Delta^2\), so
this is an affine four-dimensional boundary of the sixteen-dimensional
source. Its maps factor through the interchange quotient
\(S\to\operatorname{Sym}^2\mathbf P^1=\mathbf P^2\), and cannot be
birational. In particular, a birational admissible tuple must have a
nonzero pair of normal quintics; their common zero divisor has degree
at most five.

The order-two determinant condition is particularly explicit in these
parameters. The normal exact sequence for \(C\subset Q\subset\mathbf
P^3\) is
\[
0\to\mathcal O_c(6)\to\mathcal O_c(7)^{\oplus2}
\to\mathcal O_c(8)\to0.
\]
After tensoring by \(N_{c/S}^{-1}=\mathcal O_c(-2)\) and taking
sections, its last map is surjective, with five-dimensional kernel
\(H^0(\mathcal O_c(4))\). The vanishing of the first-normal derivative
of \(q(U)\) thus imposes seven independent affine-linear conditions on
the original sixteen parameters. Before basepoint and finiteness
screening, the order-at-least-two locus is an affine nine-dimensional
space. Its first-normal differential is a quartic scalar multiplying
the fixed inclusion \(\mathcal O_c(6)\hookrightarrow
\mathcal O_c(7)^{\oplus2}\). When it is nonzero its common zero divisor
has degree exactly four. The order-one determinant stratum is the
complement of this affine subspace. The higher-order and zero-determinant
boundaries inside the nine-dimensional space cannot be basepoint free,
by Sections 1 and 2.

For explicit computation, put
\(a=u_0v_0\), \(h=(u_0v_1+u_1v_0)/2\),
\(d=u_1v_1\), so \(ad=h^2-\Delta^2/4\). All nine-dimensional
tuples have the form
\[
U=(a^2,ah,hd,d^2)+\Delta(L_0,L_1,L_2,L_3)
+\Delta^2(\kappa_0,\kappa_1,\kappa_2,\kappa_3),
\]
with five parameters \(A,B,C,D,E\) and
\[
\begin{aligned}
L_0&=Aa+Bh,&L_1&=Ca+Ah+Bd,\\
L_2&=Da+Eh-Cd,&L_3&=Dh+Ed.
\end{aligned}
\]
The determinant is \(\Delta^2R\), with \(R\) a quadratic on the
Segre quadric. On the affine diagonal chart \((s,t)=(1,t)\), its
restriction is the quartic
\[
R|_c=(\kappa_3-CD)+(-\kappa_2-CE)t
+(C^2-\tfrac14)t^2+(-\kappa_1+AC)t^3
+(\kappa_0+BC)t^4.
\]
In the normal-coordinate convention used above the scalar quartic
for the first-normal differential is
\[
g(t)=D+Et-4Ct^2-At^3-Bt^4.
\]
These formulas retain all nine parameters, rather than choosing a
convenient nonzero minor or excluding endpoint roots. They also show
explicitly that the residual intersection quartic and normal
ramification quartic are different data.
The [exact symbolic determinant control](../computations/stci_projection_residual_geometry_2026_10_29.m2)
checks the full identity \(\det M=\Delta^2R\) over the polynomial
ring with all nine parameters, modulo
\(ad-h^2+\Delta^2/4\); its
[saved output](../computations/stci_projection_residual_geometry_2026_10_29.txt)
is `M2_NINE_PARAMETER_DETERMINANT_IDENTITY_PASS`. This verifies the
parameterization's determinant formula, not basepoint freedom or full
inverse support.

This observation does not exclude isolated ramification points. A
prospective global conductor comparison would have to control their
multiplicities, rather than count their support. For a degree-eight
normalization with smooth source the conductor divisor has class
\(f^*K_X-K_S=(10,10)\), meeting \(c\) in degree twenty. The possible
concentration of that contact at the zeros of the normal quintic pair
is a further interface, not a completed obstruction.

## 5. A finite branch passport on a smooth residual boundary

There is a sharper condition on the following explicitly restricted open
part of the \(m=2\) stratum. Assume \(D\) is smooth and irreducible,
and that the zero and pole divisors of its two target ruling functions
\(A=A_1/A_0\) and \(B=B_1/B_0\) are reduced and pairwise disjoint.
They have degrees two and six respectively. Then
\[
f_D=A/B^3:D\longrightarrow\mathbf P^1
\]
has degree twenty. Its fibers over zero and infinity each have
multiplicity partition \((3^6,1^2)\), contributing twelve ramification
units per fiber. Full inverse support makes its fiber over one supported
on \(c\cap D\), a scheme of length four. Thus that fiber contributes
at least \(20-4=16\) further ramification units. Since \(D\) has genus
one, Riemann--Hurwitz gives exactly forty total ramification units.
The lower bound \(12+12+16=40\) is therefore equality.

Consequently \(c\cap D\) consists of four distinct points, these are
exactly the points of \(f_D^{-1}(1)\), and \(f_D\) is ramified only
over \(0,1,\infty\). Its remaining multiplicity partition is a partition
of twenty into four positive parts. This is a finite branch-passport
restriction at degree twenty; it does not assert that every such cover
occurs in the projection source. In particular the residual elliptic
curve and cover belong to one of finitely many isomorphism classes of
degree-twenty three-branch-value covers. Determining which classes admit
the required \((2,2)\) embedding, marked intersection, and four sections
is an additional finite algebraic incidence problem.

This argument does not cover singular or reducible \(D\), coinciding
boundary divisors, or nonreduced endpoint fibers. Those are surviving
strata, not exceptions that can be discarded. It also does not compute
the indicated finite covers. The \(m=1\) smooth residual has genus four
and ruling degrees five and seven; the analogous calculation leaves up
to ten additional ramification units and supplies no three-branch-value
conclusion.

## Scope and verification

No accepted quartic proof or previous fixed candidate was rerun. The
new arguments are the determinant-order exclusion, the full-inverse
failure on the zero-determinant stratum, and the residual ruling/contact
calculation. They apply to this complete marked smooth-quadric source,
with basepoint freedom retained. They do not apply to the cone or plane
normalization sources and do not establish unrestricted STCI
nonexistence. The determinant, differential and conditional passport
arguments are independently reconstructed in
[the projection audit](2026-10-29-projection-locus-audit.md).
Later [boundary exclusions](2026-10-29-projection-m2-boundary.md) and
[the smooth residual audit](2026-10-29-projection-m2-doublecover-audit.md)
strengthen the surviving order-two description without deleting these
earlier proofs.
