# Intrinsic embedded ribbon-to-triple obstruction (2026-10-21)

Status: **provisional mathematical construction; independent audit pending**. Dedicated branch only. No canonical promotion.

## Precise theorem (fixed embedded ribbon)

Let \(i:C\hookrightarrow X\) be a regular immersion of codimension two, with \(X\) smooth over a base DVR \(R\), and \(C\) smooth over \(R\). Let \(I\) be its ideal and let \(q:E=I/I^2\twoheadrightarrow L\) be a line-bundle quotient with kernel \(M\). Write \(J_2\) for the inverse image of \(M\) in \(I\); this fixes the embedded ribbon \(C_2=V(J_2)\).

Consider embedded ideals \(J_3\subset\mathcal O_X\) with \(I^3\subset J_3\subset J_2\), such that locally, in regular parameters \((x,y)\) for \(I\) with \(q(x)=0\), \(q(y)\) generating \(L\), the ideal is
\[
J_3=(x-a y^2,I^3)
\]
for a local coefficient \(a\) (and, equivalently, \(J_3\) is a primitive embedded triple with first quotient \(q\)). The reduction of \(J_3\) modulo \(I^2\) is \(J_2\). Here all statements are on sufficiently small open neighborhoods of \(C\); ambient opens away from \(C\) play no role.

**Theorem.** The sheaf of local embedded primitive triples extending this *fixed* embedded ribbon is an \(\mathcal H=\mathcal Hom_{\mathcal O_C}(M,L^{\otimes2})\)-torsor (sheaf of sets, not a claimed groupoid of abstract triples). Consequently it has a canonical obstruction
\[
o_X(q)\in H^1(C,\mathcal H).
\]
It vanishes if and only if an embedded primitive triple extending the fixed ribbon exists. When it vanishes, global extensions form a torsor under \(H^0(C,\mathcal H)\).

The theorem concerns *embedded ideal subschemes*, not presentations of abstract multiple curves or their automorphism groups. An embedded subscheme has no nontrivial automorphism over \(X\). Changes of local generators and ambient coordinates act on presentations, not on these objects.

## Proof: local existence and intrinsic difference

Because \(q\) is a surjection of locally free modules and \(C\hookrightarrow X\) is regular, étale/affine locally choose regular generators \(x,y\) of \(I\) with \(q(x)=0\) and \(q(y)\) a generator of \(L\). Then \((x,I^3)\) is a local triple: its structure algebra has filtration with graded pieces \(\mathcal O_C,L,L^2\), and multiplication \(L\otimes L\simeq L^2\). Its defining equation is allowed to be modified by \(a y^2\).

For any two such triples \(J,J'\), their defining ideals modulo \(I^3\) have the same image \(M\subset I/I^2\). The unique difference is the induced map \(M\to I^2/(I^3+I J)\simeq L^2\), equivalently the coefficient difference \(a'-a\) in the chosen frame. Independence from a lift of a generator of \(M\) follows because replacing it by a unit or by an element of \(I J\) changes both equations compatibly; \(I J\) maps to zero in \(L^2\). Conversely, every homomorphism \(M\to L^2\) modifies the defining equation and produces another local primitive triple. Composition of modifications is addition, giving a free transitive \(\mathcal H\)-action.

A more explicit intrinsic description avoids identifying \(I/I^3\) with an \(\mathcal O_C\)-module: for a fixed triple \(J\), its image \(\bar J\subset I/I^3\) maps onto \(M\), and the multiplication image \(I\bar J\subset\bar J\) is the canonical rank-two quadratic submodule \(M E\subset\operatorname{Sym}^2 E\). The quotient \((I^2/I^3)/(M E)\) is canonically \(L^2\). Differences of two lifts of \(M\) to \(I/I^3\), modulo \(M E\), therefore lie in \(\operatorname{Hom}(M,L^2)\). This quotient formulation, rather than a fictitious \(\mathcal O_C\)-linear splitting of \(I/I^3\), is the invariant construction.

## Čech construction and descent

Choose an affine cover \(\{U_i\}\) trivializing \(E,M,L\), and local triples \(J_i\). On \(U_{ij}\) define \(h_{ij}=J_j-J_i\) by the intrinsic difference above. Additivity of differences gives \(h_{ij}+h_{jk}=h_{ik}\); hence \(h\) is a Čech 1-cocycle. Replacing \(J_i\) by \(J_i+a_i\) changes \(h_{ij}\) by \(a_j-a_i\). Thus \([h]\) is independent of choices. If \([h]=0\), adjust local triples to agree on overlaps; their ideal sheaves glue to a global embedded triple. Conversely a global triple gives zero cocycle. This proves the theorem.

