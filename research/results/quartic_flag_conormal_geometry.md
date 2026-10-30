---
id: STCI-R-0026
title: "Flag incidence and conormal geometry of the marked rational quartic"
kind: theorem
status: proved
scope:
  characteristic: "0, with an explicitly stated characteristic-two fixed-scheme comparison"
  curve: "fixed marked rational quartic C0"
  hypotheses:
    - "The marked missing-middle-coefficient pairing and its incidence flag"
statement: "The marked incidence is a smooth complete flag surface; degree-two divisor addition is finite flat of degree six; its conormal, contact, and dual geometry have the structures detailed below."
dependencies:
  - STCI-R-0020
evidence:
  - "research/notes/2026-10-24-quartic-flag-duality-synthesis.md"
  - "research/notes/2026-10-24-quartic-flag-incidence.md"
  - "research/computations/quartic_flag_incidence_2026_10_24.json"
independent_audits:
  - "research/notes/2026-10-24-quartic-flag-duality-independent-audit.md"
accepted_in: "research/PROMOTION_ADJUDICATION_CR15-20_2026-10-26.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Marked geometry, not an unrestricted quartic classification"
  - "No STCI exclusion follows"
  - "Saved computations not freshly replayed"
---
# Flag and conormal geometry

## Statement
For the marked pairing b((a,b,c),(A,B,C))=aC+bB+cA, the incidence b=0 is the smooth complete flag F(1,2;3). Addition of effective degree-two divisors is finite flat of degree six, including the nonreduced length-six quadruple-root fiber. The resultant is its ramification divisor, whose pushforward is twice the dual quartic.

In characteristic zero the swap equalizer is the smooth conic b^2+2ac=0; in characteristic two it is a double line, while the flag remains smooth. The conormal normalization is C0 times C0, and the residual map is the symmetric degree-two quotient. The diagonal and the involution graph are distinct sections of square two, meeting at the two marked endpoints.

The third-contact divisor consists of the osculating section and both endpoint fibers. The fourth-contact incidence has length two at each endpoint. The second flag surface is F1, finite birational over the marked dual cubic AC^2+B^2D=0. The Gauss correspondence between the two ruled surfaces is resolved by two endpoint blowups and elementary transformations.

The addition-map boundary fibers have multiplicity partitions: four simple roots give six reduced points; (2,1,1) gives two singles and two doubles; (2,2) gives two singles and a quadruple; (3,1) gives two triples; and (4) gives one length-six point. The swap quotient is a degree-three unordered pair-partition cover, not the conormal normalization; its fixed conic is Legendrian in characteristic zero.

## Hypotheses and quantifiers
These are statements about the specified marked incidence and embeddings. The characteristic-two assertion concerns the swap fixed scheme, not a claim that the flag becomes singular.

## Proof outline
The pairing matrix has determinant minus one, identifying the incidence with the complete flag. Finite divisor addition and local factorization give the degree and fiber lengths. Polar and incidence calculations identify the conormal normalization and contact sections. Local endpoint equations yield the fourth-contact lengths. Ruled-surface Gauss geometry gives the dual normalization and elementary transformations.

## Dependencies
The characteristic-dependent conormal context of R-0020.

## Evidence and verification
Independent mathematical audit of CR-15 through CR-20 and CR-42 through CR-43, with retained symbolic certificate. No fresh computation in this promotion.

## Consequences
A unified geometric model for marked factorization, conormal contacts, and duality.

## Limitations
Do not identify the conormal normalization with C0 inside its containing quadric, or infer an STCI obstruction from these incidence statements.

## Permanent evidence navigation

The `research/notes/` metadata retains original provenance identifiers, not current-tree paths. For mathematical exposition and the linked detailed source supplements, consult [the consolidated subject chapter](../synthesis/01-problem-and-curve.md). Historical identifiers remain unchanged; the theorem's hypotheses and status are not expanded.
