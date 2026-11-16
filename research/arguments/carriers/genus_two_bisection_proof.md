# Genus-two bisections: the forbidden Cartier double

Over an algebraically closed field of characteristic zero, a genus-two
normalization of an integral quartic containing the fixed
\(C_0=[s^4:s^3t:st^3:t^4]\) cannot have a mate in the
\(\lambda=0\) bisection stratum. The proof constructs the whole Cartier
double on the actual normalization and its global normal map. A local
or first-symbol thickening does not suffice. The case inputs and the
exhaustive all-quartic assembly are in the [carrier proof](quartic_carrier_proof.md).

This proof reuses the independently accepted second-pencil and full
bisection arguments. Its exact derivative calculation is a written proof;
no new numerical execution is claimed.

## 1. The actual second-pencil reduction

Let `X` be an integral nonnormal quartic containing C0, whose
normalization has sectional genus two. Put

    nu:S->X, sigma:M->S, H=nu*O_X(1), L=sigma*H.

The accepted entire-conductor and adjoint inputs give a smooth rational
M, rational singularities on normal S, and

    K_M^2=0, L^2=4, K_M.L=-2,
    f=K_M+L, f^2=0, K_M.f=-2,
    R sigma_*O_M=O_S.

The complete `|f|` is a connected rational pencil. Assume a hypothetical
mate in the bisection lane. Its smooth embedded lift `c_S` is isomorphic
to C0, and its strict transform c on M satisfies

    c^2=0, K_M.c=-2, f.c=2,
    L equivalent_Q to c+Z,

where Z is effective rational, sigma-exceptional, supported on vertical
smooth rational (-2)-curves, and orthogonal to L. Its exceptional
correction is not integral. These hypotheses are precisely the
`lambda=0` lane, not all genus-two mates.

