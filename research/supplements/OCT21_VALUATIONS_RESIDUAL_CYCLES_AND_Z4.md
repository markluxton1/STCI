# Historical mathematical investigations

Complete source texts below, retaining mathematical arguments, hypotheses, counterexamples, corrections and unresolved cases. No new independent audit or theorem promotion.

---

## Source: 2026-10-21-remote-branch-consolidation.md

# Remote branch consolidation — 2026-10-21

This is a provenance and integration record, **not a theorem promotion**.

Starting from main at d4ff9130fe8692c5ba1769041719ffb7d7bba4be, this integration adds the files genuinely absent from main:

- research/z4-characteristic-zero-lift-2026-10-20 (ac22fe2f17b9f8ef8cd286bdcd85e20b422e6fb4): 15 new files.
- research/conditional-2-12-2026-10-21 (6a729aa5adc15a0145150a321586583ca254dc77): 110 new files.
- archive/codex-5hr-interrupted (2e53a7b5e9d4c96b5741ee4a4746a4a9ff0ad647): 0 new files; its historical file paths are already present on main. The older archive branch's modifications to shared reports were deliberately not applied over later versions.

In total this commit adds 125 source artifacts plus this provenance note. The original compare-against-main endpoint reports branch additions relative to each branch's historical merge base; a direct comparison of the full main and integration Git trees establishes the actual 126 added paths and zero modified existing paths. Older branch versions of research/INDEX.md and research/computations/README.md were not substituted for current main. All source branches are retained.

The Z4 obstruction concerns the **prescribed** characteristic-two quadruple and its unramified 2-adic/integral lift, not every characteristic-zero thickening or unrestricted STCI. Its source report describes independent review but is not a promoted result record. The conditional (2,12) investigations retain their actual-pair assumptions and unresolved global realization/nonnormal-strict-sextic questions. Historical archive material remains archival evidence, not current theorem authority.

Before any promotion, consult AGENTS.md, research/AUTHORITY.md, the original reports and audits, and the canonical result-record review process. This integration records source artifacts without asserting that the original computational checks were rerun.


---

## Source: 2026-10-21-residual-cycle-proposition-audit.md

# Residual-cycle criterion and wedge degeneracy — proof audit proposal

**Status:** Residual-cycle identity follows from standard intersection theory; the proposed global wedge obstruction remains open. This note has not received an independent audit.

**Scope:** Arbitrary characteristic. Let \(C\subset\mathbf P^3\) be an integral curve of degree \(c\), and let \(F,G\) be homogeneous forms of degrees \(d,e\) with no common surface component, both vanishing on \(C\).

The degree identity below is the elementary Bézout cycle identity for a proper complete intersection; it does **not** depend on [STCI-R-0019](../results/quasiprimitive_residual_cycles.md). R0019 is a separate, stronger *conditional* statement about residual zero-cycles on an auxiliary smooth surface, requiring finite-flat curvilinearity, a saturated invertible flag, and proper residual intersection.

## 1. Exact residual-cycle criterion

Put \(Z=V_+(F,G)\). Since \((F,G)\) is a regular sequence, \(Z\) is a pure one-dimensional Cohen–Macaulay complete intersection. Write

$$
[Z]=m_C[C]+R,\qquad
m_C=\operatorname{length}(\mathcal O_{Z,\eta_C}),
$$

where \(R\) is an effective cycle without \(C\) as a component. Bézout gives

$$
\boxed{de=c\,m_C+\deg R.}
$$

Consequently \(R=0\) if and only if \(Z_{\mathrm{red}}=C\): purity excludes isolated components. For the fixed rational quartic, \(c=4\), so

$$
\boxed{\deg R=de-4m_C.}
$$

For projective homogeneous ideals, the appropriate statement is \(\sqrt{(F,G)^{\mathrm{sat}}}=I_C\); do not silently replace this with an unsaturated radical equality.

