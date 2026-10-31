# Independent audit: marked absorption and ambient nef redundancy

Date: 2026-10-31. **PASS within the scopes below; independently reviewed
provisional deductions, not canonical promotion.** The unrestricted
characteristic-zero STCI question for
\(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\) remains open.

The reviewer worked independently of the source producer, read INDEX then
MAP, checked the primary literature, and reconstructed the material
implications. No nested delegation or new computational campaign was used.
Only this audit was written by the reviewer.

## 1. Reviewed state and disposition

The reviewed artifacts are:

- [Marked embeddings through absorption deformations](2026-10-31-marked-absorption-deformations.md),
  §§1–5, including the actual-pair and field-transfer additions in
  §§3.1–3.2.
- [Unrestricted strategy assessment](2026-10-31-unrestricted-strategy-assessment.md),
  §14 only, including the ABCH calculation and corrected selection.
- The existing [full tropical construction](2026-10-31-tropical-descent.md),
  §§1–3, and [moving-family control](2026-10-31-moving-family-descent.md),
  together with the inherited [equation-lifting interface](2026-10-27-absorption-formal-lifting-interface.md),
  §§3–4, and [relative liaison interface](2026-10-28-residual-liaison-construction.md),
  §§2–2.1. These supplied bounded inputs; their entire inherited research
  records were not re-audited.

Reviewed working-tree state: 2026-10-31, based on Git HEAD
`ffe97dae929a12089e36694b20418a209b843240`, after the source's final
limits citations and review-status edits. SHA-256 of the source text
from `## 2.` up to, but excluding, `## 5.`:
`af101d8aea02155a3c5b6d9168141fd8fbc2808f846fc51bc5cabe036f638ae3`.
SHA-256 of assessment §14 through end of file:
`159687cbf14d15d0f8724398374bf40e8f2cfba2464fe0ecf6c3f60fac99f9bd`.
Header/status/audit-link updates do not change the mathematical scope
of this review.

**Disposition.** The marked map-lifting lemma, prescribed-ribbon
coalescence, sufficiently-high-degree actual-pair corollary, full-primary
identification, characteristic-zero existence transfer, and uniform
endpoint cohomology formula pass. No unresolved material mathematical
finding was identified in those claims. The initial blanket stopping
inference from “abstract deformation” to “missing projective embedding”
was rejected and corrected. The resulting positive construction is
substantive, but does not provide an STCI endpoint or an iterative
residual-elimination operation.

## 2. Marked lifting and its algebraic realization

The general lemma requires a locally Noetherian base, a proper flat
finitely presented source, a flat closed distinguished \(C\times S\),
and a given central closed immersion compatible with the fixed map on
\(C\). These hypotheses are present in the source.

