# Two algebraic e=1 directions exclude d2=4 quartic ancestors for every defect section

Date: 2026-10-08. Fixed C0 in characteristic zero. Status:
**PROVED BY COMPLETE QUARTIC FIBRES AND A PARAMETER-COVERING RANK ARGUMENT;
accepted after independent and root review.** See the
[root acceptance record](2026-10-08-session-new-results-acceptance.md).
This treats exactly the two
directions `A=r*z,B=1,12r^2+4r+3=0` with d2=4. Other positive-D2
directions and Gorenstein quadruples outside these fibres remain open.

## 1. Genuine degree-four defects and their complete linear incidence

These directions have zero primitive quadratic obstruction and unique
primitive correction gamma0=0. For a defect section delta in H0(O(4)),
every degree-four corrected triple has relation

```text
delta*m+theta*y^2=0,
m=U-r*z*V, y=V.
```

The extra global correction theta is a constant because its bundle is
O(-4+d2)=O(0). If theta=0, it shares every zero of delta, violating
finite-flatness of a genuine defect-four triple. Every nonzero homogeneous
quartic has a projective zero, including an infinity zero when its affine
degree drops. Thus theta is nonzero, and simultaneous scaling of delta
and theta normalizes theta=1. Delta is an arbitrary nonzero homogeneous
quartic; its repeated roots and infinity roots are retained.

Write the actual quartic jet on the canonical double as
`F=h*m+E*y^2+...`. It contains this triple if and only if

```text
h=delta*E.
```

An ancestor needs two linearly independent quartics because its target
classes u and v are independent. The proof below shows that this exact
linear containment system has dimension at most one for every delta.
No STCI mate or BF d2 bound is involved.

## 2. The complete seven-dimensional double-quartic space

The independent source reconstructs all 35 ambient degree-four monomials
and imposes both the curve restriction and the first normal coefficient
along `U=r*z*y,V=y`. Its exact matrix has rank 28 over the quadratic
field; all identities are reduced modulo `12r^2+4r+3`, so both roots
are covered. The complete seven-dimensional quartic space has two
primitive members with `(h,E)=(1,0),(z^8,0)`, and five other members
with

```text
(h,E)=(a_i*z^(i+2), z^i), i=0,1,2,3,4,
a0=3r-1/2,
a1=6r+2,
a2=0,
a3=4r-5/3,
a4=(66r+13)/18.
```

Their seven explicit ambient forms and the full rank verification are
stored in the standalone checker and its JSON. The five a_i are pairwise
distinct at either root: every difference is a unit modulo the defining
quadratic.

For a general member write `E=sum(e_i*z^i,i=0..4)`. Its h is

```text
h=A+B*z^8+sum(a_i*e_i*z^(i+2),i=0..4).
```

The free A and B match the constant and eighth coefficients of delta*E
uniquely. Thus the full quartic containment space is canonically the
kernel of the seven-by-five matrix obtained from coefficients z^1
through z^7 of

```text
delta*E-sum(a_i*e_i*z^(i+2),i=0..4).
```

## 3. Exact minors cover every defect section

Write `delta=d0+d1*z+d2*z^2+d3*z^3+d4*z^4` in its finite chart.

If d0 is nonzero, the rows z^1 through z^4 and columns e1 through e4
have determinant d0^4. Therefore the matrix has rank at least four
and kernel dimension at most one. Equivalently those low coefficients
determine e1,e2,e3,e4 successively from e0.

If d4 is nonzero, the rows z^4 through z^7 and columns e0 through e3
have determinant d4^4. The same conclusion follows from the high
coefficients, including infinity behavior.

It remains to retain the entire boundary d0=d4=0. There the first five
rows have determinant d1^5, and the last five rows have determinant
d3^5. If either d1 or d3 is nonzero, the matrix has full rank five.

The final boundary is `delta=d2*z^2`. The middle five rows are the
diagonal matrix

```text
diag(d2-a0,d2-a1,d2-a2,d2-a3,d2-a4).
```

Since the a_i are pairwise distinct, at most one entry can vanish.
Its rank is at least four. This final case includes the defect section
with double zeros at both endpoints; it is not discarded as a repeated
or pole stratum.

These cases cover every delta, and prove kernel dimension at most one
uniformly. Hence every genuine defect-four triple in either algebraic
direction has at most one independent containing quartic, and cannot
support the two independent multiplier equations of a common quartic
ancestor.

## 4. Exact evidence and retained scope

Run

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
 research/computations/verify_session_localcoh_e1_d4_algebraic_2026_10_08.py
```

The checker independently reconstructs the complete ambient space,
checks all seven explicit forms and their h/E coefficients, checks
pairwise differences in the exact field, and verifies all four minor
identities and the last diagonal case. It uses no discovery JSON as a
proof input. Its companion JSON records the full matrix and source hash.

The principal obstruction-zero direction `A=1+z,B=-2-8z` still needs its
defect-four rank incidence. Its complete double-quartic map is saved in
`explore_session_localcoh_e1_d4_quartic_map_2026_10_08.json`. The unique
quadric direction is already excluded for every D2 by the separate
double-divisor/P-037 proof. Directions with nonzero primitive quadratic
obstruction are not covered by this note. No claim eliminating an entire
d2=4 Gorenstein stratum follows.
