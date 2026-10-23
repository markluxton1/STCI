# Diagnostic: failed reconstructed-versus-exported FIRST residual comparison

Date: 2026-10-21. Status: **diagnostic only; no repaired certificate and no theorem promotion**.

The committed `conditional_2_12_certificate_audit_cont2_2026_10_21.json` reports an M2 assertion failure at line 23 of the generated `.m2` script. Line 22 asserts that rows 0–3 and 12–15 of the reconstructed universal FIRST operator vanish; line 23 compares rows 4–11 with the saved eight-polynomial export from `conditional_2_12_singular_continuation_2026_10_21_line_component_w1.m2`.

A separate direct arithmetic evaluation of the *recorded expressions* gives:

- Set `w=1, a=0, x=0, h4=h5=h6=h7=0`: the eight differences (reconstruction minus saved export) all vanish.
- Set `w=1, a=1, x=2, h4=h5=h6=h7=0`: the eight differences are `(12, 9/2, 0, -43/8, 175/4, 43/4, -27/4, 3/4)`.

Thus the assertion is not simply a failure to normalize syntactically equivalent polynomial expressions: the recorded expressions have different values at a rational point. The discrepancy affects seven of the eight residual rows at this test point. This is an arithmetic spot check, **not a rerun of Macaulay2**.

Next checks: independently derive the original factor-to-coefficient map, check the ordering of `ff` against the universal FIRST variables, and compare the saved export's coordinate conventions and reduction assumptions. For each of the eight rows, print `actual#(i+4)-exported#i` in Macaulay2 and isolate the earliest divergence. Do not silently replace the saved export with the reconstructed list; the source of the disagreement remains unidentified. In particular, no certificate depending on this equality is a pass until rerun with explicit exact identities.
