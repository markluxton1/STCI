# conditional 2 12 surface and symbol geometry

Permanent mathematical dossier. The (2,12) setting and every other hypothesis remain conditional as in the original arguments; full calculations, exceptional cases and failures are retained.

---

## 2026-10-20-conditional-2-12-elimination

# Conditional (2,12;6,16;2): compact norm-symbol and cubic realization incidence

Date: 2026-10-20. Status: **new exact reduction, provisional pending independent review**. No canonical result is changed. Work is over an algebraically closed characteristic-zero field, with the fixed curve C0 and the full generic ordinary coprime binary-CI initial ideal and actual saturated first relation required in the parent task. A bounded CAS interruption is process evidence only.

The source symbol matrix, exact image minor, and cubic layer are the new reviewed proposal in [the earlier global-realization note](2026-10-20-conditional-2-12-global-realization-incidence.md). The first-incidence construction is the promoted [STCI-R-0007](../results/quadratic_root_obstruction_model.md), used within its actual-CI interface and the separately reviewed finite singular-root bridge. The source script does not rerun accepted proofs.

## 1. Eight symbol equations are a norm factorization

Put `l=u+z*v/2`, the exact first symbol of the quadric `q=x0*x3-x1*x2`, and put

    D(z)=z^2*a(z)-2*z*b(z)+4*c(z)=sum(d_i*z^i,i=0..4).

The restriction of `alpha*f` to `l=0`, after the harmless scalar factor four, is `alpha*D`. The eight of the eleven symbol equations whose indices are not 3,6,9 say exactly that

    alpha(z)*D(z) belongs to span(1,z^3,z^6,z^9,z^12).

This has a geometric explanation: on the smooth quadric Q the sextic restriction is the square of the (1,3) curve equation times a section of O_Q(4,0), whose restriction to C0 is a binary quartic in z^3.

For four distinct roots of D in four distinct free mu3-orbits, the elementary factorization alone makes alpha unique up to scalar:

    alpha_can(z)=D(omega*z)*D(omega^2*z).

The stronger claim that this multiplier is necessary on **every actual supported pair**, including shared orbits and endpoint multiplicities, uses the separate quadric-intersection norm argument developed in parallel. The present exporter does not substitute generic factorization for that missing hypothesis: it explicitly imposes alpha_can. Its integration into the all-root necessity statement must cite that separate argument and its audit.

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
    /opt/homebrew/bin/M2 --script research/computations/conditional_2_12_elimination_2026_10_20.m2

The latter loads the hierarchical model and reports `COMPACT_BASE_MODEL_READY` and `COMPACT_CUBIC_EQUATIONS=48`. It launches no Groebner computation. The model is smooth-open only for the bounded CAS trial; singular-root strata remain in the parent structured incidence and are not excluded by this note.

The bounded QQ trials in `research/validation/2026-10-20-conditional-2-12-elimination/` preserve exact input files, return codes, and resource limits. Early expanded models and the first compact base model hit their 60-second CPU limits. These runs supplied **no ideal, dimension, unit, or emptiness certificate**. The final reduced cubic trial is recorded separately. No theorem may be inferred from a CPU-limited or killed process.

The precise unresolved computation is the intersection of these compact first/global-cubic equations with the inherited complete second test and full spectral torsion, together with the endpoint-zero charts. Even a nonempty answer would remain a low-order incidence rather than a global pair.


---

## 2026-10-20-conditional-2-12-global-realization-incidence

# Conditional (2,12;6,16;2): global sextic symbols and the exact remaining incidence

Date: 2026-10-20. Status: **new proposal / exact structured reduction**.
No canonical result is promoted. Independent audit of the new symbol map,
singular bridge, torsion presentation, and exporter is recorded in
[the audit](2026-10-20-conditional-2-12-incidence-audit.md).

The output is a specified scheme of remaining necessary conditions and
its first unresolved global lifting condition. **Its emptiness or
nonemptiness is not certified.** In particular the familiar smooth seed
does not belong to the full second incidence. No low-order incidence
point is asserted to be a global pair.

## 1. Scope and inherited authority

Throughout, `k` is algebraically closed of characteristic zero and

    C0=[s^4:s^3t:st^3:t^4] in P3,
    E=N*_(C0/P3)=O_P1(-7)^2,
    (r,s;a,b;epsilon)=(2,12;6,16;2).

The conditional global object being tested is an actual pair
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

