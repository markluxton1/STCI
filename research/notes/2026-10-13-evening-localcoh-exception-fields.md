# Second endpoint family: exact cubic and quartic exception closure

Date: 2026-10-13. Scope: characteristic zero, the fixed smooth rational quartic
`C0=[s^4:s^3t:st^3:t^4]`, the audited actual quartic-ancestor multiplication
tensor, primitive degree-two normal-dual directions, pure cubic top `h=t`,
and the second rational endpoint family. This does not address boundary
families with `p(0)=0`, nonendpoint cubic top zeros, or higher ancestor degrees.

## Exact result currently completed

**PROVED under the audited actual multiplication tensor and coordinate bases:**
every root of both factors

```text
f3=3*k^3+4*k^2+9*k-4
f4=13*k^4+10*k^3+2*k^2-42*k-7
```

is excluded for **every** affine lower-lift parameter `lambda`. These account
for seven of the 22 geometric parameter points still retained after the
accepted generic and quadratic calculations. The degree-15 factor remains
OPEN pending the separate exact field calculation discussed below.

The Macaulay2 computations returned target evaluation ideal `(1)` over each
number-field polynomial ring `K[lambda]` and a polynomial left dual `n` with

```text
n^T L(a*(k)+lambda*k0)=0,
n^T u=1.
```

The cubic dual has 26 nonzero entries and degree at most two in `lambda`.
The quartic dual has 26 nonzero entries and degree at most one in `lambda`.
Consequently these certificates exclude the entire affine lower-lift fibers;
they are not ranks or point samples.

## Full-fiber verification and logical scope

The new standard-library verifier
[`evening_localcoh_family2_exception_fields_2026_10_13.py`](../computations/evening_localcoh_family2_exception_fields_2026_10_13.py)
uses `Fraction`, exact polynomial division, and a restricted AST expression
parser. It works in the quotient `QQ[k]/(f)` represented by coefficient
vectors and separately in its polynomial variable `lambda`. Its certificate
verification rederives every source denominator inverse, all rational
direction expressions, all 30 seed coefficients, the affine slope vector,
and both primitive homogeneous directions. It checks:

1. The actual 32-by-30 top matrix has rank 29 over `QQ`.
2. The specified slope vector is nonzero and every seed plus `lambda*k0`
   satisfies all 32 pure-top identities. Since the top map has one-dimensional
   kernel, this gives every possible affine lift of the specified top.
3. The factor is square-free, so its degree counts distinct geometric roots.
4. The homogeneous Sylvester determinant matches the rational source
   resultant and is a **unit** modulo the factor, so every root has a
   primitive direction and no omitted nonprimitive stratum.
5. The actual tensor target columns are `e72,e73`, the dual coordinate
   `n72` is the constant one, and all eighteen entries of `n^T L` vanish
   identically as polynomials in `lambda` modulo the full factor.

The last identities imply exclusion after every homomorphism from the
quotient into an algebraically closed field of characteristic zero. Thus
coverage of all roots does not depend on accepting a numerical embedding,
a sampled rank, or even the Macaulay2 factorization result. The exact
Macaulay2 `factor` output also reports both factors as irreducible, but the
independent verification only needs square-freeness and the explicitly
checked unit inversions.

The actual tensor and coordinate sources are unchanged and SHA-256-bound
inside each certificate. They are the same tensor sources accepted in the
[previous independent quadratic audit](2026-10-08-session-localcoh-family2-quadratic-independent-audit.md).
This certificate inherits that audited coordinate interpretation; it does
not reconstruct the ambient quotient basis from fresh geometric generators.

## Reproduction and retained evidence

Generate the exact matrix inputs:

```sh
python3 research/computations/evening_localcoh_family2_exception_fields_2026_10_13.py --generate cubic quartic
```

Generate the full polynomial left kernels and duals:

```sh
/opt/homebrew/bin/M2 --script research/computations/evening-localcoh-family2-cubic-2026-10-13.m2
/opt/homebrew/bin/M2 --script research/computations/evening-localcoh-family2-quartic-2026-10-13.m2
```

Regenerate the two exact JSON certificates and verify all identities:

```sh
python3 research/computations/evening_localcoh_family2_exception_fields_2026_10_13.py --regenerate cubic quartic
```

Thereafter default verification uses only the saved certificate and an
ordinary Python 3 runtime:

```sh
python3 research/computations/evening_localcoh_family2_exception_fields_2026_10_13.py cubic quartic
```

Evidence, including the raw complete duals, target ideal outputs, terminal
logs, and JSON certificates, is retained under the respective stems
`research/computations/evening-localcoh-family2-cubic-2026-10-13` and
`research/computations/evening-localcoh-family2-quartic-2026-10-13`.
The final full-kernel processes returned exit code zero; the cubic process
finished directly and the quartic process was collected from tool session
`90236`. The strengthened independent regeneration/verification returned
exit code zero for both cases.

## Failed attempts and runtime details

The first generated M2 source used `assert #factor f==1`, which is invalid
for this Macaulay2 version because `factor` returns a `Product`. Both runs
stopped at that parser/type check before constructing any matrix. The failed
logs are preserved as `...-attempt01.log`; no mathematical result is taken
from those runs. The corrected source prints `factor f`, and the all-roots
logic is instead independently checked by exact quotient identities.

The historical SymPy interpreter path currently exists but lacks the SymPy
package (`ModuleNotFoundError`). No package installation was required. A
`--script /dev/stdin` factor probe also failed because M2 could not reopen
the shell-generated descriptor path; a saved ordinary `.m2` file succeeded.

## Continuation at the degree-15 factor

The exact generalized arithmetic includes the remaining degree-15 modulus.
A separate agent is attempting a polynomial dual of degree at most two via
ordinary field linear algebra. Writing `L=L0+lambda*L1` and
`n=n0+lambda*n1+lambda^2*n2` reduces the full polynomial identity to

```text
L0^T n0=0
L0^T n1+L1^T n0=0
L0^T n2+L1^T n1=0
L1^T n2=0
(n0)72=1, (n1)72=(n2)72=0.
```

This is a 75-by-222 exact linear system over `QQ[k]/(f15)`. A successful
solution will be independently checked against all source expressions by
the same generalized verifier. Existence has not yet been asserted here.
