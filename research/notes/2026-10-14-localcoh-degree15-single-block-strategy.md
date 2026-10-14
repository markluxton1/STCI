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
