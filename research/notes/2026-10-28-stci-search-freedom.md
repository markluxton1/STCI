# Actual equation freedom and the contact locus to search

Investigation begun October 28 and completed October 29, 2026. Status: independently reviewed provisional deduction; no canonical promotion. The independent reconstruction is [the dimension audit](2026-10-28-stci-search-freedom-independent-audit.md). This note answers the question of how much freedom remains after requiring an equation to vanish to a specified normal order, and what that says about a search for STCI equations.

The curve throughout is
\[
C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k.
\]
The search consequences and balanced symbol targets below are over an algebraically closed field of characteristic zero. The sheaf-power dimension calculation itself works in every characteristic. Write \(\mathcal I=\mathcal I_C\), \(Q=x_0x_3-x_1x_2\), and
\[
V_{d,m}=H^0(\mathbf P^3,\mathcal I^m(d)),\qquad
A_m(d)=\dim_k V_{d,m}.
\]
These are actual global homogeneous equation spaces. The power is the **ideal sheaf power**, or equivalently the homogeneous saturation of the ordinary ideal power. Since \(C\) is smooth and regularly embedded, it also expresses normal vanishing order at least \(m\); no equality with the unsaturated homogeneous power is assumed. An equation's normal order \(m\) and a pair's generic intersection length \(M\) are different quantities.

The useful answer is precise: below degree \(3m\), the remaining freedom has a forced quadric factor; starting at degree \(3m\), integral equations become possible, and by degree \(3m+2\) every abstract leading normal symbol lifts to an actual global equation. A hypothetical STCI must nevertheless lie in the locus of shared leading roots and excess contact. Generic choices from these large equation spaces leave residual curves.

## Accepted inputs and new scope

The accepted [STCI-R-0020](../results/quartic_conormal_characteristic_jump.md) gives
\(E=\mathcal I/\mathcal I^2\simeq\mathcal O_{\mathbf P^1}(-7)^{\oplus2}\)
in characteristic zero. The accepted [STCI-R-0001](../results/quartic_carrier_exclusion.md), with its stated lower-degree/factor reduction, says that a hypothetical characteristic-zero STCI can be sought with integral equations of degrees at least five. These results are used as premises, without rerunning their proofs.

The new calculation concerns all global spaces \(V_{d,m}\), their first nonzero normal symbols, and a necessary generic contact condition. It neither constructs a supported pair nor excludes the higher-contact locus. In particular, counting parameters in \(V_{a,r}\times V_{b,s}\) does not establish the codimension, independence, or consistency of the nonlinear STCI conditions.

## Exact global freedom

Set
\[
D(u)=\frac{5u^3+15u^2+16u+6}{6}\qquad(u\ge0).
\]
For every integer \(m\ge1\) and \(d\ge0\),
\[
A_m(d)=
\begin{cases}
0,&d<2m,\\[2mm]
D(d-2m),&2m\le d\le3m,\\[2mm]
\displaystyle\binom{d+3}{3}
-\frac{m(m+1)(4d+1)}2
+\frac{7m(m^2-1)}3,&d\ge3m.
\end{cases} \tag{1}
\]
The two formulas at \(d=3m\) agree. The final polynomial already holds at \(d=3m-1\).

There is more information than the dimension alone. For \(2m\le d\le3m\),
\[
V_{d,m}=Q^{\,3m-d}
V_{3(d-2m),\,d-2m}. \tag{2}
\]
Thus every section has the displayed fixed quadric factor. For example,
\(V_{2m,m}=kQ^m\), and at \(d=2m+2\) the space has dimension 23 for every \(m\ge2\), but consists of \(Q^{m-2}\) times the degree-six, order-two space. This apparent freedom cannot be used as an integral degree-\(2m+2\) carrier when \(m>2\).

