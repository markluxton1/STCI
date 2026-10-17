#!/usr/bin/env python3
"""Actual second ambient obstruction for one smooth compatible root seed.

Accepted exact embedded charts are input. All arithmetic is rational and
normal-degree-truncated. First-order corrections include both base motion
and the equation unit; the second target is the full root-scheme quotient.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

ORDER=4
ONE={(0,0,0):Q(1)}
U={(1,0,0):Q(1)}
V={(0,1,0):Q(1)}

def add(*polys):
    out={}
    for p in polys:
        for mon,c in p.items():
            out[mon]=out.get(mon,Q(0))+c
            if not out[mon]:del out[mon]
    return out

def scale(p,c):return {m:x*c for m,x in p.items() if x*c}

def mul(p,q):
    out={}
    for (u,v,z),c in p.items():
        for (a,b,k),d in q.items():
            if u+v+a+b<=ORDER:
                m=(u+a,v+b,z+k)
                out[m]=out.get(m,Q(0))+c*d
    return {m:c for m,c in out.items() if c}

def power(p,n):
    out=ONE
    for _ in range(n):out=mul(out,p)
    return out

def zpow(n):return {(0,0,n):Q(1)}

def layer(p,n):return {m:c for m,c in p.items() if sum(m[:2])==n}

def encoded(p):return [{"u":u,"v":v,"z":z,"coefficient":str(c)} for (u,v,z),c in sorted(p.items())]

# Accepted exact chart: W=(z^3+v)/(z^4+u+(3/2)zv),
# u'=(z/den-W^3)/2, v'=-3W(z/den-W^3)+2(1/den-W^4).
B=add(U,scale(mul(zpow(1),V),Q(3,2)))
t=mul(zpow(-4),B)
inv=mul(zpow(-4),add(*(scale(power(t,n),Q((-1)**n)) for n in range(ORDER+1))))
W=mul(add(zpow(3),V),inv)
AP=add(mul(zpow(1),inv),scale(power(W,3),Q(-1)))
BP=add(inv,scale(power(W,4),Q(-1)))
UP=scale(AP,Q(1,2))
VP=add(scale(mul(W,AP),Q(-3)),scale(BP,Q(2)))
F=add(mul(add(zpow(2),scale(ONE,Q(4))),power(U,2)),mul(add(zpow(2),scale(ONE,Q(-8))),power(V,2)))
F1P=add(mul(add(ONE,scale(power(W,2),Q(4))),power(UP,2)),mul(add(ONE,scale(power(W,2),Q(-8))),power(VP,2)))
normalized=mul(zpow(16),F1P)
assert layer(normalized,2)==F
# First-order Cech gauge, including beta=2z*epsilon in the equation unit.
L1=add(mul(add(scale(zpow(-4),Q(-5)),scale(zpow(-6),Q(-8))),U),mul(add(scale(zpow(-1),Q(-1,8)),scale(zpow(-3),Q(-11,2))),V))
G0=add(scale(mul(zpow(1),mul(power(U,2),V)),Q(1,8)),scale(mul(U,power(V,2)),Q(-3,4)),scale(mul(zpow(1),power(V,3)),Q(1,8)))
G1P=add(scale(mul(W,power(UP,3)),Q(-32)),scale(mul(power(UP,2),VP),Q(48)),scale(mul(W,mul(UP,power(VP,2))),Q(64)))
first=add(layer(normalized,3),layer(mul(zpow(16),G1P),3),scale(G0,Q(-1)),scale(mul(L1,F),Q(-1)))
assert not first, encoded(first)
R4=add(layer(normalized,4),layer(mul(zpow(16),G1P),4),scale(mul(L1,G0),Q(-1)))
D2={m:c for m,c in R4.items() if -11<=m[2]<=-1}
ROWS=[(4-i,i,k) for i in range(5) for k in range(-11,0)]
COLS=[(2-i,i,k) for i in range(3) for k in range(-13,0)]
A=[[F.get(tuple(row[j]-col[j] for j in range(3)),Q(0)) for col in COLS] for row in ROWS]
rhs=[D2.get(row,Q(0)) for row in ROWS]
# RREF also produces one exact left-annihilator witnessing nonmembership.
aug=[row+[rhs[i]] for i,row in enumerate(A)]
transform=[[Q(int(i==j)) for j in range(55)] for i in range(55)]
rank=0
for j in range(39):
    pivot=next((i for i in range(rank,55) if aug[i][j]),None)
    if pivot is None:continue
    aug[rank],aug[pivot]=aug[pivot],aug[rank]
    transform[rank],transform[pivot]=transform[pivot],transform[rank]
    c=aug[rank][j]
    aug[rank]=[x/c for x in aug[rank]]
    transform[rank]=[x/c for x in transform[rank]]
    for i in range(55):
        if i!=rank and aug[i][j]:
            c=aug[i][j]
            aug[i]=[x-c*y for x,y in zip(aug[i],aug[rank])]
            transform[i]=[x-c*y for x,y in zip(transform[i],transform[rank])]
    rank+=1
assert rank==39
bad=next((i for i in range(rank,55) if aug[i][-1]),None)
certificate=None
if bad is not None:
    lam=transform[bad]
    assert all(sum((lam[i]*A[i][j] for i in range(55)),Q(0))==0 for j in range(39))
    pairing=sum((lam[i]*rhs[i] for i in range(55)),Q(0))
    assert pairing
    certificate={"dual_row":[{"row":i,"monomial":encoded({ROWS[i]:Q(1)})[0],"coefficient":str(c)} for i,c in enumerate(lam) if c],"pairing":str(pairing),"A_rank":rank,"augmented_rank":rank+1}
simple_weights={(3,1,-3):Q(-1),(3,1,-1):Q(8),(1,3,-3):Q(1),(1,3,-1):Q(4)}
simple_dual=[simple_weights.get(row,Q(0)) for row in ROWS]
assert all(sum((simple_dual[i]*A[i][j] for i in range(55)),Q(0))==0 for j in range(39))
simple_pairing=sum((simple_dual[i]*rhs[i] for i in range(55)),Q(0))
assert simple_pairing==Q(1,8)

artifact={
    "status":"new exact second ambient obstruction calculation, independent review required",
    "seed":"f=(z^2+4)u^2+(z^2-8)v^2",
    "accepted_chart_input":"W=(z^3+v)/den, den=z^4+u+(3/2)zv; u'=(z/den-W^3)/2; v'=-3W(z/den-W^3)+2(1/den-W^4)",
    "first_equation_unit_L1":encoded(L1),
    "first_chart_cubic_G0":encoded(G0),
    "second_chart_cubic_G1":"-32*w*u'^3+48*u'^2*v'+64*w*u'*v'^2",
    "first_compatibility_exactly_verified":not first,
    "second_raw_discrepancy":encoded(R4),
    "second_Cech_discrepancy":encoded(D2),
    "target":"coker[H1 O(-14,2) --f--> H1 O(-12,4)], dimensions 39 -> 55 -> 16",
    "source_basis":[{"u":u,"v":v,"z":z} for u,v,z in COLS],
    "target_basis":[{"u":u,"v":v,"z":z} for u,v,z in ROWS],
    "nonzero_certificate":certificate,
    "simple_dual_certificate":{
        "formula":"lambda(r)=coefficient_z^-1[-(z^2-8)*r_(u^3v)+(z^2+4)*r_(uv^3)]",
        "dual_polynomial_vector":"(0,-c,0,a,0)",
        "nonzero_weights":encoded(simple_weights),
        "annihilates_multiplication_by_f":True,
        "pairing":str(simple_pairing)
    },
    "scope":"obstructs this single first-compatible smooth root seed at second exceptional order; no universal smooth-root exclusion or actual-CI bridge asserted"
}
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(artifact,indent=2)+"\n")
print(json.dumps({"artifact":str(path),"rank_A":rank,"obstruction_nonzero":bad is not None,"dual_certificate":certificate,"simple_pairing":str(simple_pairing)},indent=2))
