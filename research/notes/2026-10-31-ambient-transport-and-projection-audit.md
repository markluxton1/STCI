# Independent audit: ambient transport and projection selection

Date: 2026-10-31. Reviewer: `ambient_selection_independent_review`.
Status: **scoped PASS for source §§1–2 and preservation of the selection
recommendation only**. The source is
[Ambient transport and a scheme-changing projection source](2026-10-31-ambient-transport-and-projection.md).
The review covers the sections headed “What the natural birational
transport can and cannot do” and “Global Cohen–Macaulayness is a
substantive compatibility condition” as inspected on this date. It does
not identify a whole-file hash: §4 was still in progress. Later changes
to these reviewed claims require proportionate re-review.

The reviewer independently reconstructed the mathematical deductions
below, checked their preservation in the source, and checked the stated
primary sources where specified. No nested delegation, file changes
outside this audit, CAS grid, or further research campaign was performed.
All new deductions remain provisional; this audit does not promote a
canonical result or change the unrestricted STCI status.

## 1. Single-blowup birational transport

**Exact scope.** Work over an algebraically closed field of characteristic
zero with C=[s4:s3t:st3:t4]⊂P3 and B=Bl_C(P3). The claim concerns every
birational morphism B→P3, with no bound on its originating rational-map
degree. It excludes a nontrivial Cremona transformation resolved by this
single reduced-curve blowup alone. It does not exclude transformations
requiring further centers or another resolution.

