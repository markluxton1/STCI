# STCI Literature Ledger

Checked through: 2026-09-30

This ledger records the scope actually used in the research report. A source is
not listed as settling more than its hypotheses permit. “No later resolution
found” is a documented search result, not a proof that no unindexed work exists.

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
- Exact algebraic criterion used here: for a height-two ideal in a
  four-dimensional regular local/graded setting, arithmetic rank two is
  characterized by a coregular sequence of length two, equivalently codepth two
  in the relevant \(H_I^2\) module. Ordinary vanishing of \(H_I^{>2}\) is not
  enough.

### Hassanzadeh, 2024--2025

S. Hamid Hassanzadeh, “Set-Theoretically Perfect Ideals and Residual
Intersections,” arXiv:2409.05705, revised 2025; to appear in the *Journal of
the London Mathematical Society*.

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

A modern survey (D'Cruz, Theorem 2.7) states that arithmetically
Cohen--Macaulay curves in \(\mathbf P^3\) are set-theoretic complete
intersections and attributes this to Robbiano--Valla and Stückrad--Vogel.
The broad original-proof scope is not yet verified in this repository.

- Lorenzo Robbiano and Giuseppe Valla, “Some curves in \(\mathbf P^3\) are
  set-theoretic complete intersections,” LNM 997 (1983), 391--399:
  <https://doi.org/10.1007/BFb0061654>
- Scope qualification, strengthened by the 2026-10-05/06 audit: the inspected
  Robbiano--Valla 1983 article fixes a monomial curve before its ACM
  proposition. That proof supports the ACM monomial class. The LNM chapter
  and the other original cited proof were not recovered in full. The modern
  broad statement is evidence of its assertion, not an independently
  reconstructed proof for arbitrary ACM curves. See
  `notes/2026-10-05-foundational-frontier-audit.md`.
- Relevance: smooth rational quartics are not linearly normal and hence not
  ACM, so even the modern broad assertion would not settle this test case.

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
  <https://mathweb.tifr.res.in/sites/default/files/publications/ln/tifr62.pdf>
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

### Mandal--Zinna, 2025 preprint

Lisa Mandal and Md. Ali Zinna, “On set-theoretic complete intersections for
smooth curves in three-dimensional affine schemes,” arXiv:2511.07589
(submitted November 2025).

- Source: <https://arxiv.org/abs/2511.07589>
- Verified abstract theorem: every height-two local-complete-intersection ideal
  in a commutative noetherian ring of dimension three is a set-theoretic
  complete intersection.  The same preprint also gives a four-dimensional
  affine result over an algebraic closure of a finite field and a stronger
  complete-intersection conclusion under trivial conormal bundle.
- This is stronger and more general on the affine three-dimensional side than
  the separately published conditional theorem above.  It still does not
  apply to the homogeneous coordinate ring \(k[x_0,x_1,x_2,x_3]\), which has
  dimension four, and it supplies no compatibility at the hyperplane at
  infinity.  P-007 records the missing projective boundary condition exactly.
- The broad statement is an unrefereed arXiv v1 as of the search cutoff and
  must not be conflated with the authors' narrower peer-reviewed 2026 theorem.

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
  The pure-power criterion in P-033 is the resulting specialized corollary.
- Scope qualification: this is a classical cycle-level reformulation and
  computational certificate. It neither constructs a defining pair nor proves
  that one exists for any unresolved curve.

## Conductor descent and codimension-two Gorenstein criteria

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

### Franco--Kleiman--Lascu

Daniele Franco, Steven Kleiman, and Alexandru Lascu, “Gherardelli linkage and
complete intersections,” *Michigan Mathematical Journal* 48 (2000), 271--279.

- Source: <https://arxiv.org/abs/math/0003075>
- Verified scope: in characteristic zero, a pure Cohen--Macaulay codimension-two
  subscheme is a complete intersection under the corresponding subcanonical
  and self-linkage criterion. This is useful for recognizing a multiple
  structure once constructed; it does not construct one on every support.

## Carrier surfaces, divisor classes, and blowups

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
- Verified scope: concerns toric/binomial radical splittings and binomial
  arithmetic rank. It does not decide whether the characteristic-zero ideal of
  \(C_0\) is the radical of two arbitrary forms.

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

The searches included exact-title and citation searches around the sources
above, 2024--2026 arXiv and journal results on residual intersections, affine
lci curves, toric arithmetic rank, multiple structures, and projective space
curves. No later source was found that:

1. proves every smooth complex curve in \(\mathbf P^3\) is an STCI;
2. gives a smooth complex counterexample; or
3. decides the unrestricted two-arbitrary-form question for \(C_0\).

Therefore the smooth complex problem, and already the explicit smooth rational
quartic \(C_0\), remain open on the literature checked through 2026-09-30.
