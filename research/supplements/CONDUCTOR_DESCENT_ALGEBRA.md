# Full conductor membership, unit powers, and pure descent

These algebraic mechanisms apply beyond the fixed quartic. They consolidate the independently reconstructed power-descent argument, including the counterexamples that limit tensor, reduced, and numerical substitutes. They are source-reviewed mathematics; no new canonical promotion is made here. Applications must establish the actual conductor rings and the purity hypothesis.

The relevant geometric object is the finite pinching square of a normalization, rather than only its reduced double curve. [Stacks, §15.5](https://stacks.math.columbia.edu/tag/08KG) gives the ring fiber-product construction and its localization. The proofs below establish the particular membership and power assertions directly. The literature statement does not supply STCI existence.

## 1. Actual membership is stronger than a tensor equalizer

Let `A` be a Noetherian algebra over a characteristic-zero field, and let
`A ⊂ B` be a finite extension. In the normalization application A is an
integral domain and B its finite normalization. Let

    I = {a ∈ A : aB ⊂ A}, R=A/I, T=B/I.

The conductor I is an ideal in both A and B, and the injection R→T gives
the exact identity

    A = B ×_T R.

Indeed, if b modulo I belongs to R, choose a in A representing it;
then b−a belongs to I⊂A. Consequently

    q^k ∈ A  ⇔  (q mod I)^k ∈ R.                 (1)

No reducedness, normality of R or T, flatness, or separability of the
conductor map is needed. Fiber products and their compatibility with
localization are also recorded in
[Stacks, Section 15.5](https://stacks.math.columbia.edu/tag/08KG).

If q is a unit in T, write q1=q⊗1 and q2=1⊗q in E=T⊗_R T. Descent of
q^k implies that u=q1/q2 satisfies u^k=1 in the entire possibly nonreduced
ring E. Over an algebraically closed field, E decomposes by the mutually
orthogonal idempotents

    e_ζ = (1/k) Σ_{j=0}^{k−1} ζ^(−j) u^j,  ζ^k=1,

and on the e_ζ component one has the exact identity q1=ζq2. Thus there
is no additional nilpotent error in this necessary root-of-unity identity.

The converse tensor implication is false without further descent
hypotheses. Here is an explicit finite normalization counterexample.

    A=k[t^3,t^4] ⊂ B=k[t], I=t^6B,
    R=span_k{1,t^3,t^4} ⊂ T=k[t]/(t^6), q=1+t^5.

The conductor follows from the semigroup `<3,4>`: every integer at least
six occurs, but five does not. The element q is a unit in T. In the
tensor product T⊗_R T, with x=t⊗1 and y=1⊗t, the relations x^3=y^3 and
x^4=y^4 imply

    x^5−y^5=(x+y)(x^4−y^4)−xy(x^3−y^3)=0.

Hence q⊗1=1⊗q, and the same is true of every power. Nevertheless

    q^k = 1+k t^5  in T,

which is not in R for any positive integer k in characteristic zero.
An exact tensor equalizer test, even on the unit locus, therefore cannot
replace the actual R-subspace membership test (1).

## 2. Powering cannot repair unit nilpotent jets

Assume more generally that `R ⊂ T` is a finite extension of Noetherian
Q-algebras, and q∈T is a unit. Write Rred and Tred for their reductions.
The induced map Rred→Tred is injective: a member of R which is nilpotent
in T is already nilpotent in R.

**Unit jet lemma.** If qred belongs to Rred, then

    q^k ∈ R for one positive k  ⇔  q ∈ R.        (2)

Proof. Integrality shows that qred is a unit in Rred: an element of Rred
which becomes a unit in the integral extension Tred cannot lie in a
maximal ideal, by lying over. Choose a lift r∈R of qred. The nilradical
of R is nilpotent, so r is a unit of R. Now q/r=1+n with n in the
nilradical N of T; N is nilpotent. Finite polynomials define

    log(1+n)=n−n^2/2+n^3/3−...,
    exp(z)=1+z+z^2/2!+...,

on N, and they are inverse. If q^k∈R, then (q/r)^k∈R and

    k log(q/r)=log((q/r)^k) ∈ R.

Since k is invertible, log(q/r)∈R∩N. Taking its finite exponential gives
q/r∈R and hence q∈R. The reverse implication is immediate. This proof
retains every nilpotent layer of T; it is not a first-jet argument.

There is a useful exact reformulation. For a unit q define

    Ered={n∈Z : qred^n ∈ Rred^×}.

This is a subgroup of Z. If Ered={0}, no positive full power descends.
Otherwise write Ered=dZ with d≥1. Then the set of positive full
descending powers is either empty or precisely

    {d,2d,3d,...}.                               (3)

Indeed, a successful k has k=dm. Applying (2) to the unit q^d shows
that (q^d)^m∈R forces q^d∈R. Conversely its multiples then descend.
Thus the nilpotent structure can invalidate every reduced candidate,
but cannot force a larger multiple of the reduced minimum d to become
the first successful power.

The unit condition is essential. For A=k[t^2,t^3]⊂B=k[t], q=t does not
descend whereas every q^k with k≥2 does. Its conductor residue is
nilpotent and is not a unit.

## 3. Reduced generic phases and the unibranch bound

At a generic conductor point the actual R is Artinian local. Put
K=Rred and write

    Tred=Π_j L_j,

where each L_j/K is a finite field extension. K contains the algebraically
closed characteristic-zero ground field. For a unit tuple α=(α_j), take
all its values under all K-embeddings L_j→Kbar. A positive reduced power
descends precisely when every ratio between these finitely many geometric
values is a root of unity. If that holds, the least reduced exponent d
is the least common multiple of the orders of the ratios to one reference
value. Their common d-th power is Galois invariant, hence belongs to K.

If Tred consists of one field L, this gives a bound

    d=[K(α):K] ≤ [L:K].                          (4)

For completeness, if α^m∈K, then K(α) contains every root ζα of
X^m−α^m because all m-th roots of unity are in K. This polynomial is
separable, so K(α)/K is Galois with a cyclic group of order e. Its image
is the unique order-e subgroup of μ_m; thus α^e is fixed, and minimality
gives d=e.

No bound by the number of geometric branches exists in the split case.
For any root of unity ζ of order m, let

    A={p(t)∈k[t] : p(0)=p(1)}, B=k[t],
    I=t(t−1)B, R=k, T=k×k,
    q=1+(ζ−1)t.

This is an integral finite-type domain with finite normalization B:
t is integral over A via t^2−t−t(t−1)=0, and A=k+t(t−1)k[t]. The
conductor formula is exact because interpolation makes arbitrary pairs
of endpoint values in B. The residue of q is the unit (1,ζ), and

    q^k ∈ A  ⇔  ζ^k=1  ⇔  m divides k.

The reduced conductor has only two branches, while m is unbounded.
In a genuinely degree-two single-field generic conductor, however,
(4) bounds the candidate exponent by two. That degree-two hypothesis
must be established for the actual projection, not assumed from an
average conductor-degree calculation.

There is also a pointwise subintegral statement. Suppose q^k∈A and q
is a unit in B. If over a prime p of A all geometric residue values of
q coincide, then q belongs to A_p. To prove it, set C=A[q]. The fiber
C⊗_Aκ(p) is a quotient of κ(p)[z]/(z^k−q^k), a reduced separable
algebra because q^k is a unit. The common residue value is in κ(p)
in characteristic zero, so this fiber is κ(p). Nakayama applied to
(C/A)_p now gives C_p=A_p. The equal-residue condition is automatic
where B→A is subintegral. It fails in the split root-of-unity example.
Thus power descent forces descent of the section itself on a subintegral
unit locus, but not on every unit locus of a normalization.

## 4. Purity converts generic full membership into global descent

Let ν:S→X be a finite birational normalization of an integral surface,
and let

    M=ν_*O_S/O_X.

Assume M is pure of dimension one: it has no nonzero coherent subsheaf
supported on finitely many points. If L is invertible on X, then a global
section s of ν^*L descends to a section of L if and only if its germ
belongs to L at every generic point of Supp(M).

Proof. Its image σ in M⊗L is a global section. If its generic germs
vanish, the coherent subsheaf generated locally by σ has finite support.
Purity makes this subsheaf zero, so σ=0 and s descends. Necessity follows
from the defining exact sequence. For a one-dimensional Cohen–Macaulay
module, purity follows either from a nonzerodivisor killing no finite
length submodule, or from the absence of embedded associated primes;
the latter is [Stacks, Lemma 10.103.7](https://stacks.math.columbia.edu/tag/00N2).

It is essential that these generic tests use the full Artinian conductor
algebras, rather than only their residue fields. Purity removes an extra
obstruction supported at finitely many points only after the entire
generic obstruction has vanished. The example in section 1 fails this
full generic test.

## 5. Exact application to the quintic A4 lane

In the quintic A4 lane, the geometric inputs proved in the [quintic carrier geometry](QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md) are

    M=ω_Γ(−H), Γ pure Cohen–Macaulay of dimension one,
    Q∈H0(S,4H), div_S(Q)=5c,
    C0 generically regular on X.

The canonical module of the Cohen–Macaulay curve Γ is maximal
Cohen–Macaulay, so M is pure. Since c is not a conductor component,
Q, after trivializing O_X(4H), is a unit at every generic conductor point.
For each such point η form the actual rings

    Rη=O_X,η / Iη  ⊂  Tη=(ν_*O_S)η / Iη,

and let dη be the minimum reduced exponent in section 3, if it exists.
Then an actual power of Q descends if and only if:

1. Every generic conductor point has a finite dη.
2. The full, possibly nonreduced membership test Q^dη ∈ Rη passes at
   every such point, in a local trivialization.

If these conditions hold, D=lcm_η(dη) is the least positive global
descending exponent, and all global descending exponents are its positive
multiples. Proof: (3) supplies the exact local exponent groups; purity
supplies sufficiency and prevents any additional isolated obstruction.

Multiplying a local trivialization by a unit from O_X,η multiplies Q by
a unit of Rη. This changes none of these exponent groups or membership
conditions. The argument concerns sections of the pullback of an actual
downstairs line bundle; a line bundle merely defined upstairs cannot be
treated this way.

For a quintic hypersurface X⊂P3, every section of O_X(4D) lifts to an
ambient homogeneous polynomial: the hypersurface sequence and
H1(P3,O(4D−5))=0 give surjectivity. If Q^D descends, its normalized divisor
is exactly 5D c, and finite surjectivity of ν shows that the resulting
ambient equation cuts X set-theoretically down to C0. Conversely the
recorded quintic structural theorem says every hypothetical mate pulls
back to a scalar Q^k. Hence these generic full-conductor tests are an
exact mate-existence criterion within this already reduced quintic lane.

This is a structural reduction, not a parameter-space solution. In
particular, the split reduced phases can still have arbitrary root-of-unity
orders as the projection varies. What is removed is a separate search over
ever larger multiples to repair generic nilpotent jets, or a search for
extra isolated descent obstructions after full generic membership succeeds.


## 6. Differential obstruction on a prescribed Cartier ray

Let `nu:S->X` be a finite birational normalization of an integral projective surface over an algebraically closed characteristic-zero field, `L` invertible on X, and `H=nu*L`. Suppose the full reduced inverse support of an integral curve C is a nonzero smooth ample Cartier curve c mapping isomorphically to C. Suppose a section Q of H has divisor m c. Let p be a smooth point of S outside c, h a local frame of L at nu(p), and q=Q/(nu*h). If some v in ker(dnu_p) satisfies dq_p(v)!=0, no positive power of L has a section with zero support exactly C.

Indeed, a hypothetical section of L^b pulls back to a divisor r c. Since `(r-mb)c~0`, intersection with an ample divisor gives r=mb. The ratio to Q^b has divisor zero on normal projective integral S, so is a nonzero scalar. Its local expression is lambda q^b. Every pulled-back function annihilates ker(dnu_p), whereas

    d(lambda q^b)_p(v)=lambda b q(p)^(b-1)dq_p(v)!=0.

This contradiction uses q(p)!=0 and characteristic zero. A different downstairs frame multiplies q by a pulled-back unit, whose derivative kills ker(dnu_p), so the test is frame independent. The target X may be singular: its Zariski tangent space suffices. [Plane projection examples](PROJECTION_SUPPORT_AND_DIFFERENTIAL_OBSTRUCTIONS.md) realize this obstruction even when full inverse support and the upstairs divisor class both pass.

The hypothesis that Q is a section of the pullback of an actual downstairs line bundle is essential for this comparison. The unit-power lemma applies to the full nilpotent structure, while this differential test can already detect a nonzero first defect. In characteristic p, the derivative of a p-th power is zero; the all-power conclusion is unavailable.

## 7. What is reusable, and what remains to compute

The structural mechanism is exact full membership followed by purity. The residue-field phase detects a finite candidate exponent; in characteristic zero, the unit jet lemma tests that minimum once. A single residual field bounds the candidate by its extension degree. Split residual algebras permit unbounded orders, so no universal degree bound follows from a branch count. These are proved implications, not analogies between conductor and normal-filtration defects.

For a candidate carrier, compute every actual generic conductor algebra R_eta⊂T_eta and the proposed section's image, retain nilpotents, and verify purity before replacing global membership by generic tests. The quintic projection-family computation remains open. In a generically singular carrier the proposed section may fail to be a conductor unit; the nonunit cusp example above prevents using the unit lemma there.

The inherited independent algebra review covers §§1–5, and the plane differential audit covers §6. The tensor counterexample, split-order counterexample, nonunit cusp, and denominator-sensitive plane example are mathematical proof components, not disposable verification logs.

## 8. Full unit quotient and its canonical torsion lift

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
nilpotent layer. Alternatively, in the single-field case put `m=[K(alpha):K]`, where `alpha=bar u`, and suppose u^n belongs to A. The cyclic Kummer argument gives m|n. Set s=n/m and w=u^n. The polynomial V^s-w has the simple nonzero residual root alpha^m in K. Artinian local rings are Henselian, so that root lifts uniquely in A and in B. Its image from A and the root u^m in B coincide by uniqueness, proving u^m belongs to the full ring A. This alternative proof uses simple-root uniqueness, whereas the logarithmic proof displays the additive nilpotent defect.

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

## 9. Split fields: the exact Kummer and phase factorization

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
a sufficient common exponent is the least common multiple of those extension degrees. The proposal's
`lcm(1,...,r)` remains valid when only the numerical bound
`[E:K]<=r` is known. In particular, degree three is a sufficient exponent for an actual degree-three residual field, conditional on eventual descent; the least local exponent is one or three. This improves the conservative exponent six obtained from the bound alone, without identifying the minimum from the extension degree.

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


## 10. Global compression and characteristic boundaries

Work over an algebraically closed characteristic-zero ground field (more generally, require every generic downstairs conductor residue field to contain all roots of unity). Under the purity and unit hypotheses above, if each generic reduced upstairs conductor algebra is a single field E_eta over k(eta), a section Q with one descending power has a descending power of exponent `lcm_eta [E_eta:k(eta)]`. If only `[E_eta:k(eta)]<=r` is known, the conservative exponent is `lcm(1,...,r)`. This follows from the exact local exponent divisibility and purity. It is independent of nilpotent lengths. For a hypersurface X⊂P3 and Q a section of the pullback of O_X(d), it bounds the constructed ambient mate degree by `d*lcm(1,...,r)`, provided Q already has precisely the entire inverse support. Neither the primitive section degree nor absence of split residual algebras is automatic.

In characteristic p, if the nilradical is killed by the p^h-th power and the reduced class of u has order e, choose a downstairs lift a of its common residual e-th power. Then `(u^e/a)^(p^h)=1`, so `u^(e p^h)` descends. A finite unit eventually descends if and only if its reduced class is torsion; nilpotents may add p-powers. This finite assertion neither kills nonconstant function-field phases nor gives one exponent for an infinite formal tower. The [marked-deformation characteristic treatment](../synthesis/marked_deformation_and_absorption.md#3-characteristic-and-descent-finite-repair-is-not-an-infinite-lift) retains the exact all-order A_N controls.
