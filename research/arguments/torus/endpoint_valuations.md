# Endpoint valuation fans and cancellation

This is the explicit local laboratory for the prescribed quartic pair F=x1^4-x0^3*x3, G=x2^4-x0*x3^3. Work in characteristic zero except for the identified characteristic-two comparison. The endpoint surface is smooth, permitting the two-variable slice; this is not automatically available for arbitrary pairs. Flags and full initial ideals retain information lost by one scalar ideal value.

## Endpoint fans and full residue data

## 1. First distinguish the centers of the valuations

There are three different objects that can be confused if one writes only “order along the curve and at the endpoint.”

1. At the generic point of \(C\), the ambient regular local ring has dimension two, with residue field \(K=k(C)\). Its normal coordinates are \(X,Y\). The order in \((X,Y)\) is the divisorial valuation of the exceptional divisor of the ambient blowup along \(C\). It measures the least normal degree of an individual function. Its value on a two-generated ideal is not the transverse colength.
2. At a point \(p\in C\), \(\operatorname{ord}_p\) is a discrete valuation of the **curve's function field** \(k(C)\). Extending it to an ambient valuation requires more choices. It is not, by itself, a valuation of \(k(\mathbf P^3)\).
3. A complete flag on a birational ambient model combines successive orders into a higher-rank valuation. The order of the flag decides which feature is examined first. A weighted monomial valuation provides a related family of rank-one comparisons, rather than one preferred hierarchy.

These distinctions are useful rather than pedantic: the same reduced configuration looks fourfold to some point-centered valuations and simple to a valuation centered at the generic point of \(C\).

## 2. The endpoint polynomial and its weighted fan

Near \(p=[1:0:0:0]\), use

\[
u=x_1,\qquad X=x_3-u^4,\qquad Y=x_2-u^3.
\]

Then \(I_C=(X,Y)\), \(F=-X\), and actual ideal elimination gives

\[
I_Z=(X,f),\qquad
f=Y^4+4u^3Y^3+6u^6Y^2+4u^9Y
 =Y\prod_{\zeta\ne1}(Y-c_\zeta u^3),\quad c_\zeta=\zeta-1.
                                                        \tag{1}
\]

All three \(c_\zeta\) are nonzero and distinct in characteristic zero. The smooth surface \(S=V(F)\) has parameters \(u,Y\), and the marked curve is \(Y=0\).

Choose positive weights

\[
v_{\alpha,\beta}(u)=\alpha,\qquad
v_{\alpha,\beta}(Y)=\beta.
\]

For rational weights this can be rescaled to an integral monomial valuation; irrational weights give real-valued monomial valuations. Directly from (1),

\[
v_{\alpha,\beta}(f)
 =\beta+3\min(\beta,3\alpha)
 =\begin{cases}
4\beta,&\beta\le3\alpha,\\
\beta+9\alpha,&\beta\ge3\alpha.
\end{cases}                                               \tag{2}
\]

The wall \(\beta=3\alpha\) is where the common order-three tangency becomes visible. On the wall all the displayed terms have the same weight, so the initial polynomial retains the separated-root polynomial. Away from it, the initial polynomial is only \(Y^4\), or only \(4u^9Y\). The full function of weights sees more than either generic initial term.

There is no cancellation ambiguity in (2): these are distinct monomials in the associated graded ring. Cancellation becomes an issue when one evaluates a different expression representing a generator modulo the other generator; that is addressed below.

A useful reading of the two cones is:

- When normal displacement is relatively inexpensive, the four branches have the same leading direction, giving \(Y^4\).
- When normal displacement is expensive relative to motion along \(C\), the three residual separations contribute \(u^9\), leaving the marked branch factor \(Y\).
- At the balancing weight, the four actual directions are retained.

This is a simple example of a valuation fan recording unequal roles for a parameter along \(C\) and a parameter normal to it.

## 3. Three blowups turn the wall into four directions

The same contact can be read without weighted notation. Blow up the endpoint in the smooth surface \(S\), then follow the common tangent point. In the successive relevant charts put

\[
Y=uY_1,\qquad Y_1=uY_2,\qquad Y_2=uY_3.
\]

The associated exceptional divisorial valuations have weights

\[
(1,1),\qquad(1,2),\qquad(1,3)
\]

on \((u,Y)\). After the third blowup,

\[
f=u^{12}\,Y_3\prod_{\zeta\ne1}(Y_3-c_\zeta).
\]

The strict branches now meet the last exceptional curve at four distinct points: the marked direction \(0\), and the three residual directions \(c_\zeta\). The exceptional valuation has \(v(f)=12\). The pairwise contact order three has become a chain of three common infinitely near points, followed by separation.

This gives a concrete decorated contact tree. Before separation all four branches share the path; after separation their positions on the exceptional \(\mathbf P^1\) carry extra information such as a cross-ratio. The weight fan records the break at three but does not record that cross-ratio. One must retain the initial polynomial at the wall, or the four marked points on the exceptional curve. The [root-pencil note](root_pencil_geometry.md) develops the corresponding elliptic modulus.

