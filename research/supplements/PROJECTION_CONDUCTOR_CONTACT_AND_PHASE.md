# projection conductor contact and phase

Permanent complete mathematical dossier. The arguments, calculations, precise scope, corrected formulas and open cases are preserved without asserting any new theorem authority.

---

## 2026-10-14-generalization-projection-conductor-contact-budget

# A uniform conductor contact graph for Cartier normalization lifts

Date: 2026-10-14. Owner: `global_phase_duality`. Status: **NEW WRITTEN
STRUCTURAL THEOREM; independent review requested**. The accepted
[Cartier-lift classification](2026-10-14-generalization-cartier-lift-independent-audit.md),
[projective contact criterion](2026-10-14-generalization-projection-contact-phase-criterion.md),
and its uniform fiber-degree bound are premises, not computations to replay.
The new input is the actual canonical conductor ideal from the
[conductor--Jacobian bridge](2026-10-14-generalization-projection-conductor-jacobian-bridge.md).

## 1. General theorem

Let `nu:S->X subset P3` be a finite birational normalization of an
integral degree-`a` hypersurface over an algebraically closed field of
characteristic zero. Let `C subset X` be a smooth degree-`d`, genus-`g`
curve with full reduced inverse image a
single smooth ample Cartier curve `c`, mapped isomorphically to `C`.
Assume `X` is regular at the generic point of `C`. The Cartier-lift
lemma makes `S` regular along `c`. Put `H=nu*O_X(1)` and `k=c^2`.

Finite duality identifies the **actual** upstairs conductor ideal with
`omega_S tensor nu*omega_X^(-1)`. A normal surface is Cohen--Macaulay,
and its canonical sheaf is rank-one reflexive. Thus the conductor is
the divisorial ideal of an effective Weil divisor `B`:

    conductor O_S = O_S(-B),
    B ~ (a-4)H-K_S,
    N := B.c = d(a-4)+k-(2g-2).                    (1)

This statement identifies the actual ideal, not only its double dual;
there is no discarded zero-dimensional ideal defect. Globally `B`
need not be Cartier. It is Cartier near `c`, because `S` is regular
there, and this is enough to define `B|c` and its degree. Adjunction
near `c` proves the formula for `N`. If `S` is Gorenstein, `B` is
Cartier globally.

Write its effective Weil divisor as `B=sum_i m_i D_i`, with the `D_i`
distinct prime curves and `m_i>=1`. No `D_i` equals `c`, because the
normalization is an isomorphism at the generic point of `C`. Then

    sum_i m_i (D_i.c) = N.                          (2)

Every `D_i.c` is a strictly positive integer since `c` is ample.
Consequently:

* There are at most `N` prime conductor curves, and each generic
  conductor multiplicity `m_i` is at most `N`.
* If `D_i^nor` is the normalization of `D_i`, the sum of the vanishing
  orders of `c` on all its branches is `D_i.c`. Thus every such branch
  contact order, and the number of branches meeting `c`, is at most
  `N`; their sum with weights `m_i` is exactly `N`.
* The exact first-symbol bridge is

      Z(F_1) = B|c + A,                             (3)

  where `A` is the entire zero divisor of the normalization normal
  differential. In particular (2) concerns the full conductor contact,
  including multiplicities, rather than only its reduced support.

Here `F_1` is the actual first normal symbol of the carrier equation.
Identity (3) is conditional on the new bridge proof; the contact graph
bounds (1)--(2) use finite duality directly and do not depend on (3).

## 2. A bound on the entire off-diagonal pair correspondence

For every image conductor curve `Delta subset X`, let

    K=k(Delta),    E=product_(i over Delta) E_i,
    E_i=k(D_i),   d_Delta=sum_i [E_i:K].

The accepted fiber-degree argument gives `d_Delta<=a`. Characteristic
zero makes each extension separable. Fix a prime `D_i` over `Delta`.
The reduced generic algebra of all pairs with first entry on `D_i` is

    E_i tensor_K E,

of rank `d_Delta` over `E_i`. Its diagonal component is one factor
`E_i`, of rank one. Removing it leaves total rank `d_Delta-1`.
Normalizing and taking projective closures therefore gives finitely
many integral off-diagonal pair curves `T`, with finite first projection
`p_1:T->D_i`, satisfying the exact equality

    sum_(T with first image D_i) deg(p_1) = d_Delta-1 <= a-1. (4)

This includes conjugate pairs on one irreducible conductor curve as
well as pairs between different conductor curves. When `E=K` there
are no off-diagonal curves, consistent with (4). Generic nilpotents
are deliberately absent from this pair construction, but are retained
in the conductor divisor `B` and in the final full descent condition.

Pullback of the Cartier divisor `c` to each proper normal curve `T`
has total degree `deg(p_1)(D_i.c)`. Summing (4) over all first images
and then using (2) gives the uniform bound

    sum_T deg(p_1*c)
      = sum_i (d_(image D_i)-1)(D_i.c)
      <= (a-1) sum_i D_i.c
      <= (a-1)N.                                    (5)

The index `T` in (5) means the integral components of the **ordered**
off-diagonal pair correspondence. In particular a component invariant
under exchange is counted once as an integral component, rather than
being artificially doubled. The equality is the decomposition of
the finite algebra over each fixed first image, so there is no missing
conjugate-pair degree or extra factor of two.

Because `c` is ample, every `p_1*c` is a nonzero effective divisor.
Hence (5) bounds all of the following by `(a-1)N`: the number of pair
components, the number of their contact branches counted with
multiplicity, and any single contact order on their normalizations.
These quantities were not bounded by the size of the degeneracy
support alone.

## 3. The three surviving fixed-C0 models

The accepted normal splitting `N_C0/P3=O(7)^2` and transverse theorem
place every conductor contact in the support of `A`, whose degree
is at most five or six. Equations (1)--(5) supply the additional
global weighted bounds:

| Normalization and polarization | `B` class | `N=B.c` | `deg A` bound | Ordered pair contact budget |
| --- | --- | ---: | ---: | ---: |
| `P1 x P1`, `H=(2,2)`, `c=(1,1)` | `(10,10)` | 20 | 5 | 140 |
| Quadric cone, `H=2c`, `c` a smooth conic | `10c` | 20 | 5 | 140 |
| `P2`, `H=4h`, `c=h` | `51h` | 51 | 6 | 765 |

