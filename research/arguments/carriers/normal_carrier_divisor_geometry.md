# Divisor equality and local socle criteria on a normal carrier

**Status:** independently reviewed Hodge-equality, index and local-socle theorems. The Hodge equality criterion and exact-order argument were reconstructed during consolidation; the local criterion retains the normal-carrier index/socle theorem, primitive-triple certificate and separately scoped low-index exclusions as inherited premises at their exact hypotheses. This characterizes mate existence on a specified normal carrier; it does not exclude arbitrary normal carriers. The fixed-carrier Hodge and exact-index tests in §§1,3 now use the stronger all-characteristic Picard theorem of Česnavičius–Scholze; this strengthening, as distinct from the previously reviewed characteristic-zero statements, awaits independent review. The local socle and generator-replacement results retain their own characteristic hypotheses. **The newly consolidated all-degree cyclic-cover Euler formula in §3.5 and its quintic/sextic identifications have been checked algebraically against the recorded cases, but are not yet independently reviewed as a new proof package.**

## 1. A mate is equivalent to Hodge-index equality on a normal hypersurface

Let `k` be algebraically closed, of arbitrary characteristic. Let

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

Thus, for normal hypersurface carriers in any characteristic, there is no
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

For this upgrade use the strongest available complete-intersection theorem (extending the characteristic-zero saturation result of Hartshorne--Polini, Lemma 7.6):
Česnavičius–Scholze, [*Purity for flat cohomology*](https://annals.math.princeton.edu/2024/199-1/p02),
Corollary 7.2.3, proves that `Pic(X)/Z[H]` is torsion-free for
every projective complete intersection of dimension at least two over a
field. Cotner–Zavyalov, [*Lefschetz theorems in flat cohomology and applications*](https://www.cambridge.org/core/journals/compositio-mathematica/article/lefschetz-theorems-in-flat-cohomology-and-applications/8556201EDB51D7F2F76F5950A800CD64),
Theorem 1.1.8, also establish triviality of the numerically trivial Picard
scheme. Both statements apply to singular hypersurfaces in arbitrary
characteristic. Thus L is linearly trivial.

In particular some positive multiple of Delta is principal. The
canonical section of the resulting positive Cartier multiple of C,
transported through its equivalence to dH, lifts to an ambient degree-d
form using the hypersurface sequence and
`H^1(P3,O(d-a))=0`. Its restriction is nonzero and has exactly the
required divisor. This proves (1). Hodge index gives (3) iff (4).
No local Jacobian formula, rationality, or characteristic-zero Bertini
is needed here. Those hypotheses are retained wherever used later.

**Broader fixed-carrier scope.** Hartshorne--Polini, Lemma 7.6 ([2015](https://arxiv.org/abs/1301.3222)), already gives hyperplane saturation for possibly nonnormal surfaces in characteristic zero. The 2024 theorem extends it, rather than supplying a new characteristic-zero principle. The [normalized Hodge/ almost-Cartier theorem AC1--AC3](fixed_carrier_descent_and_cartier_models.md#the-normalized-hodge-matrix-and-downstairs-almost-cartier-indices) gives this exact mate criterion with normality dropped, provided the support is generically regular on the carrier and its actual downstairs almost-Cartier class has finite order modulo Picard. It also describes the relation to the normalization and conductor descent indices.

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

**Further scope (pending independent review).** In characteristic
zero the [actual almost-Cartier power--socle extension](normal_carrier_symbolic_torsion.md#normality-is-unnecessary-the-actual-almost-cartier-power-theorem)
and [intrinsic divisor comparison](normal_index_socle_and_torsion.md#intrinsic-divisor-on-a-possibly-nonnormal-generically-regular-carrier)
extend equations (3)--(5), the full local defect and symbolic-triple
bounds, and the all-index-at-most-four exclusion to possibly
nonnormal integral carriers regular at the generic point of the
smooth support. The index in those statements is now the local
almost-Cartier index **on the image surface**, not its normalization.
The normalization conductor remains a mechanism for computing
these indices or proving their infinitude. This changes the scope
of the defect test, not the crepant ADE hypotheses of the next section.

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

The flat-cohomological Lefschetz theorem in §1 gives the stronger
integral statement: RC is Cartier, and its class has torsion image in
Pic(X)/Z[H] by existence of a mate. That quotient is torsion-free, so

```
RC ~ (eR/a)H,       a | eR,       mu | R.           (8)
```

Conversely, any mate multiplicity is a positive multiple of R by
Cartierness. The ambient restriction map is surjective, so RC itself is
realized by a mate. In particular the actual invariants are

```
t = R/mu,    b_min = v t = eR/a,                   (9)
n_min = R,   b = k b_min (k positive integer).      (10)
```

The prior formula t=R/gcd(R,mu) agrees, but the saturation theorem
rules out mu not dividing R. Its divisibility condition

```
a divides e R                                     (11)
```

strictly strengthens the earlier self-intersection integrality
a divides e^2 R. This uses no genus restriction and holds in every
characteristic on a fixed normal hypersurface; no assertion about the
characteristic of the local power-socle formulas follows. The older
rational-ample torsion-detection theorem remains valuable for general
normal surfaces not known to have a saturated hyperplane class.

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
   mu | R,
   t=R/mu,
   b_min=4R/a,
   n_min=R,
   a | 4R.
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

<a id="47-unequal-degree-pairs-can-acquire-an-actual-normal-carrier"></a>
## 4.7 All-degree actual normal-carrier replacement

**Status:** unified all-degree consequence of classical Bertini and Serre's criterion; independent mathematical review required. Equal degrees are included.

**Normal-replacement theorem (NR1).** Over an algebraically closed field of characteristic zero, let \(C\subset\mathbf P^3\) be any smooth integral curve and let homogeneous forms \(F_a,G_b\), \(a\le b\), define a proper intersection with sole reduced support \(C\). Set
\[
 W=kG_b+F_aH^0(\mathbf P^3,\mathcal O(b-a)).
\]
Then a general member of \(W\) is normal integral if and only if at least one of \(F,G\) has generic normal order one along \(C\). In this case a general member has the form
\[
 K_b=\lambda G_b+F_aL_{b-a},\qquad
 \lambda\ne0,\qquad (F_a,K_b)=(F_a,G_b).
 \tag{NR1}
\]
In equal degrees this is precisely the original pencil; two independent general members are normal and define the same CI ideal.

**Proof.** The base support of \(W\) is exactly \(C\): away from \(V(F)\) some degree-\((b-a)\) form is nonzero (also for \(a=b\)), while on \(V(F)\setminus C\), \(G\ne0\). The system has no fixed surface. The characteristic-zero theorem on variable singular points ([Kleiman, *Bertini and his two fundamental theorems*, Theorem 4.1](https://arxiv.org/abs/alg-geom/9704018)) makes a general member smooth away from \(C\). Its first-normal symbol at the generic point of \(C\) is nonzero on a nonempty parameter open if either original first symbol is nonzero: multiplication by a general \(L\) does not kill the \(F\) symbol. Thus the general member is regular at every codimension-one point. A nonzero hypersurface is Cohen–Macaulay, hence \(S_2\); Serre's criterion gives normality without a prior irreducibility hypothesis. Every positive-degree hypersurface of \(\mathbf P^3\) is connected (by the hypersurface exact sequence, \(H^0(\mathcal O_{V(K)})=k\)); a connected normal Noetherian scheme is integral. Finally \(\lambda\ne0\) is a nonempty open condition and gives the ideal equality. Conversely, if both symbols vanish generically, every member is singular at the generic point of \(C\), a codimension-one point, so cannot be normal. \(\square\)

**What does the work.** The precise inputs are the base support, characteristic-zero Bertini smoothness, and generic regularity at its curve component. Neither the dimension of the system's image, a non-pencil Bertini irreducibility hypothesis, the degree-four exclusion, nor any degree bound is needed. The local condition is intrinsic to the CI: its generic transverse Artin algebra has embedding dimension at most one, equivalently at least one generator has order one. For multiplicity \(m>1\) this is generic curvilinearity. When the generic embedding dimension is two, no change within this generator system gives a normal member. This does not rule out other presentations of the same *reduced support* in different degrees. No positive-characteristic extension is asserted.

For the fixed quartic, the [quadric normal-order bound](sextic_pair_reduction.md#why-every-pair-is-generically-curvilinear) implies that every hypothetical \((5,b)\) pair satisfies NR1. The graph bound supplies this hypothesis for every \((6,6)\) pair. In contrast the entirely-thick \((6,8)\) regime remains outside NR1.

**Consequences of the existing exact index theorem.** On a normal replacement \(S=V(K_b)\) the degree-\(a\) mate cuts \(mC\), \(m=ab/4\), and \(C^2=16/b\). Write \(g=\gcd(b,4)\), \(\mu=b/g\), \(v=4/g\) and \(R=\operatorname{lcm}_{P\in C_0}\operatorname{ind}_P(C_0\subset S)\). The minimal mate degree is \(4R/b\), which divides \(a\) and is at least five. Put \(n_b=v\lceil5/v\rceil\). If \(a<2n_b\), or if the original pair has minimal degree product among sole-support pairs, minimal mate degree must equal \(a\). In the former case a proper divisor of \(a\) is at most \(a/2<n_b\); in the latter a smaller actual mate gives a smaller pair. In either case
\[
 \operatorname{ord}(\mu C-vH)=a/v=R/\mu,\qquad R=ab/4,\qquad C^2=16/b. \tag{NR2}
\]
This includes \(5\le a\le9\), and also \((10,10)\), since \(n_{10}=6\). In particular its order-one sector has \(R\mid25\) and \(R/\gcd(R,5)=5\), yielding \(R=25\), minimal mate degree ten and exact order five for \(5C-2H\). The order-one \((6,8)\) and \((6,10)\) sectors likewise give \(R=12,15\): in the second case the alternative \(R=3\) is excluded directly by \(10\mid4R\). None is a nonexistence result. The entirely-thick sectors are not covered. For arbitrary degrees the moving-root condition below supplies another sufficient condition for minimal mate degree \(a\).

<a id="equal-degree-pencils-below-degree-ten-the-sextic-proof-extends-to-octics"></a>
**Extension to arrangements.** For a proper complete intersection
with reduced support a finite union of integral curves, the same
Bertini–Serre proof gives a general normal integral larger carrier
if and only if the generic transverse embedding dimension is
at most one on **each** component. There are only finitely many
generic points, so the required nonvanishing open conditions
intersect. In characteristic zero this applies to every reduced
CI arrangement, and to any arrangement all of whose component
multiplicities are at most three: two equations of local order
at least two in the regular two-dimensional ambient local ring
have intersection length at least four (the local intersection
multiplicity inequality). In particular every proper quartic
CI with a cycle of distinct translates of total multiplicity
four and at least two components admits a general normal
pencil carrier, including the doubled two-support exceptional
pencils. This does not make the individual components
Q-Cartier at their intersections. The total Cartier condition
and [exact Hodge matrix test](../torus/fixed_surface_restriction_lifts.md#normal-carriers-a-complete-geometric-description-of-the-arrangement-monoid)
are the appropriate fixed-carrier formulation. This extension
requires independent review.

### Every-member integrality and arithmetic factor bounds

The separate factor result concerns **every** member of a generator system, not the normality of a general member. It also has a stronger arithmetic formulation. If a proper sole-\(C_0\) pair has degrees \((a,b)\), \(a\le b\), every irreducible factor \(h\) of an actual degree-\(b\) replacement \(K_b\) with \((F_a,K_b)=(F_a,G_b)\) has an actual mate \(F_a\). Hence
\[
 \deg h\ge5,\qquad 4\mid a\deg h.
\]
The first condition uses the complete quartic carrier exclusion; the second uses degree exhaustion. Define \(n_a\) to be the least integer at least five divisible by \(4/\gcd(a,4)\). Thus \(n_a=5,6,8\) when \(a\equiv0,2,\text{odd}\pmod4\), respectively. If \(b<2n_a\), every such \(K_b\) is integral, including absence of repeated factors. For an equal-degree pencil the argument applies to **every nonzero member** by choosing an independent pencil mate.

For \((d,d)\), Bézout requires even \(d\). All possible equal-degree pencils with \(d=6,8,10\) therefore have integral members: at \(d=10\), a quintic factor is forbidden by \(4\nmid50\). The first numerical equal-degree factorization threshold of these two bounds is **12**, not ten. At \(d=12\) degrees \(6+6\), for example, are not excluded by these bounds alone. This is not a construction or assertion of existence. For arbitrary degrees, NR1 gives general-member normality independently of this arithmetic factor threshold.

One can remove the factor threshold by minimizing the degree product of a hypothetical supported pair: any reducible or nonreduced generator of the same degrees supplies a smaller-degree factor with the other generator as mate, contradicting minimality. In particular every member of an equal-degree pencil of a degree-product-minimal pair is integral, without a degree restriction. The new pair obtained by factor descent need not define the original thick scheme; only support is preserved.

For a hypothetical \((8,8)\) order-one pair NR1 gives a normal octic, with \(16C_0\sim8H\). The exact index theorem applied to its primitive class \(2C_0-H\) gives \(t\mid8\) and \(b_{\min}=t\). The quartic exclusion forces \(t\ge5\), hence \(t=8\), and \(R/\gcd(R,2)=8\), \(R\mid16\) give
\[
 \boxed{R=16,\qquad \operatorname{ord}(2C_0-H)=8.}
 \tag{EQ8}
\]
This is an index necessity, not nonexistence. Neither NR1 nor the graph bound handles every entirely-thick \((8,8)\) pair. For higher degrees minimal mate degree need not equal the degree of the given mate merely for arithmetic reasons; the moving-root result below gives a separate sufficient condition.

### A stronger all-\(b\) quintic consequence: forced high indices on the **other** surface

For every hypothetical \((5,b)\) pair, \(b=4n\), \(n\ge2\), after the quartic exclusion and Bézout. The quadric restriction gives the smaller generator generic order one, so NR1 gives a normal degree-\(b\) carrier even if the original quintic is nonnormal. On it the minimal mate degree is five by the all-mate quartic exclusion. The strengthened exact index theorem gives
\[
 \Delta=nC_0-H,\quad \operatorname{ord}\Delta=5,\quad
 R=5n. \tag{NQ1}
\]
Thus every normal larger carrier with a quintic mate, not merely a
general replacement, has global Cartier index \(5n\).
The moving-root theorem still adds the important geometric conclusion
that this full index is attained at individual moving simple zeros;
a least common multiple alone need not be attained at one point.

### A local countermodel: high index can be a **moving pencil singularity**

On affine three-space take \(F=u,\ G=tu+v^m,\ C=V(u,v)\), \(m\ge2\). The ideal is exactly \((u,v^m)\); nevertheless \(G-\lambda F=(t-\lambda)u+v^m\) has a moving marked \(A_{m-1}\) singularity of Cartier index \(m\) at \(t=\lambda\). The first generator is smooth everywhere on \(C\). Thus high indices alone do not force a common singular point or a nonprimitive CI. This is a local control, not a projective construction.

More generally, let an actual sole-support pair have \(F\) smooth at a point \(P\) of \(C\) and generic length \(m\). In completed parameters \(t,u,v\), with \(F=u,\ C=(u,v)\), the restricted divisor on the smooth surface is exactly \(mC\), hence
\[
 G=u\,h+v^m w,\qquad w\text{ a unit}.
\]
If \((h+L)|_C\) has a simple zero at \(P\), set \(x=h+L,\ y=u\) and \(z=v w^{1/m}\). These are completed parameters and the actual replacement has marked equation
\[
 K=xy+z^m,\qquad C=(y,z),\qquad \operatorname{ind}_P C=m. \tag{MV1}
\]
This is the usual end-marked \(A_{m-1}\) germ, not a novel singularity type.

### The global moving-root theorem: the larger normal carrier has index \(m\)

**Unified first-symbol system (independent review required).** Assume the fixed char-zero quartic, \(a\le b\), \(m=ab/4>1\), with at least one generic order-one generator. The generic first symbols span the same saturated line in the conormal bundle (otherwise the transverse length would be one). Denote the quotient line by \(\mathcal O(-\ell)\), its kernel by \(M=\mathcal O(\ell-14)\), and write the actual symbols using a coprime binary vector \((A,B)\) of degree \(7-\ell\):
\[
 \sigma_F=f(A,B),\quad \sigma_G=g(A,B),\qquad
 \deg f=4a-14+\ell,\quad \deg g=4b-14+\ell. \tag{MV2}
\]
A zero symbol means the zero section of the indicated line bundle. Let
\[
 B_{\rm np}=\operatorname{div}\gcd(f,g),\quad \beta=\deg B_{\rm np}. \tag{MV3}
\]
The gcd is defined also if exactly one symbol is zero. Its support is precisely the nonprimitive locus of the actual CI: at a point, the ideal has a smooth local equation if and only if one of its generators has nonzero first normal there. Its multiplicities are the orders of the common first-symbol ideal, not the top-socle multiplicities.

The first-normal scalar system of \(K=\lambda G+LF\) is
\(\langle g,f\cdot H^0(\mathcal O_{\mathbf P^3}(b-a))|_C\rangle\).
Its fixed divisor is exactly \(B_{\rm np}\) because the ambient multiplication system is basepoint-free, including constants for \(a=b\). Removing the gcd leaves a basepoint-free linear system on the smooth curve. In characteristic zero a general divisor is reduced by Bertini on a curve; a general section also avoids every fixed point after division by the gcd. Thus the full divisor \(A_K\) for a general normal replacement is
\[
 A_K=B_{\rm np}+U,\qquad U\text{ reduced, disjoint from }B_{\rm np},
 \quad \alpha=\deg U=4b-14+\ell-\beta. \tag{MV4}
\]
The statement includes \(\alpha=0\), where \(U=0\). At every point of \(U\), \(F\) is smooth: if \(f(P)=0\) outside \(B_{\rm np}\), then \(g(P)\ne0\) and \(\lambda g(P)+f(P)L(P)\ne0\). Apply MV1 to obtain the marked \(A_{m-1}\) singularity with local index \(m\). Every index divides \(m\), because the actual mate cuts \(mC\). Hence
\[
 \alpha>0\quad\Longrightarrow\quad R(K,C)=m. \tag{MV5}
\]
With \(g_0=\gcd(b,4),\ \mu=b/g_0,\ v=4/g_0\), we have \(m=\mu(a/v)\). By the exact index theorem,
\[
 \alpha>0\quad\Longrightarrow\quad
 \operatorname{ord}(\mu C-vH)=a/v,\quad b_{\min}(K)=a. \tag{MV6}
\]

There are three distinct cases; the normality conclusion of NR1 covers all of them.

* If \(a<b\) and \(f\ne0\), then \(\beta\le4a-14+\ell\), so \(\alpha\ge4(b-a)>0\). In particular, for every hypothetical \((5,4n)\) pair, \(R=5n\). The strengthened fixed-carrier index theorem already forces \(R=5n\); the new information here is attainment by individual moving singularities.
* If \(a=b\), then \(\alpha>0\) exactly when the two actual first symbols are linearly independent over \(k\): after the gcd, a basepoint-free system of positive degree cannot have dimension one. The zero-moving-degree branch has a unique pencil member with generic order at least two (the kernel of the rank-one scalar-symbol map); the remaining general members are still normal. MV5--MV6 need not hold by this moving-root argument when \(\alpha=0\).
* If \(a<b\) and \(f=0\), the nonzero \(g\) is fixed up to scalar, so \(\alpha=0\); normal replacement still works but does not produce moving first-symbol zeros.

The primitive theorem of [Ellia](../../literature/README.md#ellia) gives stronger uniform marked singularity conclusions when the whole CI is primitive. The argument here accounts for the finite nonprimitive locus without assuming it empty. The large index supplied by moving roots is an automatic consequence of actual generator movement, not an independent impossibility.

### The exact defect budget is concentrated at common singularities

This conclusion does **not** need \(a<b\), a nonzero smaller symbol, or any moving roots. Let \(D_{\rm top}\) be the actual saturated top multiplication divisor of the curvilinear CI. The [CI duality and Frobenius identity](../normal-geometry/curvilinear_genus_and_defects.md#5-complete-intersection-duality-fixes-a-top-divisor) give
\[
 \deg D_{\rm top}=(m-1)\ell-4(a+b)+14,\qquad
 2\sum_i B_i=mD_{\rm top}. \tag{MV7}
\]
Here \(B_i\) are the ordinary-layer torsion divisors, not \(B_{\rm np}\). Wherever \(D_{\rm top}\) vanishes, the local monomial lattice proof shows that the finite free local algebra equals its monogenic subalgebra, hence the CI is primitive there. Conversely a smooth local containing surface gives a primitive multiple divisor with no multiplication defect. Thus the supports of \(D_{\rm top}\) and \(B_{\rm np}\) agree, independently of the carrier choice. Equality of the divisors themselves is not asserted.

For **any actual normal degree-\(b\) replacement**, the [local power--socle theorem](normal_index_socle_and_torsion.md#local-power-socle-theorem-and-bounded-index-exclusion) gives
\[
 D_{{\rm top},P}=(m/r_P-1) A_{K,P}
                     +(m/r_P)D_{r_P,P}.
\]
Both summands are nonnegative integers. At any singular point outside the nonprimitive locus we already have \(D_{{\rm top},P}=0\), so \(A_{K,P}>0\) implies **\(r_P=m,\ D_{r_P,P}=0\)**, even if that particular member has a multiple symbol zero. The general member has only simple zeros outside \(B_{\rm np}\). For it \(A_{K,P}=\operatorname{mult}_P B_{\rm np}\) at fixed points, hence the exact pointwise accounting is
\[
 \deg D_{\rm top}=\sum_{P\in B_{\rm np}}
 \left[(m/r_P-1)A_{K,P}+(m/r_P)D_{r_P,P}\right], \tag{MV8}
\]
\[
 \sum_{P\in B_{\rm np}}\frac{A_{K,P}+D_{r_P,P}}{r_P}
   =\frac{\deg D_{\rm top}+\beta}{m}. \tag{MV9}
\]
This is an identity between *actual* defects and Cartier indices of the same scheme, not an independent bound from moving singularities. It also explains why the cyclic cover and Hodge equality computations share so much of their numerical input.

Ellia's finite primitive-degree list excludes an everywhere-primitive rational-quartic CI outside his ten pairs; the complete quartic exclusion removes \((4,7)\) for \(C_0\). Consequently any hypothetical pair outside the remaining nine unordered degree pairs has a common singular point on \(C_0\), including entirely-thick pairs. For the generically curvilinear branch this is precisely \(\deg B_{\rm np}>0\). This does not prove the claim in the nine eligible primitive degree pairs, and the finite list is not a list of constructed CIs.

### Reduced common first-normal divisor: a uniform marked ADE and rank test

**Status: new generalization of the independently reviewed sextic reduced-gcd proof, pending independent review.** Assume the hypotheses of the unified first-symbol system and suppose \(B_{\rm np}\) is reduced (possibly empty). Then the generic normal replacement is smooth off \(C\), and *all* of its singularities on \(C\) are simple first-symbol zeros. At each such point the quadratic form has a nonzero paired curve/normal term and Hessian rank at least two; isolatedness gives an \(A_{r-1}\) singularity, and the marked smooth curve is end-marked by the first-symbol vanishing order one. This is exactly the local marked calculation already used in the [sextic reduced-gcd argument](sextic_pair_reduction.md#the-common-first-normal-divisor-must-be-nonreduced), using [Ellia, Definition 8 and Lemma 10](https://arxiv.org/abs/1409.3801). There is no sextic hypothesis in this local step.

More explicitly, choose completed parameters so the normal surface is \(tu-w^r=0\) and \(C=(u,w)\). The divisor of \(u\) is \(rC\), so the actual mate cutting \(mC\) is a unit times \(u^{m/r}\) on this normal germ. This requires \(r\mid m\); at a fixed point where both original equations are singular \(1<r<m\) (the case \(r=m\) gives a primitive local CI), and at moving points \(r=m\). The completed local CI is
\[
 k[[t,u,w]]/(tu-w^r,u^{m/r}).
\]
Over \(k[[t]]\), the basis \(u^j w^i\), \(0\le j<m/r,\ 0\le i<r\), and the relation \(w^r=tu\) identify the saturated normal layers. Their multiplication divisors have coefficient \(\lfloor i/r\rfloor\) in order \(i\), \(0\le i<m\); in particular the top coefficient is \(m/r-1\). This is an actual local model, rather than a restriction on the ADE labels alone.

Consequently the entire reduced-gcd stratum obeys the single combinatorial/geometric test
\[
 \begin{split}
 \deg D_{\rm top}&=\sum_{P\in B_{\rm np}}(m/r_P-1),\\
 \alpha&=4b-14+\ell-\beta,\qquad \beta=\#B_{\rm np},\\
 \alpha(m-1)+\sum_{P\in B_{\rm np}}(r_P-1)
    &\le h^{1,1}(\widetilde{V(K_b)})-1
      = b(b^2-4b+6)-3-2\binom{b-1}{3}.
 \end{split} \tag{RG1}
\]
The inequality follows from the negative-definite exceptional ADE root lattice and the positive-square hyperplane class; the surface invariants are those of the smooth degree-\(b\) hypersurface because its only singularities are rational double points (equivalently use a characteristic-zero complex model for Hodge numbers). Use binomial zero for \(b<4\). This recovers the sextic rank bound 85 and the three rows of its fixed \(A_2\), moving \(A_8\) argument; its last row still requires the curve-specific constant-direction primitive-triple obstruction. It does not prove that every admitted assignment of indices, defects or points occurs globally.

**An all-degree arithmetic consequence requiring no rank bound.** If every prime factor of \(m\) is \(1\bmod4\), then \(m\equiv1\bmod4\), and each contribution \(m/r_P-1\) in RG1 is divisible by four. But MV7 gives \(\deg D_{\rm top}\equiv14\equiv2\bmod4\). This is impossible. Thus in this entire multiplicity class **every generically curvilinear sole-support pair must have a nonreduced common first-normal divisor**. Examples include hypothetical \((5,20)\) and the order-one sector of \((10,10)\), both with \(m=25\). The result excludes the reduced-defect stratum, not those pairs or their entirely-thick sectors. More generally RG1 forces congruence modulo \(\gcd_{p\mid m}(p-1)\) for composite \(m\); it retains the individual local divisors and exact global rank test when the congruence is vacuous.

## 5. What was removed, and what remains

The new theorem removes **global lifting as a separate hypothesis or
obligation in the normal branch**. More precisely, after `Q`-Cartierness,
the scalar equality `C^2=e^2/a` (or equivalently equality in (4)) forces:

* torsion of the primitive Weil relation;
* its exact order from actual local indices;
* an effective Cartier divisor supported exactly on `C`;
* and an ambient hypersurface lifting that divisor.

The remaining boundaries are exact.

1. **Normality versus generic regularity.** The fixed-carrier
   [AC1–AC3 theorem](fixed_carrier_descent_and_cartier_models.md#the-normalized-hodge-matrix-and-downstairs-almost-cartier-indices)
   extends the Hodge criterion to generically regular integral carriers
   using the actual downstairs almost-Cartier index. The
   [S2 local extension](normal_carrier_symbolic_torsion.md#normality-is-unnecessary-the-actual-almost-cartier-power-theorem)
   likewise extends the local power–socle formula. Both extensions await
   independent review. Generically thick carriers still require their
   inverse branches and conductor descent.

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

4. **Characteristic.** The fixed-carrier numerical and Picard steps in
   Sections 1 and 3 now have an all-characteristic proof (pending
   independent review). The local power–socle theorem separately requires
   its stated tame hypotheses; characteristic-zero Bertini and the
   characteristic-zero low-degree exclusions are not transferred by
   Picard saturation alone.

5. **Other generic algebras.** If both defining equations have generic
   normal order at least two, neither one is a normal order-one carrier and
   the generic algebra need not be curvilinear. That entirely-thick branch
   requires the conormal/socle and formal-root program, supplemented by the [normalized branch and first-graph identities](numerical_surface_pullback.md#branch-valuations-and-the-actual-first-blowup). On a smooth sole-support strict intersection, [Lefschetz compression](../residuals/blowup_residual_geometry.md#lefschetz-compression-on-ample-strict-carriers) applies once a suitable ample strict carrier is generically regular; this is not automatic for arbitrary thick pairs.

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
