# Entirely-thick branch: generic cluster and Rees-valuation framework

Date: 2026-10-07  
Status: **PROVED structural reformulation / OPEN global obstruction program**

## 1. Starting point

This note starts from remote `main` at

`7662a2ebb1dd561c1fb5e3c8958799b37d962c41`.

The current canonical state proves only necessary restrictions for an entirely-thick STCI pair. If the two surfaces have degrees (a,b) and exact generic normal orders (p,q\ge2) along the smooth rational quartic (C), then

[
ab\ge4pq,qquad
7ab+28pq\ge16(aq+bp),qquad
a\ge3p,quad b\ge3q.
]

Writing (alpha=a/p,eta=b/q), the simultaneous boundary ((3,3)) is impossible, while ((3,4)) forces the first exceptional intersection into constant sections and the quadric residual data into repeated-root geometry.

The existing local family
[
f=y^2+x^{2n+1},qquad g=y^2+2x^{2n+1}
]
shows that fixed first normal forms do not bound transverse intersection length.

## 2. Literature boundary

The higher-contact language needed here is classical on a transverse smooth surface.

* Noether's intersection formula expresses the local intersection multiplicity of two plane-curve germs as the sum
  [
  i(f,g)=sum_P [kappa(P):K],m_P(f)m_P(g)
  ]
  over common infinitely-near points.
* Zariski-Lipman theory packages finite clusters/point bases by complete ideals in a two-dimensional regular local ring, with proximity inequalities and factorization into simple complete ideals.
* Rees valuations are the intrinsic divisorial valuations of the normalized blowup of an ideal and determine its integral-closure filtration.
* Hilbert-Samuel multiplicity is invariant under integral closure. For a parameter ideal (J=(f,g)) in a two-dimensional regular local ring, (e(J)=\ell(R/J)).
* Segre numbers/classes and distinguished varieties provide the higher-dimensional/global blowup language for arbitrary ideals; they depend only on the integral-closure class of the ideal.
* Jaffe (1995) already uses iterated curve blowups in the STCI problem. His strongest finiteness theorem assumes the two defining surfaces have no common singular point; the entirely-thick branch is precisely outside that hypothesis.

Useful references checked in this run include Casas-Alvero, *Singularities of Plane Curves*; Lipman's work on complete ideals and proximity inequalities; Huneke-Swanson, *Integral Closure of Ideals, Rings, and Modules*; Gaffney-Gassler on Segre numbers; Achilles-Manaresi-Pruschke on mixed multiplicities/Segre classes; and Jaffe's 1995 iterated-blowup paper.

Accordingly, the generic transverse invariant below is **standard mathematics applied to the STCI setup**, not a novelty claim.

## 3. Generic transverse cluster theorem

Let (eta) be the generic point of (C), let
[
R=mathcal O_{mathbf P^3,eta},
qquad K=kappa(eta)=k(C),
qquad mathfrak m=I_C R.
]
Then (R) is a two-dimensional regular local ring with residue field (K).

Let (f,gin R) be the images of the two defining forms (F,G), and put
[
J=(f,g).
]

### Proposition 3.1 — generic intersection multiplicity

Under the STCI support hypothesis,
[
ell_R(R/J)=rac{ab}{4}.
]

**Proof.**
The two projective surfaces have no common surface component, so their proper intersection cycle has degree (ab). Its reduced support is exactly the irreducible degree-four curve (C), hence the fundamental cycle is (m[C]) for the generic intersection multiplicity
[
m=ell_R(R/J).
]
Taking degrees gives (ab=4m).

### Proposition 3.2 — Noether decomposition of the first-blowup excess

The orders at the origin are
[
m_0(f)=p,qquad m_0(g)=q.
]
After a finite extension of (K), resolve the pair of plane-curve germs by successive point blowups. Then
[
rac{ab}{4}
=
pq+
sum_{Psucc0}[kappa(P):K],m_P(f)m_P(g).
	ag{N}
]

Consequently the coefficient
[
v=rac{ab}{4}-pq
]
computed globally in the first blowup is exactly the total generic higher-contact contribution:
[
v=
sum_{Psucc0}[kappa(P):K],m_P(f)m_P(g).
	ag{E}
]

**Proof.**
This is Noether's intersection formula applied in the two-dimensional regular local ring (R), with the origin separated from the later common infinitely-near points. Proposition 3.1 identifies the left side with (ab/4).

### Corollary 3.3 — finite generic cluster for fixed numerical data

The number of common infinitely-near points after the origin, counted without multiplicity after passage to an algebraic closure, is at most
[
E:=rac{ab}{4}-pq.
]

In particular, for fixed ((a,b,p,q)) the generic higher-contact tree has bounded depth and bounded total number of vertices.

This is a genuine finite-combinatorial reduction at fixed numerical data.

### Limitation 3.4 — no normalized uniform finiteness from this budget alone

Writing (alpha=a/p,eta=b/q),
[
E=pqleft(rac{alphaeta}{4}-1ight).
]
Thus fixing only ((alpha,eta)) does not bound the number of possible vertices independently of (p,q).

At the ((3,4)) boundary,
[
E=2pq.
]
Therefore the first global numerical budget alone cannot yield a finite list of valuation trees depending only on the normalized point ((3,4)). Any such stronger theorem must use additional global geometry: horizontal twisting on the exceptional ruled surface, the quadric residual divisors, normalization/conductor geometry, or a monotonicity theorem not supplied by the local multiplicity identity.

## 4. What the correct invariant is

There are two closely related levels.

### 4.1 Pair-sensitive object: the common infinitely-near cluster

