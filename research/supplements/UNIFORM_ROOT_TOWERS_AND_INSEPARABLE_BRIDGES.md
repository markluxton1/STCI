# uniform root towers and inseparable bridges

Permanent mathematical dossier preserving complete arguments, assumptions, characteristic boundaries, counterexamples and unresolved claims. No new theorem promotion is implied.

---

## 2026-10-15-generalization-uniform-root-tower-finite-determinacy

# A fixed finite-type root family has a finite formal-obstruction frontier

Date: 2026-10-15. Author: `universal_root_obstruction`.
Status: **NEW GENERAL STRUCTURAL THEOREM; independent conceptual and
cohomological reviews passed**. Accepted first/second root-curve
obstructions and their audits are premises. No accepted verifier is rerun.

## 1. General statement

Let `C=P1` be a smooth curve in a smooth threefold with balanced conormal

    N_C^*=O_C(-lambda) tensor V,       dim V=2.

Fix the actual formal neighborhood of `C`, and work in its induced
actual formal neighborhood of the exceptional divisor after blowing up `C`.
Write

    E=P1_base x P1_direction,
    J=I_E/I_E²=O_E(-lambda,1).

Fix integers `r>=1`, `epsilon>=0`, and assume

    lambda>3 epsilon.                                      (1)

Let `U` be the basepoint-free coefficient open in
`P(H0(E,O_E(epsilon,r)))`: no base fiber polynomial is zero. Every root
divisor `Z` in this open is therefore Cartier and finite flat of degree
`r` over the base, including singular and nonreduced roots. The first
relation is saturated everywhere. The family does not discard a
coefficient base point by saturation.

There is a canonical descending sequence of closed subschemes of this
single fixed finite-type parameter space,

    U=K0 superset K1 superset K2 superset ... ,              (2)

with these properties.

1. `Km` represents embedded effective Cartier ideals extending the
   universal root divisor through the `m`-th exceptional neighborhood.
   Such an ideal is unique whenever it exists; multiplying a local
   equation by a unit is a change of presentation, not another object.
2. The next obstruction is a canonical section of a vector bundle on
   `K(m-1)`, of rank

       h_m=m(r lambda-epsilon)-(r epsilon+r+epsilon).       (3)

   Its zero scheme is `Km`.
3. There is a finite integer `N`, depending on the fixed actual formal
   embedding and `(r,epsilon)`, such that

       KN=K(N+1)=K(N+2)=...                                (4)

   as schemes. The stable closed scheme represents compatible formal
   embedded Cartier ideals with the specified root divisor.

The bound `N` is existential. It is not supplied by a numerical degree
count, and the theorem does not determine it. Equality of one adjacent
pair `Km=K(m+1)` does not prove eventual stabilization: later obstruction
sections may still impose new equations. A certificate of an explicit
cutoff would need to control every later section.

This is finite determinacy of a **formal first-principal-ideal problem**.
It neither algebraizes the formal ideal nor realizes it by projective
hypersurfaces. The theorem does not assert that the stable scheme is
empty or nonempty.

## 2. All-order negativity is independent of the first normal order

Let `pi:Z->P1` be the finite flat root projection. The accepted divisor
sequence gives, for every `m>=1`,

    0 -> O(-epsilon) tensor Sym^m V
      -> Sym^(r+m)V tensor O
      -> pi_*O_Z(0,r+m) -> 0.                              (5)

Thus `Bm=pi_*O_Z(0,r+m)` is a globally generated rank-`r` vector bundle
of degree `epsilon(m+1)`. Every summand in its splitting on `P1` has
nonnegative degree, and no summand has degree greater than the total
`epsilon(m+1)`.

The correction and obstruction line bundle at the `m`-th step is

    L_m=N_(Z/E) tensor J^m|Z
       =O_Z(epsilon-lambda m,r+m).                         (6)

After the base twist in (6), the maximum splitting degree of `pi_*L_m`
is at most

    epsilon(m+1)+epsilon-lambda m
      =2epsilon-m(lambda-epsilon).                        (7)

Under (1), this is already negative at `m=1` and decreases thereafter.
Consequently

    H0(Z,L_m)=0                  for every m>=1,            (8)

uniformly on the entire basepoint-free coefficient open. This proof uses
neither smoothness nor reducedness of `Z`. It depends on the movement
degree `epsilon`, but not on the first normal order `r`. Condition (1)
is a sufficient uniform condition; it need not be necessary for an
individual relation or root divisor.

The relevant divisor sequence is

    0 -> O_E(-lambda m,m)
      --f--> O_E(epsilon-lambda m,r+m)
      -> L_m -> 0.                                        (9)

The two ambient `H0` groups vanish; `H2` of the source vanishes because
the direction degree is nonnegative. By (8), multiplication induces an
injection on `H1`. The two dimensions are

    source: (lambda m-1)(m+1),
    target: (lambda m-epsilon-1)(r+m+1),                    (10)

and their difference is exactly (3). The formulas include zero-dimensional
source or target groups at the smallest allowed numerical boundary.

For `C0`, `lambda=7`, `r=epsilon=2`, this gives

    L_m=O_Z(2-7m,2+m),
    h_m=12m-8,
    H0(Z,L_m)=0 for all m>=1.                              (11)

In particular, the reviewed ranks four and sixteen at the first two
steps are the start of one uniform tower, rather than unrelated tests.

If a smooth rational curve of degree `e` in `P3` has balanced normal
bundle, then `lambda=2e-1`: restricting the Euler sequence and the tangent
sequence gives `deg N=4e-2`, and the two equal splitting degrees are
`2e-1`. Thus the sufficient all-order criterion becomes

    3epsilon<2e-1.                                         (12)

It controls every first normal order `r` at once for each fixed movement
degree satisfying (12).

## 3. Relative cohomology retains every parameter scheme structure

Let `Z_univ` be the universal root divisor in `E x U`. Its divisor line
bundle is

    O_E(epsilon,r) tensor O_U(1).

The relative version of `L_m` therefore has the extra coefficient factor
`O_U(1)`. Put

    S_m=H1(E,O_E(-lambda m,m)),
    T_m=H1(E,O_E(epsilon-lambda m,r+m)).

Its relative `H1` bundle has the exact presentation

    0 -> S_m tensor O_U
      --f--> T_m tensor O_U(1)
      -> V_m -> 0.                                        (13)

The multiplication map has the same injective rank at every geometric
point, by (8)--(10). It is consequently a locally split injection of
vector bundles with locally free cokernel `V_m`, of rank (3).
The relative `H0` is zero, and the derived pushforward of the universal
bundle in (6) is `V_m[-1]`. Presentation (13) commutes with arbitrary
base change, including nonreduced parameter schemes. This provides the
relative vanishing needed for uniqueness of ideals over a family, rather
than only uniqueness at closed points.

