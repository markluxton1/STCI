# Independent audit: sectional genus zero and the singular cone

Date: 2026-10-09. Auditor: `normal_global_adversarial`. Status:
**PROVED HERE / independently accepted**, with the scope below.
This is a bounded proof audit; no canonical frontier documents were edited.

Owner proof:
[Normalization sectional genus zero](2026-10-09-session-normalization-sectional-genus-zero.md),
sections 1--6. Accepted earlier inputs are the full inverse-support
reduction, the all-scroll theorem, the all-Veronese theorem, and the
local-unit differential lemma. The vanishing and minimal-degree
classification inputs are identified explicitly below.

## 1. Exact scope and definition of sectional genus

Let k be algebraically closed of characteristic zero, X subset P3 an
integral quartic, nu:S->X its finite normal normalization, and
H=nu^*O_X(1). Assume X is regular at the generic point of the smooth
rational quartic C under consideration. Under a mate of degree b,
the full-support reduction gives a unique smooth integral c isomorphic
to C and

    div_S(nu^*G)=b c,       b c~bH,

with every normalization fiber above C a singleton. It does not assert
that c itself is Cartier at a singular point of S.

Define pi as the genus of a general divisor from the original four
pulled-back ambient coordinate sections. They are basepoint-free and
their morphism is finite. Since S is a normal surface, Sing(S) is
finite; a general member avoids it. Characteristic-zero Bertini on
S_reg gives smoothness, and the irreducibility theorem for a
basepoint-free system with two-dimensional image gives integrality.
This is a smooth integral curve whose finite birational image is a
general plane quartic, so it is that plane curve's normalization.
There is no circular assumption that the complete |H| is already
six-dimensional.

Consequently 0<=pi<=3, and pi<=2 if X is nonnormal: its codimension-one
singular support meets a general plane and produces a singular plane
quartic with positive normalization defect. In the normal case a
general plane avoids the isolated singular locus and has pi=3.

## 2. Vanishing on the resolution is valid without rationality

Choose a smooth projective resolution sigma:M->S and put L=sigma^*H.
The divisor is nef and big, with L^2=4, regardless of the rationality
or singularity type of S. A general hyperplane divisor avoids the
exceptional locus, so its strict transform Y has class L and genus pi.
Adjunction gives K_M.L=2pi-6.

If pi=0 then (K_M+L).L=-2. Since L is nef, no effective divisor can
have negative intersection with L, so h0(K_M+L)=0. The standard
characteristic-zero Kawamata--Viehweg theorem applies on the smooth
projective M to the nef and big Cartier divisor L and gives
Hi(K_M+L)=0 for i>0. Surface Riemann--Roch therefore gives

    0=chi(K_M+L)=chi(O_M)+(K_M+L).L/2=chi(O_M)-1.

The same nef-intersection argument with K_M.L=-6 gives p_g(M)=0.
Thus chi(O_M)=1 forces q(M)=0. Normality gives sigma_*O_M=O_S, and
the low-degree Leray sequence injects H1(O_S) into H1(O_M), proving
H1(O_S)=0. Rational singularities were not assumed, and no assertion
R1 sigma_*O_M=0 is required for this injection.

