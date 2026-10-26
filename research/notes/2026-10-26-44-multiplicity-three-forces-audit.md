# Independent audit: what multiplicity at least three forces in (4,4)

Date: 2026-10-26. Reviewer: independent `triple_classification` agent. Reviewed document: [multiplicity-three deductions](2026-10-26-44-multiplicity-three-forces.md). **Outcome: the stated deductions pass independent reconstruction at their stated scopes. No canonical promotion.**

## Scope and accepted premises

The field is algebraically closed of characteristic zero, the curve is the fixed embedding \(C=[s^4:s^3t:st^3:t^4]\), and the quartic pair is proper. The audit read the research index and the literal promoted statements of [R0001](../results/quartic_carrier_exclusion.md), [R0020](../results/quartic_conormal_characteristic_jump.md), and [R0022](../results/quartic_44_filtered_exclusion.md). Their accepted proofs and certificates are premises, not verification tasks. The earlier [smooth-carrier deduction](2026-10-26-44-degeneration-genus-budgets.md) and the accepted source-level conjugate pencil in the [filtered proof](2026-10-23-quartic-44-filtered-proof-proposal.md) were consulted at their recorded scope.

The reviewer independently derived the conjugate example's factorization and branch geometry before reading the new verifier. The [new script](../computations/verify_44_triple_residual_example_2026_10_26.py) was inspected as finite polynomial evidence. Its successful execution is recorded separately in the linked validation directory; the audit does not equate execution with a global proof.

## 1. Maximum multiplicity and integrality of every pencil member

Degree gives \(m_C\le4\). Equality exhausts degree sixteen, and complete-intersection purity then gives sole reduced support C, contradicting R0022. Thus \(m_C=3\) and the actual residual cycle has degree four. This reasoning does not imply residual integrality or rationality.

The all-members-integral argument uses R0001 essentially and is correct. If a quartic member has a quadratic factor carrying C, that factor is q. The mate is not divisible by q by properness, and its restriction to Q has class (4,4). The class (2,-2) rules out a second C component, so the local intersection with q has multiplicity one. A second quadratic carrying factor is necessarily q again; it doubles the multiplicity to two. Other quadratic factors are units at the generic point of C. Therefore this case cannot give multiplicity three.

Any remaining reducible quartic carrying C has the form \(A\ell\), with A an integral cubic and the plane factor a unit generically on C. If the mate is integral quartic, \(V(A,G)\) is proper of degree twelve and already contains 3C; purity gives sole support C, contrary to the precise integral-quartic/all-mate-degree statement of R0001. If the mate is reducible, the same quadratic exclusion leaves an integral cubic carrying factor B. Properness rules out A=B, and degree nine cannot accommodate 3C. This accounts for repeated factors as well as reduced factorizations.

## 2. First-symbol divisor and moving singularities

Generic transverse length three forces a nonzero linear normal relation: two equations of normal order at least two would have local intersection length at least four. The generic algebra is therefore curvilinear, \(K[\epsilon]/(\epsilon^3)\). Saturating the common first-symbol line in \(E=\mathcal O(-7)^2\) gives a subbundle \(M=\mathcal O(-7-e)\), with e nonnegative and locally free quotient \(\mathcal O(e-7)\).

The two actual first symbols are \(h_0m,h_1m\), with \(h_i\in H^0(\mathcal O(9-e))\). A constant dependence would produce a nonzero pencil member in \(H^0(\mathcal I_C^2(4))=kq^2\), already impossible at multiplicity three. Hence e lies between zero and eight. Removing the common divisor B gives a basepoint-free nonconstant pencil of degree \(n=9-e-\deg B\ge1\).

The saturated direction has no zero in any fiber of E. Since each carrier vanishes on C, its ambient differential restricted to C is its first normal symbol. Consequently its singular subscheme restricted to C is exactly the zero divisor of the corresponding scalar section. General fibers of the resulting map to the pencil line are simple in characteristic zero. They avoid any prescribed finite subset of C. The resulting fixed-plus-moving divisor statement is valid; neither a common singular point nor absence of other singularities is inferred.

## 3. The moving singularities are A2

Remove the finite loci of residual attachment and nonprimitive triple behavior. On the remaining open set the actual ideal is locally \((x,y^3)\), with curve parameter t. This follows by spreading the generic curvilinear normal form; it asserts no global primitive structure.

