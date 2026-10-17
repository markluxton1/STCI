#!/usr/bin/env python3
"""Exact DVR-lattice experiment for quasiprimitive length-six local algebras.

Realize B=A[x,y] inside Q(t)[y]/(y^6), with x=f(y), A=Q[t]_(t).
All displayed data are derived by exact rational arithmetic; a sample is not
an exhaustive normal-form classification.
"""
import itertools
import sympy as s

t = s.symbols('t')
N = 6

def val(z):
    z = s.cancel(z)
    if z == 0:
        return 1000000
    p, q = s.fraction(z)
    return min(e[0] for e in s.Poly(p, t).monoms()) - min(e[0] for e in s.Poly(q, t).monoms())

def mul(a,b):
    return [s.cancel(sum(a[j]*b[i-j] for j in range(i+1))) for i in range(N)]

def lattice(rows):
    rows = [list(row) for row in rows if any(row)]
    out = []
    for c in range(N):
        alive = [j for j,row in enumerate(rows) if row[c] != 0]
        if not alive:
            continue
        j = min(alive,key=lambda j:val(rows[j][c]))
        pivot = rows.pop(j)
        for row in rows:
            a = s.cancel(row[c]/pivot[c])
            assert val(a) >= 0
            for k in range(c,N):
                row[k] = s.cancel(row[k]-a*pivot[k])
        out.append((c,pivot))
    assert all(not any(row) for row in rows)
    return out

def coordinates(row,bas):
    row = list(row)
    coords=[]
    for c,b in bas:
        a = s.cancel(row[c]/b[c])
        assert val(a) >= 0
        coords.append(a)
        row = [s.cancel(row[k]-a*b[k]) for k in range(N)]
    assert not any(row)
    return coords

def residue(z):
    assert val(z)>=0
    return s.cancel(z).subs(t,0)

def inspect(f):
    one=[1]+[0]*5
    y=[0,1]+[0]*4
    mon=[]
    for i in range(6):
        xi=one
        for _ in range(i): xi=mul(xi,f)
        for j in range(6-i):
            z=xi
            for _ in range(j):z=mul(z,y)
            mon.append((i+j,z))
    bas=lattice([z for d,z in mon])
    assert [c for c,b in bas]==list(range(6))
    defects=tuple(-val(b[c]) for c,b in bas)
    square=lattice([z for d,z in mon if d>=2])
    assert [c for c,b in square]==list(range(2,6))
    A=sum(val(b[c]) for c,b in square)-sum(val(b[c]) for c,b in bas[2:])
    mx=s.Matrix([[residue(a) for a in coordinates(mul(f,b),bas)] for c,b in bas]).T
    my=s.Matrix([[residue(a) for a in coordinates(mul(y,b),bas)] for c,b in bas]).T
    socle=6-mx.col_join(my).rank()
    return defects,A,socle

if __name__=='__main__':
    cases=[(1,0,0,0),(0,1,0,0),(1,2,0,0),(1,-2,3,-4),
           (2,3,0,0),(1,0,2,0),(0,1,2,3),(1,2,3,4)]
    for ex in cases:
        f=[0,0]+[(t**(-a) if a>0 else -t**a if a<0 else 0) for a in ex]
        print(ex,inspect(f))
