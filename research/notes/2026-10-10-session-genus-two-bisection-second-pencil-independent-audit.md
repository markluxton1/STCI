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
