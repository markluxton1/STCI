# Bounded primary-source audit: Jaffe type versus generic contact depth

Date: 2026-08-23

Status: provisional worker contribution; not integrated and not an edit to the
canonical research outlook.

## Bounded question

Compare David B. Jaffe's iterated-curve-blowup invariants with the generic
normal-plane contact tree used in the current research state.  Determine exactly what
Jaffe bounds, whether the surface-threshold depth bound is already present there, and
where his hypotheses exclude arbitrary thick defining pairs.

## Primary source and inspection boundary

David B. Jaffe, *Applications of iterated curve blowup to set-theoretic complete
intersections in* \(\mathbf P^3\), arXiv:alg-geom/9410008v1 (1994), published in
*J. reine angew. Math.* **464** (1995), 1--46:

- abstract and record: <https://arxiv.org/abs/alg-geom/9410008>;
- primary PDF: <https://arxiv.org/pdf/alg-geom/9410008>.

Page locators below are the page numbers printed in the 59-page arXiv v1 PDF, not the
shorter journal pagination.  I inspected the complete primary PDF and its TeX source,
with concentrated checks of the introduction, Sections 1--2, 5--6, and 10--13.  No
adjacent source was needed to settle the notation or scope questions.  The negative
search included `minimal`, `integral`, normal bundle, order, type length, common
singularities, and every occurrence of \(p_i\).

## Research delta

1. **Established distinction.**  Jaffe's \(p_i(S,C)\) are closed-point singularity
   invariants of one surface-curve pair.  They are not the multiplicities of the two
   germs at the generic infinitely-near points used in the current contact tree.
2. **Established overlap.**  Jaffe's ambient iteration does follow the same generic
   infinitely-near chain when both defining surfaces are generically smooth along
   \(C\).  In that regime the normal orders are \(p=q=1\), the intersection
   multiplicity is \(n=st/d\), and the current depth is exactly \(h=n-1\).
3. **Interpretation.**  The specialization of
   \(h\geq\lceil\tau^2/d\rceil-1\) to \(p=q=1\) is formal from
   \(h=st/d-1\) and the component-exclusion inequalities \(s,t\geq\tau\).
   It is not a named result of Jaffe, who has no surface-effective threshold, but the
   genuinely new scope of the current theorem is the arbitrary-normal-order/thick
   regime rather than this non-thick specialization.
4. **Established scope boundary.**  Jaffe's main iterated machine assumes both
   equations have generic normal order one.  It does not apply when both surfaces are
   singular generically along \(C\), including an order-minimal integral thick pair.
5. **Strategic correction.**  Jaffe already gives strong conditional upper bounds on
   this depth in the no-common-singular-points stratum.  Therefore a search for a depth
   upper bound must target the generically singular/order-minimal stratum; rediscovering
   a bound under Jaffe's hypotheses would not confront the live thick-only branch.

## 1. Exact definition of Jaffe's type

### Established: surface-curve pair hypothesis

Jaffe's convention (Section 1, arXiv PDF pp. 6--8) makes \((S,C)\) a
surface-curve pair only when \(C\) is regular and \(C\not\subset
\operatorname{Sing}S\).  Locally, if \((S,C)=\operatorname{Spec}(A,\mathfrak p)\),
both \(A_{\mathfrak p}\) and \(A/\mathfrak p\) are regular.  Thus \(S\) is
smooth at the generic point of \(C\), although it may be singular at finitely many
closed points of \(C\).

### Established: definition

Let \(\pi:\widetilde S\to S\) be the blowup along \(C\), let
\(\widetilde C\) be its distinguished section over \(C\), and let
\(E_1,\ldots,E_r\) be the reduced exceptional curves of \(\widetilde S\).
Section 2, Definition, arXiv PDF pp. 8--9 defines
\[
 p_1(S,C)=\sum_{j=1}^r
   \operatorname{length}\mathcal O_{\pi^{-1}(C),E_j},
 \qquad
 p_{i+1}(S,C)=p_i(\widetilde S,\widetilde C).
\]
The sequence \((p_1,p_2,\ldots)\) is the **type** of \((S,C)\).

