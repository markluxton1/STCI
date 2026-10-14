# Torsion detected on an ample smooth rational curve

Date: 2026-10-14.
Author: `cyclic_cover_structure`, independently checking a proposal from
`conductor_general` and the root research agent. Local counterexample and
local Kummer refinement: `local_torsion_curve`.

Status: **NEW PROOF WRITTEN HERE.** Accepted repository results are premises,
not recomputed. No novelty claim is made. This note concerns normal carriers;
it does not eliminate all normal carriers or resolve the universal STCI
problem.

## 1. An intrinsic torsion-detection theorem

Let `X` be a normal integral projective surface over an algebraically closed
field `k`. Let `C` be a smooth rational prime curve. Assume that some positive
multiple `M C` is an ample effective Cartier divisor. In characteristic `p>0`,
only torsion of order prime to `p` is considered in this section. There is no
restriction on torsion orders in characteristic zero.

**Theorem.** A torsion Weil class `T` which is Cartier at every point of `C`
is zero in `Cl(X)`. Consequently the restriction homomorphism

```
Cl(X)_tors -> product_{P in C intersect Sing(X)} Cl(O_{X,P})
```

is injective (on prime-to-`p` torsion in characteristic `p`). If `T` has exact
order `t`, then

```
t = lcm_{P in C intersect Sing(X)} order(T_P).
```

The empty least common multiple is one. In particular this theorem detects
torsion at singularities **on `C`**, independently of singularities elsewhere
on the surface. It does not assert that `Cl(X)` is torsion-free.

### Proof of the cyclic-cover construction

Choose a Weil divisor representing `T`, write `t T=div(phi)`, and form the
usual cyclic reflexive algebra

```
A = direct_sum_{i=0}^{t-1} O_X(iT),
```

where multiplication crossing degree `t` uses the isomorphism
`O_X(tT)->O_X`, `f -> f phi`. Generically this is the Kummer algebra
`k(X)[z]/(z^t-phi)`.

It is a field. Indeed, `k(X)` contains all `t`-th roots of unity, and Kummer
irreducibility fails only if `phi` is a `q`-th power for a prime `q` dividing
`t`. Such a power would give
`div(psi)=(t/q)T`, contradicting the exact order `t`. Equivalently, the
Kummer extension has degree equal to the order of the class of `phi` in
`k(X)^*/k(X)^{*t}`; that order is `t` by the same divisor argument.

The relative spectrum `Y=Spec_X A` is finite, integral and projective. It is
normal: every summand is reflexive, hence has depth two at the closed points
of the normal surface; the finite algebra is therefore `S2`. At every
codimension-one point of `X`, `T` is Cartier, and its cyclic algebra is
finite etale because `t` is invertible. Thus `Y` is regular in codimension
one, and the `R1+S2` criterion applies. These facts can also be obtained by
normalizing `X` in the Kummer field; the displayed reflexive algebra is that
normalization. The cover has cyclic group `mu_t` and is etale outside the
non-Cartier locus of `T`, a finite set. Its reflexive pullback of `O_X(T)`
is trivial.

