#!/usr/bin/env python3
"""Exact global-source, ruling-line, and boundary identities; stdlib only.

The Macaulay2 companion checks projective schemes. This file checks explicit
polynomial identities and squarefreeness, not global genericity or flatness.
"""
from fractions import Fraction
import json
from pathlib import Path

NV=6

def const(n): return {(0,)*NV:n} if n else {}
def var(i):
    e=[0]*NV; e[i]=1; return {tuple(e):1}
def add(*polys):
    out={}
    for p in polys:
        for m,c in p.items(): out[m]=out.get(m,0)+c
    return {m:c for m,c in out.items() if c}
def scale(p,c): return {m:c*v for m,v in p.items() if c*v}
def sub(p,q): return add(p,scale(q,-1))
def mul(p,q):
    out={}
    for m,c in p.items():
        for n,d in q.items():
            e=tuple(x+y for x,y in zip(m,n)); out[e]=out.get(e,0)+c*d
    return {e:c for e,c in out.items() if c}
def power(p,n):
    out=const(1)
    for _ in range(n): out=mul(out,p)
    return out
def diff(p,i):
    out={}
    for m,c in p.items():
        if m[i]:
            e=list(m); e[i]-=1; out[tuple(e)]=c*m[i]
    return out
def subst(p,images):
    out={}
    for m,c in p.items():
        term=const(c)
        for image,n in zip(images,m): term=mul(term,power(image,n))
        out=add(out,term)
    return out

checks={}
# Segre restriction and moving ruling line.
a,b,A,B,c,d=[var(i) for i in range(6)]
x0=mul(A,c); x1=mul(A,d); x2=mul(B,c); x3=mul(B,d)
F=sub(power(x1,4),mul(power(x0,3),x3))
G=sub(power(x2,4),mul(x0,power(x3,3)))
left=sub(power(x1,3),mul(power(x0,2),x2))
right=sub(power(x2,3),mul(x1,power(x3,2)))
curve_factor=sub(mul(A,power(d,3)),mul(B,power(c,3)))
checks['f_segre_factorization']=add(F,mul(mul(a,x0),left))==mul(mul(power(A,3),add(d,mul(a,c))),curve_factor)
checks['g_segre_factorization']=add(G,mul(mul(b,x3),right))==scale(mul(mul(power(B,3),add(c,mul(b,d))),curve_factor),-1)
# Actual homogeneous sources and their independently differentiated symbols on C.
x0,x1,x2,x3,a,b=[var(i) for i in range(6)]
Q=sub(mul(x0,x3),mul(x1,x2))
F=sub(power(x1,4),mul(power(x0,3),x3))
G=sub(power(x2,4),mul(x0,power(x3,3)))
left=sub(power(x1,3),mul(power(x0,2),x2))
right=sub(power(x2,3),mul(x1,power(x3,2)))
H0=add(*(power(x,2) for x in [x0,x1,x2,x3]),mul(x0,x2),scale(mul(x1,x3),2))
H1=add(scale(power(x0,2),2),scale(power(x1,2),3),scale(power(x2,2),5),scale(power(x3,2),7),mul(x0,x1),mul(x0,x3),mul(x1,x2),scale(mul(x2,x3),3))
f=add(F,mul(Q,H0),mul(mul(a,x0),left))
g=add(G,mul(Q,H1),mul(mul(b,x3),right))
# Directly restrict the actual pair to the moving line in its ruling.
pa,pb,lr,ls=var(0),var(1),var(2),var(3)
line_images=[lr,scale(mul(pa,lr),-1),ls,scale(mul(pa,ls),-1),pa,pb]
checks['moving_ruling_actual_restriction']=not subst(f,line_images) and subst(g,line_images)==mul(mul(power(ls,3),sub(const(1),mul(pa,pb))),add(mul(power(pa,3),lr),ls))
fixed_images=[scale(lr,-1),lr,scale(ls,-1),ls,pa,pb]
checks['fixed_line_actual_restriction']=subst(f,fixed_images)==mul(mul(sub(const(1),pa),power(lr,3)),add(lr,ls)) and subst(g,fixed_images)==mul(mul(sub(const(1),pb),power(ls,3)),add(lr,ls))
a1,b1,u=var(0),var(1),var(2)
images=[const(1),u,power(u,3),power(u,4),a1,b1]
restrict=lambda p: subst(p,images)
checks['all_actual_pairs_vanish_on_C']=not restrict(f) and not restrict(g)
af,bf=restrict(diff(f,3)),restrict(diff(f,2))
ag,bg=restrict(diff(g,3)),restrict(diff(g,2))
det=sub(mul(af,bg),mul(bf,ag))
h0,h1=restrict(H0),restrict(H1)
expected=add(mul(add(u,a1),h1),mul(mul(power(u,9),add(const(1),mul(b1,u))),h0),scale(mul(a1,power(u,8)),-3),scale(mul(add(const(4),scale(mul(a1,b1),2)),power(u,9)),-1),scale(mul(b1,power(u,10)),-3))
checks['two_parameter_actual_boundary_formula']=det==expected
at11=lambda p:subst(p,[const(1),const(1),u,const(1),const(1),const(1)])
Eboundary=add(h1,mul(power(u,9),h0),scale(power(u,8),-3),scale(power(u,9),-3))
checks['boundary_splits_one_plus_seventeen']=at11(det)==mul(add(u,const(1)),Eboundary)
coeffs=[Eboundary.get(tuple([0,0,i,0,0,0]),0) for i in range(18)]
checks['shared_point_not_a_triple']=sum(c*((-1)**i) for i,c in enumerate(coeffs))==14
checks['both_endpoints_free']=coeffs[0]==2 and coeffs[-1]==1

