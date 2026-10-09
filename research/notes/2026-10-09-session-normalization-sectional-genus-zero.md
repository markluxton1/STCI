# Quartic normalizations of sectional genus zero and the remaining singular lane

Date: 2026-10-09. Owner: `singular_normalization_next_frontier`.
Status: **PROVED HERE, independently accepted**. The proof uses
the standard characteristic-zero Kawamata--Viehweg vanishing theorem
and the classical minimal-degree classification, with primary source
checks stated below. It does not classify every singular normalization
or settle the unrestricted quartic-carrier problem.

The [independent genus-zero audit](2026-10-09-session-normalization-genus-zero-independent-audit.md)
has accepted all sections below and the automatic generic regularity
strengthening in section 1.

Let k be an algebraically closed field of characteristic zero. Let
X subset P3 be an integral quartic, let nu:S->X be its finite
normalization, and put H=nu*O_X(1). Suppose that X is regular at the
generic point of a smooth rational curve C of degree four. A mate means
an ambient homogeneous G of some positive degree b whose zero set on X
is exactly C. No semi-log-canonical hypothesis is made.

## 1. The support and divisor identities that are available

The [full-support theorem](2026-10-06-session-conductor-support.md) and
the [smooth-lift argument](2026-10-07-session-nonnormal-structural-progress.md)
give, under a mate,

    (nu^{-1}(C))_red = c,
    nu|c:c -> C is an isomorphism,
    div_S(nu*G) = b c ~ b H.

In particular c is a smooth embedded P1 on S, every normalization fiber
above C is a singleton, and b c is Cartier. The equality of coefficients
uses H.c=deg(C)=4 and H^2=deg(X)=4. The curve c need not itself be
Cartier when it meets Sing(S). Its possible non-Cartierness is retained.

**Automatic generic regularity for the degree-four curve.** The
generic-regularity hypothesis on X along C follows from the other
quartic hypotheses. Otherwise all first derivatives of X's equation
vanish along C. A general plane meets the smooth degree-four curve
in four distinct points and cuts out an integral plane quartic on X.
Each of the four points is singular on that plane quartic, giving
normalization defect at least four, contrary to its arithmetic genus
three. Thus an integral quartic cannot be singular generically along
a smooth degree-four curve. This is root's strengthening, separately
checked in the independent audit. It does not apply to all higher
carrier degrees.

Define pi to be the genus of a general hyperplane divisor on S. The
pullbacks of the four ambient coordinates form a basepoint-free linear
system. A general member is irreducible and smooth and avoids the
finitely many singular points of S. One can apply Bertini to this
system on S_reg; its image is a general integral plane section of X.
That image has arithmetic genus three, and the pulled-back divisor
is its normalization. If X is nonnormal, the normalization defect of
the general plane section is positive. Consequently

    0 <= pi <= 2

in the nonnormal case. The separate
[singular-degree audit](2026-10-08-session-singular-degree-and-singleton-hessian-audit.md)
records the complete plane-section defect argument. Here pi is a
normalization sectional genus, not the arithmetic genus of an ambient
plane quartic and not the degree of a conductor or Jacobian scheme.

## 2. Sectional genus zero forces a minimal-degree normalization

**Proposition.** If pi=0, then the polarized surface (S,H) is one of

    (F0,C+2f), (F2,C_min+3f), (P2,O(2)),
    or the normal cone S(0,4) with its hyperplane polarization.

This classification does not assume that S is smooth.

Choose a resolution sigma:M->S and let L=sigma*H. Then L is a nef and
big Cartier divisor, L^2=4, and a general divisor Y in the original
four-section system is a smooth P1 of class L, disjoint from the
exceptional locus. Adjunction gives

    K_M.L = -6,       (K_M+L).L = -2.

No nonzero effective divisor has negative intersection with a nef
divisor, so H0(M,K_M+L)=0. Characteristic-zero Kawamata--Viehweg
vanishing also gives Hi(M,K_M+L)=0 for i>0. Surface Riemann--Roch
therefore gives

    0 = chi(K_M+L)
      = chi(O_M) + (K_M+L).L/2
      = chi(O_M)-1.

The inequality K_M.L=-6 likewise gives H0(M,K_M)=0. Hence
chi(O_M)=1 and p_g(M)=0 imply h1(O_M)=0. Since sigma_*O_M=O_S,
the low-degree Leray sequence injects H1(O_S) into H1(O_M), so

    H1(O_S)=0.

