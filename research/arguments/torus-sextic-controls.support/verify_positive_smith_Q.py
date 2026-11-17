#!/usr/bin/env python3
"""Exact Q certificate for the degree-12 Smith profiles of two sextic pencils.

Standard library only. Checks ranks modulo v, v^2, v^3, which suffice
to determine all positive Smith exponents without state-weight input.
"""
from fractions import Fraction

def mon(n):
    return [(i,j,k,n-i-j-k) for i in range(n+1)
            for j in range(n-i+1) for k in range(n-i-j+1)]

def add(*polys):
    out={}
    for p in polys:
        for e,c in p.items(): out[e]=out.get(e,0)+c
    return {e:c for e,c in out.items() if c}

def mul(a,b):
    out={}
    for e,c in a.items():
        for f,d in b.items():
            h=tuple(x+y for x,y in zip(e,f))
            out[h]=out.get(h,0)+c*d
    return {e:c for e,c in out.items() if c}

def power(p,n):
    out={(0,0,0,0):1}
    for _ in range(n): out=mul(out,p)
    return out

def scale(p,c):
    return {e:c*v for e,v in p.items() if c*v}

x=[{tuple(int(i==j) for i in range(4)):1} for j in range(4)]
q=add(mul(x[0],x[3]),scale(mul(x[1],x[2]),-1))
A=add(mul(power(x[0],2),x[2]),scale(power(x[1],3),-1))
a0=mul(mul(power(x[0],2),x[3]),A)
a1=add(a0,mul(mul(q,x[0]),A))
g=mul(mul(power(x[0],3),x[2]),q)
c=power(q,3)
lead=max(g)  # Lex leading monomial x0^4*x2*x3
lc=g[lead]

def reduce_g(p):
    p=dict(p)
    while True:
        divisible=[e for e in p if all(e[i]>=lead[i] for i in range(4))]
        if not divisible: return p
        e=max(divisible)
        coeff=Fraction(p[e],lc)
        shift=tuple(e[i]-lead[i] for i in range(4))
        for t,v in g.items():
            z=tuple(t[i]+shift[i] for i in range(4))
            p[z]=p.get(z,0)-coeff*v
            if not p[z]: del p[z]

basis6=[e for e in mon(6) if not all(e[i]>=lead[i] for i in range(4))]
basis12=[e for e in mon(12) if not all(e[i]>=lead[i] for i in range(4))]
assert (len(basis6),len(basis12))==(83,371)
idx={e:i for i,e in enumerate(basis12)}

def columns(poly):
    out=[]
    for e in basis6:
        shifted={tuple(a+b for a,b in zip(t,e)):v for t,v in poly.items()}
        out.append({idx[t]:Fraction(v) for t,v in reduce_g(shifted).items()})
    return out

def rank(cols):
    pivots={}
    for col in cols:
        v=dict(col)
        while v:
            j=min(v)
            coef=v[j]
            if j not in pivots:
                pivots[j]={k:z/coef for k,z in v.items()}
                break
            for k,z in pivots[j].items():
                w=v.get(k,0)-coef*z
                if w: v[k]=w
                else: v.pop(k,None)
    return len(pivots)

def truncated_rank(Acols,Ccols,k):
    out=[]
    m=len(basis12)
    for layer in range(k):
        for j in range(len(basis6)):
            col={layer*m+t:v for t,v in Acols[j].items()}
            if layer+1<k:
                col.update({(layer+1)*m+t:v for t,v in Ccols[j].items()})
            out.append(col)
    return rank(out)

Ccols=columns(c)
expected={0:(74,156,239),1:(80,162,245)}
for tau,a in [(0,a0),(1,a1)]:
    Acols=columns(a)
    ranks=tuple(truncated_rank(Acols,Ccols,k) for k in (1,2,3))
    assert ranks==expected[tau],(tau,ranks)
    defects=tuple(83*k-r for k,r in enumerate(ranks,1))
    # The equality of the last two defects proves that no exponent > 2 occurs.
    assert defects[1]==defects[2]
    ones=2*defects[0]-defects[1]
    twos=defects[1]-defects[0]
    print(f"tau={tau}: ranks={ranks}, defects={defects}, "
          f"Smith positive exponents=(1^{ones},2^{twos})")
# Compute the initial determinant character from actual monomial weights.
# The degree-12 image has the direct-sum presentation g*S_6 + a*R_6
# before parameter-torsion removal.
weights=(-2,-1,1,2)
def wt(e):
    return sum(i*j for i,j in zip(e,weights))
def homogeneous_weight(poly):
    values={wt(e) for e in poly}
    assert len(values)==1,values
    return values.pop()
wg=homogeneous_weight(g)
wq=homogeneous_weight(c)
assert wg==-5 and wq==0
source_weight=sum(wt(e) for e in mon(6))
quotient_weight=sum(wt(e) for e in basis6)
base_weights={}
for tau,a in [(0,a0),(1,a1)]:
    wa=homogeneous_weight(a)
    base_weights[tau]=(source_weight+len(mon(6))*wg
                       +quotient_weight+len(basis6)*wa)
    assert base_weights[tau]==-830
    print(f"tau={tau}: g*S6 weight={source_weight+len(mon(6))*wg}, "
          f"a*R6 weight={quotient_weight+len(basis6)*wa}, "
          f"initial determinant={base_weights[tau]}, "
          f"parameter shift={wq-wa}")

# Derive final characters from independently computed ranks and weights.
for tau,a in [(0,a0),(1,a1)]:
    ranks=tuple(truncated_rank(columns(a),Ccols,k) for k in (1,2,3))
    defects=tuple(83*k-r for k,r in enumerate(ranks,1))
    torsion_length=defects[2]
    final_weight=base_weights[tau]+(wq-homogeneous_weight(a))*torsion_length
    assert final_weight==(-780 if tau==0 else -810)
    print(f"tau={tau}: positive degree-12 determinant weight={final_weight}")
print("All exact rational checks passed.")
