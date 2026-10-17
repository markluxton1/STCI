"""Bounded independent audit of the actual MF6 octic determinant.

Reconstructs the first generator's actual normal coefficient, fixed binary
gradient matrix, weights, modular certificate, and infinity padding. The
owner/root separately replays all three 23-row contact syzygies. Geometry
and the no-common-component Bezout argument are proved in the audit note.
"""
from pathlib import Path
import hashlib,json,time
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import GF

started=time.monotonic()
here=Path(__file__).resolve(); root=here.parents[1]; scratch=root/'scratch'
expected_inputs={
    'derive-mf6-principal-weighted-kernel-2026-10-08.json':'0da6eff927a635a81179ce631468e9d4f3fc89a1c78af1c7a6a8cd6cc81fe85d',
    'mf6-principal-weighted-kernel-2026-10-08.json':'4889f20b60fa094cde47992342701ebdf29a98413fc216b20f971550331cd9db',
    'session-mf6-e1-principal-contact-2026-10-08.json':'bc32db62b6d87e15300168a47f50d6bf3cd952d0d19b60ad52fc5ae8cdfa9818',
}
loaded={}
for name,digest in expected_inputs.items():
    payload=(scratch/name).read_bytes()
    assert hashlib.sha256(payload).hexdigest()==digest
    loaded[name]=json.loads(payload)
candidate_path=scratch/'session-mf6-principal-weighted-candidate-2026-10-09.json'
candidate_payload=candidate_path.read_bytes();candidate=json.loads(candidate_payload)
owner=root/'computations/verify_session_mf6_principal_weighted_candidate_2026_10_09.py'
owner_hash=hashlib.sha256(owner.read_bytes()).hexdigest()
assert owner_hash==candidate['source_sha256']=='78ed372321bb99c81003892e30ca48a253b56702d0a00e05c5347e7a93e17370'
assert candidate['input_sha256']==expected_inputs
contact=loaded['derive-mf6-principal-weighted-kernel-2026-10-08.json']
kernel=loaded['mf6-principal-weighted-kernel-2026-10-08.json']
old=loaded['session-mf6-e1-principal-contact-2026-10-08.json']
p,r,b,z=s.symbols('p r b z');x0,x1,x2,x3=s.symbols('x0 x1 x2 x3')
H=s.sympify(contact['H']); assert s.expand(H-s.sympify(kernel['H']))==0
assert s.expand(H.subs(b,1)-s.sympify(old['H']))==0
assert s.expand(H-s.sympify(candidate['H']))==0
H_poly=s.Poly(H,p,r,b,domain=s.ZZ)
assert H_poly.content()==1 and s.Poly(H,p).LC()==8
assert all(2*pp+rr+bb==6 for (pp,rr,bb),cc in H_poly.terms())
assert contact['row_weights']==list(range(1,12))+list(range(10,22))
assert contact['column_weights']==[1,0,2,3,4,5,6,1,3,4,5,6,7,7,8,9,9,10]
assert contact['forms']==kernel['forms']==old['I4'] and len(kernel['forms'])==18
assert kernel['generator_degrees']==[9,9,10]
for new_key,old_key in [('first','M1'),('second','M2')]:
    new=s.Matrix([[s.sympify(c) for c in row] for row in contact[new_key]])
    previous=s.Matrix([[s.sympify(c) for c in row] for row in old[old_key]])
    assert new.subs(b,1)==previous

# Actual first generator and ambient derivatives, independent of the
# contact matrices and the owner's h coefficient vector.
forms=list(map(s.sympify,kernel['forms']))
first=list(map(s.sympify,kernel['kernel_columns'][0]));assert len(first)==18
point_C={x0:1,x1:z,x2:z**3,x3:z**4}
fu=s.expand(sum(c*s.diff(F,x3).subs(point_C) for c,F in zip(first,forms)))
fv=s.expand(sum(c*(s.diff(F,x2)+s.Rational(3,2)*z*s.diff(F,x3)).subs(point_C)
                for c,F in zip(first,forms)))
rem=lambda expression:s.expand(s.rem(s.expand(expression),H,p))
A=1+r*z;B=b+p*z;frame_det=p-r*b
assert rem(A*fu+B*fv)==0
hraw=s.expand(-r*fu-p*fv)
hcoeff=[rem(hraw.coeff(z,j)) for j in range(9)]
h=s.expand(sum(c*z**j for j,c in enumerate(hcoeff)))
assert rem(hraw-h)==0
assert rem(frame_det*fu-B*h)==0
assert rem(frame_det*fv+A*h)==0
assert all(s.expand(a-s.sympify(c))==0 for a,c in zip(hcoeff,candidate['h_coefficient_vector']))
assert len(candidate['h_coefficient_vector'])==9
for j,c in enumerate(hcoeff):
    assert all(2*pp+rr+bb==11+j for (pp,rr,bb),value in s.Poly(c,p,r,b).terms() if value)

