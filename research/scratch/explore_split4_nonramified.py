import sympy as s
z,P=s.symbols('z P')

def image_eq(p,r,u,v):
 al=s.Poly(s.expand(p*u),z);be=s.Poly(s.expand(p*v+r*u),z);ga=s.Poly(s.expand(r*v),z)
 a=[al.nth(i) for i in range(11)];b=[be.nth(i) for i in range(11)];c=[ga.nth(i) for i in range(11)]
 return [-a[9]+2*b[10],-b[0]+2*c[1],a[0]-2*b[1]+4*c[2],-3*a[1]+2*b[2]+4*c[3],a[2]-2*b[3]+4*c[4],a[3]-2*b[4]+4*c[5],-a[4]+4*c[6],a[5]-2*b[6]+4*c[7],a[6]-2*b[7]+4*c[8],-a[7]-2*b[8]+12*c[9],a[8]-2*b[9]+4*c[10]]
for name,ee,p,r,n in [('d0',z-1,-2,-1,10),('d1double',(z-1)**2,P-2*z,1+(P/2-2)*z,9),('d1distinct',z*z+z+1,P-2*z,1+(P/2+1)*z,9)]:
 B=s.cancel((z**3-1)**4/ee);co=s.symbols('u0:'+str(n+1));u=sum(co[i]*z**i for i in range(n+1));v=s.expand(B+z*u/2)
 eq=image_eq(p,r,u,v)+[s.Poly(v,z).nth(n+1)]
 M,c=s.linear_eq_to_matrix(eq,co)
 print('\nCASE',name,'A',ee,'B',s.factor(B));print('ranks',M.rank(),M.row_join(c).rank())
 sol=s.linsolve((M,c),co);print('solution',sol)
 print('pivots and determinant factors')
 rr,pivs=M.row_join(c).rref();print(pivs)
 for row in rr.tolist():
  if any(a!=0 for a in row):print([s.factor(a) for a in row])
