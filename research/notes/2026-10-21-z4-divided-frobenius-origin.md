# Divided fourth powers and the Z4 embedded triple obstruction

Status: preliminary focused calculation; **not independently audited or promoted**. Base R=Z_(2) or Z_2. Sources: research/notes/2026-10-20-z4-characteristic-zero-lifting-report.md and companion obstruction/audit notes.

## Verdict

The valuation-one arithmetic defect is real, but no coordinate-independent map from the divided-fourth-power polynomial to the embedded obstruction group has been constructed. Consequently identifying the global obstruction canonically as a divided-Frobenius image is **not established**. The established source is the quadratic ambient transition and moving-base-coordinate substitution.

## Integral equation on U

Put x0=1, x1=u, x3=u^4+X, x2=u^3+Y. Then exactly

F=-X,
G=4u^9Y+6u^6Y^2+4u^3Y^3+Y^4-3u^8X-3u^4X^2-X^3.

Thus the fourth-power defect contributes 6u^6Y^2 mod normal degree 3, and survives mod 4 as 2u^6Y^2. But the cubic power of x3 contributes -3u^4X^2 and the opposite chart has moving c; isolating 6 in this chart is not an intrinsic construction.

The independently audited quadratic ambient transitions are
c=u^-1+u^-4Y-u^-5X+u^-9X^2-u^-8XY+O(3),
A=3u^-8X-4u^-7Y-9u^-12X^2+16u^-11XY-6u^-10Y^2+O(3),
B=2u^-7X-3u^-6Y-5u^-11X^2+9u^-10XY-3u^-9Y^2+O(3).
The -6u^-10Y^2 term in A is a direct binomial-fourth-power contribution; the complete obstruction also uses the nonlinear change c and both normal equations.

## Full Cech reduction

For a=2alpha, b=2beta, h=2gamma, d=1+2delta, the audited expressions give

C1=h(ah+3b^2-5bd+3d^2) = 2gamma (mod 4),
C2=(b-d)(4ah+3b^2-8bd+6d^2) = 2 (mod 4),
C3=a(ah+9b^2-23bd+15d^2) = 2alpha (mod 4).

Hence [ob] = 2gamma[u^-1]+2[u^-2]+2alpha[u^-3] (mod 4) in H^1(P1_R,O(-4)), in the fixed audited trivializations. The proposed stronger equality [ob]=2[u^-2] (mod 4) is FALSE for general first quotients. The middle coordinate remains universally nonzero. For the distinguished quotient a=b=h=0,d=1, the exact class is -6[u^-2].

The controlling sheaf is Hom(M,L^2)=O(-4), M=O(-8), L=O(-6). Quadratic normal-coordinate and generator corrections contribute Cech coboundaries. A coordinate-dependent coefficient projection is not by itself an intrinsic morphism from divided-power defects.

## General p^r

For 0<j<p^r, v_p(binomial(p^r,j))=r-v_p(j), because binomial(p^r-1,j-1) is a p-adic unit (Lucas). Therefore the first j with valuation one is p^(r-1). Mod p,
D_(p^r)(a,b)=D_p(a^(p^(r-1)),b^(p^(r-1))),
where D_n=((a+b)^n-a^n-b^n)/p for n=p^r, and D_p is interpreted similarly. In particular D4 mod 2=a^2b^2.

A local valuation-one polynomial does not imply a nonzero global obstruction. A well-defined map to the obstruction sheaf, coordinate/generator invariance, and a nonzero resulting Cech class must be established separately. The numerical coincidence with -6 is evidence of a contribution, not proof of a canonical identification.

## Reproducibility

Run python3 research/computations/verify_z4_divided_frobenius_2026_10_21.py (requires SymPy). The script verifies exact U expansion, coefficient reductions, and finite illustrative binomial valuation tests. The general valuation identity is proved above, not inferred from tests.

## Limitations

No new complete coordinate-independent decomposition of the full Cech class into divided-power and moving-coordinate pieces has been proved here. No canonical divided-Frobenius-to-obstruction map is claimed. This note does not modify the audited nonliftability theorem.
