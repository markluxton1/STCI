# Exact closure of the first endpoint family's degree-thirteen exception

Date: 2026-10-07. Scope: characteristic zero, the fixed curve
`C0=[s^4:s^3t:st^3:t^4]`, primitive degree-two normal-dual direction,
pure cubic top `h=t`, and the first rational endpoint family classified
in the independent endpoint audit. This note does not address another
endpoint family, a nonendpoint top zero, or the universal STCI problem.

## Result and proof certificate

**PROVED under the audited actual multiplication tensor and coordinate
bases:** every member of the complete affine line of quartic lower
corrections at every geometric root of

```text
Q13(k)=729k^13+1620k^12+2889k^11-11268k^10-26574k^9-39642k^8
       +94014k^7+272968k^6+454897k^5+62256k^4-571463k^3
       -1210068k^2-966908k-379834
```

fails the target-`u` multiplication incidence. This closes all thirteen
parameter points of this exceptional locus for every lower parameter
`lambda`.

The defining polynomial is irreducible over `QQ`. Its monic reduction
modulo 53, written in ascending coefficient order, is

```text
[15,43,6,38,30,45,19,21,8,22,31,2,14,1].
```

The standalone verifier proves irreducibility by exact modular polynomial
arithmetic: `k^(53^13)=k (mod f)` and `gcd(f,k^53-k)=1`. Since the degree
13 is prime, these are the full Rabin irreducibility conditions. Thus
`K=QQ[k]/Q13` is a field, and its thirteen characteristic-zero embeddings
account for every geometric root.

The saved rational seed has lower corrections
`alpha=a*(k)+lambda*k0`. Every seed denominator was inverted exactly
in `K`, before the actual 74-by-18 multiplier matrix was exported.
Macaulay2 computed the polynomial left-kernel module over `K[lambda]`.
Its target-evaluation ideal is `(1)`. The resulting exact left dual has
26 nonzero entries, degree at most two in `lambda`, and entry 72 equal
to one.

The standalone verifier reads the actual 74-by-542 tensor and checks
both target columns against `e72,e73`. It independently verifies all
eighteen identities `n^T L(alpha)=0`, coefficient by coefficient in
`lambda`, and verifies `n^T u=1`. These identities, rather than the
module command or a generic rank calculation, prove exclusion for
every `lambda` and every embedding of `K`.

The verifier also checks the 32-by-30 actual pure-top map has rank 29,
the saved kernel direction is nonzero, and the coefficient of `lambda`
in `alpha` is exactly this kernel direction. Its constant seed and
direction coefficients are independently derived from the saved rational
expressions using an arithmetic-only parser and rational multiplication
matrices in `K`; this replay uses neither SymPy nor Macaulay2. In all
32 top coordinates it checks
`top(alpha)=t*p^i*r^(3-i)`. Consequently the affine line is the entire
lower-correction fibre, rather than a sampled collection of lifts. A
fixed four-by-four Sylvester determinant checks the homogeneous quadratic
pair is primitive, including leading-coefficient specializations.

All source inputs, including the tensor, bases, top map, rational seed,
complete dual, evaluation output, module input and generator, are bound
to the coefficient certificate by SHA256. The certificate SHA256 is

```text
c484ca17078ecfd2e30eb8d3f76e57c313f25f3684c34db286deb047429db65c
```

## Reproduction and evidence

Generate the reduced actual module:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/computations/generate_session_localcoh_q13_module_2026_10_07.py
/opt/homebrew/bin/M2 --script \
  research/computations/session-localcoh-origin-family-1-exception-q13.m2
```

Regenerate the coefficient certificate from the saved exact dual, then
verify it independently with an ordinary Python:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/computations/verify_session_localcoh_q13_dual_2026_10_07.py --regenerate
python3 research/computations/verify_session_localcoh_q13_dual_2026_10_07.py
```

The generator ran in tool session `38119`, the single M2 computation
in session `88486`, and certificate regeneration in session `86666`.
All completed with exit code zero. The initial standard-library replay
in session `27168` also passed. A stronger direct-rational-source replay
was performed subsequently; its terminal status is recorded below.
There was no overlapping copy of the Q13 module computation.

Evidence files:

- [`generate_session_localcoh_q13_module_2026_10_07.py`](../computations/generate_session_localcoh_q13_module_2026_10_07.py)
- [`session-localcoh-origin-family-1-exception-q13.m2`](../computations/session-localcoh-origin-family-1-exception-q13.m2)
- [`session-localcoh-origin-family-1-exception-q13-dual.txt`](../computations/session-localcoh-origin-family-1-exception-q13-dual.txt)
- [`session-localcoh-origin-family-1-exception-q13-evaluations.txt`](../computations/session-localcoh-origin-family-1-exception-q13-evaluations.txt)
- [`session_localcoh_q13_dual_audit_2026_10_07.json`](../computations/session_localcoh_q13_dual_audit_2026_10_07.json)
- [`verify_session_localcoh_q13_dual_2026_10_07.py`](../computations/verify_session_localcoh_q13_dual_2026_10_07.py)
- [`session-localcoh-origin-family-1-exception-q13-verification.out`](../computations/session-localcoh-origin-family-1-exception-q13-verification.out)

The separately recorded Q1 and Q3 closures, together with this Q13
closure and the previous quadratic closure, remove the first family's
available generic dual's remaining primitive parameter exceptions after
those certificates are accepted. The other three endpoint families and
nonendpoint top-zero strata retain their prior unresolved scope.
