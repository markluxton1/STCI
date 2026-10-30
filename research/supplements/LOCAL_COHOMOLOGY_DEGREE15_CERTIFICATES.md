# local cohomology degree15 certificates

Permanent subject dossier retaining full mathematical computations, counterexamples, proofs, precise hypotheses and unresolved scope. Computational implementations, where present, remain separate.

---

## 2026-10-14-localcoh-polynomial-scaling-design

# Optional polynomial scaling for the degree-15 pencil block

Status: a new exact source-polynomial transformation design, not an invertibility
certificate, rank proof, or full-fiber exclusion. The main recovery subsequently
inverted the simpler common-denominator block in about five seconds; this design
is retained as a reusable option, not a replacement for that successful path.
No inherited rank or tensor verifier was replayed in producing it.

The selected 17 by 17 block is specified by the existing modular index-selection
record. That modular record selects rows and columns only. All calculations below
use the characteristic-zero rational source of attempt03.

Every seed denominator is a rational constant times powers of k-1 and k+1.
The common denominator (k^2-1)^9 therefore clears the seed denominators. Exact
polynomial arithmetic first forms this common numerator matrix, then measures
the valuations of each nonzero entry at k=1 and k=-1. For each of the two places,
integer row and column exponents are chosen to satisfy

    row_exponent[i] + column_exponent[j] >= pole_order(B[i,j]).

The Hungarian assignment dual supplies a minimum total exponent cover of this
inequality system. Negative column exponents are permitted: polynomial
cancellation in the source verifies that the final scaled entries remain
polynomials. Rational numerical denominators are then cleared row by row.
The resulting integer polynomial matrix P has the form

    P = D B E.

The JSON records all diagonal factors and all integer coefficients of P in
increasing degree order. It has 150 nonzero entries, maximum entry degree 21,
and total determinant scaling degree 152 (77 at k=1 and 75 at k=-1).
Clearing (k^2-1)^9 independently in all 17 rows instead uses degree 306.
These figures concern input representation only; they do not bound the cost of
inversion or prove that the selected determinant is nonzero.

If an inverse of P is subsequently certified, then

    B_inverse = E P_inverse D.

This identity must still be checked in the intended field; the design by itself
supplies no inverse. The factors k-1 and k+1 must be verified to be units in that
field before transporting an inverse.

An additional exact simplification is that source row16 has precisely two
nonzero entries, both -1, in source columns6 and0. Hence the column operation
column0 := column0-column6 gives a constant pivot and removes one row and one
column. No further entire constant row appears immediately after that step.
The saved peeling record is a design for this operation; it is not a determinant
calculation.

Artifacts:

- [Reproducible scaling-design script](../computations/general_localcoh_degree15_polynomial_scaling_design_2026_10_14.py).
- [Scaled polynomial matrix and diagonal factors](../validation/2026-10-14-localcoh-degree15-polynomial-scaling-design/selected-block-scaled-polynomials.json).
- [Constant row peeling record](../validation/2026-10-14-localcoh-degree15-polynomial-scaling-design/constant-row-peel.json).
- [Original index-selection diagnostic](../computations/general-localcoh-degree15-sparse-block-2026-10-14-diagnostic.json).

The script uses Python standard-library exact rational polynomial arithmetic.
Its divisions assert exactness, and its scaling potentials assert every required
entrywise denominator inequality. It neither starts nor stops a CAS job.


---

## 2026-10-14-localcoh-degree15-single-block-strategy

# Degree15 local-cohomology: specialize first and reuse one exact inverse

## Scope and current status

This is a computational-strategy record, not a new exclusion theorem. The
accepted rational family2 pencil and its original tensor interpretation are
premises. No accepted verifier has been rerun. The degree15 factor still needs
a characteristic-zero normalized dual and its new, independent tensor-identity
check before its fifteen roots can be removed from the incidence frontier.

The generator has prepared
[attempt04 source](../computations/general-localcoh-family2-degree15-corank-one-2026-10-14-attempt04.m2)
and its
[prepared lineage](../validation/2026-10-14-localcoh-degree15-attempt04/prepared-lineage.json).
Preparing the source did not launch or stop a long computation. The root agent
owns any subsequent execution and its execution record.

Operational update: the root launched attempt04 before the final scalar
normalization correction below was delivered, then retired that execution
and prepared attempt05 from the final attempt04 source. The final source
hash is `867f0017977fea4485331ef124c3a78ac45cd34484871d47d3903e6f4c7475aa`.
It is frozen and must not be edited during a run. Execution should use a saved
validation source snapshot; the root's attempt05 execution record determines
the actual executed source and process status. No earlier attempt label or
prepared-source record is a proof of successful execution.

## Why a new route is useful

Attempt03 first performs elimination over QQ(k), then specializes its results
to the degree15 field. Its first rank computation is expensive, and subsequent
kernel and transpose-lift computations repeat elimination. An unrelated,
bounded Macaulay2 syntax check also found that the expression
`matrix(q,1,(ii,jj)->0_K)` has no supported method in the installed M2 1.26.06;
the old source would fail when it reached its dual coefficient construction.
The live source was not edited by this strategy task. Attempt04 uses the
tested constructor `(matrix apply(q,ii->{0_K}))` instead.

