#!/usr/bin/env python3
"""Export only the small q-line cubic necessary test in the normalized chart.

Reuses the new compact exporter construction without executing its file-writing
footer. No accepted proofs or large elimination are run by this script.
"""
import ast
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json

HERE=Path(__file__).resolve().parent
src=HERE/'conditional_2_12_elimination_2026_10_20.py'
tree=ast.parse(src.read_text())
stop=next(i for i,n in enumerate(tree.body) if isinstance(n,ast.Assign)
          and any(isinstance(t,ast.Name) and t.id=='stem' for t in n.targets))
env={'__file__':str(src),'__name__':'qline_compact_reuse'}
exec(compile(ast.Module(body=tree.body[:stop],type_ignores=[]),str(src),'exec'),env)
ca,cs,cm,const,var,normalized,fmt=(env[x] for x in ('ca','cs','cm','const','var','normalized','fmt'))
G=env['G'];names=env['names']
GG={}
for comp in range(4):
    for j,p in G[comp].items():
        degree=3-comp+j
        GG[degree]=ca(GG.get(degree,{}),cs(normalized(p),Q(-1,2)**(3-comp)))
D=[const(1),var(1),var(2),var(3),const(1)]
dd={j:cs(D[j+1],j+1) for j in range(4)}
for j,p in GG.items():
    dd[j+2]=ca(dd.get(j+2,{}),cs(p,-12))
remainder=[dd.get(j,{}) for j in range(7)]
for degree in range(6,3,-1):
    leading=remainder[degree]
    for j,p in enumerate(D):
        remainder[degree-4+j]=ca(remainder[degree-4+j],cs(cm(leading,p),-1))
    assert not remainder[degree]
qrem=remainder[:4]
first=[p for p in env['normalizedFirst'] if p]
symbol=[normalized(env['symbol'][i]) for i in (3,6,9)]
keep=[1,2,3,5,6,7,8,13,14,15,16]
def fmtlist(ps):return '{'+','.join(fmt(p) for p in ps)+'}'
stem=Path(__file__).with_suffix('')
lines=[
 '-- q-line necessary cubic test only: endpoint chart d0=d4=1.',
 '-- K1 eight equations after exact h collapse; norm-symbol three cubics.',
 '-- qrem=rem_D(Dprime-12*z^2*G), G=G0(z,-z/2,1).',
 '-- Necessity additionally needs gcd(alpha,D)=1; no claim on collision strata.',
 'R=QQ['+','.join(names[i] for i in keep)+',MonomialOrder=>GRevLex];',
 'firstEquations='+fmtlist(first)+';',
 'symbolEquations='+fmtlist(symbol)+';',
 'qlineEquations='+fmtlist(qrem)+';',
 'qlineIdeal=ideal join(firstEquations,symbolEquations,qlineEquations);',
 'print "QLINE_11_VARIABLE_MODEL_READY";',
 '-- No Groebner basis run by this input file.',
]
stem.with_suffix('.m2').write_text('\n'.join(lines)+'\n')
meta={'status':'new exact necessary incidence; no emptiness assertion',
      'input':str(src),'input_sha256':sha256(src.read_bytes()).hexdigest(),
      'chart':'d0=d4=1 finite projective/torus cover over nonzero endpoints',
      'variables':[names[i] for i in keep],'equations':{'K1':len(first),'norm_symbol':len(symbol),'qline':len(qrem)},
      'G_coefficients_ascending':[fmt(GG.get(i,{})) for i in range(5)],
      'qline_remainders':[fmt(p) for p in qrem],
      'qline_term_counts':[len(p) for p in qrem],
      'limitations':'For actual necessity need norm-alpha argument and gcd(alpha,D)=1; exceptional alpha-zero/cube-collision/endpoint strata retained separately.'}
stem.with_suffix('.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2))
