# Divisor compression and bounds on generically regular carriers

These are reusable conditional theorems, not an exclusion for arbitrary
higher-degree carriers. Global compression requires a normal hypersurface
and a rational **whole** resolution. The order-one normal-line inequality
also applies to a generically regular nonnormal carrier, by the independently
reviewed [pullback defect proof](numerical_surface_pullback.md). Characteristic
zero is retained for the fixed-quartic normal-bundle, BF and surface-classification
applications; the Picard/section-lifting compression itself is valid on rational
surfaces in other characteristics when its same geometric hypotheses hold.

## 1. Global denominator compression

Let `S` be a normal integral hypersurface of degree `a`, with smooth
rational projective resolution `sigma:M->S`, and let `C` be an integral curve of degree
`delta`. A degree-`b` mate gives an effective Cartier divisor `rC` with
`r delta=ab`. Put `H=sigma^*O_S(1)` and write the numerical pullback of
`C` as `c+Z`. Then `c+Z == (delta/a)H` in the numerical divisor space.

Let `n` be the least positive integer clearing the denominators of both `Z` and `delta/a`. The divisor

    n((delta/a)H-c-Z)

is integral and numerically trivial. On a smooth projective rational
surface numerical triviality implies linear triviality: this is true on
`P^2` and on a Hirzebruch surface, and a blowup adds a free exceptional
Picard summand. One can also use a common smooth resolution of a
birational map to one of these surfaces. This includes the absence of
numerically trivial torsion, not merely the vanishing of `Pic^0`.

The integral divisor is therefore principal. Pushforward of a principal
divisor under the birational map is the principal divisor of the same
rational function on the normal surface; exceptional prime divisors
disappear. Consequently

    nC ~ (n delta/a)H_S

as **Weil divisors** on `S`. Because the divisor on the right is Cartier,
`nC` is Cartier. Its effective divisor supplies a nonzero section of
`O_S(n delta/a)`. The hypersurface restriction sequence lifts that section
to `P^3`, since `H^1(P^3,O(t))=0` for every integer `t`. Its zero support
on `S` is precisely `C`.

Normality matters twice: principal-divisor pushforward has the expected
Weil-divisor meaning, and the effective Cartier divisor determined by the
section has the specified support. Rationality of the **whole** resolution
matters for numerical-to-linear equivalence. The argument makes no
assertion that numerical coincidence on a nonrational resolution suffices.

For `a=delta=4`, the integer `n` is the least common denominator of `Z`.
Every actual mate degree `b` makes `b(c+Z)` an integral Cartier pullback,
so every coefficient denominator divides `b`. Hence `n|b`. Compression
then produces a degree-`n` mate, making `n` the exact least mate degree for
this fixed normal quartic carrier under the existence hypothesis. It
legitimately removes possible local torsion inflation in this global
rational-resolution setting; it does not assume a cancellation law in an
arbitrary local class group.

## 2. A determinant bound with singular or nonreduced anticanonical divisor

For this section add the **normal-quartic rational-resolution**
classification hypotheses: the resolution is minimal, there is an
effective exceptional anticanonical divisor \(E=-K_M\), and
\(d=-E^2\in\{1,2,3\}\) with \(\rho(M)=10+d\). These are extra
geometric inputs from the classified normal quartics, not consequences
of the arbitrary-degree compression theorem in Section1.

Take **all** exceptional prime curves `E_i` of the minimal resolution and
write

    A_ij=-E_i.E_j,  b_i=-E_i^2,  E=sum a_i E_i.

Here `A` is positive definite, each `b_i` is a positive integer, and each
`a_i` is a nonnegative integer. Exceptional classes are independent and
orthogonal to `H`, which has positive square. Therefore

    r<=rho(M)-1=9+d.

Relative nefness and adjunction for an integral curve on a smooth surface
give

    (Aa)_i=K_M.E_i=b_i+2p_a(E_i)-2>=0.

