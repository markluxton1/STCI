# Independent endpoint audit and one completed exceptional fibre

Date: 2026-10-07. Scope: the characteristic-zero curve
`C0=[s^4:s^3t:st^3:t^4]`, primitive degree-two normal-dual direction,
and pure cubic top coefficient `h=t`. This is an independent audit of
Sections 4--6 of
[`2026-10-06-session-localcoh-progress.md`](2026-10-06-session-localcoh-progress.md).
It proves the stated endpoint classification and the first family's
generic exclusion, and closes its quadratic exceptional locus. It does
not exclude every quartic ancestor or address a nonendpoint top-zero.

## 1. Verdict and precise remaining locus

**PROVED under the previously audited actual top map and multiplication
tensor:** the four one-parameter direction families in the checkpoint
cover all remaining primitive `e=2,h=t` endpoint directions, after the
three corner directions and the reversed parity direction are removed.
Their lower corrections are the complete affine line `a*+lambda*k0`.
The first rational family excludes the target `u` for every `lambda`
outside the roots of its displayed clearing denominator. The formerly
retained locus `k^2-4k+5=0` is now excluded at both roots, again for every
`lambda`, by a complete exact number-field dual.

The first family's unresolved direction parameters are exactly the roots
of the following three polynomials **as exceptions to the available
dual**, without any implication that they support an ancestor:

```text
3k^4-9k^3-19k^2-43k-4
13k^4+26k^3+34k^2+6k-7
729k^13+1620k^12+2889k^11-11268k^10-26574k^9-39642k^8
 +94014k^7+272968k^6+454897k^5+62256k^4-571463k^3
 -1210068k^2-966908k-379834
```

All three are square-free and pairwise coprime. They are coprime to
`(k^2-1)(k^2+2k+3)(9k^4-21k^3+5k^2-31k+134)`, so all **21 geometric
parameter points** remain in the first family's primitive chart. Each
point retains the complete affine `lambda` fibre. The second rational
family and the two `p(0)=0` boundary families also retain their actual
quartic multiplier incidence. Their saved `.m2` inputs do not prove a
kernel or evaluation result; no live process was assumed and no seed
was promoted to an exclusion.

## 2. Surjectivity of the rational normalization

For `p(0)r(0)!=0`, actual torus and common direction scaling give
`p(0)=r(0)=1`. The top-image equations first determine

```text
b1=-6(a1^2+a2)-2a1-3/2,
Q=16a2^2+(16a1^2+12)a2+12a1^2+4a1+3=0.
```

The saved parametrization does more than give solutions. On `2a1+1!=0`
its inverse is the rational function

```text
k=(32a2+16a1^2+12)/(4(2a1+1)^2).
```

Modulo `Q`, its square is `(2a1-3)/(2a1+1)`. Substituting it into
`a1=(k^2+3)/(2(1-k^2))` and
`a2=-(k^2+2k+3)/(2(k+1)^2)` recovers the original coordinates exactly.
Neither `k=1` nor `k=-1` can arise from a finite point of this chart:
`k^2-1=-4/(2a1+1)`. At `2a1+1=0`, the equation is
`4(2a2+1)^2=0`; the last top equation is `2(b2+2)^2=0`.
Thus the unique missing normalization point is
`(a1,a2,b1,b2)=(-1/2,-1/2,1,-2)`, whose quadratic pair has the common
factor `1-t`. It is nonprimitive and loses no candidate. The remaining
top equation factors exactly into the two stated choices of `b2`.

On the separate endpoint boundary `p(0)=0,r(0)!=0`, normalization to
`r(0)=1` gives `b1=8a1^2a2` and precisely

```text
4a2(2a1+1)[(2a1+1)^2b2
           +2a2^2(2a1-1)(16a1^4+8a1^2+5)]=0.
```

