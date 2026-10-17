#!/usr/bin/env python3
"""Explore all e=2 primitive-triple directions against ambient quartics."""
from pathlib import Path
import importlib.util,json
import sympy as sp
spec=importlib.util.spec_from_file_location('gen',Path(__file__).with_name('generate.py'))
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)

def main():
    A={0:g.a0,1:g.a1,2:g.a2};B={0:g.b0,1:g.b1,2:g.b2}
    Av={2-i:c for i,c in A.items()};Bv={2-i:c for i,c in B.items()}
    W,up,vp=g.ambient([{},A,{},{}],[{},B,{},{}])
    mp=g.plus(g.prod(g.evalpoly(Bv,W),up),g.scale(-1,g.prod(g.evalpoly(Av,W),vp)))
    h2=g.shift(9,mp[2]);gu={e:c for e,c in h2.items() if e>=0}
    exponents=[(4-j-k-l,j,k,l) for j in range(5) for k in range(5-j) for l in range(5-j-k)]
    columns=[]
    for i,j,k,l in exponents:
        weight=j+3*k+4*l
        col={('c',weight):1,('u',weight-4):l,('v',weight-3):sp.Rational(2*k+3*l,2)}
        columns.append({key:c for key,c in col.items() if c})
    keys=sorted(set(key for c in columns for key in c))
    first=sp.Matrix([[c.get(key,0) for c in columns] for key in keys])
    rows=list(first.T.rref()[1]);cols=list(first.rref()[1])
    assert len(rows)==len(cols)==34
    inv=first.extract(rows,cols).inv()
    lifts=[];residuals=[]
    for d in range(8):
        target={}
        for e,c in B.items():target[('u',e+d)]=c.as_expr()
        for e,c in A.items():target[('v',e+d)]=-c.as_expr()
        vec=sp.Matrix([target.get(key,0) for key in keys])
        solution=inv*vec.extract(rows,[0])
        sol=sp.zeros(35,1)
        for i,c in zip(cols,solution):sol[i]=c
        residual=first*sol-vec
        lifts.append([g.R.from_expr(c) for c in sol])
        residuals.append([g.R.from_expr(residual[i]) for i in range(len(keys)) if i not in rows])
    q2={(2,0,0,2):1,(1,1,1,1):-2,(0,2,2,0):1}
    lifts.append([g.R(q2.get(e,0)) for e in exponents])
    zeros=[{} for _ in range(g.N-1)]
    u=[{},A,{},{}];v=[{},B,{},{}]
    X=[[g.lp()]+zeros,[g.lp(1,1)]+zeros,
       g.plus([g.lp(1,3)]+zeros,v),
       g.plus([g.lp(1,4)]+zeros,u,g.zscale(1,g.scale(g.QQ(3,2),v)))]
    monomials=[]
    for es in exponents:
        out=[g.lp()]+zeros
        for xi,e in zip(X,es):out=g.prod(out,g.power(xi,e))
        monomials.append(out)
    jets=[]
    for d,lift in enumerate(lifts):
        jet=g.plus(*(g.scale(c,m) for c,m in zip(lift,monomials)))
        if d<8:jet[2]=g.add(jet[2],g.neg(g.shift(d,gu)))
        jets.append(jet[2])
    symbolmatrix=[[residuals[d][j] if d<8 else g.zero for d in range(9)] for j in range(len(residuals[0]))]
    ekeys=sorted(set(e for jet in jets for e in jet))
    jetmatrix=[[jet.get(e,g.zero) for jet in jets] for e in ekeys]
    nonzero_symbol=[row for row in symbolmatrix if any(row)]
    assert len(nonzero_symbol)==3 and ekeys==list(range(10))
    factors=[(8*g.a1*g.b2+12*g.a2**2+8*g.a2*g.b1+26*g.b0*g.b2+13*g.b1**2)/4,
             g.b2*(4*g.a2+13*g.b1)/2,13*g.b2**2/4]
    for row,c in zip(jetmatrix[7:],factors):
        assert all(x==c*y for x,y in zip(row,nonzero_symbol[2]))
    matrix=nonzero_symbol+jetmatrix[:7]
    stringify=lambda mat:[[str(c.as_expr()) for c in row] for row in mat]
    det=g.bezout(A,B)[0]
    data={'resultant':str(det.as_expr()),'symbolmatrix':stringify(symbolmatrix),
          'jetmatrix':stringify(jetmatrix),'jet_exponents':ekeys,
          'lifts':[[str(c.as_expr()) for c in l] for l in lifts],'monomials':exponents}
    Path(__file__).with_name('general_triple_contact.json').write_text(json.dumps(data,indent=2)+'\n')
    matstr=lambda m:'matrix{'+','.join('{'+','.join(str(c.as_expr()) for c in row)+'}' for row in m)+'}'
    m2=['S=QQ[a0,a1,a2,b0,b1,b2,MonomialOrder=>GRevLex];',f'D={det.as_expr()};',
        'M='+matstr(matrix)+';','J=trim minors(9,M);','print(numgens J);',
        'K=saturate(J,ideal(D));','print gens gb K;']
    Path(__file__).with_name('general_triple_contact.m2').write_text('\n'.join(m2).replace('**','^')+'\n')
    print('general matrices:',len(symbolmatrix),len(jetmatrix),'x9')

if __name__=='__main__':main()
