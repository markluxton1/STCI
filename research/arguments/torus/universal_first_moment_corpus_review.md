# Universal first moment viewed through every Framework and the current literature

**Review scope (2026-11-22).** This is a synthesis of **all nine main-branch Framework indexes**, **all 84 main-branch Result statements** (individually routed in the [Result crosswalk](universal_first_moment_result_crosswalk.md)), the relevant owning Argument proofs and controls, and the mathematical changes exposed by open PRs [#171](https://github.com/markluxton1/STCI/pull/171), [#172](https://github.com/markluxton1/STCI/pull/172) and [#173](https://github.com/markluxton1/STCI/pull/173). It is not an independent six-perspective proof audit or a line-by-line certification of every historical Argument; the nine indexes route to 236 main-branch Argument files. The combined integration of November 23, 2026 received six independent review perspectives; individual proof owners record their covered reconstruction routes and inherited dependencies. That review does not turn this synthesis into a line-by-line certification of the historical corpus. The literature check uses primary theorem statements and abstracts; a bounded search is not a novelty certificate.

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
six-layer polynomial calculation. The bridge was independently reconstructed in the combined scoped
correctness review of November 23, 2026; its spectral–Jacobian proof owner
records the inherited mixed-minor/socle and residue-duality inputs. It does
not establish UM1.

## I. Three candidate mechanisms and their missing inputs

### 1. Source trace and Chow norm

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
The [marked-boundary calculation](spectral_boundary_modulus.md) now
constructs the concrete additive target \(J(\mathbf P^1,2\infty)\simeq
\mathbf G_a\), taking the spectral divisor minus \(m[0]\) to \(M_1\).
Depression is exactly its first-order trivialization at infinity.
What remains unconstructed is a map of **actual CI/Cartier relations**
into modulus-trivial relations, including conductor and exceptional terms;
the sufficient norm condition in that owner makes the missing input exact.
Ordinary
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
| [F-0001 Torus-supported boundaries](../../frameworks/torus-supported-boundaries/index.md) | Both full limits; sign-symmetric ACM vanishing for any numerator; nonzero moment forces non-ACM pure hulls with section-parity defects at both ends | A restriction from actual CI origin excluding those defects; invariant cycles alone do not impose ideal symmetry |
| [F-0002 Embedded torus quotients](../../frameworks/embedded-torus-quotients/index.md) | Exact constant embedded quotient, evaluation ranks, degree-exhaustion, endpoint algebras and moving quotient lower bounds | Constant quotient coverage for arbitrary moving nonreduced CI; an equality between endpoint ranks and \(M_1\) |
| [F-0003 Formal normal geometry](../../frameworks/formal-normal-geometry/index.md) | Curvilinear/entirely-thick split; conormal bounds force residual cohomology vanishing; actual source and first-jet residue pairing | A general isotropy or source-exhaustion theorem; fixed normal layers do not establish full support |
| [F-0004 Arithmetic supported lifts](../../frameworks/arithmetic-supported-lifts/index.md) | Char-2 and odd-prime explicit realizations, Frobenius collisions, finite-order nonlifting and endpoint specialization | Extension of a prescribed arithmetic obstruction to arbitrary characteristic-zero sources; \(p\mid m\) permits \(M_1(m[C])=0\) |
| [F-0005 Carrier normalization](../../frameworks/carrier-normalization/index.md) | Exact Cartier/Hodge/descent monoids; marked rational-line Jacobian gives the additive target and a sufficient norm relation | A CI-compatible modulus relation, with conductor/exceptional terms, especially on singular or non-Cartier generic branches |
| [F-0006 Global equation realization](../../frameworks/global-equation-realization/index.md) | Actual-source incidence; residual source-space identity; matrix differential and sign-symmetric ACM theorem; Hilbert-form interpretation | A source relation forcing isotropy on arbitrary non-invariant repeated ideals, or constraining the section defects of their invariant limits |
| [F-0007 Residual construction](../../frameworks/residual-construction/index.md) | Attachment and movement bounds; peeling one layer of every component gives exact linkage and new repeated-cycle classes | The layer-peeling residual is distinct from the off-support residual curve and its attachment quotient \(Q_1\); neither comparison proves universal positivity or absorption |
| [F-0008 Spectral roots](../../frameworks/spectral-roots/index.md) | Relative Picard torsion of a root divisor gives an exact graded second-relation criterion; actual octic and (6,16) tests | Identification of root Picard class with the \(q=u/v\) character, or ambient source/CI lift in the remaining strata |
| [F-0009 Local cohomology](../../frameworks/local-cohomology/index.md) | Exact coregularity test; finite section/Rao defect now has a necessary nonstandard-parity head class for nonzero moment on invariant pure curves | This finite Rao defect is not identified with the unrestricted STCI local-cohomology/coregularity obstruction; no general comparison map is supplied |

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

**B. Source and marked-divisor bridges are now more precise.** The
[Hilbert-form interpretation](chow_hilbert_symplectic_form.md) identifies
\(2M_1\) with a pulled-back symplectic form. Actual sign symmetry forces
its vanishing for [every ACM arrangement](chow_acm_parity_vanishing.md).
For invariant non-ACM pure curves, nonzero moment requires the
[specific section-parity defect](chow_section_parity_defect.md).
The rational-line generalized Jacobian supplies the additive divisor
target, but CI-compatible modulus reciprocity remains missing. Neither
bridge permits arbitrary repeated ideals to inherit symmetry from cycles.

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

## V. Bounded source questions and geometric alternatives

The [sole strategic queue](../../investigations/proof-audit/knowledge-gain-priorities.md#current-choice-and-reassessment)
compares actual next tasks. These are mechanism questions, not an additional
priority order. The [saturation and interpolation theorem](spectral_interpolation_and_polar_saturation.md)
removes the proposed independent opposite-polar cofactor gate: on a
coordinate-saturated ideal the opposite chains have equivalent membership.
The single full-chain/norm realization problem remains, with \((H,K)\)
recovering cycle parameters on the distinct-spectral-value stratum. The
determinant truncation theorem limits separate fixed-depth source arguments;
neither parameter recovery nor truncation supplies UM1.

A source-level question is to **pull back the mixed Chow coefficient
to the actual source incidence** for arbitrary degrees and express it
via the universal six-layer residue formula, retaining the condition
that the *entire* resultant lies in the translated-Chow product locus.
The sign-symmetry proof supplies a common mechanism for invariant CIs,
the explicit exceptional quartic pencils, and the displayed one-sided
non-eigenform cone-jet control. It does not cover every source in the
broader eigenform/one-sided theorems. The new bounded source question is
whether actual CI degeneration constrains the opposite-sign equal-degree
generators of the free section hull and their finite defect. Nonzero
moment forces such generators; the single quartic shows they are possible
without CI origin. A useful probe must retain that origin.

The independent geometric alternative is to test whether the
fixed-carrier mate lattice gives an additive, equivariant
\(q\)-functional on its realized divisor subgroup. The
exceptional carrier and the fixed toric quartic provide contrasting
normal and nonnormal models. One must verify that the proposed functional
respects **relations of actual Cartier divisors**; ordinary
intersection theory alone is too coarse.

Other alternatives are all-degree classification of
CI arrangements, complete Hilbert/Chow compactification, additional
sextic numerical tables, and new unrestricted fixed-depth normal
jet calculations. None currently has a specified bridge to UM1
stronger than the two above.

**Stop condition for this review:** the current proof corpus
now supplies new covered classes and a sharper non-ACM section-defect
boundary, but no universal vanishing after the trace/residue,
marked-divisor and global-source comparisons. The missing bridges remain
explicit; new claims require arguments and independent review. This
document is not a proof of UM1.
