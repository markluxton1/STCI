# Focused mathematical review: forced triple and residual-cycle globalization

Date: 2026-10-21. Scope: fresh line-by-line reasoning on two proof interfaces, independently of their recorded audit verdicts. This is not a re-run of every computational certificate.

## 1. R0012: why a hypothetical full lift forces a flat primitive triple

Let R be Z_(2) or Z_2, and let I be the ideal of a flat embedded lift of the prescribed (4,4) complete intersection. The exact sequence 0 -> I(4) --2--> I(4) -> I_0(4) -> 0 and H^1(I_0(4))=0 make multiplication by 2 surjective on finite H^1(I(4)); Nakayama kills this group. The two special quartics lift to global generators. Their cokernel vanishes on the special fiber; properness over the DVR eliminates a possible generic-only support. Thus the full family remains a (4,4) complete intersection.

If its generic reduced support is C, the generic degree-16 complete intersection has length four along the degree-four C. Cohen--Macaulay purity makes the generic local Artin algebra inject into its generic-point localization, where the fourth power of the maximal ideal is zero. R-flatness then descends I_C^4 subset I and I subset I_C to the total family.

The first conormal matrix has special rank one at every point; properness rules out a rank-zero point upstairs. Its generic rank cannot be two, since that would force multiplicity one. Its determinant vanishes generically and hence identically on the integral relative C, so the matrix has constant rank one. A local quartic combination H with unit normal coefficient cuts out a smooth relative surface W containing Z, and C is Cartier on W with local equation ell. On the generic fiber the other equation defines exactly ell^4. Both ideals I_(Z/W) and (ell^4) are 2-saturated (the former from R-flatness, the latter from its filtration by flat line bundles). Therefore they agree integrally. This yields local O_W/(ell^4), so every canonical quotient by J^n, especially J^3, is R-flat and reduces to the prescribed special stage. No independently chosen triple or global splitting is assumed.

The obstruction calculation then uses every first-order quotient p=a+bu+3hu^2, q=d+2hu and all quadratic corrections. For the prescribed mod-2 ribbon a,b,h are even and d is odd. Its H^1(O(-4)) coefficient C2=(b-d)(4ah+3b^2-8bd+6d^2) is 2 mod 4, since the first factor is odd and the second is 2 mod 4. The cohomology basis u^-1,u^-2,u^-3 is free over R; no coboundary can cancel that coefficient.

**Assessment: PASS for the stated unramified DVRs and fixed generic support.** The reduction to the triple is a consequence of flatness and the global CI, not an extra assumption. The arithmetic calculation was checked symbolically at the parity level here, not by re-running its complete expansion. Ramified DVRs and unrelated characteristic-zero multiple structures remain outside scope.

## 2. R0019: from local Smith lengths to global residual cycles

At a closed point of C, complete at R=k[[t]]. The CI algebra B is finite over R because its support is C, and torsion-free because a one-dimensional CI is Cohen--Macaulay with no embedded zero-dimensional associated prime. Thus B is free of rank m. Its saturated curvilinear filtration gives a free R-basis b_0=1,b_1,...,b_(m-1) adapted to the flag.

For q in the first nilpotent layer with nonzero generic first class, multiplication by q has zero first row and zero last column. Deleting them leaves an (m-1)-square triangular block with diagonal the maps E_i -> E_(i+1), whose valuations are ord(q_1)+ord(D_(i+1))-ord(D_i). The determinant is nonzero; it is the only potentially nonzero maximal minor, so the Smith-normal-form torsion length is (m-1)ord(q_1)+ord(D_(m-1)). This does not depend on higher coefficients of q.

On a smooth auxiliary surface Q, let h cut out C and write F|Q=h rho, G|Q=h sigma. Provided rho,sigma have no common curve component, cancellation of the nonzerodivisor h in the local ring of Q gives the exact sequence 0 -> O_(rho,sigma)(-C) -> O_Q/(h rho,h sigma) -> O_C -> 0. The middle term is B/qB; its torsion submodule is exactly the finite-length left term, because the right term is free over R. Therefore at each closed point the proper intersection multiplicity of rho and sigma equals the Smith length. Summing these local equalities, not merely their degrees, gives [rho intersect sigma]=(m-1)T+D_(m-1).

**Assessment: PASS conditional on finite-flat curvilinearity, saturated invertible order quotients, nonzero generic first class of q, and proper residual intersection.** The identity is one of zero-cycles. It neither asserts scheme equality nor survives an improper residual intersection without a separate correction.

## 3. Remaining scope boundaries

These checks validate the two logical interfaces but do not independently re-run all Macaulay2/Python calculations or prove that an arbitrary characteristic-zero STCI has the quasiprimitive filtration of R0019. In R0016, the nonsaturated resultant identity is proved by its separately audited duality and local flatness lemmas; R0010 serves as the saturated comparison and R0011 supports only the repeated-root strengthening.
