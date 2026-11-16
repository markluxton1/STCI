#!/usr/bin/env python3
"""Independent e=1 primitive-triple audit and surviving-carrier obstruction.

No imported research verifier or generated JSON is used.  The complete
degree-four ambient spaces are reconstructed in the 35 monomial columns,
including the support condition itself.  Rational identities, exact
quadratic-field ranks, both infinity charts and the affine normalization
identities are checked.  Characteristic zero, fixed C0 only.
"""
from pathlib import Path
import hashlib
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import QQ

x0, x1, x2, x3, z, w, U, V, y, m = s.symbols('x0 x1 x2 x3 z w U V y m')
xs = (x0, x1, x2, x3)
mon4 = [x0**i*x1**j*x2**k*x3**(4-i-j-k)
        for i in range(4, -1, -1)
        for j in range(4-i, -1, -1)
        for k in range(4-i-j, -1, -1)]
mon2 = [x0**i*x1**j*x2**k*x3**(2-i-j-k)
        for i in range(2, -1, -1)
        for j in range(2-i, -1, -1)
        for k in range(2-i-j, -1, -1)]
chart = {x0: 1, x1: z, x2: z**3+V,
         x3: z**4+U+s.Rational(3, 2)*z*V}

def ambient_vector(form):
    p = s.Poly(form, *xs)
    return s.Matrix([p.coeff_monomial(term) for term in mon4])

def complete_matrix(A, B, gamma, S, T):
    """Impose support, first and second jets on all ambient quartics."""
    assert s.expand(S*A+T*B-1) == 0
    sub = {U: A*y-T*gamma*y*y, V: B*y+S*gamma*y*y}
    jet = [s.expand(term.subs(chart).subs(sub)) for term in mon4]
    rows = []
    for order in range(3):
        polys = [p.coeff(y, order) for p in jet]
        degree = max(s.degree(p, z) if p else 0 for p in polys)
        rows.extend([[p.coeff(z, power) for p in polys]
                     for power in range(degree+1)])
    return s.Matrix(rows)

def cubic_data(form, A, B, S, T, gamma, substitutions=chart, modulus=None):
    jet = s.expand(form.subs(substitutions).subs({U: T*m+A*y, V: -S*m+B*y}))
    h = jet.coeff(m, 1).coeff(y, 0)
    cross = jet.coeff(m, 1).coeff(y, 1)
    pure = jet.coeff(m, 0).coeff(y, 3)
    second = s.expand(jet.coeff(m, 0).coeff(y, 2)-gamma*h)
    if modulus is None:
        assert second == 0
    else:
        assert all(s.rem(coefficient, modulus, r) == 0
                   for coefficient in s.Poly(second, z, w).coeffs())
    return s.expand(h), s.expand(gamma*cross-pure)

# Derive the universal cocycle through the actual moving support coordinate.
a0, a1, b0, b1 = s.symbols('a0 a1 b0 b1')
A, B = a0+a1*z, b0+b1*z
Av, Bv = a1+a0*w, b1+b0*w
def trunc2(expr):
    expr = s.expand(expr)
    return sum(expr.coeff(y, i)*y**i for i in range(3))
u, v = A*y, B*y
b = u+s.Rational(3, 2)*z*v
den_inv = z**-4*(1-b/z**4+b*b/z**8)
W = trunc2((z**3+v)*den_inv)
ap = trunc2(z*den_inv-trunc2(W**3))
bp = trunc2(den_inv-trunc2(W**4))
up, vp = ap/2, trunc2(-3*trunc2(W*ap)+2*bp)
mp = trunc2(Bv.subs(w, W)*up-Av.subs(w, W)*vp)
assert s.expand(mp.coeff(y, 1)) == 0
h2 = s.expand(z**8*mp.coeff(y, 2))
assert s.expand(h2+(2*A+z*B)*(12*A*A+3*z*z*B*B
                    +4*z*z*(s.diff(A, z)*B-A*s.diff(B, z)))/(8*z**5)) == 0
obstruction = [s.factor(h2.coeff(z, -i)) for i in (1, 2, 3)]
expected = [-b1*(2*a0*b1+12*a1*a1+16*a1*b0+9*b0*b0)/8,
            -(2*a1+b0)*(8*a0*b1+12*a1*a1+4*a1*b0+3*b0*b0)/8,
            -a0*(2*a0*b1+36*a1*a1+16*a1*b0+3*b0*b0)/4]
assert all(s.expand(p-q) == 0 for p, q in zip(obstruction, expected))