The quadric cone is Gorenstein, and `c` avoids its vertex. Thus its
global conductor class is Cartier and its local contact calculation
occurs entirely in the smooth locus. No resolution at the vertex is
being silently inserted.

These inequalities put the incidence into finitely many **combinatorial
weighted contact graph types**. Vertices can record the at most five or
six sites on `c`, the prime conductor branches and their positive
integer weights. Edges record ordered pair branches and their positive
contact orders, with total edge weight bounded by 140 or 765. The
actual curves, contact locations, correspondence maps and leading
coefficients still vary in families. Finitely many graph types do not
mean finitely many projection parameters or finitely many phase values.

## 4. Consequence for the general strategy and retained boundaries

The accepted projective criterion requires, on every pair curve `T`,
equality of the entire divisors `p_1*c` and `p_2*c`, followed by a
root-of-unity test on the resulting constant ratio. The new theorem
bounds the amount of integer contact data needed to formulate these
tests uniformly on each normalization model. It does not require
enumerating possible mate powers.

There is still no bound here on the order of a split scalar phase.
Even one edge with contact order one can carry an arbitrary-order
root of unity in the local split model. Canonical conductor duality
constrains that edge's integer contact data, not its scalar label.
The entire nilpotent logarithmic conductor defect must also vanish;
the reduced correspondence and (1)--(5) do not prove this vanishing.

The theorem applies more generally to any smooth ample Cartier lift
on a normal projective-hypersurface normalization, with the uniform
quantity `N` in (1). Global Gorensteinness is unnecessary: the actual
reflexive conductor ideal and smoothness along `c` suffice. For
non-Cartier lifts the contact divisor needs replacement; for a lift
through singular points of the normalization the local bridge needs
replacement; and for carriers generically
singular along `C`, the conductor can contain `c`, so its restriction
in (2) is not defined as an effective finite divisor. Those strata
are not covered by this theorem. It does not resolve the universal
integral-curve STCI problem or the unrestricted fixed-C0 problem.

No accepted certificate was rerun and no large CAS job was launched.


---

## 2026-10-14-generalization-projection-conductor-budget-independent-review

# Independent review of the canonical conductor contact budget

Date: 2026-10-14. Reviewer: `projection_global_continue`. Scope: the new proofs in
[the conductor--Jacobian bridge](2026-10-14-generalization-projection-conductor-jacobian-bridge.md)
and [the conductor contact budget](2026-10-14-generalization-projection-conductor-contact-budget.md).
Status: **PASS under the stated Gorenstein, smooth Cartier-lift, full-support,
and generic-regularity hypotheses**. The accepted Cartier-lift classification,
normal splitting, projective contact criterion, and fiber-degree bound are
premises. Their computations were not rerun.

## 1. Actual conductor and the local first-symbol identity

For a finite birational extension `A subset B` with common fraction field,
every `A`-linear map `B->A` is multiplication by a fraction. Consequently
`Hom_A(B,A)` is the actual conductor `{q:q B subset A}`, not merely its
reflexive hull or its divisorial support. Since `A` is Gorenstein and `B`
is Cohen--Macaulay, finite canonical duality gives

    omega_B = Hom_A(B,A) tensor_A omega_A.

On a Gorenstein normalization the two canonical modules are invertible. The
conductor is therefore an invertible ideal on the normalization. In the
projective hypersurface setting this proves

    conductor O_S=O_S(-B),  B~(a-4)H-K_S.

The new local bridge was independently reconstructed in completed regular
coordinates. Take source coordinates `(t,u)`, with `c=(u=0)`, and ambient
coordinates `(x,y,z)` with `C=(y=z=0)` and `nu*x=t`. Write `nu=(t,Y,Z)`.
If `h` generates the actual conductor and `eta=dx wedge dy/F_z` generates
the hypersurface dualizing module, then `h nu*eta` is a generator of
`omega_S`. Hence there is one common unit `epsilon` satisfying

    F_z composed with nu=epsilon h Y_u,
    F_y composed with nu=-epsilon h Z_u.

At least one of these rational residue expressions is available generically:
the map is birational and is an isomorphism at the generic point of the
hypersurface. The equalities extend in the regular local ring. Restriction
to `u=0` gives the exact DVR-ideal equality

    (F_y|C,F_z|C)=(h|c)(Y_u|c,Z_u|c).

Taking orders proves the entire divisor identity

    Z(F_1)=B|c+A.

This argument uses the actual invertible conductor before restricting to
`c`; it avoids the possible codimension-two error in restricting only a
Weil-divisor or reflexive-hull identity. It also keeps isolated zeros of
the transverse differential. Smoothness along `c` follows from the accepted
smooth Cartier-curve lemma. The quadric cone is Gorenstein and its smooth
Cartier conic avoids the vertex, so that model satisfies the hypotheses.

## 2. Integer conductor budget

Generic regularity along `C` ensures `c` is not a component of the effective
conductor divisor. With `B=sum m_i D_i`, ampleness and Cartierness of `c`
give positive integers `c.D_i`. Adjunction then gives the exact equality

    sum_i m_i(c.D_i)=B.c=d(a-4)+c^2-(2g-2)=N.

This bounds the number of prime conductor components, all positive
conductor multiplicities, and the total weighted branch contact with `c`.
The assertion includes the singular branches of each `D_i`: pulling the
Cartier section defining `c` to the normalization of `D_i` has divisor
whose total degree is exactly `c.D_i`.

For the smooth-quadric and quadric-cone models, `B=10c` and `N=20`; for
the plane model, `B=51h` and `N=51`. These are canonical intersection
computations, independent of a putative mate degree.

## 3. Ordered pair curves and the factor of two

Let `Delta` be a generic image conductor curve, `K=k(Delta)`, and
`E=product E_i` its reduced normalization residue algebra. For fixed first
branch `E_i`, the algebra `E_i tensor_K E` is finite etale over `E_i` in
characteristic zero, of rank `d_Delta=sum_j [E_j:K]`. Its diagonal factor
has rank one, including when `E_i/K` has nontrivial conjugates. The sum of
the first-projection degrees of all remaining factors is therefore exactly
`d_Delta-1`, not the number of field factors and not twice that number.

Using the accepted `d_Delta<=a` bound, and pulling back the Cartier contact
divisor to each normalized pair curve, gives

    sum_T deg(p_1*c)
      =sum_i(d_(image D_i)-1)(c.D_i)
      <=(a-1)sum_i c.D_i
      <=(a-1)N.

