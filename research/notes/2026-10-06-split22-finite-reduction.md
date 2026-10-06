# Two totally ramified residual roots: a full higher-jet reduction

## Result and scope

Work over an algebraically closed field of characteristic zero on

\[
 C_0=[s^4:s^3t:st^3:t^4].
\]

Retain P-020's **integral carrier, reduced/content-free split first-normal
exceptional divisor, and no vertical component** hypotheses. Consider
only the `d=1,[2,2]` family whose two residual ruling roots are the totally
ramified rulings. The two low evaluation zeros are at their preimages.
This is the complete family parameterized in
`2026-10-05-split-sextic.md`, not merely its fixed specimen.

**Proved necessary reduction.** If a carrier in this entire family has an
STCI mate of any degree, its low-factor parameter must be

\[
 \boxed{h=-\tfrac12.}
\]

Up to the diagonal automorphisms of `C0`, and up to multiplying the carrier
by a nonzero scalar, the remaining carriers have the one-parameter form

\[
\begin{aligned}
 F_\tau={}&-B^2+\tau q\mathcal K,\qquad \tau\ne0,\\
 \mathcal K={}&q(-16x_0^2+16x_1^2-x_3^2)
 +16x_1A-16x_2A+4x_3B-x_2D+8q^2,
\end{aligned}
\]

where `q,A,B,D` have their repository meanings. No STCI mate is constructed,
and this line is not excluded. Its possible extra conductor and further
normalization data must remain in the frontier. The other `[2,2]` root
configurations and the surviving `[4]` families are outside this theorem.

**Exact certificate:**
`research/computations/verify_split22_finite_reduction.py`.
Run with `/private/tmp/stci-cas-venv/bin/python` in this checkout. The full
certificate passed on 2026-10-06. The new normal-sheaf argument is in
`2026-10-05-mumford-normal-bound.md`; root independently audited that proof.
A separate adversarial audit of the present reduction was requested.

## Exact local state and the global Jacobian zero divisor

Put

\[
 a=h-\tfrac12,\quad c=3a^2+2a+1,
 \quad a\ne0,\quad 2a+1\ne0,\quad u_0u_8\ne0.
\]

The last conditions are the existing content-free endpoint conditions;
`2a+1=2h`. In the finite blowup chart set

\[
 x_0=1,\quad x_1=z,\quad x_2=z^3+e,\quad
 x_3=z^4+e((1-a)z+W).
\]

The low section is `e=W=0`. Let `f=F/e^2` be the strict-transform equation.
The ambient carrier `F`, including all its `lambda q^3` lifts, is the exact
one displayed in the older split-sextic note. Define

\[
\begin{aligned}
 R={}&a(u_0+u_2z^2+u_3z^3+u_5z^5+u_6z^6+u_8z^8)
             -2(a+1)z^4,\\
 G={}&u_2-au_3z+\beta z^2+(a^2+a+1)u_5z^3
             -a(a+2)u_6z^4+cu_8z^6,\\
 \beta={}&a\lambda-\frac{(a+1)(a^2+1)}a.
\end{aligned}
\]

Exact expansion gives the two Jacobian components along the low section:

\[
 f_W=-zR,\qquad f_e=-a^2zG.
\]

Also `f(z,0,W)=u(z)W^2-zRW`, with
`u(z)=(R+z^4)/a`. Thus the section is regular generically on the integral
strict surface, independently of whether another nonnormal curve meets it
at finitely many points. The local normal-sheaf theorem therefore applies.

The finite endpoint Hessian determinant is `-2a^3u0^2`; the reversed
endpoint determinant is `-2a^3u8^2`. Both are nonzero. At the finite
endpoint `fW=-a u0 z+...`; at the reversed endpoint the corresponding
component is `a u8 z+...`. Each endpoint is an `A1` germ with Jacobian
common order exactly one. All other base points are covered by the finite
chart with `z!=0`, so the exact global zero-divisor length is

\[
 \boxed{\delta=2+\deg\gcd(R,G).}                         \tag{1}
\]

This formula includes `G=0`, when `gcd(R,0)=R` and `delta=10`. Treating a
zero polynomial as though it had a degree-six bound would be incorrect.
That separate case is closed below.

