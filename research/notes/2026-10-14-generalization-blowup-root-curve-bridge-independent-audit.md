# Independent audit of the actual-CI blowup/root-curve bridge

Date: 2026-10-14. Status: **NEW GEOMETRIC BRIDGE PASSES UNDER ITS
LITERAL HYPOTHESES**. Reviewer: independent bridge-review worker, with
separate local-algebra and conormal subreviews. This is a written
mathematical audit, not a finite computation or a claim of ambient
obstruction nonvanishing.

Reviewed source:
[blowup/root-curve primitive bridge](2026-10-14-generalization-blowup-root-curve-primitive-bridge.md).
The accepted
[spectral root-curve theorem](2026-10-14-generalization-spectral-root-curve-relations.md)
and its
[independent audit](2026-10-14-generalization-spectral-root-curve-independent-audit.md)
are premises. Their spectral descent criterion, ambient extension class,
and cohomology targets were not reaudited. No previous CAS or carrier
certificate was replayed.

## 1. Precise conclusion and hypotheses

Let `C` be a smooth curve in a smooth threefold `X` in characteristic
zero. Work on a connected component of `C` when necessary. Let an actual
complete intersection `Y=(F,G)` have reduced support exactly `C`. Retain
all the hypotheses in the reviewed source:

- The first actual ordinary normal relation has degree `r`; its relation
  sheaf is a saturated line subbundle `R` of `Sym^r N_C^*`.
- The two **chosen actual equations** have generic normal order `r`, and
  their degree-`r` symbols jointly generate `R` at every point of `C`.
- At the generic point of `C`, the **full ordinary initial ideal**, not
  just two selected initial forms, is the binary regular sequence
  `(f_r,g_s)`, where `s>r`, `g_s` is coprime to `f_r`, and `k=s-r>=2`.
- The actual Cartier root divisor `Z=(f_r)` on the exceptional divisor
  `E` of `B=Bl_C X` is smooth. In particular, `Z` itself is reduced;
  smoothness of its reduced support alone is insufficient.

Then the intersection `Y'=D_F intersect D_G` of the strict-transform
Cartier divisors has support exactly `Z`, contains no vertical
exceptional-fiber curve component, and is everywhere an embedded
primitive `k`-fold structure on `Z`. Its first ordinary normal layer is
canonically `O_Z(-E)`. The conormal extension

```
0 -> O_Z(-E) -> N_(Z/B)^* -> O_Z(-Z_E) -> 0             (1)
```

splits, so the actual first ambient root-divisor obstruction obeys

```
kappa(df_r)=0.                                        (2)
```

The conclusion concerns this stated lane of actual supported complete
intersections. It makes no claim that the hypotheses exhaust all STCI
presentations, and it makes no claim that the fixed ambient obstruction
has a nonzero value.

## 2. Support, vertical fibers, and purity

Locally write the exceptional equation as `u`. Because each chosen
equation has normal order `r`, its strict transform is obtained by
dividing its pullback by `u^r`. On `E`, the two transformed equations
restrict to `a f_r,b f_r`. The coefficient pair `a,b` has no common zero
on `C`, and the line-subbundle condition means that `f_r` is not the zero
binary polynomial on any exceptional fiber.

The common zero set on `E` is therefore exactly `Z`. Away from `E`, the
blowup is an isomorphism, and the original pair has no common point away
from `C`. Thus `Supp(Y')=Z`. In particular, no entire exceptional fiber
is a component of the strict intersection.

Neither strict divisor contains `E`. A common surface component outside
`E` would give a common surface component of the original pair. Hence
the strict equations have height two in the smooth threefold `B` and
form a regular sequence. Their intersection is a one-dimensional
Cohen--Macaulay scheme with no embedded or isolated component. No
component or closed point has been discarded in this argument.

## 3. Generic transverse multiplicity really is `s-r`

Let `K` be the function field of `C`, and complete the generic normal
local ring to `K[[x,y]]`. Choose a lift `H` in the actual ideal whose
initial form is `g_s`. Use one original equation with nonzero generic
leading coefficient as `P`; its initial form is a nonzero scalar
multiple of `f_r`. Since these initial forms generate the **entire**
initial ideal, successive filtered division gives

