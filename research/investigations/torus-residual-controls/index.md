---
id: STCI-I-0003
type: investigation
title: Exact finite controls for embedded quotients and sextic residual limits
status: complete
scope: "#scope"
question: "#question"
findings: "#findings"
relations:
  - kind: motivates
    from: [STCI-F-0001, STCI-F-0002]
    to: [STCI-I-0003]
    at: "#purpose"
  - kind: uses
    from: [STCI-R-0044, STCI-R-0046, STCI-R-0052, STCI-R-0054]
    to: [STCI-I-0003]
    at: "#method"
  - kind: informs
    from: [STCI-I-0003]
    to: [STCI-F-0001, STCI-F-0002]
    at: "#findings"
---
# Exact finite controls for embedded quotients and sextic residual limits

## Scope

This completed activity checks the displayed finite identities and source
profiles used in the quotient and sextic accounts. It covers the exact
rational calculations and explicitly listed prime fields in [verify.py](verify.py).
The additional [Macaulay2 control](verify_transverse_limit.m2) checks the
specified length-two sextic pair and the marked curve's full transverse
limits over \(\mathbf Q\), including parameter and irrelevant saturation.
It is not an enumeration of arbitrary ideals, a saturation algorithm, a
primary-decomposition proof, or a supported-family coverage calculation.
No \(N\)-bounded supported Hilbert incidence is computed here.

## Question

Do the retained finite algebra, jet, polynomial-minor, and Hilbert checks pass
on their specified inputs and reject deliberate changes to those data?
The broader realization and comparison questions belong to
[I-0001](../supported-generator-incidence/index.md) and
[I-0002](../quotient-hilbert-comparison/index.md) and remain open.

## Purpose

[F-0001](../../frameworks/torus_supported_boundaries.md) needs controls that
retain the full ideal and distinguish moving divisors from individual points.
[F-0002](../../frameworks/embedded_torus_quotients.md) needs actual embedded
source and endpoint data. Small exact checks can detect errors in these
examples without replacing their geometric proofs.

## Method

The supporting program has four groups:

| Group | Exact assertion checked | Deliberately false control |
| --- | --- | --- |
| `quotient_checks` | Listed endpoint rank sums, determinants, and truncated algebra identities | Change an endpoint-series coefficient |
| `jet_checks` | Enumerated degree-six source, specified double-jet profile and finite source dimensions | Drop one jet row |
| `residual_checks` | Actual ambient substitution, generator change, minors, and cancellation identities | Replace the deformation polynomial's factor |
| `hilbert_checks` | CI polynomial, resolution numerator, and displayed degree sums | Change the asserted degree sum |

Each group has its genuine run and a rejected altered datum in
[test_verify.py](test_verify.py). Alterations occur in isolated temporary
namespaces; the retained mathematical inputs are preserved. These are explicit
finite controls for the numerical examples in
[R-0052](../../results/orbit_image_endpoint_polynomial.md) and
[R-0054](../../results/embedded_quotient_endpoint_counterexamples.md), and the
polynomial data in [R-0046](../../results/sextic_three_generator_full_limit.md).
The full proofs in [A-0002](../../arguments/torus_sextic_residuals.md) and
[A-0003](../../arguments/torus_embedded_quotients.md) establish the geometric
claims. The local-length reasoning in
[R-0044](../../results/local_residual_multiplicity.md) explains the invariant
meaning of multiplicities rather than inferring them from degree sums.
The additional
[transverse length-two calculation](../../arguments/torus_sextic_residuals.md#a-transverse-limit-with-generic-length-two)
has a regular-sequence proof and a full-ideal replay in Macaulay2.

Run the specified normal Python commands, which keep assertions enabled:

```sh
python3 -B research/investigations/torus-residual-controls/verify.py
python3 -B -m unittest discover -s research/investigations/torus-residual-controls -p 'test_*.py' -v
M2 --script research/investigations/torus-residual-controls/verify_transverse_limit.m2
```

## Findings

All four retained check groups passed on their actual inputs; each of the four
deliberately altered controls was rejected. This records an actual rerun with
false controls, not merely source inspection. No script execution is treated
as proving flatness, saturation, primary structure, or exhaustive family
coverage. Those claims have their independent written arguments and reviews.

The source-profile checks also preserve the existing double-sextic source
dimension 23. They do not produce a new length-nine obstruction. Numerical
agreement between samples in listed characteristics supplies no all-primes
coverage statement without a separate argument.

## Outputs and next decisions

The useful output is the preserved exact program with its four negative
controls, owned by this Investigation. No execution-log archive or generated
validation report is retained. Change this program when a new mathematical
test requires different data, and update its scope and false controls together.
Actual supported generator incidence and quotient specialization remain
separate investigations.
