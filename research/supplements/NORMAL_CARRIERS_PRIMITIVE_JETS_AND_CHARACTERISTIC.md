# Normal carriers, primitive structures, jets, and characteristic

Topical preservation of mathematical source material, including substantive failures and original audit qualifications. No theorem promotion.

---

## 2026-10-06-normal-bound-independent-audit

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


---

## 2026-10-06-normal-rational-carrier-compression

# Rational-resolution carriers: numerical denominator compression

Date: 2026-10-06. Status: proved conditional compression theorem and a
finite normal-quartic mate bound. The condition is that a mate exists on
the specified normal carrier. Numerical coincidence alone is not promoted
to a global construction on an unspecified surface.

## 1. Compression on a normal surface with rational resolution

Let `S⊂P^3` be an integral normal surface of degree `a`, and suppose its
smooth projective resolution `sigma:M→S` is rational. Let `C⊂S` be an
integral curve of degree `delta`, with strict transform `c`. Write
`H=sigma^*O_S(1)`. Suppose an ambient degree-`b` surface cuts out `C`
set-theoretically on `S`. Its divisor is `rC`, where `r delta=ab`.

Let `Cbar=c+Z` be the numerical pullback, characterized by orthogonality
to every exceptional curve. Pulling back the Cartier relation `rC~bH`
gives `Cbar≡(delta/a)H`.

Choose the least positive integer `n` which clears the coefficient
denominators of `Z` and of `delta/a`. Then

`D=n((delta/a)H-c-Z)`

is an integral divisor numerically equivalent to zero. A smooth rational
projective surface has torsion-free Picard group, with numerical
equivalence equal to linear equivalence. For example this follows on a
minimal rational model (`P^2` or a Hirzebruch surface), and each blowup
adds one free exceptional summand. Thus `D` is principal on `M`.

Push its principal divisor down to the normal surface `S`. The rational
function field is unchanged, and exceptional divisors disappear. Hence

`nC~(n delta/a)H` on `S`.

This is an actual Weil-divisor linear equivalence to a Cartier divisor,
not merely numerical equivalence. In particular `nC` is effective
Cartier, and its canonical section is a section of
`O_S(n delta/a)`. It lifts to a homogeneous ambient form, because the
restriction sequence and `H^1(P^3,O(t))=0` give surjectivity of
`H^0(P^3,O(n delta/a))→H^0(S,O_S(n delta/a))`. The lift supplies a mate
of degree `n delta/a` supported exactly on `C`.

This proves the **numerical-denominator compression theorem**. For
`a=delta=4`, its conclusion is simply `nC~nH`, with a mate of degree `n`.
Moreover any mate degree `b` clears the coefficients of `Z`: its Cartier
divisor pullback has integral exceptional coefficients. Thus `n|b`, and
`n` is the least mate degree for this fixed normal quartic carrier.

The proof uses rationality of the entire resolution. It cannot cancel a
torsion scalar in an arbitrary local class group. A cusp or elliptic
local Picard group may have further torsion in general, but under the
global mate hypothesis and rational-resolution condition the linear
equivalence above removes that possible inflation.

For `C0` in characteristic zero the known exclusions of degrees `(4,4)`
and `(4,5)`, together with the unique-quadric and all-cubic exclusions,
force this compressed degree to be at least six. The all-cubic theorem
also eliminates a reducible compressed mate having a cubic component.

## 2. Uniform bound for the remaining normal quartic carriers

The source classification and its hypotheses are recorded in
`research/notes/2026-10-05-normal-quartic-carriers.md`: a surviving normal
quartic carrier for a smooth rational quartic has rational resolution
with `K_M=-E`, where `E` is a nonzero effective exceptional divisor.
Ishii–Nakayama's exhaustive types give

| `d=-E^2` | Rational types | `rho(M)` |
|---:|---|---:|
| 1 | B2, B3 | 11 |
| 2 | B1 | 12 |
| 3 | D | 13 |

Let `E_1,...,E_r` be **all** exceptional prime curves and put
`A_ij=-E_i.E_j`, `b_i=A_ii=-E_i^2`, and `E=sum a_i E_i`, with
nonnegative integral `a_i`. The matrix `A` is positive definite. All
exceptional classes are independent and orthogonal to `H`, so
`r≤rho(M)-1=9+d`.

The resolution is minimal. Therefore `K_M.E_i≥0`: an exceptional curve
with negative canonical intersection would be a smooth rational
`(-1)` curve, contradicting minimality. Adjunction, including arithmetic
genus for a possibly singular exceptional prime curve, gives

`(A a)_i=K_M.E_i=b_i+2p_a(E_i)-2≥0`.

For `a_i=0`, one also has `K_M.E_i=-E.E_i≤0`, since distinct curves
have nonnegative intersection. Thus the displayed term is zero; `b_i>0`
forces `p_a(E_i)=0,b_i=2`. Such a curve is disjoint from the support of
`E`. In particular every vertex with `b_i>2` has `a_i≥1`.

Multiplying the displayed adjunction equation by `a_i` and summing gives

`d=a^T A a=sum a_i(b_i+2p_a(E_i)-2)`.

Every summand is nonnegative. Each vertex with `b_i>2` contributes at
least `b_i-2`. Consequently

`sum (b_i-2)_+≤d`.

For every positive integer `b`,
`b≤2(3/2)^((b-2)_+)`. Equality holds for `b=2,3`, and the inequality
then follows successively since `(b+1)/b≤3/2`. Hadamard's determinant
inequality now gives

`det A≤prod b_i≤2^r(3/2)^d≤2^(9+d)(3/2)^d=512·3^d`.

The exceptional correction has coefficient vector `A^(-1)m`, where
`m_i=c.E_i` are integers. By the adjugate formula, its denominator `n`
divides `det A`. Section 1 turns that denominator into an actual mate.
Therefore the least mate degree for the fixed carrier satisfies

| `d` | Uniform compressed mate bound |
|---:|---:|
| 1 | `n≤1536` |
| 2 | `n≤4608` |
| 3 | `n≤13824` |

**Bounded conclusion.** Every hypothetical normal quartic carrier for
`C0` in characteristic zero admits a mate of degree between 6 and 13824,
with the sharper row bound determined by `-E^2`. The simple-elliptic
case is already excluded in the companion note. The bound also covers
singular, reducible and nonreduced anticanonical `E`; it does not require
a reduced cusp cycle, a first-normal ratio assumption, or any prediction
of the precise local Cartier index before a mate is known.

This supplies a finite degree reduction for **normal quartic carriers**.
It does not bound mates on nonnormal quartic carriers or minimum carrier
degrees above four. It is a large theoretical bound, not an enumeration
of all coefficients or a practical exhaustive search already performed.

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

Exact companion:
`research/computations/verify_normal_rational_carrier_compression.py`.
It checks this matrix, the correction denominator and the three uniform
determinant bounds. It returned `PASS` under
`/private/tmp/stci-cas-venv/bin/python`; output is saved in
`research/computations/normal_rational_carrier_compression_2026-10-06.json`.
Its output does not verify the cited classification
or the global Picard and divisor arguments, which are proved above.


---

## 2026-10-06-order-one-jet-discrepancy-framework

# Order-one jet discrepancy for quartic carriers

Date: 2026-10-06

Base audited commit: fa98d696da36c6a362afaf27d40cc0867fe9aa12 (main).

Status: structural research note. Statements are labelled individually. This note does **not** prove that the rational quartic is not an STCI.

## 0. Scope and audited starting point

Work in characteristic zero on the fixed smooth monomial rational quartic
\[
C=[s^4:s^3t:st^3:t^4]\subset \mathbf P^3,
\]
with unique smooth quadric \(Q\simeq\mathbf P^1\times\mathbf P^1\). The audited order-one setup has
\[
N_C^*\simeq O_C(-7)^2\twoheadrightarrow L\simeq O_C(e-7),\qquad e=0,1,2
\]
for quartic carriers. The canonical audited-state file controls older notes.

The audited e=2 result is stronger than the older P-044-slice formulation: the universal fourth-extension obstruction has reduced zero locus
\[
b_0=-2a_1,\qquad b_1=-2a_2,
\]
and on this whole resultant-open locus
\[
H^0(I_{C_3}(4))=H^0(I_{C_4}(4))=T\,H^0(O_{\mathbf P^3}(1)).
\]
This is certified by the universal primitive-quadruple verifier and independently reconstructed by the quartic-factor audit. The dx=1 P-044 saturation certificate is now closed, but it is not needed for the global e=2 carrier exclusion.

## A. Intrinsic setup

### A.1 Successive condition maps

Let \(C=C_1\subset C_2\subset\cdots\subset C_m\) be primitive with conormal line \(L\), so \(I_{C_j}/I_{C_{j+1}}\simeq L^j\). For degree \(a\), put
\[
V_j(a)=H^0(I_{C_j}(a)),\qquad W_j(a)=H^0(L^j(a)),
\]
and let \(\rho_j(a):V_j(a)\to W_j(a)\) be restriction.

**PROVED (formal).** Define
\[
\eta_j(a)=\dim W_j(a)-\operatorname{rank}\rho_j(a)
\]
(the target shortfall) and
\[
\delta_j(a)=\min\{\dim V_j(a),\dim W_j(a)\}-\operatorname{rank}\rho_j(a)\ge0
\]
(the intrinsic maximal-rank defect). Then
\[
\dim V_{j+1}(a)=\dim V_j(a)-\dim W_j(a)+\eta_j(a).
\]
Thus numerical budget and genuine dependence are separated. For quasiprimitive structures with saturated pieces \(E_j=L^j(D_j)\), use \(W_j(a)=H^0(E_j(a))\); the BF divisors \(D_j\) alter the targets and must not be conflated with rank defects.

### A.2 Quadric comparison divisor

The conormal sequence for \(C\subset Q\subset\mathbf P^3\) is
\[
0\to O_C(-8)\to N_C^*\to O_C(-6)\to0.
\]
Let \(M=\ker(N_C^*\twoheadrightarrow L)\). Since \(\det N_C^*=O(-14)\),
\[
M\simeq O_C(-e-7).
\]
The composite \(O_C(-8)\to N_C^*\to L=O_C(e-7)\) is a section \(r\in H^0(O_C(e+1))\). Let \(R=Z(r)\).

**PROVED.** The induced map \(M\to O_C(-6)\) is multiplication by the same section up to scalar. Hence
\[
M\simeq O_C(-6)(-R),\qquad \deg R=e+1.
\]

### A.3 First quartic source

Twisting by \(O_C(4)=O_C(16)\) gives
\[
M(4)=O_C(9-e)\xrightarrow{\cdot r}O_C(10).
\]
After restricting a quartic to \(Q\) and removing \(C\), its residual lies in \(H^0(O_Q(1,3))\), restricting to \(O_C(10)\). Define
\[
K_R=\{h\in H^0(O_C(9-e)):rh\text{ extends to }H^0(O_Q(1,3))\}.
\]

**PROVED.**
\[
K_R\simeq H^0(Q,I_{R/Q}(1,3)).
\]
If \(\operatorname{ev}_R:H^0(O_Q(1,3))\to H^0(O_R(1,3))\), define
\[
\epsilon_Q(R)=\ell(R)-\operatorname{rank}(\operatorname{ev}_R).
\]
Then
\[
\dim K_R=7-e+\epsilon_Q(R).
\]

**PROVED.** For e=0 and e=1, \(\epsilon_Q(R)=0\) for every possible \(R\): \(O_Q(1,3)\) separates every length-one and length-two subscheme. Thus
\[
\dim K_R=7\ (e=0),\qquad \dim K_R=6\ (e=1).
\]
For e=2, length-three schemes can fail to impose three independent conditions. The audited ruling-fiber case has \(\epsilon_Q(R)=1\), hence \(\dim K_R=6\). The first source rank jump is therefore genuinely an e=2 phenomenon.

### A.4 The second primitive quartic condition localizes on 2R

Assume the primitive triple \(C_3\) exists. Then
\[
\rho_2:H^0(I_{C_2}(4))\to H^0(L^2(4))=H^0(O_C(2e+2)).
\]
The quadric square satisfies \(\rho_2(Q^2)=r^2\), up to normalization. Quotienting gives
\[
\bar\rho_2:K_R\to H^0(O_C(2e+2))/\langle r^2\rangle
\simeq H^0(O_{2R}(2e+2)).
\]

