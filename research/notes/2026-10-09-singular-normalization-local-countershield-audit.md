# Singular-normalization countershield: independent audit

Status: **PROVED**, for an algebraically closed field of characteristic different
from 2. This example concerns a smooth degree-two curve, not the fixed rational
quartic `C0`. It prevents a general argument from excluding a singular point of
the normalization merely because the downstairs curve is smooth and has a
set-theoretic complete-intersection mate.

Let

\[
B=k[x,g,v]/(v^2-4xg),\qquad y=x+g+v,\qquad w=y^2,
\]

and put

\[
F=(w+(x-g)^2)^2-4(x+g)^2w,
\qquad A=k[x,g,w]/(F).
\]

The discriminant of `F`, viewed as a monic quadratic in `w`, is
`64*x*g*(x+g)^2`. It is not a square in `k(x,g)`: the valuations at the prime
elements `x` and `g` are odd. Thus `F` is irreducible, and substitution of
`w=(x+g+v)^2` embeds `A` in `B`. The kernel has height one and contains the
irreducible polynomial `F`, so it equals `(F)`.

The ring `B` is finite over `A`, generated as an `A`-module by `1,v`, since
`v^2=4xg`. It has the same fraction field because

\[
v=\frac{w-x^2-6xg-g^2}{2(x+g)}.
\]

The quadric cone `B` is normal: it is a hypersurface, hence Cohen--Macaulay,
and its singular locus consists only of the origin in this two-dimensional
surface. Therefore it satisfies Serre's `S2` and `R1` conditions. Consequently
`B` is exactly the finite birational normalization of `A`.

The prime divisor `c=(g,v)` has coordinate ring `k[x]`. Its image is
`C=(g,w-x^2)`, also with coordinate ring `k[x]`, and the restricted map is an
isomorphism. At the generic point of `c`, `x` is invertible and
`g=v^2/(4x)`, so `div_B(g)=2c`. At the origin the ideal `(g,v)` has two
independent generators modulo the maximal ideal times this ideal; it is not
principal. Hence `c` is non-Cartier at that point, and its local divisor class
has exact order two.

The **scheme-theoretic** inverse image of `C` is

\[
(g,w-x^2)B=(g,xv).
\]

Its radical is `(g,v)`, so its full support is precisely `c`. Its quotient is
`k[x,v]/(v^2,xv)`; the nilpotent `v` is supported at the origin. The claim is
about support, not equality with the reduced inverse-image scheme.

Differentiation gives `F_g|C=-16*x^3`. Thus `F` has order one along the generic
point of `C`, although the normalization is singular at the point over its
origin and the lifted curve is non-Cartier there.

Homogenize with coordinates `[x:g:w:t]`:

\[
F_h=(wt+(x-g)^2)^2-4(x+g)^2wt.
\]

The homogenization is irreducible because its dehomogenization is irreducible
and it is not divisible by `t`. Its plane section is exactly

\[
F_h\vert_{g=0}=(wt-x^2)^2.
\]

The conic `g=0, wt=x^2` is smooth, and the intersection scheme of the integral
quartic surface with the plane `g=0` is its double. The normalization over the
chart `t=1` is `Spec B`, so it really has a singular point above this smooth
conic. This gives a projective set-theoretic complete-intersection example,
with generic multiplicity two, rather than only a formal local model.

An independent SymPy calculation on 2026-10-09 verified the normalization
substitution modulo `v^2-4*x*g`, the displayed discriminant, the rational
inverse identity, `F_g|C`, and the squared conic plane section. All remainders
were zero where required. These calculations check identities; the arguments
above establish normality, finiteness, irreducibility, and divisor behavior.

No conclusion about the fixed degree-four curve `C0`, or the universal STCI
problem, follows from this example.