This construction is functorial under isomorphisms of pairs \((X,C,q)\) and under base changes for which regular immersion and the prescribed quotient persist. It depends on the *embedded quadratic neighborhood* and not merely on the abstract ribbon.

## Coordinate-invariance mechanism

On an overlap, write normal variables \((X,Y)\) and \((A,B)\), with the ambient coordinate on the base changing as \(c=c_0(u)+c_1(u;X,Y)+O(I^2)\). To compare kernel equations \(m_U,m_V\), substitute the **entire** quadratic transition, including the Taylor/Hasse first derivative of coefficients of \(m_V\) evaluated at \(c\). The result is the intrinsic difference \(h_{UV}\). Individual contributions from the normal-coordinate substitution and the nilpotent base displacement are not invariants.

For the audited distinguished quartic quotient, the recorded decomposition is
\[
K_A=18u^{-2},\quad K_B=-12u^{-2},\quad K_{\rm move}=-12u^{-2},\qquad K=-6u^{-2}.
\]
Under \(A'=A+B, B'=B\), the first two terms become
\[
K_A'=18u^{-2}+9u^{-1},\quad K_B'=-12u^{-2}-9u^{-1}.
\]
The base contribution stays unchanged, so the **total** cocycle remains \(-6u^{-2}\). This is not accidental cancellation: the coordinate change carries the same embedded ideal into a new presentation, while the intrinsic difference of ideals is unchanged.

## Rational quartic specialization

For \(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_R\) and the distinguished quotient \(L=\mathcal O(-6)\), \(M=\mathcal O(-8)\), the difference sheaf is
\[
\mathcal H=M^\vee\otimes L^2=\mathcal O(-4).
\]
With \(u=s/t\) on one chart and \(c=t/s\) on the other, the audited normalization of the kernel comparison gives
\[
H^1(\mathbf P^1_R,\mathcal O(-4))
=R[u,u^{-1}]/(R[u]+u^{-4}R[u^{-1}]).
\]
The classes of \(u^{-1},u^{-2},u^{-3}\) form an \(R\)-basis. The complete audited transition computes \(o_X(q)=[-6u^{-2}]\) for the distinguished quotient. For all admissible quotients reducing to the prescribed characteristic-two ribbon, the audited coefficient of \([u^{-2}]\) is \(2\pmod4\), so none extends.

The *existence and intrinsic meaning* of the class follow from the ideal-sheaf torsor theorem above; the numerical identification uses the previously audited integral coordinate computation rather than an independent re-expansion.

## Relation to cotangent complexes

The filtered-ideal torsor is the direct, sufficient construction. No unproved identification with a cotangent-complex Ext class or a divided-Frobenius operation is asserted. Such an identification would require an explicit morphism from the relevant embedded deformation complex to \(\mathcal H[1]\) and a comparison of the two obstruction classes.

## Exact boundaries and Investigation 3 handoff

- Fix the **entire embedded first-order quotient** \(q\), not merely its isomorphism class or its residue-field reduction. The obstruction is relative to that fixed quotient.
- Work in \(I/I^3\), retaining its filtered algebra structure and the full ambient quadratic transition; do not impose a canonical graded splitting or a retraction \(C_2\to C\).
- On each chart choose an \(I\)-generator \(y\) mapping to a generator of \(L\), a kernel generator \(x\), and local equations \(x-a y^2\). Track the transformation of \(x\) and of the base-coordinate-dependent coefficients, including Hasse derivatives.
- Identify \(M\) and \(L^2\) frames on overlaps, then normalize the difference to the \(\mathcal O(-4)\) transition; for the audited quartic conventions the equation is \(K=\gamma_U(u)+u^{-4}\gamma_V(u^{-1})\).
- Investigation 3 may study arithmetic origins of \([-6u^{-2}]\), but no divided-Frobenius interpretation is established here.
- Independent review should explicitly test the intrinsic-difference quotient \(I^2/(I^3+IJ)\), its independence of choices, and faithfully flat descent before promotion.

Sources: research/notes/2026-10-20-z4-lift-independent-audit.md; research/notes/2026-10-20-z4-characteristic-zero-lifting-report.md; literature branch research/z4-intrinsic-obstruction-literature-2026-10-21; counterexample branch research/z4-divided-frobenius-2026-10-21.
