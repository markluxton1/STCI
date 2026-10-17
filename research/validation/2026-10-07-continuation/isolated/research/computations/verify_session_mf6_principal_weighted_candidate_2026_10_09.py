"""Exact polynomial carrier syzygies and a nonzero finite STCI candidate.

The candidate is the fixed degree-7/degree-7 binary-gradient resultant of
an actual first-normal octic, preserved as a 14x14 Sylvester determinant.
No expanded discriminant, exact exception list, or all-mate exclusion is
claimed. Its weighted degree210 gives at most630 distinct principal
parameter points on H=0, using the ordinary-plane double cover.
"""
from pathlib import Path
import hashlib,json,time
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import GF
BEGIN=time.monotonic();HERE=Path(__file__).resolve();ROOT=HERE.parents[1];SCRATCH=ROOT/'scratch'
paths={name:SCRATCH/name for name in ('derive-mf6-principal-weighted-kernel-2026-10-08.json','mf6-principal-weighted-kernel-2026-10-08.json','session-mf6-e1-principal-contact-2026-10-08.json')}
contact=json.loads(paths['derive-mf6-principal-weighted-kernel-2026-10-08.json'].read_text());kernel=json.loads(paths['mf6-principal-weighted-kernel-2026-10-08.json'].read_text());old=json.loads(paths['session-mf6-e1-principal-contact-2026-10-08.json'].read_text())
p,r,b,z=s.symbols('p r b z');x0,x1,x2,x3=s.symbols('x0 x1 x2 x3');xs=(x0,x1,x2,x3)
H=s.sympify(contact['H']);assert s.expand(H-s.sympify(kernel['H']))==0
assert s.expand(H.subs(b,1)-s.sympify(old['H']))==0
assert all(2*pp+rr+bb==6 for (pp,rr,bb),cc in s.Poly(H,p,r,b).terms())
forms=list(map(s.sympify,kernel['forms']));assert kernel['forms']==contact['forms']==old['I4'] and len(forms)==18
mon=[x0**i*x1**j*x2**k*x3**(4-i-j-k) for i in range(4,-1,-1) for j in range(4-i,-1,-1) for k in range(4-i-j,-1,-1)]
assert len(mon)==35
assert all(s.expand(f.subs({x0:1,x1:z,x2:z**3,x3:z**4}))==0 for f in forms)
assert s.Matrix([[s.Poly(f,*xs).coeff_monomial(mm) for f in forms] for mm in mon]).rank()==18
assert sorted(set(s.degree(mm.subs({x0:1,x1:z,x2:z**3,x3:z**4}),z) for mm in mon))==list(range(17))
M1=s.Matrix([[s.sympify(e) for e in row] for row in contact['first']]);M2=s.Matrix([[s.sympify(e) for e in row] for row in contact['second']])
assert M1.subs(b,1)==s.Matrix([[s.sympify(e) for e in row] for row in old['M1']])
assert M2.subs(b,1)==s.Matrix([[s.sympify(e) for e in row] for row in old['M2']])
M=M1.col_join(M2);assert M.shape==(23,18)
for i in range(M.rows):
 for j in range(M.cols):
  assert all(2*pp+rr+bb==contact['row_weights'][i]-contact['column_weights'][j] for (pp,rr,bb),cc in s.Poly(M[i,j],p,r,b).terms() if cc)
assert contact['column_weights']==[1,0,2,3,4,5,6,1,3,4,5,6,7,7,8,9,9,10]
columns=[[s.sympify(e) for e in col] for col in kernel['kernel_columns']]
assert kernel['generator_degrees']==[9,9,10]
for j,(col,degree) in enumerate(zip(columns,(9,9,10))):
 assert len(col)==18 and any(e!=0 for e in col)
 for i,e in enumerate(col):
  assert all(2*pp+rr+bb==degree+contact['column_weights'][i] for (pp,rr,bb),cc in s.Poly(e,p,r,b).terms() if cc)
 for i in range(M.rows):
  assert s.rem(s.expand(sum(M[i,k]*col[k] for k in range(18))),H,p)==0
 print('PASS exact weighted polynomial contact syzygy',j,'degree',degree,flush=True)
# Actual m coefficient in the balanced frame U=-r*m/(p-rb)+A*y,
# V=-p*m/(p-rb)+B*y. Multiplying by p-rb gives the polynomial hhat.
# Derivatives are evaluated on actual C0, without forming the whole F.
h_parts=[]
for f in forms:
 fu=s.diff(f,x3).subs({x0:1,x1:z,x2:z**3,x3:z**4})
 fv=(s.diff(f,x2)+s.Rational(3,2)*z*s.diff(f,x3)).subs({x0:1,x1:z,x2:z**3,x3:z**4})
 h_parts.append(s.expand(-r*fu-p*fv))
