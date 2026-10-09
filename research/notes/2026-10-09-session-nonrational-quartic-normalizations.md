# Nonrational normalizations cannot occur for nonnormal quartics containing C0

Date: 2026-10-09. Owner: `singular_normalization_next_frontier`.
Status: **PROVED HERE, submitted for independent audit**. This is a
structural reduction, not an exhaustive rational-normalization
classification or a resolution of the unrestricted STCI problem.

Throughout k is algebraically closed of characteristic zero and C0
is the fixed smooth rational curve of degree four in P3. Let X be an
integral nonnormal quartic containing C0, let nu:S->X be its finite
normalization, and let H=nu*O_X(1). The conclusion below does not
assume a mate, full inverse-image purity, Cartierness of the lifted
curve, or any semi-log-canonical condition.

## 1. Numerical data and the lifted rational curve

The general plane-section argument in the
[singular-degree audit](2026-10-08-session-singular-degree-and-singleton-hessian-audit.md)
gives normalization sectional genus

    0 <= pi <= 2.

The upper bound uses nonnormality: a general integral plane quartic
has arithmetic genus three and meets a nonnormal curve of X, so its
normalization defect is positive. Its normalized smooth curve is a
general hyperplane divisor on S.

An integral quartic is automatically regular at the generic point
of C0. Otherwise a general integral plane quartic would have the four
distinct intersection points with C0 as singular points, giving defect
at least four, greater than its arithmetic genus three. This argument
is independently recorded in the
[genus-zero audit](2026-10-09-session-normalization-genus-zero-independent-audit.md).

There is consequently exactly one curve component c of nu^{-1}(C0),
finite and birational over C0. Its reduced scheme is isomorphic to
C0, since an integral finite birational extension of a normal curve
ring is that ring. Other isolated inverse-image points may occur;
they have no role in this proof and have not been discarded.

Choose a resolution sigma:M->S. Write L=sigma*H and c# for the
strict transform of c. The proper birational map c#->c is a map of
integral curves, hence quasi-finite and finite; normality of c makes
it an isomorphism. Thus c# is a smooth P1 and

    L^2=4,       L.c#=4,       K_M.L=2pi-6.

The last identity comes from a general smooth hyperplane curve of
class L, disjoint from the exceptional locus. The Cartier divisor
L is nef, big, and globally generated. Nothing here assumes that
c is Cartier on S.

## 2. The resolution is rational or ruled, and its irregularity is bounded

Because pi<=2, one has K_M.L<0. A nonzero effective divisor has
nonnegative intersection with the nef L, so every pluricanonical
space H0(M,mK_M), m>0, vanishes. Therefore kappa(M)=-infinity.
The characteristic-zero classification of smooth projective surfaces
then says that M is rational or birationally ruled over a smooth
curve B of positive genus. In the latter case, a sequence of
contractions of (-1) curves gives a geometrically ruled surface
M0=P_B(E), with g(B)=h1(O_M). One may retain the ruling morphism
M->M0->B throughout these point blowups.

