# What the two hyperosculating planes and the quadric retain

Date: 2026-10-30. Status: **independently reviewed provisional deductions**,
with the [state-specific audit and trace supplement](2026-10-30-fixed-surface-configuration-audit.md).
Sections 1–6 and 7–8 received separate independent hand reconstruction;
neither review required a material correction.
Investigator: `fixed_surface_configuration` subagent. No canonical promotion
or unrestricted STCI conclusion is proposed.

## 1. Exact configuration and inherited constraints

Work over an algebraically closed field of characteristic zero, with
\[
C=[s^4:s^3t:st^3:t^4],\quad q=x_0x_3-x_1x_2,\quad Q=V(q),
\]
\[
p_0=[1:0:0:0],\qquad p_\infty=[0:0:0:1].
\]
To avoid the differing endpoint subscripts in discussions, write
\(H^{(0)}=V(x_0)\), \(H^{(3)}=V(x_3)\), and
\[
D=Q\cup H^{(0)}\cup H^{(3)}=V(P),\qquad P=qx_0x_3.
\]
These planes are tangent to \(Q\) at \(p_\infty,p_0\), respectively.
Each cuts \(Q\) in two ruling lines. At \(p_\infty\), the lines
\(V(x_0,x_1)\) and \(V(x_0,x_2)\) meet \(C\) in lengths three and one;
the analogous lines at \(p_0\) do the same. Their product gives the
length-four hyperplane section. Thus the planes are actual fixed surfaces
whose restrictions constrain both defining equations, not merely a choice
of affine charts.

The [special-lines-and-planes note](2026-10-24-special-lines-planes-research-note.md),
sections 7–9, already proves the following facts for a hypothetical
\((a,b)\) STCI of generic thickness \(m\): each endpoint plane section is
a proper plane CI of length \(ab=4m\) supported at its endpoint; the
quadric residual-divisor intersections must be concentrated on \(C\).
It explicitly distinguishes these lengths from the complete schemes and
from line-section lengths. The [fixed-quadric note](2026-10-30-stci-game-quadric-boundary.md),
section 4, retains the actual orders on \(Q\) and residual-divisor classes.
Neither source supplies an unrestricted exclusion.

