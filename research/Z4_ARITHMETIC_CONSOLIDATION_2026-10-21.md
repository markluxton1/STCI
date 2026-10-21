# Z4 arithmetic obstruction: consolidated research dossier (2026-10-21)

**Branch:** `research/z4-arithmetic-obstruction-consolidated-2026-10-21`  
**Status:** research evidence and navigation, **not canonical theorem promotion**. Based on `main`; original branches remain intact. This index does not override `research/results/`, `research/AUTHORITY.md`, or `AGENTS.md`.

## Reading order, status, and provenance

| Stage | Local evidence | Original branch | Status |
| --- | --- | --- | --- |
| 1. Intrinsic thickening literature | [Literature investigation](notes/2026-10-21-z4-intrinsic-obstruction-literature.md) | `research/z4-intrinsic-obstruction-literature-2026-10-21` | Literature framing, not an obstruction theorem |
| 2. Intrinsic embedded ribbon-to-triple construction | [Original construction](notes/2026-10-21-intrinsic-embedded-ribbon-triple-obstruction.md) | `research/intrinsic-ribbon-triple-2026-10-21` | Historical proposal; consult corrected audit |
| 2. Independent theorem audit | [Corrected theorem and audit](notes/2026-10-21-intrinsic-ribbon-triple-independent-audit.md) | `research/intrinsic-ribbon-triple-audit-2026-10-21` | Independently audited, with exact hypotheses |
| Arithmetic precursor | [Divided-Frobenius origin](notes/2026-10-21-z4-divided-frobenius-origin.md), [quadratic decomposition](notes/2026-10-21-z4-quadratic-source-decomposition.md), [coordinate-invariance counterexample](notes/2026-10-21-z4-coordinate-invariance-counterexample.md), [script](computations/verify_z4_divided_frobenius_2026_10_21.py) | `research/z4-divided-frobenius-2026-10-21` | Exploratory arithmetic; isolated quadratic summands are not intrinsic |
| 3. Persistent relative obstruction | [Proposed theorem](notes/2026-10-21-z4-persistent-arithmetic-obstruction.md), [script](computations/verify_z4_persistent_obstruction_2026_10_21.py) | `research/z4-persistent-arithmetic-obstruction-2026-10-21` | Original claim; qualified by independent audit |
| 3. Independent audit | [Verdict B and relative Ext correction](notes/2026-10-21-z4-persistent-independent-audit.md), [audit script](computations/audit_z4_persistent_relative_2026_10_21.py) | `research/z4-persistent-independent-audit-2026-10-21` | Fixed *marked integral embedded deformation problem*; divided first-order Yoneda differential; script reported locally passing at commit `752e38d` |
| 3. Additional global check | [Laurent coordinate supplement](notes/2026-10-21-z4-global-laurent-coordinate-supplement.md) | User-reported after audit | One reported global Čech-coboundary check; **not independently reproduced in this consolidation** |
| 4. General \(p^r\) mechanism | [Preliminary investigation](notes/2026-10-21-investigation-4-general-pr-mechanism-preliminary.md) | This consolidation, based on conversation analysis | Universal binomial identities and a split-geometry counterexample; **not independently audited** |

## Precise mathematical boundary

For the fixed marked integral embedded \(Z_4\) problem over \(\mathbf Z_{(2)}\), the audited calculation yields the leading divided obstruction
\[
\lambda(\alpha,\beta,\gamma)=\gamma[u^{-1}]+[u^{-2}]+\alpha[u^{-3}],
\quad
D(\alpha,\beta,\gamma)=\gamma[u^{-1}]+\alpha[u^{-3}].
\]
Thus \(\operatorname{rank}D=2\), and the leading class has nonzero image in the one-dimensional \(\operatorname{coker}D\); its Serre-dual annihilator is \(\langle st\rangle\). The map \(D\) is the differential of the **divided first-order Yoneda obstruction**, not the ordinary differential of the undivided integral obstruction. The relative-Ext construction and marking are essential. Do not assert this is an invariant of an unmarked abstract characteristic-two curve.

No canonical divided-Frobenius operation into this cokernel has been proved. Investigation 4 does not generalize nonvanishing automatically to all \(p^r\); the split conormal example gives a counterexample to such a claim.

## Repository policy and verification

This branch copies source reports and scripts without rewriting their historical claims. The inherited `main` research records are unchanged. Do not promote claims based on this index; follow [authority policy](AUTHORITY.md) and review the corrected theorem/audit evidence.

The copied scripts have **not** been executed in the consolidation environment. The user's prior local execution of the persistent-audit script passed four checks; that report is retained as provenance, not misrepresented as a new run. The global Laurent supplement records a reported calculation without an accompanying reproducible script. Investigation 4 remains preliminary and requires its own independent audit before promotion.
