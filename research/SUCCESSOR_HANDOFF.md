> **2026-10-06 CONSOLIDATION NOTICE:** The authoritative current status is [AUDITED_STATE_2026-10-06.md](AUDITED_STATE_2026-10-06.md). Where older frontier language below conflicts with that audited state, the audited state controls. Historical material below is retained for provenance.\n\n# STCI Successor-Session Handoff

Prepared: 2026-09-30

This file is the entry point for a fresh research session. It is intentionally
more concise than `RESEARCH_RECORD.md`. Every claim below should be read with
the exact hypotheses and proof in that record; source scopes are in
`LITERATURE_LEDGER.md`.

## 0. Continuation batch (2026-10-05)

The dated continuation work is indexed in
[`RESEARCH_UPDATE_2026-10-05.md`](RESEARCH_UPDATE_2026-10-05.md). It records
new finite local-cohomology reductions, independently audited regular
degree-(4,6) and type-(4,5) exclusions, mixed-pole calculations, the fixed
split-sextic boundary, and the exact companion scripts. The general STCI
problem and the unrestricted quartic case remain open; the update preserves
the proof, audit, computation, and speculation boundaries needed for the next
session.

## 1. Precise target problem and hypotheses

Let \(k\) be an algebraically closed field and let
\(C\subset\mathbf P^3_k\) be an integral closed curve. With
\(S=k[x_0,x_1,x_2,x_3]\) and saturated homogeneous prime \(I_C\), ask whether
there always exist homogeneous \(F,G\in S\) such that

\[
 V_+(F,G)=C,
 \qquad\text{equivalently}\qquad
 \sqrt{(F,G)^{\mathrm{sat}}}=I_C.
\]

This is the general projective integral-curve STCI problem. It is not merely
the smooth case, the rational-quartic case, the affine problem, binomial
arithmetic rank, scheme-theoretic complete intersection, or cohomological
dimension two. “Complete” in the old README wording is redundant for a closed
projective curve and can be confused with “complete intersection.”

The principal characteristic-zero test case is

\[
 C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3,
\]

with

\[
 q=x_0x_3-x_1x_2,
\]

\[
 A=x_0^2x_2-x_1^3,\quad
 B=x_0x_2^2-x_1^2x_3,\quad
 D=x_2^3-x_1x_3^2,
\]

and \(I_{C_0}=(q,A,B,D)\).

## 2. Current literature status and checked references

**KNOWN / search checked through 2026-09-30:** the general problem remains
open, the universal smooth complex problem remains open, and the unrestricted
characteristic-zero two-form question for \(C_0\) remains open.  P-040 excludes
only the degree pair \((4,5)\).

Most important checked sources:

- Eisenbud--Harris, *The Practice of Algebraic Curves* (2024), Example 3.13
  and Proposition 3.14: explicitly retains \(C_0\) as a famous open problem.
- Murayama, *MA665 Algebraic Geometry II* (28 April 2026), Question 2.6.40
  and later Macaulay-curve discussion: still open.
- Forster, LNM 1092 (1984), Theorems 5.1--5.2: every lci curve in affine
  space is an STCI.
- Bănică--Forster (1986), Boratyński (1992), and Manolache: filtrations and lci
  criteria for multiple curves.
- Eisenbud--Van de Ven (1981), Proposition 6: in characteristic zero,
  \(N_C\simeq O(7)^2\) for a smooth rational quartic.
- Stagnaro (1983) and Craighero--Gattazzo (1989): classical cubic-carrier
  exclusions for smooth rational quartics.
- Jaffe (1995): iterated blowups and degree restrictions; Remark 2.2 identifies
  missing monotonicity of the infinitely-near type sequence.
- Hartshorne--Polini (2015, 2019): almost-Cartier carrier criteria and the
  quasi-cyclic local-cohomology formulation.
- Mandal--Zinna, *J. Algebra* 690 (2026): conditional affine-threefold theorem;
  arXiv:2511.07589 is a broader unrefereed v1 and must not be conflated with
  the published theorem.

No checked source gives an unrestricted pair for \(C_0\), a smooth complex
counterexample, or a theorem for all smooth complex space curves. Absence from
a dated search is not proof that no unindexed result exists.

## 3. What this program proved

The exact ledger is P-002 through P-043 in `RESEARCH_RECORD.md`. The central
results are:

