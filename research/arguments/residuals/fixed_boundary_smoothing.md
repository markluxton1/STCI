# Independent node smoothing with the marked boundary fixed

This is the full proof home for [R-0024](../../results/ci_quartic_fixed_boundary_smoothing.md), at the exact (1,1) pencil of [R-0023](explicit_quartic_residuals.md). It is a formal and etale-local theorem after splitting the five nodes, not a polynomial coefficient arc or a universal smoothing theorem.

## 1. The actual point and the two separate boundaries

Use the homogeneous forms \(F,G,Q,A,D_3,H_0,H_1\) from the [smooth residual benchmark](explicit_quartic_residuals.md), but take coefficients 1,1:

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

## 4. Joint surjectivity by restriction and interpolation

Write \(p=C\cap L\), with \(u=r=-1\). We show that \((D,S)\) is onto over \(\mathbf Q\) by using perturbations that come from global quartics throughout.

**Fill the boundary directions vanishing at \(p\) without touching the nodes.** The quadric \(Q=x_0x_3-x_1x_2\) contains both \(C\) and \(L\). For any homogeneous quadric \(q\), the quartic \(Qq\) belongs to \(V\) and vanishes on \(L\), so perturbing either equation by it gives zero node class. Its first-normal symbol is \(q|_C\sigma_Q\), where \(\sigma_Q=(1,-u)\). The first-normal rows of (1) give

\[
\det(\sigma_Q,\sigma_g)=u^9(1+u),\qquad
\det(\sigma_f,\sigma_Q)=1+u.
\]

Quadratic restrictions fill \(H^0(\mathcal O_{\mathbf P^1}(8))\): ambient quadrics restrict onto \(H^0(Q,\mathcal O_Q(2,2))\), and on the smooth quadric the kernel of restriction to the \((1,3)\)-curve is \(\mathcal O_Q(1,-1)\), with \(H^1=0\). After homogenizing and dividing by \(s+t\), the two boundary subspaces from (5) are \(t^9H^0(\mathcal O(8))\) and \(s^9H^0(\mathcal O(8))\), together spanning \(H^0(\mathcal O(17))\). Thus the joint image contains \(H^0(\mathcal O(18)(-p))\times 0\).

**Read the last boundary value from restriction to \(L\).** In line coordinates \([x_0:x_1:x_2:x_3]=[-R:R:-S:S]\), the cubics \(A\), \(B=x_0x_2^2-x_1^2x_3\), and \(D_3\) in \(I_C\) restrict to \(R+S\) times \(R^2,-RS,-S^2\), respectively. Ambient linear forms restrict onto \(H^0(L,\mathcal O_L(1))\), so products with those cubics show that \(V\to H^0(L,\mathcal O_L(4)(-p))\) is onto. In particular, any polynomial of degree at most four divisible by \(r+1\) is an allowable restriction in the chart \(x_3=1\).

At \(p\), the actual homogeneous pair (1) has \(\sigma_f(p)=0\) and \(\sigma_g(p)=14\sigma_Q(p)=(14,14)\). In the \(x_0=1\) chart the line has \(u=-1\), \(X=-1/r-1\), and \(Y=-X\). At \(r=-1\), \(dX/dr=1\). The two quartic trivializations differ by a unit of value one at \(p\), and \(h(p)=0\), so the derivative of \(h|_L\) is the same in either trivialization. Therefore (5) gives

\[
D(h,k)(p)=14(A_h(p)-B_h(p))=14(h|_L)'(-1).
\]

In particular a \(k\)-only perturbation or an \(h\)-restriction with a double zero at \(p\) does not change this boundary value.

**Interpolate the five node directions with \(D(p)=0\).** Divide the node class by the unit \(F_1(r+1)\) in \(\mathcal A\); indeed \(P(0)=2\), \(P(-1)=-14\), and \(P(-2)=-228\). Taking \(h=0\) and \(k|_L=(r+1)k_3(r)\), where \(\deg k_3\le3\), gives every degree-at-most-three class after this normalization. Taking \(k=0\) and \(h|_L=r(r+1)^2\) gives the normalized class \(G_1/(r+2)\), which is a degree-two polynomial plus \(57/(r+2)\), since \(G_1(-2)=57\). The unique representative of \((r+2)^{-1}\) modulo \(P\) of degree at most four has degree exactly four: otherwise \((r+2)b-1\) for a representative \(b\) of degree at most three would be divisible by \(P\) and have degree at most four, forcing the impossible polynomial identity \((r+2)b=1\). These variations span the five-dimensional node algebra while keeping \(D(p)=0\). Finally take \(h|_L=r+1\) to get \(D(p)\ne0\); variations with \(D(p)=0\) can then correct its node class independently.

The image thus contains the boundary subspace vanishing at \(p\) paired with zero and surjects onto the complementary quotient \(\mathbf Q\oplus\mathcal A\), giving

\[
\boxed{\operatorname{rank}D=19,\qquad
       \operatorname{rank}S=5,\qquad
       \operatorname{rank}(D,S)=24.}          \tag{6}
\]

The final equality implies

\[
\operatorname{rank}\bigl(S|_{\ker D}\bigr)=24-19=5.
\]

