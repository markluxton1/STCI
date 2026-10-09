# Degenerate actual conductors on smooth quartic scroll normalizations

Date: 2026-10-08. Status: **PROVED all-mate exclusion for every reduced
actual downstairs conductor on a smooth rational quartic-scroll
normalization**, including every upstairs conductor scheme. The
nonreduced downstairs boundary remains open. No canonical frontier
file is edited here.

## 1. Actual scheme and normalization hypotheses

Let X be an integral quartic hypersurface over an algebraically closed
field of characteristic zero. Suppose its finite normalization
nu:S->X is a smooth rational quartic scroll, with H=nu*O_X(1). Let I be
the actual conductor, Gamma=V(I) on X, and D=V(I O_S) on S. In particular
D is the entire conductor Cartier divisor, not its reduced support.
Finite absolute duality gives

    I=nu_*omega_S, D~-K_S, H.D=6.

The [applicability note](2026-10-08-session-scroll-conductor-applicability.md)
proves Gamma is pure Cohen--Macaulay with Hilbert polynomial 3m+1.
The [Oct8 checkpoint](2026-10-08-session-checkpoint.md) strengthens this
to an arithmetically Cohen--Macaulay cubic with the Hilbert--Burch
resolution

    0 -> O_P3(-3)^2 -> O_P3(-2)^3 -> J_Gamma -> 0.

The resolution retains every nonreduced structure. The matrix is a
2 by 3 matrix of linear forms; its three maximal minors are the entire
ideal of Gamma. A reduced reducible Gamma is either a smooth conic
meeting a line once, three noncoplanar lines forming a chain, or three
noncoplanar concurrent lines. This support list alone does not classify
the entire conductor morphism. In particular the concurrent case need
not be Gorenstein or admit a finite flat double-cover description.

## 2. Generic rank two follows without global flatness

There is an exact sequence of O_Gamma-modules

    0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0,
    p=nu|D.

Here is a local derivation that does not assume p flat. Write A for a
two-dimensional Gorenstein local ring of X, B for its finite smooth
normalization, and Q=B/A. A system of parameters is B-regular, so B is
maximal Cohen--Macaulay over A. The depth lemma shows Q is a
Cohen--Macaulay module of dimension one, unless it vanishes. Applying
Hom_A(-,A) to 0->A->B->Q->0 gives

    Ext_A^1(Q,A)=A/I,

because Hom_A(B,A)=I, Hom_A(Q,A)=0, and Ext_A^1(B,A)=0.
Canonical-module biduality for Cohen--Macaulay modules of codimension
one therefore gives Q=Ext_A^1(A/I,A)=omega_Gamma. Modding the original
normalization sequence by their common conductor ideal I gives the
displayed exact sequence. The canonical-module identifications are
relative to omega_X=O_X.

Consequently, when Gamma is reduced, at its generic points the total
conductor cover has degree two: the canonical module there is a
one-dimensional vector space over the corresponding function field.
This does not imply flatness over a nongorenstein closed point of
Gamma, and no such inference is used below.

## 3. The mate imposes smooth hyperplane-section and full-fiber data

Suppose X has a mate G of positive degree b with

    (X intersect V(G))_red=C0,
    C0=[s^4:s^3t:st^3:t^4].

Gamma has degree three, so C0 is generically in the normal locus. The
full pullback support argument in the
[compression note](2026-10-08-session-irreducible-conductor-compression.md)
gives a unique c subset S isomorphic to C0, with

    (nu^-1(C0))_red=c, div(nu*G)=b c, c~H.

Every fiber over C0 consists of exactly one point. If f is a section
of O_S(H) with divisor c, then nu*G=lambda f^b with lambda constant.
In particular the restrictions of f^b to all conductor branches
descend through the actual p:D->Gamma. Finally nu|c is an isomorphism,
so its differential along c never vanishes. This differential
condition remains valid at a point where several conductor components
meet on S.

## 4. Components of a connected reduced anticanonical conductor

Now suppose D is reduced. It is connected: from
0->O_S(K_S)->O_S->O_D->0 and H^1(O_S(K_S))=0,

    H^0(O_D)=k.

If D is reducible and E is one of its irreducible components, adjunction
gives

    E.(D-E)=(-K_S-E).E=2-2 p_a(E).

