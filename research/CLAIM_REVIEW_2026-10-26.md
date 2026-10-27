# Claim-level review: first source-linked tranche (October 26)

Status: documentary examination of named source audits, not fresh execution or canonical promotion. Every claim below remains subject to the precise hypotheses of its cited note.

| ID | Claim and scope | Source | Decision / remaining gate |
|---|---|---|---|
| CR-01 | For a proper CI containing the fixed quartic, de = 4m_C + degree(R). | notes/2026-10-25-ci-cycle-valuative-audit.md section 1 | Reviewed elementary cycle identity. Distinct from R-0019 zero-cycle theorem. |
| CR-02 | At the generic point, a two-generator parameter ideal has colength equal to Hilbert-Samuel multiplicity; full adapted Rees valuations recover that multiplicity. | valuative audit sections 2-3 | Reviewed local claim; no universal upper bound follows. |
| CR-03 | Complete weak-transform cluster formula m_C = sum of residue degrees times squared weak orders. | valuative audit section 4 | Reviewed with complete cluster and total-transform basis; partial clusters give lower bounds only. |
| CR-04 | A proper CI has nonzero residual cycle iff its local curve multiplicity exceeds m_C at some point of C. | valuative audit section 7 | Reviewed using connectedness; verify exact local conventions for canonical record. |
| CR-05 | Valuative residual contact is exceptional intersection of the strict residual cycle; contact degree at most three times residual degree. | valuative audit section 7 | Reviewed; no residual existence follows without a positive witness. |
| CR-06 | Explicit rational quartic pair has ideal intersection I_C intersect I_D, with D smooth geometrically integral of degree 12 and genus 16, meeting C transversely at 18 non-endpoint points. | notes/2026-10-25-ci-cycle-smooth-residual-audit.md | Independent rational computation reported; fresh Macaulay2 replay remains. Example, not universal statement. |
| CR-07 | A special residual degenerates to a line plus smooth degree-11 genus-12 curve, with five nodes and 18 total C attachments. | notes/2026-10-25-ci-cycle-line-degeneration-audit.md | Reported independently audited; replay exact equations before promotion. |
| CR-08 | Fixed-boundary pencil tangent ranks are 19, 5, 24; boundary fiber dimension 14 with independent smoothing of five nodes and nine further formal parameters. | notes/2026-10-26-ci-cycle-fixed-boundary-node-smoothing-audit.md | Reviewed formal/etale local result, not explicit global polynomial arc. |
| CR-09 | For selected sextic F*, degree-16 forms with generic contact at least 12 modulo F* are precisely degree-10 global multiples of F*. | notes/2026-10-26-endpoint4-nonsplit-node-scope-audit.md | Two finite certificates report rank 683 and kernel dimension 286. Review corrected assignment and modular rank lifting; no fresh replay. |
| CR-10 | The selected F* has a nonsplit generic node over k(C); finite-length intersections have multiplicity 2n and contact order n modulo F*. | endpoint4 nonsplit-node scope audit | Independent local argument reviewed; distinguish constant-field extensions from algebraic closure of k(C). |
| CR-11 | Every proper degree-16 mate of this fixed F* has m_C at most 22 and residual degree at least 8. | endpoint4 nonsplit-node scope audit | Depends on CR-09 and CR-10. Strong fixed-carrier promotion candidate; no whole-family conclusion. |
| CR-12 | The comparison defect fits an exact filtered sequence and vanishes wherever either carrier is smooth along C. | RECONCILIATION_2026-10-24-IDEAL-FILTRATIONS.md | Provisional: check sheafification, spectral-sequence conventions, punctual defect and radical support. |
| CR-13 | In prescribed characteristic-two quartic example, defect vanishes and a stated kernel is O(-24). | ideal-filtration reconciliation | Example-specific provisional; compare with R-0021 and replay. |
| CR-14 | Wedge vanishing alone does not force a residual curve. | RECONCILIATION_2026-10-23-VALUATIONS.md | Reviewed correction; do not assert universal wedge obstruction. |

## Dependency and conflict findings

- CR-11 requires both the global jet-kernel identity CR-09 and the nonsplit-node local lemma CR-10.
- CR-06 rules out universal concentration of residual attachment at the two special endpoints.
- CR-08 separates fixed boundary from residual topology, but proves no explicit global polynomial smoothing arc.
- CR-03 cannot be replaced by fixed monomial weights or an incomplete cluster.
- CR-12 does not establish existence of simultaneous singularities of the two carriers.
- R-0001 and R-0020 through R-0022 are already promoted and must not be reopened or duplicated by this review.

## Remaining claim-level work

Extract and reconcile individual claims in the flag/duality, ruled-surface, and intrinsic K3 notes. Then inspect the historical notes and scratch tree with a complete path manifest. This first tranche does not certify an exhaustive repository-wide claim inventory.
