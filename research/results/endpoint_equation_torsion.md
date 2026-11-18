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

In each ordinary degree \(n\), restrict to the two endpoint charts by
dividing a representative by \(x_i^n\), then complete at \((v,p_i)\) in the
raw family. For \(N=T\) or \(N=M_j\), write this joint map as \(\rho_{N,n}\),
using the corresponding torsion module or layer of each completed family. Then
\[
 \ker\rho_{N,n}=H^0_P(N)_n,\qquad
 H^0_P(N)=\{u:P^s u=0\text{ for some }s\}.
 \tag{1}
\]
**Both endpoints together detect every class in \(T_n\)** and preserve its
order of annihilation by \(v\). The maps on the layers can have kernels.

To measure the first kernel, write \(f_0=HU,\ g_0=HV\) for the two extreme
forms, with \(H\) their full gcd. Set
\[
 e_L=\operatorname{length}_{S_P}S_P/(U,V),\qquad
 K=H^0_P(M_1),\qquad \kappa_L=\operatorname{length}_{S_P}K_P.
\]
Here \(e_L=0\) if either stripped form is a unit at \(P\). Otherwise it is
the multiplicity of \(L\) in the complete intersection of \(U,V\). For the
**moving pair** one has
\[
 0\le\kappa_L\le e_L,\qquad
 \deg R=ab-4m\ \ge\ \operatorname{mult}_L[Y_0]\ \ge\ e_L-\kappa_L.
 \tag{2}
\]
Thus complete first-layer detection and \(e_L>0\) force an actual residual
curve of degree at least \(e_L\). In particular, **if \(H|_L\) is nonzero, the
extreme forms alone give \(\operatorname{mult}_L[Y_0]=e_L\) and
\(\deg R\ge e_L\)**. If either stripped form restricts nontrivially
to \(L\), the first layer is detected in **every** ordinary degree.

If the full flat limit omits the generic point of \(L\), then
\(\kappa_L=e_L\). This holds for every sole-supported pair. Under this
hypothesis, first-layer detection in all degrees is equivalent to at least
one of \(U|_L,V|_L\) being nonzero. If both vanish identically, then
\(\dim_k\ker\rho_{M_1,n}=e_L n+O(1)\) for \(n\gg0\). The line can
therefore carry equation relations even when it is absent from the full
flat limit.

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
[Faithful flatness of local completion](https://stacks.math.columbia.edu/tag/00MC).

**Detection before taking layers.** After inverting \(v\) the two equations
form a regular sequence by the torus substitution and properness. Neither
is divisible by \(v\), hence they have no common factor in \(S[v]\) and
give a height-two complete intersection there. Every associated prime of
\(T\subset E\) has height two and contains \(v\). A nonzero submodule killed
by a power of \(P\) would have an associated prime containing
\((v,x_0,x_3)\), of height three. Thus \(H^0_P(T)=0\). Applying injectivity
to each \(v^i u\) gives the order assertion. The same argument need not
apply to quotients of \(T\).
[Regular sequences in Cohen–Macaulay rings](https://stacks.math.columbia.edu/tag/02JN).

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

Localize at \(P\) and take the submodule of the middle term killed by powers
of the local maximal ideal. The second sequence identifies it with
\((S/(U,V))_P\) up to twist, of length \(e_L\). Its intersection with
\((M_1)_P\) is \(K_P\) by the first sequence and localization of
power torsion. Its image has length \(e_L-\kappa_L\) in \((B/vB)_P\).
This image is the ideal generated by \(H\) in \(S_P/(J_0)_P\). The
source of multiplication by \(H\) in
the second sequence is already of finite length at \(P\). Consequently
\[
 e_L-\kappa_L=\operatorname{length}_{S_P} S_P/(J_0:H)_P.
 \tag{3}
\]
The length of the entire target \((B/vB)_P\) is the coefficient of \(L\) in
the full flat cycle, zero when the generic point is absent. Indeed \(Y_0\) has dimension one, and
localizing at this homogeneous prime computes the same length as the
generic projective stalk (on a line chart the extra invertible coordinate
just extends its residue field).

Specialization of the fundamental cycle gives \([Y_0]=m[C]+\operatorname{sp}R\) because
the intrinsic torus preserves \(C\), while the specialization of the moving
residual is effective of degree \(\deg R\). Since \(L\ne C\) has degree one,
this proves (2). A power change of parameter preserves the special fiber
after flat base change of the contracted family.
[Specialization of the marked cycle](../arguments/torus_hilbert_boundary.md#invariant-residual-supports-and-absorption-limits).

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
\(\kappa_L\). Indeed, in a graded prime filtration exactly \(\kappa_L\) factors
are shifts of \(S/P=k[x_1,x_2]\), and the smaller-dimensional factors
contribute at most a constant. This proves the stated growth.
[Full supported limits](supported_hilbert_full_limits.md#statement).

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
Modulo \(I\), they imply \(vD=v^2E'=0\). Also \(x^2D=q^3g\).
Hence the degree-11 class \([xD]\in T/vT\) is killed by \(x\) and \(w\).
At \(p_0\) it maps to zero already in \(T\). At \(p_\infty\) the identity
\(wxD=-vE'\) makes it divisible by \(v\) in local torsion.

At the generic point of \(L\), the elements \(z,q,A\) are units, so the
raw special-fiber ideal is \((x^3,x^2w)\) and \(xD\) is a unit times
\(x^2\). Its image in that quotient is nonzero. Consequently its
annihilator in \(S\) is precisely \((x,w)\), and the joint kernel
contains a copy of \((S/(x,w))(-11)\). In degree 12 this gives the two
independent classes \([xyD],[xzD]\). Because \(v\) has ordinary degree
zero, \((T/vT)_{12}=T_{12}/vT_{12}\), exactly the source of the bounded
comparison. The failure persists in every degree from 11 on.

Here \(H=x^2\) and \((U,V)=(wA,xzq)\), so \(e_L=1\). At the generic
point of \(L\) in the raw family, \(x^3=0\) and \(v=-x^2wA/q^3\).
Thus parameter saturation removes this stalk and \(\kappa_L=1\).
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
The special ideal therefore contains \((x,w)^3\). The moving multiplicity
on \(L\) is six because modulo \(x\) the moving equation has order two in
\(w\), and intersection multiplicity is additive for the divisor \(3V(x)\).
Since the torus preserves \(L\), its coefficient in the flat limit is at
least six. The colength of \((x,w)^3\) is six, so the localized flat
special ideal equals \((x,w)^3\). The image of \(H=x^2\) there has length
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

Independent reconstruction checked the two localization kernels, faithful
flat base change, unmixedness, the gcd exact sequence and the cycle bound.
A separate review expanded the two sextic identities and checked the line
annihilator at its generic point. It also verified the companion of
length six. The local Macaulay2 calculation reproduced both generic lengths and
the two kernel lengths by saturation and ideal quotients. The existing
rational Smith verifier reproduces the two source profiles \((1^8,2)\) and \((1^2,2)\) in degree 12.
The kernel proof uses the displayed identities and needs no rank computation.

## Limitations

These maps use completed **equation presentations** on the total family.
The two embedded endpoint fibers of the transverse quotient carry different
data. A proposed sole-support realization still needs a single moving
saturated ideal with the prescribed homogeneous generators. The residual
pencil gives no such realization. The unrestricted characteristic-zero
STCI question remains open.
