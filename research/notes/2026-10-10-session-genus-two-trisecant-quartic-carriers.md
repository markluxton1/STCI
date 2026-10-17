# Genus-two trisecant carriers and the reduced-discriminant obstruction

Date: 2026-10-10. Owner: `trisecant_quartic_geometry`.

Status: **PROVED HERE** for the line classification and carrier ideal in
sections 1--2; an independent exact audit is being preserved separately.
Sections 3--5 are a **CONDITIONAL PROOF FOR AUDIT**: they use the pending
actual ambient-line-blowup realization of the genus-two adjoint model.
They do not close the nonreduced-discriminant stratum, the endpoint
trisecant stratum, the genus-two lane, or the unrestricted STCI problem.
No canonical frontier record is changed by this note.

Work over an algebraically closed field of characteristic zero, with

    C0 = [s^4:s^3 t:s t^3:t^4],
    q = x0 x3 - x1 x2,
    A = x0^2 x2 - x1^3,
    B = x0 x2^2 - x1^2 x3,
    D = x2^3 - x1 x3^2.

The accepted mate correction has `C#+Z ~ L`, with effective rational
exceptional `Z`. In the lambda-one stratum, `C#^2=1`, `f.C#=1`, and
`K.Z=1`. Conditional on the actual blowup realization, the planes through
the conductor line give `f`, so `length(C0 cap Gamma)=4-f.C#=3`.

## 1. There are exactly two ambient types of trisecant line

Any line whose scheme-theoretic intersection with C0 has length at least
three lies on q: the nonzero restriction of a quadric to a line has zero
scheme of length two. The quadric is smooth. In Segre coordinates,

    (x0,x1,x2,x3) = (uv,uy,xv,xy),
    C0: (u:x)=(s^3:t^3), (v:y)=(s:t).

The ruling with fixed `(v:y)` meets C0 in length one. The other ruling is

    Gamma_a = (x2-a x0, x3-a x1),     a in k,
    Gamma_infinity = (x0,x1).

On C0 its common factor is `t^3-a s^3`. For `a` nonzero this gives three
distinct points. For `a=0` and infinity it gives a single point with
triple contact. Diagonal reparametrization of C0 takes `a` to `r^3 a`;
over the algebraically closed field all nonzero finite values are
equivalent to one. Reversal interchanges zero and infinity. Thus the
literal ambient line types are `Gamma_1` and `Gamma_0`.

The algebraically closed hypothesis matters here. Over an arbitrary
characteristic-zero field diagonal scaling need not identify all
nonzero values, because the needed cube root may not exist.

## 2. The entire carrier ideal has three cubic generators

For finite `a` set

    u=x0, v=x1, z=x2-a x0, w=x3-a x1,
    q=uw-vz,
    T_a=z^3+a u z^2-v w^2 = D-2a B+a^2 A.

Then, as homogeneous ideals,

    I(C0) intersect (z,w)^2 = (qz,qw,T_a).

One geometric proof is on q. A degree-d form restricting to a section
that vanishes on C0 and twice on Gamma has divisor at least
`C0+2 Gamma`, which is the divisor of the cubic T_a on q. Its remaining
section lies in `O_q(d-3,d-3)` and lifts to an ambient form of degree
`d-3`. Subtracting that multiple of T_a leaves a multiple of q.
Since q has normal order one along Gamma, that multiple belongs to
`(z,w)^2` precisely when its quotient belongs to `(z,w)`. This yields
the stated ideal, including all degrees.

For an algebraic unmixedness certificate, the three cubic generators
are the maximal minors of

    [ w     z^2+a u z ]
    [-z        -v w   ]
    [ 0         -q    ].

Their support consists of C0 and Gamma; the generic length along Gamma
is three, exactly the first infinitesimal neighborhood `(z,w)^2`.
This is compatible with a surface having multiplicity two along the
line; it is not a claim that `(z,w)^2` has generic length two.

Consequently every quartic through C0 and double along Gamma is

    F = q Q + T_a L0,
    Q in (z,w)_2,       L0 an arbitrary ambient linear form.

The quartic space is the direct sum of a seven-dimensional space
`q (z,w)_2` and the four-dimensional space `T_a R_1`, hence has dimension
eleven. The sum is direct because T_a is not divisible by q.
On q its entire divisor is

    div(F|q) = C0 + 2 Gamma + (q cap {L0=0}).

For an integral carrier L0 is nonzero. The final term may be a smooth
conic or two ruling lines. Its degenerations must be retained.

## 3. Mate support forces the discriminant to vanish at each contact

Now assume the actual lift theorem: the strict transform T in
`Bl_Gamma(P3)` is normal, its minimal resolution is M, and M contracts
only vertical ADE curves to T. Its canonical divisor is `-E_Gamma|T`.
The separate map M to the normalization S can contract horizontal
(-3) sections as well.

The entire conductor algebra on S is a quadratic algebra over Gamma.
Under a mate, the complete inverse image of C0 in S has underlying
set c, and c maps isomorphically to C0. Hence over every point of
`Gamma cap C0` the conductor has exactly one geometric point: a split
fiber would give a second normalization point outside c. Its
discriminant therefore vanishes at each contact point.

The discriminant can be read from the first normal quadratic part of
F. Write

    Q = z alpha(u,v) + w beta(u,v) + Q2(z,w),
    L0|Gamma = c0 u + c1 v,
    alpha=a0 u+a1 v,       beta=b0 u+b1 v.

The leading quadratic is

    A2 z^2 + B2 zw + C2 w^2,
    A2=-v alpha+a u L0|Gamma,
    B2=u alpha-v beta,
    C2=u beta-v L0|Gamma.

