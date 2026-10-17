# Independent conceptual audit of the finite formal-obstruction frontier

Date: 2026-10-15. Reviewer: `new_blowup_bridge_review`.
Status: **PASS WITH THE PRECISE EMBEDDED-CARTIER FUNCTOR BELOW**.
This review concerns only the new relative representability,
nonreduced-base, gluing, and noetherian stabilization arguments. The
accepted actual chart, first and second obstruction constructions and
their audits, and actual-CI bridge are premises and were not rechecked.
No old verifier or degree enumeration was run.

Reviewed proposal:
[uniform root-tower finite determinacy](2026-10-15-generalization-uniform-root-tower-finite-determinacy.md).
The separate
[all-order cohomology audit](2026-10-15-generalization-uniform-root-tower-cohomology-independent-audit.md)
supplies the stated vanishing, ranks, and coefficient twists. This note
checks the conceptual bridge from those bundles to the asserted scheme
and formal lifting functor.

## 1. The functor must parametrize embedded ideals

Use the proposal's fixed ambient formal neighborhood of the effective
Cartier divisor `E`, with `J=I_E/I_E^2`, and put

```
E_m=V(I_E^(m+1)),            E_0=E.
```

There is a square-zero **closed immersion** `E_(m-1) subset E_m`, with
kernel `J^m` on structure sheaves. There need not be a scheme morphism
or retraction `E_m -> E_(m-1)`. The proof uses restriction along the
closed immersion and does not assume such a retraction.

For a parameter scheme `T -> U`, let `F_m(T)` be the set of effective
Cartier ideals

```
I_m subset O_(E_m x T)
```

whose restriction as an embedded ideal to `E x T` is the specified
universal root ideal. The intended flatness condition is that the
quotient `O_(E_m x T)/I_m` is flat over `T`. These are ideals as
subobjects of a fixed structure sheaf. Their local equations are not
extra data, and global principality of the ideal is not required.

In this situation the flatness and normal-layer condition are
automatic. The universal root is a relative effective Cartier divisor
flat over `U`; hence after any base change its equation `f_T` acts
injectively on `O_(E x T)` and on every invertible layer `J^i x T`.
For any lift `h` of a local root equation, this regularity on the
associated graded layers proves that `h` is a nonzerodivisor on each
`E_m x T`. The quotient filtration has successive layers

```
J^i|Z_T,                 0<=i<=m.
```

They are `T`-flat, so the finite filtered quotient is `T`-flat. This
argument includes nonreduced parameter bases and nonreduced root
divisors. It does not infer regularity from closed-point behavior alone.

## 2. The relative cohomology assertion is strong enough

Let `p:Z_univ -> U` be the proper universal root family. Include the
coefficient-space line factor in the actual correction sheaf:

```
M_m=N_(Z_univ/(E x U)) tensor J^m|Z_univ.
```

Its restriction to an individual root is the proposal's `L_m`.
The audited constant-rank presentation is

```
0 -> S_m tensor O_U -> T_m tensor O_U(1) -> V_m -> 0.
```

The first map is a locally split injection with locally free cokernel.
This is more than a fiberwise dimension statement: after every base
change `T -> U`, including a nonflat or nonreduced one, it remains an
exact sequence with the same locally free cokernel pulled back.
The divisor resolution on the fixed `E x U` consequently gives

```
R p_* M_m = V_m[-1],
p_*M_m=0,
R^1 p_*M_m=V_m,                                      (1)
```

compatibly with these base changes. The coefficient factor `O_U(1)`
is essential here; the alternate `Q_m tensor O_U(1)` convention is
equivalent.

Thus the all-order vanishing is genuinely relative. Pointwise
`H0=0`, without (1) or an equivalent base-change proof, would not by
itself justify the scheme-valued uniqueness needed below.

## 3. Square-zero lifting has the asserted obstruction and no unit moduli

Fix a lift on `E_(m-1) x T`. On a suitable cover, lift one local equation
to `E_m x T`; Section 1 proves it remains regular. Transition units of
the lower ideal lift locally through a nilpotent extension. After
adjusting by a lifted unit, the difference between two local equations
lies in `J^m`, modulo multiples of the root equation. The resulting
sheaf of differences is exactly

```
Hom(I_Z/I_Z^2,J^m|Z)=M_m|Z_T.                         (2)
```

Because the extension is square zero, the transition differences add
on triple overlaps. They define a class in `H1(Z_T,M_m|Z_T)`, whose
vanishing is equivalent to gluing the local embedded ideals. If it
vanishes, the set of global ideal lifts is a torsor under
`H0(Z_T,M_m|Z_T)`.

Equation units have already been divided out in (2): replacing a lift
by `(1+v)h` changes its equation by `v h`, a multiple of the root
equation in the new layer, and does not change its ideal. Moreover an
automorphism of an ideal preserving its embedding in the structure
sheaf is the identity. There is no residual unit automorphism stack
or hidden correction parameter.

By (1), the difference group is zero after every parameter base change.
The Leray sequence also identifies

```
H1(Z_T,M_m|Z_T)=H0(T,V_m|T),                           (3)
```

since the degree-zero pushforward vanishes. The obstruction is therefore
a canonical section of `V_m|T`. It is natural under base change, not
merely a list of values at geometric points. Its scheme-theoretic zero
locus detects vanishing on nilpotent parameter directions as well.

