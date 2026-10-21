# Independent audit: intrinsic embedded ribbon-to-triple obstruction (2026-10-21)

Status: **independent mathematical audit; verdict B (correct after replacing the flawed difference argument by a canonical module extension)**. Research branch only; no canonical promotion.

## Scope and source provenance

Read `AGENTS.md`, `research/INDEX.md`, `research/AUTHORITY.md`, `research/CONTRIBUTING_AGENT.md`, the provisional theorem on `research/intrinsic-ribbon-triple-2026-10-21`, the literature report on `research/z4-intrinsic-obstruction-literature-2026-10-21`, and the five 2026-10-20 lifting reports on `main`. This audit proves the *general embedded torsor theorem* independently; it does not rerun the previously audited Laurent arithmetic. The explicit quartic coefficient is imported as an independently audited prior calculation, not a fresh computation.

## Verdict B and corrected theorem

Let `i:C -> X` be a regular immersion of codimension two of schemes, with ideal `I`, and `E=I/I²`. Fix a surjective homomorphism of locally free sheaves `q:E -> L` with `L` invertible and kernel `M` invertible. Put `J₂=ker(I -> E -> L)`, and define the **canonical ideal** `K=I J₂+I³` (indeed `I³ ⊂ I J₂`).

There is a canonical exact sequence of **O_C-modules**
```
0 -> L^⊗2 -> J₂/K -> M -> 0.                    (*)
```
The sheaf of embedded ideals `J₃` satisfying `I³ ⊂ J₃ ⊂ J₂`, with local primitive-triple normal form `(x-a y²,I³)` for generators adapted to `q`, is canonically identified with the sheaf of O_C-linear splittings of (*). It is a locally nonempty torsor under `H=Hom_O_C(M,L²)`. Its class is exactly the Yoneda extension class
```
o_X(q) = [J₂/K] ∈ Ext¹_O_C(M,L²) = H¹(C,H).
```
It vanishes exactly when a global embedded primitive triple exists. If one exists, the set of global embedded triples is a torsor under `H⁰(C,H)`.

This holds in arbitrary characteristic, including mixed-characteristic DVRs; smoothness over a DVR is sufficient but not required beyond the stated regular immersion and locally free quotient. The claim is about embedded ideals in the fixed X and the fixed quotient q, not about abstract multiple curves.

## Independent proof

1. Regular immersion gives `I²/I³ ≅ Sym²(E)`. Since `J₂` is the inverse image of `M`, `I² ⊂ J₂`, and the image of `I J₂` in `I²/I³` is precisely the image `ME` of `M ⊗ E -> Sym²(E)`. Consequently
```
(I²+K)/K = I²/(I J₂+I³) ≅ Sym²(E)/(ME) ≅ Sym²(L)=L².
```
The last isomorphism is canonical for a line quotient, with no need to invert 2. The quotient `J₂/I²=M`. These identify the kernel and cokernel of (*).

2. Since `I J₂ ⊂ K`, multiplication by `I` kills `J₂/K`. Thus (*) is genuinely an exact sequence of O_C-modules, not a spurious O_C-module structure on `I/I³`. This repairs the central gap in the provisional proof.

3. For any admissible `J₃`, `I J₃ ⊂ J₃`, `I³ ⊂ J₃`, and the local normal form implies that the image of `J₃` in `E` is `M` and its intersection with `I²` modulo `I³` is `ME`. Therefore `K ⊂ J₃` and `J₃/K -> M` is an isomorphism: its inverse is a splitting of (*).

4. Conversely, a splitting `s:M -> J₂/K` has image an O_C-submodule. Its inverse image `J₃` in `J₂` is an O_X-ideal: multiplying an element of `J₃` by a function in O_X preserves its image modulo K because the action factors through O_C, and `K` is an ideal. It contains K and hence I³, and maps onto M with quadratic intersection ME. Étale/Zariski locally choose adapted generators `x,y` of I, with x mapping to M and y to L. A splitting is generated modulo K by `x-a y²` for some local coefficient a, hence `J₃=(x-a y²,I³)`; the terms x²,xy already belong to the ideal. Since x-a y² is another regular generator of I near C, this is equivalent locally to `(x-a y²,y³)`, a primitive triple with graded pieces O_C,L,L². The construction works over any DVR without division.

5. Splittings of an exact sequence with locally free quotient M exist locally. The difference of two splittings is a unique O_C-linear map M -> L². This action is free, transitive, additive and restriction-compatible. The construction uses only intrinsic ideals and module operations.

