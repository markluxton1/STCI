# Phase 2 addendum: ruled normalizations and conditional conductor boundaries

## Paired-secant cubic

The finite normalization of the cubic x0*x2^2=x1^2*x3 is F1, with hyperplane class E+2f. On x0=1 its local ring inclusion is k[r,rw,w^2] inside k[r,w]. The upstairs conductor is (r); the downstairs conductor is the reduced double-line ideal (x1,x2). The conductor section maps two-to-one to the line, branched at the endpoints. The strict quartic lift has class 2E+2f, but the full inverse ideal is (w-r^2)(r,w), with an embedded length-one defect at each endpoint. The same F1 is the smooth cubic scroll S(1,2) in P4, projected from the omitted middle coordinate. On the smooth quadric the cubic cuts C0 plus the two limiting tangent trisecants. In characteristic two the conductor cover is inseparable and the scroll is a tangent developable.

Sources: research/notes/2026-10-24-cubic-scroll-normalization.md and research/notes/2026-10-24-p4-ruled-models-independent-audit.md. Independently reviewed provisional geometry, not a new STCI result.

## Projection cone and four-section quartic

The projected cone over C0 has ring k[s^4,s^3t,st^3,t^4], missing the integral element s^2t^2. Its normalization is the complete fourth Veronese cone, with conductor supported at the vertex and an upstairs dual-number quotient. The correct factorization is F4 contracting the negative section to the normal cone, followed by finite normalization of the projected cone. F4 itself is not finite over the projected cone. The related four-section quartic has conductor (x0,x1)^2 downstairs; its transverse ring is k[v^3,v^4,b] inside k[v,b], with conductor v^6. Full inverse ideals can have embedded endpoint corrections of colength six.

Sources: research/notes/2026-10-24-p4-ruled-surfaces-synthesis.md and its independent audit. Elementary transformations and mu4 arithmetic remain in the ruled-geometry family.

## Conditional (6,16) singular-root interface

The October 20 proposal assumes an actual supported (6,16) pair, full generic coprime normal CI (2,12), and an actual saturated movement-two first relation. The (2,2) spectral root Z must satisfy O_Z(1,-1)^12 trivial. A reviewed but unpromoted finite singular-root bridge has transform ideal (p,u^10), providing finite embedded Cartier lifts even for singular Z. Full spectral torsion eliminates cuspidal and tangent-component roots; smooth, nodal, and two-node reducible roots retain their gluing conditions. The next global step is cubic-jet matching for a genuine sextic, [F3-alpha*G0] mod (f)=0, without dividing by alpha at its zeros. Abstract Cartier lifts do not yield global equations or a support certificate.

The October 21 conductor-budget proposal originally depended on an anticanonical contraction hypothesis. The independent continuation audit subsequently VERIFIED that hypothesis in the precise actual-pair setting: a cubic-image model V is a smooth integral threefold with canonical bundle O(-2), and the strict sextic descends to an integral anticanonical surface T. Finite duality and the local monic double-cover normalization then exclude singular-curve contacts at ramified simple base zeros. Combined with the separate nodal analysis, the reviewed result gives a sharp NECESSARY alternative for any actual pair: the multiplier alpha has a multiple base zero, or alpha vanishes at a node of the full root. For a smooth full root the necessary discriminant equation is Disc_8(Ncomp(tau))=0, of degree 28 in the root coefficients. These exceptional strata have not been eliminated; no complete exclusion follows. A different proposed nodal normalization obtained by dividing by a nonunit was rejected as nonfinite. Its suggested integral replacement is not yet certified normal or equipped with an exact conductor.

Sources: research/notes/2026-10-20-conditional-2-12-singular-gluing.md and research/notes/2026-10-21-conditional-2-12-conductor-ramification.md. Conditional cross-family work, not promoted.

## Seven-cubic contraction and five-quadric anticanonical model