If the full initial ideal of the generic local ideal \(J=(F,G)\) in \(k(C)[[x,y]]\) is known, its colength computes \(m_C\). Initial forms of the two generators alone need not generate this full initial ideal: cancellation and standard-basis completion can be essential.

## 2. What the wedge actually says

**Pointwise singularity.** At \(p\in C\), the differential of \(F\) is naturally a twisted conormal vector:

$$
dF(p)\in N_{C/\mathbf P^3,p}^{\vee}\otimes\mathcal O_C(d)_p.
$$

Because \(F|_C=0\), this is the entire ambient differential restricted to \(C\). The hypersurface Jacobian criterion therefore gives

$$
\boxed{dF(p)=0\quad\Longleftrightarrow\quad V(F)\text{ is singular at }p.}
$$

If \(dF|_C\equiv0\), then \(F\) vanishes to order at least two along \(C\), and \(V(F)\) is singular at every point of \(C\). The same applies to \(G\).

**Tangency of two smooth surfaces.** If both differentials are nonzero at \(p\), then

$$
\boxed{
dF(p)\wedge dG(p)=0
\quad\Longleftrightarrow\quad
T_pV(F)=T_pV(G).
}
$$

This is different from wedge vanishing because one differential is zero: that case is a singularity of at least one surface, not tangency between two smooth surfaces.

If the two first normal symbols are nonzero and proportional **at the generic point of \(C\)**, then the generic transverse intersection multiplicity satisfies \(m_C>1\). But this does **not** by itself force a residual component.

## 3. Two local models: thickness versus residual contact

Work over \(k[[t,x,y]]\) with \(C=V(x,y)\). The coordinate \(t\) runs along \(C\).

**Model A — only a thickened \(C\).**

$$
F=x,\qquad G=x+y^4,\qquad (F,G)=(x,y^4).
$$

Both differentials are the same nonzero vector along the whole curve:

$$
dF|_C=dG|_C=dx\ne0.
$$

Their wedge vanishes identically, yet the reduced support is only \(C\) and \(m_C=4\). There is no residual curve.

**Model B — a separate curve tangent at one point.**

$$
F=x,\qquad G=x+y(y-t^4),\qquad
(F,G)=(x,y(y-t^4)).
$$

Here the reduced intersection has two components,

$$
C=V(x,y),\qquad D=V(x,y-t^4).
$$

They meet at \(t=0\) with contact/intersection order four **inside the smooth surface** \(V(x)\). At \(t=0\), the two hypersurface differentials are both \(dx\), so their wedge vanishes there. But at the generic point of \(C\),

$$
dG|_C=dx-t^4dy,
$$

which is independent of \(dF|_C=dx\), and \(m_C=1\).

**Conclusion:** These models distinguish generic transverse thickness from residual-component contact at a special point. Wedge vanishing, even with both differentials nonzero, does not by itself tell us which phenomenon occurs. For the projective quartic the exact residual test is \(de>4m_C\).

## 4. Characteristic-zero versus characteristic-two benchmark

For

$$
F=x_1^4-x_0^3x_3,\qquad
G=x_2^4-x_0x_3^3,
$$

on the chart \(x_0=1\), put

$$
t=x_1,\qquad u=x_2-t^3,\qquad v=x_3-t^4.
$$

Then

$$
(F,G)=\bigl(v,(t^3+u)^4-t^{12}\bigr).
$$

In characteristic zero, \(m_C=1\), so the residual degree is \(16-4=12\). In characteristic two, \(m_C=4\), so the residual degree is zero. The two forms have no common surface factor: \(F\) is irreducible and does not divide \(G\). Thus the criterion establishes that the characteristic-two intersection has reduced support exactly \(C\), whereas the characteristic-zero intersection does not.

## 5. Open global question

When two integral surfaces containing \(C\) have **nonzero proportional first conormal symbols**, can global constraints on their degrees, on the divisor of the common normal direction, or on poles in higher cancellation relations force \(de>4m_C\)?

