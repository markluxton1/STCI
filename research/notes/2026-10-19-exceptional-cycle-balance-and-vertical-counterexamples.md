# Exceptional cycle balance and unbounded vertical degeneration

Status: **proposed structural statements with proofs and an independent reconstruction on the stated hypotheses; not a promoted result**. See the [independent audit](2026-10-19-exceptional-cycle-and-vertical-family-independent-audit.md), including the moving-direction addendum.

The fixed-curve statements concern the characteristic-zero quartic
\(C=C_0=[s^4:s^3t:st^3:t^4]\), with the accepted inputs
\(N_{C/\mathbf P^3}=\mathcal O_{\mathbf P^1}(7)^{\oplus2}\) and
\(C\subset Q\simeq\mathbf P^1\times\mathbf P^1\) of type \((1,3)\), after choosing the order of the rulings.
The broader hypothesis is \(C\subset V(F,G)_{\mathrm{red}}\), where the two surfaces have no common surface component. No integral-carrier, normality, smooth-root, or coprime-leading-form hypothesis is imposed.

Accepted numerical restrictions are recorded in [the entirely-thick topic](../results/entirely_thick.md). This note does not re-audit them or claim an unrestricted STCI exclusion. Its new contributions are residual-cycle corrections, support-sensitive conditional STCI exclusions in section 2a, and explicit counterexamples showing that vertical degeneration is unbounded with fixed transverse generic algebra and depends on the chosen generators.

## 1. Exact first-blowup balance

Let \(d=\deg F\), \(e=\deg G\), and let \(p,q\ge1\) be their exact generic orders along \(C\). Write
\[
[V(F,G)]=m[C]+R,\qquad r=\deg R=de-4m.
\]
All cycles below retain their scheme-theoretic generic multiplicities.

Let \(\pi:B=\operatorname{Bl}_C\mathbf P^3\to\mathbf P^3\), let \(H=\pi^*\mathcal O(1)\), and let \(E\) be its exceptional divisor. Use the convention that \(\mathbf P(N)\) parametrizes lines, so that
\[
E\simeq\mathbf P^1_{\rm base}\times\mathbf P^1_{\rm dir},\qquad
H|_E=4\alpha,\quad E|_E=7\alpha-\beta,
\]
where \(\alpha,\beta\) are pullbacks of \(\mathcal O(1)\) from the indicated factors.
Thus \(\alpha^2=\beta^2=0\) and \(\alpha\beta=1\).

The two strict surfaces have divisor classes \(dH-pE,eH-qE\), and have no common surface component. Their intersection is a pure effective one-cycle
\[
X=(dH-pE)(eH-qE)=\widetilde R+Y,
\]
where \(\widetilde R\) consists of the components outside \(E\) and is the strict-transform cycle of \(R\); \(Y\) consists of all components contained in \(E\). Write its divisor class on \(E\) as
\[
[Y]_E=A\alpha+B\beta,\qquad A,B\ge0,
\]
and define the residual contact number
\[
\lambda=E\cdot\widetilde R\ge0.
\]
The horizontal degree is \(B\); \(A\) includes the total multiplicity of vertical fibers as well as the other \(\alpha\)-contributions of horizontal curves.

**Proposition 1 (cycle balance).**
\[
\boxed{B=m-pq},\qquad
\boxed{A=\lambda+7(m+pq)-4(dq+ep)}.
\tag{1}
\]

**Proof.** The restrictions above give
\[
H^2E=0,\quad HE^2=-4,\quad E^3=-14.
\]
Consequently
\[
H\cdot X=de-4pq,
\qquad E\cdot X=4(dq+ep)-14pq.
\]
On the decomposition of \(X\), these two numbers are respectively
\(r+4B\) and \(\lambda+7B-A\). Use \(r=de-4m\) and solve. This proof only uses degrees and proper intersection; it makes no identification with a projectivized normal cone or the zero locus of two first symbols. ∎

In particular the complete strict-transform exceptional cycle, including vertical components, has a controlled numerical class. It is the **entire effective cycle** whose class enters (1); horizontal and vertical parts cannot be interchanged without compensating changes.

For a rational curve of degree \(c\) with explicitly balanced normal bundle \(\mathcal O(n)^{\oplus2}\), the identical proof gives
\[
B=m-pq,\qquad A=\lambda+n(m+pq)-c(dq+ep).
\tag{2}
\]
This extension assumes the balanced bundle and does not infer it from rationality.

