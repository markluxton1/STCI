# Coordinate-invariance counterexample for the naive quadratic summand

Status: exact calculation, provisional; not independently audited or promoted.

Fix the distinguished quotient p=0,q=1,P=-4c,Q=-3, so m_V=-3A+4cB. Along X=0,Y=epsilon the quadratic coefficients are A2=-6u^-10, B2=-3u^-9, and c1=u^-4. The quadratic cocycle decomposition in the original normal coordinates is K_A=18u^-2, K_B=-12u^-2, K_move=-12u^-2, giving total K=-6u^-2.

Make the invertible integral normal-coordinate change A'=A+B, B'=B on V. Then m_V=-3A'+(4c+3)B'. The quadratic coefficient A2'=A2+B2=-6u^-10-3u^-9. Thus K_A'=18u^-2+9u^-1, K_B'=-12u^-2-9u^-1, and K_move'=-12u^-2. The total remains -6u^-2.

The difference [K_A']-[K_A]=9[u^-1] is nonzero in H^1(P1_R,O(-4))=R[u,u^-1]/(R[u]+u^-4 R[u^-1]); it even survives mod 2. Therefore the naive 'first normal coordinate' quadratic contribution does not define an intrinsic cohomology class. This disproves invariance of that decomposition, but does not disprove the existence of a more sophisticated canonical divided-Frobenius-to-obstruction construction.

Verification: direct substitution into the audited transition formulas suffices. No general nonexistence assertion about canonical divided-power operations is made.