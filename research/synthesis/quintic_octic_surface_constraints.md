# Quintic–octic surface constraints and the even-node obstruction

Fix an algebraically closed field of characteristic zero and the embedded curve
\[
C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3.
\]
For a proper complete intersection \(Y=V(F_5,G_8)\) with sole reduced support C, the quintic **cannot have only rational double points everywhere**. This includes possible singularities away from C. The theorem assumes neither reducedness of the full quintic first-symbol divisor nor reducedness of the common first-symbol divisor, and imposes no singularity hypothesis on the octic. Its full proof is in [the quasi-étale cover and symbolic-triple account](quintic_octic_ade_cover_and_triple.md).

This chapter retains the fixed-singularity geometry, actual local and residual controls, and the earlier independent proof under the additional hypothesis that the full quintic first-symbol divisor is reduced. In that proof, local normal defects give eight budgets; the quintic rank bound leaves \(4A_1+9A_4\), and the actual octic divisor relation makes the four nodes an even set in the integral Picard group. A branched double cover and Noether’s inequality exclude that configuration. Rank alone does not finish that argument. The stronger proof uses a quasi-étale cover, its canonical map, and the location of the symbolic triple’s quadratic defect.

Both are independently reviewed mathematics, and separate preservation review has accepted the stronger proof’s integration. Neither proves a full degree-\((5,8)\) exclusion or resolves unrestricted characteristic-zero STCI. A quintic with a non-ADE singularity remains outside the combined theorem.

As in the [quartic-pair chapter](quartic_pair_obstruction.md), write \(\mathcal O(j)\) for degree \(j\) on \(C\simeq\mathbf P^1\), so ambient \(\mathcal O_C(a)=\mathcal O(4a)\).

The combined degree-five boundary uses two distinct theorems:

| Quintic carrier | Current conclusion for a proper sole-supported (5,8) pair |
| --- | --- |
| Normal, globally ADE | Excluded by the cover and symbolic-triple proof here |
| Normal, with a non-ADE singularity | Open under these results, including when that singularity lies away from C |
| Nonnormal, Gorenstein normalization | Excluded for every mate degree by the [full conductor theorem](quintic_gorenstein_normalizations.md) |
| Nonnormal, non-Gorenstein normalization | Open in general; [toric center geometry](quintic_toric_center_incidence.md) gives a bounded actual-source test |

The Gorenstein hypothesis concerns the normalization, not merely the
hypersurface. An ADE normalization does not turn a nonnormal carrier into
an instance of the normal-carrier theorem.

## 1. Filtration data and the three numerical rows

