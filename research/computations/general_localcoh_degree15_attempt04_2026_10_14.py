#!/usr/bin/env python3
"""Generate an unlaunched exact-field, single-block-inverse fallback.

The modular block diagnostic selects indices only. Its rank conclusions are
not mathematical premises: all characteristic-zero inverse/complement and
dual identities are asserted by the generated source. No inherited verifier
is invoked, and no current computation is stopped or launched here.
"""
from pathlib import Path
import ast
import hashlib
import json
import re

HERE=Path(__file__).resolve().parent
BASE='general-localcoh-family2-degree15-corank-one-2026-10-14-attempt04'
PRIOR=HERE/'general-localcoh-family2-degree15-corank-one-2026-10-14-attempt03.m2'
DIAGNOSTIC=HERE/'general-localcoh-degree15-sparse-block-2026-10-14-diagnostic.json'

def m2expr(node): return ast.unparse(node).replace('**','^')

def main():
    prior=PRIOR.read_text(); diag=json.loads(DIAGNOSTIC.read_text())
    assert hashlib.sha256(prior.encode()).hexdigest()==diag['source_sha256']
    lines=prior.splitlines()
    field_line=next(l for l in lines if l.startswith('Q0=QQ[z];'))
    fexpr=field_line.split(';f=',1)[1].rstrip(';').replace('z','k')
    out=[
        '-- NEW exact degree15 fallback; selected block diagnostic is not proof.',
        '-- Accepted rational pencil/tensor interpretation consumed without inherited replay.',
        'P=QQ[k]; f='+fexpr+'; K=toField(P/ideal(f)); k=sub(k,K);',
        'print("attempt04: degree15 field constructed; specializing seeds before elimination"); flush stdio;',
    ]
    denominators=0
    for line in lines:
        match=re.fullmatch(r'(z\d+)=sub\(\((.*)\),K\);',line)
        if not match:continue
        node=ast.parse(match[2].replace('^','**'),mode='eval').body
        if isinstance(node,ast.BinOp) and isinstance(node.op,ast.Div):
            denvar='seedDenominator'+match[1][1:]
            out.extend([
                denvar+'=sub(('+m2expr(node.right)+'),K);',
                'assert('+denvar+'!=0);',
                match[1]+'=sub(('+m2expr(node.left)+'),K)/'+denvar+';',
            ])
            denominators+=1
        else:out.append(line)
    out.extend(l for l in lines if any(l.startswith(s) for s in ['A=matrix','B=matrix','v=matrix','w=matrix']))
    out.extend([
        'q=18; p=56;',
        'print("attempt04: canonical field pencil constructed; '+str(denominators)+' seed denominators checked nonzero"); flush stdio;',
        'pivotRows={'+','.join(map(str,diag['selected_rows']))+'};',
        'pivotColumns={'+','.join(map(str,diag['selected_columns']))+'};',
        'missingColumn='+str(diag['missing_column'])+';',
        'chosenBlock=matrix apply(pivotRows,ii->apply(pivotColumns,jj->B_(ii,jj)));',
        'print("attempt04: inverting selected17x17 block once"); flush stdio;',
        'chosenInverse=id_(K^17)//chosenBlock;',
        'assert(chosenBlock*chosenInverse==id_(K^17));',
        'assert(chosenInverse*chosenBlock==id_(K^17));',
        'print("attempt04: exact block inverse checked"); flush stdio;',
        'D=matrix apply(toList(0..q-1),ii->apply(toList(0..p-1),jj->if member(ii,pivotColumns) and member(jj,pivotRows) then chosenInverse_(position(pivotColumns,kk->kk==ii),position(pivotRows,kk->kk==jj)) else 0_K));',
        'DB=D*B;',
        'h=matrix apply(toList(0..q-1),ii->{(if ii==missingColumn then 1_K else 0_K)-DB_(ii,missingColumn)});',
        'eMissing=matrix{apply(q,ii->if ii==missingColumn then 1_K else 0_K)};',
        'assert(h_(missingColumn,0)==1_K);',
        'assert(B*h==0);',
        'assert(DB==id_(K^q)-h*eMissing);',
        'a=A*h;',
        'i=0;j=0;delta=0_K;',
        'for ii from 0 to q-2 do for jj from ii+1 to q-1 do if delta==0 then (corankMinor=h_(ii,0)*a_(jj,0)-h_(jj,0)*a_(ii,0); if corankMinor!=0 then (i=ii;j=jj;delta=corankMinor));',
        'assert(delta!=0);',
        'ei=matrix{apply(q,kk->if kk==i then 1_K else 0_K)};',
        'ej=matrix{apply(q,kk->if kk==j then 1_K else 0_K)};',
        'Fh=(a_(j,0)*ei-a_(i,0)*ej)/delta;',
        'Fa=(-h_(j,0)*ei+h_(i,0)*ej)/delta;',
        'assert(Fh*h==matrix{{1_K}} and Fh*a==0);',
        'assert(Fa*h==0 and Fa*a==matrix{{1_K}});',
        'c=D*w;c=c-h*(Fh*c);',
        'assert(B*c==w and Fh*c==0);',
        'D0=(id_(K^q)-h*Fh)*D;',
        'assert(D0*B==id_(K^q)-h*Fh);',
        'print("attempt04: exact complement, observability and target compatibility checked without generic rerank"); flush stdio;',
        'linrows=apply(select(toList(0..q-1),jj->jj!=i and jj!=j),jj->(matrix{apply(q,kk->if kk==jj then 1_K else 0_K)}-h_(jj,0)*Fh-a_(jj,0)*Fa));',
        'assert(all(linrows,rr->rr*h==0 and rr*a==0));',
        'linN0=apply(linrows,rr->(transpose rr)||(-transpose(rr*A*D)));',
        'linN1=apply(linrows,rr->(matrix apply(q,ii->{0_K}))||(-transpose(rr*D)));',
        'gN0=(transpose Fh)||(-transpose(Fh*A*D));',
        'gN1=(-transpose Fa)||(transpose((Fa*A-Fh)*D));',
        'gN2=(matrix apply(q,ii->{0_K}))||(transpose(Fa*D));',
    ])
    # Copy the purely univariate obstruction/normalization construction. Replace
    # the prior field name, but preserve every exact identity and output target.
    start=next(i for i,l in enumerate(lines) if l.startswith('R=K15[lambda]'))
    for line in lines[start:]:
        line=line.replace('K15','K').replace('attempt03','attempt04')
        # A nonhomogeneous polynomial Matrix retains degree metadata: compare
        # the sole normalized target entry, not equality of graded maps.
        line=line.replace('assert(transpose NN*UU==matrix{{1_R}});','assert((transpose NN*UU)_(0,0)==1_R);')
        out.append(line)
    source=HERE/(BASE+'.m2');source.write_text('\n'.join(out)+'\n')
    record={
        'status':'prepared_not_launched',
        'source':source.name,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'parent_source':PRIOR.name,'parent_source_sha256':diag['source_sha256'],
        'block_diagnostic':DIAGNOSTIC.name,'block_diagnostic_sha256':hashlib.sha256(DIAGNOSTIC.read_bytes()).hexdigest(),
        'diagnostic_scope':'Selects indices only; no finite-field rank conclusion accepted as proof.',
        'exact_checks':['all seed denominators nonzero in full degree15 field','selected block left and right inverse','full B complement identity','B*h=0 and observability minor','actual bottom target compatibility','all seventeen polynomial obstruction annihilations','normalized dual target evaluation equals1','original tensor-coordinate72 equals1'],
        'new_verifier_required':'Run general_localcoh_family2_degree15_corank_one_certificate_2026_10_14.py --stem '+BASE+' after exact source succeeds.',
        'long_job_policy':'No process launched or stopped by this generator; attempt03 remains untouched.',
    }
    validation=HERE.parent/'validation'/'2026-10-14-localcoh-degree15-attempt04'
    validation.mkdir(exist_ok=True)
    (validation/'prepared-lineage.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))

if __name__=='__main__':main()
