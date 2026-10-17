---
id: STCI-R-0004
title: Full-conductor phase and torsion-coset reduction for projection families
kind: reduction
status: proved
scope:
  characteristic: "algebraically closed field of characteristic zero"
  curve: "fixed embedded smooth curve C in projective three-space"
  hypotheses:
    - "Fixed normal integral projective surface S with ample line bundle H"
    - "Smooth ample Cartier curve c and section Q of H with divisor m*c for m>0"
    - "Finite-type parameter family of four sections of H restricting to the fixed embedded C"
    - "Retain only basepoint-free finite birational maps to integral hypersurfaces with full reduced inverse support exactly c"
statement: "After finite stratification and a finite surjective cover, mate existence is equivalent to torsion of a full-conductor phase tuple in a fixed torus; the torsion image admits a finite torsion-coset envelope."
dependencies:
  - STCI-R-0002
  - STCI-R-0003
evidence:
  - "https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-projection-torsion-coset-reduction.md"
independent_audits:
  - "https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-projection-torsion-coset-independent-review.md"
accepted_in: "https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-projection-torsion-coset-independent-review.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "The phase images and torsion cosets of the fixed C0 families have not been computed."
  - "The mate locus need not be constructible."
  - "Non-Cartier, multiple, and higher-degree inverse lifts are not covered."
---

# Full-conductor phase reduction for projection families

## Statement

Fix an algebraically closed characteristic-zero field, a normal integral projective surface S with ample H, and a smooth ample Cartier curve c. Assume a section Q of H has divisor m*c, m>0. Consider a finite-type family T of four sections of H restricting on c to a fixed embedded curve C in projective three-space.

Retain only parameters for which the sections are basepoint free, define finite birational maps onto integral hypersurfaces, and have full reduced inverse support of C equal to c, without isolated extra inverse points.

The accepted theorem constructs, after finite locally closed stratification, a constructible parameter locus T0, a finite surjective cover Z->T0, and a phase morphism z:Z->(G_m)^D such that a carrier has a set-theoretic mate exactly when its phase tuple is torsion. All generic conductor curves, nilpotent conductor equations, and admissibility boundaries are retained.

For the constructible phase image W=z(Z), the torsion points of W are a finite union of torsion points in nonempty relatively open subsets of torsion cosets contained in W. This is a finite structural envelope, not an explicit computation of those cosets.

## Hypotheses and proof outline

The original proof uses flattening and monic Noether-normalization equations before rational localization to preserve all generic conductor components on specialization. Finite Artinian matrix calculations retain the full nilpotent conductor defect. A finite root-ordering cover produces a phase tuple in a fixed torus. Laurent's theorem gives the torsion-coset envelope for the constructible phase image, with excluded parameter boundaries still excluded. The [independent review](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-projection-torsion-coset-independent-review.md) records the corrections needed for specialization and confirms the result.

## Consequences for fixed C0

The three Cartier singleton models from [STCI-R-0002](cartier_singleton_lift.md) fall within the accepted framework: degree-eight smooth quadric, degree-eight quadric cone, and degree-sixteen plane normalizations. The source establishes actual on-C conductor thresholds M=5,5,13, respectively. If the phase order is E, every positive multiple of E at least M is a mate degree; additional mate degrees, if any, are multiples of E below M. A zero-dimensional-only surviving torsion-coset envelope bounds minimum mate degrees within the family; a positive-dimensional surviving coset yields unbounded phase orders. These statements do not calculate the actual phase images or settle existence for any of the three models.

## Evidence

[Accepted source theorem](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-projection-torsion-coset-reduction.md).

[Independent review (PASS with recorded corrections)](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-projection-torsion-coset-independent-review.md).

## Limitations

The torsion set and mate locus need not be constructible. The actual C0 projection-family phase images, torsion cosets, and admissible parameters remain uncomputed. This reduction does not address non-Cartier or multiple inverse lifts and does not settle the unrestricted STCI problem.
