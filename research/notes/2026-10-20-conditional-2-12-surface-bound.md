# Conditional (2,12;6,16;2): the strict sextic must be nonnormal

Date: 2026-10-20. Author: `surface_bound` worker.

Status: **new conditional exclusion, independent review requested**. This
note does not prove the conditional configuration empty. It excludes
the stratum where the strict sextic on the blowup is normal, including
all multiplier multiplicities and all retained root types. No canonical
record or inherited proof is changed. The forced norm multiplier in the
separate geometric continuation note is independently reviewed below.

## 1. Exact scope and dependencies

Work over an algebraically closed field of characteristic zero with
`C=C0=[s^4:s^3t:st^3:t^4]`. Assume an ACTUAL homogeneous pair `(F6,G16)`
has sole reduced support `C`, FULL generic ordinary initial ideal a
coprime binary CI of degrees `(2,12)`, and ACTUAL saturated movement-two
first relation. Use promoted
[R-0010](../results/saturated_first_relation_normal_flatness.md) and
[R-0011](../results/moving_nonreduced_spectral_root_obstruction.md), and
the newly reviewed finite bridge in
[the singular-root proposal](2026-10-20-conditional-2-12-singular-gluing.md).
The latter is reviewed but unpromoted; this is an explicit dependency.

Put `B=Bl_C(P3)`, `H=pi^*O(1)`, and write `E` for its exceptional divisor.
The strict divisor `D=(F6)'` has class `6H-2E`. Its degree-two symbol is
`alpha*f`, where `alpha` is a nonzero section of `O_C(8)` and the full
reduced root `Z=(f)` has class `(2,2)` on `E=P1 x P1`. The map `Z->C`
is finite flat of degree two. Thus

    length div_Z(alpha)=16.                                      (1)

The conclusion proved below is:

> If the strict sextic `D` is normal, no such actual pair exists.
> Therefore every actual pair in the exact conditional configuration
> would have a nonnormal strict sextic.

Normality here concerns `D` on `B`, not merely the original sextic
surface in `P3`. Neither irreducibility nor the supported-CI hypothesis
is silently substituted for this assumption.

## 2. A uniform local Milnor lower bound

Let `x` be any point of `Z` at which `alpha` vanishes. The two original
degree-two symbols are `alpha*f` and `beta*f`, with `alpha,beta` having
no common base zero by normal flatness. Thus `beta` is a unit at `x`.
Choose the local finite-bridge generator `p=G16/t^2`, up to a unit,
where `t=0` defines `E`. Invertibility of the actual generator change,
and the fiberwise coprimality of the full initial pair, give

    F6/t^2=A*p+t^10*U,            U a unit,                     (2)

and `A|Z` is a unit times `alpha|Z`. There is no additional
nonvanishing hypothesis on `U`: at a zero of `alpha`, it follows from
`beta` being a unit and the invertible actual generator change.

The ideal `(A,p,t)` has finite colength. Indeed modulo `(p,t)` it is
the nonzero section `alpha|Z` of the reduced finite root curve. Since
the ambient local ring is regular of dimension three, `(A,p,t)` is a
regular sequence. Write

    ell_x=length O_(B,x)/(A,p,t).

Differentiating (2) gives

    d(F6/t^2)=p*dA+A*dp+t^9*(10U*dt+t*dU).

Consequently the ordinary Jacobian ideal satisfies

    J_(F6/t^2) subset (A,p,t^9).                                (3)

If the hypersurface singularity is isolated, its Milnor number is the
length of its ordinary Jacobian algebra. Therefore

    mu_x(D) >= length O_(B,x)/(A,p,t^9) = 9*ell_x.               (4)

The last equality is the regular-sequence filtration by powers of `t`
in the one-dimensional complete intersection `O_(B,x)/(A,p)`.
This proof works at multiple multiplier zeros, ramification points,
and singular root points. It does not assume smoothness of `(p)` or
of `Z`. When `Z` is smooth and the zero is simple, `(A,p,t)` are local
coordinates and (2) is exactly an `A9` singularity.

If `D` is normal, its singular locus is finite, because it is a
surface hypersurface in a smooth threefold. Summing (4) over (1)
then yields

    sum_(x in Sing D) mu_x(D) >= 144.                           (5)