For a primary-source consistency check, Proposition 2.6 of
[Horing, The sectional genus of quasi-polarised varieties](https://math.univ-cotedazur.fr/~hoering/articles/a12-sect-genus.pdf)
uses this nef-big vanishing and Riemann--Roch mechanism. Its complex-field
Theorem 1.2 is not needed: the direct surface proof uses standard
characteristic-zero vanishing over the stated field.

## 3. The complete map and classification are exhaustive

The exact sequence on S of a general smooth Y is

    0 -> O_S -> O_S(H) -> O_Y(H) -> 0.

Here Y=P1 and deg(H|Y)=4. Since H1(O_S)=0, it gives h0(H)=1+5=6.
The complete basepoint-free system defines phi:S->T subset P5.
It is finite: H is ample, so no positive-dimensional fiber can contain
a curve of H-degree zero. It is birational because the original
four-section map factors through it and already has k(X)=k(S).
More explicitly, the projection center is disjoint from T, as the
four sections have no common zero on S; hence
k(X) subset k(T) subset k(S) are equal. Nondegeneracy is automatic
for the image of a complete six-dimensional system. The finite
birational map gives deg(T)=H^2=4 and codim(T,P5)=3.

[Eisenbud--Green--Hulek--Popescu, Small Schemes and Varieties of Minimal Degree](https://www.math.stonybrook.edu/~sorin/eprints/2-regular.pdf),
Theorem 0.1, gives the classification over an algebraically closed
field. For a degree-four surface in P5 it yields exactly S(2,2),
S(1,3), S(0,4), and the Veronese surface. They are respectively
(F0,C+2f), (F2,C_min+3f), the rational-normal-quartic cone, and
(P2,O(2)). The first, second, and fourth are smooth. The cone is
normal: its homogeneous ring is a polynomial extension of the normal
fourth Veronese subring of k[s,t]. Thus all four T are normal.
Finite birational phi to normal T is an isomorphism, proving the
claimed exhaustive classification of the polarized normal S.

The qualification “normalization is smooth” is not introduced into
the reduction. The one singular minimal-degree possibility remains
explicitly in the list.

## 4. The singular cone exclusion passes in every mate degree

Let sigma:F4->S(0,4) contract its negative section E, with E^2=-4,
and let f be a ruling fiber. The polarization pulls back to L=E+4f.
Removing E and the vertex v identifies the two remaining smooth open
sets. Weil localization gives

    Cl(S)=Pic(F4)/Z[E]=Z[f],       [H]=4[f].

This group is torsion-free. The mate identity b(c-H)~0 therefore
makes c~H as Weil divisors, so c is Cartier. If c passed through v,
the principal quotient defining its regular one-dimensional local
ring would give embdim(O_S,v)<=2, forcing that surface local ring to
be regular. This contradicts the singular vertex. Equivalently, the
vertex has embedding dimension five and a principal quotient can
decrease it by at most one. Thus c avoids v.

Its strict transform is a smooth ruling section c#~E+4f, disjoint
from E, meeting each fiber once away from E. Choose the original
four sections so that three vanish at v and the fourth does not.
They define a cone projection: the three sections are binary
quartics q0,q1,q2, and on a ruling the remaining section is a
nonzero vertex coefficient plus a binary quartic. The q_i have no
common zero; otherwise a ruling would be contracted (indeed a point
on it would be a base point), contrary to finiteness.

They define beta:P1->B subset P2. Birationality of nu forces beta
birational, and beta^*O_B(1)=O_P1(4) makes B an integral rational
plane quartic. Every source ruling maps isomorphically to the
corresponding image ruling; only their common vertex is collapsed
on F4, and it has already been excluded from c.

If beta has a fiber containing distinct p1,p2, take the image of the
unique c#-point on the first ruling. It is a nonvertex point and has
another preimage on the second ruling. The entire inverse-support
condition forces that preimage onto c#, contradicting singleton
fibers or nu|c being an isomorphism. Thus beta must be unibranch
everywhere.

The rational plane quartic B is nevertheless singular, since its
arithmetic genus is three. At a singular point with one normalization
preimage, d beta vanishes. In formal local plane coordinates, any
nonzero first derivative would give a uniformizer with a formal
inverse, making the complete branch ring k[[t]] and the point regular.

Away from the vertex the cone map has local form

    (t,z) -> (z,beta_1(t),beta_2(t)).

Consequently its differential has rank one along the ruling above
that unibranch singularity. The ruling meets c at a point where S
is smooth. The entire pulled-back mate there is u f_c^b with u a
unit, so the independently accepted local-unit differential lemma
contradicts immersion of nu|c. This excludes the cone in every
positive mate degree. It imports no arbitrary-degree cone theorem.

## 5. The exceptional correction also passes

The owner's further identity is valid and retains the singular
normalization boundary. On any resolution, the actual effective
Cartier pullback of b c gives

    sigma^*(b c)/b=c# + Z numerically equivalent to L,

where Z is effective rational exceptional, with denominators dividing
b. The strict transform c# maps properly birationally to smooth c.
A dominant map of integral curves cannot have a positive-dimensional
fiber; otherwise the whole source curve would map to that point.
It is therefore quasi-finite, hence finite, and normality of c makes
the finite birational map an isomorphism. In particular c# is smooth.

Exceptional orthogonality L.Z=0 gives

    q=-Z^2=c#.Z>=0,       c#^2=4-q.

Adjunction to c# together with K_M.L=2pi-6 then gives exactly

    q+K_M.Z=2pi.

All intersections take place on smooth M; no Q-Gorenstein condition
on S is needed. For ADE singularities K_M is orthogonal to all
exceptional curves, giving q=2pi. At any singular point of S lying
on c, its local Weil class is nonzero torsion of order dividing b:
zero class would make c Cartier there and force S regular by the
principal-quotient argument.

## 6. Accepted conclusion and retained boundary

Combining this exhaustive pi=0 reduction and cone proof with the
accepted F0/F2 and P2 projection theorems excludes every pi=0
normalization in every mate degree. If c avoids Sing(S), it is
Cartier and its pullback on the resolution is c# with no exceptional
correction; c# is numerically L, and adjunction forces pi=0.

Therefore, under the stated generic-regularity hypothesis, any
remaining nonnormal quartic mate must have

    pi in {1,2},       c intersect Sing(S) nonempty.

In particular every integral quartic with smooth normalization is
excluded under these hypotheses. This does not cover carriers
singular at the generic point of C, other carrier degrees, or all
positive-sectional-genus singular normalizations. The singular local
countershields remain pertinent: b c may be Cartier while c is not.
No universal STCI resolution follows from this audit.

`git diff --check` passed after this independent proof was saved.

## Addendum: generic regularity along C0 is automatic for integral quartics

Status: **PROVED HERE / independently accepted**. The generic-regularity
qualifier in the earlier statement can be removed for the fixed C0.

Suppose an integral quartic X=V(F) were singular at the generic point
of the smooth degree-four curve C0. In characteristic zero the
hypersurface Jacobian criterion implies that every homogeneous partial
derivative of F vanishes at that generic point, hence on the entire
integral C0. Choose a general plane Pi. Two nonempty open conditions
can be imposed simultaneously: Pi cuts C0 transversely in four distinct
points, and Y=X intersect Pi is an integral plane quartic. The latter
is the standard Bertini irreducibility and reducedness conclusion
for the hyperplane system of an integral embedded surface; it does
not require X to be normal or smooth. See
[Stacks, Bertini theorems](https://stacks.math.columbia.edu/tag/0G4C).

At each of those four points, every derivative of the plane quartic
equation is a linear combination of the ambient partial derivatives
of F and therefore vanishes. Thus Y has four distinct singular points.
For its normalization Ybar, the normalization exact sequence gives

    3=p_a(Y)=g(Ybar)+sum_P delta_P(Y).

Each singular point of an integral plane curve has delta_P>=1, and
g(Ybar)>=0. Four such points contradict this identity. Therefore X
is regular at the generic point of C0.

Neither nonplanarity of C0 nor normality of X is used. The general
plane is chosen not to contain C0, and all four intersections are
proper, reduced, and distinct. The same argument, simultaneously
avoiding intersections and exceptional points of the finitely many
singular curve components, bounds the total degree of the reduced
one-dimensional singular support of any integral quartic by three.

Consequently the combined accepted theorem has the unqualified form:

**Every integral quartic in P3 containing C0 whose normalization is
smooth is excluded as a carrier for a set-theoretic complete-intersection
mate of every positive degree, over an algebraically closed field
of characteristic zero.**

More generally, every remaining nonnormal integral quartic carrier
with a hypothetical mate has normalization sectional genus pi in
{1,2}, and its unique smooth lift c meets Sing(S). There is no separate
generically-singular-along-C0 integral-quartic lane. Other carrier
degrees and the unrestricted STCI problem remain outside this result.
