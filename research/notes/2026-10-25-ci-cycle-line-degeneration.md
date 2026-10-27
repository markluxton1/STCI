# A line is absorbed into the residual curve: five nodes and four units of genus

Date: 2026-10-25. **Exploratory coordinate experiment; not canonically
promoted.** This note continues the deformation laboratory for actual
complete intersections containing the fixed rational quartic. It turns a
failed smooth-residual candidate into a particularly transparent genus
redistribution. No STCI claim is made.

## 1. The actual two-parameter family

Work over \(\mathbf Q\), taking geometric fibers or embedding into
\(\mathbf C\) when discussing irreducibility and topology. Retain
\[
C=[s^4:s^3t:st^3:t^4],\quad Q=x_0x_3-x_1x_2,
\]
\[
F=x_1^4-x_0^3x_3,\quad G=x_2^4-x_0x_3^3,\quad
A=x_1^3-x_0^2x_2,\quad D_3=x_2^3-x_1x_3^2.
\]
Set
\[
H_0=x_0^2+x_1^2+x_2^2+x_3^2+x_0x_2+2x_1x_3,
\]
\[
H_1=2x_0^2+3x_1^2+5x_2^2+7x_3^2+x_0x_1+x_0x_3+x_1x_2+3x_2x_3,
\]
and consider the actual homogeneous quartics
\[
f_a=F+QH_0+a x_0A,\qquad
 g_b=G+QH_1+b x_3D_3.
\tag{1}
\]
Every pair vanishes on the same embedded \(C\). The separately checked
\((a,b)=(2,3)\) member has a smooth geometrically integral residual curve
of degree twelve and genus sixteen, with eighteen simple attachments to
\(C\); its evidence is the
[exact benchmark script](../computations/verify_ci_smooth_residual_example_2026_10_25.m2).
This note investigates the initially unsuccessful choice \((1,1)\).
The general deformation framework and its review are in
[the laboratory](2026-10-25-ci-cycle-deformation-laboratory.md) and
[the exploration audit](2026-10-25-ci-cycle-exploration-audit.md).

The canonical input [R0021](../results/quartic_mu4_degeneration.md)
concerns the original prescribed \((F,G)\) family, not (1). All new finite
scheme computations here remain provisional research evidence.

## 2. Exact residual decomposition at (1,1)

Let \(I_C\) be the actual four-generator quartic-curve ideal. The
[QQ Macaulay2 experiment](../computations/ci_cycle_line_degeneration_2026_10_25.m2)
computes saturated colons
\[
I_D=((f_1,g_1):I_C)^{\mathrm{sat}},\qquad
I_E=(I_D:I_L)^{\mathrm{sat}},\qquad
I_L=(x_0+x_1,x_2+x_3).
\]
It establishes the following exact coordinate example:

* \(V(f_1,g_1)=C\cup L\cup E\) scheme-theoretically, with
  \(I_D=I_L\cap I_E\) and \((f_1,g_1)=I_C\cap I_D\).
* \(E\) has degree eleven and Hilbert polynomial \(11n-11\), hence
  arithmetic genus twelve.
* The projective Jacobian singular scheme of \(E\) is empty over
  \(\mathbf Q\), and \(H^0(E,\mathcal O_E)=\mathbf Q\). Smoothness and
  proper field-extension base change imply geometric connectedness, hence
  geometric integrality.
* \(L\cap E\) consists of five geometrically reduced points,
  \(C\cap E\) of seventeen, and \(C\cap L\) of one. There is no triple
  intersection.

Consequently all these intersections are ordinary transverse nodes in
the corresponding scheme unions. The residual curve \(D=L\cup E\) has
exactly five nodes, and the total curve has twenty-three nodes.

Parameterize the line by
\[
L=[-r:r:-s:s].
\]
Its five attachments to \(E\) are cut out by the squarefree binary quintic
\[
P_5(r,s)=4r^5-2r^4s+9r^3s^2+2r^2s^3+3rs^4+2s^5.
\tag{2}
\]
The unique point of \(C\cap L\) is the curve parameter \(u=t/s=-1\), or
\([1:-1:-1:1]\). It has \(r/s=-1\), and
\(P_5(-1,1)=-14\ne0\), so it is not one of the five residual nodes.
Neither distinguished endpoint of \(C\) occurs in this configuration's
attachment divisor.

## 3. Why the line occurs: a ruling stratum, not an accidental factor

