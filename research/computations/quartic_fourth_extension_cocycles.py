"""Exact cocycle coefficients for the intrinsic quartic fourth-extension proof.

Run with Python and SymPy. Derives the chart transitions modulo y**4 from
the rational ambient coordinate changes; no ambient quartic source matrix,
parameter sampling, Groebner classification or output file is used.
See research/synthesis/intrinsic_fourth_extension.md for geometric meaning,
all parameter boundaries and the characteristic-zero theorem.
"""
import sympy as s

# Direct arithmetic in k(z, parameters)[y]/(y^4), independently of the
# candidate's w_i/u_i/v_i formulas.
z = s.symbols('z')
def add(a,b): return [a[i]+b[i] for i in range(4)]
def scale(a,c): return [c*x for x in a]
def mul(a,b): return [sum(a[j]*b[i-j] for j in range(i+1)) for i in range(4)]
def power(a,n):
    q=[s.Integer(1),0,0,0]
    for i in range(n): q=mul(q,a)
    return q
def inverse(a):
    q=[1/a[0],0,0,0]
    for i in range(1,4): q[i]=-sum(a[j]*q[i-j] for j in range(1,i+1))/a[0]
    return q
def charts(U,V):
    X3=add([z**4,0,0,0],add(U,scale(V,3*z/s.Integer(2))))
    X2=add([z**3,0,0,0],V)
    inv=inverse(X3)
    W=mul(X2,inv)
    ap=add(scale(inv,z),scale(power(W,3),-1))
    bp=add(inv,scale(power(W,4),-1))
    return W,scale(ap,s.Rational(1,2)),add(scale(mul(W,ap),-3),scale(bp,2))
def cf(x): return s.factor(s.cancel(x))

a,b=s.symbols('a b',nonzero=True)
delta=z*(b*z-2*a); gamma=3*b**4/s.Integer(8); gp=6*a**4
W,Up,Vp=charts([0,a,gamma/(b*delta),0],[0,b,0,0])
mp=add(scale(Up,b),scale(Vp,-a)); yp=scale(Vp,1/b)
dp=add(scale(W,b),scale(power(W,2),-2*a))
G=add(mul(dp,mp),scale(power(yp,2),-gp))
eta=cf(z**10*delta*G[3])
want=72*a**7/(b*z**8)+4*a**6/z**7-2*a**5*b/z**6-a**4*b**2/z**5-a**3*b**3/(2*z**4)-a**2*b**4/(4*z**3)-a*b**5/(8*z**2)+b**6/(16*z)
print('defect second coefficient:',cf(G[2]),flush=True)
print('defect contact class exact difference:',cf(eta-want),flush=True)
H=mul(yp,mp)
print('defect kernel transition:',cf(delta*H[3]/gp),flush=True)

a0,a1,b0,b1=s.symbols('a0 a1 b0 b1')
A=a0+a1*z; B=b0+b1*z; d=a0*b1-a1*b0
W,Up,Vp=charts([0,A,0,0],[0,B,0,0])
Ap=add([a1,0,0,0],scale(W,a0)); Bp=add([b1,0,0,0],scale(W,b0))
mp=add(mul(Bp,Up),scale(mul(Ap,Vp),-1))
h2=cf(z**8*mp[2])
want2=-(2*A+z*B)*(12*A*A+3*z*z*B*B+4*z*z*(a1*B-A*b1))/(8*z**5)
print('primitive second transition difference:',cf(h2-want2),flush=True)
he=s.expand(h2); cs={i:he.coeff(z,i) for i in range(-5,2)}
gamma=cs[0]+cs[1]*z
W,Up,Vp=charts([0,A,a1*gamma/d,0],[0,B,b1*gamma/d,0])
Ap=add([a1,0,0,0],scale(W,a0)); Bp=add([b1,0,0,0],scale(W,b0))
mp=add(mul(Bp,Up),scale(mul(Ap,Vp),-1))
yp=scale(add(scale(Up,-b0),scale(Vp,a0)),1/d)
gp=add([-cs[-4],0,0,0],scale(W,-cs[-5]))
G=add(mp,mul(gp,power(yp,2)))
print('primitive second residual check:',cf(z**8*G[2]-sum(cs[i]*z**i for i in (-1,-2,-3))),flush=True)
print('primitive kernel transition:',cf(power(yp,3)[3]),flush=True)
D=s.symbols('D')
eta_numerator=s.expand(z**8*D**3*G[3].subs(d,D))
K1=cf(eta_numerator.coeff(z,-1).subs(D,d)/d**2)
K9=cf(eta_numerator.coeff(z,-9).subs(D,d)/d**2)
K5=cf((eta_numerator.coeff(z,-5).subs(D,d)/d**2).subs({a0:0,b1:0}))
want1=b1**4*(8*a0*b1+72*a1*a1+118*a1*b0+63*b0*b0)/32
want9=a0**4*(4*a0*b1+126*a1*a1+59*a1*b0+9*b0*b0)
want5=-a1*b0*(2*a1+b0)*(40*a1**3+68*a1*a1*b0+30*a1*b0*b0+11*b0**3)/8
print('primitive K1 exact difference:',cf(K1-want1),flush=True)
print('primitive K9 exact difference:',cf(K9-want9),flush=True)
print('primitive K5 boundary exact difference:',cf(K5-want5),flush=True)

# Exact identities supporting the displayed mathematical proof.
assert cf(eta-want)==0
assert cf(delta*H[3]/(6*a**4)-z**-18)==0
assert cf(h2-want2)==0
assert cf(z**8*G[2]-sum(cs[i]*z**i for i in (-1,-2,-3)))==0
assert cf(power(yp,3)[3]-z**-18)==0
assert cf(K1-want1)==0 and cf(K9-want9)==0 and cf(K5-want5)==0
print("Defective extension class:", eta)
print("Primitive obstruction coefficients K1, K9, K5:", K1, K9, K5)
