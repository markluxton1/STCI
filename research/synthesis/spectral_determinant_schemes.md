# Spectral determinant schemes and universal graded families

**Status.** Independently reviewed extension of the
[power theorem](spectral_pushforward_powers.md).
The base checkpoint is `c491ec2`. No actual embedded
realization is asserted. Throughout k is algebraically closed, in any
characteristic, and n>=2.

## 1. The scheme detected by the coefficient matrix

Let U be the open affine cone of nonzero equations f of smooth (2,2)
divisors in P1_base x P1_direction. Write q:Z->U for the universal
curve, A=O_Z(1,0), B=O_Z(0,1), and eta=B tensor A^-1. Let J=Pic^0(Z/U),
with identity section e, and let sigma_n:U->J be the section [eta^n].
The determinant D_n is that of the (n^2-1)-square coefficient matrix
C_(f,n) from the power theorem.

**Theorem.** There is an equality of closed subschemes of U,

    V(D_n) = sigma_n^-1(e).                                      (1)

This includes nilpotent parameter directions. Equivalently, the ideal
(D_n) is Fitt_0 R^1 q_*(eta^n). The equation descends to the smooth-root
open in P8; its local ideals are independent of the scalar chosen for f.

First, the matrix is a cohomology presentation in families. Put
E_n=pi_*B^n on P1_base x U. The universal divisor sequence gives

    0 -> O(-2)^(n-1) -> O^(n+1) -> E_n -> 0.

On this affine coefficient cone det E_n=O(2n-2), with a frame fixed by
the displayed source and target bases. Rank-two duality gives
E_n^*(n-2)=E_n(-n). Dualizing and twisting the sequence, then taking
base-P1 cohomology, therefore represents R q_*(eta^n) by

    [ O_U^(n^2-1) --C_(f,n)--> O_U^(n^2-1) ]                    (2)

in degrees zero and one. The two intermediate P1 bundles have no higher
cohomology. This description is compatible with arbitrary base change,
including a nonreduced parameter base. The determinant is the zeroth
Fitting ideal of the cokernel. On projective coefficient space parameter
line-bundle factors occur; local frames suffice for the same ideal claim.

It remains to identify that Fitting ideal with the Picard identity scheme.
Etale locally on U choose a section x of the smooth genus-one family.
For a relative degree-zero invertible sheaf L, the sequence

    0 -> L -> L(x) -> L(x)|x -> 0

represents R q_*L by the evaluation map between the line bundles
q_*L(x) and L(x)|x. This follows from degree-one Riemann--Roch and
cohomology/base change: L(x) has fiber h0=1 and h1=0.

Apply this on the relative Picard curve with its normalized Poincare
bundle. Identifying that Picard curve with the elliptic curve using x,
the degree-one bundle L(x) is O(Gamma) up to a parameter-line twist,
where Gamma is the graph of the varying Picard point. Its canonical
section vanishes exactly on Gamma. Evaluation at x consequently cuts
out the identity section with its ordinary Cartier scheme structure,
not a multiple of that section. Pull back along sigma_n. Fitting ideals
commute with base change, and twisting by a parameter line does not change
them. This proves (1).