## 2. Residual-degree inequalities and quadric rulings

**Proposition 2 (residual correction).** Under Proposition 1,
\[
\boxed{7de+28pq+5r\ge16(dq+ep).}
\tag{3}
\]
If no component of \(R\) lies on the unique quadric \(Q\), then the stronger inequality holds:
\[
\boxed{7de+28pq+r\ge16(dq+ep).}
\tag{4}
\]

**Proof.** The ideal sheaf \(I_C(3)\) is globally generated. One quick proof uses
\[
0\longrightarrow\mathcal O_{\mathbf P^3}(1)
\xrightarrow{\cdot Q} I_C(3)
\longrightarrow\mathcal O_Q(2,0)\longrightarrow0.
\]
The outer sheaves are globally generated and \(H^1(\mathcal O_{\mathbf P^3}(1))=0\), so global sections generate the middle sheaf: away from \(Q\), the multiples of \(Q\) suffice, and on \(Q\), the lifted generators of the quotient together with those multiples suffice. Hence \(3H-E\) is globally generated on the blowup, giving \(\lambda\le3r\). Substituting \(m=(de-r)/4\) into \(A\ge0\) in (1) proves (3).

If no residual component lies in \(Q\), its strict-transform cycle has nonnegative intersection with the effective strict quadric \(2H-E\). Therefore \(\lambda\le2r\), and the same substitution proves (4). ∎

The distinction between (3) and (4) is geometric. If
\[
R=R_{\rm out}+R_Q,\quad
\deg R_{\rm out}=r_{\rm out},\quad [R_Q]_Q=a\alpha_Q+b\beta_Q,
\]
where no component of \(R_{\rm out}\) lies in \(Q\), then
\[
\lambda_Q=C\cdot R_Q=3a+b,\qquad
\lambda_{\rm out}\le2r_{\rm out}.
\]
Indeed the strict transform of \(Q\) is isomorphic to \(Q\), since \(C\) is Cartier on it, and \(E|_{\widetilde Q}=C\). This gives the refined necessary condition
\[
\boxed{7de+28pq+r_{\rm out}+5a-3b\ge16(dq+ep).}
\tag{5}
\]
The ratio \(\lambda/r\) can equal three on a trisecant ruling line of \(Q\), so a universal bound \(\lambda\le2r\) would be false. No claim is made that (3) or (5) is attained by every prescribed collection of intersection data.

For \(r=0\), (3) returns the established entirely-thick numerical condition. It does not improve that STCI specialization. For the broader intersection problem, a positive left-hand deficit gives the explicit lower bound
\[
r\ge\max\left(0,\left\lceil\frac{16(dq+ep)-7de-28pq}{5}\right\rceil\right).
\]
The contact number \(\lambda\) depends on the residual cycle and \(C\), and does not depend on a presentation of its ideal by \(F,G\).

## 2a. A moving-direction refinement and conditional STCI exclusions

For each horizontal irreducible component \(\Gamma_i\) of the common zero locus of the first normal forms on \(E\), write
\[
[\Gamma_i]=a_i\alpha+b_i\beta,\qquad b_i>0.
\]
It is also a component of the proper intersection \(X\), with some positive generic intersection multiplicity \(n_i\). Every horizontal component of \(X\) arises this way. Let \(\nu\) be the total multiplicity of its vertical fibers. Then
\[
A=\nu+\sum_i n_i a_i,\qquad B=\sum_i n_i b_i.
\tag{6}
\]
In particular, if every common horizontal component has slope \(a_i/b_i\ge\rho\), then \(A\ge\rho B\). Together with (1), this gives
\[
\lambda+(7-\rho)m+(7+\rho)pq\ge4(dq+ep).
\tag{7}
\]
This is a support-dependent refinement; it does not presume that two first symbols determine their actual intersection multiplicities.

**Proposition 2a (unique moving-section case).** Suppose the only common horizontal root of the first normal forms is the graph \(\Gamma\) of a morphism \(\mathbf P^1\to\mathbf P^1\) of degree \(\epsilon\). Then
\[
\boxed{\nu=\lambda+(7-\epsilon)m+(7+\epsilon)pq-4(dq+ep)\ge0.}
\tag{8}
\]
This follows from \([\Gamma]=\epsilon\alpha+\beta\), since its multiplicity in \(Y\) is \(B=m-pq\). The common root can have arbitrary multiplicities in the two first symbols; neither transverse regularity nor coprime initial forms are assumed.

