# Triple-contact trisecants: the complete quartic family

This proof excludes every endpoint-trisecant mate in the genus-two
\(\lambda=1\) lane of the fixed quartic in characteristic zero.
Its upstream assumptions are the actual normal ambient conic model,
the entire conductor, the two-stratum correction theorem, and the marked
special-prime argument, all located by the
[complete carrier proof](../synthesis/quartic_carrier_proof.md).
The proof includes repeated divisor components, second horizontal primes,
all projective parameter charts, and arbitrary ADE blocks away from contact.

The equation-space exhaustion and the local attachment arguments had
separate independent reviews; the replacement preserves their full
mathematical formulas and their exact hypotheses.

Work over an algebraically closed field of characteristic zero with the
literal curve `C0=[s^4:s^3 t:s t^3:t^4]`. Use the accepted actual normal ADE
strict transform `T` in the blowup of its genus-two conductor line, and the
accepted lambda-one mate reduction:

    f.c#=1,       c#^2=1,       K_M.Z=1,
    c# ~ L-Z,    Z effective rational sigma-exceptional,
    Z.E=-c#.E for every sigma-exceptional prime E.

The special horizontal prime `B` exists, satisfies `B^2=-3`, `f.B=1`,
and `c#.B=0`. There are at most two horizontal primes. Each horizontal
prime has K-degree one and maps in the ambient exceptional surface to
the whole fiber over one point of Gamma. Distinct horizontal primes
give distinct Gamma-fibers. Vertical exceptional primes are (-2) curves
contracted in the crepant ADE resolution `rho:M -> T`.

The actual full quartic family and endpoint coordinates are from
[the carrier ideal proof](GENUS_TWO_TRISECANT_CARRIER_PROOF.md).
Here the conductor line is `Gamma=(x2,x3)`. On the blowup chart put

    a=x1/x0,       y=x2/x0,       b=x3/x2.

The exceptional surface is `y=0`; the lifted curve is exactly
`(a,b,y)=(r,r,r^3)`. The sole point of `Gamma cap C0` is `a=0`, with
scheme length three. This full parametrization, including the third
normal order, is retained throughout.

## 1. The supporting horizontal fiber is forced to lie over a=0

Every positive coefficient of Z lies over the image of c in S. Indeed
pulling back a mate whose zero divisor on S has support c produces
effective exceptional correction only over c. Thus any horizontal
prime with positive Z coefficient maps to the sole Gamma-contact a=0.
Since `K_M.Z=1`, at least one such horizontal exists. As distinct
horizontal primes have distinct Gamma-images, exactly one horizontal
prime, denoted H0 for now, has positive coefficient, and that coefficient
equals one. Every other horizontal prime has coefficient zero.

This argument does not assume that the special prime B has positive
coefficient. A possible special B at a point p different from zero is
retained below.

## 2. Exact full quartic equation after the necessary horizontal factor

Write the degree-four carrier as `F=q Q+D L0`, where
`Q in (x2,x3)_2` and L0 is any linear form. Its strict transform has
exceptional restriction

    P(a,b)=(b-a)[a0+a1*a+(b0+b1*a)*b]
              -a*b^2*(c0+c1*a).

The supporting horizontal fiber H0 requires `P(0,b)=0` identically.
Therefore `a0=b0=0`, and the entire strict-transform equation is

    T: a[(b-a)(a1+b1*b)-b^2(c0+c1*a)]
       +y[(b-a)(A+B1*b+C*b^2)+c0+c1*a
                      -a*b^2(c2+c3*b)]
       +y^2(c2+c3*b)=0.                         (1)

The coefficient named B1 here is a scalar, not the horizontal prime B.
The actual exceptional divisor `D_T=T intersect E` is the full divisor
of P on `P1_Gamma x P1_f`, of class `(2,2)`.

An additional horizontal fiber over a finite `a=p !=0` forces all coefficients
of P(p,b)/p to vanish. Reading the constant, linear, and quadratic
terms in b gives

    a1=0,       b1=0,       c0+c1*p=0.            (2)

In that finite case c1 is nonzero (otherwise P vanishes identically), and

    D_T=H0+Hp+2F0.

The notation F0 denotes the fixed f-fiber b=0. Repeated components are
retained; this is a scheme statement, not only a support statement.

There is also the other Gamma-chart: a horizontal fiber at `p=infinity`
forces `a1=b1=c1=0`. Nonzero P then requires c0 nonzero and gives
`D_T=H0+H_infinity+2F0`. Thus every possible second horizontal, including
infinity, forces c0 nonzero and has the same displayed divisor form.

## 3. All c0 !=0 and coefficient-zero-special-B cases are excluded

At the actual contact `(a,b,y)=(0,0,0)`, equation (1) has
`partial T/partial y=c0`. If c0 is nonzero, T is smooth there, and c#
meets the strict transform of H0 with intersection one, because
`a|c=r` has order one.

If H0 is the only horizontal prime, it is the special prime B. This
contradicts `c#.B=0`. This also covers cases in which H0 occurs twice
in D_T; no reduced-horizontal assumption is being made.

If H0 is not B, the special B must give a second horizontal fiber Hp,
with p different from zero, possibly infinity. The finite and infinite
calculations in section 2 give exactly `D_T=H0+Hp+2F0`.
On H0 the remaining divisor meets only at b=0. Away from that point
the exceptional section of T is reduced smooth H0, so T is smooth.
At b=0 T is smooth by c0 nonzero. Hence H0 has no vertical ADE primes
attached anywhere, including the other f-chart.

The coefficient of Z along Hp is zero by section 1, and positivity
forces all exceptional coefficients attached to Hp to be zero too.
The correction equation for H0 is therefore simply

    -3*coeff_H0(Z)=-c#.H0=-1.

It gives `coeff_H0(Z)=1/3`, contradicting the coefficient one forced
by K_M.Z=1. This excludes the possibility that B has coefficient zero
and another horizontal supplies the mate correction.

