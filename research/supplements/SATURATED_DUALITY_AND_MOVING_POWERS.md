# saturated duality and moving powers

Complete mathematical dossier preserving computations, exact hypotheses, counterexamples, independent arguments and unresolved scope.

---

## 2026-10-19-filtered-saturated-duality-moving-purepower-bridge

# Saturated duality excludes moving pure-power first relations in generic CI thickenings

Date: 2026-10-19.
Status: **PROPOSAL WITH INDEPENDENT REVIEW PASS; not promoted.**
Independent audit: [filtered-bridge review](2026-10-19-filtered-saturated-duality-moving-purepower-independent-audit.md).
Author: filtered-algebra worker, with the degree-s shortcut suggested by
the independent filtered-bridge reviewer. No canonical record is edited
or promoted.

## 1. Exact theorem proposed

Let `k` be algebraically closed of characteristic zero. Let `C` be a
smooth connected projective curve in a smooth threefold `X`, with
balanced split conormal

    E=N_(C/X)^*=H^(-1) tensor V,   dim_k V=2.

Let `Y` be an ACTUAL locally complete-intersection thickening with
`Y_red=C`. Thus `O_Y` is pure of dimension one and Gorenstein. Set
`J=I_C O_Y`, and write

    K_j=ker(Sym^j E -> J^j/J^(j+1)).

Assume the FULL generic ordinary initial ideal is the coprime binary
complete intersection

    gr_(J_eta)(O_(Y,eta)) = k(C)[x,y]/(m^r,g_s),
    2 <= r < s,                 gcd(m,g_s)=1.               (1)

Let `M subset V tensor O_C` be a line subbundle whose generic line is
spanned by `m`, put `W=H^(-1) tensor M`, and assume the ACTUAL first
relation is saturated:

    K_r=W^r as a subbundle of Sym^r E.                    (2)

If `deg M=-e<0`, **no such `Y` exists**.

This concerns the full initial ideal and the actual first relation
sheaf. A repeated factor in a tangent form alone does not give (1) or
(2). No hypothesis is made about normal orders of chosen defining
equations, their joint generation of the first relation, smoothness of
the full root, or flatness of later ordinary layers. The proof below
allows arbitrary such later torsion in advance.

For the fixed rational quartic `C0` in `P3`, the accepted conormal is
`E=O_P1(-7)^2`. The theorem would close this specified actual-thickening
lane; it is not an unrestricted STCI claim. In the broader intersection
problem `C subset Y_red`, the unique-support purity argument below does
not apply to the whole `Y` when other components are present.

## 2. Dependencies and authority

The characteristic-zero apolar bundle calculation is an accepted input
from [the pure-power tower](2026-10-14-generalization-moving-power-obstruction-tower.md)
and [its independent audit](2026-10-14-generalization-moving-purepower-tower-independent-audit.md).
For every `j>=r-1`, it gives

    Sym^j E/(W^r tensor Sym^(j-r)E)
       = H^(-j) tensor M^(-(j-r+1)) tensor Sym^(r-1)V,     (3)

where at `j=r-1` the denominator is zero.

