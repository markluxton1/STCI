# Adaptive local witnesses and the valuative contact cycle

Date: 2026-10-25. Status: exploratory continuation of the [adaptive valuative notebook](2026-10-25-ci-cycle-adaptive-valuative-notebook.md), building on the [complete-intersection cycle notebook](2026-10-25-ci-cycle-geometry-notebook.md). Standard local and intersection-theoretic facts are separated from the proposed organizing viewpoint. Nothing here asserts that every characteristic-zero complete intersection containing the fixed quartic has a residual component. The [independent valuative audit](2026-10-25-ci-cycle-valuative-audit.md) reconstructs the local criterion and the four-line counterexample.

## 1. First separate the residual question from its possible witnesses

Let \(k\) be algebraically closed of characteristic zero, let \(C=[s^4:s^3t:st^3:t^4]\) be the fixed smooth quartic, and let

\[
W=V(A,B)\subset\mathbf P^3_k
\]

be any proper complete intersection of two positive-degree hypersurfaces whose support contains \(C\). Write its fundamental cycle uniquely as

\[
[W]=m_C[C]+R,\qquad
R=\sum_{D\ne C}m_D[D]\ge0.
\]

Here \(D\) runs through the other reduced irreducible components and \(m_D\) is the generic length of \(W\) along that component. This makes sense even when \(m_C>1\). The subtraction defines a cycle; it does not claim a canonical scheme-theoretic residual to an unspecified multiple structure on \(C\).

The future universal target would be \(R\ne0\) for every such \(W\) in the stipulated characteristic-zero fixed-quartic setting. The present note supplies several equivalent ways to **recognize** \(R\ne0\) for a particular \(W\). Equivalence does not establish that the equivalent conditions always hold. In particular, no local invariant whose positivity is still unknown has resolved the global existence question.

This distinction makes room for adaptive investigation: choose the point, branch, ideal, or blowup suggested by the actual pair, rather than requiring one fixed numerical metric to order every complete intersection.

## 2. An adaptive point witness already exists at cycle level

For a closed point \(p\in C\) let

\[
e_p(W)=e_{\mathfrak m_p}(\mathcal O_{W,p})
\]

be the Hilbert--Samuel multiplicity. This is not the infinite length of the one-dimensional local ring. Over the infinite field \(k\), it can be computed as the length of a sufficiently general local linear slice. The word *general* matters: a hyperplane tangent to a branch need not calculate its multiplicity.

Associativity of multiplicities gives

\[
e_p(W)
=m_Ce_p(C)+\sum_{D\ni p}m_De_p(D)
=m_C+\sum_{D\ni p}m_De_p(D),                 \tag{1}
\]

