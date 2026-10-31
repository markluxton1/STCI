#!/usr/bin/env python3
"""Exact low-degree linear algebra for ARTIFACT-20260821-012.

Uses only Python's standard library.  It computes kernels of substitution
R=k[U0,...,U3] -> k[s,t] for the displayed binary quintics, and verifies that
each cubic in the resulting kernel vanishes on the indicated residual conic.
"""
from fractions import Fraction as Q
from itertools import product

U = [
 [17,-11,26,-29,9,-18],
 [40,-32,80,-80,40,-48],
 [47,-5,94,-27,47,-30],
 [95,-53,190,-131,103,-78],
]
def poly_trim(a):
    while a and not a[-1]: a.pop()
    return a
def poly_divrem(a,b):
    a=poly_trim(a[:]); b=poly_trim(b[:]); q=[Q(0)]*max(1,(len(a)-len(b)+1))
    while a and len(a)>=len(b):
      c=a[-1]/b[-1]; d=len(a)-len(b);q[d]=c
      for i in range(len(b)):a[d+i]-=c*b[i]
      poly_trim(a)
    return poly_trim(q),a
def poly_gcd(a,b):
    a=poly_trim(a[:]);b=poly_trim(b[:])
    while b:a,b=b,poly_divrem(a,b)[1]
    return [x/a[-1] for x in a] if a else []
g=[Q(x) for x in reversed(U[0])] # U_i(1,z), low-to-high coefficients
for u in U[1:]:g=poly_gcd(g,[Q(x) for x in reversed(u)])
print('gcd of four affine binary-coordinate polynomials:',g)

def add(a,b):
    z=a.copy()
    for m,c in b.items(): z[m]=z.get(m,Q(0))+c
    return {m:c for m,c in z.items() if c}
def mul(a,b):
    z={}
    for m,c in a.items():
      for n,d in b.items():
        k=tuple(m[i]+n[i] for i in range(len(m)))
        z[k]=z.get(k,Q(0))+c*d
    return {m:c for m,c in z.items() if c}
def power(a,n):
    z={tuple(0 for _ in next(iter(a))):Q(1)}
    for _ in range(n): z=mul(z,a)
    return z
def monoms(n,d):
    if n==1: return [(d,)]
    out=[]
    for i in range(d+1):
      for x in monoms(n-1,d-i): out.append((i,)+x)
    return out
def rref(A):
    A=[[Q(x) for x in r] for r in A]; piv=[]; i=0
    for j in range(len(A[0]) if A else 0):
      p=next((k for k in range(i,len(A)) if A[k][j]),None)
      if p is None: continue
      A[i],A[p]=A[p],A[i]; a=A[i][j]
      A[i]=[x/a for x in A[i]]
      for k in range(len(A)):
        if k!=i and A[k][j]:
          a=A[k][j]; A[k]=[A[k][l]-a*A[i][l] for l in range(len(A[0]))]
      piv.append(j); i+=1
      if i==len(A): break
    return A,piv
def null(A):
    R,p=rref(A); free=[j for j in range(len(A[0])) if j not in p]; ans=[]
    for j in free:
      v=[Q(0)]*len(A[0]); v[j]=1
      for i,k in enumerate(p): v[k]=-R[i][j]
      ans.append(v)
    return ans
def fmt(c):
    if c.denominator==1:return str(c.numerator)
    return f"{c.numerator}/{c.denominator}"