For reference, the Jacobian-algebra interpretation of the isolated
Milnor number and the Milnor-fiber sphere calculation are treated in
David Massey's [lectures on hypersurface singularities](https://arxiv.org/abs/1410.3312),
Lecture 1. The use in (3)-(4) is elementary ideal containment, and does
not invoke semicontinuity or a generic-root approximation.

## 3. Smoothing invariants and a genus-six plane section

The blowup intersection numbers and canonical class are

    H^3=1, H^2E=0, HE^2=-4, E^3=-14, K_B=-4H+E.

Hence `K_D=(2H-E)|D`, and

    D^3=40, c1(B)*D^2=40, K_D^2=-4.

One has `c2(B)*H=10`, `c2(B)*E=16`, so `c2(B)*D=28`.
Adjunction gives the Euler characteristic of a smooth member

    e(D_sm)=c2(B)*D-c1(B)*D^2+D^3=28.                          (6)

The class `3H-E` is basepoint free. One direct verification uses the
global generators of `I_C(3)`

    q*x0,q*x1,q*x2,q*x3,A,B0,D0,

where `q=x0*x3-x1*x2`, `A=x0^2*x2-x1^3`,
`B0=x0*x2^2-x1^2*x3`, `D0=x2^3-x1*x3^2`.
On the smooth quadric `(q=0)`, the last three restrict to the three
binary-quadratic multiples of the local equation of `C`; together
with `q` they generate the ideal sheaf. Their cubic versions therefore
generate `I_C(3)` and its pullback line bundle on `B`. It follows that
`6H-2E=2(3H-E)` is basepoint free. General members are smooth by
Bertini and furnish a smoothing of every normal member. The map has
three-dimensional image (off `q=0` the four `q*x_i` recover the original
projective point), so general members are also irreducible.

