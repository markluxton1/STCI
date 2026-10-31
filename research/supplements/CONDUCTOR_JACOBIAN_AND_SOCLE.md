# Conductor, transverse differential, and the actual top socle

The first part proves the full ideal-level conductor–Jacobian identity near a smooth Cartier inverse curve. The second gives the exact pointwise top-socle identity [R-0036](../results/pointwise_conductor_socle_defect.md), its normalized-thickening colength, and parity consequence. These are different implications from [fixed-carrier descent](FIXED_CARRIER_DESCENT_AND_CARTIER_MODELS.md): the second part starts with an **already existing actual supported pair**, rather than constructing its mate. The source proofs and independent reconstructions are combined without a new promotion.

The normal-index Frobenius/free-power identity is owned by [normal-index and socle theory](NORMAL_INDEX_SOCLE_AND_TORSION.md). The comparison below invokes that identity only for its stated ordinary-power lattice, preserving its separation from saturated Bănică–Forster defects.

## Local residue identity and global contact

## 1. Exact local statement

Let `X=(F=0)` be an integral hypersurface in a smooth threefold over an
algebraically closed field of characteristic zero. Let
`nu:S->X` be its finite normalization. Let `C subset X` be a smooth curve
such that the full reduced inverse image is a single smooth Cartier curve
`c`, mapped isomorphically to `C`. Suppose `X` is regular at the generic
point of `C`, and `S` is regular along `c`.

Only a neighborhood of `c` is involved. Finite duality identifies the
conductor ideal on `S` with an invertible ideal

    conductor O_S = O_S(-B),
    omega_S = conductor O_S tensor nu*omega_X.          (1)

Here `B` is effective and has no component `c`. Invertibility in this
neighborhood follows from (1), since both dualizing sheaves are invertible.

Let `A` be the full common-zero divisor of the normal differential

    alpha:O_c(c) -> N_C/ambient.

Let `D_F` be the full common-zero divisor of the actual first normal
symbol of `F`, viewed as a section of
`N_C/ambient^* tensor O_C(X)`. Thus a local first symbol
`a(t)y+b(t)z` contributes
`min(ord_t a,ord_t b)` to `D_F`.

**Proposition.** There is an equality of effective divisors on `c`:

    D_F = B|c + A.                                    (2)

This is a local equality with multiplicities, not an inference from the
degrees of the two sides. It allows isolated rank drops of `alpha`.
If the differential of `nu` has rank two everywhere along `c`, then
`A=0` and (2) specializes to `D_F=B|c`.

## 2. Direct residue and finite-duality proof

Fix a closed point of `c`, and complete the local rings. Choose ambient
coordinates `(x,y,z)` with `C=(y,z)`. The function `x|C` is a uniformizer.
Its pullback, together with a local equation `u` of `c`, is a regular
system of parameters `(t,u)` on `S`, with `nu*x=t`. Write

    nu(t,u) = (t,Y(t,u),Z(t,u)),    Y,Z in (u).

The common-zero ideal of `alpha` in `O_c=k[[t]]` is exactly

    (Y_u(t,0), Z_u(t,0)).                             (3)

Choose a local generator `h` of the conductor on `S`. On the common
function field, use the hypersurface residue generator

    eta = dx wedge dy / F_z = -dx wedge dz / F_y

of `omega_X`, using either expression where its denominator is nonzero.
At least one denominator and the corresponding numerator derivative are
nonzero generically: the normalization is birational and the map is
generically an isomorphism. Pullback gives

    nu*eta = Y_u dt wedge du / (F_z composed with nu)
           = -Z_u dt wedge du / (F_y composed with nu).

Under the common-field identification in finite duality, the generator
`h nu*eta` of the right side of (1) is a generator of `omega_S`.
Consequently it is a unit multiple of `dt wedge du`. There is therefore
a single unit `epsilon` in `k[[t,u]]` such that

    F_z composed with nu = epsilon h Y_u,
    F_y composed with nu = -epsilon h Z_u.             (4)

These equalities are first obtained in the function field and then hold
in the regular local ring. Restricting (4) to `u=0` yields the exact ideal
identity

    (F_y(t,0,0),F_z(t,0,0))
      = (h(t,0)) (Y_u(t,0),Z_u(t,0))                 (5)

