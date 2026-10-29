# Mathematical consolidation: intrinsic geometry as a subject in its own right

**Status:** thematic synthesis, not theorem promotion. Intrinsic geometry is a first-class research interest here, not material to retain only when it yields an STCI obstruction. Sources: R-0026–R-0028; special-lines/planes and automorphism/bitangent syntheses and their audits.

## Organizing geometry

The curve C=[s^4:s^3t:st^3:t^4] is the projection of the rational normal quartic in P4 from the missing-middle-coefficient point. The point is intrinsically recovered from the unordered pair of distinguished endpoints. Its unique smooth quadric Q is the Segre surface on which C has class (1,3), the graph of the cubic map [s:t]↦[s^3:t^3]. This one picture explains the trisecant ruling, the two totally ramified points, and the ambient symmetry.

The reviewed unpromoted automorphism synthesis identifies Aut(P3,C)=G_m⋊Z/2 (faithful restriction, preserving the endpoint pair). The osculating residual involution u↦-u is distinguished by H_u|C=3u+(-u); the endpoint planes have contact four. This is not the bitangent correspondence: its contact pairs satisfy u²+4uv+v²=0, with ratios -2±sqrt(3). The two conics in Sym²C=P² (diagonal and bitangent locus) meet tangentially at the two endpoint divisors. Their polar/trace relationship explains the otherwise surprising coefficient 2 in the bitangent conic. The two bitangent branches form a correspondence, not an involution.

The paired osculating planes intersect along secants sweeping R: x0*x2²-x1²*x3=0. Along C, the tangent plane of R equals the osculating plane of C; on Q the intersection cycle is C plus the two endpoint ruling lines. The special-lines note proves that trisecants are exactly one ruling of Q and no line has intersection length four with C. These are interesting positive geometric facts independent of STCI.

## Flag, dual, and ruled geometry

- **R-0026:** the marked factorization incidence is the smooth complete flag F(1,2;3); degree-two divisor addition is finite flat of degree six, with a length-six quadruple-root fiber. Its conormal normalization and contact sections give a coherent explanation of osculation, duality and the endpoint scheme structures. The characteristic-two swap equalizer degenerates to a double line while the flag itself stays smooth.
- **R-0027:** the dual discriminant's Jacobian scheme has four minimal and two embedded endpoint associated primes, with two length-one endpoint corrections. Its scheme-theoretic identities carry multiplicities that the reduced dual alone misses. The source explicitly records a corrected earlier omission of endpoint-pencil components; retain this failure mode, not the obsolete reduced description.
- **R-0028:** the projection models distinguish finite normalization, smooth resolution, and elementary transformations: the cone normalizes to P(1,1,4) and resolves on F4; the projected cubic normalizes on F1, with a doubled conductor line. Endpoint corrections are real scheme structure, not cosmetic artifacts.

## Concrete ruled and resolved-projection geometry

For the marked projection \(C_4=[s^4:s^3t:s^2t^2:st^3:t^4]\subset\mathbf P^4\) from \(z=[0:0:1:0:0]\), the resolved ambient map is
\[
\operatorname{Bl}_z\mathbf P^4=\mathbf P_{\mathbf P^3}(\mathcal O\oplus\mathcal O(-1))
\longrightarrow\mathbf P^3
\]
with the **lines** convention. Its inverse surface over \(C\) is \(\mathbb F_4\). The complete and projected quartics are graph sections \(q=s^2t^2\) and \(q=0\) in \(|E+4f|\); their intersection divisor is \(2p_0+2p_\infty\). The full graph family is five-dimensional \(H^0(\mathcal O(4))\); complementary hyperplanes give only the four-dimensional subfamily corresponding to the fixed four-coordinate span. The smooth surface and its two sections must not be confused with their projective images.

The cone's **finite normalization** is the singular weighted projective surface \(T=\mathbf P(1,1,4)\), while \(\mathbb F_4\) is its smooth resolution. The paired-secant cubic \(R=V(x_0x_2^2-x_1^2x_3)\) has finite normalization \(\mathbb F_1\), and the marked quartic is a bisection there, rather than a ruling section. Its doubled conductor line is branched at the two endpoints. The same-center cubic scroll in \(\mathbf P^4\) is
\[
\Sigma=S(1,2):
\quad X_0X_4-X_2^2=X_0X_3-X_1X_2=X_2X_3-X_1X_4=0.
\]
The scroll and projection cone meet in reduced support \(C_4\), with two additional embedded length-one endpoint corrections. On the original quadric the *different* Cartier intersection is \(R|_Q=C+L_0+L_\infty\). These residual lines are genuine one-dimensional components; the corrections upstairs are zero-dimensional embedded structure.

The ordered-endpoint elementary transforms from \(Q\) to the \(\mathbb F_4\) model change the marked section's self-intersection as \(6\to5\to4\to3\to4\), with the first three centers on the marked curve and the fourth off it. This does not identify the projective polarizations. The \(\mathbb F_1\) bisection instead splits only after the degree-two ruling-base change, on \(\mathbb F_2\). These distinctions are part of the geometric content of [R-0028](results/quartic_ruled_projection_geometry.md), with complete calculations in the [ruled-surface synthesis](notes/2026-10-24-p4-ruled-surfaces-synthesis.md).

## Why preserve this even without an STCI application

The geometry supplies its own worthwhile questions: symmetry and moduli of projected quartics; osculating versus bitangent correspondences; incidence and contact on Sym²C; dual singular schemes; normalization of ruled surfaces; behavior at distinguished endpoints and in characteristic two. It is valuable as a coherent small project, not a miscellaneous appendage to a nonexistence proof.

## Epistemic boundaries

- R-0026–R-0028 are scoped canonical records for specific marked constructions.
- Automorphism, bitangent and special-line notes are independently reviewed but remain **unpromoted**; do not silently upgrade their authority.
- A dual/incidence identity is not automatically an STCI obstruction.
- Distinguish reduced contact loci, embedded endpoint structure, and Cartier multiplicities.
- Do not equate the conormal normalization with the original curve on Q, nor the bitangent relation with the osculating involution.
- The moduli/orbit discussion in the automorphism synthesis should retain its literature qualifications; no novelty claim.

## Proposed architecture

Create a dedicated **Intrinsic geometry of the marked quartic** chapter (or small cluster of chapters) with its own reading path:
1. Projection from the rational normal quartic, unique quadric, cubic ruling and automorphisms.
2. Special lines and planes, osculating involution, bitangent correspondence and symmetric square.
3. Flag/conormal incidence and dual discriminant, including endpoint scheme structures.
4. Ruled cubic, P4 projection, normalization, conductor and elementary transformations.
5. Geometric questions and literature/moduli context.

Cross-link to STCI where a specific calculation is useful, but do not organize or judge this material by whether it advances STCI. Preserve figures and independent audits as part of the mathematical exposition. This is a deliberate exception to any overaggressive 'directly useful to STCI' retention rule.

## Next review

Check the current thematic navigation and synthesis chapters for a suitable permanent home for intrinsic geometry. Avoid producing an endless chain of temporary inventories: once the architecture is agreed, migrate explanatory content into actual chapters while leaving canonical records and audit evidence intact.