The ambient normal extension has determinant degree eight and its
Jacobian target degree twelve. Consequently

\[
 \deg N_{\Gamma/D}=\delta-4.
\]

P-020/P-023 force `Gamma#^2=13/5` for an STCI mate. The exact normal-sheaf
defect formula therefore gives

\[
 \operatorname{Def}(\Gamma)=\delta-4-13/5.
\]

Both endpoints contribute `1/2` to this defect, so `delta>=8`.
This uses numerical intersections, where cancelling the positive integer
mate scale is legitimate. No scale is cancelled in a local class group,
and no Cartier index bound is inferred by cancelling it.

## Nonzero G: exact division and the very small remaining defect budget

Suppose first that `G!=0`. Equation (1) gives `delta<=8`; hence

\[
 \delta=8,\qquad \deg G=6,\qquad G\mid R.
\]

In particular `c!=0`. Write

\[
 R=(N+az^2/c)G.
\]

The quotient's linear coefficient is zero by the coefficient of `z^7`.
Its constant coefficient is nonzero because `R(0)=a u0!=0`. Then `u2!=0`.
The coefficient of `z` forces `u3=0`. The coefficients of `z^3,z^5`
together force `u5=0`, without deleting any exceptional root of
`a^2+a+1`. The remaining equations are

\[
\begin{aligned}
 u_0&=Nu_2/a,\\
 u_6&=\frac{Nc^2u_8}{a(2a+1)^2},\\
 \beta&=\frac{a^2(3a+2)u_2}{Nc},\\
 \frac{a^3(3a+2)u_2}{Nc^2}
 -\frac{N^2(a+2)c^2u_8}{(2a+1)^2}&=-2(a+1).
\end{aligned}                                                   \tag{2}
\]

All divisions in (2) are by previously established nonzero quantities.
The factor `3a+2` is **not** divided out here.

The diagonal automorphism `z -> t z` acts, after normalizing the residual
evaluation, by `Rnew=t^-4 R(tz)` and `Gnew=t^-2 G(tz)`. It sends
`N -> N/t^2`. Since the base field is algebraically closed and `N!=0`,
we may take `N=1`. Put `tau=N^2u8`; equivalently one may use the invariant
coordinate `y=z^2/N` before the normalization.

The total defect is `7/5`. The two endpoints consume one, leaving

\[
 \boxed{\operatorname{Def}_{\rm interior}=2/5.}             \tag{3}
\]

A single interior `A1` on the smooth low curve would contribute `1/2`,
contradicting (3). This excludes every carrier with even one such node;
no assumption about the other singular points is required.

## The cubic and its Hessian remainder

For `3a+2!=0`, solve (2) by

\[
\begin{aligned}
 P&=\frac{c^2[-2(a+1)+\tau(a+2)c^2/(2a+1)^2]}{a^3(3a+2)},\\
 b&=\frac{a^2(3a+2)P}{c},\qquad
 V_6=\frac{\tau c^2}{a(2a+1)^2}.
\end{aligned}
\]

Here `u2=P`, `u0=P/a`, `u6=V6`, `u8=tau`, and `beta=b` after taking `N=1`.
In particular `P!=0`, `tau!=0`. Define the cubic

\[
 H_3(y)=P+by-a(a+2)V_6y^2+c\tau y^3,
 \qquad Q(y)=1+ay/c.
\]

The next two exact coefficients of `f` are

\[
\begin{aligned}
 L(y)={}&aP+(-a^2+3ab+2a+5)y
       -a(3a^2+4a+2)V_6y^2+a(9a^2+6a-1)\tau y^3,\\
 H_2(y)={}&a+2a^3V_6y+2a^2(a^3-a^2-a-1)\tau y^2.
\end{aligned}
\]

Set

\[
 B_2=a^3y^2-a^2QL+Q^2H_2,
 \qquad D_2=4y^2H_2/a-L^2.
\]

At a simple root of `G(z)=H3(z^2)`, differentiation **before** imposing
the collision equation gives