1. Every smooth nondegenerate rational quartic, in every characteristic, lies
   on a unique smooth quadric as type \((1,3)\) or \((3,1)\), and is cut out by
   that quadric plus two cubics.
2. The quadric cannot belong to an STCI pair; no carrier in a defining pair can
   be smooth along the whole quartic.
3. In a broad low-genus range, the two first normal forms must share a
   horizontal factor after one blowup.
4. Projective STCI relative to a chosen hyperplane is equivalent to an affine
   radical pair with relatively-prime leading forms.
5. Every smooth rational quartic in characteristic \(p>0\) has an internally
   proved and independently audited \((3,4p)\) presentation; the required cusp
   exponents are sharp after the repaired fixed-coordinate proof in P-014.
6. Fixed-degree STCI loci are constructible in finite-type families.
7. No characteristic-zero smooth rational quartic supports a primitive triple
   of conormal type \(O(-7)\).
8. Degree six is the first non-\(q\)-divisible carrier singular along the whole
   quartic; its symbolic-square space has dimension 23.
9. Two thick sextics cannot be a pair in characteristic zero. Large classes
   of one-thick-sextic configurations are excluded by normalization and branch
   intersection.
10. Under the split/no-vertical hypotheses, Hodge index forces residual root
    partition \([4]\) for type \(d=0\), and \([4]\) or \([2,2]\) for type
    \(d=1\); every other partition is excluded. The survivors are squares,
    giving \(F=T^2+qK\), and selected roots force singularities. Mate relations
    retain a scale \(k\); it cannot be canceled in torsion local class groups.
11. In the regular-ratio branch of a hypothetical \((4,6)\) pair, all four
    values \(e=0,1,2,3\) occur at first-normal order, but P-042 proves that only
    \(e=0,1\) can extend to a multiplicity-six lci.  The higher jets remain
    open in those two viable classes.
12. A \((4,5)\) pair has only the types
    \((\deg L,\deg D)=(-7,3)\) and \((-6,1)\). For \(C_0\), both are excluded
    on exhaustive parameter charts. Hence no characteristic-zero
    degree-\((4,5)\) presentation exists; this is not a higher-degree
    non-STCI theorem.
13. Independently, the regular-ratio sublocus of \((4,5)\) is reduced to two
    ambient quartic strata, the normalization \(g_1=z^2f_1\), and a
    seven-variable rank problem. This is not a universal reduction: the ratio
    of proportional first normal forms may have poles.
14. Two explicit local-cohomology classes have no common ancestor using
    multipliers of degree at most three. Degree four is the first unresolved
    multiplier degree; a coprime nonconstant-ratio first-symbol family shows
    why conormal rank alone cannot finish the problem, while P-043 excludes
    that entire explicit family at every direct-limit stage.
15. If a thick sextic has smooth normalization and the clean split conductor
    \(I_C O_S=O_S(-\Gamma_1-\Gamma_2)\), with no additional conductor
    component, then it cannot admit an STCI mate. This is a conditional
    theorem; singular normalization, extra conductor, and point-supported
    noninvertibility remain genuine loopholes.
16. For \(C_0\) in every prime characteristic \(p\ge7\), an explicit
    \((4,p)\) pair improves the curve-specific Frobenius degree.
17. For every integral \(C\subset\mathbf P^3\), STCI is equivalent to the
    existence of a nonconstant morphism
    \(\mathbf P^3\setminus C\to\mathbf P^1\), equivalently two global
    generators of some positive \(O_U(d)\).
18. Fixed-degree constructibility requires care at the arithmetic-base step:
    the generic/infinitely-many/cofinite equivalence assumes a
    one-dimensional arithmetic base with infinitely many closed points, not
    an arbitrary localization.
19. The nonregular quotient is finite data. P-038 collapses the provisional
    seven type-B \((4,5)\) strata to \(A=2D\) and
    \((c,p,\deg Z)=(2,6,10)\), after which P-040 excludes the degree pair.
    P-042 classifies seven necessary multiplicity-six numerical types and
    restricts every \((4,6)\) candidate to \(e=0\) or \(1\), leaving 15 rather
    than 36 nonregular pole strata.  This is necessary data, not existence.
