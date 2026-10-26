# Independent audit of the residual ruling-line degeneration

Date: 2026-10-25. Reviewer: independent cycle-notebook audit agent.
Status: reviewed exact example and local deformation deductions; exploratory
and not canonically promoted.

The reviewer followed [the research index](../INDEX.md). This audit concerns
the new [line-degeneration note](2026-10-25-ci-cycle-line-degeneration.md);
the original prescribed \(\mu_4\) family in
[R0021](../results/quartic_mu4_degeneration.md) is an accepted reference and
its proof was not rerun. The smooth member at parameters \((2,3)\) has its
separate [exact audit](2026-10-25-ci-cycle-smooth-residual-audit.md).

**Outcome.** The checked member at \((1,1)\) is exactly the union of the marked
quartic \(C\), a ruling line \(L\), and a smooth geometrically integral curve
\(E\) of degree eleven and genus twelve. All twenty-three pairwise attachment
points are ordinary nodes and there are no triple points. The five residual
nodes have the same nonzero smoothing direction in the specified
two-parameter family. Locally their smoothing parameters are unit multiples
of \(ab-1\). Their product has order five, with the discriminant qualification
in section 5 below.

## 1. The exact pair and its geometric data

Use the actual forms \(F,G,Q,A,D_3,H_0,H_1\) displayed in the contribution
note, and
\[
f_a=F+QH_0+a x_0A,\qquad
g_b=G+QH_1+b x_3D_3.
\]
At \((a,b)=(1,1)\), set
\[
J=(f_1,g_1),\quad I_D=\operatorname{sat}(J:I_C),\quad
I_L=(x_0+x_1,x_2+x_3),\quad
I_E=\operatorname{sat}(I_D:I_L).
\]

A separate rational Macaulay2 calculation independently reconstructed:

- \(\operatorname{codim}J=2\), \(\deg D=12\), and \(P_D(n)=12n-15\).
- \(I_D=I_L\cap I_E\) and \(J=I_C\cap I_D\), as exact ideals.
- \(\deg E=11\) and \(P_E(n)=11n-11\), hence arithmetic genus twelve.
- The saturated projective Jacobian singular ideal of \(E\) is the unit ideal.
- \(H^0(E,\mathcal O_E)=\mathbf Q^1\).
- \(L\cap E\) has five reduced geometric points, \(C\cap E\) has seventeen,
  and \(C\cap L\) has one; their triple intersection is empty.

The independent suite returned
\[
(\deg E,P_E,\deg(L\cap E),\deg(C\cap E),H^0(\mathcal O_E))
=(11,11n-11,5,17,\mathbf Q).
\]
The durable
[Macaulay2 verifier](../computations/ci_cycle_line_degeneration_2026_10_25.m2)
was then replayed and passed. The geometric smoothness plus proper
global-section argument used in the preceding smooth-residual audit proves
geometric connectedness and hence geometric integrality of \(E\). This is
stronger than primality over \(\mathbf Q\).

Reduced length-one intersections of two smooth branches give distinct tangent
directions. Thus these are transverse nodes. There are exactly five nodes
of \(D=L\cup E\), and exactly twenty-three nodes of \(C\cup L\cup E\).
The absence of triples is necessary for both counts and was tested separately.

## 2. Reconstructing the moving line

On \(Q\), use Segre coordinates
\[
(x_0,x_1,x_2,x_3)=(\rho c,\rho d,\sigma c,\sigma d),\qquad
K_C=\rho d^3-\sigma c^3.
\]
Direct substitution, independent of the residual ideal computation, gives
\[
f_a|_Q=\rho^3(d+ac)K_C,\qquad
g_b|_Q=-\sigma^3(c+bd)K_C.
\]
The ruling factors coincide precisely when \(ab=1\). Near \((1,1)\), this
gives the actual line
\[
L_a=V(x_1+a x_0,\ x_3+a x_2).
\]
It meets \(C\) at curve parameter \(u=-a\).

The fixed line \(L=L_1\), by contrast, lies on both hypersurfaces only when
\(a=b=1\). These two statements must remain distinct: the fixed-line locus
is a point, while the moving-ruling locus is the hyperbola. The formulas
identify lines in this ruling on \(Q\); no unrelated global classification
of lines in all intersections is being inferred from them.

The standard-library
[identity verifier](../computations/ci_cycle_line_degeneration_2026_10_25.py)
checks the actual global restrictions and the boundary formulas. Its fourteen
checks also passed independent replay.

## 3. The five-point scheme and normal matrix

With \(L=[-r:r:-s:s]\), put
\[
P_5=4r^5-2r^4s+9r^3s^2+2r^2s^3+3rs^4+2s^5.
\]
The actual pullback of \(L\cap E\) is \((P_5)\), which is geometrically
squarefree. The point \(C\cap L\) has \(r/s=-1\), and
\(P_5(-1,1)=-14\ne0\).

Use normal coordinates \(n_0=x_0+x_1\), \(n_1=x_2+x_3\). Differentiating the
actual pair at \((1,1)\) yields the displayed matrix in the contribution,
whose determinant is
\[
-(r+s)P_5.
\]
Its second-column entries are
\[
F_1=-r(r+s)(r+2s),\qquad
G_1=-4r^3+2r^2s-9rs^2-s^3.
\]
The exact coprimality checks show that \(F_1\), \(s\), and \(r+s\) are units
at every point of \(P_5=0\). Thus \(f_1\) is a legitimate local smooth
carrier at each residual node, even though no such choice is assumed for
arbitrary pairs in the wider investigation.