def trim(p):
    p=list(p)
    while p and p[-1]==0: p.pop()
    return p
def remainder(p,q):
    p=trim(p)
    while len(p)>=len(q):
        z=p[-1]/q[-1]; k=len(p)-len(q)
        for j,c in enumerate(q): p[j+k]-=z*c
        p=trim(p)
    return p
def gcd(p,q):
    while q: p,q=q,remainder(p,q)
    return [x/p[-1] for x in p]
def squarefree(coeffs):
    return gcd(list(map(Fraction,coeffs)),[Fraction(i*coeffs[i]) for i in range(1,len(coeffs))])==[Fraction(1)]
checks['boundary_seventeen_squarefree']=squarefree(coeffs)
q5=[2,3,2,9,-2,4]
checks['line_five_points_squarefree']=squarefree(q5)
checks['line_shared_point_excluded']=sum(c*((-1)**i) for i,c in enumerate(q5))==-14
# Normal row identity gives the common smoothing direction at all five nodes.
r,s=var(0),var(1)
qpoly=add(scale(power(r,5),4),scale(mul(power(r,4),s),-2),scale(mul(power(r,3),power(s,2)),9),scale(mul(power(r,2),power(s,3)),2),scale(mul(r,power(s,4)),3),scale(power(s,5),2))
F1=scale(mul(mul(r,add(r,s)),add(r,scale(s,2))),-1)
G1=add(scale(power(r,3),-4),scale(mul(power(r,2),s),2),scale(mul(r,power(s,2)),-9),scale(power(s,3),-1))
checks['five_nodes_same_smoothing_direction']=scale(mul(G1,power(r,3)),-1)==add(mul(r,qpoly),mul(F1,power(s,3)))
checks['genus_budget']=12+5-1==16 and 12+23-3+1==33
if not all(checks.values()): raise AssertionError(checks)
out={'scope':'Finite actual-source identities and squarefree polynomials only; projective schemes checked separately by M2.','passed':sum(checks.values()),'total':len(checks),'checks':checks,'boundary_E_coefficients_ascending_u_degree':coeffs,'line_E_intersection_coefficients_ascending_r_degree_s_equals_1':q5,'moving_line_stratum':'a*b=1','fixed_line_stratum':'a=b=1','local_five_node_smoothing_direction':'da+db','genus_E':12,'genus_smooth_residual':16,'C_E_points':17,'C_L_points':1,'L_E_points':5}
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(f'{out["passed"]}/{out["total"]} exact polynomial/budget checks: PASS')
print(path.name)