20. On an arbitrary integral carrier, a mate is equivalent to an effective
    Cartier divisor \(A=\sum m_i\Gamma_i\), every \(m_i>0\), on the
    normalization whose canonical section descends through the full,
    potentially nonreduced conductor square. In characteristic zero, the
    numerical Cartier-index compression of P-015 extends to singular integral
    \(C\) whenever a minimum carrier is generically regular along \(C\).
21. The universal-line resultant is a pure power of the Chow form exactly
    when a two-form complete intersection has reduced support \(C\). The
    10-term Pluecker Chow quartic of \(C_0\) is now computed and exactly
    verified; this is a global certificate, not an existence theorem.
22. Ordinary \(K_0(\mathbf P^3\setminus C)\) is
    \(\mathbf Z[u]/(u^3,\deg(C)u^2)\), so its Koszul condition is only
    \(\deg(C)\mid ab\).
23. STCI is equivalent to an \(I_C\)-primary codimension-two graded
    Gorenstein thickening. Merely locally Gorenstein support is not enough.
24. One Chow pencil excludes 13-dimensional quartic and 28-dimensional
    quintic carrier spaces, with coordinate-reversed counterparts. An explicit
    irreducible quartic pair passes that pencil but fails its reversal.
25. In the split-sextic frontier, a \(d=1,[4]\) root at either totally
    ramified ruling is impossible by forced vertical content. The general
    \([4]\) and \([2,2]\) loci remain open; the missed two-ramified-root
    \([2,2]\) boundary has an exact content-free first-normal survivor.

The results labeled “PROVED under hypotheses” must not be stripped of those
hypotheses. In particular, the split-sextic results do not exclude every thick
sextic.

## 4. What is known only from the literature

- Current open status and the historical formulation.
- The uniform three-equation upper bound.
- STCI results for ACM curves and the affine lci theorem.
- Classical rational-quartic exclusions for cubic and quartic carriers.
- The characteristic-zero normal bundle theorem.
- The Bănică--Forster/Boratyński/Manolache multiple-structure framework.
- Ellia's primitive numerical list.
- Jaffe's iterated-blowup inequalities and the stated monotonicity gap.
- Hartshorne--Polini's ordinary-singularity and quasi-cyclic criteria.
- Hartshorne, Moh, Ferrand, and Cowsik--Nori positive-characteristic results.

The stronger all-quartic primitive-triple exclusion and the all-smooth-
rational-quartic positive-characteristic construction are internal results,
not facts imported from those sources.

## 5. Computational evidence

Exact computations that are part of proofs:

- the 14 scripts in `research/computations`, plus one preserved scratch
  verifier, for 15 sequential exact checks;
- `research/scratch/degree6/verify_mixed45_reduction.py`, SHA-256
  `862ec150664459fc94187164bcaa1d25e87c5f815e589fff1608a28efc6a89d5`;
- exact augmented minors \(2\lambda^3,-72,-48\) for three \((4,5)\) families;
- exact Groebner eliminant
  \((2s-1)^3(2s+1)(12s^2+20s+11)^3\) in the type-B dense chart.
- exact moving-frame and flatness certificates for the dense, boundary, and
  formerly missed type-B corner;
- exact 13/28-dimensional Chow-pencil exclusions and an explicit one-pencil
  survivor/reversed-pencil failure;
- the degree-four coprime, nonconstant-ratio local-cohomology multiplier
  family and its transition-compatible all-stage obstruction;
- the content-free \(d=1,[2,2]\) split-sextic boundary survivor at first-normal
  order.

Computational evidence not promoted to a general proof:

- historical modular inconsistencies now superseded at degrees through three
  by the all-stage P-037 proof;
- generic rank failures outside the exact certified \((4,5)\) families;
- the observed forced-square behavior on a large but incomplete \(d=1\)
  split-sextic factor chart.

Exact arithmetic validates the encoded identity or finite system; it does not
show that an unstated parameter space has been exhausted.

## 6. Current conjectures and falsification attempts

1. **CONJECTURAL:** every mate-compatible split sextic on \(C_0\) in the
   surviving residual partitions \([4]\) and \([2,2]\) is excluded by higher
   jets. Falsification attempt: square discriminant and the actual
   22-dimensional normal image permit integral ambient sextics and every split
   type; only the mate/Hodge/higher-jet combination yields restrictions.
