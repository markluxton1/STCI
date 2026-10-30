# Complete-intersection cycles: permanent mathematical source consolidation

## Mathematical dependency guide: three levels of contact

The [valuative contact cycle](#2026-10-25-ci-cycle-valuative-contact-cyclemd) separates a cycle-level witness from its possible local valuations. The [endpoint valuations](#2026-10-25-ci-cycle-endpoint-valuationsmd), [valuative multiplicity](#2026-10-25-ci-cycle-valuative-multiplicitymd), and [root-collision valuations](#2026-10-25-ci-cycle-root-collision-valuationsmd) address different local degeneration regimes. The source calculations should not be reduced to a single scalar order.

The [independent valuative audit](CI_CYCLE_AUDITS_AND_BOUNDARY_SMOOTHING.md#2026-10-25-ci-cycle-valuative-auditmd) limits what follows. Compare [intrinsic coefficient valuations and the colength counterexample](INTRINSIC_VALUATIONS_AND_CONTACT_GEOMETRY.md#2026-10-23-intrinsic-coefficient-valuationsmd), [actual smooth residual examples](CI_CYCLE_DEFORMATIONS_AND_RESIDUAL_GEOMETRY.md#2026-10-25-ci-cycle-smooth-residual-examplemd), and [pencil specialization](CI_CYCLE_PENCILS_AND_SPECIALIZATION.md#2026-10-25-ci-cycle-specialization-proximitymd).

A higher contact order does not by itself establish an additional residual component or its absence; retain both the local calculation and the global intersection test.

---


This subject supplement preserves the full mathematical content of the source investigations below, including hypotheses, computations, counterexamples, and limitations. Historical headings identify internal sections, not separate retained source files. No new theorem promotion is implied.


---

## 2026-10-25-ci-cycle-valuative-contact-cycle.md

# Adaptive local witnesses and the valuative contact cycle

Date: 2026-10-25. Status: exploratory continuation of the [adaptive valuative notebook](CI_CYCLE_ADAPTIVE_FRONTIER.md#2026-10-25-ci-cycle-adaptive-valuative-notebookmd), building on the [complete-intersection cycle notebook](CI_CYCLE_DEFORMATIONS_AND_RESIDUAL_GEOMETRY.md#2026-10-25-ci-cycle-geometry-notebookmd). Standard local and intersection-theoretic facts are separated from the proposed organizing viewpoint. Nothing here asserts that every characteristic-zero complete intersection containing the fixed quartic has a residual component. The [independent valuative audit](CI_CYCLE_AUDITS_AND_BOUNDARY_SMOOTHING.md#2026-10-25-ci-cycle-valuative-auditmd) reconstructs the local criterion and the four-line counterexample.

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

A degree-dependent estimate is available, but it is not a bounded-degree solution. Since the actual fixed-quartic ideal is generated in degrees at most 3, as recorded with the explicit generators in the [deformation laboratory](CI_CYCLE_DEFORMATIONS_AND_RESIDUAL_GEOMETRY.md#2026-10-25-ci-cycle-deformation-laboratorymd), choose a general cubic through \(C\) avoiding all components of \(R\). On every normalized residual component its divisor has degree \(3\deg D\) and dominates \(T_D\). Hence

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



---

## 2026-10-25-ci-cycle-endpoint-valuations.md

# Endpoint valuations: contact fans, flags, and adaptive comparisons

Date: 2026-10-25. **Exploratory contribution; provisional and not canonically promoted.** This note responds to the broader investigation of complete-intersection cycles containing the fixed rational quartic. Its worked calculations concern the distinguished pair and two elementary local models; the proposed adaptive framework is not a theorem for arbitrary pairs.

The fixed characteristic-zero geometry is

\[
C=[s^4:s^3t:st^3:t^4],\qquad
F=x_1^4-x_0^3x_3,\quad G=x_2^4-x_0x_3^3,
\quad Z=V(F,G).
\]

The prescribed decomposition and its characteristic-two coalescence are the promoted input [STCI-R-0021](../results/quartic_mu4_degeneration.md), with its [source calculation](2026-10-23-quartic-characteristic-conormal.md). This note uses that geometry without reopening its verification. The actual partial-splitting family below is developed in [the deformation laboratory](CI_CYCLE_DEFORMATIONS_AND_RESIDUAL_GEOMETRY.md#2026-10-25-ci-cycle-deformation-laboratorymd), Section 4. The accompanying [conductor/topology note](CI_CYCLE_PENCILS_AND_SPECIALIZATION.md#2026-10-25-ci-cycle-conductor-topologymd) supplies the genus ledger.

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

This gives a concrete decorated contact tree. Before separation all four branches share the path; after separation their positions on the exceptional \(\mathbf P^1\) carry extra information such as a cross-ratio. The weight fan records the break at three but does not record that cross-ratio. One must retain the initial polynomial at the wall, or the four marked points on the exceptional curve. The [root-pencil note](CI_CYCLE_PENCILS_AND_SPECIALIZATION.md#2026-10-25-ci-cycle-root-pencilmd) develops the corresponding elliptic modulus.

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

## 9. How to make the comparison adapt to an arbitrary pair

The computations suggest a procedure rather than a universal metric.

- **Start generically along \(C\).** Retain the actual two-generated ideal in the two-dimensional regular transverse local ring over \(K=k(C)\). Determine its finite colength \(m_C\), or enough filtered information to bound it. Record the actual ideal, not only the normal orders of its chosen generators.
- **Inspect exceptional directions.** Blow up the smooth center \(C\) in the ambient threefold, and examine the transformed ideal on the normal-direction bundle. Common directions, cancellation loci, and endpoint degeneracies identify where a refinement is needed.
- **Choose points and flags from the pair.** Refine at points where coefficients vanish or initial equations acquire common factors. A direction may require a residue-field extension; that is geometric data to record, not a reason to pretend the direction was globally rational.
- **Follow until branches separate or thickness is certified.** Use further blowups, weighted valuations, residue polynomials, or a local standard basis. Keep branch multiplicity separate from pairwise contact and from curvature relative to coordinates.
- **Return to the global cycle.** For an actual proper degree-\((a,b)\) pair, the residual cycle has degree \(ab-4m_C\). A local profile is useful only insofar as it controls this number or locates actual residual components. Exceptional valuations and endpoint defects do not automatically contribute positive residual degree downstairs.

This is compatible with a broad eventual aim of detecting positive residual degree for arbitrary proper characteristic-zero pairs, while allowing the chosen valuation or flag to depend on the pair. The present calculations do not establish such a detector, a uniform list of flags, or a global inequality for the residual degree.

There is a constructive nuance about how much valuative information could suffice. Values on *all* valuations determine the integral closure of an ideal, whereas an arbitrary ideal's colength is not generally determined by its integral closure. In the generic transverse regular surface, however, the actual two-generated finite-colength ideal is a parameter ideal: its colength equals its Hilbert–Samuel multiplicity, and multiplicity is an integral-closure invariant. Thus one should not conclude from the failure of a single value that a complete valuative approach is impossible. The two multiplicity facts used here are [Huneke–Swanson, *Integral Closure of Ideals, Rings, and Modules*, Proposition 11.1.10(2) and Proposition 11.2.1](https://www.math.purdue.edu/~iswanso/book/SwansonHuneke.pdf). Moreover, each actual ideal has a finite set of ideal-dependent Rees valuations determining the integral closures of all its powers; see [Swanson, *Rees Valuations*, Definition 1.1 and Theorem 2.1](https://www.math.purdue.edu/~iswanso/reesvals.pdf). Thus finite adapted valuative descriptions exist classically, even though their selection, complexity, and global implications are not supplied by the endpoint calculation. The difficult steps are finding effective adapted data and preserving the global degree constraints. This is a structural route to explore, not a worked reconstruction algorithm or an all-pairs bound in this notebook.

## 10. Next experiments that would teach us something

1. For a pair in which neither equation is smooth at an endpoint, compute the full rank-three flag initial ideal on \(\operatorname{Bl}_C\mathbf P^3\). Compare it with a surface reduction when a smooth linear combination happens to exist.
2. Along the root pencil, retain the wall residue polynomial as well as the weight fan. The fan is constant on the open equal-contact stratum, while the four separated directions and their elliptic modulus move.
3. Along the partial-splitting pencil, compare a fixed coordinate fan with the intrinsic two-branch resolution tree. This isolates coordinate curvature from actual inter-branch contact.
4. Test whether a small adaptive set of valuations recovers \(m_C\) in actual low-degree examples with generic orders \((1,r)\), \((2,2)\), and unequal higher terms. Use the full ideal and actual global coefficients; a solution over \(k(C)\) alone is not a global pair.
5. Track the pushforward of strict residual cycles under the refinements. This is the check that prevents vertical exceptional structures from becoming fictitious residual components.

No endpoint profile here has been promoted to an all-pairs extremality principle. The useful outcome is a worked distinction between normal multiplicity, endpoint contact, separated branch positions, coordinate curvature, and exceptional geometry, together with a flexible way to decide what to inspect next.



---

## 2026-10-25-ci-cycle-valuative-multiplicity.md

# Adaptive valuations and the multiplicity spent on the marked curve

Date: 2026-10-25. Exploratory extension of the [complete-intersection-cycle notebook](CI_CYCLE_DEFORMATIONS_AND_RESIDUAL_GEOMETRY.md#2026-10-25-ci-cycle-geometry-notebookmd).

**Question and status.** The curve is the fixed smooth rational quartic
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k\), in characteristic zero. Let \(W=V(F_a,G_b)\) be any proper hypersurface intersection with \(C\subset W_{\mathrm{red}}\). Proper means that the equations have no common surface component. The guiding question is whether valuations adapted to the actual pair can expose a positive residual cycle. The valuation or finite valuation data may depend on \(W\). The distinguished \((4,4)\) intersection is a reference configuration, not a restriction on \((a,b)\).

This note identifies a useful standard-local-algebra bridge and several experiments. It proves no universal residual assertion, changes no canonical record, and leaves the global realization problem explicit. Its examples were independently reconstructed by the `valuative_examples` subagent. A separate audit should test the quantifiers and the completion/residue-field distinctions.

## 1. The global question has an exact local numerical slot

Use the elementary cycle identity in the provisional [residual-cycle audit](OCT21_VALUATIONS_RESIDUAL_CYCLES_AND_Z4.md#source-2026-10-21-residual-cycle-proposition-auditmd):

\[
[W]=m_C[C]+R_W,\qquad \deg R_W=ab-4m_C.
\]

Here \(m_C=\ell(\mathcal O_{W,\eta_C})\), and \(R_W\) is effective without \(C\) as a component. Complete-intersection purity excludes isolated reduced components. Hence the proposed universal residual statement is exactly the strict inequality

\[
\boxed{m_C<ab/4.}
\]

The cycle identity supplies only \(m_C\le ab/4\). Establishing strictness uniformly is the unresolved global task. If \(ab\) is not divisible by four, integrality of \(m_C\) already makes the inequality strict. The difficult numerical boundary occurs when equality is arithmetically possible.

At the generic point of \(C\), the ambient local ring \(A=\mathcal O_{\mathbf P^3,\eta_C}\) is regular of dimension two, with residue field \(K=k(C)\). The localized ideal \((F,G)A\) is maximal-ideal-primary and generated by a regular sequence. Completion preserves its finite length. After choosing a coefficient field and normal parameters, write

\[
R=\widehat A\cong K[[U,V]],\qquad J=(F,G)R.
\]

This coordinate description is a computational choice. Neither the ideal nor its length depends on it. In particular, \(K\) is generally **not algebraically closed**, even when \(k\) is.

## 2. The parameter-ideal hypothesis changes the valuation question

For an ideal \(I\) in a two-dimensional local ring, let \(e(I)\) denote Hilbert–Samuel multiplicity. Two standard facts apply here: a parameter ideal in a Cohen–Macaulay local ring has multiplicity equal to its colength; ideals with the same integral closure have the same multiplicity. Applied to the present regular ring,

\[
\boxed{m_C=\ell(R/J)=e(J)=e(\overline J).}
\]

See [Huneke–Swanson, *Integral Closure of Ideals, Rings, and Modules*, Proposition 11.1.10(2), printed p.225, and Proposition 11.2.1, p.226](https://www.math.purdue.edu/~iswanso/book/SwansonHuneke.pdf).

This supplies the important correction to a possible overreading of the earlier [coefficient-valuation note](INTRINSIC_VALUATIONS_AND_CONTACT_GEOMETRY.md#2026-10-23-intrinsic-coefficient-valuationsmd), section 6, and its [audit](INTRINSIC_VALUATIONS_AND_CONTACT_GEOMETRY.md#2026-10-23-intrinsic-contact-valuations-independent-auditmd), section 5. Their example

\[
J_1=(U^2,V^2),\qquad J_2=(U,V)^2
\]

correctly shows that all ambient scalar ideal values do not recover the colength of an **arbitrary** ideal: the colengths are four and three. For every centered valuation,

\[
v(J_1)=2\min\{v(U),v(V)\}=v(J_2).
\]

But \(J_2\) is not a parameter ideal. Its multiplicity is four, the same as \(J_1\). The example therefore does not show failure to recover colength **within the class of parameter ideals in this fixed regular local ring**. On that class colength is multiplicity, which integral closure retains.

This is a refinement of scope, not a claim that valuations recover the entire Artinian scheme. For example, distinct parameter ideals with the same integral closure can have different equations and gluing data while having equal colength. Nor should ambient valuations be confused with valuations of the Artinian quotient itself: the latter kill nilpotents. The ambient valuations evaluate the defining ideal before quotienting.

## 3. Exact quantifiers: all valuations, a finite adapted set, and one test

For a valuation nonnegative on \(R\), set

\[
v(J)=\min\{v(F),v(G)\}.
\]

The valuative criterion describes \(\overline J\) using all such valuations. More economically, there is a finite set of normalized divisorial **Rees valuations** \(v_1,\ldots,v_r\) satisfying, for every \(n\ge1\),

\[
\overline{J^n}
=\{h\in R:\ v_i(h)\ge n\,v_i(J)\text{ for all }i\}.
\]

The valuations are actual valuation maps on the fraction field, not just an unlabeled list of positive integers. Their construction uses the normalized blowup; see [Huneke–Swanson, Definition 10.1.1 and Theorem 10.2.2, printed pp.195–201](https://www.math.purdue.edu/~iswanso/book/SwansonHuneke.pdf).

Combining this with the parameter-ideal identity gives the precise local conclusion:

\[
\forall W\quad\exists\text{ a finite adapted valuation description determining }m_C.
\]

This is a completeness statement for computing one local multiplicity. It does **not** give

\[
\forall W\quad\exists v\quad
\text{a specified inequality in }v\text{ proving }m_C<ab/4.
\]

The latter needs a useful comparison functional and global degree constraints. There is no general reason that a single scalar value must provide it. A finite cluster, a divisor on a resolution, or the volume of a valuative filtration can be the adaptive witness instead.

The minimal Rees list can be much smaller than the full sequence of infinitely near points. Conversely, knowing values at a handful of plausible valuations does not certify that one has the complete Rees list. Completeness or a valid one-sided comparison must be proved.

## 4. A finite contact tree whose quadratic energy is multiplicity

Put \(I=\overline J\). Resolve its base points by successively blowing up closed points on the regular surface \(\operatorname{Spec}R\). For each infinitely near base point \(P\), including the original point, let

\[
r_P=\operatorname{ord}_P(I^P),\qquad
d_P=[\kappa(P):K],
\]

where \(I^P\) denotes the **weak transform**, with accumulated exceptional factors removed. Only finitely many \(r_P\) are nonzero. These orders are not the raw total-transform values \(v_{E_P}(I)\); the proximity relations connect the two kinds of numbers.

For a complete ideal, the Hoskin–Deligne formula is

\[
\ell(R/I)=\sum_P d_P\binom{r_P+1}{2}.
\]

Complete ideals have complete products, and transforms preserve products. Apply the formula to \(I^n\), whose point orders are \(nr_P\), and compare the coefficient of \(n^2/2\). This yields

\[
\boxed{e(I)=\sum_P d_P r_P^2.}
\]

The required facts, including residue-field weights and finite support, are recalled in [Lipman, *Adjoints and polars of simple complete ideals in two-dimensional regular local rings*, section 1, especially (1.2.2)](https://www.math.purdue.edu/~jlipman/papers/polars.pdf). The same formula appears in [Huneke–Swanson, Theorem 14.5.4, printed pp.285–286](https://www.math.purdue.edu/~iswanso/book/SwansonHuneke.pdf).

Thus the marked-curve multiplicity can be pictured as the quadratic energy of a finite contact tree:

\[
\boxed{m_C=\sum_P d_Pr_P^2,\qquad
\deg R_W=ab-4\sum_P d_Pr_P^2.}
\]

The second equation is the old cycle identity with a valuative computation substituted into it. No strict inequality has been gained merely by rewriting it.

On a principalizing model one can equivalently write \(I\mathcal O_X=\mathcal O_X(-D)\), with \(D\) exceptional. In the orthogonal basis of total transforms of exceptional divisors, \(D=\sum r_PE_P^*\), and the weighted intersection calculation gives \(-D^2=\sum d_Pr_P^2\). This is a useful geometric way to retain the whole cluster; it must not be replaced by the unweighted sum of squares of coefficients in the basis of strict exceptional curves.

## 5. Even every fixed-coordinate monomial valuation can miss the tree

The following local family is a direct calculation, independently checked in this investigation:

\[
J_N=(y-x^2,x^N)\subset K[[x,y]],\qquad N\ge2.
\]

Eliminating \(y\) gives \(R/J_N\cong K[[x]]/(x^N)\), so its length and multiplicity are \(N\). For **every** positive monomial weight valuation in the original coordinates, with \(v(x)=a\), \(v(y)=b\),

\[
v(J_N)=\min\{b,2a,Na\}=\min\{b,2a\}.
\]

This is independent of \(N\). Enlarging a fixed menu to all monomial weights in those coordinates therefore still misses arbitrarily long contact.

The adapted change \(z=y-x^2\) exposes the complete ideal \((z,x^N)\). Its single Rees valuation has weights \(v(x)=1\), \(v(z)=N\), and value \(N\) on the ideal. It can distinguish two members with different \(N\). Its cluster consists of \(N\) successive rational points, each with order one, giving energy \(N\).

This example supports the adaptive program strongly. The missing information is not irretrievably invisible to valuations; it lies in valuations following a nonlinear cancellation direction. The original coordinates did not follow the common branch far enough.

These are formal local examples. They do not show that globally homogeneous pairs of prescribed degrees on the fixed quartic can realize arbitrary \(N\).

## 6. Why the residue-field degree cannot be dropped

Let \(K=k(t)\), with characteristic zero, and put

\[
f=y^2-tx^2,\qquad J=(f,x^n),\qquad n\ge3.
\]

The quotient is free of rank two over \(K[[x]]/(x^n)\), with basis \(1,y\), so \(\ell(R/J)=e(J)=2n\). The quadratic tangent polynomial has two conjugate directions over \(L=K(\sqrt t)\), but a single degree-two point over \(K\).

In the blowup chart \(y=xv\), divide by the common exceptional factor \(x^2\). The weak ideal is

\[
(v^2-t,x^{n-2}).
\]

It is supported at the degree-two closed point with parameters \(x,w=v^2-t\). The cluster has order two at the original point and order one at each of \(n-2\) subsequent points with residue field \(L\). Therefore

\[
\sum_Pd_Pr_P^2=4+2(n-2)=2n.
\]

Omitting degrees gives \(n+2\), which is wrong.

There is also an explicit closure calculation:

\[
\overline J=(f,\mathfrak m^n)=(f,x^n,x^{n-1}y).
\]

The added generator is integral because

\[
(x^{n-1}y)^2=x^{2n-2}f+t x^{2n}\in J^2.
\]

The last adapted divisorial valuation has \(v(x)=v(y)=1\) and \(v(f)=n\). Its threshold ideal \(\{h:v(h)\ge n\}\) is exactly \((f,\mathfrak m^n)\): reduce modulo \(f\) to \(A(x)+yB(x)\); the residue coefficients \(1,\sqrt t\) are independent over \(K\), so their lowest terms cannot cancel. This verifies that the displayed ideal is integrally closed. Its colength is \(2n-1\), whereas its multiplicity and the parameter-ideal colength are \(2n\).

For \(n=3\), the original ideal has colength six, its closure has colength five, and both have multiplicity six. This is exactly the distinction the parameter-ideal bridge needs.

One can instead extend scalars to split the finite cluster. Since the quotient is finite-dimensional, its dimension is unchanged under field extension. Over a splitting field the degree-two chain becomes two conjugate rational chains; counting both gives the same energy. An unannounced passage to an algebraic closure followed by counting only one branch loses the factor two.

## 7. Multiplicity as volume, rather than one favored scalar

The finite Rees data define a filtration

\[
\mathcal I_n=\{h:v_i(h)\ge n v_i(J)\ \forall i\}
=\overline{J^n}.
\]

The same multiplicity can be read from its asymptotic colength:

\[
m_C=\lim_{n\to\infty}\frac{2}{n^2}\ell(R/\mathcal I_n).
\]

In adapted monomial situations this is twice a Newton-polygon complement area. For \((z,x^N)\), the complement triangle has intercepts \(N\) and one, and area \(N/2\). The area recovers multiplicity \(N\). In the original coordinates of the preceding example, the coarse monomial Newton data only saw \((y,x^2)\); the adapted tree explains the missing area.

For general ideals, the volume is encoded by the full valuative inequalities rather than a single polygon in a predetermined coordinate chart. This suggests a flexible notion of proximity: normalize the contact-tree energy by \(ab/4\), while retaining the tree and the degree constraints producing it. Numerically it is the previously defined cycle fraction \(4m_C/(ab)\), but its decomposition into contact directions may explain why a pair is or is not close to using all its degree along \(C\).

## 8. The direction of estimates matters

An unfinished cluster gives a **lower** bound for \(m_C\): all omitted terms \(d_Pr_P^2\) are nonnegative. Consequently it gives an upper bound for residual degree. This alone cannot establish positive residual degree. A certificate of strict positivity needs an upper bound on \(m_C\), or the complete exact energy.

Likewise, retaining only some valuation inequalities gives an ideal \(L\supset\overline J\). Its multiplicity satisfies \(e(L)\le e(J)\), again a lower bound on the multiplicity one wants to bound above. More valuations improve exact reconstruction, but do not automatically create the desired direction of inequality.

A useful opposite comparison is to find a known ideal \(H\subset\overline J\). Then

\[
e(J)\le e(H).
\]

For example, if an adapted parameter ideal \(H=(u^r,v^s)\) is certified to lie in \(\overline J\), then \(m_C\le rs\); a strict inequality \(4rs<ab\) would certify residual degree. Containment can be tested by the full Rees inequalities of \(J\). Choosing such an \(H\) effectively from the homogeneous pair is a genuine new experiment, not a conclusion of the general valuative criterion.

There is no total ordering of complete ideals by multiplicity. Two noncomparable integral closures can have the same energy. A valuation separating one ideal from another does not by itself order their multiplicities. The comparison ideal and containment direction must be stated.

## 9. Point-centered information detects a different phenomenon

The generic cluster computes the coefficient of \(C\) in the global cycle. It does not record where residual components meet \(C\). Near a point \(p\), choose completed coordinates \(k[[t,x,y]]\), with \(C=(x,y)\), and a transverse slice \(t=0\). If the slice ideal is maximal-ideal-primary, its colength

\[
\lambda_p=\ell\bigl(k[[x,y]]/(F(0,x,y),G(0,x,y))\bigr)
\]

is again the multiplicity of a parameter ideal. It can therefore be reconstructed by a separate two-dimensional cluster on that slice. The audited local criterion in [valuative standard-basis test](OCT21_VALUATIONS_RESIDUAL_CYCLES_AND_Z4.md#source-2026-10-21-valuative-standard-basis-criterionmd) distinguishes \(m_C\) from the total generic rank of the formal local curve. Under its finite-slice hypotheses, \(\lambda_p-m_C\) counts the positive contributions of residual formal branches through \(p\). An infinite slice length falls outside the finite multiplicity calculation and signals a different dimension situation.

The slice, the coefficient field, and the localization at the marked generic factor must remain explicit. In particular, \(k[[t,x,y]][1/t]\) is not \(k((t))[[x,y]]\); the latter isolates a completed local factor. Also, a point-centered valuation of the three-dimensional ambient ring is not automatically one of the generic two-dimensional Rees valuations. Its residue and center must be tracked.

For the distinguished characteristic-zero pair, the generic ideal is just the maximal ideal, with energy one. The interesting endpoint contact is in the point-centered comparison, where the transverse slice has length four. In characteristic two the generic energy becomes four. This is a useful reference for distinguishing residual branches near a point from transverse thickness along the entire curve; it supplies no universal bound for other pairs.

## 10. Experiments that the bridge now makes reasonable

1. **Build the actual finite cluster for selected pairs.** Start from global homogeneous \(F,G\), localize at \(\eta_C\), follow cancellation directions, and certify termination. Record field extensions, orders, proximity, and the exact energy. Compare its decomposition with the residual degree already visible geometrically.
2. **Study degree costs of long chains.** The family \((y-x^2,x^N)\) shows that long contact is locally easy. Ask what extra global degree, poles, or transition functions are required to realize an analogous chain along the fixed quartic. Keep actual \(k\)-coefficient forms distinct from free coefficients in \(k(C)\).
3. **Search for adapted comparison ideals.** Instead of a single universal metric, choose \(H_W\subset\overline{J_W}\) with computable energy and try to control that energy by \((a,b)\). A successful strict bound would need independent global input.
4. **Spread a generic cluster over an open subset of \(C\).** Track exceptional directions as finite covers or sections, and record the finitely many places where the model degenerates. Pole and conductor data may connect generic energy to point-centered excess. No flatness of such a spread is assumed in advance.
5. **Compare configurations with equal energy.** The full cluster can distinguish chains, split directions, conjugate directions, and branching even when \(m_C\) agrees. This is a richer geometric comparison than a scalar proximity score.

The local conclusion is substantial but carefully bounded: **complete adaptive ambient valuation data determine the generic multiplicity of every proper complete-intersection pair along \(C\)**. The missing global implication is to show that the resulting weighted energy is always strictly below \(ab/4\) in characteristic zero. This note does not claim that implication, an effective uniform bound, or global realizability of its formal examples.



---

## 2026-10-25-ci-cycle-root-collision-valuations.md

# Two arithmetic scales in the root pencil: a collision tree near a = 4

Date: 2026-10-25. **Exploratory continuation, not canonically promoted.**
This is a selective calculation in the actual fixed-\(C\) pencil from
[the root-pencil note](CI_CYCLE_PENCILS_AND_SPECIALIZATION.md#2026-10-25-ci-cycle-root-pencilmd). It explores a
valuative picture of proximity and uses no accepted STCI obstruction.
The established mixed-characteristic reference configuration is exactly
[STCI-R-0021](../results/quartic_mu4_degeneration.md); its proof is not rerun.

## 1. The experiment and its three distinct scales

Retain
\[
F=x_1^4-x_0^3x_3,\quad
G_a=x_2^4-a x_1x_2x_3^2+(a-1)x_0x_3^3.
\]
Over a complete rank-one valued field \(K\) of characteristic zero with
residue characteristic two, write
\[
\varepsilon=a-4,\qquad h=v(2)>0,\qquad
\gamma=v(\varepsilon)>0.
\]
Extend the valuation to an algebraic closure when discussing roots. We
initially exclude \(\varepsilon=0\) and the two residual discriminant
parameters, so the four geometric roots are distinct. Odd rational
integers are units. The root coordinate \(\lambda=1+w\) gives
\[
f_a(1+w)=w\bigl(w^3+4w^2+6w-\varepsilon\bigr).
\tag{1}
\]
The marked curve \(C\) is \(w_0=0\). The other three sheets correspond to
the roots of the cubic in parentheses. Since all their valuations below
are positive, every \(\lambda=1+w\) is a unit and all four generic
components are smooth conjugate quartics.

There are two arithmetic scales: \(h\), the size of the prime two, and
\(\gamma\), proximity of the pencil parameter to the characteristic-zero
double-\(C\) member. A local endpoint parameter later introduces a third,
horizontal scale. These should be recorded separately before any weighted
sum is chosen.

The standard Newton-polygon rule reads root valuations, counted with
multiplicity, from negative slopes and horizontal lengths of the lower
hull; see [Sharifi, Algebraic Number Theory, Proposition 5.4.11](https://math.ucla.edu/~sharifi/notes/algnum-ch05.html).
Everything specific to this pencil is calculated below.

## 2. First break: which sheets approach the marked curve fastest?

The Newton points of the residual cubic are
\[
(0,\gamma),\quad(1,h),\quad(2,2h),\quad(3,0).
\]
The point \((2,2h)\) never contributes a lower-hull vertex. The first break
is at \(\gamma=3h/2\):

| Parameter scale | Valuations of the three differences from the marked root |
| --- | --- |
| \(0<\gamma<3h/2\) | \(\gamma/3,\gamma/3,\gamma/3\) |
| \(\gamma=3h/2\) | \(h/2,h/2,h/2\) |
| \(\gamma>3h/2\) | \(\gamma-h,h/2,h/2\) |

The sum is always \(\gamma\), as it must be from the constant coefficient
\(-\varepsilon\). Above the break, label the uniquely closest root
\(w_1\), so \(v(w_1)=\gamma-h\), and call the other roots \(w_2,w_3\).

The critical equality does **not** produce a residue collision. To see
this, choose \(t^2=2\), divide the cubic at \(w=tz\) by \(t^3\), and reduce.
The result is
\[
\bar z^3+\bar z+\beta,\qquad
\beta=\overline{\varepsilon/t^3}\ne0.
\]
Its derivative is \((\bar z+1)^2\), but its value at \(\bar z=1\) is
\(\beta\ne0\). Thus the residual cubic has three distinct nonzero roots.
All six pairwise differences among \(0,w_1,w_2,w_3\) have valuation
\(h/2\) at this equality. Below it, the reduced equation after scaling is
\(z^3-\beta\), also separable in residue characteristic two; all six
pairwise differences then have valuation \(\gamma/3\).

This corrects a tempting first guess: a change in Newton slopes need not
be a collision of residual roots. Here the tree changes from four equal
branches to two closer pairs only *after* the first break.

## 3. Second break: a residual pair can collide independently of C

The first Newton polygon does not determine the mutual separation of
\(w_2\) and \(w_3\). Above the first break, they share a leading residue.
Their discriminant supplies the missing coordinate. Set
\[
B(\varepsilon)=-288-176\varepsilon-27\varepsilon^2.
\tag{2}
\]
This is both the discriminant of the residual cubic and the factor
\(-27a^2+40a-16\) of the quartic discriminant. In particular
\[
\operatorname{disc}(f_a)=\varepsilon^2B(\varepsilon).
\tag{3}
\]
The three terms in (2) have valuations
\[
5h,\qquad4h+\gamma,\qquad2\gamma.
\]
The middle term is never minimal. Therefore
\[
v(B)=
\begin{cases}
2\gamma,&\gamma<5h/2,\\
5h,&\gamma>5h/2,
\end{cases}
\tag{4}
\]
whereas at \(\gamma=5h/2\) cancellation may increase \(v(B)\).

For \(\gamma>3h/2\), put \(\delta=v(w_2-w_3)\). The two differences
\(w_1-w_2,w_1-w_3\) have valuation \(h/2\), so the cubic discriminant gives
\[
v(B)=2(h+\delta),\qquad
\delta=\frac{v(B)}2-h.
\tag{5}
\]
Thus the full collision pattern is:

| Region | Marked pair depth \(v(w_1-w_0)\) | Other pair depth \(\delta\) | Cross-pair depth |
| --- | --- | --- | --- |
| \(3h/2<\gamma<5h/2\) | \(\gamma-h\) | \(\gamma-h\) | \(h/2\) |
| \(\gamma=5h/2\) | \(3h/2\) | \(v(B)/2-h\ge3h/2\) | \(h/2\) |
| \(\gamma>5h/2\) | \(\gamma-h\) | \(3h/2\) | \(h/2\) |

The marked pair and the other pair initially deepen at the same rate.
Beyond the second break, only the marked pair continues to deepen for a
parameter approaching zero \(\varepsilon\); the other pair stabilizes.
But in a different parameter direction through the critical shell,
the *residual* pair can deepen arbitrarily while the marked pair stays
at depth \(3h/2\). This is an actual distinction between concentration
onto \(C\) and collisions elsewhere in the residual curve.

A schematic tree above the first break is

```text
all four roots, common depth h/2
  ├── {marked root 0, w1}: additional depth (gamma-h) - h/2
  └── {w2, w3}:             additional depth delta - h/2
```

Depth is a valuation of a coordinate difference. No choice of a global
metric on the ambient projective space is being asserted.

## 4. The exceptional shell retains residue information

At \(\gamma=5h/2\), use \(t^2=2\) and write
\(\varepsilon=t^5e\), with \(e\) a unit. After dividing (2) by \(t^{10}\),
the residue is
\[
\overline{B/t^{10}}=\bar e^2+1=(\bar e+1)^2.
\]
Thus \(\bar e\ne1\) gives \(v(B)=5h\); the residue \(\bar e=1\) requires
further terms and can give deeper collisions. If the residue field is
\(\mathbf F_2\), every unit has residue one, so cancellation on this
critical shell is automatic. A generic noncancelling residue exists
after a suitable residue-field extension.

An explicit ramified example is
\(K=\mathbf Q_2(\sqrt2)\), \(h=1\),
\(\varepsilon=4\sqrt2\), so \(\gamma=5/2\). Then
\[
B=-1152-704\sqrt2,\qquad v(B)=13/2,
\]
because the summands have distinct valuations \(7\) and \(13/2\).
Consequently the residual-pair depth is \(\delta=9/4\), larger than the
naive \(3/2\) value on the critical shell.

More precisely, the two zeros of \(B\) are
\[
\varepsilon_\pm=
\frac{-88\pm4\sqrt{-2}}{27}.
\]
Each has valuation \(5h/2\), while
\(v(\varepsilon_+-\varepsilon_-)=7h/2\). Writing
\(r_\pm=v(\varepsilon-\varepsilon_\pm)\), one has the exact refinement
\[
v(B)=r_++r_-,\qquad
\delta=\frac{r_++r_-}{2}-h.
\tag{6}
\]
Away from the zeros themselves these numbers are finite. If one distance
is below \(7h/2\), both distances equal that smaller value. If one exceeds
\(7h/2\), the other is \(7h/2\). At equality the residue of the next
coefficient matters again. This describes the full critical-shell
refinement in terms of the actual two discriminant points, rather than
pretending that \(\gamma\) alone determines the tree.

At \(\varepsilon=\varepsilon_\pm\), the residual pair is genuinely double;
at \(\varepsilon=0\), the marked pair is double instead. These are
separate characteristic-zero strata in the same arithmetic neighborhood.

## 5. Recovering the fourth roots of unity and the elliptic marker

The original \(\mu_4\) member has \(a=0\), hence \(\varepsilon=-4\) and
\(\gamma=2h\). The marked differences are
\[
-2,\quad i-1,\quad-i-1,
\]
with valuations \(h,h/2,h/2\); the other close pair has difference \(2i\)
and depth \(h\). Thus the two pairs have equal depths. The derivative
budget is \(h+h/2+h/2=2h=v(4)\), and the full quartic discriminant has
valuation \(8h=v(-256)\), as predicted by (3).

For \(\gamma>3h/2\), choose the cross-ratio adapted to the two pairs,
\[
x=\frac{(w_0-w_1)(w_2-w_3)}{(w_0-w_2)(w_1-w_3)}.
\]
Its depth is
\[
\ell=v(x)=\gamma+\delta-2h>0.
\tag{7}
\]
This combines the two short-pair depths after subtracting the common
cluster depth. The elliptic double cover from the root-pencil note has
\[
j=256\frac{(1-x+x^2)^3}{x^2(1-x)^2}.
\]
Since \(v(x)>0\), the factors \(1-x\) and \(1-x+x^2\) are units. Therefore
\[
v(j)=8h-2\ell
=14h-v(\operatorname{disc}f_a).
\tag{8}
\]
The second equality also follows directly from the exact pencil formula
for \(j\), since \(a-1\) is a unit in this neighborhood.
At the \(\mu_4\) member \(\ell=h\) and \(v(j)=6h\), agreeing with
\(j=1728\). This is a useful consistency bridge between a root-collision
tree and the coarse elliptic modulus. We do not infer a model of stable
reduction or a reduction type from this numerical identity alone.

## 6. Endpoint contact adds a horizontal contribution

Near \(p\), a branch has transverse coordinate \(Y=w u^3\) relative to
\(C\). If an endpoint valuation assigns \(v(u)=\alpha\ge0\), then
\[
v(Y_i-Y_j)=v(w_i-w_j)+3\alpha.
\tag{9}
\]
The first-normal determinant is \(-\varepsilon u^9\), and its valuation
is exactly
\[
\gamma+9\alpha
=\sum_{i=1}^3\bigl(v(w_i)+3\alpha\bigr).
\tag{10}
\]
The full local quartic discriminant similarly has valuation
\(v(\operatorname{disc}f_a)+36\alpha\). These equations separate
arithmetic coalescence of coefficients from the order-three geometric
contact at the endpoint.

At the other endpoint, the leading coefficients are \(\lambda^{-3}\).
They are obtained from the first endpoint by
\[
\lambda\longmapsto\frac{\lambda}{a\lambda+1-a}.
\]
In the present neighborhood its determinant \(1-a\) and all denominators
\(\lambda^4\) are units. Hence it preserves every pairwise valuation of
the coefficient differences. The same arithmetic collision tree occurs
at both endpoints, with the local horizontal factor then added as in
(9). This agreement is stronger than equality of the two elliptic
\(j\)-invariants.

## 7. What this suggests, and the next experiment

A single marked determinant records the sum \(\gamma\) and misses how it
is distributed among the three residual sheets. The first Newton polygon
recovers those three individual depths, but misses an independent
residual-pair collision. Adding the discriminant and its residue data
recovers that next layer. The tree, rather than one number, is therefore
a concrete candidate organizing object for a neighborhood of this family.

It is particularly suggestive that approaching the double-\(C\) member
and approaching a residual double-sheet member deepen different branches
of the same tree. The \(\mu_4\) configuration occupies an intermediate
balanced-pair pattern. This balance does not isolate it: the entire
region \(3h/2<\gamma<5h/2\) has equal pair depths. Unit and higher
residue data, which the exact cross-ratio retains, still distinguish
configurations. This is a useful geometric picture of symmetry, not a
global extremality assertion.

The [stdlib experiment](../computations/verify_ci_cycle_root_collision_valuations_2026_10_25.py)
and [JSON output](../computations/ci_cycle_root_collision_valuations_2026_10_25.json)
record exact rational lower hulls and budget checks. Reproduce with
`python3 research/computations/verify_ci_cycle_root_collision_valuations_2026_10_25.py research/computations/ci_cycle_root_collision_valuations_2026_10_25.json`.
The computation does not approximate algebraic roots or decide residue
cancellation; those distinctions are explicit in the formulas above.

**Review boundary.** The primary agent independently reconstructed the Newton hull, the two thresholds, the discriminant coefficients, the exceptional example in \(\mathbf Q_2(\sqrt2)\), and the cross-ratio valuation identity, and replayed all fifty finite checks. The separate valuative audit concerns the earlier local framework; it does not claim an additional independent review of this later collision experiment. These calculations remain exploratory and unpromoted.

Next one could perturb the pencil by a second actual quartic in
\(I_C(4)\), compute the local transverse Weierstrass polynomial, and ask
whether the marked collision tree, endpoint determinant, and residual
discriminant form compatible charts on a larger deformation space.
A failure would be informative: moving branch points, nonmonic
presentations, or changing carriers can make the chosen root coordinate
inadequate. No unrestricted ordering of complete intersections, stable
model, or canonical promotion is claimed here.

