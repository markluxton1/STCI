# Complete-intersection cycles: consolidated mathematical investigations

Full source mathematical content retained in subject sections. Statements retain their original provisional or audited scope; this compilation does not promote results.


---

## 2026-10-25-ci-cycle-continuation-checkpoints.md

# Complete-intersection cycle exploration: continuation checkpoints

Date: 2026-10-25, America/New_York. This is a working handoff, not theorem authority.

**October 26 instruction update:** the user reopened the usage window and asked to finish the investigations already underway, push the work, and stop. This supersedes the earlier instruction to keep selecting new items until the usage limit. The final current items are the line degeneration, fixed-boundary node smoothing, and endpoint-four actual sextic/fixed-carrier jet test.

## Authorized continuation

The user asked to continue the exploration, then proceed through substantive STCI or other repository items until the five-hour usage limit stops the run. The user also authorized pushing commits at each checkpoint. Publication authorization applies to checkpoint commits; no merge or canonical promotion is inferred.

The active branch is codex/ci-cycle-valuations-2026-10-25, based on commit 59c703c71c1fbac97fc1dc0ddbabadd9ff583a6f. That earlier checkpoint, containing the original cycle notebook and adaptive valuation framework, was already present on the remote branch codex/quartic-flag-duality-2026-10-24 when continuation resumed.

## Checkpoint 1: adaptive valuations and the arithmetic root-collision tree