first=columns[0]
hraw=s.expand(sum(c*h for c,h in zip(first,h_parts)))
hcoeff=[s.expand(s.rem(hraw.coeff(z,j),H,p)) for j in range(9)]
assert s.rem(hraw-sum(c*z**j for j,c in enumerate(hcoeff)),H,p)==0
assert all(s.rem(hraw.coeff(z,j),H,p)==0 for j in range(9,s.degree(hraw,z)+1))
for j,c in enumerate(hcoeff):
 assert all(2*pp+rr+bb==11+j for (pp,rr,bb),cc in s.Poly(c,p,r,b).terms() if cc)
h=s.Add(*[c*z**j for j,c in enumerate(hcoeff)])
# Fixed-degree binary gradients. Padding to degree7 retains a multiple
# infinity root, unlike a parameter-specialized univariate discriminant.
a=[(8-j)*hcoeff[j] for j in range(8)]
d=[(j+1)*hcoeff[j+1] for j in range(8)]
sylv=s.zeros(14,14)
for i in range(7):
 for j,c in enumerate(reversed(a)):sylv[i,i+j]=c
 for j,c in enumerate(reversed(d)):sylv[7+i,i+j]=c
row_weights=[18+i for i in range(7)]+[19+i for i in range(7)]
assert sum(row_weights)-sum(range(14))==210
for i in range(14):
 for j in range(14):
  assert all(2*pp+rr+bb==row_weights[i]-j for (pp,rr,bb),cc in s.Poly(sylv[i,j],p,r,b).terms() if cc)
# An exact modular certificate of nonzero restriction to the integral
# sextic H. Every input denominator is a power of2 and101 is invertible.
for c in list(sylv):
 for cc in s.Poly(c,p,r,b).coeffs():
  denominator=int(s.denom(cc));assert denominator & (denominator-1)==0
ell=101;point={p:4,r:2,b:1}
assert int(H.subs(point))%ell==0
P=2*p+12*r*r+16*r*b+9*b*b;T=2*p-4*r*r-4*r*b-b*b
assert int((p*P*(p-r*b)*(2*r-b)*T).subs(point))%ell!=0
def reduce_rational(cc):
 cc=s.Rational(cc);return int(s.numer(cc))*pow(int(s.denom(cc)),-1,ell)%ell
sample=sylv.subs(point).applyfunc(reduce_rational)
determinant=int(DomainMatrix.from_Matrix(sample).convert_to(GF(ell)).det())%ell
assert determinant!=0
sample_h=s.Poly(sum(reduce_rational(c.subs(point))*z**j for j,c in enumerate(hcoeff)),z,modulus=ell)
assert sample_h.degree()==8 and s.gcd(sample_h,sample_h.diff()).degree()==0
print('PASS fixed14x14 Sylvester determinant is nonzero on H mod101:',determinant,flush=True)
result={
 'status':'PASS exact syzygies and nonzero homogeneous binary-octic candidate',
 'scope':'principal e1,d2=1 good contact open; candidate is necessary for a nonnormal carrier with an STCI mate, conditional on singleton-fiber lemma',
 'not_claimed':'Exact nonnormal parameter subset, complete candidate-factor analysis, or existence/nonexistence of mates at candidate zeros',
 'H':str(H),'parameter_weights':{'p':2,'r':1,'b':1},
 'source_sha256':hashlib.sha256(HERE.read_bytes()).hexdigest(),
 'input_sha256':{name:hashlib.sha256(path.read_bytes()).hexdigest() for name,path in paths.items()},
 'generator_degrees':[9,9,10],
 'first_normal_polynomial_convention':'hhat=(p-rb)*coefficient(m) of generator0 in actual balanced chart; binary hhat=sum(h_j*s^(8-j)*t^j)',
 'h_coefficient_vector':list(map(str,hcoeff)),
 'binary_gradient_s_coefficients':list(map(str,a)),
 'binary_gradient_t_coefficients':list(map(str,d)),
 'candidate_polynomial':'Delta=det(fixed14x14Sylvester(partial_s hhat,partial_t hhat)); full determinant not expanded',
 'sylvester_matrix':[[str(sylv[i,j]) for j in range(14)] for i in range(14)],
 'candidate_weighted_degree':210,'maximum_distinct_principal_parameter_candidates':630,
 'bound_justification':'Pullback p=a^2 to ordinary P2 gives degree6 and210 curves, no common component; Bezout1260 andtwo distinct lifts overp!=0.',
 'modular_nonzero_certificate':{'prime':ell,'p':4,'r':2,'b':1,'fixed_sylvester_determinant':determinant,'octic_gcd_with_derivative_degree':0},
 'elapsed_seconds':round(time.monotonic()-BEGIN,3)}
output=SCRATCH/'session-mf6-principal-weighted-candidate-2026-10-09.json';output.write_text(json.dumps(result,indent=2)+'\n')
print('PASS saved exact determinant candidate, degree210, atmost630 principal points',flush=True)
