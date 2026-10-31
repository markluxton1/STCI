# A broad obstruction program: normal monodromy and an actual quadric residual

October 30, 2026. Investigator: nonexistence_advocate; the all-degree-margin
quadric-residual argument was proposed jointly with geometry_referee and
independently reconstructed by root. Status: **proposed enlargement under
independent geometric review**. No canonical result or question changes.
The purpose is both to enlarge exclusions independently of the opponent's
current proposal and to test that proposal accurately.

The curve is \(C=C_0=[s^4:s^3t:st^3:t^4]\) over an algebraically closed
characteristic-zero field. Write \(Q=(q=0)\),
\(q=x_0x_3-x_1x_2\), and
\[
V_{a,m}=H^0(\mathbf P^3,\mathcal I_C^m(a)).
\]
Powers are sheaf powers, equivalently saturated homogeneous powers.
For a proper containing pair retain
\([V(F_a,G_b)]=m_C[C]+R\), \(ab=4m_C+\deg R\).

## 1. The independent program and the geometric object being measured

The reviewed all-degree
[weighted-subalgebra obstruction](2026-10-30-weighted-subalgebra-line-obstruction.md)
uses actual lines on a carrier, not merely its local normal roots.
The reviewed [fixed-quadric boundary theorem](2026-10-30-stci-game-quadric-boundary.md)
uses a residual divisor on \(Q\) that every allowed correction preserves.
The next independent question is whether the **entire actual quadric
residual** supplies a test curve on much larger carrier spaces.

It does on the ordinary locus described below. A single irreducible
normal-direction cover forces one global multiplicity for a hypothetical
mate upstairs. The hyperplane and the quadric residual then impose
incompatible divisor-degree equations. This is a geometric independence
of two numerical divisor classes, not an inference from a parameter count.

## 2. Literal test-curve theorem in every degree margin

Fix \(m\ge1\), \(a\ge3m\), and \(F\in V_{a,m}\) of exact normal order
\(m\), with \(q\nmid F\). Assume:

1. The full first normal root divisor is horizontal, reduced and
   irreducible. Equivalently here, the initial binary normal form is
   irreducible of degree \(m\) over \(k(C)\), with no vertical coefficient
   divisor. Its normalization branch \(\Gamma\) has generic degree \(m\)
   over \(C\).
2. Inside \(Q\simeq\mathbf P^1\times\mathbf P^1\), the actual restriction is
   \[
   \operatorname{div}_Q(F)=mC+T,
   \quad [T]=(a-m,a-3m),
   \]
   with \(T\) reduced, no component equal to \(C\), and \(T\cap C\)
   reduced. The intersection avoids the two parametrization endpoints.
3. At each point of \(T\cap C\), the normal root in the direction tangent
   to \(Q\) is simple. The corresponding local branch of the normalization
   is regular, and the strict transform of \(T\) meets \(\Gamma\) simply.
   This last assertion follows from the simple-root condition and the
   transverse intersection in item 2, as verified below.

Then **no homogeneous \(G_b\), \(b>0\), has
\(V(F,G_b)_{\mathrm{red}}=C\)**. Global irreducibility of \(F\) need not
be added as a separate hypothesis.

### Why the branch hypothesis has actual geometric content

Use local coordinates \(t,u,q\), with \(C=(u,q)\) and \(Q=(q)\).
Blow up \((u,q)\) and use \(q=uz\). After dividing by \(u^m\), the
strict-transform equation has the form
\[
f_m(t,1,z)+u(\cdots)=0.
\]
At a point of \(T\cap C\), its root \(z=0\) is simple. The implicit
function theorem gives a regular graph \(z=z(t,u)\). Its inverse curve
is \(u=0\). The strict transform of the actual residual \(T\), with
\(q=0\), lies on this one local branch. Since \(T\) meets \(C\)
transversely in \(Q\), \(u\) has order one on \(T\).
Other normal roots at the same base point need not be simple: only
this attached root is used.