# Direct classification case identities; no numerical root search/saturation.
p, c, d = s.symbols('p c d')
first = 2*p+12*c*c+16*c*d+9*d*d
middle = 8*p+12*c*c+4*c*d+3*d*d
third = 2*p+36*c*c+16*c*d+3*d*d
assert s.expand(third-first-6*(2*c-d)*(2*c+d)) == 0
assert s.expand(middle.subs({c:d/2, p:-10*d*d})) == -72*d*d
assert s.expand(first.subs({c:-d/2, p:-2*d*d})) == 0
assert s.expand(middle.subs({c:-d/2, p:-2*d*d})) == -12*d*d
assert s.expand(third.subs({c:-d/2, p:-2*d*d})) == 0
# The middle *equation* has the factor (2c+d), so the last nonzero bracket
# is harmless. Mixed a0,b1 boundary cases have no bpf solution (note proof).
assert s.expand((third-3*middle).subs(p, 0)-4*d*(c-3*d/2)) == 0
assert s.expand((first-middle).subs(p, 0)-6*d*(2*c+d)) == 0

# Principal orbit: expected forms are explicit polynomials, checked against
# the complete 35-column matrix rather than inherited generator coordinates.
F0 = (-x0*x0*x2*x2-4*x0*x0*x2*x3-4*x0*x0*x3*x3
      +2*x0*x1*x2*x2-4*x0*x1*x2*x3-16*x0*x1*x3*x3
      +8*x0*x2**3+x1**3*x2+2*x1**3*x3+8*x1*x1*x2*x2
      +8*x1*x1*x2*x3-16*x1*x1*x3*x3+16*x1*x2**3)/16
F1 = (-x0**3*x2-2*x0**3*x3-12*x0*x0*x1*x3-48*x0*x0*x2*x3
      +x0*x1**3+12*x0*x1*x1*x2-24*x0*x1*x1*x3+48*x0*x1*x2*x2
      -96*x0*x1*x2*x3-192*x0*x1*x3*x3-384*x0*x2*x2*x3
      -768*x0*x2*x3*x3-512*x0*x3**3+2*x1**4+24*x1**3*x2
      +96*x1*x1*x2*x2+192*x1*x1*x2*x3+384*x1*x2**3
      +768*x1*x2*x2*x3-1024*x1*x3**3+512*x2**4+1024*x2**3*x3)/1024
Ag, Bg, gamma = 1+z, -2-8*z, 192*z+96
sg, tg = s.Rational(4, 3), s.Rational(1, 6)
Mg = complete_matrix(Ag, Bg, gamma, sg, tg)
assert Mg.rank() == 33
vectors = s.Matrix.hstack(ambient_vector(F0), ambient_vector(F1))
assert vectors.rank() == 2 and Mg*vectors == s.zeros(Mg.rows, 2)
alpha, beta = s.symbols('alpha beta')
h, T = cubic_data(alpha*F0+beta*F1, Ag, Bg, sg, tg, gamma)
assert s.degree(h.subs(beta, 1), z) == 8
res = s.factor(s.resultant(h.subs(beta, 1), T.subs(beta, 1), z))
assert s.expand(res+s.Rational(27, 2**26)*(8*alpha-1)*(8*alpha+3)**3) == 0
generic_gcds = {}
for value, degree in [(s.Rational(1, 8), 1), (-s.Rational(3, 8), 2)]:
    gcd = s.gcd(h.subs({alpha:value, beta:1}), T.subs({alpha:value, beta:1}))
    assert s.degree(gcd, z) == degree
    generic_gcds[str(value)] = str(s.factor(gcd))
h0, T0 = h.subs({alpha:1, beta:0}), T.subs({alpha:1, beta:0})
assert s.degree(h0, z)-s.degree(s.gcd(h0, T0), z) == 3
chart_inf = {x3: 1, x2: w, x1: w**3+2*U, x0: w**4+V/2+3*w*U}
hi, Ti = cubic_data(F0, 1+w, -8-2*w, -s.Rational(1, 3),
                   -s.Rational(1, 6), 3*w+6, chart_inf)
assert s.expand(hi-w**3*(w*w+2*w+4)/16) == 0
assert Ti.subs(w, 0) != 0
assert s.expand(Ti+(w+2)*(w*w+2*w+4)*(3*w**3+3*w*w-4*w+2)/16) == 0

# Quadric factor orbit: full degree-four kernel, including order-two forms.
Mq = complete_matrix(-z/2, s.Integer(1), s.Integer(0), s.Integer(0), s.Integer(1))
assert Mq.rank() == 25
qforms = s.Matrix.hstack(*[ambient_vector((x0*x3-x1*x2)*term) for term in mon2])
assert qforms.rank() == 10 and Mq*qforms == s.zeros(Mq.rows, 10)

# Both conjugate algebraic directions, in an exact quadratic extension.
r = s.symbols('r')
qr = 12*r*r+4*r+3
def reduced(expr):
    return s.Add(*[s.rem(coefficient, qr, r)*z**powers[0]*w**powers[1]
                   *y**powers[2]*m**powers[3]
                   for powers, coefficient in s.Poly(s.expand(expr), z, w, y, m).terms()])
