# Symmetric square, bitangent conic, and correspondences of the fixed rational quartic

Date: 2026-10-24. Status: **independently audited exploratory arguments;
not canonically promoted**. No STCI consequence is
claimed. Throughout, $k$ is algebraically closed of characteristic zero,
$C\simeq\mathbf P^1$, and

\[
c([s:t])=[s^4:s^3t:st^3:t^4],\qquad
W=H^0(\mathbf P^1,\mathcal O(4)),\quad
V=\langle s^4,s^3t,st^3,t^4\rangle.
\]

This note reconstructs the symmetric-square statements needed from the
[special-lines investigation](2026-10-24-special-lines-planes-research-note.md)
and its [independent geometry audit](2026-10-24-special-lines-planes-geometry-audit.md).
The arguments depend only on the displayed embedding and its unique
smooth containing quadric, whose elementary derivation is recalled below.
They do not use the accepted normal-bundle splitting, quartic-carrier
exclusions, or any proposed STCI obstruction. For projection and group
conventions see the companion [projection note](2026-10-24-quartic-projection-automorphisms.md).
No literature-priority claim is made.

The [independent audit](2026-10-24-quartic-symmetric-independent-audit.md)
reconstructs the arguments, including endpoint schemes and correspondence
composition, and records the final review boundary.

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

## 7. Scope and continuation

All statements above concern this fixed embedding in characteristic
zero. The proof mechanisms are evaluation on length-two divisors,
multiplication of binary quadratics, the discriminant polar form, and
graph composition. They are mathematical arguments, supplemented by
exact computations; the computations do not establish novelty or
canonical promotion. The secant image's precise analytic singularity
type at the endpoint tangent trisecants is not determined here and is
not needed for the stated normalization, fiber, or differential claims.
