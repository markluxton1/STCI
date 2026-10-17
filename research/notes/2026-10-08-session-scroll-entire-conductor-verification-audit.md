# Verification audit: all actual conductors on smooth rational quartic scrolls

Date: proof audited 2026-10-08; evidence record completed at the 2026-10-09 continuation. Auditor: `verification`. Status: **PROVED HERE**, independently accepted all-mate exclusion for the specified carrier class. No canonical frontier file is edited.

## Statement and antecedents

Let X be an integral quartic in P3 over an algebraically closed field of characteristic zero. Suppose its finite normalization is a smooth rational quartic scroll S with polarized class

    F0: H=C+2f, D~-K_S=2C+2f;
    F2: H=C_min+3f, D~-K_S=2C_min+4f.

Here D is the entire Cartier conductor divisor and Gamma is the entire downstairs conductor scheme. Then X has no mate of any positive degree presenting the fixed smooth rational quartic C0=[s^4:s^3t:st^3:t^4] as its set-theoretic intersection.

This audit uses the independently established conductor antecedents: Gamma is pure ACM with polynomial 3m+1, its ideal has the linear Hilbert--Burch resolution with three quadratic generators and two cubic syzygies, and

    0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0.

A mate supplies a single smooth c~H, nu|c an isomorphism to C0, full singleton normalization fibers over C0, and the entire identity nu^*G=lambda f^n with div(f)=c. The reduction retains all conductor multiplicities. Every proper conductor prime E is smooth rational by H1(O_E)=H0(O_S(E-D))*=0. Since D has H-degree six while Gamma has degree three, its conductor prime configurations below are proper, rather than D itself.

The all-reduced-conductor theorem and the independently audited [all-locally-Gorenstein theorem](2026-10-08-session-scroll-gorenstein-independent-audit.md) were accepted separately. This note checks the remaining nonreduced nongorenstein schemes directly, rather than invoking a classification of all quartic surfaces or the alternative transverse-completion argument in section 17 of the owner note.

## 1. Whole nongorenstein ACM cubic classification

For the 3-by-2 linear Hilbert--Burch matrix M, rank one at a point gives a unit entry and a local codimension-two complete intersection. Rank zero gives a minimal local resolution with last rank two and a canonical module with two generators. Thus the nongorenstein locus is exactly the common zero locus of the linear entries.

Let W be the span of the entries. Its dimension is at least two because the minors have height two. If dim W=4 there is no projective rank-zero locus, so the entire curve is locally Gorenstein and already excluded. If dim W=3, coordinates give W=<x,y,z> and the ideal is the cone, with vertex the w-point, over a length-three scheme Z in P2. The homogeneous ring k[x,y,z]/J is dimension one Cohen--Macaulay, hence J is saturated. Its Hilbert series is (1+2t)/(1-t), and J has no linear element. Saturation therefore makes Z noncollinear; merely knowing h0(O_Z(1))=3 would not suffice.

A length-three scheme on a smooth surface has three distinct points, one double point plus a distinct point, a curvilinear length-three point, or a length-three point with two-dimensional square-zero maximal ideal. Noncollinearity respectively means the points are noncollinear, the third point misses the double point's tangent line, or the curvilinear point has nonzero second-order departure from its tangent line. Projective coordinate changes and scaling give the four cone ideals

    (xy,xz,yz), (y^2,xy,xz), (x^2,xy,y^2-xz), (x^2,xy,y^2).

The first is reduced and already excluded. For the last case only two linear variables are needed. Conversely, if dim W=2, the three independent quadratic minors span Sym^2(W), giving exactly the final ideal. Independence follows from the Hilbert--Burch resolution and its three minimal quadratic generators. These arguments exhaust the whole nongorenstein ACM cubic schemes over the stated field.

## 2. Curvilinear triple line: divisible-by-three obstruction

At its generic point, A=K[epsilon]/epsilon^3 and omega_A is free of rank one. The canonical exact sequence therefore makes B free of rank two over A. B has K-length six and multiplication by epsilon has rank four.

Write a generic conductor factor as K_i[t]/t^a, r=[K_i:K], and k=ord_t(epsilon), allowing k=a if the image is zero. Its K-length is ar and its multiplication rank is r(a-k). Since epsilon^3=0, a<=3k. The sum of the ranks reaches the upper bound (2/3)*6=4, so equality holds in every factor: a=3k. Every actual prime multiplicity of D is divisible by three. Then the divisor class of D is divisible by three in the torsion-free Picard group, contrary to its C-coefficient two. This excludes the actual curvilinear triple-line conductor before imposing a mate.

No reduced-cover interpretation or global flatness at its nongorenstein vertex is used.

## 3. Fat triple line: the canonical-module and annihilator steps

For the fat triple line, A=K+N with dim_K N=2 and N^2=0. In omega_A=Hom_K(A,K), multiplication by N has image the one-dimensional span of 1*. Let T=NB. The canonical exact sequence gives dim_K B=6, and the image of T in B/A is N omega_A, of dimension one.

The ideal T contains N. Since T^2=0, T intersect A contains no element with nonzero scalar part: such an element is a unit in A, hence a unit in B, contradicting square-zero. Thus T intersect A=N, and dim_K T=2+1=3.

