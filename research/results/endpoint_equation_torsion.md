---
id: STCI-R-0073
type: result
title: Endpoint detection of equation torsion and a residual degree bound
scope: "#scope"
statement: "#statement"
proofs:
  - name: endpoint localization and the first equation layer
    at: "#proof"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#review-and-scope-of-the-comparison"
---
# Endpoint detection of equation torsion and a residual degree bound

In a torus degeneration of two surfaces through the quartic, their two
completed endpoint presentations together detect every homogeneous class
killed by a power of the parameter \(v\). They can nevertheless miss the
class of that element **modulo \(vT\)**. A global torsion element can become
divisible by \(v\) in both local torsion modules. The missing first-layer
classes live on the cone over the coordinate line disjoint from the quartic.
Their generic length measures how much of the intersection on that line,
as read from the extreme equations, can disappear from the flat cycle.
Two sextic pencils have identical extremes and flat line coefficients
zero and six.

## Scope

Let \(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k\) over an algebraically
closed field of any characteristic. Take **any actual proper homogeneous pair**
\(F,G\) of degrees \(a,b\) containing \(C\). Write its cycle as
\(m[C]+R\), with \(R\) effective and \(4m+\deg R=ab\). Fix either direction
of the intrinsic torus with weights \((0,1,3,4)\). Both endpoint maps below
are made in **this one degeneration**, at the geometric points
\(p_0=[1:0:0:0]\) and \(p_\infty=[0:0:0:1]\).

