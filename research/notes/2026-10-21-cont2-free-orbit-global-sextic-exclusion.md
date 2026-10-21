# Free cube-orbit endpoint chart: exact global sextic exclusion

Date: 2026-10-21, continuation 2. Status: **new exact conditional
exclusion, independently checked; not promoted to a canonical result**.

Work over an algebraically closed field of characteristic zero with
`C0=[s^4:s^3t:st^3:t^4]`, the accepted balanced conormal frame, and the
conditional `(r,s;a,b;epsilon)=(2,12;6,16;2)` configuration. This note
excludes the following precise structured incidence:

1. the moving quadratic root `f` satisfies the accepted first ambient
   incidence `K1`;
2. the sextic multiplier is the canonical cube norm of its quadric-line
   restriction, up to a nonzero scalar;
3. both endpoints of that restriction are nonzero and no root is carried
   to another root by multiplication by a primitive cube root of unity;
4. an actual global sextic has second symbol `alpha*f` and matches the
   canonical first cubic lift.

The incidence is empty as a scheme. The argument stops at the cubic
sextic obstruction. It needs neither a global mate nor a degree-twelve
standard-basis construction, because the required sextic already fails.
Applying the conclusion to actual supported complete intersections also
uses the separately proposed quadric-cycle norm argument. That scope
bridge is a dependency; this note does not promote it by implication.

## Inputs and evidence

The accepted first incidence and ambient chart are inputs from
[STCI-R-0007](../results/quadratic_root_obstruction_model.md). The actual
saturated-first-relation application uses the hypotheses of
[STCI-R-0010](../results/saturated_first_relation_normal_flatness.md) and
the separately supplied finite singular-root bridge. The new global
source map is the previously recorded
[exact sextic symbol calculation](2026-10-20-conditional-2-12-symbol-map.md).

The exact new computations are:

- [four-parameter family exporter](../computations/conditional_2_12_cubic_reduction_2026_10_21_family.py),
  [Macaulay2 input](../computations/conditional_2_12_cubic_reduction_2026_10_21_family.m2),
  and [metadata](../computations/conditional_2_12_cubic_reduction_2026_10_21_family.json);
- [full global C3 specialization](../computations/conditional_2_12_cubic_reduction_2026_10_21_candidates.py),
  [its exact equations](../computations/conditional_2_12_cubic_reduction_2026_10_21_candidates.m2),
  and [all sixteen nonzero specialized equations](../computations/conditional_2_12_cubic_reduction_2026_10_21_candidates.json);
- [lightweight exact certificate](../computations/conditional_2_12_cubic_reduction_2026_10_21_cont2_free_orbit_certificate.m2)
  and [successful output record](../computations/conditional_2_12_cubic_reduction_2026_10_21_cont2_free_orbit_certificate.json);
- [independent rational-arithmetic reconstruction](../computations/conditional_2_12_cont2_independent_unit_audit_2026_10_21.py)
  and [independent PASS record](../computations/conditional_2_12_cont2_independent_unit_audit_2026_10_21.json).

The lightweight certificate runs with
`M2 --script research/computations/conditional_2_12_cubic_reduction_2026_10_21_cont2_free_orbit_certificate.m2`.
It checks both exact ideal containments and then checks the final unit
identity by literal polynomial multiplication. It does not rely on a
unit marker from an interrupted large elimination. The older large
coefficient lifts are preserved at
[the archived exact lift matrices](../computations/conditional_2_12_cubic_reduction_2026_10_21_family_lifts.m2),
but are unnecessary for this lightweight replay.

## The norm-symbol equations collapse to a symmetric family

Put

```text
l=u+(z/2)v,
g=f(z,-z/2,1),
D=4g=d0+d1*z+d2*z^2+d3*z^3+d4*z^4.
```

On `d0*d4!=0`, projective scaling of `f` and the actual `C0` torus give
a finite cover on which `d0=d4=1`. This normalization preserves the
accepted chart: its weights are `wt(z,u,v)=(1,4,3)`.

For a primitive cube root `omega`, let

```text
U=1+d3*z^3, V=d1*z+z^4, W=d2*z^2,
alpha=U^2+V^2+W^2-U*V-U*W-V*W.
```

Thus `alpha=D(omega*z)*D(omega^2*z)`, and `D*alpha=N(z^3)` for a
quartic `N`. Multiplying `alpha` by a nonzero scalar does not change
the existence question.

Use the coordinates

```text
a=(d2+2y1-4y3, d3+2y2, 1),
b=(y0,y1,y2),
c=(1/4,d1/4+y0/2,y3).
```

Eight of the eleven global second-symbol equations vanish identically
under the norm substitution. The remaining three are linear in
`(y0,T=y1-4y3,y2)`. After nonzero constant row rescaling their matrix is

```text
J = [ d2-d1^2          -d1                  1          ]
    [ -2d1+d2*d3      -1-d1*d3+d2^2        2d3-d1*d2  ].
    [ 1                d3                  d2-d3^2    ]
```

Its determinant has the exact interpretation

```text
det J = Res_z(z^3-omega^2*d2*z+d1,
              -omega*d2*z^2+omega^2*d2*d3*z+1-d1*d3).
```

