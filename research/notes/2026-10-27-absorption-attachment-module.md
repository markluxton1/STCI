# Residual attachment from the full primary equation module

Date: 2026-10-27. Author: coordinating agent. Status: **independently reviewed provisional degree-independent interface**; see the [audit](2026-10-27-absorption-attachment-module-audit.md). The proof uses standard Nakayama, linkage duality and linear algebra over a DVR. No literature novelty or canonical promotion is claimed. The new proposed use is to connect the equation module of the full marked primary component to actual residual attachment, without curvilinearity or local complete-intersection hypotheses on that component.

## 1. Exact setting and relation to prior work

Let \(k\) be algebraically closed of any characteristic, let \(C\) be a smooth connected curve in \(\mathbf P^3_k\), and let \(Y=V(F_a,G_b)\) be a proper complete intersection containing \(C\). Let

\[
I=I_C,\quad L=I_Y,\quad J=I_T,
\]

where \(T\) is the **full \(C\)-primary component** of \(Y\), with its actual induced scheme structure. Let \(D\) be the scheme linked to \(T\):

\[
I_D=L:J.
\]

The curve \(T\) is locally Cohen--Macaulay: it is pure of dimension one, since its ideal is the isolated primary component of the unmixed complete-intersection ideal. Classical linkage makes \(D\) locally CM as well. It has no component equal to \(C\), and its fundamental cycle is the residual \(R=[Y]-m[C]\). This \(D\) is generally different from the once-linked curve \(L:I_C\), which retains marked thickness when \(m>1\). The empty \(D\) case is allowed, with zero modules below.

Retrieve [INDEX](../INDEX.md) then [MAP](../MAP.md). Relevant inherited interfaces are [R-0030](../results/local_filtration_comparison_defect.md) for a filtered comparison module, [R-0019](../results/quasiprimitive_residual_cycles.md) for saturated quasiprimitive cycle identities, and the [one-step boundary note](2026-10-27-one-step-boundary-obstruction.md), especially §§2,5. The latter already gives the determinant contact test for an arbitrary *lower* curvilinear thickening and an Ext repair criterion. None of those results is re-proved or promoted here. The present \(T\) is the full primary component of an actual pair, so its source determinant is always generically nonzero; this is a different role for the module.

## 2. The attachment module and its exact support

Define coherent \(\mathcal O_C\)-modules

\[
\mathcal E_T=J/IJ,\qquad
\mathcal Q_{Y,C}=J/(L+IJ).
\]

Actual equations give

\[
\rho:\mathcal O_C(-a)\oplus\mathcal O_C(-b)\longrightarrow\mathcal E_T,
\qquad\mathcal Q_{Y,C}=\operatorname{coker}\rho.       \tag{1}
\]

At the generic point of \(C\), \(J=L\); hence \(\rho\) is an isomorphism on the two-dimensional minimal-generator space there. In particular \(\mathcal E_T\) has generic rank two and \(\mathcal Q_{Y,C}\) is torsion.

**Support criterion.**

\[
\operatorname{Supp}\mathcal Q_{Y,C}
=C\cap\operatorname{Supp}D.                          \tag{2}
\]

Indeed, for a closed point \(p\in C\), \(\mathcal Q_p=0\) means \(J_p=L_p+I_pJ_p\). Apply Nakayama to the finite module \(J_p/L_p\), with \(I_p\) inside the local maximal ideal, to obtain \(J_p=L_p\). This says that \(Y\) has only its full marked primary component near \(p\). Conversely that equality gives \(\mathcal Q_p=0\). Since primary decomposition of \(Y\) has no embedded components, equality is equivalent to no residual component passing through \(p\).

For a projective CI, connectedness now gives

\[
\mathcal Q_{Y,C}=0
\quad\Longleftrightarrow\quad
\operatorname{Supp}Y=C.                             \tag{3}
\]

Only this last global equivalence uses connectedness. Formula (2) is local and does not assert every residual component individually meets \(C\).

## 3. Torsion correction to the determinant

Let \(\mathcal T_T=\operatorname{tors}_{\mathcal O_C}\mathcal E_T\), and put

\[
\overline{\mathcal E}_T=\mathcal E_T/\mathcal T_T.
\]

This is a rank-two vector bundle on the smooth \(C\). The induced map

\[
\bar\rho:\mathcal O_C(-a)\oplus\mathcal O_C(-b)
\longrightarrow\overline{\mathcal E}_T
\]

is generically an isomorphism and injective, with determinant

\[
\theta=\det\bar\rho\in
H^0(C,\det\overline{\mathcal E}_T\otimes\mathcal O_C(a+b))
\]

nonzero. The image of \(\rho\) meets \(\mathcal T_T\) trivially, because its composite to the torsion-free quotient is injective. Thus