The fixed line \(L\) is contained in (1) exactly at \(a=b=1\), because
\[
f_a|_L=(1-a)r^3(r+s),\qquad
 g_b|_L=(1-b)s^3(r+s).
\]
But a line in the same ruling moves with the parameters. On the smooth
quadric write
\[
x_0=\rho c,\quad x_1=\rho d,\quad
x_2=\sigma c,\quad x_3=\sigma d,
\]
and put \(K_C=\rho d^3-\sigma c^3\), which cuts out \(C\) on \(Q\).
Restriction of the actual equations gives
\[
f_a|_Q=\rho^3(d+a c)K_C,\qquad
 g_b|_Q=-\sigma^3(c+b d)K_C.
\tag{3}
\]
Thus the two ruling factors coincide precisely on the parameter hyperbola
\[
ab=1.
\tag{4}
\]
For \(a\ne0\), the residual then contains the moving ruling line
\[
L_a=V(x_1+a x_0,\ x_3+a x_2).
\]
This line meets \(C\) at the parameter \(u=-a\). The decomposition at
\((1,1)\) therefore belongs to a natural stratum inherited from the
unique containing quadric. It is not five unrelated node conditions
that happen to vanish simultaneously.

Near \((1,1)\), after restricting to the open set where the remaining
curve and the displayed intersections stay smooth and transverse, this
stratum retains a degree-eleven genus-twelve component and a line joined
to it at five points. This is an openness statement local to the checked
member, not a claim about every point of the whole hyperbola.

## 4. All five nodes smooth in the same parameter direction

For an explicit infinitesimal check, use normal coordinates to \(L\),
\(n_0=x_0+x_1\) and \(n_1=x_2+x_3\). The first-normal matrix of
\((f_1,g_1)\) is
\[
M_L=
\begin{pmatrix}
r^3+2r^2s+3rs^2+2s^3&-r^3-3r^2s-2rs^2\\
4r^2s-2rs^2+8s^3&-4r^3+2r^2s-9rs^2-s^3
\end{pmatrix}.
\]
Its determinant is
\[
\det M_L=-(r+s)P_5(r,s).
\tag{5}
\]
The six zeros are exactly the one attachment to \(C\) and the five to
\(E\). Denote the right-hand entries of its rows by
\(F_1=-r(r+s)(r+2s)\) and
\(G_1=-4r^3+2r^2s-9rs^2-s^3\). The entry \(F_1\) is nonzero at all five
roots of \(P_5\).

At such a residual node, a first-order parameter change gives values
\(\delta f=-r^3(r+s)\delta a\) and
\(\delta g=-s^3(r+s)\delta b\). A relation between the two gradient rows
identifies its one-dimensional smoothing class with
\[
(r+s)(-G_1r^3\delta a+F_1s^3\delta b).
\]
The exact polynomial identity
\[
-G_1r^3=rP_5+F_1s^3
\]
therefore makes this a nonzero scalar multiple of
\[
\delta a+\delta b
\tag{6}
\]
at each of the five nodes. The tangent line is exactly the tangent to
\(ab=1\), as predicted by the moving ruling.

