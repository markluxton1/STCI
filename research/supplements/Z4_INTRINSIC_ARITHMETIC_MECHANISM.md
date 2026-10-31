# Embedded primitive towers: gluing, arithmetic variation, and actual pairs

An abstract rational curve or its normal bundle does not determine the obstruction to extending an embedded ribbon. This chapter owns the full primitive-stage extension, the comparison under quadratic gluing changes, the marked divided leading-class theorem, and explicit counterexamples showing why the full neighborhood and integral lift are essential. It then records what an actual supported complete intersection does and does not supply. These are independently reviewed provisional results, not new canonical promotions.

The embedded ribbon-to-triple extension is proved in [higher embedded structures](HIGHER_INITIAL_IDEALS_AND_EMBEDDED_THICKENINGS.md#2026-10-21-intrinsic-embedded-ribbon-triple-obstruction). The exact arithmetic example is [R-0012's nonlifting proof](Z4_LIFTING_AND_DEFORMATION.md). The full extension—not any chosen quadratic summand—has invariant meaning. Standard square-zero derivations and cotangent-complex deformation theory contextualize the construction, but do not identify it with a Frobenius-lifting or Witt-vector obstruction. Abstract primitive-multiple-curve results likewise do not by themselves solve fixed-ambient compatibility over a mixed-characteristic DVR.

## Comparing two marked quadratic neighborhoods

## Statement and source

Work over a base scheme S. Let C have two marked quadratic ambient
neighborhoods A₂ and A₂′ with a common first neighborhood A₁, common
conormal E, and identified square-zero kernels

    0 → B → A₂ → A₁ → 0,       B = Sym²(E),
    0 → B → A₂′ → A₁ → 0.

Here A₂ denotes O_X/I³, A₁ denotes O_X/I², and the action on B
factors through O_C. The neighborhoods come from regular codimension-two
immersions, so multiplication identifies I²/I³ with Sym²(E).
Fix q:E→L, a line quotient with line kernel M.

**Comparison hypothesis:** A₂ and A₂′ are locally isomorphic as
S-algebras by isomorphisms inducing the specified identity on A₁ and B.
This is a hypothesis, not a consequence asserted for arbitrary regular
immersions. All classes below use these markings.

Define the sheaf of O_C-modules

    D₂ = Der_S(A₁,B).

There is a canonical O_C-linear map

    ρ_q:D₂ → Hom(M,L²),
    ρ_q(δ) = (Sym²(q)) ∘ (δ restricted to M).

The local isomorphisms define a difference class
β(A₂′,A₂) in H¹(C,D₂). With the overlap orientation specified in the
proof, the canonical embedded obstruction classes satisfy

    o_(A₂′)(q) − o_(A₂)(q) = H¹(ρ_q)(β(A₂′,A₂)).       (1)

Thus a genuine arithmetic *gluing-defect cocycle*, if independently
constructed in D₂ with the stated compatibility, has a natural comparison
to the Yoneda obstruction. A binomial cross-effect by itself does not
supply β or a map into D₂.

The general square-zero derivation principle is described in the
[Stacks Project, Lemma 91.2.1](https://stacks.math.columbia.edu/tag/08S3).
Formula (1) is proved directly below; it is not quoted from that source.
The target obstruction is the corrected canonical extension of the
[independent intrinsic audit](HIGHER_INITIAL_IDEALS_AND_EMBEDDED_THICKENINGS.md#2026-10-21-intrinsic-embedded-ribbon-triple-obstruction).

## Proof

An automorphism f of A₂ inducing the identity on A₁ and B has
f−id valued in B. Since this difference vanishes on B, it factors uniquely as
δ:A₁→B. Multiplicativity and B²=0 give the Leibniz identity.
Conversely, writing π:A₂→A₁ for the projection, id+δπ is an
automorphism with inverse id−δπ. Composition adds derivations.
This identifies the automorphism sheaf with the additive sheaf D₂.

For e,e′ in the square-zero ideal E of A₁,

    δ(ee′) = e δ(e′) + e′ δ(e) = 0.

For a local section a of O_C, the identity
δ(ae)=aδ(e)+eδ(a)=aδ(e) shows that δ restricted to E is
O_C-linear, independently of a choice of lift of a. Restricting to M
and projecting B to L² defines ρ_q canonically. The same identity
shows this is a morphism of O_C-modules.

Choose local isomorphisms φ_i:A₂′→A₂ on an affine trivializing cover.
Define δ_ij by

    φ_i φ_j⁻¹ = 1 + δ_ij.

The δ_ij are a Čech cocycle since automorphisms add. Replacing φ_i
by (1+ε_i)φ_i changes δ_ij by ε_i−ε_j, so their cohomology
class is independent of the local isomorphisms. We take this orientation
as the definition of β(A₂′,A₂).

Each φ_i induces an isomorphism of the canonical module extensions

    Q = J₂/(I J₂+I³),       0→L²→Q→M→0,

and its counterpart Q′, inducing identity on the end terms. On Q the
automorphism 1+δ_ij acts by adding ρ_q(δ_ij) to a lift of M:
δ kills quadratic terms, and the quotient of B in Q is precisely L².
Choose local splittings s_i of Q→M and transport to Q′ by
t_i=φ_i⁻¹s_i. Then, transporting differences back via φ_i,

    t_j−t_i  corresponds to  (s_j−s_i)+ρ_q(δ_ij).

The two splitting cocycles therefore differ by ρ_q(δ_ij).
The corrected intrinsic audit identifies those splitting cocycles with
the Yoneda classes. This proves (1).

## Coordinate changes, base movement, and arithmetic scope

No normal-coordinate decomposition was used. Isomorphisms of the full
marked data transport A₁, B, D₂, ρ_q, and (1). Derivations in D₂ may
move base functions into B. Restricting them to chosen normal variables
without carrying the full A₁ structure would lose this functoriality.
The comparison fixes A₁; a coordinate change with a first-order base
displacement must first be transported to the common marked A₁.

Over a DVR with uniformizer π, if the difference cocycle is divisible
by π, its leading reduction can be sent through the reduction of ρ_q,
provided the relevant sheaves, cohomology modules, and base-change maps
have the flatness/exactness needed for division. It then computes the
leading *difference* of embedded obstruction classes. A claim about a
persistent cokernel further needs a specified quotient-lift torsor and
its divided variation map D. These conditions are not consequences of
the arithmetic polynomial Δ_(p^r).

This comparison is useful because it names the exact missing datum:
a coordinate-equivariant arithmetic class in the sheaf of quadratic
gluing derivations, rather than an isolated coefficient of a transition.
It does not identify divided Frobenius with that class, and it imposes
no additional condition on arbitrary characteristic-zero STCI pairs.

## Primitive stages and divided leading obstructions

For a regular immersion \(C\hookrightarrow X\), let \(I\) be its ideal,
\(E=I/I^2\), and fix \(q:E\twoheadrightarrow L\) with invertible kernel
\(M\). Put \(J_2=\ker(I\to L)\). The canonical extension is

\[
0\longrightarrow L^2\longrightarrow
Q_2:=J_2/(IJ_2+I^3)\longrightarrow M\longrightarrow0.       \tag{1}
\]

Its Yoneda class is
\(o_X(q)\in H^1(C,M^\vee L^2)\); it vanishes exactly when this fixed
embedded ribbon admits a primitive triple. In particular, \(I/I^3\) must
not be substituted for \(Q_2\) as an allegedly canonical
\(\mathcal O_C\)-module. Multiplication by \(I\) annihilates \(Q_2\),
which makes (1) a literal module extension.

<a id="primitive-stage-hierarchy"></a>

## 2. A primitive-stage hierarchy

**Proved proposal B1.** Let \(C\hookrightarrow X\) be a regular immersion
of codimension two, in any characteristic. Fix an embedded primitive
\(n\)-fold structure \(Z_n\), \(n\ge2\), with ideal \(J_n\), having
local form

\[
I=(z,y),\qquad J_n=(z,y^n).
\]

Its ribbon quotient has conormal line \(L\), with kernel \(M\subset E\).
There is a canonical exact sequence

\[
0\longrightarrow L^n\longrightarrow
Q_n:=J_n/(IJ_n+I^{n+1})\longrightarrow M\longrightarrow0.     \tag{2}
\]

Its splittings correspond precisely to primitive embedded
\((n+1)\)-fold ideals \(J_{n+1}\) with

\[
I^{n+1}\subset J_{n+1}\subset J_n,\qquad
J_{n+1}+I^n=J_n.                                          \tag{3}
\]

The obstruction is

\[
o_n(X,Z_n)=[Q_n]\in
\operatorname{Ext}^1(M,L^n)=H^1(C,M^\vee L^n).               \tag{4}
\]

If it vanishes, the set of compatible global extensions is a torsor under
\(H^0(C,M^\vee L^n)\).

**Proof.** In the displayed local form,

\[
IJ_n+I^{n+1}=(z^2,zy,y^{n+1}),
\]

so \(Q_n\) is freely generated over \(\mathcal O_C\) by the classes
of \(z,y^n\). The map to \(E\) has image \(M\), generated by the
linear class of \(z\), and kernel generated by \(y^n\). The image of
\(I^n\) is this kernel. The induced map from
\(\operatorname{Sym}^n E\) factors through
\(\operatorname{Sym}^n E/(M\operatorname{Sym}^{n-1}E)=L^n\),
and is an isomorphism onto the kernel. This constructs the injection
canonically rather than by a chosen frame.

A local splitting of (2) has image generated by \(z-a y^n\). Its
inverse image in \(J_n\) is

\[
(z-a y^n,y^{n+1}).                                        \tag{5}
\]

It is an ambient ideal since the action on \(Q_n\) factors through
\(\mathcal O_C\); (5) has the required primitive local form and
satisfies (3). Conversely any ideal satisfying the primitive form and
(3) gives such a splitting. Differences of splittings are exactly
\(\mathcal O_C\)-linear maps \(M\to L^n\), so the standard splitting
cocycle is the Yoneda class (4). This proves all assertions.

The construction depends only on \(\mathcal O_X/I^{n+1}\) and the
specified \(J_n\) in that neighborhood. For \(n=2\) it is the
inherited corrected theorem. For \(n>2\) it gives a useful explicit
embedded hierarchy. It does not say that varying all lower structures is
a single linear problem: each torsor is defined **after fixing** \(Z_n\).

The hierarchy is functorial under isomorphisms carrying the whole
embedded data to one another. Flat pullback preserves the constructions;
other base changes require the relevant ideals, products, and exact
sequences to remain compatible. It does not identify cohomology groups
across arbitrary base changes.

## 3. The relative divided leading-class theorem

**Proved proposal B2, with explicit relative hypotheses.** Fix a DVR
\(R\) with a chosen uniformizer \(\pi\) and residue field \(k\).
Fix an integral marked embedded lifting problem and a special quotient
\(\bar q\). Suppose:

1. The admissible lifts modulo \(\pi^2\), including the specified gauge
   normalization, form a nonempty torsor \(P\) under a \(k\)-vector
   space \(T\).
2. The canonical embedded extensions give a relative obstruction bundle
   \(\mathcal H\), locally free over the relevant parameter space.
   Its reductions at all points of \(P\) identify canonically with the
   same \(H=\operatorname{Ext}^1(M_k,L_k^2)\). These identifications
   require the asserted relative cohomology and base-change properties.
3. Each integral obstruction \(o(q)\) reduces to zero modulo \(\pi\).
   Consequently the leading reduction
   \[
   \lambda(q)=\frac{o(q)}\pi\bmod\pi\in H                 \tag{6}
   \]
   is defined using
   \(\pi\mathcal H/\pi^2\mathcal H\simeq\mathcal H/\pi\mathcal H\).
4. The leading section is affine-linear: for one, hence every, base
   point \(q_0\in P\),
   \[
   \lambda(q_0+t)=\lambda(q_0)+D(t)
   \]
   with \(D:T\to H\) \(k\)-linear.

Then \(D\) is independent of \(q_0\), and

\[
\mathfrak o(P):=[\lambda(q_0)]\in\operatorname{coker}D        \tag{7}
\]

is independent of every base-point choice and every compatible integral
trivialization. It is natural under isomorphisms of the marked integral
problem. If \(\mathfrak o(P)\ne0\), no admissible lift in \(P\)
has zero leading obstruction, so no integral primitive triple in the
specified family exists. If the class is zero, the leading obstruction
can be cancelled within this torsor, but higher precision or later
primitive stages may still obstruct.

**Proof.** Freeness makes multiplication by \(\pi\) an isomorphism
\(\mathcal H/\pi\mathcal H\to\pi\mathcal H/\pi^2\mathcal H\),
so (6) is unambiguous in the canonically reduced fiber. A frame change
\(F=F_0+\pi F_1\) changes the leading vector by \(F_0\) only:
\((F\pi v)/\pi\equiv F_0v\pmod\pi\). In particular, changes of
integral kernel frames reducing to the identity have no effect.
Replacing \(q_0\) by \(q_0+t_0\) replaces its leading vector by
\(\lambda(q_0)+D(t_0)\), and
\(\lambda(q_0+t_0+t)-\lambda(q_0+t_0)=D(t)\).
This proves base-point independence and (7). The relative extension
and reduction are functorial; under a compatible change of tangent and
obstruction frames, \(D\) changes by the corresponding source and
target isomorphisms, so its cokernel and (7) transport naturally.
Nonvanishing follows directly from the affine equation.

This proof is elementary once the relative hypotheses are established.
It does not assume that unrelated integral Ext fibers can be compared
before reduction. It also does not infer affine linearity from the word
"obstruction." A smooth first-order lift problem and a regular section
often give affine linearity by the square-zero Taylor rule, but the
admissible parameterization, gauge quotient, and base-change comparison
must still be established in the actual embedded problem.

The relevant \(D\) is the variation of the **divided first-order**
section on the marked congruence torsor. We do not identify it
unqualifiedly with the ordinary differential of the undivided section
on a reduced congruence special fiber. A uniformizer change rescales
(6) by its residue unit; vanishing is preserved, while a numerical
normalization depends on the chosen uniformizer. The formal statement
works with \(\pi\) over a ramified DVR when its hypotheses hold;
division by \(p\) then has a different valuation. The audited quartic
calculation is not thereby extended to all ramified DVRs.

## The missing arithmetic comparison

A sufficient **conditional arithmetic comparison** is now exact. An
arithmetic construction must provide a coordinate-equivariant sheaf
map \(\chi:\mathcal A\to\mathcal D_2\) and a cocycle
\(a\in H^1(C,\mathcal A)\) whose image is the actual gluing
difference \(\beta\). Its image in the embedded obstruction is then
\(H^1(\rho_q\chi)(a)\), by [the marked quadratic-gluing comparison](#comparing-two-marked-quadratic-neighborhoods). If the cocycle is divisible by
\(\pi\), compatible flatness and base change allow leading division;
if B2's affine hypotheses hold, one may then pass to the persistent
cokernel.

The universal polynomial

\[
\Delta_{p^r}(a,b)=\frac{(a+b)^{p^r}-a^{p^r}-b^{p^r}}p
\]

supplies neither \(\chi\) nor the gluing class \(\beta\).
Its additive polynomial cocycle identity is not the descent condition
for the full embedded quadratic neighborhood. No such arithmetic
\(\chi\) has been constructed here for the quartic. This names a
precise missing lemma rather than treating a numerical coefficient as
an operation in deformation theory.

The derivation source has the usual cotangent-complex interpretation
\(\operatorname{Hom}(\mathbb L_{A_1/S},B)\) in degree zero.
This does not identify the embedded group with an arbitrary
Frobenius-lifting or Witt-vector obstruction group. Those deformation
problems require their own source objects and comparison maps.

## 5. Recovery of the quartic class and its persistence

Use the accepted full Laurent coefficients, with the fixed marked
frames of the persistent audit:

\[
\begin{aligned}
C_1&=h(ah+3b^2-5bd+3d^2),\\
C_2&=(b-d)(4ah+3b^2-8bd+6d^2),\\
C_3&=a(ah+9b^2-23bd+15d^2).
\end{aligned}                                             \tag{10}
\]

The full canonical class is represented by
\(C_1[u^{-1}]+C_2[u^{-2}]+C_3[u^{-3}]\) in
\(H^1(\mathbf P^1_R,\mathcal O(-4))\).
At \(a=b=h=0,d=1\), (10) gives exactly

\[
o_X(q_0)=-6[u^{-2}].                                      \tag{11}
\]

Substitute \(a=2\alpha,b=2\beta,h=2\gamma,d=1+2\delta\).
Dividing the full coefficients by two and reducing modulo two gives

\[
\lambda(\alpha,\beta,\gamma)
=\gamma[u^{-1}]+[u^{-2}]+\alpha[u^{-3}],\qquad
D(\alpha,\beta,\gamma)
=\gamma[u^{-1}]+\alpha[u^{-3}].                            \tag{12}
\]

Here \(\delta\) is quotient-frame gauge. The inherited exhaustiveness
and surjectivity proof supplies the full admissible torsor. The image
of \(D\) has dimension two, its kernel is the \(\beta\)-direction,
and the image of \(\lambda\) in its one-dimensional cokernel is
\([u^{-2}]\ne0\). B2 explains exactly the lift independence and
relative functoriality of this cokernel class. This recovers the
known value through the full extension cocycle; it does not construct
a divided-Frobenius preimage of (11).

Coordinate invariance can be tested without isolating a raw summand.
In adapted normal coordinates an embedded triple is
\((x-a(t)y^2,y^3)\). Under an integral change with units
\(\alpha,\delta\) on \(C\),

\[
\begin{aligned}
x'&=\alpha(t)x+C(t)y^2+A(t)xy+B(t)x^2,\\
y'&=\beta(t)x+\delta(t)y+D(t)y^2+E(t)xy+F(t)x^2,
\end{aligned}
\]

its new coefficient is

\[
a'=\frac{\alpha a+C}{\delta^2}\quad\bmod I.               \tag{13}
\]

A base change \(t'=t+e(t)y+f(t)x+O(I^2)\) changes coefficients
only in order \(I\); multiplication by \(y^2\) pushes that effect
to \(I^3\). Formula (13) therefore includes moving-base changes.
For two splittings, \(a'-b'=(\alpha/\delta^2)(a-b)\), exactly
the transition of \(\operatorname{Hom}(M,L^2)\). The complete
cocycle and the relative leading class transport; its individual
coordinate summands need not.

For a nontrivial chartwise nonlinear change of the local splitting
representatives by \(1+u\) and \(v+v^2\), the normalized Laurent
representative changes by

\[
-(1+u)+u^{-4}(u^{-1}+u^{-2}),                               \tag{14}
\]

an integral Čech coboundary in \(\mathcal O(-4)\). Thus the
representative \(-6u^{-2}\) and its leading cokernel class are
unchanged. The new script verifies (13) including nonconstant base
coefficients and moving-base displacement, and (14). This is a check
of the full splitting-cocycle rule, not a fresh re-expansion of the
previously audited ambient rational chart divisions or of the
user-reported Laurent supplement.

## 6. Same conormal, different geometric obstruction

**Counterexample B3.** Work over any field \(k\). On the standard
charts of \(C=\mathbf P^1_k\), glue two copies of \(\mathbf A^2\)
by the triangular polynomial isomorphism

\[
v=u^{-1},\qquad
y_\infty=u^{-6}y_0,\qquad
x_\infty=u^{-8}x_0+c u^{-10}y_0^2.                         \tag{15}
\]

This gives an actual smooth algebraic threefold \(X_c\to C\),
affine over \(C\), with zero section \(C\). The inverse transition
is polynomial in the normal variables over \(k[u,u^{-1}]\).
For every \(c\), the conormal and quotient are identically

\[
E=M\oplus L=\mathcal O(-8)\oplus\mathcal O(-6),\qquad
q(x)=0,\quad q(y)=y.
\]

The ribbon ideal \((x_i,y_i^2)\) glues. In (1) its two local
generators are \(x_i,y_i^2\), and (15) gives normalized extension
cocycle

\[
\frac{c u^{-10}}{u^{-8}}=c u^{-2}.
\]

Since

\[
H^1(\mathbf P^1_k,\mathcal O(-4))
=\frac{k[u,u^{-1}]}{k[u]+u^{-4}k[u^{-1}]},
\]

\(o_{X_c}(q)=c[u^{-2}]\) with the chosen Čech sign. It is nonzero
if \(c\ne0\). For \(c=0\), every ideal \((x_i,y_i^n)\) glues,
so all primitive multiplicities exist compatibly.

Consequently there is no rule depending only on the identified pair
\((E,q)\), or only on functorial symmetric or divided powers of it,
whose value equals the embedded obstruction for every regular
embedding. The two examples have the **same globally split conormal**;
only the split ambient model has the asserted tower. This does not
disprove the existence of zero maps or of a more sophisticated
arithmetic comparison retaining the full neighborhood.

It also makes the distinction between symmetric and divided powers
concrete. The regular-immersion graded algebra is
\(\operatorname{gr}_I\mathcal O_X=\operatorname{Sym}E\).
The functor \(\Gamma(E)\) is determined by the same bundle and is
identical for both models. It does not supply a divided-power
structure on the ambient ideal. The divided-power identity
\(n!\gamma_n(x)=x^n\) is
[Stacks Project, Lemma 23.2.2](https://stacks.math.columbia.edu/tag/07GK).
Over an integral DVR, a nonzero
ordinary normal generator \(x\) in a polynomial algebra cannot
generally satisfy \(p!\gamma_p(x)=x^p\), since \(x^p\) is not
divisible by \(p!\) in that algebra. A divided-power envelope or a
chosen Frobenius lift is additional data, not a consequence of having
a conormal bundle.

## 7. Same special fiber, different divided obstruction

**Counterexample B4.** Over \(R=\mathbf Z_{(p)}\) or
\(\mathbf Z_p\), replace the coefficient in (15) by \(p^h c\),
where \(h\ge1\). Then

\[
o_{X_{p^h c}}(q)=p^h c[u^{-2}]
\in H^1(\mathbf P^1_R,\mathcal O(-4))\simeq R^3.            \tag{16}
\]

All these smooth integral ambients have literally the same split
special fiber, with the same \(C_k,E_k,q_k\) and the same special
neighborhoods of every order. Nevertheless the first nonzero
\(p^h\)-divided obstruction in (16) is \(\bar c[u^{-2}]\);
the split integral lift has zero obstruction. If \(h>1\), division
by \(p\) alone still gives zero modulo \(p\), as it should.

There is an equally explicit persistence statement for \(h=1\).
For the split integral ambient, every quotient \(E\twoheadrightarrow L\)
extends to a compatible primitive tower: the surjection of symmetric
algebras \(\operatorname{Sym}E\to\operatorname{Sym}L\) constructs
the embedded line subbundle, whose zero-section powers give the tower.
Its obstruction section is therefore identically zero. The difference
from this split ambient in (15) is \(p\) times a gluing derivation.
If \(q'=q+p t\) is any admissible first-order quotient lift reducing
to the same special \(q\), both restriction to its kernel and
\(\operatorname{Sym}^2(q')\) have the same reduction as for \(q\).
The [marked quadratic-gluing comparison](#comparing-two-marked-quadratic-neighborhoods) consequently gives

\[
\lambda(q')=\bar c[u^{-2}],\qquad D=0.                     \tag{17}
\]

The compatible special-fiber Ext identification is the one in B2;
here the line bundles on \(\mathbf P^1_R\) have the displayed
free cohomology modules. Thus these integral lifts can have different
persistent cokernel classes even though their entire special
geometries agree. The marked integral lift is an essential argument
of any general comparison theorem, not optional provenance.

## 8. Characteristic \(p\), normal order, and arbitrary failure stages

The inherited arithmetic identity is

\[
v_p\binom{p^r}{j}=r-v_p(j),\qquad
\Delta_{p^r}(a,b)\equiv
\sum_{k=1}^{p-1}\frac{(-1)^{k-1}}k
a^{(p-k)p^{r-1}}b^{kp^{r-1}}\pmod p.                       \tag{18}
\]

If \(a\) is a unit along \(C\) and \(b\) has normal order one,
the least normal order displayed in (18) is \(p^{r-1}\).
If **both** arguments have normal order one, every monomial instead
has total normal order \(p^r\). This distinction must be retained
when applying the polynomial to ambient coordinates.

| \(p,r\) | \(\Delta_{p^r}\bmod p\) | least order if \(a\) is a unit, \(b\) normal |
| --- | --- | --- |
| \(2,1\) | \(ab\) | 1 |
| \(2,2\) | \(a^2b^2\) | 2 |
| \(2,3\) | \(a^4b^4\) | 4 |
| \(3,1\) | \(a^2b+ab^2\) | 1 |
| \(3,2\) | \(a^6b^3+a^3b^6\) | 3 |
| \(5,1\) | \(a^4b+2a^3b^2+2a^2b^3+ab^4\) | 1 |
| \(5,2\) | \(a^{20}b^5+2a^{15}b^{10}+2a^{10}b^{15}+a^5b^{20}\) | 5 |

For example, a particular unit-versus-normal term of degree three
is invisible modulo \(I^3\). That observation does not determine
the first geometric obstruction: other transition terms, quotient
changes, or lower-order compositions may contribute. Even a visible
arithmetic term can project to zero, be a Čech coboundary, or be
cancelled by quotient variation. The split model in B3 has all
primitive powers while every polynomial in (18) is nonzero as a
universal polynomial.

There is a stronger geometric independence. For any \(n\ge2\),
replace (15) by

\[
y_\infty=u^{-6}y_0,\qquad
x_\infty=u^{-8}x_0+c u^{-10}y_0^n.                         \tag{19}
\]

The prescribed structures \((x_i,y_i^j)\) glue for every \(j\le n\).
The stage-\(n\) extension (2) has normalized cocycle

\[
c[u^{-2}]\in H^1(\mathbf P^1_k,\mathcal O(8-6n)),           \tag{20}
\]

which is nonzero for \(c\ne0\), since \(8-6n\le-4\). Equivalently,
a compatible extension would require polynomials
\(b_0\in k[u]\), \(b_\infty\in k[u^{-1}]\) solving

\[
b_0-u^{8-6n}b_\infty=-c u^{-2},
\]

which is impossible by the Laurent quotient. Hence the first failure
of this specified primitive tower can occur at an arbitrary chosen
stage over **every** characteristic. It is not predicted solely by
\(p\) or \(p^r\). This is an actual smooth ambient construction,
not a formal analogy or a generic-point calculation.

At each fixed higher stage (2), a relative analogue of B2 can be
applied if its Ext module is locally free and its divided leading
section is affine on the specified lift torsor. Those hypotheses
are substantive. At higher precision the leading section can be
nonlinear. For the elementary section \(o(q)=4+q^2\) over
\(\mathbf Z_{(2)}\), restrict to \(q=2t\). It is divisible by four,
and

\[
\frac{o(2t)}4\bmod2=1+t^2.
\]

Its ordinary differential is zero, yet it vanishes at \(t=1\).
Quotienting by the image of that differential would incorrectly
declare a persistent nonzero class at \(t=0\). This is a counterexample
to an unrestricted higher-order linear-cokernel recipe, not a claimed
geometric realization of that elementary section. The fixed-stage
torsor theorem remains valid; the family of earlier choices need not
be affine-linear in a higher divided obstruction.

## Relative Ext construction in the marked quartic problem

Let R=Z_(2), C=P1_R, E=I/I², L=O(-6). The space of surjections E→L is the open locus U in the affine R-space Hom(E,L), and its kernel M is a line bundle on C×U. Over C×U the canonical construction
`0→L²→J₂/(IJ₂+I³)→M→0`
defines a relative extension. Its obstruction section belongs to the relative sheaf `H=R¹π_*(M^∨⊗L²)`. The degree of M on every fiber is -8; on P1 over a base, a degree -8 line bundle may differ from O(-8) by pullback of a base line bundle. Thus H is a locally free rank-three bundle, not *a priori* a fixed copy of A=H¹(O(-4)). Cohomology and base change hold here because H⁰(O(-4))=0 and H¹ has constant dimension three. Over the special quotient, H_k canonically identifies with Ext¹(M_k,L_k²), without choosing an integral trivialization.

Restrict to the congruence neighborhood of the fixed special quotient. The already audited integral cocycle proves the relative obstruction is zero modulo 2 and has coefficients divisible by 2 for all integral lifts; the same polynomial identities hold universally over the mod-4 first-order parameter ring. Consequently its reduction modulo 4 belongs to `2H/4H`. Because H is locally free over the unramified base, multiplication by 2 canonically identifies `H/2H` with `2H/4H`. This gives a *leading* section λ over the first-order congruence space. The special-fiber identifications of H are canonical: changing a lift of a frame by 1+2r acts trivially on λ modulo 2. The same observation handles changes of the integral kernel identification. One must not compare integral Ext classes in distinct fibers before this reduction.

The first-order congruence fiber modulo 4 is a torsor under Hom(E_k,L_k); dividing by quotient-frame scalars reducing to 1 gives tangent `T=H⁰(Hom(M_k,L_k))=H⁰(O(2))`. The tangent identification follows from the exact sequence `0→Hom(L_k,L_k)→Hom(E_k,L_k)→Hom(M_k,L_k)→0` on global sections: the connecting obstruction lies in H¹(O)=0. A base point q0 is used to identify the torsor with T. The affine-linear λ has canonical difference map `D:T→H¹(Hom(M_k,L_k²))`; it is independent of q0 because the difference is linear. This is the differential of the *divided first-order obstruction section*, not the ordinary differential of the undivided obstruction at the special point. Its construction is natural for automorphisms of the entire marked integral embedded problem. It is not asserted invariant under arbitrary automorphisms of an unmarked P1.

## Exhaustiveness and surjectivity

The raw conormal transition from the audited main report yields exactly
`p=a+bu+3hu², q=d+2hu, P=3ac²+(3b-4d)c+h, Q=2ac+2b-3d`.
Higher coefficients vanish because the two linear relations have unit determinant. Reduction to the prescribed special quotient gives a,b,h∈2R, d∈1+2R. On the special fiber (p,q)=(0,1), so the quotient is surjective everywhere on C_k. Its cokernel is coherent on the proper R-curve; if nonzero, its closed support would meet the special fiber (properness over the local base), a contradiction. Therefore **every** such integral parameter choice is surjective. This proof does not assume q=d+2hu is a unit in R[u]. The scalar direction δ is gauge, leaving α,β,γ as the three tangent coordinates.


## Serre duality

With the usual residue convention, [u^-1],[u^-2],[u^-3] pair respectively with 1,u,u² in H⁰(O(2)). Hence `V^⊥=k·u=k·st` and the pairing of the persistent class with st is 1. The intrinsic object is the annihilator line of D, not a preferred monomial on an abstract unmarked P1.

## A coordinate summand really changes

Fix the distinguished quotient p=0,q=1,P=-4c,Q=-3, so m_V=-3A+4cB. Along X=0,Y=epsilon the quadratic coefficients are A2=-6u^-10, B2=-3u^-9, and c1=u^-4. The quadratic cocycle decomposition in the original normal coordinates is K_A=18u^-2, K_B=-12u^-2, K_move=-12u^-2, giving total K=-6u^-2.

Make the invertible integral normal-coordinate change A'=A+B, B'=B on V. Then m_V=-3A'+(4c+3)B'. The quadratic coefficient A2'=A2+B2=-6u^-10-3u^-9. Thus K_A'=18u^-2+9u^-1, K_B'=-12u^-2-9u^-1, and K_move'=-12u^-2. The total remains -6u^-2.

The difference [K_A']-[K_A]=9[u^-1] is nonzero in H^1(P1_R,O(-4))=R[u,u^-1]/(R[u]+u^-4 R[u^-1]); it even survives mod 2. Therefore the naive 'first normal coordinate' quadratic contribution does not define an intrinsic cohomology class. This disproves invariance of that decomposition, but does not disprove the existence of a more sophisticated canonical divided-Frobenius-to-obstruction construction.

## A reported Laurent stress test

This calculation was reported independently without a standalone derivation or script; it remains a reported test, not independent proof of the general invariance theorem. Its displayed difference is an explicit coboundary.

For the distinguished conormal quotient, the original Laurent cocycle is
\[
K=-6u^{-2}.
\]
Under the reported nonlinear adapted changes
\[
m_U'=X+(1+u)Y^2,\qquad
m_V'=(-3A+4cB)+(c+c^2)B^2/9,
\]
the re-expanded cocycle is
\[
K'=1+u-6u^{-2}+u^{-5}+u^{-6}.
\]
Consequently,
\[
K'-K=(1+u)+u^{-4}(u^{-1}+u^{-2}),
\]
an explicit Čech coboundary in the stated Laurent trivializations, so the two cocycles represent the same class.

**Verification boundary:** This calculation was reported after the independent audit branch was committed. No standalone calculation script or full derivation was supplied for this supplement. It tests one nontrivial global change, not the general coordinate-invariance theorem, which relies on the relative-Ext construction in the independent audit.


---

## Consequences for actual characteristic-zero pairs

## 1. Exact setup, inherited claims, and authority

Unless a statement specifies otherwise, k is an algebraically closed field of characteristic zero,

\[
C=C_0=\{[s^4:s^3t:st^3:t^4]\}\subset X=\mathbf P^3_k,
\qquad I=I_C.
\]

Let F,G be homogeneous forms of degrees d,e, with no common surface component, and put J=(F,G), Z=V(J). First one may consider only C contained in the reduced intersection; then the fundamental cycle is m[C]+R with R effective and not containing C. The STCI hypothesis used here is the stronger equality Supp(Z)=C, equivalently R=0 together with the asserted set-theoretic support. Exceptional curves above points of C on a blow-up are not additional curves downstairs.

The following are inherited premises, rather than computations repeated in this report.

* [STCI-R-0001](../results/quartic_carrier_exclusion.md), with its accepted lower-degree and factor reduction, gives d,e at least five for any characteristic-zero STCI presentation of this C. Its complete quartic-carrier exclusion is not reopened here.
* The fixed normal bundle is N=O(7) squared, hence E=I/I²=O(-7) squared. The basic generic local intersection and blow-up restrictions are recorded in [the simultaneous-surfaces synthesis](../synthesis/02-two-surfaces.md); the entirely-thick inequalities are not asserted to exclude that branch.
* [STCI-R-0012](../results/prescribed_z4_arithmetic_nonlifting.md) rules out the prescribed flat embedded Z4 lift over exactly Z_(2) and Z_2. It does not exclude arbitrary characteristic-zero STCI presentations or arbitrary ramified bases.
* The [corrected independent ribbon-to-triple audit](HIGHER_INITIAL_IDEALS_AND_EMBEDDED_THICKENINGS.md#2026-10-21-intrinsic-embedded-ribbon-triple-obstruction) constructs, for a line quotient q:E onto L with kernel M, the canonical extension

  \[
  0\longrightarrow L^2\longrightarrow B_q
  :=J_2/(I J_2+I^3)\longrightarrow M\longrightarrow0,
  \qquad J_2=\ker(I\to L).
  \tag{1}
  \]

  Its Yoneda class o_X(q) in H¹(M dual tensor L²) vanishes precisely when the fixed embedded ribbon admits an ambient embedded primitive triple. This is independently audited evidence, not a new promoted canonical record. The distinction matters: the ambient triple need not be contained in a given Z.
* The [persistent independent audit](#relative-ext-construction-in-the-marked-quartic-problem) proves the fixed marked integral first-order calculation and its precise relative meaning. In particular, every admissible integral quotient reducing to the specified q0 has a middle obstruction coefficient 2 modulo 4. This additional relative conclusion is audited evidence, rather than a broader restatement of R0012.

The [existing literature assessment](#the-missing-arithmetic-comparison) has been consulted. Its distinction between abstract multiple curves and fixed-ambient embedded extension is retained. No claim of priority over the multiple-curve literature is made for the elementary consequences proved here. The reports and the present proofs establish the stated scope; a familiar analogy with abstract extension or divided Frobenius is not being used as a theorem.

## 2. What an actual STCI presentation forces

### 2.1 Complete intersection, purity, and generic length — proved

The two equations have height two. Thus Z is a one-dimensional local complete intersection and is Cohen–Macaulay, Gorenstein, and unmixed. In the STCI situation its only associated support component is C; it has neither a residual curve nor an isolated embedded component.

At the generic point eta of C, the completed transverse regular local ring is K[[u,v]], K=k(C), and

\[
A_\eta=K[[u,v]]/(F,G)
\]

is a zero-dimensional complete intersection of length

\[
m=de/4\in\mathbf Z_{>0}.
\tag{2}
\]

The equality uses the full STCI support condition. With residual curves one only has de=4m+deg(R). If r,s are the normal orders of the displayed equations, m is at least rs; equality holds when their initial binary forms are coprime. Their first symbols need not generate the full initial ideal: (u²,u²+v³)=(u²,v³) is the basic cancellation example.

The maximal ideal of a local Artin algebra of length m has m-th power zero. Since O_Z injects into its localization at the unique generic associated point, this gives, sheaf-theoretically,

\[
I^m\subset J\subset I.
\tag{3}
\]

The injection follows from unmixedness: every function outside the prime of C is a nonzerodivisor. It is not inferred merely from equality of cycles. A larger finite power also suffices for every spreading argument below.

### 2.2 First-normal information and its exact limitations — proved

Write N1=image(J to E). If at least one equation has generic normal order one, N1 has generic rank one and A_eta is curvilinear, isomorphic to K[z]/(z^m). The saturation M of N1 in E is a line subbundle; its quotient L=E/M is invertible. On the smooth curve there is a unique effective divisor D such that

\[
N1=M(-D).
\tag{4}
\]

Here D is the common zero divisor of the *actual two first-normal symbols*, measured in their saturated line. It is not one of the divisors D_i of a saturated quasiprimitive order filtration. In particular it should not be silently substituted into [R0019](../results/quasiprimitive_residual_cycles.md).

If L=O(epsilon-7), then M=O(-7-epsilon), epsilon is nonnegative, and the two symbols are sections of

\[
M(4d)=O(4d-7-epsilon),\qquad
M(4e)=O(4e-7-epsilon).
\tag{5}
\]

One symbol can be zero identically. Where both vanish, both surfaces are singular along C in their normal directions. Saturation extends the generic direction, but does not supply a primitive triple in Z.

If both generic orders are at least two, N1=0; there is no preferred line quotient of E forced by the pair. The higher first relation, horizontal common-direction curve, and full initial ideal then require the additional hypotheses in such results as [R0006](../results/actual_ci_smooth_root_bridge.md). Neither the arithmetic Z4 result nor the construction (1) fills those interfaces.

<a id="defect-twisted-vanishing"></a>

## 3. A new necessary condition: defect-twisted obstruction vanishing

### Proposition A — proved

Let C be a smooth integral curve regularly embedded with codimension two in a smooth threefold, over any field. Let J be an ideal with support C, whose generic transverse algebra is curvilinear of length m at least three. Assume its first-normal image has rank one, and define M,L,D by (4). Set H=M dual tensor L². Then

\[
o_X(q)\longmapsto0
\quad\text{under}\quad
H^1(C,H)\longrightarrow H^1(C,H(D)).
\tag{6}
\]

Equivalently,

\[
o_X(q)\in
\operatorname{im}\bigl[H^0(C,H(D)/H)\longrightarrow H^1(C,H)\bigr].
\tag{7}
\]

Thus the ambient extension may have a nonzero obstruction, but the actual pair supplies a meromorphic splitting with poles bounded by its first-normal defect divisor. This assertion does not claim that the corresponding triple is globally contained in Z.

**Proof.** Since the first symbols of J lie in M, one has J contained in J2. Map J into B_q in (1), and let P be its image. This is an O_C-module: multiplication by I kills B_q. Its image under B_q to M is exactly N1=M(-D).

At eta choose adapted transverse parameters f,y with J_eta=(f,y^m); the existence of f with nonzero linear part follows from generic curvilinearity. For m at least three, y^m maps to zero in B_q because I³ is killed. The image of f spans a line that projects isomorphically to M_eta. Hence P_eta meets L²_eta trivially.

The kernel of P to M is a subsheaf of the line bundle L². It has generic rank zero, so it is zero on the integral curve. Consequently P is isomorphic to N1. Its inclusion in B_q is a lift of N1 to B_q and therefore a splitting of the pullback of (1) along N1 to M. Pullback of extensions induces the map

\[
\operatorname{Ext}^1(M,L^2)\to
\operatorname{Ext}^1(M(-D),L^2)
=H^1(H(D)),
\]

which proves (6). The long exact sequence of 0 to H to H(D) to H(D)/H to 0 proves (7). All images here are sheaf images; no unproved flatness of an ordinary associated graded is used. The proof fails for m=2 because the second generator y² survives in L². End of proof.

For projective C, Serre duality gives the equivalent incidence condition

\[
\langle o_X(q),V\rangle=0
\quad\text{for every}\quad
V\in H^0(C,\omega_C\otimes H^{-1}(-D)).
\tag{8}
\]

This form makes explicit which divisor data would have to be imposed on the actual homogeneous first symbols.

### Concrete corollary for the distinguished q0 — proved, restricted direction

For the fixed quartic and the distinguished marked characteristic-zero quotient q0 from the integral calculation,

\[
L=O(-6),\quad M=O(-8),\quad H=O(-4),\qquad
o_X(q0)=-6[u^{-2}].
\]

If a characteristic-zero STCI pair has generic normal order one and its saturated quotient is this q0, then its divisor D in (4) satisfies

\[
\deg D\ge2.
\tag{9}
\]

If deg D=2, write its defining binary quadratic in the marked coordinates as

\[
Q_D=A s^2+B st+C t^2.
\]

Then a further necessary condition is B=0. For deg D at least three the first obstruction in (6) is automatically killed, so this argument gives no further restriction.

**Proof.** Under the audited Laurent/Serre pairing, [u^-2] is the functional extracting the middle coefficient of a binary quadratic. For D=0 it is nonzero. For D=P a point, H0(O(2)(-P)) is the kernel of evaluation at P. A nonzero functional annihilates this kernel exactly if it is proportional to evaluation at P. The evaluation functionals have coordinates [a²:ab:b²]; none equals [0:1:0] in characteristic zero. Thus degree one cannot work. In degree two, H0(O(2)(-D)) is spanned by Q_D and (8) is exactly B=0, including nonreduced divisors. In degree at least three H¹(O(-4+D))=0. End of proof.

This is a condition on actual surface singularity/common-zero data. It does not assert that any such pair exists, or that the incidence condition suffices to lift all later stages. The q0 label includes the chosen integral embedding and marking; it is not assigned to every quotient of degree -6.

### Size of the unrestricted first obstruction — proved

For any line quotient of E=O(-7) squared with L=O(epsilon-7),

\[
H=M^\vee\otimes L^2=O(3epsilon-7),\qquad
h^1(H)=\max(0,6-3epsilon).
\tag{10}
\]

Therefore the first embedded ribbon-to-triple obstruction vanishes for **every** such quotient when epsilon is at least two. All those ribbons have ambient embedded primitive triples, irrespective of whether a particular STCI scheme contains them. In the accepted order-one range 0 at most epsilon at most 6, only epsilon=0 or 1 can be detected at this first stage.

Even epsilon=1 does not uniformly obstruct. The inherited full cubic coefficient formulas are

\[
\begin{aligned}
C_1&=h(ah+3b^2-5bd+3d^2),\\
C_2&=(b-d)(4ah+3b^2-8bd+6d^2),\\
C_3&=a(ah+9b^2-23bd+15d^2).
\end{aligned}
\tag{11}
\]

The distinguished parameters (a,b,d,h)=(0,0,1,0) give (0,-6,0). By contrast (0,1,1,0) gives (0,0,0). The latter quotient is surjective on both charts: its local pairs are (p,q)=(u,1) and (P,Q)=(-c,-1). Thus there is an actual unobstructed quotient of the same degree. It does not reduce to the prescribed q0 modulo two, so there is no conflict with the marked integral obstruction.

## 4. Exactly when an actual pair supplies a primitive triple

### Proposition B — proved: an all-points sufficient condition

Suppose locally at **every** point of C there is f in J with nonzero linear normal coefficient, and

\[
J\subset(f)+I^3.
\tag{12}
\]

Then J3=J+I³ is a globally defined embedded primitive triple, contained in Z. Its local ideal is (f,y³) for I=(f,y); its ribbon is induced by the first-normal image, and its obstruction (1) vanishes.

Indeed (12) and f in J give J+I³=(f)+I³=(f,y³). These local expressions concern one global ideal J+I³, so no extra gluing choice is being assumed. The condition is pointwise, rather than merely generic.

In particular, if Z is an actual local complete intersection with support exactly C, generic multiplicity m at least three, and its first-normal image is a line subbundle of E **everywhere** (D=0), then it is locally a primitive m-fold structure and Proposition B applies. To prove this, choose f in J generating the first-normal image at a given point. The surface W=(f) is smooth there and C is Cartier on W, say with equation y. The remaining equation has zero support exactly C on W. The regular local ring of W is factorial, so that equation is a unit times y^m. Its exponent is the generic multiplicity. Thus J=(f,y^m), and (12) follows. The same proof works relatively over a DVR for a smooth relative setup with this everywhere rank-one condition and the asserted total support.

Proposition A recovers ambient vanishing when D=0; the local support argument in this paragraph additionally proves containment of the primitive triple in Z.

<a id="generic-primitivity-counterexample"></a>

### Counterexample C — generic primitivity does not globalize

Let C be the line V(x,y) in projective three-space with coordinates [t:x:y:w], and consider the complete intersection

\[
Y=V(x^2,y^2+t x).
\tag{13}
\]

Its support is exactly C. The two *integral* quadrics

\[
F=x^2+y^2+t x,\qquad G=x^2+2y^2+2t x
\tag{14}
\]

generate the same ideal, since 2F-G=x² and G-F=y²+t x. Each has rank three in characteristic zero, hence is irreducible even over the algebraic closure.

On w=1 the algebra is free over k[t] with basis 1,x,y,xy: it is a monic quadratic extension of k[t][x]/(x²). Where t is invertible,

\[
(x^2,y^2+t x)=(x+y^2/t,y^4),
\]

so Y is generically primitive of multiplicity four. At the point t=0, however, its transverse algebra is k[x,y]/(x²,y²). There is no surjection from this algebra to k[z]/(z³). Any such map sends x to az+bz² and y to cz+dz²; squaring forces a=c=0, so the images cannot generate z. A primitive triple inside Y near that point would be finite flat of rank three over the local t-axis and would give exactly this forbidden quotient after setting t=0. Hence no global primitive triple is contained in Y.

There is nevertheless a global embedded ribbon V(x,y²) contained in Y. Its quotient has M=L=O_C(-1), so its *ambient* obstruction lies in H¹(O(-1))=0. The ambient primitive triple V(x,y³) exists, but is not contained in Y: y²+t x maps to y². Thus even an actual induced ribbon and a vanishing ambient Yoneda class do not establish the missing containment implication. The generic triple kernel x+y²/t displays the unavoidable pole.

This example disproves the general implication using a smooth projective support and integral defining surfaces. Its support is a line, not C0. It does not disprove a possible special theorem using extra geometry of C0. Such a theorem must supply that additional argument; generic local complete intersection or generic curvilinearity is insufficient.

For completeness, even generic primitivity itself need not hold for a complete intersection: (u²,v²) in K[[u,v]] has embedding dimension two and no curvilinear length-three quotient by the same argument. Its Gorenstein property does not change this fact.

## 5. Spreading out: what survives, and what does not

### Proposition D — proved: support-preserving finite-type spread

For a characteristic-zero STCI pair of the fixed C there is a finite-type integral Z-algebra A contained in k and forms F_A,G_A of the same degrees such that

\[
I_A^N\subset(F_A,G_A)\subset I_A
\tag{15}
\]

as ideals, for some finite N, and every field fiber has reduced support exactly C. One may arrange that Z_A is a flat relative complete intersection of type (d,e).

**Proof.** Projective support equality gives height two for (F,G). Its homogeneous quotient is Cohen–Macaulay of depth two, so (F,G) is saturated. Hence its homogeneous radical is I_C and some homogeneous power I_C^N lies in (F,G). This explains the passage from sheaf support to homogeneous polynomial identities.

The fixed integral model of C can be given by

\[
\begin{aligned}
q&=x_0x_3-x_1x_2,& f&=x_1^3-x_0^2x_2,\\
h&=x_1^2x_3-x_0x_2^2,& g&=x_2^3-x_1x_3^2.
\end{aligned}
\]

It is the standard relative P¹: on x0 nonzero the chart is A[u] with coordinates (1,u,u³,u⁴), and on x3 nonzero it is the analogous chart A[c]. These charts cover the projective scheme, since x0=x3=0 forces x1=x2=0 at every homogeneous prime.

Choose finite membership identities expressing F,G in this ideal and each monomial generator of its N-th power in (F,G). Adjoin to Z every coefficient in those identities and in F,G. The resulting domain A is finite type, and the identities hold over A and after **every** base change. Thus every field fiber has the prescribed radical. This argument does not assume that tensor product preserves injections.

Every field fiber is then a height-two intersection of the same two positive-degree forms, hence a regular sequence. The fiberwise regular-sequence flatness criterion gives A-flatness of O_Z and the relative regular sequence; see [Stacks, Lemma 10.99.3, tag 00MG](https://stacks.math.columbia.edu/tag/00MG). Alternatively, generic flatness followed by a principal-open shrink suffices, and leaves the identities intact. End of proof.

The fixed Hilbert polynomial is

\[
P_Z(n)=de\,n+de(4-d-e)/2.
\tag{16}
\]

Generically defined conormal quotients can also be spread after enlarging A and shrinking: descend the morphism to O(l) on P¹_A, then remove the proper image of its nonsurjectivity locus. Properness of C_A makes that image closed, and the kernel is then a line bundle. This is an existence statement after localization; it gives no control over which residue characteristics survive. A primitive triple that actually exists over k can similarly be spread, but that does not mean its flat closure is primitive over every originally chosen special point.

Over a general finite-type integral Z-algebra, the locus removed by shrinking is a proper closed locus, **not necessarily finitely many points or rational primes**. In particular, A[1/2] is always another valid spread of the same characteristic-zero data. Therefore no existence theorem for a spread can force a characteristic-two fiber. Nor does a finite-type coefficient ring supply a map to Z_(2) or Z_2: coefficient fields, transcendental parameters, residue fields, and possible ramification all matter.

### Direct reduction to Z4 is numerically impossible for a surviving pair

By R0001 and its accepted lower-degree/factor consequences, d,e are at least five; by (2), four divides de. The smallest possible product is 36, from (6,6), so

\[
m\ge9.
\tag{17}
\]

The prescribed Z4 has degree 16 and generic multiplicity four. A flat complete-intersection family of degrees (d,e) specializing to it must satisfy equality of (16) with 16n-32. This forces de=16 and d+e=8, hence d=e=4. Thus the **whole** intersection scheme of a hypothetical surviving STCI pair cannot specialize flatly to Z4. This degree obstruction is independent of its arithmetic nonlifting.

Extracting a degree-16 intermediate structure would avoid that particular degree mismatch, but requires a global primitive fourth stage, a compatible integral extension of that stage, and the exact marked special fiber. None is forced by an arbitrary STCI. Counterexample C shows why generic primitive stages are not enough.

### Conditional arithmetic corollary — proved under explicit model hypotheses

Suppose a hypothetical characteristic-zero pair admits a model over R=Z_(2) or Z_2, in the fixed relative quartic embedding, such that the total support is C_R, the family is flat, its first-normal image is a line subbundle at every point of C_R, its generic multiplicity is at least three, and its induced quotient reduces to the distinguished q0 of the marked arithmetic problem. Then this model cannot exist.

Indeed Proposition B gives a relative primitive triple. Its canonical extension (1) must split over R. The audited full admissible-quotient calculation gives middle coefficient 2 modulo 4 for every integral quotient reducing to q0, contradicting such a splitting. This rules out a particular kind of *good marked reduction*, for any multiplicity at least three. It does not assert that a hypothetical characteristic-zero STCI must possess such a model. For a total special fiber equal to prescribed Z4, the independently stronger full nonlifting statement is precisely the promoted R0012, with its two-DVR limitation.

Flatness cannot be omitted in descent arguments. Over a DVR, generic containments extend to the total scheme when the target quotients O_Z and O_C are torsionfree, but quotient flatness is what also identifies the base-changed ideal with the actual special-fiber ideal via Tor vanishing. An ideal itself is torsionfree without its quotient being flat: (2x,x²) in Z_2[x] is an elementary counterexample.

## Verification and the unproved bridge

The [general-mechanism verifier](../computations/verify_z4_general_mechanism_2026_10_21.py) retains the full Laurent variation, nonlinear adapted coordinate change, arbitrary-stage local models, binomial order examples and nonlinear divided-section counterexample. The [actual-pair consequences verifier](../computations/verify_z4_stci_consequences_2026_10_21.py) retains the quotient values, Serre-dual incidence, integral-quadric ideal identities and CI Hilbert-polynomial arithmetic. The mathematical proofs carry the uniform and global statements; the finite controls do not replace them. The inherited independent review reconstructed the gluing comparison, defect-twisted vanishing, all-points containment bridge, projective counterexample and spreading argument. Those inherited mechanism and consequence scripts were not rerun during consolidation; the separate raw-frame reconstruction below was executed.

A general arithmetic explanation still requires a coordinate-equivariant source cocycle and a map to the actual gluing derivations that reproduces the embedded difference. An unrestricted STCI application additionally requires actual homogeneous symbols to force an incompatible quotient/defect incidence or a global compatible primitive stage. Neither follows from generic primitivity, the existence of a ribbon, a vanishing ambient obstruction, or spreading out alone. The explicit counterexamples above are mathematical limits on those proposed bridges.


## Raw-frame attribution of the middle Laurent coefficient

This exact decomposition is made only in the prescribed raw integral coordinates. The counterexample above proves that its summands do not define invariant classes. The complete raw-frame calculation was reconstructed exactly and independently reviewed during consolidation. Its individual summands remain coordinate dependent; the total obstruction and its arithmetic nonvanishing are the invariant conclusions.

Let p=a+bu+3hu^2, q=d+2hu; P(c)=3ac^2+(3b-4d)c+h, Q(c)=2ac+2b-3d. Set c0=u^-1, c1=u^-4q-u^-5p, A1=3u^-8p-4u^-7q, B1=2u^-7p-3u^-6q,
A2=-9u^-12p^2+16u^-11pq-6u^-10q^2,
B2=-5u^-11p^2+9u^-10pq-3u^-9q^2.

The quadratic cocycle K=u^8([epsilon^2]m_V+u^-8[epsilon^2]m_U) decomposes as
K_A=u^8 Q(c0) A2,
K_B=-u^8 P(c0) B2,
K_move=u^8 c1(Q'(c0) A1-P'(c0) B1).
Terms involving arbitrary quadratic embedding corrections cancel against the linear kernel transition. These formulas are an **exact equality in the chosen frame**, not an invariant direct sum of cohomology classes.

For the distinguished quotient p=0,q=1,P=-4c,Q=-3:
K_A=18u^-2, K_B=-12u^-2, K_move=-12u^-2;
K=-6u^-2. The -6 in A2 comes directly from binomial(4,2); the other contributions are divisible by four.

For the full admissible quotient family, individual summands can acquire nonzero middle residues that cancel. Their exact middle Laurent coefficients are needed; parity of one factor alone does not show its product vanishes modulo four.

Exact symbolic extraction gives middle Laurent coefficients:
[K_A]_-2 = -88abh+114adh-18b^3+59b^2d-60bd^2+18d^3;
[K_B]_-2 = 82abh-102adh+15b^3-47b^2d+45bd^2-12d^3;
[K_move]_-2 = 10abh-16adh+6b^3-23b^2d+29bd^2-12d^3.
Their sum is C2=(b-d)(4ah+3b^2-8bd+6d^2).
Substitute a=2α,b=2β,h=2γ,d=1+2δ. Modulo four the three middle coefficients are respectively **2,2β,2β**. The latter two cancel in the total, leaving C2=2 modulo four. The earlier raw-frame source attributed residues (2,0,0) to all quotients; that claim was incorrect when β is odd. At the distinguished quotient β=0 the displayed (18,-12,-12) values remain correct. This correction changes the attribution, not the reviewed total cocycle or nonlifting theorem.

This does not construct a natural map from divided-power polynomials to H^1(O(-4)). In particular, a change of raw normal coordinates changes the allocation among K_A, K_B and K_move. The total class is intrinsic for the fixed quotient, but the decomposition is not proved invariant.


The source cited a verifier that is absent from the covered snapshots. Its necessary support is replaced by [the exact Laurent reconstruction](../computations/verify_z4_raw_source_decomposition.py), which derives all three middle polynomials from the displayed raw-frame definitions, checks their sum against C2, and performs the formal parameter substitution modulo four. It was executed successfully during consolidation. This fixed-frame identity does not assert invariance of individual pieces.
