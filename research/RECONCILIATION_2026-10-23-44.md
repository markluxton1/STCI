# October 23 (4,4) verification and scope-limited promotion

## Decision
Promote STCI-R-0020 (conormal characteristic jump), STCI-R-0021 (specific mu4 family), and STCI-R-0022 (narrow characteristic-zero (4,4) filtered-contact exclusion). These are three distinct claims with different dependencies. The stronger all-degree quartic-carrier exclusion STCI-R-0001 is not used to establish R0022 and is not replaced by it.

## Clean reproducibility
[GitHub Actions run 39972680627](https://github.com/markluxton1/STCI/actions/runs/39972680627) concluded **success**: Macaulay2 mu4 certificate, exact quartic symbols, filtered-contact certificate, independent contact audit, and inherited e=1 classification audit all passed. Markdown navigation checks also passed in run 39972680363. The independent October 23 mathematical audit of the filtered proof is the acceptance basis beyond passing scripts.

## Proof-dependency boundaries
R0020 uses the explicit conormal transition and its characteristic-dependent extension class. R0021 uses the explicit flat family, charts and Macaulay2 global decomposition. R0022 uses the accepted saturated quasiprimitive/Gorenstein pairing argument (research/notes/2026-10-05-mf6-pairing-audit.md), the exhaustive e=1 primitive-triple classification (research/notes/2026-10-07-session-mf6-e1-independent-audit.md), and new e=0 orbit and cubic-contact computations. The saturated filtration is essential: ordinary nilradical powers cannot be substituted. The inherited e=1 classification is an explicitly cited source-level premise, not an independently ID-bearing theorem.

## Limits
R0022 excludes only the degree pair (4,4) for fixed C0 in characteristic zero. R0021 concerns only its specified equations. No unrestricted STCI nonexistence theorem is claimed. Symmetric algebra alone is insufficient to supply the higher embedded gluing and global quartic lifting obstruction.

## Review provenance
Source mathematical review: research/notes/2026-10-23-quartic-44-filtered-proof-independent-audit.md and research/notes/2026-10-23-quartic-geometry-symbol-independent-audit.md. Computational run: 39972680627. This promotion is recorded on the research branch for review through pull request #64; main is unchanged until merge.
