# Second endpoint family: exact generic exclusion and retained exceptions

Date: 2026-10-08. Scope: characteristic zero, the fixed rational quartic
`C0=[s^4:s^3t:st^3:t^4]`, primitive degree-two normal-dual directions,
pure cubic top `h=t`, and the second rational endpoint family. This note
does not address either `p(0)=0` boundary family or a nonendpoint top zero.

## Result and exact unresolved locus

**PROVED under the audited actual multiplication tensor and coordinate
bases:** the second rational endpoint family excludes target `u`, for
every lower-correction parameter `lambda`, away from the displayed
denominator roots. After removing chart poles and nonprimitive directions,
the following five square-free, pairwise-coprime factors retain exactly
26 primitive geometric parameter points:

```text
k^2+1
k^2-2k-1
3k^3+4k^2+9k-4
13k^4+10k^3+2k^2-42k-7
243k^15+810k^14+2646k^13+990k^12-9465k^11-54222k^10
 -114414k^9-166406k^8-34359k^7+301686k^6+897946k^5
 +1296458k^4+1345117k^3+811630k^2+285598k-610
```

Each retained parameter point still has its complete affine `lambda`
fibre. These are exceptions to this certificate, with no implication
that they support an ancestor or even an actual rank jump. No exceptional
field fibre was computed in this branch.

## Actual direction and complete affine family

The independently classified second family has

```text
p=1+(k^2+3)/(2-2k^2)*t
     -(k^2+2k+3)/(2(k+1)^2)*t^2,
r=1+(k-3)(k^2+2k+3)/((k-1)^2(k+1))*t
     -2(k^2+1)(k^2-2k-1)(k^2+2k+3)/((k-1)^3(k+1)^3)*t^2.
```

Its actual quartic lift is the complete affine line
`a*(k)+lambda*k0`, where the 32-by-30 pure-top map has rank 29 and `k0`
is its nonzero kernel vector. The clearing factors are

```text
B=2(k-1)^3(k+1)^3                  [direction denominator]
A=120(k-1)^9(k+1)^9               [ancestor denominator].
```

The certificate stores `alpha=A*(a*+lambda*k0)`, along with
`P=B*p` and `R=B*r`. Its standard-library verifier checks all four
rational direction formulas by polynomial cross-multiplication, the
rank-29 top map, and the coefficient of `lambda` in each of the thirty
ancestor coordinates. It verifies all 32 cleared pure-top identities

```text
B^3 * M(alpha) = A * coefficients(t*P^i*R^(3-i)), i=0,1,2,3.
```

Since `A` and `B` are nonzero on the retained chart, these checks prove
coverage of the entire affine lift fibre at every retained parameter.

## Exact polynomial dual

The saved full 74-by-18 module calculation over `QQ(k)[lambda]` returned
target evaluation ideal `(1)` and a complete polynomial left dual. The
cleared dual has 26 nonzero entries and degree at most two in `lambda`.
Its exact target value is

```text
D=89514547200*(k-1)^15*(k+1)^12*(k^2+1)^5*(k^2-2k-1)^5
 *(k^2+2k+3)^4*(3k^3+4k^2+9k-4)
 *(3k^4-2k^3-6k^2-18k-9)*(13k^4+10k^3+2k^2-42k-7)
 *(243k^15+810k^14+2646k^13+990k^12-9465k^11-54222k^10
   -114414k^9-166406k^8-34359k^7+301686k^6+897946k^5
   +1296458k^4+1345117k^3+811630k^2+285598k-610).
```

The verifier checks all eighteen actual tensor-column identities
`n^T L(alpha)=0` over `QQ[k,lambda]` and `n^T u=D`. It also checks
the actual target columns in the stored tensor are `e72,e73`.
Therefore target `u` cannot lie in the multiplier image wherever `D!=0`,
for every value of `lambda`.

A fixed four-by-four homogeneous Sylvester determinant gives

```text
Res_hom(p,r)=-8*(k^2+2k+3)*(3k^4-2k^3-6k^2-18k-9)
             /((k-1)^5*(k+1)^6).
```

Thus `k=+/-1` are chart poles, while the roots of `k^2+2k+3` and
`3k^4-2k^3-6k^2-18k-9` are nonprimitive. The independent verifier
reconstructs the full factorization of `D`; verifies the five remaining
factors are square-free and pairwise coprime; and verifies they are
coprime to both the chart factor and the homogeneous resultant numerator.
This establishes the precise count and scope of the retained 26 points.

## Reproduction, evidence, and terminal status

Recompute the generic module:

```sh
/opt/homebrew/bin/M2 --script \
  research/computations/session-localcoh-origin-family-2.m2
```

Regenerate its cleared certificate using SymPy:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/computations/verify_session_localcoh_family2_generic_2026_10_08.py --regenerate
```

Verify every saved identity and scope assertion with an ordinary Python:

```sh
python3 research/computations/verify_session_localcoh_family2_generic_2026_10_08.py
```

The M2 process was explicitly launched in tool session `55063` on
2026-10-08 and completed with exit code zero. Certificate regeneration
in session `18670` and strengthened default verification in session
`79082` also completed with exit code zero. No process from this branch
remains running. An auxiliary dense rational point-rank probe in session
`26885` was stopped with `KeyboardInterrupt` and exit code 130 after
the generic dual had completed; it produced no rank result, and none
is asserted here.

Full evidence is retained in
[`session-localcoh-origin-family-2-generic-dual.txt`](../computations/session-localcoh-origin-family-2-generic-dual.txt),
[`session-localcoh-origin-family-2-evaluations.txt`](../computations/session-localcoh-origin-family-2-evaluations.txt),
[`session_localcoh_family2_generic_dual_audit_2026_10_08.json`](../computations/session_localcoh_family2_generic_dual_audit_2026_10_08.json),
and the separate
[`verify_session_localcoh_family2_generic_2026_10_08.py`](../computations/verify_session_localcoh_family2_generic_2026_10_08.py).
The original generic verifier is imported as an unchanged standard-library
arithmetic helper; its exact file hash, all coordinate sources, the seed,
the full module input, raw dual, and evaluation output are bound to the
new certificate. The first family's sources and Q1/Q3 artifacts were
left unchanged.
