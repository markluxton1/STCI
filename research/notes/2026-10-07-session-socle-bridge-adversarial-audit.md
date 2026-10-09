# Independent frame audit of the corrected primitive-e=1 ancestor bridge

Date: 2026-10-07. Scope: the fixed characteristic-zero curve
`C0=[s^4:s^3t:st^3:t^4]`, quartic multipliers, and the stratum
`e=1,D2=0`. Status: **PROVED CONDITIONAL ON THE ACCEPTED ANTECEDENTS**
listed below. The corrected two-target argument passes an independent
geometric audit. The old single-multiplier pole argument does not pass.
This note makes no assertion that C0 is not a set-theoretic complete
intersection or that the whole quartic ancestor incidence is empty.

## 1. Verdict, dependencies, and the rejected implication

Assume the accepted quartic-ancestor finite bound and generic-length
theorem: an ancestor with `F*alpha=u,G*alpha=v` defines a pure finite-flat
CM quadruple `Z`, generically curvilinear, with saturated pieces

```text
E1=L=O(e-7), E2=L^2(D2), E3=L^3(D3).
```

Assume also the audited socle-pencil theorem in Section 2 of
[`2026-10-06-session-localcoh-progress.md`](2026-10-06-session-localcoh-progress.md),
the complete primitive-e=1 triple directions and quartic fibres in
[`2026-10-07-session-mf6-e1-independent-audit.md`](2026-10-07-session-mf6-e1-independent-audit.md),
and P-037's all-stage exclusion of multiplier degrees at most three.
The socle theorem gives `E3=O(-14)`. Thus `e=1` means
`L=O(-6),degD3=4`.

Under these antecedents, **there is no common quartic ancestor with
`e=1,D2=0`**. The proof below uses both target equations together.

The earlier proposed bridge used the false implication that a multiplier
containing the canonical triple also vanishes in `OZ`. In fact its image
is a nonzero socle element, because its alpha-image is one of the targets.
Consequently `h*a=T*tau` cannot be used for one multiplier. The valid
equation is `h*a-T*tau=f`, retaining its actual target image `f`.
The single-multiplier cubic pole bound is therefore not an ancestor
obstruction. Its use in an actual complete-intersection quotient is a
different argument, with a different vanishing hypothesis.

## 2. The canonical triple and its actual quotient frame

Since the two targets lie in the first inverse-system socle, the images
of `F,G` in `OZ` lie in the saturated socle `E3`. One may first verify
this generically and then use the torsion-free lower filtration quotients
to extend it to every curve point. Hence both quartics contain

```text
Z3=Spec(OZ/E3).
```

When `D2=0`, multiplication `L^2 -> E2` is an isomorphism. Locally
over a completed smooth support DVR, a normal lift `ell` of a generator
of `L` has square generating `E2`. Nakayama on the three successive
rank-one pieces shows that `1,ell,ell^2` generate the canonical triple.
Its embedded transverse algebra is primitive. No curvilinear assertion
about the quadruple's special fibre is needed.

On `x0=1` the actual ambient normal coordinates are

```text
z=x1, x2=z^3+V, x3=z^4+U+3zV/2.
```

The balanced conormal coordinates satisfy to first order on the opposite
ambient chart

```text
U'=z^-7 U, V'=z^-7 V.
```

For `L=O(-6)`, write its quotient direction `U=A(z)*ell,V=B(z)*ell`
with the classified linear polynomials `A,B`. This is the actual
balanced quotient frame: a linear coefficient multiplies an `O(-6)`
frame to give the `O(-7)` normal coordinate. It is not an arbitrary
formal transverse variable.

For the principal orbit, `A=1+z,B=-2-8z`, use

```text
ell=4U/3+V/6, m=B*U-A*V.
```

On the other chart the Bezout lift is `ell'=-U'/3-V'/6`. Substituting
the quotient values gives `ell'=z^-6*ell` to first order. Likewise
`m'=(-8-2/z)U'-(1+1/z)V'=z^-8*m` to first order.
For either algebraic orbit, `A=r*z,B=1`, use `ell=V,m=U-r*z*V`.
The opposite-chart lift is `ell'=U'/r`, whose quotient value is again
`z^-6*ell`; and `m'=U'/z-r*V'=z^-8*m` to first order.
These identities are checked directly in the independent verifier.

Higher-order changes of a lift of `L` differ by saturated degree at
least two. Cubing them changes `ell^3` only in saturated degree at least
four, which is zero on the quadruple. The moving support coordinate
has its first difference from `1/z` in normal degree one; multiplying
that difference by `ell^3` is again degree at least four. Thus these
nonlinear transitions do not change the global cubic multiplication
map `L^3 -> E3`.

## 3. The target normalization and the global degree-four coefficient

The ancestor induces the isomorphism

```text
E3 -> omega_C(-3)=O(-14).
```

The isomorphism is the accepted socle-pencil theorem, rather than a
choice of a possibly meromorphic socle generator. Choose the regular
finite-chart socle frame `w` by pulling back the standard frame of
`omega_C(-3)` through this isomorphism. After twisting by the ambient
quartic, its target space is

```text
E3(4) -> omega_C(1)=O(2).
```

To verify its scalar coordinates, in the balanced normal frame

```text
q=U+zV/2, B=-z^2U+z^3V/2+V^2.
```

