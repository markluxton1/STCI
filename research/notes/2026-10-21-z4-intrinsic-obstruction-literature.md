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
