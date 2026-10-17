# Simultaneous-target repair for primitive e=1 quartic ancestors

Date: 2026-10-07. Fixed `C0` over an algebraically closed field of
characteristic zero. Status: **PROVED UNDER THE EXPLICIT ACCEPTED INPUTS;
root and independent adversarial audits accepted on 2026-10-07.** Under the already accepted socle
theorem, P-037 and complete primitive-e=1 quartic fibres, this excludes
common quartic ancestors with `e=1,D2=0`. The defective-triple stratum
`e=1,D2>0` remains open.

The original single-multiplier argument is preserved separately as
[`2026-10-07-session-localcoh-mf6-bridge.md`](2026-10-07-session-localcoh-mf6-bridge.md),
explicitly labeled **FAILED**. Its error was treating `F*alpha=u` as
`F=0` in the quadruple rather than a nonzero socle target. This repair
keeps both target equations and their independence throughout.

## 1. Primitive triple, complete fibres and rank-two targets

The accepted quartic-ancestor reduction gives a saturated finite-flat CM
quadruple `Z` whose generic transverse algebra is curvilinear of length
four, with

```text
E1=L=O(e-7), E2=L^2(D2), E3=L^3(D3).
```

Its saturated socle `E3` is an ideal, and `OZ/E3` is torsion-free over
the reduced curve. Since the images of `F,G` in `OZ` are generically
socle elements, both vanish in `OZ/E3` everywhere. They contain the
embedded canonical triple `Z3=Spec(OZ/E3)`.

If `D2=0`, a local generator `ell` of the first quotient has square
generating the second quotient. The triple then has local basis
`1,ell,ell^2` and is primitive, whether or not the quadruple has a
defective last piece. For `e=1` it has `L=O(-6)` and belongs to the four
complete actual torus orbits in
[`2026-10-07-session-mf6-e1-independent-audit.md`](2026-10-07-session-mf6-e1-independent-audit.md).
This proof uses its complete quartic fibres, rather than its individual
carrier cubic-pole bounds or its STCI mate-support argument.

Three of these fibres are two-dimensional pencils. The original
multipliers `F,G` are linearly independent because their images are the
independent classes `u,v`. Thus they form a basis of the full pencil.
For any chosen fixed basis `F0,F1`, its target images `f0,f1` must be
an invertible constant change of `u,v`, and remain a rank-two,
basepoint-free target pencil.

## 2. The global socle and normal frames

The accepted socle-pencil theorem gives the **untwisted** isomorphism

```text
alpha: E3 -> omegaC(-3)=O_P1(-14).
```

After twisting by an ambient quartic it gives

```text
alpha: E3(4) -> omegaC(1)=O_P1(2).
```

Choose the finite socle frame `w` using this isomorphism. In the first
support chart `x0=1,x1=z`, the balanced normal parameters are exactly
the ones used by MF6:

```text
V=x2-z^3, U=q-z*V/2, q=x3-z*x2.
```

The first-normal determinant of `(q,B)` relative to `(U,V)` is `z^3`.
The raw target numerators restrict to `xz=z^3` and `yw=z^5`, so their
socle coefficients are `1,z^2` after cancellation. The accepted socle
theorem verifies that this cancellation extends at the endpoints.
Therefore, in this finite frame,

```text
f0,f1 in span_k(1,z^2),
```

and together they must be a rank-two, basepoint-free basis of that
pencil. The raw numerators are not substituted for these normalized
sections.

For the principal primitive direction, use
`ell=(4/3)U+(1/6)V`; its constant Bezout relation against
`A=1+z,B=-2-8z` is one. For the algebraic directions
`A=r*z,B=1`, use `ell=V`. Hence both represent the actual finite frame
of `L=O(-6)`. On the overlap its first class transforms as
`ell_infinity=z^-6*ell`; normal terms of order at least two do not
affect its cube in a length-four algebra. The moving support-coordinate
correction also contributes only normal order at least four after
multiplication by `ell^3`. Thus

```text
ell_infinity^3=z^-18*ell^3,
w_infinity=z^-14*w,
tau_infinity=z^-4*tau,
```

where `ell^3=tau*w`. Consequently
`tau in H0(Hom(L^3,E3))=H0(O(4))` is a polynomial of degree at most
four on the finite chart.

The corrected primitive-triple normal parameter `m+gamma*ell^2` has a
regular socle coefficient `a` in `OZ`. With the accepted MF6 convention
`T=gamma*E-K`, every quartic in its complete fibre has exactly

```text
f_i=h_i*a-T_i*tau.
```