The standard local model for a nodal family is \(xy=\tau\); see
[Stacks, étale local structure of nodal families](https://stacks.math.columbia.edu/tag/0H8M).
In a formal or étale neighborhood of this checked member, after labelling
the five nodes, each residual smoothing parameter is a unit times
\(ab-1\): it vanishes along the moving-line stratum and has nonzero
normal derivative by (6). Their product is a unit times \((ab-1)^5\).
This product records five node-smoothing contributions; it is not a
claim that the scheme-theoretic image of the critical locus has ideal
\((ab-1)^5\). That image can have reduced ideal \((ab-1)\).
This is a **local residual discriminant statement**. The total curve
retains nodes where it meets the fixed \(C\), so its entire singular-fiber
locus would not be the discriminant intended here.

To control the whole residual family locally, use the smooth blowup
\(\operatorname{Bl}_C\mathbf P^3\) from the deformation laboratory.
The two strict transforms have class \(4H-E_C\); their proper
intersection is flat near the checked base point. At its eighteen simple
attachments the blowdown is an isomorphism on the residual curve, because
the ideal of \(C\) restricts there to a Cartier point. Reducedness of
these attachments is open. Properness and openness of smoothness then
allow a neighborhood where the only residual singularities arise from
the five nodes just analyzed.

A transverse path such as \(a=1+t,b=1+2t\) smooths all five residual nodes
near \(t=0\), since \(ab-1=3t+2t^2\). Its member at \(t=1\) is also the
separately checked smooth benchmark. No assertion is made that every
intermediate parameter on the full affine path avoids all other bad
strata.

## 5. Four units of genus come from five gluing points

The residual genus is constant:
\[
p_a(L\cup E)=0+12+5-1=16.
\]
Smoothing the five nodes joins the two components and converts the
four independent cycles of their dual graph into genus on one smooth
component. This operation absorbs the line through deformation; it is
not a contraction or a blowdown of \(L\).

For the full curve the two configurations have the following budgets:

| Geometric quantity | At the line member | Nearby smooth residual |
| --- | --- | --- |
| Components | \(C,L,E\) | \(C,D\) |
| Degrees | \(4,1,11\) | \(4,12\) |
| Normalization genus sum | \(12\) | \(16\) |
| Total nodes / total delta | \(23\) | \(18\) |
| Dual-graph first Betti number | \(21\) | \(17\) |
| Arithmetic genus | \(12+23-3+1=33\) | \(16+18-2+1=33\) |
| Topological \(b_1\) over \(\mathbf C\) | \(45\) | \(49\) |
| Topological \(b_2\) over \(\mathbf C\) | \(3\) | \(2\) |

The topological Euler characteristic drops by five when the five nodes
smooth, even though the arithmetic genus stays fixed. The genus sixteen
of the residual can therefore be realized partly as genus twelve and
partly as graph gluing, without involving the severe endpoint bouquets
of the original \(\mu_4\) arrangement.

The canonical sheaf gives a particularly tidy componentwise check.
A \((4,4)\) complete intersection has \(\omega_Z=\mathcal O_Z(4)\).
For this nodal reduced fiber, normalization restricts it as the canonical
bundle plus the reduced attachment boundary. Consequently
\(2g_i-2+n_i=4d_i\):

| Component | \(d_i\) | \(g_i\) | Attachments \(n_i\) | \(2g_i-2+n_i\) |
| --- | --- | --- | --- | --- |
| \(C\) | 4 | 0 | 18 | 16 |
| \(L\) | 1 | 0 | 6 | 4 |
| \(E\) | 11 | 12 | 22 | 44 |
| Smoothed \(D\) | 12 | 16 | 18 | 48 |

This also explains the quintic before computing it. In a reduced nodal
complete intersection of degrees \(d,e\), a line component must have
\(d+e-2\) attachments, because \(\omega_Z|_L=\mathcal O_L(d+e-4)\)
and \(\deg\omega_L=-2\). Here there are six attachments in total,
and the one intersection with \(C\) leaves five for the other residual
component. Absorbing a line joined at five points then raises
normalization genus by four.

The six marked points on the line are geometrically meaningful. In
particular, it is a stable rational component of the total nodal curve,
not an unstable component discarded by forgetting the embedding.

## 6. The boundary on C stays ordinary throughout this change

Let \(u=t/s\) be the affine parameter on \(C\), and set
\[
h_0=1+u^2+u^3+2u^5+u^6+u^8,
\]
\[
h_1=2+u+3u^2+2u^4+5u^6+3u^7+7u^8.
\]
Independently differentiating the actual global sources in (1) gives the
first-normal determinant on \(C\):
\[
\beta_{a,b}(u)=(u+a)h_1+u^9(1+bu)h_0
-3au^8-(4+2ab)u^9-3bu^{10}.
\tag{7}
\]
At \((1,1)\),
\[
\beta_{1,1}(u)=(u+1)B_{17}(u),\qquad
B_{17}=h_1+u^9h_0-3u^8(u+1).
\tag{8}
\]
The factor \(u+1\) is the attachment to \(L\); \(B_{17}\) supplies the
seventeen attachments to \(E\). It is squarefree, has nonzero constant
and leading coefficients, and \(B_{17}(-1)=14\). Thus all eighteen
attachments are simple and avoid the distinguished endpoints. This
remains true on an open neighborhood in the parameter plane, including
points on both sides of the residual node-smoothing stratum.

The contact pattern along \(C\) is therefore already ordinary while
five additional nodes off \(C\) redistribute residual genus. Local
invariants sampled only at the attachments to \(C\) will miss that part
of the topology. The boundary divisor remains useful, but the residual
curve's own incidence graph supplies independent data.

## 7. Evidence limits and next experiments

The [Macaulay2 script](../computations/ci_cycle_line_degeneration_2026_10_25.m2)
and its [output](../computations/ci_cycle_line_degeneration_2026_10_25_m2.txt)
check the actual saturated residual ideals, geometric smoothness and
connectedness criterion, lengths and geometric reducedness of all three
attachment schemes, absence of triples, and the first-normal matrix.
The [stdlib companion](../computations/ci_cycle_line_degeneration_2026_10_25.py)
and [JSON output](../computations/ci_cycle_line_degeneration_2026_10_25.json)
check fourteen global-source, ruling, boundary, and genus identities.
These are exact checks over \(\mathbf Q\), with no finite-field lifting
step. The local smoothing and topology interpretations are stated
separately from the finite ideal computations.

The two-parameter family constrains all five smoothing parameters to
move together. A next experiment in the full eighteen-dimensional
quartic source should ask whether these five node smoothings can be
controlled independently while retaining a chosen first-order boundary
on \(C\). If so, partial smoothings would give a ladder of residual
normalization genera and graph contributions. If not, the dependence
could reveal a global linkage constraint worth understanding.

Another direction is to follow the degree-eleven component along
\(ab=1\), including limits of the six-pointed ruling line. Its stable
point configuration might organize boundary strata that the divisor on
\(C\) cannot see. No classification, global discriminant formula, or
canonical promotion is claimed here.
