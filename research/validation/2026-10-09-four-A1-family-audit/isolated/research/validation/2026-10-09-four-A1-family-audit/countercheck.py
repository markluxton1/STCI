#!/usr/bin/env python3
"""Independent universal polynomial checks for the four-A1 family.

No producing checker is imported, no numerical parameter sample is used.
The geometric implications of these identities are proved in the audit note.
"""
from pathlib import Path
from itertools import combinations
import hashlib
import json
import sympy as s

OUT = Path(__file__).resolve().parent
alpha,beta,gamma,delta,U,V = s.symbols('alpha beta gamma delta U V')
Y = s.symbols('Y0:5')
x0,x1,x2,x3,zeta = Y[0],Y[1],Y[3],Y[4],Y[2]
Delta = alpha*delta-beta*gamma
m = alpha*delta+beta*gamma
n = alpha*beta*gamma*delta
T = s.Matrix([
    [0,gamma**2,2*gamma*delta,delta**2,0],
    [-alpha*gamma,-m,-beta*delta,0,0],
    [0,-alpha*gamma,-m,-beta*delta,0],
    [0,0,-alpha*gamma,-m,-beta*delta],
    [0,alpha**2,2*alpha*beta,beta**2,0],
])
assert s.expand(T.det()-n*Delta**3) == 0
a,b,c,d,e = T*s.Matrix(Y)
Q1,Q2 = s.expand(a*e-c*c),s.expand(b*d-c*c)
assert s.expand(Q1-Delta**2*(x1*x2-zeta*zeta)) == 0
center = {Y[i]:s.Integer(i==2) for i in range(5)}
assert s.expand(Q1.subs(center)+Delta**2) == 0
assert s.expand(Q2.subs(center)+(m*m-n)) == 0

L = alpha**2*gamma**2*x0-alpha*gamma*m*x1-beta*delta*m*x2+beta**2*delta**2*x3
R = alpha*gamma*m*x0*x2+n*x0*x3-alpha**2*gamma**2*x1**2-n*x1*x2+beta*delta*m*x1*x3-beta**2*delta**2*x2**2
# Clearing only Delta avoids accidentally removing m=0 or m^2=n strata.
assert s.expand(Delta**2*(Q2-zeta*L-R)-(m*m-n)*Q1) == 0
F = s.expand(R**2-x1*x2*L**2)
assert s.Poly(F,x0,x1,x2,x3).total_degree() == 4
assert s.Poly(F,x0,x1,x2,x3).coeff_monomial(x0*x0*x3*x3) == n*n
assert s.expand(s.resultant(Q1,Q2,zeta)-Delta**4*F) == 0

standard_curve = {Y[i]:U**(4-i)*V**i for i in range(5)}
expected_curve = [
    U*V*(gamma*U+delta*V)**2,
    -U**2*(alpha*U+beta*V)*(gamma*U+delta*V),
    -U*V*(alpha*U+beta*V)*(gamma*U+delta*V),
    -V**2*(alpha*U+beta*V)*(gamma*U+delta*V),
    U*V*(alpha*U+beta*V)**2,
]
assert all(s.expand(value.subs(standard_curve)-target)==0 for value,target in zip((a,b,c,d,e),expected_curve))
assert s.expand(Q1.subs(standard_curve)) == 0
assert s.expand(Q2.subs(standard_curve)) == 0
assert s.expand(F.subs(standard_curve)) == 0
LC = s.expand(L.subs(standard_curve))
RC = s.expand(R.subs(standard_curve))
assert s.expand(RC+U**2*V**2*LC) == 0
assert s.Poly(LC,U,V).coeff_monomial(U**4) == alpha**2*gamma**2
assert s.Poly(LC,U,V).coeff_monomial(V**4) == beta**2*delta**2
minus_curve = dict(standard_curve)
minus_curve[zeta] = -U**2*V**2
assert s.expand(Q1.subs(minus_curve)) == 0
assert s.expand(Q2.subs(minus_curve)+2*U**2*V**2*LC) == 0
# This quadratic vanishes on the entire rational normal curve but not on
# the negative lift at any parameter with UV nonzero.
curve_quadric = Y[0]*Y[2]-Y[1]**2
assert s.expand(curve_quadric.subs(standard_curve)) == 0
assert s.expand(curve_quadric.subs(minus_curve)+2*U**6*V**2) == 0

aa,bb,cc,dd,ee = s.symbols('a b c d e')
standard_vars = (aa,bb,cc,dd,ee)
standard_q = (aa*ee-cc*cc,bb*dd-cc*cc)
Jac = s.Matrix([[s.diff(q,v) for v in standard_vars] for q in standard_q])
minors = [s.expand(Jac[:,list(pair)].det()) for pair in combinations(range(5),2)]
singular = s.groebner([*standard_q,*minors],*standard_vars)
assert singular.reduce(cc**3)[1] == 0
assert singular.reduce((aa*ee)**2)[1] == 0
assert singular.reduce((bb*dd)**2)[1] == 0
for pair in ((aa,bb),(aa,dd),(bb,ee),(dd,ee)):
    assert singular.reduce(pair[0]*pair[1])[1] == 0
