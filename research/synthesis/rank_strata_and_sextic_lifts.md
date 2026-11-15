# Geometric incidence and degeneracy loci for actual sextic lifts

**Status:** independently reviewed mathematical contribution. The general statements are proved below by linear algebra over rings. The sextic application inherits the reviewed characteristic-zero source and coefficient identifications in [the conditional sextic calculation](normalization_conductor_phase2_addendum.md); those computations were not rerun.

The curve in the application is the fixed embedding
\(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\) over an algebraically closed field of characteristic zero. The relevant carrier lane is the conditional degree-(6,16), full generic coprime normal CI-(2,12), actual saturated movement-two first-relation lane. These hypotheses do not classify arbitrary pairs. Properness and sole support are separate from every finite lifting test below.

## Geometric orientation: the space of equations over the space of roots

The geometric object is an incidence scheme over a parameter space of
possible normal roots and auxiliary data. Its points are not arbitrary
normal coefficients: they represent actual homogeneous sections
satisfying prescribed compatibility conditions. A bundle map records
these conditions, and a target section records the requested lift.

Where the map has constant rank in the scheme-theoretic determinantal
sense, its cokernel is a vector bundle. The obstruction is then a
section of that bundle, and the solvable locus is its zero scheme.
This is the intrinsic content of the matrix calculations. Rank-drop
loci are geometric degeneracy loci, not exceptional rows to discard.

For the retained sextic model, the admissible root open avoids the
single rank-drop root. The resulting injective map gives uniqueness
of a compatible actual sextic whenever one exists. This is a
statement about the low-order incidence, not existence of a degree-
sixteen mate or sole support. The finite pivot calculations later
provide exact local certificates for this geometric zero-locus
problem; they are not its conceptual definition.

## 1. What is already covered, and the added contribution

