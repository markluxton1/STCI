# Independent targeted audit: nef polarizations and arbitrary base genus

Date: 2026-10-15. Reviewer: `g3_branch_uniqueness`.

**Verdict: PASS for the stated new characteristic-zero scope.** This is a targeted review of the new intrinsic formulation, vector-bundle hypothesis, adjunction and degree formulas, passage to inequality (13), and conditional movement-two consequence. The already audited branch-algebraization, normalization, ruled-neighborhood, square-comparison, and plane-multiplicity arguments are premises and were not re-audited. No CAS computation or accepted verifier was rerun.

Reviewed artifact: [nef formal branches over arbitrary bases](2026-10-15-generalization-nef-formal-branch-arbitrary-base.md).

Reviewed SHA-256:

`9f37b173480e1e933702ead3fb53f0fe8bd3e68c073f26db00a083269d221984`.

## Intrinsic nef-polarization statement

The repackaging in Section 1 is valid. For the resolution `f:T->W` supplied by the imported branch lemma, the pullback `H=f^*(A|W)` is nef and satisfies `H.Z=A.Z=h` and `H^2=A^2.W=d` by projection. These are exactly the numerical inputs used by that lemma; no rational base or blowup presentation is used in them. Its ruled-model nef class has integer fiber degree `a>=0`. If `a=0`, its square is zero, contradicting the square comparison when `d>0`; hence `a>=1`. Thus the imported bound applies without an additional positivity assumption on the ambient nef line bundle.

The condition `d>0` is essential and is correctly retained. An ample `A` satisfies it on every integral surface. For merely nef `A`, no contradiction is claimed when `d=0`. The sentence about contraction is only an example of vanishing square; a general nef line bundle need not define a contraction. This does not affect the stated criterion.

## Exact normal bundle and new intersection formulas

The actual isomorphism `N_(C/P3)=L direct_sum L` is the correct hypothesis. The distinction from numerical balance in Section 2 is necessary. Conversely, a trivialization of `P(N)` over `C` makes its relative degree-one tautological bundle of the form `Q boxtimes O(1)`; relative pushforward recovers two identical line summands, with duals adjusted to the projectivization convention. Thus the stated equivalence with triviality as a `P1`-bundle over `C` is valid.

The Euler sequence gives `deg(T_P3|C)=4e`; the tangent sequence then gives `deg N=4e-(2-2gamma)`. Under the exact direct-sum hypothesis this yields

`lambda=2e+gamma-1`.

On `C x P1`, divisor intersections are

`(M boxtimes O(r))^2=2epsilon*r`,

`K_E.Z=r(2gamma-2)-2epsilon`.

Adjunction gives

`2g_Z-2=2epsilon*r+r(2gamma-2)-2epsilon`,

which is equivalent to the stated

`g_Z=r*gamma+(epsilon-1)(r-1)`.

Since `O_E(E)=L boxtimes O(-1)`, its degree on `Z` is `lambda*r-epsilon`; the hyperplane restriction is pulled back from a line bundle of degree `e` on `C`, so its degree on `Z` is `e*r`. Equations (4)--(6) are therefore correct. The formulas use the actual line bundles and intersection numbers, not a separability argument.

The accepted plane-multiplicity argument extends to this setting without a change: its number of imposed plane points is the degree `e` of `C`, and the root's fiber degree remains `r`. The genus of `C` does not appear in it.

## Numerical deductions and inequality (13)

Direct substitution gives

`nu-4g_Z-5=(2e-3gamma+3-4epsilon)*r+3epsilon-9`,

and

`nu-h=(e+gamma-1)*r-epsilon`.

Thus (10) and (11) are exactly the stated conditions. When `nu>=h`, for every integer `a>=1`,

`[2ah-nu*a^2]-[2h-nu]=(a-1)[2h-nu(a+1)]<=0`.

Consequently the maximum occurs at `a=1`, with value

`D=2h-nu=(1-gamma)*r+epsilon`.

The passage from the existence of an integer `1<=d<=D` satisfying (9) to (13) is correct, including the small-degree cases. All quantities are integers, and `P(k)=(k-1)(k-2)` is nondecreasing on the positive integers: `P(k+1)-P(k)=2(k-1)>=0`. In particular `P(1)=P(2)=0`. Therefore `P(D)>=P(d)>=e*r*(r-1)`. The separate requirement `D>=1` is necessary and is explicitly present. Inequality (13) is used only as a necessary condition, as it should be.

For `epsilon=2`, `e>=4`, and `r>=2`, condition (11) follows from `(e+gamma-1)r>=6>2`. Assuming (10), `gamma=1` gives `1<=d<=2`, incompatible with the positive right side of (9). For `gamma>=2`, `D=2-(gamma-1)r<=0`, contradicting `d>=1`. The positive-genus movement-two corollary is therefore valid with its high-self-intersection condition retained.

## Scope of this pass

This pass establishes no existence claim for curves with normal bundle `L direct_sum L`, no arbitrary-characteristic extension, no actual-CI exclusion beyond the imported bridge hypotheses, and no finite-tower representability or uniqueness statement over higher-genus Picard parameter spaces. Section 4 correctly preserves all of these boundaries. The original research problem is not concluded by this scope extension.
