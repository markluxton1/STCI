---
id: STCI-R-0022
title: "Filtered-contact exclusion of a (4,4) STCI of the fixed rational quartic"
kind: theorem
status: proved
scope:
  characteristic: "0"
  curve: "fixed C0=[s^4:s^3t:st^3:t^4]"
  hypotheses:
    - "Algebraically closed field of characteristic zero"
    - "Integral or, more generally, coprime quartic defining equations F,G with reduced intersection C0"
    - "Accepted saturated quasiprimitive Gorenstein filtration and primitive e=1 triple classification in the cited source notes"
statement: "No two quartic forms F,G have radical (F,G)=I_C0. This narrower filtered-contact proof does not invoke the all-degree quartic-carrier exclusion STCI-R-0001."
dependencies:
  - "STCI-R-0020"
evidence:
  - "research/notes/2026-10-23-quartic-44-filtered-proof-proposal.md"
  - "research/notes/2026-10-05-mf6-pairing-audit.md"
  - "research/notes/2026-10-07-session-mf6-e1-independent-audit.md"
  - "research/computations/verify_44_filtered_contact_2026_10_23.py"
  - "research/computations/audit_mf6_e1_primitive_2026_10_07.py"
independent_audits:
  - "research/notes/2026-10-23-quartic-44-filtered-proof-independent-audit.md"
  - "research/computations/audit_44_filtered_contact_2026_10_23.py"
accepted_in: "research/RECONCILIATION_2026-10-23-44.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Does not exclude mates of degree other than four."
  - "Relies on explicitly identified accepted filtration and e=1 primitive-triple classification inputs, not on symmetric algebra alone."
---
# Filtered-contact (4,4) exclusion

## Statement
Over an algebraically closed field of characteristic zero, no two quartic equations cut out the fixed smooth rational quartic set-theoretically.

## Hypotheses and quantifiers
The fixed embedded C0 and characteristic zero are essential. A proper quartic intersection with reduced support C0 would have generic transverse length four.

## Proof outline
A quartic vanishing to normal order at least two must be a scalar multiple of q², and cannot belong to a valid STCI pair. Thus both orders are one. The saturated Gorenstein filtration of the length-four complete intersection gives E3=O(-18), perfect graded pairings, and D2=D3. Effectivity leaves e=0 with degree-three defect, or e=1 with no defect. The complete quartic contact spaces in the three e=0 orbits and four e=1 primitive orbits are classified in the cited notes. Factored cases cannot yield a proper pair; each remaining two-dimensional pencil has nonzero cubic-contact determinant h0 tau1−h1 tau0, forcing generic length three, contradicting length four.

## Alternative K3 proof

An independently audited alternative proof of the same characteristic-zero (4,4) exclusion uses the saturated Gorenstein filtration and the exceptional lattice on a K3 resolution, rather than the primitive e=1 classification. For a hypothetical quartic pair supported only on C, the possible filtration types have (e, deg D) equal to (1,0) or (0,3). The actual first-symbol pencil has degree 6+2e after its fixed divisor is removed. A general quartic pencil member has moving A3 singularities and defect singularities of type A_(2d-1). Its K3 resolution would have exceptional rank 24-r, at least 21, contradicting the characteristic-zero Picard-rank bound of 20.

This is an alternative proof, not a new theorem or an all-degree statement. See the proof and independent audit:
- research/notes/2026-10-23-intrinsic-44-k3-proof-proposal.md
- research/notes/2026-10-23-intrinsic-quadruple-local-algebra.md
- research/notes/2026-10-23-intrinsic-44-k3-independent-audit.md

## Dependencies
The conormal splitting is STCI-R-0020. The saturated pairing and e=1 classification are accepted **source-level prerequisites**, explicitly not separately promoted as ID-bearing theorems. Neither STCI-R-0001 nor its proof is an input.

## Evidence and verification
Independent mathematical review is recorded in the linked October 23 audit. Clean [GitHub Actions run 39972680627](https://github.com/markluxton1/STCI/actions/runs/39972680627) passed both independent contact checks and the inherited e=1 classification certificate. The source-level proof, not the PASS output alone, supplies orbit exhaustion and the global filtration argument.

## Consequences
Provides a shorter proof of the (4,4) case than the full quartic-carrier exclusion.

## Limitations
It is not a coordinate-free symmetric-algebra obstruction or an unrestricted STCI theorem.

## Permanent evidence navigation

The `research/notes/` metadata preserves original provenance identifiers rather than live branch paths. The [consolidated subject chapter](../synthesis/05-exclusions.md) provides a current entry point to the mathematical argument and its retained detailed supplements. This route does not alter the record's hypotheses, proof status, or historical audit identity.