Arithmetic genus, rather than geometric genus, is the correct invariant
here. It is nonnegative even when the prime curve is singular. If `a_i=0`,
the expression also equals `-E.E_i<=0`; therefore it is zero. Since
`b_i>0`, this forces `b_i=2`, `p_a(E_i)=0`, and disjointness from the
support of `E`. In particular a vertex with `b_i>2` has `a_i>=1`.

All terms in the following sum are nonnegative:

    d=a^T A a=sum a_i(b_i+2p_a(E_i)-2).

For every vertex with `b_i>2`, its summand is at least `b_i-2`. Thus

    sum (b_i-2)_+ <= d.

The integer inequality `b<=2(3/2)^((b-2)_+)` holds for every `b>=1`;
after `b=3` it follows by multiplying successively by ratios at most
`3/2`. Hadamard's inequality consequently yields

    det A <= product b_i
          <= 2^r (3/2)^d
          <= 512*3^d.

The numerical correction is `Z=A^(-1)m` with integral
`m_i=c.E_i`. The adjugate formula implies that its common denominator
divides `det A`. Combining with section 1 gives compressed mate bounds
`1536`, `4608`, and `13824` for `d=1`, `2`, and `3`, respectively.

No step assumed that `a_i=1`, that the components are smooth rational
curves, or that the dual graph is a reduced cusp cycle. The use of
arithmetic genus and the nonnegative integer multiplicities is exactly
what allows singular, reducible and nonreduced anticanonical divisors.
The estimate would not follow from an arbitrary further blowup, since
that could introduce exceptional `(-1)` curves and destroy relative
nefness; the source explicitly supplies the required minimal resolution.

## 3. A small cusp numerical survivor is killed by the compression

A reduced rational cycle with intersection matrix

`A=[[3,-1,0,-1],[-1,2,-1,0],[0,-1,2,-1],[-1,0,-1,2]]`

has `E=sum E_i`, `E^2=-1`, and determinant four. A smooth-curve
intersection vector meeting the vertex opposite the `(-3)` vertex would
be `m=(0,0,1,0)`. The correction is

`A^(-1)m=(1,3/2,2,3/2)` and `m^T A^(-1)m=2`.

Adding six independent `A1` intersections gives total correction five,
with numerical denominator two. If this configuration belonged to an
actual mate-compatible rational normal quartic, §1 would produce a
quadric mate, contradicting the unique-quadric obstruction.

This is an exact numerical illustration, not a claim that the specified
smooth curve passage or first-normal order exists on a quartic. In
particular assigning a local first-normal order of three at this cusp
has not been justified. The point is that a numerical configuration
which survives a coarse genus/rank budget may still be eliminated by
global denominator compression.

## 4. The normal-line bound for an order-one carrier

Let `(F_a,G_b)` define a characteristic-zero smooth rational quartic
set-theoretically, with `F_a` of generic normal order one. Every
irreducible factor of `F_a` must contain `C`: its intersection with
`G_b` has a curve component in projective three-space, and the complete
intersection has reduced support only `C`. A common factor of both
equations would give an impermissible surface component. Two factors
containing `C`, including a repeated factor, would give normal order at
least two. Thus `F_a` defines an integral surface `S`, regular at the
generic point of `C`.

The identification of the BF line bundle with the normal sheaf can be
made explicit. If `N_C^*=O(-7)^2`, the first symbol of `F_a` defines a
rank-one image whose saturation is a line subbundle. The conormal of
`C` in `S` is the cokernel of that symbol; after removing torsion it is
the quotient by the saturated image. The mate has the same generic first
symbol direction, or zero first symbol: independent directions would
make the transverse intersection length one, whereas `ab/4>=4`.
Consequently this saturated quotient is the BF first piece

    L=O(e-7),

and `deg N_(C/S)=7-e`. Zeros of the carrier symbol contribute torsion,
not a change of this torsion-free quotient. This prevents an accidental
extra divisor from entering (U4).

