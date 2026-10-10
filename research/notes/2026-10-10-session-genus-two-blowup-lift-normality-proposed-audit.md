# Proposed follow-on audit: the genus-two model in the blowup of its conductor line

Date: 2026-10-10. Author: `oct10_genus_two_conductor_audit`.
Status: **COMPLETE PROPOSED PROOF / separate adversarial audit pending**.

This note records a follow-on argument discovered while auditing the
[entire conductor](2026-10-10-session-genus-two-entire-conductor-independent-audit.md).
The conductor audit remains accepted in its original scope. The present
blowup lift and normality claims have not been promoted to a canonical
frontier entry. No genus-two mate exclusion is asserted.

## 1. Exact inputs

Work over an algebraically closed field of characteristic zero. Let
`X` be an integral nonnormal quartic in `P3`, `nu:S -> X` its finite
normalization, and `sigma:M -> S` its minimal smooth resolution. Put
`H=nu*O_X(1)` and `L=sigma*H`. Use the independently accepted
genus-two inputs:

    M rational;       L^2=4;       K_M.L=-2;
    f=K_M+L;          |f| is a complete basepoint-free pencil;
    h0(M,f)=2;        f^2=0;       L.f=2;
    the actual complete |L| map has image X and is birational.

Use the newly independently audited conductor identities:

    Gamma is the actual reduced conductor line in P3;
    I_Gamma/X = nu_*omega_S;
    R sigma_*omega_M = omega_S;
    ord_Gamma(F_X)=2.

No assumption that `K_S` is Cartier or Q-Cartier is made. No assumption
that the conductor upstairs is Cartier, reduced or smooth is made.

Proposed conclusions:

1. The actual plane-through-`Gamma` rational map agrees with the accepted
   adjoint pencil and extends on `M`.
2. `M -> X` lifts to `rho:M -> Bl_Gamma(P3)`.
3. Its image is the actual strict transform `T`, which is normal and
   Gorenstein; `rho:M -> T` is a crepant resolution.
4. `T` is a conic surface over the actual plane-through-line `P1`.

## 2. The two line equations are the complete adjoint sections

Choose independent ambient linear equations `t0,t1` for `Gamma`.
Since `X` is a quartic, `H0(X,O_X(1))` has dimension four and restricts
onto the two-dimensional `H0(Gamma,O_Gamma(1))`. Consequently

    H0(X,I_Gamma/X(1)) = span(t0,t1).

Finite duality and projection formula identify this space with
`H0(S,omega_S(H))`. Resolution duality and projection formula then
identify it with

    H0(M,omega_M(L)) = H0(M,O_M(f)),

which has dimension two. Thus the two line equations correspond to a
basis `s0,s1` of the **complete** adjoint pencil.

These identifications preserve multiplication by rational functions.
At the common function field they are multiplication by one nonzero
rational canonical form. Therefore, as rational maps,

    t0/t1 = s0/s1.

This is the critical ratio statement. It does not require that the
pullback of the noninvertible canonical sheaf of `S` surject onto the
canonical bundle of `M`.

Write `t_i=g s_i` at the function field. Here `t_i` is a section of
`L`, `s_i` is a section of `f`, and `g` is a rational section of

    L-f = -K_M.

Because `s0,s1` have no common zero, the open sets where one of them
is nonzero cover all of `M`. On the open set where `s_i` is nonzero,

    g=t_i/s_i

is regular. Hence `g` is a global nonzero section of `O_M(-K_M)`.
If `D_M=div(g)`, then

    D_M is effective,        D_M ~ -K_M,
    ideal(t0,t1) O_M = O_M(-D_M).

The last equality is scheme-theoretic: on each of the same open sets,
one of the `s_i` is a unit and the two generators `g s0,g s1` generate
exactly the principal ideal `(g)`.

## 3. The lift and the strict-transform canonical bundle

