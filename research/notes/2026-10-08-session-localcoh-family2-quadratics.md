# Exact closure of both quadratic exceptions in endpoint family2

Date: 2026-10-08. Scope: characteristic zero, the fixed rational quartic
`C0=[s^4:s^3t:st^3:t^4]`, the second primitive degree-two endpoint family,
and its complete affine line of lower quartic corrections. The pure top
is the actual saved `t*p^i*r^(3-i)` normalization. This note concerns the
two quadratic exceptions to the generic family2 dual, with no assertion
about the other endpoint families or a nonendpoint top zero.

## Result

**PROVED under the audited actual tensor and coordinate bases:** both
roots of `k^2+1` and both roots of `k^2-2k-1` exclude target `u` for every
`lambda`. These four geometric direction parameters are removed from the
generic family2 certificate's retained locus.

The remaining exceptions to that generic certificate are precisely the
22 geometric roots of the following three factors, each still retaining
its full affine `lambda` fibre:

```text
3k^3+4k^2+9k-4
13k^4+10k^3+2k^2-42k-7
243k^15+810k^14+2646k^13+990k^12-9465k^11-54222k^10
 -114414k^9-166406k^8-34359k^7+301686k^6+897946k^5
 +1296458k^4+1345117k^3+811630k^2+285598k-610
```

Their square-free, pairwise-coprime and primitive-chart status was checked
by the complete generic verifier. This branch does not assert they are
actual incidence survivors. No high-degree factor calculation was begun.

## Exact fields and independent coefficient reconstruction

The two computations use

```text
Kplus=QQ[k]/(k^2+1),       k^2=-1,       discriminant=-4;
Kminus=QQ[k]/(k^2-2k-1),  k^2=2k+1,     discriminant=8.
```

Both quadratics are irreducible over `QQ`, since their discriminants
are nonzero rational nonsquares. A single standard-library verifier
implements exact arithmetic in both fields with rational coefficient
pairs. For `k^2=c+d*k`, it inverts `a+b*k` by the explicit formula

```text
(a+b*k)^(-1) = (a+d*b-b*k)/(a^2+d*a*b-c*b^2).
```

Every rational source denominator is checked by this norm formula to
be a field unit. A restricted AST parser, with no `eval`, reconstructs
all source expressions directly in the quadratic field and its
polynomial ring in `lambda`. On every default verification run, it
rederives all thirty saved seed coefficients, all thirty lower slopes,
and the four direction coefficients from the family2 rational expressions.
It compares them exactly with the certificate; it does not merely trust
a previously reduced coefficient table or a point sample.

The explicit direction formulas checked are

```text
p=1+(k^2+3)/(2-2k^2)*t
     -(k^2+2k+3)/(2(k+1)^2)*t^2,
r=1+(k-3)(k^2+2k+3)/((k-1)^2(k+1))*t
     -2(k^2+1)(k^2-2k-1)(k^2+2k+3)/((k-1)^3(k+1)^3)*t^2.
```

In both fields the verifier checks all 32 actual pure-top identities,
the rank-29 top map, and that the coefficient of `lambda` in the lift
is the exact nonzero kernel vector. Thus the full affine lift fibre is
covered. Its fixed four-by-four Sylvester determinant confirms the
homogeneous direction is primitive, even though `r` loses its quadratic
coefficient at these parameter values.

## Full polynomial duals

Separate reduced 74-by-18 modules were generated from the actual tensor,
using the directly reconstructed field coefficients. In each field,
Macaulay2 computed the full polynomial left-kernel module over `K[lambda]`
and returned target evaluation ideal `(1)`. The resulting duals each have
27 nonzero entries and degree at most two in `lambda`.

The independent verifier checks every coefficient of all eighteen
identities `n^T L(a*+lambda*k0)=0`, and checks `n^T u=1`. It checks the
actual target columns in the tensor are `e72,e73`, so the target evaluation
is tied to the same actual multiplier incidence. Since the fields are
quadratic and separable in characteristic zero, these identities hold
through both embeddings of each field into an algebraic closure. No
specialization or generic-rank extrapolation enters the conclusion.

## Reproduction and terminal execution evidence

Generate both exact field modules without SymPy:

```sh
python3 research/computations/verify_session_localcoh_family2_quadratics_2026_10_08.py --generate
```

Run each separate M2 module:

```sh
/opt/homebrew/bin/M2 --script research/computations/session-localcoh-origin-family-2-exception-qplus.m2
/opt/homebrew/bin/M2 --script research/computations/session-localcoh-origin-family-2-exception-qminus.m2
```

Regenerate coefficient certificates and verify everything using only an
ordinary Python:

```sh
python3 research/computations/verify_session_localcoh_family2_quadratics_2026_10_08.py --regenerate
python3 research/computations/verify_session_localcoh_family2_quadratics_2026_10_08.py
```

The qplus M2 process was observed terminal with exit code zero in agent-local
tool session `60266`. Its complete output included matrix readiness,
full polynomial kernel completion, full evaluation-ideal export, and
complete polynomial dual export. A parent-local query could not resolve
that handle; the agent's terminal observation and saved outputs are
the evidence for completion. No replay was inferred necessary from the
parent's unavailable handle. The qminus run returned exit code zero
directly. Both coefficient-regeneration checks and the fresh combined
default verification passed. No process from these two branches remains
running.

Evidence is retained in the
[`standard-library generator and verifier`](../computations/verify_session_localcoh_family2_quadratics_2026_10_08.py),
the
[`qplus exact certificate`](../computations/session_localcoh_family2_qplus_audit_2026_10_08.json),
the
[`qminus exact certificate`](../computations/session_localcoh_family2_qminus_audit_2026_10_08.json),
the separate `.m2`, `-dual.txt` and `-evaluations.txt` files for each field,
and the frozen source/output hashes in
[`session_localcoh_family2_quadratics_execution_2026_10_08.json`](../computations/session_localcoh_family2_quadratics_execution_2026_10_08.json).
Canonical frontier documents were left to the root agent.
