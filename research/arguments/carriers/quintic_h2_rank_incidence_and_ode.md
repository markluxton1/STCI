# Quintic h=2 rank incidence, ODE witnesses, and conductor-norm boundary

This is a necessary-incidence analysis for the **admissible nonendpoint genus-one quintic \(A_4\), \(h=2\) parameter open in characteristic zero**, not a classification of arbitrary quintic carriers or an STCI construction. It retains scheme-theoretic saturation, global witness gluing, and the distinction between rank incidence and actual conductor norm.

The [monic ODE and open-incidence derivation](extracted_quintic_h2_monic_ode_and_open_incidence.md) establishes the underlying equations and admissible parameter domain. The [degree-five frontier](extracted_quintic_h2_incidence_and_localcoh_frontier.md) records the invalid elimination shortcuts and unresolved `j=0` branch. The global seventeen-equation audit below verifies a necessary model but does not settle saturation, conductor-power descent, or global support.


On the justified remaining nonendpoint \(A_4\) quintic \(h=2\) parameter open, write \(H=t^2+vst+ws^2\), \(Q=\sum_{i=0}^6q_is^{6-i}t^i\), \(j=\bar J\), and \(R=D_HQ\). The accepted closed-lane and intrinsic-contact results give the **unit ideal** \((q_5,q_6)=A\) on the localized candidate ring; this is not permission to invert either coefficient separately. The full quadratic and cubic rank incidence has 77 minors. Its saturation by \((q_5,q_6)\) equals the saturation of **twelve fixed generators**: eleven selected cubic minors and \(jM_{56}\), where \(M_{56}=q_5r_6-q_6r_5\). The identity uses pivot covers, works with nonreduced parameter rings, and does not divide by \(j\). The actual conductor norm product can be appended as a single necessary equation without splitting its factors.

On the same localized scheme, the cubic rank condition is equivalently the existence of uniquely determined, locally gluing witnesses \(d,u\) for
\[
h\(z\)q'\(z\)=(dz+u)q\(z\),\quad
E_i=w(i+1)q_{i+1}+(vi-u)q_i+(i-1-d)q_{i-1}=0
\quad\(0\le i\le7\).
\]
The equations imply **as ideal memberships**, not just at closed points, \((d-5)(d-6)=0\) and \(j(d-6)=0\). The \(d=5\) branch retains simple intrinsic-\(A_4\) infinity contact; \(d=6\) has no infinity root. Neither is discarded.

Geometrically, the ODE measures invariance of the zero divisor of q under the polynomial vector field `h\(z\) d/dz`, with the right-hand affine factor recording the chosen line-bundle lift and infinity weight. At a root x of q of multiplicity m, write `q=(z-x)^m r`, r\(x\)≠0. The leading term of hq′ is `m h\(x\) r\(x\)(z-x)^(m-1)`, whereas `(dz+u)q` has order at least m. In characteristic zero this forces h\(x\)=0. Thus the derivative equation encodes support at the actual root directions, rather than an unrelated coefficient rank. Repeated roots of h and the prescribed infinity support still need their exact coefficient equations; this interpretation does not replace them. In characteristic p a multiplicity divisible by p makes the displayed leading coefficient vanish, so this support argument does not extend without a separability or multiplicity hypothesis.

