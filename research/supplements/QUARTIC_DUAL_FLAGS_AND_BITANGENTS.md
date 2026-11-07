# Divisor flags, secants and bitangent correspondences

The fixed marked system is \(C=[s^4:s^3t:st^3:t^4]\), over an algebraically closed characteristic-zero field unless a characteristic is explicitly changed. The missing middle coefficient of a product of quadratic divisors defines the common flag. Addition of effective divisors, secant normalization and the unordered pair-partition cover have different degrees and different fixed loci. This chapter owns their full proofs, including nonreduced boundary fibers; the [dual singular schemes](QUARTIC_DUAL_SCHEMES.md) and [conormal contact schemes](QUARTIC_CONORMAL_AND_CONTACT.md) use them.

The need to retain degree-two divisor parameters rather than just secant lines has the same geometric source as the disconnected trisecant fibers in Kohn–Nødland–Tripoli, *Secants, Bitangents, and Their Congruences*, §7, Proposition 7.1. The specific exceptional fibers and endpoint schemes below are proved directly for this marked quartic; the general congruence statement is context, not a substitute for those calculations. [Primary text](https://arxiv.org/pdf/1701.03711).

<a id="quartic-flag-incidence"></a>

## The residual-pair flag and all factorization fibers

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
[symmetric-square note, Section 2](#quartic-symmetric-square-bitangents):
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
[projection/group note](QUARTIC_PROJECTION_AND_SPECIAL_GEOMETRY.md#quartic-projection-automorphisms)
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
finite symbolic checks alone do not do so. No new
frontier exclusion is proposed. The smooth flag identification and these
maps answer the fixed-embedding questions in this note; varying the
projection center or classifying analytic singularities of the secant
image are outside its claims.



---


<a id="quartic-symmetric-square-bitangents"></a>

## Symmetric square, secants and multiplier correspondences

## 1. Degree-two divisors and the diagonal

Put $U=H^0(\mathbf P^1,\mathcal O(2))$. Sending a nonzero section to its
zero divisor gives

\[
\operatorname{Sym}^2 C=|\mathcal O(2)|=\mathbf P(U)\simeq\mathbf P^2.
\]

Here $\mathbf P(U)$ means lines of sections, so the represented point is

\[
[h]=[\alpha:\beta:\gamma],\qquad
h=\alpha s^2+\beta st+\gamma t^2.
\]

This use of $\mathbf P(U)$ parametrizes divisors; the ambient space of
the quartic embedding is instead $\mathbf P(V^\vee)$. If $u=t/s$ and
$p=c(u),q=c(v)$ are finite, then

\[
[\alpha:\beta:\gamma]=[uv:-(u+v):1].
\tag{1.1}
\]

The diagonal divisor of nonreduced pairs is the smooth conic

\[
\mathcal D:\quad d=\beta^2-4\alpha\gamma=0.
\tag{1.2}
\]

The two endpoint divisors are $2p_0=[0:0:1]$, $2p_\infty=[1:0:0]$,
where $p_0=c(0)$ and $p_\infty=c(\infty)$.
The action of $\operatorname{PGL}_2$ on degree-two divisors is its
symmetric-square action on this plane; $\mathcal D$ is invariant.
The subgroup preserving the embedded quartic is the normalizer of the
torus fixing the unordered pair $\{p_0,p_\infty\}$. Its generators act by

\[
u\mapsto\lambda u:
[\alpha:\beta:\gamma]\mapsto
[\lambda^2\alpha:\lambda\beta:\gamma],
\qquad
u\mapsto 1/u:
[\alpha:\beta:\gamma]\mapsto[\gamma:\beta:\alpha].
\tag{1.3}
\]

The weights depend on the choice of lift to $\operatorname{GL}(U)$,
while the projective action does not.

## 2. Secants give a morphism, but forget a pair on trisecants

The evaluation map $V\otimes\mathcal O\to\mathcal O_Z(4)$ has rank two
for every length-two divisor $Z=p+q$, including $Z=2p$, since the
quartic parametrization is an embedding. Its dual gives a two-dimensional
subspace of $V^\vee$. Hence

\[
\sigma:\operatorname{Sym}^2 C\longrightarrow\operatorname{Gr}(2,V^\vee),
\quad p+q\longmapsto\langle c(p),c(q)\rangle
\tag{2.1}
\]

is a morphism everywhere, with $\sigma(2p)=T_pC$. Equivalently, use the
universal length-two divisor on $C\times\operatorname{Sym}^2 C$ and its
rank-two tautological evaluation bundle.

An explicit independent check is useful. Put $a=u+v,b=uv$. Dividing
$c(u)\wedge c(v)$ by $v-u$, in Plücker order $01,02,03,12,13,23$, gives

\[
\sigma(a,b)=
[1,a^2-b,a^3-2ab,ab,b(a^2-b),b^3].
\tag{2.2}
\]

The divided difference extends to $u=v$ and gives $c(u)\wedge c'(u)$.
Globally the six coordinates are

\[
[\gamma^3,\ \gamma(\beta^2-\alpha\gamma),\
-\beta^3+2\alpha\beta\gamma,\ -\alpha\beta\gamma,\
\alpha(\beta^2-\alpha\gamma),\ \alpha^3].
\tag{2.3}
\]

There is no basepoint: the first and last coordinates force
$\alpha=\gamma=0$, when the third is nonzero. In particular
$\sigma^*\mathcal O_{\operatorname{Gr}}(1)=\mathcal O_{\mathbf P^2}(3)$.

The quadratic monomials in the four coordinates have exactly one linear
relation, $x_0x_3=x_1x_2$; their exponents are
$0,1,2,3,4,4,5,6,7,8$. Thus the containing quadric is uniquely

\[
Q=V(x_0x_3-x_1x_2).
\]

Under its Segre presentation
$x=(ac,ad,bc,bd)$, the curve is the graph
$[c:d]=[s:t]\mapsto[a:b]=[s^3:t^3]$. A line outside $Q$ meets $C$
in length at most two, because its nonzero quadratic restriction vanishes
on that section. A line on $Q$ is a ruling, with section length one or
three. The length-three sections are fibers of $u\mapsto u^3$: three
distinct points away from the endpoints, and $3p_0,3p_\infty$ at them.
There is no section of partition $[2,1]$.

It follows that a general secant retains its unordered contact pair
uniquely. An ordinary trisecant forgets which two of its three points
were selected. In fact the entire trisecant preimage is the smooth conic

\[
\mathcal T:\quad\beta^2-\alpha\gamma=0.
\tag{2.4}
\]

On the finite chart, $b=a^2$; its map to the ruling conic is
$\kappa=-a^3$. More precisely, for

\[
L_\kappa=V(x_2-\kappa x_0,x_3-\kappa x_1),
\]

the scheme fiber in this chart is

\[
\sigma^{-1}(L_\kappa)=V(b-a^2,a^3+\kappa).
\tag{2.5}
\]

For $\kappa\ne0$ this is three reduced points. For $\kappa=0$ it is
one point with curvilinear length three; reversing parameters gives the
other endpoint. Thus the tangent trisecant is associated to a unique
underlying doubled pair, but the secant morphism retains a nonreduced
fiber at it.

Every line meets $C$ in a finite divisor, which has finitely many
length-two subdivisors. The proper morphism $\sigma$ is consequently
quasi-finite, hence finite, and is birational onto its image. Therefore
$\mathbf P^2\simeq\operatorname{Sym}^2 C$ is the normalization of the
secant surface in the Grassmannian. Its Plücker degree is $9=(3H)^2$.
The surface is nonnormal along the trisecant ruling conic, with three
normalization points over a general ruling line.

There is also an infinitesimal loss of information at the endpoints.
The Jacobian of (2.2) has rank two except at $a=b=0$, where it has rank
one. For example two minors are $-(a^2+2b)$ and $2a^2+b$; their
simultaneous vanishing forces $a=b=0$. Reversal handles infinity.
For a distinct pair involving infinity, the two endpoint motions are
independent unless one tangent line is the secant, which would give the
excluded partition $[2,1]$. The killed direction at either endpoint is
the tangent direction to $\mathcal T$. No particular analytic
singularity type of the image is asserted.

These secant formulas and fiber calculations were independently
reconstructed by the subsidiary reviewer `secant_audit`; computational
identities are included in the package verifier.

## 3. Doubling, the projection center, and the bitangent conic

Let $z\in W^\vee\setminus\{0\}$ annihilate $V$, determined up to
scalar. Thus $z(f)$ extracts the coefficient of $s^2t^2$. The map

\[
\delta:\mathbf P(U)\longrightarrow\mathbf P(W),\qquad[h]\mapsto[h^2]
\tag{3.1}
\]

represents doubling $p+q\mapsto2p+2q$. The relevant locus is the
pullback of the hyperplane $\mathbf P(V)\subset\mathbf P(W)$:

\[
\mathcal B=V(q_z),\qquad q_z(h)=z(h^2)=\beta^2+2\alpha\gamma.
\tag{3.2}
\]

This definition uses the same intrinsic datum $z$ as the projection
center in $\mathbf P(W^\vee)$. It is not merely a coordinate test for
contact. Its gradient $(2\gamma,2\beta,2\alpha)$ never vanishes at a
projective point, so $\mathcal B$ is a smooth conic. Every nonendpoint
member gives a unique plane section $2p+2q$, with $p\ne q$, and hence
a bitangent plane. At an endpoint it gives $4p_0$ or $4p_\infty$, the
hyperosculating plane section.

The scheme intersection with the diagonal is

\[
I(\mathcal B\cap\mathcal D)
=(\beta^2+2\alpha\gamma,\beta^2-4\alpha\gamma)
=(\beta^2,\alpha\gamma).
\tag{3.3}
\]

On $\gamma=1$ this is $(\alpha,\beta^2)$, of length two; on
$\alpha=1$ it is $(\gamma,\beta^2)$, also of length two. Thus these
are precisely the two tangent intersections, not four distinct points.
Both conics have tangent $\alpha=0$ at $2p_0$ and $\gamma=0$ at
$2p_\infty$.

Squaring maps $\mathcal B$ to the curve of bitangent planes in
$\mathbf P(V)$, the dual ambient space. This map is a closed immersion:
in characteristic zero, $h^2\propto k^2$ forces $h\propto k$, and the
differential $k\mapsto2hk\bmod h^2$ is injective modulo $h$.
The same square-polynomial argument applies over every field extension,
so the map is universally injective; it is also unramified and proper,
which gives the closed immersion. Its pullback hyperplane bundle is
$\mathcal O_{\mathcal B}(2)=\mathcal O_{\mathbf P^1}(4)$, so the image
is a smooth rational quartic. Using $w=u+v$, it is

\[
[w^4/4:w^3:-2w:1],
\quad (s,t)\text{-section }(t^2-wst-w^2s^2/2)^2.
\tag{3.4}
\]

The endpoint members agree with the limiting osculating planes. The full
pencils of endpoint triple-contact planes are different families; their
existence does not enlarge $\mathcal B$.

## 4. The number $-4$: a cross-ratio and a trace-free conic

The automorphism action and tangency data first leave a pencil. Every
conic

\[
\mathcal B_\lambda:\quad\beta^2+\lambda\alpha\gamma=0
\tag{4.1}
\]

is invariant under (1.3). For $\lambda\ne0,-4$ it is smooth, distinct
from $\mathcal D$, and tangent to $\mathcal D$ at the same two points.
Thus invariance and the intersection scheme alone do not single out
$\lambda=2$. The trisecant conic is the member $\lambda=-1$.

There is, however, a canonical additional *condition*, requiring no
independent geometric datum beyond the diagonal conic: take the
trace-free representative relative to its polar form. The discriminant
form $d$ has matrix

\[
D=\begin{pmatrix}0&0&-2\\0&1&0\\-2&0&0\end{pmatrix},
\qquad
B_\lambda=\begin{pmatrix}0&0&\lambda/2\\0&1&0\\\lambda/2&0&0\end{pmatrix}.
\]

The condition

\[
\operatorname{tr}(D^{-1}B_\lambda)=1-\lambda/2=0
\tag{4.2}
\]

is unaffected by scaling either equation or changing projective
coordinates. It selects exactly $\lambda=2$ among this invariant
pencil. Consequently the group action together with the diagonal does
recover the bitangent conic uniquely **if** this canonical trace-free
construction is included; bare invariance and tangency do not.

The reason for trace-freeness is the quartic linear system, not a
numerical coincidence. Multiplication gives an equivariant surjection

\[
m:\operatorname{Sym}^2 U\longrightarrow W.
\tag{4.3}
\]

Its one-dimensional kernel is generated, using symmetric-tensor notation,
by $(s^2)\mathbin\odot(t^2)-(st)\mathbin\odot(st)$. This is a nonzero
multiple of the inverse discriminant tensor $D^{-1}\in\operatorname{Sym}^2 U$.
Dualizing identifies $W^\vee$ with the five-dimensional hyperplane
of quadratic forms $q$ on $U$ satisfying

\[
\operatorname{tr}(D^{-1}Q)=0,
\tag{4.4}
\]

where $Q$ is the matrix of $q$. For a general functional
$z=(z_0,\ldots,z_4)$, the image is explicitly

\[
q_z=z_0\alpha^2+2z_1\alpha\beta+
 z_2(\beta^2+2\alpha\gamma)+2z_3\beta\gamma+z_4\gamma^2,
\]

which verifies (4.4) directly. Thus the projection center determines the
normalizer-invariant trace-free conic, and conversely $q_z$ determines
$z$. This is the degree-four component of the usual decomposition
$\operatorname{Sym}^2(\operatorname{Sym}^2 k^2)=\operatorname{Sym}^4 k^2\oplus k$,
with determinant twists suppressed projectively.

One can also recover an invariant of the *pair* of conics. The
endomorphism $D^{-1}B_\lambda$ has a simple eigenvalue $1$ and a double
eigenvalue $-\lambda/4$. Their ratio is invariant under simultaneous
projective transformations and independent equation rescaling. For
$\mathcal B$ that ratio is $-2$. Hence its relative position to the
diagonal carries more information than the common tangency scheme.
The pencil spanned by the two conics has singular members $\alpha\gamma=0$
and the double line $\beta^2=0$; the unordered endpoints and the
osculating-pair line appear in that pencil as well.

For a nonendpoint pair $p=c(u),q=c(v)$, substitution of (1.1) in
(4.1) gives

\[
u^2+(2+\lambda)uv+v^2=0.
\]

The cross-ratio of the four naturally marked points
$p_0,p_\infty,p,q$ is $u/v$, using
$[a,b;c,d]=(c-a)(d-b)/((c-b)(d-a))$. Reversing either unordered pair
inverts it. Thus the unordered pair

\[
\{r,r^{-1}\},\qquad r=v/u,
\]

and its sum are intrinsic. For our trace-free conic,

\[
r+r^{-1}=-4,\qquad
\{r,r^{-1}\}=\{-2+\sqrt3,-2-\sqrt3\}.
\tag{4.5}
\]

This supplies a genuine coordinate-free cross-ratio interpretation;
there is no canonical choice between the two roots. Merely naming the
torus weights would not explain the number: the trace-free condition
coming from multiplication is what forces it. Ordinary intersection
numbers of the two conics alone only give total intersection length
four, shared by all members (4.1), and cannot recover $-4$.

## 5. Ordered correspondences, intersections, and composition

Write $\rho=-2+\sqrt3$, with either choice of the square root, and let
$\Gamma_a\subset C\times C$ be the graph of $u\mapsto au$, for
$a\in k^\times$. The osculating residual involution and the ordered
bitangent correspondence are

\[
\mathcal I=\Gamma_{-1},\qquad
\mathcal R=\Gamma_\rho\cup\Gamma_{\rho^{-1}}.
\tag{5.1}
\]

The latter is a reduced divisor of bidegree $(2,2)$, with affine equation

\[
R(u,v)=v^2+4uv+u^2=0.
\tag{5.2}
\]

Its two components are individually graphs of automorphisms, but their
union supplies two partners to a general point and is not an involution.
The first projection is finite flat of degree two; its fiber over either
endpoint is a doubled point, even though the total correspondence is
reduced.

Under simultaneous automorphism action on the two factors, a torus
element preserves each $\Gamma_a$; inversion exchanges
$\Gamma_a\leftrightarrow\Gamma_{a^{-1}}$. Thus $\mathcal R$ and
$\mathcal I$ are invariant under the full embedded automorphism group.
The two bitangent components cannot be canonically ordered. Since
$-1=(-1)^{-1}$, the osculating involution commutes with the full group.

If $a\ne b$, then $\Gamma_a\cap\Gamma_b$ consists of
$(p_0,p_0),(p_\infty,p_\infty)$, with length one at each. Locally the
equations are $v-au,v-bu$, so this is a transverse intersection.
This applies to either bitangent graph versus the diagonal and to the
two bitangent graphs versus one another. Accordingly $\mathcal R$
has ordinary nodes at the two endpoints. For its intersection with the
diagonal, however, both branches contribute:

\[
I(\mathcal R\cap\Delta)=(v-u,6u^2)
\quad\text{near }(0,0).
\tag{5.3}
\]

It has length two there and likewise at infinity. The fixed *set* of the
two-valued relation is exactly the endpoints, with this nonreduced fixed
scheme. Each individual graph has the two reduced fixed points.
Similarly $\mathcal I\cap\mathcal R$ has length two at each endpoint,
whereas $\mathcal I\cap\Delta$ has length one at each.

For cycles of correspondences, graph composition is group multiplication:

\[
\Gamma_a\circ\Gamma_b=\Gamma_{ab},\quad
\mathcal I^2=\Delta,\quad
\mathcal I\circ\mathcal R=\Gamma_{-\rho}+\Gamma_{-\rho^{-1}},
\]

\[
\mathcal R\circ\mathcal R
=\Gamma_{\rho^2}+2\Delta+\Gamma_{\rho^{-2}}.
\tag{5.4}
\]

The multiplicity two records the two paths returning to the starting
point. The scheme-theoretic image of the fiber-product composition has
instead the reduced union of these three graphs. In the finite chart its
ideal is generated by

\[
(w-u)(w^2-14uw+u^2),
\tag{5.5}
\]

whereas the resultant of $R(u,v),R(v,w)$ is
$(w-u)^2(w^2-14uw+u^2)$. Thus the resultant retains the path multiplicity
and is not the ideal of that scheme image.

For completeness, the fiber product itself is reduced. It is finite
flat over $u$ of degree four, and its generic fiber is reduced: the two
choices for $v/u$, followed by the two choices for $w/v$, give four
distinct points in the $(v,w)$-fiber, including two points with the same
$w=u$ but different $v$. A nilpotent would vanish generically and
would be $k[u]$-torsion, impossible in a flat module. Its scheme image
is therefore reduced; its support is exactly the three graphs, proving
(5.5) without confusing elimination with the resultant.

The same argument gives, as cycles,

\[
\mathcal R^{\circ n}
=\sum_{j=0}^{n}\binom nj\Gamma_{\rho^{n-2j}},
\tag{5.6}
\]

and as a scheme image the reduced union of the $n+1$ distinct graphs.
The source chain is finite flat of degree $2^n$ over the first point
and generically reduced, which again proves its reducedness.
For even $n$, the diagonal is one component, so these iterated
relations fix every point along one possible return path. The statement
that only the endpoints are fixed concerns the original nontrivial
graphs and relation, not all iterates.

The number $\rho$ has infinite multiplicative order. Indeed in a real
embedding of $\mathbf Q(\sqrt3)$, one root has absolute value strictly
between zero and one, precluding a root of unity or a power equal to
$-1$. Consequently

\[
\langle\rho,-1\rangle\simeq\mathbf Z\times\mathbf Z/2
\subset\mathbf G_m.
\tag{5.7}
\]

Its useful geometric meaning is the group of possible moves generated
by repeated bitangent choices and the osculating involution. It is
Zariski dense in the torus. Every nonendpoint orbit is infinite and
Zariski dense in $C$, while the two endpoints are individually fixed.
No additional finite symmetry or canonical ordering of $\rho,\rho^{-1}$
is implied.

## 6. Passing to unordered pairs

Let $\pi:C\times C\to\operatorname{Sym}^2 C$ be the quotient by factor
exchange. The inverse image of $\mathcal B$ is exactly $\mathcal R$.
Factor exchange swaps its two components, and the restriction of either
one to $\mathcal B$ is an isomorphism:

\[
u\longmapsto[\rho u^2:-(1+\rho)u:1]
\tag{6.1}
\]

is a degree-two parametrization of the smooth conic. At the endpoints
the two components meet; the full map $\mathcal R\to\mathcal B$ is a
split nodal double cover. In a local parameter on $\mathcal B$, its
equation has the form $d^2=c t^2$, with $c\ne0$. Its fibers at the
two intersections with the diagonal are nonreduced. This is compatible
with the order-two tangency in (3.3); it is not a branched map on either
individual normalization component.

In contrast, the image of $\mathcal I$ is the line

\[
\mathcal L_{\mathrm{osc}}:\quad\beta=0,
\]

parametrizing pairs $p+\iota(p)$. The map
$\Gamma_{-1}\simeq C\to\mathcal L_{\mathrm{osc}}$ is the degree-two
quotient by the involution, branched at $p_0,p_\infty$. Thus the
osculating-pair line and the bitangent conic have different quotient
behavior. The line is also the repeated member of the conic pencil in
Section 4.

For any $a\ne\pm1$, the unordered image of $\Gamma_a$ is a smooth
conic and equals the image of $\Gamma_{a^{-1}}$, with equation

\[
\beta^2-\frac{(1+a)^2}{a}\alpha\gamma=0.
\tag{6.2}
\]

For $a=1$ it is the diagonal conic, traversed isomorphically; for
$a=-1$ it degenerates to the line just described, traversed twice.
The ordered correspondence composition lives on $C\times C$;
forgetting order retains which unordered pairs occur, but loses both
orientation and the path multiplicities in (5.4) and (5.6).

The endpoint pair is recovered in several compatible ways: the reduced
support of $\mathcal B\cap\mathcal D$, the common degenerations of the
two bitangent graphs, the fixed points of $\iota$, and the rank-drop
points of the secant morphism on the diagonal. The constructions are
consequences of one incomplete quartic linear system, with the
multiplication map explaining the numerical invariant.


## Characteristic reach and mathematical status

The bilinear pairing has determinant \(-1\), so the incidence remains the smooth complete flag variety in every characteristic; finite-flat divisor addition and its multiplicity-partition fiber lengths are characteristic free. The swap fixed conic becomes a doubled line in characteristic two, while the ambient flag remains smooth. The characteristic-zero contact/Legendrian interpretation uses the displayed differential and symplectic forms and is not asserted unchanged in small characteristic. Multiplier arithmetic, including its finite-flat non-subgroup scheme and characteristic-two degeneration, is proved in [the arithmetic four-section chapter](ARITHMETIC_FOUR_SECTION_FAMILY.md). Secant-line injectivity fails on trisecants even in characteristic zero; divisor parameters must be retained. These exact marked statements support [R-0026](../results/quartic_flag_conormal_geometry.md) without classifying arbitrary pairs.
