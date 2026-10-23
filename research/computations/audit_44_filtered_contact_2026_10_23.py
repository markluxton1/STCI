"""New independent exact audit of e0 open-orbit quartic (4,4) contact.
Builds direct Taylor evaluations at rational support points. No code or data imports.
"""
import sympy as S
z,y=S.symbols('z y')
x0,x1,x2,x3=S.symbols('x0 x1 x2 x3')
xs=(x0,x1,x2,x3)
mon=[]
for a in range(5):
 for b in range(5-a):
  for c in range(5-a-b):
   mon.append(x0**a*x1**b*x2**c*x3**(4-a-b-c))
assert len(mon)==35
f2=3/(8*z*(z+2))
path={x0:1,x1:z,x2:z**3+y,x3:z**4+(S.Rational(3,2)*z-1)*y+f2*y*y}
# These are actual derivatives of each ambient quartic along one fixed rational
# two-jet, unrelated to the source script's separate normal-coefficient matrix.
coeff=[]
for f in mon:
 e=S.Poly(S.expand(f.subs(path)),y)
 coeff.append([S.factor(e.coeff_monomial(y**j)) for j in range(4)])
# Evaluation constraints give a necessary subspace.  Full polynomial identity
# below proves its exactness.  No assumption that finite sampling proves zero.
rows=[]
for a in range(1,15):
 for j in range(3):
  rows.append([v[j].subs(z,a) for v in coeff])
prime=1009
Arows=[[int(c.p)*pow(int(c.q),-1,prime)%prime for c in row] for row in rows]
piv=[]
for col in range(35):
 k=next((i for i in range(len(piv),len(Arows)) if Arows[i][col]),None)
 if k is None: continue
 i=len(piv); Arows[i],Arows[k]=Arows[k],Arows[i]
 inv=pow(Arows[i][col],-1,prime)
 Arows[i]=[v*inv%prime for v in Arows[i]]
 for j in range(i+1,len(Arows)):
  c=Arows[j][col]
  if c: Arows[j]=[(a-c*b)%prime for a,b in zip(Arows[j],Arows[i])]
 piv.append(col)
assert len(piv)==33
q=x0*x3-x1*x2
A=x0*x0*x2-x1**3
B=x0*x2*x2-x1*x1*x3
D=x2**3-x1*x3*x3
forms=[-(x2+x3)*(16*A+(16*x0+8*x1)*q)+(4*x2+x3)*B-x2*x2*q,
 x2*D-256*x1*A-4*q*(64*x0*x1+16*x0*x2+4*x0*x3+32*x1*x1+4*x1*x2+4*x1*x3+2*x2*x2+x2*x3)]
N=[]
for f in forms:
 poly=S.Poly(S.expand(f),*xs)
 v=S.Matrix([poly.coeff_monomial(mm) for mm in mon])
 N.append(v)
 for j in range(3):
  assert S.cancel(sum(c*t[j] for c,t in zip(v,coeff)))==0
assert S.Matrix.hstack(*N).rank()==2
# Compute first normal derivative without reusing the source pencil.
normal={x0:1,x1:z,x2:z**3+y,x3:z**4+(S.Rational(3,2)*z-1)*y+S.Symbol('m')}
m=S.Symbol('m')
h=[]; third=[]
for v,f in zip(N,forms):
 e=S.Poly(S.expand(f.subs(normal)),m,y)
 h.append(S.factor(e.coeff_monomial(m)))
 third.append(S.factor(sum(c*t[3] for c,t in zip(v,coeff))))
assert S.factor(h[0])!=0 and S.factor(h[1])!=0
contact=S.factor(h[0]*third[1]-h[1]*third[0])
assert contact!=0
print('independent necessary evaluation rank modulo 1009', len(piv))
print('full rational-function contact identities: PASS')
print('cubic determinant',contact)
print('Generic contact for any independent pair is exactly three: PASS')
# Fresh arithmetic consequence of the displayed accepted e1 principal formulas.
p=4*z*z+2*z+1
h0=p*z**3/16
h1=p*(64*z**6+8*z**3+1)/1024
t0=(2*z+1)*(1536*z**5+1152*z**4+448*z**3+48*z**2-24*z+4)
t1=(2*z+1)*(1536*z**8+1152*z**7+448*z**6+240*z**5+120*z**4+60*z**3+30*z**2+15*z+8)
assert S.factor(h0*t1-h1*t0)==(2*z-1)**3*(2*z+1)*(4*z*z+2*z+1)/256
print('e1 principal cubic determinant: PASS')
