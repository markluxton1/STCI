#!/usr/bin/env python3
"""Universal degree-two primitive fourth obstruction, polynomial arithmetic."""
from pathlib import Path
import json
import sympy as sp
from sympy.polys.rings import ring
from sympy.polys.domains import QQ

R, a0,a1,a2,b0,b1,b2,r = ring('a0,a1,a2,b0,b1,b2,r',QQ)
zero=R.zero
one=R.one
N=4

# Laurent polynomials in z, with coefficient ring R.
def lp(coeff=1,exp=0): return {exp:R(coeff)} if coeff else {}
def add(*xs):
    out={}
    for x in xs:
        for e,c in x.items():
            out[e]=out.get(e,zero)+c
            if not out[e]: del out[e]
    return out
def neg(x): return {e:-c for e,c in x.items()}
def smul(c,x): return {e:R(c)*v for e,v in x.items() if c*v}
def shift(e,x): return {i+e:c for i,c in x.items()}
def mul(x,y):
    out={}
    for i,c in x.items():
        for j,d in y.items(): out[i+j]=out.get(i+j,zero)+c*d
    return {e:c for e,c in out.items() if c}
def plus(*xs): return [add(*(x[j] for x in xs)) for j in range(N)]
def scale(c,x): return [smul(c,v) for v in x]
def zscale(e,x): return [shift(e,v) for v in x]
def prod(x,y): return [add(*(mul(x[i],y[j-i]) for i in range(j+1))) for j in range(N)]
def power(x,n):
    out=[lp()]+[{} for _ in range(N-1)]
    for _ in range(n): out=prod(out,x)
    return out
def evalpoly(p,x):
    # p is an ordinary polynomial in w represented by exponent map.
    return plus(*(scale(c,power(x,n)) for n,c in p.items())) if p else [{} for _ in range(N)]
def derivative(p): return {i-1:i*c for i,c in p.items() if i}

def bezout(A,B):
    aa=[A.get(i,zero) for i in range(3)]
    bb=[B.get(i,zero) for i in range(3)]
    M=sp.Matrix([[aa[0].as_expr(),0,bb[0].as_expr(),0],
                 [aa[1].as_expr(),aa[0].as_expr(),bb[1].as_expr(),bb[0].as_expr()],
                 [aa[2].as_expr(),aa[1].as_expr(),bb[2].as_expr(),bb[1].as_expr()],
                 [0,aa[2].as_expr(),0,bb[2].as_expr()]])
    det=R.from_expr(sp.expand(M.det()))
    nums=[R.from_expr(sp.expand(M.cofactor(0,i))) for i in range(4)]
    return det,{0:nums[0]*r,1:nums[1]*r},{0:nums[2]*r,1:nums[3]*r}

def ambient(u,v):
    a=v
    b=plus(u,zscale(1,scale(QQ(3,2),v)))
    nb=zscale(-4,b)
    inv=zscale(-4,plus(*(scale((-1)**j,power(nb,j)) for j in range(N))))
    W=prod(plus([lp(1,3)]+[{} for _ in range(N-1)],a),inv)
    up=scale(QQ(1,2),plus(zscale(1,inv),scale(-1,power(W,3))))
    vp=plus(zscale(1,scale(-3,prod(W,inv))),power(W,4),scale(2,inv))
    return W,up,vp

def reduce_inverse(p,det):
    # Cancel resultant*r-1 exactly: return numerator with denominator det^d.
    d=max((m[6] for m,c in p.terms()),default=0)
    out=zero
    for m,c in p.terms():
        m=list(m);j=m[6];m[6]=0
        out+=R.from_dict({tuple(m):c})*det**(d-j)
    # Remove resultant factors shared by numerator and denominator.
    while d:
        q,rem=divmod(out,det)
        if rem: break
        out=q;d-=1
    return out,d

def main():
    A={0:a0,1:a1,2:a2};B={0:b0,1:b1,2:b2}
    Av={0:a2,1:a1,2:a0};Bv={0:b2,1:b1,2:b0}
    det,S,T=bezout(A,B)
    detv,Sv,Tv=bezout(Av,Bv)
    assert detv==det
    W,up,vp=ambient([{},A,{},{}],[{},B,{},{}])
    mp=plus(prod(evalpoly(Bv,W),up),scale(-1,prod(evalpoly(Av,W),vp)))
    assert not mp[1]
    h2=shift(9,mp[2])
    gu={e:c for e,c in h2.items() if e>=0}
    gv={-e-1:-c for e,c in h2.items() if e<0}
    U2=neg(mul(T,gu));V2=mul(S,gu)
    W,up,vp=ambient([{},A,U2,{}],[{},B,V2,{}])
    mp=plus(prod(evalpoly(Bv,W),up),scale(-1,prod(evalpoly(Av,W),vp)))
    ep=plus(prod(evalpoly(Sv,W),up),prod(evalpoly(Tv,W),vp))
    assert all(reduce_inverse(c,det)[0]==0 for c in add(ep[1],lp(-1,-5)).values())
    gv0={-e:c for e,c in gv.items()}
    gv1=mul({-e:c for e,c in derivative(gv).items()},W[1])
    assert all(reduce_inverse(c,det)[0]==0 for c in add(mp[2],shift(-10,gv0)).values())
    h3=shift(9,add(mp[3],shift(-5,smul(2,mul(gv0,ep[2]))),shift(-10,gv1)))
    coords=[reduce_inverse(h3.get(-j,zero),det) for j in range(1,6)]
    print('resultant:',det)
    print('coordinate terms and denominator powers:',[(len(p.terms()),d) for p,d in coords])
    out={'variables':['a0','a1','a2','b0','b1','b2'],
         'resultant':str(det.as_expr()),
         'coordinates':[{'numerator':str(p.as_expr()),'denominator_power':d} for p,d in coords],
         'h2':{str(e):str(c.as_expr()) for e,c in sorted(h2.items())},
         'gu':{str(e):str(c.as_expr()) for e,c in sorted(gu.items())},
         'gv':{str(e):str(c.as_expr()) for e,c in sorted(gv.items())}}
    Path(__file__).with_name('equations.json').write_text(json.dumps(out,indent=2)+'\n')
    m2=['S=QQ[a0,a1,a2,b0,b1,b2,MonomialOrder=>GRevLex];',f'D={det.as_expr()};',
        'I=ideal('+','.join(str(p.as_expr()) for p,d in coords)+');',
        'K=ideal(2*a1+b0,2*a2+b1);',
        'assert(gens I % K == 0);',
        'assert(D^3*(2*a1+b0)^3 % I == 0);',
        'assert(D^3*(2*a2+b1)^3 % I == 0);',
        'print "ALL-DIRECTION PRIMITIVE-FOURTH ZERO LOCUS VERIFIED";',
        'print K;']
    Path(__file__).with_name('classify.m2').write_text('\n'.join(m2).replace('**','^')+'\n')

if __name__=='__main__':main()
