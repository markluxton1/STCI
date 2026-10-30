# Historical mathematical source compilation

Full original mathematical text retained below. Original hypotheses, failures, qualifications and unresolved cases retain their source status; this compilation is not an independent correctness audit.

---

## Source: 2026-10-07-thick-repeated-fiber-smoothability.md

# Entirely-thick boundary: repeated ruling fibers do not force carrier singularity

Date: 2026-10-07
Status: NEGATIVE STRUCTURAL RESULT

Assume the equality-side carrier F has degree 3p and exact order p along C. On Q,
\[
F|_Q=h^pR_F,
\]
and let a trisecant ruling fiber L occur in R_F with multiplicity M>=2.

## 1. Local ambient form along L away from C

At the generic point of L, choose regular local coordinates x,z with
\[
Q=(z=0),\qquad L=(x=z=0).
\]
Since F|_Q vanishes to order M along L,
\[
F=x^M u+zA
\]
with u a unit after localization.

Along L,
\[
\partial F/\partial x=0
\]
when M>=2, but
\[
\partial F/\partial z=A|_L.
\]
Therefore F is smooth at the generic point of L whenever A|_L is nonzero.

## 2. The degree-3p recursion supplies the transverse smoothing term

The exact boundary recursion proved previously is
\[
F=F_{\rm cub}+QK,\qquad
K\in(I_C^{p-1})_{3p-2}.
\]
The QK term is precisely the local zA term above.

At a point of L outside C, the ideal sheaf I_C is the unit ideal. Hence membership
\[
K\in I_C^{p-1}
\]
places no local vanishing condition on K there.

Thus the order-p condition along C does not force K|_L to vanish generically. For a fixed L, nonvanishing of K at its generic point is an open condition on the available kernel space whenever a section not containing L is chosen.

Consequently repeated multiplicity M of L in R_F does not by itself force the ambient carrier F to be singular along L.

## 3. Strategic consequence

The repeated-root equality theorem cannot be upgraded to a carrier exclusion by the argument
\[
M>=2\Rightarrow F\text{ singular along }L.
\]
The Q-divisible kernel is exactly the missing transverse derivative and can smooth the carrier.

This is compatible with the earlier separation result: root multiplicity is special quadric-direction data, while generic carrier behavior along the ruling fiber has an independent transverse degree of freedom.

## 4. Pair geometry is essential

For an STCI pair, the mate G restricted to L is globally constrained: its nonzero residual restriction has zeros supported on the degree-three divisor C cap L.

Thus the remaining possible coupling is not generic singularity of F along L. It must involve compatibility among:
- the transverse smoothing coefficient K|_L for F;
- the restriction of G to L;
- the three marked points of C cap L;
- and the exceptional/valuation data above those points.

In particular, any useful repeated-root obstruction must use behavior at the marked divisor C cap L or variation in the ruling family, rather than the generic point of L.

## 5. Boundary of the claim

This note does not assert existence of a global smooth STCI carrier with arbitrary prescribed repeated residual divisor. It proves only that repeated residual multiplicity plus membership in I_C^p supplies no local mechanism forcing generic singularity along L.

A global singularity statement would require an additional relation forcing every allowable K to vanish on L; no such relation is currently established.


---

## Source: 2026-10-07-thick-root-budget-separation.md

# Entirely-thick boundary: separation of root multiplicity and section coefficient

Date: 2026-10-07
Status: NEGATIVE STRUCTURAL RESULT

Let T_i be a constant component of the first exceptional intersection W=D.D', with coefficient c_i, and let P_i=T_i intersect S_Q. Let M_i be the multiplicity of the corresponding ruling component in R_F.

The two numbers live at different strata.

The cycle coefficient c_i is the generic intersection multiplicity of D and D' along T_i. Equivalently it is computed after passing to the local ring at the generic point of T_i, a two-dimensional regular local ring over k(T_i).

The root multiplicity M_i is detected at the special closed point P_i, by restricting the first normal form of F to S_Q and measuring its vanishing there.

Therefore modifications supported near P_i can alter M_i while leaving the generic germs of D,D' along T_i unchanged. Such modifications do not change c_i.

Consequently no universal inequality
    c_i >= Phi(M_i)
with Phi increasing in M_i can follow merely from the definitions, reduced support, and first exceptional geometry.

This rules out the direct strategy:
    repeated root multiplicity -> section coefficient -> total budget 2pq.

Together with the local thickened-fiber countermodel, it shows that the repeated-root theorem and the generic Noether budget are genuinely transverse pieces of information. A successful obstruction must contain a mechanism coupling special-point data to generic-along-section data.

The natural mechanisms remaining are global:
1. variation/proximity of the relative cluster along C;
2. normalization and conductor, which can couple codimension-one generic data to special points;
3. a global line-bundle/divisor relation on the exceptional surface or on a normalization;
4. singularities/branching of the carrier surfaces along T_i.

Thus the repeated-root lane should be retained as a special-point constraint, but not treated as a direct source of lower bounds on c_i.


---

## Source: 2026-10-07-thick-ruling-interpolation-audit.md

# Entirely-thick (3,4) boundary: ruling-line interpolation audit

Date: 2026-10-07
Status: CORRECTION + PROVED interpolation calculation / NO NEW EXCLUSION

## 1. Correction to the marked-point note

The previous continuation incorrectly strengthened the ruling-line condition to a pure q-th power at a single point.

With the convention C=(1,3) on Q=P1 x P1, the ruling components of R_F in class (2p,0) are trisecant ruling lines. A relevant line L meets C in a degree-three divisor
    Z_L = L intersect C.
Therefore the STCI support condition implies only that the zero divisor of
    R_G|L in H0(L,O(q))
is supported on Z_L. It need not be concentrated at one point.

If Z_L consists of three distinct points P1,P2,P3, then projectively the allowed nonzero restrictions are
    lambda * l1^e1 l2^e2 l3^e3,
    e1+e2+e3=q,
with finitely many exponent triples. Degenerate trisecant fibers are handled by the corresponding length-three divisor; the same conclusion is that the allowed restrictions form a finite union of one-dimensional vector subspaces after the support points are fixed.

Thus the previous pure-power assertion should not be used.

## 2. Exact restriction rank on distinct ruling fibers

Write
    R_G in H0(Q,O(3q,q)).
Let L_1,...,L_r be distinct fibers of the ruling containing the components of R_F.

