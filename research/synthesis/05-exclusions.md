# 5. The exclusion results and their logical architecture

This chapter records **what is excluded** and the hypotheses and proof architecture behind those exclusions. Older arguments are mentioned only when needed to prevent an obsolete open case from being mistaken for a current one. This guide does **not** replace the underlying case proofs and independent audits.

The lower-degree exclusion is a theorem about the **fixed embedded curve** and its projective equivalents. It does not rule out higher-degree carriers; the [frontier](../FRONTIER.md) and [dependency map](DEPENDENCIES.md) identify the missing steps.

## 5.1 The precise theorem

Fix an algebraically closed field \(k\) of characteristic zero and
\[
C_0=\{[s^4:s^3t:st^3:t^4]\}\subset\mathbf P^3_k.
\]
The accepted [STCI-R-0001](../results/quartic_carrier_exclusion.md) says:

> If \(X\subset\mathbf P^3\) is **any integral quartic hypersurface** containing \(C_0\), then **no** homogeneous form \(G\) of positive degree satisfies \(V(X,G)=C_0\) set-theoretically.

The quantifiers matter: the theorem imposes **no** normality, singularity-type, mate-degree, or generic-normal-order restriction. It concerns this fixed quartic embedding (and its projective equivalents), not automatically every rational quartic embedding.

The separate [R-0022 filtered-contact proof](../results/quartic_44_filtered_exclusion.md) excludes only the degree pair (4,4) and uses accepted source-level filtration and primitive-triple inputs; it does not supply the arbitrary-mate-degree argument of R-0001. The bounded-index normal-carrier result [R-0035](../results/normal_carrier_bounded_index_exclusion.md) has its own local-index and inherited-premise restrictions.

## 5.2 How the quartic proof is assembled

The [October 11 accepted assembly](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-11-session-all-quartic-results-acceptance.md) and [independent dependency audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-11-session-all-quartic-dependency-assembly-independent-audit.md) are the authoritative pointers to the component arguments.

The proof separates integral quartic carriers into two exhaustive top-level classes:

### A. Normal integral quartics

The accepted normal-carrier exclusion is an **inherited component theorem** of the full assembly. Earlier work used the classification of normal quartic surfaces and their minimal resolutions. Rational-singularity carriers, positive-genus ruled cases, and simple-elliptic configurations were eliminated by different geometric mechanisms; the remaining rational-resolution configurations required additional arguments in the accepted normal-carrier proof.

The older [normal-carrier topic note](../results/normal_carriers.md) ends with B1/B2/B3/D cases listed as open. That label describes the **historical partial stage** and is **superseded for the mate-existence question** by STCI-R-0001. It must not be read as the current frontier.

### B. Nonnormal integral quartics

The assembly organizes the nonnormal case by the genus of a normalized general plane section, with values \(0,1,2\). The genus-zero and genus-one branches use their respective audited reductions. The genus-two branch is more delicate: the accepted dependency assembly includes bisection configurations and endpoint and nonendpoint trisecant configurations, with **actual conductor and higher-contact corrections**.

This is a classification-based proof architecture, not a single numerical inequality. In particular, a bound obtained from normalization or intersection theory is not automatically the contradiction; the exceptional geometric cases and descent/contact behavior have to be closed.

| Branch | Role in the accepted theorem | Evidence |
| --- | --- | --- |
| Normal integral quartic | Full normal-carrier exclusion inherited by the assembly | [Acceptance and dependencies](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-11-session-all-quartic-results-acceptance.md) |
| Nonnormal, normalized sectional genus 0 | Audited genus-zero component | [Assembly audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-11-session-all-quartic-dependency-assembly-independent-audit.md) |
| Nonnormal, normalized sectional genus 1 | Audited genus-one component | [Assembly audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-11-session-all-quartic-dependency-assembly-independent-audit.md) |
| Nonnormal, normalized sectional genus 2 | Bisection/trisecant analysis, including conductor and higher-contact corrections | [Acceptance and dependencies](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-11-session-all-quartic-results-acceptance.md) |

**Audit boundary:** this synthesis has checked the promoted theorem record and its stated assembly structure, but has **not independently reproved or reaudited** every inherited component. Readers needing a specific genus-two or normal-carrier implication should follow the component links in the accepted assembly before using it in a new argument.

