# Investigation 3 supplement: independent global Laurent re-expansion (reported, not yet independently reproduced)

**Status:** user-reported independent calculation, transcribed here for provenance; not a new audited theorem or a machine-checked certificate.

For the distinguished conormal quotient, the original Laurent cocycle is
[
K=-6u^{-2}.
]
Under the reported nonlinear adapted changes
[
m_U'=X+(1+u)Y^2,qquad
m_V'=(-3A+4cB)+(c+c^2)B^2/9,
]
the re-expanded cocycle is
[
K'=1+u-6u^{-2}+u^{-5}+u^{-6}.
]
Consequently
[
K'-K=(1+u)+u^{-4}(u^{-1}+u^{-2}),
]
a Čech coboundary in the specified Laurent trivializations, so the two expressions represent the same class.

**Verification boundary:** The calculation was reported after the independent audit branch was committed; no standalone calculation script or full derivation was supplied for this supplement. This is one nontrivial global coordinate example, not a substitute for the relative-Ext functoriality proof in `2026-10-21-z4-persistent-independent-audit.md`. Do not label this supplement independently reproduced or promoted.