The simultaneous restriction map
    H0(Q,O(3q,q)) -> direct_sum_i H0(L_i,O(q))
is surjective whenever r <= 3q+1.

Proof: factor the section space as
    H0(P1,O(3q)) tensor H0(P1,O(q)).
Restriction to r distinct fibers is evaluation of the first factor at r distinct points, tensored with the identity on the second factor. Evaluation
    H0(P1,O(3q)) -> k^r
is surjective for r <= 3q+1.

On the (3,4) boundary the audited bound gives
    r <= min(p,q) <= q < 3q+1.
Hence all ruling-line restrictions can be prescribed independently.

## 3. Codimension of the support condition

For a fixed exponent choice on each trisecant fiber, the allowed restriction on L_i is a one-dimensional vector subspace of the (q+1)-dimensional H0(O_Li(q)). It therefore imposes q independent linear conditions.

Because the simultaneous restriction map is surjective, r fixed exponent choices impose exactly
    r q
linear conditions on R_G.

Allowing all exponent triples produces a finite union of such codimension-rq linear subspaces. It does not change the dimension.

Since
    h0(Q,O(3q,q))=(3q+1)(q+1),
and r<=q, these conditions are far from exhausting the available section space.

Therefore a dimension count based only on the restrictions of R_G to the ruling components of R_F cannot exclude the (3,4) boundary.

## 4. Multiplicity M_i of a component of R_F does not strengthen this restriction

If
    R_F = product_i L_i^{M_i},  sum M_i=2p,
the support condition on the reduced ruling line L_i depends only on L_i, not on M_i. Repeating L_i in R_F does not create additional independent restrictions on R_G|L_i.

To exploit M_i one must use higher transverse jets of R_G along L_i, not merely its restriction to L_i.

This is the key structural conclusion of the interpolation audit.

## 5. Correct next object: jets normal to the ruling line

A multiplicity-M_i component L_i^{M_i} in R_F supplies a thickened ruling line in the residual divisor of F on Q. The natural next map is therefore not
    R_G -> R_G|L_i,
but restriction to an infinitesimal neighborhood
    R_G -> R_G|_{M_i L_i}
or, equivalently, the first M_i-1 normal derivatives along L_i.

The STCI support condition should constrain the zero schemes of these transverse jets because F vanishes to higher order along L_i.

This is exactly where the jet-condition/discrepancy framework can interact nontrivially with the entirely-thick branch.

## 6. Numerical reason this may matter

The multiplicities satisfy
    sum_i M_i=2p
while r<=min(p,q).

Restriction to reduced fibers costs only rq conditions. A full M_i-jet prescription would scale instead like
    q * sum_i M_i = 2pq,
which is exactly the scale of the first exceptional Noether budget
    v=2pq.

This numerical coincidence is potentially structural:
    total repeated-root multiplicity x mate fiber degree = 2p*q = v.

It is not yet a theorem. But it identifies the first higher-jet calculation whose natural condition count lives on the same scale as the entire exceptional intersection budget.

## 7. Next target

Compute the restriction map
    H0(Q,O(3q,q)) -> H0(M_i L_i, O(3q,q)|_{M_i L_i})
for disjoint ruling fibers and determine precisely which transverse jets are forced by the STCI support condition, rather than merely by F vanishing on L_i^{M_i}.

The map itself is standard interpolation. The hard point is identifying the correct support/incidence condition on the mate jets. Any claim that all M_i jets are prescribed would require proof and must not be inferred from reduced support alone.


---

## Source: 2026-10-07-thick-segre-root-audit.md

# Entirely-thick boundary: Segre coordinate audit of the ruling-root argument

Date: 2026-10-07
Status: AUDITED / EXISTING DISTINCT-ROOT BOUND SURVIVES

For C=[s^4:s^3t:st^3:t^4] on the quadric x0*x3=x1*x2, the parametrization is, up to swapping the two middle Segre coordinates,
[s:t] x [s^3:t^3].
Thus the two ruling projections restricted to C have degrees 1 and 3.

With C=(1,3), the fibers occurring in R_F of class (2p,0) are trisecant ruling lines. A generic root selects L with C cap L=P1+P2+P3.

The first normal form of F on the quadric-direction section S_Q vanishes at all three points. This accounts for deg(D|S_Q)=6p=3*(2p).

However a point lies in D cap D' cap S_Q only if the first normal form of G also vanishes there. Although G|Q contains h^q, after dividing by the generic C-order q the first normal form on S_Q is controlled by the residual factor R_G. On L, R_G|L is a nonzero section of O_L(q), whose zeros are supported on C cap L. It has at least one zero but may concentrate all q zeros at one of the three points.

Therefore each distinct root of R_F guarantees at least one common point on S_Q, not three.

At the boundary W=sum c_j T_j and each distinct T_j meets S_Q once. Distinct trisecant fibers give disjoint degree-three divisors on C, so their guaranteed common points are distinct. Hence the existing bound survives:
#roots(R_F) <= #horizontal sections <= min(p,q).

Divisor interpretation: D|S_Q contains the pullback under the degree-three ruling projection C=S_Q -> P1_ruling of the degree-2p root divisor of R_F. By contrast W|S_Q=sum c_j P_j records only points where the mate first normal form also vanishes, with multiplicities from the full pair intersection. Thus c_j and root multiplicities M_j are not directly comparable.

The surviving discrete datum for each root L_i is an exponent allocation
(e_i1,e_i2,e_i3), e_i1+e_i2+e_i3=q,
with positive entries indicating which of the three preimages are common first-normal zeros. Any stronger obstruction must constrain these incidence assignments or their exceptional clusters; degree counting alone does not.


---

## Source: 2026-10-07-thick-sheaf-colon-recursion.md

# Entirely-thick boundary: sheaf-colon recursion by the quadric

Date: 2026-10-07
Status: PROVED SHEAF COLON / HOMOGENEOUS SATURATION STEP OPEN

Let I=I_C be the ideal sheaf of the smooth rational quartic C in P3 and let Q be its unique quadric equation.

## 1. Regular-embedding associated graded

Because C is smooth of codimension two in the smooth threefold P3, C is a regular embedding. Hence
\[
\operatorname{gr}_{\mathcal I}O_{P^3}
=\bigoplus_{m\ge0}\mathcal I^m/\mathcal I^{m+1}
\simeq \operatorname{Sym}_{O_C}(\mathcal I/\mathcal I^2).
\]

