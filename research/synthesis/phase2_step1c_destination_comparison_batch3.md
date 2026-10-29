# Phase 2 Step 1C — entirely-thick destination comparison batch 3

Original sources read: `research/notes/2026-10-07-entirely-thick-rees-valuation-framework.md`, `2026-10-07-entirely-thick-relative-blowup-budget.md`, `2026-10-07-thick-sheaf-colon-recursion.md`, `2026-10-07-rational-quartic-power-saturation.md`, and `2026-10-07-thickened-fiber-local-countermodel.md`. Compared with `research/synthesis/formal-normal-intersection.md` and `research/synthesis/normal_filtration_boundary_obstructions.md`; these are not exhaustive destination checks.

| Claim | Finding | Owner / action |
|---|---|---|
| Generic transverse Noether budget: ab/4-pq equals weighted infinitely-near multiplicity sum; fixed (a,b,p,q) bounds cluster size | Broad Rees/blowup discussion exists; exact cluster formula and limitations not confirmed in compared destinations | Entirely-thick/valuation owner; integrate formula and limitations |
| Horizontal blowup recursion: pushforward strict-transform intersection subtracts rs[Z]; degree-d covers contribute drs; terminating sectionwise tree budget sum c_j=2pq | Not located at formula level | Entirely-thick/blowup owner; retain terminal-horizontal hypothesis |
| Sheaf colon (I^p:Q)=I^(p-1) | Original early note proved this; homogeneous saturation was still open *at that stage* | Entirely-thick/ideal powers; do not preserve obsolete open status |
| Later power-saturation theorem: H0(sheaf I^m(d))=(homogeneous I^m)_d and H1=0 for d>=3m; boundary colon and quotient recursion | Exact theorem not confirmed in inspected destinations | Entirely-thick/ideal powers; preserve proof via quadric exact sequence |
| Local thickened-fiber countermodel: reduced support constrains A0 only, not higher A1,...,A(M-1); interpolation cokernel alone is not STCI obstruction | Not found in inspected destinations | Entirely-thick/negative models; preserve substantive failure |

## Reconciled chronology, mathematical content only

The October 7 sheaf-colon note ends with an open homogeneous saturation question. The later power-saturation note **answers it affirmatively** for d>=3m by induction using the exact sequence 0→I^(m-1)(d-2)→I^m(d)→O_Q(d-m,d-3m)→0, H1 vanishing and cubic products spanning the quotient. The consolidated statement must use the later theorem and must not repeat the earlier open question as current.

At the boundary, (I^p)_(3p) intersect (Q)=Q (I^(p-1))_(3p-2), and the quotient is H0(Q,O_Q(2p,0)). This is a statement about the degree-3p carrier space, not a mate exclusion.

The relative Noether recursion applies to proper intersections and terminating horizontal center trees. Persistent valuations are not proved to algebraize to extra projective common curves. No u-monotonicity theorem follows.

The local model F=h^p x^M, G=h^q(A0(y)+xA1(y)+...) has no new reduced common support off C provided A0 has none there, regardless of higher coefficients. Thus the thickened-fiber jet cokernel is not an obstruction without additional scheme-theoretic hypotheses.

**Verdict:** provisional partial/absent in the two compared syntheses; broader destination search and permanent integration remain pending. No correctness promotion, no historical edits.
