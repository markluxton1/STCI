# Jacobian duality, pencil geometry, and Hamiltonian actions

Unless a characteristic extension is stated explicitly, \(k\) is
algebraically closed of characteristic zero,
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\), and
\(Z=V(F_a,G_b)\) is a proper homogeneous complete intersection with
\(Z_{\mathrm{red}}=C\). Put \(m=ab/4\), \(d=a+b\),
\(p_0=[1:0:0:0]\), and \(p_\infty=[0:0:0:1]\).
Here \(\mathcal O_C(r)\) means degree \(r\) on \(C\simeq\mathbf P^1\);
an ambient twist by one has degree four. These are independently reviewed
**provisional** deductions, not promoted results. The Jacobian and
Hamiltonian arguments apply to arbitrary supported pairs without assuming
a smooth carrier, normal flatness, saturation of a first normal relation,
or a retraction onto \(C\). The pencil also has a polarized retraction
obstruction proved below. These statements retain actual embedded
geometry; realizing compatible global equations remains a separate problem.

**Review status (2026-10-31).** Independent mathematical and preservation review reconstructed the Jacobian and Hamiltonian deductions and their explicit characteristic extensions. The varying-Hilbert-function local control, degree-four defect notation, and ribbon section calculation were checked in their corrected homes. No material finding remains unresolved within the stated scopes. These remain reviewed provisional deductions, with no canonical promotion; no computation or inherited certificate rerun was needed.

## The actual socle and a projection-change lemma

Closed-immersion duality, as in [R-0032](../results/full_conormal_socle_budget.md), gives

\[
\mathcal S=\operatorname{Ann}_{\mathcal O_Z}(\mathcal I_C\mathcal O_Z)
 =\omega_C\otimes\omega_Z^{-1}|_C=\mathcal O_C(14-4d).
\]

The following local argument explains how actual Jacobians generate this
line; it does not replace the full thickening by its associated graded.

**Lemma.** Let \(W=(h_1,h_2)\) be a complete-intersection curve in a smooth
threefold, with smooth reduced support \(D\). In algebraic étale coordinates
\((z,u,v)\), suppose \(D=(u,v)\) and \(z|_D\) is étale. Write
\(J_{ij}=h_{1,i}h_{2,j}-h_{1,j}h_{2,i}\). In \(\mathcal O_W\),

\[
(J_{uv})=\operatorname{Ann}(u,v),\qquad J_{zu}=J_{zv}=0. \tag{1}
\]

