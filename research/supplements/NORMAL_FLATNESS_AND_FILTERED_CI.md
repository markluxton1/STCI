# normal flatness and filtered ci

## Integration guide: what normal flatness actually propagates

The [saturated first-relation theorem](#2026-10-19-filtered-generic-ci-normal-flatness) is conditional on the exact hypotheses recorded there, including the saturated generic initial complete-intersection lane and the fiberwise Hilbert-envelope argument. Its [independent audit](#2026-10-19-filtered-local-normal-flatness-independent-audit) and the nonsaturated failure shield must be retained together.

The [ideal-filtration dossier](IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-ideal-filtrations-independent-investigationmd) explains why arbitrary first-order data cannot reconstruct all higher generators. The [Rees residual dossier](REES_RESIDUAL_AND_EXCEPTIONAL_CYCLES.md#2026-10-19-rees-residual-investigation) exhibits boundary defects that escape generic-algebra budgets, and the [Delta embedding dossier](DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md#delta-embedding-geometry-report) retains the conormal and specialization distinctions.

Thus the normal-flatness result should be used as a **hypothesis-sensitive propagation lemma**, not as a blanket assertion that every moving normal root is forbidden or that the rational quartic is not STCI. The retained examples identify exactly where saturation or special-fiber control matters.

---


Complete mathematical dossier preserving proofs, counterexamples, assumptions, conditional claims and unresolved questions. Source headings below organize the arguments, without promoting results to canonical authority.

---

## 2026-10-19-filtered-generic-ci-normal-flatness

# A saturated first relation forces a uniform normal cone in the generic CI lane

Date: 2026-10-19.
Author: `filtered_algebra/annihilator_audit`, independently reconstructing the
local-family argument proposed by the filtered-algebra worker.
Status: **PROPOSAL WITH INDEPENDENT REVIEW PASS; not promoted.**
Independent audit: [local normal-flatness review](#2026-10-19-filtered-local-normal-flatness-independent-audit).
This note is a research contribution, not a promoted result record. No
canonical record is edited or promoted.

## 1. Exact proposed theorem

Let `k` be algebraically closed of characteristic zero. Let `C` be a smooth
integral curve in a smooth threefold `X`, and let `Y` be an ACTUAL locally
complete-intersection thickening with `Y_red=C`. Put

    I=I_C,       J=I O_Y,       E=I/I^2,
    K_j=ker(Sym^j E -> J^j/J^(j+1)).

Suppose that the FULL generic ordinary initial algebra is the coprime binary
complete intersection of degrees `2<=r<=s`:

    gr_(J_eta)(O_(Y,eta)) = k(C)[x,y]/(f_r,g_s),
    gcd(f_r,g_s)=1.                                         (1)

Assume also that at EVERY point `P` of `C`, after choosing a local curve
parameter `t`, the planar ideal defining the transverse special fiber
`O_(Y,P)^hat/(t)` has exact initial order `r`.                   (2)

Then:

1. Every ordinary power `J^i` is saturated in `O_Y`; equivalently,
   `O_Y/J^i` has no finite-support torsion.
2. Every ordinary normal layer `J^i/J^(i+1)` is locally free on `C`.
3. Formation of these layers commutes with the transverse special fiber.
   At every `P`, its Hilbert function is exactly the generic CI Hilbert
   function of degrees `(r,s)`.
4. Every fiber of `gr_J(O_Y)` is an Artinian graded Gorenstein algebra,
   and hence a binary graded complete intersection of degrees `(r,s)`.

The hypothesis concerns the FULL generic initial ideal, not merely two
selected initial symbols. No balanced conormal, pure-power first relation,
projectivity, or rationality hypothesis is used.

Here is a convenient sufficient condition for (2). If `r<s`, the actual
first relation sheaf `K_r` has generic rank one; it suffices that `K_r` be
a line subbundle of `Sym^r E` (the actual first relation is saturated).
If `r=s`, the corresponding rank-two first kernel being a subbundle is
sufficient. More generally it is enough that the actual degree-`r` kernel
contain locally a relation whose image in `Sym^r E` is nonzero at `P`.
The proof of this sufficient condition is included below; saturation is
not silently substituted for an actual relation.

## 2. Accepted dependency and verified external statement

The accepted codimension-two Gorenstein Hilbert-function drop theorem is
used as an input. It states that if a planar Artinian local Gorenstein
algebra has first ideal order `r`, then its Hilbert function begins
`1,2,...,r` and subsequently drops by at most one at each step.

Its characteristic-free proof is preserved in
[Reflection, higher moments, and sharp codimension-two Loewy bounds,
section 2](OCT13_THICK_EQUALITY_SOCLE_AND_FILTRATIONS.md#source-2026-10-13-generalization-higher-moment-and-loewy-boundsmd).
The delicate separate restriction calculations and Jordan-block argument
were independently checked in
[the independent socle audit](OCT13_THICK_EQUALITY_SOCLE_AND_FILTRATIONS.md#source-2026-10-13-generalization-socle-independent-auditmd),
section 6. These inherited proofs are inputs and were not rerun here.

A current primary research statement was directly checked during this
investigation: J. Jelisiejew, S. K. Masuti, M. E. Rossi,
*On the Hilbert function of Artinian local complete intersections of
codimension three*, arXiv:2202.04021v3 (1 August 2023), printed page 7,
equation (3.2):

    |h_i-h_(i-1)| <= 1.

The statement concerns codimension-two local Artinian Gorenstein/complete
intersection Hilbert functions. It credits Macaulay, Briancon, and
Iarrobino, and refers to Bertella's Theorem 2.6 for realizations.
Verified primary PDF: <https://arxiv.org/pdf/2202.04021>.

The new contribution is the passage from this accepted numerical theorem
to uniformity of ALL ordinary normal powers in an ACTUAL thickening.
The proof is independent of the global spectral/apolar bridge in
[the moving pure-power proposal](SATURATED_DUALITY_AND_MOVING_POWERS.md#2026-10-19-filtered-saturated-duality-moving-purepower-bridge).

## 3. Purity, the local finite free algebra, and exact special order

Set

    n=rs,                 d=r+s-2.

These are respectively the generic length and generic last nonzero normal
degree in (1). The actual sheaf `O_Y` is Cohen--Macaulay of dimension one,
and is pure with unique reduced support `C`.

The ideal `J^(d+1)` is zero generically along `C`. It would therefore be a
finite-support submodule of the pure sheaf `O_Y`; hence

    J^(d+1)=0 EVERYWHERE.                                  (3)

Fix a closed point `P`. Complete and choose regular coordinates `(t,x,y)`
on `X` with `I=(x,y)` and `t` a parameter on `C`. Then

    A = O_(Y,P)^hat = k[[t,x,y]]/(F,G),
    R = k[[t]].                                           (4)

The normal variables are nilpotent because `Y_red=C`, so `A` is finite over
`R`. Purity makes `t` a nonzerodivisor. Thus `A` is finite free over the DVR
`R`, of rank `n`. The special fiber

    B=A/tA = k[[x,y]]/(F(0,x,y),G(0,x,y))                  (5)

has length `n`. It is a planar Artinian complete intersection: quotienting
the regular sequence `(F,G)` by the nonzerodivisor `t` preserves the
Cohen--Macaulay codimension count. In particular `B` is Gorenstein.
Writing `m=(x,y)B`, equation (3) gives `m^(d+1)=0`.

For clarity, the sufficient saturated-first condition really gives exact
order `r` in (5). First the ideal of `Y` satisfies

    I_Y subset I_C^r.                                     (6)

Indeed this containment holds at the generic point by (1). The sheaf
`O_X/I_C^r` has a filtration with vector-bundle layers `Sym^j E` on the
smooth curve, so it is pure of dimension one. The image in this sheaf of
any local section of `I_Y` is generically zero, and consequently zero.
This proves (6), and every element of the special planar ideal has order
at least `r`.

Because of (6), the actual kernel `K_r` is the image of actual equations
in `I_Y` modulo `I_C^(r+1)`. A local section of `K_r` whose value at `P` is
nonzero can therefore be lifted locally to an actual equation `Q` of `Y`
whose degree-`r` normal symbol is nonzero at `P`. Reducing `Q` modulo `t`
gives a special-fiber equation of exact order `r`. Hence the special ideal
has exact order `r`, as required by (2). A line subbundle `K_r` for `r<s`
provides such a section at every point; a rank-two subbundle does so when
`r=s`.

This argument uses actual relation sections. A nonzero generic relation
with a coefficient vanishing at `P` does not meet this condition.

## 4. The sharp Hilbert envelope forces equality in every degree

Let `h_i=dim_k(m^i/m^(i+1))` for the special fiber (5). Its exact first
ideal order `r` gives

    h_i=i+1                  for 0<=i<r.

A nonzero degree-`r` initial form belongs to its initial ideal. Multiplying
this form by binary forms gives independent relations, and therefore

    h_i<=r                   for all i>=r-1.               (7)

Let `e<=d` be the actual special socle degree. Gorensteinness gives
`h_e=1`. By the accepted drop theorem in section 2, consecutive decreases
are at most one, so

    h_i<=e+1-i<=d+1-i        for 0<=i<=e.

Together with `h_i=0` for `i>e`, this yields the termwise upper bound

    h_i <= u_i := min(i+1,r,d+1-i),  0<=i<=d.             (8)

Because `d=r+s-2` and `r<=s`, the right hand side is precisely the Hilbert
function of the homogeneous binary CI of degrees `(r,s)`:

    1,2,...,r-1, r,...,r, r-1,...,2,1.

Its sum is

    sum_(i=0)^d u_i = r(d-r+2) = rs = n.                  (9)

But `sum h_i=length(B)=n`. Every term in (8) is an upper bound and the
total sums agree. Therefore equality holds termwise:

    h_i=u_i  for every i.                                 (10)

In particular the special socle degree is `d`, and its entire Hilbert
function is the generic CI Hilbert function. This establishes an exact
special-fiber conclusion, not merely a bound on generic ranks.

## 5. Constant special Hilbert functions remove every saturation defect

For each `i`, the finite `R`-module

    M_i=A/J^i

has generic rank

    rank_R(M_i)=sum_(j<i) u_j.

Its reduction modulo `t` is exactly the quotient by the ordinary special
maximal-ideal power:

    M_i/tM_i = A/(J^i,t) = B/m^i.

The equality here needs no a priori flatness of `J^i`: the image of the
ordinary ideal power `J^i` under the surjection `A->B` is `m^i` by the
definition of ideal multiplication. Equation (10) gives

    dim_k(M_i/tM_i)=sum_(j<i)u_j=rank_R(M_i).              (11)

By the structure theorem for finite modules over the DVR `R`, a nonzero
torsion summand would increase the left side beyond the rank. Thus every
`M_i` is torsion-free and hence free. Equivalently, every ordinary `J^i`
is saturated in `A`.

The kernel in

    0 -> J^i/J^(i+1) -> A/J^(i+1) -> A/J^i -> 0

is consequently free over `R`. Since the right hand quotient is free,
this sequence also stays exact after tensoring with `k=R/(t)`. Thus the
ordinary normal layer specializes to `m^i/m^(i+1)`. The argument holds
at every closed point of `C`, proving assertions 1--3 of section 1.

## 6. Every graded fiber is a complete intersection

For completeness, the symmetry in (10) gives more than flat graded
vector-space dimensions. In the Gorenstein algebra `B`, one always has

    m^(d+1-i) subset Ann_B(m^i).

The symmetric Hilbert function makes the dimensions equal, so these
ideals coincide. Actual multiplication therefore induces perfect
pairings

    (m^i/m^(i+1)) tensor (m^(d-i)/m^(d-i+1)) -> m^d.

Thus `gr_m(B)` is Gorenstein. A zero-dimensional graded Gorenstein quotient
of a polynomial ring in two variables is a complete intersection (the
height-two Gorenstein ideal has two generators). Its Hilbert series is

    ((1-z^r)(1-z^s))/(1-z)^2,

so the generator degrees are exactly `(r,s)`. Section 5 identifies this
algebra with the fiber of `gr_J(O_Y)`. This proves assertion 4.

## 7. Necessary failure shield: nonsaturated first relation

Consider

    A=k[[t,x,y]]/(x^2-t*y, y^2).

It is finite free of rank four over `k[[t]]`, with basis `1,x,y,xy`, is an
actual lci, and has reduced support the smooth `t`-axis. Over `k((t))`,
eliminating `y=x^2/t` gives `k((t))[x]/(x^4)`: the generic transverse
algebra has first ideal order one and socle degree three. At `t=0`, the
fiber is `k[[x,y]]/(x^2,y^2)`, of first ideal order two and socle degree
two.

The actual degree-one relation is `t*y`, so the first relation sheaf is
not saturated at `t=0`. This is precisely the hypothesis that fails.
Consequently smooth support, actual lci Gorensteinness, and a generic
tangent CI ALONE do not exclude special-fiber degeneration.

The argument also does not apply to the whole intersection when only
`C subset Y_red` is known and other reduced components are present. The
unique-support purity argument yielding (3) is then unavailable for that
whole intersection. No vertical exceptional degeneration is identified
here with an additional component downstairs.

## 8. Optional comparison with ordinary torsion before applying the theorem

Without assuming the exact-order condition, let `P_i` be the saturation
of `J^i` and write

    L_i=J^i/J^(i+1),       T_i=torsion(L_i),
    D_i=P_i/J^i,           C_i=P_i/(J^i+P_(i+1)),
    B_i=P_i/P_(i+1).

The kernel of the canonical map `L_i->B_i` is exactly `T_i`; its image is
`F_i=L_i/T_i`. There are canonical exact sequences

    0 -> F_i -> B_i -> C_i -> 0,
    0 -> T_i -> D_(i+1) -> D_i -> C_i -> 0.                (12)

The second sequence follows by mapping `P_(i+1)/J^(i+1)` to `P_i/J^i`;
its kernel is `(P_(i+1) intersect J^i)/J^(i+1)`, exactly the torsion of
`L_i`. Pointwise lengths therefore satisfy

    length(T_i)=length(D_(i+1))-length(D_i)+length(C_i).

Since `D_0=D_(d+1)=0`, this telescopes to

    sum_i length(T_i)=sum_i length(C_i).                  (13)

These identities compare the two filtrations without equating them in
advance. The theorem above proves that ALL of these finite-support
defects vanish under its exact hypotheses.

## 9. Review status and frontier impact

This remains an unpromoted structural proposal with a full proof. The
linked independent audit records PASS after reconstructing the passage
from an actual saturated first relation to special exact order, the use
of the classical drop theorem only for actual planar Gorenstein fibers,
and the DVR criterion (11). No computation is being represented as a
completed algebraic proof.

Subject to canonical promotion, the theorem supplies a general bridge from a full
generic initial CI and a saturated actual first relation to a uniform
graded CI along the support. Combining it with an applicable global
graded/root obstruction is a SEPARATE step. This note does not prove an
unrestricted STCI theorem and does not exclude nonsaturated first
relations, non-CI generic initial algebras, or intersections containing
additional reduced components.


---

## 2026-10-19-filtered-local-normal-flatness-independent-audit

# Independent audit: local extremal Hilbert function forces normal flatness

Date: 2026-10-19. Reviewer: filtered-algebra worker.
Reviewed proposal:
[2026-10-19-filtered-generic-ci-normal-flatness.md](#2026-10-19-filtered-generic-ci-normal-flatness).
Verdict: **PASS for the exact stated hypotheses; proposal not promoted.**
The reviewer independently reconstructed the specialization and DVR argument,
using the previously accepted codimension-two local Gorenstein drop theorem
as a premise. Accepted proofs and computations were not rerun.

## Scope checked

The curve `C` is smooth integral in a smooth threefold, and `Y` is an
actual lci thickening with `Y_red=C`. The full generic initial ideal is a
coprime binary CI of degrees `2<=r<=s`. The exact transverse special ideal
order is `r` at every point. A saturated actual first relation is a
sufficient condition in the rank-one `r<s` case, with the corresponding
rank-two first subbundle sufficient when `r=s`.

Projectivity, balanced conormal, rationality, and pure-power roots are not
used. The characteristic-zero scope stated in the proposal is safe.
The argument does not establish flatness from two selected generic
symbols when the FULL generic initial ideal is not known.

## Independent reconstruction

Set `n=rs` and `d=r+s-2`. Since `Y` is pure with unique reduced support,
`J^(d+1)` vanishes globally: it has zero generic fiber and cannot be a
nonzero finite-support subsheaf of `O_Y`. This is a statement about the
actual ideal power; it is stronger than a generic nilpotence statement
alone and is indispensable for the special Loewy bound.

At a closed point, choose formal coordinates `t,x,y` with `C=(x,y)`.
The completed local algebra

    A=k[[t,x,y]]/(F,G)

is finite over `R=k[[t]]` because `(x,y)` is nilpotent. The parameter `t`
is a nonzerodivisor by purity, so `A` is a finite free R-module of rank
`n`. The fiber `A/tA` is an actual planar Artin complete intersection,
not merely a quotient whose length is inferred from a tangent model.
Its length is `n`, and its maximal ideal satisfies `m^(d+1)=0`.

The sufficient first-saturation hypothesis really secures the required
exact order. The containment `I_Y subset I_C^r` holds generically, and
`O_X/I_C^r` is pure by its finite filtration with bundle layers on the
smooth curve; thus the containment holds everywhere. A local actual
first-relation section with nonzero value at the point lifts to an
actual equation. Its degree-r term remains nonzero after `t=0`.
Therefore the special ideal has exact order r, not a larger order.
This step fails for nonsaturated first relation sections and was not
silently replaced by generic information.

Let `h_i` be the special Hilbert function and let `e<=d` be its actual
socle degree. The three upper bounds are independent and compatible:

    h_i<=i+1,         h_i<=r,         h_i<=d+1-i.

For the middle bound, at degrees `i>=r-1`, multiply ONE nonzero first
form of degree r by binary forms; polynomial multiplication is
injective, giving at least `i-r+1` independent relations. For `i<r-1`,
the first bound already gives `h_i<=r`.

For the last bound, use the accepted planar Gorenstein drop theorem
backwards from `h_e=1`: `h_i-h_(i+1)<=1` yields `h_i<=e+1-i<=d+1-i`.
For `i>e`, `h_i=0`. Consequently

    h_i<=min(i+1,r,d+1-i),        0<=i<=d.

The right side is exactly the homogeneous CI(r,s) Hilbert function and
has sum `rs`. The actual special fiber also has length `rs`, so every
termwise inequality is equality. This is a maximal-length argument;
it does not infer a full Hilbert function from a single moment or from
an arbitrary Gorenstein symmetry assumption.

For `M_i=A/J^i`, its R-rank is the generic partial Hilbert sum. Its
reduction mod t is `A/(t,J^i)=(A/tA)/m^i`, whose dimension is the SAME
partial sum just proved. The ordinary-power image equality here is
formal under the quotient map and requires no a priori base-change
flatness of `J^i`. A finite R-module decomposes as a free part plus
R-torsion cyclic summands; each nonzero torsion summand adds one to the
mod-t dimension. Thus equality with the rank rules out every torsion
summand. All `A/J^i` are free, so all powers are saturated.

The sequences between consecutive free quotients stay exact mod t;
therefore the ordinary normal layers themselves are locally free and
specialize to `m^i/m^(i+1)`. Finally, the symmetric special CI Hilbert
function and local Gorenstein duality give perfect complementary-layer
pairings. Thus the special associated graded algebra is Gorenstein;
a height-two graded Gorenstein ideal in a two-variable polynomial ring
is generated by a regular sequence. Its Hilbert function fixes the
generator degrees as `(r,s)`.

## Failure shield checked

The example

    k[[t,x,y]]/(x^2-t*y,y^2)

has unique smooth reduced support, is lci and finite flat of length four,
and has generic curvilinear transverse fiber but special CI(2,2).
Its actual degree-one relation is generated by `t*y`; it is nonsaturated
at t=0. Hence it violates the exact-special-order hypothesis and does
not contradict the theorem. It demonstrates why smooth support and a
generic CI initial ideal do not suffice by themselves.

## Conclusion

All new local steps pass. The theorem is a rigorous degree-independent
normal-flatness bridge with an explicit inherited classical drop-theorem
dependency. This audit does not promote a canonical result record and
does not remove nonsaturated or generic non-CI initial patterns from
the unrestricted STCI frontier.


---

## 2026-10-19-normal-flatness-adversarial-audit

# Independent adversarial audit: saturated first relation and normal flatness

Date: 2026-10-19.
Reviewer: independent normal-flatness adversarial worker.
Outcome: **PASS for the exact theorem below.** This is independent proof
review evidence, not canonical promotion. No accepted mathematics or
canonical record was edited.

## Exact scope and evidence

Let `k` be algebraically closed of characteristic zero, let `C` be a
smooth connected projective curve regularly embedded with codimension
two in a smooth threefold `X`, and let `Y` be an actual lci thickening
with `Y_red=C`. Write `J=I_C O_Y` and `E=N_(C/X)^*`. Suppose the FULL
generic ordinary initial algebra is

    gr_(J_eta)(O_(Y,eta))=k(C)[x,y]/(f_r,g_s),
    2<=r<s,                         gcd(f_r,g_s)=1,

and the ACTUAL kernel

    R=ker(Sym^r E -> J^r/J^(r+1))

is a line subbundle of `Sym^r E`. Then every ordinary layer
`J^i/J^(i+1)` is locally free on `C`, and its full graded algebra in
every fiber is a binary graded complete intersection of degrees `(r,s)`.
No splitting or balance of `E` is assumed.

Source statement and resultant proof: section 8 of
[the spectral bridge proposal](FIRST_RELATION_AND_SPECTRAL_ROOTS.md#2026-10-19-saturated-first-relation-spectral-bridge).
The ordinary-power recovery is also detailed in its sections 3 and 6.
The saturation-duality proof is section 3 of
[the filtered-duality proposal](SATURATED_DUALITY_AND_MOVING_POWERS.md#2026-10-19-filtered-saturated-duality-moving-purepower-bridge).
Both sources remain proposals; this audit supplies independent review
of this theorem alone and does not certify other conclusions in them.

## Independent reconstruction

Put `d=r+s-2`. Since `O_Y` is Cohen--Macaulay with sole reduced support
`C`, it has no finite-support subsheaf; hence generic vanishing gives
`J^(d+1)=0` globally. Let `P_i` be the saturation of `J^i` in `O_Y`.
These ideals are multiplicative; the quotients `O_Y/P_i` are MCM, and
`B_i=P_i/P_(i+1)` are torsion-free coherent `O_C`-modules, thus vector
bundles. In particular `P_1=J`. The same argument makes
`S=Ann_Y(J)` a rank-one bundle on `C`.

The generic annihilator identity needs an actual justification beyond
the words "graded Gorenstein." In the generic Artin Gorenstein algebra
`A`, the containment

    (J_eta)^(d+1-i) subset Ann_A((J_eta)^i)

holds by nilpotence. Gorenstein duality gives the length of its right
side as `length(A/(J_eta)^i)`. Symmetry of the generic graded CI Hilbert
function makes this equal the length of its left side. Thus the
containment is equality. Both global annihilators and the `P_i` are
saturated, so

    Ann_Y(P_i)=P_(d+1-i).

Dualizing
`0 -> B_i -> O_Y/P_(i+1) -> O_Y/P_i -> 0` over the one-dimensional
Gorenstein ring `O_Y` is exact because the last term is MCM and its
local `Ext^1(-,O_Y)` vanishes. The annihilator identities identify the
resulting quotient with `B_(d-i)`. Since maps from `B_i` land in `S`,
this gives the perfect pairing

    B_(d-i)=Hom_C(B_i,S)

by actual multiplication. No retraction to `C`, or ordinary-layer
flatness, enters this step.

For `j<r`, the actual relation kernel has generic rank zero and is a
subsheaf of the bundle `Sym^j E`, hence is zero. For `r<=j<s`, the
product `R tensor Sym^(j-r)E` is a subbundle: multiplication by the
nonzero binary form in each fiber is injective with constant rank.
The actual kernel contains it and has the same generic rank. The
quotient is a torsion subsheaf of the locally free quotient by this
product and must vanish. Consequently all ordinary layers through
`s-1` are bundles, and `P_i=J^i` for `i<=s`.

Write `h=deg E`, `a=deg R`, and `ell=deg S`. The first-relation quotient
`A_j` for `j>=r-1` has rank `r` and degree

    deg A_j=(r*j-r*(r-1)/2)*h-(j-r+1)*a.

The perfect pairing of `B_(r-1)` and `B_(s-1)` therefore gives

    ell=(s-1)*h-(s-r)*a/r.

Because `P_s=J^s`, the map `A_s -> B_s` is surjective, with
`B_s=(Sym^(r-2)E)^* tensor S`. Its kernel `T` is a line subbundle and

    t=deg T=s*h-s*a/r.

Locally lift the quotient generator of `T` to a degree-`s` polynomial.
Adding a multiple of the first polynomial leaves its binary resultant
unchanged. The local resultants therefore glue even when this lift
does not split globally. Their generator-scaling exponents `s,r` and
normal-frame determinant weight `rs` give the resultant section of

    (det E)^(rs) tensor R^(-s) tensor T^(-r).

Its degree is `rs*h-s*a-r*t=0`; its generic value is nonzero precisely
by generic coprimality. A nonzero section of a degree-zero line bundle
on the smooth connected projective curve has no zero divisor. Hence
the two local polynomial generators are coprime in EVERY fiber.
The criterion retains repeated roots and nonreduced first-root fibers.

Use `R` and the full degree-`s` preimage of `T` to form the graded
quotient `D` of `Sym(E)`. The local generators have transition
`f' = u*f`, `g' = v*g+q*f`, so their ideals glue without a global
second-generator splitting. Fiberwise coprimality implies that `D` is
a finite locally free graded CI family with top line

    D_d=R tensor T tensor (det E)^(-1).

The natural algebra map `D -> B` is generically an isomorphism and
`deg D_d=a+t-h=ell=deg B_d`. Its top map is thus an isomorphism of
line bundles. At any closed point, a nonzero element in the kernel of
`D_i -> B_i` would pair with some element of `D_(d-i)` to a nonzero
top element, by the perfect CI multiplication pairing in the fiber of
`D`. Algebra-map compatibility would kill that top element, contradicting
the top isomorphism. Thus every graded map is fiberwise injective and,
by equal ranks, an isomorphism of bundles.

Finally `B` is generated in degree one, so actual multiplication gives
`P_i=J^i+P_(i+1)`. Descending from `P_(d+1)=0` proves `P_i=J^i` for
all `i`. This recovers the ORDINARY filtration, rather than proving
only a statement about its saturation.

## Adversarial tests and boundaries

* **Base change:** no ordinary fiber kernel is identified by an
  unjustified base-change operation. Before flatness is proved, the
  argument uses the saturated vector bundles `B_i` and the actual
  sheaf kernels. Fiberwise arguments only occur for those bundles and
  the everywhere-CI family `D`.
* **Nonsplit generators:** only the line quotient `T` is global. The
  resultant and top-line formula are invariant under triangular
  changes of its local lifts.
* **Special support and purity:** no extra reduced component is
  allowed. With residual components present, generic vanishing along
  `C` would not imply global vanishing, and the proof would not apply.
* **Displayed symbols:** coprime displayed leading terms are
  insufficient unless they give the FULL generic initial ideal. Its
  exact symmetric Hilbert function is used in both annihilator
  equality and every graded-rank comparison.
* **Saturation:** a generically nonzero first form alone does not make
  first-relation multiples a subbundle. The actual line-subbundle
  hypothesis is used before any degree argument.
* **Projectivity:** generic nonzero resultant plus degree zero removes
  all special degenerations on the projective curve. This review
  neither silently extends this argument to an affine base nor claims
  that projectivity is necessary in every alternative proof.

No counterexample or proof blocker was found under the stated
hypotheses. There is no unresolved mathematical dependency in this
reconstructed proof beyond the standard local duality and graded CI
facts explicitly used above. Canonical promotion is a separate review
and metadata action. The equal-degree case, nonsaturated first
relations, non-CI generic tangent cones, residual components, and the
unrestricted STCI question remain outside this audit.


---

## 2026-10-19-global-ci-filtration-investigation

# Homogeneous generator rigidity and small-movement arithmetic for C0

Date: 2026-10-19.
Status: **new theorem proposal with independent review PASS; not promoted**.
This note does not edit or promote canonical result records.

## 1. Exact scope and proposed conclusions

Let the ground field be algebraically closed of characteristic zero, and let

\[
C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3.
\]
Suppose an actual homogeneous complete intersection

\[
Y=V(F_a,G_b),\qquad Y_{\rm red}=C,
\]
exists. The equations have no common surface component. Put
\(I=I_C\), \(Q=I_Y\), and \(J=I\mathcal O_Y\). Assume the **full** generic
ordinary initial ideal is a coprime binary complete intersection of degrees
\(2\le r<s\), and the actual first degree-r relation kernel

\[
R=\ker(\operatorname{Sym}^r N_C^*\longrightarrow J^r/J^{r+1})
\]
is a line subbundle. These are exactly the substantive additional hypotheses
of promoted STCI-R-0010. Write

\[
N_C^*=\mathcal O_{\mathbf P^1}(-7)^{\oplus2},\qquad
R=\mathcal O_{\mathbf P^1}(-7r-\epsilon),\quad\epsilon\ge0.
\]
Thus the full first root has class \((\epsilon,r)\) in
\(\mathbf P^1_{\rm base}\times\mathbf P^1_{\rm dir}\).

The new proposed conclusions are:

1. The original homogeneous equations necessarily **both** have exact
   generic normal order r, and their first symbols jointly generate R at
   every point. Their two coefficient sections have positive degrees and
   no common zero. This requires the actual homogeneous two-generator
   presentation, rather than merely an abstract graded CI family.
2. Movement one, \(\epsilon=1\), is impossible, in every normal order and
   every homogeneous degree pair under these hypotheses.
3. For movement two, \(\epsilon=2\), the only possible unordered numerical
   data are

   | r | s | a | b | s-r |
   |---:|---:|---:|---:|---:|
   | 2 | 8 | 8 | 8 | 6 |
   | 2 | 12 | 6 | 16 | 10 |
   | 6 | 21 | 18 | 28 | 15 |
   | 14 | 42 | 48 | 49 | 28 |
   | 15 | 45 | 50 | 54 | 30 |
   | 20 | 60 | 64 | 75 | 40 |

   This is an exhaustive **necessary numerical list**, not an existence
   result or a completed exclusion of the six cases.
4. For each fixed integer \(1\le\epsilon\le8\), only finitely many
   numerical quadruples \((r,s;a,b)\) can satisfy these hypotheses.
   A finite divisor procedure is supplied below. No corresponding claim
   is made here for \(\epsilon\ge9\).

Neither nonsaturated first relations, non-CI full generic initial ideals,
nor intersections with residual curve components are covered.

## 2. Inputs, evidence paths, and authority boundary

- [STCI-R-0010](../results/saturated_first_relation_normal_flatness.md)
  supplies normal flatness of the entire ordinary J-adic algebra under
  the stated hypotheses. Its preserved proof computes the second minimal
  quotient relation T and its degree in
  [the saturated first-relation bridge](FIRST_RELATION_AND_SPECTRAL_ROOTS.md#2026-10-19-saturated-first-relation-spectral-bridge),
  sections 3--6. In the present splitting,

  \[
  \deg T=-7s+\frac{s\epsilon}{r}.
  \tag{1}
  \]

  The second relation is a **quotient relation**. No global second
  polynomial line is assumed.
- The general generator-filtration lemma is proved independently in
  [the generator-filtration audit](OCT13_THICK_EQUALITY_SOCLE_AND_FILTRATIONS.md#source-2026-10-13-generalization-thick-generator-filtration-auditmd),
  sections 1--4. It is a reviewed supporting source, not a separate
  promoted result record. Its general statement applies to a full
  locally CI initial ideal; the application below is enabled by R0010.
  The minimal argument needed here is recorded in section 3, so that
  this additional interface can be independently assessed.
- [STCI-R-0001](../results/quartic_carrier_exclusion.md), especially its
  separately audited factor-reduction consequences, excludes a quadric
  factor in either equation of an STCI presentation, even if that equation
  is reducible or nonreduced. Together with C of type (1,3) on its smooth
  unique quadric, this gives \(a,b\ge3r\) once conclusion 1 is known.
  The historical necessary inequality and exact audit pointer are also
  recorded in [the entirely-thick topic](../results/entirely_thick.md).
  That legacy topic is navigation, not an independent promoted authority.
- [STCI-R-0008](../results/spectral_root_picard_criterion.md) interprets
  the second relation as full-root Picard descent; its integrality
  condition \(r\mid\epsilon s\) also follows directly from (1).
- [STCI-R-0011](../results/moving_nonreduced_spectral_root_obstruction.md)
  may subsequently restrict the movement-two roots to reduced ones;
  its proof is not used in the arithmetic exclusion of movement one.

The new claims in this note remain unpromoted proposals. Independent
reconstruction passed in [the core audit](FIRST_RELATION_AND_SPECTRAL_ROOTS.md#2026-10-19-numerical-first-root-independent-audit)
and [the fixed-movement audit](#2026-10-19-global-ci-filtration-independent-audit).

## 3. The actual generator sequence and why it cannot split

Since the full ordinary initial ideal K is locally generated by a
regular sequence of degrees r,s, put

\[
M=Q/IQ,\qquad
\mathcal F^jM=\operatorname{image}(Q\cap I^j\longrightarrow Q/IQ).
\]
The generator-filtration lemma gives

\[
\operatorname{gr}_{\mathcal F}M=K/(S_+K),
\quad S=\operatorname{Sym}(N_C^*).
\]
Its two graded pieces are R in degree r and T in degree s. Consequently

\[
0\longrightarrow T\longrightarrow
\mathcal O(-4a)\oplus\mathcal O(-4b)
\longrightarrow R\longrightarrow0.
\tag{2}
\]

Here \(M=\mathcal O_C(-a)\oplus\mathcal O_C(-b)\) comes from the
**actual** homogeneous CI ideal. To recall why cancellation does not
invalidate this identification, local lifts f,g of the regular initial
sequence generate Q by finite initial-term elimination followed by Krull
intersection. Any cancellation of leading terms is a Koszul syzygy of
the two regular initial forms. Removing it gives

\[
Q\cap I^j=I^{\max(j-r,0)}f+I^{\max(j-s,0)}g,
\qquad \operatorname{in}_I(IQ)=S_+K.
\]
This proves the stated filtered quotient without assuming a global
change of homogeneous generators or a formal retraction.

The generic length of Y along C is rs. Degree of the complete
intersection gives

\[
ab=4rs.
\tag{3}
\]

Set

\[
P=7r+\epsilon,\qquad Q_0=7s-\frac{s\epsilon}{r}.
\]
Equation (1) says \(R=\mathcal O(-P)\),
\(T=\mathcal O(-Q_0)\), with both P and Q_0 integers. Taking
determinants in (2) gives

\[
4(a+b)=7(r+s)-\frac{\epsilon(s-r)}r.
\tag{4}
\]

If (2) split, uniqueness of the splitting type on \(\mathbf P^1\)
would give \(\{4a,4b\}=\{P,Q_0\}\). Therefore

\[
16ab=P Q_0
=rs\left(49-\frac{\epsilon^2}{r^2}\right)
\le49rs,
\]
contradicting \(16ab=64rs\) from (3). Thus (2) never splits, including
when \(\epsilon=0\).

The quotient map in (2) is given by sections

\[
\alpha\in H^0\mathcal O(4a-P),\qquad
\beta\in H^0\mathcal O(4b-P)
\]
with no common zero. If one were zero, the other would be nowhere zero
and would split the sequence. If either had degree zero, its nonzero
constant value would also split the sequence. Hence both sections are
nonzero and have positive degrees. They are exactly the degree-r first
symbols of the original F and G, expressed in the first relation line.
Thus both original equations have exact generic order r and jointly
generate R everywhere.

The kernel is locally generated by \((-\beta,\alpha)\). Its two
components are also nonzero positive-degree sections. We obtain the
strict interval and movement bound

\[
7r+\epsilon<4a,4b<7s-\frac{s\epsilon}{r},
\qquad 0\le\epsilon<7r.
\tag{5}
\]

The last inequality follows since the right endpoint is positive.
This rigidity is specific to genuine homogeneous C0 complete
intersections; it is not a restriction on arbitrary abstract graded
families admitted by R0008.

## 4. The quadric bound and normalized arithmetic

Neither F nor G has the unique quadric q as a factor, by the accepted
factor reduction and quadric-carrier exclusion included in the
consequences of R0001. Restrict F to the smooth quadric
\(Q\simeq\mathbf P^1\times\mathbf P^1\), where C has class (1,3).
Its exact ambient normal order r implies that the nonzero restriction
vanishes along C to order at least r. Its remaining effective divisor
has class \((a-r,a-3r)\), possibly after subtracting further copies of C.
Therefore \(a\ge3r\); the same reasoning gives \(b\ge3r\).
This argument needs no integrality of F or G.

Put \(t=s/r>1\) and \(k=\epsilon/r\). From (3)--(4) and AM--GM,

\[
7(1+t)-k(t-1)=\frac{4(a+b)}r\ge16\sqrt t.
\]
Since \(k\ge0\), necessarily

\[
t\ge\rho:=\frac{79+16\sqrt{15}}{49}>\frac{23}{8}.
\tag{6}
\]
The inequality \(\rho>23/8\) can be checked exactly by substituting
\(23/8\) into \(49t^2-158t+49\), obtaining \(-15/64<0\).
For \(\epsilon>0\), the first inequality in (6) is strict.

If \(a\le b\), then \(3r\le a\le\sqrt{ab}\). The function
\(x+ab/x\) decreases on that interval. Thus

\[
a+b\le3r+\frac{4s}{3}.
\]
Combining with (4) gives

\[
(5r-3\epsilon)t\le15r-3\epsilon.
\tag{7}
\]
For \(r>3\epsilon/5\), this is the useful upper bound

\[
t\le\frac{15r-3\epsilon}{5r-3\epsilon}
=3+\frac{6\epsilon}{5r-3\epsilon}.
\tag{8}
\]
Finally, (1) gives

\[
r\mid\epsilon s,
\quad\text{equivalently}\quad \epsilon t\in\mathbf Z.
\tag{9}
\]
These inequalities retain all first-root components and impose no
smoothness, irreducibility, or reducedness on the root.

## 5. Uniform exclusion of movement one

Let \(\epsilon=1\). Equation (9) makes t an integer. Equation (6)
forces \(t\ge3\). For every \(r\ge2\), (8) gives

\[
t\le\frac{15r-3}{5r-3}<4.
\]
Thus t=3. But (4) now gives

\[
4(a+b)=28r-2,
\]
which is impossible for integers a,b. This excludes movement one in
the full stated saturated-first-relation, full-generic-CI class, with
no bound on the defining degrees or normal orders.

## 6. Exhaustive movement-two list

Let \(\epsilon=2\). Equation (9) makes t an integer if r is odd and
a half-integer if r is even. Equations (6) and (8) force \(t\ge3\).
For \(r\ge7\), the upper bound is less than 7/2, so t=3. For
\(2\le r\le6\), the possibilities before the final integer-degree
check are exactly

| r | possible s |
|---:|:---|
| 2 | 8, 9, 10, 11, 12 |
| 3 | 9, 12 |
| 4 | 12, 14 |
| 5 | 15 |
| 6 | 18, 21 |

For r=2 the lower bound t>=4 follows directly from
\(8+6t\ge16\sqrt t\), rather than the weaker (6).
For each pair, compute the integer

\[
A=\frac{7(r+s)-2(s-r)/r}{4}.
\]
It must be an integer, and \(A^2-16rs\) must be a nonnegative square
with the correct parity. The roots of \(X^2-AX+4rs\) must be at least
3r. The only survivors from this small table are
\((r,s;a,b)=(2,8;8,8),(2,12;6,16),(6,21;18,28)\).

On t=3, equation (4) gives \(a+b=7r-1\), and the discriminant is

\[
D=(7r-1)^2-48r^2=(r-7)^2-48.
\]
For r>=7 a nonnegative square D=d^2 is equivalent to

\[
(r-7-d)(r-7+d)=48.
\]
Both factors are positive integers of the same parity. Their ordered
factor pairs are (2,24), (4,12), and (6,8), yielding respectively
\(r=20,15,14\). Substitution yields the three remaining rows in the
statement. This factorization proves exhaustion for arbitrarily large r;
a bounded search is not the proof.

## 7. Finiteness for each fixed movement at most eight

Fix \(1\le\epsilon\le8\). Since \(\epsilon t\) is an integer and
\(t>\rho>23/8\), we have \(t\ge3\): the largest possible grid point
below 3 is \(3-1/\epsilon\le23/8\).

If

\[
r>\frac{3\epsilon(2\epsilon+1)}5,
\tag{10}
\]
then (8) gives \(t<3+1/\epsilon\), so t=3. In this range

\[
a+b=7r-\epsilon/2.
\]
Odd epsilon is impossible. For even epsilon=2h the discriminant is

\[
D=(r-7h)^2-48h^2.
\]
A nonnegative square D=d^2 gives

\[
(r-7h-d)(r-7h+d)=48h^2.
\tag{11}
\]
There are finitely many signed integer factor pairs of the nonzero
fixed integer on the right, hence finitely many r and a,b. More explicitly,
the factors in (11) have the same parity and even product, so both are
even. Writing them as 2u,2v gives uv=12h^2 and
r=7h+u+v<=7h+12h^2+1. This bound also covers negative factor pairs.
Together with the small-r cutoff, the following normal-order bounds hold:

| epsilon | bound on r |
|---:|---:|
| 1 | no cases |
| 2 | 20 |
| 3 | 12 |
| 4 | 63 |
| 5 | 33 |
| 6 | 130 |
| 7 | 63 |
| 8 | 221 |

There remain finitely many r satisfying the reverse of (10), but (8)
need not bound s when its denominator is nonpositive. The following
exact factorization handles that stratum and prevents a hidden gap.
For fixed r and epsilon set \(c=7r-\epsilon>0\), as proved in (5).
Eliminate s from (3)--(4) to obtain

\[
\boxed{(ca-16r^2)(cb-16r^2)=4r^2(15r^2+\epsilon^2).}
\tag{12}
\]
The right side is a fixed positive nonzero integer. Its finitely many
signed divisor pairs determine a,b uniquely, after which
\(s=ab/(4r)\) is determined. Keeping only positive integer a,b,s with
all original conditions yields a finite exact enumeration. Thus (11)
and (12) establish finiteness without dropping small-r strata.

For epsilon>=9, the grid may contain t<3 but t>rho (for example
26/9). The argument above no longer proves finiteness; no extension
beyond the literal small-movement scope is asserted.

## 8. Smooth-root consequence and remaining work

Equation (6) with r>=2 forces s-r>=4, hence in particular the gap is
at least two. Conclusion 1 supplies automatically the two-original-
equation order and joint-generation hypotheses in
[STCI-R-0006](../results/actual_ci_smooth_root_bridge.md). Thus for a
**smooth full root**, R0010 plus an actual global homogeneous C0 CI
satisfies the ancillary equation hypotheses of that bridge. The bridge
then supplies its stated finite primitive thickness on the root.

For epsilon=2, promoted R0011 restricts the total root to be reduced;
its possibilities remain an integral (2,r) divisor or, for even r,
two distinct (1,r/2) components. Smoothness is an additional restriction.
The six numerical rows include possible singular and reducible roots
and are not discarded by the present argument. Existing smooth-root
formal nonexistence is an all-orders statement with a nonexplicit
finite empty stage; the finite gaps in the table cannot be compared
with that stage without additional work.

The frontier advances here by excluding movement one under exact
saturated/full-generic-CI hypotheses and reducing movement two to six
numerical rows. It does not classify the remaining root divisors, prove
that one of the six rows lifts, exclude every one of those rows, or
settle unrestricted STCI for C0.

## 9. Verification record

A supplementary exact integer cross-check through r=2000 returned no
movement-one rows and exactly the six movement-two rows above. It
reproduces the arithmetic only. Exhaustion is established by the
factorizations and inequalities in sections 5--7, not by this bounded
check. Independent review must reconstruct the generator-filtration
interface, nonsplitting argument, no-quadric-factor use for reducible
and nonreduced equations, and all finite arithmetic strata.


---

## 2026-10-19-global-ci-filtration-independent-audit

# Independent arithmetic audit: global CI filtration constraints

Date: 2026-10-19.
Reviewer: independent generalized-arithmetic worker.
Outcome: **PASS for the conditional finiteness proposition below.**
This note supplies independent proof review evidence. It does not promote
a canonical record or independently certify the geometric construction of
the generator filtration.

Audited proposal: section 7 of
[the global CI filtration investigation](#2026-10-19-global-ci-filtration-investigation).
The factorization arguments and strict cutoff in that section agree with
the independent reconstruction below.

## Exact scope and dependencies

The geometric application concerns the fixed rational quartic
`C0=[u^4:u^3v:uv^3:v^4]` over an algebraically closed field of
characteristic zero, with conormal bundle `O_P1(-7)^2`. Assume an actual
global complete intersection `Y=V(F_a,G_b)` has reduced support exactly
`C0`, and satisfies the hypotheses of
[STCI-R-0010](../results/saturated_first_relation_normal_flatness.md),
with full generic ordinary initial CI degrees `2<=r<s` and first
relation `R=O(-7r-epsilon)`.

The arithmetic audit takes the following further conclusions as explicit
premises of the proposed global-generator argument:

    epsilon is an integer, 1<=epsilon<=8;
    a,b,r,s are positive integers, r>=2, s>r;
    ab=4rs,                    a,b>=3r;
    4(a+b)=7(r+s)-epsilon(s-r)/r;
    r divides epsilon*s.                                   (A)

STCI-R-0010 is promoted, but does not itself state the actual-generator
exact sequence or its degree consequences. Their proof is an additional
dependency of the geometric application. The restriction `a,b>=3r`
uses the absence of a quadric factor in either actual STCI equation and
its exact normal order `r`. Its inherited supporting evidence is the
[entirely-thick audit](2026-10-06-session-thick-independent-audit.md),
under its stated STCI hypotheses. The legacy
[entirely-thick topic](../results/entirely_thick.md) is navigation, not an
additional ID-bearing promoted theorem. These lower bounds are not
premises for arbitrary intersections with residual components.

**Audited claim.** For each fixed `epsilon` in `1,...,8`, there are only
finitely many unordered quadruples `(r,s; a,b)` satisfying (A). The
proof includes every small `r`, including `5r-3epsilon<=0` and the
endpoint of the large-`r` cutoff. This is numerical finiteness, not
existence of a geometric complete intersection for any surviving tuple.

## Independent derivation of the large-order reduction

Put `t=s/r>1` and `x=epsilon/r>0`. The sum equation and positivity give

    4(a+b)/r = 7(1+t)-x(t-1) < 7(1+t).

Since `ab=4rs`, the arithmetic-geometric mean inequality gives
`a+b>=4sqrt(rs)`. Consequently

    16sqrt(t) < 7(1+t),

and, because `t>1`,

    t>rho=(79+16sqrt(15))/49>23/8.                           (B)

The last strict comparison is exact: it is equivalent to
`sqrt(15)>495/128`, and `15*128^2=245760>245025=495^2`.

Order `a<=b`. For fixed product `ab=4rs`, the function
`z+4rs/z` decreases on `0<z<=2sqrt(rs)`. Since
`3r<=a<=2sqrt(rs)`,

    a+b <= 3r+4s/3.

Combining this with the sum equation gives

    (5r-3epsilon)t <= 15r-3epsilon.                        (C)

This inequality is used as an upper bound only when
`5r-3epsilon>0`.

Define `B_epsilon=3epsilon(2epsilon+1)/5`. If
`r>B_epsilon`, then in particular `5r-3epsilon>0`, and (C) becomes

    t <= 3+6epsilon/(5r-3epsilon) < 3+1/epsilon.             (D)

The divisibility premise in (A) gives `t in (1/epsilon) Z`.
For `1<=epsilon<=8`, its largest possible value below `3` is
`3-1/epsilon<=23/8<rho`. Thus (B) forces `t>=3`, while (D) forces
`t<3+1/epsilon`. Hence

    r>B_epsilon  implies  s=3r.                            (E)

The restriction `epsilon<=8` is essential to this particular argument:
for `epsilon>=9`, lattice values strictly between `rho` and `3` can
occur. No finiteness claim for those movements is established here.

When `s=3r`, the sum equation reduces to

    a+b=7r-epsilon/2.

Thus odd `epsilon` gives no large-order tuples. If `epsilon=2k`, let
`D=b-a>=0`. The product equation gives

    D^2=(7r-k)^2-48r^2=(r-7k)^2-48k^2,

and therefore

    ((r-7k)-D)((r-7k)+D)=48k^2=12epsilon^2.                (F)

The right side is a fixed positive integer. Every solution of (F)
comes from a signed divisor pair of that integer. Parity and positivity
conditions recover integral `r,a,b`; imposing them can only shrink the
finite set. Neither factor can vanish. This proves finiteness in the
large-order range, without an unbounded numerical search.

## Small orders, including a nonpositive denominator

There are finitely many integers `2<=r<=B_epsilon`. Fix any such `r`
and write

    c=7r-epsilon.

For the stated range, `c>=14-8=6>0`. Eliminate `s=ab/(4r)` from the
sum equation in (A). Direct expansion gives the exact factorization

    (c*a-16r^2)(c*b-16r^2)=4r^2(15r^2+epsilon^2).          (G)

The right side is strictly positive, so each integral factor is a
nonzero signed divisor of that fixed integer. There are finitely many
such pairs, and `c>0` recovers at most one `a,b` from each pair.
Retaining only integral `a,b>=3r` and integral `s=ab/(4r)>r`, followed
by the remaining exact conditions in (A), is a finite procedure.
Both-positive and both-negative divisor pairs must be retained before
these filters. The proof never divides by `5r-3epsilon`, and therefore
covers the entire exceptional small-order range.

The cutoff is strict. For example, at `epsilon=7` the tuple

    (r,s; a,b)=(63,198; 189,264)

satisfies (A), with `r=B_epsilon` and
`t=22/7=3+1/epsilon`. It must be processed by (G), not discarded by
the strict large-order argument.

Equations (F) and (G) prove the stated finiteness proposition. They do
not assert that the finite lists have been geometrically excluded, or
that the arithmetic and spectral Picard conditions are sufficient for
lifting to the actual formal neighborhood or to projective equations.

## Explicit bounds and supplementary exact enumeration

For odd `epsilon`, the large-order range is empty, so

    r<=floor(3epsilon(2epsilon+1)/5).

For even `epsilon=2k`, the two factors in (F) have the same parity.
Their product is even, so they are both even. Write them `2u,2v`;
then `uv=12k^2` and `r=7k+u+v`. Positive divisor pairs satisfy
`u+v<=12k^2+1`, and negative divisor pairs satisfy the same upper
bound. Therefore the large-order range has

    r<=7k+12k^2+1.

This bound also exceeds the small-order cutoff, since

    (12k^2+7k+1)-(24k^2+6k)/5
      =(36k^2+29k+5)/5>0.

The resulting uniform bounds on `r` are `20,63,130,221` for
`epsilon=2,4,6,8`, respectively; for `epsilon=3,5,7` they are
`12,33,63`. For `epsilon=1`, the bound is below `r=2`, proving
numerical nonexistence directly.

The companion standard-library-only script
[global_ci_small_movement_divisor_audit.py](../computations/global_ci_small_movement_divisor_audit.py)
implements (F) and (G), including signed divisors and every endpoint.
Executed command:

```text
python3 research/computations/global_ci_small_movement_divisor_audit.py --show-tuples
```

The exact candidate counts and largest surviving `r` were:

| epsilon | unordered arithmetic candidates | maximum surviving r |
|---:|---:|---:|
| 1 | 0 | none |
| 2 | 6 | 20 |
| 3 | 4 | 3 |
| 4 | 11 | 63 |
| 5 | 9 | 10 |
| 6 | 19 | 130 |
| 7 | 9 | 63 |
| 8 | 19 | 221 |

For `epsilon=2` the script independently reproduced exactly

    (2,8;8,8), (2,12;6,16), (6,21;18,28),
    (14,42;48,49), (15,45;50,54), (20,60;64,75).

The proof of the finite search domain precedes the computation. These
counts concern precisely the arithmetic system (A). Root Picard descent,
ambient obstructions, and geometric realization are not tested.
