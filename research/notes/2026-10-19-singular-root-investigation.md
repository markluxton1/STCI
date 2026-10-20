# Reduced movement-two roots: the remaining formal surface must be singular

Date: 2026-10-19. Author: `singular_roots` research agent.

Status: **new conditional theorem proposal with independent review PASS; not promoted**.
The separate audits are
[the smoothing audit](2026-10-19-regular-singular-root-smoothing-audit.md) and
[the equal-slope two-component audit](2026-10-19-regular-reducible-root-independent-audit.md).
This note does not promote a canonical result, alter an accepted theorem, or
settle the singular-formal-surface case.

## 1. Exact scope and accepted premises

Let `k` be algebraically closed of characteristic zero. Work with the fixed
rational quartic `C0` in `P3`, its blowup `B=Bl_C0(P3)`, and exceptional
divisor `E=P1_base x P1_direction`. Write `p:E->P1_base`, and use the
repository conventions

    O_E(E)=O_E(7,-1),       H|E=O_E(4,0).

An embedded all-orders Cartier lift of a full root `Z subset E` means
compatible effective Cartier divisors on every exceptional neighborhood,
as in the source underlying
[STCI-R-0005](../results/smooth_root_formal_obstruction.md). Its inverse
limit is a formal effective Cartier surface `Vhat` in the completion of
`B` along `E`, with scheme-theoretic intersection `Vhat cap E=Z`.

The accepted scope distinctions remain premises:

- STCI-R-0005 excludes smooth full roots of class `(2,r)`, `r>=2`.
- [STCI-R-0011](../results/moving_nonreduced_spectral_root_obstruction.md)
  makes a spectral-descent survivor reduced. In movement two it is
  integral `(2,r)`, or two distinct smooth `(1,r/2)` components when `r`
  is even.
- [STCI-R-0010](../results/saturated_first_relation_normal_flatness.md)
  supplies spectral uniformity for actual lci thickenings only under its
  full generic binary-CI and saturated-first-relation hypotheses.
- [STCI-R-0006](../results/actual_ci_smooth_root_bridge.md) is an actual
  finite-gap bridge with a **smooth full root**; no singular-root version
  is assumed in this note.

The proposed theorem below concerns the actual ambient formal lifting
problem. It assumes no spectral Picard descent and supplies no automatic
bridge from arbitrary actual STCI equations.

## 2. Proposed theorem

**Theorem A.** Let `Z` be a reduced effective Cartier divisor of class
`(2,r)`, `r>=2`, finite flat over `P1_base`. There is no embedded
all-orders Cartier lift whose formal surface `Vhat` is regular along
the whole of `Z`.

Here regularity is a condition on the **lifted formal surface**, not on
the possibly singular curve `Z`. For a hypersurface in the completion of
the smooth threefold `B` over the perfect field `k`, the condition means
that its completed local surface rings at closed points of `Z` are
regular. This is the smooth-formal-surface condition used below.

Thus, if a reduced singular movement-two root has any all-orders
Cartier lift, every such lift has a singular surface point above
`Sing(Z)`. This narrows the surviving geometry, but does not exclude
these singular lifted surfaces.

The proof uses a smoothing **inside an algebraized smooth surface**.
It does not assert that singular roots can be smoothed in the original
exceptional root-lifting functor.

## 3. Algebraize using the singular root itself

Because `Z=Vhat cap E`, the exceptional parameter is a nonzerodivisor on
`Vhat`, and `Z` is an effective Cartier divisor in this regular formal
surface. Consequently

    N_(Z/Vhat)=O_Z(E)=O_Z(7,-1)=:N.                 (1)

The root `Z` is connected: the exact sequence on `E`

    0 -> O_E(-2,-r) -> O_E -> O_Z -> 0

and Kunneth give `H0(O_Z)=k`, since `r>=1` makes
`H1(O_E(-2,-r))=0`.

For every irreducible component `D` of `Z`, write its bidegree `(a,b)`.
Finiteness over the base gives `b>0`; effectiveness and total first
bidegree two give `0<=a<=2`. Therefore

    deg(N|D)=7b-a >=5>0.                           (2)

A line bundle on a proper curve is ample if its degree on every reduced
irreducible component is positive, so `N` is ample.

Bost's **Corollary 3.8**, rather than only his smooth-center Theorem 3.5,
applies here. It permits a proper connected locally complete intersection
scheme of definition, while requiring the formal scheme itself to be
smooth and its normal bundle ample. It algebraizes `Vhat` as a branch
of an integral algebraic surface `W subset B`. Source: J.-B. Bost,
[*Algebraic leaves of algebraic foliations over number fields*,
printed pp. 187--188](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf),
Theorem 3.5, Theorem 3.7, and Corollary 3.8. This is the geometric part of
the paper; no arithmetic hypothesis is imported.

