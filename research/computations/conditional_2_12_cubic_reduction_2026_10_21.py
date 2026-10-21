#!/usr/bin/env python3
"""Exact small q-line tests, retaining orbit collisions on the endpoint chart.

The eleven-variable compact K1 and norm-symbol presentation is an input from
the new October 20 exporter. This script adds the exact all-strata q-line
condition and identifies its free-orbit Schur determinant geometrically.
"""
import ast
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from itertools import permutations
import json

HERE=Path(__file__).resolve().parent
src=HERE/'conditional_2_12_elimination_2026_10_20.py'
tree=ast.parse(src.read_text())
stop=next(i for i,n in enumerate(tree.body) if isinstance(n,ast.Assign)
          and any(isinstance(t,ast.Name) and t.id=='stem' for t in n.targets))
env={'__file__':str(src),'__name__':'oct21_qline_reuse'}
exec(compile(ast.Module(body=tree.body[:stop],type_ignores=[]),str(src),'exec'),env)
ca,cs,cm,const,var,normalized,fmt=(env[x] for x in ('ca','cs','cm','const','var','normalized','fmt'))
G=env['G'];names=env['names']
D=[const(1),var(1),var(2),var(3),const(1)]

def remainder(p):
    p=list(p)
    for degree in range(len(p)-1,3,-1):
        leading=p[degree]
        for j,c in enumerate(D):
            p[degree-4+j]=ca(p[degree-4+j],cs(cm(leading,c),-1))
        assert not p[degree]
    return p[:4]+[{} for _ in range(max(0,4-len(p)))]

def convolution(a,b):
    out=[{} for _ in range(len(a)+len(b)-1)]
    for i,p in enumerate(a):
        for j,q in enumerate(b):
            out[i+j]=ca(out[i+j],cm(p,q))
    return out

def determinant(a):
    out={}
    for perm in permutations(range(len(a))):
        parity=sum(perm[i]>perm[j] for i in range(len(a)) for j in range(i+1,len(a)))
        term=const((-1)**parity)
        for i,j in enumerate(perm):term=cm(term,a[i][j])
        out=ca(out,term)
    return out

GG={}
for comp in range(4):
    for j,p in G[comp].items():
        degree=3-comp+j
        GG[degree]=ca(GG.get(degree,{}),cs(normalized(p),Q(-1,2)**(3-comp)))
dd={j:cs(D[j+1],j+1) for j in range(4)}
for j,p in GG.items():dd[j+2]=ca(dd.get(j+2,{}),cs(p,-12))
simple=remainder([dd.get(j,{}) for j in range(7)])
alpha=[normalized(env['alpha'].get(j,{})) for j in range(9)]
alpha_cols=[remainder([{}]*j+alpha) for j in range(4)]
alpha_matrix=[list(row) for row in zip(*alpha_cols)]
all_strata=[ca(*(cm(alpha_matrix[i][j],simple[j]) for j in range(4))) for i in range(4)]

d1,d2,d3=var(1),var(2),var(3)
J=[[ca(d2,cs(cm(d1,d1),-1)),cs(d1,-1),const(1)],
   [ca(cs(d1,-2),cm(d2,d3)),ca(const(-1),cs(cm(d1,d3),-1),cm(d2,d2)),ca(cs(d3,2),cs(cm(d1,d2),-1))],
   [const(1),d3,ca(d2,cs(cm(d3,d3),-1))]]
detJ=determinant(J)
det_alpha=determinant(alpha_matrix)
assert det_alpha == cs(cm(detJ,detJ),81)

# The three norm-symbol equations depend on y0,T=y1-4y3,y2. Their
# coefficient matrix, after harmless row rescaling, is exactly J.
first=[p for p in env['normalizedFirst'] if p]
symbol=[normalized(env['symbol'][i]) for i in (3,6,9)]
keep=[1,2,3,5,6,7,8,13,14,15,16]
def fmtlist(ps):return '{'+','.join(fmt(p) for p in ps)+'}'
def fmtmat(a):return 'matrix{'+','.join(fmtlist(row) for row in a)+'}'
stem=Path(__file__).with_suffix('')
lines=[
 '-- Exact q-line necessary test, endpoint chart d0=d4=1.',
 '-- norm alpha is imposed; actual-pair necessity uses separate Q-cycle proof.',
 '-- Both simple and collision-retaining q-line equations are exported.',
 'R=QQ['+','.join(names[i] for i in keep)+',orbitInverse,MonomialOrder=>GRevLex];',
 'firstEquations='+fmtlist(first)+';',
 'symbolEquations='+fmtlist(symbol)+';',
 'qlineSimpleEquations='+fmtlist(simple)+';',
 'alphaMultiplicationMatrix='+fmtmat(alpha_matrix)+';',
 'qlineAllStrataEquations=flatten entries(alphaMultiplicationMatrix*transpose matrix{qlineSimpleEquations});',
 'orbitDeterminant='+fmt(detJ)+';',
 'qlineAllStrataIdeal=ideal join(firstEquations,symbolEquations,qlineAllStrataEquations);',
 'qlineFreeOrbitIdeal=ideal join(firstEquations,symbolEquations,qlineSimpleEquations,{orbitInverse*orbitDeterminant-1});',
 'print "QLINE_ENDPOINT_11VAR_AND_FREEORBIT_12VAR_MODELS_READY";',
 '-- No Groebner basis or saturation run by this input file.',
]
stem.with_suffix('.m2').write_text('\n'.join(lines)+'\n')
meta={'status':'new exact q-line reduction; no emptiness assertion',
      'input':str(src),'input_sha256':sha256(src.read_bytes()).hexdigest(),
      'chart':'d0=d4=1 finite projective/torus cover over nonzero endpoints',
      'variables':[names[i] for i in keep],
      'equations':{'K1':len(first),'norm_symbol':len(symbol),'qline':4},
      'simple_qline':'rem_D(Dprime-12*z^2*G)',
      'all_strata_qline':'rem_D(alpha*(Dprime-12*z^2*G)); equivalent to rem_D(Nprime_T(z^3)-4*alpha*G) since 3*z^2 is a unit modulo D with D0=1',
      'alpha_multiplication_matrix':[[fmt(p) for p in row] for row in alpha_matrix],
      'alpha_multiplication_determinant':'81*orbitDeterminant^2',
      'orbit_determinant':fmt(detJ),
      'symbol_Schur_matrix':[[fmt(p) for p in row] for row in J],
      'symbol_free_coordinates':'y0,T=y1-4*y3,y2; y3 remains free and adds4*y3*(u+z*v/2)^2',
      'orbit_resultant_identity':'orbitDeterminant=Res_z(z^3-omega^2*d2*z+d1,-omega*d2*z^2+omega^2*d2*d3*z+1-d1*d3), omega^2+omega+1=0',
      'simple_qline_remainders':[fmt(p) for p in simple],
      'all_strata_qline_term_counts':[len(p) for p in all_strata],
      'limitations':'Endpoint-zero strata remain outside this finite normalization chart. Norm-alpha necessity is a separate proposed Q-cycle theorem; no global pair is constructed.'}
stem.with_suffix('.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps({'model':str(stem.with_suffix('.m2')),'orbit_determinant':fmt(detJ),
                  'alpha_determinant_identity_verified':True,
                  'all_strata_term_counts':[len(p) for p in all_strata]},indent=2))
