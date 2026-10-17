# The six defective e=1 endpoint triples also exclude quartic ancestors

Date: 2026-10-08. Fixed `C0` in characteristic zero. Status:
**PROVED COROLLARY OF THE ACCEPTED COMPLETE QUARTIC FIBRES AND P-037.**
This is an ancestor-specific consequence; it uses no STCI mate, BF mate
bound or single-carrier cubic-pole inference.

Let quartics `F,G` and an ancestor alpha satisfy `F*alpha=u,G*alpha=v`.
Their canonical triple is contained in both multipliers. If it has
`e=1,d2=1` and is on the complete `a0=0` or `b1=0` boundary of the
defect-killed quadratic class, the actual torus normalization gives one
of the six triples from
[`2026-10-07-session-mf6-e1-d1-endpoints.md`](2026-10-07-session-mf6-e1-d1-endpoints.md):

```text
A=r*z, B=1+z, delta=z,
or A=1+r*z, B=1, delta=1,
with r=-1/2 or 12r^2+4r+3=0.
```

At each of the four algebraic direction fibres, the **complete** quartic
space has dimension one (rank 34 in all 35 ambient monomials). Hence
F and G are proportional. Their images u and v would then be
proportional, contradicting their linear independence.

At each of the two rational-root fibres, the complete quartic space is
`C*H0(P3,O(1))`, with the fixed nonzero cubic C equal to C_L or C_R
from the endpoint audit. Thus `F=C*F1,G=C*G1` for actual homogeneous
linear forms F1,G1, and

```text
F1*(C*alpha)=u, G1*(C*alpha)=v.
```

This is a common ancestor with degree-one multipliers, prohibited by
the all-stage P-037 theorem. Since u is nonzero, `C*alpha` is nonzero;
the passage does not annihilate the ancestor.

The only symmetry used to normalize the six triples is the actual
ambient torus preserving C0 (and the reversal for equivalent charts).
Under the torus `(x0,x1,x2,x3)->(x0,lambda*x1,lambda^3*x2,lambda^4*x3)`,
q and B have weights four and six and the target numerators have weights
three and five. Therefore u and v are eigenvectors of respective
weights -7 and -5. Nonzero scalings can be absorbed into F1,G1, so
P-037 remains applicable to the fixed targets. Coordinate reversal
preserves q, sends B to -B, and swaps the two target numerators;
it exchanges u and v with the same harmless nonzero sign.

All six endpoint triples are therefore excluded from the quartic-ancestor
problem. The principal `a0*b1!=0` portion of the d2=1 sextic remains
open, as do the positive-defect d2=2,3,4 ancestor strata. In particular
the d2=4 Gorenstein case remains; its elimination does not follow from
the STCI quartic bound.

More generally, the same exact argument excludes a candidate canonical
triple if its full quartic space has dimension at most one, or if every
quartic in that space has a fixed factor of degree one, two or three:
division gives multipliers of degree at most three, prohibited by P-037.
This is a useful first check before computing the unique conormal
socle quotient from the splitting criterion.

The complete ambient fibre ranks and fixed factors were independently
audited in the endpoint source. The MF6 auditor reconfirmed those ranks,
the actual torus weights and reversal on 2026-10-08. This proof depends
on those complete spaces; merely inspecting the displayed FL/FR forms
would not suffice.
