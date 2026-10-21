# Independent audit of the persistent Z4 arithmetic class (2026-10-21)

**Verdict B, with a scope correction.** The rank-two leading variation and nonzero one-dimensional quotient are correct for the fixed *marked integral embedded deformation problem*. The report's assertion that the differential is automatically canonical from the polynomial expression alone was insufficiently justified. The construction below uses a relative Ext module and its canonical reduction, not comparisons of arbitrarily trivialized integral kernels. The Laurent computations remain dependent on the marked charts. No divided-Frobenius interpretation follows.

## Sources and status

Read AGENTS.md, INDEX.md, STATE.md, FRONTIER.md; the proposal on `research/z4-persistent-arithmetic-obstruction-2026-10-21`; the corrected intrinsic ribbon/triple audit on `research/intrinsic-ribbon-triple-audit-2026-10-21`; the coordinate-summand counterexample on `research/z4-divided-frobenius-2026-10-21`; and the October 20 main lifting, local-structure and independent-audit notes. This is an independent check of the new *variation* claim, relying on the already audited full integral cocycle for its input; it does not independently reconstruct that full cocycle from rational chart division.

## Correct relative construction

Let R=Z_(2), C=P1_R, E=I/I², L=O(-6). The space of surjections E→L is the open locus U in the affine R-space Hom(E,L), and its kernel M is a line bundle on C×U. Over C×U the canonical construction
`0→L²→J₂/(IJ₂+I³)→M→0`
defines a relative extension. Its obstruction section belongs to the relative sheaf `H=R¹π_*(M^∨⊗L²)`. The degree of M on every fiber is -8; on P1 over a base, a degree -8 line bundle may differ from O(-8) by pullback of a base line bundle. Thus H is a locally free rank-three bundle, not *a priori* a fixed copy of A=H¹(O(-4)). Cohomology and base change hold here because H⁰(O(-4))=0 and H¹ has constant dimension three. Over the special quotient, H_k canonically identifies with Ext¹(M_k,L_k²), without choosing an integral trivialization.

Restrict to the congruence neighborhood of the fixed special quotient. The already audited integral cocycle proves the relative obstruction is zero modulo 2 and has coefficients divisible by 2 for all integral lifts; the same polynomial identities hold universally over the mod-4 first-order parameter ring. Consequently its reduction modulo 4 belongs to `2H/4H`. Because H is locally free over the unramified base, multiplication by 2 canonically identifies `H/2H` with `2H/4H`. This gives a *leading* section λ over the first-order congruence space. The special-fiber identifications of H are canonical: changing a lift of a frame by 1+2r acts trivially on λ modulo 2. The same observation handles changes of the integral kernel identification. One must not compare integral Ext classes in distinct fibers before this reduction.

The first-order congruence fiber modulo 4 is a torsor under Hom(E_k,L_k); dividing by quotient-frame scalars reducing to 1 gives tangent `T=H⁰(Hom(M_k,L_k))=H⁰(O(2))`. The tangent identification follows from the exact sequence `0→Hom(L_k,L_k)→Hom(E_k,L_k)→Hom(M_k,L_k)→0` on global sections: the connecting obstruction lies in H¹(O)=0. A base point q0 is used to identify the torsor with T. The affine-linear λ has canonical difference map `D:T→H¹(Hom(M_k,L_k²))`; it is independent of q0 because the difference is linear. This is the differential of the *divided first-order obstruction section*, not the ordinary differential of the undivided obstruction at the special point. Its construction is natural for automorphisms of the entire marked integral embedded problem. It is not asserted invariant under arbitrary automorphisms of an unmarked P1.

## Exhaustiveness and surjectivity

