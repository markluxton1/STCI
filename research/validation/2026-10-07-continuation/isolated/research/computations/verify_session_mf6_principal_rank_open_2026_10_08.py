"""Exact audit: principal e=1,d2=1 quartic space has dimension one on U.

U is H=0, p*P*(p-r)*(2r-1)*T !=0. All exceptional complement fibers
remain separate. This is a quartic-containment result, not a mate exclusion.
The audit reconstructs the ambient first/second normal maps from quartics,
checks the complete seven-column frame, and certifies its contact rank using
factored raw cofactors, two resultants, and the retained S=0 fiber.
"""
from pathlib import Path
import hashlib,json,time
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import QQ
START=time.monotonic();HERE=Path(__file__).resolve();ROOT=HERE.parents[1]
SCRATCH=ROOT/'scratch'
inputs={name:SCRATCH/name for name in (
 'session-mf6-e1-principal-contact-2026-10-08.json',
 'session-mf6-e1-principal-minors-2026-10-08.json',
 'audit-mf6-e1-principal-raw-minors-2026-10-08.json')}
j=json.loads(inputs['session-mf6-e1-principal-contact-2026-10-08.json'].read_text())
k=json.loads(inputs['session-mf6-e1-principal-minors-2026-10-08.json'].read_text())
a=json.loads(inputs['audit-mf6-e1-principal-raw-minors-2026-10-08.json'].read_text())
p,r,z,U,V,y,m=s.symbols('p r z U V y m')
x0,x1,x2,x3=s.symbols('x0 x1 x2 x3');xs=(x0,x1,x2,x3)
H=s.sympify(j['H']);P=2*p+12*r*r+16*r+9
T=2*p-4*r*r-4*r-1;S=p-2*r-1;Q=12*r*r+20*r+11
assert H==s.sympify(k['H'])==s.sympify(a['H'])
forms=list(map(s.sympify,j['I4']))
mon=[x0**i*x1**jj*x2**kk*x3**(4-i-jj-kk)
     for i in range(4,-1,-1) for jj in range(4-i,-1,-1)
     for kk in range(4-i-jj,-1,-1)]
assert len(mon)==35 and len(forms)==18
assert all(s.expand(f.subs({x0:1,x1:z,x2:z**3,x3:z**4}))==0 for f in forms)
ambient=s.Matrix([[s.Poly(f,*xs).coeff_monomial(mm) for f in forms] for mm in mon])
assert ambient.rank()==18
# The parametrized quartic has Hilbert function 17 in degree four:
# the exponent sums comprise every integer from 0 through 16.
assert sorted(set(s.degree(mm.subs({x0:1,x1:z,x2:z**3,x3:z**4}),z) for mm in mon))==list(range(17))
A,B=1+r*z,1+p*z;bs,bt=p/(p-r),-r/(p-r)
h2=s.expand(-(2*A+z*B)*(12*A*A+3*z*z*B*B+4*z*z*(s.diff(A,z)*B-A*s.diff(B,z)))/(8*z**5))
c1,c2,c3=[h2.coeff(z,-i) for i in (1,2,3)]
assert s.expand(64*(c1*c3-c2*c2)-H)==0
delta=s.expand(-8*c2+8*c1*z)
assert s.expand(delta-((2*r+1)*(8*p+12*r*r+4*r+3)-p*P*z))==0
Gamma=s.Add(*[s.expand(delta*h2).coeff(z,i)*z**i for i in range(3)])
assert s.expand(delta-s.sympify(j['delta']))==0
assert s.expand(Gamma-s.sympify(j['Gamma']))==0
assert s.factor(s.resultant(delta,Gamma,z)-p**4*P**4/8)==0
chart={x0:1,x1:z,x2:z**3+V,x3:z**4+U+s.Rational(3,2)*z*V}
jet=[s.expand(f.subs(chart).subs({U:bt*m+A*y,V:-bs*m+B*y})) for f in forms]
first=[s.expand(f.coeff(m,0).coeff(y,1)) for f in jet]
second=[s.cancel((p-r)*(delta*f.coeff(m,0).coeff(y,2)-Gamma*f.coeff(m,1).coeff(y,0))) for f in jet]
def coefficient_rows(polys):
 degree=max(s.degree(f,z) if f else 0 for f in polys)
 return s.Matrix([[s.expand(f).coeff(z,i) for f in polys] for i in range(degree+1)])
