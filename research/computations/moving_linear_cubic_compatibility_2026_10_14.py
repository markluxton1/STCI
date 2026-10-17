#!/usr/bin/env python3
"""New cubic Cech calculation, exact Fraction Laurent arithmetic.

Variables are (t,z,u,v); only the u,v degree is truncated at three.
The chart and quadratic obstruction are accepted inputs.  This script
calculates the next, cubic, obstruction on its obstruction-zero locus.
"""
from fractions import Fraction as Q
import json
from pathlib import Path

MAX_NORMAL = 3


class P:
    def __init__(self, terms=None):
        self.d = {m: Q(c) for m, c in (terms or {}).items() if c and m[2]+m[3] <= MAX_NORMAL}

    @staticmethod
    def c(c):
        return P({(0,0,0,0): Q(c)})

    def __add__(self, other):
        if not isinstance(other, P): other=P.c(other)
        d=self.d.copy()
        for m,c in other.d.items(): d[m]=d.get(m,Q(0))+c
        return P(d)

    __radd__=__add__

    def __neg__(self): return P({m:-c for m,c in self.d.items()})
    def __sub__(self, other): return self+-other
    def __rsub__(self, other): return other+-self

    def __mul__(self, other):
        if not isinstance(other,P): other=P.c(other)
        d={}
        for m,c in self.d.items():
            for n,e in other.d.items():
                r=tuple(a+b for a,b in zip(m,n))
                if r[2]+r[3] <= MAX_NORMAL: d[r]=d.get(r,Q(0))+c*e
        return P(d)

    __rmul__=__mul__

    def __pow__(self, n):
        if n<0:
            assert len(self.d)==1
            m,c=next(iter(self.d.items()))
            assert m[2]+m[3]==0
            return P({tuple(x*n for x in m): c**n})
        ans=P.c(1)
        for _ in range(n): ans=ans*self
        return ans

    def homogeneous(self,n): return P({m:c for m,c in self.d.items() if m[2]+m[3]==n})

    def du(self):
        return P({(m[0],m[1],m[2]-1,m[3]):m[2]*c for m,c in self.d.items() if m[2]})

    def evaluate_normal(self,b,minus_a):
        ans=P()
        for (it,iz,iu,iv),c in self.d.items():
            ans=ans+P({(it,iz,0,0):c})*(b**iu)*(minus_a**iv)
        return ans

    def format(self):
        return [dict(t=m[0],z=m[1],u=m[2],v=m[3],coefficient=str(c)) for m,c in sorted(self.d.items())]


t=P({(1,0,0,0):1})
z=P({(0,1,0,0):1})
u=P({(0,0,1,0):1})
v=P({(0,0,0,1):1})


def poly2_mul(a,b):
    r=[Q(0)]*3
    for i,c in enumerate(a):
        for j,d in enumerate(b):
            k=i+j
            if k<2:r[k]+=c*d
            else:
                # t^2=(4/3)t-4 in Q[t]/(3t^2-4t+12).
                r[0]+=-4*c*d
                r[1]+=Q(4,3)*c*d
    return r[:2]


def reduce_diagonal(p):
    d={}
    for (it,iz,iu,iv),c in p.d.items():
        a=[Q(1),Q(0)]
        base=[Q(0),Q(1)] if it>=0 else [Q(1,3),Q(-1,4)]
        for _ in range(abs(it)): a=poly2_mul(a,base)
        for k,e in enumerate(a):
            m=(k,iz,iu,iv)
            d[m]=d.get(m,Q(0))+c*e
    return P(d)


def divide_by_a(poly,a0,a1):
    """Exact division by a0+a1*z, where a1 is an invertible monomial."""
    assert all(m[2]+m[3]==0 for m in poly.d)
    if not a1.d: return poly*(a0**-1)
    if not poly.d: return P()
    shift=min(m[1] for m in poly.d)
    rem=poly*(z**(-shift)); quo=P()
    while rem.d and max(m[1] for m in rem.d)>=1:
        degree=max(m[1] for m in rem.d)
        lead=P({(m[0],0,0,0):c for m,c in rem.d.items() if m[1]==degree})
        q=lead*(a1**-1)*(z**(degree-1))
        quo=quo+q
        rem=rem-q*(a0+a1*z)
    assert not rem.d, rem.format()
    return quo*(z**shift)