Normalize `W`. The selected formal branch is regular, hence normal.
The normalization/completion argument used in the accepted smooth-root
proof therefore preserves the entire selected branch. That argument
uses normality of `Vhat`, not smoothness of the curve `Z` itself. Its
local maps to the finite normalization glue uniquely, and reduction
modulo the exceptional parameter embeds the same possibly singular
`Z` into the normalization. The selected completed local factors are
regular. Resolve the normalized algebraic surface outside this regular
neighborhood of `Z`. We obtain a smooth projective surface `T` containing
the same Cartier curve `Z`, with its original formal neighborhood.

This leaves the numerical data

    p_a(Z)=r-1,       Z^2=7r-2.                    (3)

Let `S` be the image of `W` in `P3`, `d=deg(S)`, and let `H` on `T` be
the pullback of the hyperplane class. The surface is not exceptional,
and the blowup is an isomorphism away from `E`; hence `T->S` is
birational, `H` is nef, and

    H^2=d>0,         H.Z=4r.                      (4)

Other algebraic branches of `W` and other components of `W cap E` are
retained. None is discarded by saturation.

## 4. The normal line is generated and unobstructed

The relevant vanishing does not need a classification of the singularities.
For `N=O_Z(7,-1)`, the two restriction sequences are

    0 -> O_E(5,-r-1) -> O_E(7,-1) -> N -> 0,
    0 -> O_E(4,-r-1) -> O_E(6,-1)
      -> N tensor p*O_P1(-1) -> 0.

Kunneth gives

    H1(Z,N)=0,
    H1(Z,N tensor p*O_P1(-1))=0.                  (5)

For example, the middle terms have zero `H1` because `O_P1(-1)` has no
cohomology; the left terms have zero `H2` because their first ruling
degree is nonnegative.

The finite flat map `p:Z->P1` makes `p_*N` a vector bundle. Projection
formula and (5) give `H1(P1,(p_*N)(-1))=0`. Splitting this vector bundle
on `P1` shows that every summand has nonnegative degree. Thus `p_*N` is
generated by its global sections. The finite-map evaluation
`p* p_*N -> N` is surjective, so **`N` is generated by global sections**.

These are calculations on the original full `Z`, not on its
normalization, and preserve gluing at singular points.

## 5. An embedded smoothing lemma and its application

**Lemma B.** Let `D` be a connected reduced effective Cartier divisor
on a smooth projective surface `T` over characteristic zero. If
`H1(D,N_(D/T))=0` and `N_(D/T)` is generated by global sections, then
`D` has a flat embedded deformation on `T` whose general fiber is a
smooth connected curve, numerically equivalent to `D`.

**Proof.** Embedded Cartier deformations have tangent space `H0(N)`
and obstruction space contained in `H1(N)`. Local deformations lift
because a local defining nonzerodivisor can be lifted. Hence the
Hilbert scheme of `T` is smooth at `[D]`. Work on a smooth irreducible
open neighborhood `U` of this point, shrinking to the relative
effective-Cartier locus of the universal family `D_U subset T x U`.

At a point `x` of the central curve, write a completed local equation
of the universal family as

    f(x_1,x_2) + sum_i t_i eta_i(x_1,x_2)
                  + terms of parameter order >=2.

The classes of `eta_i` span the evaluations of `H0(N)` in the normal
fiber at `x`. Global generation gives an index with `eta_i(x)!=0`.
The total universal family is therefore regular at `x`, since its
equation has a unit derivative in that parameter direction. The whole
central curve lies in this regular locus. Properness over `U` allows
shrinking `U` so that the entire total family is regular. Over the
perfect field `k` it is smooth over `k`.

Its components dominate `U` by flatness. Characteristic-zero generic
smoothness, followed by properness, supplies a nonempty open subset of
`U` over which the family has smooth fibers. Since `H0(O_D)=k`, upper
semicontinuity gives `h0(O_(D_u))=1` near the central point; these smooth
fibers are connected, hence integral. A connected flat family of
Cartier divisors gives algebraic, hence numerical, equivalence. QED.

