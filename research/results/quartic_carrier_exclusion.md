---
id: STCI-R-0001
title: Complete exclusion of integral quartic carriers of the fixed rational quartic
kind: theorem
status: proved
scope:
  characteristic: "algebraically closed fields of characteristic zero"
  curve: "C0 = [s^4:s^3t:st^3:t^4] in P3, and its projective equivalents"
  hypotheses:
    - "X is an integral degree-four hypersurface in P3 containing C0"
    - "G is any homogeneous form of positive degree"
statement: "For every such X and G, the set V(X,G) is not C0."
dependencies: []
evidence:
  - "https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-11-session-all-quartic-results-acceptance.md"
independent_audits:
  - "https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-11-session-all-quartic-dependency-assembly-independent-audit.md"
  - "https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-11-session-degree-factor-and-mf6-scope-audit.md"
accepted_in: "https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-11-session-all-quartic-results-acceptance.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Does not settle whether C0 is an STCI using surfaces of degrees at least five."
  - "Does not apply to every smooth rational quartic embedding."
  - "Does not resolve common-quartic local-cohomology ancestor incidence."
---

# Complete quartic-carrier exclusion for the fixed C0

## Statement

Let \(k\) be algebraically closed of characteristic zero and
\[
C_0=\{[s^4:s^3t:st^3:t^4]\}\subset\mathbf P^3_k.
\]
For **every integral quartic surface** \(X\subset\mathbf P^3\) containing \(C_0\), and **every homogeneous form** \(G\) of positive degree,
\[
V(X,G)\ne C_0\quad\text{set-theoretically}.
\]
The theorem is invariant under projective coordinate change of this particular embedding.

## Hypotheses and quantifiers

There is no restriction on normality of \(X\), singularities of its finite normalization, conductor scheme, mate degree, or generic normal order of \(G\). This is an integral-carrier theorem, not a statement that arbitrary quartic equations are integral.

## Proof outline

The accepted October 11 assembly uses the previously established normal-integral-quartic exclusion and covers nonnormal integral quartics by normalized general-plane-sectional genus \(0,1,2\). The genus-two analysis includes bisection and both endpoint and nonendpoint trisecant cases, with actual conductor and higher-contact corrections. The independent dependency audit checks exhaustive coverage and the scope of inherited inputs. These are **pointers to the accepted proof**, not a new verification of its component arguments.

## Dependencies

The complete dependency graph, including the earlier normal-quartic theorem, genus-zero and genus-one audits, genus-two component proofs, and classical cubic exclusion, is in the [October 11 acceptance](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-11-session-all-quartic-results-acceptance.md) and [independent assembly audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-11-session-all-quartic-dependency-assembly-independent-audit.md). These sources remain on the Ultra research branch; this PR does not merge or duplicate them.

## Evidence and verification

- [Accepted assembled theorem](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-11-session-all-quartic-results-acceptance.md)
- [Independent dependency and coverage audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-11-session-all-quartic-dependency-assembly-independent-audit.md)
- [Factor reduction and cubic scope audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-11-session-degree-factor-and-mf6-scope-audit.md)

The linked source branch is not being declared a second canonical authority: its notes are preserved evidence for this reviewed promotion. The original Git blobs were inspected at SHA `d7d8580131e3e69c611e307a4e0d3b16d75d69b1` (acceptance), `5d3d2aa936f74195a569063ca21395ee582131dd` (assembly audit), and `7cb83e9844efb692df23f63c737c61bafc3e1db7` (factor audit).

## Consequences

By the separately audited factor reduction, every irreducible factor of either defining equation in an STCI presentation of \(C_0\) must itself admit the other equation as a mate. Combining the quartic theorem with the earlier plane, unique-quadric, and characteristic-zero cubic exclusions, **both defining degrees must be at least five**, even for reducible or nonreduced defining equations.

For a quintic carrier, Bézout additionally forces the mate degree to be divisible by four; its first numerically possible positive degree is eight. This is a necessary divisibility condition, not existence.

## Limitations

The unrestricted characteristic-zero STCI problem for \(C_0\) remains **open**. This theorem does not rule out degrees \(\ge5\), entirely-thick presentations, or distinct common-quartic ancestor questions. It must not be generalized to all smooth rational quartic embeddings without a separate argument.

## Supersession map

This result supersedes **the open-status labels**, not the underlying partial theorems, in the earlier `research/STATE.md` quartic \(e=2\), MF6 quartic-mate, and normal-quartic sections, and the corresponding quartic-mate priorities in `research/FRONTIER.md`. Their prior computations and structural lemmas remain available. The separate local-cohomology ancestor problem remains open.
