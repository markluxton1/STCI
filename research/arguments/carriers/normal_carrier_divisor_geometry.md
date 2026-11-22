# Divisor equality and local socle criteria on a normal carrier

**Status:** independently reviewed Hodge-equality, index and local-socle theorems. The Hodge equality criterion and exact-order argument were reconstructed during consolidation; the local criterion retains the normal-carrier index/socle theorem, primitive-triple certificate and separately scoped low-index exclusions as inherited premises at their exact hypotheses. This characterizes mate existence on a specified normal carrier; it does not exclude arbitrary normal carriers. The theorem has its explicit characteristic-zero scope, with the existence and exact-order arguments distinguished below. **The newly consolidated all-degree cyclic-cover Euler formula in §3.5 and its quintic/sextic identifications have been checked algebraically against the recorded cases, but are not yet independently reviewed as a new proof package.**

## 1. A mate is equivalent to Hodge-index equality on a normal hypersurface

Let `k` be algebraically closed of characteristic zero. Let

```
X subset P3_k
```

be a normal integral hypersurface of degree `a`, let `H=O_X(1)`, and let
`C subset X` be an integral curve of degree `e`. If `C` is `Q`-Cartier, its
rational self-intersection `C^2` is defined.

**Extremal-ray theorem.** The following conditions are equivalent.

1. There is a hypersurface `G` not containing `X` such that
   `Supp(X intersect G)=C`.
2. Some positive Cartier multiple of `C` is linearly equivalent to a
   positive multiple of `H`.
3. `C` is `Q`-Cartier and

   ```
   C^2=e^2/a.
   ```

4. `C` is `Q`-Cartier and its numerical class is `(e/a)H` in
   `N^1(X)_Q`.

Thus, for normal hypersurface carriers in characteristic zero, there is no
additional global torsion or ambient-lifting condition after the
`Q`-Cartier self-intersection reaches the Hodge-index boundary.

### Proof

The implications (1) => (2) => (3) are immediate but are included to fix
the exact multiplicities. If the mate has degree `b` and divisor `mC` on
`X`, then

```
mC ~ bH,             me=ab,
C^2=(b/m)(H.C)=e^2/a.
```

Condition (4) also follows.

Assume (3). Put

```
g=gcd(a,e),     mu=a/g,     v=e/g,
Delta=mu C-vH in Cl(X)_Q.
```

Then

```
Delta.H=mu e-v a=0,
Delta^2=(a/g^2)(aC^2-e^2)=0.                       (1)
```

Choose a positive integer `q` such that `L=q Delta` is Cartier. The Hodge
index theorem for the normal projective surface `X` says that the
intersection form is negative definite on `H^perp subset N^1(X)_R`.
Equation (1) therefore makes `L` numerically trivial.

It remains to upgrade numerical triviality to linear triviality. The
hypersurface sequence

```
0 -> O_P3(-a) -> O_P3 -> O_X -> 0
```

and the vanishing of intermediate cohomology of line bundles on `P3` give
`H^1(X,O_X)=0`. In characteristic zero the identity component `Pic^0(X)`
is therefore trivial. A numerically trivial line bundle lies in `Pic^tau`,
whose quotient by `Pic^0` is finite, so `L` is torsion. The accepted
SGA/Kummer hypersurface input says that `Pic(X)` is torsion-free. Hence

```
L ~ 0.
```

Consequently a positive multiple of `Delta` is principal, and for some
`q'>0`

```
q' mu C ~ q' v H.                                  (2)
```

The canonical section of `O_X(q'mu C)`, transported through (2), is a
section of `O_X(q'v)` with zero divisor exactly `q'mu C`. The restriction
map

```
H^0(P3,O(q'v)) -> H^0(X,O_X(q'v))
```

is surjective because `H^1(P3,O(q'v-a))=0`. A lift is an ambient mate and
cannot be divisible by the equation of `X`, since its restriction is
nonzero. This proves (1). The same Hodge argument shows directly that (3)
and (4) are equivalent.

