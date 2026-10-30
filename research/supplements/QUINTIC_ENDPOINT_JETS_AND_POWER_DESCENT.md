# Quintic endpoint: transverse jets and algebraic power descent

Complete mathematical derivations of the transverse-jet obstruction, its all-positive-power form, and the distinction between algebra membership and weaker equalizer tests. All original hypotheses and limitations remain in the proofs below.

---

## 1. quintic endpoint a b zero jet obstruction

# Endpoint a=b=0: a generic-line differential excludes every mate power

Date: 2026-10-11. Author: root.

Status: **DIRECT ALL-POWER PROOF; independent audit requested**. Work over
an algebraically closed field of characteristic zero. This note concerns
the a=b=0 boundary of the endpoint projection family, with arbitrary g,d.
It does not cover the nonendpoint modulus, the a!=0 family, or all quintic
normalizations. No mathematical execution is claimed here.

## 1. Imported geometric scope

Use the [quintic structural frontier](2026-10-11-session-quintic-structural-frontier.md),
its [independent audit](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md),
the [intrinsic pair classification](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md)
and the [explicit-model audit](2026-10-11-session-dp5-a4-explicit-model-independent-audit.md).
These give the normal degree-five del Pezzo surface S, its single A4
singularity, the lifted curve c, and the unique line ell. In anticanonical
coordinates put

    U0=Z5, U1=Z4, U2=Z3, U3=-Z1, U4=Z0-Z1,
    h=Z2+Z3, Q=h^5/U0 in H0(S,4H), div(Q)=5c.

Every hypothetical mate in this lane has degree 4k for k a positive
integer, and its pullback is a nonzero scalar multiple of Q^k. The global
all-quartic exclusion already makes k>=2, but the obstruction below
works for every k>=1. The normalized endpoint projection with a=b=0 is

    X0=U0, X1=U1, X2=U3+g h, X3=U4+d h.

Only projections whose line center avoids S need be considered. Such a
projection is finite birational onto an integral quintic hypersurface.
For the argument below, the map is defined near every generic point of
ell regardless of g,d, since X2=-1 there in the displayed chart.

## 2. A genuine smooth chart at the generic point of ell

The fourth blowup chart in the explicit-model audit has smooth coordinates
(x,r) and anticanonical section vector

    Z=(r, 1+xr, x^2(1+xr)^2, x(1+xr),
       x^3(1+xr)^2, x^5(1+xr)^3).

The strict ell is x=0; the blowup map to S is an isomorphism near its
generic point. The exceptional A4 chain meets ell at only one closed
point and therefore does not affect this generic smooth chart. With
B=1+xr and C=1+x+x^2r, the exact sections in this trivialization are

    h=x B C,
    X0=x^5 B^3,
    X1=x^3 B^2,
    X2=B(-1+g x C),
    X3=r-B+d x B C,
    Q=B^2 C^5.

The last equality follows from the actual section quotient h^5/U0,
not from a guess at its vanishing order. In particular Q restricts to
one along x=0 and is a unit at the generic point of ell.

## 3. The map has a transverse differential kernel

Use the actual downstairs affine patch X2!=0. Its three coordinate
functions pull back to

    Y0=X0/X2, Y1=X1/X2, Y3=X3/X2.

Modulo x^2 their exact expansions give

    Y0=0 mod x^2, Y1=0 mod x^2,
    Y3=1-r+A(r)x mod x^2,
    A(r)=r^2-g r+g-d.

Thus at the generic point of ell the differential has rank exactly one:
the r derivative of Y3 is -1, while both first derivatives of Y0,Y1
are zero. Over its residue field k(r), the transverse tangent vector

    v=partial_x+A(r) partial_r

annihilates the differential of all three downstairs coordinates. Every
regular function pulled back from the downstairs affine patch has
differential zero on v, by the chain rule. This remains true on any
singular image hypersurface: it is a statement about the actual morphism
to affine three-space, not a smoothness hypothesis on X.

## 4. The actual degree-four section has a nonzero transverse jet

Trivialize the pullback of O_X(4) by the actual coordinate X2^4. The
local function associated to Q is

    q=Q/X2^4=B^(-2) C^5 (-1+g x C)^(-4).

The inverse factors are units near the generic point of ell. Expanding
only their first order, with no omitted higher-order assertion, gives

    q=1+(5-2r+4g)x mod x^2.

