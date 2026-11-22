# 5. What the exclusion results actually rule out

The characteristic-zero fixed-curve problem remains open for higher-degree
surfaces. Its closed low-degree boundary is the accepted
[all-integral-quartic theorem R-0001](../../results/quartic_carrier_exclusion.md).
The [complete carrier proof](../../arguments/carriers/quartic_carrier_proof.md) gives the actual
argument; this chapter states its consequences and relates the different
obstruction mechanisms. In every characteristic \(p>0\), the same fixed
curve **is** an STCI using a quartic carrier; see the
[explicit construction](../../arguments/arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier).

The cases below are organized by **carrier degree**, not just
by the two numerically smallest possible pairs \((5,8)\) and \((6,6)\).
For each degree, distinguish:

- an **all-mate carrier-class exclusion** (every \(b>0\));
- a **pair-specific exclusion** (one specified \(b\));
- a **necessary reduction** that leaves a genuine realization problem.

That distinction is mathematically essential: a proof about
one sextic and all of its mates can be far stronger in its
quantifiers than a proof about every \((6,6)\) pair, even
though neither subsumes the other.

## 5.0b The classical primitive/STCI theorem already predicts the defect frontier

Begin with [Ellia, Theorems 12, 15 and Corollary 16](../../literature/README.md#ellia). His primitive CI classification leaves precisely ten eligible unordered degree pairs for a smooth rational quartic:
\[
 (4,7),(6,26),(12,18),(10,28),(9,48),
 (22,50),(20,67),(19,84),(18,118),(17,220).
\]
The complete quartic exclusion removes \((4,7)\) for the fixed embedding. Outside the remaining nine pairs, any sole-supported CI has a common singular point of its original generators. These are eligible primitive pairs, not examples, and the unrestricted common-singular-point statement is not established.

The correct all-degree division is by the **actual generic transverse embedding dimension**. The [normal replacement theorem](../../arguments/carriers/normal_carrier_divisor_geometry.md#47-unequal-degree-pairs-can-acquire-an-actual-normal-carrier) (pending independent audit) treats all \(a\le b\), including pencils: a general degree-\(b\) generator of the same ideal is normal integral exactly when some generator has generic order one. For generic multiplicity \(m>1\) this means the CI is generically curvilinear. The primitive subclass has no defect anywhere; the quasiprimitive subclass has a finite common-singular divisor. With both orders at least two, no normal member is obtainable in this generator system, and the full normal-cone/actual-source geometry is essential.

Thus all \((5,b)\) and \((6,6)\) candidates are in the finite-defect branch, and \((6,8)\) is the first numerical pair admitting the entirely-thick order pattern under the existing graph bounds. Ellia's uniform marked ADE theorem is stronger in the everywhere-primitive subclass, while the replacement theorem allows arbitrary finite nonprimitive behavior.

## 5.0a All-degree normal-carrier theorems come **before** the carrier-degree table

The strongest current exclusion statements are not organized
by degree four, five or six at all. The
[accepted all-degree local-index and socle theorem](../../arguments/carriers/normal_carrier_symbolic_torsion.md#4-cartier-index-integrality-and-new-all-degree-exclusions)
proves the following for **every** integral normal
hypersurface containing \(C_0\) in characteristic zero,
independently of the proposed mate degree:

1. **Indices dividing carrier degree.** If every actual
   on-\(C_0\) local Cartier index \(r_P\) divides
   \(a=\deg X\), no mate exists. This uses the
   exact minimal-mate theorem, not ADE classification.
2. **Nodal on-curve singularities.** If every
   singularity of \(X\) on \(C_0\) is an ordinary
   double point (or there are no such singularities),
   no mate exists, **in every degree**. Singularities
   away from \(C_0\) are unrestricted.
3. **All actual on-curve indices at most four.**
   The sharper [pointwise socle/Frobenius theorem](../../arguments/carriers/normal_carrier_symbolic_torsion.md#5-closing-the-entire-actual-index-at-most-four-class)
   excludes this whole normal-carrier class for
   **all degrees and all mates**, even when the
   index lcm \(R\) is as large as twelve.
   Consequently a hypothetical normal mate-bearing
   carrier must have **at least one actual
   local index \(\ge5\)**.
   Any configuration whose on-\(C_0\)
   singularities are only \(D_n,E_6,E_7,E_8\),
   or \(A_1,A_2,A_3\), is already excluded:
   the relevant local class-group exponents
   divide four. Off-curve singularities
   impose no hypotheses here.
4. **Quantitative growth.** If every actual
   on-curve index is bounded by a common
   integer \(s\ge3\), the stronger proven
   degree inequality is
   \[
     4a^2-(7s+6)a+16s\le0. \tag{U1}
   \]
   This means
   \[
     s\ge\frac{4a^2-6a}{7a-16},
   \]
   so the maximum actual on-curve index of
   any mate-bearing **normal** degree-\(a\)
   carrier grows at least like \(4a/7\).
   The inequality requires the fixed
   quartic's characteristic-zero normal
   splitting and the accepted
   symbolic-triple/pole input. It says
   nothing directly about nonnormal
   or generic-order-two carriers.

The [index-divides-\(12\) reduction](../../arguments/carriers/normal_carrier_symbolic_torsion.md#a-bounded-index-carrier-class)
is an intermediate consequence: it reduces
the entire normal-carrier class of that exponent
to a minimal unordered degree pair \((6,8)\);
the stronger pointwise theorem then excludes
the actual-index-at-most-four class. Do **not**
mistake the reduction to \((6,8)\) for a
possible construction.

**Why this changes the low-degree reviews.**
A normal quintic or sextic with only nodes,
\(D/E\) singularities, or indices at most
four is already excluded regardless of
the *mate's* degree: the \((5,8)\)
and \((6,6)\) ADE casework should never
redo those conclusions. It should start
only when higher-index \(A\)-type
geometry, simultaneous singularities or
actual global integral constraints survive.
This is a genuine **subsumption** of broad
classes by the general theorem, not
merely an analogy among specialized proofs.

## 5.0 Coverage by carrier degree: complete, all-mate classes, and gaps

**Degree four is completely closed.** R-0001 excludes *every*
integral quartic \(X\supset C_0\) paired with any form
of any positive degree, regardless of its normality,
conductor or singularities. Factor reduction then excludes
**every** proper sole-support pair having a degree-\(\le4\)
irreducible factor.

**Degree five has extensive all-mate exclusions, but is not
completely closed.** Every quintic is generically regular
along \(C_0\) by restriction to the unique quadric.
The existing coverage is:

| Quintic carrier class or locus | Proven scope | What closes it / what remains |
| --- | --- | --- |
| Integral **nonnormal** quintic with **Gorenstein normalization** | **All mate degrees** | [Full normalization, conductor, reflection and power-descent theorem](../../arguments/carriers/quintic_gorenstein_normalizations.md); the A4 projection/endpoint and conductor cases are constituent geometry, not independent gaps after this theorem |
| Integral quintic with a **toric normalization** | **All mate degrees** | [Complete marked polarized toric-source and projection-center inverse-support exclusion](../../arguments/carriers/quintic_toric_center_incidence.md) |
| Specified nonendpoint A4 projection \(h=3\) lane; endpoint families; some \(h=2\) subfamilies | **All mate degrees in each stated lane** | [Homogeneous \(h=3\) theorem](../../arguments/carriers/quintic_h3_support_exclusion.md), [endpoint inverse support](../../arguments/carriers/quintic_endpoint_residual_support_and_excess.md), and [nonendpoint fiber models](../../arguments/carriers/quintic_nonendpoint_support.md); much is already subsumed by the Gorenstein-normalization theorem, and must **not** be counted as disjoint additional coverage |
| **Normal quintic with globally ADE singularities** and an **octic mate** | **Only \((5,8)\)** | [Quasi-étale double-cover, canonical-map and symbolic-triple exclusion](../../arguments/carriers/quintic_octic_ade_cover_and_triple.md); includes repeated first-symbol zeros; higher mate degrees are **not** excluded by this theorem |
| **Normal quintic with restricted actual local indices** | **All mate degrees under the index hypotheses** | [Normal Hodge-gap and bounded-index theorems](../../arguments/carriers/normal_carrier_divisor_geometry.md); exclude low-index configurations independently of an ADE classification |
| Other normal quintics, and nonnormal quintics with **non-Gorenstein, non-toric normalization** | **Open in this coverage** | The [unresolved projection, \(h=2\), and normalization loci](quintic_carriers_and_a4_contact.md) retain their exact hypotheses; no complete degree-five carrier exclusion has been established |

**Degree six has several large all-mate exclusions plus a
strong all-\((6,6)\)-pair reduction, but is not completely
closed.** Distinguish a generic-normal-order-one sextic
from a *thick* order-two sextic, and distinguish splitting
in the **fixed quadratic cover** from splitting of the
**first normal cone**:

| Sextic carrier class or locus | Proven scope | What closes it / what remains |
| --- | --- | --- |
| **Two-lift** norm sextic \(F=P^2-rQ^2\) with \(P|_C=Q|_C=0\) | **All mate degrees**, including nonnormal signed cubics | [Complete two-lift theorem](../../arguments/linkage/two_lift_sextic_exclusion.md), including all residual ruling patterns |
| **One-lift** norm sextic, signed cubic smooth or Du Val **along its lift** | **All mate degrees in that sector** | [Conormal/differential and Du Val correction theorem](../../arguments/linkage/one_lift_sextic_conormal_exclusion.md); singular signed cubic excluded separately by [normalization geometry](../../arguments/linkage/signed_cubic_normalization_and_cartier_defect.md); non-Du Val, generically regular signed cubics remain |
| Integral **thick** sextic with singleton inverse a Cartier curve on its normalization | **All mate degrees under the stated normalization hypotheses** | [Projection/self-intersection integrality obstruction](../../arguments/carriers/split_sextic_conductor_and_contact.md#a-normalization-obstruction-for-an-integral-thick-sextic); splitting into two branches or a non-Cartier inverse remains distinct |
| **Split first-normal-cone** sextic with clean normalization/conductor and reduced-content-free hypotheses | **All mate degrees under these hypotheses** | [Branch intersection and polarization contradiction](../../arguments/carriers/split_sextic_conductor_and_contact.md#clean-split-conductor-a-branch-exclusion-and-its-stronger-global-model); squarefree residual and several ramified subloci excluded; the remaining non-squarefree/singular-gluing regimes are not covered |
| **Fixed explicit sextic** \(F_*\) | **All mate degrees** | [Sharp three-boundary valuation theorem](../../results/ci_fixed_sextic_jet_rigidity.md) forces positive residual support for every proper mate; nearby tested sextics have [additional all-degree-sixteen certificates](../../arguments/spectral/actual_sextic_mate_certificates.md), not a whole-family theorem |
| **Every hypothetical \((6,6)\) pair** | **All pairs with these two degrees** | [Quadric/graph bound, integral normal general-pencil carrier, saturated length-nine profiles, exact index-nine class and cyclic triple cover](../../arguments/carriers/sextic_pair_reduction.md); this is a **reduction**, not a final exclusion |
| \((6,6)\) with an **ADE general pencil member** | **Only the stated \((6,6)\) ADE sector** | [Root-rank and primitive-triple reduction](../../arguments/carriers/sextic_ade_reduction.md) narrows to \(L=\mathcal O(-6),D_2=0\); further higher-contact compatibility remains open |
| Other sextic carriers with mates of arbitrary degree | **Open in this coverage** | [Surviving one-lift, ramified split-cone and endpoint loci](open_carrier_cases.md) are not subsumed by \((6,6)\) normal-pencil arguments |

**Two different quantifiers are not a partition.** One
carrier may satisfy several rows. A hypothetical
\((6,6)\) pair can be studied through a normal *linear
combination* of the two sextics, whereas a fixed sextic
with a mate of degree \(b\ne6\) cannot generally be moved
in that same pencil. Likewise, an arbitrary-degree normal
quintic criterion is not an ADE \((5,8)\) theorem.
The coverage should be read as *nested implications*,
not an additive count of eliminated cases.


## 5.1 The precise degree-four theorem and its proof mechanisms

Fix an algebraically closed characteristic-zero field and
\(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\). For **every integral
quartic surface** \(X\supset C_0\) and **every homogeneous form** \(G\)
of positive degree, \(V(X,G)_{\mathrm{red}}\ne C_0\). No normality,
singularity, reduced-conductor, mate-degree, or first-normal-order
hypothesis is imposed. The theorem concerns this embedding and its
projective equivalents.

The [proof](../../arguments/carriers/quartic_carrier_proof.md) derives generic regularity and full
inverse support, and uses the common correction identity
\(q+K_MZ=2\pi\). Normal carriers are excluded through exceptional
correction, global denominator compression, exact cycle/tree supersets,
and the actual TypeD ideal. Nonnormal carriers have rational normalization
and normalized sectional genus zero, one or two. Their respective endings
are conductor descent on minimal-degree models; a fixed-center del Pezzo
ribbon projection; and the bisection global nilideal obstruction or the
trisecant actual attachment budget. The endpoint includes repeated
components and all projective charts.

This assembly uses every component proof at its stated hypotheses.
The independent [quartic-pair proof](../../arguments/normal-geometry/quartic_pair_obstruction.md) excludes
only \((4,4)\); the normal bounded-index result
[R-0035](../../results/normal_carrier_bounded_index_exclusion.md) has its own
index and inherited-premise restrictions. Neither is the arbitrary-mate
quartic theorem.

## 5.2 Factors and the degree bound

If \(V(F,G)_{\mathrm{red}}=C_0\), the forms are coprime: a common
irreducible factor would contribute a surface. For any irreducible factor
\(f\mid F\), \(V(f,G)\) is a nonempty pure one-dimensional projective
complete intersection. Its support lies in the irreducible \(C_0\), hence
is all of \(C_0\). The same holds for each factor of \(G\), and for
any pair of irreducible factors, one from each form. Factor multiplicities
change scheme multiplicity, not this support argument.

No plane contains the nonplanar curve. Its unique quadric is smooth, with
curve class \((1,3)\); a degree-\(b\) ambient form restricts to \((b,b)\),
which cannot have sole divisor support a positive multiple of \((1,3)\).
[Craighero--Gattazzo's cubic theorem](https://www.numdam.org/item/RSMUP_1989__81__171_0.pdf),
pp.171–173 and its subsequent proof, covers every reduced irreducible cubic
and arbitrary mate degree over algebraically closed characteristic-zero
fields. R-0001 excludes the integral quartic factors. Therefore **every
irreducible factor of either defining equation has degree at least five**,
and in particular \(\deg F,\deg G\ge5\), even for reducible or repeated
equations. This gives no existence assertion in degree five.

## 5.3 Divisibility for sole-support pairs

For a proper pair of degrees \(d,e\) with sole reduced curve support
\(C_0\), its generic intersection length is \(m=de/4\). Hence
\[
\frac4{\gcd(4,d)}\mid e.
\]
For an integral quintic carrier the mate degree must be divisible by four,
so the first numerically possible degree after the exclusion is eight.
For \(d\equiv2\pmod4\), the mate degree is even; for \(4\mid d\), this
cycle calculation alone imposes no divisibility. These are necessary
conditions for sole-support proper pairs. With a residual cycle \(R\),
the equation is instead \(de=4m+\deg R\).

## 5.4 Closed mate cases and still-useful local mechanisms

The theorem closes all quartic-*mate* subcases, including normal carriers,
primitive e2, MF6, and early-defect branches. Their intermediate proofs
remain useful: exact quartic factorization, normal-index restrictions,
global/local contact discrepancies, conductor powers and principal
candidate loci measure different failure mechanisms. A stronger theorem
does not erase a distinct proof or a counterexample to a proposed bridge.

In particular the common-quartic local-cohomology **ancestor incidence**
is a containment/annihilation question and is not proved empty by a
no-mate theorem. The same distinction applies to the principal at-most-
630-point necessary locus. A quartic ancestor of an integral sextic does
not mean that sextic has an actual quartic mate. Higher-degree entirely
thick pairs remain outside the quartic theorem.

## 5.5 Why the other results do not add a universal degree exclusion

- [R-0025](../../results/ci_fixed_sextic_jet_rigidity.md) forces residual support
  for one prescribed sextic and its stated equation-space comparison; it
  does not quantify over all sextics.
- [R-0030](../../results/local_filtration_comparison_defect.md) and the conormal/
  socle theorems retain their actual-source, saturation, and defect
  hypotheses. Neither a full initial ideal nor a zero module-comparison
  defect alone gives an STCI exclusion.
- The marked flag/dual/ruled models and the fixed-lower determinant test
  describe their actual geometric objects or conditional existence tests;
  they do not establish that every hypothetical pair belongs to them.
- Positive-characteristic sole-support constructions and prescribed
  arithmetic nonlifting concern different characteristics or specified
  embedded schemes. They do not contradict a characteristic-zero theorem.

The [carrier proof's characteristic comparison](../../arguments/carriers/quartic_carrier_proof.md#8-what-changes-in-positive-characteristic)
identifies the precise boundaries: differential mate-degree cancellation,
nilpotent Frobenius descent, the characteristic-two conormal jump,
inseparable trisecants in characteristic three, and the characteristic-zero
global surface bound. The distinction is mathematical, not a blanket
warning about reduction modulo primes.

## 5.6 Reusable exclusion proof: the actual dependency order

The low-degree exclusions can be read as **one proof by compatible
carrier geometry**, not three unrelated lists of singularity types.
This is a proof *organization* using already proved results, not a
new unrestricted exclusion theorem. In particular, the all-degree
normal-index bounds **depend on the complete degree-four exclusion**.
They cannot be used to prove that very exclusion.

**Step 0 — indispensable low-degree input.** The
[quartic-carrier theorem](../../arguments/carriers/quartic_carrier_proof.md)
is the base case: normal quartics require their specific
exceptional/actual-ideal proof, and nonnormal quartics require
their sectional-genus, full-conductor and attachment arguments.
Its conclusion, along with the classical plane/quadric/cubic
exclusions, makes **every integral defining factor have degree at
least five**. This base case must not be replaced by a theorem
whose proof invokes it.

**Step 1 — determine generic transverse embedding dimension.** For every hypothetical pair of degrees \(a\le b\), a [general actual degree-\(b\) replacement](../../arguments/carriers/normal_carrier_divisor_geometry.md#47-unequal-degree-pairs-can-acquire-an-actual-normal-carrier) is normal integral if and only if some generator has generic order one, preserving the entire CI ideal. This holds with no degree cutoff and requires neither factor integrality nor a non-pencil system. The quadric normal-order bound makes it automatic for \((5,b)\); the graph bound makes it automatic for \((6,6)\). Both order-two in \((6,8)\) remains outside the reduction. It does not make the original smaller carrier normal or eliminate its conductor geometry. In equal degrees both generators may be chosen normal. The unified proof requires independent audit; the original \((6,6)\) proof retains its reviewed status.

**Step 2 — use the complete normal-carrier test
for every mate degree.** If the chosen degree-\(a\)
carrier \(X\) is normal, the already proved
[Hodge equality theorem](../../arguments/carriers/normal_carrier_divisor_geometry.md#1-a-mate-is-equivalent-to-hodge-index-equality-on-a-normal-hypersurface)
says a mate exists *if and only if* \(C\) is
\(\mathbf Q\)-Cartier and \(\Gamma_X(C)=0\).
The [intrinsic index/defect formula](../../arguments/carriers/normal_carrier_divisor_geometry.md#2-the-intrinsic-local-divisor-is-a-necessary-and-sufficient-mate-test)
evaluates this gap from actual local symbols, indices
and multiplication, and the exact index theorem determines
the **minimal mate degree on that fixed carrier**.
For *any* normal quintic carrier with a mate,
\(R=5t\), \(b_{\min}=4t\), \(t\ge2\).
For *any* normal sextic carrier with a mate,
\(R=3t\), \(b_{\min}=2t\), \(t\ge3\).
These are **all-mate necessary conditions**;
the familiar \(R=10\) in \((5,8)\) and \(R=9\)
in \((6,6)\) are just minimal-degree specializations.
The normal Hodge equality remains necessary-and-sufficient
for existence on a *fixed* normal carrier; no extra
ambient-lifting condition survives once it holds.

**Step 3 — use whole-carrier all-mate exclusions
before degree-pair casework.** Normality is only
one possible branch. A nonnormal quintic with Gorenstein
normalization, a quintic with toric normalization,
a two-lift fixed-cover sextic, and the eligible
one-lift/split-cone/fixed-sextic classes are each
excluded for **every mate degree** by their own
actual inverse-support, conductor, intersection or
boundary-valuation mechanism (table in §5.0).
These results can retire a whole parameter family,
not merely a \((5,8)\) or \((6,6)\) case.

**Step 4 — among survivors, test realization of
the required Hodge/index geometry.**
On normal carriers the ADE/marked-curve computations
are **not independent mate criteria**. They ask
whether an actual degree-\(a\) hypersurface can
realize the required local indices and equality:
the [quintic ADE cover/primitive-triple proof](../../arguments/carriers/quintic_octic_ade_cover_and_triple.md)
excludes its \((5,8)\) sector, while the
[sextic ADE rank/primitive-triple reduction](../../arguments/carriers/sextic_ade_reduction.md)
closes several \((6,6)\) rows but leaves
\(\mathcal O(-6)\). The many special calculations
now have an identifiable responsibility: rule out
**realization of compatible global data**, rather
than recompute basic mate existence.

**Step 5 — handle remaining nonnormal or generically singular carriers
by their own gates.** For a nonnormal carrier generically
regular along \(C\), the normalization must have full inverse
support and a positive Cartier multiple of its lift; the
[conductor/differential theorem](../../arguments/carriers/carrier_conductor_differential_comparison.md)
rules out smooth normalization **together with smooth conductor
contact** for \(a\ge5\). Singular normalization, singular
conductor gluing and actual power descent require the
specialized proofs; for example the
[quintic Gorenstein-normalization theorem](../../arguments/carriers/quintic_gorenstein_normalizations.md).
For a carrier *generically singular along \(C\)*,
the normal-ray test does not apply directly; retain the
blowup/normal-order, saturated CI filtration and actual
homogeneous-lift arguments.

**What remains after combining these results.** No general
normal-carrier theorem proves \(\Gamma_X(C)>0\) for every
\(a\ge5\), and no unconditional conductor-descent exclusion
covers arbitrary nonnormal carriers. The normal Hodge-gap
criterion is a complete fixed-carrier test, not a classification
of all carriers; the genus/exceptional/root casework remains
necessary wherever it excludes a candidate with otherwise
compatible budgets. The diagram is a *dependency ordering*,
not a claim that the current degree-five or degree-six problem
is solved.

### Open question: higher-degree surface singularity budgets

Can one bound **actual realizability of the equality configuration**
uniformly in carrier degree: simultaneously the normal Hodge-gap
equality, local Cartier indices, first-normal defect divisors and
global cyclic-cover geometry—or, in the nonnormal branch,
the full conductor and actual descent? The classical
root-rank budget grows cubically in degree while the
required correction grows only linearly. This prevents
simple extrapolation of quartic surface-rank counting.
The [quintic even-node case](../../arguments/carriers/quintic_octic_surface_constraints.md#42-the-actual-divisor-relation-forces-an-even-set)
shows why integral Picard compatibility can remain decisive
after numerical equality has been reached.

## 5.7 The common adjunction gap: synthesis across degrees four, five, and six

**Status and scope.** This section compares proved mechanisms, rather than
asserting a new all-degree exclusion. It uses the fixed characteristic-zero
smooth rational quartic \(C=C_0\) of degree four. The
[normal-carrier extremal-ray criterion](../../arguments/carriers/normal_carrier_divisor_geometry.md#1-a-mate-is-equivalent-to-hodge-index-equality-on-a-normal-hypersurface)
is already necessary **and sufficient on a fixed normal \(\mathbf Q\)-Cartier carrier**;
the [conductor/differential criterion](../../arguments/carriers/carrier_conductor_differential_comparison.md)
has distinct nonnormal, generic-regularity and smoothness hypotheses.
The [quartic-carrier theorem](../../results/quartic_carrier_exclusion.md)
excludes *all* integral degree-four carriers with mates, whereas the
degree-five and degree-six exclusions below are **conditional sectors**,
not full carrier-degree exclusions.

### The normal-carrier Hodge gap is an existence test, not just a bound

Let \(X\subset\mathbf P^3\) be an integral **normal** degree-\(a\)
hypersurface containing \(C\), and assume \(C\) is \(\mathbf Q\)-Cartier.
Write \(H=\mathcal O_X(1)\). Hodge index gives
\[
 \Gamma_X(C):=\frac{16}{a}-C^2\ \ge0.
\]
The established [normal-carrier theorem](../../arguments/carriers/normal_carrier_divisor_geometry.md)
proves, in characteristic zero,
\[
 \boxed{\quad
 \Gamma_X(C)=0
 \quad\Longleftrightarrow\quad
 \text{\(C\) admits an actual homogeneous sole-support mate on \(X\)}.
 \quad} \tag{S1}
\]
If \(C\) is not \(\mathbf Q\)-Cartier, the equivalence cannot be
invoked and there is no mate on this normal \(X\).
Equality makes a multiple of \(C\) linearly equivalent to a multiple
of \(H\); the associated section lifts to \(\mathbf P^3\) by the
hypersurface restriction sequence. Thus **on normal carriers**, a
separate conjectural global equation-lifting obstruction must not
be added after (S1). Identifying the vanishing locus of the gap as
\(X\) varies is still the difficult problem.

For the saturated first normal quotient \(B=\mathcal O_C(-\ell)\),
the actual local Cartier indices \(r_P\), first-symbol vanishing
orders \(A_P\) and top ordinary multiplication defects \(D_{r_P,P}\),
the accepted intrinsic comparison makes the same test local:
\[
 \boxed{\quad
 \Gamma_X(C)=
  \sum_{P\in C}\frac{A_P+D_{r_P,P}}{r_P}
       -\left(\ell-\frac{16}{a}\right).\quad} \tag{S2}
\]
The divisors on the right arise from the **actual carrier geometry**;
an arbitrary collection of formal local numbers is not automatically
realizable. This is the common target against which low-degree
ADE/index/normal-symbol cases should be compared.

### On a Du Val carrier, exceptional correction measures this exact gap

Assume further that \(X\) has only Du Val singularities. On its
crepant minimal resolution \(\pi:\widetilde X\to X\), write
\(\pi^*C=\widetilde C+Z\), where \(Z\) is the rational exceptional
correction. The strict transform is a smooth rational curve,
\(K_{\widetilde X}=(a-4)\pi^*H\), and adjunction gives
\[
 \widetilde C^2=-2-4(a-4)=14-4a,\qquad
 C^2=\widetilde C^2-Z^2.
\]
Consequently
\[
 \boxed{\quad
 \Gamma_X(C)=
  \left(4a-14+\frac{16}{a}\right)-(-Z^2).
 \quad} \tag{S3}
\]
In particular Hodge index makes \(-Z^2\) **at most**
\(4a-14+16/a\), and a mate requires **equality**, not merely
some nonzero exceptional correction. This is a precise interpretation
of the "required correction" terminology.

| Carrier degree \(a\) | Required value of \(-Z^2\) **if a mate exists** |
| --- | ---: |
| \(4\) | \(6\) |
| \(5\) | \(46/5\) |
| \(6\) | \(38/3\) |

The last entry is exactly the
[existing sextic correction](../../arguments/torus/fixed_surface_restriction_lifts.md#ade-local-classes-and-the-global-sextic-correction-budget).
The fractions impose prime-local-index requirements in the ADE
lattice (a denominator \(5\) needs 5-primary local classes,
a denominator \(3\) needs 3-primary classes), but denominators and
exceptional rank alone are **not** sufficiency criteria.

### A formal numerical coincidence with nonnormal conductor contact

In the *different* regime where an integral carrier \(S\) is
generically regular along \(C\), its normalization \(\nu:X\to S\)
is **smooth along the unique lifted curve** \(c\cong C\), and an
actual mate exists, the existing
[conductor/differential comparison](../../arguments/carriers/carrier_conductor_differential_comparison.md#divisor-and-conductor-degrees)
computes
\[
 c^2=\frac{16}{a},\qquad
 D\cdot c=4a-14+\frac{16}{a}, \tag{S4}
\]
where \(D\) is the **full normalization conductor divisor**.
This is the same numerical adjunction discrepancy as (S3), but
\(D\cdot c\) and \(-Z^2\) are **not the same invariant**;
one concerns nonnormal descent and the other resolution of a
normal Du Val surface.

Moreover, *smoothness along \(c\)* makes \(c\) Cartier and \(c^2\)
integral, hence \(a\mid16\). Thus **degree-five and degree-six
nonnormal carriers cannot satisfy this smooth-normalization
hypothesis under a mate at all**. Their entries in the table
are not predictions of realizable conductor configurations.
For the remaining divisible degrees, the smooth-conductor local
inequality \(D\cdot c\le2\deg H_{\mathrm{diff}}\) and the balanced
normal splitting yield
\[
 (a-3)(a-4)\le0,
\]
excluding all \(a\ge5\) when the full conductor also has only
smooth contact on \(C\). Singular normalization or singular
conductor gluing is a **real mathematical escape regime**,
not an error term one may silently bound by this inequality.

### Multi-branch normalization: one intersection-matrix mechanism

The normal Hodge gap is the **one-branch, normal**
part of the story. Several broad sextic exclusions
instead live on a *normalization or signed surface*
with **two distinct curves** lying above \(C\).
Their common geometry can be stated without committing
to a special sextic equation.

Suppose a finite normalized carrier has reduced
inverse support \(\Gamma_1\cup\cdots\cup\Gamma_s\),
and **each lifted curve is Cartier** on a smooth
neighborhood of that union. The pullback of a
sole-support mate of degree \(b\) must give an
**actual effective Cartier divisor**
\[
 \operatorname{div}(\nu^*G)
   =\sum_i m_i\Gamma_i,\quad m_i>0,
 \qquad \sum_i m_i\Gamma_i\sim bH .
 \tag{MB1}
\]
Intersecting with all \(\Gamma_j\) gives
\[
 \boxed{\quad
 M\mathbf m=b\,\mathbf h,\qquad
 M_{ij}=\Gamma_i\cdot\Gamma_j,\quad
 h_j=H\cdot\Gamma_j.\quad}                     \tag{MB2}
\]
Together with \(H\sum_i m_i\Gamma_i=bH^2\),
this is a **positive-integral lattice problem**
for actual branch multiplicities, valid for
**every mate degree**. In the singular
\(\mathbf Q\)-Cartier regime, replace (MB2)
by its numerical pullback on a resolution
and retain exceptional correction; it is
not legitimate to assume the individual
curves Cartier.

This unifies the *mechanism* behind the
[two-lift norm sextic intersection proof](../../arguments/linkage/two_lift_sextic_exclusion.md#two-lift-split-carriers-intersection-on-the-signed-surface)
and the [clean split-conductor
first-normal-cone sextic exclusion](../../arguments/carriers/split_sextic_conductor_and_contact.md#clean-split-conductor-a-branch-exclusion-and-its-stronger-global-model).
In the former the polarized intersections on
a signed cubic conflict with all positive
multiplicities (or require impossible
Du Val/non-Du-Val corrections), with every
residual ruling pattern eventually excluded.
In the latter the full conductor, adjunction
and clean normal ideal force a matrix whose
positive-solution condition includes
\(d^2-10d-35=0\), impossible for its integral
normal-direction parameter. These are *two
applications of (MB1)--(MB2)*, **not**
interchangeable covers: the fixed quadratic
cover and a split first normal cone are
different geometric constructions.

When the inverse is instead a **single Cartier**
curve \(\Gamma\) of mapping degree \(\delta\)
over \(C\), (MB2) yields the scalar
\(\Gamma^2=16\delta^2/a\) and its
integrality test. For a thick sextic
\(\delta=1,2\) gives \(8/3\) or \(32/3\),
excluding that singleton Cartier branch
for *all mate degrees*. The remaining
nonnormal case requires multiple branches
or a non-Cartier inverse; neither has been
settled just by (MB2).

**Connection to quintic normalization.** The
degree-five Gorenstein-normalization proof
largely has a single lifted \(c\) and a
divisor root, but its obstruction lies at the
*next step*: actual full inverse support
and **power descent through the entire
conductor**, not merely an intersection
matrix. This distinction locates exactly
where the common normalization framework
forks into separate terminal lemmas.
Thus the uniform proof route is
\[
 \text{actual inverse support}
 \ \to\ \text{polarized divisor lattice}
 \ \to\ \text{local exceptional/contact corrections}
 \ \to\ \text{actual conductor descent}.
\]
Each arrow is a **necessary check**;
it is not a claim that every possible
normalization has been classified.

### Normal carrier replacement **across unequal defining degrees**

The [general replacement theorem](../../arguments/carriers/normal_carrier_divisor_geometry.md#47-unequal-degree-pairs-can-acquire-an-actual-normal-carrier) now includes equal degrees and gives \(K_b=G_b+F_aL_{b-a}\), normal integral with the same CI ideal, precisely for the generic order-one branch. Only base-support Bertini, \(R_1+S_2\) and connectedness are needed. The stronger **moving-root theorem** additionally distinguishes the fixed common-symbol divisor from the moving reduced divisor of the general carrier. In every degree, a nonempty moving divisor forces \(R=m=ab/4\) and minimal mate degree \(a\). For \(a<b\) this is automatic if the smaller first symbol is nonzero. For \(a=b\) it holds when the first symbols are linearly independent over \(k\); a proportional-symbol pencil instead has a unique generically thick member, and its general members are still normal. For \(a<b\) with zero smaller symbol there are no moving symbol zeros.

For \((5,4n)\) every normal larger carrier with a quintic mate has \(R=5n\) by the strengthened Picard saturation theorem, and order-five primitive class \(nC-H\); e.g. \(R=10,15,20,25\) for \(b=8,12,16,20\). This includes originally nonnormal quintics for all mate degrees, but does not classify them or obstruct the resulting high-index configuration. The [intrinsic common-defect identity](../../arguments/carriers/normal_carrier_divisor_geometry.md#the-exact-defect-budget-is-concentrated-at-common-singularities) applies to every generically curvilinear pair regardless of degree or moving-root existence: the actual top-socle divisor and common-symbol divisor have the same support, not generally the same multiplicities. Every primitive-locus singularity of a normal carrier necessarily has index \(m\), even at a multiple symbol root of a special member. These implications and the generalizations are pending independent audit.

### Going back down: when a forced high index is **not** a new obstruction

The general normal replacement is
a **real theorem-level reduction**,
but one must test whether its
resulting index restrictions
actually rule out anything.
The [local moving-singularity
calculation](../../arguments/carriers/normal_carrier_divisor_geometry.md#a-local-countermodel-high-index-can-be-a-moving-pencil-singularity)
supplies an important control:
on the affine threefold with
\(C=(u,v)\),
\[
 F=u,\quad G=tu+v^m,\quad
 K_\lambda=G-\lambda F
             =(t-\lambda)u+v^m,
\]
the same sole-supported CI
\((F,G)=(u,v^m)\) has a family
of **normal \(A_{m-1}\)
replacement carriers**,
each with a moving on-curve
Cartier index \(m\) point,
although \(F\) is smooth
along all of \(C\).

More generally, wherever the
smaller surface \(F=0\) is
smooth and \(G|_F=mC\),
write \(G=u h+v^m w\) with
\(w\) a unit. A *simple*
zero of the scalar first-normal
coefficient \(h+L\) on \(C\)
makes \(G+LF\) analytically
\(xy+z^m\) with the marked
curve of exact index \(m\).
Thus the required high-index
singularities of a **normal
larger generator** can arise
automatically at moving
normal-coefficient zeros.
The general proof and
precise hypotheses are in
the linked normal-carrier file.

In a hypothetical \((5,4n)\)
pair the generic transverse
length is \(m=5n\), and an
\(A_{5n-1}\) point has exactly
the index \(5n\) permitted
(and sometimes forced) by the
order-five class \(\Delta=nC-H\).
So the new index table is
**not yet an exclusion**.
In particular it must not be
used to infer a *common*
singular point of the original
pair on \(C\): the moving
\(A\)-model explicitly shows
why such an inference fails
even locally.

**What it changes at the
research level.** The task
is to constrain the **global
family of moving high-index
marked singularities** using
the actual homogeneous
first-symbol ratio and
higher coefficient maps,
rather than count their
possible local indices.
This is where the fixed
normal-carrier theorem,
conormal filtration,
global equation source maps
and singularity geometry
must meet. An ADE root-rank
capacity alone is too large
at high degree; an index
threshold alone is often
naturally satisfied. The
missing implication is not
new local singularity
classification but a **global
incompatibility among their
realization conditions**.

### From the normalization lattice to the **actual** mate monoid

The multi-branch criterion (MB1)--(MB2) becomes
independent of the unknown mate degree after
putting \(u_i=m_i/b\). On a smooth
normalization neighborhood of the lifted
branches, a necessary condition for
**any** sole-supported mate is
\[
 \boxed{\quad M\mathbf u=\mathbf h,\quad
 u_i>0,\quad u_i\in\mathbf Q,\quad
 \sum_i u_i(H\cdot\Gamma_i)=H^2=a.\quad}   \tag{MB3}
\]
This is a **rational positive-cone feasibility
test** performed once for all mate degrees.
If it has no solution, every mate degree
is excluded; if it has solutions, their
integral denominators impose candidate
mate congruences. For a nonsingular
intersection matrix \(M\), the unique
candidate is \(M^{-1}\mathbf h\).
For singular \(M\), one must retain
the full rational affine solution set.

**Do not reverse the implication.**
A positive rational solution does not
assert actual linear equivalence,
an effective global section, or
descent through the conductor. A singular
normalization requires its actual
Mumford pullbacks and local indices,
not an invented smooth intersection
matrix. The severe
[quintic Gorenstein-normalization
exclusion](../../arguments/carriers/quintic_gorenstein_normalizations.md)
shows how an upstairs root relation can
survive rational numerical tests while
actual inverse support or conductor
power descent fails.

The [fixed-carrier actual-mate monoid theorem](../../arguments/torus/fixed_surface_restriction_lifts.md#comparing-multiplicities-on-one-fixed-carrier)
completes the *opposite* direction.
**After** genuine homogeneous mate
sections exist on an integral \(S_2\)
carrier regular at the supported
generic points, the semigroup of
their multiplicity vectors is saturated
inside the **lattice generated by actual
mate vectors**. Thus there are
two different mathematical objects:
\[
 \begin{array}{c}
 \text{upstairs rational-positive
 divisorial feasibility (MB3)}
 \\[2pt]\Downarrow\ \text{not automatic}\\[2pt]
 \text{downstairs actual
 mate lattice/monoid}.
 \end{array}
\]
The gap is exactly actual globalization,
full inverse support and conductor gluing.
Once actual seed equations pass that
gap, negative integer powers of their
ratios introduce **no new**
codimension-two obstruction on an \(S_2\)
hypersurface: the supported actual
monoid is saturated in its own group.

**Back to quartic Chow realization.**
The same monoid argument, read
backwards, combines the
[complete quartic-carrier
all-mate exclusion](../../results/quartic_carrier_exclusion.md)
with the
[prime-cyclic translate theorem](../../arguments/torus/fixed_surface_restriction_lifts.md#reverse-application-single-curve-exclusions-constrain-multi-curve-chow-cycles)
to force **uniform multiplicities**
for any symmetric prime orbit of
projective quartic translates supported
on an integral quartic carrier.
It also makes the actual
two-translate multiplicity-vector locus
**rank at most one**, even without
an involution. This is a genuine
cross-framework implication from
single-support STCI exclusions to the
multi-support Chow cycle realization
problem; no extra candidate family is
asserted to exist. The monoid theorem
has a more general normal-carrier
version whenever a singleton translate
is excluded by the all-degree
actual-index-at-most-four theorem.

### The indices turn degree-five and degree-six cases into a single test

For a hypothetical sole-support mate of degree \(b\) on a normal
degree-\(a\) carrier, put \(g=\gcd(a,4)\),
\(\mu=a/g\), \(v=4/g\), and let \(R\) be the lcm of
the **actual local Cartier indices of \(C\)**. The existing
[local index and torsion theorem](../../arguments/carriers/normal_carrier_symbolic_torsion.md#3-exact-index-formula-on-every-normal-c0-carrier)
gives
\[
 m=ab/4,\qquad R\mid m,\qquad a\mid4R,\qquad
 t=\frac{R}{\mu},\qquad b_{\min}=4R/a,\qquad m_{\min}=R. \tag{S5}
\]
The all-quartic-carrier theorem implies \(b_{\min}\ge5\).
This immediately specializes to two strong **conditional**
constraints, without enumerating ADE singularities:

- For a **normal \((5,8)\)** candidate, \(m=10\), so \(R\mid10\)
  and \(5\mid R\); the small-mate exclusion rules out \(R=5\).
  Hence \(\boxed{R=10}\). A necessary 5-primary class alone
  cannot suffice: extra 2-primary index information is required.
- For a **normal \((6,6)\)** candidate, \(m=9\), so \(R\mid9\)
  and \(3\mid R\); the small-mate exclusion rules out \(R=3\).
  Hence \(\boxed{R=9}\). An ADE 3-torsion class of *order three*
  alone cannot suffice: some on-curve class must have exact order nine.

This distinguishes a **numerical correction budget** from an
**exact index/divisor realization condition**. In the ADE rows, the
quintic condition may be distributed across different singular points,
whereas the sextic condition requires an order-nine local class
(and therefore an appropriate \(A_n\) singularity). Neither produces
a hypothetical carrier. The stronger
[quintic--octic ADE exclusion](../../arguments/carriers/quintic_octic_surface_constraints.md)
and the
[conditional ADE sextic reduction](../../arguments/carriers/sextic_ade_reduction.md)
test additional global and filtered compatibility beyond (S5).

### Why degree six is the first new generic-normal-order regime

This change of complexity has a **single geometric cause**. The
unique smooth quadric \(Q\supset C\) has
\(C\sim(1,3)\in\operatorname{Pic}(Q)\). For any degree-\(a\)
hypersurface \(F\) through \(C\) **not divisible by the equation
of \(Q\)**, let \(r\) be its generic order along \(C\).
Restriction to \(Q\) has divisor class \((a,a)\) containing
\(rC\), hence has an effective residual of class
\((a-r,a-3r)\). Therefore
\[
 \boxed{\quad r\le\lfloor a/3\rfloor.\quad} \tag{S6}
\]
This is the established quadric-restriction argument used in the
[sextic all-pair reduction](../../arguments/carriers/sextic_pair_reduction.md#why-every-pair-is-generically-curvilinear);
it is not a new all-degree theorem. In a hypothetical sole-support
presentation the quadric cannot divide either equation, since the
other equation restricted to \(Q\) cannot have sole divisor
support on the unbalanced class \((1,3)\).

In particular **every integral degree-four or degree-five carrier
is generically regular along \(C\)**. Degree six is the *first*
possible carrier degree with generic normal order two. For an actual
sole-supported \((6,6)\) pair, however, the established
[blowup/graph residual bound](../../arguments/residuals/blowup_residual_geometry.md#5-integer-strengthening-usefulness-region-and-exact-limitations)
excludes simultaneous orders \((2,2)\): it forces at least four
residual degrees. Hence **at least one of the two sextics is
generically regular along \(C\)**, and the transverse algebra is
curvilinear of length nine. More strongly, the established
[general-pencil argument](../../arguments/carriers/sextic_pair_reduction.md#a-normal-pencil-carrier-in-characteristic-zero)
shows that a general sextic pencil member is **integral,
smooth away from \(C\), and generically regular on \(C\)**;
Serre's \(R_1+S_2\) criterion therefore makes it **normal**.
Replacing the original generators by two such general members
does not change their CI ideal. Thus any hypothetical
characteristic-zero \((6,6)\) sole-support pair has a
**normal sextic carrier**. Nonnormal sextic members may
occur in special positions, but their analysis is unnecessary
for deciding existence of a \((6,6)\) presentation.
For unequal degrees the same replacement normalizes the larger carrier, not necessarily the smaller one. Thus the nonnormal quintic lanes remain distinct fixed-carrier questions.

The graph argument is not uniform in degree: it gives no positive
residual bound at \((8,8)\) with normal orders \((2,2)\).
Thus the all-degree generic-singular-carrier regime cannot be
discarded merely by extrapolating the sextic reduction.

### The unrestricted \((6,6)\) theorem is stronger than mere nonprimitivity

The [all-pair sextic proof](../../arguments/carriers/sextic_pair_reduction.md#the-common-first-normal-divisor-must-be-nonreduced)
already proves something **strictly
stronger** than the Ellia
primitive exclusion or the
existence of a nonempty defect
divisor:

\[
 \boxed{\text{For every hypothetical
 characteristic-zero sole-supported
 \((6,6)\) pair, the common
 first-normal gcd divisor \(B_1\)
 is nonreduced.}}
\]
This holds with **no ADE or
normality hypothesis on the
original generators**.

Its proof is already a model
of the desired generalization
mechanism. If \(B_1\) were
reduced, choose a general
**normal** sextic pencil
member. Its moving simple
first-symbol roots have
marked \(A_8^1\)
singularities, while the fixed
simple roots are
\(A_2^1\), with distinct
multiplication defects.
The exact CI/socle budget
forces the following *entire*
singularity profile:

| Saturated \(\ell\) | Fixed \(A_2\) | Moving \(A_8\) | ADE root rank |
| ---: | ---: | ---: | ---: |
| 5 | 3 | 12 | 102 |
| 6 | 7 | 9 | 86 |
| 7 | 11 | 6 | 70 |

The sextic ADE root-rank
ceiling \(85\) eliminates
the first two rows; the
last has \(D_2=0\) in the
forbidden constant-direction
primitive triple, eliminating
it too. Therefore the
**remaining** sextic
problem must have a
**multiple common-symbol
zero**, not merely some
shared singular point.

This is an important
up-and-down synthesis:
the **classical**
primitive-degree theorem
says a defect is necessary;
the **actual-pair**
first-normal geometry
says it must be nonreduced;
the **global surface
rank and local triple**
arguments eliminate every
reduced-defect configuration.
The still-open nonreduced
case admits genuine
local finite-flat control
models; it cannot be
deleted by the primitive
theorem or normal
Hodge equality alone.

The **degree-independent part** of this proof is now extracted as the [uniform reduced-gcd test RG1](../../arguments/carriers/normal_carrier_divisor_geometry.md#reduced-common-first-normal-divisor-a-uniform-marked-ade-and-rank-test) (pending independent audit). For any generically curvilinear actual pair with reduced common-symbol divisor, all singularities of a general larger normal carrier are end-marked \(A_{r-1}\); the indices divide \(m\), equal \(m\) at moving roots and are proper divisors at fixed roots. The saturated layers at fixed roots have coefficients \(\lfloor i/r\rfloor\). Global duality and the full Hodge root-rank bound give a uniform test in all degrees. The sextic proof still needs its special rank/triple contradiction, but its architecture is general.

The arithmetic of this test already gives a new proposed all-degree stratum exclusion: when every prime factor of \(m=ab/4\) is \(1\bmod4\), the reduced-gcd hypothesis makes the top defect divisible by four, contrary to duality on the rational quartic. It therefore forces nonreduced common-symbol divisor in this multiplicity class, e.g. \((5,20)\) and the order-one \((10,10)\) sector. It neither excludes all possible quintic mate degrees with reduced gcd nor settles any whole pair.

### The first actual pair where both normal-carrier reductions can fail is \((6,8)\)

The two established geometries now fit together
more sharply:

- The **normal replacement** (NR1)
  applies to \(a\le b\) whenever at least
  one equation has generic normal order
  one; it always covers \((5,b)\)
  with \(b>5\).
- The established [graph/Bézout residual
  inequality](../../arguments/residuals/blowup_residual_geometry.md#5-integer-strengthening-usefulness-region-and-exact-limitations)
  rules out simultaneous generic
  normal orders \((2,2)\)
  for a sole-supported \((6,6)\)
  pair, forcing a normal general
  member there.

For \((6,b)\), with both generic
normal orders two, the **universal**
graph invariant specializes to
\[
 \boxed{K=80-10b.}                              \tag{TR1}
\]
Indeed the accepted formula is
\(K=16(6s+br)-7(6b)-28rs\);
putting \(r=s=2\) gives
\(K=80-10b\). At \(b=6\)
it is \(20>0\), imposing
positive residual degree and
excluding sole support. At
\(b=8\), it is exactly zero,
giving **no residual
obstruction**; for larger \(b\)
it becomes negative. The refined
bound assuming no residual
components on the quadric also
gives no contradiction at the
sole-support endpoint for
\(b=8,r=s=2\), without a
further geometric slope.

Thus \(\boxed{(6,8)}\) is the
**first numerically admissible**
pair where a degree-six equation
can have order two and **both**
existing normality reductions
can lose their hypotheses
simultaneously. This does **not**
establish that an order-two/order-two
complete intersection with sole
support exists. It isolates where
additional actual filtered-jet
or blowup-saturation control is
needed. The earlier normal
\((6,8)\) **index-twelve**
reduction applies only if
at least one equation has
order one; an entirely-thick
\((6,8)\) candidate requires
its own geometry.

**Higher-degree interpretation.**
The graph inequality is positive
only in its specified
\((\alpha=a/r,\beta=b/s)\)
region; when one or both
degrees increase while \(r,s\)
remain small, the bound can
become vacuous. Consequently
normal replacement plus graph
control is not a universal
mechanism, although it covers
large concrete portions of the
low-degree landscape. This is
why degree-specific results
should be assessed by **their
coverage of the order-one
and entirely-thick strata**,
rather than solely by carrier
degree or numerical correction.

<a id="a-second-uniform-threshold-equal-degree-pencils-below-ten"></a>
### Factor integrality is not a cutoff for normality

For an actual degree-\(b\) member with a degree-\(a\) mate, every irreducible factor has degree at least five and degree divisible by \(4/\gcd(a,4)\). Thus every such member is integral if \(b<2n_a\), where \(n_a\) is the smallest permissible factor degree (\(5,6,8\) for \(a\equiv0,2,\text{odd}\pmod4\)). In equal degrees Bézout forces \(d\) even; for \(d=10\) it forbids quintic factors, so **all members** are integral for the eligible \(d=6,8,10\). Degree 12 is the first numerical factorization threshold, not a proved reducible example. Minimal-degree-product pairs have all compatible members integral in every degree, by factor descent to a smaller pair if not; this preserves support, not the thick ideal.

Independently, the [normal-replacement theorem](../../arguments/carriers/normal_carrier_divisor_geometry.md#47-unequal-degree-pairs-can-acquire-an-actual-normal-carrier) gives normality of the *general* member in every degree in the order-one branch. For \((8,8)\) this forces \(R=16\) and exact order eight of \(2C-H\); for \((10,10)\) it forces \(R=25\) and exact order five of \(5C-2H\), using the exact index theorem and minimal-mate divisibility. Neither resolves the entirely-thick sector. The [proof and scope](../../arguments/carriers/normal_carrier_divisor_geometry.md#equal-degree-pencils-below-degree-ten-the-sextic-proof-extends-to-octics) distinguish the two assertions. New generalizations require independent audit.

### A direct bridge from ADE exceptional corrections to normal-layer defects

The established [normal-carrier symbolic budget](../../arguments/carriers/normal_carrier_symbolic_torsion.md#a-symbolic-triple-defect-certificate-for-unrestricted-normal-carriers)
includes the *total* first-symbol zero divisor
\[
 A:=\sum_P A_P=4a-14+\ell, \tag{S7}
\]
and the [mate-independent intrinsic comparison](../../arguments/carriers/normal_carrier_divisor_geometry.md#2-the-intrinsic-local-divisor-is-a-necessary-and-sufficient-mate-test)
gives
\[
 C^2=\ell-\sum_P\frac{A_P+D_{r_P,P}}{r_P}.
\]
Combining these **already proved** formulas with the crepant
resolution identity on a normal Du Val carrier gives
\[
 \boxed{\quad
 -Z^2=
 \sum_{P\in C}\left(
   \left(1-\frac1{r_P}\right)A_P
       -\frac{D_{r_P,P}}{r_P}\right).
 \quad} \tag{S8}
\]
This is a global equality of numerical invariants; the displayed
individual summands must not be labeled local exceptional corrections
without verifying their local identification. It explains why two
seemingly separate proof languages—ADE root-lattice corrections and
ordinary normal-layer defects—can impose the **same overall budget**.
The first-symbol zeros provide the gross correction, local Cartier
indices scale it, and genuine multiplication defects subtract from it.
Hodge equality demands that the resulting total be exactly
\(4a-14+16/a\).

**Example already present in the quintic argument.** The numerically
surviving reduced-symbol ADE configuration
\(4A_1+9A_4\) has \(A_P=1\) at each marked singularity,
local indices \(2\) and \(5\), and no primitive-index
defect in those cases. Formula (S8) gives
\[
 4\left(1-\frac12\right)
 +9\left(1-\frac15\right)
 =2+\frac{36}{5}=\frac{46}{5}.
\]
Its lcm of local indices is exactly \(R=10\), as (S5)
already predicted. In other words, that special quintic row
**simultaneously saturates the adjunction correction and the exact
index budget**. The reason it nevertheless fails is a *further*
integral Picard constraint: the four nodes form an even set, and
the associated double cover violates the global canonical-surface
inequality. See [the actual even-node proof](../../arguments/carriers/quintic_octic_surface_constraints.md#42-the-actual-divisor-relation-forces-an-even-set).

That is a useful model for distinguishing stages of an exclusion.
Reaching the Hodge correction numerically explains why a candidate
survives local counting; it does **not** mean that an actual surface
with the required integral divisor relation exists. The final
global-cover obstruction cannot be replaced by additional decimal
precision in the correction budget.

### The quintic double cover and sextic triple cover are one mechanism

The exact local-index formulas (S5) reveal the strongest
cross-degree connection. A hypothetical normal \((5,8)\) pair
forces a **nontrivial two-torsion** Weil class
\[
 \Delta_5=5[C]-4[H],\qquad 2\Delta_5=0,
\]
while an actual normal \((6,6)\) pair forces a
**nontrivial three-torsion** Weil class
\[
 \Delta_6=3[C]-2[H],\qquad 3\Delta_6=0.
\]
The "nontrivial" assertions use the exclusion of small-degree
mates, not just numerical equivalence.
Both yield connected, quasi-étale cyclic covers of the normal
carrier, with their nontrivial behavior concentrated at
the singularities meeting \(C\). This is an instance of the
[all-degree normal-carrier torsion construction](../../arguments/carriers/normal_carrier_symbolic_torsion.md#2-a-self-contained-rational-ample-local-detection-theorem),
not two unrelated ad hoc covers.

The [quintic ADE proof](../../arguments/carriers/quintic_octic_ade_cover_and_triple.md#3-the-forced-double-cover-and-its-canonical-map)
uses the **double cover** together with local ADE data,
its canonical map, and a global canonical inequality to exclude
the \((5,8)\) normal ADE sector. The
[sextic all-pair reduction](../../arguments/carriers/sextic_pair_reduction.md#exact-global-invariants-of-the-order-three-cover)
already builds the **triple cover** even without an ADE assumption,
and computes its Euler characteristic from the saturated divisor
layers. For the surviving ADE sextic lane
\(\ell=6,D_2=0\), this yields
\[
 K_Y^2=72,\qquad \chi(\mathcal O_Y)=15,
\]
without an incompatible irregularity or canonical-map bound.
The cover method is therefore **not absent in degree six**;
the numerical contradiction available in degree five does
not presently survive.

Indeed for a normal degree-\(a\) hypersurface with an order-\(t\)
quasi-étale cyclic cover \(Y\), the canonical pullback identity
gives the general numerical relation
\[
 \boxed{\quad K_Y^2=t\,a\,(a-4)^2.\quad} \tag{S9}
\]
Thus the quintic \(t=2\) case has \(K_Y^2=10\), while the
sextic \(t=3\) case has \(K_Y^2=72\).
Canonical-surface inequalities can be much less restrictive in
the latter regime. Before importing the quintic contradiction into
another degree, one must calculate the actual cover's
\(\chi,p_g,q\), singularities and canonical map; the bare
existence of torsion, or an even/three-divisible exceptional
configuration, is not enough.

This comparison identifies a **specific obstruction gap**:
the cyclic cover and local-index structure are already present
in both degrees, but the higher canonical volume leaves room
for the sextic numerical invariants. New arithmetic or global
equation restrictions would have to remove that room; repeating
the same cover construction without an additional inequality
would not advance the question.

### Why the global singularity-counting approach weakens in higher degree

The required correction \(4a-14+16/a\) grows only
**linearly** with \(a\). By contrast, the classical
Chern/Noether/Hodge formulas for the minimal resolution of a
degree-\(a\) hypersurface with only Du Val singularities give
\[
 h^{1,1}=
 \frac{2a^3-6a^2+7a}{3},\qquad
 \operatorname{rk}(\text{exceptional root lattice})
 \le h^{1,1}-1. \tag{S10}
\]
The upper rank budgets are \(19,44,85\) in degrees \(4,5,6\),
respectively; the subtraction of one reserves the positive
hyperplane class. These are the established surface bounds
used in the [quartic-pair proof](../../arguments/normal-geometry/quartic_pair_obstruction.md),
[quintic ADE proof](../../arguments/carriers/quintic_octic_surface_constraints.md#41-the-rank-bound-leaves-one-configuration)
and [sextic ADE reduction](../../arguments/carriers/sextic_ade_reduction.md#the-rank-budget-and-the-surviving-row).

| \(a\) | Required \(-Z^2\) under a mate | ADE root-rank capacity |
| --- | ---: | ---: |
| \(4\) | \(6\) | \(19\) |
| \(5\) | \(46/5\) | \(44\) |
| \(6\) | \(38/3\) | \(85\) |

This gives a structural reason that a **raw exceptional-rank
contradiction cannot simply be extrapolated** from degree four:
the available ambient cohomological capacity grows cubically
while the correction target grows linearly. Additional restrictions
must connect *where* the singularities occur, their actual local
indices and first-normal orders, and the integral divisor/cover
geometry. The quintic even-node cover provides a concrete
example: its last configuration fits the rank budget but
violates an integral global relation.

The transition from quintic to sextic should therefore not be
explained as simply "a longer thickening": the first numerically
possible pairs have generic lengths \(10\) for \((5,8)\)
and **\(9\)** for \((6,6)\). Nor does order-two generic
singularity persist for both sextic equations, by (S6).
What grows is the **geometric room on the carrier**:
larger Picard/root capacity, a more positive canonical class,
and the much larger canonical volume of the required
triple cover. This guides what to seek in higher-degree
arguments: genuine compatibility constraints, not just
a higher-volume repetition of low-degree enumeration.

### The synthesis should change what each narrow case is asked to prove

There are **three distinct levels** of compatibility:

1. **Extremal numerical ray.** On normal carriers (S1)--(S3)
   provide a complete fixed-carrier decision criterion.
   Local index, normal symbol, and ADE proofs attempt to
   force \(\Gamma_X(C)>0\) or rule out the equality geometry.
2. **Actual descent and inverse support.** On nonnormal
   carriers, a divisor or root upstairs may fail to descend
   through the *whole conductor*, or the inverse of \(C\)
   may contain extra points. This is where the
   [quintic Gorenstein-normalization proof](../../arguments/carriers/quintic_gorenstein_normalizations.md)
   and [toric inverse-support proof](../../results/toric_quintic_carrier_exclusion.md)
   act; neither is merely another test of the normal Hodge gap.
3. **Actual two-equation transverse realization.** When a carrier
   is generically singular along \(C\), or one studies a
   proposed thickening directly, abstract filtrations and normal
   symbols must still be compatible with global homogeneous
   equations and the complete parameter-saturated ideal.
   The [quartic-pair intrinsic/filtered/surface proofs](../../arguments/normal-geometry/quartic_pair_obstruction.md)
   and [all-pair sextic filtration](../../arguments/carriers/sextic_pair_reduction.md)
   probe this level with different hypotheses. The
   [exceptional quartic Hilbert boundary](../../arguments/torus/quartic_hilbert_chow_limits.md#detaching-the-embedded-endpoint)
   is a concrete warning: the correct fundamental cycle and even
   a CI Hilbert function do not guarantee proper quartic generators.

**Interpretation, not another exclusion theorem.** The many low-degree
proofs ask how a mate could supply the discrepancy between negative
adjunction self-intersection and the positive ray \(C^2=16/a\).
Some special cases fail by index/topology, others by conductor descent,
others at actual normal/filtered equation realization. Their proofs
should be compared by *which compatibility condition they destroy*,
not aggregated into an unsupported all-degree singularity budget.
The remaining gap is to show that **every** hypothetical higher-degree
carrier lies in a controlled one of these mechanisms and that the
appropriate local correction can never saturate its global
compatibility conditions—or to construct a carrier reaching equality.
The degree-four carrier theorem achieves exhaustive exclusion in one
degree; the present quintic and sextic results do not.

## 5.8 Three mechanisms for the quartic-pair obstruction

The [quartic-pair chapter](../../arguments/normal-geometry/quartic_pair_obstruction.md) owns the full bounded proof of [R-0022](../../results/quartic_44_filtered_exclusion.md), independently of R-0001. It begins with the hypothetical pair, derives its two allowed Gorenstein filtration types, and exposes the different proof mechanisms before the calculations.

- The **intrinsic fourth-extension proof** classifies the two allowed saturated types using the embedded triple's contact-extension class. Its only surviving quadruple is 4C on the containing quadric, which cannot belong to a proper quartic pair. This completed proof uses neither ambient quartic source matrices nor a global surface bound.
- The **filtered-contact proof** exhausts the actual quartic source spaces through the allowed triples. Every nonfactored pencil has a nonzero cubic-contact determinant, forcing generic transverse length three rather than four. Its finite source matrices and exact computational support remain explicit dependencies.
- The **surface proof** derives moving singularities and defect singularities from the rank-four local algebra. Their exceptional curves have rank at least twenty-one, incompatible with a resolved quartic's characteristic-zero surface bound. The K3 presentation uses the rational-double-point literature.

The **direct-blowup presentation of the surface proof** constructs those exceptional chains and proves crepancy explicitly, then derives the global bound from Noether's formula and Hodge decomposition. It removes surface-singularity classification from the proof, while retaining global surface geometry.

The [completed intrinsic argument](../../arguments/normal-geometry/intrinsic_fourth_extension.md) supplies the neighborhood-only mechanism for the two allowed quartic types. The [general contact-module criterion](../../arguments/normal-geometry/quartic_pair_obstruction.md#6-what-a-neighborhood-only-proof-still-needs), determinant target and counterexamples remain useful beyond this application; a nonvanishing or realization theorem for arbitrary higher-length types does not follow.

A proper quartic intersection can contain the fixed curve with multiplicity three and a genuine residual quartic. The chapter includes an explicit pair and explains why its eight moving exponent-three germs fit the surface budget. Thus this is also a laboratory for intersections with residual support. The characteristic-two sole-support quartic pair is a separate existence construction; the relevant conormal geometry, separability and surface bound change with characteristic.
