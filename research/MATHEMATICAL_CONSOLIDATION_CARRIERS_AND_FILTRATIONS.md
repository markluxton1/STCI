# Mathematical consolidation: normal carriers versus first-relation defects

**Status:** thematic synthesis, not a new theorem. Read canonical R-0003, R-0013, R-0016, R-0034, R-0035 and their principal proof/audit sources.

## Two genuinely different entry points

**First-relation/filtered-algebra route.** Given an actual lci thickening supported on C and a full generic ordinary binary CI (f_r,g_s), study the actual first relation K_r in Sym^r N^*. In R-0013, K_r is saturated: a global actual-generator sequence is nonsplit, both equations have exact generic order r, and movement epsilon=1 is impossible for C0. In R-0016, K_r=R(-D) need not be saturated: a quotient resultant produces an effective divisor Delta with degree (r-1)c_(s-1)-r c_s and upper bound (r-1)binom(s-r,2)length(D). For gap <=2 normal flatness follows under the full hypotheses. A nonsaturated first relation can pay for degenerations; it cannot simply be discarded.

**Carrier/divisor descent route.** Fix an integral surface X containing C. R-0003 treats an integral Cohen–Macaulay carrier with finite normalization and no isolated inverse-support points: a mate exists exactly when the full conductor descent lattice has a vector strictly positive on every inverse branch. The criterion is not an effective classification of all carriers. When X is normal, the conductor disappears and the obstruction becomes torsion of the class mu[C]-v[H], where mu=a/gcd(a,4), v=4/gcd(a,4). The normal-carrier source proves that the torsion order is detected by local class groups on C under the rational ample-Cartier-multiple hypothesis. R-0034 then relates the **actual local Cartier index** r (not the surface multiplicity) to ordinary socle defects for a mate nC: D_n,P=(n/r-1)A_F,P+(n/r)D_r,P. R-0035 excludes normal carriers whose on-curve local indices are all <=4, with inherited torsion and quadratic-direction inputs. Higher indices, nonnormal carriers, and entirely-thick cases remain outside this result.

## Intrinsic genus-one quintic (A_4) pair and its projection-center modulus

