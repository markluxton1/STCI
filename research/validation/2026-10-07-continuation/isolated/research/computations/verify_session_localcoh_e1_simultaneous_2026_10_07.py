#!/usr/bin/env python3
"""Exact two-target equations for the primitive e=1 ancestor bridge.

The actual quartic pencils and global socle/normal-frame inputs are
independently proved in the companion notes.  This self-contained check
verifies the determinant, all target-remainder constraints, and both
conjugate algebraic degree cases.  It never sets a multiplier's nonzero
target image to zero in the quadruple.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
z, r = s.symbols('z r')
u0, u2, v0, v2 = s.symbols('u0 u2 v0 v2')
P = 4*z*z+2*z+1
h0 = P*z**3/16
h1 = P*(64*z**6+8*z**3+1)/1024
T0 = (2*z+1)*(1536*z**5+1152*z**4+448*z**3+48*z*z-24*z+4)
T1 = (2*z+1)*(1536*z**8+1152*z**7+448*z**6+240*z**5+120*z**4+
              60*z**3+30*z*z+15*z+8)
determinant = (2*z-1)**3*(2*z+1)*P/256
assert s.expand(h0*T1-h1*T0-determinant) == 0
f0, f1 = u0+u2*z*z, v0+v2*z*z
qtarget = (64*z**6+8*z**3+1)*f0-64*z**3*f1
remainder = s.Poly(s.rem(qtarget, (2*z-1)**3*(2*z+1), z), z)
target_matrix = s.linear_eq_to_matrix(remainder.all_coeffs(), [u0, u2, v0, v2])[0]
assert target_matrix.rank() == 3
expected_kernel = s.Matrix([-s.Rational(1, 4), 1, -s.Rational(3, 32), s.Rational(3, 8)])
assert target_matrix*expected_kernel == s.zeros(target_matrix.rows, 1)
assert len(target_matrix.nullspace()) == 1
assert s.expand(qtarget.subs(z, s.Rational(1, 2))-3*f0.subs(z, s.Rational(1, 2))+
                8*f1.subs(z, s.Rational(1, 2))) == 0
assert s.expand(qtarget.subs(z, -s.Rational(1, 2))-f0.subs(z, -s.Rational(1, 2))-
                8*f1.subs(z, -s.Rational(1, 2))) == 0
assert s.factor(qtarget.subs(dict(zip([u0, u2, v0, v2], expected_kernel))) /
                ((2*z-1)**3*(2*z+1))) == P**2/4

# No field-specialization inference: retain both roots of the exact
# quadratic, and explicitly verify the needed scalar units modulo it.
qr = 12*r*r+4*r+3
c, d = 2*r+s.Rational(2, 3), 8*r/9
cinverse, dinverse = s.invert(c, qr, r), s.invert(d, qr, r)
assert s.rem(c*cinverse-1, qr, r) == 0
assert s.rem(d*dinverse-1, qr, r) == 0
tau_vars = s.symbols('t0:5')
tau = sum(value*z**j for j, value in enumerate(tau_vars))
algebraic_equation = s.Poly(s.expand(c*z**8*f0-d*z**3*tau-f1), z)
assert s.expand(algebraic_equation.coeff_monomial(z**10)-c*u2) == 0
assert s.expand(algebraic_equation.coeff_monomial(z**8)-c*u0) == 0
reduced = algebraic_equation.as_expr().subs({u0: 0, u2: 0})
for j, value in enumerate(tau_vars):
    assert s.expand(s.expand(reduced).coeff(z, j+3)+d*value) == 0
assert s.expand(reduced).coeff(z, 2) == -v2
assert s.expand(reduced).coeff(z, 0) == -v0

record = {
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'scope': 'Characteristic-zero C0; common quartic ancestor; e=1,D2=0; two simultaneous target equations',
    'accepted_inputs': ['global socle isomorphism E3=omegaC(-3)=O(-14)',
                        'normalized target pencil (1,z^2) in E3(4)=O(2)',
                        'tau in H0(Hom(L^3,E3))=H0(O(4))',
                        'four complete primitive-e1 quartic fibres', 'P-037 degree2 ancestor exclusion'],
    'principal_determinant': str(determinant),
    'principal_target_matrix': [[str(value) for value in row] for row in target_matrix.tolist()],
    'principal_target_rank': 3,
    'principal_kernel': list(map(str, expected_kernel)),
    'principal_target_constraint': 'f0=c0*(z^2-1/4), f1=3*f0/8; rank1 and common zero',
    'algebraic_unit_inverse_c': str(cinverse),
    'algebraic_unit_inverse_d': str(dinverse),
    'algebraic_constraint': 'z10,z8 force f0=0; z3..z7 force tau=0; then f1=0 at both roots',
    'quadric_orbit': 'F=qF2,G=qG2 makes q*alpha a degree2 common ancestor, prohibited by P-037',
    'status': 'PASS: exact coefficient checks for corrected simultaneous argument; companion geometric inputs independently audited',
    'failed_shortcut': 'F*alpha=u does not imply F=0 in OZ; individual carrier cubic-pole bound was retracted',
    'open_scope': 'e=1,D2>0 and all other still-unexcluded quartic-ancestor strata'
}
(HERE/'session_localcoh_e1_simultaneous_2026_10_07.json').write_text(json.dumps(record, indent=2)+'\n')
print('PASS: principal actual-pencil determinant and full target remainder matrix; allowed target pair has rank1.')
print('PASS: both algebraic roots, scalar units and exact polynomial-degree equations; allowed target pair is zero.')
print('Scope: corrected simultaneous-two-target bridge; global frame and accepted quartic-fibre inputs are explicit.')
