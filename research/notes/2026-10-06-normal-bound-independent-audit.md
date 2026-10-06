# Independent audit of normal-carrier compression and the order-one degree bound

Date: 2026-10-06. Role: independent, adversarial proof audit. Scope: the
denominator-compression theorem, the determinant estimate for the remaining
normal quartic carriers, and (U4) in the uniform order-one note. No new
classification or coefficient search was performed.

**Audit verdict:** the three deductions are valid with their stated
hypotheses. No gap was found. The compression is conditional on the
existence of a mate and on rationality of the entire smooth resolution;
the determinant estimate uses the **minimal** resolution. The order-one
bound applies to the equation with nonzero generic first normal symbol.
These restrictions are essential and are not removed by this audit.

## 1. Documents and primary-source checks

The audited notes are:

- `2026-10-06-normal-rational-carrier-compression.md`;
- `2026-10-06-uniform-order-one-frontier.md`, subsection containing (U4);
- `2026-10-05-mumford-normal-bound.md`, including its proof rather than only
  the asserted inequality;
- `2026-10-05-normal-quartic-carriers.md`, for the classification inputs.

I checked the saved primary text of Ishii and Nakayama,
*Classification of normal quartic surfaces with irrational singularities*,
[author preprint](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1370.pdf)
and [published paper](https://www.jstage.jst.go.jp/article/jmath1948/56/3/56_3_941/_pdf).
The local convenience copy is
`/private/tmp/stci-normalquartic-rims1370.txt`.

The following precise source hypotheses were confirmed:

- Preprint p.7 defines a minimal desingularization by relative nefness of
  the canonical class, equivalently the absence of exceptional rational
  `(-1)` curves. It also states that for a Gorenstein surface the minimal
  resolution has an effective exceptional divisor `E` with
  `K_M ~ sigma^* K_S - E`.
- Proposition 1.4, p.9, identifies the surface constructed from a basic
  triplet as a normal quartic, identifies the morphism as its minimal
  desingularization, and identifies `E` as the exceptional anticanonical
  divisor.
- The Main Theorem, p.23, makes the constructions exhaustive.
- The rational types give `(rho(M),-E^2)=(12,2)` for B1 on p.14,
  `(11,1)` for B2 on p.17, `(11,1)` for B3 on p.19, and `(13,3)` for D
  on p.23. Lemma 3.2, p.24, also confirms the complete B1/B2/B3 list.

Thus the classification supplies `rho(M)=10+d`, `1<=d<=3`, and a
minimal resolution with integral effective exceptional `E`. The audit
does not replace the separately recorded exclusions of the ruled/K3
classes or the classical lower mate-degree exclusions.

## 2. Denominator compression: verified globally, not just numerically

Let `S` be a normal integral hypersurface of degree `a`, with smooth
rational projective resolution `sigma:M->S`, and let `C` have degree
`delta`. A degree-`b` mate gives an effective Cartier divisor `rC` with
`r delta=ab`. Put `H=sigma^*O_S(1)` and write the numerical pullback of
`C` as `c+Z`. Then `c+Z == (delta/a)H` in the numerical divisor space.

Let `n` clear the denominators of both `Z` and `delta/a`. The divisor

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

## 3. The determinant estimate includes nonreduced and singular `E`

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
divides `det A`. Combining with section 2 gives compressed mate bounds
`1536`, `4608`, and `13824` for `d=1`, `2`, and `3`, respectively.

No step assumed that `a_i=1`, that the components are smooth rational
curves, or that the dual graph is a reduced cusp cycle. The use of
arithmetic genus and the nonnegative integer multiplicities is exactly
what allows singular, reducible and nonreduced anticanonical divisors.
The estimate would not follow from an arbitrary further blowup, since
that could introduce exceptional `(-1)` curves and destroy relative
nefness; the source explicitly supplies the required minimal resolution.

The existing exact script was inspected and independently rerun:

    PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
      research/computations/verify_normal_rational_carrier_compression.py

It returned `PASS`, including the three numbers and the cusp-cycle
denominator-two illustration. This run checks arithmetic, not the
geometric descent or the classification. The geometry above is the
independent proof audit.

## 4. Audit of the order-one carrier bound (U4)

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

The proof in `2026-10-05-mumford-normal-bound.md` was checked directly:
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

## 5. Exact continuation scope

The audited finite reduction is: if a normal quartic carrier for `C0`
in characteristic zero has any mate, it has one of degree at most
`13824`, with the sharper value determined by `d`. Combined with the
recorded lower-degree exclusions, the degree interval is `6..13824`.
This is a bound on mate degree for that carrier class; it is neither an
enumeration of the remaining surfaces nor an STCI exclusion.

The independently verified (U4) is a necessary lower bound in the
order-one branch for arbitrary carrier degree. It supplies no upper
bound and does not cover a pair with both generic normal orders at least
two. The universal curve problem and the unrestricted characteristic-zero
rational-quartic problem remain open.
