from fractions import Fraction as Q
from pathlib import Path
import ast
N=17;zero=(0,)*N
class P:
 def __init__(self,d=None):self.d={m:c for m,c in (d or {}).items() if c}
 def __add__(self,b):
  b=cast(b); d=self.d.copy()
  for m,c in b.d.items():d[m]=d.get(m,Q(0))+c
  return P(d)
 __radd__=__add__
 def __neg__(self):return P({m:-c for m,c in self.d.items()})
 def __sub__(self,b):return self+-cast(b)
 def __rsub__(self,b):return cast(b)+-self
 def __mul__(self,b):
  b=cast(b); d={}
  for m,c in self.d.items():
   for n,e in b.d.items():
    k=tuple(a+b for a,b in zip(m,n))
    if k[0]+k[1]<=3:d[k]=d.get(k,Q(0))+c*e
  return P(d)
 __rmul__=__mul__
 def __pow__(self,n):
  if n<0:
   assert len(self.d)==1
   (m,c),=self.d.items()
   return P({tuple(n*a for a in m):c**n})
  out=cast(1)
  for _ in range(n):out=out*self
  return out
 def __truediv__(self,b):return self*cast(b)**-1
 def __eq__(self,b):return self.d==cast(b).d
 def layer(self,n):return P({m:c for m,c in self.d.items() if m[0]+m[1]==n})
def cast(x):return x if isinstance(x,P) else P({zero:Q(x)})
def var(i):
 m=list(zero);m[i]=1;return P({tuple(m):Q(1)})
u,v,z,t1,t2=[var(i) for i in range(5)]
h=[var(5+i) for i in range(12)]
B=u+Q(3,2)*z*v
t=z**-4*B
inv=z**-4*sum(((-1)**n*t**n for n in range(4)),cast(0))
w=(z**3+v)*inv
ap=z*inv-w**3
bp=inv-w**4
up=ap/2
vp=-3*w*ap+2*bp
f=t1*t2*u**2+(t1+t2)*z*u*v+z**2*v**2
nf=z**16*(t1*t2*w**2*up**2+(t1+t2)*w*up*vp+vp**2)
assert nf.layer(2)==f
H=sum((h[j]*u*z**(-6+j) for j in range(6)),cast(0))+sum((h[6+j]*v*z**(-6+j) for j in range(6)),cast(0))
beta=-2*u*z**-4-v*z**-3
s3=nf.layer(3)-(H+beta)*f
first=[]
for i in range(4):
 for k in range(-4,0):
  out={}
  for m,c in s3.d.items():
   if m[:3]==(3-i,i,k):out[(0,0,0)+m[3:]]=c
  first.append(P(out))
# Independently parse the exported M2 expressions using exact rational arithmetic.
source=Path('research/computations/conditional_2_12_singular_continuation_2026_10_20_diagonal.m2').read_text()
expr=source.split('firstEquations={',1)[1].split('};',1)[0]
names={'t1':t1,'t2':t2,**{f'h{i}':h[i] for i in range(12)}}
def ev(a):
 if isinstance(a,ast.Constant):return cast(a.value)
 if isinstance(a,ast.Name):return names[a.id]
 if isinstance(a,ast.UnaryOp):return -ev(a.operand) if isinstance(a.op,ast.USub) else ev(a.operand)
 if isinstance(a,ast.BinOp):
  x,y=ev(a.left),ev(a.right)
  if isinstance(a.op,ast.Add):return x+y
  if isinstance(a.op,ast.Sub):return x-y
  if isinstance(a.op,ast.Mult):return x*y
  if isinstance(a.op,ast.Div):return x/y
 raise TypeError(ast.dump(a))
exported=[ev(ast.parse(s,mode='eval').body) for s in expr.split(',')]
assert len(first)==len(exported)==16
print('INDEPENDENT_DIRECT_TRANSITION_FIRST_EXPORT_MATCH:',all(a==b for a,b in zip(first,exported)))
for i,(a,b) in enumerate(zip(first,exported)):
 if a!=b:print('MISMATCH',i,(a-b).d)
