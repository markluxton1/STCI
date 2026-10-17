# Normal carriers: extremal-ray sufficiency and the all-degree local certificate

Date: 2026-10-17. Author: `normal_generalization`.

Status: **NEW PROOF AND SYNTHESIS, PENDING INDEPENDENT AUDIT.** The
normal-carrier torsion/index theorem, the intrinsic local power--socle
comparison, the symbolic-triple defect certificate, the accepted exclusion
of integral `C0` carriers of degree at most four, and the all-index-at-most-
four normal exclusion are premises. They are not reverified here. The new
step is the extremal-ray sufficiency theorem in Section 1 and its use in
Section 2 to turn the intrinsic local divisor budget into a necessary **and
sufficient** criterion for a mate. Sections 3--5 assemble, without enlarging
their scope, the strongest presently proved all-degree consequences.

This note does not exclude unrestricted normal carriers and does not resolve
the fixed `C0` or universal STCI problem.

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

The proof isolates the characteristic-zero input precisely: it suffices in
any characteristic to know that every numerically trivial line bundle on
`X` is trivial. The local Jacobian/socle results used later have their
separate tame-index restriction.

## 2. The intrinsic local divisor is a necessary-and-sufficient mate test

Now suppose `C` is smooth. Retain the accepted notation from the intrinsic
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

2. **Unbounded actual local indices.** No universal bound on `r_P` follows
   from smoothness of `C0`, the carrier degree, or surface multiplicity.
   The local models `xy-z^r=0` with the smooth curve `(x,z)` have arbitrarily
   large index and zero primitive defect. Equations (13)--(17) say exactly
   how such high indices must be distributed globally but do not exclude
   them.

3. **Curve-specific symbolic obstruction.** The improvement from the
   general balanced-rational threshold to the fixed `C0` certificate uses
   the accepted nonzero constant-direction primitive-triple obstruction.
   An analogous obstruction is not proved for every balanced rational
   curve.

4. **Characteristic.** Section 1 works whenever numerically trivial line
   bundles on `X` are trivial. Characteristic zero supplies this for normal
   hypersurfaces through the accepted Picard inputs. The local
   power--socle theorem extends when every actual index is prime to the
   characteristic, but wild indices and a characteristic-`p` replacement
   for the global Picard step remain open.

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
