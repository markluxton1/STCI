# Adaptive valuative comparisons with multiples of the quartic

Date: 2026-10-25. **Exploratory continuation of the complete-intersection cycle notebook.** New deductions and proposed comparison principles remain provisional; independent review is recorded in the [valuative audit](2026-10-25-ci-cycle-valuative-audit.md). No general residual-component theorem is claimed.

## 1. The clarified goal and its quantifiers

Fix the embedded smooth rational quartic
\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k,
\]
over an algebraically closed field of characteristic zero. Consider actual homogeneous forms \(A,B\in I_C\), of degrees \(d,e\), with no common surface component. Their intersection \(W=V(A,B)\) is a pure complete-intersection curve. Decompose its fundamental cycle as
\[
[W]=m[C]+R,\qquad C\not\subset\operatorname{Supp}(R).
\]
The eventual goal is that \(R\ne0\) for every such pair. The proper-intersection hypothesis is necessary to discuss an ordinary complete-intersection curve cycle: hypersurfaces with a common surface require an excess-intersection formulation.

“More than \(C\)” here means a component away from \(C\), not merely a coefficient \(m>1\). The unresolved possibility is an intersection supported on \(C\) with its entire degree carried by a multiple structure.

The guiding idea is to use the distinguished \((4,4)\) cycle \(Z\) as a reference configuration unusually close to a multiple of \(C\). **There need not be one distance function.** Different cycles may admit different comparisons: generic valuations, a point of \(C\), a cluster of infinitely near points, or a boundary and its residue algebra. What should remain common is the geometric conclusion being certified.

Thus the useful quantifier is potentially
\[
\forall W\quad\exists\text{ an appropriate geometric or valuative certificate for }W.
\]
It need not be a single valuation, a predetermined finite list, or one scalar score valid for every \(W\). At present this is a research program, not an established covering of all pairs by certificates.

## 2. The degree budget gives a common destination for different measures

For every proper pair, Bézout and purity give
\[
de=4m+\deg R.
\]
Consequently
\[
R\ne0\quad\Longleftrightarrow\quad m<\frac{de}{4}.
\]
This elementary identity is recorded, with its distinction from conditional auxiliary-surface results, in the [residual-cycle note](2026-10-21-residual-cycle-proposition-audit.md) and its [reconciliation](../RECONCILIATION_2026-10-23-VALUATIONS.md).

The integer \(m\) has an exact local meaning. If
\[
S=\mathcal O_{\mathbf P^3,\eta_C},\qquad J=(A,B)S,
\]
then \(S\) is a regular local ring of dimension two and \(J\) is primary to its maximal ideal. The coefficient of \(C\) is
\[
m=\operatorname{length}_S(S/J).
\]
Therefore a geometric comparison can prove residual existence by giving a sufficiently small upper bound for this generic transverse length. Alternatively it can exhibit a point where a residual branch must occur. These are compatible routes to the same conclusion.

For the reference \(Z\), characteristic zero gives \(m=1\), \(de=16\), and residual degree twelve. The difficult general question is not this computation; it is what prevents other pairs, of arbitrary degrees, from spending their whole budget on \(C\).

## 3. Generic valuations have more power on parameter ideals than on arbitrary ideals

Here the two-equation hypothesis matters. Because \(J\) is a parameter ideal in a Cohen–Macaulay local ring,
\[
m=\operatorname{length}(S/J)=e(J),
\]
where \(e\) is Hilbert–Samuel multiplicity. Multiplicity is unchanged by integral closure:
\[
m=e(\overline J).
\]
The integral closure is determined by ideal values of divisorial valuations centered on the maximal ideal of \(S\). In this excellent setting a certified full set of Rees valuations is finite. Thus sufficiently complete valuative data determines the generic multiplicity of an actual complete-intersection pair.

This refines an earlier warning in the repository. The ideals
\[
(U^2,V^2)\quad\text{and}\quad(U^2,UV,V^2)
\]
have the same integral closure and the same values for every valuation, but colengths four and three. That remains a valid warning for arbitrary ideals. It does not contradict the present statement: the second ideal is not a parameter ideal, and both ideals have multiplicity four. Restricting to the actual two-generator complete-intersection class recovers precisely the numerical invariant needed for the cycle coefficient.

The [generic valuative multiplicity note](2026-10-25-ci-cycle-valuative-multiplicity.md) supplies primary references, field-of-definition qualifications, and the finite-cluster formula. The point is a standard multiplicity theorem applied to this problem; no novelty claim is made for the theorem.

This suggests a substantial change of viewpoint: **generic transverse multiplicity is a valuative quantity on the relevant class**, even though a few scalar values or a fixed coordinate fan can miss it.