For a global geometric pair it is the sum of local contributions from the finitely
many points in \(C\cap\operatorname{Sing}S\) (Section 1, pp. 7--8).  If \(S\)
is embedded as a hypersurface in a smooth threefold, Remark 2.1 identifies the
scheme-theoretic exceptional fiber with \(\widetilde S\cap E\).  In the ambient
iteration of the introduction and Section 10, the cycle
\(S_i\cap E_i\) consists of the distinguished section \(C_i\) plus vertical
rulings over closed singular points, whose total multiplicity is \(p_i(S,C)\).

### Established warning: the entries need not decrease

Remark 2.2, p. 9 explicitly says that monotonicity
\(p_i\geq p_{i+1}\) is unknown even for rather natural classes and gives a later
example with \(p_1<p_2\).  Hence the index of the last nonzero \(p_i\), when
finite, is a persistence length for closed-point surface singularities; the values are
not a proximity sequence of generic plane-branch multiplicities.

## 2. Dictionary with the current generic contact tree

Let \(K=\overline{k(C)}\).  The current construction completes the ambient
threefold transversally at the generic point of \(C\), obtaining two plane germs
\(f,g\in K[[x,y]]\), with
\[
 p=\operatorname{mult}(f),\quad q=\operatorname{mult}(g),\quad
 m=i_0(f,g),
\]
and lets \(h\) be the largest depth of a common infinitely-near point, with the
origin at depth zero.

Under Jaffe's Section 10 hypotheses
\(C\not\subset\operatorname{Sing}S,T\), both generic germs are smooth:
\(p=q=1\).  Bézout gives
\[
 n=\frac{st}{d}=m.
\]
Section 10, pp. 38--39 states that after the \(k\)-th ambient blowup the strict
transforms meet along the distinguished section \(C_k\) with multiplicity
\(n-k\), and after the \(n\)-th blowup only strict transforms of vertical rulings
remain.  Equivalently, two smooth generic plane branches have one common point at each
depth \(0,\ldots,n-1\).  Therefore
\[
 \boxed{h=n-1=\frac{st}{d}-1.}
\]

The exact dictionary is thus:

| Current generic invariant | Jaffe non-thick iteration |
|---|---|
| normal orders \(p,q\) | both equal to \(1\) |
| generic intersection \(m\) | \(n=st/d\) |
| common point at depth \(i\) | distinguished horizontal section \(C_i\) |
| maximum generic depth \(h\) | \(n-1\) |
| generic multiplicities at every common point | \(1,1\) |
| no current generic analogue | \(p_i(S,C)\), vertical ruling mass over closed singular points of \(S\) |

**Interpretation.**  The iteration index is shared, but the numerical entries are
orthogonal.  Jaffe uses the closed-point vertical debris to constrain how a long generic
smooth-branch contact chain can globalize.

## 3. Exact bounds in Jaffe

### 3.1 No common singular points: exact type and degree/depth bounds

**Established (Theorem 10.1, "I", p. 40).**  If \(C=S\cap T\)
set-theoretically, \(C\) is smooth of degree \(d\) and genus \(g\), the
surface degrees are \(s,t\), and
\(\operatorname{Sing}S\cap\operatorname{Sing}T=\varnothing\), then, for
\(n=st/d\),
\[
 p_1=\cdots=p_{n-1}
 =\frac{d[n(s-4)+t]+(2-2g)n}{n-1}.                 \tag{J-I}
\]
The definition and Section 10 construction keep the generic-order-one condition in the
background; in applications Jaffe may replace one equation by a same-degree linear
combination to achieve it.

**Established (Theorem 13.1, "X", pp. 49--50).**  If in addition \(C\)
is not a scheme-theoretic complete intersection, then
\[
 s,t<2d^4.
\]
When \(s\leq t\), the proof gives the sharper pair of bounds
\(s<2d^2\), \(t<2d^4\).  The proof explicitly exploits the integrality of the
numbers in (J-I), meaning ordinary integer-valued \(p_i\), not integrality or
order-minimality of a thick defining pair.

**Derived interpretation, not a stated Jaffe theorem.**  In the generic-order-one
overlap,
\[
 h=\frac{st}{d}-1<4d^5-1
\]
using the sharper asymmetric degree bounds.  Thus Jaffe already supplies a
curve-degree-only depth upper bound when the two surfaces have no common singular
point.  His own common-vertex cone example on p. 50 shows the degree bound fails when
the common-singularity hypothesis is removed.

### 3.2 Common closed singularities allowed, but not generic thick contact

