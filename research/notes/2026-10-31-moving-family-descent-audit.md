# Independent audit of the moving primitive control

Date: 2026-10-31. Reviewer: independent mathematical audit worker.
Scope: [the moving-family proposal](2026-10-31-moving-family-descent.md),
equations (3)–(13) and its proposition for every integer `m≥2`, for the
fixed quartic over an algebraically closed field of characteristic zero.
Status: **the stated diagnostic construction is supported; no material
correction required; reviewed provisional evidence, no canonical promotion**.

This review reconstructs the construction from its equations. It does not
use the conclusions about arbitrary hypothetical STCI pairs in
[the separate tropical-descent note](2026-10-31-tropical-descent.md) as
authority for the new formulas. In particular, its general movement theorem
is unnecessary here. The two-divisor observation at the end of proposal §5
is a separately identified application of that note's lemma, rather than a
new input to the present proof.

## 1. Global carrier and its multiples

Substitution of the parametrization into
`F=x0²x2−x1³+x2³−x1x3²` makes each of its two displayed binomials zero.
For a simultaneous zero of its partial derivatives, `x0x2=0` together
with `x0²+3x2²=0` forces `x0=x2=0`; `x1x3=0` together with
`3x1²+x3²=0` forces `x1=x3=0`. Thus the carrier is globally smooth,
including both endpoints. Since the embedded curve is smooth on this
surface, it is Cartier. The ideal sheaf `(F)+I_C^m` therefore defines
exactly its Cartier multiple `mC`, locally `(f,y^m)`, for every `m≥2`.
There is no hidden reduced residual curve or embedded punctual component.

On the cubic `K_S=−H`, `H·C=4`, and adjunction gives `C²=2`. The
successive nilpotent layers are `O_P1(−2i)` for `0≤i<m`, so
`deg Z_m=4m`, `χ(O_Z_m)=2m−m²`, and `p_a(Z_m)=(m−1)²` follow by
additivity. This calculation uses the actual Cartier multiple, with no
assumption that it is a homogeneous scheme complete intersection.

## 2. Full closure and positive movement

Direct expansion gives `φ*F=t³f0`, with
`f0=U+t⁶(u³−v²)`, and `f∞=τ⁶f0`. These equations define one global
Cartier divisor of class `O_P1(6)` on `P1×Gm²`. Its relative gradient
along the section is `(1+3t⁶,−2t⁶)` at finite points and `(3,−2)` at
infinity, so it is smooth over the base near the entire section. Thus the
section has a Cartier multiple there, locally
`(f,(U,V)^m)`, whose fibers have algebra `k[w]/(w^m)`.

Locally the multiple has a filtration by line bundles on the section.
It is finite flat of rank `m`: finiteness follows also from containment
in the fixed order-`m` normal neighborhood, and flatness follows from
the local smooth surface coordinate. In particular, no endpoint base
parameter is a zero divisor. On the punctured base this multiple equals
the inverse image of `Z_m`; contracting that ideal back to an endpoint
changes nothing because the quotient has no parameter torsion. This
proves equality with the **full scheme-theoretic closure**, independently
of a presentation by selected divided equations.

The conormal sequence of the section in this surface is exactly

```
0 → O(−6) → O² → M → 0,
       1 ↦ (s⁶+3t⁶,−2t⁶).
```

The two entries have no common projective zero. Consequently `M=O(6)`;
the layers of the rank-`m` algebra are `M^i`. Its degree is
`e=6 sum(i, i=0,…,m−1)=3m(m−1)` without requiring a global splitting
of its algebra. The quotient direction is represented by
`[2t⁶:s⁶+3t⁶]`, a nonconstant map of degree six. Thus the embedded family
really moves although the abstract punctual algebra of each fiber is
unchanged. For `m≥2` this movement is already detected by the double
structure.

## 3. Exact contractions at both endpoints

At zero take the actual coordinate `t=x1/x0` and transverse coordinates
`A=x2/x0−t³`, `B=x3/x0−t⁴`. Expansion gives

```
F/x0³=(1+3t⁶)A−2t⁵B+3t³A²+A³−tB².
```

Over `R=k[[t]]` the coefficient `1+3t⁶` is invertible. Formal implicit
elimination gives `A=h(t,B)`, with `h(t,0)=0`; modulo `B^m` the series
in `B` truncates, so the completed downstairs ring is exactly
`R[B]/(B^m)`. The upstairs equation similarly eliminates `U` in `V`.
The actual map sends `B` to `t⁴V` and `A` to `t³U`. Substitution in the
same equation shows `t³U=h(t,t⁴V)`, with coefficients in `R`; adjoining
it adds no element. Hence the full image is exactly

```
A0=R[t⁴V] ⊂ B0=R[V]/(V^m).
```

