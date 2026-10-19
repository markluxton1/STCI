# A saturated first relation forces a uniform normal cone in the generic CI lane

Date: 2026-10-19.
Author: `filtered_algebra/annihilator_audit`, independently reconstructing the
local-family argument proposed by the filtered-algebra worker.
Status: **PROPOSAL WITH INDEPENDENT REVIEW PASS; not promoted.**
Independent audit: [local normal-flatness review](2026-10-19-filtered-local-normal-flatness-independent-audit.md).
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
section 2](2026-10-13-generalization-higher-moment-and-loewy-bounds.md).
The delicate separate restriction calculations and Jordan-block argument
were independently checked in
[the independent socle audit](2026-10-13-generalization-socle-independent-audit.md),
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
[the moving pure-power proposal](2026-10-19-filtered-saturated-duality-moving-purepower-bridge.md).

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
