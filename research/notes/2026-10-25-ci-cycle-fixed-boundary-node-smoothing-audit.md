# Independent reconstruction of the fixed-boundary node-smoothing calculation

Date: 2026-10-26. Reviewer: independent reconstruction worker in the cycle-notebook team. Status: reviewed finite calculation and its stated formal-local consequence; unpromoted research evidence. The filename retains the October 25 investigation date. This review completes the current experiment and proposes no additional work.

**Outcome.** The [investigation note](2026-10-25-ci-cycle-fixed-boundary-node-smoothing.md) correctly gives exact affine ranks 19,5,24 from actual global quartics. On the Grassmannian, the fixed-boundary tangent space has dimension 14 and maps onto all five residual-node smoothing parameters, with kernel dimension 9. After splitting and marking the geometric nodes, the stated completed local coordinate form is justified by the standard node-family theorem and the formal inverse-function argument. This is distinct from an explicitly computed coefficient arc, which the note correctly says has not been supplied.

## 1. The independently reconstructed source and maps

The reviewed point is the actual homogeneous pair

\[
f=F+QH_0+x_0A,\qquad g=G+QH_1+x_3D_3,
\]

with the forms specified in the [smooth-residual benchmark](2026-10-25-ci-cycle-smooth-residual-example.md). The [line-degeneration calculation](2026-10-25-ci-cycle-line-degeneration.md) and its [independent audit](2026-10-25-ci-cycle-line-degeneration-audit.md) supply the starting geometry: the residual is \(L\cup E\), with \(E\) smooth of degree 11 and genus 12, and exactly five reduced ordinary nodes \(L\cap E\) away from \(C\). The current rank calculation does not independently recertify projective smoothness of \(E\).

Before reading the durable verifier, the reviewer independently rebuilt its ingredients in a standard-library rational computation:

- all degree-four homogeneous monomials, grouped by weight \(m_1+3m_2+4m_3\);
- the 18-element actual global restriction-kernel basis, obtained by monomial differences within those groups;
- the two first-normal rows along \(C\), by differentiating the actual homogeneous polynomials;
- all 36 columns of the boundary differential;
- all 36 columns of the five-node smoothing map in the finite algebra below.

No arbitrary rational-function coefficients were introduced into the global quartic source.

On \(L\), use \([-r:r:-1:1]\) and

\[
P(r)=4r^5-2r^4+9r^3+2r^2+3r+2,
\qquad \mathcal A=\mathbf Q[r]/(P).
\]

The actual derivative in the \(x_2\) direction is

\[
F_1=-r(r+1)(r+2),\qquad
G_1=-4r^3+2r^2-9r-1.
\]

The reviewer checked that \(F_1\) is a unit modulo \(P\). Thus eliminating the smooth first carrier equation gives the first-order node class

\[
\delta g-(G_1/F_1)\delta f,
\]

and the scaled class

\[
S=F_1\delta g-G_1\delta f\pmod P
\]

has the same rank. The scale is an invertible factor at every geometric node. The actual gradient proportionality modulo \(P\) is checked in the durable verifier, not presumed from a numerical rank deficiency at a sampled root.

The independent exact Gaussian elimination returned

\[
\operatorname{rank}D=19,\qquad
\operatorname{rank}S=5,\qquad
\operatorname{rank}(D,S)=24.
\]

The reviewer also explicitly checked that every one of the 36 untruncated boundary-derivative polynomials has degree at most 18 before extraction of its nineteen coefficient rows. Thus the rank does not omit a higher-degree boundary constraint through coefficient truncation. The durable verifier now also asserts this bound before coefficient extraction and passed its replay.

## 2. Review and replay of the durable evidence

After that independent reconstruction, the reviewer read and replayed the [durable verifier](../computations/verify_ci_fixed_boundary_node_smoothing_2026_10_25.py) and read its [JSON evidence](../computations/ci_fixed_boundary_node_smoothing_2026_10_25.json). The verifier passed. Its ranks agree with the independent reconstruction.

The durable file additionally checks:

- squarefreeness of \(P\) and invertibility of \(F_1\) in \(\mathcal A\);
- the actual four ambient gradient-proportionality identities;
- the normal determinant along \(L\), equal to \(-(r+1)P(r)\);
- nonzero, degree 18, squarefree boundary determinant along \(C\);
- actual restriction to \(C\) of every source form;
- five explicitly solved rational source vectors whose boundary derivative is zero and whose scaled node images are \(1,r,r^2,r^3,r^4\).

