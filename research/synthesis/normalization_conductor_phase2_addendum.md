# Phase 2 addendum: ruled normalizations and conditional conductor boundaries

## Paired-secant cubic

The finite normalization of the cubic x0*x2^2=x1^2*x3 is F1, with hyperplane class E+2f. On x0=1 its local ring inclusion is k[r,rw,w^2] inside k[r,w]. The upstairs conductor is (r); the downstairs conductor is the reduced double-line ideal (x1,x2). The conductor section maps two-to-one to the line, branched at the endpoints. The strict quartic lift has class 2E+2f, but the full inverse ideal is (w-r^2)(r,w), with an embedded length-one defect at each endpoint. The same F1 is the smooth cubic scroll S(1,2) in P4, projected from the omitted middle coordinate. On the smooth quadric the cubic cuts C0 plus the two limiting tangent trisecants. In characteristic two the conductor cover is inseparable and the scroll is a tangent developable.

Sources: research/notes/2026-10-24-cubic-scroll-normalization.md and research/notes/2026-10-24-p4-ruled-models-independent-audit.md. Independently reviewed provisional geometry, not a new STCI result.

## Projection cone and four-section quartic

The projected cone over C0 has ring k[s^4,s^3t,st^3,t^4], missing the integral element s^2t^2. Its normalization is the complete fourth Veronese cone, with conductor supported at the vertex and an upstairs dual-number quotient. The correct factorization is F4 contracting the negative section to the normal cone, followed by finite normalization of the projected cone. F4 itself is not finite over the projected cone. The related four-section quartic has conductor (x0,x1)^2 downstairs; its transverse ring is k[v^3,v^4,b] inside k[v,b], with conductor v^6. Full inverse ideals can have embedded endpoint corrections of colength six.

Sources: research/notes/2026-10-24-p4-ruled-surfaces-synthesis.md and its independent audit. Elementary transformations and mu4 arithmetic remain in the ruled-geometry family.

## Conditional (6,16) singular-root interface

The October 20 proposal assumes an actual supported (6,16) pair, full generic coprime normal CI (2,12), and an actual saturated movement-two first relation. The (2,2) spectral root Z must satisfy O_Z(1,-1)^12 trivial. A reviewed but unpromoted finite singular-root bridge has transform ideal (p,u^10), providing finite embedded Cartier lifts even for singular Z. Full spectral torsion eliminates cuspidal and tangent-component roots; smooth, nodal, and two-node reducible roots retain their gluing conditions. The next global step is cubic-jet matching for a genuine sextic, [F3-alpha*G0] mod (f)=0, without dividing by alpha at its zeros. Abstract Cartier lifts do not yield global equations or a support certificate.

The October 21 conductor-budget proposal originally depended on an anticanonical contraction hypothesis. The independent continuation audit subsequently VERIFIED that hypothesis in the precise actual-pair setting: a cubic-image model V is a smooth integral threefold with canonical bundle O(-2), and the strict sextic descends to an integral anticanonical surface T. Finite duality and the local monic double-cover normalization then exclude singular-curve contacts at ramified simple base zeros. Combined with the separate nodal analysis, the reviewed result gives a sharp NECESSARY alternative for any actual pair: the multiplier alpha has a multiple base zero, or alpha vanishes at a node of the full root. For a smooth full root the necessary discriminant equation is Disc_8(Ncomp(tau))=0, of degree 28 in the root coefficients. These exceptional strata have not been eliminated; no complete exclusion follows. A different proposed nodal normalization obtained by dividing by a nonunit was rejected as nonfinite. Its suggested integral replacement is not yet certified normal or equipped with an exact conductor.

Sources: research/notes/2026-10-20-conditional-2-12-singular-gluing.md and research/notes/2026-10-21-conditional-2-12-conductor-ramification.md. Conditional cross-family work, not promoted.

## Remaining boundaries

No arbitrary projection classification, full conductor phase image, higher-index exclusion, global spectral realization, or unrestricted characteristic-zero STCI theorem follows. The separate codex/intersections-containing-quartic-2026-10-27 branch remains excluded. Original mathematical sources are retained.


Source for this correction and stronger reviewed result: research/notes/2026-10-21-conditional-2-12-surface-audit-cont2.md, sections 2-6. Its independent review reports PASS for the cubic-model interface, full conductor duality, and ramified simple-base-zero exclusion, while expressly rejecting the defective nodal normalization. The finite singular-root bridge remains reviewed but unpromoted.


### Geometric scope of movement two

The canonical reduction STCI-R-0014 identifies movement epsilon with the degree of the coefficient map from C to the projective space of binary degree-r forms. Its first normal-root divisor has bidegree (epsilon,r) on P1_base x P1_direction. In the conditional (6,16) setting, r=2 and epsilon=2, so the full first root is a divisor of bidegree (2,2). Saturation means the coefficient map has no base points; it does not exclude root collisions or ensure coprimality of specialized initial forms. Generic binary-CI coprimality and saturation are separate assumptions. The six numerical rows, including (r,s;a,b)=(2,12;6,16), are necessary candidates only under the complete hypotheses of STCI-R-0013 and STCI-R-0014; they are not a classification of arbitrary STCI presentations.

Canonical source: research/results/movement_two_six_rows.md (STCI-R-0014), geometric clarification in commit ccc9c3965e1645ed2569405e0194e31edb38e9d0. This cross-reference does not promote the conditional singular-root arguments.
