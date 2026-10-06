#!/usr/bin/env python3
"""Quartic contact matrix on universal primitive-fourth directions."""
import importlib.util,json
from pathlib import Path
import sympy as sp
spec=importlib.util.spec_from_file_location('gen',Path(__file__).with_name('generate.py'))
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)

def normlp(p,det):
    out={}
    for e,c in p.items():
        num,d=g.reduce_inverse(c,det)
        if num: out[e]=num*g.r**d
    return out

def primitive_fourth():
    A={0:g.a0,1:g.a1,2:g.a2};B={0:-2*g.a1,1:-2*g.a2,2:g.b2}
    Av={2-i:c for i,c in A.items()};Bv={2-i:c for i,c in B.items()}
    det,S,T=g.bezout(A,B);detv,Sv,Tv=g.bezout(Av,Bv)
    assert det==detv
    W,up,vp=g.ambient([{},A,{},{}],[{},B,{},{}])
    mp=g.plus(g.prod(g.evalpoly(Bv,W),up),g.scale(-1,g.prod(g.evalpoly(Av,W),vp)))
    h2=g.shift(9,mp[2]);gu2={e:c for e,c in h2.items() if e>=0}
    gv2={-e-1:-c for e,c in h2.items() if e<0}
    u=[{},A,g.neg(g.mul(T,gu2)),{}];v=[{},B,g.mul(S,gu2),{}]
    W,up,vp=g.ambient(u,v)
    mp=g.plus(g.prod(g.evalpoly(Bv,W),up),g.scale(-1,g.prod(g.evalpoly(Av,W),vp)))
    ep=g.plus(g.prod(g.evalpoly(Sv,W),up),g.prod(g.evalpoly(Tv,W),vp))
    mu=g.plus(mp,g.prod(g.evalpoly(gv2,W),g.power(ep,2)))
    h3=normlp(g.shift(9,mu[3]),det)
    assert not any(e in h3 for e in [-1,-2,-3,-4,-5])
    gu3={e:c for e,c in h3.items() if e>=0}
    gv3={-e-6:-c for e,c in h3.items() if e<0}
    u[3]=g.neg(g.mul(T,gu3));v[3]=g.mul(S,gu3)
    return det,A,B,S,T,u,v,gu2,gv2,gu3,gv3