Therefore q|ell=1, partial_r(q)|ell=0, and

    v(q)|ell=5-2r+4g,
    v(q^k)|ell=k(5-2r+4g).

For every fixed g and every positive integer k, this is a nonzero element
of k(r): the r coefficient is -2k, which is nonzero in characteristic
zero. It is immaterial that the expression can vanish at one closed
point of ell; it does not vanish at the generic point.

If a mate G of degree 4k existed, then in the patch X2!=0 its regular
function G/X2^(4k) would pull back to a nonzero scalar multiple of q^k.
Section 3 makes the differential of that function zero on v, whereas
the displayed identity makes it nonzero. This contradiction proves:

**Every admissible endpoint projection with a=b=0, for all g,d, admits
no mate in any positive degree.**

## 5. Why this is an all-power obstruction, and the retained boundary

The argument detects one actual necessary differential for a descended
section. It does not infer a bound on higher contact multiplicities from
first-normal data. The nonzero unit value q|ell=1 and characteristic zero
make the same obstruction persist under every power, by the exact chain
rule. No reduced, flat, Gorenstein or ordinary conductor-cover hypothesis
is used. No tensor-equalizer sufficiency is asserted.

The separate [a=0,b!=0 support proof](2026-10-11-session-quintic-endpoint-a0-support-exclusion.md)
and its [completed independent audit](2026-10-11-session-quintic-endpoint-a0-polynomial-support-independent-audit.md)
treat the other a=0 boundary. Combining them after this note is audited
would close the entire a=0 endpoint family. The a!=0 common-root support
problem and the extra nonendpoint modulus remain separate.


---

## 2. quintic endpoint a0 b0 power jet independent audit

# Endpoint a=b=0: independent all-power descent obstruction audit

Date: 2026-10-11. Owner: `oct11_quartic_assembly_audit`.

Status: **PROVED HERE / INDEPENDENT DIRECT PROOF AUDIT PASSES**, within
the explicit scope below. The proof is the displayed derivation, rather
than agreement among agents. A separate exact coefficient record is
supporting verification and does not establish the imported geometry.

Scope: the fixed smooth rational quartic
`C0=[s^4:s^3t:st^3:t^4]` over an algebraically closed field of
characteristic zero, the degree-five A4 del Pezzo normalization lane,
and the endpoint projection parameters `a=b=0`, with arbitrary `g,d`.
Every admissible projection in this parameter stratum has no ambient
mate in any positive degree. This does not exclude all quintic carriers,
the nonendpoint projection centers, or the endpoint `a!=0` stratum.
The universal STCI problem remains open.

## 1. Actual sources and the precise antecedents

The owner proof audited is
[the a=b=0 jet-obstruction proof](2026-10-11-session-quintic-endpoint-a-b-zero-jet-obstruction.md).
The geometric antecedents were read in the actual saved
[quintic structural frontier](2026-10-11-session-quintic-structural-frontier.md),
[independent conormal and del Pezzo audit](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md),
[intrinsic pair classification](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md),
and [explicit-model independent audit](2026-10-11-session-dp5-a4-explicit-model-independent-audit.md).
In particular:

* `S` is the normal degree-five del Pezzo surface with a single A4 point;
  `M -> S` is its minimal resolution and `L=-K_M` is the pullback of `H`.
* The actual lifted curve `c` and unique line `ell` obey
  `div(h)=c+ell`, `div(U0)=5ell`, and
  `Q=h^5/U0` is a regular section of `4H` with actual divisor `5c`.
* A hypothetical mate of an integral quintic containing this `C0`
  has full reduced inverse support `c`. Its pulled divisor is `m c`.
  Intersecting with `H` gives `5b=4m`, hence `b=4k,m=5k` for an integer
  `k>0`. Therefore its pulled section equals `lambda Q^k` for a nonzero
  scalar `lambda`: their ratio has no zeros or poles on the normal
  proper integral surface `S`, hence is a global constant.
* The actual endpoint family has four coordinates
  `X0=U0+a h`, `X1=U1+b h`, `X2=U3+g h`, `X3=U4+d h`.
  Here only its `a=b=0` stratum is treated. A projection qualifying as
  a quintic normalization has its center disjoint from `S` and is finite
  birational onto the quintic image.

The mate implication is therefore an actual global section implication,
not a conclusion based only on numerical divisor equivalence. The
all-quartic exclusion would already force `k>=2`, but the proof below
works for every `k>0` and does not use that exclusion.

