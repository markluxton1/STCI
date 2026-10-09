#!/usr/bin/env python3
"""Independent small principal-chart frame/coverage checks; no norm replay.

Reconstructs the first-normal matrix from actual quartics, verifies the
eleven-column pivot, and independently covers all excluded parameter
factors. Full cofactor/resultant and boundary rank replays remain separate.
"""
from pathlib import Path
import hashlib,json
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import QQ

ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
input_path=ROOT/'research/scratch/session-mf6-e1-principal-contact-2026-10-08.json'
j=json.loads(input_path.read_text())
p,r,z,U,V,y,m,b=s.symbols('p r z U V y m b')
x0,x1,x2,x3=s.symbols('x0 x1 x2 x3');xs=(x0,x1,x2,x3)
H=s.sympify(j['H']);P=2*p+12*r*r+16*r+9
T=2*p-4*r*r-4*r-1;S=p-2*r-1;Q=12*r*r+20*r+11
forms=list(map(s.sympify,j['I4']))
mon=[x0**i*x1**jj*x2**kk*x3**(4-i-jj-kk)
     for i in range(4,-1,-1) for jj in range(4-i,-1,-1)
     for kk in range(4-i-jj,-1,-1)]
assert len(set(mon))==35 and len(forms)==18
assert sorted(set(s.degree(mm.subs({x0:1,x1:z,x2:z**3,x3:z**4}),z) for mm in mon))==list(range(17))
assert s.Matrix([[s.Poly(f,*xs).coeff_monomial(mm) for f in forms] for mm in mon]).rank()==18
assert all(s.expand(f.subs({x0:1,x1:z,x2:z**3,x3:z**4}))==0 for f in forms)
chart={x0:1,x1:z,x2:z**3+V,x3:z**4+U+s.Rational(3,2)*z*V}
A,B=1+r*z,1+p*z
jets=[s.expand(f.subs(chart).subs({U:-r*m/(p-r)+A*y,V:-p*m/(p-r)+B*y})) for f in forms]
first=[s.expand(f.coeff(m,0).coeff(y,1)) for f in jets]
M1=s.Matrix([[f.coeff(z,i) for f in first] for i in range(11)])
assert M1==s.Matrix([[s.sympify(e) for e in row] for row in j['M1']])
cols=[0,1,2,3,4,5,6,11,12,14,15]
D=p**4*(p-r)*(2*r-1)*T*T/256
det=DomainMatrix.from_Matrix(M1[:,cols]).convert_to(QQ.poly_ring(p,r)).det().as_expr()
assert s.expand(det-D)==0
N=s.Matrix([[s.sympify(e) for e in row] for row in j['first_kernel']])
assert N.shape==(18,7)
assert (M1*N).applyfunc(s.cancel)==s.zeros(11,7)
free_rows=[7,8,9,10,13,16,17]
assert (N[free_rows,:]+D*s.eye(7)).applyfunc(s.expand)==s.zeros(7,7)

# Cover the exact complement rather than treating removed factors as units.
assert s.expand(H.subs(p,-6*r*r-8*r-s.Rational(9,2))+9*(2*r+1)**2*Q**2)==0
assert s.expand(H.subs(p,2*r*r+2*r+s.Rational(1,2))+9*(2*r-1)**2*(2*r+1)**4)==0
assert s.expand(H.subs(r,s.Rational(1,2))-8*(p-8)*(p-2)**2)==0
assert s.expand(H.subs(r,-s.Rational(1,2))-8*p*(p+2)**2)==0
assert s.expand(H.subs(p,2*r+1)+(2*r-1)**2*(2*r+1)*(6*r+1)*Q)==0
assert s.expand(P.subs(p,2*r+1)-Q)==0
assert s.discriminant(Q,r)==-128
assert s.rem(P.subs(p,2*r+1),Q,r)==0

h2=s.expand(-(2*A+z*B)*(12*A*A+3*z*z*B*B+4*z*z*(s.diff(A,z)*B-A*s.diff(B,z)))/(8*z**5))
c=[s.factor(h2.coeff(z,-i)) for i in (1,2,3)]
assert s.expand(64*(c[0]*c[2]-c[1]**2)-H)==0
primitive={p:-2,r:-s.Rational(1,2)}
assert all(v.subs(primitive)==0 for v in c)
assert all(s.rem(v.subs(p,2*r+1),Q,r)==0 for v in c[:2])
c3=s.rem(c[2].subs(p,2*r+1),Q,r)
assert s.gcd(c3,Q)==1
# Opposite-chart correction constant is -c3; its norm is exactly 24.
rr=(-5+2*s.sqrt(-2))/6;constant=s.simplify(-c3.subs(r,rr))
assert s.simplify(constant*s.conjugate(constant))==24

# Homogenize invariant H with weights wt(p)=2, wt(r)=wt(b)=1.
weighted=s.Add(*[coeff*p**i*r**jj*b**(6-2*i-jj)
                for (i,jj),coeff in s.Poly(H,p,r).terms()])
assert all(6-2*i-jj>=0 for (i,jj),coeff in s.Poly(H,p,r).terms())
cubic=p**3-8*p*p+12*p-72
assert s.expand(weighted.subs({b:0,r:1})-8*cubic)==0
assert s.expand(weighted.subs({b:0,r:0})-8*p**3)==0
mod5=[int(cubic.subs(p,v))%5 for v in range(5)]
assert all(mod5) # cubic modulo5 has no root, hence is irreducible
assert s.discriminant(cubic,p)==-160704

point={p:s.Rational(2,3),r:-s.Rational(1,6)}
assert H.subs(point)==0 and s.prod((p,P,p-r,2*r-1,T)).subs(point)!=0
M2=s.Matrix([[s.sympify(e) for e in row] for row in j['M2']])
assert M1.col_join(M2).subs(point).rank()==17

result={'scope':'Independent complete ambient first-frame and parameter-complement countercheck; full norm and boundary replays separate',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'input_sha256':{str(input_path.relative_to(ROOT)):hashlib.sha256(input_path.read_bytes()).hexdigest()},
 'M1_pivot_columns':cols,'M1_pivot_determinant':str(s.factor(det)),
 'raw_kernel_free_rows':free_rows,'raw_kernel_free_diagonal':str(-D),
 'complement_P_zero':'r=-1/2 primitive point or Q roots with p=2r+1',
 'complement_T_zero':'r=+/-1/2; retained genuine rhalf points p2,p8',
 'c1zero_infinity_correction_norm':24,
 'b0zero_cubic_mod5_values':mod5,'b0zero_cubic_irreducible':True,
 'retained_S_zero_point_rank_in_I4':17,
 'not_claimed':'No all-mate STCI exclusion; actual boundary ranks supplied by separate complete35 sources'}
(OUT/'coverage-countercheck-result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
