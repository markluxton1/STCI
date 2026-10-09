# Exact power descent in the entire quadratic conic conductor algebra

Date: 2026-10-09. Author: `quadratic_conductor_power_descent`.

Status: **PROVED HERE; independent audit requested.** These are algebraic
necessary and sufficient conditions for power descent on the actual
conductor. They do not classify which conductor data come from the fixed
rational quartic on a normal del Pezzo surface. In particular they are not
an exclusion of the remaining genus-one carriers or a resolution of STCI.

## 1. Scope and the section decomposition

Work over an algebraically closed field `k` of characteristic zero. Let
`Gamma` be the actual plane conic, allowing a smooth conic, two distinct
lines, or a plane double line. Let `M=O_Gamma(1)` and let `p:D -> Gamma`
be the entire finite flat quadratic conductor algebra

```
p_*O_D = O_Gamma direct_sum M^(-1).
```

The second summand is the trace-zero part. In a local pulled-back frame
write its generator as `w`, with multiplication `w^2=delta`. In these
coordinates `delta` has the transition rule of a section of `M^2`.
The involution fixes the base and sends `w` to `-w`.

For a section `q` of `p^*M^2`, the corresponding global decomposition is

```
q = m + w ell,
m in H^0(Gamma,M^2),  ell in H^0(Gamma,M),
delta in H^0(Gamma,M^2).
```

All products below use those transition rules, so they define global
sections. Assume `q` is a nonzerodivisor on the entire scheme `D`. In the
surface application, this holds for `q=Q|D` if `div_S(Q)=2c` and no
irreducible component of `D` is `c`: `D` is Cartier on the Cohen--Macaulay
surface, hence has no embedded associated points, and `Q` does not vanish
at any generic point of `D`. An actual conductor component cannot be `c`
when its image is in the degree-two conic while the image of `c` is the
degree-four integral curve `C0`.

For the two-quadric model used by the root, with

```
z^2 - A z - R1 = 0,       L z + R = 0,
Gamma = V(L,R),           D = V_S(L),
Q = q2 + z ell,
```

the decomposition is exactly

```
w=z-A/2,       delta=A^2/4+R1,       m=q2+A ell/2
```

on the entire `Gamma`, including its nilpotents. The complete conductor
square identifies descent of `Q^n` to the quartic surface with invariance
of `q^n` under the involution. This note addresses that algebraic
invariance; the conductor-square identification is proved in the separate
entire-conductor note.

## 2. A universal polynomial equation for a specified power

Put `d=delta ell^2`, a section of `M^4`. The anti-invariant coefficient
of `q^n` is

```
ell S_n(m,d),
S_n(m,d) = sum_{j=0}^{floor((n-1)/2)}
           binomial(n,2j+1) m^(n-2j-1) d^j.
```

Thus, for every positive integer `n`,

```
q^n descends  <=>  ell S_n(m,delta ell^2)=0 on the entire Gamma.
```

This equivalence uses that `1,w` are a free basis of the quadratic
algebra, not division by `w` or reduction to the support. For example
`S_2=2m`, `S_3=3m^2+d`, and
`S_4=4m(m^2+d)`.

## 3. Exact criterion for existence of some descended power

Define the following countable set of constants:

```
Cycl = { ((1+zeta)/(1-zeta))^2 :
         zeta in k is a root of unity, zeta != 1,-1 }.
```

Neither `0` nor `1` belongs to `Cycl`. The two reciprocal roots of unity
give the same constant. For a smooth conic or the entire plane double
line, the following criterion is necessary and sufficient:

> Some positive power of `q` descends if and only if either
> `m ell=0` as a section on the entire `Gamma`, or there exists
> `rho in Cycl` such that `m^2=rho delta ell^2` on the entire `Gamma`.

For two distinct lines, use this criterion separately on each reduced
line; the two constants may differ. A common multiple of the two chosen
root-of-unity orders, and of `2` for each `m ell=0` case, gives a single
descended power on the whole conic. There is no discarded condition at
the node: the base conic is reduced, so a section vanishing on both
irreducible components vanishes on the whole scheme.

