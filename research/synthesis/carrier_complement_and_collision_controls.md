# Carrier complements and a first-conormal collision

Two controls clarify the limits of carrier methods. A complete curve
disjoint from the target obstructs an affine complement on a specified
carrier. A multiple first-conormal root need not persist into the next
blowup. The first control concerns smooth rational **quintics**, not the
fixed quartic; the second is an explicit equation containing the fixed
quartic, with no asserted global normality or STCI mate.

**General complement criterion.** If \(D\) is an integral effective
divisor with \(D^2>0\) on a smooth projective surface, then
\[
S\setminus D\text{ affine}\ \Longleftrightarrow\ D\text{ ample}
\ \Longleftrightarrow\ \text{no complete curve is disjoint from }D.
\]
Affineness forbids a positive-dimensional proper closed curve. Conversely,
distinct integral curves have nonnegative intersection, and zero
intersection is exactly disjointness. The last condition and \(D^2>0\)
therefore give positive intersection against every curve, so the
Nakai--Moishezon criterion makes \(D\) ample. For an ample effective
Cartier divisor, embed by a sufficiently large multiple; its complement
is the closed intersection of the surface with an affine hyperplane
complement, hence affine. This proof works in every characteristic.
The positive-square hypothesis and irreducibility are part of the
criterion; they are not consequences of a support-only statement.
For the fixed quartic on its smooth quadric, the class \((1,3)\) is
ample, so that complement is affine. Nevertheless no \((b,b)\) ambient
section can have sole divisor support a multiple of \((1,3)\). Thus even
a successful affine-complement test on one carrier does not supply its
second homogeneous equation.

## 1. Every smooth cubic containing a smooth rational quintic has five disjoint lines

Let \(X\) be a smooth cubic surface over an algebraically closed
characteristic-zero field, \(H=-K_X\), and \(C\subset X\) smooth
irreducible rational with \(HC=5\). Then exactly five mutually disjoint
lines on \(X\) are disjoint from \(C\). In particular \(X\setminus C\)
is not affine. The statement is conditional on lying on a smooth cubic;
it does not say every smooth rational quintic has such a carrier.

**Proof.** Choose a six-line plane blowdown marking and write
\[
H=3h-\sum_{i=1}^6e_i,\qquad C=ah-\sum b_ie_i.
\]
Adjunction gives \(C^2=3\), so
\[
\sum b_i=3a-5,\qquad\sum b_i^2=a^2-3.
\]
The 27 lines have classes \(e_i\), \(h-e_i-e_j\), and
\(2h-\sum_{j\ne i}e_j\). Because \(C\) is irreducible and distinct
from every line, its intersections with each are nonnegative. In
particular \(b_i\ge0\) and \(a-b_i-b_j\ge0\). This step would fail
for an arbitrary effective divisor containing a line component.

Order \(b_1\ge\cdots\ge b_6\). If \(b_1+b_2+b_3>a\), the quadratic
change of marking replaces
\[
a\mapsto2a-b_1-b_2-b_3,
\quad(b_1,b_2,b_3)\mapsto
(a-b_2-b_3,a-b_1-b_3,a-b_1-b_2).
\]
This is an actual change to six disjoint exceptional lines, preserves
the two equations, keeps all coefficients nonnegative, and strictly
decreases \(a\ge2\). It terminates with
\(a\ge b_1+b_2+b_3\). Then
\(b_4+b_5+b_6\le3b_3\le a\), hence \(3a-5\le2a\) and
\(2\le a\le5\). The complete ordered solutions in that range are:

| \(a\) | \((b_1,\ldots,b_6)\) | reduced? |
|---:|---|---|
| 2 | \((1,0,0,0,0,0)\) | yes |
| 3 | \((2,1,1,0,0,0)\) | no |
| 4 | \((3,1,1,1,1,0)\), \((2,2,2,1,0,0)\) | no |
| 5 | \((3,3,1,1,1,1)\), \((3,2,2,2,1,0)\) | no |

Thus the reduced class is \(2h-e_1\). Its intersections with the 27
lines have distribution \(0^5,1^6,2^{10},3^5,4^1\). The five zero
lines are exactly \(e_2,\ldots,e_6\), and are mutually disjoint. Each
remains a positive-dimensional proper closed curve in \(X\setminus C\),
which an affine scheme cannot contain. \(\square\)

This extends the obstruction from one chosen smooth cubic to every
smooth cubic containing the same eligible quintic. It does not address
singular cubics or higher-degree carriers. The lattice calculation is
characteristic-free once the standard six-line marking is available;
the inherited source review established the statement in characteristic
zero and did not separately verify its all-characteristic application.

