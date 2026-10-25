# Intrinsic geometry interlude — 2026-10-24

## Purpose and research status

**Current research choice: pause active attempts to prove or disprove the characteristic-zero STCI question.** We are exploring the intrinsic projective geometry of the fixed smooth rational quartic
\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3
\]
**because the geometry is interesting in its own right.** Potential STCI insights are welcome side effects, **not the aim, a requirement, or a measure of success**. Do not steer every calculation toward an obstruction, carrier classification, or degree bound. This is a change of focus, not a mathematical closure: all accepted STCI results retain their exact scope, and the unrestricted question remains open. Do not silently reopen excluded quartic carriers.

The preceding [special-lines/planes exploration](notes/2026-10-24-special-lines-planes-research-note.md) and [automorphism/bitangent synthesis](notes/2026-10-24-quartic-automorphisms-bitangents-synthesis.md) are preserved on `main` as provisional research evidence, not canonical theorem authority. The earlier statement that commit `51dc477` had not been pushed is historical and no longer a current retrieval instruction. Distinguish the osculating involution from the distinct bitangent correspondence; independently check formulas before promoting claims.

## Questions to preserve

### A. The linear system, projection, and automorphisms

Set \(W=H^0(\mathbf P^1,\mathcal O(4))\), \(V=\langle s^4,s^3t,st^3,t^4\rangle\subset W\). Compare the complete rational normal quartic in \(\mathbf P(W^\vee)=\mathbf P^4\), its projection from the point annihilating \(V\), and the embedded curve in \(\mathbf P(V^\vee)=\mathbf P^3\). Characterize the projection center, the missing middle section, the unique containing quadric \(Q\), and the stabilizer of \(V\) in \(\operatorname{PGL}_2\). Prove and delimit the expected \(\operatorname{Aut}(\mathbf P^3,C)\cong\mathbf G_m\rtimes\mathbf Z/2\) (characteristic hypotheses and possible group-scheme subtleties). Interpret incidence correspondences through this action.

### B. Correspondences and the symmetric square

Use \(\operatorname{Sym}^2\mathbf P^1\cong\mathbf P^2\) to study unordered pairs \(p+q\) whose double \(2p+2q\) belongs to the hyperplane linear system. Describe the bitangent conic, diagonal conic, tangencies at the two hyperosculating points, and osculating residual involution. Explain intrinsically why the bitangent partners have ratio \(-2\pm\sqrt3\) (or satisfy \(\lambda+\lambda^{-1}=-4\)); do not stop at solving a coefficient equation. Track characteristic-two changes carefully.

### C. Four curves and characteristic degeneration

For \(F=x_1^4-x_0^3x_3\), \(G=x_2^4-x_0x_3^3\), analyze the four characteristic-zero components, their individual containing quadrics and intersections in projective space (they do **not** all lie on one common smooth \(Q\)), and automorphisms permuting them. Distinguish the stabilizer of one curve from the group preserving the four-component configuration. Study the \(\mu_4\) action as a group scheme over \(\mathbf Z_{(2)}\), orbit schemes, flatness, and the nonreduced characteristic-two fiber. Determine the role of the two common hyperosculating points without conflating set-theoretic and scheme-theoretic intersections.

### D. Dual varieties and lines

Describe the duals of \(C\), \(Q\), and the cubic ruled surface \(R\); their intersections, singularities, normalizations, and tangent-plane incidences. Explain the intrinsic polarity of \(Q\) and the precise meaning of its self-duality. Study tangent, secant, and trisecant lines in \(\operatorname{Gr}(2,4)\), with specializations at the exceptional points. Retain the distinction between osculating and bitangent correspondences.

### E. Quadric, cubic scroll, and explicit surfaces

Investigate why \(Q\) repeatedly organizes the geometry. For the cubic \(R:x_0x_2^2-x_1^2x_3=0\), verify and interpret \(R|_Q=C+L_0+L_\infty\); study its normalization, singular locus, dual, and intersections with the explicit \(X=V(F)\), \(Y=V(G)\) in both characteristics. Analyze residual components and multiplicities rather than assuming intersections are proper or reduced.

### F. Exceptional divisor and iterated blowups

For \(B=\operatorname{Bl}_C\mathbf P^3\), study \(E=\mathbf P(N_{C/\mathbf P^3})\cong\mathbf P^1\times\mathbf P^1\to C\). Distinguish abstract product structure from canonical trivialization. Blow up sections of different degrees, compute their normal bundles in the successive threefolds and the ruled exceptional surfaces, and track splitting types under sequences of section blowups of degrees \(d_1,d_2,\ldots\). Test whether an elementary-transformation description exists; do not presume every new exceptional surface remains a product.

The [October 24 ruled-surface synthesis](https://github.com/markluxton1/STCI/blob/codex/quartic-p4-ruled-surfaces-2026-10-24/research/notes/2026-10-24-p4-ruled-surfaces-synthesis.md) and independent audits are **unmerged branch evidence**, not canonical results. They construct a same-center cubic-scroll lift, a common four-curve ruled model, and explicit elementary transformations; verify their exact hypotheses and status before relying on them. The [merged discussion-reconciliation note](notes/2026-10-24-discussion-reconciliation.md) separately preserves the flag-variety, dual-incidence, and higher-contact questions.

## Execution guidance

Begin with A and B as a common foundation; C and D/E can proceed separately, and F is an independent lane. These are questions, not established assertions or a mandatory work order. Favor intrinsic explanations and unexpected relationships over exhaustive computations. Give proofs or counterexamples, precise characteristic hypotheses, explicit examples where illuminating, and honest provisional labels. Record interesting dead ends. No STCI theorem promotion or canonical frontier closure follows from this agenda.