because \(C\) is smooth. One precise route is to choose a common sufficiently general linear parameter for the finitely many branches through \(p\) and apply [Stacks, Lemma 42.3.2](https://stacks.math.columbia.edu/tag/02QG), which adds the generic lengths of the components with the appropriate slice lengths. All terms in the residual sum are positive when present.

A proper projective complete-intersection curve is connected. For this setting one needs only the elementary Koszul calculation: from

\[
0\longrightarrow\mathcal O(-a-b)
\longrightarrow\mathcal O(-a)\oplus\mathcal O(-b)
\longrightarrow I_W\longrightarrow0
\]

and the vanishing of intermediate cohomology of line bundles on \(\mathbf P^3\), obtain \(H^1(I_W)=0\) and then \(H^0(\mathcal O_W)=k\). A disconnected scheme would have a nontrivial idempotent, contradicting this equality. The cohomology input is [Stacks, cohomology of projective space](https://stacks.math.columbia.edu/tag/01XS). This proof also covers nonreduced complete intersections.

Connectedness now implies

\[
R\ne0
\quad\Longleftrightarrow\quad
\exists p\in C:\ e_p(W)>m_C.                 \tag{2}
\]

Indeed, if residual components exist, their finite union must meet \(C\); otherwise the support would be disconnected. At such a meeting point equation (1) is strict. Conversely, strictness in (1) directly exhibits a residual component through that point.

Thus one may adaptively seek a point with multiplicity exceeding the generic multiplicity along \(C\). The point need not be one of the distinguished endpoints. The formula is valid in other characteristics as well; characteristic zero has not been used to force positivity.

It is useful to retain the whole finite effective cycle

\[
M_C(W)=\sum_{p\in C}\bigl(e_p(W)-m_C\bigr)[p]. \tag{3}
\]

It is supported exactly where residual components meet \(C\). For the distinguished reduced characteristic-zero \(Z\) of [STCI-R-0021](../results/quartic_mu4_degeneration.md), write \(p=[1:0:0:0]\) and \(q=[0:0:0:1]\). Then it is \(3p+3q\): four smooth branches meet at each endpoint and the generic multiplicity of the marked component is 1. By contrast, the accepted characteristic-two fiber has fundamental cycle \(4[C]\), so \(M_C(W)=0\). That is consistent with (2), not an exception to it. The local multiplicity test does not detect internal nilpotent geometry when all cycle mass remains on \(C\).

## 3. A contact cycle built from the actual residual branches

For every reduced residual component let

\[
\nu_D:\overline D\longrightarrow D
\]

be its finite normalization. Since \(D\ne C\), the image ideal \(I_C\mathcal O_{\overline D}\) is nonzero at the generic point and has finite support of zeros. The smooth curve \(\overline D\) has discrete valuation rings at its closed points, so

\[
I_C\mathcal O_{\overline D}
=\mathcal O_{\overline D}(-T_D),\qquad
T_D=\sum_{r\mapsto C}
\operatorname{ord}_r(I_C\mathcal O_{\overline D})[r].
\]

Define the **valuative contact cycle**

\[
B_C^{\mathrm{val}}(R)
=\sum_Dm_D(\nu_D)_*T_D.                       \tag{4}
\]

For the algebraically closed field under discussion, this simply sums the branch orders at their image points on \(C\). Retain the actual effective cycle, rather than only its Chow class: on \(C\simeq\mathbf P^1\), rational equivalence remembers only its degree and loses the endpoint concentration. Nor is this contact invariant determined by the rational-equivalence class of \(R\) in \(\mathbf P^3\). Over a nonclosed field, pushforward also includes residue-field degrees; omitting them would change the invariant.

The definition uses the actual marked embedding of \(C\) in the ambient space. If \(I_C\) is locally generated by \(f_1,\ldots,f_s\), its coefficient on a branch is

\[
\min_i\operatorname{ord}_r(\nu_D^*f_i).
\]

The cycle is invariant under projective automorphisms carrying the entire marked pair to another marked pair. Changing the generators does not change the minimum: it is the order of the ideal itself. This is more adaptable than selecting one fixed ambient polynomial or one predetermined valuation for every pair.

There is a direct blowup interpretation. Let

\[
\pi:\operatorname{Bl}_C\mathbf P^3\longrightarrow\mathbf P^3
\]

have exceptional divisor \(E\). Because the pulled back ideal on \(\overline D\) is invertible, \(\nu_D\) lifts to the blowup by its universal property. Intersecting the **strict residual cycle** \(\widetilde R\) with \(E\) gives

\[
B_C^{\mathrm{val}}(R)=\pi_*(E\cdot\widetilde R). \tag{5}
\]

The intersection is proper because no strict transform of a component \(D\ne C\) lies in \(E\). Formula (5) is a cycle-level identity: one may calculate it on the normalizations and push forward. The [universal property of the blowup](https://stacks.math.columbia.edu/tag/01OF), [Cartier pullback](https://stacks.math.columbia.edu/tag/01WQ), and [degrees on curves](https://stacks.math.columbia.edu/tag/0AYQ) provide the standard foundations.

The use of strict residual transform is essential. The full inverse image of \(W\) contains exceptional geometry over \(C\); those exceptional curves or surfaces are not additional components of \(W\) downstairs. When \(R=0\), equation (5) uses the zero strict residual cycle, however complicated the full inverse image is.

Every residual branch through \(C\) contributes a positive integer. Combined with connectedness,

\[
R\ne0\quad\Longleftrightarrow\quad
B_C^{\mathrm{val}}(R)\ne0.                    \tag{6}
\]

Once again this is a recognition criterion. Writing its right side has not proved its positivity for every characteristic-zero pair.

## 4. Multiplicity excess and higher tangency separate cleanly

Choose local ambient coordinates \((u,x,y)\) at \(p\) with \(C=(x,y)\). On a normalized residual branch, write

\[
a_r=\min\{\operatorname{ord}_r(u),\operatorname{ord}_r(x),
\operatorname{ord}_r(y)\},\qquad
b_r=\min\{\operatorname{ord}_r(x),\operatorname{ord}_r(y)\}.
\]

Then \(a_r\) is the branch multiplicity at \(p\) and \(b_r\) is its contact with the ideal of \(C\). Therefore \(b_r\ge a_r\), and summing gives

\[
B_C^{\mathrm{val}}(R)\ge M_C(W).              \tag{7}
\]

The difference is an effective cycle recording contact beyond the multiplicity of the residual branches. It distinguishes a large number of branches crossing \(C\) from a smaller number following its tangent to higher order.

For \(Z\), the other three quartics have contact order 3 with \(C\) at each endpoint. Thus

\[
M_C(Z)=3p+3q,\qquad
B_C^{\mathrm{val}}(R_Z)=9p+9q,
\]

and the excess contact is \(6p+6q\). In the generic deformation picture \(C\cup D\) with 18 transverse nodes, each coefficient of both cycles is 1. This offers two complementary ways to compare configurations without asserting a total ordering.

A degree-dependent estimate is available, but it is not a bounded-degree solution. Since the actual fixed-quartic ideal is generated in degrees at most 3, as recorded with the explicit generators in the [deformation laboratory](2026-10-25-ci-cycle-deformation-laboratory.md), choose a general cubic through \(C\) avoiding all components of \(R\). On every normalized residual component its divisor has degree \(3\deg D\) and dominates \(T_D\). Hence

\[
0\le\deg M_C(W)\le\deg B_C^{\mathrm{val}}(R)\le3\deg R
=3(ab-4m_C).                                 \tag{8}
\]

The two contact degrees vanish exactly when \(R=0\), by connectedness and equations (2), (6), and (7). Thus this chain is a numerical consistency check, with no universal positive lower bound. It controls contact after the degrees \(a,b\) and residual degree are known. It provides no uniform upper bound on the possible degrees of the defining equations, no finite search over all pairs, and no positive lower bound when \(R=0\) remains possible.

## 5. A sharp warning: branch contact is not always the conductor boundary

The equality with \(9p+9q\) for \(Z\) reflects its special local planar arrangement. It does not justify identifying (4) with the conductor or the determinant boundary for arbitrary complete intersections.

Here is a small complete-intersection counterexample. In affine 3-space set

\[
A_0=k[x,y,z]/(xy-xz,xy-yz).
\]

This is the reduced union of four lines in directions

\[
(1,0,0),\quad(0,1,0),\quad(0,0,1),\quad(1,1,1).
\]

They are the affine cone over four points in \(\mathbf P^2\) with no three collinear, a complete intersection of two quadrics. Equivalently, use the same two equations in \(\mathbf P^3_{[x:y:z:w]}\); the four projective lines share the vertex \(p=[0:0:0:1]\). This is a counterexample to a universal identification of invariants, not a substitute curve for the fixed quartic in the main investigation.

Its normalization is \(B=\bigoplus_{i=1}^4k[t_i]\). In the grading at the vertex:

- the image of \((A_0)_0\) is the one-dimensional diagonal constants;
- the image of \((A_0)_1\) is \(\{\,(a,b,c,a+b+c):a,b,c\in k\,\}\), of dimension 3;
- for every degree \(d\ge2\), the image is all four copies of the degree-\(d\) piece.

The last assertion can already be checked with quadrics: \(xy\) isolates the fourth direction, and \(x^2-xy\), \(y^2-xy\), \(z^2-xy\) isolate the first three. Multiplication by a linear form nonzero on each direction extends the conclusion to all higher degrees. There is no degree-one vector supported on just one branch. Consequently the conductor extends to

\[
\bigoplus_{i=1}^4t_i^2k[t_i]\subset B,
\]

and its boundary on each normalized line has coefficient 2. The delta invariant is \((4-1)+(4-3)=4\), consistent with total conductor degree 8 for this Gorenstein singularity.

Now mark the \(x\)-axis \(L_1\) as \(C\) for this example. Its ideal is \((y,z)\). On each of the other three lines the pulled back ideal has order 1. Therefore

\[
B_{L_1}^{\mathrm{val}}(L_2+L_3+L_4)=3[p],
\qquad \text{conductor boundary on }L_1=2[p].  \tag{9}
\]

The actual first-normal determinant also has order 2: along the \(x\)-axis with parameter \(t=x\), the two linear normal rows are \((t,-t)\) and \((t,0)\), with determinant \(t^2\).

The scheme-theoretic intersection of \(L_1\) with the residual union has length 2, not 3. No nonzero linear form vanishes on all three residual directions, while \(x^2-xy\) does vanish there and restricts to \(x^2\) on \(L_1\). Hence the image of the residual ideal in \(k[x]\) is exactly \((x^2)\). The three individual branch intersections cannot be added as intersection lengths of the union.

This is the failure mechanism: a nonplanar union has relations among the gluing conditions. Pairwise valuations of a marked ideal, intersection with the residual *scheme*, and the conductor of the total ring need not add in the same way. In this example \(M_{L_1}(W)=B_{L_1}^{\mathrm{val}}(R)=3[p]\) while the conductor and determinant boundaries are \(2[p]\).

## 6. What must be controlled before using this in a deformation ordering

The valuative cycle is well defined for an individual marked cycle, but several operations require care.

**Normalization and specialization.** Normalization need not commute with taking a special fiber. Reduced components can collide, split, or become nonreduced. Even a flat family of complete intersections need not give a flat family of residual cycles after subtracting the changing generic multiplicity on \(C\).

A local toy model makes the issue visible:

\[
W_\lambda=\bigl(X,\prod_{j=0}^3(Y-j\lambda u^3)\bigr).
\]

It is flat over \(k[\lambda]\) because the second equation is monic in \(Y\). For \(\lambda\ne0\) there are four distinct branches and, relative to \(C=(X,Y)\), the three residual branches give contact 9 at \(u=0\). For \(\lambda=0\) the cycle is \(4[C]\) and the residual contact cycle is zero. This is a local characteristic-zero illustration; it is not asserted to arise from global homogeneous quartics containing the fixed projective \(C\). It shows why flatness alone gives no monotonicity for the residual contact cycle when \(m_C\) changes.

**Multiplicity and nilpotent structure.** Equations (1)--(7) retain generic component multiplicities but discard nilpotent information not changing the fundamental cycle. Two different multiple structures supported on \(C\) can both have \(R=0\) and identical zero contact cycles.

**Base field.** Under geometric base change, use geometric branches and the usual cycle pushforward. Over the present algebraically closed characteristic-zero field, normalization is well behaved under extension of algebraically closed fields. A change of characteristic is different: the accepted integral \(\mu_4\) example is precisely a case where reduced support and component multiplicity change.

**Choice of branch or blowup.** A promising adaptive experiment can choose one residual branch and refine its contact through successive blowups. The existence of a useful branch is still part of the condition being sought. An exceptional divisor appearing over \(C\) is not by itself a residual branch downstairs.

**No predetermined endpoint.** The two distinguished points give the reference configuration its concentration. The witness in (2) may lie anywhere on \(C\). Any argument inspecting only the endpoints must separately explain why residual contact cannot migrate elsewhere.

## 7. A continuation experiment suggested by the comparison

For an actual pair, first compute or estimate \(m_C\). Then seek a point where the generic local slice length exceeds \(m_C\), using the pair to choose coordinates or a candidate valuation. When such a point is found, compare three pieces of data: multiplicity excess, normalized-branch contact, and conductor/dualizing boundary if the latter is available. Their disagreement can be useful geometry rather than an error to eliminate.

For the special \(Z\), the values \(3p+3q\) and \(9p+9q\) provide a reference for branching and higher tangency. They do not force one fixed metric on every other complete intersection. An adaptive approach could ask whether some nonzero residual contact witness always survives, while permitting its support, scale, and valuation depth to depend on the actual equations. Establishing that survival for every characteristic-zero pair remains the missing mathematical step.

No canonical result or accepted proof is changed. The local criteria are standard cycle consequences; the proposed role of their hierarchy in an adaptive investigation is exploratory. The four-line calculation has been independently reconstructed in the audit, including its conductor and actual residual-intersection length.
