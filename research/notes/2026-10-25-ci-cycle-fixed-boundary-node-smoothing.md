# Five residual nodes can move independently to first order at fixed boundary

Date: 2026-10-25. Status: exploratory exact tangent calculation with independent reconstruction; no canonical promotion. The [independent review](2026-10-25-ci-cycle-fixed-boundary-node-smoothing-audit.md) records the finite calculation and its local-deformation interpretation separately. The starting point is the line-plus-degree-eleven degeneration in the [line-degeneration note](2026-10-25-ci-cycle-line-degeneration.md). The main question is whether a fixed attachment divisor on \(C\) can hide changes in the genus and component structure of the residual curve.

**Finite result.** At this actual quartic pencil, the full boundary map has projective differential rank 18, and the map from its 14-dimensional fixed-boundary tangent space to the five residual node parameters is surjective. Its kernel has dimension 9. Thus retaining the exact boundary to first order does not force any linear relation among the five node smoothing parameters. A separate formal interpretation is given below; no explicit polynomial arc with exactly constant boundary has been constructed by this calculation.

## 1. The actual point and the two separate boundaries

Use the homogeneous forms \(F,G,Q,A,D_3,H_0,H_1\) from the [smooth residual benchmark](2026-10-25-ci-cycle-smooth-residual-example.md), but take coefficients 1,1:

\[
f=F+QH_0+x_0A,\qquad
g=G+QH_1+x_3D_3.                             \tag{1}
\]

The residual cycle is \(L+E\), where

\[
L=V(x_0+x_1,x_2+x_3),\qquad
\deg E=11,\quad g(E)=12.
\]

The companion exact rational computation verifies that \(E\) is smooth and geometrically integral, \(L\cap E\) consists of five reduced points, \(C\cap E\) has seventeen reduced points, and \(C\cap L\) is one further reduced point, with no triple intersection. In particular the five nodes of \(L\cup E\) lie off \(C\). These are different from the eighteen attachment nodes of the full curve along \(C\).

The boundary-divisor map is

\[
\beta:U\subset\operatorname{Gr}(2,V)
\longrightarrow\mathbf P H^0(C,\mathcal O_{\mathbf P^1}(18)),
\qquad V=H^0(\mathbf P^3,I_C(4)),\quad \dim V=18.
\]

It is regular at this pencil because its first-normal determinant is nonzero. The determinant has degree 18 and is squarefree, so the eighteen attachments are simple. In this note, *fixed boundary* means the fiber of this actual map, not merely constant boundary degree. It fixes an effective divisor on the marked \(C\).

The five residual nodes are encoded on the chart \(x_3=1\) of \(L\) by

\[
[x_0:x_1:x_2:x_3]=[-r:r:-1:1],
\]

\[
P(r)=4r^5-2r^4+9r^3+2r^2+3r+2.               \tag{2}
\]

The finite étale algebra

\[
\mathcal A=\mathbf Q[r]/(P)
\]

records all five nodes without choosing their roots. The point \(L\cap C\) is \(r=-1\), and \(P(-1)=-14\), so none of the five nodes is that attachment point.

## 2. A node smoothing functional obtained from the actual gradients

Take normal coordinates \(n_0=x_0+x_1\), \(n_1=x_2+x_3\) along \(L\). On \(x_3=1\), the coefficients of \(n_1\) in the two first-normal parts are

\[
F_1(r)=-r(r+1)(r+2),\qquad
G_1(r)=-4r^3+2r^2-9r-1.
\]

The polynomial \(F_1\) is a unit in \(\mathcal A\): \(P\) is relatively prime to each of \(r,r+1,r+2\). Thus the first equation is a smooth carrier at every one of the five nodes. The actual gradients satisfy

\[
F_1\,\partial_jg-G_1\,\partial_jf=0
\quad\text{in }\mathcal A\quad(j=0,1,2,3).     \tag{3}
\]

For a global perturbation pair \(h,k\in V\), eliminating the first carrier equation shows that the first-order constant term in the node equation is

\[
k|_L-\frac{G_1}{F_1}h|_L.
\]

Equivalently, multiply by the invertible factor \(F_1\) and use the scaled class

\[
S(h,k)=F_1k|_L-G_1h|_L\pmod P\quad\in\mathcal A. \tag{4}
\]