The left side is nonnegative, and is positive by connectedness.
Therefore p_a(E)=0 and E.(D-E)=2. Thus every component E is a smooth
rational curve. This argument uses the arithmetic genus of the actual
component, so it also excludes singular rational components here.

## 5. Reduced conic-plus-line conductor: every mate degree is excluded

**Theorem.** Retain the normalization hypotheses, and suppose Gamma is
reduced with a smooth conic component and a line component, while D is
reduced. Then X cannot be a carrier of a set-theoretic complete
intersection presenting C0, in any positive mate degree.

The generic rank-two result of section 2 leaves two possibilities over
the conic Q.

### One irreducible component over Q

There is a single conductor component E mapping to Q with degree two.
Since D has components above the line as well, section 4 shows
E is smooth rational. A separable degree-two map P1->P1 has exactly
two distinct simple ramification points in characteristic zero.

If a point P of E belongs to c, the singleton-fiber condition forces
p^-1(p(P)) on E to contain just P. Hence P is a ramification point of
E->Q. The differential of nu restricted to T_P E vanishes there,
because nu|E factors through this ramified map and the embedded conic.
Since nu|c is an immersion, T_P c differs from T_P E. Their local
intersection multiplicity is therefore one, even if other conductor
components meet at P. It follows that

    c.E <= 2.

But c~H and H|E=p*O_Q(1), giving

    c.E=H.E=2 deg(Q)=4,

a contradiction.

### Two components over Q

