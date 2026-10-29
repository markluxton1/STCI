# Carrier and conductor geometry

**Mathematical consolidation draft — not a new proof or a change in theorem status.** Characteristic zero unless explicitly indicated. This chapter collects the geometry of a surface containing a curve and the obstruction to cutting out precisely that curve with one more equation. Canonical authority remains in the R-records and their proof/audit sources. In particular, the case-by-case quartic theorem is **outlined**, not independently reproved here.

## 1. From a set-theoretic complete intersection to a divisor on a surface

Fix
\[
C=C_0=\{[s^4:s^3t:st^3:t^4]\}\subset\mathbf P^3.
\]
Suppose homogeneous forms \(F,G\) have \(\sqrt{(F,G)}=I_C\). Choosing an **integral** component \(X=V(F_0)\) of \(V(F)\) containing \(C\), the restriction of \(G\) cuts out \(C\) set-theoretically on \(X\), provided \(G\) is not identically zero on \(X\). Because \(V(F,G)\) has pure curve support, \(F\) and \(G\) cannot share a surface component. Thus integral *carriers* are a natural intermediate problem. This reduction does not mean \(F\) itself is irreducible, or that every useful carrier is normal.

Let \(\nu:S\to X\) be the finite normalization, and let \(H=\nu^*\mathcal O_X(1)\). If \(G\) has degree \(b\), its pullback is a section of \(\mathcal O_S(bH)\). Its **entire zero support** is \(\nu^{-1}(C)\), not merely the preferred component mapping birationally to \(C\). This is the first crucial distinction: additional inverse branches and isolated inverse points matter.

When the full reduced inverse support is a single curve \(c\) mapping isomorphically to \(C\), the zero divisor is \(nc\) for some positive integer \(n\), so
\[
nc\sim bH.
\]
Intersecting with \(H\) gives \(n\deg C=b\deg X\), since \(H\cdot c=\deg C\) and \(H^2=\deg X\). Thus \(n=b\) **for a quartic carrier of this quartic curve**, but not for an arbitrary-degree carrier. On a singular normal surface \(c\) need not itself be Cartier; only the relevant multiple is necessarily Cartier. See R-0001 and its [independent assembly audit](../notes/2026-10-11-session-all-quartic-dependency-assembly-independent-audit.md).

The conceptual question is therefore twofold: **can the inverse-support divisor have the required polarization class upstairs, and can its defining section descend through the conductor downstairs?** Neither condition alone suffices.

### 1.1 Reduction to integral factors and the lower-degree bound

For a genuine set-theoretic presentation \(V(F,G)=C\), the two forms are coprime: a common irreducible factor would contribute a surface to their intersection. Let \(f\) be any irreducible factor of \(F\). Then \(f\) and \(G\) are coprime, so \(V(f,G)\) is a nonempty projective complete intersection of pure dimension one. Its support is contained in the irreducible curve \(C\), hence is exactly \(C\). Thus **every irreducible factor of either defining equation is itself an integral carrier with a mate**; multiplicities of factors do not alter the support argument.

For the fixed curve, linear carriers are impossible because \(C\) is nonplanar. Its unique quadric \(Q\) is smooth, with \(C\) of bidegree \((1,3)\); an ambient equation of degree \(b\) restricts to \((b,b)\), which cannot equal a positive multiple of \((1,3)\). Integral cubic carriers are excluded by the separately verified classical theorem, and integral quartic carriers by R-0001. Therefore **each irreducible factor** of \(F\) and \(G\) has degree at least five, and in particular \(\deg F,\deg G\ge5\). This conclusion does not assume the defining equations are irreducible and does not establish that any higher-degree presentation exists. See the [degree-factor audit](../notes/2026-10-11-session-degree-factor-and-mf6-scope-audit.md).

## 2. The normalization is not the original carrier

The normalization \(S\) remembers divisors and intersection theory more transparently than \(X\), but it can lose gluing conditions. Let \(\mathfrak c\) denote the conductor ideal of \(\mathcal O_X\subset\nu_*\mathcal O_S\). A section upstairs may have the correct zero support and still fail to be a section downstairs because its values or infinitesimal jets disagree across the conductor.

At a generic conductor point, this discrepancy is measured by the **full** unit quotient \(B_\eta^\times/A_\eta^\times\) for the finite local conductor algebra \(A_\eta\subset B_\eta\). Passing to reduced conductor points can discard nilpotent unit obstructions. In characteristic zero the logarithm identifies the nilpotent contribution with additive data, which need not be torsion. Consequently, a torsion condition on the reduced phase does not settle descent.

The fixed-carrier theorem R-0003 packages this as a lattice. If the reduced inverse image consists of curves \(\Gamma_1,\ldots,\Gamma_s\), form
\[
\Lambda=\ker\left(\mathbf Z^{s+1}\longrightarrow\mathrm{Cl}(S)\right),\quad
(n_1,\ldots,n_s,d)\mapsto\sum_jn_j[\Gamma_j]-d[H].
\]
The subgroup \(\Lambda_{\rm desc}\) imposes the generic full-conductor unit conditions modulo torsion. Subject to the theorem's exact hypotheses (integral Cohen–Macaulay carrier, finite normalization, no extraneous isolated inverse points), **a mate on this fixed carrier exists exactly when** \(\Lambda_{\rm desc}\) contains a vector positive on every inverse branch. A suitable power clears torsion and forces conductor membership along the target curve. This is a structural criterion, not an algorithm for arbitrary carriers.

**Source:** [R-0003](../results/fixed_carrier_conductor_criterion.md) and [proof with embedded independent reviews](../notes/2026-10-13-generalization-conductor-theorem.md). Its statement is valid in arbitrary characteristic; the characteristic-zero nilpotent logarithm is a tool for analyzing its phases, not a restriction on the entire fixed-carrier criterion.

## 3. The complete exclusion of integral quartic carriers

The accepted theorem R-0001 says that **no integral quartic surface** containing the fixed \(C_0\) has a set-theoretic mate of any positive degree, in characteristic zero. It does not exclude all higher-degree carriers.

Why is the case analysis finite? A normal integral quartic has its own global exclusion argument. For a nonnormal integral quartic, the arithmetic genus of a general plane section is \(3\), while the genus \(\pi\) of the corresponding normalized section belongs to \(\{0,1,2\}\). The independent assembly audit also proves that the normalization is rational, that generic regularity along \(C\) is automatic, and that the mate would have full inverse support. These facts must not be silently assumed.

The six proof lanes are:

| Surface type | Geometric mechanism |
|---|---|
| Normal integral quartic | Normal-carrier global argument, retaining nonreduced exceptional cycles |
| Nonnormal, \(\pi=0\) | Rational minimal-degree normalization: scroll, Veronese or cone; conductor constraints |
| Nonnormal, \(\pi=1\) | Degree-four ADE del Pezzo normalization; anticanonical projection, Cartier double and ribbon contact partitions |
| Nonnormal, \(\pi=2,\lambda=0\) | Bisection, second-pencil and Cartier-double/ribbon incompatibility |
| Nonnormal, \(\pi=2,\lambda=1\), nonendpoint | Trisecant with distinct contacts; exhaustive conductor decompositions and exceptional chains |
| Nonnormal, \(\pi=2,\lambda=1\), endpoint | Triple contact; exhaustive quartic family, ADE corrections and doubled-horizontal strata |

The last two rows cannot be combined by appealing to a generic trisecant. In particular, an argument that excludes only an irreducible residual conic does **not** exhaust the endpoint family. Similarly, the genus-one projection center is derived from the complete anticanonical model and restriction to the lifted curve, not assumed from a chosen example.

For exact dependencies and links to the six independently reviewed proofs, use the [quartic-carrier dependency graph](../MATHEMATICAL_CONSOLIDATION_QUARTIC_CARRIER_DEPENDENCIES.md), the [accepted assembly](../notes/2026-10-11-session-all-quartic-results-acceptance.md), and the [independent coverage audit](../notes/2026-10-11-session-all-quartic-dependency-assembly-independent-audit.md). This section is a **proof guide**; the six source proofs remain necessary until their arguments have been integrated and checked in full.

The full factor reduction and the resulting degree bound are proved in Section 1.1; the quartic-carrier theorem is its deepest input.

### 3.0 Shared reductions and the normal case

The assembly audit proves three prerequisites before splitting the nonnormal cases: generic regularity of every integral quartic along the fixed curve, rationality of every nonnormal quartic normalization, and full inverse support of a hypothetical mate. The rationality argument uses the ruled-surface intersection identity with **all infinitely near multiplicities**; it does not rely on the existence of a mate. Full inverse support uses purity of the pulled-back Cartier divisor and rules out isolated normalization points above C.

For a **normal integral quartic**, the proof is a separate global surface argument, not an instance of the normalized sectional-genus-zero, -one or -two classification. Its inherited inputs include normal-quartic classification, rational-singularity and ADE-pair results, actual normal-sheaf bounds, and necessary exceptional-graph enumerations for both reduced and nonreduced cycles. The enumerations eliminate a necessary superset; they do not assert realization of each graph. The final exceptional-passage argument is geometric. The independent assembly audit checks that the required small-degree exclusions were proved independently and do not invoke the quartic-carrier theorem being assembled.

Sources: [normal global audit](../notes/2026-10-07-session-normal-global-adversarial.md), [nonreduced-cycle audit](../notes/2026-10-07-session-normal-nonreduced-independent-audit.md), and [assembly audit](../notes/2026-10-11-session-all-quartic-dependency-assembly-independent-audit.md).

### 3.1 Genus-zero mechanism: vanishing, classification, cone

On a resolution M of the normalization S, write L for the pullback of H. In the sectional-genus-zero case, L is nef and big with L squared equal to 4, and K_M.L=-6. The divisor K_M+L has negative intersection with L and no sections. Kawamata-Viehweg vanishing and Riemann-Roch give chi(O_M)=1. A general normalized hyperplane section Y is P1, and the restriction sequence for H yields h0(S,H)=6. Thus the complete system maps S finitely and birationally to a degree-four minimal-degree surface in P5. The possibilities include scrolls, the Veronese surface and the singular rational-normal quartic cone.

The cone needs its own argument. On its F4 resolution, the hyperplane class is E+4f, with E squared -4. Its class group is Z[f] and [H]=4[f]. For a mate, the quartic-specific relation b(c-H)~0 forces c~H and makes c Cartier. The smooth curve c cannot pass through the cone vertex, whose local ring is singular. The remaining case is covered by the scroll/conductor exclusion. Exceptional corrections on the resolution must be retained; they cannot be dropped simply because c is smooth.

Sources: [genus-zero audit](../notes/2026-10-09-session-normalization-genus-zero-independent-audit.md) and [nonrational-normalization audit](../notes/2026-10-09-session-nonrational-normalization-independent-audit.md).

#### Genus-zero classification: proof of the six-section reduction

On a smooth resolution \(M\), write \(L=\sigma^*H\), so \(L^2=4\) and \(K_M\cdot L=-6\). Since \((K_M+L)\cdot L=-2\), nefness of \(L\) implies \(h^0(K_M+L)=0\). Kawamata–Viehweg vanishing gives \(H^i(M,K_M+L)=0\) for \(i>0\). Riemann–Roch then yields
\[
0=\chi(K_M+L)=\chi(\mathcal O_M)-1,
\]
so \(\chi(\mathcal O_M)=1\). The same nef-intersection argument gives \(p_g(M)=0\), hence \(h^1(M,\mathcal O_M)=0\). Because \(\sigma_*\mathcal O_M=\mathcal O_S\), the Leray edge map injects \(H^1(S,\mathcal O_S)\) into \(H^1(M,\mathcal O_M)\); no rational-singularity hypothesis is used here.

For a general smooth \(Y\in|H|\), \(Y\cong\mathbf P^1\) and \(H|_Y\cong\mathcal O_{\mathbf P^1}(4)\). The exact restriction sequence gives \(h^0(S,H)=1+5=6\). Since the original four sections generate \(H\), the complete six-section map is basepoint-free; ampleness of \(H\) makes it finite. It is birational because the original map \(S\to X\) is already birational. Its nondegenerate image in \(\mathbf P^5\) has degree four and codimension three, so is a surface of minimal degree. The complete classification gives precisely the scrolls \(S(2,2)\), \(S(1,3)\), the cone \(S(0,4)\), and the Veronese surface. All four are normal; the finite birational map is therefore an isomorphism. This is why the classification is exhaustive even though \(S\) was not assumed smooth.

For the cone, torsion-freeness of its class group forces the lifted \(c\) to be Cartier and to avoid the vertex. The remaining proof uses the ruling map to a rational plane quartic: if its normalization has two points over a plane point, singleton inverse support fails; if all fibers are singletons, the plane quartic still has a singular unibranch point, where the ruling map has vanishing differential. The source proves the resulting local-unit/conductor contradiction. Thus neither a nodal nor a cuspidal base can produce a mate. See the [genus-zero audit](../notes/2026-10-09-session-normalization-genus-zero-independent-audit.md) for the last local calculation.

### 3.2 Genus-one mechanism: intrinsic projection, ribbon, partitions

The normalization is rational by the ruled-surface argument retaining infinitely near multiplicities. Its minimal resolution is a weak degree-four del Pezzo surface; the normal anticanonical model is an ADE two-quadric intersection in P4. Restricting the complete anticanonical sections to the lifted curve determines the projection center: it deletes the middle s²t² coordinate of the rational normal quartic. This is deduced for every carrier in this lane, not assumed from a special family.

