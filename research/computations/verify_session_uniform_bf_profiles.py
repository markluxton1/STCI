#!/usr/bin/env python3
"""Independent finite numerical check of the small e=2 BF profile reduction.

These are numerical defect profiles, not embedded existence certificates.
The proof of finite-flat CI controls is given in the accompanying note.
"""
from itertools import product
import json
from pathlib import Path


def profiles(b):
    s, top = b - 1, b - 7
    middle = s // 2
    found = []
    for prefix in product(range(top + 1), repeat=middle - 1):
        d = [0, 0] + list(prefix)
        # Fill from complementary Gorenstein pairing.
        d += [0] * (s + 1 - len(d))
        for i in range(middle + 1):
            d[s - i] = top - d[i]
        if s % 2 == 0 and 2 * d[middle] != top:
            continue
        if d[2] != 0 or d[3] != 1:
            continue
        if any(d[i] > d[i + 1] for i in range(s)):
            continue
        if any(d[i] + d[j] > d[i + j]
               for i in range(s + 1) for j in range(s + 1 - i)):
            continue
        assert all(d[i] + d[s - i] == top for i in range(s + 1))
        found.append(d)
    return found


def main():
    expected = {
        9: [[0,0,0,1,1,1,2,2,2]],
        10: [[0,0,0,1,1,2,2,3,3,3]],
        11: [[0,0,0,1,1,2,3,3,4,4,4],
             [0,0,0,1,2,2,2,3,4,4,4]],
    }
    found = {b: profiles(b) for b in expected}
    assert found == expected
    # The exact CI controls tx-y^r, x^h have d_i=floor(i/r), n=r*h.
    # The complement formula follows from s=r*h-1; check all individual
    # inequalities in the two controls, including the full top degree.
    controls = [(3,3),(2,6)]
    for r,h in controls:
        b = r*h
        d = [i//r for i in range(b)]
        assert d[-1] == b-7
        assert d[2] <= 1 and d[3] <= 2
        assert all(d[i]+d[b-1-i] == d[-1] for i in range(b))
        assert all(d[i]+d[j] <= d[i+j]
                   for i in range(b) for j in range(b-i))
    output = {"status":"exhaustive numerical profiles, no embedded existence assertion",
              "profiles":found,
              "local_CI_controls":[{"r":r,"h":h,"multiplicity":r*h,
                                    "defects":[i//r for i in range(r*h)]}
                                   for r,h in controls]}
    target = Path(__file__).resolve().parents[1] / 'scratch/session_uniform_bf_profiles.json'
    target.write_text(json.dumps(output,indent=2)+'\n')
    print('SMALL e=2 BF PROFILE REDUCTION VERIFIED: b=9,10,11')
    print('LOCAL CI NUMERICAL CONTROLS VERIFIED: b=9,12')


if __name__ == '__main__':
    main()
