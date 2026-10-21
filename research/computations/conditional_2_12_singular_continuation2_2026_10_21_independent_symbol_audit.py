from fractions import Fraction as Q
N=11;zero=(0,)*N
class P:
 def __init__(self,d=None):self.d={m:c for m,c in (d or {}).items() if c}
 def __add__(self,b):
  b=cast(b);d=self.d.copy()
  for m,c in b.d.items():d[m]=d.get(m,Q(0))+c
  return P(d)
 __radd__=__add__
 def __neg__(self):return P({m:-c for m,c in self.d.items()})
 def __sub__(self,b):return self+-cast(b)
 def __rsub__(self,b):return cast(b)+-self
 def __mul__(self,b):
  b=cast(b);d={}
  for m,c in self.d.items():
   for n,e in b.d.items():
    k=tuple(a+b for a,b in zip(m,n));d[k]=d.get(k,Q(0))+c*e
  return P(d)
 __rmul__=__mul__
 def __pow__(self,n):
  o=cast(1)
  for _ in range(n):o=o*self
  return o
 def __eq__(self,b):return self.d==cast(b).d
 def coeff(self,u,v,z):
  return P({(0,0,0)+m[3:]:c for m,c in self.d.items() if m[:3]==(u,v,z)})
def cast(x):return x if isinstance(x,P) else P({zero:Q(x)})
def var(i):
 m=list(zero);m[i]=1;return P({tuple(m):Q(1)})
u,v,z,A1,B1,C1,D1,A2,B2,C2,D2=[var(i) for i in range(N)]
q=u+Q(1,2)*z*v

def factor(A,B,C,D):
 d=D-Q(1,2)*A;e=Q(-1,2)*C
 al=B**2-B*d*z+(d**2-B*e)*z**2-d*e*z**3+e**2*z**4
 li=(A+C*z)*u+(B+D*z)*v
 p=al*li;k=(A+2*D)*(d**2+Q(1,2)*B*C)
 b=-A*d**2+B*C*(D-A)
 r=A*B**2+(C*B**2-A*B*d)*z+(-A*d*e+C*(d**2-B*e))*z**3+(A*e**2-C*d*e)*z**4
 c=q*r+B**3*v+b*(-z**2*u+Q(1,2)*z**3*v)+Q(-1,8)*C**3*(-2*z**5*u)
 assert p-c==Q(1,2)*k*z**3*v
 return p,k,b
p1,k1,b1=factor(A1,B1,C1,D1);p2,k2,b2=factor(A2,B2,C2,D2)
p=p1*p2
Pj=[p.coeff(2,0,j) for j in range(11)]
Qj=[p.coeff(1,1,j) for j in range(11)]
Rj=[p.coeff(0,2,j) for j in range(11)]
L=[Pj[9]-2*Qj[10],Qj[0]-2*Rj[1],Pj[0]-2*Qj[1]+4*Rj[2],3*Pj[1]-2*Qj[2]-4*Rj[3],Pj[2]-2*Qj[3]+4*Rj[4],Pj[3]-2*Qj[4]+4*Rj[5],Pj[4]-4*Rj[6],Pj[5]-2*Qj[6]+4*Rj[7],Pj[6]-2*Qj[7]+4*Rj[8],Pj[7]+2*Qj[8]-12*Rj[9],Pj[8]-2*Qj[9]+4*Rj[10]]
expected=[cast(0) for _ in range(11)]
expected[3]=-2*(k1*B2**3+k2*B1**3)
expected[6]=-(k1*b2+k2*b1+k1*k2)
expected[9]=Q(1,4)*(k1*C2**3+k2*C1**3)
assert L==expected
print('FACTOR_CANONICAL_CUBIC_DEFECT_IDENTITIES: PASS')
print('ALL_ELEVEN_GLOBAL_SYMBOL_ROWS: PASS')
print('ROW_MULTIPLIERS_ZERO_BASED_3_6_9: -2, -1, 1/4')
