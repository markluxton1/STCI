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
[torsion/second-zero argument](2026-10-15-generalization-quadratic-root-torsion-second-zero-geometry.md)
bounds the support of the second zero locus, and hence of the stable
formal locus, by dimension two. Other components are retained.

The spectral Picard descent condition is a separate requirement on a
later second quotient relation. Formal first-principal compatibility
neither supplies that second relation nor constructs two projective
equations with the required support. The universal STCI problem and
unrestricted `C0` remain open. No commit or memory update was made.

Independent reviews of the new theorem are recorded in
[the all-order cohomology audit](2026-10-15-generalization-uniform-root-tower-cohomology-independent-audit.md)
and [the relative functor/noetherian audit](2026-10-15-generalization-uniform-root-tower-functor-independent-audit.md).
The latter includes arbitrary nonreduced parameter bases, equation units,
scheme-theoretic stabilization, and the regular locally principal formal
inverse limit. Neither review asserts algebraization.