**PROVED.** Define
\[
\delta_2^Q(R,C_3)=\min\{\dim K_R,2e+2\}-\operatorname{rank}\bar\rho_2.
\]
For e=0,1,2 the generic source/target sizes are
\[
(7,2),\qquad(6,4),\qquad(5,6).
\]
Only e=2 is generically overdetermined at this stage.

## B. e=2 reconstruction

For e=2 write the quotient by binary quadratics \(A,B\). The comparison section is \(r=A+zB/2\). The exact universal fourth-obstruction locus is
\[
b_0=-2a_1,\qquad b_1=-2a_2,
\]
and on it
\[
2r=2A+zB=2a_0+b_2z^3.
\]
Under the standard \(C\subset Q\) identification, the relevant ruling coordinate restricts as \(z^3\).

**PROVED.** Every basepoint-free e=2 quotient extending to the canonical primitive quadruple has
\[
R=C\cap F
\]
for a ruling fiber \(F\subset Q\). Thus the fourth-extension condition itself forces the first quartic source to jump from dimension 5 to 6. This is the intrinsic content behind the old P-045 ruling observation, now on the entire universal fourth-obstruction locus.

**EXACT COMPUTATIONAL CERTIFICATE.** On this locus both \(K_R\) and the finite target of \(\bar\rho_2\) have dimension six, but the audited universal contact matrix has rank exactly three everywhere. Two explicit 3x3 minors, \(-a_0^8\) and \(-b_2^8/256\), cover the parameter space, while all 4x4 minors vanish identically. Hence
\[
\operatorname{rank}\bar\rho_2=3,\qquad \delta_2^Q=3.
\]
In the seven-dimensional ambient pre-contact space (six \(K_R\) directions plus \(Q^2\)), the kernel is four-dimensional and
\[
\boxed{H^0(I_{C_3}(4))=T\,H^0(O_{\mathbf P^3}(1)).}
\]

**OPEN CONCEPTUAL STEP.** The ruling condition explains the source jump. The further rank-three collapse is stronger: three of six finite \(2R\) conditions become dependent. The exact matrix proves this universally, but a coordinate-free factorization of \(\bar\rho_2\) through a natural rank-three space attached to the ruling and extension class is still missing.

**PROVED.** BF duality forces the canonical fourth layer to be primitive for the e=2 branches of (4,7) and (4,8). Hence every defining quartic is \(T\ell\). For any mate \(G\), \(V(\ell,G)\) contributes an extra projective curve (or the whole plane), so these e=2 branches are excluded.

## C. e=0 analysis

Here \(L=O(-7)\), \(M=O(-7)\), and \(R\) has length one.

The embedded primitive-triple obstruction lies in
\[
H^1(\operatorname{Hom}(M,L^2))=H^1(O_C(-7)),
\]
of dimension six.

**PROVED (standard primitive-extension obstruction calculation).** Unlike e=2, a primitive double of direction e=0 does not automatically extend to a triple. If it extends, uniqueness follows from \(H^0(O(-7))=0\). This is compatible with P-010: the defect-free primitive e=0 triple is globally excluded, so positive \(D_2\) is essential in a quasiprimitive carrier filtration.

**PROVED.** Every length-one \(R\) imposes one independent condition on \(|O_Q(1,3)|\), so \(\dim K_R=7\). If a primitive triple existed,
\[
\bar\rho_2:K_R\;(\dim7)\to H^0(O_{2R}(2))\;(\dim2).
\]
Maximal rank would still leave a five-dimensional kernel.

**PROVED NEGATIVE STRUCTURAL RESULT.** The e=2 overdetermined-jet mechanism cannot extend verbatim to e=0. The hard geometry moves to triple existence and, for actual quasiprimitive carriers, to the defect divisor \(D_2\).

**PROVED CONNECTION TO MF6.** MF6 gives \(\deg D_2\ge3\) for e=0 saturated multiplicity-six lci/Gorenstein thickenings and excludes the nonregular (3,6) branch. The surviving (4,5) MF6 incidence lives in a modified target \(L^2(D_2)\), not the primitive target \(L^2\).

**OPEN.** Recast the MF6 type-(4,5) matrix as the quasiprimitive analogue of \(\bar\rho_2\) and identify its exceptional high-gcd locus geometrically.

## D. e=1 analysis

Here \(L=O(-6)\), \(M=O(-8)\), and \(R\) has length two.

\[
H^1(\operatorname{Hom}(M,L^2))=H^1(O_C(-4))
\]
has dimension three, while \(H^0(O(-4))=0\).

**PROVED.** Triple existence is a three-coordinate obstruction and, when it exists, the embedded primitive triple is unique. Thus e=1 differs fundamentally from e=2 before quartic second-jet dependence is considered.

**PROVED.** Every length-two subscheme imposes two independent conditions on \(|O_Q(1,3)|\). Hence \(\dim K_R=6\) for every e=1 quotient direction; there is no e=2-style source jump. For an existing primitive triple,
\[
\bar\rho_2:K_R\;(\dim6)\to H^0(O_{2R}(4))\;(\dim4).
\]
Maximal rank leaves a two-dimensional quartic kernel, so quartic survival requires no rank defect.

**OPEN.** Determine the rank of \(\bar\rho_2\) on the actual three-obstruction-zero locus of e=1 primitive triples, and determine whether that locus forces a recognizable incidence condition on \(R\) or on the second-order extension class.

The audited BF/MF6 e=1 possibilities \((d_2,d_3)=(0,4),(1,3),(2,2)\) should be separated into: first solve the triple-extension obstruction in \(H^1(O(-4))\); then study the finite \(2R\) evaluation map, modified to \(L^2(D_2)\) when \(D_2>0\).

## E. General principle

**PROVED FRAMEWORK.** For a fixed filtration and carrier degree, the signed budget
\[
B_j=\dim V_j-\dim W_j
\]
and maximal-rank defect
\[
\delta_j=\min(\dim V_j,\dim W_j)-\operatorname{rank}\rho_j
\]
separate numerical over/underdetermination from genuine dependence. Rank-defect loci are determinantal loci of families of restriction maps.

**PROVED.** For e=0,1,2, the first two primitive quartic stages are controlled by
\[
R\in |O_C(e+1)|,\qquad
K_R=H^0(I_{R/Q}(1,3)),\qquad
\bar\rho_2:K_R\to H^0(O_{2R}(2e+2)).
\]
The source discrepancy is exactly the failure of \(R\) to impose independent conditions on \(|O_Q(1,3)|\). It vanishes identically for e=0,1 and can occur for e=2. On the e=2 fourth-extension locus, extension compatibility forces \(R\) to be a ruling-fiber divisor and the second map has certified rank defect three.

**CONJECTURE.** On the e=2 fourth-extension locus, \(\bar\rho_2\) factors coordinate-freely through a natural rank-three space attached to the ruling fiber and extension class. Such a factorization would explain both rank three and the cubic-times-linear kernel.

**PROVED NEGATIVE RESULT.** There is no uniform theorem saying quartic survival for e=0,1,2 requires jet-rank degeneracy. It is false numerically for e=0 and e=1. A correct uniform theory must include extension-existence obstructions and BF defect divisors, not only containment-map ranks.

## F. Connections

**Local cohomology — PROVED CONCEPTUAL CONNECTION, not an identification theorem.** The local-cohomology quartic problem is also determinantal: an ancestor \(a\) defines a multiplication matrix \(L(a)\), and multiplier existence is \(\operatorname{rank}L(a)=\operatorname{rank}N(a)+2\). Exact local-cohomology work independently finds exceptional degree-two directions aligned with the e=2 fourth-zero family. A canonical identification with \(\bar\rho_2\) is **OPEN**.

**MF6 — PROVED CONCEPTUAL CONNECTION.** MF6 defect divisors record failure of the primitive associated graded algebra to remain pure powers of \(L\). They modify jet targets from \(L^j\) to \(L^j(D_j)\). MF6 pole/incidence calculations are a quasiprimitive refinement of the jet-budget framework, but the pole divisor is not itself the rank defect.

**P-044/P-045 — PROVED.** The old P-045 ruling condition is the dx=1 shadow of the universal e=2 statement that fourth-extension compatibility forces \(R\) to be a ruling-fiber divisor. The exact dx=1 saturation certificate closes that slice, but the universal primitive-fourth certificate is the stronger carrier input.

**Deformation/extension theory — PROVED.** The obstruction groups
\[
H^1(\operatorname{Hom}(M,L^2))=H^1(O(3e-7))
\]
explain why e=0,1,2 differ before any quartic rank count: their dimensions are 6,3,0.

## G. Single highest-value next attack

**OPEN / RECOMMENDED LEMMA.** Construct the e=1 triple-extension obstruction intrinsically as a map from the quotient pencil
\[
N_C^*\twoheadrightarrow O(-6)
\]
to
\[
H^1(O(-4))\simeq k^3,
\]
and determine its reduced zero locus together with
\[
\bar\rho_2:H^0(I_{R/Q}(1,3))\to H^0(O_{2R}(4)).
\]

The target is a geometric description of the obstruction-zero locus, followed by maximal-rank/rank-drop analysis of \(\bar\rho_2\) on its geometric strata. This directly tests whether e=2 has a genuine e=1 analogue while respecting the fact that e=1 is not dimensionally overdetermined.

A secondary target is the coordinate-free rank-three factorization of the e=2 map.

## Reproducibility / provenance

No new random-specialization computation is promoted here. New statements are deductions from exact sequences, line-bundle degrees, separation properties of \(O_Q(1,3)\), and already-audited universal e=2 certificates. Existing theorem-level computational inputs remain the universal primitive-quadruple verifier, the independent quartic-factor audit, the dx=1 saturation certificate, and the exact local-cohomology incidence certificates cited by the audited state.

No statement here upgrades an OPEN local-cohomology, MF6, e=0, or e=1 locus to an exclusion.


## H. Literature audit and novelty boundary

Literature search performed 2026-10-06 before continuing the e=1 calculation.

### H.1 Bănică--Forster: extension theory is established machinery

C. Bănică and O. Forster, *Multiplicity Structures on Space Curves*, Contemp. Math. 58 (1986), 47--64, is the primary antecedent for the embedded primitive/quasiprimitive filtration used here.