## 2. The fourth blowup chart and section scaling

The explicit-model audit, section 2, gives after the fourth blowup the
actual anticanonical section vector

    Z=(r, 1+xr, x^2(1+xr)^2, x(1+xr),
       x^3(1+xr)^2, x^5(1+xr)^3).

Here `r` denotes the fourth blowup coordinate `u4`. It is not the affine
parameter `x_plane/y_plane` used on the separate dense `y_plane!=0`
chart. The common exceptional factors have already been removed in
this vector, so all six entries use one actual local trivialization of
`L`. Write

    B=1+xr, C=1+x+x^2r.

With the saved linear change `U0=Z5,U1=Z4,U3=-Z1,U4=Z0-Z1` and
`h=Z2+Z3`, direct substitution gives

    h=x B C, U0=x^5 B^3, U1=x^3 B^2,
    X2=B(-1+g x C), X3=r-B+d x B C,
    Q=h^5/U0=B^2 C^5.

Thus the formula for `Q` is the local expression of the actual section
`h^5/U0` in the fourth tensor power of this trivialization. It is not
a quotient of incorrectly rescaled affine coordinates. In particular
its value is one on `x=0`.

The strict line `ell#` is `x=0`, with anticanonical image
`[r:1:0:0:0:0]`. The contracted A4 chain meets it only at its other,
infinite point. Consequently the resolution is an isomorphism near
the generic point of this displayed line. It is valid to use `(x,r)`
as smooth coordinates on `S` there. Along `x=0`, `X2=-1` for every
`g,d`. There is no projection base point in this chart on `ell`, and
the downstairs affine patch `X2!=0` and all the inverse factors below
are valid at its generic point.

## 3. The exact transverse kernel annihilates the downstairs ring

Let `Y0=X0/X2`, `Y1=X1/X2`, `Y3=X3/X2` be coordinates of the target
affine three-space. Calculation modulo `x^2` gives

    Y0=0 mod x^2, Y1=0 mod x^2,
    Y3=1-r+A(r)x mod x^2,
    A(r)=r^2-g r+g-d.

Indeed `X2|ell=-1`, `partial_x X2|ell=-r+g`,
`X3|ell=r-1`, and `partial_x X3|ell=-r+d`, so the quotient rule gives

    partial_x Y3|ell
      =r-d+(r-1)r-(r-1)g
      =r^2-g r+g-d.

The other two target coordinates vanish to orders five and three,
respectively. Their two first derivatives vanish along `ell`. The
`r` derivative of `Y3` is `-1`. The differential of the actual map
therefore has rank exactly one over the residue field `k(r)`.

Define the `k`-derivation at this generic point by

    D(f)=(partial_x f+A(r) partial_r f)|x=0.

It has a nonzero transverse coefficient and satisfies
`D(Y0)=D(Y1)=D(Y3)=0`. For every polynomial in these target coordinates,
the chain rule gives zero. For a regular function represented as a
quotient of such polynomials with denominator nonvanishing at the
image generic point, the quotient rule gives zero as well. Hence `D`
annihilates the full downstairs local ring pulled back to `S`.

This is valid even when the image hypersurface is singular. The
downstairs ring is a quotient/localization of the coordinate ring of
the target affine three-space; no tangent-rank conclusion requiring a
smooth image has been imported. Nor is `D` asserted to be a kernel
vector field away from `ell`: the derivation at its generic point is
all that is needed.

Although `r=1-Y3` on the reduced line, their extensions into this
smooth surface chart differ by `x A(r)` modulo `x^2`. Thus `D(r)=A(r)`
does not contradict `D(1-Y3)=0`. The obstruction concerns source
functions with their actual transverse extensions, not only their
restrictions to the reduced line.

## 4. Every positive power of the actual section violates that kernel

The degree-four section is trivialized downstairs by `X2^4`. Its
actual normalized function upstairs is

    q=Q/X2^4=B^(-2) C^5 (-1+g x C)^(-4).

Because `B=1+rx`, `C=1+x mod x^2` and
`(-1+g x C)^(-4)=1+4g x mod x^2`, this is

    q=1+(5-2r+4g)x mod x^2.

It follows that `q|ell=1`, `partial_r q|ell=0`, and

    D(q)=5-2r+4g,
    D(q^k)=k q^(k-1)|ell D(q)=k(5-2r+4g).

