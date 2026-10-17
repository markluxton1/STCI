"""Seven exact contact cofactors on the principal elliptic chart.

Input is the reproducible complete contact reconstruction. All column
factors and row units are retained in the output. No universal exclusion.
"""
from pathlib import Path
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import QQ
p,r=s.symbols('p r')
src=Path(__file__).with_name('session-mf6-e1-principal-contact-2026-10-08.json')
j=json.loads(src.read_text())
H=s.sympify(j['H'])
N=s.Matrix([[s.sympify(c) for c in row] for row in j['first_kernel']])
C=s.Matrix([[s.sympify(c) for c in row] for row in j['reduced_contact']])
column_factors=[]
for col in range(N.cols):
    factor=s.factor(s.gcd_list(list(N[:,col])))
    column_factors.append(factor)
    N[:,col]=N[:,col].applyfunc(lambda e:s.cancel(e/factor))
    C[:,col]=C[:,col].applyfunc(lambda e:s.cancel(e/factor))
assert all(e==0 for e in C[7:,:])
assert all(s.rem(e,H,p)==0 for e in C[6,:])
row_units=[p-r,p-r,p-r,p-r,p*(p-r),p*p*(p-r)]
D=s.zeros(6,7)
for i in range(6):
    for k in range(7):
        e=s.cancel(C[i,k]/row_units[i])
        assert s.denom(e).free_symbols==set()
        D[i,k]=s.rem(e,H,p)
print('exact reduced6x7 contact matrix, max entryterms',max(len(s.Poly(e,p,r).terms()) for e in D),flush=True)
minors=[]
for omitted in range(7):
    minor=D[:,[i for i in range(7) if i!=omitted]]
    determinant=DomainMatrix.from_Matrix(minor).convert_to(QQ.poly_ring(p,r)).det()
    polynomial=s.expand(determinant.as_expr())
    remainder=s.factor(s.rem(polynomial,H,p))
    print('cofactor',omitted,'terms',len(s.Poly(remainder,p,r).terms()),'factor',str(remainder)[:300],flush=True)
    minors.append(remainder)
record={'scope':'H=0, pP(p-r)(2r-1)(2p-4r²-4r-1)!=0; remaining chart fibers are separate',
        'H':str(H),'first_frame_column_divisors':list(map(str,column_factors)),
        'contact_row_units':list(map(str,row_units)),
        'contact_6x7':[[str(e) for e in row] for row in D.tolist()],
        'seven_cofactor_remainders':list(map(str,minors))}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print('SAVED complete seven-generator contact rank-drop ideal on declared open chart',flush=True)
