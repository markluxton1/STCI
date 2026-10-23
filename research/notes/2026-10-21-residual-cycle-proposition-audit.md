# Residual-cycle criterion and wedge degeneracy — proof audit proposal

Status: mathematically proved below by standard intersection theory; repository proposal pending independent review. Scope: arbitrary characteristic, integral C of degree c in P3, homogeneous F,G of degrees d,e, no common surface component, both containing C.

Let Z=V_+(F,G). Because (F,G) is a regular sequence in the homogeneous coordinate ring, Z is a pure one-dimensional Cohen–Macaulay complete intersection. Its fundamental cycle is [Z]=Σ_D length(O_{Z,η_D})[D]. Put m_C=length(O_{Z,η_C}). Then [Z]=m_C[C]+R, R effective with no C component. Bézout yields de=c m_C+deg R. Thus R≠0 iff de>c m_C; R=0 iff Z_red=C (unmixedness excludes isolated components). For fixed C0, c=4. Note: the projective radical identity is sqrt((F,G)^sat)=I_C; sqrt((F,G))=I_C without saturation is not the correct general homogeneous formulation.

If the generic local initial ideal J* in K[X,Y] is computed, its colength equals m_C because the Artinian local quotient has finite m-adic filtration. This gives a direct algorithmic criterion once a certified standard basis has been computed. Merely computing (in F,in G) can undercount m_C.

## Differential and wedge distinctions

At a point p of the smooth curve C, the first conormal symbol dF(p) is the ambient differential of F (with its natural O(d) twist). Thus dF(p)=0 if and only if V(F) is singular at p; dF|_C identically zero means F has order at least two along C and V(F) is singular along C. The same applies to G. These pointwise statements must be distinguished from nonzero generic first symbols.

If dF(p) and dG(p) are both nonzero, their wedge vanishes at p exactly when the two smooth hypersurfaces have the same tangent plane there. At the generic point of C, if both first symbols are nonzero and proportional, the generic transverse intersection length m_C is greater than one. This is a tangency/multiplicity conclusion, NOT a residual-curve conclusion. When one differential vanishes, wedge vanishing is automatic and does not establish tangency of two smooth surfaces.

Indeed, over k[[t,x,y]], with C=(x,y), F=x and G=x+y^4, both differentials restrict to the same nonzero dx along C, but (F,G)=(x,y^4) has only C as reduced support and generic transverse length four. Compare F=x, G=x+y(y-t^4), where (F,G)=(x,y(y-t^4)): C has generic transverse length one and the distinct residual curve (x,y-t^4) meets C with intersection/contact order four at t=0 inside F=0. The two models have proportional nonzero differentials at t=0, but different generic behavior; in the second model the differentials are not proportional at the generic point of C.

Consequently the wedge by itself cannot distinguish generic thickness from a residual component tangent at a special point. For the projective quartic, a residual curve is present exactly when de>4m_C, as proved above. Additional global constraints on proportional nonzero first jets may restrict m_C, but no such general obstruction is established here.

Characteristic benchmark: for F=x1^4-x0^3x3, G=x2^4-x0x3^3, on x0=1 use t=x1,u=x2-t³,v=x3-t⁴. Then J=(v,(t³+u)^4-t¹²). Characteristic zero gives m_C=1 and residual degree 12; characteristic two gives m_C=4 and residual degree zero. No common surface component: F is irreducible (linear in x3 with coefficient -x0³ and x1⁴ coprime), and F does not divide G (its restriction to F has nonzero polynomial u^4 term). Thus the criterion proves the characteristic-two pair has reduced support C globally and the characteristic-zero pair does not.

Follow-up: investigate upper bounds on m_C from global proportional first-jet data, including divisor of common direction, poles of cancellation coefficients, and degeneration of higher relations. The proposition alone is an exact test, not a uniform degree exclusion.
