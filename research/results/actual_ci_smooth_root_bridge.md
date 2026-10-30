---
id: STCI-R-0006
title: Actual complete-intersection blowup bridge for smooth full roots
kind: theorem
status: proved
scope:
  characteristic: "any algebraically closed field"
  curve: "smooth connected curve C in a smooth threefold X"
  hypotheses:
    - "The actual complete intersection (F,G) has reduced support exactly C"
    - "First degree-r ordinary normal relation is a saturated line subbundle of Sym^r N_C^*"
    - "Both actual equations have generic order r and their degree-r symbols jointly generate the first relation everywhere on C"
    - "Full generic initial ideal is the coprime binary complete intersection (f_r,g_s) with s>r and ell=s-r>=2"
    - "The full Cartier root Z=(f_r) on the blowup exceptional divisor is smooth"
statement: "The actual intersection of the two strict divisors is a primitive ell-fold structure on the full smooth root Z, with local ideal (h,u^ell) and compatible Cartier lifts through exceptional order ell-1."
dependencies:
  - STCI-R-0005
evidence:
  - "research/notes/2026-10-15-generalization-inseparable-root-blowup-bridge.md"
independent_audits:
  - "research/notes/2026-10-15-generalization-inseparable-root-blowup-local-algebra-review.md"
  - "research/notes/2026-10-15-generalization-inseparable-root-blowup-bridge-independent-audit.md"
accepted_in: "research/notes/2026-10-15-generalization-inseparable-root-blowup-bridge-independent-audit.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Not a bridge for arbitrary STCI equations or arbitrary initial forms."
  - "The first relation must be saturated and generated everywhere, and the entire initial ideal must have the prescribed form."
  - "No exclusion when the gap is one or the full root is singular or nonreduced."
---

# Actual-CI bridge for smooth full roots

## Statement

Let k be algebraically closed of any characteristic, X a smooth threefold, C a smooth connected curve, and Y=(F,G) an **actual complete intersection** with reduced support C. Assume all of the following:

1. The first ordinary normal relation of degree r is a saturated line subbundle of Sym^r(N_C^*).
2. The two actual equations have generic normal order r, and their degree-r symbols jointly generate that line at every point of C.
3. The **full** generic ordinary initial ideal is (f_r,g_s), a coprime binary complete intersection with s>r and ell=s-r>=2.
4. The full Cartier root divisor Z=(f_r) on the exceptional divisor of Bl_C(X) is smooth, not merely smooth after reduction.

Then the actual intersection of the two strict divisors has support exactly Z and has no vertical exceptional-fiber component. Locally along Z, its ideal is (h,u^ell), with h defining a smooth surface and u an exceptional parameter cutting Z as a reduced Cartier divisor. It is an embedded primitive ell-fold structure on Z, with surviving conormal O_Z(-E). Its first obstruction vanishes and it supplies compatible embedded Cartier lifts on exceptional neighborhoods of order m<ell.

No separability or tame-ramification hypothesis is needed, including for inseparable residue extensions of root points.

## Proof outline

At the generic point of C, work in the actual two-dimensional regular local ring, not its completion. Choose a standard-basis pair P,H in the actual ideal with initial forms f_r,g_s. Equality of initial ideals and Krull intersection give equality of ideals before completion. The invertible change of generators survives on the blowup. Crucially, after dividing **both original strict equations by their original order r**, the transformed ideal retains the exceptional factor u^ell. At the actual root prime, reducedness means multiplicity one even for inseparable residue extensions. Local smooth-surface/UFD arguments globalize the form (h,u^ell) without saturating away vertical components.

## Consequence with STCI-R-0005

For the balanced rational-space-curve movement-two smooth-root setting of [STCI-R-0005](smooth_root_formal_obstruction.md), the accepted finite empty-stage theorem gives an integer N for each fixed root order r. Under **all the bridge hypotheses above**, an actual CI cannot have gap ell=s-r>N. This is a conditional finite-gap obstruction, not a universal bound for all actual STCI presentations. The sources do not provide an explicit N.

## Evidence

- [Actual-CI bridge theorem](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-inseparable-root-blowup-bridge.md)
- [Independent generic local-algebra review](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-inseparable-root-blowup-local-algebra-review.md)
- [Independent full-scope audit (PASS)](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-inseparable-root-blowup-bridge-independent-audit.md)

The characteristic-zero predecessor and characteristic-free formal-tower addendum are cited and treated as inherited premises in these notes.

## Permanent evidence navigation

The `research/notes/` metadata records historical provenance identifiers, not current-tree files. For the retained mathematical argument, conditional hypotheses, and source-supplement routes, consult [the consolidated subject chapter](../synthesis/03-infinitesimal-geometry.md). The original evidence identities and theorem scope remain unchanged.
