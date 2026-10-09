#!/usr/bin/env python3
"""Exact full double-quartic maps for the e1,d2=4 obstruction-zero directions.

All35 ambient monomials are reconstructed. This produces the full h/E
linear map, and the complete linear-in-delta rank reduction, on the
principal orbit and both roots of the exact quadratic direction equation.
It does not infer emptiness from a generic rank computation.
"""
from pathlib import Path
import hashlib
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import QQ

HERE = Path(__file__).resolve().parent
x0,x1,x2,x3,z,U,V,y,m,r = s.symbols('x0 x1 x2 x3 z U V y m r')
xs = (x0,x1,x2,x3)
monomials = [x0**a*x1**b*x2**c*x3**(4-a-b-c)
             for a in range(5) for b in range(5-a) for c in range(5-a-b)]
finite = {x0:1,x1:z,x2:z**3+V,x3:z**4+U+s.Rational(3,2)*z*V}
qr = 12*r*r+4*r+3
root = (-1+2*s.sqrt(-2))/6
delta_vars = s.symbols('d0:5')
delta = sum(value*z**i for i,value in enumerate(delta_vars))


def reduce_r(value):
    return s.Add(*[s.rem(coefficient,qr,r)*z**powers[0]*y**powers[1]*m**powers[2]
                  for powers,coefficient in s.Poly(s.expand(value),z,y,m).terms()])


def coefficient_matrix(polynomials):
    max_degree = max(s.degree(value,z) for value in polynomials if value != 0)
    return s.Matrix([[s.expand(value).coeff(z,i) for value in polynomials]
                     for i in range(max_degree+1)])


cases = []
for label,A,B,bezs,bezt,gamma in [
        ('principal',1+z,-2-8*z,s.Rational(4,3),s.Rational(1,6),192*z+96),
        ('algebraic',r*z,s.Integer(1),s.Integer(0),s.Integer(1),s.Integer(0))]:
    assert s.expand(bezs*A+bezt*B) == 1
    jets = [s.expand(F.subs(finite).subs({U:bezt*m+A*y,V:-bezs*m+B*y}))
            for F in monomials]
    restrictions = [jet.coeff(m,0).coeff(y,0) for jet in jets]
    linear = [jet.coeff(m,0).coeff(y,1) for jet in jets]
    matrix = coefficient_matrix(restrictions).col_join(coefficient_matrix(linear))
    if label == 'principal':
        assert matrix.rank() == 28
        basis = s.Matrix.hstack(*matrix.nullspace())
    else:
        field = QQ.algebraic_field(s.sqrt(-2))
        actual = DomainMatrix.from_Matrix(matrix.subs(r,root)).convert_to(field)
        assert actual.rank() == 28
        basis_root = actual.nullspace().to_Matrix().T
        basis = basis_root.applyfunc(lambda value: s.rem(s.expand(value.subs(s.sqrt(-2),3*r+s.Rational(1,2))),qr,r))
        assert (matrix*basis).applyfunc(lambda value:s.rem(s.expand(value),qr,r)) == s.zeros(matrix.rows,7)
    assert basis.shape == (35,7)
    forms = [s.expand(sum(coefficient*F for coefficient,F in zip(basis.col(j),monomials)))
             for j in range(7)]
    full_jets = [s.expand(F.subs(finite).subs({U:bezt*m+A*y,V:-bezs*m+B*y}))
                 for F in forms]
    h = [jet.coeff(m,1).coeff(y,0) for jet in full_jets]
    E = [s.expand(jet.coeff(m,0).coeff(y,2)-gamma*hh)
         for jet,hh in zip(full_jets,h)]
    if label == 'algebraic':
        h,E = [[reduce_r(value) for value in values] for values in (h,E)]
    assert all(value==0 or s.degree(value,z)<=8 for value in h)
    assert all(value==0 or s.degree(value,z)<=4 for value in E)
    H = s.Matrix([[s.expand(value).coeff(z,i) for value in h] for i in range(9)])
    Err = s.Matrix([[s.expand(value).coeff(z,i) for value in E] for i in range(5)])
    if label == 'principal':
        assert Err.rank() == 5
        assert H.col_join(Err).rank() == 7
    else:
        assert DomainMatrix.from_Matrix(Err.subs(r,root)).convert_to(field).rank() == 5
        assert DomainMatrix.from_Matrix(H.col_join(Err).subs(r,root)).convert_to(field).rank() == 7
    polynomial_columns = [s.expand(hh-delta*ee) for hh,ee in zip(h,E)]
    operator = s.Matrix([[value.coeff(z,i) for value in polynomial_columns] for i in range(9)])
    if label == 'algebraic':
        operator = operator.applyfunc(lambda value:s.rem(s.expand(value),qr,r))
    cases.append({
        'label':label,
        'scope':'principal actualtorusorbit' if label=='principal' else 'both roots of12r^2+4r+3; identities modulo defining polynomial',
        'A':str(A),'B':str(B),'gamma_primitive':str(gamma),
        'full_curve_plus_first_jet_matrix_shape':list(matrix.shape),
        'full_curve_plus_first_jet_rank':28,
        'full_double_quartic_dimension':7,
        'quartic_basis':list(map(str,forms)),
        'h':list(map(str,h)), 'E':list(map(str,E)),
        'h_coefficient_matrix':[[str(value) for value in row] for row in H.tolist()],
        'E_coefficient_matrix':[[str(value) for value in row] for row in Err.tolist()],
        'complete_delta_operator':[[str(value) for value in row] for row in operator.tolist()],
        'necessary_two_quartic_condition':'rank of the complete9x7operator <=5; delta nonzero and theta normalized to1',
        'E_rank':5,'combined_hE_rank':7,
        'status':'EXACT COMPLETE LINEAR REDUCTION; no parameter-locus exhaustion asserted'
    })
    print('PASS:',label,'complete doublequartic space dim7; h inO8,E inO4; Emap ontoO4.')
record = {
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'ambient_monomials':list(map(str,monomials)),
    'scope':'e1,d2=4 primitive-obstruction-zero directions except excluded quadric; normalized global correction theta=1',
    'triple_equation':'delta*m+(delta*gamma_primitive+1)*y^2=0; containsquartic iff h=delta*E',
    'finite_flatness':'delta and delta*gamma_primitive+1 have no common zero; homogeneous infinity chart also retained',
    'open':'rankdrop parameterlocus and intrinsicVsplit/targetimage; no new direction family excluded',
    'cases':cases
}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print('OPEN: the linear-in-delta9x7 rank-drop incidence remains to be structurally resolved.')
