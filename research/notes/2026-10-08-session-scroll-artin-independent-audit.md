# Independent audit of the nonreduced scroll-conductor Artin reductions

Date: 2026-10-08. Status: **ACCEPTED independent proof audit**, under
the exact smooth-scroll normalization and full-support hypotheses.
This file audits the written proof in
[nongorenstein cubic classification](2026-10-08-session-scroll-nongorenstein-cubic-classification.md)
and records a direct completion for the double-line-plus-line case.
It makes no canonical frontier edits and no global STCI assertion.

## 1. Exact generic module and entire multiplicities

The canonical conductor sequence is

    0 -> A -> B -> omega_A -> 0

at each actual generic conductor scheme point. B is the product of
truncated DVR algebras along the conductor primes on smooth S.
Each multiplicity a is the actual Cartier-divisor multiplicity of D;
each residue extension degree r is the degree of that prime over the
support line. Characteristic zero makes the residue extensions
separable. This formulation does not approximate D or Gamma by their
reduced support.

The proper-prime cohomology argument makes every conductor prime a
smooth rational curve. All uses of c~H and the singleton-fiber
condition rely on the entire normalization inverse image, and not on
a generic fiber alone.

## 2. Curvilinear triple line

For A=K[epsilon]/epsilon^3, omega_A is free of rank one. Thus B is
free of rank two over A and multiplication by epsilon has K-rank four.
In a factor K_i[t]/t^a, write k=ord(epsilon). Its image rank is
r(a-k), while epsilon^3=0 implies a<=3k. Summing over factors gives
the upper bound four; equality forces a=3k in every factor. A factor
with epsilon=0 would make the inequality strict and cannot occur.
Every coefficient of the actual D is divisible by three. This
contradicts D~2C+(e+2)f in Pic(F_e), e=0 or 2.

This excludes the curvilinear triple-line conductor before assuming
a mate. The proof requires no plane-curve delta classification.

## 3. Fat triple line

For A=K+N, dim N=2,N^2=0, multiplication by N on omega_A has image
dimension one. NB contains N, and NB intersect A equals N: the ideal
NB is square-zero, so it cannot contain a nonzero scalar, and it
already contains both nilpotents of A. Its image in B/A is N omega_A.
Therefore dim_K NB=3 and dim_K B=6.

Each truncated DVR factor is Frobenius over K, using the field trace
of the top t-coefficient. Thus dim Ann_B(NB)=3. Since (NB)^2=0,
NB is its own annihilator. In each factor NB=(t^k), whose annihilator
is (t^(a-k)); equality makes a=2k. This proves every actual D
coefficient even.

The resulting half-conductor classes are C+f on F0 and C+2f on F2.
Their effective prime decompositions in the source note are exhaustive.
The irreducible degree-three case is excluded by the elementary
Riemann--Hurwitz/singleton-fiber obstruction. In the F0 two-component
case, pulling the sole zero of the degree-one prime's section to
the degree-two prime produces a double zero at one totally ramified
point; immersion of c forces intersection one there, a contradiction.
On F2 two distinct fiber components have proportional restrictions
and disjoint paired zeros, again contradicting singleton fibers.

The residual pattern 2C_min+4F has NB_F=(t^2). Both ambient normal
coordinates to the support line consequently vanish to order at
least two on F. The longitudinal coordinate has nonzero differential
since F maps isomorphically to the line, so nu has generic rank one
there. The
[independently audited differential lemma](2026-10-08-session-normalization-differential-independent-audit.md)
excludes a mate, including at special junctions with other conductor
components. This validates the entire fat-line exclusion.

## 4. Direct Artin completion for double-line-plus-line support

At the doubled support line L, A=K[epsilon]/epsilon^2, and B is free
of rank two. Its total K-length is four and multiplication by epsilon
has rank two. Writing epsilon=t^k in each factor gives k>=a/2,
and the total rank equality makes a=2k in every factor. The only
patterns are

    (a,r)=(4,1), (2,2), or (2,1)+(2,1).

At the reduced other line M, the rank-two algebra has patterns

    (a,r)=(2,1), (1,2), or (1,1)+(1,1).

A (4,1) factor over L has epsilon order two, so both ambient normal
coordinates to L vanish to order at least two on its prime; the
conductor ideal there vanishes to order four and does not change
this conclusion. The differential lemma excludes it. Similarly,
a doubled (2,1) factor over M has all ambient normal coordinates
in the actual conductor ideal (t^2), and is excluded by the rank-one
differential lemma. These exclusions are geometric consequences of
the whole Artin algebra, not a discarded nonreduced cover.

On F0, the only degree-two prime is horizontal C, and the degree-one
primes are fibers. The split thick-line case would use four fiber
multiplicities, exceeding D~2C+2f. Thus the cover over L is 2C.
The residual 2f over M cannot be the excluded doubled fiber and
cannot be one degree-two prime in a fiber class. It must be two
distinct fibers of multiplicity one, mapping to the same line.
Their proportional sections have disjoint paired zeros, excluding
a mate.

On F2 there is no degree-two prime. The cover over L is either
2C_min+2F or 2F1+2F2. The former leaves 2f over M, which again must
be two distinct fibers and is excluded by paired zeros. The latter
leaves 2C_min over M. It cannot be the excluded doubled prime,
one absent degree-two prime, or two distinct primes in the unique
C_min class. Therefore no mate exists in this case either.

The argument is valid at a nongorenstein intersection point, since
it uses no trace involution there. It avoids the earlier extra
square-descent obligation. Together with the accepted all-reduced
case and the two triple-line reductions, this supplies the proposed
full smooth rational quartic-scroll carrier exclusion. Promotion of
that combined theorem should use the written classification and the
independent differential audit together; it does not assert that
every nonnormal quartic has such a smooth scroll normalization.