In the alternative convention used by the first/second notes, put

    Q_m=coker[S_m tensor O_U(-1) -> T_m tensor O_U].

Then `V_m=Q_m tensor O_U(1)`. The two descriptions have the same coefficient
line factor; no scale dependence of the universal equation is lost.

## 4. Local equations explain the obstruction functor and the unit gauge

Set `E_m=V(I_E^(m+1))`, so `E_0=E`. The closed immersion
`E_(m-1) -> E_m` is square-zero: the quotient of structure sheaves
`O_(E_m) -> O_(E_(m-1))` has kernel `J^m`. There is generally no
scheme retraction from `E_m` to `E_(m-1)`.
Over a parameter scheme `T->U`, consider embedded effective Cartier
ideals in `E_m x T` whose quotient structure sheaf is flat over `T`,
and whose restriction to `E x T` is the
specified universal root ideal. The normal layers are automatically
`J^i|Z_T` for an effective Cartier lifting of the root equation.
Regularity of the root equation on every invertible graded ambient
layer identifies these quotient layers; their flatness over `T` proves
flatness of the full quotient by its finite filtration.

Suppose a Cartier ideal has already been constructed on `E_(m-1)`.
Locally lift one of its equations to `E_m`. The lift is again a
nonzerodivisor: its reduction is a nonzerodivisor on `E`, and induction
on the nilpotent filtration preserves regularity. On overlaps, two
local lifts differ, after multiplying by a lifted equation unit, by an
element of `J^m` modulo the root equation. Their ideal differences thus
form the usual torsor under

    Hom(I_Z/I_Z²,J^m|Z)=L_m.                               (14)

The Cech class in `H1(L_m)` is the obstruction to gluing these local
Cartier ideals. When it vanishes, the set of global embedded ideal lifts
is a torsor under `H0(L_m)`, hence has exactly one member by (8).
Changing equations by units has already been divided out in (14);
there is no additional family of equation-unit choices to retain as
independent moduli.

The same reasoning works over arbitrary `T` using (13). The obstruction
is a section of `V_m|T`; it vanishes exactly on the zero scheme of that
section. A zero section produces an ideal locally on `T`, and uniqueness
glues these ideals. Inductively, the functor is represented by the zero
scheme `Km` inside `K(m-1)`, and it has its universal compatible ideal.
This proves (2) and the claimed canonical obstruction sections without
introducing new correction parameters at later orders.

## 5. Noetherian stabilization is scheme-theoretic

Each `Km` is closed in the fixed noetherian scheme `U`. Let `I_m` be its
coherent ideal sheaf in `U`. Then

    I_0 subset I_1 subset I_2 subset ... .                  (15)

On an affine noetherian chart, an ascending chain of ideals stabilizes.
A finite affine cover of `U` gives one maximum stabilization index `N`.
Hence the entire chain stabilizes as coherent ideal sheaves, proving
(4) with all nilpotent parameter information retained.

Every parameter scheme mapping to the stable scheme receives its
compatible Cartier ideals at every finite exceptional order. Their
inverse limit is locally principal: choose fixed affine opens of `E`
trivializing the root ideal, begin with a root equation on each, and
inductively adjust a generator of each higher ideal by a lifted unit
so that its reduction is the chosen lower generator. These compatible
generators form a regular formal equation. Conversely, a compatible
formal Cartier ideal restricts to every `E_m`, so its parameter map
factors through every `Km` and hence through the stable scheme.

Thus finite determinacy follows from two separate facts: all-order
uniqueness keeps the construction over one fixed finite-type parameter
space; noetherianity then bounds the order at which genuinely new
conditions can occur. Without a fixed finite-type space of all surviving
choices, noetherianity alone would not give this conclusion.

## 6. The actual-CI consequence is a bounded-gap alternative

Assume an actual-CI-to-root-curve bridge with all its stated hypotheses,
and suppose the generic normal initial regular sequence has degrees
`(r,s)`, with `s>r`. Before the second independent relation appears,
the first principal relation must be compatible in normal degrees

    r+m<s,       equivalently 1<=m<s-r.                   (16)

Therefore its root lies in `K(s-r-1)`. If

    s>r+N,                                                (17)

then (16) includes the stable order `N`, and the root lies in the formal
Cartier-lift locus. Equivalently, outside that single formal locus any
actual CI in the bridge lane must have `s<=r+N`.

This is a finite-order/frontier alternative independent of enumerating
the projective hypersurface degrees. It does not give a numerical bound
until `N` is proved, and it makes no claim that an actual CI first root
necessarily belongs to the formal locus. The second relation can enter
before that stage and change the obstruction target.

