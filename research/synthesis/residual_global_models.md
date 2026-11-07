# Actual equation spaces, prescribed attachments, and two global models

Work with the fixed embedded rational quartic \(C=C_0\), over an
algebraically closed characteristic-zero field unless a local or cohomological
statement explicitly allows arbitrary characteristic. This account consolidates
reviewed mathematics. Its purpose is
to keep existence constructions visible together with necessary conditions.
The [capacity chapter](residual_capacity_and_constructions.md) distinguishes
marked and full-primary attachment; [residual intersections](residual_intersections_and_jets.md)
owns the earlier explicit quartic laboratories and valuation comparisons.



## General containing pairs and their attachment morphism

## 2. The general picture in every bidegree \(a,b\ge4\)

Put \(V_d=H^0(I_C(d))\). The curve has type \((1,3)\) on its smooth containing
quadric. The sequence

\[
0\longrightarrow\mathcal O_{\mathbf P^3}(d-2)
\longrightarrow I_C(d)
\longrightarrow\mathcal O_{\mathbf P^1\times\mathbf P^1}(d-1,d-3)
\longrightarrow0
\]

and Künneth give \(H^1(I_C(d))=0\) for \(d\ge2\). Consequently

\[
v_d:=\dim V_d=\binom{d+3}{3}-(4d+1)\qquad(d\ge2).
\]

For equal degrees the basis-free pair space is the open subset of

\[
\operatorname{Gr}(2,V_d)
\]

consisting of pencils without a common surface component. Its dimension is

\[
2(v_d-2)=2\binom{d+3}{3}-8d-6.
\]

For mixed degrees one may use the open set of proper ordered pairs in

\[
\mathbf P(V_a)\times\mathbf P(V_b),
\]

remembering that when \(a<b\), replacing \(G_b\) by \(G_b+H_{b-a}F_a\)
preserves the intersection. We do not interpret this redundant product as
the moduli space of distinct schemes.

**General-pair deduction.** For every \(a,b\ge4\), a general proper pair gives

\[
Y=C\cup D
\]

as a reduced scheme union, where \(D\) is smooth and geometrically integral,
with

\[
\boxed{\deg D=ab-4,\quad
g(D)=\frac{(a+b-4)(ab-8)}2,\quad
\operatorname{length}(C\cap D)=4(a+b)-14.}\tag{1}
\]

The attachments are distinct transverse points for a general pair.
This extends the general quartic picture using the same standard geometry;
it makes no assertion about all special pairs or fixed-boundary fibers.

Here are the hypotheses and proof. On the smooth blowup

\[
B=\operatorname{Bl}_C\mathbf P^3,
\quad H=\pi^*\mathcal O_{\mathbf P^3}(1),
\quad E=\pi^{-1}(C),
\]

the graph embedding from \(I_C(3)\), already checked in the cited note, makes

\[
L_d=dH-E=(4H-E)+(d-4)H
\]

