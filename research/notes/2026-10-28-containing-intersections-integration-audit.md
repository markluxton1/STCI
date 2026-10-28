# Independent integration audit: containing intersections and residual constructions

Date: 2026-10-28. Reviewer: `blowup_linear_systems` research agent.
Reviewed outputs:

- [Integrated synthesis](2026-10-28-containing-intersections-synthesis.md).
- [Literature and repository refresh](2026-10-28-containing-intersections-literature.md).
- The four linked source notes and their separate audits: normal jets and
  prescribed attachment, residual liaison, two-projection geometry, and
  prescribed singular carriers.

**Outcome: PASS for the integrated mathematical interpretation and proposed
next experiment, within all stated scopes.** No canonical promotion or
unrestricted STCI conclusion is supported or claimed. This integration review
is independent of the synthesis author. I authored the blowup source and
therefore use its separate independent audit for that lane rather than
assigning it a new self-review status here.

## 1. Scope and authority remain visible

The synthesis consistently fixes the embedded quartic, distinguishes
algebraically closed characteristic zero from the explicitly complex
Noether–Lefschetz applications, and preserves the any-field scope of the
ideal-sheaf-power cohomology lemma. It labels the inherited general-pair
and cubic-graph geometry as reviewed provisional premises and R-0020 as a
promoted premise. The table of different parameter spaces is essential:
generality among forms through reduced \(C\) is not generality among forms
through an ordinary thick neighborhood or a prescribed singularity base.

The all-divisor construction is stated only in its sufficient range
\(a,b\ge7\). Its concentrated-contact example has the right numerical
invariants: residual degree 45, genus 205, boundary length 42. It is an
existence result with actual equation lifts, without a claim that a rational
coefficient list was exhibited. The synthesis does not turn a finite jet
lifting theorem into fixed-degree all-order compatibility or two-generator
presentation of a full primary ideal.

## 2. Additional independent reconstruction of relative linkage

I independently checked the later §2.1 of the
[liaison source](2026-10-28-residual-liaison-construction.md), which must not
be justified by the earlier theorem about flat *full* primary families.
The source's argument instead uses the fixed reduced curve and is valid
when the once-linked curve acquires that curve as a component.

Locally over a locally Noetherian base \(T\), both \(C_T\) and the
fiberwise proper complete intersection \(Y_T\) are relative regular
immersions of codimension two in the flat ambient \(\mathbf P^3_T\).
Fiberwise regularity of the two equations gives flatness of the relative
Koszul quotient. For the nested closed immersions, derived change of rings
identifies

\[
R\mathcal Hom_{Y_T}(\mathcal O_{C_T},\mathcal O_{Y_T})
\cong
\omega_{C_T/T}\otimes\omega_{Y_T/T}^{-1}|_{C_T},
\]

concentrated in degree zero. One can see this directly by computing
ambient Koszul duals: each codimension-two regular sequence contributes
the same shift by two, which cancels. This argument does not require
\(T\) to be regular or reduced. The Koszul constructions and their
evaluation morphism are compatible with arbitrary locally Noetherian
base change.

Evaluation at one identifies this Hom module with the annihilator ideal
inside \(\mathcal O_{Y_T}\); its quotient is the colon-defined
\(\mathcal O_{D_T}\). The first two terms of the resulting exact sequence
are \(T\)-flat. After every geometric specialization the evaluation map
is still injective, since a homomorphism from a cyclic quotient is
determined by the image of one. The local flatness criterion then gives
flatness of the quotient. Tensoring the exact sequence and repeating
the same duality calculation identifies its base change with the new
colon ideal.

At \(\eta_C\), the fiber's zero-dimensional complete-intersection
algebra is Gorenstein and its socle has dimension one over \(k(C)\).
Linking to reduced \(C\) removes this one-dimensional socle, subtracting
one from the generic multiplicity. Off \(C\), the colon changes no curve
component. Thus

\[
[D_t]=(m_t-1)[C]+R_t
\]

holds as an actual cycle statement, and the once-linked curve remains
flat through a multiplicity jump. This supplies the exact missing family
justification. It does not make extraction of the full primary component
flat or compatible with specialization. The synthesis keeps those two
operations separate.

## 3. The global reinterpretations are not overextended

The synthesis's low-equation recovery concerns the embedded once-linked
curve in the stated bidegrees. It does not infer a direct link to the
fixed partner from numerical invariants, an abstract isomorphism class,
or arbitrary Hilbert deformations. Its use of Kleppe's established theorem
is tied to the explicit source resolution and characteristic-zero locally
Cohen–Macaulay hypotheses. The distinction between the Hilbert scheme and
the fixed-partner incidence is retained.

The two-projection section dictionary remains a statement about actual
global sections and ideal sheaf powers. The synthesis retains the graph
criterion \(R=0\iff\operatorname{Supp}W\subset E\). It explicitly rejects
the weaker image condition in \(\Sigma\), so it does not lose residual
trisecants contracted by the other projection or manufacture residual
curves from fibers exceptional over \(C\). The full conductor assertion
for \(\Sigma\) has independent reconstruction in the blowup audit.

The prescribed A-type carrier construction is complex and sufficiently
high degree, with a marked local class generator. The residual class
cancellation and the distinct local attachment lengths one and \(m\)
are accurately summarized. The very-general free class group on that
specified family is not transferred to every high-index carrier.

## 4. Literature and future direction

The literature refresh accurately distinguishes source access and theorems
actually used from an originality claim. The Fano model was found both in
the repository and in primary literature before its new application.
The October 2026 Brevik–Nollet result retains its smooth complex ambient
threefold, \(H^1(\mathcal O_X)=0\), smooth connected curve, ordinary ideal
power, and very-general sufficiently-high-degree hypotheses. Its conclusion
is about Picard groups of nonnormal surfaces; neither the synthesis nor
the refresh turns it into a computation of all almost-Cartier divisors or
an unrestricted STCI exclusion.

The proposed next experiment follows the new deductions: a family in the
fixed-partner liaison incidence supplies a flat once-linked object through
absorption; the conic section dictionary supplies actual equations in a
second global presentation; the graph records which components enter
\(E\); fiberwise primary extraction recovers the genuine residual. The
experiment is explicitly still to be constructed. Its statement does not
pretend that flatness proves an absorption locus is nonempty or that any
contact concentration forces generic thickness to grow.

No substantive integration correction was required. Final delivery should
verify the linked validation README and generated evidence paths after
they have been written; mathematical scope is not inferred from those
navigation links or from successful finite checks.

Root delivery addendum: the linked validation README and generated JSON/log
now exist. The final sweep checked 382 local Markdown targets in 20 files
with zero missing targets, canonical metadata reports 37 records with zero
errors, and the tracked/new text whitespace checks pass. This closes the
delivery check above without changing the review's mathematical status.
