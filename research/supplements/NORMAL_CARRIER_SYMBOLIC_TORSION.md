# normal carrier symbolic torsion

## Integration guide: class-group torsion, index bounds, and the mate problem

The [carrier torsion investigation](#2026-10-14-generalization-normal-carrier-torsion) distinguishes Cartier and Weil divisor information on possibly singular normal surfaces. The [symbolic-triple certificate](#2026-10-14-generalization-normal-carrier-symbolic-triple-certificate) adds a specific primitive structure and first torsion divisor; its [comparison audit](#2026-10-14-generalization-symbolic-triple-torsion-comparison-audit) tracks the cases of different Cartier indices and the scope of strengthened bounds.

The related [normal-index and socle dossier](NORMAL_INDEX_SOCLE_AND_TORSION.md#2026-10-14-generalization-normal-index-general-scope) records inequalities that do not presuppose a second equation. The [Rees cycle dossier](REES_RESIDUAL_AND_EXCEPTIONAL_CYCLES.md#2026-10-19-rees-residual-investigation) makes clear why a global degree budget alone does not control every filtered defect.

A normal carrier's symbolic divisor data is **not** by itself a construction of a set-theoretic complete intersection. The local index, actual homogeneous lifting, and residual-support questions remain distinct.

---


Permanent mathematical dossier. Complete source arguments are preserved with their precise hypotheses, conditional scope, calculations, failed approaches, and unresolved boundaries. This grouping does not promote claims to canonical results.

---

## 2026-10-14-generalization-normal-carrier-torsion

# Normal carriers: global torsion is exactly the local index obstruction

Date: 2026-10-14. Author: `conductor_general`.
Status: **NEW PROVED STRUCTURAL RESULTS AND CONDITIONAL ALL-DEGREE
EXCLUSIONS; independent new-proof audits recorded below.**

Accepted input, not recomputed: the fixed characteristic-zero curve
`C0=[s^4:s^3t:st^3:t^4]` has no integral carrier of degree at most four
with a mate of any positive degree. The
[Cartier-ray theorem](OCT13_CONDUCTOR_REES_AND_GENERAL_FRAMEWORK.md#source-2026-10-13-generalization-conductor-theoremmd)
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
[normal cyclic-cover torsion detection](CYCLIC_COVER_AND_MOVING_LINEAR_RIGIDITY.md#2026-10-14-normal-cyclic-cover-torsion-detection)
and [primary Picard/local-torsion inputs](OCT14_QUINTIC_ROOT_AND_NORMAL_CARRIER_REVISIONS.md#source-2026-10-14-normal-carrier-picard-local-torsion-primarymd).

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


---

## 2026-10-14-generalization-normal-carrier-symbolic-triple-certificate

# A symbolic-triple defect certificate for unrestricted normal carriers

Date: 2026-10-14. Author: `socle_audit`.
Status: **PROVED NEW NECESSARY CARRIER-WIDE CERTIFICATE AND STRONGER
POINTWISE-INDEX/DEGREE BOUND.** The all-index-at-most-four exclusion and
the exact local power-socle formula are accepted inputs; they are not
reverified here. The present result does not exclude all normal C0
carriers or resolve C0's STCI status.

Accepted inputs: `2026-10-14-generalization-index12-filtered-compatibility.md`
for the ordinary-layer and local power-socle theorems; the existing
constant-direction pole obstruction for a first relation and its next
normal layer; the already verified C0 apolar kernels and their absence
of degree-zero/one annihilators; and N_C0^* = O(-7)^2. No old symbolic
calculation or accepted nonvanishing statement is rerun.

## 1. Carrier data and an intrinsic normalized budget

Let X = V(F_a) be a normal integral carrier of C0 in characteristic zero,
and suppose a mate G_b exists. Put n = ab/4. The generic CI algebra is
curvilinear. Let B_1 = O(-ell) be the torsion-free first ordinary normal
layer, equivalently the canonical quotient of N_C0^* by the saturated
first-symbol direction of F. Then ell <= 7. Let A_P be the carrier's
first-symbol vanishing order in that saturated line, and let r_P be
the actual local Cartier index of C0 on X. For a local equation h_P
with divisor r_P C0, write D_P^(r) for the full top-power/socle defect
of W_(r_P) = X/(h_P).

These are intrinsic carrier/curve data. Multiplication of h_P by a unit
does not change its local thickening or D_P^(r). Under the hypothetical
mate, r_P divides n, and the accepted exact local formula is

    D_P^(n) = (n/r_P-1)A_P + (n/r_P)D_P^(r).   (1)

The global degrees satisfy

    A = sum A_P = 4a-14+ell,
    D = sum D_P^(n) = (n-1)ell-4(a+b)+14,
    D+A = n(ell-16/a).

Adding A_P to (1), dividing by n, and summing gives the exact
mate-independent necessary relation

    Q := ell-16/a
       = sum_P (A_P+D_P^(r))/r_P.              (2)

In particular the normalized primitive-index defect is

    sum_P D_P^(r)/r_P
       = ell-16/a - sum_P A_P/r_P >= 0.        (3)

This is one simultaneous weighted budget. It neither replaces all
indices by their maximum nor treats distinct singular points as
independent hypothetical presentations.

## 2. Cartier multiples of length two or three are automatically primitive

There is a new useful general fact. A one-dimensional CI supported on
a smooth curve, finite free of generic rank r <= 3 over R = k[[t]],
with curvilinear generic algebra, is primitive everywhere locally.

Its special fiber is a local Artinian CI of length r. An Artinian CI
of embedding dimension two has both defining orders at least two,
and therefore length at least four. Thus the length-two/three special
fiber is curvilinear. Lift a generator z of its maximal ideal. Nakayama
shows that the relative nilradical J is generated by z; purity gives
J^r = 0. The induced surjection R[z]/(z^r) -> A is a map between finite
free R-modules of rank r and is an isomorphism.

Consequently, for actual indices two or three,

    W_r = R[z]/(z^r),
    D_P^(r) = 0.                              (4)

For r=1 the carrier is smooth at P and the same conclusion holds with
the reduced-curve conventions. Thus positive primitive-index defects
can occur only at actual indices at least four. This fact uses lengths
and a relative algebra argument, not a list of Hilbert profiles.

## 3. The global symbolic triple and its first torsion divisor

Suppose ell = 7. The saturated carrier direction is then constant:
the quotient O(-7)^2 -> O(-7) has constant coefficients. Let m be its
fixed first relation and let

    Z_3 = O_X / I_(C0/X)^(3)

be the global symbolic triple. It is pure of dimension one: the
divisorial symbolic ideal is reflexive on the normal surface and has
depth two, so its quotient has depth one. Its generic length is three,
and its ordinary free first layer is the same saturated O(-7).

Let E be the effective divisor measuring its first ordinary layer
torsion. The first actual initial-relation sheaf is

    K_1(Z_3) = O(-7)(-E) tensor k m.           (5)

Its degree-two relation sheaf has rank two and generic span mV. It is
contained in the saturated constant bundle O(-14) tensor mV by generic
vanishing in the torsion-free ambient quotient. Thus precisely the
hypotheses of the accepted constant-direction relation/pole obstruction
apply: rank K_1 = 1, rank K_2 = 2, constant generic first relation, with
the entire divisor E retained.

The resulting necessary condition is

    h_E h_m = 0 in H1(O(deg E-7)).             (6)

The accepted apolar kernels have no nonzero annihilator of degree zero
or one. Therefore

    deg E >= 2.                               (7)

No lci or Gorenstein assumption is placed on Z_3. Those hypotheses are
needed for the local W_r Frobenius identity used below, not for the
first-relation obstruction. In particular the symbolic triple at an
index-two point is generally not a complete intersection.

## 4. Exact index-two periodicity and comparison at higher indices

At an index-two point choose h with divisor 2C. Normal divisorial
valuations give the exact symbolic periodicity

    I_C^(j+2) = h I_C^(j),
    in particular I_C^(3) = h I_C.             (8)

An ambient lift of h belongs to I_C. Hence h I_C has zero first normal
symbols. The symbolic triple's first relation module is exactly the
carrier image R F_1. Its saturation is the fixed line R m. Therefore

    E_P = length(Rm / R F_1) = A_P,  r_P=2.    (9)

This equality retains the actual first-symbol vanishing order A_P and
all higher carrier complexity. From (4), its length-n defect is also
exactly D_P^(n) = (n/2-1)A_P.

For r_P >= 3, the local Cartier multiple W_r surjects onto Z_3 because
h belongs to I_C^(3). Their first relation modules in the same ambient
conormal module V = R^2 satisfy

    M_r subset M_3 subset V.

Both saturate to the same generic carrier relation line L subset V.
Their first-layer torsion modules are consequently L/M_r and L/M_3,
and the first maps onto the second. The accepted pointwise Frobenius
identity for the actual CI W_r gives

    0 <= E_P <= length T_1(W_r)_P
             <= (r_P/2)D_P^(r).              (10)

This direct quotient-of-relation-modules proof avoids any assumption
that the symbolic triple is lci. At r=3, (4) improves (10) to E_P=0.
At r=1 the carrier is smooth and E_P=0 as well.

Combining (7), (9), and (10) gives the new simultaneous certificate

    2 <= deg E
      <= sum_(r_P=2) A_P
          + (1/2) sum_(r_P>=4) r_P D_P^(r).    (11)

Thus every constant-direction normal carrier must have either index-two
contributions or nonzero full primitive-index socle defects at indices
at least four. Index-three contributions are automatically primitive
and cannot clear this first symbolic-triple obstruction.

If no index-two point occurs, at least one D_P^(r)>0. This is also seen
geometrically: if all the W_r were primitive, the symbolic triple would
be primitive everywhere by saturation, with constant first direction,
contradicting the accepted quadratic obstruction.

## 5. Weighted and parity-sensitive forms

The accepted pointwise Frobenius identity gives

    r_P D_P^(r) = 2 sum_i length T_i(W_r)_P.

Thus positive D_P^(r) is at least one for even r_P, and at least two
for odd r_P. If index two is absent, (3) and (11) force

    sum_P D_P^(r)/r_P
      >= min_(actual r_P>=4)
           { 1/r_P if r_P even; 2/r_P if r_P odd }.  (12)

Equivalently, with k_P = n/r_P,

    sum_P k_P D_P^(r)
      >= min_(actual r_P>=4)
           { k_P if r_P even; 2k_P if r_P odd }.     (13)

The more precise first-torsion comparison is

    sum_(r_P>=4) (2n/r_P^2) E_P
       <= sum_P (n/r_P)D_P^(r).               (14)

For an index bound s and no index-two points, (12) is at least 1/s
when s is even and at least 1/(s-1) when s is odd >=5. If all indices
are odd, it is at least 2/s. The s<=3/no-index-two case is impossible
because all Cartier multiples are primitive by Section 2; it is not
a surviving model with a small positive defect.

These are carrier-wide rational and integral certificates. They retain
each r_P and its full D_P^(r), including high D_n corrections at fixed
index. The actual positive term cannot be manufactured by tangent-only
multiplicity reasoning.

## 6. A stronger all-carrier-degree index bound

Let s >= 3 be a bound on every actual on-curve local index. For ell=7,
put A = 4a-7. From (2),

    Q-A/s
      = sum_P A_P(1/r_P-1/s)
          + sum_P D_P^(r)/r_P.                (15)

If any primitive-index defect is positive, the second sum is at least
1/s. If all such defects vanish, (11) forces
A_2 := sum_(r_P=2)A_P >= 2. Then the first sum is at least

    A_2(1/2-1/s) >= (s-2)/s >= 1/s.

Both cases therefore give

    s(7-16/a) >= 4a-6,
    4a^2-(7s+6)a+16s <= 0.                    (16)

This improves the previous coefficient-seven bound by a full unit,
even when index-two points are present. For ell <= 6, the earlier
accepted slope/index inequality is already stronger: monotonicity in
ell yields

    4a^2-(6s+8)a+16s <= 0.

Subtracting (s-2)a shows that it implies (16) for s>=2. Thus (16)
holds for every hypothetical normal C0 carrier of degree a>=5, with
actual indices bounded by s>=3, regardless of ell or mate degree.

In the constant-direction branch with no index-two point, (12) can
improve (16) further by replacing the one-unit payment with s times
the parity-sensitive lower bound. For all odd indices, for example,

    4a^2-(7s+5)a+16s <= 0.                    (17)

The already accepted s<=4 closure is not reverified here. Equations
(16)--(17) are new structural consequences for larger index classes,
and do not themselves exclude unbounded indices.

## 7. Apolar support constraints, not only a scalar payment

The actual divisor E must satisfy (6), not merely have degree at least
two. The accepted apolar kernel description therefore also gives:

* If deg E=2, the constant direction is an endpoint and E is its
  corresponding doubled endpoint divisor.
* If deg E=3, a mixed direction has its unique divisor
  [0]+[-2theta]+[infinity]; an endpoint has its doubled endpoint plus
  one additional point.

The support of E is, by (9)--(10), contained in index-two points or
higher-index points with positive primitive-index defect. Consequently
small-degree E forces these exceptional points to occupy the specific
apolar support positions, simultaneously. A degree-three mixed model
must pay at three distinct curve points; an endpoint model requires
the appropriate doubled point. These are necessary support constraints,
not existence claims for their embedded higher lifts.

## 8. Scope and independent review

The exact normalized budget (2) holds in all normal mate-bearing C0
carriers. The symbolic-triple obstruction needs the constant-direction
branch ell=7; the final scalar bound applies also to ell<=6 because
the previous index inequality is stronger there. Nonconstant directions,
large enough pole divisors, index-two contributions, and positive
higher-index defects remain legitimate continuation strata.

The quotient-of-relation-modules comparison and the coefficient-six
arithmetic were independently reviewed by `higher_moments` in
`2026-10-14-generalization-symbolic-triple-torsion-comparison-audit.md`.
The root independently reconstructed the length-two/three primitive
Cartier-multiple argument and the improved scalar inequality. The
present note supplies the actual proofs; agent agreement is not used
as a substitute for them.



---

## 2026-10-14-generalization-symbolic-triple-torsion-comparison-audit

# Symbolic triple torsion comparison: independent structural audit

Date: 2026-10-14. Worker: `socle_audit/higher_moments`.
Status: **PROVED NEW COMPARISON AND ARITHMETIC CONSEQUENCE, CONDITIONAL
ONLY ON THE EXPLICIT ACCEPTED INPUTS BELOW.** No canonical file edited.

Accepted inputs, not reverified: the fixed C0 normal/conormal coefficients;
the ordinary curvilinear CI free-layer and pointwise Frobenius theorem;
the local power-socle identity; and the fixed constant-direction pole
obstruction forcing `deg E>=2` for the symbolic triple. This assessment
audits the quotient comparison and its new implications, rather than
assuming the symbolic triple is a complete intersection.

Let X be a normal integral carrier of C0, of degree a, with a mate.
At P let r be the actual local Cartier index of C0. A regular local
function h has divisor rC, and `W_r=O_X/(h)` is a local complete
intersection of generic length r. Set

    Z_3 = O_X / I_C^(3),
    L_1(Z_3) = I_C / (I_C^2 + I_C^(3)),
    E_P = length torsion L_1(Z_3).

The symbolic quotient is pure and has generic length three. Its
first-layer relation line has the common saturated F_1 direction;
in the constant-direction branch ell=7 it is
`K_1=O(-7)(-E)`. None of these statements requires Z_3 to be lci.

## 1. Comparison at r>=3

The valuation description of the symbolic power gives
`(h) subset I_C^(3)` when r>=3, and hence a quotient `W_r -> Z_3`.
Complete along the smooth curve parameter and use `R=k[[t]]`.
Let V be the ambient first conormal module, free of rank two over R.
Write

    M_r = kernel(V -> L_1(W_r)),
    M_3 = kernel(V -> L_1(Z_3)).

Then `M_r subset M_3`. Their generic rank-one relation space is the
same F_1 direction, so their R-saturations equal a common line L in V.
Therefore

    torsion L_1(W_r) = L/M_r,
    torsion L_1(Z_3) = L/M_3,

and the map of torsion modules is surjective. In particular

    E_P <= length T_1(W_r)_P
        <= sum_i length T_i(W_r)_P
        = r D_r,P / 2.                         (1)

The perfect Frobenius pairing is used on the actual complete
intersection W_r. It is never used on Z_3. Thus no hidden lci or
Gorenstein assumption on the symbolic triple enters (1).

## 2. Comparison at r=2 and r=1

For r=2, normality and the height-one valuation description give

    I_C^(3) = h I_C.

Indeed division by h subtracts exactly two units of curve valuation
and no valuation at any other prime. The ambient first symbols of
`h I_C` vanish: both factors lie in the ambient curve ideal. Thus
the only first-symbol relation is the carrier F_1, and

    E_P = A_F,P.                               (2)

For r=1, the smooth curve is Cartier on the normal surface; the
surface is smooth there, so `E_P=A_F,P=0`. This is the accepted
smooth-Cartier case, not a new general primitive hypothesis.

Subsequent strengthening, independently reconstructed by `socle_audit`
and the root: the relative CI W_r is automatically primitive when
r<=3. Its special Artinian CI fiber has length below four, hence cannot
have embedding dimension two; Nakayama then makes the whole finite
free algebra R[z]/(z^r). Thus D_2=D_3=0 and E_P=0 for r=3. The full
proof is recorded in
`2026-10-14-generalization-normal-carrier-symbolic-triple-certificate.md`,
Section 2. In (3)--(4), positive defects may therefore be restricted to
r>=4. The s=3/no-index-two case in (5) is impossible; the displayed
2/3 bound is an earlier necessary conditional inequality, not evidence
for a surviving positive-defect index-three model.

Summing (1)--(2), the accepted fixed-direction obstruction gives

    2 <= deg E
      <= sum_(r=2) A_F,P + (1/2) sum_(r>=3) r D_r,P.       (3)

## 3. Positive defects and parity

If there are no index-two points, (3) forces at least one positive
`D_r,P` with r>=3. The pointwise Frobenius identity implies
`r D_r,P` is even; consequently odd r forces `D_r,P>=2` whenever
positive, while even r forces at least one. Thus

    sum_P D_r,P/r >= min_(actual r>=3) delta_r/r,
    delta_r = 1 for r even, 2 for r odd.         (4)

If only r<=s is known and index two is absent, this minimum can be
bounded uniformly by

    eta_3 = 2/3,
    eta_s = 1/s       for even s>=4,
    eta_s = 1/(s-1)   for odd s>=5.              (5)

With no r>=3 available, (3) already contradicts the absence of
index two. The weaker universal estimate from (4) is `1/s`.

## 4. A one-unit improvement of the normal index bound

Let `A=sum_P A_F,P`, `A_2=sum_(r=2) A_F,P`, and retain the accepted
identity

    Q = ell-16/a = sum_P (A_F,P+D_r,P)/r.

Suppose s>=3 bounds all actual indices and ell=7, so the accepted
constant-direction pole obstruction supplies (3). Then

    Q - A/s >= 1/s.                            (6)

There are two exhaustive cases. If a `D_r,P` is positive, it is an
integer at least one and r<=s, so its contribution is at least `1/s`.
If every `D_r,P=0`, equation (3) forces `A_2>=2`, and

    Q-A/s >= A_2(1/2-1/s)
            >= (s-2)/s >= 1/s.

Thus index-two points do not prevent the weaker improvement (6).
In the ell=7 branch, `A=4a-7`, and therefore

    s(7-16/a) >= 4a-6,
    4a^2-(7s+6)a+16s <= 0.                     (7)

When index two is absent, replace `1/s` in (6) by the sharper
`eta_s` of (5), or use the actual-index minimum in (4).

The integer branch ell<=6 is also compatible with (7). The accepted
original bound and its monotonicity in ell give

    4a^2-(6s+8)a+16s <= 0.

For s>=2 the left side in (7) is smaller by `(s-2)a`, so this implies
(7). Hence, after accepting the fixed-direction pole obstruction,
(7) can be used for all ell<=7 with s>=3. The case s<=2 is already
covered by the accepted bounded-index exclusion, and is not inferred
from the new constant-direction argument.

## 5. Scope

The comparison applies to a pure symbolic triple even if it has
special-point non-lci structure. It uses the actual local index and
full CI defect of W_r; surface multiplicity, first-jet smoothness, or
index lcm does not replace those data. This is a stronger necessary
index/degree inequality, not an exclusion of unrestricted normal
carriers, nonnormal carriers, or all STCI presentations of C0.


---

## 2026-10-14-generalization-curvilinear-torsion-and-index12

# Curvilinear ordinary normal layers and local index compatibility

Date: 2026-10-14. Root continuation from the `socle_audit` worker's
index-twelve program. This precursor's new proofs are now independently
accepted in the [full filtered compatibility audit](#2026-10-14-generalization-index12-filtered-compatibility).
The [current theorem and scope record](NORMAL_INDEX_SOCLE_AND_TORSION.md#2026-10-14-generalization-normal-index-socle-theorem)
adds the local power-socle formula, a linear index/degree bound and the
all-degree exclusion of normal C0 carriers with actual on-curve indices
at most four. The sections below retain the earlier intermediate route;
their former pending labels and final next-task language are historical,
superseded by those two accepted records. The unrestricted problem and
actual index-six/twelve strata remain open. Accepted inputs were not
recomputed.

## 1. A theorem for the ordinary nilradical filtration

Let Y be a complete-intersection thickening of a smooth curve C, with
generic transverse algebra curvilinear of length n>=2. Put

```
J=I_C O_Y,  L_i=J^i/J^(i+1),
T_i=torsion(L_i),  B_i=L_i/T_i,  L=B_1.
```

Purity gives `J^n=0` everywhere. Every B_i for 0<=i<n is a line
bundle. The entire torsion sum `T=direct_sum T_i` is an ideal of the
ordinary graded algebra: multiplication of a torsion section with
another graded section remains torsion. Since the ordinary associated
graded algebra is generated by L_1, its torsion-free graded quotient
is generated by B_1. Thus for every i<n multiplication is surjective:

```
L^i -> B_i.
```

A surjection between line bundles is an isomorphism. Consequently

```
B_i=L^i,  including B_(n-1)=J^(n-1).
```

This uses the **ordinary J-adic filtration**. It is not an assertion
that every saturated BF filtration has zero multiplication defect.
The special-point defects here are retained in the torsion T_i and
the inclusion of the top ideal in the actual socle.

Write `deg L=-ell` and

```
J^(n-1)=Soc(Y)(-D),
Soc(Y)=omega_C tensor O_C(4-a-b).
```

Then

```
deg D=(n-1)ell+(2g(C)-2)+deg(C)(4-a-b).
```

Euler characteristic of the complete intersection and the ordinary
filtration gives the exact total torsion budget

```
2 sum_i length T_i = n deg D.
```

Thus first-layer torsion alone supplies a lower bound on the top-socle
defect. This equality does not assume globally primitive structure,
a global retraction to C, or a torsion-free first layer.

## 2. A pointwise strengthening by a Frobenius lattice

The preceding torsion identity holds at each point, with D's actual
local multiplicity, not only after summing over C. Complete at a point
P and choose an ambient parameter t lifting C's parameter. The local
algebra A is finite free of rank n over `R=k[[t]]`: the normal
variables are nilpotent, and Cohen--Macaulayness makes t a
nonzerodivisor. It is a relative complete intersection and hence
`Hom_R(A,R)` is a free rank-one A-module.

Choose z in J whose first class generates the free first-layer
quotient. Its powers generate all the free quotients by Section 1.
Since z^n=0 and its generic powers are independent, they define the
rank-n lattice

```
A0=R[z]/(z^n) subset A.
```

Its induced J-adic filtration is strict: a nonzero coefficient of
the least z-power remains nonzero in that layer's free quotient.
Therefore

```
length_R(A/A0)=sum_i length_R(T_i)_P.
```

Choose a generator lambda of `Hom_R(A,R)` as A-module. Its
multiplication pairing is perfect over R. Finite duality identifies
the actual socle with R via lambda, so if s generates the socle,
`lambda(s)` is a unit. Since z^(n-1) generates the top J-adic ideal,

```
z^(n-1)=t^(D_P) u s,  u a unit.
```

The Gram matrix on the powers 1,z,...,z^(n-1) is anti-triangular;
its determinant is a unit times `lambda(z^(n-1))^n`. Its t-adic
valuation is n D_P. The Gram matrix on an R-basis of A has unit
determinant. A change to a full sublattice doubles its index in the
Gram determinant. Consequently

```
2 sum_i length_R(T_i)_P=n D_P.
```

In particular n odd forces every D_P even. This proof retains all
jets and all local lattice changes. It does not identify a surface
class order with the ramification of a normalized inverse curve.

## 3. The forced length-twelve pair

The accepted bounded-index normal-carrier theorem reduces all C0
carriers whose local indices divide12 to the unordered pair(6,8).
At least one carrier is normal, so its generic normal order is one;
the generic algebra of the CI is curvilinear of length12. Its Loewy
index is eleven, and

```
deg D=11ell-42,
sum_i length T_i=6(11ell-42).
```

The conormal quotient of `O(-7)^2` gives ell<=7, and D effective
gives ell>=4. Thus the four initially necessary global alternatives
are

| ell | degree of the first direction 7-ell | deg D | total layer torsion |
|---:|---:|---:|---:|
|4|3|2|12|
|5|2|13|78|
|6|1|24|144|
|7|0|35|210|

These are consequences of one full filtered-algebra theorem, not
independent profile enumeration or assertions of existence.

## 4. Local class index controls poles in the first-symbol ratio

Let F define the normal carrier, and let a point P on C have local
Cartier index r_P dividing n. If r_P<n, choose a regular local
function h with divisor r_P C on the normal carrier. A mate's local
divisor is n C, hence its restriction is

```
G=u h^(n/r_P),  u a unit.
```

Normality proves u is a unit: its divisor and the divisor of its
inverse are zero at all height-one primes. Lift h into the ambient
curve ideal and u into ambient local units. Since n/r_P>=2,

```
G=tilde(u) tilde(h)^(n/r_P)+F H,
G_1=(H|C) F_1.
```

Thus the meromorphic first-symbol ratio G_1/F_1 is regular at P.
Any poles are supported at actual local index n points. This keeps
the precise index rather than substituting surface multiplicity.

For C0, the carrier first symbols are two binary forms of degree
4a-7. Their saturated direction has degree 7-ell, so their common
zero divisor has degree

```
deg A_F=4a-14+ell.
```

If no local index12 occurs, the ratio is regular everywhere. The
joint first-symbol image is then exactly the F_1 image. Hence
`length T_1=deg A_F`. In the ell=4 row this exceeds the *total*
torsion twelve: it is fourteen for a=6 and twenty-two for a=8.
Therefore ell=4 is excluded under the no-local-index12 hypothesis.
The remaining first-direction degrees are at most two.

This covers D/E and A1,A2,A3 mixtures, whose individual indices are
at most four; their common exponent can still be twelve. The full
bounded-index12 class also permits an actual index12 point, which
is explicitly outside this last exclusion.

If P is the pole divisor of the first-symbol ratio, the general
formula is `length T_1=deg A_F-deg P`. Thus the ell=4 row could only
survive with `deg P>=2` on a normal sextic carrier or `deg P>=10`
on a normal octic, all supported at genuine local index12 points.
This is necessary pole accounting, not an exclusion of that stratum.

## 5. Global cancellation without dropping simultaneous singularities

When all local indices are less than12, the ratio is a global
section of `O_C(b-a)`. For a normal octic with a sextic mate,
this line bundle has negative degree, so the mate's first symbol
is identically zero. For a normal sextic with an octic mate, the
ratio is a section of `O_C(2)`; the accepted quadratic restriction
surjectivity gives an ambient quadric Q with that restriction.
Replacing G by G-QF makes its first symbol zero and preserves the
entire defining ideal.

Thus this whole index class can be represented with a normal
order-one carrier and a mate of generic normal order at least two.
The replacement remains nonzero; no common surface component is
introduced. This does not make the structure primitive or assume
the two carriers are simultaneously smooth. At D-type points high
jets remain relevant even when the class index is small.

The next task is compatibility of these torsion and pole budgets
with the actual higher local ideals, especially the index-three
and index-four contributions. No exclusion of the positive rows,
the mixed order-one/thick pair, or the unrestricted STCI problem
is established here. An independent review should check the
pointwise Frobenius-lattice argument before canonical promotion.


---

## 2026-10-14-generalization-index12-filtered-compatibility

# Full filtered compatibility with local Cartier indices

Date: 2026-10-14. Author: `socle_audit`, including an independent
reconstruction of the root's new Jacobian/index argument.
Status: **PROVED NEW STRUCTURAL THEOREMS AND ALL-DEGREE EXCLUSION FOR
NORMAL C0 CARRIERS WITH ACTUAL ON-CURVE LOCAL INDICES AT MOST FOUR.**
Accepted inputs are the normal-carrier torsion/index reduction in
`2026-10-14-generalization-normal-carrier-torsion.md`, the full socle
duality/budget, the splitting N_C0^* = O(-7)^2, the exclusion of integral
carriers of degree at most four, and P-010's nonzero quadratic obstruction
for every constant first direction. Those inputs were not reverified.
Only the new filtered/index compatibility and its consequences are
proved and audited here. No canonical-state file is edited.

## 1. Ordinary free layers are powers, even in the presence of torsion

Let Y be a complete-intersection thickening of a smooth integral curve C,
whose generic transverse algebra is curvilinear of length n >= 2. Put

    J = I_C O_Y,
    L_i = J^i/J^(i+1),
    T_i = torsion(L_i),
    B_i = L_i/T_i,
    B = B_1.

Purity gives J^n = 0 everywhere. Every B_i for 0 <= i < n is a line
bundle. The direct sum of the T_i is a graded ideal: the product of a
torsion section with any normal-layer section is torsion. The ordinary
associated graded algebra is generated in degree one, hence so is its
torsion-free graded quotient. Therefore multiplication surjects

    B^i -> B_i.

A surjection between line bundles is an isomorphism. This proves

    B_i = B^i,  including J^(n-1) = B^(n-1).    (1)

This concerns the ordinary J-adic filtration. A saturated BF filtration
is a different filtration and may have nonzero multiplication divisors.
There is no conflict with earlier BF defect calculations.

Write deg B = -ell and J^(n-1) = Soc(Y)(-D), with D effective. The
accepted actual socle line gives

    deg D = (n-1)ell + (2g-2) + e(4-a-b),      (2)

where e = deg C and a,b are the defining hypersurface degrees. The
ordinary Euler-characteristic budget, together with (1), yields

    2 sum_i length T_i = n deg D.              (3)

No primitive hypothesis on Y, torsion-free layer hypothesis, or global
retraction to C is used.

## 2. The Frobenius identity is pointwise

Complete at P in C and choose a lift t of its curve parameter. The
local algebra A of Y is finite free of rank n over R = k[[t]]. Indeed
normal variables are nilpotent, and Cohen--Macaulay purity makes t a
nonzerodivisor. It is a relative complete intersection, so A^vee =
Hom_R(A,R) is free rank one as an A-module.

Choose z in J whose first symbol generates B locally. Its powers
generate each B_i by (1). Thus

    A_0 = R[z]/(z^n) subset A

is a full lattice. Its induced J-filtration is strict: the least
nonzero z-power in a polynomial has nonzero image in the corresponding
free normal layer. Comparing its graded pieces with L_i gives

    length_R(A/A_0) = sum_i length_R(T_i)_P.    (4)

Choose an A-module generator lambda of A^vee. The multiplication
pairing lambda(xy) is perfect over R. Finite duality identifies the
actual socle Ann_A(J) with R via lambda: explicitly,

    Hom_A(R,A^vee) = Hom_R(R,R) = R.

If s generates the socle, lambda(s) is a unit. Write
z^(n-1) = t^(D_P) u s, u a unit. The Gram matrix on
1,z,...,z^(n-1) is anti-triangular and has determinant a unit times
lambda(z^(n-1))^n. Its valuation is n D_P. The perfect Gram determinant
on an R-basis of A is a unit; passage to a full sublattice doubles its
index in the determinant. Therefore (4) proves the stronger identity

    2 sum_i length_R(T_i)_P = n D_P.           (5)

The independent reconstruction checks both the strict filtration and
the socle identification; no trace pairing on a nonreduced algebra is
mistaken for a perfect pairing.

## 3. The local normal-index theorem

Work in the complete regular ambient ring

    T = k[[t,x,y]],  I = (x,y),
    S = T/(F),

where S is a normal surface domain and C is the smooth curve defined
by I. Suppose a mate has divisor n C on S. Let r be the actual local
Cartier index of C, so r divides n, and put k = n/r. Choose h in S with
div(h) = r C; normality makes such a rational principal representative
regular. The mate is u h^k for a unit u in S. Units do not change its
ideal, so the two relevant local complete intersections are

    W_r = S/(h),  W_n = S/(h^k).

Let A_F,P denote the vanishing order on C of the carrier's first normal
symbol after saturating its rank-one direction. In local normal
coordinates one may write

    F_1 = t^(A_F,P) u_0 y,  u_0 a unit,         (6)

with z = x generating the free first normal quotient. For r >= 2,
W_r and W_n have the same free first-normal quotient: their generic
kernel is the direction of F_1, and taking the torsion-free quotient
saturates that same rank-one direction. Thus this z works for both.

Let D_r,P and D_n,P be their actual top-power/socle defects. The exact
compatibility theorem is

    D_n,P = (k-1) A_F,P + k D_r,P.             (7)

Its proof retains the full embedded algebra, not only the tangent cone.

### 3.1 Normality gives the colon comparison

For the ideal I in S,

    (h^k : I) = h^(k-1)(h : I).               (8)

To check the nontrivial inclusion, if c I is contained in (h^k), choose
a normal parameter z whose valuation at C is one. Then val_C(c) >=
kr-1. The rational function c/h^(k-1) has C-valuation at least r-1,
and nonnegative valuation at every other height-one prime, because
h has divisor only r C. It is regular by normality. Dividing the
containment by h^(k-1) gives its membership in (h:I).

Modulo h^k, (8) gives the isomorphism of actual socle lines

    Soc(W_n) = h^(k-1) Soc(W_r).              (9)

Also

    w = z^r/h in Frac(S)

is regular: z has C-valuation one, and the divisor of z has only
nonnegative coefficients at other primes. Its restriction to C is
generically nonzero. Writing v = ord_C,P(w), one obtains from
z^(n-1) = h^(k-1) w^(k-1) z^(r-1) and (9)

    D_n,P = D_r,P + (k-1)v.                   (10)

### 3.2 The relative Jacobian is an actual socle generator

The key standard input is the formal Artinian CI Jacobian theorem:
over a field of characteristic zero, the determinant of the defining
Jacobian generates the socle. A primary formulation, valid more
generally when the characteristic does not divide the length, is
Eisenbud--Ulrich, *Duality and socle generators for residual
intersections*, [Theorem 8.5, PDF pages 50--51](https://arxiv.org/pdf/1309.2050).
This applies to nonhomogeneous formal CI equations, not just graded
ones.

Here W_r is finite free of rank r over R: its generic transverse length
is r and it is a pure one-dimensional CI. Let

    j_r = det(partial(F,h)/partial(z,y)).

Generically j_r belongs to the socle by the standard theorem; purity
therefore shows j_r I = 0 globally. Its reduction modulo t is the
Jacobian of the length-r Artinian CI fiber, and generates that fiber's
socle in characteristic zero.

The actual socle is base-change-compatible in this situation. An
A-module generator of Hom_R(A,R) identifies Hom_A(R,A) with R;
after reduction modulo t it identifies the reduced line with
Hom_(A/tA)(k,A/tA), since the augmentation dual is the socle of the
dual algebra. Consequently j_r generates the actual R-socle by
Nakayama. This is the needed global-over-R justification; being a
generic socle generator alone would not suffice.

### 3.3 Differentiation identifies the extra defect

In S the exact identity z^r = h w holds. Lift it to T, differentiate
with respect to z,y, wedge with dF, and reduce modulo (F,h). The term
h dw vanishes, and terms from the lifted multiple of F disappear.
One obtains in the actual socle of W_r

    w j_r = r z^(r-1) det(partial(F,z)/partial(z,y)).

The top power z^(r-1) is annihilated by I. Thus the last factor reduces
to its restriction on C, which is a unit times t^(A_F,P) by (6).
Since j_r generates the socle and z^(r-1) generates its top-power
subline, this proves

    ord_C,P(w) = A_F,P + D_r,P.                (11)

Combining (10) and (11) proves (7).

If r=1, then C is Cartier on the normal hypersurface and is smooth.
The hypersurface is smooth at P: a principal quotient by C is a regular
one-dimensional local ring, so the ambient surface has embedding
dimension at most two and is regular. Thus A_F,P = D_r,P = 0, and
(7) remains valid with the evident conventions.

The class index r does not bound A_F,P or D_r,P. For example index-four
D_n singularities may have large higher corrections. Formula (7)
charges those corrections rather than suppressing them.

## 4. A pointwise index bound gives a linear carrier-degree bound

For C0 let F have degree a, let the mate have degree b, and put
n = ab/4. A normal carrier makes the generic CI algebra curvilinear.
The ordinary first free layer is O(-ell), with ell <= 7. Equations
(1)--(2) give

    deg D = (n-1)ell - 4(a+b) + 14,
    deg A_F = 4a - 14 + ell,
    deg D + deg A_F = n(ell-16/a).             (12)

Let s be an upper bound on the actual local Cartier indices of C0
at points on F. Since k = n/r >= n/s, summing (7) gives

    deg D >= (n/s-1) deg A_F,
    s(ell-16/a) >= 4a-14+ell.                  (13)

For a >= 5, the right side is positive under a hypothetical mate;
therefore ell-16/a > 0. The ratio

    (4a-14+ell)/(ell-16/a)

decreases in ell because its derivative has numerator
14-4a-16/a < 0. Using ell <= 7 in (13) yields the uniform bound

    s >= (4a-7)/(7-16/a),
    4a^2-(7s+7)a+16s <= 0.                    (14)

Thus a pointwise bound on actual curve indices bounds carrier degree
linearly; it is stronger than merely bounding the least common multiple
of many indices and using a | 16R. It imposes no bound on the number of
singular points or their D_n higher-jet complexity.

For s <= 4, (14) forces integer a <= 6. Accepted low-degree exclusions
leave only a=5,6. The actual indices divide12, hence the accepted
Cartier integrality gives a | 192 and eliminates a=5. The accepted
index/torsion theorem then gives the minimal degree pair (a,b)=(6,8),
with R=12 and n=12. Equivalently one can use the accepted index12
reduction first and apply the sharper local formula below.

For a smooth rational degree-e curve with balanced normal bundle
O(2e-1)^2, put lambda = 2e-1. The same proof gives

    deg A_F = ea-2lambda+ell,
    deg D + deg A_F = n(ell-e^2/a),
    s >= (ea-lambda)/(lambda-e^2/a),           (15)

when deg A_F > 0 and the denominator is positive. These conditions are
forced by the preceding inequality for a genuinely non-Cartier carrier
point. The ratio decreases in ell when
ea+e^2/a >= 2lambda; this holds for integer e,a in the balanced rational
setting (strictly for e>=3 by AM--GM). Degenerate smooth line cases
with zero numerator and denominator are outside the non-Cartier
application. The characteristic-zero Jacobian hypothesis remains in
force.

## 5. Closing the entire actual-index-at-most-four class

Apply the accepted index12 reduction: a minimal mate yields the same
unordered pair (6,8), length12. The other defining surface is not
assumed normal. The four initially possible first-layer slopes are

    ell = 4,5,6,7,
    deg D = 2,13,24,35.

At every point with local index at most four, k = 12/r >= 3. Formula
(7) gives D_P >= 2 A_F,P. For a normal octic,

    deg D - 2 deg A_F = 9ell-78 < 0

for every ell <= 7. Hence the normal octic carrier is impossible.

For a normal sextic,

    deg D - 2 deg A_F = 9ell-62.

Effectivity forces ell=7, deg D=35, deg A_F=17, with total slack one.
Pointwise the exact slack is

    D_P - 2 A_F,P = (k-3)A_F,P + k D_r,P.      (16)

An index-two point has k=6 and A_F,P >= 1, costing at least three; it
is impossible. An index-three point has k=4 and costs
A_F,P+4D_r,P. An index-four point has k=3 and costs 3D_r,P.
Since R=12 requires an index-three and an index-four contribution,
the total slack one forces

    D_r,P = 0 at every index-three/four point,
    sum_(r=3) A_F,P = 1,
    no index-two points.                      (17)

In particular there is exactly one index-three point with first-symbol
vanishing order one. Simultaneous index-four points are all retained;
their total first-symbol vanishing order is sixteen. No classification
or independent bound on their higher local jets has been used.

## 6. Primitive symbolic triple contradiction

For each index-three/four point, (5) applied to W_r and (17) give zero
ordinary layer torsion. The R[z]/(z^r) lattice is therefore the entire
algebra:

    W_r = R[z]/(z^r).

For j <= r, the image of the symbolic ideal I_(C/X)^(j) is (z^j) in
this algebra. To check this without assuming a primitive hypothesis,
the two ideals agree after inverting t by their C-valuations. The
quotient R[z]/(z^j) is R-torsion-free, so the ordinary ideal (z^j) is
already saturated and equality descends. Consequently the symbolic
triple is locally R[z]/(z^3) at every index-three/four point.

At all remaining points the curve has index one, and the carrier is
smooth by the argument in Section 3; its symbolic triple is likewise
primitive. Thus the global symbolic triple defined by O_X(-3C) is an
embedded primitive triple everywhere along C0. This is a conclusion
from the full filtered compatibility, not an imposed primitive-pair
assumption.

Its free first conormal quotient is the same saturated carrier
direction as B_1 of the length-twelve thickening, namely O(-7).
The map O(-7)^2 -> O(-7) has constant coefficients on P1, so its first
initial relation is a fixed linear form m. Primitivity makes the next
relation space exactly mV. The accepted P-010 quadratic obstruction
for this constant embedded primitive triple is nonzero in every
direction. This is a contradiction.

Therefore:

**No normal integral carrier of C0 in characteristic zero can admit a
mate if every actual local Cartier index of C0 at points of that carrier
is at most four. This is an all-carrier-degree and all-mate-degree
exclusion.**

It includes arbitrary simultaneous D/E rational-double-point
singularities and A1,A2,A3 mixtures along C0, using the accepted class
index bounds. Singularities away from C0 are irrelevant. No normality
of the other defining hypersurface, primitive initial presentation, or
D_n complexity bound is required.

## 7. What survives

The complete class with indices dividing12 still permits actual
index-six or index-twelve points. Those points have k=2 or k=1 in
the length-twelve formula and are not closed by Section 5. In
particular an index-twelve point can support a pole in the first-symbol
ratio and evade the stronger first-layer comparison. The local theorem
now gives the exact simultaneous system

    D_P = (12/r_P-1)A_F,P + (12/r_P)D_(r_P),P,
    2 sum_i length(T_i)_P = 12D_P,
    sum_P D_P = 11ell-42,
    sum_P A_F,P = 4a-14+ell,
    ell in {4,5,6,7},
    lcm_P r_P = 12.

These equations retain all higher primitive-index socle defects and
simultaneous support points. They do not claim that any remaining
system lifts to a global pair or that C0 is non-STCI. The unrestricted
normal, nonnormal, and entirely thick branches remain open.

## 8. Audit provenance

The ordinary free-layer theorem was first proposed by `socle_audit`
and independently reconstructed by the root and the
`index12_multiplication` worker. The root then proposed the pointwise
Frobenius identity, the local Jacobian/index formula, and the resulting
symbolic-triple contradiction. This note independently reconstructs
all of those new steps, explicitly checking the socle's base change,
the normal-domain colon argument, the shared free normal generator,
and the saturation identifying symbolic triples.

The primary Jacobian theorem was inspected for this new bridge; no
previously accepted repository calculation was rerun. Parallel agent
agreement is not the proof: Sections 1--6 contain the actual arguments.
No memory file was used for this continuation.

