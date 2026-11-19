# Equivariant set-theoretic equations and their limits

## Scope and question

The number of equations defining a reduced support differs from the number
of generators of a thickening's ideal. Requiring torus eigenforms is a
further restriction. The power lemma below separates these questions
without a complete-intersection, purity or invariance hypothesis on the
thickening.

The quartic application fixes an algebraically closed field \(k\),
\(S=k[x_0,x_1,x_2,x_3]\), \(C=[s^4:s^3t:st^3:t^4]\),
\(P=I_C\), and the torus weights \((0,1,3,4)\).
An eigenform is ordinary homogeneous and homogeneous for the integer
character grading; characters are not reduced modulo the characteristic.
The three-line example changes both the support and the torus explicitly.
The general lemmas and three-line example work in every characteristic;
the quartic's exact ranks have the characteristic hypotheses stated below.

## Radical invariance of the number of equations

Let \(S\) be a Noetherian nonnegatively graded \(k\)-algebra with a
grading-preserving split-torus action, and let \(P\) be a homogeneous
torus-stable radical ideal. For a homogeneous ideal \(K\) with
\(\sqrt K=P\), let \(\operatorname{ara}_{\rm hom}(K)\) be the least
number of ordinary homogeneous elements **in \(K\)** whose generated
ideal has radical \(P\). Define \(\operatorname{ara}_T(K)\) similarly,
requiring eigenforms. These definitions impose no fixed degrees.

**Power lemma.** For every finite \(r\), a defining \(r\)-tuple of either
kind exists in \(K\) if and only if one exists in \(P\). Consequently
\[
 \operatorname{ara}_{\rm hom}(K)=\operatorname{ara}_{\rm hom}(P),
 \qquad \operatorname{ara}_T(K)=\operatorname{ara}_T(P).             \tag{1}
\]
In particular \(K\) need not itself be invariant.

Indeed, Noetherianity gives \(P^N\subset K\subset P\) for some \(N\):
choose generators \(p_i\) of \(P\), powers \(p_i^{n_i}\in K\), and
\(N=1+\sum_i(n_i-1)\). Each degree-\(N\) product of the \(p_i\)
then contains one such power. A tuple in \(K\) already lies in \(P\).
Conversely replace a tuple \(f_1,\ldots,f_r\) in \(P\) by
\(f_1^N,\ldots,f_r^N\). Powers preserve its radical, ordinary
homogeneity and eigenform property. This proves the assertion. Finite
eigenform generating sets of \(P\) exist by splitting its homogeneous
generators into their character components.

