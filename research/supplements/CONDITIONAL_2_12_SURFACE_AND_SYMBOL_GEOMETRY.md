# conditional 2 12 surface and symbol geometry

## Proof-dependency map: symbol equations to actual sextic realization

The [norm-symbol elimination](#2026-10-20-conditional-2-12-elimination) is an exact algebraic reduction in the conditional (2,12;6,16;2) setting. The [structured incidence](#2026-10-20-conditional-2-12-global-realization-incidence) combines root conditions with the [actual sextic symbol map](#2-the-exact-global-k-linear-symbol-map). Matching an [actual cubic jet](#7-first-unresolved-global-lift-the-actual-sextic-cubic-jet) is a further condition on that incidence. See the [independent incidence audit](#2026-10-20-conditional-2-12-incidence-audit) for the scope of these tests and the [realization certificate](#8-what-a-realization-would-have-to-certify) for what an actual pair must supply.

The [quadric-cycle norm](../synthesis/normalization_conductor_phase2_addendum.md#actual-quadric-cycle-norm-bridge) and [surface bound](CONDITIONAL_2_12_CONTINUATION_AND_SEXTIC_EXCLUSIONS.md#2026-10-21-conditional-2-12-geometric-audit-and-exceptional-locus) give additional restrictions under the actual supported-pair hypotheses.

The [singular gluing and conductor analysis](CONDITIONAL_2_12_SINGULAR_AND_CONDUCTOR.md#2026-10-20-conditional-2-12-singular-continuation) checks whether the local branches can be matched; the [strict-surface continuation](CONDITIONAL_2_12_CONTINUATION_AND_SEXTIC_EXCLUSIONS.md#nonnormal-conductor-budget-and-local-escape-models) introduces additional geometric hypotheses. A solution to the eight symbol equations is not, by itself, a projective sextic with the desired residual support.

Keep the explicit elimination, actual-lift polynomial test, and audit independently inspectable.

---


Permanent mathematical dossier. The (2,12) setting and every other hypothesis remain conditional as in the original arguments; full calculations, exceptional cases and failures are retained.

---

## 2026-10-20-conditional-2-12-elimination

# Conditional (2,12;6,16;2): compact norm-symbol and cubic realization incidence

Date: 2026-10-20. Status: **new exact reduction, pending independent review**. No result is changed. Work is over an algebraically closed characteristic-zero field, with the fixed curve C0 and the full generic ordinary coprime binary-CI initial ideal and actual saturated first relation required in the parent task. A bounded CAS interruption is process evidence only.

The source symbol matrix, exact image minor, and cubic layer are the new reviewed proposal in [the earlier global-realization note](#2026-10-20-conditional-2-12-global-realization-incidence). The first-incidence construction is the [STCI-R-0007](../results/quadratic_root_obstruction_model.md), used within its actual-CI interface and the separately reviewed finite singular-root bridge. The source script does not rerun accepted proofs.

## 1. Eight symbol equations are a norm factorization

Put `l=u+z*v/2`, the exact first symbol of the quadric `q=x0*x3-x1*x2`, and put

    D(z)=z^2*a(z)-2*z*b(z)+4*c(z)=sum(d_i*z^i,i=0..4).

The restriction of `alpha*f` to `l=0`, after the harmless scalar factor four, is `alpha*D`. The eight of the eleven symbol equations whose indices are not 3,6,9 say exactly that

    alpha(z)*D(z) belongs to span(1,z^3,z^6,z^9,z^12).

This has a geometric explanation: on the smooth quadric Q the sextic restriction is the square of the (1,3) curve equation times a section of O_Q(4,0), whose restriction to C0 is a binary quartic in z^3.

For four distinct roots of D in four distinct free mu3-orbits, the elementary factorization alone makes alpha unique up to scalar:

    alpha_can(z)=D(omega*z)*D(omega^2*z).

The exporter explicitly imposes `alpha_can`. The separate [quadric-cycle norm proof and its review](../synthesis/normalization_conductor_phase2_addendum.md#actual-quadric-cycle-norm-bridge) show why this is necessary for an actual supported pair under the full hypotheses, including shared orbits and endpoint multiplicities.

The formula needs no root of unity in the coefficient ring. With

    U=d0+d3*z^3, V=d1*z+d4*z^4, W=d2*z^2,

one has identically

    alpha_can=U^2+V^2+W^2-U*V-U*W-V*W,
    D*alpha_can=U^3+V^3+W^3-3*U*V*W.

The exporter checks symbolically that substitution of alpha_can makes exactly eight annihilator rows zero and leaves only rows 3,6,9 (zero-based indexing in the earlier symbol artifact).

## 2. A finite cover of the nonzero-endpoint chart

The C0-preserving torus acts by diag(1,lambda,lambda^3,lambda^4). Together with projective scaling of f, it permits the normalization d0=d4=1 wherever d0*d4 is nonzero: the two coefficients have torus weights differing by four, and the field is algebraically closed. Thus this is a finite cover of that chart; it does not cover endpoint-zero roots.

Choose four remaining root coordinates y0=b0,y1=b1,y2=b2,y3=c2. Then

    a=d2+2*y1-4*y3+(d3+2*y2)*z+z^2,
    b=y0+y1*z+y2*z^2,
    c=1/4+(d1/4+y0/2)*z+y3*z^2.

Writing T=y1-4*y3, the three surviving symbol equations are a linear system in (y0,T,y2). After dividing its first and third rows by four and its second row by two, the matrix is

    J = [ d2-d1^2       -d1       1          ]
        [ -2*d1+d2*d3   d2^2-1   2*d3-d1*d2 ]
        [ -1            -d3      d3^2-d2    ].

The constant vector is

    ((d3-d1*d2-d1^3)/4,
     (-d2-d1^2+d3^2-d1*d2*d3+d2^3)/2,
     (-d1-3*d2*d3+d3^3)/4).

Its determinant is minus

    d1^2*d2^2*d3^2-d1^2*d2^3-d1^3*d2*d3-d2^3*d3^2
    -d1*d2*d3^3+d2^4+2*d1*d2^2*d3+3*d1^2*d3^2
    -2*d2^2-4*d1*d3+1.

The exporter does **not** invert this determinant. All its rank-drop strata remain in the compact model. Changing y3 while keeping (d1,d2,d3,y0,T,y2) fixed adds `4*y3*l^2` to f; this explains why y3 is absent from the linear system.

## 3. Eight first-incidence correction variables disappear without denominators

On this chart a2=1,c0=1/4. The top four and bottom four equations of the accepted first incidence give the exact recurrences

    h3=-a0*h5-a1*h4,
    h2=-3-a0*h4-a1*h3,
    h1=-4*a1+3*b2-a0*h3-a1*h2,
    h0=-5*a0+3*b1-a0*h2-a1*h1,

    h8=-4*c1*h7-4*c2*h6,
    h9=-9/2-4*c1*h8-4*c2*h7,
    h10=-3*b0/2-16*c1-4*c1*h9-4*c2*h8,
    h11=-3*b1/2-14*c2-4*c1*h10-4*c2*h9.

Only h4,h5,h6,h7 remain. The exporter substitutes these expressions and verifies that precisely the original rows 0..3 and 12..15 become the zero polynomial. The other eight first equations are retained. Thus the base norm-symbol model on the smooth open has twelve variables and twelve equations: seven root coefficients, four h coefficients, one smooth inverse; eight first equations, three symbol equations, and the smooth-open equation. This is only an equation count, not a dimension computation.

## 4. An exact polynomial test for the actual sextic cubic lift

The fixed 22-by-22 image minor in the earlier symbol artifact defines a k-linear splitting rho. Every sextic with prescribed symbol alpha_can*f is

    rho(alpha_can*f)+eta*q^3.

Its cubic discrepancy from the canonical root correction is

    T=T0*u^3+T1*u^2*v+T2*u*v^2+T3*v^3
     =rho(alpha_can*f)_3+eta*l^3-alpha_can*G0.

The normal cubic is divisible by f in k[z,u,v] precisely when these four polynomial identities hold on the basepoint-free root locus:

    (b^2-a*c)*T0-a*b*T1+a^2*T2=0,
    b*c*T0-a*c*T1+a^2*T3=0,
    c^2*T0-a*c*T2+a*b*T3=0,
    c^2*T1-b*c*T2+(b^2-a*c)*T3=0.

To prove sufficiency, view multiplication by f as the rank-two bundle map O(7)^2 -> O(9)^4. The four displayed syzygies annihilate its image. Where a is nonzero, the first two syzygies are independent; where c is nonzero, the last two are independent; where a=c=0 and b is nonzero, the first and fourth are independent. They therefore span the entire rank-two annihilator at every point of a basepoint-free root. Vanishing of the four identities puts T in the image bundle. The corresponding quotient coefficients are global sections of O(7)^2. This retains zeros of alpha and does not divide by a,b,c or alpha in the final condition.

The compact exporter gives exactly 48 nonzero scalar coefficient equations from these four identities. It has thirteen variables including eta and the smooth inverse. The cubic equations are sufficient and necessary for the same cubic condition as the earlier 73-equation presentation on the specified open, provided the imposed norm multiplier is applicable. They do not replace the second obstruction, full spectral gluing/torsion, later sextic compatibility, or global degree-sixteen mate.

## 5. Reproduction and current computational boundary

Run

    python3 research/computations/conditional_2_12_elimination_2026_10_20.py

The exporter reconstructs the hierarchical model, whose M2 presentation reports `COMPACT_BASE_MODEL_READY` and `COMPACT_CUBIC_EQUATIONS=48`. This is an equation export, with no Groebner computation. The model is smooth-open only for the bounded CAS trial; singular-root strata remain in the parent structured incidence and are not excluded by this note.

The bounded QQ trials in `research/validation/2026-10-20-conditional-2-12-elimination/` preserve exact input files, return codes, and resource limits. Early expanded models and the first compact base model hit their 60-second CPU limits. These runs supplied **no ideal, dimension, unit, or emptiness certificate**. The final reduced cubic trial is recorded separately. No theorem may be inferred from a CPU-limited or killed process.

The precise unresolved computation is the intersection of these compact first/global-cubic equations with the inherited complete second test and full spectral torsion, together with the endpoint-zero charts. Even a nonempty answer would remain a low-order incidence rather than a global pair.


---

## 2026-10-20-conditional-2-12-global-realization-incidence

# Conditional (2,12;6,16;2): global sextic symbols and the exact remaining incidence

Date: 2026-10-20. Status: **new proposal / exact structured reduction**.
Independent audit of the new symbol map,
singular bridge, torsion presentation, and exporter is recorded in
[the audit](#2026-10-20-conditional-2-12-incidence-audit).

The output is a specified scheme of remaining necessary conditions and
its first unresolved global lifting condition. **Its emptiness or
nonemptiness is not certified.** In particular the familiar smooth seed
does not belong to the full second incidence. No low-order incidence
point is asserted to be a global pair.

## 1. Scope and inputs

Throughout, `k` is algebraically closed of characteristic zero and

    C0=[s^4:s^3t:st^3:t^4] in P3,
    E=N*_(C0/P3)=O_P1(-7)^2,
    (r,s;a,b;epsilon)=(2,12;6,16;2).

The conditional global object being tested is an actual proper pair
`F6,G16` with reduced intersection support exactly `C0`, FULL generic
ordinary initial ideal a coprime binary complete intersection of degrees
`(2,12)`, and ACTUAL degree-two relation kernel a saturated line
subbundle. The first relation is

    R=O(-16) -> Sym^2 E=O(-14)^3,
    f=a(z)u^2+b(z)uv+c(z)v^2,
    a=a0+a1*z+a2*z^2, similarly b,c.

The three homogeneous base quadratics have no common zero. The degree-six
symbol is necessarily `alpha*f`, with `alpha in H0(O(8))`, nonzero.
The degree-sixteen symbol is `beta*f`, `beta in H0(O(48))`, and in an
actual pair `(alpha,beta)` jointly generate at every point. The low-order
scheme below has no variable beta and does not assert that joint
generation has been realized.

Precisely scoped inherited premises:

* [STCI-R-0010](../results/saturated_first_relation_normal_flatness.md)
  gives normal flatness and a coprime `(2,12)` graded CI in every fiber
  under the actual supported-pair hypotheses above.
* [STCI-R-0008](../results/spectral_root_picard_criterion.md) makes the
  graded second quotient relation equivalent to the full-scheme spectral
  descent condition. Here it is `O_Z(1,-1)^12=O_Z` for the full `(2,2)`
  root `Z`.
* [STCI-R-0011](../results/moving_nonreduced_spectral_root_obstruction.md)
  excludes nonreduced moving full roots in characteristic zero; component
  degrees in the descent identity also force equal component slopes.
* [STCI-R-0007](../results/quadratic_root_obstruction_model.md) supplies
  the exact universal first incidence and complete twenty-five-pairing
  second obstruction test. Their construction is valid for all
  basepoint-free quadratic roots, including singular ones.

The smooth bridge R-0006 does not supply necessity on singular
roots. The new, separately reviewed finite bridge in
[the singular-root note, section 2](SINGULAR_ROOT_ACTUAL_PAIR_BRIDGE.md)
fills this scope gap only under the actual hypotheses above. No inference
for residual intersections or arbitrary STCI presentations is made.

## 2. The exact global k-linear symbol map

For the fixed characteristic-zero quartic, the source calculation is
independent of the existence of a supported pair. The conormal frame
has transition `z^-7` in each summand, and `O_C0(6)=O_P1(24)`.
The map is the second normal jet
`H0(I_C0^2(6)) -> H0(Sym^2 E(6))=H0(O_P1(10))^3`.
Use the accepted balanced coordinates on `x0=1`:

    (x0,x1,x2,x3)=(1,z,z^3+v,z^4+u+(3/2)*z*v).

The degree-two normal symbols of a global sextic have the form

    P(z)u^2+Q(z)uv+R(z)v^2,             deg P,Q,R <= 10.

The coordinates in the target are, in order,

    (P0,...,P10,Q0,...,Q10,R0,...,R10).

Thus the target is `H0(O(10))^3`, of dimension 33. The map is obtained
by substituting these exact affine coordinates into the homogeneous
sextic, retaining its normal degree-two terms, and homogenizing their
base coefficients to degree ten. All coefficients are in `k`; they
are not freely chosen elements of `k(C0)`.

For a completely reproducible source basis put

    q=x0*x3-x1*x2,
    A=x0^2*x2-x1^3,
    B=x0*x2^2-x1^2*x3,
    D=x2^3-x1*x3^2.

In the following order, a basis of `H0(I_C0^2(6))` is

    q^2*(x0^2,x0*x1,x0*x2,x0*x3,x1^2,x1*x2,x1*x3,x2^2,x2*x3,x3^2),
    q*A*(x0,x1,x2,x3),
    q*B*(x2,x3), q*D*(x2,x3),
    A^2,A*B,A*D,B*D,D^2.                                  (1)

The source dimension is 23, the symbol rank is 22, and the kernel is
exactly `k*q^3`. The exact `33 x 23` matrix M and a `33 x 22` image
basis are in
[the symbol JSON](../computations/conditional_2_12_symbol_map_2026_10_20.json).
Omitting `q^2*x1*x2` from (1) gives that image basis, since
`q^2*x0*x3-q^2*x1*x2=q^3` generates the kernel. Its minor on
target rows `P0,...,P10,Q0,...,Q9,R0` has determinant exactly 48.
There is also a compact equation presentation of the image `V_(6,2)`:

    P9-2Q10 = 0,
    Q0-2R1 = 0,
    P0-2Q1+4R2 = 0,
    3P1-2Q2-4R3 = 0,
    P2-2Q3+4R4 = 0,
    P3-2Q4+4R5 = 0,
    P4-4R6 = 0,
    P5-2Q6+4R7 = 0,
    P6-2Q7+4R8 = 0,
    P7+2Q8-12R9 = 0,
    P8-2Q9+4R10 = 0.                                      (2)

These eleven independent equations cut out the entire image, not a
necessary superspace of it. The new calculation checks the 84 ambient
sextic monomials: the zeroth/first normal jet matrix has rank 61.
Its kernel therefore has dimension 23, and the independent products
(1) span it. Vanishing of these jets on the dense affine curve extends
globally because the successive targets `O_C0(6)` and `E(6)` are vector
bundles on the integral curve. This establishes the sheaf-square source
and does not silently substitute an unsaturated homogeneous square.
Rank 22 and the explicit element `q^3` identify the kernel.

The independent verifier reconstructs symbols by a different direct
binomial expansion, checks first-jet rank 61, and checks rank 22,
rank 11, and `L*M=0`. The computations are over QQ and base-change to
every characteristic-zero field.

## 3. Eleven bilinear global-symbol equations

Write `alpha=sum_(i=0)^8 alpha_i*z^i`. In (2), substitute

    Pj=sum_(i=0)^8 alpha_i*a_(j-i),
    Qj=sum_(i=0)^8 alpha_i*b_(j-i),
    Rj=sum_(i=0)^8 alpha_i*c_(j-i),                         (3)

where a coefficient with index outside 0,1,2 is zero. Equations
(2)-(3) are the exact eleven bilinear equations for
`alpha*f in V_(6,2)`. Require `alpha !=0`, but do not invert alpha as
a function on the curve. Its zeros are part of the problem.

For fixed `(f,alpha)` satisfying (3), all possible actual global
sextics with that symbol form an affine line

    F=F0(alpha*f)+eta*q^3,                  eta in k.       (4)

The symbol restriction is not automatic on the universal first
incidence. At its known smooth first-compatible torsion-two seed,

    f0=(z^2+4)u^2+(z^2-8)v^2,

the eleven-by-nine multiplier matrix has rank eight, giving precisely
one projective multiplier,

    alpha0=z^8-8z^6+96z^4+256z^2+1024.                     (5)

The second obstruction at this seed is `1/8`, so it lies outside the
combined incidence. The [cubic comparison](#7-first-unresolved-global-lift-the-actual-sextic-cubic-jet)
also excludes all of its actual sextic lifts.

At `(f0,h0,alpha0)`, adjoining the eleven equations to `A_f h=d_f`
gives a Jacobian of rank 26 in 27 rows and 30 affine variables
`(f9,h12,alpha9)`. Removing the two projective scaling directions gives
tangent dimension two. The rank-eight multiplier minor stays invertible
on a neighborhood of the seed. On that neighborhood in the membership
locus it determines the normalized multiplier regularly, so the projected
incidence has the same tangent dimension. The first incidence `K1` is
smooth of projective dimension four at `[f0]`. Thus symbol membership
removes first-compatible tangent directions. The calculation is local
to the seed, with no dimension conclusion for the full incidence or its
intersection with the second obstruction and spectral torsion. The
[independent reconstruction](#2-independent-linear-algebra-reconstruction)
checks the Jacobian against the saved first-incidence input.

## 4. Necessity of both ambient tests at singular roots

The newly reviewed bridge is short enough to make the new hypothesis
interface explicit. At any closed base point, R-0010 supplies a local
relative initial ideal `(f2,g12)` with coprime fiber symbols. Choose
actual local lifts `P,H` in the ideal, of orders 2 and 12. Initial-order
reduction and Krull intersection give `I=(P,H)` in the actual local
ring. The pair `(F,G)` differs by an invertible matrix.

On the blowup divide BOTH original equations by the same exceptional
power `t^2`. Near each point of the full root, `H/t^12` is a unit by
fiberwise coprimality, so the actual transformed ideal is

    (P/t^2,t^10*H/t^12)=(p,t^10).                          (6)

The restriction `p mod t` is the Cartier equation of the root on E;
therefore `(p,t)` is a regular sequence, including at singular root
points. The principal ideals modulo `t^10` glue from the actual ideal
and give compatible embedded Cartier lifts through `E9`. Smoothness
of the surface `(p)` is unnecessary. This proves necessity of the
first and second obstruction tests for this conditional configuration.
It does not construct such a lift from an arbitrary incidence point.

Let `FIRST(f,h)` be the sixteen equations `A_f*h=d_f`, with the exact
matrix and Cech bases of R-0007; `h` has twelve coordinates and is
unique when it exists. Let `SECOND(f,h)` be ALL twenty-five Plucker
residues from the accepted global compression, not a selected subset
or a coefficient-chart test. The exporter uses exactly these inherited
equations, without their old smooth-discriminant inverse. No inherited
proof or seed verifier is rerun.

## 5. Full spectral torsion, root types, and actual gluing

Set `S=P1_base x P1_direction`, `Z=(f)`, and `L=O_Z(1,-1)`.
The nonreduced-root obstruction and the component degree of
`L^12=O` restrict Z to a reduced integral `(2,2)` curve or two distinct
`(1,1)` components. Nonreduced fibers of either degree-two projection
are allowed; the full curve is reduced.

Uniformly for every `(2,2)` Cartier divisor,

    0 -> O_S(-1,-3) -> O_S(1,-1) -> L -> 0

gives `H0(Z,L)=0`; in particular `L` is never trivial. This gives the
following exact interpretation of the spectral locus.

| Root type | Condition and outcome |
| --- | --- |
| Smooth integral genus one | Retain the actual nonidentity `L in Pic^0(Z)[12]`. |
| Integral nodal | Retain its actual conductor identification `lambda in k*`, with `lambda^12=1`, `lambda!=1`. |
| Integral cuspidal | `Pic^0=G_a` is torsion free in characteristic zero; excluded. |
| Two transverse `(1,1)` components, two nodes | Retain `lambda=g1/g2`, the ratio of the two actual node identifications; `lambda^12=1`, `lambda!=1`. |
| Two tangent `(1,1)` components | The length-two conductor gluing gives `Pic^0=G_a`; excluded. |

For the nodal case the degree-zero pullback to the rational
normalization is always trivial. That fact discards the obstruction
unless the two fibers over the node are also identified. For the
two-node pair both identifications must be retained; either one alone
can be normalized away. Explicit invariant formulas, the conductor
jets in the additive cases, and the finite bridge proof are in
[the gluing note](SINGULAR_ROOT_ACTUAL_PAIR_BRIDGE.md).

A sparse matrix retains all these conditions in the ORIGINAL nine
coefficients, without choosing normalization coordinates:

    T12(f): H1(O_S(10,-14)) -> H1(O_S(12,-12)),
    H0(Z,L^12)=ker T12(f).                                  (7)

Both spaces have dimension 143. In affine direction `w=v/u`, use
source basis `z^i*w^m`, `0<=i<=10,-13<=m<=-1`, and target basis
`z^j*w^n`, `0<=j<=12,-11<=n<=-1`. With
`f=sum f_(p,q) z^p w^q`, the matrix entry is

    T12[(j,n),(i,m)]=f_(j-i,n-m)                            (8)

if both differences are in 0,1,2, and zero otherwise. This matrix has
1089 nonzero polynomial entries and determinant homogeneous degree143.
On the reduced equal-slope locus a nonzero section of `L^12` is
nowhere zero: its degree on every component is zero and connectedness
propagates nonvanishing. Thus `det T12=0` is exactly full triviality,
including gluing. On this zero locus the matrix has corank one, so
the projective nonzero-kernel incidence and the determinant zero
scheme are locally isomorphic; neither forgets infinitesimal scheme
structure. The explicit relative argument is in the gluing note.

## 6. The exact remaining scheme

Here is one open coefficient presentation of the reduced equal-slope
root locus, avoiding an unspecified union of charts. For three binary
quadratics `p,q,r`, let `S(p,q,r)` be the 4x6 matrix whose columns
are the coefficient vectors of `p,zp,q,zq,r,zr` in homogeneous
degree three. Define B inside P8 by

    rank S(a,b,c)=4,
    rank S(a0+b0*w+c0*w^2,
           a1+b1*w+c1*w^2,
           a2+b2*w+c2*w^2)=4,
    not all coefficients of b^2-4*a*c are zero.             (9)

The first rank means finite flat over the base; the second excludes
constant-direction components. The last means generically separable,
hence reduced in characteristic zero. A reduced `(2,2)` divisor
finite over both rulings is either integral or the union of two
`(1,1)` curves. Consequently (9) loses no spectral-torsion candidate
and precisely supplies the locus needed for (7). It imposes no
smoothness discriminant inverse.

On the affine cone over B, define the remaining necessary incidence

    S2 = { (f,h,alpha,[v]) :
             L*coeff(alpha*f)=0,
             FIRST(f,h)=0,
             SECOND(f,h)=0,
             T12(f)*v=0,
             alpha!=0, [v] in P142 } / (G_m x G_m).        (10)

The two quotient scalings are `f -> lambda*f` and
`alpha -> mu*alpha`; h is invariant. The projective v has its own
usual scalar quotient. This is 11 symbol equations, 16 first
equations, 25 COMPLETE second equations and 143 sparse linear-kernel
equations. It is equivalently the incidence with `det T12(f)=0`
and no v. All constructions are over QQ and then base-change to k.

Equation (10), including the open (9), is the precise remaining
scheme supplied here. It has the smooth-root locus and the full
nodal and two-node gluing conditions; cusps and tangent pairs have
no points in its torsion part by section 5. No statement about its
nonemptiness, components, or dimension is made without an exact
calculation. In particular failure to carry out elimination is not
evidence of survival.

The exporter writes this ideal using 173 affine cone variables; it
also adjoins 39 otherwise unused variables for the optional next
global lift. Restrict to the specified five opens and take the three
scalar quotients to read (10). `D(J)` means complement of `V(J)`;
one must not invert every generator of an open ideal, which would
discard charts. No saturation or elimination was launched.

## 7. First unresolved GLOBAL lift: the actual sextic cubic jet

K1 and K2 say the ROOT admits its first two compatible embedded
corrections. They do not imply that the actual sextic coefficients
allowed by (1) vanish on that lift. On K1 let `G0` be the canonical
first-chart cubic correction from the accepted construction
(`G0=nonnegative_z(S3)`). It has base degree at most one.

Take actual GLOBAL coefficients `c=(c0,...,c22) in k^23` in (1).
Let C be the `40 x 23` cubic-jet matrix in the symbol JSON, ordered
by `z^j*u^(3-i)*v^i`, `i=0..3,j=0..9`. The first unresolved global
condition is the following finite incidence extending (10):

    M*c=coeff(alpha*f),
    C*c-coeff(alpha*G0)=coeff(f*(ell(z)*u+m(z)*v)),
    deg ell,m <= 7.                                       (11)

There are 33 symbol and 40 cubic equations in the 23 actual global
sextic coefficients and 16 quotient coefficients. Equivalently,
using (4), the condition is

    [ F_(0,3)(alpha*f)+eta*(u+(1/2)z*v)^3-alpha*G0 ] mod f=0.

The first-chart degrees satisfy `deg F3<=8` and `deg(alpha*G0)<=9`.
Basepoint freeness at infinity makes the collective base degree of `f`
equal to two. The leading binary forms of `f` and a nonzero quotient
linear form have nonzero product, so the quotient has degree at most seven.
The residue is intrinsically a global section of `O_Z(3,3)`
(dimension 12), so its vanishing over this dense chart extends to
infinity. A change of cubic representative by a multiple of `f` is
absorbed by the quotient coefficients. The test uses polynomial
divisibility and retains every zero of `alpha`.

For the seed in section 3, `G0=(z/8)u^2v-(3/4)uv^2+(z/8)v^3`.
The `73 x 39` system (11) has coefficient rank 39 and augmented rank 40.
The [exact annihilating row](../synthesis/normalization_conductor_phase2_addendum.md#exact-failed-seed-the-row-also-kills-the-free-lift)
annihilates all 23 sextic and sixteen correction columns, including the
cubic direction of `q^3`, and pairs with the target to `-384`. This
excludes the entire affine line (4) at that seed. The independent audit
reconstructs the [matrices and pairing](#2-independent-linear-algebra-reconstruction).

The exporter supplies the equations (11) as `nextGlobalLiftIdeal`,
but their feasibility on S2 has not been determined. This is the
first unresolved condition in GLOBAL lifting. The next ABSTRACT
root-lifting obstruction is different: after the two accepted stages
it is the normal degree-five correction, or exceptional stage E3.
Even solving (11) would still leave quartic and higher sextic
compatibility, higher root stages through E9, and the global mate.

## 8. What a realization would have to certify

An abstract graded second quotient relation is not a globally split
polynomial generator. Neither the projective torsion vector in (10)
nor the quotient coefficients in (11) are a degree-sixteen equation.
A realization requires actual homogeneous `F6,G16` with coefficients
in k. In the actual two-dimensional generic local ring along C0,
one must exhibit invertible generator operations producing order-two
P and order-twelve H, verify all required cancellations through
order eleven, and show that the FULL resulting initial forms
`f2,g12` are coprime. With coprime initial forms the standard-basis
criterion gives the full initial ideal `(f2,g12)` and length
`2*12=24`; merely finding a degree-twelve relation does not.

One must also prove the global homogeneous gcd is one. Bézout then
gives the complete intersection degree `6*16=96`, while C0 already
contributes `4*24=96`. Purity of the complete intersection leaves
no residual curve or isolated embedded component. This is the
global support argument; a generic finite-jet calculation cannot
replace the gcd check. The necessary implication used earlier
assumed sole reduced support; this sufficiency check does not assume
the desired conclusion in advance.

The new global-symbol restriction is an exact obstruction to
realization and is not automatic on first-compatible roots. It has
not been shown to empty the second-compatible spectral locus. The
structured residual scheme (10) and the next concrete global
condition (11) are the stopping point, as requested.

## 9. Reproduction and verification limits

The [symbol producer](../computations/conditional_2_12_symbol_map_2026_10_20.py)
writes the [exact matrices and seed certificate](../computations/conditional_2_12_symbol_map_2026_10_20.json).
The tangent comparison reads the [saved first-incidence Jacobian](../computations/generalization_quadratic_root_curve_universal_incidence.json).
Its SHA256 is recorded in the symbol output. The
[independent direct-binomial verifier](../computations/conditional_2_12_symbol_independent_audit_2026_10_20.py)
writes a [separate reconstruction](../computations/conditional_2_12_symbol_independent_audit_2026_10_20.json).
The [structured exporter](../computations/conditional_2_12_structured_incidence_2026_10_20.py)
uses the [inherited first and second equation generator](../computations/generalization_quadratic_root_global_second_model.py).

Run from the repository root in a scratch checkout, since these scripts
write their outputs next to the inputs. The Python scripts use only the
standard library.

```sh
python3 research/computations/conditional_2_12_symbol_map_2026_10_20.py
python3 research/computations/conditional_2_12_symbol_independent_audit_2026_10_20.py
python3 research/computations/conditional_2_12_structured_incidence_2026_10_20.py
M2 --script research/computations/conditional_2_12_structured_incidence_2026_10_20.m2
```

The final command constructs the ideals and reports `STRUCTURED_MODEL_READY`
and `NEXT_GLOBAL_LIFT_EXPORTED`. This checks the equation presentation.
Elimination, nonemptiness and realization remain open at this level.




---

## 2026-10-20-conditional-2-12-incidence-audit

# Independent audit of the conditional (2,12;6,16;2) incidence

Date: 2026-10-20. Reviewer: `incidence_audit` worker, separate from the
symbol-map and singular-gluing authors.

Status: **PASS for the exact reductions specified below; no
emptiness certificate, nonemptiness certificate, or global realization.**

## 1. Scope and dependencies

The field is algebraically closed of characteristic zero, the curve is
`C0=[s^4:s^3t:st^3:t^4]`, and the conditional actual pair has degrees
`6,16`, FULL generic coprime binary ordinary initial CI `(2,12)`, and
ACTUAL saturated first relation `R=O(-16) -> Sym^2 E`, with
`E=O(-7)^2`. Thus the first root is a basepoint-free form `f` of class
`(2,2)`. All actual-CI necessity statements also require sole reduced
support `C0`; residual intersections are outside this bridge.

inputs are [R-0010](../results/saturated_first_relation_normal_flatness.md),
[R-0011](../results/moving_nonreduced_spectral_root_obstruction.md),
[R-0008](../results/spectral_root_picard_criterion.md), and the literal
universal obstruction model in
[R-0007](../results/quadratic_root_obstruction_model.md). Their inherited
proof computations were not rerun. The singular finite bridge reviewed
here is a **new argument**, not a silent extension of R-0006.

The new source artifacts reviewed are
[symbol-map generator](../computations/conditional_2_12_symbol_map_2026_10_20.py),
[symbol data](../computations/conditional_2_12_symbol_map_2026_10_20.json),
[singular-gluing proposal](SINGULAR_ROOT_ACTUAL_PAIR_BRIDGE.md),
and [combined exporter](../computations/conditional_2_12_structured_incidence_2026_10_20.py).

## 2. Independent linear-algebra reconstruction

The new independent program

    python3 research/computations/conditional_2_12_symbol_independent_audit_2026_10_20.py

uses only standard-library rational arithmetic and does not import the
producer. Its [output](../computations/conditional_2_12_symbol_independent_audit_2026_10_20.json)
records the following exact checks.

1. For a degree-six monomial `x0^a x1^b x2^c x3^d`, put
   `e=b+3c+4d`. Its restriction, `x2` derivative, and `x3` derivative
   have coefficients respectively `1*z^e`, `c*z^(e-3)`, and
   `d*z^(e-4)`. The resulting first-jet matrix has rank `61` among
   the `84` sextic monomials. Hence `h0(I_C0^2(6))=23`.
2. The 23 supplied global source polynomials have independent ambient
   coefficient vectors and vanish to first order, so they span the
   full sheaf section space rather than just a degree-six ideal-product
   subspace.
3. Independently expanding
   `x2=z^3+v`, `x3=z^4+u+(3/2)zv` reconstructs the entire `33 x 23`
   second-symbol matrix, and also the `40 x 23` cubic-layer matrix.
   For the second layer, choosing `p` copies of `v` from `x2`, and
   `q,r` copies of `u,(3/2)zv` from `x3`, uses `p+q+r=2` and scalar

       binom(c,p) multinomial(d;q,r,d-q-r) (3/2)^r,

   with base exponent `b+3(c-p)+4(d-q-r)+r`. Cancellations are
   performed before checking the stated base-degree bounds.
4. The full symbol matrix and its 22 proposed image columns have rank
   `22`. The eleven supplied annihilators are independent and kill
   the full symbol matrix. Thus they cut out its image exactly.
5. The NEW seed membership matrix has rank eight and the stated
   multiplier lies in its kernel. Using the saved accepted first
   Jacobian as input, independently differentiating the eleven new
   equations gives combined Jacobian rank 26, so the claimed
   projective tangent dimension two is correct. The independent
   cubic comparison has matrix rank 39, augmented rank 40; the
   displayed witness kills every source/quotient column and pairs
   with its target to `-384`. This checks only the new comparisons,
   without reopening the already obstructed seed.

The kernel is one-dimensional. The nonzero polynomial `q^3`, where
`q=x0*x3-x1*x2`, has order three along the curve and belongs to the
source, so it is precisely that kernel. These checks establish the
requested linear map and image; they do not establish any root or
ambient incidence nonempty.

## 3. Finite bridge at singular roots

The new proof in the singular-gluing note passes the following
independent reconstruction. R-0010 gives the FULL relative graded
ideal locally generated by `f2,g12`, coprime in every fiber. Local
lifts `P,H` in the actual ideal generate it: normal-order reduction
puts the ideal inside `(P,H)+I_C^N` for every `N`, and Krull
intersection in the actual local quotient gives equality. Since
both these and the original two equations minimally generate the
same height-two CI ideal, their change matrix is invertible in the
actual local ring.

The original order-two symbols jointly generate the line subbundle
`R`. Their coefficients `alpha` of degree `8` and `beta` of degree
`48` therefore have no common base zero. Both are nonzero, since a
single section of either positive-degree line bundle cannot generate
everywhere. Divide BOTH original equations by the common exceptional
order two. At every root point, the transformed ideal is

    (P/t^2, t^10 H/t^12)=(p,t^10),

because the reduction of `H/t^12` is nonzero at every root direction
by the fiberwise coprimality. No smoothness of `f=0` is needed.
The sequence `(t,p)` is regular because `p mod t` is the Cartier
equation of the root in the smooth exceptional surface. Thus modulo
`t^10` the local ideals are Cartier and glue as the same actual
transformed ideal. This gives the embedded lift through `E9`, so the
first and second ambient classes necessarily vanish also at singular
roots. The argument retains the exceptional power `t^10` throughout.

The review found no use of a UFD on a singular strict surface, no
replacement of the actual local ring by its generic fiber, and no
saturation that removes exceptional structure. **PASS under the
stated actual supported-CI hypotheses.**

## 4. Root strata and the torsion presentation

R-0011 forces a reduced equal-slope root, hence an integral `(2,2)`
curve or two distinct `(1,1)` curves. The universal restriction
sequence

    0 -> O(-1,-3) -> O(1,-1) -> L -> 0,

gives `H0(L)=0`, so `L=O_Z(1,-1)` is never trivial. The generalized
Jacobian of a cuspidal root, or of two `(1,1)` components tangent
at one length-two intersection, is additive and has no nonzero
12-torsion in characteristic zero. These strata are excluded.
For an integral nodal root the actual branch gluing parameter is in
`G_m`; for two transverse nodes it is the ratio of the two conductor
identifications. In either case the condition is `lambda^12=1`,
with `lambda != 1`. Normalization degrees alone would erase it.

The singular note's ruling-coordinate formula for the integral nodal
parameter was checked: if `x=[X0:X1]`, `y=[Y0:Y1]` on the normalization
and `p,q` map to the node, then

    lambda=Yj(p) Xi(q)/(Xi(p) Yj(q))

in charts nonzero at the node. The equal homogeneous degrees make
this independent of lifts of `p,q`; changing branch order inverts it.

The torsion sequence

    0 -> O(10,-14) --f--> O(12,-12) -> L^12 -> 0

has two 143-dimensional `H1` groups and zero ambient `H0`. The
proposed matrix entries are the correct multiplication entries:

    T[(k,ell),(i,j)]=f_(k-i,j-ell),

for `0<=i<=10`, `1<=j<=13`, `0<=k<=12`, `1<=ell<=11`, with out-of-range
coefficients zero. A nonzero kernel is equivalent to a section of
`L^12`. On the connected reduced equal-slope locus a nonzero section
of a multidegree-zero line bundle is nowhere zero: nonvanishing
propagates between components through their intersections. Thus this
is equivalent to `L^12=O_Z`, including the actual nodal gluing data.
At a torsion point the matrix has corank one; an invertible
142-minor gives a local scalar presentation by its determinant.
Projectivizing the nonzero kernel vector has the same local scheme
structure. Relative triviality allows the usual line bundle pulled
back from the coefficient base; no global choice of trivialization
over all parameter space is asserted.

The combined exporter imposes rank four on the two `4 x 6`
quadratic Sylvester multiplication matrices. These conditions mean
that the root is finite in both rulings. Along with a nonzero
binary discriminant polynomial, they imply exactly the reduced
integral/two-`(1,1)` alternative above. Consequently they remove
unbalanced reducible roots before using the kernel criterion. This
order matters: on an unbalanced reducible root a section can be
supported on one component, and a zero determinant alone would give
a false torsion test. **PASS for the specified open scheme.**

## 5. The first unresolved global lift is genuinely additional

The bare structured scheme combines eleven symbol-image equations,
sixteen universal first equations, twenty-five complete second
pairings, and 143 torsion-kernel equations, on the opens just
specified, with nonzero `alpha` and nonzero projective kernel vector.
No elimination has proved that scheme empty or nonempty.

Its first unresolved GLOBAL lifting condition is already cubic.
Write `F=sum c_i B_i` in the 23 actual global sextic basis elements.
The symbol condition is `M c=coeff(alpha*f)`. If the first embedded
root lift on the first base chart is `f+G0`, the actual pair would
give, below normal degree twelve, `F=A*P`. Consequently

    F3-alpha*G0 = f*(ell(z) u+m(z) v).                  (*)

This must hold with actual global sextic coefficients `c_i in k`.
One must never divide by `alpha`, since it necessarily has base
zeros. The symbol condition determines `F` only modulo `k*q^3`;
that one freedom does not remove the necessity of (*).

The exported extension keeps all 23 coefficients and imposes the
33 symbol equations and 40 cubic coefficient equations, with
`deg ell,deg m<=7`. These bounds are sufficient: the numerator in
(*) has base degree at most nine, while the collectively degree-two
form `f` has nonzero top coefficient vector on the basepoint-free
infinity chart. Polynomial divisibility on the affine chart is
equivalent to vanishing of the resulting global residue on the full
reduced root, so it retains the points over infinity. Geometrically
this residue belongs to `H0(O_Z(3,3))`, of dimension `16-4=12`.

The extension is exported as the **next condition**, not claimed
soluble. The next abstract ambient root obstruction after the
complete second test is normal degree five (`E3`). That abstract
condition is distinct from matching the globally permitted sextic
jets; it cannot replace (*).

## 6. Eventual realization certificate and stopping boundary

Even if the low-order or cubic extension has a point, actual
realization still requires homogeneous `F6,G16` with coefficients
in `k`, compatible higher jets, and no common global polynomial
factor. Over `K=k(C0)`, a finite degree-twelve standard-basis
certificate may be expressed by a truncated multiplier `Q` such
that

    H=G-QF has order 12,
    gcd(in_2(F),in_12(H))=1 in K[u,v].

The vanishing of all normal terms of `H` below twelve and the full
binary resultant nonvanishing are mandatory. The invertible
generator change then makes the coprime regular initial pair a
standard basis; a partial common-root test or isolated leading
symbol cancellation is insufficient. The resulting local CI length
is `2*12=24`.

Finally the global gcd condition makes `(F,G)` a proper projective
CI of degree `6*16=96`. Its contribution along `C0` is
`24*deg C0=24*4=96`; effectiveness and purity then leave no residual
curve, and no isolated component of this projective CI. This is
the required global gcd/Bezout step, conditional on the actual
global equations. No equation search or realization is undertaken
here; the present contribution stops at the structured incidence
and its explicit first missing global lift.

## 7. Final assembled-note review

The final [assembled proposal](#2026-10-20-conditional-2-12-global-realization-incidence)
was reviewed against the source order, target order and exact JSON.
The source basis list and eleven image forms have the correct
indices. The independent determinant of the indicated 22-row
image minor is `48`. The T12 exponent convention with negative
Laurent powers uses direction difference `n-m`, as written in the
assembled note and exporter; the singular note's positive indices
give the equivalent difference `j-ell`.

The new tangent comparison proves nonautomatic membership on K1
only; the cubic seed certificate does not newly exclude a point
of the full second incidence, and the assembled note states that
limitation. The scheme's nonemptiness remains unproved. The
eventual global gcd/Bezout paragraph correctly requires actual
global equations first and does not infer support solely from a
low-order incidence. No current mathematical defect was found in
these scoped claims. Final outcome: **PASS for the exact structured
reduction, proposed singular bridge and first unresolved global
lift; a global realization remains outside
this review.**
