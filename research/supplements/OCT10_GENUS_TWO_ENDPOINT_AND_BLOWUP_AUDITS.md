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
[unique-anticanonical-section argument](../chapters/QUARTIC_CARRIER_TECHNICAL_PROOFS.md#15-genus-two-conductor-line-positions-on-the-fixed-quartic)
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
[adjoint model](OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-two-adjoint-conic-modelmd) and
[independent mate audit](OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-two-nullcurve-mate-independent-auditmd)
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
