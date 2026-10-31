# Fixed surfaces, endpoint equations, and the missing normal action

These are full proofs for the fixed quartic C0. The finite-cover and elementary two-chart arguments are characteristic-free; the residue controls and trace criteria have the precise characteristic assumptions below. They are independently reviewed provisional deductions, not promoted results. Independent source review reconstructed the finite-flat algebra, identical-full-restriction examples, trace-residue formula and zero-first-trace counterexample, followed by the two-chart/endpoint and determinant arguments. The elementary deductions require no finite search or inherited certificate rerun. The [global equation account](global_equations_and_constructions.md) supplies the elementary quartic geometry and affine-boundary theorem.

## Characteristic scope of the separate tests

The finite-flat projection/module-splitting proof, actual q-cokernel, and equivalence of sole support with nilpotence and vanishing characteristic coefficients use no characteristic-zero assumption and work over algebraically closed k in every characteristic, under their stated endpoint/quadric hypotheses. The reduced projection [s:t]↦[s⁴:t⁴] is separable in odd characteristic and characteristic zero, and purely inseparable of degree four in characteristic two. Degree ab counts the full finite-flat algebra, not a reduced separable cover.

The generic cover-trace identity proved below works in every characteristic. Its pairing has rank four exactly in characteristic zero or odd characteristic not dividing the transverse length m; it is zero if the characteristic divides m, and also in characteristic two because the reduced cover is inseparable. The corrected canonical-cover structure theorem has no characteristic restriction. Its Gorenstein and realization hypotheses remain necessary.

The equivalence with traces through rank n=ab needs the Newton divisions 1,...,n: it is valid when n! is invertible (in particular characteristic zero or p>n). Without that condition, trace vanishing cannot replace the characteristic polynomial: even the identity on a rank-p vector space has every positive power trace zero in characteristic p but is not nilpotent. The explicit cubic Cminus decomposition, its regular-parameter thickness calculations, the two-lower-layer residue derivation, and the zero-firsttrace quartic control below retain their checked characteristic-zero scope. In characteristic two Cminus=C and the crucial coefficient 2 in the generic cubic relation vanishes; the characteristic-zero cubic controls cannot simply be reused. The actual two-chart/endpoint/determinant arguments in the second part are characteristic-free, as their proofs show.

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

The special-lines-and-planes note,
sections 7–9, already proves the following facts for a hypothetical
\((a,b)\) STCI of generic thickness \(m\): each endpoint plane section is
a proper plane CI of length \(ab=4m\) supported at its endpoint; the
quadric residual-divisor intersections must be concentrated on \(C\).
It explicitly distinguishes these lengths from the complete schemes and
from line-section lengths. The fixed-quadric note,
the finite-cover proposition, retains the actual orders on \(Q\) and residual-divisor classes.
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

## Cover multiplication, trace and geometric realization

For this comparison assume \(Y_{\mathrm{red}}=C_0\) in §4 and write
\(ab=4m\), where \(m\) is the generic transverse length along \(C_0\).
The base is \(B=\mathbf P^1\), the reduced map is
\(f:[s:t]\mapsto[s^4:t^4]\), and \(L=O_Y(1)=\pi^*O_B(1)\).
These describe one finite algebra together with its polarization. They
retain more than the reduced cover or its marked fibers alone.

### What the trace retains of transverse nilpotents

