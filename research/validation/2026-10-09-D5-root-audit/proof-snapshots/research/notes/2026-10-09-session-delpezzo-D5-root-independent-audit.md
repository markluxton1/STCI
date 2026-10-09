# Root's independent reconstruction of the D5 torsion filter

Date: 2026-10-09. Auditor: root, separate from the construction owner
`delpezzo_d5_torsion_filter`. Status: **PROVED HERE / accepted at the
stated geometric and lattice scopes**. A further worker audit was
interrupted by the weekly usage limit before its final written record;
it is not counted as a completed audit. The argument below and the
separate signed-partition check supply this acceptance.

Audited source: [D5 torsion filter](2026-10-09-session-delpezzo-D5-torsion-filter.md).
The separate [genus-one reduction](2026-10-09-session-genus-one-delpezzo-reduction.md)
and [its independent ADE audit](2026-10-09-session-rational-genus-one-ADE-independent-audit.md)
establish its weak-del-Pezzo/ADE hypotheses for every sectional-genus-one
normalization of an integral nonnormal quartic containing fixed C0.
This audit does not exclude mates in both surviving singularity types.

## 1. The geometric class lies outside the exceptional lattice

On the minimal resolution M, L=-K_M is nef and big with L^2=4.
The hypothetical mate supplies a smooth reduced curve c on S,
isomorphic to C0, with b c~bH. Its strict transform c# is also smooth
P1 and L.c#=4. Adjunction gives c#^2=2. Hence the integral class

    Z=L-c#,       L.Z=0,       Z^2=-2

is a root in the anticanonical orthogonal lattice. Pullback of the
actual effective Cartier divisor b c expresses b Z as a nonnegative
integral combination of exceptional curves, so Z belongs to their
rational span and to its integral saturation. It has Z.E<=0 on each
exceptional prime because c#.E>=0.

The owner correctly retains that c is smooth downstairs, not only
that its abstract strict transform is smooth. If Z were an integral
exceptional combination, the quotient
Cl(S)=Pic(M)/<exceptional curves> would give c~H as Weil divisors.
This makes c Cartier. At a point of c, its regular one-dimensional
quotient local ring, together with one defining equation, gives at
most two generators of the surface maximal ideal. A two-dimensional
surface local ring there must consequently be regular. Thus c avoids
all singular points of S, and c# avoids every exceptional curve.
Then Z.E=0 on the entire exceptional lattice, so its negative-definite
intersection form forces Z=0, contradicting Z^2=-2. Therefore

    Z in sat(R) minus R.

This is the required missing-root condition. It fails if one drops
downstairs smoothness, so the geometric premise is material.

## 2. The entire integral orthogonal lattice is D5

A weak del Pezzo surface of degree four is the blowup of five points
of P2, allowing infinitely near points and using total exceptional
transforms. The primary author-hosted source is
[Dolgachev, Classical Algebraic Geometry, section 8.1.3](https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1334/2024/08/CAG.21.pdf).
Its definition and ensuing statement after Definition 8.1.18 give
the weak del Pezzo blowup model; the degree rules out F0 and F2
without blowups. The Picard group is free with intersection form
diag(1,-1,-1,-1,-1,-1), and L=3h-sum e_i is primitive of square four.
The orthogonal complement therefore has discriminant four.

The displayed five Picard roots in the owner note have negative
D5 Gram matrix, also of discriminant four. Their lattice consequently
equals the whole integral orthogonal complement. This discriminant
step rules out an unrecorded finite-index enlargement. Dolgachev's
Proposition 8.2.7 gives the same forty roots explicitly; root checked
both primary passages. A geometric effective ADE exceptional basis
generates a reflection-closed root subsystem of this forty-root system.

## 3. Reconstruction by signed connected components

Use the Euclidean pairing and D5={v in Z^5: sum v_i even}, reversing
the geometric intersection sign. For a coordinate-connected root
component, choose a spanning tree and switch signs so its tree roots
are differences u_i-u_j. Their reflections are transpositions along
a connected graph and generate every permutation of that block.
Consequently the subsystem contains all differences on the block.

