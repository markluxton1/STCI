"""Exact integer partition solver for Hodge gap equality at low s.
"""

from fractions import Fraction
from math import gcd

def solve_for_pair(a, s):
    target = Fraction(7*a - 16, a)
    deg_A = 4*a - 7
    
    # We want to find N_1, ..., N_s >= 0 with sum N_r = deg_A
    # and M_1, ..., M_s >= 0 (with M_r even if r is odd)
    # such that sum_{r=1}^s (N_r + M_r) / r == target
    # and N_s + M_s > 0
    # and N_2 + 1/2 * sum_{r=4}^s r * M_r >= 2
    # and a divides 16 * lcm(present r).
    
    # Let C_r = N_r + M_r.
    # Note C_r >= 0.
    # sum C_r / r = target.
    # Also sum N_r = deg_A <= sum C_r.
    # Notice target = 7 - 16/a < 7.
    # Since sum C_r / r = target < 7, and C_r >= 0,
    # for each r, C_r / r <= target < 7, so C_r < 7 * r.
    
    # First find all tuples (C_1, ..., C_s) of non-negative integers such that:
    # sum_{r=1}^s C_r / r == target, C_s > 0, sum C_r >= deg_A.
    # Then check if a divides 16 * lcm(r for C_r > 0).
    # Then check if there exist N_r <= C_r with sum N_r = deg_A,
    # satisfying the parity and torsion conditions.
    
    solutions = []
    
    def search_C(r, current_sum, current_C):
        if r == 0:
            if current_sum == target:
                if current_C[s] > 0 and sum(current_C.values()) >= deg_A:
                    # Check divisibility
                    present_r = [k for k, v in current_C.items() if v > 0]
                    l = 1
                    for k in present_r:
                        l = (l * k) // gcd(l, k)
                    if (16 * l) % a == 0:
                        # Check if valid N_r and M_r exist
                        if check_NM(current_C):
                            solutions.append((dict(current_C), l))
            return

        # Bound on C_r:
        # current_sum + C_r / r <= target
        # Also even if all remaining C_1, ..., C_{r-1} are placed at r-1,
        # current_sum + C_r / r + (deg_A - sum(current_C) - C_r) / (r-1) ...
        max_Cr = int((target - current_sum) * r)
        for c in range(max_Cr, -1, -1):
            current_C[r] = c
            search_C(r - 1, current_sum + Fraction(c, r), current_C)
            del current_C[r]

    def check_NM(C):
        # We need N_r <= C_r with sum N_r = deg_A
        # M_r = C_r - N_r.
        # If r is odd, M_r must be even (or sum of even D_i).
        # And N_2 + 1/2 * sum_{r=4}^s r * M_r >= 2.
        
        # Check all possible N tuples:
        # Since s <= 7 and C_r are small, we can search N:
        def search_N(r, rem_deg, cur_N):
            if r == 0:
                if rem_deg == 0:
                    # Check parity and torsion
                    torsion = cur_N.get(2, 0)
                    for k in range(4, s + 1):
                        M_k = C[k] - cur_N.get(k, 0)
                        torsion += Fraction(k * M_k, 2)
                    if torsion >= 2:
                        return True
                return False
            
            # For this r:
            # If r is odd: M_r = C[r] - N_r must be even => N_r and C[r] have the same parity.
            start_N = C[r]
            step = 2 if (r % 2 == 1) else 1
            for n in range(min(C[r], rem_deg), -1, -1):
                if r % 2 == 1 and (C[r] - n) % 2 != 0:
                    continue
                cur_N[r] = n
                if search_N(r - 1, rem_deg - n, cur_N):
                    return True
                del cur_N[r]
            return False

        return search_N(s, deg_A, {})

    search_C(s, Fraction(0), {})
    return solutions

if __name__ == "__main__":
    for s in [5, 6]:
        for a in range(5, 12):
            if 4*a**2 - (7*s + 6)*a + 16*s <= 0:
                sols = solve_for_pair(a, s)
                print(f"s={s}, a={a}: {len(sols)} valid equality solutions")
                for sol, l in sols[:3]:
                    print(f"   C={sol}, lcm={l}")
