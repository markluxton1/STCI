# Intrinsic (4,4) proof: validation record

Date: 2026-10-23. This record concerns the new intrinsic K3 proof and its
supporting constructions. It does not rerun the inherited quartic-carrier
proof, the primitive-triple classification, or the earlier contact-pencil
certificate. No canonical result is promoted.

## Mathematical evidence

- [Principal proof](../../notes/2026-10-23-intrinsic-44-k3-proof-proposal.md)
  and [independent proof audit](../../notes/2026-10-23-intrinsic-44-k3-independent-audit.md).
- [Independent local-algebra construction](../../notes/2026-10-23-intrinsic-quadruple-local-algebra.md).
- [Contact construction](../../notes/2026-10-23-intrinsic-cubic-contact-construction.md),
  [coefficient valuations](../../notes/2026-10-23-intrinsic-coefficient-valuations.md),
  and [secondary audit](../../notes/2026-10-23-intrinsic-contact-valuations-independent-audit.md).
- [Integrated report, dependencies and handoff](../../notes/2026-10-23-intrinsic-44-research-report.md).

The proof audit reconstructs the rank-four Frobenius pairing, exact
embedded local normal forms, fixed-divisor equality, arbitrary local
coefficient functions, general-member singularities, and the K3 rank
contradiction. Its pass decision is mathematical review, distinct from
the calculation outputs below. The new argument does not invoke either
R0001 or R0022 as a premise.

## Executed checks and boundaries

Commands run from the repository root:

```sh
python3 research/computations/verify_intrinsic_quadruple_local_algebra_2026_10_23.py
python3 research/computations/verify_intrinsic_valuations_2026_10_23.py
/tmp/stci-z4-env/bin/python research/computations/verify_intrinsic_cubic_contact_2026_10_23.py
python3 research/computations/validate_records.py
git diff --check
```

The two first scripts use only Python's standard library. The cubic-contact
script requires SymPy; the temporary runtime path records this checkout's
execution environment, and any compatible Python with SymPy can be used.

| Check | What it verifies | What supplies the rest |
| --- | --- | --- |
| Quadruple local algebra | Generic Frobenius determinant, associative rank-four multiplication, correction removal, completed-square and Jacobian identities, ranks 24 and 21/22/23 | Written local normal-form proof and variable-coefficient Morse argument |
| Coefficient valuations | Exact cancellation, selected coefficient/normal weights, residue polynomials, coordinate example, characteristic-two singular line, colength counterexample | General valuation and domain proofs; inherited R0021 supplies global support |
| Cubic contact | Hilbert–Burch presentation, torsion relation, general cubic Taylor reduction, blowup tangents and determinant transitions | Written canonical gluing argument; no global nonvanishing is claimed |
| Canonical record validator | Metadata for the existing canonical records | Does not assess mathematical truth or promote the new proof |
| Diff and local-link checks | Whitespace and paths in the new package | Do not establish mathematics |

Exact command outputs, runtime versions, exit codes and source SHA-256
values are in [checks.json](checks.json). The JSON records the checked
Git parent and branch as execution context, rather than claiming its own
containing commit. All three new scripts exited zero with their stated
PASS outputs; the record validator checked 23 canonical records with zero
errors. The scope of those records and their statuses are unchanged.

## Delivery provenance

The task started from main at
`1f857f17f5fa9f58640bdf802b6bb02c858ecfbb` and created
`codex/intrinsic-44-k3-contact-2026-10-23`. During the usage-window pause,
the current work was saved on `research/2026-10-23_morning` in commit
`9db29c8` and pushed to that branch. The final validation and status
updates were completed in that existing research checkout. The saved
work was preserved; no accepted proof or canonical theorem status was
edited to make the new proposal appear promoted.