For the pair ((f,g)), retain the finite rooted cluster
[
mathcal K(f,g)=
{P:;P	ext{ is infinitely near to }0, 
m_P(f)m_P(g)>0}
]
with:

* proximity relations;
* residue degrees ([kappa(P):K]);
* the two multiplicity labels (m_P(f),m_P(g)).

Its weighted size is exactly (ab/4), and its part beyond the root is exactly (v).

This object passes all three immediate tests:

1. it distinguishes pairs with identical first tangent forms but different higher contact;
2. it refines the first-blowup exceptional cycle;
3. it has a direct intersection-theoretic meaning.

### 4.2 Intrinsic ideal object: normalized blowup / Rees valuations of (J=(f,g))

The normalized blowup of (J) and its exceptional prime divisors give a finite intrinsic collection of Rees valuations. The integral-closure class of (J) determines (e(J)), hence determines the total transverse multiplicity (ab/4).

This is more canonical than a chosen resolution, but it is coarser than the fully labelled pair-cluster when one wants to know how the contact is distributed between the two distinguished generators (f) and (g).

**Recommendation.** Use the normalized blowup/Rees valuations as the intrinsic carrier of the ideal-theoretic data, but use the labelled cluster (or an equivalent mixed/degree-function refinement) for inequalities involving the two individual equations.

## 5. Test on the existing counterexample family

For
[
f=y^2+x^N,qquad g=y^2+2x^N,qquad N=2n+1,
]
one has
[
J=(f,g)=(y^2,x^N),
qquad
ell(R/J)=2N=4n+2.
]

The first tangent forms are always (y^2), but the integral-closure/Newton/Rees data of ((y^2,x^N)) changes with (N). Thus Rees/cluster data detects exactly the information that the first tangent form forgets.

After the first blowup, Noether's identity gives remaining budget
[
2N-4=4n-2,
]
matching the explicit transformed calculation already in the repository.

## 6. Relation to the global exceptional bidegree

The existing first-blowup calculation gives
[
(u,v)=
left(
rac{7ab}{4}+7pq-4(aq+bp),
rac{ab}{4}-pq
ight).
]

Equation (E) identifies the second coordinate (v) with the generic sum of higher infinitely-near contact contributions.

The first coordinate (u) is therefore the genuinely global datum not visible on one generic transverse slice. It measures horizontal twisting/variation of the common-contact locus over (C). A successful global valuation theory should refine the scalar local budget (v) by assigning horizontal degree data to the divisorial valuations/centers dominating (C).

This suggests that the next invariant should not be merely a valuation tree over (K=k(C)), but a **relative weighted cluster over (C)**: horizontal centers on successive blowups, equipped with their degrees over (C), proximity relations, and the two vanishing orders.

## 7. Boundary ((3,4))

At (a=3p,b=4q),
[
(u,v)=(0,2pq).
]

The audited first-blowup argument shows that every component of the exceptional intersection is a constant section. In the relative-cluster language this says that all first-stage horizontal centers have degree one and zero total horizontal twisting budget.

This is substantially stronger than the generic slice statement. It is the place to seek a rigidity theorem:

> **Candidate next proposition.**  
> On the ((3,4)) boundary, classify relative clusters whose first horizontal centers are constant sections, whose total higher Noether budget is (2pq), and whose quadric residual divisor (R_Fin |O_Q(2p,0)|) has at most (min(p,q)) distinct ruling roots. Show that either the relative cluster acquires positive horizontal twisting at a later stage (contradicting (u=0) if a suitable monotonicity theorem holds), or a persistent center descends to an extra common curve/fixed factor.

The missing step is the parenthetical monotonicity statement. It should not be assumed: Jaffe's work is a warning that monotonicity of infinitely-near type sequences is exactly where iterated-blowup arguments can fail without extra hypotheses.

## 8. Consequences and limitations

### PROVED

1. The generic transverse multiplicity is (ab/4).
2. The first-blowup excess (v=ab/4-pq) equals the total higher Noether contact budget.
3. Fixed ((a,b,p,q)) gives a finite bound on generic common-cluster complexity.
4. Rees/integral-closure data distinguishes the repository's fixed-first-symbol counterexample family.
5. Normalized ratios alone do not give a uniform bound on cluster size via the existing scalar budget.

### NOT PROVED

1. No new normalized open region is excluded.
2. No theorem yet bounds relative-cluster complexity independently of (p,q).
3. No monotonicity of horizontal degree/twisting under successive blowups has been proved.
4. Rees valuations of (J) alone have not been shown to encode all generator-sensitive data needed for the STCI inequalities.
5. No implication from persistent generic valuation centers to an actual extra projective common curve has yet been established.

## 9. Strongest next theorem

The highest-value next step is a **relative proximity/bidegree formula**.

Construct successive blowups along horizontal common centers above (C). For each center (Z_i), record

[
(r_i,s_i,d_i,epsilon_i)
=
(v_i(F),v_i(G),deg(Z_i/C),	ext{horizontal twisting/proximity data}).
]

Prove an identity or inequality refining
[
(u,v)
]
so that:

* the (v)-coordinate specializes to Noether's sum (sum m_P(f)m_P(g));
* the (u)-coordinate is a nonnegative weighted sum of horizontal degrees/twisting terms;
* equality (u=0) forces every later horizontal center to remain constant/untwisted.

If the last bullet holds, the ((3,4)) boundary becomes a realistic target for a complete structural exclusion. If it fails, an explicit relative-cluster counterexample will identify precisely what additional normalization/conductor information is required.
