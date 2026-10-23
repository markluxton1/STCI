# Higher initial ideals and transverse valuations — provisional research note (2026-10-21)

Status: PROPOSAL; no independent review. Branch only; no canonical promotion.

## Setup
Let I be the homogeneous ideal of C0 in S and J=(F,G). The global gr_I(S)=⊕ I^n/I^{n+1} has two gradings: homogeneous polynomial degree and filtration degree. Its sheafification along C0 is Sym(I_C/I_C²), but global sections of the latter need not be obtained from individual global graded pieces without saturation. At η_C, completion gives K[[x,y]] with K=k(C0), and gr_m=K[X,Y]. The full initial ideal in_m(JR) includes leading forms of every combination AF+BG; it is generally larger than (in F,in G). Generic localization can lose special-point torsion/degeneration.

## Coprime theorem
If in(F)=F_r and in(G)=G_s are relatively prime, they are a homogeneous regular sequence; the filtered Koszul argument gives gr(R/J)=K[X,Y]/(F_r,G_s), and length(R/J)=rs. In an STCI with no residual components, Bézout gives de=4 length(R/J), hence de=4rs in this case.

## Explicit cancellation examples
(1,1): F=x, G=x+y^n, n>=2. The full initial ideal is (X,Y^n), length n, whereas the individual initials generate only (X).
(2,2): F=x², G=x²+y³. Cancellation gives J=(x²,y³), initial ideal (X²,Y³), length 6, rather than 4.
(2,3): F=x², G=x³+y^5. Cancellation by xF gives J=(x²,y^5), initial ideal (X²,Y^5), length 10 rather than 6.
These are local transverse models, not global STCI constructions.

## Quartic benchmark, local chart x0=1
Put t=x1, u=x2-t³, v=x3-t⁴. Then C is u=v=0. For F=x1⁴-x0³x3, G=x2⁴-x0 x3³:
F=-v.
G=(t³+u)^4-(t⁴+v)^3.
Modulo F, G reduces to (t³+u)^4-t¹².
At generic t ≠0, characteristic 0: initial G modulo F is 4t^9 u, so J=(v,u) and length 1. Characteristic 2: (t³+u)^4-t¹²=u⁴, so J=(v,u⁴), full initial ideal (V,U⁴), length 4. The individual initial forms in characteristic 2 are F_1=-V and G_1=-t^8 V (since (t⁴+v)^3 has linear term t⁸v), so cancellation is essential. In characteristic zero, G_1=4t⁹U-3t⁸V, and initial forms are coprime. Over algebraic closure of K in characteristic zero the transverse scheme is generically reduced of length one at C; other components of the (4,4) intersection must occur elsewhere, so the pair is not STCI in characteristic zero. In characteristic two it is a length-four curvilinear thickening along C at the generic point. Global radical equality requires separate projective chart/boundary verification.

## Valuations
The m-adic order is total transverse degree and is not a valuation on K itself. For each closed p in C, ord_p on K gives a discrete base valuation. Weight vectors (w_x,w_y)>0 give monomial valuations on K(x,y) with trivial base valuation; after choosing p, Gauss-type extensions v(Σ a_ij x^i y^j)=min(ord_p(a_ij)+i w_x+j w_y) give base-sensitive information, subject to coordinate choice and suitable completion. Composite lexicographic valuations retain transverse order and then coefficient order. Newton polygons/infinitely near points resolve common tangent factors and distinguish transverse branches; a single m-adic initial ideal generally does not encode their Puiseux exponents. Weighted initial ideals of the full ideal, not just two generators, are required. Rees valuations of J describe normalized blowup data but need not recover all infinitely near branches.

## Globalization and limitations
The degree-d normal symbol of F of I-order r is a section of Sym^r(N_C^∨)⊗O_C(d), which for the characteristic-zero balanced splitting is O_{P¹}(4d-7r)^{⊕(r+1)} (O_C(1)=O_{P¹}(4)). Thus a nonzero symbol requires 4d-7r>=0; similarly 4e-7s>=0. This is a necessary degree constraint, not a new STCI exclusion. The local (x,y) coordinates are only rational frames of the conormal bundle: rational cancellation coefficients generally have poles at closed points and do not produce ambient global polynomial combinations. Clear denominators only after tracking the induced twists and possible extra zero divisors. In characteristic two do not use the characteristic-zero normal-bundle splitting.

Related notes: [residual-cycle and wedge distinctions](2026-10-21-residual-cycle-proposition-audit.md); [special-fiber length and standard bases](2026-10-21-valuative-standard-basis-criterion.md); [orders, Hilbert filtration, and duality](2026-10-21-equality-orders-filtration-duality.md).

## Priorities
1. Compute a standard basis of the actual generic ideal for arbitrary candidate F,G and retain each cancellation certificate.
2. Track denominators of certificates at closed points and formulate sheaf-valued graded relations with saturation.
3. Compare base-sensitive weighted valuations at each exceptional point with global degree constraints.
4. Seek a numerical exclusion for nonsaturated relations and both orders >=2; no such exclusion is proved here.

This note does not claim the generic local data determine global radical equality or that the example proves a characteristic-zero impossibility theorem.