def equation(v,ms,names):
    den=1
    from math import gcd
    for c in v: den=den*c.denominator//gcd(den,c.denominator)
    w=[int(c*den) for c in v]; g=0
    for x in w:g=gcd(g,abs(x))
    w=[x//g for x in w]
    lead=next(x for x in w if x); w=[x if lead>0 else -x for x in w]
    terms=[]
    for c,m in zip(w,ms):
      if not c:continue
      fac=''.join(names[i]+(f'^{e}' if e>1 else '') for i,e in enumerate(m) if e)
      if not fac: fac='1'
      if abs(c)!=1 or fac=='1': fac=f'{abs(c)}*{fac}'
      terms.append(('-' if c<0 else '+',fac))
    s=''
    for i,(sg,term) in enumerate(terms):s+=('' if i==0 and sg=='+' else sg)+term
    return s

def image_matrix(d):
    ms=monoms(4,d); rows=[[Q(0) for _ in ms] for _ in range(5*d+1)]
    for j,m in enumerate(ms):
      f={(0,0):Q(1)}
      for i,e in enumerate(m):
        g={(5-k,k):Q(U[i][k]) for k in range(6)}
        f=mul(f,power(g,e))
      for (a,b),c in f.items():rows[b][j]=c
    return ms,rows

# Coordinate cubics in x,y,z, indexed by (x,y,z).
V=[
 {(2,1,0):17,(2,0,1):-18,(1,2,0):-7,(1,1,1):8},
 {(2,1,0):40,(2,0,1):-40,(1,2,0):-8,(1,0,2):8},
 {(2,1,0):47,(2,0,1):-30,(1,2,0):-25,(0,2,1):8},
 {(2,1,0):95,(2,0,1):-78,(1,2,0):-25,(0,1,2):8},
]
points=[(0,1,0),(0,0,1),(1,1,1),(1,2,3),(1,3,2)]
qms=monoms(3,2)
M=[[Q(x**m[0]*y**m[1]*z**m[2]) for m in qms] for x,y,z in points]
qv=null(M)[0]; q={m:c for m,c in zip(qms,qv) if c}
print('residual conic q =', equation(qv,qms,['x','y','z']))

# Find linear forms in U that vanish on q: sum a_i V_i = q*l.
cms=monoms(3,3); lms=monoms(3,1)
A=[]
for m in cms:
    row=[]
    for v in V:row.append(v.get(m,Q(0)))
    for lm in lms:row.append(-mul(q,{lm:Q(1)}).get(m,Q(0)))
    A.append(row)
ker=null(A)
print('line equations from q:')
for v in ker:
    print(' ',equation(v[:4],monoms(4,1),['U0','U1','U2','U3']))

for d in range(1,5):
    ms,A=image_matrix(d); R,p=rref(A); K=null(A)
    print(f'degree {d}: dim R_d={len(ms)}, rank={len(p)}, dim I_d={len(K)}')
    if d == 3:
      for v in K: print(' ',equation(v,ms,['U0','U1','U2','U3']))

# Whether degree four contains new minimal generators beyond R_1 I_3.
ms3,A3=image_matrix(3); K3=null(A3)
ms4,A4=image_matrix(4); index4={m:i for i,m in enumerate(ms4)}
products=[]
for v in K3:
  for j in range(4):
    w=[Q(0)]*len(ms4)
    for a,m in zip(v,ms3):
      n=list(m); n[j]+=1; w[index4[tuple(n)]]=a
    products.append(w)
print('rank of R_1*I_3 in degree 4 =',len(rref(list(map(list,zip(*products))))[1]))

# A degree-one rational inverse certificate: A(U)*t=B(U)*s.
lin=monoms(4,1)
rows=[[Q(0)]*8 for _ in range(7)]
for j,m in enumerate(lin):
  for k,c in enumerate(U[j]):
    rows[k+1][j] += c       # t*A(U)
    rows[k][4+j] -= c       # -s*B(U)
inv=null(rows)
print('linear inverse certificates A(U)*t=B(U)*s:',len(inv))
for v in inv:
  print(' ',equation(v[:4],lin,['U0','U1','U2','U3']), '*t =',
        equation(v[4:],lin,['U0','U1','U2','U3']), '*s')

# Polynomial composition of F(U(x,y,z)), reduced modulo q with leading xz.
def reduce_q(f):
    # q is normalized: solve xz = - other terms / coefficient.
    c=q.get((1,0,1)); assert c
    repl={m:-a/c for m,a in q.items() if m!=(1,0,1)}
    changed=True
    while changed:
      changed=False; out={}
      for (a,b,c0),coef in f.items():
        if a and c0:
          changed=True
          for (i,j,k),d in repl.items():
            m=(a-1+i,b+j,c0-1+k);out[m]=out.get(m,Q(0))+coef*d
        else:out[(a,b,c0)]=out.get((a,b,c0),Q(0))+coef
      f={m:c for m,c in out.items() if c}
    return f
ms,A=image_matrix(3); K=null(A)
print('cubic kernel restrictions to residual conic (zero means containment):')
for v in K:
  f={}
  for a,e in zip(v,ms):
    if not a:continue
    h={(0,0,0):Q(1)}
    for i,n in enumerate(e):h=mul(h,power(V[i],n))
    for m,c in h.items():f[m]=f.get(m,Q(0))+a*c
  print(' ', 'zero' if not reduce_q(f) else 'NONZERO')

# A bounded singular-member reconnaissance.  At a projective point P, a member
# of the four-dimensional cubic system is singular precisely when its four
# gradient vectors at P are linearly dependent (Euler makes the value equation
# redundant).  Search small rational points, then report the projective kernel
# in coefficient space.  This is a witness search only, not a discriminant
# factorization or a classification of all singular members.
def eval_monom(m, point):
    z=Q(1)
    for x,e in zip(point,m): z *= Q(x)**e
    return z
def grad_of(v, point):
    ans=[]
    for i in range(4):
        total=Q(0)
        for coeff,m in zip(v,ms):
            if m[i]:
                n=list(m); n[i]-=1
                total += coeff*m[i]*eval_monom(n,point)
        ans.append(total)
    return ans
def projective_integer(v):
    from math import gcd
    den=1
    for x in v: den=den*x.denominator//gcd(den,x.denominator)
    w=[int(x*den) for x in v]
    g=0
    for x in w:g=gcd(g,abs(x))
    w=[x//g for x in w]
    lead=next(x for x in w if x)
    return tuple(x if lead>0 else -x for x in w)
def is_normalized_point(p):
    j=next((i for i,x in enumerate(p) if x),None)
    return j is not None and p[j]==1
def same_projective_point(a,b):
    return all(Q(a[i])*Q(b[j]) == Q(a[j])*Q(b[i]) for i in range(4) for j in range(4))
def on_parametrized_quintic(p):
    # Away from G, the printed inverse certificate recovers t:s.  The witness
    # search below is outside G, so this is an exact membership test there.
    l1=5*p[3]+5*p[2]-3*p[0]
    l2=5*p[3]-3*p[1]
    if not (l1 or l2): return None
    s,t=l2,l1
    image=[]
    for u in U:
        image.append(sum(Q(c)*Q(s)**(5-i)*Q(t)**i for i,c in enumerate(u)))
    return same_projective_point(p,image)

seen=set(); witnesses=[]
for p in product(range(-3,4), repeat=4):
    if not is_normalized_point(p): continue
    grads=[[g[i] for g in [grad_of(v,p) for v in K]] for i in range(4)]
    ker=null(grads)
    if ker:
        w=projective_integer(ker[0])
        key=(p,w)
        if key not in seen:
            seen.add(key); witnesses.append(key)
print('small-coordinate singular-member witnesses:',len(witnesses))
for p,w in witnesses[:20]:
    print(' singular point',p,'on C =',on_parametrized_quintic(p),
          'has cubic-system coefficients',w)

# Local quadratic tests for the three off-base-locus witnesses retained in
# ARTIFACT-20260821-016.  On the affine chart in which P_j=1, nonzero
# determinant of the 3-by-3 Hessian after deleting j says that the singularity
# is an ordinary double point.  This is deliberately local: it neither proves
# that a whole cubic surface is normal nor classifies all members of the
# discriminant in this P3.
def hessian_of(v, point):
    ans=[]
    for i in range(4):
        row=[]
        for j in range(4):
            total=Q(0)
            for coeff,m in zip(v,ms):
                if i == j:
                    if m[i] < 2: continue
                    n=list(m); n[i]-=2
                    total += coeff*m[i]*(m[i]-1)*eval_monom(n,point)
                else:
                    if not m[i] or not m[j]: continue
                    n=list(m); n[i]-=1; n[j]-=1
                    total += coeff*m[i]*m[j]*eval_monom(n,point)
            row.append(total)
        ans.append(row)
    return ans
def det(A):
    _,piv=rref(A)
    if len(piv) < len(A): return Q(0)
    # rref loses the row-scaling factor, so use permutation expansion only in
    # this fixed 3-by-3 use case.
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
print('local Hessian tests for retained off-base witnesses:')
for p,w in [((0,1,0,-3),(301,2536,1890,-3045)),
            ((1,2,-1,1),(383,-988,-1170,525)),
            ((1,3,-1,-2),(155,-1504,-1410,1365))]:
    F=[sum(Q(c)*v[i] for c,v in zip(w,K)) for i in range(len(ms))]
    H=hessian_of(F,p)
    j=next(i for i,x in enumerate(p) if x)
    minor=[[H[a][b] for b in range(4) if b!=j] for a in range(4) if a!=j]
    print(' point',p,'chart coordinate',j,'quadratic Hessian determinant =',fmt(det(minor)))