For a primary author-hosted statement of the classification input,
see [McKernan, Classification of Surfaces, Theorem 7.7](https://www.math.ucsd.edu/~jmckerna/Teaching/20-21/Spring/206A/l_7.pdf).
Only its kappa=-infinity case is used. This is a standard surface
classification theorem, not the nonnormal quartic tables of Urabe.

Kawamata--Viehweg vanishing and Serre duality give

    H1(M,-L) = H1(M,K_M+L)^* = 0.

For a general smooth hyperplane curve Y of genus pi, the sequence
0 -> O_M(-L) -> O_M -> O_Y -> 0 therefore injects H1(O_M)
into H1(O_Y). Thus

    g(B) <= pi <= 2

if M is nonrational. The nef-big vanishing input is the same standard
one checked in [the genus-zero proof](2026-10-09-session-normalization-sectional-genus-zero.md).

## 3. Nef pushdown and the multiplicity bound at every point blowup

Suppose for contradiction that M is nonrational. Let

    M=M_r -> M_{r-1} -> ... -> M_0=P_B(E)

be point blowdowns to a relatively minimal ruled surface. Denote the
point-blowup maps by tau_i:M_i->M_{i-1}. Starting with L_r=L, define
L_{i-1}=(tau_i)_*L_i. If E_i is the exceptional curve on M_i, write

    L_i=tau_i*L_{i-1}-m_i E_i,
    m_i=L_i.E_i.

The following statements are inductive, so they apply equally to
infinitely near centers.

First m_i>=0 since L_i is nef. For every irreducible curve A on
M_{i-1}, with strict transform A# and point multiplicity r_A>=0,

    L_{i-1}.A = L_i.A# + m_i r_A >= 0.

Hence L_{i-1} is nef. All the pushed-down divisors are nef, without
assuming that their original linear systems are basepoint free.

Let f be a ruling fiber on M0, and put a=L_0.f. This number is also
the intersection of L_i with any entire fiber cycle F_i of M_i->B.
It is positive: a nef divisor of positive square cannot be numerically
orthogonal to the nonzero isotropic ruling class f by the Hodge index
theorem. The degree a is an integer.

At the i-th blowup center, choose an irreducible component A of its
entire fiber F_{i-1}. That fiber is a positive integral cycle. Nefness
of L_{i-1} gives

    L_{i-1}.A <= L_{i-1}.F_{i-1}=a.

The multiplicity r_A of A at the center is at least one. Nefness of
L_i on its strict transform gives

    0 <= L_i.A#=L_{i-1}.A-m_i r_A.

Therefore m_i<=a. This proof uses the actual component of the fiber
through the center, including reducible fibers created by previous
blowups. It does not incorrectly replace an infinitely near fiber
by a new smooth fiber. We have proved

    0 <= m_i <= a       for every i.

## 4. The ruled intersection identity forces ruling degree at most two

Choose a section C on M0 with C^2=-e, C.f=1, and write numerically

    L_0=a C+b f,
    K_{M0}=-2C+(2g-2-e)f,
    g=g(B)>=1.

The formula for K_M under a point blowup and the expression in
section 3 give, using total transforms for all exceptional classes,

    L^2 = a(2b-ae)-sum_i m_i^2 = 4,
    K_M.L = a(2g-2+e)-2b+sum_i m_i = 2pi-6.

The total-transform convention is essential for infinitely near
points; those classes have diagonal intersection -1, and each
point blowup adds exactly one m_i to the canonical intersection.
Eliminating 2b-ae yields the exact identity

    4 = (2g-2)a^2 + (6-2pi)a
        + sum_i m_i(a-m_i).

Every summand in the final sum is nonnegative by section 3. Also
2g-2>=0 and 6-2pi>=2. Thus 4>=2a, so

    1 <= a <= 2.

For pi=1 the sharper bound is a<=1. The auxiliary irregularity
bound gives exactly the possible (g,pi) pairs (1,1), (1,2), (2,2),
but their enumeration is not needed for the contradiction.

## 5. The lifted rational curve has impossible fiber degree

Every morphism from the smooth P1=c# to the positive-genus curve B
is constant. In characteristic zero a nonconstant map would be
finite separable and Riemann--Hurwitz would give

    -2 = deg(c#->B)(2g-2) + degree(ramification) >= 0.

Thus c# lies in one fiber of M->B and is an irreducible component
of its effective positive fiber cycle F. Since L is nef and every
component of F occurs with a positive integer coefficient,

    4=L.c# <= L.F=a <= 2,

a contradiction. No assumption about full normalization fibers or
a mate was used in deriving it.

**Theorem.** Every integral nonnormal quartic X containing fixed C0
has a rational normalization S. More generally the same proof applies
to any smooth rational degree-four curve in X. In particular no
nonrational normalization can supply a quartic STCI carrier for C0.

## 6. Consequences and retained work

Under a mate, the accepted [genus-zero exclusion](2026-10-09-session-normalization-sectional-genus-zero.md)
now leaves only rational normalizations with pi=1 or pi=2, and
the smooth lifted c must meet Sing(S) in non-Cartier finite-torsion
classes. The nonrational exclusion above is stronger: it excludes
those normalizations as carriers of C0 even before asking for a mate.

Rationality also gives H1(O_S)=0 by the low-degree Leray injection
into H1(O_M). Restriction to a general genus-pi hyperplane curve,
whose degree-four line bundle has H1=0 for pi=1 or 2, gives

    h0(S,H)=5 for pi=1,        h0(S,H)=4 for pi=2.

These dimensions are structural information; h0=5 alone does not
assert that H embeds S or that every genus-one normalization has
already been classified. The next genus-one reduction must establish
the canonical divisor and singularity hypotheses before a del Pezzo
or D5 root argument is imported. Rational genus-two normalizations,
their nonreduced conductors, and every higher carrier degree remain
outside this note's exclusion.
