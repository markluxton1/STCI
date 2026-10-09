#!/usr/bin/env python3
"""Independent root-matrix/cycle enumeration for the reduced normal lane.

This implementation does not import the first normal-carrier companion.
It verifies numerical implications, not the cited geometric classification.
"""
from fractions import Fraction
from math import gcd,lcm
from pathlib import Path
import json
import sympy as sp

def inverse_column(A,j):
    x=A.inv()[:,j]
    return Fraction(x[j]),lcm(*(int(a.q) for a in x))

ade=[]
for n in range(1,12):
    A=sp.diag(*([2]*n))
    for i in range(n-1): A[i,i+1]=A[i+1,i]=-1
    inv=A.inv()
    for k in range(1,(n+1)//2+1):
        col=inv[:,k-1];q=Fraction(col[k-1]);index=lcm(*(int(a.q) for a in col))
        assert q==Fraction(k*(n+1-k),n+1)
        assert index==(n+1)//gcd(n+1,k)
        ade.append((n,k,q,index,f'A{n}^{k}'))
for n in range(4,12):
    A=sp.diag(*([2]*n))
    for i in range(n-3):A[i,i+1]=A[i+1,i]=-1
    for j in (n-2,n-1):A[n-3,j]=A[j,n-3]=-1
    for j,s,q0,idx0,label in [(0,2,Fraction(1),2,f'D{n}^1'),
                              (n-1,n//2,Fraction(n,4),2 if n%2==0 else 4,f'D{n}^spin')]:
        q,idx=inverse_column(A,j)
        assert (q,idx)==(q0,idx0)
        ade.append((n,s,q,idx,label))
# Standard E_n T diagram: arms of lengths 2,1,n-4 from a center.
for n,s,q0,idx0,label in [(6,2,Fraction(4,3),3,'E6'),(7,3,Fraction(3,2),2,'E7')]:
    A=sp.diag(*([2]*n));prev=0;nxt=1;ends=[]
    for length in [2,1,n-4]:
        prev=0
        for _ in range(length):
            A[prev,nxt]=A[nxt,prev]=-1;prev=nxt;nxt+=1
        ends.append(prev)
    matched=[inverse_column(A,j) for j in ends]
    assert (q0,idx0) in matched
    ade.append((n,s,q0,idx0,label))

states=[]
def rec(start,N,P,q,index,names):
    states.append((N,P,q,index,names))
    for i in range(start,len(ade)):
        n,s,x,idx,name=ade[i]
        if N+n<=11 and P+s<=7:
            rec(i,N+n,P+s,q+x,lcm(index,idx),names+(name,))
rec(0,0,0,Fraction(0),1,())
print('ADE states',len(states),flush=True)

def compositions(d,k):
    if k==1:
        yield (d,);return
    for i in range(d+1):
        for tail in compositions(d-i,k-1):yield (i,)+tail

found={}
for d in range(1,4):
    for k in range(2,10+d):
        for extra in compositions(d,k):
            weights=tuple(x+2 for x in extra)
            # Rotate/reflect both the weights and selected vertex later.
            A=sp.diag(*weights)
            if k==2:A[0,1]=A[1,0]=-2
            else:
                for i in range(k):A[i,(i+1)%k]=A[(i+1)%k,i]=-1
            inv=A.inv()
            for j in range(k):
                cyc=weights[j:]+weights[:j]
                cyc=min(cyc,(cyc[0],)+tuple(reversed(cyc[1:])))
                qi=Fraction(inv[j,j]);idx=lcm(*(int(x.q) for x in inv[:,j]))
                for N,P,q,index,names in states:
                    if N<=9+d-k and q==5-qi:
                        key=(d,k,cyc,qi,idx,names)
                        found[key]=lcm(idx,index)
    print('d',d,'cumulative survivors',len(found),flush=True)
out=[]
for (d,k,cyc,qi,idx,names),degree in sorted(found.items()):
    row={'d':d,'k':k,'weights_from_selected':cyc,'q_irr':str(qi),'cycle_index':idx,'ADE':names,'degree':degree}
    out.append(row);print(row,flush=True)
assert len(found)==5
assert sorted(found.values())==[2,2,2,2,6]
(Path(__file__).resolve().parents[1] / 'scratch/session_normal_independent_audit.json').write_text(json.dumps(out,indent=2)+'\n')