Consequently every surviving endpoint configuration satisfies

    c0=0,       H0=B,       coeff_B(Z)=1,
    c#.B=0,    B is the sole horizontal prime.

The last assertion follows from (2): a distinct horizontal would force
c0 nonzero. If the residual contains H0 again, it is a multiplicity
statement about the same sole prime, not a second horizontal prime.

## 4. The a1 !=0 branch has two endpoint A-chains and is excluded

With c0=0 put

    R=(b-a)(a1+b1*b)-c1*a*b^2,       D_T=B_T+R.

Its restriction to B_T is the homogeneous degree-two polynomial
`b(a1+b1*b)`. If a1 is nonzero, this has two distinct zeros on P1_f,
including the zero at b=0; if b1=0, the other zero is at infinity.
At both points the derivative of R along B_T is nonzero. Thus the
exceptional section consists of two transverse branches there, even
if R itself is reducible elsewhere.

Every singularity of T on B_T lies at these two points. Each is an
A_n singularity with B attached to an endpoint of its resolution
chain: formal Morse splitting of `uv+y h` preserves y as parameter.
Let the contacted chain have length n and contact node k; let the
other chain have length m, allowing m=0. The smooth embedded descent
meets exactly one exceptional prime transversely. Solving the
intersection equations gives

    coeff_B(Z)=((n+1-k)/(n+1)) /
                  (3-n/(n+1)-m/(m+1)) <1.

The numerator is strictly below one and the denominator strictly above
one. This contradicts `coeff_B(Z)=1`. No finite chain cutoff and no
irreducibility assumption on R are used.

## 5. The a1=0, b1 !=0 branch is an exact local triple case

The equation becomes

    a*b[b1*(b-a)-c1*a*b]
       +y[(b-a)(A+B1*b+C*b^2)+c1*a-a*b^2(c2+c3*b)]
       +y^2(c2+c3*b)=0.                         (3)

