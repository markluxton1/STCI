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
