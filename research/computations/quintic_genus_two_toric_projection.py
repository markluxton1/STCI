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
