# Normal carriers: global torsion is exactly the local index obstruction

Date: 2026-10-14. Author: `conductor_general`.
Status: **NEW PROVED STRUCTURAL RESULTS AND CONDITIONAL ALL-DEGREE
EXCLUSIONS; independent new-proof audits recorded below.**

Accepted input, not recomputed: the fixed characteristic-zero curve
`C0=[s^4:s^3t:st^3:t^4]` has no integral carrier of degree at most four
with a mate of any positive degree. The
[Cartier-ray theorem](2026-10-13-generalization-conductor-theorem.md)
is also an accepted input for this continuation. No claim is made
that all normal carrier classes have now been excluded.

## 1. Immediate torsion-free class-group exclusion

Let `X subset P^3` be a normal integral surface of degree `a`, containing
`C0`, over an algebraically closed characteristic-zero field. Put

```
g = gcd(a,4),  mu = a/g,  v = 4/g,
Delta_0 = mu[C0] - v[H] in Cl(X).
```

Normality makes the carrier generically regular along `C0`, so a mate
of degree `b` has divisor `m C0` and intersection gives `4m=ab`.
Thus every possible pair is `(m,b)=k(mu,v)`. A mate exists on `X`
if and only if `Delta_0` is torsion; if its exact order is `t`, the
mate degrees on `X` are exactly

```
b = k t v,  k=1,2,3,... .
```

There is no normalization/conductor factor, since `X` is normal.
The effective divisor realizing the first relation gives a section
of `O_X(tv)`, which lifts to an ambient form by the hypersurface
sequence and `H^1(P^3,O(tv-a))=0`.

If `Cl(X)` is torsion-free, then `Delta_0=0`; it gives a mate of
degree `v<=4`. That mate is itself an integral carrier of `C0` only
after passing to an irreducible factor: some factor of its defining
form vanishes on the integral curve, and its degree is at most four.
Its intersection with `X` still has support exactly `C0`, because
the factor's intersection is contained in the full mate's support.
The factor cannot divide the equation of the distinct integral
carrier `X`; hence it gives an STCI presentation with an integral
carrier of degree at most four. This contradicts the accepted input.

**Therefore no normal integral carrier with torsion-free `Cl(X)` can
occur, in any carrier degree.** The same factor argument excludes
any mate of degree at most four, regardless of the degree of `X`.

Every normal survivor must have nonzero torsion `Delta_0`, with

```
t >= 2 if g=1;  t >= 3 if g=2;  t >= 5 if g=4.
```

These are exclusions based on an existing hypothetical mate, not a
claim that a torsion class exists on arbitrary normal hypersurfaces.

## 2. A self-contained rational-ample local detection theorem

**Theorem.** Let `X` be a normal integral projective surface over an
algebraically closed field of characteristic zero. Let `C subset X`
be a smooth rational prime curve for which some positive multiple
`m C` is an ample Cartier divisor. Then localization gives an
injection

```
Tor Cl(X) -> product_{P in C} Cl(O_X,P).
```

More precisely, the order of any torsion Weil class `T` is exactly
the least common multiple of its local class orders at points of
`C`. Only finitely many singular points can contribute.

The hypothesis on `C` is satisfied by a mate: if `div(G)=m C` on a
projective hypersurface, then `O_X(m C)=O_X(b)` is ample. No claim
that reduced `C` itself is Cartier is used.

### Proof by a connected cyclic cover

First suppose a torsion class `T` is Cartier at every point of `C`,
and let its exact order be `t>1`. Choose a representing Weil divisor
`D` and a rational function `f` with `div(f)=tD`. Form the cyclic
cover associated with a `t`-th root of `f`, taking the normalization
in that function-field extension.

The extension has degree exactly `t`. Indeed, since the ground
field contains all roots of unity, a reducible Kummer polynomial
`Z^t-f` would make `f` a `p`-th power for some prime `p|t`. The
equality of divisors would then make `(t/p)D` principal, contradicting
the exact order of `T`. Thus the resulting finite normal projective
surface `Y` is integral and connected. Finiteness of normalization
holds for varieties over a field.