The 36 coefficients of each witness are in the JSON, in its stated global basis order. Their meaning is first-order: writing the corresponding linear coefficient perturbations does not by itself keep the boundary fixed to every higher order.

The node algebra need not split over \(\mathbf Q\). Surjectivity onto its five-dimensional rational vector space becomes independent control of the five geometric nodes after extension to a splitting field. This does not assert that those five nodes are individually rational.

## 3. The Grassmannian and scalar-boundary issue

The ordered source \(V^2\) has dimension 36. Infinitesimal recombination of its two independent equations supplies four gauge directions. All four have node class zero because both original equations vanish at the nodes. Their boundary derivatives are scalar multiples of the base determinant, with the trace directions spanning that scalar line.

It follows that quotienting by these gauge directions and projectivizing the determinant target gives

\[
\operatorname{rank}d\beta=18,
\qquad \dim\ker d\beta=32-18=14.
\]

Any direction with zero projective boundary derivative may be adjusted by a gauge direction to have zero affine boundary derivative, without changing its node image. Therefore the joint rank 24 establishes

\[
\operatorname{rank}(S|_{\ker d\beta})=5,
\qquad \dim(\ker d\beta\cap\ker S)=9.
\]

There is no lost smoothing direction caused by passing from ordered equations to pencils, and no extra direction created by counting a scalar determinant variation as a movement of the effective divisor.

## 4. The formal claim and its precise extra input

Take an algebraically closed characteristic-zero field \(k\) containing the node residue fields. Near the reviewed pencil, the proper-complete-intersection locus in \(\operatorname{Gr}(2,18)\) is smooth of dimension 32, and the boundary map is regular because its determinant is nonzero.

The 18 independent projective boundary-coordinate differentials can be included in a regular formal coordinate system of the source. Equivalently, the formal inverse-function argument identifies the completed local ring of the fixed-boundary fiber with \(k[[z_1,\ldots,z_{14}]]\). This is a statement about the actual fiber of the divisor map, not only the linear kernel.

For each split node, [Stacks, Lemma 53.20.11](https://stacks.math.columbia.edu/tag/0CBX) applies to the flat universal complete-intersection family and gives a completed equation \(xy-\tau_i\). Its base parameter has differential equal to the node class calculated above, up to a unit. Because the five restricted differentials are independent, they extend to a basis of the cotangent space of that 14-dimensional regular complete local ring. Applying the formal inverse-function argument again gives

\[
\widehat{\mathcal O}_{\beta^{-1}(\beta_0),[f,g]}
\simeq k[[\tau_1,\ldots,\tau_5,z_1,\ldots,z_9]].
\]

The isomorphism is noncanonical and is asserted after the stated field extension and marking of the nodes. It legitimately expresses independent formal smoothing at exactly fixed boundary. It uses the flat node-family theorem in addition to the finite matrix calculation; the matrix alone would not state a higher-order lifting theorem.

The [étale local node-family theorem, Stacks Lemma 53.21.1](https://stacks.math.columbia.edu/tag/0CBY), supplies the algebraic local counterparts after an étale neighborhood. Together with the independent differentials, one can choose a smooth local map to the five smoothing parameters and obtain suitable algebraic curves locally in that neighborhood. In particular, a prescribed local curve \(\tau_i=c_i t\) in the five-parameter target lifts after an étale base change of that curve; nonzero \(c_i\) smooth the corresponding node generically, while zero \(c_i\) retain it in its node chart. This is an existence interpretation; it does not turn the displayed rational tangent vectors into a polynomial or rational coefficient arc on the original global parameter space. No such explicit arc has been computed here.

## 5. Scope and conclusion of review

The exact finite result, the scalar quotient, and the completed-local consequence pass independent review for this specified pencil. They explain how a fixed degree 18 attachment divisor can coexist with five independent residual-node smoothing directions. The reviewed calculation has no unrestricted complete-intersection claim and no implication that one uniform proximity invariant controls every pair.

The starting line-plus-degree-eleven geometry remains supported by its separate computation and audit. No canonical result, inherited proof, or accepted frontier record is changed. The current experiment is finished; no continuation experiment is begun by this audit.
