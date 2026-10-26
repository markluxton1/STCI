# Historical structural results: claim-level promotion packet

Date: 2026-10-26. **Proposed records only; no canonical IDs assigned or result index changed.** Prepared under research/AUTHORITY.md from original proofs and independent reviews. This packet is an explicit review request, not an acceptance decision.

## Candidate A: full conormal-filtration socle budget

**Claim.** Let C be a smooth integral curve of degree e and genus g in P3 and Y=V(F_a,G_b) an actual complete intersection with Y_red=C. Put J=I_C O_Y, n=ab/e, d the generic Loewy index, h_j the generic ranks of J^j/J^(j+1), M=sum(j h_j), and L=e(a+b-4)-(2g-2). For lambda>0 satisfying the stated degree bound for all torsion-free quotients of Sym^j N_C^*, define Delta as the sum of the corrected normal-layer degree defects **including finite-point torsion**. Then

    n(lambda*d-L)=lambda*(n*d-2*M)+2*Delta.

The actual socle is omega_C tensor O_C(4-a-b). In particular lambda*d>=L. Equality forces the globally graded Gorenstein self-duality; a **constant graded algebra** additionally requires balanced rational conormal data.

**Proof:** research/notes/2026-10-13-evening-entirely-thick-rees-progress.md, sections 2-7. **Independent audit:** research/notes/2026-10-13-generalization-socle-independent-audit.md (PROVED, with clarifications). **Limitations:** necessary conditions only; no equality-obstruction theorem imported; for arbitrary C, lambda and Delta may be real, not integers. **Overlap:** not R-0019 or legacy first-blowup bounds. **Review request:** accept precise scoped statement and dependency list.

## Candidate B: constant first-relation embedded lifting obstruction

**Claim.** For a smooth rational C with balanced conormal O(-lambda) tensor V, assume an actual embedded thickening has first initial relation a **constant** binary form f of degree r and its next-order relations consist only of fV. For each factor m of f of multiplicity nonzero in the field, its quadratic direction class h_m must vanish. In characteristic zero all factors qualify. On fixed C0, accepted nonvanishing of every h_m excludes the zero-defect constant graded CI equality model; it does **not** exclude positive-defect or moving-first-relation strata.

**Proof:** research/notes/2026-10-13-generalization-thick-equality-geometry.md. **Independent audit:** research/notes/2026-10-13-generalization-thick-relation-obstruction-independent-audit.md. **Dependencies:** the accepted P-010 quadratic direction calculation and Candidate A for the equality corollary. **Overlap:** distinct from R-0010 and R-0013. **Review request:** promote general lifting lemma and fixed-C0 corollary with explicit dependence on inherited direction classes.

## Candidate C: normal-carrier index/socle compatibility

**Claim.** For a normal carrier surface along a smooth curve, with an actual mate cutting nC, at P let r be the actual local Cartier index of C dividing n and k=n/r. With the actual first-normal vanishing A_F,P and top ordinary-power/socle defects D_r,P and D_n,P, the characteristic-zero local formula is

    D_n,P=(k-1)A_F,P+k D_r,P.

The curvilinear CI ordinary filtration additionally satisfies pointwise 2*sum_i length(T_i)_P=n D_n,P. Combining these with inherited normal-carrier index arithmetic and fixed-C0 direction obstruction excludes normal C0 mate-bearing carriers when every actual on-curve Cartier index is at most four.

**Proof:** research/notes/2026-10-14-generalization-normal-index-socle-theorem.md. **Independent reconstruction:** research/notes/2026-10-14-generalization-index12-filtered-compatibility.md. **Inherited dependency:** research/notes/2026-10-14-generalization-normal-carrier-torsion.md; low-degree carrier exclusion R-0001; P-010 direction classes. **Limitations:** indices six/twelve and larger are not excluded; do not replace actual index by surface multiplicity or generic contact. **Review request:** consider separating local identity and bounded-index exclusion into two independently addressable records.

## Candidate D: pointwise conductor and socle defect

**Claim.** In characteristic zero, let Y=(F,G) be an actual CI supported on a smooth C; assume X=(F) is integral and generically regular along C, with finite normalization S and full inverse support a single smooth Cartier c isomorphic to C; S is smooth along c. Assume the actual conductor is invertible O_S(-B) near c with no component c. If A is the zero divisor of the full transverse differential, and J^(n-1)=Soc(Y)(-D_n), then as **actual divisors**

    D_n=(n-1)A-B|c.

**Independent proof:** research/notes/2026-10-14-generalization-pointwise-conductor-socle-independent-audit.md. **Inputs:** research/notes/2026-10-14-generalization-transverse-socle-independent-audit.md and research/notes/2026-10-14-generalization-projection-conductor-jacobian-bridge.md. The latter derives the local residue identity D_F=B|c+A but originally requested independent review; the pointwise audit reconstructs the needed conductor comparison. **Limitations:** not applicable to multiple inverse branches, non-Cartier lifts, or carriers singular generically on C. **Review request:** accept exact divisor statement only with all normalization hypotheses.

## Explicit nonpromotions

The October 14 ribbon independent review accepts the symbolic construction and conditional inequalities but explicitly reserves root acceptance. Keep in review queue; preserve the corrected monotonicity sign condition. The quintic endpoint and degree-15 local-cohomology results remain scoped evidence candidates.

## Authority checklist before canonical writes

1. Record an explicit claim-level acceptance decision and confirm source/audit dependency closure.
2. Assign stable new result IDs only after acceptance; do not assume the next number from this packet.
3. Use research/RESULT_SCHEMA.md metadata, exact characteristic and normalization hypotheses, evidence and limitations.
4. Update research/results/INDEX.md and applicable frontier navigation only with accepted records.
5. Preserve the unrestricted C0 STCI question as open.
