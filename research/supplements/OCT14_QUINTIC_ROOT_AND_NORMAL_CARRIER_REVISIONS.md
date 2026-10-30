# Historical mathematical investigations

Complete source texts below, retaining mathematical arguments, hypotheses, counterexamples, corrections and unresolved cases. No new independent audit or theorem promotion.

---

## Source: 2026-10-14-generalization-projection-conductor-jacobian-bridge.md

# Conductor contact and the full first normal symbol

Date: 2026-10-14. Owner: `jacobian_contact_identity`, for
`projection_global_continue/global_phase_duality`. Status: **NEW WRITTEN
PROOF; independent review requested**. Previously accepted normalization,
normal-bundle, and Cartier-lift results are premises and were not rerun.

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


---

## Source: 2026-10-14-generalization-quadratic-root-universal-incidence.md

# Universal quadratic root incidence and a smooth torsion-compatible zero

Date: 2026-10-14. Author: `universal_root_obstruction`.
Status: **NEW EXACT REDUCTION AND EXPLICIT GEOMETRIC BOUNDARY; independent
review in progress**. The accepted spectral root-curve theorem and its
independent audit, together with the accepted actual chart operator,
are premises. No accepted chart or conormal audit is repeated.

## 1. One matrix covers every moving quadratic relation of movement two

Work in characteristic zero with the actual balanced conormal of `C0`.
Write

    f=a(z)u²+b(z)uv+c(z)v²,
    a=a0+a1 z+a2 z², b=b0+b1 z+b2 z², c=c0+c1 z+c2 z².

The coefficients are homogeneous degree-two sections on the base. Let
`U` be the open subset of `P8` where `a,b,c` have no common base zero.
The root divisor `Z=(f=0)` is then finite flat of degree two over the
base, including when it is singular or nonreduced.

The accepted first ambient class is the image of

    d_f=pr[Du f_u+Dv f_v+alpha f_z]

in `coker A_f`, where `pr` retains the Laurent powers `z^-4,...,z^-1`,
and

    Du=−(5/2)z^-4 u²−3z^-3 uv−(3/8)z^-2 v²,
    Dv=3z^-5 u²−z^-4 uv−(9/4)z^-3 v²,
    alpha=z^-3 u+(1/2)z^-2 v.

Use the source basis `z^-6,...,z^-1` first times `u`, then times `v`.
Use the target basis `z^-4,...,z^-1` first times `u³`, then times `u²v`,
then times `uv²`, then times `v³`. For `p=p0+p1 z+p2 z²`, set

```
         [ p2 p1 p0  0  0  0 ]
T(p)  =  [  0 p2 p1 p0  0  0 ].
         [  0  0 p2 p1 p0  0 ]
         [  0  0  0 p2 p1 p0 ]
```

Then the exact `16 by 12` multiplication matrix is

```
          [ T(a)   0    ]
A_f   =   [ T(b)  T(a)  ].
          [ T(c)  T(b)  ]
          [  0    T(c)  ]
```

In the same target basis, the sixteen entries of `d_f` are

```
−5a0+3b1
−4a1+3b2
−3a2
0

6c1−(7/2)b0
6c2−(5/2)b1−6a0
−(3/2)b2−(11/2)a1
−5a2

−2c0
−c1−(21/4)b0
−(19/4)b1−(3/4)a0
−(17/4)b2−(3/4)a1

0
−(9/2)c0
−4c1−(3/8)b0
−(7/2)c2−(3/8)b1.
```

These formulas are obtained by applying the accepted derivation once and
collecting its Cech powers. They retain the base derivative `alpha f_z`.
The discarded multiple of `f` from the line-bundle transition lies in
the image of `A_f` and therefore does not affect this quotient class.

The matrix `A_f` is injective throughout `U`. Indeed
`pi_*O_Z(3)` is a globally generated rank-two bundle of degree four:
its defining exact sequence is

    0 -> O(-2)² -> O⁴ -> pi_*O_Z(3) -> 0.

Its two splitting degrees are nonnegative and sum to four. After
base twist by `O(-5)` neither summand has a section. Consequently
`H0(Z,O_Z(-5,3))=0`, and the divisor sequence gives injectivity of
`H1(O(-7,1)) -> H1(O(-5,3))` even without smoothness.

Thus the single universal compatibility scheme is

    K={ [f] in U : rank[A_f | d_f]=12 },

with scheme structure defined by the `13 by 13` minors of that one
`16 by 13` matrix. Equivalently it is the incidence

    A_f h=d_f,       h in k^12.

Over `U` the vector `h` is unique whenever it exists, so the latter
incidence is the graph of the zero scheme of the rank-four quotient
obstruction. This is independent of both projective hypersurface
degrees and any later second-relation degree.

## 2. The smooth-root locus of K is nonempty

Take

    f0=(z²+4)u²+(z²−8)v².

Its first ambient obstruction vanishes. An exact preimage is

    h0=(−3z^-4−8z^-6)u+(−(1/8)z^-1−(9/2)z^-3)v.

Writing `D=Du partial_u+Dv partial_v+alpha partial_z`, a direct identity is

```
D(f0)−f0*h0
 =32z^-6 u³
  +((1/8)z−48z^-5)u²v
  +(−3/4−64z^-6)uv²
  +(1/8)z v³.
```

Every remaining Laurent power is outside `z^-4,...,z^-1`, proving
`A_f0 h0=d_f0` with the actual accepted ambient operator.

The binary coefficient polynomials `z²+4` and `z²−8` have two simple
roots each, have no common root, and are both nonzero at infinity in
the homogeneous base presentation. Thus the degree-two cover of the
base is branched at four distinct points; its `(2,2)` root divisor is
smooth and connected of genus one. This is a characteristic-zero
statement, so the displayed nonzero constants cause no exceptional
characteristic issue.

This example disproves the possible broad assertion that the actual
first ambient class is nonzero on every smooth `(2,2)` root divisor.
It supplies compatibility through the first exceptional order only.

## 3. Smooth compatibility has positive local dimension

The equations `A_f h-d_f=0` have sixteen components in nine affine
coefficient variables and twelve correction variables. At `(f0,h0)`
their Jacobian has rank sixteen. In the variable order

    a0,a1,a2,b0,b1,b2,c0,c1,c2,h0,...,h11,

where the twelve `h` coordinates follow the source basis in Section 1,
the minor on zero-based columns

    0,1,2,3,4,5,6,7,9,10,11,12,13,14,15,16

has determinant exactly `−405`. The companion standard-library Python
script records the full rational Jacobian and verifies this determinant
by exact rational elimination.

The affine incidence is therefore smooth of dimension `21−16=5` at
this point. Since the correction vector is unique and scaling the
nonzero equation `f` gives a free scalar direction, the projective
compatibility scheme `K` is smooth of dimension four at `[f0]`. Being
a smooth root divisor is an open condition. Hence `K` contains a
nonempty four-dimensional local family of smooth root divisors. This
is stronger than an isolated compatibility sample; it does not assert
that ruling-difference torsion holds throughout that local family.

## 4. The explicit zero also passes the spectral torsion condition

On `Z0=(f0=0)`, put

    A=O_Z0(1,0),    B=O_Z0(0,1),    eta=B tensor A^-1.

Then `eta` has exact order two. One elementary divisor proof uses
`c(z)=z²−8`, considered as a section of `A²`. At a zero of `u` on
`Z0`, both `a(z)` and `v` are units, and the equation

    c(z)v²=−a(z)u²

shows that the zero divisor of `c(z)` is twice the zero divisor of
`u`. There are no other zeros. Consequently `A²≅B²`.
If `A≅B`, their two complete degree-two systems would differ by an
automorphism of `P1`, forcing the image in `P1 x P1` to be a graph.
Its actual smooth `(2,2)` image excludes this. Thus `eta` is nontrivial
and has order two.