This is an investigation, not an established theorem. In particular, neither pointwise tangency nor generic proportionality alone implies a residual curve.


---

## Source: 2026-10-21-valuative-standard-basis-criterion.md

# Valuative standard-basis test — audited local criterion

**Status:** Local algebra criterion checked on 2026-10-23; working research note, not independently promoted to a canonical result. The standard-basis and valuation program remains exploratory.

## Setup and definitions

Let \(p\) be a closed point of a smooth curve \(C\), and work in completed local coordinates

$$
B=k[[t]],\qquad R=B[[x,y]],\qquad J=(F,G)\subset(x,y),
$$

where \(F,G\) form an \(R\)-regular sequence and \(C=V(x,y)\). Write \(A=R/J\). Define the **generic transverse length along \(C\)** by

$$
m_C=\operatorname{length}_{K[[x,y]]}
\bigl(K[[x,y]]/(F,G)\bigr),\qquad K=k((t)),
$$

where the coefficients are extended to \(K[[x,y]]\) via the generic formal neighborhood of \(C\). Define the **special transverse length** by

$$
\lambda_p=\operatorname{length}_{k[[x,y]]}
\bigl(k[[x,y]]/(F(0,x,y),G(0,x,y))\bigr),
$$

allowing \(\lambda_p=\infty\).

**Important distinction:** Define \(\rho_p=\dim_K(A\otimes_BK)\) when \(A\) is finite over \(B\). The number \(m_C\) measures only the component \(C\) at its generic point, whereas \(\rho_p\) measures the entire generic fiber and can include residual components through \(p\). The rings \(R[1/t]\) and \(K[[x,y]]\) are different: the latter is the completion of the former at its \((x,y)\)-adic maximal ideal. Thus \(m_C\) is the length of the completed local factor at \(C\), not automatically the total generic-fiber dimension.

## Criterion

Under the setup above,

$$
\boxed{\lambda_p=m_C<\infty
\quad\Longleftrightarrow\quad
V(J)\text{ has no residual reduced curve component through }p.}
$$

More precisely, if \(\lambda_p<\infty\), then

$$
\boxed{
\lambda_p=\rho_p=m_C+
\sum_{D\ne C}\operatorname{length}(\mathcal O_{V(J),\eta_D})\,
\deg(D\longrightarrow\operatorname{Spec}B),
}
$$

where the sum is over the other one-dimensional components of the formal local scheme through \(p\), and the degree is the finite generic-fiber degree over \(K\). The formula counts components after passing to the generic fiber; it does not assume they are geometrically irreducible. If \(\lambda_p=\infty\), the finite-length comparison is unavailable, and in this complete-intersection setup a residual component lies in the special fiber.

### Proof

Assume \(\lambda_p<\infty\). Since \(A/tA\) is Artinian, the formal finiteness/Weierstrass theorem (equivalently, topological Nakayama plus completeness) makes \(A\) a finite \(B\)-module. The ring \(A\) is one-dimensional Cohen–Macaulay because \(F,G\) form a regular sequence in the three-dimensional regular local ring \(R\). Since \(A/tA\) is zero-dimensional, \(t\) is a parameter and therefore a nonzerodivisor on \(A\). Thus \(A\) is finite torsion-free, hence finite free, over the DVR \(B\). It follows that

$$
\lambda_p=\dim_k(A/tA)
=\operatorname{rank}_B(A)
=\rho_p=\dim_K(A\otimes_BK).
$$

The finite generic fiber \(A\otimes_BK\) is Artinian. Its localization at the maximal ideal corresponding to \(C\), followed by completion, identifies with \(K[[x,y]]/(F,G)\); its \(K\)-dimension is \(m_C\). The other Artinian local factors correspond to residual components through \(p\) and have positive \(K\)-dimensions, incorporating residue-field degrees. This localization/completion step is essential: one must not identify \(R[1/t]\) with \(K[[x,y]]\). This gives the formula and shows that \(\lambda_p=m_C\) exactly when there is no other curve component.

