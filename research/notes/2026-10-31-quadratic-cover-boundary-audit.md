# Scoped audit of the quadratic-cover boundary

Date: 2026-10-31. Reviewer: `quadratic_boundary_review`, independent
mathematical reconstruction with no nested delegation.

**PASS in the scope below.** The reviewed source is
[quadratic-cover boundary](2026-10-31-quadratic-cover-boundary.md), §§1–2,
§3 through (4), §§4–5, and the corresponding scope limitations in §6.
This audit expressly excludes the graded derivation (5)–(7), its
generalization, and conclusions depending on that derivation; a separate
review covers those. It is not whole-file certification or canonical
promotion. No material correction was needed in the assigned text.

## Hypotheses and reconstruction

The field is algebraically closed of characteristic zero, the embedded
curve is exactly C=[s4:s3t:st3:t4], and the double cover is
E=S[z]/(z²−(2bc−ad)). For §§1–4 the downstairs scheme is the full
supported CI Y=V(Fα,Gβ), and W is the full D-primary extraction of its
pullback. The general converse in §5 assumes any saturated pure W with
reduced support D. In particular neither ACM nor local Gorensteinness of
W is silently added.

1. Away from the endpoints, r is a unit and its distinct reduced roots
   lift uniquely through the nilpotent ideal of the full local algebra.
   Thus the pullback splits into two copies of that algebra locally.
   The CI has no embedded components; extraction gives pure W, locally
   CM along the projective curve. The kernel of A→B vanishes generically
   and hence vanishes, since A has no embedded associated prime. B is
   generated over A by 1,z. None of this proves depth two at the vertex.

2. In the common total quotient algebra every A-linear B→A map is
   multiplication by its value at 1. This proves Hom_A(B,A)=c. Since
   B=A+Az, the kernel of A(−1)→B/A is c(−1), giving (1). At a
   projective endpoint B is maximal CM over the one-dimensional
   Gorenstein A. Applying Hom_A(−,A) gives A/c=Ext¹_A(B/A,A), the
   finite-length Matlis dual. Trivializing the degree-one twist makes
   B/A isomorphic to A/c itself, so A/c is Artin Gorenstein. The
   quadratic map (A/c)[z]/(z²−r)→B/c is onto and both lengths are
   2δp, proving (2). Equivalently B/c is a monic quadratic Frobenius
   extension of A/c and is Artin Gorenstein too. These are local
   statements: T need not be arithmetically Gorenstein, and c need not
   be invertible on W.

3. A relation p+qz for W has q in c. Conversely every element of c
   occurs as such a coefficient, because qz belongs to A. Restricting
   its conjugate to W gives −2qz, proving I_(H/W)=zc. For the length,
   0→c/zc→B/zc→B/c→0 is exact. Multiplication by z on the two full
   lattices c and B has the same determinant valuation. Its value on
   the reduced branch has order two, so that valuation is 2m.
   Consequently length H_p=2m+2δp and total length H=αβ+2δ.
   This is the actual scheme attachment, not a new residual component.

## Independent local control

For (8), use the free R=k[[t]] basis 1,w,u with w²=tu and uw=u²=0.
Then x=u+2tw has x²=4t³u and x³=0. The inclusion of the R-bases
1,x,x² and 1,w,u has determinant 8t⁴, so δp=4. After inverting t,
putting w=z−t² gives x=2tw+w²/t; on the positive branch x³=0 is
equivalent to w³=0 because w+2t² is a unit there. The displayed free
algebra is the contraction of that generic primary algebra, proving
that it is the full extraction rather than an arbitrary quotient.

For b=b0+b1w+b2u, membership in the conductor is exactly

    b1−2tb2 ∈ t⁴R,       b0−4t³b2 ∈ t⁴R.

The first condition expresses b∈A; the second expresses bz∈A after
using the first. They give c=(t⁴,x+4t³)B. The quotients are
A/c=R/(t⁴) and B/c=R[z]/(t⁴,z²), as stated. Modulo t the source is
k[u,w]/(u,w)², with two-dimensional socle, so it is non-Gorenstein.
The attachment length is 6+8=14. This exhibits why nonprincipal
conductor alone is not a contradiction when W is not Gorenstein.
It is a formal local control, with no global homogeneous realization
claimed.

## Converse, reduced union, and literature boundary

