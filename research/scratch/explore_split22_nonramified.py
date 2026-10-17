exec(open('research/scratch/explore_split4_nonramified.py').read().split('for name,ee,p,r,n in')[0])
t=s.symbols('t');n=9
A=(z-1)*(z-t);res=((z**3-1)*(z**3-t**3))**2
B=s.cancel(res/A);p=P-2*z;r=t+(P/2-1-t)*z
co=s.symbols('u0:10');u=sum(co[i]*z**i for i in range(10));v=s.expand(B+z*u/2)
eq=image_eq(p,r,u,v)+[s.Poly(v,z).nth(10)]
M,c=s.linear_eq_to_matrix(eq,co)
print('ranks',M.rank(),M.row_join(c).rank())
rr,pivs=M.row_join(c).rref();print(pivs)
for row in rr.tolist():
 if any(a!=0 for a in row):print([s.factor(a) for a in row])
print(s.linsolve((M,c),co))
