# Exact A4 chart of the parametric degree-five del Pezzo model

Date: 2026-10-11. Author: independent local-chart child of
`a4_exact_ideal`. This note concerns the stated parametrization and its
actual image closure. It does not assert that every geometric degree-five
A4 model is isomorphic to this parametrized model, nor that this chart
contains every singular point of the global surface.

## 1. Statement and scope

Let k be an algebraically closed field of characteristic zero. Let S be
the reduced projective image closure of the rational map

```
P2 --> P5,
[x:y:z] |--> [y z^2-x^3 : x y z : y^2 z : x^2 y : x y^2 : y^3].
```

Then the actual open subscheme `S intersect {Z0 != 0}` is isomorphic to

```
Spec k[a,u,v]/(u v+a^5).
```

Its only singular point is `[1:0:0:0:0:0]`. At that point its completed
local ring is exactly

```
k[[a,u,v]]/(u v+a^5),
```

the formal A4 surface singularity. The assertion follows from polynomial
coordinate changes; it needs neither a numerical singularity recognizer
nor a presumed global ideal computation.

## 2. Five exact relations

The following five quadrics vanish identically after the parametrization:

```
Z1 Z5-Z2 Z4,
Z3 Z5-Z4^2,
Z1 Z4-Z2 Z3,
Z0 Z5-Z2^2+Z3 Z4,
Z0 Z4-Z1 Z2+Z3^2.
```

On the chart `Z0=1`, put

```
a=Z1/Z0, b=Z2/Z0, c=Z3/Z0, d=Z4/Z0, e=Z5/Z0.
```

The last two relations solve

```
d=a b-c^2,
e=b^2-c d=b^2-a b c+c^3.
```

After this substitution the third relation becomes

```
f=b(a^2-c)-a c^2=0.
```

The first and second relations become `-c f` and `-b f`. Consequently the
chart coordinate ring of the scheme cut out by these five quadrics is
exactly `k[a,b,c]/(f)`, with no extra relation and no lost component.

The polynomial change of coordinates

```
u=c-a^2,
v=b+a c+a^3
```

has the polynomial inverse

```
c=u+a^2,
b=v-a u-2a^3.
```

It sends the single equation to

```
f=-u v-a^5.
```

In particular the five-quadric chart is integral: `u v+a^5` is an
irreducible primitive polynomial, linear in v over `k[a,u]`, since u and
`a^5` are relatively prime. This argument uses no characteristic-zero
division.

## 3. Why this is the actual image-closure chart

The preceding computation could otherwise only describe a proposed
containing scheme. Here density identifies it with the actual image.

On the nonempty open subset `e != 0` of the integral five-quadric chart,
take source coordinates `y=1`, `x=d/e`, `z=b/e`. The first two relations
give `a=b d/e`, `c=d^2/e`. The remaining relations give

```
e^2=b^2 e-d^3,
z^2-x^3=1/e.
```

Therefore the source parametrization, divided by its nonzero Z0, is
exactly `[1:a:b:c:d:e]`. Thus the entire open subset `e != 0` is in the
parametric image. It is nonempty, for example at
`(a,b,c,d,e)=(0,1,0,0,1)`, and hence dense in the integral chart.

All five quadrics vanish on S, so its chart is contained in this
five-quadric chart. Conversely the dense open subset just exhibited lies
in S. Since S is the reduced image closure, its chart is the entire
integral five-quadric chart scheme. This proves the asserted actual
chart identification without appealing to an unverified global kernel.

## 4. Singularity and normality

For `F=u v+a^5`, the characteristic-zero Jacobian ideal is
`(u,v,5a^4)`. Its support is the single point `(a,u,v)=(0,0,0)`.
The surface is a hypersurface, so it is Cohen--Macaulay and satisfies
Serre's S2 condition. It is regular away from that closed point, so it
also satisfies R1 and is normal. The coordinate origin corresponds to
`[1:0:0:0:0:0]`. Completion gives the displayed formal A4 equation
directly; replacing v by `-v` gives the alternative standard form
`u v-a^5=0`.

The Jacobian *scheme* is not asserted to be reduced: its local quotient
has length four in characteristic zero. Only the singular support is
a single reduced point.

## 5. Exact replay and preserved failed attempts

The written algebra above proves the result. The companion Macaulay2
source checks 20 elementary polynomial identities over QQ:

- five pullbacks of the quadrics;
- five chart-substitution identities, checked as one exact list equality;
- the equation under the A4 coordinate change;
- three coordinate identities in each direction of the inverse;
- three identities giving the inverse on the open `e != 0`.

The source is
[verify_session_dp5_a4_local_chart_2026_10_11.m2](../computations/verify_session_dp5_a4_local_chart_2026_10_11.m2),
SHA-256 `9a5672a81ce2cfd23fa0eddf2838a1b9224c9cd25a7a70535e2e5523c6ce222d`.
The observed final execution used `/opt/homebrew/bin/M2 --script`, exited
zero, and printed `PASS: 20 exact identities`; tool chunk `c6e806`.
The execution manifest and raw stdout/stderr are retained in
[2026-10-11-dp5-a4-local-chart](../validation/2026-10-11-dp5-a4-local-chart/execution-record.json).

Earlier failures are retained separately. The initial source used the
protected Macaulay2 variable `dd` (initial console chunk `8ff0c6`); its
exact source and a labeled explicit failed replay are stored as
`protected-dd-failed-source.m2`, `protected-dd-failure.*`. The next
scaffold mistakenly applied `entries` to the list `gens R` (observed
chunk `f79399`); its exact source and contemporaneous raw logs are
stored as `gens-list-failed-source.m2`, `gens-list-failure.*`. Renaming
the variable and scanning the generator list fixed these interface
errors. Neither was a failed mathematical identity.

No global-kernel, projective degree, or global-singular-locus check is
counted in this local verifier; those belong to the parent's separate
exact computation.