For any fixed `g` and every positive integer `k`, this is a nonzero
element of `k(r)` in characteristic zero, since its `r` coefficient is
`-2k`. Its possible vanishing at one closed point does not make it
zero at the generic point. The parameter `d` affects the kernel's
tangential coefficient but disappears from this test because `q`
restricts to the constant one on `ell`.

Suppose an ambient mate polynomial `G` of degree `4k` existed. The
downstairs affine function

    G/X2^(4k)=G(Y0,Y1,1,Y3)

is a polynomial in the actual target coordinates, and its pullback is
`lambda q^k` by the global section implication in section 1. Section 3
forces its derivative under `D` to be zero. Section 4 makes that
derivative `lambda k(5-2r+4g)`, which is nonzero. This contradiction
excludes every mate in every positive degree.

## 5. Audit verdict and continuation boundary

The saved owner argument has no gap in its source-section scaling,
rank/kernel computation, generic-point regularity, or all-mate
implication within the stated antecedents. It supplies a necessary
descent obstruction at one actual smooth normalization chart. No
reduced/flat conductor-cover assumption, conductor sufficiency test,
or bound on later contact multiplicities is used. The use of a first
jet is sufficient here for all powers because the tested function is
a unit with constant restriction, so the exact power rule preserves
its nonzero transverse derivative. Characteristic zero is essential
to this all-positive-integer claim.

The separate
[a=0,b!=0 support proof](2026-10-11-session-quintic-endpoint-a0-support-exclusion.md)
and its
[completed independent polynomial-support audit](2026-10-11-session-quintic-endpoint-a0-polynomial-support-independent-audit.md)
exclude the rest of the `a=0` endpoint stratum. Combining these actual
proofs closes the entire `a=0` endpoint family. The endpoint `a!=0`
common-root/contact problem, nonendpoint modulus, and other quintic
normalization strata remain open. This audit changes none of the
frozen antecedent notes or canonical records.

## 6. Supporting exact record and source snapshots

The separate
[coefficient audit](2026-10-11-session-quintic-endpoint-abzero-first-jet-independent-audit.md)
has SHA-256
`635c7b30c4fae36ad10f7bb0804f5db84c5c242499b3b238b6b5c3408c60e99a`.
Its new standard-library
[source](../validation/2026-10-11-quintic-endpoint-ell-first-jet-audit/verify_first_jets.py)
and actual
[execution record](../validation/2026-10-11-quintic-endpoint-ell-first-jet-audit/execution-record.json)
were read together with both raw streams. The one mathematical run
returned exit zero and all twelve exact polynomial/first-jet conditions
over `Z[x,r,g,d]` passed. Its source SHA-256 is
`cac0df14cdeebf27f804628b8840b4a04f87d659c5f3302318f2e309d228a194`;
the interpreter was `/opt/homebrew/opt/python@3.15/bin/python3.15 -B`.
No replay or additional mathematical execution was needed for this
direct audit. The all-positive-integer conclusion comes from section 4,
not a test of finitely many powers.

The value of `q` and its derivative are evaluated in the actual
downstairs frame `X2^4`. Any alternative regular downstairs frame
differs by a downstairs unit, whose pullback `D` kills. Thus such a
permitted frame change cannot remove the nonzero derivative. An
arbitrary source unit is not an alternative downstairs trivialization.

For continuation, the following exact source snapshots were read:

| Actual source note | SHA-256 |
| --- | --- |
| Owner a=b=0 jet obstruction | `31fce973db8cfdbb223e421692739e35f1d1a8cfc69b6026ab186b0b0d761bd1` |
| Explicit-model independent audit | `f19ae25848ba77a5c59f3a9ce53819b24258c03b5d90f234b31ec7581306f8bd` |
| Quintic structural frontier | `4e84d1183435f8509df48b6b1d02fb4f00f29736ec8670bb09b2577dc991595b` |
| Quintic conormal/del Pezzo audit | `9cf5438894e3fb07f2094b4bcc1280ec0ead01822155d3897aceb73ffc1011fb` |
| Intrinsic pair classification | `537e341fb79632997648209efb7728c64229d7bd648cc2721285e8ab04cf0e0f` |

These hashes identify the read versions; the proof retains the imported
scope even if later work promotes broader geometric classifications.


---

## 3. quintic endpoint abzero first jet independent audit

