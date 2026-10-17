#!/usr/bin/env python3
# Exact dx=1 rank-12 quartic-incidence reduction.
exec(open("research/computations/verify_e2_quartic_incidence.py").read().split("# P-045:")[0])

u=sp.symbols("u")
pc=list(pivot_cols)
fr=[j for j in range(18) if j not in pc]
pr=list(pivot_rows)
Q=M1.extract(pr,fr)
M2p=M2[:,pc]
M2f=M2[:,fr]

# Fraction-free Schur complement; vanishing is equivalent to quartic incidence
# on D(det P).
detP=sp.factor(P.det())
T=detP*M2f-M2p*P.adjugate()*Q

sub={d:1/x,a:b*x-u}
Ts=[]
for e in T:
    q=sp.cancel(e.subs(sub))
    num,den=sp.fraction(q)
    Ts.append(sp.factor(num))
print("entries",len(Ts))
g=Ts[0]
for q in Ts[1:]:
    g=sp.factor(sp.gcd(g,q))
print("global entry gcd =",g)
print("sample factorizations")
for q in Ts[:12]:
    print(sp.factor(q))
