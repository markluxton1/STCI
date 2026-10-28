# Independent audit: global freedom at prescribed normal order

Date: 2026-10-28. Reviewer: independent dimension lane under the freedom/constraints agent. Status: independently reconstructed provisional calculation; no canonical promotion.

## Scope and accepted input

Let (C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k), let \(\mathcal I=\mathcal I_C\), and let \(Q=V(x_0x_3-x_1x_2)\). The calculation concerns the sheaf powers \(\mathcal I^m\), hence saturated homogeneous powers in the coordinate ring, rather than an assertion that the unsaturated homogeneous ideals have identical graded pieces. The curve is regularly embedded, so these sheaf powers also express normal vanishing order at least \(m\).

The quadric is smooth in every characteristic. In its Segre coordinates the curve is the graph of the cubic map \((s:t)\mapsto(s^3:t^3)\), and has divisor class \((1,3)\), up to swapping the rulings. The balanced characteristic-zero conormal splitting used only in the symbol-target comparison below is the promoted [STCI-R-0020](../results/quartic_conormal_characteristic_jump.md), with its stated evidence. No inherited exclusion proof is rerun.

## Exact flag calculation

Write \(A_m(d)=h^0(\mathbf P^3,\mathcal I^m(d))\), with \(\mathcal I^0=\mathcal O\). The regular-sequence description \(\mathcal I=(Q,c)\) near \(C\), together with the Cartier divisor \(C\) on \(Q\), gives an exact sequence

\[
0\longrightarrow\mathcal I^{m-1}(d-2)
 \xrightarrow{\;Q\;}\mathcal I^m(d)
 \longrightarrow\mathcal O_Q(d-m,d-3m)\longrightarrow0. \tag{1}
\]

The kernel statement is the local equality
\((Q)\cap(Q,c)^m=Q(Q,c)^{m-1}\). It holds off \(C\) as well; thus (1) is a sheaf statement on the whole ambient projective space.

If \(d<3m\), the right-hand term has no sections. Therefore every degree-\(d\) form vanishing normally to order at least \(m\) is divisible by \(Q\), and division reduces \((m,d)\) to \((m-1,d-2)\). Iteration gives

\[
 A_m(d)=0\quad(d<2m),
\]

and, for \(2m\le d\le3m\), the exact vector-space identity

\[
 H^0(\mathcal I^m(d))
 =Q^{3m-d}H^0\bigl(\mathcal I^{d-2m}(3(d-2m))\bigr). \tag{2}
\]

The exponent in (2) is a forced common factor, not merely a dimension estimate.

For \(d\ge3m-1\), induction in (1) proves
\(H^1(\mathcal I^m(d))=0\): the left-hand term has vanishing \(H^1\) by induction, while both ruling degrees of the right-hand term are at least \(-1\), so it too has vanishing \(H^1\). For \(d\ge3m\), recursion of the dimensions in (1) gives

\[
 A_m(d)=\binom{d+3}{3}
  -\frac{m(m+1)(4d+1)}2
  +\frac{7m(m^2-1)}3. \tag{3}
\]

One can verify (3) directly by subtracting its expression for \((m-1,d-2)\): the difference is \((d-m+1)(d-3m+1)\), exactly the dimension of the right-hand term. The base is \(A_0(d)=\binom{d+3}{3}\). The same polynomial also holds at \(d=3m-1\), although the piecewise formula below already covers that boundary.

Set

\[
D(u)=A_u(3u)=\frac{5u^3+15u^2+16u+6}{6}\qquad(u\ge0).
\]

Equations (2) and (3) therefore give the all-degree formula

\[
A_m(d)=\begin{cases}
0,&d<2m,\\
D(d-2m),&2m\le d\le3m,\\
\displaystyle\binom{d+3}{3}
-\frac{m(m+1)(4d+1)}2+\frac{7m(m^2-1)}3,&d\ge3m.
\end{cases} \tag{4}
\]

The overlapping values at \(d=3m\) agree. This dimension formula uses the smooth quadric flag and is characteristic independent; the next target-space formula is stated in characteristic zero.

## Audit of actual symbol-image dimensions

The kernel of the actual global order-\(r\) symbol map is exactly
\(H^0(\mathcal I^{r+1}(d))\), so its rank is \(A_r(d)-A_{r+1}(d)\). For \(d=3r\) this equals

\[
 A_r(3r)-A_{r+1}(3r)=5r^2+2\qquad(r\ge1). \tag{5}
\]

For \(r\ge2\), this is \(D(r)-D(r-2)\); for \(r=1\), the kernel is zero and \(D(1)=7\). By R-0020, in characteristic zero the full abstract target has dimension

\[
 h^0(C,\operatorname{Sym}^rN_C^*(3r))
 =(r+1)(5r+1).
\]

Thus the actual image has codimension \(6r-1\). Counting the full target as freely available coefficients is already incorrect at the minimal degree without a forced quadric factor. The examples \(r=1,2,3\) have image dimensions \(7,22,47\), respectively, inside targets of dimension \(12,33,64\).

At \(d\ge3r+2\), (1) gives \(H^1(\mathcal I^{r+1}(d))=0\), so the global symbol map is surjective. This threshold is sufficient; it is not asserted to be an optimal threshold for every variant of the source problem.

## Audit of the generic-intersection consequence

Suppose \(F_a,G_b\) are integral equations of degrees at least five, both containing \(C\), with exact normal orders \(r,s\). If \(a<3r\), (2) forces \(Q\mid F\), contradicting integrality and \(a\ge5\); similarly \(b\ge3s\). Therefore

\[
 r\le a/3,\qquad s\le b/3,\qquad rs\le ab/9. \tag{6}
\]

Over the generic point of \(C\), if the two leading binary normal forms have no common factor, the associated graded ideal is a binary complete intersection and the generic local intersection length is exactly \(rs\). A sole-support proper intersection would instead have generic length \(ab/4\). Since \(ab/9<ab/4\), its leading normal forms must share a factor: excess contact beyond the ordinary product \(rs\) is necessary.

This is a generic tangent-cone test, not an obstruction to all pairs. Shared factors can yield precisely the higher contact that the search must test. No assertion is made that individual normal order equals the eventual intersection multiplicity. The integral-equation hypothesis excludes the evident counterexamples formed using powers or products with the quadric.

## Reproducible finite control and outcome

The reviewer independently checked (4) using Macaulay2 over \(\mathbf Q\), saturating powers of

\[
I=(x_0x_3-x_1x_2,\ x_1^3-x_0^2x_2,\ x_1^2x_3-x_0x_2^2,\ x_1x_3^2-x_2^3).
\]

The check compared \(\dim R_d-\dim(R/\operatorname{sat}(I^m))_d\) with (4) for \(m=1,2,3,4\) and every \(0\le d\le3m+2\). All comparisons passed. The proposing lane has a separate broader table. These finite comparisons test implementation and boundary values; the all-degree claim rests on (1)–(4).

Reviewer outcome: **PASS for the exact sheaf-power dimension formula, forced quadric factor, actual symbol-image rank, and the generic common-root necessity with the stated integral-equation hypotheses.** The calculation neither decides STCI nor gives expected codimensions for the higher-contact equations. Its concrete search use is to remove forced common-surface sources, retain actual global symbol images, and search the shared-root locus rather than generic pairs.
