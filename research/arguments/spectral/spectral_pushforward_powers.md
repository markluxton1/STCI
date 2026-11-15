# Spectral powers, syzygy determinants and graded constructions

**Status.** Independently reviewed mathematics. The statements below concern actual spectral curves and
abstract graded algebras. They do not construct two ambient equations for C0.

The [fourth-power account](spectral_torsion_and_syzygy_splitting.md) gives the
existing actual second-obstruction application. The general
[spectral Picard criterion R-0008](../../results/spectral_root_picard_criterion.md)
already constructs a fiberwise coprime graded second relation from a spectral
trivialization. The coefficient construction here gives a uniform coefficient
matrix for every n>=2, together with recovery of that trivialization from
its kernel. The [torsion and involution argument](quadratic_root_second_obstruction.md#2026-10-15-generalization-quadratic-root-torsion-second-zero-geometry)
and [arbitrary-order examples](moving_power_and_spectral_roots.md#2026-10-14-generalization-spectral-root-curve-relations)
supply the inherited geometric constructions.

## 1. The pushforward of every power

Let k be algebraically closed, in any characteristic. First let Sigma be
any smooth projective genus-one curve, pi:Sigma->P1 a degree-two map,
A=pi*O(1), and B any degree-two line bundle. Put eta=B tensor A^-1.

**General pushforward theorem.** For EVERY integer n, including zero and
negative integers, put E_n=pi_*B^n. Then

    E_n = O(n-1) + O(n-1)       if eta^n is nontrivial;
    E_n = O(n-2) + O(n)         if eta^n is trivial.                 (1)

No origin, embedding, nontriviality of eta, separability or division by n
is required for this statement. The smooth (2,2) construction below is
an application with eta nontrivial, not its full scope.

**Proof.** A finite degree-two map between smooth curves is flat, so E_n
is locally free of rank two. Finite pushforward preserves Euler
characteristic. Genus-one Riemann--Roch gives chi(B^n)=2n; on P1,
chi(E_n)=2+deg(E_n), hence deg(E_n)=2n-2. By the splitting theorem
([Grothendieck, Theorem 2.1](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-25.pdf)),
write E_n=O(e1)+O(e2), e1<=e2 and e1+e2=2n-2. Projection formula gives

    H0(E_n(-n)) = H0(Sigma,eta^n).                               (3)

A nonzero section of a degree-zero line bundle on an integral projective
curve has no zeros and trivializes it. The right-hand dimension is
therefore zero or one, and is one exactly when eta^n is trivial.
If it is zero then e2<=n-1, forcing e1=e2=n-1. If it is one then
only the larger summand contributes and e2=n, e1=n-2. This proves
(1), also when n<=0. These are isomorphism classes, not chosen splittings.

Now let Z be a smooth divisor of bidegree (2,2) in
P1_base x P1_direction, with

    pi = pr_base|Z,  A = O_Z(1,0),  B = O_Z(0,1),  eta = B tensor A^-1.

The divisor sequence gives H0(O_Z)=k, so Z is connected; adjunction
gives genus one. Its finite flat projection has degree two. The ruling
difference eta is nontrivial: otherwise their complete degree-two systems
would identify both projections up to an automorphism, putting Z in a
(1,1) graph. The general theorem gives (1) for this root.

For n>=2 there is also an explicit presentation. Push the divisor sequence

    0 -> O(-2,n-2) --f--> O(0,n) -> O_Z(0,n) -> 0

to the base. Direction-fiber H1 vanishes in both terms, giving

    0 -> O(-2)^(n-1) -> O^(n+1) -> E_n -> 0.                       (2)

Thus these E_n are globally generated of rank two and degree 2n-2.
The presentation, unlike the general splitting lemma, starts at n=2.

## 2. One coefficient determinant for each power

Throughout the coefficient construction take n>=2. Write

    f = a(z)u^2 + b(z)uv + c(z)v^2,

where a,b,c are homogeneous binary quadratics with no common base zero.
The dual of (2) is

    0 -> W_n -> O^(n+1) --T_(f,n)--> O(2)^(n-1) -> 0,
    W_n = E_n^*.

The matrix T_(f,n) has n-1 rows and n+1 columns; row i has a,b,c in
columns i,i+1,i+2 and zero elsewhere. Its transpose is multiplication
by the nonzero fiber polynomial f on direction forms of degree n-2,
so it has the indicated rank at every base point.

Twist by n-2 and take global sections. This gives a square coefficient map

    C_(f,n): H0(O(n-2))^(n+1) -> H0(O(n))^(n-1),
    dim(source) = dim(target) = n^2-1.                            (4)

Its entries are linear in the nine coefficients of f. Define
D_n(f)=det C_(f,n), after choosing monomial bases. Only its nonzero
scalar factor depends on those choices. By (1),

    dim ker C_(f,n) = h0(W_n(n-2))
                   = 0 if eta^n != O_Z, and 1 if eta^n = O_Z.     (5)

Consequently D_n detects eta^n=O_Z on the smooth-root locus and has
homogeneous degree n^2-1. It is nonzero in every characteristic: choose an
elliptic curve with a prime-to-characteristic torsion point of order not
dividing n and use the two-degree-two-bundles construction in section 4.
Formula (5) describes geometric fibers only:
no assertion about determinant multiplicities, reducedness of its parameter
scheme, or transverse intersection with an ambient compatibility locus is made.
This qualification is particularly important when char(k) divides n.
For n=2 and n=4, (4) recovers the existing 3-by-3 and 15-by-15 detectors.
The independently reviewed [determinant-scheme continuation](spectral_determinant_schemes.md)
addresses the scheme structure on the smooth open separately.

The construction of the matrix and sequence (2) also makes sense for a
singular or nonreduced basepoint-free root. The independently reviewed
[full-root boundary analysis](spectral_pushforward_boundary.md) identifies
the additional hypotheses and the unbalanced reducible exception.

## 3. Recovering a positive graded object from the kernel

Suppose n>2 and D_n(f)=0 for a smooth root. A nonzero kernel vector in
(4) is a section of W_n(n-2). Since det E_n=O(2n-2), rank-two duality
identifies

    W_n(n-2) = E_n^*(n-2) ~= E_n(-n).                             (6)

The identification is up to the scalar choice of determinant frame. By
(3), this gives a nonzero section of eta^n, hence a trivialization of eta^n
and a nowhere-zero morphism A^n -> B^n on Z. Adjunction supplies the
corresponding subbundle O(n) -> E_n. On each length-two root fiber its
value is a unit, including at a ramification point with nonreduced fiber.

This is the missing input for the already proved R-0008 construction. In
its notation, for any line bundle H on the rational base, set

    E = H^-1 tensor k^2,  R = H^-2 tensor O(-2),
    Q_n = Sym^n E / (R Sym^(n-2)E) = H^-n tensor E_n.

The kernel-derived line is

    T = H^-n tensor O(n) -> Q_n.                                  (7)

Take the ideal generated by T in Sym E/(R), then its inverse image in
Sym E. Locally T lifts to a binary form g_n; the fiber ideals
(f_2,g_n) are regular sequences because the value of g_n is a unit on
the full root fiber. Their graded quotient is finite locally free of
rank 2n, with fiber type (2,n). This constructs an abstract graded
complete-intersection family directly from a coefficient kernel.

For the characteristic-zero quartic's balanced conormal frame H=O(7),
T=O(-6n). A global lift T->Sym^n E would lie in
H0(O(-n))^(n+1)=0. Thus the quotient line has local polynomial lifts
but no nonzero global polynomial-line lift. This is an actual feature
of the constructed graded family, not a contradiction to its existence.
Neither (6) nor (7) realizes it in the embedded formal neighborhood of C0,
and neither supplies a proper projective pair.

## 4. Exact-order and periodicity certificates

On the smooth-root locus put T[n]={f:D_n(f)=0}. The established Picard
interpretation and (5) give, set-theoretically,

    T[m] intersect T[n] = T[gcd(m,n)],  T[1] = empty.              (8)

Indeed eta is killed by m and n precisely when it is killed by their
greatest common divisor. For N>=2, eta has exact order N precisely when

    D_N=0 and D_(N/ell)!=0 for every prime ell dividing N,          (9)

where the index-one condition is omitted because eta is nontrivial.
These are finite exact-order tests using coefficients of the actual root.
They are not scheme-theoretic intersection or ideal-generation identities.

The reused involution argument identifies the composition of the two
ruling involutions with translation by eta on the genus-one curve. Thus
(9) is also an exact-period test for this automorphism, without computing
an elliptic group law. Its periodicity interpretation is inherited; the
uniform determinant and kernel extraction are the new coefficient realization.

The existing construction from a degree-two bundle A0 and a distinct
bundle A0 tensor eta on an elliptic curve realizes every exact torsion
order N>=2 in characteristic zero. The source's arbitrary N>2 argument
also works for N=2: nontriviality, rather than N>2, proves the product
map is a closed immersion. The rank sequence of (4) then drops exactly
at multiples of N. In characteristic p the same construction works
whenever an actual geometric torsion point of the required order is given;
prime-to-p orders are always available. No existence of geometric p-torsion
on every elliptic curve is assumed.

Within the unequal-degree first-relation convention of R-0008, we retain
n>2. The first allowed degree is therefore N for N>2, and 4 for exact
order two. Degree-two second relations lie outside this convention and
are not excluded by the determinant calculation.

### Coefficient matrices and represented Picard arithmetic

If the Jacobian and eta are already represented with usable group
operations, eta^n=1 can instead be tested by binary doubling and addition
in O(log n) group operations. Constructing that representation, necessary
field extensions, coefficient growth and bit costs are additional tasks.
The coefficient-matrix dimension is quadratic in n, but its polynomial
equations and specialization behavior can be preferable for an algebraic
family. At fixed n=4 this comparison gives no asymptotic improvement
claim for the existing solver.

An arbitrary change of ruling coordinates preserves (1) and the Picard
condition, but simplifies an actual lifting problem only when its higher
ambient transitions and actual operator are transported too. Keeping the
operator fixed permits only genuine ambient symmetries, such as the
proved torus and reversal. Torsion is intrinsic to (Sigma,A,B), not to
Sigma alone, and is not a complete ambient compatibility test. The
[first-operator example below](#6-testing-this-example-in-the-actual-embedding)
makes this distinction concrete.

## 5. An explicit order-three root

Over characteristic zero, take the smooth elliptic cubic

    y^2+y=x^3,  O=infinity,  P=(0,0).

The tangent y=0 meets the curve to order three at P, so P has exact
order three. The functions x and u=y/x define degree-two systems
with bundles A=O(2O) and B=O(O+(-P)), respectively. For u, the
apparent pole at P cancels, while the simple poles are O and -P.
Their ruling difference is eta=O((-P)-O), of exact order three.
Eliminating y=ux gives the biquadratic root

    x^2 - x u^2 - u = 0,
    f(s,t;u,v) = -st*u^2 - s^2*u*v + t^2*v^2.                    (10)

The two distinct degree-two bundles embed the elliptic curve as this
smooth (2,2) divisor by the reused product-map argument. Hence the
matrices C_(f,n) have corank one exactly when 3 divides n. In particular
n=3 supplies a graded family of type (2,3), and n=6 one of type (2,6).
These are deductions from the torsion construction and the theorem,
not a claimed computer-algebra execution or an ambient realization on C0.

## 6. Testing this example in the actual embedding

Work in characteristic zero and put z=t/s, so the example is
f=-z*u^2-u*v+z^2*v^2 in the fixed
balanced normal coordinates. The accepted first ambient operator of
[R-0007](../../results/quadratic_root_obstruction_model.md) is represented by

    d_f = pr_[z^-4,...,z^-1]( f_u*DU + f_v*DV + f_z*alpha ),
    DU = -(5/2)z^-4*u^2 - 3z^-3*u*v - (3/8)z^-2*v^2,
    DV = 3z^-5*u^2 - z^-4*u*v - (9/4)z^-3*v^2,
    alpha = z^-3*u + (1/2)z^-2*v.

The permitted equation-unit correction is f*h, with
h=a(z)u+b(z)v and a,b supported on z^-6,...,z^-1. The following
functional on the cubic Cech target annihilates every such correction:

    lambda(r) = -[z^-3]r_(u^3) + [z^-4]r_(u^2*v)
                +[z^-3]r_(v^3).

Indeed the relevant coefficients of f*h are -z*a, -a-z*b and z^2*b,
so lambda(f*h)=a_-4-a_-4-b_-5+b_-5=0. Direct substitution in d_f gives
the three tested coefficients 4, 7/2 and 0, hence

    lambda(d_f) = -1/2 != 0.                                    (11)

Thus this fixed embedded root fails the first ambient Cartier-lifting
test. Its graded constructions remain valid. Under the full hypotheses
of [R-0006](../../results/actual_ci_smooth_root_bridge.md), no actual pair
whose root is this fixed equation and whose gap s-2>=2 can realize it.
In particular increasing the next relation from six to twelve does not
repair this fixed root. This does not exclude the order-three torsion
locus: an abstract change of the two ruling coordinates need not preserve
the actual embedded operator, and varying roots requires a new test.

There is also a distinct numerical restriction on any projective target.
Under all the saturated/full-generic-CI hypotheses of
[R-0013](../../results/saturated_actual_generator_movement.md) and movement two,
[R-0014](../../results/movement_two_six_rows.md) leaves only

    (r,s;a,b)=(2,8;8,8) or (2,12;6,16)

when r=2. For a smooth root of exact order three, the Picard condition
3|s retains only the second row. A (2,6) graded family can therefore
be studied for embedded realizability in its own right, but cannot be the
full generic initial CI of a global pair under those hypotheses.
The corresponding projective construction question uses (2,12) and
surface degrees (6,16), and must vary the root beyond the failed example.

## Review and remaining realization question

Independent review on 2026-10-31 by `review_spectral_powers` (GPT-6.1 Sol,
high reasoning) reconstructed the characteristic-free pushforward proof,
coefficient-map orientation, determinant/kernel identification, quotient-ideal
construction, exact-order tests and explicit example against R-0008 and its
retained proof. The review passed after clarifying that n>2 is the
unequal-degree convention, not a nonexistence claim for degree-two second
relations. No mathematical computation was needed or run for sections 1--5.

For section 6, an exact rational diagnostic reused the
[accepted incidence generator](../../computations/generalization_quadratic_root_curve_universal_incidence.py)
at (a1,b0,c2)=(-1,-1,1), with all other coefficients zero. It found rank
12 and inconsistency. Equation (11) retains the complete three-term
certificate as a direct proof; no new verifier or generated output is
needed. Independent review by `review_spectral_powers` reconstructed its
three coefficients, annihilation identity, first-lift bridge and numerical
scope against R-0006, R-0007, R-0013 and R-0014. It passed after clarifying
that a question about embedded realizability does not assert an embedded
object. The reviewer did not rerun the diagnostic; the direct certificate
is the independently checked evidence.

The new construction ends at an abstract graded family. The next embedded
question is which of these families admit successive lifts in the actual
neighborhood of C0, with the fixed conormal embedding and all allowed higher
corrections retained. The [varying-root continuation](order_three_roots_and_sextic_lifts.md)
parameterizes the full smooth order-three locus and finds twenty-four
first-compatible roots on a covered four-parameter slice; all fail the actual
sextic source. The remaining
question concerns the other roots, with the projective numerical
scope in section 6 kept separate from graded or finite-neighborhood existence.
The inherited actual n=4 obstruction model keeps all hypotheses stated in
its owning chapter. No all-n ambient obstruction model, formal lift,
projective pair or change to C0's STCI status is asserted here.


## Consolidated historical supplement: `research/supplements/CYCLIC_COVER_AND_MOVING_LINEAR_RIGIDITY.md`

# cyclic cover and moving linear rigidity

Permanent subject dossier retaining full mathematical computations, counterexamples, proofs, precise hypotheses and unresolved scope. Computational implementations, where present, remain separate.

---

<a id="2026-10-14-cyclic-cover-local-smooth-curve"></a>

## Local torsion order, cyclic-cover splitting, and ramification along a smooth curve

Date: 2026-10-14. Author: `cyclic_cover_structure/local_torsion_curve`.

Status: **PROVED HERE**, with an independent audit of the explicit families in
[2026-10-14-cyclic-cover-D4-counterexample-audit.md](#2026-10-14-cyclic-cover-d4-counterexample-audit).
These are local results. They do not give a projective mate for `C0` or resolve
the universal STCI question.

The accepted repository results were used as premises. This note studies a
new proposed bridge: whether the local Cartier index of a smooth curve can be
read from ramification of its cyclic class cover. The answer is **no**, even
on a cyclic quotient hypersurface. There is instead an exact formula involving
a fractional intersection invariant and a separate splitting number.

### 1. Setup and the exact local formula

Let `k` be algebraically closed of characteristic zero. Let `(R,m)` be a
complete normal two-dimensional local `k`-algebra, excellent and with residue
field `k`. Let `P` be a height-one prime such that

\[
  R/P\simeq k[[t]].
\]

Write `C=V(P)`. Assume that `[C]` has exact finite order `r` in `Cl(R)`. Thus
there is `f` in `R` with

\[
  \operatorname{div}_R(f)=rC.
\]

Choose `a` in `R` with `v_C(a)=1`, and put

\[
  D=\operatorname{div}(a)-C,\qquad h=a^r/f.
\]

Then `D` is effective and has no `C` component. Normality gives `h` in `R`,
and `h` does not lie in `P`, since

\[
  \operatorname{div}(h)=rD.
\]

Define

\[
  m_C=\operatorname{ord}_t(h\bmod P),\qquad
  \lambda_C=\frac{m_C}{r}\pmod{\mathbf Z}\in\mathbf Q/\mathbf Z.
\]

The choice of `a` exists: a uniformizer of the DVR `R_P` can be written
`a/b` with `a,b` in `R` and `b` not in `P`. Its numerator has valuation one.

**Theorem 1.** Let `S` be the normalization of `R` in

\[
  L=\operatorname{Frac}(R)(T),\qquad T^r=f.
\]

The cyclic class cover `Spec S -> Spec R` has degree `r`, is connected and
local, and is étale away from the closed point. Its reduced inverse image
`C^#` is the effective Cartier divisor `T=0`. It is finite flat of degree `r`
over `C`. The normalization of `C^#` has exactly

\[
  \boxed{b=\gcd(r,m_C)}
\]

branches. Each branch maps to `C` with ramification index

\[
  \boxed{e=\frac{r}{\gcd(r,m_C)}=\operatorname{ord}(\lambda_C)}.
\]

In particular,

\[
  r=be,
\]

and `e=r` holds precisely when `gcd(r,m_C)=1`. The equality `e=r` is an
additional local primitivity condition, not a consequence of smoothness of
`C`, normality of the surface, or the hypersurface hypothesis.

The invariant `lambda_C` is independent of the choices of `a` and `f`.
Equivalently, it is the local rational intersection

\[
  (D\cdot C)\pmod{\mathbf Z},
\]

where `D` is the effective representative of `-[C]` constructed above, and
`r(D.C)` means the order of the Cartier equation `h` on the smooth curve.
This convention avoids the sign ambiguity of calling it a self-linking
number. Its denominator, which is the ramification index, is independent
of that sign.

#### Proof

If `f` were a `p`-th power in `Frac(R)` for a prime `p` dividing `r`, its
root would have divisor `(r/p)C`, contradicting exact order `r`. Since the
fraction field contains all roots of unity, Kummer theory shows that
`T^r-f` is irreducible. Thus `[L:Frac(R)]=r`, and `S` is a domain with a
cyclic group of order `r`.

Normalization is finite by excellence. A finite algebra over a complete
local ring is a product of complete local algebras; since `S` is a domain,
it has one factor and is local. Its residue field is `k`.

At each height-one prime `Q`, a local uniformizer has valuation `v_Q(f)`
divisible by `r`. Dividing `T` by the corresponding uniformizer power gives
a root of a unit, whose equation has invertible derivative. Hence the
normalized extension is étale at `Q`. A normal two-dimensional local ring
is regular away from its closed point, and every point of the punctured
spectrum has height at most one; this proves the asserted étaleness.

The same calculation at `C` gives

\[
  \operatorname{div}_S(T)=\pi^*C,
\]

with coefficient one at every prime over `C`. A normal two-dimensional
ring is Cohen--Macaulay. Therefore `S/(T)` is Cohen--Macaulay of dimension
one; it is generically reduced by the coefficient-one calculation. These
facts make it reduced everywhere. Thus `C^#=V(T)` is exactly the reduced
inverse image of `C`.

The finite `R/P`-module `S/(T)` is torsion-free: a nonzero element of `R/P`
vanishes at no generic component of `C^#`, and the Cohen--Macaulay curve
has no embedded associated primes. It is consequently free over the DVR
`k[[t]]`. Its generic rank is `r`, because the cover is étale over the
generic point of `C`.

To calculate its generic algebra, use `a` as the uniformizer at `C` and
set `w=a/T`. Then

\[
  w^r=h.
\]

Reduction at `C` gives

\[
  (S/(T))\otimes_{k[[t]]}k((t))
  \simeq k((t))[w]/(w^r-h_C),\qquad h_C=h\bmod P.
\]

Write `h_C=t^{m_C}u(t)` with `u` a unit. Every unit of `k[[t]]` has an
`r`-th root, by coefficient recursion or Hensel lifting. Replacing `w` by
its quotient by that root reduces the equation to `w^r=t^{m_C}`.

Put `b=gcd(r,m_C)`, `e=r/b`, and `j=m_C/b`. The equation has `b` distinct
irreducible factors over `k((t))`, each of degree `e`; the normalization of
each factor is `k[[s]]` with

\[
  t=s^e,\qquad w=\xi s^j
\]

for a suitable root of unity `xi`. The coprimality `gcd(e,j)=1` proves
irreducibility and total ramification of degree `e`. This includes
`m_C=0`, for which `b=r` and `e=1`.

For independence, replace `a` by another element `a'` of valuation one.
The rational function `a'/a` is a unit of `R_P` and has residue in
`k((t))^*`. Thus the valuation of `h_C` changes by

\[
  r\operatorname{ord}_t((a'/a)\bmod P).
\]

Another generator of `rC` differs from `f` by a unit of `R`; its residue
on `C` has valuation zero. Hence `m_C mod r`, `lambda_C`, `b`, and `e`
are well defined. Finally, the usual local definition of intersection with
a `Q`-Cartier divisor gives `(D.C)=m_C/r`. ∎

### 2. A `D_n` counterexample: local order two, ramification one

For any integer `n>=4`, put

\[
  R_n=k[[x,y,z]]/(x^2+y^2z+z^{n-1}),\qquad C=(x,z).
\]

The curve is the smooth `y`-axis. The hypersurface has an isolated `D_n`
singularity and is normal. At the generic point of `C`, `y` is a unit and
the equation gives valuation two for `z` and valuation one for `x`. There
is no other prime in the support of `z`, since `R_n/(z)=k[[x,y]]/(x^2)`.
Thus

\[
  \operatorname{div}(z)=2C.
\]

The prime ideal `(x,z)` has two minimal generators, so `C` is not Cartier.
Its exact local class order is therefore `r=2`.

The class cover is

\[
  B_n=k[[u,y,t]]/(u^2+y^2+t^{2n-4}),\quad
  x=tu,\quad z=t^2.
\]

It is the normal `A_(2n-5)` hypersurface, with involution

\[
  (u,y,t)\longmapsto(-u,y,-t).
\]

Its invariant ring is `R_n`, and its only fixed point is the origin. The
inverse curve is

\[
  t=0,\qquad u^2+y^2=0.
\]

It has two smooth branches, `u=iy` and `u=-iy`. Each maps isomorphically
to `C` by the coordinate `y`. Consequently

\[
  r=2,\qquad b=2,\qquad e=1.
\]

Theorem 1 gives the same answer directly. Take `a=x` and `f=z`; then

\[
  h=x^2/z=-(y^2+z^{n-2}),\qquad m_C=2.
\]

This also disproves the stronger guess that a smooth finite-index curve
on a hypersurface surface germ forces the surface to be a cyclic quotient
singularity: `D_n` is a counterexample.

### 3. The complete `A`-type family realizes every possible ramification divisor

Fix `N>=2` and `1<=a<N`, and put

\[
  R_N=k[[x,y,z]]/(xy-z^N),\qquad
  C_a=(x-z^a,\ y-z^{N-a}).
\]

The curve is smooth, with parameter `z`. Define

\[
  g=\gcd(N,a),\quad r=N/g,\quad A=a/g.
\]

**Theorem 2.** The exact local class order of `C_a` is `r`. Its cyclic
class cover is

\[
  B_g=k[[U,V,z]]/(UV-z^g),\qquad
  x=U^r,\quad y=V^r,\quad z=z.
\]

Its inverse curve has

\[
  \boxed{b=\gcd(r,g)}
\]

normalized branches, each with ramification index

\[
  \boxed{e=r/\gcd(r,g)}.
\]

The fractional intersection invariant of Theorem 1 is

\[
  \boxed{\lambda_{C_a}=a^2/N\pmod{\mathbf Z}}.
\]

#### Proof of exact order and cover identification

Write the usual cyclic quotient presentation

\[
  R_N=k[[u,v]]^{\mu_N},\quad
  x=u^N,\quad y=v^N,\quad z=uv,
\]

where `zeta` acts by `(u,v)->(zeta u,zeta^{-1}v)`. The invariant-ring
description follows directly by expressing every invariant monomial using
`u^N,v^N,uv`.

The reduced inverse image of `C_a` has equation

\[
  q=u^{N-a}-v^a.
\]

This is reduced in characteristic zero and transforms by the character
`zeta^{-a}`, of exact order `r`. Thus `q^r` is invariant and its downstairs
divisor is `rC_a`.

Conversely, if `ell C_a` were principal, pull a defining equation to the
regular local ring `k[[u,v]]`. Since the quotient map is étale away from
the origin, the pullback has the divisor of `q^ell`. Unique factorization
makes it a unit times `q^ell`. Evaluating that unit at the origin shows
that invariance is possible only when `zeta^{-a ell}=1` for every `zeta`.
Hence `N` divides `a ell`, and `r` divides `ell`. This proves exact order.

The kernel of the character `zeta^{-a}` is `mu_g`. Consequently the field
generated by `q` over `Frac(R_N)` is the `mu_g` invariant field. The
normalization is its invariant ring

\[
  k[[u,v]]^{\mu_g}
  =k[[U,V,z]]/(UV-z^g),\quad U=u^g,\quad V=v^g.
\]

This identifies the class cover without an assumed class-group table.

On this cover, the inverse curve has equation

\[
  q=U^{r-A}-V^A=0.
\]

Over the generic point of `C_a`, `V=z^g/U`, so its algebra is

\[
  k((z))[U]/(U^r-z^a).
\]

The splitting count is `gcd(r,a)`. Since `gcd(r,A)=1`, this equals
`gcd(r,g)`. Kummer normalization gives ramification `r/gcd(r,g)` on each
branch.

To compute the fractional invariant without resolving the singularity,
take the element `s=x-z^a` in place of `a` in Theorem 1. It has valuation
one along `C_a`, and in the quotient presentation

\[
  s=u^a q.
\]

For `f=q^r`, this gives

\[
  h=s^r/f=u^{ar}=x^A.
\]

Restriction to `C_a` yields

\[
  h_C=z^{aA},\qquad m_C=aA=gA^2.
\]

Thus `m_C/r=a^2/N`, and `gcd(r,m_C)=gcd(r,g)` as asserted. ∎

#### Every index--ramification pair occurs

For any `r>=2` and any positive divisor `e` of `r`, put

\[
  b=r/e,\qquad N=rb,\qquad a=b.
\]

Then `g=b`, the curve has exact class order `r`, and its class cover has
`b` branches of ramification index `e`. Therefore **every pair allowed by
`e | r` is realized by a smooth curve on an `A`-type hypersurface**.

In particular, with

\[
  N=r^2,\qquad a=r,
\]

the local class order is arbitrarily large while `e=1`. The cover is the
`A_(r-1)` surface `UV=z^r`; the inverse Cartier curve is

\[
  V=U^{r-1},\qquad U^r=z^r.
\]

It is an ordinary `r`-branch plane curve singularity, and all its
normalized branches map isomorphically to `C_a`.

The smallest instance is already on `A_3`:

\[
  xy=z^4,\quad C=(x-z^2,y-z^2),\quad
  f=x+y-2z^2,\quad\operatorname{div}(f)=2C.
\]

Its class cover is `UV=z^2`, with `f=(U-V)^2`. The inverse curve consists
of `U=V=z` and `U=V=-z`, both unramified over `C`.

### 4. The gluing defect is visible in the discriminant

The preceding examples do not evade the index by making the inverse
Cartier curve smooth. They move the defect into its multiple branches and
their gluing at the closed point.

Let `A_C=S/(T)` in Theorem 1, and let `bar A_C` be its normalization.
Set

\[
  \delta=\dim_k(\bar A_C/A_C).
\]

Both rings are finite free over `k[[t]]`, with rank `r`, and their generic
algebra is étale. The trace discriminant satisfies the exact identity

\[
  \boxed{\operatorname{ord}_t\operatorname{disc}(A_C/k[[t]])
  = r-b+2\delta.}
\]

Indeed, the normalization is a product of `b` tame DVR extensions of
degree `e`; their discriminant orders sum to `b(e-1)=r-b`. Changing a
normalization basis to a basis of `A_C` multiplies the discriminant by
the square of the inclusion determinant. The valuation of that
determinant is `length_(k[[t]])(bar A_C/A_C)=delta`.

For the unramified family `N=r^2,a=r`, the inverse curve
`k[[U,z]]/(U^r-z^r)` has

\[
  b=r,\quad e=1,\quad \delta=r(r-1)/2,
\]

because its `r` smooth branches meet pairwise transversely. Its
discriminant has order `r(r-1)`, equivalently the discriminant of
`U^r-z^r` is a nonzero constant times `z^{r(r-1)}`.

Thus a future global argument may control the arithmetic genus,
discriminant, or gluing defect of the pulled-back Cartier curve. Applying
Riemann--Hurwitz only to its normalization discards the `2delta` term and
cannot bound the local Cartier index.

### 5. Consequences and failure shields for the global structural lane

- A hyperplane class is Cartier locally. Adding a multiple of it to a
  global torsion relation does not itself change local class order or
  supply a primitivity hypothesis.
- For the class cover of `[C]`, local order `r` is a cover degree;
  normalized curve ramification is `e`; branch count is `b`; these obey
  `r=be`. They are different quantities even for a smooth embedded curve.
- If a global cyclic cover of degree `M` restricts at a completed point
  to a class of exact local order `r | M`, its local algebra splits into
  `M/r` copies of the degree-`r` class cover. This follows because units
  of the complete local ring have `M`-th roots. It does not recover
  `e=r` inside each copy.
- For a multiple `q[C]`, both its local order and its curve-restriction
  Kummer character must be recomputed. A cover associated to another
  torsion class is not automatically the cover of `[C]`.
- Smoothness of `C` permits the exact one-variable Kummer formula.
  Smoothness of the normalization of its inverse curve is automatic in
  this local setting and does not make the inverse Cartier curve normal.
- The new formula is degree independent and exact. It gives a structural
  obstruction to a proposed global argument, not a negative STCI theorem.

No research record or other agent's file was edited. The
independent example audit is the companion note linked at the beginning.


---

<a id="2026-10-14-cyclic-cover-d4-counterexample-audit"></a>

## A smooth curve of local class order two whose cyclic cover splits

Date: 2026-10-14.
Author: `duval_counterexample`; independent elementary local audit for
`local_torsion_curve` and `cyclic_cover_structure`.

Status: **NEW PROVED EXAMPLE.** This note checks a new local example only.
Previously accepted global STCI results are premises and have not been
replayed. It gives no counterexample to the global STCI conjecture.

### 1. The surface and smooth curve

Let `k` be algebraically closed of characteristic zero and choose
`i in k` with `i^2=-1`. Put

```
A = k[[x,y,z]] / (x^2 + y^3 + y z^2),
X = Spec A,
C = V(x,y).
```

This is the `D_4` surface singularity. It is a two-dimensional normal
domain: the hypersurface is Cohen--Macaulay, and its gradient vanishes
only at the closed point, so it is regular in codimension one and
normal by Serre's criterion. The equation is irreducible, for example
because `y(y^2+z^2)` has odd valuation at the prime `y` of `k[[y,z]]`
and therefore is not a square in its fraction field. The curve `C` is
smooth, since

```
A/(x,y) = k[[z]].
```

The principal divisor of `y` is

```
div_X(y) = 2 C.
```

Indeed, `A/(y)=k[[x,z]]/(x^2)` has the unique minimal prime `(x,y)`;
at the generic point of `C`, `y^2+z^2` is a unit and the relation
`x^2=-y(y^2+z^2)` gives valuation two for `y`.

The ideal `(x,y)` needs two generators at the closed point. The images
of `x` and `y` are linearly independent modulo `m(x,y)`, since the
hypersurface equation has no linear term. Thus the ideal is not
principal and `C` is not Cartier. On a local normal scheme, triviality
of a Weil divisor class is equivalent to being principal. Consequently

```
order([C] in Cl(A)) = 2.
```

### 2. The normalized class cover

Adjoin a square root `t` of `y` to `Frac(A)`, and put `w=x/t`. The
normalization is

```
B = k[[t,w,z]] / (w^2 + t^4 + z^2),
y = t^2,  x = t w,  z = z.
```

The substitution satisfies the defining equation of `A`. Both new
generators are integral over `A`:

```
t^2=y,  w^2=-(y^2+z^2).
```

Thus `B` is finite over `A`, and its fraction field is
`Frac(A)(sqrt(y))`. The extension has degree two: if `y=g^2` in
`Frac(A)`, then `div(g)=C`; normality implies `g in A`, contradicting
the nonprincipality of `C` just proved.

In coordinates `u=w+i z`, `v=w-i z`, the equation of `B` is

```
u v = -t^4.
```

It is the normal `A_3` surface singularity. Hence this finite normal
ring is exactly the integral closure of `A` in the quadratic extension.
This is the cyclic class cover attached to `[C]`, using the
trivialization `2C=div(y)`.

The deck involution is

```
(t,w,z) |-> (-t,-w,z).
```

Its invariant ring is `A`: it is generated by `z`, `t^2`, `tw`, and
`w^2`, and `w^2=-t^4-z^2` removes the last generator. The fixed locus
has `t=w=0`; the defining equation then forces `z=0` on its support.
The action is therefore free away from the closed point, and the
finite cover is etale there. In particular it is quasi-etale.

### 3. Two inverse branches, each unramified over the curve

The reduced inverse support of `C` is `V(t)`. Its two components are

```
C_+ = V(t,w-i z),
C_- = V(t,w+i z).
```

Each is a smooth formal curve with parameter `z`, and each restriction
to `C` is the identity on `k[[z]]`:

```
C_+ -> C,  C_- -> C
```

are isomorphisms. The involution interchanges the two components. In
particular, the class cover has

```
class order r = 2,
number of inverse branches b = 2,
ramification index of either normalized curve map e = 1 = r/b.
```

Here `e` refers to the maps of normalized curves at the closed point.
It is distinct from divisorial ramification of the surface cover,
which is absent in every quasi-etale class cover.

The scheme-theoretic inverse ideal is `(t w,t^2)` and has reduced
support as above; no claim that this ideal equals `(t)` is needed.

### 4. Consequence and a whole `D_n` family

The assertion that a smooth curve on an isolated normal hypersurface
surface necessarily has ramification index equal to its local class
order on the associated cyclic cover is false. A further local
primitivity condition, such as having a single inverse branch, is
necessary.

The same construction gives a family. For `n>=4`, take

```
A_n = k[[x,y,z]]/(x^2+y^2 z+z^(n-1)),
C_n = V(x,z).
```

Then `div(z)=2C_n`, the ideal `(x,z)` has two minimal generators, and
`C_n` has local class order two. Its class cover is

```
B_n = k[[t,w,y]]/(w^2+y^2+t^(2n-4)),
z=t^2,  x=t w.
```

The cover has type `A_(2n-5)` and inverse branches
`t=0,w=+-i y`, both mapping isomorphically to `C_n`. The same
integrality, normality, fixed-point, and exact-order arguments apply.
This family includes the preceding `D_4` example after interchanging
the roles of `y` and `z`.

The lesson is about local cyclic covers and branch counts. It does
not by itself bound carrier degrees, force conductor torsion, or
settle whether a projective curve is a set-theoretic complete
intersection.

### 5. Independent audit of an arbitrary-order cyclic-quotient family

The parent `local_torsion_curve` independently found the following
stronger family during this audit. The formulas below were independently
derived here and have written elementary proofs; agreement alone is not
the evidence.

Let `N>=2`, `1<=a<N`, and put

```
R = k[[x,y,z]]/(xy-z^N),
C_a = V(x-z^a, y-z^(N-a)),
g = gcd(N,a),  r=N/g.
```

The curve is smooth, with parameter `z`. Write `P=V(x,z)`. One has

```
div(x-z^a)=aP+C_a,
```

so `[C_a]=-a[P]`. The class of `P` has exact order `N`. For an
elementary proof, realize `R` as the invariant subring of `k[[u,v]]`
under

```
(u,v) |-> (zeta u,zeta^(-1) v),
x=u^N,  y=v^N,  z=uv.
```

This quotient is unramified away from the origin. If `jP` is principal,
its pulled-back generator in `k[[u,v]]` has divisor `jV(u)` and hence
is `u^j` times a unit. Invariance and the nonzero constant term of that
unit imply `zeta^j=1`. Thus `N` divides `j`, while `div(x)=NP` gives
the converse. Therefore `C_a` has exact class order `r=N/g`.

The polynomial

```
q=u^(N-a)-v^a
```

is squarefree and cuts out precisely the reduced inverse divisor of
`C_a`. Its character is `zeta^(-a)`, of exact order `r`. The class
cover is consequently the quotient by the kernel `mu_g` of this
character:

```
B = k[[U,V,z]]/(UV-z^g),
U=u^g,  V=v^g,
x=U^r,  y=V^r.
```

Equivalently, `q^r` lies in `R` with divisor `rC_a`, and adjoining its
`r`-th root produces this normalized cover. The cover is connected,
local, normal, cyclic of degree `r`, and etale away from the origin.

At the generic point of `C_a` its inverse algebra is

```
k((z))[U]/(U^r-z^a),  V=z^g/U.
```

Since `k` is algebraically closed of characteristic zero, the equation
has exactly

```
b=gcd(r,a)=gcd(r,g)
```

irreducible factors over `k((z))`. Each factor normalizes to a branch
with ramification index

```
e=r/b.
```

For instance, a branch can be parametrized by `z=s^e`,
`U=c s^(a/b)`, `V=c^(-1)s^((N-a)/b)`; the coprimality of
`e` and `a/b` proves that the normalized branch has degree exactly
`e`. The equality of the two gcd expressions follows from
`gcd(r,a/g)=1`.

Every pair `r>=2`, `e|r` occurs: set `b=r/e`, `N=rb`, and `a=b`.
Then `g=b`, the exact class order is `r`, the branch count is `b`,
and the ramification index is `e`. In particular,

```
N=r^2,  a=r
```

gives arbitrary class order `r` and `r` inverse branches, each mapping
isomorphically to the original smooth curve. The case `N=4,a=2` is
already an `A_3` example of class order two and two unramified branches.

One can also read the ramification directly from a fractional
self-intersection. Take `D=(N-a)P`, which is linearly equivalent to
`C_a`. The equation

```
h=x^((N-a)/g)
```

has divisor `rD` and restricts to `z^(a(N-a)/g)` on `C_a`. Therefore

```
(D.C_a)_p=a(N-a)/N,
e=N/gcd(N,a^2).
```

This is equal to the value `r/gcd(r,g)` found from the class cover.

### 6. The fractional-intersection explanation

Here is the mechanism behind the distinction between class order and
ramification. Let `C` be a smooth curve through the closed point of a
normal complete local surface over `k`, with finite class order `r`.
Choose an effective Weil divisor `D` linearly equivalent to `C` and
not containing `C`. Such a representative exists by choosing a
section of the finite divisorial module `O(C)` whose valuation at the
generic point of `C` is exactly `-1`.

If `div(f)=rC` and `div(h_0)=D-C`, put `h=f h_0^r`. Then
`div(h)=rD`, so `h` is regular on the normal surface and restricts to
a nonzero element of `k[[z]]=O_C`. Write

```
h|_C=z^m epsilon,  epsilon in k[[z]]^*,
(D.C)_p=m/r.
```

The formal unit `epsilon` has an `r`-th root, and the class cover can
equally be constructed by adjoining an `r`-th root of `h`. Its
normalized inverse curve therefore has the same branches as

```
T^r=z^m.
```

Thus its branch count is `gcd(r,m)` and the ramification index of each
branch is `r/gcd(r,m)`, exactly the denominator of `(D.C)_p` in
lowest terms. Changing `D` changes this intersection by an integer,
because the ratio of its two Cartier equations is an `r`-th power
at the generic point of `C`. The denominator is intrinsic.

This argument concerns normalization of the reduced inverse curve;
it does not assume that restriction of the normal surface cover is
itself a normal curve.

For the `D_4` example in sections 1--3, let

```
D_+ = V(x,y-i z),  D_- = V(x,y+i z),
D=D_++D_-.
```

Then `div(x)=C+D`, so `D` is linearly equivalent to `C`, and

```
h=y(x/y)^2=-(y^2+z^2),
h|_C=-z^2,
(D.C)_p=2/2=1.
```

Its denominator is one, explaining the two unramified branches
despite local class order two.

### 7. Signed independent audit of the general theorem and discriminant

Auditor: `duval_counterexample`, 2026-10-14.
Audited source:
[2026-10-14-cyclic-cover-local-smooth-curve.md](#2026-10-14-cyclic-cover-local-smooth-curve),
sections 1 and 4 only. The examples already audited above were not
recomputed. **Verdict: the statements and written proofs are sound under
the source's complete, excellent, normal two-dimensional local
characteristic-zero hypotheses, with algebraically closed residue field
and smooth `R/P=k[[t]]`.**

The decisive steps were checked separately:

1. Exact class order makes the Kummer extension have degree exactly `r`.
   Finite normalization is local because a finite algebra over a complete
   local ring decomposes into local factors and the normalization is a
   domain. At every height-one prime, dividing the root by the appropriate
   uniformizer power leaves a root of a unit, so the extension is etale.

2. The pulled-back divisor of `T` has coefficient one at each prime over
   `C`. Normality in dimension two makes `S` Cohen--Macaulay. Hence
   `S/(T)` is a Cohen--Macaulay curve, generically reduced and consequently
   reduced everywhere. Thus it is the reduced Cartier inverse curve.
   Every generic component dominates `C`; the absence of embedded
   associated primes makes the finite `k[[t]]`-module torsion-free,
   therefore free of generic rank `r`.

3. The residue equation is `w^r=h_C`, where `w=a/T` at the generic point
   of `C`. Extracting the root of its formal unit reduces it to
   `w^r=t^m`. This has `b=gcd(r,m)` factors; each normalization is
   `k[[s]]` with `t=s^(r/b)`. Replacing the numerator uniformizer `a`
   changes `m` by an element of `rZ`; changing `f` multiplies the residue
   by a unit and changes no valuation. Thus the fractional invariant,
   branch count, and ramification index are well defined.

4. The source uses `D=div(a)-C`, whose class is `-[C]`. Section 6 here
   instead used an effective representative of `[C]`. Their fractional
   intersections have opposite signs modulo integers; their denominators
   agree. The source's sign convention is explicit and consistent.

5. For `A_C=S/(T)` and its finite normalization `bar A_C`, both are
   free lattices of rank `r` in the same separable generic algebra.
   The normalized branch discriminants have total valuation
   `b(e-1)=r-b`. If `M` is the inclusion matrix of an `A_C` basis in
   a `bar A_C` basis, its determinant has valuation
   `length_(k[[t]])(bar A_C/A_C)=dim_k(bar A_C/A_C)=delta`.
   Restricting the generic trace pairing multiplies its determinant by
   `det(M)^2`. Therefore the exact identity is

   ```
   ord_t disc(A_C/k[[t]]) = r-b+2 delta.
   ```

No gap was found in these two new results. This audit is a proof audit,
not computational evidence and not a claim of mathematical novelty.


---

<a id="2026-10-14-normal-cyclic-cover-torsion-detection"></a>

## Torsion detected on an ample smooth rational curve

Date: 2026-10-14.
Author: `cyclic_cover_structure`, independently checking a proposal from
`conductor_general` and the root research agent. Local counterexample and
local Kummer refinement: `local_torsion_curve`.

Status: **NEW PROOF WRITTEN HERE.** Accepted repository results are premises,
not recomputed. No novelty claim is made. This note concerns normal carriers;
it does not eliminate all normal carriers or resolve the universal STCI
problem.

### 1. An intrinsic torsion-detection theorem

Let `X` be a normal integral projective surface over an algebraically closed
field `k`. Let `C` be a smooth rational prime curve. Assume that some positive
multiple `M C` is an ample effective Cartier divisor. In characteristic `p>0`,
only torsion of order prime to `p` is considered in this section. There is no
restriction on torsion orders in characteristic zero.

**Theorem.** A torsion Weil class `T` which is Cartier at every point of `C`
is zero in `Cl(X)`. Consequently the restriction homomorphism

```
Cl(X)_tors -> product_{P in C intersect Sing(X)} Cl(O_{X,P})
```

is injective (on prime-to-`p` torsion in characteristic `p`). If `T` has exact
order `t`, then

```
t = lcm_{P in C intersect Sing(X)} order(T_P).
```

The empty least common multiple is one. In particular this theorem detects
torsion at singularities **on `C`**, independently of singularities elsewhere
on the surface. It does not assert that `Cl(X)` is torsion-free.

#### Proof of the cyclic-cover construction

Choose a Weil divisor representing `T`, write `t T=div(phi)`, and form the
usual cyclic reflexive algebra

```
A = direct_sum_{i=0}^{t-1} O_X(iT),
```

where multiplication crossing degree `t` uses the isomorphism
`O_X(tT)->O_X`, `f -> f phi`. Generically this is the Kummer algebra
`k(X)[z]/(z^t-phi)`.

The generic algebra is a field by the Kummer irreducibility argument in the
[connected cyclic-cover proof](../carriers/normal_carrier_symbolic_torsion.md#proof-by-a-connected-cyclic-cover).

The relative spectrum `Y=Spec_X A` is finite, integral and projective. It is
normal: every summand is reflexive, hence has depth two at the closed points
of the normal surface; the finite algebra is therefore `S2`. At every
codimension-one point of `X`, `T` is Cartier, and its cyclic algebra is
finite etale because `t` is invertible. Thus `Y` is regular in codimension
one, and the `R1+S2` criterion applies. These facts can also be obtained by
normalizing `X` in the Kummer field; the displayed reflexive algebra is that
normalization. The cover has cyclic group `mu_t` and is etale outside the
non-Cartier locus of `T`, a finite set. Its reflexive pullback of `O_X(T)`
is trivial.

These precise construction statements agree with Ambro, *Cyclic covers and
toroidal embeddings*, Section 4, Lemmas 4.1--4.2, [primary paper
PDF](https://arxiv.org/pdf/1310.3951). Etaleness near the Cartier locus here
is established directly by the local equation `w^t=unit`; the proof does
not use an assertion of etaleness at arbitrary non-Cartier singular points.

#### Proof of the torsion-detection assertion

The [connected cyclic-cover proof](../carriers/normal_carrier_symbolic_torsion.md#proof-by-a-connected-cyclic-cover)
uses étaleness near `C` and Riemann–Hurwitz to split the inverse image of the
rational curve into `t` components. Ampleness forces the support of the pulled
back Cartier divisor to be connected, so `t=1`. Applying this to the least
common multiple of the local orders times `T` gives the exact order formula.

The same proof works for a proper connected reduced curve `C` with no
nontrivial connected finite étale covers, provided an ample effective
Cartier divisor has support `C`. The cover restricted to `C` is then a
disjoint union of copies of `C`, and the same ample-support argument
forces degree one.

### 2. Exact normal-carrier formula for the quartic

Let `X subset P3` be a normal integral degree-`a` hypersurface in
characteristic zero, containing the accepted smooth rational quartic
`C0`. Put `H=O_X(1)` and

```
g = gcd(a,4),  r = a/g,  s = 4/g,
Delta_0 = r[C0] - s[H].
```

Assume `Delta_0` is torsion of exact order `t`. This is the primitive
class of a hypothetical mate; it gives the accepted first relation

```
m C0 ~ b H,  m = t r,  b = t s.
```

In particular `m C0` is ample Cartier, so the theorem applies. For each
`P in C0 intersect Sing(X)`, let `n_P` denote the exact local Cartier
index of `C0`, that is, the order of `[C0]` in `Cl(O_{X,P})`.
It is finite because `m C0` is Cartier. The hyperplane class is locally
principal, whence `Delta_{0,P}=r[C0]_P` has order

```
k_P = n_P/gcd(n_P,r).
```

Therefore

```
t = lcm_P k_P,
b_min = (4/g) lcm_P [n_P/gcd(n_P,a/g)].
```

For a normal carrier there is no normalization-conductor exponent.
The accepted primitive-ray theorem therefore says that all mate degrees
on this carrier are exactly the positive multiples of `b_min`.

This is a **conditional exact formula**, not a converse based only on
local indices. Finite local indices alone do not imply that
`Delta_0` is torsion: after local Cartier defects are removed, an
infinite-order global Cartier class can remain.

Accepted exclusion of all mates of degree at most four now implies the
necessary condition

```
(4/g) lcm_P k_P >= 5.
```

Thus the following whole normal-carrier classes are excluded at once:

* carriers for which `C0` avoids `Sing(X)`;
* carriers for which every `n_P` divides `a/g`;
* more generally, carriers for which `(4/g) lcm_P k_P <= 4`.

The possible torsion orders are consequently constrained uniformly:

```
g=1: t>=2;  g=2: t>=3;  g=4: t>=5.
```

These are necessary conditions on a hypothetical mate, not an exhaustive
carrier classification. No bound on `a`, on the local indices, or on
their least common multiple has been proved here.

### 3. Failure shield: local order is not curve ramification

A local cyclic class cover can have several branches over a smooth
curve, meeting above the surface singularity. Normalizing those branches
can remove the meeting and lose information needed for the connectedness
argument. In particular a local class order cannot simply be substituted
as a ramification index in Riemann--Hurwitz.

An explicit characteristic-zero example is

```
R = k[[x,y,z]]/(x^2 + z y^2 + z^3),
C = V(x,z).
```

This is a normal isolated hypersurface singularity and `C` is the smooth
`y`-axis. One has `div_R(z)=2C`; the ideal `(x,z)` is not principal at
the origin (its two generators remain independent modulo the maximal
ideal times the ideal). Thus `[C]` has exact local order two.

Adjoining `t` with `t^2=z` and setting `u=x/t` gives the normal cyclic
cover

```
B = k[[u,y,t]]/(u^2+y^2+t^4),
x=t u,  z=t^2.
```

The involution is `(u,y,t)->(-u,y,-t)`, and its invariant ring is `R`.
Its only fixed point is the origin, so the cover is etale outside that
point. The reduced inverse image of `C` is

```
t=0,  u= i y   union   t=0,  u=-i y.
```

It has two branches meeting at the origin. Each normalized branch maps
isomorphically to `C`; its ramification index is one, although the local
class order is two. This example is local and does not assert that this
configuration occurs on a global quartic carrier with a mate. It rules
out the general local equality needed for that shortcut.

There are examples with **arbitrarily large** local class order and
normalized-curve ramification one, even among `A`-type hypersurface
singularities. Let

```
R_N = k[[x,y,z]]/(xy-z^N),
C_a: x=z^a, y=z^(N-a),  1<=a<N.
```

This curve is smooth because its local ring is `k[[z]]`. Write

```
g0=gcd(N,a),  n=N/g0.
```

The cyclic quotient presentation of `R_N` is the invariant ring of
`k[[u,v]]` under `mu_N` acting with weights `(1,-1)`, where
`x=u^N`, `y=v^N`, `z=uv`. The reduced inverse curve is cut out by

```
q=u^(N-a)-v^a.
```

Its semi-invariant character has weight `-a` and exact order `n`.
Consequently `[C_a]` has exact order `n`. To see the exactness without
assuming a class-group classification, `q^n` is invariant and has
divisor `n C_a` downstairs. If a rational function downstairs had
divisor `j C_a`, its pullback would be `q^j` times a unit upstairs.
This unit is semi-invariant; its nonzero constant term forces its
character to be trivial. Hence `N` divides `a j`, so `n` divides `j`.

The class cover is the quotient by the kernel `mu_{g0}` of this
character. It is

```
B = k[[U,V,z]]/(UV-z^g0),
x=U^n, y=V^n.
```

On the generic point of the curve its algebra is `U^n=z^a`. Thus there
are `gcd(n,a)=gcd(n,g0)` normalized branches, each having ramification
index `n/gcd(n,a)`. Given **any** `n>=2` and any `e` dividing `n`,
take `b=n/e`, `N=n b`, and `a=b`. Then the local class order is `n`,
the number of branches is `b`, and every branch has ramification `e`.
In particular `N=n^2,a=n` gives `n` smooth branches mapping
isomorphically to `C_a`. They meet above the surface singularity.

This family proves that local Cartier indices cannot be bounded using
the normalized-curve ramification alone. It does not produce global
fixed-degree hypersurface carriers with unbounded indices.

The independent local Kummer calculation is recorded in
`2026-10-14-cyclic-cover-local-smooth-curve.md`: if `div(f)=nC`, choose
`a` with `v_C(a)=1`, and let `h=a^n/f`. Then `h` is regular, nonzero
on the generic point of `C`, and if `ell` is the order of `h|_C` at
the closed point in the smooth curve parameter, the full local class
cover has

```
gcd(n,ell) normalized branches,
ramification index n/gcd(n,ell) on each branch.
```

The residue class `ell mod n` is independent of the choices. The
ramification invariant is the fractional local intersection class
`ell/n mod Z`; it can be zero for a nontrivial divisor class.

### 4. A conditional global budget retaining the gluing

This additional calculation was independently audited by
`local_torsion_curve`. Retain the normal quartic-carrier setup of section 2
and its degree-`t` cyclic cover `pi:Y->X`. Put `H_Y=pi^*H` and let `D` be
the **reduced** inverse curve. Impose the extra hypothesis that `D` is
Cartier. The primitive relation alone does not imply this hypothesis.

The cover is etale in codimension one. Since the base hypersurface is
Gorenstein, the reflexive dualizing sheaf on `Y` agrees away from
codimension two with `pi^*omega_X` and hence agrees with it everywhere.
Thus `Y` is Gorenstein and

```
K_Y=(a-4) H_Y,  H_Y^2=t a,  H_Y.D=4t,
r D ~ s H_Y,  D^2=16t/a.
```

Adjunction to the Cartier curve gives

```
p_a(D)=1+2t(a-4)+8t/a.
```

Let `R` be the total Riemann--Hurwitz ramification of all components of
the normalization of `D` over `C0=P1`, and let `delta` be the sum of the
local delta invariants of `D`. Their total covering degree is `t`.
The normalization exact sequence and Riemann--Hurwitz, allowing
disconnected normalization, give

```
p_a(D)=1-t+R/2+delta.
```

Consequently

```
delta+R/2 = t(2a-7+8/a),
a divides 8t.
```

The finite map `D->P1` is flat because the reduced Cartier curve is
Cohen--Macaulay and has no component mapped to a point. Its trace
discriminant has degree

```
R+2delta = 2t(2a-7+8/a).
```

This is the global budget which a ramification-only argument omits. It
is a structural formula, not yet a contradiction. For example the
unramified local `A_(n^2-1)` family has the ordinary `n`-fold point
`U^n=z^n` as inverse curve, with `delta=n(n-1)/2`. If the local class
of `Delta_0` generates this order-`n` local class of `C0`, the global
degree-`t` cover has `t/n` such local copies. Their combined contribution
gives the necessary bound

```
n-1 <= 2(2a-7+8/a).
```

This bound is uniform in the mate degree **within the stated local
singularity stratum and the extra Cartier-inverse hypothesis**. It does
not bound arbitrary local indices on arbitrary carriers. Obtaining an
analogue with the residual non-Cartier inverse curve is an open next step.

### 5. What this proves and what remains

The new degree-independent gain is exact localization of the global
torsion obstruction to the finite singular set on the hypothetical
ample rational support. Normal-carrier searches can organize themselves
by those local indices rather than by separate mate degrees. The proof
also applies to arbitrary smooth rational curves with an ample Cartier
multiple and to prime-to-characteristic torsion in positive
characteristic.

The unresolved step is to bound or eliminate the allowable local indices
for **all** normal hypersurface carriers of `C0`, while retaining the
global primitive relation. The local cover may have singularities and a
singular, reducible inverse image of `C0`; its normalization need not be
rationally connected or yield a Hurwitz contradiction. Finite local
indices are necessary but do not certify the global relation. No
statement here covers nonnormal or entirely thick carriers.

For comparison, a separate standard hypersurface route uses the
simple-connectedness of a complex projective hypersurface, stated in
Maxim, *On the topology of complex projective hypersurfaces*, Proposition
2.6, [primary author PDF](https://people.math.wisc.edu/~maxim/hyp_survey.pdf),
and the local class-group exact sequence. The proof above is stronger in
its geometric scope and is self-contained apart from standard Kummer
theory, Serre's normality criterion, Serre duality, and Serre vanishing.



---

<a id="2026-10-14-moving-linear-cubic-compatibility"></a>

## Degree-one moving linear relations: the cubic obstruction

Date: 2026-10-14. Status: new exact cubic calculation, independently accepted in the
[sign/frame audit](#2026-10-14-moving-linear-cubic-independent-audit). The accepted embedded chart and the independently established
quadratic obstruction locus are premises; neither is re-audited here.

The calculation below eliminates the nonquadric members of the quadratic
obstruction-zero locus. Precisely, among basepoint-free moving linear relation
lines `O(-8) -> N_C0^*=O(-7)^2`, the only line admitting a compatible relation
through cubic normal degree is the line of the actual quadric. This is a
classification of the specified relation-lifting problem. A relation with
torsion or poles, a first relation of higher order, and an additional relation
in the relevant degree are separate problems.

### 1. Accepted inputs and the next target

Use the frames and coefficients from the [independent quadratic
audit](#source-2026-10-14-moving-linear-quadratic-obstruction-independent-auditmd):

    a=A+Cz, b=B+Dz, Delta=AD-BC != 0,
    f0=a u+b v,
    f1=(Aw+C)u'+(Bw+D)v'.

The relation line is `W=O(-8)` and its quotient is `M=O(-6)`. The quotient is
normalized by `(u,v) -> (b,-a)q`; on the other chart its frame is
`q1=z^-6 q0`. The next relation obstruction therefore lies in

    Hom(W,Sym^3 M)=O(-10).

In the chart-zero frame, its Cech class retains exactly the coefficients of
`z^-1,...,z^-9`. Nonnegative exponents and exponents at most `-10` are
coboundaries. There is no extra power of `z` after evaluating a cubic expression
at `(u,v)=(b,-a)`.

The accepted quadratic class vanishes precisely at the three diagonal points

    [A:B:C:D]=[t:0:0:1],
    (t-2)(3t^2-4t+12)=0,

and on the open conic

    A=2D, BC=8D^2, D!=0.

The conic is normalized below by `D=1, B=t, C=8/t`, with `t!=0`.

### 2. Canonical quadratic correction and the unit term

Let `T` be the accepted quadratic discrepancy evaluated at `(b,-a)`. On its
obstruction-zero locus, split it uniquely as

    T=T_plus+T_minus,
    supp(T_plus) contained in {0,1,...},
    supp(T_minus) contained in {...,-5,-4}.

There is no remaining quotient-level quadratic lifting freedom because
`H^0(O(-4))=0`. Define

    ell0=(-C u-D v)/Delta,
    ell1=(A u'+B v')/Delta,
    q0=T_plus,
    q1(w)=-z^4 T_minus(z),
    F0=f0+q0 ell0^2,
    F1=f1+q1(w)ell1^2.

On the reduced curve, `ell0(b,-a)=1`. On the other chart the corresponding
evaluation is `ell1=z^-6` in the first quotient frame. Consequently the
quadratic part of `z^8 F1-F0` evaluates to zero. The coefficient pair `(a,b)`
is unimodular, so this part is exactly divisible by the relation:

    [z^8 F1-F0]_2=f0 L2,

where `L2` has normal degree one. The degree-one term of the unit comparing
the two local generators is thus `L2`. Its contribution in degree three is
`L2 q0 ell0^2`. The evaluated cubic remainder is

    R=[z^8 F1-F0]_3(b,-a)-q0 L2(b,-a).

Local additions to either quadratic correction that are multiples of `f`
change the local generator by a unit. They change the cubic calculation by
the corresponding unit contribution and a cubic coboundary. Thus they do not
introduce another compatibility parameter. The unspecified degree-two term
of the comparison unit multiplies `f0` and vanishes in the quotient.

### 3. Exact chart calculation

The accepted chart is expanded only through normal degree three:

    b_orig=u+(3/2)zv, a_orig=v,
    inv=(z^4+b_orig)^-1,
    W=(z^3+v)inv,
    a'=z inv-W^3,
    b'=inv-W^4,
    u'=a'/2,
    v'=-3W a'+2b'.

In the second-chart corrections above, the coefficient variable `w` is
substituted by the actual `W`, including its normal terms. In particular,
the derivative of `q1(w)` is retained. The source uses the exact finite series

    inv=sum_(j=0)^3 (-b_orig)^j z^(-4j-4) modulo (u,v)^4.

All arithmetic uses `fractions.Fraction`, sparse Laurent polynomials in `t,z`,
and truncation only in the normal variables `u,v`. There is no sampling,
floating-point calculation, or generic-parameter saturation. The two nonreal
diagonal points are handled together in the exact field
`Q[t]/(3t^2-4t+12)`; negative powers of `t` use
`t^-1=1/3-t/4` there.

At the accepted quadric point `t=2`, both quadratic corrections vanish and

    L2(b,-a)=4 z^-3,
    [R]=0 in H^1(O(-10)).

The actual quadric equation is an accepted all-orders lift.

At either other diagonal point,

    q0=q1=0,
    L2(b,-a)=(2t-4)z^-3,
    [R]=(64/27)(3-t)z^-5.

Since `3t^2-4t+12` has value `27` at `t=3`, this cohomology class is nonzero
at both points. Thus neither diagonal relation extends compatibly through
cubic normal degree.

On the entire open conic, the exact corrections are

    q0=-96/t^2-192z/t^3,
    q1(w)=-6t^2-3t^3 w.

The comparison-unit evaluation is

    L2(b,-a)=64/t^3+16z^-1/t^2+20z^-2/t+4z^-3
                 -3t z^-4+t^2 z^-5+t^3 z^-6.

Its cubic class is exactly

    [R]=512z^-1/t^4-384z^-2/t^3+64z^-3/t^2
           +4t^2 z^-7-6t^3 z^-8+2t^4 z^-9.

The `z^-1` coefficient is nonzero for every allowed `t`. Hence no member of
the open conic extends through cubic normal degree. The points in the conic's
closure with `D=0` have `Delta=0`, so they are outside the basepoint-free
degree-one relation problem and are not discarded by a saturation here.

### 4. Conclusion and scope

The complete basepoint-free degree-one quadratic zero locus has now been
tested in the next normal degree. Only the actual quadric relation survives.
Equivalently, a primitive length-four structure on `C0` with a single
compatible relation line `O(-8)` and quotient conormal `O(-6)` must use the
quadric relation line. This statement fixes the line, not an arbitrary
higher-order thickening or an STCI presentation.

For a moving linear relation of movement degree `e`, the cubic target is
generally `O(4e-14)`. The new calculation concerns `e=1`; it does not exclude
`e=2` or `e=3`, whose cubic cohomology can still be nonzero, or `e>=4`, for
which this particular cohomology group vanishes. It also does not justify
taking an `r`th root of a higher-order pure-power first relation.

A useful further consequence concerns an actual primitive length-four
structure `Y` with this first quotient conormal, rather than a formal relation
alone. The relation's quotient-level corrections in degrees two and three
are unique once they exist: the differences of two compatible lifts are
sections of `Hom(W,Sym^j M)=O(8-6j)`, which have no global sections for
`j=2,3`. Multiples of the relation merely change its local generators.
Therefore the compatible ideal of `Y` modulo `I_C0^4` agrees with that of
the accepted actual quadric, and its quadric equation lies in `I_Y`.

In particular, if `Y` is the full symbolic length-four structure on an
integral normal degree-eight carrier, then the quadric section vanishes to
order at least four along `C0`. Its complete-intersection cycle has degree
`2*8=4*4`. There is no residual curve and no isolated component, because the
ambient complete intersection is pure. The quadric and that carrier would
have set-theoretic intersection `C0`, contradicting the accepted low-carrier
exclusion. Thus a normal degree-eight carrier cannot have an everywhere
primitive symbolic quadruple with free conormal `O(-6)`. This uses the full
symbolic quadruple hypothesis, not merely its generic first symbol.

The [coefficient calculation](../../computations/moving_linear_cubic_compatibility_2026_10_14.py)
reproduced the [full coefficient output](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/validation/2026-10-14-moving-linear-cubic/cubic-results.json) byte for byte, including the discrepancy and obstruction on all three
strata. Run `python3 research/computations/moving_linear_cubic_compatibility_2026_10_14.py`
from the repository root to regenerate it.


---

<a id="2026-10-14-moving-linear-cubic-independent-audit"></a>

## Independent audit of the degree-one moving linear cubic obstruction

Date: 2026-10-14. Status: **PASS**, exact independent derivation of the new
cubic calculation. The accepted embedded chart and [quadratic
audit](#source-2026-10-14-moving-linear-quadratic-obstruction-independent-auditmd)
are premises. Their earlier computations were not re-audited. The owner's
[cubic note](#2026-10-14-moving-linear-cubic-compatibility) was first read
after this audit's separate expansion had produced its answer.

### 1. Frame and correction signs

Write `W=O(-8)`, `M=O(-6)`,

    a=A+Cz, b=B+Dz, Delta=AD-BC != 0,
    f0=a u+b v,
    f1=(Aw+C)u'+(Bw+D)v'.

On the reduced overlap the quotient frame transforms by `q1=z^-6 q0`,
whereas the relation frame transforms by `W1=z^-8 W0`. Consequently the
cubic target is `Hom(W,Sym^3 M)=O(-10)`. Its first-chart coefficient is
obtained by evaluating at `(u,v)=(b,-a)`, with no additional factor of `z`.
Exactly `z^-1,...,z^-9` survive in its Cech cohomology; exponents at least
zero and at most `-10` are coboundaries.

Let `T` denote the accepted evaluated quadratic discrepancy. On its zero
locus write `T=T_plus+T_minus`, with exponent supports at least zero and
at most `-4`, respectively. Set

    ell0=(-C u-D v)/Delta,
    ell1=(A u'+B v')/Delta,
    q0=T_plus,
    q1(w)=-z^4 T_minus(z),
    F0=f0+q0 ell0^2,
    F1=f1+q1(w)ell1^2.

The quotient evaluations are `ell0=1` and `ell1=z^-6`. Thus the second
degree quotient discrepancy is `T+z^-4 q1-q0=0`; this fixes both correction
signs. The remaining second-degree expression is `f0 L2`. The gluing unit
therefore has first normal term `L2`, and

    z^8 F1=(1+L2+L3)F0 modulo normal degree four.

After evaluating in the quotient, the third-degree remainder is precisely

    R=[z^8 F1-F0]_3(b,-a)-q0 L2(b,-a).

The minus sign comes from the third-degree product `L2 q0 ell0^2`.
The term `L3 f0` vanishes in the quotient.

### 2. Independent expansion method and exact output

The independent source changes normal variables before expanding:

    u=b e+(D/Delta) h,
    v=-a e-(C/Delta) h.

Then `f0=h` and `ell0=e` exactly. In particular the coefficient of `e h`
in the second-degree overlap is directly `L2(b,-a)`. This avoids copying
the owner's binary-polynomial division or cubic output.

Put `p=u+(3/2)zv` and `k=u+(1/2)zv`. Direct expansion of the exact embedded
chart gives the new third-degree terms

    [u']_3=(1/2)z^-15(-p^3+3p^2k+6pk^2+k^3),
    [v']_3=z^-16(p^3+5p^2k-12pk^2-4k^3).

The second-chart base coordinate is the actual
`W=(z^3+v)/(z^4+p)`. Its normal terms are retained in the coefficients
of `f1` and `q1(W)`. In particular, the normal derivative of `q1` contributes
to degree three. Expanding the inverse through degree three is exact modulo
`(e,h)^4`; all arithmetic is over rational Laurent polynomials in the
indeterminate parameters `z,t`.

For the diagonal `A=t,B=C=0,D=1`, the accepted quadratic-zero condition is
`(t-2)(3t^2-4t+12)=0`. Both local quadratic corrections are zero. The raw
cubic quotient is

    R=(-10+22t-16t^2+(13/2)t^3-(11/8)t^4)z^-5.

At `t=2` it vanishes. In the exact field `Q[t]/(3t^2-4t+12)` it is

    R=(64/27)(3-t)z^-5.

This is nonzero at both nonquadric diagonal points, since the quadratic
has value `27` at `t=3`. The comparison unit at those points evaluates to
`(2t-4)z^-3`; at the quadric point it evaluates to `4z^-3`.

On the open conic `A=2,B=t,C=8/t,D=1`, with `t!=0`, the exact local
quadratic corrections are

    q0=-96/t^2-192z/t^3,
    q1(w)=-6t^2-3t^3 w.

The independently computed comparison unit is

    L2(b,-a)=t^3z^-6+t^2z^-5-3tz^-4+4z^-3
              +20t^-1z^-2+16t^-2z^-1+64t^-3.

After the required subtraction, the complete cubic quotient is

    R=3t^6z^-11+9t^5z^-10+2t^4z^-9-6t^3z^-8+4t^2z^-7
       +64t^-2z^-3-384t^-3z^-2+512t^-4z^-1
       +9216t^-5+12288t^-6z.

Its retained cohomology class is therefore

    [R]=2t^4z^-9-6t^3z^-8+4t^2z^-7
         +64t^-2z^-3-384t^-3z^-2+512t^-4z^-1.

The `z^-1` coefficient is nonzero at every allowed point. These are
identities over the parameter Laurent ring, not tests at finitely many
parameters. They agree with the owner's calculation term for term.

### 3. Lifting freedom and primitive length-four scope

Two quotient-level quadratic lifts of the same leading line differ by a
global section of `Hom(W,Sym^2 M)=O(-4)`, whose `H^0` is zero. Thus the
quadratic correction is unique modulo changes of the local relation
generator by units. Adding `f P` in local normal degree two is such a unit
change to that order. Its induced degree-three product is a local correction,
so the corresponding change of the cubic remainder is a Cech coboundary.
The unrestricted degree-two part of a comparison unit multiplies `f0` and
vanishes in the quotient. Hence no extra quadratic parameter or unit
parameter can remove a nonzero class above. Local cubic corrections remove
exactly the displayed cubic coboundaries.

A primitive curvilinear structure of length four has `I_C^4` in its ideal,
and locally its ideal modulo `I_C^4` is generated by its first relation.
There is no independent initial relation in normal degrees one, two, or
three. Its local first-relation generators must therefore pass this cubic
compatibility problem. The owner's conclusion is valid: with the specified
line `O(-8)` and quotient conormal `O(-6)`, its line must be the actual
quadric line. The calculation does not apply when torsion or poles are
allowed, or when another independent relation enters in the relevant
degree. It does not take a root of a higher-order pure-power relation and
does not assert an STCI exclusion on its own.

The independent [source](https://github.com/markluxton1/STCI/blob/88f2e4f6a418cad6f584a1ce2445787caf653f3a/research/computations/moving_linear_cubic_independent_audit_2026_10_14.py) preserves the derivation and its exact field reductions.


---

<a id="2026-10-14-moving-linear-ideal-rigidity-independent-audit"></a>

## Degree-one moving linear relations: ideal rigidity and a carrier consequence

Date: 2026-10-14. Status: independent geometric audit conditional only on the
new cubic classification's recorded exact coefficient verification. This
note does not repeat the accepted quadric or constant-direction calculations.

Use the [quadratic frame review](#source-2026-10-14-moving-linear-quadratic-obstruction-independent-auditmd)
and [new cubic classification](#2026-10-14-moving-linear-cubic-compatibility).
They identify the unique compatible basepoint-free moving linear relation
line `W=O(-8)` through normal degree three as the line of the actual quadric
`q=u+(z/2)v`. Its quotient conormal is `M=O(-6)`.

### 1. Finite principal ideals with a fixed relation line

Let `C` be a smooth curve in a smooth threefold, with conormal bundle `E`.
Fix a subline `W` in `E` whose quotient `M=E/W` is a line bundle. Consider
coherent ideals modulo `I_C^N` locally generated by one normal-order-one
relation with this leading subline. Such ideals include `I_C^N` by
definition; their associated initial ideal is generated by `W` in each
order below `N`.

Suppose two such ideals agree through normal degree `j-1`. Locally choose
their generators to agree to that order, using multiplication by units.
Their degree-`j` difference is a local section of

    Hom(W, Sym^j E / (W tensor Sym^(j-1)E))
       =Hom(W,M^j).

Compatibility of the two ideals makes these local differences a single
global section of `Hom(W,M^j)`. If that space of global sections is zero,
the differences are multiples of the common leading relation and can be
removed by multiplying the local generators by units of normal degree
`j-1`. The ideals then agree through degree `j`.

Thus a compatible finite principal ideal with fixed `W` is unique if

    H^0(Hom(W,M^j))=0 for 2<=j<N.

This is uniqueness of ideals. It does not choose a distinguished local
generator; generator units are exactly the harmless differences removed
in the argument.

### 2. The quadric direction is rigid at every finite length

For `C0`, `W=O(-8)` and `M=O(-6)` give

    Hom(W,M^j)=O(8-6j).

All these spaces of global sections vanish for `j>=2`. The actual quadric
supplies a compatible principal ideal at every finite order. Therefore,
once the degree-one moving relation has survived the cubic obstruction,
every finite principal ideal with that line equals

    (q)+I_C^N

as an ideal on the `N`th ambient infinitesimal neighborhood of `C`.
In particular, every primitive length-`N` structure with quotient
conormal `O(-6)`, for `N>=4`, is scheme-theoretically contained in the
actual quadric. Here primitive means that locally it has the form
`(f,t^N)` in smooth ambient coordinates, with `C=(f,t)`; this hypothesis
implies `I_C^N` is already contained in its ideal. Its ideal modulo
`I_C^N` is precisely of the principal form used above.

No claim is made about higher-order pure-power relations, nonsaturated
first relations, torsion in the first normal quotient, or a second
independent relation before normal degree four.

### 3. Consequence for a normal carrier

Let `F` be an integral hypersurface of degree `a` containing `C0`, and
assume its entire symbolic multiple `C_N` is a primitive length-`N`
structure with quotient conormal `O(-6)`, where `N>=4`. The rigidity result
gives `q in I_(C_N)`. If `F` is normal, this says that the effective Weil
divisor of the quadric restriction satisfies

    div_F(q) >= N C0.

If `F` differs from the quadric, `q` is nonzero on `F`, and intersecting
with the hyperplane class gives

    2a >= 4N,  hence N<=a/2.

In the equality case `N=a/2`, the residual effective Weil divisor has
degree zero and therefore vanishes. Hence the support of `F intersect Q`
is exactly `C0`: the actual quadric is a mate. This contradicts the
accepted low-degree-carrier exclusion for `C0` in characteristic zero.

Consequently such a normal carrier must satisfy the strict inequality

    N<a/2.

For `a=8`, even a primitive symbolic quadruple with conormal `O(-6)` is
therefore impossible. This conclusion requires the entire symbolic
quadruple to be primitive, not just generic curvilinearity or first
conormal freeness at selected points. It applies in every carrier degree
with the stated structure and makes no assertion about unbounded local
index strata lacking that structure.

### 4. Verification and boundary

The finite ideal uniqueness proof, inclusion of `I_C^N` for a primitive
multiple, and the divisor-degree consequence have been independently
checked geometrically. The new cubic classification supplies the actual
quadric direction; its exact source and coefficient record are linked in
the owner note. Existing low-degree exclusions are premises, not rerun
computations. This is a structural reduction with explicit hypotheses,
not a solution of the universal STCI question.


---

<a id="2026-10-14-quadric-opposite-ruling-phase-family-failure"></a>

## A global opposite-ruling phase family always has extra inverse points

Date: 2026-10-14. Owner: `quadric_global_phase_geometry`, for
`projection_conductor_ray/quadric_phase_review`.
Status: **EXACT FAILURE SHIELD FOR THE DISPLAYED FAMILY ONLY**.

Let `S=P1 x P1`, with affine coordinates `(x,y)`, diagonal `c:y=x`,
and polarization `H=(2,2)`. For `a!=0,-1` and arbitrary `u`,
homogenize the following four polynomials to bidegree `(2,2)`:

    U0=1,
    U1=(a x+y)/(a+1),
    U2=a^2 x^2+y^2-(a^2+1)xy+u x^2y+(1-u)xy^2,
    U3=x^2y^2.

On the diagonal their restriction is `[1:t:t^3:t^4]`, the literal
fixed C0. On the opposite rulings through `(0,0)`, the points
`(s,0)` and `(0,a s)` have the same projective image. The section
`Q=(y-x)^2` has respective values `s^2` and `a^2 s^2`, so this
branchwise phase is the arbitrary constant `a^{-2}`.

The four sections have no common zero. On the finite chart this
follows from `U0=1`. On the boundary `x=Infinity`, they reduce to

    [0:0:a^2 y0^2+u y0 y1:y1^2],

and on `y=Infinity` they reduce to

    [0:0:x0^2+(1-u)x0 x1:x1^2].

In each case the last two entries have no common zero; at
`(Infinity,Infinity)` the last entry is nonzero. The resulting
morphism is finite because its pulled-back polarization is ample.

However, its entire inverse image of C0 always includes a point
outside the diagonal. If `u!=0`, the point

    (x,y)=(Infinity,-a^2/u)

maps to `[0:0:0:1]`. If `u!=1`, the point

    (x,y)=(-1/(1-u),Infinity)

maps to the same endpoint. Both displayed finite coordinates are
nonzero, so these are actual boundary points outside `c`.
At least one exists for every `u`: avoiding both would require
simultaneously `u=0` and `u=1`.

Therefore this family never satisfies the full inverse-image
support condition `nu^{-1}(C0)_red=c`. In particular it supplies
no global fixed-C0 mate-admitting carrier and no counterexample to
the accepted projective frontier. The argument does not require
birationality and places no restriction on the order of `a^{-2}`.

It also does not exclude general opposite-ruling pairs. The
[complete coefficient normal form](../carriers/carrier_conductor_differential_comparison.md#the-opposite-ruling-pairing-and-its-complete-coefficient-freedom)
contains arbitrary vectors `D,E in k^4` in place of the restricted
choice `D=W2,E=u W2`; those coefficients can remove this particular
boundary obstruction. No general phase-order bound or full
four-section family exclusion follows from this calculation.


---

<a id="source-2026-10-14-moving-linear-quadratic-obstruction-independent-auditmd"></a>

## Moving linear relations: exact quadratic obstruction and independent review

Date: 2026-10-14. Status: independently derived new compatibility calculation;
the accepted embedded quadratic transition is used as a premise. No previous
normal-bundle or constant-direction computation is repeated.

This note reviews the moving operator in Section 8 of
[the thick relation extension](https://github.com/markluxton1/STCI/blob/ffe78df0f9d4378255d1a2cdcf64b2e8a80a4655/research/supplements/RELATION_LIFTING_AND_GAP_COSTS.md#source-2026-10-13-generalization-thick-equality-extensionmd)
for a moving **linear** relation. The calculation gives an obstruction-zero
family, rather than an exclusion theorem.

### 1. Frames and the cohomology target

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

### 2. Exact coefficient calculation

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

### 3. Complete obstruction-zero locus on Delta != 0

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

### 4. Independent review of the pure-power quotient

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

### 5. All finite steps before the second independent relation

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

### 6. Audit scope

The new coefficient equations, their complete case split, the frame
identification, the pure-power splitting at every step, and the finite
principal-relation lifting argument have been independently derived. The
accepted chart transition and accepted quadric equation
were used without re-verification. No new finite test establishes a
proof of global existence. The next unresolved calculation is the
cubic compatibility of the obstruction-zero moving linear relations.


### Archived exact certificate: `research/computations/moving_linear_cubic_independent_audit_2026_10_14.py`

Original source preserved verbatim, including its limitations and external dependencies.

<details><summary>Historical source</summary>

```python
"""Independent cubic audit in quotient and relation normal coordinates.

The accepted quadratic Laurent discrepancy is an input.  The NEW cubic
calculation is performed directly from the exact embedded chart, before
reading the owner's cubic source.  It uses normal coordinates e,h such that
f0=h and ell0=e, rather than dividing a degree-two binary form by f0.

Run with Python's standard library only.  Output records the complete cubic
Laurent polynomial, the retained Cech class, and the exact diagonal-field
reduction.  No numerical sample, finite-field test, or inherited checker is
used.
"""
from fractions import Fraction as F
from collections import defaultdict

# Exact normal-degree <= 3 algebra in e,h, with Laurent z,t coefficients.
# No accepted quadratic formula is recomputed; its T is imported as a premise.
def clean(p):
    return {m:F(c) for m,c in p.items() if c and m[0]+m[1] <= 3}
def mon(e=0,h=0,z=0,t=0,c=1):
    return {(e,h,z,t):F(c)} if c else {}
def add(*ps):
    o=defaultdict(F)
    for p in ps:
        for m,c in p.items(): o[m]+=c
    return clean(o)
def scale(p,c): return clean({m:v*F(c) for m,v in p.items()})
def mul(*ps):
    o=mon()
    for p in ps:
        n=defaultdict(F)
        for a,c in o.items():
            for b,d in p.items():
                m=tuple(x+y for x,y in zip(a,b))
                if m[0]+m[1] <= 3: n[m]+=c*d
        o=clean(n)
    return o
def powp(p,n):
    o=mon()
    for _ in range(n): o=mul(o,p)
    return o
def neg(p): return scale(p,-1)
def extract(p,e,h):
    return {(0,0,z,t):c for (i,j,z,t),c in p.items() if (i,j)==(e,h)}
def show(p):
    return '\n'.join(f'z^{z} t^{t}: {c}' for (e,h,z,t),c in sorted(p.items(), key=lambda x:(x[0][2],x[0][3])) ) or '0'
z=mon(z=1); t=mon(t=1); one=mon(); eps=mon(e=1); eta=mon(h=1)

def calculate(label,A,B,C,D,delta_inv):
    a=add(A,mul(C,z)); b=add(B,mul(D,z))
    delta=add(mul(A,D),neg(mul(B,C)))
    # Accepted T formula, needed only to select the specified local corrections.
    T=add(mul(mon(z=-5,c=3),powp(b,3)),
          mul(mon(z=-4,c=F(-3,2)),a,powp(b,2)),
          mul(mon(z=-3,c=F(3,4)),powp(a,2),b),
          mul(mon(z=-2,c=F(-3,8)),powp(a,3)),
          neg(mul(delta,mon(z=-3),b)),
          mul(delta,mon(z=-2,c=F(1,2)),a))
    q0={m:c for m,c in T.items() if m[2]>=0}
    q1_dict={(-m[2]-4,m[3]):-c for m,c in T.items() if m[2]<=-4}
    # u=b e+D/delta h, v=-a e-C/delta h: f0=h, ell0=e.
    u=add(mul(b,eps),mul(D,delta_inv,eta))
    v=add(neg(mul(a,eps)),neg(mul(C,delta_inv,eta)))
    borig=add(u,mul(mon(z=1,c=F(3,2)),v))
    av=mul(borig,mon(z=-4))
    inv=mul(mon(z=-4),add(*[scale(powp(av,j),(-1)**j) for j in range(4)]))
    W=mul(add(mon(z=3),v),inv)
    ap=add(mul(z,inv),neg(powp(W,3)))
    bp=add(inv,neg(powp(W,4)))
    up=scale(ap,F(1,2))
    vp=add(scale(mul(W,ap),-3),scale(bp,2))
    f0=add(mul(a,u),mul(b,v))
    f1=add(mul(add(mul(A,W),C),up),mul(add(mul(B,W),D),vp))
    ell0=mul(delta_inv,neg(add(mul(C,u),mul(D,v))))
    ell1=mul(delta_inv,add(mul(A,up),mul(B,vp)))
    q1W=add(*[mul(mon(t=k,c=c),powp(W,j)) for (j,k),c in q1_dict.items()])
    F0=add(f0,mul(q0,powp(ell0,2)))
    F1=add(f1,mul(q1W,powp(ell1,2)))
    overlap=add(mul(mon(z=8),F1),neg(F0))
    L2eval=extract(overlap,1,1)
    D3eval=extract(overlap,3,0)
    cubic=add(D3eval,neg(mul(q0,L2eval)))
    retained={m:c for m,c in cubic.items() if -9<=m[2]<=-1}
    print('\nCASE',label)
    print('q0\n'+show(q0))
    print('q1 terms [w exponent,t exponent]:'+str(sorted(q1_dict.items())))
    print('quadratic pure quotient\n'+show(extract(overlap,2,0)))
    print('L2eval\n'+show(L2eval))
    print('D3eval\n'+show(D3eval))
    print('corrected cubic\n'+show(cubic))
    print('retained\n'+show(retained))
    return cubic,retained

diag,dr=calculate('diagonal',t,{}, {},one,mon(t=-1))
conic,cr=calculate('conic',mon(c=2),t,mon(t=-1,c=8),one,mon(c=F(-1,6)))

def reduce_quad_t(p):
    # t^2=(4/3)t-4 and t^-1=1/3-t/4 in Q[t]/(3t^2-4t+12).
    def qmul(x,y):
        a,b=x; c,d=y
        return (a*c-4*b*d,a*d+b*c+F(4,3)*b*d)
    def tp(n):
        x=(F(1),F(0)); y=(F(0),F(1)) if n>=0 else (F(1,3),F(-1,4))
        for _ in range(abs(n)): x=qmul(x,y)
        return x
    out=defaultdict(F)
    for (e,h,z,tt),c in p.items():
        a,b=tp(tt); out[(e,h,z,0)]+=c*a; out[(e,h,z,1)]+=c*b
    return clean(out)
def eval_t(p,tval):
    out=defaultdict(F)
    for (e,h,z,tt),c in p.items(): out[(e,h,z,0)]+=c*F(tval)**tt
    return clean(out)
print('\ndiagonal t=2 corrected retained\n'+show(eval_t(dr,2)))
print('\ndiagonal quadratic field corrected retained\n'+show(reduce_quad_t(dr)))

# Exact conclusions of the NEW cubic calculation.  The nonquadric diagonal
# reduction is in the full quadratic number field; conic formulas hold for
# an indeterminate invertible t, hence for every point of the open conic.
assert not eval_t(dr, 2)
assert reduce_quad_t(dr) == add(mon(z=-5,c=F(64,9)),mon(z=-5,t=1,c=F(-64,27)))
assert cr == add(mon(z=-1,t=-4,c=512),mon(z=-2,t=-3,c=-384),
                 mon(z=-3,t=-2,c=64),mon(z=-7,t=2,c=4),
                 mon(z=-8,t=3,c=-6),mon(z=-9,t=4,c=2))
print('\nPASS: exact cubic diagonal and open-conic identities')
```
</details>



## Consolidated historical supplement: `research/supplements/SATURATED_DUALITY_AND_MOVING_POWERS.md`

# Saturated duality, root descent and embedded formal surfaces

The first part gives one complete proof of projective normal flatness through saturated Gorenstein duality and a degree-zero resultant, including its balanced spectral interpretation and pure-power corollary. The local Hilbert-envelope proof has its own owner in [Normal flatness](../normal-geometry/normal_flatness_and_filtered_ci.md). The second part concerns a different object: all-orders embedded formal surfaces along reduced movement-two roots.

[R-0010](../../results/saturated_first_relation_normal_flatness.md) governs the saturated-first-relation result. The arbitrary-conormal and characteristic-free extension is retained as an independently reconstructed source-level theorem; this editorial consolidation does not enlarge the record. [R-0018](../../results/regular_singular_root_formal_obstruction.md) governs the regular-formal-surface exclusion. Neither result supplies a theorem for arbitrary actual equations.

<a id="2026-10-19-filtered-saturated-duality-moving-purepower-bridge"></a>
<a id="2026-10-19-filtered-saturated-duality-moving-purepower-independent-audit"></a>

## Projective normal flatness by duality and resultants

## 1. Exact setting, claim, and authority

Let `C` be a smooth connected projective curve over an algebraically
closed field, in a smooth threefold `X`, and suppose

    E=N_(C/X)^*=H^-1 tensor V,       dim V=2.

Let `Y` be an actual locally complete-intersection thickening with
`Y_red=C`. Write `A=O_Y`, `J=I_C A`, and

    K_j=ker(Sym^j E -> J^j/J^(j+1)).

Assume the **full** generic ordinary associated graded algebra is

    gr_(J_eta)(A_eta)=k(C)[x,y]/(f_r,g_s),
    2<=r<s,                      gcd(f_r,g_s)=1.          (1)

Assume the actual first relation is a saturated line subbundle

    K_r=R=H^-r tensor M subset Sym^r E,                  (2)

where `M subset Sym^r V tensor O_C` is a line subbundle. Set

    lambda=deg H,    epsilon=-deg M,    g=s-r,
    d=r+s-2.

The corresponding full root divisor `Z subset C x P(V*)` is finite flat
of degree `r` over `C`; write `pi:Z->C` and `O_Z(1)` for the direction
line bundle. The audited balanced-conormal conclusion is that a line bundle `N`
on `C` satisfies

    O_Z(s)=pi^*N.                                       (3)

Thus an everywhere-coprime second **quotient** relation exists in the
sense of [STCI-R-0008](../../results/spectral_root_picard_criterion.md).
This is an implication from actual filtered geometry to the accepted
spectral criterion; it does not claim to lift an arbitrary abstract
graded family back to an actual thickening.

The accepted inputs are the socle-line and Gorenstein MCM duality facts
in [the independent socle audit](../normal-geometry/socle_and_loewy_bounds.md#source-2026-10-13-generalization-socle-independent-auditmd),
and the root-quotient identification of R-0008 and its
[independent evidence](moving_power_and_spectral_roots.md#2026-10-14-generalization-spectral-root-curve-independent-audit).
The existing socle audit proves perfect ordinary pairings under extra
conditions. The perfect **saturated** pairing established next is the
new bridge; no assertion that the ordinary powers are already saturated
is imported from that audit.

In fact, the bridge also forces every ordinary power `J^i` to be
saturated and the ordinary associated graded algebra to be a uniform
fiberwise complete intersection of degrees `(r,s)`. Section 6 audits
this stronger conclusion.

In characteristic zero, for the pure-power specialization
`M=M_1^r`, with `M_1 subset V tensor O_C` and `deg M_1<0`, the audited
conclusion is that no such `Y` exists. Section 8 proves this directly.
For the rational base, combining (3) with the separately reviewed
[nonreduced-root obstruction](spectral_torsion_and_syzygy_splitting.md#2026-10-19-spectral-nonreduced-root-obstruction)
excludes every nonreduced moving full root under (1)--(2). The independent
audit of that latter obstruction remains its own evidence; it is not
replaced by this audit.

## 2. Saturation and perfect complementary pairings

Because `Y` is a pure one-dimensional lci scheme with unique reduced
support `C`, a generically zero subsheaf of `A` is zero. The generic
socle degree in (1) is `d`, so `J^(d+1)=0` globally.

Let `P_i` be the saturation of `J^i` in `A`, meaning the inverse image of
the maximal finite-support subsheaf of `A/J^i`. Locally it is the
inverse image of `(J_eta)^i` in `A_eta`. We have

    P_0=A,        P_1=J,        P_(d+1)=0,
    P_i P_j subset P_(i+j),     J P_i subset P_(i+1).

The product inclusions hold generically, then globally by saturation.
Every `A/P_i` is CM of dimension one or zero, and

    B_i=P_i/P_(i+1)

is a vector bundle on `C`: it embeds in the pure sheaf `A/P_(i+1)` and
is annihilated by `J`.

Let `S=Ann_A(J)`. The accepted socle theorem makes `S` a line bundle
on `C`. For the generic Artin Gorenstein algebra, the Gorenstein graded
algebra in (1) has symmetric Hilbert function and gives

    Ann_(A_eta)((J_eta)^i)=(J_eta)^(d+1-i).              (4)

One can check the equality without assuming a homogeneous splitting of
`A_eta`: the right side annihilates `(J_eta)^i`, and its length is the
length of `A_eta/(J_eta)^i` by Hilbert-function symmetry. Frobenius
duality gives exactly that length for the annihilator, so inclusion is
equality.

Each `Ann_A(P_i)` is saturated. Indeed, if a section is generically in
this annihilator, its products with `P_i` vanish generically in the pure
sheaf `A`, and therefore vanish. Consequently equality of generic
fibers in (4) yields

    Ann_A(P_i)=P_(d+1-i).                               (5)

Apply `Hom_A(-,A)` to

    0 -> B_i -> A/P_(i+1) -> A/P_i -> 0.

The first sheaf Ext of the CM quotient `A/P_i` into the Gorenstein
curve `A` vanishes. Thus the dual sequence is exact, and (5) gives

    B_(d-i)=Hom_A(B_i,A)=Hom_C(B_i,S).                  (6)

The map is induced by multiplication. In particular all complementary
pairings `B_i tensor B_(d-i) -> S` are perfect on all of `C`.

This is a statement about the saturated filtration. It permits torsion
in the original ordinary layers, and requires no global retraction
`Y->C` or splitting of the formal neighborhood.

## 3. The actual saturated first relation determines all early layers

For `j<r`, `K_j` has zero generic rank and is a subsheaf of a vector
bundle, so `K_j=0`. For `r<=j<s`, products of the actual relation (2)
give

    R tensor Sym^(j-r)E subset K_j.                     (7)

This left subsheaf is saturated: at each point the homogeneous
polynomial `f_r` is nonzero, so multiplication by it on binary forms
has the same rank at that point as over the generic field. The
cokernel is therefore locally free. Both sides of (7) have the same
generic rank by the full initial ideal in (1). Their difference embeds
as a rank-zero subsheaf in that vector-bundle cokernel and is zero.

Hence every ordinary layer through index `s-1` is a vector bundle.
Its finite successive extensions make `A/J^i` CM for `i<=s`, proving

    P_i=J^i                 for 0<=i<=s.               (8)

This is the exact place where the actual equality in (2) is needed.
Knowing only that the saturation of `K_r` is `R` does not justify (7)
with `R`, and does not imply (8).

For `j>=r-1`, define the rank-`r` quotient bundle

    Q_j=Sym^j V/(M tensor Sym^(j-r)V),

with the denominator zero at `j=r-1`. Its degree is

    deg Q_j=(j-r+1)epsilon,

and for `r-1<=j<s`, (7)--(8) give `B_j=H^-j tensor Q_j`.

## 4. Determinants force a zero-degree second spectral section

The complementary middle pair in (6) is `(r-1,s-1)`. Its two ranks are
`r`, with degrees

    deg B_(r-1)=-r(r-1)lambda,
    deg B_(s-1)=-r(s-1)lambda+g epsilon.

Perfectness therefore forces the exact degree identity

    deg S=-d lambda+g epsilon/r.                       (9)

This equality itself imposes an integrality condition; fractions are
only notation for an already integral degree.

By (8), `J^s=P_s`. The natural map from ordinary degree-`s` symbols to
the saturated layer is consequently surjective. It factors through
the old first-relation multiples, giving

    A_s=H^-s tensor Q_s -> B_s -> 0.                   (10)

Perfect duality and `d-s=r-2` give

    B_s=B_(r-2)^vee tensor S
       =H^(r-2) tensor S tensor (Sym^(r-2)V)^vee.

This is a rank-`r-1` bundle. Thus the kernel `T` of (10) is an actual
line subbundle of `A_s`. Computing degrees from (9)--(10) yields

    deg A_s=-rs lambda+(g+1)epsilon,
    deg B_s=(r-1)(-s lambda+g epsilon/r),
    deg T=-s lambda+s epsilon/r.                      (11)

These determinant calculations need no splitting of bundles on `C`
and no assumption that `C=P1`.

For `s>=r-1`, the standard divisor sequence on `C x P(V*)` gives

    Q_s=pi_*O_Z(s).

The inclusion `T->H^-s tensor pi_*O_Z(s)` is therefore adjoint to a
section

    sigma in H^0(Z,L),
    L=O_Z(s) tensor pi^*(H^-s tensor T^-1).              (12)

Its generic restriction is, up to an invertible scalar, the second
initial generator `g_s` modulo `f_r`. The full generic coprimality in
(1) says that this section is a unit on the entire generic root scheme,
including its nilpotents.

## 5. Why nilpotents and special fibers cannot hide zeros

The full root `Z` is an effective Cartier divisor in a smooth surface
and is finite flat over `C`. Thus it is one-dimensional CM, and every
associated generic point lies over the generic point of `C`. A
section invertible at those generic points is a nonzerodivisor on
`O_Z`, even when `Z` is reducible or nonreduced. Therefore (12) defines
an injection with finite-length cokernel:

    0 -> O_Z -> L -> D -> 0.                            (13)

The degree of `O_Z(1)` is `epsilon`: intersect the root divisor, whose
class is `r` times the direction class minus `pi^*M`, with the direction
class. Pullback of a line bundle of degree `a` on `C` has degree `ra`
on `Z`. These are Euler-characteristic/intersection degrees and retain
the multiplicities of nonreduced components. Equations (11)--(12) give

    deg L=s epsilon+r(-s lambda-deg T)=0.

Taking Euler characteristics in (13) now yields `length(D)=0`. Thus
`D=0` and `sigma` is nowhere zero on the full scheme `Z`.
Consequently

    O_Z(s)=pi^*(H^s tensor T),

which is (3). There is no discarded degeneration divisor: degree zero
forces the actual divisor of this section to vanish.

This completes the general actual-to-spectral bridge. It proves the
existence of a uniform abstract second quotient relation; that relation
need not be a globally lifted second polynomial line. This distinction
is required by R-0008 and is preserved here.

## 6. The uniform quotient forces normal flatness

Let

    K'_s=ker(Sym^s E -> B_s).

Its quotient by the old first-relation multiples is exactly the line
`T` in (10). The inclusion `T->A_s` is everywhere coprime to the first
relation because the corresponding spectral section is a unit on the
full root scheme. Define the graded quotient algebra

    D=Sym(E)/(R,K'_s).

Locally on `C`, lift a frame of `T` to a degree-`s` form. Then `D` is
presented by that form and a frame of the degree-`r` first relation.
They are coprime in every fiber. Thus `D` is a relative graded
complete intersection; each `D_i` is a vector bundle of the same rank
as the generic CI Hilbert function. No global splitting of
`0 -> R Sym^(s-r)E -> K'_s -> T -> 0` is needed.

These relations vanish in the saturated associated graded algebra
`B=direct_sum B_i`, so there is a natural graded algebra map

    phi:D -> B

which is an isomorphism generically. Its top degree is a map of line
bundles. The top line of a binary graded CI glues as

    D_d=R tensor T tensor det(E)^-1.

This can be checked in local Koszul presentations: changing a first
generator and a lift of the second changes their ordered wedge by the
product of their scalar transitions; adding first-generator multiples
to the second has no effect. Therefore (11) gives

    deg D_d=(-r lambda-epsilon)
            +(-s lambda+s epsilon/r)+2lambda
           =-d lambda+g epsilon/r
           =deg S.

The generic isomorphism `phi_d:D_d->B_d=S` is consequently a global
isomorphism: a nonzero map between line bundles of equal degree on the
smooth projective curve has no zero divisor.

For each closed point `c`, the graded CI algebra `D_c` has perfect
pairings `D_(i,c) tensor D_(d-i,c) -> D_(d,c)`. If a nonzero element of
`D_(i,c)` were killed by `phi_(i,c)`, multiply it by a complementary
element giving nonzero top product. Algebra-map compatibility would
kill that product under `phi_(d,c)`, contradicting the top
isomorphism. Hence every `phi_(i,c)` is injective. Source and target
have the same rank, so every `phi_i` is an isomorphism of bundles.

It follows that `B` is generated in degree one. Since `P_1=J`, this
gives `P_i=J^i+P_(i+1)`. Descending induction from `P_(d+1)=0` yields

    P_i=J^i                    for every i.

Thus all ordinary layers are vector bundles and the ordinary graded
algebra is itself a uniform fiberwise binary complete intersection.
This conclusion was not assumed in Sections 2--5; it follows from
their spectral section and the top-line comparison.

## 7. Arbitrary conormal: the resultant upgrade

The projective normal-flatness conclusion actually requires no balanced
splitting of `E`. Let `C` again be a smooth connected projective curve,
let `E=N_(C/X)^*` be arbitrary of rank two, and keep the actual lci,
unique-support, full generic CI hypotheses of Section 1. Assume

    K_r=R subset Sym^r E

is an actual line subbundle, with `2<=r<s`. Put

    h=deg E,        a=deg R.

Sections 2--3 still apply: their saturation and MCM arguments use no
splitting. In particular the early layer quotient

    A_j=Sym^j E/(R tensor Sym^(j-r)E)

is a rank-`r` bundle for `j>=r-1`, and agrees with `B_j` for `j<s`.
Using `deg Sym^j E=j(j+1)h/2`, its degree is

    deg A_j=r(2j-r+1)h/2-(j-r+1)a.                    (14)

The complementary middle pair is still `(r-1,s-1)`. Taking degrees
in its perfect pairing gives

    deg S=(s-1)h-(s-r)a/r.                            (15)

As before, `P_s=J^s` yields an actual vector-bundle surjection
`A_s->B_s`. Its kernel is a line `T`. From

    B_s=(Sym^(r-2)E)^vee tensor S

and (14)--(15), its degree is

    deg T=s h-s a/r.                                  (16)

Choose local frames `f` of the degree-`r` relation and local lifts `g`
of `T` in degree `s`. The binary resultant glues as a section of

    U=(det E)^(rs) tensor R^(-s) tensor T^(-r).         (17)

The determinant exponent is fixed, for example, by the intrinsic
identity for two linear forms: their resultant is their wedge in
`det E`. In general the Sylvester determinant has degree `s` in the
first coefficients, degree `r` in the second coefficients, and weight
`rs` under a basis change of `E`. Changing a lift by `g->g+q f` does
not change the resultant. These are polynomial identities over the
integers, so do not require characteristic zero.

By the full generic CI hypothesis, the section is nonzero generically.
Equations (16)--(17) give

    deg U=rs h-s a-r(s h-s a/r)=0.

Thus its zero divisor on the smooth projective curve is empty. The
resultant is nonzero in every fiber, so the first relation and the
second quotient relation are coprime in every fiber. This replaces
the spectral zero-divisor argument of Section 5.

Construct `D=Sym(E)/(R,K'_s)` as in Section 6. Its top line is again
`R tensor T tensor det(E)^-1`, of degree

    a+(s h-s a/r)-h
      =(s-1)h-(s-r)a/r
      =deg S.

The generic top map is therefore an isomorphism everywhere. The perfect
fiberwise CI pairings then give `D_i=B_i` for every degree. Descending
induction gives `P_i=J^i` for all `i`, exactly as in Section 6.

**Audited arbitrary-conormal theorem.** An actual lci thickening of a
smooth connected projective curve in a smooth threefold, with full
generic coprime binary CI initial ideal of degrees `2<=r<s` and actual
saturated first relation line, has every ordinary power saturated and
a uniform fiberwise graded CI normal algebra of degrees `(r,s)`.
No balanced conormal, rationality, or characteristic-zero assumption
is used in this bridge. The corresponding graded/root exclusions can
have additional hypotheses, which must still be retained.

The equal-degree case is not included in this resultant proof: then
the first relation space has rank two and the construction of its
second quotient line is different. A separate local Hilbert-function
argument is recorded in
[the normal-flatness proposal](../normal-geometry/normal_flatness_and_filtered_ci.md#2026-10-19-filtered-generic-ci-normal-flatness);
that broader variant is not needed as a premise here.

## 8. Independent pure-power shortcut

For the moving-power specialization, write the moving direction as
`M_1 subset V tensor O_C`, `deg M_1=-e<0`, so the coefficient line in
Section 1 is `M=M_1^r` and `epsilon=re`. In characteristic zero the
accepted apolar formula is

    Q_s=M_1^(-(g+1)) tensor (constant rank-r bundle),

where constant determinant factors of `V` are harmless line factors.
Equation (9) becomes

    deg S=-d lambda+g e.

The surjection (10) would thus be a nonzero map between bundles

    A_s=H^-s M_1^(-(g+1)) tensor (constant rank r),
    B_s=H^(r-2) S tensor (constant rank r-1).

Every matrix entry of such a map is a section of the line bundle

    H^d tensor S tensor M_1^(g+1),

whose degree is

    d lambda+(-d lambda+g e)-(g+1)e=-e<0.

It has no global sections on the smooth projective integral curve.
The map (10) is therefore zero, contradicting its surjectivity onto
rank `r-1>0`.

This proves actual-thickening nonexistence for a saturated moving
pure-power first relation and full generic coprime CI initial ideal on
**any** smooth projective base curve with balanced split conormal. It
does not require proving that all late ordinary powers are saturated,
and it does not assume everywhere coprimality in advance.

## 9. Adversarial checks and retained boundaries

* **Saturation of the actual first relation is indispensable.** If
  `K_r=R(-D0)` for an effective nonzero divisor, multiplying actual
  relations only supplies `R(-D0)` multiples. The early quotient may
  have torsion, so `P_s=J^s` and (10) need not hold. Replacing `K_r` by
  its saturation would erase precisely the remaining defect.

* **The full generic initial ideal is indispensable.** It supplies
  `d=r+s-2`, symmetric generic Hilbert function, the exact early
  relation ranks, and the generic unit in (12). Two coprime-looking
  selected symbols alone do not establish these facts if there are
  additional initial generators or leading cancellations.

* **Gorenstein and purity are used separately.** Gorenstein CM duality
  proves (6); purity removes generically zero subsheaves and makes
  saturation intrinsic. A finite principal-relation thickening from
  the old tower need not be Gorenstein, and is therefore no
  counterexample.

* **The degree proof has projective scope.** The degree argument in
  (13), the degree-zero resultant, and the negative-degree vanishing in
  Section 8 use projectivity. This proof alone makes no affine-base
  extension. The separately recorded local Hilbert-function argument
  addresses that larger scope through a different input.

* **Unique support matters.** If `Y_red` has residual components in
  addition to `C`, an ideal generically zero along `C` can be nonzero
  on those other components. The proof cannot be applied unchanged to
  the whole intersection scheme in that situation. No exceptional
  vertical component is identified with a component downstairs.

* **Nonreduced total roots differ from nonreduced special fibers.**
  The spectral conclusion concerns the full divisor `Z`. It permits
  ramification and multiple special fibers of an integral reduced
  root. Applying the separate doubled-divisor theorem excludes
  repeated total components only under its rational-base,
  positive-movement, characteristic-zero hypotheses.

* **The linear and equal-degree cases are outside scope.** The proof
  uses `r>=2` and the first rank-one relation with `r<s`. It does not
  silently extend to primitive generic algebras or two independent
  first relations of the same degree.


## 2026-10-19-singular-root-investigation

# Reduced movement-two roots: the remaining formal surface must be singular

Date: 2026-10-19. Author: `singular_roots` research agent.

Status: the regular-formal-surface statement is stated in [R-0018](../../results/regular_singular_root_formal_obstruction.md); its additional observations retain source-level scope.
The separate audits are
[the smoothing audit](https://github.com/markluxton1/STCI/blob/f5066d138efb4b0d285893a463aa65197dba1e39/research/supplements/SATURATED_DUALITY_AND_MOVING_POWERS.md#source-2026-10-19-regular-singular-root-smoothing-auditmd) and
[the equal-slope two-component audit](https://github.com/markluxton1/STCI/blob/f5066d138efb4b0d285893a463aa65197dba1e39/research/supplements/SATURATED_DUALITY_AND_MOVING_POWERS.md#source-2026-10-19-regular-reducible-root-independent-auditmd).
This note does not
settle the singular-formal-surface case.

## 1. Exact scope and accepted premises

Let `k` be algebraically closed of characteristic zero. Work with the fixed
rational quartic `C0` in `P3`, its blowup `B=Bl_C0(P3)`, and exceptional
divisor `E=P1_base x P1_direction`. Write `p:E->P1_base`, and use the
repository conventions

    O_E(E)=O_E(7,-1),       H|E=O_E(4,0).

An embedded all-orders Cartier lift of a full root `Z subset E` means
compatible effective Cartier divisors on every exceptional neighborhood,
as in the source underlying
[STCI-R-0005](../../results/smooth_root_formal_obstruction.md). Its inverse
limit is a formal effective Cartier surface `Vhat` in the completion of
`B` along `E`, with scheme-theoretic intersection `Vhat cap E=Z`.

The accepted scope distinctions remain premises:

- STCI-R-0005 excludes smooth full roots of class `(2,r)`, `r>=2`.
- [STCI-R-0011](../../results/moving_nonreduced_spectral_root_obstruction.md)
  makes a spectral-descent survivor reduced. In movement two it is
  integral `(2,r)`, or two distinct smooth `(1,r/2)` components when `r`
  is even.
- [STCI-R-0010](../../results/saturated_first_relation_normal_flatness.md)
  supplies spectral uniformity for actual lci thickenings only under its
  full generic binary-CI and saturated-first-relation hypotheses.
- [STCI-R-0006](../../results/actual_ci_smooth_root_bridge.md) is an actual
  finite-gap bridge with a **smooth full root**; no singular-root version
  is assumed in this note.

The proposed theorem below concerns the actual ambient formal lifting
problem. It assumes no spectral Picard descent and supplies no automatic
bridge from arbitrary actual STCI equations.

## 2. Regular-formal-surface theorem

**Theorem A.** Let `Z` be a reduced effective Cartier divisor of class
`(2,r)`, `r>=2`, finite flat over `P1_base`. There is no embedded
all-orders Cartier lift whose formal surface `Vhat` is regular along
the whole of `Z`.

Here regularity is a condition on the **lifted formal surface**, not on
the possibly singular curve `Z`. For a hypersurface in the completion of
the smooth threefold `B` over the perfect field `k`, the condition means
that its completed local surface rings at closed points of `Z` are
regular. This is the smooth-formal-surface condition used below.

Thus, if a reduced singular movement-two root has any all-orders
Cartier lift, every such lift has a singular surface point above
`Sing(Z)`. This narrows the surviving geometry, but does not exclude
these singular lifted surfaces.

The proof uses a smoothing **inside an algebraized smooth surface**.
It does not assert that singular roots can be smoothed in the original
exceptional root-lifting functor.

## 3. Algebraize using the singular root itself

Because `Z=Vhat cap E`, the exceptional parameter is a nonzerodivisor on
`Vhat`, and `Z` is an effective Cartier divisor in this regular formal
surface. Consequently

    N_(Z/Vhat)=O_Z(E)=O_Z(7,-1)=:N.                 (1)

The root `Z` is connected: the exact sequence on `E`

    0 -> O_E(-2,-r) -> O_E -> O_Z -> 0

and Kunneth give `H0(O_Z)=k`, since `r>=1` makes
`H1(O_E(-2,-r))=0`.

For every irreducible component `D` of `Z`, write its bidegree `(a,b)`.
Finiteness over the base gives `b>0`; effectiveness and total first
bidegree two give `0<=a<=2`. Therefore

    deg(N|D)=7b-a >=5>0.                           (2)

A line bundle on a proper curve is ample if its degree on every reduced
irreducible component is positive, so `N` is ample.

Bost's **Corollary 3.8**, rather than only his smooth-center Theorem 3.5,
applies here. It permits a proper connected locally complete intersection
scheme of definition, while requiring the formal scheme itself to be
smooth and its normal bundle ample. It algebraizes `Vhat` as a branch
of an integral algebraic surface `W subset B`. Source: J.-B. Bost,
[*Algebraic leaves of algebraic foliations over number fields*,
printed pp. 187--188](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf),
Theorem 3.5, Theorem 3.7, and Corollary 3.8. This is the geometric part of
the paper; no arithmetic hypothesis is imported.

Normalize `W`. The selected formal branch is regular, hence normal.
The normalization/completion argument used in the accepted smooth-root
proof therefore preserves the entire selected branch. That argument
uses normality of `Vhat`, not smoothness of the curve `Z` itself. Its
local maps to the finite normalization glue uniquely, and reduction
modulo the exceptional parameter embeds the same possibly singular
`Z` into the normalization. The selected completed local factors are
regular. Resolve the normalized algebraic surface outside this regular
neighborhood of `Z`. We obtain a smooth projective surface `T` containing
the same Cartier curve `Z`, with its original formal neighborhood.

This leaves the numerical data

    p_a(Z)=r-1,       Z^2=7r-2.                    (3)

Let `S` be the image of `W` in `P3`, `d=deg(S)`, and let `H` on `T` be
the pullback of the hyperplane class. The surface is not exceptional,
and the blowup is an isomorphism away from `E`; hence `T->S` is
birational, `H` is nef, and

    H^2=d>0,         H.Z=4r.                      (4)

Other algebraic branches of `W` and other components of `W cap E` are
retained. None is discarded by saturation.

## 4. The normal line is generated and unobstructed

The relevant vanishing does not need a classification of the singularities.
For `N=O_Z(7,-1)`, the two restriction sequences are

    0 -> O_E(5,-r-1) -> O_E(7,-1) -> N -> 0,
    0 -> O_E(4,-r-1) -> O_E(6,-1)
      -> N tensor p*O_P1(-1) -> 0.

Kunneth gives

    H1(Z,N)=0,
    H1(Z,N tensor p*O_P1(-1))=0.                  (5)

For example, the middle terms have zero `H1` because `O_P1(-1)` has no
cohomology; the left terms have zero `H2` because their first ruling
degree is nonnegative.

The finite flat map `p:Z->P1` makes `p_*N` a vector bundle. Projection
formula and (5) give `H1(P1,(p_*N)(-1))=0`. Splitting this vector bundle
on `P1` shows that every summand has nonnegative degree. Thus `p_*N` is
generated by its global sections. The finite-map evaluation
`p* p_*N -> N` is surjective, so **`N` is generated by global sections**.

These are calculations on the original full `Z`, not on its
normalization, and preserve gluing at singular points.

## 5. An embedded smoothing lemma and its application

**Lemma B.** Let `D` be a connected reduced effective Cartier divisor
on a smooth projective surface `T` over characteristic zero. If
`H1(D,N_(D/T))=0` and `N_(D/T)` is generated by global sections, then
`D` has a flat embedded deformation on `T` whose general fiber is a
smooth connected curve, numerically equivalent to `D`.

**Proof.** Embedded Cartier deformations have tangent space `H0(N)`
and obstruction space contained in `H1(N)`. Local deformations lift
because a local defining nonzerodivisor can be lifted. Hence the
Hilbert scheme of `T` is smooth at `[D]`. Work on a smooth irreducible
open neighborhood `U` of this point, shrinking to the relative
effective-Cartier locus of the universal family `D_U subset T x U`.

At a point `x` of the central curve, write a completed local equation
of the universal family as

    f(x_1,x_2) + sum_i t_i eta_i(x_1,x_2)
                  + terms of parameter order >=2.

The classes of `eta_i` span the evaluations of `H0(N)` in the normal
fiber at `x`. Global generation gives an index with `eta_i(x)!=0`.
The total universal family is therefore regular at `x`, since its
equation has a unit derivative in that parameter direction. The whole
central curve lies in this regular locus. Properness over `U` allows
shrinking `U` so that the entire total family is regular. Over the
perfect field `k` it is smooth over `k`.

Its components dominate `U` by flatness. Characteristic-zero generic
smoothness, followed by properness, supplies a nonempty open subset of
`U` over which the family has smooth fibers. Since `H0(O_D)=k`, upper
semicontinuity gives `h0(O_(D_u))=1` near the central point; these smooth
fibers are connected, hence integral. A connected flat family of
Cartier divisors gives algebraic, hence numerical, equivalence. QED.

The embedded deformation inputs can be checked in Hartshorne's
[author-hosted *Lectures on Deformation Theory*](https://math.berkeley.edu/~robin/math274root.pdf),
Theorem 2.4 (tangent space), Theorem 6.3 (the normal-sheaf gluing
obstruction, explicitly including lci schemes), and Theorem 9.3
(lifting a regular sequence). The elementary universal-family argument
above proves the particular smoothing consequence; no claim of
equisingular deformation versality is needed.

Apply Lemma B to the curve `Z subset T` from Section 3, using (5).
There is a smooth connected integral curve `Z_t subset T` with

    g(Z_t)=r-1,       Z_t^2=7r-2,       H.Z_t=4r.    (6)

The smoothing occurs on `T`; `Z_t` need not map into `E` or cover `C0`.
Only the numerical data (6) enter the next surface argument. The
original root `Z` remains on `T` and still lies over `C0`.

## 6. Opposing degree bounds

The smooth curve `Z_t` satisfies

    Z_t^2-(4g(Z_t)+5)=3r-3>0.

Hartshorne's high-self-intersection theorem and the ruled-model
intersection argument already isolated in the evidence for
STCI-R-0005 apply to the pair `(T,Z_t)` and the nef divisor `H`.
They give

    d <= max_(a positive integer)
              (8ra-(7r-2)a^2) <= r+2.             (7)

The last maximum is at `a=1`, since `7r-2>=4r` for `r>=2`. The
geometric input is Hartshorne,
[*Curves with high self-intersection on algebraic surfaces*,
Theorem 4.1, printed p. 122](https://www.numdam.org/item/PMIHES_1969__36__111_0.pdf).
The local equivalence to the ruled neighborhood and the nef square
comparison are the same accepted mechanism as in
[the preserved independent branch review](finite_root_families_and_smooth_obstructions.md#source-2026-10-15-formal-branch-ruled-model-degree-bound-reviewmd).
We use that mechanism with the new smoothed curve, not the statement
that a smooth `(2,r)` root itself exists in `E`.

Meanwhile `W cap E` contains the original full root `Z`. Thus the
generic multiplicity `m` of the integral surface `S` along `C0`
satisfies `m>=r`. A general plane section is an integral degree-`d`
plane curve with multiplicity at least `m` at the four distinct points
of its intersection with `C0`. Its arithmetic genus gives

    (d-1)(d-2) >= 4m(m-1) >= 4r(r-1).             (8)

Equations (7)--(8) force

    r(r+1) >= 4r(r-1),

which is impossible for `r>=2`. This proves Theorem A under the stated
formal-surface regularity hypothesis.

## 7. Separate two-component proof without Hilbert smoothing

For the R0011 boundary `Z=D1 union D2`, `Di=(1,q)`, `r=2q`, assume the
lifted formal surface is regular along one full component. The surface
is automatically regular away from `D1 cap D2`, because the root is
smooth there. Regularity along one component includes every
intersection point, so it implies regularity along all `Z`.

There is a shorter proof in this case. In the regular formal surface,

    D1^2 = E.D1-D2.D1 = (7q-1)-2q = 5q-1,
    H.D1 = 4q.

Algebraization by Bost may use the full lci root `Z`, or the smooth
center `D1`, whose normal degree is positive. Normalize and resolve
outside `D1`, preserving its square. Hodge index yields

    d <= (H.D1)^2/D1^2
       = 16q^2/(5q-1) <=4q.

Both components remain in `W cap E`, so `m>=2q`. But

    (4q-1)(4q-2) < 4(2q)(2q-1)

for every `q>=1`, contradicting the plane-section genus bound.
The independent audit linked above reconstructs this shorter proof.

## 8. The exact residual gap and local countershields

At a singular root point, write an exceptional parameter as `u` and a
local lift equation as

    g = f_Z + u h_1 + u^2 h_2 + ... .

Since `df_Z` vanishes there, the lifted surface is regular at this point
exactly when `h_1` has nonzero value. Therefore Theorem A says that
every surviving all-orders lift must have at least one singular root
point with `h_1=0`. This is a concrete first-jet incidence condition
for the remaining formal problem, not an emptiness computation.

There is no automatic regularity implication. In a completed smooth
threefold chart the local equations

    g=xy+u^2,             g=y^2-x^3+u^2

give all-orders embedded Cartier lifts of, respectively, the reduced
node `xy=0` and cusp `y^2-x^3=0` on `u=0`, while the total formal
surfaces are singular at the origin. These are local counterexamples
to the missing regularity implication. They are not global lifts on
the actual exceptional surface of `C0` and do not construct STCIs.

Resolution of such singular lifted surfaces can change the normal
degree of the selected normalized root; the accepted smooth-branch
normal-degree argument cannot simply be reused there. Theorem A does
not exclude that stratum.

No finite jet cutoff, actual-CI singular-root bridge, arbitrary-first-
relation statement, or unrestricted `C0` nonexistence result is claimed.
The universal STCI question remains open.

## 9. General balanced-degree observation

The same proof, if independently reviewed in this scope, works in
characteristic zero for any smooth rational degree-`e` curve in `P3`,
`e>=4`, with explicit balanced normal bundle `O(2e-1)^2`.
Replace `7` by `lambda=2e-1` and `4` by `e`. The normal line is
`O_Z(lambda,-1)`; the same restriction-sequence proof gives generation
and vanishing because `lambda-3>=0`. Ampleness holds since
`lambda*b-a>0`. The smoothed curve has square `lambda*r-2`, genus
`r-1`, and hyperplane intersection `e*r`. The ruled-model bound remains
`d<=r+2`, while the opposing plane bound is
`(d-1)(d-2)>=e*r*(r-1)`, again contradictory for `e>=4,r>=2`.
This observation does not remove the singular-lifted-surface hypothesis.

## 10. Evidence and review status

This is a conceptual argument; no inherited verifier or accepted proof
was rerun. New calculations are the exact ruled-surface cohomology in
Section 4, the embedded smoothing argument in Section 5, and the scope
bridge retaining the original singular root while using a smooth
numerically equivalent curve on `T`.

The linked independent audits both record PASS for the fixed-C0
conditional statements. The degree-e observation in Section 9 remains
separately scoped and is not included in the reported fixed-C0 theorem.

## Characteristic scope of descent, duality and formal lifting

Saturated MCM duality and the arbitrary-conormal degree-zero resultant proof use no separability or division by an integer, as their explicit proofs show. The full-root Picard criterion is likewise valid in arbitrary characteristic. The moving-pure-power shortcut uses the characteristic-zero apolar quotient formula, and the theorem excluding repeated moving total components uses detection of integral ruling degrees by logarithmic Chern classes; the [fixed-degree apolar extension](moving_power_second_relation.md#positive-characteristic-reach-of-the-pure-power-mechanism) requiresp>s, while the [repeated-component extension](spectral_torsion_and_syzygy_splitting.md#prime-to-characteristic-spectral-descent-excludes-repeated-moving-components) requiresp∤s on the rational base. No unrestricted positive-characteristic extension is asserted. In characteristicp, on the diagonal D of P1×P1, A=O(-1,1) restricts trivially to D and A^p restricts trivially to2D because (1+h)^p=1 modulo I_D². Thus the doubled-divisor Picard injectivity step fails exactly where integer detection fails.

The smooth formal-root theorem R0005 and actual-CI smooth-root bridge R0006 have separately reviewed characteristic-free scopes under their explicit balanced-normal/smooth-full-root/actual-generation hypotheses. The bridge retains inseparable root primes and uses the actual local ring, not a coefficient-field splitting of its completion. The regular-singular-root theorem R0018 below remains in its accepted characteristic-zero scope; the argument does not automatically extend through singular formal surfaces. None of these restricted hypotheses contradicts [the every-positive-characteristic quartic-carrier construction](../arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier) on the fixed curve.


---

## Source: 2026-10-19-regular-reducible-root-independent-audit.md

# Independent audit: a regular formal surface cannot lift the equal split root

Date: 2026-10-19. Reviewer: `regular_reducible_audit`. The local Cartier,
intersection-length, completion-transitivity, and companion-containment
steps were separately checked by `regular_reducible_audit/local_check`.

Status: **PASS for the precise conditional nonexistence statement below.**
This is an independent review note, not a result record. No accepted
mathematics or metadata is changed. In particular, this note does not
apply the smooth-root statement STCI-R-0005 to a singular root.

## 1. Exact statement and inputs

Work over an algebraically closed field of characteristic zero with the fixed
smooth rational quartic `C0`. Let

    B = Bl_C0(P3),  E = P1 x P1,  O_E(E) = O_E(7,-1).

The first factor is the base `C0`. Fix `q >= 1`, and let `D1,D2` be distinct
smooth integral divisors of class `(1,q)` on `E`. Put

    Z = D1 union D2

with its reduced scheme structure. Suppose compatible embedded effective
Cartier lifts on all exceptional neighborhoods produce a Cartier formal
surface `V` in `B-hat_E`, whose reduction modulo the exceptional parameter is
exactly `Z`.

**Claim audited.** Such a lift cannot have `V` regular at every point of at
least one full component `Di`.

The words “at every point” are essential: regularity only at the generic
point of a component is automatic here and does not satisfy this hypothesis.
The assertion permits arbitrary tangency and intersection multiplicities
between `D1` and `D2`.

The accepted blowup conventions and the branch normalization, resolution,
multiplicity, and plane-genus mechanisms are recorded in
[STCI-R-0005](../../results/smooth_root_formal_obstruction.md) and its
[independent source audit](finite_root_families_and_smooth_obstructions.md#2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit),
especially Sections 1--3 and 5--6. They are used within their stated scope;
the accepted smooth-root exclusion itself is not replayed. The new points
checked here are the self-intersection of a component of a reducible root,
the change of completion center, retention of the companion component, and
the resulting numerical contradiction.

The primary algebraicity input is
[Bost, Theorem 3.5 and Corollary 3.8, printed pp. 187--188](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf#page=27).
The smooth-center version applies to a smooth connected projective curve
and a smooth formal surface with ample normal line; its algebraic closure
has the same dimension. The lci-center corollary also permits a proper
connected center that is not smooth. These are geometric results over a
field, with no number-field or analytic-convergence hypothesis. The
accepted source audit checks that the printed dimension condition includes
curves; the text extraction of the PDF loses the equality stroke.

## 2. Local algebra and the component normal degree

Write `E=(u)`. At an intersection point `p`, choose equations `a,b` of
`D1,D2` on `E` and lifts to the completed regular local ring of `B`.
After multiplying the equation of `V` by a unit, its equation is

    g = a*b + u*h.

At `p`, both `a,b` vanish, so the linear part of `g` is `h(p)*u`.
Consequently regularity of `V` at `p` forces `h` to be a unit. This argument
does not require that `a,b` be independent parameters: it includes tangent
components and higher intersection multiplicities.

Inside the regular full completed local ring of `V` at `p`,

    u = -a*b/h,
    I_D1 = (u,a) = (a),   I_D2 = (u,b) = (b).

Thus both components are Cartier there and

    length O_V,p/(a,b) = length O_E,p/(a,b).

Away from their intersection, the root is smooth and the differential of
its local equation already has a nonzero component tangent to `E`; hence
`V` is automatically regular there. It follows in particular that
regularity along one full `Di` implies regularity along all of `Z`.

The exceptional parameter is a nonzerodivisor on `V`: locally `g mod u`
is a nonzerodivisor on the smooth integral surface `E`, so `u,g` form a
regular sequence. Its zero divisor on `V` is exactly `D1+D2`. Restricting
the associated divisor identity to `D1` gives

    deg N_(D1/V)
       = deg O_D1(E) - (D1.D2)_V
       = (7q-1) - (D1.D2)_E
       = (7q-1) - 2q
       = 5q-1.                                      (1)

This is a normal line of positive degree for every `q>=1`, hence is ample
on the smooth projective curve `D1`. The same computation holds for `D2`.

## 3. Algebraization and why the other component is retained

Complete `V` along `D1`. The inclusion `D1 subset E subset B` permits
completion in two stages; completing `B-hat_E` further along `D1` gives
`B-hat_D1`. The resulting `V-hat_D1` is a closed smooth formal surface in
`B-hat_D1`, admits `D1` as its scheme of definition, and has normal line
(1). Bost's smooth-center theorem therefore gives an integral algebraic
surface `W subset B` containing this formal branch.

Formal containment along `D1` must not be replaced by an unsupported
claim that `W` has only this branch. Nevertheless it forces the algebraic
companion `D2` to be contained in `W`:

1. Choose any `p in D1 intersect D2`; such a point exists because the
   total intersection number is `2q>0`.
2. Let `w` be a local algebraic equation of `W` in `B` near `p`. It is
   zero on `V-hat_D1` and hence in its full maximal-ideal completion at
   `p`.
3. That full completion is exactly the full completion of the original
   `V` at `p`, by transitivity of completion. It contains the completed
   germ of `D2` as the quotient by `(b)` in Section 2. Thus `w` is zero
   in the completion of `O_D2,p`.
4. The map from the noetherian local domain `O_D2,p` to its completion
   is injective. Therefore `w` already vanishes in `O_D2,p`. This gives
   algebraic containment on a nonempty open subset of `D2`; integrality
   of `D2` and closedness of `W` give `D2 subset W` globally.

The argument uses an actual intersection point, the same full completed
branch at that point, and the algebraic curve `D2`. Mere abstract
isomorphism of formal surfaces would not justify it. Nor would it
justify retaining a second component disjoint from the completion center.
Here it gives scheme-theoretic containment of the reduced curves
`D1+D2` in the effective Cartier divisor `W|E` on the smooth surface `E`.

There is a shorter valid route in this specific setting. Section 2 shows
that `V` is smooth along its entire support `Z`; the center `Z` is proper,
connected, and Cartier in `V`. Its normal line is `O_Z(E)`, of degree
`7q-1>0` on each irreducible component, hence ample on `Z`. Bost's lci-center
Corollary 3.8 then algebraizes the full `V` directly, and reduction modulo
`u` immediately retains both components. The smooth-center route above
also proves the proposed continuation step explicitly.

## 4. Normalization, degree, and Hodge index

The selected formal branch is regular. On the algebraic normalization
of `W` it lifts uniquely and is the completion of a regular neighborhood
of an embedded copy of `D1`. This is the same finite-normalization and
whole-curve gluing mechanism checked in Section 3 of the accepted source
audit, now applied to the smooth center `D1`. Extra algebraic branches
are allowed. Resolve the normalization away from this regular
neighborhood, obtaining a smooth projective surface `T` with

    D1^2 = 5q-1.

Since `u` is nonzero on the selected formal branch, `W` is distinct from
`E`. Its image `S subset P3` is an integral surface and `W` is its strict
transform. Let `H` be the pullback to `T` of a hyperplane and put
`d=deg S`. Then

    H is nef,  H^2=d>0,  H.D1=4q.

Hodge index on `T` gives

    d*(5q-1) <= (4q)^2,
    d <= 16q^2/(5q-1) <= 4q,                         (2)

where the last inequality is equivalent to `q>=1`. No ruled-surface
classification or strict high-self-intersection threshold is needed for
this equal split case.

Let `m` be the generic order of `S` along `C0`. The restriction `W|E`
has degree `m` on a generic exceptional fiber and contains `D1+D2`.
Each component has fiber degree `q`; thus

    m >= 2q.                                         (3)

This lower bound remains valid with every additional algebraic branch,
exceptional intersection component, and multiplicity retained.

## 5. Numerical contradiction

The accepted plane-section argument for an integral degree-`d` surface
of generic multiplicity `m` along the smooth quartic gives

    (d-1)(d-2) >= 4m(m-1)
                >= 4(2q)(2q-1)
                 = 16q^2-8q.                        (4)

It uses a general integral plane section, transverse intersection with
the four points of `C0`, and the arithmetic genus after blowing up those
points. No assumption of ordinary plane singularities or absence of
residual surface branches is present.

For positive integral `d<=4q`,

    (d-1)(d-2) <= (4q-1)(4q-2)
                = 16q^2-12q+2
                < 16q^2-8q,

because the positive difference is `4q-2`. This contradicts (4). The
boundary `q=1` is included: (2) gives `d<=4`, whereas (4) demands at least
`8` on its left side, whose maximum in that range is `6`.

## 6. Outcome, limitations, and frontier impact

The proposed theorem passes the audit after making the following points
explicit: regularity is along a full component, not just generically;
the normal degree is computed in the regular formal surface; completion
along the component retains the same full local branch at its
intersection with the companion; and companion containment is an
algebraic consequence of local vanishing, rather than an assumed
equality `W|E=Z`.

This excludes an all-orders Cartier lift of the specified reduced equal
split root whenever its total formal surface is regular along `Z`.
It does not exclude a lift whose formal surface is singular at one or
more points of `D1 intersect D2`, roots with different component classes,
nonreduced roots, or any actual complete intersection without a separate
bridge to this exact formal-lift setting. In particular it supplies no
unrestricted characteristic-zero STCI conclusion.

Independent review has the scope stated above.
No new computation is needed for the argument, and no finite checks or
load-only CAS tests are offered as a substitute for the geometric proof.


---

## Source: 2026-10-19-regular-singular-root-smoothing-audit.md

# Independent audit: regular formal surfaces with singular movement-two roots

Date: 2026-10-19. Reviewer: `regular_singular_smoothing_audit`.

**Outcome: PASS for the precise conditional nonexistence statement below.**
The new smoothing step is valid. It closes the reduced singular-root case
only when the resulting formal surface is regular at every point of the
whole root. The argument does not establish that an arbitrary all-orders
Cartier lift, or an arbitrary actual complete intersection, has this
regularity property. No result has been changed by this audit.

## 1. Exact scope and authority

Work over an algebraically closed field `k` of characteristic zero with the
fixed rational quartic `C0` and the accepted balanced normal bundle
`N_(C0/P3)=O_P1(7)^2`. Put

    B=Bl_(C0)(P3), E=P1_base x P1_direction,
    O_E(E)=O_E(7,-1), H|E=O_E(4,0).

Let `r>=2`, and let `Z` be a **reduced effective Cartier divisor** of class
`(2,r)` on `E`, finite flat of degree `r` under the first projection
`p:Z->P1_base`. Suppose compatible embedded effective Cartier lifts of
`Z` on every exceptional neighborhood define a formal surface `Vhat` that
is **regular along all of `Z`**. Then such a lift does not exist.

The input [STCI-R-0005](../../results/smooth_root_formal_obstruction.md)
concerns a smooth full root; its [accepted independent audit](finite_root_families_and_smooth_obstructions.md#2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit)
supplies the algebraic branch, ruled-model degree, and plane-section
arguments used as premises here. This review checks their new interface
with a singular root and supplies the new smoothing argument. It does
not reopen the inherited proof or its accepted numerical inequalities.
[STCI-R-0011](../../results/moving_nonreduced_spectral_root_obstruction.md)
is not needed: ampleness and smoothing below hold for every finite-flat
root of the indicated class, including components of differing slopes.

## 2. Normal line, connectedness, and algebraization

Let `u` be an exceptional equation and `g` a local equation of `Vhat`.
Since `g mod u` cuts out the Cartier divisor `Z` in `E`, `u` remains a
nonzerodivisor on `Vhat`, and

    I_Z O_Vhat=(u,g)O_Vhat=(u),
    N_(Z/Vhat)=O_Z(E)=:N=O_Z(7,-1).

Thus the exceptional topology on `Vhat` is its `Z`-adic topology. In
particular it is a closed formal subscheme of `B` completed along `Z`.
Regularity of `Vhat`, rather than smoothness of `Z`, is the hypothesis
that gives a smooth formal surface over the perfect field `k`.

The exact sequence

    0 -> O_E(-2,-r) -> O_E -> O_Z -> 0

and Kunneth show `H0(O_Z)=k`, because `H0(O_E(-2,-r))` and
`H1(O_E(-2,-r))` vanish. Hence `Z` is connected. Each irreducible component
has class `(a,b)` with `0<=a<=2`; finiteness over the first factor gives
`b>=1`. Consequently

    deg(N|component)=7b-a >= 5.

The normal line is therefore ample on `Z`, without any descent or
equal-slope hypothesis. The finite-projection hypothesis matters here:
a vertical fiber of class `(1,0)` would instead have normal degree `-1`.

[Bost, Corollary 3.8, printed p. 188](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf#page=28)
allows a proper connected lci scheme of definition in a smooth formal
scheme and assumes its normal bundle ample; it does not require that
scheme of definition to be smooth. It gives an integral algebraic
closure `W` of dimension two containing the formal branch. The dimension
condition is `dim Z>=1`; the PDF text extraction renders its sign
incorrectly. This is the appropriate variant for singular `Z`.

## 3. Normalization still preserves the entire singular root

At a closed point `z` of `Z`, the maximal-ideal completion of the chosen
formal surface is regular of dimension two. It is a minimal completed
branch of the integral algebraic surface `W`. Excellence identifies the
completed normalization factors of `W` with the normalizations of its
completed branches. The selected branch is already normal and regular.
See [Stacks, Lemma 15.110.8 and its proof](https://stacks.math.columbia.edu/tag/0C2E).

The compatibility argument in the accepted smooth-root audit uses only
normality of the formal surface. On a normal-domain formal chart with
ring `R`, the algebraic coordinate domain of `W` injects into `R` through
the chosen minimal branch. Every element of its finite integral closure
maps into `Frac(R)` and is integral over `R`, hence belongs to `R`.
Uniqueness makes these maps agree on overlaps. The resulting morphism
`Vhat->Wnu` reduces to a section

    Z -> Wnu x_W Z -> Z.

Because normalization is finite, this section is a closed immersion.
Its image is a copy of the original `Z`, including its singularities,
and `Wnu` is regular along it. The formal neighborhood of that image is
the selected branch. This does not identify any additional branch of
`W` with it.

Resolve the projective normalization away from this regular neighborhood,
obtaining a smooth projective surface `T` containing the unchanged
Cartier curve `Z`. Resolution preserving a regular open is available
for surfaces; see [Stacks, Resolution](https://stacks.math.columbia.edu/tag/0BGJ)
and the accepted branch audit cited above. If `S` is the integral image
surface in `P3` and `H` is its hyperplane pullback to `T`, then

    Z^2=deg N=7r-2,   p_a(Z)=r-1,
    H.Z=4r,          H^2=d=deg S>0.

`W` is not `E`, since `u` is nonzero on the formal surface. Thus `W` is
the strict transform of `S` and the map to `S` is birational. `H` is nef.

## 4. Independent cohomology calculation

The divisor sequence tensored by `O_E(7,-1)` is

    0 -> O_E(5,-r-1) -> O_E(7,-1) -> i_*N -> 0.

Push this sequence along the first projection `p_E:E->P1`. Both direct
images of `O_E(7,-1)` vanish, while

    R1(p_E)_* O_E(5,-r-1)=O_P1(5) tensor H1(P1,O(-r-1)).

Since the latter vector space has dimension `r`, this gives the stronger
identity

    p_*N = O_P1(5)^r.                                      (1)

In particular

    H1(Z,N)=0,  H1(Z,N tensor p^*O_P1(-1))=0,
    h0(Z,N)=6r.

For a finite morphism, `p^*p_*N -> N` is surjective: on affine rings it
is the multiplication map `B tensor_A M -> M`. Equation (1) therefore
proves that `N` is globally generated. These assertions do not assume
that `Z` is integral or nonsingular. Equivalently, the two proposed
Kunneth computations have kernels `O_E(5,-r-1)` and
`O_E(4,-r-1)` respectively and give the same vanishings.

## 5. Smoothing on the fixed algebraic surface

This is the new step. Embedded deformations of the Cartier curve `Z` in
the smooth surface `T` have tangent space `H0(N)` and obstruction space
`H1(N)`. Local lifts exist by lifting a regular sequence. Thus the Hilbert
scheme of `T` is smooth at `[Z]`. For a source that explicitly covers a
singular lci subscheme, use [Hartshorne, *Lectures on Deformation Theory*,
Theorem 6.3 and its following remark, and Theorem 9.3](https://math.berkeley.edu/~robin/math274root.pdf#page=42).
The introductory Theorem 1.1 alone assumes a nonsingular subscheme and
would not by itself justify this application.

Choose a smooth integral neighborhood `A` of `[Z]` in the Hilbert scheme,
and let `U subset T x A` be its universal curve. After shrinking `A`, it
is a relative effective Cartier divisor. Locally, the universal ideal
reduces to the principal Cartier ideal `(f)` on the central fiber;
flatness and Nakayama lift its generator to a local equation `F`.
Properness lets these local neighborhoods cover every nearby fiber.
The relative Cartier criterion is [Stacks, Lemma 31.19.9](https://stacks.math.columbia.edu/tag/062Y).

At a closed point `z` of the central `Z`, choose parameters `t_j` on `A`
whose tangent vectors form a basis of `H0(N)`. Modulo the central ideal,
the coefficients `partial F/partial t_j` are precisely the evaluations
of those normal sections. Global generation gives one with nonzero value
at `z`. Hence `F` is not in the square of the maximal ideal of the smooth
ambient `T x A`, and `U` is regular, equivalently smooth over `k`, at `z`.
This also covers the original singular points of `Z`.

The nonsmooth locus of `U` over `k` is closed. Its image in `A` is closed
because `U->A` is proper, and it misses `[Z]`. Shrink `A` again to make
all of `U` smooth over `k`. The generic fiber of `U->A` is regular,
since its local rings are localizations of regular local rings of `U`.
Its field `k(A)` is perfect in characteristic zero, so this generic
fiber is smooth. The nonsmooth locus of the morphism `U->A` consequently
has proper closed image. There is a nonempty open of smooth fibers.
Here one must distinguish smoothness of the total space over `k` from
smoothness of its map to `A`; generic smoothness and properness supply
the latter only over a dense open. For the field-smoothness criterion see
[Stacks, Lemma 33.25.2](https://stacks.math.columbia.edu/tag/04QP).

Since `h0(O_Z)=1`, upper semicontinuity gives `h0(O_(U_a))<=1` near
`[Z]`; the fibers are nonempty, so this equals one. A smooth proper fiber
over algebraically closed `k` is therefore connected and integral.
See [Stacks, Lemma 36.32.1](https://stacks.math.columbia.edu/tag/0BDN).
Thus a nearby smooth connected curve `Z_a subset T` exists. The universal
Cartier family over connected `A` makes it algebraically equivalent to
`Z`, so

    Z_a^2=7r-2,   g(Z_a)=r-1,   H.Z_a=4r.                 (2)

No claim that this smoothed curve lies on the original exceptional
divisor, or that it yields a new embedded formal lift in `B`, is needed.
Its only role is to permit the established ruled-surface numerical
argument on `T` with the invariants (2).

## 6. Numerical contradiction and boundary

For `r>=2`,

    7r-2 > 4(r-1)+5.

Apply the accepted high-self-intersection and nef-divisor argument to
`Z_a subset T`. [Hartshorne, *Curves with high self-intersection on
algebraic surfaces*, Theorem 4.1](https://www.numdam.org/item/PMIHES_1969__36__111_0.pdf#page=12)
gives the ruled model near this smooth curve; the accepted intersection
argument gives

    d <= max_(a integer >=1) [8ra-(7r-2)a^2] = r+2.        (3)

For the opposing bound, use the **original** `Z`, not its smoothing.
Formal containment in `W` reduces modulo `u` to scheme-theoretic
containment `Z subset W|E`. The difference is effective on the smooth
surface `E`. Its generic fiber degree shows that the generic
multiplicity `m` of `S` along `C0` satisfies `m>=r`. Extra exceptional
components or other branches can only add effective fiber degree.
The accepted general-plane-section argument now gives

    (d-1)(d-2) >= 4m(m-1) >= 4r(r-1).                   (4)

But (3) gives `(d-1)(d-2)<=r(r+1)`, and

    4r(r-1)-r(r+1)=r(3r-5)>0  for every r>=2.

This contradiction passes the proposed exclusion.

The added hypothesis is regularity of the **whole formal surface**.
At a singular point of the reduced root, smoothness of the ambient
threefold and the Cartier property of the formal equation alone do
not imply it. If the formal equation is locally `g=f+u*a+...` with
`df=0` on `E`, regularity requires a nonzero linear contribution in
the transverse direction, for example `a(z)!=0`. The audit does not
prove that contribution exists for every root lift. Singular formal
surfaces remain outside this theorem, as do arbitrary actual complete
intersections without a bridge to the stated formal object.

The proof of Sections 2--6 in fact does not use reducedness once a
finite-flat effective Cartier `Z` of class `(2,r)` and a regular formal
surface are supplied: the component ampleness criterion, sequence (1),
and universal-family smoothing still apply. This is a transparent
scope strengthening of the argument, not a claim that nonreduced roots
in the actual STCI problem satisfy its regularity hypothesis.

## Review record

The reviewer independently reconstructed the normalization and smoothing
interfaces and both cohomology calculations. A separate subreviewer,
`smoothing_check`, checked the Hilbert universal-family argument and the
primary deformation, relative Cartier, and semicontinuity references.
No exact-CAS calculation, inherited proof rerun,
or git operation was used. The regularity boundary is unresolved by
this argument and remains a limitation of the argument.
