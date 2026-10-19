"""Search for candidate integer configurations satisfying the normal carrier equality criteria.

Constraints from October 17 synthesis:
1. Carrier degree a >= 5.
2. Max index s = max r_P >= 5.
3. Degree bound: 4*a^2 - (7*s + 6)*a + 16*s <= 0.
4. Target Hodge equality: sum_P (A_P + D_{r_P, P}) / r_P == 7 - 16/a.
5. deg(A) = sum_P A_P = 4*a - 7.
6. A_P >= 0, D_{r_P, P} >= 0.
7. Parity: for each P, r_P * D_{r_P, P} is even.
8. Divisibility: with R = lcm(r_P), a must divide 16*R.
9. Symbolic triple torsion:
   sum_{r_P = 2} A_P + (1/2) * sum_{r_P >= 4} r_P * D_{r_P, P} >= 2.
"""

from fractions import Fraction
from math import gcd

def solve_configurations():
    candidates = []
    
    # Check s from 5 up to 30 (sufficient to cover all moderate degrees)
    for s in range(5, 31):
        # Determine valid a for this s:
        # 4a^2 - (7s+6)a + 16s <= 0
        disc = (7*s + 6)**2 - 256*s
        if disc < 0:
            continue
        sqrt_disc = disc**0.5
        a_min = int(((7*s + 6) - sqrt_disc) / 8) + 1
        a_max = int(((7*s + 6) + sqrt_disc) / 8)
        a_min = max(a_min, 5)
        
        for a in range(a_min, a_max + 1):
            if 4*a**2 - (7*s + 6)*a + 16*s > 0:
                continue
            
            target = Fraction(7*a - 16, a)
            deg_A = 4*a - 7
            
            # We want to know if there exists a multiset of indices {r_P} with max r_P = s,
            # and integers A_P >= 0 with sum A_P = deg_A,
            # and D_P >= 0 with r_P * D_P even,
            # such that:
            #   sum (A_P + D_P) / r_P == target,
            #   a divides 16 * lcm(r_P),
            #   and sum_{r=2} A_P + 1/2 sum_{r>=4} r * D_r >= 2.
            
            candidates.append((a, s, target, deg_A))
            
    print(f"Total (a, s) pairs satisfying quadratic degree bound: {len(candidates)}")
    return candidates

if __name__ == "__main__":
    cands = solve_configurations()
    for a, s, target, deg_A in cands[:25]:
        print(f"a={a}, s={s}, target={target} ({float(target):.4f}), deg_A={deg_A}")
