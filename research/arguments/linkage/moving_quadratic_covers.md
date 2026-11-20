# Moving the quadratic conductor to a prescribed point

Work over an algebraically closed field of characteristic zero. Use
\([A:B:C:D]=[s^4:s^3t:st^3:t^4]\) for the coordinates of the fixed
quartic \(C_0\), and let \(Q=AD-BC\). Write \(V\) for the four-dimensional
series of ambient linear forms on the parametrizing line. A quartic
section \(w\notin V\) completes this series to the rational normal
quartic. Every lift of \(w^2\) to an ambient quadric has the form
\(R_0+\lambda Q\): on the smooth quadric the nine biforms of type
\((2,2)\) restrict to the nine monomials of degree eight.

## The boundary of the actual intersection

Let \(Y=V(F_a,G_b)\) be a proper CI with sole reduced support \(C_0\).
In the finite flat cover \(Z^2=R\), the two reduced lifts \(Z=\pm w\)
are distinct rational normal quartics. They coincide precisely at
\(\operatorname{div}(w)\). Extract the full primary component of one
lift. Over the generic Artin algebra the two roots lift uniquely since
\(2w\) is a unit. The CI has no embedded components, so the image of
the homogeneous algebra \(A_Y=S/(F,G)\) in the primary component is
faithful. Its saturated coordinate ring is \(B_Y=A_Y+A_YZ\), by
contraction from the chosen generic primary component and the monic
quadratic relation. More explicitly, project the quadratic algebra
localized at the sole associated prime of \(A_Y\) onto either factor
and contract the kernel. This kernel is homogeneous, since the named
reduced lift fixes the primary component under scaling. Any ambient
linear form nonzero on \(C_0\) is regular on the image, so the resulting
primary ideal is saturated. This argument also applies to a singular cover.

