#!/usr/bin/env python3
"""Bounded exact conic-component continuation, preserving the coefficient chart."""
from pathlib import Path
from fractions import Fraction as Q
from conditional_2_12_singular_continuation_2026_10_20 import load_equations

HERE=Path(__file__).resolve().parent
stem=HERE/'conditional_2_12_singular_continuation2_2026_10_21'
model=HERE/'conditional_2_12_singular_continuation_2026_10_21.m2'
path=stem.with_name(stem.name+'_conic_w1.m2')
path.write_text('\n'.join([
    '-- Exact w=1 generic norm-symbol conic component; no arbitrary ruling action.',
    'load "'+str(model)+'";',
    'T=QQ[h4,h5,h6,h7,A2,a,x,y,MonomialOrder=>Eliminate 5];',
    'phi=map(T,R,{1,a-x,(a+x)/2,A2,y+A2/2,h4,h5,h6,h7,0,0});',
    'I=ideal join(apply(firstEquations,p->phi p),apply(normSymbolEquations,p->phi p),{2*(x^2+x*y+y^2)+3});',
    'print("W1_CONIC_FIRST_ELIMINATION_START");',
    'E=eliminate({h4,h5,h6,h7,A2},I);',
    'print("W1_CONIC_FIRST_ELIMINATION_READY");',
    'S=QQ[a,x,y];psi=map(S,T,{0,0,0,0,0,a,x,y});',
    'ES=ideal psi(gens E);',
    'print("ELIMINATED_GENERATOR_COUNT="|toString(numgens ES));',
    'print("ELIMINATED_DIMENSION="|toString(dim ES));',
    'L=x^2+2;nA=a-(L+a*x)*y;nD=a+(L-a*x)*y;',
    'tauN=(a-x)*nD/2+nA*(a+x)/2-2*L;',
    'deltaN=((a^2-x^2-2)/2)*(nA*nD/2-L^2);',
    'op=a*(2*x^2+1)*L*(a^2-x^2-2)*(nA*nD/2-L^2)*(tauN^2-4*deltaN);',
    'J0=saturate(ES,ideal(op));G=gb J0;',
    'print("W1_CONIC_FIRST_ON_OPEN");print(numgens J0,dim J0,(1%G)==0);',
    '-- Weighted-homogeneous clearing: Q12(tauN,deltaN)=L^11*Q12(tau,delta).',
    'q=tauN%G;ts=tauN^2%G;de=deltaN%G;',
    'scan({ts-de,ts-2*de,ts-3*de,(ts-2*de)^2-3*de^2},p->q=(q*p)%G);',
    'J=saturate(J0+ideal(q),ideal(op));',
    'print("W1_CONIC_FIRST_TORSION_RESULT");print gens gb J;',
    '']) )
print(path)

# Entire nonzero-kappa B=0 boundary, with C1=C2=D1=1 after allowed scales/torus.
env=load_equations()
ca,cm,cs,var,fmt=(env[k] for k in ('ca','cm','cs','var','fmt'))
env['NAMES'][:]=[f'h{i}' for i in range(12)]+['t','w']
t,w=var(12),var(13);w2=cm(w,w)
f=[cs(cm(w2,t),-2),ca(t,cs(w2,-2)),{():Q(1)},
   {},cs(cm(w2,ca(cs(cm(t,t),Q(1,2)),{():Q(2)})),-1),
   ca({():Q(1)},cs(cm(w2,t),Q(-1,2))),{},{},cs(cm(w2,t),Q(-1,2))]
values=f+[var(i) for i in range(12)]
def sub(poly):
    out={}
    for m,c in poly.items():
        term={():c}
        for i in m:term=cm(term,values[i])
        out=ca(out,term)
    return out
first=[sub(poly) for poly in env['FIRST']]
for name,primitive in [('w1',False),('primitive',True)]:
    target=stem.with_name(stem.name+'_boundary_B0_'+name+'.m2')
    field=['K=toField(QQ[ww]/ideal(ww^2+ww+1));'] if primitive else ['K=QQ;']
    rows=field+[
        '-- Full nonzero-kappa B=0 boundary; C1=C2=D1=1, parameter t.',
        'R=K['+','.join(f'h{i}' for i in range(12))+',t,MonomialOrder=>Eliminate 12];',
        'w=sub(K_0,R);' if primitive else 'w=1_R;',
        'firstEquations={'+','.join(fmt(p) for p in first)+'};',
        'I=ideal firstEquations;',
        'E=eliminate({'+','.join(f'h{i}' for i in range(12))+'},I);',
        'print("BOUNDARY_B0_FIRST_ELIMINATION");print gens E;',
        'S=K[t];phi=map(S,R,{'+','.join(['0']*12+['t'])+'});',
        'ES=ideal phi(gens E);',
        'w=sub(K_0,S);' if primitive else 'w=1_S;',
        'tau=-w^2*(t^2/2+2);delta=w*t^2;',
        'q=tau*(tau^2-delta)*(tau^2-2*delta)*(tau^2-3*delta)*((tau^2-2*delta)^2-3*delta^2);',
        'J=saturate(ES+ideal(q),ideal(t*(t^2-4)));',
        'print("BOUNDARY_B0_FIRST_TORSION_RESULT");print gens gb J;',
        '']
    target.write_text('\n'.join(rows));print(target)