The conditional \((2,12;6,16;2)\) actual-pair geometry has a **separate** exact projective construction, not implied by the sextic symbol matrix. Write \(q=x_0x_3-x_1x_2\), \(A=x_0^2x_2-x_1^3\), \(B_0=x_0x_2^2-x_1^2x_3\), \(D_0=x_2^3-x_1x_3^2\). The seven cubics
\[
qx_0,\ qx_1,\ qx_2,\ qx_3,\ A,\ B_0,\ D_0
\]
generate \(I_{C_0}(3)\) and define \(\phi:\operatorname{Bl}_{C_0}\mathbf P^3\to V\subset\mathbf P^6\). In corresponding coordinates \(y_0,\ldots,y_6\), the image \(V\) is cut out **scheme-theoretically** by the five quadrics
\[
\begin{aligned}
&y_0y_5-y_2y_4+y_1^2,\quad y_0y_6-y_2y_5+y_1y_3,\\
&y_1y_5-y_3y_4+y_0y_2,\quad y_1y_6-y_3y_5+y_2^2,\quad
y_4y_6-y_5^2+y_1y_2.
\end{aligned}
\]
The homogeneous ring has free resolution of ranks \((1,5,5,1)\), shifts \((0,2,3,5)\); \(V\) is a smooth integral degree-five threefold with \(\omega_V=\mathcal O_V(-2)\). Projection to \([y_0:y_1:y_2:y_3]\) has base ideal defining the smooth conic \(\Gamma=\{y_0=\cdots=y_3=0,\ y_4y_6-y_5^2=0\}\). Its graph identifies \(\operatorname{Bl}_{C_0}\mathbf P^3=\operatorname{Bl}_\Gamma V\), contracting the strict transform of the unique quadric.

Every sextic in \(H^0(I_{C_0}^2(6))\) is a quadratic expression in these seven cubics and descends to \(T\in|\mathcal O_V(2)|\), with \(\omega_T=\mathcal O_T\). **For an actual supported pair** the low-degree carrier exclusion forces the sextic, its strict transform, and \(T\) to be integral, and the quadric cannot be a component. Finite duality for the normalization \(Y\to T\) identifies \(\omega_Y\) with its full conductor ideal, and the resulting conductor curve \(\Delta\) satisfies \(\omega_\Delta=\mathcal O_\Delta\), even if the conductor is nonreduced or \(Y\) is not Gorenstein. A generically reduced irreducible conductor component of multiplicity one must have arithmetic genus at most one. This global restriction drives the reviewed exclusion of ramified contacts over **simple** zeros of the multiplier \(\alpha\). It does not exclude repeated zeros or nodal root contacts where \(\alpha\) vanishes.

The exact cubic model, graph identification, conductor duality, and simple-zero exclusion received an independent **PASS under the conditional actual-pair hypotheses**. A different nodal example's purported finite normalization by dividing by a nonunit was explicitly **rejected** and is not used. No unconditional \((6,16)\) or STCI exclusion follows. [Cubic image and conductor construction](../notes/2026-10-21-conditional-2-12-cubic-image-and-conductor-interface.md); [independent review and rejected nodal claim](../notes/2026-10-21-conditional-2-12-surface-audit-cont2.md).

## Exact global sextic-symbol restriction in the conditional (6,16) lane

For an actual supported \((F_6,G_{16})\) pair with **full fiberwise coprime** generic normal CI \((2,12)\) and an **actual saturated movement-two** first relation, write the basepoint-free quadratic first root \(f=a(z)u^2+b(z)uv+c(z)v^2\) and the degree-six symbol \(\sigma_2(F_6)=\alpha f\), where \(\alpha\in H^0(\mathbf P^1,\mathcal O(8))\) is nonzero. A global sextic does **not** have an arbitrary symbol in \(H^0(\mathcal O(10))^3\). The exact map
\[
H^0(I_{C_0}^2(6))\longrightarrow H^0(\operatorname{Sym}^2N_{C_0/\mathbf P^3}^{\vee}(6))
\]
has source dimension 23, rank 22, kernel \(kq^3\) (with \(q=x_0x_3-x_1x_2\)), and image cut out by **eleven independent linear equations** in the 33 symbol coefficients \(P_j,Q_j,R_j\). A source basis consists of \(q^2\) times the ten quadrics; \(qA\) times \(x_0,x_1,x_2,x_3\); \(qB\) and \(qD\) times \(x_2,x_3\); and \(A^2,AB,AD,BD,D^2\), with \(A=x_0^2x_2-x_1^3\), \(B=x_0x_2^2-x_1^2x_3\), \(D=x_2^3-x_1x_3^2\). The eleven equations are, in order,
\[
\begin{gathered}
P_9-2Q_{10},\quad Q_0-2R_1,\quad P_0-2Q_1+4R_2,\quad
3P_1-2Q_2-4R_3,\\
P_2-2Q_3+4R_4,\quad P_3-2Q_4+4R_5,\quad P_4-4R_6,\quad
P_5-2Q_6+4R_7,\\
P_6-2Q_7+4R_8,\quad P_7+2Q_8-12R_9,\quad P_8-2Q_9+4R_{10}.
\end{gathered}
\]
Substituting \(P=\alpha a,Q=\alpha b,R=\alpha c\) gives **eleven bilinear global-symbol equations**. They do not invert \(\alpha\) at its zeros. For fixed compatible \((f,\alpha)\), global sextics with this symbol differ by \(\eta q^3\).