These precise construction statements agree with Ambro, *Cyclic covers and
toroidal embeddings*, Section 4, Lemmas 4.1--4.2, [primary paper
PDF](https://arxiv.org/pdf/1310.3951). Etaleness near the Cartier locus here
is established directly by the local equation `w^t=unit`; the proof does
not use an assertion of etaleness at arbitrary non-Cartier singular points.

### Proof of the torsion-detection assertion

If `T` is Cartier at every point of `C`, its invertible locus is an open
neighborhood of `C`. The cyclic cover is finite etale on that neighborhood.
Therefore `Y x_X C -> C=P1` is finite etale of degree `t`. Each connected
component is a smooth projective curve finite etale over `P1`. The
Riemann--Hurwitz formula shows that its degree is one: a degree-`e`
component would have `2g-2=-2e`, impossible for `e>1`. Thus this inverse
image consists of `t` pairwise disjoint copies of `P1`.

On the other hand `D=pi^*(M C)` is an ample effective Cartier divisor on
the normal integral projective surface `Y`, with support exactly
`pi^{-1}(C)`. Such support is connected. Here is a proof retaining all
nilpotent layers of the multiple divisor. A normal surface is
Cohen--Macaulay and has a dualizing sheaf `omega_Y`. Serre duality and
Serre vanishing give, for sufficiently large `n`,

```
H^1(Y,O_Y(-nD)) = H^1(Y,omega_Y(nD))^* = 0.
```

Also `H^0(Y,O_Y)=k` and `H^0(Y,O_Y(-nD))=0`. From the exact sequence for
the effective Cartier divisor `nD` one obtains

```
H^0(nD,O_{nD}) = k.
```

A disconnected support would give a nontrivial idempotent in this ring,
a contradiction. Hence `t=1`.

For the exact local-order formula, let `h` be the least common multiple
of the local orders of `T` at the finite set `C intersect Sing(X)`.
Every local order divides `t`, so `h` divides `t`. The class `hT` is
Cartier at every point of `C`, is torsion, and has order `t/h`. The
assertion just proved gives `hT=0`; therefore `t=h`.

The proof works without an ambient projective space and without a global
fundamental-group theorem for `X`. More generally it works if `C` is a
proper connected reduced curve with no nontrivial finite etale covers,
provided an ample effective Cartier divisor has support `C`.

## 2. Exact normal-carrier formula for the quartic

Let `X subset P3` be a normal integral degree-`a` hypersurface in
characteristic zero, containing the accepted smooth rational quartic
`C0`. Put `H=O_X(1)` and

```
g = gcd(a,4),  r = a/g,  s = 4/g,
Delta_0 = r[C0] - s[H].
```

Assume `Delta_0` is torsion of exact order `t`. This is the primitive
class of a hypothetical mate; it gives the accepted first relation

```
m C0 ~ b H,  m = t r,  b = t s.
```

In particular `m C0` is ample Cartier, so the theorem applies. For each
`P in C0 intersect Sing(X)`, let `n_P` denote the exact local Cartier
index of `C0`, that is, the order of `[C0]` in `Cl(O_{X,P})`.
It is finite because `m C0` is Cartier. The hyperplane class is locally
principal, whence `Delta_{0,P}=r[C0]_P` has order

```
k_P = n_P/gcd(n_P,r).
```

Therefore

```
t = lcm_P k_P,
b_min = (4/g) lcm_P [n_P/gcd(n_P,a/g)].
```

For a normal carrier there is no normalization-conductor exponent.
The accepted primitive-ray theorem therefore says that all mate degrees
on this carrier are exactly the positive multiples of `b_min`.

This is a **conditional exact formula**, not a converse based only on
local indices. Finite local indices alone do not imply that
`Delta_0` is torsion: after local Cartier defects are removed, an
infinite-order global Cartier class can remain.

Accepted exclusion of all mates of degree at most four now implies the
necessary condition

```
(4/g) lcm_P k_P >= 5.
```

Thus the following whole normal-carrier classes are excluded at once:

* carriers for which `C0` avoids `Sing(X)`;
* carriers for which every `n_P` divides `a/g`;
* more generally, carriers for which `(4/g) lcm_P k_P <= 4`.

The possible torsion orders are consequently constrained uniformly:

```
g=1: t>=2;  g=2: t>=3;  g=4: t>=5.
```

These are necessary conditions on a hypothetical mate, not an exhaustive
carrier classification. No bound on `a`, on the local indices, or on
their least common multiple has been proved here.

## 3. Failure shield: local order is not curve ramification

A local cyclic class cover can have several branches over a smooth
curve, meeting above the surface singularity. Normalizing those branches
can remove the meeting and lose information needed for the connectedness
argument. In particular a local class order cannot simply be substituted
as a ramification index in Riemann--Hurwitz.

An explicit characteristic-zero example is

```
R = k[[x,y,z]]/(x^2 + z y^2 + z^3),
C = V(x,z).
```

This is a normal isolated hypersurface singularity and `C` is the smooth
`y`-axis. One has `div_R(z)=2C`; the ideal `(x,z)` is not principal at
the origin (its two generators remain independent modulo the maximal
ideal times the ideal). Thus `[C]` has exact local order two.

Adjoining `t` with `t^2=z` and setting `u=x/t` gives the normal cyclic
cover

```
B = k[[u,y,t]]/(u^2+y^2+t^4),
x=t u,  z=t^2.
```

The involution is `(u,y,t)->(-u,y,-t)`, and its invariant ring is `R`.
Its only fixed point is the origin, so the cover is etale outside that
point. The reduced inverse image of `C` is

```
t=0,  u= i y   union   t=0,  u=-i y.
```

It has two branches meeting at the origin. Each normalized branch maps
isomorphically to `C`; its ramification index is one, although the local
class order is two. This example is local and does not assert that this
configuration occurs on a global quartic carrier with a mate. It rules
out the general local equality needed for that shortcut.

There are examples with **arbitrarily large** local class order and
normalized-curve ramification one, even among `A`-type hypersurface
singularities. Let

```
R_N = k[[x,y,z]]/(xy-z^N),
C_a: x=z^a, y=z^(N-a),  1<=a<N.
```

This curve is smooth because its local ring is `k[[z]]`. Write

```
g0=gcd(N,a),  n=N/g0.
```

The cyclic quotient presentation of `R_N` is the invariant ring of
`k[[u,v]]` under `mu_N` acting with weights `(1,-1)`, where
`x=u^N`, `y=v^N`, `z=uv`. The reduced inverse curve is cut out by

```
q=u^(N-a)-v^a.
```

Its semi-invariant character has weight `-a` and exact order `n`.
Consequently `[C_a]` has exact order `n`. To see the exactness without
assuming a class-group classification, `q^n` is invariant and has
divisor `n C_a` downstairs. If a rational function downstairs had
divisor `j C_a`, its pullback would be `q^j` times a unit upstairs.
This unit is semi-invariant; its nonzero constant term forces its
character to be trivial. Hence `N` divides `a j`, so `n` divides `j`.

The class cover is the quotient by the kernel `mu_{g0}` of this
character. It is

```
B = k[[U,V,z]]/(UV-z^g0),
x=U^n, y=V^n.
```

On the generic point of the curve its algebra is `U^n=z^a`. Thus there
are `gcd(n,a)=gcd(n,g0)` normalized branches, each having ramification
index `n/gcd(n,a)`. Given **any** `n>=2` and any `e` dividing `n`,
take `b=n/e`, `N=n b`, and `a=b`. Then the local class order is `n`,
the number of branches is `b`, and every branch has ramification `e`.
In particular `N=n^2,a=n` gives `n` smooth branches mapping
isomorphically to `C_a`. They meet above the surface singularity.

This family proves that local Cartier indices cannot be bounded using
the normalized-curve ramification alone. It does not produce global
fixed-degree hypersurface carriers with unbounded indices.

The independent local Kummer calculation is recorded in
`2026-10-14-cyclic-cover-local-smooth-curve.md`: if `div(f)=nC`, choose
`a` with `v_C(a)=1`, and let `h=a^n/f`. Then `h` is regular, nonzero
on the generic point of `C`, and if `ell` is the order of `h|_C` at
the closed point in the smooth curve parameter, the full local class
cover has

```
gcd(n,ell) normalized branches,
ramification index n/gcd(n,ell) on each branch.
```

The residue class `ell mod n` is independent of the choices. The
ramification invariant is the fractional local intersection class
`ell/n mod Z`; it can be zero for a nontrivial divisor class.

## 4. A conditional global budget retaining the gluing

This additional calculation was independently audited by
`local_torsion_curve`. Retain the normal quartic-carrier setup of section 2
and its degree-`t` cyclic cover `pi:Y->X`. Put `H_Y=pi^*H` and let `D` be
the **reduced** inverse curve. Impose the extra hypothesis that `D` is
Cartier. The primitive relation alone does not imply this hypothesis.

The cover is etale in codimension one. Since the base hypersurface is
Gorenstein, the reflexive dualizing sheaf on `Y` agrees away from
codimension two with `pi^*omega_X` and hence agrees with it everywhere.
Thus `Y` is Gorenstein and

```
K_Y=(a-4) H_Y,  H_Y^2=t a,  H_Y.D=4t,
r D ~ s H_Y,  D^2=16t/a.
```

Adjunction to the Cartier curve gives

```
p_a(D)=1+2t(a-4)+8t/a.
```

Let `R` be the total Riemann--Hurwitz ramification of all components of
the normalization of `D` over `C0=P1`, and let `delta` be the sum of the
local delta invariants of `D`. Their total covering degree is `t`.
The normalization exact sequence and Riemann--Hurwitz, allowing
disconnected normalization, give

```
p_a(D)=1-t+R/2+delta.
```

Consequently

```
delta+R/2 = t(2a-7+8/a),
a divides 8t.
```

The finite map `D->P1` is flat because the reduced Cartier curve is
Cohen--Macaulay and has no component mapped to a point. Its trace
discriminant has degree

```
R+2delta = 2t(2a-7+8/a).
```

This is the global budget which a ramification-only argument omits. It
is a structural formula, not yet a contradiction. For example the
unramified local `A_(n^2-1)` family has the ordinary `n`-fold point
`U^n=z^n` as inverse curve, with `delta=n(n-1)/2`. If the local class
of `Delta_0` generates this order-`n` local class of `C0`, the global
degree-`t` cover has `t/n` such local copies. Their combined contribution
gives the necessary bound

```
n-1 <= 2(2a-7+8/a).
```

This bound is uniform in the mate degree **within the stated local
singularity stratum and the extra Cartier-inverse hypothesis**. It does
not bound arbitrary local indices on arbitrary carriers. Obtaining an
analogue with the residual non-Cartier inverse curve is an open next step.

## 5. What this proves and what remains

The new degree-independent gain is exact localization of the global
torsion obstruction to the finite singular set on the hypothetical
ample rational support. Normal-carrier searches can organize themselves
by those local indices rather than by separate mate degrees. The proof
also applies to arbitrary smooth rational curves with an ample Cartier
multiple and to prime-to-characteristic torsion in positive
characteristic.

The unresolved step is to bound or eliminate the allowable local indices
for **all** normal hypersurface carriers of `C0`, while retaining the
global primitive relation. The local cover may have singularities and a
singular, reducible inverse image of `C0`; its normalization need not be
rationally connected or yield a Hurwitz contradiction. Finite local
indices are necessary but do not certify the global relation. No
statement here covers nonnormal or entirely thick carriers.

For comparison, a separate standard hypersurface route uses the
simple-connectedness of a complex projective hypersurface, stated in
Maxim, *On the topology of complex projective hypersurfaces*, Proposition
2.6, [primary author PDF](https://people.math.wisc.edu/~maxim/hyp_survey.pdf),
and the local class-group exact sequence. The proof above is stronger in
its geometric scope and is self-contained apart from standard Kummer
theory, Serre's normality criterion, Serre duality, and Serre vanishing.

