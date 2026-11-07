# Actual source incidence and monic differential reductions

Complete mathematical dossier preserving the actual investigations, calculations, exact conditions, negative results, and unresolved boundaries. Administrative commentary is retained pending editorial consolidation, not treated as proof authority.

---

<a id="2026-10-19-independent-investigation-report"></a>

## Independent investigation: saturated normal cones, moving roots, and exceptional cycles

Date: 2026-10-19. Starting branch: `main`.
Research branch: `codex/normal-cone-rigidity-2026-10-19`.

**Status:** research with separate independent audits. The unrestricted characteristic-zero STCI problem
for `C0=[s^4:s^3t:st^3:t^4]` remains open.

### A. Main findings

#### A1. A global normal-flatness theorem for actual lci thickenings

Let `C` be a smooth connected projective curve in a smooth threefold,
`Y` an actual lci thickening with `Y_red=C`, `J=I_C O_Y`, and
`E=N_(C/X)^*`. Suppose:

1. The **full generic ordinary initial ideal** is a coprime binary
   complete intersection `(f_r,g_s)`, with `2<=r<s`.
2. The actual first relation
   `R=ker(Sym^r E -> J^r/J^(r+1))` is a line **subbundle**.

Then every ordinary normal layer `J^i/J^(i+1)` is locally free on `C`,
and every graded fiber is a binary complete intersection of degrees
`(r,s)`. No balanced-conormal assumption, smooth-root assumption, or
joint generation by two chosen displayed symbols is needed. The
characteristic-zero formulation suffices for this investigation.

The proof uses the saturated ordinary powers `P_i`, whose successive
layers `B_i` have perfect complementary multiplication pairings into
the actual socle line `S`. With `d=r+s-2`, generic Gorenstein symmetry
gives `Ann(P_i)=P_(d+1-i)`; exact MCM duality then gives
`B_(d-i)=Hom(B_i,S)`. Saturation of the first relation forces
`P_i=J^i` through `i=s`.

Write `h=deg E`, `a=deg R`. Duality fixes

    deg S=(s-1)h-(s-r)a/r.

The kernel `T` of the degree-s first-relation quotient onto `B_s` is a
line subbundle and has

    deg T=s h-s a/r.

The relative resultant of the first form and this second **quotient**
relation is a generically nonzero section of

    (det E)^(rs) tensor R^(-s) tensor T^(-r).

Its degree is zero. Projectivity forces it to be nowhere zero, hence
the relations are coprime in every fiber. Their abstract graded CI
maps to the saturated graded algebra. The top map is an isomorphism
between equal-degree lines, and perfect graded pairings make every
graded map an isomorphism. Degree-one generation finally gives
`P_i=J^i` for all `i`. This removes the possible later ordinary-layer
torsion rather than assuming it away.

