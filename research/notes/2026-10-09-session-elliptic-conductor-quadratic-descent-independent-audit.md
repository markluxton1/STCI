# Independent audit: quadratic descent across an elliptic conductor

**PROVED conditional exclusion, in characteristic zero.** The argument below
excludes every mate for a carrier satisfying all the listed hypotheses. It
does not assert that these hypotheses cover every singular normalization, or
that the requisite section `Q` always exists.

Let `nu:S -> X` be the finite normalization of an integral quartic surface
`X` in `P3`, with `S` normal and `H=nu^*O_X(1)`. Assume:

1. A smooth rational curve `c` maps isomorphically to the fixed smooth rational
   quartic `C0`.
2. A global section `Q` of `O_S(2H)` has Weil divisor exactly `2c`.
3. The **actual** downstairs conductor scheme `Gamma` is a smooth conic.
4. The **actual** upstairs conductor scheme `D` is a smooth integral elliptic
   curve, avoids `Sing(S)`, and maps finite flat of degree two to `Gamma`.

The conductor scheme hypotheses, not merely equality of conductor supports,
are needed for the fiber-product descent step.

## A hypothetical mate has the required divisor

Suppose an ambient form `G` of degree `b` is a mate, so its zero support on
`X` is precisely `C0`. The restriction is nonzero. Since `C0` is not the
degree-two conductor curve, its generic point is outside the conductor;
there the normalization is an isomorphism. Every curve in `nu^{-1}(C0)`
dominates `C0` under the finite map, so `c` is the only such curve. All points
of the inverse image away from `c`, if any, are isolated in that inverse
image. Such points already contradict the zero support of a nonzero Cartier
section on the normal surface `S`.

Therefore a hypothetical mate forces
`div_S(nu^*G)=m*c` for some positive integer `m`. Intersecting with `H` gives

\[
4b=bH^2=m(H\mathbin{\cdot}c)=4m,
\]

so `m=b`. Thus `div_S(nu^*G)=b*c` follows from the mate and conductor
hypotheses; it need not be separately assumed as a generic-order statement.

The sections `(nu^*G)^2` and `Q^b` of the same invertible sheaf have identical
Weil divisors. Their ratio has no divisorial zeros or poles, so it is a unit
on the normal projective integral surface, hence a nonzero constant. Thus

\[
(\nu^*G)^2=\lambda Q^b,\qquad \lambda\in k^\times.
\]

## Even valuations exclude the anti-invariant case

Write `p:D -> Gamma` for the conductor map and `q=Q|D`. This is a nonzero
section because `D` is not the rational curve `c`. The invertible sheaf
`O_S(2H)|D` is naturally `p^*O_Gamma(2)`, and its pullback linearization gives
a canonical action of the double-cover involution `sigma` on `q`.

The displayed power identity shows that `q^b` is invariant: its restriction
comes from the downstairs section `G^2|Gamma`, up to the scalar `lambda`.
Hence the rational function `sigma(q)/q` has `b`th power one. In the function
field of the integral curve over the algebraically closed field this means
`sigma(q)/q=zeta` for a constant root of unity. Applying `sigma` twice gives
`zeta^2=1`, so `sigma(q)=q` or `sigma(q)=-q`.

Riemann--Hurwitz gives four ramification points for the separable degree-two
map from the elliptic curve to the smooth conic. At any ramification point,
choose a frame pulled back from `O_Gamma(2)`; it is invariant. In completed
local coordinates, the involution acts by `z -> -z`. An anti-invariant
section then has an odd power series and therefore an odd vanishing order.

On the other hand, `S` is smooth along `D`. Near any point of `D`, the
divisor identity `div_S(Q)=2c` makes `Q` a unit times the square of a local
equation of `c` (or a unit if the point is not on `c`). Its nonzero restriction
to the smooth curve `D` has even vanishing order. This includes tangential
intersections: the local intersection multiplicity is simply multiplied by
two. The anti-invariant possibility is therefore impossible. Consequently
`q` is invariant and descends to a section `qbar` of `O_Gamma(2)`.

## The actual conductor square gives global descent

For the actual conductor ideal `I`, the inclusion of local rings `A` in its
normalization `B` satisfies

\[
A=B\times_{B/I} A/I.
\]

This is literal: a member of `B` whose residue modulo `I` lies in `A/I`
differs from a member of `A` by an element of the common ideal `I`, hence
lies in `A`. Sheafifying and tensoring by the invertible sheaf `O_X(2)` gives

\[
0\longrightarrow O_X(2)
\longrightarrow \nu_*O_S(2H)\oplus O_\Gamma(2)
\longrightarrow p_*O_D(2H)\longrightarrow0.
\]

The pair `(Q,qbar)` is compatible on `D`, so left exactness of global
sections produces a global section of `O_X(2)` whose pullback is `Q`.
There is no additional `H1` obstruction to this compatible-pair descent.
The hypersurface sequence

\[
0\longrightarrow O_{P^3}(-2)\longrightarrow O_{P^3}(2)
\longrightarrow O_X(2)\longrightarrow0
\]

and `H1(P3,O(-2))=0` lift that section to an ambient quadric `K`.

## The fixed-curve quadric obstruction

The pullback of `K|X` has zero support exactly `c`; finite surjectivity of
`nu` therefore says that the zero support of `K|X` is exactly `C0`. This
support argument avoids any need to exchange intersection multiplicities
between the two surfaces.

The fixed curve `C0=[u^4:u^3v:uv^3:v^4]` has the unique ambient quadric
`rt-pq=0`. Indeed the ten degree-two coordinate monomials give the nine
binary monomials of degree eight, with only `rt` and `pq` coinciding. This
quadric is smooth, and `C0` has ruling class `(1,3)`, up to swapping the
rulings.

The nonzero quartic restriction `F|K` is an effective divisor of class
`(4,4)` supported only on this integral curve. Its degree is eight, so it
must equal `2C0`. But subtracting that divisor class leaves

\[
(4,4)-2(1,3)=(2,-2),
\]

which has no nonzero section on `P1 x P1`. Equivalently `(4,4)` is not the
class `2(1,3)`. This contradiction proves the conditional all-mate exclusion.

Audit outcome: global descent, parity at ramification, the passage from the
Weil divisor to local squares along the smooth conductor, and the final
quadric obstruction are all valid with the hypotheses stated above. The
existence of `Q` and the actual smooth conductor conditions remain hypotheses
to establish for each proposed carrier family.
