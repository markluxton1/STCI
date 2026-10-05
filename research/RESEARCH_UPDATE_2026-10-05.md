# Continuation batch: 2026-10-05

This file indexes the dated continuation work recorded after the 2026-09-30
handoff. It is a research record, not a resolution of the projective STCI
problem. Every result below is stated with its scope; computational checks are
exact but do not replace the geometric hypotheses in the accompanying notes.

## Current status

The unrestricted question remains open. In particular, no new pair of forms
has been found for the smooth rational quartic

\[
C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3
\]

and no counterexample to the universal integral-curve statement has been
constructed. The strongest new work narrows several branches while preserving
the unresolved incidence and higher-jet problems.

## Results proved or independently audited in this batch

- The quartic local-cohomology route now has a finite-stage reduction. Under
  P-037 and the literature's characteristic-zero degree-(4,4) exclusion, a
  hypothetical quartic ancestor is killed by \(I^4\), has a representative
  at the fixed \((q^4,B^4)\)-stage, and its primitive common conormal direction
  has degree \(e\le 2\). The degree bound is necessary only; it does not
  exclude the remaining finite nonlinear incidence problem. See
  [the finite-principal-part note](notes/2026-10-05-localcoh-finite-bound.md).

- The all-stage local-cohomology calculation excludes both ruling-ratio slices
  given by Möbius transforms of \(t\) and \(t^3\), including their boundary
  specializations, for the characteristic-zero monomial quartic. Arbitrary
  primitive directions of degree \(e\le2\) remain open. See
  [the degree-four frontier note](notes/2026-10-05-localcoh-degree4.md).

- For a regular first-normal quotient in a hypothetical degree-(4,6) pair,
  the pure constant horizontal direction \(e=0\) is excluded. The proof was
  independently audited, and a separate local residual calculation excludes
  the regular \(e=1\) branch via the \(A\le D_{m-1}\) bound. Mixed directions,
  nonregular quotients, and the remaining pole strata are not settled. See
  [the regular branch note](notes/2026-10-05-mixed46-regular.md),
  [the audit](notes/2026-10-05-audit-regular-pure.md), and
  [the residual-cycle note](notes/2026-10-05-residual-cycle.md).

- The multiplicity-six local calculation gives an exact Fitting-divisor
  identity candidate
  \(A=D_3+(D_2\wedge(D_3-D_2))\) and reduces the seven numerical pole types
  to seven explicit necessary strata with further local restrictions. The
  identity is recorded as a proof candidate where its pointwise global
  interpretation still needs a separate audit; no global sextuple or STCI
  conclusion is claimed. See
  [the pole-strata note](notes/2026-10-05-mixed46-poles.md).

- The fixed split-[2,2] degree-one sextic boundary has been lifted exactly to
  ambient equations. Its node/A1 analysis and Mumford branch intersections
  exclude the fixed normal form (the relevant intersection counts are 9 or 7,
  rather than the required 17 or 5). The larger family and higher-genus data
  remain open. See [the split-sextic note](notes/2026-10-05-split-sextic.md).

- The type-A \((4,5)\) exclusion was independently reconstructed from all
  parameter charts through the terminal extension obstruction. A dense type-B
  audit independently rederives its elimination boundaries and terminal
  obstruction. These audits strengthen P-040's degree-pair exclusion but do
  not extend it to other multiplier degrees or prove the general STCI claim.
  See [the type-A audit](notes/2026-10-05-typea-audit.md) and the verifier
  `computations/verify_typeb45_dense.py`.

- The uniform quasiprimitive restrictions give the checked bounds on
  multiplicity and first defects for quartic carriers. An exploratory
  characteristic-zero \((4,7)\), primitive-degree-two computation records a
  sample obstruction only; it is not a theorem for all \((4,7)\) pairs. See
  [the uniform-multiplicity note](notes/2026-10-05-uniform-multiplicity.md).

- A literature refresh records the scope of Thoma's one-binomial-carrier
  theorem, the published Mandal--Zinna affine result, and the limits of the
  discrepancy invariant for this projective problem. It also proves the
  uniform symbolic-power equals ordinary-power statement for integral divisors
  on a smooth quadric and gives exact Hilbert formulas. This is a useful
  special-case laboratory, not a reduction of the general problem. See
  [the literature-and-quadric note](notes/2026-10-05-literature-new-routes.md).

## Reproducible checks

