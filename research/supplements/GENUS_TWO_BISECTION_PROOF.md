# Genus-two bisections: the forbidden Cartier double

Over an algebraically closed field of characteristic zero, a genus-two
normalization of an integral quartic containing the fixed
\(C_0=[s^4:s^3t:st^3:t^4]\) cannot have a mate in the
\(\lambda=0\) bisection stratum. The proof constructs the whole Cartier
double on the actual normalization and its global normal map. A local
or first-symbol thickening does not suffice. The case inputs and the
exhaustive all-quartic assembly are in the [carrier proof](../synthesis/quartic_carrier_proof.md).

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

The [second-pencil proof](OCT10_GENUS_TWO_ENDPOINT_AND_BLOWUP_AUDITS.md#source-2026-10-10-session-genus-two-bisection-second-pencil-independent-auditmd):

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
