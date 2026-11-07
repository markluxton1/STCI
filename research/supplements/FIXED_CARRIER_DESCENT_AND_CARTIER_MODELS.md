# Fixed-carrier descent and Cartier singleton models

This is the proof home for [R-0003](../results/fixed_carrier_conductor_criterion.md) and the Cartier model classification [R-0002](../results/cartier_singleton_lift.md). It incorporates the independent source audits' corrected scopes: arbitrary characteristic for the fixed-carrier lattice theorem; characteristic zero and an actual mate for the classification; full inverse support including isolated points; and two distinct torsion orders for producing and descending a section. The unrestricted characteristic-zero question for the fixed quartic remains open.

The supporting local membership, unit-power, single-field/split-phase, and purity lemmas are proved in [full conductor algebra](CONDUCTOR_DESCENT_ALGEBRA.md). In particular, for an integral Cohen–Macaulay surface X and finite normalization nu, the sheaf nu_*O_S/O_X is pure of dimension one: at a closed point the source and normalization modules have depth at least two, so the depth lemma gives quotient depth at least one. This justifies generic-to-global descent below without discarding nilpotent conductor data or assuming the conductor is Cartier.

## 4. An exact fixed-carrier criterion, including thick support

This section does **not** need characteristic zero. Work over any
algebraically closed field. Let `X` be an integral Cohen--Macaulay
projective surface with finite normalization `nu:S->X`, let `L` be an
ample line bundle on `X`, and put `H=nu^*L`. Let `C` be an integral
curve on `X`. Write the full reduced inverse image as `W`.

If `W` contains an isolated point not lying on its curve components,
there is no section cutting `C` set-theoretically: the pullback of
such a section is an effective Cartier divisor on the normal surface
`S`, whose support has pure codimension one. Hence suppose

```
W = Gamma_1 union ... union Gamma_s
```

has no isolated points. Let `I` be the **full** conductor ideal.

Define the Cartier relation lattice

```
Lambda = ker[ Z^(s+1) -> Cl(S) ],
(n_1,...,n_s,d) -> sum n_j[Gamma_j] - d[H].
```

A vector in `Lambda` gives a rational section `Q_v` of `O_S(dH)`
with divisor `sum n_j Gamma_j`. It is unique up to `k^*`, since `S`
is integral, normal and projective. If all `n_j>=0`, normality makes
the rational section regular. A nonzero such effective divisor
forces `d>0`, by intersecting with the ample divisor `H`.

For each generic conductor point `eta` whose curve is different from
`C`, set

```
A_eta = O_X,eta/I_eta,
B_eta = (nu_*O_S)_eta/I_eta,
G_eta = B_eta^*/A_eta^*.
```

These are the actual Artinian conductor rings. The rational section
`Q_v`, in a frame pulled back from `X`, is a unit at every branch
above this `eta`, since its divisor is supported on `W`. Its class
in `G_eta` is independent of the frame and of its global scalar.
Multiplication of sections gives a homomorphism

```
phi: Lambda -> G = product_{eta off C} G_eta.
```

Define the descent lattice

```
Lambda_desc = ker[ Lambda -> G/Tor(G) ].
```

**the fixed-carrier theorem.** A positive power of a section of a positive tensor power
of `L` cuts out `C` set-theoretically if and only if

```
Lambda_desc contains v=(n,d) with every n_j>0.
```

Equivalently, `C` has a mate on this carrier precisely when the
normalization Cartier relation lattice has a fully positive vector
whose off-`C` conductor unit class is torsion.

Proof of necessity. A descending section cutting `C` has a pullback
divisor with full support `W`; its coefficient vector lies in
`Lambda`, is positive on every `Gamma_j`, and has zero conductor
class. Therefore it lies in `Lambda_desc`.