This class is a node smoothing parameter up to multiplication by a nonzero factor at each geometric node. The scale cannot change a surjectivity statement. The script checks equation (3) from the actual homogeneous derivatives and separately verifies that the normal determinant along \(L\) equals \(-(r+1)P(r)\).

## 3. The source really consists of global homogeneous quartics

For a degree-four monomial \(x_0^{m_0}x_1^{m_1}x_2^{m_2}x_3^{m_3}\), restriction to \(C\) has parameter weight

\[
w=m_1+3m_2+4m_3.
\]

Group the thirty-five monomials by this weight. In each nonempty group, subtract one fixed reference monomial from the others. This gives an integral 18-element basis of the actual restriction kernel \(V\).

On \(x_0=1\), put \(u=x_1\), \(X=x_3-u^4\), \(Y=x_2-u^3\). A monomial's first-normal part is

\[
m_3u^{w-4}X+m_2u^{w-3}Y.
\]

The formula is used on each monomial difference. Write these two coefficients as \(\sigma_h=(A_h,B_h)\). The affine differential of the determinant at (1) is

\[
D(h,k)=\det(\sigma_h,\sigma_g)
       +\det(\sigma_f,\sigma_k)
\in H^0(\mathcal O_{\mathbf P^1}(18)).         \tag{5}
\]

Its target is represented by nineteen coefficients in \(u\). The node functional (4) is represented by five coefficients in the basis \(1,r,r^2,r^3,r^4\) of \(\mathcal A\). The combined matrix therefore has 24 rows and 36 columns over \(\mathbf Q\).

The [standard-library exact verifier](../computations/verify_ci_fixed_boundary_node_smoothing_2026_10_25.py) constructs these actual source forms, the carrier functional, and both matrices. It does not replace global sections by arbitrary rational-function-valued symbols.

## 4. The exact ranks and explicit tangent witnesses

Exact Gaussian elimination over \(\mathbf Q\) gives

\[
\boxed{\operatorname{rank}D=19,\qquad
       \operatorname{rank}S=5,\qquad
       \operatorname{rank}(D,S)=24.}          \tag{6}
\]

The final equality implies

\[
\operatorname{rank}\bigl(S|_{\ker D}\bigr)=24-19=5.
\]

The calculation also solves explicitly for five rational source vectors \(v_0,\ldots,v_4\in V^2\) satisfying

\[
D(v_i)=0,\qquad S(v_i)=r^i\pmod P
\quad(i=0,\ldots,4).                         \tag{7}
\]

Their 36 source coefficients are recorded in the [JSON evidence](../computations/ci_fixed_boundary_node_smoothing_2026_10_25.json), together with the global monomial basis, polynomial (2), matrix pivot columns, and all checked ranks. The script verifies every equality in (7) exactly. These are actual homogeneous first-order perturbations with zero affine boundary derivative.

The nodes need not be individually rational over \(\mathbf Q\). Equation(7) spans their étale algebra over \(\mathbf Q\). After extending to an algebraically closed field and splitting \(P\), evaluation identifies \(\mathcal A\otimes k\) with \(k^5\), so the five geometric node parameters are independent. Selecting only one geometric node may require coefficients in a splitting field; no assertion that all nodes are rational is made.

## 5. Passing from ordered equations to the Grassmannian

The source \(V^2\) has dimension 36, while the pencil space has dimension 32. Infinitesimal changes of basis of \(f,g\) form the four-dimensional \(\operatorname{GL}_2\) gauge space. At every node both \(f\) and \(g\) vanish, so all four gauge directions have zero node class.

Their boundary derivatives are scalar multiples of the base determinant; the trace directions span that scalar line. A direction whose projective boundary derivative vanishes can therefore be modified by a gauge direction to make its affine boundary derivative exactly zero, without changing its node smoothing class. Consequently (6) gives the intrinsic pencil-space statement

\[
\operatorname{rank}d\beta=18,\qquad
\dim\ker d\beta=32-18=14,
\]

\[
\operatorname{rank}\bigl(S|_{\ker d\beta}\bigr)=5,
\qquad \dim(\ker d\beta\cap\ker S)=9.          \tag{8}
\]

The projective scaling issue does not remove one of the node parameters or manufacture an extra smoothing direction.

## 6. Formal interpretation, kept separate from the finite matrix result

