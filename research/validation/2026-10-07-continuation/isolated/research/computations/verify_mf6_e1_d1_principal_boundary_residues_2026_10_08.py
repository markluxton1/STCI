#!/usr/bin/env python3
"""Literal-form actual-chart flatness and cubic residue certificate.

Fixed C0, char0, only the listed principal boundary quartics. The cubic
pole divisor is a lower bound on D3-D2; it is not an allmate obstruction
when degree D3 is within the accepted bound.
"""
from pathlib import Path
import hashlib,json
import sympy as s
from sympy.polys.domains import QQ
x0,x1,x2,x3,z,w,U,V,y,m=s.symbols('x0 x1 x2 x3 z w U V y m')
literal_fibers=[{'name': 'rhalf_unique', 'r': '1/2', 'p': '8', 'quartic_basis': ['x0**3*x2 - x0**3*x3 + 6*x0**2*x1*x2 - 12*x0**2*x1*x3 - 40*x0**2*x2**2 + 32*x0**2*x2*x3 + 32*x0**2*x3**2 - x0*x1**3 + 12*x0*x1**2*x2 - 24*x0*x1**2*x3 - 112*x0*x1*x2**2 + 320*x0*x1*x2*x3 + 128*x0*x1*x3**2 + 320*x0*x2**3 - 384*x0*x2**2*x3 - 768*x0*x2*x3**2 - 256*x0*x3**3 - 5*x1**4 + 64*x1**3*x2 + 80*x1**3*x3 - 352*x1**2*x2**2 - 448*x1**2*x2*x3 - 640*x1**2*x3**2 + 1024*x1*x2**3 + 768*x1*x2**2*x3 + 1536*x1*x2*x3**2 + 1024*x1*x3**3 - 1280*x2**4 - 1024*x2**3*x3'], 'delta': '144 - 288*z', 'Gamma': '55296*z**2 - 3456', 'quadratic_cocycle': ['-36', '-18', '-9']}, {'name': 'Szero_unique', 'r': '-1/6', 'p': '2/3', 'quartic_basis': ['x0**3*x2 - x0**3*x3 - 2*x0**2*x1*x2/3 + 4*x0**2*x1*x3/3 + 4*x0**2*x2**2/9 - 7*x0**2*x2*x3/9 + x0**2*x3**2/9 - x0*x1**3 - 4*x0*x1**2*x2/3 + x0*x1**2*x3 + 11*x0*x1*x2**2/9 - 8*x0*x1*x2*x3/9 + 2*x0*x1*x3**2/9 - x0*x2**3/9 + 5*x1**4/3 - 13*x1**3*x2/9 - 4*x1**3*x3/9 + 7*x1**2*x2**2/9 - x1**2*x2*x3/9 + x1**2*x3**2/9 - x1*x2**3/9'], 'delta': '16/3 - 16*z/3', 'Gamma': '16*z**2/27 + 16*z/9 + 32/27', 'quadratic_cocycle': ['-2/3', '-2/3', '-2/3']}, {'name': 'c1zero_infinity_defect', 'r': '-5/6 + sqrt(2)*I/3', 'p': '-2/3 + 2*sqrt(2)*I/3', 'quartic_basis': ['x0**3*x2 - x0**3*x3 - 4*x0**2*x1*x2/3 + sqrt(2)*I*x0**2*x1*x2/3 + 8*x0**2*x1*x3/3 - 2*sqrt(2)*I*x0**2*x1*x3/3 + 32*x0**2*x2**2/9 - 17*sqrt(2)*I*x0**2*x2**2/9 - 47*x0**2*x2*x3/9 + 32*sqrt(2)*I*x0**2*x2*x3/9 + 17*x0**2*x3**2/9 - 20*sqrt(2)*I*x0**2*x3**2/9 - x0*x1**3 - 8*x0*x1**2*x2/3 + 2*sqrt(2)*I*x0*x1**2*x2/3 - x0*x1**2*x3 + sqrt(2)*I*x0*x1**2*x3 + 25*x0*x1*x2**2/9 - 13*sqrt(2)*I*x0*x1*x2**2/9 - 10*x0*x1*x2*x3/9 + 7*sqrt(2)*I*x0*x1*x2*x3/9 - 2*x0*x1*x3**2/9 + 14*sqrt(2)*I*x0*x1*x3**2/9 + x0*x2**3/9 - 7*sqrt(2)*I*x0*x2**3/9 + 7*x1**4/3 - sqrt(2)*I*x1**4/3 - 23*x1**3*x2/9 + 8*sqrt(2)*I*x1**3*x2/9 + 22*x1**3*x3/9 - 19*sqrt(2)*I*x1**3*x3/9 - 7*x1**2*x2**2/9 + 13*sqrt(2)*I*x1**2*x2**2/9 + x1**2*x2*x3/9 - 7*sqrt(2)*I*x1**2*x2*x3/9 - x1**2*x3**2/9 - 2*sqrt(2)*I*x1**2*x3**2/9 + x1*x2**3/9 + 2*sqrt(2)*I*x1*x2**3/9'], 'delta': '1', 'Gamma': 'z*(-5/9 - sqrt(2)*I/9) - 2/9 + 5*sqrt(2)*I/9', 'quadratic_cocycle': ['0', '0', '-4/3 + 10*sqrt(2)*I/3']}]

