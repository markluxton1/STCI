"""Exact actual-coordinate conormal, ribbon-net, and derivative-map checks.

The companion proof note establishes the geometric antecedents and
completeness. This source contains no generated input or parameter search.
It checks identities over QQ and keeps the omitted middle coordinate fixed.
"""
from pathlib import Path
import hashlib,json,time
import sympy as s

started=time.monotonic();here=Path(__file__).resolve()
Y=s.symbols('Y0:5');Y0,Y1,Y2,Y3,Y4=Y
t,U,V,W,a,lam,u,v=s.symbols('t U V W a lam u v')
quadrics=[Y0*Y2-Y1**2,Y0*Y3-Y1*Y2,Y0*Y4-Y1*Y3,
          Y1*Y3-Y2**2,Y1*Y4-Y2*Y3,Y2*Y4-Y3**2]
names=['q01','q02','q03','q12','q13','q23']
monomials=[Y[i]*Y[j] for i in range(5) for j in range(i,5)]
restriction=[m.subs(dict(zip(Y,[1,t,t**2,t**3,t**4]))) for m in monomials]
assert len(monomials)==15
assert s.Matrix([[f.coeff(t,j) for f in restriction] for j in range(9)]).rank()==9
assert s.Matrix([[s.Poly(q,*Y).coeff_monomial(m) for q in quadrics] for m in monomials]).rank()==6
assert all(s.expand(q.subs(dict(zip(Y,[1,t,t**2,t**3,t**4]))))==0 for q in quadrics)

# Balanced affine conormal generators, and their opposite-chart transition.
coordinates=[1,t,t**2+U,t**3+2*t*U+V,t**4+3*t**2*U+2*t*V+W]
sub=dict(zip(Y,coordinates));zero={U:0,V:0,W:0}
first=s.Matrix([[s.diff(q.subs(sub),(n)).subs(zero) for q in quadrics] for n in (U,V,W)])
expected=s.Matrix([[1,t,t**2,0,0,0],[0,1,t,t,t**2,0],[0,0,1,0,t,t**2]])
assert first==expected
op_t=coordinates[3]/coordinates[4]
op_U=coordinates[2]/coordinates[4]-op_t**2
op_raw_V=coordinates[1]/coordinates[4]-op_t**3
op_raw_W=coordinates[0]/coordinates[4]-op_t**4
op_V=op_raw_V-2*op_t*op_U
op_W=op_raw_W-3*op_t**2*op_U-2*op_t*op_V
transition=s.Matrix([[s.cancel(s.diff(e,n).subs(zero)) for n in (U,V,W)]
                     for e in (op_U,op_V,op_W)])
reverse=s.Matrix([[0,0,1],[0,1,0],[1,0,0]])
assert transition==t**-6*reverse

# The complete degree-two ideal is symmetric 3-by-3 matrices.
c=s.symbols('c0:6')
matrix=s.Matrix([[c[0],c[1],c[2]],[c[1],c[2]+c[3],c[4]],[c[2],c[4],c[5]]])
assert first*s.Matrix(c)==matrix*s.Matrix([1,t,t**2])
def Q(M):
    coeff=[M[0,0],M[0,1],M[0,2],M[1,1]-M[0,2],M[1,2],M[2,2]]
    return s.expand(sum(co*q for co,q in zip(coeff,quadrics)))
assert s.expand(Q(matrix)-sum(co*q for co,q in zip(c,quadrics)))==0

# Actual PGL2 generators preserve the matrix interpretation by congruence.
translated=[sum(s.binomial(i,j)*a**(i-j)*Y[j] for j in range(i+1)) for i in range(5)]
B=s.Matrix([[1,0,0],[a,1,0],[a*a,2*a,1]])
assert s.expand(Q(matrix).subs(dict(zip(Y,translated)),simultaneous=True)-Q(B.T*matrix*B))==0
scaled=[lam**i*Y[i] for i in range(5)];scale=s.diag(1,lam,lam**2)
assert s.expand(Q(matrix).subs(dict(zip(Y,scaled)),simultaneous=True)-lam**2*Q(scale.T*matrix*scale))==0
assert s.expand(Q(matrix).subs(dict(zip(Y,reversed(Y))),simultaneous=True)-Q(reverse*matrix*reverse))==0

