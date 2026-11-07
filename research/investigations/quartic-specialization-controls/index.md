---
id: STCI-I-0004
type: investigation
title: Finite quartic specialization controls
status: complete
scope: "#scope"
question: "#question"
findings: "#findings"
relations:
  - kind: motivates
    from: [STCI-F-0002]
    to: [STCI-I-0004]
    at: "#purpose"
---
# Finite quartic specialization controls

## Scope

Fix \(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\). The optional replays
check specified chart identities, homogeneous syzygies, and source
matrices over the integers, characteristic-zero fields and the indicated
prime fields.

## Question

Do the preserved verifiers reproduce their finite calculations and
reject deliberately corrupted input or expected output?

## Purpose

The [embedded-quotient framework](../../frameworks/embedded_torus_quotients.md)
uses the prescribed pair as an arithmetic control. The replays check
the coordinate formulas used to distinguish its projective image, its
normal graded pieces and the actual quartic source. The geometric proofs
are in [A-0004](../../arguments/quartic_specialization_and_symbols.md).

## Method

| Replay | Exact scope | Deliberately false datum |
| --- | --- | --- |
| [Two-chart transition](verify_normal_bundle.py) | Integral transition identities by symbolic expansion, quadratic syzygy determinant and ranks over \(\mathbf Q,\mathbf F_3,\mathbf F_5\), and the characteristic-three primitive triple | Change the \(\beta\)-coefficient of \(b\) from \(3u^{-8}\) to \(4u^{-8}\) |
| [Homogeneous syzygies](verify_session_quartic_normal_bundle_2026_10_10.m2) | Derivative syzygies, projective ranks and quadratic coefficient determinant over \(\mathbf Q\) | Change the determinant's absolute value from \(2^{15}\) to \(2^{14}\) |
| [Prescribed pair](verify_44_mu4_family_2026_10_23.m2) | Integral chart elimination and the group-scheme equation, characteristic-two ideal, generic initial terms, split decomposition over \(\mathbf Q(i)\), endpoint contacts and an alternate conormal cocycle over \(\mathbf Q\) | Replace the characteristic-two target ideal \((X,Y^4)\) by \((X,Y^3)\) |
| [Quartic symbols](verify_44_quartic_symbol_comparison_2026_10_23.py) | Complete quartic monomial source, first-symbol matrices, \(q^2\) kernel and second-symbol dimensions over \(\mathbf Q\) and \(\mathbf F_2\) | Change the characteristic-zero first-symbol rank from seventeen to eighteen |

[The tests](test_verifier_controls.py) run each original verifier, then
change one datum in a temporary copy and check the rejection diagnostic.
CI runs the Python and Macaulay2 groups in their respective quartic jobs.
From the repository root, with SymPy 1.14.0 and Macaulay2 on the path, run

```sh
python3.12 -B -m unittest discover -s research/investigations/quartic-specialization-controls -v
```

## Findings

All four replays passed with Python 3.12, SymPy 1.14.0 and Macaulay2
1.26.06. Each false datum was rejected. The proofs of flatness, the full
initial ideals and the characteristic scope of the symbol calculation
use the geometric arguments in
[R-0021](../../results/quartic_mu4_degeneration.md),
[R-0057](../../results/quartic_normal_initial_base_change.md) and
[R-0058](../../results/quartic_actual_symbols.md).
