# Exact closure of the first endpoint family's Q3 exception

Date: 2026-10-07. Scope: characteristic zero, the fixed curve
`C0=[s^4:s^3t:st^3:t^4]`, primitive degree-two normal-dual direction,
pure cubic top `h=t`, and the first rational endpoint family from the
independently audited endpoint classification. No assertion here concerns
a nonendpoint top zero, another endpoint family, or the global STCI question.

## Result

**PROVED under the audited actual tensor and coordinate bases:** every
member of the complete affine line of quartic ancestors at every geometric
root of

```text
Q3(k)=13k^4+26k^3+34k^2+6k-7
```

fails the target-`u` multiplication incidence. Thus this quartic factor
can be removed from the first family's denominator-exception list. Together
with the previously closed quadratic factor and Q1, the only remaining
exceptions to that family's available generic dual at this checkpoint are
the thirteen roots of the recorded degree-thirteen factor, each with its
complete affine lower-correction fibre. These thirteen points remain
exceptions to the available certificate, rather than evidence for an ancestor.

## Exact calculation and independent verification

The defining polynomial is irreducible over `QQ`: its reduction modulo 17,
made monic, is

```text
f(k)=k^4+2k^3+7k+6 in F_17[k].
```

The standard-library verifier checks `k^(17^4)=k (mod f)` and
`gcd(f,k^(17^2)-k)=1` using modular polynomial arithmetic. This is the
degree-four irreducibility test, and also ensures that
`K=QQ[k]/Q3` is a field. All seed denominators were inverted exactly in
this field before exporting the module.

The retained rational seed and its kernel direction give
`alpha=a*(k)+lambda*k0`. From the actual 74-by-542 tensor, the generator
constructs all entries of the 74-by-18 multiplier matrix `L(alpha)`.
Macaulay2 computes the full polynomial left-kernel module over `K[lambda]`.
Its target evaluation ideal is `(1)`. A resulting exact left dual `n`
has 26 nonzero entries, degree at most one in `lambda`, and entry 72 equal
to one.

The subsequent verifier uses only exact rational arithmetic and

```text
k^4=-2k^3-(34/13)k^2-(6/13)k+7/13.
```

It checks all eighteen identities `n^T L(alpha)=0` coefficient by coefficient
in `lambda`, and `n^T u=1`, with `u=e72` checked against the tensor's actual
target column. Therefore `u` is outside the image for every `lambda`.
Because Q3 is irreducible and characteristic zero is separable, this exact
field identity applies through all four embeddings into an algebraic closure.

The verifier also checks the 32-by-30 actual pure-top map has rank 29,
the nonzero coefficient of `lambda` is exactly its saved kernel vector,
and the top of every `alpha` is `t*p^i*r^(3-i)` in all 32 coordinates.
This confirms that the entire affine fibre of lower corrections has been
tested. A fixed four-by-four Sylvester determinant verifies the homogeneous
quadratic direction is primitive, including possible leading-coefficient
specializations. Every input is bound to the coefficient certificate by SHA256.

## Reproduction and terminal process status

Generate the reduced module input:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/computations/generate_session_localcoh_q3_module_2026_10_07.py
```

Compute the full polynomial dual:

```sh
/opt/homebrew/bin/M2 --script \
  research/computations/session-localcoh-origin-family-1-exception-q3.m2
```

Regenerate and independently verify the coefficient certificate:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/computations/verify_session_localcoh_q3_dual_2026_10_07.py --regenerate
python3 research/computations/verify_session_localcoh_q3_dual_2026_10_07.py
```

The generator ran in tool session `99512`, the M2 computation in session
`34782`, and certificate regeneration in session `88461`; all three
completed with exit code zero. M2 printed matrix readiness, completed its
polynomial kernel, saved the unit evaluation ideal, and saved the dual.
No computation from this branch remains running.

The complete evidence is retained in
[`session-localcoh-origin-family-1-exception-q3.m2`](../computations/session-localcoh-origin-family-1-exception-q3.m2),
[`session-localcoh-origin-family-1-exception-q3-dual.txt`](../computations/session-localcoh-origin-family-1-exception-q3-dual.txt),
[`session-localcoh-origin-family-1-exception-q3-evaluations.txt`](../computations/session-localcoh-origin-family-1-exception-q3-evaluations.txt),
and
[`session_localcoh_q3_dual_audit_2026_10_07.json`](../computations/session_localcoh_q3_dual_audit_2026_10_07.json).
The default verifier is independent of Macaulay2 and SymPy, so the
certificate remains directly checkable without reproducing the module command.
