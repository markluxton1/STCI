# Independent audit: the whole scroll conductor is an ACM cubic

Date: 2026-10-08. Status: **ACCEPTED proof audit** of the all-integer
cohomology and Hilbert--Burch lemma recorded in the Oct8 checkpoint.
This is a structural reduction of the degenerate-conductor problem,
not an exclusion of every smooth-scroll carrier.

Let nu:S->X be the finite normalization of an integral quartic surface
in P3 in characteristic zero, where S is a smooth rational quartic
scroll with H=nu*O_X(1). Let I be the actual entire conductor and
Gamma=Spec_X(O_X/I), including all of its scheme structure. Let
J_Gamma be its ideal sheaf in P3. The previously accepted finite-duality
argument identifies I with nu_*omega_S and makes the upstairs
conductor D an effective Cartier divisor linearly equivalent to -K_S.

## 1. The ideal sequence and its entire scheme scope

The conductor sequence in the ambient projective space is

    0 -> O_P3(-4) -> J_Gamma -> nu_*omega_S -> 0.

Its first term is the equation of the integral quartic X; the quotient
is exactly I, not the ideal of the reduced conductor support. Since
both H1 and H2 of every line bundle on P3 vanish, twisting gives

    H1(P3,J_Gamma(m)) = H1(S,K_S+mH)

for every integer m. Finite pushforward has no higher cohomology
correction. The separate MCM/depth proof makes Gamma a pure
Cohen--Macaulay curve, and its Hilbert polynomial is 3m+1. Thus no
isolated or embedded conductor component is silently discarded.

## 2. Cohomology on both smooth quartic scrolls, for all integers

Write S=F_e with e=0 or 2, minimal section C of square -e,
fiber f, H=C+a f with a=e/2+2, and
K_S=-2C-(e+2)f. Let pi:S->P1 be its ruling.

For a divisor kC+beta f with k>=0, ruling pushforward is

    pi_*O_S(kC+beta f)=sum_(j=0)^k O_P1(beta-j e),
    R1 pi_*O_S(kC+beta f)=0.

The formula has the minimal-section convention C^2=-e; no sign change
between the F0 and F2 calculations is hidden. If k=-1, both direct
images vanish, since every fiber has O_P1(-1) cohomology zero.

For m>=2, K_S+mH has k=m-2 and beta=ma-e-2. Its smallest ruling
summand degree is

    ma-e-2-(m-2)e = m(a-e)+e-2.

This is 2m-2 on F0 and m on F2. All summands therefore have H1=0,
and the higher ruling pushforward vanishes. At m=1 the fiber degree
is -1, so both direct images vanish. For m<=0, surface Serre duality
reduces H1(K_S+mH) to the dual of H1((-m)H). Writing n=-m>=0,
the latter pushforward has degrees na-j e, 0<=j<=n, whose minimum
is n(a-e)>=0; its higher pushforward vanishes. This includes n=0.

Thus H1(J_Gamma(m))=0 for every integer m. Together with purity and
saturation, this proves that the entire conductor coordinate ring is
arithmetically Cohen--Macaulay, not only that the conductor is locally
Cohen--Macaulay.

## 3. Minimal generators and the full graded resolution

The same sequence gives H0(J_Gamma(1))=0: K_S+H has fiber degree -1.
At m=2 its pushforward is O_P1(2), so H0(J_Gamma(2)) has dimension
three. There are also no degree-zero generators.

Let R be the saturated homogeneous coordinate ring of Gamma. Its
Krull dimension is two and it is Cohen--Macaulay. Two general linear
forms are an R-regular sequence over the infinite field k. An
Artinian reduction A has length deg Gamma=3. Its initial Hilbert
entries are A0=1 and A1=2, since J_Gamma has no linear forms. These
already sum to its length, so its h-vector is exactly (1,2).

Consequently A is k[u,v]/(u,v)^2. Its three quadratic generators
lift to the three independent quadrics of J_Gamma. Because the two
linear forms are R-regular, the Koszul Tor groups vanish and reduction
identifies J_Gamma/(ell1,ell2)J_Gamma with that reduced ideal. Graded
Nakayama therefore proves that the three quadrics generate the entire
ideal; higher-degree generators are not being guessed from the first
few Hilbert-function values.

Auslander--Buchsbaum gives projective dimension two for R and one
for its ideal. Its Hilbert series is

    Hilb_R(z)=(1+2z)/(1-z)^2,
    Hilb_J(z)=(3z^2-2z^3)/(1-z)^4.

With exactly three degree-two generators, the minimal first syzygy
module is therefore O_P3(-3)^2. This establishes

    0 -> O_P3(-3)^2 -> O_P3(-2)^3 -> J_Gamma -> 0.

The matrix is a 3-by-2 matrix of linear forms, and Hilbert--Burch
identifies its three maximal minors with the conductor quadrics.
The argument does not assume Gamma integral, reduced or Gorenstein.

## 4. What the resolution does not imply

The rank-two cover arguments for a smooth Gamma cannot be applied
merely because Gamma has this resolution. At a non-Gorenstein
conductor point its canonical module is not invertible. The upstairs
conductor algebra need not be locally free of rank two over Gamma;
the retained ordinary triple-line generic algebra is a concrete
warning. An involution on reduced component fields also does not
automatically provide descent through the entire conductor scheme.

The exact sequence under investigation by the degenerate-conductor
agent is

    0 -> O_Gamma -> nu_*O_D -> omega_Gamma -> 0.

It follows by dualizing the conductor sequence on the Gorenstein X:
the conductor I and normalization nu_*O_S are MCM dual modules,
Ext1(O_Gamma,O_X)=omega_Gamma, and the next Ext group of I vanishes.
Modding the normalization sequence by I gives the displayed sequence.
When Gamma is Gorenstein this makes nu_*O_D locally free of rank two,
since an extension of two invertible modules is locally split. At
non-Gorenstein points this conclusion is unavailable.

## 5. A false reduced-graph shortcut and its precise obstruction

The naive propagation of constant roots of unity along conductor
components needs to distinguish separate attachment points from a
triple meeting. Consider the local base node R=k[[x,y]]/(xy) and
rank-two algebra

    R[eta]/(eta^2-x-y^2).

Eliminating x embeds D on the smooth (y,eta)-surface as
y*(eta^2-y^2)=0. Its three smooth branches meet at one point. The
branch y=0 covers x=eta^2; the exchanged branches eta=+y and eta=-y
map isomorphically to x=0. A smooth curve alpha*y+beta*eta=0 has
contact one with all three branches for generic coefficients. Its
two exchanged restrictions have constant ratio
(alpha-beta)/(alpha+beta), which may be any nonzero root of unity.
On the stable branch the deck eigenvalue is -1.

Thus zeros consumed by the mutual intersection of the exchanged
line pair can also occur at both attachments to the rest of D.
The claim that f is necessarily nonzero at those attachments is
false without additional geometric information. This local example
is an obstruction to that proof strategy, not an STCI example of C0
and not a claim of global realization by a quartic projection.

The subsequent conic-component argument uses global intersection
degrees and ramification, and survives this local triple meeting.
Its completion and the nonreduced cases are separate proof
obligations; they must not be inferred just from the ACM resolution.