The next necessary global lifting equation compares the **actual cubic jet** of such a sextic with the unique first-compatible local cubic correction \(G_0\):
\[
(F_c)_3-\alpha G_0=f(\ell(z)u+m(z)v),\qquad \deg\ell,\deg m\le7.
\]
This is a finite 40-coefficient condition, distinct from the first and second local ambient classes and from the full spectral torsion criterion. The smooth torsion-two seed \(f_0=(z^2+4)u^2+(z^2-8)v^2\) admits a unique projective multiplier \(\alpha_0=z^8-8z^6+96z^4+256z^2+1024\) satisfying the eleven equations, but it **fails** the cubic comparison (an exact annihilating pairing is \(-384\)) and already fails the independently accepted second obstruction. This is a seed exclusion, not emptiness of the combined incidence.

The reviewed singular-root bridge uses the actual transformed ideal \((p,t^{10})\) and proves necessity of the ambient classes even for singular reduced roots, under the stated actual-pair hypotheses. The remaining structured scheme also retains all twenty-five second-obstruction pairings and full-scheme spectral torsion (including nodal gluing); its emptiness, nonemptiness, and realization by a globally supported pair are **unresolved**. The independent audit passed the exact symbol map and conditional necessity reductions, without promoting a general STCI exclusion. [Symbol map and cubic comparison](../notes/2026-10-20-conditional-2-12-symbol-map.md); [global incidence](../notes/2026-10-20-conditional-2-12-global-realization-incidence.md); [independent audit](../notes/2026-10-20-conditional-2-12-incidence-audit.md).

## The finite source incidence and its constant-rank cubic obstruction

Let \(S=H^0(I_C^2(6))\), and let \(\rho_2:S\to H^0(\operatorname{Sym}^2N_C^\vee(6))\) be the computed rank-22 map. Write the proposed leading symbol as \(\alpha f\), with \(f=a(z)u^2+b(z)uv+c(z)v^2\). The eleven explicit linear image equations for \(\alpha f\) define the first necessary coefficient incidence, subject to the actual saturated movement-two and nonzero-section conditions. In particular, no division by \(\alpha\) is permitted at its zeros.

For a chosen compatible sextic, the next condition is
\[
(F_c)_3-\alpha G_0=f(\ell u+m v),\qquad\deg\ell,\deg m\le7.
\]
The sixteen correction coefficients map into forty cubic coefficients by multiplication by nonzero \(f\). This map is injective in the polynomial ring and therefore has constant rank sixteen; its image is locally a subbundle and the obstruction is a section of the twenty-four-dimensional quotient. **No rank-drop stratification of this multiplication map is required.** Singular roots and multiplier zeros remain exceptional for the other conditions.

The full necessary incidence also imposes the twenty-five second-obstruction pairings and full-root spectral torsion, including nodal gluing. Its projection to root/multiplier parameters can be constructible rather than closed. The known smooth seed fails the cubic quotient obstruction, but no emptiness or nonemptiness result for the full incidence follows. Even a point satisfying all these conditions does not yet provide a proper degree-sixteen mate or prove sole reduced support.

## Coefficient-level cubic obstruction without elimination

Let \(W_7=k[z]_{\le7}\), and let \(T_9\) denote binary cubics in \(u,v\) whose four coefficients are polynomials in \(z\) of degree at most nine. For \(f=a u^2+buv+cv^2\), with \(a,b,c\in k[z]_{\le2}\), define
\[
\mu_f:W_7^2\longrightarrow T_9,\qquad
(\ell,m)\longmapsto f(\ell u+mv).
\]
Writing a target cubic as \(h=h_0u^3+h_1u^2v+h_2uv^2+h_3v^3\), the exact coefficient equations are
\[
h_0=a\ell,\qquad h_1=b\ell+am,\qquad
h_2=c\ell+bm,\qquad h_3=cm.
\]
These are polynomial equations, including at roots of \(a\), \(c\), or the discriminant \(b^2-4ac\). No coefficient division or choice of a nonvanishing root coefficient is required.

