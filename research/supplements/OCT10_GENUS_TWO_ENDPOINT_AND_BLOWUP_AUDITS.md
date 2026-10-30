# Historical mathematical investigations

Full original mathematical text follows. Preserve source-level evidence status, counterexamples, corrections and unresolved boundaries; no independent re-audit or result promotion.

---

## Source: 2026-10-10-session-genus-two-bisection-local-fibers-independent-audit.md

# Genus-two bisection local fibers: independent audit and remaining structural route

Date: 2026-10-10 local time; written at 2026-10-11T01:17 UTC.
Auditor: `bisection_local_fibers`. Status of Sections 1--4:
**PROVED HERE / independent audit passed**, conditional on the explicitly
accepted second-pencil and smooth-embedded-lift reductions. Section 5 is a
separate structural proposal requiring its own audit. No canonical file
is edited, and this note asserts no universal STCI theorem.

Audited source:
[three-blowup fiber exclusion](GENUS_TWO_BISECTION_THREE_CENTER_PROOF.md),
SHA256 `f7177554d64e14a30d169daaedee7ff2ebcc51ed8b3d8435ed590369d9f24103`.
The present auditor independently checked every coefficient, center
restriction, and final contact contradiction. This is a mathematical
audit; no CAS execution or new symbolic-check count is claimed.

## 1. Precise input and verdict