# Endpoint a=b=0: fourth-blowup first jet and arbitrary-power obstruction

Date: 2026-10-11, America/New_York. Auditor:
`oct11_quartic_assembly_audit/degree_factor_audit`.
Status: **EXACT COEFFICIENT AUDIT AND DIRECT ALL-POWER DESCENT ARGUMENT**.
No canonical or frozen source was edited. This note concerns only
the endpoint projection sublane a=b=0 of the degree-five A4 model,
over an algebraically closed characteristic-zero field.

The inherited inputs are the actual coordinates and regular section
in the [explicit-model audit](2026-10-11-session-dp5-a4-explicit-model-independent-audit.md),
and the necessary normalized-mate relation in the
[quintic structural frontier](2026-10-11-session-quintic-structural-frontier.md).
Under a mate, its degree is b_mate=4k with k a positive integer,
and its normalized section is a nonzero scalar multiple of Q^k,
where Q has actual divisor 5c. No bound on k is assumed.

## 1. The actual fourth blowup chart and cancellation

Here r is the coordinate u4 of the fourth blowup chart, not the
earlier affine parameter x/y on c. Put

    w=1+xr, z=1+xw=1+x+x^2r.

The exact transformed anticanonical sections are

    Z0=r, Z1=w, Z2=x^2w^2,
    Z3=xw, Z4=x^3w^2, Z5=x^5w^3.

The uncontracted line ell is x=0. Every finite r gives a smooth
point of S on ell; its single A4 point is the point at infinity
outside this chart. The distinguished sections are

    h=Z2+Z3=xwz, U0=Z5=x^5w^3,
    U1=Z4=x^3w^2, U3=-Z1=-w, U4=Z0-Z1=r-w.

Thus cancellation in the common function field gives the entire
regular local representative

    Q=h^5/U0=w^2z^5.

This is not division by a unit at ell. The exact identity
Q*U0=h^5 and regularity of w^2z^5 identify the extended section
there; both the numerator and denominator have order five along ell.

## 2. Correct projective normalization and all first coefficients

For a=b=0 the four endpoint projection sections are

    X0=x^5w^3,
    X1=x^3w^2,
    X2=w*(-1+g*x*z),
    X3=r-w+d*x*w*z.

Along finite ell, X2=-1, so the target affine chart X2!=0 contains
this entire open line. Trivialize the actual section Q using X2^4:

    q=Q/X2^4=z^5/[w^2*(1-g*x*z)^4].

Exact differentiation gives

    q|_(x=0)=1,
    (partial_x q)|_(x=0)=5-2r+4g,
    (partial_r q)|_(x=0)=0.

For the three target coordinates y0=X0/X2, y1=X1/X2, y3=X3/X2,
the first jets are

    y0=0 mod x^2, y1=0 mod x^2,
    y3=1-r+x*(r^2-g*r+g-d) mod x^2.

In particular partial_r y3=-1 along ell. The differential of the
projection has rank exactly one there. With

    kappa(r)=r^2-g*r+g-d,
    v=partial_x+kappa(r)*partial_r,

its transverse kernel is generated by v at each finite point of ell.
Direct substitution checks v(y0)=v(y1)=v(y3)=0 along ell.

## 3. Why singular target rings create no descent loophole

Every target regular function in this affine chart is represented
locally by a fraction of polynomials in y0,y1,y3 with denominator
nonzero at the specified image point. Since v kills all three
coordinate pullbacks along ell, the Leibniz and quotient rules make
it kill the pullback of every such target regular function.
Passing to the quotient by the target hypersurface ideal does not
change this implication. The target is permitted to be singular
along the line; target smoothness is not used.

On the other hand, for every positive integer k,

    v(q^k)|ell=k*q^(k-1)*v(q)|ell
               =k*(5-2r+4g).

This is a nonzero function on the generic point of ell, because
characteristic zero makes k and 2 nonzero and its coefficient of
r is -2k. No choice of the constants g,d changes that fact.
Multiplying q^k by a nonzero scalar also preserves nonvanishing.
Thus no positive power q^k is the pullback of a target regular
function on X2!=0.

For an ambient mate G of degree 4k, the target function G/X2^(4k)
would pull back to a nonzero scalar times Q^k/X2^(4k)=q^k,
by the inherited actual divisor relation and uniqueness up to a
constant on the proper normal integral S. This contradicts the
preceding derivative calculation. Consequently the entire endpoint
a=b=0 sublane admits no mate in any positive degree, conditional
only on the already established intrinsic-model and mate-power inputs.