def calculate(name,A,B,C,D,Delta,reduce=lambda x:x):
    a=A+C*z; b=B+D*z
    f0=a*u+b*v
    b_original=u+Q(3,2)*z*v
    inv=sum(((-b_original)**j)*(z**(-4*(j+1))) for j in range(4))
    W=(z**3+v)*inv
    ap=z*inv-W**3
    bp=inv-W**4
    up=ap*Q(1,2)
    vp=-3*W*ap+2*bp
    f1=(A*W+C)*up+(B*W+D)*vp

    # Accepted quadratic discrepancy; only split into its two coboundaries.
    T=3*z**-5*b**3-Q(3,2)*z**-4*a*b**2+Q(3,4)*z**-3*a**2*b-Q(3,8)*z**-2*a**3-Delta*z**-3*b+Delta*Q(1,2)*z**-2*a
    T=reduce(T)
    assert not P({m:c for m,c in T.d.items() if -3<=m[1]<=-1}).d
    q0=P({m:c for m,c in T.d.items() if m[1]>=0})
    low=P({m:c for m,c in T.d.items() if m[1]<=-4})
    q1_chart=-z**4*low
    q1=P()
    for (it,iz,iu,iv),c in q1_chart.d.items():
        assert iu+iv==0 and iz<=0
        q1=q1+P({(it,0,0,0):c})*(W**(-iz))
    ell0=(-C*u-D*v)*(Delta**-1)
    ell1=(A*up+B*vp)*(Delta**-1)
    F0=f0+q0*ell0**2
    F1=f1+q1*ell1**2
    discrepancy=reduce(z**8*F1-F0)
    assert not discrepancy.homogeneous(1).d
    quadratic=discrepancy.homogeneous(2)
    assert not reduce(quadratic.evaluate_normal(b,-a)).d
    L2eval=reduce(divide_by_a(reduce(quadratic.du().evaluate_normal(b,-a)),A,C))
    # Independent exact divisibility check in the unimodular coordinates
    # (f0,ell0), with u,v temporarily naming these two coordinates.
    canonical=reduce(quadratic.evaluate_normal(D*(Delta**-1)*u+b*v,-C*(Delta**-1)*u-a*v))
    assert not P({m:c for m,c in canonical.d.items() if m[3]==2}).d
    L2canonical=P({(it,iz,iu-1,iv):c for (it,iz,iu,iv),c in canonical.d.items()})
    L2=reduce(L2canonical.evaluate_normal(f0,ell0))
    assert not reduce(quadratic-f0*L2).d
    assert not reduce(L2.evaluate_normal(b,-a)-L2eval).d
    cubic=reduce(discrepancy.homogeneous(3).evaluate_normal(b,-a)-q0*L2eval)
    obstruction=P({m:c for m,c in cubic.d.items() if -9<=m[1]<=-1})
    return dict(name=name,q0=q0.format(),q1_chart=q1_chart.format(),L2eval=L2eval.format(),cubic=cubic.format(),obstruction=obstruction.format())


def main():
    results=[
        calculate("quadric",P.c(2),P(),P(),P.c(1),P.c(2)),
        calculate("other_diagonal",t,P(),P(),P.c(1),t,reduce_diagonal),
        calculate("open_conic",P.c(2),t,8*t**-1,P.c(1),P.c(-6)),
    ]
    out=Path(__file__).resolve().parents[1]/"validation"/"2026-10-14-moving-linear-cubic"
    out.mkdir(parents=True,exist_ok=True)
    (out/"cubic-results.json").write_text(json.dumps(results,indent=2)+"\n")
    for r in results:
        print(r["name"])
        for key in ("q0","q1_chart","L2eval","obstruction"):
            print(key, json.dumps(r[key],sort_keys=True))


if __name__=="__main__": main()
