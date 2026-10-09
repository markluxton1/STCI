#!/usr/bin/env python3
"""Exact rational normalization of the h=t endpoint chart with p0*r0 nonzero.

Uses SymPy for exact identities. Outputs two rational direction families;
does not claim that their quartic multiplication incidence is empty.
"""
from pathlib import Path
import json
import sympy as s

HERE = Path(__file__).resolve().parent
t, a1, a2, b1, b2, k = s.symbols('t a1 a2 b1 b2 k')
data = json.loads((HERE/'localcoh-symbol-top.json').read_text())
p, r = 1+a1*t+a2*t*t, 1+b1*t+b2*t*t
pure = s.Matrix([s.expand(t*p**i*r**(3-i)).coeff(t, j)
                 for i in range(4) for j in range(8)])
constraints = list(s.Matrix(data['annihilator'])*pure)
b1_value = -6*(a1*a1+a2)-2*a1-s.Rational(3, 2)
assert s.expand(constraints[0].subs(b1, b1_value)) == 0
quadratic = s.factor(constraints[1].subs(b1, b1_value)*(-s.Rational(2, 3)))
assert s.expand(quadratic-(16*a2*a2+(16*a1*a1+12)*a2+12*a1*a1+4*a1+3)) == 0
assert s.factor(s.discriminant(quadratic, a2)) == 16*(2*a1+1)**3*(2*a1-3)
a1_value = (k*k+3)/(2*(1-k*k))
a2_value = -(k*k+2*k+3)/(2*(k+1)**2)
b1_value_k = (k-3)*(k*k+2*k+3)/((k-1)**2*(k+1))
assert s.factor(quadratic.subs({a1: a1_value, a2: a2_value})) == 0
assert s.factor(b1_value.subs({a1: a1_value, a2: a2_value})-b1_value_k) == 0
q = k*k+2*k+3
b2_values = [
    -2*(k*k-4*k+5)*q*q/((k-1)**3*(k+1)**3),
    -2*(k*k+1)*(k*k-2*k-1)*q/((k-1)**3*(k+1)**3)
]
remaining = s.factor(constraints[2].subs(b1, b1_value))
remaining_k = s.factor(remaining.subs({a1: a1_value, a2: a2_value}))
assert s.factor(remaining_k-2*(b2-b2_values[0])*(b2-b2_values[1])) == 0
families = []
expected_resultants = [
    8*q*q*(9*k**4-21*k**3+5*k*k-31*k+134)/((k-1)**6*(k+1)**6),
    -8*q*(3*k**4-2*k**3-6*k*k-18*k-9)/((k-1)**5*(k+1)**6)
]
for index, b2_value in enumerate(b2_values):
    values = {a1: a1_value, a2: a2_value, b1: b1_value_k, b2: b2_value}
    assert all(s.factor(equation.subs(values)) == 0 for equation in constraints)
    pp, rr = s.factor(p.subs(values)), s.factor(r.subs(values))
    delta = s.factor(s.resultant(pp, rr, t))
    assert s.factor(delta-expected_resultants[index]) == 0
    families.append({'label': 'origin-family-'+str(index+1),
                     'a1': str(a1_value), 'a2': str(a2_value),
                     'b1': str(b1_value_k), 'b2': str(b2_value),
                     'resultant': str(delta)})
# Only the normalization point at infinity is missing from the finite k
# parametrization. Its affine direction contains the common factor 1-t.
boundary = {a1: -s.Rational(1, 2), a2: -s.Rational(1, 2),
            b1: s.Integer(1), b2: -s.Integer(2)}
assert all(s.expand(equation.subs(boundary)) == 0 for equation in constraints)
assert s.expand(p.subs(boundary)+(t-1)*(t+2)/2) == 0
assert s.expand(r.subs(boundary)+(t-1)*(2*t+1)) == 0
assert s.factor(remaining.subs({a1: -s.Rational(1, 2),
                              a2: -s.Rational(1, 2)})) == 2*(b2+2)**2
(HERE/'session-localcoh-origin-families.json').write_text(json.dumps({
    'scope': 'all primitive e=2 directions in h=t chart with p(0)*r(0) nonzero',
    'open_conditions': 'k != 1,-1 and displayed homogeneous resultant != 0',
    'boundary_at_infinity': 'p=(1-t)(1+t/2), r=(1-t)(1+2t); nonprimitive',
    'families': families,
    'status': 'EXACT PARAMETRIZATION; QUARTIC INCIDENCE OPEN'
}, indent=2)+'\n')
print('PASS: all three top-image equations factor exactly into two rational families.')
print('PASS: exact homogeneous resultants and the unique omitted nonprimitive boundary.')
print('Scope: h=t, p(0)*r(0) nonzero chart; no multiplier incidence exclusion claimed.')