This is an intrinsic classification under the **genus-one, degree-five anticanonical del Pezzo, unique \(A_4\), characteristic-zero** hypotheses, not a quintic mate exclusion. Let \(S\) have \(5c\sim4H\), unique degree-one line \(\ell\) with \(5\ell\sim H\), and \(c+\ell\sim H\). On the minimal resolution the \(A_4\) chain \(R_1-R_2-R_3-R_4\) meets \(c^\#\) at \(R_2\) and \(\ell^\#\) at \(R_3\). Successively contracting \(\ell^\#,R_3,R_2,R_1\) yields \(\mathbf P^2\). Reversing the contractions gives a length-four infinitely-near cluster locally equivalent to \((y-x^3,x^4)\), with fourth center off the neighboring exceptional curves. The conic class \(c^\#=2h-e_1-e_2\) consists of equations \(Ayz+Bx^2+Cxy+Dy^2=0\), smooth precisely when \(AB\ne0\). The cluster stabilizer acts transitively on these smooth conics, so the polarized intrinsic pair \((S,c)\) has one isomorphism class, represented by \(yz+x^2=0\).

After fixing this conic, the full pair automorphism group is the additive translation group \(\mathbf G_a\), acting by
\[
(x,y,z)\longmapsto(x+by,y,z-2bx-b^2y).
\]
On the rational-normal parameter \(r=s/t\) it acts by \(r\mapsto r+b\); it does **not** contain a residual scaling. The anticanonical system has six plane-cubic generators
\[
yz^2-x^3,\ xyz,\ y^2z,\ x^2y,\ xy^2,\ y^3.
\]
With the coordinate choices in the [intrinsic classification source](notes/2026-10-11-session-dp5-a4-intrinsic-pair-classification.md), the lifted curve is the complete rational normal quartic, the unique line is its tangent at the \(A_4\) endpoint, and there are actual sections with divisors \(c+\ell\), \(5\ell\), and \(5c\) (the last in \(4H\)). These are sections on \(S\), **not** automatically descended equations on a four-coordinate projected carrier.

A center in the \(\mathbf P^4\) span of \(c\) projects the rational normal quartic to \(C_0\) exactly when its associated binary quartic has two distinct double roots. Modulo translations there are **two lanes**: an endpoint lane (one double root at the fixed \(A_4\) point), with one orbit represented by the deleted-middle-coordinate center; and a nonendpoint lane, with finite double roots \(\pm\delta\), \(\delta\ne0\), modulo \(\delta\sim-\delta\). A representative nonendpoint center is
\[
p_\delta=(1,0,-\delta^2/3,0,\delta^4),
\quad\Phi_{p_\delta}(Z)=(Z-\delta)^2(Z+\delta)^2.
\]
There is no pair automorphism that normalizes every nonzero \(\delta\) to one. For each fixed center, line extensions to a projection from \(\mathbf P^5\) retain four parameters, and admissibility still requires avoidance of \(S\), finite birationality, and **full inverse support**. Thus an endpoint-only computation is not an exhaustion of genus-one quintic projections. Actual conductor descent in both lanes remains open. [Proof and complete formulas](notes/2026-10-11-session-dp5-a4-intrinsic-pair-classification.md).

## Rational-resolution denominator compression: a conditional degree bound

For a normal integral degree-\(a\) carrier \(S\subset\mathbf P^3\) with **rational smooth resolution** \(\sigma:M\to S\), let \(C\subset S\) have degree \(\delta\), strict transform \(c\), and numerical exceptional correction \(Z\). If a mate exists, its divisor is \(rC\sim bH\) with \(r\delta=ab\), and the numerical pullback is \(c+Z\equiv(\delta/a)H\). Let \(n\) be the least positive integer clearing the coefficients of \(Z\) and \(\delta/a\). Since the Picard group of a smooth rational projective surface is torsion-free and numerical equivalence agrees with linear equivalence, the integral numerically trivial divisor
\[
n((\delta/a)H-c-Z)
\]
is principal. Pushing down yields \(nC\sim(n\delta/a)H\) as an actual Cartier relation, and hypersurface restriction lifts its canonical section to an ambient mate of degree \(n\delta/a\). Conversely any mate clears these denominators. For \(a=\delta=4\), **\(n\) is the least mate degree on this fixed normal quartic**, conditional on the rational-resolution and mate hypotheses.

For the classified rational-resolution normal quartic possibilities with \(K_M=-E\), set \(d=-E^2\in\{1,2,3\}\), \(A_{ij}=-E_iE_j\) for all exceptional primes, and \(E=\sum a_iE_i\). Minimality and adjunction give
\[
\sum_i(b_i-2)_+\le d,\quad b_i=-E_i^2,\qquad
r\le9+d.
\]
Hadamard's inequality gives \(\det A\le2^r(3/2)^d\le512\cdot3^d\). The correction denominator divides \(\det A\), hence the conditional least mate degrees obey \(n\le1536,4608,13824\) for \(d=1,2,3\) respectively. This was a genuine **finite-degree reduction**, not a coefficient enumeration. The subsequently accepted all-degree quartic exclusion R-0001 supersedes it as an exclusion statement, but not its rational-Picard mechanism. It does **not** extend to nonnormal carriers or higher-degree carriers. An illustrative cusp-cycle correction with denominator two is thereby excluded as mate-compatible by the unique-quadric obstruction, without asserting that the numerical cycle is realized by a smooth curve. [Derivation](notes/2026-10-06-normal-rational-carrier-compression.md).

## Quadratic-root second obstruction: chart-free dual compression

For a basepoint-free binary quadratic \(f=a(z)u^2+b(z)uv+c(z)v^2\) of base degree two, the second ambient obstruction has a **global dual presentation** that avoids choosing an invertible coefficient chart. The transpose multiplication map
\[
T_f=\begin{pmatrix}a&b&c&0&0\\0&a&b&c&0\\0&0&a&b&c\end{pmatrix}:
\mathcal O_{\mathbf P^1}^{5}\longrightarrow\mathcal O_{\mathbf P^1}(2)^3
\]
is fiberwise surjective; \(W=\ker T_f\) has rank two and determinant \(\mathcal O(-6)\). Its degree-ten twist has \(h^0(W(10))=16\), and the canonical map \(H^0(\mathcal O(4))^5\twoheadrightarrow H^0(W(10))\) is surjective with nine-dimensional kernel. Thus **25 polynomial pairings test all 16 obstruction coordinates**, including coefficient splitting-jump loci, with no chosen minor or 39 auxiliary inverse variables. The columns of the skew \(5\times5\) matrix of signed complementary maximal minors of \(T_f\) generate \(W(6)\), giving a polynomial global test.

This is a complete representation of the **second obstruction**, not proof that its zero scheme is empty or that the first obstruction vanishes. The original construction also retains the actual embedded chart and the smoothness discriminant of the binary quartic; do not infer a universal exclusion by testing a generic coefficient chart alone. [Global dual construction](notes/2026-10-15-generalization-quadratic-root-global-second-dual-compression.md).

## Elliptic root-curve torsion and the second obstruction locus

On the smooth \((2,2)\) root-curve open \(U_{\rm sm}\subset\mathbf P^8\), put \(A=\mathcal O_Z(1,0)\), \(B=\mathcal O_Z(0,1)\), and \(\eta=B\otimes A^{-1}\in\operatorname{Pic}^0(Z)\). The two ruling deck involutions satisfy \(\iota_B\iota_A(p)=p+\eta\); thus the torsion order of \(\eta\) is the order of a **canonical translation** on the elliptic root curve. For each fixed \(n\ge2\), the \(n\)-torsion locus is a smooth codimension-one relative-Picard locus on \(U_{\rm sm}\) in characteristic zero. It is not automatically transverse to a compatibility or obstruction scheme.

For \(n=2\) there is a concrete determinantal equation: if \(f=a(z)u^2+b(z)uv+c(z)v^2\), then \(\eta\) has exact order two on the smooth open iff
\[
\det\begin{pmatrix}a_0&a_1&a_2\\b_0&b_1&b_2\\c_0&c_1&c_2\end{pmatrix}=0.
\]
At the specified seed \(f_0=(z^2+4)u^2+(z^2-8)v^2\), the accepted first compatibility component \(C\) is smooth four-dimensional, and the explicit tangent \(\delta f=zuv+4v^2\) evaluates the determinant differential to \(12\). Hence \(C\) meets the order-two divisor transversely, in a three-dimensional local branch \(D\). The canonical second obstruction \(\sigma_2\) is nonzero at the seed; its zero locus on this irreducible \(D\) has dimension **at most two**. The same local bound applies to the even-order torsion component through this seed, including orders eight and twelve.

This is a rigorous **local dimension bound on one torsion branch**, not a proof that the entire second obstruction locus is empty, not a statement about other torsion components, and not a reduction of unbounded torsion orders to finitely many. [Torsion and second-zero geometry](notes/2026-10-15-generalization-quadratic-root-torsion-second-zero-geometry.md).

## Universal quadratic root incidence and its nonzero second obstruction

In characteristic zero, consider a moving quadratic first relation of movement two
\[
f=a(z)u^2+b(z)uv+c(z)v^2,\qquad \deg a,\deg b,\deg c\le2,
\]
on the basepoint-free open \(U\subset\mathbf P^8\). The root divisor \(Z_f\subset\mathbf P^1\times\mathbf P^1\) is finite flat of degree two over the base, including singular or nonreduced members. The **actual embedded-chart** first ambient class is represented by \(d_f=\operatorname{pr}(D_uf_u+D_vf_v+\alpha f_z)\), with the base-motion term retained, modulo multiplication by \(f\). Its universal \(16\times12\) multiplication matrix \(A_f\) is injective on \(U\); therefore the first compatibility scheme is exactly
\[
K=\{[f]\in U:\operatorname{rank}[A_f\mid d_f]=12\},
\]
defined by the \(13\times13\) minors of one \(16\times13\) matrix. The correcting vector is unique on \(K\).

The explicit smooth elliptic seed \(f_0=(z^2+4)u^2+(z^2-8)v^2\) satisfies the first class. Its first-incidence Jacobian has a nonzero \(16\times16\) minor \(-405\), so \(K\) is smooth of dimension four at \([f_0]\). Moreover the ruling-difference class \(\eta=\mathcal O_{Z_0}(0,1)\otimes\mathcal O_{Z_0}(-1,0)\) has **exact order two**. Thus actual first ambient compatibility and spectral torsion coexist on a positive-dimensional smooth-root family: neither condition alone excludes the moving-root geometry.

The **second** ambient class, relevant when the independent second relation has degree \(s>4\), lives in the rank-sixteen cokernel
\[
\operatorname{coker}\big[H^1(\mathcal O(-14,2))\xrightarrow{\cdot f}H^1(\mathcal O(-12,4))\big].
\]
Retaining nonlinear base motion and the first equation-unit correction, the explicit seed's quartic residual \(R_4\) admits the Serre-dual functional
\[
\lambda(R_4)=[z^{-1}](-c\,r_1+a\,r_3)=\tfrac18\ne0.
\]
The sparse dual vector \((0,-c,0,a,0)\) annihilates the entire multiplication image. Hence the second obstruction is **nonzero at the very seed that passes the first and torsion tests**. Uniqueness of first corrections makes the second class a canonical section of a rank-sixteen vector bundle on \(K\), not an unrelated test. It is nonzero generically on the component through the seed, but its complete zero scheme remains undetermined. The result applies to actual complete intersections only under the separate actual-CI-to-root-curve bridge; it does not exclude every root divisor or the \(s=4\) lane. [Universal first incidence](notes/2026-10-14-generalization-quadratic-root-universal-incidence.md), [second-class certificate](notes/2026-10-14-generalization-quadratic-root-second-obstruction.md).

## Important interface: ordinary versus saturated filtration

The independent index/socle audit proves that, for a curvilinear actual CI thickening, the torsion-free **ordinary** layers are powers B_i=B_1^i, and 2 sum length(T_i)_P=n D_n,P. This does not assert that the **saturated** BF layers have trivial multiplication divisors. The first-relation resultant theorem instead uses the saturated filtration and its generation defects. Confusing the two makes apparent contradictions and invalid shortcut exclusions.

## Mathematical failures worth retaining

- Substituting carrier surface multiplicity for actual Cartier index invalidates the local formula.
- Using torsion-free Cl(X) to argue that no mate exists requires the rational-curve/low-degree carrier argument; it is not merely a local Picard claim.
- Claiming the bounded-index exclusion for indices 6,12 or higher is unsupported.
- Extending the resultant formula beyond a full generic binary CI or to residual-component intersections is unsupported.
- Treating a numerical defect budget as global realizability or nonexistence is unsupported.
- Treating normalization/conductor descent as an effective general algorithm is unsupported.

## Architectural decision

Keep **two subject chapters**: (1) *Normal relations and filtered thickenings*, (2) *Carriers, normalization and conductor descent*. Add a short shared interface on ordinary/saturated filtrations, local Cartier indices and socle defects. Do not merge them into one putative obstruction theorem. Canonical R records remain independent scoped theorem authority. Cross-link examples where both frameworks apply; do not assume a universal translation.

## Next content review

Review the remaining carrier results R-0002, R-0004, R-0017 and the legacy `results/normal_carrier.md` and `results/entirely_thick.md`. Identify the conceptual difference between fixed-carrier descent, phase reduction, and entire-thick cases before deciding which older syntheses to fold into the chapters.


## Degree-obstruction audit (theme 5, continuation)

The strongest global degree exclusion is **R-0001**: every integral quartic carrier of the *fixed* C0 in characteristic zero has no mate of **any** positive degree, whether normal or nonnormal. Its accepted proof assembles normal quartics and nonnormal plane-sectional genus 0,1,2 cases; the source acceptance and independent dependency audit should remain linked. Factor reduction, together with plane/quadric/cubic exclusions, implies both degrees of any hypothetical STCI presentation are at least five, including reducible defining forms. For a quintic carrier the mate degree is divisible by four (first possible degree eight). Do not misstate R-0001 as excluding arbitrary quartic forms without applying factor reduction.

**R-0022** is a mathematically distinct, narrower (4,4) proof via saturated Gorenstein filtration and contact-space classification; its alternate K3 resolution argument is retained as a valid independent route, not made the main approach. It adds insight into why length four cannot be achieved by the relevant quartic pencils but does **not** strengthen the all-degree exclusion R-0001.

The legacy **normal_carriers.md** records useful earlier geometric classification and failure modes (rational versus nonrational singularities, ADE budget, simple elliptic exclusion, Ishii–Nakayama types, finite degree bound). Its historical open cases are **not current open quartic-mate cases** after R-0001. Preserve the classification ideas, not obsolete frontier labels.

The legacy **quartic_e2.md** records an important failed shortcut: primitive e=2 quadruples **do exist**, contrary to an earlier blanket exclusion. The actual result is that their canonical primitive triples force all containing quartics to factor, excluding only specified (4,7) and (4,8) branches by that argument. The all-quartic theorem now subsumes these as mate exclusions, but does not erase their structural significance.

The legacy **order_one.md** gives conditional quasiprimitive/BF numerical restrictions (0<=e<=6 generally under its hypotheses; 0<=e<=2 for quartic order-one carriers). The **entirely-thick** branch lies outside it. These are useful inputs to the normal-filtration chapter, not unrestricted global exclusions.

The legacy **normalization_conductor.md** provides the fixed-carrier inverse-support obstruction: an isolated point in the full reduced normalization preimage excludes a mate. When all nonnormality is supported on C, an effective Cartier divisor upstairs with appropriate positive polarization is sufficient after a high conductor power. This **special support-contained sufficiency** must not be conflated with the full-conductor descent lattice of R-0003 in general.

### Remaining audit targets

For global intersection/incidence theme 6, review universal plane-family W_osc/W_bit, degree formulas, and fixed-boundary deformation records; for theme 7, map each exact computational witness to its theorem or provisional claim. This pass reviewed the **canonical statements and selected source descriptions**, not independently rerun all historical quartic exclusion proofs.