\[
0\longrightarrow\mathcal T_T\longrightarrow\mathcal Q_{Y,C}
\longrightarrow\operatorname{coker}\bar\rho
\longrightarrow0.                                  \tag{4}
\]

Over each DVR \(\mathcal O_{C,p}\), Smith normal form gives

\[
\boxed{\ \operatorname{length}\mathcal Q_p
=\operatorname{length}(\mathcal T_T)_p+
\operatorname{ord}_p(\theta).\ }                    \tag{5}
\]

Furthermore \(\mathcal T_T\) is supported precisely where \(T\) fails to be locally a complete intersection. If the torsion vanishes at \(p\), \(\mathcal E_T\) is free of rank two there, and its residue fiber shows \(\mu(J_p)=2\). A height-two ideal with these two generators in a regular local ring is a regular sequence. Conversely a local regular-sequence presentation of \(J_p\) makes \(J_p/I_pJ_p\) free of rank two on \(C\), since all Koszul coefficients vanish on \(C\).

Consequently the determinant alone need not detect every attachment: it omits the non-lci contribution from the full primary component.

## 4. Identification with the actual attachment divisor

Classical linkage duality gives

\[
J/L\simeq\omega_D\otimes\omega_Y^{-1}
=\omega_D(4-a-b).
\]

Taking the quotient by \(I\) identifies

\[
\mathcal Q_{Y,C}\simeq
\omega_D(4-a-b)\otimes_{\mathcal O_{\mathbf P^3}}\mathcal O_C.   \tag{6}
\]

One must not replace a canonical module by a structure sheaf without justification. In this particular codimension-two intersection, their **lengths after restriction** agree even when \(D\) is not Gorenstein.

Here is the local proof. Put \(B=\mathcal O_{D,p}\), a one-dimensional CM local ring, and let \(I_CB=(f,g)\). Since \(D\) has no component equal to \(C\), this is primary to the maximal ideal. Over the infinite residue field choose a linear combination of the two generators which is a nonzerodivisor \(f\) on \(B\). Complete it to an invertible change of the two generators. The quotient \(A=B/fB\) is Artinian, and its canonical module is \(\omega_A=\omega_B/f\omega_B\), up to an irrelevant invertible factor. Matlis duality gives

\[
\operatorname{length}(\omega_A/g\omega_A)
=\operatorname{length}\operatorname{Ann}_A(g)
=\operatorname{length}(A/gA).
\]

The second equality is rank-nullity for multiplication by \(g\) on the finite-length module \(A\). Thus (6) implies

\[
\operatorname{length}\mathcal Q_p
=\operatorname{length}\mathcal O_{C\cap D,p}.          \tag{7}
\]

Since every finite subscheme of smooth \(C\) is an effective Cartier divisor, equal pointwise lengths identify their ideal divisors. Write \(\operatorname{div}\mathcal T_T=\sum_p\operatorname{length}(\mathcal T_T)_p[p]\). Combining (5) and (7) gives

\[
\boxed{\ C\cap D=\operatorname{div}\mathcal T_T+\operatorname{div}\theta\ }
                                                               \tag{8}
\]

as **effective divisors on \(C\)**, or equivalently

\[
I_{C\cap D,C}
=\operatorname{Fitt}_0(\mathcal Q_{Y,C})
=\operatorname{Fitt}_0(\mathcal T_T)\,(\theta).
\]

No equality with sums of contacts of individual branches, a conductor boundary of the total curve, or an exceptional cycle is asserted. Those are different invariants. In particular (8) is not a formula for the complete residual scheme.

### Full thick attachment and the marked normal nilpotent contribution

Let \(H=T\cap D\), a finite scheme, and set \(s=a+b-4\). Classical linkage and Euler characteristic give the full attachment budget

\[
\operatorname{length}H=s\deg T-2p_a(T)+2.             \tag{9}
\]

Indeed \(I_D/L\simeq\omega_T(-s)\), so
\(\chi(\mathcal O_Y)=\chi(\omega_T(-s))+\chi(\mathcal O_D)
=-\chi(\mathcal O_T)-s\deg T+\chi(\mathcal O_D)\).
The scheme union exact sequence gives
\(\chi(\mathcal O_Y)=\chi(\mathcal O_T)+\chi(\mathcal O_D)-\operatorname{length}H\);
equating these proves (9) in every characteristic.

Since \(J\subset I\), there is also an exact sequence

\[
0\longrightarrow I\mathcal O_H\longrightarrow\mathcal O_H
\longrightarrow\mathcal O_{C\cap D}\longrightarrow0.
\]

Define \(\epsilon_{\mathrm{normal}}=\operatorname{length}(I\mathcal O_H)\).
This is the marked normal nilpotent contribution, **not the entire nilradical** of \(H\): the scheme \(C\cap D\) can itself be nonreduced along \(C\). Combining (8)–(9) yields

