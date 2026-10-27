# Independent audit: curve-centered proof routes for multiplicity four

Date: 2026-10-26. Reviewer: independent `intrinsic_intersection_route` agent. Reviewed document: [proof routes and negative controls](2026-10-26-44-intrinsic-proof-routes.md). **Outcome: the stated direct-resolution reformulation and negative controls pass independent reconstruction at their stated scopes. No canonical promotion.**

## Scope and retained premises

The curve is the fixed embedding \(C=[s^4:s^3t:st^3:t^4]\) over an algebraically closed field of characteristic zero. The pair consists of proper quartics. The reviewer read the research index, the reviewed note, and the preserved [October 23 proof](2026-10-23-intrinsic-44-k3-proof-proposal.md). Its previously audited rank-four multiplication and duality deductions were retained as premises, rather than rerunning accepted proofs or certificates.

The reformulation starts from the actual local equations forced by those deductions. It uses neither R0001 nor R0022. Its final obstruction still uses global surface cohomology. The source explicitly distinguishes this from a proof depending only on the embedded neighborhoods of C.

## Direct resolution without a singularity classification

For the hypersurface \(uv-t^r=0\), with r=2,4,6, the ambient point blowup has u-chart equation \(v_1-u^{r-2}t_1^r=0\), hence that chart is smooth; the v-chart is analogous. Its t-chart is \(u_1v_1-t^{r-2}=0\). At r=2 this is smooth, and the projective exceptional curve is the smooth conic \(uv-t^2=0\). For r>2 the tangent cone is the union of the two planes u=0 and v=0, so its projectivization consists of two lines. Their intersection is the unique remaining singular point, with exponent r-2.

On the next blowup, the strict transforms of the old lines attach to opposite ends of the new exceptional configuration: their two axis directions are distinct points in the corresponding u/v charts. Induction therefore gives a chain, not merely a collection with the right component count. Its number of components is \(N(2)=1\) and \(N(r)=2+N(r-2)=r-1\). All are smooth rational curves; subsequent point blowups preserve the strict transforms of these smooth curves.

At every singular blowup center the surface multiplicity is two. The ambient threefold point blowup has canonical discrepancy 2E, exactly canceled by subtracting 2E from the total surface transform. Hypersurface adjunction therefore proves that each strict surface transform has the pulled-back dualizing sheaf. This applies to the intermediate Gorenstein surfaces as well as the final smooth surface. No rationality theorem for the singularities, or identification by an ADE label, is needed for crepancy. Formal local coordinate changes cause no algebraization gap: completion commutes with the point blowup, and the chart smoothness and multiplicities can be checked after faithful-flat completion.

The general quartic has finite singular locus by the retained local models and Bertini away from C. A reducible projective hypersurface would be singular along the curve where two surface components meet; a repeated component also produces a positive-dimensional singular locus. Thus the general carrier is integral. Its isolated singularities and hypersurface Cohen--Macaulayness imply normality. The explicit sequence of projective ambient blowups gives a smooth connected projective resolution with trivial canonical line bundle.

Adjunction on this final surface gives self-intersection -2 for every exceptional rational curve. The chain matrix with diagonal -2 and adjacent entries 1 is negative definite and has determinant of absolute value r. Its r-1 classes are independent, and chains above different points are disjoint. These assertions follow from the displayed resolution and elementary matrix induction, rather than a classification theorem.

## The Hodge/Noether bound