The promoted smooth bridge R-0006 does not supply necessity on singular
roots. The new, separately reviewed finite bridge in
[the singular-root note, section 2](2026-10-20-conditional-2-12-singular-gluing.md)
fills this scope gap only under the actual hypotheses above. No inference
for residual intersections or arbitrary STCI presentations is made.

## 2. The exact global k-linear symbol map

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
Omitting `q^2*x1*x2` from (1) gives that image basis. Its minor on
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

the eleven equations permit precisely one projective multiplier,

    alpha0=z^8-8z^6+96z^4+256z^2+1024.                     (5)

Thus the new condition alone does not exclude that root. The accepted
second obstruction excludes it, so (5) is not a witness of a point in
the combined scheme. The optional new cubic comparison in section 7
also excludes this seed, but supplies no additional exclusion of the
already second-compatible locus. Exact seed and tangent evidence is
kept in the symbol artifact; finite sample success or failure is not a
global elimination result.

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
The promoted nonreduced-root obstruction and the component degree of
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
[the gluing note](2026-10-20-conditional-2-12-singular-gluing.md).

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

The first-chart degrees suffice: `deg F3<=8`, `deg(alpha*G0)<=9`,
and basepoint freeness at infinity means the collective base degree
of f is two; a quotient linear form needs degree at most seven.
The residue is intrinsically a global section of `O_Z(3,3)`
(dimension 12), so its vanishing over this dense chart extends to
infinity. It is polynomial divisibility and retains every zero of
alpha. No rational division by alpha is permitted.

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

New artifacts:

* [symbol producer](../computations/conditional_2_12_symbol_map_2026_10_20.py)
  and [exact matrices](../computations/conditional_2_12_symbol_map_2026_10_20.json);
* [independent direct-binomial audit](../computations/conditional_2_12_symbol_independent_audit_2026_10_20.py)
  and its JSON evidence;
* [structured exporter](../computations/conditional_2_12_structured_incidence_2026_10_20.py),
  [M2 presentation](../computations/conditional_2_12_structured_incidence_2026_10_20.m2),
  and [metadata](../computations/conditional_2_12_structured_incidence_2026_10_20.json);
* [singular bridge and full gluing proof](2026-10-20-conditional-2-12-singular-gluing.md)
  and [independent review](2026-10-20-conditional-2-12-incidence-audit.md).

Run the three new Python scripts with `python3`; they use only the
standard library. Load the exported M2 file with
`/opt/homebrew/bin/M2 --script research/computations/conditional_2_12_structured_incidence_2026_10_20.m2`.
The M2 load constructs the equations and reports MODEL_READY; this
does NOT compute a Groebner basis, determine emptiness, or certify
realization. Canonical metadata validation is a separate integrity
check, not a proof of any new mathematical assertion.

The command outcomes, new-file hashes, and local-link checks are
preserved in [the execution record](../validation/2026-10-20-conditional-2-12/execution-record.json).


---

## 2026-10-20-conditional-2-12-surface-bound

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


---

## 2026-10-20-conditional-2-12-incidence-audit

# Independent audit of the conditional (2,12;6,16;2) incidence

Date: 2026-10-20. Reviewer: `incidence_audit` worker, separate from the
symbol-map and singular-gluing authors.

Status: **PASS for the exact reductions specified below; no promotion,
emptiness certificate, nonemptiness certificate, or global realization.**

## 1. Scope and dependencies

The field is algebraically closed of characteristic zero, the curve is
`C0=[s^4:s^3t:st^3:t^4]`, and the conditional actual pair has degrees
`6,16`, FULL generic coprime binary ordinary initial CI `(2,12)`, and
ACTUAL saturated first relation `R=O(-16) -> Sym^2 E`, with
`E=O(-7)^2`. Thus the first root is a basepoint-free form `f` of class
`(2,2)`. All actual-CI necessity statements also require sole reduced
support `C0`; residual intersections are outside this bridge.

Promoted inputs are [R-0010](../results/saturated_first_relation_normal_flatness.md),
[R-0011](../results/moving_nonreduced_spectral_root_obstruction.md),
[R-0008](../results/spectral_root_picard_criterion.md), and the literal
universal obstruction model in
[R-0007](../results/quadratic_root_obstruction_model.md). Their inherited
proof computations were not rerun. The singular finite bridge reviewed
here is a **new argument**, not a silent extension of R-0006.