Since the carrier is regular at generic `C`, its normalization is an
isomorphism there. The unique curve `C^nu` above `C` maps isomorphically
to the smooth curve `C`: its rational lift extends across each point by
properness, giving a section and hence a closed immersion. Normalization
is finite, so it has no exceptional curve over a closed point of `S`.
The mate's Cartier divisor on the normalization is exactly `mC^nu`,
where `m=ab/4`. On a resolution, its Cartier pullback shows

    (C^nu)^# == (b/m)H = (4/a)H,
    ((C^nu)^#)^2 = 16/a.

The [numerical-pullback proof](numerical_surface_pullback.md) gives the exact comparison:
principalizing the curve ideal gives `D=c+Z`, relative generation gives
`D.E_i<=0`, and the positive-definite matrix with nonpositive
off-diagonal entries implies `Z>=R` for the numerical correction `R`.
The restricted ideal surjection identifies the torsion-free conormal
with `O_c(-D)`, so

    deg N_(C/S)-((C^nu)^#)^2=(Z-R).c>=0.

This proof still applies if `S` is nonnormal at finitely many points on
`C`: all resolution exceptional curves map to points after its finite
normalization, while generic regularity preserves coefficient one along
the strict transform. Thus

    16/a <= 7-e,
    a >= ceil(16/(7-e))

is verified. Together with the already known `a>=4`, the bounds for
`e=0,...,6` are `4,4,4,4,6,8,16`. The degree here belongs to the
generically regular carrier, and cannot be assigned to a mate whose
generic normal order is higher.

## 5. Early-defect and ancestor degree bounds

The [order-one frontier argument](../supplements/ORDER_ONE_JETS_AND_DEGREE_BUDGETS.md#2026-10-06-uniform-order-one-frontier)
has the following direct algebraic consequence. For a,b>=4 and an order-one equation, set
s=ab/4-1 and c=7-e. Adjunction gives

\[
\deg D_s=cs+14-4(a+b).
\]

Effectivity forces c>0, so e<=6. Writing s=2q+r or s=3q+r and using
superadditivity gives q deg D2<=2cq+cr+14-4(a+b), and the analogous
third-defect bound. Since c<=7, the additive correction is strictly
negative in both cases (at most 7-18 or 14-18). Thus

\[
\deg D2\le2(7-e)-1,\qquad\deg D3\le3(7-e)-1.
\]

Here q>=1 because ab/4>=4. For the fixed-C0 ancestor application with
the recorded first-socle targets u,v, take
equal-degree multipliers `F_d,G_d` of degree `d`, mapping an ancestor of
graded degree `-(d+3)` to the two first-socle targets of degree `-3`.
Let `n>=3` be its top principal-part order. Assume at least one multiplier
has nonzero linear normal symbol, as in the linked actual-symbol
contraction argument. Its ancestor inequality follows from the top
section degree after removing the pure-power direction:

\[
7n-4d-5-e(n-1)\ge0
\iff (7-e)(n-1)\ge4d-2.
\]

This confirms the stated finite early-jet reduction under its checked BF,
normal-bundle, and linear-contraction inputs. It does not cover two
entirely thick equations or bound either equation degree.

## Evidence and scope

The general compression, arithmetic-genus determinant proof, order-one
application and early-jet bounds reuse their accepted independent source
reviews. The normal-quartic classification supplies the d/rho data; see
[Ishii--Nakayama, Main Theorem and rational types](https://www.jstage.jst.go.jp/article/jmath1948/56/3/56_3_941/_pdf).
Exact arithmetic and the cusp illustration are checked by
[verify_normal_rational_carrier_compression.py](../computations/verify_normal_rational_carrier_compression.py).
No new execution is needed for their unchanged formulas. The exact fixed-C0
normal bundle is proved in [the bisection argument](../supplements/GENUS_TWO_BISECTION_PROOF.md#2-the-characteristic-zero-normal-bundle).

These bounds do not enumerate surfaces, construct a numerical model as a
carrier, cancel arbitrary local class-group torsion, or cover a pair whose
two equations both have generic normal order at least two. For fixed-C0
quartic mates the later [full exclusion](quartic_carrier_proof.md) closes
that special case; the general compression and higher-degree necessary
bounds remain useful mathematics.
