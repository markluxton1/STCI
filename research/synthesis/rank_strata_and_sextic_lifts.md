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
with sheaf powers/saturated homogeneous powers as in [actual equation spaces](../supplements/ACTUAL_EQUATION_SPACES.md). This is a fixed vector space and hence a trivial bundle on every root-parameter scheme. A specified finite-jet target, correction map and their gluing data must be matched by the evaluation of this same homogeneous section. The incidence (1) is independent of basis changes in these spaces. Changes of an affine jet representative by an allowed correction induce isomorphic incidences.

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