For a small extension \(A'\to A\) with kernel \(K\), the ideal of
\(\mathcal X_A\cup\mathcal C_{A'}\) inside \(\mathcal X_{A'}\) is
\[
(K O_{\mathcal X_{A'}})\cap\mathcal J_{A'}
=K\mathcal J_{A'}=K\otimes_k J.
\]
The first equality uses flatness of the distinguished quotient; the
identification uses flatness of its ideal. Thus fixing the marked map
changes the lifting sheaf to \(i^*T_{\mathbf P^3}\otimes J\), rather
than leaving the unmarked tangent sheaf. Local lifts into the smooth
target differ by derivations with these coefficients. Their Čech
class vanishes under the stated \(H^1=0\) hypothesis, at every small
extension, including after a residue-field extension. This reconstructs
the claimed sufficient criterion.

The passage to an algebraic family is also supported. Relative Mor is
algebraic and locally of finite presentation by
[Stacks 0D1C](https://stacks.math.columbia.edu/tag/0D1C).
The fiber specifying the marked map has the same local property.
The pointwise Artin criterion
[0APN](https://stacks.math.columbia.edu/tag/0APN) gives smoothness there;
an étale chart and a smooth local section through the specified point
give an actual family. The closed-immersion locus is open by
[05XA](https://stacks.math.columbia.edu/tag/05XA). The deformation
groups agree with [08U8](https://stacks.math.columbia.edu/tag/08U8).
No convergence assertion about formal series is being substituted for
these representability steps.

## 3. The ribbon application retains the specified embedded curve

Drézet's checked [full text](https://arxiv.org/html/1409.4175v3#S3.SS2),
Proposition 3.2.6 and Theorem 3.2.7(ii), supplies the global ribbon
deformation for a reduced effective divisor of distinct points. The
broader nonzero-section criterion is local in part (i). Section 2.4.4
does glue ample line bundles; it does not itself prescribe the four
sections of this embedding. The stronger wording on the arXiv landing
page is not needed here. The paper is stated over \(\mathbf C\), and
its higher-multiplicity discussion is not used as a general existence
theorem.

The three syzygy columns in the source have signed maximal minors equal
to the four parametrizing monomials and rank three everywhere on
\(\mathbf P^1\). Consequently the restricted Euler sequence gives
\[
T_{\mathbf P^3}|_{C_0}=O(5)^{\oplus2}\oplus O(6).
\]
For a given embedded ribbon with ideal \(J=O_{\mathbf P^1}(-d)\),
the marked lifting sheaf is supported on the reduced curve and has
\[
h^1=2\max(d-6,0)+\max(d-7,0).
\]
It vanishes throughout \(0\le d\le6\), including the endpoint
\(d=6\). This is a geometric statement about extending maps with a
fixed component, not a classification of all multiple structures.

The chosen total-space component of Drézet's family is closed and flat;
base change of that closed immersion gives the reduced
\(C_0\hookrightarrow W\). Its smooth rational-curve family becomes
\(\mathbf P^1\times S\) étale locally, with the central identification
prescribed, since \(H^1(T_{\mathbf P^1})=0\). It therefore supplies the
actual distinguished family required by the marked lemma. For \(d=0\),
the split ribbon and the explicit family \(z(z-t)=0\) handle the case
without extending the positive-divisor theorem silently.

The resulting fibers have degree eight and arithmetic genus \(d-1\).
Each moving component has degree four by flatness of its polarization,
and its intersection with the fixed quartic is the actual reduced
\(d\)-point scheme, not merely a numerical intersection count.

## 4. Actual equations, full primary structure, and field transfer

The addition of two equations is valid at sufficiently large fixed
twists. Relative vanishing and generation lift chosen central forms.
One can choose the central pair proper and generating the ribbon ideal
at \(\eta_C\): global generation gives independent generic conormal
classes and leaves no surface base component.

Flatness and the central lci property make the embedded family a regular
codimension-two immersion near the central fiber; properness permits a
base shrink. The determinant of the two lifted conormal classes is
nonzero on a central open. Its nonvanishing locus on each smooth
component family maps to an open neighborhood of the base point.
Therefore generic ideal generation holds on both nearby components.
Upper semicontinuity of projective fiber dimension preserves properness
of the pair, and the fiberwise regular sequences give a flat CI family.
This does not assume flatness of extracted primary components.

Generic equality with \(I_W\) identifies the entire central
\(C\)-primary component. A pure ribbon with sole irreducible support
has no embedded associated points, so its ideal is the contraction of
its localization at \(\eta_C\). This proves the stronger scheme
identification, rather than inferring it from multiplicity alone.

Thus the cycles are
\[
[Y_0]=2[C]+R_0,\qquad [Y_t]=[C]+[C_t]+R_t,\qquad
\deg R_0=\deg R_t=ab-8.
\]
The full residual relative to the fixed \(C\) loses exactly four units
of degree. Extra residual attachment may meet these curves or their
nodes. The source correctly does not identify \(d\) with the entire
CI residual attachment, assert smooth residuals, or assert flatness of
full-primary extraction. Its use of once-linking invokes the existing
relative liaison result in its stated scope.
Assessment §14's asymptotic caution is supported by the same identity:
increasing \(ab\) leaves this operation's absorbed degree equal to four,
while the remaining residual degree is \(ab-8\). Twisting alone does
not make that residual fraction tend to zero.

The added field transfer was separately reviewed. The given embedded
ribbon descends to a finitely generated characteristic-zero field
\(k_0\). The complex witness, including its marked section and central
identification, has a finite-presentation model over a finitely
generated \(k_0\)-algebra. These data and identities descend by
[Stacks 01ZM](https://stacks.math.columbia.edu/tag/01ZM);
the morphism properties descend at a finite level by
[§32.8](https://stacks.math.columbia.edu/tag/081C) and properness by
[081F](https://stacks.math.columbia.edu/tag/081F).
The smooth relative base curve and its noncentral locus, and the
finite étale reduced attachment away from its marked section, can be
retained. A closed point has residue field finite over \(k_0\), which
embeds in the original algebraically closed field over \(k_0\).
Specialization therefore retains the prescribed central ribbon. This
is a valid existence transfer; it does not attribute a wider verbatim
field statement to Drézet or embed the whole original field in
\(\mathbf C\).

## 5. Endpoint formula and the justified stopping boundary

For the conditional proper CI endpoint, put \(c=a+b-4\) and
\(E=T_{\mathbf P^3}|_Z\). ACM and adjunction identify the dual Euler
cohomology map with the surjective coordinate multiplication
\(R_{c-1}^{4}\to R_c\). Hence
\[
h^0(E)=15,\qquad h^1(E)=4H_R(c-1)-H_R(c).
\]
These are ambient projective vector fields. Restriction to \(C_0\)
is injective: a matrix having every curve point as an eigenline must
be scalar, by irreducibility and nondegeneracy. Since the restricted
tangent bundle has \(h^0=19\) and \(h^1=0\), the exact sequence with
the ideal of the marked curve gives
\[
h^1(E\otimes I_{C/Z})=4+4H_R(c-1)-H_R(c)
=19+ab(3c/2-4)>0.
\]
The equality also follows independently from
\(\chi(E)=ab(4-3c/2)\). Positivity holds for \(a,b\ge5\).
The source's extension replacing 19 by \(4e+3\) for a nondegenerate
smooth rational curve of degree \(e\) follows from its Euler sequence
and the same argument.

This nonzero group is not a nonzero obstruction class and does not
prove singularity or nonsmoothness of a marked Hom space. It proves
only that the sufficient vanishing shortcut does not certify these
endpoints. The corrected selection retains actual prescribed-ribbon
partial absorption and stops without claiming iteration to STCI.

## 6. Ambient Hilbert-scheme calculation in assessment §14

The checked [ABCH paper](https://arxiv.org/pdf/1203.0316), Theorem 2.4,
Proposition 3.1 and Corollary 3.2, gives the ambient divisor basis and
nef rays. For the actual full finite-flat tropical family, including
its nonreduced structure, the tautological bundle pulls back to its
algebra \(B\): \(O(k)\) is trivial on the fixed affine chart. Its
determinant has degree \(+e\), not \(-e\), and fixed support gives
\(f^*H=0\). Therefore every ambient nef divisor has degree
\(\beta e\ge0\), redundant with the inherited \(e>0\).

The boundary half-class has degree \(-e\); its section vanishes
identically on this family, so no negative effective-divisor
contradiction follows. Small-degree Grassmannian maps may be rational;
the calculation uses the determinant line-bundle class instead. The
characteristic-zero numerical conclusion transfers by finite-data
descent and field extension. No assertion about every intrinsic
punctual-Hilbert or marked equation-incidence inequality was proved.

This calculation supports stopping the ambient nef-divisor application.
The positive marked construction supports correcting the earlier
blanket stop on abstract deformation. Neither disposition settles the
unrestricted characteristic-zero STCI question, and no canonical
record is promoted by this audit.
