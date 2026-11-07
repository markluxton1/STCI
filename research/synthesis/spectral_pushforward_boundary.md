# Singular spectral roots and the boundary of the torsion detector

**Status.** Independently reviewed extension on
`codex/spectral-realization-2026-10-31`, based on consolidation `fd50fb6`. This is
an intrinsic classification of pushforward bundles for full basepoint-free
(2,2) root schemes, in every characteristic. It does not extend the actual
smooth-root-to-CI bridge to singular roots.
The [power theorem and coefficient maps](spectral_pushforward_powers.md)
provide the notation and smooth case.

## 1. The full root and its possible components

Let k be algebraically closed, and let

    f=a(z)u^2+b(z)uv+c(z)v^2

have quadratic base coefficients with no common zero. Then
Z=V(f) in P1_base x P1_direction is an effective Cartier divisor of
bidegree (2,2) with no vertical component. Its first projection pi is
finite flat of degree two, even when Z is singular or nonreduced.
Set A=O_Z(1,0), B=O_Z(0,1), eta=B tensor A^-1, and E_n=pi_*B^n.

Every reduced irreducible component has bidegree (a_i,b_i), with a_i>=0
and b_i>0, because a component with b_i=0 would be vertical. The total
second degree is two. Consequently precisely the following cases occur:

1. Z is integral, possibly singular.
2. Z=D1 union D2, with two distinct components of class (1,1).
3. Z=D0 union D2, with classes (0,1) and (2,1).
4. Z=2D, with D of class (1,1).

In the reducible cases each component is the graph of a morphism from
the base, since it has degree one over that base; hence it is smooth.
The two components meet in a scheme of length two. This scheme may be
supported at one point. In case 4, D is the graph of an automorphism.
There are no additional embedded components: Z is a Cartier divisor on
a smooth surface, and its homogeneous equation has the indicated factors.

The sequence

    0 -> O(-2)^(n-1) -> O^(n+1) -> E_n -> 0                       (1)

holds for every n>=2 in all four cases. In particular E_n is globally
generated, of rank two and degree 2n-2. Also H0(O_Z)=k, by the
restriction sequence from O(-2,-2) to O on the product.

## 2. The balanced cases retain the torsion criterion

In cases 1, 2 and 4, for every n>=2,

    E_n = O(n-1)^2                  if eta^n != O_Z;
    E_n = O(n-2) + O(n)             if eta^n = O_Z.                (2)

It suffices to show that a nonzero section of eta^n trivializes it.
Then H0(eta^n) has dimension zero or one, and the degree/splitting
argument in the power theorem applies without change.

For integral Z, define degree by Euler characteristic. A nonzero section
of a degree-zero invertible sheaf is injective from O_Z, with finite
length cokernel. Equality of Euler characteristics gives length zero.
This proof needs neither smoothness nor normalization of Z.

For two (1,1) components, eta has degree zero on each P1, so eta^n
restricts trivially to each. A section restricts to two constants after
choosing these trivializations. If either constant is zero, gluing across
the nonempty intersection forces the other to be zero. A nonzero section
is nonzero on both components and at every closed point, so it is a unit
locally and trivializes eta^n. This includes tangential intersections;
no replacement of the full length-two intersection by its support occurs.

For Z=2D, the square-zero ideal J=I_D/I_D^2 is O_D(-2), and eta|D=O_D.
The sequence

    0 -> O_D(-2) -> eta^n -> O_D -> 0

shows that a nonzero section restricts to a nonzero constant, since
H0(O_D(-2))=0. It is therefore a unit on the full double structure.
In particular the nilpotent information is retained in (2).

Thus the coefficient determinant D_n and kernel construction from the
power theorem continue to detect and construct a spectral trivialization
in these three cases. For n>2, R-0008 then constructs the same abstract
graded CI family. Its full-root scope includes singular and nonreduced
schemes; the smooth actual-neighborhood bridge remains a different theorem.

## 3. The unbalanced reducible exception

In case 3, eta has degrees -1 and +1 on D0 and D2. It is never torsion.
Let K=D0 intersect D2, a length-two scheme. The exact gluing sequence
for eta^n shows that a global section is zero on D0 and restricts on
D2 to a section vanishing on K. Hence, for n>=2,

    h0(Z,eta^n)=h0(D2,O(n)(-K))=n-1.                             (3)

As E_n is globally generated of degree 2n-2, (3) forces

    E_n=O + O(2n-2),  W_n=E_n^*=O + O(2-2n).                    (4)