## 4. Adaptation is essential: a simple family missed by every fixed monomial weight

In \(K[[x,y]]\), with \(K=k(C)\), consider the local parameter ideals
\[
J_N=(x-y^2,\ y^N),\qquad N\ge2.
\]
Their colength is \(N\). Yet every positive monomial valuation in the fixed coordinates \(x,y\), trivial on \(K\), gives
\[
v(J_N)=\min\{v(x),\,2v(y),\,Nv(y)\}
=\min\{v(x),\,2v(y)\}.
\]
The answer is independent of \(N\). A whole fixed monomial-weight fan cannot recover the multiplicity.

Now follow the actual smooth branch \(x-y^2=0\). In the adapted coordinates
\[
X=x-y^2,\qquad y=y,
\]
the ideal is \((X,y^N)\). Its integral closure, Newton polygon, and cluster of infinitely near points reveal \(N\). The divisorial valuation with \(v(y)=1\), \(v(X)=N\) sees a value that changes with \(N\). To compute the length from a valuation one must retain the corresponding valuation itself and the ideal's certified closure data, not just that one numerical value.

These are local models, not asserted global pairs for the quartic. Their use is methodological: let the equations tell us which direction to follow and which valuation to use.

There is a related direction-of-inequality issue. Using only some valuative inequalities generally gives an ideal containing \(\overline J\). Its multiplicity is then a lower bound for \(m\), whereas the degree-budget route needs an upper bound. A finite sample is not automatically a residual-existence certificate. One can instead certify the full closure, compute a complete cluster, or produce a computable ideal contained in \(\overline J\) whose multiplicity already lies below \(de/4\).

## 5. Points of \(C\), normal valuations, and flags

Every point \(p\) of the smooth curve defines the canonical discrete valuation
\[
\operatorname{ord}_p:k(C)^*\longrightarrow\mathbf Z.
\]
This is exactly the intrinsic point valuation suggested by the question.

At the generic point of \(C\), the ambient local ring has dimension two, so it is not itself a DVR. The ordinary transverse order is realized by the exceptional divisor of
\[
\pi:\operatorname{Bl}_C\mathbf P^3\longrightarrow\mathbf P^3.
\]
Further blowups over the generic point of \(C\) produce divisorial valuations adapted to \(J\), including its Rees valuations.

To combine normal order with a point of \(C\), let \(E\) be the exceptional surface and \(E_p\) its fiber over \(p\). The flag
\[
\operatorname{Bl}_C\mathbf P^3\supset E\supset E_p
\]
defines a composite valuation ring. After choosing a suitable splitting, its values can be written as a lexicographically ordered pair: normal order first, then order at the point in the leading residue. The residue field at the end is \(k(E_p)\), retaining a generic normal direction.

This flag is centered at \(p\) on the original threefold. It is not centered on the generic local ring \(S\): a parameter at \(p\) and its inverse are units in \(S\), but the flag assigns them nonzero values. Generic Rees valuations and point-sensitive flags play different roles and require an explicit bridge.

The [earlier coefficient-valuation note](2026-10-23-intrinsic-coefficient-valuations.md), independently reviewed but unpromoted, gives the intrinsic construction and coordinate cautions. Two particularly useful rules are:

- Positive monomial weights in actual regular parameters define valuations. An arbitrary positive real linear combination of the numerical coordinates of a lexicographic flag need not be a valuation.
- Combining \(\operatorname{ord}_p\) with normal weights works for polynomials and controlled series domains. It need not make sense on all of \(k(C)[[U,V]]\), where coefficient poles can grow without bound.

These restrictions leave a large supply of genuine valuations. They tell us to work on a specified model and transport residue data when changing coordinates.

## 6. A cycle-level point witness

There is a useful elementary way to state what an adaptive point measurement should detect. Write \(e_p(W)\) for the ordinary local multiplicity of the curve at \(p\). Associativity of multiplicity gives, because \(C\) is smooth,
\[
e_p(W)=m+\sum_{D\ni p}m_D e_p(D),
\]
where the sum is over residual components.

A positive-dimensional projective complete intersection in \(\mathbf P^3\) is connected. Here this follows directly from the Koszul resolution and vanishing of the intermediate cohomology of line bundles on \(\mathbf P^3\). Thus a nonzero residual cycle must meet \(C\). Consequently, for the present proper-pair setup,
\[
R\ne0
\quad\Longleftrightarrow\quad
\exists p\in C:\ e_p(W)>m.
\]
This is a reformulation and a certificate format, not a proof that such a point exists for every pair.

