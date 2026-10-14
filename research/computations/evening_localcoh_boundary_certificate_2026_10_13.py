#!/usr/bin/env python3
"""New exact endpoint-boundary certificates. Only standard library required.
Generic verification clears seed denominators using rational polynomial algebra;
finite exceptions are checked in exact quotient fields using the same full tensor.
"""
from fractions import Fraction as Q
from pathlib import Path
import ast, hashlib, importlib.util, itertools, json, sys
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('fields',HERE/'evening_localcoh_family2_exception_fields_2026_10_13.py')
FIELDS=importlib.util.module_from_spec(spec);spec.loader.exec_module(FIELDS)
trim,padd,pscale,pmul,pdiv=FIELDS.trim,FIELDS.padd,FIELDS.pscale,FIELDS.pmul,FIELDS.pdiv

def gcd(a,b):
 while b:a,b=b,pdiv(a,b)[1]
 return pscale(a,1/a[-1]) if a else []
def reduced(a,b):
 assert b
 if not a:return [],[Q(1)]
 d=gcd(a,b);a=pdiv(a,d)[0];b=pdiv(b,d)[0]
 return pscale(a,1/b[-1]),pscale(b,1/b[-1])
def rational(value):
 def op(v):
  if isinstance(v,ast.Constant):
   assert type(v.value)is int;return [Q(v.value)],[Q(1)]
  if isinstance(v,ast.Name):assert v.id=='k';return [Q(0),Q(1)],[Q(1)]
  if isinstance(v,ast.UnaryOp):
   a,b=op(v.operand);assert isinstance(v.op,(ast.UAdd,ast.USub));return pscale(a,-1 if isinstance(v.op,ast.USub)else 1),b
  assert isinstance(v,ast.BinOp)
  if isinstance(v.op,ast.Pow):
   assert isinstance(v.right,ast.Constant)and type(v.right.value)is int and v.right.value>=0
   a,b=op(v.left);x,y=[Q(1)],[Q(1)]
   for _ in range(v.right.value):x,y=pmul(x,a),pmul(y,b)
   return reduced(x,y)
  a,b=op(v.left);c,d=op(v.right)
  if isinstance(v.op,ast.Add):return reduced(padd(pmul(a,d),pmul(b,c)),pmul(b,d))
  if isinstance(v.op,ast.Sub):return reduced(padd(pmul(a,d),pscale(pmul(b,c),-1)),pmul(b,d))
  if isinstance(v.op,ast.Mult):return reduced(pmul(a,c),pmul(b,d))
  assert isinstance(v.op,ast.Div);return reduced(pmul(a,d),pmul(b,c))
 return op(ast.parse(value.replace('^','**'),mode='eval').body)
def add(a,b):
 c=dict(a)
 for ij,x in b.items():
  c[ij]=c.get(ij,Q(0))+x
  if not c[ij]:c.pop(ij)
 return c
def scale(a,x):return {ij:c*x for ij,c in a.items()if c*x}
def mul(a,b):
 c={}
 for (i,j),x in a.items():
  for (m,n),y in b.items():c=add(c,{(i+m,j+n):x*y})
 return c
def power(a,e):
 c={(0,0):Q(1)}
 for _ in range(e):c=mul(c,a)
 return c
def polynomial(value):
 def op(v):
  if isinstance(v,ast.Constant):assert type(v.value)is int;return {(0,0):Q(v.value)}if v.value else {}
  if isinstance(v,ast.Name):assert v.id in('k','lam');return {(1,0)if v.id=='k'else(0,1):Q(1)}
  if isinstance(v,ast.UnaryOp):assert isinstance(v.op,(ast.UAdd,ast.USub));return scale(op(v.operand),-1 if isinstance(v.op,ast.USub)else 1)
  assert isinstance(v,ast.BinOp)
  if isinstance(v.op,ast.Pow):assert isinstance(v.right,ast.Constant)and v.right.value>=0;return power(op(v.left),v.right.value)
  a,b=op(v.left),op(v.right)
  if isinstance(v.op,ast.Add):return add(a,b)
  if isinstance(v.op,ast.Sub):return add(a,scale(b,-1))
  if isinstance(v.op,ast.Mult):return mul(a,b)
  assert isinstance(v.op,ast.Div)and set(b)=={(0,0)};return scale(a,1/b[0,0])
 return op(ast.parse(value.replace('^','**').replace('lambda','lam'),mode='eval').body)
def univ(a):return {(i,0):c for i,c in enumerate(a)if c}
def encode(p):return [[i,j,str(c)]for(i,j),c in sorted(p.items())]
def decode(p):return {(i,j):Q(c)for i,j,c in p}
def tensor():
 t=[[Q(0)]*542 for _ in range(74)]
 lines=(HERE/'localcoh-incidence-tensor.txt').read_text().splitlines();assert lines[0]=='30 18 74 542'
 for line in lines[1:]:i,j,c=line.split();t[int(i)][int(j)]=Q(c)
 return t

