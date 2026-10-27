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
