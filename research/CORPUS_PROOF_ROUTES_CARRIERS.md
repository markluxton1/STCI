# Quartic-carrier proof-route inventory — STCI-R-0001

**Status:** source-text classification of proof roles, not an independent mathematical verification. Based on full reads of the ten named Arguments and the Result on the inventory branch. No source content is moved or rewritten.

## Exact Result and limits

[STCI-R-0001](results/quartic_carrier_exclusion.md) states: over an algebraically closed field of **characteristic zero**, for the fixed quartic \(C_0=[s^4:s^3t:st^3:t^4]\) (and projectively equivalent embeddings), **no integral quartic** \(X\supset C_0\) and homogeneous positive-degree \(G\) have \(V(X,G)_{\rm red}=C_0\). The mate degree is unrestricted. This does not solve characteristic-zero STCI with both degrees at least five. In positive characteristic, the same fixed embedding admits quartic-carrier STCI pairs.

## Route classification by mathematical function

| File | Role and scope | Relationship to R-0001 | Retrieval decision |
| --- | --- | --- | --- |
| [quartic_carrier_proof.md](arguments/carriers/quartic_carrier_proof.md) | Common support/divisor reduction, normal quartics, genus 0 and 1, genus 2 stratification, exhaustive assembly | **Full theorem assembly**, not an alternative proof to the following case arguments | Read first for full exclusion; use relevant numbered section for a single case |
| [genus_two_entire_conductor_proof.md](arguments/carriers/genus_two_entire_conductor_proof.md) | Entire conductor and double-cover geometry in the genus-two normalization setting | **Upstream structural lemma**, explicitly not mate exclusion | Fetch for conductor or descent hypotheses |
| [genus_two_ambient_conic_model_proof.md](arguments/carriers/genus_two_ambient_conic_model_proof.md) | Ambient line-blowup model, normal ADE strict transform and crepancy, given genus-two adjoint/conductor inputs | **Upstream geometric proof**, explicitly not mate exclusion | Fetch for ambient conic model and local attachments |
| [genus_two_bisection_proof.md](arguments/carriers/genus_two_bisection_proof.md) | \(\lambda=0\) bisection case; actual Cartier double and conormal-map contradiction; retains full fiber-weight analysis | **Specialized case proof**, not a second full proof of R-0001 | Fetch for genus-two bisection only |
| [genus_two_trisecant_carrier_proof.md](arguments/carriers/genus_two_trisecant_carrier_proof.md) | Actual trisecant carrier ideals; narrower nonzero-discriminant obstruction and unconditional line classification | **Complementary narrower argument**, not exhaustive for repeated discriminants/endpoints | Fetch for exact carrier equations or discriminant lane |
| [genus_two_nonendpoint_proof.md](arguments/carriers/genus_two_nonendpoint_proof.md) | \(\lambda=1\), nonendpoint trisecants; divisor exhaustion and all-length chain inequality | **Specialized case proof** requiring actual conic model, conductor, and special prime | Fetch for distinct/nonendpoint contact |
| [genus_two_endpoint_proof.md](arguments/carriers/genus_two_endpoint_proof.md) | \(\lambda=1\), endpoint triple contact; full quartic family, chart cases, ADE corrections | **Specialized case proof**; not interchangeable with nonendpoint proof | Fetch for endpoint lane |
| [genus_two_endpoint_local_corrections.md](arguments/carriers/genus_two_endpoint_local_corrections.md) | Formal factorizations and precise exceptional attachment positions for endpoint and doubled-horizontal subcases | **Local technical lemmas** used by endpoint proof | Fetch only for local correction calculation |
| [quartic_projection_center_moduli.md](arguments/carriers/quartic_projection_center_moduli.md) | Projection-center quotient and characteristic-two Hasse-contact comparison | **Independent exploratory geometry**, not an unrestricted mate exclusion | Do not load for R-0001 proof unless studying projection moduli |
| [quartic_singular_support_singleton_fibers.md](arguments/carriers/quartic_singular_support_singleton_fibers.md) | Reduced singular-curve support bounds, conditional Hessian/contact statements | **Independent bounded results**, not unrestricted mate exclusion | Fetch only for reduced support/singleton questions |

## Conclusions for context refactoring

1. The large assembly proof and specialized genus-two arguments have **different logical jobs**. They should **not** be deduplicated merely because each mentions the quartic-carrier exclusion.
2. The Result already states the theorem separately from the proof. Its `evidence` field mixes the assembly with specialized cases and inputs. A future metadata-only cleanup can distinguish **assembly route** from **dependencies**; do not declare six independent full proofs.
3. The upstream conductor and trisecant files are discoverable from Argument links even though not all are in the catalog-linked 127-file index. A catalog-only file count is inadequate.
4. Long Arguments can be retrieved by sections without splitting. Any physical split must preserve exact hypotheses, stable anchors, and dependency links.
5. The claim that the carrier proof is complete is **recorded source status**. This inventory has not independently checked every calculation, external theorem, or historical certificate.

## Representative retrieval tasks

- **State R-0001 and its characteristic boundary:** fetch [Result](results/quartic_carrier_exclusion.md), not the entire proof collection.
- **Explain genus-two bisection contradiction:** fetch [assembly §6.1](arguments/carriers/quartic_carrier_proof.md#61-bisection-the-global-nilideal-obstruction), then [bisection proof](arguments/carriers/genus_two_bisection_proof.md); consult entire-conductor input only when needed.
- **Check endpoint attachment formula:** fetch [endpoint local corrections §1 or §2](arguments/carriers/genus_two_endpoint_local_corrections.md), then the relevant [endpoint proof](arguments/carriers/genus_two_endpoint_proof.md).
- **Understand nonendpoint all-length inequality:** fetch [nonendpoint proof §4](arguments/carriers/genus_two_nonendpoint_proof.md#4-exact-all-length-contradiction) with its stated model hypotheses.

These are navigation routes, not claims that the abbreviated context suffices to independently certify the full theorem.

## Further inspected specialized files

| File | Classification | Why retained separately |
| --- | --- | --- |
| [genus_two_bisection_three_center_proof.md](arguments/carriers/genus_two_bisection_three_center_proof.md) | **Narrower conditional obstruction** for three-center fibers; 11,305 characters | Explicitly leaves the four-single-center partition, whereas the global ribbon argument excludes the entire bisection lane |
| [genus_two_marking_and_section_proof.md](arguments/carriers/genus_two_marking_and_section_proof.md) | **Reusable marking and proximity geometry**; 27,830 characters | Does not claim abstract root configurations are all realized and is not another complete quartic-mate exclusion |

The global bisection ribbon proof and the three-center fiber obstruction use substantively different mechanisms, but **only the former is presented as covering the whole bisection lane**. This is a genuine reason to retain both files rather than merge them as duplicates.