The [adaptive notebook](#2026-10-25-ci-cycle-adaptive-valuative-notebookmd) now states the clarified all-pairs residual-cycle goal and permits the measuring data to depend on the pair. Its reviewed local bridges are:

- Generic transverse colength equals Hilbert–Samuel multiplicity for the actual two-generator parameter ideal, so sufficiently complete adaptive valuation data recover the coefficient of \(C\).
- Residual existence is equivalent to a pointwise multiplicity jump somewhere on \(C\), using complete-intersection connectedness.
- Normalized residual-branch valuations define a contact divisor, with point-multiplicity excess below it and a cubic degree bound above it.
- This contact divisor is distinct from the conductor boundary in nonplanar germs.

The [root-collision notebook](CI_CYCLE_VALUATIONS_AND_CONTACT.md#2026-10-25-ci-cycle-root-collision-valuationsmd) is the completed concrete continuation. It gives thresholds \(3v(2)/2\) and \(5v(2)/2\), residue-sensitive refinement at the second threshold, and the cross-ratio/elliptic valuation consistency check. The stdlib script and JSON record fifty finite checks. The primary independently reconstructed these calculations; a separate additional audit of this later experiment is not claimed.

The earlier [valuative audit](CI_CYCLE_AUDITS_AND_BOUNDARY_SMOOTHING.md#2026-10-25-ci-cycle-valuative-auditmd) was preserved and its mathematical formatting cleaned. Accepted results and their proofs were not changed or rerun. No universal residual positivity has been proved.

## Publication record

Checkpoint 1 was pushed as a4420cb5d01ca27f09f4e07c0ee8289b8cb14c48. The exact remote branch ref was verified and the checkout was clean immediately after the push.

## Checkpoint 2: exact global smooth residual benchmark

The generic existence argument in the [deformation laboratory](CI_CYCLE_DEFORMATIONS_AND_RESIDUAL_GEOMETRY.md#2026-10-25-ci-cycle-deformation-laboratorymd) is now accompanied by a [fully explicit rational pair](CI_CYCLE_DEFORMATIONS_AND_RESIDUAL_GEOMETRY.md#2026-10-25-ci-cycle-smooth-residual-examplemd) and [independent audit](CI_CYCLE_AUDITS_AND_BOUNDARY_SMOOTHING.md#2026-10-25-ci-cycle-smooth-residual-auditmd). The actual saturated colon ideal has degree twelve and arithmetic genus sixteen. Exact rational Jacobian calculations show it is smooth; its space of global functions is \(\mathbf Q\), so base change gives geometric connectedness and hence geometric integrality. Its attachment scheme has eighteen geometric reduced points and avoids both distinguished endpoints.

The independent standard-library boundary calculation gives a squarefree polynomial of degree eighteen with constant coefficient four and leading coefficient three. The Macaulay2 and Python scripts, JSON, and captured rational output are retained. No finite-field lifting argument is needed.

A preliminary coefficient choice forced the line \(L=V(x_0+x_1,x_2+x_3)\). Its residual has five singular points on that line. This is the next intrinsic geometry item: isolate the degree-eleven component, check its genus and smoothness, and understand the genus redistribution when the line is absorbed in a nearby smooth residual.

The separate [frontier reconnaissance](#2026-10-25-valuative-frontier-next-experimentsmd) identifies two genuinely open STCI followups after that geometry checkpoint: the single-defect nonsaturated degree-\((6,12)\) slice, and an endpoint-four nodal chart of the conditional degree-\((6,16)\) lane. Their exact hypotheses and unresolved global-realization requirements remain explicit. Do not reopen accepted exclusions or treat these candidate experiments as existence/nonexistence results.

Checkpoint 2 was pushed as d856d78078b75ec78d38c8782b9da3a6f9b1c9ab, with the exact remote ref verified.

## Checkpoint 3: line absorption and independent smoothing at fixed boundary

The [line degeneration](CI_CYCLE_DEFORMATIONS_AND_RESIDUAL_GEOMETRY.md#2026-10-25-ci-cycle-line-degenerationmd) and its [audit](CI_CYCLE_AUDITS_AND_BOUNDARY_SMOOTHING.md#2026-10-25-ci-cycle-line-degeneration-auditmd) certify a residual \(L\cup E\), where \(E\) is smooth geometrically integral of degree eleven and genus twelve. There are five simple \(L\)-\(E\) nodes, seventeen \(C\)-\(E\) attachments, and one \(C\)-\(L\) attachment, with no triple points. The moving ruling-line stratum is \(ab=1\) near the chosen parameter. Each node-smoothing parameter is a unit times \(ab-1\); the order-five assertion concerns their product, not every scheme structure called a discriminant.

The [fixed-boundary calculation](CI_CYCLE_AUDITS_AND_BOUNDARY_SMOOTHING.md#2026-10-25-ci-cycle-fixed-boundary-node-smoothingmd), its [independent reconstruction](CI_CYCLE_AUDITS_AND_BOUNDARY_SMOOTHING.md#2026-10-25-ci-cycle-fixed-boundary-node-smoothing-auditmd), and the [October 26 final audit](2026-10-26-ci-cycle-fixed-boundary-node-smoothing-audit.md) give affine ranks \(19,5,24\). On the pencil Grassmannian the exact-boundary fiber has dimension fourteen and maps smoothly to the five marked node parameters, with nine further formal coordinates. The formal/étale local existence statement is reviewed; an explicit polynomial coefficient arc is not claimed.

These two geometric investigations are complete at their stated exploratory scope. Checkpoint 3 was pushed as 15b1806cc174737806fa4b9e2a57f70eab0de374, with the remote ref verified.

## Final checkpoint: actual endpoint-four sextics and a fixed-carrier residual certificate

The [actual-sextic note](2026-10-25-endpoint4-actual-sextics.md) completes the prescribed second-symbol lifting problem on the retained endpoint-four chart, preserving all actual global coefficient constraints and the one-dimensional kernel. It justifies the \(a_0=1\) gauge using the actual \(C\)-preserving torus and its recorded square-root cover. This family construction alone is not a mate-existence or chart-emptiness statement.

For the selected carrier
\[
F_*=-q^2x_3^2-qDx_2+D^2/4+q^3,
\quad q=x_0x_3-x_1x_2,\quad D=x_2^3-x_1x_3^2,
\]
the fixed-carrier M2 certificate and the independent normal-division implementation both pass: the \(690\times969\) matrix has rank \(683\), and all \(286\) actual global multiples \(F_*H_{10}\) are annihilated. The known-multiple guard caught an M2 multiline-assignment error during development; that error was corrected before the final certificates passed. The failure mechanism and final source/output hashes are retained.

The [independent nonsplit-node audit](2026-10-26-endpoint4-nonsplit-node-scope-audit.md) supplies the bridge from that jet kernel to **every proper degree-sixteen mate** on the selected carrier. The two conjugate generic branches have equal vanishing orders \(n\); finite intersection length is \(m_C=2n\), and \(n\ge12\) would force a global multiple of \(F_*\). Thus \(m_C\le22\), and the residual cycle has degree at least eight. This requires no prescribed full initial ideal or saturation hypothesis. It remains a new unpromoted fixed-carrier result, not an exclusion of the entire endpoint-four chart or the unrestricted characteristic-zero problem.

The exact scripts, data, output, geometric bridges, and limitations are saved. All investigations underway at the user's October 26 instruction have now reached their stated endpoints. No additional research item is being started; finish validation and push this final checkpoint, then stop.



---

## 2026-10-25-ci-cycle-adaptive-valuative-notebook.md

# Adaptive valuative comparisons with multiples of the quartic

Date: 2026-10-25. **Exploratory continuation of the complete-intersection cycle notebook.** New deductions and proposed comparison principles remain provisional; independent review is recorded in the [valuative audit](CI_CYCLE_AUDITS_AND_BOUNDARY_SMOOTHING.md#2026-10-25-ci-cycle-valuative-auditmd). No general residual-component theorem is claimed.

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

The [generic valuative multiplicity note](CI_CYCLE_VALUATIONS_AND_CONTACT.md#2026-10-25-ci-cycle-valuative-multiplicitymd) supplies primary references, field-of-definition qualifications, and the finite-cluster formula. The point is a standard multiplicity theorem applied to this problem; no novelty claim is made for the theorem.

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

It is not in general the dualizing/conductor boundary. In the local complete intersection of four noncoplanar lines, choose one line as \(C\). The other three lines each contribute one to \(\mathcal B_C\), giving \(3p\); the conductor on the marked normalized line has coefficient two. The [contact-cycle note](CI_CYCLE_VALUATIONS_AND_CONTACT.md#2026-10-25-ci-cycle-valuative-contact-cyclemd) calculates this example explicitly. These objects agree for the smooth-surface branch arrangement of \(Z\), but serve different purposes in the broader space-curve problem.

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

The [endpoint valuation notebook](CI_CYCLE_VALUATIONS_AND_CONTACT.md#2026-10-25-ci-cycle-endpoint-valuationsmd) develops these pictures and their scope.

The [root-collision continuation](CI_CYCLE_VALUATIONS_AND_CONTACT.md#2026-10-25-ci-cycle-root-collision-valuationsmd) then follows the actual root pencil near its double-\(C\) member over a field above two. It finds two different thresholds: one for how fast a residual sheet approaches the marked sheet, and another for collision within the residual sheets. The first-normal determinant records their total marked separation but misses that second collision. A full tree with residue information resolves the ambiguity.

The later [fixed-boundary node experiment](CI_CYCLE_AUDITS_AND_BOUNDARY_SMOOTHING.md#2026-10-25-ci-cycle-fixed-boundary-node-smoothingmd) supplies another concrete distinction: all five nodes inside a line-plus-degree-eleven residual curve can be smoothed independently in the formal fixed-boundary fiber, with an étale algebraic local realization. These nodes lie away from \(C\). Their smoothing changes residual normalization genus while the exact attachment divisor on \(C\) stays fixed. This is a verified local deformation picture, not a universal ordering or an explicit polynomial coefficient path.

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

## 11. Completed fixed-carrier test, October 26

The endpoint-four followup now gives one concrete instance of the adaptive certificate program. Put
\[
q=x_0x_3-x_1x_2,\qquad D=x_2^3-x_1x_3^2,\qquad
F_*=-q^2x_3^2-qDx_2+D^2/4+q^3.
\]
For this displayed degree-six carrier and every homogeneous degree-sixteen \(G\) containing \(C\), provided the intersection is proper, the new [actual-sextic investigation](2026-10-25-endpoint4-actual-sextics.md) and [nonsplit-node scope audit](2026-10-26-endpoint4-nonsplit-node-scope-audit.md) give
\[
m_C(V(F_*,G))\le22,\qquad \deg R\ge8.
\]
This is an independently reviewed, unpromoted fixed-carrier certificate in characteristic zero; it is not the universal all-pairs conclusion.

Its mechanism is explicitly valuative. The generic quadratic normal term has nonsquare discriminant class \(1+z^2\), so a quadratic function-field extension splits two conjugate transverse branches. A \(k(z)\)-defined mate has equal finite orders \(n\) on their DVRs, and \(m_C=2n\). Orders at least twelve force membership in \((F_*)+(u,v)^{12}\).

Actual homogeneous coefficient constraints then supply the missing upper bound in this example. Two different finite implementations show that the degree-sixteen global jet kernel consists only of \(F_*H_{10}\), using a rank-\(683\) matrix on \(969\) constant coefficients and explicitly annihilating all \(286\) known multiples. A proper mate cannot be such a multiple, so \(n\le11\). The normal-division specialization and nonsplit-node arguments are recorded separately from the finite rank evidence.

The carrier was obtained from the conditional movement-two chart, but this final bound needs no prescribed full initial ideal or saturation hypothesis. Other carriers, other parameters in that chart, and other mate degrees remain outside the completed calculation.

The promoted premises remain the fixed-curve conormal result [R0020](../results/quartic_conormal_characteristic_jump.md) and prescribed degeneration [R0021](../results/quartic_mu4_degeneration.md). The older valuation and residual-cycle notes are used at their provisional/reconciled scope. The new material is an exploratory framework with reviewed local deductions and the stated fixed-carrier certificate; it does not establish the universal residual claim.



---

## 2026-10-25-valuative-frontier-next-experiments.md

# Two focused frontier experiments after the valuative continuation

Date: 2026-10-25. Reconnaissance for choosing the next experiment; no canonical promotion.

Retrieval followed [INDEX](../INDEX.md), the relevant portions of [FRONTIER](../FRONTIER.md) and [STATE](../STATE.md), then the records and evidence below. The older intrinsic-geometry pause is a research preference, not mathematical closure; the present continuation is explicitly authorized to consider open STCI items. No quartic-carrier case is reopened.

The new [valuative multiplicity note](CI_CYCLE_VALUATIONS_AND_CONTACT.md#2026-10-25-ci-cycle-valuative-multiplicitymd) supplies an exploratory bridge: for an actual proper pair, the generic transverse ideal is a parameter ideal, so its multiplicity is determined by its complete adapted valuation data. The experiments here concern the extra global twisting and actual-generator restrictions that this local computation does not supply.

## Candidate A: a single nonsaturated first-relation defect in degree (6,12)

**Focused question.** Can an actual homogeneous pair of degrees \((6,12)\), with sole reduced support the fixed characteristic-zero quartic, have full generic ordinary initial CI \((2,9)\), with a first-relation saturation defect of length one and saturated movement one?

This is a deliberately narrow slice of the open nonsaturated-first-relation frontier. It does not claim to be the first possible pair in a global ordering, or to exhaust nonsaturated cases.

**Current authority.** [STCI-R-0016](../results/nonsaturated_first_relation_resultant.md) is promoted and proves a defect/resultant budget under actual lci, sole smooth support, and a full generic binary-CI initial algebra. It does not exclude nonsaturated first relations. [STCI-R-0010](../results/saturated_first_relation_normal_flatness.md) assumes saturation, and [STCI-R-0013](../results/saturated_actual_generator_movement.md) excludes movement one only in that saturated class. Consequently R0013 cannot dispose of the proposed slice. The general non-CI-initial-ideal cases remain separate; this candidate still assumes a full generic CI.

The exact identities used next are in the accepted evidence for R0016, [first-relation defect investigation](2026-10-19-first-relation-defect-investigation.md), sections 3–5. Its historical provisional label does not independently promote its contents, but R0016 explicitly links the proof and its independent audits. The new numerical application below is provisional.

Let \(R_{\mathrm{sat}}=\mathcal O(-14-\epsilon)\), let \(D\) have length \(\delta\), and use the evidence notation \(c_j\) for saturated generation defects. The socle line of an actual degree-\((a,b)\) CI has degree \(\ell=14-4(a+b)\). With \((a,b;r,s)=(6,12;2,9)\), its degree identity gives

\[
2(-58)=2(8)(-14)-7(-14-\epsilon)+c_8,
\qquad c_8=10-7\epsilon.
\]

Effectivity and \(\epsilon\ge0\) leave \((\epsilon,c_8)=(0,10)\) or \((1,3)\). In the second case the resultant equation gives

\[
\deg\Delta=c_8-2c_9=3-2c_9,
\qquad c_9=0\text{ or }1.
\]

Thus its resultant degree is three or one. For \(\delta=1\), the general bound \(c_8\le\binom72\delta\) does not contradict either value. These are necessary arithmetic possibilities, not existence evidence.

**One fresh experiment.** Use the actual sextic second-symbol image, already computed with rank 22 and kernel \(kq^3\) in the independently reviewed [sextic symbol map](2026-10-20-conditional-2-12-symbol-map.md). Its symbol calculation is reusable independently of the saturated \((2,12)\) application advertised in that note.

Parameterize a full movement-one quadratic root

\[
f=(A_0+A_1z)U^2+(B_0+B_1z)UV+(C_0+C_1z)V^2,
\]

with homogeneous endpoint charts retained, and a point \(p\) supporting \(D\). Impose that the second symbols of actual global \(F_6,G_{12}\) are multiples of \(f\), with common multiplier divisor exactly \(p\), so that their actual first kernel is \(R_{\mathrm{sat}}(-p)\). The raw multiplier degrees are nine and 33; after removing their common linear factor, the degrees are eight and 32 and the remaining two sections must have no common zero.

Next divide the truncated normal expansion of \(G_{12}\) by the actual \(F_6\) over \(k(C)\), retaining all global coefficients as constants in \(k\). Force the remainder through normal degree eight to vanish and test that its degree-nine term is coprime to \(f\). For each supplied sextic this is a finite linear test on the actual degree-twelve source. The unknown sextic/root parameters make the total incidence nonlinear, but finite.

The generic cluster energy would then be \(2\cdot9=18\), spending all degree \(72\) on \(C\). A proper global solution would therefore be highly consequential and needs independent audit; there is no asserted solution. A useful negative result could show that every solution factors through \(F_6\), violates the one-point defect condition, or has a forced extra initial relation. Failure to solve the incidence proves nothing.

The simplest local warning remains the accepted source family \((txy+x^3+y^4,xy^2)\): it is finite-flat with constant length ten while the first relation degenerates. Its generic complete-ideal cluster has energy \(4+3+3\), whereas the special cluster has energy \(9+1\). This elementary new cluster reading illustrates that constant energy permits substantial redistribution. The local \((2,5)\) model is a benchmark, not a surviving global degree row.

## Candidate B: the retained endpoint-four nodal chart in degree (6,16)

**Focused question.** Does the endpoint-root normal form \(\tau=z^4\), in the conditional \((r,s;a,b;\epsilon)=(2,12;6,16;2)\) lane, admit the next actual global homogeneous lifts at any of its retained nodal torsion parameters?

**Current authority.** [STCI-R-0014](../results/movement_two_six_rows.md) gives six necessary rows in the saturated/full generic binary-CI class, including this row. It is a promoted arithmetic reduction, not a construction or emptiness theorem. [STCI-R-0018](../results/regular_singular_root_formal_obstruction.md) excludes all-orders lifts whose entire formal surface is regular along the reduced movement-two root; singular formal surfaces remain outside its conclusion.

The [October 21 conductor/chart independent review](2026-10-21-conditional-2-12-conductor-and-chart-independent-review.md), sections 5–6, gives reviewed but **unpromoted** endpoint reductions. It leaves the normal forms \(\tau=z^3(1+z)\) and \(\tau=z^4\), plus a distinct nonzero-endpoint orbit-collision chart. On the fourth-order chart a retained root is integral nodal and its actual Picard gluing modulus satisfies

\[
\rho^{12}=1,\qquad \rho\ne1.
\]

This is a necessary torsion equation, not an exclusion of its intersection with higher ambient lifts. The review explicitly says repeated multiplier zeros and multiplier zeros at root nodes remain unresolved. The failed file [conditional certificate audit metadata](../computations/conditional_2_12_certificate_audit_cont2_2026_10_21.json) records return code one and an assertion failure at line 23 of its companion M2 input. No conclusion here relies on it.

**One fresh experiment.** Normalize projective root scale by \(a_0=1\) and use the reviewed root coefficients

\[
a=1+2b_2z+z^2,\qquad
b=\tfrac{\rho+1}{2}z+b_2z^2,\qquad
c=\tfrac\rho4z^2,
\qquad f=aU^2+bUV+cV^2.
\]

Treat every nontrivial twelfth root \(\rho\) over its exact cyclotomic field; retain the nodal and finite-ruling opens. Determine actual sextics with second symbol \(z^8f\), using the saved rank-22 image and the one-dimensional \(q^3\) lift freedom. Then impose that the remainder of an actual global \(G_{16}\), after division by that sextic, vanishes through normal degree eleven and has a coprime degree-twelve term.

This gives a fresh exact matrix/incidence problem on \(b_2\), the \(q^3\) lift parameter, and actual degree-sixteen coefficients. Retain the saturated actual-generator condition: the second-symbol multiplier of \(G_{16}\) must be nonzero at the endpoint where the sextic multiplier \(z^8\) vanishes, and the pair of multipliers must generate the actual first-relation line everywhere. The endpoint specialization may shrink the incidence substantially. Track the adapted valuation cluster along both node branches, but retain their conductor identification: normalization alone loses the modulus \(\rho\). Do not assume a regular formal surface, which would simply place the problem back in the already excluded R0018 class.

The source defines \(\tau\) and its multiplier up to a nonzero scalar; any normalization must be propagated through the actual symbol equation rather than silently reusing incompatible coordinates. A completed unit ideal or an independently checked obstruction on this exact open would close a genuine small chart. It would leave the other endpoint and collision charts, the other movement rows, and unrestricted STCI untouched.

## Recommendation

Candidate A is the more direct test of whether adaptive cluster geometry can interact with **global first-relation defects** beyond the saturated theory. Candidate B has a smaller, more concrete inherited parameter space and could produce a useful completed chart first. Both require actual homogeneous coefficient spaces and complete local cancellation data; neither can be settled by allowing arbitrary \(k(C)\)-coefficients or by counting exceptional components as downstairs residual curves.