If \(\lambda_p=\infty\), then \(A/tA\) has positive dimension. Since \(A\) is one-dimensional Cohen–Macaulay and has no embedded associated primes, some one-dimensional component lies in \(t=0\). It cannot be \(C\), on which \(t\) is a parameter, so it is residual. Conversely, absence of residual components means \(\sqrt J=(x,y)\) locally; then \(A\) is finite over \(B\) and the preceding argument yields \(\lambda_p=m_C\).

This is a **local** statement; it does not claim that arbitrary initial factors lift to global algebraic components without further work.

## Exact example: special-length jump

Take

$$
F=x^2,\qquad G=x^2+ty^3+y^4.
$$

Then

$$
J=(x^2,y^3(t+y)).
$$

At the generic point of \(C\), \(t+y\) is a unit in \(K[[x,y]]\), giving

$$
m_C=\operatorname{length}K[[x,y]]/(x^2,y^3)=6.
$$

At \(t=0\),

$$
\lambda_p=\operatorname{length}k[[x,y]]/(x^2,y^4)=8.
$$

The additional curve \(D=V(x,t+y)\) has generic multiplicity two (the \(x^2\) direction), so its contribution is exactly \(8-6=2\).

## Standard bases, valuations, and limitations

Compute a local standard basis of \(J\) in the generic formal neighborhood of \(C\) to obtain \(m_C\), and separately compute one in the special fiber to obtain \(\lambda_p\). The colength of each certified monomial initial ideal equals the corresponding finite length. **Do not specialize a generic standard basis naively:** leading coefficients may vanish at \(t=0\), changing the initial ideal and its colength.

Weighted initial forms and cancellation relations, such as \(G-F=y^3(t+y)\) in the example, help expose the jump. Ordinary tropicalization of a zero-dimensional scheme supported at the origin in the torus is empty and does not retain this length information. Use local standard bases, multiplicity-sensitive weighted initial ideals, or tropical schemes instead.

For the fixed rational quartic, a global STCI pair has no residual components, hence satisfies \(\lambda_p=m_C\) at every smooth point \(p\) after passing to appropriate completed local coordinates. This is a **necessary local test**, not a new global numerical exclusion.

**Open direction:** Relate the local jumps and their valuation data to global conormal sections, poles of cancellation coefficients, and degree constraints without assuming that a factor of an initial polynomial lifts to a separate component.


---

## Source: 2026-10-21-z4-coordinate-invariance-counterexample.md

# Coordinate-invariance counterexample for the naive quadratic summand

Status: exact calculation, provisional; not independently audited or promoted.

Fix the distinguished quotient p=0,q=1,P=-4c,Q=-3, so m_V=-3A+4cB. Along X=0,Y=epsilon the quadratic coefficients are A2=-6u^-10, B2=-3u^-9, and c1=u^-4. The quadratic cocycle decomposition in the original normal coordinates is K_A=18u^-2, K_B=-12u^-2, K_move=-12u^-2, giving total K=-6u^-2.

Make the invertible integral normal-coordinate change A'=A+B, B'=B on V. Then m_V=-3A'+(4c+3)B'. The quadratic coefficient A2'=A2+B2=-6u^-10-3u^-9. Thus K_A'=18u^-2+9u^-1, K_B'=-12u^-2-9u^-1, and K_move'=-12u^-2. The total remains -6u^-2.