Indeed, write E_n=O(e1)+O(e2), 0<=e1<=e2, e1+e2=2n-2. Only
the larger summand can contribute to H0(E_n(-n)); its contribution
e2-n+1=n-1 gives e2=2n-2 and e1=0.

The square coefficient matrix C_(f,n) therefore has corank n-1 in this
entire stratum, although eta has infinite order. At n=2 the corank is
one, exactly as on a genuine torsion root: corank one alone is not a
boundary torsion certificate. Its kernel produces sections supported
on D2 and vanishing on D0, so none is a unit on the full root. It
cannot supply a fiberwise coprime second relation by R-0008.

An explicit example valid in every characteristic is

    f(s,t;u,v)=u(s^2*u+t^2*v).                                   (5)

Its coefficients s^2,t^2,0 have no common base zero. The components
meet at t=0 with length two, illustrating that (3) is scheme-theoretic.
All D_n vanish on this example, but no positive power of eta is trivial.

For n>=3, the full-root corank distinguishes the exceptional case:
it is at least two exactly on case 3, while the other cases have
corank zero or one. This is a complete statement under the no-vertical-
component hypothesis, not a classification of arbitrary normal initial ideals.

There is also a direct parameter-space consequence: for every n>=3,
the hypersurface D_n=0 is singular at every root of case 3. All
codimension-one cofactors of C_(f,n) vanish when its corank is at
least two, so every coefficient derivative of its determinant vanishes.
This proves singularity, without asserting an exact vanishing multiplicity
or a scheme-theoretic identification with a torsion locus. At n=2 the
coefficient map is the unrestricted 3-by-3 coefficient matrix with rank
two, so its determinant hypersurface is smooth at these roots instead.

## 4. The doubled graph records characteristic directly

In case 4, change the direction coordinate by the graph automorphism
to identify D with the diagonal. This is an isomorphism of the abstract
root geometry; it is not claimed to preserve a fixed ambient obstruction.
Let x be the base coordinate, y the direction coordinate and e=y-x.
On the double diagonal e^2=0. The restriction eta=O(-1,1)|2D has
transition ratio, up to the inverse convention,

    y/x=1+e/x.

The class e/x generates H1(D,O_D(-2)): in the two standard charts,
the normal coordinate changes by e'=-e/x^2, and the Laurent class x^-1
is the unique surviving Cech coefficient for O(-2). Thus eta is the
nonzero additive class in the kernel of Pic(2D)->Pic(D).
Since e^2=0, raising this transition to n gives 1+n*e/x. Therefore

    eta^n=O_2D  iff  n=0 in k.                                  (6)

In characteristic zero every E_n is balanced. In characteristic p,
the splitting jumps exactly at multiples of p; for those n>2 a
kernel actually gives a unit on the full nonreduced root and hence an
abstract graded family. This is compatible with the already retained
[prime-to-characteristic full-root obstruction](../supplements/FIRST_RELATION_AND_SPECTRAL_ROOTS.md#prime-to-characteristic-spectral-descent-excludes-repeated-moving-components).
Its positive-characteristic double-diagonal control is inherited;
the consequence for all pushforward powers is the present application.

## 5. Constant target dimension despite changing generators

For every root above, every n>=2 and every integer q>=2n-3, the
listed splittings give

    H1(W_n(q))=0,  h0(W_n(q))=2q-2n+4.                           (7)

The bound includes the extreme summand O(2-2n) in (4). In particular,
at n=4,q=10 the dimension is sixteen in all cases. The original global
25-generator presentation consequently has no dimension jump to repair;
the degrees and interpretation of its minimal generators can change.
This recovers a consistency check on the existing full-root dual model,
without extending its ambient obstruction interpretation to other n,q.

## Review and remaining parameter-space question

Independent review on 2026-10-31 by `review_spectral_boundary` (GPT-6.1 Sol,
high reasoning) reconstructed the exhaustive component list, singular
degree-zero argument, full gluing including tangency, nonreduced Picard
calculation, all three splitting types, false-positive example and determinant
singularity consequence. The review also checked the full-root graded
construction against R-0008 and its retained audit. No material error or
unresolved proof gap was found. No mathematical computation was needed or run.

The theorem classifies geometric fibers of the coefficient matrices. The
[smooth-root scheme continuation](spectral_determinant_schemes.md) identifies
the determinant with the relative Picard torsion scheme and constructs a
universal graded family there. Scheme structure along singular roots,
including the unbalanced stratum, remains open here. The existing
normal-source, actual-neighborhood and
projective-support hypotheses remain separate.
