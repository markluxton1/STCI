# Independent actual quartic tensor reconstruction

Status: **COMPUTATIONAL EVIDENCE — exact independent reconstruction PASS.** This note binds the ambient polynomial tensor used by the family-two quadratic audit. It proves no global STCI statement and does not by itself prove the later parameter-specific dual identities.

The standalone source `actual-tensor-reconstruction.m2` freshly reconstructs the Ext-stage-four image over `QQ[x,y,z,w]`, using

- `q=x*w-y*z`, `a=x^2*z-y^3`, `b=x*z^2-y^2*w`, `d=y*w^2-z^3`, and `I=(q,a,b,d)`;
- the map `S/(q^4,b^4) -> S/I^4` and the degree-minus-seven part of its contravariant second Ext map;
- all four generator-coordinate contributions to each column of `basis(4,I)`.

The 30 reconstructed ancestor numerator polynomials have degree 13. The Ext map is injective in the relevant degree, and the checker explicitly verifies `I^4*h` lies in `(q^4,b^4)` for every ancestor and every generator of `I^4`. All 30 numerator polynomials and all 18 quartic polynomials agree literally, entry by entry, with the frozen displayed bases.

The quartic claim is independently checked against the full restriction map to `[s^4:s^3*t:s*t^3:t^4]`: the 35-dimensional ambient quartic space has restriction rank 17, and the reconstructed 18 columns are independent and restrict to zero. Thus these are the complete actual quartic forms, rather than generator-coordinate rows.

The source then reconstructs all 540 products in ancestor-major order modulo `(q^4,b^4)`, appends the two target columns `x*z*(q*b)^3` and `y*w*(q*b)^3`, and forms the full polynomial coefficient matrix. The product and combined coefficient matrices both have rank 74. The resulting 74-by-542 compressed rational matrix is **literally equal** to the frozen stored tensor; the combined stored/coefficient row space also has rank 74. Independently reconstructed degree-minus-three Ext-stage-three numerator images have dimension 74, are injectively embedded in the same Čech stage, and their union with the 540 products has rank 74. This identifies the entire next-stage image, rather than merely matching its dimension.

The final source is frozen and the terminal execution was PASS with exit code 0. It took 0.840027 seconds using Macaulay2 1.26.06. Execution metadata and hashes are in `actual-tensor-reconstruction-result.json`; frozen input hashes are in `actual-tensor-input-manifest.json`; the complete audit provenance is in `actual-tensor-provenance.json`.

Final source SHA256: `b2c4722f6d9b5d9ece43d5bfd38348527ceec7577832c37747263a8a9b85c187`.

Final execution log SHA256: `31188e3f9f4940157ed8286c3c3a9ef5a0cc94fa8a95ca299ab6183ee17c4700`.

Four development executions are preserved. Attempt 01 failed because Macaulay2's `apply` on a sequence returned a sequence where `matrix` required a list. Attempt 02 failed at a whole-matrix equality because the Ext matrix retains grading shifts while the text-loaded polynomial matrix uses ordinary polynomial degrees; a diagnostic showed all polynomial entries already agreed. Attempt 03 passed the full tensor comparison and checked the abstract next-stage dimension. The final strengthened source additionally compares the complete next-stage image with the product span, and passed. The failed checks are retained as checker-development failures, with no mathematical mismatch concealed. The separate API probe was diagnostic only.

No original computation source, original text certificate, or canonical research record was modified.
