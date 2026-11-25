# Marked Chow boundary from the two endpoint interpolation systems

**Status.** Companion to [marked Chow configurations](marked_chow_configuration_boundary.md). The reduced endpoint rank formula and the \((4,4)\) line criterion are already established; the projective boundary interpretation and explicit spectral-image calculations here are provisional deductions, pending independent review. Work over an algebraically closed field of characteristic zero unless stated otherwise. The purpose is to identify the intrinsic incidence boundary, not to enumerate low-degree STCI cases.

## 1. Two sequences of projective maps supplied by contraction

For the marked points \(s_i=(u_i,v_i)\in T\), the local evaluations at the two endpoints are
\[
(r,ur^3,vr^4),\qquad (r',\alpha r'^3,\beta r'^4),
\quad r'=q/r,\quad \alpha=v^2/u^3,\quad\beta=v^3/u^4.
\]
Thus \(\alpha=1/(q\eta),\ \beta=1/(q^2\eta)\), and \(\alpha/\beta=q\). The two natural weighted systems are
\[
V_n^0=\langle u^av^b:3a+4b\le n\rangle,\qquad
V_n^\infty=\langle\alpha^a\beta^b:3a+4b\le n\rangle
\quad(a,b\ge0).
\]
They give monomial rational maps of \(S\) to projective spaces, regular on simultaneous toric graph refinements. The first nonconstant systems (\(n=3\)) are exactly the endpoint contact pencils. At order four they give the two birational maps
\[
\varphi_0=[1:u:v],\qquad\varphi_\infty=[1:\alpha:\beta]
\]
to projective planes. At orders six, seven and eight the bases add \(u^2,uv,v^2\), respectively (or their opposite counterparts). At eight one has all plane quadratics. These are determined by the contraction, not by an arbitrary embedding of the Chow surface.

The [exact rank formula](arrangement_endpoint_delta.md#the-exact-two-endpoint-rank-formula) for distinct markings is
\[
\delta_\epsilon=\sum_{n\ge0}(m-\operatorname{rk}\operatorname{ev}_{\sigma,n}^\epsilon),
\qquad
\operatorname{ev}_{\sigma,n}^\epsilon:V_n^\epsilon\to k^m,
\qquad \epsilon\in\{0,\infty\}.
\]
Products of \(m-1\) affine-linear functions separate the points, so all evaluations are surjective by \(n=4(m-1)\). Equivalently, each delta equals the sum of the weighted rank-jump orders, counted with multiplicities. Thus for fixed \(m\) the entire reduced endpoint-length stratification is a finite determinantal stratification. Constant ranks alone do not identify the attachment algebra, its multiplication, or its nonreduced limits.

The two plane maps suggest including the strict transforms of the lines joining each pair of markings, with incidence with each other and with the inherited toric boundary. For higher systems retain the projective linear spans of subsets of markings and the corresponding linear systems of sections through them. A linear system of positive dimension is not a canonical single divisor; no finite distinguished divisor collection for all higher ranks has yet been selected. The rank-drop strata are additional to the four-character incidence discriminant in the companion note. For example a generic collinear triple in the first plane need not satisfy any additional toric-pencil incidence. These rank strata need not be smooth, and their resolutions do not follow immediately from a wonderful compactification theorem.

Log forms \(d_{\rm rel}\log(\ell_{ij}/\ell_{ik})\) for joining lines on either plane have residues equal to orders along the corresponding total transforms, including the marked exceptional divisors. This supplies a concrete family of boundary forms to compare with the longitudinal form; it does not by itself establish descent of \(q\,d\log r\).

## 2. Three markings: the cusp appears intrinsically

For three distinct points at either endpoint there are exactly three interpolation types:
\[
\begin{array}{c|c|c}
\text{type}&\text{jump orders}&\delta\\\hline
\text{noncollinear}&0,3,4&7\\
\text{nonvertical collinear}&0,3,6&9\\
\text{vertical collinear}&0,4,8&12
\end{array}
\]
The rank at weight three is two unless \(u\) is constant; the other rows follow from independence of \(1,u,v\) or Vandermonde interpolation on the line. See the established [three-branch calculation](chow_moment_residual_speciality.md).

For a reduced \((3,4)\) CI the Hilbert polynomial \(12d-18\) requires \(\delta_0+\delta_\infty=21\). Hence up to endpoint exchange the points are vertical at \(p_0\) and nonvertical collinear at \(p_\infty\). Write \(u=c\ne0\) and \(q=c/v\). The image of the vertical pencil fiber in the opposite plane is
\[
[1:\alpha:\beta]=[c q^3:q:1].
\]
Its closure is the cuspidal cubic parametrized by \([Q:S]\mapsto[cQ^3:QS^2:S^3]\), with cusp at infinity. Three distinct finite points are collinear iff their monic cubic is missing the quadratic term, i.e. \(\sum q_i=0\). This is the familiar additive group law on a cuspidal cubic. In particular the intersection of the vertical-marking stratum and the opposite collinearity discriminant restricts, off the collision diagonals, to the first-moment hyperplane. Endpoint exchange leaves \(q=\alpha/\beta\) unchanged. No new CI coverage follows: the reduced moment assertion was already known. What is new in this interpretation is the appearance of the cuspidal spectral line from the actual opposite endpoint map, rather than its independent introduction by a generalized-Jacobian modulus.

## 3. Four markings: same ranks, different realization

The complete list of possible jump orders for four distinct points at one endpoint is
\[
\begin{array}{c|c}
\text{jump orders}&\delta\\\hline
0,3,4,6&13\\
0,3,4,7&14\\
0,3,4,8&15\\
0,3,6,9&18\\
0,4,8,12&24
\end{array}
\]
Indeed constant \(u\) gives the last row by Vandermonde; affine dependence \(v=A+Bu\) with nonconstant \(u\) gives the preceding row. Otherwise \(1,u,v\) are independent. If adjoining all three of \(u^2,uv,v^2\) failed to reach rank four, their evaluations would lie in the span of \(1,u,v\), making it a unital subalgebra stable under multiplication by both \(u\) and \(v\). Those two functions generate all functions on the four distinct points, a contradiction. So the fourth jump is at six, seven or eight. This argument also gives the rank possibilities in any characteristic; the stated moment exclusion below uses characteristic zero.

For a reduced \((4,4)\) CI the Hilbert polynomial \(16d-32\) requires sum 36, forcing the pair \((18,18)\). Thus both endpoint planes have nonvertical collinearity. Write
\[
v=A+Bu,\qquad\beta=C+D\alpha.
\]
The [existing reduced line criterion](arrangement_endpoint_delta.md#the-reduced-44-locus-as-two-affine-line-incidence-conditions) states that actual reduced CI realization additionally requires \(AC\ne0\), and is sufficient under that condition. Its necessity uses invariant lifting and boundary avoidance, not just the delta sum. This distinction is crucial.

When \(AC\ne0\) the two lines in the endpoint planes give
\[
\eta(1-Bq)=Aq^2,\qquad 1-Dq=Cq^2\eta,
\]
and hence the four markings satisfy
\[
ACq^4-BDq^2+(B+D)q-1=0.
\]
The values \(q_i\) are distinct because \(u=Aq/(1-Bq)\) uniquely reconstructs the point. The missing cubic coefficient gives the moment.

If \(A=0\) then \(B\ne0\), \(q=1/B\) is constant, and \(\beta=B\alpha\), so \(C=0,D=B\) (the opposite coordinates are distinct). Conversely \(C=0\) implies the same common-quadric case by reversing endpoints. Both endpoint defects remain 18, but \(M_1=4/B\ne0\). Such a reduced arrangement is not a \((4,4)\) CI: all four quartics are on the same smooth quadric, with total class \((4,12)\) up to ruling exchange, which cannot be contained in a nonzero \((4,4)\) divisor cut by a quartic. Thus every quartic containing the arrangement contains the quadric, violating proper intersection for any two. The distinction between the two strata is an incidence with a **toric vertex** in the endpoint plane: a joining line through \([1:0:0]\) has zero intercept. Equal ranks and equal arithmetic genus alone cannot see it.

### Opposite image and the spectral cusp

For fixed \(v=A+Bu,\ A\ne0\), the opposite plane parametrization is
\[
[1:\alpha:\beta]=[Aq^4:q(1-Bq):1-Bq].
\]
Its homogeneous degree-four linear system lies in \(\langle Q^4,Q^2 S^2,QS^3,S^4\rangle\), missing \(Q^3S\). This is the pullback of the sections of \(\mathcal O(4\cdot0)\) on the rational cuspidal curve obtained by pinching \(2\infty\) (local ring \(k[[t^2,t^3]]\)). Thus the plane map factors through that curve and all hyperplane sections with four finite roots are balanced. **The plane quartic image is not asserted to be the ordinary one-cusp curve itself.** When \(B\ne0\), \(q=1/B\) and \(q=\infty\) map to the same point, and when \(B=0\) the local parametrization at infinity has orders 3 and 4. The normalization-side linear system and its missing coefficient are the essential common structure. Compare [spectral boundary modulus](spectral_boundary_modulus.md), where the same pinch arises from the aggregate boundary jet. The quartic hyperplane system is a subsystem of the balanced degree-four system, not the whole system for a fixed first line.

### Exact spectral image of the reduced realization locus

Conversely let \(H(q)=q^4+c_2q^2+c_1q+c_0\) be squarefree and \(c_0\ne0\). Choose \(AC=-1/c_0,\ BD=c_2/c_0,\ B+D=-c_1/c_0\); the last two conditions have a solution because the field is algebraically closed, and \(A,C\ne0\) can be chosen with their specified product. For every root of \(H\), neither \(1-Bq\) nor \(1-Dq\) is zero by the quartic equation, so \(\eta=Aq^2/(1-Bq)\ne0\) gives four distinct interior Chow points on the two required lines. The established line criterion supplies the actual reduced \((4,4)\) CI. Hence the spectral image is exactly the squarefree nonzero-root open part of \(V(h_1)\subset\mathbf P^4\), and its projective closure is that hyperplane. This is about the spectral projection of the reduced realization locus, not identification of the entire Chow or Hilbert closure with that hyperplane; repeated roots need separate analysis.

## 4. What the two tests establish about the boundary

The three-marking and four-marking controls reveal three distinct kinds of incidence: among markings, among their associated curves, and between those curves and the inherited toric boundary. The two endpoint maps compare the same marked configuration in different projective geometries. Their hyperplane systems can force the first moment by a missing coefficient without an explicit differential extension calculation. This is consistent with the HKT strategy of constructing a marked incidence geometry before imposing a boundary compactification.

The examples also show why preserving just the topology of the separated family, or its two delta invariants, is insufficient. Even the full list of reduced interpolation ranks does not encode arbitrary embedded source equations. The current problem is to find the right marked incidence boundary and its stable extension for general configurations, including higher-rank strata and coincident points, and to understand which information is retained under contraction. The generic four-pencil stable surface pair is only a starting point; adding the higher incidence curves changes the log canonical model and its discriminant. Neither these tests nor the ordinary cusp group law proves UM1 beyond its established coverage. No independent review, full discriminant resolution, or nonreduced flat-family identification has been completed.