Thus changing a supported thickening cannot improve its unrestricted
equivariant equation count. It can change the required degrees and the
minimal ideal-generator count. For an actual sole-supported CI with
generic length \(m\), the sharper
[primary-power bound](../torus_hilbert_boundary.md#equationhilbertchow-graph-and-its-top-fiber)
allows \(N=m\); that bound is additional information. Under restriction
from a torus \(T\) to a subtorus \(H\),
\(\operatorname{ara}_{\rm hom}\le\operatorname{ara}_H
\le\operatorname{ara}_T\), since a \(T\)-eigenform is an \(H\)-eigenform.
The example below shows that equality need not hold.

## The fixed quartic in different characteristics

Put
\[
 q=x_0x_3-x_1x_2,\qquad A=x_1^3-x_0^2x_2,\qquad
 D=x_2^3-x_1x_3^2.
\]
Their weights are \(4,3,9\), and \(\sqrt{(q,A,D)}=P\) in every
characteristic. On the Segre quadric \(q=0\), write
\((x_0,x_1,x_2,x_3)=(ac,ad,bc,bd)\). The two cubics restrict to
\(a^2(ad^3-bc^3)\) and \(-b^2(ad^3-bc^3)\). Since \([a:b]\)
is a projective coordinate, their common support is exactly the graph
\([a:b]=[c^3:d^3]\), namely \(C\). Equality also holds for the affine
cone radicals, since the equations are homogeneous and contain the origin.
An algebraic control is
\[
 B=x_1^2x_3-x_0x_2^2,\qquad B^2+AD=x_1x_2q^2.
\]

The [one-eigenform trace obstruction R-0042](../../results/eigenform_trace_obstruction.md)
excludes an eigenform pair in characteristic zero. The upper bound just
proved and (1) therefore give, for **every** homogeneous \(K\) with
radical \(P\),
\[
 \operatorname{ara}_T(K)=3\quad(\operatorname{char}k=0).           \tag{2}
\]
In positive characteristic the
[fixed-model Frobenius pair](../arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier)
has degrees \((4,N)\), with \(N=p^e=3a+4b>5\), and weights
\((4,3N)\): the mixed monomial in its second equation has weight
\(a+4(2a+3b)=3N\). Hence \(\operatorname{ara}_T(K)=2\) for every
such \(K\) in every positive characteristic; height two supplies the
lower bound. These are integer weight identities.

In characteristic zero \(\operatorname{ara}_{\rm hom}(K)\) is either
two or three, and choosing between them is exactly the unresolved STCI
question. If an ordinary defining pair exists, **every** same-radical
thickening, including both full torus limits, contains powers of that
ordinary pair. None contains an eigenform pair. Thus extra limit
generators cannot alone establish that ordinary equations acquire
residual curves: R-0042 controls eigenform equations. A theorem that every
ordinary defining pair descends to an eigenform pair for this quartic
would itself resolve the unrestricted non-STCI problem.

## A rank-two counterexample with a complete-intersection origin

In \(k[v,x,y,z]\), let \(B\subset\mathbf P^3\) be the three concurrent
coordinate lines with
\[
 I_B=(xy,xz,yz)=(y,z)\cap(x,z)\cap(x,y).
\]
There is an ordinary degree-\((2,2)\) defining pair:
\[
 \sqrt{(xy,z(x+y))}=I_B.                                      \tag{3}
\]
Indeed, \(xy=0\) forces \(x=0\) or \(y=0\), and the other equation
then forces one more of \(x,y,z\) to vanish. The forms have no common
factor and are a proper CI.

Let \(T'=(\mathbf G_m)^2\) act by
\((v,x,y,z)\mapsto(v,\alpha x,\beta y,z)\). Restriction of an ordinary
homogeneous \(T'\)-eigenform to \(v=0\) is a monomial or zero: ordinary
degree and the two characters determine all three exponents. If either
member of a proposed pair restricts to zero, their plane intersection
contains a curve. Otherwise both monomials must vanish at all three
coordinate points, so each uses at least two of \(x,y,z\). Their
supports intersect; both vanish on the corresponding coordinate line.
They cannot cut out only those three points. This proves the all-degree
obstruction \(\operatorname{ara}_{T'}(I_B)>2\); the three displayed
monomial generators give equality with three.

Now restrict to \(\lambda(t)=(t,t^2)\subset T'\). Minimum-weight
normalization of (3) gives \((xy,xz+t yz)\). Its full contracted family
and special ideal are
\[
 \mathcal K=(xy,xz+t yz,y^2z),\qquad K_0=(xy,xz,y^2z).           \tag{4}
\]
The relation \(z(xy)-y(xz+t yz)=-t y^2z\) adds the third generator.
For the monomial order \(x>y>z\), the displayed polynomials are a
monic Gröbner basis over \(k[t]\): the remaining nontrivial
S-polynomial is \(t y^3z\), reduced by \(y^2z\). Standard monomials
therefore make the quotient free over \(k[t]\). It is \(t\)-torsion
free and agrees with the raw pair after inverting \(t\), proving (4)
is the full contraction, in every characteristic.

The special ideal has the primary decomposition
\[
 K_0=(y,z)\cap(x,z)\cap(x,y^2).
\]
It is saturated because the spare variable \(v\) acts freely. Its
Hilbert--Burch matrix
\[
 \begin{pmatrix}-z&0\\y&-y^2\\0&x\end{pmatrix}
\]
has maximal minors \(xy,-xz,y^2z\); they have height two. Thus it is
ACM, with generator degrees \(2,2,3\), syzygy degrees \(3,4\), and
Hilbert numerator \(1-2u^2+u^4\), the CI(2,2) numerator. Its cycle is
\([L_x]+[L_y]+2[L_z]\), with \(L_x=V(y,z)\), and similarly for the
other two lines. An ACM invariant full boundary with a CI origin can
therefore still fail equivariant set-theoretic two-generation.

For \(\lambda\) itself there is the defining eigenpair
\[
 xy,\qquad z(x^2+yz),                                         \tag{5}
\]
of degrees \((2,3)\) and weights \((3,2)\). On \(x=0\) or \(y=0\),
its common zeros are exactly the three lines, in every characteristic.
Consequently for **every** homogeneous \(K\) with radical \(I_B\),
\[
 \operatorname{ara}_{\rm hom}(K)=\operatorname{ara}_{\lambda}(K)=2,
 \qquad \operatorname{ara}_{T'}(K)=3.                          \tag{6}
\]
This separates ordinary equations, a one-parameter action and the full
torus on the same support. It disproves general torus descent, even with
a saturated ACM CI-origin boundary. It gives no rank-one or integral-curve
counterexample for the quartic. The
[clean-cancellation theorem](../torus_hilbert_boundary.md#clean-cancellation-and-residual-descent)
applies to (4) with \(H=x\), \((u,v)=(y,z)\), \(D_0=-y^2z\):
its two effective summands may cover different components here. This
explains why its supported-descent corollary requires integral support.

## The exact local length identity and its membership hypothesis

Let \(R\) be a commutative ring, \(U\) an ideal, and assume \(H\)
is a nonzerodivisor modulo \((D)\). No regularity or dimension
hypothesis on \(R\), and no two-generation hypothesis on \(U\), is
needed for the exact sequence
\[
 0\longrightarrow R/(U+(D))\xrightarrow{\ H\ }
 R/(HU+(D))\longrightarrow R/(H,D)\longrightarrow0.             \tag{7}
\]
If \(Hr=Ha+cD\), with \(a\in U\), regularity modulo \(D\) gives
\(r-a\in(D)\); this proves injectivity. The other assertions follow
by taking the quotient by the image of multiplication by \(H\).
When the modules have finite length,
\[
 \ell R/(HU+(D))=\ell R/(U+(D))+\ell R/(H,D).                   \tag{8}
\]
The first term is \(\ell R/U\) precisely when \(D\in U\).
For example, in \(k[[r,s]]\), take \(U=(r,s^2)\), \(H=r\),
\(D=s\). The three lengths in (8) are \(2=1+1\), whereas substituting
\(\ell R/U\) would give \(2+1\). With \(D=s^2\in U\), the equality
is instead \(4=2+2\). These are monomial-basis calculations.

The first cancellation of an actual normalized pair always has
\(D_0\in(u,v)\); hence the corrected term reduces to \(R/(u,v)\)
there. At the generic point of the marked curve, (8) computes the
full limit's coefficient only after proving that its localized full
ideal is \(HU+(D)\). A three-generator approximation or a length
identity at that one point does not establish the global cycle formula.

## Endpoint defects and the polynomial budget

Let \(Z\) be any \(T\)-invariant projective scheme with reduced support
the fixed smooth quartic, and put \(\mathfrak n=\mathcal I_C\mathcal O_Z\).
Its finite nilpotent filtration has equivariant coherent layers
\(E_j=\mathfrak n^j/\mathfrak n^{j+1}\) on \(C\simeq\mathbf P^1\).
Every generically zero equivariant coherent sheaf on \(C\) has support
in \(\{p_0,p_\infty\}\): its support is a finite invariant set, while
every other orbit is infinite. This does not require freeness of that
open orbit. In particular it applies to each layer's torsion and to a
generically vanishing full normal-relation saturation quotient. Their
zeroth Fitting divisors have the form \(\alpha p_0+\beta p_\infty\),
with coefficients their stalk lengths over the endpoint DVRs.

Write \(r_j=\operatorname{rank}E_j\), \(m=\sum_j r_j\), and define
\(\deg E_j=\deg(E_j/\operatorname{tors})+
\ell(\operatorname{tors}E_j)\). Additivity and Riemann--Roch give
\[
 P_Z(n)=4mn+\sum_j\chi(E_j)
       =4mn+m+\sum_j\deg E_j.                                 \tag{9}
\]
Here \(m\) is the generic local length of \(Z\). If \(Z\) has the
CI(\(a,b\)) polynomial, this forces
\(m=ab/4\) and \(\sum_j\deg E_j=-m(2a+2b-7)\), even when \(Z\)
is not itself a CI. Endpoint torsion is included once in this budget;
it is not an additional genus penalty. The identity does not bound
individual negative bundle degrees or recover multiplication and the
embedded ideal.

These observations extend the
[intrinsic-filtration budget](../normal-geometry/actual_equation_filtration.md#intrinsic-filtration)
to invariant boundary schemes with possible embedded points. The full
[normal-equation comparison](../filtered_equation_comparison.md#local-comparison-and-the-punctual-defect)
already owns the normal initial ideal and actual equation-module defect.
Its generic formula \(\dim\Delta=\mu(H)-2\) assumes an actual
two-generator transverse parameter ideal; one cannot substitute a
boundary ideal whose generic minimal generator count has changed.
For a generically lci \(Z\), a generically independent pair mapping to
its rank-two torsion-free equation module has a determinant measuring
its cokernel divisor. This does not establish generation of the full
equation module including torsion. The
[two-filtration construction](../../frameworks/torus-supported-boundaries/weight_symbols_and_normal_filtrations.md#two-filtrations-and-the-full-normal-cone)
keeps weight and normal initials separate. The stronger
[endpoint equation-torsion theorem R-0073](../../results/endpoint_equation_torsion.md)
concerns the raw parameter family and its layers, not these normal
layers. None of these identifications can be supplied by a cycle alone.

## Remaining questions and exact support

The unresolved quartic problem concerns actual ordinary homogeneous
equations, their allowed degrees and the moving source spaces. Classifying
extra generators of invariant limits or locating their normal torsion at
endpoints does not compare the two ranks in characteristic zero. A useful
rank-one test must either prove descent with precise curve hypotheses or
give a one-parameter counterexample with its full ideal; the rank-two
example (3)--(6) does neither. For a bounded supported boundary family,
the [moving generator incidence](../torus_hilbert_boundary.md#the-moving-ideal-generator-test)
remains the actual degree-prescribed test. The endpoint budget (9) can
constrain such a family only with its real layer degrees, torsion and
multiplication, rather than ranks alone.

The prior independent reconstruction of the power argument, quartic
triple, three-line example and membership correction is recorded in
§§5–7 and 11 of the Git source
`d1973f6466d288041c2fdba3f94149169f216625:research/synthesis/torus_homogeneous_descent.md`.
Its §11 records a successful independent replay of the original
`research/computations/verify_torus_homogeneous_descent.m2` at that same
commit. These are historical review and replay records. The complete
proofs and focused native support needed here are present in the current
tree; they do not depend on retrieving that branch commit.

The focused [Singular control](equivariant_set_theoretic_descent.support/verify.sing)
checks (3)--(5), the full parameter contraction and primary decomposition,
the quartic polynomial identity and the two finite-length examples over
\(\mathbf Q\). Run from the repository root:

```sh
Singular -q research/arguments/torus/equivariant_set_theoretic_descent.support/verify.sing
```

Independent reconstruction on 2026-11-19 checked (1)–(9), including the
generality of (7), the Frobenius-pair reuse and the endpoint budget for
nonpure boundary schemes. The same reviewer inspected the focused script
before running it, then replayed all twelve controls successfully with
no parser or runtime diagnostics. A deliberately failed assertion in a
temporary copy produced a failure marker and suppressed the success
marker. Singular can still exit zero after an error: acceptance requires
the complete error-free output and the final success marker, not process
status alone. The historical M2 bundle was not replayed in this review.

This finite control does not prove the all-degree obstruction, arbitrary
characteristic statements, or general lemmas; their proofs are above.
The four-generator line and twisted-cubic controls remain in their
[full-limit](../torus_hilbert_boundary.md#a-four-generator-full-limit-with-an-embedded-point)
and [Hamiltonian-control](contact_jacobians_and_hamiltonian_actions.md#controls-and-the-precise-remaining-implication)
owners and are not duplicated here.