B is a product of truncated DVR algebras over finite separable residue extensions of K. It is Frobenius over K: on K_i[t]/t^a the pairing takes the field trace of the coefficient of t^(a-1) in a product. It is nondegenerate, so every ideal T satisfies dim Ann_B(T)=dim B-dim T. Our T is square-zero and three-dimensional, hence

    T subset Ann_B(T), dim T=dim Ann_B(T)=3,
    T=Ann_B(T).

An ideal in a truncated DVR factor is (t^k), with annihilator (t^(a-k)). Equality forces a=2k separately in every factor. In particular no odd prime multiplicity or zero ideal factor is omitted. Every coefficient of the actual D is even, so

    D=2E, E~C+f on F0, E~C_min+2f on F2.

This Frobenius argument is applicable to B, which is a product of DVR quotients; it does not assert that the nongorenstein algebra A is Frobenius or that B is free of rank two over A.

## 4. Effective divisor and full-fiber exclusions for the fat line

A prime mapping to the support line with degree r has H-degree r. For r>=2 every point of c intersect that prime must be a totally ramified point, since the entire normalization fiber is a singleton. The ramification derivative annihilates its tangent, whereas nu|c is immersive, so c meets the prime transversely at each such point. There are consequently r distinct totally ramified points. Their contribution r(r-1) cannot exceed the Riemann--Hurwitz total 2r-2; r>=3 is impossible.

On F0 the effective class C+f is a prime of degree three or a horizontal C-prime plus one fiber. The prime is excluded above. In the split case, the degree-one fiber restriction of f has one zero on the common base line. Equality of the full descended n-th powers forces the zero divisor on the degree-two horizontal prime to be the pullback of that one zero. Singleton fibers make it one totally ramified point of multiplicity two, while immersion of c requires transverse intersection one. This is a contradiction.

On F2, any prime other than C_min has class a C_min+b f with b>=2a; fibers are individually prime only with class f. Thus C_min+2f is either a degree-three prime, C_min+F1+F2 for distinct fibers, or C_min+2F. The prime case is excluded by the ramification argument. The distinct fibers have proportional nonzero restrictions of f, because their n-th powers descend to the same line. Their equal zero on the base gives distinct points of c in one normalization fiber, impossible.

The remaining actual divisor is D=2C_min+4F. In its generic F-factor B_F=K[t]/t^4 the preceding self-annihilator computation gives NB_F=(t^2). Ambient coordinates normal to the support line have classes in N, so their actual pullbacks vanish to order at least two along F: the equality modulo the conductor (t^4) implies actual membership in (t^2). The longitudinal coordinate has nonzero derivative because F maps isomorphically to the line. Hence dnu has generic rank one on F. The [independent nonimmersion-prime lemma](2026-10-08-session-nonimmersion-prime-independent-audit.md) excludes the mate. This step verifies derivative rank from the actual generic algebra; multiplicity four alone would not do so.

## 5. Doubled line plus reduced line, including the nongorenstein vertex

At the thick line L, A=K[epsilon]/epsilon^2 is generically Gorenstein, so B is free of rank two there. Its length four and epsilon-rank two give the complete partitions

    (a,r)=(4,1), (2,2), or (2,1)+(2,1),

with epsilon order a/2 in every factor. In the (4,1) factor, normal coordinates to L belong to the nilradical (epsilon) and therefore have actual valuation at least two on its prime. The nonimmersion lemma excludes this case under a mate.

At the reduced line M, total generic length two gives

    (a,r)=(2,1), (1,2), or (1,1)+(1,1).

In the doubled-prime case (2,1), normal coordinates to M vanish in A=K and thus belong to the actual conductor (t^2). This also gives generic rank at most one and is excluded. Hence all prime multiplicities over M are one under a mate.

On F0 the only H-degree-two prime is a horizontal C-prime and the only degree-one primes are fibers. The split thick-line partition consumes four fiber multiplicities, contrary to D~2C+2f. Thus L has 2C and the residual 2f over M must be two distinct multiplicity-one fibers. A degree-two prime cannot have fiber class, and a doubled fiber is already excluded. Their disjoint paired zeros contradict singleton fibers.

On F2 there is no degree-two prime. The thick-line split is either 2C_min+2F or 2F1+2F2. The first leaves class 2f over M, again forcing the excluded disjoint fiber pair. The second already has disjoint paired zeros over L; alternatively its residual 2C_min over M cannot be a degree-two prime, two distinct primes in the unique C_min class, or the excluded doubled prime. This exhausts the actual classes.

Every step takes place at the actual generic Artin scheme or on the smooth normalization. It does not extend a deck involution through the nongorenstein vertex, invoke flatness there, or assume a scheme-theoretically reduced conductor.

## Audit decision and limits

The nongorenstein ACM classification, the generic canonical modules, the rank equalities, Frobenius annihilator argument, effective divisor exhaustion, full-fiber contradictions, and actual-coordinate differential conclusion all pass independent verification. Together with the accepted reduced and locally Gorenstein cases they prove the stated exclusion for every smooth rational quartic-scroll normalization.

The theorem is for carriers of this fixed C0 and this polarized normalization class. It does not prove that every integral nonnormal quartic has such a normalization, does not include singular normalizations, and does not resolve the global STCI problem. The supporting exact script checks concrete normal forms and finite ranks; its PASS is not the reason the complete geometric theorem is accepted.

Source and execution provenance are preserved in `research/validation/2026-10-09-scroll-entire-audit/audit-manifest.json`. The independent supporting generic-length source retains explicit countermodels showing that nonreduced Gamma need not have zero discriminant and a deck involution need not preserve every prime.