very ample for \(d\ge4\): tensor a very ample line bundle with a globally
generated one, or use the same graph embedding with the Segre-Veronese
polarization \(\mathcal O(d-3,1)\). General divisors in \(L_a,L_b\) therefore
intersect in a smooth geometrically integral curve upstairs. This is the
usual [Bertini smoothness theorem](https://stacks.math.columbia.edu/tag/0FD4)
and [Bertini irreducibility theorem](https://stacks.math.columbia.edu/tag/0G4C).
The [Rees construction](https://stacks.math.columbia.edu/tag/01OF) identifies
these sections with actual global forms containing \(C\).

Section 3 proves that general first-normal determinant zeros are simple.
At any such zero, the first-normal matrix has rank one. Choose a generator
which is smooth there and make its local equation a coordinate \(x=0\).
The other equation on this smooth surface is \(y h(u,y)=0\), with

\[
C=(x,y),\qquad h(u,0)\text{ having a simple zero at }u=0.
\]

The residual \(h=0\) is smooth and meets \(y=0\) transversely. This proves the
needed blowdown assertion, including smoothness at the attachments; smoothness
upstairs alone would not justify it.

The numbers in (1) may be reconstructed on a general smooth degree-\(a\)
surface \(S\supset C\). Such an \(S\) exists: \(I_C(a)\) generates the
conormal fibers, so a general section has no normal zero along the
one-dimensional base \(C\), and Bertini applies away from \(C\). Adjunction gives

\[
K_S=(a-4)H,\quad C^2=14-4a,\quad D\sim bH-C.
\]

Thus \(H\cdot D=ab-4\), \(C\cdot D=4(a+b)-14\), and

\[
2g(D)-2=(bH-C)\cdot((a+b-4)H-C)
=(a+b-4)(ab-8)-2.
\]

These are classical adjunction/liaison calculations; they are not new
restrictions on STCI pairs with singular carriers or higher multiplicity.

| Bidegree | General residual degree | General residual genus | Simple attachments |
|---|---:|---:|---:|
| \((4,5)\) | 16 | 30 | 22 |
| \((5,5)\) | 21 | 51 | 26 |
| \((5,6)\) | 26 | 77 | 30 |
| \((6,6)\) | 32 | 112 | 34 |

For example, a general pair of quintics through \(C\) gives a genus-51 curve
of degree 21 attached at 26 points. This is the baseline geometry from which
one may deliberately specialize the residual and increase thickness along
\(C\). Since 25 is not divisible by four, \((5,5)\) itself cannot be a
sole-support endpoint; it is a useful geometry laboratory. The first equal
degree beyond quartics with an arithmetically possible endpoint is \((6,6)\).

## 3. New deduction: attachment-map dominance for all \(a,b\ge4\)

For an actual pair let \(f,g\) be its first-normal sections. Their determinant
is a section of

\[
\det N^*_{C/\mathbf P^3}\otimes\mathcal O_C(a+b)
\simeq\mathcal O_{\mathbf P^1}(N),
\qquad N=4(a+b)-14.
\]

On the open set where the pair is proper and this determinant is nonzero,
there is a morphism

\[
\beta_{a,b}:(F_a,G_b)\longmapsto[\det(f,g)]
\in\mathbf P H^0(\mathbf P^1,\mathcal O(N)).\tag{2}
\]

For \(a=b\), it descends to the Grassmannian of pencils. Its zeros give
the scheme \(C\cap D\), where \(D\) is the curve linked to the reduced \(C\).
This remains true when \(D\) is nonreduced. Locally write

\[
F=A x+B y,\qquad G=C_1x+D_1y.
\]

The elementary codimension-two linkage calculation gives

\[
((F,G):(x,y))=(F,G,AD_1-BC_1).
\]

After restriction to \(C\), the intersection ideal is therefore the first-normal
determinant. When the determinant is nonzero, \(D\) does not contain \(C\)
as a component and this is a finite effective divisor. The determinant-zero
locus requires higher-order data; it is outside the domain of (2).

**Proposition.** For every \(a,b\ge4\), \(\beta_{a,b}\) is
dominant and has surjective differential at the following explicit proper
pair:

\[
F_a=x_0^{a-4}F_4,\qquad G_b=x_3^{b-4}G_4.\tag{3}
\]

In particular a **general** divisor of degree \(N\) on the fixed marked
\(C\) is the attachment divisor of an actual proper \((a,b)\) pair. On a
dense open set of divisors it can also be realized with the smooth integral
residual of Section 2. This is a generic existence statement, not a claim
that every special effective divisor is realized by a smooth residual.

**Proof.** On \(x_0=1\), put

\[
u=x_1,\quad X=x_3-u^4,\quad Y=x_2-u^3.
\]

The first symbols at (3) are

\[
f=(-1,0),\qquad
g=(-3u^{4b-8},4u^{4b-7}).
\]

For actual global perturbations \(h\in V_a,k\in V_b\), with symbols
\((A_h,B_h),(A_k,B_k)\), the affine determinant differential is

\[
\delta\det
=u^{4b-16}(4u^9A_h+3u^8B_h)-B_k.\tag{4}
\]

The inherited, independently audited quartic calculation supplies

\[
\{4u^9A_h+3u^8B_h:h\in V_4\}
=\langle u^8,\ldots,u^{18}\rangle,
\quad
\{B_k:k\in V_4\}=\langle1,u,\ldots,u^{10}\rangle.\tag{5}
\]

For any ambient monomial \(M\) of degree \(r\), multiplication by \(M\)
multiplies a first-normal symbol of a form vanishing on \(C\) by \(M|_C\).
Here \(M|_C=u^w\), with \(w\) a sum of \(r\) elements of \(\{0,1,3,4\}\).
For \(r=1\), the possible shifts are \(0,1,3,4\), whose translates of an
interval of length eleven overlap to fill an interval four longer. Iterating
this observation for each extra degree shows that the products of quartic
perturbations with degree-\(r\) monomials span every exponent from the old
minimum to the old maximum plus \(4r\). These are actual homogeneous
perturbations over \(k\); there is no substitution of arbitrary \(k(C)\)
coefficients.

Applying this to (5), the \(h\)-part of (4) contains

\[
\langle u^{4b-8},\ldots,u^N\rangle,
\]

and the \(k\)-part contains

\[
\langle1,u,\ldots,u^{4b-6}\rangle.
\]

Their intervals overlap and cover \(0,\ldots,N\), proving surjectivity.
The base determinant is \(-4u^{4b-7}\), or homogeneously

\[
-4s^{4a-7}t^{4b-7}.
\]

It is nonzero. The pair (3) is proper: the accepted proper quartic pair
has no common factor, and the additional factors \(x_0,x_3\) do not divide
the opposite quartic. Thus it is a point of the stated domain. Affine
surjectivity gives projective surjectivity; when \(a=b\), the infinitesimal
change-of-basis directions affect the determinant by a scalar, so quotienting
by them preserves projective surjectivity. Source and target are smooth at
this point, and the differential criterion proves local smoothness and
dominance. The smooth-integral-residual open set in the irreducible source
has dense image under a dominant map; constructibility gives the asserted
dense open set of target divisors. □

The point (3) usually has nonreduced residual components on coordinate planes.
That causes no defect in the argument: it is only a regular point of the
**parameter space and attachment map** used to prove dominance. It is not
asserted to be a smooth residual example.

For equal degrees, the generic attachment fiber has dimension

\[
2(v_d-2)-(8d-14)
=\boxed{2\binom{d+3}{3}-16d+8}.\tag{6}
\]

Thus the numbers are 40 for quintic pencils and 80 for sextic pencils.
The attachment divisor leaves a great deal of actual global equation freedom.
Equation (6) is not a count of distinct residual isomorphism types, nor proof
that all analytic residual behavior is available in one fiber.

## 4. The residual also remembers a global cohomological defect

The same quadric sequence above, now for all integral twists, gives

\[
H^1(I_C(n))=
\begin{cases}k,&n=1,\\0,&n\ne1.\end{cases}\tag{7}
\]

Indeed the only nonzero Künneth term in
\(H^1(\mathcal O_Q(n-1,n-3))\) occurs at \(n=1\), namely
\(H^0(\mathcal O_{\mathbf P^1})\otimes H^1(\mathcal O_{\mathbf P^1}(-2))\).
Thus the fixed curve's Rao module is a copy of \(k\) in degree one, annihilated
by the positive-degree coordinate ideal. This is standard for this curve,
and even the official [Macaulay2 SpaceCurves documentation](https://www.macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/SpaceCurves/html/_rao__Module.html)
uses the monomial curve \(\{1,3,4\}\) as its example; this is explicitly not
claimed as a new discovery.

Classical complete-intersection linkage yields

\[
H^1(I_D(n))\simeq H^1(I_C(a+b-4-n))^*,
\]

so

\[
\boxed{H^1(I_D(n))=
\begin{cases}k,&n=a+b-5,\\0,&n\ne a+b-5.\end{cases}}\tag{8}
\]

For clarity, the degree shift can be reconstructed without trusting a shift
convention. The linkage sequence is

\[
0\to I_Y(n)\to I_D(n)\to\omega_C(n+4-a-b)\to0.
\]

The complete intersection \(Y\) is ACM. Duality on \(C\) and on \(Y\) turns
the kernel defining \(H^1(I_D(n))\) into the dual of the cokernel of

\[
H^0(\mathcal O_Y(a+b-4-n))\to
H^0(\mathcal O_C(a+b-4-n)).
\]

Since all sections on \(Y\) lift from projective space, this cokernel is
\(H^1(I_C(a+b-4-n))\). This proves the displayed formula and (8).
The linked \(D\) is locally Cohen–Macaulay; smoothness and reducedness are not
required for linkage duality. On the determinant-nonzero locus it is the
geometric residual with no \(C\)-component. On the determinant-zero locus,
the colon residual can itself retain \(C\), so it must not be identified with
the residual cycle away from \(C\).

The classical framework is recorded in Hartshorne's primary exposition
[*Experiments with Gorenstein Liaison*, Section 1, Theorem 1.1](https://arxiv.org/html/math/0106250v1):
for curves in projective three-space, Rao modules govern even liaison classes.
No assertion here that a numerical genus/degree and module alone determine
a curve, an embedding, or an actual pair of equations.

There is a useful connection to a very small cohomological model: the module
in (8) is annihilated by the positive-degree coordinate ideal, so these
residuals are diameter-one arithmetically Buchsbaum curves. Since the dual of
the one-dimensional module is again a one-dimensional module up to shift,
Rao's theorem puts all of them in the same even liaison class as the fixed
quartic, after the appropriate degree shift. This is a standard liaison
interpretation, not a classification of their singularities or attachment
maps. It suggests constructing residuals via basic double links and
Rao-preserving deformations, then testing the additional requirement that
the particular fixed embedded C be their direct partner.

This supplies a global companion to the formal neighborhood: a proposed
degree-\(ab-4\) residual cannot be arbitrary even when its attachments are
flexible. For a quintic link its one-dimensional deficiency lies in degree
five; for a sextic link it lies in degree seven. These are useful exact
filters in constructive searches.



## All-order sheaf powers and every prescribed attachment divisor

## 2. An all-order sheaf-power calculation

For every \(r\ge1\) there is an exact sequence

\[
0\longrightarrow I^{r-1}(d-2)
 \xrightarrow{\ q\ } I^r(d)
 \longrightarrow \mathcal O_Q(d-r,d-3r)\longrightarrow0. \tag{1}
\]

This is an assertion about sheaf powers, not about an unsaturated ordinary
homogeneous ideal power. Locally \(I=(q,f)\) is a regular sequence. Reducing
\(I^r\) modulo \(q\) gives \((f^r)\), with kernel
\((q)\cap I^r=qI^{r-1}\). On \(Q\), the ideal of \(rC\) is
\(\mathcal O_Q(-r,-3r)\), which proves (1).

Induction on \(r\), with Künneth on \(Q\), gives

\[
\boxed{H^1(\mathbf P^3,I^r(d))=0\quad(d\ge3r-1).} \tag{2}
\]

Indeed the left term of (1) has vanishing \(H^1\) by induction and the
right term has both bidegrees at least \(-1\). The base \(r=0\) uses
\(H^1(\mathbf P^3,\mathcal O(d))=0\). The same induction gives
\(H^2(I^r(d))=0\) for \(d\ge2r-2\): the first bidegree of the
right term is then at least \(-1\), so its \(H^2\) vanishes.

The \(H^1\) threshold is sharp. For \(d=3r-2\), the right term of (1)
is \(\mathcal O_Q(2r-2,-2)\); the adjacent \(H^1,H^2\) of the left
term vanish by the preceding bounds. Thus

\[
h^1(I^r(3r-2))=2r-1. \tag{3}
\]

Consequently every compatible section on the finite neighborhood
\(V(I^N)\) in twist \(d\ge3N-1\) lifts to an actual homogeneous form.
In particular the map

\[
H^0(I^r(d))\longrightarrow H^0(\operatorname{Sym}^r E(d))
\quad\text{is onto for }d\ge3r+2. \tag{4}
\]

For characteristic zero its target is
\(H^0(\mathcal O_{\mathbf P^1}(4d-7r))^{r+1}\).
At \(d=3r+1\) the cokernel has dimension \(2r+1\), by (3) applied to
\(r+1\) and \(H^1(I^r(d))=0\). In particular **every first-normal
section is the symbol of an actual degree-\(d\) equation for \(d\ge5\)**.
At degree four the cokernel has dimension three, agreeing with the inherited
quartic calculation without rerunning that certificate.

This is a concrete application of standard ideal-power cohomology.
[Shang, Theorem 1.1 and Theorem A](https://arxiv.org/html/2205.06289v1)
recalls Bertram–Ein–Lazarsfeld's general vanishing and studies its regularity
boundary. Our proof uses the specific smooth quadric to get (2) directly,
over any field. No literature novelty is asserted. Separate graded layers
chosen arbitrarily need not form a compatible finite-neighborhood section;
the full-jet assertion only concerns sections that already glue on that
neighborhood. Its bound grows with \(N\), so it supplies no fixed-twist
all-order lift or supported complete intersection.

## 3. Every attachment divisor can be constructed

**Proposition (sufficient range, not claimed sharp).** Let \(a,b\ge7\)
and let \(A\) be **any** effective divisor of degree
\(N=4(a+b)-14\) on the fixed marked \(C\), including nonreduced divisors.
There are actual degree-\(a,b\) homogeneous forms \(F,G\) such that:

1. \(S=V(F)\) and \(V(G)\) are smooth integral surfaces;
2. \(Y=V(F,G)=C\cup D\) scheme-theoretically, with \(D\) smooth and
   geometrically integral and with no common surface factor;
3. \(C\cap D=A\) as a scheme on \(C\), and the generic multiplicity
   along \(C\) is exactly one;
4. \(\deg D=ab-4\) and
   \(g(D)=(a+b-4)(ab-8)/2\).

The range seven is a convenient uniform bound ensuring first-jet separation
off \(C\) for the fixed-symbol variations. It is not a preferred degree
or a proposed reduction of arbitrary intersections.

**Proof.** Exchange \(a,b\) if needed to make \(a\le b\), and put
\(e=4a-7\), \(f=4b-7\). Choose a basepoint-free pair of binary forms
\(u=(u_1,u_2)\) of degree \(e\), for example \((s^e,t^e)\).
For a binary equation \(\delta\) of \(A\), the exact sequence

\[
0\to\mathcal O(f-e)\xrightarrow{u}
\mathcal O(f)^2\xrightarrow{v\mapsto\det(u,v)}
\mathcal O(e+f)\to0 \tag{5}
\]

shows that there is a pair \(v\) of degree \(f\) with
\(\det(u,v)=\delta\), since \(f-e\ge0\).
We can also choose \(v\) basepoint-free. It can vanish only at a point
of \(A\); adding \(h u\) for \(h\in H^0(\mathcal O(f-e))\)
avoids vanishing at every point of the finite support, because that line
bundle is globally generated and the field is infinite. This is a finite
union of proper affine hyperplanes to avoid, not an assertion about a
general divisor \(A\).

By (4), choose actual equations with first symbols \(u,v\). For a fixed
symbol, all lifts form an affine space under \(H^0(I^2(d))\). The sheaf
\(I^2(6)\) is globally generated, because it is a quotient of the square
of the globally generated \(I(3)\). Multiplication by linear forms makes
\(H^0(I^2(d))\) separate first jets on \(\mathbf P^3\setminus C\)
for every \(d\ge7\): at a point off \(C\), take a degree-six section
nonzero there and multiply it by ambient forms of degree \(d-6\).
[Bertini smoothness](https://stacks.math.columbia.edu/tag/0FD4) therefore
makes a general lift of \(u\) smooth off \(C\); its nowhere-zero first
symbol makes it smooth along \(C\). Such a projective hypersurface is
connected, hence smooth integral. Fix such an \(S\).

On \(S\), divide \(G|_S\) by the Cartier equation of \(C\). The
remaining section \(h\) defines an effective divisor
\(D\sim bH-C\) and restricts to \(\delta\) on \(C\), up to the
natural invertible factors. Thus \(D\) has no \(C\)-component and
\(D\cap C=A\). The local ideal is \((x,yh)\), with
\(S=(x)\), \(C=(x,y)\); since \(h\notin(y)\),
\((x,yh)=(x,y)\cap(x,h)\). This proves the scheme union and properness.

General fixed-symbol variations of \(G\) make \(D\) smooth away from
\(C\) by the same first-jet argument. At a simple zero of \(\delta\),
\(\partial h/\partial t\ne0\), so \(D\) is already smooth. At a
multiple zero \(p\), it suffices to make
\(\partial h/\partial y(p)\ne0\). Varying by \(I^2(b)\) changes
this value nontrivially: its stalk surjects onto the square of the ideal of
\(C\) on \(S\), and global generation of \(I^2(b)\) realizes a
nonzero value in its one-dimensional fiber. Avoid the corresponding
finitely many hyperplanes. Also choose the lift of \(v\) generally so
\(V(G)\) is smooth; \(v\) is nowhere zero on \(C\). All these are
nonempty open conditions on the same irreducible affine space of lifts.

Finally \(3H-C\) is globally generated on \(S\), as a quotient of
\(I(3)\). Hence \(bH-C\) is ample for \(b\ge4\). A smooth ample
effective divisor on a smooth projective surface is connected (for example
by the Hodge index theorem: two disjoint nonempty parts would both have
positive square and intersection zero). It is therefore integral. Adjunction
gives the stated degree and genus, as in the earlier general-pair note. □

## 4. A useful falsification control: all contact at one point

Set \(a=b=d\ge7\), \(e=4d-7\), and choose

\[
u=(s^e,t^e),\qquad v=(s^e,t^e+s^e).
\]

Both pairs are basepoint-free and \(\det(u,v)=s^{2e}\). The proposition
constructs smooth \(D\) with **all** \(8d-14\) attachments concentrated
at the single point \(s=0\), while the generic thickness is still one.
For \(d=7\), the residual has degree 45 and genus 205, and meets \(C\)
in the length-42 scheme at that point. The full CI has arithmetic genus
246, agreeing with \(0+205+42-1\).

This is an existence construction with prescribed actual equation symbols;
no full coefficient list or computed rational smooth pair is asserted.
It shows that extreme attachment concentration can coexist with a smooth
integral residual of the full residual degree. The distinction between
contact concentration and absorption is not merely a generic observation.




## The remaining global presentations

[Reverse linkage](residual_liaison.md) recovers low-degree equations and controls its precise deformation space, including once-link flatness through multiplicity jumps. [The two-blowup model](blowup_residual_geometry.md) transports actual sections to conic-vanishing sections on V5 while retaining both projections and the anticanonical image of E. [Full formal visibility](formal_residual_visibility.md) gives the exact fixed-twist algebraization criterion and distinguishes finite jets from all-order sections. Each full statement and proof has one home.

## Mechanisms, literature, and open construction boundary

These results identify three different global presentations. The normal-symbol
map describes actual homogeneous equation freedom; reverse linkage remembers
the low equations from an embedded residual; the \(V_5\) dictionary transports
those actual sections through a common graph. A compatible finite jet, a Rao
module, and a curve lying on the anticanonical image \(\Sigma\) provide
necessary pieces of data, each with a different missing implication.

The prescribed attachment construction proves that even all attachment at one
point can coexist with a smooth integral residual. It does not increase generic
thickness. The relative once-link is flat through multiplicity jumps while the
full-primary extraction may fail to be flat. The graph criterion says complete
absorption requires its actual strict-transform intersection to lie in \(E\),
not merely to have image in \(\Sigma\). The formal criterion removes an
algebraization gap only **after** two fixed-twist sections glue to all orders
and satisfy uniform power containment.

Fresh primary-source checks in this consolidation verified
[Cheltsov–Przyjalkowski–Shramov, Lemma 6.13](https://arxiv.org/html/1809.09223v1#S6.L13)
for the two blowups, [Kleppe, Theorem 1.3 and Proposition 1.4](https://www.numdam.org/article/AIF_2006__56_5_1297_0.pdf)
for the diameter-one unobstructedness and fixed-postulation calculation, and
[Hartshorne, §1, Propositions 1.1–1.2](https://www.numdam.org/article/CM_1971__23_3_257_0.pdf)
for projective-space G3/Lefschetz extension. The cited results supply their
stated general mechanisms; the applications and scope checks are proved above.
No novelty follows from their absence in earlier repository notes.

Essential inherited finite evidence is the original quartic symbol-image
calculation and the cubic \(V_5\) model certificate. The later normal-jet and
all-degree attachment checks corroborate the proofs, but finite samples are
not their universal justification. The exploratory sextic calculation stopped
after properness, degree 32 and genus 112; it supplies no computed smooth
sextic benchmark. No inherited computation was rerun here.


## Characteristic reach and limitation

The ideal-sheaf-power exact sequence, its vanishing thresholds and the
compatible-jet lifting result are characteristic-free. Smooth-integral
residual and prescribed-boundary constructions above are asserted in
characteristic zero, with their stated Bertini and balanced-conormal inputs.
The all-degree attachment differential includes a factor four and does not
prove dominance in characteristic two. Away from two the same explicit
linear spanning calculation is valid, but its separate geometric hypotheses
must still be checked before transferring the full construction. None of
these multiplicity-one results excludes the [positive-characteristic
quartic-carrier STCI](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier),
whose generic multiplicity is higher.