```
(P,H)=(F,G) in K[[x,y]].                              (3)
```

One can also obtain (3) from equality of the two finite colengths: the
coprime homogeneous initial forms of `P,H` give colength `rs`, equal to
the colength determined by the stated full initial ideal of `(F,G)`.
Consequently these two generating pairs differ by an invertible local
matrix. Both original equations were divided by the same `u^r`, so this
change of generators preserves the strict-intersection ideal.

On a normal blowup chart `x=u,y=uv`, that ideal is

```
( P/u^r, H/u^r )
 = ( f_r(1,v)+O(u), u^(s-r)(g_s(1,v)+O(u)) ).          (4)
```

After a finite extension of `K`, each generic root can be treated
separately. The root is simple because the actual root divisor is
smooth and reduced, finite over `C`, and generically separable in
characteristic zero. Coprimality makes the second parenthesis a unit at
that root. The first equation eliminates the root coordinate, leaving
the transverse algebra `L[[u]]/(u^k)`, where `L` is the root field and
`k=s-r`. This proves the claimed multiplicity on every root component.

Two arbitrary selected orders would not justify (3) or (4). The full
generic initial complete-intersection hypothesis is doing substantive
work here.

## 4. Direct local proof of primitivity everywhere

There is a shorter proof than the completion argument in the reviewed
source, and it proves a useful additional local normal form. Fix
`p in Z`. Choose one transformed equation `h` whose leading coefficient
is a unit at `p`. This is possible by joint leading basepoint freeness.
Since

```
h|E = a f_r,                 a(p) != 0,
```

and `Z` is smooth in `E`, the surface `S=(h)` is smooth at `p` and meets
`E` transversely along `Z`. In particular the exceptional equation `u`
cuts out `Z` as a reduced Cartier divisor on the regular local surface
`S`.

Let `h_2` be the other strict equation. Its restriction to `S` is
nonzero and has zero set exactly `Z`. In the regular local ring
`O_(S,p)`, it must therefore be

```
h_2|S = epsilon u^e,              epsilon a unit.       (5)
```

Indeed a two-dimensional regular local ring is a UFD, and `(u)` is the
only height-one prime in its zero set. The generic multiplicity from
Section 3 fixes `e=k`. Lifting the unit in (5) gives the exact local
ambient ideal

```
I_(Y',p) = (h,u^k)                                   (6)
```

already before completion. This proves the entire embedded primitive
conclusion at every point, not only generic curvilinearity. It also
proves directly that the surviving conormal is the exceptional
conormal `O_Z(-E)`.

The source's completion/Nakayama proof passes as well: over a completed
smooth-curve parameter ring the local algebra is finite free of rank
`k`; a generically zero submodule is zero by torsion freeness, so `J^k=0`;
the invertible first layer makes `J` principal; the resulting surjection
from the rank-`k` truncated polynomial algebra is an isomorphism. The
direct proof (6) avoids those auxiliary finiteness and nilpotence steps.
For readability, its coefficient field should be denoted `Bbbk` rather
than `k`, since `k` already denotes the multiplicity.

## 5. Conormal splitting, including ramification points

For an independent check of the source's conormal argument, put

```
L=O_Z(-E), M=O_Z(-Z_E), V=I_Z/I_Z^2.
```

Let `phi` be the map from the two equation line bundles to `V` given by
their first normal symbols. The quotient map `q:V -> M` sends these
symbols to `a f_r,b f_r` in the conormal line, or to `a df_r,b df_r`
under its differential embedding in `Omega_E|Z`. Hence `q phi` is
surjective.

The determinant of `phi` vanishes at the generic point of every
component of `Z`: independent linear terms there would give transverse
length one, contrary to `k>=2`. Since `Z` is reduced, this regular
determinant section vanishes identically. Locally choose a symbol `v`
with `q(v)` a unit and complete it to a basis `v,e` of `V`. Writing the
other symbol as `av+be`, the zero determinant forces `b=0`. Thus

```
K=im(phi) is a line subbundle,  K -> M is an isomorphism,
V/K = L canonically.                                  (7)
```

