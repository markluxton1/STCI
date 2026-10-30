# NORMAL BOUNDARY WEIGHTED INITIALS AND LIFTING

Permanent subject consolidation. All source mathematical detail retained with its original conditional and audited status; no new theorem promotion.


---

## boundary-repair-global-lifting

# Can the boundary repair the actual global lifting obstruction?

Date: 2026-10-26. Status: provisional structural continuation, with
[independent review](2026-10-26-boundary-repair-global-lifting-audit.md).
No canonical promotion, new exclusion, or homogeneous realization is claimed.
No isolated example or sampled pair is used.

Continuation, October 27: the
[one-step equation-module comparison](2026-10-27-one-step-boundary-obstruction.md)
proves the proposed repair principle for a fixed lower embedded
thickening and identifies exact vanishing at the final Gorenstein step.
It does not settle a comparison for arbitrary ambient obstruction complexes.

## 1. The general question worth answering

The preceding [genus account](2026-10-26-normal-torsion-spectral-genus-budget.md)
and [intrinsic initial construction](2026-10-26-weighted-initials-normal-boundary.md)
make boundary indices measurable, but have not shown that those indices
control the obstruction to realizing two actual homogeneous equations.
The next target is a comparison theorem between an allowed boundary
modification and a genuine global lifting problem.

For the line/socle budget, assume a proper CI Z of degrees (a,b) in P3,
sole smooth reduced support C, and generic transverse algebra K[y]/(y^m).
Then its saturated layers W_i=L^i(D_i) satisfy the inherited pairing
D_i+D_(m-1-i)=D_soc, with D_0=D_1=0. In particular 0<=D_i<=D_soc, and

    O_C(D_soc)=omega_C tensor O_C(4-a-b) tensor L^(-(m-1)).

The degree delta of D_soc is fixed once (a,b,m,L) are fixed. This is a
specific linear system and paired divisor data, not just an arbitrary
collection of punctual lengths. The higher-rank normal-layer account is
needed when the generic transverse algebra has embedding dimension two.

## 2. A precise repair criterion on any smooth projective curve

Let V be a vector bundle on a smooth connected projective curve C over
an algebraically closed field, and let o in H^1(C,V) be an identified
linear lifting obstruction. For effective D put Q_D=V(D)/V. The exact
sequence

    0 -> V -> V(D) -> Q_D -> 0

gives

    o maps to zero in H^1(V(D))
      iff o belongs to image(H^0(Q_D) -> H^1(V)).          (1)

Thus a permitted pole divisor repairs o exactly when its principal parts
can supply o. A cohomology class does not itself have a zero divisor.

By functorial Serre duality, the dual map to H^1(V) -> H^1(V(D)) is

    H^0(V^vee tensor omega_C(-D)) -> H^0(V^vee tensor omega_C).

Consequently (1) is equivalent to

    o annihilates H^0(V^vee tensor omega_C(-D)).          (2)