For any pure W_red=D, z is regular. Invariance and averaging separate
p+qz in I∩σI into p and qz in I. Regularity then puts q in I, so
I∩σI=(I∩S)E, proving (9). The union ring is A[z]/(z²−r).
It is finite free over A and has the same CM status: the extension of
the homogeneous maximal ideal has the same radical, and the A-module
is A⊕A(−1). When CM, the monic quadratic Frobenius extension preserves
type, giving AG union if and only if AG image. A height-two AG ideal
in the four-variable polynomial ring is a CI. Thus an actual such AG
union suffices; the statement does not manufacture one.

For U0, each branch meets the other in length two at each endpoint.
The restriction of the dualizing sheaf is ω_P1(2pa+2pd)=O_P1(2),
whereas its hyperplane bundle restricts to O_P1(4). Subcanonicity with
an integral hyperplane twist is impossible. Also U0 is the full inverse
image of C, so π_*O_U0=O_C⊕O_C(−1); this gives h0(O_U0(1))=6,
failure of ACM, and arithmetic genus three. Locally its displayed
plane equation is the ordinary tacnode z²=b⁴.

The reviewer opened the actual three linked primary PDFs and checked
the cited statements, without re-proving their general theorems:

- [Manolache, Theorem 2.10, Lemma 2.11 and Remark 2.12](https://imar.ro/journals/Revue_Mathematique/pdfs/2007/4/manolache.pdf),
  printed p.400: supplied linkage extensions are locally Gorenstein;
  their twists are restrictions of the inverse dualizing line; an
  embedded extension need not exist. In the present union setting an
  invertible attachment ideal would make each branch's canonical
  module invertible. Non-Gorenstein branches therefore require the
  more general canonical-module attachment.
- [Hartshorne, Proposition 3.1](https://arxiv.org/pdf/math/0301163),
  PDF p.5: effective divisors mH−K on an ACM surface satisfying G1
  are AG. Its G0 variant is also stated there. A locally CM surface
  in smooth Q3 is Cartier; Pic(Q3)=Z gives X∼eH and adjunction gives
  K_X=(e−3)H. Its indicated divisor is a hyperplane multiple, and the
  section lifts by H¹(Q3,O(n−e))=0. This reduction does not supply a
  section with the prescribed support.
- [Casanellas–Drozd–Hartshorne, Theorem 6.1 and Remark 6.3](https://arxiv.org/pdf/math/0307378),
  PDF p.24: codimension-two ACM subschemes on a nonsingular quadric
  threefold are glicci; the remark discusses the additional unresolved
  structure of liaison classes. Neither statement fixes intermediate
  supports or the conjugate residual partner.

The geometric gain reviewed here is the complete endpoint quadratic
pinching and the exact conjugate-union descent criterion. The local
countercontrol rules out a Gorenstein-source shortcut. No unrestricted
exclusion, global example, exhaustive classification, or bound from
(5)–(7) is certified by this scoped audit.

## Independent graded, characteristic, and strategy review

Date: 2026-10-31. Reviewer: `conductor_degree_independent_challenge`,
independent reconstruction and strategy challenge, with no nested
delegation. This section supplements the preceding review without
changing its ownership or scope.

**Scoped PASS.** This review covers the final source's §3 graded
derivation (5)–(7a), nonemptiness argument, module generalization and
characteristic statement; §6's conclusion and stopping criterion;
and their preservation in
[strategy assessment §21](2026-10-31-unrestricted-strategy-assessment.md#21-an-arbitrary-pair-boundary-bound-and-automatic-conjugate-descent).
The source SHA256 at final review is

    3498f9af99169e54ea7730d3d9c0087473806bd3367fbb9fa9e2d4cd4752dc06

One ambiguity in the earlier generalization was identified and fixed:
generation by 1 and an integral degree-one element must be generation
as an A-module, explicitly B=A+Aw. Algebra generation alone can require
higher powers and does not make B/A cyclic. The final source makes
this distinction. No unresolved material finding remains in this
review's scope. This is provisional review evidence, not canonical
promotion or an unrestricted existence/nonexistence result.

### Reconstruction of the graded argument

The full primary extraction supplies a saturated finite graded
extension A⊂B which agrees with A on the full generic Artin algebra.
Its quotient has finite projective support. Module generation by 1,z
gives B/A=T(−1), with T=A/c. In the local-cohomology sequence,
H⁰_m(B)=0 and H¹_m(A)=0 force H⁰_m(T)=0. A nonzero T therefore
has dimension one and is Cohen–Macaulay. Nonemptiness is established
without confusing the coordinate ring with the full section ring:
W spans P4, Y spans P3, and dim(B1/A1)=1. Irrelevant-torsion
vanishing excludes a quotient supported only at the cone vertex.

Put e=α+β−4. Since T is dimension-one CM, Ext²_S(T,S(−4))=0.
Dualizing (1) yields the source's exact sequence (5). Finite duality
and the common full total quotient algebra identify

    ω_B=Hom_A(B,A(e))=c(e).

Taking the quotient inside A(e), then shifting by −1, gives the
more explicit exact sequence

    0 → T(e−1) → ω_T → Ext³_S(B,S(−4))(−1) → 0.

The last term has finite length because B is CM away from its vertex.
The injection requires neither ACM nor Gorensteinness of B. In
particular it does not reinstate the invalid Gorenstein-branch
assumption excluded by the separate local control.

For a regular linear form ℓ and h-vector h0,…,hs, graded freeness over
k[ℓ] and canonical duality give

    T ≅ ⊕ᵢ k[ℓ](−i)^{hᵢ},
    ω_T ≅ ⊕ᵢ k[ℓ](i−1)^{hᵢ}.

Thus, with H_Δ(n)=dim_k T_n and H_Δ(n)=0 for n<0,

    dim_k(ω_T)_j = δ − H_Δ(−j).

The injection supplies
H_Δ(j+e−1)+H_Δ(−j)≤δ. Substituting n=j+e−1 proves (7a)
for every integer n. In particular n=0 gives H_Δ(e−1)<δ,
so s≥e. Equivalently the source's initial-degree comparison is
1−e≥indeg(ω_T)=1−s. The standard graded Artinian reduction has
no internal zero, hence δ=Σhᵢ≥s+1≥e+1=α+β−3. All twists and
inequality directions in (5)–(7a) agree.

### Primary-source comparison and characteristic scope

The reviewer opened
[Kreuzer, *On the canonical module of a 0-dimensional scheme*, §1 and Theorem 2.4](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7DC79E96BB5A7CBA61D74E9F5835E927/S0008414X00045843a.pdf/div-class-title-on-the-canonical-module-of-a-0-dimensional-scheme-div.pdf).
Its initial canonical degree and faithful-element characterization
explain the classical Cayley–Bacharach mechanism used here. The source
correctly retains a qualification: if s=e, the faithful element lies
in the initial canonical degree and the maximal-degree criterion
applies; if s>e, that stronger property has not been established.
The displayed inequality (7a) has its own direct proof above and does
not depend on extending that criterion. The finite-duality input is
also supported by
[Stacks, Lemma 47.15.8](https://stacks.math.columbia.edu/tag/0AX0).

The quadratic-cover extraction, boundary identities and conjugate
descent require only 2 invertible: smoothness of the cover, distinct
roots and their lifting through nilpotents, and separation of even
and odd parts all remain valid in odd characteristic. The reviewed
graded extension statement itself is characteristic free under its
stated hypotheses. In characteristic two this cover no longer
separates the branches, so that application of the extension argument
is unavailable. The bound therefore supplies no characteristic-zero
mechanism on its own.

### Geometric gain, preservation, and stopping decision

The boundary is the actual finite conductor scheme of the polarized
map W→Y. Its homogeneous restrictions must retain postulation
through degree at least e: the additional linear coordinate upstairs
requires a sufficiently large and appropriately graded descent
defect. This is stronger retained information than a total attachment
length or genus identity. It is not an upper bound on the available
defect, and it does not identify endpoint attachment with a residual
curve downstairs.

The focused comparison with the tropical-conductor note §§3–5 and
the ambient-projection note §§3–5 finds existing conductor duality,
genus bookkeeping and the particular quadratic source, while the
all-pair graded specialization adds the displayed necessary constraint.
This bounded comparison makes no repository-wide or literature
novelty claim. Assessment §21 preserves these distinctions, the
non-Gorenstein control's limited role, and the automatic-descent
construction target without treating that target as a construction.

The stopping recommendation passes with its final experimental
qualification. A future bounded test may investigate an unproved
geometric comparison whose predicted bound at residual degree zero
would contradict (7) or (7a), or an embedded operation with a concrete
prospect of an AG conjugate union. A successful theorem is not required
in advance. The proposal must contribute a new geometric input and a
discriminating success/failure outcome beyond requesting the desired
final equations or union. No endpoint classification follows from the
present result. Without such input, another attachment identity,
unrelated local type or reformulation of the equations should end the
test rather than expand its cases. The lack of a current comparison
or operation supplies no evidence favoring nonexistence.
