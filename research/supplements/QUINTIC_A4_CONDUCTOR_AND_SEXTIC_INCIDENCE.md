# quintic a4 conductor and sextic incidence

## Integration guide: intrinsic contact and actual sextic incidence

The A4 conductor-contact bounds constrain the marked quintic normalization. The sextic incidence calculations then ask whether **actual homogeneous equations** realize the desired contact and residual support. The [quintic carrier structure dossier](QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md) supplies geometric inputs; [the endpoint power-descent analysis](QUINTIC_ENDPOINT_JETS_AND_POWER_DESCENT.md) supplies a separate obstruction mechanism. An intrinsic contact bound, an equation on a normalization, and an ambient sextic are not interchangeable. Keep the audited contact calculations and the incidence-lifting conditions distinct.

---


Permanent complete mathematical dossier. The arguments, calculations, precise scope, corrected formulas and open cases are preserved without asserting any new theorem authority.

---

## 2026-10-14-generalization-quintic-intrinsic-a4-contact-bound

# The remaining Jbar-zero candidates have intrinsic conductor contact at most two

Date: 2026-10-14. Status: **ALL-PARAMETER CONTACT BOUND; independently
audited** in the
[new A4 contact review](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-14-generalization-quintic-intrinsic-a4-contact-independent-audit).
The actual conductor octic and complete
intrinsic A4 target-fiber criterion are accepted inputs. The accepted
all-power exclusion of `G=Jbar=0` is used as a premise, without replaying
its proof. This note does not exclude all `Jbar=0` projections or all
quintic carriers.

## 1. Scope and intrinsic coefficient identities

Use the accepted nonendpoint genus-one quintic A4 normalization family,
with nonzero delta and an actual admissible finite birational projection.
Write `j=Jbar`, retain the actual parameters `a,B,G`, and let F be the
actual primitive conductor octic in target `p=delta/r`. The intrinsic
A4 point is p=0. A mate forces full inverse support, denoted SUP.

The new exact identities are

```
F(0)|_(j=0)=0,
[p]F|_(j=0)=-2 G (delta^2+2B+G)(3delta^2+G)^2,       (1)
[p^2]F|_(j=0,G=-3delta^2)=-108 delta^5(delta^2-B).    (2)
```

Only these two coefficients are needed; the conductor section is not
replaced by first-order normal data. The characteristic-zero scalar
constants and nonzero delta are retained.

The [new coefficient source](../computations/generalization_quintic_intrinsic_a4_contact_2026_10_14.m2)
reads the accepted actual primitive polynomial, extracts these coefficients,
and asserts the displayed literal identities. Its
[captured execution](../validation/2026-10-14-quintic-intrinsic-a4-contact/attempt-01/execution-record.json)
records input/source digests, exit zero and empty stderr. It does not
reconstruct the conductor determinant or replay an accepted verifier.

## 2. Exact A4 contact bound after the accepted G=j=0 closure

Put

```
D0=delta^2/2+B,       L=delta^2+2B+G=2D0+G.
```

The accepted A4 target-fiber criterion for j=0 gives an off-c inverse
point precisely when `D0!=0` and `G=-2D0`. Therefore, whenever j=0 and
G is nonzero, SUP forces

```
L != 0.                                                    (3)
```

Indeed L=0 would give `D0=-G/2!=0` and exactly that forbidden inverse
point. This uses the actual fiber criterion with its nonzero denominator;
the D0=0 exception is not discarded.

Assume j=0 and G is nonzero. If `G+3delta^2!=0`, identity (1) and (3)
give exact conductor contact one at A4. If `G=-3delta^2`, (1) vanishes.
SUP and (3) then force `B!=delta^2`, since B=delta^2 would make L=0.
Identity (2) is consequently nonzero, so the contact is exactly two.
Thus

```
j=0, G!=0, SUP  ==>  ord_A4(F) is exactly 1 or 2.            (4)
```

The accepted theorem already excludes mates on G=j=0. Consequently
**every surviving j=0 mate candidate has intrinsic conductor contact at
most two**. This new argument does not analyze SUP on G=0; that lane is
removed by its separate accepted mate-exclusion proof.

This is one intrinsic contact argument across the whole parameter family.
It is independent of the degree of the common first-symbol gcd and does
not enumerate conductor multiplicity partitions.

## 3. Both values of Jbar satisfy the same h2 norm condition

On the actual h2 locus, the independently reviewed
[conductor--differential factor theorem](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-14-generalization-quintic-h2-conductor-quotient)
gives homogeneous `Fsrc=H Q6` in source coordinates `x=T/S=r/delta`.
The intrinsic point is `S=0`. If H contains that point, the accepted
leading-coefficient equations give G=j=0. That entire mate lane is already
closed. Thus every surviving h2 candidate has H(A4) nonzero.

If j is nonzero, SUP requires Q6 to be supported on H, so necessarily
`Res(H,Q6)=0`.

If j=0 and `Res(H,Q6)!=0`, the permitted support of Q6 consists only
of the additional A4 point. Since Q6 is a nonzero degree-six binary form,

```
Q6 = constant*S^6.
```

As H misses A4, this would give conductor contact exactly six at A4,
contradicting (4). Therefore every surviving h2 mate candidate, for either
value of j, satisfies the single homogeneous necessary condition

```
Res(H,Q6)=0.                                               (5)
```

This removes the pure-A4 exception from the small quadratic-algebra norm
test. On the declared finite inverse-map chart, the saved exact norm
factorization then imposes `N12*N18=0` for j=0 as well as j nonzero.
All denominator, content and actual-projection hypotheses of that capture
remain in force. This is a necessary two-factor incidence, not an
emptiness certificate. The repeated-root and projective infinity charts
remain in the shared homogeneous sextic support system; no inverse
discriminant is used in the proof of (5).


---

## 2026-10-14-generalization-quintic-intrinsic-a4-contact-independent-audit

# Independent audit: intrinsic A4 contact and the h2 common-root condition

Date: 2026-10-14, completed after local midnight on October 15.

Status: **PASS for the new contact bound and the resulting homogeneous
h2 condition Res(H,Q6)=0 on every surviving mate candidate.** This does
not prove the remaining resultant locus empty or prove conductor power
descent.

The reviewed proposal is
[the intrinsic A4 contact-bound note](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-14-generalization-quintic-intrinsic-a4-contact-bound).
The actual conductor octic, the complete A4 target-fiber criterion and
the accepted exclusion of G=Jbar=0 are premises. No accepted verifier
was replayed. This audit checks the new deductions directly and reads
the new coefficient-extraction source and its captured execution.

## 1. Actual A4 fibers force the needed nonvanishing

Work on the accepted admissible finite birational nonendpoint quintic
projection family, in characteristic zero, with delta nonzero. Write
j=Jbar and let SUP mean full inverse support. The accepted A4 target
fiber criterion at j=0 states that an off-c point exists exactly when

    D0=delta^2/2+B is nonzero,       G=-2D0.

For G nonzero, put L=delta^2+2B+G=2D0+G. If L=0, then
D0=-G/2 is nonzero and the displayed criterion produces an actual
off-c point. Thus

    j=0, G nonzero, SUP implies L nonzero.              (1)

This implication respects the D0=0 exception: that exception cannot
occur when L=0 and G is nonzero. No affine/projective denominator is
discarded in the argument.

## 2. Exact contact one or two

Let F(p) be the accepted actual conductor octic, with intrinsic A4
point p=0. The new coefficient identities are

    F(0)|_(j=0)=0,
    [p]F|_(j=0)=-2G L(3delta^2+G)^2,
    [p^2]F|_(j=0,G=-3delta^2)
        =-108delta^5(delta^2-B).                        (2)

The new source reads the accepted primitive polynomial directly and
asserts precisely these identities; it reconstructs neither the
conductor determinant nor the accepted fiber theorem. Its
[attempt-01 execution record](../validation/2026-10-14-quintic-intrinsic-a4-contact/attempt-01/execution-record.json)
records the accepted input digest, source digest, exit zero and empty
stderr. This is a new coefficient-extraction check, not a rerun of an
accepted verifier.

On j=0, G nonzero, SUP, equation (1) makes the factors G and L in
the first coefficient nonzero. If G+3delta^2 is nonzero, F has exact
order one at p=0. If G=-3delta^2, the first coefficient vanishes and

    L=2(B-delta^2),
    [p^2]F=54delta^5 L,                                 (3)

which is nonzero by (1). F therefore has exact order two. Since p is
a uniformizer of the smooth curve C0 at this point and c maps
isomorphically to C0, these orders are the actual conductor-contact
orders on c. Thus the new all-parameter conclusion is

    j=0, G nonzero, SUP implies ord_A4(F) in {1,2}.      (4)

The new argument does not apply (4) to G=0. For mate candidates, that
lane is removed by the separate accepted G=j=0 theorem. Only its
mate-exclusion conclusion is needed here; no new assertion about its
full-support scope is required.

## 3. The h2 resultant condition

Use the independently audited factorization Fsrc=H Q6, with H the
complete homogeneous conormal gcd of degree two, Q6 nonzero of degree
six, and source coordinates x=T/S=r/delta. The intrinsic A4 point
is S=0. The accepted leading-coefficient identities imply

    S divides H implies G=j=0.

Consequently H avoids A4 on all surviving mate candidates after the
accepted G=j=0 closure.

For j nonzero, SUP requires support(Q6) contained in support(H).
A nonzero homogeneous sextic over the algebraically closed field has
a root; hence Q6 and H have a common root and Res(H,Q6)=0.

For j=0, suppose instead that Res(H,Q6) is nonzero. This is the
homogeneous resultant, so H and Q6 have no common projective root,
including infinity and repeated-root cases. SUP permits support(Q6)
only in support(H) together with A4. Disjointness from H therefore
forces

    Q6=c S^6,       c nonzero.

Since H avoids A4, this would give ord_A4(Fsrc)=6. Equation (4)
gives a contradiction. Therefore

    every surviving actual h2 mate candidate satisfies
    Res(H,Q6)=0, for either value of j.                  (5)

