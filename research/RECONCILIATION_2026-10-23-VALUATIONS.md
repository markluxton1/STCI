# October 23, 2026 — higher initial ideals and valuations branch reconciliation

**Status:** Research-note intake and mathematical consistency audit. **No canonical theorem promotion.** Branch: `research/higher-initial-ideals-valuations-2026-10-21`. The four notes are provisional research material; accepted canonical statements remain governed by their result records and the authority policy.

## Intake

- [Equality, generic orders, Hilbert filtration, duality](notes/2026-10-21-equality-orders-filtration-duality.md): generic transverse multiplicity, full initial algebra, ordinary nilradical filtration and cautions about unsaturated graded duality.
- [Higher initial ideals and valuations](notes/2026-10-21-higher-initial-ideals-valuations.md): cancellation/standard-basis examples, base-sensitive valuations, characteristic benchmark and globalization limits.
- [Residual-cycle identity and wedge distinctions](notes/2026-10-21-residual-cycle-proposition-audit.md): elementary Bézout cycle identity, singular differentials versus smooth tangency, and local countermodels to a general wedge obstruction.
- [Valuative standard-basis criterion](notes/2026-10-21-valuative-standard-basis-criterion.md): finite-free local argument, special-fiber length, total generic-fiber dimension and transverse length along C.

## Audit decisions and precise boundaries

1. For a proper projective complete intersection containing the fixed quartic, the **elementary** identity `de=4m_C+deg R` follows from Bézout and purity. It is distinct from [STCI-R-0019](results/quasiprimitive_residual_cycles.md), which is a conditional residual **zero-cycle** theorem on an auxiliary smooth surface requiring finite-flat curvilinearity, saturation and proper intersection.
2. For the local complete intersection `A=k[[t,x,y]]/(F,G)`, finite special-fiber length implies finite freeness over `k[[t]]`. Its total generic-fiber dimension `rho_p` equals the special length `lambda_p`; the completed local factor along C has transverse length `m_C`, so `lambda_p=rho_p>=m_C`. The inequality can be strict when residual components contribute. This local test does not independently exclude a global STCI.
3. The degree-`d`, order-`r` conormal symbol is a section of `Sym^r(N_C^vee) tensor O_C(d)`; with the characteristic-not-two balanced splitting its summands are `O_{P1}(4d-7r)`, **not** `O_C(d-7r)`. [STCI-R-0020](results/quartic_conormal_characteristic_jump.md) governs the characteristic dependence.
4. The prescribed quartic equations have four distinct characteristic-zero components and characteristic-two support C with generic length four; this is the scoped theorem [STCI-R-0021](results/quartic_mu4_degeneration.md), not a general assertion about quartic pairs.
5. A zero differential along C detects a singular carrier; proportional **nonzero** differentials detect tangent smooth carriers. Neither proportionality nor wedge vanishing alone forces a residual curve. No general common-singularity or global wedge-obstruction theorem is claimed.
6. Ordinary graded Gorenstein duality is **not** inferred from Gorensteinness of the filtered local complete intersection. Conditional normal-flatness and defect theorems [STCI-R-0010](results/saturated_first_relation_normal_flatness.md) and [STCI-R-0016](results/nonsaturated_first_relation_resultant.md) retain their stronger hypotheses.
7. Generic standard bases cannot simply be specialized when leading coefficients vanish; local valuations and initial factors do not by themselves prove global component existence. The incomplete quartic embedding and saturation must be respected.

## Disposition

Retain all four notes as **research notes**, linked through [research navigation](INDEX.md); do not assign new STCI-R IDs, change canonical theorem scopes, or claim a new STCI exclusion. The further separation-divisor / conormal / valuation investigation is deferred to a separate research task.

**Merge preparation:** The branch diverged from main during this audit; review its final diff against current main and check navigation/links before merging. This reconciliation record documents the branch review, not an independent verification of every possible downstream application.
