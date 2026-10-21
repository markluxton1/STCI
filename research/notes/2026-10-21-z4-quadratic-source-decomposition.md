# Quadratic source decomposition of the Z4 triple obstruction

Status: new exact coordinate calculation, **not independently audited**. Fixed raw integral coordinates and first quotient conventions of the 2026-10-20 obstruction report. Does not assert a canonical coordinate-independent splitting.

Let p=a+bu+3hu^2, q=d+2hu; P(c)=3ac^2+(3b-4d)c+h, Q(c)=2ac+2b-3d. Set c0=u^-1, c1=u^-4q-u^-5p, A1=3u^-8p-4u^-7q, B1=2u^-7p-3u^-6q,
A2=-9u^-12p^2+16u^-11pq-6u^-10q^2,
B2=-5u^-11p^2+9u^-10pq-3u^-9q^2.

The quadratic cocycle K=u^8([epsilon^2]m_V+u^-8[epsilon^2]m_U) decomposes as
K_A=u^8 Q(c0) A2,
K_B=-u^8 P(c0) B2,
K_move=u^8 c1(Q'(c0) A1-P'(c0) B1).
Terms involving arbitrary quadratic embedding corrections cancel against the linear kernel transition. These formulas are an **exact equality in the chosen frame**, not an invariant direct sum of cohomology classes.

For the distinguished quotient p=0,q=1,P=-4c,Q=-3:
K_A=18u^-2, K_B=-12u^-2, K_move=-12u^-2;
K=-6u^-2. The -6 in A2 comes directly from binomial(4,2); the other contributions are divisible by four.

For every allowed a,b,h in 2R, d in 1+2R, reduce the quadratic pieces mod 4. Since p=0 mod 2, q=d mod 2, P(c0)=-4dc0 mod 2 plus even terms, Q(c0)=-3d mod 2, and A2=-6u^-10 q^2 mod 4 plus p-dependent terms divisible by 4, we obtain
K_A = 18d^3 u^-2 = 2u^-2 (mod 4).
K_B=0 (mod 4), since P(c0) is even and B2 is even in this family? More carefully B2=-3u^-9 q^2 mod 2 and P(c0)=-4dc0 + terms in 2R, so P is even, but its product need not be 0 mod 4: its even parts include 3b c0+h, and B2 odd. Thus K_B can have mod-4 contributions in outer Laurent degrees, even if the middle coordinate vanishes mod 4. Likewise K_move may contribute outer coordinates. Only the middle-coordinate attribution is claimed.

Exact symbolic extraction gives middle Laurent coefficients:
[K_A]_-2 = -88abh+114adh-18b^3+59b^2d-60bd^2+18d^3;
[K_B]_-2 = 82abh-102adh+15b^3-47b^2d+45bd^2-12d^3;
[K_move]_-2 = 10abh-16adh+6b^3-23b^2d+29bd^2-12d^3.
Their sum is C2=(b-d)(4ah+3b^2-8bd+6d^2).
Modulo 4 the three middle coefficients are respectively 2,0,0. This is a uniform source attribution of the **middle coordinate** in the fixed raw frame, not only at the distinguished quotient.

This does not construct a natural map from divided-power polynomials to H^1(O(-4)). In particular, a change of raw normal coordinates changes the allocation among K_A, K_B and K_move. The total class is intrinsic for the fixed quotient, but the decomposition is not proved invariant.

Verification: run the script research/computations/verify_z4_quadratic_source_2026_10_21.py (SymPy). Its identities are algebraic; geometric invariance remains a separate question.
