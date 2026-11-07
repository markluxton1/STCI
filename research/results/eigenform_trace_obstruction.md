---
id: STCI-R-0042
type: result
title: Trace obstruction for a supported pair with one eigenform
scope: "#scope"
statement: "#statement"
proofs:
  - name: finite-free trace and graded-domain reduction
    at: "research/arguments/torus_sextic_residuals.md#trace-obstruction-for-supported-pairs"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Trace obstruction for a supported pair with one eigenform

## Scope

Let \(k\) be algebraically closed, \(S=k[x_0,x_1,x_2,x_3]\), and
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k\). Let \(F,G\) be
homogeneous of positive ordinary degrees \(a,b\) with
\(V(F,G)_{\mathrm{red}}=C\). An eigenform is homogeneous for the integer
weights \((0,1,3,4)\); weights are not reduced modulo the characteristic.
The statements concern actual global equations.

## Statement

If at least one of \(F,G\) is an eigenform, then \(ab=0\) in \(k\).
Consequently such a pair is impossible in characteristic zero; in
characteristic \(p>0\),

\[
p\mid ab,\qquad \max(a,b)\ge p.
\]

Writing \(m_C\) for generic intersection multiplicity, \(ab=4m_C\);
for odd \(p\) it follows that \(p\mid m_C\) and \(ab\ge4p\).

The same obstruction \(ab=0\) holds without a weight assumption if,
after exchanging and rescaling equations, the pair satisfies the actual
polynomial congruences

\[
F\equiv x_1^a\pmod{x_0^2},\qquad
G\equiv x_2^b\pmod{x_3^2}.
\]

If an equation merely has a nonconstant eigenform factor, a supported
pair is still impossible in characteristic zero and still satisfies
\(\max(a,b)\ge p\) in characteristic \(p>0\); divisibility \(p\mid ab\)
for the original degrees is not asserted under this weaker hypothesis.

## Proof

The [complete trace proof](../arguments/torus_sextic_residuals.md#trace-obstruction-for-supported-pairs)
constructs a finite free \(k[x_0,x_3]\)-algebra with monomial basis,
compares the nilpotent trace of \(x_1x_2-x_0x_3\) before and after
base change by \((x_0^2,x_3^2)\), and proves the arbitrary-mate reduction
in each irreducible eigenform factor's graded domain.

## Evidence

Reconstructed from the trace and arbitrary-mate sections of
[weight restrictions](../supplements/EQUIVARIANT_DEGREE_BOUNDS.md).
No finite-field rank or external nonexistence theorem is a proof premise.

## Limitations

There is no reduction of arbitrary pairs to these eigenform or congruence
hypotheses. In characteristic two, the trace calculation gives no parity
claim for \(m_C\). The sharp large-prime minimum using separate positive
characteristic constructions is outside this reconstructed proof closure.
The unrestricted characteristic-zero STCI question remains open.

## Review

Independent reconstruction by the nonauthor reviewer pilot_review_sextic
accepted this route on November 4, 2026. The reviewer reconstructed the finite-free basis, nilpotent trace,
congruence base change, and graded-domain reduction from one eigenform
with an arbitrary mate. The factor qualification and characteristic-two
limitation were retained. Acceptance concerns the stated source
hypotheses; no arbitrary-pair reduction is claimed.

Independent reconstruction review accepts this route within its stated scope.
