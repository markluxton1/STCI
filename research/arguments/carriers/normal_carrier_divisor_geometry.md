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

## 4.7 Unequal-degree pairs can acquire an actual normal carrier

**Status: new consequence of classical Bertini, with exact proof
below; mathematical re-review required.**
This is a separate reduction from the already accepted
equal-degree \((6,6)\) normal-pencil argument.
Use [Kleiman, *Bertini and his two fundamental
theorems*](https://arxiv.org/abs/alg-geom/9704018),
for the irreducible/general-member and
smoothness-away-from-base statements.

**Mixed-degree normal-replacement lemma.**
Work over an algebraically closed field of
characteristic zero. Let \(a<b\) and let
\(F_a,G_b\) be *any* coprime homogeneous
forms such that their proper complete
intersection has **sole reduced support**
the smooth \(C_0\). Suppose at least one
of \(F,G\) has **generic normal order
one** along \(C_0\). Then an actual
degree-\(b\) generator of the same
complete-intersection ideal can be
chosen **integral and normal**:
\[
 \boxed{K_b=\lambda G_b+F_a L_{b-a},
 \quad\lambda\ne0,\quad
 V(F_a,K_b)=V(F_a,G_b),\quad
 V(K_b)\text{ normal integral}.}            \tag{NR1}
\]

**Proof.** Put \(d=b-a\ge1\) and
consider the projective linear system
\[
 W=kG_b+F_aH^0(\mathbf P^3,\mathcal O(d))
 \subset H^0(\mathbf P^3,\mathcal O(b)).
\]
Its *set-theoretic base locus* is exactly
\(C_0\): where \(F\ne0\), some degree-\(d\)
form is nonzero; where \(F=0\), every
point outside \(C_0\) has \(G\ne0\).
There is no fixed divisor because a
common hypersurface factor of all
members would divide both \(F\) and
\(G\), violating properness. On the
dense open \(D(F)\), the rational map
of \(W\) contains the full degree-\(d\)
Veronese coordinates from the
ratios of \(FL_i\); hence its image
has dimension three, so the system
is **not composed with a pencil**.
Classical characteristic-zero
Bertini irreducibility makes a
general member integral, while
Bertini smoothness makes it smooth
away from \(C_0\). Its generic
first-normal symbol along \(C_0\)
is nonzero for general \((\lambda,L)\):
this follows from the hypothesis
that \(F\) or \(G\) has normal order
one (and \(L|_{C_0}\ne0\) generically
when needed). Thus it is regular
at the generic point of \(C_0\);
all its singularities are isolated.
An integral hypersurface in
\(\mathbf P^3\) satisfies \(S_2\),
so Serre's \(R_1+S_2\) criterion
makes it normal. The open
\(\lambda\ne0\) gives
\((F,K)=(F,G)\). No integrality
of the original \(F\) or \(G\),
and no normality of the smaller
carrier, was assumed. \(\square\)

**Sharp scope.** When \(a=b\),
\(W\) is only the original pencil
and the non-pencil Bertini
irreducibility argument fails;
the sextic equal-degree proof
uses its separate factorization
argument. When **both** generators
have generic normal order at least
two, (NR1) does not produce a
normal carrier: every member of
\(W\) is then generically singular
along \(C_0\). The
[quadric normal-order bound](../carriers/sextic_pair_reduction.md#why-every-pair-is-generically-curvilinear)
implies **every** hypothetical
\((5,b)\) pair satisfies (NR1),
because a degree-five generator
cannot have normal order two.

**Consequences of the existing exact index theorem.**
On the new normal degree-\(b\)
carrier \(S=V(K_b)\), its degree-\(a\)
mate is \(F\). If \(5\le a\le9\),
the *minimal* mate degree on \(S\)
must be **exactly \(a\)**:
by the earlier degree-\(\le4\)
carrier exclusions every mate has
degree at least five, and no
proper positive divisor of
\(a\in\{5,\ldots,9\}\) is at least five.
Writing
\[
 g=\gcd(b,4),\quad
 \mu=b/g,\quad v=4/g,\quad
 R=\operatorname{lcm}_{P\in C_0}
     \operatorname{ind}_P(C_0\subset S),
\]
the all-degree formula §3 now gives
\[
 \boxed{\quad
 \operatorname{ord}(\mu C_0-vH_S)
  =\frac{a}{v}
  =\frac{R}{\gcd(R,\mu)},\qquad
 C_0^2=\frac{16}{b}.
 \quad}                                            \tag{NR2}
\]
Thus **every** hypothetical \((5,b)\)
pair with \(b>5\) has \(4\mid b\)
and admits a normal degree-\(b\)
carrier with a **nontrivial order-five**
class
\[
 \boxed{\Delta=(b/4)C_0-H_S,\quad 5\Delta=0.}
\]
This includes *originally nonnormal*
quintic carriers and every proposed
mate degree. Its conclusion is a
**necessary** condition on the
new degree-\(b\) carrier, not a
quintic exclusion.

For example, a hypothetical
\((6,8)\) pair with at least one
order-one generator has a
**normal octic** carrier with
a degree-six mate. Here
\(\mu=2,v=1,t=6\), so
\(R/\gcd(R,2)=6\) and **\(R=12\)**.
For \((6,10)\) under the same
order-one hypothesis, the normal
degree-ten carrier satisfies
\(R/\gcd(R,5)=3\), so
\(R=3\) or \(15\); the established
index-at-most-four exclusion
eliminates \(R=3\), forcing
**\(R=15\)**. These exact
index constraints are not
consequences of the old
equal-degree sextic normal-pencil
lemma. The actual-order-one
hypothesis is **not** known
for every \((6,8)\) or \((6,10)\)
candidate; no unconditional
mixed-sextic exclusion is claimed.

### A stronger all-\(b\) quintic consequence: forced high indices on the **other** surface

Apply (NR1)--(NR2) to an arbitrary
hypothetical proper \((5,b)\) sole-support
pair. The degree-five equation is
generically regular by restriction to
the unique quadric, and Bézout forces
\(b=4n\) with \(n\ge2\).
For a **general actual replacement**
of its degree-\(b\) equation,
\[
 K_b=G_b+F_5 L_{b-5},
\]
the degree-\(b\) surface is **normal**,
even if the original quintic is
nonnormal. On this normal surface
the degree-five mate is minimal,
and its primitive class has exact
order five:
\[
 \boxed{\quad
 \Delta=nC_0-H,\quad
 \operatorname{ord}(\Delta)=5,\quad
 \frac{R}{\gcd(R,n)}=5.\quad}             \tag{NQ1}
\]
Consequently if \(n=5^k n'\)
with \(5\nmid n'\),
\[
 \boxed{\quad v_5(R)=k+1,\qquad
     v_p(R)\le v_p(n)\ (p\ne5).\quad}     \tag{NQ2}
\]
In particular **some actual local
Cartier index along \(C_0\) on
the replacement degree-\(b\)
surface is divisible by
\(5^{v_5(n)+1}\)**.

Combining this exact torsion condition
with the **all-degree pointwise
index slope**
\[
 s_{\max}\ge
 \left\lceil\frac{4b^2-6b}{7b-16}\right\rceil
\]
first yields these **arithmetic
possibilities**. The stronger
moving-singularity theorem (MV5),
proved below from the **actual
source linear system**, then forces
\(R=m=5b/4\) for the **general
normal replacement carrier**:

| Original pair | Index lcm from torsion + slope alone | Actual lcm \(R=m\) after general replacement |
| --- | --- | --- |
| \((5,8)\) | \(10\) | **10** |
| \((5,12)\) | \(15\) | **15** |
| \((5,16)\) | \(10\) or \(20\) | **20** |
| \((5,20)\) | \(25\) | **25** |

For example, at degree eight the slope
requires \(s_{\max}\ge6\).
Equation (NQ1) allows only \(R=5\)
or \(10\); \(R=5\) would make every
local index at most five, and is
impossible. Thus a hypothetical
\((5,8)\) pair, *without assuming the
original quintic normal*, forces
an **actual index-ten point** on
a normal octic replacement carrier.
This is more precise
than merely requiring a
5-primary local class.
However, the moving
\(A_{m-1}\) singularity
mechanism below shows
that these high indices
may be **automatic**, rather
than an exclusion, on a
normal general replacement.

### A local countermodel: high index can be a **moving pencil singularity**

The exact-index conclusions (NR2)--(NQ2)
must not be mistaken for a new geometric
impossibility. Work on the **affine
threefold** \(\operatorname{Spec}k[t,u,v]\)
over an algebraically closed
characteristic-zero field, and put
\[
 F=u,\qquad
 G=tu+v^m,\qquad
 C=V(u,v),\quad m\ge2.
\]
The actual complete intersection
\((F,G)=(u,v^m)\) is curvilinear
of length \(m\), with **sole
reduced support \(C\)** on this
affine threefold. Its completed
local equations at any marked
point have the same form. For a scalar
\(\lambda\), make the permitted
generator replacement
\[
 K_\lambda=G-\lambda F
         =(t-\lambda)u+v^m.
\]
At the marked point \(t=\lambda\)
the surface \(K_\lambda=0\)
has a Du Val \(A_{m-1}\)
singularity \(xy+z^m=0\),
and the marked curve
\((u,v)\) represents the
standard local Weil class
of **exact Cartier index \(m\)**.
This is an elementary instance
of the accepted
[local class-group calculation](normal_carrier_symbolic_torsion.md#3-exact-index-formula-on-every-normal-c0-carrier).
The singular point **moves**
with \(\lambda\); \(F=u\)
is smooth at every marked point,
so the two original surfaces
do not have a common singular
point on \(C\).

**This is the general local form at a
simple moving zero, not just a
chosen artificial example.**
Let an actual sole-supported
proper pair have \(F=0\) **smooth
along \(C\) near \(P\)** and
generic intersection multiplicity
\(m\). Because \(V(F,G)\)
has sole reduced support \(C\),
the Cartier divisor cut by
\(G|_{V(F)}\) on the smooth
surface is **exactly \(mC\)**
near \(P\): a principal Cartier
divisor on a regular surface
has no separate punctual
component. In completed regular parameters
\(t,u,v\) with \(F=u,\ C=(u,v)\),
one can write
\[
 G=u\,h(t,u,v)+v^m w(t,u,v),
 \qquad w(0)\ne0.
\]
For any actual generator replacement
\(K=G+LF\), suppose
\((h+L)|_C\) has a **simple**
zero at \(P\). Then
\(x=h+L\) is a completed
local parameter transverse to
\((u,v)\), and taking an
\(m\)-th root of the unit \(w\)
gives the exact analytic equation
\[
 \boxed{K=xy+z^m,\quad
 C=(y,z),\quad
 \operatorname{ind}_P C=m.}             \tag{MV1}
\]
This is the standard \(A_{m-1}\)
marked surface germ. The
hypotheses are essential:
a multiple zero or failure
of local Cartier purity may
give different local structures.
The derivation depends only
on the *actual* source pair,
not on a chosen ADE
classification or a
conjectural complete normal
filtration.

**Interpretation:** in the
degree-\((5,4n)\) problem,
\(m=5n\), so a simple moving
zero can supply the **maximum
possible local index \(5n\)**
and fulfill the forced
order-five torsion condition
automatically. A proof that
the larger normal carrier
must have some index \(5n\)
would therefore not, on its
own, constrain the equation
family. The required research
bridge is the global
restriction on the simultaneous
locations and multiplicities
of these moving marked \(A\)
germs and the **actual**
homogeneous generators.

The model is *formal local*,
not a global projective
STCI construction. It proves
the following interpretative
limits on (NR1):

- Passing to a normal larger-degree
  carrier **can create** precisely
  the large local Cartier index
  required by its true global
  mate relation; the index's
  mere existence is therefore
  not an additional obstruction.
- The normal carrier's singular
  point need **not** be singular
  for both original generators.
  Neither the normal-replacement
  lemma nor its index consequences
  prove the unestablished
  common-singular-point conjecture.
- A genuine global restriction
  must control **how those moving
  singularities fit the finite
  dimensional homogeneous
  equation system**, including
  their global distribution,
  total first-symbol divisor,
  and exact normal-layer defects.

In particular, for the normal
replacement of a \((5,4n)\)
candidate, the forced index
\(5n\) (when attained in one
moving \(A_{5n-1}\) point)
is exactly the generic
transverse intersection length
\(m=5n\). This explains
why the table above may be
**necessary but not
discriminating**: it identifies
a geometric pattern to compare
with the ambient equations,
not a contradiction.

### The global moving-root theorem: the larger normal carrier has index \(m\)

There is a stronger consequence of the
local \(A_{m-1}\) calculation
when it is applied to the
**actual first-normal linear system
on the whole curve**. This is
an application of the established
normal splitting and Bertini;
the new comparison with Ellia's
primitive theorem is noted below.
**Independent review is required.**

Let \(a<b\), with the **smaller
generator \(F_a\) having generic
normal order one**, and
\(V(F,G)_{\mathrm{red}}=C_0\).
Put \(m=ab/4\ge2\).
Along \(C_0\) the two first-normal
symbols are **generically
proportional**, since
the generic CI length exceeds one.
In the balanced frame
\(N_{C/\mathbf P^3}^\vee
=\mathcal O(-7)^2\),
write their unique common saturated
direction as a binary vector
\((A,B)\) with coprime entries,
both of degree \(7-\ell\).
The two actual symbols are
\[
 \sigma_F=f(A,B),\qquad
 \sigma_G=g(A,B),
\]
with binary forms
\[
 \deg f=4a-14+\ell,\qquad
 \deg g=4b-14+\ell
       =\deg f+4(b-a).
 \tag{MV2}
\]
The case \(\sigma_G=0\) uses
\(g=0\) and \(\gcd(f,0)=f\);
all following assertions remain valid.

For a degree-\((b-a)\)
ambient form \(L\),
the first normal symbol
of \(K=G+LF\) is
\((g+f\,L|_C)(A,B)\).
The **fixed first-symbol base divisor**
\[
 B_{\mathrm{np}}=\operatorname{div}\bigl(\gcd(f,g)\bigr)
 \tag{MV3}
\]
is precisely the **common
singular scheme on \(C\)**
of the two original equations
at the level of first-symbol
vanishing; its underlying
support is the **nonprimitive
locus** of the actual CI.
Since \(L|_C\) comes from
the degree-\((b-a)\)
ambient linear system,
its variation is basepoint-free
and separates tangent directions
on the smooth embedded curve.
Consequently for general \(L\)
the remaining scalar zeros
are **simple**, disjoint
from \(B_{\mathrm{np}}\),
and number exactly
\[
 \boxed{\quad
 \alpha=4b-14+\ell-\deg B_{\mathrm{np}}
          \ \ge\ 4(b-a)>0.\quad}      \tag{MV4}
\]
They lie where \(F\) is smooth.
By the exact local form (MV1),
each is a marked
\(A_{m-1}^1\) point on
the **normal** replacement
carrier \(K=0\), with
local Cartier index **exactly \(m\)**.
The actual divisor
\(F|_{K=0}=mC\)
forces *every* local
Cartier index to divide \(m\).
Therefore
\[
 \boxed{\quad
 R(K,C)=m=\frac{ab}{4}.
 \quad}                                       \tag{MV5}
\]
This does not require
the original \(F\) to
be normal, smooth everywhere,
or its CI to be primitive;
it requires generic
normal order one for
the **smaller** generator.
The conclusion does **not**
follow when only the larger
\(G\) has order one.

Using the accepted exact
normal-carrier theorem with
\(g_0=\gcd(b,4)\),
\(\mu=b/g_0,\ v=4/g_0\),
the Bézout condition
\(4\mid ab\) gives \(v\mid a\)
and \(m=\mu(a/v)\). Hence
\[
 \boxed{\quad
 t=\frac{R}{\gcd(R,\mu)}
   =\frac{a}{v},\qquad
 b_{\min}(K)=vt=a. \quad}               \tag{MV6}
\]
Thus the smaller degree \(a\)
is automatically the
**minimal** mate degree
on the normal general
larger carrier, for
*every \(a\)* with its
generic normal order one,
not only for \(5\le a\le9\).
In particular, for every
hypothetical \((5,4n)\)
pair, \(R=5n\) **exactly**.
The prior alternative
\(R=10\) for a
\((5,16)\) replacement
cannot occur for a
*general* normal
replacement carrier:
\(R=20\) is forced.

**Why this is explanatory rather than an
exclusion.** The large required
index is supplied by the moving
simple \(A_{m-1}\) points
themselves; the normal-index
minimum mate theorem is therefore
**automatically saturated by
ordinary generator movement**.
What cannot be read off these
moving singularities is whether
the *fixed* nonprimitive locus
\(B_{\mathrm{np}}\) can carry
the additional normal-layer
and global geometry required
by a projective sole-support
pair.

For the same reason
Ellia's [2015 Theorem 12](../../literature/README.md#ellia)
already gives a stronger
uniform \(A_n^k\) conclusion
for a **primitive** CI; the
present generic-order-one
comparison only adds scope
when the pair is
**nonprimitive at finitely
many points**.

### The exact defect budget is concentrated at common singularities

Let \(D_{\mathrm{top}}\) denote
the *actual saturated top
multiplication defect* of
the curvilinear CI:
\[
 \deg D_{\mathrm{top}}
  =(m-1)\ell-4(a+b)+14.
 \tag{MV7}
\]
This is the accepted
Bănică--Forster/CI
duality identity, not a
new local model. For the
general normal carrier
\(K\), the pointwise
[socle/index identity](normal_carrier_symbolic_torsion.md#1-carrier-data-and-an-intrinsic-normalized-budget)
is
\[
 D_{\mathrm{top},P}
 =\left(\frac m{r_P}-1\right)A_P
  +\frac m{r_P}D_{r_P,P}.
\]
At every moving
\(A_{m-1}^1\) point,
\(r_P=m,\ A_P=1\) and
\(D_{r_P,P}=0\), so its
top defect is **zero**.
Therefore
\[
 \boxed{\quad
 \deg D_{\mathrm{top}}
 =\sum_{P\in B_{\mathrm{np}}}
    \left[
      \left(\frac m{r_P}-1\right)A_P
       +\frac m{r_P}D_{r_P,P}
    \right].\quad}                     \tag{MV8}
\]
For general \(L\), the
first-normal orders at fixed
points sum to
\(\deg B_{\mathrm{np}}\).
Equivalently the accepted
normal self-intersection
formula gives
\[
 \boxed{\quad
 \sum_{P\in B_{\mathrm{np}}}
       \frac{A_P+D_{r_P,P}}{r_P}
   =\frac{\deg D_{\mathrm{top}}
             +\deg B_{\mathrm{np}}}{m}.
 \quad}                                       \tag{MV9}
\]
This identifies precisely
how the **global top defect**
must be paid by the
**finite common-singular
locus** after the moving
singularities have exhausted
their primitive contribution.
It does not imply that
an arbitrary effective
\(B_{\mathrm{np}}\) or
defect divisor is realizable
by two homogeneous forms.

**Application of established
primitive classification.**
Ellia's Corollary 16
excludes a primitive
rational-quartic presentation
of degree \((5,b)\) for
**every \(b\)**, and excludes
\((6,6)\).
Therefore any hypothetical
pair in those degrees has
\(B_{\mathrm{np}}\ne0\):
**the two original
surfaces have a common
singular point on \(C\)**.
This is a **proved
degree-specific consequence**
of classical theory,
not the unrestricted
common-singular-point
assertion, which remains
unproved for all degrees.
For degree five the
smaller generator is
automatically generically
order one, so (MV8)--(MV9)
locate its nonprimitive
escape at finitely many
points. The entirely-thick
\((6,8)\) case has no
generic order-one
generator and is not
covered by (MV2)--(MV9).

**Scope.** The table does not
exclude the listed singularities.
Normality of the larger member
comes from Bertini on the
specific equation system;
the table says nothing about
the normality or conductor of
the original quintic. It converts
the entire **all-mate quintic**
problem into a family of precise
higher-degree normal-index
necessary conditions, without
substituting the \((5,8)\)
ADE quintic theorem for an
arbitrary mate degree. All these
consequences use the accepted
all-degree index and slope
theorems but the new mixed-degree
Bertini bridge (NR1) remains
pending independent review.

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