Thus even the full piecewise-linear function (2) is not a complete contact invariant. A useful adaptive object is a tree of valuations together with residue polynomials at the vertices where branches separate.

## 4. Normal first, then endpoint: the flag value \((1,9)\)

On the smooth surface \(S\), the complete flag

\[
S\supset C\supset\{p\}
\]

gives a rank-two valuation with lexicographic order: first take the order in \(Y\), divide it off, then take the endpoint order of the leading coefficient on \(C\). For (1),

\[
v_{S\supset C\supset p}(f)=(1,9).
\]

The first coordinate says that \(C\) is generically a simple component. The second says that the residual factor meets that branch to total order nine at this endpoint. This is the valuative form of the conductor boundary calculation. The opposite endpoint gives another nine.

Taking the ordinary point order first gives \(\operatorname{ord}_{(u,Y)}(f)=4\), with first tangent cone \(Y^4\). This has forgotten both the generic simplicity of \(C\) and the later separation of the branches. The two hierarchies answer different questions.

Equation (2) approaches the normal-first hierarchy as \(\beta/\alpha\) becomes large: the coefficient of \(\beta\) is one, and the remaining term is \(9\alpha\). This is a useful way to connect lexicographic data to families of rank-one valuations. It is an interpretation of the explicit formula, not an assertion that every higher-rank valuation has a canonical preferred real-valued approximation.

