# Cross-chapter mathematical consistency audit — 2026-10-17

**Scope:** Chapters 1–6, the dependency map, and promoted result summaries in `research/STATE.md`. This is an editorial and logical cross-check, **not** an independent reproof of the nine promoted results. Detailed source-proof verification remains in the linked acceptance notes and audits.

## Findings

| Check | Finding | Resolution |
| --- | --- | --- |
| Main problem | The fixed characteristic-zero STCI question remains open throughout. | PASS |
| Degree exclusions | Chapter 5 states the integral quartic theorem with its exact quantifiers and distinguishes the separately audited factor reduction. | PASS |
| Notation | Chapters 1–2 use \(r,s\) for **orders of original equations**, whereas Chapter 3's actual-CI bridge uses \(r,s\) for **degrees of full initial-ideal generators**. | **CROSS-REFERENCE REQUIRED**: preserve both conventions but warn explicitly at each transition. |
| Normal forms | Generic shared factors imply excess local intersection; they do not give a common global polynomial factor, or automatically a saturated global root. | PASS, keep the scope warning |
| Blowups | \(I_Z\subset I_C\) does not automatically give \(\operatorname{Bl}_C\to\operatorname{Bl}_Z\); invertibility of the pulled-back center ideal is required. | PASS |
| Root schemes | Spectral Picard descent is for graded quotient relations on the full root scheme, not ambient equations. | PASS |
| Actual-CI bridge | STCI-R-0006 requires saturation, everywhere generation, full prescribed coprime initial ideal, gap at least two, and smooth full root. | PASS |
| Carrier classification | STCI-R-0002 requires one Cartier inverse curve mapping isomorphically; its three fixed-curve models are necessary, not constructions. | PASS |
| Conductor | STCI-R-0003 requires full inverse support and full conductor-unit descent; nilpotent defects cannot be ignored. | PASS |
| Phase reduction | STCI-R-0004 is a restricted projection-family reduction; phase images and torsion cosets are not computed. | PASS |
| Historical records | Earlier quartic-mate “open” labels are superseded by STCI-R-0001, but distinct ancestor questions remain open. | PASS |
| Chapter status | Chapters 2–6 have now been merged into main, despite earlier status notes in conversation. | PASS as of audit |

## Priority correction

Use explicit notation \(r_F,r_G\) when discussing the generic orders of the *displayed equations* and \(\rho,\sigma\) when discussing the degrees of the **minimal full initial-ideal generators**. These numbers can differ: for example, \((u^2,u^2+v^3)=(u^2,v^3)\) has displayed orders \((2,2)\), but initial-ideal generator degrees \((2,3)\). The formal bridge theorem itself retains the notation \(r,s\) in its canonical source; the synthesis should translate it, not rewrite the theorem.

## Audit limitations and follow-up

- This audit did not rederive the normal/non-normal quartic classification or the independent October 11 proof assembly.
- It did not compute new root obstruction loci, conductor phase images, or higher-degree carrier exclusions.
- The next source-level audit should focus on the **generic common-normal-factor claim** in historical P-006, identifying its precise hypotheses and whether they suffice for the actual-pair root construction proposed in Chapter 6.
- A separate mechanical relative-link check may be useful; this document makes no claim to have exhaustively checked every link.

**Conclusion:** The exposition has no identified global-status contradiction, but it benefits from a notation correction at the Chapters 2–3 interface. The proposed new common-factor/root comparison remains a research problem, not a theorem.
