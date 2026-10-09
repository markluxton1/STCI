#!/usr/bin/env python3
"""Verify all-direction primitive-fourth classification and quartic carriers.

Run with Python containing SymPy and Macaulay2's M2 on PATH.  All arithmetic
is over QQ.  No temporary-session files or numerical interpolation are used.
The two polynomial-arithmetic derivations and their regenerated inspectable
equations are in research/scratch/primitive47universal.
"""
from pathlib import Path
import importlib.util
import json
import shutil
import subprocess
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
SCRATCH=ROOT/'research'/'scratch'/'primitive47universal'

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    result=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result

def main():
    if not shutil.which('M2'):
        raise RuntimeError('Macaulay2 M2 is required for exact ideal-membership certificates')
    gen=module('universal_primitive_generator',SCRATCH/'generate.py')
    gen.main()
    carrier=module('universal_primitive_carrier',SCRATCH/'quartic_contact.py')
    carrier.main()
    data=json.loads((SCRATCH/'equations.json').read_text())
    contact=json.loads((SCRATCH/'quartic_contact.json').read_text())
    a0,a1,a2,b0,b1,b2=sp.symbols('a0 a1 a2 b0 b1 b2')
    variables=[a0,a1,a2,b0,b1,b2]
    D=sp.sympify(data['resultant'])
    G=[sp.sympify(c['numerator']) for c in data['coordinates']]
    assert all(c['denominator_power']==1 for c in data['coordinates'])
    assert all(sp.Poly(p,*variables).total_degree()==8 for p in G)
    zero_locus={b0:-2*a1,b1:-2*a2}
    assert all(sp.expand(p.subs(zero_locus))==0 for p in G)
    restricted=sp.expand(D.subs(zero_locus))
    assert restricted==sp.sympify(contact['resultant'])
    assert restricted==a0**2*b2**2+6*a0*a1*a2*b2+4*a0*a2**3-2*a1**3*b2
    assert restricted.subs({a0:0,b2:0})==0

    # Independent original rational-series implementation, on ordinary and
    # affine-degree-drop directions, including both carrier boundary charts.
    original=module('original_primitive_obstruction',ROOT/'research'/'scratch'/'primitive47'/'obstruction.py')
    z=original.z
    pairs=[(z**2,1),(z**2+1,z),(z**2+z+1,z**2-z+1),
           (z**2+z,z**2+1),(z**2,1+z),(z**2+1,-2*z),
           (z**2+z+1,z**2-2*z-2),(z**2+1,z**2-2*z),
           (1+z,z**2-2),(z+z**2,z**2-2*z-2)]
    for A,B in pairs:
        values={a0:A.coeff(z,0),a1:A.coeff(z,1),a2:A.coeff(z,2),
                b0:B.coeff(z,0) if hasattr(B,'coeff') else B,
                b1:B.coeff(z,1) if hasattr(B,'coeff') else 0,
                b2:B.coeff(z,2) if hasattr(B,'coeff') else 0}
        d=D.subs(values)
        assert d!=0
        actual=original.obstruction(A,B)[3]
        expected=[sp.cancel(p.subs(values)/d) for p in G]
        assert actual==expected,(A,B,actual,expected)
        vanishes=(values[b0]==-2*values[a1] and values[b1]==-2*values[a2])
        assert all(c==0 for c in actual)==vanishes

    M=sp.Matrix([[sp.sympify(p) for p in row] for row in contact['matrix2']])
    assert M.extract([0,1,2],[4,5,6]).det()==-a0**8
    assert M.extract([4,5,6],[0,1,6]).det()==-b2**8/256
    # Since D != 0 implies (a0,b2) != (0,0), these minors cover every
    # admissible direction.  Universal cubic restriction checks were made
    # in carrier.main(), not just at the ten samples above.
    for file in ['classify.m2','quartic_contact.m2']:
        completed=subprocess.run(['M2','--script',str(SCRATCH/file)],cwd=ROOT,
                                 capture_output=True,text=True,check=True)
        print(completed.stdout.strip())
        if completed.stderr: print(completed.stderr.strip())
    print('PRIMITIVE-FOURTH CLASSIFICATION AND ALL-CHART QUARTIC CARRIER THEOREM VERIFIED')

if __name__=='__main__':main()
