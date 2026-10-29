# Quintic h2: research status and next steps

## Current result

The characteristic-zero degree-five (j=0) branch of the necessary common-conormal-quadratic/conductor-support incidence has been excluded. See [proof](quintic-h2-degree-five-exclusion.md) and [exact verifier](../computations/verify_quintic_h2_degree_five.py). This is not an STCI nonexistence theorem. The degree-six (j != 0) branch remains unresolved. The global model, including the discriminant-zero and inverse-map boundaries, is [here](2026-10-15-generalization-quintic-h2-global-monic-ODE-incidence.md).

## Recommended continuation, when research resumes

1. **Degree-six local test.** Compute the primitive conductor's vanishing order at x=0 on j != 0. Test whether conductor divisibility and H*Q'=(6*x+u)*Q constrain H as sharply as in degree five. Do not assume the degree-five pure-power form.
2. **If the local test reduces parameters**, carry out exact elimination using the authoritative primitive conductor and the smallest necessary coefficient comparisons; retain all required open conditions and repeated-root cases.
3. **If it does not**, study the support geometry and symmetric-power/spectral constraints before attempting large saturation computations. Set a computational stopping criterion.
4. **After degree six**, assess whether the obstruction mechanism extends to higher projection degrees. If it is confined to the quintic configuration, prioritize the global degree-growth problem (freedom versus constraints, residual curves allowed) instead of overinvesting in one projection lane.

## Repository handling

This is a forward-looking investigation agenda, not a promoted result. Preserve mathematical reductions, hypotheses, boundary cases, exact computational inputs and useful failed approaches; do not preserve ordinary error histories or check logs. Keep the h2 investigation coherent and link reusable conductor theory rather than duplicating it. No changes to the main branch.
