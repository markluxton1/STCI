# Moving linear relations: exact quadratic obstruction and independent review

Date: 2026-10-14. Status: independently derived new compatibility calculation;
the accepted embedded quadratic transition is used as a premise. No previous
normal-bundle or constant-direction computation is repeated.

This note reviews the moving operator in Section 8 of
[the thick relation extension](2026-10-13-generalization-thick-equality-extension.md)
for a moving **linear** relation. The calculation gives an obstruction-zero
family, rather than an exclusion theorem.

## 1. Frames and the cohomology target

Write the actual conormal bundle as `E=O(-7)^2`. Let the relation line be
`W=O(-8)` with basepoint-free image

    f=a(z)u+b(z)v,
    a=A+Cz,  b=B+Dz,  Delta=AD-BC != 0.

On the second chart, `w=z^-1` on the reduced curve, the coefficient pair is
`a_1=Aw+C=z^-1 a`, `b_1=Bw+D=z^-1 b`. The normal frames satisfy
`u'=z^-7 u`, `v'=z^-7 v` to first order, and the relation frame satisfies
`W_1=z^-8 W_0`.

The quotient `M=E/W` is `O(-6)`. Locally its generator `q` is normalized by
`u -> b q`, `v -> -a q`. Since the second-chart coefficients have the extra
factor `z^-1`, its frame transition is `q_1=z^-6 q_0`. Thus the degree-two
relation obstruction has target

    Q=Hom(W, Sym^2 M)=O(-4),
    (q_1^2/W_1)=z^-4(q_0^2/W_0).

Consequently, evaluating the chart-zero quadratic discrepancy at
`(u,v)=(b,-a)` produces the coefficient in the chart-zero frame of `Q`, with
**no extra power of z**. Its Cech cohomology class retains exactly the
coefficients of `z^-1,z^-2,z^-3`. Nonnegative exponents are first-chart
coboundaries; exponents at most `-4` are second-chart coboundaries.

More generally, a basepoint-free linear relation of movement degree `e`
has `W=O(-7-e)`, `M=O(e-7)`, and

    Q=Hom(W,Sym^2 M)=O(3e-7).

For `e>=2`, `H^1(Q)=0`, so this one-step obstruction gives no exclusion.

## 2. Exact coefficient calculation

Use the accepted quadratic chart terms

    Du=-(5/2)z^-4 u^2-3z^-3 uv-(3/8)z^-2 v^2,
    Dv=3z^-5 u^2-z^-4 uv-(9/4)z^-3 v^2.

The moving operator is

    Du f_u+Dv f_v+(z^-3 u+(1/2)z^-2 v) f_z.

Here `f_z=C u+D v`, and its value at `(b,-a)` is
`Cb-Da=-Delta`. The evaluated discrepancy is therefore exactly

    T=3 z^-5 b^3-(3/2)z^-4 a b^2
      +(3/4)z^-3 a^2 b-(3/8)z^-2 a^3
      -Delta z^-3 b+(Delta/2)z^-2 a.

The three cohomology coefficients are

    4 [z^-3]T = B(36D^2-16AD+3A^2-2BC),

    8 [z^-2]T = 24D^3-20AD^2+10A^2D-3A^3
                 +8BC(A-2D),

    8 [z^-1]T = C(-12D^2+16AD-9A^2+2BC).

These formulas include the base derivative. Dropping that term changes the
zero locus and is not a valid moving-relation calculation.

## 3. Complete obstruction-zero locus on Delta != 0

All statements here are in characteristic zero over an algebraically
closed field, and `[A:B:C:D]` is considered up to common nonzero scale.

If `B=C=0`, then `A,D` are nonzero. With `t=A/D`, the remaining equation is

    24-20t+10t^2-3t^3
      =-(t-2)(3t^2-4t+12)=0.

This gives three distinct diagonal points:

    [A:B:C:D]=[t:0:0:1],
    t=2, (2+4 sqrt(-2))/3, (2-4 sqrt(-2))/3.

The point `t=2` is the accepted quadric direction
`q=u+(z/2)v`. In that direction the raw discrepancy `T` itself is zero.

If `C=0` and `B!=0`, then `Delta=AD!=0`. The first and second coefficient
equations would require a common root of
`3t^2-16t+36` and `(t-2)(3t^2-4t+12)`. The first polynomial does not vanish
at `2`; its difference from `3t^2-4t+12` is `-12(t-2)`, so no common root
exists. If `B=0` and `C!=0`, the analogous pair is
`9t^2-16t+12` and `(t-2)(3t^2-4t+12)`. The first does not vanish at `2`;
its difference from three times the second quadratic is `-4(t+6)`, and
its value at `-6` is `432`. Again there is no common root.

If `B,C` are both nonzero, the first and third equations give
`A^2=4D^2`. Necessarily `D!=0`. For `A=-2D` they force `BC=40D^2`, and the
middle equation becomes `-1152D^3=0`, which is impossible. For `A=2D`
they force `BC=8D^2`, and the middle equation vanishes identically.
Moreover, `Delta=-6D^2!=0`.

