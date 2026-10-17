# Conductor torsion, primitive Cartier rays, and a finite carrier criterion

Started 2026-10-13; completed in the 2026-10-14 continuation.
Author: `conductor_general`, with independent new-proof audits by
`split_unit_audit` and `cartier_lattice_audit`.

Status: **NEW STRUCTURAL THEOREMS WITH WRITTEN PROOFS; independent audits
recorded below.** Previously accepted repository claims were used as
context and were not recomputed. This note audits and substantially
extends the new
[power-compression proposal](2026-10-13-evening-general-conductor-power-compression.md).
No novelty claim is made. These results give a degree-independent
framework on a **fixed carrier**; they do not classify all carriers or
resolve the global projective-curve STCI question.

## 1. Exact characteristic-zero local theorem

Let `A -> B` be a finite injective unital map of commutative Artinian
rings containing `Q`. Assume `A` is local, but allow `B` to be semilocal.
Write

```
N_A = nil(A),  N_B = nil(B),  K = A/N_A,
E = B/N_B = product_i E_i,
G = B^*/A^*,  R = E^*/K^*.
```

Here `K^*` maps diagonally to the finite field extensions `E_i`.
Since the map is injective, `N_A = A intersect N_B`.

**Theorem 1.** Reduction gives an exact sequence of abelian groups

```
0 -> N_B/N_A -> G -> R -> 0,
```

where the left-hand map is induced by the finite exponential series.
The kernel is a uniquely divisible `Q`-vector group. In particular,
reduction induces a **canonical isomorphism**

```
Tor(G)  ->  Tor(R).
```

Consequently, if a given unit `u` has any positive power in `A`, then
the **smallest** such exponent is precisely the order of its residual
class in `R`. Nilpotent layers add no exponent once eventual descent
has been established.

Proof. Units lift across nilpotent ideals. A unit whose residual class
is diagonal can be divided by a unit of `A` having the same residue,
leaving an element of `1+N_B`. The finite series

```
log(1+x) = x - x^2/2 + x^3/3 - ...,
exp(x)   = 1 + x + x^2/2! + ...
```

are mutually inverse group isomorphisms between `1+N_B` and the
additive group of `N_B`, and restrict to the corresponding groups for
`A`. This proves the exact sequence.

For a torsion residual class `r` of order `e`, choose any lift `g` in
`G`. Then `e g` belongs to the kernel. Subtract its uniquely defined
`e`-th part in that kernel from `g`; the result is an `e`-torsion lift
of `r`. A torsion lift is unique because the kernel is torsion-free.
If an actual class `g` is torsion, its order therefore equals the order
of its residue. This is a group-theoretic proof retaining every
nilpotent layer. Alternatively, the simple-root lifting argument in
the proposal proves the same exponent statement directly.

### A necessary distinction: residual torsion is not enough

A specific unit can have torsion residue but no power in `A`. For
example,

```
A=k,  B=k[epsilon]/(epsilon^2),  u=1+epsilon
```

in characteristic zero has trivial residual class, whereas
`u^n=1+n epsilon` never belongs to `A` for positive `n`.
Thus the torsion isomorphism does **not** assert that every lift of a
torsion residual class is torsion.

The missing condition has an exact logarithmic certificate. Suppose
the residual class of `u` has order `e`, so all residues `alpha_i^e`
equal a common `beta in K^*`. Choose `a in A^*` with residue `beta`.
Define

```
delta(u) = (1/e) log(u^e/a) mod N_A  in N_B/N_A.
```

This is independent of `a`, because replacing `a` changes the
logarithm by an element of `N_A`. It is also independent of replacing
`e` by a positive multiple and is a homomorphism on the preimage of
`Tor(R)`. The following are equivalent:

```
delta(u)=0;
u^e belongs to A;
some positive power of u belongs to A.
```

Indeed `log(u^e/a) in N_A` is equivalent, after exponentiating, to
`u^e/a in 1+N_A`. Conversely, if a power descends, Theorem 1 forces
the nilpotent kernel component to vanish. On the preimage of residual
torsion there is therefore a canonical decomposition into the
nilpotent defect and the unique torsion lift.

## 2. Split fields: a shared Kummer extension plus finite phases

Assume now that `K` has characteristic zero and contains all roots of
unity. Let `alpha=(alpha_i) in product E_i^*` have torsion class in
`R`, meaning that `alpha_i^n` are all the same element of `K^*` for
some `n>0`.

Fix embeddings of the `E_i` into one algebraic closure of `K`. Then

```
alpha_i = zeta_i alpha_1,  zeta_i in mu_infinity(K),  zeta_1=1.
```

It follows that all fields `K(alpha_i)` are the **same cyclic Kummer
extension** in this algebraic closure. Put

```
m = [K(alpha_i):K].
```

Then `m` divides every `[E_i:K]`. Also `alpha_i^m in K^*` for every
`i`. If

```
beta_i = alpha_i^m,
t = lcm_i order(beta_i/beta_1),
```

the exact residual order is

```
e = m t = lcm(m, order(zeta_2), ..., order(zeta_s)).
```

Proof. The polynomial `T^n-alpha_1^n` splits over `K(alpha_1)` because
`mu_n subset K`; thus `K(alpha_1)/K` is cyclic Galois. Its group embeds
in `mu_n` by `sigma -> sigma(alpha_1)/alpha_1`. Its order is `m`,
and `alpha_1^m in K`. Any exponent putting `alpha_1` in `K` is
divisible by `m`; conversely each multiple of `m` does so.
The same statements hold for each `alpha_i`. After writing an exponent
as `m h`, equality of all branch values is equivalent to
`(beta_i/beta_1)^h=1` for every `i`, giving `e=m t`.

