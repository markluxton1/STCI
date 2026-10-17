# Independent continuation audit: the entire genus-two bisection lane is excluded

Date: 2026-10-10. Auditor: `bisection_full_audit`.
Status: **PROVED HERE / independent mathematical audit accepted**.
This note changes no canonical frontier file. It supplies a stronger
structural conclusion than the original requested conductor audit:
**no genus-two quartic mate for the fixed curve can lie in the
`lambda=0` bisection stratum.** The `lambda=1` section stratum, higher
carrier degrees, the unrestricted fixed-curve question, and the universal
STCI question are not settled by this result.

Work throughout over an algebraically closed field of characteristic
zero. The fixed curve and its projective equivalents are

    C0=[s^4:s^3*t:s*t^3:t^4] in P3.

This is a proof with the actual finite normalization, actual Cartier
double, and its full global nilpotent structure. It is not a
first-normal approximation to an unrestricted mate.

## 1. Accepted inputs and the audited second-pencil reduction

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

I independently checked the [second-pencil audit](2026-10-10-session-genus-two-bisection-second-pencil-independent-audit.md):

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

## 2. Independent normal-bundle calculation for the literal C0

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

## 5. The originally requested conductor chain remains valid but weaker

I independently audited Sections 2--4 of the [quadratic-descent note](2026-10-10-session-genus-two-bisection-quadratic-descent.md),
and the [even-fiber exclusion](2026-10-10-session-genus-two-bisection-even-fiber-exclusion.md).
Their necessary reductions are valid. They are superseded as open
mate possibilities by the contradiction above.

The exact normalization sequence gives `h0(S,2H)=11`, against ten
ambient quadratic sections. On the entire conductor

    p_*O_D=O_Gamma (+) O_Gamma(-2), w^2=delta,
    Q|D=m+a w.

The common-conductor square identifies a=0 with ambient descent.
For the section having divisor 2c_S, a=0 would give a quadric mate.
The unique quadric q containing C0 has curve class (1,3), while
X restricts to (4,4), so it cannot be a mate. Thus a!=0 and can
be normalized to one. Q is a nonzerodivisor on D since D is CM
and none of its components, of total degree two, is c_S.

If m=0, the full Q^2 descends to an ambient quartic and yields a
(4,4) mate, excluded by Craighero--Gattazzo. The exact primary
statement is verified in [the source audit](2026-10-10-session-bisection-primary-descent-sources.md):
Proposition 4, printed page 187, over an algebraically closed
field of characteristic different from two and three. The
paper's convention requires reduced surfaces. The descended
quartic here is necessarily integral reduced: every factor would
contain nonplanar C0; a nonintegral degree-four factorization must
therefore consist of its unique quadric q twice, already excluded
by the same divisor-class argument. This supplies the scope guard
required for that citation.

If m!=0, existence of a descended positive power gives the exact
whole-section identity

    m^2=rho*delta,
    rho=((1+zeta)/(1-zeta))^2,
    zeta a root of unity distinct from 1,-1.

The orientation is m^2=rho*delta, not its reciprocal. One can
derive it directly at the generic algebra by dividing the
involuted section by the nonzerodivisor Q. A characteristic-zero
root of unity has no nilpotent correction. The equality extends
over the line because the relevant sheaves are invertible.
It forces a nonzero square delta=r^2 and m=alpha r. The full
conductor is reduced split, with Q restrictions (alpha+1)r and
(alpha-1)r. The ratio condition for descent is

    ((alpha+1)/(alpha-1))^n=1.

Here alpha!=0,+1,-1 and n>=3; these orders were not bounded by
the quadratic algebra alone. This was a necessary reduction,
not an actual surviving surface or mate construction.

For each even positive k_t, the actual Z_t is integral. Its
positive support contains complete exceptional fibers: an
outside zero coefficient adjacent to it would make Z.E>0,
contradicting (c+Z).E=0 and c.E>=0. Hence at a singular point
contacted by c, O(c+Z_p) is a genuine line bundle of degree zero
on every exceptional component. Kollár's Proposition 76(1)
descends it, giving local Cartierness of actual c_S. A smooth
Cartier curve through a surface point forces that local ring
to be regular, a contradiction. The primary theorem and its
proper log minimal resolution hypothesis are checked in the
same source audit; the accepted exceptional (-2)/(-3) curves
have K.E>=0, and any needed log refinement preserves all
degree-zero conditions. Thus every positive k_t is odd, leaving
only [3,1] and [1,1,1,1] before the ribbon obstruction.

The original second-pencil audit's retained [2,1,1] is a valid
earlier weaker snapshot; the even-fiber note supersedes it.
The original quadratic-descent note repeats that weaker table,
so its retained [2,1,1] must not be presented as the latest
necessary blowup list. The present full exclusion supersedes
all of these hypothetical surviving lambda-zero partitions.

## 6. The proposed contact identification also has a valid conditional proof

For completeness, Section 5 of the owner note can be promoted as
a conditional lemma under its hypothetical bisection and split
descent assumptions. It is no longer needed to exclude the lane.

Every exceptional fiber met by c has positive correction and
lies wholly in Supp(Z), by the support-closure argument. Thus
its graph is entirely vertical (-2). In the accepted normal ADE
ambient conic model T these graphs are contracted, while only
horizontal (-3) curves can be contracted by T->S. Therefore S
is ADE near c_S, and in particular Gorenstein there. Its actual
conductor ideal is omega_S and is locally invertible. Hence D
is Cartier near every point of c_S intersecting D.

Let d be its local Cartier equation at such a point. On the
ribbon R_C, d meets the reduction properly and is a
nonzerodivisor on both O_(c_S) and J. Quotienting the ribbon
sequence by d shows

    length(O_(R_C)/(d))=2*length(O_(c_S)/(d)).

In the split conductor algebra with Q=m+w=alpha r+w, the
quotient by Q is locally O_Gamma/(r^2), since alpha^2-1 is
nonzero. Its length at a zero of r is twice the order of r.
These two lengths describe the same scheme R_C intersect D.
The common conductor ideal pulled to c_S is precisely the
ambient ideal of Gamma intersect C0. Its degree is two in
the accepted bisection line-position theorem. Therefore

    div_Gamma(r)=Gamma intersect C0

as entire degree-two schemes, not just as supports. At a
simple contact, Q has order one on each of the smooth split
conductor components; a smooth S would make c_S Cartier and
Q a unit times its squared equation, forcing even order on
each component. Thus each simple contact would be singular
on S. A tangent double contact is not excluded by that
parity observation alone.

The existence of the forced global ribbon, however, has
already contradicted the balanced normal bundle regardless
of these contact types.

## 7. Continuation boundary and evidence

All conclusions above are exact sheaf, divisor, and polynomial
arguments. No sample or bounded search replaces any universal
quantifier in the bisection exclusion. The derivative identities
in Section 2 can be checked independently coefficient by
coefficient, and are included in full for that purpose.

The preserved weaker sources and primary-source audit retain
their own attribution. The current proof introduces no new
Macaulay2 execution count. It is independently checked against
the actual source notes rather than counting parallel-agent
agreement as proof.

The remaining genus-two mate lane is lambda=1, with c^2=1,
f.c=1 and length-three conductor contact. This note supplies
no exclusion there. The full genus-two quartic carrier lane,
unrestricted C0, and universal projective-curve question must
retain exactly their separately audited status.
