# Quintic endpoint: transverse jets and algebraic power descent

The proof treats the actual `a=b=0` endpoint projection of the degree-five
A4 normalization in characteristic zero, with arbitrary `g,d`. It excludes
every positive mate power using one nonzero transverse derivative of the
actual global section. The
[complementary residual-support proofs](QUINTIC_ENDPOINT_RESIDUAL_SUPPORT_AND_EXCESS.md)
close `a != 0` and `a=0,b != 0`; the extra nonendpoint projection modulus
and arbitrary quintic carriers are outside this endpoint conclusion.

<a id="1-quintic-endpoint-a-b-zero-jet-obstruction"></a>
<a id="2-quintic-endpoint-a0-b0-power-jet-independent-audit"></a>
<a id="3-quintic-endpoint-abzero-first-jet-independent-audit"></a>
## The fourth-blowup all-power obstruction

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

The geometric antecedents are the full
[quintic carrier-structure proof](QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md#1-quintic-conormal-and-delpezzo-audit),
[intrinsic pair classification](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md#1-dp5-a4-intrinsic-pair-classification)
and [explicit-model proof](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md#2-dp5-a4-explicit-model-independent-audit).
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

The exact identity `Q U0=h^5` in the common function field, together
with regularity of `B^2 C^5`, identifies the extended section here; `U0`
is not a unit along `ell`, and both sides have the required order-five
cancellation. Thus the formula for `Q` is the local expression of the actual
section `h^5/U0` in the fourth tensor power of this trivialization. It is not
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
to this all-positive-integer claim: in characteristic `p`, a positive
power divisible by `p` kills this derivative, so the displayed first jet
alone does not give an all-power exclusion there.

The [complete `a=0,b!=0` support proof](QUINTIC_ENDPOINT_RESIDUAL_SUPPORT_AND_EXCESS.md#full-inverse-support-when-a-vanishes-and-b-is-nonzero)
closes the rest of the `a=0` endpoint stratum. The
[complete `a!=0` inverse-support proof](QUINTIC_ENDPOINT_RESIDUAL_SUPPORT_AND_EXCESS.md#full-inverse-support-when-a-is-nonzero)
closes the complementary endpoint stratum. The nonendpoint modulus and
other quintic normalization strata remain separate; no unrestricted
quintic-carrier theorem is asserted.

## 6. Supporting exact record and source snapshots

The independent coefficient calculation is supported by the standard-library [source](../validation/2026-10-11-quintic-endpoint-ell-first-jet-audit/verify_first_jets.py), SHA-256 `cac0df14cdeebf27f804628b8840b4a04f87d659c5f3302318f2e309d228a194`. It checks twelve polynomial/first-jet identities over `Z[x,r,g,d]`. The all-positive-integer conclusion comes from section 4, not a test of finitely many powers.

The value of `q` and its derivative are evaluated in the actual
downstairs frame `X2^4`. Any alternative regular downstairs frame
differs by a downstairs unit, whose pullback `D` kills. Thus such a
permitted frame change cannot remove the nonzero derivative. An
arbitrary source unit is not an alternative downstairs trivialization.

The original owner proof and both independent audits were compared in full
during consolidation. The retained calculation includes the nonunit
cancellation, correct downstairs frame, quotient/localization argument for
a singular target, and characteristic-zero power rule; no saved verifier
or mathematical input was removed.


---

## Full-conductor algebra and power descent

The full proof now belongs to [full conductor algebra](CONDUCTOR_DESCENT_ALGEBRA.md): actual membership via the conductor fiber product, the false tensor-equalizer counterexample, nilpotent unit-power rigidity, exact reduced phase orders, the single-field bound and split-phase counterexample, generic-to-global purity, and the exact quintic application. These are all retained with complete proofs, and the source algebra review has been reused through an independent scope-preserving consolidation review. The endpoint fourth-blowup source and coefficient derivations above remain the geometric inputs to this application.

<a id="4-power-descent-algebra-audit"></a>
The former algebra audit's full mathematical content is in that proof home, including the alternative Henselian proof and all characteristic and unit hypotheses.