The first normal class of Q is a section
\[
\bar Q\in H^0(C,\mathcal I/\mathcal I^2(2)).
\]
Since Q is smooth along C, this class is nowhere zero. Equivalently it defines a line subbundle direction in the rank-two conormal bundle.

Locally trivializing the conormal bundle with \bar Q as one basis vector, multiplication by \bar Q on every symmetric power is multiplication by an indeterminate in a polynomial algebra. It is injective.

## 2. Sheaf colon identity

For every p>=1,
\[
(\mathcal I^p:Q)=\mathcal I^{p-1}.
\]

Proof: inclusion from right to left is immediate. If Qf lies in \mathcal I^p, reduce f modulo \mathcal I^{p-1}. Its lowest nonzero I-adic initial form, if any, lies in Sym^j(I/I^2) for j<p-1. Multiplication by \bar Q is injective and produces a nonzero class in degree j+1<p, contradicting Qf in I^p. Hence f lies in I^{p-1}.

This is local/sheaf-theoretic and requires no Rees-algebra linear-type hypothesis.

## 3. Consequence for the degree-3p kernel

If a homogeneous polynomial K of degree 3p-2 satisfies
\[
QK\in (I_{\rm hom}^p)_{3p},
\]
then after sheafification
\[
K\in H^0(P^3,\mathcal I^{p-1}(3p-2)).
\]

Thus
\[
(I_{\rm hom}^p:Q)_{3p-2}
\subseteq
H^0(\mathcal I^{p-1}(3p-2)).
\]

The reverse containment at the sheaf level is equality. The only unresolved issue for the homogeneous ordinary power is whether every global section on the right is represented in degree 3p-2 by the ordinary power I_{\rm hom}^{p-1}.

Equivalently, the only possible failure of
\[
(I_{\rm hom}^p:Q)_{3p-2}=(I_{\rm hom}^{p-1})_{3p-2}
\]
comes from saturation/irrelevant-ideal torsion of the ordinary power.

## 4. Recursive shape if saturation holds in this degree

If
\[
H^0(\mathcal I^{p-1}(3p-2))=(I_{\rm hom}^{p-1})_{3p-2},
\]
then the kernel from the degree-3p quotient note is exactly
\[
K_p=Q\,(I_{\rm hom}^{p-1})_{3p-2}.
\]

Combined with surjectivity onto H^0(Q,O(2p,0)), every boundary carrier has
\[
F=F_{\rm cub}+QK,
\]
where F_cub is a linear combination of products of p cubic equations of C and
\[
K\in(I^{p-1})_{3p-2}.
\]

This would give an exact recursion lowering normal order by one while lowering ambient degree by two.

## 5. Literature boundary

The sheaf-colon statement is standard regular-embedding/conormal algebra. Literature on Rees algebras and powers of rational normal curves is related but does not directly establish the homogeneous saturation assertion for this projected rational quartic, so no such theorem is imported here.

## 6. Next target

Determine
\[
H^0(\mathcal I^m(3m+1))/(I_{\rm hom}^m)_{3m+1}
\]
for m=p-1.

A vanishing result proving this quotient zero for all m would close the colon recursion. Otherwise an explicit nonzero quotient would identify the precise symbolic/saturated correction to the equality-boundary carrier space.


---

## Source: 2026-10-07-thickened-fiber-jets.md

# Entirely-thick boundary: thickened-fiber jet calculation

Date: 2026-10-07  
Status: **PROVED restriction-rank formula / OPEN STCI jet-incidence condition**

Let \(Q=P^1_x\times P^1_y\). The residual mate is
\[
R_G\in H^0(Q,O_Q(3q,q)).
\]
Let \(L_i\) be distinct fibers of the \(x\)-projection, with multiplicities \(M_i\) in
\[
R_F=\prod_i L_i^{M_i},\qquad \sum_i M_i=2p.
\]

## 1. Restriction to disjoint thickened fibers

Let
\[
Z=\sum_i M_iL_i.
\]
Since \(Z\) has class \((2p,0)\), there is an exact sequence
\[
0\to O_Q(3q-2p,q)\to O_Q(3q,q)\to O_Z(3q,q)\to0.
\tag{1}
\]

If \(3q-2p\ge-1\), then
\[
H^1(Q,O_Q(3q-2p,q))=0,
\]
so the restriction map
\[
H^0(Q,O_Q(3q,q))\to H^0(Z,O_Z(3q,q))
\]
is surjective.

More generally, the rank and cokernel are given exactly by the cohomology of (1).

## 2. Dimension of the full jet target

Each \(M_iL_i\) records \(M_i\) transverse coefficients, each a section of \(O_{P^1}(q)\). Therefore
\[
h^0(O_Z(3q,q))=(q+1)\sum_iM_i=2p(q+1).
\tag{2}
\]

When \(3q-2p\ge-1\), arbitrary transverse jets through order \(M_i-1\) can be prescribed independently on all repeated ruling fibers.

Thus repeated roots of \(R_F\) alone do not force special jets of \(R_G\).

## 3. Boundary in the p/q ratio

The automatic-surjectivity range is
\[
2p\le3q+1.
\tag{3}
\]

If \(2p>3q+1\), the thickened-fiber restriction map cannot be surjective. In fact the source has degree only \(3q\) in the transverse \(x\)-direction, so values on a divisor of degree \(2p\) satisfy interpolation relations.

This creates a genuine dichotomy inside the \((3,4)\) normalized boundary:

- **low-p regime** \(2p\le3q+1\): even the full repeated-root jets of the mate are freely interpolable;
- **high-p regime** \(2p>3q+1\): global transverse-degree relations appear.

The original first-stage inequality did not see this ratio.

## 4. Exact cokernel size in the high-p regime

Put
\[
m=2p-3q-1>0.
\]
Then \(3q-2p=-m-1\). Since \(q\ge0\),
\[
h^1(Q,O_Q(3q-2p,q))
=
h^1(P^1,O(-m-1))\,h^0(P^1,O(q))
=
m(q+1).
\]
Hence the thickened-fiber restriction map has cokernel dimension
\[
(2p-3q-1)(q+1).
\tag{4}
\]

This is a concrete discrepancy space.

## 5. Relation to the exceptional budget

The full thickened-fiber target has dimension \(2p(q+1)\), whose leading term is \(2pq\). The first exceptional higher-contact budget at \((3,4)\) is exactly
\[
v=2pq.
\]