### Necessity, with double-line nilpotents retained

At the generic point of an irreducible reduced conic or line, the base
ring is its function field `K`. At the unique generic point of a plane
double line, the base ring is the Artin ring `K[epsilon]/(epsilon^2)`.
Write this base ring as `T`, and let `E=T[w]/(w^2-delta)`. The image of
the nonzerodivisor `q` is a unit in `E`: in the generic zero-dimensional
ring a nonzerodivisor is invertible. If `q^n` is invariant, the unit

```
t = sigma(q)/q
```

satisfies `t^n=1`. The factors of `T^n-1` over `k` are the distinct
linear factors `T-zeta`. Consequently an `n`th root of unity in a
finite Artin algebra is a constant root of unity on each local factor,
with no nonzero nilpotent correction. This follows directly from the
pairwise coprime linear factors and their idempotent decomposition.

There are precisely three generic possibilities for `E`.

1. If the residual `delta` is nonzero and nonsquare in `K`, `E` is
   local with quadratic residue field. Thus `t=zeta` is a single
   constant. Since `sigma(t)=t^(-1)` and `sigma` fixes constants,
   `zeta=+1` or `-1`. These possibilities imply `ell=0` or `m=0`
   respectively, as exact identities in `T`.
2. If the residual `delta` is zero, `E` is local and `sigma` acts as
   the identity on its residue field. Hence `t=1`, and `ell=0` as
   an exact identity in `T`. This excludes nilpotent anti-invariant
   corrections; it is stronger than an identity only on the reduced
   support.
3. If the residual `delta` is a nonzero square, its square root lifts
   uniquely across the nilpotents after choosing a sign, since `2`
   times that root is a unit. Then `E=T x T`, with `sigma` swapping
   the two factors. Consequently `t=(zeta,zeta^(-1))`. For
   `zeta=+1` or `-1` this again gives `ell=0` or `m=0`. Otherwise,
   writing `s^2=delta` in `T` gives

   ```
   m = lambda s ell,  lambda=(1+zeta)/(1-zeta)
   ```

   up to exchanging the two factors. Hence
   `m^2=rho delta ell^2` exactly in `T`, with `rho=lambda^2 in Cycl`.

The identities on the smooth conic extend from its function field. On
the double line they extend from the generic Artin ring, not from its
residue field: a section of a locally free sheaf on this pure
Cohen--Macaulay conic that vanishes at the generic Artin ring is zero.
This can also be checked explicitly in the plane double-line ring
`k[a,b,epsilon]/(epsilon^2)`, where a homogeneous section has its full
two terms `f(a,b)+epsilon g(a,b)` and generic vanishing kills both.

Thus the global identities in the criterion retain the double-line
first-order data. On a union of distinct lines the argument applies
component by component, giving the stated separate identities.

### Sufficiency without a reducedness assumption

If `m ell=0`, the coefficient of `w` in `q^2` is `2m ell=0`, so
`q^2` descends on every conic type, with all nilpotents included.

Suppose `m^2=rho d`, where
`rho=((1+zeta)/(1-zeta))^2` and `zeta` has order `n` other than
`1` or `2`. The polynomial `S_n(m,d)` is divisible by
`m^2-rho d` in `k[m,d]`. To verify this, formally put `d=b^2`.
The difference `(m+b)^n-(m-b)^n=2b S_n(m,b^2)` vanishes at both
`m=+lambda b` and `m=-lambda b`, since their two ratios are
`zeta` and `zeta^(-1)`. Since `lambda` is nonzero and the two
linear factors are distinct, `m^2-lambda^2 b^2` divides it after
cancellation of `2b`. The resulting even polynomial in `b` is the
claimed divisibility in `k[m,d]`. The universal polynomial equation
in Section 2 then proves descent of `q^n` without division by a
potential zero or nilpotent on `Gamma`.

## 4. Finite polynomial necessary conditions independent of mate degree

The exact criterion has a countable constant set because mate degree is
unbounded. It nevertheless has a finite algebraic necessary shadow.
For a smooth conic or an entire double line, the two sections

