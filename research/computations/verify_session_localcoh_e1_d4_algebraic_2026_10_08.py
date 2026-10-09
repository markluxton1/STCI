#!/usr/bin/env python3
"""All quartic fibres for d2=4 in the two algebraic primitive directions.

Reconstruct all35 ambient monomials, retain both roots of12r^2+4r+3,
and prove the full quartic containment operator has kernel dimension at
most one for every homogeneous quartic defect section, including infinity
and repeated roots. No broad Groebner search or generic-rank inference.
"""
from pathlib import Path
import hashlib
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import QQ

x0,x1,x2,x3,z,U,V,y,m,r = s.symbols('x0 x1 x2 x3 z U V y m r')
xs=(x0,x1,x2,x3)
qr=12*r*r+4*r+3
root=(-1+2*s.sqrt(-2))/6
field=QQ.algebraic_field(s.sqrt(-2))
monomials=[x0**a*x1**b*x2**c*x3**(4-a-b-c)
           for a in range(5) for b in range(5-a) for c in range(5-a-b)]
finite={x0:1,x1:z,x2:z**3+V,x3:z**4+U+s.Rational(3,2)*z*V}


def reduced(value):
    return s.Add(*[s.rem(coefficient,qr,r)*z**powers[0]*y**powers[1]*m**powers[2]
                  for powers,coefficient in s.Poly(s.expand(value),z,y,m).terms()])


def jets(forms):
    return [reduced(F.subs(finite).subs({U:m+r*z*y,V:y})) for F in forms]


# Complete double conditions, not an assumed seven-dimensional source.
all_jets=jets(monomials)
rows=[]
for normal_order in (0,1):
    polynomials=[value.coeff(m,0).coeff(y,normal_order) for value in all_jets]
    degree=max(s.degree(value,z) for value in polynomials if value)
    rows.extend([[s.expand(value).coeff(z,power) for value in polynomials]
                 for power in range(degree+1)])
matrix=s.Matrix(rows)
assert DomainMatrix.from_Matrix(matrix.subs(r,root)).convert_to(field).rank()==28

# Explicit normalized basis: primitive h=1,z8 and five forms with E=z^i.
primitive0=x0**3*x3-(r+s.Rational(3,2))*x0*x0*x1*x2+(r+s.Rational(1,2))*x1**4
primitive8=-2*r*x0*x3**3+(3*r+s.Rational(1,2))*x1*x2*x3*x3-(r+s.Rational(1,2))*x2**4
forms=[
    x0*x0*x2*x2+(3*r-s.Rational(1,2))*x0*x1*x1*x3-(3*r+s.Rational(1,2))*x1**3*x2,
    (3*r+s.Rational(5,2))*x0*x0*x2*x3-(6*r+2)*x0*x1*x2*x2+(3*r-s.Rational(1,2))*x1**3*x3,
    -(6*r+2)*(x0*x3-x1*x2)**2,
    (5*r+s.Rational(1,6))*x0*x1*x3*x3+(r+s.Rational(11,6))*x0*x2**3-(6*r+2)*x1*x1*x2*x3,
    (r+s.Rational(11,6))*x0*x2*x2*x3+(s.Rational(4,3)*r-s.Rational(5,9))*x1*x1*x3*x3-
    (s.Rational(7,3)*r+s.Rational(23,18))*x1*x2**3]
basis=[primitive0,*forms,primitive8]
vectors=s.Matrix.hstack(*[s.Matrix([s.Poly(F,*xs).coeff_monomial(term) for term in monomials]) for F in basis])
assert DomainMatrix.from_Matrix(vectors.subs(r,root)).convert_to(field).rank()==7
assert (matrix*vectors).applyfunc(lambda value:s.rem(s.expand(value),qr,r))==s.zeros(matrix.rows,7)
coefficients=[3*r-s.Rational(1,2),6*r+2,s.Integer(0),4*r-s.Rational(5,3),(66*r+13)/18]
for i,value in enumerate(jets(forms)):
    assert value.coeff(m,0).coeff(y,0)==value.coeff(m,0).coeff(y,1)==0
    assert s.expand(value.coeff(m,1).coeff(y,0)-coefficients[i]*z**(i+2))==0
    assert s.expand(value.coeff(m,0).coeff(y,2)-z**i)==0
for value,expected_h in zip(jets([primitive0,primitive8]),[s.Integer(1),z**8]):
    assert s.expand(value.coeff(m,1).coeff(y,0)-expected_h)==0
    assert value.coeff(m,0).coeff(y,2)==0

# No two coefficients coincide at either field embedding.
for i,a in enumerate(coefficients):
    for b in coefficients[i+1:]:
        assert s.gcd(s.together(a-b).as_numer_denom()[0],qr)==1

d=s.symbols('d0:5'); e=s.symbols('e0:5')
delta=sum(value*z**i for i,value in enumerate(d))
E=sum(value*z**i for i,value in enumerate(e))
h_middle=sum(a*value*z**(i+2) for i,(a,value) in enumerate(zip(coefficients,e)))
polynomial=s.Poly(s.expand(delta*E-h_middle),z)
operator=s.Matrix([[s.expand(polynomial.coeff_monomial(z**power)).coeff(value)
                    for value in e] for power in range(1,8)])

# Exact minors cover the complete delta parameter space.
assert s.expand(operator[[0,1,2,3],[1,2,3,4]].det()-d[0]**4)==0
assert s.expand(operator[[3,4,5,6],[0,1,2,3]].det()-d[4]**4)==0
boundary=operator.subs({d[0]:0,d[4]:0})
assert s.expand(boundary[:5,:].det()-d[1]**5)==0
assert s.expand(boundary[2:7,:].det()-d[3]**5)==0
diagonal=boundary.subs({d[1]:0,d[3]:0})[1:6,:]
assert diagonal==s.diag(*[d[2]-a for a in coefficients])
# Pairwise distinct a_i allow at most one zero on this last diagonal.
# Together the four displayed minors and this final case prove rank>=4
# for every delta, hence dimension(kernel)<=1, with no open strata omitted.

HERE=Path(__file__).resolve().parent
record={
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'scope':'C0 char0; both roots of12r^2+4r+3; e1,d2=4; genuine global correction theta nonzero normalized1; all homogeneous delta including repeated/infinity roots',
    'status':'PASS: complete quartic fibre dimension at most1 for every delta; two independent target multipliers impossible',
    'double_matrix_shape':list(matrix.shape),'double_matrix_rank':28,
    'complete_double_basis':list(map(str,basis)),
    'normalized_hE_coefficients':list(map(str,coefficients)),
    'operator':[[str(value) for value in row] for row in operator.tolist()],
    'covering_minors':['d0^4','d4^4','d1^5 on d0=d4=0','d3^5 on d0=d4=0'],
    'last_case':'delta=d2*z^2; pairwise distinct diagonal constants imply rank>=4',
    'theta_zero':'nonprimitive flatness failure for genuine D2=4; not a discarded valid branch',
    'retained':'principal obstruction-zero direction and obstruction-nonzero directions in positive-D2 ancestor strata'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print('PASS: all35 ambient double conditions rank28; full normalized7-form basis verified at both roots.')
print('PASS: exact h/E weights, pairwise field-unit differences, all covering minors and final diagonal case.')
print('PROVED: every genuine d2=4 triple in either algebraic primitive direction has quartic fibre dimension<=1.')