The equality of leading terms is suggestive but not yet an identity: the jet target includes \(2p\) additional scalar degrees, and the intersection budget counts multiplicities rather than vector-space dimensions.

## 6. What is still missing

Reduced support of \(V(F,G)\) equal to \(C\) does **not** imply that \(R_G\) has prescribed values on the full thickening \(Z=\sum M_iL_i\). The calculation above only describes the ambient interpolation map.

To obtain an STCI obstruction one must prove that the support condition, proper-transform purity, or sectionwise Noether data forces the jet of \(R_G\) along \(M_iL_i\) into a proper incidence subset of
\[
H^0(M_iL_i,O(3q,q)).
\]

Without such a theorem, the discrepancy (4) is not an obstruction.

## 7. Next attack

The most promising place to derive that incidence condition is local at the length-three divisor
\[
L_i\cap C.
\]
Write the two residual equations on \(Q\) in coordinates transverse to \(L_i\), expand \(R_G\) through order \(M_i-1\), and impose that no branch of the complete intersection escapes \(C\).

This should determine whether the successive mate jets must have zeros supported on the same three-point divisor, or whether higher transverse coefficients are genuinely free. A local counterexample would settle the question just as usefully.


---

## Source: 2026-10-07-thickened-fiber-local-countermodel.md

# Entirely-thick boundary: local test of the thickened-fiber jet hypothesis

Date: 2026-10-07  
Status: **NEGATIVE RESULT — reduced STCI support does not constrain higher mate jets**