\[
 \det\operatorname{Hess}_{z,e,W}(f)
       =-2z^2(G'(z))^2 B_2(z^2).
\]

Thus every simple root with `B2!=0` is `A1`. Let `Brem` be the remainder
of `B2` modulo `H3`. When `H3` is squarefree, absence of nodes would force
all three remainder coefficients to vanish. Their exact Groebner basis
contains `a tau` and `2a^2+a`, impossible on the content-free domain.
So every mate-compatible cubic must have a repeated root.

For arbitrary cubic `H3`, a necessary condition for no simple-root node is

\[
 \boxed{H_3\mid B_{\rm rem}(H_3')^2.}                    \tag{4}
\]

At a double root the squared derivative already supplies multiplicity two;
at a triple root it supplies at least three. At a simple root it is a
unit, so (4) is exactly the needed vanishing there. Therefore (4) does
not impose an unjustified condition at a repeated root.

Clear denominators in (4) and remove only known invertible factors.
Exact elimination gives, up to those invertible factors,

\[
 (a+1)^4 S_1(a)S_2(a)S_3(a)=0,
\]

where

\[
\begin{aligned}
 S_1&=3a^4+8a^3+40a^2+36a+9,\\
 S_2&=8a^4-6a^3+33a^2+36a+9,\\
 S_3&=2a^7+15a^6+48a^5+39a^4+2a^3-3a^2+4a+1.
\end{aligned}
\]

The exact univariate Groebner element is proportional to
`a^2(a+1)^4(2a+1)^11(3a+2)^2 S1 S2 S3`.
A linear-in-`tau` Groebner element has leading coefficient proportional to
`(a+1)^2(2a+1)^7(3a+2)`. Consequently, away from `a=-1` and forbidden
values, these are finite parameter strata. The certificate preserves these
polynomials and checks every exceptional stratum, rather than interpreting
a generic sample as a complete elimination.

## Closing all three finite strata and the divided parameter value

On `S1=0`, the cubic has a triple root

\[
 y_0=(a+2)c/[3(2a+1)^2],
\]

and `tau` is the rational expression checked in the certificate. The
values `y0,Q(y0),D2(y0),B2(y0)` are all units in `Q[a]/(S1)`.
There are therefore two interior collisions, each with collision order
and Jacobian order three. The nonzero transverse determinant allows a
formal Morse elimination of `(e,W)`; its residual leading coefficient is
a nonzero multiple of `B2`, and its order is six. The germ is `A5`.

The curve index is also controlled, not inferred solely from the
singularity's name. The Morse critical section has `(e,W)=O(t^3)`, where
`t=z-z0`. Along the original smooth low curve, both Morse coordinates have
order at least three and their product has order six with nonzero leading
coefficient. Their orders are thus exactly three. The local `A5` class is
three, and the normal-sheaf defect is `3^2/6=3/2`, already exceeding (3).

On `S2=0`, exact elimination gives

\[
 \tau=-\frac{48944a^3-40956a^2+375576a+181341}{2593080}.
\]

The cubic has one double root and one simple root. The double-root value
`y0` and `Q,D2,B2,H3''` there are units modulo `S2`. The same argument
with order two gives an `A3` germ of low-curve class two and normal defect
`2^2/4=1`, again impossible. The certificate verifies these unit statements
by exact reduction and gcd, including all algebraic roots of `S2`.

On `S3=0`, the exact corresponding `tau` value makes `P=0` identically in
`Q[a]/(S3)`. It gives `u0=0`, violating endpoint content-freeness.

The exceptional chart `a=-2/3` in (2) has

\[
 \tau=1/18,\quad u_6=-3/4,\quad \beta=0,\quad u_2=U\ne0,
 \qquad H_3=U-2y^2/3+y^3/18.
\]

For its version of (4), the three remainder numerators have polynomial
gcd one in `Q[U]`. This chart has no node-free member and is excluded.

## Closing the identically-zero G stratum

If `G=0`, content-freeness forces `c=0`, and the other coefficients force

\[
 u_2=u_3=u_5=u_6=\beta=0.
\]

Indeed `c=0` has no common root with any of the other coefficient factors
`a,a^2+a+1,a+2`; no exceptional coefficient vanishing has been suppressed.
Now `delta=10`, and the allowed interior defect is `12/5`.
Put `r=z^4`. Then

\[
 R=a u_0-2(a+1)r+a u_8r^2,
\]

while the coefficient of `e^2` along the low curve is

\[
 H_2(z)=a+2a^2u_8(a^3-a^2-a-1)z^4.
\]

There are only the following possibilities.

- If the quadratic in `r` has distinct roots and `H2` is nonzero at both,
  all eight interior points are `A1`. Their defect is four.
- `H2`, being linear in `r` with nonzero constant, can vanish at only one
  of the two distinct roots. Scale that four-point cluster to `z=1`.
  Reduction modulo `c=0` then gives
  `u8=-3a-11/4`, `u0=3/4-3a`. The transverse `(z,W)` Hessian is invertible;
  the residual cubic coefficient is `(10a+11)/84`, a unit modulo `c`.
  These four germs are `A2`. The low curve has class one: the Morse
  parameter is `e`, which vanishes identically on the curve, so it is one
  of the coordinate branches. The other four germs are `A1`.
  Total interior normal defect is `4/3+2=10/3`.
- If the quadratic has a double root, scale it to `z=1`, obtaining
  `u0=u8=(a+1)/a`. Both `H2` and the transverse Hessian determinant are
  units modulo `c`. The residual Morse order is four, giving four `A3`
  germs of low-curve class two. Their total defect is four.

None equals `12/5`. This closes the case that a degree-six bound on a
nonzero polynomial would have missed.

The defects used here are the **normal-sheaf defects** `i^2/n` for the
smooth low curve of class `i<=n/2` in `A_(n-1)`. They are not the
numerical-pullback self-intersection corrections `i(n-i)/n`. In this scope
one can obtain the former by subtracting the latter from the local
Jacobian/conormal length `i`; the exact defect formula in the companion
normal-sheaf note provides the global bookkeeping.

## Surviving line and continuation requirements

The sole remaining value is `a=-1`, equivalently `h=-1/2`. In the normalized
chart,

\[
\begin{aligned}
 u_0&=-16\tau,&u_2&=16\tau,&u_6&=-4\tau,&u_8&=\tau,\\
 \beta&=-8\tau,&\lambda&=8\tau,
\end{aligned}
\]

and

\[
 G=2\tau(z^2-2)^2(z^2+2),\qquad
 R=-\tau(z^2-2)^3(z^2+2).
\]

This is the displayed carrier `Ftau=-B^2+tau q K`. At the two simple
collisions `z^2=-2`, finite exact scratch Morse calculations made the
residual vanish through degree six for all `tau`; this suggested an extra
conductor locus and was a reason to stop short of a global exclusion.
That finite-jet observation is **not** a proof of an identically vanishing
Morse residual or a completed normalization calculation, and is not used
in the theorem above.

The next mathematical move is to compute the normalization/conductor and
actual numerical branch intersections of this line, with all exceptional
`tau` values preserved. The other two collision points have `z^2=2`,
collision order three and Jacobian order two, so the clean ordinary-node
argument does not apply. Integral-carrier existence, global mate descent,
and radical support still require their own checks. The global conductor
loophole must not be replaced by a tangent-form or class-group shortcut.

## Provenance and failed reductions preserved

The fixed specimen was already excluded in the 2026-10-05 note by actual
higher jets. The present work used that family's **entire exact ambient
lift fiber**, the newly proved normal-sheaf defect inequality, and polynomial
elimination. It did not extrapolate from the fixed specimen.

The first attempted universal `degree G<=6` inference overlooked `G=0`.
That oversight was caught during the resumed 2026-10-06 audit; the companion
normal-sheaf note was amended with the explicit `G!=0` qualification, and
this certificate closes the omitted stratum independently. A further
false shortcut would identify normal-sheaf defects with inverse-Cartan
self-intersection corrections; the different values are recorded above.

The nonramified `[4]` certificate also required two resultant-sign repairs:
`Res(P-2z,1+(P/2-2)z)=-(P-2)^2/2`, and the finite-root `[2,2]` analogue
is `-(P-2)(P-2t)/2`. The repaired verifier now passes all its image, content,
selected `A3`, and symbolic ambient-lift checks. Its mathematical content
conditions were unchanged.