The raw conormal transition from the audited main report yields exactly
`p=a+bu+3hu², q=d+2hu, P=3ac²+(3b-4d)c+h, Q=2ac+2b-3d`.
Higher coefficients vanish because the two linear relations have unit determinant. Reduction to the prescribed special quotient gives a,b,h∈2R, d∈1+2R. On the special fiber (p,q)=(0,1), so the quotient is surjective everywhere on C_k. Its cokernel is coherent on the proper R-curve; if nonzero, its closed support would meet the special fiber (properness over the local base), a contradiction. Therefore **every** such integral parameter choice is surjective. This proof does not assume q=d+2hu is a unit in R[u]. The scalar direction δ is gauge, leaving α,β,γ as the three tangent coordinates.

## Exact coefficient and rank audit

From the audited full cocycle, the obstruction is represented in H¹(O(-4)) by C1[u^-1]+C2[u^-2]+C3[u^-3], with
`C1=h(ah+3b²-5bd+3d²)`,
`C2=(b-d)(4ah+3b²-8bd+6d²)`,
`C3=a(ah+9b²-23bd+15d²)`.
Independent exact polynomial arithmetic after a=2α,b=2β,h=2γ,d=1+2δ gives `(C1,C2,C3)=(2γ,2,2α) mod 4`. Every coefficient of the three differences is divisible by four. Thus
`λ(α,β,γ)=γ[u^-1]+[u^-2]+α[u^-3]`,
`D(α,β,γ)=γ[u^-1]+α[u^-3]`.
All four (α,γ) pairs occur among actual integral surjections, for example b=0,d=1 and a,h∈{0,2}. Rank(D)=2, ker(D)=k·β, and V=im(D) is two-dimensional. The image of λ in the one-dimensional coker(D) is nonzero. This proves the claimed *relative* persistence; it is not an invariant of Z4 with the integral ambient embedding forgotten.

## Serre duality

With the usual residue convention, [u^-1],[u^-2],[u^-3] pair respectively with 1,u,u² in H⁰(O(2)). Hence `V^⊥=k·u=k·st` and the pairing of the persistent class with st is 1. The intrinsic object is the annihilator line of D, not a preferred monomial on an abstract unmarked P1.

## Coordinate stress and limitation

For an adapted normal pair (x,y), a primitive triple locally has ideal `(x-a y²,y³)`. Under a genuinely nonlinear adapted change `x'=x+C y²+Axy`, `y'=y+D y²+Bx` with coefficients allowed to depend on the moving base coordinate, direct substitution modulo y³ yields `a'=a+C` (for unit linear diagonal), so for two local splittings `a'-b'=a-b`. Under arbitrary diagonal linear factors α,δ the difference becomes `(α/δ²)(a-b)`. This is an explicit second-order test involving quadratic corrections and moving-base coefficients; it verifies transformation of the *full extension cocycle* at fixed q, rather than an isolated quadratic term. A base change `v'=v+e(v)y` changes a coefficient a(v) only by a term proportional to y, hence has no effect on a(v)y² modulo y³. For arbitrary linear mixing of the kernel into the quotient, the corrected intrinsic-extension audit supplies the general affine transformation law. Functoriality of the relative extension and its divided first-order section then transports D and its cokernel.

**Verification boundary:** this report has not independently re-expanded the full three-coefficient Laurent cocycle after a second nonlinear *global* chart change. The explicit local stress test plus the intrinsic functorial construction establishes coordinate independence of the Yoneda extension and of its relative leading differential, provided the relative base-change identifications above apply. The stronger demand for a separate global symbolic re-expansion remains an optional independent computational check, not an assumed calculation.

The divided-fourth-power identity `((x+y)^4-x^4-y^4)/2 ≡ x²y² mod 2` does not supply a canonical operation into coker(D). No divided-Frobenius identification is proved.

## Recommendation

The rank-two persistent *marked relative* class can be accepted subject to independent review of this report and the inherited full-cocycle computation. Do not promote the proposed unqualified phrase “canonical cokernel of the linearized Yoneda obstruction” without specifying the **divided first-order** differential and the fixed integral embedded problem. Do not modify canonical records on this branch.
