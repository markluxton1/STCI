#!/usr/bin/env python3
"""Independent exact nonreduced anticanonical tree audit.

The first scan grows free trees by attaching leaves and solves by rational
Schur elimination. This audit builds rooted trees as multisets, identifies
free-tree centers, tests positivity using the integer matching characteristic
polynomial, and computes inverse entries by deleting paths from a tree.
No first-scan source or result is imported.
"""
from contextlib import redirect_stdout
from fractions import Fraction
from io import StringIO
from itertools import combinations_with_replacement
from math import lcm
from pathlib import Path
import json
import runpy

BASE=Path(__file__).resolve().parents[1]
with redirect_stdout(StringIO()):
    ade=runpy.run_path(str(BASE/'computations/verify_session_normal_independent_audit.py'))
states=ade['states']
byrank={}
state_seen=set()
for N,P,q,index,names in states:
    key=(N,P,q,index)
    if key in state_seen:continue
    state_seen.add(key)
    byrank.setdefault(N,[]).append((P,q,index,names))


def adjacency(code):
    adj=[]
    def visit(tree,parent=None):
        i=len(adj);adj.append([])
        if parent is not None:adj[i].append(parent);adj[parent].append(i)
        for child in tree:visit(child,i)
    visit(code)
    return tuple(tuple(a) for a in adj)


def centers(adj):
    left=set(range(len(adj)));degree=list(map(len,adj))
    while len(left)>2:
        leaves=[i for i in left if degree[i]==1]
        for i in leaves:
            left.remove(i)
            for j in adj[i]:degree[j]-=1
    return sorted(left)


def rooted_code(adj,i,parent=-1,weights=None):
    return (0 if weights is None else weights[i],
            tuple(sorted(rooted_code(adj,j,i,weights)
                         for j in adj[i] if j!=parent)))


def free_code(adj,weights=None):
    c=centers(adj)
    if len(c)==1:return (1,rooted_code(adj,c[0],weights=weights))
    return (2,tuple(sorted((rooted_code(adj,c[0],c[1],weights),
                           rooted_code(adj,c[1],c[0],weights)))))


def rooted_trees_to(nmax):
    rooted={1:[()]}
    for n in range(2,nmax+1):
        choices=sorted((size,t) for size in rooted for t in rooted[size])
        out=[]
        def recurse(rem,start,prefix):
            if rem==0:
                out.append(tuple(sorted(prefix)));return
            for i in range(start,len(choices)):
                size,t=choices[i]
                if size>rem:break
                recurse(rem-size,i,prefix+(t,))
        recurse(n-1,0,())
        rooted[n]=out
    return rooted


def multiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:c[i+j]+=x*y
    return c


def charpoly(adj,b):
    def visit(i,parent):
        prod=[1];edge=[0]
        for j in adj[i]:
            if j==parent:continue
            p,q=visit(j,i)
            e1=multiply(edge,p);e2=multiply(prod,q)
            edge=[(e1[k] if k<len(e1) else 0)+(e2[k] if k<len(e2) else 0)
                  for k in range(max(len(e1),len(e2)))]
            prod=multiply(prod,p)
        p=multiply([b[i],1],prod)
        for k,x in enumerate(edge):p[k]-=x
        return p,prod
    return visit(0,-1)[0]


def forest_det(adj,b,removed):
    seen=set()
    def visit(i,parent):
        seen.add(i);prod=1;edge=0
        for j in adj[i]:
            if j==parent or removed>>j&1:continue
            p,q=visit(j,i)
            edge=edge*p+prod*q;prod*=p
        return b[i]*prod-edge,prod
    result=1
    for i in range(len(adj)):
        if i not in seen and not(removed>>i&1):result*=visit(i,-1)[0]
    return result


