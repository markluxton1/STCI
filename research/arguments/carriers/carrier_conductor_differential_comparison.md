# Carrier conductor contact and the actual transverse differential

**Scope and status.** Independently reviewed comparison, with
an application to the fixed characteristic-zero quartic. The theorem concerns actual supported pairs on generically
regular integral carriers. It describes the gluing regimes left available
for realizing such intersections, not a presumption of nonexistence.

The full surface-normalization conductor is the object here. It is not
the conductor of the quadratic separation of a nonreduced intersection.
The actual transverse differential likewise differs from the carrier
hypersurface's first normal symbol. The
[local supported-section theorem](square_descent_and_singular_gluing.md#smooth-conductor-contact-is-bounded-by-the-actual-normal-differential)
supplies the precise comparison; its constructive singular controls explain
why smooth-contact hypotheses cannot be dropped.

## Exact statement

Let S be an integral hypersurface of degree a>=5 containing C0,
generically regular along C0, and let `nu:X->S` be its normalization.
Suppose that S has a proper sole-supported mate of some positive
degree. Then the following two conditions cannot both hold:

1. X is smooth along the reduced inverse curve c over C0.
2. The full scheme-theoretic conductor downstairs is smooth at every
   point where it meets C0.

The mate and generic regularity force the full reduced inverse to be
the single curve c, mapping isomorphically to C0. Thus these are
conditions on the actual normalization and its actual gluing scheme.
There is no global Gorenstein-normalization assumption, no assumption
that the conductor is integral, and no restriction on the mate degree.

Consequently a hypothetical carrier in this generic-regularity regime
must have a normalization singularity on c or a singular conductor
contact on C0. Carriers singular generically along C0 are outside the
statement. Smoothness of the reduced support of a nonreduced conductor
does not satisfy condition 2.

## Divisor and conductor degrees

Write b for the mate degree and H for the pulled-back hyperplane
class. Its actual section has a Cartier zero divisor supported on
the full inverse of C0. This divisor has no isolated components on
the normal surface. Generic regularity of S along C0 gives just one
prime over its generic point, of degree one. Hence the reduced inverse
is c alone. A finite birational map from an integral curve to the
normal curve C0 is an isomorphism, so `c~=C0~=P1`.

Assume condition 1. The curve c is Cartier: this holds along c since
X is smooth there, and away from c its ideal is the unit ideal. For
some positive integer m the actual divisor relation is

    m c ~ b H,   H^2=a,   H.c=4.

Intersecting with H and c gives

    4m=ab,   c^2=16/a.                                   (1)

In particular c^2 is integral, but that divisibility is not needed
for the contradiction below.

Let I be the full conductor ideal on X. Finite duality, together with
the hypersurface identity `omega_S=O_S(a-4)`, gives near c

    I ~= omega_X tensor nu^*(omega_S)^(-1).

Indeed `Hom_A(B,A)` is the conductor for a finite birational
normalization A subset B, and duality identifies
`Hom_A(B,omega_A)` with `omega_B`. The relative-duality identification
is [Stacks, Lemma 49.15.1](https://stacks.math.columbia.edu/tag/0BUL),
with the finite-ring module described in
[§49.2](https://stacks.math.columbia.edu/tag/0BUK).
Smoothness near c makes I invertible there. Write I=O_X(-D) on that
neighborhood. Generic regularity means D does not contain c, so its
restriction is an effective finite contact divisor on c.

Adjunction on the smooth neighborhood of c gives
`K_X.c=-2-c^2`. Thus the total full-conductor contact is

    Btot = D.c = 4(a-4)-K_X.c
         = 4a-14+16/a.                                  (2)

These degrees are degrees of line bundles restricted to c; no globally
Cartier canonical divisor on X is being assumed.

## The actual differential has a smaller zero divisor

The conormal splitting
[STCI-R-0020](../../results/quartic_conormal_characteristic_jump.md)
gives `N^*_(C0/P3)=O_P1(-7)^2`. The actual normalization morphism,
followed by the inclusion of S in P3, induces

    O_P1(-7)^2 -> N^*_(c/X)=O_P1(-c^2).                  (3)

This map is generically nonzero because normalization is an
isomorphism at the generic point of C0. Its two components are
sections of O_P1(7-c^2). Their common zero divisor therefore has
degree at most `7-c^2`. Let h_p be its local order. Then

    sum_p h_p <= 7-16/a.                                (4)

This is the differential of the actual finite map in the transverse
direction along c. It is not the first-symbol divisor of a chosen
hypersurface equation.

Assume condition 2 as well. At every conductor contact, the actual
conductor sequence for a hypersurface is locally

    0 -> R -> B/I -> omega_R -> 0,

where R is the downstairs conductor ring. Smooth R is a discrete
valuation ring and omega_R is free of rank one. Consequently B/I
is a free quadratic R-algebra. The pulled-back mate is an actual
element of the carrier ring with divisor m c. The
[local supported-section comparison](square_descent_and_singular_gluing.md#smooth-conductor-contact-is-bounded-by-the-actual-normal-differential)
therefore applies and gives

    b_p <= 2 h_p,                                       (5)

where b_p is the full conductor contact at that point. This local
statement permits every positive m and does not require a separate
root, parity assumption, or generic non-descent of a root.

Summing (5) and using (2), (4) gives

    4a-14+16/a <= 14-32/a,
    4a^2-28a+48 <= 0,
    (a-3)(a-4) <= 0.                                    (6)

This is impossible for a>=5. A normal carrier smooth along C0 is
also covered: its conductor contact is zero, already contradicting
the positive value in (2).

## Geometric content and boundaries

The hypersurface dualizing sheaf and adjunction specify how much
conductor gluing the actual supported divisor needs along c. The
balanced ambient conormal bundle limits how much the normalization
map can lose rank there. Smooth conductor gluing converts each unit
of differential vanishing into at most two units of conductor
contact. The required and available totals are incompatible.

This extends the contact mechanism beyond the quintic source and
beyond (5,8), without classifying its singularities. It does not give
an unrestricted nonexistence theorem: singular normalization points,
singular conductor contacts and generic singularity along C0 are
precisely missing local regimes. An actual construction could use one
of those regimes. Numerical compatibility or an abstract gluing model
still does not provide its projective embedding and mate.

The separate
[quintic integral-conductor exclusion](quintic_gorenstein_normalizations.md)
handles one singular-normalization source and its unique singular
conductor vertex by additional actual geometry. Neither theorem
subsumes the other's hypotheses.

### The amount singular conductor contacts must supply

Keep the smooth-normalization hypothesis, but allow the full conductor
to be singular where it meets C0. Let Bad be those singular contacts.
The other contacts contribute `b_p-2h_p<=0`, so the same degree
calculation gives the necessary inequality

    sum_(p in Bad) (b_p-2h_p) >= 4a-28+48/a.             (7)

Since c is Cartier, (1) also gives a|16. For a>=5, the possibilities
are a=8 and a=16, with required excess in (7) at least 10 and 39,
respectively. This quantifies the missing local contribution; it does
not bound it from above or exclude either degree. Singular conductor
gluing can exceed the smooth-contact bound, as the actual local
controls in the [componentwise square control](square_descent_and_singular_gluing.md#an-actual-supported-square-with-componentwise-descent)
demonstrate.

### A criterion for other smooth space curves

Let C be any smooth connected space curve of degree d and genus g,
under the same carrier, mate, generic-regularity, smooth-normalization
and smooth-conductor-contact hypotheses. Define ell(N) to be the
maximum degree of a line subbundle of `N=N_(C/P3)`; this definition
does not use the maximum slope of subbundles of arbitrary rank.
Then a necessary condition is

    d(a-4)+2-2g+3d^2/a <= 2 ell(N).                     (8)

The proof retains the same actual geometric objects. The mate gives
`c^2=d^2/a`; adjunction gives
`D.c=d(a-4)+2-2g+c^2`. Dualizing the actual transverse differential
and saturating its image gives a line subbundle

    N_(c/X)(H_diff) subset N_(C/P3),
    c^2+deg H_diff <= ell(N).

The local comparison bounds D.c by twice deg H_diff, yielding (8).
For a rational curve with normal splitting O(n1) plus O(n2),
ell(N)=max(n1,n2). The fixed quartic has ell(N)=7 and g=0, recovering
(6). This is a reusable necessary criterion, with no claim that its
local hypotheses cover all STCI carriers or that the inequality is
sufficient for constructing one.

Characteristic zero is used in the local supported-section lemma,
including separability of a positive power in the generic quadratic
conductor algebra. The balanced splitting also changes in
characteristic two. This proof makes no assertion about that case
and does not conflict with its known STCI construction.

## Characteristic, applications and review

The proof is characteristic zero: the local section lemma uses
separability of every positive power and absorption of units, not only
invertibility of two. The conormal splitting also has its separate
characteristic-two jump. No unchanged positive-characteristic carrier
exclusion is asserted; the actual
[every-positive-characteristic quartic construction](../arithmetic/positive_characteristic_constructions.md)
remains available.

The normalization-index mechanism and explicit projective controls are in
[normalization indices and power descent](normalization_indices_and_power_descent.md).
The distinct resolved-fiber-degree comparison has its full application in
[the toric normalization account](quintic_non_gorenstein_toric_sources.md).
The Gorenstein-normalized quintic theorem handles a specified singular
normalization regime by extra actual geometry; neither theorem subsumes
the other's hypotheses. An actual construction can seek singular
normalization along the inverse curve, singular conductor gluing, or a
carrier generically singular along its support. The inequality alone is
not sufficient for realizing any of those alternatives.

Independent frozen-source review reconstructed full inverse support,
Cartier relations, conductor duality near the curve, adjunction, the
actual differential and the local-to-global comparison. It also checked
the singular-contact excess and the general line-subbundle criterion,
including the saturation direction and the a=8 or16 consequence. No
quintic root, global Gorenstein normalization, ADE hypothesis, new
computation or unrestricted STCI conclusion enters this general proof.


## Consolidated historical supplement: `research/supplements/CONDUCTOR_JACOBIAN_AND_SOCLE.md`

Original mathematical content, hypotheses, qualifications, and proof status preserved verbatim. Relative links retain their historical source context.

# Conductor, transverse differential, and the actual top socle

The first part proves the full ideal-level conductor–Jacobian identity near a smooth Cartier inverse curve. The second gives the exact pointwise top-socle identity [R-0036](../../results/pointwise_conductor_socle_defect.md), its normalized-thickening colength, and parity consequence. These are different implications from [fixed-carrier descent](fixed_carrier_descent_and_cartier_models.md): the second part starts with an **already existing actual supported pair**, rather than constructing its mate. The source proofs and independent reconstructions are combined.

The normal-index Frobenius/free-power identity is owned by [normal-index and socle theory](normal_index_socle_and_torsion.md). The comparison below invokes that identity only for its stated ordinary-power lattice, preserving its separation from saturated Bănică–Forster defects.

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
[Frobenius/free-powers lattice identity](normal_index_socle_and_torsion.md#2026-10-14-generalization-normal-index-socle-theorem),
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
[length-two/three primitive theorem](normal_carrier_symbolic_torsion.md#2026-10-14-generalization-normal-carrier-symbolic-triple-certificate),
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



## Consolidated historical supplement: `research/supplements/PROJECTION_SUPPORT_AND_DIFFERENTIAL_OBSTRUCTIONS.md`

Original mathematical content, hypotheses, qualifications, and proof status preserved verbatim. Relative links retain their historical source context.

# Projection support and differential obstructions

Work over an algebraically closed characteristic-zero field with the fixed embedded curve `C0=[s^4:s^3t:st^3:t^4]`. The examples below separate two independent failure mechanisms in the necessary Cartier singleton models of [R-0002](../../results/cartier_singleton_lift.md): actual full inverse support can pass while infinitesimal descent fails; another actual projection can fail because of isolated inverse points. Neither family exhausts its normalization model.

The plane result and its broader two-fixed-coordinate sublane are [R-0017](../../results/singleton_plane_conductor_descent.md). The quadric families have completed independent source reconstruction and retain their stated review scopes. The exposition integrates the original proofs and the audit's unique denominator and extra-corner corrections. No symbolic computation is a premise.

## Plane normalization: actual support but no descending power

## 1. An explicit finite normalization

On `P2_(s:t:z)` put `c=(z=0)`, and define

    U0=s^4,
    U1=s^3 t,
    U2=s t^3+z^4,
    U3=t^4+s^3 z.                                      (1)

The four sections are basepoint free. If `s!=0`, `U0!=0`; if `s=0`,
the two possibly nonzero coordinates are `z^4,t^4`, which cannot vanish
together at a projective point. Thus they define a morphism

    f:P2 -> P3,             f*O(1)=O(4).

This morphism is finite. A positive-dimensional projective fiber contains
a curve, but `O(4)` would have degree zero on that curve, contradicting
ampleness. Properness and finite fibers imply finiteness.

On `s!=0`, write `x=t/s`, `n=z/s`, and use the target chart `X0!=0`.
Then

    f(x,n)=(x, x^3+n^4, x^4+n),
    x=X1/X0,
    n=X3/X0-(X1/X0)^4.                                 (2)

In particular the map is birational and is an isomorphism on this affine
chart. Its integral image `X` is a hypersurface, and the finite birational
map from normal `P2` is its normalization. The degree formula gives
`deg X=O(4)^2=16`.

For a completely explicit equation put

    A=X0^3 X3-X1^4,
    B=X0^2 X2-X1^3.

Then the image is exactly

    F=A^4-X0^13 B=0.                                   (3)

Indeed its dehomogenization at `X0=1` is

    (X3-X1^4)^4-X2+X1^3=0,

an irreducible polynomial linear in `X2`. Equation (3) is its degree-sixteen
homogenization, with no factor `X0` since `F|X0=0=X1^16`. This also checks
the degree and the signs directly. On the source,

    f*A=s^15 z,             f*B=s^8 z^4.

## 2. Full reduced inverse support, including infinity

Restriction to `z=0` gives exactly `C0`. Its parametrization is an
isomorphism: the coordinates `X1/X0=t/s` and `X2/X3=s/t` provide the
two endpoint parameters.

On `s!=0`, membership of the image in `C0` forces

    x^3+n^4=x^3,            x^4+n=x^4,

so `n=0`. On `s=0`, the image is `[0:0:z^4:t^4]`. The only point of
`C0` with its first coordinate zero is `[0:0:0:1]`; thus the image lies
on `C0` exactly when `z=0`. Consequently

    (f^-1 C0)_red=c,             f|c:c -> C0 is an isomorphism. (4)

There are no isolated extra inverse points. This is an actual realization
of the full-singleton plane normalization model before the mate condition.

## 3. Every positive mate degree is excluded

Suppose a homogeneous form `G` of positive degree `b` cut out exactly
`C0` set-theoretically on `X`. Its pullback is a nonzero section of
`O_P2(4b)` whose zero support, by (4), is exactly `c`. Its divisor must
therefore be `4b c`, and

    G(U0,U1,U2,U3)=lambda z^(4b),       lambda in k*.     (5)

Rescale `G` to make `lambda=1`. Set `s=0`. Since the map
`[t:z] -> [z^4:t^4]` is surjective onto `P1`, equation (5) forces the
polynomial identity

    G(0,0,Z,T)=Z^b.                                    (6)

Differentiate (5) in `s` and set `s=0`. The first, second, and fourth
coordinates in (1) have zero derivative there. The third has derivative
`t^3`; by (6), `G_X2|X0=X1=0=b X2^(b-1)`. Thus

    0=b t^3 z^(4b-4),                                  (7)

an impossible polynomial identity in characteristic zero.

**Conclusion (R-0017):** the integral degree-sixteen carrier (3) contains
literal `C0`, has the required Cartier singleton degree-one inverse lift,
and has no set-theoretic mate in any positive degree.

This excludes this carrier, not all integral degree-sixteen carriers.

## 4. An eleven-parameter family with the same obstruction

Let `alpha!=0` and let `P(s,t,z)` be an arbitrary homogeneous cubic. Replace
(1) by

    U0=s^4,
    U1=s^3 t,
    U2=s t^3+alpha z^4,
    U3=t^4+z P(s,t,z).                                 (8)

There are eleven affine coefficients before quotienting coordinate
equivalences: one for `alpha` and ten for `P`. Every member is basepoint
free and finite by exactly the preceding argument. Its restriction to
`c` is the literal `C0`. On `s!=0`, the third coordinate forces `n^4=0`
for any inverse point over `C0`, hence `n=0`. On `s=0`, `U2=alpha z^4`
forces `z=0` for an image on `C0`. Thus every member has full reduced
inverse support exactly `c`; birationality is considered separately below.

The boundary map is

    [t:z] -> [alpha z^4 : t^4+zP(0,t,z)].                (9)

It is basepoint free and has degree four. In particular it is surjective.
If (5) held for (8), restriction to `s=0` would force

    G(0,0,Z,T)=(Z/alpha)^b.                             (10)

The derivative `G_X3` therefore vanishes on the entire boundary plane
`X0=X1=0`. Thus the arbitrary value of `zP_s(0,t,z)` contributes zero
when differentiating the pullback identity. The same calculation gives

    0=(b/alpha)t^3 z^(4b-4),                            (11)

again impossible. Every member of (8), including the nonbirational
members, has no mate on its image. Only its birational members belong to
the degree-sixteen normalization model in STCI-Q-0001.

## 5. Exact birational locus of (8)

Write uniquely

    P=A3(s,t)+zB2(s,t)+z^2 C1(s,t)+delta z^3.

Over `K=k(x)`, where `x=t/s`, the target function field is generated by

    n^4,
    A3(1,x)n+B2(1,x)n^2+C1(1,x)n^3+delta n^4.           (12)

The extension `K(n)/K(n^4)` is Galois with group `mu4`, acting by
`n -> zeta n`. The fixed subgroup of the second generator in (12)
consists precisely of those `zeta` for which every nonzero coefficient
of `n^j` has `zeta^j=1`. Therefore

- If `A3!=0` or `C1!=0`, the map is birational, and its image has degree 16.
- If `A3=C1=0` and `B2!=0`, its generic degree is 2 and image degree is 8.
- If `A3=B2=C1=0`, its generic degree is 4 and image degree is 4.

These degrees refer to the function-field degree of `P2` over its image.
For the second and third cases `P2` is not the normalization of the image;
they are not extra normalizations in STCI-R-0002. The first case is the
nonempty explicitly determined open locus of actual normalizations within
this family. The all-degree obstruction (11) holds throughout that locus.

## 5a. Every full-singleton projection with the first two coordinates fixed

There is a stronger exclusion than the explicit family (8). Consider any
four sections of `O_P2(4)` with

    U0=s^4,              U1=s^3 t,
    U2=s t^3+z A3(s,t,z),
    U3=t^4+z B3(s,t,z),                                (15)

where `A3,B3` are arbitrary cubics. Suppose they are basepoint free and
have full reduced inverse support of `C0` exactly `c=(z=0)`. Then no
positive-degree mate exists on their image. If the map is birational,
this is a degree-sixteen normalization exclusion within STCI-Q-0001.

Proof. On the line `D=(s=0)`, every point with `z!=0` must have `U2!=0`.
Otherwise its image, whose first two coordinates vanish, would either be
the forbidden extra inverse point `[0:0:0:1]` or fail to be defined.
Thus the binary cubic `A3(0,t,z)` has no projective zero except possibly
`z=0`. Over the algebraically closed field this forces

    A3(0,t,z)=alpha z^3,              alpha!=0.

Write `A3=alpha z^3+s C2(s,t,z)`. Restricting a hypothetical identity
`G(U)=z^(4b)` to `D` again forces (10), because its boundary map is
basepoint free of degree four. Differentiating in `s` now gives

    0=(b/alpha)z^(4b-4)[t^3+z C2(0,t,z)].               (16)

The bracket is nonzero: its coefficient of `t^3` is one, while its
second term is divisible by `z`. This proves the all-degree exclusion.

The condition fixing `U0,U1` is literal and restrictive; no claim is made
that an arbitrary plane normalization can be put into (15) while
preserving literal `C0`. The surviving full-support locus inside (15)
is not classified here. The proof only shows that its members all fail
the required descent.


## A reduced-trivial phase with a nonzero nilpotent defect

The following generic local calculation includes arbitrary localized denominators; testing polynomial generators alone would not prove nonmembership.

### B. Generic local ring and denominator check

For a birational member of the explicit eleven-parameter family (8), let `D=(s=0)`, and work in
the source chart `z=1` with coordinates `r=s/z,y=t/z`. The source local
ring at the generic point of `D` is the DVR

    B=k[r,y]_(r)=k(y)[r]_(r),    E=B/(r)=k(y).

The target affine coordinate ring in the chart `X2!=0` is the subring
`A=k[a0,a1,w]` of its function field, with

    a0=r^4/(alpha+r y^3),
    a1=r^3 y/(alpha+r y^3),
    w=(y^4+P(r,y,1))/(alpha+r y^3).

The image line `ell` has prime `p=(a0,a1)` and `A/p=k[w]`: it is indeed
the entire line, because the boundary morphism to it is surjective. Its
residue coordinate pulls back to

    w0=g(y)/alpha,    g(y)=y^4+P(0,y,1).

The polynomial `g` has degree exactly four because `P` has total degree
three. Thus `w0` is transcendental over `k`, and the target residue field
`K=k(w0)` embeds in `E` with degree four. The nontrivial residue extension
proves nonnormality at the generic point of `ell`, so `D` is a conductor
prime. Also `f^{-1}(ell)` has reduced support only `D`, since `U0=s^4`;
there is no second inverse prime over the generic point of the line.

Take an arbitrary element of the target local ring `A_p`. Write it as

    N(a0,a1,w)/M(a0,a1,w),    M notin p,

using polynomial representatives. The denominator's restriction
`M(0,0,W)` is a nonzero polynomial. Substitution `W=w0` is injective, so
this denominator has nonzero residue and is invertible in `B/(r^2)`.
Because `a0,a1` vanish modulo `r^2`, the image of this localized element
in `B/(r^2)` is exactly

    R(w),    R(W)=N(0,0,W)/M(0,0,W) in k(W).

This establishes the asserted form for all localized elements, including
those with denominators; no polynomial-only assumption is hidden. If its
residue is the constant `alpha^(-b)`, injectivity of `k(W)->E`,
`W->w0`, forces the rational function `R` itself to be that constant.
Consequently the element has zero coefficient of `r` modulo `r^2`.

In contrast,

    q^b=(alpha+r y^3)^(-b)
       =alpha^(-b)-b alpha^(-b-1)y^3 r mod r^2,

has nonzero linear coefficient for every positive `b`. Thus `q^b` is not
in `A_p`, even though its residue `alpha^(-b)` lies in `K*` and is the
identity class of `E*/K*`. This is an exact first-order obstruction at the
actual generic conductor prime. It does not require knowing which power
of `(r)` equals or lies in the conductor ideal.

For the explicit member (1) the affine chart `s!=0` is an isomorphism, by
the explicit inverse already checked. The generic nonnormality along
`D`, together with this isomorphism off `D`, proves that the entire
conductor support upstairs is `D`. No scheme multiplicity is inferred,
and no analogous entire-support assertion is justified here for arbitrary
`P`.

The differential lemma and this generic local calculation are therefore
independently reviewed with the literal hypotheses above. Their scope is
an obstruction and an explicit family calculation, not a computation of
the full plane-model phase image or a general exclusion of that model.


For the explicit member (1), the differential test in [full conductor algebra, §6](conductor_descent_algebra.md#6-differential-obstruction-on-a-prescribed-cartier-ray) applies at `(r,y)=(0,1)` with frame U2. There `q=1/(1+ry^3)`, the target differentials satisfy `da0=da1=0`, `dw=-dr+4dy`, and `v=partial_r+(1/4)partial_y` has `dq(v)=-1`. This geometric proof and the polynomial derivative proof detect the same obstruction at different levels and are both retained.

## Smooth quadric: isolated inverse points prohibit every mate

On `S=P1_(s:t) x P1_(u:v)`, put `q=sv-tu`, `p=sv+tu`, `c=(q=0)`, and `H=O(2,2)`. The two systems are

    U0=s^2u^2+q tv/2, U1=su p/2, U2=tv p/2,
    U3=t^2v^2+kappa q^2,
    kappa!=0, kappa^3!=-1/64;

and the companion family

    V0=s^2u^2+q tv/2+gamma q^2, V1=su p/2,
    V2=tv p/2, V3=t^2v^2, gamma!=0.

Both restrict on c to the literal C0. Both are finite normalizations of integral degree-eight hypersurfaces, but c is not the full inverse support. The following proves every parameter boundary, the rational inverses, and the isolated-point obstruction.

## 1. Basepoint-free locus and finiteness of the kappa family

Write `p=sv+tu`, `q=sv-tu`. Vanishing of both middle coordinates gives
either `p=0`, or `su=tv=0`. The latter locus consists of exactly the two
cross-corners

    ((0:1),(1:0)),       ((1:0),(0:1)).

At both, `q!=0`, and `U3=kappa q^2`. Thus these are not basepoints when
`kappa!=0`; both are basepoints when `kappa=0`.

The antidiagonal `D=(p=0)` is parametrized globally by
`(s:t)=(a:b), (u:v)=(a:-b)`. Its nonzero coordinate candidates are exactly

    U0=a^4+ab^3,           U3=b^4+4kappa a^2b^2.

At `a=0` or `b=0`, one of these is nonzero. Otherwise putting `x=b/a`
gives a simultaneous zero precisely when

    x^3=-1,               x^2=-4kappa.

These imply `kappa^3=-1/64`; conversely `x=1/(4kappa)` solves both
equations on that parameter locus. Hence the two stated exclusions are
the exact basepoint-free conditions, including all boundary charts.

The resulting projective morphism pulls back `O(1)` to the ample bundle
`O(2,2)`. A positive-dimensional fiber would contain a complete curve on
which this ample bundle has degree zero, which is impossible. Properness
and zero-dimensional fibers therefore give finiteness.

## 2. Birationality and degree of the kappa family

On `s=u=1`, set `x=t`, `y=v`, `r=xy`, `d=y-x`, `P=x+y`. Direct
substitution independently gives

    (U0,U1,U2,U3)=(1+dr/2,P/2,rP/2,r^2+kappa d^2).

For `z_i=Ui/U0`, `lambda=U0`, and `r z1!=0`, one has

    r=z2/z1,  P=2lambda z1,  d=2(lambda-1)/r.

Using `P^2-d^2=4r` produces

    (1-r^2 z1^2)lambda^2-2lambda+1+r^3=0.

The fourth coordinate then gives

    4kappa z1^2 lambda^2-z3 lambda+r^2-4kappa r=0.

Eliminating the quadratic term yields

    lambda=[(1-r^2 z1^2)(r^2-4kappa r)-4kappa z1^2(1+r^3)]
           /[(1-r^2 z1^2)z3-8kappa z1^2],

with denominator `(1-r^2z1^2)z3-8kappa z1^2`. At `x=0,y=1`, this
rational function is defined and equals `-kappa`. Although `r=0` there,
this evaluation is used solely to prove nonidentity of the denominator;
it is not asserted to lie in the inverse chart. Because `S` is integral,
the simultaneous nonvanishing inverse conditions have a nonempty dense
intersection. Recovering `x=(P-d)/2`, `y=(P+d)/2` proves birationality for
every nonzero `kappa`; no further exceptional parameter occurs.

The finite birational morphism from normal `S` is the finite normalization
of its integral image. Finiteness makes the image a surface, hence an
integral hypersurface in `P3`. The degree formula gives
`deg X=H^2=(2,2)^2=8`.

## 3. Full inverse-support obstruction in the kappa family

Restriction to `c` gives the prescribed four quartic coordinates. The
parametrization of `C0` is an isomorphism: on the two endpoint charts its
local parameters are respectively `X1/X0=t/s` and `X2/X3=s/t`.

On `D`, the two degree-four sections above have no common zero on the
admissible parameter locus. They define a degree-four map to
`L=(X1=X2=0)`. Characteristic zero ensures four distinct geometric points
in its generic fiber. Its degree-four residue extension means the finite
normalization is not an isomorphism at the generic point of `L`; therefore
`D` belongs to the actual conductor support. This is a curve on `S`
mapping to a curve on `X`, not a vertical exceptional divisor.

The two roots of `b^2+4kappa a^2=0` give two distinct off-diagonal points
on `D` over `[1:0:0:0]`. The three roots of `a^3+b^3=0` give three
distinct off-diagonal points on `D` over `[0:0:0:1]`. Each has `ab!=0`,
and the other nonzero coordinate follows from basepoint-freeness. Thus the
claimed lower bound of five is valid for every admissible `kappa`.
Additionally, the two cross-corners from the basepoint calculation also map to
`[0:0:0:1]`, giving seven forced endpoint extras. The source's lower bound
does not claim an exact total count.

To check that no other inverse curve absorbs these points, take any
nonendpoint target `[1:z:z^3:z^4]`. Then `z!=0`, `U1,U2!=0`, so all four
source coordinates are nonzero, and the affine calculation applies. For
an off-diagonal inverse point one has `r=z^2`, `d!=0`, `lambda!=1`, and

    kappa d^2=(lambda-1)r^2,
    d^2=4r(lambda^2-1),
    d=2(lambda-1)/r.

Cancelling only the already nonzero factors gives

    r=4kappa(lambda+1),
    lambda-1=64kappa^3(lambda+1)^4,
    z^2=r.

The polynomial in `lambda` is nonzero for every `kappa!=0`. It admits
only finitely many values of `lambda`, and then only finitely many `z`.
Boundary points with `su=0` have `U1=0` and cannot lie over a nonendpoint.
Every curve in the inverse support of `C0` must map onto `C0`, because
the morphism is finite. Hence `c` is the sole curve component, and the
extra points outside it are isolated in the full inverse support. This
argument is uniform on the entire stated parameter locus.

## 4. Companion family: exact full inverse support

For the companion family, `V3=0` forces `t=0` or `v=0`. At `t=0`, the equation `V1=0`
forces `uv=0`; the respective nonzero coordinates are `s^2u^2` or
`gamma s^2v^2`. At `v=0`, the two cases similarly give `s^2u^2` or
`gamma t^2u^2`. Thus every `gamma!=0` is basepoint-free, with no further
condition. Ampleness again gives finiteness.

On the affine chart the coordinates are

    (1+dr/2+gamma d^2,P/2,rP/2,r^2).

Recover successively

    r=z2/z1, lambda=r^2/z3, P=2lambda z1,
    D=P^2-4r, d=2(lambda-1-gamma D)/r.

Since `D=d^2` on the image, this proves the rational inverse
without any square-root choice. Its nonvanishing conditions are dense;
for example `x=y=1` satisfies them for every `gamma`. Thus every
`gamma!=0` gives the claimed degree-eight integral carrier and finite
normalization.

For every nonendpoint point `[1:z:z^3:z^4]`, these identities force
`r=z^2`, `lambda=1`, `P=2z`, `D=d=0`. Its unique inverse point is on
`c`; the boundary cannot occur because `V1,V2` are nonzero.

Over `[1:0:0:0]`, the preceding boundary calculation gives exactly the
diagonal endpoint and the two cross-corners. Over `[0:0:0:1]`, `tv!=0`
and `V2=0` force `p=0`; the antidiagonal parametrization gives exactly
the diagonal endpoint `a=0` and the roots

    1+4gamma x^2+x^3=0,           x=b/a.

All roots are finite and nonzero. The discriminant is
`-256gamma^3-27`. If it vanishes, the repeated root is `x=-8gamma/3`,
and the second derivative there is `-8gamma!=0`, so it is exactly
double. There are therefore exactly three distinct extra points from
this cubic, or exactly two when `gamma^3=-27/256`. Together with the two
cross-corners, this proves the asserted entire reduced inverse support:
five isolated extras ordinarily, and four on the exceptional parameter
locus. In particular `gamma=1` has exactly five.

On `D`, the sections `a^4+ab^3+4gamma a^2b^2` and `b^4` have no common
zero. The degree-four map to `L` and the conductor-prime conclusion
follow exactly as in the preceding conductor calculation.

## 5. Every mate degree and the precise frontier boundary

If a homogeneous form `G` of positive degree `b` cut out exactly `C0`
on either carrier, its restriction and pullback would be nonzero sections.
The zero support of the pullback on smooth `S` would be the complete
inverse support of `C0`, including its isolated points. A nonzero section
of a line bundle on a smooth integral surface defines an effective
Cartier divisor, whose support has pure codimension one. This is
impossible. Equivalently, since `c` is the only inverse curve, the
pullback divisor must be `m c`; in `Pic(S)=Z^2`, comparison with
`bH=(2b,2b)` gives `m=2b`, and this divisor misses every off-`c` point.
Thus the exclusions hold in every positive mate degree.

The first-jet claim also checks directly: in both families
`L0|c=x^2/2`, while `L1|c=L2|c=L3|c=0`. The balanced formulas give
`A=x^5`, `B=0`, with homogeneous common-zero divisor `5(t=0)`.
The inverse-support conclusions above use the actual maps and do not
follow merely from these jets.

These explicit subfamilies provide actual carrier constructions and
completed, reviewed all-degree exclusions within their stated parameter
sets. They neither exhaust the sixteen-parameter smooth-quadric family
nor decide either other model in STCI-R-0002. No surviving full-support
conductor phase image is computed. STCI-Q-0001 and the unrestricted
characteristic-zero question remain open.


## Characteristic boundary

The map and support identities are polynomial geometric calculations. The plane all-power contradiction uses the nonvanishing of the positive degree b in the field. In characteristic p it excludes only degrees prime to p (indeed all b not divisible by p); the differential of a p-th power is zero. Thus this proof supplies no all-degree positive-characteristic exclusion. The two quadric inverse formulas and support calculations require 2 invertible; their displayed parameter separability and root counts must additionally be checked in any selected positive characteristic. The complete characteristic-zero families remain the reviewed statements. The [positive-characteristic construction](../arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier) uses a quartic carrier for this fixed curve. The [arithmetic plane-source treatment](../arithmetic/arithmetic_root_collision.md#arithmetic-degree-bounds-missing-jets-and-actual-non-binomial-equations) also proves actual Frobenius descent on the explicit degree-sixteen plane carrier, retaining its full conductor multiplicity. Thus the all-degree plane exclusion is specific to characteristic zero.

## The opposite-ruling pairing and its complete coefficient freedom

This separate source calculation retains the full coefficient family for a prescribed pairing, and explains why its sparse failed subfamily is not an exclusion of that whole family. It is not an exhaustion of arbitrary smooth-quadric projections.

## 1. Opposite-ruling gluing with a constant phase

Use affine coordinates `(x,y)` on the quadric with `c:y=x`, and let
`W0,W1,W2,W3` be the four coordinate vectors of the fixed curve

    U(t,t)=W0+t W1+t^3 W2+t^4 W3.

The distinguished section is `Q=(y-x)^2`, homogenized to bidegree
`(2,2)`. Suppose the two opposite rulings through `(0,0)` are paired
by `(x,0) <-> (0,a x)`, where `a!=0`. If the projective images agree
and the ratio of `Q` after that identification is constant, the
projective proportionality factor is constant in this affine
trivialization: the two `Q` values are `x^2` and `a^2 x^2`.
At the common point both coordinate vectors are `W0`, so that
constant factor equals one. Hence

    U(x,0)=U(0,a x).

The degree-one coefficient on the diagonal is `W1!=0`; consequently
`a=-1` is impossible in this form. For `a!=0,-1`, comparison of the
nine bidegree `(2,2)` coefficients gives the complete normal form

    U(x,y)=W0+(a x+y)/(a+1) W1
           +(a^2 x^2+y^2-(a^2+1)xy) D
           +xy[x E+y(W2-E)]+x^2y^2 W3,                 (1)

with arbitrary vectors `D,E in k^4`. Conversely, (1) has the fixed
diagonal restriction and the stated ruling identification. Its
branchwise phase is `a^{-2}` if the ratio is taken from the first
ruling to the second. Thus branchwise gluing alone places no bound
on the root-of-unity order.

This normal form assumes the specified affine scaling pairing.
It does not classify arbitrary conductor components or every
Möbius pairing, and it does not imply basepoint-freeness,
birationality, full support, or complete conductor descent.

## 2. The sparse family fails full support for every parameter

The especially simple family proposed in the phase exploration has

    D=W2, E=u W2,
    U0=1,
    U1=(a x+y)/(a+1),
    U2=a^2x^2+y^2-(a^2+1)xy+u x^2y+(1-u)xy^2,
    U3=x^2y^2.                                        (2)

Homogenize to bidegree `(2,2)` in `[x0:x1]` and `[y0:y1]`.
The four sections have no common zero: on the finite chart `U0=1`;
on `x0=0` the relevant pair is

    U2=a^2 y0^2+u y0 y1,   U3=y1^2,

and on `y0=0` it is

    U2=x0^2+(1-u)x0 x1,    U3=x1^2.

At the common point at infinity, `U3!=0`. This proves a finite
morphism because `H` is ample.

Nevertheless, the entire inverse image of C0 is never just `c`.
If `u!=0`, the boundary point

    x=Infinity,  y=-a^2/u

is finite in the second coordinate, lies outside `c`, and maps to
`[0:0:0:1]`, the infinite endpoint of C0. If `u!=1`, the analogous
point

    y=Infinity,  x=-1/(1-u)

also lies outside `c` and maps to the same endpoint. Avoiding the
first point would require `u=0`; avoiding the second would require
`u=1`. They cannot both be avoided. This argument is valid without
any birationality assumption and rules out full support for all
parameters of (2).

In characteristic zero there is also a useful finite-chart check. For an inverse image of
`[1:t:t^3:t^4]` with `t!=0`, put `l=a x+y=(a+1)t` and `p=xy`.
One has `p=+t^2` or `p=-t^2`. For the negative choice write
`x=r t`, `y=v t`, so

    a r+v=a+1,   rv=-1,
    a r^2-(a+1)r-1=0.

The quadratic coefficient of `U2` is then exactly
`2(a+1)^2`, independently of the selected root. Its cubic
coefficient is `C=-[u r+(1-u)v]`. Thus an extra point occurs at

    t=-2(a+1)^2/(C-1)

whenever `C!=1`. If `a^2+6a+1!=0`, the two roots are distinct.
Making `C=1` at both roots would force `(a+1)u-a=0`, which instead
gives `C=-1`. Hence at least one finite extra point exists in that
stratum. The boundary argument above additionally covers the
double-root stratum and all exceptional finite-chart cases.

## 3. Why this does not eliminate the complete normal form

For (1), the boundary restrictions are the vector-valued conics

    U(Infinity,y) ~ a^2 D+y E+y^2 W3,
    U(x,Infinity) ~ D+x(W2-E)+x^2 W3.                  (3)

Project to `k^4/k W3`. If the projected pairs `(D,E)` and
`(D,W2-E)` are both linearly independent, neither boundary ruling
has an extra finite point mapping to the infinite endpoint of C0.
For example, the coefficient choice `D=W0`, `E=W1` satisfies these
independence conditions. This is only a boundary observation; no
full-support or basepoint-free assertion is made for that choice.

Thus the obstruction in Section 2 comes from its restricted
coefficient choice. Treating it as a phase-order theorem or as an
exclusion of all opposite-ruling conductor pairs would discard
six permitted coefficients. The surviving structural problem is
to impose the full radical inverse-image condition and complete
conductor descent on (1), or on more general paired curves.