This counts integral components of the ordered off-diagonal fiber product.
An exchange-invariant integral component is counted once; exchange may act
nontrivially on its function field. Thus the displayed formula has neither
a missing conjugate-pair factor nor an unjustified factor of two. Every
summand is a positive integer, since the projected curve meets the ample
`c`. The bounds 140 and 765 on pair-contact data follow.

## 4. Mathematical consequence and scope

The result supplies a uniform finite amount of integer contact data for
all mate degrees on any one of the three fixed normalized models. It also
shows that the full conductor contact is recovered from the carrier first
symbol *and* the actual normalization differential, under the explicit
duality hypotheses. Neither first symbol alone nor a reduced common-root
support substitutes for this identity.

The theorem leaves the scalar phases unbounded and retains the entire
nilpotent conductor defect. Finite weighted graph types do not give finitely
many projection coefficients or a finite list of phase values. The
non-Gorenstein, non-Cartier, multiple-inverse-branch, and generically thick
boundaries remain outside its scope. This is an accepted structural
reduction, not an exclusion of all nonnormal carriers or a solution of the
universal STCI question.


---

## 2026-10-14-generalization-projection-contact-phase-criterion

# Projective contact divisors detect residual conductor torsion

Date: 2026-10-14. Owner: `projection_conductor_ray`. Status: **NEW
STRUCTURAL REDUCTION; independent review passed** in the
[written review](2026-10-14-generalization-projection-contact-phase-independent-review.md).
This uses the
accepted [Cartier-lift classification](2026-10-14-generalization-cartier-lift-independent-audit.md),
[full conductor theorem](2026-10-13-generalization-conductor-theorem.md),
and [transverse differential theorem](2026-10-14-generalization-transverse-socle-independent-audit.md)
as premises. None of their certificates is rerun. The result below
reduces residual function-field torsion to projective intersection
data and finitely many leading coefficients. It does not eliminate
the nilpotent conductor defect or bound root-of-unity orders.

## 1. Exact contact criterion

Let `nu:S->X` be a finite birational normalization of an integral
projective surface over an algebraically closed characteristic-zero
field `k`. Assume `X` is Cohen--Macaulay for the global descent
conclusions in Section 5; the residual contact criterion itself does
not require this extra hypothesis. Let `C subset X` be integral, with full reduced inverse
image a single smooth Cartier curve `c` mapped isomorphically to `C`.
Let `H=nu*L`, where `L` is ample on `X`, and assume that an upstairs
section `Q of H` has divisor

    div(Q)=m c,    m>0.                                    (1)

In particular `c` is ample. Let `eta` be a generic conductor point
whose curve is different from `C`. Write the actual reduced
normalization conductor algebra there as

    E=product_i E_i,    K=k(eta),

where each `E_i/K` is finite and separable. `Q` is a unit in the
entire conductor algebra at `eta`, because its zero divisor is
supported only on `c`.

For every component of the reduced geometric-pair correspondence
above `eta` whose two geometric entries differ, take its projective
closure in `S x_X S` and its normalization `T`. The projections
`p_1,p_2:T->S` are finite onto curves. There is a canonical
identification

    p_1*H=p_2*H,

because `nu p_1=nu p_2`. Thus the ratio

    rho_T=p_1*Q/p_2*Q

is a nonzero rational function on the proper integral normal curve
`T`, with exact divisor

    div(rho_T)=m(p_1*c-p_2*c).                             (2)

**Theorem.** The residual class of `Q` in `E*/K*` is torsion if and
only if, on all these finitely many correspondences:

    p_1*c=p_2*c as entire effective divisors;               (3)
    the resulting constant rho_T belongs to mu_infinity(k). (4)

Diagonal pair components have ratio one and require no test. An
off-C unibranch conductor with residual field `E=K` therefore has no
residual obstruction; its full nilpotent obstruction can still be
nonzero. Components dominating `C` are deliberately excluded from
this unit criterion. The accepted conductor theorem handles their
vanishing by a sufficiently large positive power. Consequently this
part of the theorem allows the carrier to be generically singular
along `C`; generic regularity is needed only in Section 3 below.

Proof. The divisor formula follows from (1) and the canonical
line-bundle identification. A rational function on a proper normal
integral curve over `k` has zero divisor exactly when it is a
nonzero constant: it and its inverse are then regular, and proper
integrality gives `H0(T,O_T)=k`. This proves the equivalence between
constant ratios and (3).

Choose a rational frame of `L` at `eta`, and write the residues of
`Q` as `alpha=(alpha_i) in E*`. A power `alpha^N` belongs to the
diagonal `K*` if and only if all its geometric values agree. In
characteristic zero, base change to a separable algebraic closure
of `K` identifies these values with the factors of `E tensor_K
Kbar`; the equality test consists exactly of the geometric-pair
ratios above. Hence residual torsion implies every `rho_T^N=1`.
Conversely, if all ratios are roots of unity, their finitely many
orders have a common multiple `N`. All geometric values of
`alpha^N` agree; faithful scalar descent then puts `alpha^N` in
`K*`. This is the desired residual torsion. No reduced test is used
to claim full conductor descent.

### A sharper single-field consequence

If `E` is one field, condition (3) on every conjugate-pair
correspondence already implies (4). To see this, pass to a finite
Galois closure `K'/K` and a representative `alpha in K'`. Constant
conjugate ratios give

    sigma(alpha)/alpha=chi(sigma) in k*.

Galois automorphisms fix `k`, so `chi` is a homomorphism from a finite
group to `k*`; its values are roots of unity. Thus the single-field
residual test is just equality of contact divisors. For several
fields, the constants comparing different field factors need not
be roots of unity. These relative split phases remain a real
condition and can have unbounded finite orders.

## 2. All residual information is read at contact points

Every `T` above meets `c` under either projection, since its image
is a curve and `c` is ample. Full inverse support implies

    supp(p_1*c)=supp(p_2*c).                               (5)

Indeed `p_1(t) in c` implies `nu p_2(t) in C`, so `p_2(t) in c`;
the reverse implication is identical. As `nu|c` is an isomorphism,
each such pair equals `(P,P)` for one point `P in c`.

Equality of supports (5) does not imply equality of multiplicities
in (3). An unequal contact order is an immediate all-power
exclusion: `rho_T` has a zero or pole, and no positive power can
become a constant. If the orders agree, one contact point suffices
to evaluate the constant ratio.

More precisely, choose a local equation `q` of `c` at `P`, a
uniformizer `z` on `T` at `t`, and write

    q(p_1(z))=beta_1 z^r+...,   q(p_2(z))=beta_2 z^r+...,
    beta_1 beta_2 != 0.