The new source artifacts reviewed are
[symbol-map generator](../computations/conditional_2_12_symbol_map_2026_10_20.py),
[symbol data](../computations/conditional_2_12_symbol_map_2026_10_20.json),
[singular-gluing proposal](2026-10-20-conditional-2-12-singular-gluing.md),
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

The final [assembled proposal](2026-10-20-conditional-2-12-global-realization-incidence.md)
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
lift; canonical promotion and a global realization remain outside
this review.**


---

## 2026-10-20-conditional-2-12-symbol-map

# Exact global sextic symbol map in the conditional (2,12;6,16;2) lane

Date: 2026-10-20. Status: **new exact reduction and evidence; independently
reviewed proposal, no canonical promotion**. See
[the independent audit](2026-10-20-conditional-2-12-incidence-audit.md).
Work over an algebraically closed field of characteristic
zero with `C0=[s^4:s^3t:st^3:t^4]`. The intended application assumes the
full generic ordinary initial ideal is a coprime binary CI of degrees
`(2,12)` and the actual first relation is saturated. This note computes
one global-symbol restriction and its first subsequent sextic lifting
condition. It does not prove that the combined root incidence is empty.

## Inputs and authority

The balanced conormal `E=O_P1(-7)^2`, the exact embedded chart, and the
universal first ambient incidence are used as accepted inputs from
[STCI-R-0007](../results/quadratic_root_obstruction_model.md) and its
linked evidence. The normal-flatness theorem relevant to the intended
actual-CI application is
[STCI-R-0010](../results/saturated_first_relation_normal_flatness.md).
No accepted chart, saturation, or first-obstruction theorem is rerun.

The new evidence is
[the standard-library Python script](../computations/conditional_2_12_symbol_map_2026_10_20.py)
and [its full rational JSON output](../computations/conditional_2_12_symbol_map_2026_10_20.json).
Run `python3 research/computations/conditional_2_12_symbol_map_2026_10_20.py`.
The accepted first-incidence Jacobian is read from its saved JSON as an
input for the new tangent-space comparison; that input's SHA256 is
recorded in the new output.

## The exact map and its global source

On the first base chart let `z=t/s`. Use the accepted balanced normal
coordinates

```text
(x0,x1,x2,x3)=(1,z,z^3+v,z^4+u+(3/2)zv).
```

Both conormal frame vectors have transition `z^-7`. Since
`O_C0(6)=O_P1(24)`, the requested map has target

```text
H0(Sym^2 E(6))=H0(O_P1(10))^3,
```

with ordered basis `z^j u^2`, `z^j uv`, `z^j v^2`, each `j=0,...,10`.
For an actual homogeneous sextic `F`, its exact second symbol is

```text
sigma2(F)=[F(1,z,z^3+v,z^4+u+(3/2)zv)]_(normal degree 2).
```

This formula uses actual global `k`-coefficients throughout.

Set

```text
q=x0*x3-x1*x2,
A=x0^2*x2-x1^3,
B=x0*x2^2-x1^2*x3,
D=x2^3-x1*x3^2.
```

A basis of the global source is the following list of 23 sextics:

```text
q^2 times all ten quadratic monomials in x0,x1,x2,x3;
q*A*x0, q*A*x1, q*A*x2, q*A*x3;
q*B*x2, q*B*x3, q*D*x2, q*D*x3;
A^2, A*B, A*D, B*D, D^2.
```

The script checks this source without relying on a saturation claim.
There are 84 ambient sextic monomials. Their zeroth and first normal
coefficients form a rational matrix of rank 61, so the global kernel
has dimension 23. Vanishing on the dense affine part of `C0` suffices:
first the restriction is a section of `O_C0(6)`, and after that vanishes
the first symbol is a section of the vector bundle `E(6)`; either
section vanishes globally if it vanishes densely. Thus this kernel is
exactly `H0(I_C0^2(6))` for the sheaf square. The displayed 23 ordinary
ideal-product sextics are independently linearly independent and belong
to that kernel. They therefore span the entire sheaf-theoretic source,
including any possible homogeneous saturation issue in this degree.

The second-symbol matrix has rank 22. The sextic `q^3` has zero second
symbol, so the kernel is exactly `k*q^3`. An image basis is obtained by
omitting `q^2*x1*x2` from the displayed source basis. Indeed the only
kernel relation is

```text
q^2*x0*x3-q^2*x1*x2=q^3.
```