For Gamma_1 put `r=v/u`. At a contact `r^3=1`, its discriminant obeys

    Delta(r) = (alpha(1,r)+r beta(1,r)-2r^2 L0(1,r))^2.

Vanishing at all three distinct contacts is thus equivalent to

    a0=2c1,       a1=-b0,       b1=2c0.

With these substitutions the entire quartic discriminant is

    Delta = 4(v^3-u^3)
              [(c0^2+b0 c1)v+(b0 c0-c1^2)u].

The identification with the actual conductor algebra uses the
canonical ideal: on the resolution the conductor ideal is
`O_M(K_M)`, and `R sigma_* O_M = O_S`,
`R sigma_* omega_M = omega_S`. The quotient pushes to the actual
conductor structure sheaf. The same argument for the rational ADE
resolution `M -> T`, with `omega_T=O_T(-E_Gamma)`, gives
`sigma_T* O_(D_M)=O_(D_T)` and no higher direct image. Both quotients
therefore have the same pushforward to Gamma as schemes, not only
the same generic quadratic field. On the ambient exceptional divisor
`E_Gamma=P1_Gamma times P1`, the exact sequence

    0 -> O(-2,-2) -> O -> O_(D_T) -> 0

gives `0 -> O_Gamma -> p_*O_(D_T) -> O_Gamma(-2) -> 0` and
`R1 p_* O_(D_T)=0`, even when D_T has vertical components. This is
precisely the quadratic algebra with the displayed discriminant,
including its identically-zero case. Thus isolated changes of its
extension at bad fibers cannot remove the contact vanishing
conditions.

## 4. A nonzero discriminant permits only one horizontal section

A horizontal sigma-exceptional E has `L.E=0`, `f.E=1`, so its image in
the ambient blowup is the entire exceptional fiber P1 above a point
of Gamma. Therefore the whole leading quadratic must vanish there.
The discriminant has a root of multiplicity at least two at that
point. The point lies in C0 because the correction cycle is supported
over c; a horizontal section with zero correction coefficient is also
avoided by c, as positivity gives `Z.E=C#.E=0`.

In the `Delta != 0` case, two horizontal sections cannot have positive
correction coefficients: the three C0-contact roots and two double
roots would require quartic degree at least five. There is therefore
exactly one horizontal section in the correction support, with
coefficient one since `K.Z=1`. A horizontal section outside the
correction support cannot meet that support, because `Z.E=0` and
effectiveness make each such intersection nonnegative. It does not
change its connected exceptional fiber.

Normalize the supporting contact to r=1 by cube-root diagonal
scaling. Whole-quadratic vanishing gives

    b0=c1-c0,
    Delta=4 kappa (v^3-u^3)(v-u),
    kappa=c0^2-c0 c1+c1^2.

For `kappa != 0`, the exceptional intersection on T is

    D_T = E_p + D',

where the residual `(1,2)` curve meets E_p in two distinct points.
Indeed after removing its common linear factor on Gamma, its
quadratic discriminant at p is nonzero. At either intersection the
ambient exceptional-divisor section D_T is an ordinary node.

Away from these points E_p is a smooth Cartier curve on T. A smooth
Cartier curve cannot pass through a singular surface point: if the
quotient of a two-dimensional local ring by one nonzerodivisor is a
regular one-dimensional ring, its maximal ideal has at most two
generators, so the surface local ring is regular. Hence T is smooth
along E_p away from the two nodes.

At each node the local ambient equation has the form

    xy + t R(x,y,t) = 0,

with the exceptional section `t=0`. If T is singular there, formal
Morse splitting in x,y yields `xy+g(t)=0`. Normality makes g nonzero,
and the rational Gorenstein singularity is A_n. The branches E_p and
D' meet opposite endpoints of the minimal-resolution A_n chain.
Consequently the connected sigma-exceptional graph containing the
(-3) section E has at most two endpoint A_n arms.

## 5. An exceptional correction cannot exist on that graph

Its coefficient at E is one. A chain arm of n (-2) curves, numbered
from E, has coefficients z_i satisfying

    2z_i-z_(i-1)-z_(i+1) = epsilon_i,
    z_0=1,       z_(n+1)=0,

where `epsilon_i=C#.F_i`. Smooth embedded descent supplies at most
one contact prime in the connected fiber, with intersection one.
With no contact on an arm its first coefficient is

    z_1=n/(n+1)<1.

With the unique contact at position j it is

    z_1=n/(n+1)+(n+1-j)/(n+1)<2.

If c contacts E, its equation requires the sum of its at most two
neighbor coefficients to equal two; both are strictly below one.
If c contacts an arm, the E equation requires that sum to equal
three; the contacted arm is strictly below two and the other strictly
below one. If it does not contact this graph, the required sum is
three while both terms are below one. Every possibility contradicts
the intersection equations.

Thus, conditional on the actual normal-blowup realization and the
scheme/discriminant interface above, the generic-trisecant lambda-one
mate branch with `Delta != 0` is excluded.

## 6. Deliberate surviving boundary

This argument leaves `kappa=0`, hence `Delta identically zero`, open.
The residual exceptional curve may then be nonreduced; node and
endpoint-chain arguments cannot be imported to that boundary. The
two endpoint trisecant lines likewise remain open here. At `a=0`,
the sole discriminant vanishing condition is `a0=0`, which forces a
factor `v^2` but does not give three distinct contact roots. The
lambda-zero bisecant branch is not addressed by this note.
