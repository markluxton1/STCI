# The residual-pair flag threefold of the fixed rational quartic

Date: 2026-10-24. Author role: `flag_incidence`. **Status: new provisional
research evidence, with explicit proofs; not a canonical result or an STCI
assertion.** Work over an algebraically closed field of characteristic zero
unless a characteristic is stated separately. The curve and marked system
are exactly
\[
C=[s^4:s^3t:st^3:t^4],\qquad
V=\langle s^4,s^3t,st^3,t^4\rangle\subset W=H^0(C,\mathcal O(4)).
\]
Here degrees on the parameter curve refer to its identification with
\(\mathbf P^1\). The projective space \(\mathbf P(V)\) parametrizes
hyperplane **sections**, while the ambient embedding is in
\(\mathbf P(V^\vee)\).

The retrieval route was [INDEX](../INDEX.md), the
[contribution checklist](../CONTRIBUTING_AGENT.md), the
[discussion reconciliation](2026-10-24-discussion-reconciliation.md), and the
[symmetric-square note](2026-10-24-quartic-symmetric-square-bitangents.md)
with its [independent audit](2026-10-24-quartic-symmetric-independent-audit.md).
The group and secant-map facts used below are retained in their exact
characteristic-zero scopes from those independently audited exploratory
notes. They are not canonically promoted. No accepted normal-bundle or
STCI theorem is required. The new arguments concern the global flag,
factorization map, its ramification, and the full group action.

## 1. Construction over arbitrary bases and nonreduced divisors

Put \(U=H^0(\mathbf P^1,\mathcal O(2))\) and
\(P=\operatorname{Sym}^2 C=\mathbf P(U)\), with the convention of lines
of sections. Multiplication of binary forms defines a morphism
\[
m:P\times P\longrightarrow\mathbf P(W),\qquad([h],[k])\longmapsto[hk].
\]
It has no basepoints, because a product of nonzero sections on the integral
curve is nonzero. Define the incidence scheme by the Cartesian square
\[
\mathcal I=(P\times P)\times_{\mathbf P(W)}\mathbf P(V).
\tag{1}
\]
This definition includes all nonreduced divisors and works after arbitrary
base change. Equivalently, its points over a scheme consist of two relative
effective Cartier divisors of degree two whose sum belongs to the marked
relative hyperplane system. No disjointness, reducedness, or secant
injectivity is imposed.

The quotient map \(z:W\to W/V\), a map to a one-dimensional vector
space, produces the symmetric bilinear form
\[
b_z:U\otimes U\longrightarrow W/V,\qquad (h,k)\longmapsto z(hk).
\tag{2}
\]
Thus \(\mathcal I=V(b_z)\) is globally a divisor of bidegree \((1,1)\).
Choose a scalar trivialization of \(W/V\), and write
\[
h=\alpha s^2+\beta st+\gamma t^2,\qquad
k=A s^2+Bst+Ct^2.
\]
The equation, including every boundary configuration, is
\[
\alpha C+\beta B+\gamma A=0,
\qquad
M_z=\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix},
\qquad\det M_z=-1.
\tag{3}
\]
In particular this pairing is nondegenerate in **every** characteristic.
The displayed calculation verifies the intrinsic construction; it does
not replace it by an affine incidence condition.

For a second bundle construction, let \(\mathcal Z\subset C\times P\)
be the universal degree-two divisor. Evaluation gives a rank-two bundle
\(\mathcal E=p_*\mathcal O_{\mathcal Z}(4)\) and a surjection
\(V\otimes\mathcal O_P\to\mathcal E\). Surjectivity follows from the
fact that the marked system embeds \(C\), hence separates length-two
subschemes. Its rank-two kernel \(\mathcal K\) parametrizes planes
containing the secant or tangent determined by the divisor. Multiplication
by the universal quadratic identifies
\[
\mathcal K\simeq\mathcal O_P(-1)\otimes
\ker\big(U\otimes\mathcal O_P\xrightarrow{b_z(h,-)}\mathcal O_P(1)\big).
\]
Tensoring a bundle by a line bundle does not change its projective bundle.
Consequently \(\mathbf P_P(\mathcal K)\simeq\mathcal I\), and the
residual divisor is defined globally by division by the universal Cartier
divisor. This proves the claimed secant–plane interpretation over arbitrary
bases, including infinitesimal families.

