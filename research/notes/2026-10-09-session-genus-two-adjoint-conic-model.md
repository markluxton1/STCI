# The genus-two adjoint conic model and its bounded exceptional locus

Date: 2026-10-09. Owner: `delpezzo_d5_torsion_filter`.
Status: **PROVED HERE**. Sections 1--2 are independently accepted in
the [adjoint audit](2026-10-09-session-genus-two-adjoint-independent-audit.md)
and its [degree-one counteraudit](2026-10-09-session-genus-two-degree-one-counteraudit.md).
Sections 4--5 and 7 are independently accepted in the
[null-curve and mate-strata audit](2026-10-09-session-genus-two-nullcurve-mate-independent-audit.md).
Sections 3, 6 and 8 are supplied for a final bounded audit. This is a
structural reduction; neither the genus-two mate lane nor the
unrestricted STCI problem is excluded here.

Work over an algebraically closed field of characteristic zero. Let
X in P3 be an integral nonnormal quartic containing a smooth rational
degree-four curve C0. Let nu:S->X be its finite normalization,
sigma:M->S its minimal smooth resolution, H=nu*O_X(1), and L=sigma*H.
Assume normalization sectional genus pi=2.

The accepted [rationality theorem](2026-10-09-session-nonrational-quartic-normalizations.md)
gives rational M, without a mate hypothesis. The basic data are

    L nef, big and globally generated,
    L^2=4,       K_M.L=-2,       chi(O_M)=1,
    h0(M,L)=h0(S,H)=4.

The four actual ambient sections span this complete space; the
complete |L| morphism has the actual quartic X as its image and is
birational. An integral prime E has L.E=0 exactly when it is
sigma-exceptional. Minimality forbids an exceptional smooth rational
(-1) curve, but does not forbid (-1) curves with positive L-degree.
No conductor classification or ADE hypothesis is assumed.

## 1. The adjoint is nef and has square zero

Set A=K_M+L. Nef-big Kawamata--Viehweg vanishing and Riemann--Roch give

    h0(M,A)=1+(A.L)/2=2,       A.L=2.

If A.E<0 for an integral prime E, effectiveness makes E a fixed
component and forces E^2<0. Adjunction gives

    K_M.E=2p_a(E)-2-E^2.

This is nonnegative for p_a(E)>=1 or E^2<=-2. The remaining case is
a smooth rational (-1) curve, and minimality then gives L.E>=1,
so A.E=-1+L.E>=0. Hence A is nef. Its square is

    A^2=K_M^2,

and Hodge index against L gives 0<=A^2<=1.

If A^2=1, the class T=L+2K_M is numerically zero: T.L=0 and T^2=0,
and L-perp is negative definite. A numerically trivial divisor N
on this rational M is linearly trivial by the following useful
direct argument. Riemann--Roch gives chi(N)=1; Serre duality gives
h2(N)=h0(K_M-N)=0 because (K_M-N).L=-2. Thus N has a nonzero section.
Its zero divisor is effective and numerically zero, hence zero by
intersection with an ample class. In particular T~0 and L~2A.

Two independent sections u,v of A give three independent square
sections u^2,uv,v^2 of L. Independence follows from the nonconstant
rational function u/v. Completing them to a basis of h0(L)=4 puts
the |L| image in the nonzero quadric X0 X2-X1^2=0, contrary to its
being an integral quartic hypersurface. Therefore

    A^2=K_M^2=0.

The independent degree-one counteraudit verifies this exact
contradiction. An anticanonical classification theorem is not needed.

## 2. The entire adjoint system is a rational pencil without base points

Write |A|=|P|+D, where D is fixed and |P| has no fixed curve.
Then h0(P)=2. Nefness of A gives A.P=A.D=0. Two general members of
|P| have no common curve, hence P^2>=0. Subtracting the appropriate
rational multiple of A makes P orthogonal to L; Hodge index then
gives P^2<=0. Thus P^2=0 and P is numerically proportional to A.
Any base point would give a positive local intersection multiplicity
between two general members, so |P| has no base points.

The associated map to P1 has connected fibers. Its Stein base is P1
because M is rational. If its finite map to the original target had
degree d, then h0(P)=h0(P1,O(d))=d+1, so d=1. A general fiber F is
smooth and integral. Since K_M=A-L and A.P=0,

    2g(F)-2=K_M.P=-L.P<0.