## 5.3 From integral carriers to arbitrary defining equations

An STCI presentation is not assumed at the outset to use irreducible equations. Suppose \(F=F_1\cdots F_t\) factors into irreducible homogeneous factors and \(V(F,G)=C_0\) set-theoretically. Because \(C_0\subset V(F,G)\) is irreducible, at least one factor \(F_i\) vanishes on \(C_0\). More strongly, for **every** factor \(F_i\), the set \(V(F_i,G)\) is contained in \(C_0\), and projective hypersurface intersection forces a nonempty curve component. Thus \(V(F_i,G)=C_0\), and each factor is itself a carrier with mate \(G\). The exact factor-reduction scope, including repeated factors, is covered by the [degree-factor audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-11-session-degree-factor-and-mf6-scope-audit.md).

Together with the earlier plane, quadric, and characteristic-zero cubic exclusions, STCI-R-0001 therefore implies:

\[
\boxed{\deg F\ge5,\qquad \deg G\ge5}
\]
for **every** hypothetical two-equation presentation, including reducible or nonreduced equations.

This is a lower bound on the **total degrees** of the equations, not a classification of higher-degree integral carriers. One may reduce to integral factors for exclusion arguments, but should not silently assume that a chosen minimal pair is integral without recording the reduction.

## 5.4 A useful degree-five consequence

If an integral quintic carrier \(X\) had a mate \(G\) of degree \(e\), Bézout along \(C_0\) would give generic intersection length
\[
m=\frac{5e}{4}.
\]
Hence \(4\mid e\). Since degrees at most four are already excluded, the **first numerically possible mate degree is eight**. This is only divisibility and lower-degree bookkeeping: it neither constructs nor excludes a \((5,8)\) pair.

The same principle applies to other degrees: \(4\mid de\) is necessary for the fixed degree-four curve, but generally far from sufficient.

## 5.5 Scope of older partial quartic arguments

A completed theorem can supersede the **open status** of an earlier subcase without making its calculations false or useless.

| Historical lane | What survives mathematically | What is no longer open |
| --- | --- | --- |
| [Normal quartic carriers](../results/normal_carriers.md) | Surface-classification and resolution methods; intermediate exclusions | Existence of a mate on an integral normal quartic |
| [Order-one structures](../results/order_one.md) | Conormal/jet and quasiprimitive constraints | Any quartic-carrier mate case they previously left |
| [Primitive quartic e=2](../results/quartic_e2.md) | Fourth-obstruction and factorization calculations | Higher mate degrees on integral quartic carriers |
| MF6 and thickening analyses in [STATE](../STATE.md) | Gorenstein pairings, defect identities, ancestor questions | Actual quartic-mate survivors |
| Local-cohomology ancestor incidence in [STATE](../STATE.md) | Finite principal-part reduction and unresolved incidence | **Not** superseded as a distinct ancestor-incidence question |

For present-day research decisions, use [STATE](../STATE.md) and [FRONTIER](../FRONTIER.md), rather than the old case labels. The independent [degree-(4,4) exclusion R-0022](../results/quartic_44_filtered_exclusion.md) is narrower than R-0001 and does not reopen quartic carriers. For residual intersections of arbitrary surfaces, see [residual intersections and jets](residual_intersections_and_jets.md): a quartic surface can appear in a proper intersection with residual curves without contradicting the STCI exclusion.

## 5.6 Why the newer methods are not additional exclusions

The Phase 3 integration adds several precise tools, but does not extend the degree bound of R-0001. Their quantifiers differ:

- The residual-jet theorem R-0025 forces positive residual degree for mates to **one prescribed sextic**, not every sextic or every carrier of degree at least five.
- The characteristic-two family R-0021 gives sole reduced support in characteristic two, while its characteristic-zero generic fiber has four components. The prescribed arithmetic nonlifting theorem R-0012 concerns that embedded special scheme and two specified bases, not arbitrary characteristic-zero pairs.
- The local filtered comparison R-0030 and conormal/socle results R-0032–R-0033 have stated saturation, defect or equality hypotheses. They do not establish a common singular point for every hypothetical STCI pair.
- The flag, dual and ruled models R-0026–R-0029 are proved for specified marked constructions. Their endpoint corrections are not automatically singularities of both equations in an arbitrary pair.
- The reviewed October 27 fixed-lower determinant test characterizes **proper** degree-compatible pairs with sole support once a lower embedded thickening is fixed. It is an exact conditional existence test, not proof that the required pair or lower scheme exists.

