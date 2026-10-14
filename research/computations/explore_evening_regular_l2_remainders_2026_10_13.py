from pathlib import Path
import sympy as s
d,q,k,a=s.symbols('delta q kappa a')
locals_map={'delta':d,'q':q,'kappa':k,'a':a}
def read(label):
    return s.sympify(Path('/private/tmp/common_root_regular_'+label+'.txt').read_text().replace('^','**'),locals=locals_map)
L=read('L2')
f2,f3,f4=[read('f'+str(n)) for n in (2,3,4)]
domain=s.QQ.frac_field(d,q)
def remainder(expr):
    return s.Poly(expr,k,domain=s.QQ.frac_field(d,q,a)).rem(s.Poly(L,k,domain=s.QQ.frac_field(d,q,a))).as_expr()
A=s.diff(f2,a); C=f2.subs(a,0)
print('A modulo L2=',s.factor(remainder(A)),flush=True)
print('Res A,L2=',s.factor(s.resultant(A,L,k)),flush=True)
R3=s.Poly(f3,a).all_coeffs()
E3=s.expand(sum(v*(-C)**(len(R3)-1-i)*A**i for i,v in enumerate(R3)))
print('E3 numerator terms=',len(s.Poly(E3,d,q,k).terms()),flush=True)
rem3=s.factor(remainder(E3))
print('E3 reduced=',rem3,flush=True)
print('Res E3,L2=',s.factor(s.resultant(s.fraction(rem3)[0],L,k)),flush=True)
