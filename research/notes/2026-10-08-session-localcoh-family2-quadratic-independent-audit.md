# Independent audit of both family2 quadratic exception fibres

Date: 2026-10-08. Scope: characteristic zero, the fixed rational quartic
`C0=[s^4:s^3t:st^3:t^4]`, the second primitive degree-two endpoint
direction family, and all its lower correction parameters at the roots
of `k^2+1` and `k^2-2k-1`. Auditor: a separate agent from the coefficient
certificate producer. No original coefficient certificate, generation
source, or canonical frontier document was edited.

## Verdict

**PROVED under the previously audited local-cohomology interpretation:**
the two roots of each quadratic, four geometric direction parameters in
total, exclude target `u` for **every** affine lower correction `lambda`.
The producing verifier passed an isolated replay with all thirteen input
files frozen. A separate implementation using SymPy algebraic-number
domains passed all exact polynomial identities without importing the
producing verifier or regenerating its coefficient certificates.

Together with the previously accepted generic family2 certificate, these
exclusions reduce that certificate's retained primitive direction locus
from 26 points to 22 points, of degrees `3+4+15`. Each remaining point
retains its entire affine `lambda` fibre. These are unresolved certificate
exceptions; no surviving incidence or ancestor is inferred. The other
endpoint families, nonendpoint top zeros, unrestricted quartic incidence,
and the global STCI problem remain outside this conclusion.

## Actual forms, top map, and complete parameter fibre

The independent
[`countercheck.py`](../validation/2026-10-08-family2-quadratic-audit/countercheck.py)
parses the displayed stage-four ancestor numerators and quartic forms in
[`localcoh-incidence-bases.txt`](../computations/localcoh-incidence-bases.txt).
It verifies the quartics are the following **actual degree-four forms**:

```text
q=xw-yz, A=x^2z-y^3, B=xz^2-y^2w, C=yw^2-z^3;
q*(x^2,xy,xw,yz,zw,w^2),
A*(x,y,z,w), B*(x,y,z,w), C*(x,y,z,w).
```

They all vanish on `C0` and have independent coefficient vectors of rank
18. The restriction of the 35 degree-four monomials to `C0` has rank 17,
so the displayed forms span exactly the full degree-four ideal piece.
They are not four-coordinate generator rows mistaken for polynomial forms.

The checker independently substitutes `x=1,y=t,z=t^3+a,w=t^4+ta+q`
in every actual ancestor numerator. It extracts its normal-order-three
part, converts it to the previously audited balanced normal coordinates,
and computes all four degree-six residues. All thirty top columns match
the saved top map literally. The resulting `32x30` matrix has rank 29.
Its nonzero rational kernel vector is exactly the lower slope in the
family2 seed. Consequently every lift of the specified nonzero pure top
is the full affine line

```text
alpha(k,lambda)=a*(k)+lambda*k0.
```

At each quadratic field, all thirty constant seed coefficients and all
thirty slopes are compared directly to the rational family2 source, and
all six direction coefficients are compared to the same source. Every
source denominator is inverted only after checking it is a unit modulo
the defining quadratic. All 32 coefficients of the specified actual
normalization `t*p^i*r^(3-i)`, `i=0,1,2,3`, match the top of `alpha`.
Thus no lower parameter is lost through sampling or a generic-rank
argument. The projective limit with zero top is a different stratum,
not a lift of this fixed nonzero top.

The independent fixed-size homogeneous Sylvester determinant is nonzero
in each field even though `r` loses its quadratic coefficient there:

| Field | Chosen exact embedding | Homogeneous resultant |
|---|---|---|
| `QQ[k]/(k^2+1)` | `k=i` | `-8i` |
| `QQ[k]/(k^2-2k-1)` | `k=1+sqrt(2)` | `-96+68sqrt(2)` |

The second norm is `-32`, so neither conjugate resultant vanishes. Both
quadratics are coprime to the chart-pole factor and homogeneous
nonprimitive factors. These four parameters are admissible primitive
directions, not excluded chart or normalization points.

## Independent field and polynomial dual checks

The original verifier uses rational coefficient pairs and an AST parser.
The new countercheck instead uses SymPy's algebraic-number domains
`QQ(i)` and `QQ(1+sqrt(2))`, reducing rational source expressions by
polynomial remainders and extended inverses. It does not import any
helper from the original verifier. It also compares all 74 entries of
each raw Macaulay2 dual directly with the saved coefficient certificate.

In each field the dual has 27 nonzero entries and degree two in `lambda`.
The tensor is read as a sparse `74x542` matrix with header
`30 18 74 542`; its last two target columns are checked to be exactly
`e72,e73`. For each of the eighteen multiplier columns, the new checker
forms its image from **all thirty ancestor coordinates**, multiplies it
by the full dual, and verifies that every coefficient through degree
three in `lambda` is zero:

```text
n(lambda)^T L(alpha(lambda))=0,    n(lambda)^T u=1.
```

If `L(alpha)*x=u`, these exact identities would give `0=1` after left
multiplication by `n`. One valid dual is sufficient; correctness does
not depend on trusting a claim that the exported vector spans an entire
left kernel or that the producing module computation was exhaustive.
There are no `lambda` denominators, so specialization creates no
additional exceptional lower parameters.

