#!/usr/bin/env python3
"""Bind literal two-chart residue forms to fresh complete35 replay output."""
from pathlib import Path
import ast,hashlib,json
import sympy as s
from sympy.polys.domains import QQ
OUT=Path(__file__).resolve().parent
source=OUT/'research/computations/verify_mf6_e1_d1_principal_boundary_residues_2026_10_08.py'
boundary=OUT/'research/computations/verify_mf6_e1_d1_principal_boundaries_2026_10_08_all.json'
tree=ast.parse(source.read_text())
assignment=next(item for item in tree.body if isinstance(item,ast.Assign) and
                any(isinstance(target,ast.Name) and target.id=='literal_fibers' for target in item.targets))
literals=ast.literal_eval(assignment.value)
fibres={row['name']:row for row in json.loads(boundary.read_text())['fibers']}
x0,x1,x2,x3,z,w,U,V,eps=s.symbols('x0 x1 x2 x3 z w U V eps')
matched=[]
for row in literals:
    name=row['name'];actual=fibres[name]
    field=QQ.algebraic_field(s.sqrt(-2)) if 'sqrt' in row['r'] else QQ
    for key in ['r','p']:
        assert field.from_sympy(s.sympify(row[key])-s.sympify(actual[key]))==field.zero
    for key in ['delta','Gamma']:
        assert s.Poly(s.sympify(row[key])-s.sympify(actual[key]),z,domain=field).is_zero
    assert len(row['quartic_basis'])==len(actual['quartic_basis'])==1
    assert s.Poly(s.sympify(row['quartic_basis'][0])-s.sympify(actual['quartic_basis'][0]),x0,x1,x2,x3,domain=field).is_zero
    assert all(field.from_sympy(s.sympify(v)-s.sympify(a))==field.zero for v,a in zip(row['quadratic_cocycle'],actual['quadratic_cocycle']))
    matched.append(name)

# Derive the normal-linear transition by actual projective coordinate change.
den=z**4+eps*U+s.Rational(3,2)*z*eps*V
w_actual=(z**3+eps*V)/den
Vraw=z/den-w_actual**3
Uraw=1/den-w_actual**4-s.Rational(3,2)*w_actual*Vraw
assert s.cancel(s.diff(Vraw,eps).subs(eps,0)-2*U/z**7)==0
assert s.cancel(s.diff(Uraw,eps).subs(eps,0)-V/(2*z**7))==0
# Thus Uop=Vraw/2,Vop=2Uraw have scalar z^-7 transitions. Their
# opposite affine chart is x1=w³+2Uop,x0=w4+Vop/2+3wUop.
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'status':'PASS exact literal-source binding and actual balanced first-normal transition',
 'source_sha256':sha(Path(__file__)),
 'input_sha256':{str(source.relative_to(OUT)):sha(source),str(boundary.relative_to(OUT)):sha(boundary)},
 'matched_complete35_fibres':matched,
 'raw_opposite_normal_transition':'(Uraw,Vraw)=z^-7*(V/2,2U)',
 'balanced_opposite_chart':'x3=1,x2=w,x1=w³+2Uop,x0=w4+Vop/2+3wUop',
 'scope':'No carrier geometry or additional mate claim'}
(OUT/'residue-input-comparison-result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