There are two components E,E', each mapping to Q with degree one. They
are smooth rational and their finite degree-one maps to the smooth
conic are isomorphisms. Identify their restricted hyperplane bundles
with O_Q(1). The mate relation gives

    (f|E')^b=(f|E)^b,

so f|E'=zeta f|E for a constant b-th root of unity zeta. Neither
restriction vanishes identically, since its image is the conic rather
than C0. Every zero on E must lie in E intersect E', because the same
zero occurs at the paired point on E', and a fiber over C0 is a
singleton. At such a mutual point both restrictions have the same
order a, since the maps to Q are isomorphisms.

If their local contact multiplicity is m and a>m, smoothness of c is
impossible. Indeed write E:w=0 and E':w=u(t)t^m, u(0)!=0. The first
restriction has order greater than m, so f_t(0)=0 and smoothness of c
gives f_w(0)!=0. Taylor subtraction then makes

    f(t,u(t)t^m)-f(t,0)

have order exactly m, whereas both restrictions have order greater
than m. Thus a<=m. Summing all zeros gives

    2=H.E=c.E <= E.E' <= E.(D-E)=2.

Equality forces E to have no intersection with any other component of
D. The same holds for E'. Thus E union E' is a connected component of
D, disjoint from the nonempty conductor above the line, contradicting
section 4. This proves the theorem.

The proof requires neither a global deck involution nor ordinary pinch
points. In particular it includes conductor triple points, where an
earlier proposed eigenvalue-propagation argument was insufficient.

## 6. Failed extension and a local countermodel

It is unsafe to assume that a paired line component's attachment to
the remaining conductor is a different point from its mutual
intersection with its paired component. For example, over the nodal
base R=k[[x,y]]/(xy), the rank-two algebra

    R[eta]/(eta^2-x-y^2)

is the planar reduced curve

    y(eta-y)(eta+y)=0.

Its three smooth branches meet at one point. The two exchanged
branches eta=+/-y map to one base component; the stable branch y=0
maps by x=eta^2 to the other. A smooth section
f=alpha*y+beta*eta has an arbitrary ratio
(alpha-beta)/(alpha+beta) on the exchanged branches, and vanishes at
the common attachment point. Suitable root-of-unity ratios, together
with an even power on the stable branch, give local descended powers.
Thus reducedness, singleton fibers, and local smoothness do not alone
force equal branch eigenvalues. This model does not assert a global
quartic realization, and does not contradict section 5: its global
conic component has degree four on its degree-two cover, which supplies
the extra intersection contradiction there.

## 7. The conic-plus-line theorem includes every upstairs scheme

The reduced-D hypothesis of section 5 can be removed. This extension
was proposed by the normal-global-adversarial agent and independently
checked by the present author and root. Its separate written proof is
the [all-D independent audit](2026-10-08-session-scroll-conic-line-independent-audit.md).

For every proper prime E<D, even when D is nonreduced, the sequence
0->O_S(-E)->O_S->O_E->0 gives

    H^1(O_E)=H^2(O_S(-E))=H^0(O_S(E-D))*=0.

The final vanishing holds because E-D is the negative of a nonzero
effective divisor on the projective integral S. Thus every proper
conductor prime is a smooth rational curve, and adjunction still gives
E.(D-E)=2, with all residual multiplicities retained.

Over the conic, the generic rank-two alternatives are:

* one prime E of multiplicity one and covering degree two;
* two primes E,E' of multiplicity one and covering degree one;
* one prime E of multiplicity two and covering degree one.

The first two cases are excluded by section 5 verbatim, allowing a
nonreduced remainder of D. The remaining doubled-conic case has H.E=2.
Write the two scroll polarizations as

    F0: H=C+2f, C^2=f^2=0, C.f=1;
    F2: H=C_min+3f, C_min^2=-2, C_min.f=1.

On F2 there is no prime of H-degree two. A prime other than C_min has
class a C_min+b f with a>=0, b>=2a. For a=0 a prime is a single fiber,
of degree one; for a>=1 its degree a+b is at least three. On F0, a
prime of degree two must be C-horizontal: its class is C. Indeed a
prime of class a C+b f has nonnegative a,b, H-degree 2a+b, and a=0
gives a single fiber.

Therefore the doubled-conic case occurs only on F0 and has

    D=2E+2f.

The residual conductor is either two distinct fibers F1,F2 or one
doubled fiber 2F. If F1,F2 are distinct, the points E intersect F1 and
E intersect F2 are distinct and both map to the unique node of the
conic-plus-line conductor. But nu|E is an isomorphism to the conic,
which is impossible. Hence D=2(E+F).

The reduced conic-plus-line curve Gamma is nodal and Gorenstein.
The exact sequence of section 2 makes p_*O_D locally free of rank two
over Gamma, since its quotient omega_Gamma is invertible. Trace splits
this algebra as O_Gamma direct-sum L, for an invertible L, with a local
trace-zero generator eta satisfying eta^2=Delta. Over both generic
components the upstairs conductor is a doubled prime, so Delta
vanishes generically on both components. Reducedness of Gamma forces
Delta=0 everywhere.

Write f|D=a+eta b in this trace splitting. The section a is generically
nonzero on every base component, because c is not a conductor prime.
The descended-power equality gives

    n a^(n-1)b=0.

Characteristic zero and torsionfreeness of the invertible trace-free
summand imply b=0 globally. Thus f itself descends through the entire
conductor square to O_X(1), and then to an ambient hyperplane. That
hyperplane would contain C0, a contradiction.

This proves the conic-plus-line theorem for every upstairs conductor
scheme. If only its downstairs reduced support is initially known to
be a smooth conic plus a line meeting once, it suffices: the support
already has degree three, so the pure CM conductor with polynomial
3m+1 has generic multiplicity one everywhere and no finite-support
nilradical. Its actual scheme is consequently reduced.

## 8. Three-line conductors: complete finite reduction

The following extension was independently audited by root and the
normal-global-adversarial agent. Its proof uses the actual generic
ranks and scroll divisor classes, not an unproved flat-cover assertion
at the nongorenstein concurrent point.

Assume Gamma is reduced with three line components. The exact sequence
of section 2 implies generic degree two over each line. Every proper
conductor prime is smooth rational by section 7 and has H-degree at
most two.

On F0 the only such primes are horizontal C-curves, of H-degree two,
and fibers, of degree one. Since D~2C+2f, there must be two distinct
horizontal primes C1,C2, each occurring once and covering different
base lines with degree two. The remaining cover over the third line
is either 2F or F+F' for two distinct fibers. The latter is impossible
under a mate: restrictions of f to F,F' are proportional after their
degree-one identifications with the same base line, and therefore
their zeros give two distinct normalization points over a point of
C0. Thus

    D=C1+C2+2F.

Since nu|F is an isomorphism to its base line and C1 intersect F and
C2 intersect F are distinct points, the three base lines cannot be
concurrent. They form the reduced noncoplanar chain. This Gamma is
Gorenstein, so the exact sequence makes p finite flat of rank two.
The trace discriminant vanishes identically on the central base line,
because its inverse conductor is 2F. Thus over each of the two base
nodes the finite fiber is eta^2=0 and has just one point. Each C_i
therefore maps with ramification to its line at its intersection with
F.

For a degree-two map C_i=P1->P1 there are two simple ramification
points. The singleton and differential arguments of section 5 imply
all points of c intersect C_i are these points, with multiplicity one.
Since c.C_i=H.C_i=2, both ramification points occur. In particular c
passes through both distinct points C1 intersect F and C2 intersect F,
contradicting c.F=H.F=1.

On F2 the only primes of H-degree at most two are C_min and individual
fibers, each of degree one. The class D~2C_min+4f forces C_min with
multiplicity two, covering one base line with degree one. The remaining
four fiber multiplicities provide two degree-two covers of the other
two base lines. A pair of distinct fibers over the same line is
impossible under a mate by the same paired-zero argument. Hence

    D=2C_min+2F1+2F2,

where F1,F2 are distinct fibers mapping to different base lines.
Their distinct intersections with C_min, which maps isomorphically
to its base line, again force Gamma to be a chain. The trace
discriminant vanishes generically on every component and therefore
globally on this reduced Gamma. The nilpotent-power argument in
section 7 makes f descend to an impossible ambient hyperplane.

These two reductions exclude every reduced three-line conductor under
the smooth-scroll hypotheses.
The concurrent case is not silently treated as Gorenstein: it is
eliminated by the divisor/fiber reduction before using a trace algebra.

## 9. Combined all-reduced-conductor theorem

**Theorem.** Let X be an integral quartic over an algebraically closed
characteristic-zero field, whose normalization is a smooth rational
quartic scroll. If its actual entire downstairs conductor is reduced,
then X cannot be a carrier of a set-theoretic complete-intersection
presentation of C0, in any positive mate degree. No reducedness
assumption on the upstairs anticanonical conductor is made.

Indeed the ACM cubic classification leaves a smooth twisted cubic,
a smooth conic plus a line meeting once, or three lines in a
noncoplanar chain or concurrent configuration. The smooth twisted
cubic case is proved in the
[entire-conductor applicability theorem](2026-10-08-session-scroll-conductor-applicability.md).
Sections 5 and 7 cover the conic-plus-line case with every upstairs
scheme. Section 8 covers the three-line cases with every upstairs
scheme. The proof is a classification of the reduced ACM conductor
and actual prime divisors of D; no classification of all nonnormal
quartic normalizations is asserted.

## 10. Precise retained boundary

Nonreduced Gamma remains unresolved here. The pure CM/ACM cubic
statement must retain nilpotents and the entire Hilbert--Burch ideal.
No extension of the trace algebra or deck involution is asserted at a
nongorenstein cubic point.

An immediate application target is the unique principal e=1,d2=1
quartic at (p,r)=(8,1/2), whose Jacobian support is a plane conic that
splits into two lines. Its Jacobian scheme is not the conductor scheme.
In particular a degree-two reduced singular support does not satisfy
the conic-plus-line hypothesis above; the actual degree-three
conductor and normalization must be identified first.

Independent audit: the normal-global-adversarial agent separately
checked section 5, including the ramification differential at a
conductor triple point. The ACM and Hilbert--Burch calculation has its
own independent audit. These agreements are audits of the written
proof, not substitutes for its hypotheses or arguments.

## 11. Generic-Artin square compression for a Gorenstein conductor

This reduction is valid for a locally Gorenstein actual Gamma,
including nonreduced Gamma. The section 2 exact sequence then makes
p_*O_D locally free of rank two, with its global trace involution
sigma. Suppose sigma preserves every reduced prime of D. For a mate,
f is generically nonzero on every such prime, and

    (sigma(f)/f)^n=1

in its generic Artin ring. The characteristic-zero polynomial T^n-1
has only simple roots. Each ratio is therefore an actual constant
root of unity, with no nilpotent correction. Applying sigma twice at
the same prime gives that root's square equal to one. Thus f^2 is
sigma invariant at every generic associated point of D. Since D is
a Cartier Cohen--Macaulay divisor with no embedded associated points,
f^2 is invariant globally. The fixed algebra is O_Gamma, so the
entire conductor square descends f^2 to O_X(2), then to an ambient
quadric, contradicting the unique-quadric geometry of C0.

The hypothesis that sigma preserves the primes is substantive. When
sigma exchanges two primes, their generic ratios may be arbitrary
reciprocal roots of unity; applying sigma twice alone does not bound
their orders. The paired-zero arguments elsewhere in this note are
used to handle exactly that exception.

## 12. Accepted all-Gorenstein-conductor extension

The following finite reduction has a completed
[independent audit](2026-10-08-session-scroll-gorenstein-independent-audit.md).
It extends section 9 from reduced Gamma to every locally Gorenstein
actual Gamma, retaining arbitrary D. It does not claim a locally
Gorenstein property for every ACM cubic.

A nonreduced pure degree-three Gamma has support either one line
with multiplicity three, or two lines with multiplicities two and one.
Its connectedness forces the two lines to meet. If Gamma were a
Gorenstein triple line, omega_Gamma would be invertible with

    deg(omega_Gamma)=2p_a(Gamma)-2=-2.

For any invertible sheaf M on a pure triple line, devissage through
the reduced line gives

    chi(M)-chi(O_Gamma)=3 deg(M|L).

Taking M=omega_Gamma makes -2 divisible by three, impossible. Thus
a nonreduced locally Gorenstein cubic has generic multiplicities
two on a line L and one on a different line M.

At the generic point of L, the conductor algebra is a free rank-two
algebra over K[epsilon]/(epsilon^2), K=k(L). Its total K-length is
four, and multiplication by epsilon has rank two. Each upstairs
generic factor is a DVR quotient t^a with residue extension degree r.
If epsilon has order k there, epsilon^2=0 gives k>=a/2. The total
rank equality forces k=a/2 in every factor. Hence a is even and the
only partitions of the upstairs total length are

    (a,r)=(4,1), (2,2), or (2,1)+(2,1).

This uses actual generic nilpotent lengths, rather than interpreting
the reduced upstairs support as a rank-two cover. Above M the usual
length-two alternatives apply.

On F0, the generic (4,1) alternative would require a degree-one
fiber with multiplicity four, contrary to D~2C+2f. The split
(2,1)+(2,1) alternative would likewise require four fiber
multiplicities and is impossible. The (2,2) alternative is 2E with
E a horizontal C-prime. The residual class is 2f over M. If it is
two distinct fibers, their disjoint paired zeros exclude a mate.
Otherwise D=2E+2F. The trace involution preserves both reduced
primes, so section 11 excludes every mate.

On F2 there is no degree-two prime. For (4,1), D=4F+2C_min, and the
trace involution preserves both primes, so section 11 applies.
For (2,1)+(2,1), the degree-one pair is either C_min and a fiber F,
or two distinct fibers F1,F2. In the latter case disjoint paired
zeros exclude a mate. In the former case the residual class 2f over
M is a doubled fiber or a pair of distinct fibers. Sigma exchanges
C_min and F and permutes the remaining fibers. But C_min meets each
remaining fiber, whereas F meets none of them. An automorphism of D
cannot map those nonempty intersections to empty intersections.
Thus this configuration is impossible for the global trace
involution, before assuming a mate.

Thus every smooth rational quartic-scroll normalization with locally
Gorenstein actual conductor is excluded. The boundary of this
particular argument is an actual nonreduced nongorenstein ACM cubic;
later sections address that boundary using additional structural
information. A concrete successful nonreduced example is the
[MF6 (8,1/2) conductor proof](2026-10-08-session-mf6-rhalf-scroll-conductor.md).

## 13. A cover of a support line cannot have degree at least three

Let E be any proper prime component of the actual D and suppose its
reduced map to a line in P3 has degree r>=2. This lemma does not require
Gamma reduced or Gorenstein, nor a trace algebra. Section 7 makes
E a smooth rational curve. If c meets E, the singleton-fiber condition
makes its point the sole point of the entire degree-r fiber on E.
The finite map P1->P1 is separable in characteristic zero, so its
ramification index there is r. Its differential vanishes, and therefore
dnu annihilates the tangent line of E. The immersion of c into its
smooth image forces c transverse to E, with local intersection one.

Riemann--Hurwitz gives total ramification degree 2r-2. Each possible
intersection consumes r-1 of that budget, so at most two such points
exist. But c~H and E maps to a line, giving

    c.E=H.E=r.

Thus r<=2. Every prime cover of a support line of degree at least three
is excluded under a mate, including a degree-three prime in a
nonreduced triple-line conductor. This is a necessary geometric
obstruction; it does not classify the remaining degree-one and
degree-two prime configurations.

## 14. Generic descent extends across a nongorenstein conductor point

The normalization duality proof in section 2 gives the whole
normalization quotient

    0 -> O_X -> nu_*O_S -> omega_Gamma -> 0.

For every m it therefore identifies the descent obstruction of a
global section s of O_S(mH) with its image in omega_Gamma(m). The
canonical module of the pure CM curve Gamma is again Cohen--Macaulay
and has no nonzero finite-support submodule. Consequently, if s
descends at every generic point of the actual Gamma, with its full
Artin scheme structure retained, its global obstruction vanishes.
It descends everywhere on X.

This does not replace actual Gamma by its normalization or its reduced
support. It says that generic descent through the entire Artin
conductor algebra is enough for an existing global section on S.
It removes the need to construct a global deck involution at a
nongorenstein conductor point.

## 15. A doubled crossing forces squared eigenvalues to agree

Suppose E and E' are smooth transverse conductor primes, each with
multiplicity two, meeting at P. Assume their image lies in an open
Gorenstein part of Gamma and the local trace involution sigma exchanges
them. Choose regular parameters u,v at P with E={u=0}, E'={v=0}.
Suppose f defines the smooth c and its descended power gives generic
Artin-ring ratios

    sigma(f)=zeta f on 2E,
    sigma(f)=zeta^-1 f on 2E'.

These are equalities on the entire generic doubled schemes, not just
on their reduced fields. In the local ring of D, whose equation is
u^2 v^2, their differences belong respectively to (u^2) and (v^2).
Subtracting gives

    (zeta-zeta^-1) f in (u^2,v^2).

If zeta^2!=1, then f has no linear term, contrary to smoothness of c
at P. Hence zeta^2=1, and f^2 is generically invariant on both doubled
branches. This argument is stronger than the reduced crossing case,
where arbitrary reciprocal roots are locally possible.

## 16. Proposed exclusion for every double-line-plus-line conductor

The reduction in section 12 needs a global Gorenstein hypothesis only
to control the split C_min+fiber configuration on F2. Sections 14--15
suggest removing that hypothesis entirely for Gamma supported on two
lines with multiplicities two and one. The generic Artin partitions
still hold, since the actual multiplicity-two conductor is Gorenstein
at its generic point and the rank-two algebra is free there.

In the F0 and F2 configurations with a unique upstairs prime over each
base component, the generic trace action preserves both primes.
Section 11 therefore makes f^2 descend at each actual generic scheme
point. Section 14 extends that descent globally, without any global
trace involution.

The only additional configuration is

    S=F2, D=2C_min+2F+2F',

where C_min and F map isomorphically to the doubled line L, and F'
maps isomorphically to the other line M. Their restrictions of f have
the same zero, so c passes through P=C_min intersect F. The point
Q=C_min intersect F' maps to L intersect M. Since P and Q are
different and nu|C_min is an isomorphism, P maps away from the line
intersection. A pure CM double curve with smooth line support is a
ribbon away from M, hence locally Gorenstein there. Thus its local
trace involution exists near P and exchanges the two doubled primes.
Section 15 forces zeta^2=1. The remaining doubled fiber has an identity
reduced trace action and makes f descend generically there. Hence
f^2 descends at every actual generic scheme point and, by section 14,
globally. The usual quadric contradiction follows.

This extension was independently checked by the
normal-global-adversarial agent, while the direct Artin reduction in
[the independent audit](2026-10-08-session-scroll-artin-independent-audit.md)
provides another route through this case. It retains the generic Artin
lengths and the local doubled branches; a reduced-support argument
alone would not prove it. Triple-line conductors remain outside this
extension.

## 17. Proposed entire smooth-scroll closure by the differential obstruction

This alternate transverse-plane proof is retained as an independent
research route, with its geometric slice passage still explicitly
unpromoted. The exact Artin proof in
[nongorenstein cubic classification](2026-10-08-session-scroll-nongorenstein-cubic-classification.md)
and its [independent audit](2026-10-08-session-scroll-artin-independent-audit.md)
avoid this passage. The
[differential obstruction audit](2026-10-08-session-normalization-differential-independent-audit.md)
independently proves its first step: under a mate, nu must be
generically immersive along every proper conductor prime E. If its
generic differential rank were at most one, choose P in c intersect E
(nonempty since c~H is ample). Rank at P is also at most one. Rank zero
contradicts the immersion of c. For rank one, ker(dnu) restricted to E
is a regular line subbundle near P. Trivialize H by a nonvanishing
ambient hyperplane section. The identity nu*G=lambda f^n gives

    n f^(n-1) df(K)=0 on E.

Since f is not identically zero on E and characteristic is zero,
df(K)=0 on E, including P. Smoothness of c now makes its tangent equal
to ker(dnu), again contradicting the immersion of c.

At the generic point of a conductor support line, complete the
one-dimensional hypersurface local ring and extend its residue field
to an algebraic closure. This is a reduced plane-curve singularity
transverse to the line. Separability of the prime's map to the line
gives a nonzero longitudinal differential. Hence generic rank two of
nu means each geometric transverse branch is smooth: at least one
of its two normal coordinates has nonzero linear term.

The actual multiplicity m of Gamma along that support line equals
the transverse delta invariant. Indeed B/A=omega_Gamma has residue
field length m, the same length as the canonical module of the
Artin conductor quotient A/I. For smooth plane branches, delta is
the sum of pairwise intersection multiplicities, and the conductor
order on each branch is the sum of its intersections with the other
branches. These two formulas can be proved directly. The
Mayer--Vietoris sequence for a branch and the union of the others
adds its intersection multiplicity to the normalization defect.
For the conductor formula, choose a projection x which is a parameter
on every smooth branch fi. The hypersurface canonical generator
dx/(partial F/partial y), F=product fi, has on branch i a pole of
order sum_{j!=i} I(fi,fj); finite canonical duality gives precisely
that conductor order. No classification of arbitrary singular plane
branches is required, because the differential obstruction already
excludes them under a mate.

### Double-line-plus-line support

Here the generic deltas are two on L and one on M. At L, smooth
branches with total pair contact two must be two branches of contact
two, with conductor order two on each. At M, delta one means two
smooth transverse branches, with conductor order one on each.

On F0, the thick-line orbit of two branches is either a single
H-degree-two prime with multiplicity two, or two H-degree-one primes
of multiplicity two. The second would require four fiber
multiplicities, impossible in D~2C+2f. The first is 2C and leaves
2f. Since the other support line has a node, this residual cover must
be two distinct fibers with multiplicity one. Their paired zeros
contradict full singleton fibers.

On F2 there is no H-degree-two prime. The thick-line branches are two
degree-one primes with multiplicity two. If they are C_min and F,
the residual 2f over M is again a pair of distinct fibers and is
excluded. If they are two fibers, the residual 2C_min cannot realize
a nodal cover of M: it is neither one degree-two prime of multiplicity
one nor two distinct degree-one primes. Thus every double-line-plus-line
conductor is excluded, including nongorenstein points.

### Triple-line support

The generic delta is three. With all geometric branches smooth there
are only two possibilities: two branches with contact three, having
conductor order three each; or three branches with all pairwise
contacts one, having conductor order two each.

In the two-branch case, one degree-two prime of multiplicity three
would violate the C-coefficient bound on F0 and the absence of a
degree-two prime on F2. Two distinct degree-one primes of multiplicity
three would require either the unique C_min with coefficient three
on F2, or six fiber multiplicities on either scroll. All are
incompatible with D~-K.

For three ordinary branches, their residue-field orbits have sizes
three, two-plus-one, or one-plus-one-plus-one. A single degree-three
prime of multiplicity two is excluded by section 13. For the
two-plus-one orbit, only F0 permits the class: D=2E+2T with E a
horizontal degree-two prime mapping to the line and T a degree-one
fiber mapping to that same line. The two points of c intersect E
must be its two simple ramification points, with distinct branch
values. The mate vanishes at both values on the common base line,
so its pullback on the isomorphic T also vanishes at both points.
This contradicts c.T=H.T=1.

For three degree-one primes, only F2 permits the class:
D=2C_min+2F1+2F2. Each restricted f is a linear section pulled back
from the common support line. The descended power forces their zeros
to have the same base value. The two distinct fibers F1,F2 then
contain two different points of c in the same normalization fiber,
a contradiction.

Together with the accepted reduced-conductor theorem, this argument
would exclude every smooth rational quartic-scroll normalization in
any mate degree. The remaining audit is the exact passage from the
generic hypersurface ring to the geometric transverse branch
partition; all divisor and full-fiber cases above have been stated
with their actual conductor orders. This does not classify singular
scroll normalizations or all nonnormal quartic carriers.
