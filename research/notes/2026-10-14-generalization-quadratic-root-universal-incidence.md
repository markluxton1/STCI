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
