#!/usr/bin/env python3
"""Prepare NEW exact polynomial block inversion, no inherited verifier replay."""
from pathlib import Path
from fractions import Fraction as Q
import ast, hashlib, json, math, re
from evening_localcoh_family2_exception_fields_2026_10_13 import trim,padd,pscale,pmul,pdiv,CASES
HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'validation/2026-10-14-localcoh-degree15-attempt05/source.m2'
OUT=HERE.parent/'validation/2026-10-14-localcoh-degree15-attempt06'
def gcd(a,b):
 while b:a,b=b,pdiv(a,b)[1]
 return pscale(a,1/a[-1]) if a else []
class RF:
 def __init__(self,n=(),d=(Q(1),)):
  n=trim(n);d=trim(d);assert d
  if not n:self.n=[];self.d=[Q(1)];return
  g=gcd(n,d);n,r=pdiv(n,g);assert not r;d,r=pdiv(d,g);assert not r
  c=1/d[-1];self.n=pscale(n,c);self.d=pscale(d,c)
 def __add__(self,b):return RF(padd(pmul(self.n,b.d),pmul(b.n,self.d)),pmul(self.d,b.d))
 def __neg__(self):return RF(pscale(self.n,-1),self.d)
 def __sub__(self,b):return self+-b
 def __mul__(self,b):return RF(pmul(self.n,b.n),pmul(self.d,b.d))
 def __truediv__(self,b):return RF(pmul(self.n,b.d),pmul(self.d,b.n))
 def __pow__(self,e):
  c=RF([Q(1)])
  for _ in range(e):c=c*self
  return c

def expr(s,env):
 def v(t):
  if isinstance(t,ast.Constant):return RF([Q(t.value)])
  if isinstance(t,ast.Name):return env[t.id]
  if isinstance(t,ast.UnaryOp):return -v(t.operand) if isinstance(t.op,ast.USub) else v(t.operand)
  assert isinstance(t,ast.BinOp)
  if isinstance(t.op,ast.Pow):return v(t.left)**t.right.value
  a,b=v(t.left),v(t.right)
  if isinstance(t.op,ast.Add):return a+b
  if isinstance(t.op,ast.Sub):return a-b
  if isinstance(t.op,ast.Mult):return a*b
  assert isinstance(t.op,ast.Div);return a/b
 return v(ast.parse(s.replace('^','**').replace('0_K','0'),mode='eval').body)
def polystr(a):
 assert all(x.denominator==1 for x in a)
 return str(len(a))+'  '+' '.join(str(x.numerator) for x in a)
def main():
 s=SOURCE.read_text();env={'k':RF([Q(0),Q(1)])}
 for l in s.splitlines():
  m=re.fullmatch(r'(seedDenominator\d+)=sub\(\((.*)\),K\);',l)
  if m:env[m[1]]=expr(m[2],env)
  m=re.fullmatch(r'(z\d+)=sub\(\((.*)\),K\)(?:/(seedDenominator\d+))?;',l)
  if m:
   value=expr(m[2],env);env[m[1]]=value/env[m[3]] if m[3] else value
 line=next(l for l in s.splitlines() if l.startswith('B=matrix'))
 B=[[expr(e,env) for e in row.split(',')] for row in line[len('B=matrix{{'):-len('}};')].split('},{')]
 diagnostic=json.loads((HERE/'general-localcoh-degree15-sparse-block-2026-10-14-diagnostic.json').read_text())
 rows=diagnostic['selected_rows'];cols=diagnostic['selected_columns']
 block=[[B[i][j] for j in cols] for i in rows];d=[Q(1)]
 for row in block:
  for x in row:
   g=gcd(d,x.d);div,r=pdiv(x.d,g);assert not r;d=pmul(d,div)
 nums=[]
 for row in block:
  for x in row:
   q,r=pdiv(d,x.d);assert not r;nums.append(pmul(q,x.n))
 scale=math.lcm(*(x.denominator for p in nums for x in p));d=pscale(d,scale);nums=[pscale(p,scale) for p in nums]
 text='17\n'+polystr(d)+'\n'+polystr(list(map(Q,CASES['degree15'])))+'\n'+'\n'.join(map(polystr,nums))+'\n'
 OUT.mkdir(exist_ok=True);(OUT/'block-input.txt').write_text(text)
 record={'scope':'New exact Z[k] fraction-free block inversion input; inherited pencil used as premise.','source':str(SOURCE.relative_to(HERE.parent.parent)),'source_sha256':hashlib.sha256(s.encode()).hexdigest(),'preparer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'selected_rows':rows,'selected_columns':cols,'missing_column':diagnostic['missing_column'],'clearing_polynomial_coefficients':list(map(str,d)),'max_entry_degree':max(map(len,nums))-1,'max_entry_coefficient_bits':max(abs(x.numerator).bit_length() for p in nums for x in p),'block_input_sha256':hashlib.sha256(text.encode()).hexdigest()}
 (OUT/'prepared-lineage.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
if __name__=='__main__':main()
