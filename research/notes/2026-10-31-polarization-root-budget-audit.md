# Independent audit of the polarization-root and residual-budget note

Date: 2026-10-31. Reviewer: fresh `gpt-6.1-sol/high` worker.
Status: **the preserved provisional deductions pass within their stated
scope after one corrected affinization statement**. No canonical promotion,
unrestricted STCI conclusion, residual-degree inequality, or new construction.

## 1. Reviewed artifact and boundaries

This audit covers [the preserved note](2026-10-31-polarization-root-budget.md),
Sections 1–5, including the explicit trace pairing (3), restriction-boundary
interpretation (5a), uniform linear-series statements (6), and the existing
twisted-cubic calculation (7). It was checked against the actual draft,
then the corrected affinization paragraph and added (5a) were inspected.
Subsequent status-only edits do not change the mathematical state covered.
The actual recommendation and residual-budget interpretation in
[the strategy assessment, Section 12](2026-10-31-unrestricted-strategy-assessment.md#12-arbitrary-pair-roots-and-the-limits-of-a-residual-budget-interpretation)
were also inspected. They preserve the same scopes, distinguish the
twisted-cubic control's zero invariant defect from the quartic defect,
and make no additional mathematical claim requiring a separate proof.

The setting is the fixed embedding
\(C_0=[s^4:s^3t:st^3:t^4]\), algebraically closed characteristic zero,
and a hypothetical proper complete intersection with reduced support
exactly C0. The inherited degree restriction uses
[R-0001](../results/quartic_carrier_exclusion.md) and its stated factor
reduction; those accepted exclusions were not reproved. The broader
proper-intersection problem with residual cycle R is a separate scope.
No nested delegation, classification, numerical campaign, or other file
change was undertaken by this reviewer.

## 2. Root and module arguments

The unit sequence, logarithm, lifting of constants, and vanishing of
\(H^2(J)\) give the claimed exact sequence of abelian groups. Its kernel
is uniquely divisible by four, giving exactly one isomorphism class of
the fourth root with reduced degree one. This does not canonically choose
the fourth-power identification and does not imply any sections exist.

The full section modules retain all integer twists. Their positive tails
are finite over B, and their negative tails vanish by Serre duality and
Serre vanishing. Their full-section construction kills zeroth and first
local cohomology at the vertex; off the vertex the corresponding sheaves
are invertible. Thus their MCM property, and the finite CM root algebra,
are justified rather than inferred from a blanket ascent assertion.
The sheaf/section-module correspondence does not require reducedness;
see [Stacks, Section 28.29](https://stacks.math.columbia.edu/tag/01QG).

The proof correctly uses B's CI resolution to identify its full
hyperplane section ring with its embedded coordinate ring, including
vanishing at negative hyperplane twists. It does not use that equality
for an arbitrary primary component of a larger intersection.

## 3. Nonreduced duality and grading

The map on punctured line bundles is a fourth-power map, finite étale
over the nonreduced base in characteristic zero. The functional
\(t=4\operatorname{pr}_{A^{\mu_4}}\) defines an actual homogeneous
pairing globally. It is the perfect trace pairing on the puncture.
Both source and target are MCM B-modules, the latter by Gorenstein
duality over B; depth two extends their sections across the vertex.
This proves (3), hence finite duality proves (4).

This is the required repair to an earlier imprecise reflexive-extension
shortcut. No normal-domain theorem is being imported for nonreduced B.
With \(B_q\) placed in A-degree 4q, the canonical shift is 4c; in B's
original standard grading it is c. The note preserves this distinction.
The normality assumptions in
[Tomari–Watanabe](https://www.jstage.jst.go.jp/article/kodaimath1978/24/3/24_3_436/_pdf/-char/en)
do not supply an additional theorem about this root algebra.

## 4. Vertex defect and uniform linear series

The nilpotent restriction kernel identifies the reduction with its image
in k[s,t]. Restriction is surjective in sufficiently large degrees,
so k[s,t] is the normalization and the quotient D has finite length.
Taking fourth-Veronese pieces gives the fixed quartic coordinate ring.
Its sole missing fourth-divisible degree is the middle monomial in
degree four; the elementary exponent-sum check for higher degrees is
correct. Formula (5a) follows directly from the cohomology sequence of
\(0\to J L^n\to L^n\to O_{C_0}(n)\to0\).

One material wording error in the reviewed draft was corrected: the
affinization of the smooth punctured plane is the plane and therefore
removes D. The corrected note says that the affine model
\(\operatorname{Spec}A_{\rm red}\) retains D, while affinizing its
puncture or normalizing the model removes it. The corrected statement
was inspected. This also correctly explains the failure of global
sections to commute with reduction in this setting.

For (6), every element \(\alpha s+\beta t\) of V1 has fourth power
with middle coefficient \(6\alpha^2\beta^2=0\). A vector subspace
contained in the union of the two coordinate axes lies in one axis.
For V2 the middle-coefficient pairing has nonsingular matrix in dimension
three and vanishes on V2 times V2; thus V2 is totally isotropic and has
dimension at most one. These assertions concern the images of sections.
Neither nonzero images nor bounds on all nilpotent sections follow.

Geometrically D measures a section-extension obstruction through the
nilpotent structure and is supported at the cone vertex. Formula (5a)
does not identify it with an attachment length or a residual component.

## 5. Existing ribbon control and strategy disposition

The inherited twisted-cubic equations define the actual proper (2,3)
CI with cycle twice the twisted cubic. Its two displayed charts give a
primitive ribbon with nilradical O(-5) and canonical polarization H.
The overlap and cube-root transition were independently reconstructed.
For M raised to the n-th power, the coefficient of each nilpotent term
is exactly \((n/3-j)u^{n-j-3}\). Polynomial corrections at zero and
exponents at most n-5 at infinity give no sections at n=1, exactly one
at n=2, and full reduced restriction for every n at least three. The
potential obstruction at n=3 has zero coefficient. Negative degrees
have neither reduced nor nilpotent sections.

Thus the normalization defect has dimensions two in degrees one and
two and vanishes elsewhere. The cube-Veronese defect vanishes. The
canonical-ribbon interpretation is consistent with
[Bayer–Eisenbud, Sections 4–5](https://www.math.columbia.edu/~bayer/papers/Ribbons_BE95.pdf).
This actual CI control proves compatibility of some root defects with
R=0. It does not realize the quartic's nonzero invariant defect, and
therefore does not disprove the possibility of a further theorem about
that particular equivariant defect.

The stopping recommendation was challenged against the stronger data:
the Gorenstein shift, fixed nonzero invariant defect, and restrictions
on V1 and V2 might be useful inputs. None of the preserved arguments
shows those inputs to be incompatible or forces a section they forbid.
There is also no constructed nilpotent extension with the required
four-generator, two-relation fourth Veronese. Accordingly the bounded
recommendation to stop the bare mechanism is supported. It is not a
claim that all future root-based work is impossible.

For a general proper CI with cycle \(ab=4m+\deg R\), its C0-primary
part retains the abstract root argument but need not retain the full
CI coordinate-ring identity or the same dualizing sheaf. No comparison
from D to \(\deg R\) has been established. The note correctly leaves
both absorption into C0 and a positive residual-degree floor unresolved.
Its new content is a provisional all-pair structural reformulation,
uniform reduced-section restrictions, and an exact boundary on the
inference that those facts currently support.
