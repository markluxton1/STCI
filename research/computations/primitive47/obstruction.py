#!/usr/bin/env python3
"""Exact moving-coordinate primitive-fourth obstruction for e=2 on C0.

Research scratch.  Input is a coprime pair A(z), B(z) of binary quadratics,
describing N_C^* -> O(-5), u |-> A, v |-> B.  The canonical primitive
triple exists uniquely because Hom(M,L^2)=O(-1).  Return its fourth
obstruction in H^1(O(-6)).  No finite scan is a global exclusion.
"""
import sympy as sp

z = sp.symbols("z", nonzero=True)
w = sp.symbols("w")

def plus(a,b):
    return [sp.expand(x+y) for x,y in zip(a,b)]

def scale(c,a):
    return [sp.expand(c*x) for x in a]

def mul(a,b):
    return [sp.expand(sum(a[i]*b[j] for i in range(k+1) for j in [k-i])) for k in range(4)]

def power(a,n):
    out=[sp.Integer(1),0,0,0]
    for _ in range(n): out=mul(out,a)
    return out

def poly_eval(p,arg,var=w):
    out=[0,0,0,0]
    for (n,),co in sp.Poly(p,var).terms(): out=plus(out,scale(co,power(arg,n)))
    return out

def bezout(a,b,var):
    s0,s1,t0,t1=sp.symbols("s0 s1 t0 t1")
    eq=sp.Poly((s0+s1*var)*a+(t0+t1*var)*b-1,var)
    sol=sp.solve(eq.all_coeffs(),(s0,s1,t0,t1))
    if not sol:
        # Degree drop can make linear Bezout nonunique; Euclid gives one.
        su,tv,g=sp.gcdex(a,b,var)
        if g!=1: raise ValueError("pair has an affine basepoint")
        return su,tv
    return sp.cancel((s0+s1*var).subs(sol)),sp.cancel((t0+t1*var).subs(sol))

def ambient_change(u,v):
    a=v
    b=plus(u,scale(sp.Rational(3,2)*z,v))
    nb=scale(z**-4,b)
    inv=scale(z**-4,plus(plus([1,0,0,0],scale(-1,nb)),plus(power(nb,2),scale(-1,power(nb,3)))))
    W=mul(plus([z**3,0,0,0],a),inv)
    up=scale(sp.Rational(1,2),plus(scale(z,inv),scale(-1,power(W,3))))
    vp=plus(plus(scale(-3*z,mul(W,inv)),power(W,4)),scale(2,inv))
    return W,up,vp

def obstruction(A,B):
    A,B=sp.sympify(A),sp.sympify(B)
    av=sp.expand(w**2*A.subs(z,1/w))
    bv=sp.expand(w**2*B.subs(z,1/w))
    if sp.gcd(av,bv)!=1: raise ValueError("pair has a projective basepoint")
    su,tv=bezout(A,B,z)
    sv,tvv=bezout(av,bv,w)
    W,up,vp=ambient_change([0,A,0,0],[0,B,0,0])
    mp=plus(mul(poly_eval(bv,W),up),scale(-1,mul(poly_eval(av,W),vp)))
    assert sp.cancel(mp[1])==0
    h2=sp.expand(z**9*mp[2])
    terms=sp.Add.make_args(h2)
    nonneg=sum(t for t in terms if t.as_powers_dict().get(z,0)>=0)
    negative=sp.expand(h2-nonneg)
    gu=sp.expand(nonneg)
    gv=sp.expand((-z*negative).subs(z,1/w))
    assert sp.cancel(gu-h2-z**-1*gv.subs(w,1/z))==0
    assert not any(t.as_powers_dict().get(w,0)<0 for t in sp.Add.make_args(gv))
    W,up,vp=ambient_change([0,A,-tv*gu,0],[0,B,su*gu,0])
    mp=plus(mul(poly_eval(bv,W),up),scale(-1,mul(poly_eval(av,W),vp)))
    ep=plus(mul(poly_eval(sv,W),up),mul(poly_eval(tvv,W),vp))
    assert sp.cancel(ep[1]-z**-5)==0
    # Only these coefficients contribute. Cancel the linear ell coefficient
    # before squaring: expanding unsimplified rational Bezout expressions
    # gives an unnecessary and very large generic-parameter expression.
    gv0=gv.subs(w,1/z)
    gv1=sp.diff(gv,w).subs(w,1/z)*W[1]
    assert sp.cancel(mp[2]+gv0*z**-10)==0
    mp3=sp.cancel(mp[3])
    ep2=sp.cancel(ep[2])
    h3=sp.cancel(z**9*(mp3+2*gv0*z**-5*ep2+gv1*z**-10))
    num,den=sp.fraction(h3)
    # Both affine gauges are polynomial; only Laurent poles at 0/infinity.
    assert sp.Poly(den,z).length()==1
    h3=sp.expand(h3)
    coords=[sp.cancel(h3.coeff(z,-j)) for j in range(1,6)]
    return h2,gu,gv,coords

if __name__=="__main__":
    pairs=[(z**2,1),(z**2+1,z),(z**2+z+1,z**2-z+1),(z**2+z,z**2+1),(z**2,1+z)]
    for A,B in pairs:
        h2,gu,gv,c=obstruction(A,B)
        print("A=",A,"B=",B,"h2=",h2,"gammaU=",gu,"gammaV=",gv,"h3 coords=",c,flush=True)
