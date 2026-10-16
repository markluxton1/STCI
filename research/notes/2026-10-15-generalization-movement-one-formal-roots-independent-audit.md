# Independent targeted audit: movement-one formal roots

Date: 2026-10-15. Reviewer: `g3_branch_uniqueness`.

**Verdict: PASS for Section 5 in its stated characteristic-zero scope.** The imported intrinsic nef criterion, branch/ruled-surface argument, and plane-adjunction inequality are premises. Only the new movement-one corollary was reviewed; accepted Sections 1--4 and prior CAS certificates were not re-audited.

Reviewed artifact: [Section 5 of nef formal branches over arbitrary bases](2026-10-15-generalization-nef-formal-branch-arbitrary-base.md).

Reviewed whole-file SHA-256:

`4d73bbb45ba2689a0f0fb33e88a32d2c3687b004371f06b5afc603ef3864a01e`.

For a smooth root of class `(1,r)` on the exceptional product of a balanced smooth rational degree-`e` curve, the new substitutions are correct:

`g=0`, `nu=(2e-1)r-1`, `h=er`.

When `e>=3` and `r>=2`, `nu>5` and `nu-h=(e-1)r-1>0`. The accepted criterion therefore gives an integral surface degree `1<=d<=r+1`. The function `(d-1)(d-2)` is nondecreasing on the positive integers, so the plane-adjunction lower bound would require

`e*r*(r-1) <= (d-1)(d-2) <= r*(r-1)`.

This is impossible. The all-orders exclusion for every `r>=2` is correct, with no claimed finite cutoff.

For `r=1` and `e>=4`, `nu=2e-2>5` and `nu>=h`; hence `d<=2`. A smooth rational plane curve has degree one or two by plane adjunction. Thus the given curve cannot lie in a plane, and the integral algebraic surface closure is a quadric `Q`.

The generic normal order `m` of `Q` along `C` is positive. Applying the imported plane inequality with `d=2` gives `0>=e*m*(m-1)`, hence `m=1`. The strict transform is therefore Cartier of class `2H-E`, whose restriction to `E` is `(1,1)`. This restriction is effective and contains the given integral `(1,1)` root `Z`. Their difference is an effective linearly trivial divisor on `P1 x P1`, hence zero: a global section of its trivial associated line bundle is a nonzero constant. Consequently `W|E=Z` as Cartier divisors, not only as supports.

At every point of `Z`, reduction of a local equation of `W` modulo an equation of `E` is a regular local parameter of the smooth surface `E`. Thus `W` is smooth and transverse to `E` there. Its smooth completed germ has only that one branch, so the original formal Cartier ideal equals the strict-transform ideal near `Z`; both ideals are units away from `Z` on `E`. This justifies the asserted equality on the whole completion along `E`.

The remaining smoothness and converse statements also pass. The ordinary first symbol of `Q` defines the normal derivative map

`N_C -> O_C(2)`.

Under `N_C=O_P1(2e-1)^2`, its two coefficients are sections of `O_P1(1)`. A simultaneous zero would give an entire exceptional fiber in `W|E`, impossible because `Z` is finite over `C`. They are therefore nowhere simultaneously zero, which is equivalent to `Q` being smooth along `C`.

Conversely, if a quadric contains `C` and is smooth along it, these two coefficients have no simultaneous zero. Two such degree-one sections are linearly independent, and their fiberwise linear zero locus is the smooth graph of a degree-one map `P1 -> P1`, of class `(1,1)`. The strict transform gives its compatible Cartier ideals on every exceptional neighborhood. Thus the converse supplies exactly the roots claimed in Section 5.

The degree boundaries are correctly retained: the `r>=2` exclusion assumes `e>=3`, whereas the `r=1` classification assumes `e>=4`. No conclusion for the omitted degree-three, order-one case is inferred. This audit does not import finite-jet rigidity for `C0`, enlarge the actual-CI bridge, or establish any finite cutoff.