The only intersection of B_T with the residual exceptional divisor is
b=0, of multiplicity two. Thus every singularity of T on B_T is at
this one point. The full local proof is in
[the exact local correction proof](GENUS_TWO_ENDPOINT_LOCAL_CORRECTIONS.md#1-triple-residual-contact).
It preserves the complete polynomial (3) and proves:

* A nonzero: B attaches to an endpoint of an A_n chain, giving its
  correction coefficient below 1/2.
* A=0 and c1 nonzero: exact quadratic factorization over k[[b]] puts
  the surface in `XY=b^(n+1)*unit`. B has factor orders `(n-1,2)`;
  c has orders `(1,n)` in the opposite orientation. The correction
  coefficient is exactly `2/(n+5)`, below one, for n>=3.
* A=c1=0 and c2 nonzero: the ordinary triple cubic after completing
  the square gives precisely D4; B and c meet distinct outer arms.
  The correction coefficient is 1/4.
* A=c1=c2=0: multiplicity is at least three, incompatible with ADE.

The abstract D7 numerical graph shield cannot be imported to this
equation without verifying actual realization. The ordinary triple
cubic here has three distinct factors b1*a*b*(b-a), which gives D4.

## 6. The doubled-horizontal subcase is also excluded

If a1=b1=0, nonzero P requires c1 nonzero, and

    D_T=2B_T+2F0.

Its full actual equation is

    -c1*a^2*b^2
       +y[(b-a)(A+B1*b+C*b^2)+c1*a-a*b^2(c2+c3*b)]
       +y^2(c2+c3*b)=0.                         (4)

The normal coefficient along B_T is the global degree-three section

    h_B(b)=b*(A+B1*b+C*b^2).

Thus additional singular points of T on B_T can occur away from the
contact at the other zeros of h_B, including infinity. The earlier
two-node endpoint-chain shortcut does not apply here. The complete
proof is in
[the doubled-horizontal proof](GENUS_TWO_ENDPOINT_LOCAL_CORRECTIONS.md#2-the-doubled-horizontal-divisor).
Here is its structural calculation.

For an ADE block let Q be its positive Cartan matrix and let v encode
the intersections of B with its exceptional primes. At the contact
block let e_j encode the unique transverse c# contact. Since the B
coefficient is one, the B intersection equation requires

    sum_blocks v^t Q^(-1) v + v^t Q^(-1) e_j =3.      (5)

Away from the contact, write `a=u*A0`, `y=u^2*Y0` on M, with B given
by u=0 and its f-parameter unchanged. Crepancy of the hypersurface
canonical generator `da wedge db/F_y` forces
`A0|B=unit*h_B`. Equation (4) then forces `Y0|B=unit*h_B` as well.
If an away-contact root has multiplicity k, comparison with the
total transform of div(y) gives the exact identity

    2*v^t Q^(-1) v=k.                              (6)

This retains arbitrary ADE types, multiple graph attachments, and
the other f-chart; it does not replace such blocks by A1 points.

If A is nonzero, both B and c have tangent outside the rank-two
quadratic kernel, and hence meet endpoints of the contact A_n chain.
Their combined contribution to (5) is strictly below two. The
remaining degree-two zero divisor of h_B contributes one by (6).
This contradicts (5). As an additional global check, A=c1 would make
T singular along all of the fixed conductor component F0, since
`F_y|F0=a*(c1-A)` and all other partial derivatives vanish there.
It is excluded by normality, independently of the numerical bound.
In fact A nonzero and A different from c1 forces precisely A3:
the quartic term restricted to the quadratic kernel is nonzero.
B and c meet the same endpoint, so the contact contribution is 3/2
and the total bound is 5/2, as detailed in the independent audit.

If A=0, normality leaves `k=ord_0(h_B)` equal to two or three.
The exact quadratic factorization in the independent audit gives
an `A_(2k+1)` contact, with B at node k and c at an endpoint.
The contact contribution to (5) is at most `(k+2)/2`; the other
zeros of h_B have total multiplicity `3-k` and contribute
`(3-k)/2` by (6). Thus the entire left side of (5) is at most
`5/2`, again less than three. This excludes all of (4).

If a1=b1=c1=0, P vanishes identically. The actual quartic then has
generic normal order at least three along Gamma, contrary to the
accepted genus-two generic multiplicity two. It is not another
surviving genus-two carrier stratum.


### Archived exact certificate: `research/computations/verify_session_genus_two_line_positions_2026_10_10.m2`

The following original computational certificate is preserved verbatim, with its original hypotheses, limitations, and external dependencies. No additional mathematical conclusion is asserted by its archival transfer.

<details><summary>Original source</summary>

```macaulay2
-- Exact identities for the actual conductor-line positions on C0.
-- Characteristic zero; no sampled parameters and no mate search.
R=QQ[a,b,k,s,t,l,m];
checks=0;
proofCheck=(label,condition)->(
    if not condition then error("FAIL: "|label);
    checks=checks+1;
);
P={1,a,a^3,a^4};
Q={1,b,b^3,b^4};
V=apply(0..3,i->l*P#i+m*Q#i);
proofCheck("complete finite-secant q identity",V#0*V#3-V#1*V#2==l*m*(a-b)^2*(a^2+a*b+b^2));
dP={0,1,3*a^2,4*a^3};
V=apply(0..3,i->l*P#i+m*dP#i);
proofCheck("complete finite-tangent q identity",V#0*V#3-V#1*V#2==-3*a^2*m^2);
Pinfinity={0,0,0,1};
V=apply(0..3,i->l*P#i+m*Pinfinity#i);
proofCheck("secant through infinity",V#0*V#3-V#1*V#2==l*m);
XX={s^4,s^3*t,s*t^3,t^4};
g=t^3-k*s^3;
proofCheck("finite trisecant first generator",XX#2-k*XX#0==s*g);
proofCheck("finite trisecant second generator",XX#3-k*XX#1==t*g);
proofCheck("endpoint infinity first generator",XX#0==s*s^3);
proofCheck("endpoint infinity second generator",XX#1==t*s^3);
S2=a^2+a*b+b^2;
S3=(a+b)*(a^2+b^2);
f=(t-a*s)*(t-b*s);
T0=XX#2-S2*XX#1+a*b*(a+b)*XX#0;
T1=XX#3-S3*XX#1+a*b*S2*XX#0;
u=s*(t+(a+b)*s);
v=t^2+(a+b)*s*t+S2*s^2;
proofCheck("finite secant homogeneous first residual",T0==f*u);
proofCheck("finite secant homogeneous second residual",T1==f*v);
proofCheck("finite residual infinity has no common zero",sub(v,{s=>0})==t^2);
proofCheck("finite residual other root boundary",sub(v,{t=>-(a+b)*s})==S2*s^2);
proofCheck("coincident tangent boundary",sub(S2,{b=>a})==3*a^2);
f=s*(t-a*s);
proofCheck("infinity secant first residual",XX#1-a*XX#0==f*s^2);
proofCheck("infinity secant second residual",XX#2-a^3*XX#0==f*(t^2+a*s*t+a^2*s^2));
proofCheck("infinity residual has no common zero",sub(t^2+a*s*t+a^2*s^2,{s=>0})==t^2);
proofCheck("cube collision identity",a^3-b^3==(a-b)*S2);
proofCheck("endpoint triple factor",sub(g,{k=>0})==t^3);
print("PASS genus-two literal line-position identities: "|toString checks|" checks");
```
</details>


### Archived exact certificate: `research/computations/quintic_genus_two_toric_projection.py`

The following original computational certificate is preserved verbatim, with its original hypotheses, limitations, and external dependencies. No additional mathematical conclusion is asserted by its archival transfer.

<details><summary>Original source</summary>

```python
"""Exact inverse-support certificate for the genus-two toric quintic source.

Requires SymPy; independently executed with version 1.14.0.
The computation is read-only and prints its exact identities as JSON.
"""
import json
import sys
import sympy as s

# Toric ideal from the exponent map (A,B,C,D,E)=(s,sx,sxy,sxy^2,sx^2y^5).
A,B,C,D,E,S,X,Y = s.symbols('A B C D E S X Y')
Qtor = B*D - C**2
Rtor = A*E*C - D**3
Ttor = A*B*E - C*D**2
elim_gb = s.groebner(
    [A-S, B-S*X, C-S*X*Y, D-S*X*Y**2, E-S*X**2*Y**5],
    S, X, Y, A, B, C, D, E, order='lex'
)
elim = [p.as_expr() for p in elim_gb.polys
        if not any(p.as_expr().has(v) for v in (S, X, Y))]
source_gb = s.groebner([Qtor, Rtor, Ttor], A, B, C, D, E, order='grlex')
assert len(elim) == 3
assert all(source_gb.reduce(p)[1] == 0 for p in elim)
image_gb = s.groebner(elim, A, B, C, D, E, order='grlex')
assert all(image_gb.reduce(p)[1] == 0 for p in (Qtor, Rtor, Ttor))

# Marked curve, h=u+v; coefficient matrix in the complete quartic basis.
u,v = s.symbols('u v')
hom = (u*v**3, u**3*(u+v), u**2*(u+v)*v,
       u*(u+v)*v**2, (u+v)**2*v**2)
quartic_basis = (u**4, u**3*v, u**2*v**2, u*v**3, v**4)
coeff_matrix = s.Matrix([
    [s.Poly(f, u, v).coeff_monomial(m) for m in quartic_basis]
    for f in hom
])
assert coeff_matrix.det() != 0
Acurve,Bcurve,Ccurve,Dcurve,Ecurve = hom
X0curve = s.expand(Bcurve-Ccurve+Dcurve-Acurve)
X1curve = s.expand(Ccurve-Dcurve+Acurve)
X2curve = Acurve
X3curve = s.expand(Ecurve-Dcurve-Acurve)
assert (X0curve, X1curve, X2curve, X3curve) == (u**4, u**3*v, u*v**3, v**4)
assert all(s.expand(q.subs({A:Acurve, B:Bcurve, C:Ccurve,
                             D:Dcurve, E:Ecurve})) == 0
           for q in (Qtor, Rtor, Ttor))

# Projection center and finiteness/birationality checks.
center_value_Q = Qtor.subs({A:0, B:0, C:1, D:1, E:1})
assert center_value_Q == -1
projection_forms = (
    -A+B-C+D, A+C-D, A, -A-D+E
)
assert s.Matrix([[s.Poly(f, A,B,C,D,E).coeff_monomial(m)
                   for m in (A,B,C,D,E)] for f in projection_forms]).rank() == 4

# Inverse fiber over C0 on v=1, t=u/v, with free fiber coordinate z=D.
t,z = s.symbols('t z')
x0,x1,x2,x3 = t**4,t**3,t,1
Af = x2
Bf = x0+x1
Df = z
Cf = x1+z-x2
Ef = x3+z+x2
Qf = s.factor(Bf*Df-Cf**2)
Rf = s.factor(Af*Ef*Cf-Df**3)
Tf = s.factor(Af*Bf*Ef-Cf*Df**2)
z0 = t**2+t
z1 = t**4-t**3-t**2+t
f5 = t**5-2*t**4+t**3+t**2-t+1
assert s.expand(Qf + (z-z0)*(z-z1)) == 0
assert s.expand(Rf + (z-z0)*(t**3+t**2*z-t+z**2)) == 0
assert s.expand(Tf + (z-z0)*(t**4+t**3*z+t**3+t**2*z+z**2)) == 0
assert s.factor((t**3+t**2*z1-t+z1**2)/f5) == t*(t-1)*(t+1)
assert s.factor((t**4+t**3*z1+t**3+t**2*z1+z1**2)/f5) == t**2*(t+1)
assert s.gcd(f5, s.diff(f5,t)) == 1
assert s.gcd(f5, t*(t+1)*(t-2)) == 1
assert s.factor(z1-z0) == t**2*(t-2)*(t+1)

# Exact affine ideal Groebner basis, not just generic-fiber gcd.
fiber_gb = s.groebner([Qf,Rf,Tf], z,t, order='lex')
expected_gb = s.groebner([-(z-z0)*(z-z1),
                          -t*(t+1)*(z-z0)*f5], z,t, order='lex')
assert [s.factor(p.as_expr()) for p in fiber_gb.polys] == \
       [s.factor(p.as_expr()) for p in expected_gb.polys]

# v=0 endpoint: target [1:0:0:0], free coordinate z. The common ideal is (z).
Qinf = s.expand((1+0)*z - (0+z-0)**2)
Rinf = s.expand(0*(0+z+0)*(0+z-0)-z**3)
Tinf = s.expand(0*(1+0)*(0+z+0)-(0+z-0)*z**2)
assert s.gcd(s.gcd(Qinf,Rinf),Tinf) == z

# Other endpoint fibers on v=1.
endpoint_fibers = {}
for tv in (0,-1):
    endpoint_fibers[str(tv)] = [str(s.factor(p.subs(t,tv))) for p in (Qf,Rf,Tf)]
assert s.gcd(s.gcd(Qf.subs(t,0), Rf.subs(t,0)), Tf.subs(t,0)) == z**2
assert s.gcd(s.gcd(Qf.subs(t,-1), Rf.subs(t,-1)), Tf.subs(t,-1)) == z**2

record = {
    "execution": {"command": f"python3 {__file__}",
                  "python": sys.version.split()[0], "sympy": s.__version__},
    "toric_elimination_generators": [str(s.factor(p)) for p in elim],
    "Q_R_T_generate_full_toric_kernel": True,
    "marked_curve_quartic_coefficient_matrix": str(coeff_matrix),
    "quartic_determinant": str(coeff_matrix.det()),
    "projected_marked_curve": [str(x) for x in (X0curve,X1curve,X2curve,X3curve)],
    "projection_center_Q_value": str(center_value_Q),
    "projection_forms_rank": 4,
    "affine_v1_fiber_equations": [str(Qf),str(Rf),str(Tf)],
    "affine_fiber_groebner_basis": [str(s.factor(p.as_expr())) for p in fiber_gb.polys],
    "marked_graph_z0": str(z0),
    "residual_graph_z1": str(z1),
    "residual_quintic": str(f5),
    "residual_quintic_squarefree": True,
    "residual_quintic_coprime_to_t_tplus1_tminus2": True,
    "extra_inverse_points": "five distinct reduced points, one over each root of f5; all off the marked graph",
    "v1_endpoints_t0_and_tminus1_fiber_equations": endpoint_fibers,
    "v0_point_target_1000_common_fiber_gcd": str(s.gcd(s.gcd(Qinf,Rinf),Tinf)),
    "scope": "Exact support over C0 is marked graph plus five extra points; t=0,-1 fibers have length 2 supported on the marked point; v=0 fiber is one reduced marked point.",
}
print(json.dumps(record, indent=2))
```
</details>


## Consolidated historical supplement: `research/supplements/OCT10_GENUS_TWO_ENDPOINT_AND_BLOWUP_AUDITS.md`

Original mathematical content and its qualifications are retained verbatim. Relative links refer to the source's original supplement location.

# Historical mathematical investigations

Full original mathematical text follows. Preserve source-level evidence status, counterexamples, corrections and unresolved boundaries. This compilation supplies no new independent audit.

---

## Source: 2026-10-10-session-genus-two-bisection-local-fibers-independent-audit.md

# Genus-two bisection local fibers: independent audit and remaining structural route

Date: 2026-10-10 local time; written at 2026-10-11T01:17 UTC.
Auditor: `bisection_local_fibers`. Status of Sections 1--4:
**PROVED HERE / independent audit passed**, conditional on the explicitly
accepted second-pencil and smooth-embedded-lift reductions. Section 5 is a
separate structural proposal requiring its own audit. The review covers the
stated bisection case.

Audited source:
[three-blowup fiber exclusion](GENUS_TWO_BISECTION_THREE_CENTER_PROOF.md),
SHA256 `f7177554d64e14a30d169daaedee7ff2ebcc51ed8b3d8435ed590369d9f24103`.
The present auditor independently checked every coefficient, center
restriction, and final contact contradiction. This is a mathematical
audit; no CAS execution or new symbolic-check count is claimed.

## 1. Precise input and verdict

Use the characteristic-zero notation of the
[second-pencil audit](#source-2026-10-10-session-genus-two-bisection-second-pencil-independent-auditmd).
There is a smooth weak degree-four del Pezzo surface V, with connected
rational pencils f and c satisfying `-K_V=f+c` and `f.c=2`. The smooth
minimal resolution M is obtained from V by four point blowups disjoint
from the actual smooth curve c, including every infinitely near center.
For a hypothetical lambda-zero mate,

    Z_t=(k_t/2)F_t-R_t,

is an actual equality of rational divisors, with full scheme-theoretic
fiber multiplicities. The positive support of Z consists of
sigma-exceptional vertical (-2)-curves. A contacted exceptional graph
has only one transverse c-contact, and the actual pullback of a local
uniformizer supplies a positive integral anti-nef exceptional cycle
whose coefficient at that contact is one.

The three-blowup note is accepted at exactly this scope: **every fiber
with k_t=3 is impossible**. Combining it with the independently checked
[even-count exclusion](../chapters/QUARTIC_CARRIER_TECHNICAL_PROOFS.md#bisection-with-an-even-fiber-count)
leaves only `[1,1,1,1]`. This conclusion does not yet use conductor power
descent, the splitting of the conductor, or the fixed embedding of C0.

## 2. The fiber list includes all multiplicities

The source's relative contraction argument is sufficient. Contracting a
vertical (-1)-curve E preserves anticanonical nefness: for an uncontracted
curve C, the anticanonical degree of its image increases by `E.C`.
Reverse a contraction sequence to a ruled surface. Starting from a
smooth square-zero fiber, the first blowup produces two (-1)-components.
An intermediate (-2)-component cannot be touched while anticanonical
nefness is retained. Smooth blowups at a (-1)-end extend a reduced chain;
the intersection of two adjacent (-1)-components can instead be blown
up once, creating a multiplicity-two (-1)-component with two
multiplicity-one (-2)-leaves. Subsequent smooth blowups extend the
multiplicity-two tail.

Thus the irreducible square-zero, reduced-chain, and nonreduced D-tail
fiber types exhaust the possibilities on V, including preexisting ADE
exceptional components. This argument does not assume that a degenerate
conic is reduced, and does not impose a root-rank bound.

## 3. Independent check of the three-center histories

An original V-component of multiplicity m has no coefficient in the
relative canonical divisor R. Its strict transform therefore has Z
coefficient `3m/2>0` and must finish with square -2. Old (-2)-components
cannot be hit, old (-1)-components must be hit once, and a square-zero
component must be hit twice. At a new center, the fiber multiplicity is
the sum of the multiplicities of components through it; the relative
canonical coefficient is one plus their relative canonical coefficients.
These rules use the actual total transforms and remain valid at
intersection centers.

The irreducible case has just one possible complete history: a smooth
blowup of the old component, an intersection blowup of that component
with the new exceptional, and a smooth blowup of the next exceptional.
The positive graph is A3, with unchanged total c-contact two. The
reduced case can finish only when the two old (-1)-ends were adjacent
and were blown up together; two further smooth blowups produce D4.
Its two old ends both meet c once, in the same exceptional graph. Both
cases violate the actual smooth-lift condition.

In the nonreduced case the three centers are forced smooth successive
points starting on the unique multiplicity-two (-1)-component A. The
positive graph is D_n, with A internal on the long arm, or at its fork.
The shortest graph is D5 and its correction is

    3A+(3/2)(U+V)+2E1+E2.

This correction is effective, numerically anti-nef after adding c, and
has `c.Z_t=3`. The numerical data alone do not exclude it. If an actual
uniformizer cycle had coefficient one at A, the (-2) anti-nef inequality
would force both adjacent coefficients to be one. Propagation along the
old multiplicity-two tail reaches a trivalent vertex with coefficient
one, where `2>=1+1+1` is impossible. This verifies the required local
contradiction without using a fundamental-cycle table.

## 4. Failure shield: one blowup need not start with a reduced node

It would be false to infer locally that k=1 forces a reduced nodal fiber.
For example, on V take a multiplicity-two (-1)-component A with two
multiplicity-one (-2)-leaves U,V. Blow up a smooth point of A disjoint
from c. On M,

    F=2A+U+V+2E,   R=E,
    Z=(1/2)F-R=A+(U+V)/2.

The new E has square -1 and zero Z coefficient; the positive graph is
A3, contacted at its middle component A. The positive integral
anti-nef cycle with all three coefficients one is compatible with the
local uniformizer condition. This is a local consistency example, not
a globally realized quartic or mate.

Consequently any exclusion of nonreduced k=1 fibers must use a global
constraint, not the three-blowup proof or a local smoothness shortcut.

## 5. Proposed global route for the four-single-blowup partition

The following additional route is supplied to the root for a separate
audit; it is not needed for the accepted Sections 1--4.

The finite double cover `W->P1_f x P1_c` has branch equation of bidegree
(2,2), quadratic in the second coordinate. Its discriminant is a
nonzero degree-four section on the f-base. Nonzeroness follows from
the integral smooth general f-fiber. Each supported k=1 fiber must
already be degenerate on V: an irreducible square-zero component would
have positive Z coefficient after only one hit and would have square
-1 rather than -2. Four distinct supported fibers therefore require
four discriminant zeros. Degree four forces each zero to be simple.

A simple discriminant zero gives a nonzero quadratic with one double
root, and the total double-cover surface is regular at the corresponding
node. Every degeneration is thus a simple reduced nodal conic. In
particular the branch curve is smooth: a singular branch point would
give a discriminant zero of multiplicity at least two. A smooth branch
divisor of class (2,2) is connected and hence irreducible; it is a smooth
genus-one curve. The local node blowup is forced, and each of the four
nodes lies on the ramification curve of the double cover.

The ramification curve on V is the anticanonical divisor `-K_V=f+c`.
Its proper transform through the four node blowups is an effective
integral anticanonical divisor on M and remains a smooth genus-one
curve. The actual ambient conic model supplies an effective divisor
`D_M=-K_M`, pulled back from the entire conductor. The
[unique-anticanonical-section argument](../chapters/QUARTIC_CARRIER_TECHNICAL_PROOFS.md#15-genus-two-conductor-line-positions-on-the-fixed-quartic)
would identify D_M with this irreducible genus-one curve. To check that
argument directly, tensor the basepoint-free f-pencil sequence by -K.
An effective section of `-K-f` would write `L=2f+T` and impose a
nonzero quadric equation on the actual quartic image via three squares.
Thus `H0(-K-f)=0`. Two independent anticanonical sections would then
give four independent products with the two f-sections, a basis of
`H0(L)`, and a Segre quadric on the image. Hence `h0(-K)=1`.

If the entire upstairs conductor has already been proved reduced split
with two rational components, its pulled-back divisor cannot be the
single irreducible genus-one curve just obtained. This would exclude
`[1,1,1,1]` and complete an alternative structural bisection exclusion.
The discriminant-to-entire-conductor identification, and any possible
horizontal contraction, should be checked explicitly before relying on
this argument. A separate global Cartier-double-ribbon obstruction is
currently under independent audit and may supersede this longer route.

## 6. Independent check of the proposed ribbon alternative

The root also proposed a short obstruction using the actual Cartier
double `2c_S~2H`. A CM double curve with reduction a smooth P1 has a
square-zero nilradical: its square is generically zero, hence finite
support, and a CM curve has no nonzero finite-support subsheaf. The
nilradical is rank-one torsion-free on P1, so it is a line bundle.
From `chi(O_S(mH))=2m^2+m+1`, the Cartier exact sequence gives double
curve polynomial `8m-6`. Subtracting the reduced curve polynomial
`4m+1` gives nilradical `O_P1(-8)`.

For the literal curve C0, the normal bundle is `O(7) direct_sum O(7)`.
An independent hand calculation is as follows. The quadratic syzygies
of `[s^4,s^3t,st^3,t^4]` are

    (st,-s^2,0,0), (t^2,-st,0,0), (0,t^2,-s^2,0),
    (0,0,st,-s^2), (0,0,t^2,-st).

On s=1 their differential images in `Omega_P1(6)=O(4)` are
`-1,-t,-2t^2,-t^3,-t^4`, times dt. The differential map is therefore
an isomorphism on global sections in characteristic different from
two. Consequently `H0(N^*(6))=H0(N(-8))=0`, and determinant `O(14)`
forces the asserted splitting.

The morphism from the double to P3 induces a global map
`I_C0/I_C0^2 -> O(-8)`. This map is generically surjective outside
the conductor, where normalization is an isomorphism and the double
is the actual Cartier double of c. Its Hom group is nevertheless zero,
since `Hom(O(-7)^2,O(-8))=H0(O(-1))^2=0`. The construction needs no
global closed immersion of the double into P3. This corroborates the
root's proposed obstruction; its final acceptance is assigned to the
separate full auditor and is not asserted by this local-fiber record.


---

## Source: 2026-10-10-session-genus-two-bisection-second-pencil-independent-audit.md

# Independent audit: the genus-two bisection double cover and its fiber weights

Date: 2026-10-10. Auditor: `bisection_second_pencil_audit`, with a
separate adversarial check by `fiber_weight_parity_audit` of Sections
5--7. Status: **PROVED HERE, conditional on the accepted genus-two
mate reduction**. This is a structural reduction; it does not exclude
the entire bisection stratum or resolve the genus-two mate problem.
No frontier file was edited by this auditor.

## 1. Exact hypotheses and notation

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

## 2. The second complete connected rational pencil

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

## 3. The Stein cover has branch class (2,2)

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

## 4. W is an ADE del Pezzo surface, and M has four further blowups

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

## 5. Rational linear equivalence forces actual whole fibers

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

## 6. Exact weights count the four blowups

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

## 7. Missing-lattice parity leaves three partitions

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

## 8. Scope and a check against an invalid stronger bound

The separate fiber-weight auditor accepted Sections 5--7 and supplied
a local consistency check for an odd count. Start with a reduced nodal
fiber `A+B` on V, where both components are `(-1)` curves. Blowing up
their intersection once gives

    F=A'+B'+2E,   R=E,   Z=(A'+B')/2.

Both A' and B' are `(-2)` curves. This matches `k=1` and weight `1/2`;
it shows why rational coefficients and intersection centers must be
included. The example is a local fiber check, not a globally realized
quartic carrier or a mate.

No exclusion of `[3,1]`, `[2,1,1]`, or `[1,1,1,1]` follows from the
counting argument alone. Exceptional-fiber connectedness, the smooth
embedded lift, the actual quartic map, and conductor descent still
have to be imposed. The lambda-one section lane is unchanged.


---

## Source: 2026-10-10-session-genus-two-lambda-one-marked-prime-audit.md

# Bounded audit: exceptional prime classes in the lambda-one plane marking

Date: 2026-10-10. Auditor: degree-one-anticanonical counteraudit agent.
Status: **PROVED HERE / accepted bounded structural classification**.
No frontier file or computation script was edited. This note
does not exclude the lambda-one stratum or assert that any listed
configuration is realized by an actual quartic normalization or mate.

## 1. Hypotheses and total-transform convention

Work over an algebraically closed field of characteristic zero. Keep
the hypotheses of the accepted genus-two nullcurve audit: sigma:M->S
is a resolution of a normal surface; the nef divisor L is pulled back
from an ample divisor on S; and its complete map is birational onto
the actual integral quartic. In the lambda-one stratum the actual
smooth lifted curve c# maps isomorphically to a smooth embedded curve
c in S. Its complete system supplies a birational morphism

    q:M->P2,

consisting of nine successive point blowups, possibly infinitely near.
The actual c# is a smooth member of class h, mapping to a line that
avoids the blowup centers. Use the total exceptional classes e0,...,e8,
so

    h^2=1, e_i^2=-1, h.e_i=e_i.e_j=0 for i!=j,
    K=-3h+sum_{i=0}^8 e_i,
    L=4h-2e0-sum_{i=1}^8 e_i,
    f=K+L=h-e0,             c#=h.

Every sigma-exceptional prime is assumed already proved to be either
a vertical smooth rational (-2)-curve, with f.E=0, or a horizontal
smooth rational (-3)-section, with f.E=1. There are at most two
horizontal primes, and they are pairwise disjoint. Every such prime
has L.E=0. The classification below starts with these proved inputs.

For a blowup center p_a, let P(a) be the set of later centers lying on
the then-current strict transform of the exceptional curve born at
p_a. These are the centers directly proximate to p_a, not all indirect
descendants. The final prime strict transform is exactly

    F_a=e_a-sum_{j in P(a)} e_j.                 (1)

Each coefficient in this subtraction is one because the strict
exceptional curve remains smooth. A satellite center belongs to two
different sets P(a) and contributes once to each respective formula;
it does not contribute twice to one prime. This follows inductively
from the strict-transform formula for one blowup. For a primary
reference on these conventions and the corresponding proximity
inequalities, see [Calabri--Ciliberto, On Cremona contractibility,
section 2, p. 392, equation (2)](https://seminariomatematico.polito.it/rendiconti/71-34/0.pdf).

## 2. Nefness forces the double center to be proper and controls satellites

Write m0=2 and m_a=1 for a>=1. Formula (1) gives

    L.F_a=m_a-sum_{j in P(a)} m_j >= 0.         (2)

If p0 were infinitely near, it would be proximate to some earlier
center p_a with a!=0. Then L.F_a<=1-2<0, contrary to nefness.
Thus p0 is a proper point of P2. Independent proper-center branches
can be reordered to blow up p0 first. Consequently f=h-e0 is the
actual pulled-back pencil of lines through this proper point.

After this observation every member of P(a) is a simple center. If
r_a=|P(a)|, (2) becomes

    r0<=2,                  r_a<=1 for every a>=1.              (3)

There is at most one satellite center in the entire marking. Indeed,
suppose a center p_j lies at the intersection of two older strict
exceptionals F_a,F_b, with p_a earlier than p_b. Their intersection
could exist only if the creation point p_b lay on the strict transform
of F_a: subsequent blowups can remove an intersection of two old
strict transforms, but cannot create one. Thus both p_b and p_j are
directly proximate to p_a. Inequality (3) forces a=0. Such a satellite
is therefore the second direct child of p0, at the intersection of
the p0 exceptional and the exceptional of its first child p_i.
It exhausts p0's two-child budget; no further satellite is possible.

The branches over all other proper points consist of free chains.
Over p0 there are at most two free branches, or the single pattern

    first child i proximate to 0,
    satellite j proximate to both 0 and i,
    later free chain starting at j.

This is a necessary proximity restriction, without a realizability
assertion for the complete marked linear system.

## 3. Degree-zero exceptional primes

Since p0 is proper, (1) gives

    F_a^2=-1-r_a,
    f.F_0=1,                f.F_a=0 for a>=1,
    L.F_0=2-r0,             L.F_a=1-r_a for a>=1.

Accordingly the degree-zero sigma-exceptional primes have precisely
the following forms, with the proximity relations required by (1):

    R_ab=e_a-e_b,            a,b in {1,...,8}, P(a)={b};
    B_A=e0-e_i-e_j,          A={i,j}=P(0), r0=2.

The R_ab are vertical (-2)-curves. The unique possible B_A is a
horizontal (-3)-section. In particular there cannot be two distinct
degree-zero horizontal primes.

The graph on degree-zero vertical primes alone is a disjoint union
of A-chains: every simple center has at most one direct child, and
the satellite restriction prevents a child from having two simple
parents. For two consecutive chain roots their intersection is one,
and all other distinct roots on that chain have intersection zero.

If p0 has two free children i,j, B_A can attach to the initial root
of each of their two chains. If j is the satellite child of 0 and i,
then

    B_A.R_ij=0,
    B_A.R_jk=1 if the later child k of j exists.

Thus B_A attaches to the second vertex of the chain i->j->k->...,
rather than to R_ij. This can make that second vertical vertex
trivalent if the chain continues. If j has no child, R_ij and B_A
are disjoint components of the degree-zero sigma-exceptional locus.

## 4. Positive plane degree: complete arithmetic classification

If a prime E has d=h.E>0, its plane image is an integral plane curve
of degree d and E is its strict transform. Write

    E=d h-sum_{a=0}^8 b_a e_a,          b_a>=0 integral.         (4)

Here b_a is the actual multiplicity of the successive strict transform
at p_a. This nonnegativity holds for infinitely near and satellite
centers as well. It does not apply to degree-zero F_a: in the notation
of (4), that prime has b_a=-1 at its creation index.

For every positive-degree prime, the additional proximity constraints
are

    b_a >= sum_{j in P(a)} b_j,                              (5)

because E.F_a>=0 for the distinct primes E and F_a. These inequalities
remain necessary after the following arithmetic classification.

If E is vertical, f.E=0 and E^2=-2 give

    b0=d,
    sum_{a=1}^8 b_a=2d,
    sum_{a=1}^8 b_a^2=2.

The last equality forces two entries to be one and all others zero;
their sum then forces d=1. The only possible positive-degree vertical
prime class is therefore

    V_P=h-e0-e_i-e_j,       P={i,j} subset {1,...,8}.          (6)

It is the strict transform of an actual plane line through p0.

If E is horizontal, f.E=1 and E^2=-3 give

    b0=d-1,
    sum_{a=1}^8 b_a=2d+2,
    sum_{a=1}^8 b_a^2=2d+2.

Nonnegative integrality forces every b_a for a>=1 to be zero or one.
There are 2d+2 ones among eight entries, so 1<=d<=3. The exhaustive
arithmetic list is

    d=1: h-sum_{a in T} e_a,              |T|=4;
    d=2: 2h-e0-sum_{a in T} e_a,          |T|=6;
    d=3: 3h-2e0-sum_{a=1}^8 e_a.

No prime-effectivity or incidence claim is implicit in this list.
Adjunction imposes no extra equation here: K.E=f.E follows from
L.E=0 and f=K+L, and the displayed squares already give genus zero.

## 5. Embedded smoothness excludes the conic and cubic and limits components

The assumption that c#->c is an isomorphism to a smooth embedded
curve supplies more than a numerical divisor identity. Let p be a
singular point of S lying on c, and P the unique point of c# above p.
Choose a local function a in the maximal ideal of O_(S,p) whose
restriction to c is a uniformizer; such a function exists because
O_(S,p)->O_(c,p) is surjective. Its pullback has positive order along
every exceptional prime above p. The smooth local ring O_(M,P) is
factorial. Restriction to c# has order exactly one, hence

    1 >= sum of local intersection multiplicities of c#
         with exceptional branches through P.

It follows that exactly one exceptional prime passes through P,
that c# meets it transversely, and that no other point of that
exceptional fiber meets c#. Every connected exceptional graph is
contained in one fiber of sigma; thus it has at most one vertex E
with c#.E>0. In particular

    h.E=c#.E is either zero or one for every exceptional prime.

The horizontal conic and cubic in section 4 have h-degree two and
three and are excluded. All surviving positive-degree exceptional
primes are therefore plane lines: (6), with square -2, or

    H_T=h-sum_{a in T} e_a,              |T|=4, square -3.     (7)

Each connected sigma-exceptional graph has at most one such line
vertex. Consequently distinct positive-degree exceptional primes
are pairwise disjoint, and they cannot be connected even through
degree-zero exceptional vertices.

## 6. Explicit necessary intersection and graph restrictions

For a chain root R_ab=e_a-e_b, intersections with V_P,H_T,B_A are

    V_P.R_ab = 1_(a in P)-1_(b in P),
    H_T.R_ab = 1_(a in T)-1_(b in T),
    B_A.R_ab = 1_(a in A)-1_(b in A).

They must be nonnegative; an entry one gives a single transverse
intersection because both primes are smooth. This enforces the
prefix conditions along the corresponding proximity chains. The
complete root-root formula is

    R_ab.R_cd=-delta_ac+delta_ad+delta_bc-delta_bd.

For distinct positive-degree vertices, the preceding disjointness
condition gives

    V_P.V_Q=-|P intersection Q|=0,
    H_T.V_P=1-|T intersection P|=0,
    H_T.H_U=1-|T intersection U|=0.

Thus vertical line supports are pairwise disjoint, each horizontal
line support meets each vertical line support in exactly one index,
and two horizontal line supports meet in exactly one index. There
are at most four positive-degree vertical primes, because their
two-element supports are disjoint in an eight-element set. This is
an upper bound, not an existence statement.

For the possible degree-zero horizontal B_A,

    B_A.V_P=1-|A intersection P| >=0,
    B_A.H_T=-|A intersection T|=0.

The second equality is forced already by nonnegative prime
intersection, consistently with horizontal disjointness. More
strongly, (5) and the zero multiplicity of H_T at p0 show that H_T
passes through no center above p0. Its exceptional graph component
therefore contains no B_A. A component containing B_A may contain
at most one positive-degree vertical line. Two or more V_P with
A intersection P empty would each meet B_A and violate this rule.

There is at most one B_A and at most two horizontal vertices in
total. If B_A exists, at most one H_T can exist; otherwise at most
two H_T can exist. Distinct horizontal vertices have no direct edge.
Each final graph is assembled from the degree-zero chains and the
possible B_A described in section 3, with at most one plane-line
vertex per connected component. Every edge permitted by the marked
intersection formulas has multiplicity one. A horizontal section
also meets at most one component of any given f-fiber, at a smooth
point of that fiber, since its total fiber intersection is one.

## 7. Caveats, useful counterexamples to shortcuts, and freeze boundary

The formula subtracting all descendants is false. In a free chain
p_b proximate to p_a, p_c proximate only to p_b, the final strict
transform of the a-exceptional has class e_a-e_b, not e_a-e_b-e_c.
At the allowed satellite pattern j proximate to 0 and i, the classes
are e0-e_i-e_j and e_i-e_j, with intersection zero; coefficient two
at e_j in either individual prime would be incorrect. These are
local blowup illustrations of the formulas, not claimed realized
quartic configurations.

Applying nonnegative b_a to degree-zero primes would likewise be
incorrect. Applying h.E<=1 using only numerical equivalence c#=h,
without the smooth embedded curve and isomorphism hypotheses, would
also be unjustified. Those geometric hypotheses are essential to
section 5.

The class list, proper-double-center conclusion, proximity budget,
at-most-one-satellite restriction, and graph restrictions are accepted.
The arithmetic class list was independently checked by a second
bounded audit. Agreement is provenance; the proofs are the explicit
intersection and multiplicity arguments above. Actual incidence,
prime effectivity, full graph realization, normalization/conductor
descent, and existence or exclusion of a mate remain separate work.
No lambda-one exclusion is claimed. This note is frozen for the
requested pause closure after its content and hash are reported.


---
