# CR-09 certificate inspection — 2026-10-26

**Disposition: source-and-output audit passed; no independent execution in this review.** Scope is the selected sextic F* and degree-16 mates only. This note inspects the saved Macaulay2 script, its execution log and metadata, and the separately implemented Python/C++ normal-division script and JSON. It does not claim a fresh run or an independently archived nonzero 683×683 minor.

## Source artifacts examined

- `computations/endpoint4_fixed_m2_2026_10_25.m2`: constructs the actual four-term F*, substitutes x=(1,z,z³+v,z⁴+u+3zv/2), reduces all 969 global degree-16 monomials modulo (F*,(u,v)^12), stacks 23-dimensional quotient maps, and checks global multiples.
- `computations/endpoint4_fixed_m2_2026_10_25.txt`: progressive rank 23 at z=1 through 667 at z=29 and 683 at z=30; final rank 683; zero product with multiples; independent multiple rank 286.
- `computations/endpoint4_fixed_m2_2026_10_25.json`: PASS, return code 0, 9.35 seconds, recorded script/log SHA-256, prime 65521, parameters rho=-1,a0=1,b1=b2=0,kappa=1, and explicit implementation corrections.
- `computations/endpoint4_fixed_jet_independent_2026_10_26.py`: separately expands homogeneous carrier, substitutes chart, reduces by leading u² relation, builds 690×969 matrix, checks each of 286 multiples, and calls C++ modular elimination.
- `computations/endpoint4_fixed_jet_independent_2026_10_26.json`: rank 683, nullity 286, 286 multiples annihilated, 30 good samples, matrix SHA-256 a3e546424d11200e1d8075c7f9d5d342787bd925a303901bd2b33b2661f56445.

## Verification of mathematical bridge

1. `dim H0(P3,O(16))=binom(19,3)=969`, `dim H0(P3,O(10))=binom(13,3)=286`; multiplication by nonzero F* is injective.
2. The local quadratic term is `z^8((1+z²)u²−z²v²/4)`. Over B=Z[1/2,z,z^-1,(1+z²)^-1], its u² coefficient is a unit. Reduction modulo (F*,(u,v)^12) has the 23 normal monomials `v^0,...,v^11,u,uv,...,uv^10`; all remaining monomials of total degree <12 reduce by an increasing-total-degree substitution, hence terminate.
3. Evaluation at z=1,...,30 modulo 65521 is defined: z and 1+z² are nonzero at these values. The 690-row stacked map is the specialization of the constant-global-coefficient jet map over the rational function field, not an enlarged rational-coefficient source.
4. Recorded rank 683 mod 65521 implies rank ≥683 in characteristic zero (some 683-minor survives); 286 independent multiples annihilated identically imply rank ≤969−286=683. Therefore the global kernel is precisely F*H0(O(10)), assuming the saved finite rank is authentic and correctly computed.
5. The M2 code checks `rank multipleCoefficients==286`, reconstructs `globalCarrier*monomial10` in the 969-row monomial order, and checks all entries of `stackedJets*multipleCoefficients` vanish. This specifically addresses the prior multiline assignment and monomial-order failures. The Python script constructs F* from its four terms independently and checks all 286 multiples at every sample.
6. The two programs use distinct quotient implementations (M2 quotient-ring coefficients vs recursive normal division); both report rank 683. Their shared input formula and samples are intentional, not a claim of independent random trials.

## Caveats

- The M2 script breaks on reaching rank 683 and asserts 690 rows, so the stored log is consistent with exactly 30 samples. A purported rank beyond 683 would contradict the known 286-dimensional kernel.
- The scripts' output records are internally consistent with their assertions. The audit did **not** recompute their SHA-256 hashes, execute M2/C++, or reconstruct the full matrix from the repository through GitHub; the saved rank is therefore **inspected and corroborated**, not freshly reproduced.
- The finite rank certificate is only a necessary jet-kernel statement; the fixed-carrier residual-degree conclusion additionally requires CR-10's nonsplit-node and finite-length argument.
- No universal claim for all sextics, other degree mates, or STCI follows.

## Adjudication update

**CR-09: accept as certificate-backed, source-inspected result, with independent rerun still desirable. CR-11: the local-to-global implication is established subject to that finite certificate.** This is sufficient for a candidate *single scoped result* for the selected F*, but a canonical promotion should explicitly disclose the saved-certificate status, or wait for independent execution according to repository policy.