This splits (1). Moreover, with `J=I_Z O_(Y')`, the ordinary first layer
is exactly

```
J/J^2 = I_Z/(I_Z^2+I_(Y')) = V/K = O_Z(-E),            (8)
```

so no point-supported torsion has been suppressed.

Here `df_r` means the **full differential on `E`**, including the base
direction. No unramifiedness hypothesis on `Z -> C` is needed. For
example, at a smooth ramification point the root equation may be
`f=t-v^2`: its fiber derivative vanishes at the origin, but
`df=dt-2v dv` does not. Using only the fiber derivative would invalidate
this argument.

## 6. Actual exceptional lifts and the obstruction implication

The local form (6) also globalizes the higher-order interpretation.
Writing `E_k=V(I_E^k)`, one has `I_E^k subset I_(Y')`, and
`I_(Y')/I_E^k` is locally generated by the nonzerodivisor `h` on `E_k`.
It is therefore an invertible ideal on `E_k`. Thus `Y'` is an actual
Cartier lifting of `Z` into `E_k`, and restriction gives compatible
Cartier liftings through every exceptional order strictly below `k`.
This does not supply lifts at or beyond order `k`.

The first obstruction implication can also be checked directly from
the conormal diagram. Restrict the ambient cotangent extension to `Z`:

```
0 -> L -> Omega_B|Z -> Omega_E|Z -> 0.
```

Its extension class is the restriction of the accepted first-neighborhood
class `kappa`. Pull it back along

```
df_r:M -> Omega_E|Z.
```

Because `Z` is smooth, the pullback middle term is precisely `V`, giving
(1). Consequently

```
class(1) = df_r^*(kappa|Z)
         in Ext1_Z(M,L)
          = H1(Z,O_Z(Z_E) tensor O_Z(-E)).              (9)
```

The splitting in (7) proves (2). This uses the actual geometric class,
not merely the dimension of its cohomology target. An opposite Cech
extension convention can negate its representative and has no effect
on the vanishing assertion.

## 7. Nonzero first-relation defects must retain their base points

The hypotheses cannot be replaced by saturation of a defective first
relation. The following family exhibits the precise failure without
any degree enumeration.

In `A3_(t,x,y)`, let `C=(x,y)`. Choose a squarefree homogeneous binary
form `f_r(x,y)` and a homogeneous form `h_(r+1)(x,y)` coprime to `f_r`.
For an integer `q>=2`, set

```
F=t f_r+h_(r+1),       G=F+f_r^q.                     (10)
```

This is an actual height-two complete intersection supported exactly on
`C`: its common zero set is `f_r=h_(r+1)=0`, whose only normal-plane point
is the origin. Both chosen equations have generic normal order `r`.
Over `Bbbk(t)`,

```
(F,G)=(t f_r+h_(r+1), h_(r+1)^q),
```

and the coprime initial forms give the full generic initial complete
intersection of degrees `(r,q(r+1))`, with gap at least two. The
saturated first relation has the smooth root divisor given by the
distinct constant root sections of `f_r`.

However, the **actual** degree-`r` relation sheaf is `t O_C f_r`, whose
inclusion has a first-relation defect at `t=0`. Both actual leading
coefficients vanish there. On the exceptional divisor, the restrictions
of the two strict equations are both `t f_r`, so their intersection
contains the entire exceptional fiber over `t=0`.

Thus the nonzero defect is a real boundary stratum. Its joint leading
base point cannot be deleted or cured by replacing `t O_C f_r` with its
saturation. This family is outside the reviewed theorem and does not
contradict it.

## Audit disposition

The generic blowup length, exact support/no-vertical-component claim,
global first-layer splitting, entire embedded primitivity, and necessity
`kappa(df_r)=0` all pass under the literal hypotheses. The direct local
normal form `(h,u^k)` supplies a structural proof with no socle-profile
or degree enumeration. The retained boundaries are the actual
first-relation defect and its base points, singular or nonreduced root
divisors, noncoprime next relation, generic initial ideals outside the
stated binary complete-intersection form, unequal chosen normal orders,
and gap one. The value of the fixed ambient obstruction remains a
separate new problem. The universal STCI question and unrestricted
characteristic-zero `C0` remain open.