Here is the geometric reason. The smooth quadric \(Q\simeq\mathbf P^1\times\mathbf P^1\) contains \(C\) as a Cartier divisor of class \((1,3)\), up to swapping the rulings. The local regular-sequence identity
\((Q)\cap\mathcal I^m=Q\mathcal I^{m-1}\)
gives the flag sequence
\[
0\longrightarrow\mathcal I^{m-1}(d-2)
\xrightarrow{Q}\mathcal I^m(d)
\longrightarrow\mathcal O_Q(d-m,d-3m)\longrightarrow0. \tag{3}
\]
If \(d<3m\), the right-hand term has no sections, proving the forced factor and its iteration. Induction in (3) gives
\(H^1(\mathcal I^m(d))=0\) for \(d\ge3m-1\).
In the range \(d\ge3m\), taking sections yields
\[
A_m(d)=A_{m-1}(d-2)+(d-m+1)(d-3m+1),
\]
which sums to (1). This proves the all-degree formula; finite computations below only check its implementation and boundary values.

## Asymptotic interpretation

For fixed \(m\) and \(d\to\infty\), the number of independent linear conditions is exactly
\[
\operatorname{codim}V_{d,m}
=\frac{m(m+1)(4d+1)}2-\frac{7m(m^2-1)}3
\qquad(d\ge3m-1). \tag{4}
\]
It grows linearly in \(d\), while the ambient form space grows cubically. Vanishing to a fixed normal order therefore becomes inexpensive in large degree.

The more relevant scaling for high multiplicity is \(m/d\to\theta\). For \(0\le\theta\le1/3\),
\[
\frac{A_m(d)}{\binom{d+3}{3}}
\longrightarrow 1-12\theta^2+14\theta^3. \tag{5}
\]
At the boundary \(d=3m\), the limiting fraction is \(5/27\), so the global equation space is still large: \(A_m(3m)\sim5m^3/6\). For \(1/3\le\theta\le1/2\), the fraction is instead
\(5(1-2\theta)^3\), but this entire region has the forced quadric factor in (2). Above \(\theta=1/2\), there are no sections. These are dimensions of equation spaces, not expected dimensions of a STCI locus.

## Actual leading symbols: a small degree margin removes the first obstruction

For an equation of exact order \(r\), its leading normal symbol lies in
\[
H^0(C,\operatorname{Sym}^rE\otimes\mathcal O_C(d))
=H^0\bigl(\mathbf P^1,\mathcal O(4d-7r)\bigr)^{\oplus(r+1)}.
\]
Its actual source image has dimension
\[
\dim\operatorname{im}\sigma_{d,r}=A_r(d)-A_{r+1}(d), \tag{6}
\]
because the kernel is exactly \(V_{d,r+1}\). At the first degrees without a forced quadric factor, the comparison is

| Degree | Actual symbol image dimension | Full symbol target dimension | Codimension |
|---|---:|---:|---:|
| \(d=3r\) | \(5r^2+2\) | \((r+1)(5r+1)\) | \(6r-1\) |
| \(d=3r+1\) | \(5r^2+8r+4\) | \(5(r+1)^2\) | \(2r+1\) |
| \(d\ge3r+2\) | \((r+1)(4d-7r+1)\) | same | 0 |

The last row follows from \(H^1(\mathcal I^{r+1}(d))=0\). It is a surjectivity statement for the first nonzero normal symbol, and does not say that an arbitrary compatible tower of higher symbols comes from a pair of the required fixed degrees.

The small exact examples are useful controls:

| \((d,r)\) | Equation space \(A_r(d)\) | Symbol image | Full target |
|---|---:|---:|---:|
| \((3,1)\) | 7 | 7 | 12 |
| \((4,1)\) | 18 | 17 | 20 |
| \((5,1)\) | 35 | 28 | 28 |
| \((6,2)\) | 23 | 22 | 33 |
| \((7,2)\) | 47 | 40 | 45 |
| \((8,2)\) | 80 | 57 | 57 |
| \((9,3)\) | 54 | 47 | 64 |
| \((10,3)\) | 96 | 73 | 80 |
| \((11,3)\) | 150 | 96 | 96 |