This is a necessary incidence condition. It does not assert that the
quadratic and sextic have precisely one common root, that any root is
simple, or that conductor support or descent follows from the
resultant. On a rational finite inverse-map chart, a previously
captured exact factorization of this resultant may now be imposed
for j=0 as well as j nonzero, subject to that capture's denominator,
content and projection restrictions. No boundary chart is eliminated
by the proof of (5).

The accepted proofs remain premises. The new mathematical content
reviewed here consists only of (1), the deductions (3)-(5) from the
literal new coefficients, and their precise geometric scope.


---

## 2026-10-14-generalization-quintic-h2-conductor-quotient

# The degree-two first-symbol divisor divides the actual conductor octic

Date: 2026-10-14. Owner: `quintic_shared_incidence/support_structural`.
Status: **THE HOMOGENEOUS FACTOR, SEXTIC INCIDENCE AND HESSIAN CRITERION
PASS [INDEPENDENT REVIEW](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-14-generalization-quintic-h2-conductor-factor-independent-audit).
THE NEW NORM REDUCTION IN SECTION 6 HAS CAPTURED EXACT ARITHMETIC;
ITS INDEPENDENT REVIEW IS PENDING.**
Accepted conormal charts, the actual conductor theorem, the complete
homogeneous h=2 cover, and the A4 conductor value are premises. No
accepted certificate has been replayed. This note neither excludes the
remaining quintic lane nor proves conductor power descent.

## 1. Common coordinates and statement

Work over an algebraically closed field of characteristic zero, on an
actual admissible finite birational nonendpoint projection in the
accepted genus-one A4 quintic family, with `delta!=0`. Write

    z=r/delta=t/s,       p=delta/r=s/t.

The actual source-coordinate octic is therefore

    F_z(1,z)=z^8 Fdet(1/z,1).

Here `Fdet` is the accepted actual homogeneous conductor restriction,
not an affine norm with its extraneous leading factors. Let `H(s,t)`
be the complete homogeneous gcd of the corrected conormal cubics in
the same source coordinate, and assume `degree H=2`. Then

    H divides F_z as homogeneous binary forms.                 (1)

In particular there is a nonzero homogeneous sextic `Q=F_z/H`, and

    supp(F_z) subset supp(H*s^epsilon)
      iff supp(Q) subset supp(H*s^epsilon),                    (2)

where the intrinsic A4 point is `s=0`, and `epsilon=1` if the actual
`Jbar` is zero and `epsilon=0` otherwise. This keeps the intrinsic
exceptional point in exactly the accepted support bridge.

The coordinate binding matters. Earlier saved coefficients `c_i`
describe `B(u)=Fdet(1-u,1)`, after substituting the finite h=2 coefficient
map. They convert to the actual source-coordinate form by the exact
binary transformation

    F_z(1,z)=sum_(i=0)^8 c_i (z-1)^i z^(8-i).                 (3)

Thus the old `B` coefficient array must not be paired directly with
`H=z^2+v*z+w`. The corrected capture is
`validation/2026-10-14-quintic-logarithmic-support/attempt-05-correct-coordinate/`.
Its subsequent sextic quotient capture is owned by the shared-incidence
parent, not reconstructed here.

## 2. The conductor annihilates the relative differentials

Let `A subset B` be a finite birational ring extension, and let `I`
be its conductor, considered as an ideal of both rings. Then

    I * Omega_(B/A)=0.                                       (4)

Indeed, for `c in I` and `b in B`, both `c` and `cb` belong to `A`, so
in the relative differential module

    c db = d(cb)-b dc = 0.

Since differentials `db` generate, this proves (4). The identity
localizes and remains true after tensoring with a quotient of `B`.
It uses the actual conductor ideal, including its nonreduced structure.

Now consider a smooth source point of `c`. The accepted two conormal
charts supply local source coordinates `(u,T)` with `c:T=0`, a target
curve parameter `y` with nonzero derivative in `u`, and target normal
coordinates `U,V` vanishing along `C0`. Restricted to `c`,

    dy = alpha du + beta dT,   alpha a unit,
    dU = u1 dT,               dV = v1 dT.

The target affine coordinate differentials are generated by
`dy,dU,dV`; any hypersurface relation among them changes no image.
Eliminating `du` with `dy` gives the exact local module description

    Omega_(S/X) tensor O_c = O_c/(u1,v1) * dT,                (5)

up to its harmless local line-bundle frame. The accepted formulas
identify `(u1,v1)` with the ideal generated by the two corrected
conormal symbols, after multiplying by units. This includes the
opposite target chart at `r=0`. In the DVR of the smooth curve at the
point, that ideal is generated by their gcd, with its full order.

The actual upstairs conductor is locally generated by its defining
section. Apply (4), then tensor with `O_c`. Its restriction `F_z`
annihilates (5), hence belongs to `(u1,v1)`. Therefore, at every smooth
source point,

    ord(F_z) >= min(ord(P),ord(J)) = ord(H).                  (6)

This is a lower bound supplied by the relative differential module.
It gives no upper bound on conductor contact and does not identify
the conductor divisor with the first-symbol divisor.

## 3. The possible A4 factor and homogeneous divisibility

The only point of `c` outside those smooth source charts is the
intrinsic A4 point `r=infinity`, equivalently `z=infinity` or `s=0`.
The accepted complete h=2 cover proves that double infinity is
impossible. Thus its multiplicity in `H` is either zero or one.

If infinity belongs to `H`, the leading coefficients of both corrected
source cubics vanish. The accepted literal cubics then give

    g=3b-2a,             d=4b-3a,
    Jbar=d-2g+2b-a=0.

The accepted exact conductor value

    Fdet(0,1)=-3 Jbar Delta1

therefore vanishes. It supplies at least the one conductor zero
required by the simple factor `s` of `H`. Combining this with (6)
at every other point proves homogeneous divisibility (1), including
all repeated finite factors and every h=2 infinity-once parameter.
No determinant of the finite coefficient system is inverted in this
proof. Its exceptional repeated-factor locus is retained.

The finite monic cover provides a small supporting identity on its
rational inverse chart: apply (3) to its saved exact coefficient array
and divide by the monic `z^2+v*z+w`. The remainder is exactly zero and
the quotient has affine degree six and coefficient content one. This
new arithmetic observation agrees with (1); the written differential
proof supplies the larger chart scope. No arithmetic observation is
being promoted to an admissibility theorem.

## 4. One sextic support incidence, with the A4 allowance

For a binary form `K`, put

    D_K=(partial_t K) partial_s-(partial_s K) partial_t.

The characteristic-zero logarithmic-support lemma in the
[shared support note](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-14-generalization-quintic-logarithmic-conductor-support)
implies that support in a fixed quadratic `H` is equivalent to
being an eigenvector of `D_H`. Since `D_H H=0`, (1) gives

    D_H F_z=H D_H Q.

Thus, wherever no extra A4 point is permitted, the complete support
condition is the seven-dimensional representation equation

    D_H Q=mu Q.                                              (7)

For `H=a*s^2+b*s*t+c*t^2`, put `Delta=b^2-4ac`. The characteristic
polynomial on degree-six binary forms is

    mu (mu^2-4Delta)(mu^2-16Delta)(mu^2-36Delta).              (8)

This remains `mu^7` on the repeated-root boundary. It follows from
the standard two-dimensional matrix with square `Delta*Id`, then
its sixth symmetric power; no octic root-multiplicity partition has
to be enumerated.

For the entire intrinsic A4 allowance use, with `j=Jbar`,

    D_(sH) Q=L1 Q,          degree L1=1,
    j D_H Q=mu Q,           mu a scalar.                     (9)

When `j!=0`, the second equation is exactly support in `H`; the
first is then automatic. When `j=0`, nonzero `Q` forces `mu=0`,
and the first permits precisely support in `sH`. This is a single
homogeneous incidence over the whole h=2 locus, without inverting
`j`, the discriminant, or a leading coefficient. Note that

    D_(sH)(H Q)=H*(D_(sH)Q-H_t Q),

so the linear eigenfactor of the original octic shifts when one
passes to the sextic. Reapplying the support lemma to `Q` avoids
any implicit identification of those two linear factors.

On `s=1`, write `H=z^2+v*z+w` and `Q=sum_(i=0)^6 q_i*z^i`.
The quadratic action coefficients are

    d_i=(6-2i)v q_i+(14-2i)q_(i-1)-2(i+1)w q_(i+1),

and the cubic `sH` action coefficients are

    e_i=(6-3i)v q_i+(15-3i)q_(i-1)-3(i+1)w q_(i+1),

with out-of-range coefficients zero. The former runs through degree
six and the latter through degree seven. These formulas retain
fixed-degree leading drops.

## 5. An independent Hessian covariant for j nonzero

There is a second uniform formulation that uses (1). For any nonzero
quadratic `H` and nonzero octic `F=H Q`, in characteristic zero,

    supp(F) subset supp(H)
      iff J(Hess(F),Q)=0,                                   (10)

where `Hess(F)=F_ss F_tt-F_st^2` and
`J(A,B)=A_s B_t-A_t B_s`. This is one binary covariant identity,
including the double-root degeneration of `H`.

To prove it, put `A=Hess(F)`, of degree twelve. Since `Q` has
degree six, the identity `J(A,Q)=0` means

    A=kappa Q^2                                            (11)

for a scalar `kappa`. Indeed, after dehomogenizing, the Jacobian is
six times `q a'-2a q'`, up to the nonzero homogeneous frame, so
the rational function `a/q^2` has derivative zero. The field has
characteristic zero.

