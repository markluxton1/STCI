exec(open('research/scratch/explore_split4_nonramified.py').read().split('for name,ee,p,r,n in')[0])
x0,x1,x2,x3,e,n,X=s.symbols('x0 x1 x2 x3 e n X')
q=x0*x3-x1*x2;AA=x0*x0*x2-x1**3;BB=x0*x2*x2-x1*x1*x3;DD=x2**3-x1*x3*x3
T=AA-2*BB+DD
Tf=s.cancel(T.subs({x0:1,x1:z,x2:z**3+e,x3:z**4+e*(z+n)})/e)
t1=s.expand(Tf.subs(e,0));print('T1',s.factor(t1)); t10=t1.subs(n,0);t11=s.diff(t1,n)
for name,a,p,r,deg in [('d0',z-1,-2,-1,10),('double',(z-1)**2,P-2*z,1+(P/2-2)*z,9)]:
 B=s.cancel((z**3-1)**4/a);co=s.symbols('u0:'+str(deg+1));u=sum(co[i]*z**i for i in range(deg+1));v=s.expand(B+z*u/2);M,c=s.linear_eq_to_matrix(image_eq(p,r,u,v)+[s.Poly(v,z).nth(deg+1)],co);ss=list(s.linsolve((M,c),co))[0];u=s.expand(u.subs(dict(zip(co,ss))))
 JJ=s.expand(a*u+p*B-2*t10*t11);print(name,'J eval terms',s.Poly(JJ,z).terms());J=sum(s.Poly(JJ,z).nth(3*i+j)*X**i*z**j for i in range(4) for j in range(2));assert s.expand(J.subs(X,z**3)-JJ)==0
 print('Jz atselected',s.factor(s.diff(J,z).subs({X:1,z:1})));print('JX atselected',s.factor(s.diff(J,X).subs({X:1,z:1})))