## 4. Induction gives closed scheme representability

Start with `K_0=U` and its universal root ideal. Suppose `K_(m-1)`
represents the lower ideal-lifting functor and carries its universal
ideal. Applying Section 3 gives a canonical obstruction section of
`V_m|K_(m-1)`. Let `K_m` be its zero scheme.

For every `T -> K_(m-1)`, the section pulls back to the obstruction for
the pulled-back lower ideal. A lift exists exactly when the map factors
through `K_m`. Such a lift is unique: the relative `H0` in (1) is zero.
Local existence over parameter charts therefore glues, by uniqueness,
to a universal ideal on `E_m x K_m`. This proves representability by
the closed immersion

```
K_m subset K_(m-1)
```

with its full scheme structure, including possible nilpotents.

All earlier-stage compatibility is automatic under restriction, since
the lower ideal is unique. Nonlinear base-coordinate changes and lower
equation-unit corrections affect the canonical obstruction section;
they do not change the new-layer coefficient sheaf (2). This is an
embedded Cartier-ideal tower, before an independent second relation
changes the actual-CI problem.

## 5. Noetherian stabilization is sufficient, with the stated limitation

The closed subschemes `K_m` all lie in the one fixed noetherian,
quasi-compact coefficient open `U`. Their ideal sheaves form an
ascending chain of coherent ideals. On each affine noetherian chart
the chain stabilizes, and a finite affine cover supplies one common
index `N`. Thus

```
K_N=K_(N+1)=K_(N+2)=...
```

as schemes, not only as sets. This is a valid use of noetherianity.
It depends on the uniqueness that kept all stages over the same fixed
parameter scheme. It would not follow from noetherianity of unrelated
spaces with new correction parameters at each stage.

The integer `N` is an eventual stabilization index for the entire
chain. One observed equality of adjacent stages does not establish
that those stages are already stable; a later obstruction can still
impose new conditions. No computable value or uniform numerical bound
for `N` follows from the ranks alone.

## 6. The stable scheme represents formal Cartier ideals

Let `K_infinity=K_N`. Its universal ideals at all orders form a
compatible system. To check that their inverse limit is a formal
Cartier ideal, work over an affine parameter chart and an affine open
of `E` trivializing the root ideal. The corresponding nilpotent
thickenings of this affine open are affine. Restriction of successive
invertible ideal modules is surjective, so a chosen lower generator
can be lifted to a generator at the next order. A lift of a generator
is still a generator by nilpotent Nakayama. Equivalently, one can
adjust any higher generator by a lifted unit.

Choose these generators compatibly. Their inverse limit is a single
local formal equation. It is a nonzerodivisor: an annihilator would
reduce to an annihilator of the regular equation at every finite
stage, hence would be zero in the separated inverse limit. On overlaps
the compatible units also pass to the inverse limit. The limit ideal
is consequently invertible and locally generated by a regular formal
equation, with the prescribed root. Its finite quotients have the
flat normal layers of Section 1.

This constructs the formal ideal directly. No algebraization theorem,
properness of the ambient threefold, or globally defined formal
equation is assumed. Properness of the root family was used to obtain
the relative cohomology bundle, not to turn a formal divisor into an
algebraic hypersurface.

Conversely, a formal Cartier ideal with this root restricts to an
object of every finite lifting functor. Its parameter map therefore
factors through every `K_m`, hence through `K_N`. Thus the stable
scheme represents the stated compatible formal ideal functor. This
statement concerns compatible Cartier ideals on the adic formal
neighborhood; it makes no extra claim about flatness of an infinite
inverse-limit module over an arbitrary nonnoetherian base.

## 7. The actual-CI consequence retains its strict indexing

Use the accepted bridge only within its stated hypotheses, in
particular the smooth actual root and jointly generating leading
symbols. If its ordinary generic initial relation degrees are `(r,s)`,
then the strict intersection has local ideal `(h,u^(s-r))`. With the
current convention `E_m=V(u^(m+1))`, it supplies a Cartier root lift
only through stages

```
m<s-r.
```

Accordingly an actual CI with `s>r+N` must have its root in the stable
formal locus `K_N`. Outside this locus it must satisfy `s<=r+N`.
For `r=2`, the strict implication is `s>2+N`. At equality the CI only
supplies stage `N-1`, and no membership in `K_N` follows.

This is a necessary bounded-gap alternative. Formal ideal lifting is
not sufficient for an actual supported CI; spectral second-relation
descent, its extension, and projective realization remain separate.
The tower is defined on the full basepoint-free root open, while this
application uses the smooth-root part where the actual bridge applies.

## Disposition

The new tower and finite formal-obstruction frontier pass this
conceptual review under the precise embedded-Cartier formulation.
The two wording requirements communicated to the owner are to use the
closed immersions `E_(m-1) subset E_m` rather than imply nonexistent
retractions, and to state flatness for the divisor quotient. Both are
supported by the proof above and introduce no extra hypothesis in the
stated universal root family.

No value for `N`, equations of the stable locus, algebraization,
emptiness, or unrestricted STCI conclusion is proved. The universal
STCI question and unrestricted characteristic-zero `C0` remain open.