If `L` were a root of `F` outside `H`, of multiplicity `e`, then
`1<=e<=6` because `H|F`. At that root, `Q^2` has order `2e`,
whereas `Hess(F)` has exact order `2e-2`. For example, for
`F(s,t)=t^8 f(s/t)`,

    Hess(F)(z,1)=7*(8 f f''-7(f')^2).

If `f=z^e u`, `u(0)!=0`, its leading coefficient is
`7e(e-8)u(0)^2`, which is nonzero. This contradicts (11), also
when `kappa=0`.

Conversely, if `H` has two distinct roots `H=L M` and support holds,
write `F=c L^a M^b`, with `a,b>=1` and `a+b=8`. Direct
differentiation gives the homogeneous identity

    Hess(F)=7ab Hess(H) Q^2.

If `H` has a double root, support forces `F` to be an eighth power
of that root and its Hessian is zero. Both cases give (10).
This proof uses no case list of possible exponents.

Equivalently, the quotient-free identity is

    H J(Hess(F),F)-F J(Hess(F),H)=0,                         (12)

because its left side is `H^2 J(Hess(F),Q)`. It is stronger to
retain the lower-degree equation (7) for computation; (10) is a
coordinate-invariant independent formulation. For `j=0` with an
extra allowed A4 point outside `H`, use (9), not (10).

## 6. One quadratic-algebra norm gives a small necessary reduction

This section concerns the finite monic inverse-map chart of the shared
coefficient capture, with its determinant, denominators, removed common
content, and nonzero conductor condition retained. It is additional
new arithmetic and was not part of the structural review cited above.

In the quadratic algebra `A=k[z]/(z^2+v*z+w)`, write the remainder
of the captured sextic `Q` as `r0+r1*z`. Its norm is

    Norm_A(r0+r1*z)=r0^2-v*r0*r1+w*r1^2=Res_z(H,Q).          (13)

This determinant formula holds whether or not `H` is squarefree.
The new exact calculation finds

    gcd(r0,r1)=D,
    D=(v^2-4w)*(v^2+6vw+6w^2+2w),
    Res_z(H,Q)=D^2*N12*N18,                                 (14)

where `N12,N18` are saved explicit parameter polynomials of total
degrees twelve and eighteen. The source asserts the literal product
identity, the two factor degrees and their exponent one. The saved
factor files are sufficient to inspect the factors without listing
their long expansions here.

When `j!=0`, the required support is only `H`. Since `Q` is a nonzero
degree-six binary form, support in the finite monic `H` implies that
`H,Q` share a root. Thus on the declared `D!=0` chart,

    support(Q) subset support(H) implies N12*N18=0.           (15)

The two-factor condition is a necessary reduction, not an equivalent
support test. In particular it retains parameter families with only
one accidental shared root and does not assert that every remaining
sextic root belongs to `H`. When `j=0` permits the additional A4 point,
`Q` could be supported entirely at that point; then (15) is not
necessary and is not imposed. The full homogeneous equations (9)
remain the uniform support criterion in that case and on the
exceptional coefficient-map charts.

To determine whether an existing open condition removes either
factor, the new source also computes the actual rational h=2
cofactor map and verifies

    gcd(N12*N18, numerator(A*Dcofactor-Bcofactor*C))=1,
    gcd(N12*N18, numerator(Jbar))=1,
    gcd(N12*N18, numerator(G))=1,
    gcd(N12*N18, numerator(Delta1))=1.

Consequently these known parameter numerators do not remove either
whole factor. This does not prove existence of admissible points on
their zero loci.

The new
[bounded norm source](../computations/generalization_quintic_h2_quotient_norm_2026_10_14.m2)
reuses only the authoritative new sextic from
`attempt-06-sextic-quotient/Q-sextic.txt`; no octic construction or
accepted verifier is replayed. Its
[captured execution](../validation/2026-10-14-quintic-h2-quotient-norm/attempt-01/execution-record.json)
has exit zero and empty stderr and stores the source/input digests,
literal factors, primitive remainder, parameter numerators, and all
four exact gcd values. No incidence elimination was launched.

## 7. Exact scope and next obligation

The structural conclusion proved here is the full first-symbol
factor `H|F_z` on the actual h=2 quintic locus and a corresponding
sextic logarithmic support incidence. It does not prove that the
sextic incidence is empty. The actual center conditions, full inverse
support, exceptional target fibers, integral residual, higher contact,
and nonlinear conductor power descent remain separate requirements.
No global quintic exclusion follows merely from the quotient or
from its representation-theoretic spectral polynomial.


---

## 2026-10-14-generalization-quintic-h2-conductor-factor-independent-audit

# Independent audit: the h2 conductor factor and the sextic incidence

Date: 2026-10-14, completed after local midnight on October 15.

Status: **PASS for the new homogeneous divisibility H|Fsrc, including
full repeated finite-root multiplicity and the infinity-once chart;
PASS for the reciprocal coordinate correction, sextic support incidence,
and its product-action formulas.** The supplementary Hessian criterion
in section 5 of the proposed quotient note also passes a separate
independent calculation. These are new structural reductions, not a
quintic exclusion, an empty-locus certificate, or a conductor-descent
theorem.

The principal reviewed statements are in
[the h2 conductor-quotient note](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-14-generalization-quintic-h2-conductor-quotient)
and [the corrected-coordinate sextic-incidence note](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-14-generalization-quintic-h2-coordinate-correction-and-sextic-incidence).
The accepted actual conductor theorem, corrected two conormal charts,
complete homogeneous h2 cover, and exact A4 conductor value are premises.
No accepted proof or CAS certificate was replayed. The new attempt05 and
attempt06 source files and their recorded exit-zero executions were read;
the mathematical implications below are proved independently of those
executions.

## 1. The actual restricted differential module

For any ring inclusion A into B with conductor I, one has

    I Omega_(B/A)=0.                                      (1)

For a in I and b in B, both a and ab belong to A, so
a db=d(ab)-b da=0 in the relative differential module. The db generate
that module. This argument holds before source localization and hence
also after localizing at any source point or tensoring with the curve.
In particular it does not require a singleton normalization fiber or
the full inverse-support hypothesis.

Let q be a finite point of the accepted source curve c. The source
surface is smooth there with regular parameters (u,T), where c is T=0.
The map c to C0 is an isomorphism. Choose a target curve parameter y
and balanced target normal coordinates U,V. Their pullbacks restricted
to c have differentials

    dy=alpha du+beta dT,       alpha a unit,
    dU=u1 dT,                 dV=v1 dT.                  (2)

The normal derivatives have no du contribution because U and V vanish
identically on c. The target coordinates (y,U,V) form a regular ambient
coordinate system: the balanced replacement of the two normal
coordinates is triangular with invertible linear part. Thus the image
of the pulled-back target cotangent module is generated by the three
displayed differentials. Passing from ambient cotangents to those of
the hypersurface introduces relations among these generators but does
not change their image in the source cotangent module.

After tensoring the cotangent cokernel with O_c, eliminating du by dy
gives the exact local description

    Omega_(S/X) tensor O_c
        = O_c/(u1,v1) times the local normal frame dT.   (3)

This is a cokernel computation; no left-exactness of tensor product is
being assumed. The accepted explicit conormal formulas give

    V_T=P(r)/r^7,       U_T=J(r)/(2r^7)

where r is nonzero. At r=0 the accepted opposite chart replaces r^7
by (r-delta)^7 and interchanges the two components by nonzero constant
factors. Since delta is nonzero, these cover every finite source
point with unit denominators. Replacing r by delta*x also multiplies
the normalized cubic pair by units. Consequently (u1,v1) is precisely
the local ideal generated by the two corrected cubic sections.

In the DVR O_(c,q), its order is the full minimum of the two cubic
orders. This includes a repeated common root and gives

    (u1,v1)=(local equation of H),
    Ann_Oc(Omega_(S/X) tensor O_c)=(u1,v1).             (4)

The accepted actual ambient conductor quadric pulls back to a generator
of the entire upstairs conductor ideal, up to a local unit. Equation
(1), restricted to c, therefore implies

    Fsrc belongs to (u1,v1),
    ord_q(Fsrc) >= ord_q(H).                           (5)

This is a lower bound on the conductor's actual local multiplicity.
It asserts neither equality nor an upper bound, and uses the actual
conductor in addition to first-normal data.

## 2. The intrinsic A4 point and homogeneous divisibility

Use source homogeneous coordinates (S,T) with

    x=r/delta=T/S,         p=delta/r=S/T.

The only source point on c not covered by section 1 is the intrinsic
A4 point S=0. On the complete accepted h2 cover this point occurs in
H at most once: double infinity is impossible. If it occurs, both
cubic leading coefficients vanish, whence

    g=3b-2a,             d=4b-3a,
    j=Jbar=d-2g+2b-a=0.

The accepted exact value Fdet(0,1)=-3 j Delta1 then gives
Fdet(0,1)=0. This is the zero at source S=0, so it supplies at least
the one unit of conductor order required there. No calculation of
relative differentials at the singular A4 point is needed.

Together with (5) at every finite point, this proves

    H divides Fsrc as homogeneous binary forms.        (6)

The accepted nonzero conductor restriction has homogeneous degree
eight. For degree H=2, the quotient Q=Fsrc/H is therefore a nonzero
homogeneous sextic, even when its affine degree drops. The proof uses
no inverse of the finite-cover determinant and hence retains its
repeated-root and infinity-once strata. It only claims (6) for the
actual admissible finite birational quintic projections covered by the
accepted premises; no admissibility claim for an arbitrary coefficient
pair follows.

## 3. Common-coordinate correction

With p=S/T and x=T/S, the common-coordinate binary octic is

    Fsrc(S,T)=Fdet(S,T),
    Fsrc(1,x)=x^8 Fdet(1/x,1).                         (7)

The equality in the first line uses the same ordered homogeneous
variables for the target p coordinate and the reciprocal source x
coordinate. It does not identify their affine parameters. In this
coordinate, the intrinsic A4 point is the linear form Pinf=S, and
source x=0 is target p=infinity.

If the previously captured coefficients describe
B(t)=sum c_i t^i=Fdet(1-t,1), up to their recorded common scalar, then

    Fsrc(1,x)=sum c_i (x-1)^i x^(8-i),
    g_j=(-1)^(8-j) sum_(i=8-j)^8 binomial(i,8-j)c_i.    (8)

Expanding the summands proves the second identity directly. The
inverse polynomial transformation is

    B(t)=(1-t)^8 Fsrc(1,1/(1-t)).                     (9)

Equations (8)-(9) are an invertible constant binary-coordinate
transformation. They preserve all fixed-degree leading drops. They
also preserve a nonzero coefficient vector and its common parameter
content. This confirms the coordinate repair in attempt05; the earlier
attempt04 vector cannot be paired with H=x^2+v*x+w as an actual h2
incidence.

The scalar comparison to the actual octic remains subject to the
original denominator, removed-content and inverse-map restrictions.
An invertible coordinate transformation does not extend that rational
map to its exceptional boundary.

## 4. Sextic support equations and exact coefficient signs

Since H is nonzero and (6) holds, support of Fsrc=H Q is contained in
support of H Pinf^epsilon precisely when the same holds for Q. This
follows by taking the union of the two supports, and needs no condition
on their intersection or root multiplicities.

For K a nonzero binary form, put

    D_K=K_T partial_S-K_S partial_T.

The independently audited characteristic-zero Hamiltonian criterion
says that support of a nonzero Q lies in K precisely when Q divides
D_K Q. Applying it to quadratic H and cubic H Pinf gives one incidence
for the complete A4 allowance:

    D_(H Pinf) Q=L Q,       L homogeneous of degree one,
    j D_H Q=mu Q,          mu a scalar.                (10)

For j nonzero the second equation forces support in H, and the first
then holds automatically. For j=0, Q nonzero forces mu=0, and the
first equation permits precisely support in H Pinf. This includes a
repeated H, Pinf already dividing H, and infinity. The statement is
about geometric points over the characteristic-zero field, with H and
Q nonzero; it does not assert a witness-lifting theorem over arbitrary
nonreduced parameter bases.

The product rules have a necessary correction term in the cubic case:

    D_H(H Q)=H D_H Q,
    D_(PH)(H Q)=H[D_(PH)Q-(D_H P)Q].                 (11)

Indeed D_(PH)=P D_H+H D_P and D_P H=-D_H P. For P=S,
D_H P=H_T, so the correction is -H_T Q. It is a linear multiple of
Q and is absorbed in the unrestricted L of (10). The linear quotient
for the original octic and that for the sextic must therefore not be
identified without this shift.

For a binary form of degree n, dehomogenization on S=1 gives

    D_K Q=n k'(x)q(x)-degree(K) k(x)q'(x).           (12)

Use n=6 and H(1,x)=x^2+vx+w. For q_i=0 outside 0 through 6, the
quadratic action has coefficients

    d_i=(6-2i)v q_i+(14-2i)q_(i-1)-2(i+1)w q_(i+1),

and the cubic action for P=S has coefficients

    e_i=(6-3i)v q_i+(15-3i)q_(i-1)-3(i+1)w q_(i+1).

These are exactly the attempt06 formulas, with d through degree six
and e through degree seven. In particular the cubic uses homogeneous
degree three despite its affine polynomial being the same H(x).
The product rules in that source are exactly (11) dehomogenized.

The quadratic action on Sym^6 has characteristic polynomial

    mu*(mu^2-4Delta)*(mu^2-16Delta)*(mu^2-36Delta),
    Delta=v^2-4w.

This follows from eigenvalues 1 and -1 times a square root of Delta
on the two-dimensional representation and the seven weights of its
sixth symmetric power. Polynomial continuation gives the same formula
at Delta=0, where it is mu^7. This identity is not an eigenvector
existence or incidence-emptiness assertion for the actual family.

## 5. Supplementary Hessian criterion

The additional proposed criterion, independently checked in a separate
worker calculation, is also valid. Let A=Hess(Fsrc), a degree-twelve
form, and Q=Fsrc/H a degree-six form. Then

    J(A,Q)=0 iff A=kappa Q^2 for a scalar kappa.        (13)

After dehomogenizing, the Jacobian is six times q*a'-2a*q', so its
vanishing says the rational function a/q^2 has derivative zero. In
characteristic zero this function is constant; the case A=0 is
included. If Fsrc has a root outside H of order e, then 1<=e<=6,
while Q has order e. The Hessian has exact order 2e-2 there: for
f=z^e u with u(0) nonzero, its first nonzero coefficient in

    Hess(Fsrc)(z,1)=7*[8 f f''-7(f')^2]

is 7e(e-8)u(0)^2, which is nonzero. This contradicts (13), including
kappa=0. A linear coordinate change covers infinity; Hessians acquire
only the nonzero factor det(g)^2 and Jacobian vanishing is invariant.

Conversely, if H=lambda L M has distinct roots and support holds,
write Fsrc=c L^a M^b with a+b=8 and a,b>=1. Direct differentiation
gives

    Hess(Fsrc)=7ab Hess(H) Q^2.

The scalar lambda cancels correctly through Q. If H is a square,
support forces Fsrc to be an eighth power and its Hessian vanishes.
Thus J(Hess(Fsrc),Q)=0 is equivalent to support in H. Finally,

    H J(A,Fsrc)-Fsrc J(A,H)=H^2 J(A,Q),

so the displayed quotient-free equation is equivalent in the binary
polynomial domain. As in the proposal, this Hessian condition is only
for support in H; when j=0 permits an extra A4 point outside H, use
(10).

## 6. Evidence and acceptance boundary

The new
[attempt05 record](../validation/2026-10-14-quintic-logarithmic-support/attempt-05-correct-coordinate/execution-record.json)
records exact forward/inverse coordinate transformations and both
Hamiltonian images, with exit zero and empty stderr. The new
[attempt06 record](../validation/2026-10-14-quintic-logarithmic-support/attempt-06-sextic-quotient/execution-record.json)
records literal Fsrc=H Q and both coefficient/product identities, also
with exit zero and empty stderr. These captures apply to the accepted
finite rational inverse-map open. They support the displayed arithmetic
and do not replace the global written proof of (6).

The remaining mathematical task is to determine the actual geometric
locus satisfying (10), with the original center, fiber and admissibility
conditions, and then the full nonlinear conductor descent. The factor
and sextic incidence do not prove full inverse support, do not solve
power descent, and do not close the quintic lane or the STCI problem.


---

## 2026-10-14-generalization-quintic-logarithmic-conductor-support

# Logarithmic conductor support as one homogeneous representation equation

Date: 2026-10-14. **Coordinate-binding correction:** the attempt02/04
coefficient capture below used p->1-z while the h2 source and actual
octic parameters are reciprocal. Its exact algebraic output is retained
as a failed geometric bridge and must not be used as the actual h2
incidence. The [corrected capture](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-14-generalization-quintic-h2-coordinate-correction-and-sextic-incidence)
now uses z^8 F(1/z) and has passed literal transformation checks.
The general support/eigenvector proof is unaffected.

Status: **PROVED STRUCTURAL LEMMA, with [independent review](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-14-generalization-quintic-logarithmic-support-independent-audit)**. This continues the existing quintic lane without
splitting workers by root partitions. Accepted conductor forms, gcd
covers and previously closed quintic charts are premises. No inherited
certificate is replayed. The new lemma is valid in arbitrary degree;
its quadratic specialization supplies one equation for the remaining
degree-two allowed support, including repeated roots and infinity.

## 1. A power-free support criterion

Let k be algebraically closed of characteristic zero. Let F,H be nonzero
homogeneous binary forms of degrees n>=1 and h>=1. Then

```
supp(div F) subset supp(div H)
  iff F divides H partial_s F and F divides H partial_t F.       (1)
```

This uses projective support and retains the entire divisor of F. At a
root P of F of multiplicity m, a local derivation transverse to P lowers
that multiplicity to m-1, because m is nonzero in characteristic zero.
The two homogeneous coordinate derivatives span that transverse
direction locally. Thus divisibility in (1) forces H(P)=0. Conversely,
if H vanishes at every root, its at least one unit of root valuation
repairs the at most one unit lost by either derivative. This proves both
divisibilities at every linear prime. Unique factorization proves (1).
The argument includes the point at infinity and does not assume F or H
squarefree. In characteristic p the implication can fail at a root whose
multiplicity is divisible by p; no unrestricted positive-characteristic
version is used here.

Equivalently, there are homogeneous forms L_s,L_t of degree h-1 with

```
H partial_s F=L_s F,  H partial_t F=L_t F,
s L_s+t L_t=n H.                                             (2)
```

The last identity is Euler's identity. Thus an arbitrary large power
divisibility or a root-partition enumeration can be replaced by one
finite logarithmic linear system. For h=1, (2) gives the single-root
criterion directly. The forms H and F must remain nonzero; the zero
form is a separate original geometric stratum.

There is an even more economical equivalent condition. Put
`D_H=H_t partial_s-H_s partial_t`, for arbitrary h>=1. Then

```
supp(div F) subset supp(div H) iff F divides D_H F.            (2a)
```

For h>=2 this is `D_H F=L F`, with L homogeneous of degree h-2;
for h=1 it means `D_H F=0`. Indeed, on x=t/s write
H=s^h h(x), F=s^n f(x). The operator becomes
`n h'(x)f(x)-h h(x)f'(x)`. At a root of f not vanishing on h,
the last term has order exactly m-1 and the first at least m.
The degree h and the multiplicity m are nonzero scalars in
characteristic zero. At a root on h both terms have order at
least m. This proves (2a), including all multiplicities. Thus one
homogeneous Hamiltonian equation suffices in every allowed-support
degree.

## 2. For quadratic H, the criterion is a Lie-algebra eigenvector equation

Write H=a s^2+b st+c t^2 and define the degree-zero derivation

```
D_H=(partial_t H) partial_s-(partial_s H) partial_t.
```

It acts on the constant vector space Sym^n(k^2). The induced vector
field on P1 vanishes precisely at div H, since on x=t/s it is
`-2H(1,x) partial_x`. Then (1) is equivalent to

```
D_H F=mu F for some scalar mu in k.                           (3)
```

Indeed (3) makes div F invariant under that vector field. If a root of
F were not a zero of the vector field, its nonzero transverse derivative
would have order m-1 while mu F has order at least m, a contradiction.
Conversely, if the support lies at the zeros of the vector field, the
same valuation argument makes F divide D_H F. Both have degree n, so
their quotient is a scalar. This proof handles a double zero of H and
all multiplicity distributions of F at once.

For any coefficient vector f of F, (3) says exactly

```
rank[ f | D_H f ]<=1.                                       (4)
```

All two-by-two minors of this (n+1)-by-two matrix are one homogeneous
scheme of necessary and sufficient support conditions on the nonzero
F,H locus. No coefficient of F or H is inverted, so this formulation
keeps leading drops and roots at infinity. It is an assertion about
support, not about the full nonreduced conductor or descent.

The operator on the standard two-dimensional representation is

```
[[b,2c],[-2a,-b]],  discriminant Delta=b^2-4ac.
```

For n=8 its characteristic polynomial is

```
mu (mu^2-4Delta)(mu^2-16Delta)(mu^2-36Delta)(mu^2-64Delta).
```

This single representation identity replaces the list of nine possible
root-multiplicity weights. When Delta=0 it remains the nilpotent
identity mu^9; the repeated-root boundary has not been removed.

## 3. A root-free test when H is not specified

The projective stabilizer of a nonzero degree-n binary form F has
positive-dimensional Lie algebra if and only if F has at most two
distinct projective roots. A nonzero projective vector field preserving
its finite root set must vanish at each root and has at most two zeros.
Conversely, a vector field vanishing at the one or two prescribed points
makes F an eigenvector by Section 2. Thus, in characteristic zero,

```
F has at most two distinct roots
 iff rank[ F | s partial_sF-t partial_tF |
                    s partial_tF | t partial_sF ]<=3.        (5)
```

The displayed four columns represent F and a basis of sl2 acting on F.
The first column is nonzero, so a linear dependence supplies a nonzero
Lie-algebra element, not merely a zero multiple of F. This is a
determinantal condition in the original coefficients, with no root
adjoining. It can be used as a preliminary geometric obstruction;
when an allowed quadratic H is already fixed, (4) retains the stronger
requirement that the roots occur at its actual support.

## 4. Application and precise unfinished quintic obligation

In the accepted nonendpoint genus-one A4 quintic model, the actual
binary conductor form has degree eight. Full support requires its roots
to lie in the actual permitted inverse-C0 support, with the intrinsic A4
contribution kept exactly as in the original conductor theorem. Wherever
the remaining permitted form is the homogeneous gcd H of degree two,
the entire support requirement is (3) or (4), after using the actual
coefficient map. If an additional permitted point is present on an
exceptional chart, multiply it into H and use (1)--(2) instead. No
exceptional permitted point is silently discarded to force h=2.

The finite monic quadratic cover used in the new computation only
parameterizes quadratics avoiding its infinity point. Its determinant,
denominators, nonzero conductor condition and all content factors are
recorded. That calculation is an exact coefficient/incidence capture,
not a global quintic exclusion. In particular a leading coefficient
cannot be divided out on the claim that an infinity chart has already
been handled; its precise previously accepted coverage must be cited.

The current next step is to insert the actual octic coefficient map
into the homogeneous eigenvector incidence and prove incompatibility
with the full-support/projection conditions, or exhibit the remaining
geometric family and test its full conductor. The nonlinear logarithmic
conductor defect still has to vanish for any proposed mate. A support
identity alone does not solve descent, and no assertion that the whole
quintic lane is closed is made.

### One incidence keeps the intrinsic A4 allowance as well

Let j be the actual Jbar scalar and let P be the fixed nonzero
linear form of the intrinsic A4 point. The accepted condition is
support(F) contained in support(H) when j!=0 and in support(HP)
when j=0. It is equivalent to the simultaneous equations

```
D_(HP) F=L_1 F,          deg L_1=1,
j D_H F=mu F,           mu a scalar,                        (6)
```

for quadratic H and octic F. When j!=0 the second equation forces
support in H and the first is automatic. When j=0, nonzero F
forces mu=0 and only the first equation remains, allowing exactly
HP. Thus the entire A4 allowance is retained by one polynomial
incidence, rather than splitting work by j=0 or root partitions.
F,H,P must stay nonzero, and all projection/cofactor conditions apply.

For the monic H=z^2+vz+w chart, if F=sum_(i=0)^8 c_i z^i,
the Hamiltonian image has coefficients

```
d_i=(8-2i)v c_i+(18-2i)c_(i-1)-2(i+1)w c_(i+1),
c_(-1)=c_9=0.                                             (7)
```

The [completed coefficient capture](../validation/2026-10-14-quintic-logarithmic-support/attempt-04/execution-record.json)
stores an exact 9-by-two matrix (c,d) for the supplied, incorrectly
coordinate-bound substitution, with exit zero and empty stderr.
It is not an actual h2 geometric certificate. The rational-map calculation
in attempt02 produced all nine coefficients before a later ring-
coercion error; those saved coefficients were reused instead of
reconstructed. Attempt03's sequence/list setup failure is retained
separately. This is new incidence data, not a proof that its rank
locus is empty.

The accepted finite quadratic cover solves four linear equations
for the two cofactor pairs, with determinant
`(v^2-4w)(v^2+2w+6vw+6w^2)`. The stored rational map is valid only
off this determinant. To retain the repeated-root locus without
splitting cases, use those four linear equations in (6) instead
of their rational inverse. Retain projective coefficients of H
to include infinity. Equation (6) itself needs neither inverse.

This is one shared structural problem. It deliberately avoids creating
separate research tasks for the multiplicity partitions of an octic on
two points.


---

## 2026-10-14-generalization-quintic-logarithmic-support-independent-audit

# Independent audit of the logarithmic binary-support mechanism

Date: 2026-10-14, completed across local midnight on October 15.

Status: **PASS for the new characteristic-zero support mechanism,
quadratic representation test, stabilizer rank test, and unified A4
allowance equations. The attempt-04 matrix is not accepted as the actual
finite-h2 conductor incidence because its input uses a wrong coordinate
binding.** This is an independent written proof audit, not a new quintic
exclusion or a proof of emptiness of any coefficient locus.

The reviewed proposal is
[the logarithmic conductor-support note](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-14-generalization-quintic-logarithmic-conductor-support).
Accepted actual-conductor, homogeneous-gcd-cover and previous quintic
certificates are premises. Their verifiers were not rerun. The audit
checks the new elementary implications directly and checks the new
coordinate bridge against the coordinate definitions in those premises.

## 1. General Hamiltonian criterion: independently proved

Let k be algebraically closed of characteristic zero. Let F,H be nonzero
binary forms of degrees n>=1 and h>=1. Define

    D_H = H_t partial_s - H_s partial_t.

Then the following three conditions are equivalent:

    supp(div F) contained in supp(div H);
    F divides H F_s and F divides H F_t;
    F divides D_H F.                                      (A)

Here support is projective support. In the final divisibility D_H F has
degree n+h-2; when h=1 the condition means D_H F=0.

For the middle condition, factor F=ell^m G at any linear factor ell of F,
with ell not dividing G. At least one of the two nonzero constants
ell_s,ell_t is nonzero. Differentiating in that coordinate gives exact
ell-adic order m-1, because m is nonzero in k. Each other coordinate
derivative has order at least m-1. Consequently the two divisibilities
hold at ell precisely when ell divides H. Checking all factors of F
proves the first equivalence, including their full multiplicities.

For the final condition, use s!=0 and x=t/s, writing

    F=s^n f(x), H=s^h q(x).

A direct product-rule calculation gives

    D_H F = s^(n+h-2) [n q'(x) f(x) - h q(x) f'(x)].      (B)

Suppose f has a root alpha of multiplicity m. If q(alpha)!=0, the
second summand has order exactly m-1, while the first has order at
least m. The nonzero scalar h*m prevents cancellation of that leading
term, so F cannot divide D_H F. If q has order r>=1 at alpha, both
summands have order at least m+r-1>=m, including the case in which a
summand vanishes identically. The other projective chart gives exactly
the same argument at s=0. Thus F divides D_H F precisely when every
root of F is a root of H. No squarefreeness assumption is present.

This proof needs both degree h and all relevant multiplicities m to be
nonzero scalars. Characteristic zero supplies that hypothesis. An
unrestricted positive-characteristic statement is false, for instance
when F is a p-th power. For h=1, degree alone forces the quotient to
be zero, and (A) says exactly F is a nonzero scalar multiple of H^n.

The two-derivative formulation yields unique homogeneous quotients
L_s,L_t of degree h-1 and Euler's identity

    H F_s=L_s F, H F_t=L_t F,
    s L_s+t L_t=n H.

These equations and (A) retain all root multiplicities. They express a
support condition; they do not determine conductor multiplicities or
prove descent of a section through a nonnormal surface.

## 2. Quadratic H: the eigenvector test and characteristic polynomial

For H=a s^2+b st+c t^2, D_H preserves degree n. Therefore (A) is
equivalent to

    D_H F=mu F for a scalar mu.                           (C)

For a nonzero coefficient vector f, this is equivalent to all two-by-two
minors of [f | D_H f] vanishing. Indeed, choose any nonzero coefficient
f_i; vanishing of its minors with all other rows gives
mu=(D_H f)_i/f_i and then all rows of (C). Choosing that coefficient
in the proof introduces no coefficient inversion in the global minor
equations themselves.

The induced vector field on x=t/s is -2H(1,x) partial_x. Its zero
divisor is the quadratic divisor of H, including a double zero when
H is a square. Thus the geometric eigenvector argument in the proposal
is also valid: any root outside its zero divisor gives a forbidden
order m-1 term.

The derivation acts on coordinate functions by

    D_H(s)=b s+2c t, D_H(t)=-2a s-b t.

The matrix of these values on the coordinate column (s,t)^T is

    A=[[b,2c],[-2a,-b]], A^2=(b^2-4ac) I.

With coefficient columns for the basis (s,t), the operator matrix is
A^T. This transpose convention has no effect on the characteristic
polynomial or any support conclusion, but specifying the convention
avoids confusing point-coordinate and coefficient-coordinate matrices.

Put Delta=b^2-4ac. If Delta!=0, A has eigenvalues lambda,-lambda with
lambda^2=Delta. Its induced action on degree n forms has eigenvalues
(n-2i)lambda, for 0<=i<=n. For n=8 this gives

    char(D_H;mu)
      =mu (mu^2-4Delta)(mu^2-16Delta)
           (mu^2-36Delta)(mu^2-64Delta).                  (D)

Both sides are polynomial in a,b,c, so equality on Delta!=0 proves
the polynomial identity everywhere. Alternatively, if Delta=0 and
H!=0, an invertible linear coordinate change takes H to a nonzero
multiple of s^2, for which D_H is a nonzero multiple of s partial_t.
That action is nilpotent, has characteristic polynomial mu^9, and
has kernel spanned by s^8. Thus the repeated-root locus is retained;
it permits exactly the single-root support that (A) requires.

For H=z^2+vz+w and F(z)=sum_(i=0)^8 c_i z^i, homogenize with
z=t/s. Formula (B) becomes

    8(v+2z)F(z)-2(z^2+vz+w)F'(z).

Its z^9 terms cancel, and its degree-i coefficient is exactly

    d_i=(8-2i)v c_i+(18-2i)c_(i-1)-2(i+1)w c_(i+1),
    c_(-1)=c_9=0.                                        (E)

Thus equation (7) of the proposal is correct for any supplied octic
coefficient vector in this same coordinate. It does not validate the
geometric provenance of that coefficient vector.

## 3. Projective stabilizer rank test: independently proved

For F!=0 of degree n>=1, consider the four coefficient columns

    F, (s partial_s-t partial_t)F, s partial_t F, t partial_s F.

Their rank is at most three if and only if some nonzero element X of
sl2 acts by X(F)=mu F. A dependence cannot use only the first column,
since F!=0. Conversely such an eigenrelation is a dependence. The last
three operators form a basis of sl2 over characteristic zero.

The projective vector field induced by a nonzero X is nonzero and is a
global section of T_(P1)=O_(P1)(2). In a finite chart it is a polynomial
of degree at most two times partial_x; its projective zero divisor has
degree two. The same root-valuation argument used in section 1 forces
every root of F to lie in this divisor. Hence F has at most two distinct
projective roots. Conversely, if the support of F has one or two
points, choose a nonzero quadratic H vanishing on these points. Section
2 gives D_H F=mu F, supplying the dependence. Therefore

    rank[F | (s partial_s-t partial_t)F |
               s partial_t F | t partial_s F]<=3
       iff F has at most two distinct projective roots.   (F)

This proof also covers n=1,2, when the rank inequality is automatic and
the root bound is automatic. No assertion about a reduced determinantal
scheme or about stabilizers in positive characteristic is needed.

## 4. Unified Jbar/A4 allowance: independently proved

Let H be a nonzero quadratic, P a nonzero linear form, F a nonzero octic,
and j the actual Jbar scalar. Then the conditional support requirement

    j!=0: supp(F) contained in supp(H);
    j=0:  supp(F) contained in supp(HP)

is equivalent, on k-valued points, to existence of L_1 in Sym^1 and
mu in k satisfying

    D_(HP) F=L_1 F,
    j D_H F=mu F.                                        (G)

If j!=0, the second equation is (C) with eigenvalue mu/j. It forces
support in H, which also lies in HP; the first equation follows from
section 1. If j=0, F!=0 forces mu=0, and the first equation is exactly
the degree-three case of (A), allowing HP. This includes P equal to a
root of H, repeated H, and P at infinity. No disjoint-root hypothesis or
root-partition enumeration is required.

One can also remove the auxiliary quotient variables without choosing
roots: the first equation says that the degree-nine coefficient vector
of D_(HP)F lies in the span of the independent vectors sF,tF. Thus it is
equivalent on F!=0 to rank[sF | tF | D_(HP)F]<=2, together with
rank[F | j D_HF]<=1. These fixed-size matrix conditions retain the same
conditional support statement. They add no conductor-descent result.

All assertions above concern geometric points and a polynomial
incidence presenting them. They do not identify that incidence with a
reduced scheme, nor claim that an underlying-support condition over an
arbitrary nonreduced parameter base is equivalent to those equations.
For example, over k[epsilon]/(epsilon^2), F=s^2+epsilon t^2 and H=s^2
have the same underlying support, but D_H F=-4epsilon st is not a
scalar multiple of F. This distinction is harmless for the stated
characteristic-zero geometric-point criterion and should be preserved
in subsequent elimination or closure language.

There is a separate witness-lifting caveat for (F). Over the same ring,
let F=s^n+epsilon t^n with n>=3. Subtracting nF from the second column
of the stabilizer matrix leaves that column divisible by epsilon;
the third column is also divisible by epsilon. Thus all four-by-four
minors vanish. But D_H F=mu F for H=a s^2+b st+c t^2 forces

    mu=n b, c=0, epsilon a=0, 2n epsilon b=0.

Every coefficient of H is then in (epsilon), so no such H defines an
R-valued point of the projective quadratic space. This example forbids
promoting the field-valued determinantal criterion to a witness-lifting
statement over arbitrary bases. It does not by itself show that the
determinantal ideal is nonradical.

## 5. New coordinate-binding gap in attempt02/attempt04

This gap is independent of sections 1--4 and their proofs. The finite
monic quadratic cover is explicitly defined with

    z=r/delta, H_z(z)=z^2+vz+w

in section 1 and section 3 of the
[accepted homogeneous-gcd audit](NONENDPOINT_CUBIC_PAIR_COMPLETION.md#2026-10-13-session-nonendpoint-homogeneous-gcd-rank-and-cover-independent-audit).
The actual primitive conductor polynomial is F_p(p), with

    r0=delta/p,
    Pt(p)=p^3 P(delta/p)/delta^3

in sections 2 and 4 of the
[accepted diagonal-norm note](NONENDPOINT_RESIDUAL_FACTORIZATION_AND_GENUS.md#4-nonendpoint-diagonal-norm-identity).
Combining these definitions gives p=1/z on their common finite chart.
It does not give p=1-z. The latter relation uses the target normalization
coordinate z_target=1-p, which is a different coordinate from r/delta.

The
[attempt02 source](../computations/generalization_quintic_logarithmic_support_2026_10_14_attempt02.m2)
uses the correct cover parameter substitutions but sends its final
primitive-polynomial variable p to 1-zPar. Thus its saved coefficients
are coefficients of a different transformed form. The
[attempt04 source](../computations/generalization_quintic_logarithmic_support_2026_10_14_attempt04.m2)
correctly applies formula (E) to that saved vector and its
[execution record](../validation/2026-10-14-quintic-logarithmic-support/attempt-04/execution-record.json)
records exit zero. Exact postprocessing cannot repair the wrong
coordinate binding. Consequently its 9-by-2 matrix must not be cited
as the actual finite-h2 conductor-support matrix.

The corrected homogeneous conductor in the z chart is

    F_z(z)=z^8 F_p(1/z),                                  (H)

after the same actual parameter substitutions. If F_p=sum f_i p^i,
its z coefficients are f_(8-i). Formula (H) is homogeneous coordinate
interchange, so no division by z is needed in the final octic. It keeps
all degree drops: p=0 maps to z=infinity and p=infinity maps to z=0.
The intrinsic A4 allowance p=0 is therefore the linear form s when
z=t/s. Equivalently, in p coordinates the allowed quadratic is
H_p(p)=1+vp+wp^2, and the A4 allowance is p=0. Either choice is valid
provided both the actual conductor and all allowed forms use it.

This audit records the required correction; the shared-incidence
worker owns the corrected capture. No corrected capture, rank-locus
emptiness or geometry of its surviving points is asserted here.

## 6. Localization and acceptance boundary

The abstract criteria need F,H,P nonzero. If any is zero, its divisor
or the support criterion used here is undefined or changes meaning;
matrix minors alone may then vanish for an irrelevant reason. The
original geometric zero-form stratum remains a separate obligation.

The rational finite-h2 cover also retains its original determinant
open condition, exact-gcd cofactor condition, actual projection-center
avoidance, and any other accepted geometric hypotheses. A normalized
polynomial coefficient vector obtained by clearing denominators and
removing common parameter content represents the actual conductor only
where the resulting scalar comparison is a unit and the original
conductor is nonzero. On denominator or content boundaries, a
specialized primitive extension or the closure of the rational map
cannot replace the original coefficient equations. In particular,
the original four linear cover equations are the correct data for
retaining the repeated-root determinant boundary; the homogeneous
general criterion itself excludes no such boundary.

Accepted new mathematics from this audit consists of (A)--(G), with
their nonzero and characteristic-zero hypotheses. The coordinate
correction (H) follows directly from the accepted coordinate
definitions. The quintic application remains a necessary support
incidence, still requiring its correctly bound actual coefficients,
all original geometric conditions, and the full nonlinear conductor
descent conditions. There is no new global quintic, C0, or STCI
conclusion.


---

## 2026-10-14-generalization-quintic-h2-coordinate-correction-and-sextic-incidence

# Corrected h2 source coordinates and one sextic conductor-support incidence

Date: 2026-10-14. Status: **EXACT COORDINATE CORRECTION AND INCIDENCE
CAPTURE; independently audited** in the
[new factor and source-binding audit](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-14-generalization-quintic-h2-conductor-factor-independent-audit).
Accepted parameter covers,
the actual octic conductor, and previously closed quintic lanes are premises.
This note makes no support-emptiness, full-descent, whole-quintic or universal
STCI claim. The earlier attempt04 is retained as a coefficient capture with
an incorrect common-coordinate binding; it is not an actual h2 support test.

## 1. The necessary coordinate correction

The accepted finite h2 cover uses

```
x=r/delta,       H(x)=x^2+v*x+w,
P(x)=(A*x+B)H(x),       J(x)=(C*x+D)H(x).
```

The target parameter is `y=(r-delta)/r`, so the actual octic variable in
the frozen primitive polynomial is

```
p=1-y=delta/r=1/x.
```

Consequently the actual source-coordinate binary octic is

```
G(S,T)=Fdet(S,T),       G(1,x)=x^8 Fdet(1/x,1).       (1)
```

The source point at infinity is the intrinsic A4 point: its linear form
is `S`, and its target coordinate is `p=0`. Source `x=0` is target
infinity `p=infinity`. These are different points and neither is omitted.

Attempt02 inserted the accepted coefficient map into `Fdet(1-x,1)`, while
attempt04 applied the Hamiltonian action for `H(x)=x^2+vx+w` to those
coefficients. Those use different coordinates on the same P1. The computed
matrices exist, but their rank locus does not express the intended support
condition. No emptiness or quintic-closure conclusion had been derived from
that capture. The [original attempt04](../validation/2026-10-14-quintic-logarithmic-support/attempt-04/execution-record.json)
and its earlier failures remain preserved.

Let `B(t)=sum c_i t^i` be the saved polynomial from attempt02, after its
common denominator and nonzero `delta^4` content were removed. Then

```
G(1,x)=x^8 B(1-1/x)
      =sum_(i=0)^8 c_i (x-1)^i x^(8-i).              (2)
```

This is an invertible constant linear transformation on binary octics.
It preserves the nonzero form condition, the common coefficient content,
and all projective degree-drop strata. Explicitly, its coefficients are

```
g_j=(-1)^(8-j) sum_(i=8-j)^8 binomial(i,8-j)c_i.
```

The inverse is `B(t)=(1-t)^8 G(1,1/(1-t))`. The new
[attempt05 source](../computations/generalization_quintic_logarithmic_support_2026_10_14_attempt05.m2)
asserts both literal polynomial transformations, then asserts the quadratic
and A4-cubic Hamiltonian coefficient identities. Its
[captured execution](../validation/2026-10-14-quintic-logarithmic-support/attempt-05-correct-coordinate/execution-record.json)
has exit zero and empty stderr. It reuses all nine saved coefficients;
neither the accepted octic nor the rational inverse map is reconstructed.

## 2. Remove the forced differential factor before testing support

The new [conductor--differential factor proof](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-14-generalization-quintic-h2-conductor-quotient)
shows, on the entire actual h2 locus,

```
G=H Q,                 degree Q=6.                  (3)
```

The proof uses the actual conductor annihilation of relative differentials
at finite smooth source points, and the accepted A4 value and complete
infinity cover for the sole singular source point. It is a lower bound on
conductor contact. It places no upper bound on later contact or conductor
multiplicity and gives no descent assertion.

For any nonzero H,Q and any nonzero permitted linear form P, one has

```
supp(HQ) subset supp(H P^epsilon)
 iff supp(Q) subset supp(H P^epsilon).               (4)
```

Thus the degree-eight support condition reduces to the degree-six quotient,
without losing a high-contact or repeated-root stratum. Put `j=Jbar`,
`P=S` and define `D_A=A_T partial_S-A_S partial_T`. The exact shared
support incidence is

```
D_(HP) Q = L Q,        L a homogeneous linear form,
j D_H Q = mu Q,        mu a scalar.                 (5)
```

If j is nonzero the second equation says precisely that Q is supported
on H; the first then follows. If j is zero, Q nonzero forces mu=0 and
the first equation permits exactly the additional intrinsic A4 point.
The equation uses homogeneous forms, so infinity, a repeated H, and every
fixed-degree leading drop remain present together.

There is also a direct product-action check. Since `D_H H=0` and
`D_(PH)H=-H D_H P`,

```
D_H(HQ)=H D_H Q,
D_(PH)(HQ)=H [D_(PH)Q-(D_H P)Q].                    (6)
```

The last correction is linear and is absorbed into the free L in (5).

## 3. Captured sextic coefficient system on the accepted inverse-map open

On the monic finite chart write `Q=sum_(i=0)^6 q_i x^i`, with
`q_i=0` outside `0<=i<=6`. The two Hamiltonian images in (5) have
coefficients

```
d_i=(6-2i)v q_i+(14-2i)q_(i-1)-2(i+1)w q_(i+1),  0<=i<=6,
e_i=(6-3i)v q_i+(15-3i)q_(i-1)-3(i+1)w q_(i+1),  0<=i<=7.
```

Here `d` is the degree-preserving quadratic action and `e` is the
degree-seven cubic action, because `P=S` has affine dehomogenization one.
For `L=ell0*S+ell1*T`, (5) is the single fifteen-equation system

```
e_i=ell0 q_i+ell1 q_(i-1),       0<=i<=7,
j d_i=mu q_i,                  0<=i<=6.             (7)
```

For the nonzero-j part, all two-by-two minors of the stored seven-by-two
matrix `(q,d)` express the second line after removing its scalar unknown.
The characteristic polynomial of the action on Sym^6, with eigenvalue
`nu=mu/j`, is

```
nu*(nu^2-4 Delta)*(nu^2-16 Delta)*(nu^2-36 Delta),
Delta=v^2-4w.
```

Equivalently the shared scalar variable satisfies
`mu*(mu^2-4*j^2*Delta)*(mu^2-16*j^2*Delta)*(mu^2-36*j^2*Delta)=0`.

This is one representation equation, including its nilpotent repeated-root
boundary; the spectral identity is not an assertion that the actual family
has an eigenvector at any parameter.

The new [attempt06 source](../computations/generalization_quintic_logarithmic_support_2026_10_14_attempt06.m2)
divides the corrected G by the monic H, asserts the literal identity G=HQ,
and asserts both coefficient formulas and both product-action formulas.
Its [captured execution](../validation/2026-10-14-quintic-logarithmic-support/attempt-06-sextic-quotient/execution-record.json)
has exit zero and empty stderr. It saves all seven q_i, the seven-by-two
quadratic matrix and all eight A4-cubic coefficients. This is exact
incidence data, not an emptiness certificate.

The rational coefficient map is valid only off

```
(v^2-4w)*(v^2+2w+6vw+6w^2)=0.
```

Its stored denominator and delta^4 content retain those restrictions.
The written factor proof and homogeneous system (5) do not use that inverse.

## 4. One polynomial system retains every h2 chart

To avoid every inverse denominator, take all forms in the source homogeneous
coordinates `(S,T)` and use the literal accepted octic coefficient map. Use
quadratic H, independent linear cofactors A,C, sextic Q, linear L and scalar
mu as auxiliary variables. Impose coefficientwise

```
Psource=H A,        Jsource=H C,
Gactual=H Q,
D_(SH)Q=L Q,       j D_HQ=mu Q.                     (8)
```

Require `delta!=0`, H and Q nonzero, and the determinant of A,C nonzero.
The last condition makes the homogeneous gcd exactly two. Add the original
center-avoidance and finite-birational hypotheses when interpreting this as
an actual normalization projection. No quadratic leading coefficient, H
discriminant, center pivot, or cofactor coefficient is inverted in (8).
The accepted h2 cover proves that finite monic, repeated finite and
infinity-once loci are all represented; its exceptional K locus is already
inconsistent and double infinity is already impossible.

The support part of (8) is necessary and sufficient for the actual
restricted conductor to have only the permitted roots, under the actual
h2 geometric hypotheses. It is not sufficient for full inverse support or
for power descent through the full conductor algebra. The precise remaining
task is to prove this finite incidence incompatible with the original
projection and fiber equations, or describe its surviving geometric family
and test the complete conductor logarithm. No partition of the six or eight
contact multiplicities is required to state or investigate it.

## 5. Scalar-free shared matrices and the intrinsic contact bound

The scalar unknowns in (5) may be removed without choosing a root or a
coefficient of Q. In coefficient spaces the same incidence is

```
rank[Q | j D_HQ] <= 1,               a 7-by-2 matrix,
rank[S Q | T Q | D_(SH)Q] <= 2,      an 8-by-3 matrix.       (9)
```

The first column Q is nonzero. Multiplication by S and T gives two
linearly independent columns for nonzero Q, so the second rank condition
is exactly membership in their span; it does not add a hidden leading
coefficient assumption. At j=0 the first rank condition is automatic.
Thus all two-by-two minors of the first matrix and all three-by-three
minors of the second form one homogeneous coefficient ideal.

The separately audited
[intrinsic A4 contact bound](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-14-generalization-quintic-intrinsic-a4-contact-bound)
proves that after accepted G=j=0 mate closure, every j=0 full-support
candidate has actual A4 conductor contact one or two. Therefore every
surviving h2 mate candidate, including j=0, satisfies `Res(H,Q)=0`.
On the captured finite inverse-map chart this is the single necessary
condition `N12*N18=0` from the
[bounded norm calculation](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-14-generalization-quintic-h2-conductor-quotient).
Neither factor is separately declared impossible.

This contact bound also gives one coefficient-open condition useful for
the shared matrix ideal. H has no A4 root in a surviving lane, since its
infinity leading equations would give accepted-closed G=j=0. For j
nonzero, the accepted A4 target-fiber criterion makes F(A4) nonzero, so
q6 is nonzero. For j=0, source-infinity contact one or two makes Q have
affine degree five or four. Consequently

```
(q4,q5,q6) != (0,0,0)                                    (10)
```

on every surviving finite-chart candidate. Condition (10) is a single
ideal-open locus. Saturating by a product q4*q5*q6 would be wrong: it
would remove the entire j=0 locus. A future exact shared ideal certificate
may use saturation by the ideal `(q4,q5,q6)`, together with the stipulated
delta, inverse-map determinant and exact-h2 cofactor determinant units.
The j factor in the first matrix's minors must be retained.


---

## 2026-10-13-generalization-quintic-l2

# Regular single-root conductor concentration is impossible in every mate degree

Date: 2026-10-13, completed across local midnight on October 14.
Author: `quintic_continuation/l2_structural`.

Status: **NEW EXACT ELIMINATION AND WRITTEN THEOREM; independent audit
pending**. Accepted existing Taylor, actual-conductor, actual-fiber and
regular-L1 proofs are premises, as requested by the user. None of their
verifiers was replayed. This note closes the remaining regular L2
incidence in that explicitly scoped problem, subject to the new audit.
It does not close denominator-zero, infinity, multiple homogeneous
conormal-root, or Jbar-zero incidences.

## 1. The two new statements

Work over an algebraically closed field of characteristic zero in the
accepted nonendpoint sectional-genus-one quintic A4 normalization model.
Retain every actual projection-center avoidance and finite birational
projection hypothesis. Write `d=delta`, `k=kappa=aq+B`,

    Pc=q^2-6q+6, U=q(k-d)-d^2,
    D=2d(q-1)+q(q-2), E=d^2+d(3q-4)+q(q-2).

Impose the complete finite common-root incidence `Pt(q)=Jt(q)=0`, with
`G=Gs,J=Js` as in the accepted
[Taylor incidence](2026-10-13-session-nonendpoint-single-root-taylor-incidence.md).
The actual octic conductor restriction has expansion

    F(q+t)=sum_(i=1)^8 f_i t^i,
    f1=-d q L1 L2.

The regular chart is `qZ(q)!=0`, where `Z(q)=q Pc U`. Thus `d,q,Pc,U`
are units. We do not invert the original fiber leading coefficient
`A(q)`, either diagonal quotient value, or any unmentioned projection
parameter.

**New local theorem.** On this regular chart, if `L1!=0` and `L2=0`,
then `f2,f3,f4,f5` cannot all vanish. Consequently the actual conductor
restriction has local order at most five at q. This is a statement
about the full section, rather than a bound inferred from its first
normal symbol. It is independent of mate degree and does not require
Jbar nonzero or the sole-root condition.

**New all-mate consequence.** If additionally `Jbar=Js!=0` and q is
the sole common homogeneous conormal root, there is no mate of any
positive degree on the regular chart. The inherited
[quotient-fiber theorem](2026-10-13-session-nonendpoint-single-root-quotient-fibers.md)
already excludes the regular L1 branch under full inverse support.
The remaining branch has `L1!=0,L2=0`, but full inverse support and
the sole-root/Jbar hypotheses concentrate the nonzero degree-eight
actual conductor section entirely at q. That would force local order
eight, contradicting the new local theorem.

The common-root equations by themselves do not impose homogeneous gcd
degree one. Sole-root and Jbar conditions are used only in the last
support-concentration implication. Centers on the normalization remain
inadmissible, as in the accepted model; they are not silently removed
from a claimed unrestricted parameter exhaustion.

## 2. The discriminant and the first genuine unfolding parameter

The following exact new identities explain why four-parameter Taylor
incidence becomes a two-parameter algebraic problem:

    Disc_k(L2)=12 q(q-1)d^5 [d q(q-1)-(q-2)Pc],

    partial_a f2 = -(d q/2) L1 partial_k L2  (mod L2).       (1)

The second identity is modulo the actual complete L2 equation, with
the accepted common-root substitutions already made. In particular,
on `L1!=0` and away from its discriminant, `f2=0` uniquely determines
a. No later coefficients are discarded.

At `q=1`, L2 is the nonzero value `d^5`, so the L2 branch is empty.
At `q!=1,2` the discriminant-zero family, whenever its k-leading
coefficient is nonzero, has

    d=(q-2)Pc/[q(q-1)], k=d E/D,
    L1=0,
    f2=(q-2)^4 Pc^12/[9q^8(q-1)^8]!=0.                    (2)

Thus it cannot meet the new local incidence. Its possible k-leading
drop is treated separately in section 4, rather than lost in `k=dE/D`.
At q=2 the discriminant is a nonzero scalar times `d^4`, so it has
no discriminant-zero family with d nonzero.

## 3. Complete rational cover when q!=1,2 and D!=0

Over an algebraically closed field every point on this chart has an
exact discriminant coordinate m satisfying

    m^2=3-3(q-2)Pc/[d q(q-1)],
    d=3(q-2)Pc/[q(q-1)(3-m^2)],
    k=d(E+m d^2/3)/D.                                  (3)

Conversely the chosen m for a given point is
`m=3(Dk/d-E)/d^2`, so (3) covers both quadratic roots and does not
require choosing one branch of a square root. The pointwise inverse
requires precisely d,D nonzero. Here `m^2-3!=0` because
`q(q-1)(q-2)Pc!=0`. Also

    D=(q-2)(qm-3q+6)(qm+3q-6)/[q(m^2-3)].              (4)

Thus both displayed linear factors in (4) are units on this chart.
Write the following explicit polynomial:

    H=q^4m^2+3q^4m-3q^3m^2-3q^4-15q^3m+3q^2m^2
        +36q^3+27q^2m-144q^2-18qm+216q-108.

On the cover the exact first-factor expression is

    L1=-3m(q-2)Pc^2 H/
          [q^2(q-1)(m^2-3)^2(qm+3q-6)].              (5)

Therefore `L1!=0` forces both m and H nonzero. This justifies the H
division below; H is not saturated away without explanation.
Identity (1) makes the coefficient of a in f2 nonzero. Define

    av=-[f2|_(a=0)]/[partial_a f2]

on this exact chart. Its fully expanded rational function and both
numerator/denominator inputs are saved, rather than suppressed behind
an existence claim.

After substituting `a=av`, let n3,n4,n5 be the literal polynomial
numerators of f3,f4,f5, in the rational function field QQ(q,m).
The exact normalizations are

    n3=(q-2)^5 Pc^7 H g3,
    n4=(q-2)^5 Pc^7 g4,
    n5=(q-2)^5 Pc^7 g5.                               (6)

The saved g3,g4,g5 have total degrees 22,32,32. All factors removed
in (6) are units under the stated assumptions. Thus simultaneous
vanishing of f2,f3,f4,f5 implies `g3=g4=g5=0`.

Compute the literal fixed-degree resultants in m:

    R34=Res_m(g3,g4), R35=Res_m(g3,g5).

The exact QQ gcd is

    gcd(R34,R35)=q^53(q-2)^44 Pc^69.                  (7)

A common finite root of g3,g4,g5 forces both resultants to vanish,
including any leading-degree drop of these polynomials. Formula (7)
then forces one of q,q-2,Pc to vanish, contrary to the chart. The
argument uses only this necessary resultant implication, not a claim
that every resultant root is an actual solution. The literal Bezout
witness for the original resultants is saved separately.

## 4. The k-leading drop D=0 is retained and excluded

This boundary is the leading coefficient of L2 as a polynomial in k;
it is different from a geometric Cramer denominator or the original
fiber leading coefficient A(q). Since q=1 is already impossible,
`D=0,d!=0,q!=0` gives

    d=-q(q-2)/[2(q-1)], q!=2,
    k=-q(q-2)(7q^2-12q+6)/[24(q-1)^3].               (8)

The L2 equation is genuinely linear in k on this chart: its k
coefficient is `-3q^3(q-2)^4/[4(q-1)^2]`, which is nonzero.
Consequently (1) again makes f2 affine with nonzero a coefficient
on L1!=0. More explicitly that coefficient is

    3q^6(q-2)^6 V/[128(q-1)^4],
    V=5q^4-30q^3+66q^2-72q+36.

The drop V=0 is precisely an L1=0 point here and is outside the
new local theorem. After solving f2 for a, the full f3,f4 rational
functions are saved. Their literal numerators satisfy

    gcd(numerator f3,numerator f4)=q^4.              (9)

The saved literal Bezout witness combines those original numerators
to q^4. Since q is a unit, f3 and f4 cannot both vanish. No putative
exception at V=0 or a denominator of the a-solve is silently retained
as a solution: those conditions contradict L1!=0 by (1).

## 5. The target q=2 is retained and excluded

At q=2, L2 is a nonzero scalar multiple of

    6k^2-6d(d+2)k+d^2(d^2+6d+6).

The complete quadratic-field cover is

    mu^2=3, k=d+(3+mu)d^2/6,
    L1=-mu d(d+2mu/3).                              (10)

Because the ground field is algebraically closed and characteristic
zero, the two embeddings of QQ(mu) include both roots. With d nonzero,
L1 nonzero is exactly the retained unit `d+2mu/3!=0`.

In the exact ring QQ(mu)[d,a,z], let h2,h3,h4,h5 be the actual Taylor
coefficients under (10), and let

    h6=1-z*d*(d+2mu/3).

The literal polynomial identity in the saved five-entry column is

    (h2 h3 h4 h5 h6) * C = 1.                       (11)

Its multiplication was asserted exactly before saving C. Under the
retained units h6 can be zero; therefore h2,h3,h4,h5 cannot all be
zero. The witness is over the actual quadratic number field, not a
floating-point embedding or a sample mu value.

An earlier attempted unsaturated unit assertion failed because L1=0
solutions remained. That failure was mathematically informative and
is preserved. Equation (11) applies after the inherited L1 exclusion;
it is not a claim that the unrestricted q=2 Taylor ideal is empty.

## 6. Generalization and exact remaining scope

The new bound is **uniform in mate degree** and follows from the
actual conductor section plus its polynomial deformation in a. The
Jacobian factor L2 is accompanied by a discriminant, and the next
Taylor coefficient detects its simple-root unfolding through (1).
After one coefficient solves the unfolding parameter, three more
coefficients give a finite exact cover obstruction. This avoids
separate searches for every mate exponent.

The local theorem is stronger than the single-root application, but
the order-five bound alone cannot rule out several conductor-support
points sharing total degree eight. No general conductor local-order
bound for arbitrary carriers follows from these particular formulas.
The useful broader scheme is to combine an actual conductor section,
a complete discriminant cover, a nonzero unfolding coefficient and
a literal higher-coefficient Bezout obstruction.

The unclosed incidences remain `Z(q)=0` (including Pc=0 and U=0),
the intrinsic q=0 target, target infinity, Jbar=0 where permitted
A4 contribution can occur, and additional common homogeneous
conormal roots. Other normalization genera and other carrier degrees
are outside this model. The universal projective-curve STCI question
and the unrestricted characteristic-zero C0 question remain open.

## 7. Evidence and failure history

All new sources have prefix
`research/computations/generalization_quintic_l2_` and all outputs are
in `research/validation/2026-10-13-generalization-quintic-l2/`.
The accepted input is the frozen actual primitive octic
`2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/primitive-polynomial.txt`.

The coefficient-cover source generated its exact rational data and
numerators before entering a redundant direct saturation. That
saturation was interrupted after the separate exact resultant route
completed; no saturation result is claimed. Its source and raw outputs
are preserved, and the coefficient artifacts feed the completed
resultant and literal-Bézout sources.

The compact drops source initially encountered M2 syntax and a
protected-name error; its completed third version passed the new
identity calculation. The boundary source retains number-field
fraction-interface, Sequence/matrix-interface, unsaturated-unit,
matrix-lift-interface and ring-coercion failures. They are distinct
attempts, not successful independent proofs. The final clean source,
literal witnesses, raw streams, source snapshots, exit statuses and
hashes are bound by the manifest. Verification counts are restricted
to their stated algebraic identities and do not independently prove
the inherited conductor-module theorem or certify novelty.
