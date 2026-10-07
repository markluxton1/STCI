# Entirely-thick branch: relative blowup budget on the \((3,4)\) boundary

Date: 2026-10-07  
Status: **PROVED recursion and finiteness / OPEN rigidity step**

This note continues \`2026-10-07-entirely-thick-rees-valuation-framework.md\`.

## 1. Blowup recursion along a horizontal common center

Let \(Y\) be a smooth threefold and let \(D,D'\) be effective Cartier divisors with proper one-dimensional intersection. Let \(Z\subset Y\) be a smooth curve contained in both divisors. Write
\[
r=\operatorname{ord}_Z(D),\qquad s=\operatorname{ord}_Z(D').
\]
Blow up \(Z\):
\[
\pi:Y_1=\operatorname{Bl}_Z(Y)\to Y
\]
with exceptional divisor \(E\). The strict transforms satisfy
\[
\widetilde D=\pi^*D-rE,\qquad
\widetilde D'=\pi^*D'-sE.
\]

### Proposition 1.1 — cycle recursion

In \(A_1(Y)\),
\[
\pi_*\bigl([\widetilde D]\cdot[\widetilde D']\bigr)
=
[D]\cdot[D']-rs[Z].
\tag{R}
\]

**Proof.**
Expand
\[
(\pi^*D-rE)(\pi^*D'-sE).
\]
For a blowup along a codimension-two smooth center,
\[
\pi_*E=0,\qquad \pi_*(E^2)=-[Z].
\]
The two mixed terms therefore push forward to zero and the \(rsE^2\) term pushes forward to \(-rs[Z]\).

This is the relative threefold analogue of the first step in Noether's plane-curve formula.

## 2. Recursion with a finite cover of the parent center

Suppose a later smooth horizontal center \(Z'\) maps finitely onto an earlier center \(Z\) with degree \(d\). If the current strict transforms have orders \(r',s'\) along \(Z'\), then after blowing up \(Z'\) its contribution pushed all the way down to \(Z\) is
\[
d\,r's'[Z].
\tag{R_d}
\]

Thus every common horizontal descendant consumes a positive integer amount of the coefficient of its ancestral horizontal component.

## 3. Application to the \((3,4)\) boundary

For \(a=3p,b=4q\), the first blowup \(B=\operatorname{Bl}_C\mathbf P^3\) has exceptional intersection cycle
\[
W=D\cdot D'=\sum_{j=1}^r c_jT_j,
\]
where the \(T_j\) are distinct constant sections and
\[
r\le\min(p,q),\qquad c_j\ge1,\qquad \sum_j c_j=2pq.
\tag{B}
\]

Fix one \(T_j\). Blow up every horizontal common center above \(T_j\) until the strict transforms no longer meet generically above it. Iterating Proposition 1.1 gives a sectionwise relative Noether identity
\[
c_j
=
\sum_{\nu\in\mathcal T_j}
d_\nu r_\nu s_\nu,
\tag{SN}
\]
provided the terminal intersection has no horizontal component above \(T_j\). Here:

- \(\mathcal T_j\) is the finite tree of horizontal common centers above \(T_j\);
- \(d_\nu\) is the degree of the center over its parent/ancestral section as measured after pushdown;
- \(r_\nu,s_\nu\) are the two vanishing orders along that center.

If a horizontal component survives indefinitely, the pair has a persistent divisorial valuation/common formal branch; converting that persistence into an actual projective common curve is a separate algebraization problem and is not asserted here.

### Corollary 3.1 — relative horizontal finiteness

For every terminating tree,
\[
\#\mathcal T_j\le c_j,
\qquad
\sum_j\#\mathcal T_j\le2pq.
\]
More generally, the total degree-weighted number of centers is bounded by \(2pq\).

Thus the \((3,4)\) boundary has a finite relative horizontal cluster for fixed \(p,q\), not merely a finite cluster on one generic transverse slice.

## 4. Why the proposed \(u\)-monotonicity is not justified

The first exceptional bidegree is \((u,v)=(0,2pq)\). It is tempting to regard \(u\) as a nonnegative energy that later horizontal twisting must increase. Proposition 1.1 shows that this is not automatic.

A blowup of a constant section removes \(rs[T_j]\) from the pushforward intersection cycle. New intersection curves may live on the new exceptional ruled surface. Their geometry can twist relative to \(T_j\) while their pushforward remains a multiple of the same class \([T_j]\). Therefore the original \(u=0\) records the support/class of the first-stage cycle but does not by itself constrain all later ruled-surface bidegrees.

So the candidate implication

\[
u=0\Longrightarrow\text{all later horizontal centers are constant/untwisted}
\]

is **not proved and should not be used**. A new invariant is needed if later twisting is to be controlled.

This is compatible with Jaffe's warning that iterated-blowup type sequences require extra control in the presence of common singularities.

## 5. Refined invariant suggested by the recursion

The natural object is now a **decorated relative cluster**
\[
\mathscr C(F,G/C)
\]
whose vertices are horizontal common centers on successive blowups and whose decorations include

\[
(d_\nu,r_\nu,s_\nu,N_{Z_\nu/Y_\nu},\text{proximity data}).
\]

The first three entries control the intersection budget. The normal bundle of the center in the current threefold controls the geometry of the next exceptional ruled surface:
\[
E_{\nu+1}=\mathbf P(N_{Z_\nu/Y_\nu}).
\]

This is the missing global datum that the generic Rees valuations over \(k(C)\) do not see.

## 6. Relation to the quadric repeated-root constraint

At the \((3,4)\) boundary the audited argument also gives
\[
R_F\in H^0(Q,O_Q(2p,0))
\]
with at most \(r\le\min(p,q)\) distinct ruling roots. Each root corresponds to the intersection of a first-stage constant section \(T_j\) with the quadric-direction section \(S_Q\).

Hence the \(2p\) root multiplicity is distributed among at most \(\min(p,q)\) sectionwise cluster budgets \(c_j\), whose total is \(2pq\).

The next useful inequality must relate:

1. the root multiplicity \(M_j\) of \(R_F\) at the point corresponding to \(T_j\);
2. the coefficient \(c_j\) of \(T_j\) in \(W\);
3. the first blowup orders \(r_j,s_j\) of \(D,D'\) along \(T_j\);
4. the normal bundle \(N_{T_j/B}\).

A lower bound of the form
\[
c_j\ge \Phi(M_j,p,q)
\]
strong enough that
\[
\sum_j\Phi(M_j,p,q)>2pq
\]
would exclude the boundary. No such bound is currently proved.

## 7. Immediate next calculation

Compute \(N_{T/B}\) for a constant section \(T\subset E\simeq\mathbf P^1\times\mathbf P^1\subset B\), and then compute the divisor classes cut on
\[
E_T=\mathbf P(N_{T/B})
\]
by the strict transforms after blowing up \(T\).

This is concrete because:

- \(N_{T/E}\) is determined by the self-intersection of the constant section in \(E\);
- \(N_{E/B}|_T=O_E(E)|_T\) is known from
  \[
  E|_E=O_E(7,-1);
  \]
- the extension
  \[
  0\to N_{T/E}\to N_{T/B}\to N_{E/B}|_T\to0
  \]
  can therefore be analyzed explicitly on \(T\simeq\mathbf P^1\).

That calculation should determine whether the next exceptional ruled surface has enough positivity/negativity to force a new inequality connecting \(c_j\) to the repeated-root multiplicity.