For `a2=0`, the full homogeneous quadratic resultant is `a1^2*b2`,
so primitivity requires both factors nonzero. The actual reversal sends
this branch to the already certified parity branch, as in the checkpoint.
For `a2!=0`, torus normalization gives `a2=1`. Then either
`a1!=-1/2` and the displayed rational boundary formula holds, or
`a1=-1/2` and `b2` is free. The latter family has resultant `(b2+8)/4`
and must remain. No division by `a2` or `2a1+1` removes it.

The independent script uses a fixed four-by-four Sylvester determinant,
so its resultant checks include roots at infinity when leading
coefficients specialize to zero. It verifies the rational inverse and
all four saved seeds against the 32-by-30 actual top map. The map has
rank 29, its three annihilator rows have rank three, and its kernel is
one-dimensional. Hence the affine line of lower corrections is complete
at every retained parameter value.

## 3. What the generic polynomial dual actually proves

The saved first-family JSON has a cleared ancestor

```text
A=120(k-1)^9(k+1)^9*(a*(k)+lambda*k0).
```

The independent audit checks this identity coordinate by coordinate,
and checks `a*(k)` against its actual pure cubic top. The prefactor is
nonzero throughout the retained chart. The standard-library dual
verifier then checks all 18 actual tensor columns and the target value
against its full polynomial denominator. The independent audit also
reconstructs the displayed factorization of that target value exactly.
Thus the exclusion concerns the specified complete affine family of
ancestors, rather than an unrelated tensor kernel.

The factors `k+/-1` lie outside the chart. The factors `k^2+2k+3` and
`9k^4-21k^3+5k^2-31k+134` are precisely nonprimitive loci for the first
family. The additional quadratic `k^2-4k+5` was a genuine primitive
exception to this particular generic dual, and is closed next. The three
remaining factors retain the 21 points listed above.

## 4. Exact closure of the quadratic exception

The saved Macaulay2 output is a 74-entry row over

```text
K[lambda], K=QQ[k]/(k^2-4k+5).
```

Its entry 72 is exactly one. I reduced the actual rational seed and every
dual coefficient modulo the defining polynomial, checking each
denominator is a field unit. The defining polynomial has discriminant
`-4`, so it is irreducible over `QQ`. This is an exact field calculation;
it treats both geometric roots through the two embeddings into an
algebraically closed characteristic-zero field.

The new independent certificate stores each coefficient as `a+b*k` with
`a,b` rational. Its default verifier uses only Python's standard library
and the relation `k^2=4k-5`. It checks:

- the hashes of the actual tensor, coordinate basis, top map, rational
  seed, saved complete dual, evaluation file and module input;
- the actual pure cubic top of the entire affine ancestor, with its
  lower direction in the top-map kernel;
- the target columns `e72,e73` in the saved tensor;
- **all 18** polynomial identities `n^T L=0` over `K[lambda]`;
- `n^T u=1` and a nonzero primitive resultant.

Consequently no member at either quadratic root maps to `u`, for any
`lambda`. This removes `k^2-4k+5` from the unresolved exception list.
The certificate does not require trusting that the saved module's
kernel command or printed evaluation ideal was correct.

## 5. Reproduction and evidence

Run the complete endpoint audit with the repository's SymPy runtime:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/computations/audit_session_localcoh_endpoint_2026_10_07.py
```

Verify the completed quadratic exception with an ordinary Python:

```sh
python3 research/computations/verify_session_localcoh_q2_dual_2026_10_07.py
```

Regenerate its coefficient certificate from the saved rational sources
with the SymPy runtime and `--regenerate` on that same verifier.

The two exact output records are
[`session_localcoh_endpoint_audit_2026_10_07.json`](../computations/session_localcoh_endpoint_audit_2026_10_07.json)
and
[`session_localcoh_q2_dual_audit_2026_10_07.json`](../computations/session_localcoh_q2_dual_audit_2026_10_07.json).
Both were freshly generated and all assertions passed on 2026-10-07.
The uncomputed family inputs and every remaining denominator locus are
preserved for the next session.