This note tests the open question at the end of \`2026-10-07-thickened-fiber-jets.md\`.

## 1. Local setup on the quadric

Let \(L\) be a ruling component of the residual divisor \(R_F\), occurring with multiplicity \(M\). Near a point of \(L\), choose regular coordinates \((x,y)\) on \(Q\) with
\[
L=(x=0).
\]
Let \(h=0\) cut out \(C\cap Q\). After removing units and other residual factors not vanishing generically on \(L\), write
\[
F|_Q=h^p x^M u
\]
with \(u\) a unit.

Write the mate as
\[
G|_Q=h^q R_G,
\]
and expand
\[
R_G=A_0(y)+xA_1(y)+\cdots+x^{M-1}A_{M-1}(y)+x^M B(x,y).
\tag{1}
\]

## 2. Reduced-support condition

Away from \(C\), \(h\) is a unit. The reduced zero set of \(F|_Q\) near \(L\) is then simply
\[
x=0,
\]
independently of the multiplicity \(M\).

Consequently an extra common point of \(F\) and \(G\) on \(Q\setminus C\) occurs exactly when
\[
x=0,\qquad A_0(y)=0
\]
at a point outside \(C\).

Thus the condition that the reduced common support on \(Q\) be contained in \(C\) imposes a condition only on
\[
R_G|_L=A_0(y).
\]
It imposes no condition on
\[
A_1,\ldots,A_{M-1}.
\]

### Proposition

Multiplicity \(M\) of a ruling component \(L\) in \(R_F\) does not, from reduced support alone, force any condition on the first \(M-1\) transverse jets of \(R_G\) along \(L\).

This remains true even though the reduced restriction \(R_G|_L\) must have all of its zeros supported on the degree-three divisor \(L\cap C\).

## 3. Explicit local family

Fix any admissible nonzero \(A_0(y)\) whose zero set is contained in \(L\cap C\). Then for arbitrary power series or polynomial coefficients
\[
A_1(y),\ldots,A_{M-1}(y),
\]
the pair
\[
F=h^p x^M,\qquad
G=h^q\left(A_0(y)+xA_1(y)+\cdots+x^{M-1}A_{M-1}(y)\right)
\]
has no additional reduced common point near \(L\setminus C\).

Hence there is an arbitrarily large family of higher mate jets with identical reduced-support behavior.

## 4. Consequence for the discrepancy calculation

The cokernel
\[
H^1(Q,O_Q(3q-2p,q))
\]
computed in the thickened-fiber note is a genuine interpolation discrepancy when \(2p>3q+1\), but reduced STCI support does not require \(R_G\) to hit a special point or subspace of the full thickened-fiber jet target.

Therefore that cokernel is **not an STCI obstruction by itself**.

The numerical coincidence
\[
h^0(O_Z(3q,q))=2p(q+1),\qquad v=2pq
\]
also has no established obstruction-theoretic meaning at this stage.

## 5. What survives from the quadric argument

The robust information is exactly zeroth order along each distinct ruling component:

1. \(R_F\) has at most \(\min(p,q)\) distinct ruling components.
2. Their multiplicities sum to \(2p\).
3. On each reduced component \(L_i\), every zero of \(R_G|_{L_i}\) is supported on \(L_i\cap C\).
4. Higher transverse jets of \(R_G\) are not controlled by reduced support.

Thus repeated-root multiplicity is a constraint on \(F\), but it does not automatically multiply the number of independent conditions imposed on \(G\).

## 6. Strategic consequence

This closes the simplest attempt to combine the repeated-root reduction with ordinary jet-discrepancy interpolation on \(Q\).

To exploit the multiplicities \(M_i\), one needs genuinely scheme-theoretic information beyond reduced support, for example:

- the sectionwise intersection coefficients \(c_i\) on the first exceptional surface;
- the local complete-intersection length along \(C\);
- integral closure/Rees valuations of the pair ideal;
- or normalization/conductor constraints.

The next promising calculation is therefore to relate \(M_i\) to the **sectionwise coefficient \(c_i\)** using local intersection multiplicity at the point \(T_i\cap S_Q\), not by trying to constrain higher jets of the mate from support alone.


---

## Source: 2026-10-08-session-checkpoint.md

# Continuation checkpoint after the October 8 batch, reconciled October 9

The [October 9 acceptance](OCT9_SINGULAR_DELPEZZO_AND_LOCAL_LIFTS.md#source-2026-10-09-session-results-acceptancemd)
supersedes the older open smooth-normalization language below. Every
genus-zero and every smooth-normalization quartic carrier is now
excluded; every nonnormal quartic containing C0 has rational
normalization. Genus one reduces to 4A1 or A3+2A1 and even mate
degrees; other projections of those types and rational genus two remain
open. The principal necessary mate-candidate locus has bound 630.
The complete current execution index has 97 sources and 110 indexed
executions; the 91/103 decomposition below describes this earlier batch.

Date: 2026-10-08. The universal STCI problem and the unrestricted
characteristic-zero C0 problem remain **OPEN**. Read the reconciled
[audited state](../AUDITED_STATE_2026-10-07.md) first. This checkpoint
preserves incomplete work as well as accepted progress.

## Accepted changes to the frontier

1. Every integral quartic normalized by (P2,O(2)) is excluded as a
   carrier of a smooth rational degree-four curve in characteristic
   zero, in every mate degree, including the non-slc Jordan forms.
2. Every integral quartic singular along a smooth twisted cubic is
   excluded as a carrier of fixed C0 in characteristic zero, in every
   mate degree. Its finite smooth-scroll normalization and whole
   conductor hypotheses are proved, rather than assumed.
3. The first rational primitive e=2,h=t endpoint ancestor family is
   fully excluded, including all 23 generic-dual exceptions and every
   affine lower lift. The second family has a generic exclusion with
   26 retained primitive geometric parameter points.
4. Both algebraic e=1,d2=4 ancestor directions are excluded for every
   homogeneous defect section, including repeated and infinity roots.
   The principal and obstruction-nonzero directions remain open.
5. The generator-bundle splitting criterion, all-defect quadric
   direction and six defect-one endpoint ancestor exclusions are
   accepted separately from their STCI-carrier counterparts.

The new scroll and defect-four results are reviewed in the
[root acceptance record](OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-new-results-acceptancemd).
The [late acceptance record](OCT8_LOCALCOH_AND_CONDUCTOR_ENDPOINTS.md#source-2026-10-08-session-late-results-acceptancemd)
supersedes the former incomplete contact and degenerate-conductor
boundaries. It accepts the entire e=1,d2=1 ancestor lane, every smooth
rational quartic-scroll carrier with unrestricted conductor schemes,
and both second-family quadratic exceptions. The second family now
retains 22 points in degree3,4,15 factors with their full lift fibres.
The previous all-normal-quartic and primitive e=1,D2=0 carrier theorems
remain accepted with their recorded antecedents. None of these results
is an exclusion of every quartic or every defining degree.

## Principal e=1,d2=1: an elliptic direction curve and finite contact locus

**PROVED equation reduction:** the saved principal chart equation H is
geometrically integral and has genus-one normalization. Put x=r+1/2,
W=(p+2-4x)/x^2, A=-W^3+8W^2-12W+72 and
C=2(W^2-6W+36). The exact identity is

    H(-2+4x+W*x^2,x-1/2)=-8*x^4*(A*x^2-2C*x+C).

Setting Y=(A*x-C)/W gives

    Y^2=2(W-6)(W^2-6W+36).

On the dense open where x,W,A are nonzero, the inverse is
x=(C+W*Y)/A, r=x-1/2, p=-2+4x+W*x^2. The Weierstrass form is

    YE^2=XE^3+96XE-448,
    XE=2(W-4), YE=2Y,
    discriminant=-143327232, j=2048/3.

The quadratic discriminant in x is a square factor times a cubic with
three distinct roots, so it is not a square even after extending the
constant field to an algebraic closure. The original H has no component
x=0, since H(p,-1/2)=8p(p+2)^2 is not the zero polynomial. This proves
geometric integrality and the genus statement. The
[self-contained identity source](../computations/verify_session_mf6_principal_elliptic_2026_10_08.py)
passed in a separate source-byte snapshot. Root compared its literal H
with the saved contact reconstruction. This is a reduction of that
candidate direction curve; it is not a full stratum exclusion.

**PROVED complete principal ancestor exclusion:** the following saved
data have now been reconstructed and exhausted in the complete open
and all projective boundary charts. The agent saved
the full first-normal/contact reconstruction and seven contact cofactors:

- [Complete contact data](../scratch/session-mf6-e1-principal-contact-2026-10-08.json)
  and [reconstruction source](../scratch/session-mf6-e1-principal-contact-2026-10-08.py).
- [Reduced six-by-seven contact matrix and seven cofactors](../scratch/session-mf6-e1-principal-minors-2026-10-08.json)
  and [source](../scratch/session-mf6-e1-principal-minors-2026-10-08.py).
- [Independent raw-cofactor factors](../scratch/audit-mf6-e1-principal-raw-minors-2026-10-08.json),
  [source](../scratch/audit-mf6-e1-principal-raw-minors-2026-10-08.py)
  and [completed printed output](../scratch/audit-mf6-e1-principal-raw-minors-2026-10-08.out).

The reduced matrix retains declared units and column frame factors.
Its seven maximal minors have full rank six on the declared open,
including the retained nonunit S branch. The complete first-normal
frame has an explicit nonzero free-row determinant. Two residual norms
and an exact quadratic-field gcd remove the possible rank drops.
Fresh all-35-column calculations exhaust the r=1/2, alternative defect
section at infinity and projective b0=0 charts. The node p=2,r=1/2
has dimension four with a fixed cubic times all linear forms; every
other valid principal fibre has dimension one. The node reduces to
P-037 rather than being discarded by a uniform dimension assertion.
See the [independent completeness proof](OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-principal-e1-d1-independent-completeness-auditmd)
and [frozen audit record](../validation/2026-10-08-principal-e1-d1-audit/audit-manifest.json).
Together with the accepted endpoints and primitive-point finite-flat
obstruction, this closes the entire e=1,d2=1 ancestor lane.

The principal unique-carrier problem is separate. The complement
carriers are all excluded in every mate degree, including the actual
nonreduced p=8,r=1/2 conductor. The remaining nonnormal carrier locus
is a finite proper closed subset of the integral parameter curve;
its exact enumeration remains OPEN. Saved weighted degree9,9,10
polynomial kernel generators are leads for this next step; inspect
their current completed audit status before relying on them.

An earlier message and the first elliptic verifier incorrectly used
H(p,-1/2)=8(p+2)^3. Root direct substitution corrected it to
8p(p+2)^2. The failed source revision and log are retained, and the
corrected verifier passed. Neither form vanishes identically in p,
so the no-vertical-component argument and Weierstrass identities are
unchanged. Do not reuse the incorrect fiber factor.

The principal e=1,d2=4 intrinsic-extension derivation was saved as
[an exploratory source](../computations/derive_session_localcoh_e1_d4_principal_extension_2026_10_08.py).
No completed output or independent cocycle identification was established
before interruption. Its proposed equation and its intersection with the
full quartic-rank incidence remain **OPEN**.

## Smooth-scroll conductors: an additional structural reduction

**PROVED with a separate written independent audit.** For any
smooth rational quartic-scroll normalization S->X, the actual downstairs
conductor is an ACM cubic curve with Hilbert polynomial 3m+1, including
reducible and nonreduced cases. The
[independent ACM proof](OCT8_SCROLL_CONDUCTOR_AND_ACM.md#source-2026-10-08-session-scroll-acm-independent-auditmd)
now verifies the entire cohomological route. Here is the root's
verification, retained as an additional derivation.

Let J_Gamma be the conductor's ideal in P3. Finite duality gives

    0 -> O_P3(-4) -> J_Gamma -> nu_*omega_S -> 0.

The intermediate cohomology of line bundles on P3 vanishes, so
H1(J_Gamma(m))=H1(S,K_S+mH). Write S=F_e, with e=0 or 2,
H=C_min+a f, a=e/2+2 and K_S=-2C_min-(e+2)f. For m>=2,
the ruling pushforward is a sum of line bundles of degrees

    ma-e-2-j e,  0<=j<=m-2.

The minimum is m(a-e)+e-2: it is 2m-2 for e=0 and m for e=2.
Every summand has vanishing H1, and fiber degree m-2>=0 makes R1
of the pushforward zero. For m=1, fiber degree is -1, so both direct
images vanish. For m<=0, Serre duality reduces the claim to
H1(S,(-m)H)=0; its ruling summands all have degree at least
(-m)(a-e)>=0. Thus H1(J_Gamma(m))=0 for every integer m.

Moreover H0(J_Gamma(1))=0 and H0(J_Gamma(2)) has dimension three.
The codimension-two ACM coordinate ring has Hilbert h-vector (1,2):
its degree is three, and its first two entries already sum to three.
An Artinian reduction is k[u,v]/(u,v)^2. Lifting its three quadratic
generators and applying graded Nakayama gives the Hilbert--Burch
resolution

    0 -> O_P3(-3)^2 -> O_P3(-2)^3 -> J_Gamma -> 0.

This establishes the determinantal starting point used by the now
completed smooth-scroll theorem. The nongorenstein rank-zero schemes
are classified; their entire generic canonical modules, Frobenius
annihilators and actual differential valuations exhaust the residual
nonreduced cases. The independently proved differential obstruction
uses the entire mate power, not an ordinary-pinch count or reduced-fibre
involution. See the [classification](OCT8_SCROLL_GORENSTEIN_AND_SINGULAR_AUDITS.md#source-2026-10-08-session-scroll-nongorenstein-cubic-classificationmd),
[exact Artin audit](OCT8_SCROLL_CONDUCTOR_AND_ACM.md#source-2026-10-08-session-scroll-artin-independent-auditmd)
and [full independent audit](OCT8_SCROLL_GORENSTEIN_AND_SINGULAR_AUDITS.md#source-2026-10-08-session-scroll-nongorenstein-independent-auditmd).
**PROVED:** every integral quartic with smooth rational quartic-scroll
normalization is excluded for fixed C0 in every mate degree. Singular
normalizations and other smooth polarization classes remain OPEN.

## Execution and provenance boundary

Research agents have ended with account usage-limit errors and later
resumed after verified resets. Completed
files survive; planned audits, unfinished calculations and absent output
files do not acquire completion status from the assignment. Root replay
handle 61220 completed with exit zero; the later literal-minor and repaired
elliptic root runs also completed. The principal raw-factor output ends
in DONE and has a complete JSON, but no root-observed terminal process
record was supplied for that agent run. Do not infer a live process from
its source or restart an overlapping calculation without checking handles.

The [reconciled validation index](../validation/2026-10-08-continuation-index/index.json)
at this earlier checkpoint contained 91 distinct top-level sources,
all with a latest PASS record, and 103 explicitly indexed executions.
Of these, the continuation added
28 distinct sources in 30 central records, a separate strengthened
Veronese revision, the independent first-family countercheck, four
independent principal executions, and three additional family2 sources
with six explicitly indexed executions including tensor checker repairs.
Nested imports and agent discovery commands are not inflated into
independent source or execution counts. The original 55-source baseline
was retained, not rerun merely because the date changed.

The two central continuation failures remain visible: the conormal
verifier lacked its provenance proof-note input, then passed with the
completed input closure; the first elliptic verifier had the false fiber
factor above, then passed in a separate repaired source snapshot.

The integrity audit also found that the former --add copier recopied
files absent from the *initial* manifest, even when they had already
been added. Consequently the superseded October 7 Veronese-classifier
source bytes were overwritten by the strengthened revision. Its original
hash, log and addition-manifest transition remain; its old source bytes
are **not** claimed retained. The current stronger source has a separate
snapshot, matching hash and fresh PASS. The copier now checks whether
the target already exists, preventing this repeated-copy behavior.
This loss is explicitly represented in the index, rather than hidden
behind an assertion of immutable historical snapshots.

At 2026-10-09 11:25:38 UTC the 2:01 AM local reset had passed, and live
usage allowed ordinary work. The finite principal-carrier and singular
normalization agents resumed; their assignments are not completed
results until the sources, outputs and scope are reconciled. The full
scroll and family2 quadratic audits already have durable final proofs.
No root process is claimed live from a saved script alone.

No Git commit or branch mutation was attempted. Current worktree files
and dated evidence, rather than the retained October 6 commit alone,
are the continuation state. No universal counterexample, unrestricted
two-form presentation of C0 or all-degree obstruction has been obtained.


---

## Source: 2026-10-08-session-first-endpoint-completeness-audit.md

# Completeness audit of the first rational endpoint family

Date: 2026-10-08. Auditor: the verification agent, independently of the
certificate-producing agents. Scope: characteristic zero, the fixed curve
`C0=[s^4:s^3t:st^3:t^4]`, primitive degree-two normal-dual direction,
pure cubic top coefficient `h=t`, and the **first** rational endpoint
family in the audited classification. No pre-existing dual, coefficient
certificate, checker, or canonical research record was edited for this
audit.

## 1. Verdict

**PROVED under the previously audited actual top map, coordinate bases,
and multiplication tensor:** every admissible direction parameter in
the first rational endpoint family, with its entire affine line of
quartic lower corrections, fails the target-`u` multiplication incidence.
There are no remaining direction or lower-parameter exceptions in this
family. This conclusion uses the geometric coverage argument, the generic
polynomial dual, all four exact exceptional-field duals, and the direct
cross-artifact checks preserved with this audit; it does not follow from
a generic rank calculation or from a printed `PASS` alone.

The older independent checkpoint
[`2026-10-07-session-localcoh-independent-audit.md`](OCT7_LOCALCOH_ENDPOINT_AND_SIMULTANEOUS_TARGETS.md#independent-audit)
retained 21 first-family geometric points after the quadratic exception
was closed. Its first-family exception list is superseded by the Q1, Q3,
and Q13 certificates and this combined audit. The complete exceptional
partition initially contained 23 geometric points, counting the two Q2
roots; all 23 are now covered, each for every lower parameter `lambda`.

This proves a family exclusion. It does not exclude the other three
classified endpoint families, nonendpoint top-zero strata, every quartic
ancestor, or every degree pair. The global STCI question and the
unrestricted status of `C0` remain open. Positive characteristic is not
covered by the rational arithmetic in this record.

## 2. Precisely which parameters are covered

Write the normalized direction as

```text
p(t)=1+a1*t+a2*t^2,   r(t)=1+b1*t+b2*t^2,
a1=(k^2+3)/(2(1-k^2)),
a2=-(k^2+2k+3)/(2(k+1)^2),
b1=(k-3)(k^2+2k+3)/((k-1)^2(k+1)),
b2=-2(k^2-4k+5)(k^2+2k+3)^2/((k-1)^3(k+1)^3).
```

The parameter chart is `k!=1,-1`. The fixed-degree homogeneous quadratic
resultant is

```text
8*(k^2+2k+3)^2*(9k^4-21k^3+5k^2-31k+134)
 /((k-1)^6*(k+1)^6).