The [second-pencil proof](https://github.com/markluxton1/STCI/blob/2cc61e8ddb8d1fbfe7034285dac65df5b4c2ac75/research/supplements/OCT10_GENUS_TWO_ENDPOINT_AND_BLOWUP_AUDITS.md#source-2026-10-10-session-genus-two-bisection-second-pencil-independent-auditmd):

* `0->O_M->O_M(c)->O_c->0` and rationality give `h0(c)=2` and generation
  everywhere. The Stein factor has genus zero; its finite map to the
  target has degree one since otherwise the complete system has at
  least three sections. Thus `|c|` is a connected rational pencil.
* `(f,c)` is dominant of degree two. Its normal Stein cover W of
  `P1 x P1` is finite flat: normal surface rings are CM, and the finite
  module over the smooth base is locally free. Trace splits the algebra.
  Restriction to each general ruling has upstairs P1, giving branch
  line bundle `O(1,1)`, hence branch class `(2,2)`.
* Finite duality gives `omega_W=phi*O(-1,-1)` and `(-K_W)^2=4`.
  Anti-ampleness of omega and the birational Leray sequence imply
  rational singularities, rather than assuming them from rational
  birationality. Thus W is Gorenstein ADE. Its crepant minimal
  resolution V has `K_V^2=4`, and M is obtained from V by exactly four
  point blowups, including infinitely near centers.
* For the actual integral relative canonical divisor R, the resulting
  equality is `Z+R equivalent_Q to 2f`. Clearing denominators and
  using the complete connected pencil shows this is an actual sum
  of entire fibers, `Z+R=sum q_t F_t`. Intersecting each part with
  K gives `q_t=k_t/2`, where k_t counts the four blowup centers over t.
  In particular

      Z+R=(1/2)sum_t k_t F_t,
      sum_t k_t=4,
      2Z=sum_t k_t F_t-2R.

These equalities retain all component multiplicities and intersection
centers. The total-transform exceptional basis verifies
`K_M.R_t=R_t^2=-k_t` even at infinitely near centers.

Thus 2Z is an integral exceptional divisor. The integral numerical
class `2c+2Z-2L` is trivial on the smooth rational M by the accepted
numerical-to-linear lemma. Pushing the resulting actual linear
equivalence to normal S gives

    2c_S ~ 2H.

This is an actual Cartier equivalence. In particular there is a
nonzero section `Q in H0(S,O_S(2H))` with entire divisor `2c_S`.
The exceptional class has exact order two, so every mate degree is
even. These are normalization statements; Q need not be ambient.

## 2. The characteristic-zero normal bundle

Write `F=(s^4,s^3*t,s*t^3,t^4)`. The tangent and Euler sequences
give `deg N_(C0/P3)=14`. To compute the splitting, twist the conormal
sequence by `O_P1(6)`. A global section of `N^*(6)` is a tuple of
quadratic binary forms

    a_i=A_i s^2+B_i s*t+C_i t^2

satisfying both polynomial identities

    sum_i a_i (partial F_i/partial s)=0,
    sum_i a_i (partial F_i/partial t)=0.

Here the Euler condition `sum a_i F_i=0` follows from the two
derivative conditions since the common degree is four. Conversely
these two derivative identities say the Euler-kernel section maps
to zero in `Omega_P1(6)`. They therefore compute precisely the
global conormal sections, without discarding the points s=0 or t=0.

The coefficients of the first identity, from s^5 to t^5, are

    4A0, 4B0+3A1, 4C0+3B1, 3C1+A2, B2, C2.

Those of the second are

    A1, B1, C1+3A2, 3B2+4A3, 3C2+4B3, 4C3.

The endpoint equations immediately kill ten of the twelve unknowns.
The remaining two satisfy

    3C1+A2=0, C1+3A2=0,

whose determinant is eight. In characteristic zero all twelve
coefficients are zero. Thus `H0(N^*(6))=0`.

By the splitting theorem on P1, write `N=O(a)+O(b)` with a+b=14.
The preceding vanishing implies a,b>=7, hence

    N_(C0/P3)=O_P1(7) direct_sum O_P1(7).

In particular

    Hom(N_(C0/P3)^*, O_P1(-8))=0.

This is a direct exact calculation for the fixed monomial quartic;
it is not an assertion about all rational-quartic projections.

## 3. The actual Cartier double is a ribbon with nilideal O(-8)

Let `R_C=V_S(Q)` be the entire double curve. Since S is a normal
surface, it is CM. Since Q is a section of an invertible sheaf and
is nonzero on integral S, it is a nonzerodivisor. Therefore R_C
is a pure CM curve with support exactly the smooth embedded c_S.
At its generic point the normal surface is a DVR and div(Q)=2c_S,
so R_C has generic length two.

Let J be its nilradical. Generically J has rank one and J^2=0.
The image J^2 in O_(R_C) is thus supported at finitely many points.
A pure CM curve has no nonzero coherent subsheaf supported at
finitely many points, so J^2=0 everywhere. The same argument shows
that J has no finite-support torsion. Hence J is a rank-one
torsion-free O_(c_S)-module, and, since c_S is smooth, is a line
bundle. This proves that the actual full R_C is a ribbon.

The nilideal's degree can be calculated without assuming any
Gorenstein or Q-Gorenstein property of S. The accepted rational
resolution and Riemann--Roch give, for every integer m,

    chi(O_S(mH))=chi(O_M(mL))=1+2m^2+m.

The exact Cartier sequence is

    0->O_S(-2H)->O_S->O_(R_C)->0.

Consequently

    chi(O_(R_C))=1-7=-6.

The reduction sequence `0->J->O_(R_C)->O_(c_S)->0` and
`chi(O_(c_S))=1` imply `chi(J)=-7`. Thus

    J=O_P1(-8).

Equivalently this ribbon has arithmetic genus seven. No formula
for a canonical divisor on non-Gorenstein S entered this argument.

## 4. The actual ambient conormal map gives a contradiction

The actual normalization morphism, followed by the inclusion of X,
restricts to a morphism

    j:R_C -> X -> P3,

whose reduction is the given closed embedding c_S~=C0. The ambient
ideal sheaf `I_(C0/P3)` pulls back into J. Because J^2=0, its square
pulls back to zero. This gives a global O_(C0)-linear homomorphism

    I_(C0/P3)/I_(C0/P3)^2 = N_(C0/P3)^* -> J.

This statement uses the full ribbon, including every point where
normalization can fail to be an immersion. Such points do not
prevent formation of the global conormal map.

The map is nonzero. Indeed the accepted entire conductor is a line
Gamma, while C0 has degree four and is not that line. On the dense
open of C0 outside Gamma, normalization is an isomorphism with X.
There R_C is an actual closed subscheme of X and hence of P3.
For that closed immersion the ambient ideal of the reduced curve
generates its nilideal. Thus the displayed map is generically
surjective onto a line bundle, and in particular nonzero.

Section 2 and Section 3 show simultaneously that the target is
O(-8) and that no nonzero homomorphism to it can exist. This is the
contradiction. Therefore the entire genus-two bisection mate lane
is excluded for the fixed C0 in characteristic zero.

The obstruction is global. A generic/local conormal map exists,
but it cannot extend to the required global nilideal. The proof
does not infer multiplicities from tangent support data; the
Cartier equivalence forces the whole CM ribbon before its
conormal map is used.


---

## Detailed second-pencil and full-fiber weight derivation

### Genus-two bisection double cover and fiber weights

The following derivation gives the second-pencil and fiber-weight formulas under the hypothetical bisection assumptions. The global ribbon obstruction below excludes the bisection lane independently of the local partition analysis.

#### 1. Exact hypotheses and notation

Work over an algebraically closed field of characteristic zero. The
[adjoint model](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-two-adjoint-conic-modelmd) and
[independent mate audit](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-two-nullcurve-mate-independent-auditmd)
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

#### 2. The second complete connected rational pencil

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

#### 3. The Stein cover has branch class (2,2)

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

#### 4. W is an ADE del Pezzo surface, and M has four further blowups

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

#### 5. Rational linear equivalence forces actual whole fibers

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

#### 6. Exact weights count the four blowups

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

#### 7. Missing-lattice parity leaves three partitions

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

#### 8. Scope and a check against an invalid stronger bound

A reduced nodal fiber \(A+B\) on \(V\), with \((-1)\)-components, can be blown up at its node to give \(F=A'+B'+2E,\ R=E,\ Z=(A'+B')/2\), where \(A',B'\) are \((-2)\)-curves. Thus a single blowup can give \(k=1\) and rational weight \(1/2\); one must retain intersection centers and full fiber multiplicities. This local consistency model is not a realized quartic or mate. Fiber counting **alone** excludes none of \([3,1],[2,1,1],[1,1,1,1]\); connectedness, the actual embedded lift, the quartic map, and conductor descent remain separate, as does the \(\lambda=1\) section lane.

---

