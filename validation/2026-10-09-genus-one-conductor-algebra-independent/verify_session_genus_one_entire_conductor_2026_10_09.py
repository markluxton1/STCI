#!/usr/bin/env python3
"""Bounded symbolic companion to root's full genus-one conductor proof."""
import json
from pathlib import Path

import sympy as s

x0, x1, x2, x3, z, U, V, t = s.symbols('x0 x1 x2 x3 z U V t')
a, b, c, d, e, f, g, h, i, j = s.symbols('a b c d e f g h i j')
E = [x0*z-x1**2, x0*x2-x1*z, x0*x3-x1*x2,
     x1*x2-z**2, x1*x3-z*x2, z*x3-x2**2]
lift = {x0: U**4, x1: U**3*V, x2: U*V**3, x3: V**4, z: U**2*V**2}
checks = {}

def check(label, expression):
    assert s.expand(expression) == 0, label
    checks[label] = True

for n, quadric in enumerate(E):
    check(f'actual_RNC_quadric_{n}', quadric.subs(lift))
A = a*x0-b*x1-d*x2+e*x3
R1 = x1*x2-a*x1**2+b*x0*x2+c*(x0*x3-x1*x2)+d*x1*x3-e*x2**2
L = f*x0-g*x1-i*x2+j*x3
R = -f*x1**2+g*x0*x2+h*(x0*x3-x1*x2)+i*x1*x3-j*x2**2
Q1 = z**2-A*z-R1
Q2 = L*z+R
check('normalized_first_quadric', Q1+E[3]+a*E[0]+b*E[1]+c*E[2]+d*E[4]+e*E[5])
check('normalized_second_quadric', Q2-f*E[0]-g*E[1]-h*E[2]-i*E[4]-j*E[5])
F = R**2+A*L*R-R1*L**2
check('elimination_identity', L**2*Q1-(Q2**2-(2*R+A*L)*Q2+F))
check('conductor_Lz', L*z+R-Q2)
check('conductor_Rz', R*z-A*R+L*R1-(z-A)*Q2+L*Q1)
check('trace_involution', Q1.subs(z, A-z)-Q1)
Lc = s.expand(L.subs(lift))
Ac = s.expand(A.subs(lift))
zc = U**2*V**2
check('curve_R_restriction', R.subs(lift)+zc*Lc)
check('curve_R1_restriction', R1.subs(lift)-zc**2+Ac*zc)
assert s.Poly(Lc,U,V).coeff_monomial(U**2*V**2) == 0
assert s.Poly(Ac-2*zc,U,V).coeff_monomial(U**2*V**2) == -2
checks['middle_coefficient_L'] = True
checks['middle_coefficient_other_root'] = True
hs_B = (1-t**2)**2/(1-t)**5
hs_A = (1-t**4)/(1-t)**4
hs_C = (1-t)*(1-t**2)/(1-t)**4
assert s.cancel(hs_B-hs_A-t*hs_C) == 0
checks['Hilbert_series_exact_module'] = True
report = {'status':'PASS', 'field':'Q with independent symbolic parameters',
          'checks':checks, 'check_count':len(checks),
          'scope':'entire conductor algebra and fixed-C0 identities; no global STCI conclusion'}
output = Path('research/scratch/session-genus-one-entire-conductor-2026-10-09.json')
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,sort_keys=True))