Put \(K=k(B)\), \(A=(\pi_*O_Y)_K\), and \(K'=k(C_0)\).
Then \(A\) is an Artinian local \(K\)-algebra of dimension \(4m\),
with residue field \(K'\) of degree four. Filter \(A\) by powers of its
nilradical \(N\). Each quotient is a \(K'\)-vector space, and multiplication
by \(u\in A\) on it is multiplication by its residue \(\bar u\).
The sum of the quotient dimensions over \(K'\) is \(m\), so additivity
of matrix trace gives
\[
\operatorname{Tr}_{A/K}(u)
=m\operatorname{Tr}_{K'/K}(\bar u),
\qquad
\operatorname{Tr}_{A/K}(uv)
=m\operatorname{Tr}_{K'/K}(\bar u\bar v).
\tag{T}
\]
This argument is characteristic-free and does not choose an algebra
splitting. Since the finite locally free sheaves on \(B\) are torsion-free,
the generic identity gives the corresponding global trace identity
\(\operatorname{Tr}_{Y/B}=m\operatorname{Tr}_{C_0/B}\circ\mathrm{red}\).

In characteristic zero, or odd characteristic \(p\nmid m\), the field
extension \(K'/K\) is separable and its trace pairing is nondegenerate.
Thus (T) has rank four on the \(4m\)-dimensional algebra, and its radical
is exactly \(N\). If \(p\mid m\), the trace is zero. In characteristic
two the reduced extension is purely inseparable of degree four, so its
trace is also zero, regardless of \(m\). In all cases, for \(m>1\) the
ordinary trace discriminant is identically zero: its generic determinant
vanishes. It is therefore not an effective two-point branch divisor of
this nonreduced cover. Normalizing a scalar trace by \(m\), when allowed,
does not construct a multiplicative retraction to \(C_0\).

Only the reduced cover is étale off the two marked fibers in
characteristic different from two. The nilpotent-invariance results for
étale categories in [SGA 1, I.5.5 and I.8.3](https://arxiv.org/pdf/math/0206203)
and its tame specialization results in XIII.2.8–2.12 for smooth curves
with boundary do not construct the embedded transverse nilpotent algebra.
The full cover with \(m>1\) is generically nonreduced and is not étale
there. Likewise a nonzero Jacobian socle element under its
prime-to-characteristic hypothesis is not an étaleness statement. The
[actual different and characteristic bounds](contact_jacobians_and_hamiltonian_actions.md#the-six-ambient-minors-different-and-contact-identity)
retain that additional structure.

There is a concrete global interpretation of the omitted linear section.
A retraction \(r:Y\to C_0\) over \(B\) would preserve \(L\) compatibly with
restriction, and split the map from \(H^0(Y,L)\), of dimension four, onto
\(H^0(C_0,L|_{C_0})\), of dimension five. The complete
[polarized retraction proof](contact_jacobians_and_hamiltonian_actions.md#a-pencil-compatible-polarized-retraction-cannot-extend-globally)
also gives the general linear-normality criterion. Its section argument
works in every characteristic; only in characteristic different from
two does formal étaleness give the unique punctured \(B\)-retraction.
This expresses the missing section \(s^2t^2\), with no identification of
a particular obstructing endpoint or exclusion of arbitrary unpolarized
retractions. It is compatible with the positive-characteristic supported
pairs.

### A canonical cover embedding and the separate ambient embedding

An actual CI pencil satisfies the hypotheses of the corrected
[Casnati–Ekedahl structure theorem, Landesman–Vakil–Wood, Theorem 3.2 and Remark 3.3](https://arxiv.org/pdf/2203.01840).
The theorem applies to finite locally free Gorenstein covers of degree at
least three over arbitrary schemes, with no reducedness or characteristic
restriction. It gives a relative canonical embedding into
\(\mathbf P((\pi_*O_Y/O_B)^\vee)\) and its self-dual resolution, with
nondegenerate arithmetically Gorenstein fibers. Here each fiber is a
zero-dimensional complete intersection in its plane and hence
Gorenstein. Adjunction gives
\[
\omega_Y\simeq O_Y(a+b-4),\qquad
\omega_{Y/B}\simeq O_Y(a+b-2)=L^{a+b-2}.
\tag{C}
\]
The theorem applies to this actual, generally nonreduced cover. It does
not construct its multiplication starting from the module (7), or
identify its canonical projective bundle with the original \(\mathbf P^3\).

For a constructive converse, let an abstract finite cover \(\rho:T\to B\)
have the displayed module splitting (7), with \(a,b\ge2\), and put
\(L_T=\rho^*O_B(1)\). Projection formula already gives
\[
\begin{aligned}
H^0(T,L_T)
&=\bigoplus_{i=0}^{a-1}\bigoplus_{j=0}^{b-1}
H^0(B,O_B(1-i-j)),\\
h^0(T,L_T)&=2+1+1=4.
\end{aligned}
\]
Pullback of the base pencil generates \(L_T\), so these four sections
supply an actual morphism \(\Phi_{|L_T|}:T\to\mathbf P^3\).
Four sections and basepoint freeness are therefore already available.
Realizing the specified embedded multiple curve requires further data:

- The reduced scheme must be \(C_0\), with reduced map \(f\), and restriction
  of the four sections must have image precisely
  \(\langle s^4,s^3t,st^3,t^4\rangle\subset H^0(\mathbf P^1,O(4))\),
  after choosing the desired ambient coordinates.
- The morphism must be a closed immersion, including separation of the
  transverse nilpotent directions, with a complete-intersection image.
- For the canonical-cover route, \(\rho\) must itself be Gorenstein and
  its algebra-linear canonical duality must give the prescribed power
  of \(L_T\).

The last condition is stronger than the visible symmetry of the split
module. Indeed, reindexing \((i,j)\) by \((a-1-i,b-1-j)\) gives an
\(O_B\)-module isomorphism
\[
(\rho_*O_T)^\vee\simeq(\rho_*O_T)(a+b-2).
\]
For a finite cover, however, \(\rho_*\omega_{T/B}\) is
\(\operatorname{Hom}_{O_B}(\rho_*O_T,O_B)\) with its natural
\(\rho_*O_T\)-module action. An isomorphism yielding (C) must respect
that action. An arbitrary symmetry of the underlying split bundle
supplies no such perfect multiplication pairing. Gorensteinness itself
only makes \(\omega_{T/B}\) invertible; it does not specify its isomorphism
with \(L_T^{a+b-2}\).

These are geometric realization conditions on a useful construction of
multiple structures. They identify what a proposed cover produces and
what must be supplied to recover the prescribed intersection in
\(\mathbf P^3\); they do not presume that realization fails. For the
separate arithmetic implications and compatible lifts, use the
[full equation incidence and arithmetic degree bounds](../supplements/ARITHMETIC_EQUATIONS_AND_JET_GAPS.md#the-full-simultaneous-equation-incidence).
The cover statements prove no all-pair divisibility condition or
mixed-characteristic supported lift. Their source applications retain
scoped independent review. Independent integration review reconstructed the
trace and realization arguments and accepted their precise characteristic,
section-generation and algebra-duality boundaries. No new cover is constructed
by that review.

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

**Universal criterion.** In addition to the hypotheses of the finite-cover proposition,
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

## 7. The first trace depends only on two lower fiber-degree layers

This section answers a further all-pairs question raised by (8). The two
endpoint conditions force
\[
\operatorname{tr}(q)=c x_0x_3.
\tag{11}
\]
Could characteristic zero and the common quadric support force \(c\ne0\)?
Section 8 gives an explicit negative answer. First, the coefficient has
an exact description valid for arbitrary pairs satisfying the finite-cover proposition.

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
The same homogeneous-basis lifting argument as in the finite-cover proposition gives a
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
defining pairs.

## Actual affine equations and the single-endpoint test

## 1. Once actual split sections glue, the missing line is not an extra obstruction

**Two-chart criterion.** Fix positive integers \(a,b\). The curve \(C\) is the reduced intersection of degree-\((a,b)\) homogeneous equations if and only if there are polynomial pairs

\[
(f_0,g_0)\quad\hbox{on }U_0,\qquad
(f_\infty,g_\infty)\quad\hbox{on }U_\infty
\]

whose zero sets are respectively \(C\cap U_0\) and \(C\cap U_\infty\), and which obey the **actual section identities** on the entire overlap

\[
f_0=(x_3/x_0)^a f_\infty,\qquad
g_0=(x_3/x_0)^b g_\infty.                 \tag{1}
\]

The right sides use the usual change of affine coordinates. No restriction is placed on the generic thickness of either pair, apart from the compatibility already forced by (1).

**Proof of extension.** Write the \(U_0\) coordinates as

\[
z=x_1/x_0,\quad y=x_2/x_0,\quad D=x_3/x_0,
\]

and the \(U_\infty\) coordinates as

\[
A=x_0/x_3,\quad B=x_1/x_3,\quad W=x_2/x_3.
\]

A section identity for twist \(d\) is

\[
h_\infty(A,B,W)=A^d h_0(B/A,W/A,1/A).
\]

The monomial \(z^iy^jD^k\) contributes \(B^iW^jA^{d-i-j-k}\). Distinct triples give distinct Laurent monomials, so there is no cancellation of negative powers of \(A\). Polynomiality on both charts is exactly the condition that every monomial of \(h_0\) has total degree at most \(d\). Consequently \(x_0^d h_0\) is a unique homogeneous polynomial of degree \(d\). This directly proves extension across \(M\), without a bundle-splitting assumption or a convergence argument.

Apply this to obtain \(F_a,G_b\). They have no common surface component: a surface cannot be contained in the line \(M\), so any common surface would meet \(U\), contradicting the prescribed one-dimensional support there. Thus \(Y=V(F,G)\) is a proper projective complete-intersection curve. Every component outside \(C\) is contained in \(M\). Since \(M\cap C=\varnothing\), any such component would disconnect the support of \(Y\).

For completeness, the Koszul resolution and the intermediate cohomology vanishing for line bundles on \(\mathbf P^3\) give

\[
H^1(\mathcal I_Y)=0,\qquad H^0(\mathcal O_Y)=k.
\]

Hence \(Y\) is connected, including when it is nonreduced. No residual component exists. The converse is restriction of the homogeneous equations. The cohomology input is [Stacks, Lemma 30.8.1](https://stacks.math.columbia.edu/tag/01XS).

**Geometric meaning.** Compatibility of two arbitrary local ideals is weaker than (1). But once the equations themselves are sections of the same split ambient bundle \(\mathcal O(a)\oplus\mathcal O(b)\), there is no independent curve-at-\(M\) problem left. The complement is codimension two, the sections extend, and a disconnected extra component is impossible for their complete intersection. This is an explicit polynomial version of the [full fixed-twist formal-section theorem](formal_residual_visibility.md#6-an-exact-construction-oriented-reformulation).

More generally one may first glue the pairs as a section of a rank-two bundle on \(U\). If that bundle is then proved isomorphic to \(\mathcal O_U(a)\oplus\mathcal O_U(b)\), the same conclusion follows after applying that isomorphism. No assertion that arbitrary bundles on \(U\) split, or descend from the base of a ruling, is used here.

## 2. For any chosen affine radical pair, every global failure is visible at one endpoint

Let \(f,g\in k[z,y,D]\) be **any** pair with

\[
\sqrt{(f,g)}=I_{C\cap U_0},
\]

and let \(F,G\) be their ordinary homogenizations. They have no common factor: an affine common hypersurface factor contradicts the radical equality, and ordinary homogenization introduces no \(x_0\) factor. Thus \(Y=V(F,G)\) is a proper CI. Let \(m\) be its generic length along \(C\).

**Single-endpoint criterion.** The following are equivalent:

1. \(Y_{\mathrm{red}}=C\).
2. The completed ideal at \(p_\infty\) contains a power of the completed ideal of \(C\):
   \[
   I_{C,p_\infty}^{N}\widehat{\mathcal O}_{\mathbf P^3,p_\infty}
   \subset (F,G)\widehat{\mathcal O}_{\mathbf P^3,p_\infty}
   \quad\text{for some }N.
   \]
3. The Hilbert–Samuel multiplicity at the endpoint satisfies \(e_{p_\infty}(Y)=m\).

**Proof.** All residual components lie in \(H_\infty=V(x_0)\), because the affine zero set is prescribed. Their union, if nonempty, must meet \(C\) by the connectedness proved above. Since \(C\cap H_\infty=\{p_\infty\}\), some residual component passes through this endpoint. Power containment there excludes such a component; its implication in the local ring follows by faithful-flat contraction from completion. Conversely sole support gives power containment by Noetherianity.

For the multiplicity statement, associativity, smoothness of \(C\), and Cohen–Macaulay purity of the CI give

\[
e_{p_\infty}(Y)
=m+\sum_{D_j\ne C,\ p_\infty\in D_j}
 m_j e_{p_\infty}(D_j).
\]

Every summand is positive. The sum is nonempty precisely when residual components exist, by the preceding argument. One may compute the left side as the length after a sufficiently general local linear slice. The slice-length foundation is [Stacks, Lemma 42.3.2](https://stacks.math.columbia.edu/tag/02QG). This specializes the inherited all-points detector, rather than asserting a new multiplicity theorem.

**Geometric meaning.** An affine STCI pair can acquire a long or reducible residual configuration at infinity. Some components can attach through other residual components, so it is false that every one must pass through \(p_\infty\). Nevertheless the entire failure cannot hide away from that endpoint. A full local endpoint test therefore decides a chosen affine pair, without scanning the whole boundary plane.

This gives the precise scope of a valuative attack: adapt valuations and residue data to the **full endpoint ideal** and its generic thickness. A universal strict inequality \(e_{p_\infty}(Y)>m\) for every characteristic-zero affine radical pair would prove non-STCI. No such inequality has been established here. Conversely a pair achieving equality would construct an STCI. The criterion makes that target exact; it does not supply either outcome.

## 3. The two reduced affine generators do not form an invertible transition on the whole overlap

Put

\[
q=x_0x_3-x_1x_2,\quad c_0=x_1^3-x_0^2x_2,\quad
c_\infty=x_2^3-x_1x_3^2.
\]

The normalized pairs \((q/x_0^2,c_0/x_0^3)\) and \((q/x_3^2,c_\infty/x_3^3)\) generate the reduced ideals on their respective affines. Write the first pair as \((q_0,c_{0,0})=(D-zy,z^3-y)\). The exact identity

\[
x_0^2c_\infty=-x_2^2c_0-(2x_1^2x_2+x_1q)q
\]

gives on the overlap

\[
\binom{q_\infty}{c_{\infty,\infty}}
=
\begin{pmatrix}
D^{-2}&0\\
-D^{-3}(2z^2y+zq_0)&-D^{-3}y^2
\end{pmatrix}
\binom{q_0}{c_{0,0}}.                         \tag{2}
\]

This matrix has determinant \(-y^2D^{-5}\), which is not a unit on the whole overlap \(\operatorname{Spec}k[z,y,D,D^{-1}]\). It is invertible near the overlap with \(C\), where \(y\ne0\).

In fact **no** invertible matrix on that whole overlap transforms these two generating pairs into each other. To see this, set \(z=t,y=t^3,D=t^4\) on \(C\cap U_0\cap U_\infty\). Every such matrix must induce the same map on \(I_C/I_C^2\); its determinant restricts to

\[
-t^{-14}.
\]

But every unit of \(k[z,y,D,D^{-1}]\) is \(cD^n\), restricting to \(ct^{4n}\). The exponent \(-14\) is not divisible by four. This is a contradiction. The conclusion also holds after replacing either affine pair by any other two generators of the same reduced ideal: along each affine copy of \(\mathbf A^1\subset C\), the determinant of a basis change is a nonzero constant, and cannot change the exponent.

**Geometric meaning.** Two generating pairs can define exactly the same ideal on the overlap without being related by a globally invertible two-by-two matrix there. The determinant obstruction is the degree-\(14\) normal determinant of the reduced quartic, versus the multiples of four obtained by restricting ambient line bundles. It is the familiar reduced-curve adjunction obstruction in explicit endpoint coordinates, not a new obstruction to arbitrary higher multiple structures. A successful higher thickening can have different determinant data; its entire transition, including nonlinear terms, still has to be handled.

For clarity, the full graph coordinates also show the nonlinearity directly. Put

\[
u=D-z^4,\quad v=y-z^3,
\qquad u'=A-W^4,\quad v'=B-W^3.
\]

Then, with \(D=z^4+u\),

\[
W=\frac{z^3+v}{D},\qquad
u'=\frac{D^3-(z^3+v)^4}{D^4},\qquad
v'=\frac{zD^2-(z^3+v)^3}{D^3}.                \tag{3}
\]

These identities hold on the actual ambient overlap. Replacing \(D\) by \(z^4\) or retaining only their linear terms records a normal symbol, not an actual transition of equations. In particular the base-coordinate change itself has normal corrections.

## 4. What endpoint orders omit, and the exact stopping point

The hyperplane-at-infinity degree filtration is the ambient valuation at the generic point of that plane. It is distinct from the point valuation on \(k(C)\) or an ambient valuation centered at the closed endpoint. In the \(U_0\) coordinates it sends \(z,y,D\) to \(-1\). In graph coordinates its values on \(z,v,u\) are respectively \(-1,-3,-4\), but those three weights alone do not define it: the exact cancellations

\[
y=z^3+v,\qquad D=z^4+u
\]

raise both values to \(-1\). Thus termwise endpoint weights in a chosen normal frame can lose precisely the cancellations controlling homogeneous degree and actual extension. This concrete example complements the inherited warning that scalar valuation data omit residue relations.

There is no conflict with the [full formal-section theorem](formal_residual_visibility.md#6-an-exact-construction-oriented-reformulation). **Full** fixed-twist formal gluing at all orders, together with uniform power containment, is already enough. The unresolved step is producing that data from generic normal forms, finitely many jets, or coefficient valuations. Equations (1) and (3), or the inherited full formal-section formulation, specify what must eventually be proved; there is no license to replace them by first-order determinant matching.

The contribution of this stream is therefore a sharply located route and failure analysis: simultaneous actual two-chart descent automatically handles the remote line; any chosen affine pair can be tested at its one omitted endpoint; and the naïve reduced-generator gluing fails even before bundle splitting. No higher-degree class has been excluded, no successful higher thickening has been constructed, and the characteristic-zero question remains open.