For an STCI presentation with exact orders \(p,q\ge2\), write \(\alpha_0=d/p\), \(\beta_0=e/q\). The accepted factor reduction rules out a quadric factor of either equation, and the entirely-thick restriction-to-quadric input gives \(\alpha_0,\beta_0\ge3\). This lower bound is **not** asserted for arbitrary residual intersections with a quadric factor. Equation (8) now yields the stronger necessary condition
\[
\boxed{\frac{7-\epsilon}{4}\alpha_0\beta_0+7+\epsilon
\ge4(\alpha_0+\beta_0).}
\tag{9}
\]
Two infinite conditional families are thereby excluded:

- If \(\epsilon\ge2\), no such STCI pair can have
  \(\min(\alpha_0,\beta_0)\le16/5\). Indeed increasing \(\epsilon\) decreases the left side of (9), because \(\alpha_0\beta_0/4>1\); for \(\epsilon=2\), (9) rearranges to
  \(\beta_0(5\alpha_0/4-4)\ge4\alpha_0-9\), impossible when \(3\le\alpha_0\le16/5\).
- If \(\epsilon=1\) and \(\alpha_0=3\), then \(\beta_0\ge8\). The unsloped condition alone only forces \(\beta_0\ge4\) on this boundary.

For example the unique-degree-two-section hypothesis excludes normalized degree pair \((\alpha_0,\beta_0)=(4,4)\), which the unsloped inequality allows. These conclusions are about the **common horizontal root support**, not arbitrary moving first relation sheaves. They allow arbitrary special-point degeneration and vertical fibers, whose effect is retained in \(\nu\ge0\). They do not exclude common-root configurations with additional lower-slope components, nor arbitrary STCI equations.

There is also a necessary condition with no prescribed common-root configuration. For every hypothetical entirely-thick STCI pair,
\[
B=pq(\alpha_0\beta_0/4-1)>0,\qquad
A-7B=pq\bigl(14-4\alpha_0-4\beta_0\bigr)<0.
\]
Equation (6) therefore forces **at least one horizontal common-root component of slope strictly less than seven**. In the unique-section case this implies the degree-independent bound \(\epsilon\le6\). The conclusion concerns the support of the two first normal forms; it is neither a full initial-ideal classification nor a formal-root lift theorem.

## 3. Unbounded vertical fibers with fixed entirely-thick generic data

**Proposition 3 (local counterexample family).** Fix integers \(p\ge2\), \(a>p\), \(b>p\). For each \(N\ge1\), in the smooth threefold \(\mathbf A^3_{t,u,v}\), put
\[
C=V(u,v),\qquad f=t^N u^p+v^a,\qquad g=f+u^b.
\]
Then the following hold, over any field (in particular in characteristic zero).

1. \((f,g)=(u^b,v^a+t^N u^p)\) is a complete-intersection ideal with radical \((u,v)\).
2. Its quotient is finite free of rank \(m=ab\) over \(k[t]\), with basis \(u^i v^j\), \(0\le i<b,0\le j<a\).
3. Both displayed equations have exact generic normal order \(p\).
4. On \(\operatorname{Bl}_C\mathbf A^3\), the intersection cycle of their two strict surfaces consists of the horizontal section \(u=0\) in the exceptional bundle, with coefficient \(ab-p^2\), and the vertical exceptional fiber over \(t=0\), with coefficient \(N(b-p)\).
5. The equally valid generators \((f,g-f)=(f,u^b)\) have orders \(p,b\). Their strict-surface intersection contains no vertical fiber, and has the same horizontal section with coefficient \(b(a-p)\).

**Proof.** Monic division first by \(u^b\), then by \(v^a+t^N u^p\), proves the basis assertion. The quotient is free over \(k[t]\), so this is a flat lci family with constant transverse length. Its radical is \((u,v)\) because \(u\) is nilpotent, followed by \(v\). There is no residual one-dimensional component.

In the blowup chart \(v=uw\), the two displayed strict equations generate
\[
(t^N+u^{a-p}w^a,\ u^{b-p}).
\]
At the generic point of the exceptional fiber \(u=t=0\), \(w\) is a transcendental unit, and this quotient has length \(N(b-p)\): it is free of rank \(N\) over \(k(w)[u]/(u^{b-p})\), by monic division in \(t\). This proves the vertical multiplicity.

