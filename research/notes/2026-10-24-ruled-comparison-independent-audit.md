# Independent audit: natural ruled comparisons and their limits

Date: 2026-10-24. Reviewer: independent agent `comparison_audit`.
Status: **independently reconstructed provisional geometry; no canonical promotion**.
The field is algebraically closed of characteristic zero except where a change is explicitly stated. The fixed curve is
\[
C=[s^4:s^3t:st^3:t^4].
\]
The reviewer read [INDEX](../INDEX.md) and the [contribution instructions](../CONTRIBUTING_AGENT.md), then reconstructed the comparisons below from local bundle coordinates and intersection theory before consulting author drafts. No STCI result is a premise. This audit verifies specific maps; it does not identify arbitrary birational equivalences as geometric explanations.

## 1. A four-step elementary transformation from the quadric to the four-sheet model

Use the Segre parametrization
\[
Q=\mathbf P^1_{[a:b]}\times\mathbf P^1_{[s:t]},\qquad
[x_0:x_1:x_2:x_3]=[as:at:bs:bt].
\]
The ruling base is the parameter line of the degree-one projection of C. On s≠0 write u=t/s and v=b/a. Then C is v=u³. Write E₀={a=0}, the section v=∞, and f for a ruling fiber. Thus
\[
Q=\mathbb F_0,\qquad C=E_0+3f,\qquad C^2=6.
\]
This negative-section notation starts with a chosen square-zero section; on F₀ there is no unique minimal section.

Put w=1/u near p∞=[0:1], and r=1/v near E₀. The curve is r=w³. Blow up (w,r)=(0,0) and contract the strict transform of the fiber w=0. This is the elementary transformation with center on E₀. Its new local fiber coordinate near the strict transform E₁ is
\[
r_1=r/w.
\]
Repeating with rᵢ=r/wⁱ and center (w,rᵢ)=(0,0), for i=0,1,2,3, gives
\[
\mathbb F_0\dashrightarrow\mathbb F_1\dashrightarrow
\mathbb F_2\dashrightarrow\mathbb F_3\dashrightarrow\mathbb F_4.
\tag{1}
\]
Each Eᵢ becomes the negative section Eᵢ₊₁: blowing up its point decreases its square by one; its strict transform is disjoint from the contracted fiber. In the last surface the affine coordinate complementary to E₄ near infinity is
\[
q_\infty=1/r_4=w^4v,
\]
while over the finite u chart q₀=v. These are precisely the transition functions of the total space O(4), compactified by its infinity section E₄. This identifies the target with F₄ by its bundle transitions, not only by its intersection matrix.

The first three centers lie on the strict transform of C: rᵢ=w³⁻ⁱ for i=0,1,2. On F₃ the curve has r₃=1 at w=0, so the fourth center r₃=0 is off the curve. The resulting classes and squares are

| Surface | Strict transform of C | Square | Intersection with minimal section |
| --- | --- | --- | --- |
| F₀ | E₀+3f | 6 | 3 |
| F₁ | E₁+3f | 5 | 2 |
| F₂ | E₂+3f | 4 | 1 |
| F₃ | E₃+3f | 3 | 0 |
| F₄ | E₄+4f | 4 | 0 |

Here the final graph is q₀=u³ and q∞=w. It is the strict transform of C₁ on the common ruling model of F=x₁⁴−x₀³x₃, with q=x₂/x₀ on the finite chart. The map is explicitly compatible with the distinguished curve and degree-one ruling.