```

Thus an admissible parameter also avoids the roots of
`qk=k^2+2k+3` and `B=9k^4-21k^3+5k^2-31k+134`. Using a four-by-four
Sylvester determinant matters: a dehomogenized resultant alone could
miss a common root at infinity when a leading coefficient vanishes.
The existing geometric audit and all exceptional-field checkers use
the fixed-size homogeneous determinant.

The rational classification covers the normalized finite directions.
On `2a1+1!=0` its inverse is

```text
k=(32a2+16a1^2+12)/(4(2a1+1)^2).
```

Modulo the top-image equation, this recovers both `a1` and `a2`, and
`k^2-1=-4/(2a1+1)`. The only omitted normalization point at
`2a1+1=0`, equivalently the limit `k=infinity`, is
`(a1,a2,b1,b2)=(-1/2,-1/2,1,-2)`. Its quadratics share `1-t`, so it is
nonprimitive. Neither `k=+/-1` nor `k=infinity` leaves an admissible
first-family point unexamined. The second choice of `b2` and the separate
`p(0)=0` boundary branches belong to the other families and remain outside
this conclusion.

For any admissible `k`, the actual top map `M` has shape `32x30` and rank
29. Its rational nonzero kernel vector `k0` spans its kernel. Consequently
all lifts of the fixed nonzero top are exactly

```text
alpha(k,lambda)=a*(k)+lambda*k0,   lambda in the base field.
```

The rank remains 29 after extension to any characteristic-zero field.
The pure-top check compares all 32 coefficients of
`t*p^i*r^(3-i)`, `i=0,1,2,3`, through degree seven. It verifies both the
constant seed and the vanishing top of the entire `lambda` direction.
This is the whole affine fibre, including every specialization of
`lambda`. A projective point `lambda=infinity` would have zero top after
projective rescaling and is not a lift of this fixed nonzero top. It
belongs to a different stratum; it is not an omitted point of this affine
fibre. Nonzero scalar multiples of `h=t` are absorbed by ancestor scaling
as in the geometric classification.

## 3. Exhaustive partition of the generic denominator

The generic certificate uses the cleared ancestor

```text
alpha_cleared=120*(k-1)^9*(k+1)^9*alpha(k,lambda).
```

This scalar is nonzero throughout the admissible chart. Its exact dual
target value, independent of `lambda`, is

```text
D=89514547200*(k-1)^14*(k+1)^11*Q2^5*qk^8*B*Q1*Q3*Q13,
Q2=k^2-4k+5,
Q1=3k^4-9k^3-19k^2-43k-4,
Q3=13k^4+26k^3+34k^2+6k-7,
Q13=729k^13+1620k^12+2889k^11-11268k^10-26574k^9-39642k^8
    +94014k^7+272968k^6+454897k^5+62256k^4-571463k^3
    -1210068k^2-966908k-379834.