\[
\boxed{\ \operatorname{length}\mathcal T_T+\deg\operatorname{div}\theta
+\epsilon_{\mathrm{normal}}
=(a+b-4)\deg T-2p_a(T)+2.\ }                          \tag{10}
\]

This is an identity for an actual pair and its full primary/residual schemes, not a universal positive lower bound. If the residual vanishes, all three terms vanish. The filtration by powers of \(I\) on \(\mathcal O_H\) retains further normal attachment layers; it terminates since a pure length-\(m\) thickening \(T\) satisfies \(I^m\mathcal O_T=0\).

The targeted [complete-intersection discrepancy literature check](2026-10-27-absorption-discrepancy-literature.md) identifies (9) in Theorem B of Benguş-Lasnier–Rangachev's numerical-invariants paper. Its hypotheses do allow nonreduced CM generically-CI curves; the full primary \(T\) belongs to that scope. The paper's full \(T\cap D\) attachment must not be confused with the reduced-marked \(C\cap D\) of (8). The local proof above independently fixes that scope distinction.

## 5. A sharp control: the determinant can be a unit at a real attachment

This is a local explanatory example, not a global homogeneous realization on the fixed quartic. It is used to test exactly the proposed omission of \(\mathcal T_T\), not to launch a case classification.

In \(k[[t,x,y]]\), mark \(C=(x,y)\) and take

\[
L=(x^2,xy+ty^2),\qquad
J=(x^2,xy+ty^2,y^3).
\]

The quotient by \(J\) is free over \(k[[t]]\), with basis \(1,x,y,y^2\), so \(J\) is \(C\)-primary and CM. At \(t\ne0\), \(y^3\) belongs to \(L\), since

\[
t^2y^3=yx^2+(-x+ty)(xy+ty^2).
\]

Thus it is the full marked primary component. The residual ideal is

\[
K=(x+ty,t^2)=L:J,\qquad L=J\cap K.
\]

A Hilbert--Burch matrix for \(J\) is

\[
\begin{pmatrix}
y&0\\
-x+ty&-y^2\\
-t^2&x+ty
\end{pmatrix}.
\]

Reducing its relations modulo \(I=(x,y)\) gives

\[
\mathcal E_T\simeq k[[t]]^2\oplus k[[t]]/(t^2).
\]

The actual equations \(x^2,xy+ty^2\) map to the two free basis vectors. Hence \(\bar\rho\) is the identity and \(\theta\) is a unit, but

\[
\mathcal Q_{Y,C}\simeq k[[t]]/(t^2),\qquad C\cap D=2[0].
\]

All attachment length sits in the non-lci torsion term. This disproves a determinant-only residual detector for general full primary components.

The full thick attachment is larger: substituting \(x=-ty\) in \(J+K\) gives
\(\mathcal O_H\simeq k[[t,y]]/(t^2,y^3)\), of length six.
The marked normal ideal \(I\mathcal O_H=(y)\) has length four, while
\(\mathcal O_{C\cap D}=k[[t]]/(t^2)\) has length two.
Thus \(\epsilon_{\mathrm{normal}}=4\), illustrating the two distinct attachment quantities in (10).

## 6. Interpretation, family limitation and literature

For a fixed fiber this gives an exact degree-independent bridge between actual equation generation and residual attachment, including a correction beyond the curvilinear/vector-bundle-only picture. It supplies a target that any proposed absorption deformation must account for, rather than identifying arbitrary filtered defects with a residual curve.

It does **not** yet give an absorption deformation. Extracting the full \(C\)-primary component need not commute with specialization; its degree changes when generic multiplicity rises. Consequently neither \(\mathcal E_T\), its torsion length nor (8) may be treated as a flat family without a separate base-change argument. Fixed lower thickenings used as witnesses are different objects. The parallel [formal lifting investigation](2026-10-27-absorption-formal-lifting-interface.md) addresses compatible motion of such witnesses and actual equations.

Primary literature checked: [Hartshorne's linkage exposition, §1](https://arxiv.org/html/math/0106250v1), [Stacks, Fitting ideals](https://stacks.math.columbia.edu/tag/07Z6), and [Chardin–Naéliton–Tran, Cohen–Macaulayness and canonical module of residual intersections, 2019](https://csdlkhoahoc.hueuni.edu.vn/data/2019/7/cohen%E2%80%93macaulayness_and_canonical_module_of_residual_intersections.pdf). Their standard linkage/canonical-module results explain (6); the present direct-link setting does not need an unrestricted higher-residual-intersection theorem. Local canonical-module reduction and Artinian duality are stated explicitly in the proof. A targeted repo search did not locate the combined full-primary attachment identity (8), but no claim of literature novelty follows.

Independent reconstruction, the local negative control and exact scope are recorded in the [attachment-module audit](2026-10-27-absorption-attachment-module-audit.md). No new canonical result is asserted.