Every component of \(T\) is generically in the smooth locus of \(V(F)\):
away from \(C\), its reduced equation in \(Q\) has a nonzero derivative.
Thus its strict transform maps birationally to that actual component.
These are genuine curves downstairs, not vertical exceptional cycles.

### The two incompatible degree equations

Suppose a sole-support mate existed. Every irreducible factor of \(F\)
must contain \(C\); otherwise its proper positive-degree intersection
with \(G_b\) would be a projective curve contained in its finite
intersection with \(C\). A common surface factor with \(G_b\) already
violates sole support. The irreducible first normal form then forces
\(F\) to have just one global factor, with multiplicity one.

Let \(\nu:S\to V(F)\) be its finite normalization and
\(H=\nu^*\mathcal O(1)\). The divisorial inverse image of \(C\) is the
single curve \(\Gamma\), of degree \(m\) over \(C\). A hypothetical mate
has
\[
\operatorname{div}(\nu^*G_b)=r\Gamma,\qquad r>0.
\]
Intersection with \(H\), using \(H^2=a\), \(H\cdot\Gamma=4m\), gives
\[
ab=4mr. \tag{1}
\]
Its restriction to the actual residual curve \(T\) is nonzero and has
zeros only at \(T\cap C\). The local graph above makes every zero have
order exactly \(r\). Therefore
\[
b\,\deg T=r(C\cdot T).
\]
Here the actual divisor classes on the smooth target quadric give
\[
\deg T=2a-4m,\qquad C\cdot T=4a-6m.
\]
Consequently
\[
b(2a-4m)=r(4a-6m). \tag{2}
\]
Eliminating \(r\) between (1) and (2) requires
\[
2a^2-7am+8m^2=0.
\]
This is impossible: its discriminant in \(a/m\) is \(-15\), or
\[
2a^2-7am+8m^2
=2(a-7m/4)^2+15m^2/8>0.
\]
The obstruction is uniform in the mate degree.

When the normalization is regular along the whole \(\Gamma\), the same
geometry can be expressed as a numerical divisor gap. The pullback of
the quadric is \(\Gamma+\widetilde T\), so
\[
\Gamma^2=14m-4a,\qquad
\det\begin{pmatrix}H^2&H\Gamma\\H\Gamma&\Gamma^2\end{pmatrix}
=-2(2a^2-7am+8m^2)<0.
\]
A mate would make \(bH=r\Gamma\), forcing that determinant to vanish.
The actual residual curve exhibits the numerical independence directly.

## 3. A nonempty dense open subset of every full actual source is excluded

The preceding hypotheses hold on a nonempty Zariski-open subset of
every \(V_{a,m}\), \(a\ge3m\). This is a statement about the full actual
global source, not merely the small subalgebra \(k[q,c_0,c_2]\).

The promoted [normal-bundle splitting R-0020](../results/quartic_conormal_characteristic_jump.md)
gives \(\mathcal I_C/\mathcal I_C^2=\mathcal O(-7)^2\).
On the normal-direction surface
\[
P=\mathbf P^1_{\rm base}\times\mathbf P^1_{\rm direction},
\]
the order-\(m\) symbol of a degree-\(a\) equation cuts a divisor of class
\[
(4a-7m,m).
\]
The first entry is the coefficient degree on the base; the second is
the degree of its covering of \(C\).

The actual cubic equations globally generate
\((\mathcal I_C/\mathcal I_C^2)(3)=\mathcal O(5)^2\): use the cubic
generators of \(\mathcal I_C\) and the products \(q x_i\). Hence their
normal forms give a basepoint-free system of class \((5,1)\) on \(P\).
Writing \(a=3m+u\), \(u\ge0\), the products of \(m\) cubics multiplied
by ambient degree-\(u\) forms lie in \(V_{a,m}\) and generate the
symbol line bundle \(\mathcal O_P(4a-7m,m)\) at every point.
The full actual symbol system is therefore basepoint free and ample.

