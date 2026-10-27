# Moving a thickening together with actual equations

Date: 2026-10-27. **Status: provisional all-degree interface and exact control, independently reviewed in the linked audit; no canonical promotion.** The guiding question is how residual mass can move onto the fixed quartic C, with no assumption that a supported endpoint is impossible. The main point is to distinguish deformation of a lower thickening from deformation of an actual homogeneous pair containing it.

## 1. Scope, retrieval, and what is not being repeated

Let X=P3_k, let C=C0=[s^4:s^3t:st^3:t^4] be the fixed smooth quartic, and let I=I_C. Sections 2–4 work in arbitrary characteristic and for any smooth projective marked curve in a smooth projective threefold, using its chosen polarization. Section 5 is the explicitly characteristic-zero control for the fixed C0. Let T be an embedded pure Cohen–Macaulay thickening with reduced support C and ideal J. Its generic length is m. No curvilinearity, normal-flatness, saturated first relation, or globally split equation module is assumed.

Repository retrieval followed [INDEX](../INDEX.md) then [MAP](../MAP.md), the [containing-intersections vision](2026-10-27-containing-intersections-research-vision.md), [R-0016](../results/nonsaturated_first_relation_resultant.md), [R-0030](../results/local_filtration_comparison_defect.md), [R-0033](../results/constant_first_relation_lifting.md), the [intrinsic cubic-contact construction](2026-10-23-intrinsic-cubic-contact-construction.md), and the [one-step boundary obstruction](2026-10-27-one-step-boundary-obstruction.md).

Those records already contain the fixed-lower curvilinear Ext repair problem, actual-source restrictions, local filtered cancellation, and equation-module budgets. The [formal visibility note](2026-10-27-formal-neighborhood-residual-visibility.md) already proves extension of full globally glued fixed-twist formal sections via G3. None is reproved here as new. This note instead allows **the embedded lower thickening to move**, identifies its compatibility obstruction with actual equation coefficients, and explains why moving the *full* primary component in a flat family is not a model of absorption.

The [independent flag-tangent audit](2026-10-27-absorption-flag-tangent-audit.md) reconstructs the tangent formula, the projective absorption control, and the fixed-quartic ribbon control below. Standard Quot deformation theory is being applied, not claimed as novel mathematics.

## 2. A finite ambient flag for arbitrary generic length

Purity gives the elementary useful bound

    I^m subset J subset I.                                      (1)

At the generic point of C, the maximal ideal of the Artinian algebra O_T has nilpotence exponent at most its length m. Thus I^m O_T vanishes generically. Its image in O_T is supported at finitely many points; a pure Cohen–Macaulay curve has no nonzero submodule with such support. Hence it vanishes everywhere. This proof does not require the generic algebra to be curvilinear or a complete intersection.

Fix any N with I^N subset J. Put

    B_N=I/I^N,       Q_T=I/J,       K_T=J/I^N.

The marked thickenings C subset T subset V(I^N) with a chosen Hilbert polynomial are exactly the corresponding quotients

    B_N -> Q_T,

in the Quot scheme of the **fixed coherent module** B_N. Indeed an O_X-submodule J/I^N of I/I^N is an ideal modulo I^N, and therefore gives an ideal J in O_X. Flatness of Q_T over a parameter base is equivalent to flatness of O_T, by

    0 -> Q_T -> O_T -> O_C -> 0.

One then restricts to the open locus of pure CM fibers when that condition is needed. Formula (1) permits N=m at any individual pure thickening of generic length m. It does not give a uniform bound on its Euler characteristic or on defining degrees, and no bounded unrestricted search is inferred.

The first-order tangent space to this marked flag is

    V_T = H^0 Hom_X(J/I^N, I/J).                                (2)

Here is an explicit derivation, which also fixes signs. For A=k[epsilon]/epsilon^2, represent the deformed ideal by the graph convention

    J_xi = {j + epsilon h : h mod J = xi(j)}.