The universal property of the blowup applies to the invertible ideal
just obtained. It gives a unique lift

    rho:M -> B:=Bl_Gamma(P3).

Equivalently, `B` is the incidence hypersurface in `P3 x P1` with
equation `t0 v-t1 u=0`; the pair of maps `(|L|,|f|)` from `M` satisfies
that equation everywhere. This description also identifies the ruling
coordinate without changing the original ambient projection.

Let `H_B` be the pulled-back hyperplane class and `E_B` the exceptional
divisor. The lift satisfies

    rho*H_B=L,       rho*E_B=D_M.

The image of `rho` is the actual strict transform `T` of `X`, because
over the dense complement of `Gamma` both maps agree with the original
birational map to `X`. The order-two result gives

    T ~ 4H_B-2E_B.

The smooth threefold `B` has canonical class `-4H_B+E_B`. Adjunction
therefore gives the invertible dualizing sheaf

    omega_T = O_T(-E_B),

even before normality of `T` has been established. Pulling back gives

    rho*omega_T = O_M(-D_M) = O_M(K_M) = omega_M.

The equality here is an isomorphism of line bundles on the projective
surface `M`. No normality or canonical divisor on the intermediate
surface `T` has been assumed in obtaining it.

## 4. Normality directly from the proper duality trace

The following elementary duality observation avoids a circular
classification of the singularities of the normalization of `T`.

**Lemma.** Let `rho:Y -> T` be proper birational, with `Y` smooth and
`T` proper integral Gorenstein over an algebraically closed field.
If `omega_Y` is isomorphic to `rho*omega_T` as line bundles, then `T`
is normal.

**Proposed proof.** Projection formula gives

    rho_*omega_Y = omega_T tensor rho_*O_Y.

Proper duality has a trace map `rho_*omega_Y -> omega_T`. Its
generic map is nonzero, since the birational map is an isomorphism at
the generic point. Untwist by the invertible `omega_T`; this produces
a generically nonzero `O_T`-linear map

    psi:rho_*O_Y -> O_T.

The restriction to `O_T subset rho_*O_Y` is an endomorphism of `O_T`.
It is multiplication by a global function on proper integral `T`,
thus by a constant `c in k`. It is generically nonzero, so `c!=0`.
After rescaling, it is the identity on `O_T`.

At the common fraction field an `O_T`-linear map of rank-one modules
is multiplication by its value at `1`. Thus the rescaled map is
multiplication by `1`. Every section of `rho_*O_Y` must already be
in `O_T`, whence `rho_*O_Y=O_T`. Proper birational pushforward from
normal `Y` is the finite normalization algebra of `T` (equivalently,
apply Stein factorization). Therefore `T` is normal. QED.

Apply this lemma to the line-bundle identity from section 3. It proves
normality of the actual strict transform.