The embedded deformation inputs can be checked in Hartshorne's
[author-hosted *Lectures on Deformation Theory*](https://math.berkeley.edu/~robin/math274root.pdf),
Theorem 2.4 (tangent space), Theorem 6.3 (the normal-sheaf gluing
obstruction, explicitly including lci schemes), and Theorem 9.3
(lifting a regular sequence). The elementary universal-family argument
above proves the particular smoothing consequence; no claim of
equisingular deformation versality is needed.

Apply Lemma B to the curve `Z subset T` from Section 3, using (5).
There is a smooth connected integral curve `Z_t subset T` with

    g(Z_t)=r-1,       Z_t^2=7r-2,       H.Z_t=4r.    (6)

The smoothing occurs on `T`; `Z_t` need not map into `E` or cover `C0`.
Only the numerical data (6) enter the next surface argument. The
original root `Z` remains on `T` and still lies over `C0`.

## 6. Opposing degree bounds

The smooth curve `Z_t` satisfies

    Z_t^2-(4g(Z_t)+5)=3r-3>0.

Hartshorne's high-self-intersection theorem and the ruled-model
intersection argument already isolated in the evidence for
STCI-R-0005 apply to the pair `(T,Z_t)` and the nef divisor `H`.
They give

    d <= max_(a positive integer)
              (8ra-(7r-2)a^2) <= r+2.             (7)

The last maximum is at `a=1`, since `7r-2>=4r` for `r>=2`. The
geometric input is Hartshorne,
[*Curves with high self-intersection on algebraic surfaces*,
Theorem 4.1, printed p. 122](https://www.numdam.org/item/PMIHES_1969__36__111_0.pdf).
The local equivalence to the ruled neighborhood and the nef square
comparison are the same accepted mechanism as in
[the preserved independent branch review](2026-10-15-formal-branch-ruled-model-degree-bound-review.md).
We use that mechanism with the new smoothed curve, not the statement
that a smooth `(2,r)` root itself exists in `E`.

Meanwhile `W cap E` contains the original full root `Z`. Thus the
generic multiplicity `m` of the integral surface `S` along `C0`
satisfies `m>=r`. A general plane section is an integral degree-`d`
plane curve with multiplicity at least `m` at the four distinct points
of its intersection with `C0`. Its arithmetic genus gives

    (d-1)(d-2) >= 4m(m-1) >= 4r(r-1).             (8)

Equations (7)--(8) force

    r(r+1) >= 4r(r-1),

which is impossible for `r>=2`. This proves Theorem A under the stated
formal-surface regularity hypothesis.

## 7. Separate two-component proof without Hilbert smoothing

For the R0011 boundary `Z=D1 union D2`, `Di=(1,q)`, `r=2q`, assume the
lifted formal surface is regular along one full component. The surface
is automatically regular away from `D1 cap D2`, because the root is
smooth there. Regularity along one component includes every
intersection point, so it implies regularity along all `Z`.

There is a shorter proof in this case. In the regular formal surface,

    D1^2 = E.D1-D2.D1 = (7q-1)-2q = 5q-1,
    H.D1 = 4q.

Algebraization by Bost may use the full lci root `Z`, or the smooth
center `D1`, whose normal degree is positive. Normalize and resolve
outside `D1`, preserving its square. Hodge index yields

    d <= (H.D1)^2/D1^2
       = 16q^2/(5q-1) <=4q.

Both components remain in `W cap E`, so `m>=2q`. But

    (4q-1)(4q-2) < 4(2q)(2q-1)

for every `q>=1`, contradicting the plane-section genus bound.
The independent audit linked above reconstructs this shorter proof.

## 8. The exact residual gap and local countershields

At a singular root point, write an exceptional parameter as `u` and a
local lift equation as

    g = f_Z + u h_1 + u^2 h_2 + ... .

Since `df_Z` vanishes there, the lifted surface is regular at this point
exactly when `h_1` has nonzero value. Therefore Theorem A says that
every surviving all-orders lift must have at least one singular root
point with `h_1=0`. This is a concrete first-jet incidence condition
for the remaining formal problem, not an emptiness computation.

There is no automatic regularity implication. In a completed smooth
threefold chart the local equations

    g=xy+u^2,             g=y^2-x^3+u^2

give all-orders embedded Cartier lifts of, respectively, the reduced
node `xy=0` and cusp `y^2-x^3=0` on `u=0`, while the total formal
surfaces are singular at the origin. These are local counterexamples
to the missing regularity implication. They are not global lifts on
the actual exceptional surface of `C0` and do not construct STCIs.

Resolution of such singular lifted surfaces can change the normal
degree of the selected normalized root; the accepted smooth-branch
normal-degree argument cannot simply be reused there. Theorem A does
not exclude that stratum.

No finite jet cutoff, actual-CI singular-root bridge, arbitrary-first-
relation statement, or unrestricted `C0` nonexistence result is claimed.
The universal STCI question remains open.

## 9. General balanced-degree observation

The same proof, if independently reviewed in this scope, works in
characteristic zero for any smooth rational degree-`e` curve in `P3`,
`e>=4`, with explicit balanced normal bundle `O(2e-1)^2`.
Replace `7` by `lambda=2e-1` and `4` by `e`. The normal line is
`O_Z(lambda,-1)`; the same restriction-sequence proof gives generation
and vanishing because `lambda-3>=0`. Ampleness holds since
`lambda*b-a>0`. The smoothed curve has square `lambda*r-2`, genus
`r-1`, and hyperplane intersection `e*r`. The ruled-model bound remains
`d<=r+2`, while the opposing plane bound is
`(d-1)(d-2)>=e*r*(r-1)`, again contradictory for `e>=4,r>=2`.
This observation does not remove the singular-lifted-surface hypothesis.

## 10. Evidence and review status

This is a conceptual argument; no inherited verifier or accepted proof
was rerun. New calculations are the exact ruled-surface cohomology in
Section 4, the embedded smoothing argument in Section 5, and the scope
bridge retaining the original singular root while using a smooth
numerically equivalent curve on `T`.

The linked independent audits both record PASS for the fixed-C0
conditional statements. The degree-e observation in Section 9 remains
separately scoped and is not included in the reported fixed-C0 theorem.
No canonical record is edited or promoted by this note.
