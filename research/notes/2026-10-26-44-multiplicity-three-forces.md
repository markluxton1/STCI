# What multiplicity at least three forces in a (4,4) intersection

Date: 2026-10-26. Status: new deductions and explicit residual calculation, independently reviewed in the [audit](2026-10-26-44-multiplicity-three-forces-audit.md); no canonical promotion.

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

The elementary identity \(H^0(\mathcal I_C^2(4))=kq^2\), for \(q=x_0x_3-x_1x_2\), and the new [smooth-carrier lemma](2026-10-26-44-degeneration-genus-budgets.md) are already independently reviewed. The displayed conjugate pencils below are inherited accepted source-level evidence from [October 7, section 4](2026-10-07-session-mf6-e1-independent-audit.md) and [the October 23 filtered proof](2026-10-23-quartic-44-filtered-proof-proposal.md). Their residual factorization and geometric interpretation are the new calculation here. No exhaustiveness assertion from the multiplicity-four classification is transferred to arbitrary multiplicity-three pairs.

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

The use of R0022 in section 2 can be replaced by the existing, independently audited [October 23 K3 proof](2026-10-23-intrinsic-44-k3-proof-proposal.md), with its [independent audit](2026-10-23-intrinsic-44-k3-independent-audit.md) and [rank-four local algebra](2026-10-23-intrinsic-quadruple-local-algebra.md). That proof is explanatory evidence, not a promoted canonical result. It is the multiplicity-four analogue of the moving-A2 argument above and uses neither R0001 nor R0022.

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