for axis in (0,1,3,4):
    axis_substitution = {v:s.Integer(j==axis) for j,v in enumerate(standard_vars)}
    assert all(poly.subs(axis_substitution)==0 for poly in (*standard_q,*minors))
# These equations prove the radical of the Jacobian locus is exactly the
# four coordinate axes in the affine cone, hence four points in P4.
local_models = {
    'a=1': (standard_q[1], {aa:1,ee:cc**2}, bb*dd-cc**2),
    'b=1': (standard_q[0], {bb:1,dd:cc**2}, aa*ee-cc**2),
    'd=1': (standard_q[0], {dd:1,bb:cc**2}, aa*ee-cc**2),
    'e=1': (standard_q[1], {ee:1,aa:cc**2}, bb*dd-cc**2),
}
for polynomial,substitution,expected in local_models.values():
    assert s.expand(polynomial.subs(substitution)-expected) == 0
for axis,(u,v) in {1:(1,0),3:(0,1),0:(beta,-alpha),4:(delta,-gamma)}.items():
    point=[s.expand(value.subs({U:u,V:v})) for value in expected_curve]
    assert all(value==0 for i,value in enumerate(point) if i!=axis)
    expected_nonzero={1:-alpha*gamma,3:-beta*delta,0:-alpha*beta*Delta**2,4:-gamma*delta*Delta**2}[axis]
    assert s.expand(point[axis]-expected_nonzero) == 0

u0,u1,v0,v1,tcoord,ucoord,rcoord = s.symbols('u0 u1 v0 v1 tcoord ucoord rcoord')
cover = {aa:u0*u0*v0*v0,bb:u0*u0*v1*v1,cc:u0*u1*v0*v1,
         dd:u1*u1*v0*v0,ee:u1*u1*v1*v1}
odd = alpha*u0*u0*v0*v1+beta*u0*u1*v0*v0+gamma*u0*u1*v1*v1+delta*u1*u1*v0*v1
curve_section = alpha**2*aa*bb+beta**2*aa*dd+gamma**2*bb*ee+delta**2*dd*ee+2*cc*(alpha*beta*aa+alpha*gamma*bb+beta*delta*dd+gamma*delta*ee)+2*m*cc**2
assert s.expand(curve_section.subs(cover)-odd**2) == 0
curve_section_on_Y = curve_section.subs(dict(zip(standard_vars,(a,b,c,d,e))))
assert s.expand(curve_section_on_Y.subs(standard_curve)) == 0
odd_affine = odd.subs({u0:1,v0:1,u1:tcoord,v1:ucoord})
assert s.expand(odd_affine.subs(tcoord,rcoord*ucoord)-ucoord*(alpha+beta*rcoord+rcoord*(gamma+delta*rcoord)*ucoord**2)) == 0

result = {
    'status':'PASS universal polynomial identities; geometric proof in independent audit note',
    'scope':'Characteristic zero, alpha*beta*gamma*delta*(alpha*delta-beta*gamma) nonzero',
    'coordinate_change_determinant':str(s.factor(T.det())),
    'projection_center_Q1':'-(alpha*delta-beta*gamma)^2',
    'cancelled_quadric_coefficient':str((m*m-n)/Delta**2),
    'L':str(L),'R':str(R),
    'image_quartic_nonzero_coefficient_x0_squared_x3_squared':str(n*n),
    'uniform_resultant_equals_Delta_to_four_times_F':True,
    'curve_is_linear_transform_of_standard_RNC':True,
    'curve_lies_on_both_quadrics':True,
    'projected_curve_is_fixed_C0':True,
    'standard_surface_singular_locus_exactly_four_axes':True,
    'all_four_singularities_have_A1_local_models':True,
    'curve_passes_all_four_singularities':True,
    'quotient_cover_quadric_section_pulls_back_to_odd_square':True,
    'quadric_section_vanishes_on_actual_RNC':True,
    'odd_curve_branch_equation_verified':True,
    'L_curve_endpoint_coefficients':[str(alpha**2*gamma**2),str(beta**2*delta**2)],
    'R_curve_equals_minus_U_squared_V_squared_L_curve':True,
    'negative_lift_satisfies_Q1':True,
    'negative_lift_Q2_equals_minus_twice_U_squared_V_squared_L_curve':True,
    'negative_lift_violates_RNC_quadric_by':'-2*U^6*V^2',
    'no_assumption_m_nonzero':True,
    'no_assumption_cancelled_quadric_coefficient_nonzero':True,
    'uniform_parameter_identities_without_samples':True,
    'does_not_claim_all_singular_normalizations_or_all_four_A1_embeddings':True,
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(OUT/'countercheck-result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
