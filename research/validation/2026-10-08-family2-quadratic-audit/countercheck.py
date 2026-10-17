#!/usr/bin/env python3
"""Separate exact implementation for the two family2 quadratic fibres.

This uses SymPy algebraic-number domains, never imports the producing
verifier, and never regenerates a coefficient certificate. It independently
rebuilds actual quartic forms and the balanced top map from stage numerators.
"""
from pathlib import Path
from itertools import permutations
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
HERE = ROOT / 'research/computations'
OUT = Path(__file__).resolve().parent
k, lam, t, x, y, z, w, a, q, b = s.symbols('k lam t x y z w a q b')
hashes = {}


def read(name):
    path = HERE / name
    data = path.read_bytes()
    hashes[str(path.relative_to(ROOT))] = hashlib.sha256(data).hexdigest()
    return data.decode()


def js(name):
    return json.loads(read(name))


lines = read('localcoh-incidence-bases.txt').splitlines()
assert lines[0] == 'ancestor stage4 numerators' and lines[31] == 'quartic multipliers'
H = [s.sympify(text.replace('^', '**'), locals=dict(zip('xyzw', (x,y,z,w))))
     for text in lines[1:31]]
W = [s.sympify(text.replace('^', '**'), locals=dict(zip('xyzw', (x,y,z,w))))
     for text in lines[32:]]
assert len(H) == 30 and len(W) == 18
quad = x*w-y*z
A, B, C = x*x*z-y**3, x*z*z-y*y*w, y*w*w-z**3
expected = [quad*m for m in (x*x,x*y,x*w,y*z,z*w,w*w)] + [gen*v for gen in (A,B,C) for v in (x,y,z,w)]
assert all(s.expand(u-v) == 0 for u,v in zip(W, expected))
assert all(s.Poly(f,x,y,z,w).total_degree() == 4 for f in W)
monomials = sorted({mon for f in W for mon in s.Poly(f,x,y,z,w).monoms()})
assert s.Matrix([[s.Poly(f,x,y,z,w).coeff_monomial(mon) for f in W] for mon in monomials]).rank() == 18
# All thirty-five degree-four monomials restrict to seventeen independent
# s,t monomials on C0; hence the ideal's degree-four piece is exactly 18.
degree_four = [(i,j,h,4-i-j-h) for i in range(5) for j in range(5-i) for h in range(5-i-j)]
restr = s.Matrix([[int(j+3*h+4*v == n) for i,j,h,v in degree_four] for n in range(17)])
assert len(degree_four) == 35 and restr.rank() == 17
assert all(s.expand(f.subs({x:1,y:t,z:t**3,w:t**4})) == 0 for f in W)

top = js('localcoh-symbol-top.json')
M = s.Matrix([[s.Rational(v) for v in row] for row in top['matrix']])
assert M.shape == (32,30) and M.rank() == 29
columns = []
for h in H:
    normal = s.Poly(s.expand(h.subs({x:1,y:t,z:t**3+a,w:t**4+t*a+q})),a,q)
    assert all(i+j >= 3 for i,j in normal.monoms())
    h3 = sum(coef*a**i*q**j for (i,j),coef in normal.terms() if i+j == 3)
    normal3 = s.expand(h3.subs(a,(b+t*t*q)/t**3))
    u, v = q/s.Integer(2)-b/(2*t*t), q/t+b/t**3
    columns.append([s.cancel(s.Poly(s.expand(normal3*u**i*v**(3-i)),q,b).coeff_monomial(q**3*b**3)/t**3) for i in range(4)])
rebuilt = s.Matrix([[s.expand(col[i]).coeff(t,j) for col in columns] for i in range(4) for j in range(8)])
assert rebuilt == M
assert [[str(s.expand(v)) for v in col] for col in columns] == top['columns']
print('PASS: actual 18 quartic forms span I(C0)_4; all30 top columns rebuilt from actual stage numerators.', flush=True)

