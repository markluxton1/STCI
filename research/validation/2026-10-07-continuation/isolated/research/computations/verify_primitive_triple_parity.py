#!/usr/bin/env python3
"""Exact entire parity slice of e=2 primitive-triple quartic compatibility."""
from pathlib import Path
import importlib.util,itertools,json
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import QQ

ROOT=Path(__file__).resolve().parents[2]
SCRATCH=ROOT/'research'/'scratch'/'primitive47universal'

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj

def main():
    generator=module('general_triple_contact',SCRATCH/'general_triple_contact.py')
    generator.main()
    data=json.loads((SCRATCH/'general_triple_contact.json').read_text())
    a0,a1,a2,b0,b1,b2,b=sp.symbols('a0 a1 a2 b0 b1 b2 b')
    parity={a0:1,a1:0,a2:1,b0:0,b1:b,b2:0}
    originalrows=data['symbolmatrix']+data['jetmatrix'][:7]
    M=sp.Matrix([[sp.sympify(c).subs(parity) for c in row] for row in originalrows])
    M=M[[i for i in range(M.rows) if any(M.row(i))],:]
    assert M.shape==(10,9)
    minors=[];gcd=sp.Integer(0)
    for rows in itertools.combinations(range(10),9):
        # Polynomial-domain determinant avoids expensive generic Expr
        # simplification and does exact coefficient arithmetic over QQ[b].
        polynomial=DomainMatrix.from_Matrix(M.extract(rows,range(9))).convert_to(QQ.poly_ring(b)).det().as_expr()
        minors.append(sp.factor(polynomial));gcd=sp.gcd(gcd,polynomial)
    gcd=sp.Poly(gcd,b).monic().as_expr()
    assert sp.factor(gcd)==(b-6)*(b+2)**9*(b+6)**2
    assert M.subs(b,-2).rank()==5
    assert M.subs(b,-6).rank()==8 and M.subs(b,6).rank()==8
    D=sp.sympify(data['resultant']).subs(parity)
    assert sp.expand(D)==b**2

    x,y,Z,W=sp.symbols('x y Z W')
    expected={6:6*x*W*y**2-x**2*y*Z-4*x**2*Z**2+y**4-2*y**3*Z,
              -6:-(8*x*W**3+6*x*W*y*Z+12*x*W*Z**2+x**2*Z**2-y**3*Z-6*y**2*Z**2-12*y*Z**3-8*Z**4)/6}
    old=module('original_fourth_obstruction',ROOT/'research'/'scratch'/'primitive47'/'obstruction.py')
    classes={-6:[64,0,-8,0,0],6:[-128,0,160,0,-192]}
    hankel_determinants={-6:512,6:-163840}
    output={'parameter':'A=1+z^2, B=b*z, b!=0',
            'minor_gcd':str(sp.factor(gcd)),'maximal_minors':[str(p) for p in minors],
            'special_directions':{}}
    for value in [-6,6]:
        null=M.subs(b,value).nullspace()
        assert len(null)==1
        coefficients=sp.Matrix([[sp.sympify(c).subs(parity).subs(b,value) for c in lift] for lift in data['lifts']]).T*null[0]
        F=sp.expand(sum(c*x**i*y**j*Z**k*W**l for c,(i,j,k,l) in zip(coefficients,data['monomials'])))
        assert sp.expand(F-expected[value])==0
        c=old.obstruction(1+old.z**2,value*old.z)[3]
        assert c==classes[value]
        H=sp.Matrix([[c[0],c[1],c[2]],[c[1],c[2],c[3]],[c[2],c[3],c[4]]])
        assert H.det()==hankel_determinants[value] and H.rank()==3
        output['special_directions'][str(value)]={'quartic':str(F),'fourth_obstruction':list(map(str,c)),
                                                  'hankel_determinant':str(H.det())}
    (SCRATCH/'parity_triple_certificate.json').write_text(json.dumps(output,indent=2)+'\n')
    print('ENTIRE PRIMITIVE-TRIPLE PARITY SLICE VERIFIED: b=-2,-6,6 ONLY')
    print('b=-2: cubic times linear carriers; b=+-6: fourth classes have no degree-two annihilator')

if __name__=='__main__':main()