There are two further consequences for this same eligible quintic.
No plane contains it, by degree. A containing quadric would cut an
effective residual divisor \(R=2H-C\) on \(X\), with \(HR=1\) and
\(R^2=-5\). Ampleness of \(H\) makes an effective degree-one divisor
an actual line, whose square is \(-1\), a contradiction. Consequently
every containing cubic is irreducible and reduced: a factorization into
lower-degree forms would put the irreducible \(C\) on one of those
excluded plane or quadric factors. A pencil of two distinct containing
cubics with one smooth member has a nonzero positive-degree discriminant
section; over an algebraically closed field it has a zero. Thus it also
contains singular **integral** cubic members. This produces singular
carriers without classifying their singularities or their complements.

## 2. A one-node cubic: the complete degree-one obstruction

Let \(X\) be an integral cubic whose only singularity is one \(A_1\)
point, and let
the smooth rational quintic \(C\) avoid that point. Its crepant weak
del Pezzo resolution has hyperplane class \(H=-K\), exceptional root
\(\alpha\), and strict curve \(D\) with
\(HD=5,D^2=3,D\alpha=0\).

Choose \(\alpha=(0;-1,1,0,0,0,0)\) in the six-point marking. Exactly
15 of the 27 numerical \((-1)\)-classes \(\ell\) are orthogonal to it.
Each such class is effective without assuming a line correspondence:
Riemann--Roch gives \(\chi(\ell)=1\), while
\(H(K-\ell)=-4<0\) gives \(h^2(\ell)=0\), hence \(h^0(\ell)\ge1\).
Since \(H\ell=1\), an effective representative has a noncontracted
degree-one component whose image is a complete line on \(X\).

An effective degree-one divisor cannot contain the irreducible degree-five
\(D\), so \(D\ell\ge0\). Write \(D=(a;b_1,\ldots,b_6)\). Cauchy
applied to its degree and square equations gives
\[
(3a-5)^2\le6(a^2-3),\qquad2\le a\le8.
\]
The [exact lattice enumeration](../computations/nodal_cubic_quintic_lattice.py)
retains **all signed** integral \(b_i\) in their square bound, checks
\(D\alpha=0\) and the 15 inequalities, and finds 120 classes. Each has
zero intersection with exactly three of those 15 classes. Every component
of a chosen effective representative has nonnegative intersection with
\(D\), so total zero forces its degree-one component to be disjoint
from \(D\). Its image is disjoint from \(C\), including the node because
\(C\) avoids it. Thus \(X\setminus C\) is not affine.

One disjoint image line suffices; the calculation does not establish that
all three numerical zeros give distinct image lines. Higher ADE types,
multiple nodes, nonnormal cubics, and curves through the node are outside
the statement. The source labeled its second argument independent, but
its recorded creator was the same lead. Consolidation review has now
independently reconstructed the proof and finite bound, reduced the 15
inequalities, and enumerated all 120 classes in a separate standard-library
calculation, obtaining three zero intersections in every case. This
discharges the earlier independence gap without relying on the label.
The standard one-node crepant model and the exact finite
enumeration are the essential inputs. In characteristic two the ordinary
quadratic-form and resolution assumptions require separate treatment;
no positive-characteristic extension is asserted from the lattice alone.

## 3. The corrected coordinate quintic benchmark and its singularity incidences