Proof of sufficiency. Let `v` be such a vector. At every generic
conductor curve off `C`, some common positive power of `Q_v` lies
in `A_eta`, because `phi(v)` is torsion. At the generic point of `C`,
if it is itself a conductor curve, `Q_v` vanishes on **all** branches
above `C`. In the semilocal normal one-dimensional normalization ring, conductor membership can be checked in its DVR localizations at those branches. A sufficiently large power therefore belongs to the actual conductor ideal. Such a power
automatically belongs to `O_X,eta`. Take a common multiple large
enough for both requirements. The [purity/depth argument](CONDUCTOR_DESCENT_ALGEBRA.md#4-purity-converts-generic-full-membership-into-global-descent) gives global descent to `L^(Nd)`. Its pullback still has full
support `W`; surjectivity of `nu` gives zero support exactly `C`.

If `X` is a degree-`a` hypersurface in `P^3` and `L=O_X(1)`, every
descending section of `O_X(b)` lifts to an ambient degree-`b` form,
since `H^1(P^3,O(b-a))=0`. Thus this criterion is exactly a criterion
for an ambient STCI mate **on the chosen carrier**.

The theorem retains both kinds of conductor behavior. On components
lying over `C`, vanishing enters the conductor after a large power.
On components away from `C`, unit descent is precisely a torsion
condition. For characteristic zero, the full-ring unit-power theorem separates the latter
condition into residual finite phases and the vanishing of the
nilpotent logarithmic defect. No local class at a closed point is
silently discarded: the original section already exists everywhere
on `S`, and Cohen--Macaulayness forces generic actual membership to
extend everywhere on `X`.

## 5. Finite lattice reduction, rather than separate mate degrees

The group `Lambda` is a subgroup of a finite-rank free abelian group,
so it is a finite-rank lattice. Since `G/Tor(G)` is torsion-free,
`Lambda_desc` is a **saturated sublattice of Lambda**. Saturation here
is relative to `Lambda`, not necessarily to the ambient
`Z^(s+1)`; torsion divisor classes can make the latter distinction
substantive.

The semigroup

```
M = Lambda_desc intersect N^(s+1)
```

has a finite Hilbert basis. To see finiteness directly, its cone is
the intersection of a rational linear subspace with the nonnegative
orthant. Triangulate that rational polyhedral cone into finitely many
cones with integral ray generators. In each cone, remove integer
multiples of those generators from a lattice point. What remains is
a lattice point in a bounded fundamental parallelepiped, of which
there are finitely many. These points and the ray generators generate
`M`. Passing to a minimal generating set gives a finite Hilbert basis.

Let its nonzero members be `h_1,...,h_q`. Then the fixed-carrier theorem has the
finite equivalent test:

```
for each Gamma_j, some h_i has positive j-th coefficient.
```

Indeed a fully positive vector decomposes into Hilbert basis members,
so the supports of those members cover all `Gamma_j`. Conversely the
sum of a support-covering subset of the basis is fully positive.

For **existence alone**, a full Hilbert basis is unnecessary. The
rational cone
`(Lambda_desc tensor R) intersect R_>=0^(s+1)` has finitely many
extreme rays. Choose an integral lattice vector on each ray. A
full-support vector exists exactly when the union of their curve
supports covers all branches; a support-covering sum constructs it.
Thus computation of the rational cone and its extreme rays can be
the first finite target, reserving a Hilbert basis for finer degree
or multiplicity questions.

**Do not claim that each Hilbert basis member is itself a mate.** A
member can omit some branches above `C`; at the generic point of `C`
it may then have a mixture of zero and nonzero branch residues, which
no power can descend. The support-covering sum removes that problem.

There is also a fixed-data power bound. The torsion group
`phi(Lambda_desc)` is finitely generated, hence finite. Denote its
exponent by `E_{X,C,L}`. For every normalization branch above `C`
on which the conductor has positive valuation, write

```
c_j = ord_{Gamma_j}(I O_S),
c_max = max(1, all these c_j).
```

Any fully positive vector has `n_j>=1`, so every power exponent
divisible by `E_{X,C,L}` and at least `c_max` descends. In particular
the single common choice

```
N_{X,C,L} = E_{X,C,L} ceil(c_max/E_{X,C,L})
```

works for every fully supported vector in `Lambda_desc`. For a
particular vector one can improve `c_max` to
`max(1, ceil(c_j/n_j))`.

If `v_0` is a support-covering sum of Hilbert basis members, this
constructs a mate of degree at most `N_{X,C,L} d(v_0)` in the
hypersurface case. This bound depends on the fixed carrier, curve
and polarization. Split phases can have unbounded orders as these
data vary. Moreover **abstract finite generation is not an effective
algorithm**: computing `Cl(S)`, the relation lattice, and the integer
relations among the conductor-unit images remains substantial work.

The conceptual gain is exact: all mate degrees on a fixed carrier
are governed by one lattice and one homomorphism, rather than by a
new calculation for each degree. Non-torsion conductor classes cut
the lattice; finite conductor phases determine only the final power.

## 6. Primitive Cartier rays and a carrier-degree-independent bound

Let `v=(n_1,...,n_s,d)` be a primitive positive integer vector in the
ambient lattice, so `gcd(n_1,...,n_s,d)=1`. Put

```
Delta_v = sum n_j[Gamma_j] - d[H] in Cl(S).
```

The ray generated by `v` contains a Cartier relation if and only if
`Delta_v` is torsion. If its order is `t`, then `t v` is the first
Cartier relation on that ray. The associated primitive Cartier
section has degree `t d`. A mate along this ray exists if and only if
`phi(t v)` is torsion; its actual descending power is then governed
by the full conductor and lattice tests.

This separates two different torsion orders: the class-group order
needed to **produce** an upstairs section, and the conductor-unit
order needed to **descend** it. An existing mate does not justify
dividing its divisor by the gcd without keeping the first order.

There is a useful uniform upstairs consequence when there is only
one curve `Gamma` in `W`. Write

```
a = H^2,  c = H.Gamma,  g = gcd(a,c).
```

Any mate has divisor `n Gamma` linearly equivalent to `d H`, so
intersection with `H` forces `n c=d a`. The primitive ray is therefore

```
(n_0,d_0) = (a/g,c/g).
```

If `Cl(S)` is torsion-free, existence of any mate implies

```
(a/g)[Gamma] = (c/g)[H]
```

already. It supplies a base section `Q` of degree

```
d_0 = c/g <= c,
```

**independent of the carrier degree**. The full mate problem along
this unique ray is then one conductor torsion problem for `Q`.

For a hypersurface carrier generically regular along a degree-`e`
curve `C`, the unique branch maps birationally to `C`, so `c=e` and
`a=deg(X)`. Thus, assuming the full inverse image has only this branch
and `Cl(S)` is torsion-free, an upstairs base section has degree

```
e/gcd(deg(X),e) <= e.
```

A smooth rational normalization has torsion-free Picard group and
`Cl(S)=Pic(S)`, so belongs to this scope. For `C0` of degree four,
the possible base degrees on **all** such carriers are `1,2,4`.
This does not bound the carrier degree or the descending mate degree,
and it does not cover multiple normalization branches or torsion
class groups. It nevertheless replaces separate upstairs mate-degree
searches across an entire normalization class by finitely many base
degrees.

There is an **exact minimum-degree formula** in the same one-branch
situation when `X` is generically regular along `C`. Let `t` be the
order of the primitive class

```
Delta_0 = (a/g)[Gamma] - (c/g)[H],
```

with `t=infinity` if it is not torsion. If `t` is finite, let `Q`
be the section associated to `t(a/g,c/g)` and put

```
E = order(phi(t(a/g,c/g))),
```

again allowing infinity. There is no generic conductor component
equal to `C`, so there is no additional vanishing threshold there.
A mate exists if and only if **both `t` and `E` are finite**. If so,
the possible mate degrees on this carrier are exactly

```
k t E (c/g),   k=1,2,3,... .
```

To prove exactness, every relation lies on the intersection-determined
ray. The class order forces its ray coefficient to be divisible by
`t`; its upstairs section is then a scalar multiple of a power of
`Q`. Actual conductor descent forces that power to be divisible by
`E`, and sufficiency follows from generic-to-global descent.
For torsion-free `Cl(S)`, `t=1`; for a hypersurface and `c=deg(C)`,
the minimum degree is exactly

```
E deg(C)/gcd(deg(X),deg(C)).
```

This identifies the full sequence of mate degrees with two torsion
orders rather than with a sequence of independent degree problems.

## 7. APic interface and the thick-carrier boundary

The conductor unit quotient used here is the generic-point version
of the standard quotient sheaf
`nu_*O_S^*/O_X^*`. Its identification with the quotient of the full
conductor unit sheaves is precisely the interface developed in
Hartshorne--Polini, Proposition 2.6; their Sections 3--4 relate these
data to Picard and almost-Picard groups. Their Proposition 7.1
expresses the chosen-carrier STCI condition by a relation between
`C` and the hyperplane class in APic when `C` meets the singular locus
only finitely. See the primary source
[*Divisors class groups of singular surfaces*](https://arxiv.org/html/1301.3222).

An almost-Cartier divisor is locally principal outside codimension
two. When `C` lies in the codimension-one singular locus, its reduced
ideal need not be almost Cartier. Writing `[C] in APic(X)` in that
case requires a separate proof. The normalization relation lattice
and full conductor-unit map in the fixed-carrier theorem make no such assumption.
They retain the multiplicities of all branches and apply directly
to the section of a hypothetical Cartier mate.

Accordingly the class-group ray and conductor torsion tests are a
precise replacement for an unjustified single reduced-curve APic
class in the entirely thick situation. Computing them remains the
central task.

## 8. Positive characteristic comparison

The local nilpotent distinction changes in characteristic `p>0`.
If `N_B^(p^h)=0` and the residual class of a unit `u` has order `e`,
choose `a in A^*` lifting its common residual `e`-th power. Then

```
(u^e/a)^(p^h)=1,
u^(e p^h)=a^(p^h) in A.
```

Hence in positive characteristic a given unit eventually descends
**if and only if its residual class is torsion**. Nilpotents can add
`p`-powers but cannot supply the characteristic-zero infinite-order
logarithmic obstruction. The lattice criterion of the fixed-carrier theorem still
holds; this observation simplifies its local unit map. It does not
make nonconstant residual ratios automatically torsion over function
fields, and it does not prove the universal STCI statement.


## Cartier singleton models: the complete proof

## 1. Exact theorem

Work over an algebraically closed field of characteristic zero. Let
`C subset P3` be a smooth rational curve of degree `d`, and let
`X subset P3` be an integral degree-`a` hypersurface with a mate for
`C`. Let `nu:S->X` be its finite normalization, `H=nu*O_X(1)`.
Assume the full reduced inverse image is one curve `c`, that
`nu|c:c->C` is an isomorphism, and that **c is Cartier on S**.

Then the complete system `|c|` identifies `S` with a normal surface
of minimal degree. With `n=c^2=d^2/a`, the possibilities are:

| Pair `(S,c)` | Integral hyperplane pullback | Carrier degree |
|---|---|---|
| `P2`, a line | `H=d h` | `a=d^2` |
| `P2`, a smooth conic; `d` even | `H=(d/2)h` | `a=d^2/4` |
| Smooth rational normal scroll of degree `n>=2`, hyperplane section; `n|d` | `H=(d/n)c` | `a=d^2/n` |
| Rational-normal cone of degree `n>=2`, smooth Cartier hyperplane section; `n|d` | `H=(d/n)c` | `a=d^2/n` |

The conclusion is about the normalization and its polarization. It
does not assert that every four-coordinate projection of these models
has a mate. Full support and entire conductor descent remain required.

## 2. Why Cartierness gives enough smoothness

At a point `P in c`, take a local defining nonzerodivisor `f` in the
normal surface ring `R=O_S,P`. The quotient `R/(f)=O_c,P` is regular
of dimension one because `c` is smooth. A generator of its maximal
ideal, lifted to `R`, together with `f` generates the maximal ideal
of `R` by Nakayama. Thus `embdim(R)<=2=dim(R)`, and `R` is regular.
Consequently `S` is smooth along all of `c`; its finitely many possible
singularities lie away from `c`.

The mate gives `m c~bH` with `md=ab`. Since `c` is Cartier,
`O(c)` is ample: a positive power is the ample `O(bH)`. Its square
is the positive integer `n=d^2/a`.

Resolve the isolated singularities by `sigma:M->S`, an isomorphism
near `c`. The strict transform `c_M` equals the Cartier pullback,
is smooth rational, and has square `n`. The pullback `L=sigma*H`
is nef and big, and `m c_M~bL`. Adjunction gives

    K_M.c_M=-n-2,    K_M.L=(m/b)(-n-2)<0.

Hence no positive multiple of `K_M` can be effective. The same
characteristic-zero surface-classification input as in the accepted
carrier work makes `M` rational or birationally ruled over a
positive-genus curve. In the latter case the ruling extends to `M`,
and the rational `c_M` is a fiber component, so has square at most
zero. This contradicts `n>0`. Thus `M` is rational.

Normality gives `sigma*O_M=O_S`. The Leray edge map injects
`H1(S,O_S)` into `H1(M,O_M)=0`, so `H1(S,O_S)=0`. No rational-
singularity hypothesis was assumed here; the eventual minimal-degree
classification will impose the actual singularity type.

## 3. The complete linear system and cone polarization

The sequence

    0 -> O_S -> O_S(c) -> O_P1(n) -> 0

gives `h0(O_S(c))=n+2` and surjective restriction. The canonical
section generates away from `c`, and restriction generates on `c`.
Therefore `|c|` is basepointfree. Since `c` is ample, its morphism
to `P^(n+1)` is finite. The nondegenerate image `Y` has

    n=deg(phi) deg(Y),    deg(Y)>=n.

Thus it is a finite birational map to a minimal-degree surface.
The [Del Pezzo--Bertini classification](https://arxiv.org/html/math/0404517v5)
gives normal `Y`, so finite birationality makes `S~Y`. The new
singular possibility is the cone over a rational normal curve; the
plane and Veronese surface remain smooth.

For the smooth entries, numerical and linear equivalence agree on the resulting smooth rational surface. Thus H=(d/n)c in Pic(S) tensor Q. A smooth scroll has c=E+t f with E²=−e, t>e≥0 and n=2t−e. Its E-coefficient is one, so integrality of H forces n|d. On P2 a line gives H=d h, while a smooth conic gives H=(d/2)h and requires d even. For a cone of degree `n`, its minimal resolution
is `F_n`, with exceptional section `E^2=-n` and ruling `f`. The
pullback of the Cartier hyperplane is

    L_c=E+n f.

Pullback injects `Pic(S)` into `Pic(F_n)`: pushing a trivial pulled-
back line bundle down and using `sigma*O_M=O_S` proves injectivity.
Any pulled-back Cartier line bundle has zero degree on the contracted
`E`, so its class `xE+yf` satisfies `y=nx`. It is therefore an
integer multiple of `L_c`. Since `c` itself is Cartier, this proves
`Pic(S)=Z[c]` and `H=(d/n)c` with `n|d`.

For `n=1` the cone is simply `P2` and belongs to the plane entry.
No additional singular minimal-degree surface is missing in dimension
two. The theorem is now proved with every displayed hypothesis retained.

## 4. Fixed C0 and a new non-Cartier boundary

For the literal degree-four `C0`, the accepted all-quartic theorem
removes the `a=4` entries. Every remaining carrier under the theorem's
support and degree-one assumptions has one of exactly three pairs:

    a=8,  S=P1 x P1, c=(1,1), H=(2,2);
    a=8,  S=quadric cone, c=Cartier conic, H=2c;
    a=16, S=P2, c=line, H=4h.

This classifies the entire **Cartier-lift lane**, including singular
normalizations and unibranch thick carriers satisfying the explicit
support assumptions. All have a primitive degree-one normalized
section `Q`, with divisor `2c` or `4c`; all normalized mates are
scalar powers of it.

In particular, every generically regular carrier of fixed C0 whose
degree is neither 8 nor 16 must have a non-Cartier point of its lift
on the normalization if it admits a mate. This is stronger than the
smooth-normalization statement and applies to all carrier degrees.
It does not classify the non-Cartier singularities or bound their
indices. For fixed C0 the index condition remains
`a divides 16 t` for any Cartier multiple `tc`.

Normal hypersurface carriers are even more restricted in this lane.
If `X=S` were a normal carrier satisfying the theorem, its minimal-
degree normalization would have `H^1(O_X)=0` and `p_g(X)=0`, whereas
a degree-8 or degree-16 hypersurface has
`p_g=(a-1)(a-2)(a-3)/6>0`. Equivalently, its canonical class
`(a-4)H` has positive degree on `c`, contradicting the smooth-locus
adjunction value `-n-2`. Thus a normal carrier of fixed C0 with a
mate cannot have Cartier lift at any degree; its lift must meet a
genuine non-Cartier singularity. This is conditional on the fixed-C0
premises and the actual mate, not an all-normal-carrier exclusion.

The missing global possibilities remain non-Cartier lifts, several
inverse-image primes, or finite inverse curves of degree greater than
one. The three projection targets still require full conductor descent.



## Constructive use of the descent lattice

A fully positive relation can be formed by multiplying sections from different nonnegative divisor directions. In characteristic zero, if their reduced conductor phases are torsion and their logarithmic defects cancel on every off-C conductor component, the product has torsion full-conductor class and the fixed-carrier theorem supplies a descending power. For example in `K[epsilon]/(epsilon^2)` modulo K, neither `1+epsilon` nor `1-epsilon` has any positive descending power, but their product is one. This is actual cancellation in the unit quotient, not repair by taking a larger power.

The global sections and their effective divisors must exist on the same normalization and in compatible actual twists. On a single divisor ray, sections of the same line bundle with the same divisor differ by a global scalar on normal integral projective S, so their defects cannot be adjusted independently. Several inverse-branch multiplicity directions provide possible freedom; no such compatible full-support construction for the fixed quartic has been supplied. This construction interface is stronger than a one-ray search but remains a conditional method.

## Characteristic range

The fixed-carrier relation-cone theorem, purity/depth argument, support-covering criterion and primitive-ray arithmetic use no characteristic-zero hypothesis. Finite nilpotent unit defects become removable by a sufficiently large p-power in characteristic p; the reduced phase must still be torsion. The minimal-degree classification above is the characteristic-zero theorem: its rationality step uses surface classification in that range, so the proof has not established the same complete list in positive characteristic. This restriction is substantive for the fixed quartic, which has a [quartic-carrier STCI in every positive characteristic](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier).

## Canonical compression on a minimum actual carrier

This reduction applies beyond any fixed degree pair.  Work in characteristic
zero and define

\[
 \alpha(C)=\min\{\deg X:\ X\subset\mathbf P^3\text{ is integral and some }
 Y\text{ satisfies }|X\cap Y|=C\}.
\]

If \(C\) is an STCI, the set is nonempty.  Indeed, after factoring either
defining equation, every irreducible factor meets the other hypersurface in a
curve; that curve is contained in the irreducible support \(C\), and hence has
support exactly \(C\).  This factor lemma is why minimality must be taken
among carriers that actually occur in a defining pair, not among all surfaces
containing \(C\).  The unique smooth quadric is an immediate counterexample
to the latter, incorrect formulation.

Let \(X\) attain \(\alpha(C)=a\), suppose \(X\) is generically smooth along
the rational quartic \(C\), and let a degree-\(b\) surface \(Y\) be a mate.
Write \(H=\mathcal O_X(1)\).  At the generic point of \(C\), the Cartier
divisor \(Y|_X\) has a positive multiplicity \(r\), so

\[
 r[C]=b[H]\quad\text{in }\operatorname{APic}X,
 \qquad 4r=ab.
\]

At each of the finitely many points
\(p\in C\cap\operatorname{Sing}X\), let \(e_p\) be the order of the local
almost-Cartier class \([C]_p\), and put \(e=\operatorname{lcm}_p(e_p)\), with
the empty lcm equal to one.  The displayed relation shows \(e_p\mid r\).
Hartshorne--Polini's local-to-global sequence for almost-Cartier divisors then
shows that \(eC\) is Cartier.  Write \(r=qe\).  In \(\operatorname{Pic}X\),

\[
 q[eC]=b[H].
\]

Thus the class of \(eC\) is torsion modulo \(\mathbf ZH\).  In characteristic
zero, Hartshorne--Polini Lemma 7.6 says that
\(\operatorname{Pic}X/\mathbf ZH\) is torsion-free.  Consequently

\[
 eC\sim nH,
 \qquad n=\frac{4e}{a}\in\mathbf Z_{>0},
 \qquad b=qn.
\]

The canonical section of \(\mathcal O_X(eC)\simeq\mathcal O_X(n)\) lifts to
an ambient degree-\(n\) form, since

\[
 H^1(\mathbf P^3,\mathcal O_{\mathbf P^3}(n-a))=0.
\]

It cuts out the Cartier divisor \(eC\) on \(X\).  If \(n<a\), factor this
lift.  No factor is \(X\), and the factor lemma makes every irreducible factor
another integral carrier occurring in a defining pair, of degree below
\(a\).  This contradicts the definition of \(\alpha(C)\).  Therefore

\[
 \boxed{a\mid4e,\qquad n=4e/a\ge a,
 \qquad e\ge a^2/4.}
\]

The exact compression relation is \(n=be/r\).  If \(b\) was already minimal
among mates for this fixed \(X\), then necessarily \(e=r\) and \(n=b\).
Away from the finite singular set of \(X\), the compressed multiple structure
is locally \((u,v^e)\), hence primitive there and quasi-primitive globally.

For a minimal degree-six carrier that is generically smooth along \(C\), this
forces

\[
 3\mid e,\qquad e\ge9,\qquad
 (a,n)=(6,2e/3).
\]

The first canonical possibility is therefore \(e=9\) and a \((6,6)\) pair.
Local Cartier indices \(e=3\) or \(6\) would compress to a quadric or quartic
carrier and cannot represent a genuinely sextic-minimal phenomenon.


The mechanism does not use rationality or genus: for a smooth integral curve of degree d in P3 under the same characteristic-zero, actual-minimum-carrier and generic-regularity hypotheses, the proof replaces 4 by d and gives `a|de`, `n=de/a>=a`, and `e>=a²/d`. This is a bounded extension of the compression statement, not a bound on a without control of actual local indices. It does not apply to a carrier generically singular along C, where the reduced curve need not define the assumed APic class. The characteristic-zero Picard torsion-freeness input has not been extended here to unrestricted characteristic p.

## Singleton rays without a Cartier lift: exact index conditions

Let `C` be a smooth integral curve of degree `d` and genus `g` in `P3`.
Let `X` be an integral degree-`a` hypersurface containing `C`, with finite
normalization `nu:S->X`, and put `H=nu*O_X(1)`; `H` is ample and
`H^2=a`. Assume

    (nu^{-1}(C))_red=c,  and  nu|c:c -> C is an isomorphism.       (2.1)

This is an explicit support and degree-one hypothesis. If `X` is
generically regular along `C` and has a mate, the full-support theorem implies (2.1): there is one dominating prime because normalization
is an isomorphism at the generic point, isolated inverse-image points
are prohibited by the mate, and a finite birational map to the normal
curve `C` is an isomorphism. Some nonregular unibranch carriers also
satisfy (2.1).

If a mate of degree `b` exists, its pullback has divisor `m c`, with

    m d=a b,   m c~b H,   c_num=(d/a)H,   c_num^2=d^2/a.          (2.2)

Here `c` is Q-Cartier because an actual positive multiple is Cartier;
the intersection numbers are therefore defined without any assumption
on the normalization singularity type.

Set `h=gcd(a,d)`, `u=a/h`, `v=d/h`, and

    D=u c-v H in Cl(S).                                        (2.3)

Every normalized mate has `m=u k,b=v k`. Its existence therefore forces
`D` to be torsion. Conversely, if `k D=0`, linear equivalence gives a
section of `O_S(v k H)` whose divisor is exactly `u k c`. This supplies
the required positive Cartier support upstairs. It supplies an ambient
mate exactly when this section descends through the full conductor.

For a normal carrier `X=S`, descent is automatic, so (under (2.1)) the
criterion `D is torsion` is necessary and sufficient. It is also necessary
and sufficient if all normalization defect is supported on `C`, by the
accepted [asymptotic conductor theorem](NORMALIZATION_SECTION_AND_MODULE_DESCENT.md).
On a general nonnormal carrier, torsion upstairs leaves a real additional
descent obstruction. This exact distinction survives arbitrary degrees.

If `t c` is Cartier, restriction of its line bundle to the smooth `c`
gives the stronger elementary index condition

    a divides t d^2.                                          (2.4)

Indeed its restriction has integer degree `t c_num^2=t d^2/a`.
Using only the Cartier square would give the weaker condition
`a divides t^2 d^2`. If `z K_S` is Cartier, and `pi` is the sectional
genus of `(S,H)`, intersection with `c` similarly gives

    a divides z d(2 pi-a-2).                                  (2.5)

The sectional genus here is that of a general hyperplane pullback,
chosen to avoid the finitely many singular points of the normal surface.
Adjunction gives `K_S.H=2pi-a-2`; this numerical identity is defined
even if `K_S` itself is not Q-Cartier, by intersection with the Cartier
hyperplane divisor. Condition (2.5) is used only when the stated global
Cartier canonical multiple exists.


## Normal carriers and the entire ADE correction lattice

On a normal hypersurface, the exact criterion is torsion of the primitive ray class.
The canonical index filter imposes no new restriction there:
`K_X=(a-4)H`, so `K_X.c=d(a-4)` is already integral. If a mate exists,
the curve's Cartier index is at least `a/gcd(a,d^2)` by the Cartier-index condition.
This lower bound grows with `a`; it is not an upper degree bound.

For a rational singleton lift on a normal carrier whose singularities
along `c` are ADE, let `sigma:M->S` be a resolution crepant over the ADE points on c and arbitrary elsewhere. The exceptional and discrepancy curves over points off c are disjoint from the strict transform c#. Write the Mumford pullback `c_num=c# +Z`. The smooth strict transform
is rational and adjunction gives the uniform exact correction equation

    -Z^2=2+d(a-4)+d^2/a.                                    (5.1)

Indeed `c#^2=c_num^2+Z^2`, and `K_M.c#=K_S.c=d(a-4)`.
This is a necessary equation in the entire exceptional lattice.
It organizes every carrier degree by a local correction budget. The
exceptional lattice can itself grow with the carrier and is not
bounded by the accepted quartic proof. Without a new global bound or
geometric realization theorem, (5.1) does not exclude all `a`.
For noncrepant resolutions the discrepancy intersection must also
be retained; replacing it by zero would be invalid.

## What choosing a minimum carrier does not supply

For an actual STCI pair with no common surface component, each
irreducible factor of either form is itself a carrier with the other
form as mate; this is the accepted positive-degree factor argument.
It is therefore legitimate to select an integral carrier of minimum
degree among all carriers that admit a mate for `C`.

This choice supplies neither generic regularity along `C` nor smooth
normalization nor the full singleton isomorphic-lift condition. The fact that
there are smooth general surfaces containing `C` in sufficiently
large degree also supplies no mate on such a surface. Linear
combinations `G+F T` preserve a given pair when the degrees permit,
but can stay singular along `C` when both generators have generic
normal order at least two. Thus there is no presently justified
degree-lowering or smooth-normalization lemma for a minimum carrier.

The theorem in the Cartier-model theorem consequently reduces every smooth-normalization,
singleton degree-one rational lane at once, including thick carriers
when they satisfy those stated hypotheses. It leaves singular
normalizations, several inverse-image primes, and finite lifts of
degree greater than one as distinct global tasks. The accepted
quartic and scoped quintic exclusions do not remove those tasks.


For the fixed quartic, the surviving smooth models have complete section dimensions h0(H)=9 and15 respectively, and sectional genera1 and3. Adjunction gives `2g−2=d(d+2pi−a−2)/a`, so with d=4,g=0 one has `pi=(a−4)/4`. These are necessary normalization/polarization data, not projections or mate constructions. The cone has its own Cartier model as proved above.

## Conditional low-field-degree consequences

In the smooth quadric and plane Cartier models, the primitive section Q has degree one with divisor2c or4c. Assume Q is a unit at every generic conductor point and every reduced upstairs conductor algebra is a single field. If all extension degrees are at most two, any mate implies Q² descends, hence an ambient quadric mate, excluded for the fixed quartic in characteristic zero. A degree bound three gives sufficient exponent6; degree bound four gives sufficient exponent12. If the actual degree list uses only1,2,4, exponent4 suffices, and the quartic-carrier exclusion eliminates the carrier. These are conditional coverage results; neither integral double-cover conductors nor absence of split phases is automatic for every projection.

## Consolidation review

Independent consolidation review reconstructed the fixed-carrier sufficiency, full-support cone test, primitive torsion orders, minimal-degree and cone-polarization proof, minimum-actual-carrier compression and its degree-d extension, singleton index/canonical divisibilities, on-curve ADE correction, low-field consequences, and stated characteristic boundaries. It accepted these at their displayed hypotheses after correcting semilocal DVR wording and localizing crepancy to the ADE points along c. This preserves the mathematical statements and review scope.
