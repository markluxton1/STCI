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