The difference [K_A']-[K_A]=9[u^-1] is nonzero in H^1(P1_R,O(-4))=R[u,u^-1]/(R[u]+u^-4 R[u^-1]); it even survives mod 2. Therefore the naive 'first normal coordinate' quadratic contribution does not define an intrinsic cohomology class. This disproves invariance of that decomposition, but does not disprove the existence of a more sophisticated canonical divided-Frobenius-to-obstruction construction.

Verification: direct substitution into the audited transition formulas suffices. No general nonexistence assertion about canonical divided-power operations is made.

---

## Source: 2026-10-21-z4-global-laurent-coordinate-supplement.md

# Investigation 3 supplement: global Laurent re-expansion (reported, not independently reproduced)

**Status:** user-reported independent calculation, recorded for provenance; not a new independently audited theorem or machine-checked certificate.

For the distinguished conormal quotient, the original Laurent cocycle is
\[
K=-6u^{-2}.
\]
Under the reported nonlinear adapted changes
\[
m_U'=X+(1+u)Y^2,\qquad
m_V'=(-3A+4cB)+(c+c^2)B^2/9,
\]
the re-expanded cocycle is
\[
K'=1+u-6u^{-2}+u^{-5}+u^{-6}.
\]
Consequently,
\[
K'-K=(1+u)+u^{-4}(u^{-1}+u^{-2}),
\]
an explicit Čech coboundary in the stated Laurent trivializations, so the two cocycles represent the same class.

**Verification boundary:** This calculation was reported after the independent audit branch was committed. No standalone calculation script or full derivation was supplied for this supplement. It tests one nontrivial global change, not the general coordinate-invariance theorem, which relies on the relative-Ext construction in the independent audit.


---

## Source: 2026-10-21-z4-intrinsic-obstruction-literature.md

# Intrinsic embedded ribbon-to-triple obstruction: focused literature assessment (2026-10-21)

Status: literature-based research proposal; not an independently audited new theorem; no canonical promotion.

## Verdict

The appropriate framework is the *embedded lifting of a conormal quotient through the quadratic normal neighborhood*, with Illusie's cotangent-complex theory supplying the functorial conceptual interpretation. Drézet's abstract primitive multiple curve extension theory is related but does **not** directly calculate this embedded obstruction. No verified source identifies this particular class with divided Frobenius.

## Repository scope and evidence

Read AGENTS.md and the five 2026-10-20 Z4 reports on main, and the coordinate-invariance counterexample on research/z4-divided-frobenius-2026-10-21. The audited but unpromoted result establishes nonlifting over Z_(2) and Z_2 for the prescribed Z4 with generic support C. For the canonical ribbon, N^* -> L=O(-6) has kernel M=O(-8). Its necessary embedded triple obstruction is in H^1(Hom(M,L^2))=H^1(O(-4)); the distinguished quotient gives -6[u^-2] and every admissible quotient has middle coefficient 2 mod 4. The coordinate counterexample changes one purported summand by 9[u^-1] while leaving the total class unchanged. Thus only the full quadratic defect should be assigned invariant meaning.

## Literature map

1. Bayer–Eisenbud, *Ribbons and their canonical embeddings*, Trans. AMS 347 (1995), 719–756, https://eisenbud.github.io/papers/index.html . The paper treats abstract ribbons, restricted cotangent sequences, gluing and embeddings. It is the correct ribbon background, not a theorem equating embedded triple obstruction with divided Frobenius. Precise theorem numbering for the claimed specialization has not been verified.
2. J.-M. Drézet, *Paramétrisation des courbes multiples primitives*, Adv. Geom. 7 (2007), https://arxiv.org/abs/math/0605726 ; and *Primitive multiple schemes*, https://arxiv.org/abs/2004.04921 . These construct primitive multiplicity-n objects via nonabelian transition automorphisms; extension obstruction for abstract primitive schemes appears in H^2 of a suitable vector bundle. These complex-base statements cannot be applied over Z_(2) without checking a relative extension of the proofs. On a curve abstract H^2 vanishes, but the fixed-ambient embedded compatibility may still obstruct in H^1.
3. Illusie, *Complexe cotangent et déformations*, LNM 239 (1971), and LNM 283 (1972). Modern precise reference: Stacks Project, Tag 08SM, Section 92.16, https://stacks.math.columbia.edu/tag/08SM ; and Tag 08S3, Section 91.2, https://stacks.math.columbia.edu/tag/08S3 . The cotangent complex controls lifting ring maps and square-zero extensions through Ext groups; the exact embedded quotient obstruction target below is a specialized reduction, not a direct quotation from a general Illusie theorem.
4. Deligne–Illusie and subsequent Frobenius-lifting theory distinguish lifting a scheme to W2 from lifting its Frobenius. A Frobenius-lifting obstruction is generally in an Ext^1 group involving Frobenius-pulled differentials; scheme lifting can involve Ext^2. See discussion and references in https://www.sciencedirect.com/science/article/abs/pii/S0022404924001804 . Neither is identified in the cited work with the Z4 embedded class.

## Candidate intrinsic construction (to be proved, not cited as an established theorem)

Let i:C_R -> P^3_R be the regular immersion, I its ideal, E=I/I^2, and Q=I/I^3. The multiplication gives the canonical exact sequence
0 -> Sym^2 E -> Q -> E -> 0
as sheaves of modules on the underlying topological space, with caution: Q is naturally an O_{P^3}/I^3-module, and an O_C-module structure or splitting is NOT canonical. Thus formulate the lifting problem in the category of filtered sheaves/algebras over the full second neighborhood, not by assuming Q is canonically an O_C-module.

Fix a surjection q:E -> L with kernel M. On affine cover U_i choose embedded primitive triples reducing to the specified ribbon and compatible with q. Compare their local quadratic kernel equations on overlaps using the full transition of O_{P^3}/I^3, including the nilpotent displacement of base coordinates. Their differences give a Cech 1-cocycle valued in Hom(M,L^2) provided the torsor and gauge-action assertions below hold. Local quadratic corrections give coboundaries. The class is independent of frames and normal coordinates because the *full* filtered algebra and embedding are transported. This is a proposed explicit intrinsic implementation, not yet a proved universal natural transformation.

For the quartic the Cech quotient is R[u,u^-1]/(R[u]+u^-4 R[u^-1]); its basis is [u^-1],[u^-2],[u^-3]. The audited calculation yields K and -6[u^-2] for the distinguished quotient. The moving-base term is indispensable.

## Arithmetic assessment

D_{p^r}(a,b)=((a+b)^{p^r}-a^{p^r}-b^{p^r})/p is an integral polynomial. For 0<j<p^r, v_p(binomial(p^r,j))=r-v_p(j). These identities measure integral failure of additivity of p-power maps, but alone give no morphism to H^1(Hom(M,L^2)). They do not imply that the first valuation-one coefficient is the first global embedded obstruction. The numerical coincidence -6 = -binomial(4,2) is suggestive, not a coordinate-independent theorem; the known coordinate counterexample disproves the naive summand interpretation.

## Exact gap / next investigation

Prove the following conditional proposition over R=Z_(2), or find a counterexample: for the fixed regular immersion C_R in P^3_R and any admissible surjection E -> L reducing to the specified ribbon, the groupoid of locally embedded primitive triples extending that ribbon, with fixed first-order quotient, is locally nonempty and its descent differences form a torsor under Hom(M,L^2). Show that its Cech obstruction is canonical under all automorphisms of the complete quadratic neighborhood, and in the audited raw coordinates equals [K]. Determine whether there is a natural divided-power/Frobenius-defect construction into that torsor, and if so prove its image has middle Laurent coordinate 2 mod 4 for all admissible quotients. If not, report the failure precisely.

Caveat: an intrinsic obstruction may depend on the full quadratic neighborhood and the chosen lifted quotient; it need not be an invariant of the abstract ribbon alone. No claim is made for arbitrary ramified DVRs or the unrestricted characteristic-zero STCI problem.

## Bibliographic verification boundary

The references and section-level Stacks tags above were verified through searchable sources. Exact theorem numbers for Bayer–Eisenbud, Drézet and original Illusie volumes were not independently verified and should not be fabricated. This report is a focused, provisional literature handoff rather than a primary-source-complete audit.


---

## Source: 2026-10-21-z4-persistent-independent-audit.md

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