The determinant has six zeros: five residual attachments and one attachment
to \(C\). Its degree six also agrees with the determinant of the quartic
first-normal map on a line, whose two summands each have degree three.

## 4. Independent first-order smoothing calculation

At a point of \(P_5=0\), parameter variations have
\[
\delta f=-r^3(r+s)\delta a,\qquad
\delta g=-s^3(r+s)\delta b.
\]
Eliminate the normal coordinate with nonzero derivative \(F_1\). A convenient
representative of the one-dimensional node-smoothing class is
\[
\delta g-\frac{G_1}{F_1}\delta f
=(r+s)\left(\frac{G_1}{F_1}r^3\delta a-s^3\delta b\right).
\]
The independently checked polynomial identity
\[
-G_1r^3=rP_5+F_1s^3
\]
reduces this class to
\[
-s^3(r+s)(\delta a+\delta b).
\]
The scalar is nonzero at all five nodes. This proves the common smoothing
direction, with no choice of numerical approximations to the roots of \(P_5\).
The sign differs from another possible cokernel representative only by a unit.

The direction is precisely normal to \(ab=1\) at \((1,1)\). A tangent
direction to that hyperbola does not smooth the nodes to first order; a
transverse direction smooths all five to first order.

## 5. From first order to the local discriminant

First-order agreement alone would not prove that the five full discriminant
branches coincide. Here the moving line supplies the additional information.
Along \(ab=1\), a neighborhood of the checked member retains a smooth
remaining component and five simple intersections with \(L_a\). Simplicity
of the intersections ensures that their positions persist after an étale or
analytic localization. Hence each node's smoothing parameter vanishes along
the actual smooth divisor \(h=ab-1=0\).

After labelling the geometric nodes, the standard local form is
\(xy=\tau_i(a,b)\). The completed version and its hypotheses are in
[Stacks, Lemma 53.20.11](https://stacks.math.columbia.edu/tag/0C58); the
[étale nodal-family description](https://stacks.math.columbia.edu/tag/0H8M)
gives the corresponding local formulation. Since \(h\) divides \(\tau_i\)
and its derivative transverse to \(h=0\) is nonzero, the quotient is a unit:
\[
\tau_i=h\,u_i,\qquad u_i(1,1)\ne0.
\]
Therefore
\[
\prod_{i=1}^5\tau_i=(ab-1)^5u,\qquad u(1,1)\ne0.
\]

The multiplicity five belongs to this product of node-smoothing contributions,
or the corresponding norm/Fitting discriminant. It is not a universal claim
about every scheme structure called a discriminant: the scheme-theoretic
image of the critical locus can have the reduced ideal \((ab-1)\). The
contribution note now states this distinction explicitly.

To exclude additional residual singularities near this parameter, use a
proper flat model. The two strict transforms on
\(\operatorname{Bl}_C\mathbf P^3\) are divisors of class \(4H-\mathcal E\).
Their central proper intersection is the residual curve. A relative regular
sequence gives flatness after shrinking the parameter neighborhood. At the
eighteen reduced marked attachments the residual curve crosses \(\mathcal E\)
transversely, and blowdown is an isomorphism on it. These conditions remain
open nearby. Properness and openness of smoothness then reduce the local
residual singular-fiber support to the five node neighborhoods just analyzed.
This supplies the needed geometric bridge; the finite first-order matrix
calculation alone would not supply it.

The statement is local near \((1,1)\). It does not assert that the entire
affine parameter plane, the whole hyperbola, or every point of a path to
\((2,3)\) has only these singularities.

## 6. Genus and topology cross-checks

The residual curve satisfies
\[
p_a(L\cup E)=0+12+5-1=16.
\]
Its five gluing edges between two components have four graph cycles.
Smoothing all five nodes joins the components and converts these four
cycles into genus, yielding the smooth residual genus sixteen.

For the total curve, the line member has three normalized components of
total genus twelve and twenty-three nodes, hence arithmetic genus
\[
12+23-3+1=33.
\]
Its dual graph has first Betti number twenty-one, so over \(\mathbf C\)
the total curve has \(b_1=24+21=45\), \(b_2=3\), and Euler characteristic
\(-41\). The smooth-residual member has \(b_1=49\), \(b_2=2\), and Euler
characteristic \(-46\). The drop by five agrees with smoothing five ordinary
nodes. The componentwise canonical-degree table in the contribution also
checks: each component satisfies \(2g_i-2+n_i=4d_i\).

This is deformation that absorbs a line into a higher-genus residual
component, not a contraction of that line. The explicit local discriminant
and finite ideal identities support this picture without an STCI inference.

## 7. Review boundary

The exact geometric example, moving ruling, five common first-order smoothing
classes, local product-discriminant statement, and topology calculations pass
independent review with the qualifications above. Evidence is reproducible
using the two durable scripts linked in sections 1 and 2. No new canonical
record, all-pairs theorem, or global discriminant classification is asserted.