If every other edge also becomes a difference, the block is A_(m-1)
with rational span sum epsilon_i v_i=0. If an edge becomes a sum,
permuting its coordinates produces all sums as well, giving the full
D_m block. This includes D2=2A1 and D3=A3. No third connected type
can occur in this coordinate-root model.

An integer vector in a balanced A block satisfying its signed-sum
equation belongs to that A root lattice. Its ordinary sum is even,
since signs have no effect modulo two. Each D block spans all its
coordinates rationally and has an independent even-sum condition
in the root lattice. The ambient D5 instead imposes just the total
even sum across all D blocks. With t nonempty D blocks the index
is 2^(t-1) when t>=1, and one when t=0.

A missing ambient root in the rational span cannot lie inside a
block: those roots are already present. If its two coordinates lie
in separate blocks, any balanced block gives a nonzero signed sum,
which excludes rational-span membership. Thus a missing root joins
two D blocks, and conversely every such root violates both separate
parities while satisfying the ambient total parity.

Each D block has at least two coordinates. On five coordinates two
blocks have sizes only (2,2) or (2,3). A further nontrivial block
cannot fit. These are exactly 4A1 and A3+2A1, with saturation D4
and D5 respectively, both index two. This is a direct completeness
proof, independent of the program's enumerated count.

## 4. Chamber, correction and parity

For the effective geometric exceptional roots, the inequalities are
z.alpha_i=-Z.E_i=c#.E_i>=0. In a D2 block with simple roots
u1-u2 and u1+u2, only +u1 among signed coordinate vectors satisfies
both inequalities. In a D3 block with simple roots u1-u2, u2-u3,
u2+u3, only +u1 does so. Therefore a missing root joining the two
blocks has exactly one dominant choice.

For 4A1 it is u1+u3, giving

    Z=(E1+E2+E3+E4)/2,       c#.Ei=1 for all four.

For A3+2A1 it is u1+u4. Here u1-u2 is the middle A3 root; the
other two D3 roots are its ends. This gives

    Z=E_mid+(E_left+E_right+F1+F2)/2,
    (c#.E_mid,c#.E_left,c#.E_right,c#.F1,c#.F2)=(1,0,0,1,1).

All coefficients are nonnegative, as required by the actual divisor
pullback. These corrections are the nonzero order-two classes in
sat(R)/R. Since b Z belongs to R, every hypothetical mate degree b
is even. This does not show that any even degree works.

## 5. Independent finite control and evidence boundary

The owner enumerates reflection closures and checks integer-lattice
membership with Hermite normal form. Root wrote a separate
[signed-partition countercheck](../validation/2026-10-09-D5-root-audit/countercheck.py)
using all 52 set partitions of five coordinates and all balanced
sign assignments or full D blocks. It uses neither reflection
closure nor Hermite normal form. It obtains the same 428 embedded
subsystems and checks rational-span membership and the separate
parities of every one of the forty ambient roots. Exactly fifteen
embeddings are 4A1 and ten are A3+2A1; their missing-root counts
are sixteen and twenty-four. Every other embedding is saturated.

Its terminal isolated execution passed in 0.091 seconds. The frozen
owner source also completed its separate isolated replay with exit
zero in 3.059 seconds. The terminal statuses, source snapshots, logs
and output hashes are in
[replay-manifest.json](../validation/2026-10-09-D5-root-audit/replay-manifest.json).
The written signed-component proof establishes the theorem; these
controls check its finite arithmetic representation. Neither process
remains running.

## 6. Combined accepted conclusion

Combining this lattice proof with the separately audited rationality
and genus-one del Pezzo reductions, every hypothetical quartic mate
for fixed C0 in the normalization sectional-genus-one lane requires
exactly one of the two complete exceptional types above, and an even
mate degree. All other ADE types in that lane are excluded. The
explicit four-A1 family has an additional all-degree exclusion by
full fibers, but other four-A1 projections and A3+2A1 remain OPEN.
Rational genus-two normalizations and higher carrier degrees also
remain OPEN. No unrestricted C0 or universal STCI conclusion follows.