The JSON contains both the full `33 by 23` map and this `33 by 22` image
basis, with all entries exact rational numbers. For the displayed image
columns, the minor on target rows `P0,...,P10,Q0,...,Q9,R0` has determinant
exactly `48`; this is a compact rank-22 certificate.

## Eleven equations for the 22-dimensional image

Write a target element as

```text
P(z)u^2+Q(z)uv+R(z)v^2,
P=sum P_j z^j, Q=sum Q_j z^j, R=sum R_j z^j.
```

The image `V_(6,2)` is exactly the common kernel of the following eleven
independent linear forms:

| Row | Linear form |
| --- | --- |
| 1 | `P9-2Q10` |
| 2 | `Q0-2R1` |
| 3 | `P0-2Q1+4R2` |
| 4 | `3P1-2Q2-4R3` |
| 5 | `P2-2Q3+4R4` |
| 6 | `P3-2Q4+4R5` |
| 7 | `P4-4R6` |
| 8 | `P5-2Q6+4R7` |
| 9 | `P6-2Q7+4R8` |
| 10 | `P7+2Q8-12R9` |
| 11 | `P8-2Q9+4R10` |

The rational calculation verifies that these rows annihilate all 22
image columns and have rank eleven. Together with rank 22 of the map,
this proves equality with the image, rather than only necessity.

For `f=a(z)u^2+b(z)uv+c(z)v^2`, with base-quadratic `a,b,c`, and
`alpha=sum_(i=0)^8 alpha_i z^i`, put

```text
P_j=sum_i alpha_i a_(j-i),
Q_j=sum_i alpha_i b_(j-i),
R_j=sum_i alpha_i c_(j-i),
```

with coefficients outside their allowed ranges zero. Substitution in
the table gives eleven explicit bilinear equations on
`U x P(H0(O_P1(8)))`, where `U` is the basepoint-free open in the root
coefficient space `P8`. The multiplier is nonzero but may have zeros.
This is an exact scheme presentation of the new membership condition
`alpha*f in V_(6,2)`. It introduces no rational-function coefficients.

## The new restriction is not automatic on the first incidence

For the accepted first-compatible smooth torsion-two seed

```text
f0=(z^2+4)u^2+(z^2-8)v^2,
```

the eleven-by-nine multiplier matrix has rank eight. Its one-dimensional
kernel is generated by

```text
alpha0=z^8-8z^6+96z^4+256z^2+1024.
```

Thus the new symbol condition alone does not exclude the seed. Its
accepted second ambient obstruction is already nonzero, equal to
`1/8`, so this point is not a survivor of the full first-plus-second
obstruction test.

Nevertheless the new global condition is not automatic on the accepted
first compatibility scheme `K1`. At `(f0,h0,alpha0)`, append the eleven
new bilinear equations to `A_f h=d_f`. In the 30 affine variables
`f9,h12,alpha9`, the combined 27-row Jacobian has rank 26. After removing
the two independent projective scaling directions, its tangent dimension
is two. Because the projective multiplier is unique at the seed, this
is also the tangent dimension of the projected membership incidence.
The accepted `K1` is smooth of projective dimension four at `[f0]`.
The new global symbol condition therefore removes first-compatible
tangent directions. This is a tangent-space statement, not an assertion
that the new scheme has dimension two. It says nothing by itself about
the intersection with the second ambient obstruction and the torsion
locus.

## The first subsequent condition on an actual sextic

Let `c_1,...,c_23` be actual `k`-coefficients in the displayed sextic
basis, write `F_c` for their global sextic, and let `M` be the exact
second-symbol matrix. Over the membership incidence impose

```text
M*c=coeff(alpha*f).
```

Its solution fiber is an affine line in the `q^3` direction. On `K1`
the accepted ambient model gives the canonical first cubic correction
`G0`, with base degree at most one. The next necessary condition for
`F_c` to belong to the lifted first relation is

```text
F_(c,3)-alpha*G0=f*(ell(z)u+m(z)v),       deg ell,m <=7.       (C3)
```

