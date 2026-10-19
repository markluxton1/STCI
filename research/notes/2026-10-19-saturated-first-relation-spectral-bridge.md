# A saturated first relation forces normal flatness: resultant and spectral bridges

Date: 2026-10-19.
Status: **PROPOSAL WITH INDEPENDENT REVIEW PASS; not promoted.**
Independent audit: [filtered-bridge review](2026-10-19-filtered-saturated-duality-moving-purepower-independent-audit.md).
Authors: root and filtered-algebra workers; independent filtered-bridge
reviewer. No canonical record is edited or promoted.

The main general theorem in section 8 removes the balanced-conormal assumption
from the bridge. Sections 1--7 retain the explicit spectral interpretation
in the split case. The proofs are compatible and use the same saturated
duality lemma.

## 1. Precise split-case claim

Let `C` be a smooth connected projective curve over an algebraically
closed field of characteristic zero, embedded in a smooth threefold
`X`. Assume

    E=N_(C/X)^*=H^(-1) tensor V,       dim_k V=2.

Let `Y` be an actual locally complete-intersection thickening with
`Y_red=C`, and put `J=I_C O_Y`. Suppose the FULL generic ordinary
initial ideal is a coprime binary complete intersection

    gr_(J_eta)(O_(Y,eta))=k(C)[x,y]/(f_r,g_s),
    2 <= r < s,                         gcd(f_r,g_s)=1.   (1)

Let `R=H^(-r) tensor M` be its ACTUAL first relation sheaf,

    R=ker(Sym^r E -> J^r/J^(r+1)),

and assume `R` is a line SUBBUNDLE of `Sym^r E`. Equivalently the
coefficient inclusion

    M subset Sym^r(V) tensor O_C

is saturated and is nonzero in every fiber. Write

    lambda=deg H,     epsilon=-deg M,     d=r+s-2.

The first coefficient form defines the FULL root scheme

    Z subset C x P(V^*),       pi:Z->C.

It is finite flat of degree `r`; it may be singular, reducible, or
nonreduced.

**Proposed conclusions.**

1. The first saturated relation forces an everywhere-coprime second
   quotient relation of degree `s` on this FULL root scheme.
2. More precisely there is a line bundle `T` on `C` such that

       O_Z(s) = pi^*(H^s tensor T),
       deg T=-s*lambda+s*epsilon/r.                     (2)

   Thus the spectral Picard criterion of STCI-R-0008 is a necessary
   condition for the ACTUAL generic-CI thickening under these hypotheses.
3. Every ordinary `J`-adic layer is locally free on `C`; every fiber of
   the ordinary associated graded algebra is a binary graded complete
   intersection of degrees `(r,s)`.

Conclusion 3 is a further rigidity argument after the core spectral
bridge. Its proof uses a nonsplit second-generator extension correctly;
no global second polynomial line is assumed.

For `C0` one has `C=P1`, `H=O(7)`. This theorem would bridge a much
broader first-root class than STCI-R-0006, while still requiring the FULL
generic initial ideal (1) and a saturated ACTUAL first relation. It does
not cover arbitrary actual STCI equations.

## 2. Dependencies and exact authority boundary

The spectral interpretation for abstract graded second quotient
relations is promoted as [STCI-R-0008](../results/spectral_root_picard_criterion.md).
Its proof and nonsplit-generator warning are in
[the original spectral note](2026-10-14-generalization-spectral-root-curve-relations.md)
and [its independent audit](2026-10-14-generalization-spectral-root-curve-independent-audit.md).
That promoted theorem alone does not provide an actual-CI bridge.

The new saturated-duality lemma, including its proof from actual
Gorenstein MCM duality, is in section 3 of
[the simultaneous pure-power proposal](2026-10-19-filtered-saturated-duality-moving-purepower-bridge.md).
The use below does not depend on pure-power, movement, or apolarity:
only the symmetric generic Hilbert function in (1) is used for perfect
saturated pairings. The actual socle line and local MCM duality are
accepted in [the socle audit](2026-10-13-generalization-socle-independent-audit.md).

All new assertions here remain unpromoted proposals. The linked independent
written review records PASS under the stated hypotheses. No accepted
computation is rerun.

