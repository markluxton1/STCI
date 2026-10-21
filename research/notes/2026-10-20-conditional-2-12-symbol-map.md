# Exact global sextic symbol map in the conditional (2,12;6,16;2) lane

Date: 2026-10-20. Status: **new exact reduction and evidence; independently
reviewed proposal, no canonical promotion**. See
[the independent audit](2026-10-20-conditional-2-12-incidence-audit.md).
Work over an algebraically closed field of characteristic
zero with `C0=[s^4:s^3t:st^3:t^4]`. The intended application assumes the
full generic ordinary initial ideal is a coprime binary CI of degrees
`(2,12)` and the actual first relation is saturated. This note computes
one global-symbol restriction and its first subsequent sextic lifting
condition. It does not prove that the combined root incidence is empty.

## Inputs and authority

The balanced conormal `E=O_P1(-7)^2`, the exact embedded chart, and the
universal first ambient incidence are used as accepted inputs from
[STCI-R-0007](../results/quadratic_root_obstruction_model.md) and its
linked evidence. The normal-flatness theorem relevant to the intended
actual-CI application is
[STCI-R-0010](../results/saturated_first_relation_normal_flatness.md).
No accepted chart, saturation, or first-obstruction theorem is rerun.

The new evidence is
[the standard-library Python script](../computations/conditional_2_12_symbol_map_2026_10_20.py)
and [its full rational JSON output](../computations/conditional_2_12_symbol_map_2026_10_20.json).
Run `python3 research/computations/conditional_2_12_symbol_map_2026_10_20.py`.
The accepted first-incidence Jacobian is read from its saved JSON as an
input for the new tangent-space comparison; that input's SHA256 is
recorded in the new output.

## The exact map and its global source

On the first base chart let `z=t/s`. Use the accepted balanced normal
coordinates

```text
(x0,x1,x2,x3)=(1,z,z^3+v,z^4+u+(3/2)zv).
```

Both conormal frame vectors have transition `z^-7`. Since
`O_C0(6)=O_P1(24)`, the requested map has target

```text
H0(Sym^2 E(6))=H0(O_P1(10))^3,
```

with ordered basis `z^j u^2`, `z^j uv`, `z^j v^2`, each `j=0,...,10`.
For an actual homogeneous sextic `F`, its exact second symbol is

```text
sigma2(F)=[F(1,z,z^3+v,z^4+u+(3/2)zv)]_(normal degree 2).
```

This formula uses actual global `k`-coefficients throughout.

Set

```text
q=x0*x3-x1*x2,
A=x0^2*x2-x1^3,
B=x0*x2^2-x1^2*x3,
D=x2^3-x1*x3^2.
```

A basis of the global source is the following list of 23 sextics:

```text
q^2 times all ten quadratic monomials in x0,x1,x2,x3;
q*A*x0, q*A*x1, q*A*x2, q*A*x3;
q*B*x2, q*B*x3, q*D*x2, q*D*x3;
A^2, A*B, A*D, B*D, D^2.
```

The script checks this source without relying on a saturation claim.
There are 84 ambient sextic monomials. Their zeroth and first normal
coefficients form a rational matrix of rank 61, so the global kernel
has dimension 23. Vanishing on the dense affine part of `C0` suffices:
first the restriction is a section of `O_C0(6)`, and after that vanishes
the first symbol is a section of the vector bundle `E(6)`; either
section vanishes globally if it vanishes densely. Thus this kernel is
exactly `H0(I_C0^2(6))` for the sheaf square. The displayed 23 ordinary
ideal-product sextics are independently linearly independent and belong
to that kernel. They therefore span the entire sheaf-theoretic source,
including any possible homogeneous saturation issue in this degree.

The second-symbol matrix has rank 22. The sextic `q^3` has zero second
symbol, so the kernel is exactly `k*q^3`. An image basis is obtained by
omitting `q^2*x1*x2` from the displayed source basis. Indeed the only
kernel relation is

```text
q^2*x0*x3-q^2*x1*x2=q^3.
```

The JSON contains both the full `33 by 23` map and this `33 by 22` image
basis, with all entries exact rational numbers. For the displayed image
columns, the minor on target rows `P0,...,P10,Q0,...,Q9,R0` has determinant
exactly `48`; this is a compact rank-22 certificate.

## Eleven equations for the 22-dimensional image

Write a target element as

```text
P(z)u^2+Q(z)uv+R(z)v^2,
P=sum P_j z^j, Q=sum Q_j z^j, R=sum R_j z^j.
```

The image `V_(6,2)` is exactly the common kernel of the following eleven
independent linear forms:

| Row | Linear form |
| --- | --- |
| 1 | `P9-2Q10` |
| 2 | `Q0-2R1` |
| 3 | `P0-2Q1+4R2` |
| 4 | `3P1-2Q2-4R3` |
| 5 | `P2-2Q3+4R4` |
| 6 | `P3-2Q4+4R5` |
| 7 | `P4-4R6` |
| 8 | `P5-2Q6+4R7` |
| 9 | `P6-2Q7+4R8` |
| 10 | `P7+2Q8-12R9` |
| 11 | `P8-2Q9+4R10` |

The rational calculation verifies that these rows annihilate all 22
image columns and have rank eleven. Together with rank 22 of the map,
this proves equality with the image, rather than only necessity.