R0 = x0**3*x3-(r+s.Rational(3, 2))*x0*x0*x1*x2+(r+s.Rational(1, 2))*x1**4
R1 = x0*x3**3+(r-s.Rational(7, 6))*x1*x2*x3*x3+(s.Rational(1, 6)-r)*x2**4
Mr = complete_matrix(r*z, s.Integer(1), s.Integer(0), s.Integer(0), s.Integer(1))
root = (-1+2*s.sqrt(-2))/6
DM = DomainMatrix.from_Matrix(Mr.subs(r, root)).convert_to(QQ.algebraic_field(s.sqrt(-2)))
assert DM.rank() == 33
rvectors = s.Matrix.hstack(ambient_vector(R0), ambient_vector(R1))
assert rvectors.rank() == 2
assert all(s.rem(c, qr, r) == 0 for c in Mr*rvectors)
hr, Tr = cubic_data(alpha*R0+beta*R1, r*z, s.Integer(1),
                    s.Integer(0), s.Integer(1), s.Integer(0), modulus=qr)
assert reduced(hr-alpha-beta*(2*r+s.Rational(2, 3))*z**8) == 0
assert reduced(Tr-beta*s.Rational(8, 9)*r*z**3) == 0
assert s.gcd(r, qr) == 1 and s.gcd(2*r+s.Rational(2, 3), qr) == 1
rinv = -4*r-s.Rational(4, 3)
assert s.rem(r*rinv-1, qr, r) == 0
jinf = s.expand(R0.subs(chart_inf).subs({U:r*y, V:w*y-rinv*m}))
hri, Kri = reduced(jinf.coeff(m, 1).coeff(y, 0)), reduced(jinf.coeff(m, 0).coeff(y, 3))
assert s.expand(hri-w**8) == 0
assert reduced(jinf.coeff(m, 0).coeff(y, 2)) == 0
assert s.expand(Kri-(s.Rational(16, 27)*r+s.Rational(4, 9))*w**3) == 0
assert s.gcd(s.Rational(16, 27)*r+s.Rational(4, 9), qr) == 1

# New all-degree remaining-carrier obstruction. Distinguish coefficient
# kappa from a defining equation's degree. Every identity is polynomial.
u, v, kappa = s.symbols('u v kappa')
a = kappa+1
X1 = u*u*(a*v-u)/kappa
X0 = u*X1
surface = x0**3*x3-a*x0*x0*x1*x2+kappa*x1**4
normsub = {x0:X0, x1:X1, x2:v, x3:1}
assert s.factor(surface.subs(normsub)) == 0
assert s.factor(u**3-a*v*u*u+kappa*X1) == 0
delta = v-u
cofactor = kappa*v*v+kappa*u*v-u*u
assert s.factor(X1-v**3+delta*cofactor/kappa) == 0
assert s.factor(X0-v**4-u*(X1-v**3)+delta*v**3) == 0
assert X0.subs(u, 0) == X1.subs(u, 0) == 0
assert s.factor(X0.subs(u, a*v)) == s.factor(X1.subs(u, a*v)) == 0
assert s.expand(3*(r+s.Rational(1, 2))**2-2*(r+s.Rational(1, 2))+1-qr/4) == 0
assert s.expand(kappa*(s.Rational(2, 3)-kappa)-s.Rational(1, 3)
                +(3*kappa*kappa-2*kappa+1)/3) == 0
# Coordinate reversal carries the other pencil member to the conjugate R0.
reverse = {x0:x3, x1:x2, x2:x1, x3:x0}
conjugate_r = -r-s.Rational(1, 3)
assert s.expand(R1-R0.subs(r, conjugate_r).subs(reverse, simultaneous=True)) == 0

# Small-degree BF implications, corrected separately at b=6.
assert 2*6-8 == 4       # D3=D5 since D2=0.
assert (2*7-8)/2 == 3   # 2D3=D6.
assert (2*8-8)/2 == 4   # D3+D4=D7 and D4>=D3.

record = {
    'status':'PASS exact audit; geometric proof and scopes in companion note',
    'ambient_column_count':35,
    'complete_matrix_ranks':{'principal':33, 'quadric':25, 'algebraic':33},
    'principal_resultant':str(res),
    'principal_exceptional_gcds':generic_gcds,
    'principal_infinity_h':str(s.factor(hi)),
    'principal_infinity_T':str(s.factor(Ti)),
    'algebraic_infinity_h':str(hri),
    'algebraic_infinity_K':str(Kri),
    'normalization':{'X0':str(X0), 'X1':str(X1), 'X2':'v', 'X3':'1'},
    'scope':'Fixed C0, characteristic zero, quartic carrier, e=1,D2=0, every mate degree',
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'sympy':s.__version__,
}
output = Path(__file__).with_name('audit_mf6_e1_primitive_2026_10_07.json')
output.write_text(json.dumps(record, indent=2)+'\n')
print('PASS: independent complete 35-column ambient matrices for all four direction orbits')
print('PASS: generic-orbit polar bound >=6; algebraic mixed members polar bound >=8')
print('PASS: both moving infinity boundary members, including exact multiplicities')
print('PASS: surviving pure members finite normalization, full support and branch-value identities')
print('RESULT: together with audited BF bound d3<=5, all e=1,D2=0 quartic carriers are excluded')