For completeness the class transformation can be checked for any curve D∼aEᵢ+bf having multiplicity m at the chosen center. Its strict transform meets the contracted fiber in a−m. Consequently
\[
(D')^2=D^2-m^2+(a-m)^2=D^2+a^2-2am,
\]
\[
D'\sim aE_{i+1}+(b+a-m)f.
\tag{2}
\]
The table follows by taking a=1 and m=1,1,1,0. This also checks that the fourth step cannot be omitted or incorrectly placed on C: either would produce the wrong square and bundle.

The comparison does not preserve the projective hyperplane linear systems. A general Q-hyperplane has class E₀+f and misses all four centers, hence its final strict transform is E₄+5f. Conversely a general F-hyperplane pulls back birationally to a section of class E₀+4f, whose first four centers lie on it; its transform is E₄+4f. Thus preserving the curve and ruling does not make the two projective embeddings equivalent.

## 2. What makes the chain natural, and which choices remain

The construction uses the explicit Segre factors, the ordered endpoint p∞, and the section E₀={a=0}. These are supplied by the fixed coordinate presentation together with a choice between the two endpoints. It is equivariant for the torus
\[
u\mapsto\alpha u,\qquad v\mapsto\alpha^3v,
\]
which preserves C and the four successive centers. It is therefore substantially more constrained than an arbitrary birational map between rational surfaces.

Endpoint interchange exchanges F=x₁⁴−x₀³x₃ with the analogous surface G=x₂⁴−x₀x₃³. It exchanges the above chain with its counterpart based at p₀. The unordered endpoint pair alone does not choose a unique chain to a chosen one of F and G. No assertion of a canonical map invariant under the full torus normalizer follows.

To identify the image of C with the zero-graph section C in the projection-cone model rather than the section C₁ in the F model, compose the last map with the bundle translation q↦q−st³, interpreted as a global section of O(4). This is an automorphism of the ruled model. It does not identify all its chosen projective image maps or conductor structures.

## 3. The cubic scroll has a different ruling on the marked curve

For the cubic-scroll normalization use
\[
\mathbb F_1=\mathbf P_{\rm quot}(\mathcal O(1)\oplus\mathcal O(2)),
\quad H_1=E_1+2f_1,
\quad \widetilde C=2E_1+2f_1.
\]
An independent affine reconstruction takes the ruling coordinate y and point coordinate λ:
\[
(y,\lambda)\longmapsto[1:\lambda:\lambda y:y^2]\in R.
\]
The lift of C is y=λ². Hence its ruling map is the quotient u↦u²; it is a bisection, while C is a section for the rulings used in Sections 1–2. A birational map of ruled surfaces over an isomorphism of bases preserves the degree of the marked curve over that base. It therefore cannot carry these marked curves to one another while identifying these two specified rulings. This is a concrete obstruction to the overly broad claim that all models are related by ruling-compatible elementary transformations.

There is instead a natural degree-two incidence base change:
\[
\begin{array}{ccc}
\mathbb F_2 &\longrightarrow& \mathbb F_1\\
\downarrow &&\downarrow\\
\mathbf P^1_u&\xrightarrow{u\mapsto u^2}&\mathbf P^1_y.
\end{array}
\tag{3}
\]
Indeed pulling back O(1)⊕O(2) gives O(2)⊕O(4), whose projective bundle after twisting is F₂. Its negative section has square −2. Pullback of the cubic-scroll hyperplane is
\[
H_2=E_2+4f_2,\qquad H_2^2=6=2H_1^2.
\]
Pullback of the marked bisection is
\[
2E_2+4f_2=\Gamma_++\Gamma_-,\qquad
\Gamma_\pm\sim E_2+2f_2,
\]
where on the finite chart Γ± is λ=±u. The complement of E₂ is O(2), so λ∞=u⁻²λ; the graphs are the sections ±st. Each has square two. Their difference 2st vanishes to order one at each endpoint. Thus Γ₊·Γ₋=2 with the exact intersection divisor p₀+p∞ on either graph. Each maps isomorphically to the original marked curve; their bases map with degree two.

In characteristic two the same base-change equation is λ²−u²=(λ−u)². The scheme inverse of the bisection is a double section, while its reduced support is one graph. This statement uses the actual base-change construction and does not claim that normalization commutes with a change of characteristic.

This F₂ and the F₂ in the elementary chain (1) are abstractly the same Hirzebruch type, but their marked curves have different classes and squares: E₂+2f₂ (square two) in the base-change construction, versus E₂+3f₂ (square four) in (1). Their equality as abstract surfaces supplies no identification of the marked configurations.

## 4. Audit outcome and scope

The explicit four-step elementary chain is verified. It proves a relationship compatible with the marked curve and the degree-one ruling, with the ordered endpoint and explicit embedding data stated. Its divisor transform formula, intermediate classes, and final bundle transitions agree independently.

The cubic-scroll model is linked naturally by a degree-two base change and splitting of the marked bisection, rather than by a birational identification of the specified rulings. Its hyperplane pullback and graph intersection divisor are verified. The characteristic-two assertion here is restricted to this exact base-change equation.

The author notes retain the proofs and full normalization/conductor information for the [projection cone](2026-10-24-projection-cone-ruled-model.md), [cubic scroll](2026-10-24-cubic-scroll-normalization.md), and [four-sheet surface](2026-10-24-four-sheet-ruled-surface.md). Their independent central-model and arithmetic audits are separate from this comparison audit. These are new provisional research contributions, with no change to canonical results, no STCI implication, and no novelty claim.