Using the same local frame of `O_S(c)` at the common point `P`,
equation (1) and the canonical `H` frame show

    rho_T(t)=(beta_1/beta_2)^m.                            (6)

The unit multiplying `q^m` has the same value at `p_1(t)=p_2(t)=P`
and cancels. Formula (6) is coordinate independent as a ratio. Thus
one computes the correspondence and its contact orders once, then
reads a residual phase from local leading terms; one does not
solve a separate power-membership problem for every mate degree.

For a component joining branch curves `D_i,D_j` with projection
degrees `e_1,e_2`, a useful necessary numerical test from (3) is

    e_1(c.D_i)=e_2(c.D_j).                                (7)

This total-degree equality is weaker than the required pointwise
contact-divisor equality and must not replace it.

## 3. Every contact lies at transverse degeneracy

Now also assume `X subset P3` and that `X` is regular at the generic
point of `C`. The accepted
transverse theorem supplies the generically nonzero map

    alpha:O_c(c)->N_C/P3

and its entire effective common-zero divisor `A`. Every contact
point of an off-C conductor correspondence lies in `supp(A)`.

Here is a local proof of the new assertion. If `alpha(P)!=0`, the
map `S->P3` is immersive at `P`: its tangent on `c` is injective,
and its transverse normal image is nonzero. The fibre of `nu` over
`nu(P)` is a singleton, by full inverse support and the isomorphism
on `c`. Let `R=O_X,nu(P)` and let `B` be the finite local
normalization algebra above it. Cotangent surjectivity from the
immersion gives `m_R B=m_B` by Nakayama. Thus `B/m_R B=k`; another
application of Nakayama to the finite `R`-module `B` says that `1`
generates `B`, so `R->B` is surjective. It is also injective, hence
an isomorphism. There is therefore no conductor curve through `P`
upstairs. Any contact with an off-C conductor curve forces
`alpha(P)=0`.

For the three accepted fixed-C0 Cartier-lift models this puts all
residual correspondence contacts at at most five or six points:

| Normalization and polarization | `m` | Maximum `deg(A)` |
|---|---:|---:|
| `P1 x P1`, `H=(2,2)`, `c=(1,1)` | 2 | 5 |
| Quadric cone, `H=2c`, `c` a Cartier conic | 2 | 5 |
| `P2`, `H=4h`, `c` a line | 4 | 6 |

These are numbers of possible distinct contact sites, bounded by
the degree of the **entire** degeneracy divisor. They do not bound
the number of correspondence branches, their contact orders, or
the orders of their constant phases. At a cone vertex the lift
curve does not pass through the singularity, because a smooth
Cartier curve forces the surface smooth along it; the proof above
is consequently valid in all three models.

## 4. A literal sixteen-parameter quadric correspondence

On `S=P1_(s:t) x P1_(u:v)`, put

    q=sv-tu,    c=(q=0),    Q=q^2,
    P0=s^2 u^2,
    P1=su(sv+tu)/2,
    P2=tv(sv+tu)/2,
    P3=t^2 v^2.

These restrictions to `c` are the prescribed literal quartic
coordinates `(s^4,s^3t,st^3,t^4)`. Every four-coordinate lift with
these fixed restrictions is uniquely

    U_i=P_i+q L_i,  0<=i<=3,
    L_i=a_i su+b_i sv+c_i tu+d_i tv.                       (8)

The sixteen coefficients are the entire projection family before
quotienting automorphisms. On the basepointfree finite birational
locus the image is an integral degree-eight hypersurface. This
parameterization uses the accepted restriction-sequence reduction;
the symmetric `P_i` make the two projections in the fibre product
particularly explicit.

### The first jets are precisely an arbitrary pair of quintics

The universal family has an explicit linear first-jet quotient. On
the chart `s=u=1`, write `t=x,v=x+n`, so `q=n`, and put

    f_i(x)=L_i|c=a_i+l_i x+d_i x^2,    l_i=b_i+c_i.

Normalize the image coordinates by `U0`. Their transverse derivative
at `n=0` is

    v1=1/2+f1-x f0,
    v2=(3/2)x^2+f2-x^3 f0,
    v3=2x^3+f3-x^4 f0.

Taking the derivatives of the two local normal equations
`X2-X1^3` and `X3-X1^4` gives

    a=f2-3x^2 f1+2x^3 f0,
    b=f3-4x^3 f1+3x^4 f0.

The balanced pair is

    A=a=f2-3x^2 f1+2x^3 f0,
    B=2b-3x a=2f3-3x f2+x^3 f1.                          (8a)

Both have degree at most five. This is an actual balanced normal
frame, including infinity. On the reciprocal source chart take
`x'=1/x` and `n'=1/(x+n)-1/x`; the reciprocal target curve
coordinate is `X2/X3`. Direct differentiation of the analogous
normal equations gives

    A_infinity=-x^(-5) B,    B_infinity=-x^(-5) A.          (8b)

The constant interchange of the frame does not change the common
zero divisor. Thus the homogenizations

    A_h(s,t)=s^5 A(t/s),    B_h(s,t)=s^5 B(t/s)

represent the entire normal map `O(2)->O(7)^2`, and its degeneracy
divisor is exactly the homogeneous gcd divisor of `A_h,B_h`, with
full multiplicity and infinity retained. When they are not both
zero its degree is at most five. When both vanish the projection
is generically nonimmersive along `c` and belongs to the separate
thick-carrier boundary.

The twelve coefficients `(a_i,l_i,d_i)` map **isomorphically** to
the twelve coefficients of the arbitrary pair `(A,B)`. In fact,
if `A=sum A_j x^j` and `B=sum B_j x^j`, the explicit inverse is

    d0=A5/2,         l0=(A4+3B5)/2,   a0=(A3+3B4)/2,
    d1=B5,           l1=B4,           a1=-(B3+3A2)/8,
    d2=-(A2+3B3)/8,  l2=A1,           a2=A0,
    d3=(B2+3A1)/2,   l3=(B1+3A0)/2,   a3=B0/2.             (8c)

The other four parameters `b_i-c_i` vary the coefficients of
`q^2` in the four `U_i`; they affect second and later jets while
leaving (8a) unchanged. This surjectivity is a statement about the
entire lift vector space. It does not say that every quintic pair
has a basepointfree, birational, full-support admissible projection,
or that a first-jet pair determines its conductor. Equations
(8a)--(8c) make the degree-one-through-five gcd strata and their
four independent higher-jet parameters explicit for further work.

