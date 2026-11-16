# Point witnesses and actual residual contact cycles

Let Y=V(F_a,G_b) be an actual proper projective intersection containing the fixed smooth C=C0, over an algebraically closed field. Write [Y]=m_C[C]+R with effective weighted residual cycle R. The results here recognize residual support and compare contact; they do not force positivity for every characteristic-zero pair.

## Point witnesses and the valuative residual contact cycle

## 1. First separate the residual question from its possible witnesses

Let \(k\) be algebraically closed of characteristic zero, let \(C=[s^4:s^3t:st^3:t^4]\) be the fixed smooth quartic, and let

\[
W=V(A,B)\subset\mathbf P^3_k
\]

be any proper complete intersection of two positive-degree hypersurfaces whose support contains \(C\). Write its fundamental cycle uniquely as

\[
[W]=m_C[C]+R,\qquad
R=\sum_{D\ne C}m_D[D]\ge0.
\]

Here \(D\) runs through the other reduced irreducible components and \(m_D\) is the generic length of \(W\) along that component. This makes sense even when \(m_C>1\). The subtraction defines a cycle; it does not claim a canonical scheme-theoretic residual to an unspecified multiple structure on \(C\).

The future universal target would be \(R\ne0\) for every such \(W\) in the stipulated characteristic-zero fixed-quartic setting. The present note supplies several equivalent ways to **recognize** \(R\ne0\) for a particular \(W\). Equivalence does not establish that the equivalent conditions always hold. In particular, no local invariant whose positivity is still unknown has resolved the global existence question.

This distinction makes room for adaptive investigation: choose the point, branch, ideal, or blowup suggested by the actual pair, rather than requiring one fixed numerical metric to order every complete intersection.

## 2. An adaptive point witness already exists at cycle level

For a closed point \(p\in C\) let

\[
e_p(W)=e_{\mathfrak m_p}(\mathcal O_{W,p})
\]

be the Hilbert--Samuel multiplicity. This is not the infinite length of the one-dimensional local ring. Over the infinite field \(k\), it can be computed as the length of a sufficiently general local linear slice. The word *general* matters: a hyperplane tangent to a branch need not calculate its multiplicity.

Associativity of multiplicities gives

\[
e_p(W)
=m_Ce_p(C)+\sum_{D\ni p}m_De_p(D)
=m_C+\sum_{D\ni p}m_De_p(D),                 \tag{1}
\]