There is a useful standard local consequence after extending scalars to split and mark the five nodes. The parameter space of pencils is smooth, and the surjective boundary differential makes the completed fixed-boundary fiber a smooth formal space of dimension 14.

For a split node in a flat family, [Stacks, Lemma 53.20.11](https://stacks.math.columbia.edu/tag/0CBX) gives a completed equation \(xy-\tau_i=0\), with \(\tau_i\) a function of the formal base parameters. Its first differential is the node class (4), up to a unit. The étale local counterpart is [Stacks, Lemma 53.21.1](https://stacks.math.columbia.edu/tag/0CBY).

On the completed fixed-boundary fiber, the five linear forms \(d\tau_i\) are independent by (8). Formal coordinates can therefore be chosen so that its complete local ring is

\[
k[[\tau_1,\ldots,\tau_5,z_1,\ldots,z_9]].     \tag{9}
\]

In this formal sense the five residual nodes can be smoothed independently while the boundary divisor is held exactly fixed. This conclusion uses the standard node local form and the formal inverse-function argument in addition to the finite rank computation.

The étale node charts also give a local algebraic existence interpretation. After a common étale base change that labels the nodes, the five node parameters are regular functions. The joint map \((\beta,\tau_1,\ldots,\tau_5)\) has surjective differential, so its restriction to the fixed-boundary fiber maps smoothly to \(\mathbf A^5\) near the marked point. A chosen one-parameter pattern \(\tau_i=c_i t\) therefore lifts locally after an étale change of the one-parameter base; a zero \(c_i\) retains that node, and a nonzero \(c_i\) smooths it in the generic fiber. This is an existence statement for local algebraic families, derived from smoothness and the node charts. It does not display their coefficients in the original global quartic chart.

No explicit polynomial or rational one-parameter path in the global coefficient space is supplied here. In particular, the five tangent pairs in (7) preserve the boundary to first order; simply writing \(f+th,g+tk\) need not preserve it at higher orders. Constructing such a path, or displaying the recursively corrected coefficient series, remains a separate experiment. Formal node charts likewise do not give a new uniform statement for arbitrary complete intersections.

## 7. The geometric picture suggested by the calculation

The residual \(L\cup E\) has

\[
p_a(L\cup E)=0+12+5-1=16.
\]

Its dual graph has two vertices joined by five edges, so four units of arithmetic genus lie in graph cycles. Smoothing all five connecting nodes would combine the components and turn those graph cycles into four additional units of normalization genus, giving the genus 16 smooth residual picture.

The rank calculation shows that these five node directions survive the fixed-boundary constraint. The attachment divisor records where the residual meets \(C\); it does not determine how much genus resides in the residual normalization or in gluing away from \(C\). This is a concrete organizing structure for the notebook: the 14-dimensional boundary fiber has five independent residual-node directions and nine further tangent directions invisible to both diagnostics.

For partial smoothing over a splitting field, the usual graph picture predicts that smoothing at least one connecting node joins the two components, while the other unsmoothed bridges become self-nodes. One should distinguish that formal/local picture from an explicitly computed global algebraic subfamily. The strongest directly reproduced statement remains the exact joint rank and its tangent witnesses.

The next focused experiment is to lift one tangent witness through higher orders under the exact equation \(\beta=\beta_0\), then compute the residual normalization in a concrete fiber. The result would make visible what the boundary map presently hides. No fixed scalar proximity measure is required to formulate this experiment.

## Reproducibility and scope

```sh
python3 research/computations/verify_ci_fixed_boundary_node_smoothing_2026_10_25.py
```

The script uses only Python's standard library and finishes in a fraction of a second. It checks that \(P\) is squarefree, the carrier derivative is invertible, the gradient-dependence identities hold at the node algebra, the base boundary is degree 18 and squarefree, and all five explicit rational tangent pairs satisfy (7). A separate agent independently rebuilt the global basis and both maps in a scratch computation, obtaining the same ranks 19,5,24 and the same Grassmannian interpretation.

The geometry of \(L,E\) and their intersections is supplied by the [companion exact line-degeneration computation](2026-10-25-ci-cycle-line-degeneration.md) and its [independent audit](2026-10-25-ci-cycle-line-degeneration-audit.md); this script does not repeat that projective smoothness calculation. The formal interpretation has its additional local-deformation input stated explicitly. No accepted result, proof, or canonical frontier record changes.