For \(f\ne0\), the map \(\mu_f\) is injective: if \(f(\ell u+mv)=0\) in the integral domain \(k[z,u,v]\), then \(\ell=m=0\). Thus every compatible cubic has a **unique** correction pair, and the cokernel dimension is \(4(10)-2(8)=24\). This is a statement about the fixed-\(f\) linear map, not about twenty-four independent equations on the nonlinear parameter scheme \((f,\alpha,F_c)\). On the nonzero-root open, the matrices \(\mu_f\) form a constant-rank family, so the obstruction is a well-defined cokernel section; its zero scheme may have excess dimension or singular components.

The displayed four polynomial identities are an alternative exact computational representation of the quotient obstruction. They allow direct coefficient comparison without computing 24 moving quotient coordinates. The eleven first-symbol equations, the second-obstruction pairings, and the full-root spectral conditions remain additional constraints. In particular, the constant rank of \(\mu_f\) neither excludes singular quadratic roots nor proves the existence of a proper degree-sixteen mate.

## Varying the sextic lift: the missing \(q^3\) direction

The preceding rank-sixteen calculation fixes a chosen sextic \(F_c\) with the prescribed quadratic normal symbol. But the kernel of the quadratic-symbol map is \(kq^3\), so every sextic with that symbol is \(F_c+\eta q^3\). Since \(q\) vanishes to normal order one, \(q^3\) contributes a generally nonzero cubic jet. Write \(\tau=(q^3)_3\) in the same local cubic-coefficient model. **Existence of some compatible sextic lift** therefore requires
\[
(F_c)_3-\alpha G_0+\eta\tau=f(\ell u+mv)
\]
for a scalar \(\eta\) and \(\deg\ell,\deg m\le7\). The fixed-lift quotient class \(b=[(F_c)_3-\alpha G_0]\) must lie in the line spanned by \([\tau]\) in \(\operatorname{coker}\mu_f\), rather than necessarily vanish there.

Equivalently, the correct varying-lift map is
\[
\widetilde\mu_f:W_7^2\oplus k\longrightarrow T_9,\qquad
(\ell,m,\eta)\longmapsto f(\ell u+mv)-\eta\tau.
\]
It has rank sixteen if \(\tau\in\operatorname{im}\mu_f\), and rank seventeen otherwise. Thus the **varying-lift** obstruction has codimension twenty-four or twenty-three, respectively. The earlier constant-rank assertion applies only to the correction submap \(\mu_f\), not to \(\widetilde\mu_f\). On the generic fiber over \(k(z)\), if \(q_1\) is the nonzero linear normal symbol of \(q\), then \(\tau=q_1^3\); for a quadratic \(f\), the necessary generic condition for \(\tau\in f\cdot k(z)[u,v]_1\) is that \(f\) be proportional to \(q_1^2\). This generic divisibility alone is not sufficient for membership in the bounded polynomial correction space \(W_7^2\).

The coefficient equations become \(h_i+\eta\tau_i=(a\ell,\ b\ell+am,\ c\ell+bm)_i\), with the fourth coefficient \(cm\). They remain division-free. Any claim that a seed fails the cubic comparison must specify whether the test allowed the \(q^3\) direction; a fixed-lift failure alone does not exclude all sextics with the same quadratic symbol. The independently computed second obstruction is unaffected by this logical distinction, subject to its original hypotheses.

## Exact failed seed and the remaining incidence

The smooth torsion-two root \(f_0=(z^2+4)u^2+(z^2-8)v^2\) has a unique projective multiplier \(\alpha_0=z^8-8z^6+96z^4+256z^2+1024\) satisfying all eleven quadratic-symbol image equations. This is a positive first-stage realization result for that seed, not a full ambient lift. The next cubic comparison fails: the recorded exact annihilating pairing is \(-384\), so the specified seed does **not** extend to the required compatible sextic jet. It independently fails the accepted second obstruction.