Therefore F is P1 and L.P=2. Comparing with L.A=2 shows P is
numerically equivalent to A; the effective fixed part D is
numerically zero and is therefore zero. Consequently

    f:=K_M+L,       |f| is a basepoint-free connected rational pencil,
    f^2=0,         L.f=2,       K_M.f=-2.

The general fiber is mapped by the actual complete |L| isomorphically
onto a smooth plane conic in X. Its degree-two line bundle uses at
most three independent sections. A two-dimensional subspace would
give a degree-two map onto a line, contradicting birationality on
the general fiber. Thus all three sections of O_P1(2) occur.

This fibration is on M. It need not descend as a morphism to S,
because some curves contracted by sigma can be horizontal for it.

## 3. A marked eight-blowup ruled model

Contract vertical (-1) curves until the smooth rational fibration
is a relatively minimal ruled surface F_n. A smooth relatively
minimal P1 fibration over P1 is a P1 bundle, so this is a Hirzebruch
surface. The resulting factorization M->F_n consists of point
blowups, including possibly infinitely near centers. Since K_M^2=0
and K_Fn^2=8, there are exactly eight point blowups.

Write C_min^2=-n and C_min.f=1 on F_n, and use total transforms
e1,...,e8 for the blowup classes. Every contracted vertical (-1)
curve E has f.E=0, K.E=-1, and therefore

    L.E=(f-K).E=1.

At each contraction the pushed-down L remains nef; intersecting
strict transforms proves this directly, as in the rationality note.
The canonical blowup formula therefore gives the actual marked class

    L=2C_min+(n+3)f-sum_{i=1}^8 e_i.

On F_n the pushed-down L has intersection 3-n with C_min. Nefness
forces

    0<=n<=3.

All multiplicities are one in this total-transform marking. This
does not mean that all eight centers are distinct points of F_n.
For a direct numerical control, the pushed-down class has square
twelve and canonical intersection minus ten; subtracting the eight
blowup classes gives L^2=4 and K_M.L=-2 as required.

This model uses only the adjoint fibration. It does not assert that
the normalization is itself the strict transform of X in a blowup
of an ambient line, or that the original conductor is a reduced line.

## 4. All contracted prime curves have tightly bounded types

Let E be any integral sigma-exceptional prime. Put

    d=f.E=K_M.E>=0,
    Q=K_M+L/2.

The inequality d>=0 follows from nefness of f. The projection Q
lies in L-perp and has square -1. Since L-perp is negative definite,
Cauchy--Schwarz there gives

    d^2=(Q.E)^2<=-E^2.

Adjunction gives

    -E^2=d+2-2p_a(E),
    d^2<=d+2-2p_a(E).

If d=0, the negative square forces p_a(E)=0 and E^2=-2. Thus every
vertical contracted prime is a smooth rational (-2) curve.

If d>0, the inequality leaves only d=1 or d=2. For d=1 the map
E->P1 induced by f has degree one. It is finite birational, and the
target P1 is normal, so it is an isomorphism. Hence E is a smooth
rational section and E^2=-3.

For d=2 the inequality forces p_a(E)=0 and E^2=-4. Equality in
Cauchy--Schwarz gives E numerically equivalent to -2Q=-2K_M-L.
The numerical-to-linear argument of section 1 gives

    E~ -2K_M-L,       L~2f+E.

Multiplying three independent sections u^2,uv,v^2 of 2f by the
nonzero section of E gives three independent sections of L with
the same quadric relation. This contradicts the actual quartic
image. Thus the (-4) bisection cannot occur.

**Conclusion.** Every contracted prime is either a vertical smooth
(-2) curve or a horizontal smooth (-3) section. No positive-genus
exceptional prime has been omitted by an ADE assumption.

## 5. There are at most two horizontal curves, and they are disjoint

For two distinct horizontal (-3) sections E1,E2 put t=E1.E2>=0.
For T=E1+E2, one has K_M.T=2 and T^2=-6+2t. Cauchy--Schwarz on
L-perp gives 4<=6-2t, so t<=1.

If t=1, equality gives T numerically equivalent to -2Q, hence
T~-2K_M-L and L~2f+T. The effective divisor T gives the same
three-section quadric contradiction as section 4. Therefore t=0:
two such sections are disjoint.

