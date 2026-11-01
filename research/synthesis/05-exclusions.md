# 5. What the exclusion results actually rule out

The characteristic-zero fixed-curve problem remains open for higher-degree
surfaces. Its closed low-degree boundary is the accepted
[all-integral-quartic theorem R-0001](../results/quartic_carrier_exclusion.md).
The [complete carrier proof](quartic_carrier_proof.md) gives the actual
argument; this chapter states its consequences and relates the different
obstruction mechanisms. In every characteristic \(p>0\), the same fixed
curve **is** an STCI using a quartic carrier; see the
[explicit construction](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier).

Two reviewed provisional results sharpen degree-five scope. An integral
[nonnormal quintic with Gorenstein normalization](quintic_gorenstein_normalizations.md)
has no mate in any degree. A proper sole-supported degree-(5,8) pair cannot
have a [globally ADE quintic](quintic_octic_surface_constraints.md), even with
repeated first symbols. Normal quintics with worse singularities and nonnormal
quintics with non-Gorenstein normalization are not excluded by these theorems.

## 5.1 The precise degree-four theorem and its proof mechanisms

Fix an algebraically closed characteristic-zero field and
\(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\). For **every integral
quartic surface** \(X\supset C_0\) and **every homogeneous form** \(G\)
of positive degree, \(V(X,G)_{\mathrm{red}}\ne C_0\). No normality,
singularity, reduced-conductor, mate-degree, or first-normal-order
hypothesis is imposed. The theorem concerns this embedding and its
projective equivalents.

The [proof](quartic_carrier_proof.md) derives generic regularity and full
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
The independent [quartic-pair proof](quartic_pair_obstruction.md) excludes
only \((4,4)\); the normal bounded-index result
[R-0035](../results/normal_carrier_bounded_index_exclusion.md) has its own
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

- [R-0025](../results/ci_fixed_sextic_jet_rigidity.md) forces residual support
  for one prescribed sextic and its stated equation-space comparison; it
  does not quantify over all sextics.
- [R-0030](../results/local_filtration_comparison_defect.md) and the conormal/
  socle theorems retain their actual-source, saturation, and defect
  hypotheses. Neither a full initial ideal nor a zero module-comparison
  defect alone gives an STCI exclusion.
- The marked flag/dual/ruled models and the fixed-lower determinant test
  describe their actual geometric objects or conditional existence tests;
  they do not establish that every hypothetical pair belongs to them.
- Positive-characteristic sole-support constructions and prescribed
  arithmetic nonlifting concern different characteristics or specified
  embedded schemes. They do not contradict a characteristic-zero theorem.

The [carrier proof's characteristic comparison](quartic_carrier_proof.md#8-what-changes-in-positive-characteristic)
identifies the precise boundaries: differential mate-degree cancellation,
nilpotent Frobenius descent, the characteristic-two conormal jump,
inseparable trisecants in characteristic three, and the characteristic-zero
global surface bound. The distinction is mathematical, not a blanket
warning about reduction modulo primes.

## 5.6 Common mechanisms and the missing higher-degree implication

Normalization yields a divisor relation; conductor gluing tests actual
descent; numerical pullback measures exceptional correction; the normal
line measures actual ideal vanishing; a ribbon tests whether the required
global normal map exists. These are linked operations on different
objects. The [general ruled criterion and ribbon Hom threshold](quartic_carrier_proof.md)
extract reusable parts of the quartic proof, while its endpoint cubic
normal coefficient explains why some case distinctions remain necessary.

The unrestricted problem still needs a construction or obstruction for
actual homogeneous higher-degree pairs. Formal/local/graded models,
numerical class compatibility, and one fixed-carrier exclusion do not
establish that missing implication. See [the frontier](06-frontier.md) and
[dependency map](DEPENDENCIES.md).

## 5.8 Three mechanisms for the quartic-pair obstruction

The [quartic-pair chapter](quartic_pair_obstruction.md) owns the full bounded proof of [R-0022](../results/quartic_44_filtered_exclusion.md), independently of R-0001. It begins with the hypothetical pair, derives its two allowed Gorenstein filtration types, and exposes the different proof mechanisms before the calculations.

- The **intrinsic fourth-extension proof** classifies the two allowed saturated types using the embedded triple's contact-extension class. Its only surviving quadruple is 4C on the containing quadric, which cannot belong to a proper quartic pair. This completed proof uses neither ambient quartic source matrices nor a global surface bound.
- The **filtered-contact proof** exhausts the actual quartic source spaces through the allowed triples. Every nonfactored pencil has a nonzero cubic-contact determinant, forcing generic transverse length three rather than four. Its finite source matrices and exact computational support remain explicit dependencies.
- The **surface proof** derives moving singularities and defect singularities from the rank-four local algebra. Their exceptional curves have rank at least twenty-one, incompatible with a resolved quartic's characteristic-zero surface bound. The K3 presentation uses the rational-double-point literature.

The **direct-blowup presentation of the surface proof** constructs those exceptional chains and proves crepancy explicitly, then derives the global bound from Noether's formula and Hodge decomposition. It removes surface-singularity classification from the proof, while retaining global surface geometry.

The [completed intrinsic argument](intrinsic_fourth_extension.md) supplies the neighborhood-only mechanism for the two allowed quartic types. The [general contact-module criterion](quartic_pair_obstruction.md#6-what-a-neighborhood-only-proof-still-needs), determinant target and counterexamples remain useful beyond this application; a nonvanishing or realization theorem for arbitrary higher-length types does not follow.

A proper quartic intersection can contain the fixed curve with multiplicity three and a genuine residual quartic. The chapter includes an explicit pair and explains why its eight moving exponent-three germs fit the surface budget. Thus this is also a laboratory for intersections with residual support. The characteristic-two sole-support quartic pair is a separate existence construction; the relevant conormal geometry, separability and surface bound change with characteristic.
