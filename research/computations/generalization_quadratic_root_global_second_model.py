#!/usr/bin/env python3
"""One global K1+K2 model, with 25 complete dual tests and no coefficient chart.

The accepted full embedded chart is input. Rational sparse arithmetic only.
No accepted seed or rank verifier is rerun. Output is one characteristic-zero
Macaulay2 ideal on the homogeneous smooth-discriminant open.
"""
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import json

NAMES=[f'{l}{j}' for l in 'abc' for j in range(3)]+[f'h{j}' for j in range(12)]
# A coefficient polynomial maps a sorted tuple of variable indices to Q.
def ca(*polys):
    out={}
    for p in polys:
        for m,c in p.items():
            out[m]=out.get(m,Q(0))+c
            if not out[m]:del out[m]
    return out

def cs(p,c):return {m:c*x for m,x in p.items() if c*x}
def cm(p,q):
    out={}
    for a,c in p.items():
        for b,d in q.items():
            m=tuple(sorted(a+b));out[m]=out.get(m,Q(0))+c*d
    return {m:c for m,c in out.items() if c}
def cp(p,n):
    out={():Q(1)}
    for _ in range(n):out=cm(out,p)
    return out

def const(c):return {():Q(c)} if c else {}
def var(i):return {(i,):Q(1)}

# Laurent normal polynomials: (u degree,v degree,z exponent) -> coefficient.
def pa(*polys):
    out={}
    for p in polys:
        for m,c in p.items():
            value=ca(out.get(m,{}),c)
            if value:out[m]=value
            elif m in out:del out[m]
    return out

def ps(p,c):return {m:cs(x,c) for m,x in p.items() if cs(x,c)}
def pm(p,q):
    out={}
    for (u,v,z),c in p.items():
        for (a,b,k),d in q.items():
            if u+v+a+b<=4:
                m=(u+a,v+b,z+k)
                value=ca(out.get(m,{}),cm(c,d))
                if value:out[m]=value
                elif m in out:del out[m]
    return out

def pp(p,n):
    out={(0,0,0):const(1)}
    for _ in range(n):out=pm(out,p)
    return out

def mono(u=0,v=0,z=0,c=1):return {(u,v,z):const(c)}
def layer(p,n):return {m:c for m,c in p.items() if sum(m[:2])==n}

def ceval(p,values):
    return sum((c*__import__('functools').reduce(lambda x,i:x*values[i],m,Q(1)) for m,c in p.items()),Q(0))

def fmt(p):
    terms=[]
    for m,c in sorted(p.items(),key=lambda x:(len(x[0]),x[0])):
        factors='*'.join(NAMES[i] for i in m)
        coefficient='' if abs(c)==1 and factors else str(abs(c))
        terms.append(('-' if c<0 else '+')+coefficient+('*' if coefficient and factors else '')+factors)
    s=''.join(terms)
    return s[1:] if s.startswith('+') else (s or '0')

ONE=mono();U=mono(u=1);V=mono(v=1)
# Accepted full embedded transition, truncated only at the needed new order.
B=pa(U,ps(pm(mono(z=1),V),Q(3,2)))
t=pm(mono(z=-4),B)
inv=pm(mono(z=-4),pa(*(ps(pp(t,n),Q((-1)**n)) for n in range(5))))
W=pm(pa(mono(z=3),V),inv)
AP=pa(pm(mono(z=1),inv),ps(pp(W,3),Q(-1)))
BP=pa(inv,ps(pp(W,4),Q(-1)))
UP=ps(AP,Q(1,2));VP=pa(ps(pm(W,AP),Q(-3)),ps(BP,Q(2)))
F={}
FP={}
for i in range(3):
    for j in range(3):
        F=pa(F,{(2-i,i,j):var(3*i+j)})
        basis=pm(pp(W,2-j),pm(pp(UP,2-i),pp(VP,i)))
        FP=pa(FP,{m:cm(c,var(3*i+j)) for m,c in basis.items()})
NF=pm(mono(z=16),FP)
assert layer(NF,2)==F
H={}
for i in range(2):
    for j,k in enumerate(range(-6,0)):
        H=pa(H,{(1-i,i,k):var(9+6*i+j)})
BETA=pa(mono(u=1,z=-4,c=-2),mono(v=1,z=-3,c=-1))
L1=pa(H,BETA)
S3=pa(layer(NF,3),ps(pm(L1,F),Q(-1)))
FIRST_ROWS=[(3-i,i,k) for i in range(4) for k in range(-4,0)]
FIRST=[S3.get(row,{}) for row in FIRST_ROWS]
G0={m:c for m,c in S3.items() if m[2]>=0}
G1P={}
for (u,v,z),coefficient in S3.items():
    if z<=-5:
        assert -z-5 in (0,1)
        pull=pm(pp(W,-z-5),pm(pp(UP,u),pp(VP,v)))
        G1P=pa(G1P,{m:cs(cm(c,coefficient),Q(-1)) for m,c in pull.items()})