Use the characteristic-zero notation of the
[second-pencil audit](#source-2026-10-10-session-genus-two-bisection-second-pencil-independent-auditmd).
There is a smooth weak degree-four del Pezzo surface V, with connected
rational pencils f and c satisfying `-K_V=f+c` and `f.c=2`. The smooth
minimal resolution M is obtained from V by four point blowups disjoint
from the actual smooth curve c, including every infinitely near center.
For a hypothetical lambda-zero mate,

    Z_t=(k_t/2)F_t-R_t,

is an actual equality of rational divisors, with full scheme-theoretic
fiber multiplicities. The positive support of Z consists of
sigma-exceptional vertical (-2)-curves. A contacted exceptional graph
has only one transverse c-contact, and the actual pullback of a local
uniformizer supplies a positive integral anti-nef exceptional cycle
whose coefficient at that contact is one.

The three-blowup note is accepted at exactly this scope: **every fiber
with k_t=3 is impossible**. Combining it with the independently checked
[even-count exclusion](GENUS_TWO_BISECTION_EVEN_FIBER_PROOF.md)
leaves only `[1,1,1,1]`. This conclusion does not yet use conductor power
descent, the splitting of the conductor, or the fixed embedding of C0.

## 2. The fiber list includes all multiplicities

The source's relative contraction argument is sufficient. Contracting a
vertical (-1)-curve E preserves anticanonical nefness: for an uncontracted
curve C, the anticanonical degree of its image increases by `E.C`.
Reverse a contraction sequence to a ruled surface. Starting from a
smooth square-zero fiber, the first blowup produces two (-1)-components.
An intermediate (-2)-component cannot be touched while anticanonical
nefness is retained. Smooth blowups at a (-1)-end extend a reduced chain;
the intersection of two adjacent (-1)-components can instead be blown
up once, creating a multiplicity-two (-1)-component with two
multiplicity-one (-2)-leaves. Subsequent smooth blowups extend the
multiplicity-two tail.

Thus the irreducible square-zero, reduced-chain, and nonreduced D-tail
fiber types exhaust the possibilities on V, including preexisting ADE
exceptional components. This argument does not assume that a degenerate
conic is reduced, and does not impose a root-rank bound.

## 3. Independent check of the three-center histories

An original V-component of multiplicity m has no coefficient in the
relative canonical divisor R. Its strict transform therefore has Z
coefficient `3m/2>0` and must finish with square -2. Old (-2)-components
cannot be hit, old (-1)-components must be hit once, and a square-zero
component must be hit twice. At a new center, the fiber multiplicity is
the sum of the multiplicities of components through it; the relative
canonical coefficient is one plus their relative canonical coefficients.
These rules use the actual total transforms and remain valid at
intersection centers.

The irreducible case has just one possible complete history: a smooth
blowup of the old component, an intersection blowup of that component
with the new exceptional, and a smooth blowup of the next exceptional.
The positive graph is A3, with unchanged total c-contact two. The
reduced case can finish only when the two old (-1)-ends were adjacent
and were blown up together; two further smooth blowups produce D4.
Its two old ends both meet c once, in the same exceptional graph. Both
cases violate the actual smooth-lift condition.

In the nonreduced case the three centers are forced smooth successive
points starting on the unique multiplicity-two (-1)-component A. The
positive graph is D_n, with A internal on the long arm, or at its fork.
The shortest graph is D5 and its correction is

    3A+(3/2)(U+V)+2E1+E2.

This correction is effective, numerically anti-nef after adding c, and
has `c.Z_t=3`. The numerical data alone do not exclude it. If an actual
uniformizer cycle had coefficient one at A, the (-2) anti-nef inequality
would force both adjacent coefficients to be one. Propagation along the
old multiplicity-two tail reaches a trivalent vertex with coefficient
one, where `2>=1+1+1` is impossible. This verifies the required local
contradiction without using a fundamental-cycle table.

## 4. Failure shield: one blowup need not start with a reduced node

It would be false to infer locally that k=1 forces a reduced nodal fiber.
For example, on V take a multiplicity-two (-1)-component A with two
multiplicity-one (-2)-leaves U,V. Blow up a smooth point of A disjoint
from c. On M,

    F=2A+U+V+2E,   R=E,
    Z=(1/2)F-R=A+(U+V)/2.

The new E has square -1 and zero Z coefficient; the positive graph is
A3, contacted at its middle component A. The positive integral
anti-nef cycle with all three coefficients one is compatible with the
local uniformizer condition. This is a local consistency example, not
a globally realized quartic or mate.

Consequently any exclusion of nonreduced k=1 fibers must use a global
constraint, not the three-blowup proof or a local smoothness shortcut.

## 5. Proposed global route for the four-single-blowup partition

The following additional route is supplied to the root for a separate
audit; it is not needed for the accepted Sections 1--4.

The finite double cover `W->P1_f x P1_c` has branch equation of bidegree
(2,2), quadratic in the second coordinate. Its discriminant is a
nonzero degree-four section on the f-base. Nonzeroness follows from
the integral smooth general f-fiber. Each supported k=1 fiber must
already be degenerate on V: an irreducible square-zero component would
have positive Z coefficient after only one hit and would have square
-1 rather than -2. Four distinct supported fibers therefore require
four discriminant zeros. Degree four forces each zero to be simple.

A simple discriminant zero gives a nonzero quadratic with one double
root, and the total double-cover surface is regular at the corresponding
node. Every degeneration is thus a simple reduced nodal conic. In
particular the branch curve is smooth: a singular branch point would
give a discriminant zero of multiplicity at least two. A smooth branch
divisor of class (2,2) is connected and hence irreducible; it is a smooth
genus-one curve. The local node blowup is forced, and each of the four
nodes lies on the ramification curve of the double cover.

The ramification curve on V is the anticanonical divisor `-K_V=f+c`.
Its proper transform through the four node blowups is an effective
integral anticanonical divisor on M and remains a smooth genus-one
curve. The actual ambient conic model supplies an effective divisor
`D_M=-K_M`, pulled back from the entire conductor. The
[unique-anticanonical-section argument](2026-10-10-session-genus-two-conductor-line-position.md)
would identify D_M with this irreducible genus-one curve. To check that
argument directly, tensor the basepoint-free f-pencil sequence by -K.
An effective section of `-K-f` would write `L=2f+T` and impose a
nonzero quadric equation on the actual quartic image via three squares.
Thus `H0(-K-f)=0`. Two independent anticanonical sections would then
give four independent products with the two f-sections, a basis of
`H0(L)`, and a Segre quadric on the image. Hence `h0(-K)=1`.

If the entire upstairs conductor has already been proved reduced split
with two rational components, its pulled-back divisor cannot be the
single irreducible genus-one curve just obtained. This would exclude
`[1,1,1,1]` and complete an alternative structural bisection exclusion.
The discriminant-to-entire-conductor identification, and any possible
horizontal contraction, should be checked explicitly before promoting
this section. A separate global Cartier-double-ribbon obstruction is
currently under independent audit and may supersede this longer route.

## 6. Independent check of the proposed ribbon alternative

The root also proposed a short obstruction using the actual Cartier
double `2c_S~2H`. A CM double curve with reduction a smooth P1 has a
square-zero nilradical: its square is generically zero, hence finite
support, and a CM curve has no nonzero finite-support subsheaf. The
nilradical is rank-one torsion-free on P1, so it is a line bundle.
From `chi(O_S(mH))=2m^2+m+1`, the Cartier exact sequence gives double
curve polynomial `8m-6`. Subtracting the reduced curve polynomial
`4m+1` gives nilradical `O_P1(-8)`.

For the literal curve C0, the normal bundle is `O(7) direct_sum O(7)`.
An independent hand calculation is as follows. The quadratic syzygies
of `[s^4,s^3t,st^3,t^4]` are

    (st,-s^2,0,0), (t^2,-st,0,0), (0,t^2,-s^2,0),
    (0,0,st,-s^2), (0,0,t^2,-st).

On s=1 their differential images in `Omega_P1(6)=O(4)` are
`-1,-t,-2t^2,-t^3,-t^4`, times dt. The differential map is therefore
an isomorphism on global sections in characteristic different from
two. Consequently `H0(N^*(6))=H0(N(-8))=0`, and determinant `O(14)`
forces the asserted splitting.

The morphism from the double to P3 induces a global map
`I_C0/I_C0^2 -> O(-8)`. This map is generically surjective outside
the conductor, where normalization is an isomorphism and the double
is the actual Cartier double of c. Its Hom group is nevertheless zero,
since `Hom(O(-7)^2,O(-8))=H0(O(-1))^2=0`. The construction needs no
global closed immersion of the double into P3. This corroborates the
root's proposed obstruction; its final acceptance is assigned to the
separate full auditor and is not asserted by this local-fiber record.


---

## Source: 2026-10-10-session-genus-two-bisection-second-pencil-independent-audit.md

# Independent audit: the genus-two bisection double cover and its fiber weights

Date: 2026-10-10. Auditor: `bisection_second_pencil_audit`, with a
separate adversarial check by `fiber_weight_parity_audit` of Sections
5--7. Status: **PROVED HERE, conditional on the accepted genus-two
mate reduction**. This is a structural reduction; it does not exclude
the entire bisection stratum or resolve the genus-two mate problem.
No canonical frontier file was edited by this auditor.

## 1. Exact hypotheses and notation

Work over an algebraically closed field of characteristic zero. The
[adjoint model](2026-10-09-session-genus-two-adjoint-conic-model.md) and
[independent mate audit](2026-10-09-session-genus-two-nullcurve-mate-independent-audit.md)
give a smooth rational minimal resolution `sigma:M->S`, the pulled-back
hyperplane class `L`, and a connected rational pencil `f=K_M+L`, with

    K_M^2=0,   L^2=4,   K_M.L=-2,   f^2=0,   K_M.f=-2.

Assume a hypothetical mate in the retained `lambda=0` stratum. Write
`c` for its smooth strict transform on M and `Z` for its actual
effective rational exceptional correction. Thus

    c=P1,   c^2=0,   K_M.c=-2,   f.c=2,
    L equivalent_Q to c+Z,   L.Z=0,   Z^2=-4.

Every prime in `Supp(Z)` is a smooth rational vertical `(-2)` curve.
In particular `K_M.Z_t=0` for the portion of Z over any f-fiber t.
The accepted smooth-embedded-lift argument also gives

    Z is not an integral divisor in the sigma-exceptional lattice.

An actual degree-b mate supplies `bZ` integral in that lattice.
Fractional exceptional coefficients must not be discarded. When the
accepted relation is initially numerical, clearing its denominators
and applying the numerical-to-linear lemma on the smooth rational M
gives the displayed rational linear equivalence. That is sufficient
for every clearing-denominator argument below.

## 2. The second complete connected rational pencil

The exact sequence

    0 -> O_M -> O_M(c) -> O_c(c) -> 0

has last term `O_P1` and `H1(O_M)=0`. Consequently `h0(c)=2`, and the
restriction map onto `H0(O_c)` is surjective. A section restricting
nontrivially to c is nonzero everywhere on c; the canonical section
of `O_M(c)` is nonzero off c. These two sections generate everywhere,
so the complete pencil is basepoint free.

Its Stein factor has a genus-zero base: `H1` of that base injects into
`H1(O_M)=0`. If the finite map from this P1 to the target P1 had degree
d, projection formula and connectedness would give `h0(c)=d+1`.
Thus d=1. The pencil has connected fibers. General fibers are smooth
by characteristic-zero generic smoothness and have genus zero by
adjunction. This argument includes special reducible or nonreduced
members; it does not impose smoothness on every member.

## 3. The Stein cover has branch class (2,2)

The morphism

    psi=(f,c): M -> Y=P1 x P1

is dominant and generically finite. Otherwise its two pencils would
factor through one curve and their fiber intersection would be zero.
Its degree is the intersection of the two pulled-back ruling classes,
namely `f.c=2`. Its Stein factorization is

    M --mu--> W --phi--> Y,

where mu is birational, W is normal integral, and phi is finite of
degree two. Normal surfaces are Cohen--Macaulay. Since Y is regular
of dimension two, the finite O_Y-module `phi_*O_W` is locally free
(regular parameters are a maximal Cohen--Macaulay sequence, and the
Auslander--Buchsbaum formula applies). Hence phi is flat.

Trace divided by two splits its algebra as

    phi_*O_W = O_Y direct_sum N^(-1),
    N=O_Y(a,b),   w^2=delta in H0(Y,N^2).

Over a general member of either ruling, mu is an isomorphism on the
corresponding general pencil fiber: every mu-exceptional curve has
both f- and c-degree zero, so only finitely many parameter values are
affected. Each restricted double cover therefore has upstairs P1.
Its Euler characteristic is `1+(1-b)=2-b` for the first ruling, and
`2-a` for the other. Both are 1, proving `a=b=1`.

Thus the branch section has class `(2,2)` and

    phi_*O_W = O_Y direct_sum O_Y(-1,-1).

No smoothness, irreducibility, or general-position hypothesis on the
branch curve was used. In particular branch components and branch
singularities remain included.

## 4. W is an ADE del Pezzo surface, and M has four further blowups

Finite duality gives

    omega_W = phi^*(omega_Y tensor N) = phi^*O_Y(-1,-1).

For clarity, the required algebra calculation is valid even on a
special fiber where the multiplication section degenerates. Locally
`B=A[w]/(w^2-delta)`, and the pairing taking the coefficient of w in
`bb'` has matrix `[[0,1],[1,0]]`. It identifies `Hom_A(B,A)` with B
with the N twist when the local generator of N is changed. Hence the
dualizing sheaf is invertible without a smooth-branch assumption.

The anticanonical class is the finite pullback of `O_Y(1,1)`, so it is
ample and has square 4. We establish rational singularities separately
from birational rationality. Serre duality gives `H2(O_W)=0`, since
`omega_W` is antiample. The birational Leray sequence gives

    H1(O_W) -> H1(O_M)=0 -> H0(R1 mu_*O_M) -> H2(O_W)=0.

Here `mu_*O_M=O_W`, and `R1 mu_*O_M` is supported on finitely many
points. It therefore vanishes. W has rational singularities. Normal
Gorenstein rational surface singularities are rational double points;
the applicable primary reference is [Stacks, Section 54.12](https://stacks.math.columbia.edu/tag/0BGB).
Thus W is an ADE del Pezzo surface of degree four.

Let `rho:V->W` be its minimal crepant resolution. Every resolution of
a normal surface dominates the minimal resolution, so mu factors as

    M --alpha--> V --rho--> W.

The morphism alpha between smooth surfaces is a sequence of point
blowups, allowing infinitely near centers; see [Stacks, Lemma 54.17.1](https://stacks.math.columbia.edu/tag/0C5Q).
Crepancy gives `K_V^2=4`. Each point blowup lowers the canonical square
by one. Since `K_M^2=0`, the sequence has exactly four blowups.

Write `e_i` for the effective total exceptional transform of the i-th
of these four blowups. These total classes satisfy `e_i.e_j=-delta_ij`.
The actual relative canonical divisor is

    R=K_M-alpha^*K_V=sum_{i=1}^4 e_i.

It is effective and integral, even when the centers are infinitely
near or are intersections of prior exceptional components. Its
support is alpha-exceptional and consequently vertical for both f
and c. ADE exceptional curves already present on V are crepant and
need not occur in R.

Since `alpha^*K_V=-f-c` while `K_M=f-L=f-c-Z`, we obtain

    Z+R equivalent_Q to 2f.

## 5. Rational linear equivalence forces actual whole fibers

Put `D=Z+R`, an actual effective Q-divisor. Choose a positive integer m
clearing its denominators and its rational linear equivalence. Then
`mD` is an effective integral divisor linearly equivalent to `2mf`.
Because the f-pencil has connected fibers,

    H0(M,O_M(2mf)) = H0(P1,O_P1(2m)).

Every effective divisor in this linear system is the actual pullback
of a degree-2m divisor on the base. Thus, writing `F_t` for the complete
scheme-theoretic fiber, including every component multiplicity,

    D=sum_t q_t F_t,   q_t>=0 rational,   sum_t q_t=2.

This is equality of actual Q-divisors, not merely a numerical class.
There is no assumption that the fibers, Z, or the branch curve are
reduced. It would be incorrect to infer at most two supported fibers
just from the degree 2; the weights may be halves.

## 6. Exact weights count the four blowups

Let `k_t` be the number of the four alpha-blowups whose centers lie
over the f-parameter t, counting every infinitely near center. Write

    R_t=sum_{i over t} e_i.

The total-transform intersection identities give

    K_M.R_t=-k_t.

Equivalently, at a point blowup over t the actual relative canonical
divisor changes by `R_t -> b^*R_t+E_new`. Its square drops by one,
because `b^*R_t.E_new=0`; its intersection with the pullback of K_V is
zero. Thus `R_t^2=K_M.R_t=-k_t`. This also verifies the assertion
directly at intersection centers and along infinitely near chains.

Taking K_M-intersection of the actual part of D over t gives

    -2q_t=K_M.(q_t F_t)=K_M.Z_t+K_M.R_t=0-k_t.

Therefore

    q_t=k_t/2,   sum_t k_t=4.

In particular D is supported on exactly those fibers over which at
least one of the four blowups occurs. There are at most four such
fibers. The exact divisor identity is

    Z+R=(1/2) sum_t k_t F_t,
    2Z=sum_t k_t F_t-2R.

Thus `2Z` is an integral effective sigma-exceptional divisor. These
claims make no assumptions on the multiplicities of components of
the complete fibers and survive all degenerate ADE branch types.

## 7. Missing-lattice parity leaves three partitions

If every nonzero k_t were even, the last formula would make Z itself
an integral divisor. Since its support is sigma-exceptional, it would
belong to the integral sigma-exceptional lattice, contrary to the
accepted missing-lattice condition.

The possible partitions of four therefore reduce as follows:

| Blowup counts over distinct f-fibers | Fiber weights | Status here |
| --- | --- | --- |
| `[4]` | `[2]` | Excluded: Z integral |
| `[3,1]` | `[3/2,1/2]` | Retained |
| `[2,2]` | `[1,1]` | Excluded: Z integral |
| `[2,1,1]` | `[1,1/2,1/2]` | Retained |
| `[1,1,1,1]` | `[1/2,1/2,1/2,1/2]` | Retained |

The correction has exact order two modulo the integral exceptional
lattice: it is not integral, but twice it is integral. Combining this
with an actual mate's integral `bZ` forces b even. Clearing numerical
equivalence now also gives `2c equivalent to 2L-2Z` on M and hence
the actual Weil linear equivalence `2c_S equivalent to 2H` downstairs
on S. No assertion is made that its doubled section comes from an
ambient quadratic form: descent to X is a separate question.

## 8. Scope and a check against an invalid stronger bound

The separate fiber-weight auditor accepted Sections 5--7 and supplied
a local consistency check for an odd count. Start with a reduced nodal
fiber `A+B` on V, where both components are `(-1)` curves. Blowing up
their intersection once gives

    F=A'+B'+2E,   R=E,   Z=(A'+B')/2.

Both A' and B' are `(-2)` curves. This matches `k=1` and weight `1/2`;
it shows why rational coefficients and intersection centers must be
included. The example is a local fiber check, not a globally realized
quartic carrier or a mate.

No exclusion of `[3,1]`, `[2,1,1]`, or `[1,1,1,1]` follows from the
counting argument alone. Exceptional-fiber connectedness, the smooth
embedded lift, the actual quartic map, and conductor descent still
have to be imposed. The lambda-one section lane is unchanged.


---

## Source: 2026-10-10-session-genus-two-blowup-lift-normality-independent-audit.md

# Independent audit: the genus-two normalization has an actual normal ambient conic model

Date: 2026-10-10. Auditor: `oct10_genus_one_interfaces`, in a separately
assigned genus-two task. Status: **PROVED HERE / independent structural
audit passed**, under the explicitly accepted inputs below. No canonical
frontier file or prior evidence seal is edited. No mate exclusion follows
from this structural theorem alone.

Audited owner proof:
[genus-two blowup lift and normality](2026-10-10-session-genus-two-blowup-lift-normality-proposed-audit.md),
including its subsequently added section 6. Audited source SHA256:
`2ca17ce2e546bd7ee4f0585cf5b42755c6f723fa8ec867f076a0e33bfd4a1999`.
The owner note's proposal label records its status before this separate
audit; the present note independently establishes acceptance at the
bounded scope stated here.

## 1. Inputs and exact conclusion

Work over an algebraically closed field of characteristic zero. Let
`X` be an integral nonnormal quartic surface in `P3`, let `nu:S->X`
be its finite normalization, and let `sigma:M->S` be its minimal smooth
resolution. Set `H=nu*O_X(1)` and `L=sigma*H`. Accept the established
sectional-genus-two inputs:

    M rational,     L^2=4,     K_M.L=-2,
    f=K_M+L,        h0(f)=2,
    |f| complete and basepoint free,
    f^2=0,          L.f=2,
    the actual |L| morphism is birational onto X.

Also accept the independently proved [entire conductor theorem](GENUS_TWO_ENTIRE_CONDUCTOR_PROOF.md):
the actual conductor `Gamma` is a reduced line, its ideal on `X` is
`I=nu_*omega_S`, resolution duality gives `R sigma_*omega_M=omega_S`,
and the generic order of the quartic equation along `Gamma` is exactly
two. That source's SHA256 at this audit is
`77bc3c17b7832907fd2d859de6e4d82735f6b279efb923ecd9a865fbc0767550`.
These inputs hold in the accepted genus-two normalization lane for a
quartic containing fixed `C0`; no mate is used in them.

The proposed follow-on conclusions pass:

* The actual planes-through-line rational map agrees with the complete
  adjoint pencil and extends everywhere on `M`.
* The actual morphism `M->X->P3` lifts to `B=Bl_Gamma(P3)`.
* Its image is the integral strict transform `T` of `X`, of class
  `4H_B-2E_B`. This `T` is normal Gorenstein with only Du Val
  singularities, and `M->T` is its crepant resolution.
* The ruling of `B` restricts to the actual plane-conic family on `T`.

This conclusion concerns `T`. It does not show the original
normalization `S` is Gorenstein, and does not make its adjoint pencil
descend through possible horizontal exceptional contractions.

## 2. The natural canonical identifications preserve the actual ratios

Choose independent ambient line equations `t0,t1` of `Gamma`. The four
ambient linear sections give all of `H0(X,O_X(1))`, and their restriction
onto `H0(Gamma,O_Gamma(1))` is surjective. Hence

    H0(X,I(1))=span(t0,t1).

Finite duality and projection formula identify this space with
`H0(S,omega_S(H))`. The accepted resolution duality and projection
formula identify the latter with `H0(M,omega_M(L))=H0(M,f)`.
The resulting `s0,s1` are therefore a basis of the complete pencil.

One must use these **sheaf-theoretic natural identifications**, not an
arbitrary two-dimensional vector-space isomorphism. The finite duality
identification is linear over the finite normalization algebra; in the
common function field both canonical modules are one-dimensional.
The proper-duality identification has the same rank-one function-field
property. Thus the composite is multiplication by one nonzero rational
canonical form, independent of the chosen section. Taking ratios gives

    t0/t1=s0/s1

as rational functions, using compatible rational trivializations of the
two line bundles. There is no need for the possibly noninvertible
`sigma*omega_S` to surject onto `omega_M`. Only its accepted pushforward
duality and the common function-field identification are used.

It follows that there is one rational section `g` of
`L-f=-K_M` such that `t_i=g s_i`. The open sets on which `s0` or `s1`
is nonzero cover **all** of `M`, because the complete pencil is
basepoint free. On each such open `g=t_i/s_i` is regular. The two
expressions agree in the function field and hence agree on their
overlap. Consequently `g` is a nonzero global section of `-K_M`.

Writing `D_M=div(g)` gives an actual effective Cartier divisor with

    D_M ~ -K_M.

Locally trivialize `L` and `f`. Because the two `s_i` generate `f`,
the ideal generated by the two pulled-back line forms is exactly
the local principal ideal `(g)`. These local image ideals glue to

    I_Gamma/P3 O_M = O_M(-D_M) subset O_M.

This is equality of image ideals, including their scheme structure
and every exceptional point. It is stronger than a common divisorial
factor plus an unexamined zero-dimensional residual base locus. The
absence of that residual locus follows from the complete pencil's
basepoint freeness.

## 3. Lift, integral strict transform, and exact multiplicity

The inverse image of the ambient center is now an effective Cartier
divisor. The [universal property of blowing up, Stacks 31.33.5](https://stacks.math.columbia.edu/tag/01OF)
therefore gives a unique lift `rho:M->B`. The blowup is the incidence
hypersurface in `P3 x P1` cut out by `t0 v-t1 u=0`; the pair
`(|L|,|f|)` satisfies that equation because of section 2. It follows
that the second coordinate is the **actual** plane-through-`Gamma`
parameter, rather than an unbound abstract conic pencil.

Its pullbacks are

    rho*H_B=L,       rho*E_B=D_M.

Outside `Gamma`, the blowup is an isomorphism, and the lift is the
original birational map to `X`. Since `M` is proper, its image is
closed and irreducible. It is consequently the closure of the dense
strict-transform open, hence the entire strict transform `T`.
The induced `rho:M->T` is proper birational.

The strict transform is integral: it is the reduced scheme-theoretic
closure of that integral dense open. On the smooth threefold `B`
it is a prime codimension-one divisor and hence Cartier. It follows
that it is Gorenstein and Cohen--Macaulay **before** normality is
proved. This is the needed hypothesis for the trace argument; being
a proper image of a normal source alone would not give normality.

The order of the total transform along the prime exceptional divisor
is the order of `F_X` in the ideal of the generic point of `Gamma`.
The accepted transverse calculation makes this coefficient exactly
two. Subtracting this actual coefficient gives

    T ~ 4H_B-2E_B.

Special points of higher local multiplicity on `Gamma` do not alter
that coefficient or add an exceptional surface component to the
integral strict transform. For a linear center the ideal-power
membership can also be seen by expanding `F_X` in its two normal
line coordinates: its constant and linear coefficient polynomials
vanish identically on `Gamma`, while at least one quadratic coefficient
is nonzero. Thus there is no unverified replacement of generic order
by a stronger uniform pointwise statement.

The ambient canonical divisor is `K_B=-4H_B+E_B`. Adjunction for the
Cartier `T` then gives

    omega_T=O_T(-E_B),
    rho*omega_T=O_M(-D_M) isomorphic to omega_M.

The signs have an independent incidence check. If `F_B` is the ruling
class from `P1`, then `E_B=H_B-F_B`. The incidence variety has class
`(1,1)` in `P3 x P1`, so adjunction gives `K_B=-3H_B-F_B`, which is
again `-4H_B+E_B`. The strict transform has class `2H_B+2F_B`, and
its canonical class is `-H_B+F_B=-E_B` as above.

## 4. Normality from proper trace: the complete independent lemma

**Lemma.** Let `rho:Y->T` be a proper birational morphism of integral
varieties over algebraically closed `k`. Suppose `Y` is smooth, `T`
is proper over `k` and Gorenstein, and there is a line-bundle isomorphism
`alpha:rho*omega_T -> omega_Y`. Then `T` is normal.

Here is the full proof, with the cohomological shift explicit. Put
`d=dim(Y)=dim(T)` and `B_T=rho_*O_Y`. Their dualizing complexes
normalized over the same field are `omega_Y[d]` and `omega_T[d]`.
Proper duality gives the counit

    R rho_*(omega_Y[d]) -> omega_T[d].

Taking `H^(-d)` gives the actual sheaf map
`rho_*omega_Y -> omega_T`. Equivalently it is `H^0` after removing
the common shift. This map exists without normality of `T` and without
vanishing of any higher direct image. The precise primary statements
are [Stacks 48.20.8](https://stacks.math.columbia.edu/tag/0AUD)
and [48.20.11](https://stacks.math.columbia.edu/tag/0B6X).

On the dense birational isomorphism open, the counit is the trace
for an isomorphism. Compatibility with open restriction is included
in [Stacks 48.7.1](https://stacks.math.columbia.edu/tag/0B6J).
Hence it is nonzero at the generic point. Composing the projection
formula and the chosen `alpha` with this trace gives

    omega_T tensor B_T -> rho_*omega_Y -> omega_T.

Untwisting the invertible `omega_T` produces a generically nonzero
`O_T`-linear map `psi:B_T->O_T`. Its restriction to the natural
inclusion `O_T->B_T` is multiplication by the global function
`c=psi(1)`. Properness and integrality give `H0(T,O_T)=k`;
this uses no normality, as in
[Stacks 33.9.3](https://stacks.math.columbia.edu/tag/0366).
At the generic point `B_T` and `O_T` are the same function field.
A nonzero linear endomorphism of that field has nonzero value at
one, so `c` is a nonzero constant. Divide `psi` by it.

The rescaled map is the identity at the common function field.
For every local section `b` of `B_T`, its value under `psi` is
therefore the same rational function `b`, but belongs to `O_T`.
Both sheaves embed in the rational function sheaf because the
schemes are integral and the morphism is birational. Thus
`B_T=O_T` as sheaves of rings. By
[Stein factorization, Stacks 37.53.4](https://stacks.math.columbia.edu/tag/03H0),
the pushforward from normal `Y` is the finite normalization algebra
of `T`, so `T` is normal. Alternatively every affine section ring
of `T` is now the ring of regular functions on an open of normal
`Y`; it is integrally closed as an intersection of normal local rings.

The chosen line-bundle isomorphism need not agree with the canonical
one on the dense open. It remains nonzero there, and the resulting
nonzero generic scalar is precisely the scalar forced to be a global
unit by the preceding properness argument. Thus no compatibility
assumption on `alpha` has been left implicit.

Apply this lemma with the actual `T` and the isomorphism from section 3.
All hypotheses have been established before the application. This
proves normality without assuming it in the duality, adjunction, or
strict-transform step.

### Countershield: target properness cannot be omitted

The finite normalization `A1 -> Spec k[t^2,t^3]` is proper birational,
its source is smooth and its target is integral Gorenstein. Both
canonical line bundles are abstractly trivial, yet the cusp is not
normal. In the trace proof the generic conductor multiplier can be
`t^2`, a nonconstant nonunit. It cannot be divided out globally.
For instance the cusp equation `y^2=x^3`, with `x=t^2`, `y=t^3`,
has canonical generator `dx/(2y)=dt/t^2`; the trace of the smooth
generator `dt` is `t^2` times this generator. This verifies concretely
which rescaling step fails. It is a counterexample only to a version
omitting properness of the target over `k`, not to the lemma used here.

## 5. Crepancy, ADE, and the conic ruling

After normality, choose compatible canonical rational forms on the
common function field. The relative canonical divisor
`K_M-rho*K_T` is supported on the exceptional locus. Its line bundle
is trivial by section 3. If a principal divisor is supported there,
its pushforward divisor on normal proper `T` is zero; its rational
function and inverse extend over `T`, hence are constant. Therefore
the actual relative divisor is zero:

    K_M=rho*K_T.

This is the crepant equality required by the characteristic-zero
Du Val criterion. Thus `T` has only ADE singularities. This is not a
conclusion that every singular point of `S` is ADE.

Since the lift is the pair `(|L|,|f|)`, a prime on `M` is contracted
precisely when `L.E=f.E=0`. The accepted null-curve theorem makes
these the vertical smooth rational `(-2)` curves. Horizontal
`(-3)` sections are not contracted to points by `rho`; they can be
contracted only in the subsequent map `T->S`. This distinction is
consistent with the earlier non-Gorenstein normalization boundary.

Every ruling fiber of `B` is the actual plane through `Gamma`.
Both `H_B` and `E_B` restrict to its line class, so the equation
of `T` restricts to a quadratic. It cannot vanish identically on
one whole plane: that would put a plane in the integral quartic
`X`. Thus the fibers are actual nonzero plane conic schemes,
including singular and doubled conics. The general conic is the
accepted smooth conic. No smoothness of the exceptional conductor
or all special fibers is claimed.

The proper normal `T` factors through the finite normalization `S`.
The map `T->S` is birational. The only curves it can contract lift
on `M` to sigma-exceptional horizontal primes; the accepted theorem
bounds them by at most two disjoint `(-3)` sections on `M`. Their
images on `T` may meet at contracted vertical configurations, so
disjointness on `T` is not inferred.

## 6. The added mate line-position consequences also pass

Let `c#` be the smooth strict transform on `M` isomorphic to fixed
`C0`. It is not contained in `D_M`, because its ambient image is
not the conductor line. Restriction of `t_i=g s_i` gives the actual
two line equations on `O_P1(4)`. The restricted `s_i` have no common
zero, so the entire line-intersection ideal on `C0` is generated by
`g|c#`. Its scheme length is therefore

    tau=length(Gamma intersect C0)=D_M.c#=4-f.c#.

Repeated contacts and all exceptional passages are retained here.
The accepted mate strata give respectively `tau=2` for the bisection
and `tau=3` for the section. This is a statement about complete
intersection schemes, not only distinct intersection points.

At every such point, all conductor-cover fiber points are zeros
of a pulled-back mate. Full support and the isomorphism of the
curve above `C0` force that fiber to have singleton support. In
the accepted quadratic line algebra `w^2=delta`, characteristic
zero then forces `delta(P)=0`. Only this support inclusion is
proved; no multiplicity of `g|c#` in `delta` is inferred, and
`delta` identically zero remains allowed.

For the section case, `tau=3` additionally forces `Gamma` onto the
unique smooth quadric `q=x0*x3-x1*x2` containing fixed `C0`: a
degree-two section on a line vanishing on a length-three scheme
must vanish identically. The Segre parametrization

    (a0,a1)=(U,V),       (b0,b1)=(U^3,V^3)

expresses `C0` on this quadric. The two ruling degrees are one
and three, so the length-three line is in the trisecant ruling.
This necessary consequence does not by itself exclude that case.

## 7. Independent scope, evidence, and continuation

A separate delegated `proper_trace_normality_microaudit` independently
accepted the lemma in section 4, including its shifts, generic trace,
global scalar, and normalization step. It independently identified
the same affine-cusp countershield. This audit also read the stated
primary Stacks passages directly and checked the owner's natural
ratios, global fixed part, strict-transform class, both canonical
sign calculations, crepancy, and added line-position paragraph.

These are algebraic-geometric proofs; no finite search, symbolic
sample, or historical verifier pass substitutes for their sheaf
and morphism statements. No new numerical test is needed to turn
the trace proof into a proof. The preceding conductor and adjoint
results retain their own independent scopes and acceptance records.

The structural model is accepted at all stated inputs and conclusions.
The two genus-two mate strata, their full inverse support and descent
conditions, higher carrier degrees, unrestricted fixed `C0`, and
the universal projective-curve STCI question remain open.


---

## Source: 2026-10-10-session-genus-two-endpoint-double-horizontal-independent-audit.md

# Endpoint double-horizontal conductor: independent exclusion

Date: 2026-10-10. Auditor: `double_horizontal_endpoint`.
Status: **PROVED HERE CONDITIONALLY on the accepted genus-two conic model and mate correction inputs**.
This note concerns exactly the endpoint stratum `D_T=2B_T+2F_T`.
It does not claim to exclude other conductor divisors or the unrestricted
set-theoretic complete-intersection problem. No canonical frontier file is
edited here.

## 1. Inputs and the actual equation

Work over an algebraically closed field of characteristic zero. The actual
quartic strict transform `T` in the blowup of the conductor line is normal
Gorenstein, has only ADE singularities, and has a crepant resolution
`rho:M -> T`. At the endpoint use the actual chart

    a=x1/x0,   y=x2/x0,   b=x3/x2,
    C_T: (a,b,y)=(r,r,r^3).

The conductor exceptional surface is `y=0`. In the stratum audited here the
surface equation is

    F = -c*a^2*b^2
        +y*((b-a)*(A+B*b+C*b^2)+c*a-a*b^2*(d+e*b))
        +y^2*(d+e*b),                         c != 0.

Consequently `div_T(y)=2B_T+2F_T`, where locally `B_T=(a,y)` and
`F_T=(b,y)`. The second curve is the vertical conductor component at
`b=0`; it has positive ambient hyperplane degree and is not an exceptional
prime of the normalization map to the quartic. The strict horizontal curve
`B` on `M` satisfies

    B^2=-3,   c#.B=0,   coeff_B(Z)=1,

where `Z` is the effective mate correction and `c#` is the strict curve.
The numerical equations for every contracted vertical ADE prime `E_i`
are `Z.E_i=-c#.E_i`; also `Z.B=0`. At the endpoint the smooth embedded
curve meets one vertical prime with intersection one. These are the
supplied genus-two lambda-one mate inputs, not conclusions from a
first-normal approximation.

On `B_T` the normal coefficient is

    h(b)=F_y(0,b,0)=b*(A+B*b+C*b^2).

Globally this is a nonzero section of `O_B(3)`. It cannot vanish
identically, since that would make all of `B_T` singular on `T`,
contrary to normality. Thus the total multiplicity of its zeros,
including infinity in the other blowup chart, is exactly three.

For an ADE exceptional block put `Q=(-E_i.E_j)` and let the vector
`v` have entries `B.E_i`. Define its contribution

    g_BB = v^t*Q^(-1)*v.

If the contact of `c#` is on that block at node `j`, put
`g_BC=v^t*Q^(-1)*e_j`. The equations above and `coeff_B(Z)=1` imply

    sum_blocks g_BB + g_BC = 3.                 (1)

Only the endpoint block has the `g_BC` term. Blocks outside `B` do not
change this equation. We now bound its left side strictly below three.

## 2. Exact contribution of every root away from the contact

Let `p` be a zero of `h` of multiplicity `k`, away from `b=0`. This
includes a possible point in the chart at infinity. The local equation
there has the form

    a^2*v(a,t)+y*h(t)+a*y*u(a,t,y)+y^2*w(a,t,y)=0,

where `t` is a parameter on `B_T` and `v(0,0)` is a unit. In particular
`div_T(y)=2B_T` near `p`.

On the smooth resolution choose coordinates `(u,t)` with `B=(u=0)`;
the parameter `t` can be the pulled-back parameter on `B_T`, because
the strict transform of the smooth curve `B_T` maps isomorphically to it.
Write

    a=u*A0(u,t),   y=u^2*Y0(u,t).

The hypersurface canonical generator is `da wedge dt/F_y`. Its pullback
is a unit times `du wedge dt`, since the resolution is crepant. Therefore

    A0(0,t) = unit*h(t).

Substitute the two expansions into the defining equation, divide by
`u^2`, and restrict to `B`. It follows that

    Y0(0,t) = unit*h(t).

Thus the leading normal coefficient of `y` on the strict curve has
vanishing order exactly `k` at `p`. On the other hand its divisor is

    div_M(y)=2B+sum_i beta_i E_i,
    beta=2*Q^(-1)*v.

Restricting the residual divisor to `B` identifies that same order with
`sum_i beta_i*(B.E_i)`. Hence

    2*g_BB=k.                                  (2)

This argument allows every ADE type, multiple attachments, and repeated
roots. It does not assume an A-chain away from the contact. A root where
`T` is smooth would give zero residual divisor and therefore `k=0`, so
every positive-order root contributes exactly as in (2).

## 3. Contact with a simple root: A is nonzero

First `A=c` is impossible: along the whole vertical curve `b=y=0`,
all first partial derivatives vanish except possibly
`F_y=a*(c-A)`. Thus `A=c` would make `T` singular along a curve,
contrary to normality. In this paragraph we therefore have
`A!=0` and `A!=c`.

The quadratic part at the contact is

    y*(A*b+(c-A)*a+d*y).

It has rank two. In fact the actual equation forces the germ to be
`A3`. To see this set `t=a` and use `z=A*b+(c-A)*a` as the other
linear coordinate, keeping `y` as the third. Its quadratic kernel is

    y=z=0,   b=((A-c)/A)*t.

The leading restriction to this kernel is
`-c*((A-c)/A)^2*t^4`, with nonzero coefficient. Formal elimination
of the nondegenerate `(z,y)` variables does not change this leading
coefficient: the critical value of `z` has order at least two and
that of `y` has order at least three. Indeed the cubic terms all
contain `y`, so their derivative in `z` vanishes on the kernel;
the derivative in `z` of the first term without `y` has order three.
The formal splitting lemma therefore gives `x*w=unit*t^4`.

The tangent
line of `B_T` is `(a,y)=0`; it is outside the kernel of this quadratic
form, since `A!=0`. The tangent line of `C_T` is `(a,b,y)=(r,r,0)`;
it too is outside the kernel, since substitution into the second linear
factor gives `c*r`, and `c!=0`.

For a rank-two `A_n` germ, a smooth curve with tangent outside the
quadratic kernel meets an endpoint of its exceptional chain. This follows
from the form `x*z=t^(n+1)`: one of `x,z` has order one along the curve,
so its attachment index is `1` or `n`. Both `B` and `c#` therefore attach
at the same endpoint: both have nonzero first-order `z` coordinate
and zero first-order `y` coordinate. The inverse `A3` matrix gives

    g_BB = 3/4,
    g_BC = 3/4,
    g_BB+g_BC = 3/2.

The remaining zeros of `h` have total multiplicity two. By (2) their
total contribution is exactly one. Thus the left side of (1) is exactly
`5/2`, a contradiction. The weaker arbitrary-chain endpoint bound
would already suffice; the global normality cut and the actual quartic
equation supply this sharper fixed value.

## 4. Contact with a repeated root: exact formal factorization

Suppose `A=0`. Put

    P(b)=B*b+C*b^2,   D(b)=d+e*b,
    h(b)=b*P(b),      u(b)=c-P(b)-b^2*D(b).

Then the equation is exactly

    -c*b^2*a^2+u(b)*a*y+h(b)*y+D(b)*y^2=0.

The normality condition leaves `k=ord_0(h)` equal to two or three.
Since `u(0)=c!=0`, take the formal square root with constant term `c`,
and set

    s(b)=sqrt(u(b)^2+4*c*b^2*D(b)),
    w(b)=(u(b)+s(b))/2,   v(b)=D(b)/w(b).

Both `s,w` are units. The invertible formal change

    X=a+v*y,    Y=-c*b^2*a+w*y

has determinant `s=w+c*b^2*v`. Its exact identities are

    F=X*Y+h*y,
    y=(Y+c*b^2*X)/s.

Consequently, after translations

    X1=X+h/s,   Y1=Y+c*b^2*h/s,
    X1*Y1=c*b^2*h^2/s^2.

This is an `A_(2k+1)` equation, after rescaling one coordinate by a
formal unit. On `B_T` the orders of `X1,Y1` are exactly `(k,k+2)`.
Therefore `B` meets node `k` of the `A_(2k+1)` chain, with the reversal
of the chain being immaterial. On `C_T`, `a=b=r` and `y=r^3`, the
coordinate `X1` has order one; hence `c#` meets an endpoint.

Writing `N=2k+2`, the inverse-chain formula now gives

    g_BB = k*(k+2)/N,
    g_BC <= (k+2)/N,
    g_BB+g_BC <= (k+2)/2.

For `k=2` this contact contribution is at most two and the remaining
simple root contributes one half. For `k=3` this contact contribution
is at most five halves and there is no other root. In both cases the
left side of (1) is at most `5/2`, again a contradiction.

## 5. Audited conclusion and scope

Under the stated accepted conic-model and mate-correction hypotheses,
the entire endpoint stratum `D_T=2B_T+2F_T` is excluded. The argument
includes all roots of the normal coefficient at infinity, its repeated
roots, and arbitrary ADE blocks away from the curve contact. In fact
those latter blocks have the exact contribution `ord(h)/2`, rather
than an assumed A-chain bound.

The contact is forced to be `A3` with endpoint attachment, `A5` with
attachment `2`, or `A7` with attachment `3`; these are consequences of the exact ambient
equation and formal factorization. Thus an abstract D/E graph at the
contact is not an omitted parameter stratum in this double-horizontal
case. Other endpoint divisor types and every broader genus-two or
global STCI claim require their own arguments.


---

## Source: 2026-10-10-session-genus-two-endpoint-full-independent-audit.md

# Endpoint trisecant lane: independent coverage and correction audit

Date: 2026-10-10. Auditor: `endpoint_adversarial_audit`.
Status: **PROVED HERE / independent mathematical audit**, conditional only
on the previously accepted genus-two normal conic-model, marking, and
mate-correction inputs listed below. Under those inputs the endpoint
lambda-one lane is excluded. This note makes no claim about lambda zero,
carriers of other degree, other rational quartics, or the universal STCI
problem. No canonical frontier file is edited here.

The audited sources are the
[full endpoint reduction](#source-2026-10-10-session-genus-two-endpoint-full-quartic-reductionmd),
the [local triple ADE calculation](OCT10_BISECTION_AND_ENDPOINT_FOUNDATIONS.md#source-2026-10-10-session-endpoint-local-ade-correction-auditmd),
and the [double-horizontal calculation](#source-2026-10-10-session-genus-two-endpoint-double-horizontal-independent-auditmd).
The older
[irreducible-residual note](2026-10-10-session-genus-two-endpoint-irreducible-conic-obstruction.md)
was read but is not used as an exhaustion certificate: it covers only one
residual stratum. The entire quartic family is supplied by section 2 of
the [carrier ideal proof](2026-10-10-session-genus-two-trisecant-quartic-carriers.md).

## 1. Exact inputs and claim

The ground field is algebraically closed of characteristic zero, and

    C0=[s^4:s^3t:st^3:t^4].

An integral quartic carrier has normalization S and smooth rational
resolution M. In the lambda-one mate stratum the accepted inputs give

    rho:M -> T subset Bl_Gamma(P3),
    T normal Gorenstein ADE, rho crepant,
    f.c#=1, c#^2=1,
    c# ~ L-Z, Z effective rational sigma-exceptional,
    K_M.Z=1, Z.E=-c#.E for every sigma-exceptional prime E.

The map rho contracts precisely the vertical (-2) primes. Every
horizontal sigma-exceptional prime is a (-3) section and has K-degree
one. There are at most two horizontal primes; their images in T are
distinct fibers over points of Gamma on
`E=P1_Gamma x P1_f`. The special prime B exists and satisfies `c#.B=0`.
The smooth embedded descent and local uniformizer input says that the
strict curve meets exactly one prime in any contacted exceptional
fiber, transversely and with intersection one.

The conclusion audited here is: **no mate of any degree exists when
Gamma is either endpoint trisecant of this fixed C0 and lambda=1**.
Reversal exchanges the two endpoints, so it suffices to use
`Gamma=(x2,x3)`.

## 2. Coverage of the full quartic equation

On the affine blowup chart set

    a=x1/x0, y=x2/x0, b=x3/x2.

The actual lifted curve is `(a,b,y)=(r,r,r^3)` and the exceptional
surface is `y=0`. Its only Gamma-contact is `a=0`, of length three.
The ideal identity

    I(C0) intersect (x2,x3)^2=(q*x2,q*x3,D)

gives every quartic as `q Q+D L0`, where `Q in (x2,x3)_2` and L0 is
linear. The restriction of the full strict-transform equation to E is

    P(a,b)=(b-a)[a0+a1*a+(b0+b1*a)*b]
             -a*b^2*(c0+c1*a).

Every positive horizontal coefficient of Z must map to the sole
Gamma-contact: the pullback of the actual mate has no zero outside the
image of c. Since the horizontal coefficients sum to `K.Z=1`, exactly
one horizontal image H0 over `a=0` has positive coefficient, equal to
one. Other horizontal coefficients can be zero and are retained.
The condition `P(0,b)=0` gives `a0=b0=0`, with no extra restriction.
Thus every possible carrier under a mate has the exact equation

    a[(b-a)(a1+b1*b)-b^2(c0+c1*a)]
      +y[(b-a)(A+B1*b+C*b^2)+c0+c1*a-a*b^2(c2+c3*b)]
      +y^2(c2+c3*b)=0.                                  (1)

This preserves the complete third normal order of C0; it is not a
first-normal truncation. The carrier ideal proof is sound: on q the
divisor `C0+2Gamma` has class `(3,3)` and is the divisor of D. The
remaining equal-bidegree section lifts to P3. Subtracting this multiple
of D leaves `q Q`; order two along Gamma forces Q into its ideal.

## 3. The coefficient-zero B and doubled-H0 gap is repaired

At the C-contact, the derivative in y of (1) is c0. If `c0!=0`, T is
smooth there and `c#.H0=1`, because a restricts to r.

If H0 is the only horizontal prime, it must be the special B. This
contradicts `c#.B=0`. It also excludes a doubled H0 component; no
reduced-divisor assumption is needed.

If B is a second horizontal over finite `p!=0`, the identity
`P(p,b)=0` gives

    a1=b1=0, c0+c1*p=0,
    D_T=H0+Hp+2F0.

The case `p=infinity` is essential. In the other Gamma chart its
condition is `a1=b1=c1=0`; nonzero P then gives c0 nonzero and
`D_T=H0+H_infinity+2F0`. Thus it has the same geometry.
H0 is smooth on T everywhere: off b=0 the exceptional restriction is
a reduced smooth component, and at b=0 the y-derivative c0 is nonzero.
Hence there are no attached ADE primes. The other horizontal has
coefficient zero, and all its attached coefficients are zero as well.
The correction equation is therefore `-3 z_H0=-1`, giving `z_H0=1/3`,
contrary to the forced value one.

This covers the formerly dangerous possibility `a1=0,b1=c0!=0`, where
the exceptional divisor contains doubled H0. An early argument that
H0 then had at most one A-chain was unjustified: its normal derivative
can have three zeros. The special-B argument above excludes this case
without that shortcut. The corrected proof has been communicated to
the owner and parent.

Every surviving case consequently has `c0=0`, sole horizontal B=H0,
`z_B=1`, and `c#.B=0`. A distinct horizontal would force c0 nonzero.

## 4. Two distinct residual intersections

If `a1!=0`, the residual divisor on B_T is the global binary quadratic
`b(a1+b1*b)`. It has two distinct zeros, including infinity when b1=0.
At each, the two exceptional-divisor branches are transverse; all
other points of B_T are smooth on T. Relative formal Morse splitting
with the exceptional parameter fixed gives A_n chains with B attached
at an endpoint. The relative splitting has been audited separately in
[the branch-preserving Morse note](OCT10_TRISECANTS_NORMAL_BUNDLE_AND_RIBBONS.md#source-2026-10-10-session-relative-morse-conductor-branches-independent-auditmd).

If the contacted chain has length n and contact node k, and the other
has length m, then

    z_B=((n+1-k)/(n+1)) /
           (3-n/(n+1)-m/(m+1)) <1.

The numerator is below one and the denominator above one for all
lengths. This contradicts `z_B=1`. Reducibility of the residual away
from these two points is irrelevant and is not excluded by fiat.

## 5. Triple residual intersection: actual A/D positions

For `a1=0,b1=u!=0`, put `v=c1,d=c2,e=c3`. The full equation is

    a*b*(u*(b-a)-v*a*b)
      +y*((b-a)*(A+beta*b+gamma*b^2)+v*a-a*b^2*(d+e*b))
      +y^2*(d+e*b)=0.                                   (2)

The restriction of the residual to B_T is the global quadratic `u b^2`;
all singularities of T on B_T lie at the one contact, including the
other b-chart. The audited local cases are exhaustive:

* If A is nonzero, fixing a gives a nondegenerate transverse factorization
  at `a=0`, namely `y*(A b+...+d y)`. Relative Morse splitting therefore
  puts B at an endpoint of an A_n chain. The correction coefficient is
  below one half for every possible contacted node.
* If `A=0,v!=0`, the equation is exactly quadratic in `(a,y)` over
  `k[[b]]`. Factor its nondegenerate binary quadratic and complete its
  two linear terms. One translated coordinate on B has order exactly
  two; the other has finite order m>=2. On C one coordinate has order
  exactly one. Hence the surface is `A_(m+1)`, B meets `E_(n-1)`, and C
  meets `E_1`, in consistent orientation. The inverse Cartan entries give
  `z_B=2/(n+5)<1`. This controls the dangerous internal attachment rather
  than replacing it by an endpoint assumption.
* If `A=v=0,d!=0`, the cubic in the tangent plane is
  `u*a*b*(b-a)`, with three distinct factors. The first blowup has
  precisely three A1 points in those directions. Its resolution is D4;
  B and C meet different outer arms transversely. The inverse D4 entries
  are 1 on an outer diagonal and 1/2 between distinct outer arms, giving
  `z_B=1/4`.
* If `A=v=d=0`, the surface has multiplicity three, incompatible with ADE.

I checked the exact binary-quadratic factorization and branch orders in
the local note, as well as its first blowup formula. The D7 numerical
shield is not a realized parameter case of (2); no arbitrary ADE graph
enumeration is being mistaken for this actual-family computation.

## 6. Doubled horizontal: arbitrary ADE roots are included

The remaining nonzero exceptional polynomial has `a1=b1=0,c1=c!=0` and

    D_T=2B_T+2F0,
    F=-c*a^2*b^2
       +y*((b-a)*(A+B1*b+C*b^2)+c*a-a*b^2*(d+e*b))
       +y^2*(d+e*b).

The normal derivative on B_T is

    h(b)=b*(A+B1*b+C*b^2).

It is a nonzero global section of `O_B(3)`: the relevant line bundle is
`O_B(T-E)`, of degree three. Identical vanishing would make T singular
along all of B_T, contradicting normality. Its zeros, including infinity,
have total multiplicity three.

For an ADE block write `Q=(-E_i.E_j)`, `v_i=B.E_i`,
`g_BB=v^t Q^-1 v`, and at the contacted node j write
`g_BC=v^t Q^-1 e_j`. The equation for B with `z_B=1` is

    sum_blocks g_BB+g_BC=3.                              (3)

At an away-contact root of h of order k, the local divisor is exactly
`div_T(y)=2B_T`. On the crepant resolution choose coordinates `(u,t)`
with B=(u=0), where t is the pulled-back parameter along the smooth
B_T. Write `a=u A0`, `y=u^2 Y0`. Pullback of the hypersurface canonical
generator `da wedge dt/F_y` is a regular unit times `du wedge dt`.
Restricting its coefficient to B gives `A0=unit*h`. Substituting into
the equation and restricting its u^2 coefficient then gives
`Y0=unit*h`, because the coefficient of a^2 is a unit away from b=0.

On the other hand `div_M(y)=2B+sum beta_i E_i` has
`beta=2Q^-1 v`. Restricting its residual divisor to B gives

    2*g_BB=ord(h)=k.                                    (4)

This is an exact equality, valid for arbitrary ADE type, repeated roots,
and multiple attachment points. I independently checked the canonical
residue and divisor arguments; an A-chain-only estimate is unnecessary.

If A is nonzero, both B and C have tangents outside the kernel of the
rank-two Hessian at the contact, since their relevant linear factors
evaluate to A and c, respectively. They meet A_n endpoints. Thus the
contact contribution in (3) is strictly below two; the remaining h-zeros
contribute exactly one by (4), contradicting (3).

If A=0, the contact order of h is k=2 or 3. The exact formal change in
the doubled-horizontal note gives

    X1*Y1=c*b^2*h^2/s^2, s a unit,
    ord_B(X1,Y1)=(k,k+2), ord_C(X1)=1.

Hence the actual contact is `A_(2k+1)`, B meets node k and C an endpoint.
The contact contribution is at most `(k+2)/2`, and all remaining roots
contribute `(3-k)/2`. Their sum is at most `5/2`, contradicting (3).
I verified the formal identities, the exact orders, and this inequality
directly. There is no omitted D/E contact case in this subfamily.

Finally `a1=b1=c1=0` makes P identically zero, giving order at least
three along Gamma, contrary to the accepted genus-two generic order
two. It is not another carrier stratum.

## 7. Verdict and evidence boundary

The cases `c0!=0`, `a1!=0`, `a1=0,b1!=0`, and
`a1=b1=0,c1!=0` exhaust every nonzero exceptional polynomial of the
full quartic family. Their correction equations all contradict the
mate inputs. Reversal covers the opposite endpoint. The endpoint
lambda-one exclusion therefore passes this independent audit.

This verdict rests on the written geometric proof and exact local
identities, not agreement between agents or a finite graph search.
The companion M2 checker of the local triple note supplements those
identities; no execution count is asserted here before inspecting its
separate raw execution record. No computer certificate is used to
replace the arbitrary-degree mate support or arbitrary-ADE argument.

The fixed-curve, characteristic-zero, quartic-carrier, and lambda-one
hypotheses remain essential. The universal STCI question, lambda zero,
and all higher-degree carrier strata remain outside this audit.


---

## Source: 2026-10-10-session-genus-two-endpoint-full-quartic-reduction.md

# Endpoint trisecant: full quartic exhaustion and mate exclusion

Date: 2026-10-10. Author: `trisecant_endpoint_research`.
Status: **PROVED HERE / combined independent audit PASS**. The local
triple and doubled-horizontal proofs have separate written independent
audits. The binding
[full independent coverage verdict](#source-2026-10-10-session-genus-two-endpoint-full-independent-auditmd)
checks the full family exhaustion and all local interfaces. The conclusion
remains scoped to the fixed curve, characteristic zero, the accepted conic
model, and the lambda-one stratum; root canonical acceptance is separate.
No canonical frontier record is edited by this note.

Work over an algebraically closed field of characteristic zero with the
literal curve `C0=[s^4:s^3 t:s t^3:t^4]`. Use the accepted actual normal ADE
strict transform `T` in the blowup of its genus-two conductor line, and the
accepted lambda-one mate reduction:

    f.c#=1,       c#^2=1,       K_M.Z=1,
    c# ~ L-Z,    Z effective rational sigma-exceptional,
    Z.E=-c#.E for every sigma-exceptional prime E.

The special horizontal prime `B` exists, satisfies `B^2=-3`, `f.B=1`,
and `c#.B=0`. There are at most two horizontal primes. Each horizontal
prime has K-degree one and maps in the ambient exceptional surface to
the whole fiber over one point of Gamma. Distinct horizontal primes
give distinct Gamma-fibers. Vertical exceptional primes are (-2) curves
contracted in the crepant ADE resolution `rho:M -> T`.

The actual full quartic family and endpoint coordinates are from
[the carrier ideal proof](2026-10-10-session-genus-two-trisecant-quartic-carriers.md).
Here the conductor line is `Gamma=(x2,x3)`. On the blowup chart put

    a=x1/x0,       y=x2/x0,       b=x3/x2.

The exceptional surface is `y=0`; the lifted curve is exactly
`(a,b,y)=(r,r,r^3)`. The sole point of `Gamma cap C0` is `a=0`, with
scheme length three. This full parametrization, including the third
normal order, is retained throughout.

## 1. The supporting horizontal fiber is forced to lie over a=0

Every positive coefficient of Z lies over the image of c in S. Indeed
pulling back a mate whose zero divisor on S has support c produces
effective exceptional correction only over c. Thus any horizontal
prime with positive Z coefficient maps to the sole Gamma-contact a=0.
Since `K_M.Z=1`, at least one such horizontal exists. As distinct
horizontal primes have distinct Gamma-images, exactly one horizontal
prime, denoted H0 for now, has positive coefficient, and that coefficient
equals one. Every other horizontal prime has coefficient zero.

This argument does not assume that the special prime B has positive
coefficient. A possible special B at a point p different from zero is
retained below.

## 2. Exact full quartic equation after the necessary horizontal factor

Write the degree-four carrier as `F=q Q+D L0`, where
`Q in (x2,x3)_2` and L0 is any linear form. Its strict transform has
exceptional restriction

    P(a,b)=(b-a)[a0+a1*a+(b0+b1*a)*b]
              -a*b^2*(c0+c1*a).

The supporting horizontal fiber H0 requires `P(0,b)=0` identically.
Therefore `a0=b0=0`, and the entire strict-transform equation is

    T: a[(b-a)(a1+b1*b)-b^2(c0+c1*a)]
       +y[(b-a)(A+B1*b+C*b^2)+c0+c1*a
                      -a*b^2(c2+c3*b)]
       +y^2(c2+c3*b)=0.                         (1)

The coefficient named B1 here is a scalar, not the horizontal prime B.
The actual exceptional divisor `D_T=T intersect E` is the full divisor
of P on `P1_Gamma x P1_f`, of class `(2,2)`.

An additional horizontal fiber over a finite `a=p !=0` forces all coefficients
of P(p,b)/p to vanish. Reading the constant, linear, and quadratic
terms in b gives

    a1=0,       b1=0,       c0+c1*p=0.            (2)

In that finite case c1 is nonzero (otherwise P vanishes identically), and

    D_T=H0+Hp+2F0.

The notation F0 denotes the fixed f-fiber b=0. Repeated components are
retained; this is a scheme statement, not only a support statement.

There is also the other Gamma-chart: a horizontal fiber at `p=infinity`
forces `a1=b1=c1=0`. Nonzero P then requires c0 nonzero and gives
`D_T=H0+H_infinity+2F0`. Thus every possible second horizontal, including
infinity, forces c0 nonzero and has the same displayed divisor form.

## 3. All c0 !=0 and coefficient-zero-special-B cases are excluded

At the actual contact `(a,b,y)=(0,0,0)`, equation (1) has
`partial T/partial y=c0`. If c0 is nonzero, T is smooth there, and c#
meets the strict transform of H0 with intersection one, because
`a|c=r` has order one.

If H0 is the only horizontal prime, it is the special prime B. This
contradicts `c#.B=0`. This also covers cases in which H0 occurs twice
in D_T; no reduced-horizontal assumption is being made.

If H0 is not B, the special B must give a second horizontal fiber Hp,
with p different from zero, possibly infinity. The finite and infinite
calculations in section 2 give exactly `D_T=H0+Hp+2F0`.
On H0 the remaining divisor meets only at b=0. Away from that point
the exceptional section of T is reduced smooth H0, so T is smooth.
At b=0 T is smooth by c0 nonzero. Hence H0 has no vertical ADE primes
attached anywhere, including the other f-chart.

The coefficient of Z along Hp is zero by section 1, and positivity
forces all exceptional coefficients attached to Hp to be zero too.
The correction equation for H0 is therefore simply

    -3*coeff_H0(Z)=-c#.H0=-1.

It gives `coeff_H0(Z)=1/3`, contradicting the coefficient one forced
by K_M.Z=1. This excludes the possibility that B has coefficient zero
and another horizontal supplies the mate correction.

Consequently every surviving endpoint configuration satisfies

    c0=0,       H0=B,       coeff_B(Z)=1,
    c#.B=0,    B is the sole horizontal prime.

The last assertion follows from (2): a distinct horizontal would force
c0 nonzero. If the residual contains H0 again, it is a multiplicity
statement about the same sole prime, not a second horizontal prime.

## 4. The a1 !=0 branch has two endpoint A-chains and is excluded

With c0=0 put

    R=(b-a)(a1+b1*b)-c1*a*b^2,       D_T=B_T+R.

Its restriction to B_T is the homogeneous degree-two polynomial
`b(a1+b1*b)`. If a1 is nonzero, this has two distinct zeros on P1_f,
including the zero at b=0; if b1=0, the other zero is at infinity.
At both points the derivative of R along B_T is nonzero. Thus the
exceptional section consists of two transverse branches there, even
if R itself is reducible elsewhere.

Every singularity of T on B_T lies at these two points. Each is an
A_n singularity with B attached to an endpoint of its resolution
chain: formal Morse splitting of `uv+y h` preserves y as parameter.
Let the contacted chain have length n and contact node k; let the
other chain have length m, allowing m=0. The smooth embedded descent
meets exactly one exceptional prime transversely. Solving the
intersection equations gives

    coeff_B(Z)=((n+1-k)/(n+1)) /
                  (3-n/(n+1)-m/(m+1)) <1.

The numerator is strictly below one and the denominator strictly above
one. This contradicts `coeff_B(Z)=1`. No finite chain cutoff and no
irreducibility assumption on R are used.

## 5. The a1=0, b1 !=0 branch is an exact local triple case

The equation becomes

    a*b[b1*(b-a)-c1*a*b]
       +y[(b-a)(A+B1*b+C*b^2)+c1*a-a*b^2(c2+c3*b)]
       +y^2(c2+c3*b)=0.                         (3)

The only intersection of B_T with the residual exceptional divisor is
b=0, of multiplicity two. Thus every singularity of T on B_T is at
this one point. The full local proof is in
[the exact local ADE correction audit](OCT10_BISECTION_AND_ENDPOINT_FOUNDATIONS.md#source-2026-10-10-session-endpoint-local-ade-correction-auditmd).
It preserves the complete polynomial (3) and proves:

* A nonzero: B attaches to an endpoint of an A_n chain, giving its
  correction coefficient below 1/2.
* A=0 and c1 nonzero: exact quadratic factorization over k[[b]] puts
  the surface in `XY=b^(n+1)*unit`. B has factor orders `(n-1,2)`;
  c has orders `(1,n)` in the opposite orientation. The correction
  coefficient is exactly `2/(n+5)`, below one, for n>=3.
* A=c1=0 and c2 nonzero: the ordinary triple cubic after completing
  the square gives precisely D4; B and c meet distinct outer arms.
  The correction coefficient is 1/4.
* A=c1=c2=0: multiplicity is at least three, incompatible with ADE.

The abstract D7 numerical graph shield cannot be imported to this
equation without verifying actual realization. The ordinary triple
cubic here has three distinct factors b1*a*b*(b-a), which gives D4.

## 6. The doubled-horizontal subcase is also excluded

If a1=b1=0, nonzero P requires c1 nonzero, and

    D_T=2B_T+2F0.

Its full actual equation is

    -c1*a^2*b^2
       +y[(b-a)(A+B1*b+C*b^2)+c1*a-a*b^2(c2+c3*b)]
       +y^2(c2+c3*b)=0.                         (4)

The normal coefficient along B_T is the global degree-three section

    h_B(b)=b*(A+B1*b+C*b^2).

Thus additional singular points of T on B_T can occur away from the
contact at the other zeros of h_B, including infinity. The earlier
two-node endpoint-chain shortcut does not apply here. The complete
proof is in
[the doubled-horizontal independent audit](#source-2026-10-10-session-genus-two-endpoint-double-horizontal-independent-auditmd).
Here is its structural calculation.

For an ADE block let Q be its positive Cartan matrix and let v encode
the intersections of B with its exceptional primes. At the contact
block let e_j encode the unique transverse c# contact. Since the B
coefficient is one, the B intersection equation requires

    sum_blocks v^t Q^(-1) v + v^t Q^(-1) e_j =3.      (5)

Away from the contact, write `a=u*A0`, `y=u^2*Y0` on M, with B given
by u=0 and its f-parameter unchanged. Crepancy of the hypersurface
canonical generator `da wedge db/F_y` forces
`A0|B=unit*h_B`. Equation (4) then forces `Y0|B=unit*h_B` as well.
If an away-contact root has multiplicity k, comparison with the
total transform of div(y) gives the exact identity

    2*v^t Q^(-1) v=k.                              (6)

This retains arbitrary ADE types, multiple graph attachments, and
the other f-chart; it does not replace such blocks by A1 points.

If A is nonzero, both B and c have tangent outside the rank-two
quadratic kernel, and hence meet endpoints of the contact A_n chain.
Their combined contribution to (5) is strictly below two. The
remaining degree-two zero divisor of h_B contributes one by (6).
This contradicts (5). As an additional global check, A=c1 would make
T singular along all of the fixed conductor component F0, since
`F_y|F0=a*(c1-A)` and all other partial derivatives vanish there.
It is excluded by normality, independently of the numerical bound.
In fact A nonzero and A different from c1 forces precisely A3:
the quartic term restricted to the quadratic kernel is nonzero.
B and c meet the same endpoint, so the contact contribution is 3/2
and the total bound is 5/2, as detailed in the independent audit.

If A=0, normality leaves `k=ord_0(h_B)` equal to two or three.
The exact quadratic factorization in the independent audit gives
an `A_(2k+1)` contact, with B at node k and c at an endpoint.
The contact contribution to (5) is at most `(k+2)/2`; the other
zeros of h_B have total multiplicity `3-k` and contribute
`(3-k)/2` by (6). Thus the entire left side of (5) is at most
`5/2`, again less than three. This excludes all of (4).

If a1=b1=c1=0, P vanishes identically. The actual quartic then has
generic normal order at least three along Gamma, contrary to the
accepted genus-two generic multiplicity two. It is not another
surviving genus-two carrier stratum.

## 7. Full endpoint conclusion and surviving larger scope

Sections 3--6 exhaust the full eleven-dimensional quartic carrier
family after the necessary supporting-horizontal factor. They exclude
every endpoint-trisecant lambda-one mate for the literal C0 over an
algebraically closed field of characteristic zero, using the accepted
genus-two normal conic model and correction/contact reductions.

The proof explicitly includes a zero coefficient of the special B,
a second horizontal fiber at a finite point or infinity, repeated
horizontal and vertical conductor components, internal A-chain
attachments, D4, arbitrary ADE blocks away from the contact, and
repeated normal-coefficient roots. Neither a tangent-only argument nor
an abstract all-A-chain assumption is used.

This endpoint theorem requires the separate nonendpoint theorem to
close the lambda-one stratum. The lambda-zero stratum requires its
separate double-curve argument. No conclusion about all carrier
degrees, arbitrary integral curves, or the universal STCI problem
follows from this note alone.


---

## Source: 2026-10-10-session-genus-two-lambda-one-marked-prime-audit.md

# Bounded audit: exceptional prime classes in the lambda-one plane marking

Date: 2026-10-10. Auditor: degree-one-anticanonical counteraudit agent.
Status: **PROVED HERE / accepted bounded structural classification**.
No canonical frontier file or computation script was edited. This note
does not exclude the lambda-one stratum or assert that any listed
configuration is realized by an actual quartic normalization or mate.

## 1. Hypotheses and total-transform convention

Work over an algebraically closed field of characteristic zero. Keep
the hypotheses of the accepted genus-two nullcurve audit: sigma:M->S
is a resolution of a normal surface; the nef divisor L is pulled back
from an ample divisor on S; and its complete map is birational onto
the actual integral quartic. In the lambda-one stratum the actual
smooth lifted curve c# maps isomorphically to a smooth embedded curve
c in S. Its complete system supplies a birational morphism

    q:M->P2,

consisting of nine successive point blowups, possibly infinitely near.
The actual c# is a smooth member of class h, mapping to a line that
avoids the blowup centers. Use the total exceptional classes e0,...,e8,
so

    h^2=1, e_i^2=-1, h.e_i=e_i.e_j=0 for i!=j,
    K=-3h+sum_{i=0}^8 e_i,
    L=4h-2e0-sum_{i=1}^8 e_i,
    f=K+L=h-e0,             c#=h.

Every sigma-exceptional prime is assumed already proved to be either
a vertical smooth rational (-2)-curve, with f.E=0, or a horizontal
smooth rational (-3)-section, with f.E=1. There are at most two
horizontal primes, and they are pairwise disjoint. Every such prime
has L.E=0. The classification below starts with these proved inputs.

For a blowup center p_a, let P(a) be the set of later centers lying on
the then-current strict transform of the exceptional curve born at
p_a. These are the centers directly proximate to p_a, not all indirect
descendants. The final prime strict transform is exactly

    F_a=e_a-sum_{j in P(a)} e_j.                 (1)

Each coefficient in this subtraction is one because the strict
exceptional curve remains smooth. A satellite center belongs to two
different sets P(a) and contributes once to each respective formula;
it does not contribute twice to one prime. This follows inductively
from the strict-transform formula for one blowup. For a primary
reference on these conventions and the corresponding proximity
inequalities, see [Calabri--Ciliberto, On Cremona contractibility,
section 2, p. 392, equation (2)](https://seminariomatematico.polito.it/rendiconti/71-34/0.pdf).

## 2. Nefness forces the double center to be proper and controls satellites

Write m0=2 and m_a=1 for a>=1. Formula (1) gives

    L.F_a=m_a-sum_{j in P(a)} m_j >= 0.         (2)

If p0 were infinitely near, it would be proximate to some earlier
center p_a with a!=0. Then L.F_a<=1-2<0, contrary to nefness.
Thus p0 is a proper point of P2. Independent proper-center branches
can be reordered to blow up p0 first. Consequently f=h-e0 is the
actual pulled-back pencil of lines through this proper point.

After this observation every member of P(a) is a simple center. If
r_a=|P(a)|, (2) becomes

    r0<=2,                  r_a<=1 for every a>=1.              (3)

There is at most one satellite center in the entire marking. Indeed,
suppose a center p_j lies at the intersection of two older strict
exceptionals F_a,F_b, with p_a earlier than p_b. Their intersection
could exist only if the creation point p_b lay on the strict transform
of F_a: subsequent blowups can remove an intersection of two old
strict transforms, but cannot create one. Thus both p_b and p_j are
directly proximate to p_a. Inequality (3) forces a=0. Such a satellite
is therefore the second direct child of p0, at the intersection of
the p0 exceptional and the exceptional of its first child p_i.
It exhausts p0's two-child budget; no further satellite is possible.

The branches over all other proper points consist of free chains.
Over p0 there are at most two free branches, or the single pattern

    first child i proximate to 0,
    satellite j proximate to both 0 and i,
    later free chain starting at j.

This is a necessary proximity restriction, without a realizability
assertion for the complete marked linear system.

## 3. Degree-zero exceptional primes

Since p0 is proper, (1) gives

    F_a^2=-1-r_a,
    f.F_0=1,                f.F_a=0 for a>=1,
    L.F_0=2-r0,             L.F_a=1-r_a for a>=1.

Accordingly the degree-zero sigma-exceptional primes have precisely
the following forms, with the proximity relations required by (1):

    R_ab=e_a-e_b,            a,b in {1,...,8}, P(a)={b};
    B_A=e0-e_i-e_j,          A={i,j}=P(0), r0=2.

The R_ab are vertical (-2)-curves. The unique possible B_A is a
horizontal (-3)-section. In particular there cannot be two distinct
degree-zero horizontal primes.

The graph on degree-zero vertical primes alone is a disjoint union
of A-chains: every simple center has at most one direct child, and
the satellite restriction prevents a child from having two simple
parents. For two consecutive chain roots their intersection is one,
and all other distinct roots on that chain have intersection zero.

If p0 has two free children i,j, B_A can attach to the initial root
of each of their two chains. If j is the satellite child of 0 and i,
then

    B_A.R_ij=0,
    B_A.R_jk=1 if the later child k of j exists.

Thus B_A attaches to the second vertex of the chain i->j->k->...,
rather than to R_ij. This can make that second vertical vertex
trivalent if the chain continues. If j has no child, R_ij and B_A
are disjoint components of the degree-zero sigma-exceptional locus.

## 4. Positive plane degree: complete arithmetic classification

If a prime E has d=h.E>0, its plane image is an integral plane curve
of degree d and E is its strict transform. Write

    E=d h-sum_{a=0}^8 b_a e_a,          b_a>=0 integral.         (4)

Here b_a is the actual multiplicity of the successive strict transform
at p_a. This nonnegativity holds for infinitely near and satellite
centers as well. It does not apply to degree-zero F_a: in the notation
of (4), that prime has b_a=-1 at its creation index.

For every positive-degree prime, the additional proximity constraints
are

    b_a >= sum_{j in P(a)} b_j,                              (5)

because E.F_a>=0 for the distinct primes E and F_a. These inequalities
remain necessary after the following arithmetic classification.

If E is vertical, f.E=0 and E^2=-2 give

    b0=d,
    sum_{a=1}^8 b_a=2d,
    sum_{a=1}^8 b_a^2=2.

The last equality forces two entries to be one and all others zero;
their sum then forces d=1. The only possible positive-degree vertical
prime class is therefore

    V_P=h-e0-e_i-e_j,       P={i,j} subset {1,...,8}.          (6)

It is the strict transform of an actual plane line through p0.

If E is horizontal, f.E=1 and E^2=-3 give

    b0=d-1,
    sum_{a=1}^8 b_a=2d+2,
    sum_{a=1}^8 b_a^2=2d+2.

Nonnegative integrality forces every b_a for a>=1 to be zero or one.
There are 2d+2 ones among eight entries, so 1<=d<=3. The exhaustive
arithmetic list is

    d=1: h-sum_{a in T} e_a,              |T|=4;
    d=2: 2h-e0-sum_{a in T} e_a,          |T|=6;
    d=3: 3h-2e0-sum_{a=1}^8 e_a.

No prime-effectivity or incidence claim is implicit in this list.
Adjunction imposes no extra equation here: K.E=f.E follows from
L.E=0 and f=K+L, and the displayed squares already give genus zero.

## 5. Embedded smoothness excludes the conic and cubic and limits components

The assumption that c#->c is an isomorphism to a smooth embedded
curve supplies more than a numerical divisor identity. Let p be a
singular point of S lying on c, and P the unique point of c# above p.
Choose a local function a in the maximal ideal of O_(S,p) whose
restriction to c is a uniformizer; such a function exists because
O_(S,p)->O_(c,p) is surjective. Its pullback has positive order along
every exceptional prime above p. The smooth local ring O_(M,P) is
factorial. Restriction to c# has order exactly one, hence

    1 >= sum of local intersection multiplicities of c#
         with exceptional branches through P.

It follows that exactly one exceptional prime passes through P,
that c# meets it transversely, and that no other point of that
exceptional fiber meets c#. Every connected exceptional graph is
contained in one fiber of sigma; thus it has at most one vertex E
with c#.E>0. In particular

    h.E=c#.E is either zero or one for every exceptional prime.

The horizontal conic and cubic in section 4 have h-degree two and
three and are excluded. All surviving positive-degree exceptional
primes are therefore plane lines: (6), with square -2, or

    H_T=h-sum_{a in T} e_a,              |T|=4, square -3.     (7)

Each connected sigma-exceptional graph has at most one such line
vertex. Consequently distinct positive-degree exceptional primes
are pairwise disjoint, and they cannot be connected even through
degree-zero exceptional vertices.

## 6. Explicit necessary intersection and graph restrictions

For a chain root R_ab=e_a-e_b, intersections with V_P,H_T,B_A are

    V_P.R_ab = 1_(a in P)-1_(b in P),
    H_T.R_ab = 1_(a in T)-1_(b in T),
    B_A.R_ab = 1_(a in A)-1_(b in A).

They must be nonnegative; an entry one gives a single transverse
intersection because both primes are smooth. This enforces the
prefix conditions along the corresponding proximity chains. The
complete root-root formula is

    R_ab.R_cd=-delta_ac+delta_ad+delta_bc-delta_bd.

For distinct positive-degree vertices, the preceding disjointness
condition gives

    V_P.V_Q=-|P intersection Q|=0,
    H_T.V_P=1-|T intersection P|=0,
    H_T.H_U=1-|T intersection U|=0.

Thus vertical line supports are pairwise disjoint, each horizontal
line support meets each vertical line support in exactly one index,
and two horizontal line supports meet in exactly one index. There
are at most four positive-degree vertical primes, because their
two-element supports are disjoint in an eight-element set. This is
an upper bound, not an existence statement.

For the possible degree-zero horizontal B_A,

    B_A.V_P=1-|A intersection P| >=0,
    B_A.H_T=-|A intersection T|=0.

The second equality is forced already by nonnegative prime
intersection, consistently with horizontal disjointness. More
strongly, (5) and the zero multiplicity of H_T at p0 show that H_T
passes through no center above p0. Its exceptional graph component
therefore contains no B_A. A component containing B_A may contain
at most one positive-degree vertical line. Two or more V_P with
A intersection P empty would each meet B_A and violate this rule.

There is at most one B_A and at most two horizontal vertices in
total. If B_A exists, at most one H_T can exist; otherwise at most
two H_T can exist. Distinct horizontal vertices have no direct edge.
Each final graph is assembled from the degree-zero chains and the
possible B_A described in section 3, with at most one plane-line
vertex per connected component. Every edge permitted by the marked
intersection formulas has multiplicity one. A horizontal section
also meets at most one component of any given f-fiber, at a smooth
point of that fiber, since its total fiber intersection is one.

## 7. Caveats, useful counterexamples to shortcuts, and freeze boundary

The formula subtracting all descendants is false. In a free chain
p_b proximate to p_a, p_c proximate only to p_b, the final strict
transform of the a-exceptional has class e_a-e_b, not e_a-e_b-e_c.
At the allowed satellite pattern j proximate to 0 and i, the classes
are e0-e_i-e_j and e_i-e_j, with intersection zero; coefficient two
at e_j in either individual prime would be incorrect. These are
local blowup illustrations of the formulas, not claimed realized
quartic configurations.

Applying nonnegative b_a to degree-zero primes would likewise be
incorrect. Applying h.E<=1 using only numerical equivalence c#=h,
without the smooth embedded curve and isomorphism hypotheses, would
also be unjustified. Those geometric hypotheses are essential to
section 5.

The class list, proper-double-center conclusion, proximity budget,
at-most-one-satellite restriction, and graph restrictions are accepted.
The arithmetic class list was independently checked by a second
bounded audit. Agreement is provenance; the proofs are the explicit
intersection and multiplicity arguments above. Actual incidence,
prime effectivity, full graph realization, normalization/conductor
descent, and existence or exclusion of a mate remain separate work.
No lambda-one exclusion is claimed. This note is frozen for the
requested pause closure after its content and hash are reported.


---

## Source: 2026-10-10-session-genus-two-nonendpoint-trisecant-conic-obstruction.md

# Nonendpoint trisecant conductor: a conditional conic-model mate obstruction

Date: 2026-10-10. Author: `trisecant_conic_obstruction`.
Status: **PROVED HERE CONDITIONALLY / parent audit pending**. This is a
complete obstruction for the nonendpoint trisecant position, conditional
on the separate normal-blowup theorem and the already audited
lambda-one special-horizontal-prime reduction. It does not cover the
endpoint triple-contact line, the lambda-zero stratum, or arbitrary
carrier degrees. No canonical frontier file is edited.

## 1. Inputs and exact scope

Use the genus-two notation in the
[adjoint conic model](2026-10-09-session-genus-two-adjoint-conic-model.md).
Assume the proposed
[normal blowup lift](2026-10-10-session-genus-two-blowup-lift-normality-proposed-audit.md)
has passed its separate audit. Thus

    rho:M -> T subset Bl_Gamma(P3),
    T normal Gorenstein with a crepant resolution rho,
    f = the actual planes-through-Gamma pencil,
    D_T = T intersect E is a Cartier divisor,
    E = P1_Gamma x P1_f,       [D_T]=(2,2).

The class convention here gives a fiber over a point of Gamma class
`(1,0)` and a fiber over a point of the pencil class `(0,1)`.
The actual conductor on the finite normalization `S` is a line, with
entire finite-flat degree-two inverse conductor, as proved in the
[conductor audit](GENUS_TWO_ENTIRE_CONDUCTOR_PROOF.md).
The proper birational map `T -> S` contracts exactly the horizontal
sigma-exceptional curves. All other sigma-exceptional primes are the
vertical (-2) curves resolved by rho.

Assume a mate exists in the lambda-one stratum. Then `f.c#=1` and

    c# ~ L-Z,       Z effective rational sigma-exceptional,
    K_M.Z=1,       Z.E=-c#.E for every exceptional prime E.

The accepted
[no-zero-horizontal audit](2026-10-10-session-genus-two-no-zero-horizontal-independent-audit.md)
forces the special horizontal prime

    B=e0-e_i-e_j,       B^2=-3,       f.B=1,       c#.B=0.

There are at most two horizontal primes; any second one is disjoint
from B on M. A horizontal prime maps in E to the entire fiber over
its fixed point on Gamma. Write the image of B as `B_T` and its Gamma
point as `p_B`.

For this note assume Gamma meets C0 in three distinct points. For the
literal rational quartic these are the nonendpoint trisecants: the
ruling lines with fixed `[s^3:t^3]=[alpha:beta]`, where `alpha beta !=0`.
The diagonal automorphisms normalize these to `alpha=beta=1`. The
three contacts then occur at `t^3-s^3=0`, with distinct Gamma coordinates
and distinct f-coordinates. The argument uses only those two
distinctness statements.

## 2. A necessary singleton-fiber test

The image `c_T` of c# in T is a section of the pencil and is isomorphic
to P1. Indeed `f|c#` is degree one, and the image is the section of the
separated morphism `T -> P1` determined by that inverse parameterization.
Thus c_T has only one point over each contact with Gamma.

At a Gamma point lying on C0, the mate polynomial vanishes. It therefore
vanishes at every point of the entire inverse conductor over that point.
Its divisor on S has support only the lifted curve c. In particular,
every point of that conductor fiber must be the point of c over that
Gamma point.

Away from the images of horizontal exceptional curves, `T -> S` is an
isomorphism. Consequently the support of `D_T -> Gamma` over a C0-contact
away from those images must be a singleton. Two distinct points are
impossible. This is a support test on the actual conductor, not an
even-valuation or tangent-only test.

Do not assume at this stage that p_B belongs to C0. The coefficient of
B in the exceptional correction can be zero when another horizontal
prime is present. There are nevertheless at least two C0-contact points
away from p_B, whether p_B is a contact or not.

## 3. Every reducible residual divisor is excluded

Since B_T is a fiber component of D_T, its multiplicity is one or two.

If its multiplicity is two, the remaining divisor has class `(0,2)`.
At least two C0-contact points away from p_B have distinct f-coordinates. Each must
lie in the remaining divisor, so that divisor consists of two distinct
fibers of f. But they give two distinct conductor points over every
Gamma point away from p_B, contradicting section 2. A double f-fiber
cannot contain the two distinct f-contact coordinates.

Now suppose B_T has multiplicity one, and write

    D_T=B_T+R,       [R]=(1,2).

If R is reducible, its components can only have the following classes,
including repetitions:

    (1,1)+(0,1),     or     (1,0)+(0,2).

An irreducible `(1,1)` component is a graph over f and maps isomorphically
to Gamma. Together with an f-fiber it has singleton fibers over at most
one Gamma point: their unique intersection. There are at least two C0-contact
points away from p_B, so the first case fails. Reducibility of the
`(1,1)` component reduces to the second case.

In the second case the `(1,0)` component is another fiber B'_T over
a Gamma point p_B'. If the `(0,2)` part consists of distinct f-fibers,
the third C0-contact away from p_B and p_B' has two inverse points and
fails the support test. If p_B'=p_B, this was already the
multiplicity-two case. The only remaining possibility is

    D_T=B_T+B'_T+2F0,       p_B' != p_B.

If either p_B or p_B' is outside C0, there are at least two contacts
away from both. Their distinct f-coordinates cannot both lie on the
double f-fiber F0. Therefore p_B and p_B' must be two of the three
contacts in this last remaining possibility. The last contact must
have f-coordinate f0. The f-coordinate of the contact over p_B is
different from f0. At that point D_T is locally just the reduced smooth
component B_T: neither B'_T nor F0 passes there. The defining equation
of T restricted to the smooth E therefore has nonzero differential;
T itself is smooth there. Thus c# actually intersects B on M there,
contradicting `c#.B=0`.

This excludes all reducible and nonreduced residual possibilities,
including double f-fibers and double horizontal fibers. It does not
assume that the entire conductor upstairs is reduced.

## 4. Irreducible R forces only two A-chains on B

An irreducible R of class `(1,2)` is a graph over f. Its two quadratic
coefficient polynomials have no common zero (a common factor would give
an f-fiber component), so R is a smooth P1 and `R -> Gamma` has degree
two. It is separable in characteristic zero.

B is then the only horizontal sigma-exceptional prime: any other one
would supply another Gamma-fiber component in D_T. Therefore
`K_M.Z=1` gives `coeff_B(Z)=1`. The mate does vanish on B after
pullback, and full support forces p_B to belong to C0. This conclusion
is used only in the sole-horizontal case, where its coefficient is
positive. The two C0-contact
points away from p_B must be singleton fibers of R by section 2. They
are its two branch values. A separable degree-two map from P1 has total
ramification degree two, so it is unramified over p_B. Thus R meets B_T
in exactly two distinct transverse points.

Every singular point of T on B_T lies at B_T intersect R. At a point
where R is absent, the restriction of the T equation to E has nonzero
differential, so T is smooth. At either transverse intersection choose
formal coordinates `(u,v,r)` in the smooth ambient blowup, with E
given by r=0 and the two components given by u=0 and v=0. The equation
of T is

    uv+r*h(u,v,r)=0.

If singular, its quadratic part has rank at least two because its
u,v minor is nondegenerate. Since T is Du Val, it is of type A_n.
The formal splitting lemma can be made with r as parameter: the
changes in u,v are zero modulo r, giving the usual form
`xy+r^(n+1)=0`. The two curves in r=0 meet the opposite endpoints of
the exceptional A_n chain. This is the standard rank-two A_n form;
compare [Reid's Du Val notes, Table 1 and section 2.2](https://mreid.warwick.ac.uk/surf/more/DuVal.pdf).
In particular D_n and E_n branching is not permitted at these two
transverse intersections.

The sigma-fiber containing B is therefore B(-3), with at most two
endpoint A-chains. There is no length restriction in this argument.

## 5. The correction coefficient is strictly less than one

The contact of c_T with B_T over p_B must be singular on T, because
c#.B=0. Let the A_n chain over this point have nodes 1,...,n, with B
attached at node 1. The smooth embedded lift meets exactly one node k
transversely, with `1<=k<=n`; this is the accepted singleton-contact
and local-uniformizer consequence. It cannot meet the other chain,
since c_T has just its one f-coordinate over p_B. Write the other
chain length as m>=0 (m=0 means there is no second exceptional chain).

Put `a=coeff_B(Z)`. Solving the first A_n chain gives its neighboring
coefficient

    z1 = n/(n+1)*a + (n+1-k)/(n+1).

The neighboring coefficient of the other chain is
`m/(m+1)*a`. The equation `Z.B=-c#.B=0` therefore gives

    a = ((n+1-k)/(n+1)) /
        (3 - n/(n+1) - m/(m+1)) < 1.

The numerator is strictly less than one; the denominator is strictly
greater than one. The inequality holds for every n>=1, m>=0 and every
contact node k, without a finite graph cutoff.

On the other hand B is the sole horizontal prime, all vertical
exceptional primes have K-degree zero, and `K_M.B=1`. Hence

    a=K_M.Z=1,

a contradiction. This excludes the irreducible residual case.

## 6. Boundary and preserved failed shortcuts

Conditional on the exact structural inputs in section 1, no lambda-one
mate exists when the conductor line is a nonendpoint trisecant of C0.
Sections 3--5 cover all residual divisor strata of D_T.

The endpoint triple-contact lines remain outside this argument. Their
single Gamma-contact does not force two distinct branch values of R.
The full lambda-zero and genus-two problems also remain open.

Two tempting shortcuts are deliberately not used. First, c#.B=0 does
not imply c_T avoids B_T: a vertical ADE chain can separate their
strict transforms. Second, the transverse B_T/R intersection need not
be an A1 singularity; completing `uv+r h` can give an arbitrarily long
A_n chain. The all-length correction calculation, rather than an
A1-only calculation, is the obstruction above.