2. **CONJECTURAL:** \(H^2_{I_{C_0}}(S)\) is not quasi-cyclic. Falsification
   attempt: multiplier degrees through three are excluded, but degree-four
   first-symbol candidates remain and are not ancestor constructions.
3. **SPECULATIVE:** a Jaffe-type monotonicity substitute could exclude a broad
   low-genus class. Positive-characteristic STCI constructions show that any
   such statement must detect Frobenius rather than assert formal
   nontermination in all characteristics.

The global conjecture “\(C_0\) is not an STCI in characteristic zero” remains
plausible but unproved; the present evidence does not justify presenting it as
near-settled.

## 7. Failed or exhausted approaches

- Ordinary local cohomological dimension: always the wrong granularity here.
- Constant-coefficient topology/étale cohomology: reaches but does not exceed
  the two-affine-open bound.
- Picard, Chow, Chern classes, and ordinary \(K_0\): retain only degree and
  Bezout divisibility, not unstable two-generation.
- Rao module of the reduced curve: not an obstruction to smooth STCI support.
- Two binomial equations: excludes only the binomial route.
- Naive homogenization or saturation: creates/discards boundary components
  without producing a projective pair.
- Smooth or ordinary carriers: omit the singular-along-\(C\) escape.
- First blowup alone: shared factors occur in actual positive-characteristic
  pairs and need not obstruct termination.
- Square normal discriminant \(\Rightarrow\) reducible sextic: false.
- Normal surface \(\Rightarrow\) ordinary branch intersection: false; use
  \(xy=e^n\) as the counterexample.
- First-normal image excludes most split types: false; it contains all
  \(d=0,\ldots,5\).
- First-normal \((4,6)\) incidence: exhausted; all surviving classes occur.
- A proportional first-normal pair has a globally regular quotient: false.
  The local models \(tu+v^m,u\) have constant transverse length \(m\) and
  quotient \(1/t\). Never apply the \(g_1=z^2f_1\) normalization or the
  \(e\le3\) list outside the regular-ratio branch.
- Frozen type-B coordinate \(W=1/z\): invalid; use the moving ambient quotient.
- Monomial endpoint primary ideal \((q^2,a^2)\): false; mixed terms matter.
- “Many agents” as evidence of independent representations: false in the old
  archive; mathematical ownership must be separated by representation.

## 8. Smooth-case findings

The smooth complex case is verified open and is a high-value target. The
rational quartic is the most productive intermediate object because it is the
first open smooth case, has balanced normal bundle in characteristic zero, and
admits exact quadric and jet coordinates.

Smoothness gives conormal bundles, regular blowups, and multiple-structure
filtrations, but a successful projective pair must use singular/non-Cartier
carrier behavior. The strong affine theorem therefore does not transfer by
local smoothness alone.

In positive characteristic the smooth rational-quartic family is internally
resolved positively. In characteristic zero the smallest primitive structure
and both multiplicity-five types are excluded, so degree \((4,5)\) is
impossible. No unrestricted positive or negative result is known in higher
degrees.

## 9. General-case findings

The general integral-curve problem remains substantially broader. Results that
survive beyond rational quartics include:

- the exact affine/projective leading-form criterion;
- fixed-degree constructibility;
- the first-normal common-factor theorem over its numerical range;
- almost-Cartier compression for minimum-degree generically smooth carriers;
- the warning that smooth success would not address singular support.

For singular curves, conormal bundles and regular blowups are replaced by the
exact P-032 normalization/conductor criterion, conductor-corrected rank-one
modules, Rees valuations, and almost-Cartier class groups. This is a genuine
general reformulation: normalized divisor support and class are not enough;
the canonical section must descend through the conductor. In module language
one must intersect \(\nu_*O_S(-A)\) with \(O_X\) inside the total quotient
sheaf; omitting this condition is false even for the transverse cusp. It is not yet an
existence or obstruction theorem comparable in strength to the bounded
rational-quartic exclusions.

## 10. Important examples and counterexample candidates

- \(C_0\): principal unresolved smooth characteristic-zero candidate.
- Every smooth rational quartic in characteristic \(p>0\): internally proved
  positive family, showing that formal obstructions must see characteristic.
