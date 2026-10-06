# Independent audit of the uniform entirely-thick numerical restriction

Date: 2026-10-06. Status: **proved necessary condition**, independently
derived from the blowup intersection identities; a further **proved
conditional boundary reduction** is included below. Neither assertion
excludes the entire thick branch. No claim of novelty is made.

## Hypotheses and properness

Work over an algebraically closed field of characteristic zero. Let
`C ⊂ P³` be a smooth nondegenerate rational quartic, lying on its smooth
quadric `Q`, with ruling convention `C=(1,3)`. The checked normal bundle is
`N_(C/P³)=O_P¹(7)⊕O_P¹(7)`.

Suppose homogeneous forms `F_a,G_b` have reduced common projective support
exactly `C`. Write their exact generic normal orders along `C` as `p,q`;
the entirely-thick branch has `p,q≥2`. The argument works for arbitrary
positive `p,q` and does not require either surface to be integral.

The two forms have no common irreducible surface factor, since that factor
would be a component of their common zero support. Neither is divisible by
the quadric equation: if one were, its common zero set with the other would
contain the zero divisor of the other's restriction to `Q`, which cannot
have support `C` alone because `(b,b)` is not a positive multiple of
`(1,3)`. A restriction identically zero on `Q` also gives a common surface.

Consequently `F|Q=h^p R_F` and `G|Q=h^q R_G`, where `h=0` cuts out `C`
on `Q`, and the nonzero residual sections have classes

    R_F ∈ H⁰(Q,O_Q(a-p,a-3p)),
    R_G ∈ H⁰(Q,O_Q(b-q,b-3q)).

The displayed exponents need not be the exact orders on `Q`: a residual
section can itself be divisible by `h`. They imply `a≥3p,b≥3q` nonetheless.

Put `B=Bl_C P³`, let `H` be the hyperplane pullback, and let `E` be the
exceptional divisor. The strict transforms are effective Cartier divisors

    D=aH-pE,  D'=bH-qE.

They have no common surface component, so their scheme intersection is a
proper Cartier complete intersection on the smooth threefold `B`. It is
Cohen--Macaulay and pure of dimension one. Its fundamental cycle `W=D·D'`
is effective. The blowup is an isomorphism off `E`, and the original
equations have no common point off `C`; hence the entire scheme
intersection, and in particular its cycle, is supported in `E`.

This addresses possible hidden issues: nonreduced surface equations and
vertical exceptional components are allowed; an embedded zero-dimensional
component does not arise in this Cartier complete intersection. In any
event, a zero-dimensional component could not change the cycle numerics.

## Independent numerical derivation

Use the same bidegree convention as P-020:

    E≅P¹×P¹,
    H|E=O_E(4,0),  E|E=O_E(7,-1),
    H³=1,  H²E=0,  HE²=-4,  E³=-14.

Write the class of the effective curve cycle on `E` as `(u,v)`. The two
intersection numbers determine this class, because

    H·W=4v,
    E·W=7v-u.

Direct expansion in the blowup gives

    H·D·D' = ab-4pq,
    E·D·D' = 4(aq+bp)-14pq.

Therefore

    v = ab/4-pq,
    u = 7ab/4+7pq-4(aq+bp).                         (T1)

Every irreducible effective curve on `P¹×P¹` has nonnegative bidegrees.
Taking positive cycle multiplicities preserves this property, including
for vertical fibers. Thus an STCI pair must satisfy

    ab≥4pq,
    7ab+28pq≥16(aq+bp).                            (T2)

With `α=a/p,β=b/q`, the second inequality reads

    7αβ/4+7≥4(α+β),  α,β≥3.                       (T3)

For `α=3`, it forces `β≥4`; by symmetry, `β=3` forces `α≥4`.
In particular every pair with both `a=3p` and `b=3q` is excluded, at all
normal orders. For `a=b=6,p=q=2`, the formula gives `(u,v)=(-5,5)`,
recovering the thick-sextic contradiction in P-018.

The inequality does not give an upper bound on `p,q,a,b` and does not
exclude the region of large degree-to-order ratios. Its proof does not
assume any bound on later normal jets or local contact multiplicity.

## Further consequence at numerical equality

Assume now the boundary values

    a=3p,  b=4q.

Then `(T1)` gives `(u,v)=(0,2pq)`. Every irreducible curve in the support
of `W` therefore has class `(0,1)`: these are constant sections of the
exceptional `P¹`-bundle over `C`. Let their distinct supports be
`T₁,...,T_r`. There are no vertical components in this equality case.
Restriction of each strict-transform divisor to `E` gives

    D|E=(5p,p),  D'|E=(9q,q).

