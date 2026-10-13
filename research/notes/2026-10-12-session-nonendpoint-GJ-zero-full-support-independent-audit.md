# Independent audit: nonendpoint G=J=0 full-support exclusion

Date of mathematical checks: 2026-10-12. Final audit saved: 2026-10-13.
Auditor: `oct11_endpoint_support_global_audit/two_root_contact_audit`.
Status: **PASS: geometric root cover and direct exact polynomial certificates**.

This audits the frozen [owner proof](2026-10-12-session-nonendpoint-GJ-zero-full-support-exclusion.md), SHA256
`9a3532827eaf3c45efcbf9759681d7070045923465710b19d06efc4799a06d33`.
No correction to its mathematical claim is required. The result excludes the
whole displayed `G=J=0` nonendpoint projection subfamily in every mate degree.
The unrestricted nonendpoint family and the universal STCI problem remain open.

## 1. Scope and geometric inputs

Work with fixed `C0=[1:z:z^3:z^4]` over an algebraically closed field of
characteristic zero, in the accepted intrinsic A4 quintic model. Retain
`delta!=0` and require the projection center to avoid the intrinsic surface
`S`. Here `B=b-a`, `G=g-3b+2a`, and `J=d-2g+2b-a`; this `J` is the lift
parameter, also denoted `Jbar`, rather than the first-normal cubic numerator.

The [target-fiber reduction](2026-10-12-session-nonendpoint-target-fiber-reduction-and-bounded-exclusions.md)
supplies the complete affine chart `S minus ell=A2(r,T)`, the actual sections
`X0,...,X3`, and the embedded curve `c:T=0`, with parameter
`z=(r-delta)/r`. The missing `r=infinity` point is the intrinsic A4 point
on `c`, mapping to `z=1`. Finite points of `ell` have quadric value
`-3delta^2`, so cannot give off-`c` inverse points of `C0`; the remaining
point of `ell` is the A4 point. Thus every possible off-`c` inverse point
is covered by the displayed affine chart, including inverse points at
target infinity. These previously audited chart facts are necessary here.

The accepted quintic full-support theorem makes
`(pi^{-1}(C0))_red=c` necessary for every mate degree. The argument below
contradicts that condition using actual fibers, including the quadratic
transverse term `T^2`. It uses no first-normal length bound. The case
`B=0`, namely `a=b=g=d`, is already excluded in Section 9 of the target-fiber
reduction and its [independent audit](2026-10-12-session-nonendpoint-target-fiber-independent-proof-audit.md).
The new argument therefore treats `B!=0` without losing the `B=0` case.

## 2. The forced parameter and the projective degree boundary

Put `k=B/delta^2!=0` and `p=1-z`. For a finite target, the exact equations,
with the actual normalization scalar `lambda=X0`, are

```text
F1 = delta r^3-(delta r+B)T-p lambda = 0,
F2 = 3delta^2 r^2-delta^3 r-p^2(3-p)lambda = 0,
F3 = delta^4-2delta^3 r+p^3(2-p)lambda = 0,
X0 = lambda.
```

These are invertible linear combinations of the actual target equations.
If the equations held with `lambda=0`, all four sections would vanish,
contrary to center avoidance. Thus reconstructing a solution of these
equations cannot produce a spurious projective point with zero coordinates.

At `p_c=-1/k`, `r_c=-k delta`, the two linear transverse constraints
become compatible and the remaining equation is exactly

```text
T*(p_c T+p_c a+B-delta-delta^2/p_c)=0.
```

Its reconstructed scalar is `lambda=k^4 delta^4!=0`, independently of `T`.
A nonzero second root gives an actual off-`c` point, so full support forces

```text
a=2k^2 delta^2-k delta=2B^2/delta^2-B/delta.             (A)
```

With (A), this fiber is genuinely doubled at `T=0`. No division by
`2-p_c` or `3-p_c` was used; in particular `k=-1/2` and `k=-1/3` are covered.

For target infinity, the equations are `X0=X1=X2=0`. When `r=0`, the
first coordinate difference and `B!=0` force `T=0`, so there is no off-`c`
point there. For `r!=0`, they force `delta r+B!=0` and
`T=delta r^3/(delta r+B)`. The actual remaining polynomials satisfy

```text
Qinf=3delta^2(r+k delta)(r-delta/3),
Pinf(-k delta)=-k^3 delta^5!=0,
Pinf(delta/3)=-delta^4 L/9,
L=(1+3k)^2-9delta k^2(1+2k).
```

The point `r=-k delta` is excluded explicitly, rather than discarded by
denominator cancellation. If `L=0`, then `r=delta/3` has nonzero
denominator: its possible vanishing would force `k=-1/3`, but at that
value `L=-delta/3!=0`. Its reconstructed `T` is nonzero and it is an
actual off-`c` point at target infinity; center avoidance gives `X3!=0`.
Consequently full support forces `L!=0`. This is a geometric proof of
the exact degree condition used next, covering the leading-coefficient
boundary before the finite-root argument.

## 3. Actual quintic equation and every exceptional root

Define

```text
P6=p^2-3p+3,             Pc=p^2-6p+6,
E=(1+3k)p-3-6k,
r_s=delta(3-p)/(3(2-p)),
lambda_s=delta^4/(3p^2(2-p)^2),
T_s=delta^2 P6 Pc/(9p(2-p)^2 E).
```

For `p!=0,2` and `E!=0`, the independent checker verifies `F1=F2=F3=0`
and the actual normalization identity

```text
X0(r_s,T_s)-lambda_s=delta^3 Pc W/(27p^2(2-p)^3 E^2),
W=p P6 E^2-9delta(p-2)(kp^2-2kp-1)
    *(2k^2p^2-6k^2p+kp^2+6k^2-4kp+6k+1).
```

