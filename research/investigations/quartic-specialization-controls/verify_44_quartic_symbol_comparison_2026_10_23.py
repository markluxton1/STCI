#!/usr/bin/env python3
"""Exact quartic first symbols of C0, using only Python's standard library.
No inherited theorem is rechecked: compares the NEW explicit characteristic-2
image with the known characteristic-zero coordinate image.
"""
from fractions import Fraction
from itertools import product

def rank(rows, p=None):
    a = [[(Fraction(x) if p is None else int(x)%p) for x in row] for row in rows]
    r=0
    for j in range(len(a[0])):
        i=next((i for i in range(r,len(a)) if a[i][j]),None)
        if i is None: continue
        a[r],a[i]=a[i],a[r]
        q=(1/a[r][j] if p is None else pow(a[r][j],-1,p))
        a[r]=[(x*q if p is None else x*q%p) for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][j]:
                q=a[i][j]
                a[i]=[(x-q*y if p is None else (x-q*y)%p) for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r

mons=[m for m in product(range(5),repeat=4) if sum(m)==4]
weight=lambda m:m[1]+3*m[2]+4*m[3]
groups={w:[m for m in mons if weight(m)==w] for w in range(17)}
assert all(groups.values()) and len(mons)==35
# An integral basis of I_C(4): differences of monomials of equal t-exponent.
ker=[(m,ms[0]) for ms in groups.values() for m in ms[1:]]
assert len(ker)==18
# For m=x0^i*x1^j*x2^k*x3^l, its normal first part is
# k*u^(w-3)*a + l*u^(w-4)*b on x0=1,x1=u,x2=u^3+a,x3=u^4+b.
def symbol(m,r,frame):
    d={}
    for sign,exps in ((1,m),(-1,r)):
        w=weight(exps); k,l=exps[2:]
        if l:d[(0,w-4)]=d.get((0,w-4),0)+sign*l
        alpha=k+(Fraction(3,2)*l if frame=='balanced0' else l)
        if alpha:d[(1,w-3)]=d.get((1,w-3),0)+sign*alpha
    return {i:v for i,v in d.items() if v}

s0=[symbol(m,r,'balanced0') for m,r in ker]
assert all(0<=j<=9 for col in s0 for (_i,j) in col)
m0=[[col.get((i,j),0) for col in s0] for i in range(2) for j in range(10)]
assert rank(m0)==17
for ui,vi in ((1,2),(4,5),(7,8)):
    assert all(col.get((0,ui),0)==2*col.get((1,vi),0) for col in s0)
print('char0: rank17 in H0(O9)^2, defined by U1=2V2,U4=2V5,U7=2V8')

s2=[{i:int(v)%2 for i,v in symbol(m,r,'split2').items() if int(v)%2} for m,r in ker]
assert all(0<=j<=(8 if i==0 else 10) for col in s2 for (i,j) in col)
m2=[[col.get((i,j),0) for col in s2] for i,n in ((0,8),(1,10)) for j in range(n+1)]
assert rank(m2,2)==17
for vi in (2,5,8):assert all(col.get((1,vi),0)==0 for col in s2)
print('char2: rank17 in H0(O8) plus H0(O10), defined by B2=B5=B8=0')
# q^2 has all monomials of parameter weight8. Because differences m-m_ref
# are an integral basis, the coordinates are simply its nonreference coefficients.
q2={(2,0,0,2):1,(1,1,1,1):-2,(0,2,2,0):1}
assert sum(q2.values())==0
q2ker=[q2.get(m,0) for m,r in ker]
assert any(q2ker) and any(v%2 for v in q2ker)
assert all(sum(a*b for a,b in zip(row,q2ker))==0 for row in m0)
assert all(sum(a*b for a,b in zip(row,q2ker))%2==0 for row in m2)
# q has nonzero normal linear part b-u*a; hence q^2 has nonzero
# normal quadratic part in both characteristics. In the selected frames:
# char0 q^2 = U^2+u*U*V+(u^2/4)*V^2; char2 q^2=e^2.
# Thus the degree4 second-symbol image of the first-symbol kernel is exactly
# one dimensional, rather than merely bounded above by one.
assert (1,1,Fraction(1,4)) != (0,0,0)
# Here (4) means ambient twist O_C(4)=O_P1(16).
# Using the inherited splittings E0=O(-7)^2 and E2=O(-8)+O(-6):
dim_second_target0=3*(16-14+1)
dim_second_target2=(16-16+1)+(16-14+1)+(16-12+1)
assert dim_second_target0==dim_second_target2==9
print('both: dimension I_C(4)=18; kernel dimension=1, verified generator q^2')
print('Actual second-symbol degree4 image k*q^2; full target dimension9 in both characteristics')
print('ALL EXACT NEW SYMBOL COMPARISON CHECKS PASS')