The existence argument only needs every numerically trivial Cartier line
bundle on `X` to be torsion: taking one further multiple then gives (2).
Torsion-freeness of `Pic(X)` is used for the exact-order conclusions below.
The local Jacobian/socle results have their separate tame-index restriction;
no unrestricted characteristic-`p` exact-order or Picard transfer is asserted here.

## 2. The intrinsic local divisor is a necessary-and-sufficient mate test

Continue with the normal characteristic-zero hypersurface of Section 1, and assume
explicitly that `C` is both smooth and `Q`-Cartier, so every actual local
Cartier index below is finite. Retain the accepted notation from the intrinsic
normal-index theorem. Saturating the first normal symbol of `X` gives a
line quotient `B` of `N^*_(C/P3)` with `deg B=-ell`. At an on-curve point
`P`, let

```
r_P       = actual local Cartier index of C on X,
A_P       = vanishing order of the saturated first normal symbol,
D_(r_P),P = top ordinary-power/socle defect of the actual local
             Cartier multiple r_P C.
```

Put `R=lcm_P r_P`. The accepted intrinsic comparison, which assumes no
mate, constructs the effective rational divisor

```
E_X,C = sum_P (A_P+D_(r_P),P)/r_P [P]
```

and proves

```
deg E_X,C=ell-C^2.                                  (3)
```

Combining (3) with the extremal-ray theorem and Hodge index gives the new
sharp alternative

```
sum_P (A_P+D_(r_P),P)/r_P
    >= ell-e^2/a,                                   (4)
```

and, in characteristic zero,

```
equality in (4)  <=>  C has a mate on X.             (5)
```

Equivalently, define the **normal Hodge gap**

```
Gamma_X(C)=e^2/a-C^2
          =deg E_X,C-(ell-e^2/a) >= 0.               (6)
```

Then `Gamma_X(C)=0` is exactly the mate locus among normal `Q`-Cartier
carriers. If `Delta=mu C-vH`, equation (1) reads

```
Delta^2=-mu^2 Gamma_X(C).                            (7)
```

This removes a formerly separate global obligation: finite local indices
alone still do not imply torsion, but finite local indices **plus equality
in the intrinsic local budget** do. The equality forces the global Cartier
ray and the ambient lift.

The line-bundle form of the accepted comparison remains stronger than
(4):

```
O_C(R E_X,C)=B^(-R) tensor O_X(-RC)|C.
```

It should be retained in positive genus even when only the scalar Hodge gap
is being used.

## 2.5 The ADE exceptional correction is the normal-layer defect budget