M1,M2=coefficient_rows(first),coefficient_rows(second)
assert M1==s.Matrix([[s.sympify(e) for e in row] for row in j['M1']])
assert M2==s.Matrix([[s.sympify(e) for e in row] for row in j['M2']])
assert M1.shape==(11,18)
pivot_cols=(0,1,2,3,4,5,6,11,12,14,15)
pivot_det=DomainMatrix.from_Matrix(M1[:,pivot_cols]).convert_to(QQ.poly_ring(p,r)).det().as_expr()
assert s.expand(pivot_det-p**4*(p-r)*(2*r-1)*T*T/256)==0
N=s.Matrix([[s.sympify(e) for e in row] for row in j['first_kernel']])
assert N.shape==(18,7) and (M1*N).applyfunc(s.cancel)==s.zeros(11,7)
column_divisors=list(map(s.sympify,k['first_frame_column_divisors']))
for col,divisor in enumerate(column_divisors):
 assert s.factor(s.gcd_list(list(N[:,col]))-divisor)==0
 N[:,col]=N[:,col].applyfunc(lambda e:s.cancel(e/divisor))
free_rows=(7,8,9,10,13,16,17)
free=N[list(free_rows),:]
assert all(free[i,jj]==0 for i in range(7) for jj in range(7) if i!=jj)
assert s.factor(free.det())!=0
# Every displayed diagonal factor is a unit on the stated U.
assert s.factor(free.det())== -p**8*(2*r-1)**6*T**11/2**52
contact=(M2*N).applyfunc(s.cancel)
assert all(e==0 for e in contact[7:,:])
assert all(s.rem(e,H,p)==0 for e in contact[6,:])
D=contact[:6,:]
row_units=list(map(s.sympify,k['contact_row_units']))
for row,unit in enumerate(row_units):
 for col in range(7):D[row,col]=s.cancel(D[row,col]/unit)
assert all(not s.denom(e).free_symbols for e in D)
assert all(s.rem(D[i,jj]-s.sympify(k['contact_6x7'][i][jj]),H,p)==0 for i in range(6) for jj in range(7))
print('PASS reconstructed all quartics, first-normal rank11, complete seven-frame and contact map',flush=True)
# Raw cofactors are factored BEFORE any H reduction. This preserves small
# residuals and gives an exact identity for each actual determinant.
raw=[];residual={};factor_metadata=[]
for record in a['minors']:
 omitted=record['omitted'];minor=D[:,[i for i in range(7) if i!=omitted]]
 determinant=DomainMatrix.from_Matrix(minor).convert_to(QQ.poly_ring(p,r)).det().as_expr()
 factors=[(s.sympify(f),n) for f,n in record['factors']]
 represented=s.sympify(record['coefficient'])*s.prod(f**n for f,n in factors)
 assert s.expand(determinant-represented)==0
 assert s.expand(s.rem(determinant,H,p)-s.sympify(k['seven_cofactor_remainders'][omitted]))==0
 raw.append((omitted,determinant))
 residual[omitted]=factors[-1][0]
 factor_metadata.append({'omitted':omitted,'factors':record['factors'],'coefficient':record['coefficient']})