- For \(C_0\) and every prime \(p\ge7\), the explicit pair
  \(x_0x_3^3-x_2^4\) and
  \(x_0^a x_2^b x_3^c-x_1^p\), with \(3b+4c=p\) and \(a=p-b-c\), has degrees
  \((4,p)\).
- \(F_*=A^2+B^2+D^2+q^2(x_0^2+x_1^2+x_2^2+x_3^2)\): an integral sextic
  singular exactly along \(C_0\), proving that thick carriers genuinely exist.
- \((A+x_3q)(A-x_3q)+q^3\) and
  \((A+x_3q)(2A+D)+q^3\): integral sextics with split first-normal divisor;
  counterexamples to “square discriminant forces ambient reducibility.”
- \(xy=e^n\): normal local surface where branch Mumford intersection is
  \(1/n\); counterexample to the normality shortcut.
- The former type-B survivor \((r,s)=(0,-1/2)\): an excluded intermediate
  point whose final class is \([-128z^{-1}]\), not a current candidate.
- Local-cohomology classes \(u=xz/(qB)\), \(v=yw/(qB)\): ancestor obstruction
  through degree three, plus an all-stage exclusion of the explicit P-039
  degree-four family. Other degree-four pairs remain the next frontier; this is
  not a counterexample to quasi-cyclicity.

No smooth complex counterexample is known.

## 11. Ranked unresolved leads

1. **Multiplicity-six \((4,6)\) attack:** match P-042's seven necessary
   Bănică--Forster/Gorenstein numerical types with the 15 viable first-normal
   pole strata; do not infer realization from either list.
2. **Mixed \((4,6)\) two-track analysis:** impose higher transverse jets in
   the viable regular classes \(e=0,1\), while separately parameterizing the
   15 nonregular order-\((1,1)\) strata.
3. **Surviving split-sextic roots:** analyze partition \([4]\) for \(d=0\)
   and partitions \([4]\), \([2,2]\) for \(d=1\); all other root partitions
   are already excluded. Retain the mate scale \(k\); do not cancel torsion.
4. **Degree-four local-cohomology ancestors:** classify the remaining
   proportional first-conormal pairs. P-043's exact dual certificate already
   excludes the full P-039 family at every direct-limit stage.
5. **Generalize P-012:** the independent in-run audit, including the wild
   characteristic-two step, is complete. Test other curves with unibranch
   plane projections.
6. **Jaffe-sequence control:** seek monotonicity under a precise singularity
   class, or an invariant replacing it; do not merely iterate blowups.
7. **Singular integral curves:** develop conductor/almost-Cartier reductions
   parallel to the smooth conormal formalism.

## 12. Dependencies among the leads

- Lead 1 starts from P-042, P-031, and the higher transverse-jet equations.
- Lead 2 depends on the corrected branch split in P-021, the exact
  first-normal incidence, and P-042's restriction to \(e=0,1\); it does not
  depend on resolving \((4,5)\).
- Lead 3 depends on P-020 through P-023, P-030, and the torsion correction in
  P-041, and must respect the
  separate clean-conductor exclusion P-027. Only the partitions \([4]\) and,
  for \(d=1\), \([2,2]\), outside those conditional closures should be
  parameterized.
- Lead 4 depends on P-037, P-039, and P-043 and can run independently of
  carrier geometry.
- Lead 5 depends on P-008, P-012, and P-014; the P-012 proof audit is complete,
  so this lane is now generalization rather than re-audit.
- Lead 6 starts from P-006 and Jaffe; positive-characteristic examples from
  P-012 are mandatory controls.
- Lead 7 starts from P-015 plus normalization/conductor literature and should
  remain separate from smooth-only claims.

## 13. Recommended mathematical language for each lead

1. Bănică--Forster and Manolache filtrations, Gorenstein duality, effective
   defect divisors, Euler characteristic, and conormal quotient bounds.
2. Complete local intersection algebras over \(k(C)[[x,y]]\), formal implicit
   elimination, and coefficientwise jet conditions.
3. Normalization, Mumford intersection on normal surfaces, residual binary
   forms, and Hodge index on a resolution.
4. Direct-limit local cohomology, completed endpoint principal parts, and
   finite Laurent systems.
5. Numerical semigroups, radicial/separable normalization, Frobenius descent,
   and descent of homogeneous equations.