The resultant vanishes exactly when `D(z)` and `D(omega*z)` have a
common root in this endpoint chart. No condition that `D` itself be
squarefree is imposed. The identity is checked by the determinant of
the five-by-five Sylvester matrix over `QQ[omega]/(omega^2+omega+1)`.

The Cramer numerators are exactly
`(-d1/4,-d2/2,-d3/4)*det J`. Hence on `det J!=0` the second-symbol
condition is equivalent to

```text
y0=-d1/4, T=-d2/2, y2=-d3/4.
```

Writing `t=y3`, this gives the four-parameter root family

```text
a=(4t,d3/2,1),
b=(-d1/4,4t-d2/2,-d3/4),
c=(1/4,d1/8,t).
```

It is useful to see the geometry of the compression. With `w=-2u/v`,

```text
8*f(z,-w/2,1)
 =(8t+d3*z+2z^2)w^2
  +(d1+(2d2-16t)z+d3*z^2)w
  +(2+d1*z+8t*z^2)
```

is symmetric in `z,w`, restricts on the diagonal to `2D(z)`, and its
`t` term is `8t(z-w)^2`.

## First compatibility and the quadric part of C3 leave four points

Let `G0` be the accepted canonical first cubic correction over `K1`, and
put `G(z)=G0(z,-z/2,1)`. For a global sextic, restriction to the fixed
quadric gives

```text
F|Q=v^2 R(z^3+v).
```

Consequently the norm-symbol and actual cubic matching conditions imply

```text
D | Nprime_T(z^3)-4*alpha*G.
```

Since `D0=1` and `det J!=0`, both `z` and `alpha` are units modulo `D`.
Differentiating `N(z^3)=D*alpha` therefore makes this exactly equivalent
to the four remainder equations

```text
rem_D(Dprime-12*z^2*G)=0.
```

Eight accepted first-incidence equations eliminate
`h0,...,h3,h8,...,h11` without denominators on `d0=d4=1`. Substitute
the symmetric root family. In

```text
QQ[d1,d2,d3,t,h4,h5,h6,h7]
```

the remaining eight `K1` equations and these four q-line cubic equations
generate exactly the following triangular ideal:

```text
h6=0, h5=0, h4=-2h7, d3=0, d1=0,
t=(27/4)h7^3+(15/32)h7,
d2=108h7^3-(9/2)h7,
648h7^4+45h7^2-4=0.
```

Both ideal containments are verified over `QQ`, and the independent
audit reconstructs the same ideal from its own first/C3 construction.
Thus this step is an exact scheme calculation, not a sample. It has
dimension zero and degree four. Writing `h=h7`, one also has
`24th=1` and `d2=16t-12h`. The four points obey

```text
h^2=(-5+3sqrt(17))/144  or  (-5-3sqrt(17))/144.
```

They satisfy `det J!=0`: here `det J=(d2^2-1)^2` and
`d2^2=216h^2-11`, which is never one on the displayed quartic. This
observation is a consistency check; the exact ideal computation was
performed on a closed enlargement and did not discard the determinant
boundary during its calculation.

## Full global sextic C3 gives a two-line unit certificate

The actual degree-six second-symbol map has kernel exactly `k*q^3`.
Consequently every global sextic with second symbol `alpha*f` has the
fixed rational `k`-linear source splitting plus one coefficient `eta`
of `q^3`. The full cubic comparison is

```text
F3-alpha*G0+eta*q1^3 = f*(ell*u+m*v).
```

Its necessary polynomial syzygy equations are obtained from the actual
global source matrices. They retain the coefficient `eta`; no generic
`k(C0)` coefficients or hidden splitting of a second relation are used.
At the four-point scheme, two of those exact equations are

```text
E4=(3/4)eta+(369/16)h-(891/2)h^3,
E8=(1/8)eta+(27/32)h-(81/4)h^3.
```

Their difference is

```text
E4-6E8=18h-324h^3.
```

Let `p=648h^4+45h^2-4`. The following is a literal identity in
`QQ[h,eta]`:

```text
1 = ((162h^2-1)/4)*p
    +(81h^3+(77/8)h)*(E4-6E8).
```

The independent standard-library rational verifier reconstructs the
specialized full C3 equations from a separate source construction,
matches the equation directions, and checks this identity without a
Groebner basis. Therefore all four candidates fail actual global
sextic C3, and the free-orbit endpoint incidence is empty.

## Precisely what remains outside this result

The conclusion excludes every root in the stated chart, including
singular full roots whenever the accepted/proposed necessity bridges
apply. It does not require a smooth root or reduced diagonal divisor
`D`. It does not cover `d0*d4=0` or `det J=0`.

On the orbit-collision boundary, cancellation by `alpha` is invalid.
The exact retained condition is the multiplication of the four simple
remainders by the four-by-four multiplication matrix of `alpha` on
`k[z]/(D)`. Its determinant is exactly `81*(det J)^2`, as recorded in
the [all-strata q-line exporter](../computations/conditional_2_12_cubic_reduction_2026_10_21.json).
The collision and endpoint strata remain separate work; this proof
does not silently saturate them away.

No unrestricted STCI conclusion or full decision of the conditional
configuration follows from this chart exclusion alone. No global pair
has been realized.