The proof uses an actual globally required power and its nonzero
first derivative at a unit value. It does not infer arbitrary
higher-multiplicity behavior from tangent data. In positive
characteristic a power divisible by that characteristic can kill
this derivative, so the all-power conclusion is not transferred
to that setting. The a!=0, a=0/b!=0, and nonendpoint projection
lanes are outside this coefficient audit.

## 4. Exact execution evidence

The independent standard-library
[polynomial and first-jet source](../validation/2026-10-11-quintic-endpoint-ell-first-jet-audit/verify_first_jets.py)
reconstructs the actual Z sections and passes twelve exact checks
over Z[x,r,g,d]. Its final SHA-256 is
`cac0df14cdeebf27f804628b8840b4a04f87d659c5f3302318f2e309d228a194`.
The [execution record](../validation/2026-10-11-quintic-endpoint-ell-first-jet-audit/execution-record.json)
preserves the actual exit-zero command, interpreter, elapsed time,
and source/raw-stream hashes. Its UTC timestamp falls on October 12,
which is still October 11 in the specified local timezone.

The recording wrapper is not a second mathematical verifier.
The unbounded-k conclusion is the direct Leibniz-rule proof above,
not an extrapolation from checks of finitely many powers.


---

## 4. power descent algebra audit

# Full-conductor power descent: an independent algebra audit

Date: 2026-10-11. Owner: `power_descent_algebra_audit`, child of
`oct11_quintic_power_descent`.

Status: the algebraic statements below are **PROVED HERE** with explicit
proofs. The application to the degree-five A4 del Pezzo lane uses the
recorded geometric inputs in the
[quintic structural frontier](2026-10-11-session-quintic-structural-frontier.md),
particularly the actual conductor, purity of the normalization quotient,
and `div(Q)=5c`. This note does not assert that any projection satisfies
the resulting power criterion, or exclude every quintic carrier.

## 1. Actual membership is stronger than a tensor equalizer

Let `A` be a Noetherian algebra over a characteristic-zero field, and let
`A ⊂ B` be a finite extension. In the normalization application A is an
integral domain and B its finite normalization. Let

    I = {a ∈ A : aB ⊂ A}, R=A/I, T=B/I.

The conductor I is an ideal in both A and B, and the injection R→T gives
the exact identity

    A = B ×_T R.

Indeed, if b modulo I belongs to R, choose a in A representing it;
then b−a belongs to I⊂A. Consequently

    q^k ∈ A  ⇔  (q mod I)^k ∈ R.                 (1)

