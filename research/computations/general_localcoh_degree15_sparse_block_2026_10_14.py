#!/usr/bin/env python3
"""Bounded modular DIAGNOSTIC selecting a B block; never a proof of exclusion.

Read the unchanged attempt03 rational pencil. Arithmetic is in the quotient
F_p[k]/(f15); every inverted pivot must be a unit. A later characteristic-zero
source must certify the selected block inverse and original-tensor dual.
"""
from pathlib import Path
import ast
import hashlib
import json
import re
import time

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'general-localcoh-family2-degree15-corank-one-2026-10-14-attempt03.m2'
PRIME = 1000000007
MODULUS = [-610,285598,811630,1345117,1296458,897946,301686,-34359,-166406,-114414,-54222,-9465,990,2646,810,243]

def trim(a):
    a=list(a)
    while a and not a[-1]: a.pop()
    return a

def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a): c[i]=(c[i]+x)%PRIME
    for i,x in enumerate(b): c[i]=(c[i]+x)%PRIME
    return trim(c)

def scale(a,c): return trim([(x*c)%PRIME for x in a])

def mul(a,b):
    c=[0]*(len(a)+len(b)-1) if a and b else []
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=(c[i+j]+x*y)%PRIME
    return trim(c)

def div(a,b):
    a=trim(a); b=trim(b); assert b
    q=[0]*max(0,len(a)-len(b)+1)
    inv=pow(b[-1],-1,PRIME)
    while a and len(a)>=len(b):
        d=len(a)-len(b); c=a[-1]*inv%PRIME; q[d]=c
        for j,x in enumerate(b): a[d+j]=(a[d+j]-c*x)%PRIME
        a=trim(a)
    return trim(q),a

F=[x%PRIME for x in MODULUS]
def field(a): return tuple(div(a,F)[1])
ZERO=(); ONE=(1,)
def times(a,b): return field(mul(a,b))
def plus(a,b): return tuple(add(a,b))
def neg(a): return tuple(scale(a,-1))
def inverse(a):
    r0,r1=F,list(a); s0,s1=[],[1]
    while r1:
        q,r=div(r0,r1); r0,r1=r1,r; s0,s1=s1,add(s0,scale(mul(q,s1),-1))
    if len(r0)!=1: raise ValueError('nonunit modular diagnostic pivot')
    return field(scale(s0,pow(r0[0],-1,PRIME)))

def power(a,e):
    c=ONE
    while e:
        if e&1:c=times(c,a)
        a=times(a,a);e>>=1
    return c

def expression(s,env):
    def visit(v):
        if isinstance(v,ast.Constant): return field([v.value])
        if isinstance(v,ast.Name): return env[v.id]
        if isinstance(v,ast.UnaryOp):
            a=visit(v.operand)
            return neg(a) if isinstance(v.op,ast.USub) else a
        assert isinstance(v,ast.BinOp)
        a=visit(v.left)
        if isinstance(v.op,ast.Pow): return power(a,v.right.value)
        b=visit(v.right)
        if isinstance(v.op,ast.Add): return plus(a,b)
        if isinstance(v.op,ast.Sub): return plus(a,neg(b))
        if isinstance(v.op,ast.Mult): return times(a,b)
        assert isinstance(v.op,ast.Div)
        return times(a,inverse(b))
    return visit(ast.parse(s.replace('^','**'),mode='eval').body)

def main():
    started=time.monotonic(); source=SOURCE.read_text(); env={'k':(0,1)}
    for line in source.splitlines():
        m=re.fullmatch(r'(z\d+)=sub\(\((.*)\),K\);',line)
        if m: env[m[1]]=expression(m[2],env)
    line=next(l for l in source.splitlines() if l.startswith('B=matrix'))
    rows=line[len('B=matrix{{'):-len('}};')].split('},{')
    B=[[expression(e.replace('0_K','0'),env) for e in row.split(',')] for row in rows]
    assert len(B)==56 and all(len(row)==18 for row in B)
    original=[row[:] for row in B]; row_order=list(range(56)); cols=[]; rows=[]
    active=set(range(18))
    for r in range(17):
        options=[]
        for i in range(r,56):
            nonzero=[j for j in active if B[i][j]]
            for j in nonzero:
                options.append((len(nonzero),sum(bool(B[ii][j]) for ii in range(r,56)),i,j))
        found=False
        for _,_,i,j in sorted(options):
            try: inv=inverse(B[i][j])
            except ValueError:continue
            found=True;break
        assert found,'no unit pivot in diagnostic quotient ring'
        B[r],B[i]=B[i],B[r];row_order[r],row_order[i]=row_order[i],row_order[r]
        B[r]=[times(x,inv) for x in B[r]]
        for i in range(r+1,56):
            coeff=B[i][j]
            if coeff:B[i]=[plus(x,neg(times(coeff,y))) for x,y in zip(B[i],B[r])]
        rows.append(row_order[r]);cols.append(j);active.remove(j)
    assert len(active)==1
    result={
        'scope':'Modular diagnostic only, no mathematical exclusion or exact rank claim.',
        'source':SOURCE.name,'source_sha256':hashlib.sha256(source.encode()).hexdigest(),
        'prime':PRIME,'modulus_coefficients':MODULUS,
        'selected_rows':rows,'selected_columns':cols,'missing_column':next(iter(active)),
        'original_block_nonzero_entries':sum(bool(original[i][j]) for i in rows for j in cols),
        'elapsed_seconds':round(time.monotonic()-started,3),
        'required_exact_followup':'Invert selected17x17 block over QQ[k]/f15; verify M*inverse=I, D*B=I-h*e_missing, and normalized originaltensor dual.'
    }
    output=HERE/'general-localcoh-degree15-sparse-block-2026-10-14-diagnostic.json'
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