Suppose three such curves existed. For their sum T, pairwise
disjointness gives T^2=-9 and K_M.T=3. Cauchy equality gives

    T equivalent to -3Q,       2T~-6K_M-3L.

The upgrade to the displayed linear equivalence uses the same
numerically-trivial-divisor argument. It implies L=2B in Pic(M),
with the explicit integral class B=-3K_M-T-L. Then

    B^2=1,       K_M.B=-1.

Riemann--Roch gives chi(B)=2. Also h2(B)=h0(K_M-B)=0 because its
L-degree is negative. Hence h0(B)>=2, and the square sections of
two independent sections of B again put the |L| image in a quadric.
This contradiction proves that there are at most two horizontal
(-3) sections.

They can still meet vertical (-2) curves in their exceptional fiber.
No claim that all singularities of S are ADE is made.

## 6. The vertical root lattice is the explicit D8 lattice

In the marked ruled model of section 3, a Picard class orthogonal
to both f and L has the form

    v=b f-sum_i d_i e_i,       2b=sum_i d_i.

Its square is -sum_i d_i^2. Thus the integral lattice

    f-perp intersect L-perp

is the negative D8 lattice: integer vectors (d1,...,d8) with even
coordinate sum. Its roots are the 112 vectors +/-u_i+/-u_j, bound
geometrically to

    +/- (e_i-e_j),       +/- (f-e_i-e_j).

Every vertical contracted (-2) curve is one of these roots. The
negative definite lattice of all vertical exceptional primes is
therefore an embedded root subsystem of D8, and its total rank is
at most eight. The signed-coordinate argument from the
[D5 filter](2026-10-09-session-delpezzo-D5-torsion-filter.md) applies
to root sublattices here as well: coordinate-connected components
are A or D, including D2=2A1 and D3=A3. This is an exact lattice
identification, not a claim that every embedded D8 configuration
is geometrically realized in the given conic model.

If there are no horizontal exceptional curves, every exceptional
prime is (-2) and the canonical divisor is crepant on the minimal
resolution; the standard Du Val criterion then gives ADE singularities
of S. With horizontal sections present that inference is unavailable.

## 7. A mate retains two correction strata, not just the ADE one

Now add a hypothetical mate. Its full support supplies a smooth
embedded c=P1 on S and an effective rational exceptional correction Z,

    c# + Z equivalent to L,       Z=sum_i a_i E_i,       a_i>=0.

The class Z=L-c# is integral, although its coefficients in the
exceptional basis may be fractional. Put

    q=-Z^2>0,       lambda=K_M.Z.

The general adjunction identity from the sectional-genus record is

    q+lambda=2pi=4.

Since K_M.E is zero on every vertical prime and one on each
horizontal (-3) section,

    lambda=sum of the horizontal correction coefficients.

It is a nonnegative integer, because K_M and Z are integral classes.
Cauchy--Schwarz with Q in section 4 gives

    lambda^2<=q=4-lambda.

Therefore exactly two necessary numerical strata remain:

| lambda | q | c#^2 | f.c# | Type of lifted rational curve on M |
| --- | --- | --- | --- | --- |
| 0 | 4 | 0 | 2 | Bisection |
| 1 | 3 | 1 | 1 | Section |

The lambda=1 stratum must not be discarded by setting Z^2=-4 in
advance. That equality presupposes K_M.Z=0, which is automatic in
the ADE lane but has not been established in the non-ADE lane.
An attempted audit shortcut making that substitution was corrected
before acceptance. Effectiveness alone permits lambda=1.

In the lambda=0 stratum, Z has zero coefficient on all horizontal
sections. It is supported on vertical (-2) components and belongs
to D8. For a horizontal section E, positivity gives Z.E>=0 while
the mate gives Z.E=-c#.E<=0. Consequently Z.E=c#.E=0. Thus both
the correction support and c# avoid the horizontal sections in this
stratum. This avoidance is conditional on lambda=0.

As in the D5 proof, Z is not in the integral exceptional lattice R:
otherwise c~H downstairs would be Cartier, so embedded smoothness
forces c to avoid Sing(S), and negative definiteness then forces
Z=0. Under a degree-b mate, bZ belongs to R. Determining which
D8 root sublattices and exceptional configurations can contain the
required missing norm-four or norm-three class remains open here.

