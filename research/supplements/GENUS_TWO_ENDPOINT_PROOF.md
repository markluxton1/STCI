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