In particular `[p^5]W=L` and `W(2)=2`. Thus full support gives an actual
degree-five polynomial, rather than an assumed generic-degree numerator.

Take a root of `W` outside `{0,3+sqrt(3),3-sqrt(3)}`. Its `Pc` value
is nonzero, and `p=2` is impossible. All remaining cases are covered:

- If `E!=0` and `P6!=0`, then `T_s!=0` and `lambda_s!=0`. The actual
  normalization identity gives an off-`c` point of the required target.
- If `E!=0` and `P6=0`, then `T_s=0`. The actual embedded `c` would
  require `r_s=delta/p`, whereas
  `p(3-p)-3(2-p)=-Pc!=0`. Thus this cannot be a root of `W`.
- If `E=0`, the exact polynomial identity that
  `3(2-p)W-delta P6^2 Pc` is divisible by `E` forces `P6=0`.
  Now `r_s=delta/(3-p)` and `delta r_s+B=0`. Both linear transverse
  constraints and their constants vanish. The remaining actual equation is
  `J0=pT^2+[delta r_s+B-p(2r_s^2+r_s-a)]T+r_s^3(pr_s-delta)=0`.
  Its leading coefficient and constant are nonzero. It therefore has a
  nonzero `T` root over the algebraically closed field, giving an actual
  off-`c` point. Its scalar is explicitly `lambda=delta r_s^3/p!=0`.

For the last case, `P6` has no roots at `0,2,3`, and is coprime to `Pc`;
the independent checker verifies the explicit identity
`((5-p)/3)P6+((p-2)/3)Pc=1`. Hence the nonzero constant and the asserted
inequality `r_s!=delta/p` do not conceal an exceptional coincidence.
At `p=3`, `E=3k!=0`, so no omitted division by `3-p` occurs: that
division was used only on the `P6=0` case. At `k=-1/3`, `E=-1`, and
there is no `E=0` fiber. The target `p=0` is deliberately retained with
every possible multiplicity; the branch formula is never evaluated there.

Thus full support forces every root of `W` into the three displayed
distinct targets, with no uncovered finite denominator or projective fiber.

## 4. Complete profiles and direct certificate verification

Choose `s` with `s^2=3`. The degree and root-cover conclusions force

```text
W=L p^i(p-(3+s))^j(p-(3-s))^h,
i,j,h>=0, i+j+h=5.
```

There are exactly 21 triples. They include every order `0,...,5` at
`p=0`. The leading coefficients already agree, so each profile is exactly
five equations `f_t=[p^t]W-L[p^t](monic profile)=0`, for `t=0,...,4`.
The [owner's exported artifact](../validation/2026-10-12-nonendpoint-GJ-zero-normalized-lead/twenty-one-polynomial-bezout-certificates.txt)
prints five polynomials `b_t` for each profile, with `sum f_t b_t=1`.

The independent verifier parses those actual exported vectors and directly
multiplies them with sparse standard-library `Fraction` polynomial
arithmetic in `Q[p,k,delta,s]/(s^2-3)`. It regenerates no Groebner basis
or certificate vector. Every product is exactly `1`; every `b_t` contains
no `p` and is a polynomial in the parameters, with only constant rational
number-field coefficients. No saturation, inverse parameter, or omitted
parameter fiber is present in these identities. They specialize under
every embedding `Q(s)` into the algebraically closed characteristic-zero
field. Changing the choice of `s` swaps `j,h` in an already complete list.
Therefore all 21 necessary profiles are impossible.

## 5. Captured evidence and conclusion

The independent [source](../validation/2026-10-12-nonendpoint-GJ-zero-independent-audit/verify_fraction_certificates.py)
has SHA256 `de3e420cb004884b7771322468756fdab362f035ed69657e152428cb71c83ceb`.
Its accepted [execution record](../validation/2026-10-12-nonendpoint-GJ-zero-independent-audit/attempts/20261012T213210690020Z/execution-record.json)
captures the actual command, source snapshot, certificate-input snapshot,
raw stdout and stderr, and their SHA256 hashes. It records exit `0` and
**PASS, 80 assertions**: 15 structural identities, 21 checks that the
certificate vectors are parameter polynomials, 21 monic-profile checks,
21 direct exported-certificate products, and two completeness/degree checks.
These are assertions in one independent checker lineage, not 80 separate
geometric results. The recorded executable is
`/Library/Developer/CommandLineTools/usr/bin/python3`.

The earlier [failed attempt](../validation/2026-10-12-nonendpoint-GJ-zero-independent-audit/attempts/20261012T213152010950Z/execution-record.json)
is retained with source and raw streams. Its failure was a parser syntax
collision between the Macaulay2 variable `del` and the Python keyword;
the accepted source aliases that token to `par_delta`. No mathematical
identity failed, and no failed capture was overwritten.

The accepted independent record binds the unchanged owner note, source
`44d3b193783dc76562febe23af452a5b863b65b5f992dc6b1f83fad4a0c8fc33`,
owner execution record
`8e317259cf5e7fa71f16cfcd71f5e630354b4c52471c1329698bfb62582d1bb2`,
and actual exported certificate input
`46e1c3daa4c1b927a91bb65c747775de243533d4c6dc98b9562324fbb99aa304`.
No owner, canonical, historical seal, or Git file was changed by this audit.

**Audited conclusion:** `B!=0`, `G=Jbar=0` cannot have full inverse
support under the stated hypotheses. Combined with the separately audited
`B=0` exclusion, this proves the whole `G=Jbar=0` nonendpoint subfamily
admits no mate in any degree. Other nonendpoint parameter strata remain
open; this result is not a proof of non-STCI for `C0` or of the universal
projective-curve STCI statement.
