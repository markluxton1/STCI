from pathlib import Path
import json,hashlib,re
import sympy as s
p,r,b=s.symbols('p r b');HERE=Path(__file__).parent
source=HERE/'derive-mf6-principal-weighted-kernel-2026-10-08.json';data=json.loads(source.read_text());output=HERE/'mf6-principal-weighted-kernel-2026-10-08.txt';lines=output.read_text().splitlines();assert lines[0]=='{{9}, {9}, {10}}'
entries=lines[1].replace(' ','');rows=entries[2:-2].split('},{');assert len(rows)==18
G=[]
for row in rows:
 fields=row.split(',');assert len(fields)==3
 assert all(re.fullmatch(r'[0-9prb+*/^()\-]+',field) for field in fields)
 G.append([s.sympify(field.replace('^','**')) for field in fields])
H=s.sympify(data['H']);M1=s.Matrix([[s.sympify(e) for e in row] for row in data['first']]);M2=s.Matrix([[s.sympify(e) for e in row] for row in data['second']]);GM=s.Matrix(G)
for j,degree in enumerate((9,9,10)):
 for i in range(18):
  assert all(2*pp+rr+bb==degree+data['column_weights'][i] for (pp,rr,bb),cc in s.Poly(GM[i,j],p,r,b).terms() if cc)
 for mat in (M1,M2):
  for i in range(mat.rows):
   assert s.rem(s.expand(sum(mat[i,k]*GM[k,j] for k in range(18))),H,p)==0
 print('PASS exact homogeneous generator',j,'degree',degree,flush=True)
record={'status':'PASS exact three polynomial quartic-contact syzygies',
 'not_claimed':'Independent completeness of kernel module, all fiber basepoint freeness, or exact nonnormality subset',
 'H':str(H),'column_weights':data['column_weights'],'generator_degrees':[9,9,10],
 'kernel_columns':[[str(GM[i,j]) for i in range(18)] for j in range(3)],
 'forms':data['forms'],'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'm2_export_sha256':hashlib.sha256(output.read_bytes()).hexdigest(),
 'audit_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'mf6-principal-weighted-kernel-2026-10-08.json').write_text(json.dumps(record,indent=2)+'\n')
print('SAVED exact polynomial projective carrier syzygies; choose nonzero column or retain base fibers',flush=True)