```
m^2, delta ell^2 in H^0(Gamma,M^4)
```

must be linearly dependent over `k`. Indeed, the exact criterion gives
a constant proportionality, except in the case `m ell=0`. In that
case the generic Artin proof above gives `m=0` or `ell=0`, and the
generic identity extends to the whole irreducible scheme, so one of
these two sections is zero.

For the smooth conic, parameterize by `P1`; `M=O_P1(2)`, so the two
sections are binary forms of degree eight. Their `2 x 9` coefficient
matrix has rank at most one: all `36` two-column minors vanish.
For a plane double line, `h^0(M^4)=9` as well. In coordinates
`Gamma:epsilon^2=0` in `P2[a,b,epsilon]`, a convenient basis is

```
a^4,a^3b,a^2b^2,ab^3,b^4,
epsilon a^3,epsilon a^2b,epsilon ab^2,epsilon b^3.
```

The same `36` minors must vanish with these full scheme coefficients.
Checking only the first five coefficients is insufficient.

For two distinct lines, the separate restrictions of `m^2` and
`delta ell^2` are binary quartics. The required ranks are at most
one for two `2 x 5` matrices, hence `10` minors per line. The constants
are allowed to differ on the two lines, so imposing a single global
proportionality on all nine conic coefficients would be unjustified.

These finite equations are necessary, not sufficient for power descent.
For example, proportionality with a constant outside `Cycl` need not
give a descended power, and the double-line proportionality at `rho=0`
does not by itself kill a nonzero nilpotent `m`.

## 5. A split-cover example prevents an algebra-only degree bound

Take a smooth conic `Gamma=P1` with `M=O_P1(2)`. Choose a section
`s` of `M` with two simple zeros and form the complete quadratic
algebra with `delta=s^2`. Thus `D` consists of two copies of `P1`
meeting at those two points; it is connected, Gorenstein and has
arithmetic genus one. Its algebra still satisfies
`p_*O_D=O_Gamma direct_sum M^(-1)` and `H^0(D,O_D)=k`.

Choose any root of unity `zeta != 1`, and set

```
lambda=(1+zeta)/(1-zeta),  ell=s,  m=lambda s^2,
q=(lambda s+w)s.
```

The two components have restrictions

```
q_+=(lambda+1)s^2,     q_-=(lambda-1)s^2.
```

Both constants are nonzero, so `q` is a nonzerodivisor. Their ratio
is `zeta^(-1)` with this choice of lambda; the inverse has the same
order. Accordingly the smallest positive descended power is the
order of `zeta`, which can be arbitrarily large. The only zeros lie
over the two singleton support fibers `s=0`, and the orders on each
component are even. Thus connectedness, arithmetic genus one,
singleton support fibers at zeros, and even component valuations do
not bound the power exponent in this algebra alone.

This is **not** a construction of a del Pezzo surface, a doubled
rational normal quartic, or an STCI pair. Those additional geometric
requirements may exclude the example. It identifies the exact
remaining obstruction to an argument based only on the quadratic
conductor algebra. In particular a root-of-unity ratio on exchanged
components must not be silently replaced by a global sign.

## 6. Remaining surface-geometric work

For an integral nonsplit cover of a reduced irreducible conic, power
descent does force `q` to be invariant or anti-invariant. Invariance
of the original global `Q` on the entire conductor yields an ambient
quadric with doubled `C0`, which is already excluded by the fixed
curve's unique smooth quadric and its ruling class `(1,3)`.

Anti-invariance remains possible when the conductor passes through
singularities at which `c` is not Cartier. The local `A1` model
`x^2+l x-z^2=0`, `c=(x,z)`, `Q=x`, `D=(l)` has
`div(Q)=2c`, and on the nodal conductor `sigma(x)=-x` while `x^2`
descends. Thus the smooth-conductor parity proof does not extend by
ignoring those singular points.

The root and `singular_normalization_next_frontier` are pursuing the
actual rational-normal-quartic ribbon, two-quadric pencil and
projection singleton constraints. The bounded rank equations here
can be combined with those exact geometric constraints; they do not
replace them.