The Hodge-gap formula has a second geometric interpretation,
using the **same actual local data**, whenever \(X\) has only
Du Val singularities. Let
\(\pi:\widetilde X\to X\) be its crepant
minimal resolution and write
\(\pi^*C=\widetilde C+Z\), with rational
exceptional correction \(Z\). The strict transform
is a smooth rational quartic. Adjunction and
crepancy give
\[
 \widetilde C^2=14-4a,\qquad
 C^2=\widetilde C^2-Z^2.
\]
The total zero divisor of the degree-\(a\)
surface's saturated first normal symbol has degree
\(\sum_PA_P=4a-14+\ell\); this is the
normal-bundle degree used in the
[accepted carrier symbolic budget](normal_carrier_symbolic_torsion.md#a-symbolic-triple-defect-certificate-for-unrestricted-normal-carriers).
Combine it with the **mate-independent** local
self-intersection formula of §2 to obtain
\[
 \boxed{\quad
 -Z^2=\sum_{P\in C}\left(
     \left(1-\frac1{r_P}\right)A_P
     -\frac{D_{r_P,P}}{r_P}
     \right).\quad}                                   \tag{ADE1}
\]
This numerical identity applies to any normal ADE
carrier containing the fixed \(C\), even when it
does **not** possess a mate. It does not identify
the displayed summands with individual exceptional
intersection contributions without further
local analysis.

If a mate exists, Hodge equality forces
\[
 \boxed{-Z^2=4a-14+\frac{16}{a}.}                 \tag{ADE2}
\]
Thus the familiar quartic, quintic and sextic
correction targets \(6,46/5,38/3\) are
specializations of one adjunction identity.
The first-symbol divisor, actual local
Cartier indices and ordinary multiplication
defects are different descriptions of its
*available* correction; the Hodge equality
specifies its *required* value.

This translation does **not** replace
the final global surface-geometry proofs:
realizability of (ADE2) by an actual
hypersurface with the requisite torsion class
is a distinct constraint. The quintic
\(4A_1+9A_4\) reduced-symbol row, for example,
meets the correction \(46/5\) but fails the
forced double-cover canonical-map bound.

## 3. Exact exponent and minimal mate once the boundary is reached

Assume the equivalent conditions of Section 1. For every point of `C` on
`Sing(X)`, let `r_P` be the actual local Cartier index, and put

```
R=lcm_P r_P,       g=gcd(a,e),
mu=a/g,            v=e/g.
```

The accepted local detection theorem now gives the exact order of the
primitive Weil class and not merely an upper bound:

```
t=R/gcd(R,mu).                                      (8)
```

The mate degrees on this fixed carrier are exactly

```
b=k t v,       k=1,2,3,... .                        (9)
```

The minimal generic transverse length is

```
n_min=mu t=lcm(mu,R).                               (10)
```

In particular

```
a divides e^2 R.                                    (11)
```

Equations (8)--(10), together with (5), give a complete numerical
description on a fixed normal carrier: the intrinsic equality decides
existence; the actual local indices determine the least mate and every
higher mate. No independent section-lifting or hidden global torsion factor
remains.

This is not an effective classification of all normal carriers: computing
`C^2`, the local indices and the full defects can still be difficult, and
unbounded indices occur even in elementary local hypersurface models.

## 3.5 A single cyclic-cover Euler formula for all normal carrier degrees

**Scope.** This is a direct combination of the established
[normalized Kummer eigensheaf construction (Ambro, §4, Lemmas
4.1–4.2)](https://arxiv.org/abs/1310.3951), the hypersurface
Hilbert polynomial and the *actual divisorial filtration*
of a smooth \(C=C_0\) on a normal characteristic-zero
hypersurface. It is not an additional existence theorem.

Suppose \(X\) is a normal integral degree-\(a\) hypersurface
and has an actual sole-support mate. Retain
\[
 g=\gcd(a,4),\quad \mu=a/g,\quad v=4/g,\quad
 t=\operatorname{ord}_{\operatorname{Cl}(X)}
          (\mu C-vH),\quad
 m=t\mu,\quad b=tv.
\]
The minimal mate has divisor \(mC\sim bH\).
The class \(\Delta=\mu C-vH\) defines a connected
quasi-étale cyclic cover \(\pi:Y\to X\) of degree
\(t\), with exact normalized eigensheaf decomposition
\[
 \pi_*\mathcal O_Y
   =\bigoplus_{j=0}^{t-1}\mathcal O_X(j\Delta).
 \tag{CE1}
\]
Here \(\mathcal O_X(D)\) denotes the rank-one reflexive
divisorial sheaf, not necessarily a line bundle.

Write \(I_i=\mathcal O_X(-iC)\) for \(0\le i\le m\).
The divisorial quotient \(E_i=I_i/I_{i+1}\) is a
torsion-free rank-one sheaf on the smooth \(C\), hence a
line bundle. In the actual normal filtration set
\[
 E_i=\mathcal O_C(-i\ell+D_i),\quad
 D_0=D_1=0,\quad 0\le i<m,
\]
where \(\ell\) is the degree of the saturated first
normal line and \(D_i\) its *actual* effective
multiplication-defect divisors. With the convention
\(\mathcal O_{\mathbf P^3}(1)|_C=\mathcal O_{\mathbf P^1}(4)\),
\[
 \chi(E_i(nH))=4n+1-i\ell+\deg D_i.
\]
The hypersurface restriction sequence gives
\[
 \chi(\mathcal O_X(nH))
 =\chi_0+\frac a2n(n-a+4),\qquad
 \chi_0=1+\binom{a-1}{3}.                         \tag{CE2}
\]
For \(h=1,\ldots,t-1\), the actual Cartier
relation \(t\Delta\sim0\) identifies the eigensheaf
\[
 \mathcal O_X((t-h)\Delta)
 \simeq\mathcal O_X(hvH-h\mu C).
\]
The exact filtration of the coherent quotient
\(\mathcal O_X/\mathcal O_X(-h\mu C)\) by \(E_i\)
then yields the **uniform arithmetic identity**
\[
 \boxed{\begin{aligned}
 \chi(\mathcal O_Y)
 ={}&t\chi_0+
 \sum_{h=1}^{t-1}\Bigg[
    \frac a2(hv)(hv-a+4)
   -h\mu(4hv+1)\\
 &\qquad+\frac{\ell\,h\mu(h\mu-1)}2
   -\sum_{i=0}^{h\mu-1}\deg D_i
 \Bigg].
 \end{aligned}}                                      \tag{CE3}
\]
All divisorial-layer terms refer to the **same actual
carrier and mate**; an abstract sequence of possible
\(D_i\) does not create a cover. Because the cover is
quasi-étale and \(K_X=(a-4)H\), one also has
\[
 \boxed{K_Y^2=t\,a(a-4)^2.}                         \tag{CE4}
\]
These are characteristic-zero formulas for the normal
cover itself; passing to a resolution preserves
\(\chi\) **when the cover has rational singularities**,
not in general.

**Recovery of both degree-specific calculations.**
For a normal \((5,8)\) candidate one has
\((a,\mu,v,t)=(5,5,4,2)\). Writing the first
line quotient \(\mathcal O(-q)\), formula (CE3) becomes
\[
 \boxed{\chi(\mathcal O_Y)
 =-45+10q-\sum_{i=0}^4\deg D_i,\quad K_Y^2=10.}
 \tag{CE5}
\]
For the **globally ADE** quintic case the cover
and its resolution have rational singularities.
The independently established exceptional-cover
Euler calculation gives
\(\chi(\mathcal O_Y)=10-w/4\), hence the
additional exact comparison
\[
 \boxed{\sum_{i=0}^4\deg D_i
         =10q-55+\frac w4.}                       \tag{CE6}
\]
This identifies a constraint between **saturated
multiplication defects** and the ADE cover's
exceptional contribution \(w\); it does not identify
either invariant pointwise or replace the global
canonical-map inequality.

For a normal \((6,6)\) candidate,
\((a,\mu,v,t)=(6,3,2,3)\), and the existing
saturated profile
\[
 (D_0,\ldots,D_8)
 =(0,0,A,B,T,2T-B,2T-A,2T,2T),
 \qquad \deg T=4\ell-17
\]
reduces (CE3) immediately to
\[
 \boxed{\chi(\mathcal O_Y)
 =6\ell-21-2\deg A,\quad K_Y^2=72.}              \tag{CE7}
\]
Thus the quintic and sextic Euler calculations are
two evaluations of a **single exact filtration
identity**. The genus, cover order and available
canonical inequalities differ; no general
contradiction follows from (CE3) alone.

## 4. Strongest current all-degree consequence for the fixed rational quartic

Specialize to

```
C0=[s^4:s^3t:st^3:t^4],       e=4,
N_C0^*=O_P1(-7)^2.
```

Let `X` be a normal integral carrier of degree `a`. If `C0` is not
`Q`-Cartier, it has no mate on `X`. If it is `Q`-Cartier, define
`ell,A_P,r_P,D_r,P` as above. The exact normal-carrier decision criterion
is

```
sum_P (A_P+D_(r_P),P)/r_P = ell-16/a.               (12)
```

Every equality candidate satisfies all of the following, in every mate
degree.

1. `a>=5`. With `g=gcd(a,4)`, `mu=a/g`, `v=4/g` and
   `R=lcm_P r_P`,

   ```
   t=R/gcd(R,mu),
   b_min=v t,
   n_min=lcm(mu,R),
   a | 16R.
   ```

   The accepted low-degree theorem also forces `b_min>=5`.

2. Let `s=max_P r_P`. The accepted symbolic-triple improvement of the
   local power--socle inequality gives

   ```
   4a^2-(7s+6)a+16s <= 0,
   s >= ceil(a(4a-6)/(7a-16)).                       (13)
   ```

   The separately accepted all-index-at-most-four theorem strengthens the
   small cases to

   ```
   s>=5.                                             (14)
   ```

   Conversely, for each fixed `s`, (13) bounds `a` by the larger root

   ```
   a <= ((7s+6)+sqrt((7s+6)^2-256s))/8.              (15)
   ```

   This is a finite carrier-degree reduction for every bounded-index
   class, not a universal index bound.

3. The pointwise Frobenius identity and local power formula hold:

   ```
   2 sum_i length(T_i)_P=r_P D_(r_P),P,
   D_n,P=(n/r_P-1)A_P+(n/r_P)D_(r_P),P.              (16)
   ```

   Thus `r_P D_(r_P),P` is even; in particular a positive defect at odd
   index is at least two.

4. In the constant-direction branch `ell=7`, the first-layer torsion
   divisor `T_3` of the global symbolic triple obeys the accepted
   carrier-wide certificate

   ```
   2 <= deg T_3
      <= sum_(r_P=2) A_P
         +(1/2)sum_(r_P>=4) r_P D_(r_P),P.            (17)
   ```

   Its support must also satisfy the accepted apolar condition: degree two
   forces the appropriate doubled endpoint divisor; degree three forces
   either the mixed three-point divisor or an endpoint doubled divisor plus
   one point. Index-three primitive multiples contribute neither local
   defect nor symbolic-triple torsion.

Statements (12)--(17) are one simultaneous all-degree certificate. They do
not treat different singular points as separate hypothetical
presentations, replace actual indices by ADE labels, or discard higher
jets. In particular, every hypothetical normal carrier lies on the
Hodge-index equality boundary and must contain an on-curve singularity of
index at least five; as carrier degree grows, its maximum actual index must
grow at least asymptotically like `4a/7`.

## 4.5 Degree five and degree six: **all mate degrees** before specializing

The exact-index theorem (§3) is **not only a tool for
\((5,8)\) or \((6,6)\)**. It constrains
every normal integral degree-five or degree-six carrier
with any sole-support mate, under the same
characteristic-zero and fixed-\(C_0\) hypotheses.

**Every normal quintic with a mate.**
Here \((a,e,g,\mu,v)=(5,4,1,5,4)\).
Since \(C_0^2=16/5\), the actual global
Cartier index \(R\) satisfies \(5\mid16R\),
hence \(R=5t\) for some positive integer \(t\).
The exact theorem gives
\[
 \operatorname{ord}(5C_0-4H)=t,\qquad
 \boxed{b_{\min}=4t,\quad m_{\min}=5t,\quad R=5t.}
 \tag{Q5}
\]
The quartic-carrier theorem rules out \(t=1\):
otherwise an actual degree-four mate would
exist on the quintic. Therefore \(t\ge2\)
and **\(R\ge10\)**. Every mate on this fixed
quintic has degree a positive multiple of
\(4t\). The familiar \((5,8)\) case corresponds
to \(t=2\) and \(R=10\); other allowed
\(t\) are **not** excluded by the
\((5,8)\) ADE proof.

**Every normal sextic with a mate.**
Here \((a,e,g,\mu,v)=(6,4,2,3,2)\).
The same integrality forces \(3\mid R\);
write \(R=3t\). Then
\[
 \operatorname{ord}(3C_0-2H)=t,\qquad
 \boxed{b_{\min}=2t,\quad m_{\min}=3t,\quad R=3t.}
 \tag{S6}
\]
If \(t=1\) or \(2\), an actual degree-two
or degree-four mate exists, contradicting
the established low-degree exclusions.
Thus \(t\ge3\), **\(R\ge9\)**, and every
mate degree is a positive multiple of
\(2t\). The equal-degree \((6,6)\)
case forces \(t=3,R=9\) because its
specific mate has degree six. For
\((6,b)\) with \(b\ne6\), one cannot assume
that this same index-nine specialization
holds; the **all-mate** statement is
the family (S6).

These are **necessary index and torsion constraints**
for all mate degrees, not exclusion of
all normal quintics or sextics. Each
candidate must also satisfy the **Hodge
equality** \(C_0^2=16/a\) and the
actual normal-symbol/socle comparison,
which is already a sufficient
fixed-normal-carrier test if verified
on a real surface. Nor do these equations
apply to a nonnormal degree-five/six
image or a degree-six carrier singular
generically on \(C_0\): those require
the normalization/branch geometry.

## 5. What was removed, and what remains

The new theorem removes **global lifting as a separate hypothesis or
obligation in the normal branch**. More precisely, after `Q`-Cartierness,
the scalar equality `C^2=e^2/a` (or equivalently equality in (4)) forces:

* torsion of the primitive Weil relation;
* its exact order from actual local indices;
* an effective Cartier divisor supported exactly on `C`;
* and an ambient hypersurface lifting that divisor.

The remaining boundaries are exact.

1. **Normality.** The Hodge step applies to Cartier multiples on a normal
   surface, and the accepted local formula uses normality in the colon
   identity and in regularity of `z^r/h`. A nonnormal carrier requires its
   normalization, conductor colengths, residual phases and possibly several
   inverse branches. The accepted singleton Cartier-lift conductor formula
   is a separate partial replacement, not a consequence of this note.

2. **Local indices and the missing global bound.** Local smoothness of the
   branch and surface multiplicity alone do not bound `r_P`: the local
   models `xy-z^r=0` with the smooth curve `(x,z)` have arbitrarily large
   index and zero primitive defect, while their polynomial degrees grow
   with `r`. These are not fixed-degree global carriers of `C0`, and no
   global index bound or fixed-degree unboundedness is supplied here.
   Equations (13)--(17) constrain the global distribution of actual indices
   without excluding all possible high-index configurations.

3. **Curve-specific symbolic obstruction.** The improvement from the
   general balanced-rational threshold to the fixed `C0` certificate uses
   the accepted nonzero constant-direction primitive-triple obstruction.
   An analogous obstruction is not proved for every balanced rational
   curve.

4. **Characteristic.** Existence in Section 1 only needs numerically
   trivial Cartier line bundles on `X` to be torsion; exact order additionally
   uses the accepted torsion-free Picard input. The theorem here is stated
   in characteristic zero. The local power--socle theorem has the separately
   proved range where every actual index is prime to the characteristic;
   no unrestricted characteristic-`p` exact-order or Picard transfer is
   asserted here.

5. **Other generic algebras.** If both defining equations have generic
   normal order at least two, neither one is a normal order-one carrier and
   the generic algebra need not be curvilinear. That entirely-thick branch
   remains governed by the separate conormal/socle and formal-root program.

The normal branch has therefore been reduced, without a degree-by-degree
mate search, to a sharply stated geometric question:

> Can a normal integral hypersurface containing `C0` realize the extremal
> equality `C0^2=16/a` while satisfying the exact local divisor,
> high-index, parity and symbolic-triple support conditions (12)--(17)?

A proof that the intrinsic inequality (4) is always strict for `C0` would
close every normal carrier in every degree at once. It would not by itself
close nonnormal or entirely-thick carriers.


---


## Scope

The local divisor criterion requires a smooth Q-Cartier curve. Numerical triviality gives torsion only under the stated hypotheses; exact-order formulas additionally use torsion-free Picard input. Local unbounded-index examples do not settle the fixed-degree global question.