Equivalently, this is the standard reflexive cyclic algebra built
from the powers of `O_X(D)`. In codimension one it is an unramified
Kummer cover: the valuations of `f` are divisible by `t` and `t` is
invertible. Thus it is quasi-etale. Wherever `D` is Cartier, the
reflexive sheaf is an actual line bundle and its torsion
trivialization defines a finite etale `mu_t`-torsor. Since `D` is
Cartier at all points of `C`, the cover is finite etale on a
neighborhood of `C`.

Its restriction over `C=P^1` is a finite etale cover of degree `t`.
Such a cover is the disjoint union of `t` copies of `P^1`: for each
connected component, Riemann--Hurwitz for an unramified separable
cover gives `2g-2=-2d`, forcing `d=1`. Therefore the support of
`pi^*(m C)` is disconnected.

On the other hand, `pi^*(m C)` is an ample effective Cartier divisor
on the normal integral projective surface `Y`. Its support must be
connected. Here is a direct proof retaining the possibly singular
surface. A normal surface is Cohen--Macaulay and has a dualizing
sheaf. For an ample effective Cartier divisor `A`, Serre duality
and Serre vanishing give, for all sufficiently large `n`,

```
H^1(Y,O_Y(-nA)) = H^1(Y,omega_Y(nA))^* = 0.
```

Since `H^0(Y,O_Y)=k` and `H^0(Y,O_Y(-nA))=0`, the exact sequence
of `nA` gives `H^0(nA,O_{nA})=k`. Disconnected support would give a
nontrivial idempotent and at least two independent global sections,
a contradiction.

Hence a torsion class Cartier along `C` must be zero. Now let `T`
have order `t`, and let `h` be the least common multiple of its local
orders along `C`. Each local order divides `t`, so `h|t`. The class
`hT` is Cartier at every point of `C`; Cartierness is open, so it is
Cartier on a neighborhood of `C`. It is torsion and therefore zero
by the preceding argument. Thus `t|h`, and `t=h`.

This proof does not use simple connectedness of the entire surface,
the Picard group of a hypersurface, or smoothness of `Y`. In positive
characteristic the same proof applies to torsion of order prime to
the characteristic. No assertion about wild `p`-torsion follows.

## 3. Exact index formula on every normal `C0` carrier

Assume a mate on a normal degree-`a` carrier exists. For
`P in C0 intersect Sing(X)`, put

```
r_P = order([C0] in Cl(O_X,P)),
R   = lcm_P r_P,
```

with an empty least common multiple equal to one. These local
Cartier indices are finite, because the mate makes a positive
multiple of `C0` Cartier. The local class of `Delta_0` is
`mu[C0]`, since `H` is Cartier. Consequently its local order is

```
q_P = r_P/gcd(r_P,mu).
```

The theorem of section 2 applies because the hypothetical mate makes
a multiple of `C0` ample. It therefore gives

```
t = lcm_P q_P = R/gcd(R,mu),
b_min = v R/gcd(R,mu).
```

The equality between the least common multiple and the last quotient
follows prime by prime: the valuation is
`max(0,max_P ord_l(r_P)-ord_l(mu))`.

**There is no additional invisible global torsion factor.** The
entire order of the primitive normal-carrier class is detected by
the Cartier indices of the smooth curve at the singular points it
actually meets.

This is a necessary formula under existence of a mate. Finite local
indices alone do **not** prove that `Delta_0` is globally torsion:
its residual Cartier class can still have infinite order. One must
not invert this implication without a separate global relation.

## 4. Cartier-index integrality and new all-degree exclusions

The global Cartier index of `C0` is exactly `R`: a Weil divisor on
a normal surface is Cartier if and only if it is Cartier at every
point, and its local classes are already zero at the regular points
and away from its support. Hence `R C0` is an actual Cartier divisor.
Under a hypothetical mate, `C0` is numerically `(4/a)H` and

```
C0^2=16/a,
deg(O_X(R C0)|C0) = 16R/a in Z.
```