A second bounded toy check found that the nonhomogeneous polynomial maps can
retain degree metadata making `transpose NN*UU==matrix{{1_R}}` false even
when its sole entry is exactly1. The final source instead asserts the exact
required scalar identity `(transpose NN*UU)_(0,0)==1_R`. The
[full dual toy](../validation/2026-10-14-localcoh-degree15-attempt04/bounded-dual-syntax-test.json)
and
[quadratic Bezout toy](../validation/2026-10-14-localcoh-degree15-attempt04/bounded-quadratic-syntax-test.json)
both pass with this correction. These tests exercise the constant-linear
and nonconstant-linear/quadratic normalization branches in unrelated small
QQ matrices; they make no degree15 mathematical claim.

The new route specializes all thirty seed coordinates first and explicitly
checks their twenty-five nontrivial denominators in the full degree15 field.
It computes one selected17x17 block inverse and derives every required vector
and transpose lift from it. It never invokes a generic rank computation,
kernel computation, or repeated transpose solve.

## The selected block is a diagnostic choice

The bounded standard-library
[selector](../computations/general_localcoh_degree15_sparse_block_2026_10_14.py)
uses the quotient F_p[k]/f15 with p=1000000007. Every modular pivot must be a
unit in that quotient. It selected the following row and column lists in
0.193 seconds:

```text
rows    = 0,16,7,8,17,12,5,18,4,19,49,13,11,14,20,54,55
columns = 17,6,5,16,0,7,4,1,13,8,10,2,3,9,11,12,14
missing column = 15
```

The original17x17 block has150 nonzero entries. These numerical choices are
stored in the
[diagnostic record](../computations/general-localcoh-degree15-sparse-block-2026-10-14-diagnostic.json).
Its output selects indices only; no modular rank or finite sample is being
accepted as mathematical evidence for an exclusion. Attempt04 certifies both
left and right inverse identities in characteristic zero before using this
block.

## The reusable exact construction

Let I and J be the selected row and column lists, let l be the missing column,
and set M=B[I,J]. Embed M inverse into an18x56 matrix D, with zero row l and
zero columns outside I. Define E=e_l transpose and h=(I18−DB)e_l. The exact
assertions are

```text
M M^-1 = M^-1 M = I17,
h_l = 1,
B h = 0,
D B = I18 − h E.
```

Together these certify rankB=17 in the full degree15 field and provide the
required right-inverse complement. For every row r satisfying r h=0, the
identity r D B=r supplies its transpose lift without another elimination.

Set a=A h. The source checks a nonzero2x2 minor of (h,a) in the same exact
field, constructs Fh and Fa with

```text
Fh h=1, Fh a=0, Fa h=0, Fa a=1,
```

and checks the actual target equation Bc=w with c=Dw−h Fh Dw. It also verifies
the full complement identity D0 B=I18−h Fh for D0=(I18−h Fh)D. A failed
denominator, inverse, complement, observability, or target check preserves an
exceptional case; it is not interpreted as an exclusion.

The sixteen linear duals use rows r annihilating h and a and have coefficient
vectors (r transpose, −(r A D) transpose) and
(0, −(r D) transpose). The quadratic dual uses Fh, Fa and the corresponding
three lifts through D. These are the already recorded abstract corank-one
construction, with no generic-field elimination hidden in a lift operation.
All seventeen annihilation identities are then checked in K15[lambda].

## Required final certificate

The source prints the full univariate target evaluation ideal. It constructs
a normalized dual only if that ideal is the unit ideal, and checks both
n transpose L=0 and n transpose U=1. It transports the dual back through the
accepted rational row transformation T and asserts original coordinate72 is
exactly1. No degree15 exclusion is claimed from the preparation, modular
diagnostic, or canonical-pencil calculations alone.

After exact source success, the new-certificate verifier can be run as:

```text
python3 research/computations/general_localcoh_family2_degree15_corank_one_certificate_2026_10_14.py --stem general-localcoh-family2-degree15-corank-one-2026-10-14-attempt04
```

That verifier consumes the accepted original tensor interpretation, checks
the normalized degree-at-most2 dual and all eighteen actual tensor-column
identities modulo the entire degree15 polynomial, and binds source/output
hashes. Its new `--stem` argument preserves the former attempt02 default and
allows separate attempt03/04 lineages. It does not rerun accepted tensor,
top-map, or rank29 verifiers.

Actual arithmetic cost remains unknown. The new route removes symbolic
QQ(k) coefficient growth and replaces the former repeated elimination with
one17x17 inverse, followed by matrix products and univariate degree-at-most2
operations. This is a structural reduction in work, not a wall-clock promise.


---

## 2026-10-14-localcoh-degree15-fractionfree-certificate

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
