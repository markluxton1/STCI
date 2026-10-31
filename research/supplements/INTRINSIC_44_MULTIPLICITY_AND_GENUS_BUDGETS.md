# INTRINSIC 44 MULTIPLICITY AND GENUS BUDGETS

## Cross-supplement synthesis: distinct (4,4) obstruction routes (editorial, not a new audit)

The historical material contains several arguments with different inputs and different logical targets. They should not be conflated:

| Route | Retained location | What it supplies | Limitation |
| --- | --- | --- | --- |
| Filtered quartic-contact calculation | [Filtered proposal and independent audit](IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-quartic-44-filtered-proof-proposalmd) | A classification- and calculation-dependent route through the two saturated numerical types and actual cubic-contact constraints | Its computational exhaustiveness and inherited hypotheses remain attached to the original audit; this synopsis is not an independent rerun |
| First-symbol pencil and surface singularities | [Intrinsic K3 proposal](../synthesis/quartic_pair_obstruction.md#4-direct-blowups-and-the-global-contradiction) and [audit](../synthesis/quartic_pair_obstruction.md#4-direct-blowups-and-the-global-contradiction) | A different route from the defect algebra and first-symbol divisor to moving singularities and an exceptional-rank contradiction | Characteristic-zero and K3-specific; preserve as historical reviewed evidence, not a newly promoted result |
| Explicit local multiplication and defect types | [Intrinsic quadruple local algebra](../synthesis/quartic_pair_obstruction.md) | The local normal form and identification of the fixed divisor, with coefficient-function qualifications | Local algebra does not by itself prove global realizability or a global STCI exclusion |
| Genus and torsion budgets | [Degeneration genus budgets](#44-degeneration-genus-budgets) and [normal torsion spectral budget](CURVILINEAR_GENUS_AND_DEFECTS.md#normal-torsion-spectral-genus-budget) | Numerical bookkeeping, boundary divisors, and explicit reduced/nonreduced comparison examples | Necessary conditions and examples are not sufficient to exclude all pairs |

**Shared starting point.** The fixed quartic curve, its conormal bundle and the generic transverse length-four hypothesis belong to the common setup. The filtered and surface-singularity arguments then diverge: one analyzes actual quartic lifting/contact spaces; the other counts singularities of a general pencil member. The genus-budget work instead studies what numerical restrictions survive under degeneration. The local-algebra source is a bridge between the two obstruction routes, not a replacement for either global step.

**Preservation rule.** Keep the explicit triple-multiplicity plus residual-quartic examples in [the multiplicity-three construction](#44-multiplicity-three-forces), the negative control where quadric restrictions fail to determine normal multiplicity in [the proof-routes discussion](#44-intrinsic-proof-routes), and the nonreduced degeneration examples in [the genus-budget section](#44-degeneration-genus-budgets). These prevent the stronger-looking arguments from being incorrectly extended to lower generic multiplicity, arbitrary residual support, or higher degrees. The source audits and their epistemic qualifications remain authoritative for their own claims.

---


Permanent subject consolidation. All source mathematical detail retained with its original conditional and audited status; no new theorem promotion.


---

## 44-intrinsic-proof-routes

[Complete proof routes and negative controls](../synthesis/quartic_pair_obstruction.md), including the [completed embedded fourth-extension proof](../synthesis/intrinsic_fourth_extension.md).

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

The elementary identity \(H^0(\mathcal I_C^2(4))=kq^2\), for \(q=x_0x_3-x_1x_2\), and the new [smooth-carrier lemma](#44-degeneration-genus-budgets) are already independently reviewed. The displayed conjugate pencils below are inherited accepted source-level evidence from [October 7, section 4](OCT7_MF6_AND_NONNORMAL_STRUCTURES.md#source-2026-10-07-session-mf6-e1-independent-auditmd) and [the October 23 filtered proof](IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-quartic-44-filtered-proof-proposalmd). Their residual factorization and geometric interpretation are the new calculation here. No exhaustiveness assertion from the multiplicity-four classification is transferred to arbitrary multiplicity-three pairs.

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

The exact factorization and chart checks are reproducible with the standard-library [verifier](../computations/verify_44_triple_residual_example_2026_10_26.py). These finite identities are distinct from the global purity and properness proof above. No inherited certificate is rerun.

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

The [complete rank-four surface proof](../synthesis/quartic_pair_obstruction.md#1-a-common-numerical-reduction) excludes multiplicity four without R-0001 or R-0022 as inputs. Thus it supplies an independent proof of the maximum-multiplicity assertion here. The all-members-integral assertion for arbitrary multiplicity-three pencils in section 3 retains its separate R-0001 dependency.

## 44-intrinsic-proof-routes-audit

[Reviewed mathematical replacement: direct blowups, controls and contact geometry](../synthesis/quartic_pair_obstruction.md).

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

Promoted inputs are [R0021](../results/quartic_mu4_degeneration.md), for the prescribed four-quartic configuration, and the precise scope of [R0022](../results/quartic_44_filtered_exclusion.md), for the already established fixed-curve (4,4) exclusion. Neither exclusion proof is rerun. The [previous cycle notebook](../synthesis/root_pencil_geometry.md) and [conductor/topology note](../synthesis/root_pencil_geometry.md), with their linked audits, supply reviewed but unpromoted geometry. The smooth-carrier dichotomy in section 7 is a new elementary deduction, independently reconstructed during this move.

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
The reviewer read the research index, the reviewed note, promoted records [R0021](../results/quartic_mu4_degeneration.md) and [R0022](../results/quartic_44_filtered_exclusion.md), and the relevant [conductor/topology evidence](../synthesis/root_pencil_geometry.md). The prescribed four-quartic decomposition and the fixed-curve exclusion were retained at their recorded scope; their inherited proofs and certificates were not rerun. The earlier generic smooth residual and eight-component competitor remain reviewed, unpromoted inputs with the provenance stated in the main note.

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
