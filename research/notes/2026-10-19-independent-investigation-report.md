# Independent investigation: saturated normal cones, moving roots, and exceptional cycles

Date: 2026-10-19. Starting branch: `main`.
Research branch: `codex/normal-cone-rigidity-2026-10-19`.

**Status:** new research proposals with separate independent audits, not
canonical promotions. The unrestricted characteristic-zero STCI problem
for `C0=[s^4:s^3t:st^3:t^4]` remains open.

## A. Main findings

### A1. A global normal-flatness theorem for actual lci thickenings

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

Source: [general theorem and proof, Section 8](2026-10-19-saturated-first-relation-spectral-bridge.md).
The same note proves the balanced full-root spectral bridge and retains
the nonsplit second-generator extension.
Independent reconstruction: [filtered bridge audit](2026-10-19-filtered-saturated-duality-moving-purepower-independent-audit.md).
Additional adversarial review: [normal-flatness audit](2026-10-19-normal-flatness-adversarial-audit.md).

A separate local proof uses the accepted sharp codimension-two
Artinian Gorenstein Hilbert-function bound. Length `rs`, Loewy degree
at most `r+s-2`, and exact transverse first order `r` force the entire
special Hilbert function to equal the CI envelope. A DVR argument then
makes every ordinary layer flat. This second proof removes projectivity
and also treats `r=s` under its explicit constant-exact-order hypothesis;
the saturated first kernel is a sufficient condition of the appropriate
rank. Its [source](2026-10-19-filtered-generic-ci-normal-flatness.md) and
[separate audit](2026-10-19-filtered-local-normal-flatness-independent-audit.md)
record the additional classical dependency. It supplies independent
support for A1 rather than a finite check of the resultant proof.

### A2. Moving nonreduced full roots are excluded in that actual class

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

Source: [nonreduced-root proof](2026-10-19-spectral-nonreduced-root-obstruction.md).
Independent reconstruction: [spectral audit](2026-10-19-spectral-nonreduced-root-independent-audit.md).
A shorter general-base argument for moving pure powers is preserved
in [the pure-power note](2026-10-19-filtered-saturated-duality-moving-purepower-bridge.md).

### A3. Exact exceptional-cycle balance and new support restrictions

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

Source: [cycle balance, slope refinement, and examples](2026-10-19-exceptional-cycle-balance-and-vertical-counterexamples.md).
Independent reconstruction: [cycle audit, including slope addendum](2026-10-19-exceptional-cycle-and-vertical-family-independent-audit.md).

### A4. Counterexamples and actual higher-degree carriers

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

Source: [actual degree-eight families](2026-10-19-quadric-antidiagonal-fourfold-line-proposal.md).
Independent reconstruction: [carrier audit](2026-10-19-quadric-antidiagonal-fourfold-line-independent-audit.md).

## B. Dependencies, authority, and precise frontier change

The investigation used the promoted records
[STCI-R-0001](../results/quartic_carrier_exclusion.md),
[STCI-R-0008](../results/spectral_root_picard_criterion.md),
[STCI-R-0009](../results/moving_purepower_boundary.md), and
[STCI-R-0003](../results/fixed_carrier_conductor_criterion.md)
within their stated scopes. The fixed normal bundle is the
characteristic-zero `N_C0=O(7)^2`. No quartic proof was rerun.

For the numerical `d/p,e/q>=3` input, the exact inherited proof is
the [entirely-thick independent audit](2026-10-06-session-thick-independent-audit.md).
The legacy [entirely-thick topic](../results/entirely_thick.md) is
navigation, not an ID-bearing promoted theorem. This metadata authority
gap is recorded explicitly; no stronger universal claim is inferred.
The STCI factor reduction and low-degree exclusion have promoted support
in R-0001 and its linked audit.

The genuinely new bridge is A1, proved in the source and independently
reviewed, rather than an inference from a prior summary. It closes
later special-point normal-layer degeneration within its exact
saturated-first/generic-CI class. A2 then excludes all moving
nonreduced full roots within that actual class. A3 supplies additional
support-sensitive restrictions without requiring that first relation
to be a saturated line. No canonical result, question, state, or
frontier record was edited or promoted.

An independent local Hilbert-function argument is preserved in
[the local normal-flatness proposal](2026-10-19-filtered-generic-ci-normal-flatness.md).
It has its own classical dependency and a separate
[independent audit](2026-10-19-filtered-local-normal-flatness-independent-audit.md).
It is also a reviewed but unpromoted proposal. The projective theorem
has the self-contained resultant/duality proof and does not depend on
this additional classical bound or on the local route's broader scope.

## C. Most promising connection

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

## D. Remaining obstacles

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

## E. Recommended continuation and evidence checks

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

All principal results have full proof text and separate review evidence;
there is no uncompleted elimination computation underlying the reported
claims. Closing verification checked all 13 new notes and 70 local
Markdown links, with all targets present.
`python3 research/computations/validate_records.py` checked 10 canonical
records with zero errors. `git diff --cached --check` passed after a
whitespace-only correction to one audit. These are repository integrity
checks; mathematical validity rests on the proofs and independent
reconstructions, including a separate adversarial review of A1.

The package is committed on
[the research branch](https://github.com/markluxton1/STCI/tree/codex/normal-cone-rigidity-2026-10-19).
The exact closing commit is identified in the investigation message.
Standard external inputs, with direct primary links, are identified in
the respective source and audit notes.