There is a single derived spectral polynomial on this entire scheme. Put \(\Delta=v^2-4w\), \(\eta=dv-2u\),
\[
P_6\(X\)=X\(X^2-4\Delta\)\(X^2-16\Delta\)\(X^2-36\Delta\),\qquad
P_5\(X\)=\(X^2-\Delta\)\(X^2-9\Delta\)\(X^2-25\Delta\).
\]
Then \((d-5)P_6\(\eta\)+(6-d)P_5\(\eta\)\) belongs to the same ODE ideal. The proof uses the two complementary idempotents \(d-5\) and \(6-d\) and Cayley–Hamilton on the sixth and fifth symmetric powers, without radicalizing, inverting a discriminant, or choosing roots. This is a computational compression, **not a unit-ideal certificate**. The subsequent whole-\(h=2\) global saturation prospect stopped at its memory guard and supplied no mathematical emptiness result; that resource-limit history is not part of the theorem. [Twelve generators](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/QUINTIC_H2_SPECTRAL_AND_GENERATOR_SYSTEM.md#2026-10-15-generalization-quintic-h2-twelve-generator-independent-audit), [ODE equivalence](extracted_quintic_h2_monic_ode_and_open_incidence.md#2026-10-15-generalization-quintic-h2-automatic-open-ODE-independent-audit), [spectral identity](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/QUINTIC_H2_SPECTRAL_AND_GENERATOR_SYSTEM.md#2026-10-15-generalization-quintic-h2-eta-spectral-independent-audit).


The **global** monic necessary incidence has seventeen equations in nine variables on the original-parameter open `delta E Delta1!=0`. It retains the inverse-map boundary `Delta K=0`. Saturating by `Delta K` treats only a smaller chart and cannot settle the global incidence. The [global monic proof](extracted_quintic_h2_monic_ode_and_open_incidence.md#2026-10-15-generalization-quintic-h2-global-monic-ODE-incidence) states this boundary exactly. The [degree-five j=0 reduction](extracted_quintic_h2_incidence_and_localcoh_frontier.md#why-the-proposed-eliminations-do-not-close-the-branch) remains unresolved: both proposed exclusions mistake a fixed simple A4 zero at source infinity for one at source zero, so they do not justify their pure-power specialization. The later verifier additionally divides the unreversed determinant polynomial instead of the actual source conductor. Replaying its resultants cannot repair this reduction gap. The degree-six j!=0 branch and full conductor-power descent remain open. Neither the ODE reduction nor the spectral accelerator resolves them.

---

## Whole-h2 global saturation remains open

The accepted seventeen-equation, nine-variable model over `QQ` retains
repeated roots and the finite cover boundary. Its
[runnable input](https://github.com/markluxton1/STCI/blob/bb5b1d5348097028738db196c262fe44b81b69ca/research/computations/generalization_quintic_h2_global_monic_ode_input_2026_10_16.m2)
loads the exact equations and domain polynomial. The target is

```macaulay2
saturate(h2GlobalIdeal, ideal h2GlobalDomainUnit)
```

on the domain `delta*E*Delta1 != 0`. No rational-cover determinant,
quadratic discriminant, quotient coefficient or `Jbar` is additionally
inverted. A bounded attempt did not complete this saturation and supplied
no ideal, dimension, unit certificate or emptiness conclusion. The global
H2 incidence remains undecided. Its geometric scope is the
[global monic ODE incidence](extracted_quintic_h2_monic_ode_and_open_incidence.md#2026-10-15-generalization-quintic-h2-global-monic-ODE-incidence)
and the [independent argument](#2026-10-16-generalization-quintic-h2-global-monic-ode-independent-audit).

---

<a id="2026-10-16-generalization-quintic-h2-global-monic-ode-independent-audit"></a>
## Global monic h=2 ODE incidence and its unsolved saturation

The necessary global monic \(h_2\) incidence has seventeen equations in nine variables on \(\delta E\Delta_1\ne0\), including repeated roots and the finite inverse-map boundary. The [original incidence](extracted_quintic_h2_monic_ode_and_open_incidence.md#2026-10-15-generalization-quintic-h2-global-monic-ODE-incidence) supplies conormal, octic, conductor, and ODE inputs. The seventeen equations are necessary; neither their saturation nor emptiness of the admissible locus has been proved.

### 1. Monic coverage and exact homogeneous gcd degree

For any remaining actual h2 mate candidate, a common factor at source
infinity would force G=j=0 by the accepted leading-coefficient
equations. The accepted mate closure excludes that lane. Thus the
complete degree-two homogeneous gcd has nonzero t^2 coefficient,
and its unique monic representative is

    H(x)=x^2+v*x+w,       x=r/delta=t/s.

This monic chart is therefore global for the remaining h2 mate
candidates. It imposes no distinct-root hypothesis. It also does
not normalize delta to one.

Write the literal normalized cubics as

    P=G*x^3+P2*x^2+P1*x-2a,
    Jc=(G+2j)*x^3+J2*x^2+J1*x-a-B,

where

    P2=6B+delta^2-3delta,       P1=3a-3B+2delta,
    J2=6B+3G+5delta^2-3delta,   J1=3a+3B+delta-delta^2.

Set A=G, Bc=P2-vG, C=G+2j, Dc=J2-v(G+2j). The leading two
coefficients of (Ax+Bc)H and (Cx+Dc)H match the cubics identically.
Their remaining coefficients match precisely when

    -2a-w*Bc=0,       P1-v*Bc-w*A=0,
    -a-B-w*Dc=0,      J1-v*Dc-w*C=0.                  (1)

These are exactly the four saved cover equations, with no coefficient
system inverted. Direct expansion gives

    E=A*Dc-Bc*C
     =G*(3G+4delta^2)-2j*(6B+delta^2-3delta).          (2)

The terms involving v cancel. The unit E is the determinant of the
two homogeneous linear cofactors A*t+Bc*s and C*t+Dc*s. At field
points they are independent exactly when they are coprime, so (1)
and E nonzero give complete homogeneous gcd degree two. This
includes affine degree drops of either cubic. A zero cubic or a
proportional cofactor pair instead has E=0 and is correctly outside
the exact-h2 domain.

### 2. Fixed-degree octic reversal and monic division

For the accepted actual Fdet(p,1)=sum_(i=0)^8 f_i*p^i, reciprocal
source coordinates give Fsrc(1,x)=sum f_i*x^(8-i). Put q7=q8=0
and define downward

    q_i=f_(6-i)-v*q_(i+1)-w*q_(i+2),    i=6,...,0.

For the coefficient of x^(i+2) in H*Q, this is exactly
q_i+v*q_(i+1)+w*q_(i+2)=f_(6-i). Therefore all coefficients
of degree at least two match, and the remaining two coefficients
are exactly

    r0=f8-w*q0,
    r1=f7-v*q0-w*q1,
    Fsrc=H*Q+r1*x+r0.                                (3)

The two explicit equations r0=r1=0 are retained. The accepted
geometric factor theorem supplies them for every actual h2
projection; this assembly does not extend that theorem to a
divisibility assertion over an arbitrary nonreduced
conormal-cover base. After the equations are imposed, (3) is an
exact ring identity on the incidence.

Monic division introduces no parameter denominator. Fixed degree
eight reversal and degree six quotient retain all coefficient drops
and the source point at infinity. In particular q6=f0 and
q5=f1-v*q6 have the intended A4 interpretation.

### 3. The new global domain does not invert Delta or K

The domain is exactly

    delta*E*Delta1 nonzero,
    Delta1=G(G+3delta^2)(G+delta^2+2B)
      +j[(delta^2-5B)G-3B(delta^2+3B)]-B*j^2.         (4)

Delta1 is necessary for all remaining mate candidates by the accepted
closures and A4 support argument. Delta=v^2-4w and
K=v^2+6vw+6w^2+2w are not factors of the declared unit product.
Thus the repeated finite-root boundary and the failed rational
inverse-map boundary remain represented by the original equations.
An accepted inconsistency on part of that boundary may be used as
a theorem, but no such locus is silently cancelled from this model.

For the unscaled actual quotient, the accepted A4 coefficients give

    q6=-3j*Delta1,
    q5=-2(G+3delta^2)*Delta1 modulo j.                (5)

There is no captured inverse-map scalar here. The accepted automatic
open proof now applies with kappa=1: the explicit Delta1-square
membership, or its equivalent quotient-ring argument, gives
(q5,q6)=1 after (4). This is an exact ideal equality and includes
nonreduced bases. It needs neither Delta nor K to be a unit.

The previous ODE and spectral proofs use monic H, (5), the Delta1
unit, coefficient unimodularity and field scalars 2,3. They therefore
apply unchanged to this original-parameter ring before any rational
inverse of the four cover equations. Their earlier actual use on a
smaller inverse-map chart does not limit this algebraic transfer.

### 4. The seventeen-equation system and its precise meaning

Using eta=dv-2u, the eight ODE coefficients are exactly

    2w(i+1)q_(i+1)+[(2i-d)v+eta]q_i
                         +2(i-1-d)q_(i-1),
    i=0,...,7.                                        (6)

These are twice the coefficients of H*q'-(dx+u)q. The change from
u to eta is invertible. The accepted globally unique ODE-witness
argument applies by (5), so (6) is the same shared rank/support
incidence on this domain, including its j=0 allowance.

There are four equations (1), two equations (3) and eight equations
(6), making fourteen. The three accepted derived equations

    (d-5)(d-6),       j(d-6),
    (d-5)P6(eta)+(6-d)P5(eta)

bring the saved presentation to seventeen equations in the nine
variables delta,a,B,G,j,v,w,d,eta. They belong to the same localized
ODE ideal, so appending them changes no scheme on (4). The temporary
variables p and x used in assembly are not additional model variables.

On actual admissible h2 projections, this incidence expresses the
accepted restricted-conductor support obligation. Every remaining
actual h2 mate candidate lies in it. The model does not impose center
avoidance or all original fiber conditions, and it does not establish
full inverse support or nonlinear conductor descent. An algebraic
survivor is therefore not automatically a projection or a mate.

### 5. Exact model and checking boundary

The [assembly source](https://github.com/markluxton1/STCI/blob/add6e1664e6d9db84e67fb0276a318a804b3d2f8/research/computations/generalization_quintic_h2_global_monic_ode_export_2026_10_15_attempt02.m2) verifies the reversed octic, four cover equations, eight ODE equations, and three accelerators. The [load-only model](https://github.com/markluxton1/STCI/blob/bb5b1d5348097028738db196c262fe44b81b69ca/research/computations/generalization_quintic_h2_global_monic_ode_input_2026_10_16.m2) reads the seventeen equations and original domain polynomial over \(\mathbf Q\), checks their ring and shapes, and exposes the ideal and domain unit. It does **not** perform Gröbner elimination, saturation, localization, or a nonemptiness test. The pending global saturation must invert only \(\delta E\Delta_1\); restricting to the additional \(\Delta K\ne0\) chart would lose the repeated-root/cover boundary. Neither a quintic nor unrestricted STCI conclusion follows.

