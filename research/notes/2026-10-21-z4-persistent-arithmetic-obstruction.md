# Investigation 3: persistent leading arithmetic obstruction for the prescribed Z4

Date: 2026-10-21. **Status: new research proposal; requires independent audit; not canonical promotion.**
Branch: `research/z4-persistent-arithmetic-obstruction-2026-10-21`.
Scope: fixed embedded relative rational quartic over R=Z_(2), fixed special conormal quotient, and the full family of integral quotients lifting it. No general STCI conclusion.

## Verdict: B (relative to the fixed embedded deformation problem)

The variation subspace of the leading Yoneda obstruction is intrinsically the image of the first-order variation map and has dimension two. Its cokernel is one-dimensional and the persistent class is nonzero. This **does not** establish a canonical divided-Frobenius realization. In particular the distinguished middle Laurent coefficient is a *calculation* of the intrinsic quotient, not its definition.

### Source and authority

Read AGENTS.md, research/INDEX.md, research/STATE.md, research/FRONTIER.md; corrected independent Yoneda audit at `research/intrinsic-ribbon-triple-audit-2026-10-21:research/notes/2026-10-21-intrinsic-ribbon-triple-independent-audit.md`; counterexample at `research/z4-divided-frobenius-2026-10-21:research/notes/2026-10-21-z4-coordinate-invariance-counterexample.md`; and the five 2026-10-20 Z4 reports on main. The quartic cocycle formula and its identification with the canonical Yoneda extension are imported from the independently audited sources; the mod-4 reduction and variation/cokernel conclusions are checked here. The earlier normal-coordinate summand is explicitly *not* invariant.

## 1. Exact family of admissible quotients

Let E=I/I², L=O(-6), M=O(-8), and fix the reduction \bar q:E_k -> L_k of the distinguished quotient. Define Q as the set of surjections q:E_R -> L_R whose reduction equals \bar q, **modulo automorphisms of L_R reducing to the identity**. The last quotient only removes scalar presentation gauge; keeping framed quotients instead gives the same obstruction and variation.

Using the audited U/V conormal transition, every homomorphism E -> L has exactly the form
```
p=a+bu+3hu², q=d+2hu;
P=3ac²+(3b-4d)c+h, Q=2ac+2b-3d
```
with a,b,h,d in R. Fixing the reduction imposes a,b,h in 2R and d in 1+2R. **Every such choice is surjective**: on U, q=d+2hu reduces to 1; on V, Q=2ac+2b-3d reduces to 1 in F2[c]. A cokernel of a map of finite locally free sheaves supported away from the closed fiber on the proper R-curve is empty (equivalently, on these two affine charts one of the two displayed components is a unit, since d is odd and 2h is even, and Q has odd constant and even other coefficients). Thus no extra realizability constraint occurs.

More precisely the displayed U component q=d+2hu is a unit in R[u] **only when h=0**; surjectivity is instead by the pair (p,q) and the properness/closed-fiber argument above, not by claiming q is a unit in the polynomial ring. This distinction matters.

The parameter space of framed lifts is the congruence fiber in the rank-four R-module Hom(E,L); after quotienting by scalar units 1+2R it is a formal neighborhood of the distinguished point in the open scheme of quotients. Its mod-4 first-order tangent space is
T = H⁰(C_k,Hom(M_k,L_k)) = H⁰(P¹_k,O(2)), dimension 3.
Indeed the four parameters (α,β,γ,δ) modulo 2 have the scalar direction δ, leaving (α,β,γ). The special-fiber quotient is fixed and the variation is first-order over R/4; no assertion is made that the whole integral congruence fiber is a vector space.

## 2. The intrinsic variation map

For each q in Q, let J₂(q)=ker(I -> E -> L), K(q)=I J₂(q)+I³ and
E_q=J₂(q)/K(q). The corrected audit proves a canonical extension
0 -> L² -> E_q -> M -> 0
and its class o(q) in A=Ext¹(M,L²)=H¹(O(-4)).
The fixed special quotient supplies fixed special L_k and M_k, so all classes reduce into the same A_k=A/2A. The audited calculation gives o(q) in 2A for every q in Q. Define λ(q)=(o(q)/2) mod 2.

For t in T choose any lift q_t congruent to q₀+2t modulo 4 (a local choice of quotient frame is harmless). Define
D(t)=λ(q_t)-λ(q₀) in A_k.
The formula depends only on t, not on the lift modulo 4: the audited obstruction is polynomial in a,b,h,d with integral coefficients, and differences of parameters in 4R give differences in 4A. Its first-order Taylor expansion is linear because products of two 2-adic perturbations vanish modulo 4. Scalar presentation gauge acts trivially on the extension class. This gives a canonical k-linear map D:T -> A_k, with functoriality under automorphisms of the fixed embedded deformation problem. It is **not** a canonical map from an unmarked abstract P¹ without its embedded quotient.