The relevant twists are `h in H0(O(8))`, `f in H0(O(2))`, and
`tau in H0(O(4))`. The corrected normal coefficient `a` and the cubic
coefficient `T` have inhomogeneous transition, so neither is assigned
an unsupported polynomial-degree bound. If the corrected normal frame
changes as `m_corr,infinity=z^-8*m_corr+rho*ell^3`, putting
`sigma=z^14*rho` gives

```text
a_infinity=z^6*a+sigma*tau,
h_infinity=z^-8*h,
T_infinity=z^2*T+z^-4*h*sigma,
f_infinity=z^-2*f.
```

These identities make the nonzero target equation glue correctly.
They do not replace it by an annihilation equation.

## 3. Principal orbit: simultaneous compatibility contradicts basepoint freedom

Put `P=4z^2+2z+1`. The complete principal pencil has

```text
h0=P*z^3/16,
h1=P*(64z^6+8z^3+1)/1024,
T0=(2z+1)*(1536z^5+1152z^4+448z^3+48z^2-24z+4),
T1=(2z+1)*(1536z^8+1152z^7+448z^6+240z^5+120z^4
           +60z^3+30z^2+15z+8).
```

Eliminating `a` from the two correct equations gives

```text
h1*f0-h0*f1=(h0*T1-h1*T0)*tau,
h0*T1-h1*T0=(2z-1)^3*(2z+1)*P/256.
```

Cancel the nonzero polynomial `P` to obtain

```text
(64z^6+8z^3+1)*f0-64z^3*f1
       =4*(2z-1)^3*(2z+1)*tau.
```

At `z=1/2` this requires `3f0(1/2)-8f1(1/2)=0`; at `z=-1/2`
it requires `f0(-1/2)+8f1(-1/2)=0`. Each `f_i` lies in
`span(1,z^2)`, so its values at these two points are equal. The two
independent relations force both targets to vanish there. This
contradicts their basepoint freedom. The principal contradiction needs
no degree bound on `tau`.

For a stronger exact coefficient check, the full remainder matrix
modulo `(2z-1)^3*(2z+1)` has rank three and kernel

```text
(f0,f1)=c*(z^2-1/4, (3/8)*(z^2-1/4)).
```

Thus it even forces the target pencil to rank at most one. Both
checks use the nonzero target terms, unlike the failed shortcut.

## 4. The two algebraic orbits: polynomial-degree contradiction

For `A=r*z,B=1,12r^2+4r+3=0`, the complete pencil has `gamma=0`
and

```text
h0=1, T0=0,
h1=(2r+2/3)*z^8, T1=(8r/9)*z^3.
```

Both scalar coefficients are units modulo the defining quadratic.
The target equations become

```text
a=f0,
f1=(2r+2/3)*z^8*f0-(8r/9)*z^3*tau.
```

The first right-hand term has degree at least eight for any nonzero
`f0`; the second has degree at most seven because `deg tau<=4`; and
`deg f1<=2`. Hence `f0=0`. The remaining right-hand term is divisible
by `z^3`, so `f1=0` as well. This contradicts target independence.
The exact quadratic-field unit checks treat both roots without generic
field-specialization inference.

## 5. The fourth orbit and exact evidence

For `A=-z/2,B=1`, the complete fibre is
`q*H0(P3,O(2))`. Hence `F=q*F2,G=q*G2`, and

```text
F2*(q*alpha)=u, G2*(q*alpha)=v.
```

This is a degree-two common ancestor, forbidden by the all-stage P-037
theorem. It is the ancestor-specific quadric-factor argument, with no
STCI mate assumption.

The independent exact coefficient verifier is
[`verify_session_localcoh_e1_simultaneous_2026_10_07.py`](../computations/verify_session_localcoh_e1_simultaneous_2026_10_07.py).
It reconstructs the determinant and target remainder matrix from the
displayed accepted pencil coefficients, checks both simple evaluations
and the complete rank-three constraint, and verifies the scalar units
and all forcing degree coefficients over the exact algebraic field.
Its JSON states the required geometric inputs explicitly. Script
agreement is not a substitute for the frame argument in Section 2.

The root independently verified both simultaneous contradictions. The
separate frame audit
[`2026-10-07-session-socle-bridge-adversarial-audit.md`](2026-10-07-session-socle-bridge-adversarial-audit.md)
accepted the global socle frame, normalized targets, quotient-frame
transitions, tau degree bound and complete quadric orbit. The corrected
`e=1,D2=0` ancestor exclusion is therefore accepted. The failed earlier
proof remains clearly labeled as such.