6. Rees valuations, infinitely-near type sequences, surface singularities,
   and characteristic-sensitive invariants.
7. Conductors, torsion-free rank-one sheaves, almost-Cartier class groups, and
   normalization push-pull.

## 14. Warnings and hidden assumptions

- Use projective saturation/radical correctly; affine-cone language can hide
  the hyperplane at infinity.
- Distinguish raw homogeneous (I^2) from its saturation/sheaf symbolic square.
- The balanced bundle \(N_C\simeq O(7)^2\) is characteristic-zero; \(C_0\) has
  \(O(6)\oplus O(8)\) in characteristic two.
- Boratyński's displayed type applies after thick structures are excluded.
- A split exceptional divisor does not imply a reducible ambient surface.
- A normal surface can have fractional Mumford branch intersections.
- P-027 needs a smooth normalization and an exactly clean split conductor;
  it does not cover singular normalization, extra conductor curves, or
  point-supported noninvertibility.
- In P-023, (K_0=2H-E) is the pulled-back adjunction class, not automatically
  (K_{\widetilde S}).
- First-normal compatibility does not imply the required total contact length.
- Proportional first normal forms need only have a rational quotient. The
  quotient can have poles at vertical order jumps; do not use the
  \(g_1=z^2f_1\) normalization or the \(e\le3\) list without first proving
  regularity.
- The type-B quotient coordinate moves; never reuse the frozen-frame script.
- P-037 excludes multiplier degrees through three; P-039 shows that
  degree-four conormal rank one is insufficient. Do not call this
  non-quasi-cyclicity.
- In split-sextic mate relations, retain the positive common scale \(k\).
  From \(4k[\Gamma]=0\) or \(10k[\Gamma]=0\), never cancel \(k\) in a
  potentially torsion local class group.
- P-012 was independently audited within this run, including characteristic
  two, but has not received external peer review.
- The old “primitive-triple exceptional locus” question is stale: P-010 closes
  it for every characteristic-zero smooth rational quartic.

## 15. Files and sections to read first

Read in this order:

1. `research/SUCCESSOR_HANDOFF.md` — this frontier map.
2. `research/RESEARCH_REPORT.md` — synthesis and epistemic ledger.
3. `research/RESEARCH_RECORD.md`:
   - problem reconstruction and claim table;
   - P-010 through P-043;
   - failed approaches and open questions.
4. `research/LITERATURE_LEDGER.md` — checked source scopes.
5. `research/computations/README.md` — exact verifier boundaries.
6. The durable endpoint, boundary, and corner verifiers under
   `research/computations`.
7. `research/scratch/degree6/verify_mixed45_reduction.py` — conditional
   regular-ratio ambient \((4,5)\) reduction.
8. `research/scratch/explore_quasi45_type_b.py` only as historical scratch;
   check its moving-frame assumptions before reuse.

All essential type-B formulas are copied into P-025 and the durable verifiers.
Do not use `/private/tmp/typeb_generic.py`.

## 16. Unresolved source-verification questions

- Has arXiv:2511.07589 acquired peer review or a revised theorem since the
  cutoff? Check before calling its broad affine claim established.
- The exact theorem number in Manolache's 1994 paper for the multiplicity-five
  display was not independently recovered; Boratyński's checked theorem proves
  the needed statement.
- No published source was located for the stronger all-quartic primitive-
  triple exclusion P-010; this is not a novelty proof.
- No published source was located for the family-wide positive-characteristic
  result P-012; literature search does not validate its proof.
- Current-open-status searches cannot rule out unpublished or newly indexed
  work after 2026-09-30.
- The full original ACM-curve proofs were not rederived; source chains and
  modern statements were checked.

## 17. Conservative continuation batches

The initial 64-agent wave exceeded the workstation's practical memory budget
and was interrupted by a computer crash. Do not recreate it. The sustained
safe envelope in this run was the primary plus at most seven read-only,
nondelegating workers, eight total. Use closed batches, monitor aggregate
memory rather than per-thread Activity Monitor entries, and reconcile
completed lanes promptly.

Recommended batches, in order:

1. exploit the audited multiplicity-six \((4,6)\) filtration; attack the
   smallest of the 15 remaining pole strata; and classify degree-four
   local-cohomology pairs outside P-043's excluded family;