Write \(S=k[x_0,x_1,x_2,x_3]\), \(P=(x_0,x_3)\), and
\(L=V_+(P)=L_{12}\), the coordinate line disjoint from \(C\). In \(S[v]\)
take the actual orbit equations \(f,g\), clearing the parameter powers
separately so each has nonzero specialization. For example in the positive
direction substitute \(x_i\mapsto v^{w_i}x_i\) and divide each equation by
its lowest power of \(v\). The ordinary degree of \(v\) is zero. One can also
use an effective parameter when the equations descend under a power change
and remain equivariant, as in the sextic pencil below. Set
\[
 I=(f,g),\quad E=S[v]/I,\quad T=(I:v^\infty)/I,\quad
 B=E/T,\quad M_j=v^{j-1}T/v^j T\quad(j\ge1).
\]
Thus \(T\) consists of the classes killed by some power of \(v\).
Write \(J_0=\ker(S\to B/vB)\). The **full flat limit** \(Y_0=\operatorname{Proj}(S/J_0)\)
has saturated ideal \(J_0:S_+^\infty\) and Hilbert polynomial
\(abn+ab(4-a-b)/2\). This contraction keeps the entire projective special
fiber, including any embedded points. The modules \(T,M_j\) refer to the two equations
before this contraction. The prior [flat-limit and cancellation argument](../arguments/torus_hilbert_boundary.md#clean-cancellation-and-residual-descent)
identifies \(M_1\) with the difference between the full initial ideal and
the two extreme equations. The [extreme-gcd theorem](../arguments/torus/equivariant_degree_bounds.md#extreme-components-of-arbitrary-presentations)
controls their radical under its sole-support and characteristic hypotheses.
In characteristic zero its radical equality already excludes sole support
if \(L\) occurs outside the common hypersurface. It gives no multiplicity
there and cannot distinguish a relation supported on \(L\) inside that
hypersurface from a component of the full flat limit. These are the two
quantities measured below.

## Statement

**Raw torsion.** For \(t\in T_n\), vanishing of both completed endpoint
images implies \(t=0\). Applying this to \(v^i t\) for each \(i\) also
recovers its annihilation order.

**Filtration layers.** A nonzero \([t]\in (T/vT)_n\) disappears at both
endpoints precisely when \(t_i=v s_i\) for some \(s_i\) in the completed
local torsion module at each endpoint \(i\). There need not be a single
\(s\in T\) with \(t=vs\).
In each ordinary degree \(n\), restrict to the two endpoint charts by
dividing a representative by \(x_i^n\), then complete at \((v,p_i)\) in the
raw family. For \(N=T\) or \(N=M_j\), write this joint map as \(\rho_{N,n}\),
using the corresponding torsion module or layer of each completed family. Then
\[
 \ker\rho_{N,n}=H^0_P(N)_n,\qquad
 H^0_P(N)=\{u:P^s u=0\text{ for some }s\}.
 \tag{1}
\]
**Residual degree.** Write \(f_0=HU,\ g_0=HV\) for the two extreme
forms, with \(H\) their full gcd. Let \(e_L\) count the multiplicity of
the line in the intersection after removing \(H\), and let \(\kappa_L\)
count the generic length there of the first-layer classes missed by both
endpoints. In local algebra these are
\[
 e_L=\operatorname{length}_{S_P}S_P/(U,V),\qquad
 K=H^0_P(M_1),\qquad \kappa_L=\operatorname{length}_{S_P}K_P.
\]
Here \(e_L=0\) if either stripped form is a unit at \(P\). For the moving
pair one has
\[
 0\le\kappa_L\le e_L,\qquad
 \deg R=ab-4m\ \ge\ \operatorname{mult}_L[Y_0]\ \ge\ e_L-\kappa_L.
 \tag{2}
\]
Thus complete first-layer detection and \(e_L>0\) force a nonzero moving
residual cycle of degree at least \(e_L\), counting multiplicities. In
particular, **if \(H|_L\) is nonzero, the
extreme forms alone give \(\operatorname{mult}_L[Y_0]=e_L\) and
\(\deg R\ge e_L\)**. If either stripped form restricts nontrivially
to \(L\), the first layer is detected in **every** ordinary degree.

**First-layer criterion.** Assume \(\eta_L\notin Y_0\), as holds for every
sole-supported pair. Then \(\kappa_L=e_L\), and
\[
  \rho_{M_1,n}\text{ is injective for every }n
  \quad\Longleftrightarrow\quad
  U|_L\ne0\ \text{or}\ V|_L\ne0.
\]
The maps in this equivalence are joint restrictions on \(M_1=T/vT\).
When both restrictions vanish, their kernel has dimension \(e_L n+O(1)\)
for \(n\gg0\). Raw torsion is jointly detected without this hypothesis;
for higher layers (1) gives the kernel.

## Proof

**Restriction to one endpoint.** On the chart \(x_i\ne0\), set
\(z_l=x_l/x_i\) for \(l\ne i\). Dehomogenization on a fixed degree is
localization followed by taking degree zero after division by \(x_i^n\).
Its kernel is the \(x_i\)-power torsion. We show that passing from this chart
to the completed local module at its endpoint loses no further classes.

The chart has a second grading from the torus, with \(v\) assigned the
compensating weight making each orbit equation homogeneous. The three
weights of the \(z_l\) have the same strict sign at either extreme chart.
Orient that grading to make them positive. Since \(S[v]\) is Noetherian,
a single power \(v^h\) kills \(T\) and its layers. If a polynomial
\(s=s_0(z)+v b(v,z)\), with \(s_0(0)\ne0\), kills a chart class \(u\),
then \(s_0^h u=(-vb)^h u=0\). The lowest weight component of a nonzero
\(u\) survives multiplication by \(s_0^h\), whose constant coefficient is
nonzero. This proves injectivity upon localization at the endpoint for
classes of mixed torus weights as well. No sign condition on \(v\) was used.

Completion at that local ring is faithfully flat. Localization and flat
base change commute with the kernel of \(v^h\), images of powers of \(v\)
and the resulting quotients. Multiplication by \(v\) stays injective on
\(B\), so the torsion computed in the completed raw ring is exactly the
extended \(T\). The same argument works over \(k[[v]]\), because extending a
module killed by \(v^h\) from \(k[v]\) to \(k[[v]]\) leaves it unchanged.
Intersecting the two single-chart kernels gives (1), since an element killed by
a power of each of \(x_0,x_3\) is killed by a power of \(P\).
[Stacks, Lemma 10.97.3 (faithful flatness of Noetherian local completion)](https://stacks.math.columbia.edu/tag/00MC).

**Detection before taking layers.** After inverting \(v\) the two equations
form a regular sequence by the torus substitution and properness. Neither
is divisible by \(v\), hence they have no common factor in \(S[v]\) and
give a height-two complete intersection there. Every associated prime of
\(T\subset E\) has height two and contains \(v\). A nonzero submodule killed
by a power of \(P\) would have an associated prime containing
\((v,x_0,x_3)\), of height three. Thus \(H^0_P(T)=0\). Applying injectivity
to each \(v^i u\) gives the order assertion. The same argument need not
apply to quotients of \(T\).
[Stacks, Lemma 10.104.2 (regular sequences and dimension)](https://stacks.math.columbia.edu/tag/02JN) · [Lemma 10.103.7 (associated primes of a finite Cohen–Macaulay module)](https://stacks.math.columbia.edu/tag/0BUS).

**The line in the first layer.** Since \(v\) is regular on \(B\), reduction
modulo \(v\) gives the first of two exact sequences of graded \(S\)-modules below.
\[
\begin{aligned}
0&\longrightarrow M_1\longrightarrow S/(f_0,g_0)
                \longrightarrow B/vB\longrightarrow0,\\
0&\longrightarrow (S/(U,V))(-\deg H)\xrightarrow{\ H\ } S/(f_0,g_0)
                \longrightarrow S/(H)\longrightarrow0 .
\end{aligned}
\]
The second follows by cancelling \(H\) in the polynomial ring and includes
the unit cases. The hypersurface quotient has no associated prime containing
\(P\). The source of multiplication by \(H\) is zero or an unmixed height-two complete
intersection. The only associated prime of the middle term that could
contain \(P\) is therefore \(P\) itself, and it can occur only if
\(U,V\in P\). This proves the assertion in every degree when one stripped
form restricts nontrivially. It also rules out a separate finite-length
kernel at the irrelevant ideal for this first layer.

### Local torsion at the generic point of the line

**Lemma.** Put \(D=S_P\), \(\mathfrak m=PD\), and \(N=D/(HU,HV)\).
Multiplication by \(H\) identifies \(D/(U,V)\) with
\(H^0_{\mathfrak m}(N)\).

Indeed \(D\) is a regular local ring of dimension two. The coprime forms
\(U,V\) generate either the unit ideal in \(D\) or an \(\mathfrak m\)-primary
ideal, since no height-one prime contains both. Hence \(D/(U,V)\) has
finite length, including length zero. If \(H\notin P\), then \(H\) is
a unit in \(D\), and its image is all of \(N\). If \(H\in P\), it is a
nonzero nonunit in the domain \(D\). The quotient \(D/(H)\) is a
one-dimensional Cohen–Macaulay hypersurface, so some element of
\(\mathfrak m\) acts on it injectively. It has no \(\mathfrak m\)-power
torsion. In the localized gcd sequence every \(\mathfrak m\)-power torsion
element of \(N\) must therefore lie in the image of multiplication by
\(H\), and every element of that image is torsion by finite length.

The lemma gives a submodule of length \(e_L\). Its intersection with
\((M_1)_P\) is \(H^0_{\mathfrak m}((M_1)_P)=K_P\), by localization of
power torsion. In the first exact sequence its image in \((B/vB)_P\)
is the principal ideal generated by \(H\), of length \(e_L-\kappa_L\).
Taking the kernel of multiplication by \(H\) into that target gives
\[
 e_L-\kappa_L=\operatorname{length}_{S_P} S_P/(J_0:H)_P.
 \tag{3}
\]
The length of the entire target \((B/vB)_P\) is the coefficient of \(L\) in
the full flat cycle, zero when the generic point is absent. Indeed \(Y_0\) has dimension one, and
localizing at this homogeneous prime computes the same length as the
generic projective stalk (on a line chart the extra invertible coordinate
just extends its residue field).

### Specialization of the marked cycle

Work over the DVR \(A=k[v]_{(v)}\) with fraction field \(K_v\). The
projective family \(Y=\operatorname{Proj}(B\otimes_{k[v]}A)\) is the
schematic closure of its one-dimensional generic fiber in
\(\mathbf P^3_A\). Saturation by \(v\) removes the kernel of restriction
to the generic fiber. The resulting coordinate modules are torsion-free
over the DVR, hence flat, also on projective charts. For a closed flat
subscheme of a scheme locally of finite type over a DVR, specialization
takes the generic fundamental one-cycle to the special fundamental
one-cycle when the generic fiber has dimension at most one.
[Stacks, Lemma 15.22.11 (flatness over a DVR)](https://stacks.math.columbia.edu/tag/0AUW) · [Lemma 62.4.2 (specialization of the fundamental cycle)](https://stacks.math.columbia.edu/tag/0H4J).

Use the original torus parameter first. Its action preserves the marked
curve, so the generic cycle is \(m[C_{K_v}]+R_{K_v}\), where \(R_{K_v}\)
is the torus translate of the effective residual cycle. The closure of
the marked component is \(C_A\), and its specialization is \([C]\).
Specialization is additive and sends each integral residual component to
the effective one-cycle of the special fiber of its closure. Thus
\[
 [Y_0]_1=m[C]+\operatorname{sp}(R_{K_v}).
\]
The displayed \(m[C]\) is the contribution of the marked component.
The residual specialization can contribute further copies of \(C\).
Embedded points remain in \(Y_0\); its fundamental one-cycle takes lengths
only at generic points of curves. Taking degrees in this cycle identity,
the CI Hilbert polynomial gives \(\deg[Y_0]_1=ab\), so the effective residual
specialization has degree \(ab-4m=\deg R\). Since \(L\ne C\) is a line,
its coefficient is at most this degree. This proves (2).
[Stacks, §62.4 (specialization on cycles)](https://stacks.math.columbia.edu/tag/0H4H) · [Lemma 33.44.6 (degree weighted by generic lengths on a proper curve)](https://stacks.math.columbia.edu/tag/0AYW) · [Marked residual specialization](../arguments/torus_hilbert_boundary.md#invariant-residual-supports-and-absorption-limits).

For an effective parameter \(v=t^d\), pass from \(k[v]_{(v)}\) to
\(k[t]_{(t)}\). This extension is flat, and flat base change preserves
the schematic closure of the quasi-compact generic fiber. Specialization
of cycles commutes with the DVR extension, whose residue field is still
\(k\). The special fiber upstairs is taken modulo its uniformizer \(t\).
It is the same \(Y_0\), with the same cycle coefficients, for any \(d\)
including one divisible by the characteristic. Torsion layers are indexed
using the uniformizer of the chosen presentation.
[Stacks, Lemma 29.26.16 (schematic images under flat base change)](https://stacks.math.columbia.edu/tag/081I) · [Lemma 62.4.3 (specialization under DVR extension)](https://stacks.math.columbia.edu/tag/0H4K).

### Consequences for first-layer detection

If \(H\notin P\), each vertical associated prime of \(T\) has the form
\((v,h)\), where \(h\) is an irreducible common factor of \(f_0,g_0\).
Indeed it has height two and contains \(v,f,g\), so its image modulo
\(v\) is a height-one prime containing both extreme forms. None of these
primes lies in \((v,P)\). Thus \(T_{(v,P)}=0\) and the full special fiber
agrees there with the raw one, whose local ring on the cone is
\(S_P/(U,V)\). This proves the equality read directly from the extremes.

When \(L\) is absent generically, the image in \((B/vB)_P\) is zero and
\(\kappa_L=e_L\). A sole-supported orbit has this property in both directions because
a power of \(I_C\) cuts out a fixed neighborhood containing the orbit and
its closure. The graded module \(K\) is supported on the cone over the
line. If \(\kappa_L>0\), its eventual Hilbert function has slope
\(\kappa_L\). To see this, take a homogeneous prime filtration of the
finite graded \(S\)-module \(K\) (choose a homogeneous element with maximal
annihilator in each successive quotient). After localizing at \(P\)
exactly \(\kappa_L\) factors remain, each a shifted copy of \(S/P\) before
localization. Each contributes \(n+O(1)\) to \(\dim_k K_n\). The other
factors have dimension at most one, hence bounded Hilbert function.
If both \(U,V\) vanish on \(L\) and \(\eta_L\notin Y_0\), this proves
failure of joint first-layer detection in every sufficiently large degree.
The associated-prime argument gives the converse in every degree.
[Stacks, Lemma 10.62.1 (prime filtration)](https://stacks.math.columbia.edu/tag/00L0) · [Lemma 10.117.1 (dimension and Hilbert polynomial for the standard graded factors)](https://stacks.math.columbia.edu/tag/00P6) · [Full supported limits](supported_hilbert_full_limits.md#statement).

## A relation missed at both endpoints

Use the positive degeneration of the **actual proper residual sextic
pencil** \(W_0\) over \(\mathbf Q\) in the
[degree-12 Smith calculation](../arguments/torus_hilbert_boundary.md#degree-12-relation-persistence-for-the-residual-sextic-pencil).
With effective parameter \(v=t^5\), write \(x,y,z,w=x_0,x_1,x_2,x_3\) and set
\[
 q=xw-yz,\quad A=x^2z-y^3,\quad
 g=x^3zq,\quad f=x^2wA+v q^3,\quad
 D=xzq^4,\quad E'=z^4q^4,\quad B'=(q^3-z^3A)/x.
\]
The numerator of \(B'\) vanishes at \(x=0\). Two polynomial identities give
\[
 vD=(xzq)f-wAg,\qquad xwD+vE'=z^4qf+wB'g .
\]
Modulo \(I\), they imply \(vD=v^2E'=0\). Since \(x^2D=q^3g\) and
\(wxD=-vE'\), the annihilator of the degree-11 class \([xD]\in T/vT\)
contains \(P=(x,w)\). On the \(x\)-chart the element \(xD\) itself is
zero. On the \(w\)-chart it has the torsion divisor \(-E'/w\) by \(v\).

For the reverse annihilator inclusion, localize at \(P\). Here \(z,q,A\)
are units, so setting \(v=0\) in the raw equations gives the ideal
\((x^3,x^2w)=x^2(x,w)\). The class of \(xD=x^2zq^4\) is nonzero in
that quotient since \(zq^4\) is a unit. The injection \(T/vT\hookrightarrow
S/(f_0,g_0)\) therefore shows \([xD]_P\ne0\). Any annihilator outside
\(P\) would be a unit at this stalk and would kill this nonzero class.
Hence \(\operatorname{Ann}_S([xD])=P\), and \([xD]\) generates a copy
of \((S/P)(-11)\) in the joint kernel. In degree 12 this gives the two
independent classes \([xyD],[xzD]\). Because \(v\) has ordinary degree
zero, \((T/vT)_{12}=T_{12}/vT_{12}\), exactly the source of the bounded
comparison. The failure persists in every degree from 11 on.

Here \(H=x^2\) and \((U,V)=(wA,xzq)\) generates \(P S_P\), so \(e_L=1\).
In the total ring localized at \((v,P)\) the raw ideal is
\((x^3,v+x^2wA/q^3)\). Modulo this ideal \(v^2=0\) because \(x^4=0\).
Its saturation by \(v\) is the unit ideal. Thus the flat special stalk
is zero and \(\kappa_L=e_L=1\).
The line carries a first-layer relation although it is absent from the
full limit at its generic point. This geometry answers the bounded
endpoint question with an explicit nonzero class in the kernel.

Changing only the higher-weight term reverses the outcome at the same
line. Take the companion pencil generated by \(x^2wA+w^2q^2\) and the
same \(g\). Both projective flat limits have Hilbert polynomial \(36n-144\).
The companion remains proper since none of \(x,z,q\) divides its first form. It has identical positive extremes, hence the same \(H,U,V,e_L\).
At the generic point of the line, \(A,q,z\) are units and the new family
has equations \(x^3,\ x^2wA+v w^2q^2\) with effective parameter
\(v=t^9\). Multiplying the latter by \(x\) gives \(xw^2\) after
parameter saturation. Multiplying by \(w\) then gives \(w^3\).
Along with the two special equations \(x^3,x^2w\) up to units, these
give \((x,w)^3\subseteq (J_0)_P\). For the opposite length bound,
compute the moving multiplicity in \(k(y,z)[[x,w]]\) at parameter one.
Modulo \(x\), the first form is \(y^2z^2 w^2\). In the quotient by that
first form, \(x\) is a nonzerodivisor, since \(x\) is prime and does not
divide the form. Successive quotients by \(x\) in its filtration modulo
\(x^3\) thus all have length two. The moving cycle contains \(6[L]\).
The torus fixes \(L\), so the specialization lemma applied to this marked
line preserves that summand and the other summands specialize effectively.
It follows that \(\operatorname{length}(S_P/(J_0)_P)\ge6\). The surjection
from \(S_P/(x,w)^3\), itself of length six, has zero kernel. This proves
equality of the two localized ideals. The image of \(H=x^2\) there has length
one, and (3) gives \(\kappa_L=0\). The two actual pencils thus distinguish
a line carrying a missed relation from a line carrying residual cycle
multiplicity while keeping even the extreme equations fixed.

## Test on supplied equations

The [Macaulay2 line test](../arguments/torus-sextic-controls.support/endpoint_line_test.m2)
accepts two coprime homogeneous forms over \(\mathbf Q\) through \(C\) and a
direction. Load the file in Macaulay2 and call
`endpointLineTest(F,G,"min")` or `endpointLineTest(F,G,"max")` in the
coordinate order \(x_0,x_1,x_2,x_3\). It returns the two restriction tests,
\(e_L,\kappa_L\), and the coefficient of \(L\) in the full flat cycle, a
lower bound on the moving residual degree. A zero lower bound leaves the
residual degree undetermined.

The calculation works at \((x_0,x_3)\) over \(\mathbf Q(x_1,x_2)\).
When \(H|_L\ne0\), the extremes suffice. Otherwise it builds the original
orbit equations over that field, saturates by the torus parameter, and
specializes to get \(J_0\) there. Localization commutes with taking this
parameter saturation. The local colengths of \(J_0\) and \(J_0:H\) give
the flat coefficient and (3). All required local quotients have finite
length. Their dimensions modulo successive powers of \((x_0,x_3)\)
stabilize at that length by Nakayama's lemma. Run the examples from the
repository root.

```sh
M2 --script research/arguments/torus-sextic-controls.support/endpoint_line_test.m2
```

For a check where the predicted line first appears in the limit, take
\(F=xq+z^3-yw^2\), \(G=wA\) in the coordinates above. The cubic restricts
to \(z^3\) on \(L\), while the minimum-weight forms are \(xq,wA\).
They are coprime and generate \((x,w)\) at its generic point. The same
calculation for \(F^r,G^s\), \(r,s\ge1\), gives \(H=1\) and
\(e_L=rs\) from \((x^r,w^s)\). Thus the moving residual has degree at
least \(rs\) although it does not contain \(L\). The script checks
\(r=s=2\) and the distinct case \(H|_L=0\) of the sextic witness.

## Review and scope of the comparison

The revised written proof received a favorable mathematical and editorial
re-review, including the local torsion lemma, DVR specialization, and sextic
local calculations. The reviewer did not independently execute the Macaulay2
or Smith scripts. [Initial review](https://github.com/markluxton1/STCI/pull/151#pullrequestreview-5959552820) · [Follow-up review](https://github.com/markluxton1/STCI/pull/151#pullrequestreview-5960083577).

The proof derives the endpoint kernels, the line-length identity and
the residual inequality from the cited classical algebra and cycle
specialization results. Their application to the two completed presentations
of the same equation pair, and the explicit failure of first-layer detection,
are the contributions here. Both sextic line coefficients and the annihilator
of \([xD]\) are calculated in the text. Separate checks of this revision
reconstructed the DVR specialization and the two sextic local calculations.

As computational cross-checks, the Macaulay2 replay gives
\((e_L,\kappa_L,\operatorname{mult}_L[Y_0])=(1,1,0)\) for \(W_0\) and
\((1,0,6)\) for the companion. The rational Smith replay checks the
degree-12 **source** profiles \((1^8,2)\) for \(W_0\) and \((1^2,2)\)
for \(W_1\), a different pencil from the companion. The endpoint kernel
calculation follows from the polynomial identities and localization above.

## Limitations

These maps use completed **equation presentations** on the total family.
The two embedded endpoint fibers of the transverse quotient carry different
data. The sextic witness rules out a general inference from joint local
divisibility to global divisibility in \(T\). For a hypothetical
sole-supported pair, (2) allows \(\kappa_L=e_L\) and gives lower bound
zero. To exclude a specified family via \(e_L-\kappa_L\), it suffices
to establish, independently of sole support, \(\kappa_L\le e_L-1\) in
some intrinsic direction for every pair in the family. This requires \(e_L>0\) in that
direction. A claim about unrestricted STCI would also require coverage
of all candidate pairs. Construction still requires a single moving
saturated ideal with the prescribed homogeneous generators. The
characteristic-zero STCI question for \(C\) remains open.