The accepted spectral criterion consequently permits a coprime second
quotient relation in every even degree `s>2`. In particular it permits
`s=8` and `s=12`, the two second degrees appearing in the accepted
scalar numerical boundary. The second relation remains a quotient
relation with its nonsplit extension; no global second polynomial
line has been constructed.

Thus the actual first ambient compatibility and the exact spectral
torsion descent condition coexist. Their conjunction alone does not
exclude this geometry. Higher actual ambient obstruction classes,
and eventual realization by projective equations with the required
support, remain unresolved.

## 5. Reproducible evidence and scope

The exact matrix, Cech bases, explicit preimage, and Jacobian certificate
are recorded in

- [the standard-library verifier](../computations/generalization_quadratic_root_curve_universal_incidence.py),
- [its exact JSON output](../computations/generalization_quadratic_root_curve_universal_incidence.json).

Run with `python3 research/computations/generalization_quadratic_root_curve_universal_incidence.py`.
No SymPy, parameter sampling, Groebner basis, or generic-rank inference is
used. The matrix identity and one nonzero Jacobian determinant are exact
certificates. The spectral theorem/audit and accepted chart operator were
used as premises; they were not re-audited.

The newly proposed actual-CI-to-root-curve bridge is separate. Once that
bridge passes independent review, `K` is a necessary incidence for its
stated lane. Nothing here promotes that bridge's hypotheses to a theorem
about every complete intersection. The universal STCI problem and
unrestricted `C0` remain open. No commit or memory update was made.


---

## Source: 2026-10-14-generalization-quintic-h3-results-acceptance.md

# Acceptance: the entire nonendpoint homogeneous gcd-three lane is excluded

Date: 2026-10-14. Root integration. Status: **PROVED in the stated
characteristic-zero nonendpoint genus-one quintic A4 normalization
model, with every positive mate degree**. The universal STCI question,
unrestricted C0 question and other quintic normalization lanes remain open.