The inputs are [R-0001](../results/quartic_carrier_exclusion.md) and its factor/lower-degree reduction, [R-0020](../results/quartic_conormal_characteristic_jump.md), and the ordinary curvilinear-layer and socle identities of [R-0034](../results/normal_carrier_index_socle.md). The [ordinary-layer/lattice proof](../supplements/CURVILINEAR_GENUS_AND_DEFECTS.md#normal-torsion-spectral-genus-budget) identifies torsion-free ordinary layers with powers of the first quotient and proves the pointwise socle/torsion relation. This is ordinary normal-layer torsion, not the filtered-equation comparison invariant of R-0030.

Bézout gives transverse length \(m=40/4=10\), and complete-intersection adjunction gives \(\omega_Y=\mathcal O_Y(9)\), \(p_a(Y)=181\). The quintic is integral by the accepted factor reduction and has a nonzero first normal symbol by §2, so it is smooth at the generic point of C. Its equation supplies one ambient normal parameter there; the generic length-ten transverse algebra is therefore curvilinear. Thus no additional generic-curvilinearity hypothesis is needed for the actual supported pair. The following identities still concern that specific generic algebra, rather than arbitrary length-ten plane algebras. Write \(K=I_C\mathcal O_Y\),
\(T_i=\operatorname{tors}(K^i/K^{i+1})\), and
\(L=(K/K^2)/T_1=\mathcal O(-q)\). Since \(E=N_C^*=\mathcal O(-7)^2\) surjects onto \(L\), one has \(q\le7\). The torsion-free ordinary layers are \(L^i\), \(0\le i\le9\). Euler-characteristic additivity gives \(-180=10-45q+\tau\), while the top saturated socle is \(\omega_C\otimes(\omega_Y|_C)^{-1}=\mathcal O(-38)\). Its inclusion of \(L^9=\mathcal O(-9q)\) defines the effective socle divisor. Together with pointwise Gorenstein duality these give

\[
\tau=\sum_i\operatorname{length}T_i=45q-190,
\qquad \deg D_{\rm soc}=9q-38,
\qquad \tau_p=5(D_{\rm soc})_p.                 \tag{1}
\]

Effectivity gives \(q\ge5\), so the three necessary rows are

| q | total ordinary torsion | socle-defect degree |
|---|---:|---:|
| 5 | 35 | 7 |
| 6 | 80 | 16 |
| 7 | 125 | 25 |

The first quotient, genus and socle identities are necessary data. They do not construct an embedded multiple curve or actual quintic/octic equations.

## 2. Fixed defects and moving octic singularities

Both F and every \(S_H=G+FH\), \(H\in H^0(\mathcal O_{\mathbf P^3}(3))\),
are integral: the factor reduction above would require each factor to have
degree at least five, impossible for two factors of either degree five or
eight. Also \((F,S_H)=(F,G)\), so the whole scheme, not just its cycle, is fixed.

The actual octic system also has a symmetry restriction, independent of
its ADE status. For the fixed weights \((0,1,3,4)\), neither F nor any
member \(G+FH\) can be weight-homogeneous. The
[equivariant theorem](../supplements/EQUIVARIANT_DEGREE_BOUNDS.md)
excludes a characteristic-zero supported pair whenever one equation is
weight-homogeneous, with arbitrary mate. Here \((F,G+FH)=(F,G)\), while
properness prevents a zero member, so that theorem applies to every member
of this system. This reviewed consequence also constrains the non-ADE
boundary; it does not reduce arbitrary pairs to invariant ones.

The quintic has a nonzero first normal symbol. Indeed let
\(Q=x_0x_3-x_1x_2\). If a quintic vanishes to normal order at least two
along C, its restriction to the smooth quadric Q contains \(2C\). Taking
\(C\) of type \((1,3)\), the residual class \((5,5)-2(1,3)=(3,-1)\)
is not effective. Thus Q divides the quintic; smoothness of Q along C then
implies that the quotient cubic contains C. This proves

\[
H^0(\mathcal I_C^2(5))=Q\,H^0(\mathcal I_C(3)).       \tag{2}
\]

Such a quintic is not integral. This argument concerns sheaf powers; no
unsaturated homogeneous-power identification is assumed.

Let \(M=\ker(E\twoheadrightarrow L)=\mathcal O(q-14)\). In its saturated
direction the first symbols of the equations are scalar sections

\[
a\in H^0(\mathcal O(q+6)),\qquad
b\in H^0(\mathcal O(q+18)),\qquad a\ne0.
\]

Put \(B=\gcd(a,b)\), \(\beta=\deg B\), with
\(\gcd(a,0)=\operatorname{div}(a)\). Saturation makes the local direction
nonzero in every fiber, so the scheme of simultaneous singularities
restricted to C is exactly B. The first ordinary torsion is
\(T_1=M/M(-B)\), of length \(\beta\).

In fact

\[
\operatorname{Supp}\Bigl(\bigoplus_i T_i\Bigr)=\operatorname{Supp} B,
\qquad 1\le\beta\le q+6.                            \tag{3}
\]

At a point outside B one carrier is smooth. On that surface the smooth
curve C is Cartier, and sole support forces the mate locally to be a unit
times its tenth power. The ideal is therefore \((x,y^{10})\), so all
ordinary layers are free. Conversely every point of B has nonzero T1.
Equation (1) makes B nonempty. This is a statement about ordinary-layer
torsion; it does not identify that torsion with the different filtered-equation
comparison invariant \(\Delta\) in [R-0030](../results/local_filtration_comparison_defect.md).

The first symbol of \(S_H\) is \(b+ha\), where
\(h=H|_C\in H^0(\mathcal O(12))\). Cubic restrictions fill this whole
space: sums of three exponents from \(\{0,1,3,4\}\) contain every integer
from zero to twelve. After removing B, the linear system spanned by
\(b/B\) and \((a/B)H^0(\mathcal O(12))\) is basepoint free.
A general member has simple zeros, avoids B, and also avoids the zeros
of a outside B. Generic simplicity follows either from curve Bertini in
characteristic zero or directly from value and first-jet separation wherever
\(a/B\ne0\). The affine family with coefficient of b equal to one meets
this open set; the case b=0 is the complete degree-twelve system times a.

Consequently a general octic has on C the fixed divisor B and

\[
N=q+18-\beta\ \ge12                              \tag{4}
\]

distinct moving singular points. All these moving singularities have marked pair type \(A_9^1\): the resolved curve meets the first end of the exceptional chain. This is the general local mechanism \((x,y^m)\) with a simple moving first-symbol zero producing \(xt+y^m\). It is the same coordinate-change argument as [the quartic-pair local calculation](quartic_pair_obstruction.md#3-from-the-marked-neighborhood-to-surface-equations), now with \(m=10\), not an application of its degree-four exclusion. Indeed, at such a point straighten the smooth quintic to
x; the pair is \((x,y^{10})\), and
\(S_H=xA+y^{10}U\) with \(U\) a unit and \(A|_C\) having a simple zero.
Use A as the curve coordinate and absorb a tenth root of U into y. This
gives \(xt+y^{10}\), preserving C as \((x,y)\).

The degree-eight system is generated by G and the cubic multiples of F,
and has base support exactly C. Bertini makes its general member smooth
off C. Its first-symbol zero set on C is finite, so the general integral
octic has only isolated singularities and is normal. **Rational double
singularities at B do not follow from this argument.**

## 3. Reduced common divisor: exact local models and eight budgets

Assume in this section that B is reduced. At each of its points the general
octic's first normal symbol vanishes to order exactly one. In coordinates
\((t,x,y)\), with \(I_C=(x,y)\), its Hessian therefore contains a nonzero
\(tx\) term. Its quadratic rank is at least two. The formal splitting
lemma and isolation just proved make it an \(A_{r-1}\) singularity.
The split one-variable term cannot vanish identically, since that would
give a curve of singularities.

The surface–curve pair is \(A_{r-1}^1\): in the standard classification of
smooth curves on an A singularity the first-symbol order equals the smaller
end-distance k, and here it is one. See Ellia, Definition 8 and Lemma 10,
[arXiv:1409.3801](https://arxiv.org/html/1409.3801). Equivalently the pair has
formal coordinates

\[
S_H:tu-w^r=0,\qquad C:(u,w)=0.                    \tag{5}
\]

In this normal local surface C has Cartier index r and \(\operatorname{div}(u)=rC\).
Since the actual mate cuts \(10C\), \(r\mid10\), and, up to a unit and
adding a multiple of S_H, its equation is \(u^k\), \(k=10/r\).
The complete intersection at this point is exactly

\[
\mathcal B=k[[t,u,w]]/(tu-w^r,u^k),\qquad rk=10.    \tag{6}
\]

This normal form supplies the higher layers, not just a first-order count.
It is free over \(D=k[[t]]\) on \(u^i w^j\),
\(0\le i<k,\ 0\le j<r\). Its generic curvilinear generator is w, and
\(w^{ri+j}=t^i u^i w^j\). Hence the index of the monomial lattice D[w]
in \(\mathcal B\), equal to the total ordinary-layer torsion by the
inherited lattice proof, is

\[
\tau_p=r\sum_{i=0}^{k-1}i=5(k-1).
\]

The socle generator is \(u^{k-1}w^{r-1}\), while
\(w^9=t^{k-1}u^{k-1}w^{r-1}\); thus \((D_{\rm soc})_p=k-1\).
The case r=10 makes the other carrier smooth and has no defect, so it
cannot occur on B. The case r=1 is smooth. The only fixed types are

| general octic pair | r | local mate | first torsion | total ordinary torsion | socle defect |
|---|---:|---|---:|---:|---:|
| \(A_1^1\) | 2 | \(u^5\) | 1 | 20 | 4 |
| \(A_4^1\) | 5 | \(u^2\) | 1 | 5 | 1 |

Let u now count the fixed A1 points and v the fixed A4 points (these counts
are unrelated to the local coordinate in (5)). Then

\[
4u+v=9q-38,\qquad \beta=u+v\le q+6.                \tag{7}
\]

The inequalities give
\[
\max\!\left(0,\left\lceil\frac{8q-44}{3}\right\rceil\right)
\le u\le\left\lfloor\frac{9q-38}{4}\right\rfloor,
\qquad v=9q-38-4u.
\]
Thus the following eight rows exhaust the nonnegative integer possibilities without a search cutoff. The last two columns will compare the quintic rank bound and the general octic's weighted ADE inequality. These are necessary budgets, not realization data.

| q | fixed A1: u | fixed A4: v | beta | moving A9 on octic | quintic rank above C | octic ADE weight |
|---|---:|---:|---:|---:|---:|---:|
| 5 | 0 | 7 | 7 | 16 | 64 | 192 |
| 5 | 1 | 3 | 4 | 19 | 76 | 204 |
| 6 | 2 | 8 | 10 | 14 | 52 | 180 |
| 6 | 3 | 4 | 7 | 17 | 64 | 192 |
| 6 | 4 | 0 | 4 | 20 | 76 | 204 |
| 7 | 4 | 9 | 13 | 12 | 40 | 168 |
| 7 | 5 | 5 | 10 | 15 | 52 | 180 |
| 7 | 6 | 1 | 7 | 18 | 64 | 192 |

In particular, if every fixed singularity of the general octic is an
ordinary node, then \(q=6\) and there are exactly four fixed nodes.
This conclusion does not require first assuming B reduced: a smooth curve
through an ordinary node has first-symbol order one, so that assumption
then follows. Neither q=5 nor q=7 can be paid for by nodes alone.

## 4. The quintic rank bound and integral Picard relation

### 4.1 The rank bound leaves one configuration

Impose two additional conditions on the actual quintic:

1. Its first-symbol zero divisor \(\operatorname{div}(a)\) is reduced.
2. The quintic has only rational double points everywhere (smooth points
   allowed), including away from C.

These conditions are not consequences of the STCI hypothesis. They imply
B reduced. At a fixed point write \(F=\epsilon u^k+hS_H\) using (5)–(6),
where \(\epsilon\) is a unit and k is 5 or 2. Simplicity of a forces h to
be a unit. Dividing by h and replacing
\(t\) by \(t+(\epsilon/h)u^{k-1}\) proves that F has the same A1 or A4
pair type there. At every other zero of a the octic is smooth, and the
primitive local calculation from section 2 makes F an A9. Thus the rank
of its exceptional configurations above C is

\[
R_C=u+4v+9(q+6-u-v)=9q+54-8u-5v.                 \tag{8}
\]

For the Hodge calculation, descend the finite defining data to a finitely
generated characteristic-zero field and embed that field into the complex
numbers. For a quintic with only rational double points, the minimal resolution \(X\to S\) is crepant, so \(K_X\sim H\) and \(K_X^2=5\), where \(H\) is the pulled-back hyperplane class. Rationality of these singularities gives \(H^1(\mathcal O_X)=H^1(\mathcal O_S)=0\), while \(h^0(K_X)=h^0(\mathcal O_S(1))=4\). Thus \(\chi(\mathcal O_X)=5\). Noether's formula gives \(c_2=12\chi-K^2=55\), and Hodge decomposition gives \(b_2=53\) and \(h^{1,1}=53-2p_g=45\). These are the hypersurface formulas used also in Ellia's Proposition 14. The negative definite exceptional
root lattices, together with the positive-square pullback of a hyperplane,
are independent algebraic classes. Therefore

\[
R_C\le44.                                         \tag{9}
\]

The rank column in the table leaves exactly one row:

\[
\boxed{q=7,\quad 4A_1+9A_4\text{ on the quintic along C},
\quad\beta=13.}                                   \tag{10}
\]

Its general octic has those fixed types and twelve moving A9 points.
Additional quintic exceptional rank off C is at most four. This is the
only configuration left by the rank bound under the two extra conditions.
The actual integral divisor relation eliminates it as follows.

### 4.2 The actual divisor relation forces an even set

Let \(\pi:X\to S=V(F_5)\) be the minimal resolution, let H denote the
pulled-back hyperplane class, and write \(\widetilde C\) for the strict
transform of C. The actual octic cuts the Cartier divisor \(10C\), so
\(10C\sim8H\) on S. Label each A4 chain so that \(\widetilde C\) meets
its first end. The rational pullback of C has correction \(E/2\) at an
A1 point and
\((4E_1+3E_2+2E_3+E_4)/5\) at an A4 point. These coefficients follow
by imposing zero intersection with every exceptional curve. For example,
the latter coefficient vector has intersections \((-1,0,0,0)\) with
the A4 chain, canceling the intersections of \(\widetilde C\).

Let N be the sum of the four exceptional node curves and let A be the
sum of the integral weighted divisors
\(4E_1+3E_2+2E_3+E_4\) over the nine A4 points. Pulling back the actual
Cartier linear equivalence gives an equality in \(\operatorname{Pic}(X)\):

\[
10\widetilde C+5N+2A\sim8H.
\]

In particular, the integral divisor class

\[
D=4H-5\widetilde C-A-2N
\quad\text{satisfies}\quad 2D\sim N.               \tag{11}
\]

This explicit expression does not divide an equality in the numerical
lattice or assume that \(\operatorname{Pic}(X)\) is torsion free. The four
nodes form an even set in the Picard group. Exceptional curves over points
away from C have coefficient zero in the pullback of \(10C\); they do not
enter (11).

The obstruction now concerns this integral Picard relation, rather than the rank of the root lattice. The following general lemma completes the argument and separates its reusable surface mechanism.

### 4.3 An even-node budget from a branched double cover

**Lemma.** Let \(X\) be a smooth complex projective surface with \(K_X\) nef and big. Suppose a nonempty set of \(n\) disjoint smooth rational curves \(E_i\) with \(E_i^2=-2\) satisfies
\[
N=\sum E_i\sim2D\qquad\text{in }\operatorname{Pic}(X).
\]
Then
\[
n\equiv0\pmod4,\qquad
n\ge8\chi(\mathcal O_X)-4K_X^2-12.
\tag{12}
\]

Choose the section of \(\mathcal O_X(2D)\) with divisor \(N\). The algebra \(\mathcal O_X\oplus\mathcal O_X(-D)\), with multiplication given by this section, defines a double cover \(f:Z\to X\). It is smooth because the branch curves are smooth and disjoint, and integral: a rational trivialization of the branch section has odd valuation at each branch component and cannot be a square in \(k(X)\).

Adjunction gives \(K_XE_i=0\), hence \(D^2=-n/2\), \(K_XD=0\). Riemann--Roch applied to the direct-image algebra and the canonical double-cover formula give
\[
\chi(\mathcal O_Z)=2\chi(\mathcal O_X)-n/4,
\qquad K_Z^2=2K_X^2-n.
\tag{13}
\]
In particular \(4\mid n\). The ramification curves \(R_i\) map isomorphically to the \(E_i\); since \(f^*E_i=2R_i\), one has \(R_i^2=-1\). Contract these disjoint curves to a smooth surface \(\sigma:Z\to W\). Their sum \(R\sim f^*D\) by the tautological cover section, so
\[
\sigma^*K_W\sim K_Z-R\sim f^*K_X.
\tag{14}
\]
Thus \(K_W\) is nef and big, \(W\) is minimal of general type, and
\[
K_W^2=2K_X^2,\qquad
\chi(\mathcal O_W)=2\chi(\mathcal O_X)-n/4.
\]
Noether's inequality yields
\[
2K_X^2\ge2p_g(W)-4
\ge2\chi(\mathcal O_W)-6
=4\chi(\mathcal O_X)-n/2-6,
\]
which rearranges to (12).

The external ingredients are the double-cover construction and canonical formula in [Debarre, *Inégalités numériques pour les surfaces de type général*](https://www.numdam.org/item/10.24033/bsmf.1965.pdf), §1.4, printed p. 322, and classical Noether inequality on printed p. 320. The [1983 addendum](https://www.numdam.org/item/10.24033/bsmf.1990.pdf) repairs the stronger irregular-surface theorem 6.1; that theorem is not used. Formula (12) is the deduction here, not a theorem attributed to Debarre.

Apply the lemma to the globally ADE quintic resolution: \(K_X\sim H\) is nef and big, \(K_X^2=5\), \(\chi(\mathcal O_X)=5\). It forces \(n\ge8\), contradicting the four-node even set (11). Explicitly its cover would have \(\chi(\mathcal O_Z)=9\), \(K_Z^2=6\), and the contracted minimal surface would have \(\chi(\mathcal O_W)=9\), \(K_W^2=10\), while Noether requires at least twelve. Extra ADE exceptional curves away from \(C\) do not enter the branch or change these invariants. This also excludes an even set of exactly four exceptional node curves on any globally ADE quintic, independently of the specified quartic.

All characteristic-zero field qualifications can be handled by descending the finite hypothetical-pair data to a finitely generated field and embedding into \(\mathbf C\) before taking a resolution. If descending an already constructed cover, include its line bundle, section and isomorphism data. No embedding of the entire original algebraically closed field into \(\mathbf C\) is required.

**Conditional exclusion in the generic-curvilinear length-ten setting.** No hypothetical pair treated here can have both a reduced quintic first-symbol divisor and a quintic with only
rational double points everywhere. Equivalently, any such pair must have
a repeated zero in \(\operatorname{div}(a)\), or a quintic singularity
that is not a rational double point, possibly away from C. This does not
imply that the common divisor B is nonreduced. The cover argument also
shows, independently of C, that the resolution of a globally ADE quintic
cannot have an even set consisting of exactly four exceptional node curves.

## 5. Why primitive uniformity does not settle the fixed defects

Ellia's Theorem 12 assumes that the complete-intersection multiple curve is
primitive, meaning locally contained in a smooth surface. His proof uses
the existence, at each point of C, of a smooth member of the containing
system; its singularity incidence is then a graph over C.
[Source, Theorem 12 and proof](https://arxiv.org/html/1409.3801).

Here B is nonempty, and every local equation of Y lies in the square of
the ambient maximal ideal at each point of B: both generators are singular.
No local smooth surface can contain Y there. Every octic G+FH is singular
at those points. In a pencil, the incidence contains the fixed fibers
\(\{p\}\times\mathbf P^1\), in addition to its moving part. Thus the
primitive smooth-member premise and the graph argument fail exactly on B.
Normality of the general octic survives by section 2, but uniform ADE type
and a global ADE singularity bound cannot be imported across B.

Sections 3–4 recover a portion of that strategy by proving the necessary
local hypotheses separately, then using the actual Picard relation to
construct the forbidden cover. The torsion total itself is not a surface
singularity bound.

## 6. What the local models and octic inequality do not exclude

The two algebras (6) are actual supported complete intersections of length
ten in a formal smooth threefold. They realize total torsion 20 and 5 at
one reduced common-singularity point. In particular, each eight-row budget
can be paid arithmetically by local models of the correct multiplicity.
This supplies local flexibility and refutes \(\tau\le\operatorname{length}(B)\) as a general local-algebra inequality. It does not rule out bounds with an additional factor or further geometric hypotheses, including restrictions coming from actual global quintic–octic equations.

It does not glue those algebras on the fixed projective C, produce global
degree-five/eight equations, or establish the prescribed line quotient.
The inherited control \(4C\) on the smooth quadric already shows why a
normal algebra and the right genus need not give equations of the required
degrees; see [the actual quadric quadruple control](quartic_pair_obstruction.md#7-controls-and-geometric-limits).

Even in the reduced-B case, the usual octic A-singularity inequality does
not discard a row. The surface inequality used in [Ellia, Proposition 14](https://arxiv.org/html/1409.3801), assigns an \(A_n\) point weight \((n+1)-1/(n+1)\). Here its weighted sum is
\[
\tfrac32u+\tfrac{24}{5}v+\tfrac{99}{10}(q+18-u-v),
\]
whose values in the table are all below
\(2\cdot8\cdot7^2/3=784/3\). This is a direct check of a valid bound under
the ADE conclusions of section 3, not evidence that the rows are realizable.

## 7. A proper homogeneous residual-support control

There is also a simple proper pair of exactly the requested degrees that
shows why arbitrary fixed points cannot automatically be assigned ADE types.
It is deliberately a **residual-support control**, not an STCI candidate.
Put

\[
A=x_0^2x_2-x_1^3,\quad Q=x_0x_3-x_1x_2,\qquad
F=x_1^2 A+x_3 Q^2,\quad G=A^2Q.                    \tag{15}
\]

These homogeneous equations have degrees five and eight and contain C.
Neither A nor Q divides F, so they have no common factor and form a proper
complete intersection. On \(x_0=1\), use the polynomial coordinates

\[
t=x_1,\quad x=x_2-t^3=A,\quad y=x_3-tx_2=Q.
\]

Then C is \((x,y)=0\) and

\[
F=t^2x+(t^4+tx+y)y^2
  =t(t+y^2)x+y^2(t^4+y),\qquad G=x^2y.             \tag{16}
\]

F is integral: its coefficient and constant term as a linear polynomial
in x are relatively prime in \(k[t,y]\), and its homogenization has no
x0 factor. At \(p=[1:0:0:0]\), both F and G have ambient multiplicity
three. For every cubic H, \(G+FH\) has no quadratic term there. Hence
every member is worse than a rational double point at p. Its first-symbol
common divisor on C has order two at this point.

The first symbol of F is \(x_1^2\sigma_A\), and that of G is zero.
The saturated first direction of A has quotient \(\mathcal O(-7)\): on
the finite chart its first symbol is x; at infinity, in coordinates
\(c=x_2/x_3, X=x_0/x_3-c^4, Y=x_1/x_3-c^3\), it is
\(2c^5X-3c^6Y\), with common order five. Thus its saturated line has
degree \(-12+5=-7\). This is an actual q=7 first-direction control.

Generically t is invertible. Eliminating x from (16) gives
\(x=-t^2y^2+O(y^3)\), so \(G\) has order five. The intersection cycle is
\(5C+R\), with \(\deg R=40-20=20\). Residual support is real: the line
\(x_1=x_3=0\), locally \(t=y=0\), lies in both surfaces and passes
through p. No multiplicity-ten defect or sole-support conclusion is claimed
for this control. The equations show directly that the first direction and
degree bounds alone do not supply the missing ADE hypothesis; residual
exclusion remains an essential extra condition.


## 8. How the two quintic proofs strengthen the shared surface mechanism

Both investigations begin with actual homogeneous equations, a saturated normal direction and first-symbol divisors. A simple moving first-symbol zero in a primitive multiplicity-\(m\) locus gives the surface germ \(xt+y^m\), hence an \(A_{m-1}\) chain. That local mechanism is shared; the global conclusions depend on the carrier degree, defect models and actual equation system.

For the [quartic pair](quartic_pair_obstruction.md), rank-four Gorenstein algebra classifies every fixed defect and forces exceptional rank at least twenty-one on a crepant resolution with trivial canonical bundle. The surface rank bound itself is contradictory. For the quintic–octic pair, reduced common divisor gives the local length-ten models in §3, but the general octic’s weighted ADE inequality discards none of the eight rows. The explicit quintic rank computation in §4 requires the full quintic symbol to be reduced, as well as a globally ADE quintic. It leaves rank forty, which fits within forty-four. The decisive extra information is the **actual Cartier linear equivalence** \(10C\sim8H\): it supplies integral Picard parity and an even-node cover. A numerical root-lattice relation alone would not justify that cover. The general even-node budget in §4.3 remains useful independently of this degree pair.

The [stronger globally ADE proof](quintic_octic_ade_cover_and_triple.md) retains the same Cartier relation but uses the nontrivial two-torsion Weil class \(5C-4H\). Its quasi-étale cover has \(K^2=10\), and the actual invariant canonical sections give a bound stronger than Noether alone. Exhaustive ADE bookkeeping leaves four rows, including repeated first-symbol zeros. The actual symbolic triple then has a saturated quadratic defect of degree zero, one or two; the degree-two survivor is supported at two distinct points, whereas the constant-direction embedded transition forces a double marked endpoint. This additional argument removes the reduced-symbol assumption without claiming that all degree-two triples are impossible.

The remaining boundary is exact: the quintic must have a non-ADE singularity somewhere, possibly off C. Merely imposing ADE along C is insufficient for either global surface argument. Repeated quintic first-symbol zeros no longer form a separate escape when the quintic is globally ADE. Nonnormal quintics and normal quintics with worse singularities are outside this theorem; the [residual-support control](#7-a-proper-homogeneous-residual-support-control) has generic multiplicity five and residual degree twenty, so it supplies neither a length-ten example nor a sole-supported pair. Ordinary-layer torsion is not by itself a bound on singularity type.

The earlier conditional proof, its corrected eight-row arithmetic, the local-model and residual-control scopes, and the generalized even-node budget (12) retain their independent consolidation review. The new companion preserves the separately reviewed full ADE proof and its audit’s additional controls; separate preservation review has accepted this stronger integration. No computer search or new computational certificate is needed. Both accounts retain the stated review scopes and do not supply an unrestricted STCI conclusion.
