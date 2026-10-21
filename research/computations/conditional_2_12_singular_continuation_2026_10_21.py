#!/usr/bin/env python3
"""Compact generic two-node forced-norm incidence in actual C0 coordinates.

No root ruling is changed by PGL2. Only independent factor scales and
the actual C0 torus are used. Boundary charts remain explicit obligations.
"""
import ast
from fractions import Fraction as Q
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent


def main():
    source=HERE/'generalization_quadratic_root_global_second_model.py'
    tree=ast.parse(source.read_text())
    stop=next(i for i,n in enumerate(tree.body) if isinstance(n,ast.Assign)
              and any(isinstance(t,ast.Name) and t.id=='G1P' for t in n.targets))
    env={'__file__':str(source),'__name__':'new_two_node_norm_export'}
    exec(compile(ast.Module(body=[n for n in tree.body[:stop] if not isinstance(n,ast.Assert)],
                            type_ignores=[]),str(source),'exec'),env)
    oldca,oldcm,cs,var,const=(env[k] for k in ('ca','cm','cs','var','const'))
    # Work in QQ[w]/(w^3-1) throughout coefficient construction.
    def red(p):
        out={}
        for m,c in p.items():
            count=m.count(0)
            n=tuple([0]*(count%3)+[i for i in m if i])
            out[n]=out.get(n,Q(0))+c
        return {m:c for m,c in out.items() if c}
    def ca(*p):return red(oldca(*p))
    def cm(p,q):return red(oldcm(p,q))
    def cp(p,n):
        out=const(1)
        for _ in range(n):out=cm(out,p)
        return out
    names=['w','A1','D1','A2','D2','h4','h5','h6','h7','eta']
    env['NAMES'][:]=names
    w,A1,D1,A2,D2,H4,H5,H6,H7,eta=[var(i) for i in range(10)]
    invw=cp(w,2)
    f=[cm(A1,A2),ca(cm(A1,w),A2),w,
       ca(A1,A2),ca(cm(A1,D2),cm(A2,D1),const(1),w),ca(D2,cm(w,D1)),
       const(1),ca(D1,D2),cm(D1,D2)]
    H=[{} for _ in range(12)]
    H[4:8]=[H4,H5,H6,H7]
    H[3]=cm(invw,ca(cs(cm(f[0],H[5]),-1),cs(cm(f[1],H[4]),-1)))
    H[2]=ca(const(-3),cm(invw,ca(cs(cm(f[0],H[4]),-1),cs(cm(f[1],H[3]),-1))))
    H[1]=cm(invw,ca(cs(f[1],-4),cs(f[5],3),cs(cm(f[0],H[3]),-1),cs(cm(f[1],H[2]),-1)))
    H[0]=cm(invw,ca(cs(f[0],-5),cs(f[4],3),cs(cm(f[0],H[2]),-1),cs(cm(f[1],H[1]),-1)))
    H[8]=ca(cs(cm(f[7],H[7]),-1),cs(cm(f[8],H[6]),-1))
    H[9]=ca(const(Q(-9,2)),cs(cm(f[7],H[8]),-1),cs(cm(f[8],H[7]),-1))
    H[10]=ca(cs(f[3],Q(-3,8)),cs(f[7],-4),cs(cm(f[7],H[9]),-1),cs(cm(f[8],H[8]),-1))
    H[11]=ca(cs(f[4],Q(-3,8)),cs(f[8],Q(-7,2)),cs(cm(f[7],H[10]),-1),cs(cm(f[8],H[9]),-1))
    values=f+H
    def sub(p):
        out={}
        for m,c in p.items():
            term=const(c)
            for i in m:term=cm(term,values[i])
            out=ca(out,term)
        return out
    first=[sub(p) for p in env['FIRST']]
    assert [i for i,p in enumerate(first) if p]==list(range(4,12))
    G=[[sub(env['G0'].get((3-i,i,j),{})) for j in range(2)] for i in range(4)]
    d1=ca(D1,cs(A1,Q(-1,2)));d2=ca(D2,cs(A2,Q(-1,2)))
    k1=cm(ca(A1,cs(D1,2)),ca(cp(d1,2),const(Q(1,2))))
    k2=cm(ca(A2,cs(D2,2)),ca(cp(d2,2),cs(w,Q(1,2))))
    b1=ca(cs(cm(A1,cp(d1,2)),-1),D1,cs(A1,-1))
    b2=ca(cs(cm(A2,cp(d2,2)),-1),cm(w,ca(D2,cs(A2,-1))))
    norms=[ca(k1,k2),ca(b2,cs(b1,-1),cs(k1,-1))]
    fmt=env['fmt']
    data=json.loads((HERE/'conditional_2_12_symbol_map_2026_10_20.json').read_text())
    rows=data['image_rank_certificate']['minor_rows_zero_based']
    labels=data['source_basis_labels'];cols=[labels.index(x) for x in data['image_basis_labels']]
    M=[[Q(data['symbol_matrix_33_by_23'][i][j]) for j in cols] for i in rows]
    aug=[r+[Q(int(i==j)) for j in range(22)] for i,r in enumerate(M)]
    for j in range(22):
        pivot=next(i for i in range(j,22) if aug[i][j]);aug[j],aug[pivot]=aug[pivot],aug[j]
        a=aug[j][j];aug[j]=[x/a for x in aug[j]]
        for i in range(22):
            if i!=j and aug[i][j]:
                a=aug[i][j];aug[i]=[x-a*y for x,y in zip(aug[i],aug[j])]
    inverse=[r[22:] for r in aug]
    C=[[Q(row[j]) for j in cols] for row in data['cubic_layer_matrix_40_by_23']]
    K=[[sum(C[i][k]*inverse[k][j] for k in range(22)) for j in range(22)] for i in range(40)]
    matrix='matrix{'+','.join('{'+','.join(map(str,r))+'}' for r in K)+'}'
    def zpoly(parts):
        return '+'.join('('+fmt(p)+')*zz^'+str(j) for j,p in enumerate(parts) if p) or '0'
    stem=HERE/'conditional_2_12_singular_continuation_2026_10_21'
    m2=stem.with_suffix('.m2')
    m2.write_text('\n'.join([
        '-- Generic two-node B1=B2=C1=1,C2=w; only actual torus/factor scales used.',
        'R=QQ['+','.join(names)+',iv,MonomialOrder=>GRevLex];',
        'firstEquations={'+','.join(fmt(p) for p in first if p)+'};',
        'normSymbolEquations={'+','.join(fmt(p) for p in norms)+'};',
        'kappa1='+fmt(k1)+';',
        'tau=A1*D2+A2*D1-1-w;',
        'delta=(A1*D1-1)*(A2*D2-w);',
        'twoNodeGenericOpen=kappa1*delta*(tau^2-4*delta);',
        'baseIdeal=ideal join(firstEquations,normSymbolEquations,{w^3-1,iv*twoNodeGenericOpen-1});',
        'S=R[zz];',
        'aa='+zpoly(f[:3])+';','bb='+zpoly(f[3:6])+';','cc='+zpoly(f[6:9])+';',
        'ttau1=1+(D1-A1/2)*zz-zz^2/2;',
        'ttau2=1+(D2-A2/2)*zz-w*zz^2/2;',
        'ttau=ttau1*ttau2;',
        'coeffR=(p,j)->sub(coefficient(zz^j,p),R);',
        'uu=coeffR(ttau,0)+coeffR(ttau,3)*zz^3;',
        'vv=coeffR(ttau,1)*zz+coeffR(ttau,4)*zz^4;',
        'ww=coeffR(ttau,2)*zz^2;',
        'alphaCanonical=uu^2+vv^2+ww^2-uu*vv-uu*ww-vv*ww;',
        'afVector=flatten apply({aa,bb,cc},p->apply(11,j->coeffR(alphaCanonical*p,j)));',
        'splitCubicMatrix=sub('+matrix+',R);',
        'splitCubicVector=flatten entries(splitCubicMatrix*transpose matrix{apply({'+','.join(map(str,rows))+'},j->afVector#j)});',
        'gg={'+','.join(zpoly(p) for p in G)+'};',
        'tt=apply(4,i->sum(10,j->(splitCubicVector#(10*i+j))*zz^j)-alphaCanonical*gg#i+eta*({1,3/2,3/4,1/8}#i)*zz^i);',
        'syzygies={(bb^2-aa*cc)*tt#0-aa*bb*tt#1+aa^2*tt#2,bb*cc*tt#0-aa*cc*tt#1+aa^2*tt#3,cc^2*tt#0-aa*cc*tt#2+aa*bb*tt#3,cc^2*tt#1-bb*cc*tt#2+(bb^2-aa*cc)*tt#3};',
        'cubicEquations=select(flatten apply(syzygies,p->apply(14,j->coeffR(p,j))),p->p!=0);',
        'cubicIdeal=baseIdeal+ideal cubicEquations;',
        'print("GENERIC_TWO_NODE_NORM_FIRST_AND_CUBIC_MODEL_READY");',
        'print("FIRST_COUNT="|toString(#firstEquations));',
        'print("CUBIC_COUNT="|toString(#cubicEquations));',
        '-- Spectral torsion Q12 is imposed by the bounded quotient-reduced runner.',
        '']) )
    # Exact line component of the generic norm-symbol locus, y=x.
    line_names=['w','a','x','h4','h5','h6','h7','iv']
    env['NAMES'][:]=line_names
    ww,ap,xp=[var(i) for i in range(3)]
    w2=cp(ww,2)
    line_values=[ww,ca(ap,cs(xp,-1)),cs(ca(ap,xp),Q(1,2)),
                 cs(cm(w2,ca(ap,xp)),-1),cs(cm(w2,ca(xp,cs(ap,-1))),Q(1,2))]
    line_values += [var(i) for i in range(3,7)]+[{}]
    def line_sub(p):
        out={}
        for m,c in p.items():
            term=const(c)
            for i in m:term=cm(term,line_values[i])
            out=ca(out,term)
        return out
    line_first=[line_sub(p) for p in first if p]
    assert not any(line_sub(p) for p in norms)
    line_m2=stem.with_name(stem.name+'_line_component.m2')
    line_m2.write_text('\n'.join([
        '-- Exact y=x component on the generic forced-norm two-node chart.',
        'R=QQ['+','.join(line_names)+',MonomialOrder=>GRevLex];',
        'firstEquations={'+','.join(fmt(p) for p in line_first)+'};',
        'tau=-w^2*(a^2+x^2)-1-w;',
        'delta=w*((a^2-x^2-2)/2)^2;',
        'kappa=a*(2*x^2+1);',
        'openPolynomial=kappa*delta*(tau^2-4*delta);',
        'I=ideal join(firstEquations,{w^3-1,iv*openPolynomial-1});',
        'print("LINE_FIRST_GROEBNER_START");',
        'G=gb I;',
        'print("LINE_FIRST_GROEBNER_READY");print gens G;',
        '-- Reduce after each product; do not expand degree22 torsion first.',
        'q=tau%G; ts=(tau^2)%G; de=delta%G;',
        'scan({ts-de,ts-2*de,ts-3*de,(ts-2*de)^2-3*de^2},p->q=(q*p)%G);',
        'J=I+ideal(q);',
        'print("LINE_FIRST_TORSION_GROEBNER_READY");print gens gb J;',
        '']) )
    # The w=1 line component depends on a only through p=a^2.
    # Eliminate four linear h variables before any inverse or torsion expansion.
    w1_names=['h4','h5','h6','h7','p','x']
    def w1_sub(poly):
        stage={}
        for m,c in poly.items():
            n=tuple(i for i in m if i!=0)
            stage[n]=stage.get(n,Q(0))+c
        stage={m:c for m,c in stage.items() if c}
        out={}
        for m,c in stage.items():
            assert m.count(1)%2==0
            n=tuple(sorted([4]*(m.count(1)//2)+[5]*m.count(2)+
                           [i-3 for i in m if 3<=i<=6]))
            out[n]=out.get(n,Q(0))+c
        return {m:c for m,c in out.items() if c}
    w1_first=[w1_sub(poly) for poly in line_first]
    env['NAMES'][:]=w1_names
    w1_m2=stem.with_name(stem.name+'_line_component_w1.m2')
    w1_m2.write_text('\n'.join([
        '-- Exact w=1,y=x generic norm component, p=a^2; p nonzero.',
        'R=QQ['+','.join(w1_names)+',MonomialOrder=>Eliminate 4];',
        'firstEquations={'+','.join(fmt(poly) for poly in w1_first)+'};',
        'I=ideal firstEquations;',
        'print("W1_LINE_FIRST_ELIMINATION_START");',
        'E=eliminate({h4,h5,h6,h7},I);',
        'print("W1_LINE_FIRST_ELIMINATION_READY");print gens E;',
        'S=QQ[p,x];phi=map(S,R,{0,0,0,0,p,x});',
        'ES=ideal phi(gens E);',
        'tau=-(p+x^2+2);delta=((p-x^2-2)/2)^2;',
        'q=tau*(tau^2-delta)*(tau^2-2*delta)*(tau^2-3*delta)*((tau^2-2*delta)^2-3*delta^2);',
        'op=p*(2*x^2+1)*(p-x^2-2)*(x^2+2);',
        'J=saturate(ES+ideal(q),ideal(op));',
        'print("W1_LINE_FIRST_TORSION_RESULT");print gens gb J;',
        '']) )
    env['NAMES'][:]=line_names
    primitive_m2=stem.with_name(stem.name+'_line_component_primitive.m2')
    primitive_m2.write_text('\n'.join([
        '-- Exact primitive-cube-root line component over QQ(w), w^2+w+1=0.',
        'K=toField(QQ[ww]/ideal(ww^2+ww+1));',
        'R=K[h4,h5,h6,h7,a,x,MonomialOrder=>Eliminate 4];',
        'w=sub(K_0,R);',
        'firstEquations={'+','.join(fmt(poly) for poly in line_first)+'};',
        'I=ideal firstEquations;',
        'print("PRIMITIVE_LINE_FIRST_ELIMINATION_START");',
        'E=eliminate({h4,h5,h6,h7},I);',
        'print("PRIMITIVE_LINE_FIRST_ELIMINATION_READY");print gens E;',
        'S=K[a,x];phi=map(S,R,{0,0,0,0,a,x});',
        'ES=ideal phi(gens E);w=sub(K_0,S);',
        'tau=w^2*(1-a^2-x^2);delta=w*((a^2-x^2-2)/2)^2;',
        'q=tau*(tau^2-delta)*(tau^2-2*delta)*(tau^2-3*delta)*((tau^2-2*delta)^2-3*delta^2);',
        'op=a*(2*x^2+1)*(a^2-x^2-2)*(2*a^2-3);',
        'J=saturate(ES+ideal(q),ideal(op));',
        'print("PRIMITIVE_LINE_FIRST_TORSION_RESULT");print gens gb J;',
        '']) )
    stem.with_suffix('.json').write_text(json.dumps({
        'status':'new compact original-coordinate generic two-node reduction; no elimination claimed',
        'chart':'B1=B2=C1=1,C2=w,w^3=1; finite cover by factor scales and actual C0 torus',
        'generic_open':'B1*B2*C1*C2*kappa1*kappa2*Delta1*Delta2*(tau^2-4delta)!=0 before normalization',
        'remaining_boundary_strata':['kappa1=kappa2=0','B1*B2*C1*C2=0 with both kappa nonzero','integral nodal roots','smooth roots'],
        'excluded_mixed_kappa':'exactly one kappa zero forces that factor to be the quadric direction',
        'norm_symbol_equations':list(map(fmt,norms)),
        'first_count':8,'eliminated_first_rows':[0,1,2,3,12,13,14,15],
        'first_free_h':['h4','h5','h6','h7'],
        'spectral_torsion':'tau*(tau^2-delta)*(tau^2-2delta)*(tau^2-3delta)*((tau^2-2delta)^2-3delta^2)=0',
        'global_cube_uses_actual_22_by_22_symbol_splitting':True,
    },indent=2)+'\n')
    print(m2)
    print(line_m2)
    print(w1_m2)
    print(primitive_m2)


if __name__=='__main__':main()
