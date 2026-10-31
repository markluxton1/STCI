# Independent audit: two affine endpoints and actual gluing

Date: 2026-10-30. Reviewer: independent affine-endpoints audit agent. Source: [Two affine endpoints](2026-10-30-four-streams-affine-endpoints.md), sections 1–4, including equations (1)–(3). **Outcome: the displayed deductions pass independent hand reconstruction under their stated hypotheses.** They remain reviewed provisional deductions, with no canonical promotion and no characteristic-zero STCI resolution. No material correction to the mathematical claims is required.

## 1. Actual two-chart identities and the missing line

The hypotheses are the fixed smooth quartic over algebraically closed \(k\), positive twists \(a,b\), polynomial pairs on the *entire* affine charts, the stated reduced zero sets, and literal section identities on the *entire ambient overlap*. For twist \(d\), the substitution sends the exponent triple \((i,j,k)\) to \((i,j,d-i-j-k)\). This map is injective, so negative \(A\)-exponents cannot cancel. Polynomiality is exactly total degree at most \(d\), and gives a unique homogeneous extension. This proof imposes no upper degree bound and makes no assumption on generic transverse multiplicity.

A common surface component of the extensions would meet \(U=\mathbf P^3\setminus M\), contradicting the chart supports. The resulting regular sequence defines a pure Cohen–Macaulay projective curve. Its Koszul resolution gives \(H^1(\mathcal I_Y)=0\), using \(H^1(\mathcal O(n))=H^2(\mathcal O(n))=0\) on \(\mathbf P^3\); hence \(H^0(\mathcal O_Y)=k\). Any extra curve component would be contained in \(M\), disjoint from \(C\), and disconnect \(Y\). Purity excludes separate zero-dimensional components. This proves the criterion, including nonreduced structures. The conditional split-bundle variant is valid only after an actual isomorphism with the specified ambient split twists is supplied; the note does not assume such splitting.

## 2. One endpoint for every chosen affine radical pair

For any \(f,g\) with the stated radical, no affine hypersurface can divide both. An ordinary homogenization has no \(x_0\) factor; any other common homogeneous factor would dehomogenize to a forbidden common factor. Thus the pair defines a proper CI. All residual curves lie in \(H_\infty\). Connectedness forces their *union* to meet \(C\), and \(C\cap H_\infty=\{p_\infty\}\); consequently at least one residual curve passes through this endpoint whenever any residual exists. It is neither needed nor true that every residual component meets \(C\) directly.

Write \(A=\mathcal O_{\mathbf P^3,p_\infty}\), \(J=(F,G)A\), and \(I=I_{C,p_\infty}\). Since \(J\subset I\), containment \(I^N\widehat A\subset J\widehat A\) contracts to \(I^N\subset J\) by faithful flatness. It excludes every residual prime through the endpoint. Conversely sole support gives \(\sqrt J=I\) and hence such a finite power by Noetherianity. No passage from formal topological support to power containment is being assumed.

Here \(e_{p_\infty}(Y)\) means **Hilbert–Samuel multiplicity**, not the length of the unsliced local ring. Associativity gives exactly

\[
e_{p_\infty}(Y)=m+\sum_{D\ne C,\ p_\infty\in D}m_D e_{p_\infty}(D),
\]

because \(C\) is smooth and has point multiplicity one. All summands are positive, and the preceding connectedness argument makes the sum nonempty precisely when there is residual support anywhere. Thus all three conditions are equivalent. Over the infinite field \(k\), a sufficiently general local linear form is a reduction of the maximal ideal; the Cohen–Macaulay curve quotient then has slice length equal to this multiplicity. An arbitrary special slice need not compute it.

This test covers arbitrary affine radical pairs, arbitrary degrees, and higher multiplicities. It supplies neither a universal strict inequality nor an example attaining equality. A projective STCI pair cannot have an \(x_0\) factor, since its intersection with \(x_0=0\) would then contain a plane curve. Thus dehomogenizing a successful projective pair would be covered by ordinary homogenization here; the endpoint formulation does not omit that possibility.

## 3. Whole-overlap determinant, alternate generators, and nonlinear terms

