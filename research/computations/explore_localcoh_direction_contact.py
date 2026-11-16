#!/usr/bin/env python3
"""Exact second-contact map in a balanced constant conormal direction.

This is exploratory linear algebra, not an ancestor exclusion.
"""
import sympy as sp
from pathlib import Path

x,y,z,w,t,U,V,lam=sp.symbols('x y z w t U V lambda')
q=x*w-y*z
A=x*x*z-y**3
B=x*z*z-y*y*w
C=y*w*w-z**3
ambient=(x,y,z,w)
chart={x:1,y:t,z:t**3+V,w:t**4+U+sp.Rational(3,2)*t*V}
monomials=[x*x,x*y,y*y,x*z,x*w,y*w,z*z,z*w,w*w]

def lift(P,Q):
    R=sp.Poly(sp.expand(Q-t*P/2),t)
    rc=lambda i:R.coeff_monomial(t**i)
    J=rc(0)*x*A+rc(1)*y*A+rc(3)*z*A+rc(4)*w*A+rc(6)*z*B+rc(7)*w*B-rc(9)*z*C-rc(10)*w*C
    PJ=-rc(6)*t**5-rc(7)*t**6-2*rc(9)*t**8-2*rc(10)*t**9
    p=sp.Poly(sp.expand(P-PJ),t)
    assert p.degree()<=8
    return sp.expand(J+q*sum(p.coeff_monomial(t**i)*monomials[i] for i in range(9)))

hs=[1,t+lam*t*t/2,t**3,t**4+lam*t**5/2,t**6,t**7+lam*t**8/2,t**9]
forms=[lift(lam*h,h) for h in hs]+[q*q]
bs=[]
for f,h in zip(forms,hs+[0]):
    fchart=sp.Poly(sp.expand(f.subs(chart)),U,V)
    assert sp.expand(fchart.coeff_monomial(U)-lam*h)==0
    assert sp.expand(fchart.coeff_monomial(V)-h)==0
    b=sp.expand(fchart.coeff_monomial(U*U)-lam*fchart.coeff_monomial(U*V)+lam*lam*fchart.coeff_monomial(V*V))
    bs.append(b)
for i,(f,h,b) in enumerate(zip(forms,hs+[0],bs)):
    print(i,'F=',sp.factor(f),'h=',h,'b=',sp.factor(b))
pairs=[(i,j) for i in range(8) for j in range(i+1,8)]
wedges=[sp.Poly(sp.expand((hs+[0])[i]*bs[j]-(hs+[0])[j]*bs[i]),t) for i,j in pairs]
deg=max(p.degree() for p in wedges if p)
M=sp.Matrix([[p.coeff_monomial(t**k) for p in wedges] for k in range(deg+1)])
print('contact wedge shape:',M.shape)
for value in [0,1,2,-1,sp.Rational(1,2)]:
    Ml=M.subs(lam,value)
    print('lambda=',value,'rank',Ml.rank(),'kernel dimension',len(Ml.nullspace()))
    # The kernel has decomposable and nondecomposable points. Its size alone
    # gives no pair classification.

# Generate a Plucker-locus audit in coordinates whose first four quartics
# are the unique cubic in this direction times x,y,z,w.
T=q*(lam*x+lam**2*y/2-lam**4*z/8-lam**5*w/16)+A-lam**3*B/4-lam**6*C/64
for value in [0,1,2]:
    ff=[sp.expand((T*v).subs(lam,value)) for v in ambient]+[forms[i].subs(lam,value) for i in [4,5,6,7]]
    hnew=[]; bnew=[]
    for f in ff:
        p=sp.Poly(sp.expand(f.subs(chart)),U,V)
        hnew.append(p.coeff_monomial(V))
        bnew.append(sp.expand(p.coeff_monomial(U*U)-value*p.coeff_monomial(U*V)+value*value*p.coeff_monomial(V*V)))
    assert sp.Matrix([[sp.Poly(f,*ambient).coeff_monomial(m) for f in ff] for m in sp.Poly(sum(ff),*ambient).monoms()]).rank()==8
    ww=[sp.Poly(sp.expand(hnew[i]*bnew[j]-hnew[j]*bnew[i]),t) for i,j in pairs]
    maxd=max(p.degree() for p in ww if p)
    mat=sp.Matrix([[p.coeff_monomial(t**k) for p in ww] for k in range(maxd+1)])
    null=mat.nullspace()
    avars=sp.symbols('a0:'+str(len(null)))
    pv={ij:sum(v[k]*a for v,a in zip(null,avars)) for k,ij in enumerate(pairs)}
    pf=[]
    for i in range(8):
        for j in range(i+1,8):
            for k in range(j+1,8):
                for l in range(k+1,8):
                    f=sp.expand(pv[i,j]*pv[k,l]-pv[i,k]*pv[j,l]+pv[i,l]*pv[j,k])
                    if f:pf.append(f)
    outside=[v for (i,j),v in pv.items() if j>=4 and v]
    def m2expr(f):return str(f).replace('**','^')
    code='-- Exact second-contact Plucker locus for constant direction lambda='+str(value)+'\n'
    code+='R=QQ['+','.join(map(str,avars))+',MonomialOrder=>GRevLex];\n'
    code+='I=ideal('+','.join(m2expr(f) for f in pf)+');\n'
    code+='J=ideal('+','.join(m2expr(f) for f in outside)+');\n'
    code+='print("contact ideal dimension = "|toString dim I);\n'
    code+='sat=saturate(I,J);\nprint("outside saturation = "|toString sat);\n'
    code+='print("outside saturation dimension = "|toString dim sat);\n'
    dest=Path(__file__).with_name('explore_localcoh_direction_contact_lambda'+str(value)+'.m2')
    dest.write_text(code)
    print('generated',dest)
    if value==2:
        residuals=[sp.expand(hnew[0]*bnew[i]-bnew[0]*hnew[i]) for i in range(4,8)]
        assert sp.Matrix([[sp.expand(f).coeff(t,k) for f in residuals] for k in range(20)]).rank()==4
        for j in range(4,8):
            for k in range(j+1,8):
                inds=[i for i in range(8) if i not in [j,k]]
                fv=sp.symbols('f0:6');gv=sp.symbols('g0:6')
                fco=dict(zip(inds,fv));gco=dict(zip(inds,gv))
                fco.update({j:1,k:0});gco.update({j:0,k:1})
                hf=sum(fco[i]*hnew[i] for i in range(8));hg=sum(gco[i]*hnew[i] for i in range(8))
                bf=sum(fco[i]*bnew[i] for i in range(8));bg=sum(gco[i]*bnew[i] for i in range(8))
                ce=sp.Poly(sp.expand(hf*bg-hg*bf),t)
                eq=ce.all_coeffs()
                code='R=QQ['+','.join(map(str,fv+gv))+',MonomialOrder=>GRevLex];\n'
                code+='I=ideal('+','.join(m2expr(e) for e in eq if e)+');\n'
                code+='print("chart '+str(j)+','+str(k)+' unit ideal = "|toString(I==ideal(1_R)));\n'
                code+='print("chart dimension = "|toString dim I);\n'
                dest=Path(__file__).with_name('explore_localcoh_direction_contact_chart'+str(j)+str(k)+'.m2')
                dest.write_text(code)
                print('generated',dest)