**Proof.** At each closed point complete along the curve parameter.
The resulting algebra \(A\) is finite free of rank \(m\) over the DVR
\(R=k[[z-z(p)]]\): it is finite because its reduction is \(R\), and
Cohen–Macaulay purity makes the parameter regular. Its socle
\(\Sigma=\operatorname{Ann}_A(u,v)\) is a saturated rank-one free
\(R\)-submodule. The Artinian CI Jacobian theorem first puts \(j=J_{uv}\)
in the socle over the fraction field, and torsion freeness puts it in
\(\Sigma\). Saturation injects \(\Sigma/\mathfrak m_R\Sigma\) into
\(A/\mathfrak m_RA\). This Artinian CI has length \(m\), and its Jacobian
is a nonzero socle generator in characteristic zero. Nakayama gives
\(\Sigma=Rj\). Completion is faithfully flat, so this holds algebraically.
The formal, nonhomogeneous Artin-Jacobian input is
[Eisenbud–Ulrich, Theorem 8.5](https://arxiv.org/pdf/1309.2050).

Now work on the algebraic neighborhood, not just one completed stalk.
For every constant \(\lambda\in k\), the coordinate
\(z_\lambda=z+\lambda u\) has the same restriction to \(D\), and its
relative Jacobian is \(j-\lambda J_{zv}\). Taking \(\lambda=1\) shows
\(J_{zv}=gj\) for a regular function \(g\) on \(D\). If \(g(p)\ne0\),
choose \(\lambda=g(p)^{-1}\). Then \((1-\lambda g)j\) fails to generate
the socle at \(p\), contradicting the generator assertion for \(z_\lambda\).
Thus \(g\) vanishes at every closed point of the reduced finite-type curve
and is zero. Changing to \(z+\lambda v\) similarly kills \(J_{zu}\). ∎

The algebraic neighborhood is essential: vanishing at the only closed point
of a formal local curve does not prove a power series zero. This proof also
avoids an unsupported comparison of absolute fundamental-class normalizations
for different relative projections. No exact multiplicity-normalized absolute
class-map assertion is needed.

A local control tests the absence of a normal-flatness hypothesis:

\[
A=k[[z,u,v]]/(u^2-zv,v^2)
\]

is free over \(k[[z]]\) on \(1,u,v,uv\). After inverting \(z\), eliminating
\(v=u^2/z\) makes its fiber curvilinear of length four; at \(z=0\) the
fiber is \(k[u,v]/(u^2,v^2)\), with a different normal Hilbert function.
Nevertheless \(J_{uv}=4uv\), \(J_{zu}=0\), and \(J_{zv}=-2v^2=0\).
In characteristic zero or odd characteristic the actual socle generator
and mixed-minor identities therefore persist through this Hilbert-function
jump. This is an exact local control, not a homogeneous projective pair.

## The six ambient minors, different, and contact identity

Put \(M_{ij}=F_{x_i}G_{x_j}-F_{x_j}G_{x_i}\). Their classes lie in
\(\mathcal S(d-2)=\mathcal O_C(6)\), and after one common nonzero scalar,

\[
(M_{01},M_{02},M_{03},M_{12},M_{13},M_{23})
=(t^6,-3s^2t^4,2s^3t^3,4s^3t^3,-3s^4t^2,s^6). \tag{2}
\]

Indeed (1) makes the local Jacobian tuple a nonzero socle multiple of the
reduced tangent direction. Euler's identities identify its homogeneous
complementary minors with the tangent plane of the affine cone. Differentiating
\(\phi=(s^4,s^3t,st^3,t^4)\) gives tangent Plücker coordinates
\((s^6,3s^4t^2,4s^3t^3,2s^3t^3,3s^2t^4,t^6)\), after dividing by four.
Complementation using \(dx_0\wedge dx_1\wedge dx_2\wedge dx_3\) gives (2).
The twist has degree \(14-4d+4(d-2)=6\). The actual and displayed tuples
have the same ratios and no common zero, so their ratio is an automorphism
of \(\mathcal O_C(6)\), hence one nonzero constant. In particular the six
minors generate the actual socle ideal sheaf.

The base-point-free projection \([x_0:x_3]:Z\to B=\mathbf P^1\) is finite
flat of degree \(ab\): its reduction is the finite degree-four map
\(f([s:t])=[s^4:t^4]\), properness makes it finite, and the CM source
makes its module over the smooth base torsion free. Its relative Jacobian
is \(M_{12}\). The Jacobian formula for the different
([Stacks 49.12](https://stacks.math.columbia.edu/tag/0BWB)) and (2) give

\[
R_f=3p_0+3p_\infty,\qquad
\mathfrak D_{Z/B}=\mathcal S(-R_f)\subset\mathcal O_Z. \tag{3}
\]

The displayed divisor is the zero divisor of \(M_{12}\) as a section on
the smooth support, with its indicated socle twist. The different is a
nilpotent ideal of the thick scheme; it is not a Cartier ramification
divisor on \(Z\), and \(Z\to B\) is not étale off these endpoints.
Multiplication by the nonzero section on the socle line is injective, so

\[
\operatorname{Ann}_{\mathcal O_Z}(M_{12})=\mathcal I_C\mathcal O_Z,
\qquad (F,G):M_{12}=I_C. \tag{4}
\]

The latter equality and \(M_{12}-2M_{03}\in(F,G)\) hold in the polynomial
ring because a homogeneous CI curve ideal is saturated. Thus

\[
M_{12}-2M_{03}=A_{b-2}F+B_{a-2}G. \tag{5}
\]

The cone is Lagrangian for
\(\omega=dx_0\wedge dx_3-2dx_1\wedge dx_2\). Up to an overall sign its
Poisson bracket is

\[
\{H,K\}=H_0K_3-H_3K_0-\tfrac12(H_1K_2-H_2K_1).
\]

Equation (5) means \(\{F,G\}\in(F,G)\), equivalently the **actual thick
ideal** is involutive. The reduced Legendrian criterion alone would only
control its radical. [Buczyński, §§3–5](https://arxiv.org/pdf/math/0503528)
provides the reduced contact dictionary; its normal irreducible-CI theorems
cannot be transferred to this everywhere nonreduced scheme.

## A pencil-compatible polarized retraction cannot extend globally

Write \(i:C\hookrightarrow Z\), \(\pi:Z\to B\) for the pencil above,
\(f=\pi\circ i\), and
\[
L=\mathcal O_Z(1)=\pi^*\mathcal O_B(1).
\]
The equality follows from the two generating ambient sections \(x_0,x_3\),
which have no common zero on \(Z\). There is no retraction
\(r:Z\to C\) satisfying both
\[
r\circ i=\mathrm{id}_C,\qquad f\circ r=\pi. \tag{Retract}
\]

**Proof.** Nondegeneracy of the embedded quartic forces \(a,b\ge2\).
The complete-intersection resolution, twisted by one, is
\[
0\longrightarrow\mathcal O_{\mathbf P^3}(1-a-b)
\longrightarrow\mathcal O_{\mathbf P^3}(1-a)\oplus
                    \mathcal O_{\mathbf P^3}(1-b)
\longrightarrow\mathcal I_Z(1)\longrightarrow0.
\]
Intermediate line-bundle cohomology on \(\mathbf P^3\) vanishes in
every characteristic, so \(H^0(\mathcal I_Z(1))=H^1(\mathcal I_Z(1))=0\).
Consequently ambient linear forms give
\[
h^0(Z,L)=4,\qquad
h^0(C,i^*L)=h^0(\mathbf P^1,\mathcal O_{\mathbf P^1}(4))=5. \tag{Sections}
\]
Here \(i^*L\) has degree four in this chapter's curve-degree notation.
If (Retract) held, its pencil compatibility would identify
\[
r^*i^*L=(f\circ r)^*\mathcal O_B(1)=L
\]
compatibly with restriction to \(C\). Pullback along \(r\) would then
split
\[
H^0(Z,L)\longrightarrow H^0(C,i^*L).
\]
This would make a map from a four-dimensional space onto a five-dimensional
space surjective, which is impossible. ∎

This section-count proof is characteristic free under the same proper
supported-complete-intersection hypothesis; it uses no Jacobian, trace,
or separability assertion. For \(\operatorname{char}k\ne2\), however,
\(C^\circ\to B^\circ\) is finite étale, where
\(B^\circ=B\setminus\{0,\infty\}\), \(Z^\circ=\pi^{-1}(B^\circ)\),
and \(C^\circ=C\cap Z^\circ\). Formal étaleness uniquely lifts the
identity of \(C^\circ\) across the nilpotent immersion
\(C^\circ\hookrightarrow Z^\circ\), giving a unique retraction over
\(B^\circ\). See [Stacks, Theorem 41.15.1](https://stacks.math.columbia.edu/tag/06NE).
It follows that this particular punctured retraction cannot extend to a
retraction over all of \(B\). The proof does not identify an obstructing
endpoint. In characteristic two the reduced pencil is purely inseparable;
this formal-étale existence and uniqueness assertion is not available.

The section argument has a general form. Suppose
\(D\subset Y\subset\mathbf P^N\), ambient linear forms surject onto
\(H^0(Y,H)\) for \(H=\mathcal O_Y(1)\), and the given embedding of
\(D\) is not linearly normal. There is no retraction \(r:Y\to D\)
with an isomorphism \(r^*(H|_D)\simeq H\) compatible with restriction
along \(D\). Such an isomorphism and \(r|_D=\mathrm{id}_D\) would split
restriction on global sections. Its composition with the ambient
linear-section map would surject onto \(H^0(D,H|_D)\), contrary to the
failure of linear normality. This criterion is also characteristic free.

For the quartic, a pencil-compatible retraction would lift the omitted
section \(s^2t^2\). Its failure is the geometric consequence of the
existing missing fifth hyperplane section, not another numerical budget.
It excludes no arbitrary unpolarized abstract retraction and gives no
endpoint classification or STCI contradiction. In particular, the
section argument remains consistent with the supported complete
intersections in positive characteristic. The corollary and its general
polarized form carry a separate inherited scoped independent review;
they remain provisional.

## Hamiltonian actions in the entirely thick branch

On \(U=\mathbf A^4\setminus\{0\}\), let \(L\) be the smooth punctured cone,
\(P=\mathcal I_L\), \(X=V(F,G)\cap U\), and \(N=P\mathcal O_X\). Assume
\(F,G\in P^2\) as **ideal sheaves on \(U\)**. No square membership at the
vertex is implied. For either induced Hamiltonian derivation \(\delta\),
Leibniz and \(\{P,P\}\subset P\) give

\[
\delta(\mathcal O_X)\subset N,\qquad
\delta(N^j)\subset N^{j+1}\ (j\ge1). \tag{6}
\]

One uniform power of \(N\) is zero; hence a uniform power of \(\delta\)
is zero. The finite exponential \(\exp(t\delta)\) defines a
\(\mathbf G_a\)-action on \(X\), with inverse \(\exp(-t\delta)\), fixing
\(L\) pointwise. The sheaf maps glue because they preserve the same reduced
opens. They need not extend across the vertex or descend projectively:
the derivation generally has positive degree \(a-2\) or \(b-2\).

Every derivation preserving \(N\) preserves \(\Sigma=\operatorname{Ann}N\):
differentiate \(sn=0\). By (6) its action on \(\Sigma\) is
\(\mathcal O_L\)-linear. This module is a line bundle by duality, so its
endomorphism is multiplication by a function on reduced \(L\). Nilpotence
forces that function zero. Both Hamiltonians therefore kill the **entire**
socle, including both endpoint neighborhoods.

There is also a sharper homogeneous cofactor condition. Write
\(\{F,G\}=AF+BG\) with the degrees in (5). These cofactors are unique:
their difference would be a Koszul syzygy \((HG,-HF)\) with
\(\deg H=-2\). At the generic point of \(L\), \(I=(F,G)\) is
\(P\)-primary and \(I/PI\) has basis \(F,G\) over \(k(L)\). The action of
\(\delta_F\) is linear there and nilpotent: for \(P^r\subset I\), repeated
application sends \(I\subset P^2\) into \(P^{r+1}\subset PI\). Its matrix is
\(\left(\begin{smallmatrix}0&A\\0&B\end{smallmatrix}\right)\), so \(B|_L=0\).
The trace of \(\delta_G\) is \(-A\), hence \(A|_L=0\). Integrality and
homogeneity give \(A,B\in I_C\), or

\[
\{F,G\}\in I_C(F,G). \tag{7}
\]

The involutive-ideal complex begins

\[
\mathcal O_X\longrightarrow\mathcal Hom(I/I^2,\mathcal O_X),
\quad h\longmapsto(F\mapsto\{F,h\},G\mapsto\{G,h\}).
\]

Its zeroth kernel contains \(\Sigma\). Over \(\mathbf C\) every socle
stalk is infinite-dimensional as a vector space, since it is a line over
the positive-dimensional support's local ring. Thus the kernel does not
have finite-dimensional constructible stalks. The reduced Lagrangian
constant-kernel/rigidity theory of
[Sevenheck–van Straten](https://arxiv.org/pdf/math/0002083) and their
[rigidity paper](https://arxiv.org/pdf/math/0311503) cannot simply be applied.
Indeed both first derivatives vanish everywhere, making the embedding
dimension four throughout the two-dimensional support; their Condition P
bound for the corresponding \(S_0\) stratum fails. This computes no first
cohomology and supplies no nonexistence theorem. In a cotangent chart
\(I=(p_1^2,p_2^2)\), every \(h(q_1,q_2)p_1p_2\) is in the common kernel:
the flows move nilpotent transverse structure, not the reduced support.

## Exact characteristic boundaries

The socle line from closed-immersion duality is characteristic free for
an actual CI on this smooth support. The local Artinian Jacobian step
is more restrictive: its trace is \(h\mapsto m\bar h\). Over an
algebraically closed field of characteristic \(p>0\), the proof of (1)
still works when \(p\nmid m\), including the algebraic closed-point
projection-change argument. When \(p\mid m\), the relative Jacobian is
zero, so its socle-generation and subsequent recovery statements cannot
be retained. This is a genuine loss of information, not failure to define
a trace or a dualizing module.

For odd \(p\nmid m\), the same calculation gives (2)–(5): four is
invertible in the tangent computation, the reduced fourfold projection
is separable and tame, and the displayed symplectic form is nondegenerate
because two is invertible. This supplies the contact compatibility for
those hypothetical pairs; it is not a positive-characteristic exclusion.
For \(p=2\), the reduced fourfold projection is purely inseparable and the
displayed contact form degenerates, so this symplectic interpretation and
the ramification description (3) are not asserted. The characteristic-seven
supported pair in the [tropical chapter](tropical_thickenings_and_endpoint_duality.md#positive-movement-and-the-global-presentation-barrier)
has \(m=7\) and \(M_{12}=0\), even though the reduced cover is tame.

For an involutive ideal with a smooth Lagrangian support in any
characteristic where the symplectic form exists, the filtration inclusions
(6) are algebraic and remain valid. They make the derivations nilpotent.
However the characteristic-zero exponential uses factorial denominators;
nilpotence alone in characteristic \(p\) does not establish the stated
algebraic additive-group action by this proof. Likewise the deduction that
the socle action is zero uses only nilpotence and reducedness once the
socle is a line, but a full positive-characteristic version of the
Hamiltonian conclusion must separately establish its involutive-ideal
input. The complex's large socle kernel is then the same algebraic
phenomenon; its complex-analytic constructibility interpretation is
specifically over \(\mathbf C\). The every-positive-characteristic STCI
construction is compatible with these boundaries and does not contradict
any characteristic-zero exclusion.

## Controls and the precise remaining implication

The twisted cubic \(T=[s^3:s^2t:st^2:t^3]\) has the actual supported CI

\[
f=x_0x_2-x_1^2,\qquad
g=x_2^3-2x_1x_2x_3+x_0x_3^2.
\]

On \(x_0=1\), \(x_2=x_1^2\) and \(g=(x_3-x_1^3)^2\); on \(x_0=0\) the
only common point is \([0:0:0:1]\). Thus this is generically double on \(T\).
For \(dx_0\wedge dx_3-3dx_1\wedge dx_2\), direct differentiation gives
\(M_{12}-3M_{03}=-4x_3f\), or \(\{f,g\}=\tfrac43x_3f\). Involutivity is
therefore compatible with an actual nonlinear supported CI.

Even homogeneous commuting generators of the same ideal need not exist.
The entirely thick degree-\((6,6)\) ideal \(J=(f^3,g^2)\) satisfies
\(\{f^3,g^2\}=8x_3f^3g\ne0\). Its degree-six piece is exactly the span
of its two generators; any homogeneous minimal generating pair is an
invertible constant change of this pair, multiplying the bracket by a
nonzero determinant. No such pair commutes. With central parameters,
\((F-\lambda,G-\mu)\) is involutive exactly when \(\{F,G\}=0\), by
substituting \(\lambda=F,\mu=G\). Thus an involutive zero level does not
supply an involutive universal level-set family; compare
[Garay, §1](https://www.journalofsing.org/volume8/garay.pdf).

Finally \(q=x_0x_3-x_1x_2\) has Hamiltonian coordinate weights
\((-1,-\tfrac12,\tfrac12,1)\), proportional to the quartic torus weights
modulo scalar dilation. But \(q\) is only in the radical: involutivity of
\((F,G)\) does not imply its invariance under \(\{q,-\}\), a torus action,
or an equivariant splitting. The realization problem still concerns the
quartic's actual global homogeneous equations. The socle and contact identities
constrain any such pair, while the polarized retraction obstruction explains one failure
of extending the punctured pencil geometry. None supplies an arbitrary
unpolarized splitting or a contradiction for every homogeneous pair; the
remaining task is an actual supported construction or an obstruction with
the necessary global coverage.
