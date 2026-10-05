# e=2 quartic-carrier obstruction: stabilizer, generic cross-section, and surviving family

Date: 2026-10-05

Status: **characteristic-zero continuation**. The ambient-stabilizer statement and the three-parameter exclusion are PROVED; the full four-parameter obstruction formulas are an exact computational result with strong cross-checks, including exact specialization checks. The explicit surviving family and the resulting falsification of the universal cubic exclusion are independently reconstructed and verified. Nothing here constructs a quartic carrier or an STCI presentation.

Throughout,
[
C_0=[s^4:s^3t:st^3:t^4]subsetmathbf P^3.
]

## 1. Ambient stabilizer — PROVED

The embedding linear system is
[
W=langle s^4,s^3t,st^3,t^4anglesubset H^0(O_{mathbf P^1}(4)).
]
In characteristic zero the only (PGL_2) transformations preserving (W) are
[
zmapstolambda z,qquad zmapstolambda/z.
]
The kernel of
[
operatorname{Stab}_{PGL_4}(C_0)	ooperatorname{Aut}(mathbf P^1)
]
is trivial. Hence
[
oxed{operatorname{Stab}_{PGL_4}(C_0)congmathbf G_mtimesmathbf Z/2.}
]
In the formal coordinates used below the torus acts by
[
zmapstolambda z,qquad Umapstolambda^4U,qquad Vmapstolambda^3V.
]
There is no hidden continuous ambient symmetry reducing a general (e=2) quotient to the earlier two-parameter family.

## 2. Generic e=2 symmetry cross-section

On (A_2B_0
e0), projective scaling plus the genuine ambient torus normalize a general (e=2) quotient to
[
oxed{A=x+az+z^2,qquad B=1+bz+dz^2.}
]
This is a generic cross-section to the actual symmetry, **not literally an affine chart of (P^5)**.

The resultant is
[
oxed{Delta=1-ab+a^2d-2dx+b^2x-abdx+d^2x^2.}
]
Basepoint-free is equivalent to (Delta
e0).

On (xd
e0), inversion acts by
[
oxed{(x,a,b,d)mapstoleft(rac{x}{d^2},rac ad,rac bx,rac d{x^2}ight).}
]
Thus the previously studied (x=b=0) family is codimension two in the essential generic moduli.

## 3. Formal-neighborhood audit — independently audited

The nonlinear two-chart transition was independently reconstructed. A crucial point is
[
oxed{w
e1/z}
]
off the reduced curve. Freezing (w=1/z) destroys higher-order information contributing to the obstruction. Calculations using a frozen opposite-chart coordinate must not be reused unless separately corrected.

Several exploratory slice/factorization claims from the research conversation were discarded during this audit and are not promoted here.

## 4. Three-parameter b=0 family — PROVED

For
[
A=x+az+z^2,qquad B=1+dz^2,
]
put
[
Delta_0=1+a^2d-2dx+d^2x^2.
]
The quadratic graph corrections and all five cubic obstruction numerators (G_i(a,d,x)) were independently regenerated. Exact Gröbner reduction gives
[
oxed{Delta_0in(G_1,ldots,G_5).}
]
Consequently
[
G_1=cdots=G_5=0LongrightarrowDelta_0=0.
]
Hence no basepoint-free member of this entire three-parameter family extends from the relevant primitive triple to a primitive quadruple. This strictly strengthens the earlier (x=b=0) result.

## 5. Full four-parameter cubic obstruction — exact computation with strong cross-checks

For
[
A=x+az+z^2,qquad B=1+bz+dz^2,
]
the cubic mismatch has form
[
M_3=rac{N(z;x,a,b,d)}{32z^{25}Delta^3}.
]
The five relevant coefficients of (N) are each exactly divisible by (Delta^2). Therefore
[
oxed{Omega_i=rac{G_i(x,a,b,d)}{32Delta},qquad i=1,ldots,5.}
]
The exact (G_i) are persisted in
`../computations/e2_full4_obstruction_2026-10-05.txt`.

Exact checks:
- (b=0) reproduces all five independently audited three-parameter obstruction polynomials;
- (x=b=0) reproduces the retained two-parameter obstruction polynomials.

## 6. Universal cubic e=2 exclusion — FALSE

The attempted implication
[
oxed{Omega=0LongrightarrowDelta=0}
]
is **FALSE**.

On (dx=1), write (u=bx-a). Then
[
Delta=rac{u^2}{x}
]
and all five obstruction numerators factor as (G_i=uQ_i). On
[
a=-rac12,
]
all five original (G_i) vanish when
[
u=rac12-2x,
]
equivalently (b=-2). Thus
[
oxed{A=z^2-rac12z+x,qquad B=1-2z+rac1xz^2}
]
satisfies
[
oxed{G_1=cdots=G_5=0.}
]
Its resultant is
[
oxed{Delta=rac{(4x-1)^2}{4x}.}
]
For (x
e0,rac14), the pair is basepoint-free. Therefore the corresponding (e=2) primitive triple extends to a primitive quadruple.

This falsifies the proposed universal **first nontrivial extension-obstruction strategy**. It does not construct a quartic carrier.

## 7. Scope and revised frontier

Do **not** infer:
- existence of an (e=2) quartic carrier;
- existence of an STCI presentation;
- failure of the desired no-quartic-carrier theorem for (C_0);
- failure of the global STCI conjecture.

The surviving family proves only that the first nontrivial extension obstruction is insufficient.

The immediate (e=2) question is:

> Exactly what infinitesimal multiplicity/order does a genuine (e=2) quartic carrier force, and does the explicit surviving primitive quadruple extend through the next required stage?

The sharp test family is
[
A=z^2-rac12z+x,qquad B=1-2z+x^{-1}z^2.
]

Continued higher-order (e=2) computation is not automatically the highest-value global strategy. Other live branches remain:
- equivariance/representation-theoretic interpretation of (Omega);
- (e=1);
- (e=0);
- whether the local-cohomology route can treat (e=0,1,2) uniformly.

All formal calculations in this note currently carry the characteristic-zero caveat.
