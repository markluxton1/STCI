# Independent audit: marked-thickening motion and actual-pair tangents

Date: 2026-10-27. Reviewer: formal-lane focused deformation/literature agent, independent of the proposed argument. **Status: the claims below pass independent reconstruction in their stated scopes; provisional evidence, no canonical promotion.** The task is to distinguish movement of a fixed lower thickening from movement of actual global equations and from a jump of its primary thickness.

This audit followed [INDEX](../INDEX.md) then [MAP](../MAP.md). It checks a general deformation interface rather than reopening the accepted quartic-carrier or conormal results. The abstract tangent calculation is standard embedded/Quot deformation theory; no novelty claim is made.

## 1. Setup and the exact tangent space

Let X=P3_k, let C be a fixed smooth curve with ideal sheaf I, and let C subset T subset V(I^N) be a marked embedded thickening with ideal J, so I^N subset J subset I. Fix its Hilbert polynomial. The tangent calculation does not require T to be lci, Gorenstein, generically curvilinear, or Cohen--Macaulay; those conditions may be imposed separately on the research stratum.

The space of first-order embedded motions of T preserving both fixed outer schemes is

    H0(X, Hom_X(J/I^N, I/J)).                         (1)

I reconstructed this on an affine open Spec A. Adopt the graph convention that xi:J->A/J corresponds to

    J_xi = { j+epsilon*h : j in J and h mod J=xi(j) }

inside A[epsilon]/(epsilon^2). A-linearity makes this an ideal. It reduces to J and intersects epsilon*A in epsilon*J, so A[epsilon]/J_xi is flat over the dual numbers. Conversely every embedded flat first-order ideal has this form, independently of the choice of representatives h. The construction localizes, hence glues.

The two fixed incidences give exactly the advertised restrictions. The condition J_xi subset I[epsilon] says that xi(J) is contained in I/J. The condition I^N[epsilon] subset J_xi says xi vanishes on I^N. Thus (1) is necessary and sufficient. In particular a Hom into O_T would allow motion off the fixed C, and omitting the quotient by I^N would allow motion outside the selected finite ambient neighborhood.

Equivalently the Hom in (1) factors through J/(I^N+J^2), since J kills the target I/J. This does not turn it into the source equation module J/IJ: the two quotients answer different questions.

## 2. Pair-lifting condition and exact sequence

Fix actual global forms F in H0(J(a)), G in H0(J(b)), with a,b>0. Work with affine spaces of coefficient vectors, so there is no projective scaling quotient in the tangent calculation. For a tangent xi from (1), a pair motion

    F+epsilon*f, G+epsilon*g

lies in the moving ideal iff

    f|_T = xi(F),  g|_T = xi(G).                     (2)

The signs match the graph convention above. Choosing the opposite graph convention reverses both signs without changing any kernel or obstruction conclusion.

Since xi takes values in I/J, a global lift satisfying (2) automatically vanishes on C. Therefore f and g are actual elements of H0(I(a)) and H0(I(b)), not function-field coefficients. The exact sequence

    0 -> J(d) -> I(d) -> (I/J)(d) -> 0

gives connecting maps delta_d into H1(J(d)). Define

    Ob_(F,G)(xi) = (delta_a(xi(F)), delta_b(xi(G))).  (3)

Equation (2) has global lifts iff (3) vanishes. If so, the choices form an affine torsor under H0(J(a)) plus H0(J(b)). Equivalently, the tangent space to the marked-thickening/pair incidence has exact sequence

    0 -> H0(J(a)) plus H0(J(b))
      -> T_(T,F,G) Inc
      -> ker Ob_(F,G) -> 0.                         (4)

This is exact at the right end: by definition a vector in the kernel has the required two global lifts. A motion of T alone does not assert that this obstruction vanishes. Properness of a given pair is an open condition, so it requires no additional *first-order tangent equation* at a proper point; nevertheless finding an honest arc and remaining in the desired stratum require more than a first-order solution.

No claim follows that every tangent integrates. The Hom space describes first-order motion of T; the actual Hilbert/Quot deformation can have higher obstructions. Likewise (3) is a first-order global coefficient compatibility map, not the complete obstruction theory for a tower of thickenings.

## 3. The primary component cannot absorb mass in a flat fixed-polynomial motion

Here is a globally homogeneous control valid in every characteristic. In P3_[x:y:z:w] over A1_lambda set

    Y_lambda = V(x, y^m*(y-lambda*z)),  m>=1,
    L = V(x,y).

The coordinate quotient is free over k[lambda,z,w] on 1,y,...,y^m, since its relation is monic in y of degree m+1. Hence this is a flat projective family of proper (1,m+1) complete intersections. Every fiber has degree m+1 and the same full Hilbert polynomial.

For lambda nonzero, the ideal decomposes as

    (x,y^m) intersect (x,y-lambda*z),

because the two principal factors are coprime in k[y,z,w]. They need not be comaximal; their projective lines meet at [0:0:0:1]. The L-primary component has degree m, and the other line is a genuine attached residual component. At lambda=0 the entire fiber has ideal (x,y^(m+1)) and is supported on L, with generic length m+1.

Thus the primary component assigned fiber by fiber has degree m before specialization and m+1 at the special fiber. It cannot itself be a flat projective family over a connected base. In general, for a pure curve T supported on the fixed C, its degree is deg(C) times its generic length. A flat family of such T with fixed Hilbert polynomial fixes this leading coefficient and hence fixes the generic length.

This is a precise limitation of a proposed strategy: motion within one marked-thickening Hilbert stratum studies a fixed amount of mass on C. To study absorption, one can keep a fixed lower T and let the pair acquire an additional generic layer at the special point; one cannot assume that its *full primary component* continues flatly across the jump. The plane-line control is not a construction for the fixed rational quartic and gives no evidence that the analogous endpoint exists there.

## 4. Primary literature refreshed

The following authoritative sources were inspected on 2026-10-27:

- [Stacks, Remark 99.7.10, tag 0CZV](https://stacks.math.columbia.edu/tag/0CZV) identifies the choices of quotient lifts across a square-zero extension, once a lift exists, as a torsor under Hom(kernel, quotient tensor the square-zero ideal). Specialization to the constant lift gives the embedded tangent calculation used above. The fixed-incidence conditions in (1) were reconstructed directly rather than read into this general remark.
- [Stacks, Remark 99.7.9, tag 0CZU](https://stacks.math.columbia.edu/tag/0CZU) constructs an Ext1 obstruction to quotient lifting and distinguishes its vanishing from the later choice of a lift. This supports the caution about higher deformation theory; its general Ext1 obstruction is not identified with the more specific global coefficient map (3).
- [Stacks, Lemma 36.32.2, tag 0B9T](https://stacks.math.columbia.edu/tag/0B9T) gives local constancy of Euler characteristic for a finitely presented flat sheaf in a proper finitely presented family. Applying it to twists gives constancy of the Hilbert polynomial, the input needed in section 3.

These are standard deformation and flatness facts. The contribution proposed for the current research is their exact organization around moving lower embeddings and actual global pairs, without confusing that motion with an increase of primary multiplicity.

## 5. Outcome and limits

Claims (1)--(4), with the stated affine coefficient convention, pass this audit. The homogeneous family in section 3 independently verifies the nonflat-primary-component warning. No computation or inherited theorem replay was needed: the proofs are explicit ideal and exact-sequence calculations. Nothing here proves the obstruction map is nonzero or zero for the fixed quartic in an uncomputed stratum, proves a tangent integrates, gives a uniform degree bound, or settles characteristic-zero STCI.