This is an exact criterion in arbitrary characteristic. The standard
duality input is [Stacks, section 53.4](https://stacks.math.columbia.edu/tag/0E31).
For varying D on a general curve, use the principal-parts incidence
and cohomology/base-change strata; no unqualified closed-locus assertion
across jumping cohomology dimensions is needed.

## 3. On P1, all repair divisors at once give a kernel test

Suppose V=O_P1(-r), r>=2, and n=r-2. Regard o as a linear functional on
H^0(O(n)) by Serre duality. A divisor D of degree B is the zero divisor
of some nonzero h in H^0(O(B)). For B<=n, the subspace in (2) is

    h H^0(O(n-B)) subset H^0(O(n));

for B>n it is zero. Define the multiplication matrix

    C_(B,o): H^0(O(B)) -> H^0(O(n-B))^vee,
    h |-> (g |-> o(hg)),                                (3)

interpreting H^0 of a negative line bundle as zero. Then

    some effective D of degree at most B repairs o
      iff ker C_(B,o) is nonzero.                       (4)

One can pad a divisor to obtain degree exactly B; further twisting
preserves vanishing. Conversely a nonzero kernel element cuts out an
effective degree-B divisor and satisfies (2). Repeated roots of h include
all nonreduced boundary divisors automatically. This is a statement about
an entire divisor family, not a pointwise experiment. It is often called
a catalecticant/multiplication test; its proof here is (1)--(3).

It also gives an immediate limit on the method. If

    B>=floor(r/2),

the source of (3) has dimension B+1 greater than the target dimension
max(r-1-B,0). Every obstruction then has a repair by SOME arbitrary
degree-B divisor. A single line-bundle obstruction cannot exclude using
that relaxed pole allowance. This does not show that an actual boundary
with the required paired divisors and global-source restrictions exists.

For V=direct_sum_i O(-r_i), discard summands with H^1=0, and stack

    C_(B,o): H^0(O(B))
       -> direct_sum_i H^0(O(r_i-2-B))^vee.              (5)

The SAME h must kill every component. Its nonzero kernel is exactly
simultaneous repair by one divisor. Testing each component with its own
divisor discards this common-support and common-multiplicity condition.
Multiple lifting classes can be stacked in the same manner when the
same modification is required to repair them. On fixed splitting-type
strata, (5) is a universal matrix on the actual obstruction parameter
family; full-column-rank and its failure are finite algebraic conditions.

## 4. The unproved comparison needed for our multiple curves

The following is a RESEARCH TARGET, not a consequence of the repair lemma:

    At a specified lifting stage, actual realizations with boundary
    D_soc induce a morphism of obstruction problems in which the
    obstruction o in H^1(V) becomes zero after a controlled modification
    V subset V' subset V(c D_soc), for an explicit integer c.

Proving this requires identifying the lifting complex and how saturation
changes it. There is a reason to try it. For saturated line layers,

    Hom(W_i,W_j)=L^(j-i)(D_j-D_i)
      subset L^(j-i)(D_soc).

Tensor constructions similarly give explicit multiple-divisor bounds.
These inclusions suggest possible correction bundles, but do NOT prove
that an actual realization kills the relevant obstruction in them. The
map between the lifting problems is essential. Depending on the stage,
several correction bundles or different multiples c may be necessary.

After this comparison, (1)--(5) provide necessary tests. Allowing every
divisor of degree c delta is a safe relaxation of allowing only c D_soc
with D_soc in its prescribed linear system. Failure even in the relaxed
test excludes all permitted repairs. Passing it does not prove an actual
correction or a lift: the restricted divisor, paired D_i, nonlinear
equations and actual global source may still fail.

Neither ordinary torsion T_n nor spectral comparison Delta is to be
identified with a pole allowance without proving this bridge. The
existing promoted [R0016](../results/nonsaturated_first_relation_resultant.md)
and [R0019](../results/quasiprimitive_residual_cycles.md) already give
specific conditional divisor comparisons. They are precedents with their
own hypotheses, not authority for the proposed general comparison above.

## 5. Preserve the actual homogeneous source throughout

Let I=I_C and d a carrier degree. The actual finite normal-jet image is

    U_(d,N)=image[H^0(I(d)) -> H^0((I/I^(N+1))(d))].

The ideal-sheaf exact sequence gives the exact description

    U_(d,N)=ker[H^0((I/I^(N+1))(d))
                  -> H^1(P3,I^(N+1)(d))].              (6)

Likewise the possible first nonzero symbols of order n are

    V_(d,n)=image[H^0(I^n(d)) -> H^0(C,Sym^n E(d))]
           =ker[H^0(C,Sym^n E(d))
                  -> H^1(P3,I^(n+1)(d))].              (7)

Separate choices in the V_(d,n) do not imply one compatible finite jet
in U_(d,N). A next-jet lift also has the exact kernel bundle sequence

    0 -> Sym^N E(d) -> (I/I^(N+1))(d)
          -> (I/I^N)(d) -> 0,

whose connecting class lies in H^1(C,Sym^N E(d)). This is one explicit
kind of genuine linear lifting class; other relation/ideal lifting
problems require their own correct targets and maps.

The universal objects should range over admissible lower lifts and
boundary data while imposing (6) for both carrier degrees. Their unknown
coefficients remain constants in k. A generic nonzero obstruction only
excludes a dense open locus; its zero locus must still be studied.
An isolated successful or failed lift does not settle the family.

## 6. An exact finite endpoint for a fixed degree pair

For actual proper global F_a,G_b containing an integral C of degree d,
suppose d divides ab and put M=ab/d. At the generic point of C, let
R=O_(P3,eta_C), with maximal ideal m. Then

    Z_red=C iff length_R R/(F,G,m^(M+1))=M.              (8)

Proof: properness gives a finite generic transverse length m_C, and
Bezout bounds d m_C<=ab. An Artin local algebra of length m_C has
nilpotent maximal ideal of exponent at most m_C. Since m_C<=M, the
truncation in (8) already retains its full length. Equality m_C=M
exhausts degree ab; any residual curve would have positive degree, and
purity of the complete intersection rules out embedded components.
The converse follows in the same way from degree exhaustion.

After a chosen formal coefficient/normal chart, (8) is a finite matrix
rank condition including ALL truncated multiples of F,G. The length
criterion itself is intrinsic. The residue field K=k(C) is not asserted
to be a canonically embedded coefficient field in R/m^(M+1).

Over the universal proper-pair open set in
P H^0(I(a)) times P H^0(I(b)), the finite rank equations concern actual
global coefficients. Fixed coordinate denominators can be cleared and
rational-function identities expanded into finitely many k-equations.
This gives an exact fixed-degree question across all pairs, rather than
a sampled example. It supplies no uniform bound on carrier degrees.

## 7. What the outcomes would teach

- If no permitted boundary repairs any actual-source obstruction on a
  stratum, we obtain an exclusion of that entire stratum.
- If repair occurs only on a proper determinantal locus, it identifies
  precisely which degenerations remain; it is not a universal exclusion.
- If dimensions force repair for every class in the relaxed test, the
  isolated obstruction/pole budget is structurally too weak. Shared
  divisors, actual source images or higher relations must carry the work.
- If abstract repairs exist but (6) fails, the issue is homogeneous
  realization. If (6) passes but the multiplicative lift fails, the
  missing information is filtered ideal/algebra compatibility.
- If the exact final locus (8) is proved nonempty within the proper-pair
  open set, it gives actual fixed-degree existence, unlike survival of
  a lower-order necessary condition.

The first substantive target is the controlled-modification comparison
in section 4, followed by the common-divisor test for its actual
obstruction family. A computation is warranted if it determines a
universal map, proves its rank/zero locus, or exposes a mechanism that
persists on a stated family. No new isolated example is needed here.



---

## weighted-initials-normal-boundary

# Weighted initial ideals over the coefficient curve

Date: 2026-10-26. Status: provisional continuation, with
[independent review](2026-10-26-weighted-initials-normal-boundary-audit.md).
No canonical promotion or STCI exclusion is claimed.

## Question and inherited scope

The question is about all weighted initial ideals, including those that
contain monomials, rather than only the monomial-free tropical locus.
Let C be smooth over algebraically closed k, K=k(C), and choose rational
normal coordinates X,Y. A point p below means a closed point of C.
Characteristic is arbitrary for the local example.

The [October 23 coefficient-valuation note](2026-10-23-intrinsic-coefficient-valuations.md)
and its [review](2026-10-23-intrinsic-contact-valuations-independent-audit.md)
already establish the Gauss construction, formal-series domain restriction,
coordinate dependence, and scalar-value limitation in their stated scope.
Those reviewed provisional constructions are premises, not replay tasks.
This continuation links them to the
[normal torsion/genus account](2026-10-26-normal-torsion-spectral-genus-budget.md).

## 1. The proposed valuations and their initials

With a fixed rational normal frame, for w=(alpha,beta) in Z^2,

    v_(p,w)(sum a_ij X^i Y^j)
      =min_(a_ij nonzero)(ord_p a_ij+i alpha+j beta).

This is a valuation on K[X,Y] and extends to K(X,Y). Multiplicativity
follows because initial polynomials multiply in the domain
gr_(ord_p)(K)[X,Y]. Ties preserve a nonzero residue polynomial.
Thus C_closed times Z^2 is a valid indexing family in that chosen frame.
Rational or real weights also make sense for polynomials; integral
weights alone need not sample every cell of the resulting complex.

After choosing a uniformizer t at p, write a_ij=t^(r_ij) u_ij with u_ij
a unit. The initial form retains the terms of least value, with coefficient
initials over gr_(ord_p)K=k[T,T^-1]. For integer weights one can instead
normalize residue variables and write

    in_(p,w)(f)=residue(t^(-v(f)) f(t^alpha U,t^beta V)).

This lies in k[U,V]. The integral model O_C,p[X,Y] instead has graded
coefficient ring k[T], with T noninvertible. Keeping that model lets
coefficient vanishing remain visible as torsion.

Initial ideals always use ALL elements of an ideal. Taking the two
displayed carrier initials can miss relations created by cancellation.
For a K-ideal, a scalar infimum over its nonzero elements is not useful:
multiplication by t^(-N) drives values to minus infinity. Integral ideals
and full initial ideals avoid that misuse.

For formal series with coefficients regular at p, positive normal weights
give a well-defined valuation centered at (t,X,Y). Arbitrary K[[X,Y]]
does not satisfy the necessary bounded-tail condition: the series
sum_(n>=0) t^(-n^2) X^n has term values unbounded below for each fixed
finite alpha. Finite normal symbols have no such issue. The existing
normal-first lexicographic construction is another option on the full
generic formal ring.

## 2. Newton and Groebner combinatorics

For a polynomial f, lift each exponent to

    (i,j,ord_p a_ij).

Their lower hull gives the support function w -> v_(p,w)(f). Equalities

    ord_p a_ij+i alpha+j beta
      =ord_p a_kl+k alpha+l beta

cut out rational affine walls in the weight plane. Full initial ideals
refine the comparisons for individual polynomials. At fixed coefficient
weight one, use a Groebner complex or local chamber decomposition;
do not automatically call it a fan. Allowing a coefficient weight lambda
homogenizes these equations in (lambda,alpha,beta), with our plane the
slice lambda=1. No global finite-fan assertion is needed here.

In a fixed homogeneous normal degree n, adding (c,c) to w adds nc to
every term value, so only alpha-beta affects term ties. The diagonal
direction matters when comparing different normal orders.

The tropical locus selects weights for which the full initial ideal is
monomial free. We retain every weight and its full initial algebra.
This is essential for nilpotent normal thickenings: their ideals contain
powers of the normal variables, so every initial ideal contains monomials.
The normal-torus tropical locus is empty even when the affine initial
algebras contain substantial multiplicity and boundary information.
Standard terminology and definitions appear in
[Vinzant's initial-ideal/Groebner-complex notes](https://sites.math.washington.edu/~vinzant/teaching/582D/0116.pdf).

## 3. Complete chamber calculation for the supported quadruple

Take D=k[[t]], r>=1, and

    J=(x^2,y^2+t^r x) in D[[x,y]].

Use positive rational weights (1,alpha,beta) on (t,x,y), and put

    delta=2 beta-r-alpha.

In the integral associated graded ring k[T,X,Y], the FULL initials are

| Region | Initial ideal |
| --- | --- |
| delta<0 | (X^2,Y^2) |
| delta=0 | (X^2,Y^2+T^r X) |
| delta>0 | (X^2,T^r X,XY^2,Y^4) |

For delta<0 the two displayed initials are coprime monomials. For delta=0
they are the regular sequence X^2,Y^2+T^r X. In either case the two
equations form a filtered standard basis.

For delta>0, set f=x^2, g=y^2+t^r x, h=xy^2, q=y^4. The latter two
belong to J by the exact identities

    xg-t^r f=h,       y^2g-t^r h=q.

The monomial initials of f,g,h,q are X^2,T^r X,XY^2,Y^4. Their syzygies
are generated by the pairs (f,g),(f,h),(g,h),(h,q). They lift as

    t^r f-xg+h=0,     y^2 f-xh=0,
    y^2 g-t^r h-q=0,  y^2 h-xq=0.

In the first and third identities the correction has higher weight by
delta>0; the others lift exactly. The complete filtered syzygy-lifting
criterion proves the full-initial claim for all the stated weights.
This is a symbolic proof, not an inference from sampled weights.

The wall

    2 beta=alpha+r

retains the boundary exponent r. In the delta>0 chamber, preserving the
normal-degree grading, the T-torsion has length r in each of normal
degrees one and two. The total local torsion is 2r and the socle divisor
is r[p], as in the preceding genus note.

After inverting T, the three normalized residue initial ideals become

    (U^2,V^2),   (U^2,V^2+U),   (U,V^4),

respectively. Each has quotient length four. A single field initial
algebra no longer displays the exponent r in its torsion modules. The
valued-field FAMILY still retains r through the wall location. Thus do
not claim that all valued-field data lose the boundary; the integral
lattice is what identifies its actual torsion/divisor/genus contribution.

## 4. Frame changes and the information to retain

For diagonal changes X'=fX,Y'=gY, the same valuation has weights

    alpha'=alpha+ord_p f, beta'=beta+ord_p g.

The accompanying coefficient transformation makes the value of the
actual normal form unchanged. General GL_2 changes can require residue
relations, rather than a transformation of weight vectors alone. For
example v(X)=1,v(Y)=2 and X'=X,Y'=Y+X give v(X')=v(Y')=1 but
v(Y'-X')=2. A newly chosen monomial Gauss valuation of weights (1,1)
would give value one to that difference. The transported valuation
remembers in(Y')=in(X').

Thus C_closed times Z^2 is a coordinate chart for this family, not an
intrinsic product independent of the normal frame. Integral models and
their transitions must be retained when adding divisor degrees globally.

Scalar ideal minima alone are also insufficient: (X^2,Y^2) and
(X^2,XY,Y^2) have the same value under every centered valuation but
colengths four and three. Valuations belong on the ambient normal
algebra; a valuation on a nonreduced quotient kills its nilpotents.

There is an exact determinant bridge to the preceding genus budget.
In normal degree n, let a matrix M_n over D have columns generating
H_n subset Sym^n E_p, of generic rank h. Smith form writes its nonzero
invariant factors as t^(e_1),...,t^(e_h), and gives

    mult_p B_n=length_D(H_n^sat/H_n)=sum e_i
      =min ord_p(nonzero h-by-h minors of M_n).

For rank zero this contribution is zero. This formula is independent of
integral frame changes. It turns the torsion budget into valuations of
determinants, while preserving cancellations inside those determinants.
For example the matrix with columns (1,1) and (1,1+t^r) has all entry
valuations zero, but determinant valuation r. Entry valuations alone
miss this boundary index; the residue relations and their lifts matter.

The proposed data to retain are the local full initial algebras, their
integral coefficient lattices, their normal grading, and frame-transition
maps. Their combinatorics constrain the boundary divisors from the genus
budget and the initial relation modules entering the normal Koszul
spectral sequence. A weighted wall by itself is not identified with a
spectral-sequence page. Global realization still requires the actual
homogeneous carrier sections and filtered gluing.

## 5. Intrinsic normal symbols and weighted flags

This continuation answers the question about removing normal-coordinate
choices. All constructions here are intrinsic to the indicated embedded
configuration, not to the abstract curve independently of its embedding.

For C regularly embedded in a smooth threefold X, put E=I/I^2. The
canonical algebra is

    S=gr_I O_X=Sym E.

A degree-a hypersurface of normal order n has initial symbol in
Sym^n E tensor O_C(a), without choosing X,Y. For C subset Z subset X,

    H=ker(S -> gr_(I O_Z) O_Z)

is the intrinsic full initial ideal sheaf. These are the normal-cone
constructions in [Stacks, section 31.20](https://stacks.math.columbia.edu/tag/062Z),
with regular-immersion identification in
[section 31.22](https://stacks.math.columbia.edu/tag/0638).

For a rational section s of a vector bundle V on C, its coefficient
order at p is intrinsically

    c_p(s)=max{q in Z : s belongs to m_p^q V_p}.

Negative powers mean fractional lattices. Its coefficient initial lies
in (m_p^q/m_p^(q+1)) tensor V|p. In an integral local frame this is the
minimum of the component orders, but the definition uses no frame or
uniformizer. This applies also to the twisted normal-symbol bundles.

Equal normal weights need only E: for finite graded sums s=sum s_n in
S_K, the valuation

    v_(p,a)(s)=min_n(c_p(s_n)+a n)

is intrinsic. In any integral normal frame it is the previous Gauss
formula with w_X=w_Y=a. The associated graded ring is locally a
polynomial ring over gr_(m_p)O_C,p for the integral model; on S_K the
coefficient ring is localized to gr_(ord_p)K=k[T,T^-1]. Both are domains,
which proves multiplicativity.

For the full integer-weight family there is an especially direct
coordinate-free replacement for a weight pair. Choose an O_C,p-lattice
Lambda subset E_K, meaning a free rank-two module spanning E_K, and set

    c_(Lambda,n)(s)=max{r:s belongs to m_p^r Sym^n Lambda},
    v_Lambda(sum s_n)=min_n c_(Lambda,n)(s_n).

This is a valuation on Sym_K E_K and its fraction field. Any integral
basis of Lambda proves the Gauss property, while its definition uses
only Lambda. The unit ball on degree one recovers Lambda itself.
The old chosen-frame formula corresponds precisely to

    Lambda_w=m_p^(-w_X) O_C,p X + m_p^(-w_Y) O_C,p Y.

Thus the intrinsic indexing set is pairs (p,Lambda), rather than a
canonically fixed C times Z^2. A frame displays diagonal lattices.
For common weight a, Lambda=m_p^(-a) E_p gives the construction above.

Up to homothety these rank-two lattices are the vertices of the
Bruhat--Tits tree; a basis displays one apartment. The actual lattice,
including its scale, is needed here: replacing Lambda by m_p^(-c)Lambda
adds nc to the value in normal degree n. For the general-DVR lattice
and tree construction see Ludwig--Merten,
[section 3](https://afm.episciences.org/18061/pdf). No finite-residue-field
assumption or fixed finite valency is imposed here.

Unequal weights require a weighted flag of E, rather than two named
coordinates. Suppose an intrinsic line subbundle R subset E is given,
with quotient line L. In the generically curvilinear thickening studied
above this flag is supplied by Z itself:

    L=(K/K^2)/torsion, R=ker(E -> L).

Thus R is the saturation of the actual first-symbol image even where
that image degenerates. No splitting of 0 -> R -> E -> L -> 0 is needed.

Assign weight beta to R and alpha to L, with beta>alpha. Use the
intrinsic lattice

    Lambda_(alpha,beta)=m_p^(-beta) R_p+m_p^(-alpha) E_p.

Its symmetric powers give equivalently
the intrinsic filtration

    B_(n,j)=image(R^j tensor Sym^(n-j) E -> Sym^n E),
    B_(n,j)/B_(n,j+1)=R^j tensor L^(n-j).

Its level is n alpha+j(beta-alpha). Combining with coefficient order
at p gives the full basis-free formula, for integer alpha,beta,q,

    F^q(S_n tensor K)
      =sum_(j=0)^n m_p^(q-n alpha-j(beta-alpha)) B_(n,j),p.

For real weights use the ceiling of each exponent. For finite graded
sums take the direct sum over n. In an adapted integral frame X spanning
R and Y lifting L, this is exactly

    min(ord_p a_ij+i beta+j alpha).

To check independence, another adapted frame has X'=uX,
Y'=vY+bX with u,v units and b regular at p. Since beta>alpha, both this
substitution and its inverse preserve the filtration. Consequently the
valuation and its associated initial algebra are independent of the
adapted frame, despite a possibly nonsplit extension. The model lives
on the normal bundle Spec_C Sym E, which has a canonical projection to C.

This is an additional flag if only C subset X is specified. When Z is
generically curvilinear it is intrinsic to C subset Z subset X. For a
candidate-search problem the flag is data to vary, rather than a reason
to choose a global coordinate frame. This does not select a canonical
unequal-weight flag from an arbitrary bare rank-two bundle.

For the fixed rational quartic there is also a distinguished flag before
choosing Z: its unique smooth quadric Q gives the specified sequence
0 -> O(-8) -> E -> O(-6) -> 0 in
[R0020](../results/quartic_conormal_characteristic_jump.md). That flag
defines weighted normal-algebra filtrations in characteristic zero too,
where the extension is nonsplit. A hypothetical thickening's flag R
need not equal this quadric flag; no alignment is assumed.

The actual ambient neighborhood needs a further distinction. A full
Taylor expansion into separate normal degrees requires extra splitting
data; the normal-symbol algebra alone does not supply it. Even an
adapted conormal flag does not determine arbitrary finite weighted
valuations on the full ambient formal ring. For example the lifts
x and x'=x+y^2 have the same class in I/I^2, while a Gauss valuation
with v(x)=beta>2 alpha=2v(y) gives v(x')=2 alpha. Thus the flag
construction on S is an intrinsic refinement of the normal initial
algebra, not an assertion that every ambient weighted initial ideal is
determined by E and R alone. Retain Rees/filtered neighborhood data for
actual equations and cancellations between different normal orders.

For intrinsic valuations directly on the ambient function field there
is the already reviewed geometric route. Let D_exc be the exceptional
divisor of Bl_C X, with fiber D_p over p. The flag

    Bl_C X superset D_exc superset D_p

gives the normal-first, coefficient-second valuation. A point q in D_p
refines it to a full flag and remembers a normal direction. For a
normal symbol s of degree n, first take r=c_p(s), then take the zero
order at q of its residue binary-form section. This yields the local
lexicographic description (n,r,order_q residue(s)); the flag and
section-valued initials provide the intrinsic meaning. Uniformizers
used for numerical labels must be compatible with the flag. Composition
is justified by [Stacks, Lemma 10.50.10](https://stacks.math.columbia.edu/tag/088Z).

Here D_exc=Proj_C Sym E, with points interpreted as one-dimensional
quotients of E. The quotient E -> L supplied by a curvilinear Z picks a
section and hence a distinguished q_p in each D_p. Use the ambient
exceptional divisor: Proj gr_K O_Z is empty for a solely supported
nilpotent thickening. The lexicographic flag valuation and the finite
weighted flag filtrations are distinct constructions; a linear
functional on the lexicographic leading value does not in general
recover the finite weighted minimum of an arbitrary sum.

All boundary divisors B_n=div Fitt_0(H_n^sat/H_n) and the genus budget
already have this intrinsic meaning. Frame polynomials are ways of
calculating their initial objects and maps, not part of their definition.



---

## boundary-repair-global-lifting-audit

# Independent audit: boundary repair and global lifting

Review date: 2026-10-27. Reviewer: independent `repair_note_audit` agent.
Source: [boundary repair and global lifting](2026-10-26-boundary-repair-global-lifting.md).
Outcome: **PASS within the stated scopes**. The exact repair criteria,
source-image identities, and fixed-degree endpoint are independently
reconstructed below. The controlled boundary-modification comparison
remains an explicitly unproved research target. No canonical promotion,
new STCI exclusion, or homogeneous realization is certified by this review.

## 1. Scope and method

The reviewer read the retrieval index and contribution protocol, then
checked the exact source text. The review distinguishes the following:

- smooth-projective-curve cohomology for a specified vector bundle V;
- the entire effective-divisor family on P1, with B a nonnegative integer;
- normal and jet images from actual homogeneous equations;
- the degree-exhaustion criterion for actual proper complete intersections;
- the proposed, but not yet established, comparison with saturated boundary
  data of a supported generically curvilinear thickening.

The saturated Gorenstein pairing is used only in its inherited scope.
No accepted proof or executable certificate was rerun, and no sampled
example is used as evidence for a universal assertion.

## 2. Principal parts and the dual repair condition

For effective D, the quotient Q_D=V(D)/V is a finite-support sheaf, and
the exact sequence 0 -> V -> V(D) -> Q_D -> 0 gives the exact segment

    H^0(Q_D) -> H^1(V) -> H^1(V(D)).

Thus the kernel of the latter map is exactly the principal-parts image.
This proves the source's criterion for an identified class o in H^1(V).
It does not endow o itself with a zero divisor.

Functorial Serre duality identifies the dual of H^1(V) -> H^1(V(D)) with
the inclusion

    H^0(V^vee tensor omega_C(-D))
      -> H^0(V^vee tensor omega_C).

A class maps to zero if and only if its functional vanishes on the image
of this inclusion. The annihilator criterion therefore has the correct
direction and twist. Both arguments work in arbitrary characteristic.
The source correctly avoids assuming that varying-divisor cohomology
dimensions are constant on an arbitrary higher-genus curve.

## 3. P1: common-divisor kernel and the dimension threshold

For V=O(-r), r>=2, let n=r-2. Serre duality identifies o with a functional
on H^0(O(n)). If D has degree B and is cut out by nonzero h in H^0(O(B)),
then the image of H^0(O(n)(-D)) in H^0(O(n)) is exactly
h H^0(O(n-B)); it is zero when n-B<0.

Consequently repair by D is equivalent to

    o(hg)=0 for every g in H^0(O(n-B)),

which is exactly h in the kernel of the source's multiplication map.
Conversely any nonzero kernel element defines such an effective D.
If a divisor of degree less than B repairs o, adding an effective divisor
to obtain degree B preserves vanishing, since the maps on H^1 factor.
This verifies the stated equivalence with degree at most B. Repeated
factors of h are permitted throughout; no reduced-support restriction
or separability assumption is hidden in the argument.

The dimensions in the threshold argument are B+1 and max(r-1-B,0).
For B>=floor(r/2), the former is strictly greater than the latter.
Hence a nonzero kernel exists for every o. This establishes the stated
limit of a single line-bundle obstruction under an unrestricted pole
allowance. It does not prove an actual boundary or a realizable lift.

For a split bundle, the direct-sum H^1 class maps to zero exactly when
every component does. If one divisor must repair them, the SAME section h
must lie in every component kernel. The stacked map therefore gives the
correct simultaneous condition. Allowing a separate h for each component
would be a weaker test and would lose the common-boundary requirement.
On a fixed splitting-type stratum these maps have fixed source and target
dimensions, so their ranks and degeneracy loci have the stated finite
algebraic meaning. No assertion of universal rank is inferred from a
generic parameter or a selected point.

## 4. The boundary comparison is not proved by these criteria

The inherited relations D_i+D_(m-1-i)=D_soc and effectivity imply
0<=D_i<=D_soc. Accordingly

    Hom(L^i(D_i),L^j(D_j))
      =L^(j-i)(D_j-D_i) subset L^(j-i)(D_soc)

is correct. These are inclusions of possible coefficient bundles. They
do not prove a morphism of lifting problems or identify the obstruction
for an actual multiple curve with its image under a chosen twist.

The source explicitly marks the needed V -> V' -> V(c D_soc) comparison
as unproved, requires the actual lifting complex, and does not identify
ordinary torsion, spectral Delta, and allowed principal parts. This is
the essential remaining dependency. The relaxation to arbitrary divisors
of degree c delta is logically safe only after the comparison is supplied:
failure of the relaxed test excludes permitted repairs; passing it proves
neither the constrained divisor data nor a genuine lift.

## 5. Actual homogeneous jet and symbol images

The source-image formulas follow directly from the sheaf sequences

    0 -> I^(N+1)(d) -> I(d) -> (I/I^(N+1))(d) -> 0,
    0 -> I^(n+1)(d) -> I^n(d) -> Sym^n E(d) -> 0.

Their H^0 images are precisely the displayed connecting-map kernels.
The second sequence uses the regular embedding of C in the smooth
threefold. These are actual global k-linear source images, not arbitrary
K=k(C) normal symbols.

The next-jet sequence with kernel Sym^N E(d) is likewise exact. Its
connecting class is in H^1(C,Sym^N E(d)), as stated. The note correctly
distinguishes this explicit linear jet obstruction from other relation
or ideal lifting problems, whose targets have not been supplied by that
sequence. Choosing allowable graded symbols separately does not specify
one compatible jet, so retaining the whole source U_(d,N) is necessary.

## 6. Fixed-degree generic length and degree exhaustion

Let F,G be actual global forms of degrees a,b defining a proper complete
intersection containing an integral C of degree d, and suppose M=ab/d
is an integer. At eta_C the two equations have finite transverse length
m_C. The fundamental cycle and Bezout give d m_C<=ab, hence m_C<=M.

For any Artin local algebra of length m_C, every nonzero successive
maximal-ideal power strictly decreases length: equality of adjacent
powers would make that power zero by Nakayama. Therefore its maximal
ideal has exponent at most m_C. The quotient by m^(M+1) already retains
the full local algebra R/(F,G), and its length is m_C.

It follows that the truncated length is M exactly when m_C=M. Then the
contribution of C consumes degree ab. Any additional curve component
would contribute positive degree, while purity of the proper complete
intersection rules out embedded components. Conversely sole reduced
support C gives m_C=M. This proves the intrinsic finite endpoint in
the source, with all its properness and actual-global-form hypotheses.

The matrix interpretation requires all truncated multiples. The note
appropriately states that a coefficient/normal chart is chosen for that
calculation: the residue field is not claimed to be canonically embedded
in R/m^(M+1). Fixed chart denominators can be cleared, with coefficients
of the actual forms remaining constants in k. One must retain the proper
pair open locus. No bound uniform in a,b follows from this fixed-degree
criterion.

## Outcome

No substantive correction to the inspected source text is required.
The universal repair test and the exact finite endpoint pass independent
reconstruction. The proposed boundary-to-obstruction comparison remains
open and must not be reported as a completed theorem. The audit supports
using these criteria to choose a class-wide calculation and to diagnose
when a coarse obstruction is too weak; it does not certify any new
exclusion, nonempty realization locus, or canonical result promotion.



---

## weighted-initials-normal-boundary-audit

# Independent audit: weighted initials and normal boundary data

Date: 2026-10-26. Reviewer: independent `valuation_budget` agent.
Status: independent reconstruction of the [companion continuation](2026-10-26-weighted-initials-normal-boundary.md).
Outcome: **PASS within the stated domains and hypotheses**. This is reviewed
provisional evidence, not canonical promotion, a global realization, or an
STCI exclusion.

## Scope and method

The reviewer read the retrieval index and the preceding normal-torsion
budget, then independently checked the integral chamber calculation,
coefficient-ring distinctions, frame changes, and determinant-lattice
bridge. The existing reviewed Gauss/domain construction is used in its
stated scope; inherited certificates and accepted exclusions were not
rerun. No finite sample is used to justify the all-weights calculation.

## 1. Domain, residues, and coordinate qualifications

For each closed p of a smooth curve C and a chosen rational normal frame,
the displayed minimum is a Gauss valuation on k(C)[X,Y] for any integer
weights, and extends by quotients to k(C)(X,Y). Initial polynomials over
the associated graded coefficient domain prove multiplicativity even
when multiple terms tie. Positive rational weights extend this formula
to the integral completed local model D[[X,Y]], D=k[[t]]. The divergent
series sum t^(-n^2)X^n correctly rules out the same formula on arbitrary
k(C)[[X,Y]]. No centering claim is made on that entire generic formal ring.

For integer weights, substituting X=t^alpha U,Y=t^beta V and dividing
by t^v(f) gives the stated residue initial in k[U,V]. This is a normalized
description of a valued-field initial. The integral model retains the
coefficient symbol T as noninvertible; passing to the field inverts it.
The warning that inf v(J)=-infinity for a nonzero k(C)-ideal is correct,
because multiplication by t^(-N) is allowed. This warning does not deny
the well-defined valued-field full initial ideal.

The diagonal frame-change signs are correct: X'=fX makes the transported
weight alpha'=alpha+ord_p(f). The GL_2 counterexample correctly shows
that the values of new coordinate variables alone need not determine the
transported valuation: the initial relation between those variables must
also be retained. Thus C_closed times Z^2 is a framed family, rather than
a canonical global product of valuation spaces.

The Newton comparisons give rational affine walls at fixed coefficient
weight one. Calling their subdivision a complex, rather than asserting
an unqualified fan or a global finiteness theorem, is appropriate.
Integral weights need not meet every rational cell. The diagonal shift
observation in fixed normal degree is correct.

## 2. Full chamber calculation, all stated weights

Let J=(x^2,y^2+t^r x) in D[[x,y]], r>=1, and give (t,x,y)
positive rational weights (1,alpha,beta). Put delta=2 beta-r-alpha.
The integral associated graded coefficient ring is k[T].

If delta<0, the carrier initials are X^2,Y^2. They form a regular
sequence, so their Koszul syzygy lifts and no extra initial generator
appears. If delta=0, the initials are X^2,Y^2+T^rX. This is again a
regular sequence: modulo X^2, the second polynomial is monic in Y and
is therefore a nonzerodivisor. The standard filtered argument gives the
claimed full initial ideal in both cases.

For delta>0, set f=x^2, g=y^2+t^r x, h=xy^2, q=y^4. Their initials are

    X^2, T^rX, XY^2, Y^4.

All pair syzygies of these four monomials are generated by the pairs
(f,g), (f,h), (g,h), (h,q). The omitted (f,q) and (g,q) pair syzygies
factor through h. The displayed identities

    t^r f-xg+h=0,     y^2 f-xh=0,
    y^2 g-t^r h-q=0,  y^2 h-xq=0

lift those generators. In the first identity, h has weight delta more
than t^r f and x times the initial term of g. In the third, q has weight
delta more than y^2 times that initial term and t^r h. The other two
identities lift without corrections. Positive rational weights may be
scaled to positive integer weights, and completeness permits successive
strict increases of weight. The filtered syzygy criterion therefore
proves the FULL initial ideal, not just inclusion, for every stated
weight. The argument and identities work in arbitrary characteristic.

The three chamber ideals in the source are consequently correct. After
inverting T and normalizing, they become

    (U^2,V^2), (U^2,V^2+U), (U,V^4),

each of colength four. The family still remembers r in the wall
2 beta=alpha+r, even though one normalized field initial does not
display an r-length coefficient-torsion module. The source explicitly
preserves this distinction and does not overstate information loss.

In the delta>0 chamber the ideal is homogeneous for normal degree if
deg X=deg Y=1 and deg T=0. Its coefficient torsion has length r in
normal degrees one and two. Thus tau_p=2r and D_soc=r[p], agreeing
with the prior pointwise budget. On the wall, Y^2+T^rX mixes two normal
degrees. In the delta<0 chamber the initial ideal is normal homogeneous,
but its normal layers are those of this different weighted degeneration,
not the ordinary normal layers of B. Their absence of coefficient torsion
does not contradict the ordinary torsion budget or imply an extra component.

## 3. Determinants recover the normal saturation indices

The additional Smith-minor bridge is correct. Let columns of a matrix M
over D generate H_n inside the free module S_n, and let h be its rank.
Smith form reduces M by invertible row and column operations to its
nonzero entries t^(e_1),...,t^(e_h), up to units. Hence

    length_D(H_n^sat/H_n)=sum e_i
      =min ord_t(nonzero h by h minors of M).

For h=0, the index is zero, with the empty minor interpreted as one.
This is the local multiplicity of the intrinsic divisor B_n. It is
invariant under integral frame changes and depends on the integral
lattice, not merely the generic subspace H_n tensor k((t)).

For M=[[1,1],[1,1+t^r]], every entry has valuation zero but det M=t^r.
Thus entrywise valuations or a tropical determinant lower bound need
not determine the index: tied leading terms can cancel. Actual minor
valuations and residue/initial relations retain this information. This
supports the proposed use of full initial data rather than scalar minima.

## 4. Scope boundaries and outcome

Monomial-containing initials must be retained for the stated problem.
A nilpotent normal ideal contains powers of the normal variables, so
its full initial ideal contains monomials at every weight. Its normal
torus tropical locus can therefore be empty while its affine initial
algebras retain the relevant thickness. The equality of scalar ideal
values for (X^2,Y^2) and (X^2,XY,Y^2) is also correct under every
centered valuation; their different colengths show what those scalar
values omit.

The source does not identify weighted walls with normal-Koszul
spectral-sequence pages. Those pages depend on the specified normal
filtration and its higher differential maps. Weighted initials can
organize initial relations and coefficient defects without independently
supplying the extension data or a global descent theorem. Actual
homogeneous carrier sections, frame transitions, and filtered gluing
remain necessary for global realization.

No substantive correction to the inspected continuation is required.
The all-weights chamber proof and the Smith-minor bridge are independently
reconstructed here. No canonical result record is changed or promoted.

## 5. Additional independent review of intrinsic symbols and weighted flags

Reviewer: independent `budget_audit` agent, 2026-10-26. This addendum reviews
only the newly appended section 5 of the source. It independently checks
the intrinsic constructions and their coordinate qualifications; no
inherited proof or certificate is replayed.

For a regular immersion C subset X, the identification
gr_I O_X=Sym(I/I^2) and the kernel definition of the full initial ideal H
are intrinsic to the marked embedding. A normal-order-n degree-a equation
has symbol in Sym^n E tensor O_C(a); choosing local normal coordinates is
unnecessary for that assertion. The coefficient order

    c_p(s)=max{q : s belongs to m_p^q V_p}

is likewise invariant under GL(V_p) over the local DVR. Its associated
initial is a section of the stated graded coefficient line tensored with
the fibre of V. The zero section has order infinity, as usual.

One coefficient-ring qualification was requested in the source: on the
integral local algebra Sym(E_p), the equal-weight associated graded is a
polynomial algebra over gr_m O_C,p=k(p)[T]. On S_K=Sym(E) tensor k(C),
the coefficient parameter is invertible, so the coefficient graded ring
is k(p)[T,T^(-1)]. The valuation remains multiplicative in either domain;
the integral statement followed by localization proves the field version.
This is a ring-domain correction, not a change to the valuation formula.

For unequal weights, let R subset E be a line subbundle, L=E/R, and
beta>alpha. In an adapted frame X for R and Y lifting L, the submodule

    B_(n,j)=image(R^j tensor Sym^(n-j) E -> Sym^n E)

has basis X^i Y^(n-i) for i>=j. It follows directly that the proposed
sum

    sum_(j=0)^n m_p^(q-n alpha-j(beta-alpha)) B_(n,j),p

contains a coefficient of X^i Y^(n-i) exactly when its order is at least
q-i beta-(n-i)alpha. For real weights this lower integer bound is the
ceiling of the exponent. Thus the basis-free filtration is exactly the
displayed Gauss minimum, without requiring a splitting E=R direct_sum L.

An adapted change X'=uX, Y'=vY+bX, with u,v units and b integral, preserves
the filtration: the added term bX has weight at least beta>alpha. The
inverse is adapted and has the same property, proving equality rather
than only one-sided containment. On associated graded normal variables,
the off-diagonal term vanishes and the diagonal unit changes remain.
Consequently the filtration and associated initial algebra are independent
of the adapted integral frame. A nonsplit extension is therefore not an
obstruction to this construction. The flag is additional data for a bare
embedding, and is supplied intrinsically by a generically curvilinear
marked thickening through E -> (K/K^2)/torsion. This distinction is stated
correctly.

The ambient warning is necessary and correct. The coordinate lifts x and
x+y^2 have the same class in I/I^2, but under beta>2 alpha their ambient
Gauss values differ. Hence the conormal flag alone does not determine
every finite weighted filtration on the full ambient formal ring. The
construction on Sym E has a canonical projection to C and must retain
its stated separation from actual filtered-neighborhood data.

For the geometric alternative, the exceptional divisor of Bl_C X is
Proj_C Sym E in the quotient-line convention. The fibre over p and a
point q in that fibre give the stated regular flag. For a homogeneous
normal symbol its three-stage value is normal degree, coefficient order,
and zero order of the normalized residue binary-form section at q;
local Cartier equations and coefficient uniformizers must be chosen
compatibly with the flag. The quotient E -> L selects the claimed section
of this exceptional divisor. If K is nilpotent, the irrelevant ideal of
gr_K O_Z is nilpotent as well, so its Proj is empty. Using the ambient
exceptional divisor is therefore essential.

Finally, the lexicographic flag valuation and the finite weighted minimum
are correctly distinguished. Selecting a lexicographic leading term and
then applying a linear weight need not select the least weighted term of
the original sum. The intrinsic determinant/saturation boundary divisors
remain independent of these coordinate presentations.

**Addendum outcome:** PASS after the coefficient-ring qualification above;
no further mathematical correction is required. The findings remain
reviewed provisional evidence, with no new global realization, exclusion,
or canonical result promotion.

## 6. Independent review of the lattice formulation

Date: 2026-10-26. Reviewer: independent `intrinsic_filtration` agent.
The reviewer read the saved section 5 and independently reconstructed the
lattice formulation. This review concerns its algebra, not a new audit
of the cited Bruhat--Tits source or a global ambient extension theorem.

Let D=O_C,p, m=m_p, K=k(C), and let Lambda be a full D-lattice in E_K.
The formula c_(Lambda,n)(s)=max{r:s belongs to m^r Sym^n Lambda}, followed
by the minimum over the finite homogeneous components, is a valuation.
Indeed, any D-basis of Lambda makes it the coefficient Gauss valuation
on a polynomial algebra. Its initial polynomials multiply in the domain
gr_(ord_p)K[U,V]. The definition uses only Lambda, so changing its integral
basis cannot change the valuation. Its degree-one unit ball recovers
Lambda, as claimed.

The signs in Lambda_w=m^(-w_X)DX+m^(-w_Y)DY are correct: X is t^(w_X)
times the lattice basis vector t^(-w_X)X, and therefore has value w_X.
This holds for all integer weights, including negative ones, on the
polynomial algebra and its fraction field. The distinguished reference
lattice E_p is separate from the weighted lattice Lambda. In particular,
Lambda=m^(-a)E_p assigns common normal weight a. Replacing any Lambda by
m^(-c)Lambda adds nc to the value of a homogeneous degree-n symbol.
The actual lattice scale is thus relevant when normal degrees are mixed.

For a saturated line R subset E with quotient L and integers beta>alpha,
Lambda=m^(-beta)R_p+m^(-alpha)E_p is intrinsic without a splitting.
An adapted integral frame r,y expresses it as
t^(-beta)Dr direct_sum t^(-alpha)Dy. Expanding its symmetric powers gives
exactly the source's sum over B_(n,j) with coefficient exponent
q-n alpha-j(beta-alpha). Thus the lattice construction and the previous
weighted-flag filtration agree. For real weights, the ceiling formula
defines the filtration directly; a single D-lattice is not asserted.

The algebra on which this construction is intrinsic is Sym_K E_K, or the
normal-bundle model with its canonical projection to C. No identification
of that model with the full ambient formal neighborhood is supplied by a
lattice or conormal flag. The example x versus x+y^2 when beta>2 alpha
correctly demonstrates the additional higher-order data needed there.

**Lattice review outcome: PASS.** No source correction is required for
the inspected lattice formulas. They remain reviewed provisional evidence
and do not promote a global ambient valuation or realization theorem.