The literature also uses the hyperosculating planes in the quartic-pair
problem: [Craighero–Gattazzo (1986)](https://www.numdam.org/item/RSMUP_1986__76__177_0.pdf)
has that restricted degree scope. The facts about finite modules,
characteristic polynomials and nilpotence used below are standard, rather
than claimed as new general theorems; see
[Stacks, Cayley–Hamilton](https://stacks.math.columbia.edu/tag/00DX) and
[determinants of finite-length modules](https://stacks.math.columbia.edu/tag/0GSY).
The contribution here is an explicit barrier for the **full simultaneous
fixed-surface scheme data**, together with its all-pairs geometric meaning.

## 2. A control: residual curves can meet all three fixed surfaces only on C

Put
\[
c_0=x_1^3-x_0^2x_2,\qquad c_2=x_2^3-x_1x_3^2.
\]
The cubic complete intersection has precisely the reduced support
\[
V(c_0,c_2)=C\cup C^-\cup L,
\tag{1}
\]
where
\[
C^-=[s^4:s^3t:st^3:-t^4],\qquad L=V(x_1,x_2).
\]
In fact (1) is a reduced scheme. On \(x_0=1\), eliminating \(x_2\)
gives
\[
x_2=x_1^3,\qquad x_1(x_1^4-x_3)(x_1^4+x_3)=0.
\]
The factors are distinct, the affine scheme is reduced, and its components
are the indicated line and quartics. On \(x_0=0\), the equations leave
only \(p_\infty\), already in their closures. The complete intersection
is Cohen–Macaulay and has no embedded components; its generic reducedness
therefore proves reducedness globally.

On the Segre quadric, use
\[
x_0=AU,\quad x_1=AV,\quad x_2=BU,\quad x_3=BV,
\quad h=AV^3-BU^3.
\]
Then
\[
c_0|_Q=A^2h,\qquad c_2|_Q=-B^2h.
\tag{2}
\]
Since \(A,B\) have no common zero, the **whole common scheme on Q is C**.
On \(H^{(0)}\) the pair is
\((x_1^3,x_2^3-x_1x_3^2)\), with its sole common point \(p_\infty\)
and total length nine. On \(H^{(3)}\) the analogous scheme has length
nine at \(p_0\).

Nevertheless \(q|_{C^-}=-2s^4t^4\), while \(q|_L=x_0x_3\).
Both residual components meet \(Q\) only at the marked endpoints, and
their intersections with each endpoint plane are concentrated there too.
This does not mistake a vertical exceptional cycle for a curve: \(C^-\)
and \(L\) are actual projective residual components of degrees four and one.
The cubic example fails \(4\mid ab\), so it is a control, not a surviving
degree row. A related endpoint-only residual phenomenon is already
recorded for binomial quartic carriers in the branch source
`restructure/mathematical-consolidation:research/synthesis/01-problem-and-curve.md`,
sections 1.2C–E. No novelty claim is made for that broad phenomenon.

## 3. Full fixed-D restrictions do not determine generic thickness

**Proposition.** For every integer \(r\ge2\), consider the degree-\((3r,3r)\)
pairs
\[
\begin{aligned}
J_r&=(c_0^r,c_2^r),\\
J'_r&=(c_0^r,c_2^r+q x_0^{3r-3}x_3).
\end{aligned}
\tag{3}
\]
Both are proper complete intersections containing \(C\). Their actual
equations have identical restrictions on the entire scheme \(D\), so in
particular their intersection schemes with \(D\) are identical, including
all overlaps between its three components. The common quadric scheme is
the Cartier multiple \(rC\subset Q\), and the two endpoint plane schemes
are identical of length \(9r^2\). But their generic thicknesses along \(C\)
are respectively
\[
m(J_r)=r^2,\qquad m(J'_r)=r.
\tag{4}
\]

**Proof.** The difference of the second equations is
\(P x_0^{3r-4}\), so it vanishes on the whole union \(D\), not only on
its components separately. Formula (2) shows that on \(Q\) the ideal
sheaf is \((h^r)\). The restrictions to the two planes are the \(r\)-th
powers of the displayed cubic pair, with no common curve, so Bézout gives
length \(9r^2\) at the sole common point.

The polynomial \(c_0\) is irreducible: viewed as a primitive polynomial
in \(x_2\) over \(k[x_0,x_1,x_3]\), it is irreducible over that ring's
fraction field. Neither mate in (3) is divisible by \(c_0\). For the
second mate this can already be seen at \([1:0:0:1]\), where \(c_0=c_2=0\)
but \(q x_0^{3r-3}x_3=1\). Thus both pairs are proper.

At the generic point of \(C\), \(h=c_0\) and \(q\) are regular parameters.
The exact identity
\[
x_0^2c_2=-x_2^2c_0-(2x_1^2x_2+x_1q)q
\tag{5}
\]
writes \(c_2=\alpha h+\beta q\), with \(\alpha,\beta\) units there.
Consequently \(c_0,c_2\) are also regular parameters, and \(J_r\) has
length \(r^2\). For \(J'_r\), write the added term \(uq\), where
\(u=x_0^{3r-3}x_3\) is a unit. Modulo \(h^r\), the expression
\((\alpha h+\beta q)^r\) is \(q\) times an element of the maximal ideal
because \(r\ge2\). Hence
\[
(h^r,c_2^r+uq)=(h^r,q)
\]
in that local ring, and its length is \(r\). This proves (4).

For even \(r\), the necessary divisibility \(4\mid9r^2\) holds. The
residual degrees of these two proper intersections are nevertheless
\(5r^2\) and \(9r^2-4r\), respectively. Neither example is an STCI.
The conclusion is carefully limited: the fixed-surface data in (3)
cannot recover generic thickness. It does **not** prove that no stronger
argument using some fixed-D restrictions can obstruct all their lifts,
or that the specific fixed data in (3) admit an STCI lift.

**Geometric meaning.** This ambiguity persists after retaining the entire
schemes on all three surfaces and their gluing, rather than just their
reduced supports or endpoint lengths. The allowed correction changes a
normal derivative to \(Q\) away from the endpoints. In the first pair,
two independent transverse parameters are both raised to power \(r\);
in the second, a transverse parameter is killed to first order. The
quadric restriction sees the same \(r\)-fold divisor in both cases.

## 4. The plane pencil converts every admissible pair into one finite cover

Let \(Y=V(F_a,G_b)\) be any proper homogeneous CI containing \(C\), and
assume its intersections with \(H^{(0)},H^{(3)}\) are supported only at
\(p_\infty,p_0\), respectively. No hypothesis on generic thickness is
made. Set \(n=ab\) and \(M=V(x_0,x_3)\).

**Proposition.** Projection from \(M\) restricts to a finite flat morphism
\[
\pi:Y\longrightarrow\mathbf P^1,\qquad [x]\longmapsto[x_0:x_3],
\tag{6}
\]
of degree \(n\). Its restriction to \(C\) is the degree-four cover
\([s:t]\mapsto[s^4:t^4]\), totally ramified over the two marked fibers.
As an \(\mathcal O_{\mathbf P^1}\)-module, its algebra has the noncanonical
splitting
\[
E=\pi_*\mathcal O_Y
\simeq\bigoplus_{i=0}^{a-1}\bigoplus_{j=0}^{b-1}
\mathcal O_{\mathbf P^1}(-i-j).
\tag{7}
\]

**Proof.** The endpoint assumptions imply \(Y\cap M=\varnothing\).
A positive-dimensional fiber of the projection would be a projective
curve in a plane of the pencil disjoint from its line \(M\), impossible
by Bézout. The proper morphism (6) is therefore finite. Every local base
parameter is a nonzerodivisor on the pure Cohen–Macaulay curve \(Y\),
since no component lies in a fiber. Thus the finite module is torsion-free
over the smooth base curve, hence locally free. Each fiber is a proper
hyperplane section, of length \(ab\).

For (7), let \(R=k[x_0,x_1,x_2,x_3]/(F,G)\) and
\(B=k[x_0,x_3]\). The empty intersection with \(M\) makes \(R\) finite
over \(B\); \(x_0,x_3\) are a regular sequence in the dimension-two
Cohen–Macaulay graded ring \(R\). The quotient
\[
R/(x_0,x_3)=k[x_1,x_2]/(F|_M,G|_M)
\]
is an Artinian CI, with Hilbert series
\((1+z+\cdots+z^{a-1})(1+z+\cdots+z^{b-1})\).
Lift a homogeneous basis to \(R\). Graded Nakayama gives a surjection
from the corresponding sum of shifted free \(B\)-modules; the regular
sequence and Hilbert series show that its kernel has zero Hilbert
series, hence is zero. Sheafification gives (7).

The module splitting is not an algebra splitting. Its multiplication,
and the two maps given by multiplication by \(x_1,x_2\), retain the
actual arbitrary defining pair. Replacing them by freely chosen matrices
would discard the ambient realization problem.

## 5. The quadric section is a cokernel; sole support requires nilpotence

Because \(\mathcal O_Y(1)=\pi^*\mathcal O_{\mathbf P^1}(1)\), multiplication
by \(q\) gives a twisted endomorphism
\[
N:E\longrightarrow E(2).
\]
Its characteristic polynomial has coefficient sections
\[
\chi_N(T)=T^n+\gamma_1T^{n-1}+\cdots+\gamma_n,
\qquad \gamma_j\in H^0(\mathbf P^1,\mathcal O(2j)).
\tag{8}
\]
This means the usual characteristic polynomial in any local trivialization
of \(\mathcal O(2)\); the displayed coefficients glue with those twists.
There is a canonical right-exact sequence
\[
E(-2)\xrightarrow{q}E\longrightarrow
\pi_*\mathcal O_{Y\cap Q}\longrightarrow0.
\tag{9}
\]
Thus the full quadric intersection is its cokernel, and the two full
plane-section algebras are the two marked fibers of \(E\), with their
induced multiplication operators.

**Universal criterion.** In addition to the hypotheses of section 4,
assume \((Y\cap Q)_{\rm red}=C\). Then the following are equivalent:

1. \(Y_{\rm red}=C\).
2. \(N\) is nilpotent, meaning an iterated twisted power is zero.
3. Every coefficient \(\gamma_j\) in (8) is identically zero.
4. \(\operatorname{tr}(N^j)=0\) in
   \(H^0(\mathbf P^1,\mathcal O(2j))\) for \(1\le j\le n\).

**Proof.** Sole support makes the section \(q\) nilpotent on \(Y\).
Conversely nilpotence puts \(Y_{\rm red}\) inside \(Q\), and the specified
quadric intersection then gives \(Y_{\rm red}=C\). Over the function
field of the reduced integral base, nilpotence is equivalent to
\(\chi_N=T^n\); coefficients vanishing generically vanish identically.
The reverse implication also follows globally from Cayley–Hamilton,
which gives the bound \(N^n=0\). Newton identities give equivalence with
the trace conditions in characteristic zero.

The plane tests force each \(\gamma_j\) to vanish at both marked base
points: \(q\) acts nilpotently on each zero-dimensional endpoint fiber.
That is not identical vanishing of a section of \(\mathcal O(2j)\).
For the pair \(J_r\), on \(x_0=1\) put \(\lambda=x_3\). Its actual
characteristic polynomial is
\[
\chi_N(T)=T^{4r^2}(T-2\lambda)^{4r^2}(T-\lambda)^{r^2}.
\tag{10}
\]
Indeed (1) and its generic thickness \(r^2\) give four sheets from
\(C\), four from \(C^-\), and one from \(L\), with reduced \(q\)-values
\(0,2\lambda,\lambda\). Nilpotents on these sheets do not change their
characteristic roots, but do retain their multiplicities. In particular
\(\operatorname{tr}(N)=9r^2x_0x_3\) globally. It vanishes on both
endpoint fibers while being nonzero.

At the generic point of \(C\), multiplication by \(q\) on the transverse
Artinian algebra is nilpotent for any containing pair. Its cokernel
dimension is the generic multiplicity of \(Y\cap Q\) along \(C\): the
number of Jordan blocks. Its full algebra length \(m\) is the sum of
their sizes. Formula (3) has the same cokernel dimension \(r\), but sums
\(r^2\) and \(r\). This identifies exactly the thickness information
that the restriction to \(Q\) omits.

## 6. Consequence for the unrestricted question and review boundary

All hypothetical STCI pairs satisfy section 4 and the quadric-support
hypothesis of section 5, so this is an interface for the **full question**.
It packages the two planes as marked fibers of an actual finite cover and
the quadric as an actual multiplication operator on that cover. A
hypothetical supported pair must turn all \(ab\) sheets into thickness on
the cyclic four-sheeted cover \(C\to\mathbf P^1\), hence \(m=ab/4\).

The criterion is a standard nilpotence test specialized to this geometry,
not a new nonexistence theorem. Neither (7), (9), nor the endpoint fiber
schemes have been shown to prevent the required nilpotent algebra
structure. Conversely no such algebra with two actual homogeneous
defining equations has been constructed. The useful new barrier is
precise: even identical equations on the whole fixed union \(D\) can
hide different transverse lengths; a proposed compatibility obstruction
must control this missing normal action or an equivalent invariant.

The displayed identities, generic lengths and characteristic polynomial
are proved directly above. Sections 1–6 passed the
[independent hand audit](2026-10-30-fixed-surface-configuration-audit.md)
without a material correction; its recorded source state precedes the
trace additions below. No inherited certificate was rerun, no computer
algebra experiment was performed, and no canonical result was promoted.
The full question remains open.

## 7. The first trace depends only on two lower fiber-degree layers

This section answers a further all-pairs question raised by (8). The two
endpoint conditions force
\[
\operatorname{tr}(q)=c x_0x_3.
\tag{11}
\]
Could characteristic zero and the common quadric support force \(c\ne0\)?
Section 8 gives an explicit negative answer. First, the coefficient has
an exact description valid for arbitrary pairs satisfying section 4.

Write \(u=x_0,v=x_3,x=x_1,y=x_2\), and decompose by degree in \(x,y\):
\[
F=\sum_{i=0}^a f_i(u,v;x,y),\qquad
G=\sum_{i=0}^b g_i(u,v;x,y),
\]
where \(f_i\) has fiber degree \(a-i\) and base degree \(i\), and
\(g_i\) has fiber degree \(b-i\) and base degree \(i\). In particular
\(f_0,g_0\in k[x,y]\) have no common projective zero. Missing layers are
understood to be zero. Set
\[
F_\epsilon=f_0+\epsilon f_1+\epsilon^2 f_2+\cdots,
\qquad
G_\epsilon=g_0+\epsilon g_1+\epsilon^2 g_2+\cdots.
\]

**Degree-two trace formula.** The polynomial
\(T(u,v)=\operatorname{tr}(x_1x_2)\) is determined entirely by
\(f_0,f_1,f_2,g_0,g_1,g_2\). For fixed leading forms, it is linear in
the second lower layers and quadratic in the first lower layers, with
the two kinds of terms added. An exact coefficient prescription is
\[
T(u,v)=[\epsilon^2]\,
\operatorname{tr}_{\,k[u,v,\epsilon]/(\epsilon^3)[x,y]/
(f_0+\epsilon f_1+\epsilon^2f_2,\,
g_0+\epsilon g_1+\epsilon^2g_2)}(xy).
\tag{12}
\]
The trace in (12) is the trace of a finite free algebra of rank \(ab\)
over \(k[u,v,\epsilon]/(\epsilon^3)\). This prescription is independent
of its chosen basis. Under the two endpoint conditions,
\(T(u,v)=\tau uv\), and therefore
\[
c=ab-\tau=ab-T(1,1).
\tag{13}
\]

For an explicit scalar formula, put \(\{f,g\}=f_xg_y-f_yg_x\) and
\[
J_0=\{f_0,g_0\},\quad
J_1=\{f_1,g_0\}+\{f_0,g_1\},\quad
J_2=\{f_2,g_0\}+\{f_1,g_1\}+\{f_0,g_2\}.
\]
Then
\[
\begin{aligned}
T(u,v)=\operatorname{Res}_{0}\,xy\Bigg[&
\frac{J_2}{f_0g_0}
-\frac{J_1f_1+J_0f_2}{f_0^2g_0}
-\frac{J_1g_1+J_0g_2}{f_0g_0^2}\\
&+\frac{J_0f_1^2}{f_0^3g_0}
+\frac{J_0f_1g_1}{f_0^2g_0^2}
+\frac{J_0g_1^2}{f_0g_0^3}\Bigg],dx\wedge dy.
\end{aligned}
\tag{14}
\]
Each summand denotes the local Grothendieck residue for the indicated
ordered powers of \((f_0,g_0)\), whose common zero is the origin. Thus
(14) is a finite formula in the six specified layers, rather than a
condition on unspecified roots of the full equations.

**Proof.** The leading forms are a regular sequence with finite quotient.
The same homogeneous-basis lifting argument as in section 4 gives a
finite free deformation over \(k[u,v,\epsilon]\), with those leading
forms fixed. For \(\epsilon\ne0\), scaling \((x,y)\) by \(\epsilon\)
identifies its fibers with those of the original equations, because
\(F_\epsilon=F(\epsilon u,x,y,\epsilon v)\) and similarly for \(G\).
Multiplication by \(xy\) then has trace \(\epsilon^2T(u,v)\). Equality
extends to \(\epsilon=0\) by freeness, proving (12). It also proves
independence of every layer with index at least three.

The trace–residue identity gives
\[
\operatorname{tr}(xy)=
\operatorname{Res}\frac{xy\,\{F_\epsilon,G_\epsilon\}}
{F_\epsilon G_\epsilon}\,dx\wedge dy.
\]
Expand both denominators as geometric series around \((f_0,g_0)\) and
take the coefficient of \(\epsilon^2\). The numerator has coefficients
\(J_0,J_1,J_2\), giving exactly (14). This also exhibits linear
dependence on \(f_2,g_2\) and quadratic dependence on \(f_1,g_1\).
One may justify this expansion on fixed small residue cycles over
\(\mathbf C\); the resulting rational identity in the coefficients
holds over every characteristic-zero field. The leading-form resultant
is nonzero, so these residue expressions are defined throughout the
present setting.

The primary source for the trace–residue identity and the deformation to
leading forms is [Cattani–Dickenstein–Sturmfels, *Computing Multidimensional
Residues*](https://arxiv.org/pdf/alg-geom/9404011), sections 1 and 4,
especially equation (4.7). Formula (14) is its degree-two expansion here.
Euler–Jacobi vanishing for a low-degree **residue numerator** must not
be applied directly to a trace: the trace numerator contains the
Jacobian, as the displayed identity requires.

**Geometric meaning.** The first moment is sensitive to the top two
lower layers of the actual equations in the fibers of the plane pencil.
It does not inspect all their normal contact or all residual sheets.
Corrections invisible to these six layers are invisible to this first
moment, even if they substantially alter the intersection elsewhere.

## 8. All three boundary supports are compatible with zero first trace

**Counterexample.** Set
\[
F_\alpha=x_1^4-x_0^3x_3+\alpha q x_1x_2,
\qquad
G_\beta=x_2^4-x_0x_3^3+\beta q x_1x_2,
\tag{15}
\]
with \(\alpha\beta\ne1\). These are proper quartic pairs containing \(C\).
Their two endpoint plane sections have their entire length sixteen at
the respective endpoint, and their common quadric support is exactly
\(C\). Nevertheless
\[
\boxed{\operatorname{tr}(q)=
8\frac{\alpha\beta-2}{\alpha\beta-1}\,x_0x_3.}
\tag{16}
\]
In particular \(\alpha=1,\beta=2\) makes the trace identically zero.
This pair is not an STCI; its second trace is nonzero.

**Boundary and properness proof.** On either endpoint plane the two
equations become
\[
x_1^2(x_1^2-\alpha x_2^2),\qquad
x_2^2(x_2^2-\beta x_1^2).
\tag{17}
\]
They have no common root in \(\mathbf P^1_{[x_1:x_2]}\) when
\(\alpha\beta\ne1\). Their plane common scheme is therefore a proper
degree-\((4,4)\) CI at the designated point. In particular the pair
misses \(M\), which also proves properness: a common surface component
would necessarily meet the projective line \(M\).

On \(Q\), the corrections disappear. In the Segre coordinates of
section 2 their restrictions are
\[
F_\alpha|_Q=A^3Vh,\qquad G_\beta|_Q=-B^3Uh.
\]
The residual coefficients have common zeros only at \((A,U)=(0,0)\)
and \((B,V)=(0,0)\), namely the two endpoints, already on \(C\).
Thus the common quadric support is exactly \(C\). The actual common
scheme can have endpoint structure; no assertion that it is just the
reduced curve is needed or made.

**Trace proof retaining all sheet multiplicities.** Over
\(K=k(\lambda)\), where \(x_0=1\) and \(x_3=\lambda\), put
\(z=x_1x_2\). Then
\[
x_1^4=A(z):=\alpha z^2-\alpha\lambda z+\lambda,
\qquad
x_2^4=B(z):=\beta z^2-\beta\lambda z+\lambda^3.
\]
Consequently the algebra of the fiber is a rank-four extension of
\(K[z]/(p(z))\), where
\[
\begin{aligned}
p(z)={}&(1-\alpha\beta)z^4+2\alpha\beta\lambda z^3\\
&-(\alpha\beta\lambda^2+\alpha\lambda^3+\beta\lambda)z^2
+(\alpha\lambda^4+\beta\lambda^2)z-\lambda^4.
\end{aligned}
\tag{18}
\]
More precisely it is
\[
\bigl(K[z]/(p(z))\bigr)[x_1]/(x_1^4-A(z)),
\qquad x_2=z/x_1.
\]
The constant coefficient of \(p\) makes \(z\) a unit, and
\(A(z)B(z)=z^4\) makes \(A(z)\), hence \(x_1\), a unit. The two
descriptions are therefore isomorphic, including nilpotent structures.
Thus every characteristic root of multiplication by \(z\) in the
degree-four algebra is counted four times in the full rank-sixteen
algebra. Its trace is
\[
\operatorname{tr}(x_1x_2)
=4\left(-\frac{2\alpha\beta\lambda}{1-\alpha\beta}\right).
\]
Subtracting this from \(16\lambda\) gives (16).

For \(\alpha=1,\beta=2\), at \(\lambda=1\), the monic polynomial
for the four \(z\)-roots is
\[
z^4-4z^3+5z^2-3z+1.
\]
For \(q=1-z\), it becomes
\[
T^4-T^2+T.
\tag{19}
\]
The characteristic polynomial on the full fiber is the fourth power
of (19). Its first trace is zero, while its second trace is \(8\).
In particular \(q\) is not nilpotent and there are actual sheets away
from \(Q\), despite all three boundary-support conditions. The root
\(z=\lambda\) in (18) supplies \(C\); at these parameters it is
generically simple, since the derivative of the monic polynomial there
is \(\lambda^2(\lambda^2-4\lambda+2)\), not identically zero. Thus
the generic thickness on \(C\) is one and the residual degree is twelve.

**Meaning and stopping point.** The vanishing in (16) comes from
cancellation among residual \(q\)-values, rather than disappearance of
the residual sheets. No positivity principle for those values is
available over an algebraically closed characteristic-zero field. A
universal nonzero-first-trace argument is therefore ruled out under
exactly the proposed plane and quadric support hypotheses. The full
characteristic polynomial or an equivalent collection of higher moments
still detects the distinction. This counterexample is a test of a
proposed universal invariant, not an additional family exclusion or a
claim that the higher-moment equations are inconsistent for arbitrary
defining pairs. Sections 7–8 passed their own independent review in the
companion audit's supplement; their status remains provisional.
