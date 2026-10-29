# Phase 2 Step 1B — destination reconciliation checkpoint 3

Date 2026-10-29. Branch `restructure/mathematical-consolidation`. Mathematical preservation audit only; not a proof audit, integration, or source deletion.

## Actual owner comparison: quartic carrier

Compared `research/chapters/CARRIER_AND_CONDUCTOR_GEOMETRY.md` and `research/MATHEMATICAL_CONSOLIDATION_QUARTIC_CARRIER_DEPENDENCIES.md` against `research/notes/2026-10-10-session-genus-two-trisecant-quartic-carriers.md` and intake batch 2.

**PARTIAL — genus-two trisecant carrier ideal.** The owner chapter §§3.4–3.5 retains the nonendpoint/endpoint division and requirement to exhaust all quartics; the dependency DAG retains proof-source links. Neither owner text spells out the exact homogeneous ideal
`I(C0) ∩ (z,w)^2=(qz,qw,T_a)`, `T_a=D-2aB+a²A`, or the eleven-dimensional quartic family `F=qQ+T_a L0` (7+4 dimensions). The source proves the ideal/line classification, while discriminant exclusion is conditional on the actual blowup/conductor identification. **Step 2 P1:** preserve these exact formulas and conditional boundary in carrier chapter §3.4, referencing the source for full proof. Verification required before any promotion of the conditional discriminant argument. Owner: quartic carrier/genus-two.

**PARTIAL — genus-two line classification.** Source gives two geometric types `Gamma_1` (three distinct contacts) and `Gamma_0` (triple contact), using ruling of the unique quadric; the chapter distinguishes the endpoint cases but does not preserve the explicit `Gamma_a=(x2-a x0,x3-a x1)`, `Gamma_infinity=(x0,x1)` and cube-root caveat for non-algebraically-closed fields. **Step 2 P2:** add concise explicit line classification in same chapter. Owner: genus-two quartic carriers.

**PRESERVED at theorem-structure level — quartic carrier six-lane exclusion.** The carrier chapter and dependency DAG distinguish normal, genus zero, genus one, genus-two bisection, nonendpoint and endpoint. This does not certify every lemma or example preserved. R-0001 authority is not changed.

**PARTIAL — A3+2A1 / four-A1 negative projection examples.** Carrier chapter §3.2 outlines ADE genus-one exclusion; main normalization dossier §21 explicitly warns four-A1 family does not exhaust the lattice stratum. The specific four extra inverse points of A3+2A1 and non-Cartier class of four-A1 require exact owner placement. **Step 2 P2:** retain separate explicit negative examples in genus-one chapter, with source scope and no universal projection exclusion.

## Actual owner comparison: thick equality boundary

Compared `research/notes/2026-10-07-thick-boundary-carrier-rigidity.md` to `research/MATHEMATICAL_CONSOLIDATION_PROJECTIONS_AND_THICK_CONTACT.md` and carrier chapter. **PARTIAL:** the consolidation map records entirely-thick inequalities and (3,4) repeated-root geometry but omits the precise equality-case restriction `F|Q=h^pR_F`, `R_F in H^0(Q,O(2p,0))`, exact h-order p, and `r<=min(p,q)` distinct ruling factors for an STCI equality pair. Original source also retains the ambient lifting open problem `H^0(I_C^p(3p))` and its associated-graded map. **Step 2 P1:** filtered/thickening owner should retain exact theorem and open lifting question, cross-reference from carrier chapter. Do not infer reducibility or normality.

## Actual source comparison: positive-characteristic cuspidal quartic

Read `research/notes/2026-10-05-positive-quartic-carrier-optimality.md`. Its fixed carrier is `F=x0*x3^3-x2^4`; exact mate degrees: char 0 none, char 2 iff 4|N, char 3 iff 3|N, char 5 iff 25|N, char p>=7 iff p|N. The criterion is `p^{v_p(N)} in <3,4>` from the semigroup of the normalization; it is NOT a universal minimum-degree theorem. **NEEDS REVIEW:** permanent positive-characteristic owner has not yet been inspected; source alone is not destination preservation. **Step 2 P1:** find owner and preserve exact semigroup criterion and exceptional p=5.

## Actual owner comparison: intrinsic geometry

Compared `research/INTRINSIC_GEOMETRY_INTERLUDE_2026-10-24.md` and `research/synthesis/normalization_conductor_phase2_addendum.md` to intake batch 13. **PARTIAL:** the interlude is a research-question map, not a proof destination. It records the P4 projection, cubic R, duality and characteristic issues as questions; the addendum retains F1/F4 normalization/conductor mechanisms but not the full Gauss-dual formulas or the complete P4 resolved-projection computations. **Step 2 P2:** inspect other permanent intrinsic geometry result/chapters; if absent, assign a single primary intrinsic geometry destination. Do not count a question as preserved mathematics.

## Actual source comparison: intrinsic quintic A4 pair

Read `research/notes/2026-10-11-session-dp5-a4-intrinsic-pair-classification.md`. It proves, under genus-one/A4/char-zero hypotheses, the plane cluster `(y-x^3,x^4)`, unique smooth conic orbit, `c+ell~H`, and two distinct projection-center lanes, with nonendpoint modulus. **NEEDS REVIEW:** dedicated permanent quintic owner not yet located and read. **Step 2 P1:** verify exact cluster, automorphism action, center modulus and source scope in permanent quintic destination; do not treat intrinsic classification as mate exclusion.

## Priority and ownership update

P1: genus-two ideal and conditional discriminant; thick equality theorem; positive-characteristic exact mate degrees; quintic A4 owner lookup.
P2: genus-two explicit line types; ADE family examples; intrinsic F1/F4/P4 dual formulas.
General conductor theory remains owned by `normalization_conductor_projection.md`; case-by-case quartic genus-two/ADE by carrier chapter; thick equality by filtered-thickening; quintic A4 by dedicated quintic owner; F1/F4/P4 by intrinsic geometry; characteristic-dependent carrier example by positive-characteristic owner.

## Running status

This checkpoint adds eight distinct grouped mathematical comparisons with source-level inspection in four primary notes and destination inspection in four permanent texts. Classification: one structural PRESERVED, five PARTIAL, two NEEDS REVIEW (the grouped intrinsic and ADE findings may contain further individual subclaims). This is **not** a count of all distinct contributions among 549 sources. Earlier checkpoints 1 and 2 remain in force; this document refines, rather than duplicates, their entries.

Step 1B **NOT CLOSED**: authoritative deduplicated claim inventory across all intake batches, precise destination audit of remaining cross-family owner texts, complete gap register and final coverage certificate are still required. No theorem promotion or changes to `main`.