Every `T_j` is a component of both restricted divisors. Fiber degree
therefore bounds the number of distinct sections:

    r≤min(p,q).                                    (T4)

The quadric-direction section is `S_Q=Q^strict∩E`, with class `(1,1)`.
Each `T_j` meets `S_Q` in exactly one reduced point: geometrically `S_Q`
is the graph of a degree-one automorphism from the base to the normal
direction projective line, and `T_j` has constant direction.

Here

    R_F has class (2p,0),
    R_G has class (3q,q).

Thus `R_F` is a binary form of degree `2p` in the coordinate indexing the
trisecant ruling lines of `Q`. Consider one distinct ruling component
`ℓ` of `R_F`. It is contained in `V(F)`. The restriction `G|ℓ` is
nonzero, or else `ℓ` would be an extra common curve. Equivalently
`R_G|ℓ` is a nonzero section of `O_ℓ(q)`. Since `q>0`, it has a zero
`P`. The STCI support condition forces that zero to lie in `ℓ∩C`,
because `G|ℓ=(h|ℓ)^q(R_G|ℓ)` and every zero of `G|ℓ` must lie in `C`.

Let `P̃` be the point of `S_Q` above `P`. The restriction of the
`p`-th normal form of `F` to `S_Q` is exactly `R_F|C`; its value at `P`
is zero. Similarly the restriction of the `q`-th normal form of `G` is
`R_G|C`, so its value at `P` is zero. Hence

    P̃∈D∩D'∩S_Q.

This conclusion also holds if `h|R_G`, in which case the latter normal
form vanishes identically on `S_Q`. It only uses divisibility by `h^q`,
not the assertion that `q` is the exact order of `G|Q` along `C`.

Purity of the Cartier intersection makes every point of `D∩D'` belong
to its one-dimensional support, which here is `T₁∪...∪T_r`. Each `T_j`
supplies only one point on `S_Q`. Distinct ruling lines of this family are
disjoint, so distinct components `ℓ` require distinct such points. Thus

    R_F has at most r≤min(p,q) distinct ruling roots. (T5)

The multiplicities sum to `2p`; at least one root therefore has
multiplicity at least `ceil(2p/min(p,q))`. This is a repeated-root
reduction on the equality boundary, not a contradiction or a construction.
It does not use the split/content-free/no-vertical assumptions of P-020.

If one additionally assumes the first-normal divisor of `F` has no
vertical component, then `r=p` is impossible: factoring off `p` constant
sections leaves an effective divisor of class `(5p,0)`, which is a nonzero
union of vertical fibers. Under that additional hypothesis `(T4)` can be
strengthened to `r≤min(p-1,q)`.

## Why first tangent forms cannot cap the cycle multiplicities

Over the generic coefficient field `K=k(C)`, fix normal orders `p=q=2`.
For any integer `n≥1`, take the two local equations

    f=y²+x^(2n+1),
    g=y²+2x^(2n+1)

in `K[[x,y]]`. In characteristic zero both germs are irreducible, since
the exponent `2n+1` is odd. They have the same first tangent polynomial
`y²` and reduced common support the origin. Subtracting their equations
gives the exact transverse length

    length K[[x,y]]/(f,g)=2(2n+1)=4n+2.

On the blowup chart `y=xz`, the strict-transform equations are

    f'=z²+x^(2n-1),
    g'=z²+2x^(2n-1).

Their intersection is supported at the same exceptional tangent direction,
with exact length

    length K[[x,z]]/(f',g')=2(2n-1)=4n-2.

Thus the excess over the product `pq=4` is arbitrarily large while the
normal orders and first tangent forms remain fixed. This directly
invalidates any inference that the coefficient of a common tangent
component in `W` is bounded by its multiplicity in the two first-normal
divisors. The effective-cycle proof of `(T1)--(T3)` never makes that
inference. These are local models, and no claim is made that they
globalize to projective STCI pairs on the quartic.

## Relation to the existing normalization frontier

P-019 and P-020 give sharper necessary conditions for a thick sextic under
specified branching hypotheses, and P-027 closes the smooth-normalization
clean-conductor case. None of those hypotheses follows from the cycle
effectivity argument above. P-032 still requires an effective Cartier
divisor on the full normalization, numerical/linear equivalence to a
hyperplane multiple, and section descent through the full conductor
square. The new cycle inequality and equality-root reduction supply
necessary restrictions before that descent analysis; they do not remove
its non-Cartier, extra-conductor, or higher-contact loopholes.
