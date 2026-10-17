"""New specialization of accepted conductor octic; exact rational arithmetic."""
import ast
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "research/validation/2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/primitive-polynomial.txt"

def add(a, b, scale=1):
    c = dict(a)
    for m, x in b.items():
        c[m] = c.get(m, Q(0)) + scale*x
        if c[m] == 0:
            del c[m]
    return c

def mul(a, b):
    c = {}
    for (ja, pa), x in a.items():
        for (jb, pb), y in b.items():
            m = ja+jb, pa+pb
            c[m] = c.get(m, Q(0)) + x*y
    return {m:x for m,x in c.items() if x}

def const(x): return {(0,0):Q(x)} if x else {}

def power(a, n):
    c = const(1)
    for _ in range(n): c = mul(c, a)
    return c

def evaluate(node, subs):
    if isinstance(node, ast.Constant) and type(node.value) is int: return const(node.value)
    if isinstance(node, ast.Name): return subs[node.id]
    if isinstance(node, ast.UnaryOp):
        a = evaluate(node.operand, subs)
        return a if isinstance(node.op, ast.UAdd) else {m:-x for m,x in a.items()}
    if isinstance(node, ast.BinOp):
        a = evaluate(node.left, subs)
        if isinstance(node.op, ast.Pow): return power(a, node.right.value)
        b = evaluate(node.right, subs)
        if isinstance(node.op, ast.Add): return add(a,b)
        if isinstance(node.op, ast.Sub): return add(a,b,-1)
        if isinstance(node.op, ast.Mult): return mul(a,b)
    raise ValueError(ast.dump(node))

def divide_p_monic(a,b):
    degree = max(m[1] for m in b)
    assert {m:x for m,x in b.items() if m[1] == degree} == {(0,degree):Q(1)}
    r, quotient = dict(a), {}
    while r and max(m[1] for m in r) >= degree:
        n = max(m[1] for m in r)
        lead = {(j,n-degree):x for (j,p),x in r.items() if p == n}
        quotient = add(quotient,lead)
        r = add(r,mul(lead,b),-1)
    return quotient,r

def display(a):
    return " + ".join(f"({x})j^{j}p^{p}" for (j,p),x in sorted(a.items(), key=lambda item:(item[0][1],item[0][0]))) or "0"

j,p = {(1,0):Q(1)}, {(0,1):Q(1)}
assert hashlib.sha256(INPUT.read_bytes()).hexdigest() == "d5701314fdf45a60b66d4763159ac383a7fed5eb51d9821115455ab968e0ea84"
tree = ast.parse(INPUT.read_text().replace("^","**"),mode="eval").body
zero_p = dict(delta=const(-1),a={},B=const(Q(-2,3)),G={},J=j,p=p)
zero_j = dict(delta=const(1),a=add(const(Q(1,3)),j,-1),B=add(j,const(Q(-1,3))),G={m:-2*x for m,x in j.items()},J=j,p=p)
S = add(add(power(p,3),{m:-6*x for m,x in power(p,2).items()}),add({m:6*x for m,x in p.items()},{m:3*x for m,x in j.items()}))

FP = evaluate(tree,zero_p)
FJ = evaluate(tree,zero_j)
quotient,remainder = divide_p_monic(FP,S)
assert remainder == {}
Q5 = {m: Q(9,2)*x for m,x in quotient.items()}
support_quotient,support_remainder = divide_p_monic(power(S,5),Q5)

def uj_trim(a):
    while a and a[-1] == 0: a.pop()
    return a

def uj_add(a,b,scale=1):
    c = [Q(0)]*max(len(a),len(b))
    for i,x in enumerate(a): c[i] += x
    for i,x in enumerate(b): c[i] += scale*x
    return uj_trim(c)

