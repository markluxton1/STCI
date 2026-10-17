#!/usr/bin/env python3
"""Exact geometry of the principal e1,d2=1 invariant direction curve.

Proves polynomial identities and finite structural tests. The genus-one
argument and weighted chart interpretation are in the companion note.
No complete quartic rank-drop or cubic-defect incidence is solved here.
"""
from pathlib import Path
import hashlib,json
import sympy as s
p,r,b,z,x,v,k=s.symbols('p r b z x v k')
H=(8*p**3-(64*r*r+128*r*b+16*b*b)*p*p
   +(96*r**4+512*r**3*b+592*r*r*b*b+128*r*b**3+6*b**4)*p
   -(576*r**6+960*r**5*b+880*r**4*b*b+544*r**3*b**3
     +220*r*r*b**4+60*r*b**5+9*b**6))
S6=(93*b**6+676*b**5*r+1996*b**4*r*r+3552*b**3*r**3
    +7984*b*b*r**4+10816*b*r**5+5952*r**6)
assert s.expand(s.discriminant(H,p)+1728*(2*r-b)**2*(2*r+b)**4*S6)==0
assert s.gcd(S6.subs(b,1),s.diff(S6.subs(b,1),r))==1
assert S6.subs({b:1,r:s.Rational(1,2)})!=0
assert S6.subs({b:1,r:-s.Rational(1,2)})!=0
Ha=H.subs(b,1)
sing=s.groebner([Ha,s.diff(Ha,p),s.diff(Ha,r)],p,r,order='lex',domain=s.QQ)
expected=[8*p+24*r**3+12*r*r-38*r-3,(2*r-1)*(2*r+1)**3]
assert all(sing.reduce(e)[1]==0 for e in expected)
eg=s.groebner(expected,p,r,order='lex',domain=s.QQ)
assert all(eg.reduce(e.as_expr())[1]==0 for e in sing.polys)
node=s.expand(Ha.subs({p:2+v,r:s.Rational(1,2)+x}))
quadratic=sum(c*x**pw[0]*v**pw[1] for pw,c in s.Poly(node,x,v).terms() if sum(pw)==2)
assert s.expand(quadratic+48*(v*v-8*x*v+28*x*x))==0
tacnode=s.expand(Ha.subs({p:-2+4*x+v,r:-s.Rational(1,2)+x}))
assert all(tacnode.subs(v,k*x*x).coeff(x,i)==0 for i in range(4))
assert s.expand(tacnode.subs(v,k*x*x).coeff(x,4)+16*(k*k-6*k+36))==0
assert s.discriminant(k*k-6*k+36,k)==-108
# Absolute irreducibility: any rational root of monic cubic over k(r)
# is polynomial in r, of degree<=2. All coefficient equations have ideal1.
a,c,d=s.symbols('a c d')
root_equations=s.Poly(Ha.subs(p,a*r*r+c*r+d),r).all_coeffs()
root_test=s.groebner(root_equations,a,c,d,order='lex',domain=s.QQ)
assert list(root_test)==[1]
infpoly=p**3-8*p*p+12*p-72
assert s.expand(H.subs({b:0,r:1})-8*infpoly)==0
assert s.discriminant(infpoly,p)==-160704

# Explicit genus-one function-field model after two tacnode blowups.
W,Y=s.symbols('W Y')
At=-W**3+8*W*W-12*W+72
Ct=2*(W*W-6*W+36)
quad=At*x*x-2*Ct*x+Ct
assert s.expand(Ha.subs({r:x-s.Rational(1,2),p:-2+4*x+W*x*x})+8*x**4*quad)==0
assert s.expand(Ct-At-W*W*(W-6))==0
E=Y*Y-2*(W-6)*(W*W-6*W+36)
assert s.expand((At*x-Ct)**2-W*W*2*(W-6)*(W*W-6*W+36)-At*quad)==0
inverse_x=(Ct+W*Y)/At
assert s.factor(At*quad.subs(x,inverse_x)-W*W*E)==0
XE,YE=s.symbols('XE YE')
weierstrass=YE*YE-XE**3-96*XE+448
assert s.expand(weierstrass.subs({XE:2*(W-4),YE:2*Y})-4*E)==0
assert s.discriminant(XE**3+96*XE-448,XE)!=0
j_invariant=s.Rational(1728)*4*96**3/(4*96**3+27*448**2)
assert j_invariant==s.Rational(2048,3)

