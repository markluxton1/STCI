# Review feedback: all-degree torus movement bounds

Review target: commit `0bf65a3720a7373f79821d8e7ee166638b01fbb1`. This is a review handoff for the authoring agent, **not** a new mathematical result or a verification certificate. Remove this temporary note after resolving its actionable points; preserve only substantive improvements in the canonical Result, Argument, Framework, and Investigation objects.

## Assessment

R-0072 is an important structural advance: actual homogeneous equations constrain the splitting filtration and first-order variation of the **entire** moving transverse quotient, uniformly in characteristic-zero bidegrees and without classifying transverse singularities. The one-summand control demonstrates that the CI Hilbert polynomial and large total Plücker degree are insufficient. This improves the route from actual equations to geometric constraints; it does not establish a new general degree exclusion.

## Requested revisions

1. **Proof readability (R-0072).** Isolate the multiplicativity of the splitting filtration, `B_{>=i} B_{>=j} ⊆ B_{>=i+j}`, as a short lemma, including the assertion that its positive part is an ideal and the Laurent-weight separation argument for actual components of F. Explain why these are intrinsic to the quotient bundle, not chosen splittings. Keep the proof geometric and avoid computational expansion.
2. **Precision in summaries.** Explicitly distinguish the rank of the induced tangent map `K_x → B_x` from the dimension of the image of the classifying morphism (the base is one-dimensional). Clarify that generic secant rank need not persist at the two special fibers; equation (3) is necessary and does not prove an endpoint exclusion.
3. **Strategic framing (research map and I-0002).** Identify the central missing implication as **global two-generator/equation-module compatibility**: which further restrictions on a moving quotient follow from being the entire torus modification of a saturated two-generated homogeneous ideal, beyond splitting, generic ranks, Hilbert polynomial, and both endpoint image algebras? Sharpen I-0002's next decision to one bounded compatibility theorem or explicit counterexample, rather than general endpoint enumeration.
4. **Control interpretation.** Make the one-summand example's logical role explicit: it defeats numerical Hilbert/total-movement tests but is not evidence that the new splitting bounds suffice for realization. Keep the example in its existing argument home, with a reference from R-0072; avoid another duplicate Result.
5. **Literature discipline.** Before developing a new equation-module construction, check established Rees/symmetric algebra and approximation-complex methods and identify exactly what they do and do not already imply for this saturated two-generator problem. Do not present a new theorem or investigation unless a concrete gap remains.

## Scope and acceptance

Do **not** add another framework, launch degree-by-degree splitting enumeration, or expand the repo's permanent inventory. Preserve the current four-object ownership structure. Implement only nonredundant edits in canonical files, and report which requests were already satisfied or deliberately declined, with reasons. The theorem's proof dependencies and its claimed review status were not independently reverified in this feedback pass.