[Global lifting interfaces](global_lifting_interfaces.md) already proves the fixed-data obstruction modulo all allowed higher lifts. [The sextic addendum](normalization_conductor_phase2_addendum.md#varying-the-sextic-lift-the-missing-q3-direction) retains the free \(q^3\) direction and warns that its rank can differ from the rank of the correction submap. [Polynomial duals and affine pencils](../supplements/POLYNOMIAL_DUALS_AND_AFFINE_PENCILS.md) already supplies rank-stratified determinantal fallbacks and sharper special pencil certificates. The general determinantal criterion is therefore not presented as a new repository discovery.

The useful additions here are: an exact bundle/functor formulation, including nonreduced-base safeguards; an exact description of the rank-drop root in the stated sextic coefficient model; the consequent uniqueness of the compatible actual sextic throughout the actual-pair-admissible root open; and an explicit pivot-residual/unit-ideal completion test that eliminates all cubic lift/correction variables without dropping an open boundary.

## 2. A bundle-map incidence theorem on determinantal strata

A lifting problem in a family is naturally an affine incidence
scheme inside the total space of a vector bundle. On each
scheme-theoretic constant-rank stratum, its image and cokernel
become bundles and the obstruction is a well-defined section.
The zero scheme controls local solvability; when the kernel is
nonzero, the space of lifts is a torsor rather than a canonically
chosen lift. The ring-level proof below is what makes this
geometric formulation valid even over nonreduced parameter bases.



Let \(B\) be a scheme and let \(V,U,S,T\) be finite locally free \(\mathcal O_B\)-modules. Let
\[
\sigma:V\to S,\qquad \tau:V\to T,\qquad a:U\to T
\]
be bundle maps, and let \(s\in\Gamma(B,S)\), \(t\in\Gamma(B,T)\). The correction source \(U\) may have redundant generators; injectivity of \(a\) is unnecessary. Define
\[
L:V\oplus U\longrightarrow S\oplus T,\qquad
L(v,u)=(\sigma v,\tau v-a u),\qquad b=(s,t).
\tag{1}
\]
The actual lift incidence is the closed subscheme of the total space of \(V\oplus U\) defined by \(L(v,u)=b\). This construction commutes with arbitrary base change: it is a finite system of equations between vector bundles, without taking an unverified fiberwise kernel or image.

Fix a determinantal rank stratum
\[
B_r=V(I_{r+1}(L))\setminus V(I_r(L)).                 \tag{2}
\]
Here the closed part is given its determinantal scheme structure; ranks and ideals are local in bundle trivializations. On \(B_r\), \(L\) is locally equivalent by invertible row and column operations to \(\operatorname{diag}(I_r,0)\). Consequently its image, kernel, and cokernel \(Q_r\) are vector bundles, their defining sequences are locally split, and all commute with arbitrary base change within this stratum. The class
\[
o_r=[b]\in\Gamma(B_r,Q_r)                           \tag{3}
\]
is the family obstruction. Its zero scheme \(Z_r\) represents the condition that local lifts exist. Over \(Z_r\), the incidence is an affine bundle, locally a torsor under \(\ker L\); every geometric fiber is an affine space of dimension \(\operatorname{rank}V+\operatorname{rank}U-r\). A global section of this torsor is a stronger request than local existence; no such global choice is implied when \(\ker L\ne0\). If \(\ker L=0\), the incidence is canonically isomorphic to \(Z_r\), and the successful lift is unique and regular on its zero scheme.

**Proof over a ring.** Work where one \(r\)-minor \(A\) is invertible and move it to the upper-left block. Row/column elimination changes the matrix to \(\operatorname{diag}(I_r,D)\). Every entry of \(D\) times \(\det A\) is an \((r+1)\)-minor up to sign. Thus \(D=0\) on the scheme (2). The assertions reduce to solving the first \(r\) coordinates of the target and setting the remaining target coordinates to zero. All operations use invertible matrices and therefore survive arbitrary pullback. This also proves the affine-bundle and uniqueness assertions. \(\square\)

The union of the geometric solvability loci \(Z_r\) is constructible when \(B\) is of finite type over a field. Each \(Z_r\) is closed in its own locally closed stratum; it need not be closed in \(B\). This explicit finite rank decomposition also gives the constructibility directly; the general finite-presentation image principle is [Chevalley's theorem](https://stacks.math.columbia.edu/tag/00FE).

Two qualifications matter. First, a map of bundles whose ranks merely agree on geometric fibers need not be locally split over a nonreduced base. Multiplication by \(\epsilon\) on \(k[\epsilon]/(\epsilon^2)\) has rank zero on every geometric fiber but is not the zero map. The determinantal scheme structure in (2), or an independently proved local splitting, is needed. On a reduced base, constant geometric rank suffices, since the higher minors then vanish as functions. Second, geometric-point vanishing and scheme-theoretic zero are distinct: the equation \(0\cdot v=\epsilon\) is solvable on the only geometric fiber of the dual numbers and has no solution over the dual numbers themselves.

If \(\sigma\) is locally split of constant rank, one can first restrict to \(s\in\operatorname{im}\sigma\), choose a local lift \(v_0\), and put \(K=\ker\sigma\). Then (3) is the familiar class
\[
[\tau(v_0)-t]\in T/(\operatorname{im}a+\tau K),       \tag{4}
\]
provided the combined correction map \(U\oplus K\to T\) has its own locally split constant rank. Formula (1) works without making either of these preliminary choices and remains valid when the ranks change.

## 3. Why degeneracy boundaries cannot be inferred from generic fibers

Solvability is closed *within* a locally split rank stratum, but
need not be closed across rank jumps. A generic solution can
escape to infinity in the affine lift bundle, and a special
fiber can gain new solutions. These elementary examples explain
why a geometric argument must retain every determinantal
boundary rather than extrapolate from the generic root.



These examples concern actual linear incidence over \(\mathbf A^1_x\), not a failure of nonlinear geometry.

* \(xv=1\) is solvable at every \(x\ne0\) and not at \(0\). Its image is \(D(x)\), so generic existence does not imply special existence or closedness. The solution \(1/x\) escapes the affine lift space at the boundary.
* \(xv=0,\ 0=x\) is solvable exactly at \(x=0\). Thus generic exclusion leaves a special solution. Even without a rank jump, \(v=0,\ 0=x\) has the same phenomenon.
* Over \(k[x]\), the matrix \([x]\) has no nonzero polynomial left annihilator. Nevertheless its specialization at \(x=0\) excludes target \(1\). A search for global polynomial left duals alone therefore misses this boundary exclusion. Specialization can create new left-kernel directions.

On an irreducible reduced constant-rank stratum the solvability locus is closed. A generic solution then forces the obstruction section to vanish on that whole stratum, and every geometric point is solvable there. A generic exclusion says only that its closed zero locus is proper, and does not establish emptiness. Passing between different rank strata remains a separate task. Compactifying lift variables projectively also does not repair the first example: the homogenized limit has homogenizing coordinate zero, so it does not give a lift in the original affine problem.

## 4. Global equation spaces, evaluation, and jumping kernels

The natural source is the space of actual homogeneous equations
through the embedded curve, not a freely chosen collection of
normal jets. In families, evaluation on a finite neighborhood
produces a morphism of bundles when cohomology and base change
justify it. If source dimensions jump, the correct incidence
retains ambient coefficients and imposes their containment
equations, rather than replacing them by a prematurely formed
kernel bundle.



The invariant object is the incidence of **actual homogeneous sections**, not independently selected normal coefficients. For a fixed embedded curve and fixed \((d,r)\), take the entire accepted source
\[
V_{d,r}=H^0(\mathbf P^3,\mathcal I_C^r(d)),
\]
with sheaf powers/saturated homogeneous powers as in [actual equation spaces](global_equation_jets.md#exact-homogeneous-equation-spaces-and-fixed-quadric-restrictions). This is a fixed vector space and hence a trivial bundle on every root-parameter scheme. A specified finite-jet target, correction map and their gluing data must be matched by the evaluation of this same homogeneous section. The incidence (1) is independent of basis changes in these spaces. Changes of an affine jet representative by an allowed correction induce isomorphic incidences.

For a genuinely varying embedded family, one may instead have a relative finite neighborhood \(Z\subset\mathbf P^3_B\). If \(H=\pi_*\mathcal O_Z(d)\) is finite locally free and its formation commutes with the relevant base changes, the canonical evaluation
\[
H^0(\mathbf P^3,\mathcal O(d))\otimes\mathcal O_B\longrightarrow H
\tag{5}
\]
defines the actual homogeneous containment incidence. Its fiber kernel is exactly the actual degree-\(d\) space vanishing on \(Z_b\). These local-freeness/base-change hypotheses must be verified; they do not follow solely from flatness of \(Z\), or from a generic dimension count. Standard flat base-change statements are in [Stacks, cohomology and base change](https://stacks.math.columbia.edu/tag/02KE); this draft assumes, rather than invents, the additional hypotheses needed for a given (5).

There is a particularly safe coefficient alternative when a finite matrix \(D:E\to H\) has already been proved to present the actual source fiberwise as \(\ker D_b\). Do not replace it by a guessed source bundle across a rank jump. Keep the original ambient coefficients \(v\in E\), add the equation \(Dv=0\), and stack it with the other equations:
\[
(v,u)\longmapsto (Dv,\sigma v,\tau v-au),\qquad
\text{target }(0,s,t).                              \tag{6}
\]
Then (1)–(3) apply to the stacked map; the actual fiber source can jump without losing new sections. The source comparison is essential: for \(D=[x]\), the sheaf kernel over \(k[x]\) is zero, but the kernel of its fiber at zero is one-dimensional. Tensoring the total-space kernel silently deletes that special actual source. Formula (6) retains it.

The 33-plus-40 sextic coefficient target below is the **accepted coordinate jet model**. Its 40 cubic coefficients should not be silently identified with an intrinsic \(H^0(\operatorname{Sym}^3N_C^\vee(6))\): they record the chosen affine normal expansions and their allowed correction model. The actual source-to-coefficient map and the validity of that model are inherited inputs. Basis-free incidence does not prove unestablished comparison or gluing maps.

## 5. The exceptional root as a degeneracy locus

The sextic correction map has a simple geometric exceptional
configuration: the quadratic normal root becomes the square
of the distinguished linear direction. Exactly there the cubic
direction supplied by the quadric cube lies in the correction
image. The resulting rank drop is a geometric alignment of
normal directions, not an accidental matrix cancellation.
The following calculation proves that this is the only
rank-drop point in the stated coefficient model.



Retain the characteristic-zero balanced coordinates of the addendum. Set
\[
q_1=u+zv/2,\quad \theta=q_1^3,\quad
f=a(z)u^2+b(z)uv+c(z)v^2\ne0,
\qquad \deg a,\deg b,\deg c\le2.
\]
Write \(W_7=k[z]_{\le7}\) and let \(T_9\) be the forty-dimensional space of binary cubics with coefficient degree at most nine. The accepted correction map and its full varying-lift enlargement are
\[
\mu_f:W_7^2\to T_9,\quad (\ell,m)\mapsto f(\ell u+mv),
\qquad B_f=(\mu_f\mid-\theta):W_7^2\oplus k\to T_9.
\tag{7}
\]

**Claim.** The rank of \(B_f\) is sixteen exactly when \(f=\lambda q_1^2\) for a nonzero scalar \(\lambda\in k\), and is seventeen otherwise. Thus its rank-drop locus in the projective nine-coefficient root space is the single point \([q_1^2]\), set-theoretically. No claim about the unreduced determinantal scheme at that point is needed here.

**Proof.** The polynomial ring is a domain, so \(\mu_f\) is injective. Rank sixteen means that \(\theta=f(\ell u+mv)\) for bounded polynomial \(\ell,m\). Over \(k(z)[u,v]\), the quadratic \(f\) divides the cube of the single linear form \(q_1\); hence \(f=a(z)q_1^2\) over \(k(z)\). Comparing the \(u^2\) coefficients shows that this scalar is the original polynomial \(a(z)\). Thus \(b=za\), \(c=z^2a/4\). The degree bound on \(c\) forces \(a\) to be constant, and it is nonzero. Conversely \(f=\lambda q_1^2\) gives \(\theta=f(\lambda^{-1}u+z(2\lambda)^{-1}v)\), an allowed correction of degree one. \(\square\)

For clarity, the rank-drop point has coefficient equations
\[
a_1=a_2=b_0=b_2=c_0=c_1=0,\qquad b_1=a_0,\qquad c_2=a_0/4,
\quad a_0\ne0.                                    \tag{8}
\]
The statement is about the displayed homogeneous root parameterization; projective rescaling is already accounted for.

The actual-pair open used in [the quadric-cycle norm bridge](normalization_conductor_phase2_addendum.md#actual-quadric-cycle-norm-bridge) is
\[
\tau_Q=f(-z/2,1)\not\equiv0.                       \tag{9}
\]
This means a nonzero quartic section, not that it is nonzero at every base point. The reviewed necessity argument is: an actual sole-support pair cannot have the quadric \(Q\) as a component of its sextic; if (9) fails, the sextic restriction to \(Q\) has order at least three along \(C\), leaving class \((3,-3)\), which has no nonzero section; hence \(Q\) would be a component. This uses actual sole support and the stated first-symbol hypotheses; it is not an arbitrary-source restriction imposed for convenience.

The rank-drop point in (8) fails (9). Therefore \(B_f\) has full column rank seventeen on **all** of the actual-pair-admissible open (9), including singular roots, collisions, multiplier zeros, and endpoint strata that satisfy the other retained hypotheses. The broader open \([f]\ne[q_1^2]\) also has rank seventeen. Removing (8) does not remove every root divisible by \(q_1\), whereas (9) does; the actual-pair open is the justified smaller domain.

## 6. The obstruction-bundle zero locus and uniqueness of a lift

On the admissible root open the full actual-source map is
injective. Its cokernel bundle carries the obstruction section,
whose zero scheme is precisely the compatible low-order
incidence. Injectivity means that a successful lift is unique
and varies regularly, not that the zero scheme is nonempty
or has its expected codimension.



Let \(V=H^0(\mathcal I_C^2(6))\), with accepted dimension 23, second-symbol map \(\rho_2:V\to S_2\) of rank 22, \(\dim S_2=33\), and kernel \(kq^3\). Let \(\tau_3:V\to T_9\) be the accepted linear cubic-coefficient map, so \(\tau_3(q^3)=\theta\). For root/multiplier/cubic-target data, write the target as \((\alpha f,\alpha G_0)\) in this model. Use the complete block map
\[
L_f: V\oplus W_7^2\to S_2\oplus T_9,
\qquad (F,w)\mapsto (\rho_2F,\tau_3F-\mu_fw).
\tag{10}
\]
It has 39 columns and 73 rows. On (9) it has full column rank 39: an element in its kernel has \(F=\eta q^3\), and its second equation is \(\eta\theta=\mu_fw\); the independence in (7) forces \(\eta=0,w=0\).

Consequently on any admissible parameter scheme where these source and target bundles and target sections are defined, the low-order actual-source incidence is the zero scheme of a rank-34 cokernel-bundle section. Its projection to that admissible parameter scheme is a closed immersion, and there is **at most one actual sextic** matching a fixed \((f,\alpha,G_0)\). The successful sextic and correction coefficients, when they exist, vary regularly on this zero scheme. This is local in coefficient/projective charts and glues with the appropriate line-bundle twists; projective root or multiplier coordinates must not be treated as globally chosen scalar sections.

Equivalently, impose the eleven symbol-image equations first and choose any fixed linear right inverse of \(\rho_2\) on its image. This gives a polynomially varying representative \(F_c\). Put \(h=\tau_3(F_c)-\alpha G_0\). The remaining equation is
\[
B_f(\ell,m,\eta)=h,
\quad\text{and the actual sextic is }F_c+\eta q^3.   \tag{11}
\]
The cokernel now has rank 23. Once (11) is solvable, all seventeen unknowns are unique. Changing \(F_c\) by \(\lambda q^3\) changes \(\eta\) by \(-\lambda\), preserving the actual sextic. Changing \(G_0\) by an allowed \(f\)-multiple changes only the correction pair. These invariances do not identify other embedded obstructions with this one.

The number 34 is eleven symbol conditions plus a rank-23 cubic quotient. It does **not** assert that thirty-four scalar equations cut the nonlinear root parameter space in expected codimension, or that those equations are independent as functions of root parameters. The low-order incidence is closed relative to its stated open/bundle base. Its closure in the full root space, other spectral/root incidences, and the full actual-pair image need not be the same closed set.

## 7. Pivot charts as local equations for the geometric zero locus

A nonzero maximal minor trivializes the image subbundle.
The remaining equations are local defining equations of the
cokernel-section zero locus. Covering all pivot opens gives
a finite exact test on the declared parameter domain; using
only a convenient minor risks discarding legitimate boundary
solutions. The residual polynomials below are computational
certificates for this bundle-theoretic statement.



This is an exact route to completing a specified low-order coefficient chart; it is not a report that a pending chart calculation was performed.

Take a finitely generated characteristic-zero field \(K\), an affine parameter chart with equation ideal \(J\subset K[x_1,\ldots,x_N]\), and a retained principal open \(D(g)\). All actual denominator units belong in \(g\). If a condition is an ideal-open \((g_1,\ldots,g_e)\ne0\), cover it by the finitely many \(D(g_i)\); multiplying the \(g_i\) would impose the wrong open. Treat projective parameter spaces by a finite affine cover. Assume the source comparison and regular target \(h\) in (11) have been established on this chart and (9) holds.

For each set \(I\) of seventeen rows of the \(40\times17\) matrix \(B_f\), let
\[
\delta_I=\det (B_f)_I,
\qquad
r_{I,j}=\delta_I h_j-(B_f)_j\operatorname{adj}((B_f)_I)h_I
\quad(j\notin I).                                 \tag{12}
\]
Only twenty-three residuals are needed on each pivot open. On \(D(\delta_I)\), equation (11) is equivalent to their vanishing, and the unique solution is
\[
(\ell,m,\eta)^t=\operatorname{adj}((B_f)_I)h_I/\delta_I.
\tag{13}
\]
Indeed the selected seventeen equations force (13); substitution into each remaining equation gives exactly (12). Conversely (12) makes every row hold. No division by a root coefficient or by \(\alpha\) occurs. The finitely many pivot opens cover (9) because of the proved rank seventeen. Any additional **polynomial** necessary conditions already expressed on this same chart can be added to \(J\); conditions requiring a cover or further variables must keep that representation.

Hence the retained chart has no geometrically compatible point if and only if, for **every** pivot open in a proved cover, the finite polynomial ideal
\[
\bigl(J,\ r_{I,j}\ (j\notin I),\ 1-y g\delta_I\bigr)
\subset K[x_1,\ldots,x_N,y]                       \tag{14}
\]
is the unit ideal. This is the elementary localization/Nullstellensatz criterion; see [Hilbert Nullstellensatz](https://stacks.math.columbia.edu/tag/00FV). A literal identity expressing one in these generators is a complete exclusion certificate for that retained pivot chart. If the ideal is proper, it has a point over an algebraic closure of \(K\), with \(g\delta_I\ne0\), and (13) constructs its actual compatible sextic. Such a point is a low-order survivor, not an actual supported pair. A Gröbner calculation provides a terminating decision method for this finite polynomial problem; no practical time or memory bound is claimed.

This improves on a generic-rank or selected-fiber calculation: it gives a finite necessary-and-sufficient completion test on the **whole declared open**, retains every rank and denominator boundary through a proved cover, and eliminates all seventeen linear lift/correction variables before nonlinear elimination. An arbitrary selected minor is insufficient unless its open is the whole chart or the complementary pivots are also covered. The same proof works for the full block matrix (10), with 39-row pivots and 34 residuals, if one wants to avoid choosing \(F_c\).

The representation of \(G_0\), the twenty-five second-obstruction pairings, full spectral torsion including node gluing, and chart coverage must be supplied by their owning calculations. Formula (14) does not turn unresolved or merely necessary representations of those conditions into exact ones. Applying (14) to an exact algebraic representation decides that representation, at its stated logical strength.

## 8. Disposition and remaining work

The new scoped conclusion is that cubic actual-source realization in this sextic model has a unique actual lift on the actual-pair-admissible root open, rather than a surviving free \(q^3\) parameter after cubic matching. It gives a smaller finite completion problem for retained collision, node, and endpoint opens once their target/gluing data are genuinely supplied. It does not close any such open by calculation, construct a degree-sixteen mate, prove properness or sole support, or resolve the unrestricted characteristic-zero STCI question.

## Independent review

Independent reconstruction checked the determinantal scheme strata and nonreduced-base safeguards, the exact bounded-polynomial rank-drop classification, the inherited identity for the cubic layer of the quadric cubed, the actual-pair necessity of the admissible root open, the full-column-rank block argument and unique regular lift, and the complete pivot-residual test. The statements are accepted at their displayed hypotheses. The inherited source computations were not rerun. No nonlinear chart emptiness, degree-sixteen mate, properness or sole-support certificate follows.


## Consolidated historical supplement: `research/supplements/ACTUAL_SEXTIC_MATE_CERTIFICATES.md`

Original mathematical content, hypotheses, qualifications, and proof status preserved verbatim. Relative links retain their historical source context.

# Selected sextics: full mate spaces and rigid residual schemes

For seven specified characteristic-zero sextics, an exact actual-global mate calculation bounds all degree-sixteen mates. This is a finite set of carrier certificates, not an exclusion of their whole parameter family. The useful geometric conclusion at four carriers is stronger than an insufficient-contact verdict: every maximizer gives the same complete-intersection ideal and the same residual line. The retained computation is necessary support for this claim.

## Search question and inputs

For the fixed characteristic-zero curve
\(C=[s^4:s^3t:st^3:t^4]\), seek actual global homogeneous equations
\((F_6,G_{16})\) with reduced intersection support \(C\). Their full
intersection has degree 96, so sole support requires generic transverse
length \(m_C=24\). We start with proper intersections and retain their
residual cycle:

\[
[V(F_6,G_{16})]=m_C[C]+R,\qquad \deg R=96-4m_C.
\]

The [actual sextic construction](toric_sextic_residuals_and_limits.md#endpoint-four-sextic-constructions)
provides global equations on a retained nodal endpoint-four chart. We use
the rational modulus \(\rho=-1\), but vary parameters that the completed
[R-0025 certificate](../results/ci_fixed_sextic_jet_rigidity.md) did not test.
Put

\[
q=x_0x_3-x_1x_2,\quad D=x_2^3-x_1x_3^2,
\]

\[
F_{t,\kappa}=-q^2x_3^2-qDx_2-tqDx_3+D^2/4+\kappa q^3.
\]

These are actual homogeneous sextics with constant coefficients, rather
than proposed function-field symbols. The seven newly tested inputs are

\[
(t,\kappa)=(0,0),(1,0),(1,1),(1,-1),(2,0),(2,1),(0,-1).
\]

The previously certified point \((0,1)\) was deliberately not replayed.
The old certificate and source family are inherited inputs; all ranks in
the table below are new calculations. The numerical row \((6,16)\) is
motivated by [R-0014](../results/movement_two_six_rows.md) under its stated
hypotheses. The fixed-carrier deductions below apply to every proper
degree-16 mate of each displayed sextic and do not assume that numerical
row's filtration or saturation hypotheses.

## A concrete candidate and its exact failure

For every member of this family, take the actual mate

\[
G_{16}=q^8.
\]

The pair is proper: \(q\) is irreducible and
\(F_{t,\kappa}\bmod q=D^2/4\ne0\), so \(\gcd(F_{t,\kappa},q)=1\).
The residual is completely visible. On the smooth quadric \(Q=V(q)\), use
Segre coordinates

\[
[x_0:x_1:x_2:x_3]=[ac:ad:bc:bd].
\]

Then

\[
D=b^2(bc^3-ad^3),\qquad
\operatorname{div}_Q(D)=2L_0+C,
\quad L_0=V(x_2,x_3).
\]

Consequently

\[
\boxed{[V(F_{t,\kappa},q^8)]=16[C]+32[L_0].}
\]

This candidate puts two thirds of the complete-intersection degree on
\(C\), but its remaining degree is a line with multiplicity 32. Increasing
the exponent of the quadric preserves that residual proportion. The search
test is whether a degree-16 perturbation can retain or improve the contact
with \(C\) while removing that residual.

## Exact score for all mates of each selected carrier

Use the actual balanced normal chart

\[
(x_0,x_1,x_2,x_3)
=(1,z,z^3+v,z^4+u+3zv/2).
\]

The quadratic normal term of \(F_{t,\kappa}\) is \(z^8f_t\), where

\[
f_t=(1+2tz+z^2)u^2+tz^2uv-z^2v^2/4.
\]

Its discriminant has square class

\[
P_t(z)=1+2tz+(1+t^2)z^2,\qquad
\operatorname{disc}_z(P_t)=-4.
\]

Thus it is nonsquare in \(k(z)\) over any algebraically closed
characteristic-zero constant field. If \(1+t^2=0\), the polynomial is
linear with a simple zero and the same conclusion holds. This fact is
independent of \(\kappa\).

The completed carrier has two conjugate smooth transverse branches over
the quadratic extension of \(k(z)\). A global mate has the same finite
order \(n\) on both branches, so

\[
m_C=2n,\qquad
G\in(F_{t,\kappa})+(u,v)^n.
\]

For the membership assertion, prepare \(F\) as a monic quadratic in \(u\)
and write the mate's remainder as \(a(v)u+b(v)\). Restricting to the two
branches and subtracting shows \(\operatorname{ord}_v a\ge n-1\), then
\(\operatorname{ord}_v b\ge n\). Hence the remainder has normal degree
at least \(n\). Properness ensures finite intersection length. This is the
same local lemma used in R-0025; its hypotheses are verified here for the
new inputs.

Let

\[
\mathcal K_j(F)=
\{G\in H^0(\mathbf P^3,\mathcal O(16)):
G\in(F)+(u,v)^j\text{ over }k(z)[[u,v]]\}.
\]

The source has dimension 969. The 286 independent global multiples
\(F H^0(\mathcal O(10))\) always lie in \(\mathcal K_j\). At cutoff eight,
\(q^8\) supplies one further direction, independent of the multiples.

The script evaluates actual degree-16 source monomials in the truncated
normal quotient at 80 good base points modulo 65521. It checks all 286
actual multiples at every point. The table gives modular ranks, which are
lower bounds on the characteristic-zero ranks.

| Selected \((t,\kappa)\) | Rank at cutoff 8 | Rank at cutoff 9 | Rank at cutoff 10 | Consequence for every proper \(G_{16}\) |
|---|---:|---:|---:|---|
| \((0,0),(1,0),(2,0)\) | 642 | 672 | 683 | \(m_C\le18\), \(\deg R\ge24\) |
| \((1,1),(1,-1),(2,1),(0,-1)\) | 682 | 683 | 683 | Exact maximum \(m_C=16\), sharp minimum \(\deg R=32\) |

All seven have rank 683 at cutoffs eleven and twelve as well. These are
certificates about all degree-16 global mates of the selected inputs,
rather than seven proposed mates or random local coefficients.

For the four displayed nonzero-\(\kappa\) inputs the rank at cutoff eight
is already as large as possible, because the known 287-dimensional space
of multiples plus \(q^8\) is in its kernel. Therefore

\[
\boxed{\mathcal K_8(F)=F H^0(\mathcal O(10))\oplus kq^8,\qquad
\mathcal K_9(F)=F H^0(\mathcal O(10)).}
\]

It follows that \(m_C\le16\), with equality attained by the concrete pair
above. More strongly, every proper mate attaining this maximal contact is
\(G=FH+cq^8\), \(c\ne0\), and consequently

\[
\boxed{(F,G)=(F,q^8).}
\]

Thus the entire full complete-intersection scheme is rigid at maximal
contact for these inputs. A perturbation preserving maximal contact cannot
remove the residual line; it only changes the presentation of the same
ideal. This explains their failure more precisely than saying that an
obstruction matrix has large rank.

At the three selected \(\kappa=0\) inputs, the ranks only give upper bounds
41 and 11 on proper source directions at cutoffs eight and nine. They do
not prove that any of these extra characteristic-zero directions exist.
The cutoff-ten kernel equality is decisive, so \(m_C\le18\), but attainment
of 18 and a sharp residual bound have not been established.

## Why finite-field rank proves a characteristic-zero failure here

The leading \(u^2\) coefficient is
\(z^8(1+2tz+z^2)\). Every sampled point makes it a unit modulo 65521.
Recursive normal division has denominators generated by this coefficient
and 2. It therefore defines a rational remainder matrix with good
specialization at the chosen prime. A nonzero modular minor is a nonzero
characteristic-zero minor. Conversely the known global multiples, and at
cutoff eight the explicit \(q^8\), give characteristic-zero kernel lower
bounds. Matching these bounds proves the displayed kernel equalities and
their persistence under constant-field extension.

The order-12 remainder basis is
\(1,v,\ldots,v^{11},u,uv,\ldots,uv^{10}\). Lower cutoff matrices are
obtained by retaining rows of smaller normal degree: division by the
carrier never lowers total normal degree, so this restriction commutes
with truncation. The independent M2 implementation instead forms the
truncated quotient directly.

An early 40-point trial had cutoff-eight rank 600, exactly its row count,
and nonzero-\(\kappa\) cutoff-nine rank 680, again the row count. Those
values did not measure actual freedom. Expanding to 80 points resolved
this sampling limitation and gave the sharp statements above. No
characteristic-zero candidate was inferred from a modular kernel.

## Computational meaning and limitations

The exact [Python/C++ verifier](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/stci_search_sextic_jets_2026_10_28.py) and [result table](https://github.com/markluxton1/STCI/blob/6880e35bb6c7ec13c2ba18cc1a0cce328e1d795f/research/computations/stci_search_sextic_jets_2026_10_28.json) retain all seven inputs, good points and source hashes. The implementation imports the existing exact division and elimination routines without running the older fixed-carrier test. The separately assembled [Macaulay2 calculation](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_stci_search_nodal_m2_2026_10_28.m2) checks representative inputs by direct truncated quotient construction. The inherited independent audit covers the rank specialization and representative reconstruction; it is not a fresh replay of every rank in this consolidation.

The rank is measuring the global equation subspace whose pullback has specified branch order. Matching a modular rank lower bound with explicit characteristic-zero kernel vectors proves an equality; a modular kernel alone would give no characteristic-zero candidate. At the three \(\kappa=0\) inputs the bound is not sharp. At the other four inputs, raising or perturbing the mate while preserving maximal contact cannot move the residual scheme. Neither fact bounds other carrier parameters or all mate degrees.


## Geometry of the parameter boundary and remaining limitations

Introduce a degree-one auxiliary coordinate \(W\). The exact identity
\[
F_{t,\kappa}=q^2\left[
W^2-2(x_2+tx_3)W-x_3^2+\kappa(x_0x_3-x_1x_2)
\right]_{W=D/(2q)}
\]
exhibits a genuine geometric degeneration. The auxiliary quadric has rank
five when \(\kappa\ne0\): its gradient equations force all five
coordinates to vanish. When \(\kappa=0\), its restriction to
\((x_2,x_3,W)\) has symmetric matrix determinant one and its remaining
two coordinates are free, so the rank is three and the vertex is a line.
This verifies the rank change. It does not identify the whole surface
normalization or prove that the rank change explains the exact jet-kernel
dimensions.



## Consolidated historical supplement: `research/supplements/CONDITIONAL_2_12_CONTINUATION_AND_SEXTIC_EXCLUSIONS.md`

Original mathematical content, hypotheses, qualifications, and proof status preserved verbatim. Relative links retain their historical source context.

# conditional 2 12 continuation and sextic exclusions

## Proof-dependency map: conditional exclusions and exceptional loci

The [strict-surface continuation](#nonnormal-conductor-budget-and-local-escape-models) and [exceptional-locus audit](#2026-10-21-conditional-2-12-geometric-audit-and-exceptional-locus) refine the original conditional (2,12;6,16;2) geometry. The [surface audit continuation](#2026-10-21-conditional-2-12-surface-audit-cont2) and [free-orbit sextic exclusion](#2026-10-21-cont2-free-orbit-global-sextic-exclusion) make more specific deductions under the retained assumptions.

These depend on the [symbol and actual sextic realization tests](https://github.com/markluxton1/STCI/blob/20b05fb7ee16f14e4e371c7e0dce7256ba11b480/research/supplements/CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md#2026-10-20-conditional-2-12-global-realization-incidence) and on the [node/conductor constraints](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/CONDITIONAL_2_12_SINGULAR_AND_CONDUCTOR.md#2026-10-21-conditional-2-12-cubic-image-and-conductor-interface). The surface-bound arguments, exceptional-locus computations, and actual homogeneous lifting are distinct steps. A conditional exclusion on a specified orbit or singularity type does not eliminate all (2,12) pairs.

Retain the original hypotheses, computational certificates, exceptional cases, and independent audits as the evidence for each narrow conclusion.

---


Complete mathematical arguments and exploratory boundaries preserved. Conditional conclusions remain conditional; computational and geometric obstructions are not asserted beyond their original hypotheses.

---

## Nonnormal conductor budget and local escape models

These conditional consequences use an actual sole-support degree-(6,16) pair, full generic initial CI (2,12), and actual saturated movement-two first relation. The complete strict-sextic proof follows below.

## 4. Conductor budget: a useful identity, not yet an exclusion

For an integral nonnormal strict sextic let `nu:Y->D` normalize it.
The finite-duality identity gives

    omega_Y = I_conductor tensor nu^*omega_D,
    omega_D=O_D(Q'),          Q'=2H-E.

Let `Cbar` be the conductor scheme on `Y`. If a general `L` section
meets all its components properly, normalizes the corresponding
section curve, and avoids the finitely many normalization singular
points, ordinary curve conductor duality gives

    L.Cbar=2*(6-g_L)<=12.

Here `g_L` is the geometric genus of that section curve. The identity
records the arithmetic-genus-six budget for a general `L` section;
it cannot be used when that section does not separate components or
meets a contracted conductor component improperly without checking
the stated conditions. In particular it is not a bound on the
length of the whole Jacobian scheme.

The normal plane class `H` has degree zero on exceptional vertical
fibers, whereas `L` has degree one there, so `L` can detect conductor
on such fibers. The initial budget of twelve alone nevertheless
allows several generic ordinary-double fibers and supplies no
contradiction by itself. High contact does not force their generic
transverse singularity to be `z^m+t^10`: the permitted formal model

    F'=p*(z^2+t^2)+t^10

is generically an ordinary double point along the fiber `z=t=0`.
Its conductor cost cannot be estimated by silently omitting the
`t^2` term in `A`.

## 5. Local nonnormal escape models and the global degree boundary

At a smooth ramification point a simple BASE multiplier can still
give a nonreduced pulled-back divisor. The exact formal model

    A=z, p=z-w^2-2t^5,
    F'=A*p+t^10=(z-t^5)^2-z*w^2

has smooth root `z=w^2` on `E`, simple base multiplier `z`, and a
singular curve `w=0,z=t^5`. Thus squarefreeness on the base alone
does not establish local normality. This model is not a global
sextic in the permitted coefficient space.

At a node with a simple base multiplier there are further local
escapes. Put

    R=(z-t)^2*(z-t^8),
    F'=z*w^2-R,
    p=(F'-t^10)/z.

The last expression is regular because `R(0,t)=-t^10`. Then
`F'=z*p+t^10`, the exceptional root is `w^2-z^2=0`, and the
singular curve `w=0,z=t` leaves `E`. This verifies why the case
where a base multiplier vanishes at a node needs its own analysis.

None of these formal constructions supplies actual global
`k`-coefficients of `F6,G16`, and the original literal normal-degree
budget of the sextic is still binding. They are countermodels to
missing local hypotheses, not counterexamples to the global
conditional exclusion sought by the user.

The separate conductor-ramification note develops a stronger route
through a Gorenstein surface with trivial dualizing sheaf. Applying
it here requires an independently justified contraction to such a
surface; the bare local bridge does not supply that contraction.
Until that bridge and the local conductor arguments are reviewed,
section 3 is the exact independently checked global exclusion.


---

## 2026-10-21-conditional-2-12-geometric-audit-and-exceptional-locus

# Conditional (2,12;6,16;2): geometric audit and an exact exceptional locus

Date: 2026-10-21. Author: `incidence_audit` worker.

Status: **independent review PASS for the normal-strict-sextic
exclusion; ampleness and nodal scope extension independently
reviewed PASS by `surface_bound`, with separate root reconstruction.**
No record is edited. The configuration remains unresolved
on the explicit degree-52 exceptional locus in section 6. Sections
3--4 retain the weaker smooth-root step from which it was derived.

## 1. Exact scope and reviewed dependencies

The field is algebraically closed of characteristic zero,
`C=C0=[s^4:s^3t:st^3:t^4]`, and the hypothetical actual homogeneous
pair has degrees `6,16`, sole reduced support `C`, FULL generic
coprime ordinary initial CI `(2,12)`, and ACTUAL saturated
movement-two first relation. Let `B=Bl_C(P3)`, let `E` be the
exceptional divisor, and put `H=pi^*O(1)`.

The inputs are
[R-0010](../results/saturated_first_relation_normal_flatness.md) and
[R-0011](../results/moving_nonreduced_spectral_root_obstruction.md).
The finite singular-root bridge is a separately reviewed but
dependency in
[the October 20 singular-root note](../supplements/SINGULAR_ROOT_ACTUAL_PAIR_BRIDGE.md).
It gives common order-two transforms with local ideal `(p,t^10)`
at every full root point. The full root `Z=(f)` is reduced of class
`(2,2)` on `E`, and `Z->C` is finite flat of degree two.

This review concerns
[the strict-surface proposal](https://github.com/markluxton1/STCI/blob/20b05fb7ee16f14e4e371c7e0dce7256ba11b480/research/supplements/CONDITIONAL_2_12_CONTINUATION_AND_SEXTIC_EXCLUSIONS.md#2026-10-21-conditional-2-12-geometric-audit-and-exceptional-locus)
and [the actual-pair norm proof](../synthesis/normalization_conductor_phase2_addendum.md#actual-quadric-cycle-norm-bridge).
Inherited chart, normal-flatness and root-obstruction verifiers were
not rerun. The normal-surface argument below was independently
reconstructed from its geometric inputs.

## 2. Normal strict sextics: independent review PASS

Write `D=(F6)'`, of class `6H-2E`. At a zero of `alpha|Z`, the
other original symbol coefficient `beta` is a unit. After choosing
`p=G16/t^2` up to a unit, the actual generator change gives

    F6/t^2=A*p+t^10*U,             U a unit,

and the divisor of `A|Z` equals that of `alpha|Z`. The ideal
`(A,p,t)` is a parameter ideal in the regular three-dimensional
ambient ring, hence a regular sequence. Differentiation gives the
ordinary Jacobian containment

    J_(F6/t^2) subset (A,p,t^9).

For an isolated singularity its Milnor number is therefore at
least `9*length O/(A,p,t)`. This works at multiple zeros and
singular root points: it uses a complete-intersection length, not
smooth local coordinates. Since `length div_Z(alpha)=2*8=16`, a
normal `D` would have

    sum mu_x(D) >= 144.                                    (1)

The blowup intersection calculations were independently checked:

    H^3=1, H^2 E=0, H E^2=-4, E^3=-14,
    K_B=-4H+E,
    c2(B).H=10, c2(B).E=16,
    D^3=40, c1(B).D^2=40, c2(B).D=28.

For example a general plane transform is `Bl_4(P2)`, with Euler
number seven, giving `c2(B).H=7+3=10`. On `E=P1 x P1`, the normal
bundle is `O(7,-1)`, giving `c2(B).E=4+(2,2).(7,-1)=16`.
Adjunction yields `K_D=(2H-E)|D`, `K_D^2=-4`, and smooth-member
Euler number `28`.

The seven cubics `q*x0,...,q*x3,A,B0,D0` generate `I_C(3)`.
On `Q`, the last three are the local equation of `C` multiplied
by the basepoint-free first-ruling quadratics `a^2,ab,b^2`.
Together with `q` this proves sheaf generation, including along
`C`. Thus `L=3H-E` and `2L=6H-2E` are basepoint free; their general
members are smooth by Bertini. This supplies a smoothing in the
same linear system.

Connectedness of `D` follows from `H1(O_B(-D))=0`. By Serre
duality this is `H2(O_B(2H-E))=0`; the strict quadric sequence
reduces it to the acyclic bundle `O_Q(1,-1)` and the rational
threefold `B`. Hence a normal `D` is connected and integral.

For a projective resolution `S->D`, the pullback plane class `h`
is nef and big, with square six. A general plane avoids the finite
singular-point images, and its strict curve is smooth and
irreducible. Adjunction computes genus

    1+(6+4)/2=6.

The nef-and-big Kawamata--Viehweg theorem applies to the integral
divisor `h` on the smooth projective `S`, so
`H1(K_S+h)=0`. Serre duality and the restriction sequence inject
`H1(O_S)` into the genus-six curve's `H1`, proving `q(S)<=6`.
The relevant theorem was checked directly in
[Fujino's statement, Theorem 0.1](https://www.math.kyoto-u.ac.jp/~fujino/kawamata--viehweg2.pdf);
there is no fractional boundary in this application.

The exceptional curves of `S->D` have negative-definite
intersection matrix, so their `H2` classes inject into `H2(S,Q)`.
The contraction exact sequence then gives `b3(D)=b3(S)<=12`.
Connected fibers give `b1(D)<=b1(S)<=12`. With `b0=b4=1` and
`b2>=0`, this gives `e(D)>=-22`. The isolated hypersurface
smoothing formula gives

    sum mu_x(D)=28-e(D)<=50,                                (2)

contradicting (1). No assertion `b1(D)=0`, crepant resolution, or
classification of K3 singularities is needed. Over a general
algebraically closed characteristic-zero field, the finite-type
data descend to a finitely generated field embedded in `C`;
geometric normality and the actual hypotheses persist. This
proves the claimed exclusion with its exact normality assumption.

**Review outcome:** PASS. The threshold `144>50` includes all
multiplier multiplicities and all retained root types. The proof
does not apply directly to positive-dimensional singular loci.

The isolated argument cannot be applied to a nonnormal strict sextic with a singular curve: its ordinary Jacobian algebra has infinite length. Embedding a finite complete intersection (A,p,t^9) in that singular scheme gives no bound on the degree of the whole scheme or a discriminant multiplicity. The [Aluffi–Cukierman multiplicity formula](https://www.math.fsu.edu/~aluffi/papers/1992Mod.pdf) uses the full Segre class and first-jet spanning; an arbitrary finite subscheme length supplies neither. The local escape models above preserve the explicit counterexamples to this misuse.

## 3. Ampleness extends the exclusion to a whole root open

The seven cubic generators give a closed graph embedding

    B -> P3 x P6,

with `H` and `L=3H-E` the restrictions of the two hyperplane
classes. This follows from the Rees-algebra construction of the
blowup, after twisting the ideal by `O(3)`. Consequently the
strict mate divisor

    G' =16H-2E=10H+2L

is the restriction of `O(10,2)` and is **ample**. This argument
uses positive coefficients on both graph factors and does not
claim that `L` itself is ample.

The actual common-transform intersection has reduced support
exactly `Z`. Off `E` this follows from sole reduced support of the
original pair; on `E` it follows from the jointly generating
coefficient pair `(alpha,beta)`.

Assume now that `Z` is smooth and that `div_Z(alpha)` is reduced.
At a point of `Z` with `alpha!=0`, the strict sextic is smooth,
because its exceptional restriction is a unit times the smooth
root equation. At a zero, `(A,p,t)` are regular local coordinates
and the equation is `A*p+t^10*unit`, an isolated `A9` singularity.
Thus the singular locus of `D` is zero-dimensional in a
neighborhood of `Z`.

If the global singular locus of `D` had a curve component
`Gamma`, then ampleness of `G'` would force `Gamma` to meet `G'`.
A contained curve would itself lie in `Z`; otherwise its
intersection is nonempty and lies in `Z`. Both alternatives
contradict local zero-dimensionality of the singular locus at
every point of `Z`. Hence `Sing D` is finite. A hypersurface is
Cohen--Macaulay, and finiteness of its singular locus gives
regularity in codimension one; Serre's criterion makes `D`
normal. Section 2 then contradicts existence.

**New consequence:** an actual pair in this conditional
configuration cannot have both a smooth full root and a reduced
divisor `div_Z(alpha)`. This uses actual support and global
ampleness; a bare root incidence point does not supply them.

## 4. First polynomial exceptional locus (strengthened in section 6)

In the fixed original coefficient coordinates put

    Delta=b^2-4ac,
    tau=(z^2/4)a-(z/2)b+c,
    alpha proportional Ncomp(tau).

The [actual-pair norm proof](../synthesis/normalization_conductor_phase2_addendum.md#actual-quadric-cycle-norm-bridge)
establishes the last identity and `tau!=0`, including ramified fibers
and collision multiplicities. The separate `surface_bound` review
applies to that local contact argument and its hypotheses.

For a finite flat quadratic root in characteristic zero,

    Z smooth iff Disc_4(Delta)!=0.

When `Z` is smooth, the pulled-back divisor of the base binary
octic `alpha` is reduced precisely when `alpha` is squarefree and
its zero divisor avoids the branch divisor `Delta`. The exceptional
closed condition from the smooth-root step is therefore

    E(f)=Disc_4(Delta)
           *Disc_8(Ncomp(tau))
           *Res_(8,4)(Ncomp(tau),Delta)=0.                 (3)

Here every discriminant and resultant is homogeneous; zero or
infinite affine roots are retained. The degrees in the nine
coefficients of `f` are respectively `12,28,24`, so `E` has
degree `64`. The open `tau!=0`, the reduced doubly finite root
open, the exact Picard gluing condition and all earlier ambient
and global coefficient conditions remain in force.

Equation (3) is necessary for an actual global pair. It does not
say that its zero locus has actual pairs, or that it is empty
after the other equations. It retains the singular-root strata,
multiple multiplier zeros, and collisions between multiplier
zeros and branch points.

## 5. Why the exceptional strata cannot be silently discarded

The local bridge alone permits a positive-dimensional singular
locus when the multiplier has a multiple zero. For example

    A=z^2, p=x, F'=x*z^2+t^10

has `U=1` and finite `(A,p,t)` but is singular along `z=t=0`.
That is a whole exceptional-fiber direction, not an isolated
Milnor singularity.

Even squarefreeness on the base is insufficient at ramification.
Take a smooth root `p mod t=z-w^2`, the simple base multiplier
`alpha=z`, and

    A=z+t^5, p=z-w^2-t^5,
    F'=A*p+t^10=z^2-z*w^2-w^2*t^5.

The singular locus contains `z=w=0`, with `t` arbitrary. Thus
the root is smooth and `alpha` is squarefree on the base, but its
pullback divisor is not reduced and the normality conclusion
fails. The resultant factor in (3) is justified. These are local
countermodels to an omitted hypothesis; neither is asserted to
come from a global sextic with the permitted degree budget.

At a multiple base zero `c` of `alpha`, the first cubic matching
condition says, on the exceptional fiber,

    F3(c,u,v)=f(c,u,v)*(ell(c)u+m(c)v).

The entire fiber can be singular only if `ell(c)=m(c)=0`, since
`f(c,u,v)` is a nonzero polynomial. If the quotient linear form
is nonzero, only its finite zeros and the root points can be
singular on that fiber. This gives a further exact local test;
it is not by itself a criterion excluding singular curves that
leave the exceptional divisor through one of those points.

The remaining task is to combine this exceptional locus with
the actual cubic and higher global sextic lifts, or control its
normalization and conductor. The isolated Milnor bound does not
dispose of these loci, and the present note makes no conditional
emptiness claim on them.

## 6. Nodal extension: only a nonreduced multiplier divisor remains

The smoothness hypothesis on `Z` in section 3 can be removed.
After the full Picard torsion test, the only retained roots are
smooth integral, integral nodal, and two `(1,1)` components meeting
at two transverse nodes. In particular `Z` has at most two
ordinary nodes. Cusps and tangent-component roots are already
excluded by the torsion-free additive Picard argument; this
extension does not reopen them.

**Claim.** Every actual pair in the exact conditional configuration
has a nonreduced divisor `div_Z(alpha)`.

**Proof.** Suppose that divisor is reduced. Then every base zero
of `alpha` is simple, and its inverse image consists of two
distinct smooth unramified root points. In particular `alpha`
does not vanish at a node: a Cartier function vanishing at an
ordinary node cannot cut out a reduced point there. The elementary
double-cover equation also shows that every multiplier zero avoids
the discriminant divisor `Delta`.

We describe `Sing D` along the entire exceptional surface, not
only along `Z`:

* Outside `Z` and the fibers over multiplier zeros, `D` does not
  meet `E`.
* On a multiplier fiber away from `Z`, the derivative of
  `alpha*f` in the base direction is nonzero, since the multiplier
  zero is simple and `f` is a unit. Thus `D` is smooth there.
* At a smooth root point with `alpha!=0`, the nonzero root
  derivative makes `D` smooth.
* At a multiplier zero on `Z`, the simple intersection gives the
  isolated `A9` singularity of section 3.

It remains to examine a node of `Z`, where `alpha` is a unit.
Use `t=0` as the exceptional equation, and two tangential
coordinates on `E`. The restriction of `F6/t^2` has an ordinary
node, so its Hessian in the two tangential variables is
nondegenerate. The analytic Morse lemma with parameter `t`, or
its characteristic-zero formal version, puts the local equation
in the form

    x*y+h(t),

by a coordinate change preserving `t`. If `h` is not identically
zero, the surface is smooth or has an isolated `A_n` singularity
and is normal. If `h` is identically zero, the local singular
locus is the unique smooth curve `x=y=0`, transverse to `E`.
It has intersection multiplicity one with `E`. These statements
also hold over an arbitrary algebraically closed
characteristic-zero field after completion or descent to `C`.

Suppose `D` is not normal. Its hypersurface singular locus then
has positive dimension, hence contains an integral projective
curve `Sigma`. (A two-dimensional component is already impossible:
its intersection with the ample mate would give a curve in `Z`
where `D` is generically smooth.) The preceding local description
shows that no such curve is contained in `E`, and every point of
`Sigma intersect E` is one of the at most two nodes, with local
intersection multiplicity one. Hence

    d=H.Sigma is a positive integer,
    e=E.Sigma is an integer with 0<=e<=2.                    (4)

There are no intersections of `Sigma` with the strict mate outside
`Z`, by actual sole support. At each possible node contact
`alpha` is a unit, so choose the finite-bridge generator to be
`p=F6/t^2`. The other original generator then satisfies

    G16/t^2=C*p+t^10*V,           V a unit.

Restricting to the smooth branch of `Sigma` gives exactly order
ten at each of its transverse exceptional contacts. In particular
the strict mate cannot contain `Sigma`, and its intersection
degree is `10e`. On the other hand its divisor class gives

    16d-2e = G'.Sigma = 10e,
    4d=3e.                                                    (5)

Since `d>0` and `d,e` are integers, (5) forces `d>=3` and
`e>=4`, contradicting (4). This rules out all singular curves.
Therefore `D` is normal, and the normal-strict-sextic exclusion
in section 2 gives the final contradiction. The claim follows.

Consequently the exact exceptional closed condition strengthens
(3) to

    E_reduced_alpha(f)
       =Disc_8(Ncomp(tau))
           *Res_(8,4)(Ncomp(tau),Delta)=0.                    (6)

Its degree in the nine original root coefficients is `28+24=52`.
There is no factor `Disc_4(Delta)`: nodal full roots with a reduced
multiplier divisor have been excluded by the transverse-node
argument, so singular roots are not retained merely for being
singular. On the retained reduced double-cover locus, (6) says
exactly that `div_Z(alpha)` is nonreduced. The full finite-flat
root, homogeneous roots at infinity, and every earlier open and
gluing equation remain in force.

This is a necessary actual-global-pair obstruction. It is not a
proof that the zero scheme of (6), after the other global lifting
conditions, is empty. The remaining loci include multiple base
zeros of the forced norm multiplier and collisions of its zeros
with branch or node fibers. The local countermodels in section 5
explain why the normality argument cannot simply discard them.

**Independent review.** The separate `surface_bound` worker
reconstructed the exceptional-surface cases, parameter-preserving
Morse argument, unique transverse node branch, and divisor
identity `16d-2e=10e`, and reported PASS. The root agent separately
checked the same argument, including smoothness outside `Z` on
simple multiplier fibers. These are review records for a new
conditional proposal.

## 7. Where a remaining singular curve must meet the root

There is a further conditional classification useful for the
exceptional locus. Suppose the actual strict sextic is normal in
a neighborhood of `Z intersect {alpha=0}`. If a singular curve
`Sigma` remains, its contacts with `Z` are all nodes where
`alpha` is a unit. The parameter-Morse argument gives at most
two such contacts, each transverse to `E`. Write their number
as `n<=2`, and put `d=H.Sigma`, `e=E.Sigma`.

There can now be EXTRA contacts with `E` outside `Z`, on multiple
multiplier fibers; these must be retained. In particular it is
not valid to replace `e` by `n`. The actual mate has zeros on
`Sigma` only at its `Z` contacts, and its local order there is
ten. Thus the correct degree identity is

    16d-2e=10n.                                             (7)

If `Sigma` is not contained in the strict quadric `Q'`,
effectivity of `Q'=2H-E` gives `e<=2d`. Hence `12d<=10n<=20`.
For `d>=2` this is impossible. For `d=1`, the inequality forces
`n=2`, but (7) would give `e=-2`, also impossible. Thus every
remaining singular curve under the displayed normality
assumption is contained in `Q'`.

Since `D intersect Q'=R` has class `(4,0)`, such a curve is a
ruling line. It has `d=1`, `e=3`, and (7) gives `n=1`. It passes
through precisely one node of the full root, in the quadric
direction. Moreover `D` being singular along the line forces
its multiplicity in `R` to be at least two. The norm identity
then forces the corresponding multiplicities in `tau` and
multiple multiplier zeros at the other ruling-orbit points.
The ruling cannot be a branch fiber of `pi3`: such a line has
its entire length-three intersection with `C` at zero or
infinity, contradicting the transverse multiplicity one at
the node. Thus its three curve-intersection points are distinct.

Consequently an actual remaining pair must exhibit at least one
of the following concrete phenomena:

* The strict sextic is nonnormal at a root point where
  `alpha=0`.
* It is singular along a trisecant ruling line on `Q`, meeting
  the full root at an ordinary node in the quadric direction,
  with the forced residual-line and multiplier multiplicities
  above.

This is a classification under the stated local normality
alternative, not an exclusion of either phenomenon. The
`conductor_budget` worker independently checked (7), the need
to retain the extra exceptional contacts, the `Q'` inequality,
and the ruling-line conclusion. It reported the numeric
argument sound. Full conductor analysis of the two alternatives
remains open in this note.


---

## 2026-10-21-conditional-2-12-surface-audit-cont2

# Conditional (2,12;6,16;2): cubic-model and conductor continuation audit

Date: 2026-10-21. Reviewer: `surface_bound`.

Status: **independent review PASS for the cubic-model interface and the
ramified simple-multiplier exclusion; one incorrect normalization claim
in the separate nodal example is explicitly rejected below**. All results
are reviewed proposals rather than records. No actual pair or
full emptiness result is asserted.

## 1. Scope and reviewed files

The exact actual-pair scope is `C0`, algebraically closed characteristic
zero, degrees `(6,16)`, sole reduced support `C0`, FULL generic coprime
ordinary initial CI `(2,12)`, and ACTUAL saturated movement-two first
relation. The reviewed inputs are:

* [the cubic-image and conductor interface](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/CONDITIONAL_2_12_SINGULAR_AND_CONDUCTOR.md#2026-10-21-conditional-2-12-cubic-image-and-conductor-interface);
* [the conductor-ramification proposal](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/CONDITIONAL_2_12_SINGULAR_AND_CONDUCTOR.md#2026-10-21-conditional-2-12-conductor-ramification), sections 1--6;
* [the normality and ampleness audit](#2026-10-21-conditional-2-12-geometric-audit-and-exceptional-locus),
  whose nodal extension was independently reconstructed in
  [the surface continuation](#nonnormal-conductor-budget-and-local-escape-models).

The singular-root finite bridge remains an explicit reviewed but
dependency. The lower-carrier input was read in
[R-0001](../results/quartic_carrier_exclusion.md), including its
**Consequences** paragraph, which expressly includes the earlier
plane/quadric/cubic exclusions and factor reduction. No inherited
carrier proof was rerun.

## 3. Full conductor duality and component genus: independent review PASS

Let `Y` normalize the integral Gorenstein `T` with `omega_T=O_T`.
Finite duality identifies `omega_Y` with the conductor ideal `I`
inside `O_Y`. Strictly, the `Hom_T` expression is a sheaf on `T`
and equals the pushforward of this `O_Y`-module; the module
identification itself is exact. Normal surface `Y` is Cohen--Macaulay.
The canonical ideal is depth two, so `C=V(I)` is a pure
Cohen--Macaulay curve (unless empty).

Apply `Hom_Y(-,omega_Y)` to
`0->I->O_Y->O_C->0`. Since `End_Y(omega_Y)=O_Y`, the resulting
cokernel is `O_Y/I`; codimension-one duality identifies it with
`omega_C`. Thus `omega_C=O_C`, even when `Y` is not Gorenstein
and the conductor is nonreduced.

For an irreducible reduced conductor component `R` of generic
multiplicity one, finite closed-immersion duality gives
`omega_R=Hom_C(O_R,O_C)=Ann(I_R)`. Its map into `O_R` is
generically nonzero and is injective because the canonical module
of an integral curve is torsion free. Its cokernel is finite;
Euler characteristics yield `2p_a(R)-2<=0`. Nilpotents on other
components do not affect this argument.

The map between the normalizations of `D` and `T` exists by the
universal property of normalization and is proper birational. A
conductor component not contracted by `phi` maps nonconstantly
and properly onto an integral conductor component, hence finitely.
It is birational because the ambient map is an isomorphism off
`Q'`. Therefore arithmetic genus can only increase in its image.
This remains true when the particular singular point lies on `Q'`.

**Verdict: PASS.** No assumption that the whole conductor is reduced,
or that the normalization is Gorenstein, has been inserted.

## 4. Ramified simple-base zeros: independent review PASS

At a smooth ramification point with a simple base zero of `alpha`,
both `A` and `p` are regular in the base coordinate `z`. Factoring
them by their unique roots in `z` and applying the parameter
Morse lemma gives exactly

    F'=x^2-B(w,t),
    B=s(w,t)^2-t^10*u(w,t),    s(w,0)=unit*w^2, u a unit.

The critical section in the centered `z` variable is divisible
by `t^10`; this verifies that the coefficient of `t^10` in the
critical value remains a UNIT. Therefore

    B=(s-t^5*sqrt(u))*(s+t^5*sqrt(u)).

The factors are coprime and each is Weierstrass of degree two in
`w`. Nonnormality forces precisely one to have a double linear
factor `e*d^2`, with `d=w-phi(t)`; the other cannot also be a
square, because its restriction to `d=0` has odd valuation five.

Here the finite normalization calculation IS valid: the double
cover is MONIC in `x`, and its normalization is
`R+R*y`, with `y^2=B_other` and original ring `R+d*R*y`.
The exact conductor is `d*(R+R*y)`. Its curve germ is
`y^2=t^5*unit`, reduced and irreducible, with delta two and
generic multiplicity one. A noncontracted global conductor
component would have arithmetic genus at least two, contradicting
section 3.

If the corresponding singular curve is contracted, it is a ruling
fiber `W` of `Q'`. Its normal bundle is `O+O(-1)` and `D|W=O`.
The nonzero discriminant of the global quadratic normal cone is
then a section of `O_W(2)`. The exact local normal form makes it
vanish to order five at the point, impossible. The parameter `t`
is indeed a uniformizer on `W=(x,d)`.

**Verdict: PASS.** Together with section 2, this removes the
conditional contraction hypothesis from the ramified simple-base
zero exclusion for ACTUAL pairs. It does not establish normality
at repeated base zeros or at nodes where `alpha` vanishes.

## 5. Strengthened exact exceptional locus

Assume `alpha` is squarefree on the base and does not vanish at
a root node. The ramified-simple-zero result removes the only
additional singular-curve contacts beyond the earlier nodal
argument. Every singular curve must then meet `E` solely in the
at most two root nodes, where `alpha` is a unit and the parameter
Morse form is `xy+h(t)`. A singular curve there is unique and
transverse to `E`. Writing `d=H.Sigma>0`, `n=E.Sigma<=2`, actual
support gives `G'.Sigma=10n`, whereas its class gives
`16d-2n=10n`, impossible. Thus `D` is normal and the reviewed
`144>50` obstruction applies.

Every actual pair must therefore satisfy at least one of:

    alpha has a multiple zero on the BASE;
    alpha vanishes at a NODE of the full root.

For smooth full roots, the new necessary equation is simply
`Disc_8(Ncomp(tau))=0`, degree 28 in the original root coefficients.
For nodal strata retain the actual node incidence
`alpha(c)=0, f(c,w)=0, df(c,w)=0`. These are necessary global
realization conditions. Their intersections with the full first,
second, torsion, and actual global sextic lifting conditions
have not been proved empty here.

## 6. Rejected finite-normalization assertion in the nodal caution

Section 7 of the conductor-ramification proposal correctly gives
the local equation

    F=z*w^2-(z-t^3)^2*(z-t^4)=z*p+t^10

and its nonnormal curve. Its subsequent claimed normalization
`y=w/(z-t^3)`, `z*(y^2-1)=-t^4` is NOT finite over the original
surface: at `z=t=w=0` its fiber contains the affine `y`-line.
Thus the assertions there that the finite conductor has two
smooth branches and that the displayed surface is the finite
normalization are rejected. A warning was added above that
historical paragraph rather than deleting it.

A potentially correct finite extension instead adjoins

    v=z*w/(z-t^n),         v^2=z*(z-t^m),
    z*w=(z-t^n)*v,
    v*w=(z-t^n)*(z-t^m),         2n+m=10.

The new generator is integral because its quadratic equation
is monic. Normality and the exact conductor of this extension
require their own verification. They are not assumed in the
exclusions of sections 2--5. In particular, the defective nodal
example supplies no evidence that the remaining global node
stratum survives the conductor test.


---

## 2026-10-21-cont2-free-orbit-global-sextic-exclusion

# Free cube-orbit endpoint chart: exact global sextic exclusion

Date: 2026-10-21, continuation 2. Status: **new exact conditional
exclusion, independently checked**.

Work over an algebraically closed field of characteristic zero with
`C0=[s^4:s^3t:st^3:t^4]`, the accepted balanced conormal frame, and the
conditional `(r,s;a,b;epsilon)=(2,12;6,16;2)` configuration. This note
excludes the following precise structured incidence:

1. the moving quadratic root `f` satisfies the accepted first ambient
   incidence `K1`;
2. the sextic multiplier is the canonical cube norm of its quadric-line
   restriction, up to a nonzero scalar;
3. both endpoints of that restriction are nonzero and no root is carried
   to another root by multiplication by a primitive cube root of unity;
4. an actual global sextic has second symbol `alpha*f` and matches the
   canonical first cubic lift.

The incidence is empty as a scheme. The argument stops at the cubic
sextic obstruction. It needs neither a global mate nor a degree-twelve
standard-basis construction, because the required sextic already fails.
Applying the conclusion to actual supported complete intersections also
uses the [quadric-cycle norm argument](../synthesis/normalization_conductor_phase2_addendum.md#actual-quadric-cycle-norm-bridge).

## Inputs and evidence

The accepted first incidence and ambient chart are inputs from
[STCI-R-0007](../results/quadratic_root_obstruction_model.md). The actual
saturated-first-relation application uses the hypotheses of
[STCI-R-0010](../results/saturated_first_relation_normal_flatness.md) and
the separately supplied finite singular-root bridge. The new global
source map is the previously recorded
[exact sextic symbol calculation](#2-the-exact-global-k-linear-symbol-map).

The exact new computations are:

- [four-parameter family exporter](../computations/conditional_2_12_cubic_reduction_2026_10_21_family.py),
  and [Macaulay2 input](https://github.com/markluxton1/STCI/blob/2aae7dc301b4a5ef0024f00e541d6f55b922a92e/research/computations/conditional_2_12_cubic_reduction_2026_10_21_family.m2);
- [full global C3 specialization](https://github.com/markluxton1/STCI/blob/934b6bafd7b255f58e3f9b3e93507afb57cb6266/research/computations/conditional_2_12_cubic_reduction_2026_10_21_candidates.py),
  [its exact equations](https://github.com/markluxton1/STCI/blob/c2e11996d7bb689d3a9a9156458b805330f1b541/research/computations/conditional_2_12_cubic_reduction_2026_10_21_candidates.m2),
  and [all sixteen nonzero specialized equations](https://github.com/markluxton1/STCI/blob/934b6bafd7b255f58e3f9b3e93507afb57cb6266/research/computations/conditional_2_12_cubic_reduction_2026_10_21_candidates.json);
- [lightweight exact certificate](https://github.com/markluxton1/STCI/blob/8775cf615047b7a878c436eab7bd9b0a0f039190/research/computations/conditional_2_12_cubic_reduction_2026_10_21_cont2_free_orbit_certificate.m2)
  and [historical successful run record](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/conditional_2_12_cubic_reduction_2026_10_21_cont2_free_orbit_certificate.json);
- [independent rational-arithmetic reconstruction](https://github.com/markluxton1/STCI/blob/ef8f99f8ff31c8bd4609833d467f9ee88d6123f9/research/computations/conditional_2_12_cont2_independent_unit_audit_2026_10_21.py),
  whose exact residual comparison and raw unit identity are explained below.

The lightweight certificate runs with
`M2 --script research/computations/conditional_2_12_cubic_reduction_2026_10_21_cont2_free_orbit_certificate.m2`.
It checks both exact ideal containments and then checks the final unit
identity by literal polynomial multiplication. It does not rely on a
unit marker from an interrupted large elimination. The historical run and the retirement replay both completed the two
exact ideal containments and the raw polynomial unit identity. The large
coefficient-lift dump adds no step to these checks.

## The norm-symbol equations collapse to a symmetric family

Put

```text
l=u+(z/2)v,
g=f(z,-z/2,1),
D=4g=d0+d1*z+d2*z^2+d3*z^3+d4*z^4.
```

On `d0*d4!=0`, projective scaling of `f` and the actual `C0` torus give
a finite cover on which `d0=d4=1`. This normalization preserves the
accepted chart: its weights are `wt(z,u,v)=(1,4,3)`.

For a primitive cube root `omega`, let

```text
U=1+d3*z^3, V=d1*z+z^4, W=d2*z^2,
alpha=U^2+V^2+W^2-U*V-U*W-V*W.
```

Thus `alpha=D(omega*z)*D(omega^2*z)`, and `D*alpha=N(z^3)` for a
quartic `N`. Multiplying `alpha` by a nonzero scalar does not change
the existence question.

Use the coordinates

```text
a=(d2+2y1-4y3, d3+2y2, 1),
b=(y0,y1,y2),
c=(1/4,d1/4+y0/2,y3).
```

Eight of the eleven global second-symbol equations vanish identically
under the norm substitution. The remaining three are linear in
`(y0,T=y1-4y3,y2)`. After nonzero constant row rescaling their matrix is

```text
J = [ d2-d1^2          -d1                  1          ]
    [ -2d1+d2*d3      -1-d1*d3+d2^2        2d3-d1*d2  ].
    [ 1                d3                  d2-d3^2    ]
```

Its determinant has the exact interpretation

```text
det J = Res_z(z^3-omega^2*d2*z+d1,
              -omega*d2*z^2+omega^2*d2*d3*z+1-d1*d3).
```

The resultant vanishes exactly when `D(z)` and `D(omega*z)` have a
common root in this endpoint chart. No condition that `D` itself be
squarefree is imposed. The identity is checked by the determinant of
the five-by-five Sylvester matrix over `QQ[omega]/(omega^2+omega+1)`.

The Cramer numerators are exactly
`(-d1/4,-d2/2,-d3/4)*det J`. Hence on `det J!=0` the second-symbol
condition is equivalent to

```text
y0=-d1/4, T=-d2/2, y2=-d3/4.
```

Writing `t=y3`, this gives the four-parameter root family

```text
a=(4t,d3/2,1),
b=(-d1/4,4t-d2/2,-d3/4),
c=(1/4,d1/8,t).
```

It is useful to see the geometry of the compression. With `w=-2u/v`,

```text
8*f(z,-w/2,1)
 =(8t+d3*z+2z^2)w^2
  +(d1+(2d2-16t)z+d3*z^2)w
  +(2+d1*z+8t*z^2)
```

is symmetric in `z,w`, restricts on the diagonal to `2D(z)`, and its
`t` term is `8t(z-w)^2`.

## First compatibility and the quadric part of C3 leave four points

Let `G0` be the accepted canonical first cubic correction over `K1`, and
put `G(z)=G0(z,-z/2,1)`. For a global sextic, restriction to the fixed
quadric gives

```text
F|Q=v^2 R(z^3+v).
```

Consequently the norm-symbol and actual cubic matching conditions imply

```text
D | Nprime_T(z^3)-4*alpha*G.
```

Since `D0=1` and `det J!=0`, both `z` and `alpha` are units modulo `D`.
Differentiating `N(z^3)=D*alpha` therefore makes this exactly equivalent
to the four remainder equations

```text
rem_D(Dprime-12*z^2*G)=0.
```

Eight accepted first-incidence equations eliminate
`h0,...,h3,h8,...,h11` without denominators on `d0=d4=1`. Substitute
the symmetric root family. In

```text
QQ[d1,d2,d3,t,h4,h5,h6,h7]
```

the remaining eight `K1` equations and these four q-line cubic equations
generate exactly the following triangular ideal:

```text
h6=0, h5=0, h4=-2h7, d3=0, d1=0,
t=(27/4)h7^3+(15/32)h7,
d2=108h7^3-(9/2)h7,
648h7^4+45h7^2-4=0.
```

Both ideal containments are verified over `QQ`, and the independent
audit reconstructs the same ideal from its own first/C3 construction.
The [augmented-matrix comparison](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/validation/2026-10-21-conditional-2-12-elimination/independent_family_ideal_audit.m2) replayed in Macaulay2 1.26.06 and gave the same dimension-zero,
degree-four ideal. Writing `h=h7`, one also has
`24th=1` and `d2=16t-12h`. The four points obey

```text
h^2=(-5+3sqrt(17))/144  or  (-5-3sqrt(17))/144.
```

They satisfy `det J!=0`: here `det J=(d2^2-1)^2` and
`d2^2=216h^2-11`, which is never one on the displayed quartic. This
observation is a consistency check; the exact ideal computation was
performed on a closed enlargement and did not discard the determinant
boundary during its calculation.

On this four-point scheme, `D=1+d2*z^2+z^4` has discriminant
`16*(d2^2-4)^2`. If `d2^2=4`, the relation `d2^2=216*h^2-11` forces
`h^2=5/72`, where `648*h^4+45*h^2-4=9/4`. Thus all four candidate
quartics are squarefree. This calculation uses the eight first and four
quadric cubic equations without a Schur pivot condition. The
[earlier discriminant certificate builder](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/validation/2026-10-21-conditional-2-12-elimination/schur_discD_qq_certificate_builder.m2) checks a smaller chart with a specified invertible pivot.

## Full global sextic C3 gives a two-line unit certificate

The actual degree-six second-symbol map has kernel exactly `k*q^3`.
Consequently every global sextic with second symbol `alpha*f` has the
fixed rational `k`-linear source splitting plus one coefficient `eta`
of `q^3`. The full cubic comparison is

```text
F3-alpha*G0+eta*q1^3 = f*(ell*u+m*v).
```

Its necessary polynomial syzygy equations are obtained from the actual
global source matrices. They retain the coefficient `eta`; no generic
`k(C0)` coefficients or hidden splitting of a second relation are used.
At the four-point scheme, two of those exact equations are

```text
E4=(3/4)eta+(369/16)h-(891/2)h^3,
E8=(1/8)eta+(27/32)h-(81/4)h^3.
```

Their difference is

```text
E4-6E8=18h-324h^3.
```

Let `p=648h^4+45h^2-4`. The following is a literal identity in
`QQ[h,eta]`:

```text
1 = ((162h^2-1)/4)*p
    +(81h^3+(77/8)h)*(E4-6E8).
```

The independent standard-library rational verifier reconstructs the
specialized full C3 equations from a separate source construction,
matches the equation directions, and checks this identity without a
Groebner basis. Therefore all four candidates fail actual global
sextic C3, and the free-orbit endpoint incidence is empty.

## Precisely what remains outside this result

The conclusion excludes every root in the stated chart, including
singular full roots whenever the accepted/proposed necessity bridges
apply. It does not require a smooth root or reduced diagonal divisor
`D`. It does not cover `d0*d4=0` or `det J=0`.

On the orbit-collision boundary, cancellation by `alpha` is invalid.
The exact retained condition is the multiplication of the four simple
remainders by the four-by-four multiplication matrix of `alpha` on
`k[z]/(D)`. Its determinant is exactly `81*(det J)^2`, as recorded in
the [all-strata q-line exporter](https://github.com/markluxton1/STCI/blob/934b6bafd7b255f58e3f9b3e93507afb57cb6266/research/computations/conditional_2_12_cubic_reduction_2026_10_21.json).
The collision and endpoint strata remain separate work; this proof
does not silently saturate them away.

No unrestricted STCI conclusion or full decision of the conditional
configuration follows from this chart exclusion alone. No global pair
has been realized.



## Consolidated historical supplement: `research/supplements/CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md`

Original mathematical content, hypotheses, qualifications, and proof status preserved verbatim. Relative links retain their historical source context.

# conditional 2 12 surface and symbol geometry

## Proof-dependency map: symbol equations to actual sextic realization

The [norm-symbol elimination](#2026-10-20-conditional-2-12-elimination) is an exact algebraic reduction in the conditional (2,12;6,16;2) setting. The [structured incidence](#2026-10-20-conditional-2-12-global-realization-incidence) combines root conditions with the [actual sextic symbol map](#2-the-exact-global-k-linear-symbol-map). Matching an [actual cubic jet](#7-first-unresolved-global-lift-the-actual-sextic-cubic-jet) is a further condition on that incidence. See the [independent incidence audit](#2026-10-20-conditional-2-12-incidence-audit) for the scope of these tests and the [realization certificate](#8-what-a-realization-would-have-to-certify) for what an actual pair must supply.

The [quadric-cycle norm](../synthesis/normalization_conductor_phase2_addendum.md#actual-quadric-cycle-norm-bridge) and [surface bound](https://github.com/markluxton1/STCI/blob/20b05fb7ee16f14e4e371c7e0dce7256ba11b480/research/supplements/CONDITIONAL_2_12_CONTINUATION_AND_SEXTIC_EXCLUSIONS.md#2026-10-21-conditional-2-12-geometric-audit-and-exceptional-locus) give additional restrictions under the actual supported-pair hypotheses.

The [singular gluing and conductor analysis](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/CONDITIONAL_2_12_SINGULAR_AND_CONDUCTOR.md#2026-10-20-conditional-2-12-singular-continuation) checks whether the local branches can be matched; the [strict-surface continuation](#nonnormal-conductor-budget-and-local-escape-models) introduces additional geometric hypotheses. A solution to the eight symbol equations is not, by itself, a projective sextic with the desired residual support.

Keep the explicit elimination, actual-lift polynomial test, and audit independently inspectable.

---


Permanent mathematical dossier. The (2,12) setting and every other hypothesis remain conditional as in the original arguments; full calculations, exceptional cases and failures are retained.

---

## 2026-10-20-conditional-2-12-elimination

# Conditional (2,12;6,16;2): compact norm-symbol and cubic realization incidence

Date: 2026-10-20. Status: **new exact reduction, pending independent review**. No result is changed. Work is over an algebraically closed characteristic-zero field, with the fixed curve C0 and the full generic ordinary coprime binary-CI initial ideal and actual saturated first relation required in the parent task. A bounded CAS interruption is process evidence only.

The source symbol matrix, exact image minor, and cubic layer are the new reviewed proposal in [the earlier global-realization note](#2026-10-20-conditional-2-12-global-realization-incidence). The first-incidence construction is the [STCI-R-0007](../results/quadratic_root_obstruction_model.md), used within its actual-CI interface and the separately reviewed finite singular-root bridge. The source script does not rerun accepted proofs.

## 1. Eight symbol equations are a norm factorization

Put `l=u+z*v/2`, the exact first symbol of the quadric `q=x0*x3-x1*x2`, and put

    D(z)=z^2*a(z)-2*z*b(z)+4*c(z)=sum(d_i*z^i,i=0..4).

The restriction of `alpha*f` to `l=0`, after the harmless scalar factor four, is `alpha*D`. The eight of the eleven symbol equations whose indices are not 3,6,9 say exactly that

    alpha(z)*D(z) belongs to span(1,z^3,z^6,z^9,z^12).

This has a geometric explanation: on the smooth quadric Q the sextic restriction is the square of the (1,3) curve equation times a section of O_Q(4,0), whose restriction to C0 is a binary quartic in z^3.

For four distinct roots of D in four distinct free mu3-orbits, the elementary factorization alone makes alpha unique up to scalar:

    alpha_can(z)=D(omega*z)*D(omega^2*z).

The exporter explicitly imposes `alpha_can`. The separate [quadric-cycle norm proof and its review](../synthesis/normalization_conductor_phase2_addendum.md#actual-quadric-cycle-norm-bridge) show why this is necessary for an actual supported pair under the full hypotheses, including shared orbits and endpoint multiplicities.

The formula needs no root of unity in the coefficient ring. With

    U=d0+d3*z^3, V=d1*z+d4*z^4, W=d2*z^2,

one has identically

    alpha_can=U^2+V^2+W^2-U*V-U*W-V*W,
    D*alpha_can=U^3+V^3+W^3-3*U*V*W.

The exporter checks symbolically that substitution of alpha_can makes exactly eight annihilator rows zero and leaves only rows 3,6,9 (zero-based indexing in the earlier symbol artifact).

## 2. A finite cover of the nonzero-endpoint chart

The C0-preserving torus acts by diag(1,lambda,lambda^3,lambda^4). Together with projective scaling of f, it permits the normalization d0=d4=1 wherever d0*d4 is nonzero: the two coefficients have torus weights differing by four, and the field is algebraically closed. Thus this is a finite cover of that chart; it does not cover endpoint-zero roots.

Choose four remaining root coordinates y0=b0,y1=b1,y2=b2,y3=c2. Then

    a=d2+2*y1-4*y3+(d3+2*y2)*z+z^2,
    b=y0+y1*z+y2*z^2,
    c=1/4+(d1/4+y0/2)*z+y3*z^2.

Writing T=y1-4*y3, the three surviving symbol equations are a linear system in (y0,T,y2). After dividing its first and third rows by four and its second row by two, the matrix is

    J = [ d2-d1^2       -d1       1          ]
        [ -2*d1+d2*d3   d2^2-1   2*d3-d1*d2 ]
        [ -1            -d3      d3^2-d2    ].

The constant vector is

    ((d3-d1*d2-d1^3)/4,
     (-d2-d1^2+d3^2-d1*d2*d3+d2^3)/2,
     (-d1-3*d2*d3+d3^3)/4).

Its determinant is minus

    d1^2*d2^2*d3^2-d1^2*d2^3-d1^3*d2*d3-d2^3*d3^2
    -d1*d2*d3^3+d2^4+2*d1*d2^2*d3+3*d1^2*d3^2
    -2*d2^2-4*d1*d3+1.

The exporter does **not** invert this determinant. All its rank-drop strata remain in the compact model. Changing y3 while keeping (d1,d2,d3,y0,T,y2) fixed adds `4*y3*l^2` to f; this explains why y3 is absent from the linear system.

## 3. Eight first-incidence correction variables disappear without denominators

On this chart a2=1,c0=1/4. The top four and bottom four equations of the accepted first incidence give the exact recurrences

    h3=-a0*h5-a1*h4,
    h2=-3-a0*h4-a1*h3,
    h1=-4*a1+3*b2-a0*h3-a1*h2,
    h0=-5*a0+3*b1-a0*h2-a1*h1,

    h8=-4*c1*h7-4*c2*h6,
    h9=-9/2-4*c1*h8-4*c2*h7,
    h10=-3*b0/2-16*c1-4*c1*h9-4*c2*h8,
    h11=-3*b1/2-14*c2-4*c1*h10-4*c2*h9.

Only h4,h5,h6,h7 remain. The exporter substitutes these expressions and verifies that precisely the original rows 0..3 and 12..15 become the zero polynomial. The other eight first equations are retained. Thus the base norm-symbol model on the smooth open has twelve variables and twelve equations: seven root coefficients, four h coefficients, one smooth inverse; eight first equations, three symbol equations, and the smooth-open equation. This is only an equation count, not a dimension computation.

## 4. An exact polynomial test for the actual sextic cubic lift

The fixed 22-by-22 image minor in the earlier symbol artifact defines a k-linear splitting rho. Every sextic with prescribed symbol alpha_can*f is

    rho(alpha_can*f)+eta*q^3.

Its cubic discrepancy from the canonical root correction is

    T=T0*u^3+T1*u^2*v+T2*u*v^2+T3*v^3
     =rho(alpha_can*f)_3+eta*l^3-alpha_can*G0.

The normal cubic is divisible by f in k[z,u,v] precisely when these four polynomial identities hold on the basepoint-free root locus:

    (b^2-a*c)*T0-a*b*T1+a^2*T2=0,
    b*c*T0-a*c*T1+a^2*T3=0,
    c^2*T0-a*c*T2+a*b*T3=0,
    c^2*T1-b*c*T2+(b^2-a*c)*T3=0.

To prove sufficiency, view multiplication by f as the rank-two bundle map O(7)^2 -> O(9)^4. The four displayed syzygies annihilate its image. Where a is nonzero, the first two syzygies are independent; where c is nonzero, the last two are independent; where a=c=0 and b is nonzero, the first and fourth are independent. They therefore span the entire rank-two annihilator at every point of a basepoint-free root. Vanishing of the four identities puts T in the image bundle. The corresponding quotient coefficients are global sections of O(7)^2. This retains zeros of alpha and does not divide by a,b,c or alpha in the final condition.

The compact exporter gives exactly 48 nonzero scalar coefficient equations from these four identities. It has thirteen variables including eta and the smooth inverse. The cubic equations are sufficient and necessary for the same cubic condition as the earlier 73-equation presentation on the specified open, provided the imposed norm multiplier is applicable. They do not replace the second obstruction, full spectral gluing/torsion, later sextic compatibility, or global degree-sixteen mate.

## 5. Reproduction and current computational boundary

Run

    python3 research/computations/conditional_2_12_elimination_2026_10_20.py

The exporter reconstructs the hierarchical model, whose M2 presentation reports `COMPACT_BASE_MODEL_READY` and `COMPACT_CUBIC_EQUATIONS=48`. This is an equation export, with no Groebner computation. The model is smooth-open only for the bounded CAS trial; singular-root strata remain in the parent structured incidence and are not excluded by this note.

The bounded QQ trials in `research/validation/2026-10-20-conditional-2-12-elimination/` preserve exact input files, return codes, and resource limits. Early expanded models and the first compact base model hit their 60-second CPU limits. These runs supplied **no ideal, dimension, unit, or emptiness certificate**. The final reduced cubic trial is recorded separately. No theorem may be inferred from a CPU-limited or killed process.

The precise unresolved computation is the intersection of these compact first/global-cubic equations with the inherited complete second test and full spectral torsion, together with the endpoint-zero charts. Even a nonempty answer would remain a low-order incidence rather than a global pair.


---

## 2026-10-20-conditional-2-12-global-realization-incidence

# Conditional (2,12;6,16;2): global sextic symbols and the exact remaining incidence

Date: 2026-10-20. Status: **new proposal / exact structured reduction**.
Independent audit of the new symbol map,
singular bridge, torsion presentation, and exporter is recorded in
[the audit](#2026-10-20-conditional-2-12-incidence-audit).

The output is a specified scheme of remaining necessary conditions and
its first unresolved global lifting condition. **Its emptiness or
nonemptiness is not certified.** In particular the familiar smooth seed
does not belong to the full second incidence. No low-order incidence
point is asserted to be a global pair.

## 1. Scope and inputs

Throughout, `k` is algebraically closed of characteristic zero and

    C0=[s^4:s^3t:st^3:t^4] in P3,
    E=N*_(C0/P3)=O_P1(-7)^2,
    (r,s;a,b;epsilon)=(2,12;6,16;2).

The conditional global object being tested is an actual proper pair
`F6,G16` with reduced intersection support exactly `C0`, FULL generic
ordinary initial ideal a coprime binary complete intersection of degrees
`(2,12)`, and ACTUAL degree-two relation kernel a saturated line
subbundle. The first relation is

    R=O(-16) -> Sym^2 E=O(-14)^3,
    f=a(z)u^2+b(z)uv+c(z)v^2,
    a=a0+a1*z+a2*z^2, similarly b,c.

The three homogeneous base quadratics have no common zero. The degree-six
symbol is necessarily `alpha*f`, with `alpha in H0(O(8))`, nonzero.
The degree-sixteen symbol is `beta*f`, `beta in H0(O(48))`, and in an
actual pair `(alpha,beta)` jointly generate at every point. The low-order
scheme below has no variable beta and does not assert that joint
generation has been realized.

Precisely scoped inherited premises:

* [STCI-R-0010](../results/saturated_first_relation_normal_flatness.md)
  gives normal flatness and a coprime `(2,12)` graded CI in every fiber
  under the actual supported-pair hypotheses above.
* [STCI-R-0008](../results/spectral_root_picard_criterion.md) makes the
  graded second quotient relation equivalent to the full-scheme spectral
  descent condition. Here it is `O_Z(1,-1)^12=O_Z` for the full `(2,2)`
  root `Z`.
* [STCI-R-0011](../results/moving_nonreduced_spectral_root_obstruction.md)
  excludes nonreduced moving full roots in characteristic zero; component
  degrees in the descent identity also force equal component slopes.
* [STCI-R-0007](../results/quadratic_root_obstruction_model.md) supplies
  the exact universal first incidence and complete twenty-five-pairing
  second obstruction test. Their construction is valid for all
  basepoint-free quadratic roots, including singular ones.

The smooth bridge R-0006 does not supply necessity on singular
roots. The new, separately reviewed finite bridge in
[the singular-root note, section 2](../supplements/SINGULAR_ROOT_ACTUAL_PAIR_BRIDGE.md)
fills this scope gap only under the actual hypotheses above. No inference
for residual intersections or arbitrary STCI presentations is made.

## 2. The exact global k-linear symbol map

For the fixed characteristic-zero quartic, the source calculation is
independent of the existence of a supported pair. The conormal frame
has transition `z^-7` in each summand, and `O_C0(6)=O_P1(24)`.
The map is the second normal jet
`H0(I_C0^2(6)) -> H0(Sym^2 E(6))=H0(O_P1(10))^3`.
Use the accepted balanced coordinates on `x0=1`:

    (x0,x1,x2,x3)=(1,z,z^3+v,z^4+u+(3/2)*z*v).

The degree-two normal symbols of a global sextic have the form

    P(z)u^2+Q(z)uv+R(z)v^2,             deg P,Q,R <= 10.

The coordinates in the target are, in order,

    (P0,...,P10,Q0,...,Q10,R0,...,R10).

Thus the target is `H0(O(10))^3`, of dimension 33. The map is obtained
by substituting these exact affine coordinates into the homogeneous
sextic, retaining its normal degree-two terms, and homogenizing their
base coefficients to degree ten. All coefficients are in `k`; they
are not freely chosen elements of `k(C0)`.

For a completely reproducible source basis put

    q=x0*x3-x1*x2,
    A=x0^2*x2-x1^3,
    B=x0*x2^2-x1^2*x3,
    D=x2^3-x1*x3^2.

In the following order, a basis of `H0(I_C0^2(6))` is

    q^2*(x0^2,x0*x1,x0*x2,x0*x3,x1^2,x1*x2,x1*x3,x2^2,x2*x3,x3^2),
    q*A*(x0,x1,x2,x3),
    q*B*(x2,x3), q*D*(x2,x3),
    A^2,A*B,A*D,B*D,D^2.                                  (1)

The source dimension is 23, the symbol rank is 22, and the kernel is
exactly `k*q^3`. The exact `33 x 23` matrix M and a `33 x 22` image
basis are in
[the symbol JSON](../computations/conditional_2_12_symbol_map_2026_10_20.json).
Omitting `q^2*x1*x2` from (1) gives that image basis, since
`q^2*x0*x3-q^2*x1*x2=q^3` generates the kernel. Its minor on
target rows `P0,...,P10,Q0,...,Q9,R0` has determinant exactly 48.
There is also a compact equation presentation of the image `V_(6,2)`:

    P9-2Q10 = 0,
    Q0-2R1 = 0,
    P0-2Q1+4R2 = 0,
    3P1-2Q2-4R3 = 0,
    P2-2Q3+4R4 = 0,
    P3-2Q4+4R5 = 0,
    P4-4R6 = 0,
    P5-2Q6+4R7 = 0,
    P6-2Q7+4R8 = 0,
    P7+2Q8-12R9 = 0,
    P8-2Q9+4R10 = 0.                                      (2)

These eleven independent equations cut out the entire image, not a
necessary superspace of it. The new calculation checks the 84 ambient
sextic monomials: the zeroth/first normal jet matrix has rank 61.
Its kernel therefore has dimension 23, and the independent products
(1) span it. Vanishing of these jets on the dense affine curve extends
globally because the successive targets `O_C0(6)` and `E(6)` are vector
bundles on the integral curve. This establishes the sheaf-square source
and does not silently substitute an unsaturated homogeneous square.
Rank 22 and the explicit element `q^3` identify the kernel.

The independent verifier reconstructs symbols by a different direct
binomial expansion, checks first-jet rank 61, and checks rank 22,
rank 11, and `L*M=0`. The computations are over QQ and base-change to
every characteristic-zero field.

## 3. Eleven bilinear global-symbol equations

Write `alpha=sum_(i=0)^8 alpha_i*z^i`. In (2), substitute

    Pj=sum_(i=0)^8 alpha_i*a_(j-i),
    Qj=sum_(i=0)^8 alpha_i*b_(j-i),
    Rj=sum_(i=0)^8 alpha_i*c_(j-i),                         (3)

where a coefficient with index outside 0,1,2 is zero. Equations
(2)-(3) are the exact eleven bilinear equations for
`alpha*f in V_(6,2)`. Require `alpha !=0`, but do not invert alpha as
a function on the curve. Its zeros are part of the problem.

For fixed `(f,alpha)` satisfying (3), all possible actual global
sextics with that symbol form an affine line

    F=F0(alpha*f)+eta*q^3,                  eta in k.       (4)

The symbol restriction is not automatic on the universal first
incidence. At its known smooth first-compatible torsion-two seed,

    f0=(z^2+4)u^2+(z^2-8)v^2,

the eleven-by-nine multiplier matrix has rank eight, giving precisely
one projective multiplier,

    alpha0=z^8-8z^6+96z^4+256z^2+1024.                     (5)

The second obstruction at this seed is `1/8`, so it lies outside the
combined incidence. The [cubic comparison](#7-first-unresolved-global-lift-the-actual-sextic-cubic-jet)
also excludes all of its actual sextic lifts.

At `(f0,h0,alpha0)`, adjoining the eleven equations to `A_f h=d_f`
gives a Jacobian of rank 26 in 27 rows and 30 affine variables
`(f9,h12,alpha9)`. Removing the two projective scaling directions gives
tangent dimension two. The rank-eight multiplier minor stays invertible
on a neighborhood of the seed. On that neighborhood in the membership
locus it determines the normalized multiplier regularly, so the projected
incidence has the same tangent dimension. The first incidence `K1` is
smooth of projective dimension four at `[f0]`. Thus symbol membership
removes first-compatible tangent directions. The calculation is local
to the seed, with no dimension conclusion for the full incidence or its
intersection with the second obstruction and spectral torsion. The
[independent reconstruction](#2-independent-linear-algebra-reconstruction)
checks the Jacobian against the saved first-incidence input.

## 4. Necessity of both ambient tests at singular roots

The newly reviewed bridge is short enough to make the new hypothesis
interface explicit. At any closed base point, R-0010 supplies a local
relative initial ideal `(f2,g12)` with coprime fiber symbols. Choose
actual local lifts `P,H` in the ideal, of orders 2 and 12. Initial-order
reduction and Krull intersection give `I=(P,H)` in the actual local
ring. The pair `(F,G)` differs by an invertible matrix.

On the blowup divide BOTH original equations by the same exceptional
power `t^2`. Near each point of the full root, `H/t^12` is a unit by
fiberwise coprimality, so the actual transformed ideal is

    (P/t^2,t^10*H/t^12)=(p,t^10).                          (6)

The restriction `p mod t` is the Cartier equation of the root on E;
therefore `(p,t)` is a regular sequence, including at singular root
points. The principal ideals modulo `t^10` glue from the actual ideal
and give compatible embedded Cartier lifts through `E9`. Smoothness
of the surface `(p)` is unnecessary. This proves necessity of the
first and second obstruction tests for this conditional configuration.
It does not construct such a lift from an arbitrary incidence point.

Let `FIRST(f,h)` be the sixteen equations `A_f*h=d_f`, with the exact
matrix and Cech bases of R-0007; `h` has twelve coordinates and is
unique when it exists. Let `SECOND(f,h)` be ALL twenty-five Plucker
residues from the accepted global compression, not a selected subset
or a coefficient-chart test. The exporter uses exactly these inherited
equations, without their old smooth-discriminant inverse. No inherited
proof or seed verifier is rerun.

## 5. Full spectral torsion, root types, and actual gluing

Set `S=P1_base x P1_direction`, `Z=(f)`, and `L=O_Z(1,-1)`.
The nonreduced-root obstruction and the component degree of
`L^12=O` restrict Z to a reduced integral `(2,2)` curve or two distinct
`(1,1)` components. Nonreduced fibers of either degree-two projection
are allowed; the full curve is reduced.

Uniformly for every `(2,2)` Cartier divisor,

    0 -> O_S(-1,-3) -> O_S(1,-1) -> L -> 0

gives `H0(Z,L)=0`; in particular `L` is never trivial. This gives the
following exact interpretation of the spectral locus.

| Root type | Condition and outcome |
| --- | --- |
| Smooth integral genus one | Retain the actual nonidentity `L in Pic^0(Z)[12]`. |
| Integral nodal | Retain its actual conductor identification `lambda in k*`, with `lambda^12=1`, `lambda!=1`. |
| Integral cuspidal | `Pic^0=G_a` is torsion free in characteristic zero; excluded. |
| Two transverse `(1,1)` components, two nodes | Retain `lambda=g1/g2`, the ratio of the two actual node identifications; `lambda^12=1`, `lambda!=1`. |
| Two tangent `(1,1)` components | The length-two conductor gluing gives `Pic^0=G_a`; excluded. |

For the nodal case the degree-zero pullback to the rational
normalization is always trivial. That fact discards the obstruction
unless the two fibers over the node are also identified. For the
two-node pair both identifications must be retained; either one alone
can be normalized away. Explicit invariant formulas, the conductor
jets in the additive cases, and the finite bridge proof are in
[the gluing note](../supplements/SINGULAR_ROOT_ACTUAL_PAIR_BRIDGE.md).

A sparse matrix retains all these conditions in the ORIGINAL nine
coefficients, without choosing normalization coordinates:

    T12(f): H1(O_S(10,-14)) -> H1(O_S(12,-12)),
    H0(Z,L^12)=ker T12(f).                                  (7)

Both spaces have dimension 143. In affine direction `w=v/u`, use
source basis `z^i*w^m`, `0<=i<=10,-13<=m<=-1`, and target basis
`z^j*w^n`, `0<=j<=12,-11<=n<=-1`. With
`f=sum f_(p,q) z^p w^q`, the matrix entry is

    T12[(j,n),(i,m)]=f_(j-i,n-m)                            (8)

if both differences are in 0,1,2, and zero otherwise. This matrix has
1089 nonzero polynomial entries and determinant homogeneous degree143.
On the reduced equal-slope locus a nonzero section of `L^12` is
nowhere zero: its degree on every component is zero and connectedness
propagates nonvanishing. Thus `det T12=0` is exactly full triviality,
including gluing. On this zero locus the matrix has corank one, so
the projective nonzero-kernel incidence and the determinant zero
scheme are locally isomorphic; neither forgets infinitesimal scheme
structure. The explicit relative argument is in the gluing note.

## 6. The exact remaining scheme

Here is one open coefficient presentation of the reduced equal-slope
root locus, avoiding an unspecified union of charts. For three binary
quadratics `p,q,r`, let `S(p,q,r)` be the 4x6 matrix whose columns
are the coefficient vectors of `p,zp,q,zq,r,zr` in homogeneous
degree three. Define B inside P8 by

    rank S(a,b,c)=4,
    rank S(a0+b0*w+c0*w^2,
           a1+b1*w+c1*w^2,
           a2+b2*w+c2*w^2)=4,
    not all coefficients of b^2-4*a*c are zero.             (9)

The first rank means finite flat over the base; the second excludes
constant-direction components. The last means generically separable,
hence reduced in characteristic zero. A reduced `(2,2)` divisor
finite over both rulings is either integral or the union of two
`(1,1)` curves. Consequently (9) loses no spectral-torsion candidate
and precisely supplies the locus needed for (7). It imposes no
smoothness discriminant inverse.

On the affine cone over B, define the remaining necessary incidence

    S2 = { (f,h,alpha,[v]) :
             L*coeff(alpha*f)=0,
             FIRST(f,h)=0,
             SECOND(f,h)=0,
             T12(f)*v=0,
             alpha!=0, [v] in P142 } / (G_m x G_m).        (10)

The two quotient scalings are `f -> lambda*f` and
`alpha -> mu*alpha`; h is invariant. The projective v has its own
usual scalar quotient. This is 11 symbol equations, 16 first
equations, 25 COMPLETE second equations and 143 sparse linear-kernel
equations. It is equivalently the incidence with `det T12(f)=0`
and no v. All constructions are over QQ and then base-change to k.

Equation (10), including the open (9), is the precise remaining
scheme supplied here. It has the smooth-root locus and the full
nodal and two-node gluing conditions; cusps and tangent pairs have
no points in its torsion part by section 5. No statement about its
nonemptiness, components, or dimension is made without an exact
calculation. In particular failure to carry out elimination is not
evidence of survival.

The exporter writes this ideal using 173 affine cone variables; it
also adjoins 39 otherwise unused variables for the optional next
global lift. Restrict to the specified five opens and take the three
scalar quotients to read (10). `D(J)` means complement of `V(J)`;
one must not invert every generator of an open ideal, which would
discard charts. No saturation or elimination was launched.

## 7. First unresolved GLOBAL lift: the actual sextic cubic jet

K1 and K2 say the ROOT admits its first two compatible embedded
corrections. They do not imply that the actual sextic coefficients
allowed by (1) vanish on that lift. On K1 let `G0` be the canonical
first-chart cubic correction from the accepted construction
(`G0=nonnegative_z(S3)`). It has base degree at most one.

Take actual GLOBAL coefficients `c=(c0,...,c22) in k^23` in (1).
Let C be the `40 x 23` cubic-jet matrix in the symbol JSON, ordered
by `z^j*u^(3-i)*v^i`, `i=0..3,j=0..9`. The first unresolved global
condition is the following finite incidence extending (10):

    M*c=coeff(alpha*f),
    C*c-coeff(alpha*G0)=coeff(f*(ell(z)*u+m(z)*v)),
    deg ell,m <= 7.                                       (11)

There are 33 symbol and 40 cubic equations in the 23 actual global
sextic coefficients and 16 quotient coefficients. Equivalently,
using (4), the condition is

    [ F_(0,3)(alpha*f)+eta*(u+(1/2)z*v)^3-alpha*G0 ] mod f=0.

The first-chart degrees satisfy `deg F3<=8` and `deg(alpha*G0)<=9`.
Basepoint freeness at infinity makes the collective base degree of `f`
equal to two. The leading binary forms of `f` and a nonzero quotient
linear form have nonzero product, so the quotient has degree at most seven.
The residue is intrinsically a global section of `O_Z(3,3)`
(dimension 12), so its vanishing over this dense chart extends to
infinity. A change of cubic representative by a multiple of `f` is
absorbed by the quotient coefficients. The test uses polynomial
divisibility and retains every zero of `alpha`.

For the seed in section 3, `G0=(z/8)u^2v-(3/4)uv^2+(z/8)v^3`.
The `73 x 39` system (11) has coefficient rank 39 and augmented rank 40.
The [exact annihilating row](../synthesis/normalization_conductor_phase2_addendum.md#exact-failed-seed-the-row-also-kills-the-free-lift)
annihilates all 23 sextic and sixteen correction columns, including the
cubic direction of `q^3`, and pairs with the target to `-384`. This
excludes the entire affine line (4) at that seed. The independent audit
reconstructs the [matrices and pairing](#2-independent-linear-algebra-reconstruction).

The exporter supplies the equations (11) as `nextGlobalLiftIdeal`,
but their feasibility on S2 has not been determined. This is the
first unresolved condition in GLOBAL lifting. The next ABSTRACT
root-lifting obstruction is different: after the two accepted stages
it is the normal degree-five correction, or exceptional stage E3.
Even solving (11) would still leave quartic and higher sextic
compatibility, higher root stages through E9, and the global mate.

## 8. What a realization would have to certify

An abstract graded second quotient relation is not a globally split
polynomial generator. Neither the projective torsion vector in (10)
nor the quotient coefficients in (11) are a degree-sixteen equation.
A realization requires actual homogeneous `F6,G16` with coefficients
in k. In the actual two-dimensional generic local ring along C0,
one must exhibit invertible generator operations producing order-two
P and order-twelve H, verify all required cancellations through
order eleven, and show that the FULL resulting initial forms
`f2,g12` are coprime. With coprime initial forms the standard-basis
criterion gives the full initial ideal `(f2,g12)` and length
`2*12=24`; merely finding a degree-twelve relation does not.

One must also prove the global homogeneous gcd is one. Bézout then
gives the complete intersection degree `6*16=96`, while C0 already
contributes `4*24=96`. Purity of the complete intersection leaves
no residual curve or isolated embedded component. This is the
global support argument; a generic finite-jet calculation cannot
replace the gcd check. The necessary implication used earlier
assumed sole reduced support; this sufficiency check does not assume
the desired conclusion in advance.

The new global-symbol restriction is an exact obstruction to
realization and is not automatic on first-compatible roots. It has
not been shown to empty the second-compatible spectral locus. The
structured residual scheme (10) and the next concrete global
condition (11) are the stopping point, as requested.

## 9. Reproduction and verification limits

The [symbol producer](../computations/conditional_2_12_symbol_map_2026_10_20.py)
writes the [exact matrices and seed certificate](../computations/conditional_2_12_symbol_map_2026_10_20.json).
The tangent comparison reads the [saved first-incidence Jacobian](../computations/generalization_quadratic_root_curve_universal_incidence.json).
Its SHA256 is recorded in the symbol output. The
[independent direct-binomial verifier](https://github.com/markluxton1/STCI/blob/8f7fc950c8868d2e02d98c31bb028d15930f9dd1/research/computations/conditional_2_12_symbol_independent_audit_2026_10_20.py)
reconstructs the symbol matrices and seed ranks over the rationals.
Its JSON report was reproduced byte for byte during retirement.
[Historical reconstruction report](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/conditional_2_12_symbol_independent_audit_2026_10_20.json).
The [structured exporter](../computations/conditional_2_12_structured_incidence_2026_10_20.py)
uses the [inherited first and second equation generator](../computations/generalization_quadratic_root_global_second_model.py).

Run from the repository root in a scratch checkout, since these scripts
write their outputs next to the inputs. The Python scripts use only the
standard library.

The archived command uses [conditional_2_12_symbol_independent_audit_2026_10_20.py](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/conditional_2_12_symbol_independent_audit_2026_10_20.py) from the pinned repository snapshot.

```sh
python3 research/computations/conditional_2_12_symbol_map_2026_10_20.py
python3 research/computations/conditional_2_12_symbol_independent_audit_2026_10_20.py
python3 research/computations/conditional_2_12_structured_incidence_2026_10_20.py
M2 --script research/computations/conditional_2_12_structured_incidence_2026_10_20.m2
```

The final command constructs the ideals and reports `STRUCTURED_MODEL_READY`
and `NEXT_GLOBAL_LIFT_EXPORTED`. This checks the equation presentation.
Elimination, nonemptiness and realization remain open at this level.




---

## 2026-10-20-conditional-2-12-incidence-audit

# Independent audit of the conditional (2,12;6,16;2) incidence

Date: 2026-10-20. Reviewer: `incidence_audit` worker, separate from the
symbol-map and singular-gluing authors.

Status: **PASS for the exact reductions specified below; no
emptiness certificate, nonemptiness certificate, or global realization.**

## 1. Scope and dependencies

The field is algebraically closed of characteristic zero, the curve is
`C0=[s^4:s^3t:st^3:t^4]`, and the conditional actual pair has degrees
`6,16`, FULL generic coprime binary ordinary initial CI `(2,12)`, and
ACTUAL saturated first relation `R=O(-16) -> Sym^2 E`, with
`E=O(-7)^2`. Thus the first root is a basepoint-free form `f` of class
`(2,2)`. All actual-CI necessity statements also require sole reduced
support `C0`; residual intersections are outside this bridge.

inputs are [R-0010](../results/saturated_first_relation_normal_flatness.md),
[R-0011](../results/moving_nonreduced_spectral_root_obstruction.md),
[R-0008](../results/spectral_root_picard_criterion.md), and the literal
universal obstruction model in
[R-0007](../results/quadratic_root_obstruction_model.md). Their inherited
proof computations were not rerun. The singular finite bridge reviewed
here is a **new argument**, not a silent extension of R-0006.

The new source artifacts reviewed are
[symbol-map generator](../computations/conditional_2_12_symbol_map_2026_10_20.py),
[symbol data](../computations/conditional_2_12_symbol_map_2026_10_20.json),
[singular-gluing proposal](../supplements/SINGULAR_ROOT_ACTUAL_PAIR_BRIDGE.md),
and [combined exporter](../computations/conditional_2_12_structured_incidence_2026_10_20.py).

## 2. Independent linear-algebra reconstruction

The new independent program

The archived command uses [conditional_2_12_symbol_independent_audit_2026_10_20.py](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/conditional_2_12_symbol_independent_audit_2026_10_20.py) from the pinned repository snapshot.

    python3 research/computations/conditional_2_12_symbol_independent_audit_2026_10_20.py

uses standard-library rational arithmetic to reconstruct the matrices
independently of the producer. The [historical report](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/conditional_2_12_symbol_independent_audit_2026_10_20.json) records the
following exact checks.

1. For a degree-six monomial `x0^a x1^b x2^c x3^d`, put
   `e=b+3c+4d`. Its restriction, `x2` derivative, and `x3` derivative
   have coefficients respectively `1*z^e`, `c*z^(e-3)`, and
   `d*z^(e-4)`. The resulting first-jet matrix has rank `61` among
   the `84` sextic monomials. Hence `h0(I_C0^2(6))=23`.
2. The 23 supplied global source polynomials have independent ambient
   coefficient vectors and vanish to first order, so they span the
   full sheaf section space rather than just a degree-six ideal-product
   subspace.
3. Independently expanding
   `x2=z^3+v`, `x3=z^4+u+(3/2)zv` reconstructs the entire `33 x 23`
   second-symbol matrix, and also the `40 x 23` cubic-layer matrix.
   For the second layer, choosing `p` copies of `v` from `x2`, and
   `q,r` copies of `u,(3/2)zv` from `x3`, uses `p+q+r=2` and scalar

       binom(c,p) multinomial(d;q,r,d-q-r) (3/2)^r,

   with base exponent `b+3(c-p)+4(d-q-r)+r`. Cancellations are
   performed before checking the stated base-degree bounds.
4. The full symbol matrix and its 22 proposed image columns have rank
   `22`. The eleven supplied annihilators are independent and kill
   the full symbol matrix. Thus they cut out its image exactly.
5. The NEW seed membership matrix has rank eight and the stated
   multiplier lies in its kernel. Using the saved accepted first
   Jacobian as input, independently differentiating the eleven new
   equations gives combined Jacobian rank 26, so the claimed
   projective tangent dimension two is correct. The independent
   cubic comparison has matrix rank 39, augmented rank 40; the
   displayed witness kills every source/quotient column and pairs
   with its target to `-384`. This checks only the new comparisons,
   without reopening the already obstructed seed.

The kernel is one-dimensional. The nonzero polynomial `q^3`, where
`q=x0*x3-x1*x2`, has order three along the curve and belongs to the
source, so it is precisely that kernel. These checks establish the
requested linear map and image; they do not establish any root or
ambient incidence nonempty.

## 3. Finite bridge at singular roots

The new proof in the singular-gluing note passes the following
independent reconstruction. R-0010 gives the FULL relative graded
ideal locally generated by `f2,g12`, coprime in every fiber. Local
lifts `P,H` in the actual ideal generate it: normal-order reduction
puts the ideal inside `(P,H)+I_C^N` for every `N`, and Krull
intersection in the actual local quotient gives equality. Since
both these and the original two equations minimally generate the
same height-two CI ideal, their change matrix is invertible in the
actual local ring.

The original order-two symbols jointly generate the line subbundle
`R`. Their coefficients `alpha` of degree `8` and `beta` of degree
`48` therefore have no common base zero. Both are nonzero, since a
single section of either positive-degree line bundle cannot generate
everywhere. Divide BOTH original equations by the common exceptional
order two. At every root point, the transformed ideal is

    (P/t^2, t^10 H/t^12)=(p,t^10),

because the reduction of `H/t^12` is nonzero at every root direction
by the fiberwise coprimality. No smoothness of `f=0` is needed.
The sequence `(t,p)` is regular because `p mod t` is the Cartier
equation of the root in the smooth exceptional surface. Thus modulo
`t^10` the local ideals are Cartier and glue as the same actual
transformed ideal. This gives the embedded lift through `E9`, so the
first and second ambient classes necessarily vanish also at singular
roots. The argument retains the exceptional power `t^10` throughout.

The review found no use of a UFD on a singular strict surface, no
replacement of the actual local ring by its generic fiber, and no
saturation that removes exceptional structure. **PASS under the
stated actual supported-CI hypotheses.**

## 4. Root strata and the torsion presentation

R-0011 forces a reduced equal-slope root, hence an integral `(2,2)`
curve or two distinct `(1,1)` curves. The universal restriction
sequence

    0 -> O(-1,-3) -> O(1,-1) -> L -> 0,

gives `H0(L)=0`, so `L=O_Z(1,-1)` is never trivial. The generalized
Jacobian of a cuspidal root, or of two `(1,1)` components tangent
at one length-two intersection, is additive and has no nonzero
12-torsion in characteristic zero. These strata are excluded.
For an integral nodal root the actual branch gluing parameter is in
`G_m`; for two transverse nodes it is the ratio of the two conductor
identifications. In either case the condition is `lambda^12=1`,
with `lambda != 1`. Normalization degrees alone would erase it.

The singular note's ruling-coordinate formula for the integral nodal
parameter was checked: if `x=[X0:X1]`, `y=[Y0:Y1]` on the normalization
and `p,q` map to the node, then

    lambda=Yj(p) Xi(q)/(Xi(p) Yj(q))

in charts nonzero at the node. The equal homogeneous degrees make
this independent of lifts of `p,q`; changing branch order inverts it.

The torsion sequence

    0 -> O(10,-14) --f--> O(12,-12) -> L^12 -> 0

has two 143-dimensional `H1` groups and zero ambient `H0`. The
proposed matrix entries are the correct multiplication entries:

    T[(k,ell),(i,j)]=f_(k-i,j-ell),

for `0<=i<=10`, `1<=j<=13`, `0<=k<=12`, `1<=ell<=11`, with out-of-range
coefficients zero. A nonzero kernel is equivalent to a section of
`L^12`. On the connected reduced equal-slope locus a nonzero section
of a multidegree-zero line bundle is nowhere zero: nonvanishing
propagates between components through their intersections. Thus this
is equivalent to `L^12=O_Z`, including the actual nodal gluing data.
At a torsion point the matrix has corank one; an invertible
142-minor gives a local scalar presentation by its determinant.
Projectivizing the nonzero kernel vector has the same local scheme
structure. Relative triviality allows the usual line bundle pulled
back from the coefficient base; no global choice of trivialization
over all parameter space is asserted.

The combined exporter imposes rank four on the two `4 x 6`
quadratic Sylvester multiplication matrices. These conditions mean
that the root is finite in both rulings. Along with a nonzero
binary discriminant polynomial, they imply exactly the reduced
integral/two-`(1,1)` alternative above. Consequently they remove
unbalanced reducible roots before using the kernel criterion. This
order matters: on an unbalanced reducible root a section can be
supported on one component, and a zero determinant alone would give
a false torsion test. **PASS for the specified open scheme.**

## 5. The first unresolved global lift is genuinely additional

The bare structured scheme combines eleven symbol-image equations,
sixteen universal first equations, twenty-five complete second
pairings, and 143 torsion-kernel equations, on the opens just
specified, with nonzero `alpha` and nonzero projective kernel vector.
No elimination has proved that scheme empty or nonempty.

Its first unresolved GLOBAL lifting condition is already cubic.
Write `F=sum c_i B_i` in the 23 actual global sextic basis elements.
The symbol condition is `M c=coeff(alpha*f)`. If the first embedded
root lift on the first base chart is `f+G0`, the actual pair would
give, below normal degree twelve, `F=A*P`. Consequently

    F3-alpha*G0 = f*(ell(z) u+m(z) v).                  (*)

This must hold with actual global sextic coefficients `c_i in k`.
One must never divide by `alpha`, since it necessarily has base
zeros. The symbol condition determines `F` only modulo `k*q^3`;
that one freedom does not remove the necessity of (*).

The exported extension keeps all 23 coefficients and imposes the
33 symbol equations and 40 cubic coefficient equations, with
`deg ell,deg m<=7`. These bounds are sufficient: the numerator in
(*) has base degree at most nine, while the collectively degree-two
form `f` has nonzero top coefficient vector on the basepoint-free
infinity chart. Polynomial divisibility on the affine chart is
equivalent to vanishing of the resulting global residue on the full
reduced root, so it retains the points over infinity. Geometrically
this residue belongs to `H0(O_Z(3,3))`, of dimension `16-4=12`.

The extension is exported as the **next condition**, not claimed
soluble. The next abstract ambient root obstruction after the
complete second test is normal degree five (`E3`). That abstract
condition is distinct from matching the globally permitted sextic
jets; it cannot replace (*).

## 6. Eventual realization certificate and stopping boundary

Even if the low-order or cubic extension has a point, actual
realization still requires homogeneous `F6,G16` with coefficients
in `k`, compatible higher jets, and no common global polynomial
factor. Over `K=k(C0)`, a finite degree-twelve standard-basis
certificate may be expressed by a truncated multiplier `Q` such
that

    H=G-QF has order 12,
    gcd(in_2(F),in_12(H))=1 in K[u,v].

The vanishing of all normal terms of `H` below twelve and the full
binary resultant nonvanishing are mandatory. The invertible
generator change then makes the coprime regular initial pair a
standard basis; a partial common-root test or isolated leading
symbol cancellation is insufficient. The resulting local CI length
is `2*12=24`.

Finally the global gcd condition makes `(F,G)` a proper projective
CI of degree `6*16=96`. Its contribution along `C0` is
`24*deg C0=24*4=96`; effectiveness and purity then leave no residual
curve, and no isolated component of this projective CI. This is
the required global gcd/Bezout step, conditional on the actual
global equations. No equation search or realization is undertaken
here; the present contribution stops at the structured incidence
and its explicit first missing global lift.

## 7. Final assembled-note review

The final [assembled proposal](#2026-10-20-conditional-2-12-global-realization-incidence)
was reviewed against the source order, target order and exact JSON.
The source basis list and eleven image forms have the correct
indices. The independent determinant of the indicated 22-row
image minor is `48`. The T12 exponent convention with negative
Laurent powers uses direction difference `n-m`, as written in the
assembled note and exporter; the singular note's positive indices
give the equivalent difference `j-ell`.

The new tangent comparison proves nonautomatic membership on K1
only; the cubic seed certificate does not newly exclude a point
of the full second incidence, and the assembled note states that
limitation. The scheme's nonemptiness remains unproved. The
eventual global gcd/Bezout paragraph correctly requires actual
global equations first and does not infer support solely from a
low-order incidence. No current mathematical defect was found in
these scoped claims. Final outcome: **PASS for the exact structured
reduction, proposed singular bridge and first unresolved global
lift; a global realization remains outside
this review.**


### Retired source certificate: `research/computations/conditional_2_12_cubic_reduction_2026_10_21.json`

Historical source retained verbatim, including limitations and external dependencies. Relative file paths in archived code refer to the original repository location.

<details><summary>Original source</summary>

```json
{
  "status": "new exact q-line reduction; no emptiness assertion",
  "input": "/Users/markluxton/Projects/STCI/research/computations/conditional_2_12_elimination_2026_10_20.py",
  "input_sha256": "66d8c0d841cc12d664b5188f72c943d85411e3c0617aeb4d6f0cef96c9277713",
  "chart": "d0=d4=1 finite projective/torus cover over nonzero endpoints",
  "variables": [
    "d1",
    "d2",
    "d3",
    "y0",
    "y1",
    "y2",
    "y3",
    "h4",
    "h5",
    "h6",
    "h7"
  ],
  "equations": {
    "K1": 8,
    "norm_symbol": 3,
    "qline": 4
  },
  "simple_qline": "rem_D(Dprime-12*z^2*G)",
  "all_strata_qline": "rem_D(alpha*(Dprime-12*z^2*G)); equivalent to rem_D(Nprime_T(z^3)-4*alpha*G) since 3*z^2 is a unit modulo D with D0=1",
  "alpha_multiplication_matrix": [
    [
      "3-3*d2*d2+6*d2*d3*d3-3*d3*d3*d3*d3",
      "-6*d3+3*d1*d3*d3+6*d2*d2*d3-9*d2*d3*d3*d3+3*d3*d3*d3*d3*d3",
      "-3*d2+9*d3*d3+3*d1*d2*d3+3*d2*d2*d2-6*d1*d3*d3*d3-12*d2*d2*d3*d3+12*d2*d3*d3*d3*d3-3*d3*d3*d3*d3*d3*d3",
      "12*d2*d3+3*d1*d2*d2-12*d3*d3*d3-12*d1*d2*d3*d3-9*d2*d2*d2*d3+9*d1*d3*d3*d3*d3+21*d2*d2*d3*d3*d3-15*d2*d3*d3*d3*d3*d3+3*d3*d3*d3*d3*d3*d3*d3"
    ],
    [
      "-3*d2*d3-3*d1*d2*d2+3*d3*d3*d3+6*d1*d2*d3*d3-3*d1*d3*d3*d3*d3",
      "3-6*d1*d3-3*d2*d2+6*d2*d3*d3+3*d1*d1*d3*d3+6*d1*d2*d2*d3-3*d3*d3*d3*d3-9*d1*d2*d3*d3*d3+3*d1*d3*d3*d3*d3*d3",
      "-6*d3-3*d1*d2+12*d1*d3*d3+6*d2*d2*d3+3*d1*d1*d2*d3+3*d1*d2*d2*d2-9*d2*d3*d3*d3-6*d1*d1*d3*d3*d3-12*d1*d2*d2*d3*d3+3*d3*d3*d3*d3*d3+12*d1*d2*d3*d3*d3*d3-3*d1*d3*d3*d3*d3*d3*d3",
      "-3*d2+9*d3*d3+15*d1*d2*d3+3*d2*d2*d2+3*d1*d1*d2*d2-18*d1*d3*d3*d3-12*d2*d2*d3*d3-12*d1*d1*d2*d3*d3-9*d1*d2*d2*d2*d3+12*d2*d3*d3*d3*d3+9*d1*d1*d3*d3*d3*d3+21*d1*d2*d2*d3*d3*d3-3*d3*d3*d3*d3*d3*d3-15*d1*d2*d3*d3*d3*d3*d3+3*d1*d3*d3*d3*d3*d3*d3*d3"
    ],
    [
      "3*d2-3*d3*d3-3*d1*d2*d3-3*d2*d2*d2+3*d1*d3*d3*d3+6*d2*d2*d3*d3-3*d2*d3*d3*d3*d3",
      "-9*d2*d3-3*d1*d2*d2+3*d3*d3*d3+9*d1*d2*d3*d3+6*d2*d2*d2*d3-3*d1*d3*d3*d3*d3-9*d2*d2*d3*d3*d3+3*d2*d3*d3*d3*d3*d3",
      "3-6*d1*d3-6*d2*d2+15*d2*d3*d3+3*d1*d1*d3*d3+9*d1*d2*d2*d3+3*d2*d2*d2*d2-3*d3*d3*d3*d3-15*d1*d2*d3*d3*d3-12*d2*d2*d2*d3*d3+3*d1*d3*d3*d3*d3*d3+12*d2*d2*d3*d3*d3*d3-3*d2*d3*d3*d3*d3*d3*d3",
      "-6*d3-3*d1*d2+12*d1*d3*d3+18*d2*d2*d3+3*d1*d1*d2*d3+6*d1*d2*d2*d2-21*d2*d3*d3*d3-6*d1*d1*d3*d3*d3-24*d1*d2*d2*d3*d3-9*d2*d2*d2*d2*d3+3*d3*d3*d3*d3*d3+21*d1*d2*d3*d3*d3*d3+21*d2*d2*d2*d3*d3*d3-3*d1*d3*d3*d3*d3*d3*d3-15*d2*d2*d3*d3*d3*d3*d3+3*d2*d3*d3*d3*d3*d3*d3*d3"
    ],
    [
      "6*d3-3*d1*d3*d3-6*d2*d2*d3+9*d2*d3*d3*d3-3*d3*d3*d3*d3*d3",
      "3*d2-9*d3*d3-3*d1*d2*d3-3*d2*d2*d2+6*d1*d3*d3*d3+12*d2*d2*d3*d3-12*d2*d3*d3*d3*d3+3*d3*d3*d3*d3*d3*d3",
      "-12*d2*d3-3*d1*d2*d2+12*d3*d3*d3+12*d1*d2*d3*d3+9*d2*d2*d2*d3-9*d1*d3*d3*d3*d3-21*d2*d2*d3*d3*d3+15*d2*d3*d3*d3*d3*d3-3*d3*d3*d3*d3*d3*d3*d3",
      "3-6*d1*d3-6*d2*d2+27*d2*d3*d3+3*d1*d1*d3*d3+12*d1*d2*d2*d3+3*d2*d2*d2*d2-15*d3*d3*d3*d3-27*d1*d2*d3*d3*d3-21*d2*d2*d2*d3*d3+12*d1*d3*d3*d3*d3*d3+33*d2*d2*d3*d3*d3*d3-18*d2*d3*d3*d3*d3*d3*d3+3*d3*d3*d3*d3*d3*d3*d3*d3"
    ]
  ],
  "alpha_multiplication_determinant": "81*orbitDeterminant^2",
  "orbit_determinant": "1-3*d1*d3-2*d2*d2+3*d1*d1*d3*d3+d1*d2*d2*d3+d2*d2*d2*d2-d1*d1*d2*d2*d2-d2*d2*d2*d3*d3-d1*d1*d1*d3*d3*d3+d1*d1*d2*d2*d3*d3",
  "symbol_Schur_matrix": [
    [
      "d2-d1*d1",
      "-d1",
      "1"
    ],
    [
      "-2*d1+d2*d3",
      "-1-d1*d3+d2*d2",
      "2*d3-d1*d2"
    ],
    [
      "1",
      "d3",
      "d2-d3*d3"
    ]
  ],
  "symbol_free_coordinates": "y0,T=y1-4*y3,y2; y3 remains free and adds4*y3*(u+z*v/2)^2",
  "orbit_resultant_identity": "orbitDeterminant=Res_z(z^3-omega^2*d2*z+d1,-omega*d2*z^2+omega^2*d2*d3*z+1-d1*d3), omega^2+omega+1=0",
  "simple_qline_remainders": [
    "-1/2*d1+3/2*y0-3/2*d2*h5-3/2*d3*h4-3*y1*h5-3*y2*h4+6*y3*h5-24*d1*y3*h7-48*y0*y3*h7-48*y3*y3*h6+3*d1*d1*d1*h7+18*d1*d1*y0*h7+12*d1*d1*y3*h6+36*d1*y0*y0*h7+48*d1*y0*y3*h6+24*y0*y0*y0*h7+48*y0*y0*y3*h6",
    "2*d2+9/2*y1-12*y3+3/2*h4+3*d1*y0-3*y0*y0-3/2*d1*d2*h5-3/2*d1*d3*h4-3*d1*y1*h5-3*d1*y2*h4+6*d1*y3*h5-48*y3*y3*h7+12*d1*d1*y3*h7+96*d1*y0*y3*h7+48*d1*y3*y3*h6+144*y0*y0*y3*h7+192*y0*y3*y3*h6-6*d1*d1*d1*y0*h7-36*d1*d1*y0*y0*h7-24*d1*d1*y0*y3*h6-72*d1*y0*y0*y0*h7-96*d1*y0*y0*y3*h6-48*y0*y0*y0*y0*h7-96*y0*y0*y0*y3*h6",
    "3*d3+9/2*y2+3/2*h5-3/2*d1*d2+6*d1*y3+3/2*d1*h4+3/2*d2*y0-9*y0*y1+18*y0*y3-3*d1*d1*y0-3*d1*y0*y0-3/2*d2*d2*h5-3/2*d2*d3*h4-3*d2*y1*h5-3*d2*y2*h4+6*d2*y3*h5+6*y0*y0*y0-24*d1*d2*y3*h7+96*d1*y3*y3*h7-48*d2*y0*y3*h7-48*d2*y3*y3*h6+288*y0*y3*y3*h7+192*y3*y3*y3*h6+3*d1*d1*d1*d2*h7-12*d1*d1*d1*y3*h7+18*d1*d1*d2*y0*h7+12*d1*d1*d2*y3*h6-144*d1*d1*y0*y3*h7-48*d1*d1*y3*y3*h6+36*d1*d2*y0*y0*h7+48*d1*d2*y0*y3*h6-432*d1*y0*y0*y3*h7-384*d1*y0*y3*y3*h6+24*d2*y0*y0*y0*h7+48*d2*y0*y0*y3*h6-384*y0*y0*y0*y3*h7-576*y0*y0*y3*y3*h6+6*d1*d1*d1*d1*y0*h7+48*d1*d1*d1*y0*y0*h7+24*d1*d1*d1*y0*y3*h6+144*d1*d1*y0*y0*y0*h7+144*d1*d1*y0*y0*y3*h6+192*d1*y0*y0*y0*y0*h7+288*d1*y0*y0*y0*y3*h6+96*y0*y0*y0*y0*y0*h7+192*y0*y0*y0*y0*y3*h6",
    "-1/2-3/2*d1*d3-3*d1*y2+9/2*d2*y1-12*d2*y3+3/2*d2*h4+3/2*d3*y0+3*y0*y2-3*y0*h5+9*y1*y1-42*y1*y3+48*y3*y3-6*y3*h4+3/2*d1*d1*d2+3*d1*d1*y1-6*d1*d1*y3+3/2*d1*d2*y0+3*d1*y0*y1-6*d1*y0*y3-3/2*d2*d3*h5-3*d2*y0*y0-3/2*d3*d3*h4-3*d3*y1*h5-3*d3*y2*h4+6*d3*y3*h5-6*y0*y0*y1+12*y0*y0*y3-24*d1*d3*y3*h7-48*d1*y2*y3*h7-48*d2*y3*y3*h7-48*d3*y0*y3*h7-48*d3*y3*y3*h6-96*y0*y2*y3*h7-96*y1*y3*y3*h7-96*y2*y3*y3*h6+192*y3*y3*y3*h7+3*d1*d1*d1*d3*h7+6*d1*d1*d1*y2*h7+36*d1*d1*d2*y3*h7+18*d1*d1*d3*y0*h7+12*d1*d1*d3*y3*h6+36*d1*d1*y0*y2*h7+72*d1*d1*y1*y3*h7+24*d1*d1*y2*y3*h6-144*d1*d1*y3*y3*h7+144*d1*d2*y0*y3*h7+96*d1*d2*y3*y3*h6+36*d1*d3*y0*y0*h7+48*d1*d3*y0*y3*h6+72*d1*y0*y0*y2*h7+288*d1*y0*y1*y3*h7+96*d1*y0*y2*y3*h6-576*d1*y0*y3*y3*h7+192*d1*y1*y3*y3*h6-384*d1*y3*y3*y3*h6+144*d2*y0*y0*y3*h7+192*d2*y0*y3*y3*h6+24*d3*y0*y0*y0*h7+48*d3*y0*y0*y3*h6+48*y0*y0*y0*y2*h7+288*y0*y0*y1*y3*h7+96*y0*y0*y2*y3*h6-576*y0*y0*y3*y3*h7+384*y0*y1*y3*y3*h6-768*y0*y3*y3*y3*h6-3*d1*d1*d1*d1*d2*h7-6*d1*d1*d1*d1*y1*h7+12*d1*d1*d1*d1*y3*h7-24*d1*d1*d1*d2*y0*h7-12*d1*d1*d1*d2*y3*h6-48*d1*d1*d1*y0*y1*h7+96*d1*d1*d1*y0*y3*h7-24*d1*d1*d1*y1*y3*h6+48*d1*d1*d1*y3*y3*h6-72*d1*d1*d2*y0*y0*h7-72*d1*d1*d2*y0*y3*h6-144*d1*d1*y0*y0*y1*h7+288*d1*d1*y0*y0*y3*h7-144*d1*d1*y0*y1*y3*h6+288*d1*d1*y0*y3*y3*h6-96*d1*d2*y0*y0*y0*h7-144*d1*d2*y0*y0*y3*h6-192*d1*y0*y0*y0*y1*h7+384*d1*y0*y0*y0*y3*h7-288*d1*y0*y0*y1*y3*h6+576*d1*y0*y0*y3*y3*h6-48*d2*y0*y0*y0*y0*h7-96*d2*y0*y0*y0*y3*h6-96*y0*y0*y0*y0*y1*h7+192*y0*y0*y0*y0*y3*h7-192*y0*y0*y0*y1*y3*h6+384*y0*y0*y0*y3*y3*h6"
  ],
  "all_strata_qline_term_counts": [
    1012,
    1415,
    1573,
    1382
  ],
  "limitations": "Endpoint-zero strata remain outside this finite normalization chart. Norm-alpha necessity is a separate proposed Q-cycle theorem; no global pair is constructed."
}
```
</details>


### Retired source certificate: `research/computations/conditional_2_12_cubic_reduction_2026_10_21_candidates.json`

Historical source retained verbatim, including limitations and external dependencies. Relative file paths in archived code refer to the original repository location.

<details><summary>Original source</summary>

```json
{
  "status": "exact candidate test; no conclusion until verified computation",
  "input_sha256": "66d8c0d841cc12d664b5188f72c943d85411e3c0617aeb4d6f0cef96c9277713",
  "candidate_polynomial": "648h^4+45h^2-4",
  "t": "27h^3/4+15h/32=1/(24h) modulo candidate polynomial",
  "d2": "108h^3-9h/2",
  "first_h_retained": "h4=-2h,h5=h6=0,h7=h",
  "unique_nonzero_full_cubic_equations": [
    "-9/32-15/32*h*eta+27/4*h^2-27/4*h^3*eta",
    "-45/16*eta-7335/64*h+99/2*h^2*eta+17901/8*h^3",
    "1539/32-123/32*h*eta-3753/4*h^2+297/4*h^3*eta",
    "3/4*eta+369/16*h-891/2*h^3",
    "-237/64+21/64*h*eta+567/8*h^2-135/8*h^3*eta",
    "-9/32*eta-891/128*h-9/4*h^2*eta+2025/16*h^3",
    "-105/64-15/64*h*eta+243/8*h^2-27/8*h^3*eta",
    "1/8*eta+27/32*h-81/4*h^3",
    "1/16*eta+27/64*h-81/8*h^3",
    "-105/128-15/128*h*eta+243/16*h^2-27/16*h^3*eta",
    "-9/64*eta-891/256*h-9/8*h^2*eta+2025/32*h^3",
    "-237/128+21/128*h*eta+567/16*h^2-135/16*h^3*eta",
    "3/32*eta+369/128*h-891/16*h^3",
    "1539/256-123/256*h*eta-3753/32*h^2+297/32*h^3*eta",
    "-45/128*eta-7335/512*h+99/16*h^2*eta+17901/64*h^3",
    "-9/256-15/256*h*eta+27/32*h^2-27/32*h^3*eta"
  ],
  "raw_equation_count": 48,
  "unique_nonzero_count": 16,
  "global_coefficients": "Fixed actual k-linear sextic splitting from22 image columns; eta is exactly q^3 coefficient."
}
```
</details>


### Retired source certificate: `research/computations/conditional_2_12_cubic_reduction_2026_10_21_candidates.py`

Historical source retained verbatim, including limitations and external dependencies. Relative file paths in archived code refer to the original repository location.

<details><summary>Original source</summary>

```python
#!/usr/bin/env python3
"""Exact full-C3 test at the four free-orbit q-line candidates.

Uses only the new structured full-C3 exporter, no inherited theorem replay.
All global sextic coefficients are the fixed rational splitting of the actual
23-dimensional k-linear source; eta is its sole q^3 ambiguity.
"""
import ast,json
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
HERE=Path(__file__).resolve().parent
src=HERE/'conditional_2_12_elimination_2026_10_20.py'
t=ast.parse(src.read_text())
stop=next(i for i,n in enumerate(t.body) if isinstance(n,ast.Assign)
          and any(isinstance(x,ast.Name) and x.id=='stem' for x in n.targets))
e={'__file__':str(src),'__name__':'candidate_fullC3'}
exec(compile(ast.Module(body=t.body[:stop],type_ignores=[]),str(src),'exec'),e)

def add(*ps):
    out={}
    for p in ps:
        for m,c in p.items():out[m]=out.get(m,Q(0))+c
    return {m:c for m,c in out.items() if c}
def scale(p,c):return {m:c*x for m,x in p.items() if c*x}
def reduce_h(p):
    p=dict(p)
    for hp in range(max((m[0] for m in p),default=0),3,-1):
        for ep in list({m[1] for m in p if m[0]==hp}):
            c=p.pop((hp,ep),Q(0))
            if c:
                p[(hp-4,ep)]=p.get((hp-4,ep),Q(0))+c/Q(162)
                p[(hp-2,ep)]=p.get((hp-2,ep),Q(0))-c*Q(5,72)
    return {m:c for m,c in p.items() if c}
def mul(p,q):
    out={}
    for (h,a),c in p.items():
        for (j,b),d in q.items():out[(h+j,a+b)]=out.get((h+j,a+b),Q(0))+c*d
    return reduce_h(out)
def const(c):return {(0,0):Q(c)} if c else {}
h={(1,0):Q(1)};eta={(0,1):Q(1)}
tt={(3,0):Q(27,4),(1,0):Q(15,32)}
d2=add(scale(tt,16),scale(h,-12))
rep={1:{},2:d2,3:{},5:{},6:add(scale(h,6),scale(tt,-4)),7:{},8:tt,
     13:scale(h,-2),14:{},15:{},16:h,21:eta}
def substitute(p):
    out={}
    for m,c in p.items():
        term=const(c)
        for i in m:
            assert i in rep, i
            term=mul(term,rep[i])
        out=add(out,term)
    return reduce_h(out)
def fmt(p):
    terms=[]
    for (hp,ep),c in sorted(p.items()):
        mon='*'.join((('h' if hp==1 else f'h^{hp}') if hp else '',
                      ('eta' if ep==1 else f'eta^{ep}') if ep else '')).strip('*')
        coeff='' if abs(c)==1 and mon else str(abs(c))
        terms.append(('-' if c<0 else '+')+coeff+('*' if coeff and mon else '')+mon)
    s=''.join(terms)
    return s[1:] if s.startswith('+') else(s or '0')

full_cubic=[substitute(e['normalized'](p)) for p in e['cubic']]
unique=[]
for p in full_cubic:
    if p and p not in unique:unique.append(p)
stem=Path(__file__).with_suffix('')
lines=[
 '-- Exact four-candidate full global sextic cubic test.',
 'R=QQ[h,eta,MonomialOrder=>GRevLex];',
 'candidatePolynomial=648*h^4+45*h^2-4;',
 'cubicEquations={'+','.join(fmt(p) for p in unique)+'};',
 'candidateCubicIdeal=ideal join({candidatePolynomial},cubicEquations);',
 'print "CANDIDATE_FULL_C3_MODEL_READY";',
 '-- No Groebner basis run by this exporter.',
]
stem.with_suffix('.m2').write_text('\n'.join(lines)+'\n')
meta={'status':'exact candidate test; no conclusion until verified computation',
      'input_sha256':sha256(src.read_bytes()).hexdigest(),
      'candidate_polynomial':'648h^4+45h^2-4',
      't':'27h^3/4+15h/32=1/(24h) modulo candidate polynomial',
      'd2':'108h^3-9h/2',
      'first_h_retained':'h4=-2h,h5=h6=0,h7=h',
      'unique_nonzero_full_cubic_equations':[fmt(p) for p in unique],
      'raw_equation_count':len(full_cubic),'unique_nonzero_count':len(unique),
      'global_coefficients':'Fixed actual k-linear sextic splitting from22 image columns; eta is exactly q^3 coefficient.'}
stem.with_suffix('.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2))
```
</details>
