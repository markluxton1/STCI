# Formal normal geometry: research questions and proof obligations

**Status:** provisional questions, not promoted canonical question records.
**Starting point:** [formal normal geometry](../frameworks/formal-normal-geometry.md); follow [authority policy](../AUTHORITY.md) and [frontier](../FRONTIER.md).

## Central problem: simultaneous realization

Fix the smooth rational quartic C in P^3 over an algebraically closed field of characteristic zero. Put K=k(C), and let J_eta be a finite-colength ideal of K[[X,Y]] specifying a candidate embedded generic thickening.

Study the **simultaneous** existence and compatibility of:
- a coherent ambient ideal sheaf J contained in I_C, defining a subscheme T of P^3 containing C, whose completed localization at the generic point eta_C of C equals J_eta. No condition sqrt(J)=I_C is imposed: T may have additional components;
- two distinct integral surfaces X_F and X_G containing the same ambient thickening, with (F),(G) contained in J;
- equality J=(F,G), when the candidate thickening is intended to be the complete intersection itself;
- the further set-theoretic condition V(F,G)_red=C.

Do not assume the last condition while studying the preceding ones. In particular, Z=V(F,G) may have components distinct from C, and a thickening T contained in Z need not equal Z.

## Priority A: compare the three normal constructions

Precisely relate the J-adic associated graded algebra of O_Z (J=I_C O_Z), its normal cone/projectivization, and the intersection of the strict transforms of X_F and X_G with E in Bl_C(P^3). Identify the exact ideals, saturations and maps involved. Prove which data are intrinsic to (F,G) and which depend on the chosen generators or ambient carriers. Do not conflate leading forms of generators with the full initial ideal.

## Priority B: detect extra components

For Z with C contained in Z_red, determine which features of exceptional scheme structure can imply an additional one-dimensional component downstairs, and which arise from a nonreduced thickening supported on C or special-point exceptional geometry. Explicitly address what generic completion over K cannot detect, including components meeting C only at special points. Seek necessary/sufficient criteria with precise hypotheses; do not infer an extra component merely from a vertical exceptional curve.

## Priority C: local-to-global compatibility

Identify obstruction and lifting conditions for a finite-colength K[[X,Y]] ideal to spread out along C, embed in P^3, be supported on each of two integral surfaces, and equal their intersection. Incorporate the normal bundle O(7)^2 and global degrees only where needed. Distinguish formal, algebraic, and projective realizability. Treat the two carriers symmetrically.

## Priority D: successive blowups and valuations

Investigate whether valuations/weighted initial ideals organize the successive normal directions and exceptional components into intrinsic structural data. Work over K, its algebraic closure, or a completed valued extension only after specifying the field and valuation. A completion k((t)) at a point of C is not K or its algebraic closure. Tropical language should help formulate and prove theorems about cancellation and initial ideals, not motivate large enumerations of examples.

## Priority E: multiplicity two as a test

For generic intersection length two, seek a theorem describing possible local complete-intersection structures and their behavior under blowup, allowing Z to have other global components. State separately what follows locally, what requires a global ambient realization, and what the STCI assumption would add. Do not impose arbitrary orders r,s without checking compatibility with length two.

## Required proof discipline

For each proposed result: state hypotheses, precise conclusion, proof or counterexample, dependence on existing canonical results, and what remains open. Search the repository and literature before claiming novelty. The unrestricted characteristic-zero STCI question remains open in the repository's authority model. The assertion that every STCI pair has a common singular point on C is not available as a general premise without an audited proof. Existing integral-quartic-carrier exclusions are not to be reopened as live cases.

## Success criterion

A useful outcome is one rigorously proved structural implication connecting **at least two** of the realization levels, with a clear account of how exceptional geometry records (or fails to record) compatibility. An explicit computation alone is not the desired outcome.