The actual equality-of-image locus in `S x S` is defined by all six
minors

    U_i(P)U_j(P')-U_j(P)U_i(P'),    0<=i<j<=3.             (9)

For the residual test, remove the diagonal locus and take the
projective closure, then normalize each curve component dominating
an off-C conductor curve. Its contact divisors are obtained by
pulling back `q(P)=0` and `q(P')=0`. Under the canonical matching
of `H`, the ratio is

    rho_T=q(P)^2/q(P')^2,                                 (10)

with the equality-of-image scale included through that line-bundle
identification. If homogeneous representatives are used with
`U_i(P')=lambda U_i(P)`, the scalar version of (10) is
`lambda q(P)^2/q(P')^2`; omitting this factor would give the wrong
invariant. In a common target-coordinate frame, the formula is the
ratio of `q^2/U_i` on the two branches. At a contact point, the
scalar factor tends to one in the common source frame, yielding
the square of the contact leading-coefficient ratio in (6).

Taking the closure retains all contact points on the diagonal.
Reducing and normalizing (9) is used only for the residual-field
test; it does **not** compute the full conductor or its nilpotent
logarithmic defect. Full support is separately imposed by the
pullback ideal of literal `C0`, retaining every possible isolated
inverse point. The basepoint, finite-birational, full-support, and
entire conductor conditions remain mandatory throughout (8).

## 5. Exact integration with full conductor descent

For a fixed projection satisfying these hypotheses, with `X`
Cohen--Macaulay as in every hypersurface model here:

1. Compare the finitely many full contact divisors on the actual
   residual correspondences. Any mismatch excludes every mate.
2. Evaluate the resulting constant phases by (6). A non-root-of-
   unity split phase excludes every mate. Single-field components
   require no additional root-of-unity test after all conjugate
   contacts match.
3. If all residual classes are torsion, compute the full Artinian
   conductor logarithmic defects from the accepted conductor
   theorem. Each must vanish. A reduced correspondence cannot
   replace this step.
4. If the defects vanish, the conductor theorem gives eventual
   descent. When `X` is an integral hypersurface in `P3`,
   `L=O_X(1)`, and the carrier is generically regular along `C`, the
   minimum ambient mate degree is the exact residual order of `Q`.
   For the general polarized surface, the statement concerns the
   least descending tensor exponent rather than an ambient degree.

This is a finite geometric criterion on a **chosen** projection,
not an effective algorithm over arbitrary unspecified coefficient
fields, and not a proof that every parameter stratum is covered.
Root-of-unity membership still depends on the coefficient field;
its orders can be unbounded in a family. The accepted affine split
phase example is consistent with (6): arbitrary ratios of branch
slopes give arbitrary finite phases after squaring or taking fourth
powers. The new projective gain is that every residual component
must meet the ample lift and its entire function-field ratio is
controlled by its contact divisor and a leading coefficient at one
of at most five or six degeneracy points. This is a structural
target across all mate degrees, rather than a mate-degree search.

## 6. Evidence and next target

No large CAS job or accepted-certificate replay was launched for
this note. The displayed universal lift is a direct expression of
the accepted restriction sequence. The new assertions are the
contact-divisor torsion criterion, the single-field refinement,
the leading-coefficient formula, localization of contacts at `A`,
and the explicit arbitrary-quintic first-jet quotient. The independent
review checked all of these assertions and requested the explicit
ambient hypotheses adopted in Sections 3 and 5. It separately
reconstructed the reciprocal-chart normal transition and every
coefficient in the first-jet inverse.

The next genuinely global target is to determine whether an
admissible parameter choice in (8) can satisfy **all** contact
equalities while also having vanishing entire nilpotent defect.
One should organize that question by the degree-one-through-five
degeneracy strata and by the actual off-diagonal correspondence,
not by the possible powers of `Q`. The other two normalized models
admit the same contact criterion and retain their explicit
degeneracy bounds. The universal projective-curve STCI problem and
unrestricted fixed-C0 problem remain unresolved.

## 7. A uniform mate bound in the single-field sublane

There is a quantitative consequence for all projections in each
fixed model, rather than only one carrier. If `nu:S->X subset P3`
is finite with `nu*O_X(1)=H` and `H^2=a`, then at any point with
residue field `K` its normalization residue degrees obey

    sum_i [E_i:K] <= a.                                  (11)

Indeed, over `K`, choose a line through the corresponding `K`-point
of `X_K` that is not contained in `X_K`. Two target hyperplanes
cutting that line pull back to a proper zero-dimensional
intersection of two `H_K` divisors, of total length `H^2=a`.
The entire scheme fibre is a closed subscheme of that intersection,
so its length is at most `a`; its reduced residue degrees have at
most that sum. The infinite field `K` ensures such a line can be
chosen. This proof does not assume that the finite normalization
is flat.

Suppose now the carrier is generically regular along `C`, every
off-C generic conductor residual algebra consists of a **single**
field, and a mate exists. The accepted characteristic-zero theorem
then makes each exact local descent order divide its field degree.
Vanishing of the full logarithmic defects follows from actual mate
existence. The minimum mate degree is their least common multiple,
so (11) gives the uniform divisibility bounds

    degree-eight models:     b_min divides lcm(1,...,8)=840;
    degree-sixteen model:    b_min divides lcm(1,...,16)=720720. (12)

These are conservative uniform bounds, not assertions that those
large degrees are necessary or that checking them is a practical
computation. In particular, in this sublane it is enough to test
one fixed power `Q^840` or `Q^720720` on the **full** conductor,
rather than arbitrary powers: an existing mate forces that power
to descend, and descent of that power constructs a mate. This
last equivalence retains the nilpotent defect. A single reduced
test still cannot decide it.

The hypothesis that the carrier is generically regular along `C`
removes the separate conductor vanishing threshold on `C`. No
bound in (12) is asserted here for the thick-on-C boundary. No
split-conductor phase is bounded by (11): even two degree-one
residual fields can have an arbitrary-order relative root of
unity. The contact criterion in Sections 1--3 remains the exact
replacement for that false inference.

## 8. A deliberately preserved failed global phase construction

The [opposite-ruling normal form](2026-10-14-quadric-opposite-ruling-phase-normal-form.md)
gives the entire coefficient family for the specified pairing
`(x,0)<->(0,a x)` through one diagonal point. It retains arbitrary
four-vectors `D,E`; its branchwise phase is `a^(-2)`. This is a
new exact incidence subfamily and imposes no phase-order bound.

The especially sparse coefficient choice `D=W2,E=u W2` yields a
basepointfree finite projection, but the [full-support failure
shield](2026-10-14-quadric-opposite-ruling-phase-family-failure.md)
shows that it always has an extra off-diagonal inverse point above
the infinite endpoint of literal C0. The two boundary obstructions
would require simultaneously `u=0` and `u=1` to disappear.
Consequently it supplies no admissible fixed-C0 carrier. This
failure does not exclude the full `D,E` normal form: linearly
independent projected coefficient pairs can remove that particular
boundary obstruction. The entire full-support and nilpotent
descent problem remains for that broader family.


---

## 2026-10-14-generalization-projection-contact-phase-independent-review

# Independent review of the projective contact and phase criterion

Date: 2026-10-14. Reviewer: `quadric_phase_review`. Scope: the new arguments in
[the projection contact and phase note](2026-10-14-generalization-projection-contact-phase-criterion.md).
Previously accepted Cartier-lift, conductor, and transverse differential results
are premises; none of their certificates was replayed.

Status: **PASS for the new residual criterion and its stated refinements**, with
the ambient `P3` hypotheses made explicit wherever an ambient normal bundle or
mate degree is used. This is a fixed-carrier reduction, not an exclusion of all
projection parameters or a bound on split-phase orders.

## 1. Proper pair curves and the divisor calculation

For an off-`C` generic conductor point, the distinct geometric pairs in the
reduced algebra are represented by the components of the reduced fiber product
`S x_X S` that dominate the corresponding conductor curve. Their projective
closures are proper; normalizing each integral curve component produces a
proper integral normal curve `T`. Each projection to `S` is finite because the
normalization map `S->X` is finite and both projections of the fiber product
are finite. The common composite to `X` canonically identifies `p1*H` and
`p2*H`.

Consequently the nonzero section ratio is a rational function, and

    div(rho_T)=m(p1*c-p2*c).

The entire contact divisors must agree, not just their degrees or supports. On
a proper integral normal curve over an algebraically closed field, a rational
function with zero divisor and its inverse are regular; hence it is a constant
in `k*`. This establishes the equivalence between contact-divisor equality and
constancy without a degree-of-mate search.

In characteristic zero, the finite residual fields are separable. After a
separable scalar extension the equality of all geometric values of a tuple
`alpha in product E_i*` is exactly the condition that it belong to the diagonal
`K*`. Thus all pair ratios being roots of unity is equivalent to some positive
power of the tuple being diagonal: take a common multiple of the finitely many
orders and descend the equality of geometric values. This checks both
directions of the residual torsion criterion.

Components lying over `C` are excluded from this unit test. Their images of
`Q` in the generic normalization conductor quotient are nilpotent, since
`div(Q)=m c`, and all sufficiently large powers vanish there. For the subsequent
global descent assertion, require `X` Cohen--Macaulay, as in the accepted
conductor theorem; this is automatic for the integral hypersurface models.
The accepted absence of closed-point associated primes in the normalization
quotient then allows generic conductor membership to give global membership.
This does not remove any off-`C` nilpotent obstruction. The residual contact
criterion itself does not require the Cohen--Macaulay hypothesis.

## 2. Single-field refinement and leading coefficients

For one residual field, pass to its finite Galois normal closure `K'/K`.
Constancy of every conjugate-pair ratio gives

    sigma(alpha)/alpha=chi(sigma) in k*.

Every Galois automorphism fixes `k`. Therefore `chi` is a character of the
finite Galois group; its values are roots of unity. The single-field residual
torsion condition is thus precisely equality of all conjugate contact
divisors. The accepted Kummer theorem subsequently gives the sharper order
dividing the actual residue-field degree. Constants comparing different
field factors have no such automatic finite-group constraint.

The ample divisor `c` meets each projected pair curve. Full inverse support
and injectivity of `c->C` imply that contact pairs are `(P,P)` and that the two
effective contact divisors have identical support. Their multiplicities can
still differ. If a local equation of `c` pulls back as

    beta1 z^r+...,  beta2 z^r+...,

then, in the common target frame, the unit in the local expression of `Q`
has the same value at the two projections and cancels. The phase is exactly

    (beta1/beta2)^m.

This formula is invariant under changing the local curve equation, pair-curve
uniformizer, or source frame. It supplies no order bound for a split phase.

## 3. Localization at the transverse zero divisor

Here the surface must be embedded in `P3`, the curve must be smooth there,
and the carrier must be generically regular along `C`, as in the accepted
transverse theorem. If the normal differential is nonzero at `P`, its normal
image is independent of the tangent to `c`; the map to `P3` is immersive at
`P`.

The local normalization algebra above `nu(P)` is finite and local because the
fiber is a singleton. Surjectivity on cotangent spaces gives

    m_R B=m_B

by Nakayama on the finitely generated `B`-module `m_B/m_R B`. Hence
`B/m_R B=k`. A second use of Nakayama, now on the finite `R`-module `B`, says
that `1` generates it. The injective birational map `R->B` is consequently
surjective and an isomorphism. No conductor curve can meet `P`. Every contact
therefore belongs to the support of the entire transverse degeneracy divisor
`A`.

The resulting bounds of five or six distinct sites in the three accepted
Cartier-lift models bound contact sites only. They bound neither numbers of
pair components nor contact multiplicities nor orders of scalar phases.

## 4. The literal quadric family and ambient degrees

The displayed sections `P_i` restrict to the literal four quartic monomials.
The accepted restriction sequence identifies its kernel with `q H0(O(1,1))`,
so `U_i=P_i+q L_i` is the whole sixteen-parameter family, with unique `L_i`.
The six equality-of-image minors define the actual pair locus before taking
off-diagonal closures.

The invariant phase in homogeneous representatives requires the scale factor:
if `U_i(P')=lambda U_i(P)`, then

    rho_T=lambda q(P)^2/q(P')^2.

Indeed a common target-coordinate frame gives
`(q(P)^2/U_i(P))/(q(P')^2/U_i(P'))`. Omitting `lambda` would make the formula
depend on the homogeneous representatives. At a contact pair `(P,P)`,
compatible local source frames make its limiting value one, agreeing with the
leading-coefficient formula.

For a general polarized surface the result gives descending exponents. To
identify the smallest descending exponent with the smallest ambient mate
degree, require an integral hypersurface `X subset P3`, `L=O_X(1)`, the
degree-one normalized section `Q`, generic regularity along `C`, and vanishing
of all off-`C` logarithmic conductor defects. Under these hypotheses the
accepted conductor result identifies the exponent with the common exact
residual order. Ambient forms represent all sections of `O_X(b)`, so this is
the mate degree. These scope restrictions are necessary.

## 5. The exact first-normal-jet map

The new first-jet formulas in the owner note were checked directly, without
calling an inherited certificate. On the chart `s=u=1,t=x,v=x+n`, write
`f_i=L_i|c=a_i+l_i x+d_i x^2`, with `l_i=b_i+c_i`. Normal differentiation in
the target affine chart gives

    a=f2-3x^2 f1+2x^3 f0,
    b=f3-4x^3 f1+3x^4 f0.

Balancing by `A=a`, `B=2b-3x a` cancels the potential degree-six term:

    B=2f3-3x f2+x^3 f1.

In the reciprocal source chart, the normal parameter is
`n'=1/(x+n)-1/x=-n/x^2+O(n^2)`. With target base parameter `Y=X2/X3`,
the corresponding two unbalanced target conormal derivatives, measured
against the old `n`, are

    x^-7(2b-3x a),    x^-8(3b-4x a).

Changing to differentiation against `n'` multiplies both by `-x^2`.
The same balancing in the reciprocal chart gives exactly

    (A_infinity,B_infinity)=-x^-5(B,A).

Thus the two quintics represent the map `O(2)->O(7)^2`, after a fixed
swap of the balanced frame on the reciprocal chart. Both the normal-source
factor and target-coordinate scale are included in this calculation.

For coefficients numbered from zero through five, direct extraction gives

    A=(a2,l2,d2-3a1,2a0-3l1,2l0-3d1,2d0),
    B=(2a3,2l3-3a2,2d3-3l2,a1-3d2,l1,d1).

These equations invert as

    d0=A5/2, l0=(A4+3B5)/2, a0=(A3+3B4)/2,
    d1=B5, l1=B4, a1=-(B3+3A2)/8,
    d2=-(A2+3B3)/8, l2=A1, a2=A0,
    d3=(B2+3A1)/2, l3=(B1+3A0)/2, a3=B0/2.

The twelve-dimensional first-jet map is therefore an isomorphism in
characteristic zero. Its four-dimensional invisible kernel in the sixteen
projection parameters is precisely the four `q^2` variations supplied by
`b_i-c_i`. The homogeneous greatest common divisor of `A,B` supplies the
entire first differential zero divisor, including its point at infinity.
If both quintics vanish identically, the map is not generically transverse;
the zero-pair case must remain separate from a finite-degree gcd stratum.

## 6. Uniform residual-field bound for the fixed normalized models

The additional single-field corollary was independently checked. Suppose a
finite map from the fixed polarized surface to `P3` is birational onto its
integral image, of degree `a=H^2`. At any generic conductor point `eta`, put
`K=k(eta)` and regard that point as a `K`-point of `X_K`. Since `K` is infinite,
one may choose a `K`-line through it that is not contained in `X_K`. Its two
defining hyperplanes pull back to divisors of `H_K` meeting properly in a
zero-dimensional scheme of total length `H^2=a`. The entire scheme fiber above
the chosen point is a closed subscheme of this intersection. Therefore

    sum_i [E_i:K] <= length(fiber) <= a.

This includes possible nonreduced fibers; it bounds the reduced residual
degrees by the entire fiber length and does not identify the two.

For the quadric targets `a=8`, and for the plane target `a=16`. If every
off-`C` residual algebra is a single field, the carrier is generically regular
along `C`, and all full logarithmic defects vanish, the exact minimum
descending exponent is the least common multiple of local residual orders.
Each such order divides an actual residue-field degree at most `a` by the
accepted single-field theorem. Consequently

    b_min divides lcm(1,...,8)=840       (quadric models),
    b_min divides lcm(1,...,16)=720720   (plane model).

This is a conditional uniform bound across those single-field projections,
not an existence assertion. Split residual products are expressly excluded
from this numerical corollary: their relative scalar phases are not bounded
by the reduced fiber degree.

## 7. What remains

The reduced pair correspondence detects residual torsion only. The full
Artinian conductor logarithmic defects, basepoint-free and birational
conditions, and full inverse support—including isolated extra inverse
points—remain mandatory. This review does not replace them by contact
equalities. It confirms a structural criterion across all powers of one
chosen primitive ray; it does not resolve the unrestricted fixed-`C0` or
universal projective-curve STCI questions.


---

## 2026-10-14-generalization-projection-ray-and-split-phase-model

# Projection rays, a global five-coordinate lead, and an exact split-phase shield

Date: 2026-10-14. Owner: `global_structure`. Status: **EXACT REFORMULATION
AND NEW LOCAL EXAMPLE; GLOBAL EXCLUSION OPEN**. Accepted classification
and conductor results are used without reruns.

## 1. The finite-dimensional projection spaces

The [Cartier-lift theorem](2026-10-14-generalization-cartier-lift-minimal-degree.md)
leaves three fixed-C0 models after accepted quartic exclusion:

    smooth quadric, H=(2,2), c=(1,1);
    quadric cone, H=2c, c smooth Cartier conic;
    plane, H=4h, c a line.

All have a primitive normalized section `Q in H0(S,H)` with divisor
`2c` or `4c`, respectively. The normal mate ray is precisely `Q^b`.
This is already a reduction of all mate degrees to one distinguished
section, but descent of its powers remains a global problem.

Fix the isomorphism of `c` with the literal C0 parametrization, and
write `W=span(s^4,s^3t,st^3,t^4)` in `H0(c,O(4))`. For a smooth
quadric, restriction

    H0(S,O(2,2)) -> H0(c,O(4))

is surjective and has kernel `H0(O(1,1))`, of dimension four. For
the plane with `H=4h`, its kernel is `ell H0(O(3))`, of dimension
ten, where `ell=0` is `c`. The same cone dimension is four, obtained
from its Cartier sequence. Once a splitting of restriction is fixed,
every four-coordinate subspace mapping isomorphically to `W` is the
graph of a linear map from `W` to this kernel. Thus the parameter
spaces before quotienting surface symmetries have affine dimensions
16 for either degree-eight model and 40 for the degree-sixteen model.

Four sections must have no base point. Since `H` is ample, their
resulting morphism is automatically finite: a positive-dimensional
fiber would have zero `H` degree. Birationality onto the image is an
additional condition. On that locus the model is the actual finite
normalization, and the image degrees are eight or sixteen.

The full support condition is exact and finite-dimensional: pull back
the actual generators of `I_C0` through the four sections and require
the radical of their sheaf ideal on `S` to be `I_c`. This retains every
extra isolated inverse point and every extra prime. It is not implied
by the fixed restriction to `c`.

## 2. Exact section-ring condition and what it does not bound

Let

    B=direct_sum_(b>=0) H0(S,bH),
    R=k[U0,U1,U2,U3] subset B,

where the four actual projection sections generate `R`. The carrier
is a hypersurface in P3, so its ambient degree-`b` forms supply all
sections of `O_X(b)`, by `H1(P3,O(b-a))=0`. Consequently

    a mate of degree b exists iff Q^b belongs to R_b.        (1)

When the projection is finite birational, `B` is a finite graded
module over `R` (it is the section module of the finite coherent
normalization algebra), and `Q` lies in the common fraction field.
The intermediate algebra `R[Q]` is finite birational. Thus (1) is an
actual power-membership condition in one finite ambient module,
equivalently the full conductor descent of one primitive ray.

The conductor theorem compresses single-field residual algebras.
Split residual products instead retain scalar root-of-unity phases.
Finite-dimensional parameter spaces or a finite normalization module
do not by themselves bound the orders of those phases. The exact
example below preserves full support and a smooth degree-one lift,
so these hypotheses cannot silently remove the phase problem.

## 3. An entire split-conductor affine example with unbounded phase order

Choose nonzero distinct `alpha,beta` in an algebraically closed
characteristic-zero field. Set `lambda=alpha+beta`, `mu=alpha beta`,

    B=k[u,v],
    y=v^2-lambda u v,
    h=y+mu u^2=(v-alpha u)(v-beta u),
    z=v h,
    A=k[u,y,z] subset B.

Put `R0=k[u,y]`. The equation `v^2-lambda u v-y=0` makes `B`
finite free of rank two over `R0`, and

    B=R0 direct_sum R0 v,
    A=R0 direct_sum h R0 v.

The latter is closed under multiplication because
`(hv)^2=yh^2+lambda u h(hv)`. Away from `h=0`, `v=z/h`, so the
extension `A subset B` is finite birational; normal `B` is its
normalization. The actual integral affine carrier is the hypersurface

    z^2-lambda u h z-y h^2=0,    h=y+mu u^2.                 (2)

Its conductor is exactly `hB`. To see this, an element `a+bv` belongs
to `A` exactly when `b in hR0`; requiring its product with `v` to
belong to `A` then forces `a+b lambda u in hR0`, hence `a in hR0`.
Thus the entire conductor square is

    A/hB=k[u],
    B/hB=k[u,v]/((v-alpha u)(v-beta u)),

with downstairs ideal `(h,z)` and upstairs divisor the two actual
lines `v=alpha u` and `v=beta u`. The upstairs curve is reducible,
with the two lines meeting at `(0,0)`; no nilpotent or intersection
data is dropped. Their maps to the downstairs line agree in the
coordinate `u`.

Let `C` downstairs be `y=z=0`. Its full reduced inverse image is
exactly the smooth line `c:v=0`, mapped isomorphically by `u`.
Indeed if `v!=0`, the first equation forces `v=lambda u`, and the
second then forces `mu u^2=0`, contradicting `mu!=0` and `v!=0`.
At `u=0` the only inverse point is still `v=0`; no isolated extra
normalization point appears.

For any fixed positive integer `q`, put `Q=v^q`. Modulo the entire
conductor its two restrictions are

    alpha^q u^q,   beta^q u^q.

Therefore the exact full-ring criterion is

    Q^n in A iff alpha^(q n)=beta^(q n).                      (3)

For sufficiency, if the two constants agree, the conductor residue
is the diagonal polynomial `alpha^(qn)u^(qn)` in `k[u]`; subtracting
it leaves an element of `hB subset A`. Necessity is immediate from
the two generic restrictions. Thus (3) includes the intersection
point and the entire conductor, not just a generic unit test.

Choose `alpha/beta` to be a root of unity of order `N`, with
`gcd(N,q)=1`. Then the smallest descending positive power is exactly
`n=N`, which is unbounded while the formulas (2) have fixed degrees
and the smooth singleton lift is unchanged. The primitive-like
orders `q=2` or four therefore do not bound split phases locally.

This is an affine example with a line support. It is **not** a
projective fixed-C0 carrier or a counterexample to any accepted
projective theorem. It proves that a proposed global argument must
use global projectivity, polarization or the actual fixed-C0
projection geometry in addition to these local support conditions.

## 4. Five-coordinate viewpoint: a concrete global lead

Adjoin `Q` to the four projection sections. Since the original four
generate `H`, the five also do, and their map has a finite image

    Y subset P4,  coordinates [U0:U1:U2:U3:Q].

Projection from the fifth-coordinate point is finite birational
`Y->X`. The hyperplane `Q=0` has scheme pullback `2c` or `4c`, and
the reduced curve there is the prescribed fixed C0.

For any scalar `zeta`, let `T_zeta` scale just the fifth coordinate.
At a split conductor identification where the `U_i` agree and the
two `Q` values have ratio `zeta`, the corresponding branch curves
are contained in `Y intersect T_zeta(Y)`. A mate requires these
phase ratios to be constant roots of unity and requires full
Artinian conductor membership as well.

This is a geometric reformulation, **not a proved exclusion**.
The shared hyperplane curve occurs for every `zeta`, so a naive
intersection-degree count must first separate that forced common
component from the additional branch curve. The local example above
shows why neither low coordinate degree nor isolated ramification
alone makes all `zeta` have bounded order. A useful new theorem
would have to couple the extra common curves to the actual
hyperplane multiplicity, global canonical/conductor divisor, or
prescribed C0 parametrization.

The separately written [transverse differential/socle theorem](2026-10-14-generalization-transverse-differential-socle-bound.md)
already supplies one global coupling: on a generically regular
carrier, every surviving projection requires a nonzero common-zero
divisor of the transverse differential, with bounded degree five
or six and a quantitative conductor-contact budget. Classifying
those root strata while preserving the split phase model is the
next structural target. No mate-power search has been started.


---

## 2026-10-14-generalization-projection-finite-phase-space

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