This accepts the final obligation of the
[owner continuation](OCT13_THICK_EQUALITY_SOCLE_AND_FILTRATIONS.md#source-2026-10-13-generalization-quintic-continuationmd)
after the earlier [independent geometric audit](#source-2026-10-14-generalization-quintic-new-independent-auditmd).
The completed literal membership identity is an input; it is not
re-expanded here at the user's direction. The new root review matches
that final identity to the already reviewed six-generator geometry and
complete homogeneous support cover.

## 1. Exact coverage and inherited premises

Keep the actual center-avoidance, finite birational projection and
delta nonzero hypotheses of the accepted A4 model. The complete
homogeneous gcd-three classification is an accepted input. It covers
the zero-conormal-cubic charts and all nonzero proportional pairs,
including the entire lambda=1 boundary. Those zero and lambda-one
charts already have completed independent all-mate support exclusions.

In the remaining main proportional family, the accepted full inverse
support/conductor theorem forces the roots of the complete nonzero
binary octic to lie on the homogeneous cubic H3. Its factorization is
`F=constant H3 S5`. The allowed main parameters make

```
V=delta lambda(lambda-1)(lambda^2-4lambda+1)
  ((lambda+1)delta+lambda-1)
```

nonzero. The earlier review retains all Jbar-zero exclusions before
using support concentration. No Jbar-zero parameter is removed by
an unmentioned saturation.

The homogeneous leading-drop argument excludes infinity support in
this main family. Thus `c5=LC(S5)` is nonzero on any hypothetical
survivor, and all remaining roots of S5 are finite. The independently
audited support lemma gives a complete alternative:

1. At least three distinct roots force H3 squarefree and H3 dividing S5.
2. At most two roots have multiplicities 5, 4+1, or 3+2.

The first alternative and multiplicity at least four already have
literal original-generator witnesses and accepted independent geometry.
Repeated roots and all homogeneous leading drops remain covered.

## 2. The final original-generator identity

For multiplicities 3+2, choose x to be the triple root. The actual
six-generator row M6 comprises

```
S5(x), S5'(x), S5''(x),
c4^2-4c3 c5-6x c4 c5-15x^2 c5^2,
H3(x), (2c5)^3 H3(-(c4+3x c5)/(2c5)).
```

These are polynomial equations after the stated denominator clearing.
The second root is uniquely the double root of the residual quadratic;
2c5 is a unit. Thus every actual 3+2 support configuration satisfies
all six equations. Coalescence into a fifth root is also retained.

The completed source
[support32 witness](../computations/generalization_quintic_h3_support32_witness.m2)
loads those **original six generators**, finds exponent two, constructs
the column W, and asserts the exact identity

```
M6 W=(V c5)^2.
```

The [captured execution](../validation/2026-10-13-generalization-quintic-h3/support32-witness-attempt-01/execution-record.json)
records source SHA256
`2f8741c5cd8b7e1c97cc60d12ab0bad6409b6a7bc3121dcc09722a12b6b6c55a`,
exit zero and empty stderr. Its output explicitly reports exponent two
and the literal original-six-generator product pass. The source retains
the final product assertion before writing the witness.

At a simultaneous zero of M6 with Vc5 nonzero, this identity says
`0=(Vc5)^2`, impossible. This closes the last support pattern without
interpreting a leading resultant factor as an actual inverse point,
replacing full conductor multiplicity by a first symbol, or relying
only on a printed saturated unit ideal.

## 3. Archive and continuation bindings

The [exact witness archive](../validation/2026-10-13-generalization-quintic-h3/support32-witness.txt.gz)
contains 107657203 uncompressed bytes, SHA256
`65feb2e88ea19fd28d67512628a28915d05d1c7a44bd657fe7e99ada2910905b`.
Its gzip size is 50074835 bytes. The
[archive manifest](../validation/2026-10-13-generalization-quintic-h3/support32-archive-manifest.json)
checks archival identity only, not a new mathematical product.
The completed subset extraction, padded back to the original six
generators and verified there, has identical uncompressed witness
content. Both attempt records are preserved.

To inspect the large matrix, decompress to a temporary directory;
do not replace the repository archive by a greater-than-100MB raw file.
The original owner and independent audit's “3+2 pending” labels are
historical and are superseded by this completed certificate binding.

## 4. Accepted conclusion and exact open boundary

Every admissible nonendpoint genus-one quintic A4 projection whose
corrected conormal cubics have homogeneous gcd degree three is
excluded in every mate degree, including zero-cubic and proportional
families. This is the complete h=3 lane, not every genus-one quintic.

The remaining nonendpoint work retains homogeneous gcd degree two,
its repeated/two-root supports, and degree-one singular target-fiber
charts `qZ=0`, intrinsic A4/infinity and allowed Jbar-zero contributions.
Actual full conductor power descent on any surviving support locus
is still required. Other quintic genera, normal quintics, higher
carriers and entirely thick presentations remain separately open.


---

## Source: 2026-10-14-generalization-quintic-new-independent-audit.md

# Independent audit of new nonendpoint quintic support reductions

Date: 2026-10-14. Independent auditor: `quintic_new_audit`, with arithmetic
subaudit `h3_literal_witness`.

Status: **NEW GEOMETRIC PROOF AUDIT; ZERO-CUBIC, LAMBDA-ONE AND REGULAR
SOLE-ROOT EXCLUSIONS ACCEPTED. MAIN h=3 CERTIFICATES ARE RECORDED BELOW
WITH THEIR EXACT CURRENT LIMITS.** Older accepted proofs are premises. No accepted
model, conductor, conormal, endpoint, residual-partition, or regular-L1
verifier was rerun. Canonical files were not edited.

This audit reviews the owner notes
[quintic continuation](OCT13_THICK_EQUALITY_SOCLE_AND_FILTRATIONS.md#source-2026-10-13-generalization-quintic-continuationmd)
and [regular L2](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-13-generalization-quintic-l2). The underlying
problem remains restricted to the fixed characteristic-zero rational
quartic C0, the sectional-genus-one degree-five A4 normalization model,
and its actual nonendpoint projections. It does not decide the universal
projective-curve problem, other quintic normalization genera, higher
carriers, or entirely thick presentations.

## 1. Premises and the geometric implication actually being audited

The accepted normalization model and actual center-avoidance conditions
give a finite birational projection `nu:S->X`, with `c` mapped
isomorphically to C0. A mate forces full inverse support
`nu^{-1}(C0)_red=c`. The
[accepted conductor module audit](NONENDPOINT_CONORMAL_AND_CONDUCTOR_MODULES.md)
identifies the upstairs conductor with an actual Cartier divisor in
`|2H|`, whose restriction to c is a nonzero degree-eight binary form F.
The accepted local-ring argument implies

    supp(F) subset supp(H P^epsilon),
    epsilon=1 if Jbar=0, and zero otherwise,

where H is the complete homogeneous gcd of the corrected conormal cubics,
and P=0 is the intrinsic A4 point. This is only a necessary support
condition. In particular, the first-normal multiplicity of H does not
bound the conductor multiplicity of F.

All uses below retain the binary degrees. An affine leading drop is an
actual root at infinity. No argument discards a center minor or interprets
a resultant leading factor as an extra normalization point. When a
certificate excludes a larger coefficient family than the admissible
centers, the exclusion automatically applies to its admissible subset;
that does not replace center avoidance with a new assumption.

## 2. Zero-P and zero-J: complete support exclusions

On the zero-P chart, put `j=Jbar`. The captured exact factorization is

    F=(2/9) S3 Q5,
    S3=p^3-6p^2+6p+3j,
    Q5=p^5+(j/3-13/2)p^4+(27/2)p^3
        +(-12-5j/2)p^2+(9/2-3j/2+j^2)p+9j-3j^2.

Both factors are monic, of their fixed binary degrees. Hence neither has
an infinity root, for any j. For j nonzero the support condition says
every Q5 root lies on S3. At j=0 the additional allowed A4 point is already
a root of S3, since S3(0)=0. The same condition therefore applies for
every j, without discarding the Jbar-zero value.

Support inclusion is equivalent to `Q5 | S3^5`: a Q5 root has multiplicity
at most five, whereas its multiplicity in S3^5 is at least five. The
captured division has remainder degree below five and its five original
coefficient polynomials have a literal Bezout combination equal to one.
Thus they cannot all vanish at any algebraic j. This proves that the
entire zero-P chart fails full inverse support.

The zero-J chart is obtained by the invertible binary transformation
`(P,Q,j)->(P,P-Q,-j)`. The captured octic identity and conormal identity
are polynomial homogeneous identities, including their fixed-degree
powers of P-Q. The transformation preserves the point P=0. It also
retains points that become infinity; it is not merely an affine change
on an open subset. Consequently the zero-J chart fails full inverse
support as well.

The independent standard-library arithmetic audit reads the captured
JSON and checks the original factorization, original division product,
generator binding, all five Bezout products, and both homogeneous
coordinate identities. It uses restricted AST parsing and exact
`fractions.Fraction` arithmetic; it neither imports nor executes the
owner checker. Evidence is
[the literal arithmetic report](../validation/2026-10-14-quintic-independent-audit/h3-literal-arithmetic-report.json),
[source](../validation/2026-10-14-quintic-independent-audit/h3-literal-arithmetic.py)
and [raw output](../validation/2026-10-14-quintic-independent-audit/h3-literal-arithmetic.stdout.txt).

**Audit conclusion: PROVED within the inherited model.** Both charts have
no mate in any degree, because they fail the necessary full support
condition. This conclusion uses every parameter j and every projective
point; it is stronger than the earlier generic-gcd observation.

## 3. Lambda=1: the added A4 root and all leading drops are retained

The actual captured main coefficient lists specialize to

    H3=(d+1)p^3-6p^2+(6-6d)p+4d,
    S5=2d*p*Q4,
    Q4=(90d^2-76d-58)p^4+(-405d^2+458d+203)p^3
        +(675d^2-858d-261)p^2+(-450d^2+800d+174)p-400d.

Here d is delta and d is nonzero. Jbar=0, so the allowed support is H3
together with p=0. Since Q4(0)=-400d is nonzero, this added A4 point
cannot cover any root of Q4. Support requires every Q4 root to lie on H3.

On `T=45d^2-38d-29 != 0`, Q4 has degree four. Its finite roots must satisfy
`Q4 | H3^4`, independently of any leading drop of H3 itself. The captured
four remainders have denominators respectively `32,256,512,512` times
T^9. Their original numerator generators have a literal Bezout product
equal to one. No d in this chart satisfies the support condition.

On T=0, the fixed-degree Q4 has an infinity root. H3 has an infinity root
only when d+1=0. The exact polynomial identity

    T-(45d-83)(d+1)=54

shows that these conditions cannot occur together. The additional A4
point p=0 is finite. Thus the entire Q4-leading-drop locus also fails
support. At d=-1, where H3 loses affine degree, T=54 is nonzero, so the
original Bezout chart already covers it.

The independent arithmetic subaudit checks the original numerator
Bezout product, all denominator factors, and the exact binding of the
captured fractions to `H3^4 mod Q4`. A separate exact sparse-polynomial
calculation binds the compact H3 and Q4 to the actual main coefficient
lists at lambda=1; its
[report](../validation/2026-10-14-quintic-independent-audit/lambda-binding-result.json)
also records the nonzero scalar 2d and the infinity separation identity.
The arithmetic report in section 2 contains the original-generator
checks. Failed parser versions are preserved in this independent lineage.

**Audit conclusion: PROVED within the inherited model.** The whole
lambda=1 chart fails full inverse support and has no mate in any degree.

## 4. A degree-independent root-support lemma

Let H and S be nonzero homogeneous binary forms of degrees r and n over
an algebraically closed field, and suppose `supp(S) subset supp(H)`.
Then S has at most r distinct projective roots. If it has exactly r,
H is squarefree and H divides S. Otherwise S has at most r-1 roots;
its multiplicities form a partition of n into at most r-1 positive parts.

Proof: a degree-r binary form has at most r distinct roots. Equality in
the support bound forces H to have exactly those r roots, each of
multiplicity one. Each divides S, so their product H divides S up to
a nonzero scalar. The remaining assertion is just the factorization of
S with its positive root multiplicities. This proof retains infinity
and requires no characteristic assumption. Derivative descriptions of
the resulting incidence need their own characteristic hypotheses.

For r=3,n=5 the complete alternatives are: H divides S, a root of S has
multiplicity at least four, or the exact root pattern is 3+2. This replaces
one very large power-remainder calculation with smaller divisibility and
root-multiplicity incidences. It is a proved structural reduction; it
does not by itself assert that any parameter incidence is empty.

## 5. Main h=3: homogeneous infinity and the first two support alternatives

On the main proportional chart the captured actual factorization is

    F=-d^4 H3 S5/(1296 lambda^6).

The minus sign follows from the captured normalization of H3; only the
nonzero scalar matters for support. The complete Jbar-zero factorization
reduces all lambda!=1, Jbar=0 values to the already excluded G=Jbar=0
all-power locus. That accepted theorem excludes mates there; this audit
does not replace it by an unsupported full-SUP exclusion.

Thus the main support analysis retains

    V=d lambda(lambda-1)(lambda^2-4lambda+1)
      ((lambda+1)d+lambda-1) != 0.

Write c5=LC(S5) and h3=LC(H3)=d+2lambda-1. If c5=0, S5 has an infinity
root, so support would require h3=0. Substituting d=1-2lambda gives the
exact coefficient identity

    c5=-216 lambda^4(2lambda-1)^3=216 lambda^4 d^3,

contradicting d lambda nonzero. This is a complete homogeneous exclusion
of the S5 leading-drop case. If h3=0 while c5!=0, H3 has at most two
finite roots, so the at-least-three-root alternative cannot occur.

On h3 c5!=0 the saved three pseudoremainder coefficients R_i of S5 by
H3 are divided only by the common factor lambda^2, a unit. The literal
original-generator identity is

    sum_i W_i R_i=(V h3 c5)^2.

This excludes H3|S5 on the precise declared chart. The exact witness is
[saved](../validation/2026-10-13-generalization-quintic-h3/h-divides-s-witness.txt),
and the owner source asserts the literal matrix product before saving it.
The original failed extraction omitted c5, found no witness at the stated
bounded exponent, and failed its assertion. Its failure is retained;
the repaired chart is the one used here.

For multiplicity at least four the original four generators are
`S5(x),S5'(x),S5''(x),S5'''(x)`. In characteristic zero their vanishing is
equivalent to a root of multiplicity at least four. The completed owner
source records a literal combination of these original generators equal
to `(V c5)^2`, with x retained as a variable. Its
[22 MB exact witness](../validation/2026-10-13-generalization-quintic-h3/multiplicity4-witness.txt)
is accompanied by exponent two, the original input row, the source
`generalization_quintic_h3_multiplicity_witness.m2`, and passing raw output.
This is an exact membership certificate on all parameters, rather than
a reliance on a printed saturated `ideal(1)` or a root sample.

The independent arithmetic subaudit now also multiplies the original
three R_i entries by their saved 3-by-1 witness, using a strict expanded
monomial parser and denominator-cleared integer convolution. Its residual
is exactly zero against the original `(V h3 c5)^2` target. The R_i contain
69,62,58 terms and the corresponding witnesses contain 436,465,485 terms;
these are descriptive sizes, not additional theorem counts. It binds the
actual captured c5 and the exponent-two file. Evidence is the
[main literal report](../validation/2026-10-14-quintic-independent-audit/main-h3-literal-arithmetic-report.json),
[independent source](../validation/2026-10-14-quintic-independent-audit/main-h3-literal-arithmetic.py)
and its raw output. The first unavailable-runtime-path attempt is retained.

**Audit conclusion for these alternatives: their geometric implications
are sound, with actual original-generator membership witnesses.** The
three-root and multiplicity-at-least-four alternatives are excluded under
the stated units. No expensive repetition of the already asserted 22 MB
witness product is counted as a new independent calculation here.

## 6. The remaining 3+2 support pattern: exact required certificate

If x is the triple root of an affine quintic with coefficients c_i, then
division by `(p-x)^3` gives the residual quadratic

    c5 p^2+(c4+3x c5)p+(c3+3x c4+6x^2 c5).

Its discriminant is exactly

    c4^2-4c3c5-6x c4c5-15x^2 c5^2.

With c5 nonzero, discriminant zero makes its double root
`y=-(c4+3x c5)/(2c5)`. Full support requires H3(x)=H3(y)=0. Multiplying
the latter equation by `(2c5)^3` is equivalent to it, even if H3 loses
affine degree, because 2c5 is a unit. Thus the owner's six original
generators retain exactly the necessary equations, all finite x,y,
coalescence into a fifth root, and every H3-leading drop.

The new saturation output for these six generators is the unit ideal.
At the time this audit section was written, an original-generator power
witness for this six-generator ideal had not yet been bound to a finished
execution. **The final 3+2 emptiness claim and the complete main h=3
exclusion remain pending that literal witness.** Neither the unfinished
unrestricted multiplicity32 calculation nor the unit-ideal printout alone
is promoted by this audit. Sections 4--5 remain proved without it.

## 7. Regular L2: geometric elimination cover and retained exceptional loci

The owner L2 theorem asserts that, on the accepted finite common-root
incidence and regular chart `qZ(q)!=0`, with `L1!=0,L2=0`, the actual
Taylor coefficients f2,f3,f4,f5 cannot all vanish. Here

    Pc=q^2-6q+6, U=q(k-d)-d^2,
    D=2d(q-1)+q(q-2), E=d^2+d(3q-4)+q(q-2),
    Z(q)=q Pc U.

The exact coefficient identity
`partial_a f2=-(dq/2)L1 partial_k L2 (mod L2)` justifies solving for a
only where the L2 root is simple and L1 is nonzero. No original fiber
leading coefficient or unstated center parameter is divided out.

The finite cover is complete. q=1 is impossible because L2=d^5. q=2 is
handled by its two-embedding quadratic-field cover. Away from q=1,2,
the D=0 boundary makes L2 genuinely linear in k and is handled separately.
On D!=0, a discriminant-zero root has the displayed L1=0 value and lies
outside the new L1!=0 theorem. The remaining points have the algebraic
coordinate m in owner equations (3)--(4). Both signs are covered because
the inverse formula determines m from the actual k; no chosen square-root
branch is lost. All rational-cover denominators are units under d,q,Pc,
q-1,q-2,D nonzero and m^2!=3.

The audit initially flagged the extra polynomial H removed from the f3
numerator. The owner now records the exact identity

    L1=-3m(q-2)Pc^2 H/
      [q^2(q-1)(m^2-3)^2(qm+3q-6)].

Consequently m and H are units on the retained L1!=0 chart. This repairs
the proof gap that would arise from removing H without this identity.
The three normalizations of f3,f4,f5 therefore preserve every candidate.
A common finite m root forces both fixed-degree resultants R34,R35 to
vanish. This implication is valid even when their m-leading degrees drop;
no converse resultant implication is being used.

The completed literal original-resultant witness combines R34,R35 to
`q^53(q-2)^44 Pc^69`, a unit on this chart. The completed D=0 witness
combines the original f3,f4 numerators to q^4. On D=0 the displayed a
coefficient can vanish only when L1 does, by the same derivative identity;
its additional quartic V is therefore not a missing a-solve stratum.
At q=2 the owner gives an original five-generator witness, over the exact
field QQ(mu), mu^2=3, for f2,f3,f4,f5 together with
`1-z*d*(d+2mu/3)`. Both embeddings apply to the characteristic-zero
algebraically closed ground field, so the two L2 roots are retained.
The inverse equation imposes precisely the stated d,L1 units.

These literal witnesses are saved under
`validation/2026-10-13-generalization-quintic-l2/`; the completed Bezout
source asserts the three coefficient normalizations and both original
products before saving them, and the q2 source asserts its matrix product.
The evidence comprises the actual input pairs, targets, columns and raw
PASS streams, rather than just gcd factors or a saturated ideal printout.
This independent review inspects those exact constructions and accepts
their geometry; it does not count them as fresh independent executions.

**Audit conclusion: the local regular-L2 theorem and its all-mate
single-root consequence are proved by the displayed cover and completed
literal owner certificates, within their precise scope.** The latter
consequence additionally needs Jbar nonzero and q to be the sole common
homogeneous conormal root. Then full support concentrates the actual
nonzero degree-eight binary section at q, forcing order eight, while
nonvanishing of at least one of f2 through f5 gives order at most five.
The regular-L1 geometric bridge is reviewed explicitly in section 8.

This does not prove an order bound on Z=0, target infinity, q=0, Jbar=0,
or the excluded L1 branch. It does not exclude several support points
sharing conductor degree eight. All those distinctions survive handoff.

The independent audit additionally verifies nine small rational-cover
identities directly, without loading F or an inherited source. They
include the compact discriminant, the cover equation and inverse, the
L1/H identity, the D factor, and the D=0 solve. On D=0 the exact relation
is `L1=-q(q-2)V/[8(q-1)]`, confirming directly that V=0 is the already
excluded L1=0 boundary. The original full L2 discriminant at q=2 is
48d^6; the normalized quadratic after removing 2d has discriminant 12d^4.
Either is nonzero for d nonzero. This clarifies an exponent slip in the
owner note without changing its conclusion. The
[new small source](../validation/2026-10-14-quintic-independent-audit/l2-cover-algebra.m2)
has exit zero and nine literal PASS statements in its
[raw output](../validation/2026-10-14-quintic-independent-audit/l2-cover-algebra.stdout.txt).
The first version's unparenthesized `diff` expression caused an M2 parse
failure and is retained. An unexecuted Python alternative was abandoned
because the remembered CAS runtime is absent and system Python has no
SymPy; it supplies no evidence.

## 8. Independent review of the existing regular-L1 geometric bridge

The exact identities in the
[October 13 quotient-fiber note](NONENDPOINT_SINGLE_ROOT_INCIDENCE.md)
were already captured and verified, but its geometric bridge still
requested independent review. This section reviews only that implication;
its eleven-identity checker and separate exact double-root checker were
not replayed.

On `qZ(q)!=0`, the actual finite normalization-point reconstruction in
the accepted fiber model applies to common quotient roots. Put
`rho=d/q`. After removing the diagonal factors, the exact linear and
quadratic quotients are L and Q, with normalized quotient norm

    OffNorm=d^2 q^5 U^2 L1.

When Aq!=0, L is a genuine linear polynomial. On L1=0 its unique finite
root also solves Q. When Aq=0, the accepted cubic's quadratic coefficient
is `-q[3d^2q(2-q)]^2`, nonzero on this chart. Thus Q after diagonal
division is a genuine linear polynomial. Its leading coefficient is
nonzero, and OffNorm=0 forces the constant L to vanish identically; Q
still has a finite common root. This retains the leading drop rather
than mistaking a fixed-degree resultant factor Aq for a point.

Full inverse support forces every such root to equal rho; an off-diagonal
root reconstructs an actual normalization point outside c. It follows
that `L(rho)=Q(rho)=0`. A doubled or tripled fiber supported at rho is
allowed at this stage and is not excluded by saturation.

The exact equation `L(rho)=dq*S=0` excludes q=1,2 and gives
`k=d+d^2(2q-3)/[3(q-1)(q-2)]`. The exact Q(rho) equation then forces

    d=Pc(q-2)/[q(q-1)].

That last equation is used even when `P6=q^2-3q+3` vanishes and Aq=0.
The proof does not divide by P6, so this degree-drop component is retained.
The captured actual-section computation on these precise parameters is

    F(q+t)=f2*t^2+terms of degree at least three,
    f2=(q-2)^4 Pc^12/[9q^8(q-1)^8] != 0.

All factors in this expression are units under the stated chart and the
just-derived exclusions q=1,2. If Jbar!=0 and q is the sole common
homogeneous conormal root, the accepted support bridge requires the
nonzero degree-eight conductor form to be concentrated at q, hence to
have order eight. Its actual order two contradicts that requirement.

**Audit conclusion: the regular-L1 all-mate exclusion is now independently
accepted in exactly this sole-root, Jbar-nonzero, qZ-nonzero scope.** This
supplies the previously pending geometric premise needed for section 7's
combined regular sole-root theorem. No such conclusion is extended to
Z=0, other conormal roots, or an allowed A4 contribution when Jbar=0.

## 9. Continuation boundary and evidence accounting

The new reviewed mathematics already excludes the zero-cubic and
lambda-one h=3 charts, the three-root and multiplicity-at-least-four main
h=3 alternatives, and the regular finite sole-root Jbar-nonzero lane in
every mate degree. The degree-independent root-support lemma in section 4
is an additional reusable result. The final main 3+2 witness is the
specific remaining review item in this note; no global quintic or C0
conclusion is drawn while it is pending.

All exact arithmetic counts in the independent report refer to stated
identity products and coefficient bindings. They do not re-prove the
normalization/conductor theorem, exhaust other parameter strata, or
establish novelty. The failed sources and interrupted direct saturation
and Hermite approaches remain useful provenance, but supply no missing
theorem. Additional completed witnesses can be appended to this audit
without replaying accepted verifiers.


---

## Source: 2026-10-14-generalization-ribbon-independent-review.md

# Independent written review of the symbolic-ribbon generalization

Date: 2026-10-14. Reviewer: `global_structure`, distinct from the author
`ribbon_general`. Status: **NEW CONDITIONAL THEOREM REVIEWED; root
acceptance remains separate**. This is mathematical review of a new
written proof. No accepted repository statement or verifier was rerun.

The reviewed source is
[the symbolic-ribbon criterion](OCT13_THICK_EQUALITY_SOCLE_AND_FILTRATIONS.md#source-2026-10-13-generalization-ribbon-numerical-criterionmd).
I independently reconstructed its sheaf arguments, multiplication maps,
Euler identity and all displayed numerical specializations. The theorem
is sound under its stated normality, smooth curve, actual Cartier
relation, finite normalized-carrier map and degree-one-lift hypotheses.
Its conormal inequality additionally requires the stated generically
nonzero first-layer map; the valuation version instead measures its
first surviving layer.

## 1. What makes the symbolic double an entire ribbon

On a normal surface every divisorial ideal `I_i=O(-ic)` is reflexive
and has depth two at closed points. The quotient of `I_i` by
`I_(i+1)` has depth at least one by the depth lemma. The quotient is
annihilated by the reduced curve ideal `I_1`, has generic rank one
on `c`, and has no finite-point torsion. Because `c` is smooth it is
therefore a line bundle `E_i`, including at singular points of the
ambient normal surface.

The defining valuation inequalities prove `I_1^2 subset I_2` and
`sqrt(I_2)=I_1`. Hence `O/I_2` has square-zero nilideal `E_1` and
is Cohen--Macaulay of generic length two. This is the entire symbolic
ribbon; no Cartierness of `2c` has entered. The corresponding assertion
for ordinary ideal squares would not follow from this proof.

## 2. Multiplication and the actual Cartier relation

Products of representatives descend to

    E_i tensor E_j -> E_(i+j)

because changing a representative introduces a product in
`I_(i+j+1)`. This is an `O_c`-linear map, generically an isomorphism,
and therefore an injection of line bundles. Its zero divisor is
effective. Associativity verifies the coefficientwise defect
inequality in the author's note.

If `rc~bH` is Cartier, the equality of divisorial sheaves is

    I_(i+r)=I_i tensor O(-rc).

It gives `E_r=O_c(-bH)` and the stated periodicity. Multiplying a
layer until its index is a multiple of `r` gives

    deg E_j <= -j d^2/a,

since `rd=ba`. This is independent of whether any ambient first
normal direction survives.

## 3. The Euler identity and conormal bounds

The hyperplane Euler difference computes

    chi(O_S(mH))=(a/2)m^2-(kappa/2)m+chi(O_S).

For the carrier application a general Cartier hyperplane section
avoids the isolated normal-surface singularities. The arithmetic
Euler difference also works without requiring its geometric
smoothness. Subtracting the value at `m=-b` from that at zero and
using the symbolic filtration yields

    sum_(i=0)^(r-1) deg E_i
      =-(ab^2+b kappa)/2-r(1-g).

Thus the arbitrary surface Euler constant cancels. The inequality
`deg E_i>=i ell`, for `ell=deg E_1`, gives exactly the author's
bound for `r>=2`. For `r=2` no higher multiplication defect remains,
so the bound is an equality.

A generically nonzero map `N_C*->E_1` gives a generically injective
dual map `E_1^{-1}->N_C`. Saturating this line can only increase
its degree. Therefore `ell>=-M` whenever `M` bounds all line
subbundle degrees of `N_C`. The larger splitting degree supplies
the exact `M` on `P1`; semistability supplies the separate claimed
slope bound on an arbitrary smooth curve.

The valuation refinement is also valid globally. If `q` is the
minimum generic valuation of the pulled-back ambient curve ideal,
that ideal lies in `I_q` by its defining valuation, and its square
lies in `I_(2q) subset I_(q+1)`. Passing to `E_q` therefore gives
a map from the ambient conormal bundle. It is generically nonzero
by the definition of `q`, so the periodicity and saturation argument
give `q d^2<=a M`. This does not manufacture singleton support or
an isomorphic lift; those remain assumptions.

## 4. Numerical scope and one corrected sentence

Substitution of `M=2d-1,g=0,kappa=2pi-a-2` gives

    r[d^2-a(2d-1)]+2d(pi-1)+a(d+1)<=0.

At `a=d` it reduces to `2pi<=(r-1)(d-1)`. At `r=2,a=d`, the
nilbundle has degree exactly `-d-2pi`. This proves the all-degree
balanced-rational Cartier-double obstruction `2pi>d-1`, conditional
on the actual double relation and nonzero first conormal map.

The accepted quintic input gives only `ell<=-7/2`, hence
`-7<=ell<=-4`; the new criterion does not exclude it. The existing
quartic bisection instance is used as an accepted specialization,
not reverified.

During review I found one overbroad monotonicity sentence: increasing
`r` need not weaken the Euler bound merely because `pi>=g` when
`a` and `d` differ. The author corrected this before finalization.
Writing the upper bound as

    -A-(A+B)/(r-1),
    A=d^2/a, B=d kappa/a+2(1-g),

shows that enlargement weakens it precisely when `A+B>=0`.
For `a=d` this sign is `2(pi-g)`. No theorem conclusion depended
on the former broad sentence.

This review accepts the stated conditional inequalities and ribbon
construction. It supplies no global Cartier-index bound, no
classification of the multiplication defects, no exclusion for
multiple normalization primes, and no unrestricted STCI resolution.


---

## Source: 2026-10-14-moving-linear-quadratic-obstruction-independent-audit.md

# Moving linear relations: exact quadratic obstruction and independent review

Date: 2026-10-14. Status: independently derived new compatibility calculation;
the accepted embedded quadratic transition is used as a premise. No previous
normal-bundle or constant-direction computation is repeated.

This note reviews the moving operator in Section 8 of
[the thick relation extension](OCT13_THICK_EQUALITY_SOCLE_AND_FILTRATIONS.md#source-2026-10-13-generalization-thick-equality-extensionmd)
for a moving **linear** relation. The calculation gives an obstruction-zero
family, rather than an exclusion theorem.

## 1. Frames and the cohomology target

Write the actual conormal bundle as `E=O(-7)^2`. Let the relation line be
`W=O(-8)` with basepoint-free image

    f=a(z)u+b(z)v,
    a=A+Cz,  b=B+Dz,  Delta=AD-BC != 0.

On the second chart, `w=z^-1` on the reduced curve, the coefficient pair is
`a_1=Aw+C=z^-1 a`, `b_1=Bw+D=z^-1 b`. The normal frames satisfy
`u'=z^-7 u`, `v'=z^-7 v` to first order, and the relation frame satisfies
`W_1=z^-8 W_0`.

The quotient `M=E/W` is `O(-6)`. Locally its generator `q` is normalized by
`u -> b q`, `v -> -a q`. Since the second-chart coefficients have the extra
factor `z^-1`, its frame transition is `q_1=z^-6 q_0`. Thus the degree-two
relation obstruction has target

    Q=Hom(W, Sym^2 M)=O(-4),
    (q_1^2/W_1)=z^-4(q_0^2/W_0).

Consequently, evaluating the chart-zero quadratic discrepancy at
`(u,v)=(b,-a)` produces the coefficient in the chart-zero frame of `Q`, with
**no extra power of z**. Its Cech cohomology class retains exactly the
coefficients of `z^-1,z^-2,z^-3`. Nonnegative exponents are first-chart
coboundaries; exponents at most `-4` are second-chart coboundaries.

More generally, a basepoint-free linear relation of movement degree `e`
has `W=O(-7-e)`, `M=O(e-7)`, and

    Q=Hom(W,Sym^2 M)=O(3e-7).

For `e>=2`, `H^1(Q)=0`, so this one-step obstruction gives no exclusion.

## 2. Exact coefficient calculation

Use the accepted quadratic chart terms

    Du=-(5/2)z^-4 u^2-3z^-3 uv-(3/8)z^-2 v^2,
    Dv=3z^-5 u^2-z^-4 uv-(9/4)z^-3 v^2.

The moving operator is

    Du f_u+Dv f_v+(z^-3 u+(1/2)z^-2 v) f_z.

Here `f_z=C u+D v`, and its value at `(b,-a)` is
`Cb-Da=-Delta`. The evaluated discrepancy is therefore exactly

    T=3 z^-5 b^3-(3/2)z^-4 a b^2
      +(3/4)z^-3 a^2 b-(3/8)z^-2 a^3
      -Delta z^-3 b+(Delta/2)z^-2 a.

The three cohomology coefficients are

    4 [z^-3]T = B(36D^2-16AD+3A^2-2BC),

    8 [z^-2]T = 24D^3-20AD^2+10A^2D-3A^3
                 +8BC(A-2D),

    8 [z^-1]T = C(-12D^2+16AD-9A^2+2BC).

These formulas include the base derivative. Dropping that term changes the
zero locus and is not a valid moving-relation calculation.

## 3. Complete obstruction-zero locus on Delta != 0

All statements here are in characteristic zero over an algebraically
closed field, and `[A:B:C:D]` is considered up to common nonzero scale.

If `B=C=0`, then `A,D` are nonzero. With `t=A/D`, the remaining equation is

    24-20t+10t^2-3t^3
      =-(t-2)(3t^2-4t+12)=0.

This gives three distinct diagonal points:

    [A:B:C:D]=[t:0:0:1],
    t=2, (2+4 sqrt(-2))/3, (2-4 sqrt(-2))/3.

The point `t=2` is the accepted quadric direction
`q=u+(z/2)v`. In that direction the raw discrepancy `T` itself is zero.

If `C=0` and `B!=0`, then `Delta=AD!=0`. The first and second coefficient
equations would require a common root of
`3t^2-16t+36` and `(t-2)(3t^2-4t+12)`. The first polynomial does not vanish
at `2`; its difference from `3t^2-4t+12` is `-12(t-2)`, so no common root
exists. If `B=0` and `C!=0`, the analogous pair is
`9t^2-16t+12` and `(t-2)(3t^2-4t+12)`. The first does not vanish at `2`;
its difference from three times the second quadratic is `-4(t+6)`, and
its value at `-6` is `432`. Again there is no common root.

If `B,C` are both nonzero, the first and third equations give
`A^2=4D^2`. Necessarily `D!=0`. For `A=-2D` they force `BC=40D^2`, and the
middle equation becomes `-1152D^3=0`, which is impossible. For `A=2D`
they force `BC=8D^2`, and the middle equation vanishes identically.
Moreover, `Delta=-6D^2!=0`.

Thus the exact zero locus is the disjoint union of the three diagonal
points above and the open conic

    A=2D,  BC=8D^2,  D!=0.

The closure of this conic has two points with `D=0`; both have `Delta=0`
and are outside the basepoint-free degree-one problem. Passing the
quadratic obstruction means compatibility through this one normal step;
it does not prove a global surface, primitive quadruple, or STCI pair.

## 4. Independent review of the pure-power quotient

Let `L=O(-e)` be any basepoint-free moving direction inside the constant
rank-two bundle `V tensor O`, and consider the pure-power relation
`m^r` of movement degree `re`. Put

    Q_tilde=Sym^(r+1)V / (L^r tensor V).

The annihilator line `L_perp` inside `V^* tensor O` is `O(-e)`. The
annihilator of `m^r V` under the perfect characteristic-zero symmetric
pairing is exactly

    (L_perp)^2 tensor Sym^(r-1)V^*.

Indeed, in a basis with `m` the first vector, the two vectors spanning
`m^r V` have exponents `(r+1,0)` and `(r,1)`; their annihilator consists
precisely of degree-`r+1` dual binary forms divisible by the square of the
second dual variable. This is a fiberwise equality of rank-`r` bundles,
so

    Q_tilde^*=O(-2e)^r,
    Q_tilde=O(2e)^r.

After restoring the conormal twist and tensoring with the dual relation
line, the actual next-order obstruction bundle is

    Q_r=O((r+2)e-7)^r.

For `e=1`, all pure powers of order `r>=4` therefore have zero
`H^1(Q_r)`. For `e>=2`, already `r>=1` gives zero `H^1(Q_r)`. This proves
that no universal exclusion of moving pure-power first relations can
come from this quadratic step alone. It does not assert the existence
of a complete-intersection thickening with such a first relation.

For the actual quadric direction, the global equation `q^r` supplies
all higher-order lifts of the single relation. A new second independent
relation, or additional full-algebra constraints, is required to obtain
an STCI exclusion.

## 5. All finite steps before the second independent relation

The apolar argument extends to every step `k>=1`. For the pure-power
first relation `m^r`, the initial multiples in degree `r+k` are
`L^r tensor Sym^k V`. Their annihilator is precisely

    (L_perp)^(k+1) tensor Sym^(r-1)V^*.

This follows in the same basis: the initial multiples have second-variable
exponents `0,...,k`, and their annihilator has second-variable exponent at
least `k+1`. It is an equality of rank-`r` bundles. Thus, after the actual
conormal twist and dual relation twist, the obstruction bundle is

    Q_k=Hom(W_r, Sym^(r+k)E / (W_r tensor Sym^k E))
       =O((r+k+1)e-7k)^r,
    W_r=O(-r(7+e)).

The displayed direct-sum isomorphism is independent of local direction
coordinates. A fixed volume form on the constant two-dimensional vector
space identifies the annihilator line with `L`; changing that volume form
only introduces a constant one-dimensional factor.

If all these `H^1(Q_k)` vanish for `1<=k<g`, one can construct a coherent
principal-relation ideal modulo `I_C^(r+g)` with associated initial ideal
generated by `m^r` in every order below `r+g`. Here is the precise finite
construction. Choose arbitrary local lifts of the leading relation on an
affine cover. Assuming they already glue, up to multiplication by units,
through order `r+k-1`, their degree-`r+k` discrepancy is a Cech cocycle
with values in `Q_k`. Vanishing of `H^1(Q_k)` permits local degree-`r+k`
corrections; the discrepancy left in `W_r tensor Sym^k E` is removed by
changing the gluing units in normal degree `k`. The generated local ideals
then agree modulo `I_C^(r+k+1)`. Iterating gives the claimed finite ideal.
Local multiplication by the nonzero leading polynomial `m^r` is injective
in the symmetric normal algebra; consequently this construction adds no
unexpected initial relation or torsion layer below the cutoff.

This is a finite formal-neighborhood construction, not the construction
of a global hypersurface or a complete-intersection pair. No algebraization
or compatible infinite-order lifting is asserted here.

For `1<=e<7`, the obstruction-bundle degree decreases with `k`. All the
required groups vanish if and only if

    (r+g)e >= 7g-8.

For `e=1`, this reads `r>=6g-8`. In particular, for any prescribed finite
gap `g`, moving pure-power first relations of sufficiently high order pass
every formal compatibility step before the second independent relation.
Thus increasing the finite jet order cannot by itself give a uniform
exclusion of all such moving first relations. The full algebra, the
independent second relation, or a global condition must enter a universal
argument.

## 6. Audit scope

The new coefficient equations, their complete case split, the frame
identification, the pure-power splitting at every step, and the finite
principal-relation lifting argument have been independently derived. The
accepted chart transition and accepted quadric equation
were used without re-verification. No new finite test is promoted to a
proof of global existence. The next unresolved calculation is the
cubic compatibility of the obstruction-zero moving linear relations.


---

## Source: 2026-10-14-normal-carrier-picard-local-torsion-primary.md

# Normal carrier Picard and local torsion: primary sources and new index audit

Date: 2026-10-14. Owner: `normal_torsion_primary`, child of `conductor_general`.

Scope: integral normal hypersurface surface `X` in projective three-space over an algebraically closed characteristic-zero field. The smooth rational quartic `C0` is fixed. Previously accepted exclusions of all mates of degree at most four are premises; no inherited verification was rerun. This note records new source checks and new numerical deductions only.

## 1. Picard torsion vanishes; Weil class torsion need not vanish

**KNOWN, primary theorem.** [Grothendieck, SGA 2, Expose XII, Corollary 3.5](https://wstein.org/sga/circle/SGA2.pdf), printed p.120, PDF page 128: for a projective scheme `V`, an ample invertible sheaf, and a regular section with zero scheme `Z`, the map of etale fundamental groups is surjective when the ambient depth at closed points is at least two. With depth at least three at closed points of `Z`, and purity at closed points outside `Z`, it is an isomorphism. Regular local rings give the required purity.

Apply this with `V=P3`, the ample sheaf `O(a)`, and the equation of `X`. The ambient local rings have depth three and are regular everywhere. Thus `pi_1^et(X)=pi_1^et(P3)=1`. The triviality for projective space can also be obtained by repeated applications of the same corollary starting with `P1`, whose connected finite etale covers are trivial by Riemann-Hurwitz.

**PROVED consequence.** [Stacks Project, Kummer theory, Lemma 59.28.1](https://stacks.math.columbia.edu/tag/03PK) applies to every positive integer in characteristic zero. Since the only global units on integral proper `X` are constants and the field is algebraically closed, Kummer gives

`Pic(X)[n] = H^1_et(X,mu_n) = Hom_cont(pi_1^et(X),mu_n) = 0`.

Therefore `Pic(X)` is torsion-free. This statement does **not** imply that `Cl(X)` is torsion-free.

**KNOWN, primary local-global sequence.** [Hartshorne--Polini, Divisors Class Groups of Singular Surfaces, Proposition 2.2(c)](https://arxiv.org/pdf/1301.3222), pp.2--3, gives the sequence of Picard, almost Picard, and local almost Picard groups. For a normal surface it specializes to

`0 -> Pic(X) -> Cl(X) -> direct_sum_{P in Sing(X)} Cl(O_X,P)`.

Exactness at `Cl(X)` is the required assertion; no surjectivity onto the direct sum is assumed. Picard torsion-freeness implies that localization is injective on the torsion subgroup of `Cl(X)`.

## 2. Exact local-index formula for the normal quartic carrier

Write `a=deg X`, `g=gcd(a,4)`, `mu=a/g`, `v=4/g`, and

`Delta0 = mu[C0] - v[H]`.

Assume `Delta0` has finite order `t`; this is the accepted normal-carrier mate criterion. The accepted exact progression of mate degrees gives `b_min=v*t`.

**PROVED HERE.** Let `r_P` be the algebraic local Cartier index of `C0` at `P in C0 intersect Sing(X)`. These indices are finite: the torsion relation makes `t*mu*C0` Cartier. Off `C0`, the local class of `Delta0` is zero. At a point on `C0` its local class is `mu[C0]_P`, hence its order is `r_P/gcd(r_P,mu)`. Injectivity of localization on global torsion gives

`t = lcm_P (r_P/gcd(r_P,mu))`.

Set `R=lcm_P r_P`, using `R=1` for the empty set. For each prime `ell`, the valuation on the preceding least common multiple is

`max_P max(v_ell(r_P)-v_ell(mu),0) = max(v_ell(R)-v_ell(mu),0)`.

Consequently

`t = R/gcd(R,mu)` and `b_min = (4/g)*R/gcd(R,a/g)`.

If `R` divides `a=g*mu`, the valuation formula gives `t` dividing `g`, so `b_min<=4`. The accepted low-degree exclusions therefore imply:

**Every normal carrier admitting a mate must have at least one singular point on `C0` whose local Cartier index does not divide the carrier degree.**

The special case `C0` disjoint from `Sing(X)` has `R=t=1` and is excluded. The same conclusion follows directly because then `C0` is Cartier everywhere, so `Delta0` is a torsion element of `Pic(X)` and must vanish.

## 3. Ordinary nodes and bounded local exponents

**KNOWN, primary local class computations.** [Brevik--Nollet, Local Picard Groups, Sections 4.1.1--4.1.3](https://arxiv.org/pdf/1110.1867), pp.8--9, give the completed rational-double-point class groups:

| Type | Completed local class group | Exponent |
|---|---|---|
| `A_n` | `Z/(n+1)` | `n+1` |
| `D_n`, `n` odd | `Z/4` | `4` |
| `D_n`, `n` even | `(Z/2)^2` | `2` |
| `E_6` | `Z/3` | `3` |
| `E_7` | `Z/2` | `2` |
| `E_8` | `0` | `1` |

Their Proposition 2.4 uses the injective map from the algebraic local class group to the completed class group. Its injectivity follows by faithful flat descent: if the completed rank-one reflexive module is free, the original module is free. In this normal excellent setting completion preserves the relevant rank-one reflexive module.

Source caution: the introductory summary at the beginning of their Section 4 reverses some `D_n` parity and `E_6/E_7` assignments. The detailed subsections and the introduction's explicit `D_n` discussion agree with the table above; use those precise locations.

**PROVED HERE, node corollary.** At an ordinary node, completion has exponent two, so `r_P` divides two. A smooth curve through a singular surface point cannot be Cartier: if its local ideal is `(f)`, the one-dimensional quotient is regular, giving embedding dimension of the surface local ring at most two, hence regularity. Thus a node on `C0` has `r_P=2`.

If all singularities on `C0` are ordinary nodes, `R` is one or two. For even `a`, `R` divides `a`; all these carriers are excluded. For odd `a`, the torsion formula alone requires a node on `C0`, and then `g=1`, `mu=a` odd, `R=t=2`, and `b_min=8`. The stronger Cartier-intersection constraint in Section 6 also excludes this odd-degree possibility. Thus the final result excludes all normal carriers with only ordinary nodes on `C0`, in every carrier degree covered by the accepted low-degree-carrier exclusions.

More generally, if every on-curve local class group has exponent dividing `L`, then `R` divides `L` and

`t divides L/gcd(L,mu)`, so `b_min <= (4/g)*L/gcd(L,a/g)`.

All new formulas and both node parity consequences passed an independent symbolic argument supplied to `conductor_general`. Algebraic local indices, not an unsupported equality between algebraic and analytic class groups, are used throughout.

## 4. Failure shield: normal hypersurface class groups can have torsion

**KNOWN construction plus explicit consequence.** [Elsenhans--Jahnel, Kummer Surfaces and the Computation of the Picard Group, Sections 4.2--4.3](https://arxiv.org/pdf/1109.4346), pp.6--7, describe a Kummer quartic `Q` with sixteen ordinary nodes, its abelian double cover, and the divisibility of the exceptional sum on the resolution `S`:

`2 alpha = E_1+...+E_16` in `Pic(S)`.

The exceptional curves are linearly independent over the rationals, as their intersection matrix is diagonal with entries `-2`. Under `Pic(S)=Cl(S) -> Cl(Q)`, the class of `alpha` has order two: its double is exceptionally supported, while `alpha` cannot be an integral combination of the `E_i`. Thus a normal quartic hypersurface has nonzero torsion in its Weil class group, although its Picard group is torsion-free.

This example defeats any unrestricted claim that normal projective hypersurfaces in `P3` have torsion-free `Cl`. It supplies no normal carrier for `C0` satisfying the required torsion relation; that is a separate problem.

## 5. Precise cyclic-cover source and its scope

[Ambro, Cyclic Covers and Toroidal Embeddings, Section 4, Lemmas 4.1--4.2](https://arxiv.org/pdf/1310.3951), pp.25--26, prove that a torsion Weil divisor of exact order `t`, with `t` prime to the characteristic, gives an irreducible normal cyclic cover of degree `t` by adjoining the root of a principal representative of `tD`. Lemma 3.5, p.22, gives the codimension-one ramification index `t/gcd(t,ord_E(phi))`; the proof of Lemma 3.6, p.23, gives etaleness on the regular locus when `D` is integral. Hence the torsion cover is quasi-etale, rather than necessarily etale at singular points.

Source caution: Theorem 0.1(a)'s introductory phrase about the entire etale locus, if read literally for non-Cartier integral `D`, is overbroad and conflicts with the stated flatness criterion. The precise later lemmas and the local Cartier argument are sufficient here. Do not use that introductory phrase to erase singular-point ramification.

No statement about the fundamental group of `X_reg` being trivial has been obtained or assumed. The Kummer example proves that such a general assertion is false. No universal bound on `t` across unbounded carrier degree is claimed.

## 6. New integral Cartier-intersection constraint and finite index families

Added on 2026-10-14 after the preceding source work. This is a new independent audit of the root's suggested strengthening, not a replay of an inherited computation.

**PROVED HERE.** Under the mate relation, `C0` is Q-Cartier. By the definition of each algebraic local index, `R*C0` is Cartier at every singular point on `C0`. It is automatically Cartier at regular points and, as a divisor, is zero locally outside `C0`. Therefore `R*C0` is globally Cartier.

If a mate gives `m*C0 ~ b*H`, intersection with `H` gives `4m=ab`, so `b/m=4/a`. The rational self-intersection is consequently

`C0^2 = (b/m)(H.C0) = 16/a`.

Equivalently, one can avoid treating the Q-Cartier self-intersection as a separate definition: restrict the line-bundle relation for `m*R*C0 ~ b*R*H` to `C0`, then take integer degrees and divide by `m`. Since `H|C0` has degree four, this gives

`deg(O_X(R*C0)|C0) = 4bR/m = 16R/a`.

The left side is the degree of an actual invertible sheaf on the smooth projective curve. It is an integer, hence

`a divides 16R`.

This argument would also work for an integral projective curve of degree `d`, giving `a divides d^2 R`, whenever the mate relation and actual local Cartier indices exist.

**PROVED finite arithmetic consequences.** Assume the accepted exclusion of normal carrier degrees at most four, so a surviving carrier has `a>=5`. If every local index divides a fixed integer `L`, enumerate only

`R|L`, `a|16R`, `g=gcd(a,4)`, `t=R/gcd(R,a/g)`, `b_min=(4/g)*t>4`.

An elementary integer divisor enumeration gives:

| Local index bound | Surviving `(a,R,t,b_min)` |
|---|---|
| `L=2` | none |
| `L=3` | none |
| `L=4` | none |
| `L=6` | none |
| `L=12` | `(6,12,4,8)` and `(8,12,6,6)` |

For `L=12`, the proper-divisor values `R=1,2,3,4,6` are already excluded by the preceding rows. For `R=12`, the carrier degrees to inspect are the divisors of `192` at least five: `6,8,12,16,24,32,48,64,96,192`. Substitution in the exact torsion formula leaves precisely `6` and `8`; the degree `12` case has mate degree four and the remaining cases have smaller mates. The enumeration was also checked with a short Python integer-divisor loop; this is elementary arithmetic verification, not a new CAS certificate or a rerun of an old verifier.

**Final node conclusion.** On-curve ordinary nodes give `R<=2`, so `a|32`. No odd carrier degree at least five divides `32`; the even degrees have already been excluded by `b_min<=4`. Hence all normal `C0` carriers whose on-curve singularities are ordinary nodes are excluded, assuming the accepted carrier-degree-at-most-four exclusions. Singularities away from `C0` are unrestricted in this statement.

The two `L=12` rows are only necessary arithmetic survivors. No existence statement, classification of actual on-curve ADE configurations, or global normal-carrier resolution follows from this table alone.


---

## Source: 2026-10-14-quadric-opposite-ruling-phase-normal-form.md

# Opposite ruling phases: the full coefficient normal form and a sparse-family obstruction

Date: 2026-10-14. Owner: `quadric_global_phase_geometry`, within the
projection/conductor continuation. Status: **NEW EXACT ELEMENTARY
REDUCTION; NO GLOBAL MATE OR FULL-SUPPORT CONSTRUCTION CLAIMED**.

Previously accepted Cartier-lift and conductor results are premises.
This calculation concerns only the smooth quadric target
`S=P1 x P1`, `H=(2,2)`, and its diagonal `c`.

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
