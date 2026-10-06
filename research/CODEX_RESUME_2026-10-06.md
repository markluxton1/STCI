# Codex resume handoff — 2026-10-06

This branch resumes the interrupted `ultra_mode` research workspace on top of the independently audited main branch.

**Authoritative status:** `research/AUDITED_STATE_2026-10-06.md`. If restored exploratory material conflicts with it, the audited state controls. The original `ultra_mode` branch remains untouched as the exact historical snapshot.

## Changes established after the interruption

- Uniform order-one structure is proved; quartic carriers have e=0,1,2 with audited early-defect bounds, and arbitrary order-one carriers have e<=6.
- Primitive e=2 quartic work was completed and independently audited: on the universal fourth-obstruction locus, the canonical primitive triple has a distinguished cubic T and `H^0(I_{C_3}(4))=T H^0(O(1))`. Thus e=2 branches of (4,7) and (4,8) are excluded.
- The dx=1/P-044 residual classification is **OPEN**: multivariate resultant coprimality did not prove emptiness; an exact saturation/unit-ideal certificate is still required.
- Local cohomology: finite order-four reduction, 74x18 incidence specification, e<=2 direction bound, first-conormal image, and several subfamily exclusions are retained; the full bilinear incidence problem/general e=2 charts remain **OPEN**.
- Normal quartic exclusions are audited; remaining rational-resolution B1/B2/B3/D cases are finitely bounded/compressed, not excluded.
- MF6 pairing/divisor identities are audited; e=0 has d2>=3 and the nonregular (3,6) branch is excluded; the (4,5) exceptional incidence locus remains **OPEN**.
- Split-carrier calculations are reductions, not complete exclusions; the totally ramified [2,2] survivor family remains **OPEN**.
- The smooth rational quartic STCI problem and the entirely-thick branch remain **OPEN**.

## Restored Codex workspace

Useful unfinished material from `ultra_mode` is restored here: general/chart e=2 local-cohomology incidence experiments, direction-contact/parity experiments, generated symbol/tensor data, MF6 type-4 exploration, split-carrier exploration, and primitive-e=2 generation/contact scratch. These are research leads, not canonical results.

Known-faulty `localcoh-symbol-paritycheck.m2` and `localcoh-symbol-seedcheck.m2` are intentionally absent; their quartic-basis construction was wrong.

Before resuming an interrupted calculation, read the canonical audited state and the relevant retained note. Prefer geometric/algebraic arguments over proliferating brute-force cases. Do not modify `main` directly.