print('PASS all seven actual raw cofactor factorizations and saved remainder identities',flush=True)
# Extra factor (2r+1) is a unit on pP-open, with both excluded roots retained.
assert s.factor(H.subs(r,-s.Rational(1,2)))==8*p*(p+2)**2
assert s.expand(P.subs(r,-s.Rational(1,2))-2*(p+2))==0
# Away from S=0, cofactor6 and cofactor5 prefactors are units. Their
# residual common zeros can lie only above the gcd of the two norms.
R6,R5=residual[6],residual[5]
q6,q5=s.resultant(H,R6,p),s.resultant(H,R5,p)
gcd=s.Poly(s.gcd(q6,q5),r,domain=QQ).monic().as_expr()
expected=s.Poly((2*r-1)**16*(2*r+1)**26*Q**5,r,domain=QQ).monic().as_expr()
assert s.expand(gcd-expected)==0
# Exact Euclidean fiber computation over one quadratic embedding; the
# conjugate embedding is covered by field conjugation over QQ.
i=s.sqrt(-2);rr=(-5+2*i)/6;K=QQ.algebraic_field(i)
field_polys=[s.Poly(s.rem(f,Q,r).subs(r,rr),p,domain=K) for f in (H,R6,R5)]
fH,f6,f5=field_polys
fiber_gcd=fH.gcd(f6).gcd(f5).monic()
assert s.expand(fiber_gcd.as_expr()-(p-(2*rr+1)))==0
u,v,g=s.gcdex(fH,f6)
assert u*fH+v*f6==g
assert g.monic()==fiber_gcd
assert f5.rem(fiber_gcd).is_zero
assert s.simplify(P.subs({r:rr,p:2*rr+1}))==0
print('PASS two resultants leave only P=0 quadratic fibers outside r=+/-1/2',flush=True)
# S is NOT a unit. Handle its full remaining fiber rather than silently
# cancelling the S^3 prefactor in cofactors6,5.
assert s.factor(H.subs(p,2*r+1))==-(2*r-1)**2*(2*r+1)*(6*r+1)*Q
assert s.expand(P.subs(p,2*r+1)-Q)==0
point={r:-s.Rational(1,6),p:s.Rational(2,3)}
assert H.subs(point)==0 and s.prod((p,P,p-r,2*r-1,T)).subs(point)!=0
fiber=D.subs(point)
cofactor4=fiber[:,[i for i in range(7) if i!=4]].det()
assert cofactor4==s.Rational(1073741824,36472996377170786403)
assert fiber.rank()==6
print('PASS retained S=0 fiber has a nonzero actual cofactor4',flush=True)
result={
 'status':'PASS',
 'scope':'Fixed C0, characteristic zero; H=0 and pP(p-r)(2r-1)T !=0; quartic dimension exactly one',
 'not_claimed':'Mate exclusion, global principal-lane exclusion, or exhausted chart complement',
 'source_sha256':hashlib.sha256(HERE.read_bytes()).hexdigest(),
 'input_sha256':{name:hashlib.sha256(path.read_bytes()).hexdigest() for name,path in inputs.items()},
 'first_normal_pivot_columns':list(pivot_cols),'first_normal_pivot_determinant':str(s.factor(pivot_det)),
 'kernel_free_rows':list(free_rows),'kernel_free_determinant':str(s.factor(free.det())),
 'cofactor_factorizations':factor_metadata,
 'resultant6_factors':[[str(f),int(n)] for f,n in s.factor_list(q6)[1]],
 'resultant5_factors':[[str(f),int(n)] for f,n in s.factor_list(q5)[1]],
 'resultant_gcd_monic':str(gcd),'quadratic_fiber_gcd':str(fiber_gcd.as_expr()),
 'retained_S_zero_point':{'r':'-1/6','p':'2/3','cofactor4':str(cofactor4)},
 'elapsed_seconds':round(time.monotonic()-START,3)}
output=ROOT/'scratch/session-mf6-principal-rank-open-audit-2026-10-08.json'
output.write_text(json.dumps(result,indent=2)+'\n')
print('PASS complete declared open has contact rank6, ambient quartic kernel dimension1',flush=True)