# Rebuild the actual fixed 7/7 binary-gradient Sylvester matrix.
grad_s=[(8-j)*hcoeff[j] for j in range(8)]
grad_t=[(j+1)*hcoeff[j+1] for j in range(8)]
def fixed_sylvester(coeff_s,coeff_t,degree):
    mat=s.zeros(2*degree)
    for i in range(degree):
        for j,c in enumerate(reversed(coeff_s)):mat[i,i+j]=c
        for j,c in enumerate(reversed(coeff_t)):mat[degree+i,i+j]=c
    return mat
matrix=fixed_sylvester(grad_s,grad_t,7)
saved=s.Matrix([[s.sympify(c) for c in row] for row in candidate['sylvester_matrix']])
assert matrix.shape==(14,14) and all(s.expand(c-d)==0 for c,d in zip(matrix,saved))
rows=list(range(18,25))+list(range(19,26));columns=list(range(14))
assert sum(rows)-sum(columns)==210
for i in range(14):
    for j in range(14):
        for powers,c in s.Poly(matrix[i,j],p,r,b).terms():
            if not c:continue
            assert 2*powers[0]+powers[1]+powers[2]==rows[i]-columns[j]
            den=int(s.denom(c));assert den>0 and den&(den-1)==0

ell=101;sample={p:4,r:2,b:1}
assert H.subs(sample)%ell==0
P=2*p+12*r*r+16*r*b+9*b*b;T=2*p-4*r*r-4*r*b-b*b
open_value=int((p*P*frame_det*(2*r-b)*T).subs(sample))%ell
assert open_value!=0
def mod(value):
    value=s.Rational(value)
    return int(s.numer(value))*pow(int(s.denom(value)),-1,ell)%ell
mod_matrix=matrix.subs(sample).applyfunc(mod)
det=int(DomainMatrix.from_Matrix(mod_matrix).convert_to(GF(ell)).det())%ell
assert det==22==candidate['modular_nonzero_certificate']['fixed_sylvester_determinant']
sample_coeff=[mod(c.subs(sample)) for c in hcoeff]
sample_h=s.Poly(sum(c*z**j for j,c in enumerate(sample_coeff)),z,modulus=ell)
assert sample_h.degree()==8 and s.gcd(sample_h,sample_h.diff()).degree()==0

# Fixed padding separates a simple infinity root from a multiple one.
# h=(s prod_{j=1}^7(t-j s)) has 8 distinct projective roots, including
# infinity; h=s² prod_{j=1}^6(t-j s) has a double infinity root.
simple=s.Poly(s.prod(z-j for j in range(1,8)),z)
multiple=s.Poly(s.prod(z-j for j in range(1,7)),z)
def gradient_matrix_of_affine_octic(poly):
    cc=[poly.nth(j) for j in range(9)]
    return fixed_sylvester([(8-j)*cc[j] for j in range(8)],
                           [(j+1)*cc[j+1] for j in range(8)],7)
assert gradient_matrix_of_affine_octic(simple).det()!=0
assert gradient_matrix_of_affine_octic(multiple).det()==0
assert fixed_sylvester([0]*8,[0]*8,7)==s.zeros(14)

record={
 'status':'PASS bounded independent actual-octic, matrix, weights, modular and infinity audit',
 'source_sha256':hashlib.sha256(here.read_bytes()).hexdigest(),
 'owner_source_sha256':owner_hash,'input_sha256':expected_inputs,
 'owner_result_sha256':hashlib.sha256(candidate_payload).hexdigest(),
 'checks':{'actual_firstnormal_from_18_forms':True,'direction_syzygy':True,
           'balanced_frame_clear_denominator_identities':True,'full_saved_h_vector_agrees':True,
           'actual14x14_matrix_agrees':True,'weight210_every_entry':True,
           'all_coefficient_denominators_powers2':True,'H_primitive_integer':True,
           'mod101_point_on_H_and_in_open':True,'open_product_mod101':open_value,
           'sample_h_coefficients_mod101':sample_coeff,'sample_fixed_determinant_mod101':det,
           'sample_octic_squarefree':True,'simple_infinity_root_padding_nonzero':True,
           'multiple_infinity_root_padding_zero':True,'zero_generator_octic_retained':True},
 'proof_scope':'Exact first generator coefficient and binary-gradient certificate. Accepted irreducibility of H and geometric necessity are inherited audited antecedents; Bezout proof is in companion independent note.',
 'not_repeated':'Full three-generator 23-row syzygy replay is separately run centrally. No factorization, finite zero-list, or all-mate exclusion is claimed.',
 'elapsed_seconds':round(time.monotonic()-started,3)}
out=scratch/'audit-session-mf6-weighted-candidate-2026-10-09.json'
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2),flush=True)
