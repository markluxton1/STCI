# Complement sections: independent mathematical and strategy audit

Date: 2026-10-31. Reviewer: independent worker
`/root/complement_topology_independent_review`; no nested delegation.
Scope: §§1–5 of the [source](2026-10-31-complement-sections-and-topology.md)
and the complement-related stopping decision. The later plane-normalization
selection has a separate reviewer and is not covered by this portion.

## State and verdict

**Scoped PASS.** No material defect remains in the reviewed source or
complement recommendation. The requested citation-scope corrections were
applied and checked in the final source. This is a provisional research
audit, not canonical promotion or an unrestricted STCI result.

Reviewed source SHA-256:
`ea0a96a7334c447d4e1082b5bcaf2fe8fa023262cdfec5862ad779ab8889ed4e`.

The complement exposition and overall stopping language in
[assessment §23](2026-10-31-unrestricted-strategy-assessment.md#23-the-continuous-section-problem-is-solvable-algebraic-realization-remains)
were also checked. The section's UTF-8 text, from its heading through the
end of the file at review, had SHA-256
`1af1bed761d84c9daad504937c6e0a5cc83b5beccaece229d7759e5838c21722`.
This fingerprint identifies the reviewed state; it does not expand this
review to the plane-normalization propositions explicitly excluded above.

## Independent reconstruction

The review reconstructed the arguments before the source draft, then
checked their preservation in §§1–5. The initial brief concerned smooth
rational curves; reconstruction established that rationality is unnecessary
for the section criterion. It enters only through the genus term in the
cohomology table.

1. **Gysin maps and torsion.** For a smooth connected complex curve C of
   degree d and genus g, the oriented real-rank-four normal bundle gives
   the displayed complement sequence. The pushforward from H0(C) to
   H4(P3) multiplies by d; the pushforward from H2(C) to H6(P3) multiplies
   by one, since a point pushes forward to a point. Hence H2(U)=Z,
   H4(U) fits into `0 -> Z/d -> H4(U) -> Z^(2g) -> 0`, and all other
   positive integral cohomology vanishes. The extension splits as groups
   noncanonically; h-squared generates its torsion subgroup.
2. **Complete continuous-section obstruction.** General position removes
   C from a nullhomotopy of a loop. A compact tubular-neighborhood
   complement gives finite CW type of dimension at most six. For the
   S3 sphere bundle of any complex rank-two bundle, the primary obstruction
   is c2. The two remaining obstruction groups are H5(U;Z/2) and
   H6(U;Z/2). Both vanish by the coefficient Bockstein sequence, not by
   an unsupported inference from rational cohomology. Simple connectedness
   removes local-coefficient ambiguity. This proves sufficiency as well
   as necessity. For O(a) direct-sum O(b), c2=ab h-squared, so the exact
   criterion is d dividing ab.
3. **Holomorphic realization.** Hartogs extension in local bundle
   trivializations glues uniquely across the codimension-two curve.
   Global holomorphic sections of O(n) on P3 are homogeneous polynomials.
   For positive a,b, absence of common zeros off C excludes a common
   hypersurface component and excludes an identically zero component of
   the pair. Projective intersection is nonempty and proper, and smooth
   connected C is irreducible, so the reduced support is exactly C.
   The continuous-to-holomorphic gap is therefore the actual equation
   problem; there is no further holomorphic-to-algebraic gap here.
4. **Nonsplitting is compatible with equations.** The maps `(F,G)` and
   `(-G,F)` give the asserted exact sequence. The two local right inverses
   differ by `(F,G)/(FG)`, producing the stated Cech class up to sign.
   Hartogs and positivity make Hom(O(a) direct-sum O(b),O) zero, so
   no algebraic or holomorphic retraction exists. This proves the
   extension class nonzero without claiming it obstructs successful
   equations. Continuous Hermitian orthogonal complementation does not
   produce an algebraic complementary line bundle.

## Primary-source and mechanism scope

- [Hatcher, Vector Bundles and K-Theory, §3.3 and Proposition 3.22](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf)
  supplies the section-obstruction framework and Euler-class identification.
  [Hatcher, Algebraic Topology, Chapter 4, p. 339](https://pi.math.cornell.edu/~hatcher/AT/ATch4.pdf)
  records pi4(S3)=pi5(S3)=Z/2. The source now includes both references;
  the vanishing of the resulting cohomology groups is proved in the note.
- [Asok–Bachmann–Hopkins, Theorem 7.1.1](https://arxiv.org/html/2306.04631)
  concerns a rank-r bundle on a smooth affine (r+1)-fold over an
  algebraically closed characteristic-zero field and splitting off a
  trivial direct summand. U is nonaffine because its regular functions
  are constant. On U the desired nowhere-zero section does not imply a
  direct summand. A positive-rank Jouanolou replacement also changes the
  dimension while preserving rank two; the theorem cannot simply be
  reapplied, and any separately obtained section requires actual descent.
- [Asok–Hoyois–Wendt, Introduction and Theorem 4.2.10](https://msp.org/gt/2018/22-2/gt-v22-n2-p11-s.pdf)
  compares naive A1-homotopy classes of morphisms with motivic homotopy
  classes under the stated smooth-affine-source and target hypotheses.
  The review requested this precise wording in place of identifying
  actual maps themselves with homotopy classes; the final source and
  assessment incorporate it. The algebraically closed field hypothesis
  of the preceding splitting theorem was also made explicit. These
  corrections do not change the nonaffineness or descent conclusion.

## Geometric meaning and stopping decision

The actual object measured is the S3 bundle of nonzero directions in
O(a) direct-sum O(b) on the complement. Its continuous section problem
is completely solved by degree divisibility. A holomorphic section would
already supply the desired global equations, while their necessarily
nonsplit extension explains why an affine direct-summand theorem answers
a different question here.

The complement recommendation is supported: do not compute further
classical section obstructions for bundles whose continuous sections
have been proved to exist, and do not infer actual section descent from
an affine replacement alone. This does not exhaust enriched motivic
information, carrier-dependent topology, or all complement constructions.
A specified new section construction, strict descent mechanism, or
algebraic obstruction may be explored without requiring its success in
advance. The fixed-quartic characteristic-zero STCI question remains open.

Assessment §23 preserves these limits: it distinguishes completion of
this section problem from exhaustion of all topology, and an unproved
new mechanism from a bare reformulation. Its complement-related decision
not to start another Euler or secondary-section calculation is accepted.
The general requirement to specify added global input and a stopping
condition is also accepted; the separate plane selection requires its
own review evidence.

No proof certificate or numerical computation was required or run.
No carrier classification, new defining pair, or canonical promotion is
claimed. This review supplies evidence for the stated propositions and
bounded stopping decision, not evidence favoring unrestricted nonexistence.

## Separate plane-normalization selection review

Date: 2026-10-31. Reviewer: independent worker
`/root/plane_descent_strategy_review`; no nested delegation. Scope:
the plane-normalization paragraphs and their stopping recommendation in
[assessment §23](2026-10-31-unrestricted-strategy-assessment.md#23-the-continuous-section-problem-is-solvable-algebraic-realization-remains),
in the section state fingerprinted above. This appendix does not review
the complement theorem or expand the preceding reviewer's scope.

**Scoped PASS.** The assessment preserves the restricted scope of the
known arithmetic plane source and tested variation. Their exclusions do
not exclude all four quartics extending the marked line series.
[R-0004](../results/projection_phase_reduction.md) already retains full
phase and nilpotent-conductor descent under its admissibility hypotheses;
it does not compute the actual surviving phase image. The reviewed
[pinching assessment, §16](2026-10-31-unrestricted-strategy-assessment.md#16-pinching-abstract-supported-sections-and-the-marked-projective-image)
supplies the prior Ferrand pushout/descent evidence: abstract supported
sections are real constructive input, but do not furnish the prescribed
four sections or guarantee descent through their actual projective image.
That earlier primary-source audit is reused here, not independently
repeated. A reduced point pairing omits necessary infinitesimal gluing.
The assessment's invocation of Kollár's finite relations is likewise not
used as a theorem producing the prescribed ambient realization.

The ambient-symmetry lemma was independently reconstructed. For a
birational map f:P2→P3 given by degree-d forms, suppose one nonidentity
sigma in PGL3 satisfies f=f composed with sigma on a reduced divisor D.
Every crossminor F_i(F_j composed with sigma) minus
F_j(F_i composed with sigma) has degree 2d and is divisible by the
reduced equation of D. If deg D>2d, all minors vanish identically;
composition with a rational inverse then forces sigma to be the identity.
Thus deg D≤2d, giving eight for quartics. Geometrically this bounds the
divisorial coincidence locus for one ambient symmetry; it does not
construct a conductor. The multiplicity-weighted conductor class 51L
does not give this reduced degree. Degrees cannot be summed for
components paired by different automorphisms, and a conductor deck map
need not extend to P2. All these limitations survive in §23.

The discarded local phase refinement also has a valid conditional
form. On a smooth conductor branch different from L=(z=0), suppose a
cyclic automorphism of order e fixes p on L and acts on its cotangent
line by a primitive root xi. Choose F_i nonzero at p and set
q=z^4/F_i on the branch; if ord_p(z)=k, then ord_p(q)=4k. If q^b is
invariant, (sigma*q/q)^b=1 in the branch function field, so the quotient
is a constant root of unity. Leading terms give sigma*q/q=xi^(4k),
whose order e/gcd(e,4k) divides b. This conditional local corollary
does not supply the action, global compatible sections, admissibility,
or nilpotent descent. It is retained as a scope check within the existing
phase criterion, not as a new research lane or promoted result.

The nonselection is supported: no new marked plane projection or mate
was supplied. Stop the proposed inertia or ambient-symmetry classification;
reopen for specified global sections or compatible pinching/projection
data with a mechanism for actual full power descent. Such a mechanism
may be unproved when selected for a bounded test. These source limitations
do not favor unrestricted nonexistence. No calculation, new construction,
canonical promotion, or complement-proof review is claimed by this appendix.
