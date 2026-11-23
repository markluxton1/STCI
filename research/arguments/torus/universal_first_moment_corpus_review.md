# Universal first moment viewed through every Framework and the current literature

**Review scope (2026-11-22).** This is a synthesis of **all nine main-branch Framework indexes**, **all 84 main-branch Result statements** (individually routed in the [Result crosswalk](universal_first_moment_result_crosswalk.md)), the relevant owning Argument proofs and controls, and the mathematical changes exposed by open PRs [#171](https://github.com/markluxton1/STCI/pull/171), [#172](https://github.com/markluxton1/STCI/pull/172) and [#173](https://github.com/markluxton1/STCI/pull/173). It is not an independent six-perspective proof audit or a line-by-line certification of every historical Argument; the nine indexes route to 236 main-branch Argument files. New branch deductions have their stated pending-review status. The literature check uses primary theorem statements and abstracts; a bounded search is not a novelty certificate.

The sole mathematical target of this review is the **necessary condition**
\[
 \tag{UM1}
 [V(F_a,G_b)]=\sum_i n_i[C_{u_i,v_i}]
 \quad\Longrightarrow\quad
 M_1=\sum_i n_i\,\frac{u_i}{v_i}=0
\]
for **every actual proper homogeneous pair** in characteristic zero, of **any**
degrees \(a,b>0\), with \(ab=4\sum_i n_i\). It is stronger than is
needed for STCI, but would exclude \(m[C]\) since \(M_1=m\neq0\).
Do not confuse: (i) a pair containing a translate, (ii) its complete
intersection *cycle* consisting entirely of translates, (iii) the
reduced union of these translates, and (iv) a proper two-generated ideal.

The projected binary Chow polynomial
\(H_\sigma(A,B)=\prod_i(A-(u_i/v_i)B)^{n_i}\) has \(M_1\) as its negative
next-to-leading coefficient. The full homogeneous transverse Chow
polynomial retains both \(u_i,v_i\); the first moment is only a
necessary possible separator, not the full realization criterion.
The equation \(V(M_1)\) is stable under simultaneous transverse
torus translation, since \(M_1\) transforms by the character \(u/v\).
It is not a translation-invariant scalar; its **vanishing** is intrinsic
to the chosen torus character.

### Post-review strengthened bridge: Serre duality of first normal jets

The [new first-jet spectral–Jacobian argument](spectral_jacobian_first_jet_bridge.md)
refines the earlier exact source picture. A translated-cycle CI
satisfies \(A M_{12}-2B M_{03}=0\) in its actual ring, and
\[
 2M_1=\operatorname{Res}_{f_0,g_0}(p s-q r).
\]
Unlike the **general** six-layer degree-two trace, this formula
depends only on the first normal equations jets **provided**
the entire cycle is translated. The residue is the Serre trace
of a Koszul connecting class in \(H^1(\mathbf P^1,\omega)\),
and is a nondegenerate alternating Macaulay pairing.
The two quotient characters \(\xi=u/v,\eta=u^2/v\) are
respectively the parameters of the unique containing quadric
and of the cubic scroll with the two fixed residual trisecants.
The missing proof is now an **isotropy assertion for the
first-jet image of the simultaneous spectral–Jacobian
complete-intersection incidence**, rather than an unrestricted
six-layer polynomial calculation. The new bridge is
pending independent review and does not establish UM1.

## I. Three candidate general mechanisms, ranked by missing work

### 1. Source trace / Chow norm: the closest exact reduction

For any such Chow-matched pair, the disjoint line \(L=V(x_0,x_3)\)
gives an actual finite free algebra
\(E=k[x_0,x_1,x_2,x_3]/(F,G)\) over \(A=k[x_0,x_3]\).
Its graded module decomposition is fixed by the CI degrees; its
multiplication is not. The exact identity
\[
 \tag{T} \operatorname{Tr}_{E/A}(x_1x_2)
 =4x_0x_3 M_1
\]
uses trace additivity through generic nilpotent layers. This equality
requires no invariance of \(E\). The
[all-degree degree-two trace theorem in PR #171](https://github.com/markluxton1/STCI/blob/codex/chow-polytope-realization/research/arguments/torus/fixed_surface_and_endpoint_algebras.md#7-the-first-trace-depends-only-on-two-lower-fiber-degree-layers)
shows that its **value** is determined by the six layers
\(f_0,f_1,f_2,g_0,g_1,g_2\) in powers of the center coordinates
\(x_0,x_3\), and expresses it by a Grothendieck residue.
The [norm/Chow identity in PR #172](https://github.com/markluxton1/STCI/blob/chatgpt/cross-degree-exclusion-synthesis/research/arguments/torus/chow_arrangement_moments.md#the-homogeneous-transverse-chow-form-as-a-section-norm)
expresses the same scalar as the mixed coefficient of the plane-section
resultant. These are **two descriptions of one condition**, not
two independent obstructions. Invariant or eigenform sources,
coordinate congruences and certain one-sided cone jets make (T) vanish.
Nothing known says Chow matching forces one of those source conditions.

The genuine open gate is to use **the full translated-cycle restriction**
on \(F,G\) to force the six-layer trace to vanish, or to find a
non-eigenform counterexample. The fixed quadric/endpoint restriction
alone is insufficient: the explicit quartic source counterexample
can have zero first trace and nonetheless retain residual sheets.
The center-jet restriction from \(I_C(d)\) is surjective at fixed depth
for \(d\gg0\) (PR #172), so a proof based only on one source's
low-order jet cannot be degree uniform. Test *joint* equations,
their syzygies, and the global Chow requirement.

### 2. Supported divisor cycles and class-group relations: a distinct route

On a fixed normal integral carrier \(X\), PR #172 describes all
supported mate multiplicity vectors via a negative-semidefinite Hodge
matrix, plus Cartierness of the **total** divisor. The nonnormal
extension replaces this by normalized intersection data and actual
downstairs almost-Cartier/conductor relations. These are strong
necessary/sufficient fixed-carrier criteria under their own
hypotheses. The [all-mate exceptional quartic theorem](https://github.com/markluxton1/STCI/blob/chatgpt/cross-degree-exclusion-synthesis/research/arguments/torus/quartic_exceptional_carrier_geometry.md#all-mate-degrees-on-a-retained-exceptional-carrier)
forces \(n_+=n_-=2j\) for supports with \(u/v=\pm1\), and
hence \(M_1=0\) for all mate degrees \(4j\). Here \(M_1\) is forced
by the multiplicity **lattice**, not a proper invariant initial pair.
This mechanism transfers to a broader carrier only after proving
that its allowable mate vectors lie in the kernel of the
additive functional \(n\mapsto\sum n_iq_i\).

**Open geometric comparison:** is there a canonically constructed,
suitably equivariant additive cycle functional (for example arising
from a residual trace, a relative divisor-class map, or a reciprocity
pairing) that sends every ambient hyperplane section to zero and
evaluates to \(q_i\) on each \(C_{u_i,v_i}\)?
No such global homomorphism has been constructed. Ordinary
\(\mathrm{CH}_1(\mathbf P^3)=\mathbb Z\) cannot carry it, since all
degree-four translates have the same ordinary Chow class but different
\(q_i\). Any construction must remember the *marked projection line,
torus quotient or boundary*, and be compatible with actual
divisor descent. This is a precise conceptual alternative to
the six-layer source computation, not a claimed theorem.

### 3. Normal structures, multiplication and global realization

The third approach asks whether the support hypothesis forces
relations on the *multiplication map* of the finite cover, not just
its graded module. Primitive/quasiprimitive filtrations, socle duality,
root Picard torsion and local coregularity constrain that algebra
when appropriate. But there are explicit normal-Koszul cancellations
of arbitrarily high order, equal restricted graded diagrams with
different embedded algebras, and two opposite weight limits with the
same indices but different generic contact. Their common implication
is **negative:** splitting, Hilbert data, root torsion or determinant
indices alone do not recover \(\operatorname{Tr}(\mu_{x_1x_2})\).
A useful theorem would compare the full algebra-law and actual
homogeneous equation maps to that specific trace functional.

## II. Framework-by-Framework assessment (all nine)

| Main Framework | What it contributes to UM1 | Precisely what is not supplied |
|---|---|---|
| [F-0001 Torus-supported boundaries](../../frameworks/torus-supported-boundaries/index.md) | Invariant cycle versus possibly non-invariant ideal; both full Hilbert limits; actual generator and cancellation layers; paired extrema from the same source | A proper invariant CI in the fixed Chow fiber, or a theorem that the mixed trace of non-invariant sources is zero |
| [F-0002 Embedded torus quotients](../../frameworks/embedded-torus-quotients/index.md) | Exact constant embedded quotient, evaluation ranks, degree-exhaustion, endpoint algebras and moving quotient lower bounds | Constant quotient coverage for arbitrary moving nonreduced CI; an equality between endpoint ranks and \(M_1\) |
| [F-0003 Formal normal geometry](../../frameworks/formal-normal-geometry/index.md) | Curvilinear/entirely-thick split, actual source filtrations, root lifting, Gorenstein socle and projective compatibility | Any canonical map from local root/jet obstruction to the additive function \(M_1\); all-degree finite truncation |
| [F-0004 Arithmetic supported lifts](../../frameworks/arithmetic-supported-lifts/index.md) | Char-2 and odd-prime explicit realizations, Frobenius collisions, finite-order nonlifting and endpoint specialization | Extension of a prescribed arithmetic obstruction to arbitrary characteristic-zero sources; \(p\mid m\) permits \(M_1(m[C])=0\) |
| [F-0005 Carrier normalization](../../frameworks/carrier-normalization/index.md) | Exact Cartier/Hodge/descent monoids and many all-mate exclusions; candidate geometric explanation of linear relations in multiplicity vectors | A carrier-independent functional of those relations equal to \(M_1\), especially on singular/non-Cartier generic branches |
| [F-0006 Global equation realization](../../frameworks/global-equation-realization/index.md) | Correct actual-source incidence, Sylvester Chow determinant, trace/norm, and necessary coprimeness | A source relation forcing its mixed coefficient to vanish on the entire Chow-matched image |
| [F-0007 Residual construction](../../frameworks/residual-construction/index.md) | Degree-exhaustion terminal condition, residual attachment and movement bounds, actual absorption examples | A rule identifying a general residual curve with a sum of translates, or a universal zero-moment identity under residual absorption |
| [F-0008 Spectral roots](../../frameworks/spectral-roots/index.md) | Relative Picard torsion of a root divisor gives an exact graded second-relation criterion; actual octic and (6,16) tests | Identification of root Picard class with the \(q=u/v\) character, or ambient source/CI lift in the remaining strata |
| [F-0009 Local cohomology](../../frameworks/local-cohomology/index.md) | Hartshorne–Polini/Hellus exact two-coregular-elements test; simultaneous ancestors and actual multiplication targets | A map whose value is \(M_1\) and which vanishes for all coregular pairs; bounded quartic ancestors have residual degree |

### Consequences of this matrix

1. **Proofs about a chosen carrier are important but not a universal
   source reduction.** In PR #172, generic curvilinearity on every
   component allows a general normal integral replacement of the larger
   equation via Bertini and Serre's criterion. Entirely-thick
   generic algebras (embedding dimension two) do not admit that
   replacement. The two regimes must remain separate. For a
   *hypothetical sole-support pair of minimal degree product*, factor
   descent makes its actual generators integral; this is a weaker
   STCI-specific route than UM1 for all arrangements.
2. **Hilbert-flat limits are not enough.** The exceptional non-invariant
   quartic cycles in PR #171 lie outside the Chow closure of invariant
   quartic CI cycles, yet have \(M_1=0\). Full toric limits can require
   three generators with the CI polynomial (R-0046).
   Invariant-cycle continuity extends the *linear Chow equation* only
   from a **covered** locus, not from all possible CIs.
3. **Finite-jet versus all-degree statements must be sorted by their
   actual source.** The trace itself is determined by six
   center-of-projection layers in all degrees, but the property
   "the entire cycle is translated" is not determined by those
   layers; high-degree single-form jets are flexible. Conversely,
   normal-cone filtrations admit arbitrarily high cancellation pages.
   Neither observation contradicts the other: they are different
   filtrations and different questions.
4. **The two types of torus boundary cannot be merged.**
   Low/high intrinsic-weight equation filtrations, completed image
   algebras at \(p_0,p_\infty\), and jets at the *disjoint projection
   line* \(L\) are different. PR #173's two canonical sections of the
   Chow quotient graph explain the intrinsic extremes, not the
   six-layer trace restriction by themselves.
5. **Do not trade necessary conditions for a classification.**
   The exact \((4,4)\) dual affine-line incidence is a reduced-CI
   criterion. The endpoint Hilbert polynomial, normal-carrier
   multiplicity matrix and mixed-moment determinants impose further
   conditions on realizability. Their classification is unnecessary
   for proving UM1 and none by itself covers repeated non-invariant
   cycles.

## III. Relevant literature, strongest applicable statements and non-implications

**Direct primary algebra for the proposed proof.**

* Cattani–Dickenstein–Sturmfels,
  [*Computing Multidimensional Residues*](https://arxiv.org/abs/alg-geom/9404011),
  gives a rational global-residue expression for traces of
  finite-dimensional complete intersections. It applies to the
  zero-dimensional fibers of the finite cover when the leading
  fiber forms remain a regular sequence. It **calculates** (T), but
  Euler–Jacobi vanishing on lower residue numerators does not imply
  vanishing of the **trace**, whose numerator includes the Jacobian.
* D'Andrea–Jeronimo,
  [*Rational Formulas for Traces in Zero-Dimensional Algebras*](https://arxiv.org/abs/math/0503721),
  expresses the trace of a multiplication map via generalized Chow
  forms, including sparse resultant formulas for suitable torus CIs
  over characteristic zero. This verifies the trace/Chow
  coefficient dictionary; it does not make its value zero.
* Eisenbud–Ulrich,
  [*Duality and Socle*](https://www.math.purdue.edu/~bulrich/papers/Duality-and-Socle-180119.pdf),
  Theorems 8.1, 8.3 in the referenced manuscript, relate
  the relative CI different and trace duality for finite-free
  presentations. PR #171 uses them for endpoint different lengths.
  They constrain **trace lattices**, not the particular mixed
  trace without a source identity.
* Eisenbud–Schreyer,
  [*Resultants and Chow Forms via Exterior Syzygies*](https://arxiv.org/abs/math/0111040),
  produces the cycle Chow form from a determinant of a Chow complex.
  The proper two-surface pair supplies the Sylvester resultant.
  Factorization or a perfect-power Chow target still requires an
  actual pair and does not establish a vanishing coefficient.
* Vaccarino,
  [*The ring of multisymmetric functions*](https://www.numdam.org/articles/10.5802/aif.2111/),
  controls the coefficient algebra of the full transverse
  Chow product, in characteristic zero especially through mixed
  power sums. It yields an invariant-theory dictionary, not
  additional necessary CI relations.

**Strong geometric and arithmetic input.**

* Hartshorne–Polini,
  [*Quasi-cyclic modules and coregular sequences*](https://arxiv.org/abs/1907.05472),
  Theorem 3.1 under its regular-sequence and higher-local-cohomology
  hypotheses, gives an equivalent local-cohomology criterion for
  a set-theoretic complete intersection. It is the strongest
  **abstract all-degree criterion** in the corpus, but there is no
  established map from its simultaneous coregularity defect to M1.
  Their [*Divisor class groups of singular surfaces*](https://arxiv.org/abs/1301.3222)
  supplies a fixed-carrier almost-Cartier criterion when the
  marked curve meets the singular locus only finitely; not when
  it is generically singular along the carrier.
* Česnavičius–Scholze,
  [*Purity for flat cohomology*](https://annals.math.princeton.edu/2024/199-1/p02),
  Corollary 7.2.3, and Cotner–Zavyalov,
  [*Lefschetz theorems in flat cohomology and applications*](https://www.cambridge.org/core/journals/compositio-mathematica/article/lefschetz-theorems-in-flat-cohomology-and-applications/8556201EDB51D7F2F76F5950A800CD64),
  Theorem 1.1.8, supply strong Picard-saturation and
  numerical-Picard triviality for projective complete intersections
  under their stated hypotheses. PR #172 uses these to sharpen
  **fixed-carrier** divisor-class realizability; neither provides
  a class-group functional whose values are the torus positions.
* Bănică–Forster, [*Multiplicity Structures on Space Curves*](https://www.mathematik.uni-muenchen.de/~forster/eprints/multip_struct.pdf),
  and Ferrand's doubling construction give the primitive and
  quasiprimitive extension framework. Their hypotheses concern
  specified conormal quotients, not all finite-free CI trace algebras.
  Goto–Heinzer–Kim's
  [leading-ideal theory](https://www.sciencedirect.com/science/article/pii/S0021869307001202)
  classifies local initial-form phenomena for height-two regular
  parameter ideals; the global homogeneous lift remains a separate
  problem.
* Kapranov–Sturmfels–Zelevinsky, *Quotients of toric varieties*
  (Math. Ann. 290 (1991)), gives the normalized toric Chow quotient
  and fiber-polytope fan. PR #173 computes its special four-ray
  fan. Chow quotient geometry controls **cycles and limit strata**,
  not proper-CI preservation.
* Benoist, [*The resultant divisor is negative*](https://arxiv.org/abs/2601.11474)
  (2026), gives a tower of blowups for gcd strata of **binary**
  forms and identifies a normal cancellation map in its setup.
  This is a promising algebraic template for the pair restricted to
  \(L\), but its theorem is not an all-dimensional blowup of the
  \(\mathbf P^3\) equation-source incidence.
* Brevik–Nollet,
  [*Noether–Lefschetz theory and surfaces containing a multiple curve*](https://doi.org/10.1017/nmj.2026.10139)
  (published 19 October 2026), Theorem 1.1: over \(\mathbb C\),
  for a smooth projective threefold \(X\) with \(H^1(O_X)=0\),
  smooth connected \(C\subset X\), \(m\ge2\), and very general
  sufficiently high-degree surface \(Y\) containing the **ordinary
  infinitesimal neighborhood** \(I_C^m\),
  \(\operatorname{Pic}(X)\to\operatorname{Pic}(Y)\) is an isomorphism.
  In particular very general such thick surfaces in \(\mathbf P^3\)
  have Picard generated by \(O(1)\). This is relevant to the
  *entirely-thick* carrier locus, but neither controls **special
  carriers** chosen by a mate nor identifies the generally
  non-Cartier class of \(C\) with an invertible sheaf.
  It therefore supplies no UM1 theorem.
* Ferrand–Szpiro/Forster's affine lci STCI theorems do
  not preserve the projective boundary or split the projective
  bundle into two prescribed homogeneous equations. The
  characteristic-positive binomial construction (Barile–Morales–Thoma)
  relies on Frobenius and does not imply characteristic-zero UM1.

**Literature status.** Craighero–Gattazzo's classical \((4,4)\)
and cubic-carrier exclusions, together with Eisenbud–Harris (2024)
and Murayama's April 2026 notes, still leave the unrestricted
characteristic-zero rational-quartic STCI problem unresolved on the
checked sources. No located theorem states UM1 for arbitrary
non-invariant proper Chow-matched pairs. This conclusion has the
ordinary limits of a literature search.

## IV. Upward iteration: what newly changes

**A. The strongest common identity is not an intersection-number
budget.** UM1 is the vanishing of a **semi-invariant linear Chow
coefficient**, equivalently a specific trace of the actual finite
cover. Replacing it with endpoint delta, Hodge equality, degree
exhaustion or a root torsion condition may lose exactly the
coefficient to be explained. Their rigorous role is to restrict
the image of a *joint actual-equation map* into that trace.

**B. Two rigorously distinct possible bridges emerge.** The
six-layer residue functional is a concrete source-level equation.
The proposed relative-divisor functional would be a geometric
explanation if constructed, but cannot factor through the ordinary
ambient Chow group. Both must account for the exceptional
non-invariant quartic family and arbitrary repeated multiplicities.

**C. Minimal STCI need not wait for all arrangements.** The
complete all-degree UM1 statement is sufficient but stronger than
needed. A proof that (T) vanishes for all *minimal-degree-product*
sole-supported pairs would suffice. PR #172's factor descent and
normal replacement can be used for that narrower target, subject
to the entire-thick case. Conversely, restricting attention
solely to minimal pairs loses the advantageous symmetric cycle
family and should not be confused with a derivation of UM1.

**D. A second synthesis pass does not close the gap.** The new
Brevik–Nollet paper is a useful very-general result but cannot
remove the exceptional-special-carrier locus. The all-mate
exceptional quartic theorem is a genuine extension of known
vanishing coverage, but fixed-carrier lattice constraints do not
yet define an all-carrier character. The remaining obstacle is
specific: connect the global Chow-matched support restrictions
to the single degree-two finite-cover trace.

## V. Bounded next questions, chosen for information gain

The most useful first test is to **pull back the mixed Chow coefficient
to the actual source incidence** for arbitrary degrees and express it
via the universal six-layer residue formula, retaining the condition
that the *entire* resultant lies in the translated-Chow product locus.
Compare three exact solved inputs on the same functional:
(1) invariant/eigenform CI; (2) the exceptional non-invariant
quartic pencils; (3) non-eigenform one-sided cone-jet presentations.
Ask whether a common relation on the actual **pair** is forced,
rather than separately postulating a normal form for each generator.
A failure should produce a concrete candidate counterexample or an
identified missing higher-source condition.

The independent geometric alternative is to test whether the
fixed-carrier mate lattice gives an additive, equivariant
\(q\)-functional on its realized divisor subgroup. The
exceptional carrier and the fixed toric quartic provide contrasting
non-normal models. One must verify that the proposed functional
respects **relations of actual Cartier divisors**; ordinary
intersection theory alone is too coarse.

The lower-priority alternatives are all-degree classification of
CI arrangements, complete Hilbert/Chow compactification, additional
sextic numerical tables, and new unrestricted fixed-depth normal
jet calculations. None currently has a specified bridge to UM1
stronger than the two above.

**Stop condition for this review:** the current proof corpus
supplies no additional justified all-degree necessary equation after
the trace/residue, divisor-monoid and global source comparisons.
The missing bridges are explicit; further claims require new
arguments and independent review. This document is not a proof of
UM1 and does not mark PR #173 ready for merge.
