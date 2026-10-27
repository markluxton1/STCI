# Independent audit: (4,4) degeneration and genus budgets

Date: 2026-10-26. Reviewer: independent `genus_topology` agent. Reviewed document: [degeneration and genus budgets](2026-10-26-44-degeneration-genus-budgets.md). **Outcome: the stated elementary deductions pass independent reconstruction at the scopes below. This is an evidence audit, with no canonical promotion.**

## Scope and inputs

The ambient space is projective three-space over an algebraically closed field of characteristic zero. Ordinary topology refers to the associated complex curve. Defining pairs are proper: their forms have no common surface component. The marked curve is the fixed embedding
\[
C=[s^4:s^3t:st^3:t^4].
\]
The reviewer read the research index, the reviewed note, promoted records [R0021](../results/quartic_mu4_degeneration.md) and [R0022](../results/quartic_44_filtered_exclusion.md), and the relevant [conductor/topology evidence](2026-10-25-ci-cycle-conductor-topology.md). The prescribed four-quartic decomposition and the fixed-curve exclusion were retained at their recorded scope; their inherited proofs and certificates were not rerun. The earlier generic smooth residual and eight-component competitor remain reviewed, unpromoted inputs with the provenance stated in the main note.

## Reconstruction of the scheme and reduced-curve budgets

1. The Koszul resolution gives the displayed polynomial and genus for every proper pair, including nonreduced pairs. Intermediate line-bundle cohomology on projective three-space gives \(H^1(\mathcal I_W)=0\), hence \(H^0(\mathcal O_W)=k\). Thus the claimed connectedness and equality \(h^1(\mathcal O_W)=p_a(W)\) also hold for these nonreduced complete intersections. Purity, Cohen--Macaulayness, Gorensteinness, and the adjunction formula follow from the regular sequence.

2. On the open parameter locus of proper pairs, the universal Koszul family is flat. Smooth complete intersections form a dense open subset. A general coefficient line through a prescribed proper pair has a smooth generic fiber after restricting the base to retain properness. This proves smoothability of every proper pair under discussion. It does not identify a flat curve limit when specialized forms gain a common factor, and it does not require that a smoothing retain the marked curve.

3. For reduced fibers, the finite normalization sequence independently yields
\[
p_a(W)=\sum_i g_i+\delta-r+1.
\]
The bipartite branch-incidence graph has first Betti number \(b=\sum_p(r_p-1)-r+1\). The dimension left after identifying branch origins is \(u=\delta-\sum_p(r_p-1)\), giving the stated decomposition into normalization, toric, and unipotent contributions in characteristic zero. The notation in the reviewed source is \(u\), consistently with its later formulas.

