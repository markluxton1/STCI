#!/usr/bin/env python3
"""Exact supporting checks for the locally-Gorenstein conductor audit.

The theorem is the geometric proof in the companion audit note. This
source independently checks the complete generic Artin length partitions
and preserves countermodels to two invalid shortcuts. These examples are
algebras, not claimed global quartic conductor realizations.
"""
from pathlib import Path
from itertools import combinations_with_replacement
import hashlib,json
import sympy as s

# A factor is L[t]/t^a, [L:K]=r, with ord_t(epsilon)=k.
# Length4 and rank(epsilon)=2 are forced by rank2 freeness over
# K[epsilon]/epsilon². The rank contribution is r(a-k).
possibilities=[(a,r,k) for a in range(1,5) for r in range(1,5)
               for k in range(1,a+1) if a*r<=4 and 2*k>=a]
partitions=[]
for count in range(1,5):
    for factors in combinations_with_replacement(possibilities,count):
        if sum(a*r for a,r,k in factors)==4 and sum(r*(a-k) for a,r,k in factors)==2:
            partitions.append(factors)
expected=[((2,1,1),(2,1,1)),((2,2,1),),((4,1,2),)]
assert sorted(partitions)==expected
assert all(2*k==a for factors in partitions for a,r,k in factors)

# Nonzero discriminants on a thick base are compatible with nonreduced D.
# Example1: K[t]/t4 with epsilon=t², free over R with basis1,t.
epsilon_t4=s.Matrix([[s.Integer(i==j+2) for j in range(4)] for i in range(4)])
assert epsilon_t4.rank()==2 and epsilon_t4**2==s.zeros(4)
eta_t4=s.Matrix([[s.Integer(i==j+1) for j in range(4)] for i in range(4)])
assert eta_t4**2==epsilon_t4 and epsilon_t4!=s.zeros(4)
# Example2: R[eta]/(eta²-d), d=s transcendental and nonsquare in k(s).
# Basis1,eta,epsilon,epsilon*eta; Delta=d is a nonzero unit.
d=s.symbols('d',nonzero=True)
eta_unit=s.Matrix([[0,d,0,0],[1,0,0,0],[0,0,0,d],[0,0,1,0]])
epsilon_unit=s.Matrix([[0,0,0,0],[0,0,0,0],[1,0,0,0],[0,1,0,0]])
assert eta_unit**2==d*s.eye(4)
assert epsilon_unit.rank()==2 and epsilon_unit**2==s.zeros(4)
assert eta_unit*epsilon_unit==epsilon_unit*eta_unit

# A split rank2 algebra over a thick base can exchange its reduced primes.
# f=(1,zeta) has a descended cube but no descended square for a primitive
# third root. This disproves automatic square compression for exchanged
# primes, even though the base is Gorenstein and the algebra finite flat.
zeta=s.symbols('zeta');modulus=zeta*zeta+zeta+1
assert s.rem(zeta**3-1,modulus,zeta)==0
assert s.rem(zeta-1,modulus,zeta)!=0
assert s.rem(zeta**2-1,modulus,zeta)!=0

# Low-degree prime classes used in the geometric reduction.
# A multiple of a ruling fiber is not prime. F2 primes different from
# C_min have b>=2a, because their intersection with C_min is nonnegative.
F0_primes=[(a,b) for a in range(3) for b in range(3)
           if 0<2*a+b<=2 and (a!=0 or b==1)]
F2_primes=[(a,b) for a in range(3) for b in range(5)
           if 0<a+b<=2 and b>=2*a and (a!=0 or b==1)]
assert sorted(F0_primes)==[(0,1),(1,0)]
assert F2_primes==[(0,1)] # C_min=(1,0) is the separately retained prime.

record={
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'status':'PASS complete generic Artin partitions and exact shortcut countermodels',
 'scope':'Characteristic zero; conditional rank2 freeness over a doubled generic base. The global conductor theorem is proved separately in the mathematical audit.',
 'generic_length4_rank2_partitions':[[{'a':a,'residue_degree':r,'epsilon_order':k} for a,r,k in factors] for factors in partitions],
 'thick_base_discriminant_examples':['K[t]/t4, epsilon=t², Delta=epsilon!=0','K(sqrt(d))[epsilon]/epsilon², Delta=d a nonzero unit'],
 'exchanged_prime_countermodel':'B=R×R, R=K[epsilon]/epsilon²; sigma exchanges factors; f=(1,zeta), zeta primitive cube root; f³ descends, f² does not',
 'F0_low_degree_prime_classes':F0_primes,
 'F2_low_degree_prime_classes':[(1,0),*F2_primes],
 'not_claimed':'No automatic prime preservation; no Delta=0 assertion on nonreduced Gamma; no global realization of the countermodels; no nongorenstein extension'}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2),flush=True)