```

The new independent countercheck reconstructs this polynomial exactly
from `dual_on_u`, verifies its degree is 76, and verifies all 30 cleared
ancestor coordinates against the rational seed and kernel. It also
checks every one of the eight distinct displayed factors is squarefree
over `QQ`, and that they are pairwise coprime. The factor multiplicities
are retained rather than replaced by a reduced zero locus.

| Factor | Multiplicity in D | Geometric treatment |
|---|---:|---|
| `k-1` | 14 | Outside the rational chart |
| `k+1` | 11 | Outside the rational chart |
| `qk` | 8 | Nonprimitive homogeneous direction |
| `B` | 1 | Nonprimitive homogeneous direction |
| `Q2` | 5 | Exact dual at both geometric roots, every `lambda` |
| `Q1` | 1 | Exact dual at all four geometric roots, every `lambda` |
| `Q3` | 1 | Exact dual at all four geometric roots, every `lambda` |
| `Q13` | 1 | Exact dual at all thirteen geometric roots, every `lambda` |

There is therefore no additional denominator locus. Off its roots the
generic dual gives `n^T L(alpha_cleared)=0` and `n^T u=D!=0`. Since
ancestor clearing is by a nonzero scalar, this excludes the original
ancestor as well. Every root that survives chart and primitivity tests
lies in exactly one of the four exceptional-field loci below.

## 4. Audit of the exceptional-field arithmetic

The Q1, Q2, Q3, and Q13 default checkers use exact `Fraction` arithmetic
in `K[lambda]`, with `K=QQ[k]/Qi`, and dictionaries for polynomial powers
of `lambda`. Convolution followed by descending reduction implements
the appropriate power-basis multiplication. In particular the Q3
relation is
`k^4=-2k^3-(34/13)k^2-(6/13)k+7/13`, exactly the relation from `Q3`.
For Q13 the lower coefficients divided by the leading coefficient 729
give the reduction relation; rational inverses are computed by solving
the exact multiplication matrix and their products are asserted to be
one. The Q13 rational-expression parser admits only integers, `k`,
rational arithmetic, and nonnegative integral powers.

The fields really are fields. Q2 has discriminant `-4`, hence is
irreducible over `QQ`. The other checkers prove irreducibility through
degree-preserving finite-field reductions and complete Rabin conditions:

| Polynomial | Prime | Monic coefficients in ascending order | Conditions |
|---|---:|---|---|
| Q1 | 23 | `[14,1,9,20,1]` | `x^(23^4)=x`, `gcd(f,x^(23^2)-x)=1` |
| Q3 | 17 | `[6,7,0,2,1]` | `x^(17^4)=x`, `gcd(f,x^(17^2)-x)=1` |
| Q13 | 53 | `[15,43,6,38,30,45,19,21,8,22,31,2,14,1]` | `x^(53^13)=x`, `gcd(f,x^53-x)=1` |

These are the complete tests: the first identity puts every irreducible
factor degree among the divisors of the total degree; for degree four
the gcd condition removes degrees one and two, and for prime degree
thirteen it removes degree one. The first identity also rules out
repeated factors. The integer leading coefficients survive reduction,
so irreducibility lifts to `QQ` by the usual primitive-polynomial
argument. The independent countercheck recomputes the monic reductions
and both conditions with SymPy's separate `galoistools` implementation;
it does not invoke the saved verifier bodies. All conditions passed.

In characteristic zero each `Qi` is separable. Its `deg(Qi)` embeddings
into an algebraically closed characteristic-zero field correspond to
all its geometric roots. Exact polynomial identities over `K[lambda]`
transport through every embedding. A nonzero denominator inverted in
`K` remains nonzero under every such embedding. There are no
`lambda`-denominators: the duals are polynomials, with entry 72 exactly
one, so specialization introduces no exceptional lower-parameter values.

## 5. Actual tensor, full lifts, and direct source binding

The retained tensor has header `30 18 74 542`: thirty ancestor coordinates,
eighteen actual quartic multiplier coordinates, seventy-four quotient
coordinates, and `30*18+2` columns. All exceptional-field checkers read
this tensor, assert the two final columns are `e72` and `e73`, and check
all eighteen identities

```text
sum(row=0..73) n[row](lambda) *
    sum(i=0..29) tensor[row,18*i+col]*alpha[i](lambda) = 0,
