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
in [the independent socle audit](2026-10-13-generalization-socle-independent-audit.md),
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
