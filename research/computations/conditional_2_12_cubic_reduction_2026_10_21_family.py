#!/usr/bin/env python3
"""Free-mu3-orbit symbol family, with actual K1 and q-line cubic tests.

The norm-symbol Schur system has polynomial solution
y0=-d1/4, y1=4t-d2/2, y2=-d3/4. Its coefficient determinant is exactly
the orbit-collision determinant; hence this is an equivalence on that open.
"""
import ast,json
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
HERE=Path(__file__).resolve().parent
src=HERE/'conditional_2_12_cubic_reduction_2026_10_21.py'
t=ast.parse(src.read_text())
stop=next(i for i,n in enumerate(t.body) if isinstance(n,ast.Assign)
          and any(isinstance(x,ast.Name) and x.id=='stem' for x in n.targets))
e={'__file__':str(src),'__name__':'family_export'}
exec(compile(ast.Module(body=t.body[:stop],type_ignores=[]),str(src),'exec'),e)
ca,cs,cm,var,const,fmt=(e[x] for x in ('ca','cs','cm','var','const','fmt'))
replacement={5:cs(var(1),Q(-1,4)),6:ca(cs(var(8),4),cs(var(2),Q(-1,2))),7:cs(var(3),Q(-1,4))}
def sub(p):
    out={}
    for m,c in p.items():
        term=const(c)
        for i in m:term=cm(term,replacement.get(i,var(i)))
        out=ca(out,term)
    return out
assert all(not sub(p) for p in e['symbol'])
first=[sub(p) for p in e['first']]
simple=[sub(p) for p in e['simple']]
keep=[1,2,3,8,13,14,15,16]
names=e['names']
def fmtlist(ps):return '{'+','.join(fmt(p) for p in ps)+'}'
stem=Path(__file__).with_suffix('')
lines=[
 '-- Free orbit family; d0=d4=1. y3 is t.',
 '-- Symbol equations solved exactly on orbit determinant !=0.',
 'R=QQ['+','.join(names[i] for i in keep)+',MonomialOrder=>GRevLex];',
 'firstEquations='+fmtlist(first)+';',
 'qlineEquations='+fmtlist(simple)+';',
 'print "EIGHT_VARIABLE_FAMILY_EQUATIONS_READY";',
 'familyIdeal=ideal join(firstEquations,qlineEquations);',
 'print "EIGHT_VARIABLE_FAMILY_IDEAL_READY";',
 '-- A unit here excludes a closed enlargement of the free-orbit chart.',
 '-- No Groebner basis is run by this file.',
]
stem.with_suffix('.m2').write_text('\n'.join(lines)+'\n')
meta={'status':'new exact free-orbit reduction, not emptiness',
      'input_sha256':sha256(src.read_bytes()).hexdigest(),
      'symbol_solution':{'y0':'-d1/4','y1':'4*y3-d2/2','y2':'-d3/4'},
      'f':'a=(4t,d3/2,1), b=(-d1/4,4t-d2/2,-d3/4), c=(1/4,d1/8,t)',
      'symmetric_curve':'8*f(z,-w/2,1)=(8t+d3*z+2*z^2)*w^2+(d1+(2*d2-16t)*z+d3*z^2)*w+(2+d1*z+8t*z^2)',
      'variables':[names[i] for i in keep],
      'equations':{'K1':len(first),'qline':len(simple)},
      'term_counts':{'K1':[len(p) for p in first],'qline':[len(p) for p in simple]},
      'limitations':'Equivalent symbol family only on orbit determinant nonzero; qline simple equivalence has the same open. Boundary not discarded.'}
stem.with_suffix('.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2))