The latter degree is integral because `O_X(R C0)` is an actual line
bundle restricted to the smooth projective curve. Therefore

```
a divides 16R.
```

This is separate from the torsion order `t` of `Delta_0`: the global
Cartier index of the curve is `R`, whereas `t=R/gcd(R,mu)`. Keeping
those two integers distinct avoids a false divisibility claim.

### Index-dividing-degree exclusion

If every local Cartier index of `C0` divides the carrier degree
`a`, then `R|a=g mu`, hence

```
R/gcd(R,mu) divides g.
```

Under a hypothetical mate, the exact index formula gives
`b_min = (4/g)t <=4`, contradicting section 1. Therefore:

**No normal integral carrier of any degree can admit a mate if all
local Cartier indices of `C0` divide its degree.**

It suffices that the actual indices divide `a`; the full local
class groups need not be finite or have exponent dividing `a`.

### Ordinary nodes along `C0`

At an ordinary double point in characteristic zero, the completed
surface local ring is `k[[x,y,z]]/(xy-z^2)`, whose class group is
`Z/2`. Thus the local index of any Weil curve divides two. The same
bound holds in the algebraic local ring: if the completed reflexive
module becomes invertible, faithful flat descent makes the original
module invertible. This concerns points on `C0`; singularities
elsewhere do not enter the index formula.

For even `a`, every contributing index divides `2|a`. The preceding
all-degree theorem therefore proves:

**Every even-degree normal carrier whose singular points on `C0`
are ordinary nodes is excluded.** Its singularities away from `C0`
can be arbitrary normal surface singularities.

For odd `a`, `g=1` and `mu` is odd. The exact order divides two.
Before using integrality, its only possible nontrivial torsion order
is two and its first mate degree would be eight. But `R<=2` gives

```
a divides 16R divides 32.
```

No odd `a>=5` divides 32, and the smaller carrier degrees are already
excluded. Combining this with the even-degree argument proves:

**Every normal carrier whose singular points on `C0` are ordinary
nodes is excluded, in every carrier degree and every mate degree.**
Its normal surface singularities away from `C0` remain unrestricted.
This is a new structural closure; it is not a rerun of an old
degree-by-degree nodal certificate.

### A bounded-index carrier class

More generally, if all local indices divide a fixed integer `L`,
then under a mate

```
t divides L/gcd(L,mu),
b_min <= (4/g) L/gcd(L,mu).
R divides L,  a divides 16R,  hence a divides 16L.
```

Thus a carrier class with bounded local index exponent has both a
uniform mate-degree bound and a **finite list of possible carrier
degrees**. Retain only divisor pairs

```
R|L,  a|16R,  a>=5,
(4/g) R/gcd(R,a/g) > 4.
```

Elementary exact divisor arithmetic gives:

| Common bound `L` on local indices | Surviving `(a,R,t,b_min)` |
| --- | --- |
| 2 | none |
| 3 | none |
| 4 | none |
| 6 | none |
| 12 | `(6,12,4,8)` and `(8,12,6,6)` |

For `L=12`, the possible `R` are `1,2,3,4,6,12`. The first five
give no survivor. For `R=12`, the carrier degrees at least five
dividing 192 are
`6,8,12,16,24,32,48,64,96,192`; their respective first mate degrees
are `8,6,4,3,2,3,1,3,1,1`. Only the first two exceed four.
The corresponding elementary calculation is preserved in
`research/computations/normal_carrier_index_reduction_2026_10_14.py`.

Consequently all normal carrier classes with on-curve local indices
dividing `2`, `3`, `4` or `6` are excluded across all degrees.
For indices dividing 12, all degrees reduce to just the carrier/mate
pairs `(6,8)` and `(8,6)`, with actual global curve index `R=12`.
The first mate degree refers to the minimal mate on that chosen
carrier; no existence of either pair is asserted.

