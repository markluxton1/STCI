# Independent arithmetic audit: global CI filtration constraints

Date: 2026-10-19.
Reviewer: independent generalized-arithmetic worker.
Outcome: **PASS for the conditional finiteness proposition below.**
This note supplies independent proof review evidence. It does not promote
a canonical record or independently certify the geometric construction of
the generator filtration.

Audited proposal: section 7 of
[the global CI filtration investigation](2026-10-19-global-ci-filtration-investigation.md).
The factorization arguments and strict cutoff in that section agree with
the independent reconstruction below.

## Exact scope and dependencies

The geometric application concerns the fixed rational quartic
`C0=[u^4:u^3v:uv^3:v^4]` over an algebraically closed field of
characteristic zero, with conormal bundle `O_P1(-7)^2`. Assume an actual
global complete intersection `Y=V(F_a,G_b)` has reduced support exactly
`C0`, and satisfies the hypotheses of
[STCI-R-0010](../results/saturated_first_relation_normal_flatness.md),
with full generic ordinary initial CI degrees `2<=r<s` and first
relation `R=O(-7r-epsilon)`.

The arithmetic audit takes the following further conclusions as explicit
premises of the proposed global-generator argument:

    epsilon is an integer, 1<=epsilon<=8;
    a,b,r,s are positive integers, r>=2, s>r;
    ab=4rs,                    a,b>=3r;
    4(a+b)=7(r+s)-epsilon(s-r)/r;
    r divides epsilon*s.                                   (A)

STCI-R-0010 is promoted, but does not itself state the actual-generator
exact sequence or its degree consequences. Their proof is an additional
dependency of the geometric application. The restriction `a,b>=3r`
uses the absence of a quadric factor in either actual STCI equation and
its exact normal order `r`. Its inherited supporting evidence is the
[entirely-thick audit](2026-10-06-session-thick-independent-audit.md),
under its stated STCI hypotheses. The legacy
[entirely-thick topic](../results/entirely_thick.md) is navigation, not an
additional ID-bearing promoted theorem. These lower bounds are not
premises for arbitrary intersections with residual components.

**Audited claim.** For each fixed `epsilon` in `1,...,8`, there are only
finitely many unordered quadruples `(r,s; a,b)` satisfying (A). The
proof includes every small `r`, including `5r-3epsilon<=0` and the
endpoint of the large-`r` cutoff. This is numerical finiteness, not
existence of a geometric complete intersection for any surviving tuple.

## Independent derivation of the large-order reduction

Put `t=s/r>1` and `x=epsilon/r>0`. The sum equation and positivity give

    4(a+b)/r = 7(1+t)-x(t-1) < 7(1+t).

Since `ab=4rs`, the arithmetic-geometric mean inequality gives
`a+b>=4sqrt(rs)`. Consequently

    16sqrt(t) < 7(1+t),

and, because `t>1`,

    t>rho=(79+16sqrt(15))/49>23/8.                           (B)

The last strict comparison is exact: it is equivalent to
`sqrt(15)>495/128`, and `15*128^2=245760>245025=495^2`.

Order `a<=b`. For fixed product `ab=4rs`, the function
`z+4rs/z` decreases on `0<z<=2sqrt(rs)`. Since
`3r<=a<=2sqrt(rs)`,

    a+b <= 3r+4s/3.

Combining this with the sum equation gives

    (5r-3epsilon)t <= 15r-3epsilon.                        (C)

This inequality is used as an upper bound only when
`5r-3epsilon>0`.

Define `B_epsilon=3epsilon(2epsilon+1)/5`. If
`r>B_epsilon`, then in particular `5r-3epsilon>0`, and (C) becomes

    t <= 3+6epsilon/(5r-3epsilon) < 3+1/epsilon.             (D)

The divisibility premise in (A) gives `t in (1/epsilon) Z`.
For `1<=epsilon<=8`, its largest possible value below `3` is
`3-1/epsilon<=23/8<rho`. Thus (B) forces `t>=3`, while (D) forces
`t<3+1/epsilon`. Hence

    r>B_epsilon  implies  s=3r.                            (E)

The restriction `epsilon<=8` is essential to this particular argument:
for `epsilon>=9`, lattice values strictly between `rho` and `3` can
occur. No finiteness claim for those movements is established here.

