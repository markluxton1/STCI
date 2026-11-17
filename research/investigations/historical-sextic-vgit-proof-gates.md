# Historical sextic ADE and VGIT: unresolved proof gates

**Status:** Recovery adjudication complete; the mathematical claims below are **not certified**. The original sources and executable checks remain available in Git history on `recovery/gemini-audit-worktree`. This record prevents loss of potentially useful mathematics without promoting unsupported conclusions.

## Sextic ADE — fixed-pencil contact classification

Historical source: `research/supplements/SEXTIC_ADE_REDUCTION.md`.
Historical checker: `research/computations/verify_sextic_triple_toric_vgit.py` (26,061 characters).

The source asserts torus weight decompositions for primitive-triple sextic equation spaces, the bilinear contact tower `Omega_3, Omega_4, Omega_5`, exhaustive treatment of 153 torus-fixed weight pairs, three isolated coprime pencils surviving contact through order five, and their exclusion by order-six colength six. The checker has functions for the decomposition, contact tower, quintic common-factor hull and fixed-pencil cases; its `main()` calls those functions. **It was inspected but not executed or independently proved in this recovery audit.** In particular, a classification of fixed pencils does not exclude moving pencils with a common-factor fixed limit.

Preserved canonical material: the intrinsic kernel and local cubic-contact quotient in `research/arguments/carriers/sextic_ade_reduction.md` (recovery commit `df344e1`), with the higher-order classification explicitly labeled unpromoted. The original ADE reduction and its hypotheses remain separately documented in the canonical carrier argument.

**Gate:** Check the precise orbit hypotheses and global-to-local comparison; rerun/reconstruct the exact certificate and confirm exhaustive fixed-pencil coverage before promoting the higher-contact claim. No new STCI exclusion follows at present.

## VGIT — common-factor blowup

Historical source: `research/synthesis/vgit_surface_pairs_and_full_limits.md`.
Historical checker: `research/computations/verify_vgit_surface_pairs.py` (13,480 characters).

Preserved canonical material: the exact degreewise common-factor rank-loss formula and the prime-ideal carrier/coprime-pencil dichotomy in `research/arguments/torus_hilbert_boundary.md` (recovery commit `456db66`).

**Identified proof defect:** The source's §8.3 infers that `(DA,DB,G)=(D,G)∩(A,B)` from `gcd(A,B)=gcd(D,G)=1`, with `G∈(A,B)`. This is not valid without an additional condition such as `D` regular modulo `(A,B)`. A counterexample is `A=x, B=y, D=x+y, G=xy(z-w)`: both gcd conditions hold, but `D∈(A,B)`, so the asserted equality fails. The counterexample concerns the general algebraic implication, not necessarily the restricted quartic-containing locus. The historical checker tests two specific `e=4,5` examples in degrees 6 through 13, not the general theorem. The full blowup resolution and exhaustive secondary-indeterminacy classification are **not established** by this audit.

**Gate:** Establish the missing height-three/nonzerodivisor hypothesis on the intended geometric locus, or stratify the failure locus and state a restricted theorem. Then verify the claimed morphism extension independently of first-order normal directions and the proposed completeness of the secondary strata.

## Disposition and dependencies

Both historical files are **adjudicated as partially integrated with explicit unresolved proof obligations**. They need not remain open in the historical *inventory* once these obligations are tracked here, but their claims must not be labeled verified, canonical Results, or used to exclude the characteristic-zero STCI problem. Retain the recovery branch or other durable Git references until any needed certificates are migrated. This investigation is the single forward-looking record for these two proof gates; avoid reopening the entire 69-source recovery audit merely to continue mathematical research.
