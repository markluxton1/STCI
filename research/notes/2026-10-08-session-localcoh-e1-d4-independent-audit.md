# Independent audit of the algebraic e1,d2=4 quartic exclusion

Date: 2026-10-08. Fixed C0, characteristic zero. Scope: exactly
`A=r*z,B=1,12r^2+4r+3=0`, genuine degree-four second defect. The audited
claim is in
[`2026-10-08-session-localcoh-e1-d4-algebraic.md`](2026-10-08-session-localcoh-e1-d4-algebraic.md).

**ACCEPTED:** every genuine triple in either algebraic direction has a
complete space of containing ambient quartics of dimension at most one.
It therefore cannot be the canonical triple of a quartic common ancestor
with independent target classes u and v. This is uniform over every
defect section, including repeated roots and roots at infinity. It does
not eliminate the other directions or an entire Gorenstein stratum.

## Genuine triples and normalization

The previously audited defective-triple presentation is
`J=(delta*m+theta*y^2,m*y,m^2,y^3)`, up to the harmless sign convention
for the correction. For these obstruction-zero directions the primitive
correction is zero. The possible additional correction is a section of
`O(-4+d2)=O(0)`, so theta is a scalar.

The theta-zero branch is excluded by finite-flatness, rather than being
discarded to make the rank argument work. Near a zero of the nonzero
defect section, take a support DVR R. If theta is zero, the quotient has
R-module presentation

```text
R*1 + R*y + R*y^2 + (R/(delta))*m.
```

The last summand is nonzero torsion, inconsistent with finite-flatness
over R. Every nonzero homogeneous section of `O(4)` has a projective
zero over the algebraically closed field. This includes an infinity
zero when its finite polynomial has degree below four. Thus theta must
be nonzero. Dividing the relation by theta normalizes theta to one and
replaces delta by delta/theta, preserving the same triple and its defect
divisor. This retains every nonzero five-coefficient quartic delta; no
root separation or finite-support assumption is used.

With theta one, the quotient has free basis `1,y,m` and relation
`y^2=-delta*m`. Therefore an actual quartic jet
`F=h*m+E*y^2+...` vanishes on the triple exactly when `h=delta*E`.
The omitted terms lie in `(m*y,m^2,y^3)`. This also proves the containment
criterion at zeros of delta, rather than merely away from them.

## Complete ambient quartic space

The source enumerates all exponent quadruples of sum four: there are
`binomial(7,3)=35`, each occurring once. It substitutes the actual
finite-chart normal parameters and imposes the constant and first
normal coefficients of the canonical double. The resulting `31x35`
matrix has rank 28 over `QQ(sqrt(-2))`.

The defining polynomial has discriminant `-128` and is irreducible over
QQ. The chosen root is `(-1+2*sqrt(-2))/6`. Every entry is rational in
r; conjugation preserves rank, so the second root is also covered.
The source verifies seven independent homogeneous quartic forms in the
kernel. Rank-nullity shows that these span the complete ambient space,
rather than a selected pencil. Checking the dense finite chart suffices
for the global double conditions: the primitive double is finite-flat
over C0, so its structure sheaf has no support torsion at infinity.
The forms themselves are homogeneous global forms.

The normalized basis consists of two forms with `(h,E)=(1,0),(z^8,0)`
and five forms with

```text
(h,E)=(a_i*z^(i+2),z^i), i=0,...,4,
(a0,a1,a2,a3,a4)=(3r-1/2,6r+2,0,4r-5/3,(66r+13)/18).
```

All their normal coefficients are checked exactly modulo the quadratic.
Every pairwise difference `a_i-a_j` is a unit in the field.

For `E=sum(e_i*z^i)`, the two primitive basis coefficients determine
the constant and eighth coefficients of h freely. Containment determines
them uniquely as the corresponding coefficients of `delta*E`. The
remaining seven equations are the coefficients z through z^7 of
`delta*E-sum(a_i*e_i*z^(i+2))`. Hence the containing-quartic space is
isomorphic to the kernel of the displayed `7x5` operator. In particular,
E zero does not leave an extra primitive quartic: it forces h zero and
both primitive coefficients zero.

## Coverage of every defect section

The four minor identities provide an exhaustive case split:

1. If d0 is nonzero, the lower `4x4` triangular minor is d0^4.
2. If d4 is nonzero, the upper `4x4` triangular minor is d4^4.
3. With d0=d4=0, the first five-row determinant is d1^5, and the last
   five-row determinant is d3^5. A nonzero d1 or d3 gives rank five.
4. The entire remaining locus is `delta=d2*z^2`. Its middle five-row
   matrix is `diag(d2-a0,...,d2-a4)`. Since the a_i are pairwise distinct,
   at most one diagonal entry can vanish, so rank is at least four.

These are polynomial identities and field-unit statements, valid at
both roots of the quadratic. They prove rank at least four everywhere,
and kernel dimension at most one. The last case explicitly retains the
section with double zeros at both endpoints. A section with d4 zero has
an infinity zero; it is covered by the same coefficient split. Nothing
in the argument assumes reduced support.

If two quartics F,G gave `F*alpha=u,G*alpha=v`, both would contain the
canonical triple and would be proportional in this at-most-one-dimensional
space. Their images would be proportional, contrary to the independent
targets. This uses the accepted canonical-triple reduction for ancestors,
not an STCI mate bound or a further carrier classification.

## Fresh replay and provenance

The retained self-contained
[`source`](../computations/verify_session_localcoh_e1_d4_algebraic_2026_10_08.py)
was inspected and freshly replayed from an exact byte snapshot in an
isolated directory. It reads no discovery JSON or generated proof input.
The source SHA256 is

```text
ae88024f00b8216be727957930747001b44f457e532a0746e6a8e2a657850a02
```

The replay completed with exit code zero and all assertions passed. Its
source copy, generated complete matrix/basis JSON, output log, and hashes
are preserved under
[`2026-10-08-e1-d4-algebraic-audit`](../validation/2026-10-08-e1-d4-algebraic-audit/replay-manifest.json).
The generated JSON is byte-identical to the retained canonical generated
JSON; the original source and generated JSON were not modified. This
audit does not edit any canonical frontier file.