Source: [general theorem and proof, Section 8](SATURATED_DUALITY_AND_MOVING_POWERS.md#projective-normal-flatness-by-duality-and-resultants).
The same note proves the balanced full-root spectral bridge and retains
the nonsplit second-generator extension.
Independent reconstruction: [filtered bridge audit](SATURATED_DUALITY_AND_MOVING_POWERS.md#2026-10-19-filtered-saturated-duality-moving-purepower-independent-audit).
Additional adversarial review: [normal-flatness audit](NORMAL_FLATNESS_AND_FILTERED_CI.md#2026-10-19-normal-flatness-adversarial-audit).

A separate local proof uses the accepted sharp codimension-two
Artinian Gorenstein Hilbert-function bound. Length `rs`, Loewy degree
at most `r+s-2`, and exact transverse first order `r` force the entire
special Hilbert function to equal the CI envelope. A DVR argument then
makes every ordinary layer flat. This second proof removes projectivity
and also treats `r=s` under its explicit constant-exact-order hypothesis;
the saturated first kernel is a sufficient condition of the appropriate
rank. Its [source](NORMAL_FLATNESS_AND_FILTERED_CI.md#2026-10-19-filtered-generic-ci-normal-flatness) and
[separate audit](NORMAL_FLATNESS_AND_FILTERED_CI.md#2026-10-19-filtered-local-normal-flatness-independent-audit)
record the additional classical dependency. It supplies independent
support for A1 rather than a finite check of the resultant proof.

#### A2. Moving nonreduced full roots are excluded in that actual class

Over characteristic zero, let `Z subset P1_base x P1_direction` be a
finite-flat Cartier root divisor of class `(epsilon,r)`, `epsilon>0`.
If `O_Z(0,s)=pi*O(n)` for any `s>0`, then `Z` is reduced. Moreover, if
`g=gcd(epsilon,r)`, its irreducible components have classes

    t_i(epsilon/g,r/g),  t_i positive integers,  sum t_i=g.

In particular, coprime `epsilon,r` force an integral root.

The auxiliary theorem is that

    Pic(P1 x P1) -> Pic(2D)

is injective for every effective divisor `D` with both bidegrees
positive. A trivialization on `2D` makes logarithmic transition
differentials vanish in `Omega_surface|D`; the vanishing
`H1(Omega_surface(-D))=0` then detects both ambient Chern-class
coordinates. A repeated component of a moving spectral root would
contain just such a doubled divisor and contradict injectivity.
Singular and reducible divisors are retained throughout.

Combining A1 with [STCI-R-0008](../results/spectral_root_picard_criterion.md)
and this Picard argument yields a direct exclusion of actual
`C0`-supported lci thickenings whose first full root is moving and
nonreduced, **provided the full generic CI and saturated-first-line
hypotheses hold**. This includes repeated irreducible multisections
and mixtures of components, beyond powers of one moving section.

For movement two, a spectral survivor must be an integral reduced
`(2,r)` divisor, possibly singular, or (for even `r`) a union of two
distinct smooth rational `(1,r/2)` divisors. Ramified nonreduced
**fibers** of a reduced total root remain allowed.

Source: [nonreduced-root proof](FIRST_RELATION_AND_SPECTRAL_ROOTS.md#2026-10-19-spectral-nonreduced-root-obstruction).
Independent reconstruction: [spectral audit](FIRST_RELATION_AND_SPECTRAL_ROOTS.md#2026-10-19-spectral-nonreduced-root-independent-audit).
A shorter general-base argument for moving pure powers is preserved
in [the pure-power note](SATURATED_DUALITY_AND_MOVING_POWERS.md#2026-10-19-filtered-saturated-duality-moving-purepower-bridge).

#### A3. Exact exceptional-cycle balance and new support restrictions

In the broader proper-intersection setting for `C0`, write

    [V(F,G)]=m[C0]+R_res,  delta=deg R_res=de-4m.

Let `p,q` be the exact generic normal orders of the displayed equations.
On the first blowup write the strict-surface intersection cycle as
`R_res~+Y_exc`, and put `lambda=E_exceptional . R_res~`. If
`[Y_exc]=A alpha+B beta` on `P1_base x P1_direction`, then

    B=m-pq,
    A=lambda+7(m+pq)-4(dq+ep).

If all horizontal common first-symbol root components have slope
`base degree / degree over C0 >= rho`, effectivity gives `A>=rho B`.
In an entirely-thick STCI, with `x=d/p`, `y=e/q`, this yields

    ((7-rho)/4)xy+7+rho >= 4(x+y).

The inherited STCI-specific restrictions give `x,y>=3`. Consequently:

- Some common horizontal root component must have slope `<7`.
- If the sole common horizontal root is a graph, its degree is at most
  six.
- If all common horizontal roots have slope at least two, then
  `min(x,y)<=16/5` is excluded, including the normalized pair `(4,4)`.
- For a sole degree-one graph root, `x=3` forces `y>=8`.

These conclusions retain arbitrary vertical exceptional multiplicity.
They concern common roots of the **displayed first symbols**, which
are different from the full initial-ideal root in A1--A2.

The exact balance also gives the residual correction

    7de+28pq+5 delta >=16(dq+ep).

If no residual component lies on the unique quadric, its coefficient
improves from five to one. These are necessary inequalities, not a
residual-existence theorem.

Source: [cycle balance, slope refinement, and examples](../synthesis/blowup_residual_geometry.md).
Independent reconstruction: [cycle audit, including slope addendum](../synthesis/blowup_residual_geometry.md).

#### A4. Counterexamples and actual higher-degree carriers

The local family

    f=t^N u^p+v^a,  g=f+u^b,  a,b>p>=2

has pure support `V(u,v)` and is finite free of rank `ab` over `k[t]`.
Its first strict-surface intersection has vertical coefficient
`N(b-p)`, unbounded while the generic multiplicity and displayed
orders are fixed. On the subsequence `N=aL`, even the full generic
filtered algebra is fixed up to isomorphism. Replacing `g` by `g-f`
removes the vertical component. The source also gives a homogeneous
projective pure-line example. Thus vertical exceptional multiplicity
is neither a residual curve downstairs nor an invariant of the ideal
independent of its chosen generators.

Two explicit one-parameter smooth-quadric normalization families were
also constructed. Their images are actual integral degree-eight
surfaces containing literal `C0`. Each has isolated extra points in
the full inverse support of `C0`, so no member admits a mate of any
positive degree. The simpler family's full inverse support is
computed exactly; at parameter `gamma=1` it is the diagonal plus
exactly five isolated points. These families do not exhaust the
degree-eight projection model.

Source: [actual degree-eight families](PROJECTION_SUPPORT_AND_DIFFERENTIAL_OBSTRUCTIONS.md#smooth-quadric-isolated-inverse-points-prohibit-every-mate).
Independent reconstruction: [carrier audit](PROJECTION_SUPPORT_AND_DIFFERENTIAL_OBSTRUCTIONS.md#smooth-quadric-isolated-inverse-points-prohibit-every-mate).

### B. Dependencies and remaining cases

The investigation used the records
[STCI-R-0001](../results/quartic_carrier_exclusion.md),
[STCI-R-0008](../results/spectral_root_picard_criterion.md),
[STCI-R-0009](../results/moving_purepower_boundary.md), and
[STCI-R-0003](../results/fixed_carrier_conductor_criterion.md)
within their stated scopes. The fixed normal bundle is the
characteristic-zero `N_C0=O(7)^2`. No quartic proof was rerun.

For the numerical `d/p,e/q>=3` input, the exact inherited proof is
the [entirely-thick independent audit](../synthesis/rees_and_vertical_controls.md#supported-cycle-bidegrees-and-the-universal-numerical-restriction).
The [entirely-thick topic](../results/entirely_thick.md) gives the
notation and context for that numerical restriction.
The STCI factor reduction and low-degree exclusion have support
in R-0001 and its linked audit.

The genuinely new bridge is A1, proved in the source and independently
reviewed, rather than an inference from a prior summary. It closes
later special-point normal-layer degeneration within its exact
saturated-first/generic-CI class. A2 then excludes all moving
nonreduced full roots within that actual class. A3 supplies additional
support-sensitive restrictions without requiring that first relation
to be a saturated line.

An independent local Hilbert-function argument is preserved in
[the local normal-flatness proposal](NORMAL_FLATNESS_AND_FILTERED_CI.md#2026-10-19-filtered-generic-ci-normal-flatness).
It has its own classical dependency and a separate
[independent audit](NORMAL_FLATNESS_AND_FILTERED_CI.md#2026-10-19-filtered-local-normal-flatness-independent-audit).
It is also a reviewed proposal. The projective theorem
has the self-contained resultant/duality proof and does not depend on
this additional classical bound or on the local route's broader scope.

### C. Most promising connection

Gorenstein duality controls a finite-support defect that previously
separated generic formal algebra from the full spectral curve. The
second quotient relation has a generically nonzero resultant of degree
zero. This is the mechanism forcing uniformity; generic coprimality
alone would not suffice. It makes the full Picard obstruction directly
applicable to an actual intersection in a nontrivial infinite class.

The blowup work complements that bridge by retaining chosen-equation
and vertical-cycle information. Its counterexamples show why the
uniformity proof must use the full algebra and projectivity, rather
than interpreting vertical degeneration as a residual component.

### D. Remaining obstacles

1. **Nonsaturated first relation.** Determine the torsion and its
   duality constraints when the first actual kernel is not a
   subbundle. The exact early-layer identification used in A1 then
   fails. The local proposal preserves an explicit nonsaturated
   counterexample; saturation cannot simply be dropped.
2. **Non-CI generic tangent algebra.** An actual transverse Artin CI
   can have an ordinary initial ideal with three or more generators.
   Its generic graded algebra need not be Gorenstein. The complementary
   saturated-power duality in A1 then has no established symmetric
   index formula.
3. **Reduced roots and ambient lifting.** A1 provides graded/spectral
   uniformity; it does not supply arbitrary embedded Cartier lifts of
   a singular root in the actual blowup. Integral singular roots and
   distinct-component roots require actual ambient obstruction data.
4. **Exceptional support distribution.** The class `(A,B)` and its
   slope budget do not determine higher contact along each direction.
   A further global constraint on multiplicities is still missing.
5. **Full-support normalization families.** The explicit degree-eight
   exclusions have isolated inverse points. They do not compute phase
   images for projections that actually satisfy the required full
   singleton inverse support, or address all higher carriers.

No shared singular point of arbitrary defining surfaces is assumed.

### E. Recommended continuation and evidence checks

First study the torsion of the earliest nonsaturated relation and how
its length changes the degree-zero resultant calculation. A useful
target is an exact effective-defect formula replacing the zero degree
in A1; one must keep the torsion in every comparison map. In parallel,
investigate codimension-two non-CI generic initial ideals with the
smallest number of additional generators, using their actual
annihilator flags rather than assuming graded Gorenstein symmetry.

For the saturated generic-CI class, direct effort toward reduced
singular roots and the equal-slope rational-component pairs identified
in A2. Additional nonreduced spectral scans are unnecessary in that
class. The chosen-symbol slope theorem gives a separate way to select
surviving normalized-degree regions without conflating the two root
objects.

All principal results have full proof text and separate review evidence; there is no uncompleted elimination computation underlying the reported claims. Mathematical validity rests on those proofs and independent reconstructions, including the separate adversarial review of A1.

The package is recorded at
[the research commit](https://github.com/markluxton1/STCI/tree/6be25be178b1e34e1209172f92dee6816e7aa87b).
The exact closing commit is identified in the investigation message.
Standard external inputs, with direct primary links, are identified in
the respective source and audit notes.

---

<a id="2026-10-16-session-structural-continuation"></a>

## October 16 structural continuation and successor entry

The universal integral-curve STCI question and unrestricted characteristic-zero
`C0=[s^4:s^3t:st^3:t^4]` remain **OPEN**. The October 13
all-branch reconstruction remains an accepted premise; no branch-source
or accepted mathematical verifier was replayed in this continuation.

The current externally observed checkpoint is
`bf124f8ab962ef0ed4085397034c50ee8d0d7162`, title
`2026-10-15 afternoon limit reached`. The primary agent did not create
that commit. This continuation has further working-tree changes.

### 1. The strongest structural generalization

The new [intrinsic finite-root-family theorem](FINITE_ROOT_FAMILIES_AND_SMOOTH_OBSTRUCTIONS.md#2026-10-15-generalization-intrinsic-finite-root-family)
and [independent new-scope audit](FINITE_ROOT_FAMILIES_AND_SMOOTH_OBSTRUCTIONS.md#2026-10-15-generalization-intrinsic-finite-root-family-independent-audit)
remove the rational-base and split-normal-bundle hypotheses from a fixed
bounded smooth-root family. If `A=Z^2_E`, `nu=E.Z`, and
`nu>max(A,0)`, all successive correction lines have negative degree
`A-m nu`. Relative cohomology gives obstruction bundles of rank
`g_Z-1-A+m nu`, compatibly with arbitrary parameter base change, including
nilpotent directions. The embedded-Cartier ideals are unique whenever
they exist, so their closed obstruction schemes remain in one fixed
finite-type space and eventually stabilize as schemes.

For the actual blowup of **any** fixed smooth space curve of degree e
and genus gamma, the actual exceptional ruled surface obeys

```
A=(4e+2gamma-2)r^2-2r nu,
A=2g_Z-2+4er-2nu.
```

Fixed `(r,nu)` fixes numerical class and Hilbert polynomial. One smooth
Cartier Hilbert open therefore contains all smooth connected roots of
that class. If `nu>4g_Z+5`, a hypothetical infinite lift also requires
a positive integer d satisfying

```
d<=max_(a>=1 integer)(2aer-nu a^2),
(d-1)(d-2)>=e r(r-1).
```

Incompatibility makes the stable scheme empty, and gives a finite
uniform empty stage N over the whole fixed family. Under a valid
actual-CI bridge, `s-r<=N`. The theorem does not compute N, bound all
numerical classes, or treat singular/nonreduced roots. Its new intrinsic
proof and audit state characteristic-zero scope.

This contains the preceding balanced-rational movement-two result:
for e>=4 and every r>=2, all smooth roots of class `(2,r)` have no
infinite formal lift. Movement-one roots of order r>=2 are also excluded
for e>=3; for r=1,e>=4, their all-orders lifts are exactly containing
quadric germs smooth along C. The broader inequalities, rather than
separate carrier degrees, are the continuing geometric mechanism.

### 2. Characteristic and actual-CI bridge

The [formal characteristic addendum](FINITE_ROOT_FAMILIES_AND_SMOOTH_OBSTRUCTIONS.md#2026-10-15-generalization-smooth-root-characteristic-scope-addendum)
accepts the balanced-rational formal theorem and finite tower in every
algebraically closed characteristic, with its explicit normal-bundle
and smooth-root hypotheses.

The [inseparable-root actual-CI bridge](UNIFORM_ROOT_TOWERS_AND_INSEPARABLE_BRIDGES.md#2026-10-15-generalization-inseparable-root-blowup-bridge)
now also has a [full independent new-scope PASS](UNIFORM_ROOT_TOWERS_AND_INSEPARABLE_BRIDGES.md#2026-10-15-generalization-inseparable-root-blowup-bridge-independent-audit).
It uses the actual root prime over `k(C)` and an uncompleted standard
basis, retaining inseparable residue fields. The original strict-divisor
intersection is locally `(h,u^(s-r))`, without saturation or removal
of a vertical component. Its Cartier-root stages are precisely those
with `m<s-r`. Thus the same gap bound applies in every characteristic
within the literal saturated-line, joint-leading-generation, full
generic-initial-CI and smooth-full-root hypotheses. No assertion about
literal C0 splitting in bad characteristics is inserted.

### 3. Arithmetic reduction of all mate powers

The [effective rational phase theorem](PROJECTION_TORSION_AND_RATIONAL_PHASE_BOUNDS.md#2026-10-15-generalization-effective-rational-phase-bound)
and [arithmetic review](PROJECTION_TORSION_AND_RATIONAL_PHASE_BOUNDS.md#2026-10-15-generalization-effective-rational-phase-bound-independent-review)
are accepted. For an explicit rational constructible phase image,
Mann's theorem, finite cyclotomic calculations and Smith normal form
give a finite exact coset/boundary certificate. It decides torsion
existence, detects unbounded least mate degrees through a surviving
positive-dimensional coset, and bounds phase orders by `P(S)d^D` if
only isolated cosets survive. The three fixed projection models have
on-C thresholds 5,5,13, so the corresponding least-degree bounds are
that phase bound plus 4 or 12.

The whole fixed normalization families stay over Q, retaining all
branch choices. A stronger corollary starts from finite rational
section/module data for these three fixed models and constructs the
actual phase image by a terminating algebraic procedure; the written
review contains its scope addendum. A fresh
[October 16 raw-input scope audit](EFFECTIVE_PROJECTION_PHASE_DECISION.md#reviewed-claim-and-input)
now passes the final admissibility and generic-freeness formulation.
The precise finite rational input is one of the three fixed source
rings with H,c,Q, four polynomial parameter sections with their prescribed
C0 restrictions, and finite constructible parameter conditions. The
terminating algorithm decides whether any actual carrier in that input
family has any mate, and whether its least mate degrees are unbounded
or admit a computable uniform bound. It does not require an oracle for
unspecified class groups or arbitrary coefficient fields.
No actual phase image, Mann partition list, or family decision has been
computed. Neither practical complexity nor a numerical C0 bound follows
from the existence of the algorithm.

### 4. The dedicated quintic target

Accepted shared reductions now include the global remaining-mate
Delta1 unit, exact q6-to-j scalar binding, eleven-generator reduction,
automatic `(q5,q6)=1`, and the equivalent eight-equation logarithmic
ODE on the declared rational inverse-map chart. The reviewed eta
spectral accelerator retains one ideal rather than separate degree,
root or norm-factor cases.

The new [global monic h2 ODE model](QUINTIC_H2_MONIC_ODE_AND_OPEN_INCIDENCE.md#2026-10-15-generalization-quintic-h2-global-monic-ode-incidence)
is the next whole-h2 target. It uses the original parameters, a monic
quadratic H, four conormal remainders, two actual-conductor remainders,
eight ODE coefficients and three derived accelerators: seventeen equations
in nine variables, with only `delta*E*Delta1` inverted. Its purpose is
to retain the repeated-root and cover-determinant boundary that the
earlier rational inverse-map chart could not cover. The
[final global scope audit](#2026-10-16-generalization-quintic-h2-global-monic-ode-independent-audit)
now passes the whole-h2 cover and current exact artifact bindings. Its
[runnable input](../computations/generalization_quintic_h2_global_monic_ode_input_2026_10_16.m2)
is saved and passed a load-only check. One subsequent capped global QQ
saturation reached GB but produced no result, as recorded below. The one
next saturation target is `h2GlobalIdeal : h2GlobalDomainUnit^infinity`,
with all repeated-root and cover boundaries retained in the same model.

The quintic is not closed. The earlier h3, coprime, endpoint and stated
residual-partition exclusions remain accepted. Other quintic
normalizations and retained h1 singular/intrinsic/common-root scope
remain separate obligations. A whole-h2 unit-ideal certificate would
not by itself prove a whole-quintic theorem.

### 5. Computation and continuation state

The complete global quadratic-root second model uses twenty-five scalar pairings and retains the homogeneous branch discriminant, including infinity. Its completeness is not an emptiness result. The bounded quintic ODE, spectral and global QQ saturation attempts did not complete an ideal computation or unit certificate. The twenty-two finite family-two exception-root closures and accepted large quintic witnesses remain separate premises.

---

<a id="2026-10-16-generalization-quintic-h2-global-qq-prospect-terminal-record"></a>

## Whole-h2 global saturation remains open

The accepted seventeen-equation, nine-variable model over `QQ` retains
repeated roots and the finite cover boundary. Its
[runnable input](../computations/generalization_quintic_h2_global_monic_ode_input_2026_10_16.m2)
loads the exact equations and domain polynomial. The target is

```macaulay2
saturate(h2GlobalIdeal, ideal h2GlobalDomainUnit)
```

on the domain `delta*E*Delta1 != 0`. No rational-cover determinant,
quadratic discriminant, quotient coefficient or `Jbar` is additionally
inverted. A bounded attempt did not complete this saturation and supplied
no ideal, dimension, unit certificate or emptiness conclusion. The global
H2 incidence remains undecided. Its geometric scope is the
[global monic ODE incidence](QUINTIC_H2_MONIC_ODE_AND_OPEN_INCIDENCE.md#2026-10-15-generalization-quintic-h2-global-monic-ode-incidence)
and the [independent argument](#2026-10-16-generalization-quintic-h2-global-monic-ode-independent-audit).

---

<a id="2026-10-16-generalization-quintic-h2-global-monic-ode-independent-audit"></a>

## Independent audit: one global monic h2 ODE incidence

Date: 2026-10-16.

Status: **PASS for the new global monic cover, original-parameter
coefficient assembly, and transfer of the accepted ODE/spectral
algebra to the domain delta*E*Delta1 nonzero.** The seventeen
equations in nine variables retain the finite inverse-map boundary.
This is a necessary incidence for every remaining actual h2 mate
candidate, not an emptiness or mate-existence theorem.

The reviewed proposal is
[the global monic incidence note](QUINTIC_H2_MONIC_ODE_AND_OPEN_INCIDENCE.md#2026-10-15-generalization-quintic-h2-global-monic-ode-incidence).
Accepted conormal forms, the actual octic, the global h2 conductor
factor, previous mate closures, the Delta1 open, and ODE/spectral
proofs are premises. No accepted proof or verifier was replayed.
This audit uses written coefficient calculations and read-only
source/artifact/hash inspection. No CAS was run during completion
of this audit, and no model assembly or elimination was repeated.

### 1. Monic coverage and exact homogeneous gcd degree

For any remaining actual h2 mate candidate, a common factor at source
infinity would force G=j=0 by the accepted leading-coefficient
equations. The accepted mate closure excludes that lane. Thus the
complete degree-two homogeneous gcd has nonzero t^2 coefficient,
and its unique monic representative is

    H(x)=x^2+v*x+w,       x=r/delta=t/s.

This monic chart is therefore global for the remaining h2 mate
candidates. It imposes no distinct-root hypothesis. It also does
not normalize delta to one.

Write the literal normalized cubics as

    P=G*x^3+P2*x^2+P1*x-2a,
    Jc=(G+2j)*x^3+J2*x^2+J1*x-a-B,

where

    P2=6B+delta^2-3delta,       P1=3a-3B+2delta,
    J2=6B+3G+5delta^2-3delta,   J1=3a+3B+delta-delta^2.

Set A=G, Bc=P2-vG, C=G+2j, Dc=J2-v(G+2j). The leading two
coefficients of (Ax+Bc)H and (Cx+Dc)H match the cubics identically.
Their remaining coefficients match precisely when

    -2a-w*Bc=0,       P1-v*Bc-w*A=0,
    -a-B-w*Dc=0,      J1-v*Dc-w*C=0.                  (1)

These are exactly the four saved cover equations, with no coefficient
system inverted. Direct expansion gives

    E=A*Dc-Bc*C
     =G*(3G+4delta^2)-2j*(6B+delta^2-3delta).          (2)

The terms involving v cancel. The unit E is the determinant of the
two homogeneous linear cofactors A*t+Bc*s and C*t+Dc*s. At field
points they are independent exactly when they are coprime, so (1)
and E nonzero give complete homogeneous gcd degree two. This
includes affine degree drops of either cubic. A zero cubic or a
proportional cofactor pair instead has E=0 and is correctly outside
the exact-h2 domain.

### 2. Fixed-degree octic reversal and monic division

For the accepted actual Fdet(p,1)=sum_(i=0)^8 f_i*p^i, reciprocal
source coordinates give Fsrc(1,x)=sum f_i*x^(8-i). Put q7=q8=0
and define downward

    q_i=f_(6-i)-v*q_(i+1)-w*q_(i+2),    i=6,...,0.

For the coefficient of x^(i+2) in H*Q, this is exactly
q_i+v*q_(i+1)+w*q_(i+2)=f_(6-i). Therefore all coefficients
of degree at least two match, and the remaining two coefficients
are exactly

    r0=f8-w*q0,
    r1=f7-v*q0-w*q1,
    Fsrc=H*Q+r1*x+r0.                                (3)

The two explicit equations r0=r1=0 are retained. The accepted
geometric factor theorem supplies them for every actual h2
projection; this assembly does not extend that theorem to a
divisibility assertion over an arbitrary nonreduced
conormal-cover base. After the equations are imposed, (3) is an
exact ring identity on the incidence.

Monic division introduces no parameter denominator. Fixed degree
eight reversal and degree six quotient retain all coefficient drops
and the source point at infinity. In particular q6=f0 and
q5=f1-v*q6 have the intended A4 interpretation.

### 3. The new global domain does not invert Delta or K

The domain is exactly

    delta*E*Delta1 nonzero,
    Delta1=G(G+3delta^2)(G+delta^2+2B)
      +j[(delta^2-5B)G-3B(delta^2+3B)]-B*j^2.         (4)

Delta1 is necessary for all remaining mate candidates by the accepted
closures and A4 support argument. Delta=v^2-4w and
K=v^2+6vw+6w^2+2w are not factors of the declared unit product.
Thus the repeated finite-root boundary and the failed rational
inverse-map boundary remain represented by the original equations.
An accepted inconsistency on part of that boundary may be used as
a theorem, but no such locus is silently cancelled from this model.

For the unscaled actual quotient, the accepted A4 coefficients give

    q6=-3j*Delta1,
    q5=-2(G+3delta^2)*Delta1 modulo j.                (5)

There is no captured inverse-map scalar here. The accepted automatic
open proof now applies with kappa=1: the explicit Delta1-square
membership, or its equivalent quotient-ring argument, gives
(q5,q6)=1 after (4). This is an exact ideal equality and includes
nonreduced bases. It needs neither Delta nor K to be a unit.

The previous ODE and spectral proofs use monic H, (5), the Delta1
unit, coefficient unimodularity and field scalars 2,3. They therefore
apply unchanged to this original-parameter ring before any rational
inverse of the four cover equations. Their earlier actual use on a
smaller inverse-map chart does not limit this algebraic transfer.

### 4. The seventeen-equation system and its precise meaning

Using eta=dv-2u, the eight ODE coefficients are exactly

    2w(i+1)q_(i+1)+[(2i-d)v+eta]q_i
                         +2(i-1-d)q_(i-1),
    i=0,...,7.                                        (6)

These are twice the coefficients of H*q'-(dx+u)q. The change from
u to eta is invertible. The accepted globally unique ODE-witness
argument applies by (5), so (6) is the same shared rank/support
incidence on this domain, including its j=0 allowance.

There are four equations (1), two equations (3) and eight equations
(6), making fourteen. The three accepted derived equations

    (d-5)(d-6),       j(d-6),
    (d-5)P6(eta)+(6-d)P5(eta)

bring the saved presentation to seventeen equations in the nine
variables delta,a,B,G,j,v,w,d,eta. They belong to the same localized
ODE ideal, so appending them changes no scheme on (4). The temporary
variables p and x used in assembly are not additional model variables.

On actual admissible h2 projections, this incidence expresses the
accepted restricted-conductor support obligation. Every remaining
actual h2 mate candidate lies in it. The model does not impose center
avoidance or all original fiber conditions, and it does not establish
full inverse support or nonlinear conductor descent. An algebraic
survivor is therefore not automatically a projection or a mate.

### 5. Exact model and checking boundary

The [assembly source](../computations/generalization_quintic_h2_global_monic_ode_export_2026_10_15_attempt02.m2) derives the model from the literal accepted octic, reversed coefficients, recurrence, four cover equations, eight ODE equations and three accelerators. Its polynomial assertions check the cofactor and quotient/remainder identities. The retained seventeen-equation row and original domain polynomial supply precisely the incidence (4); grouped and individual coefficient exports are redundant representations.

The new currently runnable
[load-only input](../computations/generalization_quintic_h2_global_monic_ode_input_2026_10_16.m2)
reads the completed seventeen-equation row and domain polynomial
over QQ in the stated nine-variable order. It asserts the ring,
matrix shape and nonzero domain polynomial, and retains the objects
h2GlobalRing, h2GlobalEquations, h2GlobalIdeal and
h2GlobalDomainUnit. It constructs no coefficient map and calls no
Groebner basis or saturation operation. The domain polynomial is
loaded as data for a future localization; the load-only script does
not itself localize or prove the domain nonempty.

Loading the completed input checks its ring and equation presentation. It is distinct from assembling the coefficients and supplies no saturation or elimination result.

The one global future target is therefore the saved seventeen-equation
incidence localized at (4). No Gröbner basis, saturation, resultant
or emptiness computation for this global model is certified here.
A result restricted to Delta*K nonzero cannot close this larger
incidence. The unrestricted quintic and STCI questions remain outside
the conclusion of this audit.