Here `F_(c,3)` is the literal normal-degree-three part of the global
sextic in the accepted chart. Its base degree is at most eight, as
checked for every source basis vector; `alpha*G0` has base degree at
most nine. Since `f` is basepoint-free at infinity, at least one of its
homogeneous quadratic base coefficients has nonzero leading affine
coefficient. Multiplication of the leading nonzero binary normal forms
then proves the degree bound seven for `ell,m`. Thus (C3) is exactly
forty coefficient equations in the four cubic normal monomials and
base powers `0,...,9`. The `40 by 23` matrix of `F_(c,3)` is saved in the
JSON. This is a finite next obstruction with actual global sextic
coefficients; it is not an unrestricted homogeneous-equation search.
The test is invariant under adding multiples of `f` to the chosen
local cubic representative, because `ell,m` absorb that change.

For the accepted seed, the canonical correction is

```text
G0=(z/8)u^2v-(3/4)uv^2+(z/8)v^3.
```

With the multiplier `alpha0` above, the 33 symbol equations and forty
cubic equations give a rational system with 39 unknowns
`c23,ell8,m8`. Its coefficient matrix has rank 39, while its augmented
matrix has rank 40. The JSON stores an exact annihilating row and its
nonzero target pairing `-384`. For a short independently checkable
description, order the target first as `P0,...,P10,Q0,...,Q10,R0,...,R10`
and then as cubic coefficients `T_(i,j)` of `z^j*u^(3-i)*v^i`. The row is

```text
P4+64P8-192P10+Q5-16Q7
 +3T_(0,0)-12T_(0,2)+48T_(0,4)-192T_(0,6)+768T_(0,8)
 -2T_(1,1)+8T_(1,3)-32T_(1,5)+128T_(1,7)-512T_(1,9).
```

It annihilates every pair `(M*c,F_(c,3)-f*(ell*u+m*v))`, but its value
on `(coeff(alpha0*f0),coeff(alpha0*G0))` is `-384`. Hence even this
symbol-compatible seed cannot be realized by a global sextic matching
the unique first ambient lift. This is consistent with its already
known second-obstruction failure and does not exclude a new component
of the fully combined incidence.

## Unresolved scope

The complete intersection of the eleven global-symbol equations with
the accepted universal first incidence, all twenty-five second dual
pairings, and exact Picard torsion descent is not solved by this note.
Equation (C3) is the first exported subsequent condition on the global
sextic. No global degree-sixteen mate, degree-twelve standard basis,
full initial-pair coprimality, or global gcd/Bezout certificate is
constructed. A nonempty low-order incidence would establish none of
those facts.

The independent audit passes the specified exact reduction. Canonical
promotion would require a separate reviewed change to result records.


---

## 2026-10-20-conditional-2-12-geometric-continuation

# Conditional (2,12;6,16;2): quadric contact and a forced norm multiplier

Date: 2026-10-20. Author: `incidence_audit` worker.

Status: **new conditional proposal; sections 1--4 independently
reviewed PASS by the `surface_bound` worker; not promoted**.
This note concerns only an actual global pair with degrees `6,16`,
sole reduced support `C0`, FULL generic coprime ordinary initial CI
`(2,12)`, and ACTUAL saturated movement-two first relation. It does
not assert such a pair exists or that the structured incidence is
empty. No accepted computation is rerun, and no canonical record is
edited.

## 1. Inputs and notation

Use [R-0010](../results/saturated_first_relation_normal_flatness.md),
[R-0011](../results/moving_nonreduced_spectral_root_obstruction.md),
and the newly reviewed finite bridge in
[the singular-root note](2026-10-20-conditional-2-12-singular-gluing.md).
In particular, on the blowup `B=Bl_C0(P3)`, with exceptional divisor
`E`, the common order-two transforms of an actual pair have local
ideal `(p,t^10)` at each full root point. The root is reduced of
class `(2,2)`, integral or two distinct `(1,1)` components. The
characteristic is zero and the field is algebraically closed.

Let `Q=(q=0)`, where `q=x0*x3-x1*x2`, be the smooth quadric. Identify
its rulings so that `C0` has class `(1,3)` and the cubic map

    pi3:C0 -> P1_ruling,          z -> z^3

is the first ruling. In the accepted balanced coordinates the
quadric's first normal equation is

    q1=u+(1/2)zv.

For `f=a(z)u^2+b(z)uv+c(z)v^2`, write

    tau(z)=f(-z/2,1)=(z^2/4)a(z)-(z/2)b(z)+c(z).

This is the homogeneous degree-four restriction of the `(2,2)`
root equation to the quadric direction section of class `(1,1)`.
The sextic symbol is `alpha*f`, with `alpha` homogeneous of degree
eight on `C0`.