# Net eta=(1,u,v): the three symmetric matrices with fixed kernel eta.
eta=s.Matrix([1,u,v]);left=s.Matrix([u,-1,0]);right=s.Matrix([v,0,-1])
net=[left*left.T,left*right.T+right*left.T,right*right.T]
assert all(M*eta==s.zeros(3,1) for M in net)
assert s.Matrix([[M[i,j] for M in net] for i,j in [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]]).rank()==3
net_forms=[Q(M) for M in net]
derivatives=[s.expand(s.diff(q,Y2).subs(dict(zip(Y,[1,t,t**2,t**3,t**4])))) for q in net_forms]
expected_derivatives=[(u-t)*(u+2*t),(2*u+t)*(v-t*t),(v-t*t)**2]
assert all(s.expand(g-h)==0 for g,h in zip(derivatives,expected_derivatives))
center=[s.Poly(q,Y2).coeff_monomial(Y2**2) for q in net_forms]
assert center==[-1,-u,-v]

# Standard admissible net eta=(0,1,0): local complete intersection ribbon.
standard=[quadrics[0],quadrics[2]-quadrics[3],quadrics[5]]
eps=s.symbols('eps')
ribbon_chart=dict(zip(Y,[1,t,t**2,t**3+eps,t**4+2*t*eps]))
assert [s.expand(q.subs(ribbon_chart)) for q in standard]==[0,0,-eps**2]
assert [s.expand(q.subs(dict(zip(Y,[0,Y1,Y2,Y3,0])))) for q in standard]==[-Y1**2,Y2**2-2*Y1*Y3,-Y3**2]
standard_derivatives=[s.expand(s.diff(q,Y2).subs(dict(zip(Y,[1,t,t**2,t**3,t**4])))) for q in standard]
assert standard_derivatives==[1,2*t*t,t**4]
assert standard_derivatives[1]**2-4*standard_derivatives[0]*standard_derivatives[2]==0

# Singular intrinsic quotient eta=(1,0,0) has every gradient zero at t=0.
singular_net=[quadrics[3],quadrics[4],quadrics[5]]
assert all(all(s.diff(q,y).subs(dict(zip(Y,[1,0,0,0,0])))==0 for y in Y) for q in singular_net)

# Exact degree-map controls, including the extra basepoint conic.
g0,g1,g2=expected_derivatives
y=(t+2*u)/(v-t*t);x=(u-t)*(u+2*t)/(v-t*t)**2
deck=-(v+2*u*t)/(t+2*u)
assert s.cancel(y.subs(t,deck)-y)==0
deck_difference=-9*u*(t*t+4*t*u+v)*(u*t*t+v*t+u*v)/((t*t-v)**2*(4*u*u-v)**2)
assert s.cancel(x.subs(t,deck)-x-deck_difference)==0
assert s.factor(y.subs(v,4*u*u))==-1/(t-2*u)
assert s.expand((g0*g2+2*g1*g1).subs(u,0))==0
assert s.factor(s.gcd(s.gcd(g0.subs(v,u*u/4),g1.subs(v,u*u/4)),g2.subs(v,u*u/4)))==t+u/2

record={
 'status':'PASS exact conormal, complete ribbon-net, and derivative-map identities',
 'source_sha256':hashlib.sha256(here.read_bytes()).hexdigest(),
 'quadrics':dict(zip(names,map(str,quadrics))),
 'normal_frame':'Y0=1,Y1=t,Y2=t²+U,Y3=t³+2tU+V,Y4=t⁴+3t²U+2tV+W',
 'opposite_conormal_transition':'(U_infinity,V_infinity,W_infinity)=t^(−6)(W,V,U) modulo square ideal',
 'firstnormal_matrix':[[str(e) for e in row] for row in first.tolist()],
 'symmetric_matrix':[[str(e) for e in row] for row in matrix.tolist()],
 'ribbon_net':'M_Q eta=0; eta∈P²; intrinsic Veronese conic eta1²=eta0 eta2 excluded',
 'net_eta_1_u_v_forms':list(map(str,net_forms)),
 'derivative_eta_1_u_v_affine':list(map(str,expected_derivatives)),
 'center_functional_eta_1_u_v':center,
 'derivative_map_classification':{
    'double_conic':'eta1=0 or eta0=eta2=0, with intrinsic conic excluded',
    'birational_cubic_with_one_simple_basepoint':'eta1²=4eta0 eta2 and eta1!=0',
    'birational_quartic':'all other admissible eta',
    'chart_coverage':'eta0!=0 uses eta=(1,u,v); reversal handles eta2!=0; eta=(0,1,0) separately checked'},
 'deck_difference':str(deck_difference),
 'scope':'Identities support complete geometric ribbon classification in companion proof note. No all-mate exclusion or classification of admissible projection pencils is inferred from the derivative-map identities.',
 'elapsed_seconds':round(time.monotonic()-started,3)}
out=here.parents[1]/'scratch/session-rnc-ribbon-net-2026-10-09.json'
out.write_text(json.dumps(record,indent=2,default=str)+'\n')
print(json.dumps(record,indent=2,default=str),flush=True)