The new exact companions are listed in
[`computations/README.md`](computations/README.md). They cover the finite
principal-part dimensions, ruling slices, the regular mixed-(4,6) branch, the
residual lattice, the split-[2,2] lift, the type-A and dense type-B audits, the
quadric power algebra, and the conductor example. The original fifteen
verification scripts from the prior handoff were rerun as well. All Python
checks passed under
`/private/tmp/stci-cas-venv/bin/python` with
`PYTHONDONTWRITEBYTECODE=1`; the two Macaulay2 checks passed with
`/opt/homebrew/bin/M2 --script`. Generated bytecode is ignored and is not part
of the research record.

## Highest-value remaining questions

1. Solve or exclude the finite quartic incidence problem in
   \((0:_{H_I^2(S)}I^4)_{-7}\) after the direction bound \(e\le2\), including
   the non-ruling directions.
2. Audit the pointwise Fitting-divisor identity and then combine it with the
   mixed-(4,6) pole strata without assuming regularity of the first quotient.
3. Determine whether the split-sextic boundary calculation extends from the
   fixed normal form to the full parameter family.
4. Find a uniform geometric invariant connecting these finite local
   obstructions to the original saturated-radical STCI condition.

The notes deliberately retain the distinction between proved statements,
independent audits, exact computational evidence, and unresolved conjectural
extensions.

## Late continuation: full e=2 quartic-carrier obstruction

A later 2026-10-05 branch completed the ambient-stabilizer calculation and
computed the generic four-parameter (e=2) cubic extension obstruction exactly,
with strong cross-checks. In characteristic zero,
[
operatorname{Stab}_{PGL_4}(C_0)congmathbf G_mtimesmathbf Z/2,
]
so on (A_2B_0
e0) the genuine generic symmetry cross-section is
[
A=x+az+z^2,qquad B=1+bz+dz^2.
]
The full exact obstruction has
[
Omega_i=G_i/(32Delta),qquad
Delta=1-ab+a^2d-2dx+b^2x-abdx+d^2x^2.
]
The three-parameter (b=0) family is completely excluded by the exact
membership (Delta_0in(G_1,ldots,G_5)).

Crucially, the hoped-for universal implication
[
Omega=0LongrightarrowDelta=0
]
is **FALSE**. The basepoint-free family
[
A=z^2-	frac12z+x,qquad B=1-2z+x^{-1}z^2,
qquad x
e0,	frac14,
]
has all five obstruction coordinates zero and therefore extends to a primitive
quadruple. This is not a quartic carrier or an STCI construction; it proves
only that the first nontrivial (e=2) extension obstruction is insufficient.
A subsequent independent audit reconstructed this surviving family's cubic
obstruction directly from the pre-P-044 moving-coordinate formal-neighborhood
calculation, obtaining \(\Omega=(0,0,0,0,0)\), and independently verified the
resultant \((4x-1)^2/(4x)\).

See [the full e=2 note](notes/2026-10-05-e2-full-obstruction.md) and the
[exact formula audit](computations/e2_full4_obstruction_2026-10-05.txt).
The immediate (e=2) question is now the infinitesimal order actually forced
by a genuine quartic carrier and whether this explicit surviving quadruple
extends through that order. The (e=0), (e=1), equivariance, and uniform
local-cohomology routes remain live alternatives.


## Late continuation: P-044 survivor cubic theorem

The explicit basepoint-free P-044 survivor is now excluded as a quartic
carrier, without computing higher primitive extensions.  For
[
A=z^2-	frac12z+x,qquad B=1-2z+x^{-1}z^2,qquad x
e0,	frac14,
]
the canonical primitive triple lies on the irreducible cubic
[
H_x=D+4x^2B+4x^4A+
(-4x^3x_0+8x^3x_1-2xx_2+4xx_3)q.
]
The primitive filtration gives degree (12) and genus (13).  Comparing with
a proper ((3,4)) complete intersection (degree (12), genus (19)) proves
[
H^0(I_{C_3(x)}(4))=H_xH^0(O(1)),
]
so every containing quartic is reducible as (H_xell).  The plane factor
forces extra set-theoretic intersection with any septic, excluding this entire
explicit survivor family from a ((4,7)) STCI presentation.

**Status: PROVED / INDEPENDENTLY AUDITED.**  This does not classify all P-044
zeros and does not eliminate the full (e=2) branch.  The immediate frontier
is now classification or geometric exclusion of the remaining basepoint-free
P-044 zero locus, rather than extending this explicit family farther up the
primitive tower.  See
[the proof](notes/2026-10-05-p044-survivor-cubic.md) and
`computations/verify_p044_survivor_cubic.py`.
