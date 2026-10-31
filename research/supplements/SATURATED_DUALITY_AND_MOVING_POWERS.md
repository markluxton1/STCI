# Saturated duality, root descent and embedded formal surfaces

The first part gives one complete proof of projective normal flatness through saturated Gorenstein duality and a degree-zero resultant, including its balanced spectral interpretation and pure-power corollary. The local Hilbert-envelope proof has its own owner in [Normal flatness](NORMAL_FLATNESS_AND_FILTERED_CI.md). The second part concerns a different object: all-orders embedded formal surfaces along reduced movement-two roots.

[R-0010](../results/saturated_first_relation_normal_flatness.md) governs the canonical saturated-first-relation result. The arbitrary-conormal and characteristic-free extension is retained as an independently reconstructed source-level theorem; this editorial consolidation does not enlarge the canonical record. [R-0018](../results/regular_singular_root_formal_obstruction.md) governs the regular-formal-surface exclusion. Neither result supplies a theorem for arbitrary actual equations.

<a id="2026-10-19-filtered-saturated-duality-moving-purepower-bridge"></a>
<a id="2026-10-19-filtered-saturated-duality-moving-purepower-independent-audit"></a>

## Projective normal flatness by duality and resultants

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
in [the independent socle audit](SOCLE_AND_LOEWY_BOUNDS.md#source-2026-10-13-generalization-socle-independent-auditmd),
and the root-quotient identification of R-0008 and its
[independent evidence](MOVING_POWER_AND_SPECTRAL_ROOTS.md#2026-10-14-generalization-spectral-root-curve-independent-audit).
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
[nonreduced-root obstruction](FIRST_RELATION_AND_SPECTRAL_ROOTS.md#2026-10-19-spectral-nonreduced-root-obstruction)
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
[the normal-flatness proposal](NORMAL_FLATNESS_AND_FILTERED_CI.md#2026-10-19-filtered-generic-ci-normal-flatness);
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


## 2026-10-19-singular-root-investigation

# Reduced movement-two roots: the remaining formal surface must be singular

Date: 2026-10-19. Author: `singular_roots` research agent.

Status: the regular-formal-surface statement is promoted in [R-0018](../results/regular_singular_root_formal_obstruction.md); its additional observations retain source-level scope.
The separate audits are
[the smoothing audit](SATURATED_DUALITY_AND_MOVING_POWERS.md#source-2026-10-19-regular-singular-root-smoothing-auditmd) and
[the equal-slope two-component audit](SATURATED_DUALITY_AND_MOVING_POWERS.md#source-2026-10-19-regular-reducible-root-independent-auditmd).
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

## 2. Regular-formal-surface theorem

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
[the preserved independent branch review](FINITE_ROOT_FAMILIES_AND_SMOOTH_OBSTRUCTIONS.md#source-2026-10-15-formal-branch-ruled-model-degree-bound-reviewmd).
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

## Characteristic scope of descent, duality and formal lifting

Saturated MCM duality and the arbitrary-conormal degree-zero resultant proof use no separability or division by an integer, as their explicit proofs show. The full-root Picard criterion is likewise valid in arbitrary characteristic. The moving-pure-power shortcut uses the characteristic-zero apolar quotient formula, and the theorem excluding repeated moving total components uses detection of integral ruling degrees by logarithmic Chern classes; the [fixed-degree apolar extension](MOVING_POWER_SECOND_RELATION.md#positive-characteristic-reach-of-the-pure-power-mechanism) requiresp>s, while the [repeated-component extension](FIRST_RELATION_AND_SPECTRAL_ROOTS.md#prime-to-characteristic-spectral-descent-excludes-repeated-moving-components) requiresp∤s on the rational base. No unrestricted positive-characteristic extension is asserted. In characteristicp, on the diagonal D of P1×P1, A=O(-1,1) restricts trivially to D and A^p restricts trivially to2D because (1+h)^p=1 modulo I_D². Thus the doubled-divisor Picard injectivity step fails exactly where integer detection fails.

The smooth formal-root theorem R0005 and actual-CI smooth-root bridge R0006 have separately reviewed characteristic-free scopes under their explicit balanced-normal/smooth-full-root/actual-generation hypotheses. The bridge retains inseparable root primes and uses the actual local ring, not a coefficient-field splitting of its completion. The regular-singular-root theorem R0018 below remains in its accepted characteristic-zero scope; the argument does not automatically extend through singular formal surfaces. None of these restricted hypotheses contradicts [the every-positive-characteristic quartic-carrier construction](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier) on the fixed curve.


---

## Source: 2026-10-19-regular-reducible-root-independent-audit.md

# Independent audit: a regular formal surface cannot lift the equal split root

Date: 2026-10-19. Reviewer: `regular_reducible_audit`. The local Cartier,
intersection-length, completion-transitivity, and companion-containment
steps were separately checked by `regular_reducible_audit/local_check`.

Status: **PASS for the precise conditional nonexistence statement below.**
This is an independent review note, not a promoted result record. No accepted
mathematics or canonical metadata is changed. In particular, this note does not
apply the smooth-root statement STCI-R-0005 to a singular root.

## 1. Exact statement and inputs

Work over an algebraically closed field of characteristic zero with the fixed
smooth rational quartic `C0`. Let

    B = Bl_C0(P3),  E = P1 x P1,  O_E(E) = O_E(7,-1).

The first factor is the base `C0`. Fix `q >= 1`, and let `D1,D2` be distinct
smooth integral divisors of class `(1,q)` on `E`. Put

    Z = D1 union D2

with its reduced scheme structure. Suppose compatible embedded effective
Cartier lifts on all exceptional neighborhoods produce a Cartier formal
surface `V` in `B-hat_E`, whose reduction modulo the exceptional parameter is
exactly `Z`.

**Claim audited.** Such a lift cannot have `V` regular at every point of at
least one full component `Di`.

The words “at every point” are essential: regularity only at the generic
point of a component is automatic here and does not satisfy this hypothesis.
The assertion permits arbitrary tangency and intersection multiplicities
between `D1` and `D2`.

The accepted blowup conventions and the branch normalization, resolution,
multiplicity, and plane-genus mechanisms are recorded in
[STCI-R-0005](../results/smooth_root_formal_obstruction.md) and its
[independent source audit](FINITE_ROOT_FAMILIES_AND_SMOOTH_OBSTRUCTIONS.md#2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit),
especially Sections 1--3 and 5--6. They are used within their stated scope;
the accepted smooth-root exclusion itself is not replayed. The new points
checked here are the self-intersection of a component of a reducible root,
the change of completion center, retention of the companion component, and
the resulting numerical contradiction.

The primary algebraicity input is
[Bost, Theorem 3.5 and Corollary 3.8, printed pp. 187--188](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf#page=27).
The smooth-center version applies to a smooth connected projective curve
and a smooth formal surface with ample normal line; its algebraic closure
has the same dimension. The lci-center corollary also permits a proper
connected center that is not smooth. These are geometric results over a
field, with no number-field or analytic-convergence hypothesis. The
accepted source audit checks that the printed dimension condition includes
curves; the text extraction of the PDF loses the equality stroke.

## 2. Local algebra and the component normal degree

Write `E=(u)`. At an intersection point `p`, choose equations `a,b` of
`D1,D2` on `E` and lifts to the completed regular local ring of `B`.
After multiplying the equation of `V` by a unit, its equation is

    g = a*b + u*h.

At `p`, both `a,b` vanish, so the linear part of `g` is `h(p)*u`.
Consequently regularity of `V` at `p` forces `h` to be a unit. This argument
does not require that `a,b` be independent parameters: it includes tangent
components and higher intersection multiplicities.

Inside the regular full completed local ring of `V` at `p`,

    u = -a*b/h,
    I_D1 = (u,a) = (a),   I_D2 = (u,b) = (b).

Thus both components are Cartier there and

    length O_V,p/(a,b) = length O_E,p/(a,b).

Away from their intersection, the root is smooth and the differential of
its local equation already has a nonzero component tangent to `E`; hence
`V` is automatically regular there. It follows in particular that
regularity along one full `Di` implies regularity along all of `Z`.

The exceptional parameter is a nonzerodivisor on `V`: locally `g mod u`
is a nonzerodivisor on the smooth integral surface `E`, so `u,g` form a
regular sequence. Its zero divisor on `V` is exactly `D1+D2`. Restricting
the associated divisor identity to `D1` gives

    deg N_(D1/V)
       = deg O_D1(E) - (D1.D2)_V
       = (7q-1) - (D1.D2)_E
       = (7q-1) - 2q
       = 5q-1.                                      (1)

This is a normal line of positive degree for every `q>=1`, hence is ample
on the smooth projective curve `D1`. The same computation holds for `D2`.

## 3. Algebraization and why the other component is retained

Complete `V` along `D1`. The inclusion `D1 subset E subset B` permits
completion in two stages; completing `B-hat_E` further along `D1` gives
`B-hat_D1`. The resulting `V-hat_D1` is a closed smooth formal surface in
`B-hat_D1`, admits `D1` as its scheme of definition, and has normal line
(1). Bost's smooth-center theorem therefore gives an integral algebraic
surface `W subset B` containing this formal branch.

Formal containment along `D1` must not be replaced by an unsupported
claim that `W` has only this branch. Nevertheless it forces the algebraic
companion `D2` to be contained in `W`:

1. Choose any `p in D1 intersect D2`; such a point exists because the
   total intersection number is `2q>0`.
2. Let `w` be a local algebraic equation of `W` in `B` near `p`. It is
   zero on `V-hat_D1` and hence in its full maximal-ideal completion at
   `p`.
3. That full completion is exactly the full completion of the original
   `V` at `p`, by transitivity of completion. It contains the completed
   germ of `D2` as the quotient by `(b)` in Section 2. Thus `w` is zero
   in the completion of `O_D2,p`.
4. The map from the noetherian local domain `O_D2,p` to its completion
   is injective. Therefore `w` already vanishes in `O_D2,p`. This gives
   algebraic containment on a nonempty open subset of `D2`; integrality
   of `D2` and closedness of `W` give `D2 subset W` globally.

The argument uses an actual intersection point, the same full completed
branch at that point, and the algebraic curve `D2`. Mere abstract
isomorphism of formal surfaces would not justify it. Nor would it
justify retaining a second component disjoint from the completion center.
Here it gives scheme-theoretic containment of the reduced curves
`D1+D2` in the effective Cartier divisor `W|E` on the smooth surface `E`.

There is a shorter valid route in this specific setting. Section 2 shows
that `V` is smooth along its entire support `Z`; the center `Z` is proper,
connected, and Cartier in `V`. Its normal line is `O_Z(E)`, of degree
`7q-1>0` on each irreducible component, hence ample on `Z`. Bost's lci-center
Corollary 3.8 then algebraizes the full `V` directly, and reduction modulo
`u` immediately retains both components. The smooth-center route above
also proves the proposed continuation step explicitly.

## 4. Normalization, degree, and Hodge index

The selected formal branch is regular. On the algebraic normalization
of `W` it lifts uniquely and is the completion of a regular neighborhood
of an embedded copy of `D1`. This is the same finite-normalization and
whole-curve gluing mechanism checked in Section 3 of the accepted source
audit, now applied to the smooth center `D1`. Extra algebraic branches
are allowed. Resolve the normalization away from this regular
neighborhood, obtaining a smooth projective surface `T` with

    D1^2 = 5q-1.

Since `u` is nonzero on the selected formal branch, `W` is distinct from
`E`. Its image `S subset P3` is an integral surface and `W` is its strict
transform. Let `H` be the pullback to `T` of a hyperplane and put
`d=deg S`. Then

    H is nef,  H^2=d>0,  H.D1=4q.

Hodge index on `T` gives

    d*(5q-1) <= (4q)^2,
    d <= 16q^2/(5q-1) <= 4q,                         (2)

where the last inequality is equivalent to `q>=1`. No ruled-surface
classification or strict high-self-intersection threshold is needed for
this equal split case.

Let `m` be the generic order of `S` along `C0`. The restriction `W|E`
has degree `m` on a generic exceptional fiber and contains `D1+D2`.
Each component has fiber degree `q`; thus

    m >= 2q.                                         (3)

This lower bound remains valid with every additional algebraic branch,
exceptional intersection component, and multiplicity retained.

## 5. Numerical contradiction

The accepted plane-section argument for an integral degree-`d` surface
of generic multiplicity `m` along the smooth quartic gives

    (d-1)(d-2) >= 4m(m-1)
                >= 4(2q)(2q-1)
                 = 16q^2-8q.                        (4)

It uses a general integral plane section, transverse intersection with
the four points of `C0`, and the arithmetic genus after blowing up those
points. No assumption of ordinary plane singularities or absence of
residual surface branches is present.

For positive integral `d<=4q`,

    (d-1)(d-2) <= (4q-1)(4q-2)
                = 16q^2-12q+2
                < 16q^2-8q,

because the positive difference is `4q-2`. This contradicts (4). The
boundary `q=1` is included: (2) gives `d<=4`, whereas (4) demands at least
`8` on its left side, whose maximum in that range is `6`.

## 6. Outcome, limitations, and frontier impact

The proposed theorem passes the audit after making the following points
explicit: regularity is along a full component, not just generically;
the normal degree is computed in the regular formal surface; completion
along the component retains the same full local branch at its
intersection with the companion; and companion containment is an
algebraic consequence of local vanishing, rather than an assumed
equality `W|E=Z`.

This excludes an all-orders Cartier lift of the specified reduced equal
split root whenever its total formal surface is regular along `Z`.
It does not exclude a lift whose formal surface is singular at one or
more points of `D1 intersect D2`, roots with different component classes,
nonreduced roots, or any actual complete intersection without a separate
bridge to this exact formal-lift setting. In particular it supplies no
unrestricted characteristic-zero STCI conclusion.

Authority status remains **reviewed proposal/evidence, not promoted**.
No new computation is needed for the argument, and no finite checks or
load-only CAS tests are offered as a substitute for the geometric proof.


---

## Source: 2026-10-19-regular-singular-root-smoothing-audit.md

# Independent audit: regular formal surfaces with singular movement-two roots

Date: 2026-10-19. Reviewer: `regular_singular_smoothing_audit`.

**Outcome: PASS for the precise conditional nonexistence statement below.**
The new smoothing step is valid. It closes the reduced singular-root case
only when the resulting formal surface is regular at every point of the
whole root. The argument does not establish that an arbitrary all-orders
Cartier lift, or an arbitrary actual complete intersection, has this
regularity property. No canonical result has been changed by this audit.

## 1. Exact scope and authority

Work over an algebraically closed field `k` of characteristic zero with the
fixed rational quartic `C0` and the accepted balanced normal bundle
`N_(C0/P3)=O_P1(7)^2`. Put

    B=Bl_(C0)(P3), E=P1_base x P1_direction,
    O_E(E)=O_E(7,-1), H|E=O_E(4,0).

Let `r>=2`, and let `Z` be a **reduced effective Cartier divisor** of class
`(2,r)` on `E`, finite flat of degree `r` under the first projection
`p:Z->P1_base`. Suppose compatible embedded effective Cartier lifts of
`Z` on every exceptional neighborhood define a formal surface `Vhat` that
is **regular along all of `Z`**. Then such a lift does not exist.

The promoted input [STCI-R-0005](../results/smooth_root_formal_obstruction.md)
concerns a smooth full root; its [accepted independent audit](FINITE_ROOT_FAMILIES_AND_SMOOTH_OBSTRUCTIONS.md#2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit)
supplies the algebraic branch, ruled-model degree, and plane-section
arguments used as premises here. This review checks their new interface
with a singular root and supplies the new smoothing argument. It does
not reopen the inherited proof or its accepted numerical inequalities.
[STCI-R-0011](../results/moving_nonreduced_spectral_root_obstruction.md)
is not needed: ampleness and smoothing below hold for every finite-flat
root of the indicated class, including components of differing slopes.

## 2. Normal line, connectedness, and algebraization

Let `u` be an exceptional equation and `g` a local equation of `Vhat`.
Since `g mod u` cuts out the Cartier divisor `Z` in `E`, `u` remains a
nonzerodivisor on `Vhat`, and

    I_Z O_Vhat=(u,g)O_Vhat=(u),
    N_(Z/Vhat)=O_Z(E)=:N=O_Z(7,-1).

Thus the exceptional topology on `Vhat` is its `Z`-adic topology. In
particular it is a closed formal subscheme of `B` completed along `Z`.
Regularity of `Vhat`, rather than smoothness of `Z`, is the hypothesis
that gives a smooth formal surface over the perfect field `k`.

The exact sequence

    0 -> O_E(-2,-r) -> O_E -> O_Z -> 0

and Kunneth show `H0(O_Z)=k`, because `H0(O_E(-2,-r))` and
`H1(O_E(-2,-r))` vanish. Hence `Z` is connected. Each irreducible component
has class `(a,b)` with `0<=a<=2`; finiteness over the first factor gives
`b>=1`. Consequently

    deg(N|component)=7b-a >= 5.

The normal line is therefore ample on `Z`, without any descent or
equal-slope hypothesis. The finite-projection hypothesis matters here:
a vertical fiber of class `(1,0)` would instead have normal degree `-1`.

[Bost, Corollary 3.8, printed p. 188](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf#page=28)
allows a proper connected lci scheme of definition in a smooth formal
scheme and assumes its normal bundle ample; it does not require that
scheme of definition to be smooth. It gives an integral algebraic
closure `W` of dimension two containing the formal branch. The dimension
condition is `dim Z>=1`; the PDF text extraction renders its sign
incorrectly. This is the appropriate variant for singular `Z`.

## 3. Normalization still preserves the entire singular root

At a closed point `z` of `Z`, the maximal-ideal completion of the chosen
formal surface is regular of dimension two. It is a minimal completed
branch of the integral algebraic surface `W`. Excellence identifies the
completed normalization factors of `W` with the normalizations of its
completed branches. The selected branch is already normal and regular.
See [Stacks, Lemma 15.110.8 and its proof](https://stacks.math.columbia.edu/tag/0C2E).

The compatibility argument in the accepted smooth-root audit uses only
normality of the formal surface. On a normal-domain formal chart with
ring `R`, the algebraic coordinate domain of `W` injects into `R` through
the chosen minimal branch. Every element of its finite integral closure
maps into `Frac(R)` and is integral over `R`, hence belongs to `R`.
Uniqueness makes these maps agree on overlaps. The resulting morphism
`Vhat->Wnu` reduces to a section

    Z -> Wnu x_W Z -> Z.

Because normalization is finite, this section is a closed immersion.
Its image is a copy of the original `Z`, including its singularities,
and `Wnu` is regular along it. The formal neighborhood of that image is
the selected branch. This does not identify any additional branch of
`W` with it.

Resolve the projective normalization away from this regular neighborhood,
obtaining a smooth projective surface `T` containing the unchanged
Cartier curve `Z`. Resolution preserving a regular open is available
for surfaces; see [Stacks, Resolution](https://stacks.math.columbia.edu/tag/0BGJ)
and the accepted branch audit cited above. If `S` is the integral image
surface in `P3` and `H` is its hyperplane pullback to `T`, then

    Z^2=deg N=7r-2,   p_a(Z)=r-1,
    H.Z=4r,          H^2=d=deg S>0.

`W` is not `E`, since `u` is nonzero on the formal surface. Thus `W` is
the strict transform of `S` and the map to `S` is birational. `H` is nef.

## 4. Independent cohomology calculation

The divisor sequence tensored by `O_E(7,-1)` is

    0 -> O_E(5,-r-1) -> O_E(7,-1) -> i_*N -> 0.

Push this sequence along the first projection `p_E:E->P1`. Both direct
images of `O_E(7,-1)` vanish, while

    R1(p_E)_* O_E(5,-r-1)=O_P1(5) tensor H1(P1,O(-r-1)).

Since the latter vector space has dimension `r`, this gives the stronger
identity

    p_*N = O_P1(5)^r.                                      (1)

In particular

    H1(Z,N)=0,  H1(Z,N tensor p^*O_P1(-1))=0,
    h0(Z,N)=6r.

For a finite morphism, `p^*p_*N -> N` is surjective: on affine rings it
is the multiplication map `B tensor_A M -> M`. Equation (1) therefore
proves that `N` is globally generated. These assertions do not assume
that `Z` is integral or nonsingular. Equivalently, the two proposed
Kunneth computations have kernels `O_E(5,-r-1)` and
`O_E(4,-r-1)` respectively and give the same vanishings.

## 5. Smoothing on the fixed algebraic surface

This is the new step. Embedded deformations of the Cartier curve `Z` in
the smooth surface `T` have tangent space `H0(N)` and obstruction space
`H1(N)`. Local lifts exist by lifting a regular sequence. Thus the Hilbert
scheme of `T` is smooth at `[Z]`. For a source that explicitly covers a
singular lci subscheme, use [Hartshorne, *Lectures on Deformation Theory*,
Theorem 6.3 and its following remark, and Theorem 9.3](https://math.berkeley.edu/~robin/math274root.pdf#page=42).
The introductory Theorem 1.1 alone assumes a nonsingular subscheme and
would not by itself justify this application.

Choose a smooth integral neighborhood `A` of `[Z]` in the Hilbert scheme,
and let `U subset T x A` be its universal curve. After shrinking `A`, it
is a relative effective Cartier divisor. Locally, the universal ideal
reduces to the principal Cartier ideal `(f)` on the central fiber;
flatness and Nakayama lift its generator to a local equation `F`.
Properness lets these local neighborhoods cover every nearby fiber.
The relative Cartier criterion is [Stacks, Lemma 31.19.9](https://stacks.math.columbia.edu/tag/062Y).

At a closed point `z` of the central `Z`, choose parameters `t_j` on `A`
whose tangent vectors form a basis of `H0(N)`. Modulo the central ideal,
the coefficients `partial F/partial t_j` are precisely the evaluations
of those normal sections. Global generation gives one with nonzero value
at `z`. Hence `F` is not in the square of the maximal ideal of the smooth
ambient `T x A`, and `U` is regular, equivalently smooth over `k`, at `z`.
This also covers the original singular points of `Z`.

The nonsmooth locus of `U` over `k` is closed. Its image in `A` is closed
because `U->A` is proper, and it misses `[Z]`. Shrink `A` again to make
all of `U` smooth over `k`. The generic fiber of `U->A` is regular,
since its local rings are localizations of regular local rings of `U`.
Its field `k(A)` is perfect in characteristic zero, so this generic
fiber is smooth. The nonsmooth locus of the morphism `U->A` consequently
has proper closed image. There is a nonempty open of smooth fibers.
Here one must distinguish smoothness of the total space over `k` from
smoothness of its map to `A`; generic smoothness and properness supply
the latter only over a dense open. For the field-smoothness criterion see
[Stacks, Lemma 33.25.2](https://stacks.math.columbia.edu/tag/04QP).

Since `h0(O_Z)=1`, upper semicontinuity gives `h0(O_(U_a))<=1` near
`[Z]`; the fibers are nonempty, so this equals one. A smooth proper fiber
over algebraically closed `k` is therefore connected and integral.
See [Stacks, Lemma 36.32.1](https://stacks.math.columbia.edu/tag/0BDN).
Thus a nearby smooth connected curve `Z_a subset T` exists. The universal
Cartier family over connected `A` makes it algebraically equivalent to
`Z`, so

    Z_a^2=7r-2,   g(Z_a)=r-1,   H.Z_a=4r.                 (2)

No claim that this smoothed curve lies on the original exceptional
divisor, or that it yields a new embedded formal lift in `B`, is needed.
Its only role is to permit the established ruled-surface numerical
argument on `T` with the invariants (2).

## 6. Numerical contradiction and boundary

For `r>=2`,

    7r-2 > 4(r-1)+5.

Apply the accepted high-self-intersection and nef-divisor argument to
`Z_a subset T`. [Hartshorne, *Curves with high self-intersection on
algebraic surfaces*, Theorem 4.1](https://www.numdam.org/item/PMIHES_1969__36__111_0.pdf#page=12)
gives the ruled model near this smooth curve; the accepted intersection
argument gives

    d <= max_(a integer >=1) [8ra-(7r-2)a^2] = r+2.        (3)

For the opposing bound, use the **original** `Z`, not its smoothing.
Formal containment in `W` reduces modulo `u` to scheme-theoretic
containment `Z subset W|E`. The difference is effective on the smooth
surface `E`. Its generic fiber degree shows that the generic
multiplicity `m` of `S` along `C0` satisfies `m>=r`. Extra exceptional
components or other branches can only add effective fiber degree.
The accepted general-plane-section argument now gives

    (d-1)(d-2) >= 4m(m-1) >= 4r(r-1).                   (4)

But (3) gives `(d-1)(d-2)<=r(r+1)`, and

    4r(r-1)-r(r+1)=r(3r-5)>0  for every r>=2.

This contradiction passes the proposed exclusion.

The added hypothesis is regularity of the **whole formal surface**.
At a singular point of the reduced root, smoothness of the ambient
threefold and the Cartier property of the formal equation alone do
not imply it. If the formal equation is locally `g=f+u*a+...` with
`df=0` on `E`, regularity requires a nonzero linear contribution in
the transverse direction, for example `a(z)!=0`. The audit does not
prove that contribution exists for every root lift. Singular formal
surfaces remain outside this theorem, as do arbitrary actual complete
intersections without a bridge to the stated formal object.

The proof of Sections 2--6 in fact does not use reducedness once a
finite-flat effective Cartier `Z` of class `(2,r)` and a regular formal
surface are supplied: the component ampleness criterion, sequence (1),
and universal-family smoothing still apply. This is a transparent
scope strengthening of the argument, not a claim that nonreduced roots
in the actual STCI problem satisfy its regularity hypothesis.

## Review record

The reviewer independently reconstructed the normalization and smoothing
interfaces and both cohomology calculations. A separate subreviewer,
`smoothing_check`, checked the Hilbert universal-family argument and the
primary deformation, relative Cartier, and semicontinuity references.
No exact-CAS calculation, inherited proof rerun, canonical promotion,
or git operation was used. The regularity boundary is unresolved by
this argument and must survive any later result promotion.
