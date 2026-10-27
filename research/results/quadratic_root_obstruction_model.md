---
id: STCI-R-0007
title: Universal first and second ambient obstructions for quadratic movement-two roots
kind: reduction
status: proved
scope:
  characteristic: "characteristic zero"
  curve: "fixed monomial rational quartic C0 in P3"
  hypotheses:
    - "Basepoint-free binary quadratic root f=a(z)u^2+b(z)uv+c(z)v^2, with a,b,c quadratic on the base"
    - "Actual embedded blowup chart and first normal relation operator from the accepted root framework"
    - "Second-class actual-CI application additionally requires the STCI-R-0006 bridge and next relation degree s>4"
statement: "The first obstruction is a universal 16-by-13 rank incidence on P8, and the second obstruction has a complete chart-free test by 25 scalar pairings. The second class is nonzero at an explicit smooth first-compatible torsion-two seed."
dependencies:
  - STCI-R-0005
  - STCI-R-0006
evidence:
  - "research/notes/2026-10-14-generalization-quadratic-root-universal-incidence.md"
  - "research/notes/2026-10-14-generalization-quadratic-root-second-obstruction.md"
  - "research/notes/2026-10-15-generalization-quadratic-root-global-second-dual-compression.md"
independent_audits:
  - "research/notes/2026-10-14-generalization-quadratic-root-universal-incidence-independent-audit.md"
  - "research/notes/2026-10-14-generalization-quadratic-root-second-obstruction-independent-audit.md"
  - "research/notes/2026-10-15-generalization-quadratic-root-global-second-dual-compression-independent-audit.md"
accepted_in: "research/notes/2026-10-15-generalization-quadratic-root-global-second-dual-compression-independent-audit.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "The global second zero locus is not proved empty."
  - "The smooth seed demonstrates that first-order and spectral torsion conditions are not sufficient."
  - "No explicit finite obstruction stage for every smooth root is computed."
  - "No unrestricted actual-CI or STCI exclusion."
---

# Quadratic movement-two root: universal obstruction model

## First compatibility scheme

For the fixed C0 in characteristic zero, write the moving first normal relation as f=a(z)u^2+b(z)uv+c(z)v^2 with base-quadratic a,b,c and no common base zero. This gives a basepoint-free open U in P8. The accepted first ambient obstruction is the cokernel class of the actual chart operator. It vanishes precisely on the universal 16-by-13 rank incidence formed by the 16-by-12 multiplication matrix A_f and the 16-vector d_f. The multiplication matrix is injective on all U, including singular and nonreduced root divisors.

An explicit smooth seed is f=(z^2+4)u^2+(z^2-8)v^2. It lies on a smooth four-dimensional component of the first compatibility scheme, and its smooth genus-one root has ruling-difference class of exact order two. Hence neither the first ambient class nor the spectral torsion test alone excludes the seed.

## Second obstruction

The compatible first principal relation is unique. Its next actual ambient obstruction is a canonical class in a rank-sixteen bundle on the first compatibility scheme. At the smooth seed, an independently checked sparse Serre-dual pairing equals 1/8, so the second obstruction is **nonzero**. Consequently the generic point of the four-dimensional first-compatible component through the seed fails the second lift. This does not establish that the entire second zero scheme is empty.

The accepted global dual compression replaces the sixteen obstruction coordinates by twenty-five exact scalar pairings, valid across the entire basepoint-free family without choosing coefficient charts or invertible minors. Its rank-two bundle W is the kernel of the surjection

    O_P1^5 -> O_P1(2)^3

with rows (a,b,c,0,0), (0,a,b,c,0), (0,0,a,b,c). The dual obstruction space is H^0(P1,W(10)), of dimension sixteen. The surjection from H^0(O_P1(4))^5, of dimension twenty-five, supplies a complete pairing test.

## Open geometric locus

The second zero locus, its other components, and its intersection with spectral torsion loci remain unresolved. The global model gives sixteen first equations, twenty-five second equations, and a homogeneous discriminant nonvanishing condition for smooth roots. An attempted elimination did not yield a mathematical emptiness certificate.

The second obstruction is a necessary condition for actual supported complete intersections **only** when the full hypotheses of [STCI-R-0006](actual_ci_smooth_root_bridge.md) hold and the next relation degree s>4. At s=4 the next relation changes the obstruction target. No general STCI conclusion follows.

## Proofs and independent reviews

- [Universal first incidence](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-quadratic-root-universal-incidence.md) and [independent audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-quadratic-root-universal-incidence-independent-audit.md).
- [Actual second obstruction](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-quadratic-root-second-obstruction.md) and [independent audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-quadratic-root-second-obstruction-independent-audit.md).
- [Global second-dual compression](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-quadratic-root-global-second-dual-compression.md) and [independent audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-quadratic-root-global-second-dual-compression-independent-audit.md).

These are accepted proof and audit links on the preserved Ultra branch, not newly rerun computations.