In characteristic zero a general member is smooth by Bertini. It is
connected because
\[
H^1(P,\mathcal O_P(-(4a-7m),-m))=0
\]
by the Künneth formula. A smooth connected divisor is irreducible.
This produces the single horizontal normal cover, of degree \(m\).
For the standard Bertini framework see
[Stacks, Section 33.47](https://stacks.math.columbia.edu/tag/0FD4) and
[the geometric irreducibility criterion in Section 37.32](https://stacks.math.columbia.edu/tag/0G4C).
Here ampleness, basepoint freedom, and connectedness are checked for the
actual symbol image; surjectivity onto the full abstract symbol space
is not assumed.

The residual restriction system on \(Q\) contains all products of
degree-\(2m\) forms in the first ruling and forms of class \((u,u)\).
It is therefore the complete system of class \((2m+u,u)\).
For \(u>0\), a general residual \(T\) is smooth and meets \(C\)
transversely away from the endpoints. For \(u=0\), it is \(2m\)
distinct nonendpoint ruling lines, and their cubic inverse parameters
on \(C\) are distinct in characteristic zero.

The simple attached normal root is also an actual open condition with
a nonempty complement to its failure locus. At each point of the
quadric-direction section on \(P\), choose a cubic \(H_3\) whose normal
value is nonzero and an ambient linear form \(\ell\) nonzero at the
base point. The normal forms of
\[
H_3^m P_u,\qquad qH_3^{m-1}P_{u+1}
\]
can be chosen with respectively a nonzero value, and zero value but
nonzero vertical derivative. Both have degree \(a\) and order at
least \(m\). Thus value and vertical derivative impose two independent
linear conditions at each point of this one-dimensional section.
The bad incidence has codimension at least one in the projective
symbol parameter space. Its image is closed because the section is
projective. A general symbol avoids it.

The finite collection of nonempty open conditions just described has
nonempty intersection in the irreducible actual parameter space.
Pulling them back under the linear symbol map gives the claimed
nonempty dense open subset of \(V_{a,m}\). Every member in that open
has no mate of any degree.

This does not prove that a generic pair fails by a new dimension
heuristic: it identifies an explicit geometric open carrier class and
a uniform test-curve contradiction on it. A hypothetical STCI can
still lie in its special closed complement.

## 4. A normal-root slope balance on the remaining ordinary locus

There is a refinement when the full normal root divisor is horizontal
and reduced but possibly reducible, while the actual residual and all
its attachments satisfy the regularity conditions above. Let its
components have projection degrees
\[
e_j=\deg(Z_j\to C),\qquad d_j=\deg(Z_j\to\mathbf P^1_{\rm direction}).
\]
Then
\[
\sum e_j=m,\qquad \sum d_j=4a-7m.
\]
The quadric normal direction is a graph of degree one. Indeed its
conormal form is a nowhere-simultaneously-zero pair of linear forms
in the balanced splitting. Its intersection with \(Z_j\) therefore
has degree \(e_j+d_j\); these are exactly the ordinary actual
attachments of \(T\) to the inverse curve \(\Gamma_j\).

A hypothetical mate has orders \(r_j>0\) on these inverse curves.
The two global degree equations become
\[
ab=4\sum e_jr_j,\qquad
b(2a-4m)=\sum(e_j+d_j)r_j.
\]
Thus
\[
\frac{\sum d_jr_j}{\sum e_jr_j}=7-\frac{16m}{a}. \tag{3}
\]
The unweighted ratio of the two sums is
\((4a-7m)/m\), strictly larger, since
\[
4a/m-7-(7-16m/a)
=\frac{2(2a^2-7am+8m^2)}{am}>0.
\]
Consequently a surviving ordinary candidate must have some component
\[
\boxed{\frac{d_j}{e_j}\le7-\frac{16m}{a}<7.}
\]
At the critical degree \(a=3m\), the bound is \(5/3\); a component
of covering degree one then has direction degree at most one.
This locates the possible escape in a low-variation component,
repeated/vertical normal structure, or nonordinary attachments.
It does not say that such a component is globally realizable by a
supporting pair.

## 5. An explicit new carrier outside the old subalgebra

The test-curve criterion is nonvacuous beyond the old source. Put
\[
F=c_0^2+c_2^2+q\,x_0c_0,\qquad
c_0=x_1^3-x_0^2x_2,\quad c_2=x_2^3-x_1x_3^2.
\]
It has degree six and order two. On \(x_0=1\), with \(u=w-t^3\),
its initial binary quadratic is
\[
4t^{10}q^2+(-4t^{11}-1)qu+(1+t^{12})u^2.
\]
Its discriminant is \(1+8t^{11}-16t^{10}\), of odd degree eleven,
so it is not a square in \(k(t)\). Hence there is one generic
normalization inverse curve of degree two over \(C\).

On the actual quadric,
\[
F|_Q=u^2(w^4+1).
\]
The four residual lines have \(w=\zeta\), \(\zeta^4=-1\), and meet
\(C\) at \(t^3=\zeta\). At these points the coefficient
\(-4t^{11}-1\) is nonzero: its vanishing together with
\(t^{12}=-1\) would force \(t=4\), impossible in characteristic zero.
Thus each attached \(q=0\) branch is regular and every line meets it
simply. The single-cover test-line argument excludes all mate degrees:
\[
6b=8r,\qquad b=3r.
\]

The carrier is outside the constant-coefficient degree-six subalgebra
source. Its quadric restriction fixes the binary boundary
\(c_0^2+c_2^2\); representing its remaining term there would require
\(q x_0c_0\) to be a scalar multiple of \(q^3\), which it is not.

The [new exact control](../computations/stci_game_obstruction_2026_10_30.m2)
checks this carrier's normal form, discriminant, line factorization
and nonvanishing condition. Its
[output](../computations/stci_game_obstruction_2026_10_30.txt)
is a local/global identity control, not an unproved normalization
classification. This example need not belong to every smooth-root
generic condition in Section 3; the smaller test-line criterion suffices.

## 6. The actual exchange with the existence side

The existence advocate's current E3 is an elliptic inverse curve
\(\Gamma=(2,2)\) mapping to \(C\) with degree two, on a source smooth
quadric with \(H=(2,2)=\Gamma\). The first explicit member is
basepoint free and birational onto a degree-eight image, but has a
projective off-\(\Gamma\) inverse scheme of length twelve. The
[existence record](2026-10-30-stci-game-existence.md) retains that
failure and the full five-parameter revision.

This is not refuted by calling it generic. With \(a=8,m=2\), a
horizontal root component of data \((e,d)=(2,6)\) has ratio three,
exactly the target \(7-16m/a=3\) in (3). A full order-two initial
divisor has class \((18,2)\), so such a horizontal component requires
vertical boundary data of degree twelve. The source elliptic curve
also has much lower genus than a smooth full \((18,2)\) root cover,
whose genus would be seventeen. These are geometric reasons E3
lies outside the ordinary dense open class, not proof it is impossible.

The numerical divisor relation \(H=\Gamma\) makes a mate pullback
\(b\Gamma\) possible upstairs. The existence side proposes to move
the twelve unwanted inverse points onto \(\Gamma\), retaining their
boundary defect as ramification/attachment data, then test actual
global descent. I challenged the missing family-level support test
and asked for the residual curve class in its quotient model. The
existence side explicitly acknowledged that this residual class and
its saturation are uncomputed. Neither side claims a uniform floor
for that entire family yet.

## 7. What changes for the general STCI question

The independent obstruction has expanded from a small graded source
and a large fixed-cubic fiber to a dense open part of **every**
non-forced-factor degree/order source \(V_{a,m}\), \(a\ge3m\).
It is uniform in the mate degree. Merely moving to large degree or
large individual equation spaces therefore does not make a generic
carrier useful.

The constructive response is precise: seek the special normal-cover,
vertical-defect, repeated-root or attachment boundary where the
test-curve equations change. E3 is an actual example of this kind
of numerical escape, although its first member fails full support.

The missing universal implication is still substantial. Nothing
proved here places every hypothetical defining carrier in the
ordinary open class, bounds all vertical defects, or excludes all
low-variation components in (3). No global triangular row operation
has been shown to remove those boundary cases. The unrestricted
characteristic-zero question remains open.