When `s=3r`, the sum equation reduces to

    a+b=7r-epsilon/2.

Thus odd `epsilon` gives no large-order tuples. If `epsilon=2k`, let
`D=b-a>=0`. The product equation gives

    D^2=(7r-k)^2-48r^2=(r-7k)^2-48k^2,

and therefore

    ((r-7k)-D)((r-7k)+D)=48k^2=12epsilon^2.                (F)

The right side is a fixed positive integer. Every solution of (F)
comes from a signed divisor pair of that integer. Parity and positivity
conditions recover integral `r,a,b`; imposing them can only shrink the
finite set. Neither factor can vanish. This proves finiteness in the
large-order range, without an unbounded numerical search.

## Small orders, including a nonpositive denominator

There are finitely many integers `2<=r<=B_epsilon`. Fix any such `r`
and write

    c=7r-epsilon.

For the stated range, `c>=14-8=6>0`. Eliminate `s=ab/(4r)` from the
sum equation in (A). Direct expansion gives the exact factorization

    (c*a-16r^2)(c*b-16r^2)=4r^2(15r^2+epsilon^2).          (G)

The right side is strictly positive, so each integral factor is a
nonzero signed divisor of that fixed integer. There are finitely many
such pairs, and `c>0` recovers at most one `a,b` from each pair.
Retaining only integral `a,b>=3r` and integral `s=ab/(4r)>r`, followed
by the remaining exact conditions in (A), is a finite procedure.
Both-positive and both-negative divisor pairs must be retained before
these filters. The proof never divides by `5r-3epsilon`, and therefore
covers the entire exceptional small-order range.

The cutoff is strict. For example, at `epsilon=7` the tuple

    (r,s; a,b)=(63,198; 189,264)

satisfies (A), with `r=B_epsilon` and
`t=22/7=3+1/epsilon`. It must be processed by (G), not discarded by
the strict large-order argument.

Equations (F) and (G) prove the stated finiteness proposition. They do
not assert that the finite lists have been geometrically excluded, or
that the arithmetic and spectral Picard conditions are sufficient for
lifting to the actual formal neighborhood or to projective equations.

## Explicit bounds and supplementary exact enumeration

For odd `epsilon`, the large-order range is empty, so

    r<=floor(3epsilon(2epsilon+1)/5).

For even `epsilon=2k`, the two factors in (F) have the same parity.
Their product is even, so they are both even. Write them `2u,2v`;
then `uv=12k^2` and `r=7k+u+v`. Positive divisor pairs satisfy
`u+v<=12k^2+1`, and negative divisor pairs satisfy the same upper
bound. Therefore the large-order range has

    r<=7k+12k^2+1.

This bound also exceeds the small-order cutoff, since

    (12k^2+7k+1)-(24k^2+6k)/5
      =(36k^2+29k+5)/5>0.

The resulting uniform bounds on `r` are `20,63,130,221` for
`epsilon=2,4,6,8`, respectively; for `epsilon=3,5,7` they are
`12,33,63`. For `epsilon=1`, the bound is below `r=2`, proving
numerical nonexistence directly.

The companion standard-library-only script
[global_ci_small_movement_divisor_audit.py](../computations/global_ci_small_movement_divisor_audit.py)
implements (F) and (G), including signed divisors and every endpoint.
Executed command:

```text
python3 research/computations/global_ci_small_movement_divisor_audit.py --show-tuples
```

The exact candidate counts and largest surviving `r` were:

| epsilon | unordered arithmetic candidates | maximum surviving r |
|---:|---:|---:|
| 1 | 0 | none |
| 2 | 6 | 20 |
| 3 | 4 | 3 |
| 4 | 11 | 63 |
| 5 | 9 | 10 |
| 6 | 19 | 130 |
| 7 | 9 | 63 |
| 8 | 19 | 221 |

For `epsilon=2` the script independently reproduced exactly

    (2,8;8,8), (2,12;6,16), (6,21;18,28),
    (14,42;48,49), (15,45;50,54), (20,60;64,75).

The proof of the finite search domain precedes the computation. These
counts concern precisely the arithmetic system (A). Root Picard descent,
ambient obstructions, and geometric realization are not tested.
