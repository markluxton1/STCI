#!/usr/bin/env python3
"""Independent exact frame and two-target identities for the e=1 socle bridge.

The accepted finite-flat inverse-system/socle theorem and complete primitive
triple classification are geometric antecedents, not claims certified by
this script. No research module or generated certificate is imported.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

z, U, V, ell, r = s.symbols('z U V ell r')
q = U + z*V/2
B = -z*z*U + z**3*V/2 + V*V
jacobian = s.det(s.Matrix([[s.diff(q, U), s.diff(q, V)],
                          [s.diff(B, U), s.diff(B, V)]]).subs({U:0,V:0}))
assert s.expand(jacobian-z**3) == 0
assert s.cancel(z**3/jacobian) == 1
assert s.cancel(z**5/jacobian) == z*z

# These are the actual first-order moving-chart transitions of the balanced
# ambient normal frame. The quotient maps below check the L frame itself,
# rather than assuming that every Bezout lift has the right line-bundle twist.
Up, Vp = z**-7*U, z**-7*V
principal_L = {U:(1+z)*ell, V:(-2-8*z)*ell}
principal_m = (-2-8*z)*U-(1+z)*V
principal_mp = (-8-2/z)*Up-(1+1/z)*Vp
principal_ellp = -Up/3-Vp/6
assert s.expand(principal_mp-z**-8*principal_m) == 0
assert s.expand(principal_ellp.subs(principal_L)-z**-6*ell) == 0
algebraic_L = {U:r*z*ell, V:ell}
algebraic_m = U-r*z*V
algebraic_mp = Up/z-r*Vp
algebraic_ellp = Up/r
assert s.expand(algebraic_mp-z**-8*algebraic_m) == 0
assert s.expand(algebraic_ellp.subs(algebraic_L)-z**-6*ell) == 0
assert 3*(-6)-(-14) == -4  # tau_infinity=z^-4*tau_finite.

# The principal h/T data are explicit accepted quartic-jet coefficients.
# Recheck their determinant without importing their producing computation.
P = 4*z*z+2*z+1
h0 = P*z**3/16
h1 = P*(64*z**6+8*z**3+1)/1024
T0 = (2*z+1)*(1536*z**5+1152*z**4+448*z**3
              +48*z*z-24*z+4)
T1 = (2*z+1)*(1536*z**8+1152*z**7+448*z**6+240*z**5
              +120*z**4+60*z**3+30*z*z+15*z+8)
Delta = s.factor(h0*T1-h1*T0)
assert s.expand(Delta-(2*z-1)**3*(2*z+1)*P/256) == 0

A, BB, C, D = s.symbols('A BB C D')
f0, f1 = A+BB*z*z, C+D*z*z
tau_vars = s.symbols('tau0:5')
tau = sum(c*z**i for i,c in enumerate(tau_vars))
principal_relation = s.expand((64*z**6+8*z**3+1)*f0
                             -64*z**3*f1
                             -4*(2*z-1)**3*(2*z+1)*tau)
assert s.expand(principal_relation.subs(z,s.Rational(1,2))
                -(3*f0-8*f1).subs(z,s.Rational(1,2))) == 0
assert s.expand(principal_relation.subs(z,-s.Rational(1,2))
                -(f0+8*f1).subs(z,-s.Rational(1,2))) == 0
assert f0.subs(z,s.Rational(1,2)) == f0.subs(z,-s.Rational(1,2))
assert f1.subs(z,s.Rational(1,2)) == f1.subs(z,-s.Rational(1,2))
equations = s.Poly(principal_relation,z).all_coeffs()
mat, rhs = s.linear_eq_to_matrix(equations,(A,BB,C,D)+tau_vars)
assert rhs == s.zeros(mat.rows,1)
assert mat.rank() == 8 and len(mat.nullspace()) == 1
kernel = mat.nullspace()[0]
assert kernel[1] != 0
kernel = kernel/kernel[1]
assert list(kernel[:4]) == [-s.Rational(1,4),1,-s.Rational(3,32),s.Rational(3,8)]

# The algebraic-field relation has only the zero solution in the prescribed
# global degrees. Exact rank over Q(sqrt(-2)) handles both conjugate roots.
qr = 12*r*r+4*r+3
cc, dd = 2*r+s.Rational(2,3), s.Rational(8,9)*r
assert s.gcd(cc,qr) == 1 and s.gcd(dd,qr) == 1
alg_relation = s.expand(cc*z**8*f0-dd*z**3*tau-f1)
alg_mat,_ = s.linear_eq_to_matrix(s.Poly(alg_relation,z).all_coeffs(),
                                 (A,BB,C,D)+tau_vars)
root = (-1+2*s.sqrt(-2))/6
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import QQ
alg_DM = DomainMatrix.from_Matrix(alg_mat.subs(r,root)).convert_to(
    QQ.algebraic_field(s.sqrt(-2)))
assert alg_DM.rank() == 9

record = {
    'status':'PASS: exact frame, target, determinant and rank checks',
    'scope':'Fixed C0, characteristic zero, common quartic ancestor, e=1,D2=0',
    'antecedents':'Accepted finite-flat inverse-system/socle theorem; complete primitive e=1 quartic fibres; P-037',
    'target_symbols':['1','z**2'],
    'line_bundles':{'L':-6,'E3':-14,'Hom(L**3,E3)':4},
    'principal_determinant':str(Delta),
    'principal_constraint_rank':8,
    'principal_solution_target_rank':1,
    'algebraic_constraint_rank':9,
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'sympy':s.__version__,
}
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps(record,indent=2)+'\n')
print(record['status'])
print('PASS: principal finite target evaluations contradict the basepoint-free pencil')
print('PASS: algebraic global degree bounds force both target images to be zero')
