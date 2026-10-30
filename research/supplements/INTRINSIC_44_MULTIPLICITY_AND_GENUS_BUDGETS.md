# INTRINSIC 44 MULTIPLICITY AND GENUS BUDGETS

## Cross-supplement synthesis: distinct (4,4) obstruction routes (editorial, not a new audit)

The historical material contains several arguments with different inputs and different logical targets. They should not be conflated:

| Route | Retained location | What it supplies | Limitation |
| --- | --- | --- | --- |
| Filtered quartic-contact calculation | [Filtered proposal and independent audit](IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-quartic-44-filtered-proof-proposalmd) | A classification- and calculation-dependent route through the two saturated numerical types and actual cubic-contact constraints | Its computational exhaustiveness and inherited hypotheses remain attached to the original audit; this synopsis is not an independent rerun |
| First-symbol pencil and surface singularities | [Intrinsic K3 proposal](INTRINSIC_44_APPROACHES_AND_CHARACTERISTIC_CONORMAL.md#intrinsic-44-k3-proof-proposal) and [audit](INTRINSIC_44_APPROACHES_AND_CHARACTERISTIC_CONORMAL.md#intrinsic-44-k3-independent-audit) | A different route from the defect algebra and first-symbol divisor to moving singularities and an exceptional-rank contradiction | Characteristic-zero and K3-specific; preserve as historical reviewed evidence, not a newly promoted result |
| Explicit local multiplication and defect types | [Intrinsic quadruple local algebra](INTRINSIC_VALUATIONS_AND_CONTACT_GEOMETRY.md#2026-10-23-intrinsic-quadruple-local-algebramd) | The local normal form and identification of the fixed divisor, with coefficient-function qualifications | Local algebra does not by itself prove global realizability or a global STCI exclusion |
| Genus and torsion budgets | [Degeneration genus budgets](#44-degeneration-genus-budgets) and [normal torsion spectral budget](#normal-torsion-spectral-genus-budget) | Numerical bookkeeping, boundary divisors, and explicit reduced/nonreduced comparison examples | Necessary conditions and examples are not sufficient to exclude all pairs |

**Shared starting point.** The fixed quartic curve, its conormal bundle and the generic transverse length-four hypothesis belong to the common setup. The filtered and surface-singularity arguments then diverge: one analyzes actual quartic lifting/contact spaces; the other counts singularities of a general pencil member. The genus-budget work instead studies what numerical restrictions survive under degeneration. The local-algebra source is a bridge between the two obstruction routes, not a replacement for either global step.

**Preservation rule.** Keep the explicit triple-multiplicity plus residual-quartic examples in [the multiplicity-three construction](#44-multiplicity-three-forces), the negative control where quadric restrictions fail to determine normal multiplicity in [the proof-routes discussion](#44-intrinsic-proof-routes), and the nonreduced degeneration examples in [the genus-budget section](#44-degeneration-genus-budgets). These prevent the stronger-looking arguments from being incorrectly extended to lower generic multiplicity, arbitrary residual support, or higher degrees. The source audits and their epistemic qualifications remain authoritative for their own claims.

---


Permanent subject consolidation. All source mathematical detail retained with its original conditional and audited status; no new theorem promotion.


---

## 44-intrinsic-proof-routes

# Curve-centered proof routes for multiplicity four

Date: 2026-10-26. Status: exploratory synthesis, an explicit reformulation of an existing proof, and new negative controls; independently reviewed in the [audit](#2026-10-26-44-intrinsic-proof-routes-audit). No canonical promotion.

## 1. Question and honest distinction

For the fixed characteristic-zero rational quartic
\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3,
\]
can multiplicity four in a proper quartic pair be excluded by an argument intrinsic to the marked curve, without a classification of K3 surface singularities?

Two requests should be distinguished. The singularity classification can be removed completely: the equations forced by the marked neighborhood admit direct blowup calculations, and Noether's formula and Hodge theory finish the same global surface obstruction. This is a complete reformulation of the [existing independently audited proof](INTRINSIC_44_APPROACHES_AND_CHARACTERISTIC_CONORMAL.md#intrinsic-44-k3-proof-proposal), retaining its [audit](INTRINSIC_44_APPROACHES_AND_CHARACTERISTIC_CONORMAL.md#intrinsic-44-k3-independent-audit). It is not a new obstruction or a purely curve-only proof.

A proof using only the embedded infinitesimal neighborhoods and actual quartic source, with no global surface-rank bound, remains missing. Sections 4--6 give concrete reasons why genus, conormal degrees, the quadric restriction, and numerical positivity alone cannot supply it, and state a precise sufficient nonvanishing theorem.

The accepted balanced conormal [R0020](../results/quartic_conormal_characteristic_jump.md), the unique smooth quadric and its ruling classes, and rank-four finite-flat Gorenstein duality are retained. Neither R0001 nor R0022 is used to establish the multiplicity-four contradiction. No inherited proof or certificate is rerun.

## 2. What the marked neighborhood already forces

The hypothetical complete intersection W has degree sixteen and generic multiplicity four along C. Purity and degree imply sole reduced support C. The elementary unique-quadric argument excludes any quartic pencil member of normal order at least two: it would be a multiple of q² and could not yield sole support C on the quadric. Thus the generic algebra is curvilinear of length four.

The existing local multiplication and duality argument gives
\[
L=\mathcal O(e-7),\quad E_2=L^2(D),\quad
E_3=L^3(D)=\mathcal O(-18),\quad \deg D=3-3e.
\]
Here degrees are on the normalization \(C\simeq\mathbf P^1\), with ambient \(\mathcal O_C(4)=\mathcal O(16)\). Effectivity leaves e=1,D=0 or e=0,deg D=3. The common fixed divisor of the actual first normal symbols is exactly D, and the moving pencil has degree \(6+2e\).

At primitive points the exact ambient local ideal is \((m,\ell^4)\). At a defect of multiplicity d it is \((x^2,y^2-t^d x)\). These are derived from rank-four multiplication, not from a classification of surface singularities. The primitive moving-zero calculation gives a general carrier equation \(uv-t^4\). At a defect, the parametric Morse calculation gives \(uv-t^{2d}\). Only exponents 2,4,6 occur. Bertini gives smoothness outside C. These conclusions, including arbitrary local coefficient functions, are proved in the preserved [local-algebra note](INTRINSIC_VALUATIONS_AND_CONTACT_GEOMETRY.md#2026-10-23-intrinsic-quadruple-local-algebra).

## 3. Direct blowups and a classification-free surface bound

Consider the local equation
\[
uv-t^r=0,\qquad r\in\{2,4,6\}.
\]
Blow up the origin in its smooth ambient threefold. In the u-chart, put v=u v1,t=u t1; the strict transform is
\[
v_1-u^{r-2}t_1^r=0,
\]
which is smooth. The v-chart is similar. In the t-chart put u=t u1,v=t v1; the equation is
\[
u_1v_1-t^{r-2}=0.
\]
For r=2 the exceptional curve is a smooth conic. For r>2 the exceptional curve consists of two projective lines; the only remaining singular point lies at their intersection in the t-chart. Repeating this calculation inserts the exceptional curves of the exponent r-2 equation between the two lines. Hence the final exceptional curves form a chain, with counts
\[
N(2)=1,\qquad N(r)=2+N(r-2),\qquad N(r)=r-1.
\]
This directly gives one, three, and five curves for r=2,4,6. No surface-singularity classification is invoked.

Every blowup center is an ambient point at which the strict surface has multiplicity two. If \(\pi\) is such an ambient blowup, its canonical discrepancy is 2E and its strict surface is \(\pi^*S-2E\). Adjunction therefore gives
\[
K_{S'}=\pi^*K_S.
\]
Thus the full explicit resolution is crepant. The original integral quartic has trivial dualizing sheaf by hypersurface adjunction, so the smooth projective resolution \(\widetilde S\) has trivial canonical line bundle, without appealing to a K3 classification or a theorem recognizing rational double points. Integrality and normality follow as in the original proof from the finite singular locus; they are not input assumptions.

The exceptional components are smooth rational curves. Adjunction on the resolution makes their self-intersections -2. The tridiagonal chain matrix is negative definite, with nonzero determinant of absolute value r; the r-1 classes are independent. Different singular points give disjoint chains.

For completeness, the needed global bound can also be derived without naming the surface type. Work over the complex numbers after descent from a finitely generated characteristic-zero coefficient field. Put \(q=h^1(\mathcal O_{\widetilde S})\). Since the canonical line bundle is trivial, \(p_g=1\) and \(\chi(\mathcal O)=2-q\). Noether's formula and Hodge decomposition give
\[
c_2=12(2-q),\qquad
b_2=c_2-2+4q=22-8q,\qquad
h^{1,1}=b_2-2p_g=20-8q\le20.
\]
These are general smooth projective surface identities, not a classification theorem; see [Hacking's surface notes](https://paulhacking.github.io/surfaces.pdf), sections 2,5,6. The pullback hyperplane class has square four and is orthogonal to the exceptional chains. Thus the total exceptional rank is at most \(h^{1,1}-1\le19\).

The marked-neighborhood calculation, however, requires
\[
3(6+2e)+\sum_{p\in\operatorname{Supp}D}(2d_p-1)
=24-\#\operatorname{Supp}D\ge21.
\]
This is a contradiction. It is a complete exclusion with direct local blowups and general Hodge/Noether theory. Its remaining global surface input should not be advertised as a purely C-intrinsic proof.

## 4. A real quadruple with the right lower invariants

Let \(Q\simeq\mathbf P^1\times\mathbf P^1\) be the unique quadric, with C of type (1,3), and take the actual Cartier divisor
\[
Y=4C\subset Q.
\]
It has degree sixteen and
\[
p_a(Y)=1+\tfrac12(4,12)\cdot(2,10)=33.
\]
Its primitive nilpotent layers are
\[
\mathcal O_C,\quad\mathcal O(-6),\quad
\mathcal O(-12),\quad\mathcal O(-18).
\]
Thus it has exactly the Hilbert polynomial and graded-layer degrees of the primitive hypothetical (4,4) structure. Those data cannot alone exclude a quadruple.

Of course Y is not a proper (4,4) intersection: every quartic through it contains Q, since \((4,4)-4(1,3)=(0,-8)\) has no sections. Explicitly,
\[
H^0(\mathcal I_Y(4))=qH^0(\mathcal O_{\mathbf P^3}(2)).
\]
This is already enough to exclude this particular candidate, not all possible marked quadruples.

There is also an intrinsically infinitesimal failure of complete-intersection adjunction. One has
\[
\omega_Y=\mathcal O_Q(2,10)|_Y,\qquad
\omega_Y\otimes\mathcal O_Y(-4)=\mathcal O_Q(-2,6)|_Y.
\]
The discrepancy is trivial on C, but nontrivial even on 2C in characteristic zero. Here is a direct cohomological proof. Put \(M=\mathcal O_Q(-2,6)\). The sequence
\[
0\to\mathcal O_Q(-4,0)\xrightarrow{c_C^2}M\to M|_{2C}\to0
\]
identifies \(H^0(M|_{2C})\) with the kernel of multiplication by \(c_C^2\) on H1. In Segre coordinates C has equation \(ad^3-bc^3\). In natural Cech bases the three-dimensional source maps to the span of
\[
d^6,\quad -2c^3d^3,\quad c^6
\]
in \(H^0(\mathcal O_{\mathbf P^1}(6))\). These sections are independent in characteristic zero, so the map is injective and \(H^0(M|_{2C})=0\). A trivial line bundle would have a nonzero section. Thus the full dualizing sheaf fails to match even though its restriction to C matches. The vanishing of the middle coefficient in characteristic two is informative but is not used as a proof of existence there.

This control shows why a stronger intrinsic proof must retain the nonlinear marked neighborhood and its line-bundle gluing, not only restriction to the reduced C. It gives no assertion that an arbitrary hypothetical W lies in Q.

## 5. The quadric restriction forgets transverse multiplicity

There is a sharper negative control for a proof using only the two residual (3,1) divisors on Q. Set
\[
F=x_1^4-x_0^3x_3,\quad G=x_2^4-x_0x_3^3,
\quad q=x_0x_3-x_1x_2.
\]
For the actual triple example from the [preceding note](#44-multiplicity-three-forces), take \(12r^2+4r+3=0\) and put
\[
a=r+3/2,\quad b=r+1/2,\quad
c=1/6-r,\quad d=r-7/6.
\]
Its equations satisfy the direct identities
\[
R_0=bF+ax_0^2q,\qquad R_1=cG-dx_3^2q.
\]
Hence their restricted pencils on Q are identical up to nonzero basis scalars. Nevertheless \(m_C(V(F,G))=1\), while \(m_C(V(R_0,R_1))=3\). The same residual ruling divisors and base scheme on Q can therefore have different transverse multiplicities in projective space. Restriction to Q loses precisely some of the necessary normal lifting information.

## 6. The exact C-neighborhood target

The existing [intrinsic cubic-contact construction](INTRINSIC_VALUATIONS_AND_CONTACT_GEOMETRY.md#2026-10-23-intrinsic-cubic-contact-construction) formulates a genuinely marked-neighborhood obstruction. For a quasiprimitive triple T with ideal J define
\[
\mathcal M_T=(J/I_CJ)/\mathrm{torsion}.
\]
The actual two-dimensional source W of quartic equations gives
\[
\rho_T:W\otimes\mathcal O_C\longrightarrow\mathcal M_T(4).
\]
Its determinant is a section of degree four or six in the two adjunction-allowed cases. At generic contact at least three, with a nonzero first symbol,
\[
\det\rho_T\ne0\iff m_C(V(W))=3.
\]
A fully C-neighborhood proof would show that every proper actual quartic source in the allowed types has nonzero determinant, using the full embedded transition and without enumerating triple directions or quartic pencils. This is a precise sufficient statement, not a proved new theorem here. The established coordinate contact proof proves it using those classifications; the intrinsic construction alone does not.

Positivity of the determinant line is insufficient. The contact note gives abstract models \(\mathcal M_T(4)=\mathcal O(2)^2\) or \(\mathcal O(3)^2\), with the relevant exact-sequence degrees, in which two independent sections lie in a single summand and have zero wedge. Such models are not claimed realizable by the actual embedding. They identify why the actual source is indispensable.

For the primitive e=1 branch there is also a geometric normal-bundle formulation. After three successive blowups along C and its prescribed normal-direction sections, the remaining reduced base curve C3 is isomorphic to C. The transformed quartic line bundle restricts to \(\mathcal O_C(-2)\). Two actual generators of its ideal would force
\[
N_{C_3/X_3}\simeq\mathcal O(-2)^2.
\]
The numerical normal sequence is only
\[
0\to\mathcal O(-10)\to N_{C_3/X_3}\to\mathcal O(6)\to0,
\]
which permits that balanced middle bundle. Proving the actual extension from this embedding cannot be balanced would be a sufficient intrinsic obstruction in this primitive branch; the defective branch would still require its own treatment. Numerical splitting or positivity cannot be assumed. This is an alternative necessary condition, not an equivalence to global quartic realization.

## 7. Status and continuation

The direct-resolution reformulation is complete and avoids the classification of surface singularities and of K3 surfaces, while retaining a global Hodge/Noether bound. It is a refinement of the existing proof's exposition, not a stronger scope result. The marked-neighborhood-only nonvanishing remains unresolved by these deductions. The negative controls and normal-bundle criterion make that missing implication explicit. No canonical exclusion is reopened or promoted, no inherited experiment is rerun, and no all-degree STCI conclusion follows.



---

## 44-multiplicity-three-forces-audit

# Independent audit: what multiplicity at least three forces in (4,4)

Date: 2026-10-26. Reviewer: independent `triple_classification` agent. Reviewed document: [multiplicity-three deductions](#44-multiplicity-three-forces). **Outcome: the stated deductions pass independent reconstruction at their stated scopes. No canonical promotion.**

## Scope and accepted premises

The field is algebraically closed of characteristic zero, the curve is the fixed embedding \(C=[s^4:s^3t:st^3:t^4]\), and the quartic pair is proper. The audit read the research index and the literal promoted statements of [R0001](../results/quartic_carrier_exclusion.md), [R0020](../results/quartic_conormal_characteristic_jump.md), and [R0022](../results/quartic_44_filtered_exclusion.md). Their accepted proofs and certificates are premises, not verification tasks. The earlier [smooth-carrier deduction](#44-degeneration-genus-budgets) and the accepted source-level conjugate pencil in the [filtered proof](IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-quartic-44-filtered-proof-proposalmd) were consulted at their recorded scope.

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



---

## 44-multiplicity-three-forces

# What multiplicity at least three forces in a (4,4) intersection

Date: 2026-10-26. Status: new deductions and explicit residual calculation, independently reviewed in the [audit](#44-multiplicity-three-forces-audit); no canonical promotion.

## 1. Exact question, inputs, and answer

Let k be algebraically closed of characteristic zero, let
\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3,
\]
and let \(W=V(F,G)\) be a proper complete intersection of two quartics containing C. Suppose its generic transverse multiplicity \(m_C(W)\) is at least three. The conclusion is:

1. The multiplicity is exactly three and \([W]=3[C]+R\), with R an effective degree-four cycle having no C component.
2. Every nonzero member of the quartic pencil is integral. This conclusion uses the accepted all-mate-degree quartic-carrier exclusion R0001.
3. Every member is singular somewhere on C. There is a nonconstant pencil map on C whose fibers give moving singular points; a common singular point is not forced.
4. At the general moving points the carrier singularities are \(A_2\). In particular, this case has a different singularity budget from the previously excluded multiplicity-four case.
5. The case occurs: an explicit proper pair has cycle \(3C+C_\kappa\), with \(C_\kappa\) a distinct smooth rational quartic. For this example a general pencil member has eight moving \(A_2\) points on C and there are no fixed common singular points on C.

This closes the multiplicity/residual-existence question in degree (4,4): the maximum multiplicity is three, it is attained, and at that maximum the residual degree is exactly four. It does not classify every possible degree-four residual scheme.

Promoted premises, used without rerunning their proofs:

- [R0022](../results/quartic_44_filtered_exclusion.md): no proper quartic pair has sole reduced support this C in characteristic zero.
- [R0001](../results/quartic_carrier_exclusion.md): no integral quartic carrier through this C admits any homogeneous mate with sole support C.
- [R0020](../results/quartic_conormal_characteristic_jump.md): \(N^*_{C/\mathbf P^3}=\mathcal O_{\mathbf P^1}(-7)^2\).

The elementary identity \(H^0(\mathcal I_C^2(4))=kq^2\), for \(q=x_0x_3-x_1x_2\), and the new [smooth-carrier lemma](#44-degeneration-genus-budgets) are already independently reviewed. The displayed conjugate pencils below are inherited accepted source-level evidence from [October 7, section 4](2026-10-07-session-mf6-e1-independent-audit.md) and [the October 23 filtered proof](IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-quartic-44-filtered-proof-proposalmd). Their residual factorization and geometric interpretation are the new calculation here. No exhaustiveness assertion from the multiplicity-four classification is transferred to arbitrary multiplicity-three pairs.

## 2. Exactly triple, with a real degree-four residual

Bézout gives \(4m_C(W)\le16\), so \(m_C(W)\le4\). If equality held, purity of the complete intersection and degree exhaustion would imply \(W_{\mathrm{red}}=C\), contrary to R0022. Hence
\[
\boxed{m_C(W)=3,\qquad [W]=3[C]+R,\qquad\deg R=4.}
\]
The degree-four cycle R is downstairs in projective space; no exceptional component on a blowup is being counted as a residual curve. Its being integral, reduced, smooth, or rational does not follow from this degree argument.

The generic transverse algebra is necessarily curvilinear. In a transverse regular local surface, a length-three complete intersection cannot have embedding dimension two: if both equations had order at least two, local intersection multiplicity would be at least four. Thus over \(K=k(C)\), after completion,
\[
\widehat{\mathcal O}_{W,\eta_C}\simeq K[\epsilon]/(\epsilon^3).
\]

## 3. Every carrier in the pencil is integral

First, no pencil member can have a quadratic factor carrying C. That factor must be the unique quadric q. A quartic mate not divisible by q restricts to a divisor of type (4,4) on \(Q\simeq\mathbf P^1\times\mathbf P^1\), while C has type (1,3). C occurs at most once, since (4,4)-2(1,3)=(2,-2) is not effective. Thus a member q times a quadratic not carrying C gives multiplicity one; the only repeated quadratic carrying case \(q^2\) gives multiplicity two. Both contradict m=3.

If a quartic member H were reducible, C would therefore lie on an integral cubic factor A, with \(H=A\ell\) and the plane \(\ell=0\) not containing C. For another basis member G,
\[
m_C(A,G)=3.
\]
If G is integral, the proper intersection \(V(A,G)\) has degree twelve and already contains the degree-twelve cycle 3C. Purity gives sole support C, contradicting R0001 with G as the integral quartic carrier and A as its mate. This uses the literal promoted statement of R0001, rather than assuming R0022 covers degrees (3,4).

If G is reducible, the quadratic case is already excluded, so its carrying factor is an integral cubic B and its remaining factor is a plane. Properness excludes A=B; Bézout gives degree nine for \(V(A,B)\), which cannot contain 3C of degree twelve. This also contradicts m=3. Therefore
\[
\boxed{\text{Every nonzero member of the pencil is an integral quartic.}}
\]
This conclusion is not claimed independently of the accepted R0001 premise.

## 4. A moving singularity divisor on C

Write \(E=N^*_{C/\mathbf P^3}=\mathcal O(-7)^2\). At generic multiplicity three, the two first normal symbols are dependent. Their saturated common image line is
\[
M=\mathcal O(-7-e)\subset E,\qquad e\ge0,
\]
with locally free quotient \(L=\mathcal O(e-7)\). Saturation is important: a local generator of M has no zero in E.

After twisting by \(\mathcal O_C(4)=\mathcal O_{\mathbf P^1}(16)\), write
\[
\sigma_F=h_0m,\qquad\sigma_G=h_1m,\qquad
h_0,h_1\in H^0(\mathcal O_{\mathbf P^1}(9-e)).
\]
The sections \(h_0,h_1\) are linearly independent. Otherwise a nonzero constant pencil combination would have zero first symbol, hence would be a nonzero multiple of q², which section 3 has excluded. Consequently
\[
0\le e\le8.
\]

Let B be the common zero divisor of \(h_0,h_1\), and put \(b=\deg B\). Removing B gives a basepoint-free, nonconstant pencil on C, of degree
\[
\boxed{n=9-e-b\ge1.}
\]
Equivalently, it gives the nonconstant map from a curve point to the pencil member singular there. Its degree is n. For \(H=\alpha F+\beta G\), the scheme of singular points of H restricted to C is the zero divisor of \(\alpha h_0+\beta h_1\). This follows because H vanishes identically on C and its differential along C is precisely its normal symbol; the saturated direction m is nonzero in every fiber.

Every member thus has a singularity divisor of degree \(9-e\) on C, counting the vanishing orders of the first symbol. For a general member, this consists of the fixed divisor B plus n distinct moving points. Characteristic-zero separability is used for generic simplicity. In particular, every member is singular somewhere on C, and the moving part has positive degree even when B is nonempty. The assertion does not force B to be nonempty.

## 5. The general moving singularities are A2

Remove the finite subset of C where the primary triple is nonprimitive or where the residual scheme meets C. Locally on the remaining open set, the actual complete-intersection ideal is
\[
I_W=(x,y^3)
\]
in smooth ambient coordinates (t,x,y), with \(C=(x,y)\). This is an open normal form for the generic curvilinear triple, not a global normal-flatness assertion.

The two quartics generate this ideal, so their coefficient matrix relative to the generators x and y³ is invertible. At a simple moving first-symbol zero for H, its x coefficient vanishes simply in t. A second pencil generator has unit x coefficient there; invertibility forces the y³ coefficient of H to be a unit. Thus
\[
H=xA(t,x,y)+y^3B(t,x,y),\qquad
\partial_t A(0)\ne0,\quad B(0)\ne0.
\]
A formal coordinate change using A as a coordinate, followed by a unit adjustment, gives
\[
\boxed{H=tx+y^3,\quad\text{an }A_2\text{ surface singularity}.}
\]
The general moving fibers avoid the finite removed subset and the branch values of the pencil map. Hence a general carrier has n moving A2 singularities on this open subset of C. It may have additional fixed singularities or singularities elsewhere. Normality or a global K3 resolution is not asserted for every such pencil.

This explains the change from the hypothetical multiplicity-four mechanism: a local triple \((x,y^3)\) produces A2 at a simple moving zero; the analogous quadruple \((x,y^4)\) produces A3. Their exceptional-rank budgets differ.

## 6. An explicit genuine 3C plus a rational quartic

Choose r satisfying \(12r^2+4r+3=0\) and define
\[
\begin{aligned}
R_0&=x_0^3x_3-(r+3/2)x_0^2x_1x_2+(r+1/2)x_1^4,\\
R_1&=x_0x_3^3+(r-7/6)x_1x_2x_3^2+(1/6-r)x_2^4.
\end{aligned}
\]
Set \(a=r+3/2\), \(b=r+1/2\), \(c=1/6-r\). On \(x_0=1\), take \(x_1=z\), \(x_2=pz^3\), \(x_3=qz^4\). The first equation gives \(q=ap-b\), and the second gives the exact factorization
\[
q^3+(r-7/6)pq^2+cp^4=(p-1)^3(cp+b^3).
\]
The residual root is
\[
\kappa=\frac{2r-3}{18r-3},\qquad q=-\frac\kappa3,
\qquad27\kappa^2-14\kappa+3=0.
\]
The constants \(\kappa\) and \(-\kappa/3\) are nonzero, and \(\kappa\ne1\). Therefore
\[
C_\kappa=[s^4:s^3t:\kappa st^3:-(\kappa/3)t^4]
\]
is a distinct smooth rational quartic, obtained by a diagonal projective transformation of C. The simple residual root and triple root yield
\[
\boxed{[V(R_0,R_1)]=3[C]+[C_\kappa].}
\]

For global properness, R0 is a primitive linear polynomial in x3 over k[x0,x1,x2]: its coefficient x0³ is coprime to its constant coefficient because \(b\ne0\). Gauss's lemma makes R0 irreducible. R1 is not proportional to it, so the intersection is proper. The identified cycle already has degree sixteen, and purity rules out further cycle or isolated components. The calculation establishes an actual global pair, beyond a transverse formal model.

The residual quartic lies on \(3x_0x_3+x_1x_2=0\), not on the original Q. It meets C only at the endpoints, with intersection length three at each: on the finite chart the differences are \((\kappa-1)z^3\) and \((-\kappa/3-1)z^4\); the opposite chart gives the same minimum order. Thus the reduced union \(C\cup C_\kappa\) has arithmetic genus five. Its genus is different from that of the full (4,4) scheme.

The inherited first-symbol coefficients on the finite chart are
\[
h_{R_0}=1,\qquad h_{R_1}=(2r+2/3)z^8,
\]
as sections of \(\mathcal O_{\mathbf P^1}(8)\). This also follows directly from the global gradients: put \(h=2r+2/3\) and
\[
v=(-2rt^4,(-a+4b)st^3,-as^3t,s^4).
\]
Then \(\nabla R_0|_C=s^8v\), \(\nabla R_1|_C=ht^8v\), and v is nowhere zero. Thus the singularity divisor on C of \(\alpha R_0+\beta R_1\) is
\[
\alpha s^8+\beta h t^8=0.
\]
There is no common projective zero: R0 is smooth at every finite point of C, and R1 is smooth at infinity. For \(\alpha\beta\ne0\), there are eight distinct moving zeros, hence eight moving A2 points. No common singular point on C is forced by multiplicity three. Eight A2 configurations have total exceptional rank sixteen, which by itself causes no K3 rank contradiction.

The new exact factorization and chart checks are reproducible with the standard-library [verifier](../computations/verify_44_triple_residual_example_2026_10_26.py); its [execution record](../validation/44-triple-residual-2026-10-26/README.md) distinguishes finite identities from the global purity and properness proof above. No inherited certificate is rerun.

## 7. Residual genus and what is not classified

Let T be the saturated C-primary triple and D the residual scheme. They are locally Cohen--Macaulay curves linked in W, of degrees twelve and four. Liaison gives
\[
p_a(T)-p_a(D)=16.
\]
For completeness, the duality sequence has kernel
\(\mathcal I_{T/W}\simeq\omega_D(-4)\). Its Euler characteristic is \(4n+p_a(D)-17\); subtracting from \(\chi(\mathcal O_W(n))=16n-32\) gives \(p_a(T)=p_a(D)+16\). The union sequence then gives
\[
\operatorname{length}(T\cap D)=18-2p_a(D).
\]

If the saturated quasiprimitive triple filtration is written
\[
\mathcal O_C,\quad L=\mathcal O(e-7),\quad
L^2(D_2),\qquad d_2=\deg D_2,
\]
its Euler characteristic yields
\[
p_a(T)=19-3e-d_2,\qquad
\boxed{p_a(D)=3-3e-d_2.}
\]
This formula uses the stated triple filtration, not the Gorenstein graded pairings of a sole-support quadruple. The restrictions e=0,d2=3 or e=1,d2=0 from the excluded multiplicity-four problem cannot be asserted for every multiplicity-three pair.

In the displayed primitive e=1 example, \(p_a(T)=16\), \(p_a(D)=0\), and \(\operatorname{length}(T\cap D)=18\). The reduced intersection \(C\cap D\) has length six. The previously derived eighteen-unit boundary for a reduced marked component must not be applied to this nonreduced W by replacing T with C.

The forced residual cycle has degree four, but the present argument does not prove it always integral, reduced, rational, or on a fixed quadric. A complete residual classification would require controlling all actual quartic source spaces for the possible defective triple structures. The accepted multiplicity-four proof classifies only its forced types. This additional classification is not needed to close the maximum-multiplicity and residual-existence assertions proved here.

## 8. Review and frontier impact

The independent review reconstructs the new deductions, checks the explicit global example, and retains the stated accepted premises. The new verifier proves its listed finite polynomial identities only. Canonical exclusions remain premises and are not retested. No canonical record, proof, or unrestricted STCI status changes. The new conclusion is the attained maximum three, the forced residual degree four, and the singularity structure of the entire integral pencil at that maximum.

## 9. An independent route to the multiplicity-four bound

The use of R0022 in section 2 can be replaced by the existing, independently audited [October 23 K3 proof](INTRINSIC_44_APPROACHES_AND_CHARACTERISTIC_CONORMAL.md#intrinsic-44-k3-proof-proposal), with its [independent audit](INTRINSIC_44_APPROACHES_AND_CHARACTERISTIC_CONORMAL.md#intrinsic-44-k3-independent-audit) and [rank-four local algebra](INTRINSIC_VALUATIONS_AND_CONTACT_GEOMETRY.md#2026-10-23-intrinsic-quadruple-local-algebra). That proof is explanatory evidence, not a promoted canonical result. It is the multiplicity-four analogue of the moving-A2 argument above and uses neither R0001 nor R0022.

Under hypothetical multiplicity four, purity and degree give sole support C. The smooth-quadric calculation excludes any order-two quartic member, so the generic transverse algebra is curvilinear of length four. Saturated Gorenstein duality gives
\[
L=\mathcal O(e-7),\quad E_2=L^2(D),\quad
E_3=L^3(D)=\mathcal O(-18),\quad\deg D=3-3e.
\]
Hence the primitive case is e=1,D=0; the only defective case is e=0,deg D=3. At a defect of multiplicity d, the exact embedded local ideal is \((x^2,y^2-t^d x)\). Its first-symbol fixed divisor is exactly D. Removing D leaves a basepoint-free pencil of degree \(6+2e\), so a general quartic has that many moving A3 points and, at each defect, a fixed singularity of type \(A_{2d-1}\).

| Type | Moving singularities | Fixed singularities | Exceptional rank |
| --- | --- | --- | ---: |
| e=1, D=0 | 8 A3 | none | 24 |
| e=0, D=p+q+r | 6 A3 | 3 A1 | 21 |
| e=0, D=2p+q | 6 A3 | A3+A1 | 22 |
| e=0, D=3p | 6 A3 | A5 | 23 |

Bertini gives smoothness off C; the displayed local forms show the singular locus is finite and consists only of rational double points. Finite singular locus itself proves the general carrier integral and normal, without the integrality argument of section 3 or its R0001 premise. Its minimal resolution is K3. The exceptional classes form a negative-definite lattice orthogonal to the positive-square hyperplane class, so their rank is at most nineteen in characteristic zero. Every row contradicts this bound.

This replaces the R0022 input for the maximum-multiplicity assertion. The all-members-integral assertion for arbitrary multiplicity-three pencils in section 3 still has its explicitly separate R0001 dependency; the K3 argument here makes no all-mate-degree claim. Existing proof, audit, and computation artifacts were preserved and no inherited proof or certificate was rerun for this explanation.



---

## 44-intrinsic-proof-routes-audit

# Independent audit: curve-centered proof routes for multiplicity four

Date: 2026-10-26. Reviewer: independent `intrinsic_intersection_route` agent. Reviewed document: [proof routes and negative controls](#44-intrinsic-proof-routes). **Outcome: the stated direct-resolution reformulation and negative controls pass independent reconstruction at their stated scopes. No canonical promotion.**

## Scope and retained premises

The curve is the fixed embedding \(C=[s^4:s^3t:st^3:t^4]\) over an algebraically closed field of characteristic zero. The pair consists of proper quartics. The reviewer read the research index, the reviewed note, and the preserved [October 23 proof](INTRINSIC_44_APPROACHES_AND_CHARACTERISTIC_CONORMAL.md#intrinsic-44-k3-proof-proposal). Its previously audited rank-four multiplication and duality deductions were retained as premises, rather than rerunning accepted proofs or certificates.

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

The determinant target and its degree-four/degree-six alternatives are retained at the exact scope of the [intrinsic cubic-contact construction](INTRINSIC_VALUATIONS_AND_CONTACT_GEOMETRY.md#2026-10-23-intrinsic-cubic-contact-construction). The source correctly calls classification-free nonvanishing for actual quartic sources an unresolved sufficient statement. The abstract rank-one source examples demonstrate why the line-bundle degrees alone do not prove it.

For the primitive e=1 branch, the blowup normal degrees reconstruct as follows. The first selected normal line has degree six inside \(N_C=\mathcal O(7)^2\). The successive normal sequences have degrees (2,6), (-4,6), and finally (-10,6). The transformed quartic line bundle has successive degrees 10,4,-2 on the successive center curves. After three blowups, actual generation of the reduced remaining center ideal by two such sections would give its conormal bundle \(\mathcal O(2)^2\), equivalently normal bundle \(\mathcal O(-2)^2\).

The final sequence \(0\to\mathcal O(-10)\to N\to\mathcal O(6)\to0\) does permit this middle bundle: two degree-eight forms with no common zero embed \(\mathcal O(-10)\) in \(\mathcal O(-2)^2\), with quotient \(\mathcal O(6)\). It cannot be split or ruled out numerically. The source properly states a necessary condition and an unproved sufficient obstruction, not an equivalence to global realization. The defective branch is explicitly left separate.

## Review decision

No substantive mathematical correction was required. The direct blowup calculation removes the surface-singularity classification while retaining the global Hodge/Noether obstruction. The negative controls establish genuine limits of simpler numerical and quadric-only approaches. A proof confined to the marked infinitesimal neighborhood is not claimed. Existing accepted evidence retains its status; no canonical result or question is created, promoted, or reopened.



---

## 44-degeneration-genus-budgets

# Degenerating a (4,4) curve: cycles, gluing, and nilpotent genus

Date: 2026-10-26. Status: exploratory synthesis and new elementary deductions; independent review is recorded in the [audit](#44-degeneration-genus-budgets-audit). No canonical promotion.

## 1. Question and scope

What can a smooth complete-intersection curve of type (4,4) in projective three-space degenerate into, and what does the fixed Hilbert polynomial actually constrain? First allow all proper pairs; then retain the marked curve
\[
C=[s^4:s^3t:st^3:t^4].
\]
The field is algebraically closed of characteristic zero; statements about ordinary topology use the associated complex curve. A proper pair has no common surface component. Throughout, a cycle means the fundamental effective one-cycle of an actual scheme, not the full scheme structure.

Completion of this move means deriving the genus and componentwise boundary constraints, giving actual smoothable examples at several extremes, and isolating the additional information needed when a component acquires multiplicity. It does not mean classifying all degree partitions or all embedded limits.

Promoted inputs are [R0021](../results/quartic_mu4_degeneration.md), for the prescribed four-quartic configuration, and the precise scope of [R0022](../results/quartic_44_filtered_exclusion.md), for the already established fixed-curve (4,4) exclusion. Neither exclusion proof is rerun. The [previous cycle notebook](2026-10-25-ci-cycle-geometry-notebook.md) and [conductor/topology note](2026-10-25-ci-cycle-conductor-topology.md), with their linked audits, supply reviewed but unpromoted geometry. The smooth-carrier dichotomy in section 7 is a new elementary deduction, independently reconstructed during this move.

## 2. What is conserved

The Koszul resolution of a proper pair of degrees (a,b) gives
\[
P_W(n)=abn-\frac{ab(a+b-4)}2,\qquad
p_a(W)=1+\frac{ab(a+b-4)}2.
\]
Adjunction gives the additional, stronger constraint
\[
\omega_W\simeq\mathcal O_W(a+b-4).
\]
These assertions hold for nonreduced complete intersections too. Such a curve is pure, Cohen--Macaulay, and Gorenstein; the Koszul resolution also gives \(H^0(\mathcal O_W)=k\), hence connectedness and \(h^1(\mathcal O_W)=p_a(W)\).

For (4,4), these become
\[
\deg W=16,\quad P_W(n)=16n-32,\quad p_a(W)=33,
\quad\omega_W=\mathcal O_W(4).
\]
The open locus of proper pencils in \(\operatorname{Gr}(2,H^0(\mathcal O_{\mathbf P^3}(4)))\) carries a flat universal complete-intersection family, and smooth members form a dense open subset. Every proper pair discussed here can therefore be smoothed by a general perturbation. A specialization acquiring a common surface leaves this open locus: its two specialized equations need not describe the flat curve limit.

For general flat projective families, constancy of Euler characteristics of twists follows from [Stacks, Lemma 36.32.2](https://stacks.math.columbia.edu/tag/0B9T), applied to the structure sheaf and its twists. This is coherent Euler characteristic, not ordinary topological Euler characteristic. A cycle alone does not have a specified arithmetic genus: the gluing and nilpotent structure are essential.

## 3. The reduced genus budget and the graph

Let W be reduced, with r integral components, normalization genera \(g_i\), and local delta invariants \(\delta_p\). The normalization exact sequence gives
\[
33=\sum_i g_i+\delta(W)-r+1,
\qquad \delta(W)=\sum_p\delta_p.
\]
Thus \(\delta=32+r-\sum g_i\). For definitions and finite normalization quotients see [Stacks, delta invariant](https://stacks.math.columbia.edu/tag/0C3Q).

For nodal curves this is the familiar graph identity
\[
33=\sum_i g_i+b_1(\Gamma).
\]
For arbitrary reduced curves, use the bipartite graph of normalized components and singular points, with an edge for each local branch. If \(r_p\) is the number of branches at p, put
\[
b=\sum_p(r_p-1)-r+1,\qquad
u=\delta-\sum_p(r_p-1).
\]
Then
\[
33=\sum_i g_i+b+u.
\]
Here b counts graph loops, while u measures gluing beyond identifying the branch origins. In characteristic zero these are the abelian, toric, and unipotent dimensions of the generalized Jacobian, as explained in the earlier conductor/topology note. In particular, tangencies can contribute arithmetic genus without adding the same number of topological loops.

For the complex reduced curve,
\[
b_1(W)=2\sum_i g_i+b,\quad b_2(W)=r,
\quad\chi_{\rm top}(W)=2r-2\sum_i g_i-\sum_p(r_p-1).
\]
The smooth fiber has Euler characteristic -64. The local complete-intersection Milnor formula
\(\mu_p=2\delta_p-r_p+1\) gives
\[
\chi_{\rm top}(W)=-64+\sum_p\mu_p.
\]
The local formula is [Dimca--Greuel, Theorem 2.1(1), p. 115](https://www.journalofsing.org/volume18/dimca-greuel.pdf), attributing it to Buchweitz--Greuel. These reduced isolated-singularity formulas do not apply by simply reducing a generically nonreduced fiber.

## 4. Actual reduced configurations

### Sixteen lines: all genus in graph loops

Choose eight planes \(A_i,B_j\), \(1\le i,j\le4\), in general linear position and set
\[
F=\prod_i A_i,\qquad G=\prod_j B_j.
\]
The sixteen lines \(L_{ij}=V(A_i,B_j)\) meet precisely when they share a row or column. General position rules out fourfold plane intersections and hence triple points of the curve. There are
\[
4\binom42+4\binom42=48
\]
ordinary nodes, so the rook graph has \(48-16+1=33\) loops. Each line has six attachments. This is a complete intersection with genus allocation \((\sum g_i,b,u)=(0,33,0)\).

It also gives the sharp upper bound for total delta among reduced (4,4) curves:
\[
\delta=32+r-\sum_i g_i\le48,
\]
since \(r\le16\). This comparison allows all proper pairs, without retaining the fixed quartic.

### Four plane quartics

Keep F a product of four general planes but choose G a general smooth quartic surface. Each plane section is smooth of genus three. Every pair meets at four points, giving twenty-four nodes in total. Thus
\[
33=4\cdot3+24-4+1=12+21.
\]

### Retaining the fixed rational quartic

The reviewed provisional notebook supplies a general member
\[
W=C\cup D,\qquad \deg D=12,\quad g(D)=16,
\quad\operatorname{length}(C\cap D)=18,
\]
with D smooth and eighteen ordinary attachments. The allocation is \((16,17,0)\).

At the promoted prescribed pair
\[
F=x_1^4-x_0^3x_3,\qquad G=x_2^4-x_0x_3^3,
\]
there are four smooth rational quartics, with pairwise contact three at each of two endpoints. Each endpoint has four branches, delta eighteen, and Milnor number thirty-three. Therefore
\[
33=0+36-4+1=0+3+30.
\]
Its ordinary Betti numbers are \((b_0,b_1,b_2)=(1,3,4)\), and its Euler characteristic is two. The two endpoints account for the change \(-64+66=2\) under smoothing. Its delta thirty-six is not maximal, even in the marked-C class: the earlier notebook contains an independently checked eight-rational-component example with delta forty.

## 5. Adjunction gives a constraint on each component

On the normalization of a component of degree e and genus g, with map \(\nu_i:\widetilde C_i\to W\), its conductor divisor \(B_i\) satisfies
\[
\nu_i^*\omega_W=\omega_{\widetilde C_i}(B_i),\qquad
\deg B_i=(a+b-4)e-2g+2.
\]
This concerns reduced Gorenstein curves. For a smooth component in a reduced union, \(B_i\) measures its scheme-theoretic attachment to the rest. In a nodal curve it counts the marked branches of nodes; a self-node contributes twice on its normalized component.

For (4,4), a proposed component of degree e and normalization genus g must carry conductor degree \(4e-2g+2\). In particular, a rational line has six units, a smooth plane quartic has twelve, and a rational quartic has eighteen. These are stronger constraints than the total genus equation alone, though they still do not imply global realizability.

For \(W=C\cup D\) reduced and C smooth of degree e and genus g, put \(s=a+b-4\). The attachment and residual formulas are
\[
\operatorname{length}(C\cap D)=se-2g+2,
\quad\deg D=ab-e,
\quad p_a(D)=g+\frac{s(ab-2e)}2.
\]
They follow from duality on C and the union exact sequence. For the fixed rational quartic in degree (d,d), they specialize to
\[
\deg D=d^2-4,\quad p_a(D)=(d-2)(d^2-8),
\quad\operatorname{length}(C\cap D)=8d-14.
\]
The residual genus is arithmetic; smoothness and irreducibility require separate existence arguments. At d=4 the reviewed notebook supplies those arguments. At other degrees these formulas alone do not supply them.

## 6. Nonreduced limits: an explicit nilpotent calculation

Take independent linear forms L,M and
\[
W=V(L^4,M^4).
\]
This is a proper complete intersection with cycle \(16[V(L,M)]\). A complementary choice of coordinates gives a finite projection to the support line and
\[
\pi_*\mathcal O_W=\bigoplus_{0\le i,j\le3}
\mathcal O_{\mathbf P^1}(-i-j).
\]
Consequently
\[
P_W(n)=\sum_{i,j}(n-i-j+1)=16(n+1)-48=16n-32.
\]
Its reduced topology is a sphere, while the twisted nilpotent layers account for arithmetic genus thirty-three. There are no additional residual components.

Even a pure multiplicity-four degree-four support occurs in characteristic zero: \(V(L^4,G_4)\) has cycle \(4[D]\) when \(D=V(L,G_4)\) is a smooth plane quartic. Its four layers \(\mathcal O_D(-j)\), \(0\le j\le3\), have polynomials \(4n-4j-2\), whose sum is again \(16n-32\).

These examples show that fixed Hilbert polynomial, arithmetic genus, subcanonical duality, and smoothability permit pure multiple cycles, including rational support. The excluded fixed cycle \(4[C]\) needs the actual rational-quartic embedding; its exclusion is the scope of promoted R0022, not a consequence of the general topology budget.

## 7. A sharper marked-curve deduction when a carrier is smooth along C

**Proposed lemma.** Suppose a proper quartic pencil contains C and has a member F smooth at every point of C. If its generic intersection multiplicity along C is at least two, then the pencil contains \(q^2\), where \(q=x_0x_3-x_1x_2\). More precisely,
\[
W=V(F,q^2),\qquad [W]=2[C]+2[C'],
\]
where C' is the residual divisor of type (3,1) to C of type (1,3) on the smooth quadric Q. The divisor C' has no C component. Thus the generic multiplicity of C is exactly two. The residual divisor C' need not be irreducible or reduced for a special F.

**Proof.** The first normal symbols f,g of F,G are sections of \(N^*_{C/\mathbf P^3}(4)\). Generic multiplicity at least two forces their wedge to vanish generically, hence everywhere. Smoothness of F along all of C makes f nowhere zero, so it defines a subbundle \(\mathcal O_C\). The symbol g belongs to this subbundle, giving \(g=\lambda f\) with \(\lambda\in H^0(\mathcal O_C)=k\). Thus
\[
G-\lambda F\in H^0(\mathcal I_C^2(4)).
\]
Here the square is the ideal-sheaf square, so saturation issues are not suppressed. The known elementary quartic calculation gives this space as \(kq^2\): restriction of a twice-vanishing quartic to Q would have residual type (2,-2), so is zero; after division by q, its quadratic factor must be the unique quadric through C. Properness makes \(G-\lambda F\) nonzero. Finally, C' has type (3,1); subtracting C leaves type (2,-2), so C' cannot contain C. This proves the stated cycle and multiplicity.

For an explicit smooth example take the displayed F,G from section 4 and \(S=V(F+G)\). Its partial derivatives show S smooth in characteristic zero. Under Segre coordinates \((x_0,x_1,x_2,x_3)=(ac,ad,bc,bd)\),
\[
(F+G)|_Q=(ad^3-bc^3)(a^3d-b^3c).
\]
Both factors define smooth rational quartics C,C', with ten transverse intersections (the endpoints and eight other points). Hence
\[
V(F+G,q^2)\quad\hbox{has cycle }2C+2C'.
\]
Its reduced support D is the (2,4) curve \(C\cup C'\), of genus nine. On S, W is the double Cartier divisor 2D. The sequence
\[
0\longrightarrow\mathcal O_D(-2)\longrightarrow
\mathcal O_{2D}\longrightarrow\mathcal O_D\longrightarrow0
\]
gives polynomials \((8n-24)+(8n-8)=16n-32\).

There is also an actual flat pencil retaining C between the four-quartic member and this double member:
\[
W_{[u:v]}=V(F+G,\ uF+vq^2).
\]
No nonzero combination \(uF+vq^2\) is a multiple of F+G, so every parameter is a proper complete intersection on S. At [1:0] it is the four-quartic arrangement; at [0:1] it is 2D. No assertion that the other members of this particular pencil have smooth residual curves is needed.

On any smooth quartic carrier the same calculation is compatible with the K3 intersection lattice:
\[
H^2=4,\quad H\cdot C=4,\quad C^2=-2,
\quad C'=2H-C,\quad C\cdot C'=10.
\]
This explains why reduced quartics in a (4,4) arrangement carry eighteen attachment units, while the support quartics in the doubled (2,4) member carry ten. Reduction has changed the adjunction problem.

For general equal degree d and any smooth connected projective marked curve, the first part of the argument still applies: if one carrier is smooth everywhere along C and the multiplicity is at least two, a constant change of the two generators produces a nonzero member of \(H^0(\mathcal I_C^2(d))\). At d=4 its one-dimensionality makes the conclusion especially rigid. In higher degrees this source space grows, and its image on the smooth carrier must be studied rather than assumed to consist of a single square.

## 8. General patterns and the remaining question

For (d,d),
\[
P_W(n)=d^2n-d^2(d-2),\qquad g=1+d^2(d-2).
\]
Products of d general planes on each side yield \(d^2\) lines with \(d^2(d-1)\) nodes, so all genus becomes graph loops. The opposite example \(V(L^d,M^d)\) has cycle \(d^2[L\cap M]\) and layers \(\mathcal O_L(-i-j)\), \(0\le i,j<d\), yielding the same polynomial. For (a,b), the corresponding grid has ab lines and \(a\binom b2+b\binom a2\) nodes, whose graph genus is exactly \(1+ab(a+b-4)/2\).

The most useful classification data therefore consist of component degrees and multiplicities, normalization genera, incidence and branch contacts, componentwise conductor divisors in the reduced case, and nilpotent filtrations in the nonreduced case. Numerical conditions are necessary; an actual pair of global forms remains an additional realization requirement.

For the fixed quartic, the new smooth-carrier dichotomy isolates a precise difficult stratum: multiplicity at least three requires that every pencil member be singular somewhere on C. It does not assert a common singular point for all members, and does not classify that stratum. In higher degrees, studying \(H^0(\mathcal I_C^2(d))\) on a smooth carrier is a concrete continuation of the same question. No unrestricted STCI conclusion or new canonical record is claimed.

## 9. Evidence and review boundary

All new product examples, genus allocations, nilpotent calculations, and the smooth-carrier lemma have elementary proofs above and independent agent reconstruction in the linked audit. No inherited certificate was rerun. External sources were inspected for flat-family coherent Euler characteristic, the delta definition, and the local Milnor formula, at the precise links above; no literature novelty claim is made. The unresolved work is a classification or realization theorem beyond these examples and the stated smooth-carrier stratum.



---

## 44-degeneration-genus-budgets-audit

# Independent audit: (4,4) degeneration and genus budgets

Date: 2026-10-26. Reviewer: independent `genus_topology` agent. Reviewed document: [degeneration and genus budgets](#44-degeneration-genus-budgets). **Outcome: the stated elementary deductions pass independent reconstruction at the scopes below. This is an evidence audit, with no canonical promotion.**

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



---

## normal-torsion-spectral-genus-budget

# Normal-order divisors, torsion, and the complete-intersection genus budget

Date: 2026-10-26. Status: research synthesis and new elementary bridge arguments;
independent audit is recorded in the [companion audit](#normal-torsion-spectral-genus-budget-audit).
No canonical result is promoted. No unrestricted STCI exclusion is claimed.

## 1. Exact question and scope

Let k be algebraically closed, C a smooth connected curve of degree d and
genus g in P3, and Z=V(F_a,G_b) a proper complete intersection. Initially
allow C to be only a marked component of Z_red. The finite normal-filtration
identities below impose the additional hypothesis Z_red=C. The main
specialization assumes generic transverse algebra k(C)[y]/(y^m), m>=2.
The characteristic is arbitrary unless a specific quartic example says otherwise.

There are two genericities: a general parameter of a smoothing, and the
generic point of the special support C. They must be distinguished.
The special scheme Z, including its nilpotents, is a flat limit of smooth
complete intersections. Its reduction C alone has a different Hilbert
polynomial unless Z=C. A smoothing with irreducible smooth general fiber
cannot continue to contain this fixed C in every fiber when ab>d.

The proper-pair Koszul resolution gives

    deg Z=ab,  p_a(Z)=1+ab(a+b-4)/2,
    omega_Z=O_Z(a+b-4).

These are stronger together than genus alone. General perturbations of a
proper pair give a smoothing; if the specialized equations acquire a common
surface, their naive zero locus need not be the flat curve limit.
The [earlier genus notebook](#44-degeneration-genus-budgets)
records this distinction. Constancy of coherent Euler characteristic in
proper flat families is [Stacks, Lemma 36.32.2](https://stacks.math.columbia.edu/tag/0B9T).

## 2. The ordinary normal layers give the genus exactly

Put I=I_C, J=I_Z, K=I O_Z, E=I/I^2, and

    A_n=K^n/K^(n+1),  A=direct_sum A_n,
    T_n=tors_C(A_n),  V_n=A_n/T_n,  r_n=rank V_n.

The V_n are vector bundles on the smooth curve. Write tau_n=length T_n.
These constructions require no global retraction Z -> C: the quotients
A_n themselves are O_C-modules. If Z_red=C, K is nilpotent, so additivity
of Euler characteristic and Riemann--Roch give

    P_Z(t)=sum_n {r_n d t + deg V_n + r_n(1-g) + tau_n}.

Consequently, with m=sum r_n the generic transverse length,

    ab=md,
    p_a(Z)=1+m(g-1)-sum_n deg V_n-sum_n tau_n.             (1)

This is an equality, not just a necessary inequality. Riemann--Roch here
is the usual coherent Euler-characteristic formula; see
[Stacks, section 53.5](https://stacks.math.columbia.edu/tag/0B5B).
The finite torsion has positive Euler characteristic and therefore LOWERS
arithmetic genus when the bundle degrees and generic ranks are fixed.
The multiplicity budget fixes ranks; punctual torsion changes the constant
term of the Hilbert polynomial, not its leading coefficient.

## 3. Curvilinear generic algebra: the bundle part is forced

Assume the generic transverse algebra is k(C)[y]/(y^m). Then K^m=0
globally: K^m is a generically zero subsheaf of the pure one-dimensional
sheaf O_Z, and hence must vanish. Thus A_n=0 for n>=m.

The O_C-torsion T=direct_sum T_n is a homogeneous ideal in A. Since A is
generated in degree one, A/T is generated by L=V_1, a line bundle.
For 0<=n<m the multiplication map L^n -> V_n is a surjection of line
bundles and therefore an isomorphism. In particular,

    A/T = O_C direct_sum L direct_sum ... direct_sum L^(m-1)   (2)

as graded algebras, with multiplication truncated at degree m. There are
NO additional multiplication-zero divisors in this particular quotient
grading. Its map E -> L is globally surjective. A rational normal form
does not supply a global basis, but its direction extends by saturation;
the ordinary graded boundary information lies in the T_n.

Let tau=sum tau_n and ell=deg L. Equation (1) becomes

    p_a(Z)=1+m(g-1)-binom(m,2) ell-tau,
    binom(m,2) ell+tau=m(g-1)-ab(a+b-4)/2.                (3)

The first layer is precisely the relative conormal sheaf
N^*_(C/Z)=K/K^2=A_1. Its torsion alone does not give tau: higher A_n can
also have torsion. If R=ker(E -> L), the actual first-symbol image is a
line subsheaf H_1=R(-B_1), where B_1 is effective, and

    T_1=R/R(-B_1).

Thus B_1 is an intrinsic first-order failure divisor. Arbitrary zeros and
poles introduced by a chosen rational frame are not themselves invariants.

For every n define the effective divisor

    B_n=sum_p length_(O_C,p)(T_n,p) [p].

Equivalently Fitt_0(T_n)=O_C(-B_n). This retains the divisor of lengths,
not the entire module structure or its elementary divisors.

There is a direct full-initial-ideal description. Let S_n=Sym^n E and
H_n=ker(S_n -> A_n). If H_n^sat is its saturation in S_n, then

    T_n=H_n^sat/H_n.

Both H_n and H_n^sat are vector bundles of the same rank on C, and B_n
is the divisor of det(H_n) -> det(H_n^sat). Thus there really is an
intrinsic initial-ideal saturation divisor at each normal order, even
when that degree contains more than one relation. This is unrelated to
choosing the initials of only the two original carrier equations.

## 4. Saturate first: the same boundary information appears as divisors

Define P_i to be the saturation of K^i inside O_Z, namely the inverse
image of the maximal zero-dimensional subsheaf of O_Z/K^i. These are
intrinsic ideals; no global O_C-algebra structure on O_Z is assumed.
They are multiplicative, P_0=O_Z, P_1=K, P_m=0, and

    W_i=P_i/P_(i+1)

are line bundles on C. Indeed O_Z/P_(i+1) has no punctual submodule,
and K P_i is contained in P_(i+1), as can be checked generically and
then by saturation. Here W_0=O_C and W_1=L.

Multiplication now gives generically invertible, possibly non-surjective
maps L^i -> W_i. Their divisors define

    W_i=L^i(D_i),  D_i effective,  D_0=D_1=0.             (4)

This is the divisor description suggested in the question. It uses a
different filtration from (2). There is a pointwise equality

    sum_n B_n = sum_i D_i.                              (5)

Thus the ordinary torsion and the saturated divisors are two accounts
of the SAME genus contribution. One must not add both to equation (3).
Individual indices need not match: B_1 may correspond to part of D_2.

Proof of (5). Complete at p and lift a uniformizer on C to obtain
D=k[[t]] inside B=completed O_Z,p. The algebra B is finite free of rank
m over D: t is a parameter and a nonzerodivisor by Cohen--Macaulayness,
and B/tB is finite. Choose y in K lifting a generator of L. Then

    B'=D[y]=D[Y]/(Y^m) is a full-rank sublattice of B.

The inclusion is strict for the normal filtrations:
B' intersect K^n=y^n B'. Indeed after passing to k((t)), coefficients of
1,y,...,y^(n-1) in an element of K^n must vanish. The graded cokernel
in degree n is T_n: y^n maps isomorphically onto V_n, so its image splits
off the torsion locally. Hence length_D(B/B')=sum_n length_D T_n.
Using instead the saturated flag P_i, the diagonal indices of the same
monomial lattice are exactly mult_p D_i. Their sum gives the same index.
This proves (5) as actual divisors, not just as numerical equivalence.

## 5. Complete-intersection duality fixes a top divisor

Let M=Ann_(O_Z)(K). Finite duality for C inside the Gorenstein curve Z gives

    M=Hom_Z(O_C,O_Z)=omega_C tensor O_C(4-a-b).           (6)

It is a line bundle on C. Generically it is the last power K^(m-1), so
purity and saturation identify M=P_(m-1). Also A_(m-1)=K^(m-1) is torsion
free, being a subsheaf of O_Z. Therefore T_(m-1)=0 and there is a
canonical inclusion

    L^(m-1) -> M,
    L^(m-1)=M(-D_soc),  D_soc=D_(m-1).                  (7)

Its degree is

    (m-1) ell=2g-2-d(a+b-4)-deg D_soc.                 (8)

There is also a pointwise constraint stronger than the total genus formula:

    2 sum_n B_n = m D_soc.                              (9)

In particular 2 tau_p=m mult_p D_soc at every p. This is an equality of
integer divisors in every characteristic; it does not divide by 2 in k.
For odd m every coefficient of D_soc is even.

Local proof of (9). Retain D, B, B' from section 4. Since B is a finite
flat complete intersection over D, choose a Frobenius functional lambda
for which (u,v) -> lambda(uv) is a perfect D-pairing. Its restriction to
Ann_B K is an isomorphism with D. To see this, the orthogonal complement
of K is Ann_B K: lambda(uK)=0 implies lambda((uz)v)=0 for every z in K
and v in B, and perfection implies uz=0. Since B/K=D is free, this
orthogonal complement identifies with Hom_D(B/K,D)=D.

If r=mult_p D_soc, lambda(y^(m-1)) has valuation r. In the monomial
basis 1,y,...,y^(m-1) the Gram matrix has zero entries beyond its
antidiagonal because y^m=0. Its determinant is

    +/- lambda(y^(m-1))^m,

of valuation mr. On the other hand the lattice change B' subset B has
index tau_p, and changes a Gram determinant by the square of its basis
determinant. Since the Gram determinant on B is a unit, its valuation
is 2 tau_p. This proves (9).

The standard duality inputs for this local argument are
[finite-map dualizing modules](https://stacks.math.columbia.edu/tag/0BUK)
and the [finite flat Gorenstein criterion](https://stacks.math.columbia.edu/tag/0C14).
The lattice/divisor identity is the argument above, not a theorem
attributed to those references.

Summing (9) and combining with (8) recovers (3), using ab=md. Thus the
socle, torsion and genus accounts are compatible. The pointwise identity
retains information the total Hilbert polynomial forgets. The existing
saturated Gorenstein pairing gives the more refined relations
D_i+D_(m-1-i)=D_soc; these are inherited in the precise quasiprimitive
scope used by [R0022](../results/quartic_44_filtered_exclusion.md), rather
than a newly promoted general theorem here.

## 6. What the spectral sequence adds, and what it does not

Put S=Sym E, H=in_I(J) the FULL initial ideal, Q=H/S_+H, and
D_eq=J/IJ=O_C(-a) direct_sum O_C(-b). Set

    F^n D_eq=((J intersect I^n)+IJ)/IJ,
    G_n=gr_F^n D_eq,
    Delta_n=in_I(IJ)_n/(S_+H)_n.

The reviewed provisional framework establishes the intrinsic exact sequences

    0 -> Delta_n -> Q_n -> G_n -> 0.                    (10)

Locally, filter the Koszul complex on NORMAL PARAMETERS x,y in O_Z.
Its first page and target are

    E_1^(i,n)=Tor_i^S(A,O_C)_n
       => gr_F^n Tor_i^(O_P3)(O_Z,O_C),
    d_r:E_r^(i,n) -> E_r^(i-1,n+r).

The targets in homological degrees 0,1,2 are O_C, D_eq, det D_eq.
The Delta_n are filtered by incoming images from degree two to degree
one. In particular they constrain whether apparent initial generators
can reduce to the two actual equations with the required global twists.
They are not an extra independent genus term in (1) or (3).

The precise reviewed source is the
[October 24 continuation](DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md#delta-singular-locus-continuation),
with its [independent review](DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md#delta-singular-locus-review).
Its canonical promotion and global sheaf/descent gates remain those in
the [reconciliation](../RECONCILIATION_2026-10-24-IDEAL-FILTRATIONS.md).
The local spectral-sequence statement and the intrinsic sheaf comparison
(10) suffice for the distinctions made here. A new global spectral
obstruction must verify its own transition maps and actual equation spaces.

Since the G_n filter D_eq, they satisfy

    sum rank G_n=2,
    sum_n (deg(G_n/tors)+length tors G_n)=-d(a+b).        (11)

This is an equation-module budget, distinct from the structure-sheaf
budget (1). If Delta is generically zero, locally over a DVR,

    length Delta_n=length tors Q_n-length tors G_n.

Torsion in Q_n need not be canceled by a higher differential. Even the
unweighted K-theoretic Euler identity of the entire normal Koszul
spectral sequence is insufficient on its own: lambda_-1(E) and
lambda_-1(D_eq) both vanish in K_0 of a smooth curve. The useful content
retains normal degrees, maps, torsion, and the actual global generators.

## 7. An explicit supported boundary model

For any r>=1, in every characteristic, take

    B=k[[t,x,y]]/(x^2, y^2+t^r x),  K=(x,y).

It is a complete intersection, free over D=k[[t]] on 1,x,y,xy, and
K^4=0. There is no residual curve. Generically x=-t^(-r)y^2 and the
transverse algebra is k((t))[y]/(y^4). The rational change fails at t=0,
just as suggested in the question. Direct calculation gives

    K=D{x,y,xy}, K^2=D{t^r x,xy}, K^3=D{t^r xy},
    H=(t^r X,X^2,XY^2,Y^4),
    A_1=D Y direct_sum D/(t^r) X,
    A_2=D Y^2 direct_sum D/(t^r) XY,
    A_3=D Y^3.

Thus tau_p=2r. Saturation gives

    P_2=D{x,xy}, P_3=D xy,
    D_2=D_3=r[p], D_soc=r[p],

and (9) reads 2(2r)=4r. The ordinary torsion-free grading is just
D[Y]/(Y^4), although multiplication into the saturated second and third
layers vanishes to order r. This explicitly reconciles the two pictures.

Here Q_1=D, Q_2=Q_3=D/(t^r), Q_4=D. In equation frames e_f,e_g,

    F^2 D_eq=D e_f,
    F^3 D_eq=t^r D e_f,
    F^4 D_eq=t^(2r) D e_f,
    F^5 D_eq=0.

Thus every Q_n -> G_n is an isomorphism and Delta=0. This model
generalizes the reviewed r=1 control from the October 24 continuation;
the formulas here follow directly from the displayed free basis.

Finally B/tB=k[x,y]/(x^2,y^2) has length four and Hilbert function (1,2,1).
But (gr_K B) tensor_D k has length six. Relative normal grading does
not commute with restriction to this special fiber. Those two extra
graded lengths are torsion, not a residual component or extra length in
the actual flat fiber. Flatness over D and normal flatness are different.

## 8. The fixed rational quartic and the characteristic distinction

For C=C0, O_C(1)=O_P1(4), g=0. The promoted
[R0020](../results/quartic_conormal_characteristic_jump.md) gives

    E=O(-7)^2 in characteristic different from 2,
    E=O(-8) direct_sum O(-6) in characteristic 2.

The characteristic-two split is the split of the SPECIFIED quadric
conormal extension, not a universal principle eliminating boundary
phenomena. A global quotient direction exists in characteristic zero too:
O(-7)^2 -> O(-6) can be given by [s,t]. The local model of section 7
has trivial ambient conormal and boundary torsion even in characteristic 2.

The known characteristic-two (4,4) equations have the stronger actual
chart descriptions (X,Y^4) and (A,B^4), covering C. They give no boundary
torsion, L=O(-6), and D_soc=0. These are properties of the equations and
their gluing, not splitting alone; see the
[characteristic note](INTRINSIC_44_APPROACHES_AND_CHARACTERISTIC_CONORMAL.md#quartic-characteristic-conormal).

As a diagnostic of (3), a hypothetical characteristic-zero curvilinear
(4,4) thickening would have m=4 and p_a=33, so

    6 ell+tau=-36,  3 ell=-18-deg D_soc.

Since E -> L is surjective, ell>=-7. Effectivity leaves exactly

| ell | total torsion tau | deg D_soc |
| --- | --- | --- |
| -7 | 6 | 3 |
| -6 | 0 | 0 |

These are the already known two numerical types in the accepted
filtered-contact argument. This is a translation into ordinary torsion,
not a new exclusion proof. R0022 excludes their realization by actual
quartic pairs through further contact information. The control 4C on
the smooth quadric has the correct primitive graded algebra and genus
in characteristic zero but is not a (4,4) complete intersection.

## 9. Residual support and continuation

When C is only a component of Z_red, K need not be nilpotent. The finite
sum (1) is then inapplicable to all of Z. If Z=W union R is its decomposition
into the C-primary part W and the remaining curve R, with finite intersection,

    chi(O_Z)=chi(O_W)+chi(O_R)-length(W intersect R),
    deg Z=deg W+deg R.

The C-primary part need not itself be a complete intersection or Gorenstein,
so (6)--(9) require a separate check for W. A vertical degeneration of
the normal cone is not by itself evidence of R.

The next substantive target is to couple (3), (7), (9), and (11) to the
actual maps H^0(I_C(a)), H^0(I_C(b)) and their higher-symbol images for a
chosen degree pair and generic transverse Hilbert type. Surviving
divisor data are necessary data, not global homogeneous equations.
For a generic algebra of embedding dimension two, retain all ranks r_n
and vector bundles V_n in (1); the single-line and socle-divisor formulas
above do not automatically extend to that setting.

## 10. Utility check: what actually becomes finite?

This section assesses the payoff without claiming that the language of
valuations has supplied a new exclusion. In the quasiprimitive setting,
the inherited symmetry D_i+D_(m-1-i)=D_soc already gives
2 sum_i D_i=m D_soc. The pointwise identity (9) is its translation into
ordinary graded torsion using (5). That translation is useful for exact
initial-ideal/module calculations, but does not strengthen the accepted
saturated-duality constraint by itself. Intrinsic lattice language
likewise removes dependence on frames without imposing a new realizability
condition by itself. No case is excluded merely by this reorganization.

There is a concrete finite arithmetic consequence in the primitive
curvilinear branch. Assume characteristic zero, C=C0, Z_red=C, m>=2,
all T_n=0, and proper homogeneous carrier degrees 2<=a<=b. Write
L=O(-q). The conormal quotient E=O(-7)^2 -> L gives q<=7, and
primitive adjunction has negative degree, so q>=1. Equations (7)--(8)
with D_soc=0 give

    m=ab/4,
    q(m-1)=4(a+b)-14,
    (qa-16)(qb-16)=4((q-7)^2+15).                       (12)

This is a factorization of the existing degree budget, not a new
valuation theorem. Its positive right side forces both factors to have
the same sign. They cannot both be negative: since a,b>=2, their product
would be at most (16-2q)^2, which is smaller than the right side by 8q.
Thus positive divisor pairs give an exhaustive finite reduction:

| q | Unordered necessary degree pairs (a,b) |
| --- | --- |
| 1 | (17,220), (18,118), (19,84), (20,67), (22,50), (28,33) |
| 2 | (9,48), (10,28), (12,18), (13,16) |
| 3 | (6,26) |
| 4 | none |
| 5 | (4,7) |
| 6 | (3,8), (4,4) |
| 7 | (3,4) |

There are fifteen numerical rows, and the larger carrier degree is at
most 220 in this branch. These are NOT fifteen unresolved geometric
candidates: some already lie in established excluded scopes, and every
row still needs actual homogeneous equations and higher-neighborhood
compatibility. No novelty claim or comprehensive literature comparison
is made. The exact divisor enumeration is reproducible with

    python3 research/computations/primitive_curvilinear_degree_budget_2026_10_26.py

The formula does not extend this degree bound to nonprimitive cases.
Allowing D_soc with degree delta changes (12) to

    q(m-1)=4(a+b)-14+delta,
    2 tau=m delta.

An effective boundary divisor can absorb the growing discrepancy; a
separate bound on that payment would be necessary for a new exclusion.
The strong one-line formulas also do not cover the generic binary
(2,12) initial algebra in the scoped degree-(6,16) realization lane.
For that setting one must retain the higher-rank layers from (1), and
the promoted [R0016](../results/nonsaturated_first_relation_resultant.md)
already contains a conditional effective resultant budget.

A decisive control is the primitive divisor 4C on the smooth quadric.
In characteristic zero it has L=O(-6), the required degree sixteen,
genus thirty-three, saturated layers, and perfect pairings, but is not
a (4,4) complete intersection. See the inherited
[characteristic note, section 6](INTRINSIC_44_APPROACHES_AND_CHARACTERISTIC_CONORMAL.md#quartic-characteristic-conormal).
This shows exactly why matching the normal algebra and genus does not
settle homogeneous realization. Progress requires an additional bound
or incompatibility involving the actual carrier-section maps, their
minors, and filtered lifting; changing the coordinates used to describe
them does not provide that extra bound.

## Provenance and review boundary

Promoted inputs used: R0020 for the conormal characteristic jump, and
R0022 only to identify the existing scope of the (4,4) exclusion. The
spectral comparison is reviewed provisional evidence, not a promoted
record. The local lattice proofs, divisor equality (5), and pointwise
socle/torsion identity (9) are the elementary bridges derived in this
investigation. The saturated pairing quoted in section 5 is an inherited
source-level premise, not freshly certified here. No novelty claim is made.
No inherited proof or finite computational certificate was rerun.



---

## normal-torsion-spectral-genus-budget-audit

# Independent audit: normal torsion, divisors, and the CI genus budget

Date: 2026-10-26. Reviewer: independent `budget_audit` agent. Status:
independently reconstructed mathematical review of the [companion
synthesis](#2026-10-26-normal-torsion-spectral-genus-budget), not canonical
promotion. No unrestricted STCI theorem, global homogeneous realization,
or literature novelty claim is asserted.

## Scope and review method

The audited setting is an algebraically closed field k of arbitrary
characteristic, a smooth connected projective curve C in P3, and a proper
complete intersection Z=V(F_a,G_b). The finite normal-filtration statements
assume Z_red=C. The line-bundle and socle-divisor specialization additionally
assumes that the transverse algebra at the generic point of C is
k(C)[y]/(y^m), m>=2. Write K=I_C O_Z,
A_n=K^n/K^(n+1), T_n=tors_C A_n, and L=A_1/T_1.

The reviewer independently reconstructed the genus identity, the
torsion-free graded algebra, both local lattice computations, the
Gorenstein socle argument, and the fixed-quartic arithmetic. The review
also tested the necessity of Gorenstein duality using a supported,
Cohen--Macaulay non-Gorenstein algebra. Accepted exclusion proofs and
inherited executable certificates were not rerun. The spectral comparison
is checked against its stated reviewed-provisional scope, without claiming
a fresh global descent theorem.

## 1. Ordinary grading and the sign of the genus contribution

The claim K^m=0 follows from purity: K^m vanishes generically, hence would
be a finite-support subsheaf of the pure one-dimensional sheaf O_Z. Such a
subsheaf is zero. Thus A_n=0 for n>=m; there is no overlooked torsion tail.

The direct sum T of the O_C-torsion modules T_n is an ideal of the graded
algebra A. Since A is generated in degree one, A/T is generated by L.
Every graded piece V_n=A_n/T_n for 0<=n<m is a line bundle. The resulting
surjection L^n -> V_n is an isomorphism of line bundles. This independently
establishes

    A/T = O_C direct_sum L direct_sum ... direct_sum L^(m-1)

with truncated multiplication. Consequently there are no additional
multiplication-zero divisors in this particular quotient grading. The
saturated filtration used later need not be generated in degree one, and
can carry such divisors.

Euler-characteristic additivity and Riemann--Roch give, for
tau=sum_n length T_n and ell=deg L,

    chi(O_Z)=m(1-g)+binom(m,2) ell+tau,
    p_a(Z)=1+m(g-1)-binom(m,2) ell-tau.

The sign in the synthesis is correct: positive punctual torsion lowers
arithmetic genus when C, m, and ell are fixed. The more general formula
using ranks and degrees of V_n also follows without curvilinearity.
These are necessary numerical identities for an actual Z, not
realization criteria.

The first-symbol description H_1=R(-B_1), R=ker(E -> L), is correct:
A_1=E/H_1 and its torsion is R/H_1. For higher normal degrees, the equally
intrinsic description is

    T_n = H_n^sat/H_n,

where H_n^sat is the saturation of H_n inside the vector bundle
S_n=Sym^n E. Indeed H_n^sat/H_n is exactly the torsion of S_n/H_n=A_n.
The effective divisor defined by Fitt_0(T_n) records its lengths, not its
full elementary-divisor or module structure.

## 2. Saturation and the equality of actual divisors

Let P_i be the inverse image of the maximal finite-support submodule of
O_Z/K^i. Equivalently P_i consists of the sections whose generic image
belongs to K_eta^i. Products satisfy P_i P_j subset P_(i+j). Also
K P_i subset P_(i+1), so W_i=P_i/P_(i+1) is an O_C-module. Its injection
into O_Z/P_(i+1), which has no finite-support submodule, makes it
torsion-free. Its generic rank is one, hence it is a line bundle.
P_1=K, P_m=0, and W_1=L. Products of lifts induce canonical maps
L^i -> W_i, defining effective divisors D_i with W_i=L^i(D_i) and
D_0=D_1=0.

Here is an independent local reconstruction of the pointwise identity

    sum_n length(T_n,p) = sum_i mult_p(D_i).

Complete at p. Lift a uniformizer t of C to the ambient regular local
ring, so its completion can be written k[[t,x,y]], and put D=k[[t]],
B=completed O_Z,p. The ring B is finite over D because B/tB is
Artinian and B is complete; t is a parameter and is a nonzerodivisor
by Cohen--Macaulayness. Hence B is D-free of rank m. This local choice
does not impose a global retraction Z -> C.

Choose y in K lifting a local generator of L. It generates the generic
nilpotent ideal, and y^m=0. The algebra B'=D[y] is a full sublattice of B,
free on 1,y,...,y^(m-1). The inclusion is strict for the K-filtration:

    B' intersect K^i B = D{y^i,...,y^(m-1)}.

To prove this, invert t. A polynomial in the displayed monomial basis
belongs to K_eta^i only if all coefficients of lower powers vanish;
those coefficients already vanish in D. The map from D y^i to A_i
projects isomorphically onto V_i=L^i. Its cokernel is T_i, so

    length_D(B/B')=sum_i length_D T_i.

Using instead the saturated flag P_i, the same monomial lattice has
diagonal indices mult_p D_i. Thus its index is also sum_i mult_p D_i.
This proves equality of effective divisors, rather than merely equality
of degree or linear equivalence. It also explains why individual degree
indices need not coincide in the ordinary and saturated descriptions.

## 3. Gorenstein duality and the stronger pointwise identity

Finite duality for C inside the Gorenstein curve Z gives

    M=Ann_(O_Z) K=Hom_Z(O_C,O_Z)
      =omega_C tensor O_C(4-a-b).

The ideal M is saturated: a finite-support obstruction to an element
annihilating K would be a finite-support submodule of O_Z and hence zero.
Its generic fibre is K_eta^(m-1), so M=P_(m-1). Moreover K^(m-1) is
torsion-free as a subsheaf of O_Z and is the last ordinary layer. It is
therefore isomorphic to L^(m-1). Its inclusion in M defines

    L^(m-1)=M(-D_soc),  D_soc=D_(m-1).

For the claimed pointwise identity, retain B, D, B' above. Since B is
finite flat Gorenstein over D, choose lambda:B -> D giving a perfect
Frobenius pairing lambda(uv). The orthogonal complement of K is Ann_B K:
orthogonality implies lambda((uz)v)=0 for z in K and every v in B,
and perfection forces uz=0. Perfect duality identifies this complement
with Hom_D(B/K,D)=D, and restriction of lambda to Ann_B K is an
isomorphism. In particular lambda takes a generator of Ann_B K to a
unit.

Write r=mult_p D_soc. Then ord_t lambda(y^(m-1))=r. The Gram matrix on
the basis 1,y,...,y^(m-1) of B' has zero entries beyond the antidiagonal,
because y^m=0. Its determinant is

    +/- lambda(y^(m-1))^m.

Its valuation is mr. On the other hand, if P is the lattice-change
matrix from B' to a D-basis of B, its determinant valuation is the
index length_D(B/B'). The Gram matrix transforms by P^T G_B P; G_B has
unit determinant. Its valuation is therefore twice that index. This proves

    2 sum_n length(T_n,p)=m mult_p D_soc

at every p, in arbitrary characteristic. No division by two in k is used.
For odd m, the coefficients of D_soc are even. Combining this local
identity with adjunction recovers the genus identity, using ab=m deg C.

As a consistency check, the saturated flag also has
Ann_B P_i=P_(m-i). Under lambda it is a self-dual saturated lattice flag,
so the induced rank-one quotient pairings W_i W_(m-1-i) -> M are perfect.
The corresponding product sections give
D_i+D_(m-1-i)=D_soc. The synthesis conservatively labels the pairing it
uses as inherited source-level evidence in the quasiprimitive scope of
R0022; no promotion of a new general pairing theorem is needed here.

## 4. A scope countercheck: Cohen--Macaulayness alone is insufficient

Take D=k[[t]], r>=1, and

    B=D[x,z]/(x^2-t^r z, xz, z^2).

This algebra is D-free on 1,x,z and has sole reduced support C. Its
generic algebra is k((t))[x]/(x^3), and it is Cohen--Macaulay. At the
closed fibre it is k[x,z]/(x,z)^2, so it is not Gorenstein. With
K=(x,z),

    K^2=t^r D z, K^3=0,
    T_1=D/(t^r), T_2=0,
    Ann_B K=D z.

The top ordinary power has index r in Ann_B K. Thus tau_p=r and the
top divisor has multiplicity r, but 2 tau_p=2r differs from 3r. This
does not contradict the synthesis, which assumes a complete intersection.
It verifies that the Frobenius/Gorenstein hypothesis in the strong local
budget is substantive. The ordinary grading and saturated-index identity
continue to hold in this countercheck.

## 5. Local boundary control, spectral comparison, and characteristic

For the supported complete-intersection model

    B=D[[x,y]]/(x^2, y^2+t^r x),

the free basis 1,x,y,xy gives
K=D{x,y,xy}, K^2=D{t^r x,xy}, K^3=D{t^r xy}, K^4=0.
The ordinary torsion lengths are r in degrees one and two, and zero in
degree three. Saturation gives D_2=D_3=D_soc=r[p]. Thus both divisor
identities agree pointwise: sum B_n=2r[p]=D_2+D_3, and
2 sum B_n=4r[p]. The full relative initial ideal and equation filtration
displayed in the synthesis agree with these bases.

This model has Delta=0 despite its nonzero normal-layer torsion. The
spectral comparison measures initial-equation generators lost on passage
to the filtered two-equation module; it is not the total torsion of the
structure-sheaf grading. Adding a separate Delta term to the genus
formula would therefore be unjustified. The targets O_C, D_eq, det D_eq
and the exact equation-module degree budget in the synthesis are
consistent with the actual CI Koszul resolution. The reviewed
provisional status and remaining global spectral descent gates are
explicitly preserved.

For the fixed rational quartic, promoted R0020 supplies E=O(-7)^2 in
characteristic different from two. The quotient E -> L gives ell>=-7.
For a hypothetical sole-support curvilinear (4,4) intersection, the
genus and adjunction equations give

    6 ell+tau=-36,  3 ell=-18-deg D_soc.

Effectivity leaves (ell,tau,deg D_soc)=(-7,6,3) or (-6,0,0), exactly
the inherited two numerical types. This does not show existence of
either type as a quartic pair; R0022 already excludes their actual
quartic realization using further contact information.

The distinction between splitting of the specified quadric conormal
extension and existence of a global quotient line is correct. The local
boundary model works in characteristic two with trivial ambient
conormal. Splitting alone cannot eliminate the boundary. The known
characteristic-two pair has stronger actual chart forms (X,Y^4) and
(A,B^4), which explain its absence of boundary torsion.

## Outcome and limitations

**Outcome: PASS for the stated mathematical synthesis.** No substantive
correction to the inspected source text is required. The proposed
degreewise saturation description T_n=H_n^sat/H_n is correct and is
verified in section 1 above. The new local lattice bridge and pointwise
socle/torsion identity have been independently reconstructed; they remain
reviewed research evidence, not ID-bearing canonical results.

The audit does not certify a global pair, a new exclusion, a new global
spectral-sequence descent construction, or any general statement with
residual components. If C is only a marked component, K can fail to be
nilpotent and the finite genus sum cannot be applied to all of Z. A
C-primary component can fail to be Gorenstein even when Z is a complete
intersection, so its socle-duality budget requires separate hypotheses.
For generic embedding dimension two, the full ranks and vector-bundle
degrees remain necessary; the single-line argument does not apply.

No executable replay was necessary for the lattice proofs, and no
inherited proof or certificate was rerun merely to reorganize evidence.

## Addendum: independent utility and primitive-degree audit

Date: 2026-10-26. Reviewer: independent `utility_audit` agent. The reviewer
read section 10 of the synthesis and the new standard-library script
`research/computations/primitive_curvilinear_degree_budget_2026_10_26.py`,
independently reconstructed the arithmetic, and ran that script. This is
a review of the new arithmetic check, not a replay of inherited proofs.

In the stated characteristic-zero, fixed-quartic, sole-support primitive
curvilinear setting, E=O(-7)^2 surjecting onto L=O(-q) gives q<=7.
With m=ab/4>=2 and a,b>=2, primitive adjunction gives

    q(m-1)=4(a+b)-14>0,

so q>=1. Expanding and rearranging yields exactly

    (qa-16)(qb-16)=4((q-7)^2+15).

The positivity argument is complete. The right side is positive, so the
two factors have the same sign and neither is zero. If both were
negative, a,b>=2 implies their product is at most (16-2q)^2; the claimed
right side exceeds that bound by 8q>0. Therefore both factors are
positive, and positive divisor pairs exhaust all possible a<=b. The
script enumerates those divisors only up to the exact integer square
root, checks the necessary congruences, requires 4 to divide ab, and
checks the original adjunction equality on every retained row. Thus its
completeness is supplied by the factor proof, not an arbitrary degree
cutoff.

The fresh run reports fifteen rows and maximum larger degree 220. Its
rows agree with the source table, including (17,220), which a bounded
search below degree 200 would miss. The q=4 factor possibilities fail
the integrality requirement on m. No arithmetic discrepancy was found.

The nonprimitive sign is correct: an effective socle divisor of degree
delta changes adjunction to

    q(m-1)=4(a+b)-14+delta,  2 tau=m delta.

Equivalently the factor product would equal the old target plus
4q delta. Since this audit supplies no uniform bound on delta, the
primitive degree bound does not extend to that branch. It also does
not apply to generic embedding dimension two or to a marked component
with residual support.

The utility assessment is accurate. In the inherited quasiprimitive
scope, summing the saturated Gorenstein symmetry already gives
2 sum_i D_i=m D_soc. Translating this into ordinary torsion uses the
newly explicit equality sum B_n=sum D_i, but introduces no stronger
duality constraint. The primitive factorization follows the existing
genus/adjunction/conormal data; it is not an extra exclusion obtained
from the valuation parameter space. The source correctly labels all
fifteen entries necessary numerical rows, rather than fifteen unresolved
or realized geometric cases, and preserves the actual homogeneous
realization gap and the primitive 4C-on-a-quadric control.

**Addendum outcome: PASS.** The finite arithmetic reduction and its
limited utility are correctly stated. No canonical result is promoted,
and no comprehensive novelty or literature audit is asserted.