The degree-three and degree-four rows are controls of the source spaces, not reopened STCI cases. At degree \(3r\), most equation freedom lies in higher-order terms: the equation space has cubic growth in \(r\), while its symbol image has quadratic growth. A search should keep these higher terms as adjustable contact data after selecting the leading root pattern.

## What a STCI candidate must do with this freedom

Suppose an actual proper pair \((F_a,G_b)\) has generic normal orders \(r,s\). At the generic point of \(C\), the transverse ambient local ring is regular of dimension two over \(k(C)\). If the two initial binary forms are coprime, their local intersection length is exactly \(rs\). A complete intersection with sole reduced support \(C\) would instead need length
\[
M=ab/4. \tag{7}
\]

For the integral degree-at-least-five representatives supplied by the accepted low-degree/factor reduction, (2) forces
\[
r\le a/3,\qquad s\le b/3.
\]
Consequently a coprime-leading-symbol pair has
\[
M=rs\le ab/9,
\qquad
\deg R=ab-4M\ge5ab/9. \tag{8}
\]
The lower bound in (8) is conditional on coprime leading symbols. It is **not** a residual lower bound on arbitrary pairs: shared leading roots can raise the local intersection length above \(rs\).

This proves a useful necessary search condition: a hypothetical integral STCI pair must have a nontrivial common factor between its leading normal forms over \(k(C)\). It must acquire at least \(ab/4-rs\) additional generic contact units, and the ratio of its required length to the ordinary product is at least \(9/4\). These are exact necessities, not an argument that the extra contact is unavailable.

The resulting candidate generator is concrete:

1. Choose degrees and exact equation orders with \(a,b\ge5\), \(4\mid ab\), \(r\le a/3\), and \(s\le b/3\).
2. Choose a shared-root pattern for the leading symbols, retaining its movement, branching and marked boundary behavior. At \(a=3r\) or \(3r+1\), impose the actual image in (6); at \(a\ge3r+2\), every leading symbol is available. Apply the analogous rule to \(G\).
3. Lift using actual coefficients in \(V_{a,r}\) and \(V_{b,s}\). Compute the full generic local intersection length, allowing cancellations and extra initial generators. Do not substitute the product \(rs\) once the symbols share a root.
4. Retain only proper pairs, compute \(ab-4M\), and test full global support and boundary attachment when the generic length reaches \(ab/4\). Record whether a failure came from a forced surface, inaccessible global symbol, insufficient higher contact, or residual/global boundary behavior.

This workflow uses freedom where it exists and makes each failure update a specific part of the next candidate choice. It does not make any one shared-root type compulsory; the accepted root, conductor and filtration records can test patterns within their exact hypotheses.

## Evidence, checks and limitations

The [independent audit](2026-10-28-stci-search-freedom-independent-audit.md) reconstructs the flag sequence and all-degree formula, verifies the symbol ranks and generic common-root necessity, and records its own finite Macaulay2 controls. Its outcome is PASS with the stated scope. The auxiliary result at degree \(3r+1\), included explicitly here, follows by substituting (1) into (6).

The reproducible [Macaulay2 script](../computations/stci_search_freedom_2026_10_28.m2) works over \(\mathbf Q\), saturates the powers, checks (1) for \(1\le m\le6\) and every \(0\le d\le3m+2\), checks the forced fixed factor, and verifies the three symbol rows. Its [saved JSON](../computations/stci_search_freedom_2026_10_28.json) preserves the outcome and source/image/target dimensions. An initial matrix-target mismatch in the fixed-factor check was repaired by converting the ideal-module basis to its ambient polynomial matrix; it was an implementation error, not a mathematical counterexample.

No existing accepted proof was rerun to establish a new exclusion. No unrestricted STCI conclusion follows. The missing work is to solve or obstruct the actual higher-contact equations on one of the admissible shared-root loci, with global coefficients and properness retained. The first-symbol count alone does not settle those equations, even when its map is surjective.