As independent computational evidence, the [standard-library exact verifier](../../computations/verify_ci_fixed_boundary_node_smoothing_2026_10_25.py) reconstructs these ranks in the actual global monomial-difference basis: nineteen boundary coefficients and five node coefficients on the 36-dimensional ordered source. It also produces five explicit rational source vectors \(v_0,\ldots,v_4\in V^2\) satisfying

\[
D(v_i)=0,\qquad S(v_i)=r^i\pmod P
\quad(i=0,\ldots,4).                         \tag{7}
\]

Their 36 source coefficients are recorded in the [JSON evidence](../../computations/ci_fixed_boundary_node_smoothing_2026_10_25.json), together with the global monomial basis, polynomial (2), matrix pivot columns, and all checked ranks. The script verifies every equality in (7) exactly. These are actual homogeneous first-order perturbations with zero affine boundary derivative.

The nodes need not be individually rational over \(\mathbf Q\). Equation (7) spans their étale algebra over \(\mathbf Q\). After extending to an algebraically closed field and splitting \(P\), evaluation identifies \(\mathcal A\otimes k\) with \(k^5\), so the five geometric node parameters are independent. Selecting only one geometric node may require coefficients in a splitting field; no assertion that all nodes are rational is made.

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

## 6. Formal interpretation, kept separate from the tangent calculation

There is a useful standard local consequence after extending scalars to split and mark the five nodes. The parameter space of pencils is smooth, and the surjective boundary differential makes the completed fixed-boundary fiber a smooth formal space of dimension 14.

For a split node in a flat family, [Stacks, Lemma 53.20.11](https://stacks.math.columbia.edu/tag/0CBX) gives a completed equation \(xy-\tau_i=0\), with \(\tau_i\) a function of the formal base parameters. Its first differential is the node class (4), up to a unit. The étale local counterpart is [Stacks, Lemma 53.21.1](https://stacks.math.columbia.edu/tag/0CBY).

On the completed fixed-boundary fiber, the five linear forms \(d\tau_i\) are independent by (8). Formal coordinates can therefore be chosen so that its complete local ring is

\[
k[[\tau_1,\ldots,\tau_5,z_1,\ldots,z_9]].     \tag{9}
\]

In this formal sense the five residual nodes can be smoothed independently while the boundary divisor is held exactly fixed. This uses unobstructedness of the smooth fixed-boundary parameter fiber, not merely the existence of five first-order vectors. The standard node local form and the formal inverse-function argument are additional to the tangent surjectivity proof.

The étale node charts also give a local algebraic existence interpretation. After a common étale base change that labels the nodes, the five node parameters are regular functions. The joint map \((\beta,\tau_1,\ldots,\tau_5)\) has surjective differential, so its restriction to the fixed-boundary fiber maps smoothly to \(\mathbf A^5\) near the marked point. A chosen one-parameter pattern \(\tau_i=c_i t\) therefore lifts locally after an étale change of the one-parameter base; a zero \(c_i\) retains that node, and a nonzero \(c_i\) smooths it in the generic fiber. This is an existence statement for local algebraic families, derived from smoothness and the node charts. It does not display their coefficients in the original global quartic chart.

No explicit polynomial or rational one-parameter path in the global coefficient space is supplied here. In particular, the five tangent pairs in (7) preserve the boundary to first order; simply writing \(f+th,g+tk\) need not preserve it at higher orders. Constructing such a path, or displaying the recursively corrected coefficient series, remains a separate experiment. Formal node charts likewise do not give a new uniform statement for arbitrary complete intersections.

## 7. The geometric picture suggested by the calculation

The residual \(L\cup E\) has

\[
p_a(L\cup E)=0+12+5-1=16.
\]

Its dual graph has two vertices joined by five edges, so four units of arithmetic genus lie in graph cycles. Smoothing all five connecting nodes would combine the components and turn those graph cycles into four additional units of normalization genus, giving the genus 16 smooth residual picture.

The joint surjectivity proof shows that these five node directions survive the fixed-boundary constraint. The attachment divisor records where the residual meets \(C\); it does not determine how much genus resides in the residual normalization or in gluing away from \(C\). This is a concrete organizing structure for the notebook: the 14-dimensional boundary fiber has five independent residual-node directions and nine further tangent directions invisible to both diagnostics.

For partial smoothing over a splitting field, the usual graph picture predicts that smoothing at least one connecting node joins the two components, while the other unsmoothed bridges become self-nodes. One should distinguish that formal/local picture from an explicitly computed global algebraic subfamily. The strongest directly reproduced statement remains the exact joint rank and its tangent witnesses.

The next focused experiment is to lift one tangent witness through higher orders under the exact equation \(\beta=\beta_0\), then compute the residual normalization in a concrete fiber. The result would make visible what the boundary map presently hides. No fixed scalar proximity measure is required to formulate this experiment.

## Characteristic reach and limitation

The node-family/formal-coordinate mechanism works for split ordinary nodes in any characteristic **provided flatness and independent differentials hold**. The geometric tangent proof and its matrix verification are for the certified characteristic-zero pencil only; neither gives all-prime ranks or nodal reduction. Thus the local smoothing theorem does not obstruct [positive-characteristic quartic-carrier pairs](../arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier).