For a generating pencil pair, the coefficient matrix relative to x and y³ is invertible. At a simple moving first-symbol zero of a member H, its x coefficient vanishes simply in t, whereas another generator has unit x coefficient. The determinant condition forces H's y³ coefficient to be a unit. Writing \(H=xA+y^3B\), one has \(A_t(0)\ne0\) and \(B(0)\ne0\). Use A as a coordinate and apply the formal splitting lemma to its nondegenerate hyperbolic pair with x; the remaining one-variable term has order three with nonzero coefficient. Thus the surface germ is \(tx+y^3\), of type A2. This validates the n moving A2 points for a general carrier, while retaining the note's limitations concerning fixed singularities, other singularities, and normality.

## 4. Explicit example and its global cycle

For \(12r^2+4r+3=0\), put \(a=r+3/2\), \(b=r+1/2\), \(c=1/6-r\). Direct reduction in the quadratic field gives \(b^3=r/9-1/6\) and
\[
(ap-b)^3+(r-7/6)p(ap-b)^2+cp^4=(p-1)^3(cp+b^3).
\]
The residual root is the stated \(\kappa=(2r-3)/(18r-3)\), with residual x3 coefficient \(-\kappa/3\). The root is nonzero, simple, and distinct from one. Nonzero diagonal scaling makes its projective parametrization a smooth rational quartic of degree four. The script's field multiplication, inverse, polynomial arithmetic, and factor check match this calculation.

The properness proof is genuinely global: R0 is primitive and linear in x3 over \(k[x_0,x_1,x_2]\), with relatively prime coefficient and constant term, so Gauss's lemma makes it irreducible. R1 is not proportional to R0. The pair is consequently a regular sequence. The dense-chart components already account for degree twelve plus four; complete-intersection purity excludes further components or isolated embedded points. The full cycle is therefore \(3C+C_\kappa\).

On each endpoint chart the ideal of one reduced branch restricted to the other has nonzero cubic and quartic terms in its parameter, giving intersection length three. There are no other intersections. The reduced support has genus five.

The new global gradient calculation was reconstructed by differentiating both displayed quartics. With \(h=2r+2/3\), the gradient of R0 restricted to C is \(s^8v\), where \(v=(-2rt^4,(-a+4b)st^3,-as^3t,s^4)\). For R1 its four coefficients agree with \(ht^8v\): the first identity is \(-2rh=1\), and the remaining ones follow by substituting \(r^2=-r/3-1/4\). The vector v has no projective zero, because its final component is nonzero when s is nonzero and its first component is nonzero when s is zero. Thus the global singularity divisor is exactly \(\alpha s^8+\beta h t^8\), with no common base point and eight simple roots for \(\alpha\beta\ne0\). The local A2 argument applies at these roots. This is an actual example and does not classify all residual quartics.

## 5. Liaison and filtration arithmetic

The saturated C-primary triple T and its residual D are locally Cohen--Macaulay curves with no common component. Residual duality in the (4,4) Gorenstein curve gives \(\mathcal I_{T/W}\simeq\omega_D(-4)\). Since D has degree four, its twisted dualizing Euler characteristic is \(4n+p_a(D)-17\). Subtracting from \(16n-32\) yields \(p_a(T)=p_a(D)+16\). The union sequence then gives intersection length \(18-2p_a(D)\). These identities remain valid when D is nonreduced.

For the stated saturated triple filtration, summing Euler characteristics of \(\mathcal O_C,L,L^2(D_2)\) gives \(p_a(T)=19-3e-d_2\), hence \(p_a(D)=3-3e-d_2\). The note correctly keeps this conditional on that filtration and does not import the sole-support quadruple's restricted numerical types. In the displayed primitive e=1 example the values are sixteen, zero, and eighteen, while the reduced attachment length is six.

## Review decision

No substantive mathematical correction is required. The attained maximum, forced residual degree, integral-pencil deduction using R0001, moving singularity divisor, general moving A2 structure, and explicit example all reconstruct at the stated hypotheses. The note explicitly leaves the classification of all degree-four residual schemes open. The verifier establishes only its listed finite identities; global properness, purity, liaison, and singularity interpretation are supplied by the arguments above. No canonical result or question is created or promoted.