No reducedness, normality of R or T, flatness, or separability of the
conductor map is needed. Fiber products and their compatibility with
localization are also recorded in
[Stacks, Section 15.5](https://stacks.math.columbia.edu/tag/08KG).

If q is a unit in T, write q1=q⊗1 and q2=1⊗q in E=T⊗_R T. Descent of
q^k implies that u=q1/q2 satisfies u^k=1 in the entire possibly nonreduced
ring E. Over an algebraically closed field, E decomposes by the mutually
orthogonal idempotents

    e_ζ = (1/k) Σ_{j=0}^{k−1} ζ^(−j) u^j,  ζ^k=1,

and on the e_ζ component one has the exact identity q1=ζq2. Thus there
is no additional nilpotent error in this necessary root-of-unity identity.

The converse tensor implication is false without further descent
hypotheses. Here is an explicit finite normalization counterexample.

    A=k[t^3,t^4] ⊂ B=k[t], I=t^6B,
    R=span_k{1,t^3,t^4} ⊂ T=k[t]/(t^6), q=1+t^5.

The conductor follows from the semigroup `<3,4>`: every integer at least
six occurs, but five does not. The element q is a unit in T. In the
tensor product T⊗_R T, with x=t⊗1 and y=1⊗t, the relations x^3=y^3 and
x^4=y^4 imply

    x^5−y^5=(x+y)(x^4−y^4)−xy(x^3−y^3)=0.

Hence q⊗1=1⊗q, and the same is true of every power. Nevertheless

    q^k = 1+k t^5  in T,

which is not in R for any positive integer k in characteristic zero.
An exact tensor equalizer test, even on the unit locus, therefore cannot
replace the actual R-subspace membership test (1).

## 2. Powering cannot repair unit nilpotent jets

Assume more generally that `R ⊂ T` is a finite extension of Noetherian
Q-algebras, and q∈T is a unit. Write Rred and Tred for their reductions.
The induced map Rred→Tred is injective: a member of R which is nilpotent
in T is already nilpotent in R.

**Unit jet lemma.** If qred belongs to Rred, then

    q^k ∈ R for one positive k  ⇔  q ∈ R.        (2)

Proof. Integrality shows that qred is a unit in Rred: an element of Rred
which becomes a unit in the integral extension Tred cannot lie in a
maximal ideal, by lying over. Choose a lift r∈R of qred. The nilradical
of R is nilpotent, so r is a unit of R. Now q/r=1+n with n in the
nilradical N of T; N is nilpotent. Finite polynomials define

    log(1+n)=n−n^2/2+n^3/3−...,
    exp(z)=1+z+z^2/2!+...,

on N, and they are inverse. If q^k∈R, then (q/r)^k∈R and

    k log(q/r)=log((q/r)^k) ∈ R.

Since k is invertible, log(q/r)∈R∩N. Taking its finite exponential gives
q/r∈R and hence q∈R. The reverse implication is immediate. This proof
retains every nilpotent layer of T; it is not a first-jet argument.

There is a useful exact reformulation. For a unit q define

    Ered={n∈Z : qred^n ∈ Rred^×}.

This is a subgroup of Z. If Ered={0}, no positive full power descends.
Otherwise write Ered=dZ with d≥1. Then the set of positive full
descending powers is either empty or precisely

    {d,2d,3d,...}.                               (3)

Indeed, a successful k has k=dm. Applying (2) to the unit q^d shows
that (q^d)^m∈R forces q^d∈R. Conversely its multiples then descend.
Thus the nilpotent structure can invalidate every reduced candidate,
but cannot force a larger multiple of the reduced minimum d to become
the first successful power.

The unit condition is essential. For A=k[t^2,t^3]⊂B=k[t], q=t does not
descend whereas every q^k with k≥2 does. Its conductor residue is
nilpotent and is not a unit.

## 3. Reduced generic phases and the unibranch bound

At a generic conductor point the actual R is Artinian local. Put
K=Rred and write

    Tred=Π_j L_j,

where each L_j/K is a finite field extension. K contains the algebraically
closed characteristic-zero ground field. For a unit tuple α=(α_j), take
all its values under all K-embeddings L_j→Kbar. A positive reduced power
descends precisely when every ratio between these finitely many geometric
values is a root of unity. If that holds, the least reduced exponent d
is the least common multiple of the orders of the ratios to one reference
value. Their common d-th power is Galois invariant, hence belongs to K.

If Tred consists of one field L, this gives a bound

    d=[K(α):K] ≤ [L:K].                          (4)

For completeness, if α^m∈K, then K(α) contains every root ζα of
X^m−α^m because all m-th roots of unity are in K. This polynomial is
separable, so K(α)/K is Galois with a cyclic group of order e. Its image
is the unique order-e subgroup of μ_m; thus α^e is fixed, and minimality
gives d=e.

No bound by the number of geometric branches exists in the split case.
For any root of unity ζ of order m, let

    A={p(t)∈k[t] : p(0)=p(1)}, B=k[t],
    I=t(t−1)B, R=k, T=k×k,
    q=1+(ζ−1)t.

This is an integral finite-type domain with finite normalization B:
t is integral over A via t^2−t−t(t−1)=0, and A=k+t(t−1)k[t]. The
conductor formula is exact because interpolation makes arbitrary pairs
of endpoint values in B. The residue of q is the unit (1,ζ), and

    q^k ∈ A  ⇔  ζ^k=1  ⇔  m divides k.

The reduced conductor has only two branches, while m is unbounded.
In a genuinely degree-two single-field generic conductor, however,
(4) bounds the candidate exponent by two. That degree-two hypothesis
must be established for the actual projection, not assumed from an
average conductor-degree calculation.

There is also a pointwise subintegral statement. Suppose q^k∈A and q
is a unit in B. If over a prime p of A all geometric residue values of
q coincide, then q belongs to A_p. To prove it, set C=A[q]. The fiber
C⊗_Aκ(p) is a quotient of κ(p)[z]/(z^k−q^k), a reduced separable
algebra because q^k is a unit. The common residue value is in κ(p)
in characteristic zero, so this fiber is κ(p). Nakayama applied to
(C/A)_p now gives C_p=A_p. The equal-residue condition is automatic
where B→A is subintegral. It fails in the split root-of-unity example.
Thus power descent forces descent of the section itself on a subintegral
unit locus, but not on every unit locus of a normalization.

## 4. Purity converts generic full membership into global descent

Let ν:S→X be a finite birational normalization of an integral surface,
and let

    M=ν_*O_S/O_X.

Assume M is pure of dimension one: it has no nonzero coherent subsheaf
supported on finitely many points. If L is invertible on X, then a global
section s of ν^*L descends to a section of L if and only if its germ
belongs to L at every generic point of Supp(M).

Proof. Its image σ in M⊗L is a global section. If its generic germs
vanish, the coherent subsheaf generated locally by σ has finite support.
Purity makes this subsheaf zero, so σ=0 and s descends. Necessity follows
from the defining exact sequence. For a one-dimensional Cohen–Macaulay
module, purity follows either from a nonzerodivisor killing no finite
length submodule, or from the absence of embedded associated primes;
the latter is [Stacks, Lemma 10.103.7](https://stacks.math.columbia.edu/tag/00N2).

It is essential that these generic tests use the full Artinian conductor
algebras, rather than only their residue fields. Purity removes an extra
obstruction supported at finitely many points only after the entire
generic obstruction has vanished. The example in section 1 fails this
full generic test.

## 5. Exact application to the quintic A4 lane

The recorded quintic inputs are

    M=ω_Γ(−H), Γ pure Cohen–Macaulay of dimension one,
    Q∈H0(S,4H), div_S(Q)=5c,
    C0 generically regular on X.

The canonical module of the Cohen–Macaulay curve Γ is maximal
Cohen–Macaulay, so M is pure. Since c is not a conductor component,
Q, after trivializing O_X(4H), is a unit at every generic conductor point.
For each such point η form the actual rings

    Rη=O_X,η / Iη  ⊂  Tη=(ν_*O_S)η / Iη,

and let dη be the minimum reduced exponent in section 3, if it exists.
Then an actual power of Q descends if and only if:

1. Every generic conductor point has a finite dη.
2. The full, possibly nonreduced membership test Q^dη ∈ Rη passes at
   every such point, in a local trivialization.

If these conditions hold, D=lcm_η(dη) is the least positive global
descending exponent, and all global descending exponents are its positive
multiples. Proof: (3) supplies the exact local exponent groups; purity
supplies sufficiency and prevents any additional isolated obstruction.

Multiplying a local trivialization by a unit from O_X,η multiplies Q by
a unit of Rη. This changes none of these exponent groups or membership
conditions. The argument concerns sections of the pullback of an actual
downstairs line bundle; a line bundle merely defined upstairs cannot be
treated this way.

For a quintic hypersurface X⊂P3, every section of O_X(4D) lifts to an
ambient homogeneous polynomial: the hypersurface sequence and
H1(P3,O(4D−5))=0 give surjectivity. If Q^D descends, its normalized divisor
is exactly 5D c, and finite surjectivity of ν shows that the resulting
ambient equation cuts X set-theoretically down to C0. Conversely the
recorded quintic structural theorem says every hypothetical mate pulls
back to a scalar Q^k. Hence these generic full-conductor tests are an
exact mate-existence criterion within this already reduced quintic lane.

This is a structural reduction, not a parameter-space solution. In
particular, the split reduced phases can still have arbitrary root-of-unity
orders as the projection varies. What is removed is a separate search over
ever larger multiples to repair generic nilpotent jets, or a search for
extra isolated descent obstructions after full generic membership succeeds.

## 6. Evidence and continuation boundary

The proofs of (1)–(4), the tensor counterexample, the pointwise statement,
and the purity criterion are direct algebraic arguments in this note;
no finite symbolic run is used as a substitute for their quantifiers.
The imported geometric inputs remain those of the linked quintic frontier.
The finite-conductor nilpotent logarithm uses characteristic zero, and is
not transferred to positive characteristic.

The next actual task is to construct Rη⊂Tη and the residue of Q for the
four-parameter projection family, with all nonreduced generic strata
retained. For a single-field component, (4) may bound its candidate power;
for split components, root-of-unity phases and their full jet compatibility
must both be examined. No projection is excluded by this note alone.
