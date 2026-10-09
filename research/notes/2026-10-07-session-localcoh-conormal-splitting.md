# Intrinsic conormal splitting required by every common quartic ancestor

Date: 2026-10-07; current files and rank criteria re-audited 2026-10-08.
Fixed `C0` in characteristic zero. Status:
**PROVED NECESSARY CRITERION**, conditional on the accepted quartic-ancestor
filtration, socle-pencil theorem and intrinsic conormal sequence. This
criterion does not establish emptiness of a remaining parameter stratum.
In particular, the `e=1,d2=d3=4` Gorenstein case is retained.

## 1. The global splitting theorem

Let a common quartic ancestor define its CM quadruple `Z4`, and let
`Z3=Z4/E3` be the canonical triple, with ideal sheaf `J`. Set

```text
V=(J/(I_C*J))/torsion.
```

The accepted intrinsic normal-layer calculation is valid for a defective
triple as well as a primitive one, and gives

```text
0 -> L^3(D2) -> V -> M(-D2) -> 0,
L=O(e-7), M=O(-e-7), degV=2e-28.
```

For example the local Hilbert--Burch presentation at a defect has two
free normal generators and a torsion summand supported on the defect.
This is the sequence used in the independent MF6 audit. Its use in the
ancestor setting needs one additional functorial check: every element
of `J` maps in `OZ4` into the socle line `E3`. Since `I_C*E3=0`, that
map factors through `J/(I_C*J)`. Any torsion element maps to zero because
`E3` is a line bundle. Hence there is a well-defined map

```text
phi: V -> E3=O(-14).
```

The two actual quartic multiplier sections of `V(4)` map to the
basepoint-free normalized target pencil in `E3(4)=O(2)`. At every
point one target is a unit in a local line frame, so `phi` is surjective
as a sheaf map. Its kernel is a line bundle of degree `2e-14`:

```text
0 -> O(2e-14) -> V -> O(-14) -> 0.
```

The extension group is `H1(O(2e))`, which vanishes for every `e>=0`.
Consequently every common quartic ancestor necessarily satisfies

```text
V=O(2e-14) direct-sum O(-14),
V(4)=O(2e+2) direct-sum O(2).
```

For `e=0,1,2`, these are respectively `O(2)^2`, `O(4)+O(2)` and
`O(6)+O(2)` after the quartic twist. This is an intrinsic requirement
on the canonical triple. It does not impose vanishing of F or G in
the quadruple: their images remain the two nonzero socle targets.

## 2. Exact Hankel rank form for the remaining e=1 defects

The socle theorem gives `d3=4`. The accepted simultaneous-target proof
excludes `d2=0`. It leaves precisely `d2=1,2,3,4` at the level of the
filtration inequalities `0<=D2<=D3`. The STCI quartic BF bound `d2<=3`
must not be imported into this ancestor setting.

For a fixed `D2` of degree d2, the intrinsic sequence after twisting is

```text
0 -> O(d2-2) -> V(4) -> O(8-d2) -> 0.
```

Put `n=5-d2`. Its extension class lies in `H1(O(-2n))`, represented on
the two standard P1 charts by a Laurent class

```text
eta=c1*z^-1+c2*z^-2+...+c(2n-1)*z^-(2n-1).
```

Twisting by `O(-4)`, the connecting map is

```text
delta_eta: H0(O(n-1)) -> H1(O(-n-1)).
```

In the bases `1,z,...,z^(n-1)` and `z^-1,...,z^-n`, its matrix is the
symmetric n-by-n Hankel matrix `H_ij=c(i+j+1)`, indexed from zero.
The required split type is **equivalent** to

```text
rank H=n-1.
```

Indeed its kernel has dimension `h0(V(4)(-4))`. Every rank-two bundle
of degree six on P1 splits as `O(a)+O(6-a)`. That h0 equals one
exactly for the desired split `O(2)+O(4)`: a summand of degree four
contributes one, any larger summand contributes at least two, and
the balanced `O(3)^2` contributes zero.

Thus the exact required ranks are:

| d2 | Extension dimension | Connecting matrix | Required rank |
| --- | --- | --- | --- |
| 1 | 7 | 4 by 4 symmetric Hankel | 3 |
| 2 | 5 | 3 by 3 symmetric Hankel | 2 |
| 3 | 3 | 2 by 2 symmetric Hankel | 1 |
| 4 | 1 | 1 by 1 | 0 |

For d2=3 this is `c1*c3-c2^2=0` with the matrix nonzero. For d2=4 it
is exactly `eta=0`. A nonzero extension of `O(-12)` by `O(-14)` has
middle bundle `O(-13)^2`, so it cannot occur. No argument has yet
excluded the zero extension or the Gorenstein quadruple possibility.

## 3. Endpoint e=2 and constant-direction e=0 forms

For e=2 the socle theorem gives `d3=1`, and the same splitting theorem
requires `V(4)=O(2)+O(6)`.

For d2=0, twist its intrinsic sequence by `O(-6)`. The connecting map
is `H0(O(1))->H1(O(-5))`, a four-by-two Hankel matrix using the five
Laurent coordinates of `H1(O(-6))`. It must have rank exactly one.
For d2=1, the map is `H0(O(0))->H1(O(-4))`, a three-by-one matrix;
it must be zero. Thus the defective e=2 triple requires its entire
three-coordinate intrinsic extension class to vanish. These are
necessary splitting conditions, not exclusions. The actual ambient
extension class still has to be evaluated on each remaining direction
and lower correction.

For e=0, write `m=7-d2`. If m>=1, twisting by `O(-3)` gives the
square connecting map `H0(O(m-1))->H1(O(-m-1))`. The required middle
bundle `V(4)=O(2)^2` is equivalent to this m-by-m Hankel map being
invertible. For m=0 the intrinsic sequence already splits as `O(2)^2`.
This is a different rank from the e=1 case; do not transfer a rank-one
or singular-Hankel condition to the constant-direction lane.

## 4. Continuation target and exact scope

For `e=1,2`, the required quotient `V(4)->O(2)` is unique up to a
nonzero scalar. Indeed every map from its maximal summand `O(2e+2)`
to `O(2)` is zero, while the endomorphisms of the lower summand are
constants. Thus a remaining triple does not have a free socle-map
parameter after the splitting criterion holds. The actual ambient
quartic space `H0(J(4))` maps to `H0(V(4))`; projecting by this unique
quotient must produce both normalized sections `1,z^2`. A rank-one
image, or a two-dimensional image different from `span(1,z^2)`, excludes
that triple. A three-dimensional image merely passes this necessary
quartic-image condition and does not establish an inverse-system
ancestor.

For e=1, the maximal-summand section is the unique nonzero element of
`H0(V(4)(-4))`, given by the kernel of the exact Hankel matrix above.
For e=2 use `H0(V(4)(-6))`. If `kappa` is this nowhere-vanishing
section and S is the actual normal-layer image of a quartic, the
socle-quotient section is `det(kappa,S)` in O(2), up to the single
common scalar. This gives a direct linear image test after the
intrinsic extension class is evaluated; it avoids introducing arbitrary
quartic multiplier coefficients prematurely.

The next substantive computation is the actual ambient Laurent
extension class eta of V for defect-killed canonical triples, followed
by these exact rank conditions and the two-target image map. A generic
rank is not a parameter-space exhaustion. The whole d2=4 boundary,
including its new global triple correction parameter, must remain.

The root and the independent MF6 auditor confirmed the functorial map
and degree computation on 2026-10-07. The coefficient exporter
`session_localcoh_conormal_hankel_2026_10_07.py` records the connecting
matrices and the e=1 determinant equations symbolically. It does not
evaluate the actual ambient class and makes no new family exclusion.
The independent standard-library checker
`verify_session_localcoh_conormal_splitting_2026_10_08.py` reconstructs
the cup-product coefficients and symbolic determinants from the saved
record and verifies the degree/rank equivalences. Its validation record
stores fresh source, proof and output hashes.