assert max((m[2] for m in G0),default=0)<=1
R4=pa(layer(NF,4),layer(pm(mono(z=16),G1P),4),ps(pm(L1,G0),Q(-1)))
R4={m:c for m,c in R4.items() if -11<=m[2]<=-1}

# Each p below is a polynomial in z (u=v=0) with coefficient polynomials.
ABC=[{(0,0,j):var(3*i+j) for j in range(3)} for i in range(3)]
ZERO={}
T=[[ABC[0],ABC[1],ABC[2],ZERO,ZERO],[ZERO,ABC[0],ABC[1],ABC[2],ZERO],[ZERO,ZERO,ABC[0],ABC[1],ABC[2]]]
def det3(matrix):
    out={}
    for perm in permutations(range(3)):
        inversions=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        term=ONE
        for i,j in enumerate(perm):term=pm(term,matrix[i][j])
        out=pa(out,ps(term,Q((-1)**inversions)))
    return out
K=[[{} for j in range(5)] for i in range(5)]
for i in range(5):
    for j in range(i+1,5):
        cols=[c for c in range(5) if c not in (i,j)]
        minor=det3([[T[r][c] for c in cols] for r in range(3)])
        K[i][j]=ps(minor,Q((-1)**(i+j+1)))
        K[j][i]=ps(K[i][j],Q(-1))
# New-model consistency: all Plucker columns are genuine universal syzygies.
for row in range(3):
    for col in range(5):
        assert not pa(*(pm(T[row][j],K[j][col]) for j in range(5)))
SECOND=[]
for col in range(5):
    for shift in range(5):
        residue={}
        for i in range(5):
            for (_,_,z),q in K[i][col].items():
                r=R4.get((4-i,i,-1-shift-z),{})
                residue=ca(residue,cm(q,r))
        SECOND.append(residue)

# Homogeneous binary quartic discriminant: no degree-four affine assumption.
DELTA=pa(pm(ABC[1],ABC[1]),ps(pm(ABC[0],ABC[2]),Q(-4)))
d=[DELTA.get((0,0,j),{}) for j in range(5)]
I=ca(cs(cm(d[4],d[0]),Q(12)),cs(cm(d[3],d[1]),Q(-3)),cp(d[2],2))
J=ca(cs(cm(cm(d[4],d[2]),d[0]),Q(72)),cs(cm(cm(d[3],d[2]),d[1]),Q(9)),cs(cm(d[4],cp(d[1],2)),Q(-27)),cs(cm(cp(d[3],2),d[0]),Q(-27)),cs(cp(d[2],3),Q(-2)))
DISC=cs(ca(cs(cp(I,3),Q(4)),cs(cp(J,2),Q(-1))),Q(1,27))
assert all(len(m)==12 for m in DISC)

stem=Path(__file__).with_suffix('')
model=stem.with_suffix('.m2')
lines=[
'-- One global characteristic-zero K1+K2 incidence, no coefficient chart.',
'-- First/second classes are accepted inputs; this is a new dual compression.',
'R=QQ['+','.join(NAMES+['smoothInverse'])+',MonomialOrder=>GRevLex];',
'firstEquations={'+','.join(fmt(p) for p in FIRST)+'};',
'secondEquations={'+','.join(fmt(p) for p in SECOND)+'};',
'smoothDiscriminant='+fmt(DISC)+';',
'globalSecondIdeal=ideal join(firstEquations,secondEquations,{smoothInverse*smoothDiscriminant-1});',
'print("MODEL_READY: 16 first equations, 25 complete second dual equations, one smooth inverse");',
'print("NO_ELIMINATION_RUN_BY_INPUT_FILE");'
]
model.write_text('\n'.join(lines)+'\n')
meta={
'status':'new global exact model; proof/audit in paired note; no emptiness claimed',
'variables':NAMES+['smoothInverse'],
'first_equations':len(FIRST),'second_dual_equations':len(SECOND),
'first_term_counts':[len(p) for p in FIRST],
'second_term_counts':[len(p) for p in SECOND],
'second_max_total_degree':max((len(m) for p in SECOND for m in p),default=0),
'discriminant_terms':len(DISC),'discriminant_homogeneous_degree':12,
'smoothness':'Disc_homogeneous_binary_quartic(b^2-4ac) != 0, allowing affine leading coefficient zero',
'ideal':'16 first equations +25 complete Plucker dual residues +smoothInverse*Disc-1',
'first_corrections':'L1=h+beta; G0=nonnegative_z(S3); G1=-z^5*negative_z_at_most_-5(S3), converted to second chart',
'R4':'pr_-11..-1([z^16(f1+G1)]_4-L1*G0)',
'Plucker_identity_TK_verified_exactly':True,
'no_seed_or_old_rank_verifier_run':True,
'model_file':str(model),
'limitations':'Model export only. No global Groebner result or effective empty stage asserted.'
}
stem.with_suffix('.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2))