For \(Z\), \(m=1\) and \(e_p(Z)=e_q(Z)=4\), so the two endpoints witness residual branches immediately. For a general nodal \(C\cup D\), the witnesses are the eighteen attachment points, where \(e_r(W)=2\); the distinguished endpoints can have multiplicity one and detect nothing. This explains precisely why the appropriate measuring points may depend on \(W\).

Ordinary point multiplicity does not record contact order: four branches with pairwise contact three and four branches with distinct tangents can both have multiplicity four. Valuations at infinitely near points retain the distinction.

## 7. A valuative contact divisor attached to the actual residual cycle

Suppose \(R=\sum m_D[D]\). Normalize each integral residual component:
\[
\nu_D:\widetilde D\longrightarrow D.
\]
At a point \(r\) above \(C\), the nonzero ideal \(I_C\mathcal O_{\widetilde D,r}\) is principal in a DVR. Define
\[
c_r(D,C)=\operatorname{ord}_r(I_C\mathcal O_{\widetilde D,r}).
\]
These are genuine branch valuations. Push their weighted sum onto \(C\):
\[
\mathcal B_C(R)=
\sum_D m_D\sum_{r\mapsto C}c_r(D,C)\,[\nu_D(r)].
\]
The field is algebraically closed here; residue-degree weights are needed over a nonclosed field.

This construction uses the actual cycle \(R\), the marked embedding of \(C\), and normalizations of residual components. It does not require \(C\) to be generically simple in \(W\). Equivalently, it is the pushforward to \(C\) of the intersection of \(E\) with the strict residual cycle on \(\operatorname{Bl}_C\mathbf P^3\).

For \(Z\), each of its three residual quartics has order three at each endpoint:
\[
\mathcal B_C(R_Z)=9p+9q.
\]
For a general nodal \(C\cup D\), it is the sum of the eighteen simple attachments. At the root-pencil collision \(a=4\), the residual cycle consists of two quartics, so it becomes \(6p+6q\), even though the first-normal determinant is identically zero.

Thus this valuative divisor continues to make sense in a class where the first-normal boundary no longer does. It is a natural candidate for comparing contact with a multiple of \(C\).

It is not in general the dualizing/conductor boundary. In the local complete intersection of four noncoplanar lines, choose one line as \(C\). The other three lines each contribute one to \(\mathcal B_C\), giving \(3p\); the conductor on the marked normalized line has coefficient two. The [contact-cycle note](2026-10-25-ci-cycle-valuative-contact-cycle.md) calculates this example explicitly. These objects agree for the smooth-surface branch arrangement of \(Z\), but serve different purposes in the broader space-curve problem.

Connectedness also gives
\[
R\ne0\quad\Longleftrightarrow\quad \mathcal B_C(R)\ne0
\]
for these complete intersections. Computing \(R\) first would already solve the detection problem for a given pair. The research challenge is to estimate or recover enough of this contact data from equations, valuations, and global constraints before a full residual decomposition.

The point witness and the contact divisor fit into an effective hierarchy. Put
\[
M_C(W)=\sum_{p\in C}(e_p(W)-m)[p].
\]
On a normalized residual branch with local coordinates \(C=(x,y)\), ordinary branch multiplicity is \(\min\{\operatorname{ord}(u),\operatorname{ord}(x),\operatorname{ord}(y)\}\), whereas its ideal contact is \(\min\{\operatorname{ord}(x),\operatorname{ord}(y)\}\). Thus
\[
M_C(W)\le\mathcal B_C(R).
\]
The fixed quartic's ideal is generated in degrees at most three. A general cubic through \(C\) avoiding the residual components therefore gives
\[
0\le\deg M_C(W)\le\deg\mathcal B_C(R)\le3\deg R
=3(de-4m).
\]
For \(Z\), the first two divisors are \(3p+3q\) and \(9p+9q\). The difference records higher tangency beyond branch multiplicity. Both vanish on a cycle supported entirely on \(C\); the hierarchy supplies no universal positive lower bound by itself.

## 8. The endpoint valuation profile of \(Z\)

Near \(p\), eliminate the smooth carrier equation \(F\) and work with
\[
f(u,Y)=Y\prod_{\zeta\ne1}\bigl(Y-(\zeta-1)u^3\bigr).
\]
A positive monomial valuation on this smooth surface, with
\[
v(u)=\alpha,\qquad v(Y)=\beta,
\]
has
\[
v(f)=\beta+3\min\{\beta,3\alpha\}.
\]
The wall \(\beta=3\alpha\) exposes the three residual branch directions. Below the wall the four branches look compressed into the common tangent; at the wall the residue polynomial separates them. Following successive point blowups reaches this separation after the rays \((1,1),(1,2),(1,3)\).