Suppose now that `D` is normal. It is connected and therefore integral.
For completeness, connectedness follows from `H^1(O_B(-D))=0`:
by Serre duality this is dual to `H^2(O_B(2H-E))`. The strict quadric
`Q'` has class `2H-E`, is isomorphic to `P1 x P1`, and its normal
bundle is `O_Q(1,-1)`. The sequence

    0 -> O_B -> O_B(Q') -> O_Q(1,-1) -> 0

gives that vanishing, since `B` is rational and every cohomology group
of `O_Q(1,-1)` vanishes.

Let `r:S->D` be a projective resolution, and let `h` denote the
pullback of the ambient plane class. Then `h` is nef and big, with
`h^2=6`. A general ambient plane avoids the finite singular locus of
`D`; its inverse-image curve `Gamma` is smooth and irreducible. Its
genus, computed on the smooth locus of `D`, is

    K_D*H_D=4,
    g(Gamma)=1+(H_D^2+K_D*H_D)/2=6.                            (7)

Kawamata-Viehweg vanishing on the smooth projective surface `S` gives
`H^1(S,K_S+h)=0`. Serre duality gives `H^1(S,O_S(-h))=0`. The
restriction sequence therefore injects `H^1(O_S)` into
`H^1(O_Gamma)`, and

    q(S)<=6,              b1(S)=b3(S)=2q(S)<=12.                (8)

An exact statement of the vanishing theorem for nef and big divisors
is in Osamu Fujino's [Kawamata-Viehweg vanishing notes](https://www.math.kyoto-u.ac.jp/~fujino/kawamata--viehweg2.pdf),
Theorem 0.3; apply it to an integral divisor and the map to a point.
No positivity of the canonical class of `S` is required.

## 4. A deliberately coarse global upper bound of fifty

Write `Exc` for the reduced exceptional curve of `r`. Its irreducible
components have negative-definite intersection matrix. Equivalently,
their classes inject in `H2(S,QQ)`; one can use Hodge index with the
nef and big class `h`, or the standard exceptional-curve theorem for
a resolution of a normal surface. In particular the contraction
exact sequence

    H3(Exc)=0 -> H3(S) -> H3(D) -> H2(Exc) -> H2(S)

shows `b3(D)=b3(S)<=12`. Connected exceptional fibers and the same
contraction sequence in degree one give `b1(D)<=b1(S)<=12`.
Since `D` is integral and projective, `b0(D)=b4(D)=1`; also `b2(D)>=0`.
Consequently

    e(D)=2-b1(D)+b2(D)-b3(D) >= -22.                           (9)

For a surface with isolated hypersurface singularities, a smoothing
replaces each singular point by a Milnor fiber with Euler
characteristic `1+mu_x`. Using (6),

    sum mu_x(D)=e(D_sm)-e(D)<=28+22=50.                       (10)

Equations (5) and (10) contradict each other. This proves the normal
strict-sextic exclusion stated in section 1. The bound fifty is
intentionally coarse; no sharper K3 or discriminant bound is needed.
The topological argument is over `CC`. For a general algebraically
closed characteristic-zero field, descend the finitely many
coefficients and data to a finitely generated characteristic-zero
field and embed it in `CC`; geometric normality and the actual
finite-type hypotheses persist after algebraically closed extension.

## 5. What remains genuinely unresolved

The proof does not apply to a nonnormal strict sextic, whose singular
locus has positive dimension. At such a point the ordinary Jacobian
algebra has infinite length, so (3) cannot be combined with an
isolated Milnor-number Euler formula. For example

    p=x, A=z^2, F'=x*z^2+t^10

has the required finite intersection `(A,p,t)` of length two and a
reduced smooth root `(p mod t=0)`, but its singular locus is the line
`z=t=0`. It illustrates the defect in silently extending the isolated
argument. It is a local caution, not a global `C0` realization.

Similarly, embedding the finite complete intersection
`(A,p,t^9)` in the singular scheme does not by itself bound the degree
of that singular scheme or a discriminant multiplicity when the
singular scheme has curve components. Aluffi-Cukierman's
[multiplicity formula](https://www.math.fsu.edu/~aluffi/papers/1992Mod.pdf)
uses the full Segre class and requires first-jet spanning; neither
condition can be replaced by the length of an arbitrary finite
subscheme. No universal nonnormal discriminant bound is asserted here.

Thus the remaining actual-pair problem has been narrowed to the
nonnormal strict-sextic stratum, retaining every root/gluing type
allowed by the earlier spectral incidence and the forced norm
multiplier. Its conductor, normalization, and singular curve need
additional control. A low-order incidence point on that stratum is
still not an actual global pair, and no degree-sixteen realization or
degree-twelve standard-basis certificate is supplied by this note.

## 6. Independent audit of the forced norm multiplier

I independently reconstructed sections 1-4 of
[the geometric continuation note](2026-10-20-conditional-2-12-geometric-continuation.md).
Verdict: **PASS within the actual supported-pair scope**, including
all repeated-root, collision, and ramification cases.

On `Q'` the strict divisors are `R=(4,0)` and `T=(14,10)`. No ruling
component of `R` is a component of `T`, since such a common curve
would survive downstairs outside `C`. If `m_y` is the multiplicity
of a ruling in `R`, total intersection there is exactly `10m_y`.
Restricting the actual ideal `(p,t^10)` to the smooth `Q'` gives local
length `10 ord_x(tau)` with no root smoothness requirement. Hence

    m_y=sum_(pi3(x)=y) ord_x(tau),
    R=pi3_*div(tau),
    div(alpha)=pi3^*pi3_*div(tau)-div(tau).

The affine quadric coordinates `(1,z,b,z*b)`, with `C:b=z^3`, verify
`alpha(z)*tau(z)=R4(z^3)` directly. This yields the homogeneous
polynomial identity `alpha proportional tau(zeta*z)tau(zeta^2*z)`.
The coefficient formula over `QQ` in the owner note is correct.
At the branch fibers the orders are `3m-m=2m`; at unramified fibers
they are the sums of the other two orbit multiplicities. Thus no
collision or branch open was inadvertently removed. The argument
also correctly excludes `tau=0` by the noneffective residual class
`(3,-3)` on `Q`, after excluding a quadric component of the actual
pair by its Picard class.

This audit establishes no reverse implication from the norm identity
to global realization. The singular-root finite bridge remains an
explicit reviewed-proposal dependency.
