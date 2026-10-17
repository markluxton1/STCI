# Supporting literal arithmetic audit, 2026-10-14

Status: **EXACT IDENTITY AUDIT PASSED**, over `QQ`. This supports the new
quintic support-incidence certificates. It is not a standalone geometric
acceptance, and it makes no universal STCI claim.

No accepted computation was imported or rerun. The captured polynomials and
original-generator witnesses were read as mathematical data and multiplied
by independent standard-library arithmetic. The scripts record input hashes
for provenance; hash agreement is not counted as mathematical verification.

## Zero charts

`h3-literal-arithmetic.py` independently checks the JSON capture
`research/validation/2026-10-13-h3-zero-chart-conductor-new/new-exact-support-incidence.json`.
The following identities pass:

- `S*Q5 = (9/2)*zero_P_F`, with `Q5` monic of degree five in `p`.
- `S^5 = Q5*captured_quotient + captured_remainder`, and the remainder has
  `p` degree below five.
- The five original generator lists are exactly the five `p` coefficients
  of that remainder.
- Multiplying those five original generators by the five captured Bezout
  coefficients gives exactly `1`.
- The binary coordinate swap takes the captured zero-P octic to zero-J:
  `FJ(p,j)=(p-1)^8*FP(p/(p-1),-j)`.
- The corresponding cubic swap gives the literal zero-J conormal:
  `(-2/3)*(p-1)^3*S(p/(p-1),-j)`.

## Lambda equals one

The same source independently parses the four compact numerator and
denominator captures and the original four-entry Bezout matrix. The original
numerator/witness product is exactly `1`.

Writing `T=45*delta^2-38*delta-29`, the captured remainder denominators are
respectively `32*T^9`, `256*T^9`, `512*T^9`, `512*T^9`. After clearing `T^9`,
the captured numerator/denominator remainder is exactly `H^4 mod Q4`; its
`q` degree is below four. The binding is proved by nine fraction-free
division steps and exact zero residual, without generating a new Bezout
certificate.

The separate `lambda-binding-audit.py` proves that the literal main
coefficient captures specialize to

`main_H(delta,1,q) = H(delta,q)`

and

`main_S(delta,1,q) = 2*delta*q*Q4(delta,q)`.

The factor `2*delta` is a unit on the intended `delta != 0` chart. It is not
a constant unit of `QQ[delta]`; retain that parameter condition when using
the binding.

Both independent arithmetic sources check the leading-drop separation:

`T-(45*delta-83)*(delta+1)=54`,

with `H` infinity coefficient `delta+1` and `Q4` infinity coefficient `2*T`.
Also `Q4(0)=-400*delta`. The captured compact remainder formulas use the
`T != 0` chart; the displayed leading-drop identity does not.

## Main H divides S coefficient witness

`main-h3-literal-arithmetic.py` uses a separate strict expanded-monomial text
parser. Each of the three original entries in `h-divides-s-remainder.txt`
divides exactly by `ll^2`. The resulting generator term counts are
`[69,62,58]`; the three captured witness term counts are `[436,465,485]`.

The captured exponent is `2`. Exact denominator-cleared integer convolution
gives

`sum_i ((original_remainder_i/ll^2)*captured_witness_i) = U^2`,

where

`U = S_coeff5*dl*ll*(ll-1)*(ll^2-4*ll+1)*((ll+1)*dl+ll-1)*(dl+2*ll-1)`.

Here `S_coeff5` comes directly from the captured main-S coefficient list.
The target has 229 terms; the identity residual has zero terms. This audit
checks the displayed exponent-two witness and makes no assertion that two
is the minimal possible exponent.

## Evidence and limits

The raw outputs and JSON reports are saved alongside their sources:

- `h3-literal-arithmetic.stdout.txt`, `h3-literal-arithmetic-report.json`:
  all 16 requested zero-chart/compact-lambda identity and binding checks pass.
- `lambda-binding-stdout.txt`, `lambda-binding-result.json`: the main
  coefficient specialization and scalar binding pass.
- `main-h3-literal-arithmetic.stdout.txt`,
  `main-h3-literal-arithmetic-report.json`: the full original-generator
  exponent-two product passes.

No mathematical discrepancy was found. The initial main audit command
encountered a missing old `/private/tmp/stci-cas-venv/bin/python` path after
the execution environment changed; that operational failure is retained in
`main-h3-literal-arithmetic-attempt-01.stderr.txt`. The completed main audit
used `/opt/homebrew/bin/python3` and only its standard library, with empty
final stderr and exit code zero.

Normalization/conductor geometry, admissibility, repeated-root coverage,
parameter-stratum exhaustion, and characteristic-positive conclusions are
outside this supporting audit. Canonical acceptance and research-frontier
edits are left to the coordinating reviewer.
