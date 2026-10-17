# Degree15 full-fiber exclusion by fraction-free polynomial arithmetic

## Exact result and scope

**New result, verified in the original tensor.** In the accepted second rational
endpoint family of the quartic-ancestor local-cohomology incidence, every root
of

\[
\begin{aligned}
f_{15}(k)={}&243k^{15}+810k^{14}+2646k^{13}+990k^{12}-9465k^{11}
-54222k^{10}-114414k^9-166406k^8\\
&-34359k^7+301686k^6+897946k^5+1296458k^4
+1345117k^3+811630k^2+285598k-610
\end{aligned}
\]

has no affine lower lift satisfying the actual tensor incidence. The new
certificate is a polynomial vector \(n(k,\lambda)\) with 74 coordinates,
reduced modulo the **entire** polynomial \(f_{15}\), satisfying

\[
 n^T L_{\rm actual}(k,\lambda)=0,\qquad n_{72}=1.
\]

The generated vector actually has degree at most **one** in \(\lambda\).
The inherited general corank-one construction allows degree two. These
identities exclude the target for every affine \(\lambda\), including at all
fifteen algebraic roots; this is not root sampling or a numerical rank test.

The accepted cubic and quartic field certificates are premises and were not
rerun. Combining their seven roots with this new certificate removes all
22 finite exception roots in this specific second rational family. This
statement does not enlarge the accepted quartic-ancestor incidence to
arbitrary carriers, change the other family's scope, or resolve the universal
STCI question. The established projective lower-lift boundary remains an
inherited separate premise.

## Why the arithmetic route changed

Attempt05 stalled while inverting a selected 17 by 17 block directly in the
degree15 number field. Its missing process handle and PID do not supply a
successful exit or a failed mathematical assertion. The new attempt06 is a
different computation: solve over integer polynomials first, then specialize
one certified rational inverse. No inherited tensor, rank29, top-map, cubic,
or quartic verifier was replayed.

Let \(M=B[I,J]\) be the previously selected block of the accepted rational
pencil

\[
 L_{\rm can}=\begin{pmatrix}\lambda I_{18}+A\\B\end{pmatrix}.
\]

Exact rational-function arithmetic clears its denominators by

\[
 d(k)=8141785875300\,(k^2-1)^9,\qquad P=dM\in M_{17}(\mathbb Z[k]).
\]

Each entry of \(P\) has degree at most18 and coefficients of at most59 bits.
FLINT computes an integer polynomial matrix \(N\) and polynomial \(D\)
with

\[
 PN=NP=D I_{17}.
\]

Both identities were checked over \(\mathbb Z[k]\), before specialization.
The resulting \(D\) has degree280. Polynomial extended gcd computations
then check that both \(d\) and \(D\) are units modulo \(f_{15}\), and set

\[
 M^{-1}=dN D^{-1}\pmod{f_{15}}.
\]

Both specialized inverse identities were also checked. Thus the diagnostic
row/column selection is certified in characteristic zero before use.

This removes repeated division by growing algebraic-field pivots. The exact
polynomial inversion and its identity checks took5.201 CPU seconds in this
run. This is an observed cost for this matrix, not a general complexity or
performance claim. The optional [row/column scaling design](2026-10-14-localcoh-polynomial-scaling-design.md)
can further reduce degree growth in related computations; it is unnecessary
for the successful certificate here.

## Construction and normalization of the dual

Embed \(M^{-1}\) into an18 by56 matrix \(D_B\), using the selected rows and
columns and zero on the missing column complement. With missing column
\(l=15\), set

\[
 h=(I-D_BB)e_l,\qquad a=Ah.
\]

The program checks

\[
 Bh=0,\quad h_l=1,\quad D_BB=I-he_l^T,
\]

then constructs \(F_h,F_a\) with

\[
 F_hh=1,\quad F_ha=0,\quad F_ah=0,\quad F_aa=1.
\]