Compare a pure fourfold marked branch \(Y^4\). For \(\beta>3\alpha\),
\[
v(f)=\beta+9\alpha<4\beta=v(Y^4).
\]
This is a precise local sense in which the residual branches separate sooner than a pure multiple of \(C\). At the critical wall their numerical values agree; the residue polynomial distinguishes four branches from a repeated root. Both values and residues belong in the measuring apparatus.

The normal-first surface flag records \((1,9)\): one copy of \(C\), then nine units of contact at the endpoint. The point-first order is four. These are complementary summaries of the same polynomial.

For the partial-splitting deformation from the first notebook,
\[
f_\lambda=
Y(Y^3+4u^3Y^2+6u^6Y+4u^9-\lambda u),\qquad \lambda\ne0,
\]
the weighted profile is
\[
v(f_\lambda)=\beta+\min\{3\beta,\alpha\}.
\]
The normal-first flag becomes \((1,1)\), and the ordinary point multiplicity becomes two. Contact has left the endpoint and appears at eight moving points.

These surface calculations require the indicated smooth carrier chart. For the ambient ideal \((X,f)\), a scalar ideal value is \(\min\{v(X),v(f)\}\), which may conceal the interesting part. One should retain the quotient by the actual smooth carrier, the full transformed ideal, or sufficiently refined intersection data. A single minimum is not an intrinsic substitute for all of them.

The [endpoint valuation notebook](2026-10-25-ci-cycle-endpoint-valuations.md) develops these pictures and their scope.

The [root-collision continuation](2026-10-25-ci-cycle-root-collision-valuations.md) then follows the actual root pencil near its double-\(C\) member over a field above two. It finds two different thresholds: one for how fast a residual sheet approaches the marked sheet, and another for collision within the residual sheets. The first-normal determinant records their total marked separation but misses that second collision. A full tree with residue information resolves the ambiguity.

## 9. How “closest” might guide adaptive certificates

The reference configuration provides several thresholds at once:

- Its generic transverse multiplicity is one.
- Its endpoint ordinary multiplicity is four.
- Each residual branch separates from \(C\) at contact order three.
- The sum of the residual contact orders is nine at each endpoint.
- Its two endpoint branch configurations have the same harmonic modulus.
- In the prescribed arithmetic model the four sheets collapse to generic length four in characteristic two.

No single one orders every possible intersection. The root-pencil member with double \(C\), for example, has larger generic mass on \(C\) and a smaller residual contact divisor. It is an important test for a proposed notion of closeness, not a reason to abandon the broader idea.

A useful strategy is to ask which feature makes a candidate appear closer to a multiple of \(C\), then choose valuations that resolve that feature. If generic multiplicity is high, inspect its complete cluster. If contact is concentrated at a point, follow that point's blowups. If a numerical value agrees with a pure multiple, compare the initial residue algebra. If a generic normal direction degenerates at a point, use a model retaining both the normal and point valuations.

This suggests a family of local comparison problems rather than a universal scalar minimization. A successful family would cover every actual pair while using the global degrees, twisting, and gluing to rule out an entirely supported multiple. The missing step is that coverage and its global inequality; it is not supplied by the valuative reformulations alone.

## 10. Focused next experiments

1. Compute \(\overline{J_\eta}\), its Rees valuations, and a complete point cluster for a few explicit families. Record \(e(J_\eta)\) separately from \(\operatorname{length}(S/\overline{J_\eta})\).
2. Follow the root pencil toward its double-component member using \(\mathcal B_C(R)\), point multiplicities, and endpoint residue polynomials. Determine which refined comparison survives the zero determinant.
3. In the fourteen-dimensional fixed-boundary fiber, compare the determinant boundary with \(\mathcal B_C(R)\). Locate nonplanar endpoint members where they differ.
4. Seek degree-dependent upper bounds for the complete-cluster multiplicity of actual homogeneous pairs. Keep all coefficient constraints over \(k\); generic formal ideals such as \(J_N\) are tests of a proposed argument, not global realizations.
5. Try a covering by certificate types: independent first symbols; resolved common normal directions; point multiplicity jumps; higher residue splitting. For each type, state its exact hypotheses and the remaining class.

The promoted premises remain the fixed-curve conormal result [R0020](../results/quartic_conormal_characteristic_jump.md) and prescribed degeneration [R0021](../results/quartic_mu4_degeneration.md). The older valuation and residual-cycle notes are used at their provisional/reconciled scope. The new material is an exploratory framework, with independently reviewed local deductions, and does not establish the universal residual claim.
