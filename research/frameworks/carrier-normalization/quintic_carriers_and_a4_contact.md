# Quintic carrier support and A4 conductor contact

[Carrier Framework](index.md) · [Original section addresses](normalization_conductor_projection.md)

## Quintic geometry before the final support incidence

The [quintic structural proof](../../arguments/carriers/quintic_conormal_and_factor_geometry.md#quintic-carriers-conormal-factorization-residual-divisors-and-low-pole-spaces) first isolates its hypotheses: in the specified nonnormal Gorenstein genus-one lane, the normal degree-five anticanonical model has one A4 singularity, a smooth lifted quartic c and a unique line ell with `H=c+ell=5ell` and `5c=4H`. This is not a classification of all quintic carriers. The [intrinsic pair proof](../../arguments/carriers/del_pezzo_five_a4.md#degree-five-del-pezzo-a4-model-intrinsic-classification-and-explicit-equations) contracts the marked A4 chain to the full plane cluster `(y−x³,x⁴)`, classifies every admissible smooth conic through it, and computes the residual automorphism group as translations. Its proof explains why the extra nonendpoint projection parameter cannot be discarded by scaling.

| Actual projection stratum | Retained mechanism and precise remaining boundary |
| --- | --- |
| Endpoint a=0 | [Support and excess proof](../../arguments/carriers/quintic_endpoint_residual_support_and_excess.md) plus [the actual fourth-blowup unit jet](../../arguments/carriers/quintic_endpoint_jets_and_power_descent.md) exclude every positive mate power in this stratum. The unit jet is an actual-ring obstruction, not only equalizer matching. |
| Endpoint a≠0 | The residual anticanonical divisor gives target contact11, intrinsic contact4 and excess7. The completed [global inverse-support proof](../../arguments/carriers/quintic_endpoint_residual_support_and_excess.md#2-endpoint-a-nonzero-global-independent-audit) then excludes every such endpoint projection: its actual target septic must be supported at common roots of U,V; each has order≤4, order4 allows no second root, and the three-root family is separately excluded. A degree7 septic cannot have the resulting support. |
| Nonendpoint reducible residual | The [exhaustive pole filtration](../../arguments/carriers/nonendpoint_residual_factorization_and_genus.md) preserves cancellation and repeated-prime strata. The specified partitions 2+2+2, 2+4 and 3+3 are excluded through [actual higher contacts](../../arguments/carriers/nonendpoint_cubic_contact.md#nonendpoint-conic-plus-quartic-residuals-all-eight-families) and [complete cubic-pair scope](../../arguments/carriers/nonendpoint_cubic_pairs.md#nonendpoint-residual-cubic-pairs-complete-contact-and-coefficient-proof), not a generic-root count. |
| Nonendpoint integral residual | The actual source has arithmetic genus one, including singular affine cubics, and is smooth at its A4 point. Full inverse support excludes a degree-two map, so its image is birational of class (4,2), arithmetic genus three. Its intrinsic c-ideal has length6, including length2 at A4; target contact14 forces excess8. The curve-model quotient length2 cancels in the local contact comparison and gives no upper bound on that excess. This incidence remains open. |
| Nonendpoint target fibers | The [actual fiber equations](../../arguments/carriers/quintic_nonendpoint_support.md#4-nonendpoint-target-fiber-reduction-and-bounded-exclusions) keep finite denominator/rank boundaries, A4 target, infinity and primitive cube-root compatibility. Their equal-lift exclusion does not exhaust every projection. The [single-root incidence](../../arguments/carriers/quintic_toric_center_incidence.md#nonendpoint-single-root-incidence-and-actual-quotient-fibers) preserves separate quotient fibers and singular denominator charts. |

The recurring mechanism is **scheme-theoretic pullback of the marked curve ideal**, followed by exact lengths in actual integral curve rings. Finite birational curve-model defect, conductor contact, differential degeneracy and excess contact are different quantities. Smooth source or image branches can have high mutual contact. The seven- and eight-length budgets by themselves are necessary constraints. The endpoint case has a completed additional actual-fiber and higher-jet exclusion; the integral nonendpoint eight-excess incidence remains open. The entire intrinsic endpoint family is therefore excluded in every mate degree, while the separate nonendpoint modulus is retained. These are the characteristic-zero source results; their A4/del Pezzo classification and coefficient separability have not been asserted in arbitrary characteristic.


## Quintic support: closed h=3 and the remaining h=2 problem

These statements concern **admissible nonendpoint genus-one quintic \(A_4\) projections in characteristic zero**, not all quintic carriers. Let \(H_j\) be the homogeneous gcd of the corrected first conormal cubics, and let \(F_{\rm cond}\) be the **actual homogeneous conductor octic**.

**Complete \(h=3\) lane.** Under the accepted homogeneous gcd-three classification, every admissible projection with \(\deg H_3=3\) is excluded for **all positive mate degrees**. Zero-cubic and proportional boundary charts are included. In the remaining proportional family \(F_{\rm cond}=\mathrm{const}\cdot H_3S_5\). Full inverse support restricts the roots of \(S_5\) to those of \(H_3\). The homogeneous leading-drop analysis excludes infinity support, and the complete alternatives are: three distinct roots, or multiplicity patterns \(5\), \(4+1\), \(3+2\). The last pattern uses the **original six-generator** polynomial row \(M_6\) and an exact identity \(M_6W=(Vc_5)^2\), where the admissible parameter product \(Vc_5\) is nonzero; thus the six equations cannot vanish simultaneously. This closes the entire \(h=3\) lane, not merely a generic chart. [Accepted scoped result](../../arguments/carriers/quintic_h3_support_exclusion.md).

**Differential content of \(h=2\).** For every finite birational ring extension \(A\subset B\) with conductor \(I\), the identity \(I\Omega_{B/A}=0\) follows from \(c\,db=d(cb)-b\,dc\) for \(c\in I\). Along the smooth lifted curve, the relative differentials have the local form \(\Omega_{S/X}\otimes\mathcal O_c\cong\mathcal O_c/(u_1,v_1)\,dT\), where \(u_1,v_1\) are the corrected conormal symbols. Hence their complete homogeneous gcd \(H_2\) divides \(F_{\rm cond}\), including multiplicities and the permitted simple \(A_4\) infinity factor. Write \(F_{\rm cond}=H_2Q_6\), with \(Q_6\) homogeneous sextic. This is **divisibility**, not equality of conductor and first-symbol divisors.

When no extra \(A_4\) support is allowed, the remaining support condition becomes the eigenvector equation
\[
D_{H_2}Q_6=\mu Q_6,\qquad D_K=\(\partial_tK\)\partial_s-\(\partial_sK\)\partial_t.
\]
For quadratic \(H_2=as^2+bst+ct^2\), with \(\Delta=b^2-4ac\), the degree-six action has characteristic polynomial
\[
\mu\(\mu^2-4\Delta\)\(\mu^2-16\Delta\)\(\mu^2-36\Delta\),
\]
valid also on the repeated-root boundary. With the allowed \(A_4\) point \(s=0\), retain the homogeneous system \(D_{sH_2}Q_6=L_1Q_6,\ jD_{H_2}Q_6=\mu Q_6\), \(j=\bar J\), rather than discarding \(j=0\). For \(j\ne0\) the support condition is equivalently the covariant identity \(J(\operatorname{Hess}\(F_{\rm cond}\),Q_6)=0\). These are necessary incidence reductions, **not an \(h=2\) exclusion or conductor-power descent**. The original source flags its later quadratic-algebra norm computation as pending independent review. [Differential proof and incidence](../../arguments/carriers/quintic_a4_contact_and_norm.md#2026-10-14-generalization-quintic-h2-conductor-quotient).



## Actual h=2 incidence and its linear-system meaning

On the remaining admissible nonendpoint genus-one quintic \(A_4\), \(h=2\) parameter open in characteristic zero, write \(H=t^2+vst+ws^2\), \(Q=\sum_{i=0}^6q_is^{6-i}t^i\), \(j=\bar J\), and \(R=D_HQ\). The localized candidate ring satisfies the **unit ideal** \((q_5,q_6)=A\), not separate invertibility of either coefficient. The 77 quadratic/cubic rank minors have the same saturation by this ideal as twelve fixed generators (eleven cubic minors and \(jM_{56}\)); the comparison holds scheme-theoretically without division by \(j\).

The rank condition admits locally unique, globally gluing ODE witnesses \(d,u\), yielding the necessary identities \((d-5)(d-6)=0\) and the remaining \(j\)-dependent constraints **as ideal memberships**, not merely on closed points. The actual conductor norm is an additional necessary equation; rank incidence alone does not produce an STCI pair or close the full \(h=2\) locus. The [complete pivot-cover saturation, ODE gluing, spectral cases, and norm analysis](../../arguments/carriers/quintic_h2_rank_incidence_and_ode.md) retain the explicit equations and their exact localization hypotheses.

## Intrinsic A4 contact and the necessary homogeneous norm

In the admissible nonendpoint genus-one quintic \(A_4\) model, write \(j=\bar J\), \(\delta\ne0\), and \(F\) for the **actual primitive conductor octic** in the target coordinate \(p=\delta/r\). On \(j=0\), the exact coefficient identities are
\[
F(0)=0,\quad [p]F=-2G\(\delta^2+2B+G\)\(3\delta^2+G\)^2,
\]
and, when \(G=-3\delta^2\),
\[
[p^2]F=-108\delta^5\(\delta^2-B\).
\]
The accepted \(G=j=0\) mate exclusion and full target-fiber criterion show that any remaining \(j=0\) mate candidate has \(G\ne0\) and \(\delta^2+2B+G\ne0\). Thus its intrinsic \(A_4\) conductor contact is **exactly one or two**, not arbitrarily large. The contact-two case occurs on \(G=-3\delta^2\) with \(B\ne\delta^2\).

For the homogeneous \(h=2\) factorization \(F_{\rm src}=H_2Q_6\), the first-symbol factor \(H_2\) cannot contain the \(A_4\) point on a surviving candidate. If \(\operatorname{Res}(H_2,Q_6)\ne0\) when \(j=0\), all sextic roots would have to lie at the \(A_4\) point, forcing conductor contact six and contradicting the bound. Therefore **every remaining \(h=2\) mate candidate**, for either value of \(j\), satisfies \(\operatorname{Res}(H_2,Q_6)=0\). This is a necessary homogeneous norm equation, not an emptiness proof; the repeated-root and infinity charts remain included. [Intrinsic coefficient and support proof](../../arguments/carriers/quintic_a4_contact_and_norm.md#2026-10-14-generalization-quintic-intrinsic-a4-contact-bound).



## Full conductor contact, its differential, and its weighted budget

For a finite normalization \(\nu:S\to X=\(F=0\)\subset\mathbf P^3\) with \(X\) integral, a smooth curve \(C\) whose **full reduced inverse image** is one smooth Cartier \(c\cong C\), \(S\) regular along \(c\), and \(X\) regular at the generic point of \(C\), finite duality identifies the actual upstairs conductor as \(\mathcal O_S(-B)=\omega_S\otimes\nu^*\omega_X^{-1}\) near \(c\). Let \(A\) be the full common-zero divisor of the normal differential of \(\nu\) along \(c\), and \(D_F\) the common-zero divisor of the **actual first normal symbol** of \(F\). The residue/Jacobian identity yields the equality of effective divisors, with multiplicities,
\[
D_F=B|_c+A.
\]
In particular \(A\) is **not** itself the conductor contact divisor; equality \(D_F=B|_c\) requires transverse immersion all along \(c\).

If \(X\) has degree \(a\), \(C\) degree \(d\) and genus \(g\), and \(k=c^2\), adjunction gives the weighted conductor budget
\[
N=B\cdot c=d(a-4)+k-(2g-2).
\]
Writing \(B=\sum m_iD_i\), ampleness of \(c\) gives \(\sum m_i\(D_i\cdot c\)=N\), bounding prime conductor components, multiplicities and total branch contact. For each downstairs conductor curve, let \(d_\Delta\le a\) be the total generic reduced normalization degree. The **ordered off-diagonal pair correspondence**, including conjugate pairs on one prime, has total weighted first-projection contact bounded by \((a-1)N\). The three fixed-\(C_0\) singleton models give \((a,N,(a-1)N)=(8,20,140)\) for both quadric normalizations and \((16,51,765)\) for the plane normalization. These are finite integer-contact budgets, **not** bounds on scalar phase orders or nilpotent logarithmic defects. The global conductor need not be Cartier, only Cartier near \(c\); singular or non-Cartier lifts and generically nonregular carriers are outside the stated bridge. An independent review **passed under the stated Gorenstein, smooth Cartier-lift, full-support and generic-regularity hypotheses**; applications to a globally non-Gorenstein normalization require retaining the original local-versus-global distinction. [Independent review](../../arguments/carriers/projection_conductor_contact_and_phase.md#actual-projection-spaces-and-conductor-phases). [Jacobian identity](../../arguments/carriers/conductor_jacobian_local_residue_proof.md), [contact and pair budgets](../../arguments/carriers/projection_conductor_contact_and_phase.md#actual-projection-spaces-and-conductor-phases).