An actual Cartier divisor 2c on the normalization defines a Cohen-Macaulay ribbon, including at ADE points where c need not be Cartier. Its nilideal and the entire nonreduced conductor enter the mate obstruction. Replacing this double by the ordinary square of the curve ideal would be incorrect.

The remaining derivative is a binary quartic. Its five multiplicity partitions are [1,1,1,1], [2,1,1], [2,2], [3,1], and [4]. The first two are excluded by the derivative and ribbon-net argument. The remaining three require the complete repeated-partition calculations, including invisible quadric coefficients and boundary directions. The independent Macaulay2 audit records 29 successful checks; earlier failed scaffolding runs are not passing certificates.

Sources: [genus-one interface audit](../notes/2026-10-10-session-genus-one-interface-independent-audit.md) and [repeated-partition audit](../notes/2026-10-10-session-ribbon-repeated-partitions-independent-audit.md).

#### Genus-one projection and ribbon: the missing derivation

The degree-four weak del Pezzo identification is not just numerical. The genus-one ADE proof obtains \(K_M\sim-L\) and the crepant anticanonical model. The correction \(Z=L-c^\#\) lies in the \(D_5\) Picard lattice with \(Z^2=-2\); the exceptional-lattice saturation argument leaves only two configurations and shows \(2Z\) belongs to the exceptional lattice. Consequently \(2c\sim2H\) as Weil divisors on \(S\), an **actual Cartier equivalence**. This supplies a section \(Q\in H^0(S,2H)\) with entire divisor \(2c\). Any hypothetical mate restricts upstairs to a scalar power of \(Q\), but that does not assert that \(Q\) itself descends.

The complete anticanonical system has five sections and identifies \(S\) with a normal intersection of two quadrics in \(\mathbf P^4\). Restriction
\[
H^0(S,H)\longrightarrow H^0(c,\mathcal O_{\mathbf P^1}(4))
\]
is injective: a hyperplane section containing \(c\) would equal \(c\) by degree, making \(c\) Cartier and contradicting the nonzero exceptional correction. Both spaces have dimension five, so it is an isomorphism. The complete coordinates on \(c\) are therefore
\[
(Y_0,\ldots,Y_4)=(s^4,s^3t,s^2t^2,st^3,t^4).
\]
The given projection to the fixed \(C\subset\mathbf P^3\) **necessarily deletes \(Y_2\)**. Its center misses \(S\), because the original four sections generate \(H\).

The conductor can be computed without discarding its scheme structure. Writing \(z=Y_2\), suitable generators of the two-quadric ideal have the form
\[
Q_1=z^2-Az-R_1,\qquad Q_2=Lz+R,
\]
with \(A,L\) linear and \(R_1,R\) quadratic in the retained coordinates. Elimination gives the quartic equation \(R^2+ALR-R_1L^2=0\). The independent algebra proof identifies the **entire** conductor as \((L,R)\), including nonreduced fibers; it is not enough to use the reduced support. The section \(Q\) above defines an actual \((2,2,2)\) complete-intersection double of the rational normal quartic in \(\mathbf P^4\). Its arithmetic genus is five, so its square-zero nilideal is \(\mathcal O_{\mathbf P^1}(-6)\). Since the conormal bundle of the rational normal quartic in \(\mathbf P^4\) is \(\mathcal O(-6)^3\), every such embedded ribbon is encoded by a nonzero quotient direction. The source's explicit ribbon-net matrix
\[
M(d)=
\begin{pmatrix}
d_0&d_1&d_2\\
d_1&d_2+d_3&d_4\\
d_2&d_4&d_5
\end{pmatrix}
\]
has to annihilate that direction for each defining quadric. This turns the geometric classification into the five exhaustive binary-quartic root partitions discussed above. The full ideal certificates, direction boundaries and conductor-power obstruction remain in the [genus-one interface audit](../notes/2026-10-10-session-genus-one-interface-independent-audit.md) and [repeated-partition audit](../notes/2026-10-10-session-ribbon-repeated-partitions-independent-audit.md).

#### A four-(A_1) ADE projection family: numerical feasibility does not imply a mate

Over an algebraically closed characteristic-zero field, the normal degree-four del Pezzo
\[
S=V(ae-c^2,\ bd-c^2)\subset\mathbf P^4
\]
has exactly four \(A_1\) singularities. A four-parameter open \(\alpha\beta\gamma\delta(\alpha\delta-\beta\gamma)\ne0\) admits a smooth rational normal quartic \(c\subset S\) through all four singular points, with \(2c\sim2H\) and non-Cartier local class of order two at each singularity. Thus the genus-one numerical and torsion conditions can genuinely occur; they are not sufficient for a mate.

Projecting from the deleted-middle-coordinate center, which lies outside \(S\), gives finite birational integral quartics containing the **literal** \(C_0\). In the source's coordinates the eliminated equation is \(F=R^2-x_1x_2L^2\), with \(L\) linear and \(R\) quadratic. Along \(C_0\), \(L_C\) is a nonzero quartic whose endpoint values are nonzero, so every zero has \(UV\ne0\). At each such zero the normalization fiber contains two distinct points with middle coordinates \(z=\pm U^2V^2\), only one on \(c\). This violates full inverse support and excludes **every member of this specified parameter open in every mate degree**, including repeated-root subloci. It does not exhaust all four-\(A_1\) projections, other ADE configurations, or degenerate parameter boundaries. The construction illustrates why an ADE lattice condition, even with \(2c\sim2H\), is weaker than an actual fixed-carrier mate. [Explicit family and fiber proof](../notes/2026-10-09-session-singular-delpezzo-four-A1-family.md).

#### An (A_3+2A_1) projection family: four isolated inverse points

A second concrete genus-one ADE test is the normal degree-four complete intersection
\[
S=V(ab-c^2,\ cd-e^2)\subset\mathbf P^4.
\]
It has two \(A_1\) singularities and one \(A_3\) singularity. On the parameter open \(\gamma\delta(\alpha\delta-\beta\gamma)\ne0\), the five binary quartics
\[
a=s^2D^2,\quad b=t^2D^2,\quad c=stD^2,\quad d=stN^2,\quad e=-stDN,
\quad D=\gamma s+\delta t,\quad N=\alpha s+\beta t
\]
give a rational normal quartic: their coefficient determinant is \(\gamma^2\delta^2(\alpha\delta-\beta\gamma)^3\). Deleting its middle coefficient projects it isomorphically to the fixed \(C_0\), and the center lies outside \(S\). The resulting image is an integral quartic with finite birational normalization \(S\).

The extra inverse fibers are controlled by the actual quartic
\[
P_4=\gamma^4s^4-2\gamma^3\delta s^3t-2\gamma\delta^3st^3+\delta^4t^4.
\]
Its endpoint coefficients are nonzero. After rescaling, its polynomial is \(r^4-2r^3-2r+1\), with discriminant \(-1728\), so there are **four distinct nonendpoint zeros**. At each zero the projection line contains, in addition to the marked curve point, another point of \(S\) with nonzero middle-coordinate displacement \(\lambda=-2s^2t^2\). The extra inverse points are isolated because the projection is generically one-to-one along \(C_0\). Purity of the zero divisor of any pulled-back mate excludes **every carrier in this displayed family in every mate degree**. This does not classify all \(A_3+2A_1\) projections or all centers. [Explicit proof](../notes/2026-10-09-session-A3-two-A1-projection-family.md).

#### Reduced singular-support degree and singleton Hessian constraints

For an integral quartic surface \(X\subset\mathbf P^3\) in characteristic zero, let \(\Sigma\) be the **reduced one-dimensional support** of \(\operatorname{Sing}(X)\). A general plane section is an integral plane quartic of arithmetic genus three, and every transverse point of \(H\cap\Sigma\) contributes at least one to its normalization defect. Therefore \(\deg\Sigma\le3\); if \(X\) is nonnormal, \(1\le\deg\Sigma\le3\). A reduced planar cubic cannot occur: writing its plane as \(z=0\) and its squarefree cubic as \(g=0\), the vanishing of all first derivatives forces \(F=z(\lambda g+zQ_2)\), contradicting integrality. The degree-three reduced supports are therefore restricted to a twisted cubic, a meeting conic-plus-line, a chain of three lines with skew endpoints, or three concurrent noncoplanar lines. These are **support types**, not existence or normalization classifications.

The bound is **false for the Jacobian scheme degree**: the integral quartic \(F=x^2z^2+y^3w\) has reduced singular support two lines of total degree two but one-dimensional Jacobian scheme degree four. Separately, at a nonnormal surface point with a **singleton normalization fiber**, the local hypersurface Hessian has rank at most one; rank at least two would yield a formally split \(uv+g(w)\), which is either normal or has multiple normalization branches. These are necessary screening conditions, not quartic-carrier exclusions. [Support and Hessian proof](../notes/2026-10-08-session-singular-degree-and-singleton-hessian-audit.md).

### 3.2a Shared genus-two geometry and exhaustion

On the minimal resolution M of a genus-two normalization, the adjoint divisor f=K_M+L is a connected basepoint-free conic pencil. The actual exceptional correction Z satisfies q=-Z²>0, lambda=K_M.Z a nonnegative integer, q+lambda=4 and lambda²<=q. These force exactly two possibilities: (lambda,q)=(0,4) and (1,3). The bisection and trisecant cases are therefore exhaustive; an older assumption that q always equals four would miss the latter.

In the trisecant case the conductor line lies in the degree-three ruling of the unique smooth quadric containing C. Its intersection with C is described by a cubic with either three distinct roots or a triple endpoint root; the opposite endpoint is obtained by reversal. The normal ADE model is the strict transform in the blowup of the conductor line; **it is not the potentially non-Gorenstein normalization S**. The actual conductor retains split, singular and nonreduced covers. These are shared prerequisites, not additional unexamined case assumptions.

Sources: [genus-two adjoint audit](../notes/2026-10-09-session-genus-two-adjoint-independent-audit.md), [null-curve and correction audit](../notes/2026-10-09-session-genus-two-nullcurve-mate-independent-audit.md), [entire-conductor audit](../notes/2026-10-10-session-genus-two-entire-conductor-independent-audit.md), and [normal strict-transform audit](../notes/2026-10-10-session-genus-two-blowup-lift-normality-independent-audit.md).

#### Conductor line positions: the two strata have different geometry

In the genus-two blowup-lift framework, identifying the adjoint pencil with the pencil of planes through the reduced conductor line \(\Gamma\) gives the conditional scheme-length identity
\[
\tau=\operatorname{length}(C_0\cap\Gamma)=4-f\cdot c^\#.
\]
Thus the \(\lambda=0\) bisection stratum has \(\tau=2\), while the \(\lambda=1\) trisecant stratum has \(\tau=3\). This implication uses the **separate blowup-lift identification**; the elementary line-position classification below does not.

All trisecants lie in the degree-three ruling of the unique quadric and are \(\Gamma_\kappa=(x_2-\kappa x_0,x_3-\kappa x_1)\), together with \(\Gamma_\infty=(x_0,x_1)\). For \(\kappa\ne0,\infty\), the contact divisor consists of three distinct cube roots of \(\kappa\); at the two endpoints it is a single length-three fat point. **No trisecant has contact partition \([2,1]\)**, and no line meets \(C_0\) in length four.

The length-two positions are precisely ordinary secants not lying in the quadric and tangents at nonendpoint points. For finite distinct parameters \(a,b\), their secant lies in the quadric exactly when \(a^2+ab+b^2=0\), equivalently \(a^3=b^3\); for \(a=b\ne0\), the tangent has length two. Secants through infinity remain ordinary bisecants. These explicit boundary distinctions prevent treating a length-two conductor as a degenerate member of the trisecant ruling. [Full line-position calculation and conditional lift discussion](../notes/2026-10-10-session-genus-two-conductor-line-position.md).

#### Relative Morse splitting with labeled conductor branches

The nonendpoint trisecant argument uses a local assertion stronger than the abstract classification of Du Val singularities. In characteristic zero, suppose a completed surface germ has
\[
F=uv+r\,h(u,v,r)
\]
and the **specified** Cartier divisor \(r=0\) has reduced branches \((u,r)\), \((v,r)\). If the surface is smooth or Du Val, an \(r\)-preserving formal Morse iteration, with changes \(x\equiv u,\ y\equiv v\pmod r\), yields \(F=xy+g(r)\). If singular, \(g(r)\) has finite order \(m\ge2\); rescaling a unit gives \(xy=r^m\), preserving both branch ideals. Consequently the singularity is \(A_{m-1}\), not \(D\) or \(E\), and the **actual two branches** meet opposite ends of the minimal crepant exceptional chain. For \(A_1\), they meet the single exceptional curve at distinct points. This follows from the explicit toric resolution charts
\[
x=a_i^{i+1}b_i^i,\quad y=a_i^{m-i-1}b_i^{m-i},\quad r=a_ib_i
\quad(0\le i<m).
\]
The local statement was independently audited; it does **not** independently establish the global nonendpoint-trisecant hypotheses or exclusion. [Parameter-preserving proof](../notes/2026-10-10-session-relative-morse-conductor-branches-independent-audit.md).

### 3.3 Genus-two bisection: a global conormal contradiction

The genus-two normalization admits a second-pencil reduction, with bisection case denoted lambda=0 in the source. Under a hypothetical mate, the accepted conductor geometry produces an **actual Cartier double** R_C supported on the smooth lifted curve c. Its Cohen-Macaulay purity makes the nilideal J square-zero globally, not merely generically, and the source calculates J=O_C(-8). This is a genuine ribbon on the normalization, including its singular points.

The morphism from this ribbon to P3 induces a global conormal map N*_(C/P3) -> J. It is nonzero: away from the conductor line the normalization is an isomorphism, so the embedded ribbon generates its nilideal from the ambient curve ideal. For the fixed C in characteristic zero, N*_(C/P3)=O(-7) direct sum O(-7). Hence Hom(N*,O(-8))=0. Contradiction. This **global** argument excludes the whole bisection lane; the older quadratic-conductor chain remains a valid but weaker conditional analysis.

Source: [bisection independent proof and audit](../notes/2026-10-10-session-genus-two-bisection-full-independent-audit.md).

### 3.4 Nonendpoint trisecant: support and exceptional chains

In the lambda=1 trisecant stratum, the lifted curve is a section of the second ruling. A hypothetical mate forces **singleton inverse support at every conductor contact**: all points in the normalization fiber above a point of C must lie on the single lifted curve. On the normal conic model the exceptional divisor has bidegree (2,2); a distinguished horizontal component B has class (1,0). The audit exhausts multiplicity two on B, multiplicity one with reducible residual, and multiplicity one with integral residual.

In the integral residual case the residual has class (1,2), is a smooth rational graph over the ruling, and meets B in two transverse points. Exceptional corrections are then controlled by ADE chains at the contacts. The exact chain solution, with arbitrary chain lengths and all contact positions, contradicts the required correction budget. This is a universal positivity/intersection contradiction, not a finite search through short chains. The proof's independent symbolic replay supplements rather than replaces that argument.

Sources: [nonendpoint independent audit](../notes/2026-10-10-session-genus-two-nonendpoint-trisecant-continuation-independent-audit.md) and [owner's conic obstruction](../notes/2026-10-10-session-genus-two-nonendpoint-trisecant-conic-obstruction.md).

#### Explicit trisecant lines and the quartic linear system

For \(C_0=[s^4:s^3t:st^3:t^4]\), write \(q=x_0x_3-x_1x_2\) and
\(A=x_0^2x_2-x_1^3\), \(B=x_0x_2^2-x_1^2x_3\), \(D=x_2^3-x_1x_3^2\).
Every trisecant line lies on \(Q=V(q)\), since a line not contained in the quadric meets it in length at most two. The trisecant ruling consists of
\[
\Gamma_a=V(x_2-a x_0,x_3-a x_1),\qquad
\Gamma_\infty=V(x_0,x_1).
\]
The contact divisor for finite \(a\) is \(t^3-a s^3\). In characteristic zero over an algebraically closed field, nonzero \(a\) gives three distinct contacts and one orbit (represented by \(a=1\)); \(a=0,\infty\) give triple contact and are exchanged by reversal. Over a non-algebraically-closed field, nonzero parameters need not be equivalent: the scaling requires a cube root.

For finite \(a\), set \(u=x_0,v=x_1,z=x_2-a x_0,w=x_3-a x_1\) and \(T_a=D-2aB+a^2A=z^3+a u z^2-vw^2\). The exact homogeneous ideal is
\[
I(C_0)\cap(z,w)^2=(qz,qw,T_a).
\]
Consequently every quartic through \(C_0\) and double along \(\Gamma_a\) is
\[
F=qQ_2+T_aL_1,\quad Q_2\in(z,w)_2,\quad L_1\in k[x_0,x_1,x_2,x_3]_1.
\]
Here \((z,w)_2\) denotes the seven-dimensional degree-two part of the line ideal, **not** its three-dimensional square in degree two. The summands have dimensions seven and four and intersect trivially, so the vector space of quartics has dimension **11** (projective dimension **10**). On the quadric,
\[
\operatorname{div}(F|_Q)=C_0+2\Gamma_a+(Q\cap V(L_1)).
\]
The residual conic can degenerate into ruling lines; it must not be assumed integral.

A separate discriminant obstruction in the [original trisecant calculation](../notes/2026-10-10-session-genus-two-trisecant-quartic-carriers.md) is **conditional** on identifying the actual normalized conductor with the quadratic algebra on the ambient line blowup, together with the stated normality and contraction hypotheses. Under those hypotheses the discriminant must vanish at each contact; for \(\Gamma_1\), after imposing contact vanishing it takes the form \(4(v^3-u^3)[(c_0^2+b_0c_1)v+(b_0c_0-c_1^2)u]\). The argument excludes the nonzero-discriminant branch only under its lifting hypotheses. It does **not** settle identically-zero discriminant, endpoint triple contact, or the whole genus-two lane by itself. The chapter's separately sourced endpoint and nonendpoint analyses must not be conflated with this conditional calculation.

### 3.5 Endpoint trisecant: the full quartic family matters

At the endpoint, the conductor contact is triple, and the nonendpoint transversality argument cannot simply be reused. The owner first derives the **complete** quartic equation from the ideal identity I(C) intersect (x2,x3)^2=(q*x2,q*x3,D). Its exceptional polynomial is then exhausted by the four coefficient regimes c0 nonzero; a1 nonzero; a1=0 with b1 nonzero; and a1=b1=0 with c1 nonzero. The last regime includes doubled horizontal components, while the preceding regime includes triple residual contact and local A/D configurations.

The independent audit checks the coefficient-zero and doubled-component gaps, the two distinct residual intersections, triple-contact ADE corrections, and arbitrary ADE roots in the doubled-horizontal case. Each regime contradicts the mate correction identities. Reversal handles the opposite endpoint. A former argument restricted to irreducible residual curves was **not** an exhaustion proof and cannot stand in for these additional cases.

Sources: [full endpoint reduction](../notes/2026-10-10-session-genus-two-endpoint-full-quartic-reduction.md), [independent coverage audit](../notes/2026-10-10-session-genus-two-endpoint-full-independent-audit.md), [local ADE correction audit](../notes/2026-10-10-session-endpoint-local-ade-correction-audit.md), and [doubled-horizontal audit](../notes/2026-10-10-session-genus-two-endpoint-double-horizontal-independent-audit.md).

## 3.6 Two short proofs extracted from the genus-two sources

**Numerical dichotomy.** On the smooth rational resolution \(M\), let \(L\) be the pulled-back hyperplane class, \(c^\#\) the smooth strict transform of the curve, and \(Z\) the effective rational exceptional correction, so that \(c^\#\equiv L-Z\) and \(L\cdot Z=0\). The adjoint-pencil argument gives \(L^2=4\) and \(K_M\cdot L=-2\). Put
\[
q=-Z^2>0,\qquad \lambda=K_M\cdot Z\in\mathbf Z_{\ge0}.
\]
Negative definiteness of the exceptional lattice proves \(q>0\); the classification of its vertical and horizontal components gives \(\lambda\ge0\). Adjunction on \(c^\#\cong\mathbf P^1\) gives
\[
-2=(c^\#)^2+K_M\cdot c^\#
=(4-q)+(-2-\lambda),
\]
hence \(q+\lambda=4\). The exceptional intersection estimate gives \(\lambda^2\le q\). Consequently \(\lambda^2+\lambda\le4\), so \(\lambda=0\) or \(1\). The resulting pairs are \((0,4)\) and \((1,3)\). Moreover, for the conic pencil \(f=K_M+L\),
\[
f\cdot c^\#=2-\lambda,
\]
which is respectively a bisection or a section. The only inherited nontrivial inequality is the exceptional estimate \(\lambda^2\le q\); its proof and the classification of exceptional components remain in the [null-curve audit](../notes/2026-10-09-session-genus-two-nullcurve-mate-independent-audit.md).

**Bisection contradiction.** In the \(\lambda=0\) case, the second-pencil calculation yields the *linear*, not merely numerical, equivalence \(2c\sim2H\) on the normal surface \(S\). This is obtained by showing \(2Z\) integral in the exceptional lattice and using numerical-to-linear equivalence on the rational resolution. A section of \(\mathcal O_S(2H)\) therefore defines a Cartier double \(R_C\) with entire support \(c\). Since \(S\) is normal and hence Cohen–Macaulay, \(R_C\) is a pure Cohen–Macaulay curve of generic length two. Its nilradical \(J\) is generically square-zero; purity excludes a nonzero finite-support \(J^2\), so \(J^2=0\) everywhere. The same purity makes \(J\) torsion-free of rank one on the smooth rational \(c\), hence a line bundle.

The rational-resolution Riemann–Roch computation gives
\[
\chi(\mathcal O_S(mH))=1+2m^2+m.
\]
The Cartier sequence for \(R_C\) therefore gives
\[
\chi(\mathcal O_{R_C})=\chi(\mathcal O_S)-\chi(\mathcal O_S(-2H))
=1-7=-6.
\]
As \(\chi(\mathcal O_c)=1\), the reduction sequence gives \(\chi(J)=-7\), hence \(J\cong\mathcal O_{\mathbf P^1}(-8)\). The morphism \(R_C\to\mathbf P^3\) induces
\[
N^\vee_{C/\mathbf P^3}=I_C/I_C^2\longrightarrow J.
\]
This map is nonzero: off the conductor line the normalization is an isomorphism and the embedded double has nilideal generated by the ambient curve ideal. But the independently calculated splitting \(N^\vee_{C/\mathbf P^3}\cong\mathcal O(-7)^{\oplus2}\) gives
\[
\operatorname{Hom}\bigl(N^\vee_{C/\mathbf P^3},J\bigr)
=H^0(\mathcal O(-1))^{\oplus2}=0.
\]
This contradiction excludes the bisection stratum. It uses the entire Cartier double, not an assumed first infinitesimal neighborhood. The exact derivation of \(2c\sim2H\), the splitting calculation and the purity arguments are in the [independent bisection proof](../notes/2026-10-10-session-genus-two-bisection-full-independent-audit.md).

## 3.7 Characteristic-dependent cuspidal quartic: exact fixed-carrier mate degrees

Let \(k\) be algebraically closed, \(C_0=[s^4:s^3t:st^3:t^4]\), and fix the *particular* integral quartic cone
\[
X=V(F),\qquad F=x_0x_3^3-x_2^4.
\]
The normalization is \(\nu:\mathbf P(1,1,4)\to X\), \([s:t:z]\mapsto[s^4:z:st^3:t^4]\), induced by \(A=k[s^4,st^3,t^4,z]\subset k[s,t,z]\) with weights \(1,1,4\). It is finite, birational, and universally injective. The full inverse support of \(C_0\) is the Cartier divisor \(D=V(\phi)\), \(\phi=z-s^3t\), of weighted degree four.

A degree-\(N>0\) mate \(G\) exists on **this fixed carrier** precisely when \(\phi^N\in A\). Indeed the pullback of any such mate has support exactly \(D\); factoriality of \(k[s,t,z]\) and weighted degree force its pullback to be a scalar multiple of \(\phi^N\). Conversely, membership gives a homogeneous lift with exactly the required support.

For \(R=k[s^4,st^3,t^4]\), the monomial criterion is
\[
s^{3r}t^r\in R\quad\Longleftrightarrow\quad r\in\langle3,4\rangle
=\{0,3,4,6,7,8,\ldots\}.
\]
In characteristic zero, the coefficient \(-Ns^3t\) of \(z^{N-1}\) prevents descent for every \(N>0\). In characteristic \(p>0\), write \(N=p^eM\) with \(p\nmid M\). Frobenius and the first nonzero lower coefficient give the **exact criterion**
\[
\phi^N\in A\quad\Longleftrightarrow\quad p^{v_p(N)}\in\langle3,4\rangle.
\]
Thus the qualifying degrees are: characteristic \(2\), exactly \(4\mid N\); characteristic \(3\), exactly \(3\mid N\); characteristic \(5\), exactly \(25\mid N\); and prime characteristic \(p\ge7\), exactly \(p\mid N\). Minimum mate degrees are respectively \(4,3,25,p\). The characteristic-five exception comes from the semigroup gap \(5\), not a computational accident. If \(r=3b+4c=p^e\), set \(a=2b+3c\); the explicit mate \(x_0^a x_2^b x_3^c-x_1^r\) pulls back to \(-\phi^r\).

These are **all mate degrees for this fixed cone**, not global minima for the curve across all carriers; in particular the characteristic-five \((4,25)\) pair does not supersede a separately known \((3,20)\) presentation. The characteristic-zero conclusion is likewise only a fixed-carrier exclusion. [Source and proof](../notes/2026-10-05-positive-quartic-carrier-optimality.md).

## 4. Cartier singleton lifts: a necessary classification, not a construction

Under the stronger hypotheses that the entire reduced inverse image is a single curve \(c\cong C\) and **\(c\) is Cartier on the normalization**, R-0002 classifies the possible normalization/polarization pairs. The mate makes \(c\) ample, and \(|c|\) realizes a normal surface of minimal degree. The proof uses the Cartier restriction sequence, surface classification and the singular cone case.

For the fixed quartic \(C_0\), after excluding quartic carriers, three necessary higher-degree models remain:

| Carrier degree | Normalization | Polarization and lift |
|---|---|---|
| \(8\) | \(\mathbf P^1\times\mathbf P^1\) | \(H=(2,2)\), \(c=(1,1)\) |
| \(8\) | Quadric cone | \(H=2c\), \(c\) a smooth Cartier conic |
| \(16\) | \(\mathbf P^2\) | \(H=\mathcal O_{\mathbf P^2}(4)\), \(c\) a line |

These are **necessary candidates only**. One must still produce an admissible projection, verify full inverse support, and solve conductor descent. Non-Cartier lifts, multiple inverse branches and other carriers lie outside this classification.

**Source:** [R-0002](../results/cartier_singleton_lift.md), [proof](../notes/2026-10-14-generalization-cartier-lift-minimal-degree.md), and [independent audit](../notes/2026-10-14-generalization-cartier-lift-independent-audit.md).

## 5. Projection phases: reducing a family without solving it

R-0004 considers finite-type families of projections of such normalizations, subject to basepoint-freeness, finite birationality and full inverse support. After stratification and a finite cover, the conductor data define a phase morphism into a torus. A carrier admits a mate precisely when its phase is torsion. Laurent's theorem constrains the torsion points to a finite torsion-coset envelope.

This does **not** calculate the phase image for the three candidate normalizations, nor imply that an admissible torsion phase exists. Nilpotent conductor constraints and excluded parameter boundaries remain part of the problem.

The explicit plane-normalization family in R-0017 is an instructive counterweight: it has finite birational maps and the correct full singleton inverse support, but a first-order conductor obstruction prevents a mate in every degree **for that family**. Thus correct inverse support is not sufficient for descent, and the example does not exclude all degree-sixteen plane projections.

**Sources:** [R-0004](../results/projection_phase_reduction.md), [R-0017](../results/singleton_plane_conductor_descent.md).

## 6. Normal carriers: local Cartier indices and socle compatibility

A separate restriction arises when \(X\) is **normal** and a mate cuts a multiple \(nC\) on it. At a point \(P\in C\), let \(r\) be the actual local Cartier index of \(C\) on \(X\), with \(n=kr\). The local power/socle identity of R-0034 reads
\[
D_{n,P}=(k-1)A_{F,P}+kD_{r,P},
\qquad
2\sum_i\operatorname{length}(T_i)_P=nD_{n,P},
\]
under its curvilinear complete-intersection and filtration hypotheses. Here the \(T_i\) are torsion in the ordinary conormal-power layers. The **actual Cartier index is not surface multiplicity**; substituting one for the other invalidates the argument.

For \(C_0\), R-0035 combines these constraints with the normal-carrier torsion reduction, the low-degree carrier exclusion and the inherited P-010 quadratic-direction obstruction. The result excludes normal integral carriers with a mate **when every on-curve local Cartier index is at most four**. Indices six, twelve and higher are not excluded by this theorem, and the result says nothing about nonnormal carriers.

The inherited P-010 calculation comes from the two embedded charts of \(C_0\), not merely abstract splitting of its conormal bundle. Its finite-direction class is
\[
h_\theta=3\theta^3z^{-5}-\frac32\theta^2z^{-4}
+\frac34\theta z^{-3}-\frac38z^{-2}\in H^1(\mathcal O(-7)),
\]
and the remaining direction gives \(3z^{-5}\). Both are nonzero in characteristic zero. The index/socle audit treats these coefficients as **previously accepted inputs**, not as a fresh verification.

**Sources:** [R-0034](../results/normal_carrier_index_socle.md), [R-0035](../results/normal_carrier_bounded_index_exclusion.md), [normal-carrier torsion proof](../notes/2026-10-14-generalization-normal-carrier-torsion.md), [index/socle independent audit](../notes/2026-10-14-generalization-index12-filtered-compatibility.md), and [historical P-010 derivation](../RESEARCH_RECORD.md).

## 7. The remaining carrier problem

The preceding arguments do not show that \(C_0\) is not a set-theoretic complete intersection. They leave, among other things, higher-degree integral carriers; nonnormal carriers outside the quartic classification; normal carriers with larger local indices; and Cartier singleton projection families whose admissible conductor phases are not determined.

The natural research order is: understand the possible inverse support and divisor class on the normalization; compute the **full** conductor descent obstruction; then test whether a mate can exist. This avoids treating a successful normalization model, a numerical relation, or a reduced phase calculation as an actual STCI construction.

The [quartic-carrier technical appendix](QUARTIC_CARRIER_TECHNICAL_PROOFS.md) now preserves the genus-one exact algebra, nonendpoint all-length inequality, and endpoint ADE/doubled-horizontal budget in a compact permanent home. It identifies source calculations still requiring retention.

## 8. Proof preservation and consolidation decisions

This section is a **claim-level editorial disposition**, not permission to delete the supporting source files. The permanent exposition now contains the theorem statement, shared reductions, and decisive mechanism of each lane. What follows identifies the material that remains mathematically necessary for reconstructing those proofs.

| Claim / proof component | What this chapter now preserves | What still requires an exact technical proof | Disposition |
|---|---|---|---|
| Shared nonnormal reductions | Generic regularity, rationality, full inverse support | Ruled intersection with infinitely near multiplicities; purity and normalization-fiber arguments | Retain source as technical proof |
| Normal quartic exclusion | Scope and global exceptional-cycle strategy | Reduced and nonreduced graph enumerations, necessary-superset argument, final exceptional passage | Retain both audit/proof sources |
| Genus zero | Vanishing, six sections, minimal-degree classification, singular cone class-group argument | All-scroll and Veronese universal exclusions; cone exceptional correction | Retain technical proofs |
| Genus one | ADE degree-four del Pezzo, forced projection center, Cartier ribbon, five partitions | Entire-conductor algebra, complete ribbon net, universal ideals for [4], [3,1], [2,2], direction boundaries | Retain complete proof and exact validation |
| Genus two shared | Adjoint pencil, two numerical strata, actual ADE strict transform | Null-curve classification, full conductor algebra, normality and correction lemmas | Retain upstream proofs |
| Genus-two bisection | Full ribbon and global conormal-map contradiction | Cartier-double and nilideal derivation; independent normal-bundle calculation | Retain exact proof |
| Genus-two nonendpoint | All effective decompositions and all-length exceptional-chain contradiction | Complete divisor case split, chain equations and contact inequalities | Retain exact proof |
| Genus-two endpoint | Four coefficient regimes and complete ADE/doubled-horizontal exhaustion | Quartic ideal identity, local A/D correction equations, doubled-horizontal arbitrary-root argument | Retain exact proof |
| Final degree bound | Coprime factor reduction, quadric class, independent cubic exclusion | Primary cubic source and no-circularity evidence | Retain proof audit |

### Where the detailed mathematics should live

A **permanent proof section** is appropriate for arguments whose content is concise and structurally central: the normalization divisor-degree calculation; the factor reduction; the genus-two numerical dichotomy; and the global bisection conormal contradiction. These can be expanded and checked directly in this chapter without reproducing whole historical sessions.

A **technical appendix** is appropriate for long but reusable computations: the genus-one universal ideal and conductor certificates, normal-quartic exceptional graphs, nonendpoint all-length chain solutions, and endpoint ADE/doubled-horizontal calculations. Such an appendix should preserve exact formulas, hypotheses, and independently checked computational evidence, not merely a PASS label.

An **audit/evidence record** remains appropriate for independent replays, failed scripts, corrections, primary-source verification, and the assembly audit's attribution. These are evidence about the proof rather than the mathematical exposition itself. They should remain reachable from the permanent proof or appendix; a passing bounded computation is not a substitute for the universal argument.

### What is and is not redundant

The [quartic-carrier dependency graph](../MATHEMATICAL_CONSOLIDATION_QUARTIC_CARRIER_DEPENDENCIES.md) and the six-lane table in Section 3 overlap in *orientation*, but the graph still provides a compact dependency map. They are candidates for eventual navigation consolidation, **not** proof deletion.

The older [irreducible-residual endpoint note](../notes/2026-10-10-session-genus-two-endpoint-irreducible-conic-obstruction.md) is mathematically narrower than the full endpoint reduction: it cannot be used as an exhaustive proof. Its unique calculations should be checked against the full reduction before it is considered redundant. Likewise, the [earlier bisection quadratic-descent note](../notes/2026-10-10-session-genus-two-bisection-quadratic-descent.md) provides a weaker conductor route; its conditional content is not automatically disposable because the global conormal contradiction is stronger.

**No deletion decision is justified solely by a newer theorem's stronger conclusion.** The criterion is whether a historical source contains a unique valid argument, counterexample, hypothesis check, computation, or useful failure explanation absent from the retained permanent material.

### Immediate proof-integration order

First, write the short intrinsic arguments directly into the chapter and check their hypotheses. Second, prepare one quartic-carrier technical appendix organized by the six lanes, with links to original exact proofs. Third, compare each historical source against the appendix claim by claim and record any genuinely unique content. Only then consider retiring duplicated narrative files; preserve the canonical R-0001 theorem and independent audits throughout.

## Editorial and verification status

**Critical review, pass 1:** checked all 16 relative Markdown links against the complete working-branch Git tree: all resolve. Corrected a material overgeneralization in Section 1: the coefficient of the singleton lift in the pulled-back mate divisor is \(n=b\deg X/\deg C\), and equals the mate degree only for quartic carriers of the degree-four curve. Also made explicit why a proper STCI pair has no common surface component. The rest of the chapter has been compared at the statement/scope level with R-0001, R-0002, R-0003, R-0004, R-0017, R-0034 and R-0035; this is **not** an independent audit of the original proofs.

This is the **first permanent-chapter draft**. It integrates accepted statements and the geometric reasons for their scope, while linking rather than duplicating long source proofs. It has not been independently proof-audited; it is **not yet a replacement for canonical R-records or their underlying evidence**. Before retiring historical files, each six-lane proof and each conductor/index lemma must be compared for unique content, and the chapter's references and hypotheses checked line by line.

## 9. Generic nonimmersion and four MF6 boundary carriers

The generic nonimmersion-prime lemma in [the original proof](../notes/2026-10-08-session-nonimmersion-prime-independent-audit.md) applies to a finite birational map from a smooth projective surface, a smooth lifted divisor c linearly equivalent to the pullback polarization H, an immersion on c, and a mate pullback equal to a nonzero scalar times the nth power of the defining section of c, with n nonzero in the ground field. Every distinct integral curve E with positive H-intersection must be generically immersive. The proof uses vanishing derivative minors along E, a unit-pivot kernel vector, and cancellation of the nonzero section in the local domain of E *before* evaluating at a point of E intersect c. It does not apply when the characteristic divides n or to isolated rank-drop points.

The [four explicit nonnormal MF6 boundary carriers](../notes/2026-10-07-session-nonnormal-mf6-independent-audit.md) are excluded in every mate degree in characteristic zero. Their affine finite normalization has a unique reduced lifted quartic and a duplicated fiber whose two points impose a root-of-unity equation on any descending mate power. The relevant quadratic parameter has norm 1/3, contradicting that equation. This is a fixed-carrier statement about four specified quartics, not a general nonnormal exclusion or an exclusion of all pencil members.

The [ordinary pinch and nodal conductor analysis](../notes/2026-10-07-session-nonnormal-structural-progress.md) proves transversality for an immersed lifted curve at an ordinary pinch. Under explicit ordinary-singularity assumptions this yields a four-versus-six scroll conductor count and a six-point Roman Veronese no-conic obstruction. A separate nodal-conductor local model admits smooth embedded image curves of arbitrarily high conductor contact, so reduced branch counts cannot be used without the ordinary hypotheses.

These arguments are incorporated as source-preservation statements, not independently certified new theorems. The Veronese Jordan classification and Mumford numerical-pullback proof still need detailed integration.

## 10. Numerical self-intersection versus normal degree: provisional

The [Step 1C Mumford-bound review](../synthesis/phase2_step1c_mumford_numerical_bound_review.md) preserves the proposed inequality between the numerical self-intersection of the lifted curve and its normal degree on an integral carrier generically regular along that curve. It records the exceptional-cycle defect, the ordinary-node half-unit contribution, and the conditional split-sextic Jacobian restriction. **Independent audit is still required**; the bound is not promoted here as a new canonical theorem. In particular the identically-zero polynomial branch remains separate.

## Exact genus-two trisecant carrier linear system

For the fixed rational quartic on `Q=(x0*x3-x1*x2=0)`, every trisecant line lies in the ruling meeting C in length three. It is `Gamma_a=(x2-a*x0,x3-a*x1)` for finite `a`, or `Gamma_infinity=(x0,x1)`. The intersection divisor on C is `t^3-a*s^3`; over an algebraically closed characteristic-zero field, the two ambient types are three distinct contacts (`a!=0,infinity`) and a triple contact (`a=0,infinity`). Over a nonclosed field, diagonal scaling may not identify nonzero parameters without cube roots.

Put `z=x2-a*x0`, `w=x3-a*x1`, `q=x0*x3-x1*x2`, `A=x0^2*x2-x1^3`, `B=x0*x2^2-x1^2*x3`, `D=x2^3-x1*x3^2`, and `T_a=D-2*a*B+a^2*A`. The exact homogeneous ideal of forms containing C and double along Gamma is `I(C) intersect (z,w)^2=(q*z,q*w,T_a)`. Its quartic space is `F=q*Q2+T_a*L0`, where `Q2` is quadratic in `(z,w)` and `L0` is an ambient linear form; dimensions are 7+4=11. On Q, `div(F|Q)=C+2*Gamma+(Q intersect (L0=0))`. The residual conic may degenerate and must not be discarded. These ideal and dimension statements are unconditional within the fixed-curve setup; see [the source proof](../notes/2026-10-10-session-genus-two-trisecant-quartic-carriers.md).

The source's subsequent discriminant and correction-cycle exclusion requires the **actual normal ambient-line-blowup realization** and conductor identification; it is not a free-standing proof from the ideal calculation. In the three-contact case the discriminant at each `r^3=1` is a square; requiring vanishing at all contacts gives `a0=2*c1`, `a1=-b0`, `b1=2*c0`, and then `Delta=4*(v^3-u^3)*((c0^2+b0*c1)*v+(b0*c0-c1^2)*u)`. The nonzero-discriminant graph argument is conditional on that realization and does not address the identically-zero discriminant or endpoint line within this source. Later audited genus-two exclusions belong to the complete carrier theorem; do not confuse this conditional historical argument with their proof status.