## 2. Exactly when this is a flag variety

The isomorphism \(b_z:U\simeq U^*\otimes(W/V)\) identifies the second
factor with \(\mathbf P(U^*)\). Under that identification,
\[
\mathcal I\simeq\{(x,\ell):x\in\ell\}\subset
\mathbf P(U)\times\mathbf P(U^*)=F(1,2;U).
\tag{4}
\]
This is an isomorphism of the **marked two projections**, with the second
projection identified by \(b_z\); no prior duality between the two copies
of \(P\) is assumed. Both projections are smooth projective-line bundles.

More generally, for any codimension-one system \(V'\subset W\), this
same incidence construction is the usual flag incidence precisely when
its multiplication pairing has rank three. Indeed rank three gives (4).
Multiplication onto \(W\) is surjective, so the pairing is nonzero.
If its rank is one or two, the product of its two projectivized
radicals is a nonempty singular subscheme of the bilinear hypersurface:
at a pair of radical vectors both partial differentials vanish. It
therefore cannot be isomorphic to the smooth flag threefold. This
criterion does not claim that every degenerate system embeds the curve.

The plane \(\operatorname{Sym}^2 C\), its diagonal conic, multiplication
of divisors, and addition of relative effective divisors are intrinsic to
\(C\). The line bundle of degree two is unique up to isomorphism on this
rational curve; changing its scalar identification has no projective
effect. The selected hyperplane system, \(z\), the form \(b_z\), its
polarity, and the resulting marked flag construction belong to the
**embedded** curve. They are independent of coordinates but are not data
of an unmarked abstract rational curve. The abstract flag variety alone
forgets the distinguished diagonal conic and the map to \(\mathbf P(V)\).
Its larger abstract automorphism group must not be substituted for the
automorphism group of the embedded quartic.

Write \(H_1,H_2\) for the two hyperplane classes. Adjunction gives
\(K_{\mathcal I}=-2H_1-2H_2\). The usual cotangent realization
\(\mathcal I\simeq\mathbf P(T^*P)\) supplies the canonical contact
structure of a three-dimensional incidence flag variety. In representatives
it is
\[
\ker b_z(y,dx),\qquad b_z(x,y)=0,
\tag{5}
\]
with contact line bundle \(\mathcal O_{\mathcal I}(1,1)\). Formula (5)
means the usual twisted one-form; no affine trivialization is canonical.

## 3. Residual swap, its fixed scheme, and polarity

The operation
\[
\tau([h],[k])=([k],[h])
\]
is defined over the whole scheme and exchanges the two rulings. It is a
polarity duality of the flag variety, induced by \(b_z\), rather than a
self-map of its first base plane. In the ambient product its equalizer
with the identity is the diagonal, including its full scheme structure.
Consequently
\[
\operatorname{Fix}_{\mathcal I}(\tau)
=\{([h],[h]):z(h^2)=0\}
\simeq V(\beta^2+2\alpha\gamma)=:\mathcal B.
\tag{6}
\]
Over characteristic zero it is exactly the smooth bitangent conic,
including the endpoint quadruple-contact sections. The multiplication map
on this conic is \([h]\mapsto[h^2]\), the embedded rational quartic of
bitangent planes. The equation proves fixed **scheme**, not just fixed
support.

The same equalizer calculation in characteristic two gives the double
line \(V(\beta^2)\), even though \(\mathcal I\) remains a smooth flag
threefold. For characteristic different from two the conic is smooth;
in characteristic three it coincides with the diagonal conic of doubled
points, so its generic member does not represent two distinct tangent
contacts. The ordinary bitangent interpretation used here therefore
requires the stated characteristic-zero assumption (or further separate
analysis away from characteristics two and three).

Differentiation of \(b_z(x,y)=0\) shows that swap sends the contact form
in (5) to its negative. Thus it preserves the contact distribution. On
its fixed conic, differentiation of \(b_z(x,x)=0\) gives
\(b_z(x,dx)=0\) in characteristic different from two. The fixed conic
is therefore a Legendrian curve in the flag contact threefold. This is an
intrinsic interpretation of the bitangent conic after retaining the
embedding polarity, not an identification with the osculating involution.

## 4. The map to hyperplanes: six factorizations and all boundary fibers

Restriction of multiplication defines
\[
f:\mathcal I\longrightarrow\mathbf P(V),\qquad(D,R)\longmapsto D+R,
\quad f^*\mathcal O(1)=\mathcal O_{\mathcal I}(1,1).
\tag{7}
\]
It is **finite flat of degree six**. To see this globally, the addition
map \(\operatorname{Sym}^2 C\times\operatorname{Sym}^2 C\to
\operatorname{Sym}^4 C\) is proper and has finite fibers, hence is
finite. Source and target are smooth of the same dimension, so the
finite map is flat by the regular-target/Cohen–Macaulay-source criterion.
Its degree is six from the choices of two among four distinct points.
Equation (1) is its base change to \(\mathbf P(V)\).

This also describes the nonreduced fibers. If
\(E=\sum m_i p_i\) and \(D=\sum n_i p_i\), with
\(0\leq n_i\leq m_i\) and \(\sum n_i=2\), the corresponding
point of \(f^{-1}(E)\) has length
\(\prod_i\binom{m_i}{n_i}\). Distinct support clusters split étale
locally; each cluster multiplication map is finite flat with the stated
binomial degree and a unique point over its fully concentrated divisor.
Thus the complete list by root partition is:

| Hyperplane divisor partition | Fiber support and local lengths |
| --- | --- |
| \(1+1+1+1\) | Six reduced points |
| \(2+1+1\) | Two reduced points and two points of length two |
| \(2+2\) | Two reduced points and one point of length four |
| \(3+1\) | Two points, each of length three |
| \(4\) | One point of length six |

For example at an endpoint quadruple root, take monic factors
\(h=v^2+av+b\), \(k=v^2+cv+d\). The fiber over \(v^4\)
has \(c=-a\), \(d=a^2-b\), and local algebra
\[
k[a,b]/(a^3-2ab,\ a^2b-b^2).
\tag{8}
\]
It has length six and embedding dimension two in characteristic zero;
replacing it by its single support point would discard most of the fiber.

The ramification divisor is
\[
\operatorname{Ram}(f)=V(\operatorname{Res}(h,k)),\qquad
[\operatorname{Ram}(f)]=2H_1+2H_2.
\tag{9}
\]
Indeed multiplication is étale when the two factors are coprime, by
unique infinitesimal division; its differential loses rank exactly when
they share a root. In a monic chart the Jacobian determinant is the
resultant up to sign; (9) also follows from the canonical classes and
(7). The branch support is the discriminant \(C^\vee\). At a quartic
with precisely one double root, its two factorizations that split the
double root each have simple ramification, whereas the two factorizations
that keep the double root together are unramified. Therefore, as cycles,
\[
f_*\operatorname{Ram}(f)=2[C^\vee].
\]
In particular the conormal surface described below is generally **not**
the ramification divisor of this map.

Swap preserves (7). Its quotient parametrizes the three unordered
partitions of a general four-point divisor into pairs and gives a finite
degree-three map \(\mathcal I/\langle\tau\rangle\to\mathbf P(V)\).
In characteristic zero this quotient has transverse ordinary quadratic
quotient singularities along the image of the fixed conic: locally the
involution acts by \((t,x,y)\mapsto(t,-x,-y)\), so the invariant local
algebra has the relation \((xy)^2=x^2y^2\). This observation does not
identify the quotient with the dual surface; their dimensions differ.

## 5. Secant lines and what the flag remembers over trisecants

Let \(\sigma:P\to\operatorname{Gr}(2,V^*)\) be the global secant
morphism, constructed by the universal rank-two evaluation bundle; the
diagonal gives tangent lines. There are two maps
\[
\ell_1=\sigma\circ\operatorname{pr}_1,\qquad
\ell_2=\sigma\circ\operatorname{pr}_2.
\]
The two lines \(\ell_1(D,R),\ell_2(D,R)\) lie in the hyperplane
\(f(D,R)\). Swap exchanges these line maps and fixes the hyperplane map.

Retain the audited facts from the
[symmetric-square note, Section 2](2026-10-24-quartic-symmetric-square-bitangents.md):
\(\sigma\) is the finite birational normalization of its secant surface
\(S\) in the Grassmannian; a general trisecant ruling of the unique
quadric has three reduced inverse pairs; an endpoint tangent trisecant
has one inverse pair with curvilinear length three. In the finite chart
\(a=u+v,b=uv\), a trisecant ruling of parameter \(\kappa\) has fiber
\[
(b-a^2,\ a^3+\kappa).
\tag{10}
\]
These are retained premises, not new computations of inherited results.

Let
\[
J=\{(L,H):L\in S,\ L\subset H\}.
\]
It is the projective-line bundle over \(S\) of planes containing its
universal line. The diagram
\[
\mathcal I\longrightarrow J,\qquad (D,R)\longmapsto(\sigma(D),f(D,R))
\]
is the base change of \(\sigma:P\to S\), because the bundle
construction in Section 1 parametrizes exactly the same plane pencil.
It is consequently finite birational; \(\mathcal I\) is smooth and
is the normalization of the integral threefold \(J\). For every plane
through a given trisecant, the fiber of \(\mathcal I\to J\) has the
same scheme structure as (10). The residual divisor depends on the plane,
but does not recover which pair was forgotten by \(\sigma\). Thus the
secant–plane flag with its marked divisor is smooth; forgetting that
marking produces precisely the known trisecant identifications.

## 6. Conormal and bitangent correspondences inside one threefold

Let \(\mathcal D\subset P\) be the diagonal conic of doubled points,
\(\beta^2-4\alpha\gamma=0\). Then
\[
N_1=\operatorname{pr}_1^{-1}(\mathcal D),\qquad
N_2=\operatorname{pr}_2^{-1}(\mathcal D)=\tau(N_1)
\tag{11}
\]
are smooth surfaces. The first identifies canonically with the conormal
incidence normalization via
\[
(p,H)\longmapsto(2p,\ H|_C-2p),
\]
since hyperplanes containing \(T_pC\) are exactly sections vanishing
along \(2p\). This uses conormal **covectors**, not ambient normal
vectors. Their classes are \([N_1]=2H_1\), \([N_2]=2H_2\).

Their scheme intersection is the ordered contact curve
\[
(2p,2q),\qquad2p+2q\in\mathbf P(V).
\tag{12}
\]
Writing finite parameters \(u,v\), its equation is
\(u^2+4uv+v^2=0\). Thus it is the union of the two bitangent graph
components with multipliers \(-2\pm\sqrt3\), meeting transversely as
curves at the two endpoint pairs. This is the ordered two-valued
bitangent relation; the fixed conic (6) instead records a single degree-two
divisor \(p+q\) paired with **itself**. The two constructions have the
same bitangent hyperplane image, but different markings and maps.

A further scheme distinction is visible without selecting coordinates on
\(N_1\). Its intersection with the swap-fixed conic is
\[
N_1\cap\operatorname{Fix}(\tau)
=\{(2p,2p):4p\in\mathbf P(V)\}.
\]
This is exactly the fourth-contact jet locus. Pulling back
\(z(h^2)\) by \(h=(t-us)^2\) gives \(6u^2\), with the
symmetric expression at infinity. Its two endpoint components have
length two each. This agrees with the fourth-contact divisor
\(2p_0+2p_\infty\); it is not the reduced intersection of the
quadric-tangent and osculating sections on the conormal surface.

The osculating section of \(N_1\) consists of
\[
(2p,\ p+\iota(p)),\qquad\iota(u)=-u,
\]
because \(H_p|_C=3p+\iota(p)\). Swap carries it to
\((p+\iota(p),2p)\). The ambient central involution \(\iota\)
acts simultaneously on both divisors and fixes a different set of flags;
it does not implement this exchange. The bitangent relation has two
partners, the osculating map has one, and residual swap acts on a
threefold of marked factorizations. They are naturally related through
(7), (11), and (12), without being identified.

## 7. One line in the divisor plane gives both cubic scrolls

The line \(L_\iota=V(\beta)\subset P\) consists of the unordered
osculating pairs \(p+\iota(p)\), including the doubled endpoint limits.
Its secants sweep the given primal cubic \(R\). The same line defines
an intrinsic smooth surface in the flag:
\[
M_\iota=\operatorname{pr}_1^{-1}(L_\iota)\subset\mathcal I.
\]
On this line, equation (3) is \(\alpha C+\gamma A=0\). Its
rank-two kernel over \(\mathbf P^1\) is
\(\mathcal O\oplus\mathcal O(-1)\), so
\(M_\iota\simeq\mathbb F_1\). It parametrizes every plane through
every osculating-pair secant, with that secant retained as a marking.

Its image under \(f\) is the dual of the primal cubic. Indeed on the
ruling chart of \(R\), write a point as
\([a:b:zb:z^2a]\). Off the singular directrix its tangent plane is
\[
[z^2b:-2z^2a:2za:-b].
\]
For a fixed nonzero finite \(z\), as \([a:b]\) varies these planes
fill densely the pencil through that ruling. Taking closures proves
\(f(M_\iota)=R^\vee\). This uses the characteristic-zero nonzero
coefficient 2; it is not valid without modification in characteristic two.
A general quartic in this image has exactly one even quadratic factor,
so the restriction of the finite map \(f\) is birational. Since
\(M_\iota\) is smooth, it is the finite normalization of \(R^\vee\).
The degree is
\[
(H_1+H_2)^2\cdot H_1\big|_{\mathcal I}=3.
\]
For a coordinate verification, write an even quadratic as
\(v^2-z\), with residual factor \(zA+Bv+Av^2\). Its product has
four marked coefficients \([-z^2A:-zB:B:A]\), which satisfy
\[
a_0a_2^2+a_1^2a_3=0.
\]
The dual is thus another cubic ruled surface, with this sign determined
by the conormal pairing convention. The proof via pencils identifies the
image intrinsically; the polynomial identity verifies its equation.

The two constructions from \(L_\iota\) retain different flags:
projectivizing points of its secant lines gives the normalization of the
primal \(R\), whereas projectivizing planes through those lines gives
\(M_\iota\), the normalization of \(R^\vee\). The Gauss map compares
them rationally; an abstract identification of their copies of
\(\mathbb F_1\) does not prove that this rational map extends everywhere.
In the flag, \(N_1\cap M_\iota\) consists scheme-theoretically of the
two full endpoint pencil fibers. Indeed \(\mathcal D\cap L_\iota\)
is the two reduced endpoint double divisors in characteristic zero.
In contrast, \(N_2\cap M_\iota\) is exactly the swapped osculating
curve \((p+\iota(p),2p)\), scheme-theoretically. In the same finite
chart, the condition that the residual factor be \((v-p)^2\) is
\(z=p^2\), and its homogeneous closure is a smooth bisection over
\(L_\iota\). This curve maps to the osculating quartic. Thus the
osculating image shared by the full dual surfaces is lifted by different
factor markings: on \(N_1\) one retains the double contact, while on
\(M_\iota\) one retains the osculating pair. The two descriptions are
exchanged by residual swap.

## 8. The full embedded automorphism group and all fixed loci

Retain from the independently audited
[projection/group note](2026-10-24-quartic-projection-automorphisms.md)
that \(G=\operatorname{Aut}(\mathbf P^3,C)=\mathbf G_m\rtimes\mathbf Z/2\).
On the divisor plane its generators are
\[
t_\lambda[\alpha:\beta:\gamma]=[\lambda^2\alpha:\lambda\beta:\gamma],
\qquad
r_a[\alpha:\beta:\gamma]=[a^2\gamma:a\beta:\alpha],
\quad r_a(u)=a/u.
\]
Their simultaneous actions on the factors obey
\(b_z(t_\lambda x,t_\lambda y)=\lambda^2b_z(x,y)\) and
\(b_z(r_ax,r_ay)=a^2b_z(x,y)\), hence preserve \(\mathcal I\), its
contact distribution, \(f\), and all the natural constructions above
in the equivariant sense. They commute with \(\tau\). Both the bitangent
and osculating correspondences are \(G\)-invariant; choosing one bitangent
multiplier breaks endpoint-exchange symmetry.

Here is a complete scheme-theoretic fixed-locus classification on the
flag threefold. Put \(e_0=[1:0:0]\), \(m=e_1=[0:1:0]\),
\(e_2=[0:0:1]\), and \(L=V(\beta)\).

| Element or subgroup | Fixed scheme on \(\mathcal I\) |
| --- | --- |
| Identity | \(\mathcal I\) |
| \(t_\lambda\), \(\lambda\ne\pm1\) | Six reduced \((e_i,e_j)\), omitting \((e_0,e_2),(m,m),(e_2,e_0)\) |
| Full torus | The same six reduced points |
| Central involution \(t_{-1}=\iota\) | Three disjoint smooth projective lines |
| Any reflection \(r_a\) | Three disjoint smooth projective lines |
| Full group \(G\) | Empty |
| Residual swap \(\tau\) | Smooth diagonal bitangent conic (6) |

For \(t_{-1}\) the three components are the orthogonality graph in
\(L\times L\), and \(L\times\{m\}\), \(\{m\}\times L\).
The graph is \([\alpha:0:\gamma]\mapsto[\alpha:0:-\gamma]\).
For \(r_a\) use the orthogonal eigenspaces
\[
E_+=\{\alpha=a\gamma\},\qquad E_-=k(-a,0,1).
\]
The three components are the orthogonality graph in
\(\mathbf P(E_+)^2\), together with
\(\mathbf P(E_+)\times\mathbf P(E_-)\) and its reverse.
The restrictions of \(b_z\) to both eigenspaces are nondegenerate, so
these components are smooth and disjoint. For a general torus element
all three eigenvalues are distinct, and direct substitution gives the
six indicated pairs. The only point of \(P\) fixed by all of \(G\)
is \(m\), but \((m,m)\notin\mathcal I\). Semisimplicity in
characteristic zero gives reduced eigenspace equalizers; the bilinear
restrictions just described establish the stated scheme structures.
These fixed-locus claims were independently reconstructed by the focused
reviewer `flag_fixed_loci` during this investigation.

The invariant surfaces \(N_1\) and \(M_\iota\) inherit the action,
and their fixed schemes can be read without choosing a product
trivialization. Every nonidentity torus element and every reflection has
four reduced fixed points on \(N_1\): intersect the first-factor fixed
locus with the doubled-divisor conic \(\mathcal D\). There is no
\(G\)-fixed point. On \(M_\iota\), a torus element other than
\(1,-1\) has four reduced fixed points. The central involution fixes
two disjoint projective lines: the orthogonality graph in \(L^2\) and
\(L\times\{m\}\). For \(r_a\), put
\(x_+=[a:0:1]\), \(x_-=[-a:0:1]\). Its fixed scheme on
\(M_\iota\) is the disjoint union
\[
\{x_-\}\times\mathbf P(E_+),\qquad
\{(x_+,m)\},\qquad\{(x_+,x_-)\}.
\]
The restrictions are reduced: \(\mathcal D\) meets the relevant fixed
lines transversely, and \(L\cap\mathbf P(E_+)\) is the reduced point
\(x_+\). The full group again has no fixed point. The two projections,
the factorization map, the secant maps, the normalization maps, and the
Gauss correspondence remain equivariant; an equivariant map can identify
several fixed or nonfixed markings downstairs, so these fixed schemes
are statements on the specified smooth marked models.

For completeness, every combined action has the uniform equalizer
\[
\operatorname{Fix}(\tau g)\simeq
\{x\in\operatorname{Fix}_P(g^2):b_z(x,gx)=0\},
\quad x\longmapsto(x,gx).
\tag{13}
\]
For \(g=t_{-1}\) this is the smooth conic
\(2\alpha\gamma-\beta^2=0\), graphed by \(t_{-1}\);
for \(\lambda^2=-1\) it is the graph over \(L\); for other
\(\lambda\notin\{1,-1\}\) it is two reduced endpoint flags.
For a reflection it is the graph over the smooth conic
\(\alpha^2+a\beta^2+a^2\gamma^2=0\). These different fixed
subvarieties give a concrete scheme-level distinction between residual
swap and the osculating action, even though they commute.

## 9. Verification and remaining review boundary

The companion
[scoped verifier](../computations/verify_quartic_flag_incidence_2026_10_24.py)
checks only the new bilinear, resultant/Jacobian, quadruple-root fiber,
contact, and group formulas, and explicitly labelled characteristic-two
boundary identities for the synthesis. It does not rerun inherited group, conormal,
or secant proofs. Its output is
[recorded separately](../computations/quartic_flag_incidence_2026_10_24.json).
The intrinsic arguments above establish globality and completeness;
finite symbolic checks alone do not do so. No new canonical record or
frontier exclusion is proposed. The smooth flag identification and these
maps answer the fixed-embedding questions in this note; varying the
projection center or classifying analytic singularities of the secant
image are outside its claims.