The ordinary ideal-deformation condition is O_X-linearity of xi:J -> O_T. Keeping T above the fixed C requires image in I/J; keeping the fixed I^N inside the deformed ideal requires xi(I^N)=0. These are precisely (2). Conversely the usual graph construction for a quotient gives a flat first-order ideal from every such xi.

Because J annihilates I/J, these maps also factor through J/(I^N+J^2). This tangent source must not be confused with the equation module J/IJ used in contact determinants. The former governs motion of T; the latter governs generators through a fixed T.

Fresh primary references: [Stacks 0CZV](https://stacks.math.columbia.edu/tag/0CZV) gives the Hom description of quotient lifts, and [0CZU](https://stacks.math.columbia.edu/tag/0CZU) treats their separate Ext obstruction. In the present Quot problem the usual obstruction group for lifting the thickening itself is Ext^1_X(J/I^N,I/J), with the appropriate small-extension coefficients. That obstruction and the carrier obstruction next are different problems.

## 3. Exact tangent compatibility with arbitrary-degree actual equations

Fix positive degrees a,b and actual forms

    F in H^0(J(a)),       G in H^0(J(b)).

They may define a proper intersection containing T and additional residual curves. No conclusion about their generic multiplicity is imposed. Let Inc_N be the local incidence of this marked Quot flag and **affine coefficient spaces** of pairs through T. Projectivizing equations only removes the usual scaling directions; it does not change the compatibility criterion.

For each d use

    0 -> J(d) -> I(d) -> (I/J)(d) -> 0

and its connecting homomorphism

    delta_d:H^0((I/J)(d)) -> H^1(J(d)).

**Actual-pair tangent criterion.** A flag motion xi in V_T lifts to a first-order motion of the actual global pair iff

    Ob_(F,G)(xi)
      =(delta_a(xi(F)), delta_b(xi(G))) = 0.                    (3)

There is an exact sequence of tangent vector spaces

    0 -> H^0(J(a)) plus H^0(J(b))
      -> T_(T,F,G) Inc_N
      -> ker Ob_(F,G) -> 0.                                   (4)

Proof. Write F_epsilon=F+epsilon dotF and G_epsilon=G+epsilon dotG. By the graph convention, membership in J_xi is exactly

    dotF mod J=xi(F),        dotG mod J=xi(G).                  (5)

The coefficient corrections must be actual global forms. Because xi has image in I/J, any correction satisfying (5) vanishes on the fixed C. Thus its allowed source is exactly H^0(I(a)) or H^0(I(b)). The displayed cohomology sequence says that these lifts exist precisely when (3) vanishes. For a given xi, differences of lifts lie in H^0(J(a)) and H^0(J(b)), proving (4).

This works for arbitrary m,a,b. It neither substitutes k(C)-coefficients for actual coefficients nor assumes a general choice of carrier. A nonzero class rules out that specified first-order flag motion with the specified degrees and starting pair. It does not exclude a different motion, larger degree, or a different thickening.

## 4. The same distinction persists through an Artin lifting tower

Let B' -> B be a small extension of local Artin k-algebras, with kernel A annihilated by the maximal ideal of B'. Suppose a marked flat family T_B with I^N subset J_B subset I has **already been lifted** to a marked flat T_B' with ideal J_B'. For an actual section F_B in H^0(J_B(a)), flatness gives

    0 -> J(a) tensor_k A -> J_B'(a) -> J_B(a) -> 0,

where J is the special-fiber ideal. Its connecting class

    ob_(T_B',a)(F_B) in H^1(J(a)) tensor_k A                  (6)

vanishes iff the actual degree-a equation lifts through that chosen moving thickening. The lifts form a torsor under H^0(J(a)) tensor A. There is an independent analogous class for G_B. This follows directly from the exact sequence, not from an assumption of unobstructed Hilbert schemes.

The order of work matters. First lift the quotient/ideal T, whose obstruction is a Quot deformation problem. Then lift its two chosen global sections, whose obstruction is (6). If a coherent tower succeeds, its coefficients form actual fixed-degree formal coefficient series. This statement does not assert that the resulting formal arc converges or has been algebraized to an algebraic parameter curve; each finite stage is already a genuine homogeneous coefficient calculation.

There is a separate fixed-T source problem. To prescribe sections of the full equation module D_T=J/IJ, the exact sequence

    0 -> IJ(d) -> J(d) -> D_T(d) -> 0

gives an obstruction in H^1(IJ(d)). This is different from H^1(J(d)) in (3)–(6): the former lifts proposed generator classes through a fixed T, while the latter moves an already chosen actual equation with T. Keeping these two connecting maps distinct prevents a fixed-lower repair calculation from being mistaken for a deformation of a global pair.

For a bounded family and sufficiently large twists, Serre vanishing makes the higher cohomology of the relevant ideal sheaves vanish. On a neighborhood with base change, the spaces of sections are vector bundles and the pair incidence is their total space. Thus sufficiently large degrees remove this **section-lifting** obstruction. They do not ensure that two sections generate J along C, remove residual components, or solve an unrestricted degree problem. In particular, large-twist freedom cannot replace the equation-module generation condition.

## 5. A completely explicit nonzero obstruction on the fixed quartic

This is a control of (3), not a proposed STCI construction and not a reopening of the accepted low-degree exclusions. Assume characteristic zero. Let Q=V(q), q=x0*x3-x1*x2, be the unique smooth containing quadric, and take T=2C as a Cartier divisor on Q. Its ideal in P3 is

    J=(q)+I^2.

The accepted conormal sequence from [R-0020](../results/quartic_conormal_characteristic_jump.md) gives

    0 -> K=O_P1(-8) -> E=O_P1(-7)^2 -> L=O_P1(-6) -> 0,

with J/I^2=K and I/J=L. The marked ribbon flag, N=2, therefore has tangent

    V_T=H^0 Hom(K,L)=H^0(O_P1(2)),      dim V_T=3.              (7)

These directions are integrable motions of embedded double structures: surjections E -> L are pairs of linear binary forms without a common zero, modulo a common scalar. They form an open subset of P3. Here the Quot problem is on C, because I annihilates E, and its obstruction group Ext^1_C(K,L)=H^1(C,O(2)) vanishes. This is not a claim that the ambient Ext^1_X(i_*K,i_*L) vanishes; the ambient group can have additional normal-direction contributions. This is the elementary conormal-quotient construction of double curves, with ideal the inverse image of the kernel in I; local normal parameters give the ideal (x,y^2), proving purity and multiplicity two.

Now hold the degree-two carrier F=q at the starting point. Because Q is the unique containing quadric,

    H^0(I(2))=H^0(J(2))=k*q.

Its image in H^0((I/J)(2))=H^0(O_P1(2)) is zero. Consequently

    delta_2:H^0(O_P1(2)) -> H^1(J(2))

is injective. In fact it is an isomorphism: the ten ambient quadrics map to the nine-dimensional H^0(O_C(2)) with one-dimensional kernel kq, so H^1(I(2))=0. The symbol q trivializes K(2), and evaluation xi -> xi(q) identifies (7) with H^0(L(2)). Therefore **Ob_q is an isomorphism between three-dimensional spaces**. Every nonzero ribbon direction fails to lift together with any moving actual quadric equation through C.

For an actual proper pair through this T take

    F=q,       G=f^2,       f=x0^2*x2-x1^3,

of degrees (2,6). On Q the cubic f has divisor C+2ell for one ruling line ell. Hence the pair has cycle 2C+4ell and full C-primary component T. Since G belongs to the fixed I^2, xi(G)=0 for every flag motion. Thus (3) is exactly the preceding nonzero quadric obstruction in its first coordinate, with zero second coordinate.

This falsifies the naive inference “an embedded multiple curve can move, so the chosen-degree containing equations can be moved with it.” It also identifies the precise failure space; there is no genericity or computation gap. It gives no universal negative statement, and increasing degrees can remove the section-lifting obstruction as section 4 explains.

## 6. Why the full primary component cannot move flatly through absorption

In a flat projective family of thickenings T_s with fixed support C and fixed Hilbert polynomial, the leading coefficient is constant. Since deg T_s=(deg C)*m_s, the generic length m_s is constant. This is an immediate consequence of flat Hilbert-polynomial constancy; see [Stacks 0B9T](https://stacks.math.columbia.edu/tag/0B9T) for the underlying Euler-characteristic statement. Therefore absorption, which raises m_C in a flat family of total intersections, cannot be represented by a flat family of their **full C-primary components** alone.

There is an actual projective control, valid for every m>=1. In P3_[x:y:z:w] mark the line L=(x,y) and put

    Y_lambda=V(x, y^m*(y-lambda*z)).                            (8)

This is a flat family of proper (1,m+1) complete intersections: after imposing x=0, its equation is monic in y over k[lambda,z,w]. For lambda nonzero its cycle is mL+L_lambda, with L_lambda=(x,y-lambda*z). The two lines meet at [0:0:0:1]. At lambda=0 the cycle is (m+1)L. Thus (8) is genuine residual absorption in characteristic zero as well as positive characteristic.

The L-primary ideal is (x,y^m) for lambda nonzero and (x,y^(m+1)) at zero. Those components have degrees m and m+1, so fiberwise primary extraction is not a flat operation and does not commute with this specialization. This is a line control of the general issue, not a fixed-quartic example or a claim that its collision can be transferred to C0.

A **fixed lower witness** can nevertheless remain flat. In (8) take T=mL throughout; then Y_lambda contains T for every lambda, but T ceases to be the full primary component at zero. This is the useful role of (2)–(6): use a flat lower thickening to organize actual pairs, allow the pair to stop generating its ideal generically, and then identify a larger primary thickening in that special fiber. Requiring the lower witness to remain the full primary component would discard exactly the absorption boundary under investigation.

The same warning applies to torsion-free equation modules in a family. Even flat embedded thickenings can change generic algebra type. For example over a coefficient line t, the family

    J_lambda=(x^2-lambda*y, x*y, y^2)

has quotient free on 1,x,y over k[t,lambda]. At nonzero lambda its generic normal algebra is curvilinear of length three and needs two ideal generators; at zero it is k(t)[x,y]/(x,y)^2 and needs three. Rank-two equation modules cannot be carried across such a boundary without hypotheses. For families of primary components of actual pairs one must prove the needed flatness and base-change assertions rather than inherit them from flatness of the total intersection.

## 7. Constructive use and exact remaining tasks

This interface supplies a general rule rather than a favored degree pair:

1. Choose a marked lower thickening T, including its embedding and a Hilbert-polynomial stratum; retain (1) and the full quotient B_N -> I/J.
2. Construct actual sections F_a,G_b through it. If prescribing equation-module classes first, compute their H^1(IJ(d)) lifting classes.
3. When moving T, compute the map (3), not merely its tangent dimension. A class in ker Ob is a permitted first-order motion of the actual pair, with the lifts supplied by (5).
4. For further orders, keep the chosen quotient lift and evaluate (6) for both equations. Generic success does not replace the special zero loci or the next obstruction.
5. Track properness and actual residual germs. At a boundary where m_C rises, retain T as a lower witness and re-extract the larger full primary component in that fiber; do not assume its extraction commutes with base change.

The root lane's full attachment module and determinant correction describe each actual fiber. This note supplies the distinct compatibility conditions for moving the embedded lower data and the pair together. The smooth-carrier interpolation lane supplies positive characteristic-zero absorption families when degrees are allowed to grow; the ribbon control explains why existence of such motions cannot be transferred to a prescribed smaller degree.

No arbitrary-degree STCI obstruction or construction is asserted. What is now exact is where a proposed motion can fail, how to test it with actual coefficient spaces, why ample degrees can help with one obstruction, and why flatness of a full primary component is the wrong requirement at absorption.
