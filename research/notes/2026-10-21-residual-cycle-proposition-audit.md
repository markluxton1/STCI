# Residual-cycle criterion and wedge degeneracy — proof audit proposal

Status: mathematically proved below by standard intersection theory; repository proposal pending independent review. Scope: arbitrary characteristic, integral C of degree c in P3, homogeneous F,G of degrees d,e, no common surface component, both containing C.

Let Z=V_+(F,G). Because (F,G) is a regular sequence in the homogeneous coordinate ring, Z is a pure one-dimensional Cohen–Macaulay complete intersection. Its fundamental cycle is [Z]=Σ_D length(O_{Z,η_D})[D]. Put m_C=length(O_{Z,η_C}). Then [Z]=m_C[C]+R, R effective with no C component. Bézout yields de=c m_C+deg R. Thus R≠0 iff de>c m_C; R=0 iff Z_red=C (unmixedness excludes isolated components). For fixed C0, c=4. Note: the projective radical identity is sqrt((F,G)^sat)=I_C; sqrt((F,G))=I_C without saturation is not the correct general homogeneous formulation.

If the generic local initial ideal J* in K[X,Y] is computed, its colength equals m_C because the Artinian local quotient has finite m-adic filtration. This gives a direct algorithmic criterion once a certified standard basis has been computed. Merely computing (in F,in G) can undercount m_C.

Wedge test: when both first normal symbols are nonzero, vanishing of (dF∧dG)|_C means proportional first symbols and m_C>1. This does NOT force a residual curve: F=x, G=x+y^4 is a local counterexample with length four. A residual curve follows precisely when de>4m_C for the quartic. The possibility that additional GLOBAL hypotheses on proportional first jets force such a strict inequality remains open; it cannot follow from wedge vanishing alone.

Characteristic benchmark: for F=x1^4-x0^3x3, G=x2^4-x0x3^3, on x0=1 use t=x1,u=x2-t³,v=x3-t⁴. Then J=(v,(t³+u)^4-t¹²). Characteristic zero gives m_C=1 and residual degree 12; characteristic two gives m_C=4 and residual degree zero. No common surface component: F is irreducible (linear in x3 with coefficient -x0³ and x1⁴ coprime), and F does not divide G (its restriction to F has nonzero polynomial u^4 term). Thus the criterion proves the characteristic-two pair has reduced support C globally and the characteristic-zero pair does not.

Follow-up: investigate upper bounds on m_C from global proportional first-jet data, including divisor of common direction, poles of cancellation coefficients, and degeneration of higher relations. The proposition alone is an exact test, not a uniform degree exclusion.