because \(C\) is smooth. One precise route is to choose a common sufficiently general linear parameter for the finitely many branches through \(p\) and apply [Stacks, Lemma 42.3.2](https://stacks.math.columbia.edu/tag/02QG), which adds the generic lengths of the components with the appropriate slice lengths. All terms in the residual sum are positive when present.

A proper projective complete-intersection curve is connected. For this setting one needs only the elementary Koszul calculation: from

\[
0\longrightarrow\mathcal O(-a-b)
\longrightarrow\mathcal O(-a)\oplus\mathcal O(-b)
\longrightarrow I_W\longrightarrow0
\]

and the vanishing of intermediate cohomology of line bundles on \(\mathbf P^3\), obtain \(H^1(I_W)=0\) and then \(H^0(\mathcal O_W)=k\). A disconnected scheme would have a nontrivial idempotent, contradicting this equality. The cohomology input is [Stacks, cohomology of projective space](https://stacks.math.columbia.edu/tag/01XS). This proof also covers nonreduced complete intersections.

Connectedness now implies

\[
R\ne0
\quad\Longleftrightarrow\quad
\exists p\in C:\ e_p(W)>m_C.                 \tag{2}
\]

Indeed, if residual components exist, their finite union must meet \(C\); otherwise the support would be disconnected. At such a meeting point equation (1) is strict. Conversely, strictness in (1) directly exhibits a residual component through that point.

Thus one may adaptively seek a point with multiplicity exceeding the generic multiplicity along \(C\). The point need not be one of the distinguished endpoints. The formula is valid in other characteristics as well; characteristic zero has not been used to force positivity.

It is useful to retain the whole finite effective cycle

\[
M_C(W)=\sum_{p\in C}\bigl(e_p(W)-m_C\bigr)[p]. \tag{3}
\]

It is supported exactly where residual components meet \(C\). For the distinguished reduced characteristic-zero \(Z\) of [STCI-R-0021](../../results/quartic_mu4_degeneration.md), write \(p=[1:0:0:0]\) and \(q=[0:0:0:1]\). Then it is \(3p+3q\): four smooth branches meet at each endpoint and the generic multiplicity of the marked component is 1. By contrast, the accepted characteristic-two fiber has fundamental cycle \(4[C]\), so \(M_C(W)=0\). That is consistent with (2), not an exception to it. The local multiplicity test does not detect internal nilpotent geometry when all cycle mass remains on \(C\).

## 3. A contact cycle built from the actual residual branches

For every reduced residual component let

\[
\nu_D:\overline D\longrightarrow D
\]

be its finite normalization. Since \(D\ne C\), the image ideal \(I_C\mathcal O_{\overline D}\) is nonzero at the generic point and has finite support of zeros. The smooth curve \(\overline D\) has discrete valuation rings at its closed points, so

\[
I_C\mathcal O_{\overline D}
=\mathcal O_{\overline D}(-T_D),\qquad
T_D=\sum_{r\mapsto C}
\operatorname{ord}_r(I_C\mathcal O_{\overline D})[r].
\]

Define the **valuative contact cycle**

\[
B_C^{\mathrm{val}}(R)
=\sum_Dm_D(\nu_D)_*T_D.                       \tag{4}
\]

For the algebraically closed field under discussion, this simply sums the branch orders at their image points on \(C\). Retain the actual effective cycle, rather than only its Chow class: on \(C\simeq\mathbf P^1\), rational equivalence remembers only its degree and loses the endpoint concentration. Nor is this contact invariant determined by the rational-equivalence class of \(R\) in \(\mathbf P^3\). Over a nonclosed field, pushforward also includes residue-field degrees; omitting them would change the invariant.

The definition uses the actual marked embedding of \(C\) in the ambient space. If \(I_C\) is locally generated by \(f_1,\ldots,f_s\), its coefficient on a branch is

\[
\min_i\operatorname{ord}_r(\nu_D^*f_i).
\]

The cycle is invariant under projective automorphisms carrying the entire marked pair to another marked pair. Changing the generators does not change the minimum: it is the order of the ideal itself. This is more adaptable than selecting one fixed ambient polynomial or one predetermined valuation for every pair.

There is a direct blowup interpretation. Let

\[
\pi:\operatorname{Bl}_C\mathbf P^3\longrightarrow\mathbf P^3
\]

have exceptional divisor \(E\). Because the pulled back ideal on \(\overline D\) is invertible, \(\nu_D\) lifts to the blowup by its universal property. Intersecting the **strict residual cycle** \(\widetilde R\) with \(E\) gives

\[
B_C^{\mathrm{val}}(R)=\pi_*(E\cdot\widetilde R). \tag{5}
\]

The intersection is proper because no strict transform of a component \(D\ne C\) lies in \(E\). Formula (5) is a cycle-level identity: one may calculate it on the normalizations and push forward. The [universal property of the blowup](https://stacks.math.columbia.edu/tag/01OF), [Cartier pullback](https://stacks.math.columbia.edu/tag/01WQ), and [degrees on curves](https://stacks.math.columbia.edu/tag/0AYQ) provide the standard foundations.

The use of strict residual transform is essential. The full inverse image of \(W\) contains exceptional geometry over \(C\); those exceptional curves or surfaces are not additional components of \(W\) downstairs. When \(R=0\), equation (5) uses the zero strict residual cycle, however complicated the full inverse image is.

Every residual branch through \(C\) contributes a positive integer. Combined with connectedness,

\[
R\ne0\quad\Longleftrightarrow\quad
B_C^{\mathrm{val}}(R)\ne0.                    \tag{6}
\]

Once again this is a recognition criterion. Writing its right side has not proved its positivity for every characteristic-zero pair.

## 4. Multiplicity excess and higher tangency separate cleanly

Choose local ambient coordinates \((u,x,y)\) at \(p\) with \(C=(x,y)\). On a normalized residual branch, write

\[
a_r=\min\{\operatorname{ord}_r(u),\operatorname{ord}_r(x),
\operatorname{ord}_r(y)\},\qquad
b_r=\min\{\operatorname{ord}_r(x),\operatorname{ord}_r(y)\}.
\]

Then \(a_r\) is the branch multiplicity at \(p\) and \(b_r\) is its contact with the ideal of \(C\). Therefore \(b_r\ge a_r\), and summing gives

\[
B_C^{\mathrm{val}}(R)\ge M_C(W).              \tag{7}
\]

The difference is an effective cycle recording contact beyond the multiplicity of the residual branches. It distinguishes a large number of branches crossing \(C\) from a smaller number following its tangent to higher order.

For \(Z\), the other three quartics have contact order 3 with \(C\) at each endpoint. Thus

\[
M_C(Z)=3p+3q,\qquad
B_C^{\mathrm{val}}(R_Z)=9p+9q,
\]

and the excess contact is \(6p+6q\). In the generic deformation picture \(C\cup D\) with 18 transverse nodes, each coefficient of both cycles is 1. This offers two complementary ways to compare configurations without asserting a total ordering.

A degree-dependent estimate is available, but it is not a bounded-degree solution. Since the actual fixed-quartic ideal is generated in degrees at most 3, as recorded with the explicit generators in the [deformation laboratory](residual_global_models.md), choose a general cubic through \(C\) avoiding all components of \(R\). On every normalized residual component its divisor has degree \(3\deg D\) and dominates \(T_D\). Hence

\[
0\le\deg M_C(W)\le\deg B_C^{\mathrm{val}}(R)\le3\deg R
=3(ab-4m_C).                                 \tag{8}
\]

The two contact degrees vanish exactly when \(R=0\), by connectedness and equations (2), (6), and (7). Thus this chain is a numerical consistency check, with no universal positive lower bound. It controls contact after the degrees \(a,b\) and residual degree are known. It provides no uniform upper bound on the possible degrees of the defining equations, no finite search over all pairs, and no positive lower bound when \(R=0\) remains possible.

## 5. A sharp warning: branch contact is not always the conductor boundary

The equality with \(9p+9q\) for \(Z\) reflects its special local planar arrangement. It does not justify identifying (4) with the conductor or the determinant boundary for arbitrary complete intersections.

Here is a small complete-intersection counterexample. In affine 3-space set

\[
A_0=k[x,y,z]/(xy-xz,xy-yz).
\]

This is the reduced union of four lines in directions

\[
(1,0,0),\quad(0,1,0),\quad(0,0,1),\quad(1,1,1).
\]

They are the affine cone over four points in \(\mathbf P^2\) with no three collinear, a complete intersection of two quadrics. Equivalently, use the same two equations in \(\mathbf P^3_{[x:y:z:w]}\); the four projective lines share the vertex \(p=[0:0:0:1]\). This is a counterexample to a universal identification of invariants, not a substitute curve for the fixed quartic in the main investigation.

Its normalization is \(B=\bigoplus_{i=1}^4k[t_i]\). In the grading at the vertex:

- the image of \((A_0)_0\) is the one-dimensional diagonal constants;
- the image of \((A_0)_1\) is \(\{\,(a,b,c,a+b+c):a,b,c\in k\,\}\), of dimension 3;
- for every degree \(d\ge2\), the image is all four copies of the degree-\(d\) piece.

The last assertion can already be checked with quadrics: \(xy\) isolates the fourth direction, and \(x^2-xy\), \(y^2-xy\), \(z^2-xy\) isolate the first three. Multiplication by a linear form nonzero on each direction extends the conclusion to all higher degrees. There is no degree-one vector supported on just one branch. Consequently the conductor extends to

\[
\bigoplus_{i=1}^4t_i^2k[t_i]\subset B,
\]

and its boundary on each normalized line has coefficient 2. The delta invariant is \((4-1)+(4-3)=4\), consistent with total conductor degree 8 for this Gorenstein singularity.

Now mark the \(x\)-axis \(L_1\) as \(C\) for this example. Its ideal is \((y,z)\). On each of the other three lines the pulled back ideal has order 1. Therefore

\[
B_{L_1}^{\mathrm{val}}(L_2+L_3+L_4)=3[p],
\qquad \text{conductor boundary on }L_1=2[p].  \tag{9}
\]

The actual first-normal determinant also has order 2: along the \(x\)-axis with parameter \(t=x\), the two linear normal rows are \((t,-t)\) and \((t,0)\), with determinant \(t^2\).

The scheme-theoretic intersection of \(L_1\) with the residual union has length 2, not 3. No nonzero linear form vanishes on all three residual directions, while \(x^2-xy\) does vanish there and restricts to \(x^2\) on \(L_1\). Hence the image of the residual ideal in \(k[x]\) is exactly \((x^2)\). The three individual branch intersections cannot be added as intersection lengths of the union.

This is the failure mechanism: a nonplanar union has relations among the gluing conditions. Pairwise valuations of a marked ideal, intersection with the residual *scheme*, and the conductor of the total ring need not add in the same way. In this example \(M_{L_1}(W)=B_{L_1}^{\mathrm{val}}(R)=3[p]\) while the conductor and determinant boundaries are \(2[p]\).




## Characteristic reach

The associativity/connectedness detector, normalization-contact construction and cubic degree bound are characteristic-free. The four-line conductor control is a scoped characteristic-zero example. Actual positive-characteristic supported pairs have zero residual contact and violate no recognition theorem.

## Wedge degeneracy distinguishes neither thickness nor residual contact

At a point of the smooth marked curve, the first normal class of an equation
is its entire ambient differential, because its tangential derivative on C
vanishes. The hypersurface Jacobian criterion says dF(p)=0 exactly when its
carrier is singular at p. When dF(p) and dG(p) are both nonzero, their wedge
vanishes exactly when the two smooth tangent planes coincide. A zero
individual differential instead means a singular carrier; it is not tangency
between two smooth carriers. For an integral curve singular at some closed
points, this conormal-bundle formulation is restricted to its smooth locus;
the fundamental-cycle degree identity itself needs no smoothness.

Two exact local controls work in arbitrary characteristic, in k[[t,x,y]]
with marked C=(x,y):

- F=x and G=x+y^4 have identical nonzero differentials dx along C, with
  identically zero wedge. Their ideal is (x,y^4), of sole reduced support C
  and generic length four. No residual curve occurs.
- F=x and G=x+y(y-t^4) have ideal (x,y(y-t^4)). The reduced components are
  C and D=(x,y-t^4), meeting in length four in the smooth carrier x=0.
  Their two carrier differentials coincide at t=0, while generically on C
  dG=dx-t^4dy is independent of dF=dx, and generic marked length is one.

Thus generic proportionality of first symbols can indicate thickness,
whereas a special-point dependence can indicate attachment; neither wedge
vanishing alone is an obstruction. These are explanatory local models,
not asserted homogeneous realizations on the fixed quartic. The actual
projective residual test remains the full generic length and degree identity.


## Consolidated historical source: `research/supplements/MIXED_SEXTIC_CONTACT.md`

# Exact degree-six branch contact on a mixed-weight sextic

Over an algebraically closed characteristic-zero field, this is the full actual degree-six mate calculation for \(q^3+\alpha c_0^2+\beta c_2^2\), \(\alpha\beta\ne0\). Its independent computation and the mathematical rank-to-kernel argument are retained. The stronger [test-curve theorem](../curve/carrier_test_curves.md) excludes every mate degree on the same source; the calculation here additionally proves integrality, the individual branch-order bound, and a quantitative residual floor for proper sextic pairs. These are useful distinct conclusions.

## Exact family and bounded endpoint

Let k be an algebraically closed field of characteristic zero, let
C=[s^4:s^3t:st^3:t^4] in P3, and write

\[
q=x_0x_3-x_1x_2,\quad c_0=x_1^3-x_0^2x_2,\quad
c_2=x_2^3-x_1x_3^2.
\]

For **every** alpha,beta in k with alpha*beta nonzero, put

\[
F_{\alpha,\beta}=q^3+\alpha c_0^2+\beta c_2^2.
\tag{1}
\]

The completed incidence problem here keeps all 84 scalar coefficients
of an arbitrary actual homogeneous sextic G. It asks for a proper pair
(F,G) with generic transverse intersection length at least nine along C.
Nine is the necessary sole-support value 6*6/4. The answer is **empty**.
More precisely:

1. Every surface (1) is integral.
2. For every homogeneous sextic G with no common surface factor with F,
   the generic length along C is at most eight. Thus
   [V(F,G)]=m_C[C]+R has deg R=36-4m_C at least four whenever G contains C.
3. On either of the two formal transverse branches of F at generic C,
   a global sextic has vanishing order at least five **if and only if**
   it is a scalar multiple of F.

The numerical bound eight is an upper bound; attainment is not asserted.
This is a complete all-parameter, all-global-sextic calculation, rather
than a collection of selected carrier samples. The uniform rank statement
uses the recorded exact parameter-ideal certificate; it has not been
independently recomputed in this mathematical review. Taken alone this calculation does not exclude
higher mate degrees, other mixed-weight carriers, or the boundary
alpha*beta=0, and it does not resolve unrestricted STCI.

## Torus normalization retains every nonzero parameter

Use the torus preserving C,

\[
\tau_\rho(x_0,x_1,x_2,x_3)
=(x_0,\rho x_1,\rho^3x_2,\rho^4x_3).
\]

The weights of q,c0,c2 are 4,3,9. Choose rho with
rho^12=-alpha/beta. Dividing F composed with tau_rho by beta*rho^18
therefore gives

\[
F_h=hq^3+c_2^2-c_0^2,\qquad
h=1/(\beta\rho^6)\ne0,\qquad h^2=-1/(\alpha\beta).
\tag{2}
\]

This is a projective automorphism and scalar rescaling. It preserves
properness, actual global coefficient spaces and generic contact.
Every nonzero alpha,beta is covered; no convenient parameter minor is
inverted. The computation uses the indeterminate `k` for h.

## Both split branches, including asymmetric contact

On x0=1 set x1=z, x2=z^3+v, and x3=z^4+q+zv. These are actual normal
coordinates over k(z). Here c0=-v, and

\[
c_2=(z^3+v)^3-z(z^4+q+zv)^2
=-2z^5q+z^6v+\text{terms of normal order at least two}.
\]

The quadratic initial form of (2) factors as

\[
(-2z^5q+(z^6-1)v)(-2z^5q+(z^6+1)v).
\tag{3}
\]

The factors are distinct over k(z), for every h, so these are two smooth
formal branches defined over k(z). This is a **split** node. Equality of
the two branch orders is not used. In particular, the earlier nonsplit
node argument for a different sextic family cannot be applied here.

Choose the branch with

\[
v_1=\frac{2z^5}{z^6+1}q.
\]

If v has been determined through degree n-1, the coefficient of the new
term v_n*q^n in F_h is -4z^5*v_n*q^(n+1). Consequently, for n=2,3,4,

\[
v_n=\frac{[q^{n+1}]F_h(q,v_{<n})}{4z^5}.
\tag{4}
\]

This constructs v modulo q^5 and makes F_h zero modulo q^6. The
coefficients are polynomial in h over
Q[z,z^-1,(z^6+1)^-1]. A global sextic with branch order at least five
has all its q^0 through q^4 coefficients zero as rational functions of z.
Their exact specialization on the two finite schemes below is therefore
a necessary condition, valid for every h and every extension of the
constant field.

The other branch is covered without assuming symmetry of G. Choose
sigma with sigma^6=-1. Then F_h composed with tau_sigma equals
-F_{-h}, and c2=+c0 and c2=-c0 are interchanged. The same all-nonzero-h
calculation therefore applies separately to each branch.

## Exact global coefficient calculation and all rank strata

The primary historical Macaulay2 verifier
works over Q[h], with no inversion of h during matrix construction. The
[independent Macaulay2 verifier](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/stci_mixed_contact_audit_2026_10_29.m2)
computes both exceptional polynomials and the independently assembled rank
strata. The retirement replay matched its [historical output](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/stci_mixed_contact_audit_2026_10_29.txt).
For the first sample scheme z^18=1,

\[
(z^6+1)^{-1}=(z^{12}-z^6+1)/2,\qquad z^{-5}=z^{13}.
\]

The 18 points are distinct in characteristic zero, and none is a pole of
(4). Simultaneous reduction in Q[h,z,q]/(z^18-1,q^6) makes all calculations
exact. Evaluating all 84 degree-six monomials and retaining q-degrees
zero through four gives a 90 by 84 matrix M over Q[h]. Its columns are
actual global monomials; they are never allowed arbitrary k(z) source
coefficients.

The subgroup mu6 splits the matrix into six blocks. A monomial with
weight w=e1+3e2+4e3 has its q^j coefficient supported in z-exponents
congruent to w-4j modulo six. Therefore the blocks have 15 rows and,
respectively, 16,13,14,14,14,13 columns. For each block we compute the
presentation of the cokernel of its transpose over the PID Q[h].

| Weight mod 6 | Nonzero torsion invariant factors from z^18=1 | Free rank |
| --- | --- | --- |
| 0 | h, h, h^2 P7(h) | 1 |
| 1 | h, h, h | 0 |
| 2 | h, h, h^2 | 0 |
| 3 | h, h, h, h^2 | 0 |
| 4 | h, h, h^2 | 0 |
| 5 | h, h, h | 0 |

Here

\[
\begin{aligned}
P_7(h)={}&1215h^7+183834h^6+16985880h^5+1305652552h^4\\
&+56634503616h^3+1412125752640h^2\\
&+14480360156160h-16148528394240.
\end{aligned}
\]

The first finite test alone leaves the roots of P7 as exceptional
parameters. They are **not discarded**. Add a second sample scheme
z^18=8 in the weight-zero block. In this quotient,

\[
(z^6+1)^{-1}=(z^{12}-z^6+1)/9,\qquad z^{-5}=z^{13}/8.
\]

Its 18 points are also distinct and avoid every pole. The combined
30 by 16 weight-zero block has torsion invariant factors h,h,h^2 and
free rank one. Equivalently, the independent verifier computes a second
degree-seven exceptional factor Q7 and checks gcd(P7,Q7)=1 over Q[h].
Thus every nonzero h, including every root of P7, has total matrix rank
83. The displayed excluded value h=0 corresponds to the factored carrier
c2^2-c0^2; it lies outside (2).

The primary script additionally checks that the actual ambient vector
of F_h is annihilated and has a coefficient equal to one. Hence F_h
specializes to a nonzero kernel vector at **every** parameter. Rank 83
proves the kernel is exactly its scalar span. Its assertions check the
ranks and that all torsion away from h=0 vanishes, using the annihilator
of Ext^1 over Q[h]. These checks retain the full one-parameter rank
locus; they are not modular sample-rank extrapolations.

A rational-function branch identity must pass these finite necessary
tests. Since their kernel already equals the actual carrier span, the
same holds for the full global branch-contact incidence. Conversely,
F_h itself vanishes identically on the branch, so this identifies the
kernel exactly.

## Integrality and residual consequences

Suppose F_h had a proper homogeneous factor H vanishing identically on
the chosen formal branch. At least one factor would do so, since the
branch evaluation has integral target k(z)[[q]]. Its degree d is at most
five, and

\[
H\cdot H^0(\mathbf P^3,\mathcal O(6-d))
\]

would give at least four independent actual sextics in the branch-contact
kernel. Multiplication by H is injective in the polynomial ring. This
contradicts its proved dimension one. Thus F_h is integral; this argument
uses the completed global calculation and does not assume integrality
while computing it.

For any proper sextic G, the two finite branch orders n+ and n- are
therefore each at most four. The transverse local intersection length
is their sum, at most eight. A sole-support (6,6) complete intersection
would need length nine by Bezout. Therefore the required global-contact
incidence is empty, and every proper containing pair in this family has
a genuine residual curve of degree at least four. No exceptional vertical
cycle is counted as a residual curve.

## Necessary exact computational support

The historical primary verifier and [separately assembled verifier](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/stci_mixed_contact_audit_2026_10_29.m2), with the independent saved output, retain the exact \(\mathbf Q[h]\) matrix and both exceptional rank strata. A sampled rank at one \(h\), or the first finite scheme alone, would not establish the theorem: the second scheme removes the roots of \(P_7\). Their algebraic interpretation is the kernel of actual global sextics restricting to order at least five on one formal branch. No function-field source coefficients are permitted. The inherited independent review reconstructed the recurrence, weight blocks, invariant factors, and integrality deduction. No fresh rank run was required for the editorial consolidation.
