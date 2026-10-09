#!/usr/bin/env python3
"""Independent exact audit of the four e=2 endpoint direction families.

This audits classification coverage, the first family's generic certificate,
and every exceptional denominator factor.  It does not infer emptiness of
uncomputed families or of the retained finite exceptional fibres.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import sympy as s

HERE = Path(__file__).resolve().parent
t, k, a, c, b, d, lam = s.symbols('t k a c b d lam')
top = json.loads((HERE/'localcoh-symbol-top.json').read_text())
M = s.Matrix(top['matrix'])
C = s.Matrix(top['annihilator'])
assert M.shape == (32, 30) and M.rank() == 29
assert C.shape == (3, 32) and C.rank() == 3 and C*M == s.zeros(3, 30)


def symbol(p, r):
    return s.Matrix([s.expand(t*p**i*r**(3-i)).coeff(t, j)
                     for i in range(4) for j in range(8)])


def homogeneous_resultant(p, r):
    # This fixed-size Sylvester determinant retains infinity roots when
    # either dehomogenized quadratic loses degree at a parameter value.
    p0, p1, p2 = [s.expand(p).coeff(t, j) for j in range(3)]
    r0, r1, r2 = [s.expand(r).coeff(t, j) for j in range(3)]
    return s.factor(s.det(s.Matrix([[p2, p1, p0, 0], [0, p2, p1, p0],
                                    [r2, r1, r0, 0], [0, r2, r1, r0]])))


# Both endpoint coordinates are nonzero: common direction scaling and the
# ambient torus set p0=r0=1.  Neither operation changes primitivity.
p, r = 1+a*t+c*t*t, 1+b*t+d*t*t
equations = list(C*symbol(p, r))
bvalue = -6*(a*a+c)-2*a-s.Rational(3, 2)
assert s.expand(equations[0].subs(b, bvalue)) == 0
quadratic = 16*c*c+(16*a*a+12)*c+12*a*a+4*a+3
assert s.expand(equations[1].subs(b, bvalue)+s.Rational(3, 2)*quadratic) == 0
assert s.factor(s.discriminant(quadratic, c)) == 16*(2*a+1)**3*(2*a-3)
avalue = (k*k+3)/(2*(1-k*k))
cvalue = -(k*k+2*k+3)/(2*(k+1)**2)
inverse_k = (32*c+16*a*a+12)/(4*(2*a+1)**2)


def modulo_quadratic(value):
    numerator = s.together(value).as_numer_denom()[0]
    return s.factor(s.rem(numerator, quadratic, c))


# This rational inverse proves surjectivity onto the finite affine chart,
# not merely that a proposed parametrization produces some solutions.
assert modulo_quadratic(inverse_k**2-(2*a-3)/(2*a+1)) == 0
assert modulo_quadratic(avalue.subs(k, inverse_k)-a) == 0
assert modulo_quadratic(cvalue.subs(k, inverse_k)-c) == 0
assert s.factor(quadratic.subs(a, -s.Rational(1, 2))) == 4*(2*c+1)**2
last = s.factor(equations[2].subs(b, bvalue))
assert s.factor(last.subs({a: -s.Rational(1, 2), c: -s.Rational(1, 2)})) == 2*(d+2)**2
boundary_p = p.subs({a: -s.Rational(1, 2), c: -s.Rational(1, 2)})
boundary_r = r.subs({b: 1, d: -2})
assert s.degree(s.gcd(boundary_p, boundary_r), t) == 1
qk = k*k+2*k+3
bvalue_k = (k-3)*qk/((k-1)**2*(k+1))
dvalues = [-2*(k*k-4*k+5)*qk*qk/((k-1)**3*(k+1)**3),
           -2*(k*k+1)*(k*k-2*k-1)*qk/((k-1)**3*(k+1)**3)]
assert s.factor(last.subs({a: avalue, c: cvalue}) -
                2*(d-dvalues[0])*(d-dvalues[1])) == 0
expected_resultants = [
    8*qk*qk*(9*k**4-21*k**3+5*k*k-31*k+134)/((k-1)**6*(k+1)**6),
    -8*qk*(3*k**4-2*k**3-6*k*k-18*k-9)/((k-1)**5*(k+1)**6)]
for dvalue, expected in zip(dvalues, expected_resultants):
    values = {a: avalue, c: cvalue, b: bvalue_k, d: dvalue}
    assert all(s.cancel(eq.subs(values)) == 0 for eq in equations)
    assert s.cancel(homogeneous_resultant(p.subs(values), r.subs(values))-expected) == 0

# The second endpoint boundary p0=0,r0!=0 must be retained independently.
p, r = a*t+c*t*t, 1+b*t+d*t*t
equations_boundary = list(C*symbol(p, r))
assert equations_boundary[0] == 0
assert s.expand(equations_boundary[1]-3*(b-8*a*a*c)) == 0
expected = 4*c*(2*a+1)*((2*a+1)**2*d+
                         2*c*c*(2*a-1)*(16*a**4+8*a*a+5))
assert s.expand(equations_boundary[2].subs(b, 8*a*a*c)-expected) == 0
assert homogeneous_resultant(a*t, 1+d*t*t) == a*a*d
dboundary = -2*(2*k-1)*(16*k**4+8*k*k+5)/(2*k+1)**2
boundary_values = {a: k, c: 1, b: 8*k*k, d: dboundary}
assert all(s.cancel(eq.subs(boundary_values)) == 0 for eq in equations_boundary)
boundary_res = -(2*k-1)*(32*k**6+32*k**4+24*k**3+26*k*k+6*k+1)/(2*k+1)**2
assert s.cancel(homogeneous_resultant(p.subs(boundary_values), r.subs(boundary_values))-
                boundary_res) == 0
exception_values = {a: -s.Rational(1, 2), c: 1, b: 2}
assert all(s.cancel(eq.subs(exception_values)) == 0 for eq in equations_boundary)
assert s.expand(homogeneous_resultant(p.subs(exception_values), r.subs(exception_values))-
                (d+8)/4) == 0

# Verify the saved seeds for all four families, whether or not M2 completed.
for index in range(1, 5):
    seed_data = json.loads((HERE/f'session-localcoh-origin-family-{index}-seed.json').read_text())
    seed = s.Matrix([s.sympify(v, locals={'k': k}) for v in seed_data['seed']])
    kernel = s.Matrix([s.Rational(v) for v in seed_data['kernel']])
    assert M*kernel == s.zeros(32, 1) and kernel != s.zeros(30, 1)
    if index <= 2:
        pp = 1+avalue*t+cvalue*t*t
        rr = 1+bvalue_k*t+dvalues[index-1]*t*t
    elif index == 3:
        pp, rr = k*t+t*t, 1+8*k*k*t+dboundary*t*t
    else:
        pp, rr = -t/2+t*t, 1+2*t+k*t*t
    assert all(s.cancel(v) == 0 for v in M*seed-symbol(pp, rr))

# The existing polynomial certificate must concern the same actual affine
# line of ancestors, with all clearing factors kept explicit.
generic = json.loads((HERE/'session-localcoh-origin-family-1-polynomial-dual.json').read_text())
seed_data = json.loads((HERE/'session-localcoh-origin-family-1-seed.json').read_text())


def terms(value):
    return sum(s.Rational(v)*k**i*lam**j for i, j, v in value)


ancestor_denominator = 120*(k-1)**9*(k+1)**9
assert s.expand(terms(generic['ancestor_denominator'])-ancestor_denominator) == 0
for stored, seed_value, kernel_value in zip(generic['alpha'], seed_data['seed'], seed_data['kernel']):
    assert s.cancel(terms(stored)-ancestor_denominator*(
        s.sympify(seed_value, locals={'k': k})+lam*s.Rational(kernel_value))) == 0
remaining = [3*k**4-9*k**3-19*k*k-43*k-4,
             13*k**4+26*k**3+34*k*k+6*k-7,
             729*k**13+1620*k**12+2889*k**11-11268*k**10-26574*k**9-
             39642*k**8+94014*k**7+272968*k**6+454897*k**5+62256*k**4-
             571463*k**3-1210068*k*k-966908*k-379834]
nonprimitive_quartic = 9*k**4-21*k**3+5*k*k-31*k+134
target = 89514547200*(k-1)**14*(k+1)**11*(k*k-4*k+5)**5*qk**8*nonprimitive_quartic
for poly in remaining:
    target *= poly
assert s.expand(terms(generic['dual_on_u'])-target) == 0
for index, poly in enumerate(remaining):
    assert s.gcd(poly, s.diff(poly, k)) == 1
    assert s.gcd(poly, (k*k-1)*qk*nonprimitive_quartic) == 1
    for other in remaining[index+1:]:
        assert s.gcd(poly, other) == 1
subprocess.run([sys.executable, str(HERE/'session-localcoh-origin-generic-dual.py')], check=True)
subprocess.run([sys.executable, str(HERE/'verify_session_localcoh_q2_dual_2026_10_07.py')], check=True)

inputs = ['localcoh-symbol-top.json', 'session-localcoh-origin-parametrize.py',
          'session-localcoh-origin-boundary.py', 'session-localcoh-origin-generic-dual.py',
          'session-localcoh-origin-family-1-polynomial-dual.json',
          'session_localcoh_q2_dual_audit_2026_10_07.json'] + \
         [f'session-localcoh-origin-family-{index}-seed.json' for index in range(1, 5)]
(HERE/'session_localcoh_endpoint_audit_2026_10_07.json').write_text(json.dumps({
    'input_sha256': {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in inputs},
    'classification': 'PASS: all primitive h=t endpoint directions, both p0*r0!=0 and p0=0 boundary',
    'rational_inverse': str(inverse_k),
    'generic_certificate': 'PASS: actual pure-top affine lift and all 18 polynomial tensor identities',
    'q2_exception': 'PROVED EXCLUDED: both roots, every lambda',
    'remaining_first_family_polynomials': list(map(str, remaining)),
    'remaining_first_family_geometric_points': 21,
    'scope': 'Characteristic zero; primitive e=2 with top-zero at the chosen endpoint',
    'open': ['21 first-family exceptional direction fibres',
             'second rational family', 'p0=0 rational boundary family',
             'p0=0 exceptional boundary family', 'top-zero at a nonendpoint point']
}, indent=2)+'\n')
print('PASS: classification is surjective, including the omitted nonprimitive normalization point.')
print('PASS: fixed-degree homogeneous resultants include all infinity-root degenerations.')
print('PASS: rank29 top map gives the complete affine line of lifts for each direction.')
print('OPEN: 21 first-family exceptional geometric directions; three other families; nonendpoint top zero.')