**Established (Theorem 10.3, "II", p. 41).**  Assume only that both surfaces
are generically smooth along \(C\).  For every \(1\leq k\leq n-1\),
\[
 \sum_{i=1}^{k-1}2^{k-i-1}(n-i+1)p_i+(n-k)p_k
 \geq
 2^{k-1}\{dt+n[d(s-4)+2-2g]\}.                 \tag{J-II}
\]
This permits singular points common to the two surfaces.  It supplies lower bounds on
the closed-point type needed to sustain a prescribed chain of length \(n-1\); it does
not bound \(n\) or \(h\) without an independent upper bound on the type.

### 3.3 Rational singularities: weighted lower bounds and finite complexity

**Established locally (Proposition 6.5, pp. 26--27).**  For a rational double
point surface-curve pair,
\[
 \sum_{k\geq1}\frac{p_k}{k(k+1)}\geq\Delta(S,C),              \tag{J-\Delta}
\]
where \(\Delta\) is the resolution-theoretic correction
\(C^2-\widetilde C^2\).

**Established globally (Theorem 11.1, "III", p. 42).**  Over \(\mathbf C\),
if \(S\) has rational singularities and the other defining surface is generically
smooth along \(C\), then
\[
 \sum_{k\geq1}\frac{p_k}{k(k+1)}
 \geq \frac{d^2}{s}+d(s-4)+2-2g.               \tag{J-III}
\]
Remark 11.2 says Jaffe cannot in general replace the infinite sum by the first
\(n-1\) terms; he can do so after excluding odd \(D_{r,r}\) configurations.

**Established local length information (Propositions 5.2 and 5.6, pp. 18--23).**
Jaffe computes every rational-double-point type explicitly.  Except for odd
\(D_{r,r}\), he proves
\[
 p_j(S,C)=0\quad\text{for all }j\geq\operatorname{order}(S,C).
\]
Here `order` is the Cartier order of the Weil divisor \(C\) in the local class group,
not the generic normal vanishing order and not order-minimality of a defining pair.
The exception is substantial: for odd \(r\),
\[
 \operatorname{type}(D_{r,r})=((r-1)/2,1^{[r-1]}),
\]
which has length \(r\) although its Cartier order is \(4\).

**Established surface-complexity bound (Lemma 11.3, p. 42).**  If a degree-
\(s\) complex surface has rational singularities and its minimal resolution has
\(N\) exceptional curves, then
\[
 N\leq \frac{s}{3}(2s^2-6s+7)-1.                \tag{J-N}
\]

**Derived interpretation.**  The explicit ADE types have length at most the number
of exceptional curves in their minimal resolutions.  Hence their global summed type
has length at most the right side of (J-N).  Under the hypotheses of Theorem I and the
rational-singularity argument in the proof of Theorem 12.2, a non-complete-intersection
pair has \(p_1=\cdots=p_h>0\), and the exceptional odd \(D_{r,r}\) cases are
excluded there.  Consequently one obtains the conditional depth bound
\[
 h\leq N\leq \frac{s}{3}(2s^2-6s+7)-1.
\]
This is not an arbitrary-pair bound: it uses characteristic zero, rational
singularities, no common singular points, and generic normal order one.

### 3.4 Normal-bundle upper bound

**Established (Proposition 11.6, p. 44).**  Let \(N_C\) be the normal bundle
of \(C\subset\mathbf P^3\), let \(\ell\) be the maximum degree of a line
subbundle of \(N_C\), and put
\[
 k_N=3d+(2g-2)-\ell.
\]
For a degree-\(s\) surface generically smooth along \(C\),
\[
 p_1(S,C)\leq d(s-1)-k_N.                       \tag{J-NB}
\]
This constrains the first closed-point singularity mass.  It is not an upper bound on
generic contact depth by itself, though it can be combined with (J-I) or (J-II) in
their respective strata.

## 4. Comparison with the surface-threshold depth bound

Suppose the current component-exclusion argument gives
\(s\geq\tau_S(C)\) and \(t\geq\tau_S(C)\) for a pair whose two defining
surfaces are generically smooth along \(C\).  Jaffe's overlap then gives
\[
 h=\frac{st}{d}-1
 \geq \left\lceil\frac{\tau_S(C)^2}{d}\right\rceil-1.
\]

Therefore:

- **Established non-subsumption statement.**  Jaffe does not define
  \(\tau_S(C)\), prove the component-exclusion lemma, or state this family-level
  threshold bound.
- **Interpretation.**  Once those new surface ingredients are supplied, the
  \(p=q=1\) specialization needs no new contact-tree inequality: it follows from
  Jaffe's exact chain length and Bézout.
- **Established scope gain of the current theorem.**  The inequality
  \(m\leq(h+1)pq\) and its threshold consequence continue to make sense when
  \(p,q>1\) and the tangent cones branch.  That is exactly the regime omitted by
  Jaffe's iteration.

For the smooth \((1,r)\) quadric family the resulting lower bound
\(h\geq r-1\) is therefore not a theorem already written by Jaffe, but in the
non-thick stratum it is compatible with—and formally reducible to—his
\(h=st/d-1\) setup.  The strategic value is the demand it places on every thick
presentation, not a strengthening of Jaffe inside his original stratum.

## 5. Why arbitrary thick pairs are outside Jaffe's machine

### Established hypothesis failure

If a homogeneous equation has generic normal order \(p\geq2\) along \(C\),
then \(C\subset\operatorname{Sing}V(F)\).  Such a hypersurface does not form a
Jaffe surface-curve pair.  Section 10 explicitly assumes
\[
 C\not\subset\operatorname{Sing}S,
 \qquad C\not\subset\operatorname{Sing}T.
\]
Moreover, Part III's surfaces are reduced and irreducible, so power-derived
nonreduced equations are excluded even before this generic-smoothness condition.

### Established proof failure

The formulas in Section 10 use
\[
 [S_k]=sH-\sum_{i=1}^kE_i,
 \qquad [T_k]=tH-\sum_{i=1}^kE_i,
\]
and the fact that the multiplicity along the distinguished section falls from \(n\)
to \(n-k\), one unit per blowup.  For normal orders \(p,q>1\), the first divisor
classes subtract \(pE_1,qE_1\); the exceptional tangent cones can have several
horizontal components or multisections; and multiplicities evolve by proximity rather
than by subtracting one.  Thus (J-I) and (J-II) cannot simply be read with different
initial \(p,q\).

### Negative result of the audit

The paper contains no theorem that:

- de-powers or descends a pair singular generically along \(C\);
- puts an order-minimal integral thick pair into the generic-order-one regime;
- bounds the generic contact depth of such a pair;
- bounds the normal orders \(p,q\) or a branched proximity tree; or
- uses `order-minimality` in the current presentation-theoretic sense.

Theorem 10.3 permits common **closed** singular points but still requires both surfaces
to be generically smooth along \(C\).  Theorem 13.1's hypothesis
\(\operatorname{Sing}S\cap\operatorname{Sing}T=\varnothing\) excludes a
genuinely thick pair even more directly, because both singular loci contain \(C\).

## 6. Lead-facing interpretation

The current program should not treat Jaffe's type as the thick contact tree.  A more
accurate synthesis is a two-axis object:

1. a **horizontal generic proximity tree**, whose depth and multiplicities are the
   current \(h,p_P,q_P\); and
2. at each horizontal stage, **vertical closed-point surface types** of Jaffe, whose
   aggregate masses are \(p_i(S,C)\) whenever that stage is generically smooth.

Jaffe proves that the vertical axis can constrain the length of a horizontal
order-one chain.  The live problem is to construct an analogue when the horizontal
tangent divisor itself has degree greater than one and branches.  The highest-value
literature-sensitive next step is therefore not another audit of Jaffe's conditional
degree bound, but a recursive divisor/proximity calculation for an order-minimal
integral thick pair, with Jaffe-type vertical corrections attached only after a branch
becomes generically smooth.

## Epistemic summary

- **Established:** definitions, exact formulas (J-I)--(J-NB), hypotheses, and the
  equality \(h=st/d-1\) in the generic-order-one overlap.
- **Derived interpretation:** the displayed depth consequences of Theorem X and of the
  ADE exceptional-curve bound; these are immediate combinations, not claims that Jaffe
  states them in contact-tree language.
- **Negative search boundary:** no arbitrary-thick, order-minimal, de-powering, or
  branched-contact-depth theorem was found in the complete source.
- **Uncertainty retained:** the audit does not exclude a relevant later generalization
  by another author; adjacent literature was deliberately not expanded because the
  assignment was a bounded Jaffe audit.
