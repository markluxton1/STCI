# Marked Chow configurations and their universal log boundary

**Status.** Provisional geometric synthesis for characteristic zero over an algebraically closed field. The open constructions and numerical arguments below have direct derivations; independent review and extension over collisions are outstanding. The objective is to discover a boundary from the quotient maps and the geometry of endpoint attachment, not to assume a compactification or reduce the research program to the first moment.

## 1. Quotient tower and the two families

Use coordinates \([z:x:y:w]\) and the one-dimensional torus \(H\) of weights \((0,1,3,4)\). Put \(S=(\mathbf P^3//_{\rm Ch}H)^\nu\), with dense quotient torus \(T\). The [explicit fan and graph](chow_quotient_fan_and_blowup_comparison.md) are authoritative for the single-curve quotient. In coordinates
\[
r=x/z,\quad u=yz^2/x^3,\quad v=wz^3/x^4,\quad q=u/v,\quad \eta=u^2/v
\]
the evaluation is
\[
(r,q,\eta)\mapsto[1:r:(\eta/q)r^3:(\eta/q^2)r^4].
\]
Every primitive character of the projective three-torus defines a rank-two kernel and a normalized one-dimensional toric Chow quotient \(\mathbf P^1\). The six coordinate ratios are \(r,\eta r^3/q,\eta r^4/q^2,\eta r^2/q,\eta r^3/q^2,r/q\), in the order \(x/z,y/z,w/z,y/x,w/x,w/y\). The last two transverse characters \(q,\eta\) (in addition to these six ratios) kill \(H\); their quotient maps factor rationally through \(S\). The previous products of projective lines are products of such quotient maps; simultaneous regularity requires common graph refinements, not a canonical morphism from each original quotient.

Let \(X\) be the normalized graph with maps \(\mathbf P^3\leftarrow X\to S\). Over \(T\), \(X_T=T\times\mathbf P^1\), with each fiber lifting one orbit closure. The two global endpoint sections are contracted to \(p_0,p_\infty\). In characteristic zero Chen–Satriano identify the normalized orbit Chow quotient with the coarse space of the relevant stable log-map moduli (Theorem 1.1). Its domains are chains of rational curves (Proposition 3.8), and boundary components can map by multiple covers. The universal nodal domain lives over the stack. On each two-pointed chain the dualizing sheaf twisted by the two marks is trivial, since on a component it is the canonical sheaf twisted by its two special points. Residue at the first mark identifies the one-dimensional space of sections with the field, and the relative statement follows by base change. The section normalized to residue \(+1\) there has residue \(-1\) at the other end and opposite residues at each node.

For ordered configurations with \(m\ge1\), take the normalized Chow quotients
\[
B_m=((\mathbf P^3)^m//_{\rm Ch}H^m)^\nu=S^m,\qquad
L_m=((\mathbf P^3)^m//_{\rm Ch}H_{\rm diag})^\nu.
\]
For the independent action, the weight projection of the Segre polytope is the product of the single-factor weight projections. The fibers are Cartesian products, so the fiber fan is the product of the single-factor fans.

The two quotient tori have dimensions \(3m-1\) and \(2m\), respectively for \(L_m\) and \(B_m\). The projection forgets the relative longitudinal coordinates \(r_i/r_1\), \(i>1\). On the normalized graph of the resulting rational map \(L_m\dashrightarrow B_m\), the restriction over \(T^m\) has fan obtained by intersecting the diagonal quotient fan with the kernel of the transverse projection. On this kernel the heights in factor \(i\) are affine in the longitudinal weight, with slope \(a_i\). At each total weight, the lower hull fills the factors' intervals \([0,4]\) in increasing order of \(a_i\). Indeed, transferring weight from a larger slope to an unsaturated smaller slope decreases the height. Ties merge adjacent intervals, so the resulting fan is the braid fan on the slopes modulo simultaneous translation. The relative coordinates split the lattice, giving \(T^m\times\overline L_m^{\rm LM}\) over the dense torus. Here \(\overline L_m^{\rm LM}=(\mathbf P^1)^m//_{\rm Ch}\mathbf G_m\) is the Losev–Manin space and its ordered partitions record relative longitudinal rates. This calculation is over the interior. To compare longitudinal and transverse scales, a path with orders \((a,b,c)\) in \((r,u,v)\) is evaluated by the minimum of \((0,a,3a+b,4a+c)\).

For the other family, use the forgetful map \(S^{m+1}\to S^m\) and marked sections \(\gamma_i(\sigma)=(\sigma,s_i)\). Over the distinct interior configuration locus the ambient threefold family is \(B_m^\circ\times X\); its marked subfamily is the union \(\pi(P)=s_i\) inside it. Its fiber is precisely the \(m\) disjoint embedded curves in \(X\), not a single curve. Evaluation identifies their endpoint sections. The full arrangement Chow form is the product of the individual Chow forms; passing to unordered configurations is optional and loses only the labels. The normalization of the cycle closure is \(\operatorname{Sym}^m S\): multiplication is proper, generically one-to-one on unordered distinct interior orbits and has finite fibers (only finitely many effective degree-four subcycles of any fixed cycle); normality follows from the finite quotient of the normal product. This does not give a canonical length-\(m\) scheme at a collision. The spectral polynomial \(\prod(T-q_i S)\) is one projection of the full Chow form.

## 2. Which boundary is supplied by the quotient maps?

The HKT guiding analogy is a marked pair whose distinguished curves are part of the geometry, and whose moduli boundary detects changes in their incidence. We distinguish boundaries in a fiber from discriminants in the base. Do not choose the blowup order before specifying these objects.

The two carrier pencils \(q,\eta\) and the two leading endpoint contact pencils
\[
u=\eta/q,\qquad \alpha=1/(q\eta)
\]
give four primitive character directions (the \(B_2\) root directions up to sign). They have a common smooth toric compactification
\(S_8=\operatorname{Bl}_{4\ {\rm corners}}(\mathbf P^1_q\times\mathbf P^1_\eta)\), with the eight coordinate and diagonal cocharacter rays. Each of the four displayed characters extends to a morphism to \(\mathbf P^1\) because its kernel rays are in this fan. The original Chow surface has four rays in \((\operatorname{ord}q,\operatorname{ord}\eta)\) coordinates, namely \((1,2),(-1,1),(-1,-1),(1,-2)\). Retaining evaluation to \(\mathbf P^3\) calls for a common refinement. Resolving just \(q,\eta\) on \(S\) adds the four axis rays. Further subdivisions may be needed for smoothness.

For each marking include the fibers \(Q_i,R_i,U_i,A_i\) of \(q,\eta,u,\alpha\) respectively. Blow up the marked sections in the surface family:
\[
Y_\sigma=\operatorname{Bl}_{s_1,\dots,s_m}S_8,\qquad
B_\sigma=\widetilde D_{\rm tor}+\sum_i(E_i+\widetilde Q_i+\widetilde R_i+\widetilde U_i+\widetilde A_i).
\]
On the generic open these four branches meet transversely at each marking, with no other triple concurrence, and the blown-up boundary is SNC. Pulling back the longitudinal graph family (using a common refinement as needed) is, around the interior marked fibers, the blowup along the disjoint orbit curves. The exceptional surfaces are \(E_i\times C_i\simeq\mathbf P^1\times\mathbf P^1\), meeting the two endpoint sections transversely. This is the quotient-side exceptional product, not an identification with the original \(\operatorname{Bl}_C\mathbf P^3\); compare the existing elementary-transform/normal-frame geometry. In particular the markings are no longer disembodied curves: they give boundary surfaces spanning the longitudinal direction in a varying ambient threefold.

## 3. Generic stable surface pair (direct calculation, pending review)

Assume pairwise distinct values within each of the four pencils, no accidental concurrence of three pencil fibers outside the marked points, and characteristic zero. The four smooth pencil directions at a marked point are distinct. Their intersections with toric boundary lie away from toric fixed points. The two diagonal pencils meet twice in the torus, including the unmarked sign partner when the labels agree. These conditions define a nonempty generic open (the only identically forced triple concurrences are at the common marking).

Write \(F_\chi\) for a generic fiber class on \(S_8\), \(D=\sum_{\chi=q,\eta,u,\alpha}F_\chi\). The toric anticanonical boundary cancels \(K_{S_8}\). Blowing up a point of \(k\) smooth branches and including the exceptional divisor changes the log canonical pullback by \((2-k)E\). Here \(k=4\), so
\[
K_Y+B=m\pi^*D-2\sum E_i.
\]
The intersection matrix of the four pencil classes has diagonal zero, off-diagonal entries one except \(F_uF_\alpha=2\), as given by character determinants. Thus \(D^2=14\), and the log square is \(14m^2-4m>0\).

Every exceptional curve has degree 2. Every marked pencil fiber has degree \(3m-2\) or \(4m-2\). Each toric boundary ray spans the kernel of exactly one of the four characters. That character is primitive on the orbit lattice of the corresponding boundary curve and has degree one there. The other three characters are constant on the curve, so the log class has degree \(m\). For any other irreducible curve \(\Gamma\) on \(S_8\) meeting the torus, the sums of intersections with the distinct marked \(q\)-fibers and \(\eta\)-fibers each bound \(\sum_i\operatorname{mult}_{s_i}\Gamma\). At least one of the other two pencil degrees is positive, since \((u,\alpha)\) has character determinant of absolute value two and is finite on the torus. Hence \(mD\cdot\Gamma-2\sum_i\operatorname{mult}_{s_i}\Gamma>0\). Nakai–Moishezon gives ampleness. Together with the SNC boundary this gives a stable surface pair on the generic open. Using just the two carrier pencils gives degree zero on each marked exceptional curve. Extra toric subdivisions away from the markings are log-crepant for the full toric boundary and the marked pencil divisors because the blowup centers are toric fixed points avoided by the marked pencil fibers. They may be contracted in the log model. Simultaneous torus translation preserves the isomorphism class of the labeled surface pair while changing the embedded configuration coordinates. The stable extension of the family remains open.

## 4. Base discriminants: incidence, contact and collisions

First include the inherited toric boundary and the equal-value loci for each character, \(\chi_i=\chi_j\). The latter are not necessarily collisions: \(q_i=q_j\) means common quadric, while \(u_i=u_j\) detects order-four rather than order-three pairwise attachment at \(p_0\); \(\alpha_i=\alpha_j\) does so at \(p_\infty\). An actual collision requires both \(q,\eta\) equal. Record new triple concurrences in the torus:
\[
\eta_j=q_i u_k,\quad q_i\eta_j\alpha_k=1,\quad
q_i^2u_j\alpha_k=1,\quad\eta_i^2\alpha_k=u_j
\]
for the triples \(QRU,QRA,QUA,RUA\), respectively. Include incidences of any additional distinguished curves with the inherited boundary. In characteristic zero \(U_i\cap A_i\) consists of \(s_i\) and its sign partner \((-q_i,-\eta_i)\). Quadruple concurrence and connected components of intersections must be kept in the incidence poset.

This is an arrangement of translated subtori on the configuration torus for the four pencils alone. It is not the full attachment discriminant. The [two endpoint interpolation systems](marked_chow_endpoint_incidence.md) give additional determinantal rank strata and distinguished incidence curves, even when no two character values agree. They explain why the boundary should be enlarged beyond toric arrangements. A rank stratum is not automatically smooth or cleanly intersecting; no wonderful model for their union has yet been constructed.

Fulton–MacPherson compactifies ordered distinct points on a smooth surface by resolving the diagonals, deepest first (a \(k\)-fold diagonal has codimension \(2k-2\)). Its expanded family separates marked sections on bubble components. Pull back the longitudinal family there if desired. This is distinct from blowing up the marked points *inside* each surface fiber. A Hilbert scheme of points (Fogarty for a smooth surface) records infinitesimal schemes, and FM records relative positions and scales; neither can be substituted for the other or assumed to determine the flat embedded CI limit. A global compactification respecting all maps, all rank strata and both families is still to be chosen. Li's wonderful construction needs a building set of smooth subvarieties with the requisite clean intersections. Do not blindly blow up every rank locus.

## 5. Differential forms and exact remaining gap

Over distinct interior markings let \(Z_{\rm red}\) be their glued reduced image, with normalization the disjoint union of the \(C_i\). Horizontal gluing contracts all first ends together and all last ends together; vertical gluing in a stable log map joins components of one degenerate orbit. The two operations differ. For the branchwise logarithmic form \(q_i\,dr/r\), Rosenlicht's residue criterion at the horizontal endpoints is \(\sum q_i=0\) (opposite signs at the two ends); higher-order attachments add no new residue condition for a form with only simple poles. In a nonreduced actual CI use trace and finite duality, not normalization of a nonreduced scheme; the generic lengths weight the residues by \(n_i\). The [centered differential and first-jet comparison](transverse_chow_quadric_graph_gluing.md#centered-differential-and-scalar-part-of-the-spectrum) already separates the scalar obstruction. Ordinary global residue cancellation is automatic between the two endpoints; it is not separate vanishing. Even an actual balanced CI supports other log forms with nonzero horizontal residue, for example \(q^4\,dr/r\) on the four fourth-root-of-unity branches. Log geometry by itself does not force the uncentered \(q\)-form to descend.

One possible stable-map analogue of horizontal gluing inserts contracted rational components at the two endpoint vertices with the \(m\) branches attached; the resulting banana graph has genus \(m-1\), not the actual arithmetic genus of a thick CI. Marking or stabilizing the bubbles is needed for small \(m\); no canonical positions or cross ratios are supplied by the graph alone. This is an analogy, not an additional assertion of a family or a proof of moment balance.

Logarithmic forms on the marked surface such as \(d_{\rm rel}\log(\ell_{ij}/\ell_{ik})\) for joining lines in an endpoint plane have residue divisors determined by incidence, and can be followed through the family. The open question is whether the correct boundary supplies a functorial mechanism tying the actual defining equations or their adjunction data to the distinguished longitudinal form. Do not assume that a well-chosen boundary makes this automatic. The small diagonal and the arbitrary nonreduced CI realization remain open; reduced moment coverage is already established by invariant lifting. The present objective is broader: understand the marked-pair geometry and its change-of-incidence strata before choosing further modifications.

## External inputs and scope

- Kapranov–Sturmfels–Zelevinsky, *Quotients of toric varieties*, Math. Ann. 290 (1991), 643–655, and Billera–Sturmfels fiber polytopes: normalized quotient fan, as in the existing fan proof.
- Chen–Satriano, [*Chow Quotients of Toric Varieties as Moduli of Stable Log Maps*](https://arxiv.org/abs/1201.3406): rank-one subtorus of a projective normal toric variety in characteristic zero; coarse-space identification, not a universal nodal scheme on the coarse space.
- Hacking–Keel–Tevelev, [*Stable pair, tropical, and log canonical compactifications of moduli spaces of del Pezzo surfaces*](https://arxiv.org/abs/math/0702505), Invent. Math. 178 (2009), 173–227: marked distinguished curves and stable-pair compactification; not an application theorem for our family. Their [hyperplane-arrangement compactification](https://arxiv.org/abs/math/0501227) is also relevant.
- Losev–Manin, [*New moduli spaces of pointed curves and pencils of flat connections*](https://arxiv.org/abs/math/0001003), construct the moduli of pointed chains. Di Rocco–Schaffler, [*Families of pointed toric varieties and degenerations*](https://arxiv.org/abs/2110.04842), §4, identify the diagonal Chow quotient of a product of projective lines with the permutohedral toric variety.
- Fulton–MacPherson, [*A Compactification of Configuration Spaces*](https://annals.math.princeton.edu/1994/139-1/p06); Li, [*Wonderful compactification of an arrangement of subvarieties*](https://arxiv.org/abs/math/0611412); De Concini–Procesi toric arrangements. Fogarty, *Algebraic families on an algebraic surface*, Amer. J. Math. 90 (1968), 511–521.
- Rosenlicht regular differentials and finite duality: the existing [spectral boundary modulus](spectral_boundary_modulus.md) and centered-form comparison give the relevant scope.

No literature theorem has been identified that selects our entire discriminant, gives its stable extension or implies arbitrary-CI first-moment vanishing. The proposed construction is not yet a new exclusion theorem.
