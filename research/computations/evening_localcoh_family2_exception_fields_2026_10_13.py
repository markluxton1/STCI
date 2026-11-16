#!/usr/bin/env python3
"""Exact full-fiber family2 exception certificates, arbitrary number-field degree.

Generation uses standard-library Fraction/AST arithmetic. Macaulay2 supplies a
polynomial dual; verification rederives directions, all affine lifts, and every
actual tensor identity without a CAS. No finite parameter/lambda sampling is used.
"""
from fractions import Fraction as Q
from pathlib import Path
import ast, hashlib, itertools, json, sys
HERE=Path(__file__).resolve().parent
CASES={
 'cubic':[-4,9,4,3],
 'quartic':[-7,-42,2,10,13],
 'degree15':[-610,285598,811630,1345117,1296458,897946,301686,-34359,-166406,-114414,-54222,-9465,990,2646,810,243]
}
INPUTS=['localcoh-incidence-tensor.txt','localcoh-incidence-bases.txt','localcoh-symbol-top.json','session-localcoh-origin-family-2-seed.json']
def trim(a):
 a=list(a)
 while a and not a[-1]:a.pop()
 return a

def padd(a,b):
 c=[Q(0)]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=x
 return trim(c)
def pscale(a,c):return trim([c*x for x in a])
def pmul(a,b):
 c=[Q(0)]*(len(a)+len(b)-1) if a and b else []
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return trim(c)
def pdiv(a,b):
 a=trim(a);b=trim(b);assert b
 q=[Q(0)]*max(0,len(a)-len(b)+1)
 while a and len(a)>=len(b):
  d=len(a)-len(b);c=a[-1]/b[-1];q[d]=c
  for j,x in enumerate(b):a[d+j]-=c*x
  a=trim(a)
 return trim(q),a