Direct expansion verifies the displayed cubic identity and matrix (2), whose determinant is \(-y^2D^{-5}\). On \(C\cap U_0\cap U_\infty\), the coordinate \(t\) gives determinant \(-t^{-14}\). Any matrix relating these pairs induces the unique change between their conormal bases, so its determinant must have this same restriction. The overlap ring is exactly \(R=k[z,y,D,D^{-1}]\), with \(R^*=k^*D^{\mathbf Z}\); restricted units have exponents divisible by four. Since \(-14\notin4\mathbf Z\), no matrix in \(GL_2(R)\) can perform the change. This argument remains valid in characteristic two.

Replacing either pair by any two generators of the same reduced affine ideal does not evade the test: their conormal images are bases over \(k[t]\), or \(k[t^{-1}]\), respectively, and each basis-change determinant is a nonzero constant. The restricted exponent cannot change. In contrast, localizing near \(C\) makes \(y\) invertible and makes the displayed matrix invertible. Thus this is an obstruction on the *entire ambient overlap*, not a failure of local regular embedding. Geometrically it is the normal determinant of degree 14, equivalently the conormal determinant of degree -14; it excludes reduced presentations, not arbitrary thicker CI schemes.

I independently substituted \(A=1/D\), \(B=z/D\), \(W=(z^3+v)/D\) into \(u'=A-W^4\), \(v'=B-W^3\). Both formulas (3) follow exactly. The denominator \(D=z^4+u\) is invertible on this overlap. Replacing it by \(z^4\), or retaining only first-order normal terms, loses actual ambient transition data.

## 4. Valuations, inherited authority, and literal clarifications

The degree valuation is \(\operatorname{ord}_{H_\infty}\) on \(k(\mathbf P^3)\), centered at the generic point of the boundary plane. It is **not** a valuation centered at the closed endpoint \(p_\infty\), nor the curve valuation \(\operatorname{ord}_{p_\infty}\) on \(k(C)\). Its values \(-1,-3,-4\) on \(z,v,u\) follow from unequal-order subtraction. The exact sums \(z^3+v=y\), \(z^4+u=D\) have value \(-1\); a monomial valuation defined by those three weights would instead give \(-3,-4\). The warning that weights alone omit residue cancellation is therefore correct.

The all-degree boundary mechanism and the impossibility of a successful *reduced* affine generating pair are inherited from [P-007](../RESEARCH_RECORD.md#p-007-an-exact-affine-to-projective-boundary-criterion). The global fixed-twist formal-pair implication and connectedness/multiplicity detector are already recorded in [October 27, sections 2 and 5–6](2026-10-27-formal-neighborhood-residual-visibility.md) and its [independent audit](2026-10-27-formal-residual-visibility-audit.md). The present note correctly offers an explicit chart specialization and endpoint recognition test, not a new algebraization theorem. Generic normal forms, finite jets, or scalar valuations still do not supply the required global sections and power containment.

Primary citations were opened during this audit: [Stacks 01XS, Lemma 30.8.1](https://stacks.math.columbia.edu/tag/01XS) supplies the stated cohomology vanishings; [Stacks 02QG, Lemma 42.3.2](https://stacks.math.columbia.edu/tag/02QG) supplies the one-dimensional Cohen–Macaulay componentwise slice-length formula. The latter is a slice-length foundation, exactly as cited; it should not be described as a theorem that every linear slice computes Hilbert–Samuel multiplicity.

Literal clarifications: spelling out “Hilbert–Samuel” and “generic point of \(H_\infty\)” would help prevent the two confusions above, but does not change the claims. The requested typo \(I_C^{,N}\) does **not** occur in the reviewed source; its displayed endpoint expression already reads \(I_{C,p_\infty}^{N}\). If that malformed expression occurs in a companion rendering, replace it by \(I_C^N\), with the appropriate stalk/completion indicated.

No synthetic computations, inherited certificate reruns, canonical edits, navigation edits, or Git operations were performed. The geometric gain is an exact location for the remaining construction/exclusion problem: actual compatible twisted equations, or the full endpoint ideal and its multiplicity. Neither side of the unrestricted characteristic-zero question is decided.