The precise duality input is the counit trace for a proper morphism;
the identity `rho^!(omega_T[2])=omega_M[2]` follows from normalized
duality over the field. Its degree-zero trace is the map used above.
See [Stacks 48.19, proper duality and the duality functors](https://stacks.math.columbia.edu/tag/0AU3).
The generic nonvanishing follows by restriction to the birational
isomorphism locus. No vanishing theorem for `R1 rho_*O_M` is used in
this normality proof.

## 5. Crepancy, exceptional curves, and conic fibers

Now that `T` is normal Gorenstein, its canonical pullback is defined.
The relative canonical divisor is supported on the exceptional locus.
The obtained line-bundle identity makes it linearly trivial. A
principal divisor supported only on exceptional curves pushes to the
zero divisor on the proper normal `T`; its rational function is then
constant. Thus the relative canonical divisor is actually zero:

    K_M = rho*K_T.

This is a crepant resolution. The standard surface characterization
therefore makes the singularities Du Val; the primary formulation
checked is [Reid, Theorem 2.1(2)](https://mreid.warwick.ac.uk/surf/more/DuVal.pdf).
For an algebraic field of characteristic zero use its standard
algebraic surface version. The conclusion is about `T`, not `S`.

A prime curve on `M` is contracted by `rho` exactly when

    L.E=0 and f.E=0,

because the blowup is a closed subscheme of `P3 x P1`, and the map is
the pair `(|L|,|f|)`. The accepted null-curve theorem says these are
precisely the vertical smooth rational `(-2)` curves. This also
independently matches the crepant resolution and leaves no exceptional
`(-1)` curve for `rho`.

The ruling `B -> P1` has each fiber equal to the corresponding plane
through `Gamma`. On such a plane `H_B` and `E_B` both restrict to the
line class. Therefore the strict-transform equation restricts to a
quadratic equation:

    (4H_B-2E_B)|fiber = O_P2(2).

It never vanishes identically on the whole fiber. Otherwise that
plane would lie in `T`, and its image plane would lie in integral
quartic `X`, which is impossible. Thus `T -> P1` is the actual family
of plane conics obtained by subtracting the double conductor line
from the original plane quartics. Its general fiber is the already
accepted smooth plane conic.

Because `T` is normal, its dominant map to `X` factors through the
finite normalization `S`. The resulting proper birational map
`T -> S` can contract only the images of the horizontal exceptional
curves of `sigma`. The accepted null-curve theorem bounds their
strict transforms on `M` by at most two disjoint `(-3)` sections.
Their images on `T` need not be disjoint: they could meet at a
contracted vertical configuration. No stronger boundary claim is
made here.

## 6. Conditional mate line-position consequences

Let `c` be the strict transform on `M` of the fixed smooth rational
degree-four curve `C0`, and use the accepted isomorphism `c -> C0`.
The curve is not contained in `D_M`, since its ambient image is not
the conductor line. Restricting the common-factor formula to `c`
gives the actual two ambient line equations on `O_P1(4)`:

    t_i|c = (g|c)(s_i|c).

The restricted adjoint sections have no common zero. Hence the entire
intersection scheme `Gamma intersect C0` is the zero divisor of
`g|c`, including repeated contacts and points whose image is singular
on `S`. Its length is

    tau = D_M.c = 4-f.c.

For the two accepted numerical mate strata this says

    f.c=2 (bisection) => tau=2,
    f.c=1 (section)   => tau=3.

Thus these are actual length-two and length-three line intersections,
not just first-jet incidences. The formula does not classify their
positions on the fixed parameter line.

There is also a direct consequence of the accepted conductor theorem
and full support of a hypothetical mate. Every point
`P in Gamma intersect C0` is a zero of the mate, so all points of the
finite conductor fiber `p^{-1}(P)` must lie on the curve over `C0`.
That curve maps isomorphically to `C0`, so the fiber has singleton
set-theoretic support. In the quadratic algebra

    O_Gamma[w]/(w^2-delta)

over an algebraically closed field of characteristic zero, this forces
`delta(P)=0`. Thus the support of every line intersection lies in the
zero set of the quartic branch section. The case `delta=0` identically
is retained and imposes no finite branch-support bound.

This paragraph gives necessary geometric constraints. It does not
establish multiplicities of the intersection in the branch divisor,
nor does it exclude either mate stratum.

## 7. Exact review obligations

A separate auditor should check:

1. that the finite and resolution duality isomorphisms in section 2
   identify ratios of the two actual ambient line forms;
2. that the absence of adjoint base points makes the common factor
   globally regular, including all exceptional strata;
3. that the normality lemma uses the actual proper duality trace and
   does not assume normality of `T` beforehand;
4. that the strict-transform class and canonical identity use generic
   conductor multiplicity exactly two;
5. that crepancy and the conic model are inferred only after normality.

Until those checks are independently completed, this note is a
proposed structural theorem. It is neither an accepted complete
genus-two classification nor a mate exclusion. The genus-two mate
lane and unrestricted STCI questions remain **OPEN**.