Injectivity and the exact index follow from the respective free bases
`t^(4j)V^j` and `V^j`, `0≤j<m`; their cokernel is the direct sum of
`R/(t^(4j))`. Thus `δ0=4 binom(m,2)`. This is an equality for the
complete local algebras in every multiplicity, rather than a first-order
or generic approximation.

At infinity the corrected coordinates must all be retained:

```
z=x2/x3=τu/v,
1+U'=v²/u³,   1+V'=v³/u⁴.
```

The exponent matrix `((-3,2),(-4,3))` has determinant `−1`, so this
is an invertible torus coordinate change; replacing `τ` by `z=τu/v`
also gives an invertible ambient coordinate change near the endpoint.
Its transverse ideal is therefore still the full section ideal, and
its `m`th power is preserved. This verifies the change for all nilpotent
orders, including the mixing of base and transverse coordinates.

With `X=x1/x3−z³` and `Y=x0/x3−z⁴`, direct expansion gives

```
F/x3³=−(1+3z⁶)X+2z⁵Y−3z³X²−X³+zY².
```

Implicit elimination of `X`, using the invertible coefficient
`−(1+3z⁶)`, repeats the complete argument with the **actual** base
parameter `z`. Thus
`A∞=k[[z]][z⁴V'] ⊂ B∞=k[[z]][V']/(V'^m)` and
`δ∞=4 binom(m,2)`. Replacing `z` by `τ` without this coordinate change
would not establish the claimed actual endpoint algebra.

The map from `W_m` is finite because `W_m` is proper and has finite
topological fibers. It is an isomorphism on the interior. The completed
endpoint injections above prove that its scheme-theoretic image is
exactly `Z_m`; completion is faithfully flat for these local rings.
Both endpoint images are primitive locally complete intersections and
therefore Gorenstein. The conormal comparison has zero divisor
`4p0+4p∞`: it changes `O(−2)` downstairs into `O(6)` upstairs.
The higher-layer indices are its successive multiples. As an independent
numerical consistency check,

```
χ(O_W_m)−χ(O_Z_m)
= (m+3m(m−1))−(2m−m²)
= 4m(m−1) = δ0+δ∞.
```

## 4. Failure of a homogeneous two-equation presentation

The curve has no linear equation. Among its ten degree-two monomials,
the parametrized exponent sums are all distinct except the collision
`0+4=1+3`; hence its quadric ideal is exactly the span of
`q=x0x3−x1x2`. In the zero chart `q=B−tA`. Its normal linear form is
independent of that of `F` over `k(t)`, since their determinant is
`1+t⁶`. Therefore `q` has order exactly one on `C` in `S`, and cannot
vanish on any `Z_m` with `m≥2`. The least degree of a homogeneous
equation of `Z_m` is consequently three.

A homogeneous scheme complete intersection of degrees `a≤b` has
saturated ideal generated in those degrees, forcing `a=3` here.
Its degree gives `3b=4m`; its genus gives
`(m−1)²=1+3b(b−1)/2`, or `m=2b` after using the degree equality.
These relations force `b=0`, contradicting positive defining degrees.
This excludes every homogeneous scheme CI presentation of this exact
image, for all `m≥2`, independently of the inherited low-degree STCI
exclusions.

## 5. Source check, scope, and remaining question

The linked primary source
[Bănică–Forster, §§2.1–2.3](https://www.mathematik.uni-muenchen.de/~forster/eprints/multip_struct.pdf)
was inspected directly: it supplies the primitive local model,
line-bundle filtration and reduced-curve dualizing restriction cited in
the proposal. The algebraic arguments above derive the facts needed
here directly, so the paper's primarily analytic setup introduces no
unproved field-extension assertion into this construction.

The polynomial expansions, smoothness, all-`m` elimination, line degrees,
and degree/genus contradiction were reconstructed by hand. No inherited
proof or certificate was rerun. An optional computer-algebra expansion
check could not start because the system Python lacks SymPy; no successful
CAS check is claimed. This does not affect the exact displayed expansions
or the general elimination proof.

Geometrically the example exhibits a smooth global carrier whose
thickened section acquires positive conormal degree after undoing the
endpoint normal contractions. Each contracted image remains primitive;
endpoint Gorensteinness does not remove this movement. Thus local CI
structure, curvilinear fibers, positive movement and these two Gorenstein
endpoint contractions can coexist in every multiplicity. They cannot
alone establish the proposed general contradiction. The additional
homogeneous generator condition fails for this image, as proved above.

This is a control for the general STCI investigation, not a hypothetical
STCI pair or an obstruction to all such pairs. No claim that a different
moving family has, or cannot have, the required global homogeneous
generators follows. The unrestricted characteristic-zero STCI problem
remains open. No canonical result or navigation state is promoted by
this audit.