def main():
    det,A,B,S,T,u,v,*corrections=primitive_fourth()
    # All homogeneous quartic monomials and their first normal coefficients.
    exponents=[(4-j-k-l,j,k,l) for j in range(5) for k in range(5-j) for l in range(5-j-k)]
    columns=[]
    for i,j,k,l in exponents:
        weight=j+3*k+4*l
        col={('c',weight):1,('u',weight-4):l,('v',weight-3):sp.Rational(2*k+3*l,2)}
        columns.append({key:c for key,c in col.items() if c})
    keys=sorted(set(key for c in columns for key in c))
    first=sp.Matrix([[c.get(key,0) for c in columns] for key in keys])
    hdegrees=[0,1,3,4,6,7]
    lifts=[]
    for d in hdegrees:
        target={}
        for e,c in B.items():target[('u',e+d)]=c.as_expr()
        for e,c in A.items():target[('v',e+d)]=-c.as_expr()
        vec=sp.Matrix([target.get(key,0) for key in keys])
        sol,params=first.gauss_jordan_solve(vec)
        sol=sol.subs({p:0 for p in params})
        assert first*sol==vec
        lifts.append([g.R.from_expr(s) for s in sol])
    # Extra kernel generator Q²=(x0*x3-x1*x2)².
    q2={ (2,0,0,2):1,(1,1,1,1):-2,(0,2,2,0):1}
    lifts.append([g.R(q2.get(e,0)) for e in exponents])
    # Universal cubic found independently from cubic first symbols.
    x,y,z,w=sp.symbols('x y z w')
    aa0,aa1,aa2,bb2=[p.as_expr() for p in [g.a0,g.a1,g.a2,g.b2]]
    cubic=(x*w-y*z)*(2*aa0*aa1*x+2*aa0*aa2*y+aa1*bb2*z+aa2*bb2*w)+aa0**2*(x**2*z-y**3)+aa0*bb2*(x*z**2-y**2*w)-bb2**2*(y*w**2-z**3)/4
    cubic_lifts=[]
    for xi in [x,y,z,w]:
        p=sp.Poly(sp.expand(xi*cubic),x,y,z,w)
        cubic_lifts.append([g.R.from_expr(p.coeff_monomial(x**i*y**j*z**k*w**l)) for i,j,k,l in exponents])
    zeros=[{} for _ in range(g.N-1)]
    X=[ [g.lp()]+zeros,[g.lp(1,1)]+zeros,
        g.plus([g.lp(1,3)]+zeros,v),
        g.plus([g.lp(1,4)]+zeros,u,g.zscale(1,g.scale(g.QQ(3,2),v))) ]
    monomials=[]
    for es in exponents:
        out=[g.lp()]+zeros
        for xi,e in zip(X,es):out=g.prod(out,g.power(xi,e))
        monomials.append(out)
    jets=[]
    for lift in lifts:
        jet=g.plus(*(g.scale(c,m) for c,m in zip(lift,monomials)))
        jet=[normlp(p,det) for p in jet]
        assert not jet[0] and not jet[1]
        jets.append(jet)
    for lift in cubic_lifts:
        jet=g.plus(*(g.scale(c,m) for c,m in zip(lift,monomials)))
        assert all(not normlp(p,det) for p in jet)
    keys2=sorted(set(e for jet in jets for e in jet[2]))
    keys3=sorted(set(e for jet in jets for e in jet[3]))
    assert all(e>=0 for e in keys2+keys3)
    matrix2=[];matrix3=[]
    for degree,keys,mat in [(2,keys2,matrix2),(3,keys3,matrix3)]:
        for e in keys:
            entries=[g.reduce_inverse(jet[degree].get(e,g.zero),det) for jet in jets]
            d=max(d for p,d in entries)
            row=[p*det**(d-j) for p,j in entries]
            mat.append([str(p.as_expr()) for p in row])
    data={'resultant':str(det.as_expr()),'monomials':exponents,'lifts':[[str(c.as_expr()) for c in l] for l in lifts],
          'hdegrees':hdegrees,'matrix2':matrix2,'matrix3':matrix3,
          'cubic':str(sp.expand(cubic)),
          'cubic_multiples':[[str(c.as_expr()) for c in l] for l in cubic_lifts],
          'corrections':[{str(e):str(c.as_expr()) for e,c in sorted(p.items())} for p in corrections]}
    Path(__file__).with_name('quartic_contact.json').write_text(json.dumps(data,indent=2)+'\n')
    matstr=lambda m:'matrix{'+','.join('{'+','.join(row)+'}' for row in m)+'}'
    text=['S=QQ[a0,a1,a2,b2,MonomialOrder=>GRevLex];',f'D={det.as_expr()};',
          'M2jet='+matstr(matrix2)+';','M3jet='+matstr(matrix3)+';',
          'assert(rank M2jet == 3);',
          'assert(rank(M2jet||M3jet) == 3);',
          'assert(det(M2jet^{0,1,2}_{4,5,6}) == -a0^8);',
          'assert(det(M2jet^{4,5,6}_{0,1,6}) == -b2^8/256);',
          'print "UNIVERSAL QUARTIC CONTACT KERNEL VERIFIED: CUBIC TIMES LINEARS";']
    Path(__file__).with_name('quartic_contact.m2').write_text('\n'.join(text).replace('**','^')+'\n')
    print('quartic jets rows:',len(matrix2),len(matrix3),'entry max terms:',max(len(g.R.from_expr(sp.sympify(p)).terms()) for row in matrix2+matrix3 for p in row))

if __name__=='__main__':main()