In the other chart \(u=vw\), the strict ideal is
\[
(t^Nw^p+v^{a-p},\ v^{b-p}w^b).
\]
Over \(k(t)\), its support is \(v=w=0\), the horizontal section corresponding to the normal direction \(u=0\). Additivity of intersection multiplicity in the factored second equation gives
\[
(b-p)\,\operatorname{length}K[[w]]/(t^Nw^p)
+b\,\operatorname{length}K[[v]]/(v^{a-p})
=(b-p)p+b(a-p)=ab-p^2.
\]
There are no other components: away from the exceptional locus the blowup is an isomorphism and \(V(f,g)\) has support \(C\); within that locus, the two initial forms have the sole generic normal direction \(u=0\), and their only common entire fiber is at \(t=0\).

For the replacement pair, the strict equation of \(u^b\) is the unit one in the first chart, excluding a vertical fiber. In the second chart the strict ideal is
\((t^Nw^p+v^{a-p},w^b)\), free of rank \(b(a-p)\) over \(k[t]\). This proves the final assertion. ∎

With fixed \(p,a,b\), generic normal orders and length remain fixed while the vertical coefficient is unbounded. Thus no upper bound for vertical multiplicity can depend only on \(m,p,q\); even flatness and a pure \(C\)-supported lci do not supply such a bound. This is a local statement: it does **not** construct an STCI of the fixed quartic.

The stronger conclusion with a fixed **generic algebra**, rather than just fixed numerical data, holds on the subsequence \(N=aL\). Over \(K=k(t)\), the substitution \(v=t^L v'\) identifies every such quotient with
\[
K[u,v']/(u^b,v'^a+u^p).
\]
The substitution preserves the maximal-ideal filtration, while the vertical coefficient \(aL(b-p)\) is unbounded. Thus even the isomorphism class of the generic filtered algebra does not bound vertical multiplicity of these chosen-pair strict transforms.

## 4. An actual projective pure-support example

Vertical fibers can occur even for homogeneous two-hypersurface presentations on projective three-space. For \(p\ge2,N\ge1\), take coordinates \([T:U:V:W]\) and
\[
F=T^NU^p+V^{N+p},\qquad
G=F+U^{N+p}.
\]
Both equations have degree \(D=N+p\), no common surface component, and
\[
\sqrt{(F,G)}=(U,V).
\]
Their intersection is a complete-intersection thickening of the line \(L=V(U,V)\), of generic length \(D^2\). Their generic orders along \(L\) are \(p,p\). Near \([0:0:0:1]\), this is Proposition 3 with \(a=b=N+p\), so the first strict-surface intersection contains the exceptional fiber there with coefficient \(N^2\). The leading forms have no other common entire fiber. Replacing \(G\) by \(G-F=U^{N+p}\) removes that vertical fiber. This homogeneous example concerns a line with a different normal bundle; its role is to refute a general vertical-implies-residual principle, not to settle any quartic case.

## 5. Frontier impact and unresolved interface

The numerical class of the entire first-blowup exceptional cycle satisfies an exact residual-contact balance. The contact bound is sensitive to residual curves on the unique quadric and to its two rulings. The slopes of actual common normal directions refine the numerical obstruction and exclude the conditional infinite families in §2a. Vertical exceptional multiplicities can nevertheless be arbitrarily large while the generic filtered algebra is fixed (using the subsequence above), and they can disappear after an invertible generator change.

Consequently a proposed intrinsic invariant built from successive intersections of **individual strict equations** needs an explicit proof of generator invariance, or explicit correction terms. The normal cone of the quotient and the saturated full initial ideal remain distinct from these chosen-pair cycles. The examples do not rule out invariants of the full filtered ideal.

The precise unsolved step relevant to the quartic is to further constrain the distribution of the effective class \((A,B)\) among horizontal curves and vertical fibers using the globally realizable full normal filtration. The residual-correction inequality alone recovers the inherited inequality when \(R=0\); section 2a adds new conditional exclusions using horizontal support slopes. The unrestricted characteristic-zero \(C_0\) STCI problem remains open.

Independent audit: [independent reconstruction of cycle balance, residual bounds, degeneration examples, and the moving-direction refinement](2026-10-19-exceptional-cycle-and-vertical-family-independent-audit.md). No canonical result or question record is modified by this note.