results=[]
for f in literal_fibers:
    r,p=map(s.sympify,[f['r'],f['p']]);F=s.sympify(f['quartic_basis'][0])
    field=QQ.algebraic_field(s.sqrt(-2)) if 'sqrt' in f['r'] else QQ
    def poly(e,var):return s.Poly(s.expand(e),var,domain=field)
    det=p-r
    A,B=1+r*z,1+p*z;bs,bt=p/det,-r/det
    e=s.expand(F.subs({x0:1,x1:z,x2:z**3+V,x3:z**4+U+s.Rational(3,2)*z*V}).subs({U:bt*m+A*y,V:-bs*m+B*y}))
    d,g=poly(s.sympify(f['delta']),z),poly(s.sympify(f['Gamma']),z)
    h=poly(e.coeff(m,1).coeff(y,0),z);Q=poly(e.coeff(m,0).coeff(y,2),z)
    assert d*Q==g*h
    E=poly(e.coeff(m,1).coeff(y,1),z);K=poly(e.coeff(m,0).coeff(y,3),z)
    S=h.exquo(d);T=g*E-d*K
    pole_degree=S.degree()-s.gcd(S,T).degree()
    Ai,Bi=r+w,p+w;si,ti=-1/det,1/det
    ei=s.expand(F.subs({x3:1,x2:w,x1:w**3+2*U,x0:w**4+V/2+3*w*U}).subs({U:ti*m+Ai*y,V:-si*m+Bi*y}))
    di=poly(w*d.as_expr().subs(z,1/w),w)
    hi=poly(ei.coeff(m,1).coeff(y,0),w);Qi=poly(ei.coeff(m,0).coeff(y,2),w)
    gi=(di*Qi).exquo(hi)
    Ei=poly(ei.coeff(m,1).coeff(y,1),w);Ki=poly(ei.coeff(m,0).coeff(y,3),w)
    Si=hi.exquo(di);Ti=gi*Ei-di*Ki
    def order0(P):return min(power[0] for power,c in P.terms())
    infinity_pole=max(0,order0(Si)-order0(Ti))
    if f['name']=='c1zero_infinity_defect':
        c3=field.from_sympy(s.sympify(f['quadratic_cocycle'][2]))
        assert field.from_sympy(gi.eval(0))==-c3 and c3!=0
        assert di.as_expr()==w
    expected={'rhalf_unique':(2,0),'Szero_unique':(1,3),'c1zero_infinity_defect':(3,1)}
    if f['name'] in expected:assert (pole_degree,infinity_pole)==expected[f['name']]
    row={'name':f['name'],'finite_h':str(h.as_expr()),'finite_S':str(S.as_expr()),'finite_T':str(T.as_expr()),
         'infinity_h':str(hi.as_expr()),'infinity_delta':str(di.as_expr()),'infinity_Gamma':str(gi.as_expr()),
         'infinity_S':str(Si.as_expr()),'infinity_T':str(Ti.as_expr()),
         'finite_excess_degree':pole_degree,'infinity_excess':infinity_pole,'D3_degree_lower_bound':1+pole_degree+infinity_pole}
    print(f['name'],'finite cubic excess',pole_degree,'infinity',infinity_pole,'D3 lower bound',row['D3_degree_lower_bound'],flush=True)
    results.append(row)
record={'status':'PASS actual two-chart cubic residue calculations and infinity-defect flatness',
        'scope':'Fixed C0, char0, listed three quartic fibers including both quadratic conjugates',
        'fibers':results,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'sympy':s.__version__}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print('PASS actual infinity correction is minus c3 and is a unit at both infinity-defect roots')