## 3. Saturated filtration and exact early layers

Let `P_i` be the saturation of `J^i` in `O_Y`, and let

    B_i=P_i/P_(i+1),       S=Ann_Y(J).

Purity gives `J^(d+1)=0` globally. The saturation lemma gives vector
bundles `B_i`, a multiplicative saturated filtration, and perfect
actual multiplication pairings

    B_i tensor B_(d-i) -> S,
    B_(d-i)=B_i^* tensor S.                              (3)

For `j<r`, the actual initial relation kernel `K_j` is zero because it
is a rank-zero subsheaf of a vector bundle. For `r<=j<s`, one has

    R tensor Sym^(j-r)E subset K_j.

This product is a saturated subbundle of `Sym^j E`: in every fiber,
multiplication by the nonzero binary form `f_r` is injective with the
same rank. The generic rank of `K_j` is exactly that of this subbundle
by (1). The quotient between them is therefore zero. Hence

    K_j=R tensor Sym^(j-r)E,                 r<=j<s.     (4)

All ordinary layers through degree `s-1` are consequently vector bundles,
and successive extension gives

    P_i=J^i for i<=s.                                   (5)

Set, for `j>=r-1`,

    Q_j=Sym^j V/(M tensor Sym^(j-r)V),

where the denominator is zero at `j=r-1`. These are vector bundles with

    rank Q_j=r,       deg Q_j=(j-r+1)*epsilon.

For `r-1<=j<s`, equations (4)--(5) identify

    B_j=H^(-j) tensor Q_j.                              (6)

## 4. Duality fixes the socle degree and second quotient degree

Pair `B_(r-1)=H^(-(r-1)) tensor Sym^(r-1)V` with `B_(s-1)` in (3).
Taking degrees and using (6) gives

    deg S=-d*lambda+(s-r)*epsilon/r.                    (7)

Now `P_s=J^s` implies a SURJECTION

    A_s := Sym^s E/(R tensor Sym^(s-r)E) -> B_s.         (8)

The source is `H^(-s) tensor Q_s`, rank `r`, and the target, by (3), is

    B_s=H^(r-2) tensor S tensor (Sym^(r-2)V)^*,

rank `r-1`. The kernel `T` of (8) is a line subbundle. Degree subtraction
using (7) gives

    deg T=-s*lambda+s*epsilon/r.                        (9)

In particular the displayed rational quantities must be integral in
any actual example. This is a consequence, not an extra assumption.

## 5. The full root section has degree zero and no zeros

For `s>=r-1`, restriction to the root divisor gives

    Q_s = pi_* O_Z(s),
    A_s = H^(-s) tensor pi_* O_Z(s).                     (10)

Indeed the restriction sequence on `C x P1` has kernel
`M tensor O_(P1)(s-r)` and has vanishing relative first cohomology in
this range. It holds for the FULL Cartier root, including nilpotents.

By finite adjunction, the inclusion `T -> A_s` corresponds to a section

    sigma of L_Z := O_Z(s) tensor pi^*(H^(-s) tensor T^(-1)). (11)

At the generic point of `C`, its image is the unique second quotient
relation supplied by the full initial ideal in (1). Coprimality there
means that `sigma` is a UNIT on the entire generic root algebra. This
retains its nilpotents and each of its generic components.

The scheme `Z` is an effective Cartier divisor in the smooth surface
`C x P1`, hence is a pure Cohen--Macaulay curve. It is finite flat over
`C` and has no vertical associated points. A section that is a unit at
all generic points is therefore a nonzerodivisor and yields

    0 -> O_Z -> L_Z -> D_sigma -> 0,

where `D_sigma` has finite length. The coefficient root class gives

    deg O_Z(1)=epsilon,
    deg pi^*A=r deg A

for every line bundle `A` on `C`, with degrees and lengths computed on
the full root scheme. Therefore (9) gives

    deg L_Z=s*epsilon+r(-s*lambda-deg T)=0.

By the exact sequence, this degree is `length D_sigma`. Thus the
cokernel is zero and `sigma` is nowhere zero, including on nonreduced
or singular fibers. It trivializes `L_Z`, proving (2).