With a=2α,b=2β,h=2γ,d=1+2δ, exact polynomial reduction yields
(C₁,C₂,C₃)=(2γ,2,2α) mod 4.
Consequently in the audited Laurent basis (u^-1,u^-2,u^-3),
λ(q)=γ[u^-1]+[u^-2]+α[u^-3],
D(α,β,γ)=γ[u^-1]+α[u^-3].
All α,γ in F2 occur for actual surjections (previous section); hence
**V=im(D)=span{[u^-1],[u^-3]}**, dim V=2.
The β-direction is the kernel of D, and δ is presentation gauge. Thus the span of all pairwise differences is exactly im(D), not merely contained in it.

The coordinate-free definition of V is im(D), not the displayed span. The canonical extension, reduction and first-order difference construction commute with isomorphisms of (X_R,C_R,\bar q) preserving the specified integral deformation problem; therefore such isomorphisms transport V and the quotient class. Changing adapted normal coordinates, including quadratic corrections and moving-base terms, changes representatives and local splittings but not Yoneda classes. The counterexample for A'=A+B shows why a singled-out quadratic contribution cannot replace the full extension.

## 3. Persistent class and dual interpretation

Define \bar λ to be the common image of λ(q) in A_k/V. This is independent of q because all differences lie in V. Since dim A_k=3 and dim V=2, dim(A_k/V)=1. The displayed calculation gives \bar λ equal to the nonzero image of [u^-2]. Therefore no admissible integral quotient admits an embedded primitive triple: its Yoneda class has nonzero leading component.

By Serre duality A_k^∨=H⁰(P¹_k,O(2)). The annihilator V^⊥ is an **intrinsically defined line**, namely ker(D^∨). In the standard u=s/t chart, residue pairing identifies [u^-1],[u^-2],[u^-3] with the coefficient functionals on 1,u,u², respectively. Thus V^⊥ is spanned by u, i.e. the homogeneous quadratic st. This is a **geometric characterization relative to the embedded deformation problem**: the line is the annihilator of its obstruction variation, not an arbitrary declaration that the monomial st is canonical on an unmarked P¹. The pairing of λ with any nonzero element of V^⊥ is nonzero (over F2 it equals 1 with the indicated normalization). There is no claimed absolute preferred generator under all automorphisms of an unmarked curve.

This is also the cokernel of the linearized Yoneda obstruction map. Its interpretation needs no new noncanonical splitting of the reduced extension.

## 4. Divided fourth powers: boundary of the theorem

D₄(a,b)=((a+b)^4-a^4-b^4)/2 = 2a³b+3a²b²+2ab³, so D₄ mod 2=a²b². This is a natural polynomial cross-effect for *specified elements* a,b of an integral algebra; it is not additive in each input and does not by itself define a sheaf-linear morphism into Ext¹(M,L²). In particular replacing adapted normal coordinates by A'=A+B changes an isolated quadratic contribution by 9[u^-1], nonzero modulo 2, while the total Yoneda class is fixed (source counterexample). This variation lies in V for this example, but that coincidence **does not prove** that arbitrary divided-power coordinate defects land in V or that D₄ descends to A_k/V.

No canonical natural transformation from the filtered quadratic neighborhood or a PD/Frobenius-lift structure to A_k/V is constructed here. Additional choices would at minimum require a functorial way to evaluate the fourth-power cross-effect on the embedded conormal filtration and a proof that all coordinate/gauge defects map into V. Consequently the arithmetic leading class and its persistence are proved, while a divided-Frobenius identification remains unproved.

## 5. Reproducibility and scope

Run `python3 research/computations/verify_z4_persistent_obstruction_2026_10_21.py` (SymPy) for exact coefficient identities and linear rank. The script checks polynomial identities, not the source geometric conormal parameterization or the general Yoneda theorem; those are proved in the cited audits. Example actual lifts: (a,b,h,d)=(0,0,0,1), (2,0,0,1), (0,0,2,1), (2,0,2,1), yielding divided coordinates (0,1,0),(0,1,1),(1,1,0),(1,1,1).

**Investigation 4 handoff (no investigation performed):** for a proposed p^r analog first establish a flat integral embedding and a fixed special quotient, compute its canonical Yoneda obstruction, prove divisibility by p in a p-torsion-free Ext group, identify the actual mod-p quotient-deformation tangent and the image of its leading obstruction differential, and only then test whether divided p-power cross-effects descend to the intrinsic cokernel. The p=2 quartic result alone proves no general p^r statement.