Thus the exact zero locus is the disjoint union of the three diagonal
points above and the open conic

    A=2D,  BC=8D^2,  D!=0.

The closure of this conic has two points with `D=0`; both have `Delta=0`
and are outside the basepoint-free degree-one problem. Passing the
quadratic obstruction means compatibility through this one normal step;
it does not prove a global surface, primitive quadruple, or STCI pair.

## 4. Independent review of the pure-power quotient

Let `L=O(-e)` be any basepoint-free moving direction inside the constant
rank-two bundle `V tensor O`, and consider the pure-power relation
`m^r` of movement degree `re`. Put

    Q_tilde=Sym^(r+1)V / (L^r tensor V).

The annihilator line `L_perp` inside `V^* tensor O` is `O(-e)`. The
annihilator of `m^r V` under the perfect characteristic-zero symmetric
pairing is exactly

    (L_perp)^2 tensor Sym^(r-1)V^*.

Indeed, in a basis with `m` the first vector, the two vectors spanning
`m^r V` have exponents `(r+1,0)` and `(r,1)`; their annihilator consists
precisely of degree-`r+1` dual binary forms divisible by the square of the
second dual variable. This is a fiberwise equality of rank-`r` bundles,
so

    Q_tilde^*=O(-2e)^r,
    Q_tilde=O(2e)^r.

After restoring the conormal twist and tensoring with the dual relation
line, the actual next-order obstruction bundle is

    Q_r=O((r+2)e-7)^r.

For `e=1`, all pure powers of order `r>=4` therefore have zero
`H^1(Q_r)`. For `e>=2`, already `r>=1` gives zero `H^1(Q_r)`. This proves
that no universal exclusion of moving pure-power first relations can
come from this quadratic step alone. It does not assert the existence
of a complete-intersection thickening with such a first relation.

For the actual quadric direction, the global equation `q^r` supplies
all higher-order lifts of the single relation. A new second independent
relation, or additional full-algebra constraints, is required to obtain
an STCI exclusion.

## 5. All finite steps before the second independent relation

The apolar argument extends to every step `k>=1`. For the pure-power
first relation `m^r`, the initial multiples in degree `r+k` are
`L^r tensor Sym^k V`. Their annihilator is precisely

    (L_perp)^(k+1) tensor Sym^(r-1)V^*.

This follows in the same basis: the initial multiples have second-variable
exponents `0,...,k`, and their annihilator has second-variable exponent at
least `k+1`. It is an equality of rank-`r` bundles. Thus, after the actual
conormal twist and dual relation twist, the obstruction bundle is

    Q_k=Hom(W_r, Sym^(r+k)E / (W_r tensor Sym^k E))
       =O((r+k+1)e-7k)^r,
    W_r=O(-r(7+e)).

The displayed direct-sum isomorphism is independent of local direction
coordinates. A fixed volume form on the constant two-dimensional vector
space identifies the annihilator line with `L`; changing that volume form
only introduces a constant one-dimensional factor.

If all these `H^1(Q_k)` vanish for `1<=k<g`, one can construct a coherent
principal-relation ideal modulo `I_C^(r+g)` with associated initial ideal
generated by `m^r` in every order below `r+g`. Here is the precise finite
construction. Choose arbitrary local lifts of the leading relation on an
affine cover. Assuming they already glue, up to multiplication by units,
through order `r+k-1`, their degree-`r+k` discrepancy is a Cech cocycle
with values in `Q_k`. Vanishing of `H^1(Q_k)` permits local degree-`r+k`
corrections; the discrepancy left in `W_r tensor Sym^k E` is removed by
changing the gluing units in normal degree `k`. The generated local ideals
then agree modulo `I_C^(r+k+1)`. Iterating gives the claimed finite ideal.
Local multiplication by the nonzero leading polynomial `m^r` is injective
in the symmetric normal algebra; consequently this construction adds no
unexpected initial relation or torsion layer below the cutoff.

This is a finite formal-neighborhood construction, not the construction
of a global hypersurface or a complete-intersection pair. No algebraization
or compatible infinite-order lifting is asserted here.

For `1<=e<7`, the obstruction-bundle degree decreases with `k`. All the
required groups vanish if and only if

    (r+g)e >= 7g-8.

For `e=1`, this reads `r>=6g-8`. In particular, for any prescribed finite
gap `g`, moving pure-power first relations of sufficiently high order pass
every formal compatibility step before the second independent relation.
Thus increasing the finite jet order cannot by itself give a uniform
exclusion of all such moving first relations. The full algebra, the
independent second relation, or a global condition must enter a universal
argument.

## 6. Audit scope

The new coefficient equations, their complete case split, the frame
identification, the pure-power splitting at every step, and the finite
principal-relation lifting argument have been independently derived. The
accepted chart transition and accepted quadric equation
were used without re-verification. No new finite test is promoted to a
proof of global existence. The next unresolved calculation is the
cubic compatibility of the obstruction-zero moving linear relations.