After the stated characteristic-zero descent and complex base change, set \(q=h^1(\mathcal O)\). Triviality of the canonical line bundle on a connected smooth projective surface gives \(p_g=1\), hence \(\chi(\mathcal O)=2-q\). Noether's formula gives \(c_2=12(2-q)\). Hodge decomposition and Poincare duality give \(b_1=b_3=2q\), whence
\[
b_2=c_2-2+4q=22-8q,
\qquad h^{1,1}=b_2-2p_g=20-8q\le20.
\]
No vanishing of q is assumed or needed. The positive-square pullback hyperplane class is orthogonal to the independent exceptional classes, so their rank is at most nineteen. The retained marked-neighborhood count is \(24-\#\operatorname{Supp}D\ge21\), giving the contradiction. This is a complete replacement of singularity/K3 classification by direct resolution and general surface identities; it remains a global surface-rank argument.

## Quadric negative control and full adjunction

For \(Y=4C\) on the smooth quadric, the divisor has type (4,12), degree sixteen, and arithmetic genus \(1+(4,12)\cdot(2,10)/2=33\). Since \(C^2_Q=6\), its four nilpotent layers have the stated degrees 0,-6,-12,-18. Quartics through Y restrict to sections of \(\mathcal O_Q(0,-8)\), hence vanish on Q; the quartic source is exactly q times all quadratics. This actual quadruple therefore disproves any exclusion based only on degree, genus, and graded-layer degrees, while supplying no proper quartic pair.

Adjunction gives \(\omega_Y=\mathcal O_Q(2,10)|_Y\), so the discrepancy from \(\mathcal O_Y(4)\) is \(M|_Y\), where \(M=\mathcal O_Q(-2,6)\). Its degree on C is zero. To check its infinitesimal nontriviality, the sequence for 2C has left term \(M(-2C)=\mathcal O_Q(-4,0)\). Both initial H0 groups vanish, and the resulting H1 map has three-dimensional source and seven-dimensional target. Multiplication by \((ad^3-bc^3)^2\) maps a Cech basis, up to order and nonzero rescaling, to \(d^6,-2c^3d^3,c^6\). These are independent in characteristic zero, so \(H^0(M|_{2C})=0\). In particular the discrepancy is nontrivial even on 2C. The note correctly refrains from asserting that an arbitrary hypothetical quadruple lies on Q.

## Identical quadric restrictions with different multiplicity

Writing \(a=r+3/2,b=r+1/2,c=1/6-r,d=r-7/6\), one has a-b=1 and c+d=-1. Direct expansion proves
\[
R_0=bF+ax_0^2q,\qquad R_1=cG-dx_3^2q.
\]
The coefficients b,c are nonzero for the stated quadratic equation on r. Thus the restricted pairs generate exactly the same ideal and pencil on Q up to nonzero basis scalars. The inherited prescribed pair has multiplicity one, while the independently established explicit residual example has multiplicity three. This is a legitimate negative control for any argument using only those restrictions. No inherited decomposition proof was rerun.

## Neighborhood target and normal-bundle condition

The determinant target and its degree-four/degree-six alternatives are retained at the exact scope of the [intrinsic cubic-contact construction](2026-10-23-intrinsic-cubic-contact-construction.md). The source correctly calls classification-free nonvanishing for actual quartic sources an unresolved sufficient statement. The abstract rank-one source examples demonstrate why the line-bundle degrees alone do not prove it.

For the primitive e=1 branch, the blowup normal degrees reconstruct as follows. The first selected normal line has degree six inside \(N_C=\mathcal O(7)^2\). The successive normal sequences have degrees (2,6), (-4,6), and finally (-10,6). The transformed quartic line bundle has successive degrees 10,4,-2 on the successive center curves. After three blowups, actual generation of the reduced remaining center ideal by two such sections would give its conormal bundle \(\mathcal O(2)^2\), equivalently normal bundle \(\mathcal O(-2)^2\).

The final sequence \(0\to\mathcal O(-10)\to N\to\mathcal O(6)\to0\) does permit this middle bundle: two degree-eight forms with no common zero embed \(\mathcal O(-10)\) in \(\mathcal O(-2)^2\), with quotient \(\mathcal O(6)\). It cannot be split or ruled out numerically. The source properly states a necessary condition and an unproved sufficient obstruction, not an equivalence to global realization. The defective branch is explicitly left separate.

## Review decision

No substantive mathematical correction was required. The direct blowup calculation removes the surface-singularity classification while retaining the global Hodge/Noether obstruction. The negative controls establish genuine limits of simpler numerical and quadric-only approaches. A proof confined to the marked infinitesimal neighborhood is not claimed. Existing accepted evidence retains its status; no canonical result or question is created, promoted, or reopened.
