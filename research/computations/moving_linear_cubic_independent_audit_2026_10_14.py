"""Independent cubic audit in quotient and relation normal coordinates.

The accepted quadratic Laurent discrepancy is an input.  The NEW cubic
calculation is performed directly from the exact embedded chart, before
reading the owner's cubic source.  It uses normal coordinates e,h such that
f0=h and ell0=e, rather than dividing a degree-two binary form by f0.

Run with Python's standard library only.  Output records the complete cubic
Laurent polynomial, the retained Cech class, and the exact diagonal-field
reduction.  No numerical sample, finite-field test, or inherited checker is
used.
"""
from fractions import Fraction as F
from collections import defaultdict

# Exact normal-degree <= 3 algebra in e,h, with Laurent z,t coefficients.
# No accepted quadratic formula is recomputed; its T is imported as a premise.
def clean(p):
    return {m:F(c) for m,c in p.items() if c and m[0]+m[1] <= 3}
def mon(e=0,h=0,z=0,t=0,c=1):
    return {(e,h,z,t):F(c)} if c else {}
def add(*ps):
    o=defaultdict(F)
    for p in ps:
        for m,c in p.items(): o[m]+=c
    return clean(o)
def scale(p,c): return clean({m:v*F(c) for m,v in p.items()})
def mul(*ps):
    o=mon()
    for p in ps:
        n=defaultdict(F)
        for a,c in o.items():
            for b,d in p.items():
                m=tuple(x+y for x,y in zip(a,b))
                if m[0]+m[1] <= 3: n[m]+=c*d
        o=clean(n)
    return o
def powp(p,n):
    o=mon()
    for _ in range(n): o=mul(o,p)
    return o
def neg(p): return scale(p,-1)
def extract(p,e,h):
    return {(0,0,z,t):c for (i,j,z,t),c in p.items() if (i,j)==(e,h)}
def show(p):
    return '\n'.join(f'z^{z} t^{t}: {c}' for (e,h,z,t),c in sorted(p.items(), key=lambda x:(x[0][2],x[0][3])) ) or '0'
z=mon(z=1); t=mon(t=1); one=mon(); eps=mon(e=1); eta=mon(h=1)

def calculate(label,A,B,C,D,delta_inv):
    a=add(A,mul(C,z)); b=add(B,mul(D,z))
    delta=add(mul(A,D),neg(mul(B,C)))
    # Accepted T formula, needed only to select the specified local corrections.
    T=add(mul(mon(z=-5,c=3),powp(b,3)),
          mul(mon(z=-4,c=F(-3,2)),a,powp(b,2)),
          mul(mon(z=-3,c=F(3,4)),powp(a,2),b),
          mul(mon(z=-2,c=F(-3,8)),powp(a,3)),
          neg(mul(delta,mon(z=-3),b)),
          mul(delta,mon(z=-2,c=F(1,2)),a))
    q0={m:c for m,c in T.items() if m[2]>=0}
    q1_dict={(-m[2]-4,m[3]):-c for m,c in T.items() if m[2]<=-4}
    # u=b e+D/delta h, v=-a e-C/delta h: f0=h, ell0=e.
    u=add(mul(b,eps),mul(D,delta_inv,eta))
    v=add(neg(mul(a,eps)),neg(mul(C,delta_inv,eta)))
    borig=add(u,mul(mon(z=1,c=F(3,2)),v))
    av=mul(borig,mon(z=-4))
    inv=mul(mon(z=-4),add(*[scale(powp(av,j),(-1)**j) for j in range(4)]))
    W=mul(add(mon(z=3),v),inv)
    ap=add(mul(z,inv),neg(powp(W,3)))
    bp=add(inv,neg(powp(W,4)))
    up=scale(ap,F(1,2))
    vp=add(scale(mul(W,ap),-3),scale(bp,2))
    f0=add(mul(a,u),mul(b,v))
    f1=add(mul(add(mul(A,W),C),up),mul(add(mul(B,W),D),vp))
    ell0=mul(delta_inv,neg(add(mul(C,u),mul(D,v))))
    ell1=mul(delta_inv,add(mul(A,up),mul(B,vp)))
    q1W=add(*[mul(mon(t=k,c=c),powp(W,j)) for (j,k),c in q1_dict.items()])
    F0=add(f0,mul(q0,powp(ell0,2)))
    F1=add(f1,mul(q1W,powp(ell1,2)))
    overlap=add(mul(mon(z=8),F1),neg(F0))
    L2eval=extract(overlap,1,1)
    D3eval=extract(overlap,3,0)
    cubic=add(D3eval,neg(mul(q0,L2eval)))
    retained={m:c for m,c in cubic.items() if -9<=m[2]<=-1}
    print('\nCASE',label)
    print('q0\n'+show(q0))
    print('q1 terms [w exponent,t exponent]:'+str(sorted(q1_dict.items())))
    print('quadratic pure quotient\n'+show(extract(overlap,2,0)))
    print('L2eval\n'+show(L2eval))
    print('D3eval\n'+show(D3eval))
    print('corrected cubic\n'+show(cubic))
    print('retained\n'+show(retained))
    return cubic,retained

diag,dr=calculate('diagonal',t,{}, {},one,mon(t=-1))
conic,cr=calculate('conic',mon(c=2),t,mon(t=-1,c=8),one,mon(c=F(-1,6)))

def reduce_quad_t(p):
    # t^2=(4/3)t-4 and t^-1=1/3-t/4 in Q[t]/(3t^2-4t+12).
    def qmul(x,y):
        a,b=x; c,d=y
        return (a*c-4*b*d,a*d+b*c+F(4,3)*b*d)
    def tp(n):
        x=(F(1),F(0)); y=(F(0),F(1)) if n>=0 else (F(1,3),F(-1,4))
        for _ in range(abs(n)): x=qmul(x,y)
        return x
    out=defaultdict(F)
    for (e,h,z,tt),c in p.items():
        a,b=tp(tt); out[(e,h,z,0)]+=c*a; out[(e,h,z,1)]+=c*b
    return clean(out)
def eval_t(p,tval):
    out=defaultdict(F)
    for (e,h,z,tt),c in p.items(): out[(e,h,z,0)]+=c*F(tval)**tt
    return clean(out)
print('\ndiagonal t=2 corrected retained\n'+show(eval_t(dr,2)))
print('\ndiagonal quadratic field corrected retained\n'+show(reduce_quad_t(dr)))

# Exact conclusions of the NEW cubic calculation.  The nonquadric diagonal
# reduction is in the full quadratic number field; conic formulas hold for
# an indeterminate invertible t, hence for every point of the open conic.
assert not eval_t(dr, 2)
assert reduce_quad_t(dr) == add(mon(z=-5,c=F(64,9)),mon(z=-5,t=1,c=F(-64,27)))
assert cr == add(mon(z=-1,t=-4,c=512),mon(z=-2,t=-3,c=-384),
                 mon(z=-3,t=-2,c=64),mon(z=-7,t=2,c=4),
                 mon(z=-8,t=3,c=-6),mon(z=-9,t=4,c=2))
print('\nPASS: exact cubic diagonal and open-conic identities')