# Principal direction representative A=1+r z,B=1+p z; unique defect.
A,B=1+r*z,1+p*z
h2=s.expand(-(2*A+z*B)*(12*A*A+3*z*z*B*B
             +4*z*z*(s.diff(A,z)*B-A*s.diff(B,z)))/(8*z**5))
cocycle=[s.factor(h2.coeff(z,-i)) for i in(1,2,3)]
assert s.expand(Ha-64*(cocycle[0]*cocycle[2]-cocycle[1]**2))==0
delta=s.expand(-8*cocycle[1]+8*cocycle[0]*z)
Gamma=s.Add(*[s.expand(delta*h2).coeff(z,i)*z**i for i in range(3)])
P=2*p+12*r*r+16*r+9
assert s.factor(s.resultant(delta,Gamma,z)-p**4*P**4/8)==0
# On pP!=0, delta and Gamma are coprime with no further flatness deletion.
Q=8*p+12*r*r+4*r+3
assert s.expand(delta-(2*r+1)*Q+p*P*z)==0
qinfty=12*r*r+20*r+11
assert s.rem(P.subs(p,2*r+1),qinfty,r)==0
assert s.rem(Q.subs(p,2*r+1),qinfty,r)==0
assert s.rem(Ha.subs(p,2*r+1),qinfty,r)==0
qzero=44*r*r+20*r+3
assert s.rem((2*p+36*r*r+16*r+3).subs(p,(2*r-3)/11),qzero,r)==0
assert s.rem(Q.subs(p,(2*r-3)/11),qzero,r)==0

record={'status':'PASS direction-curve structure and exact defect/flatness identities',
        'scope':'Fixed C0,char0,e1,d2=1 principal a0*b1!=0; b0=0 chart retained',
        'weighted_H':str(H),'discriminant_remaining_sextic':str(S6),
        'affine_singular_ideal':list(map(str,expected)),
        'singular_types':{'p2_rhalf':'ordinary node','pminus2_rminushalf':'ordinary tacnode'},
        'absolute_irreducibility_root_equations':list(map(str,root_equations)),
        'root_test_groebner':['1'],'normalization_genus':1,
        'weierstrass':'YE^2=XE^3+96*XE-448','j_invariant':str(j_invariant),
        'birational_coordinates':'x=r+1/2; W=(p+2-4x)/x^2; Y=(A(W)*x-C(W))/W',
        'birational_inverse':'x=(C(W)+W*Y)/A(W); r=x-1/2; p=-2+4x+W*x^2',
        'b0_zero_polynomial':str(infpoly),
        'quadratic_cocycle':list(map(str,cocycle)),'delta':str(delta),'Gamma':str(Gamma),
        'finite_flatness_resultant':'p^4*(2p+12r^2+16r+9)^4/8',
        'c1_chart_exceptions':'primitive(-2,-1/2) or p=2r+1,12r^2+20r+11=0',
        'c3_zero_defect_at_zero':'p=(2r-3)/11,44r^2+20r+3=0',
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'sympy':s.__version__}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print('PASS: absolute irreducibility, node/tacnode ideals, squarefree remaining degree6 discriminant')
print('PASS: three distinct b0=0 chart points and genus-one normalization data')
print('PASS: explicit birational Weierstrass model YE^2=XE^3+96XE-448, j=2048/3')
print('PASS: unique linear defect, exact Gamma splitting and nonzero flatness resultant on pP!=0')
print('OPEN: complete ambient quartic rank-drop and cubic residue incidence on the remaining curve')