[Hartshorne--Polini, Example 7.10(2)--(3)](https://arxiv.org/html/1907.05472#S7)
place Vahlen's rational quintic in class \((2;1,0^5)\) on a smooth cubic.
They construct its set-theoretic presentation by two cubics and a quartic.
The quadrisecant forces every containing cubic to contain a residual
line. Their construction does not settle whether some other carrier
has affine complement or whether two equations suffice.

An exact rational benchmark realizes the divisor configuration by blowing
up the six points
\[
(1:0:0),(0:1:0),(0:0:1),(1:1:1),(1:2:3),(1:3:2)
\]
and using the cubic sections
\[
\begin{aligned}
U_0&=17x^2y-18x^2z-7xy^2+8xyz,\\
U_1&=40x^2y-40x^2z-8xy^2+8xz^2,\\
U_2&=47x^2y-30x^2z-25xy^2+8y^2z,\\
U_3&=95x^2y-78x^2z-25xy^2+8yz^2.
\end{aligned}
\]
The conic \(xz+y^2+z^2=0\), parametrized by
\((x:y:z)=(-(s^2+t^2):st:t^2)\), gives the rational quintic after
removing its common parametrization factor. The exact source
[vahlen_quintic_exact.py](../computations/vahlen_quintic_exact.py)
retains the binary quintic, cubic equation, all exact substitution
kernels, and the finite-degree rank calculations. It verifies
\(\dim I_C(d)=0,0,4,14\) for \(d=1,2,3,4\), with one new minimal
quartic class modulo linear multiples of cubics. This finite-degree
calculation does not prove generation of the full saturated ideal.
The model realizes the stated divisor configuration; uniqueness of a
projective class named Vahlen's quintic was not established.

The residual conic \(7x^2-5xy-5xz+3yz=0\) maps to the **corrected** line
\[
G=V(3U_2-5U_0,\ 3U_3-5U_0-5U_1).                    \tag{11}
\]
The [direct reconstruction](../computations/vahlen_base_locus_discriminant.py)
derives (11) from rational conic points and verifies every cubic-kernel
member vanishes on it. The earlier differently printed linear forms
must not be reused. Intrinsically the same containment follows because
a degree-three form on a line cannot vanish on a length-four intersection
without vanishing identically.

Writing a cubic in the coefficient \(\mathbf P^3\) as
\(F=\ell_1Q_1+\ell_2Q_2\), with \(\ell_i\) the equations of (11),
its singularities on \(G\) are exactly the common zeros of
\(Q_1|_G,Q_2|_G\). Their binary-quadratic resultant is a nonzero
homogeneous quartic in the four cubic coefficients. The same exact
source exhibits a nonzero \(2\times2\) minor of the normal-gradient
evaluation matrix on \(C\), so a general point of \(C\) has a
\(\mathbf P^1\) of containing cubics singular there. This is an
incidence surface before projection; its image degree, generic singularity
type, and overlap with the on-\(G\) locus remain uncomputed. These are
two exact partial strata, not a full discriminant factorization or a
complement theorem. All arithmetic is over \(\mathbf Q\); special-prime
rank, smoothness and denominator behavior are not asserted.

## 4. A fivefold conormal zero can disappear after one blowup

For the fixed quartic in coordinates \((x,y,z,w)\), put
\[
\begin{aligned}
F_{\rm coll}={}&x^3w-2x^2yz+10x^2z^2-10xy^2w-16xyz^2+16xz^3\\
&-10xz^2w+xw^3+y^4+16y^3w-16y^2zw+10y^2w^2\\
&-2yzw^2+z^4,
\end{aligned}
\]
and \(H(t)=(t-1)^5(1+5t+5t^2+t^3)\). Exact substitution and
differentiation give
\[
F_{\rm coll}|_C=0,\qquad
\nabla F_{\rm coll}|_C=(t^4,-2t^3,2t,-1)H(t),
\]
including the projective endpoint, and exclude a factor of the unique
quadric. Near \(t=1\), write \(t=1+\tau\),
\(z=t^3+r,w=t^4+tr+q\). Its normal quadratic term is
\(9r^2-18rq+11q^2\), of determinant 18; its first normal-linear term
is \(12\tau^5(r-q)\). Completing the normal square gives first pure
term \(-4\tau^{10}\). Characteristic-zero formal Morse splitting
therefore gives an \(A_9\) germ.

The actual first blowup chart \(q=r(t+v)\) has exceptional restriction
\(-H(t)v\), so the local first contribution is five. Its strict
transform has nonzero \(r\)-coefficient two at the selected section,
hence is smooth there after this blowup. The local smooth-curve pair is
\(A_{9,5}\), with type \((5)\): its second contribution is zero.
The remaining cubic factor has three distinct roots and is coprime to
the simple-root tangent determinant
\(10-16t+16t^3-10t^4+2t^6\); those points are \(A_{1,1}\).
The complete type for this displayed equation is \((8)\), with second
entry zero. The exact polynomial, Taylor and blowup calculations are
retained in [c4_root_collision.py](../computations/c4_root_collision.py),
with its [conormal dependency](../computations/c4_conormal.py).

Thus coalescing first-normal roots while retaining the same normal
direction need not create higher iterative depth. A high ADE label is
not a substitute for checking the next strict transform. This is an
example, not a claim that every repeated root has second entry zero,
or that \(F_{\rm coll}\) is globally irreducible, normal, paired with
a quintic, or an STCI presentation. Its obsolete degree-\((4,5)\)
search motivation is unnecessary: the local distinction remains useful
after the all-quartic theorem.

The displayed formal argument assumes characteristic zero. Reduction
modulo two or three destroys the nondegenerate normal quadratic; other
positive characteristics also require checking the residual roots and
the actual coefficients and local branch hypotheses. No blanket
positive-characteristic \(A_{9,5}\) assertion follows from its integral
polynomial.

**Review state.** The smooth-cubic proof had a separate mathematical
reconstruction in its source. The nodal enumeration and the collision
retain their explicitly bounded source evidence and limitations; no
fresh execution or promotion is claimed by transferring them. The
coordinate correction is incorporated into (11) and the source-script
consumer. Independent consolidation review must compare these proof
homes with their proposed archived-source removals.