seed = js('session-localcoh-origin-family-2-seed.json')
kernel = s.Matrix([s.Rational(v) for v in seed['kernel']])
assert len(seed['seed']) == len(kernel) == 30 and kernel != s.zeros(30,1)
assert M*kernel == s.zeros(32,1)
tensor_lines = read('localcoh-incidence-tensor.txt').splitlines()
assert tensor_lines[0] == '30 18 74 542'
T = [[s.Rational(0) for _ in range(542)] for _ in range(74)]
for text in tensor_lines[1:]:
    row,col,value = text.split()
    T[int(row)][int(col)] += s.Rational(value)
assert [row[540] for row in T] == [s.Rational(i == 72) for i in range(74)]
assert [row[541] for row in T] == [s.Rational(i == 73) for i in range(74)]

cases = {'qplus': (k*k+1,s.I), 'qminus': (k*k-2*k-1,1+s.sqrt(2))}
table = {}
for case,(modulus,root) in cases.items():
    domain = s.QQ.algebraic_field(root)
    zero, one = domain.zero, domain.one
    certificate = js('session_localcoh_family2_'+case+'_audit_2026_10_08.json')
    assert certificate['case'] == case and s.sympify(certificate['defining_polynomial'].replace('^','**')) == modulus
    assert s.discriminant(modulus,k) == certificate['discriminant']
    assert s.Poly(modulus,k).is_irreducible and s.gcd(modulus,s.diff(modulus,k)) == 1
    for name,digest in certificate['coordinate_sha256'].items():
        assert hashlib.sha256(read(name).encode()).hexdigest() == digest

    def reduce_source(expression):
        num,den = s.fraction(s.cancel(s.sympify(expression,locals={'k':k})))
        den = s.rem(den,modulus,k)
        assert den != 0 and s.gcd(den,modulus,k) == 1
        reduced = s.rem(s.rem(num,modulus,k)*s.invert(den,modulus,k),modulus,k)
        return domain.from_sympy(reduced.subs(k,root))

    def decode(terms):
        assert len({row[0] for row in terms}) == len(terms)
        assert all(type(row[0]) is int and row[0] >= 0 for row in terms)
        if not terms:
            return [zero]
        result = [zero]*(1+max(row[0] for row in terms))
        for degree,c0,c1 in terms:
            result[degree] = domain.from_sympy(s.Rational(c0)+s.Rational(c1)*root)
        while len(result)>1 and result[-1] == zero:
            result.pop()
        return result

    def coefficient(poly,n):
        return poly[n] if n<len(poly) else zero

    alpha = [decode(row) for row in certificate['alpha']]
    dual = [decode(row) for row in certificate['dual']]
    assert len(alpha) == 30 and len(dual) == 74 and dual[72] == [one]
    for value,text,slope in zip(alpha,seed['seed'],seed['kernel']):
        assert len(value)<=2 and coefficient(value,0) == reduce_source(text)
        assert coefficient(value,1) == domain.from_sympy(s.Rational(slope))
    p,r = ([decode(poly) for poly in certificate[name]] for name in ('direction_p','direction_r'))
    expected_direction = [['1',seed['family']['a1'],seed['family']['a2']], ['1',seed['family']['b1'],seed['family']['b2']]]
    for saved,source in zip((p,r),expected_direction):
        assert len(saved) == 3
        assert all(len(v)==1 and v[0] == reduce_source(text) for v,text in zip(saved,source))
    p,r = [v[0] for v in p], [v[0] for v in r]

    def convolution(first,second):
        answer = [zero]*(len(first)+len(second)-1)
        for i,c in enumerate(first):
            for j,d in enumerate(second):
                answer[i+j] += c*d
        return answer

    def power(value,n):
        answer = [one]
        for _ in range(n):
            answer = convolution(answer,value)
        return answer

    target = []
    for i in range(4):
        target += [zero]+convolution(power(p,i),power(r,3-i))
    assert len(target) == 32
    for row,value in zip(M.tolist(),target):
        for degree in (0,1):
            got = sum((domain.from_sympy(c)*coefficient(v,degree) for c,v in zip(row,alpha)),zero)
            assert got == (value if degree==0 else zero)

    sylvester = [[p[2],p[1],p[0],zero],[zero,p[2],p[1],p[0]], [r[2],r[1],r[0],zero],[zero,r[2],r[1],r[0]]]
    resultant = zero
    for perm in permutations(range(4)):
        term = one
        for i,j in enumerate(perm):
            term *= sylvester[i][j]
        resultant += (-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))*term
    assert resultant != zero and resultant == reduce_source(seed['family']['resultant'])
    assert s.gcd(modulus,(k*k-1)*(k*k+2*k+3)*(3*k**4-2*k**3-6*k*k-18*k-9),k) == 1

    # Directly match the raw Macaulay2 dual independently of the stored JSON.
    raw = read('session-localcoh-origin-family-2-exception-'+case+'-dual.txt').splitlines()
    assert len(raw) == 74
    for index,line in enumerate(raw):
        label,expression = line.split(maxsplit=1)
        assert int(label) == index
        polynomial = s.Poly(s.sympify(expression.replace('^','**').replace('lambda','lam'),locals={'k':k,'lam':lam}),lam)
        for n in range(max(polynomial.degree()+1,len(dual[index]))):
            assert reduce_source(str(polynomial.nth(n))) == coefficient(dual[index],n)

    # Every column is formed from all30 actual ancestor coordinates. Test
    # each coefficient through degree3: L has degree1, the dual degree2.
    assert max(map(len,dual)) == 3
    for col in range(18):
        totals = [zero]*4
        for row in range(74):
            if all(v == zero for v in dual[row]):
                continue
            matrix_entry = [sum((domain.from_sympy(T[row][18*i+col])*coefficient(alpha[i],n) for i in range(30)),zero) for n in range(2)]
            for n,value in enumerate(convolution(dual[row],matrix_entry)):
                totals[n] += value
        assert all(v == zero for v in totals), (case,col)
    table[case] = {'polynomial':str(modulus),'discriminant':certificate['discriminant'],
                   'both_geometric_roots_covered':True,'all_lambda_covered':True,
                   'dual_nonzero_entries':sum(any(c != zero for c in v) for v in dual),
                   'dual_lambda_degree':2,'target_value':'1',
                   'all18_columns_all_polynomial_coefficients_zero':True,
                   'all30_seed_and_slope_coefficients_match':True,
                   'all32_top_coefficients_match':True,
                   'homogeneous_resultant_nonzero':True,
                   'resultant_at_field_root':str(domain.to_sympy(resultant))}
    print('PASS '+case+': independent algebraic-number arithmetic, all18 polynomial identities, complete affine line.',flush=True)