2. analyze the three surviving split-sextic root partitions with the
   torsion-corrected mate relation; explore two-pencil Chow systems; and
   develop a singular-support normalization/conductor formulation;
3. generalize the positive-characteristic projection method; pursue
   Jaffe-sequence control; and independently audit any new exact eliminations
   before promoting them.

Every lane must return an exact statement, hypotheses, proof or certificate,
counterexample search, failure boundary, and reproducibility notes. Workers
must remain read-only; the primary alone reconciles the durable ledgers.

## 0a. Late 2026-10-05 e=2 correction

The full \(e=2\) quartic-carrier obstruction branch materially changes the
frontier. In characteristic zero the ambient stabilizer is
\(\mathbf G_m\times\mathbf Z/2\), and a genuine generic cross-section is
\[
A=x+az+z^2,\qquad B=1+bz+dz^2.
\]
The full cubic obstruction was computed exactly with strong cross-checks. The
\(b=0\) three-parameter family is excluded exactly, but the proposed universal
statement
\[
\Omega=0\Rightarrow\operatorname{Res}(A,B)=0
\]
is **FALSE**. For
\[
A=z^2-\tfrac12z+x,\qquad B=1-2z+x^{-1}z^2
\]
all five obstruction coordinates vanish, while
\[
\operatorname{Res}(A,B)=\frac{(4x-1)^2}{4x},
\]
so \(x\ne0,\tfrac14\) gives a basepoint-free primitive triple extending to a
primitive quadruple. A subsequent independent audit reconstructed this
surviving family's cubic obstruction directly from the pre-P-044 moving-coordinate
formal-neighborhood calculation and obtained \(\Omega=(0,0,0,0,0)\); it also
independently verified the displayed resultant. Thus this surviving family and
the falsification are independently verified.

Do not confuse this \(O(-5)\), \(e=2\) statement with the proved \(O(-7)\)
primitive-triple exclusion in P-010. No quartic carrier or STCI pair has been
constructed. P-046 now determines what an actual \((4,7),e=2\) carrier would
force: it is a globally primitive septuple. The next step is therefore to
impose quartic containment of the canonical \(C_3\) on the P-044 locus, not to
compute higher primitive jets indiscriminately. Also keep \(e=0\), \(e=1\),
equivariance, and the uniform local-cohomology route open.

See
[the dated e=2 note](notes/2026-10-05-e2-full-obstruction.md),
[the exact formulas](computations/e2_full4_obstruction_2026-10-05.txt), and
[the primitive-septuple note](notes/2026-10-05-e2-primitive-septuple.md).


## 0b. Late 2026-10-05 P-045 correction

P-045 closes the explicit P-044 survivor as a quartic-carrier candidate. For
\[
A=z^2-\tfrac12z+x,\qquad B=1-2z+x^{-1}z^2,\qquad x\ne0,\tfrac14,
\]
the canonical primitive triple \(C_3(x)\) lies on an irreducible cubic \(H_x\),
and
\[
H^0(I_{C_3(x)}(4))=H_xH^0(O(1)).
\]
Thus every quartic containing the triple is \(H_x\ell\), and the plane factor
prevents any septic mate from cutting out only the nonplanar \(C_0\).
Therefore the known P-044 survivor does not produce a \((4,7)\) STCI pair.

Do **not** infer that the whole \(e=2\) branch is excluded: the full
basepoint-free P-044 zero locus is not classified. P-046 now gives a stronger
structural restriction on genuine carriers: every characteristic-zero
\((4,7),e=2\) complete intersection supported on \(C_0\) is a globally
primitive septuple of type \(L=O(-5)\). Hence every genuine carrier gives a
basepoint-free P-044 zero **and** its actual quartic generator contains the
associated canonical primitive triple \(C_3\).

Accordingly the next \(e=2\) task is not unrestricted classification of the
P-044 zero locus and not higher primitive obstruction. First derive the general
quartic-containment incidence condition
\[
H^0(I_{C_3(A,B)}(4))\ne0
\]
in the moving \(e=2\) coordinates and intersect it with P-044. Only survivors
of that intersection merit higher-order analysis.

See \`notes/2026-10-05-p044-survivor-cubic.md\`,
\`notes/2026-10-05-e2-primitive-septuple.md\`, and
\`computations/verify_p044_survivor_cubic.py\`.
