#!/usr/bin/env python3
"""Necessary defective e=1 triple/cubic reductions, not an exclusion.

Exact local syzygies, cocycle killing matrices, target twists, the
six boundary direction triples, and the compact sextic specification.
No universal third-order class or quartic incidence is solved here.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

delta, gamma, m, y = s.symbols('delta gamma m y')
g1, g2, g3 = delta*m-gamma*y*y, m*y, m*m
assert s.expand(m*g1+gamma*y*g2-delta*g3) == 0
assert s.expand(m*g2-y*g3) == 0
assert s.expand(gamma*y**3-delta*g2+y*g1) == 0
HB = s.Matrix([[m, 0], [gamma*y, m], [-delta, -y]])
assert s.expand(HB[[0, 1], :].det()-g3) == 0
assert s.expand(HB[[0, 2], :].det()+g2) == 0
assert s.expand(HB[[1, 2], :].det()-g1) == 0

# Direct third-layer valuation identity; independent integral cases.
for a in range(1, 10):
    for val_f3 in range(-40, 20):
        d3 = max(a, -a-val_f3)
        assert d3-a == max(0, -2*a-val_f3)

z, a0, a1, b0, b1, p = s.symbols('z a0 a1 b0 b1 p')
A, B = a0+a1*z, b0+b1*z
h2 = s.expand(-(2*A+z*B)*(12*A*A+3*z*z*B*B
                       +4*z*z*(s.diff(A,z)*B-A*s.diff(B,z)))/(8*z**5))
c = [s.factor(h2.coeff(z, -i)) for i in (1, 2, 3)]
l0, l1, l2 = s.symbols('l0 l1 l2')
kill1 = s.Matrix([[c[0], c[1]], [c[1], c[2]]])
kill2 = s.Matrix([[c[0], c[1], c[2]]])
assert (kill1*s.Matrix([l0,l1])-s.Matrix([
    s.expand((l0+l1*z)*h2).coeff(z,-i) for i in (1,2)])).applyfunc(s.expand) == s.zeros(2,1)
assert (kill2*s.Matrix([l0,l1,l2])-s.Matrix([
    s.expand((l0+l1*z+l2*z*z)*h2).coeff(z,-1)])).applyfunc(s.expand) == s.zeros(1,1)
sextic = s.expand(64*kill1.det())
compact = (8*p**3-(64*a1*a1+128*a1*b0+16*b0*b0)*p*p
           +(96*a1**4+512*a1**3*b0+592*a1*a1*b0*b0
             +128*a1*b0**3+6*b0**4)*p
           -(576*a1**6+960*a1**5*b0+880*a1**4*b0*b0
             +544*a1**3*b0**3+220*a1*a1*b0**4
             +60*a1*b0**5+9*b0**6))
assert s.expand(sextic-compact.subs(p,a0*b1)) == 0
assert len(s.Poly(sextic,a0,a1,b0,b1).terms()) == 16

r = s.symbols('r')
qr = 12*r*r+4*r+3
boundary_r = (2*r+1)*qr
left = [s.factor(ci.subs({a0:0,a1:r,b0:1,b1:1})) for ci in c]
right = [s.factor(ci.subs({a0:1,a1:r,b0:1,b1:0})) for ci in c]
assert left[2] == right[0] == 0
assert s.expand(left[1]+boundary_r/8) == 0
assert s.expand(right[1]+boundary_r/8) == 0
assert left[0].subs(r,-s.Rational(1,2)) != 0
assert right[2].subs(r,-s.Rational(1,2)) != 0
assert s.gcd(left[0],qr) == s.gcd(right[2],qr) == 1
# Principal boundary killing sections delta=z and delta=1, respectively.
assert all(s.rem(ci,boundary_r,r) == 0 for ci in left[1:])
assert all(s.rem(ci,boundary_r,r) == 0 for ci in right[:2])

# Cubic class target twists from P=L^3(D2), Q=M(-D2).
deg_L, deg_M = -6, -8
twists = {}
for d2,d3 in [(1,3),(2,2)]:
    source = 3*deg_L-deg_M+2*d2
    target = source+d3-d2
    assert target == -6
    twists[str((d2,d3))] = {'class_twist':source,'annihilator_degree':d3-d2,
                           'target_twist':target}
assert twists['(1, 3)']['class_twist'] == -8
assert twists['(2, 2)']['class_twist'] == -6
cubic_coefficients = s.symbols('C1:8')
hankel = s.Matrix([[cubic_coefficients[i+j] for j in range(3)] for i in range(5)])
annihilator = l0+l1*z+l2*z*z
cubic_laurent = sum(ci*z**(-i-1) for i,ci in enumerate(cubic_coefficients))
assert (hankel*s.Matrix([l0,l1,l2])-s.Matrix([
    s.expand(annihilator*cubic_laurent).coeff(z,-i) for i in range(1,6)])).applyfunc(s.expand) == s.zeros(5,1)

record = {
    'status':'PASS necessary structural identities; both defective MF6 types remain open',
    'second_cocycle_coefficients':list(map(str,c)),
    'd2_one_sextic_numerator':str(compact),
    'compact_invariant':'p=a0*b1; retain both a0=0 and b1=0 boundaries separately',
    'boundary_direction_equation':str(boundary_r),
    'boundary_left_coefficients':list(map(str,left)),
    'boundary_right_coefficients':list(map(str,right)),
    'cubic_target_twists':twists,
    'type_13_hankel_shape':[5,3],
    'type_22_condition':'all five Laurent coefficients of H1(O(-6)) vanish',
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'sympy':s.__version__,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print('PASS: local triple module syzygies and normalized cubic residue delta^2*f3')
print('PASS: exact d2=1 sextic and d2=2 linear quadratic-cocycle killing equations')
print('PASS: six boundary direction triples retained, with their proper endpoint defect')
print('PASS: type (1,3) quadratic 5x3 Hankel annihilator; type (2,2) five vanishing coefficients')
print('OPEN: neither universal cubic class nor complete ambient defective incidence is solved')