## 2. The quadric direction cannot be a root component

An actual supported pair cannot have `Q` as a component of `F6`.
Otherwise `G16|Q` is a nonzero effective Cartier divisor with sole
reduced support `C0`: `G` cannot contain `Q`, since the global pair
has no common hypersurface factor. Such a divisor would be `m*C0`,
whereas its class is `(16,16)` and `C0` has class `(1,3)`. No
integer `m` gives these two classes.

Consequently `tau` is not identically zero. Indeed if `tau=0`,
then the restriction `F6|Q` has order at least three on `C0`.
The remainder would have class

    (6,6)-3(1,3)=(3,-3),

which is not effective on the smooth quadric. Hence `F6|Q` would
vanish identically, forcing the already excluded quadric factor.

Thus an actual global pair satisfies the additional open condition

    q1 does not divide f,             tau != 0.

This removes a permitted reduced two-component spectral stratum.
Whether an earlier global lifting test already removes it is a
separate implication, not assumed here.

## 3. Residual divisors on Q and exact local contacts

The restrictions are

    div(F6|Q)=2C0+R,      R of class (4,0),
    div(G16|Q)=2C0+T,     T of class (14,10).

Both multiplicities along `C0` are exactly two, since their generic
symbols restrict to nonzero multiples of `tau`. The residual
divisor `R` is a sum of ruling fibers, with their actual positive
multiplicities. The divisors `R,T` have no common component and no
common point outside `C0`, by sole reduced support of the original
pair. In particular

    R.T=40.

The strict transform `Q'` is isomorphic to `Q`: blowing up a
Cartier divisor `C0` on the smooth quadric does not change that
surface. Under this isomorphism, `E|Q'=C0`, and restriction of the
common order-two transforms gives precisely the divisors `R,T`.

