# Entirely-thick branch: generic cluster and Rees-valuation framework

Date: 2026-10-07  
Status: **PROVED structural reformulation / OPEN global obstruction program**

## 1. Starting point

Starting remote \`main\`: \`7662a2ebb1dd561c1fb5e3c8958799b37d962c41\`.

For degrees \(a,b\) and exact generic normal orders \(p,q\ge2\), the audited necessary conditions are
\[
ab\ge4pq,\qquad 7ab+28pq\ge16(aq+bp),\qquad a\ge3p,\quad b\ge3q.
\]
Writing \(\alpha=a/p,\beta=b/q\), the \((3,3)\) boundary is impossible and the \((3,4)\) boundary forces the first exceptional intersection into constant sections.

The local family
\[
f=y^2+x^{2n+1},\qquad g=y^2+2x^{2n+1}
\]
shows that fixed first normal forms do not bound transverse intersection length.

## 2. Literature boundary

The required higher-contact language is classical on a transverse smooth surface.

- Noether's intersection formula expresses local intersection multiplicity as a sum of products of multiplicities over common infinitely-near points.
- Zariski-Lipman/cluster theory packages infinitely-near points using proximity relations and complete ideals in two-dimensional regular local rings.
- Rees valuations are the intrinsic divisorial valuations of the normalized blowup of an ideal and control its integral-closure filtration.
- Hilbert-Samuel multiplicity is invariant under integral closure. For a parameter ideal \(J=(f,g)\) in a two-dimensional regular local ring, \(e(J)=\ell(R/J)\).
- Segre numbers/classes and distinguished varieties give higher-dimensional blowup invariants for arbitrary ideals.
- Jaffe's iterated-curve-blowup method is directly relevant to STCI, but its strongest finite-list theorem assumes the two surfaces have no common singular point; the entirely-thick branch lies outside that hypothesis.

References checked include Casas-Alvero, *Singularities of Plane Curves*; Huneke-Swanson, *Integral Closure of Ideals, Rings, and Modules*; Gaffney-Gassler on Segre numbers; and Jaffe (1995).

Thus the generic transverse invariant below is standard mathematics applied to this STCI setup, not a novelty claim.

## 3. Generic transverse cluster theorem

Let \(\eta\) be the generic point of \(C\), and set
\[
R=\mathcal O_{\mathbf P^3,\eta},\qquad K=\kappa(\eta)=k(C),\qquad \mathfrak m=I_CR.
\]
Then \(R\) is a two-dimensional regular local ring. Let \(f,g\in R\) be the images of the defining forms and \(J=(f,g)\).

### Proposition 3.1 — generic intersection multiplicity

Under the STCI support hypothesis,
\[
\ell_R(R/J)=\frac{ab}{4}.
\]

Indeed, the two projective surfaces have no common surface component, so their proper intersection cycle has degree \(ab\). Its reduced support is exactly the irreducible degree-four curve \(C\), hence the fundamental cycle is \(m[C]\), where \(m=\ell_R(R/J)\). Taking degrees gives \(ab=4m\).

### Proposition 3.2 — Noether decomposition

The orders at the origin are \(m_0(f)=p\) and \(m_0(g)=q\). After a finite extension of \(K\), resolve the pair of plane-curve germs by successive point blowups. Noether's formula gives
\[
\frac{ab}{4}
=
pq+\sum_{P\succ0}[\kappa(P):K]\,m_P(f)m_P(g).
\tag{N}
\]
Therefore
\[
v:=\frac{ab}{4}-pq
=
\sum_{P\succ0}[\kappa(P):K]\,m_P(f)m_P(g).
\tag{E}
\]

Thus the second coordinate \(v\) of the audited first exceptional bidegree is exactly the total generic higher-contact budget.

### Corollary 3.3 — fixed-data finiteness

For fixed \((a,b,p,q)\), the number of common infinitely-near points after the origin is at most
\[
E=\frac{ab}{4}-pq,
\]
after passage to an algebraic closure and ignoring multiplicity. Hence the generic common cluster has bounded depth and bounded total number of vertices.

### Limitation 3.4 — normalized ratios do not suffice

Since
\[
E=pq\left(\frac{\alpha\beta}{4}-1\right),
\]
fixing only \((\alpha,\beta)\) does not bound cluster size independently of \(p,q\). At \((3,4)\),
\[
E=2pq.
\]

## 4. Correct higher-order objects

### Pair-sensitive object

Retain the common infinitely-near cluster with proximity relations, residue degrees, and the two multiplicity labels \(m_P(f),m_P(g)\). This distinguishes pairs with the same first tangent forms but different higher contact and directly refines the first exceptional cycle.

### Intrinsic ideal object

The normalized blowup of \(J=(f,g)\) and its Rees valuations give a canonical ideal-theoretic invariant. The integral-closure class determines \(e(J)\), hence the total transverse multiplicity \(ab/4\). It is, however, coarser than the labelled pair-cluster when the two distinguished generators must be tracked separately.

Recommendation: use Rees valuations as the intrinsic ideal-theoretic carrier, but use the labelled cluster (or a mixed refinement) for generator-sensitive inequalities.

## 5. Counterexample family

For
\[
f=y^2+x^N,\qquad g=y^2+2x^N,
\]
one has
\[
J=(f,g)=(y^2,x^N),\qquad \ell(R/J)=2N.
\]
The first tangent forms are always \(y^2\), but the integral-closure/Newton/Rees data changes with \(N\). After the first blowup the remaining Noether budget is
\[
2N-4,
\]
matching the transformed local calculation in the audited thick note.

## 6. Relation to the global exceptional bidegree

The first blowup gives
\[
(u,v)=
\left(
\frac{7ab}{4}+7pq-4(aq+bp),
\frac{ab}{4}-pq
\right).
\]
Equation (E) identifies \(v\) with the generic higher-contact sum. The coordinate \(u\) records global information not visible on one generic transverse slice.

This motivates a relative weighted cluster over \(C\): horizontal centers on successive blowups, equipped with degrees over \(C\), proximity relations, and the two vanishing orders.

## 7. Boundary \((3,4)\)

At \(a=3p,b=4q\),
\[
(u,v)=(0,2pq).
\]
The audited first-blowup argument shows that the support of the exceptional intersection is a union of constant sections, and the quadric residual divisor \(R_F\in|O_Q(2p,0)|\) has at most \(\min(p,q)\) distinct ruling roots.

The natural next problem is therefore to classify the descendants of these constant sections under successive blowups. A naive monotonicity assertion for \(u\) should not be assumed; this is tested in the continuation note.

## 8. Proved conclusions and limitations

**PROVED**

1. The generic transverse multiplicity is \(ab/4\).
2. The first-blowup excess \(v=ab/4-pq\) equals the total higher Noether contact budget.
3. Fixed \((a,b,p,q)\) gives finite generic cluster complexity.
4. Rees/integral-closure data distinguishes the fixed-first-symbol counterexample family.
5. Normalized ratios alone do not give uniform cluster-size bounds through this scalar budget.

**NOT PROVED**

1. No new normalized open region is excluded.
2. No uniform bound independent of \(p,q\) is known.
3. No monotonicity of horizontal twisting under successive blowups is established.
4. Rees valuations alone have not been shown to retain all generator-sensitive STCI data.
5. Persistent generic valuation centers have not yet been shown to force an extra projective common curve.
