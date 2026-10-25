#!/usr/bin/env python3
"""Finite exact polynomial checks for the exploratory root pencil; stdlib only.

No global geometry, completeness, flatness, or extremality is inferred by this
script. Run from any directory; optional first argument selects a JSON output.
"""
from itertools import permutations
import json
from pathlib import Path
import sys

# Sparse polynomials in a,z,u,y,s,t, all with integer coefficients.
NV = 6
def const(n): return {(0,)*NV: n} if n else {}
def var(i):
    e = [0]*NV; e[i] = 1
    return {tuple(e): 1}
def add(*ps):
    r = {}
    for p in ps:
        for e, c in p.items(): r[e] = r.get(e, 0)+c
    return {e:c for e,c in r.items() if c}
def scale(p, c): return {e:v*c for e,v in p.items() if v*c}
def sub(p, q): return add(p, scale(q, -1))
def mul(p, q):
    r = {}
    for e,c in p.items():
        for f,d in q.items():
            ef = tuple(x+y for x,y in zip(e,f)); r[ef] = r.get(ef,0)+c*d
    return {e:c for e,c in r.items() if c}
def power(p,n):
    r=const(1)
    for _ in range(n): r=mul(r,p)
    return r
def determinant(matrix):
    n=len(matrix); ans={}
    for perm in permutations(range(n)):
        inv=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        term=const(-1 if inv%2 else 1)
        for i,j in enumerate(perm):
            term=mul(term,matrix[i][j])
            if not term: break
        ans=add(ans,term)
    return ans

a,z,u,y,s,t=[var(i) for i in range(NV)]
one=const(1)
f=add(power(z,4),scale(mul(a,z),-1),a,const(-1))
residual=add(power(z,3),power(z,2),z,one,scale(a,-1))
checks={}
checks['fixed_root_factorization']=f==mul(sub(z,one),residual)
# On f(z)=0, z^4=a*z+1-a; this identifies the two endpoint
# leading-coefficient configurations by z -> z/(a*z+1-a).
checks['endpoint_mobius_relation']=not add(f, scale(a,-1), one, mul(a,z), scale(power(z,4),-1))
# Resultant(f,f') = discriminant(f), since monic degree4 has sign (+).
fc=[one,{}, {},scale(a,-1),sub(a,one)]
dc=[const(4),{}, {},scale(a,-1)]
zero={}
M=[]
for shift in range(3): M.append([zero]*shift+fc+[zero]*(2-shift))
for shift in range(4): M.append([zero]*shift+dc+[zero]*(3-shift))
disc=determinant(M)
expected=add(scale(power(sub(a,one),3),256),scale(power(a,4),-27))
factored=mul(power(sub(a,const(4)),2),add(scale(power(a,2),-27),scale(a,40),const(-16)))
checks['discriminant_formula']=disc==expected
checks['discriminant_factorization']=disc==factored
f4=add(power(z,4),scale(z,-4),const(3))
checks['double_C_at_a4']=f4==mul(power(sub(z,one),2),add(power(z,2),scale(z,2),const(3)))
checks['a1_zero_root']=add(power(z,4),scale(z,-1))==mul(z,sub(power(z,3),one))
# Expansion f(1+h) = (4-a)h+6h2+4h3+h4.
h=sub(z,one)
checks['translated_polynomial']=f==add(mul(sub(const(4),a),h),scale(power(h,2),6),scale(power(h,3),4),power(h,4))
# The cubic transform has a2=6,a4=4b,a6=b2, b=4-a.
b=sub(const(4),a)
b2=const(24); b4=scale(b,8); b6=scale(power(b,2),4)
c4=sub(power(b2,2),scale(b4,24))
c6=add(scale(power(b2,3),-1),scale(mul(b2,b4),36),scale(b6,-216))
checks['elliptic_c4']=c4==scale(sub(a,one),192)
checks['elliptic_c6']=c6==scale(power(a,2),-864)
checks['elliptic_discriminant']=sub(power(c4,3),power(c6,2))==scale(disc,1728*16)
checks['j_numerator']=power(c4,3)==scale(power(sub(a,one),3),1728*16*256)
# Parametric evaluation of G_a on C_lambda yields s4*t12*f(lambda).
x0=power(s,4); x1=mul(power(s,3),t); x2=mul(mul(z,s),power(t,3)); x3=power(t,4)
Ga=add(power(x2,4),scale(mul(mul(mul(a,x1),x2),power(x3,2)),-1),mul(mul(sub(a,one),x0),power(x3,3)))
checks['homogeneous_branch_equation']=Ga==mul(mul(power(s,4),power(t,12)),f)
# Determinant derivative along the marked root: f'(1)=4-a.
checks['marked_root_derivative']=sub(const(4),a)==b
out={'scope':'Finite exact identities only; geometry remains an exploratory proposal.', 'checks':checks,'passed':sum(checks.values()),'total':len(checks), 'formulas':{'root_polynomial':'z^4-a*z+a-1','discriminant':'(a-4)^2*(-27*a^2+40*a-16)','elliptic_j':'1728*256*(a-1)^3/(256*(a-1)^3-27*a^4)'}}
if not all(checks.values()): raise AssertionError(out)
encoded=json.dumps(out,indent=2)+'\n'
if len(sys.argv)>1: Path(sys.argv[1]).write_text(encoded)
print(encoded,end='')