4. The normalization is topologically quotiented by identifying the finitely many branch origins. It follows that \(b_1=2\sum g_i+b\), \(b_2=r\), and the stated Euler characteristic formula holds. Substitution of the normalization genus identity gives \(\chi_{\mathrm{top}}(W)=-64+\sum_p(2\delta_p-r_p+1)\). The identification of the local summand with the Milnor number is valid for the reduced isolated complete-intersection curve germs. The main note correctly avoids applying this reduced formula to a generically nonreduced fiber merely by taking its reduction. The cited [Dimca--Greuel paper](https://www.journalofsing.org/volume18/dimca-greuel.pdf), Theorem 2.1(1), supplies the local formula.

5. In the plane-product grid, a node occurs exactly at the intersection of two lines sharing a row or column. General linear position excludes points lying on four planes and excludes three curve branches meeting. Hence there are sixteen lines and forty-eight ordinary nodes, with graph genus thirty-three. Since every reduced component has positive integral degree, \(r\le16\); therefore \(\delta\le48\), attained by this example. For four general plane sections of a smooth quartic, the twelve normalization-genus units and twenty-four nodes give genus thirty-three as claimed. The general \((a,b)\) grid counts likewise reconstruct directly.

## Componentwise conductor and nonreduced checks

For a reduced Gorenstein curve with normalization \(\nu\), finite duality gives
\[
\omega_{\widetilde W}=\mathfrak c\otimes\nu^*\omega_W,
\]
where the conductor extended to the normalization is \(\mathfrak c=\mathcal O_{\widetilde W}(-B)\). Restricting to an individual normalized component therefore yields the asserted degree \((a+b-4)e-2g+2\). This restriction, rather than a conductor formula for nonreduced fibers, is the correct hypothesis. For a smooth component of a reduced union, the conductor ideal on that component is the ideal of its scheme-theoretic intersection with the complementary reduced curve. The attachment-length formula follows. The union exact sequence then gives the stated residual arithmetic genus, without an assumption of residual irreducibility or smoothness. The note marks those existence questions separately.

The nonreduced examples reconstruct independently. For \(V(L^4,M^4)\), complementary homogeneous coordinates exhibit the rank-sixteen module with shifts \(-i-j\); summing the sixteen linear polynomials gives \(16n-32\). For \(V(L^4,G_4)\) with smooth plane-quartic reduction, the powers of the regular parameter \(L\) have layers \(\mathcal O_D(-j)\), \(0\le j\le3\), and give the same polynomial. Thus the examples really have the stated pure multiple cycles. They establish no analogous existence for the fixed rational-quartic embedding.

## Independent reconstruction of the new smooth-carrier lemma

Suppose a quartic pencil has a member \(F\) smooth everywhere along \(C\). Its first normal symbol \(f\) is a nowhere-zero section of \(N^*_{C/\mathbf P^3}(4)\). If the generic intersection multiplicity is at least two, the second first symbol \(g\) has zero wedge with \(f\). The subbundle generated by \(f\) is \(\mathcal O_C\), so \(g=\lambda f\) with a globally regular function \(\lambda\), necessarily a constant. Thus \(G-\lambda F\) belongs to the actual ideal-sheaf square in degree four. This argument needs neither a pointwise constant ratio assumption nor a splitting of the conormal bundle.

On the smooth quadric \(Q\), the marked curve has type \((1,3)\). Restricting a quartic from \(\mathcal I_C^2\) to \(Q\) gives a section of \(\mathcal O_Q(2,-2)\), which vanishes. Divide by \(q\): the residual quadratic must vanish on \(C\), and restriction to \(Q\) leaves type \((1,-1)\), again with no sections. Hence the residual quadratic is a scalar multiple of \(q\), proving \(H^0(\mathcal I_C^2(4))=kq^2\). Properness makes the new pencil member nonzero.

The divisor of \(F|_Q\) is \(C+C'\) with \(C'\) of type \((3,1)\). Since \((3,1)-(1,3)=(2,-2)\) is not effective, \(C'\) has no \(C\) component. Intersecting with \(q^2\) doubles this divisor, giving \([W]=2[C]+2[C']\), where \([C']\) retains its possible component multiplicities. The multiplicity of \(C\) is exactly two. This confirms the lemma and its contrapositive: multiplicity at least three forces every pencil member to be singular somewhere on \(C\), without forcing a common singular point.

The first-symbol argument for equal degree \(d\) and an arbitrary smooth connected projective marked curve is valid under the same smooth-carrier hypothesis. Its conclusion is membership of a nonzero pencil member in \(H^0(\mathcal I_C^2(d))\); the quartic one-dimensionality cannot be carried into higher degrees without new information.

## Explicit smooth surface, double member, and pencil

For the displayed prescribed \(F,G\), write \(S=F+G=x_1^4+x_2^4-x_0^3x_3-x_0x_3^3\). Its partial derivatives in \(x_1,x_2\) force \(x_1=x_2=0\) at a singular point. The remaining equations would force either all coordinates zero or simultaneously \(x_0^2=-3x_3^2\) and \(3x_0^2=-x_3^2\), impossible in characteristic zero. Thus \(S\) is smooth, and in particular integral.

In Segre coordinates, direct multiplication verifies
\[
S|_Q=(ad^3-bc^3)(a^3d-b^3c).
\]
Each factor defines a graph of a degree-three map of projective lines, hence a smooth rational quartic. Restricting the second factor to the first curve gives \(st(s^8-t^8)\), whose ten distinct zeros prove the stated transverse intersections. Hence the reduced divisor \(D=C\cup C'\) has degree eight and genus nine. On \(S\), it is the Cartier divisor cut by \(q\), so \(\mathcal O_D(-D)=\mathcal O_D(-2)\). The double-divisor exact sequence gives the two polynomials \(8n-24\) and \(8n-8\), with sum \(16n-32\).

The forms \(F,q^2\) are linearly independent modulo \(S\): comparing the coefficients of \(x_1^4\) and \(x_2^4\) in a supposed relation first kills the \(F\) and \(S\) coefficients and then kills the \(q^2\) coefficient. Since \(S\) is integral, every nonzero member cuts a proper Cartier divisor. The resulting family over the full projective pencil is flat and has the two endpoints claimed. This argument does not assert that the remaining residual members of this pencil are smooth.

Finally, adjunction on the smooth quartic gives \(C^2=-2\), and \(C'=2H-C\) gives \(C\cdot C'=10\), agreeing independently with the explicit intersections. The change from eighteen boundary units for a component of a reduced \((4,4)\) curve to ten for a component of the reduced \((2,4)\) support is correctly distinguished.

## Review decision and limitations

No substantive mathematical correction was required. Componentwise normalization notation was suggested for clarity in section 5. All new elementary claims reconstructed above are independently reviewed evidence. The inherited reviewed inputs retain their pre-existing status. This audit proves neither a classification of possible embedded limits nor realization of arbitrary numerical data, and it supplies no unrestricted STCI conclusion. No canonical result or question is created or promoted.