The actual socle line and Gorenstein MCM duality are accepted inputs in
[the independent socle audit](OCT13_THICK_EQUALITY_SOCLE_AND_FILTRATIONS.md#source-2026-10-13-generalization-socle-independent-auditmd),
sections 2--4. That audit does not itself supply the general saturated
pairing used below; its ordinary pairing statements have more
restrictive equality/torsion-free hypotheses. The new bridge consists
of the saturated pairing, exact early layers, and degree-s contradiction.

[STCI-R-0009](../results/moving_purepower_boundary.md) already excludes a
uniform fiberwise graded CI with this first moving power. The proposed
proof reaches an actual-thickening exclusion directly and does not need
to assume that uniformity or invoke it as an intermediate conclusion.
No inherited proof or computation is rerun.

## 3. Saturated powers and exact global duality

The generic graded algebra in (1) is Gorenstein, with last nonzero degree

    d=r+s-2.

Purity implies `J^(d+1)=0` globally: that ideal is a generically zero
subsheaf of `O_Y`, which has no nonzero finite-support subsheaf.

Let `P_i` be the saturation of `J^i` in `O_Y`, namely the inverse image
of the finite-support torsion of `O_Y/J^i`. Equivalently, locally,

    P_i=O_Y intersect (J_eta)^i inside O_(Y,eta).

Then `P_0=O_Y`, `P_1=J`, `P_(d+1)=0`, and `O_Y/P_i` is pure CM (or
zero). Every `P_i` is MCM as well. Generic multiplication containments
and saturation give

    P_i P_j subset P_(i+j),   J P_i subset P_(i+1).

Thus `B_i=P_i/P_(i+1)` is annihilated by `J`; it is a vector bundle on
`C`, because it is a subsheaf of the pure sheaf `O_Y/P_(i+1)`.

Let `S=Ann_Y(J)` be the actual socle line. For an actual CI of degrees
`a,b` in `P3`, its accepted value is
`S=omega_C tensor O_C(4-a-b)`, but no explicit formula is needed here.

Set `Q_i=Ann_Y(P_i)`. These ideals are saturated: a finite-support
section of `O_Y/Q_i` would multiply `P_i` into a finite-support subsheaf
of `O_Y` and therefore would already lie in `Q_i`. At the generic point,
the graded Gorenstein property in (1) gives

    Ann((J_eta)^i)=(J_eta)^(d+1-i).

Both global ideals with those generic fibers are saturated. Hence

    Q_i=P_(d+1-i).                                      (4)

On a Gorenstein curve, MCM duality is exact on MCM modules. Dualize

    0 -> B_i -> O_Y/P_(i+1) -> O_Y/P_i -> 0.

The local `Ext^1_Y(O_Y/P_i,O_Y)` vanishes. Since `J B_i=0`, every map
`B_i -> O_Y` lands in `S`. Exactness and (4) yield

    B_(d-i) = Hom_C(B_i,S),
    B_i tensor B_(d-i) -> S is perfect everywhere.        (5)

The map is induced by actual multiplication. This is a statement about
the SATURATED filtration and makes no assumption that ordinary layers
are torsion-free. No global retraction `Y -> C` is asserted.

## 4. Saturation of the first relation controls all early layers

For `j<r`, `K_j` has generic rank zero. It is a subsheaf of the bundle
`Sym^j E`, so `K_j=0`. Thus

    J^j/J^(j+1)=Sym^j E,                  0<=j<r.         (6)

For `r<=j<s`, products of (2) give

    W^r tensor Sym^(j-r)E subset K_j.

The left side is saturated in `Sym^j E`: choose `W` as one local basis
vector of `E`; the complementary monomials give a free quotient of rank
`r`. Assumption (1) gives equal generic ranks. The quotient between the
two sides is a rank-zero subsheaf of that free quotient, so it vanishes:

    K_j=W^r tensor Sym^(j-r)E,            r<=j<s.         (7)

Every ordinary layer through index `s-1` is therefore a bundle. Its
successive extensions show that `O_Y/J^i` is CM for `i<=s`, whence

    P_i=J^i,                             0<=i<=s.        (8)

Combining (3), (6), and (7),

    B_(r-1)=H^(-(r-1)) tensor Sym^(r-1)V,
    B_(s-1)=H^(-(s-1)) tensor M^(-(s-r))
                                      tensor Sym^(r-1)V. (9)

This is where a SATURATED ACTUAL first relation is indispensable;
generic first-symbol information does not establish (7) or (8).

## 5. The socle degree forces an impossible degree-s quotient map

Write `lambda=deg H` and `g=s-r`. The perfect pairing of the two
rank-r bundles in (9) gives

    deg S=-lambda*d+e*g.                                (10)

Only degrees are needed; the base need not be rational and no
identification of equal-degree line bundles is assumed.

By (8), `P_s=J^s`, so `Sym^s E -> B_s` is surjective. First-relation
multiples vanish, hence there is an induced surjection

    A_s := Sym^s E/(W^r tensor Sym^(s-r)E) -> B_s.        (11)

The source, by (3), is

    A_s=H^(-s) tensor M^(-(g+1)) tensor Sym^(r-1)V.

The target, by (5) and (6), is

    B_s=Hom_C(B_(r-2),S)
       =H^(r-2) tensor S tensor (Sym^(r-2)V)^*.

Its rank is `r-1>0`. Therefore the bundle of homomorphisms in (11) is
a constant vector-space bundle tensored with the line

    H^(s+r-2) tensor S tensor M^(g+1).

Using `s+r-2=d` and (10), that line has degree

    lambda*d + (-lambda*d+e*g) - e(g+1) = -e < 0.

A negative-degree line bundle on a smooth projective curve has no
nonzero global section. Consequently EVERY global map `A_s -> B_s`
is zero, contradicting the surjection (11). This proves the proposed
nonexistence theorem.

An equivalent determinant calculation retains the prospective second
relation: the kernel `T` in (11) would be a line of degree
`-s*lambda+s*e`, and `Hom(T,A_s)` would be a constant vector space
tensored with a line of degree `-(r-1)e<0`. The Hom-vanishing argument
above avoids introducing this unnecessary extra line.

For `C0`, (10) is the exact necessary equality

    mu=7d+14-4(a+b)=e(s-r).

The contradiction uses the actual degree-s quotient map, not this
scalar equality alone.

## 6. Frontier impact and unresolved cases

The separate independent review passed. Within its exact hypotheses,
this closes actual lci thickenings with a
moving pure-power first relation satisfying (1)--(2), even when later
ordinary layers were initially allowed arbitrary special-point
degeneration. It supplies a more direct actual-CI interface for this
specific initial pattern than STCI-R-0006, without its smooth-root,
chosen-symbol, or finite-gap hypotheses.

It does not treat nonsaturated first relations, generic non-CI initial
ideals, or general reducible/nonreduced full root schemes. The
unrestricted characteristic-zero `C0` question remains open.

No computation is required. Independent review must reconstruct (4)--(5),
the rank/saturation step (7), the accepted apolar input (3), and the
surjectivity in (11). Generic CI Hilbert symmetry, actual Gorenstein
duality, and global projectivity all have explicit roles and must not
be silently dropped.


---

## 2026-10-19-filtered-saturated-duality-moving-purepower-independent-audit

# Independent audit: saturated duality and the actual-to-spectral CI bridge

Date: 2026-10-19. Reviewer: `filtered_bridge_audit`.
Status: **PASS within the exact hypotheses below; reviewed proposal, not a
promoted canonical result.**

The initial proposal was the moving-pure-power argument in
[the filtered-duality note](2026-10-19-filtered-saturated-duality-moving-purepower-bridge.md).
Independent reconstruction yielded a shorter pure-power contradiction;
the parent investigation then proposed the arbitrary-first-relation
spectral bridge audited in Sections 4--5 below and its arbitrary-conormal
resultant extension in Section 7. The general proposal is recorded in
[the saturated-first-relation bridge](2026-10-19-saturated-first-relation-spectral-bridge.md).
This file records those stronger reconstructions explicitly. No accepted proof, canonical record,
or inherited computation was modified or rerun.

## 1. Exact setting, claim, and authority

Let `C` be a smooth connected projective curve over an algebraically
closed field, in a smooth threefold `X`, and suppose

    E=N_(C/X)^*=H^-1 tensor V,       dim V=2.

Let `Y` be an actual locally complete-intersection thickening with
`Y_red=C`. Write `A=O_Y`, `J=I_C A`, and

    K_j=ker(Sym^j E -> J^j/J^(j+1)).

Assume the **full** generic ordinary associated graded algebra is

    gr_(J_eta)(A_eta)=k(C)[x,y]/(f_r,g_s),
    2<=r<s,                      gcd(f_r,g_s)=1.          (1)

Assume the actual first relation is a saturated line subbundle

    K_r=R=H^-r tensor M subset Sym^r E,                  (2)

where `M subset Sym^r V tensor O_C` is a line subbundle. Set

    lambda=deg H,    epsilon=-deg M,    g=s-r,
    d=r+s-2.

The corresponding full root divisor `Z subset C x P(V*)` is finite flat
of degree `r` over `C`; write `pi:Z->C` and `O_Z(1)` for the direction
line bundle. The audited balanced-conormal conclusion is that a line bundle `N`
on `C` satisfies

    O_Z(s)=pi^*N.                                       (3)

Thus an everywhere-coprime second **quotient** relation exists in the
sense of promoted [STCI-R-0008](../results/spectral_root_picard_criterion.md).
This is an implication from actual filtered geometry to the accepted
spectral criterion; it does not claim to lift an arbitrary abstract
graded family back to an actual thickening.

The accepted inputs are the socle-line and Gorenstein MCM duality facts
in [the independent socle audit](OCT13_THICK_EQUALITY_SOCLE_AND_FILTRATIONS.md#source-2026-10-13-generalization-socle-independent-auditmd),
and the root-quotient identification of R-0008 and its
[independent evidence](2026-10-14-generalization-spectral-root-curve-independent-audit.md).
The existing socle audit proves perfect ordinary pairings under extra
conditions. The perfect **saturated** pairing established next is the
new bridge; no assertion that the ordinary powers are already saturated
is imported from that audit.

In fact, the bridge also forces every ordinary power `J^i` to be
saturated and the ordinary associated graded algebra to be a uniform
fiberwise complete intersection of degrees `(r,s)`. Section 6 audits
this stronger conclusion.

In characteristic zero, for the pure-power specialization
`M=M_1^r`, with `M_1 subset V tensor O_C` and `deg M_1<0`, the audited
conclusion is that no such `Y` exists. Section 8 proves this directly.
For the rational base, combining (3) with the separately reviewed
[nonreduced-root obstruction](2026-10-19-spectral-nonreduced-root-obstruction.md)
excludes every nonreduced moving full root under (1)--(2). The independent
audit of that latter obstruction remains its own evidence; it is not
replaced by this audit.

## 2. Saturation and perfect complementary pairings

Because `Y` is a pure one-dimensional lci scheme with unique reduced
support `C`, a generically zero subsheaf of `A` is zero. The generic
socle degree in (1) is `d`, so `J^(d+1)=0` globally.

Let `P_i` be the saturation of `J^i` in `A`, meaning the inverse image of
the maximal finite-support subsheaf of `A/J^i`. Locally it is the
inverse image of `(J_eta)^i` in `A_eta`. We have

    P_0=A,        P_1=J,        P_(d+1)=0,
    P_i P_j subset P_(i+j),     J P_i subset P_(i+1).

The product inclusions hold generically, then globally by saturation.
Every `A/P_i` is CM of dimension one or zero, and

    B_i=P_i/P_(i+1)

is a vector bundle on `C`: it embeds in the pure sheaf `A/P_(i+1)` and
is annihilated by `J`.

Let `S=Ann_A(J)`. The accepted socle theorem makes `S` a line bundle
on `C`. For the generic Artin Gorenstein algebra, the Gorenstein graded
algebra in (1) has symmetric Hilbert function and gives

    Ann_(A_eta)((J_eta)^i)=(J_eta)^(d+1-i).              (4)

One can check the equality without assuming a homogeneous splitting of
`A_eta`: the right side annihilates `(J_eta)^i`, and its length is the
length of `A_eta/(J_eta)^i` by Hilbert-function symmetry. Frobenius
duality gives exactly that length for the annihilator, so inclusion is
equality.

Each `Ann_A(P_i)` is saturated. Indeed, if a section is generically in
this annihilator, its products with `P_i` vanish generically in the pure
sheaf `A`, and therefore vanish. Consequently equality of generic
fibers in (4) yields

    Ann_A(P_i)=P_(d+1-i).                               (5)

Apply `Hom_A(-,A)` to

    0 -> B_i -> A/P_(i+1) -> A/P_i -> 0.

The first sheaf Ext of the CM quotient `A/P_i` into the Gorenstein
curve `A` vanishes. Thus the dual sequence is exact, and (5) gives

    B_(d-i)=Hom_A(B_i,A)=Hom_C(B_i,S).                  (6)

The map is induced by multiplication. In particular all complementary
pairings `B_i tensor B_(d-i) -> S` are perfect on all of `C`.

This is a statement about the saturated filtration. It permits torsion
in the original ordinary layers, and requires no global retraction
`Y->C` or splitting of the formal neighborhood.

## 3. The actual saturated first relation determines all early layers

For `j<r`, `K_j` has zero generic rank and is a subsheaf of a vector
bundle, so `K_j=0`. For `r<=j<s`, products of the actual relation (2)
give

    R tensor Sym^(j-r)E subset K_j.                     (7)

This left subsheaf is saturated: at each point the homogeneous
polynomial `f_r` is nonzero, so multiplication by it on binary forms
has the same rank at that point as over the generic field. The
cokernel is therefore locally free. Both sides of (7) have the same
generic rank by the full initial ideal in (1). Their difference embeds
as a rank-zero subsheaf in that vector-bundle cokernel and is zero.

Hence every ordinary layer through index `s-1` is a vector bundle.
Its finite successive extensions make `A/J^i` CM for `i<=s`, proving

    P_i=J^i                 for 0<=i<=s.               (8)

This is the exact place where the actual equality in (2) is needed.
Knowing only that the saturation of `K_r` is `R` does not justify (7)
with `R`, and does not imply (8).

For `j>=r-1`, define the rank-`r` quotient bundle

    Q_j=Sym^j V/(M tensor Sym^(j-r)V),

with the denominator zero at `j=r-1`. Its degree is

    deg Q_j=(j-r+1)epsilon,

and for `r-1<=j<s`, (7)--(8) give `B_j=H^-j tensor Q_j`.

## 4. Determinants force a zero-degree second spectral section

The complementary middle pair in (6) is `(r-1,s-1)`. Its two ranks are
`r`, with degrees

    deg B_(r-1)=-r(r-1)lambda,
    deg B_(s-1)=-r(s-1)lambda+g epsilon.

Perfectness therefore forces the exact degree identity

    deg S=-d lambda+g epsilon/r.                       (9)

This equality itself imposes an integrality condition; fractions are
only notation for an already integral degree.

By (8), `J^s=P_s`. The natural map from ordinary degree-`s` symbols to
the saturated layer is consequently surjective. It factors through
the old first-relation multiples, giving

    A_s=H^-s tensor Q_s -> B_s -> 0.                   (10)

Perfect duality and `d-s=r-2` give

    B_s=B_(r-2)^vee tensor S
       =H^(r-2) tensor S tensor (Sym^(r-2)V)^vee.

This is a rank-`r-1` bundle. Thus the kernel `T` of (10) is an actual
line subbundle of `A_s`. Computing degrees from (9)--(10) yields

    deg A_s=-rs lambda+(g+1)epsilon,
    deg B_s=(r-1)(-s lambda+g epsilon/r),
    deg T=-s lambda+s epsilon/r.                      (11)

These determinant calculations need no splitting of bundles on `C`
and no assumption that `C=P1`.

For `s>=r-1`, the standard divisor sequence on `C x P(V*)` gives

    Q_s=pi_*O_Z(s).

The inclusion `T->H^-s tensor pi_*O_Z(s)` is therefore adjoint to a
section

    sigma in H^0(Z,L),
    L=O_Z(s) tensor pi^*(H^-s tensor T^-1).              (12)

Its generic restriction is, up to an invertible scalar, the second
initial generator `g_s` modulo `f_r`. The full generic coprimality in
(1) says that this section is a unit on the entire generic root scheme,
including its nilpotents.

## 5. Why nilpotents and special fibers cannot hide zeros

The full root `Z` is an effective Cartier divisor in a smooth surface
and is finite flat over `C`. Thus it is one-dimensional CM, and every
associated generic point lies over the generic point of `C`. A
section invertible at those generic points is a nonzerodivisor on
`O_Z`, even when `Z` is reducible or nonreduced. Therefore (12) defines
an injection with finite-length cokernel:

    0 -> O_Z -> L -> D -> 0.                            (13)

The degree of `O_Z(1)` is `epsilon`: intersect the root divisor, whose
class is `r` times the direction class minus `pi^*M`, with the direction
class. Pullback of a line bundle of degree `a` on `C` has degree `ra`
on `Z`. These are Euler-characteristic/intersection degrees and retain
the multiplicities of nonreduced components. Equations (11)--(12) give

    deg L=s epsilon+r(-s lambda-deg T)=0.

Taking Euler characteristics in (13) now yields `length(D)=0`. Thus
`D=0` and `sigma` is nowhere zero on the full scheme `Z`.
Consequently

    O_Z(s)=pi^*(H^s tensor T),

which is (3). There is no discarded degeneration divisor: degree zero
forces the actual divisor of this section to vanish.

This completes the general actual-to-spectral bridge. It proves the
existence of a uniform abstract second quotient relation; that relation
need not be a globally lifted second polynomial line. This distinction
is required by R-0008 and is preserved here.

## 6. The uniform quotient forces normal flatness

Let

    K'_s=ker(Sym^s E -> B_s).

Its quotient by the old first-relation multiples is exactly the line
`T` in (10). The inclusion `T->A_s` is everywhere coprime to the first
relation because the corresponding spectral section is a unit on the
full root scheme. Define the graded quotient algebra

    D=Sym(E)/(R,K'_s).

Locally on `C`, lift a frame of `T` to a degree-`s` form. Then `D` is
presented by that form and a frame of the degree-`r` first relation.
They are coprime in every fiber. Thus `D` is a relative graded
complete intersection; each `D_i` is a vector bundle of the same rank
as the generic CI Hilbert function. No global splitting of
`0 -> R Sym^(s-r)E -> K'_s -> T -> 0` is needed.

These relations vanish in the saturated associated graded algebra
`B=direct_sum B_i`, so there is a natural graded algebra map

    phi:D -> B

which is an isomorphism generically. Its top degree is a map of line
bundles. The top line of a binary graded CI glues as

    D_d=R tensor T tensor det(E)^-1.

This can be checked in local Koszul presentations: changing a first
generator and a lift of the second changes their ordered wedge by the
product of their scalar transitions; adding first-generator multiples
to the second has no effect. Therefore (11) gives

    deg D_d=(-r lambda-epsilon)
            +(-s lambda+s epsilon/r)+2lambda
           =-d lambda+g epsilon/r
           =deg S.

The generic isomorphism `phi_d:D_d->B_d=S` is consequently a global
isomorphism: a nonzero map between line bundles of equal degree on the
smooth projective curve has no zero divisor.

For each closed point `c`, the graded CI algebra `D_c` has perfect
pairings `D_(i,c) tensor D_(d-i,c) -> D_(d,c)`. If a nonzero element of
`D_(i,c)` were killed by `phi_(i,c)`, multiply it by a complementary
element giving nonzero top product. Algebra-map compatibility would
kill that product under `phi_(d,c)`, contradicting the top
isomorphism. Hence every `phi_(i,c)` is injective. Source and target
have the same rank, so every `phi_i` is an isomorphism of bundles.

It follows that `B` is generated in degree one. Since `P_1=J`, this
gives `P_i=J^i+P_(i+1)`. Descending induction from `P_(d+1)=0` yields

    P_i=J^i                    for every i.

Thus all ordinary layers are vector bundles and the ordinary graded
algebra is itself a uniform fiberwise binary complete intersection.
This conclusion was not assumed in Sections 2--5; it follows from
their spectral section and the top-line comparison.

## 7. Arbitrary conormal: the resultant upgrade

The projective normal-flatness conclusion actually requires no balanced
splitting of `E`. Let `C` again be a smooth connected projective curve,
let `E=N_(C/X)^*` be arbitrary of rank two, and keep the actual lci,
unique-support, full generic CI hypotheses of Section 1. Assume

    K_r=R subset Sym^r E

is an actual line subbundle, with `2<=r<s`. Put

    h=deg E,        a=deg R.

Sections 2--3 still apply: their saturation and MCM arguments use no
splitting. In particular the early layer quotient

    A_j=Sym^j E/(R tensor Sym^(j-r)E)

is a rank-`r` bundle for `j>=r-1`, and agrees with `B_j` for `j<s`.
Using `deg Sym^j E=j(j+1)h/2`, its degree is

    deg A_j=r(2j-r+1)h/2-(j-r+1)a.                    (14)

The complementary middle pair is still `(r-1,s-1)`. Taking degrees
in its perfect pairing gives

    deg S=(s-1)h-(s-r)a/r.                            (15)

As before, `P_s=J^s` yields an actual vector-bundle surjection
`A_s->B_s`. Its kernel is a line `T`. From

    B_s=(Sym^(r-2)E)^vee tensor S

and (14)--(15), its degree is

    deg T=s h-s a/r.                                  (16)

Choose local frames `f` of the degree-`r` relation and local lifts `g`
of `T` in degree `s`. The binary resultant glues as a section of

    U=(det E)^(rs) tensor R^(-s) tensor T^(-r).         (17)

The determinant exponent is fixed, for example, by the intrinsic
identity for two linear forms: their resultant is their wedge in
`det E`. In general the Sylvester determinant has degree `s` in the
first coefficients, degree `r` in the second coefficients, and weight
`rs` under a basis change of `E`. Changing a lift by `g->g+q f` does
not change the resultant. These are polynomial identities over the
integers, so do not require characteristic zero.

By the full generic CI hypothesis, the section is nonzero generically.
Equations (16)--(17) give

    deg U=rs h-s a-r(s h-s a/r)=0.

Thus its zero divisor on the smooth projective curve is empty. The
resultant is nonzero in every fiber, so the first relation and the
second quotient relation are coprime in every fiber. This replaces
the spectral zero-divisor argument of Section 5.

Construct `D=Sym(E)/(R,K'_s)` as in Section 6. Its top line is again
`R tensor T tensor det(E)^-1`, of degree

    a+(s h-s a/r)-h
      =(s-1)h-(s-r)a/r
      =deg S.

The generic top map is therefore an isomorphism everywhere. The perfect
fiberwise CI pairings then give `D_i=B_i` for every degree. Descending
induction gives `P_i=J^i` for all `i`, exactly as in Section 6.

**Audited arbitrary-conormal theorem.** An actual lci thickening of a
smooth connected projective curve in a smooth threefold, with full
generic coprime binary CI initial ideal of degrees `2<=r<s` and actual
saturated first relation line, has every ordinary power saturated and
a uniform fiberwise graded CI normal algebra of degrees `(r,s)`.
No balanced conormal, rationality, or characteristic-zero assumption
is used in this bridge. The corresponding graded/root exclusions can
have additional hypotheses, which must still be retained.

The equal-degree case is not included in this resultant proof: then
the first relation space has rank two and the construction of its
second quotient line is different. A separate local Hilbert-function
argument is recorded in
[the normal-flatness proposal](2026-10-19-filtered-generic-ci-normal-flatness.md);
that broader variant is not needed as a premise here.

## 8. Independent pure-power shortcut

For the moving-power specialization, write the moving direction as
`M_1 subset V tensor O_C`, `deg M_1=-e<0`, so the coefficient line in
Section 1 is `M=M_1^r` and `epsilon=re`. In characteristic zero the
accepted apolar formula is

    Q_s=M_1^(-(g+1)) tensor (constant rank-r bundle),

where constant determinant factors of `V` are harmless line factors.
Equation (9) becomes

    deg S=-d lambda+g e.

The surjection (10) would thus be a nonzero map between bundles

    A_s=H^-s M_1^(-(g+1)) tensor (constant rank r),
    B_s=H^(r-2) S tensor (constant rank r-1).

Every matrix entry of such a map is a section of the line bundle

    H^d tensor S tensor M_1^(g+1),

whose degree is

    d lambda+(-d lambda+g e)-(g+1)e=-e<0.

It has no global sections on the smooth projective integral curve.
The map (10) is therefore zero, contradicting its surjectivity onto
rank `r-1>0`.

This proves actual-thickening nonexistence for a saturated moving
pure-power first relation and full generic coprime CI initial ideal on
**any** smooth projective base curve with balanced split conormal. It
does not require proving that all late ordinary powers are saturated,
and it does not assume everywhere coprimality in advance.

## 9. Adversarial checks and retained boundaries

* **Saturation of the actual first relation is indispensable.** If
  `K_r=R(-D0)` for an effective nonzero divisor, multiplying actual
  relations only supplies `R(-D0)` multiples. The early quotient may
  have torsion, so `P_s=J^s` and (10) need not hold. Replacing `K_r` by
  its saturation would erase precisely the remaining defect.

* **The full generic initial ideal is indispensable.** It supplies
  `d=r+s-2`, symmetric generic Hilbert function, the exact early
  relation ranks, and the generic unit in (12). Two coprime-looking
  selected symbols alone do not establish these facts if there are
  additional initial generators or leading cancellations.

* **Gorenstein and purity are used separately.** Gorenstein CM duality
  proves (6); purity removes generically zero subsheaves and makes
  saturation intrinsic. A finite principal-relation thickening from
  the old tower need not be Gorenstein, and is therefore no
  counterexample.

* **The degree proof has projective scope.** The degree argument in
  (13), the degree-zero resultant, and the negative-degree vanishing in
  Section 8 use projectivity. This proof alone makes no affine-base
  extension. The separately recorded local Hilbert-function argument
  addresses that larger scope through a different input.

* **Unique support matters.** If `Y_red` has residual components in
  addition to `C`, an ideal generically zero along `C` can be nonzero
  on those other components. The proof cannot be applied unchanged to
  the whole intersection scheme in that situation. No exceptional
  vertical component is identified with a component downstairs.

* **Nonreduced total roots differ from nonreduced special fibers.**
  The spectral conclusion concerns the full divisor `Z`. It permits
  ramification and multiple special fibers of an integral reduced
  root. Applying the separate doubled-divisor theorem excludes
  repeated total components only under its rational-base,
  positive-movement, characteristic-zero hypotheses.

* **The linear and equal-degree cases are outside scope.** The proof
  uses `r>=2` and the first rank-one relation with `r<s`. It does not
  silently extend to primitive generic algebras or two independent
  first relations of the same degree.

## 10. Verdict and frontier impact

The general bridge (1)--(3), the perfect saturated duality, the
normal-flatness upgrade, the arbitrary-conormal resultant argument,
and the pure-power actual-thickening exclusion
pass independent reconstruction.
There is no unresolved finite computation in these arguments. The
new claims remain unpromoted and require the repository's normal
canonical review procedure before entering an ID-bearing result record.

For `C0`, `H=O_P1(7)`. The bridge imposes the full spectral Picard test
on every actual lci thickening with saturated first relation and full
generic CI initial ideal of distinct degrees. With the separately
audited nonreduced-root obstruction, its moving full root must be
reduced. Nonsaturated first relations, generic non-CI initial ideals,
constant roots, and reduced-root ambient lifting remain open. The
unrestricted characteristic-zero STCI question is not resolved.


---

## 2026-10-19-singular-root-investigation

# Reduced movement-two roots: the remaining formal surface must be singular

Date: 2026-10-19. Author: `singular_roots` research agent.

Status: **new conditional theorem proposal with independent review PASS; not promoted**.
The separate audits are
[the smoothing audit](OCT15_20_PROJECTION_ROOT_AND_SURFACE_FRONTIERS.md#source-2026-10-19-regular-singular-root-smoothing-auditmd) and
[the equal-slope two-component audit](OCT15_20_PROJECTION_ROOT_AND_SURFACE_FRONTIERS.md#source-2026-10-19-regular-reducible-root-independent-auditmd).
This note does not promote a canonical result, alter an accepted theorem, or
settle the singular-formal-surface case.

## 1. Exact scope and accepted premises

Let `k` be algebraically closed of characteristic zero. Work with the fixed
rational quartic `C0` in `P3`, its blowup `B=Bl_C0(P3)`, and exceptional
divisor `E=P1_base x P1_direction`. Write `p:E->P1_base`, and use the
repository conventions

    O_E(E)=O_E(7,-1),       H|E=O_E(4,0).

An embedded all-orders Cartier lift of a full root `Z subset E` means
compatible effective Cartier divisors on every exceptional neighborhood,
as in the source underlying
[STCI-R-0005](../results/smooth_root_formal_obstruction.md). Its inverse
limit is a formal effective Cartier surface `Vhat` in the completion of
`B` along `E`, with scheme-theoretic intersection `Vhat cap E=Z`.

The accepted scope distinctions remain premises:

- STCI-R-0005 excludes smooth full roots of class `(2,r)`, `r>=2`.
- [STCI-R-0011](../results/moving_nonreduced_spectral_root_obstruction.md)
  makes a spectral-descent survivor reduced. In movement two it is
  integral `(2,r)`, or two distinct smooth `(1,r/2)` components when `r`
  is even.
- [STCI-R-0010](../results/saturated_first_relation_normal_flatness.md)
  supplies spectral uniformity for actual lci thickenings only under its
  full generic binary-CI and saturated-first-relation hypotheses.
- [STCI-R-0006](../results/actual_ci_smooth_root_bridge.md) is an actual
  finite-gap bridge with a **smooth full root**; no singular-root version
  is assumed in this note.

The proposed theorem below concerns the actual ambient formal lifting
problem. It assumes no spectral Picard descent and supplies no automatic
bridge from arbitrary actual STCI equations.

## 2. Proposed theorem

**Theorem A.** Let `Z` be a reduced effective Cartier divisor of class
`(2,r)`, `r>=2`, finite flat over `P1_base`. There is no embedded
all-orders Cartier lift whose formal surface `Vhat` is regular along
the whole of `Z`.

Here regularity is a condition on the **lifted formal surface**, not on
the possibly singular curve `Z`. For a hypersurface in the completion of
the smooth threefold `B` over the perfect field `k`, the condition means
that its completed local surface rings at closed points of `Z` are
regular. This is the smooth-formal-surface condition used below.

Thus, if a reduced singular movement-two root has any all-orders
Cartier lift, every such lift has a singular surface point above
`Sing(Z)`. This narrows the surviving geometry, but does not exclude
these singular lifted surfaces.

The proof uses a smoothing **inside an algebraized smooth surface**.
It does not assert that singular roots can be smoothed in the original
exceptional root-lifting functor.

## 3. Algebraize using the singular root itself

Because `Z=Vhat cap E`, the exceptional parameter is a nonzerodivisor on
`Vhat`, and `Z` is an effective Cartier divisor in this regular formal
surface. Consequently

    N_(Z/Vhat)=O_Z(E)=O_Z(7,-1)=:N.                 (1)

The root `Z` is connected: the exact sequence on `E`

    0 -> O_E(-2,-r) -> O_E -> O_Z -> 0

and Kunneth give `H0(O_Z)=k`, since `r>=1` makes
`H1(O_E(-2,-r))=0`.

For every irreducible component `D` of `Z`, write its bidegree `(a,b)`.
Finiteness over the base gives `b>0`; effectiveness and total first
bidegree two give `0<=a<=2`. Therefore

    deg(N|D)=7b-a >=5>0.                           (2)

A line bundle on a proper curve is ample if its degree on every reduced
irreducible component is positive, so `N` is ample.

Bost's **Corollary 3.8**, rather than only his smooth-center Theorem 3.5,
applies here. It permits a proper connected locally complete intersection
scheme of definition, while requiring the formal scheme itself to be
smooth and its normal bundle ample. It algebraizes `Vhat` as a branch
of an integral algebraic surface `W subset B`. Source: J.-B. Bost,
[*Algebraic leaves of algebraic foliations over number fields*,
printed pp. 187--188](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf),
Theorem 3.5, Theorem 3.7, and Corollary 3.8. This is the geometric part of
the paper; no arithmetic hypothesis is imported.

Normalize `W`. The selected formal branch is regular, hence normal.
The normalization/completion argument used in the accepted smooth-root
proof therefore preserves the entire selected branch. That argument
uses normality of `Vhat`, not smoothness of the curve `Z` itself. Its
local maps to the finite normalization glue uniquely, and reduction
modulo the exceptional parameter embeds the same possibly singular
`Z` into the normalization. The selected completed local factors are
regular. Resolve the normalized algebraic surface outside this regular
neighborhood of `Z`. We obtain a smooth projective surface `T` containing
the same Cartier curve `Z`, with its original formal neighborhood.

This leaves the numerical data

    p_a(Z)=r-1,       Z^2=7r-2.                    (3)

Let `S` be the image of `W` in `P3`, `d=deg(S)`, and let `H` on `T` be
the pullback of the hyperplane class. The surface is not exceptional,
and the blowup is an isomorphism away from `E`; hence `T->S` is
birational, `H` is nef, and

    H^2=d>0,         H.Z=4r.                      (4)

Other algebraic branches of `W` and other components of `W cap E` are
retained. None is discarded by saturation.

## 4. The normal line is generated and unobstructed

The relevant vanishing does not need a classification of the singularities.
For `N=O_Z(7,-1)`, the two restriction sequences are

    0 -> O_E(5,-r-1) -> O_E(7,-1) -> N -> 0,
    0 -> O_E(4,-r-1) -> O_E(6,-1)
      -> N tensor p*O_P1(-1) -> 0.

Kunneth gives

    H1(Z,N)=0,
    H1(Z,N tensor p*O_P1(-1))=0.                  (5)

For example, the middle terms have zero `H1` because `O_P1(-1)` has no
cohomology; the left terms have zero `H2` because their first ruling
degree is nonnegative.

The finite flat map `p:Z->P1` makes `p_*N` a vector bundle. Projection
formula and (5) give `H1(P1,(p_*N)(-1))=0`. Splitting this vector bundle
on `P1` shows that every summand has nonnegative degree. Thus `p_*N` is
generated by its global sections. The finite-map evaluation
`p* p_*N -> N` is surjective, so **`N` is generated by global sections**.

These are calculations on the original full `Z`, not on its
normalization, and preserve gluing at singular points.

## 5. An embedded smoothing lemma and its application

**Lemma B.** Let `D` be a connected reduced effective Cartier divisor
on a smooth projective surface `T` over characteristic zero. If
`H1(D,N_(D/T))=0` and `N_(D/T)` is generated by global sections, then
`D` has a flat embedded deformation on `T` whose general fiber is a
smooth connected curve, numerically equivalent to `D`.

**Proof.** Embedded Cartier deformations have tangent space `H0(N)`
and obstruction space contained in `H1(N)`. Local deformations lift
because a local defining nonzerodivisor can be lifted. Hence the
Hilbert scheme of `T` is smooth at `[D]`. Work on a smooth irreducible
open neighborhood `U` of this point, shrinking to the relative
effective-Cartier locus of the universal family `D_U subset T x U`.

At a point `x` of the central curve, write a completed local equation
of the universal family as

    f(x_1,x_2) + sum_i t_i eta_i(x_1,x_2)
                  + terms of parameter order >=2.

The classes of `eta_i` span the evaluations of `H0(N)` in the normal
fiber at `x`. Global generation gives an index with `eta_i(x)!=0`.
The total universal family is therefore regular at `x`, since its
equation has a unit derivative in that parameter direction. The whole
central curve lies in this regular locus. Properness over `U` allows
shrinking `U` so that the entire total family is regular. Over the
perfect field `k` it is smooth over `k`.

Its components dominate `U` by flatness. Characteristic-zero generic
smoothness, followed by properness, supplies a nonempty open subset of
`U` over which the family has smooth fibers. Since `H0(O_D)=k`, upper
semicontinuity gives `h0(O_(D_u))=1` near the central point; these smooth
fibers are connected, hence integral. A connected flat family of
Cartier divisors gives algebraic, hence numerical, equivalence. QED.

The embedded deformation inputs can be checked in Hartshorne's
[author-hosted *Lectures on Deformation Theory*](https://math.berkeley.edu/~robin/math274root.pdf),
Theorem 2.4 (tangent space), Theorem 6.3 (the normal-sheaf gluing
obstruction, explicitly including lci schemes), and Theorem 9.3
(lifting a regular sequence). The elementary universal-family argument
above proves the particular smoothing consequence; no claim of
equisingular deformation versality is needed.

Apply Lemma B to the curve `Z subset T` from Section 3, using (5).
There is a smooth connected integral curve `Z_t subset T` with

    g(Z_t)=r-1,       Z_t^2=7r-2,       H.Z_t=4r.    (6)

The smoothing occurs on `T`; `Z_t` need not map into `E` or cover `C0`.
Only the numerical data (6) enter the next surface argument. The
original root `Z` remains on `T` and still lies over `C0`.

## 6. Opposing degree bounds

The smooth curve `Z_t` satisfies

    Z_t^2-(4g(Z_t)+5)=3r-3>0.

Hartshorne's high-self-intersection theorem and the ruled-model
intersection argument already isolated in the evidence for
STCI-R-0005 apply to the pair `(T,Z_t)` and the nef divisor `H`.
They give

    d <= max_(a positive integer)
              (8ra-(7r-2)a^2) <= r+2.             (7)

The last maximum is at `a=1`, since `7r-2>=4r` for `r>=2`. The
geometric input is Hartshorne,
[*Curves with high self-intersection on algebraic surfaces*,
Theorem 4.1, printed p. 122](https://www.numdam.org/item/PMIHES_1969__36__111_0.pdf).
The local equivalence to the ruled neighborhood and the nef square
comparison are the same accepted mechanism as in
[the preserved independent branch review](OCT15_20_PROJECTION_ROOT_AND_SURFACE_FRONTIERS.md#source-2026-10-15-formal-branch-ruled-model-degree-bound-reviewmd).
We use that mechanism with the new smoothed curve, not the statement
that a smooth `(2,r)` root itself exists in `E`.

Meanwhile `W cap E` contains the original full root `Z`. Thus the
generic multiplicity `m` of the integral surface `S` along `C0`
satisfies `m>=r`. A general plane section is an integral degree-`d`
plane curve with multiplicity at least `m` at the four distinct points
of its intersection with `C0`. Its arithmetic genus gives

    (d-1)(d-2) >= 4m(m-1) >= 4r(r-1).             (8)

Equations (7)--(8) force

    r(r+1) >= 4r(r-1),

which is impossible for `r>=2`. This proves Theorem A under the stated
formal-surface regularity hypothesis.

## 7. Separate two-component proof without Hilbert smoothing

For the R0011 boundary `Z=D1 union D2`, `Di=(1,q)`, `r=2q`, assume the
lifted formal surface is regular along one full component. The surface
is automatically regular away from `D1 cap D2`, because the root is
smooth there. Regularity along one component includes every
intersection point, so it implies regularity along all `Z`.

There is a shorter proof in this case. In the regular formal surface,

    D1^2 = E.D1-D2.D1 = (7q-1)-2q = 5q-1,
    H.D1 = 4q.

Algebraization by Bost may use the full lci root `Z`, or the smooth
center `D1`, whose normal degree is positive. Normalize and resolve
outside `D1`, preserving its square. Hodge index yields

    d <= (H.D1)^2/D1^2
       = 16q^2/(5q-1) <=4q.

Both components remain in `W cap E`, so `m>=2q`. But

    (4q-1)(4q-2) < 4(2q)(2q-1)

for every `q>=1`, contradicting the plane-section genus bound.
The independent audit linked above reconstructs this shorter proof.

## 8. The exact residual gap and local countershields

At a singular root point, write an exceptional parameter as `u` and a
local lift equation as

    g = f_Z + u h_1 + u^2 h_2 + ... .

Since `df_Z` vanishes there, the lifted surface is regular at this point
exactly when `h_1` has nonzero value. Therefore Theorem A says that
every surviving all-orders lift must have at least one singular root
point with `h_1=0`. This is a concrete first-jet incidence condition
for the remaining formal problem, not an emptiness computation.

There is no automatic regularity implication. In a completed smooth
threefold chart the local equations

    g=xy+u^2,             g=y^2-x^3+u^2

give all-orders embedded Cartier lifts of, respectively, the reduced
node `xy=0` and cusp `y^2-x^3=0` on `u=0`, while the total formal
surfaces are singular at the origin. These are local counterexamples
to the missing regularity implication. They are not global lifts on
the actual exceptional surface of `C0` and do not construct STCIs.

Resolution of such singular lifted surfaces can change the normal
degree of the selected normalized root; the accepted smooth-branch
normal-degree argument cannot simply be reused there. Theorem A does
not exclude that stratum.

No finite jet cutoff, actual-CI singular-root bridge, arbitrary-first-
relation statement, or unrestricted `C0` nonexistence result is claimed.
The universal STCI question remains open.

## 9. General balanced-degree observation

The same proof, if independently reviewed in this scope, works in
characteristic zero for any smooth rational degree-`e` curve in `P3`,
`e>=4`, with explicit balanced normal bundle `O(2e-1)^2`.
Replace `7` by `lambda=2e-1` and `4` by `e`. The normal line is
`O_Z(lambda,-1)`; the same restriction-sequence proof gives generation
and vanishing because `lambda-3>=0`. Ampleness holds since
`lambda*b-a>0`. The smoothed curve has square `lambda*r-2`, genus
`r-1`, and hyperplane intersection `e*r`. The ruled-model bound remains
`d<=r+2`, while the opposing plane bound is
`(d-1)(d-2)>=e*r*(r-1)`, again contradictory for `e>=4,r>=2`.
This observation does not remove the singular-lifted-surface hypothesis.

## 10. Evidence and review status

This is a conceptual argument; no inherited verifier or accepted proof
was rerun. New calculations are the exact ruled-surface cohomology in
Section 4, the embedded smoothing argument in Section 5, and the scope
bridge retaining the original singular root while using a smooth
numerically equivalent curve on `T`.

The linked independent audits both record PASS for the fixed-C0
conditional statements. The degree-e observation in Section 9 remains
separately scoped and is not included in the reported fixed-C0 theorem.
No canonical record is edited or promoted by this note.