[Cheltsov–Przyjalkowski–Shramov, Lemma 6.13](https://arxiv.org/html/1809.09223v1#S6.L13)
was checked directly. Its proof identifies the common blowup of a conic
in V5 and a smooth rational quartic in P3, and explicitly gives this
quartic's parameterization. The deduction in the source uses this
geometric contraction, rather than treating the lemma as an already
stated theorem excluding Cremona transformations.

With H the plane pullback and E exceptional, L=3H−E is the second
hyperplane pullback. H,L are an integral basis, since E=3H−L. The two
contractions give the distinct nef boundary rays. Independently,

    H³=1, H²E=0, HE²=−4, E³=−14,
    (3H−E)³=27−36+14=5.

For a birational morphism ρ:B→P3, D=ρ*O(1) is integral, nef and has
D³=1. An ample D would make ρ finite; a finite birational morphism to
the normal P3 is an isomorphism, contrary to Picard rank two. Hence D
is on a boundary ray. Integrality gives D=nH or nL for an integer n>0.
The cubes force D=H, and h0(B,H)=4 forces ρ to be the original blowdown
followed by a projective automorphism. **PASS within this exact scope.**

Geometrically, the natural blowup offers a genuinely different target
V5, but supplies no second contraction back to P3 that could itself
provide a new supported pair. An added-center proposal must still
specify its equations and boundary behavior. No classification of
such proposals follows from this calculation.

## 2. Explicit Cremona control and its actual residual curves

For Φ=[ab:b²:ac:ad] and Ψ=[y0²:y0y1:y1y2:y1y3], direct composition
gives ΨΦ=ab²[a:b:c:d] on its dense domain, and the other composition
is likewise the identity as a rational map. On C, canceling s4t from
the displayed coordinate forms gives [s3:s2t:st2:t3]. Substitution
independently verifies

    Φ*Q=b f0,       Φ*G=a² h0,
    f0=a²c−b³,     h0=ac³−2b²cd+abd².

The target pair is supported on the twisted cubic with generic
multiplicity two: on y0=1, Q gives y2=y1² and G becomes
(y3−y1³)²; the y0=0 boundary adds only the endpoint.

For the source intersection after full surface-factor removal, the
generic lengths were reconstructed independently:

- On ab≠0, f0 gives c=b³/a², and
  h0=(b/a⁵)(a³d−b⁴)². The coefficient is a unit at the generic point
  of C, so its intersection multiplicity is two.
- At ℓ=(a,b), c,d are generic units. The equation h0 solves
  a=(2d/c²)b²+O(b³), so f0=−b³+O(b⁴). The length is three.
- At M=(b,c), a,d are generic units. Modulo f0, c=b³/a² and h0 is
  b times a unit. The length is one.

The cubic f0 is primitive and irreducible as a polynomial linear in c,
and h0 is not divisible by it; thus the intersection is proper. The
cycle degrees 2·4+3·1+1·1=12 exhaust its Bézout degree. This confirms
the full cycle 2[C]+3[ℓ]+[M], with no omitted curve component. This is
a cycle assertion, not a claim that the full intersection scheme is
the disjoint union of those components.

In the chart d=1 the parameterization is [r4:r3:r:1], so ℓ is the
tangent at p_infinity. M joins the two endpoints. These are genuine
residual curves downstairs, rather than exceptional vertical cycles.
Removing exceptional surface factors has not removed their support.

The inherited cubic exclusion is explicitly recorded in the
consequences of [STCI-R-0001](../results/quartic_carrier_exclusion.md).
This audit checks its applicability to the irreducible f0; it does not
rerun the accepted cubic theorem. Therefore no replacement mate while
retaining f0 can produce an STCI. **PASS.** Neither this control nor
the single-blowup theorem excludes arbitrary Cremona transports.

## 3. Global CM and AG compatibility boundaries

The following deductions in source §2 were independently checked.

**Historical question.** The reviewer directly checked
[Singh–Walther, Example 3.5 and Question 3.6](https://www.math.purdue.edu/~walther/research/pure.pdf).
The example is exactly the four-generator algebra
k[s4,s3t,st3,t4]. In characteristic zero, the question asks for an
ideal with the same radical and Cohen–Macaulay quotient, without
requiring that ideal to be homogeneous. This supports the historical
attribution. It does not establish that no later solution exists.
The source's reported focused-search outcome remains a search
limitation, not mathematical proof of current status or an exhaustive
literature review. The source preserves this distinction.

**AG in the actual P3.** A codimension-two arithmetically Gorenstein
curve has a perfect height-two ideal of type one. Hilbert–Burch gives
two minimal ideal generators, hence a complete intersection. ACM alone
does not imply this, and local Gorensteinness is not the required
arithmetical condition. **PASS.**

**Isomorphic linear projection.** A scheme spanning PN, N>3, has at
least N+1 independent coordinate sections of O(1). An isomorphic linear
projection to P3 preserves this polarization. The image, containing
the nondegenerate C, has no linear ideal equation, and the restriction
sequence gives h1(I_Y(1))≥N+1−4>0. Thus it is not ACM. This argument
does not require the source to be AG. The source explicitly excludes
nonisomorphic scheme-changing projections from this conclusion.
**PASS for the mathematical implication.** The specific
Notari–Ojeda–Spreafico theorem-number and ambient-space attribution
was supplied by the completed primary-source scout; this reviewer did
not separately recheck those theorems.

**Canonical idealization.** For a local ring (A,m) and nonzero finite
module K, the maximal ideal of A⋉K is m⊕K, whose square is m²⊕mK.
Consequently

    edim(A⋉K)=edim(A)+dim_k(K/mK).

Nakayama makes the added summand positive. For an ACM cone of embedding
dimension four and K=ω_A, this is 4+type(A)>4, preventing an embedding
as a quotient of the fixed four-variable coordinate ring. Without CM,
the expression is 4+μ_A(ω_A), and one must not call the idealization
automatically Gorenstein. The source incorporates this correction.
**PASS.** This does not exclude nontrivial extensions or embedded
Ferrand constructions. The Manolache attribution is retained as the
completed scout's source evidence; this reviewer did not separately
recheck that paper.

The geometric content is that an abstract Gorenstein extension, a
locally Gorenstein multiple curve, and an actual AG curve in the fixed
P3 impose different conditions. None of these boundary arguments is
an exclusion of all embedded ACM or AG thickenings supported on C.

## 4. Selection recommendation: provenance and stopping conditions

The reviewer challenged the initial nonselection because an actual
scheme-changing projection of a specified AG complete intersection in
P4 retains reduced support automatically. It need not preserve the
source scheme, so the isomorphic-projection objection cannot discard
it. This is additional construction input beyond asking directly for
unknown equations in P3.

The resulting recommendation was a uniform analysis of the entire
positive-integer (u,v) family with the equation h kept to the first
power, using the saturation interface described in source §3. The
parent accepted and reported this choice before its uniform test.
Its stopping conditions were:

- A surviving ACM image would be checked for Gorenstein type.
- A uniform failure would close this specified source.
- Case-dependent computations without a general mechanism would stop
  the test, without an exponent grid or automatic expansion to powers
  of h.

This paragraph records the selection's scope and rationale. **It does
not independently certify the reviewer's own projection criterion,
module presentation, hand control, or any claim in source §§3–4.**
Those require the separate fresh reviewer assigned by the parent.
In particular no outcome of the ongoing uniform test is asserted here.

## Disposition

Source §§1–2 preserve the scoped deductions and the identified CM/type
wording correction. No established material finding remains open in
those deductions. The primary-attribution checks not separately
repeated here and the historical-search limitation are identified
above. Independent coverage of source §§3–4 remains pending a different
reviewer; this audit is deliberately not a whole-note acceptance.

## 5. Fresh independent review of the projection family and conductor obstruction

Date: 2026-10-31. Reviewer: `projection_conductor_proof_review`.
Disposition: **mathematical PASS for source §§3–5 within the exact scope
below**. This is a separate fresh review of the first reviewer's own
projection interface and the subsequently supplied uniform proof. The
preceding review is preserved unchanged. No nested delegation, exponent
grid, new CAS computation, or additional source family was used.

**Claim and hypotheses.** Over an algebraically closed field of
characteristic zero, put S=k[a,b,c,d], r=2bc−ad, T=S[z],
f=b²−az, g=c²−dz, and h=z²−r. For every pair of positive integers
u,v, consider the actual CI W_uv=Proj(T/(h,f^u,g^v)) and its finite
scheme image Y_uv under forgetting z. The audited conclusion is that
no Y_uv is arithmetically Gorenstein or a scheme-theoretic complete
intersection in the given P3. More precisely, u≥2 gives failure of
local Gorensteinness at p_a, and v≥2 gives the corresponding failure
at p_d; Y_11 is not ACM. This does not decide whether the common
reduced support C is STCI, whether another thickening containing Y_uv
is a CI, or whether images with (u,v)≠(1,1) are ACM.

**Source geometry and the deficiency interface.** Independently
eliminating a,d on z≠0 gives (z²−bc)²=0. The z=0 boundary adds
exactly the two endpoints. Thus the common support is the rational
normal quartic D, and the three equations have height three in the
five-variable polynomial ring, hence form a regular sequence. Their
degree-eight intersection has cycle 2D; the powers retain the same
support and regular-sequence property. The projection is finite because
z satisfies the monic quadratic h. Its reduced image is the fixed C.
This direct argument supplies the source construction without needing
the Torrente attribution, which this reviewer did not separately check.

The radical of S_+B is the full irrelevant ideal of B, since z²=r.
The dimension-two CI therefore has H⁰_(S_+)(B)=H¹_(S_+)(B)=0.
The inclusion A⊂B establishes saturation of the elimination ideal,
and the local-cohomology sequence establishes
H¹_(S_+)(A)=H⁰_(S_+)(B/A). Reducing modulo z²=r gives coefficient
relations (P,Q), (rQ,P), (R,T_v), (rT_v,R). Killing the first
module generator, which is the image A, leaves exactly

    B/A ≅ (S/(P,Q,R,T_v))(-1).

Thus the saturation criterion in source §3 is correct. It tests
arithmetical CM of this actual image, rather than asserting the
existence or exhaustiveness of general supported thickenings.

**Conductor and generic isomorphism on nilpotents.** The class of
p+qz lies in A precisely when q belongs to K=(P,Q,R,T_v). Multiplying
by z gives qr+pz, whose class lies in A precisely when p belongs to K.
Since 1,z generate B over A, the conductor as a B-ideal is therefore
KB=(Q,T_v)B. This argument is valid before assuming birationality and
is independent of representatives. On D away from the endpoints,
b²=az gives

    Q_u|D = −2^(u−1) a^u z^(u−1) ≠ 0.

Because Q_u is already in the conductor, its invertibility there
forces A=B, including the entire nilpotent structure. A statement
about only the reduced curve, or étaleness alone, would not establish
this required fact. The source supplies the stronger argument.
Locally along the projective curve, a parameter nonzero generically
on D is a nonzerodivisor on B and on A⊂B. Both rings are thus
one-dimensional CM, and the generic equality gives their common
total quotient ring. The image can still fail *arithmetical* CM at
the irrelevant vertex, consistently with the preceding criterion.

**Endpoint nonprincipality, including v=1.** On a=1, eliminating d
gives the displayed local CI in b,c,z with
f=b²−z and g=c²−2bzc+z³. For u≥2, specialization c=z=0 maps
Q_u to −u b^(2u−2), while T_v and g^v vanish and f^u maps to
b^(2u). The nonzero class in k[b]/(b^(2u)) survives endpoint
localization. Hence Q_u is not generated by T_v in B_p.

For the converse nonmembership, the identity
2zQ_u=(b²−z)^u−(b²+z)^u shows that the quotient R_u by f^u,Q_u
is Artinian local: both b²−z and b²+z are nilpotent, and hence b,z
are nilpotent. Neither defining polynomial has a linear term for
u≥2, so b remains nonzero in R_u. After substituting d=2bc−z²,
the j=1 term of T_v has c-leading coefficient −2v b and degree
2v−1; every larger odd j has smaller c-degree. This coefficient is
nonzero in characteristic zero. The polynomial g^v is monic of
c-degree 2v over the possibly nonreduced R_u. Consequently polynomial
division gives a nonzero remainder T_v, proving that T_v is not
generated by Q_u in B_p. The quotient by g^v is Artinian local,
with reduced support c=0, so this second nonmembership also survives
localization. These arguments include v=1; they do not omit that
boundary. By Nakayama the conductor has two minimal generators and
is not principal. Exchanging a,d and b,c treats every v≥2, including
u=1.

**Finite duality on nonreduced schemes.** The reviewer directly checked
[Stacks Tag 0AX0](https://stacks.math.columbia.edu/tag/0AX0): finite
duality transfers a dualizing complex for arbitrary Noetherian rings,
without a reducedness hypothesis. Under the hypothetical Gorenstein
condition on A_p, and using the one-dimensional CM B_p above, its
canonical-module consequence is

    ω_(B_p) ≅ Hom_(A_p)(B_p,A_p).

The common-total-quotient-ring property identifies this Hom with the
conductor: after localization any A-linear map is multiplication by
its value at 1, and its image condition is precisely βB_p⊂A_p.
The CI source B_p is Gorenstein, so its canonical module is free of
rank one. The conductor would then be principal, contradicting the
two necessary generators. This checks the essential duality step on
the full nilpotent schemes. The reviewer did not independently
retrieve Piene's PDF; the cited placement before Proposition 2.9 is
the producer's attribution and is not needed for this checked proof.

**The remaining pair and the general principle.** For u=v=1, the
coefficient ideal is (a,d,b²,c²), a proper irrelevant-primary ideal.
Its nonzero quotient is entirely irrelevant torsion, so the established
cohomology sequence proves failure of ACM. Together with the endpoint
argument, this covers every positive u,v without enumeration.

The source/image cokernel and conductor formulas also hold for an
arbitrary algebra S[z]/(z²−r) with imposed relations P+Qz and R+Tz.
For finite birational Gorenstein curve source and target, the same
canonical-module argument requires an invertible conductor on the
source. The specific two-generator obstruction proved here uses the
displayed power family and characteristic zero; it is not a general
obstruction for every quadratic cover or every supported thickening.

**Geometric meaning and disposition.** The construction supplies genuine
ambient AG thickenings with exactly the required reduced support and
no residual curve. The finite projection retains their generic
nilpotent structures but, once a power is nontrivial, its endpoint
conductor is not a Cartier ideal on the Gorenstein source. This prevents
the actual embedded image from retaining Gorenstein duality. It closes
the entire specified direct-image CI construction, rather than an
exhaustive class of possible STCI equations. No mathematical correction
remains in the reviewed proof. A wording clarification requested by this
review distinguishes the cokernel B/A from the actual image ring A.
The outcome remains independently reviewed provisional mathematics,
with no canonical promotion or change to unrestricted STCI status.

## 6. Bounded characteristic comparison extracted from the same proof

Reviewer: `projection_conductor_proof_review`. **PASS for the following
extensions**, independently reconstructed at the parent's request without
new calculations, exponent enumeration, or a new construction campaign.

For a positive characteristic p satisfying p∤2uv, the proof of the
displayed family's non-AG image is unchanged. The generic equality uses
2^(u−1)≠0; the Artinian identity uses 2 invertible; the first endpoint
test uses u≠0; and the second uses 2v≠0. The absence of linear terms
in the two defining polynomials of R_u for u≥2 does not depend on
characteristic. The pair (1,1) has the same nonzero irrelevant torsion.
This is an extension of the proved mechanism within the same source,
not a statement covering exponents divisible by p.

In odd characteristic p, take u=v=n=p^e, e≥1, and m=(n−1)/2.
Frobenius and z²=r give

    P=b^(2n),   Q=−a^n r^m,
    R=c^(2n),   T_v=−d^n r^m.

The conductor is therefore r^m(a^n,d^n)B. After sheafification on W,
a,d have no common zero, since they have none on its reduced support
D. Thus the conductor ideal sheaf is exactly r^m O_W. Moreover r is
a nonzerodivisor on the pure CI source: it is nonzero at the sole
generic support D. Hence this conductor is an effective Cartier ideal
on W. This is explicitly a sheaf statement; the homogeneous conductor
ideal still has the displayed (a^n,d^n) factor. Removing that factor
at the cone vertex would be unjustified.

Geometrically, Frobenius turns the endpoint conductor defect into a
Cartier divisor, so the non-Cartier obstruction proved in characteristic
zero disappears for these powers. Invertibility is only the necessary
condition supplied by duality; no converse has been proved here.
These powers consequently provide no asserted locally Gorenstein,
ACM, AG, CI, or STCI image and no new characteristic-zero conclusion.

## 7. Final preservation check and reviewed source state

Reviewer: `projection_conductor_proof_review`. Date: 2026-10-31.
**Final scoped PASS.** Source §§3–5, including the final characteristic
comparison and corrected identification of B/A as a cokernel, were
checked in the source state with SHA-256

    5e578fba3774456584e184d205686fa1a26ad4faf42615395c43153ec65605e3

for `2026-10-31-ambient-transport-and-projection.md`. The independent
coverage in §§5–6 above applies to that exact state. The other reviewer's
coverage of source §§1–2 remains separately identified above; this
reviewer does not claim to have independently repeated that work.

The substantive text of
[strategy assessment §20](2026-10-31-unrestricted-strategy-assessment.md#20-ambient-transport-a-genuine-projection-source-and-its-conductor-obstruction)
was also checked for preservation against the source and the separate
audit scopes. It retains the exact full-family conclusion, nilpotent
conductor mechanism, unresolved ACM question, Frobenius limitation,
absence of an exhaustive reduction, and open unrestricted STCI status.
The (1,1) isomorphic-projection description follows from the established
cokernel having only irrelevant support. The alternative-source synopsis
preserves the first reviewer's scoped findings and their limitations;
its primary sources were not independently re-audited here. The parent
may replace the assessment's pending-preservation sentence with this
scoped PASS without further mathematical change. No material finding
remains unresolved within this review's stated scope.

## 8. Further extraction: global adjunction for odd Frobenius powers and characteristic two

Reviewer: `projection_conductor_proof_review`. Date: 2026-10-31.
**PASS for the following additional deductions**, independently challenged
after the preceding reviewed version was preserved. These are further
consequences for the same source; they supersede no proved statement
above and do not extend the construction campaign. In particular, the
earlier absence of a positive conclusion from conductor invertibility
alone remains valid.

**Odd Frobenius powers: the global obstruction.** In odd characteristic,
let u=v=n=p^e, e≥1. The checked conductor calculation gives
c=O_W(1−n), and the checked generic isomorphism on the full nilpotent
structures gives deg(Y)=deg(W)=8n². Suppose the actual Y were a
scheme-theoretic complete intersection of degrees a,b. Then ab=8n²,
ω_Y=O_Y(a+b−4), and ω_W=O_W(4n−3). The coordinate projection
pulls O_Y(1) back to O_W(1). Finite duality therefore gives

    O_W(4n−3) ≅ c ⊗ π*ω_Y = O_W(a+b−n−3).

Restriction to D≅P1, where O_W(1)|D has degree four, forces
a+b=5n. But then (a−b)²=(a+b)²−4ab=−7n²<0 as an equality of
ordinary integer degrees. Hence Y is not a CI, and consequently not
AG in P3. The degree calculation and inequality take place in the
integers, not the positive-characteristic field. The conductor is
Cartier in these cases; the obstruction is instead the incompatible
global dualizing twist and degree budget. This proves no failure of
local Gorensteinness or ACM.

**Characteristic two: actual CI images.** Let n=2^e, e≥1. Now
h=z²+ad, and Frobenius gives relations in the retained coordinates:

    F=b^(2n)+a^(3n/2)d^(n/2),
    G=c^(2n)+a^(n/2)d^(3n/2).

Thus B=(S/(F,G))[z]/(z²+ad) exactly, with S/(F,G) embedded by the
constant coefficient of this monic quotient. In particular the actual
image ring A is S/(F,G). The forms are monic in the separate variables
b,c, making A finite free over k[a,d]; they form a height-two regular
sequence. This supplies an actual CI(2n,2n), of degree 4n².

The radical is precisely I_C. Explicitly

    F=(b⁴+a³d)^(n/2),   G=(c⁴+ad³)^(n/2).

On a≠0, the first quartic gives d=b⁴/a³, and the second gives
c⁴=b¹²/a⁸. The fourth-power map is injective in characteristic two,
so c=b³/a² on the reduced support. These are the fixed quartic's
parameter equations on that chart. At a=0, b=c=0 and only the other
endpoint remains. This checks the entire projective reduced support.

The projection here is finite flat and radicial of rank two, since
B is free with basis 1,z over A and its quadratic equation is purely
inseparable. Its map on the reduced curves D→C is nevertheless an
isomorphism, with reduced function-field degree one. The rank-two
statement concerns the full nilpotent schemes: they are not generically
isomorphic, so the odd-characteristic birational-conductor argument
does not apply. The ambient quadric h is singular along
a=d=z=0; this line is disjoint from D. No smoothness of that entire
quadric is needed for the displayed monic algebra or CI conclusions.

This is a uniform recovery of the characteristic-two quartic pair
and its powers in the same operation, rather than a new STCI theorem
in characteristic zero. The three geometric mechanisms remain distinct:
non-Cartier endpoint conductor in the audited characteristic-zero family,
incompatible global adjunction for odd Frobenius powers, and actual
rank-two projection onto a CI in characteristic two.

## 9. Final state after the further extraction

Reviewer: `projection_conductor_proof_review`. Date: 2026-10-31.
**Final scoped PASS** for source §§3–6 in the state with SHA-256

    0fa00e1fa531806e4489cc91817b7c9e9d5a3bd98128b8686b60e57a4c89d4a7

for `2026-10-31-ambient-transport-and-projection.md`. The earlier hash
in §7 identifies the earlier accepted state and is retained; §8 records
the substantive independent review of the subsequent extraction.
The final §5 points to §6 without drawing a sufficient-condition
inference from invertibility alone. The final §6 preserves the odd
Frobenius adjunction contradiction as an integer-degree argument and
the characteristic-two exact CI construction, including the full-scheme
rank-two versus reduced-isomorphism distinction. The linked prior
positive-characteristic construction was checked: its q=4 pair is
exactly the quartic pair recovered here in characteristic two.

The revised characteristic paragraph of strategy assessment §20 was
also checked against these statements. It preserves the odd-Frobenius
AG/CI exclusion without asserting failure of ACM or local Gorensteinness,
and the known characteristic-two success without implying a
characteristic-zero construction. The assessment may explicitly set
n=p^e and label its source-closing recommendation characteristic zero;
these are clarity adjustments consistent with this disposition.
There is no new canonical promotion, exhaustive reduction, or change
to the unrestricted characteristic-zero STCI question. No material
finding remains unresolved in this review's stated scope.
