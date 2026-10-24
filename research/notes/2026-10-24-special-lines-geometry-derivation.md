# Independent derivation: special lines and planes of the fixed rational quartic

Date: 2026-10-24. Author: independent geometry agent `special_geometry`.
Status: **new research evidence; not a promoted canonical result**.
Scope: the specified embedding of `P1` in `P3` over an algebraically closed
field of characteristic zero. No STCI hypothesis is used in this note.

The proofs below start from the embedding, rather than from earlier quartic
carrier exclusions or conormal calculations. They distinguish the
scheme-theoretic intersection of a line with the curve from a plane section.

## 1. The intrinsic ruling picture

Write `c(u)=[1:u:u^3:u^4]`. The only quadratic relation is
`q=x0*x3-x1*x2`: the ten quadratic monomials have pullback exponents
`0,1,2,3,4,4,5,6,7,8`, so their kernel is one-dimensional. Its quadric
`Q` is smooth. Under the Segre identification

```
Q=P1_A x P1_B,
x0=A0*B0, x1=A0*B1, x2=A1*B0, x3=A1*B1,
```

the curve is the graph `[A0:A1]=[s^3:t^3]` over `[B0:B1]=[s:t]`.
Thus `C` has divisor class `(1,3)`, the projection to `B` is an isomorphism,
and the projection to `A` has degree three. The two totally ramified points
of the degree-three projection are `p0=c(0)` and `p∞=c(∞)`.
This distinguishes the two ruling families intrinsically.

The degree-three ruling line over `v` is

```
L_v : x2=v*x0, x3=v*x1,
L_v.C = sum_{u^3=v} [c(u)].
```

For nonzero finite `v` the three points are distinct. At `v=0,∞` the
intersection divisor is respectively `3p0,3p∞`. The other ruling line
through `c(a)` is

```
M_a : x1=a*x0, x3=a*x2,
M_a.C = [c(a)].
```

**All lines meeting C in scheme length greater than two are exactly the
lines `L_v`; their length is three, never four.** Indeed, if a line not
contained in `Q` met `C` in length at least three, the nonzero quadratic
`q` on that line would vanish on a subscheme of length at least three,
contradicting degree two. A line contained in the smooth quadric belongs
to one of its two rulings, where the preceding degrees apply.

In particular, the tangent line is a trisecant only at `p0,p∞`. At all
other points it has intersection length exactly two with `C`. To check
the distinction directly, `T_a=<c(a),c'(a)>` and
`q(c(a)+z*c'(a))=-3*a^2*z^2`. At `a=0` the tangent is `L_0`, and the
opposite chart gives `T_∞=L_∞`. A secant through two distinct finite points
`a,b` lies in `Q` exactly when `a^3=b^3`; it then contains the third point
of the cubic fiber. All other ordinary secants have length two.

## 2. Osculation and the intrinsic involution

Hyperplane sections form the four-dimensional subspace
`W=<s^4,s^3*t,s*t^3,t^4>` of `H0(P1,O(4))`. A section with triple zero at
nonzero finite `a` has the form `(u-a)^3*(u-b)`. The missing coefficient
of `u^2` is `3*a*(a+b)`, so `b=-a`. Consequently

```
H_a : -a^4*x0+2*a^3*x1-2*a*x2+x3=0,
H_a.C = 3[c(a)]+[c(-a)].
```

The homogeneous plane map is

```
[s:t] -> [-t^4:2*s*t^3:-2*s^3*t:s^4].
```

Its limits are `H_0:x3=0` and `H_∞:x0=0`, with sections `4p0` and
`4p∞`. These are the two hyperosculating planes. At either endpoint the
2-jet spans only the tangent line; the displayed hyperosculating plane
is the unique plane of contact order four and the limit of generic
osculating planes. Every plane through the endpoint tangent line already
has contact at least three there. This endpoint jet-rank drop should not
be hidden in a generic second-derivative definition of osculation.

The residual-point map is the involution `iota(u)=-u`. Intrinsically it is
the unique nonidentity involution of `C≅P1` fixing each of the two totally
ramified points of the distinguished cubic ruling projection. Its two
fixed points are exactly the hyperosculating points.

It extends to the ambient projective involution

```
sigma[x0:x1:x2:x3]=[x0:-x1:-x2:x3].
```

On `Q` this changes the signs of both `A1` and `B1`, so it preserves
each ruling family. Its ambient fixed locus consists of the two disjoint
lines `E_+=V(x1,x2)` and `E_-=V(x0,x3)`. Its four fixed points on `Q`
are the four Segre coordinate points, only two of which lie on `C`.

For nonfixed `a`, the two osculating planes intersect in the ordinary
secant joining their contact points:

```
H_a ∩ H_-a = S_{a^2},
S_w : x2=w*x1, x3=w^2*x0.
```

This follows either by adding/subtracting their equations or because
each plane contains both points and the planes are distinct. Thus the
paired plane intersection has length two on `C`, not a length-three
osculating-line intersection. The limiting lines at `w=0,∞` are the
two tangent trisecants. The pairing factors through `C/iota`, with
quotient coordinate `w=u^2`.

