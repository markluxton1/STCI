# Square descent, conductor contact and singular gluing

**Scope and status.** Independently reviewed provisional local theorems and
actual constructions over an algebraically closed field of characteristic
zero; no canonical promotion. Local supported intersections are useful
realizations in their own right. They must still meet the fixed embedding,
polarization and section-image conditions to become a projective application.

Three quantities remain separate: the carrier equation's first normal
symbol, the actual normalization map's transverse differential, and the
failure of a root to generate its normalization. The smooth-contact theorem
below compares the latter map with full conductor contact only under its
power-descent hypotheses. Singular-gluing controls show which hypotheses
cannot be discarded.

## Smooth-conductor contact is bounded by the actual normal differential

There is a further consequence of the actual local algebra in [the smooth-conductor formula](#a-general-local-formula-when-the-conductor-downstairs-is-smooth).
Retain its smooth normalization B, smooth downstairs conductor R,
principal full conductor I, rank-two conductor algebra, smooth curve
with full singleton inverse mapping isomorphically to C, and finite
positive contact b. Suppose an actual section g in A pulls back to a
function with divisor n c, for any positive integer n. No separate
non-descending root, parity hypothesis, or fixed mate exponent is needed.

Let h be the vanishing order on c of the image of the actual
normalization normal-differential map

    (I_C/I_C^2)|c -> I_c/I_c^2.

Equivalently, pull back two ambient normal parameters of the smooth
curve C, retain their first coefficients in an equation w of c,
and take the minimum of their orders along c. Changes of regular
ambient normal frame or of the local equation of c preserve h.
This is the transverse differential order, **not** the first-symbol
order of a hypersurface equation. Then

    h>=1,   b<=2h.                                      (22)

For b>=2 the more precise alternatives are b=h or b=2h.

If b=1 and h=0, the isomorphism c->C supplies one tangent direction
and a unit transverse coefficient supplies the other. The target
cotangent map onto the smooth normalization is surjective. The finite
singleton cotangent/Nakayama lemma forces A=B locally, contradicting
positive conductor contact. This proves (22) when b=1.

For b>=2, the parameter argument in [the smooth-conductor formula](#a-general-local-formula-when-the-conductor-downstairs-is-smooth) gives a lift s of the smooth
conductor parameter restricting to a uniformizer of c. Write the
pulled-back section as `g=unit*w0^n`; an n-th root of the unit exists
in the complete characteristic-zero normalization. Replacing w0 by
that root times w0 preserves c, its normal-differential orders, and
the coordinate pair with s. Thus write

    B=k[[s,w]], g=w^n belongs to A,
    I=(F), F=w^2+a(s)w+b0(s), ord_s(b0)=b.

Set u=F. The ring S=k[[s,u]] embeds in B, which is free over S with
basis 1,w and relation `w^2+a w+b0-u=0`. This also follows directly
by eliminating u in the complete ring k[[s,u,w]]. The preimage of R
modulo I is therefore

    A=S+uB=S+uSw,
    v=uw,
    A=k[[s,u,v]]/(v^2+a u v+b0 u^2-u^3).                (23)

The smooth image C has ambient normal parameters U=u-b0(s), V=v.
Their pullbacks are

    U=a(s)w+w^2,
    V=b0(s)w+a(s)w^2+w^3.

Thus the actual differential image ideal is (a,b0), and

    h=min(ord_s(a),ord_s(b0)).                          (24)

The generic quadratic conductor algebra is reduced. Otherwise its
repeated root alpha is nonzero, since b0 is nonzero by finite contact,
and in the dual-number algebra
`w^n=alpha^n+n alpha^(n-1) epsilon` is not scalar. This contradicts
descent in characteristic zero. Its distinct nonzero roots alpha,beta
therefore satisfy `beta=zeta alpha`, where zeta is a constant n-th
root of unity and zeta!=1. If zeta=-1 then a=0 and (24) gives h=b.
Otherwise its trace puts alpha in R, and

    a=-(1+zeta)alpha, b0=zeta alpha^2.

Writing k=ord_s(alpha) gives h=k and b=2k. This proves (22) and
the two alternatives, without an upper bound on contact assumed
from a first-normal zero alone. The power-descent condition is what
forces the comparison.

## A general local formula when the conductor downstairs is smooth

This local theorem includes an extension from a square to any descended
power. It concerns the stated data, not a classification of arbitrary
nonnormal hypersurfaces.

Let A be an excellent characteristic-zero surface local ring with finite
normalization `B=k[[t,w]]`, and let I be the full conductor, principal
in B. Suppose `R=A/I=k[[s]]` is smooth, and `D=B/I` is finite free of
rank two over R. Let a smooth curve c in B map isomorphically to its
smooth image in A, with full singleton inverse support. Assume

    div(q)=m c,   m odd,   q^N belongs to A,   N>=2,
    q is generically non-descending on Gamma=Spec R.

Suppose the conductor has finite contact
`b=length O_c/(I|c)`. Cayley–Hamilton on the rank-two R-algebra D makes
`A'=A+Aq` a subalgebra: lift the trace and norm coefficients from R to
A, and use `Iq subset I subset A`. Then

    length B/A' = ((m-1)/2)*b.                           (8)

For m=5 this is exactly 2b. In the application, the rank-two hypothesis
comes from the actual conductor sequence, not just the degree of its
reduced support.

Choose a local equation w of c and absorb the unit in q into w by taking
an m-th root, so q=w^m. The quotient in (8) is `D/(R+Rq)`. Generic
non-descent and the descended power imply that the generic quadratic
algebra D is reduced: in a double-root algebra, the first nilpotent term
of a positive power cannot vanish in characteristic zero unless q
becomes scalar. Its generic root values are nonzero, since the conductor
does not contain c.

If b=1, D is smooth and c meets it transversely. The finite local double
cover of the smooth curve Gamma is totally ramified, so after choosing
parameters `D=k[[r]]` and `R=k[[r^2]]`. If tau is the involution, then
`tau(q)/q` is an N-th root of unity and its square is one. Non-descent
forces it to be -1. As q has order m on D, its coefficient in the odd
basis r has order `(m-1)/2` in R. This proves (8) in this case.

If b>=2, choose an element of A restricting to a parameter on c. Modulo
I it is a function of s; the error restricts to order at least b on c.
Therefore s itself restricts to order one on c. The pair (s,w) is now
a regular system of parameters of B, and Weierstrass preparation gives

    D=R[w]/(f),  f monic quadratic in w.

Let alpha,beta be its two roots in an algebraic closure of k((s)).
Descent and non-descent give

    beta=zeta*alpha,   zeta^(mN)=1,   zeta^m!=1.

If zeta is not -1, the trace `(1+zeta)*alpha` belongs to R, so alpha
belongs to R. Write `a=ord_s(alpha)`. Then b=2a, and interpolation
shows that the coefficient of w in q modulo f is

    ((1-zeta^m)/(1-zeta))*alpha^(m-1).

Its order is `(m-1)a`, giving (8). If zeta=-1, write
`f=w^2-v(s)`. Then `b=ord_s(v)` and
`w^m=v^((m-1)/2)w`, giving the same result. This case includes singular
and ramified conductor curves upstairs. The proof does not assume that
s was initially a coordinate on B or that D was smooth.

Geometrically, the formula compares the actual failure of the root to
generate the normalization with the entire conductor contact. It holds
for any descended power, while the smoothness assumptions are local to
the normalization and the conductor downstairs. Singular normalization
points are outside this argument. The following extension handles reduced
Gorenstein singularities of Gamma when the normalization remains smooth.

## Reduced Gorenstein conductors at a smooth normalization point

The formula extends to every positive odd root multiplicity m and to
singular Gamma under the following precise hypotheses. Work over an
algebraically closed field of characteristic zero in completed local
rings. Let `B=k[[u,v]]` be the normalization, I its full principal
conductor, and suppose `R=A/I` is reduced and Gorenstein. Require the
actual conductor sequence

    0 -> R -> D=B/I -> omega_R -> 0,   omega_R isomorphic to R.     (9)

Let c be smooth, with full singleton inverse support and an isomorphic
smooth image C. Suppose `div(q)=m c`, with m positive and odd, some
`q^N` with N>=2 belongs to A,
and the class of q in D/R is nonzero generically on every branch of R.
The finite conductor contact is `b=length O_c/(I|c)`. Then

    length B/(A+Aq)=((m-1)/2)*b.                               (10)

For the quintic root m=5 this is exactly 2b.

Here branchwise non-descent is explicit; it must not be deduced merely
from non-descent somewhere on a reducible conductor. In the integral
global application the nonzero section of the rank-one dualizing sheaf
supplies it wherever that sheaf is locally free.

Sequence (9) splits as R-modules. Thus D is a free quadratic R-algebra,
and its trace involution tau has invariant part R and a free rank-one
anti-invariant part. Cayley–Hamilton gives the same closure of A+Aq
as in [the smooth-conductor formula](#a-general-local-formula-when-the-conductor-downstairs-is-smooth). The involution lifts to B: when D is singular, choose lifts
of a tau-eigenbasis of its cotangent space. They are parameters of B,
and the linear sign action on them induces tau and preserves I. When
D is smooth, lift its eigenparameter and choose a complementary equation
for I. The identity action is excluded by generic non-descent. The
action -Id on both tangent parameters is impossible: it would give two
independent anti-invariant cotangent classes, whereas the anti-module
is free of rank one over R and its maximal ideal acts through at least
second-order terms. The lift is therefore a reflection. Choose

    tau(u)=u, tau(v)=-v,   S=B^tau=k[[u,t]], t=v^2.

A generator of the tau-stable principal ideal I can be chosen as an
eigenvector by averaging. It must be invariant. Indeed, an
anti-invariant generator has form `v g`, g in S; it gives
`R=S/(t g)` and anti-module `S/(g)`, which is not a faithful free
rank-one R-module. Hence I=fB with f in S,

    R=S/(f),   A=S+fB=S+fvS.                                  (11)

Absorb the unit in q into a smooth equation w of c, so q=w^m, and
write `w=A0(u,t)+v B0(u,t)`. Since the extra term fvS in (11)
restricts to order at least b+1>=2 on c, the smooth isomorphism c->C
requires an invariant function restricting to a uniformizer. Therefore
B0 is a unit: otherwise the linear part of w would be a nonzero
multiple of u, and both u and t=v^2 would restrict to order at least
two, contradicting that requirement.

On each normalized branch gamma of D, descent gives
`tau(w)/w=zeta_gamma`, a constant (mN)-th root of unity. Generic
non-descent gives `zeta_gamma^m != 1`. In particular this ratio is
not one. As `w-tau(w)=2v B0` and B0 is a unit,

    ord_gamma(v)=ord_gamma(w),
    d=(q-tau(q))/(2v) in S,
    ord_gamma(d)=(m-1) ord_gamma(w).                        (12)

The curve D is reduced. The only possible generically nonreduced
component of f(u,v^2) over reduced R is a component t=0. There its
quadratic algebra is a double-root algebra; a nonzero scalar part
of w with its unit anti-coefficient cannot have a scalar (mN)-th
power in characteristic zero. If that scalar part is zero and m>=3,
q itself is zero, contradicting non-descent. If m=1 instead, the
scalar part A0(u,t) is divisible by t and w is a unit times v; then
c lies in the conductor component t=v^2=0, contrary to finite b.
Thus no doubled component occurs. Away from t=0 the quadratic map
is etale, so reduced R makes the entire Cartier divisor fB reduced.

The anti-coordinate of q is d, so `B/(A+Aq)=R/(d)`. The rank-two
free extension S->B and the reduced-curve intersection formula give

    2 length R/(d) = length B/(f,d)
                    = sum_gamma ord_gamma(d)
                    = (m-1) sum_gamma ord_gamma(w)
                    = (m-1)b.

This proves (10) for every positive odd m and every descended power
N>=2 under the stated conditions. For m=5, allowing a reduced
Gorenstein singularity of the downstairs conductor at a smooth source
point does not supply an extra odd unit of root-adjoining defect. The A4
normalization point and non-Gorenstein conductor points are outside
this local statement; their contributions are not assigned by it.

## An actual square-only supported hypersurface

### The hypersurface and its full conductor

Work over an algebraically closed field of characteristic zero. Choose
integers `m>=2, k>=1`, and a primitive `2m`-th root of unity zeta. In
`B=k[[t,w]]`, set

    s=1+zeta,
    P=(w-t^k)(w-zeta*t^k)
      =w^2-s*t^k*w+zeta*t^(2k),
    u=P,  v=w*P.

Then the subring generated by t,u,v is the complete hypersurface

    A=k[[t,u,v]]/(H),
    H=v^2-s*t^k*u*v+zeta*t^(2k)*u^2-u^3.              (1)

Write `R=k[[t,u]]`. The monic relation

    w^2-s*t^k*w+zeta*t^(2k)-u=0

identifies B with the free R-module `R+Rw`, while

    A=R+R*u*w.                                        (2)

Indeed, the right-hand side is a subring with basis 1,v and relation (1).
It embeds in B; conversely (1) is monic quadratic in v and gives exactly
that free R-module. Thus A is a domain, B is finite over A, and
`w=v/u` in their common fraction field. Since B is regular, B is the
normalization of A.

The entire conductor, including its scheme structure, is

    (A:B)=uB=PB.                                      (3)

For a proof, an element `a+bw` of B belongs to A precisely when `b` is
divisible by u. To multiply B back into A it suffices also to multiply by
w. The coefficient of w in `(a+bw)w` is `a+s*t^k*b`, so a must likewise
be divisible by u. This proves (3).

### The marked curve and its two contacts

Let `c=V(w)` on the normalization. Its image is the smooth curve

    C=V(U,V) in Spec A,
    U=u-zeta*t^(2k),  V=v,
    A/(U,V)=k[[t]].                                   (4)

Its full inverse ideal is

    (U,V)B=(w*(w-s*t^k), w*P).

Its radical is (w): if a prime over this ideal did not contain w, it would
contain both `w-s*t^k` and P, hence t and then w, a contradiction. The
map `c->C` is an isomorphism. This is a statement about reduced inverse
support; the inverse scheme need not be reduced.

The differential of the normalization in the transverse direction gives

    U_w|c=-s*t^k,   V_w|c=zeta*t^(2k).

Equivalently, in the smooth ambient coordinates t,U,V, the linear normal
part of the hypersurface equation has coefficients

    H_U|C=-zeta^2*t^(4k),
    H_V|C=-s*zeta*t^(3k).

The first pair has common vanishing order k, while the hypersurface's
first normal symbol has common vanishing order **3k**. These must not be
identified: the normalization map's transverse differential and the
carrier equation's normal derivative are different objects.

The conductor restriction on c is `P(t,0)=zeta*t^(2k)`, so

    b=length O_c/(P|c)=2k.                             (5)

In this example the carrier first-symbol order is `h=3k`, and the
transverse differential order is k. No inequality comparing the actual
carrier first symbol with b is disproved by replacing h with that latter
order.

### Actual power descent and the supported local intersection

Put `q=w^m`. Then

    q does not belong to A,     q^2=w^(2m) belongs to A. (6)

For the second assertion, `w^(2m)-t^(2mk)` is divisible by P, and PB is
contained in A. For the first, reduce modulo PB. The image of A in
`B/PB=k[[t]][w]/(P)` consists of constants in w. But evaluating q on
the two branches gives `t^(mk)` and `-t^(mk)`, so it cannot be constant.

Let Q be the element of A represented by `w^(2m)`, and choose any lift
of Q to `k[[t,u,v]]`. The actual two-equation pair is **(H,Q)**. It is
a height-two complete intersection: A is a domain and Q is nonzero.
Finite surjectivity of the normalization gives

    V_A(Q)=image V_B(w^(2m))=C.

At the generic point of C, the conductor is a unit because
`P(t,0)=zeta*t^(2k)` is nonzero. Normalization is an isomorphism there,
and Q has transverse order 2m. Thus the generic intersection length is
exactly 2m. Adding U as another equation would change the problem and
is not part of this construction.

For m=5, this is an actual local multiplicity-ten mate with square-only
descent. For k=2 its conductor contact is four and its carrier
first-symbol order is six. These local values alone provide no global
quintic or fixed-quartic embedding.

### Adjoining the root need not normalize

The intermediate finite ring `A'=A+Aq` is closed under multiplication
because q squared belongs to A. From (2),

    B/A = k[[t]] * [w].

In this quotient, interpolation at `w=t^k` and `w=zeta*t^k` gives

    [q]=(2/(1-zeta))*t^((m-1)*k)*[w].

It follows that

    length B/A'=(m-1)*k.                              (7)

For m=5 this is 4k, supported at the origin. The intermediate ring
agrees with its normalization in codimension one but is not normal.
Consequently it is not S2. A root-generated partial normalization must
not be assumed Cohen–Macaulay merely because A is a hypersurface and
q satisfies a monic quadratic equation: the algebra is an image of the
quadratic algebra and can acquire a finite defect.

### Scope and consequence for the main problem

This model realizes actual local square descent, finite singleton
normalization, and supported two-equation intersection together. It
does not bound the possibilities for a global conductor or the section
image of a degree-five projection. The exact distinction between the
normalization differential and the carrier first symbol is essential
when importing it into the fixed quartic's conormal calculations.

The finite defect in (7) gives a concrete geometric meaning to a possible
global root-adjoining defect: even after one descends a power, adjoining
its root can leave isolated failures of normality. Controlling the
locations and lengths of those failures requires more than their total.

## An actual singular-conductor model at the marked A4 point

There is a constructive control outside the smooth-normalization
hypothesis of [the reduced-Gorenstein formula](#reduced-gorenstein-conductors-at-a-smooth-normalization-point). In the completed normal A4 surface put

    B=k[[x,y,z]]/(xy-z^5),   c: x=z^2, y=z^3,
    q=x^3-5x^2 z^2+10x z^4-10z^6+5y z^3-y^2.

Then `div_B(q)=5c`. Indeed `x^2 q=(x-z^2)^5`; the expanded expression
has no extra divisor on either component of z=0, where it restricts
to x^3 or -y^2. Let sigma exchange x and y, and set

    s=x+y, v=x-y, Delta=s^2-4z^5=v^2, S=k[[s,z]],
    f=q+sigma(q)
     =s^3-(1+5z^2)s^2+(5z^3+10z^4-3z^5)s
       +2z^5-20z^6+10z^7,
    g=(s^2+s-5s z^2-5z^3+10z^4-z^5)/2.

Direct expansion gives `B=S+Sv` and `q=f/2+gv`. Define

    A=S+fB=S+fSv,   w=fv,
    A=k[[s,z,w]]/(H),   H=w^2-f^2 Delta.                 (13)

The free S-basis 1,w proves that this presentation embeds into B.
The ring is a domain. Adjoining v is finite, with `v^2=Delta`, and
birational, with `v=w/f`. Since B is normal it is exactly the
normalization of A. Its full conductor is fB: if `a+bv` is in the
conductor then its membership in A forces b in fS, while membership
of `(a+bv)v` forces a in fS. Conversely fB multiplies B into A.

Thus the actual conductor downstairs is the integral Gorenstein curve
`Gamma=Spec S/(f)`. With weights wt(z)=2 and wt(s)=5, the initial
equation is `-s^2+2z^5`. It is the A4 plane cusp, with normalization
`z=t^2, s=sqrt(2)t^5+...`. In particular Gamma is reduced and integral,
and D=B/fB is free of rank two over it. Moreover

    Q=q^2=f^2/4+g w+g^2 Delta belongs to A.              (14)

The root itself does not descend generically: modulo f, its
anti-coordinate is the nonzero class of g.

The smooth curve image and full inverse support are explicit. Put
`s0=z^2+z^3`, `v0=z^2-z^3`, and define C in A by

    s=s0,   w=f(s0,z)v0.

Its ring is k[[z]]. In B the first equation gives
`(v-v0)(v+v0)=0`, while the second gives `f(s0,z)(v-v0)=0`.
Since `f(s0,z)=z^4(z-1)^5`, the second sign contributes only the
origin, already on c. Hence the full reduced inverse is c and c->C
is an isomorphism.

Equations (13) and (14) alone form an actual height-two complete
intersection in the regular ambient k[[s,z,w]]. Finite surjectivity
and `div_B(q^2)=10c` prove that its reduced support is exactly C.
At generic c the conductor is a unit, so the generic intersection
multiplicity is ten. No third equation is added to force support.

Finally the conductor contact and root-adjoining defect are

    b=ord_c(f)=4,
    B/(A+Aq) = (S/(f))/(g),
    length B/(A+Aq)=5.                                 (15)

The last equality follows on the cusp normalization: the term s/2
in g has order five and the remaining terms have higher order.
This is an odd defect at a singular normalization point with a
singular integral Gorenstein conductor. It shows that the
[smooth-conductor A4 exclusion](root_descent_and_conductor_defects.md#the-marked-a4-point-cannot-lie-over-a-smooth-conductor-point)
cannot simply be extended to singular conductors.

It does not supply the desired global correction: with b=4, the
value that would repair a local contribution 2b by one is nine,
whereas (15) is five. Nor is this a projective quintic. The
[actual integral-conductor projection](quintic_conductor_geometry.md)
has a conductor singularity of embedding dimension three; the plane
cusp here has embedding dimension two. The example supplies a real
local power-descent mechanism, not a realization of that global vertex.

## A gluing control that fails the hypersurface condition

A separate explicit model shows why the correct phase and a small
conductor genus still do not guarantee a hypersurface carrier. Let
`B=k[[t,w]]`, let zeta be a primitive tenth root of unity, and let
a be nonzero. For k=2 or 3 put

    f=(t-a w^k)(t-a zeta^k w^k),   D=B/(f).

Using the original w coordinate on each branch identifies D with

    {(phi1,phi2) in k[[w1]] times k[[w2]]:
                  phi1(w)-phi2(w) is divisible by w^k}.

Embed a base curve ring by

    phi(u) |-> (phi(w1),phi(zeta w2)).

Its image lies in D exactly when all coefficients below degree k
have exponent divisible by ten. Thus the base rings in the two
cases are `R2=k[[u^2,u^3]]` and `R3=k[[u^3,u^4,u^5]]`.
Let A be the inverse image of R in B. Its full conductor is fB:
generically D is a split quadratic algebra over the diagonal base
field, whose conductor is zero, and D is torsion-free over R.

The ambient function q=w^5 restricts to `(w1^5,w2^5)`. This differs
from the base image of u^5, which is `(w1^5,-w2^5)`. Consequently
q is generically non-descending, while q^2 is the descended image of
u^10. Confusing these two pairs would incorrectly remove the
non-descent mechanism.

Nevertheless A cannot be a Gorenstein hypersurface. At degrees
1,...,k-1, the diagonal classes in D/R survive modulo the maximal
ideal of R. At degree k, D has two independent branch coefficients,
while R plus its maximal-ideal multiple of D contributes only one.
It follows that

    minimal generators of D/R >= k.

For k=2 the cusp R2 is Gorenstein, so its dualizing module has one
generator. For k=3 the monomial space curve R3 has a minimal
Hilbert–Burch resolution with two final generators, so its dualizing
module has two. In both cases

    minimal generators of omega_R = k-1 < k.

Hence `D/R` is not isomorphic to `omega_R`. This violates the local
conductor canonical sequence that a Gorenstein hypersurface A with
this regular normalization and full conductor would have. The k=3
base even has delta invariant two and embedding dimension three,
matching the numerical type of the actual quintic vertex, but its
gluing still fails this necessary carrier condition.

This excludes only these explicit two-branch pushouts. No assertion
that every delta-two conductor has this form is made, and no broader
phase classification was selected. The geometric lesson is that
power descent on a glued surface and compatibility with its required
hypersurface dualizing structure are separate conditions.

The conclusion uses the actual embeddings, ambient/base-function
distinction, full conductor and surviving module generators. It does not
rely on a numerical length comparison or an unproved phase bound.

## An actual supported square with componentwise descent

This control is in complete local rings over an algebraically closed
field of characteristic zero. Put

    B=k[[s,v]],  S0=k[[s,t]],  t=v^2,
    q=(v-s)^5=e+v d,
    e=-s(5t^2+10s^2 t+s^4),
    d=t^2+10s^2 t+5s^4,   f=e d.

Define

    A=S0+fB=S0 plus f v S0,
    W=fv,
    A=k[[s,t,W]]/(W^2-t f^2).                          (6)

This is an actual integral hypersurface with normalization B: v is
integral, `v=W/f` in the fraction field, and B is regular. Testing
multiplication by 1 and v shows that the full conductor is fB.
Downstairs Gamma has ring `R=S0/(ed)`, with five distinct reduced
branches: s=0 and the two distinct parabolas from each quadratic
factor e/s and d. It is singular at their common origin.

The actual section

    G=e^2+t d^2+2W=q^2                                (7)

has zero divisor 10c upstairs, where c is v=s. Its smooth image is

    t=s^2,   W=-256s^10,

and the full reduced inverse is c. Directly,
`e^2-t d^2=(s^2-t)^5`; substituting (7) into (6) therefore leaves
the tenth power of t-s^2, with the stated unique reduced curve.

In `B/A=(S0/(ed))v`, the class of q is multiplication by d. It is
zero generically on the two d-branches and nonzero generically on
the e-branches. In particular the components on which q descends
do meet c. The kernel and remaining quotient are

    K=(e)/(ed),   B/(A+Aq)=(S0/(d))v.                   (8)

The latter is one-dimensional; assigning it length 17 would be
incorrect. This model also has full conductor contact b=9 and actual
normal-differential order h=1 along c. Indeed f restricts to
`-256s^9`, while the normal parameter t-s^2 has first coefficient
2s in v-s. The other normal parameter has higher-order first
coefficient. Thus singular conductor gluing can have b>2h, even
with smooth normalization and an actual supported pair.

This is a formal hypersurface and pair in three ambient variables.
It is not the fixed quartic embedding, a degree-five projective
carrier, or a homogeneous octic mate. Its role is to disprove the
abstract inference that supported power forces componentwise
non-descent or the smooth-contact inequality.

## A nonreduced conductor with the same root multiplicity

Take instead

    B=k[[s,v]], t=v^2,
    A=k[[s,t,W]]/(W^2-s^4 t),   W=s^2 v,
    I=s^2B,   R=k[[s,t]]/(s^2),
    q=v^5=t^2v,   q^2=t^5 in A.

The full reduced inverse of the smooth image `t=W=0` is c:v=0.
The root and its actual descended square have divisors 5c and 10c.
The conductor is nonreduced. Nevertheless q's class generates its
canonical quotient at the generic point s=0, where t is a unit.
The remaining quotient is

    B/(A+Aq)=k[[s,t]]/(s^2,t^2) times v,

of length four, and the conductor contact with c is two. Therefore
neither reducedness nor generic failure of generation follows from
the supported square. This control is again local, with no claimed
projective quintic realization.

## The marked A4 point can meet a smooth conductor when q descends

The generic non-descent hypothesis in the
[marked A4 smooth-conductor exclusion](root_descent_and_conductor_defects.md#the-marked-a4-point-cannot-lie-over-a-smooth-conductor-point) is
essential. Use its same marked normal surface and root,

    B=k[[x,y,z]]/(xy-z^5),  c: x=z^2,y=z^3,
    s=x+y, v=x-y, Delta=s^2-4z^5,
    S0=k[[s,z]], B=S0 plus v S0,
    q=(x-z^2)^5/x^2=e+v d.

The regular expansion of q and its invariant part e are in the
[singular A4 control](square_descent_and_singular_gluing.md#an-actual-singular-conductor-model-at-the-marked-a4-point).
Its anti-invariant coefficient is

    d=(s^2+s-5sz^2-5z^3+10z^4-z^5)/2.

This time choose f=d and put

    A=S0 plus f v S0,
    W=fv,   A=k[[s,z,W]]/(W^2-f^2 Delta).

As in the previous rank-two models, B is the finite birational
normalization and the full conductor is fB. The downstairs conductor
`S0/(f)` is smooth, because the derivative of f with respect to s
at the origin is 1/2. But now the root itself descends:

    q=e+W belongs to A,   div_B(q)=5c.

The image C is smooth since z remains an ambient parameter on it.
The divisor of this actual section forces its full reduced inverse
to be c. Its conductor contact is exactly two, since

    f|c = z^2(1-z)^4/2.

Thus a smooth conductor can pass through the marked A4 normalization
point when q descends there. A global quartic root descending
everywhere on the projective quintic is excluded by R-0001; this
local control makes no such claim. Its relevance is a component of
a nonintegral conductor on which the root class vanishes generically.
One cannot use the integral-conductor A4 exclusion at that component
without first checking its non-descent hypothesis.

## What the controls establish and what remains to realize

The displayed equations are actual local hypersurfaces and two-equation
supported intersections where stated; the failed pushouts are excluded by
their dualizing modules, not by a numerical phase guess. Singular gluing can
have contact b=9 with transverse order h=1, a nonreduced conductor can still
have a generically generating root class, and a root already descending on
a smooth conductor can meet a marked A4 normalization point. The singular
A4 square example has odd defect five but does not realize the required
projective quintic vertex. None of these controls constructs the fixed
quartic or supplies a classification of singular conductor schemes.

The smooth and reduced-Gorenstein lemmas retain full conductor sequences,
actual algebra closure, finite singleton inverse support and branchwise
non-descent where required. They do not apply merely because the reduced
support of a nonreduced conductor is smooth. Characteristic zero is used
for unit-root extraction and separability of every positive power; no
unbounded-exponent Frobenius analogue is asserted. The known
[positive-characteristic constructions](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md)
therefore present no conflict.

Independent frozen-source review reconstructed each local ring,
normalization, entire conductor, actual supported pair and divisor,
root-defect length and differential distinction. Separate review covered
the arbitrary-positive-exponent contact bound, the odd-multiplicity
reflection argument (including m=1), the singular A4 model and the
non-hypersurface gluing control. Those precise scopes are reused here;
there was no new local classification or CAS campaign.
