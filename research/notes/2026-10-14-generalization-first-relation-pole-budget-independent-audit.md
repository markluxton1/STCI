# Independent review of the constant-relation pole budget

Date: 2026-10-14, America/New_York. Reviewer: root.
Status: **PROVED under the explicit hypotheses below**. This reviews new
Section 6 of [the thick extension](2026-10-13-generalization-thick-equality-extension.md).
The previously accepted quadratic transition and apolar annihilator
classification are inputs; their calculations were not repeated.

## 1. Hypotheses and verdict

Work in characteristic zero on fixed
`C0=[s^4:s^3t:st^3:t^4]`, with `N_C0=O(7)^2`. Let `Q` be an actual
embedded ideal defining a thickening, and write

```
K_j = ker(Sym^j N_C0^* -> gr_j(O_Y)).
```

Suppose the first generic relation has degree `r`, its generic direction
is a constant nonzero binary form `f`, and there is no independent
relation in degree `r+1`. Suppose its actual line sheaf is

```
K_r = O(-7r) f(-D),  D effective, delta=deg D.
```

The conclusion is correct: the section cutting out `D` annihilates the
accepted primitive-triple obstruction `h_m` for **each** linear factor
`m` of `f`. This retains the multiplicity of every factor and the full
special-point divisor; it does not discard poles or claim the generic
direction is constant in other cases.

## 2. Saturation is the crucial step

The generic degree-`r+1` relation space is `f V`, where `V=k^2`.
The constant subbundle `O(-7(r+1)) tensor f V` has a locally free
quotient in the ambient symmetric conormal bundle. Composing the
inclusion of `K_(r+1)` with that quotient gives a generically zero
map from a vector bundle to a vector bundle on an integral smooth
curve. It is zero everywhere. Therefore every actual next-order
relation lies in the saturated constant span `f V`, even where
`K_(r+1)` has a modified lattice.

It is consequently legitimate to test a lifted degree-`r` generator
in the quotient `W=Sym^(r+1)V/f V`. No assertion that the actual
relation lattice equals its saturation is needed.

## 3. The obstruction has the stated twist

Choose local normal coordinates and a local generator `h` of the
divisor ideal of `D`. A lift of the initial relation `h f` changes in
next normal order by `h D_ambient(f)`. Differentiating `h` under
motion of the support coordinate contributes a multiple of `f` times
a linear normal coordinate. Changing the scalar gluing unit has the
same form. Both contributions vanish in `W`. Local next-order
corrections change the resulting cocycle by a coboundary.

The correction bundle is intrinsically

```
Hom(K_r, O(-7(r+1)) tensor W) = O(D-7) tensor W.
```

Thus the necessary obstruction is the image of the quadratic ambient
transition class under multiplication by the global section of
`O(D)` cutting out `D`, in `H^1(O(D-7)) tensor W`. This explains the
positive divisor twist, rather than merely assigning it by analogy
with the linear case. On `P1`, this is `H^1(O(delta-7)) tensor W`.

## 4. Factor extraction and consequences

Write `f=m^t H(m,ell)` with `H(0,1)!=0`. The coefficient functional
extracting `m^(t-1) ell^(r+2-t)` vanishes on `f V`, so it defines a
constant map from `W` to `k`. The Leibniz rule sends the obstruction
to

```
t H(0,1) D h_m.
```

Both scalar factors are nonzero in characteristic zero. An actual
embedded lift therefore requires `D h_m=0` for every factor `m`.

The imported apolar classification gives the following necessary
conditions uniformly in `r`:

- `delta<=1` is impossible.
- At `delta=2`, `f` is a power of one pure endpoint direction and
  `D` is its doubled endpoint.
- At `delta=3`, `f` is still a power of one direction. A mixed
  `m=U+theta V` requires exactly `D=div(st(t+2theta s))`;
  an endpoint requires its doubled endpoint plus one point.
- If `f` has two distinct factors, `delta>=4`.

These use the established facts that a mixed direction has no
annihilator below degree three and a unique degree-three annihilator,
while the endpoints require divisibility by their respective squared
coordinates. Distinct mixed directions have distinct degree-three
divisors, and a mixed degree-three divisor has only simple endpoint
zeros. A divisor annihilating both endpoints has degree at least four.
No accepted rank calculation was rerun.

This theorem is necessary structure. It does not assert existence
of any remaining power relation, control higher obstructions, handle
moving binary directions, or exclude positive-defect STCI
presentations. In positive characteristic the factor multiplicity
`t` can vanish, so the argument is not transferred there.