For the reviewed `(2,2)` component on `C0`, the second section is nonzero
at the smooth torsion-two seed and hence generically nonzero on its
four-dimensional first-compatibility component. The stable formal locus
is consequently a proper closed subset of that component. Determining
its equations, or proving it empty, remains a new problem; finite
determinacy does not itself settle that geometry. On the specified
three-dimensional torsion-two intersection component through the seed,
the separately reviewed
[torsion/second-zero argument](QUADRATIC_ROOT_SECOND_ZERO_AND_DUAL_COMPRESSION.md#2026-10-15-generalization-quadratic-root-torsion-second-zero-geometry)
bounds the support of the second zero locus, and hence of the stable
formal locus, by dimension two. Other components are retained.

The spectral Picard descent condition is a separate requirement on a
later second quotient relation. Formal first-principal compatibility
neither supplies that second relation nor constructs two projective
equations with the required support. The universal STCI problem and
unrestricted `C0` remain open. No commit or memory update was made.

Independent reviews of the new theorem are recorded in
[the all-order cohomology audit](UNIFORM_ROOT_TOWERS_AND_INSEPARABLE_BRIDGES.md#2026-10-15-generalization-uniform-root-tower-cohomology-independent-audit)
and [the relative functor/noetherian audit](UNIFORM_ROOT_TOWERS_AND_INSEPARABLE_BRIDGES.md#2026-10-15-generalization-uniform-root-tower-functor-independent-audit).
The latter includes arbitrary nonreduced parameter bases, equation units,
scheme-theoretic stabilization, and the regular locally principal formal
inverse limit. Neither review asserts algebraization.


---

## 2026-10-15-generalization-uniform-root-tower-functor-independent-audit

# Independent conceptual audit of the finite formal-obstruction frontier

Date: 2026-10-15. Reviewer: `new_blowup_bridge_review`.
Status: **PASS WITH THE PRECISE EMBEDDED-CARTIER FUNCTOR BELOW**.
This review concerns only the new relative representability,
nonreduced-base, gluing, and noetherian stabilization arguments. The
accepted actual chart, first and second obstruction constructions and
their audits, and actual-CI bridge are premises and were not rechecked.
No old verifier or degree enumeration was run.

Reviewed proposal:
[uniform root-tower finite determinacy](UNIFORM_ROOT_TOWERS_AND_INSEPARABLE_BRIDGES.md#2026-10-15-generalization-uniform-root-tower-finite-determinacy).
The separate
[all-order cohomology audit](UNIFORM_ROOT_TOWERS_AND_INSEPARABLE_BRIDGES.md#2026-10-15-generalization-uniform-root-tower-cohomology-independent-audit)
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


---

## 2026-10-15-generalization-uniform-root-tower-cohomology-independent-audit

# Independent audit: cohomology for the uniform root-lifting tower

Date: 2026-10-15. Reviewer: `tower_finite_audit`, with a separate
`square_zero_cartier` subreview of the equation-unit issue.
Status: **PASS for the stated cohomology, coefficient twists, and
conditional relation-gap consequence**. The finite-determinacy theorem
also requires the relative embedded-Cartier lifting argument, assigned
to a separate conceptual reviewer. No accepted chart computation,
first-incidence verifier, or second-obstruction verifier was rerun.

Reviewed proposal:
[uniform root-tower finite determinacy](UNIFORM_ROOT_TOWERS_AND_INSEPARABLE_BRIDGES.md#2026-10-15-generalization-uniform-root-tower-finite-determinacy).
The accepted first and second obstruction calculations are premises;
this review concerns the new all-order structural input.

## 1. The precise general setting

Let the ground field be fixed, let

    E = P1_base x P1_fiber,
    J = O_E(-lambda,1),

and suppose that `E` is an effective Cartier divisor in a fixed ambient
formal neighborhood with conormal `J`. Here `lambda` is an integer,
`r>=1`, `epsilon>=0`, and

    lambda > 3 epsilon.                              (1)

Let `U` be the open subset of

    P H0(E,O_E(epsilon,r))

parametrizing equations nonzero on every fiber of `E -> P1_base`.
No smoothness or reducedness condition is imposed on their root
divisors. Each root divisor `Z` is an effective Cartier divisor on `E`
and is finite flat of degree `r` over the base. In particular repeated
root directions and nonreduced root divisors are retained.

For a fixed root the proposed step-`k` coefficient sheaf is

    L_k = N_(Z/E) tensor J^k|Z
        = O_Z(epsilon-lambda k,r+k),       k>=1.     (2)

This is the correct sheaf for differences of embedded Cartier ideal
lifts from `V(I_E^k)` to `V(I_E^(k+1))`. It concerns ideals, rather
than chosen local generators of those ideals.

## 2. Uniform H0 vanishing includes every nonreduced root

Write `pi:Z -> P1_base`. For `n=r+k`, restriction of the divisor
sequence and pushforward in the fiber direction gives

    0 -> O(-epsilon)^(k+1)
      -> O^(r+k+1)
      -> W_(r+k)=pi_*O_Z(0,r+k) -> 0.               (3)

The vanishing of the relevant relative `H1` follows from `k>=1`.
Multiplication by the nonzero degree-`r` fiber equation is injective
on every fiber. The last term is therefore a globally generated
vector bundle of rank `r`, with

    deg W_(r+k) = epsilon(k+1).                     (4)

After extending the ground field to an algebraic closure, write

    W_(r+k) = direct_sum_i O(d_i).

Global generation implies `d_i>=0`, and (4) implies

    max_i d_i <= epsilon(k+1).

Twisting by the first degree in (2) bounds every splitting degree by

    epsilon-lambda k+epsilon(k+1)
      = 2 epsilon-k(lambda-epsilon)
      <= 3 epsilon-lambda < 0.                     (5)

Thus

    H0(Z,L_k)=0                     for every k>=1. (6)

Nothing in (3)--(6) uses smoothness, irreducibility, separability, or
reducedness of `Z`. The condition (1) is sufficient; no necessity or
sharpness claim is made.

For `(r,epsilon,lambda)=(2,2,7)`, (4) gives rank two and degree
`2k+2`. The upper bound (5) is `4-5k`, as proposed.

## 3. The H1 rank formula is correct, including boundary values

The divisor sequence for (2) is

    0 -> O_E(-lambda k,k)
      --f--> O_E(epsilon-lambda k,r+k)
      -> O_Z(epsilon-lambda k,r+k) -> 0.            (7)

The two sheaves on `E` have zero `H0` and `H2`. For `H2`, use the
nonnegative fiber degrees `k` and `r+k`; for `H0`, use (1).
The long exact sequence and (6) consequently give

    0 -> H1 O_E(-lambda k,k)
      --f--> H1 O_E(epsilon-lambda k,r+k)
      -> H1(Z,L_k) -> 0.                           (8)

The source and target dimensions are respectively

    a_k=(lambda k-1)(k+1),
    b_k=(lambda k-epsilon-1)(r+k+1).

These formulas also apply when a first factor is zero, for example
`epsilon=0,lambda=1,k=1`. Therefore

    h_k = b_k-a_k
        = k(r lambda-epsilon)-(r epsilon+r+epsilon). (9)

For the fixed quartic data this is

    h_k=12k-8.

This obtains both the stated rank and the injectivity required for
the quotient construction. It does not infer injectivity from a
generic rank computation.

## 4. Universal coefficient twists and arbitrary base change

Let `q:mathcal Z -> U` be the universal root family, and write
`H=O_U(1)`. The universal equation cuts out a divisor with ideal

    I_mathcal Z=O_E(-epsilon,-r) boxtimes H^-1.

Consequently its relative normal bundle is

    N_(mathcal Z/(E x U))=O_mathcal Z(epsilon,r) tensor q^*H.

The actual relative obstruction sheaf is therefore

    mathcal L_k
      =O_mathcal Z(epsilon-lambda k,r+k) tensor q^*H. (10)

The factor `H` is essential globally on projective coefficient space.
One can omit it only on a chart where the equation has been normalized
and `H` trivialized.

Applying the universal version of (7), with (10), gives the finite
presentation

    0 -> H1 O_E(-lambda k,k) tensor O_U
      --f--> H1 O_E(epsilon-lambda k,r+k) tensor H
      -> V_k -> 0,                                 (11)

where `V_k=R1 q_*mathcal L_k`. Equivalently, one may put

    Q_k=coker[a_k O_U(-1) --f--> b_k O_U],
    V_k=Q_k tensor H.

For every geometric point of `U`, the first map in (11) is injective
by (6)--(8). Some maximal minor is therefore a unit locally near each
point, and the map is locally a split inclusion of vector bundles.
Its cokernel is locally free of rank (9), and (11) remains exact after
every base change, including nonflat maps from nonreduced schemes.
The constant source and target cohomology in (7) can be computed by
their usual finite Cech presentations. Since (11) is locally split,
the same presentations after tensoring show universally that

    q_*mathcal L_k=0,
    R1 q_*mathcal L_k=V_k,

and formation of these sheaves commutes with arbitrary base change.
This avoids relying on a false general principle that constant fiber
dimensions by themselves always suffice over a nonreduced base.

## 5. What the cohomology permits in the deformation argument

For clarity, a direct local check of the relevant equation gauges is
as follows. Let `A' -> A` be one ambient square-zero step with kernel
`M=J^k`, and let `(h)` be an already lifted Cartier ideal. Any local
lift `h'` is a nonzerodivisor: `h` is regular in `A`, and the initial
equation `f` is regular on `M`, which is an invertible sheaf on `E`.
Two generator lifts differ by an element of `M`; changing generators
by a unit changes this difference by `fM`. Thus the sheaf of ideal
lifts has differences

    Hom(I_Z/I_Z^2,M/fM)=N_(Z/E) tensor J^k|Z.

Moreover, `A'/(h')` sits in an exact sequence with outer terms
`M/fM` and `A/(h)`. Both are flat over the parameter base, so the
lift remains a relative effective Cartier divisor. This check
retains equation units and works over nilpotent parameter bases.
For the general base-change property of relative effective Cartier
divisors, compare [Stacks Project, Section 31.19](https://stacks.math.columbia.edu/tag/056P).

Given the standard resulting lifting-torsor construction, (11) makes
its obstruction a section of `V_k` on the preceding lifting locus.
Its zero scheme is closed, and (6) gives uniqueness of the resulting
embedded ideal lift over every parameter base. This is exactly the
cohomological package needed for the separate conceptual review; it
does not identify local generator choices as canonical equations.

## 6. Finite determinacy and the relation-gap consequence: scope

If the relative lifting construction produces closed subschemes

    U=K_0 superset K_1 superset K_2 superset ...,

with `K_k` representing Cartier lifting into `V(I_E^(k+1))`, their
ideal sheaves form an ascending chain of coherent ideals on the
Noetherian scheme `U`. Hence the chain is eventually constant
scheme-theoretically; see
[Stacks Project, Lemma 30.10.1](https://stacks.math.columbia.edu/tag/01Y8).
The present cohomology argument supplies the missing all-order
uniqueness and coefficient-bundle input, but does not alone replace
the representability argument.

The resulting cutoff `N` is existential. It depends on the fixed
ambient formal neighborhood and the fixed `(r,epsilon)` family.
Neither the numerical inequality (1) nor Noetherianity gives a
numerical bound for `N`. One equality `K_n=K_(n+1)` is insufficient
to certify that every later locus is equal.

Under the accepted actual-CI bridge hypotheses, a pair whose full
generic initial relation degrees are `(r,s)` gives a Cartier lifting
of the root into `V(I_E^(s-r))`. It therefore lies in `K_k` for

    k < s-r.

Consequently, once an eventual stabilization index `N` exists,

    s > r+N

forces this root into `K_N`, the formal lifting locus. In the
quadratic case this is precisely `s>2+N`.

This last implication retains every hypothesis of the actual-CI
bridge, including actual smoothness of the root divisor where that
bridge requires it. Allowing nonreduced roots in the cohomology and
universal tower does not extend that bridge to nonreduced roots.
There is no algebraization claim, no asserted value of `N`, no proof
that the stabilized locus is empty, and no unrestricted STCI
conclusion. No commit or memory update was made.


---

## 2026-10-15-generalization-inseparable-root-blowup-bridge

# The actual-CI blowup bridge does not require separable root fields

Date: 2026-10-15. Author: `formal_algebraization_route`.
Status: **ARBITRARY-CHARACTERISTIC BRIDGE; independent review passed** in
the [full new-scope audit](UNIFORM_ROOT_TOWERS_AND_INSEPARABLE_BRIDGES.md#2026-10-15-generalization-inseparable-root-blowup-bridge-independent-audit),
with a separate [generic local-algebra review](UNIFORM_ROOT_TOWERS_AND_INSEPARABLE_BRIDGES.md#2026-10-15-generalization-inseparable-root-blowup-local-algebra-review).
The accepted characteristic-zero bridge is a premise. This note proves
the new extension to arbitrary characteristic by replacing its single
root-splitting step with uncompleted local algebra over `K=k(C)`.
No accepted certificate, computation, or characteristic-zero proof was
replayed.

## 1. Literal hypotheses and conclusion

Let `k` be an algebraically closed field of any characteristic, `X` a
smooth threefold, and `C subset X` a smooth connected curve. Let the
actual complete intersection `Y=(F,G)` have reduced support exactly `C`.
Retain the literal hypotheses of the
[accepted actual-CI/root bridge](QUADRATIC_ROOT_AND_BLOWUP_INCIDENCE.md#2026-10-14-generalization-blowup-root-curve-primitive-bridge):

1. The first ordinary normal relation has degree `r`, and its actual
   relation sheaf is a saturated line subbundle of `Sym^r N_C^*`.
2. Both chosen actual equations have generic normal order `r`. Their
   degree-`r` symbols jointly generate that line at every point of `C`.
   Their two coefficient sections have no common zero.
3. The **entire** generic ordinary initial ideal is the binary complete
   intersection `(f_r,g_s)`, with `s>r` and the two forms coprime. Put
   `ell=s-r` and assume `ell>=2`.
4. On `B=Bl_C X`, the actual Cartier root divisor `Z=(f_r)` in the
   exceptional divisor `E` is smooth. Smoothness of the reduced support
   of a nonreduced root is insufficient.

Then the actual strict intersection `Y'=D_F intersect D_G` has support
exactly `Z`, no vertical exceptional-fiber component, and the exact
uncompleted local form

    I_(Y',p)=(h,u^ell)                                  (1)

at every point `p in Z`, with `S=(h)` a smooth surface and `u` an
exceptional equation cutting out `Z` as a reduced Cartier divisor on
`S`. Consequently `Y'` is an embedded primitive `ell`-fold structure
on the full smooth `Z`, with surviving conormal `O_Z(-E)`.

The conormal extension for `Z subset E subset B` splits. The actual
first obstruction therefore vanishes. Moreover `Y'` gives a compatible
embedded Cartier lift of `Z` on `V(I_E^ell)` and hence at every stage

    E_m=V(I_E^(m+1)),       m<ell.                      (2)

No separability of `Z->C`, tame ramification, or invertibility of `r`,
`s`, or `ell` in the field is assumed.

## 2. The generic standard basis exists before completion

Set `A=O_(X,eta_C)`, a two-dimensional regular local ring, with maximal
ideal `m=I_C A` and residue field `K=k(C)`. Its associated graded ring
is `K[x,y]`. Put `I=(F,G)A`. It is an `m`-primary complete intersection.

Choose one original generator `P` whose degree-`r` symbol is nonzero;
multiply it by a unit of `A` if necessary, so that its symbol is `f_r`.
Choose `H in I` with initial form `g_s`. Such a lift exists by the
definition of the degree-`s` part of the full initial ideal. Put
`J=(P,H)`. Then

    J subset I,
    (f_r,g_s) subset in_m(J) subset in_m(I)=(f_r,g_s).

Thus the two initial ideals agree. Successive order reduction says that
every element of `I` lies in `J+m^n` for every `n`. Krull intersection
in the finite module `A/J` gives

    I=(P,H)                                              (3)

in the actual local ring `A`. Equivalently, the homogeneous regular
sequence gives the same finite colength for the two ideals. No
completion, coefficient field, geometric root splitting, or division by
the characteristic is used.

Both generating pairs `(F,G)` and `(P,H)` minimally generate the
height-two complete intersection `I`. Their coefficient change matrix
is therefore in `GL_2(A)`; this follows by reducing its generating map
modulo `m` and applying Nakayama.

On the ordinary blowup of `Spec A` at `m`, divide **both** members of
either pair by `u^r`. The invertible change matrix remains invertible,
so it preserves the actual ideal of the strict intersection:

    (F/u^r,G/u^r)=(P/u^r,H/u^r).                        (4)

The second entry on the right is `u^(s-r)*(H/u^s)`. Replacing that entry
by `H/u^s` would instead saturate away the multiplicity and is not
permitted. The proof uses (4), with the common exponent `r`, throughout.
The object is the intersection of the two original strict divisors,
not the strict transform of the supported intersection `Y`. Saturating
the eventual ideal `(p,u^ell)` by `u` would give the unit ideal and
destroy this object entirely; no such saturation is performed.

## 3. The generic root prime may be inseparable

Let `xi` be the generic point of a component of `Z`. Every component is
horizontal over `C`: a line subbundle gives a nonzero binary polynomial
on every exceptional fiber, so `Z->C` is finite of degree `r`.

Choose a blowup chart `x=u`, `y=uv` containing `xi`, and let

    T=O_(Bl_m Spec A,xi).

It is a regular local ring of dimension two, and

    T/(u)=K[v]_(q),
    K'=k(xi)=K[v]/(q),                                  (5)

where `q` is the irreducible polynomial of that generic root. The
actual smooth root divisor is reduced; consequently its generic fiber
is reduced and `q` occurs to exponent exactly one in `f_r(1,v)` as a
polynomial over `K`. It may have zero derivative and become a repeated
root after an inseparable extension. Neither circumstance changes
the exponent of its prime factor over `K` in (5).

Put `p=P/u^r` and `a=H/u^s`. Modulo `u`,

    p=f_r(1,v)=unit*q in K[v]_(q),
    a=g_s(1,v).

Coprimality makes the latter nonzero modulo `q`. Thus `a` is a full
unit in `T`, while `(u,p)` is its maximal ideal. Formula (4) becomes

    I_(Y',xi)=(p,u^ell) in T.                           (6)

The ring `T/(p)` is an uncompleted DVR with uniformizer `u`, so

    length_T T/(p,u^ell)=ell.                           (7)

This proves the generic transverse multiplicity on every component of
`Z` over its actual root field. It does not replace `K'` by an
algebraic closure, use `q'`, or count distinct geometric roots.

In particular no `K`-compatible identification with
`K'[[u]]/(u^ell)` is asserted. For inseparable residue extensions a
deformed root equation need not admit such a compatible coefficient
field. The exact local ideal (6) and length (7) are the needed facts.

A single family illustrates this distinction without a root-case
enumeration. In characteristic `p>0`, take `C=(x,y)` in affine
`(t,x,y)`-space and

    F=y^p-t*x^p+x^(p+1),
    G=F+x^(p+ell),       ell>=2.

Its full generic initial ideal has the coprime generators
`y^p-t*x^p,x^(p+ell)`, with `r=p` and `s=p+ell`. On the `x=u,y=uv`
chart the actual strict ideal is

    (v^p-t+u,u^ell).

The root `v^p=t` is a smooth total-space divisor, purely inseparable
over the `t`-line, and the displayed ideal is exactly the claimed
primitive `ell`-fold. In the containing DVR the relation is
`t=v^p+u`. A `K`-compatible coefficient field containing a root of
`a^p=t` would require `(a-v)^p=u`, impossible because its `u`-valuation
would be `1/p`. The same obstruction survives modulo `u^ell`: the
linear `u` term cannot be canceled by a `p`-th power of an element in
`(u)`. Thus the stronger split `K`-algebra claim genuinely fails even
though the local ideal and transverse length theorem hold.

## 4. Actual support and every closed point are retained

The characteristic-free support argument uses the original strict
equations. Their restrictions to `E` are `a f_r,b f_r`, and the actual
coefficient pair `a,b` has no common zero. Their common zero set on
`E` is exactly `Z`. Off `E`, the blowup is an isomorphism and the
original pair has no common point off `C`. Hence

    Supp(Y')=Z.

No entire exceptional fiber is a component. In particular no vertical
component has been removed by saturation. Neither strict divisor
contains `E`; a shared surface component off `E` would contradict
the original complete intersection. Thus their height-two intersection
in the smooth threefold is Cohen--Macaulay and has no discarded embedded
or isolated component.

Fix a closed point `z in Z`. One original strict equation `h` has a
leading coefficient which is a unit there. Its restriction to `E`
cuts out the actual smooth divisor `Z`. The **full** differential on
`E`, including base directions, is nonzero. Therefore `(h,u)` cuts
out the smooth curve `Z` in the smooth threefold: `S=(h)` is smooth
at `z`, transverse to `E`, and `u` cuts out `Z` as a reduced Cartier
divisor on `S`.

Restrict the other strict equation `h_2` to the regular local surface
ring `O_(S,z)`. It is nonzero, and its zero set is precisely `(u)`.
This ring is a UFD and `(u)` is prime, so

    h_2|S=epsilon*u^b,       epsilon a unit.

Its order at the generic point of this component is (7), hence `b=ell`.
Lifting the unit gives exactly (1), before completion. This also covers
smooth points at which the root projection is purely inseparable.
For example `v^p-t` has vanishing fiber derivative but nonzero full
differential `-dt`; the latter is what this proof uses.

## 5. Conormal splitting and compatible actual lifts

Locally (1) with `ell>=2` shows that the first normal symbols of the
two equations span precisely the conormal line generated by `h`.
Its projection to `O_Z(-Z_E)` is an isomorphism, since `h|E` generates
the ideal of `Z` in `E`. These local image lines are the image of the
global two-equation symbol map and therefore glue. They split

    0 -> O_Z(-E) -> N_(Z/B)^* -> O_Z(-Z_E) -> 0.

The actual quotient line, hence the first ordinary normal layer of
`Y'`, is `O_Z(-E)`; no torsion layer is discarded. The cotangent
extension description of the first embedded root-divisor obstruction
is characteristic free and uses the full differential. Thus the
splitting gives `kappa(df_r)=0` in the actual obstruction group.
This is the geometric class in the chosen characteristic. No
characteristic-zero chart representative involving rational denominators
is transferred to an exceptional characteristic.

Formula (1) also gives `I_E^ell subset I_(Y')`. On `V(I_E^ell)`, the
quotient ideal is generated by `h`, which is a nonzerodivisor since
`(h,u)` is a regular sequence. It is therefore an actual invertible
embedded ideal extending `I_(Z/E)`. This proves (2), with all equation
units and all points retained.

## 6. Consequence for the characteristic-free smooth-root cutoff

The [characteristic-scope addendum](FINITE_ROOT_FAMILIES_AND_SMOOTH_OBSTRUCTIONS.md#2026-10-15-generalization-smooth-root-characteristic-scope-addendum)
already proves the formal smooth movement-two nonexistence theorem
and its finite empty smooth-root stage in every characteristic under
the explicit normal-bundle hypothesis. The present new proof supplies
the missing actual-CI bridge in that characteristic as well, under
the literal hypotheses in Section 1.

For a fixed balanced smooth rational embedding of degree `e>=4` and a
fixed first normal order `r`, let its empty smooth-root stage be `K_N`.
The actual gap `ell=s-r` supplies the stage `K_(ell-1)` by (2). Thus

    s-r<=N, equivalently s<=r+N.                        (8)

Equality only supplies stage `N-1` and is not excluded. The cutoff
is existential, depends on the actual embedding and `r`, and excludes
no finite-gap pair merely because it is finite. No normal-bundle
splitting in an exceptional characteristic is inferred for `C0`.

The proof does not cover a nonreduced actual root, first-relation
defects, joint leading base points, a noncoprime next initial relation,
or the absence of the full ordinary initial complete-intersection
hypothesis. Those are substantive retained boundaries. The universal
STCI and unrestricted `C0` problems remain open.


---

## 2026-10-15-generalization-inseparable-root-blowup-bridge-independent-audit

# Independent audit of the inseparable-root actual-CI bridge

Date: 2026-10-15. Reviewer: `new_logarithmic_review`.

Status: **PASS for the new arbitrary-characteristic actual-CI bridge,
under all literal hypotheses.** The proposed repair correctly replaces
the separable-root elimination argument with uncompleted local algebra
at the actual root prime. It proves the full global primitive structure,
the conormal splitting, actual Cartier lifts through the claimed stages,
and the conditional finite-gap consequence in arbitrary characteristic.

Reviewed source:
[inseparable-root blowup bridge](UNIFORM_ROOT_TOWERS_AND_INSEPARABLE_BRIDGES.md#2026-10-15-generalization-inseparable-root-blowup-bridge).
The accepted characteristic-zero bridge and the
[characteristic-free formal/tower addendum](FINITE_ROOT_FAMILIES_AND_SMOOTH_OBSTRUCTIONS.md#2026-10-15-generalization-smooth-root-characteristic-scope-addendum)
are premises. The separate
[generic local-algebra review](UNIFORM_ROOT_TOWERS_AND_INSEPARABLE_BRIDGES.md#2026-10-15-generalization-inseparable-root-blowup-local-algebra-review)
passes the standard-basis and root-prime steps. This full new-scope
audit checks their use in the global extension, the new wild family,
and the obstruction/lift consequences. No accepted computation,
characteristic-zero proof, CAS calculation, or verifier was replayed.

## 1. The scope that must survive the extension

Let k be algebraically closed of any characteristic, X a smooth
threefold, and C a smooth connected curve. The actual complete
intersection Y=(F,G) has reduced support exactly C. The statement uses
all of the following:

- The actual first degree-r relation sheaf is a saturated line
  subbundle of Sym^r N_C^*.
- Both chosen actual equations have generic normal order r, and their
  degree-r coefficient sections generate this line at every point.
- The **full** generic ordinary initial ideal is the coprime binary
  complete intersection (f_r,g_s), with s>r and ell=s-r>=2.
- The actual Cartier divisor Z=(f_r) on E is smooth, including its
  scheme structure, not just its reduced support.

These hypotheses are stronger than a claim about two selected initial
forms. Joint leading base points, defective relation sheaves, vertical
fiber components, nonreduced roots, and noncoprime next relations have
not been removed by saturation or admitted by the new characteristic
scope. Components of the smooth Z can be handled separately.

## 2. The new generic replacement uses the actual local ideal

At eta_C, A=O_(X,eta_C) is a regular local ring of dimension two,
with maximal ideal m and residue field K=k(C). Its associated graded
ring is K[x,y]. The proposed choice P,H in I=(F,G)A is legitimate:
P is an original generator normalized by a lifted unit, and g_s in
the degree-s component of the full initial ideal is the symbol of an
actual H in I intersect m^s.

For J=(P,H), the inclusions of initial ideals force
in_m(J)=in_m(I). For each fixed n, repeated finite order reduction
puts every element of I into J+m^n. Krull intersection in the finite
module A/J then gives I=J in the uncompleted ring. There is no claim
that an infinite division series converges in A. Both pairs minimally
generate the height-two ideal, so their change matrix lies in GL_2(A).

Its pullback remains invertible on the localized blowup. Both original
strict equations were divided by u^r, and the valid transformed ideal
is therefore

    (F/u^r,G/u^r)=(P/u^r,H/u^r)
                  =(P/u^r,u^ell*(H/u^s)).               (A)

This keeps the second exceptional factor. Dividing the new H by u^s
instead would change the object. The proof correctly studies the
intersection of the original two strict divisors, rather than a
saturation or the strict transform of the supported intersection Y.

At a generic root prime xi, use either blowup chart as needed, so no
root at infinity is lost. On x=u,y=uv the regular local ring T has

    T/(u)=K[v]_(q), residue field K'=K[v]/(q),

where q is irreducible over the actual K. Reducedness of Z is retained
under localization to K. Thus q has exponent one in f_r(1,v) over K,
even when q'=0 and K'/K is inseparable. For p=P/u^r, reduction gives
p=unit*q modulo u, so the maximal ideal of T is (u,p).
Coprimality makes H/u^s a unit at xi. Consequently (A) is exactly

    I_(Y',xi)=(p,u^ell).

The ring T/(p) is a regular local ring of dimension one, with uniformizer
u. Hence the length is ell. This is length at the actual prime with
residue field K', not a count of geometric roots or an assertion of
a K-compatible truncated coefficient-field model.

## 3. The actual global hypotheses give the local form everywhere

On E, the two original strict equations restrict to a f_r,b f_r.
The actual coefficient pair has no common zero, so this common zero
scheme is exactly Z. Off E the blowup is an isomorphism and Y has no
point away from C. Therefore Supp(Y')=Z. In particular no vertical
exceptional fiber is a component. The two strict divisors have no
common surface component; their intersection in the smooth threefold
is height two and Cohen--Macaulay, with no additional embedded or
isolated support. These conclusions use the original global equations,
not merely the generic generator change.

At every closed z in Z, choose an original strict equation h with unit
leading coefficient. Its restriction to E defines the actual smooth
Z. The full differential on E is nonzero; thus dh and du are
independent ambient cotangent vectors. This proves that S=(h) is
smooth and meets E transversely along Z, in any characteristic.
The differential in the base direction is retained when the fiber
derivative vanishes.

In the regular local surface ring R=O_(S,z), u is prime because
R/(u)=O_(Z,z) is a domain. The other strict equation has a nonzero
restriction h_2 with radical (u), by the support assertion. Unique
factorization in R gives h_2=epsilon*u^b, with epsilon a unit.
Localization at the generic point of the component identifies b
with the generic length ell already established. Lifting the unit
to the ambient local ring proves the exact uncompleted local ideal

    I_(Y',z)=(h,u^ell)                                  (B)

at every point. Neither geometric root splitting nor a coefficient
field is needed. The new inseparable generic calculation is therefore
sufficient to carry the global primitive structure across all closed
points, including purely inseparable projection points.

## 4. Conormal splitting and actual lifts are intrinsic

Let J=I_(Z/B). Since ell>=2, the image of I_Y' in J/J^2 is locally
the line generated by [h]; u^ell maps to zero. These lines glue as
the image of the global ideal map. Projection to N_(Z/E)^* is an
isomorphism on this line because h|E generates I_(Z/E). Thus they
split the actual sequence

    0 -> O_Z(-E) -> N_(Z/B)^* -> N_(Z/E)^* -> 0.

The quotient J/(J^2+I_Y') is exactly O_Z(-E), with no suppressed
point torsion. This gives the stated surviving ordinary conormal.
The full differential embedding N_(Z/E)^*->Omega_E|Z exists because
Z and E are smooth over k. Pulling back the ambient cotangent
extension gives this conormal sequence in every characteristic.
Its splitting therefore gives vanishing of the actual first
embedded-divisor obstruction. It does not transfer any
characteristic-zero formula or rational-denominator representative.

Equation (B) also gives I_E^ell subset I_Y' globally. On
V(I_E^ell), its quotient ideal is locally generated by h and is
invertible and embedded. For precision, the regular sequence is
(u,h); h is a nonzerodivisor modulo each u^n, since the successive
u-adic layers reduce this assertion to regularity modulo u. Thus
restriction preserves embedded Cartier ideals for every n<=ell.
Their equations and units glue because the ideal is the intrinsic
quotient of I_Y'. With E_m=V(I_E^(m+1)), the range supplied is

    m<ell.                                              (C)

No lift at the next stage is asserted. The condition ell>=2 is
substantive for the splitting and first-obstruction statement.

## 5. The wild family and the coefficient-field warning both pass

In characteristic p>0, put C=(x,y) in A3_(t,x,y), and choose

    F=y^p-t*x^p+x^(p+1),
    G=F+x^(p+ell), ell>=2.

The ideal is (F,x^(p+ell)), with radical (x,y), so it is an actual
height-two complete intersection supported exactly on C. Both chosen
equations have generic normal order p, and their leading coefficients
in the line generated by y^p-t*x^p are 1. That line is saturated:
the y^p coefficient is a unit at every base point.

For completeness, the claim about the **full** generic initial ideal
has an exact hand proof. Over K=k(t), the actual quotient by
x^(p+ell) is free of rank p over K[x]/(x^(p+ell)), because F is monic
of y-degree p. Its K-length is p*(p+ell). The coprime homogeneous
complete intersection (y^p-t*x^p,x^(p+ell)) has that same colength
and is contained in the actual initial ideal. Equality of these
finite colengths proves equality of the full initial ideals.

The root lies entirely in the x-chart and is v^p=t. It is smooth
as a total divisor, with full differential -dt, while its projection
is purely inseparable. Direct common division by u^p gives

    I_Y'=(v^p-t+u,u^ell).

This is a family satisfying the new bridge hypotheses, with exactly
the asserted primitive structure.

The containing generic DVR has u=t-v^p and residue field K'. If a
K-compatible embedding of K' existed, its element a with a^p=t
would satisfy (a-v)^p=u. That is impossible in a DVR, since its
valuation would require v_u(a-v)=1/p. Modulo u^ell the same failure
is already visible in the first layer: reduction forces a-v in (u),
so its p-th power lies in (u^p) subset (u^2), whereas u does not.
This works for every ell>=2, including ell<p.

The warning is specifically about compatibility with the original
K=k(t) embedding. Coefficient fields as k-fields are not excluded;
the natural k(v) coefficient field has t=v^p+u under the original
K-map. The example does not contradict Cohen coefficient fields.
Its base curve is affine, and it is not an example of an infinite
projective movement-two formal root excluded by the accepted theorem.

## 6. Consequence and acceptance boundary

Under the accepted characteristic-free smooth-root formal theorem and
tower, fix a balanced smooth rational embedding in P3 of degree e>=4
and a first normal order r. If K_N is its empty smooth-root stage,
the newly extended actual bridge supplies K_(ell-1) by (C).
Consequently

    ell=s-r<=N, equivalently s<=r+N.

At equality the actual pair supplies only stage N-1; that equality
is not excluded. Thus the positive-characteristic conditional
qualification in the earlier characteristic addendum is now met
for the literal actual-CI lane in Section 1. The bound remains
existential and does not exclude pairs introducing the second
relation before the empty stage.

This audit accepts the arbitrary-characteristic extension of that
lane, including the inseparable-root replacement and the field-model
failure shield. It does not infer a balanced normal bundle for the
literal C0 in an exceptional characteristic, cover defective or
nonreduced roots, or remove the full generic initial-ideal hypothesis.
No universal STCI or unrestricted C0 conclusion is drawn.

No commit, memory write, accepted verifier replay, or CAS computation
was performed.


---

## 2026-10-15-generalization-inseparable-root-blowup-local-algebra-review

# Local-algebra review of the inseparable-root blowup repair

Date: 2026-10-15. Reviewer: `inseparable_blowup_bridge`.
Status: **PASS for the new generic standard-basis, actual divided-ideal,
and root-prime length arguments in Sections 2--3 of the owner note.**
This is a focused written review of the new characteristic extension;
it does not reaudit the accepted characteristic-zero bridge, replay a
certificate, or certify the separate formal nonexistence theorem.

Reviewed source:
[the inseparable-root bridge owner note](UNIFORM_ROOT_TOWERS_AND_INSEPARABLE_BRIDGES.md#2026-10-15-generalization-inseparable-root-blowup-bridge).

## 1. The generator change is valid in the uncompleted ring

Use the owner's notation

    A=O_(X,eta_C), m=I_C A, K=A/m, I=(F,G)A.

The ring `A` is regular local of dimension two, and `I` is `m`-primary.
The full initial ideal hypothesis is

    in_m(I)=(f_r,g_s) in gr_m(A)=K[x,y].

Choose an original equation `P` with degree-`r` initial form `f_r`,
up to multiplication by a lifted unit. The element `g_s` belongs to
the degree-`s` part of the initial ideal, which is the image of
`I intersect m^s` in `m^s/m^(s+1)`. Thus an actual element `H in I`
with initial form exactly `g_s` exists. It is not merely a formal
lift after completion.

For `J=(P,H)`, the inclusions

    (f_r,g_s) subset in_m(J) subset in_m(I)=(f_r,g_s)

give equality. Cancellation of the initial form of any element of
`I` raises its order using coefficients lifted from `gr_m(A)`. After
finitely many cancellations, that element lies in `J+m^n`, for each
fixed `n`. Consequently

    I/J subset intersection_n m^n(A/J)=0

by Krull intersection in the finite `A`-module `A/J`. This proves
`I=(P,H)` before completion. In particular there is no convergence
assumption on an infinite division process.

Both pairs `(F,G)` and `(P,H)` minimally generate the same height-two
ideal: one generator would violate the principal ideal theorem.
If `(P,H)^t=M(F,G)^t`, reduction on the two-dimensional space
`I/mI` makes `M mod m` invertible. Therefore `det M` is an actual
unit of `A`, so `M in GL_2(A)`. This is the unit condition needed on
the blowup; equality of abstract initial ideals alone is not being
used as an unsupported change of strict-transform equations.

## 2. The common division exponent retains the actual intersection

Blowup commutes with localization at `eta_C`. On a chart of
`Bl_m Spec A` with exceptional equation `u`, the pullback of `M`
remains invertible. Both original equations have order `r`, so the
intersection of their individual strict-transform divisors has ideal

    (F/u^r,G/u^r)=(P/u^r,H/u^r)
                  =(P/u^r,u^(s-r)*(H/u^s)).

All quotients displayed here are regular functions on the chosen
chart, since `m O_B=(u)`. The retained factor `u^(s-r)` is essential.
The second equation after the generator change is the divided
equation `H/u^r`; it is not the individual strict transform `H/u^s`.

This target is the **intersection of the strict transforms of the
original two divisors**. It is not the strict transform of the
supported intersection `Y` itself: `Y` has empty restriction away
from the center, so its strict transform defined by closure from
that open set is empty. In particular, saturating the divided ideal
by `u` would destroy the supported strict intersection. No such
saturation occurs in the owner argument.

## 3. The generic local length needs a reduced prime, not separability

Let `xi` be the generic point of a component of the actual smooth
root divisor. All these components dominate `C`: the actual
line-subbundle hypothesis prevents the binary root form from
vanishing on an entire exceptional fiber. On a chart `x=u,y=uv`,
the ring

    T=O_(Bl_m Spec A,xi)

is regular local of dimension two, with

    T/(u)=K[v]_(q),
    T/m_T=K'=K[v]/(q).

Here `q` is the irreducible polynomial defining the actual root
prime. Reducedness of the actual root divisor implies reducedness
after localization to the generic point of `C`. Thus the prime
factor `q` occurs to exponent one in `f_r(1,v)` over `K`. This
statement does not assert that `q` has a nonzero derivative or
distinct roots after algebraic closure. It remains valid when
`K'/K` is inseparable.

Set `p=P/u^r` and `a=H/u^s`. The reduction of `p` modulo `u`
is a unit times `q` in the DVR `K[v]_(q)`. Therefore

    m_T=(u,p).

Coprimality of `f_r` and `g_s` says that `a mod m_T` is nonzero
in the actual field `K'`; hence `a` is an actual unit in `T`.
With `ell=s-r`, the unsaturated divided ideal is exactly

    (p,u^ell*a)=(p,u^ell).

Because `(u,p)` is a regular system of parameters of `T`, the
uncompleted local ring `T/(p)` is a DVR with uniformizer `u`.
The successive quotients of its `u`-adic filtration through
`u^ell` are the field `K'`. It follows that

    length_T T/(p,u^ell)=ell.

This is length over the actual root prime, whose residue field is
`K'`. It is not a count of geometric roots. No separable extension,
fiber derivative, or compatible coefficient-field embedding is
needed. The owner's explicit refusal to assert a `K`-compatible
isomorphism with `K'[[u]]/(u^ell)` is necessary: an inseparable
root deformation need not admit that extra structure.

## 4. Scope of this review and the retained support boundary

The new generic calculation is valid in every characteristic.
Its root-prime length step needs only reducedness of the generic
root divisor. The separate extension to every closed point uses
the literal smoothness of the whole actual root divisor and its
full differential on the exceptional surface, as stated by the
owner. The calculation above supplies its generic exponent
without an additional separability hypothesis.

The generic generator change does not prove absence of vertical
components by itself. That conclusion continues to use the
original global hypotheses: the actual degree-`r` relation is a
line subbundle, and the actual leading coefficient pair has no
common zero. The restrictions of the original strict equations
are then `a f_r,b f_r`; their common zero scheme on `E` is the
actual root divisor. No defective point or vertical exceptional
fiber is discarded in passing to the generic local calculation.

There is no new gap in Sections 2--3 under the stated hypotheses.
This review does not promote the independent global scope audit
or a new canonical acceptance record on its own.
