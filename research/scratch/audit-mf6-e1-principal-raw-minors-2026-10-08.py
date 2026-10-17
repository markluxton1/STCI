from pathlib import Path
import json,time
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import QQ
p,r=s.symbols('p r')
b=Path(__file__).parent
j=json.loads((b/'session-mf6-e1-principal-contact-2026-10-08.json').read_text())
k=json.loads((b/'session-mf6-e1-principal-minors-2026-10-08.json').read_text())
H=s.sympify(j['H']); C=s.Matrix([[s.sympify(c) for c in row] for row in j['reduced_contact']])
for col,fac in enumerate(k['first_frame_column_divisors']):
 for row in range(C.rows): C[row,col]=s.cancel(C[row,col]/s.sympify(fac))
D=C[:6,:]
for i,fac in enumerate(k['contact_row_units']):
 for col in range(D.cols): D[i,col]=s.cancel(D[i,col]/s.sympify(fac))
assert all(s.denom(e).free_symbols==set() for e in D)
minors=[]
for omitted in reversed(range(7)):
 tick=time.monotonic(); minor=D[:,[i for i in range(7) if i!=omitted]]
 determinant=DomainMatrix.from_Matrix(minor).convert_to(QQ.poly_ring(p,r)).det().as_expr()
 fl=s.factor_list(determinant)
 print('cofactor',omitted,'seconds',time.monotonic()-tick,'factors',[(s.total_degree(f),n) for f,n in fl[1]],flush=True)
 minors.append({'omitted':omitted,'coefficient':str(fl[0]),'factors':[[str(f),int(n)] for f,n in fl[1]],'raw':str(determinant)})
 (b/'audit-mf6-e1-principal-raw-minors-2026-10-08.json').write_text(json.dumps({'H':str(H),'minors':minors},indent=2)+'\n')
print('DONE',flush=True)