These results sharpen the *interfaces* to the open problem. A new exclusion requires either a family-level bound covering all candidates under its hypotheses or a genuine global incompatibility theorem. See the [dependency map](DEPENDENCIES.md) and [frontier](06-frontier.md).

## 5.6A Why fixed-degree and carrier-family obstructions do not enlarge the exclusion theorem

For a hypothetical proper pair of degrees \(d,e\) supported only on the degree-four curve, the generic transverse length must be \(de/4\). The finite truncated-length criterion is exact for an actual pair, but checking one pair or one fixed carrier cannot quantify over all degree-\(d\) carriers. The audited sextic jet bound [R-0025](../results/ci_fixed_sextic_jet_rigidity.md) therefore proves residual support for its prescribed carrier and mate degree, not a new universal lower bound on the defining degrees.

Likewise the full initial ideal may have higher cancellation-generated equations while the filtered actual equation module has zero comparison defect; these two local facts do not imply an STCI exclusion. See [the integrated normal-filtration treatment](normal_filtration_boundary_obstructions.md#full-initial-ideals-and-the-filtered-equation-module). The conductor–socle identity [R-0036](../results/pointwise_conductor_socle_defect.md) is conditional on an actual pair and restrictive normalization hypotheses; it does not eliminate all higher-degree carriers. The only unrestricted degree conclusion recorded here remains [R-0001](../results/quartic_carrier_exclusion.md).

## 5.7 Relation to the other chapters

The quartic exclusion uses global geometry of **carriers**, including normalizations and conductor corrections, and so is most directly related to [Chapter 4](04-carriers.md). The common-normal-factor and jet analyses of [Chapters 2](02-two-surfaces.md) and [3](03-infinitesimal-geometry.md) offer different necessary conditions and structural tools. Their unfinished cases do not weaken the quartic theorem; nor does the quartic theorem settle their more general questions for carriers of degree at least five.

The proper synthesis is therefore:

1. **Closed:** integral carrier degrees \(\le4\) for the fixed curve in characteristic zero, hence both defining degrees at least five.
2. **Still useful:** the geometric mechanisms and exact partial computations that led to, or run alongside, those exclusions.
3. **Open:** higher-degree carriers, special-point degeneration, general initial-ideal patterns, and unrestricted STCI existence.

Next: [the surviving frontier](06-frontier.md); [logical dependency map](DEPENDENCIES.md).


## 5.8 The (4,4) laboratory is not a surviving STCI degree case

For two quartic equations, Bézout gives total cycle degree sixteen. If the generic multiplicity along the degree-four curve is \(m_C=3\), the residual cycle has degree (16-12=4). The reviewed explicit constructions and their audits in [multiplicity and genus budgets](../supplements/INTRINSIC_44_MULTIPLICITY_AND_GENUS_BUDGETS.md) exhibit a genuine residual quartic and study moving \(A_2\) singularities of pencil members. This is valuable information about residual geometry, not a counterexample to R-0001.

A hypothetical proper (4,4) intersection with sole reduced support \(C\) would instead have generic multiplicity four. The historical geometric proof can be reformulated using direct blowups and surface numerical inequalities without relying on a classification of singularities; it is **not** thereby a proof using only the infinitesimal neighborhood of \(C\). In particular, the same restriction to the containing quadric can occur with different transverse multiplicities, so quadric restriction alone does not determine the needed obstruction. The narrower promoted exclusion is [R-0022](../results/quartic_44_filtered_exclusion.md); the unrestricted integral-quartic carrier theorem is [R-0001](../results/quartic_carrier_exclusion.md).

The characteristic-two prescribed (4,4) pair is a separate example whose special reduced support can be \(C\); its flat arithmetic deformation may acquire additional generic components. It is not a characteristic-zero (4,4) STCI and does not contradict the exclusions. See [R-0021](../results/quartic_mu4_degeneration.md) and the [arithmetic lifting supplement](../supplements/Z4_LIFTING_AND_DEFORMATION.md).
