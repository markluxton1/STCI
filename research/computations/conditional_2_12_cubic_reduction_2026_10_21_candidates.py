#!/usr/bin/env python3
"""Exact full-C3 test at the four free-orbit q-line candidates.

Uses only the new structured full-C3 exporter, no inherited theorem replay.
All global sextic coefficients are the fixed rational splitting of the actual
23-dimensional k-linear source; eta is its sole q^3 ambiguity.
"""
import ast,json
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
HERE=Path(__file__).resolve().parent
src=HERE/'conditional_2_12_elimination_2026_10_20.py'
t=ast.parse(src.read_text())
stop=next(i for i,n in enumerate(t.body) if isinstance(n,ast.Assign)
          and any(isinstance(x,ast.Name) and x.id=='stem' for x in n.targets))
e={'__file__':str(src),'__name__':'candidate_fullC3'}
exec(compile(ast.Module(body=t.body[:stop],type_ignores=[]),str(src),'exec'),e)

def add(*ps):
    out={}
    for p in ps:
        for m,c in p.items():out[m]=out.get(m,Q(0))+c
    return {m:c for m,c in out.items() if c}
def scale(p,c):return {m:c*x for m,x in p.items() if c*x}
def reduce_h(p):
    p=dict(p)
    for hp in range(max((m[0] for m in p),default=0),3,-1):
        for ep in list({m[1] for m in p if m[0]==hp}):
            c=p.pop((hp,ep),Q(0))
            if c:
                p[(hp-4,ep)]=p.get((hp-4,ep),Q(0))+c/Q(162)
                p[(hp-2,ep)]=p.get((hp-2,ep),Q(0))-c*Q(5,72)
    return {m:c for m,c in p.items() if c}
def mul(p,q):
    out={}
    for (h,a),c in p.items():
        for (j,b),d in q.items():out[(h+j,a+b)]=out.get((h+j,a+b),Q(0))+c*d
    return reduce_h(out)
def const(c):return {(0,0):Q(c)} if c else {}
h={(1,0):Q(1)};eta={(0,1):Q(1)}
tt={(3,0):Q(27,4),(1,0):Q(15,32)}
d2=add(scale(tt,16),scale(h,-12))
rep={1:{},2:d2,3:{},5:{},6:add(scale(h,6),scale(tt,-4)),7:{},8:tt,
     13:scale(h,-2),14:{},15:{},16:h,21:eta}
def substitute(p):
    out={}
    for m,c in p.items():
        term=const(c)
        for i in m:
            assert i in rep, i
            term=mul(term,rep[i])
        out=add(out,term)
    return reduce_h(out)
def fmt(p):
    terms=[]
    for (hp,ep),c in sorted(p.items()):
        mon='*'.join((('h' if hp==1 else f'h^{hp}') if hp else '',
                      ('eta' if ep==1 else f'eta^{ep}') if ep else '')).strip('*')
        coeff='' if abs(c)==1 and mon else str(abs(c))
        terms.append(('-' if c<0 else '+')+coeff+('*' if coeff and mon else '')+mon)
    s=''.join(terms)
    return s[1:] if s.startswith('+') else(s or '0')

full_cubic=[substitute(e['normalized'](p)) for p in e['cubic']]
unique=[]
for p in full_cubic:
    if p and p not in unique:unique.append(p)
stem=Path(__file__).with_suffix('')
lines=[
 '-- Exact four-candidate full global sextic cubic test.',
 'R=QQ[h,eta,MonomialOrder=>GRevLex];',
 'candidatePolynomial=648*h^4+45*h^2-4;',
 'cubicEquations={'+','.join(fmt(p) for p in unique)+'};',
 'candidateCubicIdeal=ideal join({candidatePolynomial},cubicEquations);',
 'print "CANDIDATE_FULL_C3_MODEL_READY";',
 '-- No Groebner basis run by this exporter.',
]
stem.with_suffix('.m2').write_text('\n'.join(lines)+'\n')
meta={'status':'exact candidate test; no conclusion until verified computation',
      'input_sha256':sha256(src.read_bytes()).hexdigest(),
      'candidate_polynomial':'648h^4+45h^2-4',
      't':'27h^3/4+15h/32=1/(24h) modulo candidate polynomial',
      'd2':'108h^3-9h/2',
      'first_h_retained':'h4=-2h,h5=h6=0,h7=h',
      'unique_nonzero_full_cubic_equations':[fmt(p) for p in unique],
      'raw_equation_count':len(full_cubic),'unique_nonzero_count':len(unique),
      'global_coefficients':'Fixed actual k-linear sextic splitting from22 image columns; eta is exactly q^3 coefficient.'}
stem.with_suffix('.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2))
