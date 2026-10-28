# Order-one structure

Canonical status: **PROVED under the stated characteristic-zero rational-quartic/BF hypotheses**

Let \(C\subset\mathbf P^3\) be a smooth nondegenerate rational quartic and suppose an STCI pair has at least one equation of generic normal order one along \(C\). The generic transverse algebra is curvilinear and the saturated multiple structure is quasiprimitive. Write
\[
E_i=L^i(D_i),\qquad L=O_{\mathbf P^1}(e-7).
\]

Gorenstein duality and effectivity give the uniform first-direction bound
\[
0\le e\le6
\]
for arbitrary carrier degrees \(a,b\ge4\), together with uniform early-defect bounds on \(D_2,D_3\). For a quartic order-one carrier the stronger audited restrictions give \(0\le e\le2\).

If \(F_a\) is the equation with nonzero generic first-normal symbol, the numerical normal-sheaf argument also gives
\[
16/a\le7-e.
\]

These statements do not apply to the entirely-thick branch.

## Provenance

Primary proof record:
- \`../notes/2026-10-06-uniform-order-one-frontier.md\`
- \`../notes/2026-10-05-mf6-pairing-audit.md\`
- \`../notes/2026-10-05-mumford-normal-bound.md\`
- \`../notes/2026-10-06-primitive-quadruple-audit.md\`

Current frontier: \`../open/jet_condition_framework.md\` and \`../open/mf6.md\`.

## Historical jet-discrepancy comparison (scope-limited)

The October 6 framework distinguishes a filtration defect divisor from a failure of maximal rank. For a primitive filtration with conormal line L, write V_j(a)=H^0(I_{C_j}(a)), W_j(a)=H^0(L^j(a)), and rho_j:V_j(a)->W_j(a). Define eta_j=dim(W_j)-rank(rho_j) and delta_j=min(dim(V_j),dim(W_j))-rank(rho_j). Then dim(V_{j+1})=dim(V_j)-dim(W_j)+eta_j. For quasiprimitive structures the target is H^0(L^j(D_j)(a)); the divisor D_j and the rank defect delta_j are different invariants.

For the fixed rational quartic on its unique quadric Q, the conormal sequence is 0->O_C(-8)->N_C^*->O_C(-6)->0. Given an order-one quotient N_C^*->L=O_C(e-7), its kernel is M=O_C(-e-7). When the comparison map O_C(-8)->L is nonzero, it defines r in H^0(O_C(e+1)) and a divisor R=Z(r) of degree e+1; the induced M->O_C(-6) is multiplication by r up to scalar.

The first quartic-source space K_R=H^0(Q,I_{R/Q}(1,3)) has dimension 7-e+epsilon_Q(R), where epsilon_Q(R) is the evaluation shortfall of R on O_Q(1,3). For e=0,1, every R of the required length imposes independent conditions, giving dimensions 7 and 6. For e=2, a length-three ruling-fiber divisor has epsilon_Q(R)=1 and dimension 6. When a primitive triple exists, the second quartic condition modulo Q^2 is encoded by a finite evaluation map K_R -> H^0(O_{2R}(2e+2)). The source note supplies further exact e=2 rank certificates; this consolidation does not independently rerun them.

The comparison-zero e=1 direction is excluded from the divisor-R formulation and is analyzed separately in the later e=1 rebuild. That rebuild also corrects an invalid inference that any mate meeting a fixed ruling line creates support outside C; the repaired argument uses intersection multiplicity on a smooth carrier. None of these calculations settles unrestricted characteristic-zero STCI.

Sources: [October 6 jet-discrepancy framework](../notes/2026-10-06-order-one-jet-discrepancy-framework.md) and [October 7 e=1 rebuild](../notes/2026-10-07-e1-jet-rebuild.md). Preserve the original proofs and certificates pending claim-level audit.
