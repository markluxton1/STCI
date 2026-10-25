#!/usr/bin/env python3
"""Exact checks for the NEW residual-pair flag formulas only.

Run python3 research/computations/verify_quartic_flag_incidence_2026_10_24.py
Requires SymPy 1.14.0 in the selected Python environment.
An optional first argument chooses the JSON output path. No accepted proof,
normal splitting, or inherited secant/group classification is rerun.
"""
import json
from pathlib import Path
import sys
import sympy as s

checks = []
def check(name, condition, evidence):
    passed = bool(condition)
    checks.append({'name': name, 'passed': passed, 'evidence': str(evidence)})
    if not passed:
        raise AssertionError(name)

a,b,c,A,B,C,lam,aa,v = s.symbols('a b c A B C lam aa v')
x=s.Matrix([a,b,c]); y=s.Matrix([A,B,C]); M=s.Matrix([[0,0,1],[0,1,0],[1,0,0]])
check('bilinear_product_coefficient', s.expand((a+b*v+c*v*v)*(A+B*v+C*v*v)).coeff(v,2)==(x.T*M*y)[0], 'a*C+b*B+c*A')
check('pairing_nondegenerate_integrally', M.det()==-1, M.det())
T=s.diag(lam**2,lam,1)
J=s.Matrix([[0,0,aa**2],[0,aa,0],[1,0,0]])
check('torus_similitude', T.T*M*T==lam**2*M, 'T^t M T=lam^2 M')
check('reflection_similitude', J.T*M*J==aa**2*M and J*J==aa**2*s.eye(3), 'J^t M J=aa^2 M; J^2=aa^2')
check('swap_fixed_quadratic', (x.T*M*x)[0]==2*a*c+b*b, 2*a*c+b*b)
check('combined_reflection_fixed_conic', s.expand((x.T*M*J*x)[0])==a*a+aa*b*b+aa*aa*c*c, s.expand((x.T*M*J*x)[0]))

# Monic chart gamma=C=1; impose the middle coefficient b+d+a*c=0.
p,q,r=s.symbols('p q r')
d=-q-p*r
h=v*v+p*v+q; k=v*v+r*v+d
f=s.Matrix([q*d,p*d+q*r,p+r])
resultant=s.resultant(h,k,v)
jac=f.jacobian([p,q,r]).det()
check('factorization_jacobian_equals_negative_resultant', s.expand(jac+resultant)==0, s.factor(resultant))

# The fiber over v^4. A Groebner basis also exhibits its six monomials.
G=s.groebner([p**3-2*p*q,p*p*q-q*q],p,q)
expected=[p**3-2*p*q,p*p*q-q*q,p*q*q,q**3]
check('quadruple_root_fiber_groebner_basis', list(G)==expected, list(G))
std=[1,p,p*p,q,p*q,q*q]
check('quadruple_root_fiber_length_six', len(std)==6 and all(G.reduce(s.sympify(m))[1]==m for m in std), std)
check('quadruple_root_fiber_maximal_ideal_nilpotent', all(G.reduce(p**i*q**(6-i))[1]==0 for i in range(7)), '(p,q)^6=0')

# On L_iota: h=v^2-z, k=z*A+B*v+A*v^2.
z=s.symbols('z')
prod=s.expand((v*v-z)*(z*A+B*v+A*v*v))
check('even_factor_dual_cubic', s.expand(prod.coeff(v,0)*prod.coeff(v,3)**2+prod.coeff(v,1)**2*prod.coeff(v,4))==0, prod)
# This coordinate convention gives a0*a3^2+a1^2*a4=0 with four target
# coefficients numbered 0,1,3,4; equivalently a0*a2^2+a1^2*a3=0.

# Explicit characteristic-two boundary checks supplied to the synthesis.
D=s.symbols('D')
quartic=A+B*v+C*v**3+D*v**4
K=A*C*C+D*B*B
def mod2(expr, *gens):
    return s.Poly(s.expand(expr),*gens,modulus=2).as_expr()
check('characteristic_two_fixed_scheme_is_double_line', mod2((x.T*M*x)[0],a,b,c)==b*b, 'q mod 2=b^2')
check('characteristic_two_discriminant_square', mod2(s.discriminant(quartic,v)-K*K,A,B,C,D)==0, 'Disc mod 2=(A C^2+D B^2)^2')
check('characteristic_two_tangent_substitution', mod2(K.subs({A:D*v**4,B:C*v*v}, simultaneous=True),C,D,v)==0, 'A=D v^4, B=C v^2 => K=0')
X0,X1,X2,X3=s.symbols('X0 X1 X2 X3')
R=X0*X2*X2-X1*X1*X3
grad=[mod2(s.diff(R,X),X0,X1,X2,X3) for X in [X0,X1,X2,X3]]
check('characteristic_two_cubic_gauss_line', grad==[X2**2,0,0,X1**2], grad)

out=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('quartic_flag_incidence_2026_10_24.json')
payload={'scope':'New residual-pair flag identities for the fixed quartic; no canonical promotion', 'sympy':s.__version__, 'checks':checks, 'passed':all(c['passed'] for c in checks)}
out.write_text(json.dumps(payload,indent=2)+'\n')
print(f'{len(checks)} exact checks passed; wrote {out}')