def path_masks(adj):
    result={}
    for start in range(len(adj)):
        def visit(i,parent,mask):
            mask|=1<<i;result[start,i]=mask
            for j in adj[i]:
                if j!=parent:visit(j,i,mask)
        visit(start,-1,0)
    return result


def main():
    rooted=rooted_trees_to(12)
    counts={2:1,3:1,4:2,5:3,6:6,7:11,8:23,9:47,10:106,11:235,12:551}
    cases=0;records={};matches=[];positive=0
    for k in range(2,13):
        free={}
        for code in rooted[k]:
            adj=adjacency(code);free.setdefault(free_code(adj),adj)
        assert len(free)==counts[k]
        print('independent free trees',k,len(free),flush=True)
        for adj in free.values():
            paths=path_masks(adj)
            for total in (1,2,3):
                for positions in combinations_with_replacement(range(k),total):
                    cases+=1;beta=[0]*k
                    for i in positions:beta[i]+=1
                    b=[x+2 for x in beta]
                    p=charpoly(adj,b)
                    # Symmetry makes every root real. Positive coefficients
                    # of det(A+xI) exclude every nonpositive eigenvalue.
                    if any(x<=0 for x in p):continue
                    positive+=1;det=p[0];cache={}
                    def cofactor(i,j):
                        mask=paths[i,j]
                        if mask not in cache:cache[mask]=forest_det(adj,b,mask)
                        return cache[mask]
                    support=sorted(set(positions));a=[None]*k
                    d=0;bad=False
                    for i in support:
                        num=sum(beta[j]*cofactor(i,j) for j in support)
                        if num%det:bad=True;break
                        a[i]=num//det;d+=beta[i]*a[i]
                    if bad or d not in (1,2,3) or k>9+d:continue
                    for i in range(k):
                        if a[i] is None:
                            num=sum(beta[j]*cofactor(i,j) for j in support)
                            if num%det:bad=True;break
                            a[i]=num//det
                    if bad or any(x<1 for x in a):continue
                    assert any(x>1 for x in a)
                    assert all(b[i]*a[i]-sum(a[j] for j in adj[i])==beta[i]
                               for i in range(k))
                    key=free_code(adj,b)
                    if key in records:continue
                    selected=[]
                    for j,t in enumerate(a):
                        if t not in ([1] if d==1 else [1,2]):continue
                        z=[Fraction(cofactor(i,j),det) for i in range(k)]
                        assert all(b[i]*z[i]-sum(z[u] for u in adj[i])==int(i==j)
                                   for i in range(k))
                        q=z[j];idx=lcm(*(x.denominator for x in z));req=6-t-q
                        for rank in range(10+d-k):
                            for P,qa,L,names in byrank.get(rank,[]):
                                if qa!=req:continue
                                mate=lcm(idx,L)
                                if mate<=5:continue
                                row={'d':d,'k':k,'adj':adj,'b':b,'a':a,'selected':j,
                                     't':t,'q':str(q),'index':idx,'ADErank':rank,
                                     'ADEorder':P,'ADEq':str(qa),'mate':mate,'ADE':names}
                                matches.append(row);selected.append(row)
                    records[key]={'d':d,'adj':adj,'b':b,'a':a,'survivors':selected}
        print('positive',positive,'valid',len(records),'matches',len(matches),flush=True)
    assert cases==381802
    assert len(records)==195
    assert len(matches)==12
    assert all(r['d']==3 and r['t']==2 for r in matches)
    output={'status':'independent exact graph enumeration, not geometric existence',
            'cases':cases,'positive_cases':positive,'valid_cycles':len(records),
            'trees':list(records.values()),'matches':matches}
    target=BASE/'scratch/session_nonreduced_independent_audit.json'
    target.write_text(json.dumps(output,indent=2)+'\n')
    print('NONREDUCED INDEPENDENT AUDIT PASS:',cases,len(records),len(matches),flush=True)
    print('ALL SURVIVORS d=3,t=2',flush=True)


if __name__=='__main__':main()