for col=0..17,
n[72](lambda)=1.
```

Thus if `L(alpha)*x=u` for any eighteen-coordinate multiplier vector,
left multiplication by `n` would give `0=1`. This argument is valid for
every `lambda` and every field embedding. It does not require trusting
the saved Macaulay2 module command, its evaluation ideal, or the claim
that the returned row spans an entire kernel. One correct exact row is
enough. Failure to reach `u` also rules out the stronger incidence that
requires both target eigenclasses.

The Q3 and Q13 source loops, field relations, irreducibility tests,
target checks, all 32 pure-top coefficient checks, rank-29 Gaussian
elimination, homogeneous resultants, and all eighteen tensor identities
were inspected rather than inferred from terminal success messages.
Q1 and Q2 follow the same complete identity pattern. Every coefficient
certificate binds the actual tensor, bases, top map, rational seed,
saved full dual, and auxiliary generation records by SHA256.

One provenance limitation needed an explicit additional check: the
default Q1/Q2/Q3 verifiers validate the saved field direction and pure-top
lift but do not themselves derive every constant seed/direction
coefficient from the rational first-family expressions. Hash binding
alone does not establish that derivation. The Q13 default verifier does
derive those coefficients directly. The new independent countercheck
supplies the missing direct comparison for **all four** fields: all
thirty seed coefficients, all thirty lower slopes, and all six direction
coefficients match the rational first-family source after exact modular
reduction. Every rational denominator is checked nonzero and inverted.
This closes the provenance limitation without editing the existing
checkers or relying on a fresh regeneration of their inputs.

## 6. Durable replay record

The new independent source is
[`countercheck.py`](../validation/2026-10-08-first-endpoint-audit/countercheck.py).
It is self-contained apart from the retained repository inputs and
SymPy, writes one deterministic JSON result, and invokes neither the
saved exceptional verifier bodies nor any generator. The final run
completed with exit code zero. Reproduce it from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/validation/2026-10-08-first-endpoint-audit/countercheck.py \
  > research/validation/2026-10-08-first-endpoint-audit/countercheck.log
```

Its
[`countercheck-result.json`](../validation/2026-10-08-first-endpoint-audit/countercheck-result.json)
contains the full factor partition, multiplicities, finite reductions,
all four coefficient-comparison results, and the hashes of every input.
The output
[`countercheck.log`](../validation/2026-10-08-first-endpoint-audit/countercheck.log)
is byte-identical to that JSON. Source SHA256:

```text
4fb9d7cf4b0a119bc8bfd0b1d5bb3a4bece08948bb9d44f505d3091ce2e74df0
```

Result/log SHA256:

```text
d5197c04be2c9fcb567c49b46fa8342345af4bc5dd7b0a3f965c07b61b57d34d
```

The reviewed source hashes and all coefficient-certificate hashes are
preserved in
[`audit-manifest.json`](../validation/2026-10-08-first-endpoint-audit/audit-manifest.json).
The original field proofs and their generation/replay routes are
preserved in the
[Q1 note](OCT7_LOCALCOH_ENDPOINT_AND_SIMULTANEOUS_TARGETS.md#q1-exception),
[Q3 note](OCT7_LOCALCOH_ENDPOINT_AND_SIMULTANEOUS_TARGETS.md#q3-exception), and
[Q13 note](OCT7_LOCALCOH_ENDPOINT_AND_SIMULTANEOUS_TARGETS.md#q13-exception), with Q2 in the
[independent endpoint audit](OCT7_LOCALCOH_ENDPOINT_AND_SIMULTANEOUS_TARGETS.md#independent-audit).
Root's central continuation validation records the full current checker
replays separately. This additional countercheck concerns parameter
coverage and source binding; it does not duplicate or substitute for
the eighteen-column tensor replay.

The next unresolved endpoint work starts with the second rational family
or one of the two `p(0)=0` boundary families. The first family should no
longer be listed as retaining Q1, Q3, or Q13 exceptions.