class Audit:
 def __init__(self,case):
  self.case=case;self.mod=list(map(Q,CASES[case]));self.n=len(self.mod)-1
  self.zero=(Q(0),)*self.n;self.one=(Q(1),)+(Q(0),)*(self.n-1)
  self.stem='evening-localcoh-family2-'+case+'-2026-10-13'
  self.cert=HERE/(self.stem+'-certificate.json')
 def field(self,a):return tuple(pdiv(a,self.mod)[1]+[Q(0)]*self.n)[:self.n]
 def times(self,a,b):return self.field(pmul(a,b))
 def inverse(self,a):
  r0,r1=self.mod,trim(a);s0,s1=[],[Q(1)]
  while r1:
   q,r=pdiv(r0,r1);r0,r1=r1,r;s0,s1=s1,padd(s0,pscale(pmul(q,s1),-1))
  assert len(r0)==1,'denominator is not a unit modulo the exception factor'
  return self.field(pscale(s0,1/r0[0]))
 def add(self,a,b):
  c=dict(a)
  for d,y in b.items():
   z=tuple(x+y for x,y in zip(c.get(d,self.zero),y))
   if z==self.zero:c.pop(d,None)
   else:c[d]=z
  return c
 def scale(self,a,c):return {d:tuple(c*x for x in v) for d,v in a.items() if c and v!=self.zero}
 def mul(self,a,b):
  c={}
  for i,x in a.items():
   for j,y in b.items():
    z=self.times(x,y)
    if z!=self.zero:c=self.add(c,{i+j:z})
  return c
 def power(self,a,e):
  c={0:self.one}
  while e:
   if e&1:c=self.mul(c,a)
   a=self.mul(a,a);e>>=1
  return c
 def expr(self,s):
  def visit(v):
   if isinstance(v,ast.Constant):
    assert type(v.value)is int
    return {} if not v.value else {0:self.field([Q(v.value)])}
   if isinstance(v,ast.Name):
    assert v.id in ('k','lam')
    return {0:self.field([0,1])} if v.id=='k' else {1:self.one}
   if isinstance(v,ast.UnaryOp):
    assert isinstance(v.op,(ast.UAdd,ast.USub))
    return self.scale(visit(v.operand),-1 if isinstance(v.op,ast.USub) else 1)
   assert isinstance(v,ast.BinOp)
   if isinstance(v.op,ast.Pow):
    assert isinstance(v.right,ast.Constant)and type(v.right.value)is int and v.right.value>=0
    return self.power(visit(v.left),v.right.value)
   a,b=visit(v.left),visit(v.right)
   if isinstance(v.op,ast.Add):return self.add(a,b)
   if isinstance(v.op,ast.Sub):return self.add(a,self.scale(b,-1))
   if isinstance(v.op,ast.Mult):return self.mul(a,b)
   assert isinstance(v.op,ast.Div)and set(b)=={0}
   return self.mul(a,{0:self.inverse(b[0])})
  return visit(ast.parse(s.replace('^','**').replace('lambda','lam'),mode='eval').body)
 def source(self):
  s=json.loads((HERE/INPUTS[3]).read_text());seed=list(map(self.expr,s['seed']))
  assert all(set(v).issubset({0}) for v in seed)
  kernel=list(map(Q,s['kernel']))
  alpha=[self.add(v,{} if not c else {1:self.field([c])}) for v,c in zip(seed,kernel)]
  expected={'a1':'(k**2+3)/(2-2*k**2)','a2':'-(k**2+2*k+3)/(2*(k+1)**2)','b1':'(k-3)*(k**2+2*k+3)/((k-1)**2*(k+1))','b2':'-2*(k**2+1)*(k**2-2*k-1)*(k**2+2*k+3)/((k-1)**3*(k+1)**3)'}
  for name,e in expected.items():assert self.expr(s['family'][name])==self.expr(e)
  p=[{0:self.one},self.expr(s['family']['a1']),self.expr(s['family']['a2'])]
  r=[{0:self.one},self.expr(s['family']['b1']),self.expr(s['family']['b2'])]
  return s,alpha,kernel,p,r
 def tensor(self):
  t=[[Q(0)]*542 for _ in range(74)];lines=(HERE/INPUTS[0]).read_text().splitlines()
  assert lines[0]=='30 18 74 542'
  for line in lines[1:]:
   i,j,c=line.split();t[int(i)][int(j)]+=Q(c)
  assert [v[540]for v in t]==[Q(i==72)for i in range(74)]
  assert [v[541]for v in t]==[Q(i==73)for i in range(74)]
  return t
 def matrix(self,alpha):
  t=self.tensor();L=[]
  for row in t:
   entries=[]
   for j in range(18):
    v={}
    for i in range(30):v=self.add(v,self.scale(alpha[i],row[18*i+j]))
    entries.append(v)
   L.append(entries)
  return L
 def fstring(self,v):return '+'.join('('+str(c)+')'+('*k^'+str(i)if i else '')for i,c in enumerate(v)if c)or '0'
 def generate(self):
  s,a,ker,p,r=self.source();L=self.matrix(a)
  def e(v):return '+'.join('sub(('+self.fstring(c)+'),R)'+('*lambda^'+str(d)if d else '')for d,c in sorted(v.items()))or '0_R'
  mod=self.fstring(self.mod)
  out=['P=QQ[k]; f='+mod+'; print factor f; K0=toField(P/ideal(f)); R=K0[lambda];',
   'L=matrix{'+','.join('{'+','.join(map(e,row))+'}'for row in L)+'};',
   'U=matrix{'+','.join('{'+str(int(i==72))+'}'for i in range(74))+'};',
   'print("actual complete matrix ready: '+self.case+'");',
   'V=gens kernel transpose L; E=transpose U*V; J=ideal E;',
   'print("full polynomial left kernel computed: '+self.case+'");',
   'ff=openOut "research/computations/'+self.stem+'-evaluations.txt"; ff << gens gb J << endl; close ff;',
   'if J==ideal(1_R) then (c=matrix{{1_R}} // E; n=V*c; assert(transpose n*L==0); assert(transpose n*U==matrix{{1_R}}); ff=openOut "research/computations/'+self.stem+'-dual.txt"; for row from 0 to 73 do ff << row << " " << toString n_(row,0) << endl; close ff; print("complete polynomial dual saved: '+self.case+'"));',
   'print("target evaluation ideal: "); print gens gb J; exit 0;']
  (HERE/(self.stem+'.m2')).write_text('\n'.join(out)+'\n')
  print('GENERATED',self.case,'field degree',self.n,flush=True)
 def encode(self,p):return [[d]+list(map(str,c))for d,c in sorted(p.items())]
 def decode(self,p):
  out={}
  for v in p:
   d=v[0];assert d>=0 and d not in out and len(v)==self.n+1
   c=tuple(map(Q,v[1:]));assert c!=self.zero;out[d]=c
  return out
 def regenerate(self):
  s,a,ker,p,r=self.source();dual=[]
  for row,line in enumerate((HERE/(self.stem+'-dual.txt')).read_text().splitlines()):
   i,e=line.split(maxsplit=1);assert int(i)==row;dual.append(self.expr(e))
  inputs=INPUTS+[self.stem+'.m2',self.stem+'-dual.txt',self.stem+'-evaluations.txt',Path(__file__).name]
  out={'case':self.case,'modulus_coefficients':list(map(str,self.mod)),'field_degree':self.n,'sha256':{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest()for n in inputs},'alpha':list(map(self.encode,a)),'dual':list(map(self.encode,dual)),'direction_p':list(map(self.encode,p)),'direction_r':list(map(self.encode,r)),'scope':'Second rational endpoint family, all roots of the defining factor, every affine lower lift lambda','status':'EXACT FIELD POLYNOMIAL CERTIFICATE, INDEPENDENT STANDARD-LIBRARY IDENTITY VERIFICATION'}
  self.cert.write_text(json.dumps(out,indent=2)+'\n')
 def verify(self):
  c=json.loads(self.cert.read_text());assert c['case']==self.case and list(map(Q,c['modulus_coefficients']))==self.mod
  g,h=self.mod,[i*x for i,x in enumerate(self.mod) if i][0:]
  while h:g,h=h,pdiv(g,h)[1]
  assert len(trim(g))==1,'exception factor must be square-free'
  for n,h in c['sha256'].items():assert hashlib.sha256((HERE/n).read_bytes()).hexdigest()==h,n
  s,a,ker,p,r=self.source();assert a==list(map(self.decode,c['alpha']))
  assert p==list(map(self.decode,c['direction_p']))and r==list(map(self.decode,c['direction_r']))
  dual=list(map(self.decode,c['dual']));assert len(dual)==74 and dual[72]=={0:self.one}
  M=[[Q(x)for x in row]for row in json.loads((HERE/INPUTS[2]).read_text())['matrix']]
  rank=0;ech=[row[:]for row in M]
  for j in range(30):
   pivot=next((i for i in range(rank,len(ech))if ech[i][j]),None)
   if pivot is None:continue
   ech[rank],ech[pivot]=ech[pivot],ech[rank];e=ech[rank][j];ech[rank]=[x/e for x in ech[rank]]
   for i in range(rank+1,len(ech)):
    e=ech[i][j]
    if e:ech[i]=[x-e*y for x,y in zip(ech[i],ech[rank])]
   rank+=1
  assert rank==29 and len(a)==30 and any(ker)
  def tmul(a,b):
   c=[{}for _ in range(len(a)+len(b)-1)]
   for i,x in enumerate(a):
    for j,y in enumerate(b):c[i+j]=self.add(c[i+j],self.mul(x,y))
   return c
  def tpow(a,e):
   c=[{0:self.one}]
   for _ in range(e):c=tmul(c,a)
   return c
  top=[]
  for i in range(4):top.extend([{}]+tmul(tpow(p,i),tpow(r,3-i)))
  assert len(top)==len(M)==32
  for row,expected in zip(M,top):
   v={}
   for e,x in zip(row,a):v=self.add(v,self.scale(x,e))
   assert v==expected
  for x,e in zip(a,ker):assert set(x).issubset({0,1})and x.get(1,self.zero)==self.field([e])
  syl=[[p[2],p[1],p[0],{}],[{},p[2],p[1],p[0]],[r[2],r[1],r[0],{}],[{},r[2],r[1],r[0]]];res={}
  for perm in itertools.permutations(range(4)):
   sign=(-1)**sum(perm[i]>perm[j]for i in range(4)for j in range(i+1,4));v={0:self.one}
   for i,j in enumerate(perm):v=self.mul(v,syl[i][j])
   res=self.add(res,self.scale(v,sign))
  assert res==self.expr(s['family']['resultant'])and set(res)=={0}and res[0]!=self.zero
  assert self.times(res[0],self.inverse(res[0]))==self.one,'resultant must be a unit at every root'
  L=self.matrix(a)
  for j in range(18):
   v={}
   for i in range(74):v=self.add(v,self.mul(dual[i],L[i][j]))
   assert not v,('tensor column',j)
  print('PASS',self.case,': directions, rank29 pure-top map, whole affine lift, primitive resultant, 18 exact polynomial dual identities, n^T u=1.',flush=True)
  print('PROVED under actual tensor: every root of degree',self.n,'factor excluded, for all lambda.',flush=True)
if __name__=='__main__':
 selected=[s for s in sys.argv[1:]if s in CASES]or list(CASES)
 for case in selected:
  a=Audit(case)
  if '--generate'in sys.argv:a.generate()
  else:
   if '--regenerate'in sys.argv:a.regenerate()
   a.verify()