The exact sequence of the Cartier divisor Y on S is

    0 -> O_S -> O_S(H) -> O_Y(H) -> 0.

The line bundle O_Y(H) has degree four on P1. Taking global sections
gives h0(S,H)=1+5=6.

The complete linear system |H| defines a finite morphism S->T subset
P5. It is finite because H is ample, so a positive-dimensional fiber
would contain a curve on which H has degree zero. It is birational:
the original four-coordinate normalization map factors through this
map, and already induces the equality k(X)=k(S). Thus T is an integral
nondegenerate degree-four surface in P5, a variety of minimal degree.

The classical classification says that such a surface is a rational
normal scroll S(a,b), with 0<=a<=b and a+b=4, or the Veronese surface.
These surfaces are normal: the positive-parameter scrolls and the
Veronese are smooth, and S(0,4) is the normal cone over a rational
normal quartic. The finite birational map from S to this normal T is
an isomorphism. The three scrolls are S(2,2)=F0, S(1,3)=F2, and
S(0,4); this proves the proposition.

For the source inputs, [Horing, The sectional genus of quasi-polarised
varieties](https://math.univ-cotedazur.fr/~hoering/articles/a12-sect-genus.pdf)
explicitly uses Kawamata--Viehweg vanishing and Riemann--Roch in
Proposition 2.6, and states g=0 implies Delta=0 for normal complex
varieties in Theorem 1.2. The direct surface proof above supplies the
needed result over k without importing that theorem's complex-field
restriction. [Eisenbud--Green--Hulek--Popescu, Small schemes and
varieties of minimal degree](https://www.math.stonybrook.edu/~sorin/eprints/2-regular.pdf),
Theorem 0.1, states the minimal-degree classification, including cones.
Only that stated standard theorem is imported here.

## 3. The singular minimal-degree cone is excluded in every mate degree

**Proposition.** If (S,H)=S(0,4) with its hyperplane polarization,
X has no mate for C as above.

Let sigma:F4->S contract its negative section E, where E^2=-4 and
E.f=1. Its hyperplane pullback is

    L=E+4f.

Deleting the exceptional E upstairs and the vertex v downstairs
identifies their remaining open sets. Since deleting a codimension-two
point does not change the Weil class group,

    Cl(S) = Pic(F4)/Z[E] = Z[f],       [H]=4[f].

This group has no torsion. Thus b(c-H)~0 implies c~H as Weil divisors.
In particular c is Cartier, since H is Cartier. A smooth curve which
is Cartier at a point of a surface forces that surface point to be
regular: in a two-dimensional local ring R, a principal curve ideal
(h) with R/(h) regular of dimension one gives embdim(R)<=2. Therefore
c does not pass through the singular vertex v.

Its strict transform c# on F4 is a smooth curve of class L, disjoint
from E, and c#.f=1. It is a section of the ruling F4->P1 and meets
every ruling fiber in exactly one point away from E.

The complete |H| map identifies S with its cone in P5. The original
four sections are a linear projection with center disjoint from S:
basepoint freeness proves the disjointness. The image X is a cone
with vertex nu(v). Choose coordinates with that vertex [1:0:0:0].
Three of the sections vanish at v and are binary quartics on the
base P1; the fourth does not vanish at v. The three binary quartics
have no common zero, since otherwise their ruling would be contracted,
contrary to finiteness. They define

    beta:P1 -> B subset P2.

The map beta is finite birational: a generic degree greater than one
would give that same degree for nu on a general cone ruling. Its
pullback O_B(1) is O_P1(4), so B is an integral plane quartic and beta
is its normalization. Every ruling fiber minus E maps isomorphically
to its image ruling minus the vertex, since H.f=1.

If some point of B has at least two preimages p1,p2 in P1, denote the
corresponding ruling fibers by F1,F2. The point c# intersect F1 maps
to a nonvertex point x on their common image ruling. There is also
one normalization preimage of x in F2. Full inverse support requires
that point to be c# intersect F2. Thus these two distinct points of
c have the same image, contradicting nu|c being an isomorphism.
Every fiber of beta is therefore a singleton.

The rational plane quartic B is singular, since its arithmetic genus
is three. Choose a singular point with its unique preimage p. The
derivative of beta at p is zero. Indeed, a nonzero derivative in
one local plane coordinate gives a uniformizer of k[[t]]; its formal
inverse shows that the completed local branch ring is k[[t]], making
the singleton plane-curve point regular. This is incompatible with
singularity.

Consequently, at every nonvertex point of the ruling F_p, the
differential of nu has rank one. In local coordinates t,z, with
t=0 defining F_p, the map is

    (t,z) -> (z,beta_1(t),beta_2(t)),

and its kernel along F_p is generated by partial_t. Let P be the
unique point c intersect F_p. The surface S is smooth there, c has
a smooth local equation f=0, and a local pullback of the mate is

    nu*G = u f^b,

with u a unit. Differentiating in the kernel of dnu and restricting
to the integral ruling gives

    f^(b-1) (b u partial_t(f)+f partial_t(u)) = 0.

The restriction of f is nonzero on the ruling, so it can be cancelled.
At P, f=0 and b u is nonzero, giving partial_t(f)(P)=0. The smooth
tangent of c is therefore the kernel of dnu, contrary to the
immersion nu|c:c->C subset P3. This proves the cone exclusion.

The same local-unit differential argument is independently stated in
[the differential audit](2026-10-08-session-normalization-differential-independent-audit.md).
The proof here does not cite an unrederived arbitrary-degree cone
theorem and does not assume that a section on S descends to X.

## 4. Consequence after combining the accepted scroll and Veronese lanes

The accepted [entire smooth-scroll theorem](2026-10-08-session-scroll-nongorenstein-independent-audit.md)
excludes the first two polarizations in section 2, and the accepted
[entire Veronese theorem](2026-10-08-session-veronese-allmate-independent-audit.md)
excludes the third. Section 3 excludes the fourth. Thus:

**Corollary.** Under the hypotheses above, a mate requires pi>0.
Since X is nonnormal in this remaining lane, pi is one or two.
The smooth-locus lemma in the structural note forces pi=0 if c
avoids Sing(S). Therefore every hypothetical mate in the remaining
nonnormal quartic lane has

    pi in {1,2},       c intersect Sing(S) nonempty.

In particular **every integral quartic with smooth normalization** is
excluded in every mate degree. There is no additional smooth
normalization polarization omitted by the F0/F2/P2 exclusion: under
a mate, its sectional genus would be zero and section 2 is exhaustive.
Section 1 makes the generic-regularity hypothesis automatic for every
integral quartic containing this smooth degree-four curve. Thus the
corollary covers all integral quartic carriers of fixed C0. Thick
carriers in other degrees, and all other carrier degrees, are separate.

## 5. The correction retained at singular normalization points

For a resolution sigma:M->S, the equality b c~bH supplies an effective
rational exceptional divisor Z such that

    sigma*(b c)/b = c# + Z numerically equivalent to L=sigma*H.

Its coefficients have denominators dividing b. Negative definiteness
of the exceptional intersection form gives

    q=-Z^2=c#.Z >= 0,       c#^2=4-q.

The strict transform c# is still smooth and isomorphic to c: its
proper birational map to the already smooth c is an isomorphism.
Adjunction, K_M.L=2pi-6, and c#=L-Z numerically give the exact identity

    q + K_M.Z = 2pi.

No Q-Gorenstein assumption on S is needed for this identity: all
intersections are on smooth M. For an ADE normalization, K_M is
orthogonal to the exceptional curves and it reduces to q=2pi.

At each singular point of c, the local Weil class [c] is a nonzero
torsion class of order dividing b. If it were zero, c would be Cartier
and the local regularity argument of section 3 would make S smooth
there. Thus locally factorial or torsion-free local class groups
remove such points. This is a necessary filter; it does not exclude
all singular normalization classes. In particular rational double
points can admit exactly this finite torsion.

The [local lift countershield](2026-10-09-session-singular-local-lift.md)
constructs an order-one affine quartic carrier with A1 normalization
and a smooth curve passing through the normalization singularity,
with full inverse support and an actual local mate. It prevents
discarding the remaining singular lane merely from smoothness of c
or the Cartier property of b c.

## 6. Continuation boundary

The next structural task is to examine pi=1 or pi=2 normalizations
together with the actual conductor and the finite torsion classes
at c intersect Sing(S). The exact identity in section 5 must retain
its exceptional correction. Pulling the mate to a resolution can
introduce exceptional zero factors, so the unit differential proof
cannot be transferred across those points without checking them.

No full classification of those positive-genus normalizations has
been imported from a table of semi-log-canonical quartics. Original
Urabe classification endpoints attempted on October 8 were inaccessible;
the secondary restatements and slc tables remain leads rather than
an exhaustion of arbitrary nonnormal quartics. The universal problem
and the unrestricted fixed C0 characteristic-zero problem remain open.