The formula using `beta_i` is intrinsic. The formula using `zeta_i`
uses chosen embeddings, but its value is unchanged when those
embeddings change: the resulting changes are roots of unity of order
dividing `m`.

For a single field `E`, the phase factor is absent:

```
e=m divides [E:K].
```

This sharpens the original proposal. If actual residual extension
degrees at the finitely many generic conductor components are known,
the common exponent is their least common multiple. The proposal's
`lcm(1,...,r)` remains valid when only the numerical bound
`[E:K]<=r` is known. In particular, an actual degree-three field needs
exponent three, rather than the conservative exponent six obtained
from the bound alone.

For several fields, the bounded Kummer factor satisfies

```
m divides gcd_i [E_i:K],
```

but the relative phase factor can have arbitrarily large order.
The example `A=k`, `B=k x k`, `u=(1,zeta)` exhibits arbitrary exact
order with total residual degree two. This obstruction persists with
fixed ring lengths. A degree or length bound alone cannot control
split phases.

One optional description of the residual torsion is useful. With
the chosen embeddings, put `F=intersection_i E_i` inside the algebraic
closure. The preceding argument gives

```
Tor((product E_i^*)/K^*)
    ~= Tor(F^*/K^*) x mu_infinity(K)^(s-1),
```

by taking the common radical class represented by `alpha_1` and the
ratios `alpha_i/alpha_1`. The displayed splitting uses embeddings;
the intrinsic exponent and the torsion reduction theorem do not.

## 3. Audit of the proposed global compression theorem

The proposal's global theorem is correct under its stated hypotheses:
finite normalization, integral Cohen--Macaulay projective surface,
characteristic zero, a section `Q` which is a unit at every generic
upstairs conductor point, a single residual field over each generic
downstairs conductor point, and existence of an actually descending
power. The unit hypothesis and the existence of some descending
power are essential.

The local theorem proves membership in the **full** conductor
quotient, not only its reduction. At a closed point of a surface,
both `O_X` and `nu_*O_S` have depth at least two: the first by
Cohen--Macaulayness and the second by normality and finiteness.
Hence the depth lemma gives

```
depth_x(nu_*O_S/O_X) >= 1
```

when the quotient is nonzero. This quotient has no associated closed
points. Its only possible associated points are generic points of
the conductor curves. A section of this quotient vanishing at all
those points is zero. This justifies passing from generic conductor
membership to global descent; no Cartier hypothesis on the
downstairs conductor is needed.

A sharper choice in that theorem is

```
N = lcm_eta [E_eta:k(eta)]
```

when the actual single-field degrees are known. No Artinian length
bound enters this exponent.

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

**Theorem 2.** A positive power of a section of a positive tensor power
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
above `C`. In the semilocal normalization, which is a product of
DVR localizations at those branches, a sufficiently large power
therefore belongs to the actual conductor ideal. Such a power
automatically belongs to `O_X,eta`. Take a common multiple large
enough for both requirements. The purity/depth argument in section
3 gives global descent to `L^(Nd)`. Its pullback still has full
support `W`; surjectivity of `nu` gives zero support exactly `C`.

If `X` is a degree-`a` hypersurface in `P^3` and `L=O_X(1)`, every
descending section of `O_X(b)` lifts to an ambient degree-`b` form,
since `H^1(P^3,O(b-a))=0`. Thus this criterion is exactly a criterion
for an ambient STCI mate **on the chosen carrier**.

The theorem retains both kinds of conductor behavior. On components
lying over `C`, vanishing enters the conductor after a large power.
On components away from `C`, unit descent is precisely a torsion
condition. For characteristic zero, Theorem 1 separates the latter
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

Let its nonzero members be `h_1,...,h_q`. Then Theorem 2 has the
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
by sections 1--5.

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
and full conductor-unit map in Theorem 2 make no such assumption.
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
logarithmic obstruction. The lattice criterion of Theorem 2 still
holds; this observation simplifies its local unit map. It does not
make nonconstant residual ratios automatically torsion over function
fields, and it does not prove the universal STCI statement.

## 9. Audit record and next mathematical target

The independent `split_unit_audit` checked Theorem 1, the residual
torsion versus a given lift distinction, the logarithmic defect, the
common Kummer extension, and the exact split exponent. Its useful
messages were received before a transport interruption; the root
proofs above preserve their content. The independent
`cartier_lattice_audit` checked generic-to-global sufficiency and
flagged two scope improvements adopted here: the lattice theorem
works in arbitrary characteristic, and its finite Hilbert-basis
existence is not an effective algorithm. Its primitive-ray check is
complete: it independently confirmed the torsion-free class-group
bound and the exact one-branch arithmetic progression of mate
degrees. A separate combinatorial/APic check through that auditor
also confirmed the finite support-covering argument and the APic
scope. These audits concern the new theorem rather than a rerun of
accepted repository computations.

The highest-value next target is to compute one **carrier-class
relation/descent map**, using the accepted normalization and full
conductor data already in the repository. For smooth rational
normalizations generically regular along `C0`, start with base degrees
`1,2,4`, rather than arbitrary mate degrees. For thick carriers,
compute all branch classes and the map `phi`; then determine whether
the descent cone has full support. The irreducible global gaps are:

* classification or degree control of all possible integral carriers;
* class-group and branch-lattice control when the normalization is
  nonrational, singular, or has multiple branches over `C`;
* actual non-torsion conductor-unit relations, especially for split
  components off `C`;
* simultaneous compatibility with the separately developed thick
  valuation/Rees constraints.

No fixed-carrier finite reduction is a theorem that every possible
carrier has been covered. No field-degree bound eliminates split
phases, and no reduced conductor computation certifies the
characteristic-zero nilpotent defect.