def uj_mul(a,b):
    if not a or not b: return []
    c = [Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for k,y in enumerate(b): c[i+k] += x*y
    return uj_trim(c)

def uj_div(a,b):
    r = list(a)
    c = [Q(0)]*max(0,len(a)-len(b)+1)
    while r and len(r) >= len(b):
        degree = len(r)-len(b)
        coefficient = r[-1]/b[-1]
        c[degree] += coefficient
        r = uj_add(r,[Q(0)]*degree+[coefficient*x for x in b],-1)
    return uj_trim(c),r

def uj_xgcd(a,b):
    r0,r1 = a,b
    s0,s1 = [Q(1)],[]
    t0,t1 = [],[Q(1)]
    while r1:
        q,r = uj_div(r0,r1)
        r0,r1 = r1,r
        s0,s1 = s1,uj_add(s0,uj_mul(q,s1),-1)
        t0,t1 = t1,uj_add(t0,uj_mul(q,t1),-1)
    if not r0: return [],[],[]
    scale = 1/r0[-1]
    return ([scale*x for x in r0],[scale*x for x in s0],[scale*x for x in t0])

coefficients = []
for degree in range(5):
    c = {j:x for (j,p),x in support_remainder.items() if p == degree}
    coefficients.append(uj_trim([c.get(j,Q(0)) for j in range(max(c,default=-1)+1)]))
g = []
bezout = [[] for _ in coefficients]
for i,c in enumerate(coefficients):
    g_new,u,v = uj_xgcd(g,c)
    bezout = [uj_mul(u,b) for b in bezout]
    bezout[i] = uj_add(bezout[i],v)
    g = g_new
check = []
for c,b in zip(coefficients,bezout): check = uj_add(check,uj_mul(c,b))
assert check == g
assert g == [Q(1)]
assert all(not b for b in bezout[2:])
assert add(mul(Q5,support_quotient),support_remainder) == power(S,5)

# Homogeneous coordinate swap: p_new=p_old/(p_old-1), j_new=-j_old.
transformed = {}
for (jj,pp),x in FP.items():
    monomial = mul({(jj,pp):(-1)**jj*x},power(add(p,const(-1)),8-pp))
    transformed = add(transformed,monomial)
assert transformed == FJ
SJ = {}
for (jj,pp),x in S.items():
    monomial = mul({(jj,pp):Q(-2,3)*(-1)**jj*x},power(add(p,const(-1)),3-pp))
    SJ = add(SJ,monomial)
literal_PtJ = add(add({(1,0):Q(-2)},mul(add({(1,0):Q(6)},const(-4)),p)),add(mul(add(const(4),{(1,0):Q(-6)}),power(p,2)),mul(add({(1,0):Q(2)},const(Q(-2,3))),power(p,3))))
assert SJ == literal_PtJ


OUT = ROOT / "research/validation/2026-10-13-h3-zero-chart-conductor-new"
OUT.mkdir(exist_ok=True)
def encode(poly): return [{"j":m[0],"p":m[1],"coefficient":str(x)} for m,x in sorted(poly.items())]
record = {
    "input":str(INPUT.relative_to(ROOT)),
    "input_sha256":hashlib.sha256(INPUT.read_bytes()).hexdigest(),
    "zero_P_F":encode(FP),"zero_J_F":encode(FJ),"S":encode(S),"Q5_monic":encode(Q5),
    "S5_division_quotient":encode(support_quotient),"S5_division_remainder":encode(support_remainder),
    "remainder_coefficients_ascending_j":[[str(x) for x in c] for c in coefficients],
    "bezout_coefficients_ascending_j":[[str(x) for x in b] for b in bezout],
    "bezout_gcd_ascending_j":[str(x) for x in g],
    "octics_binary_transform":"FJ(P,Q,j)=FP(P,P-Q,-j)",
    "conormal_binary_transform":"PtJ(P,Q,j)=(-2/3)*S(P,P-Q,-j)",
}
(OUT/"new-exact-support-incidence.json").write_text(json.dumps(record,indent=2)+"\n")

print(json.dumps({"status":"PASS", "new_mathematical_conditions":5, "conditions":["zero-P exact cubic-quintic factorization", "support polynomial exact division", "first-two remainder coefficient Bezout product equals one", "zero-J homogeneous octic coordinate identity", "zero-J homogeneous conormal coordinate identity"], "remainder_degrees":[len(c)-1 for c in coefficients], "bezout_degrees":[len(c)-1 for c in bezout], "scope":"Both zero conormal cubic charts have no admissible projection satisfying SUP, conditional on the accepted actual conductor-support bridge; new proof pending independent audit"},indent=2))
