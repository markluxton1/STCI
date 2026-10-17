#!/usr/bin/env python3
"""Independent quick cross-artifact checks for first endpoint completeness.

Uses SymPy only as an independent polynomial/finite-field implementation.
Does not invoke the saved Q1/Q2/Q3/Q13 verifier bodies or regenerate inputs.
"""
from pathlib import Path
import hashlib,json
import sympy as s
from sympy.polys.galoistools import gf_monic,gf_pow_mod,gf_sub,gf_gcd
from sympy.polys.domains import ZZ
ROOT=Path(__file__).resolve().parents[3]
HERE=ROOT/'research/computations'
OUT=Path(__file__).resolve().parent
k,lam=s.symbols('k lam')
polys={
 'q1':3*k**4-9*k**3-19*k**2-43*k-4,
 'q2':k**2-4*k+5,
 'q3':13*k**4+26*k**3+34*k**2+6*k-7,
 'q13':729*k**13+1620*k**12+2889*k**11-11268*k**10-26574*k**9-39642*k**8+94014*k**7+272968*k**6+454897*k**5+62256*k**4-571463*k**3-1210068*k**2-966908*k-379834,
}
chart=k*k-1; qk=k*k+2*k+3; nonprim=9*k**4-21*k**3+5*k*k-31*k+134
seed=json.loads((HERE/'session-localcoh-origin-family-1-seed.json').read_text())
family=seed['family']; degree_table={}
assert len(seed['seed'])==len(seed['kernel'])==30
input_hashes={}
def record_input(path):
 input_hashes[str(path.relative_to(ROOT))]=hashlib.sha256(path.read_bytes()).hexdigest()
record_input(HERE/'session-localcoh-origin-family-1-seed.json')
for label,f in polys.items():
 cert=HERE/f'session_localcoh_{label}_dual_audit_2026_10_07.json';d=json.loads(cert.read_text());n=s.degree(f,k)
 record_input(cert)
 assert len(d['alpha'])==30
 for name,expected_hash in d['coordinate_sha256'].items():
  assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==expected_hash
  record_input(HERE/name)
 def reduce_field(expr):
  num,den=s.fraction(s.cancel(expr));den=s.rem(den,f,k);assert den!=0
  return s.rem(s.rem(num,f,k)*s.invert(den,f,k),f,k)
 def stored_element(cs):return sum(s.Rational(v)*k**j for j,v in enumerate(cs))
 for coordinate,expr,slope in zip(d['alpha'],seed['seed'],seed['kernel']):
  assert len({row[0] for row in coordinate})==len(coordinate)
  assert all(len(row)==int(n)+1 for row in coordinate)
  saved={int(row[0]):stored_element(row[1:]) for row in coordinate}
  assert saved.get(0,s.Integer(0))==s.expand(reduce_field(s.sympify(expr,locals={'k':k})))
  assert saved.get(1,s.Integer(0))==s.Rational(slope)
  assert set(saved).issubset({0,1})
 for key,expressions in [('direction_p',['1',family['a1'],family['a2']]),('direction_r',['1',family['b1'],family['b2']])]:
  assert len(d[key])==3
  for cs,expr in zip(d[key],expressions):
   assert s.expand(stored_element(cs)-reduce_field(s.sympify(expr,locals={'k':k})))==0
 assert s.gcd(f,chart*qk*nonprim)==1
 assert s.gcd(f,s.diff(f,k))==1
 degree_table[label]={'degree':int(n),'seed_all30_coefficients_match_rational_source':True,'direction_all6_coefficients_match_first_family':True,'squarefree':True,'coprime_to_chart_and_primitive_exclusions':True,'certificate_sha256':hashlib.sha256(cert.read_bytes()).hexdigest()}
 if label!='q2':
  p={'q1':23,'q3':17,'q13':53}[label]; coeff=[int(v)%p for v in s.Poly(f,k).all_coeffs()];assert coeff[0]
  _,monic=gf_monic(coeff,p,ZZ)
  final=gf_sub(gf_pow_mod([1,0],p**int(n),monic,p,ZZ),[1,0],p,ZZ)
  assert final==[]
  frobenius_gcd=gf_gcd(monic,gf_sub(gf_pow_mod([1,0],p**(int(n)//int(next(iter(s.factorint(n))))),monic,p,ZZ),[1,0],p,ZZ),p,ZZ)
  assert len(frobenius_gcd)==1
  degree_table[label]['finite_prime']=p;degree_table[label]['monic_reduction_ascending']=list(reversed(monic));degree_table[label]['independent_Rabin_conditions_pass']=True
 else:assert s.discriminant(f,k)==-4
for i,(name,f) in enumerate(polys.items()):
 for other,g in list(polys.items())[i+1:]:assert s.gcd(f,g)==1
D=json.loads((HERE/'session-localcoh-origin-family-1-polynomial-dual.json').read_text())
record_input(HERE/'session-localcoh-origin-family-1-polynomial-dual.json')
for name,expected_hash in D['coordinate_sha256'].items():
 assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==expected_hash
 record_input(HERE/name)
partition={'chart_k_minus_1':k-1,'chart_k_plus_1':k+1,'nonprimitive_qk':qk,'nonprimitive_quartic':nonprim,**polys}
for i,(name,f) in enumerate(partition.items()):
 assert s.gcd(f,s.diff(f,k))==1
 for other,g in list(partition.items())[i+1:]:assert s.gcd(f,g)==1
def expr(terms):return sum(s.Rational(v)*k**i*lam**j for i,j,v in terms)
expected=89514547200*(k-1)**14*(k+1)**11*polys['q2']**5*qk**8*nonprim*polys['q1']*polys['q3']*polys['q13']
assert s.Poly(expr(D['dual_on_u'])-expected,k,lam).is_zero
assert s.degree(expected,k)==76 and not expr(D['dual_on_u']).has(lam)
clear=120*(k-1)**9*(k+1)**9
assert s.Poly(expr(D['ancestor_denominator'])-clear,k,lam).is_zero
for alpha,a,ker in zip(D['alpha'],seed['seed'],seed['kernel']):
 assert s.cancel(expr(alpha)-clear*(s.sympify(a,locals={'k':k})+lam*s.Rational(ker)))==0
result={'scope':'Independent factor partition, Rabin finite reductions, exact seed/direction cross-artifact audit; not full tensor replay','generic_target_degree':76,'generic_target_independent_of_lambda':True,'generic_cleared_ancestor_nonzero_on_chart':True,'exceptional_factor_degrees':{name:int(s.degree(f,k)) for name,f in polys.items()},'all_exceptional_factors_pairwise_coprime':True,'all_exceptional_geometric_points':23,'all_distinct_denominator_factors_squarefree_and_pairwise_coprime':True,'generic_factor_partition':{name:str(s.expand(f)) for name,f in partition.items()},'generic_factor_multiplicities':{'chart_k_minus_1':14,'chart_k_plus_1':11,'nonprimitive_qk':8,'nonprimitive_quartic':1,'q1':1,'q2':5,'q3':1,'q13':1},'input_sha256':input_hashes,'checker_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'fields':degree_table}
(OUT/'countercheck-result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)