def generic(index,regenerate=False):
 stem='evening_localcoh_boundary_'+str(index)+'_2026_10_13';cert=HERE/(stem+'-certificate.json')
 data=json.loads((HERE/(stem+'-seed.json')).read_text());seeds=list(map(rational,data['seed']));kernel=list(map(Q,data['kernel']))
 den=[Q(1)]
 for a,b in seeds:den=pdiv(pmul(den,b),gcd(den,b))[0]
 alpha=[add(univ(pmul(a,pdiv(den,b)[0])),{(i,1):c*slope for i,c in enumerate(den)if c*slope})for(a,b),slope in zip(seeds,kernel)]
 dual=[]
 for row,line in enumerate((HERE/(stem+'-cleared-dual.txt')).read_text().splitlines()):
  i,e=line.split(maxsplit=1);assert int(i)==row;dual.append(polynomial(e))
 target=polynomial((HERE/(stem+'-denominator.txt')).read_text())
 inputs=['localcoh-incidence-tensor.txt','localcoh-incidence-bases.txt','localcoh-symbol-top.json',stem+'-seed.json',stem+'-cleared-dual.txt',stem+'-denominator.txt']
 if regenerate:
  c={'index':index,'sha256':{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest()for n in inputs},'ancestor_denominator':list(map(str,den)),'alpha':list(map(encode,alpha)),'dual':list(map(encode,dual)),'target':encode(target),'status':'NEW EXACT GENERIC BOUNDARY CERTIFICATE'}
  cert.write_text(json.dumps(c,indent=2)+'\n')
 c=json.loads(cert.read_text())
 for n,h in c['sha256'].items():assert hashlib.sha256((HERE/n).read_bytes()).hexdigest()==h,n
 assert alpha==list(map(decode,c['alpha']))and dual==list(map(decode,c['dual']))and target==decode(c['target'])
 assert len(alpha)==30 and len(dual)==74 and dual[72]==target and target
 T=tensor()
 for j in range(18):
  v={}
  for i in range(30):
   prod={}
   for r in range(74):prod=add(prod,scale(dual[r],T[r][18*i+j]))
   v=add(v,mul(prod,alpha[i]))
  assert not v,('generic column',j)
 # Cover every lift of the declared pure top: accepted rank29 map plus its exact one-dimensional kernel.
 M=[[Q(x)for x in row]for row in json.loads((HERE/'localcoh-symbol-top.json').read_text())['matrix']]
 fam=data['family'];p=[rational(fam.get('p0','1')),rational(fam['a1']),rational(fam['a2'])];r=[rational('1'),rational(fam['b1']),rational(fam['b2'])]
 d=[Q(1)]
 for a,b in p+r:d=pdiv(pmul(d,b),gcd(d,b))[0]
 P=[univ(pmul(a,pdiv(d,b)[0]))for a,b in p];R=[univ(pmul(a,pdiv(d,b)[0]))for a,b in r]
 def tmul(a,b):
  out=[{}for _ in range(len(a)+len(b)-1)]
  for i,x in enumerate(a):
   for j,y in enumerate(b):out[i+j]=add(out[i+j],mul(x,y))
  return out
 def tpow(a,e):
  out=[{(0,0):Q(1)}]
  for _ in range(e):out=tmul(out,a)
  return out
 top=[]
 for i in range(4):top.extend([{}]+tmul(tpow(P,i),tpow(R,3-i)))
 assert len(top)==32
 for row,expected in zip(M,top):
  v={}
  for x,a in zip(row,alpha):v=add(v,scale(a,x))
  assert mul(v,power(univ(d),3))==mul(univ(den),expected)
 print('PASS new boundary',index,'generic: complete affine lifts, 32 pure-top identities, all 18 actual tensor identities; target denominator',str(list(map(str,target.keys()))),flush=True)
 return target

class Boundary(FIELDS.Audit):
 def __init__(self,case):
  self.case=case;self.mod=list(map(Q,{'zero':[0,1],'eight':[-8,1],'minus8over3':[8,3],'quad':[-128,24,1]}[case]));self.n=len(self.mod)-1
  self.zero=(Q(0),)*self.n;self.one=(Q(1),)+(Q(0),)*(self.n-1)
  self.stem='evening_localcoh_boundary_4_'+case+'_2026_10_13';self.cert=HERE/(self.stem+'-certificate.json')
 def source(self):
  s=json.loads((HERE/'evening_localcoh_boundary_4_2026_10_13-seed.json').read_text());seed=list(map(self.expr,s['seed']));kernel=list(map(Q,s['kernel']))
  assert all(set(v).issubset({0})for v in seed)
  alpha=[self.add(v,{}if not c else{1:self.field([c])})for v,c in zip(seed,kernel)]
  expected={'p0':'0','a1':'-1/2','a2':'1','b1':'2','b2':'k'}
  for key,v in expected.items():assert self.expr(s['family'][key])==self.expr(v)
  p=[{},self.expr('-1/2'),self.expr('1')];r=[self.expr('1'),self.expr('2'),self.expr('k')]
  s['family']['resultant']='(k+8)/4'
  return s,alpha,kernel,p,r
 def regenerate(self):
  src=HERE/(self.stem+'-generic-dual.txt');dst=HERE/(self.stem+'-dual.txt');dst.write_text(src.read_text());super().regenerate()

if __name__=='__main__':
 if 'generic'in sys.argv:
  for i in (3,4):
   if str(i)in sys.argv:generic(i,'--regenerate'in sys.argv)
 else:
  FIELDS.INPUTS[3]='evening_localcoh_boundary_4_2026_10_13-seed.json'
  for case in('zero','eight','minus8over3','quad'):
   b=Boundary(case)
   if '--regenerate'in sys.argv:b.regenerate()
   b.verify()