At a point of the full root meeting the quadric direction section,
restrict the actual transformed ideal `(p,t^10)` to `Q'`. Since
`tau` is nonzero, `(p,t)` on the smooth surface `Q'` has finite
colength, equal to the root/quadric-direction intersection
multiplicity `nu` there. The regular-sequence filtration gives

    length O_(Q',x)/(p,t^10)
      =10*length O_(Q',x)/(p,t)=10*nu.                    (1)

This does not require `p=0` to be smooth. Away from the full root,
the transformed ideal is the unit ideal near `E`, so there are no
other residual intersection points on `C0`.

Summing (1) gives exactly

    R.T=10*(Z . Q_direction)=10*4=40.                    (2)

Thus the elementary quadric degree budget saturates; it gives no
numerical contradiction. It also identifies all contacts and their
scheme lengths rather than treating a vertical exceptional curve
as a residual component downstairs.

## 4. A forced norm identity, including degenerate orbit strata

The local formula implies more than the total equality (2). Write
`R=sum m_y L_y` as a divisor of ruling fibers. Since `T.L_y=10`,
and `T` has no component `L_y`, restriction to that fiber gives

    10*m_y
       =sum_(x in C0 intersect L_y) i_x(R,T)
       =10*sum_(x in pi3^-1(y)) ord_x(tau).

Hence the actual divisors satisfy

    R=pi3_* div(tau).                                    (3)

On the affine quadric chart the equation of `C0` is `v=b-z^3`,
and `F6|Q=v^2 R4(b)`. Comparing its second symbol with `alpha*f`
gives `alpha(z)*tau(z)=R4(z^3)`. Together with (3), this yields

    div(alpha)=pi3^* pi3_* div(tau)-div(tau).              (4)

Thus the actual degree-eight multiplier is uniquely determined
projectively by `tau`, including branch points and repeated roots.
If `zeta` is a primitive cube root of unity, an explicit formula is

    alpha(z) proportional to tau(zeta*z)*tau(zeta^2*z).    (5)

Formula (5) is a polynomial construction; there is no division by
`alpha` or by a function vanishing on `C0`. If
`tau=sum_(j=0)^4 t_j z^j`, the coefficient of `z^m` in the right
side is

    sum_(2j=m) t_j^2
      +sum_(j<k, j+k=m) e_(j,k)*t_j*t_k,

where `e_(j,k)=2` if `j=k mod 3`, and `e_(j,k)=-1` otherwise.
So the same map is defined over QQ without adjoining `zeta`.
Its homogeneous version is nowhere zero for every nonzero `tau`.

Explicitly the coefficient vector is

    A0=t0^2,
    A1=-t0*t1,
    A2=t1^2-t0*t2,
    A3=2*t0*t3-t1*t2,
    A4=t2^2-t0*t4-t1*t3,
    A5=2*t1*t4-t2*t3,
    A6=t3^2-t2*t4,
    A7=-t3*t4,
    A8=t4^2,

where

    t0=c0,
    t1=c1-b0/2,
    t2=c2-b1/2+a0/4,
    t3=-b2/2+a1/4,
    t4=a2/4.

One may impose `alpha_i*A_j-alpha_j*A_i=0` for all `i<j`, with
`alpha!=0` and `tau!=0`, or eliminate the projective multiplier by
substituting `[alpha_0:...:alpha_8]=[A0:...:A8]`. The latter makes
the eleven global-symbol equations homogeneous cubics in the nine
coefficients of `f`; it does not alter the actual root coordinates
or erase any norm ramification stratum.

All ramification multiplicities are retained in this argument.
At zero or infinity the map `pi3` has ramification index three:
if `tau` has order `m` there, its norm divisor has order `m`, its
pulled-back norm has order `3m`, and (4) gives order `2m` for
`alpha`. In an unramified orbit, with orders `m_0,m_1,m_2` for
`tau`, (4) gives orders `m_1+m_2,m_2+m_0,m_0+m_1` for `alpha`.
Thus repeated roots, collisions within an orbit and the two branch
fibers are covered without a genericity exception.

This supplies an exact additional necessary global-pair condition
on the low-order scheme: impose the projective equality in (5),
or substitute its quadratic coefficient vector for `alpha`, on
the open `tau!=0`. When the four roots of `tau` lie in distinct
unramified `pi3` fibers, the sextic symbol restriction on Q already
forces this multiplier. On collision and branch strata that
restriction can leave other choices; (3)-(5) retain the one forced
by the ACTUAL supported pair and its gap-ten contact ideal. No
claim that this condition is new on every component of the earlier
incidence is made.

As a consistency check, at the saved smooth seed

    tau=z^4/4+2z^2-8,

the coefficient vector in (5), multiplied by 16, is

    z^8-8z^6+96z^4+256z^2+1024,

the previously computed projective multiplier. This algebraic
identity does not make that already obstructed seed a survivor.

## 5. Surface singularity route: promising but incomplete

The strict sextic divisor has class `D=6H-2E`. A smooth member has
`c2=28`, `K^2=-4`, and `chi(O)=2`. Near a smooth root point where
`alpha|Z` has a simple zero, the actual equation has form

    A*p+t^10 B,         A|Z=alpha|Z.

At a simple zero on a smooth root this is an `A9` surface
singularity. Here `B` is automatically a unit: the second original
coefficient `beta` is nonzero at the zero of `alpha`, and the
invertible actual generator matrix forces its off-diagonal entry
`B` to be nonzero. There are sixteen zeros counted on the
degree-two cover `Z -> C0`. This suggests an exceptionally strong
vanishing-cycle obstruction on the normal isolated-singularity
locus. At a zero of multiplicity `m`, the special model
`(t+z^m)p+t^10` gives type `A_(10m-1)`.

These observations are **not a completed exclusion**. One must
handle nonnormal strict surfaces or singular curves, singular root
points and repeated zeros, and justify the precise
global vanishing-cycle bound. Irreducibility of a carrier is not
normality of its strict transform. The actual supported-pair
condition alone does not forbid singular curves outside `E` or
singular exceptional fibers. No Milnor-number argument in this
note discards those strata or claims that the conditional problem
is solved.

The proposed advance of this note is the exact contact identity and
forced multiplier (3)-(5), with independent review PASS. It can
reduce the structured incidence without starting an unstructured
search over global equations; whether the resulting incidence is
empty remains unresolved here.

## 6. Independent review of the norm argument

The separate `surface_bound` worker reconstructed sections 1--4
and reported **PASS**, including collision and branch multiplicities.
The review checked equality of the restricted actual ideal on
`Q'`, regularity from `tau!=0`, exclusion of a component of `T`
on each ruling fiber, the direct affine comparison
`F6|Q=v^2 R4(b)`, and the homogeneous/root-of-unity and QQ formulas.
This is recorded review of the new conditional lemma, not canonical
promotion or an emptiness certificate. The review also supplied
the automatic-unit observation for `B` incorporated in section 5.