in the DVR `k[[t]]`. Since `F(t,0,0)=0`, the remaining partial
`F_x(t,0,0)` is identically zero. Thus the left side of (5) is precisely
the common-zero ideal of the first normal symbol. The two factors on
the right define `B|c` and `A`. Orders in (5) prove (2) point by point.
Faithful flatness of completion gives the original local statement.

The use of finite duality is concrete here: for the finite birational
extension `O_X subset nu*O_S` with common function field,

    Hom_O_X(nu*O_S,O_X)
      = {q in K(X):q O_S subset O_X}
      = conductor.

Tensoring by the invertible `omega_X` is the dualizing module of `S`.
Thus (1) uses the actual conductor, including all closed-point contact;
no reduced conductor support or first-symbol substitute is inserted.

## 3. Relation to the Jacobian-conductor formula

The coordinate identities (4) are the smooth-normalization case of
Ragni Piene, *Ideals associated to a desingularization*, Lecture Notes
in Mathematics 732 (1979), 503--517, Theorem 1 and Corollary 1,
[DOI 10.1007/BFb0066659](https://doi.org/10.1007/BFb0066659).
They give the ideal formula

    Jac(X) O_S = conductor O_S * Fitt_0(Omega_S/X).

The modern explicit coordinate statement is Theorem 3.1 of
Nuño-Ballesteros and Fernández-Hernández,
[*Disentangling mappings defined on ICIS*](https://link.springer.com/article/10.1007/s13163-024-00507-3):
the partial derivatives of an image equation pull back to a common
conductor generator times the signed maximal minors of the differential.
An [institutional full-text copy](https://riunet.upv.es/bitstreams/26a18ad6-9f8e-442c-828d-81c30b29162a/download)
is also available. This reference corroborates (4); the proof above
supplies the algebraic local argument used in this note.

## 4. Global class and the three fixed-C0 targets

Now suppose the ambient threefold is `P3`, `X` has degree `a`,
`C` has degree `d` and genus `g`, and write `H=nu*O_X(1)`.
Since `omega_X=O_X(a-4)`, (1) gives, wherever `S` is Gorenstein,

    B ~ (a-4)H-K_S.                                  (6)

If `S` is globally Gorenstein, this is a global Cartier-divisor identity.
Otherwise it is the local identity near `c` needed below. Adjunction
along the smooth Cartier curve gives

    B.c = d(a-4)+c^2-(2g-2).                         (7)

For the accepted fixed rational quartic `C0`, the singleton Cartier-lift
classification leaves three targets:

| Normalization target | `a` | `c^2` | `B.c` |
| --- | ---: | ---: | ---: |
| Smooth quadric, `c` of type `(1,1)`, `H=2c` | 8 | 2 | 20 |
| Quadric cone, `c` a smooth Cartier conic, `H=2c` | 8 | 2 | 20 |
| `P2`, `c` a line, `H=4c` | 16 | 1 | 51 |

The quadric cone is singular only at its vertex, which does not lie on
the smooth Cartier conic `c`. It is Gorenstein globally, so (6) is valid
globally and the smooth local proof applies all along `c`. No assertion
that this normalization is smooth at the vertex is needed.

## 5. Scope and warning

Formula (2) identifies the conductor contact using **both** the actual
carrier first symbol `D_F` and the transverse differential divisor `A`:

    B|c = D_F-A.

The divisor `A` alone is not the full conductor contact. This distinction
is compatible with the accepted warning that first-normal data alone
does not recover the conductor or higher horizontal multiplicity. Here
finite normalization, its actual conductor via duality, and the smooth
Cartier lift are explicit hypotheses and inputs.

The proposition does not treat a singular normalization along the lift,
a non-Cartier lift, several inverse branches, an inverse curve of higher
degree over `C`, or a carrier singular at the generic point of `C`.
It supplies no automatic bound on split residual phase orders.



## Exact top-socle divisor for an actual pair

## 1. Statement and definition of the defect

Let `M` be a smooth threefold over an algebraically closed field of
characteristic zero, and let `C` be a smooth curve. Suppose

```
Y=(F,G),               Supp(Y)_red=C,
```

is an actual complete intersection. Assume the integral carrier
`X=(F=0)` is regular at the generic point of `C`. Let `nu:S -> X` be
its finite normalization. Require that the full reduced inverse support
of `C` is a singleton smooth Cartier curve `c`, mapped isomorphically
to `C`, and that `S` is smooth along `c`.

Let the actual conductor near `c` be the invertible ideal

```
conductor O_S=O_S(-B),
```

where `B` is effective and has no component `c`. Let `A` be the full
zero divisor, with common-zero multiplicities, of

```
alpha:O_c(c) -> N_(C/M).
```

Write `nu*G=unit*u^n` locally along `c`, where `u=0` defines `c` and
`n>=2`. Thus the actual generic normal algebra is curvilinear of
length `n`. Put `J=I_C O_Y` and `Soc(Y)=Ann_(O_Y)(J)`. The accepted
socle theorem identifies this as an invertible sheaf on `C`; purity
gives `J^n=0`, and `J^(n-1)` is an invertible subsheaf. Define its
actual top-power/socle defect divisor `D_n` by

```
J^(n-1)=Soc(Y)(-D_n).                                 (1)
```

Equivalently this is the defect of the multiplication map from
`L^(tensor(n-1))` to the full actual socle, where
`L=(J/J^2)_tf=O_c(-c)(-A)`. Multiplication onto `J^(n-1)` is surjective:
it is generated by products of `n-1` elements of `J`; terms from `J^2`
change such a product by `J^n=0`, and torsion in a first-layer input
maps to zero in the torsion-free target. Consequently no extra defect
is inserted between this multiplication image and the actual top
ordinary power.

**Theorem.** There is an equality of actual divisors on `c=C`:

```
D_n=(n-1)A-B|c.                                       (2)
```

In particular, for every closed point `P`,

```
(n-1)A_P >= (B|c)_P.                                 (3)
```

This is stronger than an equality of degrees or divisor classes. No
primitive multiple-curve hypothesis, absence of first-layer torsion,
or global retraction onto `C` is assumed.

## 2. The actual CI embeds in the normalized thickening

Fix a closed point `P` of `C` and its unique inverse point on `c`.
Choose completed ambient coordinates `(t,y,z)` with `C=(y,z)` and
`t|C` a uniformizer. The pullback of `t`, together with a local
equation `u` of `c`, gives regular parameters on `S`. Thus

```
R=Bbbk[[t]],
Lambda=R[[y,z]]/(F,G),
nu(t,u)=(t,Y(t,u),Z(t,u)),          Y,Z in (u).
```

The full inverse-support hypothesis makes

```
g=nu*G=gamma(t,u)u^n,              gamma a unit.       (4)
```

Indeed the regular local surface ring is factorial, and `c` is the
only prime in the support of the pullback mate. Generic carrier
regularity identifies its multiplicity with the actual generic
complete-intersection length `n`.

The finite map induces

```
Lambda -> T=R[[u]]/(u^n).                             (5)
```

This map is injective. Its kernel vanishes at the generic point of
`C`, where normalization is an isomorphism. It therefore has finite
support. But `Lambda` is a pure one-dimensional complete intersection
and has no nonzero finite-length submodule. Equivalently, `Lambda`
is finite free over `R`: support on `C` gives finiteness, and the
parameter `t` is a nonzerodivisor by Cohen--Macaulay purity. Its rank
is `n`. The target is also free of rank `n`, so (5) is generically an
isomorphism with a finite-length cokernel.

That cokernel is retained. The proof does not replace the actual
complete intersection by the normalized thickening.

## 3. The relative Jacobian generates the actual socle

Let

```
j=F_y G_z-F_z G_y,
Sigma=Ann_Lambda((y,z)Lambda).
```

For the Artin-fiber input, Eisenbud–Ulrich, [Duality and Socle Generators for Residual Intersections, Theorem 8.5](https://www.math.purdue.edu/~bulrich/papers/Duality-and-Socle-180119.pdf), treats a finite local Gorenstein algebra whose dimension is prime to the characteristic and, in its complete-intersection case, identifies the Jacobian socle generator. The local fibers here have dimension n. In characteristic zero (and, by this same input, when the characteristic does not divide n), the generic Artin complete-intersection Jacobian theorem puts `j` in
the socle after inverting `t`. Since `Lambda` is `R`-torsion free,
the equalities `yj=zj=0` then hold in `Lambda` itself. Hence `j in Sigma`.

The relative socle `Sigma` is a free rank-one `R`-module. Its rank is
one generically, and it is an `R`-submodule of the finite free module
`Lambda`. It is also saturated in `Lambda`: if `t a in Sigma`, then
`t ya=t za=0`, so torsion freeness gives `ya=za=0`. It follows that

```
Sigma/t Sigma -> Lambda/t Lambda
```

is injective. The special fiber

```
Lambda/t Lambda
 = Bbbk[[y,z]]/(F(0,y,z),G(0,y,z))
```

is an Artin complete intersection of length `n`, because `Lambda`
is free of rank `n`. The image of `j` is precisely its Jacobian
determinant and is a nonzero socle generator in characteristic zero.
Thus `j` is nonzero in `Sigma/t Sigma`, and Nakayama gives

```
Sigma=R j.                                           (6)
```

This proves the actual generator statement at the closed point. It
does not assume in advance that taking socles commutes with base
change. In particular, no hidden nonunit specialization factor is
allowed in (6).

## 4. Exact images of the socle and top ordinary power

Let `h` be a local generator of the actual conductor. The accepted
residue identities give a single unit `epsilon` with

```
F_y composed with nu = -epsilon h Z_u,
F_z composed with nu =  epsilon h Y_u.                (7)
```

Since the ambient coordinate `t` pulls back to the chosen parameter
`t`, the chain rule and (4) give

```
j composed with nu
 = -epsilon h (Z_u(G_z composed with nu)
                        +Y_u(G_y composed with nu))
 = -epsilon h partial_u(g)
 = -epsilon h (n gamma u^(n-1)+gamma_u u^n).
```

In `T`, this is

```
j composed with nu
 = -n epsilon(t,0) gamma(t,0) h(t,0) u^(n-1).          (8)
```

The coefficient other than `h(t,0)` is a unit. Therefore (6) yields
the exact image

```
im(Sigma)=h(t,0)R u^(n-1).                            (9)
```

Write

```
a=A_P=min(ord_t Y_u(t,0),ord_t Z_u(t,0)),
b=(B|c)_P=ord_t h(t,0).
```

The second order is finite because the conductor has no component
`c`. Write `Y=u a_1(t)+O(u^2)`, `Z=u a_2(t)+O(u^2)`. Every product
of `n-1` elements of the actual ideal `J=(y,z)Lambda` maps to
`u^(n-1)` times a coefficient in `(a_1,a_2)^(n-1)`; all higher
`u` terms vanish. Conversely the monomials in `y,z`, with arbitrary
coefficients from `R`, realize that whole coefficient ideal. Hence

```
im(J^(n-1))
 = (Y_u(t,0),Z_u(t,0))^(n-1) R u^(n-1)
 = t^((n-1)a)R u^(n-1).                              (10)
```

The injection (5) shows in particular that `J^n=0` and that its actual
top power is exactly the lattice in (10). Comparing (9) and (10)
gives

```
length_R(Sigma/J^(n-1))=(n-1)a-b >=0.                 (11)
```

By definition, this length is `D_(n,P)`. Equality (2) follows point by
point; faithful flatness of completion recovers the original local
divisor multiplicities.

This computation also confirms the suggested generator comparison:
after a local invertible linear change of the ambient normal coordinates,
one normal function `w` has
`nu*w=t^a unit*u+O(u^2)` and maps to a generator of the torsion-free
first layer. Then `w^(n-1)/j` has order exactly `(n-1)a-b`. Formula
(10) avoids choosing `w` and retains the entire actual top ideal.

## 5. Consequences across all mate powers

For a fixed carrier and its fixed normalization data, (3) supplies
necessary conditions in every mate multiplicity at once:

- `Supp(B|c) subset Supp(A)`. A conductor contact with `A_P=0` excludes
  every mate satisfying these hypotheses, regardless of its degree.
- At each point with `A_P>0`,
  `n>=1+ceil((B|c)_P/A_P)`.
  Their maximum is a simultaneous necessary lower bound for `n`.
- The entire actual defect is determined by the same divisor formula
  for every permitted mate multiplicity. No closed-point correction
  or higher-jet defect has been omitted from `D_n`.

Taking degrees recovers the accepted conductor-contact inequality.
In projective space, the accepted adjunction expression
`B.c=d(a-4)+c^2-(2g-2)` identifies it with the earlier transverse
socle bound. That numerical consequence is used as a consistency
check, not as a substitute for the new pointwise proof.

The pointwise necessary conditions neither bound mate multiplicity
above nor settle the residual phase/torsion conditions for conductor
descent. Vanishing of the displayed defect does not by itself supply
a projective mate.

## 6. Exact colength in the thickening on the carrier normalization

There is a further pointwise consequence using the accepted ordinary
[Frobenius/free-powers lattice identity](NORMAL_INDEX_SOCLE_AND_TORSION.md#2026-10-14-generalization-normal-index-socle-theorem),
Section 2. Keep the local notation above and choose `w in J` mapping to
a generator of the torsion-free first layer, so

```
nu*w=t^a q(t)u+O(u^2),                 q(t) a unit.
```

The ordinary free-powers lattice is
`Lambda_0=R[w] subset Lambda`, isomorphic to `R[v]/(v^n)`, with basis
`1,w,...,w^(n-1)`. The accepted lattice identity is

```
length_R(Lambda/Lambda_0)=n D_(n,P)/2.                 (12)
```

Relative to this basis and `1,u,...,u^(n-1)` of `T`, the inclusion
`Lambda_0 -> T` is triangular, with diagonal

```
1, t^a q, (t^a q)^2, ..., (t^a q)^(n-1).
```

Consequently its determinant has valuation `n(n-1)a/2`; the higher
coefficients of `nu*w` make no contribution. The actual inclusions
`Lambda_0 subset Lambda subset T` give the exact sequence

```
0 -> Lambda/Lambda_0 -> T/Lambda_0 -> T/Lambda -> 0.
```

Subtracting lengths and applying (2) yields the new exact formula

```
length_R(T/Lambda)
 = n((n-1)a-D_(n,P))/2
 = n(B|c)_P/2.                                       (13)
```

Thus if `delta_n` is the effective divisor recording these local
colengths, one has

```
2 delta_n=n B|c.                                     (14)
```

In particular, **odd `n` forces every coefficient of `B|c` to be
even**. This is a necessary condition on every actual CI in this
lane; arbitrary normalized support or a graded construction alone
does not supply the lattice inclusions used in the proof.

Here `T=O_S/(nu*G)` locally is the **normalized thickening**, meaning
the pullback thickening on the normalization of the carrier `X`.
It is not asserted to be a normalization of the nonreduced scheme
`Y`. Formula (13) measures the finite colength of the actual CI
inside this specified pullback thickening.

Finally the accepted
[length-two/three primitive theorem](NORMAL_CARRIER_SYMBOLIC_TORSION.md#2026-10-14-generalization-normal-carrier-symbolic-triple-certificate),
Section 2, gives `D_n=0` for `n in {2,3}`. Hence in these two lengths
the pointwise divisor relation specializes to

```
B|c=(n-1)A.                                         (15)
```

These are consequences of accepted lattice and small-rank premises;
neither earlier proof was rerun.

## Scope of the pointwise statement

The proposed identity passes under all the explicit hypotheses. The
two potentially delicate bridges both pass: purity gives the
injection into `T`, and saturation plus the Artin-fiber Jacobian
theorem gives the actual relative-socle generator at every point.
Finite colength of `Lambda` in `T` contributes no additional term
to (2).

Characteristic zero is substantive for this proof: the factor `n`
in (8) and nonvanishing of the Artin Jacobian must be retained. The
same argument works when the characteristic does not divide `n`;
there is no claim here in characteristic dividing `n`. For example,
`F=y,G=z^p` in characteristic `p` has a nonzero socle but zero
Jacobian. Generic carrier regularity, singleton degree-one inverse
support, the Cartier lift, smoothness of the normalization along the
lift, and the actual supported complete intersection are also
substantive hypotheses. No extension to several inverse branches,
non-Cartier lifts, singular normalization along the lift, or entirely
thick carriers is inferred.

The universal STCI question and unrestricted characteristic-zero
`C0` remain open.

## Consolidation review

Independent consolidation review reconstructed the residue ideal identity, actual-CI injection into the pullback thickening, closed-fiber Jacobian socle generation, exact pointwise divisor, colength and parity consequences. It accepted the stated geometric and characteristic hypotheses, with the prime-to-n Artin-fiber input checked in the primary Eisenbud–Ulrich theorem. The ordinary-power lattice premise remains owned by the linked normal-index theorem; no saturated-filtration equivalence is asserted.