The two rows give the **same unordered defining degree pair `(6,8)`**.
A minimal mate form is integral: if it had a proper irreducible
factor vanishing on the integral curve, that factor would be a mate
on the same carrier of smaller degree, contradicting minimality.
The resulting complete-intersection scheme has generic multiplicity

```
(6*8)/deg(C0)=12
```

along `C0`. Thus the entire normal-carrier class with on-curve
indices dividing 12 collapses to this one degree pair and one
generic multiplicity, retaining the true possibility of simultaneous
singular points and nonprimitive structures. At least one defining
surface has the normality and index hypotheses; normality of the
other defining surface is not inferred.

For context, the detailed primary class-group tables in
Brevik--Nollet, Sections 4.1.1--4.1.3, give exponents two or four for
`D_n`, three for `E6`, two for `E7`, and one for `E8`. Thus all
`D/E` rational-double-point singularities along `C0` have indices
dividing 12 and lie in this two-pair reduction. So do mixtures with
`A1,A2,A3`. Primary source:
[*Local Picard Groups*](https://arxiv.org/pdf/1110.1867).
Use its detailed subsections: the introductory Section 4 summary
contains parity and `E6/E7` assignment errors which the detailed
subsections correct.

### General integral curves, not just the rational quartic

The hypersurface Picard route in section 5 removes the rationality
hypothesis from the index formulas. Let `C` be **any integral**
degree-`e` projective curve on a normal degree-`a` hypersurface in
`P^3` over an algebraically closed characteristic-zero field, and
suppose it has a mate on that carrier. Put `g=gcd(a,e)` and let
`R` be the least common multiple of the actual local Cartier indices
of `C`. All those indices are finite by the mate. Then

```
Delta_0 = (a/g)[C] - (e/g)[H],
t = order(Delta_0) = R/gcd(R,a/g),
b_min = (e/g) R/gcd(R,a/g),
a divides e^2 R.
```

The first two formulas use the torsion-free Picard group and the
localization kernel; the last uses the integer degree of the actual
line bundle `O_X(RC)` restricted to the integral curve. Its numerical
degree is `R C^2=R e^2/a`. Degree of a line bundle remains an integer
on a possibly singular integral projective curve.

Consequently, if the actual on-curve Cartier indices all divide
`L`, then

```
a divides e^2 L.
```

Thus **a bound on local curve indices gives a finite carrier-degree
reduction for all integral curves**, in every mate degree. This does
not impose or prove such an index bound for unrestricted carriers;
it identifies precisely the new geometric invariant whose control
would turn the normal branch into a finite carrier problem.

## 5. Primary literature and the Pic/Cl distinction

The exact literature input inspected for projective hypersurfaces is
SGA 2, Expose XII, Corollary 3.5, printed page 120, PDF page 128 in
the recomposed edition. Applied to the ample hypersurface section
inside the regular threefold `P^3`, it identifies its etale
fundamental group with that of `P^3`. In characteristic zero the
Kummer sequence, and divisibility of the constant units, then give
`Pic(X)[n]=0` for every `n`. Thus **Pic(X) is torsion-free**.
Primary source: [SGA 2](https://wstein.org/sga/circle/SGA2.pdf).

For a normal surface, an elementary localization sequence has kernel
`Pic(X)` in

```
Cl(X) -> product_{P in Sing(X)} Cl(O_X,P).
```

Indeed a Weil class is locally trivial at all singular points
exactly when its reflexive sheaf is everywhere invertible. Hence,
with the preceding Picard theorem, localization is injective on
`Tor Cl(X)`. The class `Delta_0` is already Cartier away from `C0`,
so only singular points on `C0` contribute. This is an independent
standard-input route to the index formula. The relevant class-group
sequence is also present in Hartshorne--Polini, Proposition 2.2(c),
specialized to a normal surface; see
[*Divisors class groups of singular surfaces*](https://arxiv.org/html/1301.3222).

The new rational-ample cyclic proof in section 2 gives a broader
statement without assuming the Picard group of the whole surface
is torsion-free. It also makes the localization mechanism geometric.

Torsion-free `Pic(X)` does **not** mean torsion-free `Cl(X)`. A
Kummer quartic is the quotient of an abelian surface by its sign
involution, with sixteen isolated nodes. The connected double cover
is etale over the smooth locus. Its nontrivial order-two eigensheaf
there gives nonzero order-two torsion in `Pic(X_reg)=Cl(X)`; if the
eigensheaf were trivial, the cover would split, since units on the
smooth locus extend to constants on the normal projective surface.
The quotient description is documented, for example, in the primary
paper
[*Birational Geometry of Blow-ups of Projective Spaces Along Points
and Lines*](https://academic.oup.com/imrn/article/2021/9/6442/5930818).
This is a failure shield for the blanket assertion that normal
hypersurface class groups have no torsion. It does not supply a
counterexample to the accepted `C0` exclusions.

## 6. What the cyclic cover does and does not control

For a hypothetical `Delta_0` of exact order `t`, its cyclic cover is
quasi-etale, connected and must fail to be etale somewhere on `C0`.
Its degree is now determined exactly by the local index formula.
The pullback of the primitive relation becomes trivial:

```
mu pi^*C0 ~ v pi^*H.
```

This yields an upstairs section in degree `v<=4`, but the covering
surface maps to `X` with degree `t` and is not itself an embedded
surface in `P^3`. The accepted low-degree carrier exclusion cannot
be applied directly to this upstairs section. Its norm recovers a
degree-`tv` mate on `X`.

No contradiction follows merely from `K_Y=pi^*K_X`: for `a>=5`,
the covering surface can have ample canonical divisor just as the
base does. Likewise a cover can pull back the rational curve to
several components meeting over singular points. Local class order
is not automatically the ramification index of the normalization
of one curve component. A Riemann--Hurwitz argument must retain
that distinction.

There is also no bound on local index from smoothness of `C0` or
surface multiplicity alone. The local normal hypersurface

```
xy-z^r=0,   C=(x,z)=0
```

has multiplicity two, contains a smooth curve, and that curve's
local divisor class has order `r`. One may see this using the quotient
map `x=u^r,y=v^r,z=uv` from the smooth plane by
`(u,v)->(zeta u,zeta^(-1)v)`: the curve corresponds to the character
of exact order `r`. Its indices are arbitrarily large. This is a
local failure shield, not a constructed global `C0` carrier.

## 7. Audit record and successor target

The new rational-ample local detection proof was independently
reconstructed by `cyclic_cover_structure`, including Kummer
connectedness, etaleness near Cartier points, and ample-divisor
connectedness on a normal surface. `normal_torsion_primary`
independently inspected the exact SGA 2 hypersurface theorem and
the local class-group route, and audited the local-index and nodal
arithmetic corollaries. It also independently audited
`a|16R` and the full bounded-index divisor table. The new elementary
arithmetic script ran successfully and checked precisely the rows
displayed above. These audits concern new deductions, not a rerun
of accepted low-degree exclusions. The auxiliary proof records are
[normal cyclic-cover torsion detection](2026-10-14-normal-cyclic-cover-torsion-detection.md)
and [primary Picard/local-torsion inputs](2026-10-14-normal-carrier-picard-local-torsion-primary.md).

The remaining normal-carrier target is now sharp: show that the
specific class `Delta_0` cannot be torsion with the required local
indices, or exclude the resulting finite cyclic cover geometry.
The nodal class is now closed across all degrees. More broadly,
on-curve local index exponents dividing `2,3,4,6` are closed, and
exponent 12 leaves only the unordered defining pair `(6,8)`, with
generic intersection length 12. The next exact target in this class
is compatibility of that full local length with the actual index
three/four contributions at the singular points; no primitive-pair
assumption may be imposed, and higher jets must be retained when a
`D_n` curve has index four but large singularity corrections. For
general normal carriers, one needs actual Cartier indices of the
smooth curve at the singular points it meets; multiplicity and the
carrier's Picard group alone are insufficient. All nonnormal and
entirely thick carrier lanes retain their separate conductor and
branch-lattice issues.