For the standard recursive construction of valuations from admissible flags, see [Lazarsfeld–Mustaţă, *Convex bodies associated to linear series*, Section 1.1](https://www.math.stonybrook.edu/robert.lazarsfeld/Reprints/Laz.Mustata.CBALS.pdf). In the present note the valuations are applied locally to functions and extended to their fraction fields; no global Newton–Okounkov body is being asserted.

## 5. The partial-splitting pencil changes the fan

Keep \(F\) fixed and replace \(G\) by

\[
G_\lambda=G+\lambda Qx_0^2,\qquad Q=x_0x_3-x_1x_2.
\]

The actual equation on \(S\) is

\[
f_\lambda
 =Y\left(Y^3+4u^3Y^2+6u^6Y+4u^9-\lambda u\right).       \tag{3}
\]

For a nonzero characteristic-zero parameter \(\lambda\), the weighted value becomes

\[
v_{\alpha,\beta}(f_\lambda)
 =\beta+\min(3\beta,\alpha).                             \tag{4}
\]

The new wall is \(\alpha=3\beta\). Every other term in the residual factor has greater weight than \(\alpha\) or \(3\beta\). The normal-first flag value is now

\[
v_{S\supset C\supset p}(f_\lambda)=(1,1).
\]

The residual branch is smooth at \(p\), since its equation has nonzero \(u\)-derivative \(-\lambda\). It is transverse to \(C\). Nine units of attachment at this endpoint have become one retained node plus eight mobile simple attachments; the latter satisfy \(u^8=\lambda/4\). The opposite endpoint keeps its order-nine attachment in this asymmetric family.

There is a subtle coordinate warning. The new wall in (4) no longer measures a common order-three contact between distinct branches. The residual branch has expansion \(u\sim Y^3/\lambda\), so the wall records its curvature relative to the chosen coordinate line \(u=0\). Replacing \(u\) by the residual equation in parentheses in (3) is an analytic coordinate change, and the node becomes exactly a product of two parameters. Its adapted valuation profile is then simply the sum of their weights.

Therefore a fixed coordinate fan is a useful laboratory, while an intrinsic adaptive comparison should permit coordinate changes or encode infinitely near branches. It must distinguish shared branch contact from contact of a single smooth branch with an arbitrarily chosen coordinate axis.

## 6. A comparison table, including thickness

The following local surface models isolate the different observations. Coefficients \(c_j\ne0\) are distinct.

| Model | Weighted value in chosen \((u,Y)\) | Normal-first flag | What it represents |
|---|---|---|---|
| \(Y\prod_{j=1}^3(Y-c_j u^3)\) | \(\beta+3\min(\beta,3\alpha)\) | \((1,9)\) | Four reduced branches, marked branch simple |
| Partial split (3), \(\lambda\ne0\) | \(\beta+\min(3\beta,\alpha)\) | \((1,1)\) | A node at the retained endpoint |
| \(Y^2\prod_{j=1}^2(Y-c_j u^3)\) | \(2\beta+2\min(\beta,3\alpha)\) | \((2,6)\) | Marked component doubled, two residual branches |
| \(Y^4\) | \(4\beta\) | \((4,0)\) | Pure transverse length four |
| Adapted node \(YV\) | \(\beta+v(V)\) | \((1,1)\) relative to its transverse parameter | Two transverse reduced branches |

The pure \(Y^4\) model is the actual endpoint model in characteristic two for the prescribed equations. In characteristic zero it is a formal comparison model here, not a claimed global \((4,4)\) realization. The doubled model matches the local pattern of the marked-root collision in the root pencil, after allowing nonzero distinct residual coefficients.

A single point-centered scalar cannot identify generic thickness. For example, when \(\alpha=\beta=1\), the four reduced tangent branches and \(Y^4\) both have value four. Even the partial-split node can have value \(4\beta\) if \(\alpha\ge3\beta\) in the original coordinates. The distinction appears when the center, the flag, and the residue data are retained.

At the generic point of \(C\), \(u\) is a unit. Formally putting \(\alpha=0\) in the relevant expression gives \(v(f)=\beta\) for the reduced arrangement, while \(v(Y^4)=4\beta\). This is why endpoint contact should not be silently relabelled as generic multiplicity.

## 7. Lifting back to the ambient threefold

The surface calculation is legitimate because \(F\) is smooth at \(p\). It is not automatically available for an arbitrary complete-intersection pair whose two equations may both be singular there.

For the present pair, the ambient completed local ring is \(k[[u,X,Y]]\), and an ambient monomial valuation with values \((\alpha,\gamma,\beta)\) gives

\[
v(I_C)=\min(\gamma,\beta),\qquad
v(I_Z)=\min\bigl(\gamma,\ \beta+3\min(\beta,3\alpha)\bigr). \tag{5}
\]

If \(\gamma\) is small, the smooth generator \(X\) hides the entire residual profile in the scalar value of the ideal. Looking at all weights with \(\gamma\) sufficiently large recovers the plane slice, but there is no justification for treating one convenient ambient value as the whole invariant.

The generic normal order of the ideal is also insufficient: both \((X,Y)\) and \((X,Y^4)\) have least normal order one, while their transverse lengths are one and four. Recovering a two-dimensional intersection multiplicity needs more than the minimum of two orders.

There is a natural ambient flag construction that survives without choosing a smooth member of the pair. Let

\[
B=\operatorname{Bl}_C\mathbf P^3,\qquad E\to C
\]

be its exceptional ruled surface. It is a projective bundle because the ambient and center are smooth; see [Stacks Project, Lemma 37.17.3](https://stacks.math.columbia.edu/tag/0FUT), with its stated projectivization convention. A full flag

\[
B\supset E\supset E_p\supset\{\xi\}
\]

has successive dimensions \(3,2,1,0\), where \(E_p\) is the exceptional fiber over a point \(p\in C\) and \(\xi\) is a chosen normal direction in that fiber. It gives a rank-three valuation of the ambient function field. The direction \(\xi\) can be selected from the actual transformed ideal or from common initial normal directions of a proposed pair; it need not be fixed in advance for every \(W\).

In the \(Y\)-chart of the present blowup, put \(Y=t,X=t\xi\). The flag is locally \(t=0\), then \(u=0\), then \(\xi=0\). With lexicographic order on \((t,u,\xi)\),

\[
v(X)=(1,0,1),\qquad v(f)=(1,9,0).
\]

The ideal's single minimum is \((1,0,1)\), again hiding the second datum. The collection of initial equations, not merely their minimum, is the relevant object.

This is also a place where actual cancellation matters. The original second equation is

\[
G=f-3u^8X-3u^4X^2-X^3.
\]

Its first flag term can lie in the direction already generated by \(X\). Eliminating those actual multiples reveals \(f\) and its ninefold endpoint coefficient. Values attached independently to the displayed generators can change under a change of generating pair; the full ideal and its induced filtered quotient retain the geometry.

## 8. A blowup warning: exceptional components are not residual curves downstairs

In the same chart, the total inverse-image ideal is

\[
I_Z\mathcal O_B
 =t\left(\xi,\ t^3+4u^3t^2+6u^6t+4u^9\right).           \tag{6}
\]

The factor \(t\) records the exceptional surface in the full inverse image. Saturating by \(t\) gives the strict transform of the residual curve, with ideal

\[
\left(\xi,\ t^3+4u^3t^2+6u^6t+4u^9\right).
\]

Its intersection with \(E\) is cut out by \((\xi,u^9)\), a length-nine scheme over \(p\). The three residual branches contribute three each. This realizes the contact budget as an intersection upstairs.

The marked component \(C\), being the center, has no strict transform obtained by closing its complement to the center. The exceptional surface is not an additional curve component of the original intersection. One must distinguish the full inverse image, its exceptional part, and the strict residual transform. A proposed valuative residual detector must eventually push forward the correct curve cycle, rather than count all exceptional geometry as residual degree downstairs.

The basic total-transform/exceptional-divisor conventions are fixed in [Stacks Project, Section 31.33](https://stacks.math.columbia.edu/tag/01OF). Equation (6) is an explicit coordinate calculation in the present example.




## Characteristic reach

The distinct-four-branch weighted fan is characteristic-zero data; in characteristic two its displayed polynomial becomes Y^4 and its reduced support is only the marked curve. The explicit ambient blowup and cancellation reasoning remain local algebra in every characteristic with the equations adjusted as stated. No universal residual conclusion follows.
