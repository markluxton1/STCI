from pathlib import Path
import json
import sympy as s
p,r,b,z,U,V,y,m=s.symbols('p r b z U V y m');x0,x1,x2,x3=s.symbols('x0 x1 x2 x3')
HERE=Path(__file__).parent;j=json.loads((HERE/'session-mf6-e1-principal-contact-2026-10-08.json').read_text());forms=list(map(s.sympify,j['I4']))
A,B=1+r*z,b+p*z;det=p-r*b;bs,bt=p/det,-r/det
h2=s.expand(-(2*A+z*B)*(12*A*A+3*z*z*B*B+4*z*z*(s.diff(A,z)*B-A*s.diff(B,z)))/(8*z**5));c1,c2,c3=[h2.coeff(z,-i) for i in (1,2,3)];H=s.expand(64*(c1*c3-c2*c2));delta=s.expand(-8*c2+8*c1*z);Gamma=sum(s.expand(delta*h2).coeff(z,i)*z**i for i in range(3))
chart={x0:1,x1:z,x2:z**3+V,x3:z**4+U+s.Rational(3,2)*z*V};jet=[s.expand(f.subs(chart).subs({U:bt*m+A*y,V:-bs*m+B*y})) for f in forms]
first=[s.expand(f.coeff(m,0).coeff(y,1)) for f in jet];second=[s.cancel(det*(delta*f.coeff(m,0).coeff(y,2)-Gamma*f.coeff(m,1).coeff(y,0))) for f in jet]
def rows(polys): return [[s.expand(f).coeff(z,i) for f in polys] for i in range(max(s.degree(f,z) if f else 0 for f in polys)+1)]
M1,M2=rows(first),rows(second)
weights=[]
for f in forms:
 ww=set(sum(i*w for i,w in zip(mm,(0,1,3,4))) for mm,cc in s.Poly(f,x0,x1,x2,x3).terms());assert len(ww)==1;weights.append(ww.pop())
row_weights=[1+i for i in range(len(M1))]+[10+i for i in range(len(M2))];column_weights=[w-3 for w in weights]
for ii,row in enumerate(M1+M2):
 for jj,entry in enumerate(row):
  assert all(2*aa+rr+bb==row_weights[ii]-column_weights[jj] for (aa,rr,bb),cc in s.Poly(entry,p,r,b).terms() if cc)
def m2expr(e):return str(e).replace('**','^')
code=['R=QQ[p,r,b,Degrees=>{2,1,1}];','H='+m2expr(H)+';','S=R/ideal(H);',
 'M=map(S^{'+','.join(str(w) for w in row_weights)+'},S^{'+','.join(str(w) for w in column_weights)+'},{'+','.join('{'+','.join(m2expr(e) for e in row)+'}' for row in M1+M2)+'});',
 'print("homogeneous",isHomogeneous M);','K=ker M;','G=mingens K;','print("kernel degrees", degrees source G);','print("kernel matrix",G);',
 'o=openOut "research/scratch/mf6-principal-weighted-kernel-2026-10-08.txt";','o << toString degrees source G << endl;', 'o << toString entries G << endl;','close o;']
(HERE/'derive-mf6-principal-weighted-kernel-2026-10-08.m2').write_text('\n'.join(code)+'\n')
(HERE/'derive-mf6-principal-weighted-kernel-2026-10-08.json').write_text(json.dumps({'H':str(H),'first':[[str(e) for e in row] for row in M1],'second':[[str(e) for e in row] for row in M2],'row_weights':row_weights,'column_weights':column_weights,'forms':j['I4']},indent=2)+'\n')
print('SAVED homogeneous weighted contact matrix',len(M1+M2),'x18',flush=True)