The calculation gives a concrete counterexample to the implication “first-symbol image membership plus smooth torsion-two root implies next-jet realizability.” It does not show the entire incidence empty. The remaining problem must keep the full scheme of singular roots, all twenty-five second-obstruction pairings, and the cubic-jet equations simultaneously. Any argument that divides by \(\alpha\) must first isolate its zero locus, where the compatibility problem changes. The explicit seed and its scope are in [the symbol-map source](../notes/2026-10-20-conditional-2-12-symbol-map.md).

## What the conditional (6,16) computation actually tests

This lane is a controlled illustration of the distinction between a root scheme, an ambient symbol, and an actual supported pair. Its quadratic normal root and movement-two relation impose a spectral condition on the full root, but the degree-six symbol must also lie in the **rank-22 image** of the global map from the 23-dimensional space of sextics vanishing twice along C. Its one-dimensional kernel is generated by \(q^3\); the eleven independent linear constraints on the 33 symbol coefficients are therefore genuine global-source conditions, not optional genericity assumptions.

The cubic-image and conductor calculation adds a further restriction **conditional on an actual supported pair**: the multiplier has a multiple base zero or vanishes at a node of the full root. The smooth-root discriminant condition and the remaining exceptional strata are necessary tests, not a proof that a proper pair exists or that every (6,16) pair is excluded. In particular, the rejected nonfinite nodal normalization cannot be used to close the nodal stratum.

These conditions sit at different logical levels: (i) root and formal normal algebra; (ii) actual global sextic source; (iii) conductor geometry for a supported pair; and (iv) the still-unresolved exceptional locus. Their conjunction is a candidate-family test, not a universal implication between the global determinant, residual-jet and conductor-descent routes. See [Chapter 3](03-infinitesimal-geometry.md#311-embedded-one-step-lifting-and-the-actual-homogeneous-source) and [dependencies](DEPENDENCIES.md).

## Why the conditional sextic conductor does not solve descent

The seven-cubic contraction supplies an exact anticanonical surface model **assuming an actual supported pair**. Its duality calculation constrains the conductor of that model, and the simple-zero argument eliminates a specified ramification stratum. This is logically different from the full-conductor descent test for an independently chosen normalization and a proposed mate: in the sextic argument the pair is an antecedent, whereas in the projection program its existence is the conclusion sought.

The eleven linear equations defining the global sextic-symbol image likewise impose necessary realization conditions without selecting a proper degree-sixteen mate. The remaining multiple-base-zero and nodal-contact loci therefore require direct treatment; neither the cubic-image duality nor the symbol rank closes them. For the general descent framework and the role of nilpotent conductor phases, see [Chapter 4](04-carriers.md#42-the-full-conductor-descent-criterion) and [the projection phase synthesis](normalization_conductor_projection.md#23a-full-conductor-phases-an-exact-local-to-family-distinction).

## Remaining boundaries

No arbitrary projection classification, full conductor phase image, higher-index exclusion, global spectral realization, or unrestricted characteristic-zero STCI theorem follows. The separate codex/intersections-containing-quartic-2026-10-27 branch remains excluded. Original mathematical sources are retained.


Source for this correction and stronger reviewed result: research/notes/2026-10-21-conditional-2-12-surface-audit-cont2.md, sections 2-6. Its independent review reports PASS for the cubic-model interface, full conductor duality, and ramified simple-base-zero exclusion, while expressly rejecting the defective nodal normalization. The finite singular-root bridge remains reviewed but unpromoted.


### Geometric scope of movement two

The canonical reduction STCI-R-0014 identifies movement epsilon with the degree of the coefficient map from C to the projective space of binary degree-r forms. Its first normal-root divisor has bidegree (epsilon,r) on P1_base x P1_direction. In the conditional (6,16) setting, r=2 and epsilon=2, so the full first root is a divisor of bidegree (2,2). Saturation means the coefficient map has no base points; it does not exclude root collisions or ensure coprimality of specialized initial forms. Generic binary-CI coprimality and saturation are separate assumptions. The six numerical rows, including (r,s;a,b)=(2,12;6,16), are necessary candidates only under the complete hypotheses of STCI-R-0013 and STCI-R-0014; they are not a classification of arbitrary STCI presentations.

Canonical source: research/results/movement_two_six_rows.md (STCI-R-0014), geometric clarification in commit ccc9c3965e1645ed2569405e0194e31edb38e9d0. This cross-reference does not promote the conditional singular-root arguments.