Consequently `T` is everywhere coprime to the first quotient relation.
No finite-support degeneration divisor survives. The degree-zero
argument, rather than generic coprimality alone, removes that divisor.

## 6. Further rigidity: recovering the full ordinary graded algebra

Let `K'_s` be the kernel of `Sym^s E -> B_s`. Its quotient by first
relation multiples is exactly `T`. Define the graded algebra

    D = Sym(E)/(ideal generated by R and K'_s).

Locally lift `T` to a second polynomial generator; different lifts
differ by a multiple of the first relation. Section 5 makes the two
local generators a regular sequence of degrees `(r,s)` in EVERY fiber.
Thus `D` is a finite locally free graded CI family. This construction
uses the generator extension, which need not split globally.

Both `R` and `K'_s` vanish in the multiplicative saturated graded algebra
`B=direct_sum B_i`, so there is a natural algebra morphism

    D -> B.                                             (12)

It is an isomorphism at the generic point and both sides have the same
graded ranks. The graded CI socle line is

    D_d=R tensor T tensor det(E)^(-1).

This determinant formula is invariant under changing the local second
generator by a multiple of the first; it does not assume a split
generator extension. Equations (7) and (9) give

    deg D_d=deg S=deg B_d.

The top component of (12) is generically nonzero. A nonzero map between
line bundles of equal degree on a smooth projective connected curve
is an isomorphism. Therefore the top map is an isomorphism everywhere.

At a closed point of `C`, suppose an element of `D_i` maps to zero in
`B_i`. Perfect fiberwise Gorenstein multiplication in `D` pairs it with
an element of `D_(d-i)` to a nonzero element of `D_d`, unless it was zero
already. The latter nonzero top element cannot map to zero because the
top map is an isomorphism. This contradiction proves that each
`D_i -> B_i` is fiberwise injective. Equal ranks now give an isomorphism
of every graded bundle.

Hence `B` is generated in degree one. In particular `J^i -> B_i` is
surjective for every `i`, or

    P_i=J^i+P_(i+1).

Descending induction from `P_(d+1)=0` gives `P_i=J^i` for all `i`. Thus
all ordinary layers are bundles and every ordinary graded fiber is the
binary CI just constructed. This proves conclusion 3 without an
external Hilbert-function classification.

## 7. Scope and frontier consequences

The proof turns the spectral criterion from an abstract graded test
into a necessary test for actual lci thickenings satisfying (1) and a
saturated first relation. It retains all singularities, repeated roots,
nilpotents, and fibers of the first root. It does not use smoothness or
separability of `Z`, or joint generation by chosen original equations.

Any independent theorem excluding spectral descent on a given root
class can therefore be combined with this bridge, but must be cited
with its exact additional hypotheses. In particular, exclusion of
moving nonreduced roots is a separate proposed contribution; it is not
silently part of STCI-R-0008.

Nonsaturated first relations, generic initial ideals with more than two
minimal generators, and intersections with residual curve components
remain outside the theorem. No unrestricted characteristic-zero STCI
conclusion follows.

Independent review should check especially the saturation equality (4),
the actual surjection (8), generic UNIT rather than merely generically
nonzero in (11), degree on the full nonreduced root, the nonsplit graded
CI construction in section 6, and its top pairing argument.


## 8. Main generalization: arbitrary conormal via a degree-zero resultant

The balanced splitting of `E` is unnecessary for the actual normal-flatness
bridge. This section is an independently reviewed proposal within the
same proof package; its characteristic-zero scope suffices here.

**General theorem proposed.** Let `C` be a smooth connected projective
curve in a smooth threefold, and let `Y` be an actual lci thickening
with `Y_red=C`. Let `E=N_(C/X)^*` be ANY rank-two conormal bundle.
Suppose the full generic initial ideal is the coprime binary CI
`(f_r,g_s)`, with `2<=r<s`, and the ACTUAL first relation sheaf

    R=ker(Sym^r E -> J^r/J^(r+1))

is a line subbundle of `Sym^r E`. Then EVERY ordinary `J`-adic layer is
locally free on `C`, and every fiber of the full ordinary associated
graded algebra is a binary graded complete intersection of degrees
`(r,s)`.

Set

    h=deg E,      a=deg R,      d=r+s-2.

The same saturation argument as sections 3--4 gives perfect pairings
`B_i tensor B_(d-i) -> S`, and exact early layers

    B_j=Sym^j E,                                  j<r,
    B_j=Sym^j E/(R tensor Sym^(j-r)E),             r<=j<s,
    P_i=J^i,                                     i<=s.   (13)

The product `R tensor Sym^(j-r)E` is a subbundle because every fiber
first form is nonzero; no splitting of `E` is used. For `j>=r-1` the
quotient bundle `A_j` by first-relation multiples has rank `r` and

    deg A_j=[r*j-r*(r-1)/2]*h-(j-r+1)*a.                (14)

This follows by subtracting the degrees in its defining exact sequence,
using `deg Sym^j E=j(j+1)h/2`.

Pair the exact early layers `B_(r-1)` and `B_(s-1)`. Their degrees in
(14) give

    ell := deg S=(s-1)*h-((s-r)/r)*a.                   (15)

As before, `P_s=J^s` gives a surjection `A_s -> B_s`, where

    B_s=(Sym^(r-2)E)^* tensor S.

Its kernel `T` is a line subbundle and degree subtraction gives

    t := deg T=s*h-(s/r)*a.                            (16)

Now work locally on `C` and choose a frame of `E`, a generator `f_r`
of `R`, and a polynomial lift `g_s` of the quotient generator `T`.
The homogeneous binary resultant `Res(f_r,g_s)` is unchanged by replacing
`g_s` with `g_s+f_r*h_(s-r)`. Thus it is well-defined for the second
QUOTIENT relation and does not require a global second polynomial line.

Under rescaling the first and second relation generators, the resultant
scales with exponents `s` and `r`. Under a change of normal basis, the
homogeneous resultant has the determinant weight `rs`. Hence the local
resultants glue to a section of the intrinsic line bundle

    L_Res=(det E)^(rs) tensor R^(-s) tensor T^(-r).     (17)

These weights can also be checked directly by viewing the resultant as
the determinant of the homogeneous Sylvester multiplication map; the
identity under `g_s -> g_s+f_r*h_(s-r)` is a polynomial identity and
retains repeated roots and all coefficient specializations.

Equations (16)--(17) give

    deg L_Res=rs*h-s*a-r*t=0.

The FULL generic initial CI hypothesis makes the generic resultant
nonzero. A nonzero section of a degree-zero line bundle on a smooth
projective connected curve has no zeros. Thus the resultant is nowhere
zero, so the two quotient relations are coprime in EVERY fiber.

Define the graded CI family `D` from the first relation and the full
preimage `K'_s` of `T` in `Sym^s E`, as in section 6. Its local regular
sequence generators need not split globally. There is a natural map
`D -> B`; both sides have the same generic graded ranks. Its top line is

    D_d=R tensor T tensor (det E)^(-1),

and, by (15)--(16),

    deg D_d=a+t-h=ell=deg S.

The generic top map is nonzero and is therefore an isomorphism everywhere.
Perfect graded multiplication in EVERY fiber of `D` then forces every
map `D_i -> B_i` to be fiberwise injective, hence an isomorphism. Exactly
as in section 6, generation of `B` in degree one gives
`P_i=J^i+P_(i+1)`; descending induction yields `P_i=J^i` for every `i`.
This proves the general theorem.

The resultant proof requires no Hilbert-function classification,
apolarity, balanced splitting, smoothness of the root, or global
retraction. Its key global input is the projectivity of `C`, which
turns a generic nonzero degree-zero resultant section into an everywhere
nonzero section. A separate local extremal-Hilbert-function proof,
with its explicit classical drop-theorem dependency, is preserved in
[the independent local normal-flatness proposal](2026-10-19-filtered-generic-ci-normal-flatness.md).
That independent route also handles the equal-degree case under its
stated exact-order hypothesis; this section only claims `r<s`.

For balanced split `E`, the resultant conclusion recovers the full-root
spectral descent in section 5. Combined with any correctly scoped
nonreduced-root Picard obstruction, it applies that obstruction to actual
lci thickenings satisfying the stated saturated-first and full-generic-CI
hypotheses. All remaining assumptions continue to be essential boundaries;
no unrestricted STCI exclusion is claimed.