remaining = [3*k**3+4*k*k+9*k-4,13*k**4+10*k**3+2*k*k-42*k-7,
243*k**15+810*k**14+2646*k**13+990*k**12-9465*k**11-54222*k**10-114414*k**9-166406*k**8-34359*k**7+301686*k**6+897946*k**5+1296458*k**4+1345117*k**3+811630*k*k+285598*k-610]
for i,f in enumerate(remaining):
    assert s.gcd(f,s.diff(f,k),k) == 1
    assert s.gcd(f,(k*k-1)*(k*k+2*k+3)*(3*k**4-2*k**3-6*k*k-18*k-9),k) == 1
    for _,(g,_) in cases.items():
        assert s.gcd(f,g,k) == 1
    for g in remaining[i+1:]:
        assert s.gcd(f,g,k) == 1
result = {'scope':'Characteristic zero; second rational h=t endpoint family; two quadratic factors only',
          'status':'PASS independent countercheck; 4 geometric roots excluded for every lambda',
          'actual_quartic_dimension':18,'actual_top_map_rebuilt':True,'top_rank':29,
          'remaining_exception_degrees':[3,4,15],'remaining_geometric_points':22,
          'remaining_full_lambda_fibres':'OPEN','fields':table,'input_sha256':hashes,
          'countercheck_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(OUT/'countercheck-result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
