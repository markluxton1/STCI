# A finite phase space for a bounded projection family

Date: 2026-10-14. Owner: `phase_family_constructibility`.
Status: **NEW STRUCTURAL REDUCTION; independent review pending.** No inherited
certificate has been rerun. The accepted
[full conductor theorem](2026-10-13-generalization-conductor-theorem.md) and
[projection/contact reduction](2026-10-14-generalization-projection-contact-phase-criterion.md)
are premises. The reduction does not prove that the remaining fixed-C0
projection families contain any mate, or exclude them. It replaces the search
over all mate exponents by finite algebraic data and a precisely isolated
torsion condition.

## 1. An exponent-free full Artinian criterion

Let `F` be a characteristic-zero field and `A subset B` an injective unital
map of finite-dimensional commutative `F`-algebras. Allow both algebras to be
products of Artinian local algebras. Put `N_A=nil(A)` and `N_B=nil(B)`.

There are unique maximal etale `F`-subalgebras

    K subset A, E subset B,
    A=K direct_sum N_A, B=E direct_sum N_B.                 (1)

The inclusions are compatible: `K=E intersect A`, and `N_A=N_B intersect A`.
Indeed, their reductions are finite etale over the perfect field `F`;
formal etaleness lifts each reduction uniquely across a nilpotent ideal.
This is also the finite-dimensional case of the maximal weakly etale
subalgebra construction and its functoriality in
[Stacks, Section 15.107, Lemmas 2--3](https://stacks.math.columbia.edu/tag/0CKQ).

For a unit `u in B*`, write uniquely

    u=v exp(w), v in E*, w in N_B,                         (2)

where `v` is the lift of the reduction of `u`, and the exponential and
logarithm are finite series. Define

    D=E tensor_K E,
    rho=(v tensor 1)/(1 tensor v) in D*.                    (3)

**Artinian criterion.** The following are equivalent:

    some positive power of u belongs to A;
    w belongs to N_A and rho is a torsion unit of D.        (4)

Moreover, when (4) holds, the least descending exponent is the order of
`rho`.

Proof. For every positive integer `n`, compatibility of the etale splittings
and (2) give

    u^n in A iff v^n in K and n w in N_A
             iff v^n in K and w in N_A.                   (5)

The second equivalence uses characteristic zero. The finite etale map
`K -> E` is faithfully flat: it is injective, so every field factor of `K`
has an upstairs factor. Its equalizer identity is

    K={e in E: e tensor 1=1 tensor e in E tensor_K E}.

Thus `v^n in K` is exactly `rho^n=1`. This proves (4) and the exponent
assertion. It retains every nilpotent conductor layer; a reduced contact
test alone would omit the condition `w in N_A`.

## 2. Scalar phases without labelling geometric conductor branches

Now let `F=k(x)`, where `k` is algebraically closed of characteristic zero.
Let `d=dim_F(D)`, and let `chi_rho(Z)` be the characteristic polynomial of
multiplication by `rho` on the `F`-vector space `D`. The algebra `D` is finite
etale. Hence

    rho torsion iff chi_rho(Z)=product_(i=1)^d (Z-z_i)
                    for constants z_i in mu_infinity(k).  (6)

Repeated roots in this displayed characteristic polynomial are allowed.
Its minimal polynomial is squarefree. Therefore, if all `z_i` have orders
dividing `n`, the minimal polynomial divides `Z^n-1`, giving `rho^n=1`.
The converse follows by applying each geometric embedding of `D` to
`rho^n=1`. The exact order is `lcm_i order(z_i)`.

An important intermediate algebraic condition is

    every coefficient of chi_rho belongs to k subset k(x). (7)

This is equivalent to every reduced geometric pair ratio being constant.
It does not assert that the constants have finite order. It packages the
accepted entire-contact-divisor condition without separately normalizing
or labelling every pair curve. All conjugate branches and every split
comparison are included in `D`.

## 3. Finite algebra matrices give a finite-type phase cover

Let `T` be a finite-type reduced `k`-scheme. Suppose that, on each of finitely
many locally closed strata, the algebra data `A_t subset B_t` over `k(x)`
and the unit `u_t` are supplied by fixed-size multiplication and inclusion
matrices whose entries are rational functions of `x` and the parameters.
Every required denominator is assumed nonzero as a polynomial in `x` on
that stratum. Finite products of such algebra models are allowed.

There is a finite further stratification and a constructible locus `T_0`
with a finite surjective phase cover

    Z -> T_0,   z:Z -> G_m^d,                              (8)

such that:

* `T_0` is exactly the locus where `w_t in N_(A_t)` and (7) hold;
* the points above `t` are the ordered multisets of roots of
  `chi_(rho_t)` (using a product of phase covers for several models);
* `u_t` has an eventually descending power exactly when some, equivalently
  every, phase tuple above `t` belongs to `mu_infinity(k)^d`.

Here a constructible locus is represented by a finite disjoint union of
locally closed reduced schemes. The finite cover may be replaced by its
reduction. It need not be etale where some phases coincide.

All operations in this construction are bounded algebraic operations. A
detailed way to avoid an implicit quantifier over rational functions is:

1. The kernel of the trace pairing of a finite commutative algebra in
   characteristic zero is its nilradical. Over an algebraic closure this
   follows by decomposing into local factors: the trace on a local factor
   is its positive length times its residue, so its pairing has precisely
   the maximal ideal as radical. Kernel bases and membership tests are
   rational matrix operations on finitely many rank/minor strata.
2. The finite etale reduction has a primitive element, since `k(x)` is
   infinite. Choose one over the generic point of a stratum and retain its
   nonzero discriminant. If `p` is its squarefree polynomial and `b` an
   arbitrary lift, `p'(b)` is a unit. Finitely many Newton steps lift the
   primitive element into the algebra. Nilpotence index at most
   `dim_F(B)` bounds the number of steps. Substitution gives the canonical
   etale part `v` of `u`; finite logarithm gives `w`. Remaining parameter
   loci are treated by the same rank construction, not by an exponent
   search.
3. Form `D`, multiplication by `rho`, and its characteristic polynomial
   by finite linear algebra. Each coefficient is a bounded rational
   function `f(x,t)`. Its constancy in `x` is a finite algebraic condition:
   clear denominators in `partial f/partial x=0` and set all coefficients
   equal to zero. In characteristic zero the derivative kernel of `k(x)`
   is exactly `k`. On a finite refinement, the resulting constant is a
   regular parameter function: take the ratio of any selected nonzero
   coefficient of the denominator and the corresponding numerator
   coefficient.
4. Adjoin the scalar variables `z_i` and equate the elementary symmetric
   polynomials in them to these regular coefficients. This is finite over
   `T_0`: each `z_i` satisfies the same monic polynomial; their product is a
   unit, so their inverses are integral as well. Algebraic closedness gives
   a root ordering over every `k`-point.

Rank, discriminant, denominator, and primitive-element choices create
finitely many strata. For example, choose valid data over every generic
point, shrink to a dense open where the finitely many identities and
nonvanishings hold, and repeat on the closed complement. Noetherian
induction terminates. This does not introduce unknown functions of
unbounded degree or unbounded nilpotent exponents.

## 4. Why bounded projective projection families fit the matrix hypothesis

Fix a normal integral projective surface `S`, an ample line bundle `H`, a
smooth ample Cartier curve `c`, and a section `Q` with `div(Q)=m c`. Let a
finite-type parameter space supply four sections of `H` whose restrictions
to `c` give the fixed embedded curve `C subset P3`. Retain parameters where
the sections are basepointfree, the induced finite map `f_t:S->X_t` is
birational, and the full reduced inverse image of `C` is `c`. Assume the
images are integral hypersurfaces. These assumptions hold on the relevant
constructible locus in the accepted 16- and 40-parameter fixed-C0 models.

These admissibility requirements are constructible. Basepointfreeness is
open by properness of the basepoint incidence. An ample pullback forbids
positive-dimensional fibres, so the resulting projective map is finite.
Its image and its generic degree are controlled after flattening finite
presentations. Full inverse support is the complement of the constructible
image of `f^{-1}(C) minus (c times T)`; this keeps extra isolated inverse
points as well as extra curves. The image assertion uses
[Chevalley's theorem](https://stacks.math.columbia.edu/tag/00FE).

Here is a conductor construction that does not assume that formation of
the *actual* conductor commutes with every specialization.

Over the generic point of an irreducible parameter stratum take the
normalization inclusion and an actual common conductor ideal `I`. Spread
its finitely many generators, the inclusion, and the identities
`I B subset A` to a dense open of that stratum. Flatten the relevant
coherent modules so the inclusions and common-ideal quotients survive on
fibres. On a fibre the resulting common ideal may be smaller than its
actual conductor. This causes no loss: for any common ideal `J subset A`
that is also a `B`-ideal,

    b in A iff b mod J belongs to A/J subset B/J.           (9)

The generic ideal is nonzero on the integral image; shrink so the quotient
has fibre dimension at most one. Extra support introduced by a smaller
ideal only supplies an additional exact membership test, automatically
trivial where the normalization is already an isomorphism. These spreading
and flatness choices require finite presentations; a finite stratification
exists by
[generic flatness stratification](https://stacks.math.columbia.edu/tag/0ASY).

On finitely many target affine charts, trivialize `O_X(1)` and remove `C`.
Apply [Noether normalization](https://stacks.math.columbia.edu/tag/00OY) to
the generic one-dimensional conductor support. After rational localization
this supplies the field `k(T)(x)` and finite-dimensional full quotient
algebras `A/J subset B/J`. Choose bases and spread their finite
multiplication tables. Shrinking the parameter stratum makes all selected
denominators nonzero as polynomials in `x` and preserves the generic-fibre
bases and identities. Repeat on the closed parameter complement. This is
exactly the fixed-size rational matrix situation of Section 3. Several
affine charts can repeat the same generic conductor point; duplicate exact
tests do not affect the criterion.

The resulting ranks, hence all nilpotence indices, have a finite maximum
on these finitely many strata. Conductor components lying over `C` can be
handled separately: the residue of `Q` is zero on every upstairs branch,
so some uniformly bounded power vanishes in each of their Artinian
quotients. They impose a bounded lower threshold on a descending exponent,
and no further condition on eventual descent. Off `C`, the normalized
section in a target frame is a unit, and Sections 1--3 apply.

Finally, the accepted Cohen--Macaulay conductor theorem says that generic
membership at every conductor curve is global membership. Thus the phase
criterion is exact for existence of a mate. When the image is generically
regular along `C`, its least mate degree is exactly the common phase order.
Without that regularity, any mate exponent is a multiple of the phase
order; a sufficiently large such multiple also passes the bounded
vanishing threshold over `C`. This still proves eventual descent and makes
unbounded phase orders imply unbounded least mate degrees.

The matrix sizes are bounded for this fixed finite-type family. This is an
existence of a finite algebraic model, not a numerical bound extracted from
the canonical degree formulas, and not a claim that the model is already
computed for the three fixed-C0 families.

## 5. What the phase image does and does not settle

Let `W=z(Z) subset G_m^d`. It is constructible by Chevalley. The mate locus
is exactly the projection of

    Z(k) intersect z^{-1}(mu_infinity(k)^d).               (10)

The torsion condition in (10) is deliberately retained. The mate locus
need not itself be constructible: even the finite algebra family
`A=F` diagonally in `B=F times F`, `u=(1,t)`, over `t in G_m`, has eventual
descent exactly for `t in mu_infinity(k)`. In characteristic zero this is
infinite and has infinite complement, whereas constructible subsets of
`G_m` are finite or cofinite.

There is a useful exact one-phase dichotomy. Suppose, after a finite
refinement, the phase image lies in a fixed torsion translate of a
one-dimensional subtorus, parameterized as

    z_i=xi_i lambda^(m_i), xi_i fixed roots of unity,
    m_i integers, gcd(m_1,...,m_d)=1.                      (11)

The admissible `lambda` image is constructible in `G_m`. If it is finite,
only finitely many phase tuples can occur. If it is infinite, it is
cofinite. It consequently contains roots of unity of arbitrarily large
orders; every such value is realized by an admissible parameter and gives
a mate. Phase orders are unbounded: if `M` kills all `xi_i` and the phase
tuple has order `e`, Bezout on the `m_i` gives `lambda^(M e)=1`, hence
`e >= order(lambda)/M`.

The hypothesis (11) must be proved for the actual phase image. It cannot
be replaced by positive dimension. The curve

    {(lambda,2 lambda): lambda in G_m} subset G_m^2

is positive dimensional and contains no torsion point in characteristic
zero. Thus a multiphase image retains a substantive torsion-intersection
problem even after every contact and logarithmic condition has been made
algebraic.

For the fixed-C0 projective families this yields a concrete structural
target: construct the finite phase image after imposing the entire
nilpotent equations, and determine its torus relations. A surviving
one-phase torsion translate with infinite image would prove existence,
whereas a phase image with no torsion point would exclude the full family
at every mate degree. Neither alternative has yet been established.