Their Proposition 2.4 states, in the present notation, that extending a primitive multiplicity-k structure \(Z'\) of type \(L\) to multiplicity \(k+1\) is equivalent to choosing a retraction of
\[
0\to L^k\to \nu_{Z'}|_C\to M\to0,
\qquad
M=\ker(\nu_C\twoheadrightarrow L).
\]
Their Corollary 2.5 identifies the splitting obstruction/torsor groups as
\[
H^1(\det(\nu_C)^*\otimes L^{k+1}),\qquad
H^0(\det(\nu_C)^*\otimes L^{k+1}).
\]
For the rational quartic, \(\det\nu_C=O(-14)\), so for double-to-triple extension (\(k=2\)) this is exactly
\[
H^1(O(14)\otimes O(3e-21))=H^1(O(3e-7)).
\]

**LITERATURE-ESTABLISHED, NOT NEW.** The obstruction groups of dimensions \(6,3,0\) for e=0,1,2 are a direct specialization of Bănică--Forster. Likewise their Section 3 already gives the CM filtration, quasiprimitive line bundles \(L_j=L^j(D_j)\), superadditivity \(D_i+D_j\le D_{i+j}\), and the interpretation of later quasiprimitive extensions as meromorphic retractions. These should be cited as the conceptual source of the BF language used throughout STCI.

Source: C. Bănică--O. Forster, *Multiplicity Structures on Space Curves*, Contemp. Math. 58 (1986), 47--64; electronic copy on O. Forster's LMU page.

### H.2 Drézet: modern intrinsic parametrization

Jean-Marc Drézet, *Paramétrisation des courbes multiples primitives*, Adv. Geom. 7 (2007), 559--612, develops primitive curves of arbitrary multiplicity by gluing \(U_i\times\operatorname{Spec}\mathbf C[t]/(t^n)\) and nonabelian \(H^1\). His later survey and papers develop extension, deformation, and moduli theory further.

**LITERATURE-ESTABLISHED, NOT NEW.** Treating primitive multiple curves intrinsically via their canonical filtration and associated line bundle, rather than by ambient coordinates, is standard. Any eventual general theorem should be phrased compatibly with this literature rather than advertised as a new theory of primitive multiple curves.

Relevant sources:
- J.-M. Drézet, *Paramétrisation des courbes multiples primitives*, Adv. Geom. 7 (2007), 559--612, arXiv:math/0605726.
- J.-M. Drézet, *Primitive multiple schemes*, Eur. J. Math. 7 (2021), 985--1045, arXiv:2004.04921.
- J.-M. Drézet, *Primitive multiple curves: classification, deformations and moduli spaces of sheaves* (survey, 2013).

### H.3 Rational-quartic STCI literature

The rational quartic is a classical unresolved characteristic-zero STCI problem. Relevant antecedents found in the search include:

- P. C. Craighero--R. Gattazzo (1986): the monomial rational quartic is not the set-theoretic intersection of two quartic surfaces.
- P. C. Craighero--R. Gattazzo (1989): no smooth rational quartic is an STCI on a cubic surface.
- D. B. Jaffe, *Applications of iterated curve blow-up to set theoretic complete intersections in P3*, J. reine angew. Math. 464 (1995), 1--46: finite numerical lists of possible degree pairs under the stated hypotheses; for \((d,g)=(4,0)\) the list includes \((4,7)\).
- Ph. Ellia, *Primitive set-theoretic complete intersections* (arXiv:1409.3801): numerical restrictions for primitive STCI structures. Corollary 16 leaves ten rational-quartic numerical cases, including \((a,b,l)=(4,7,5)\), and explicitly describes its improvement over Jaffe as numerical rather than a full rational-quartic exclusion.

**LITERATURE CHECKED / NO PRIOR IDENTIFICATION FOUND.** In the sources located in this search, no formulation was found of the STCI quartic-carrier problem as the pair
\[
K_R=H^0(I_{R/Q}(1,3)),\qquad
\bar\rho_2:K_R\to H^0(O_{2R}(2e+2)),
\]
nor a derivation of the e=2 cubic-times-linear factorization from a determinantal rank collapse on the fourth-extension locus. Absence from this search is not a proof of novelty; a stronger novelty claim requires a targeted bibliography/citation-chain search.

### H.4 Ropes/ribbons literature

The ribbon/rope literature (Bayer--Eisenbud for ribbons; later Gallego--González--Purnaprajna and Drézet for ropes/primitive multiple curves and deformations) confirms that embedded multiple structures, conormal bundles, and deformation maps are mature subjects.

**NOVELTY BOUNDARY.** The potentially project-specific contribution is therefore not:
1. the canonical filtration;
2. conormal quotient \(L\);
3. extension obstruction groups;
4. defect divisors for quasiprimitive structures; or
5. determinantal loci in the abstract.

The candidate new ingredient is their **specific coupling for the rational quartic carrier problem**:
\[
\text{BF extension data}
\longrightarrow R\subset C\subset Q
\longrightarrow K_R
\longrightarrow \text{finite jet evaluation on }2R
\longrightarrow \text{ambient factorization}.
\]
The universal e=2 computation supplies a nontrivial instance where extension compatibility forces a special incidence locus for \(R\), and that incidence is followed by an additional rank-three collapse of the ambient quartic jet map.

### H.5 Revised status of the framework

**PROVED + LITERATURE-ALIGNED.** The two-layer organization
\[
\text{existence/splitting of the multiple structure}
\quad+\quad
\text{rank of ambient containment maps}
\]
is the correct framework, but the first layer is Bănică--Forster/Drézet theory.

**PROJECT-SPECIFIC PROVED RESULT.** For the rational quartic and quartic carriers, the quadric comparison converts the ambient first-symbol problem into evaluation of \(O_Q(1,3)\) on \(R\), and the next primitive containment condition into a finite map on \(2R\). The e=2 fourth-extension locus forces \(R\) to be a ruling divisor and has exact ambient rank three.

**OPEN NOVELTY QUESTION.** Determine whether this \(R/2R\) ambient-carrier reduction, or an equivalent construction, already occurs in the older literature on contact of surfaces along curves (notably Gallarati), infinitesimal neighborhoods, or Rees/principal-parts methods. Search should continue before publication-level novelty claims.

## I. Revised next attack after literature audit

The highest-value mathematical calculation remains e=1, but it should now be posed explicitly as a **Bănică--Forster splitting problem plus ambient carrier map**, not as invention of a new obstruction theory.

Let \(L=O(-6)\), \(M=O(-8)\). Starting from the Ferrand double \(C_2\), compute the BF extension
\[
0\to L^2=O(-12)\to \nu_{C_2}|_C\to M=O(-8)\to0.
\]
Its class lies in
\[
\operatorname{Ext}^1(M,L^2)=H^1(O(-4)).
\]
The next exact target is:

1. express this extension class intrinsically in terms of the quotient \(N_C^*\twoheadrightarrow O(-6)\) and comparison divisor \(R\in|O_C(2)|\);
2. determine its reduced splitting locus in the resultant-open quotient parameter space;
3. only on that locus, form the ambient map
   \[
   \bar\rho_2:H^0(I_{R/Q}(1,3))\to H^0(O_{2R}(4));
   \]
4. determine whether its rank-drop locus has a geometric incidence description.

This cleanly separates standard extension theory from the genuinely unresolved ambient-STCI geometry.


## J. Exact e=1 primitive-triple obstruction

This section carries out the first revised target from Section I for the fixed quartic
\[
C_0=[s^4:s^3t:st^3:t^4].
\]

### J.1 Setup

For \(e=1\),
\[
L=O(-6),\qquad M=O(-8),
\]
and every Ferrand double is specified in the fixed split conormal frame by
\[
A=a_0+a_1z,\qquad B=b_0+b_1z,
\]
with projective basepoint-free condition
\[
\Delta=a_0b_1-a_1b_0\ne0.
\]

By Bănică--Forster Proposition 2.4, extension to a primitive triple is equivalent to splitting
\[
0\to L^2=O(-12)\to \nu_{C_2}|_C\to M=O(-8)\to0.
\]
The extension class lies in
\[
\operatorname{Ext}^1(M,L^2)=H^1(O(-4)).
\]

**LITERATURE STATUS.** The splitting criterion and obstruction group are standard Bănică--Forster theory. The explicit specialization below to the fixed embedded rational quartic and its quotient pencil was not found in the targeted literature search; it should presently be treated as a project calculation, not a publication-level novelty claim.

### J.2 Moving-coordinate cocycle

Use the same exact embedded chart transition as in the audited e=2 computation, but now reverse the binary *linear* forms by
\[
A^\vee(w)=wA(1/w),\qquad B^\vee(w)=wB(1/w).
\]
For \(m=Bu-Av\), which has line type \(M=O(-8)\), the quadratic coefficient of the opposite-chart equation gives the Cech cocycle
\[
h_2=-\frac{2A+zB}{8z^5}
\left(12A^2+3z^2B^2+4z^2(A'B-AB')\right).
\]
The same formal expression appeared in the e=2 calculation; the different line type changes which Laurent coefficients survive in cohomology.

For \(H^1(O(-4))\), the basis classes are \(z^{-1},z^{-2},z^{-3}\). Up to a common nonzero scalar, the three obstruction coordinates are
\[
\boxed{
\begin{aligned}
c_1={}&-b_1(2a_0b_1+12a_1^2+16a_1b_0+9b_0^2),\\
c_2={}&-(2a_1+b_0)(8a_0b_1+12a_1^2+4a_1b_0+3b_0^2),\\
c_3={}&-2a_0(2a_0b_1+36a_1^2+16a_1b_0+3b_0^2).
\end{aligned}}
\]

**PROVED COMPUTATIONALLY/FORMALLY.** These are the exact Cech coordinates obtained from the moving-coordinate transition; no sampling is used.

### J.3 Exact zero locus on the resultant-open quotient space

Localize at \(\Delta\) by adjoining \(t\Delta-1\). An exact Groebner calculation gives, among the localized consequences,
\[
a_0(2a_1+b_0)=b_1(2a_1+b_0)=0,
\]
\[
a_0(a_0b_1+2b_0^2)=b_1(a_0b_1+2b_0^2)=0,
\]
and
\[
a_0(3b_0^2t+2)=b_1(3b_0^2t+2)=0.
\]

Hence the resultant-open zero locus has the following exhaustive set-theoretic decomposition.

#### Main component

If \((a_0,b_1)\ne(0,0)\), then
\[
\boxed{b_0=-2a_1,\qquad a_0b_1=-8a_1^2.}
\]
Here
\[
\Delta=-6a_1^2\ne0,
\]
so \(a_1,a_0,b_1\) are all nonzero. Projectively this is a one-dimensional rational locus.

The quadric-comparison section is
\[
r=A+\frac z2B
=a_0+\frac{b_1}{2}z^2
=a_0-\frac{4a_1^2}{a_0}z^2.
\]
Thus its degree-two divisor \(R\) is a symmetric pair in the chosen affine coordinate. Whether this admits a coordinate-free incidence interpretation is OPEN.

#### Boundary directions

If \(a_0=b_1=0\), put \(r_0=b_0/a_1\). Basepoint-freeness says \(r_0\ne0\), and the remaining obstruction is
\[
(r_0+2)(3r_0^2+4r_0+12)=0.
\]
Thus there are three additional projective quotient directions over an algebraically closed characteristic-zero field:
\[
\boxed{r_0=-2,\quad 3r_0^2+4r_0+12=0.}
\]

At \(r_0=-2\), the comparison section \(A+\frac z2B\) vanishes identically. This is a genuinely exceptional configuration: the primitive conormal kernel \(M=O(-8)\) coincides with the quadric conormal subline \(O(-8)\subset N_C^*\). The divisor \(R\) formalism must therefore be treated separately there; one must not write a length-two \(R=Z(r)\).

At the two quadratic-root directions, the comparison section is a nonzero scalar multiple of \(z\) as an \(O(2)\)-section, so its homogeneous zero divisor consists of the two coordinate boundary points \(0,\infty\).

**PROVED.** The above main component plus three boundary points is the complete reduced/set-theoretic primitive-triple locus on \(\Delta\ne0\), subject to the exact transition conventions already audited for the fixed curve.

Reproduction:
\[
\texttt{python research/computations/verify\_e1\_triple\_obstruction.py}.
\]

### J.4 Consequence for the jet-budget program

The e=1 extension-existence condition is therefore neither vacuous nor a generic three-independent-equation cut. It has a positive-dimensional exceptional component. This reinforces the revised framework:

\[
\text{BF splitting degeneracy}
\quad\text{first, then}\quad
\text{ambient quartic jet rank}.
\]

On the main component, \(R\) has length two and
\[
K_R=H^0(I_{R/Q}(1,3))
\]
has dimension six. The next concrete problem is to compute
\[
\bar\rho_2:K_R\to H^0(O_{2R}(4))
\]
along the one-dimensional main component and the two nonzero-comparison boundary directions. The \(r\equiv0\) boundary direction requires a separate formulation because the \(R/2R\) reduction degenerates.

### J.5 Literature check specific to this calculation

A targeted search was made for explicit primitive-triple formulas for embedded rational quartics, Ferrand doubles extended to triples, and formulas for the Bănică--Forster splitting class. The sources located continue to use BF/Ferrand as the general mechanism; no explicit formula matching the three \(c_i\) above was found.

Ellia's primitive-STCI work uses numerical consequences of primitive multiple structures rather than this quotient-pencil splitting locus. Modern papers using quasi-primitive extensions likewise cite BF as the construction machinery. Therefore the safe current classification is:

- **standard:** Ferrand double construction, BF splitting criterion, obstruction group \(H^1(O(-4))\);
- **project-specific exact calculation:** the three displayed \(c_i\) and their resultant-open zero-locus decomposition;
- **unknown novelty:** whether an equivalent classification occurs in older specialized literature not indexed by the searches used here.

Before any external write-up, search citation chains around Bănică--Forster, Ferrand, and older work on multiple/contact structures rather than claiming the explicit locus is new.


## K. Exact e=1 quartic contact on the primitive-triple locus

The e=1 BF splitting locus from Section J can now be tested against the ambient quartic carrier map.

### K.1 Full quartic-through-double source

The ambient quartic ideal of \(C_0\) has dimension 18. For a quotient
\[
A=a_0+a_1z,\qquad B=b_0+b_1z,
\]
impose that the first normal symbol be \(h(B,-A)\), with \(h\in H^0(O(8))\). Exact linear algebra in the 35 quartic monomials gives, away from the exceptional comparison-zero direction below,
\[
h^0(I_{C_2}(4))=7.
\]
This agrees with the intrinsic decomposition
\[
6=\dim K_R,\qquad 7=6+\dim\langle Q^2\rangle.
\]

For a lift \(F\) with symbol \(h(B,-A)\), its restriction to the canonical primitive triple is the quadratic Taylor coefficient
\[
[F(A\epsilon,B\epsilon)]_{\epsilon^2}-h\gamma,
\]
where \(\gamma\) is the nonnegative-chart correction obtained from the BF quadratic cocycle.

### K.2 Main one-dimensional triple component: no jet-rank defect

Parameterize the main component projectively by
\[
a_0=1,\qquad a_1=t,\qquad b_0=-2t,\qquad b_1=-8t^2.
\]
The resultant is
\[
\Delta=-6t^2,
\]
so every admissible point has \(t\ne0\).

The full second-order contact matrix has rank exactly five for every \(t\ne0\). A single covering \(5\times5\) minor is
\[
\boxed{-589824\,t^{16}},
\]
so there is no specialization gap on the component.

Therefore
\[
\boxed{h^0(I_{C_3}(4))=2}
\]
at every point of the main e=1 primitive-triple family.

Equivalently, after quotienting the universal \(Q^2\) source direction against \(r^2\), the finite map
\[
\bar\rho_2:K_R\to H^0(O_{2R}(4))
\]
has maximal rank four. Thus
\[
\boxed{\delta_2^Q=0}
\]
uniformly on the main component.

**PROVED.** The e=2 carrier mechanism does not recur here: BF splitting imposes a special one-dimensional family of quotients, but it does not force a second ambient jet-rank defect.

### K.3 Two nonzero-comparison isolated directions

At the two isolated directions
\[
a_0=b_1=0,\qquad
3(b_0/a_1)^2+4(b_0/a_1)+12=0,
\]
the quartic-through-double source has dimension seven and the full contact map again has rank five. Hence
\[
\boxed{h^0(I_{C_3}(4))=2}
\]
there as well.

So every e=1 primitive triple with nonzero quadric-comparison section has exactly the expected two-dimensional quartic carrier space.

### K.4 The comparison-zero point is qualitatively different

At the remaining isolated direction, scale to
\[
A=z,\qquad B=-2.
\]
Then
\[
A+\frac z2B=0.
\]
Hence the primitive conormal kernel \(M=O(-8)\) is exactly the quadric conormal subline
\[
O_C(-8)\subset N_C^*.
\]

The first-symbol source jumps:
\[
\boxed{h^0(I_{C_2}(4))=10}.
\]
The BF quadratic cocycle vanishes identically, so the canonical triple has no quadratic gluing correction in the fixed charts. Moreover the quadric equation has chart expression
\[
Q=u+\frac z2v,
\]
and under the triple parameterization
\[
u=z\epsilon,\qquad v=-2\epsilon
\]
it vanishes identically.

Therefore the canonical primitive triple is contained in the smooth quadric:
\[
\boxed{C_3\subset Q}.
\]

Consequently
\[
Q\cdot H^0(O_{\mathbf P^3}(2))
\subseteq H^0(I_{C_3}(4)).
\]
Both sides have dimension ten, so
\[
\boxed{
H^0(I_{C_3}(4))
=
Q\cdot H^0(O_{\mathbf P^3}(2)).
}
\]

**PROVED.** This exceptional e=1 triple has maximal carrier freedom only because the entire triple lies on the quadric; every quartic carrier factors by \(Q\).

For an STCI presentation with a quartic equation, this is immediately dangerous in exactly the same elementary projective sense as the e=2 cubic-times-linear factorization: a defining quartic \(QH_2\) carries the entire surface component \(Q=0\), and intersection with any positive-degree mate contains a curve on \(Q\), not merely the nonplanar quartic support. Thus this direction cannot supply a genuine quartic equation in an STCI pair supported exactly on \(C_0\).

### K.5 Structural conclusion for e=1

The primitive e=1 locus exhibits two distinct mechanisms:

1. **nonzero comparison section:** BF splitting is exceptional, but ambient quartic contact is maximal rank and leaves exactly a two-dimensional quartic kernel;
2. **zero comparison section:** the primitive structure aligns with the quadric itself, the source jumps to dimension ten, and every quartic factors through \(Q\).

This strengthens the negative conclusion from the jet-budget framework. Rank defect is not the general source of carrier survival. For e=1, the generic primitive-triple survivor locus has **zero** ambient discrepancy:
\[
\delta_2^Q=0.
\]
The remaining two quartics must therefore be understood geometrically rather than eliminated by dimension count.

Reproduction:
\[
\texttt{python research/computations/verify\_e1\_quartic\_contact.py}.
\]

## L. Next e=1 target

The highest-value next question is now:

> On the nonzero-comparison e=1 primitive-triple locus, what are the two quartics in \(H^0(I_{C_3}(4))\), and what is their common residual geometry?

Possible outcomes are sharply distinguishable:

- the two-dimensional pencil has a fixed factor or fixed residual curve, giving an immediate carrier obstruction;
- the pencil has no fixed factor but a forced base locus beyond \(C\), which may still obstruct STCI;
- the pencil is geometrically genuine, in which case one must pass to the fourth/quasiprimitive layer and BF defect data.

Before interpreting any observed fixed locus as new, compare it with classical surface-contact/residual-intersection literature and with the older rational-quartic STCI papers.


---

## Consolidation status (2026-10-28)

This is retained as detailed historical evidence, not a present quartic-carrier research frontier. The [canonical order-one result](../results/order_one.md) now includes the rank-defect definitions, quadric comparison and finite-jet source model. The [October 7 e=1 rebuild](OCT7_SATURATION_REES_AND_CARRIER_CLASSIFICATION.md#2026-10-07-e1-jet-rebuild) supplies later calculations and explicitly repairs the initially invalid fixed-ruling-line argument. The [complete quartic-carrier exclusion](../results/quartic_carrier_exclusion.md) supersedes historical quartic-mate open cases; the unrestricted higher-degree STCI problem remains open. All exact computational claims here retain their original audit status, without new independent reruns.


---

## 2026-10-06-positive-characteristic-literature-audit

# Positive-characteristic literature audit, 2026-10-06

Status: primary-source literature audit and an exact audit of an unrefereed proof. No universal projective STCI theorem is asserted. This note was prepared independently of the agents working on the characteristic-zero computation frontier.

## Conclusions and scope

The search did not locate a primary-source theorem proving that every integral curve in `P^3` is an STCI either over an arbitrary algebraically closed field of positive characteristic or over `Fpbar`. A failed search is not a proof of open status. The positive results actually found have extra hypotheses or are affine. Two particularly tempting apparent shortcuts fail for precise reasons recorded below.

1. Cowsik--Nori concerns affine curves, not projective curves or their two-dimensional cones.
2. Moh concerns all projective monomial curves in characteristic `p>0`, and curves admitting a birational linear plane projection with center disjoint from the curve and only cusps in the plane image. It does not state that every projective curve admits such a projection.
3. Das's peer-reviewed theorem already proves STCI for lci surfaces in affine space over `Fpbar`; a non-CI projective space curve has a cone that is not lci at its vertex.
4. A 2025 Mandal--Zinna preprint states a broader affine result, but its displayed splitting argument fails an elementary exactness test. Its unrestricted claims should be recorded as claims with an invalid proof, not imported as established theorems.
5. Torsion in the degree-zero Picard group over `Fpbar` does not remove the Neron--Severi obstruction to a curve being STCI on a specified surface. A different literature term, the *set-theoretic complete intersection property* (SCIP), concerns cutting finite subsets on a curve and must not be confused with cutting the curve by two surfaces.

## Primary sources checked

### Cowsik--Nori and the projective special families

R. C. Cowsik and M. V. Nori, *Affine curves in characteristic p are set theoretic complete intersections*, Invent. Math. 45 (1978), 111--114. The [publisher record](https://link.springer.com/article/10.1007/BF01390268) confirms the bibliographic data; the full paper was not accessible through the browser. The theorem is affine: a pure affine curve in affine `n`-space in characteristic `p` is set-theoretically cut out by `n-1` equations. The affirmative projective conclusion does not occur in the title or in the accessible primary record.

T. T. Moh, *Set-theoretic complete intersections*, Proc. AMS 94 (1985), 217--220. The [AMS abstract](https://www.ams.org/proc/1985-094-02/S0002-9939-1985-0784166-1/) directly states two results: projective monomial curves over a characteristic-`p` field are STCI; and a curve over an algebraically closed characteristic-`p` field is STCI if it has a birational linear plane projection, with center disjoint from the curve, whose image has only cusps. Its references include Hartshorne's *Complete intersections in characteristic p>0*, Amer. J. Math. 101 (1979), 380--383, and Ferrand's 1979 chapter. Hartshorne's [JSTOR record](https://www.jstor.org/stable/2373984) was found, but its full text was not accessible. The universal monomial-family scope is verified directly in Moh, rather than extrapolated from Hartshorne.

### Das: the established affine surface theorem

Mrinal Kanti Das, *On a conjecture of Murthy*, Adv. Math. 331 (2018), 326--338, DOI 10.1016/j.aim.2018.04.012. The [publisher abstract](https://www.sciencedirect.com/science/article/pii/S000187081830152X) explicitly gives the lci affine-surface application. The [author PDF](https://oldweb.isical.ac.in/~mrinal/Murthy_CI_v2.pdf), accessible through indexed primary-source search text, gives Theorem 4.2: an lci ideal of height `d-2` in `Fpbar[X1,...,Xd]`, `d>=4`, is STCI. Theorem 4.1 first constructs a same-support lci thickening with free conormal. For `d=4`, the proof produces a rank-two projective module and invokes Quillen--Suslin to make it free. This is affine space and requires the lci hypothesis.

### Mandal--Zinna: published and preprint statements are distinct

The separate published paper *Set-theoretic complete intersection for smooth surfaces in a smooth affine algebra*, J. Algebra 693 (2026), 36--53, DOI 10.1016/j.jalgebra.2025.12.026, has a [primary publisher abstract](https://www.sciencedirect.com/science/article/abs/pii/S0021869326000165). Its surface result is conditional: smooth affine ambient algebra over `Fpbar`, trivial conormal, and torsion class in the Grothendieck group. Several formulas in the browser's introduction extract are missing, so this audit does not claim to have verified the precise dimension inequality of every numbered theorem.

The [arXiv v1 full text](https://arxiv.org/html/2511.07589v1) of *On set-theoretic complete intersections for smooth curves in three-dimensional affine schemes* was inspected directly. Theorem 4.8 claims STCI for any height-two lci ideal in a four-dimensional affine algebra over `Fpbar`. Theorem 4.4 also claims CI for a height-two lci ideal with free conormal in any Noetherian ring of dimension at least two. Theorem 4.8 reuses the proof of Theorem 4.2. The exactness audit below invalidates that argument. This audit refutes the unrestricted Theorem 4.4; it does not by itself refute every field-restricted STCI assertion in the preprint.

## Exact obstruction to applying affine surface theorems to the cone

This is proved here and needs no literature extension.

Let `S=k[x0,x1,x2,x3]`, let `m=(x0,x1,x2,x3)`, and let `I` be the homogeneous prime ideal of an integral projective curve. If `I_m` is lci, it has two minimal generators because its height is two in the regular local ring `S_m`. The minimal number of generators equals

`dim_k(I/mI)`.

This is also the number of minimal homogeneous generators of `I`. Hence `I` has two homogeneous generators, so the projective curve is already a scheme-theoretic complete intersection. Thus the affine cone of every projective curve that is not a scheme-theoretic CI fails the lci hypothesis at the vertex. Smoothness of the projective curve does not fix this failure. For example, the twisted cubic is smooth, but its cone ideal has three quadratic minimal generators.

Even an affine same-support pair need not be homogeneous. A further argument is required to supply two homogeneous equations or to control the hyperplane at infinity.

## Exact audit of arXiv:2511.07589v1, Step 3

The source location is Theorem 4.2, Step 3, displayed sequence following equation (1); in the browser HTML it is lines 343--350. The problem is the substitution of `J/(c)` for the actual tensor quotient `J/cJ`.

Test the claimed operation on a complete intersection, over any field:

```
A = k[x,y,z],       J = (x,y),       c = x,
P = A^2,
f(1) = (-y,x),      g(a,b) = ax+by.
```

The sequence `0 -> A -> P -> J -> 0` is exact. Put `B=A/(x)=k[y,z]`. The preprint's proposed sequence with last term `J/(x)` becomes

```
B -> B^2 -> (y) -> 0,
t |-> (-yt,0),       (a,b) |-> by.
```

Its middle kernel is `B(1,0)`, while the preceding image is `yB(1,0)`. The middle homology is `B/(y)`, which is nonzero. Therefore that displayed sequence is not exact, even for this simplest CI ideal.

The actual tensor quotient has an extra torsion summand:

`J/xJ = (x,y)/(x^2,xy)`,

and the class of `x` is nonzero but annihilated by `y`. The natural quotient from `J/xJ` to `J/(x)` kills this summand. If the paper's notation `J/(c)` were instead interpreted as `J/cJ`, its assertion that this module is locally free of rank one would fail in the same example. Neither interpretation repairs the splitting step.

This is an exact algebraic countercheck of the proof, not an argument from parallel agreement or from the theorem's surprising breadth.

## Independent refutation of the unrestricted CI claim

This elementary example is proved here; it is outside the user's algebraically closed-field setting and is used solely to test the preprint's explicit *arbitrary Noetherian ring* claim.

Let

`A = R[x,y,z]/(x^2+y^2+z^2-1)` and `I=(x,y,z-1)`.

The algebra is a smooth two-dimensional real affine algebra, and `I` is the maximal ideal at the north pole. It is lci of height two. In `I/I^2`, the sphere equation gives `2(z-1)=0`, so `I/I^2` has basis the classes of `x,y` and is free of rank two over `A/I=R`.

Suppose `I=(f,g)`. On the real sphere `S^2`, the smooth map `F=(f,g):S^2 -> R^2` then has exactly one zero, the north pole. Since the two generators give a basis of `I/I^2`, its derivative at this zero is invertible, so the local winding number is `+1` or `-1`.

Here is a direct contradiction without invoking an Euler-class computation. On `R^2 \ {0}`, the form

`alpha = (u dv-v du)/(u^2+v^2)`

is closed. Remove a small disk around the north pole from `S^2`; `F^*alpha` is a smooth closed form on the remaining compact surface. Stokes's theorem forces its integral on the boundary to be zero. The invertible derivative forces that same integral to be `+2*pi` or `-2*pi`. Thus `I` cannot have two generators. It is lci with free conormal but is not a CI.

This disproves the preprint's unrestricted Theorem 4.4. It does not give a counterexample to projective STCI over an algebraically closed field.

## Why finite-field torsion does not settle the projective problem

Hartshorne--Polini, *Divisor class groups of singular surfaces*, [primary arXiv full text](https://arxiv.org/html/1301.3222), Proposition 7.1: if a curve meets the singular locus of its carrier surface only finitely, it is STCI on that surface precisely when `r[C]=m[H]` in `APic(X)` for positive integers `r,m`.

An elementary fixed-carrier counterexample to an overbroad torsion inference is a ruling line `L` on a smooth quadric `Q=P^1 x P^1`, over `Fpbar` or any algebraically closed field. Here `Pic^0(Q)=0`, `Pic(Q)=Z^2`, `[H]=(1,1)`, and `[L]=(1,0)`. There are no positive `r,m` with `r(1,0)=m(1,1)`. Thus `L` is not STCI on this chosen quadric, despite complete torsion of `Pic^0(Q)`. Of course the line is STCI in the ambient `P^3` using two planes. The example isolates the gap: finding a suitable carrier with the required full divisor-class relation remains additional work.

Kollar--Lieblich--Olsson--Sawin, *The Zariski topology, linear systems, and algebraic varieties*, [authors' book PDF](https://williamsawin.com/ReconstructionBook.pdf), Definition 7.1.1 and Theorem 7.1.10, prove that over a locally finite perfect field every irreducible curve has SCIP. In that terminology SCIP means that every finite closed subset of the curve can be obtained by intersecting the curve with an ambient effective divisor. It does not mean that the curve is the intersection of two ambient surfaces. The finite-field torsion used there concerns line bundles on the curve and cutting finite subsets. This theorem therefore supplies no hidden affirmative answer to the user's projective space-curve problem.

## Continuation implications

- Preserve the affine/projective and lci-cone boundaries in the ledger.
- Replace any reliance on the broad 2025 preprint with the established affine results whose hypotheses have actually been checked.
- If the broad preprint is retained, attach this exact proof audit and distinguish its claimed results from verified theorems.
- Over `Fpbar`, a useful affirmative route would still have to construct a carrier or a homogeneous thickening satisfying the full divisor relation; degree-zero Picard torsion alone is insufficient.
- No changes to canonical research files were made by this audit agent.


---

## 2026-10-06-primitive-quadruple-audit

# Independent audit of the degree-two primitive-fourth family

Date: 2026-10-06. Status: **independently audited** for the fixed
characteristic-zero curve

\[
C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3.
\]

This note audits the universal calculation in
`scratch/primitive47universal/` and the geometric reconstruction in
`2026-10-05-primitive-carrier-theory.md`. The result is an exact reduced
fourth-obstruction locus and an exhaustive quartic carrier factorization.
It excludes the degree-two first quotient branches of the degree pairs
(4,7) and (4,8). It does **not** exclude every pair of either degree, and it
does not assert a universal obstruction to primitive quadruples.

## 1. Complete parameter coverage

Use the fixed split normal frames of the repository and write a quotient

\[
N_{C_0}^*=O(-7)^2\twoheadrightarrow L=O(-5)
\]

as the pair of binary quadratic sections

\[
A=a_0+a_1z+a_2z^2,\qquad B=b_0+b_1z+b_2z^2.
\]

The epimorphism condition is exactly nonvanishing of their HOMOGENEOUS
resultant

\[
\Delta=a_0^2b_2^2-a_0a_1b_1b_2-2a_0a_2b_0b_2
 +a_0a_2b_1^2+a_1^2b_0b_2-a_1a_2b_0b_1+a_2^2b_0^2.
\]

There is no assumed nonzero leading coefficient. The Sylvester linear map
from pairs of homogeneous linear forms to binary cubics is invertible
precisely on \(\Delta\ne0\). Applying its inverse to the constant affine
polynomial supplies polynomial Bezout coordinates on the first chart;
reversing both binary forms supplies them on the second chart. Thus degree
drops are included. The excluded resultant divisor consists of
non-epimorphic quotients and is not a missing quotient chart.

No arbitrary change of the split conormal frame or of the source coordinate
is used to normalize a pencil. Such a change would require transport of
the nonlinear embedded transition. The six symbolic coefficients and the
single resultant-open condition already cover all quotient points.

The kernel line is \(M=O(-9)\). Both cohomology groups of
\(\operatorname{Hom}(M,L^2)=O(-1)\) vanish. Consequently every such double
has a unique embedded primitive triple. The fourth obstruction lies in
\(H^1(O(-6))\), with its five Laurent coefficients.

## 2. The fourth-obstruction locus is nonempty and exhaustive

The exact embedded transition uses

\[
W=\frac{z^3+v}{z^4+u+\tfrac32zv},
\]

before truncation. The universal code evaluates every opposite-chart
quadratic and correction at this moving coordinate. Its inverse-resultant
arithmetic clears denominators only by powers of \(\Delta\). Thus the
persisted five numerator polynomials have exactly the obstruction's zero
set on \(\Delta\ne0\).

Let I be their ideal and set

\[
K=(2a_1+b_0,2a_2+b_1).
\]

The fresh Macaulay2 audit verified

\[
I\subseteq K,\qquad
\Delta^3(2a_1+b_0)^3\in I,\qquad
\Delta^3(2a_2+b_1)^3\in I.
\]

Therefore the **reduced/set-theoretic** zero locus on the resultant-open
set is exactly

\[
\boxed{b_0=-2a_1,\qquad b_1=-2a_2.}
\]

These certificates do not claim equality of the unreduced obstruction
ideals after localization. Reduced equality is sufficient for every
geometric quotient point and for the carrier exclusion below.

On this locus the resultant becomes

\[
\Delta_0=a_0^2b_2^2+6a_0a_1a_2b_2+4a_0a_2^3-2a_1^3b_2.
\]

In particular \((a_0,b_2)\ne(0,0)\). The sample
\(A=z^2+1,B=-2z\) belongs to the locus and is a mandatory control against
a false blanket exclusion of primitive quadruples.

## 3. Independent quadratic contact reconstruction

The audit companion `computations/verify_primitive_quartic_factor_audit.py`
does not import the universal Laurent-jet implementation. It reconstructs
the quadratic cocycle directly from the ambient transition. With
\(D=A'B-AB'\), it obtains

\[
h_2=-\frac{2A+zB}{8z^5}
 (12A^2+3z^2B^2+4z^2D).
\]

The derivative term comes from the first displacement of W; it disappears
incorrectly if W is frozen to 1/z. Let \(\gamma_U\) be the nonnegative
Laurent part of \(h_2\). A first-chart triple equation is
\(m+\gamma_U\ell^2=0\), where \(m=Bu-Av\).

The companion independently computes the entire first-symbol image from
the thirty-five degree-four monomials. The quartic ideal has dimension
eighteen, its normal image has rank seventeen, and the three independent
image equations are

\[
P_1=2Q_2,\qquad P_4=2Q_5,\qquad P_7=2Q_8.
\]

The kernel is the one-dimensional space generated by the quadric square.
On the reduced fourth-obstruction locus, a symbol is \(h(B,-A)\), with
h a global section of O(7). The three image equations force
\(h_2=h_5=0\): explicitly they imply

\[
a_0h_2=0,\qquad b_2h_2+2a_0h_5=0,\qquad b_2h_5=0.
\]

Since \((a_0,b_2)\ne(0,0)\), this covers both boundary charts. The six
remaining coefficient lifts plus the quadric square give an exhaustive
seven-dimensional pre-contact space.

For a lift with first symbol h m, the actual triple restriction is the
ordinary quadratic Taylor coefficient under u=A ell, v=B ell, minus
\(h\gamma_U\). This formula is independent of the Bezout coordinate:
the second correction changes m by exactly \(-\gamma_U\ell^2\).
The audit companion reconstructs all seven such coefficients and matches
the persisted matrix M2 exactly.

Its function-field rank is three, hence all fourth minors vanish
identically. Two explicit third minors are

\[
\det M2_{\{0,1,2\},\{4,5,6\}}=-a_0^8,
\quad
\det M2_{\{4,5,6\},\{0,1,6\}}=-b_2^8/256.
\]

Their opens cover \(\Delta_0\ne0\). Therefore its rank is exactly three
at EVERY quotient point in scope, not merely at a generic point. The
quartic triple-carrier kernel consequently has dimension four everywhere.

## 4. The kernel is exactly a cubic times all linear forms

In ambient coordinates [x:y:Z:W] set Q=xW-yZ and

\[
\begin{aligned}
T={}&Q(2a_0a_1x+2a_0a_2y+a_1b_2Z+a_2b_2W)\\
 &+a_0^2(x^2Z-y^3)+a_0b_2(xZ^2-y^2W)
 -\frac{b_2^2}{4}(yW^2-Z^3).
\end{aligned}
\]

The audit independently checks

\[
\sigma_1(T)=-\frac{2a_0+b_2z^3}{2}(B,-A)
\]

and verifies its quadratic Taylor cancellation against \(\gamma_U\).
Thus T contains the canonical triple. It is nonzero on the entire
resultant-open locus: its coefficients of y^3 and Z^3 are respectively
\(-a_0^2\) and \(b_2^2/4\).

The companion expresses xT,yT,ZT,WT in the seven universal lift basis and
checks their polynomial identities and contacts. Multiplication by the
nonzero polynomial T is injective on the four-dimensional linear-form
space, at every specialization. They are four independent kernel elements,
which exhaust the dimension computed above. Hence

\[
\boxed{H^0(\mathcal I_{C_3}(4))=T\,H^0(O_{\mathbf P^3}(1)).}
\]

The persisted third-contact matrix also kills those four columns, and its
combined rank remains three. This checks their compatibility with the
primitive fourth layer. The carrier exclusion already follows at the
triple layer and does not need a terminal higher obstruction.

The symbol scalar \(2a_0+b_2z^3\) has zeros as a homogeneous O(3)
section. T need not be smooth along the whole reduced curve. None of these
statements constructs an STCI or a smooth ambient carrier.

## 5. Exact degree-pair consequence

For a hypothetical (4,b) pair on C0, the verified BF formula gives

\[
\deg D_{b-1}=(3-e)b+e-9.
\]

At e=2 this is b-7. If b=7, the top defect is zero and all defects vanish.
If b=8, the top defect has degree one; superadditivity gives
2D2<=D4<=D7 and 2D3<=D6<=D7, so D2=D3=0. In either case the canonical
primitive quadruple has L=O(-5). Its quotient therefore lies on the
audited reduced fourth-obstruction locus. The defining quartic contains
its canonical triple, hence has the form F4=T L1 for a nonzero linear form.

This is immediately incompatible with an STCI presentation of nonplanar
C0. V(L1,G_b) is a nonempty projective curve, or the whole plane if the
restriction vanishes identically. It cannot be contained in C0, because
C0 is integral and not contained in that plane. Thus the terminal
exclusion requires no independent cubic-carrier literature theorem.

The conclusion is precisely: **the e=2 branches of (4,7) and (4,8) are
excluded**. The e=0 and e=1 branches, larger pairs with early defects, and
the entirely thick branch are outside this result.

## 6. Companion uniform-bound audit

The separate root note `2026-10-06-uniform-order-one-frontier.md` was
checked algebraically. For a,b>=4 and an order-one equation, set
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

Here q>=1 because ab/4>=4. The ancestor inequality likewise follows from
the top section degree after removing its pure-power direction:

\[
7n-4d-5-e(n-1)\ge0
\iff (7-e)(n-1)\ge4d-2.
\]

This confirms the stated finite early-jet reduction under its checked BF,
normal-bundle, and linear-contraction inputs. It does not cover two
entirely thick equations or bound either equation degree.

## Reproducibility

Fresh checks on 2026-10-06 passed:

- `/opt/homebrew/bin/M2 --script research/scratch/primitive47universal/classify.m2`;
- `/opt/homebrew/bin/M2 --script research/scratch/primitive47universal/quartic_contact.m2`;
- `PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python research/computations/verify_primitive_quartic_factor_audit.py`.

The audit Python check uses the persisted lift list as input but verifies
the full ambient image, reconstructs the quadratic cocycle and contact
matrix independently, and checks the polynomial T-factor identities. Its
third-layer check uses the persisted third-contact matrix. The universal
fourth-obstruction generation and membership certificates remain separate
inspectable inputs; no finite quotient sampling is used as a proof.


---

## 2026-10-06-primitive-quadruple-universal

# Universal primitive-fourth classification and the ambient quartic obstruction

Status: exact universal classification and carrier theorem, verified over
characteristic zero. The result excludes the degree-two direction branches
of hypothetical `(4,7)` and `(4,8)` complete intersections on the fixed curve
`C0=[s^4:s^3t:st^3:t^4]`. It does not settle STCI for `C0`, other rational
quartics, arbitrary curves, or positive characteristic.

The computation corrects the plausible universal exclusion suggested by
the samples in `2026-10-05-uniform-multiplicity.md`: primitive quadruples of
conormal quotient type `O(-5)` **do exist**. Their quotient directions form
a resultant-open subset of a linear projective three-space. The obstruction
to the indicated complete intersections is instead that every ambient
quartic containing their canonical primitive triple factors as a cubic
times a linear form.

## Formal coordinates and complete parameter coverage

Use the first ambient chart

\[
z=x_1/x_0,\quad v=x_2/x_0-z^3,\quad
u=x_3/x_0-z^4-\tfrac32zv.
\]

The opposite moving coordinate is

\[
W=\frac{z^3+v}{z^4+u+\tfrac32zv},
\]

and its split normal coordinates are

\[
u'=\tfrac12\left(\frac z{z^4+u+\tfrac32zv}-W^3\right),\quad
v'=-\frac{3zW}{z^4+u+\tfrac32zv}+W^4+
\frac2{z^4+u+\tfrac32zv}.
\]

To first order both normal coordinates transition by `z^-7`. Specify
the quotient `O(-7)^2 -> L=O(-5)` by

\[
A=a_0+a_1z+a_2z^2,\qquad B=b_0+b_1z+b_2z^2,
\quad u\mapsto A\ell,\quad v\mapsto B\ell.
\]

These are homogeneous binary quadratics, even when an affine leading
coefficient vanishes. Their projective resultant is

\[
\Delta=a_0^2b_2^2-a_0a_1b_1b_2-2a_0a_2b_0b_2+
a_0a_2b_1^2+a_1^2b_0b_2-a_1a_2b_0b_1+a_2^2b_0^2.
\]

The sole parameter restriction is `Delta != 0`. The matrix sending
degree-at-most-one Bezout coefficients `(S0,S1,T0,T1)` to the coefficients
of `(S0+S1 z)A+(T0+T1 z)B` is

\[
\begin{pmatrix}
a_0&0&b_0&0\\a_1&a_0&b_1&b_0\\
a_2&a_1&b_2&b_1\\0&a_2&0&b_2
\end{pmatrix}.
\]

Its determinant is `Delta`, including affine degree drops. Thus the
Bezout gauges exist uniquely over the entire resultant-open set; no
additional leading-coefficient charts, generic-pencil normalization, or
unexamined boundary directions enter the computation. Reversing the
coefficient vectors gives the opposite-chart gauges, with the same
determinant. We do not use arbitrary changes of the split frame or base
coordinate to normalize quotient directions: those would require changing
the full nonlinear transition.

Set `m=Bu-Av`, whose line type is `M=O(-9)`. Then

\[
\operatorname{Hom}(M,L^2)=O(-1),\qquad
\operatorname{Hom}(M,L^3)=O(-6).
\]

Because both cohomology groups of `O(-1)` vanish, each direction has a
unique embedded primitive triple. A zero fourth obstruction also produces
a unique primitive quadruple, since `H0(O(-6))=0`.

## Exact fourth obstruction and its entire zero locus

For `d=A'B-AB'`, the quadratic cocycle is

\[
h_2=-\frac{2A+zB}{8z^5}\left(12A^2+3z^2B^2+4z^2d\right).
\]

Write `gammaU` for its nonnegative Laurent part and put
`gammaV=(-z*(h2-gammaU))|_(z=1/w)`. The canonical triple has
`m+gammaU ell^2=0` on the first chart and
`m'+gammaV(W) ell'^2=0` on the second. Polynomial Bezout coefficients
`SA+TB=1` give its first-chart parameterization

\[
u=A\ell-T\gamma_U\ell^2,\qquad
v=B\ell+S\gamma_U\ell^2.
\]

All coefficient functions in the opposite equation are evaluated at the
moving coordinate `W` **before truncating**. The cubic coefficient of that
equation, multiplied by `z^9`, gives a Laurent cocycle `h3`; its
coefficients of `z^-1,...,z^-5` represent `H1(O(-6))`.

The universal exact result is

\[
(c_1,\ldots,c_5)=(G_1,\ldots,G_5)/\Delta,
\]

where each `Gi` is a homogeneous degree-eight polynomial. Their complete
expanded values, not a numerical fit, are preserved in
`research/scratch/primitive47universal/equations.json`. If `I=(G1,...,G5)`
and `K=(2a1+b0,2a2+b1)`, the verified exact certificates are

\[
I\subseteq K,\qquad
\Delta^3(2a_1+b_0)^3\in I,\qquad
\Delta^3(2a_2+b_1)^3\in I.
\]

Consequently, on `Delta != 0`, all five coordinates vanish **if and only if**

\[
\boxed{b_0=-2a_1,\qquad b_1=-2a_2.}
\]

This is a set-theoretic classification; the powers in the membership
certificates are not a claim that the obstruction scheme is reduced.
Its projectivized parameter space is an open subset of a linear `P3`.
The restricted resultant is

\[
\Delta_0=a_0^2b_2^2+6a_0a_1a_2b_2+4a_0a_2^3-2a_1^3b_2.
\]

In particular, `(a0,b2)` cannot both vanish. Equivalently, the fourth-zero
directions satisfy

\[
2A+zB=q_0=2a_0+b_2z^3.
\]

For example `A=z^2+1, B=-2z` has
`h2=-4/z-8/z^3-3/z^5`, `gammaU=0`,
`gammaV=4+8w^2+3w^4`, and all five fourth coordinates zero. The prior
nonzero sampled direction `A=z^2,B=1` lies outside this locus.

## Every quartic carrier is a cubic multiple, on all charts

Use ambient coordinates `[x:y:Z:W]`, and define

\[
Q=xW-yZ,
\]

\[
\boxed{
T=Q(2a_0a_1x+2a_0a_2y+a_1b_2Z+a_2b_2W)
+a_0^2(x^2Z-y^3)+a_0b_2(xZ^2-y^2W)
-\frac{b_2^2}{4}(yW^2-Z^3).
}
\]

This cubic is in the ideal of `C0`; its first normal symbol is
`-q0(B,-A)/2`. It contains the canonical primitive triple and quadruple.
The universal verifier checks the latter directly through third order in
`ell`, using the unique gluing correction for the quadruple.

The first-symbol image of ambient quartics in `I(C0)` has dimension 17,
with kernel `kQ^2`; its three missing linear combinations are
`Qnormal_2=P_1/2`, `Qnormal_5=P_4/2`, `Qnormal_8=P_7/2`.
For direction `(B,-A)` on the fourth-zero locus, an admissible symbol is
`h(B,-A)`, with

\[
h\in\langle1,z,z^3,z^4,z^6,z^7\rangle.
\]

Thus its quartic lift has seven coefficients, the six coefficients of
`h` and the coefficient `k` of `Q^2`. Restricting these lifts to the
canonical triple gives the following seven-by-seven matrix, with columns
ordered `(h0,h1,h3,h4,h6,h7,k)` and rows ordered by the coefficient of
`z^0,...,z^6` in the quadratic normal jet:

\[
\begin{pmatrix}
a_0a_2b_2&-a_0a_1b_2&-2a_0^2a_2&0&0&0&a_0^2\\
-a_0b_2^2/4&0&a_0^2b_2/2&0&-a_0^3&0&0\\
0&a_0b_2^2/4&0&-a_0^2b_2/2&0&a_0^3&0\\
a_2b_2^2/2&-a_1b_2^2/2&-a_0a_2b_2&-a_0a_1b_2&-2a_0^2a_2&2a_0^2a_1&a_0b_2\\
-b_2^3/8&0&a_0b_2^2/4&0&-a_0^2b_2/2&0&0\\
0&b_2^3/8&0&-a_0b_2^2/4&0&a_0^2b_2/2&0\\
0&0&0&-a_1b_2^2/2&-a_0a_2b_2&a_0a_1b_2&b_2^2/4
\end{pmatrix}.
\]

Its minor in zero-based rows `(0,1,2)` and columns `(4,5,6)` is
`-a0^8`; that in rows `(4,5,6)` and columns `(0,1,6)` is
`-b2^8/256`. Because `Delta0 != 0` implies `(a0,b2) != (0,0)`, these
two minors cover every admissible direction and prove rank at least three.
The four independent quartics `xT,yT,ZT,WT` lie in the kernel. The cubic
is never zero: its `y^3` coefficient is `-a0^2`, and its `Z^3`
coefficient is `b2^2/4`. Hence these multiples are linearly independent,
proving rank exactly three on the full resultant-open locus.

For the primitive triple `Y3` and quadruple `Y4`, this proves

\[
\boxed{
H^0(\mathcal I_{Y_3}(4))=
H^0(\mathcal I_{Y_4}(4))=
T\,H^0(O_{\mathbf P^3}(1)).
}
\]

An equivalent compact solution of the matrix is

\[
h=q_0(c_0+c_1z+c_3z^3+c_4z^4),\qquad
k=2a_1b_2c_1+4a_0a_2c_3.
\]

The coincidence between the fourth-zero locus and the rank-two exceptional
quartic first-symbol direction locus is independently obtained in the
local-cohomology direction investigation. It explains why a generic
first-symbol rank count would miss this family.

## Consequence for hypothetical complete intersections

For a quasiprimitive complete intersection `(4,b)` supported on `C0`,
the checked filtration duality in `2026-10-05-uniform-multiplicity.md`
gives, when `L=O(-5)`, top defect degree `b-7`. At `b=7` the entire
structure is primitive. At `b=8`, superadditivity and complementary
divisor duality force `D2=D3=0`, so its canonical fourth structure is
primitive. Thus either branch requires a direction in the classified
fourth-zero locus and its defining quartic must contain `Y3`.

The carrier theorem forces `F4=T*H` with `H` a nonzero linear form.
For any homogeneous mate `Gb` of positive degree, `V(H,Gb)` is a
projective plane curve or the whole plane. It is contained in
`V(F4,Gb)`, and it cannot be contained in the nonplanar integral curve
`C0`. Therefore `V(F4,Gb)` cannot have support exactly `C0`.

This excludes the **e=2 branches** of `(4,7)` and `(4,8)` on `C0`.
The same argument excludes any `(4,b)` whose e=2 canonical quadruple is
primitive. It does not exclude e=0 or e=1 at these degrees, nor e=2
structures with a defect before the fourth layer, nor carriers of higher
degrees. The cubic `T` can be singular at the zeros of `q0`; its existence
does not furnish a smooth supporting surface or an STCI construction.

## Reproduction and continuation evidence

One repository-local command verifies the full calculation, including
exact ideal membership and all-chart rank minors:

```sh
python research/computations/verify_primitive_quadruple_universal.py
```

It requires SymPy and Macaulay2's `M2`. The verified session used
`/private/tmp/stci-cas-venv/bin/python` and Macaulay2 1.26.06. The script
does not depend on other files under `/private/tmp`. It regenerates its
inspectable scratch equations, derives all jets with sparse polynomial
arithmetic, checks ten directions against the original independent
rational-series implementation, verifies the universal cubic restrictions,
and runs exact Macaulay2 certificates. The ten sample comparisons are
cross-checks; the global conclusions come from the polynomial identities,
resultant-localized membership certificates, and covering minors.

The durable files are `verify_primitive_quadruple_universal.py`,
`scratch/primitive47universal/{generate.py,equations.json,classify.m2}`,
and `scratch/primitive47universal/{quartic_contact.py,quartic_contact.json,
quartic_contact.m2}`. The independent theoretical reconstruction is in
`2026-10-05-primitive-carrier-theory.md`; the frontier-audit lane is
checking the quadratic cocycle and contact matrix by a separate
Bezout-independent computation.

A tempting fifth-order exclusion also fails for the sample
`A=z^2+1,B=-2z`: its fifth obstruction is zero, as recorded with exact
Laurent coefficients in the theory note. The productive next question is
therefore the uniform ambient compatibility of an e=2 primitive triple,
and then the remaining case `deg D2=1`; increasing sampled primitive
orders does not address the ambient quartic factor obstruction.


---

## 2026-10-06-primitive-triple-parity

# Complete primitive-triple parity slice and a two-defect obstruction

Status: exact characteristic-zero classification of the entire parity
slice; necessary extension argument checked conceptually by the frontier
audit lane. The statement concerns the fixed curve
`C0=[s^4:s^3t:st^3:t^4]`, a hypothetical complete intersection with a
quartic carrier, degree-two first quotient, and **D2=0**. The conclusion is
an all-mate-degree exclusion for this parity slice. It does not exclude
arbitrary degree-two directions or the case `deg D2=1`.

## Exhaustive one-parameter family

Consider the basepoint-free quotient direction

\[
A=a_0+a_2z^2,\qquad B=b_1z.
\]

Projective coprimality forces `a0*a2*b1 != 0`. The actual ambient
automorphism

\[
[x_0:x_1:x_2:x_3]\longmapsto
[x_0:c x_1:c^3x_2:c^4x_3]
\]

preserves `C0` and sends the exact split coordinates `(z,u,v)` to
`(cz,c^4u,c^3v)`. Choose `c^2=a2/a0` and rescale the quotient. This
gives the complete normal form

\[
\boxed{A=1+z^2,\qquad B=\beta z,\qquad \beta\ne0,}
\]

where `beta=b1/a2`. This normalization uses an embedded automorphism and
transports the full jets; it is not an arbitrary normal-frame or pencil
change. Its homogeneous resultant is `beta^2`.

## Exact quartic compatibility of the canonical primitive triple

Because `Hom(M,L^2)=O(-1)`, every degree-two direction has its unique
primitive triple `Y3`. A quartic containing `Y3` must have first symbol
`h(B,-A)`, with `h` a binary form of degree seven, and may have the extra
`Q^2` coefficient, where `Q=x0*x3-x1*x2`. These nine coefficients obey
three ambient first-symbol image constraints and seven actual quadratic
contact equations.

The universal derivation in
`scratch/primitive47universal/general_triple_contact.py` reconstructs the
symbol image from all 35 quartic monomials, chooses a constant rational
right inverse to its 34-dimensional combined restriction/symbol image,
and computes the contact coefficient

\[
f_2-h\gamma_U,
\]

where `f2` is the ordinary quadratic Taylor coefficient and `gammaU`
is the nonnegative Laurent part of the canonical triple cocycle. This
formula does not require a Bezout choice. Three higher polynomial
coefficients are exact multiples of one first-symbol constraint, so the
ten equations are exhaustive.

On the displayed parity family, the resulting matrix is ten by nine.
The exact greatest common divisor of its ten maximal minors, normalized
to be monic, is

\[
\boxed{(\beta-6)(\beta+2)^9(\beta+6)^2.}
\]

Thus the triple has an ambient quartic carrier **if and only if**

\[
\boxed{\beta=-2,\quad -6,\quad\text{or }6.}
\]

At `beta=-2` the matrix rank is five, and the four-dimensional carrier
space is cubic times linear forms, exactly as proved in
`2026-10-06-primitive-quadruple-universal.md`. At `beta=+-6` the rank is
eight and the carrier is unique up to scalar. In ambient coordinates
`[x:y:Z:W]`, convenient forms are

\[
F_+=6xWy^2-x^2yZ-4x^2Z^2+y^4-2y^3Z,
\]

\[
F_-=8xW^3+6xWyZ+12xWZ^2+x^2Z^2-y^3Z
       -6y^2Z^2-12yZ^3-8Z^4.
\]

The normalizations in the exact coefficient certificate are `F+` and
`-F-/6`, respectively. No claim of geometric irreducibility is needed.
A separate Jacobian check found affine singular-ideal dimension two and
degree three for each; these are not covered by an isolated-singularity
normal-quartic argument.

## A necessary condition for introducing the fourth-layer defect

Let `Y3` be the primitive triple associated to a degree-two quotient, and
put `L=O(-5)` and `M=O(-9)`. Its ideal is locally generated by

\[
f=m+\gamma\ell^2,\qquad \ell^3.
\]

Consequently the rank-two bundle

\[
\mathcal V=\mathcal I_{Y_3}/
                 (\mathcal I_C\mathcal I_{Y_3})
\]

fits in an exact sequence

\[
0\longrightarrow L^3\longrightarrow\mathcal V
\longrightarrow M\longrightarrow0.
\]

Its extension class is the ordinary primitive-fourth obstruction
`h3 in H1(Hom(M,L^3))=H1(O(-6))`: the off-diagonal term of the transition
between the two ideal generators is precisely the cubic moving-coordinate
coefficient used in the universal fourth verifier.

Suppose a saturated quasiprimitive fourth layer `Y4` extends `Y3`, with

\[
E_3=\mathcal I_{Y_3}/\mathcal I_{Y_4}=L^3(D_3).
\]

The support ideal `I_C` annihilates `E3`: it does so generically, and
`E3` is torsion free on `C`. Hence the quotient map gives
`V -> E3`. Its restriction to `L^3` is the canonical multiplication
section with zero divisor `D3`. Applying `Hom(-,E3)` to the exact sequence
above shows the necessary condition

\[
\boxed{
h_3\longmapsto0\quad\text{in}\quad
H^1(O(-6+D_3)).
}
\]

This is a necessary condition, not a sufficiency or classification claim
for defective extensions. Equivalently, some nonzero binary form of degree
`deg D3` must annihilate the class under multiplication. Higher terms
`ell*f` and `ell^4` cannot alter this condition, because their images in
`E3` vanish.

For a quartic-carrier complete intersection with degree-two first quotient,
the checked all-degree filtration calculation in
`2026-10-05-uniform-multiplicity.md` gives, with `s=mate_degree-1`,

\[
\deg D_s=s-6.
\]

Write `s=3q+r`, `0<=r<=2`. Superadditivity implies
`q deg D3 <= 3q+r-6 < 3q`, and hence

\[
\boxed{\deg D_3\le2.}
\]

This bound uses the complete-intersection adjunction and divisor duality;
it is not a bound for arbitrary standalone multiple curves.

## The two remaining parity carriers cannot support the bounded defect

The exact fourth-obstruction coordinates, ordered by
`z^-1,...,z^-5`, are

\[
c_+=( -128,0,160,0,-192),\qquad
c_-=(64,0,-8,0,0).
\]

Multiplication by an arbitrary binary quadratic has, in these coordinates,
the matrix

\[
H(c)=\begin{pmatrix}
c_1&c_2&c_3\\c_2&c_3&c_4\\c_3&c_4&c_5
\end{pmatrix}
:H^0(O(2))\longrightarrow H^1(O(-4)).
\]

This follows directly by multiplying a Laurent representative by
`sigma0+sigma1*z+sigma2*z^2` and keeping the three surviving terms
`z^-1,z^-2,z^-3`. The determinants are

\[
\det H(c_+)=-163840,\qquad \det H(c_-)=512.
\]

Thus neither class has a nonzero quadratic annihilator. A degree-zero or
degree-one annihilator would produce a quadratic annihilator by further
multiplication, so these are excluded as well. Neither unique quartic
triple carrier can be part of a hypothetical complete intersection with
`deg D3<=2`. The `beta=-2` carrier has already been excluded by its linear
factor. Every other parameter admits no quartic containing its primitive
triple. Therefore the entire basepoint-free parity family with `D2=0`
is excluded for **every mate degree**.

## Reproduction and remaining open computation

The exact companion is

```sh
python research/computations/verify_primitive_triple_parity.py
```

It regenerates the arbitrary-direction quartic contact matrix, uses
polynomial-domain determinants over `QQ[beta]` for all ten maximal minors,
checks their gcd and the three exceptional ranks, reconstructs the two
unique quartics, checks their classes against the original rational-series
fourth-obstruction implementation, and verifies both Hankel determinants.
Its full certificate is
`scratch/primitive47universal/parity_triple_certificate.json`.

The all-direction primitive-triple contact matrix is saved in
`general_triple_contact.json`. Attempts to compute the whole six-parameter
rank-drop ideal by generic Macaulay2 maximal minors and saturation were
stopped after remaining slow. A normalized nonexceptional chart and a
finite-field version also did not complete. Those attempts establish no
global classification. An exact one-chart Dynamic determinant calculation
completed but produced large expanded minors; it did not settle the
saturated ideal. The files `general_triple_contact.m2`,
`triple_contact_p_chart.m2`, and `triple_contact_p_factors.m2` preserve the
attempts. No unfinished CAS jobs remain from this lane.

The strongest continuation target is the arbitrary-direction rank-drop
locus of the ten-by-nine matrix, followed by the quadratic-annihilator
incidence condition for its fourth obstruction. The separate case
`deg D2=1` needs a defective-triple gluing state; a primitive-triple
calculation cannot silently be applied to it.


---

## 2026-10-06-quartic-jet-geometry-structural-supplement

# Canonical-status notice

This note was developed on a side branch that forked before the 2026-10-06 audited consolidation. Its geometric lemmas and proposed jet-budget framework are retained as structural research material. **Its repeated statement that the characteristic-zero (4,7), e=2 branch remains open is superseded by `research/AUDITED_STATE_2026-10-06.md`, Section B:** the canonical primitive-triple quartic factorization theorem excludes the e=2 branches of (4,7) and (4,8). Do not use the obsolete frontier language below as a premise. The jet/ruling interpretation may still be useful for e=0/e=1 and broader STCI questions.

---

# Quartic jet geometry and a possible STCI condition-budget framework

Date: 2026-10-06

## Purpose

This note records the geometric reinterpretation of the quartic-incidence calculation for the primitive (4,7), e=2 program for
C = [s^4:s^3t:st^3:t^4] in P^3,
and isolates a possible general research program suggested by it.

The immediate problem remains: a hypothetical (4,7), e=2 carrier must contain the canonical primitive triple C_3. We want to understand H^0(I_{C_3}(4)) geometrically, especially together with P-044. The broader observation is that STCI questions may be organized by a successive "jet-condition budget" for hypersurfaces required to contain primitive multiple structures.

Statements below are labelled PROVED / EXACT COMPUTATIONAL EVIDENCE / HEURISTIC / OPEN. The broader jet-budget program is not a theorem.

---

## 1. The unique quadric and the first-normal codimension three

Let Q = P^1 x P^1 be the unique smooth quadric containing C. With the convention used here, C has bidegree (3,1).

For a quartic F containing the primitive double C_2, its restriction to Q has C as a component:
F|_Q = C + D, with D of bidegree (1,3).

The residual restriction sequence is

    0 -> O_Q(-2,2) -> O_Q(1,3) -> O_C(10) -> 0.

Since H^0(O_Q(-2,2))=0 and H^1(O_Q(1,3))=0, we obtain

    0 -> H^0(O_Q(1,3)) -> H^0(O_C(10))
      -> H^1(O_Q(-2,2)) -> 0.

By Kunneth,

    H^1(O_Q(-2,2))
      = H^1(P^1,O(-2)) tensor H^0(P^1,O(2)),

so this cokernel has dimension 3.

**PROVED.** The previously observed codimension-three first-normal condition is intrinsic: the extendable degree-10 sections are the kernel of the connecting map to H^1(O_Q(-2,2)). In the affine coordinate basis this is the old

    V = <1,z,z^3,z^4,z^6,z^7,z^9,z^10>;

the missing z^2,z^5,z^8 are a coordinate manifestation of the 3-dimensional cohomological obstruction.

## 2. Comparison of the two conormal filtrations

The embedding through the quadric gives

    0 -> O(-8) -> N_C^* = O(-7)^2 -> O(-6) -> 0.

The primitive double gives

    0 -> M=O(-9) -> N_C^*=O(-7)^2 -> L=O(-5) -> 0.

The composite O(-8) -> N_C^* -> L=O(-5) is multiplication by a cubic r in H^0(O_C(3)). In the established affine normalization,

    r = A + (z/2) B.

Let R=Z(r), a degree-three divisor.

**PROVED.** Up to scalar, the induced map M=O(-9) -> O(-6) is also multiplication by r. Thus

    M = O(-6)(-R).

Geometrically, the primitive conormal kernel is the elementary modification of the conormal direction inside Q at R.

After twisting by O_C(4)=O(16),

    M(4)=O(7) -> O(10)

is h |-> rh.

## 3. Intrinsic description of the first-order source K_r

A quartic through C_2, modulo the universal q^2 direction, corresponds to h in H^0(O_C(7)) such that rh extends from C to a section of O_Q(1,3). Therefore

    K_r = ker[ H^0(O_C(7)) -> H^1(O_Q(-2,2)) ],
                 h |-> delta(rh).

Equivalently,

    K_r = H^0(Q,I_{R/Q}(1,3)).

**PROVED.** Generically three points impose three independent conditions on H^0(O_Q(1,3)), whose dimension is 8, so dim K_r=5. Together with q^2, this gives generic h^0(I_{C_2}(4))=6.

### The P-045 rank jump

On P-045, a=-1/2 and b=-2, and

    r = x + (d/2) z^3

(in the dx=1 normalization, r=x+(1/(2x))z^3).

Under affine coordinates for C in Q, z maps to (z,z^3). Hence the three points of R have the same second ruling coordinate: R is the intersection of C with a ruling fiber F_0.

Conversely, from

    r = x + (a+1/2)z + (1+b/2)z^2 + (d/2)z^3,

being pulled back from a linear equation in the second ruling coordinate forces a=-1/2 and b=-2.

**PROVED within the current normalization/conventions.**

    P-045 <=> R is a ruling-fiber divisor on C.

Since O_Q(1,3)|_{F_0}=O_{P^1}(1) for the relevant ruling convention, any (1,3)-section vanishing at all three points of R=C intersect F_0 must contain F_0. Hence

    H^0(I_{R/Q}(1,3)) = H^0(O_Q(1,2)),

and dim K_r=6. This gives a geometric explanation of the source jump at P-045.

## 4. The second-order target is supported on 2R

For the primitive triple,

    I_{C_2/C_3} = L^2 = O(-10).

Twisting by O_C(4)=O(16) gives O(6), hence

    0 -> I_{C_3}(4) -> I_{C_2}(4) --rho--> O_C(6).

The unique quadric satisfies intrinsically

    rho(q^2)=r^2.

Therefore, after quotienting by q^2,

    bar-rho: K_r -> H^0(O(6))/<r^2>.

Because div(r^2)=2R,

    0 -> O_C --r^2--> O_C(6) -> O_{2R}(6) -> 0,

and H^1(O_C)=0, so

    H^0(O(6))/<r^2> = H^0(O_{2R}(6)).

**PROVED.** The essential second-order map is

    bar-rho: K_r -> H^0(O_{2R}(6)).

For reduced R=p_1+p_2+p_3, the six-dimensional target decomposes locally as three length-two contributions. Thus the second-order obstruction is localized at the three points where the primitive and quadric conormal directions meet.

## 5. Local normal form for the second-order condition

This subsection records the local derivation; signs depend on choices of local generators, but the structural content does not.

Choose local coordinates near p in R:
- u along C,
- v normal to C inside Q,
- w an equation for Q.

Then I_C=(v,w). Normalize the primitive quotient locally so that, to first order,

    v |-> epsilon,    w |-> r epsilon.

Write the canonical triple as

    v = epsilon + alpha epsilon^2,
    w = r epsilon + beta epsilon^2  mod epsilon^3,

and set kappa=beta-r alpha.

A quartic containing C_2 has local expansion

    F = h(w-rv) + 1/2(A v^2 + 2Bvw + Cw^2) + O(I_C^3).

Substitution gives

    rho(F) = h kappa + 1/2(A+2Br+Cr^2),

and modulo r^2,

    bar-rho(F) = [h kappa + A/2 + Br]_{2R}.

Restricting F to Q, write F|_Q=v d_h, where d_h=0 is the residual (1,3)-divisor D_h. Then locally

    d_h = -rh + (A/2)v + ...

At a simple p in R, if u=r is used as local parameter,

    partial_u d_h(p) = -h(p),
    partial_v d_h(p) = A(p)/2.

Thus the value component of bar-rho(F)|_{2p} prescribes a relation between the tangent and transverse derivatives of D_h at p:

    partial_v d_h(p) - kappa(p) partial_u d_h(p) = 0

up to the sign convention for kappa.

**PROVED LOCALLY, subject to the stated generator/sign conventions.** One of the two new conditions at each p in R is a prescribed tangent-direction/contact condition for D_h.

The second coefficient modulo r^2 involves a second jet of d_h, not merely its first jet. Therefore it is premature to identify all six new conditions with containment of three fixed doubled points in Q.

## 6. Condition count and the P-045 degeneration

The vector space H^0(O_Q(1,3)) has dimension 8.

For general R, requiring D to contain R imposes 3 independent conditions, leaving 8-3=5, namely K_r.

Passing from C_2 to C_3 asks for two further local conditions at each of the three points, encoded by

    bar-rho: K_r -> H^0(O_{2R}(6)),

whose target has dimension 6.

Hence the naive total is

    3 + 6 = 9

conditions on an 8-dimensional vector space.

**INTERPRETATION, not by itself a proof of nonexistence.** Generic quartic incidence is overdetermined. Survival requires dependencies among the point/jet conditions.

**EXACT COMPUTATIONAL EVIDENCE from the existing verifier.**
- Generically dim K_r=5 and bar-rho is injective, so no quartic contains C_3.
- At P-045, dim K_r=6, the corresponding second-order rank drops to 3, and the full kernel H^0(I_{C_3}(4)) has dimension 4.
- Those four quartics are exactly the multiples H_x H^0(O(1)) of the survivor cubic, so they do not provide genuine irreducible quartic carriers.

The ruling-fiber geometry explains the first jump:

    R=C intersect F_0
      => D=F_0+D', D' in |O_Q(1,2)|.

It is a strong geometric candidate for explaining the second-order rank collapse as well, but a complete intrinsic proof of that rank collapse has not yet been written.

## 7. Immediate open problem for the C_0 program

The desired implication remains

    P-044 + H^0(I_{C_3}(4)) != 0
      => R is a ruling-fiber divisor,

or an equivalent statement implying P-045.

If established, the existing P-045 analysis then shows all quartics through C_3 are cubic multiples, killing genuine quartic carriers in the surviving (4,7), e=2 branch.

The next conceptual test is to understand whether P-044 (extension C_3 -> C_4) can itself be localized at R and compared directly with the contact conditions above. If that fails to simplify, a small targeted exact calculation of the combined degeneracy locus is justified; a broad Groebner/saturation attack should remain fallback.

---

# Part II. Proposed general STCI jet-budget program

## 8. Successive jet maps for primitive multiple structures

Let C in P^3 be a smooth integral curve and suppose a primitive multiple structure has filtration

    C=C_1 subset C_2 subset ... subset C_m

with conormal line L and

    I_{C_k/C_{k+1}} = L^k.

For a degree-a hypersurface, each step gives

    0 -> I_{C_{k+1}}(a) -> I_{C_k}(a) -> L^k(a),

and hence a natural map

    rho_k: H^0(I_{C_k}(a)) -> H^0(L^k(a)).

A degree-a hypersurface containing C_m must survive all successive maps.

Define

    s_k = h^0(I_{C_k}(a)),
    c_k = rank(rho_k).

Then s_{k+1}=s_k-c_k. The basic regimes are:

    s_k > c_k : survival dimensionally expected;
    s_k = c_k : borderline/determinantal;
    s_k < c_k : survival requires rank degeneracy.

This is only a bookkeeping principle until the maps and their dependencies are understood geometrically.

## 9. Why this may interact with STCI degree growth

For a primitive complete intersection of surfaces of degrees a,b supported on a degree-d curve, the multiplicity is

    m = ab/d.

Thus increasing carrier degrees has competing effects:
1. it increases the number of available hypersurface sections;
2. it also increases the required multiplicity, hence the number of infinitesimal layers that must be survived.

The relevant comparison is therefore not a single Hilbert-function count. It is the cumulative loss from the successive ranks (or a more invariant replacement accounting for the changing domains) against the initial carrier freedom.

A naive sum of h^0(L^k(a)) is not sufficient: targets can vanish, maps need not be surjective, and dependencies can be forced by geometry. The C_0 ruling-fiber phenomenon is precisely an example where the geometry of the conormal data changes the rank.

## 10. Candidate general principle

**HEURISTIC / RESEARCH PROGRAM.** Define an expected jet budget for candidate carrier data by comparing available hypersurface freedom with the ranks expected from the successive maps rho_k.

Negative expected budget should not be interpreted as an automatic obstruction. Rather:

> When the expected jet budget is negative, existence of a carrier forces the conormal/multiple-structure data into degeneracy loci of the successive jet maps.

The useful theorem would therefore have the form

    negative expected jet budget
      => STCI only on specified geometric degeneracy loci.

The substantive problem is to describe those degeneracy loci geometrically.

This suggests a possible division:
- underdetermined cases: carrier freedom exceeds the independent jet conditions, so survival is dimensionally plausible;
- overdetermined cases: STCI requires special geometric dependencies among the jet conditions.

Known STCI examples should eventually be tested against this distinction.

## 11. Why C_0 is a useful laboratory

The present quartic calculation exhibits the proposed mechanism concretely:

    primitive quotient
      -> R
      -> K_r
      -> localized jet conditions
      -> overdetermination.

The exceptional rank-drop locus has a recognizable geometric feature:

    R = C intersect ruling fiber.

Thus C_0 offers a test of whether algebraic rank-degeneracy loci of successive jet maps systematically admit geometric descriptions. That question should be answered here before attempting a broad abstraction.

## 12. Status summary

### PROVED / structurally established
- The codimension-three first-normal obstruction is H^1(O_Q(-2,2)).
- The cubic r compares the quadric conormal direction with the primitive conormal quotient.
- M = O(-6)(-R).
- K_r = H^0(I_{R/Q}(1,3)).
- P-045 corresponds to R being a ruling-fiber divisor (within the current normalization).
- The essential second-order target is H^0(O_{2R}(6)).
- Locally, one component at each p in R is a prescribed first-order contact direction; the other involves a second jet.

### EXACT COMPUTATIONAL EVIDENCE already present in the repository
- Generic quartic incidence at C_3 is empty.
- At P-045 the source and second-order ranks jump as recorded above.
- The resulting quartics through C_3 are cubic multiples, not genuine carriers.

### OPEN
- Give a fully intrinsic description of the second local condition at each point of R.
- Explain the P-045 second-order rank collapse geometrically.
- Prove or disprove P-044 + H^0(I_{C_3}(4)) != 0 => R ruling fiber.
- Determine whether P-044 localizes naturally at R.
- Formulate a correct general jet-budget invariant and test it on known STCI/non-STCI examples before treating it as a general obstruction theory.


---

## Consolidation status (2026-10-28)

This historical note remains a source for the geometric derivations and should not be deleted merely because its original research agenda was superseded. The current [jet geometry](../results/jet_geometry.md) and [order-one result](../results/order_one.md) summarize the structural claims. The complete [quartic-carrier theorem](../results/quartic_carrier_exclusion.md) supersedes *all* open quartic-mate status labels, not just the old (4,7), e=2 label. In particular, the P-044 and e=0,1 quartic-mate tasks below are not active STCI cases. Their intermediate calculations may still inform higher-degree jet questions. No historical computation was independently rerun in this consolidation.