The union of these paired secants is the irreducible cubic ruled surface

```
R : x0*x2^2-x1^2*x3=0.
```

Its singular locus is the line `E_+`; a general point of that line is a
double point. The other fixed line `E_-` is a directrix too. Indeed,
`S_w` joins `[1:0:0:w^2]∈E_+` to `[0:1:w:0]∈E_-`: the first endpoint
has two possible parameters and the second has one. This explains the
double line without appealing merely to an implicit equation. At `p0,p∞`
the local equation is a pinch-point form `z^2-x^2*y`; these are the two
ramification points of the degree-two map from the ruling parameter to
`E_+`. On `Q` there is the useful divisor identity

```
R|Q=C+L_0+L_∞,
```

since the Segre pullback of its equation factors as
`A0*A1*(A1*B0^3-A0*B1^3)`. The residual conic class `(2,0)` thus
consists precisely of the two endpoint tangent trisecants.

For distinct osculating planes, their intersection line avoids `C`
unless the parameters are interchanged by `iota`. This also follows
from taking the common divisor of `3a+(-a)` and `3b+(-b)`.

## 3. Bitangency gives a different correspondence

A plane bitangent at distinct finite points `a,b` has section
`(u-a)^2*(u-b)^2`. The vanishing middle coefficient is

```
a^2+4*a*b+b^2=0.
```

Thus `b=r*a`, where `r=-2+sqrt(3)` or its inverse
`r^-1=-2-sqrt(3)`. **The two contact points of a bitangent plane are not
paired by `iota`.** Instead `iota` sends one bitangent pair `{a,b}` to
another pair `{-a,-b}`. Relative to the two ramification points, the
unordered multiplicative ratio satisfies `r+r^-1=-4`.

For such `a,b` the plane is

```
B_{a,b}: a^2*b^2*x0-2*a*b*(a+b)*x1-2*(a+b)*x2+x3=0.
```

There are no bitangents at one endpoint and a distinct point: the same
middle-coefficient condition excludes them. The compactified family
has two degenerate members, with sections `4p0` and `4p∞`, exactly the
hyperosculating planes.

A coordinate-free organization uses `Sym^2(C)≅P2`. An unordered
length-two divisor has binary quadratic equation
`h=alpha*s^2+beta*s*t+gamma*t^2`; its doubled divisor is a hyperplane
section exactly when `h^2∈W`, namely

```
beta^2+2*alpha*gamma=0.
```

This is a smooth conic in `Sym^2(C)`. Squaring maps it to a rational
quartic curve of bitangent planes in the dual projective space. It
meets the diagonal (double-point divisors) in exactly the two endpoint
divisors, with intersection multiplicity two at each: the diagonal is
`beta^2-4*alpha*gamma=0`, and the two conics have the same tangent
line at either intersection. The ordered correspondence on `C×C` is the union of the two
graphs `b=r*a` and `b=r^-1*a`, exchanged by interchanging the factors.

## 4. Incidence identities

For a generic `a`, the tangent line `T_a` lies in `H_a`, in the tangent
plane to `Q`, and in the two bitangent planes at `a`. In particular,

```
H_a ∩ B_{a,r*a}=T_a.
```

Any two distinct tangent lines are coplanar, and hence intersect, exactly
when their contact points form a bitangent pair. This is because a plane
containing both tangent lines has two double zeros in its section,
and conversely the bitangent plane contains both lines. In particular
`T_a` and `T_-a` are skew for nonzero finite `a`.

The plane tangent to `Q` at `c(a)` has section

```
(u-a)*(u^3-a^3),
```

and cuts `Q` in `L_{a^3} ∪ M_a`. Thus its section is
`2[a]+[zeta*a]+[zeta^2*a]` for a primitive cube root `zeta`, with the
endpoint limits `4p0,4p∞`. In contrast, a nonendpoint osculating plane
cuts `Q` in a smooth conic with section `3[a]+[-a]`; a nondegenerate
bitangent plane cuts it in a smooth conic with section `2[a]+2[b]`.
Their plane determinants are respectively `3*a^4` and `9*a^2*b^2`,
so neither kind is a tangent plane to `Q` away from the endpoints.

More generally, if distinct planes `H,K` have section divisors `D_H,D_K`,
the scheme `C∩(H∩K)` is exactly their common divisor
`min(D_H,D_K)`. Locally on the smooth curve this is the equality
`(t^h,t^k)=(t^min(h,k))`. It gives the preceding line incidences without
mistaking contact multiplicities in a plane for line-intersection
multiplicities.

## 5. Scope and novelty boundary

These are elementary projective-geometric statements reconstructed here,
not a literature-priority claim. No normal-bundle splitting or accepted
degree-four exclusion is reproved or used. The configurations by
themselves say nothing about the existence of higher-degree STCI pairs.
Their potential application must retain the distinction between the
length-three ruling lines, the length-two paired secants, and the
length-four hyperosculating **plane** sections.