For `f=a(z)u^2+b(z)uv+c(z)v^2`, with base-quadratic `a,b,c`, and
`alpha=sum_(i=0)^8 alpha_i z^i`, put

```text
P_j=sum_i alpha_i a_(j-i),
Q_j=sum_i alpha_i b_(j-i),
R_j=sum_i alpha_i c_(j-i),
```

with coefficients outside their allowed ranges zero. Substitution in
the table gives eleven explicit bilinear equations on
`U x P(H0(O_P1(8)))`, where `U` is the basepoint-free open in the root
coefficient space `P8`. The multiplier is nonzero but may have zeros.
This is an exact scheme presentation of the new membership condition
`alpha*f in V_(6,2)`. It introduces no rational-function coefficients.

## The new restriction is not automatic on the first incidence

For the accepted first-compatible smooth torsion-two seed

```text
f0=(z^2+4)u^2+(z^2-8)v^2,
```

the eleven-by-nine multiplier matrix has rank eight. Its one-dimensional
kernel is generated by

```text
alpha0=z^8-8z^6+96z^4+256z^2+1024.
```

Thus the new symbol condition alone does not exclude the seed. Its
accepted second ambient obstruction is already nonzero, equal to
`1/8`, so this point is not a survivor of the full first-plus-second
obstruction test.

Nevertheless the new global condition is not automatic on the accepted
first compatibility scheme `K1`. At `(f0,h0,alpha0)`, append the eleven
new bilinear equations to `A_f h=d_f`. In the 30 affine variables
`f9,h12,alpha9`, the combined 27-row Jacobian has rank 26. After removing
the two independent projective scaling directions, its tangent dimension
is two. Because the projective multiplier is unique at the seed, this
is also the tangent dimension of the projected membership incidence.
The accepted `K1` is smooth of projective dimension four at `[f0]`.
The new global symbol condition therefore removes first-compatible
tangent directions. This is a tangent-space statement, not an assertion
that the new scheme has dimension two. It says nothing by itself about
the intersection with the second ambient obstruction and the torsion
locus.

## The first subsequent condition on an actual sextic

Let `c_1,...,c_23` be actual `k`-coefficients in the displayed sextic
basis, write `F_c` for their global sextic, and let `M` be the exact
second-symbol matrix. Over the membership incidence impose

```text
M*c=coeff(alpha*f).
```

Its solution fiber is an affine line in the `q^3` direction. On `K1`
the accepted ambient model gives the canonical first cubic correction
`G0`, with base degree at most one. The next necessary condition for
`F_c` to belong to the lifted first relation is

```text
F_(c,3)-alpha*G0=f*(ell(z)u+m(z)v),       deg ell,m <=7.       (C3)
```

Here `F_(c,3)` is the literal normal-degree-three part of the global
sextic in the accepted chart. Its base degree is at most eight, as
checked for every source basis vector; `alpha*G0` has base degree at
most nine. Since `f` is basepoint-free at infinity, at least one of its
homogeneous quadratic base coefficients has nonzero leading affine
coefficient. Multiplication of the leading nonzero binary normal forms
then proves the degree bound seven for `ell,m`. Thus (C3) is exactly
forty coefficient equations in the four cubic normal monomials and
base powers `0,...,9`. The `40 by 23` matrix of `F_(c,3)` is saved in the
JSON. This is a finite next obstruction with actual global sextic
coefficients; it is not an unrestricted homogeneous-equation search.
The test is invariant under adding multiples of `f` to the chosen
local cubic representative, because `ell,m` absorb that change.

For the accepted seed, the canonical correction is

```text
G0=(z/8)u^2v-(3/4)uv^2+(z/8)v^3.
```

With the multiplier `alpha0` above, the 33 symbol equations and forty
cubic equations give a rational system with 39 unknowns
`c23,ell8,m8`. Its coefficient matrix has rank 39, while its augmented
matrix has rank 40. The JSON stores an exact annihilating row and its
nonzero target pairing `-384`. For a short independently checkable
description, order the target first as `P0,...,P10,Q0,...,Q10,R0,...,R10`
and then as cubic coefficients `T_(i,j)` of `z^j*u^(3-i)*v^i`. The row is

```text
P4+64P8-192P10+Q5-16Q7
 +3T_(0,0)-12T_(0,2)+48T_(0,4)-192T_(0,6)+768T_(0,8)
 -2T_(1,1)+8T_(1,3)-32T_(1,5)+128T_(1,7)-512T_(1,9).
```

It annihilates every pair `(M*c,F_(c,3)-f*(ell*u+m*v))`, but its value
on `(coeff(alpha0*f0),coeff(alpha0*G0))` is `-384`. Hence even this
symbol-compatible seed cannot be realized by a global sextic matching
the unique first ambient lift. This is consistent with its already
known second-obstruction failure and does not exclude a new component
of the fully combined incidence.

## Unresolved scope

The complete intersection of the eleven global-symbol equations with
the accepted universal first incidence, all twenty-five second dual
pairings, and exact Picard torsion descent is not solved by this note.
Equation (C3) is the first exported subsequent condition on the global
sextic. No global degree-sixteen mate, degree-twelve standard basis,
full initial-pair coprimality, or global gcd/Bezout certificate is
constructed. A nonempty low-order incidence would establish none of
those facts.

The independent audit passes the specified exact reduction. Canonical
promotion would require a separate reviewed change to result records.
