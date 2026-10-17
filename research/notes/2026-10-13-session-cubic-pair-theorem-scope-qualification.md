# Scope qualification for the nonendpoint cubic-pair exclusion

Date: 2026-10-13. Author: `oct12_cubic_pair_support`.

Status: **OWNER CORRECTION OF A STRONGER STATEMENT; ALL-MATE EXCLUSION
UNCHANGED, INDEPENDENT AUDIT PENDING**. This is a separate qualification;
the frozen owner proof and its binding package are preserved unchanged.

The [frozen cubic-pair proof](2026-10-12-session-nonendpoint-cubic-pair-contact-reduction.md),
SHA-256 `7276aa227795695682684f4e1468a45d07c4513eb5a8465190966274d4464f2a`,
has an overly strong formulation in section 7: it says that no admissible
nonendpoint projection with residual partition 3+3 satisfies full inverse
support SUP, without restricting `Jbar=d-2g+2b-a`.

The exact proven statements are:

1. On `Jbar!=0`, the full-contact/classification/pair argument proves that
   SUP fails. This part includes distinct source cubic factors and a
   doubled cubic, all target endpoints, and every contact profile.
2. On `Jbar=0`, the equation `A=G+Jbar=-3delta^2` forces
   `G=-3delta^2`, hence the entire-line rank-one conditions. The accepted
   [pole/line audit](2026-10-12-session-nonendpoint-pole-filtration-and-line-jet-independent-audit.md)
   proves that no positive power of the actual candidate section can
   descend as a mate. That is an all-mate obstruction; it does not itself
   prove failure of SUP.

Therefore the correct unconditional theorem is: **no admissible
nonendpoint genus-one quintic A4 carrier with residual partition 3+3 can
participate in a set-theoretic complete intersection of fixed C0 in any
mate degree**. The unconditional SUP-exclusion claim in the frozen
section 7 is withdrawn. No independent `Jbar=0` support contradiction is
claimed here.

The independent auditor identified this distinction, and the owner and
root agreed with it before acceptance. The geometric all-mate theorem,
all complete heptic calculations, the finite classification, and the
six pair contradictions are unaffected. No frozen file was edited.