The defining quadratics have discriminants `-4` and `8`; both are
irreducible and separable over `QQ`. The identities transport through
both embeddings into any algebraically closed characteristic-zero
field. Every inverted field unit remains nonzero under each embedding.
This establishes all four geometric roots, rather than just the two
chosen exact embeddings used by the independent arithmetic implementation.

## Durable execution record

The independent countercheck completed in tool session `19588` with exit
code zero. Its source, output, and full input hashes are in
[`countercheck-result.json`](../validation/2026-10-08-family2-quadratic-audit/countercheck-result.json)
and the retained
[`countercheck.log`](../validation/2026-10-08-family2-quadratic-audit/countercheck.log).
Its source SHA256 is

```text
88e8aa6072fd93074453a2fe6fbef710bc3b6a2273151f12d00320233c095334
```

The unchanged original verifier was copied with all its input closure
into a separate snapshot and ran with exit code zero in 0.082 seconds.
The snapshot's thirteen input hashes were unchanged after execution.
Reproduction and its terminal record are in
[`isolated-replay.py`](../validation/2026-10-08-family2-quadratic-audit/isolated-replay.py),
[`isolated-replay.log`](../validation/2026-10-08-family2-quadratic-audit/isolated-replay.log),
and
[`isolated-replay-manifest.json`](../validation/2026-10-08-family2-quadratic-audit/isolated-replay-manifest.json).
The replayed original verifier SHA256 is
`a1168854beed0d56838851710444a5d2d35ef835333f9ab179d2163f23739ea3`;
its output SHA256 is
`69a490fc61abf1fe30a932b6e84f5707470db7e47806aef71921fb4f10dd1aed`.

Reproduce the additional independent check from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/validation/2026-10-08-family2-quadratic-audit/countercheck.py
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/validation/2026-10-08-family2-quadratic-audit/isolated-replay.py
```

The producing agent's independent evidence and original process history
are retained in the
[quadratic proof note](2026-10-08-session-localcoh-family2-quadratics.md).
The absent parent-local handle for one producing process was not treated
as a failed computation or used to infer a live process. Acceptance here
comes from the exact identities and new terminal executions.

## Fresh reconstruction of the complete actual tensor

An additional independent Macaulay2 checker completed with exit code zero
in 0.840 seconds. Its
[`actual-tensor-reconstruction.m2`](../validation/2026-10-08-family2-quadratic-audit/actual-tensor-reconstruction.m2)
rebuilds the ancestor space from the Ext map, verifies that it has
dimension 30 and that the map is injective in degree `-7`, and sums all
four ideal-generator contributions to obtain actual quartic forms.
Every one of its thirty degree-thirteen ancestor polynomial entries and
eighteen quartic polynomial entries agrees literally with the frozen
displayed bases. It additionally verifies `I^4*h subset (q^4,B^4)` for
each ancestor and every generator of `I^4`.

All 540 actual ancestor-times-quartic product columns and the two target
columns are reduced modulo `(q^4,B^4)` afresh. Their full coefficient
matrix has rank 74, the product-only matrix already has rank 74, and
the independent compressed matrix is **literally equal** to the retained
`74x542` tensor. The union of the uncompressed coefficient rows and stored
rows also has rank 74. Thus no quotient equation or target row was lost
through compression. The entire degree `-3` stage-three Ext image is
independently reconstructed in the same quotient, its injection is
verified, and its union with the 540 product columns has rank 74. This
establishes actual equality with the complete next-stage image, beyond
merely matching its abstract dimension.

Its
[`actual-tensor-reconstruction.log`](../validation/2026-10-08-family2-quadratic-audit/actual-tensor-reconstruction.log),
[`terminal result`](../validation/2026-10-08-family2-quadratic-audit/actual-tensor-reconstruction-result.json),
and
[`frozen input manifest`](../validation/2026-10-08-family2-quadratic-audit/actual-tensor-input-manifest.json)
retain the exact evidence. Source SHA256:

```text
b2c4722f6d9b5d9ece43d5bfd38348527ceec7577832c37747263a8a9b85c187
```

Log SHA256:

```text
31188e3f9f4940157ed8286c3c3a9ef5a0cc94fa8a95ca299ab6183ee17c4700
```

Two earlier checker scaffolding failures are preserved separately: an
M2 sequence-versus-list mismatch and comparison of differently graded
matrices rather than their polynomial entries. Neither reported a
disagreement of a displayed polynomial or tensor entry. The final
checker uses entrywise polynomial comparison for the graded ancestor
matrix and performs the literal rational tensor comparison successfully.
The first passing source, log, and terminal result are also retained as
`attempt03-pass` records; the final source strengthens that pass by
identifying the complete next-stage image explicitly. The full tensor
development record is in
[`actual-tensor-provenance.json`](../validation/2026-10-08-family2-quadratic-audit/actual-tensor-provenance.json).

The combined
[`audit-manifest.json`](../validation/2026-10-08-family2-quadratic-audit/audit-manifest.json)
binds this note, the three successful final proof checks, their input
closures, the original generation history, and both retained scaffolding
failures. No process from this audit remains running.