## 8. The two strata have concrete moving systems

In the lambda=0 stratum, the smooth P1 c# has square zero. The
restriction sequence

    0 -> O_M -> O_M(c#) -> O_c#(c#) -> 0

and H1(O_M)=0 give h0(c#)=2. The system is basepoint free: its
restriction to c# is O_P1, and the canonical section is nonzero
away from c#. Thus c# is a fiber of a second rational pencil.
The two rational pencils have fiber intersection f.c#=2.

In the lambda=1 stratum, c#^2=1. The same sequence restricts to
O_P1(1), gives h0(c#)=3, and proves basepoint freeness. The complete
|c#| map has two-dimensional image in P2 and generic degree one,
because c#^2=1. It is therefore a birational morphism M->P2.
As K_M^2=0, it consists of nine point blowups.

Mark c# by the pullback h of a line and the nine total exceptional
classes e0,...,e8. The nef class L has the form

    L=4h-sum_{i=0}^8 m_i e_i,       m_i>=0.

Nefness of its successive pushdowns ensures these nonnegative
integer multiplicities, including infinitely near centers. The
two intersection identities give

    sum_i m_i=10,       sum_i m_i^2=12,
    sum_i m_i(m_i-1)=2.

Exactly one m_i is two and the other eight are one. Renaming the
double center e0, the actual marked classes are

    L=4h-2e0-sum_{i=1}^8 e_i,
    f=K_M+L=h-e0,
    c#=h,
    Z=L-c#=3h-2e0-sum_{i=1}^8 e_i.

This is a stronger marked reduction for the retained lambda=1
mate stratum. It does not show that the effective rational
exceptional representative of Z has integral coefficients, nor
that it descends to a mate on X. In particular the smooth lifted
curve and its singleton normalization fibers remain necessary
conditions in addition to these marked identities.

## 9. Relationship with a double-line blowup, retaining its hypotheses

For comparison only, if an actual carrier X has a line ell of
generic multiplicity two, put B=Bl_ell(P3), with pulled-back
hyperplane H_B and exceptional divisor E_B. Its strict transform is

    T~4H_B-2E_B=2H_B+2f_B,       f_B=H_B-E_B.

When T is normal, adjunction gives K_T=-E_B|T. The exceptional
intersection is a (2,2) scheme in E_B=P1 times P1, with arithmetic
genus one. The numerical identities are H_B^2|T=4,
H_B.E_B|T=2, and (E_B|T)^2=0. This is consistent with the adjoint
model, but it is a conditional ambient realization.

[Dolgachev, Monoidal and submonoidal surfaces, and Cremona transformations](https://sites.lsa.umich.edu/idolga-new/wp-content/uploads/sites/1467/2024/08/monoidal.pdf),
section 3, explicitly imposes conditions before identifying the
normalization with this strict transform. Definition 3.6 retains
that identification, discriminant multiplicity bounds and smoothness
of the small discriminant; Proposition 3.7 gives the resulting
normalization geometry. Its nondegenerate model must not be used
as coverage of arbitrary genus-two normalizations. Sections 1--8
above do not use those extra hypotheses or an asserted reduced
downstairs conductor line.

## 10. Continuation-ready boundary

The intrinsic adjoint argument produces a connected rational conic
fibration, K_M^2=0, an explicit eight-blowup ruled marking, and a
bounded exceptional locus: vertical D8 roots and at most two
disjoint horizontal (-3) sections. For a mate it retains exactly
the two numerical correction strata of section 7, and section 8
gives a concrete marked plane model in the non-ADE stratum.

The next finite task is to classify smooth-lift correction vectors
in these exceptional configurations. Downstairs smoothness is stronger
than smoothness of c# alone; for example meeting multiple exceptional
branches or tangency to an exceptional prime may prevent a uniformizer
of c from descending. A necessary local condition must be proved
before it is used as a lattice exhaustion. The actual conductor,
full inverse-image support, and descent of sections to the original
quartic remain separate obligations.

No exhaustive genus-two mate exclusion, no conductor purity theorem,
and no universal STCI conclusion is claimed. No canonical frontier
file has been edited by this owner.