The inputs concerning Picard schemes and Fitting ideals are standard;
the comparison with the explicit convolution matrix is the assertion here.
See [Stacks, fixed-curve Picard background](https://stacks.math.columbia.edu/tag/0BA0)
and [Stacks, Fitting ideals](https://stacks.math.columbia.edu/tag/07Z6).
The relative evaluation argument is given above, rather than attributed
to the fixed-curve reference.

## 2. Smoothness and intersections, with exact characteristic scope

If n is invertible in k, V(D_n) is a smooth reduced divisor of the
smooth-root parameter open. At a point with eta^n=O, fix the elliptic
curve and A, and vary B in Pic^2. Degree-two section spaces remain rank
two; after choosing local frames their product maps remain closed
immersions on an open neighborhood. They give actual coefficient
deformations. The variation of eta is the free Picard direction, and
the derivative of [n] in that direction is multiplication by n.
By (1), a local equation for D_n has a nonzero derivative there.

This argument does not require a choice of origin satisfying A=O(2x),
so it also covers characteristic two when n is odd. It supplies no
transversality to an actual embedded compatibility locus.

There is also a scheme-theoretic strengthening of the gcd rule. For
m,n>=2 and d=gcd(m,n),

    V(D_m) intersect V(D_n) = V(D_d)                             (3)

as closed subschemes on the smooth-root open; for d=1 the right side
is empty. Locally the ideal equality is (D_m,D_n)=(D_d), with D_1=1.
Indeed [m]eta and [n]eta vanish over any test scheme precisely when
[d]eta vanishes: Bezout expresses d as an integral combination of m,n,
and both m,n are multiples of d. Thus the corresponding elliptic
subgroup schemes intersect in J[d], and (1) gives (3). In particular,
if d divides n, the local divisor equation D_d divides D_n.

These are identities on the smooth open. They are not unsaturated
polynomial ideal identities on the full coefficient space: the
[unbalanced reducible roots](spectral_pushforward_boundary.md#3-the-unbalanced-reducible-exception)
already violate the geometric gcd interpretation there.

## 3. What multiplicity means in positive characteristic

Fix an elliptic curve E and a degree-two bundle A, vary the nonzero
point eta in Pic^0(E), and set B=A tensor eta. Locally choose frames
of both linear systems to obtain a family of smooth (2,2) equations.
On this fixed-curve parameter family, (1) identifies the divisor with
E[n] away from the identity, including its multiplicities.

Write n=p^r m, with p not dividing m, in characteristic p. At every
geometric n-torsion point that remains in this family, its multiplicity is

    p^r       if E is ordinary;
    p^(2r)    if E is supersingular.                            (4)

When r=0 these both equal one. To see (4), factor [n] into a purely
inseparable isogeny followed by a separable isogeny. The latter is etale;
the former has local degree p^r or p^(2r), respectively. Translation
by a geometric kernel point identifies its local multiplicity with
that at the identity. For the separable/inseparable degree facts see
[MIT elliptic-curves lectures, Lecture 13](https://math.mit.edu/classes/18.783/2022/LectureSlides13.pdf).
If E is supersingular and m=1 there are no nonidentity geometric points
to retain; this gives an empty fixed-curve locus, not extra smooth roots.

These fixed-curve multiplicities must not be identified with multiplicities
of every component in the total coefficient space. Varying the elliptic
curve can change the local equation. For example, in characteristic two,
D_2 is the unrestricted 3-by-3 coefficient determinant. At every smooth
root where D_2=0 that matrix has rank two, so its determinant hypersurface
is smooth. Its restriction to the fixed ordinary elliptic curve has
multiplicity two by (4). Thus corank one and fiberwise nonreduced torsion
do not imply a singular or nonreduced total determinant hypersurface.

## 4. A family of graded complete intersections over the torsion scheme

Put T_n=V(D_n) inside U and restrict the coefficient matrix to T_n.
Every geometric fiber has corank exactly one. Near each point an
(n^2-2)-minor is a unit; row and column operations put C_(f,n) into
the form diag(I,t), with t a unit times D_n. On T_n this is diag(I,0),
even when T_n is nonreduced. Its kernel K_n is therefore a line bundle
on T_n, rather than a chosen nowhere-zero vector on the whole parameter
space. By (2), K_n=q_*(eta^n) on that restricted family.

The evaluation map

    q^*K_n -> eta^n                                             (5)

is an isomorphism: on each geometric fiber its nonzero section is
nowhere zero, and a morphism between invertible sheaves which is a unit
on every residue field is a unit. Formula (5) gives a universal relative
spectral trivialization, retaining the parameter-line factor K_n.

For n>2, fix a line bundle H on P1_base. On P1_base x T_n set

    E=H^-1 tensor k^2,  R=H^-2 tensor O(-2),
    Q_n=(Sym E/(R))_n=H^-n tensor pi_*B^n,
    T=H^-n tensor O(n) tensor pr_T^*K_n.

Adjunction from (5) embeds T in Q_n as a line subbundle. Form the
ideal generated by T in Sym E/(R), then its inverse image in Sym E.
This gives a finite locally free graded algebra of rank 2n over
P1_base x T_n, with geometric fibers complete intersections of type
(2,n). Locally a generator of T lifts to a polynomial g_n; its value
is a unit on the full length-two root fiber, so (f_2,g_n) is coprime.
The degreewise Koszul complex is exact on all residue fields. Its
maps consequently split locally in each degree, showing that the
graded pieces are locally free, also over nonreduced parameter bases.
They vanish above degree n, and their total rank is 2n.

This is the parameter-family form of the [R-0008 quotient-ideal construction](../results/spectral_root_picard_criterion.md).
It is compatible with base change. The kernel line avoids a global choice
of eigenvector; forgetting that line would discard gluing data. The
construction takes place on the normal-bundle model and does not identify
it with the actual embedded neighborhood of C0. No two global ambient
equations, support-preserving formal lift or projective pair follow.

## Review and remaining questions

Independent review on 2026-10-31 by `review_determinant_schemes` (GPT-6.1 Sol,
high reasoning) reconstructed the family cohomology complex, Picard evaluation
divisor, arbitrary-base-change assertion, characteristic scope, scheme gcd
identity and universal graded construction over nonreduced bases. It also
checked the distinction between fixed-curve fiber multiplicity and total
parameter-space multiplicity, and the primary-source scope. The review found
no material error or unresolved proof gap. The fixed-curve Picard citation
was relabeled to avoid attributing the relative proof to that narrower source.
A separate `spectral_determinant` continuation checked the varying-B tangent
argument in characteristic two and the fixed-curve/total-space distinction;
the earlier characteristic-zero origin-choice argument is not used there.
No mathematical computation was needed or run for this note.

The singular-root parameter schemes, multiplicities along their unbalanced
boundary, and a classification of total torsion-divisor geometry when p|n
remain beyond the present results. Actual embedded lifting is a separate
problem; the [fixed order-three example](spectral_pushforward_powers.md#6-testing-this-example-in-the-actual-embedding)
already fails its first ambient test despite lying on this positive graded
family. No projective realization follows.