Their first-normal determinant is `z^3`. The restrictions of the raw
target numerators `x0*x2,x1*x3` are `z^3,z^5`; the normalized residue
coefficients are therefore exactly `1,z^2`. The same regular sections
extend at `z=0`: one computes the equality on the dense chart where the
determinant is nonzero, then uses the regular balanced residue frame
and torsion-freeness. The homogeneous pencil is `(s^2,t^2)` and has no
common zero. The raw numerators alone would give an incorrect endpoint
frame.

Multiplication gives a global line-bundle map

```text
L^3=O(-18) -> E3=O(-14).
```

Write `ell^3=tau(z)*w` on the finite chart. Then `tau` is a polynomial
of degree at most four. Explicitly, `ell'=z^-6*ell` modulo irrelevant
higher terms and `w'=z^-14*w`, so
`tau'(1/z)=z^-4*tau(z)`. Regularity at both endpoints gives the degree
bound. This is the crucial geometric constraint on the coefficient;
it cannot be assumed for an arbitrary chosen formal socle frame.

If `F0,F1` are a basis of the complete two-dimensional quartic fibre,
their alpha-images `f0,f1` lie in `span(1,z^2)` and form a basis of that
pencil: the given `F,G` are independent and their images are `u,v`.
Consequently the two images have no common projective zero.
Actual ambient torus normalization preserves this property and this
pencil, since the targets are two torus eigenvectors. Only those actual
torus transformations are used in the orbit classification.

## 4. Correct multiplier identities

In a primitive triple chart choose its regular quadratic correction
`gamma` so that `m+gamma*ell^2=0` in `OZ3`. In the quadruple write

```text
m+gamma*ell^2=a(z)*w, ell^3=tau(z)*w.
```

Both coefficients are regular on that chart. If a quartic's jet is

```text
F=h*m+gamma*h*ell^2+E*m*ell+K*ell^3+higher terms,
T=gamma*E-K,
```

then `m*ell=-gamma*ell^3`: the extra term `a*w*ell` is zero because
`E3` is annihilated by the curve ideal. Terms of saturated degree four
also vanish. Hence its actual image in `E3(4)` is

```text
f=h*a-T*tau.
```

For a basis `F0,F1`, eliminate the unrestricted local coefficient `a`:

```text
h1*f0-h0*f1=(h0*T1-h1*T0)*tau.
```

There is no assumption that either quartic annihilates `OZ`.

## 5. Principal orbit: two finite points contradict the target pencil

Put `P=4z^2+2z+1`. The accepted quartic jets give

```text
h0=P*z^3/16,
h1=P*(64z^6+8z^3+1)/1024,
h0*T1-h1*T0=(2z-1)^3*(2z+1)*P/256.
```

The determinant identity is independently recomputed from the explicit
`T0,T1`. Cancelling the nonzero polynomial `P` from the identity of
regular functions gives

```text
(64z^6+8z^3+1)*f0-64z^3*f1
    =4*(2z-1)^3*(2z+1)*tau.
```

At `z=1/2` it says `3*f0-8*f1=0`; at `z=-1/2` it says
`f0+8*f1=0`. Every section in `span(1,z^2)` has the same value at
these two points in the fixed finite-chart frame. The two linear
equations therefore force both `f0,f1` to vanish at both points.
This contradicts the basepoint-free pencil. Both points are finite,
and `P` is nonzero at them, so no endpoint or denominator issue occurs.

As a redundant stronger algebra check, the complete polynomial
coefficient system with `deg(tau)<=4` has a one-dimensional solution
space. Its target part is

```text
f0=c*(z^2-1/4), f1=(3/8)*f0.
```

It has rank one and cannot be the required target basis. The two-point
proof already supplies the contradiction without this stronger check.

## 6. Algebraic orbits: the global degrees contradict either target basis

For either root `12r^2+4r+3=0`, the accepted complete pencil has

```text
h0=1,T0=0, h1=(2r+2/3)*z^8,T1=(8r/9)*z^3.
```

Both displayed constants are nonzero. The first equation gives
`a=f0`; the second therefore reads

```text
f1=(2r+2/3)*z^8*f0-(8r/9)*z^3*tau.
```

If `f0` is nonzero its first term has degree at least eight, whereas
the second term has degree at most seven and `f1` has degree at most
two. Thus `f0=0`, already contradicting independence of the two target
images. In fact the remaining equation, with a right side divisible
by `z^3` and left side of degree at most two, forces `tau=f1=0` too.
The exact coefficient matrix has rank nine over `Q(sqrt(-2))`, confirming
the zero solution for both geometric conjugates. The degree argument
itself proves the contradiction.

## 7. Quadric-factor orbit and reproducibility

In the fourth orbit `A=-z/2,B=1`, the complete quartic fibre is
`q*H0(P3,O(2))`. Both multiplier equations then make `q*alpha` a common
ancestor with degree-two multipliers. P-037 excludes it. This is the
correct ancestor obstruction for this fibre; the STCI divisor-class
argument on the quadric is not being substituted for it.

The four primitive triple orbits are exhausted, proving the stated
conditional quartic-ancestor exclusion. Positive `D2` makes the
canonical triple defective and remains outside this argument. Other
values of `e`, multiplier degrees beyond four, and the universal STCI
question also remain outside it.

Run the independent exact frame and coefficient checks with

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/computations/audit_session_socle_bridge_frames_2026_10_07.py
```

Its source imports no other research verifier or generated JSON. It
checks the determinant-normalized targets, actual first-order quotient
frames, principal cubic determinant, two-point equations, full principal
coefficient rank and both-conjugate algebraic coefficient rank. The
durable JSON carries the source hash. These exact identities support the
geometric proof above; they do not prove the listed antecedents.