Put \(T=A_Y/\mathfrak c=S/J_\Delta\) for the conductor quotient. It
gives \(B_Y/A_Y=T(-1)\). The quotient is supported projectively on
\(\operatorname{div}(w)\), since a root lifts through the nilpotent
ideal wherever \(w\ne0\). The omitted section \(w\notin V\) gives
\((B_Y/A_Y)_1\ne0\). The same exact sequence, the depth-two CI ring,
and saturation of \(B_Y\) give \(H^0_{\mathfrak m}(T)=0\). Thus
\(J_\Delta\) is the saturated boundary ideal. The duality proof gives
\[
 H_\Delta(d)+H_\Delta(a+b-5-d)\le\ell\Delta ,
 \qquad H_\Delta(d)=\dim T_d .
\]
It only uses this degree-one extension of the full CI algebra.
[Graded conductor sequence and canonical injection](quadratic_covers_and_conductor_descent.md#8-attachment-and-a-global-lower-bound-on-boundary-length).

If the separated graded algebra \(B_Y\) is also Cohen--Macaulay, the
same dual sequence gives \(\omega_T\simeq T(a+b-5)\): its only possible
cokernel is \(\operatorname{Ext}^3_S(B_Y,S(-4))(-1)\), which then vanishes.
Thus \(T\) is graded Gorenstein and an Artin reduction has symmetric
\(h\)-vector, final entry one, and socle degree \(a+b-4\). This extra
ACM hypothesis is not automatic for a separated branch. The
[conductor-regularity literature](../../literature/README.md#eisenbud--ulrich-conductor-regularity)
uses related duality under different reducedness and CM hypotheses.

If \(F\) is integral and \(R\) is nonsquare in \(k(F)\) after
trivializing by a linear form squared, then
\[
               (J_\Delta)_d=(F)_d \quad(2d+2<b).                    \tag{2}
\]
Indeed \(h\in(J_\Delta)_d\) gives \(Zh=P\in(A_Y)_{d+1}\).
The norm \(P^2-Rh^2\), using polynomial representatives, belongs to
\((F,G)\). In this degree it belongs to \((F)\). If \(F\nmid h\),
division on the integral surface makes \(R\) a square there. The
reverse containment follows from \(F=0\) on \(Y\). The
[nonsplit onset](endpoint_lattice_capacity.md#nonsplit-lower-onset-in-the-same-conductor-quotient)
and the [choice of cover preserving the two marked endpoints](quadratic_cover_choice.md)
give this constraint on the original pencil. Moving \(w\) also moves
the scheme on which the necessary postulation is imposed.

## Four general points and the maximum length

Let \(H_i=\dim_{k(C_0)} J_\eta^i/J_\eta^{i+1}\), where \(J_\eta\)
is the maximal ideal of the generic transverse algebra. Put
\(\Lambda=H^\vee\), \(S(\Lambda)=\sum_j\binom{\Lambda_j}{2}\),
and \(L=\Lambda_1\), the nilpotence index. The Hilbert function of a
plane Artin algebra is unimodal: in a binary monomial initial ideal,
as soon as a degree has missing standard monomials, their multiples
exclude at least one more monomial in the next degree. For any \(w,R\)
as above, completing at each root and applying the
[local length bound](quadratic_conductor_lattices.md#length-equality-and-the-restriction-to-the-reduced-branch)
gives \(\ell\Delta\le4S(\Lambda)\). Indeed the generic Jordan type of
each \(R-w^2\), in a local retraction to the smooth curve, is dominated
by \(\Lambda\) by the filtration argument. Its generic Hilbert function
is \(H\), since the two affine curve parameters \(B/A,C/D\) give
coefficient fields on their charts. The multiplicities of the roots
sum to four. Equality requires and suffices that at each root the
closed transverse Jordan partition of \(R-w^2\) be \(\Lambda\).

For general \(w,R\) the bound is attained, with
\(\Delta\cap C_0=(L-1)\operatorname{div}(w)\) as schemes on \(C_0\).
Here is why the actual quadric pencil reaches general transverse
directions at all four roots. On \(A=1\) put \(x=B,\ y=C-x^3,\
q=D-xC\). The algebra on this chart is finite free over \(k[x]\),
by the nilpotent filtration and purity. Shrink the line so all
successive layers are free and the ordinary transverse Hilbert function
is \(H\). Write \(w(x)^2=\sum b_jx^j\). On \(q=0\) its quadratic
lift is \(\sum_{0\le i,j\le2}b_{i+3j}x^i C^j\). The coefficient
of \(y\) at a root \(\xi\) is
\[
       B_w(\xi)=\sum_{0\le i\le2,\ 1\le j\le2}
                        j\,b_{i+3j}\xi^{i+3j-3}.
\]
On the irreducible incidence \(w(\xi)=0\) with the \(x^2\) coefficient
normalized to one, this is generically nonzero: \(w=x^2-\xi^2\)
gives \(B_w(\xi)=\xi\). The four-simple-root incidence is finite
over the open of quartics with four finite simple zeros. Hence a
general \(w\) has four good roots and \(B_w\ne0\) at each. Varying
\(\lambda\) varies the other coefficient through all scalars. The
graded transverse algebra is a quotient in at most two variables,
so a general linear form is strong Lefschetz in characteristic zero.
The powers of any lift have at least the ranks of the graded symbol,
and the Hilbert-function dominance bound forces equality. One
\(\lambda\) works at all four points. The local equality and reduced
trace now give the assertions. [Iarrobino, Macias Marques and McDaniel,
Theorem 2.5, Proposition 2.10 and Lemma 2.15](https://arxiv.org/pdf/1802.07383).

For any such fixed \(w\), general \(\lambda\) also gives nonsplitting
on any finite list of integral surfaces of degrees \(d>2\).
In fact at most \(1+\lfloor\log_2(2d)\rfloor\) finite parameters split
on one surface. Take a general integral plane section. A nonzero
member of the pencil cannot vanish on this section unless it contains
the plane, by degree. Only finitely many members contain planes since
the pencil contains the smooth quadric \(Q\). Thus \(f=-R_0/Q\) gives
a nonconstant map of degree \(N\le2d\) on the normalized section.
At its generic point each square specializes from a unit in the
surface DVR after trivialization. For \(m\ge1\) split values,
the \(m-1\) ratios \((f-\lambda_i)/(f-\lambda_1)\), \(i=2,\ldots,m\),
are squares in the section field. Their square classes in \(k(f)\)
are independent by valuation at the \(\lambda_i\). The resulting
multiquadratic degree \(2^{m-1}\) divides \(N\).

## A general osculating cone is nonsplit on any prescribed carrier

For \(p\in k^\times\) choose \(w=(t-ps)^4\). The \(s^2t^2\)
coefficient \(6p^2\) makes this a missing linear section. There is
a unique lift of \(w^2\) singular at \(C_0(p)\):
\[
\begin{split}
R_p={}&A^2p^8-8ABp^7+28B^2p^6-56ACp^5+(62AD+8BC)p^4\\
     &\hspace{13mm}-56BDp^3+28C^2p^2-8CDp+D^2 .
\end{split}                                                         \tag{3}
\]
Substitution gives \((t-ps)^8\), and all partial derivatives vanish at
\([1:p:p^3:p^4]\). Uniqueness follows from smoothness of \(Q\) there.
At \(p=1\), in the independent forms \(U=A+D-B-C,\ V'=A-D,\ W=B-C\),
the expression is \(16U^2-15{V'}^2+24V'W+12W^2\). This has rank
three, and diagonal rescaling gives the same rank for all \(p\ne0\).

Fix an integral surface \(F\). The coordinate planes \(A=0,D=0\)
miss the vertex and cut smooth conics for every \(p\ne0\), so the
restriction has an odd divisorial valuation there. On any other \(F\)
we may use \(AD\ne0\) at its generic point and trivialize by \(A^2\).
If all roots in \(p\) of
(3) had even multiplicities, the square root with leading coefficient
\(A\) would have coefficients, in descending powers,
\[
 A,\quad -4B,\quad 6B^2/A,\quad -28C+24B^3/A^2,\quad \pm D.
\]
Comparison with \(-8CDp\) forces \(B^3=A^2C\) or \(3B^3=4A^2C\).
The \(p^4\) coefficient then forces respectively \(AD=BC\) or
\(8AD=BC\). In each case the quadric is irreducible and does not divide
the cubic, so these identities cannot hold on any surface. At least
one factor over \(k(F)\) has odd multiplicity. A constant root
\(p_0\in k^\times\) forces \(F=V(R_{p_0})\), and the distinct vertices
allow at most one such root. Since the polynomial has degree eight
and nonzero constant term, a lone odd constant factor would leave odd
total degree for the other factors. There is therefore an odd factor
whose roots vary on \(F\). After shrinking the smooth locus of
\(F\), all distinct monic factors give disjoint finite étale divisors
over it by their discriminants and resultants. The chosen factor dominates
the \(p\)-line because its root varies on \(F\).
In characteristic zero it has a dense smooth locus over that line.
Its image contains an open set, so for general \(p\) the divisor on
\(F\) has a component of the original odd multiplicity. Thus \(R_p\)
is nonsquare in \(k(F)\). The same \(p\) works for finitely many
preassigned carriers and may avoid any finite subset of \(C_0\).

At such a point put \(u=x-p\). In the actual completed algebra
\(O=k[[u]]\to A_p\) the boundary is supported only there,
\(w=u^4\), and \(v=R_p-u^8\in uJ+J^2\). Indeed \(v\) vanishes
on the reduced curve and its two normal derivatives vanish at \(u=0\)
by (3). The powers of \(J\) have free graded pieces at a general \(p\).
The [quadratic singularity estimate](quadratic_conductor_lattices.md#extra-vanishing-at-a-quadratic-singularity)
therefore applies to exactly the boundary in (2).

## The homogeneous jet test

Let \(m_0=\max(0,8(L-1)-4)\). With \(N\) multiplication by \(v\),
apply the following \(k\)-linear map to **actual degree-\(d\) forms**
dehomogenized in \(A_p\):
\[
 {\cal P}_d(h)=
 \left(\sum_{j=0}^{L-1}\binom{1/2}{j}
            u^{m_0+4-8j}N^j\right)h
               \pmod{u^{m_0}A_p}.                                   \tag{4}
\]
Here \(J^L=0\) by generic vanishing and torsion-freeness. The sum
is \(u^{m_0}z\). Its kernel consists precisely of forms with \(zh\)
regular at \(p\). At every other point \(w\) is a unit in a local
frame, and saturation of \(J_\Delta\) gives
\(\ker{\cal P}_d=(J_\Delta)_d\) in every degree. Thus the rank is
the *embedded* Hilbert function \(H_\Delta(d)\). Equation (2)
requires injectivity modulo the multiples of \(F\) for \(2d+2<b\).
In complementary degrees the sum of the two ranks is bounded by
the length of the same local quotient. One can run (4) over \(k(p)\)
for a moving point. The homogeneous columns must then be allowed
coefficients in \(k(p)\); specialization preserves their generic rank
on an open set at each fixed degree.

The quartic's torus action gives another way to evaluate the same map.
For \(\rho_p[A:B:C:D]=[A:pB:p^3C:p^4D]\), (3) gives
\(R_p\circ\rho_p=p^8R_1\) and the chosen root value scales by \(p^4\).
Thus the test at \(p\) on \(Y\) is the test at \(1\) on
\(\rho_p^{-1}Y\), transporting the ambient degree-\(d\) columns too.
This compares the embedded orbit over the open torus. At \(p=0\)
the quadric (3) specializes to \(D^2\) and the chosen root is the
ambient linear form \(D\) itself. Substitution in this equation
does not compute a flat limit of the conductor or of the orbit ideal.
The flat graph calculation below identifies precisely what is lost.

The [exact jet calculation](../../computations/moving_quadratic_conductor.py)
implements (4). Its control is the actual divisor \(2C_0\) on \(Q\).
On the chart it has \(q=0,\ y^2=0\), so \(v=B_w(x)y\). Formula (3)
gives \(B_w(p)=0,\ B_w'(p)=72p^4\). Hence the conductor on this
ribbon has quotient \(k(p)[[u]]/(u^3)\) and its unique linear equation
is the osculating plane with trace \((x-p)^3(x+p)\). This checks an
ambient kernel over the moving parameter. The ribbon is a control
for the calculation. The CI postulation hypotheses apply to the
entire hypothetical intersection.

Replay from the repository root with
~~~sh
python3 research/computations/moving_quadratic_conductor.py
~~~

## The flat graph at the endpoint

Fix any pure thickening \(Y\) of \(C_0\), not necessarily a CI, and let
\(R=k[[\pi]]\). On \(Y_R\) remove the section \(\Gamma:t=\pi s\).
There \(w_\pi=(t-\pi s)^4\) is invertible and the chosen root of
\(R_\pi\) lifts uniquely through the nilpotent ideal. Let \(B\) be
the image of the finite quadratic algebra in this root graph, using
degree-one frames; locally it is generated by \(1,z\) over
\(A=\mathcal O_{Y_R}\). It is \(R\)-flat, being a torsion-free
submodule of the sheaf on the complement. The map \(A\to B\) is
injective: restriction across \(\Gamma\) loses no section of a pure
curve, and \(Y_R\) is flat.

The quotient \(Q_B=B/A\) is supported on an infinitesimal neighborhood
of \(\Gamma\), hence finite over \(R\). Reduction modulo \(\pi\)
injects \(Q_B[\pi]\) into \(A_0\). Its image is punctual, so purity
of \(Y\) forces it to vanish. Thus \(Q_B\) is finite free and
\(A_0\hookrightarrow B_0\). On the complement of the endpoint the
special root is the ambient form \(D\), since \(R_0=D^2\).
Consequently the pure quotient of \(B_0\) is exactly \(A_0\): the
map to that quotient is the identity on \(A_0\), and its kernel
\(T_B\) is punctual. In particular \(B_0=A_0\oplus T_B\) as
\(A_0\)-modules and
\[
             \ell T_B=\dim_k(Q_B/\pi Q_B)=\delta_{\rm generic}.
\]
This retains the full conductor quotient, not just its length. Locally
put \(e=z-D\). Then \(T_B=A_0e\) and \(e^2=-2De\). The
family conductor sequence \(0\to\mathfrak c\to A\to Q_B\to0\),
with its degree-one twist suppressed, base-changes exactly because
\(Q_B\) is \(R\)-free. Hence
\(\operatorname{Ann}_{A_0}(e)=\mathfrak c_0\) and
\(T_B\simeq(A_0/\mathfrak c_0)(-1)\) in graded notation.
Here \(\mathfrak c_0\) is the specialized **family** conductor;
the conductor of the pure identity extension \(A_0=A_0\) is the
unit ideal. These are different specializations.
In the [simultaneous-graph correction identity](toric_limit_conductor_comparison.md#simultaneous-graph-and-the-exact-correction)
\(\delta_{\rm pure}=\delta_{\rm generic}+\alpha-\beta\), this
family therefore has \(\alpha=\delta_{\rm pure}=0\) and
\(\beta=\delta_{\rm generic}\). The whole generic conductor becomes
embedded punctual torsion. This is a flat finite-graph calculation on
a fixed pure source; it neither computes the orbit limit of its ideal
nor supplies a universal bound on the correction for other families.
