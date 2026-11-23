# STCI Literature Ledger

Broad search assessed through 2026-09-30; selected primary-source mechanisms and inherited October 13 corrections rechecked/integrated on 2026-10-31. These are bounded checks, not a claim of exhaustive coverage. **No fresh external literature search was performed in the November 16, 2026 GitHub-only mathematical cleanup.** The references below retain their individual dated verification scopes; the ledger does not certify that no later solution has appeared.

This ledger records the scope actually used in the research report. A source is
not listed as settling more than its hypotheses permit. “No later resolution
found” is a documented search result, not a proof that no unindexed work exists.

The November 20, 2026 joint review of PRs #168 and #169 freshly checked
the primary sources cited below for Jordan type, embedded multiple curves,
conductor duality, common-factor blowups and actual-pair coregularity.
Murayama's April 2026 open-problem statements were also rechecked; the AMS
preview was inaccessible on this pass. This was a targeted comparison,
not an exhaustive new literature survey or a claim of originality.

The [affine/projective scope account](../arguments/equations/global_equations_and_constructions.md#affineprojective-scope-and-explicit-literature-counterchecks) retains the exact lci-cone criterion, tensor-quotient proof failure, real-sphere CI counterexample, fixed-quadric Picard control, SCIP distinction, and failed unique-prime inference. They have distinct field and quantifier scopes; none settles the projective algebraically closed STCI problem.

## Current status and general bounds

### Eisenbud--Harris, 2024

David Eisenbud and Joe Harris, *The Practice of Algebraic Curves: A Second
Course in Algebraic Geometry*, Graduate Studies in Mathematics 250, AMS, 2024,
Example 3.13 and Proposition 3.14.

- Official preview:
  <https://www.ams.org/bookstore/pspdf/gsm-250-prev.pdf>
- Verified scope: for
  \(C_0=[s^4:s^3t:st^3:t^4]\), the ideal needs four minimal generators and
  three equations suffice up to saturation; the text explicitly describes the
  question whether two forms generate its ideal up to radical as one of the
  famous open problems in curve theory.
- Consequence: because \(C_0\) is a smooth complex rational quartic, this is a
  direct 2024 witness that the universal smooth-complex statement was still
  open.

### Murayama, April 2026

Takumi Murayama, *MA665 Algebraic Geometry II*, compiled 28 April 2026, and
the companion local-cohomology notes.

- Course notes: <https://www.math.purdue.edu/~murayama/ma665.pdf>
- Local-cohomology notes:
  <https://www.math.purdue.edu/~murayama/LocalCohomology.pdf>
- Verified scope: Question 2.6.40 states the projective space-curve STCI
  question as open since Perron, and the later discussion retains the Macaulay
  rational quartic as open in characteristic zero/over \(\mathbf C\).  The
  companion notes explicitly record the positive-characteristic case as an
  STCI.  The displayed final coordinate in one occurrence appears to contain
  a typo, but the intended curve is clear.
- Together with the 2024 book and the dated searches recorded here, this is
  the most recent explicit checked source for the current open status.  It is
  still a literature-search conclusion, not proof of absence of an unindexed
  result.

### Hartshorne--Polini, 2019

Robin Hartshorne and Claudia Polini, “Quasi-cyclic modules and coregular
sequences,” arXiv:1907.05472.

- Source: <https://arxiv.org/abs/1907.05472>
- Verified scope: gives a local-cohomological characterization and necessary
  conditions; the abstract explicitly calls the question whether every
  connected curve in projective three-space is an STCI still open.
- Exact criterion (Theorem 3.1): for an **A-regular sequence** f_1,...,f_r in I, equality of radicals is equivalent to coregularity on H_I^r(A) and H_I^i(A)=0 for i>r. The standard graded convention requires homogeneous elements. For a connected space curve the relevant test concerns a homogeneous pair on H_I^2(S), not ordinary higher vanishing alone.
- Proposition 5.2 and Example 5.3(c) explicitly treat the fixed quartic: the smooth quadric and cuspidal cubic are individually coregular, but their pair retains a double line. Corollary 4.6 supplies graded quasi-cyclicity as a necessary condition. The [global equation account](../arguments/equations/global_equations_and_constructions.md#homogeneous-local-cohomology-and-the-second-equation) records the exact use.
- The proof of Theorem 3.1 uses the successive local-cohomology exact sequences. The [actual-pair interpretation](../arguments/local-cohomology/actual_pair_coregularity.md) retains their grading to identify the second cokernel with \(H_I^1(S/(f,g))(\deg f)\), under its explicit first-coregularity and vanishing hypotheses; this is not a new STCI criterion.

### Hassanzadeh, 2024--2025

S. Hamid Hassanzadeh, “Set-Theoretically Perfect Ideals and Residual
Intersections,” arXiv:2409.05705, revised 2025; published in *Journal of the London Mathematical Society* 111(3) (2025), e70108, DOI [10.1112/jlms.70108](https://doi.org/10.1112/jlms.70108).

- Source: <https://arxiv.org/abs/2409.05705>
- Verified scope: proves perfect subideals with the same radical for residual
  intersections under stated Serre hypotheses. It does not prove that every
  integral or smooth projective space curve has arithmetic rank two.

### Walther--Zhang, 2021 survey

Uli Walther and Wenliang Zhang, “Local cohomology—an invitation,”
arXiv:2106.09796, §4.1.1.

- Source: <https://arxiv.org/abs/2106.09796>
- Verified scope: explains that the homogeneous arithmetic rank of the
  Macaulay quartic in characteristic zero is unknown and that the immediate
  higher-local-cohomology obstruction vanishes.

### Kneser and Eisenbud--Evans

- Martin Kneser, “Über die Darstellung algebraischer Raumkurven als
  Durchschnitte von Flächen,” *Archiv der Mathematik* 11 (1960), 157--158.
- David Eisenbud and E. Graham Evans, “Every Algebraic Set in
  \(n\)-Space Is the Intersection of \(n\) Hypersurfaces,” *Inventiones
  Mathematicae* 19 (1973), 107--112.
- Verified consequence: every projective space curve is set-theoretically cut
  out by at most three hypersurfaces. Thus the unresolved dichotomy in
  \(\mathbf P^3\) is arithmetic rank two versus three, not an unbounded equation
  count.

### Arithmetically Cohen--Macaulay curves

A modern survey (D'Cruz, Theorem 2.7) states that arithmetically Cohen--Macaulay curves in \(\mathbf P^3\) are set-theoretic complete intersections and attributes this to Robbiano--Valla and Stückrad--Vogel. The broad original-proof scope has not been independently verified in this repository.

- Lorenzo Robbiano and Giuseppe Valla, “Some curves in \(\mathbf P^3\) are
  set-theoretic complete intersections,” LNM 997 (1983), 391--399:
  <https://doi.org/10.1007/BFb0061654>
- Exact checked primary scope: the [official chapter preview](https://page-one.springer.com/pdf/preview/10.1007/BFb0061654), printed pp.391–392, identifies §2 and Corollary2.3 as the positive result for **ACM monomial** space curves in every characteristic. This does not establish an arbitrary-ACM theorem. D'Cruz's [Theorem2.7](https://arxiv.org/html/2003.09101v1) states the broader assertion and also cites Stückrad–Vogel, *On the number of equations defining an algebraic set of zeros in n-space*, Teubner-Texte48 (1982), pp.88–107; that original text was inaccessible in the bounded audit. [Thoma1993](https://archive.mpim-bonn.mpg.de/948/1/preprint_1993_86.pdf), introduction p.2, likewise mentions ACM curves broadly inside a monomial discussion. The broad assertion remains a source-coverage gap, not a refuted theorem or independently reconstructed proof.

- Relevance: smooth rational quartics are not linearly normal and hence not
  ACM, so this broad positive theorem stops exactly before the smallest open
  smooth case.

## Artinian Jordan type and the quadratic conductor

Anthony Iarrobino, Pedro Macias Marques and Chris McDaniel,
*Artinian algebras and Jordan type*, [arXiv:1802.07383](https://arxiv.org/pdf/1802.07383),
version 6 (August 31, 2022), Theorem 2.5, Proposition 2.10 and Lemma 2.15.

The November 20, 2026 proof review checked the Jordan-type bound by the
conjugate Hilbert function, the equality for a strong Lefschetz element,
and the characteristic-zero height-two graded Artinian Lefschetz result.
The [moving-conductor proof](../arguments/linkage/moving_quadratic_covers.md#four-general-points-and-the-maximum-length)
uses these on the graded transverse algebra, then separately verifies that
actual quadric lifts reach the required directions. The source alone does
not establish global realization, conductor lengths or an STCI obstruction.
Only its characteristic-zero Lefschetz assertion is used here.
A direct earlier proof of that graded assertion is Harima--Migliore--Nagel--Watanabe,
[Proposition 4.4, p. 22](https://arxiv.org/pdf/math/0208201).

### Eisenbud--Ulrich conductor regularity

David Eisenbud and Bernd Ulrich, *The Regularity of the Conductor*,
[arXiv:1302.5752](https://arxiv.org/pdf/1302.5752), Theorem 3.1,
p. 3; proof pp. 6--7. Their regularity formula concerns a reduced projective scheme
with Gorenstein coordinate ring and a finite graded Cohen--Macaulay
intermediate algebra in its normalization. It illustrates the same
canonical-module mechanism, but does not subsume the possibly nonreduced,
non-ACM separated branch used here. Our
[conditional ACM refinement](../arguments/linkage/moving_quadratic_covers.md#the-boundary-of-the-actual-intersection)
comes directly from the existing conductor dual sequence.
Finite-map duality itself does not require reducedness; compare
[Stacks, Lemma 47.15.8](https://stacks.math.columbia.edu/tag/0AX0).

## Affine lci theorems and the projective gap

### Forster's affine-space theorem

Otto Forster, “Complete Intersections in Affine Algebraic Varieties and Stein
Spaces,” LNM 1092 (1984), 1--28.

- Author PDF:
  <https://www.mathematik.uni-muenchen.de/~forster/eprints/Compl_inter.pdf>
- Verified scope: Theorem 5.1 treats lci subschemes of affine space with
  trivial conormal bundle; Theorem 5.2 states that every lci curve in affine
  space is a set-theoretic complete intersection.  The proof packages the
  Ferrand double and affine vector-bundle input, attributing the three-space
  case to Szpiro and the higher-dimensional case to Mohan Kumar.
- This is the correct strong affine comparison for a smooth projective space
  curve.  It gives equations after deleting a hyperplane, but it provides
  neither relatively-prime leading forms nor a splitting of the corresponding
  projective bundle.  P-007 makes that boundary failure exact.

### Ferrand--Szpiro

- Daniel Ferrand, “Courbes gauches et fibrés de rang deux,”
  *C. R. Acad. Sci. Paris* 281 (1975), 345--347.
- Lucien Szpiro, *Lectures on Equations Defining Space Curves*, Tata Institute
  of Fundamental Research Lectures on Mathematics and Physics 62,
  Springer/TIFR, 1979.
- TIFR text:
  <https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr62.pdf>
- Verified scope:
  1. an lci curve in affine three-space is a set-theoretic complete
     intersection;
  2. a projective lci curve supports a double structure obtained as the zero
     scheme of a section of a rank-two vector bundle.
- The missing projective step is bundle splitting. On affine space,
  Quillen--Suslin makes the bundle free. On \(\mathbf P^3\), the Ferrand bundle
  may be indecomposable, whereas two global equations require
  \(\mathcal O(a)\oplus\mathcal O(b)\).

### Mandal--Zinna, published 2026

Lisa Mandal and Md. Ali Zinna, “Set-theoretic complete intersection for curves
in affine three-folds,” *Journal of Algebra* 690 (2026), 101--113,
DOI 10.1016/j.jalgebra.2025.10.042.

- Publisher page:
  <https://www.sciencedirect.com/science/article/abs/pii/S0021869325006295>
- Verified published theorem: over a three-dimensional affine algebra over a
  \(C_1\)-field of characteristic zero, an lci height-two ideal with free
  conormal module and torsion Grothendieck-group class is an STCI; a ring-level
  variant assumes every stably free rank-three module is free.
- It is an affine, conditional theorem. It neither controls the hyperplane at
  infinity nor splits a projective Ferrand bundle.

### Mandal--Zinna, 2025 preprint: claim with invalid displayed proof

Lisa Mandal and Md. Ali Zinna, “On set-theoretic complete intersections for smooth curves in three-dimensional affine schemes,” [arXiv:2511.07589v1](https://arxiv.org/html/2511.07589v1), submitted 10 November 2025. The inspected record still exposes v1; an unchanged abstract is not a repaired proof.

The abstract claims arbitrary dimension-three Noetherian affine lci curves are STCI, with a four-dimensional finite-field-closure analogue. The stated proof does not justify these broad claims. In Theorem 4.2 Step 3, the displayed splitting substitutes J/(c) for the tensor quotient J/cJ. The exact audit is elementary: in A=k[x,y,z], take J=(x,y), c=x and the resolution t↦(−yt,xt), (a,b)↦ax+by. Over B=A/(x), the proposed last term J/(x) produces middle kernel B(1,0), preceding image yB(1,0), and nonzero homology B/(y). If the notation means J/xJ instead, the nonzero class of x is killed by y, refuting rank-one local freeness. Neither reading repairs the step.

The [existing exact proof audit and real-sphere counterexample](../arguments/equations/global_equations_and_constructions.md#exact-audit-of-arxiv251107589v1-step-3) retain the full reasoning. The real example refutes the arbitrary-Noetherian-ring CI assertion; it does not refute every field-restricted STCI claim or furnish a projective algebraically closed counterexample. Keep these failed broad arguments distinct from the narrower published conditional theorems.

### Additional affine papers: verified scope versus discovery lead

- Mandal–Zinna, *Set-theoretic complete intersection for smooth surfaces in a smooth affine algebra*, J. Algebra 693 (2026), 36–53, [publisher](https://www.sciencedirect.com/science/article/abs/pii/S0021869326000165), DOI 10.1016/j.jalgebra.2025.12.026: the inherited primary-abstract check retains the smooth affine Fpbar ambient, trivial conormal and torsion Grothendieck-class hypotheses. Missing rendered dimensions were not inferred.
- Lisa Mandal, *Set theoretic complete intersection of ideals in a Laurent polynomial ring*, Communications in Algebra 54(11) (2026), 3565–3573, [publisher](https://www.tandfonline.com/doi/abs/10.1080/00927872.2025.2604611): the inherited publisher-abstract check requires a dimension-n affine Fpbar algebra, n≥3, an lci height-n ideal in A[T,T^-1], free conormal and torsion Grothendieck class. It does not close the projective gap.
- **Discovery lead only:** Mandal–Zinna, *On the minimal number of generators of local complete intersection ideals in affine four-folds*, J. Pure Appl. Algebra 230(11) (2026), 108384, [DOI](https://doi.org/10.1016/j.jpaa.2026.108384). The inherited October 13 search recovered metadata but not primary theorem/proof text. No theorem from it is relied upon here.

### A failed negative-resolution claim

Erdoğdu, [*Radically finite rings and space curves*, arXiv:2209.04489](https://arxiv.org/abs/2209.04489), cannot be used as a resolution. The [existing exact countercheck](../arguments/equations/global_equations_and_constructions.md#the-failed-unique-prime-inference-in-arxiv220904489v1) isolates the proof's inference from a unique maximal ideal to a unique prime. In R=k[x,y]_(x,y), A=R[T], g=y+(1−y)T, the prime (x,g) has quotient k[y]_(y) and is strictly smaller than the unique maximal ideal (x,y,T) above it. This is an audit of that inference, not a projective counterexample.

## Chow forms and global determinant representations

### Eisenbud--Schreyer

David Eisenbud and Frank-Olaf Schreyer, “Resultants and Chow Forms via
Exterior Syzygies,” arXiv:math/0111040 (2001).

- Source: <https://arxiv.org/abs/math/0111040>
- Directly checked scope: the source defines Chow complexes on Grassmannians
  and states that the Chow form of the associated cycle is the determinant of
  the corresponding Chow complex.
- Use here: for two forms on the universal line, the twisted pushed-forward
  Koszul complex is the square Sylvester bundle map, whose determinant is the
  binary resultant and hence the Chow form of the complete-intersection cycle.
  The pure-power criterion in P-033 is the resulting specialized corollary, under the no-common-factor/proper-CI hypothesis. Purity makes its top-dimensional-cycle identity a sole-support test; an arbitrary nonpure scheme can carry additional lower-dimensional support invisible to its Chow form.
- Scope qualification: this is a classical cycle-level reformulation and
  computational certificate. It neither constructs a defining pair nor proves
  that one exists for any unresolved curve.

### Common-factor degenerations and excess intersection

Robert Lazarsfeld, *Excess intersection of divisors*, Compositio
Mathematica 43 (1981), 281--296,
[Lemma 1.1, p. 287](https://www.math.stonybrook.edu/robert.lazarsfeld/Reprints/Lazarsfeld.Excess.Intersection.Divisors.pdf),
describes first-order limiting cycles for a dense open of tangent
directions; exceptional directions can depend on higher terms. Its setup
uses a smooth projective \(n\)-fold, \(n\) divisors and basepoint-free
systems. It provides excess-intersection context, not a verbatim theorem
for constrained positive-dimensional intersections through this curve.
The [common-quadric proof](../arguments/equations/common_quadric_chow_boundary.md)
instead uses an explicit colon sequence and Koszul calculation, and the
[local blowup proof](../arguments/equations/common_quadric_resultant_blowup.md)
controls all normal directions on its injective-cancellation open,
including the stated common-ruling factors.

Olivier Benoist, *The resultant divisor is negative* (2026),
[Theorem 3.1 and §3.2](https://arxiv.org/pdf/2601.11474), gives a
global tower of gcd-stratum blowups for **binary** forms of degrees
\(1\le d<e\). Proposition 3.3(ii), equation (3.4), identifies its
normal cancellation map \((F,G)\mapsto BG-CF\); Theorem 4.11 identifies
the tower with the corresponding multigraded Hilbert scheme. This paper
supersedes arXiv:1212.4862. Its §1.6 leaves higher-dimensional analogues
as questions. The binary theorem is a close classical comparison, but
does not give the constrained \(\mathbf P^3\) coefficient ideal
\(J^2\) across all lines. That assertion and its ruling-dependent
failure retain the direct residual-source and secant proof above.

## Conductor descent and codimension-two Gorenstein criteria

### Grothendieck--Lefschetz for the covering quadric

SGA 2, [Exposé XII, Corollary 3.7](https://arxiv.org/pdf/math/0511279),
gives \(\operatorname{Pic}(X)=\mathbf Z[\mathcal O_X(1)]\) for a projective
complete intersection of dimension at least three. It applies to the smooth
quadric threefold used in the
[split norm factorization](../arguments/linkage/split_carrier_norm_and_conductor.md#split-carrier-the-conductor-is-an-actual-complete-intersection).
This is the Picard-group input for the even-degree factorization; a paper
on normal surfaces does not supply that citation.

### Morrison's local conormal comparison

D. R. Morrison, [The Birational Geometry of Surfaces with Rational Double Points](https://web.math.ucsb.edu/~drm/papers/birgeoRDP.pdf),
*Math. Ann.* 271 (1985), 415--438, Theorem 3.1 (p. 424) and Table 2.2
(p. 421). The theorem compares the conormal sheaf of a smooth Weil curve
with that of its strict transform at rational double points. In a smooth
threefold, the local presentation \(k[[t]]^2/k[[t]](a,b)\) identifies its
torsion length with \(\min(\operatorname{ord}a,\operatorname{ord}b)\), the
common derivative-zero order in the
[one-lift sextic proof](../arguments/linkage/one_lift_sextic_conormal_exclusion.md#the-same-length-budget-controls-all-du-val-types).
The table gives value three at the admissible \(E_7\) vertex, stronger
than the lower bound two sufficient for that proof. Theorem 3.1 is local
near the curve; Theorem 3.2 has a stronger ambient canonical-bundle
hypothesis and is not being applied to the quadric threefold.

### Cohen–Macaulay purity and symbolic layers

For the [symbolic Cartier-layer argument](../arguments/linkage/signed_cubic_normalization_and_cartier_defect.md#the-cartier-defect-restriction-in-signed-degree-m),
[Stacks, §10.103, Lemmas 10.103.5 and 10.103.7](https://stacks.math.columbia.edu/tag/00N2)
supply the standard purity input: quotienting a Cohen–Macaulay local
ring by a nonzerodivisor preserves Cohen–Macaulayness in one lower
dimension, and the quotient has no embedded associated primes. With
the actual mate's sole support, its ideal is therefore primary at the
marked curve. This replaces normal-surface divisor theory in that
specific proof; it does not remove normality from unrelated results.

### Ferrand

Daniel Ferrand, “Conducteur, descente et pincement,” *Bulletin de la Société
Mathématique de France* 131 (2003), no. 4, 553--585.

- Source: <https://www.numdam.org/item/BSMF_2003__131_4_553_0/>.
- Verified use: the conductor square and its fiber-product exact sequence are
  the classical descent mechanism used in P-032.  The full, possibly
  nonreduced conductor schemes are required; normalized divisor support alone
  does not imply descent.

### Serre and Burch

- Jean-Pierre Serre, “Sur les modules projectifs,” *Séminaire Dubreil. Algèbre
  et théorie des nombres* 14 (1960--1961), exposé 2:
  <https://numdam.org/item/SD_1960-1961__14_1_A2_0/>.
- Lindsay Burch, “On ideals of finite homological dimension in local rings,”
  *Mathematical Proceedings of the Cambridge Philosophical Society* 64
  (1968), 941--948:
  <https://doi.org/10.1017/S0305004100043620>.
- Verified use: in codimension two, the Hilbert--Burch resolution of a perfect
  ideal has last rank one exactly when the ideal has two minimal generators.
  Consequently a height-two graded Gorenstein ideal is a complete
  intersection.  This makes P-035 a classical equivalence; “arithmetically
  Gorenstein,” not merely locally Gorenstein, is essential.

**Bănică--Forster's classical local triple.** In §3 of [*Multiplicity Structures on Space Curves*](https://www.mathematik.uni-muenchen.de/~forster/eprints/multip_struct.pdf), the local quasiprimitive triple has ideal \((t^d x-y^2,xy,x^2)\). This is existing theory. The [BF triple and actual-pair attachment TR1--TR4](../arguments/residuals/residual_capacity_and_constructions.md#triples-the-full-attachment-has-only-two-independent-divisors) uses its Hilbert--Burch syzygies to identify the actual full-primary conormal-torsion divisor with \(D_2\), then combines this with the previously recorded liaison duality and attachment-module determinant to express the whole three-layer attachment filtration through two effective divisors. Do not attribute the local form to this project or extend the two-divisor identity to arbitrary multiplicity. Independent review of the cross-module linkage remains pending.

**Fourth-order scope and source check.**
In the original 1986 Bănică--Forster
§3.9, p. 61, the lci quasiprimitive
quadruple with \(D_2=D_3=d[P]\)
has local ideal \((t^d x-y^2,x^2)\).
It has nonzero multiplication defects
but a torsion-free rank-two
conormal equation module. This
[TR5--TR6 counterexample](../arguments/residuals/residual_capacity_and_constructions.md#a-classical-fourth-order-counterexample-to-extrapolating-tr2)
rules out extending the triple
torsion identity to all
multiplicities. Moreover the
[original 1986 scan](https://sites.lsa.umich.edu/idolga-new/wp-content/uploads/sites/1467/2024/08/coxeter86.pdf)
prints \(y(t^dx-y^2)\) in the
other, non-lci quadruple ideal,
while a re-typeset PDF gives
\(y(t^d-y^2)\), omitting \(x\).
Use the original formula in
subsequent calculations; the
transcription variant cannot
have the announced generic
multiplicity.

## Contact geometry and Legendrian curves on quadrics

Nikita Kalinin, [*Legendrian curves in CP3: cubics and curves on a quadric surface*](https://arxiv.org/abs/1607.07486), *Zapiski Nauchnykh Seminarov POMI* 476 (2018), 92–110, [published paper](https://ftp.pdmi.ras.ru/pub/publicat/znsl/v476/p092.pdf), **Theorem 4.3** (Theorem 13 in the arXiv numbering).
The theorem classifies algebraic Legendrian curves on smooth quadrics
in complex projective three-space using the characteristic foliation
of the restricted contact structure. This is the established general
classification, not a new result of the STCI project. In the
[marked Segre graph comparison](../arguments/torus/quadric_pencil_spectral_intrinsic_geometry.md),
the special contact forms
\(\omega_q=dx_0\wedge dx_3-(2/q)dx_1\wedge dx_2\) select precisely the
graphs \([s^3:u t^3]\) inside \(Q_q\), while their spectral trace
still lacks a universal complete-intersection vanishing theorem.
The [existing Hamiltonian/Jacobian theorem](../arguments/torus/contact_jacobians_and_hamiltonian_actions.md#the-six-ambient-minors-different-and-contact-identity)
proves an actual Poisson-involutivity statement under **sole support**;
neither the published Legendrian classification nor that theorem
proves the unrestricted moment relation on multicomponent cycles.

## Multiple structures, bundles, and liaison

### Eisenbud--Van de Ven

David Eisenbud and A. Van de Ven, “On the Normal Bundles of Smooth Rational
Space Curves,” *Mathematische Annalen* 256 (1981), 453--463.

- Author PDF: <https://eisenbud.github.io/papers/pdfs/1981-001.pdf>
- Verified scope: over an algebraically closed field of characteristic zero,
  every smooth rational quartic has balanced normal bundle
  \(N_C\simeq\mathcal O_{\mathbf P^1}(7)^2\); more generally their Proposition
  6 gives \(N_C\simeq\mathcal O(2n-1)^2\) for a smooth rational degree-\(n>3\)
  curve on a smooth quadric.  This supplies the family-level normal-bundle
  input in P-010, rather than extrapolating from the explicit computation for
  \(C_0\).

### Bănică--Forster

Constantin Bănică and Otto Forster, “Multiplicity Structures on Space Curves,”
in *The Lefschetz Centennial Conference, Part I*, Contemporary Mathematics 58,
AMS, 1986.

- Author reprint:
  <https://www.mathematik.uni-muenchen.de/~forster/eprints/multip_struct.pdf>
- Verified scope: classifies primitive multiple structures through conormal
  quotients and extension data. Proposition 2.4 supplies the splitting
  obstruction used in P-010.
- Textual caveat used in P-038: the available typeset reprint's §3.9(ii)
  displays the second local generator as (y(t^d-y^2)), dropping the (x)
  from (y(t^dx-y^2)).  The literal printed ideal is not flat and is
  generically multiplicity one; the corrected expression is forced by the
  preceding extension construction and restores the stated length-four
  fibers.  P-038 records and checks the corrected local algebra rather than
  silently quoting the typo.

### Embedded multiple curves and the osculating quotient

The November 20, 2026 primary-source review checked Bănică--Forster's
[author reprint](https://www.mathematik.uni-muenchen.de/~forster/eprints/multip_struct.pdf),
Proposition 2.4 and following remark (reprint pp. 6--8), for fixed-ambient
primitive extensions via splitting the restricted conormal extension.
Proposition 3.7 and §3.8 (pp. 11--12) give quasiprimitive extensions as
epimorphisms compatible with the prescribed multiplication section and
their open parameter locus. Section 3.9 (pp. 12--13) gives the triple
normal form \((t^d x-y^2,xy,x^2)\); the separate length-four typo
noted above is not used for this triple calculation.

These mechanisms are classical. The
[fixed-quotient computation](../arguments/normal-geometry/osculating_ribbon_obstruction.md)
supplies the particular class \(2[u^{-2}]\), splitting
\(\mathcal E=\mathcal O(-10)^2\), and complete defect-divisor
classification. It is not presented as a new general extension theorem.
The original treatment is mainly complex analytic (§0.1); the needed
ideal/module construction is reconstructed algebraically here before its
odd-characteristic extension is used.

Jean-Marc Drézet, *Paramétrisation des courbes multiples primitives*,
[Proposition 5.1.1(4), printed p. 32](https://webusers.imj-prg.fr/~jean-marc.drezet/papers/param.pdf),
proves that every **abstract** primitive multiple curve extends to the
next multiplicity. This does not preserve a chosen embedding in
\(\mathbf P^3\) or its fixed conormal quotient, and therefore does
not contradict the embedded osculating obstruction.

### Boratyński and Manolache

- M. Boratyński, “Locally complete intersection multiple structures on smooth
  algebraic curves,” *Proceedings of the AMS* 115 (1992), 877--879,
  DOI <https://doi.org/10.1090/S0002-9939-1992-1120504-1>.
- Nicolae Manolache, “Multiple Structures on Smooth Support,” *Mathematische
  Nachrichten* 167 (1994), 157--202,
  DOI <https://doi.org/10.1002/mana.19941670108>.
- Nicolae Manolache, “Gorenstein Multiple Structures on Smooth Algebraic
  Varieties,” arXiv:0706.2204:
  <https://arxiv.org/abs/0706.2204>.
- Verified use: Boratyński's theorem says that a quasiprimitive multiple curve
  with Bănică--Forster graded pieces \(E_i\) is lci precisely when the
  multiplication pairings \(E_i\otimes E_{t-i}\to E_t\) are isomorphisms.
  In multiplicities four and five this gives the graded shapes
  \((L,D,D)\) and \((L,D,2D,2D)\), respectively.  Manolache supplies the
  broader filtration and Gorenstein-duality framework.  These are the checked
  structural inputs to P-016; none of these sources eliminates the two
  rational-quartic \((4,5)\) types by itself.

### Ellia

Philippe Ellia, “Complete intersections primitive structures on space curves,”
*International Journal of Mathematics* 26 (2015), 1550104.

- Source: <https://arxiv.org/abs/1409.3801>
- Verified scope: derives numerical restrictions on complete-intersection
  primitive structures. For a smooth rational quartic it leaves a finite list
  of primitive numerical types, but explicitly does not produce a curve that
  cannot be an STCI by arbitrary multiple structures.
- After excluding the cubic case, the ten remaining rational-quartic primitive
  degree pairs recorded there are
  \[
  (4,7),(6,26),(12,18),(10,28),(9,48),(22,50),(20,67),
  (19,84),(18,118),(17,220).
  \]

**Further exact application of Ellia, not a new theorem.**
[Theorem 12](https://arxiv.org/abs/1409.3801)
proves that for a **primitive**
multiple curve \(X\) cut
scheme-theoretically by degrees
\((a,b)\), a general degree-\(b\)
surface containing \(X\) is
normal and has *uniform*
marked \(A_n^k\) singularities
along the smooth support,
as well as being smooth
outside it. [Theorem 15 and
Corollary 16](https://arxiv.org/abs/1409.3801)
then give the ten rational-quartic
primitive candidate pairs in the
preceding list. This is
considerably stronger than
generic Bertini **within the
primitive setting**.

The [all-degree normal replacement theorem](../arguments/carriers/normal_carrier_divisor_geometry.md#47-unequal-degree-pairs-can-acquire-an-actual-normal-carrier) uses classical characteristic-zero Bertini smoothness ([Kleiman 1997, Theorem 4.1](https://arxiv.org/abs/alg-geom/9704018)), Serre's criterion and hypersurface connectedness. Neither a non-pencil hypothesis nor prior integrality is required. It allows nonprimitive special points and equal or unequal degrees. This is a direct application of classical theory, not a new foundational Bertini result. Ellia's primitive theorem is stronger within its hypotheses. Simple first-symbol roots give the standard marked \(A_{r-1}\) germs of Ellia's Definition 8 and Lemma 10; the [reduced-gcd argument](../arguments/carriers/normal_carrier_divisor_geometry.md#reduced-common-first-normal-divisor-a-uniform-marked-ade-and-rank-test) uses this local geometry outside the everywhere-primitive case, combining it with the actual CI defect budget. The generalization is pending independent review.

The complete quartic exclusion removes \((4,7)\) from the ten eligible primitive pairs. Thus **outside the remaining nine pairs**, a hypothetical CI has a common singular point on \(C_0\). In the generically curvilinear branch this means a nonempty finite nonprimitive locus; if both generators have higher generic order then nonprimitivity is already generic. No primitive existence is claimed within the nine pairs, and the unrestricted common-singular assertion remains open.

### Franco--Kleiman--Lascu

Daniele Franco, Steven Kleiman, and Alexandru Lascu, “Gherardelli linkage and
complete intersections,” *Michigan Mathematical Journal* 48 (2000), 271--279.

- Source: <https://arxiv.org/abs/math/0003075>
- Verified scope: in characteristic zero, a pure Cohen--Macaulay codimension-two
  subscheme is a complete intersection under the corresponding subcanonical
  and self-linkage criterion. This is useful for recognizing a multiple
  structure once constructed; it does not construct one on every support.

### Saturated attachment and finite primary images

The Bănică--Forster and Manolache filtration and Gorenstein duality inputs, together with ordinary liaison and the Benguş-Lasnier--Rangachev discrepancy/genus formula, supply the ingredients of the [layerwise attachment comparison](../arguments/residuals/residual_capacity_and_constructions.md#layerwise-attachment-duality-on-a-non-gorenstein-primary-component); the local canonical-ideal application retains individual layers rather than only total length. The [actual-pair local-cohomology application](../arguments/local-cohomology/actual_pair_coregularity.md#actual-attachment-equation-modules-are-the-dual-annihilator-layers) uses Grothendieck local duality after liaison and retains Hartshorne--Polini's first-coregularity hypothesis. Numerical-semigroup binomial interpolation in the [toric primary lattice](../arguments/torus/fixed_carrier_chow_arrangements.md#all-order-primary-structure-and-attachment-on-the-classified-carrier) is related to Yasuda's higher Nash blowup jet matrices and Chávez-Martínez--Duarte--Giles Flores; no identification with a higher Nash blowup is asserted. Exact references and hypotheses are at the proof owners. These are applications and refinements, not priority claims.

## Carrier surfaces, divisor classes, and blowups

### Sharp complete-intersection Picard input (2024)

Česnavičius–Scholze, [*Purity for flat cohomology*](https://annals.math.princeton.edu/2024/199-1/p02), Annals 199 (2024), 51–180, Corollary 7.2.3 ([preprint](https://arxiv.org/abs/1912.10932)), prove that `Pic(X)/Z[O_X(1)]` is torsion-free for a projective complete intersection of dimension at least two over any field. Cotner–Zavyalov, [*Lefschetz theorems in flat cohomology and applications*](https://www.cambridge.org/core/journals/compositio-mathematica/article/lefschetz-theorems-in-flat-cohomology-and-applications/8556201EDB51D7F2F76F5950A800CD64), Theorem 1.1.8, give torsion-free Picard group, nondivisibility of the hyperplane class, and trivial numerically trivial Picard scheme. This includes singular hypersurfaces, in arbitrary characteristic. Hartshorne--Polini (2015), Lemma 7.6, had already proved hyperplane saturation for surfaces in P3 in characteristic zero, without normality; the recent result is its arbitrary-characteristic extension. Together with their Proposition 2.2(c) and Proposition 7.1 it yields the [normalized Hodge and downstairs almost-Cartier criterion](../arguments/carriers/fixed_carrier_descent_and_cartier_models.md#the-normalized-hodge-matrix-and-downstairs-almost-cartier-indices) and separates the upstairs Cartier index from the true downstairs minimum multiplicity. The numerical detection argument also extends their Theorem 4.5 (Picard pullback injectivity over C) to arbitrary characteristic for integral hypersurfaces. These are new applications, not newly discovered characteristic-zero Picard results. It strengthens our [fixed-carrier exact-index theorem](../arguments/carriers/normal_carrier_divisor_geometry.md#3-exact-exponent-and-minimal-mate-once-the-boundary-is-reached): under existence of a mate, the least Cartier multiple RC already lies on the integral hyperplane ray, hence the least mate multiplicity is R and the least mate degree is eR/a. The Hodge equality criterion on a normal Q-Cartier carrier also extends independently of characteristic. These statements do not imply torsion-free Weil class groups or arbitrary-characteristic Bertini or local socle formulas. The new application awaits independent review.

### Brevik--Nollet, October 2026: very general thick carriers

John Brevik and Scott Nollet, *Noether--Lefschetz theory and surfaces
containing a multiple curve*, *Nagoya Mathematical Journal* 261 (2026),
e54, published online October 19, 2026, [publisher primary source](https://doi.org/10.1017/nmj.2026.10139).

**Theorem 1.1, exact hypotheses.** Let (X\subset\mathbf P^N_{\mathbf C})
be a smooth projective threefold with (H^1(X,\mathcal O_X)=0), let
(C\subseteq X) be a smooth connected curve, (m\ge2), and let
(Z=C^{(m)}\) be the *ordinary infinitesimal neighborhood* defined by
(\mathcal I_Z=\mathcal I_C^m). For sufficiently large (d) and a
**very general** degree-(d) hypersurface section (Y) containing
(Z), restriction (\operatorname{Pic}(X)\to\operatorname{Pic}(Y))
is an isomorphism. For (X=\mathbf P^3), the Picard group of that
very general thick carrier is generated by (\mathcal O_Y(1)).
The paper explicitly treats nonnormal surfaces and also considers
other thick complete-intersection base loci with different Picard behavior.

**Implication for our entirely-thick regime.** This is a strong
very-general carrier theorem, directly relevant when both defining
equations vanish to order at least two on the rational quartic. It
does **not** cover the special surface selected by a hypothetical
actual mate, or classify its Weil/almost-Cartier curve class. The
curve need not define an invertible divisor on the generically
singular carrier. Hence the theorem neither excludes arbitrary
entirely-thick mates nor forces the first transverse trace
(M_1=\sum n_i u_i/v_i) to vanish. Any application must
first prove a suitable genericity/semicontinuity or actual
divisor-descent bridge, not merely invoke Picard rank one.


For quintic carriers, Andreatta–Sommese's sectional-genus classification
describes polarized surfaces. The fixed quartic and its projection center
require additional data. The repository's marked toric classification and
inverse-image calculation supply those data and exclude every mate on
an integral quintic with toric normalization. [External hypotheses and their application](../arguments/carriers/quintic_non_gorenstein_toric_sources.md#1-why-this-source-remains-relevant) ·
[Repository theorem](../results/toric_quintic_carrier_exclusion.md)

**Ample divisors on the graph.** Cotner–Zavyalov, Theorem 3.2.2 (same reference), gives the low-degree finite-coefficient Lefschetz comparison for an ample Cartier surface in a smooth proper threefold with affine complement. In characteristic zero the Kummer sequence implies saturation of the ambient Picard restriction when the ambient Picard group is torsion-free; normality of the surface is unnecessary. The [strict-carrier compression LC1–LC4](../arguments/residuals/blowup_residual_geometry.md#lefschetz-compression-on-ample-strict-carriers) uses this established theorem on the blowup, where the Picard group has rank two, plus an explicit graph cohomology vanishing to lift the compressed Cartier divisor to an actual homogeneous mate. This is an application of Lefschetz, not an assertion that the ample surface's entire Picard group comes from the blowup. Pending independent review.

### K3 ADE saturation and the Fano-side carrier

Garbagnati--Penegini--Perego, [*Singular symplectic surfaces* (2026), §4.2.1, Lemma 4.10 and Proposition 4.11](https://link.springer.com/article/10.1007/s13366-026-00838-w), classify divisible exceptional ADE classes on K3 surfaces, with individual orders bounded by eight, building on Nikulin and the torus quotient classifications. Thus for a normal K3 carrier any finite-order Weil class has order at most eight, via the Picard group of its resolution modulo the exceptional lattice. The [carrier application](../arguments/carriers/normal_carrier_symbolic_torsion.md#a-uniform-torsion-bound-on-normal-k3-carriers) identifies the actual primitive ray \(\mu\Delta-vH\) and bounds local indices; on \(|2M|\) in \(V_5\) this gives \(R\le16\) and a mate in degree at most eight on \(V_5\). Prescribed conic vanishing is separate. This is an application of existing classification, not a newly proved bound for K3 divisible classes. The [marked ADE obstruction on the primitive graph row](../arguments/residuals/blowup_residual_geometry.md#a-k3-marked-lattice-obstruction-to-the-primitive-graph-row) instead uses the classical K3 signature and local even ADE discriminant forms together with a new pointwise finite-thickening transfer. A smoothing of the actual anticanonical carrier bounds the marked ADE ranks even if singularities away from the curve are worse. Independent review of these applications is pending.

### Brevik--Nollet, 2026: Noether--Lefschetz with a thick base curve

John Brevik and Scott Nollet,
[*Noether–Lefschetz theory and surfaces containing a multiple curve*](https://www.cambridge.org/core/journals/nagoya-mathematical-journal/article/noetherlefschetz-theory-and-surfaces-containing-a-multiple-curve/7C89E45108F00A35D058DFF899040964),
*Nagoya Mathematical Journal* 261 (2026), e54
(published online **19 October 2026**),
Theorem 3.9; compare the earlier
[*Noether–Lefschetz theorem with base locus*](https://arxiv.org/abs/0806.1243).

**Exact hypotheses and application.**
The 2026 theorem considers the ordinary
\(m\)-th infinitesimal neighborhood
\(C^{(m)}=V(\mathcal I_C^m)\), \(m\ge2\),
of a smooth connected curve in a regular
complex projective threefold. If
\(\mathcal I_C(\lfloor d/m\rfloor-1)\)
is globally generated and
\(H^0(\mathcal I_C^{m-1}(K_X+dH))\ne0\),
then for a **very general** degree-\(d\)
surface \(Y\) containing \(C^{(m)}\)
the map \(\operatorname{Pic}X\to\operatorname{Pic}Y\)
is an isomorphism.

For our **fixed non-linearly-normal**
rational quartic \(C_0\subset\mathbf P^3\),
the ideal \(\mathcal I_{C_0}\) is
**3-regular**, since its quadratic
restriction is surjective and the higher
cohomology required by regularity vanishes;
therefore \(\mathcal I_{C_0}(3)\)
is globally generated. Its unique
quadric \(q\) gives
\(q^{m-1}\in H^0(\mathcal I_C^{m-1}(2m-2))\).
Thus **Theorem 3.9**, not the paper's
complete-intersection Corollary 4.1,
applies whenever
\[
 \boxed{d\ge4m, \qquad
 \operatorname{Pic}(Y)\cong\mathbb Z[O_Y(1)]
 \quad\text{for very general }
 Y\supset C_0^{(m)}.}                \tag{NL}
\]
The stated \(d\ge4m\) is a sufficient
bound from the theorem, **not claimed
optimal**. At \(m=2\) it starts at
\(d=8\), so the important thick-sextic
degree-six case is **not** covered.

**Limits for STCI.** These \(Y\)
are generically singular along \(C_0\)
and nonnormal. The theorem controls
\(\operatorname{Pic}Y\), not the
normalization conductor, the appropriate
almost-Cartier divisor group or the
actual homogeneous mate equations.
In particular \(\operatorname{Pic}Y
=\mathbb Z H\) does **not**
exclude a supported Cartier divisor
cut by a hypothetical mate:
such a divisor already has class \(bH\).
A very-general Picard theorem also
does **not** exclude exceptional
carriers in the same linear system.
The comparison clarifies why high-degree
generic thick carriers and the exceptional
STCI-realization locus are different
problems, and why the
[normalization/conductor framework](../frameworks/carrier-normalization/index.md)
remains necessary.

### Normalization conductors and ordinary double surfaces

- Steven Kleiman, Joseph Lipman, and Bernd Ulrich, “The source double-point
  cycle of a finite map of codimension one,” author PDF:
  <https://www.math.purdue.edu/~jlipman/papers/2-point.pdf>.
- V. S. Kulikov and Vik. S. Kulikov, “On complete degenerations of surfaces
  with ordinary singularities in \(\mathbf P^3\),” *Sbornik: Mathematics*
  201 (2010), 129--158:
  <https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&option_lang=eng&paperid=7526&what=fullteng>.
- Verified use: under a **smooth normalization** and clean conductor, the
  source double-point formula gives \(K_S+D_{\mathrm{cond}}=2H\) for a
  sextic.  For an ordinary sextic with rational-quartic double curve, the
  classical formulas give \(K_S^2=-4\), \(c_2=28\), \(\chi=2\), and twenty
  pinch points.  These formulas do not apply to an arbitrary generically
  nodal sextic or to a singular normalization; the qualification is essential
  in the split-sextic analysis.

### Hartshorne--Polini, 2015

Robin Hartshorne and Claudia Polini, “Divisor class groups of singular
surfaces,” *Transactions of the AMS* 367 (2015), 6357--6385.

- Source: <https://arxiv.org/abs/1301.3222>
- Verified exact criterion: if \(C\) meets \(\operatorname{Sing}X\) only
  finitely, then \(C\) is an STCI on \(X\) exactly when
  \(r[C]=m[H]\) in \(\operatorname{APic}(X)\) for some positive \(r,m\).
- Verified restriction: for ordinary singularities in characteristic zero,
  smooth STCI curves satisfy strong degree--genus bounds; a rational quartic
  cannot occur on such a carrier.
- Escape hatch: the criterion does not apply when the carrier is singular along
  the whole curve, exactly the “thick” regime retained in this report.

The October 10 literature audit identifies Examples 6.10 and 7.16 for
the smooth nine-point plane model and its STCI curves, and Remarks 2.5
and 3.2 for the conductor quotient in the singular-normalization case.
The latter uses classes in APic downstairs with Cartier pullback upstairs.
Example 7.13 and Remark 7.14 exhibit a ruled cubic with root-of-unity orders
of arbitrary size. This mechanism supplies no bounded mate-order search.
[Dated primary-source assessment](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/supplements/OCT10_TRISECANTS_NORMAL_BUNDLE_AND_RIBBONS.md#source-2026-10-10-session-primary-literature-frontier-refreshmd).

### Jaffe

David B. Jaffe, “Applications of iterated curve blow-up to set theoretic
complete intersections in \(\mathbf P^3\),” *Journal für die reine und
angewandte Mathematik* 464 (1995), 1--46.

- Source: <https://arxiv.org/abs/alg-geom/9410008>
- Verified scope: in characteristic zero, if two defining surfaces have no
  common singular point, iterated blowups give degree bounds and a finite list.
  For \((d,g)=(4,0)\), with \(a\le b\), the list is
  \[
  \begin{gathered}
  (3,4),(3,8),(4,4),(4,7),(6,26),(9,48),(10,28),(12,18),\\
  (13,16),(17,220),(18,118),(19,84),(20,67),(22,50),(28,33).
  \end{gathered}
  \]
- It is not an unconditional finite reduction: common singular points and
  surfaces singular along the curve remain outside its strongest bound.
- Remark 2.2 explicitly identifies the missing structural theorem: it is not
  known in the relevant generality that the infinitely-near type sequence is
  nonincreasing.  Jaffe already supplies the iteration; future work must
  control it in the presence of common singularities rather than merely
  repeat the blowups.

- Theorem 11.11 treats a quartic with rational singularities and a smooth
  curve cut out set-theoretically by an arbitrary mate. It forces linear
  normality. The displayed result is over `C`; the introduction states
  characteristic-zero scope. Replacing the mate by `g+fh` in the proof
  avoids a generic-smoothness hypothesis on the original mate. Rational
  singularities of the finite normalization alone do not give this
  hypothesis on the quartic carrier. [Dated theorem scope check](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/supplements/OCT10_TRISECANTS_NORMAL_BUNDLE_AND_RIBBONS.md#source-2026-10-10-session-primary-literature-frontier-refreshmd).

- Separate all-degree **cone-carrier** scope: Jaffe's [author paper introduction](https://arxiv.org/html/alg-geom/9410008) reports the prior characteristic-zero result d≤g+3 for a smooth curve cut out by a reduced irreducible cone and another reduced irreducible surface. For (d,g)=(4,0) this excludes that chosen type of carrier in every degree. The original paper is *Space curves which are the intersection of a cone with another surface*, Duke Math.J.57 (1988), 859–876, [DOI](https://doi.org/10.1215/S0012-7094-88-05738-9). Its original proof was inaccessible in the bounded audit: this is a primary author-reported theorem, not a freshly reconstructed proof or a theorem about all higher-degree surfaces.

### Ronconi, 1985

The [1985 paper](https://www.numdam.org/item/RSMUP_1985__74__23_0.pdf),
p. 23, shows that each complex quartic monoid singular in codimension one
has some curve that fails to be STCI on that prescribed monoid. The theorem
does not identify that curve with the fixed quartic. The October 10 audit
read the summary and introduction. It could not access the full 1984
predecessor paper. [Dated primary-source assessment](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/supplements/OCT10_TRISECANTS_NORMAL_BUNDLE_AND_RIBBONS.md#source-2026-10-10-session-primary-literature-frontier-refreshmd).

## The smooth rational quartic and its known exclusions

### Craighero, 1981

P. C. Craighero, “Una osservazione sulla curva di Cremona di
\(\mathbf P^3_k\),” *Rendiconti del Seminario Matematico della Università di
Padova* 65 (1981), 177--190.

- Source: <https://www.numdam.org/item/RSMUP_1981__65__177_0/>
- Verified scope: in characteristic different from \(2,3\), the monomial
  quartic is not the STCI of a cubic and a quartic. The paper also records the
  characteristic-three cubic--quartic equations.

### Stagnaro, 1983

Ezio Stagnaro, “Sulle curve razionali non singolari di ordine 4 di
\(P^3_k\),” *Rendiconti dell'Accademia Nazionale delle Scienze detta dei XL*,
Memorie di Matematica VII (1983), 51--88.

- Scan:
  <https://media.accademiaxl.it/memorie/S5-VVII-P1-2-1983/Stagnaro51-87.pdf>
- Verified scope: Theorem 3 excludes degree-three/degree-four surfaces
  osculating along any smooth rational quartic in characteristic different
  from two and three, and the paper constructs characteristic-three
  examples.  Thus the global no-\((3,4)\) consequence of P-010 is classical.
- P-010's stronger assertion is different: it excludes every embedded
  primitive triple of conormal type \(O(-7)\), whether or not it is generated
  by a global cubic/quartic pair.  No prior all-quartic computation of that
  formal-neighborhood obstruction was located.

### Craighero--Gattazzo, 1986

P. C. Craighero and R. Gattazzo, “The curve
\(\widetilde{\mathcal C}_4=(\lambda^4,\lambda^3\mu,\lambda\mu^3,\mu^4)\)
is not set-theoretic complete intersection of two quartic surfaces,”
*Rendiconti del Seminario Matematico della Università di Padova* 76 (1986),
177--200.

- Source: <https://www.numdam.org/item/RSMUP_1986__76__177_0/>
- Verified scope: excludes only the degree pair \((4,4)\), in characteristic
  different from \(2,3\); it is not an absolute non-STCI theorem.

### Craighero--Gattazzo, 1989

P. C. Craighero and R. Gattazzo, “No rational nonsingular quartic curve
\(\mathcal C_4\subset\mathbf P^3\) can be set-theoretic complete intersection
on a cubic surface,” *Rendiconti del Seminario Matematico della Università di
Padova* 81 (1989), 171--192.

- Source: <https://www.numdam.org/item/RSMUP_1989__81__171_0/>
- Verified scope: over an algebraically closed field of characteristic zero,
  no smooth rational quartic is an STCI of a cubic and a surface of any degree.
  This removes every \((3,n)\) pair, but not higher-degree carriers.

### Thoma, 1989

Apostolos Thoma, “Ideal theoretic complete intersections in
\(\mathbf P^3_K\),” *Proceedings of the AMS* 107 (1989), 341--345.

- DOI: <https://doi.org/10.1090/S0002-9939-1989-0984817-6>
- Verified scope: in characteristic zero, a projective monomial space curve is
  cut out by two binomial surfaces precisely in the ideal-theoretic complete
  intersection case. This excludes two binomials for \(C_0\), not two arbitrary
  forms.

### Hellus--Hübl, 2016

Michael Hellus and Reinhold Hübl, “A result on Macaulay's curve,”
*Communications in Algebra* 44 (2016), 479--485.

- Source: <https://arxiv.org/abs/1312.7661>
- Verified scope: if two homogeneous forms cut out \(C_0\), their lowest and
  highest components in the natural bigrading must each have nonunit common
  divisors lying in \(I_{C_0}\). This is a necessary structural constraint,
  not a nonexistence theorem.

## Positive characteristic

### Hartshorne and Moh

- Robin Hartshorne, “Complete intersections in characteristic \(p>0\),”
  *American Journal of Mathematics* 101 (1979), 380--383.
- T. T. Moh, “Set-theoretic complete intersections,” *Proceedings of the AMS*
  94 (1985), 217--220.
- Moh source:
  <https://www.ams.org/proc/1985-094-02/S0002-9939-1985-0784166-1/>
- Verified scope: projective monomial curves are STCI in positive
  characteristic; Moh also gives a broader sufficient construction from a
  birational plane projection with only cusps whose linear center is disjoint
  from the curve.
- These results explain the mechanism in P-008. The current report proves the
  additional family statement P-012—every smooth rational quartic in positive
  characteristic—using an *internal* projection whose center lies on the
  curve, followed by explicit Frobenius descent. Thus Moh's stated projection
  criterion does not directly supply P-012.

### Barile--Morales--Thoma: a direct construction for the fixed family

Margherita Barile, Marcel Morales and Apostolos Thoma, *Set-theoretic complete intersections on binomials*, Proc. AMS 130 (2002), 1893–1903, [publisher DOI](https://doi.org/10.1090/S0002-9939-01-06289-X); [inspected primary-article PDF](https://scispace.com/pdf/set-theoretic-complete-intersections-on-binomials-3eapbpony9.pdf).

Theorem 5 characterizes toric binomial STCI in characteristic p by complete p-gluing. Theorem 4 says characteristic-zero binomial STCI forces ideal-theoretic CI. Section 3 Example 1 explicitly handles {(d,0),(d−1,1),(1,d−1),(0,d)}. For C0, d=4; choose p^e>5 and write p^e=3a+4b with a,b≥0. Its construction specializes to the homogeneous pair x_2^4−x_1^3x_4 and x_3^(p^e)−x_1^b x_2^a x_4^(2a+3b). Their radical is the cone ideal in characteristic p, hence their projective support is C0. Frobenius is essential. The characteristic-zero binomial-only exclusion supplies no arbitrary-form obstruction. This full-proof check avoids treating the inaccessible Moh article as newly verified beyond its abstract.

### Cowsik--Nori is affine

R. C. Cowsik and M. V. Nori, “Affine curves in characteristic \(p\) are set
theoretic complete intersections,” *Inventiones Mathematicae* 45 (1978),
111--114.

- DOI: <https://doi.org/10.1007/BF01390268>
- Verified scope: every pure affine curve in \(\mathbf A^n\) over a
  characteristic-\(p\) field is cut out set-theoretically by \(n-1\)
  equations.
- It does not settle a projective curve by passing to the affine cone: the cone
  over a projective curve has dimension two in \(\mathbf A^4\), not dimension
  one. Dehomogenization also loses control at infinity.
- No authoritative theorem settling every integral projective curve in
  \(\mathbf P^3\) in a fixed positive characteristic was located; current
  sources still list special projective families rather than a general result.

### Recent toric work

Anargyros Katsabekis and Apostolos Thoma, “Radical splittings of toric ideals,”
*Journal of Algebraic Combinatorics* 64 (2026), article 42.

- DOI: <https://doi.org/10.1007/s10801-026-01593-w>
- Verified source-specific scope: §4, Remarks 4.7, treats symmetric projective monomial curves with a+b=d and gcd(a,b,d)=1. Its radical splitting number is 2 in positive characteristic and 3 in characteristic zero; fixed C0 has (a,b,d)=(1,3,4). This concerns **binomial** arithmetic rank and does not decide two arbitrary forms.

## Cohomological background

### Hartshorne second vanishing

Robin Hartshorne, “Cohomological Dimension of Algebraic Varieties,” *Annals of
Mathematics* 88 (1968), 403--450.

- Source: <https://annals.math.princeton.edu/1968/88-3/p03>
- Verified consequence used here: for the homogeneous prime of an integral
  projective curve in \(\mathbf P^3\), local cohomological dimension is already
  two. Thus cohomological complete-intersection behavior does not imply
  arithmetic rank two in this problem.

### Lyubeznik

Gennady Lyubeznik, “Étale cohomological dimension and the topology of
algebraic varieties,” *Annals of Mathematics* 137 (1993), 71--128.

- Source: <https://annals.math.princeton.edu/1993/137-1/p02>
- Scope used: étale cohomological-dimension bounds associated with affine
  coverings. For complements of smooth space curves, constant coefficients
  reach but do not exceed the bound forced by two principal affine opens, so
  they do not provide the missing obstruction.

## Status conclusion after the dated search

The inherited searches (through 2026-09-30) included exact-title and citation searches around the sources
above, 2024--2026 arXiv and journal results on residual intersections, affine
lci curves, toric arithmetic rank, multiple structures, and projective space
curves. No later source was found that:

1. proves every smooth complex curve in \(\mathbf P^3\) is an STCI;
2. gives a smooth complex counterexample; or
3. decides the unrestricted two-arbitrary-form question for \(C_0\).

Therefore the smooth complex problem, and already the explicit smooth rational
quartic \(C_0\), remain open on the literature checked through 2026-09-30.

## Multiple structures and dependent jet conditions: background versus STCI synthesis

The geometric language used by the current jet-condition program has substantial classical background. Ferrand's doubling construction encodes doubles through quotients of the conormal bundle; Bănică--Forster develop the filtrations and multiplicative line-bundle structure of primitive and quasiprimitive multiple structures; subsequent work, including Drézet's theory of primitive multiple curves and their extensions, continues this framework. Separately, the interpolation literature studies when fat-point and jet conditions fail to impose independent conditions on linear systems.

These sources are background for the **form** of the STCI analysis; they do not by themselves establish the project-specific mechanism currently recorded for the rational quartic. In particular, the chain
\[
R\longrightarrow H^0(I_R(1,3))\longrightarrow H^0(O_{2R}(6))
\]
and the associated ruling-fiber degeneration are retained as an STCI-specific geometric synthesis in this repository. The present literature check did not locate this exact mechanism as a published theorem. This is not a novelty claim: absence from the checked literature is weaker than proof of originality.

Accordingly, future work should describe the general philosophy of dependent infinitesimal/jet conditions as standard background and reserve any novelty language for precisely stated STCI-specific lemmas after a dedicated literature check.


## October 21 accepted-interface references

The conditional regular-surface obstruction [STCI-R-0018](../results/regular_singular_root_formal_obstruction.md) uses Bost, *Algebraic leaves of algebraic foliations over number fields*, Corollary 3.8, for algebraization with a proper connected lci scheme of definition; Hartshorne, *Lectures on Deformation Theory*, Theorems 6.3 and 9.3, for deformations of singular lci Cartier curves; and the ruled-surface argument used by STCI-R-0005. These citations and their precise singular-center applicability were checked in [the dedicated audit](../results/regular_singular_root_formal_obstruction.md). This ledger entry records dependencies, not an independent new literature theorem.

## General constructive mechanisms checked in the synthesis

The [global-equation chapter](../arguments/equations/global_equations_and_constructions.md), [finite-pullback proof](../arguments/carriers/finite_pullback_and_matrix_obstructions.md), and [foliation/affine account](../arguments/carriers/foliation_and_affine_degree_mechanisms.md) state exact hypotheses alongside their uses. In particular: Poonen Theorem 2.2 extends sufficiently highly polarized maps from a fixed closed subscheme with target dimension at least ambient dimension, without sole-inverse-support control; Amerik–Kuznetsova Theorem 2 concerns degree-greater-than-one maps between projective bundles over a simply connected complex projective base with H1(B,L)=0 for every line bundle; Forster–Wolffhardt Theorem 1.5 is affine and preserves a zero scheme in the dual bundle, not a split target. The normalized foliation formulas retain the finite non-Kupka/component hypotheses and the unit-times-exact condition. None supplies unrestricted equations or a universal obstruction for C0.

## Section realization, finite-order presentations and liaison

The mathematical accounts now incorporate the following bounded primary-source comparisons directly into their proofs:

- [Complement sections](../arguments/equations/complement_section_obstructions.md) uses purity/Gysin and sphere-bundle obstruction theory, then checks the affine and analytic hypotheses of the cited splitting and realization theorems. Twisted Chow-Witt vanishing here does not assume the complement is affine.
- [Punctual presentations](../arguments/normal-geometry/punctual_quadric_extensions.md) retains the distinction between arbitrary homogeneous twists and the linear/maximal-generation hypotheses of matrix-representation results, and between multiple quadrics and double-plane classifications.
- [Quadratic conductor descent](../arguments/linkage/quadratic_covers_and_conductor_descent.md) combines finite duality with the canonical-module postulation argument; its module-generation hypotheses and non-Gorenstein controls remain explicit.
- [Supported linkage](../arguments/linkage/supported_linkage_operations.md) checks the source and generic-smoothness hypotheses in liaison and blowup results rather than using liaison-class membership or Rao dimensions as realization theorems.

These are scoped integrations, not an exhaustive new literature search.

The selected later contributions retain these further primary-source limits in
their mathematical homes:

- [Canonical conductor endomorphisms](../arguments/linkage/quadratic_covers_and_conductor_descent.md#13-canonical-conductor-section-completion-and-embedded-action)
  uses the canonical-module endomorphism description of finite S2-ification;
  it does not identify that completion with an embedding repair. The ambient
  norm bound is a repository deduction from actual equations and the existing
  canonical Hilbert-function inequality.
- [Liaison additions and residual constructions](../arguments/linkage/supported_linkage_operations.md)
  states the HMN ideal/Rao sequence, the full CDH subsheaf and cohomology
  conditions, and the BPW height/support limits beside the actual constructions.
- [Elementary transforms and monads](../arguments/equations/global_equations_and_constructions.md)
  distinguishes the specific torsion-free sheaf from a reflexive or monad output;
  the fixed-twist ordinary-power generic-flatness result asserts flatness, not
  vanishing or a mixed-characteristic lift.
- [Finite Gorenstein covers](../arguments/torus/fixed_surface_and_endpoint_algebras.md)
  applies Casnati–Ekedahl to the supplied actual cover. Its canonical embedding
  and available sections do not supply the required original projective image
  or its algebra-linear duality. The [polarized retraction criterion](../arguments/torus/contact_jacobians_and_hamiltonian_actions.md#a-pencil-compatible-polarized-retraction-cannot-extend-globally)
  separately uses formal étaleness only on the unramified open.
- [The sextic cyclic-cover calculation](../arguments/carriers/sextic_pair_reduction.md)
  checks characteristic-zero Bertini and the normalized Kummer eigensheaf
  formula with arbitrary normal singularities. Its numerical invariants belong
  to the normal cover; resolution inequalities are not imported without their
  hypotheses.

These entries reuse the scoped primary checks recorded with the selected
contributions and their independent reviews. They do not certify unchecked
extensions or assert literature novelty.


## Source comparisons for carrier gluing, global jets and spectral realization

The following homes retain the checked primary statements, complete repository
deductions and their application boundaries. This integration reuses the scoped
source reviews; it is not a new exhaustive literature search or a novelty claim.

- [Carrier conductor contact](../arguments/carriers/carrier_conductor_differential_comparison.md)
  uses finite duality near the inverse curve and the actual transverse
  differential. [Singular-gluing controls](../arguments/carriers/square_descent_and_singular_gluing.md)
  show why the full conductor and smoothness hypotheses matter; trace and power
  arguments retain their characteristic restrictions.
- [Quintic–octic cover geometry](../arguments/carriers/quintic_octic_ade_cover_and_triple.md)
  retains the exact Jaffe-type local defect formulas and the canonical-cover
  inequality hypotheses. Repeated symbols are covered by the complete proof;
  a rank budget alone does not establish the exclusion.
- [Global equation jets](../arguments/equations/global_equation_jets.md) applies the filtered
  complex spectral sequence to actual source images. The general finite
  homogeneous realization argument uses the stated formal-rational-function
  theorem; its existential conclusion is distinct from the explicit
  quadric-flag bound and from a uniform effective witness-degree bound.
- [Spectral powers](../arguments/spectral/spectral_pushforward_powers.md) uses splitting on
  the projective line and genus-one cohomology. The
  [determinant-scheme argument](../arguments/spectral/spectral_determinant_schemes.md) keeps
  relative Picard torsion, fixed-curve torsion multiplicities and total-space
  smoothness separate. Its graded family is not an ambient realization theorem.
- [Cox fibers and ordinary powers](../arguments/torus/cox_fiber_and_power_defects.md)
  uses the specified Cox presentation and distinguishes saturation and ambient
  section defects from reduction-number conclusions. The
  [genus and threshold comparisons](../arguments/carriers/genus_and_threshold_limits.md)
  apply least-containing-degree bounds to the full complete intersection and
  retain the local positivity hypotheses.
- [Supported pencils](../arguments/carriers/pencil_milnor_budget.md) keeps the polar/Euler
  identity, special-point Milnor defects, and complete-ideal/local-threshold
  comparisons. For the fixed quartic, the resulting global inequality is
  implied by the local bounds; the identity is not a new independent exclusion.
- [Bounded characteristic transfer](../arguments/arithmetic/effective_characteristic_transfer.md)
  uses an effective arithmetic Nullstellensatz with its explicit encoding and
  height conditions. Quartic-carrier growth is unconditional; all-pair growth
  still assumes characteristic-zero nonexistence.
- [Finite maps](../arguments/equations/global_equations_and_constructions.md),
  [supported flat closure and cover moduli](../arguments/torus/fixed_surface_and_endpoint_algebras.md),
  and [smooth-cone quantization](../arguments/torus/contact_jacobians_and_hamiltonian_actions.md)
  retain the limits of extension, stable patching, moduli properness and supported
  characteristic-class results. Flat closure does not preserve every Gorenstein,
  splitting or presentation property; quantization does not supply the required
  filtered ambient equations.


The [exact Chow bundle account](../arguments/equations/chow_bundle_maps.md) retains the
independently reviewed incidence-variety Hom proof in every characteristic,
and distinguishes Eisenbud–Schreyer's linear Chow determinants from the
prescribed Sylvester bundle types. The
[exceptional-cover controls](../arguments/normal-geometry/section_defects_and_exceptional_cover_controls.md#smooth-models-and-dynamical-source-hypotheses)
retain the everywhere-potential-good-reduction and simultaneous-conjugacy
hypotheses of Petsche–Szpiro–Tepper and Silverman. Their final source review
closed the earlier audit gap; neither comparison provides an unrestricted
STCI construction or obstruction.


### Zero-dimensional Chow norms, traces, and border bases

Carlos D'Andrea and Gabriela Jeronimo, *Rational Formulas for Traces in
Zero-Dimensional Algebras*, Applicable Algebra in Engineering,
Communication and Computing **19** (2008), 495--508,
[arXiv:math/0503721](https://arxiv.org/abs/math/0503721), express traces of
multiplication in a finite-dimensional algebra through generalized Chow
forms; for torus complete intersections they give sparse-resultant formulas.
This is the established input behind the
[homogeneous transverse Chow/norm comparison](../arguments/torus/chow_arrangement_moments.md#the-homogeneous-transverse-chow-form-as-a-section-norm).
The project-specific calculation there is the explicit quartic kernel
\(\Psi_{W,U,V}\), its fixed-plane injectivity on the translated family, and
its comparison with the already-established global source resultant.

Achim Kehrein and Martin Kreuzer, *Characterizations of Border Bases*,
J. Pure Appl. Algebra **196** (2005), 251--270,
[DOI 10.1016/j.jpaa.2004.08.028](https://doi.org/10.1016/j.jpaa.2004.08.028),
give the standard border-basis characterizations. In particular, the formal
multiplication matrices commute exactly when the border prebasis defines the
intended zero-dimensional algebra. Their theory identifies the
[marked border-product gate MJ1](../arguments/residuals/blowup_residual_geometry.md#finite-index-rigidity-of-higher-marked-jets)
as a rectangular special case of a classical algebra-consistency criterion.
The STCI-specific content of MJ2--MJ4 is the consequence of that gate for the
actual marked graph and homogeneous contact constraints, not the
border-basis criterion itself.


### Trace matrices and the radical of a zero-dimensional section

Itnuit Janovitz-Freireich, Bernard Mourrain, Lajos Rónyai and Ágnes Szántó,
*On the Computation of Matrices of Traces and Radicals of Ideals*,
J. Symbolic Computation **47** (2012), 102--122,
[arXiv:0901.2778](https://arxiv.org/abs/0901.2778), compute moment and trace
matrices from Macaulay-type resultant matrices and, for affine complete
intersections, from Bezoutians; these matrices recover the radical of a
zero-dimensional ideal.  The underlying characteristic-zero fact that the
radical of the regular trace pairing is the nilradical is also already used
in the repository's finite-algebra arguments.

The
[five-row translated-support gate CHR1--CHR6](../arguments/torus/chow_arrangement_moments.md#a-five-row-trace-rank-gate-for-one-translate-versus-residual-translates)
applies this classical theorem to the fixed symmetric plane section.
Its project-specific contribution is the five homogeneous degree-four test
sections whose restricted trace map has rank four for exactly one translated
quartic and rank five for every arrangement containing at least two distinct
translates.  No general trace-radical theorem is attributed to this project.


### The rational quartic Rao module and a hyperplane-jet application

Mengyuan Zhang, *The SpaceCurves package in Macaulay2*, Journal of Software
for Algebra and Geometry **8** (2018), 31--48, records explicitly that the
smooth rational quartic in \(\mathbf P^3\) has Hartshorne--Rao module \(k\)
concentrated in degree \(1\), and that its ideal consists of the unique
quadric together with three cubic generators.  This is standard liaison
theory and is not new to the project.

The
[terminal hyperplane-jet theorem HJ1--HJ6](../arguments/equations/global_equation_jets.md#a-terminal-hyperplane-jet-defect-in-every-degree)
uses this known one-dimensional Rao module on the symmetric hyperplane
\(x_3=x_0\).  The reduced section is the plane \((2,2)\) complete
intersection
\((x_0^2-x_1x_2,\ x_1^2-x_2^2)\).  All truncated hyperplane jets of a
degree-\(d\) equation lift through normal order \(d-3\); at order \(d-2\)
there is exactly one missing class, represented by
\((x_3-x_0)^{d-2}(x_1^2-x_2^2)\).  The all-degree placement of the Rao
class in this particular transverse flag is the project-specific
application; the Rao-module computation itself is classical.


### Scheja--Storch: Kähler different versus the Artin socle

For a finite-dimensional local algebra
\(A=k[[x_1,\ldots,x_n]]/I\) in characteristic zero, the classical
Scheja--Storch theorem identifies the Kähler different
\(\mathfrak D_K(A/k)=\operatorname{Fitt}_0\Omega_{A/k}\):
it is nonzero exactly when \(A\) is a zero-dimensional complete
intersection, and then it is the socle of \(A\).  Equivalently, for a
non-complete-intersection Artin algebra the maximal Jacobian-minor ideal
vanishes in \(A\).  A modern proof/reference is
[Ulrich et al., *Duality and socle generators for residual intersections*,
Theorem 7.1 and Appendix](https://www.math.purdue.edu/~bulrich/papers/Duality-and-Socle-180119.pdf);
the same theorem is summarized in Vasconcelos' survey on Jacobian ideals.

This is the strongest established input in the
[dense-orbit contact calculation](../arguments/torus/contact_jacobians_and_hamiltonian_actions.md#dense-orbit-contact-is-automatic-after-sole-support-collapse).
For the quartic's induced transverse Poisson bracket,
\(\{u,v\}\) is a unit times \(u-v\).  Since \(u-v\) belongs to the maximal
ideal at the sole-support point \((1,1)\), it kills the Kähler different in
the CI case and the different is already zero in the non-CI case.
Accordingly every finite transverse ideal supported at \((1,1)\) is
automatically involutive.  The project-specific content is the explicit
transverse bracket and its consequence for where the global contact
obstruction can live, not the Scheja--Storch theorem.
