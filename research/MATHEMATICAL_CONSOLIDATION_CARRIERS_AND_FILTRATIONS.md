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