6. On a trivializing cover choose splittings s_i and set h_ij=s_j-s_i. Then h_ij+h_jk=h_ik. Replacing s_i by s_i+t_i adds the Čech coboundary t_j-t_i. Vanishing means the splittings can be adjusted to agree and glue, and inverse images in J₂ give a global *embedded ideal*. Conversely a global ideal yields a global splitting. Standard sheaf Ext gives Ext¹(M,L²)=H¹(Hom(M,L²)) because M is locally free. There is no nonabelian obstruction at this fixed embedded stage.

## Arbitrary adapted coordinate transformations

Locally choose generators x,y of I with q(x)=0 and q(y) a frame of L. Any other adapted generators, modulo I³, have the form
```
x' = α x + A x² + B xy + C y²,
y' = β x + δ y + D x² + E xy + F y²,
```
where α and δ restrict to units on C; coefficients may be ambient functions, including dependence on moving base coordinates. Terms from nilpotent variations of these coefficients are already included in their quadratic jets. In the quotient by `(x-a y²,I³)`, x=a y², y'=δ y + O(y²), and x'=(α a+C)y². Hence
```
a' = (α a+C)/δ²
```
with all coefficients restricted to C (and the appropriate local frames). For two choices a,b in the *same original frame*,
```
a' - b' = (α/δ²)(a-b).
```
This is exactly the transition for Hom(M,L²): x' has M-frame αx, y' has L-frame δy. The affine translation C/δ² may depend on the full quadratic neighborhood and base-coordinate movement; it cancels in differences. Arbitrary linear mixing β, all x²/xy terms, and quadratic corrections to y' do not change this result. No chosen retraction of the quadratic neighborhood is used. Equality is equality of ideals, not of preferred generators.

## Functoriality, base change and dependence

Isomorphisms of embedded triples (X,C,q) carry I,J₂,K and (*) to their counterparts, hence carry the Yoneda class functorially. For a flat base change of the ambient setup, the defining ideals, conormal exact sequence and (*) pull back exactly, and the extension class pulls back naturally. For nonflat base change, the same conclusion holds **if** the regular immersion and the conormal quotient remain compatible, the relevant ideal/product/graded identifications commute with pullback, and the pulled-back sequence remains exact; it is not automatic for arbitrary base change. Natural pullback of the Ext class does not assert that the cohomology base-change map is an isomorphism. The class is determined by the embedded quadratic neighborhood O_X/I³ and q: J₂/K is computed entirely inside that truncation. It need not be determined by the associated graded algebra Sym(E) or by the abstract ribbon alone.

## Quartic consistency

For the specified relative rational quartic and distinguished quotient `L=O(-6), M=O(-8)`,
```
H = M^∨ ⊗ L² = O(-4).
```
On the two standard affine charts, H¹(O(-4)) has Laurent representatives u^-1,u^-2,u^-3. The earlier independently audited raw ambient calculation yields the transition defect `K(u)` and for the distinguished quotient `[-6u^-2]`. The current theorem proves **why** the difference of local kernel equations represents the intrinsic Yoneda extension class: each local equation defines a splitting of (*), and their normalized differences are precisely its Čech connecting cocycle. This identifies the type and intrinsic meaning of the previously audited numerical class; it is not a new re-expansion or a re-verification of the sign conventions. The earlier lifting audit establishes the middle coefficient is 2 mod 4 for all specified admissible quotients over Z_(2) and Z_2. No claim for arbitrary ramified DVRs follows.

## Explicit defect in the provisional proof

The statement that one can subtract arbitrary lifts of M *inside I/I³* as O_C-linear maps is not justified: I/I³ has no canonical O_C-module structure. Also the expression I²/(I³+IJ) is circular unless J is fixed and it does not by itself define a common comparison object for varying J. The common object is instead **J₂/(I J₂+I³)**. It is annihilated by I, so the difference construction and its additive law are literal O_C-module statements. The original numerical calculation survives; the original general proof should not be promoted verbatim.

## Audit status and handoff

**Verdict B.** The corrected embedded torsor theorem and its descent/coordinate invariance are proved above by a canonical short exact sequence. No symbolic calculation was needed for the general proof. The quartic coefficient and its universal mod-4 reduction remain imported from the five independently reviewed October 20 reports, not recomputed here. Investigation 3 may safely use the intrinsic extension class as a proved construction, subject to citing this corrected theorem and preserving the fixed-q and base hypotheses. Any identification with divided Frobenius remains unproved. Do not promote or merge this branch without separate repository review.
