# Mathematical consolidation: normal carriers versus first-relation defects

**Status:** thematic synthesis, not a new theorem. Read canonical R-0003, R-0013, R-0016, R-0034, R-0035 and their principal proof/audit sources.

## Two genuinely different entry points

**First-relation/filtered-algebra route.** Given an actual lci thickening supported on C and a full generic ordinary binary CI (f_r,g_s), study the actual first relation K_r in Sym^r N^*. In R-0013, K_r is saturated: a global actual-generator sequence is nonsplit, both equations have exact generic order r, and movement epsilon=1 is impossible for C0. In R-0016, K_r=R(-D) need not be saturated: a quotient resultant produces an effective divisor Delta with degree (r-1)c_(s-1)-r c_s and upper bound (r-1)binom(s-r,2)length(D). For gap <=2 normal flatness follows under the full hypotheses. A nonsaturated first relation can pay for degenerations; it cannot simply be discarded.

**Carrier/divisor descent route.** Fix an integral surface X containing C. R-0003 treats an integral Cohen–Macaulay carrier with finite normalization and no isolated inverse-support points: a mate exists exactly when the full conductor descent lattice has a vector strictly positive on every inverse branch. The criterion is not an effective classification of all carriers. When X is normal, the conductor disappears and the obstruction becomes torsion of the class mu[C]-v[H], where mu=a/gcd(a,4), v=4/gcd(a,4). The normal-carrier source proves that the torsion order is detected by local class groups on C under the rational ample-Cartier-multiple hypothesis. R-0034 then relates the **actual local Cartier index** r (not the surface multiplicity) to ordinary socle defects for a mate nC: D_n,P=(n/r-1)A_F,P+(n/r)D_r,P. R-0035 excludes normal carriers whose on-curve local indices are all <=4, with inherited torsion and quadratic-direction inputs. Higher indices, nonnormal carriers, and entirely-thick cases remain outside this result.

## Important interface: ordinary versus saturated filtration

The independent index/socle audit proves that, for a curvilinear actual CI thickening, the torsion-free **ordinary** layers are powers B_i=B_1^i, and 2 sum length(T_i)_P=n D_n,P. This does not assert that the **saturated** BF layers have trivial multiplication divisors. The first-relation resultant theorem instead uses the saturated filtration and its generation defects. Confusing the two makes apparent contradictions and invalid shortcut exclusions.

## Mathematical failures worth retaining

- Substituting carrier surface multiplicity for actual Cartier index invalidates the local formula.
- Using torsion-free Cl(X) to argue that no mate exists requires the rational-curve/low-degree carrier argument; it is not merely a local Picard claim.
- Claiming the bounded-index exclusion for indices 6,12 or higher is unsupported.
- Extending the resultant formula beyond a full generic binary CI or to residual-component intersections is unsupported.
- Treating a numerical defect budget as global realizability or nonexistence is unsupported.
- Treating normalization/conductor descent as an effective general algorithm is unsupported.

## Architectural decision

Keep **two subject chapters**: (1) *Normal relations and filtered thickenings*, (2) *Carriers, normalization and conductor descent*. Add a short shared interface on ordinary/saturated filtrations, local Cartier indices and socle defects. Do not merge them into one putative obstruction theorem. Canonical R records remain independent scoped theorem authority. Cross-link examples where both frameworks apply; do not assume a universal translation.

## Next content review

Review the remaining carrier results R-0002, R-0004, R-0017 and the legacy `results/normal_carrier.md` and `results/entirely_thick.md`. Identify the conceptual difference between fixed-carrier descent, phase reduction, and entire-thick cases before deciding which older syntheses to fold into the chapters.


## Degree-obstruction audit (theme 5, continuation)

The strongest global degree exclusion is **R-0001**: every integral quartic carrier of the *fixed* C0 in characteristic zero has no mate of **any** positive degree, whether normal or nonnormal. Its accepted proof assembles normal quartics and nonnormal plane-sectional genus 0,1,2 cases; the source acceptance and independent dependency audit should remain linked. Factor reduction, together with plane/quadric/cubic exclusions, implies both degrees of any hypothetical STCI presentation are at least five, including reducible defining forms. For a quintic carrier the mate degree is divisible by four (first possible degree eight). Do not misstate R-0001 as excluding arbitrary quartic forms without applying factor reduction.

**R-0022** is a mathematically distinct, narrower (4,4) proof via saturated Gorenstein filtration and contact-space classification; its alternate K3 resolution argument is retained as a valid independent route, not made the main approach. It adds insight into why length four cannot be achieved by the relevant quartic pencils but does **not** strengthen the all-degree exclusion R-0001.

The legacy **normal_carriers.md** records useful earlier geometric classification and failure modes (rational versus nonrational singularities, ADE budget, simple elliptic exclusion, Ishii–Nakayama types, finite degree bound). Its historical open cases are **not current open quartic-mate cases** after R-0001. Preserve the classification ideas, not obsolete frontier labels.

The legacy **quartic_e2.md** records an important failed shortcut: primitive e=2 quadruples **do exist**, contrary to an earlier blanket exclusion. The actual result is that their canonical primitive triples force all containing quartics to factor, excluding only specified (4,7) and (4,8) branches by that argument. The all-quartic theorem now subsumes these as mate exclusions, but does not erase their structural significance.

The legacy **order_one.md** gives conditional quasiprimitive/BF numerical restrictions (0<=e<=6 generally under its hypotheses; 0<=e<=2 for quartic order-one carriers). The **entirely-thick** branch lies outside it. These are useful inputs to the normal-filtration chapter, not unrestricted global exclusions.

The legacy **normalization_conductor.md** provides the fixed-carrier inverse-support obstruction: an isolated point in the full reduced normalization preimage excludes a mate. When all nonnormality is supported on C, an effective Cartier divisor upstairs with appropriate positive polarization is sufficient after a high conductor power. This **special support-contained sufficiency** must not be conflated with the full-conductor descent lattice of R-0003 in general.

### Remaining audit targets

For global intersection/incidence theme 6, review universal plane-family W_osc/W_bit, degree formulas, and fixed-boundary deformation records; for theme 7, map each exact computational witness to its theorem or provisional claim. This pass reviewed the **canonical statements and selected source descriptions**, not independently rerun all historical quartic exclusion proofs.
