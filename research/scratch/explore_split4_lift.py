exec(open('research/scratch/explore_split4_local.py').read().split('for name,a,p,r,deg in')[0])
xi,eta=s.symbols('xi eta')
mon2=[x0*x0,x0*x1,x0*x2,x0*x3,x1*x1,x1*x2,x1*x3,x2*x2,x2*x3,x3*x3]
cands=[q*q*m for m in mon2]+[q*h*x for h in [AA,BB,DD] for x in [x0,x1,x2,x3]]+[AA*AA,AA*BB,BB*BB,BB*DD,DD*DD]
def nor(F):
 ff=s.Poly(s.expand(F.subs({x0:1,x1:z,x2:z**3+eta,x3:z**4+xi+s.Rational(3,2)*z*eta})),xi,eta)
 return [s.Poly(ff.coeff_monomial(m),z).nth(i) for m in [xi*xi,xi*eta,eta*eta] for i in range(11)]
M=s.Matrix.hstack(*[s.Matrix(nor(F)) for F in cands]);cols=list(M.rref()[1]);MM=M[:,cols];rows=list(MM.T.rref()[1]);inv=MM[rows,:].inv();print('rank',len(cols),'rows',rows)
def lift(target):
 vec=s.Matrix(nor(target)) if not target.has(xi,eta) else s.Matrix([s.Poly(s.Poly(s.expand(target),xi,eta).coeff_monomial(m),z).nth(i) for m in [xi*xi,xi*eta,eta*eta] for i in range(11)])
 cc=inv*vec[rows,:];assert MM*cc==vec
 return sum(cc[j]*cands[cols[j]] for j in range(len(cols)))