It checks the actual bottom target compatibility and constructs the accepted
sixteen linear duals and one quadratic dual using multiplication by
\(D_B\), without Gaussian elimination. Every coefficient of all17
annihilation identities is checked in \((\mathbb Q[k]/f_{15})[\lambda]\).

In this instance the first two linear target evaluations
\(\ell_i=\alpha_i+\beta_i\lambda\) suffice. Their incompatibility is
certified by a unit denominator in the same full quotient. The normalized
dual is the corresponding constant linear combination

\[
 n=\frac{\beta_0 n_1-\beta_1n_0}
          {\beta_0\alpha_1-\beta_1\alpha_0}.
\]

The program checks \(n^TL_{\rm can}=0\), \(n^TU_{\rm can}=1\), transports
through the accepted constant row transformation \(T\), and checks original
coordinate72 equals1. Generation took0.966 CPU seconds. This stage consumes
the inherited tensor interpretation; it does not establish that interpretation
again.

## Independent original-tensor verification and evidence

The existing new-certificate verifier independently reconstructs the actual
74 by18 tensor matrix from the accepted tensor and family seed files. Using
only Python standard-library `Fraction` and polynomial arithmetic, it checks
all18 complete polynomial column identities modulo \(f_{15}\), the degree
bound, and the exact target normalization. It exited0 after approximately
5.6 seconds. Its identity-checking body is unchanged; a backward-compatible
`--generator-file` option was added only to bind actual C and input provenance
instead of assuming an M2 generator.

The primary evidence is:

- [Normalized original-tensor dual](../computations/general-localcoh-family2-degree15-corank-one-2026-10-14-attempt06-dual.txt).
- [Independent tensor certificate](../computations/general-localcoh-family2-degree15-corank-one-2026-10-14-attempt06-certificate.json).
- [Independent verification execution record](../validation/2026-10-14-localcoh-degree15-attempt06/verification-execution-record.json) and [successful output](../validation/2026-10-14-localcoh-degree15-attempt06/verification-stdout.txt).
- [Exact inverse execution record](../validation/2026-10-14-localcoh-degree15-attempt06/execution-record.json), [specialized inverse](../validation/2026-10-14-localcoh-degree15-attempt06/field-inverse.txt), and [compressed polynomial inverse](../validation/2026-10-14-localcoh-degree15-attempt06/polynomial-inverse.txt.gz).
- [Dual generation execution record](../validation/2026-10-14-localcoh-degree15-attempt06/dual-execution-record.json) and [all obstruction evaluations](../validation/2026-10-14-localcoh-degree15-attempt06/obstructions.txt).
- [Polynomial input preparer](../computations/general_localcoh_degree15_fractionfree_prepare_2026_10_14.py), [FLINT inverse source](../computations/general_localcoh_degree15_fractionfree_inverse_2026_10_14.c), [dual input preparer](../computations/general_localcoh_degree15_fractionfree_dual_prepare_2026_10_14.py), and [FLINT dual source](../computations/general_localcoh_degree15_fractionfree_dual_2026_10_14.c).
- [Independent verifier](../computations/general_localcoh_family2_degree15_corank_one_certificate_2026_10_14.py).

All three new computation stages have terminal exit0 records and empty
stderr. Frozen source snapshots are kept in the attempt06 directory. The
19,189,736-byte polynomial inverse was compressed to avoid a large raw text
file; the [archive manifest](../validation/2026-10-14-localcoh-degree15-attempt06/polynomial-inverse-archive.json)
binds both raw and compressed hashes and the exact decompression round trip.
Hashes bind provenance; the displayed polynomial identities and independent
original-tensor identities provide the mathematical evidence.

To verify this **new** certificate when a fresh check is justified:

```sh
python3 research/computations/general_localcoh_family2_degree15_corank_one_certificate_2026_10_14.py --verify --stem general-localcoh-family2-degree15-corank-one-2026-10-14-attempt06
```

No new exceptional-field or parameter-chart search was opened after this
certificate. The reusable advance is the fraction-free polynomial inverse
followed by a single quotient-field scalar inversion; the scoped mathematical
advance is completion of this family's fifteen previously pending roots.
