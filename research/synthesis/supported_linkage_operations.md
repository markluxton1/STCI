# Constructing supported curves: ACM sources and stronger descent gates

Work over an algebraically closed field of characteristic zero with
\(C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\). Put
\[
 S=k[a,b,c,d],\quad E=S[z]/(z^2-2bc+ad),\quad Q_3=\operatorname{Proj}E,
\]
with involution \(\sigma(z)=-z\). The lift
\[
 D=[s^4:s^3t:s^2t^2:st^3:t^4]\subset Q_3
\]
is displayed in coordinates \([a:b:z:c:d]\); write \(P=I_D\subset E\).
All constructions preserve this embedding and hyperplane polarization.
The intermediate constructive target considered here is an actual supported
**ACM curve downstairs in \(\mathbf P^3\)**. A complete intersection is a stronger target. For a codimension-two
curve in \(\mathbf P^3\), AG implies CI: if S/I is CM, the Hilbert–Burch resolution of I
has last free rank equal to the CM type of S/I; type one gives two ideal
generators, hence a regular sequence. An ACM quotient need not have type
one and its ideal can have more than two minimal generators. An ACM
curve on \(Q_3\) therefore supplies useful input, with its actual projection
and coordinate image still to be checked. The deductions here are reviewed
construction controls, not an STCI conclusion. The
unrestricted characteristic-zero question remains open.

The [quadratic-cover account](quadratic_covers_and_conductor_descent.md)
owns the arbitrary-pair boundary, automatic conjugate descent, and the
criterion that an AG conjugate union supplies a CI image. The
[residual liaison account](residual_liaison.md) owns once-link flatness,
reverse recovery of equations, and the fixed-partner deformation space.
Here the problem is a different one: construct actual supported schemes,
then test whether their generic algebra and descended equations can
meet those global requirements.

## 1. Rao dimensions repeat the canonical-boundary inequality

Suppose a supported complete intersection has degrees \(\alpha,\beta\),
put \(e=\alpha+\beta-4\), and extract its full \(D\)-primary lift \(W\).
In the notation of the quadratic-cover account, its coordinate ring
\(B\) fits into
\[
 0\to A\to B\to T(-1)\to0,
\]
where \(A=S/(F_\alpha,G_\beta)\), \(T=A/\mathfrak c\) is the
one-dimensional graded CM conductor-boundary ring, and
\(\Delta=\operatorname{Proj}T\) has length \(\delta\).
No ACM or Gorenstein hypothesis on \(B\) is imposed. The canonical
sequence and graded local duality give
\[
 0\to T(e-1)\to\omega_T\to M_W^\vee(-1)\to0,
 \tag{1}
\]
where
\(M_W=H^1_*(Q_3,\mathcal I_{W/Q_3})=H^1_{\mathfrak m}(B)\) and
\(M^\vee_j=\operatorname{Hom}_k(M_{-j},k)\).
For \(H_\Delta(n)=\dim_k T_n\), degree \(1-n\) of (1) is
\[
 \dim_k M_W(n)=\delta-H_\Delta(n-1)-H_\Delta(e-n).
 \tag{2}
\]
Indeed \(\dim(\omega_T)_j=\delta-H_\Delta(-j)\), as follows by
writing \(T\) as a free graded module over a regular linear form.
Substitution gives (2) with no additional geometric assumption.

The symmetry \(n\leftrightarrow\alpha+\beta-3-n\) is automatic.
Nonnegativity in (2) is precisely the existing canonical restriction
inequality; comparing these dimensions does not supply a second budget.
The [ambient extremal-boundary argument](quadratic_covers_and_conductor_descent.md#12-embedded-curve-exclusion-of-the-minimal-boundary) adds information not contained in this numerical identity: for a supported fixed-quartic pair it excludes the minimal boundary by forcing a genuine line downstairs, strengthening the lower bound to \(\delta\ge\alpha+\beta-2\).

The multiplication maps and embedded presentation remain additional
information. [Hartshorne–Migliore–Nagel, §5, especially Example 5.5](https://academicweb.nd.edu/~jmiglior/HMN.pdf)
explicitly retain MCM-module and presentation data beyond the Rao
module for CI-biliaison on \(Q_3\). That source supplies no bound
incompatible with this particular support or its direct conjugate link.

The attachment identity \(g_Y=g_W+\delta\) also shows that an upper
bound for \(g_W\) gives a lower bound for \(\delta\), rather than the
upper boundary budget that an obstruction comparison would need.

## 2. Support and multiplicity alone give no genus lower bound

Write \(N^*_{D/Q_3}=\mathcal O_{\mathbf P^1}(u_0)\oplus
\mathcal O_{\mathbf P^1}(v_0)\). For every
\(l>\max(u_0,v_0)\), the sections
\(s^{l-u_0},t^{l-v_0}\) have no common zero and give a surjection
\[
 N^*_{D/Q_3}\twoheadrightarrow\mathcal O_{\mathbf P^1}(l).
\]
The kernel of the composite
\(\mathcal I_D\to N^*_{D/Q_3}\to\mathcal O(l)\)
is an ideal sheaf containing \(\mathcal I_D^2\). It defines an
embedded ribbon \(W_l\subset Q_3\), with exact sequence
\[
 0\to\mathcal O_{\mathbf P^1}(l)\to\mathcal O_{W_l}
 \to\mathcal O_D\to0.
\]
Thus \(p_a(W_l)=-l-1\), with fixed support \(D\) and multiplicity two.
This is the Ferrand quotient/kernel construction, recalled in
[Notari–Ojeda–Spreafico, §2](https://arxiv.org/pdf/0812.2578).
For large \(l\), \(h^0(\mathcal O_{W_l})=l+2>1\), so these ribbons
are not ACM: a projective ACM curve has only the constant sections in
degree zero. No AG conjugate union is asserted.

Consequently a genus lower bound using only fixed support, multiplicity
and the smooth ambient quadric is false. A bound using actual ACM or
AG-union hypotheses is a different question. [Jaffe, Theorem 10.3](https://arxiv.org/pdf/alg-geom/9410008)
gives higher-blowup inequalities when both defining surfaces are
generically smooth along \(C\), explicitly \(C\not\subset\operatorname{Sing}S\)
and \(C\not\subset\operatorname{Sing}T\). Those premises do not cover
arbitrary normal orders and common generic singularities. Its stronger
global conclusions require their own further hypotheses.

## 3. Actual supported ACM schemes from basic double linkage

Put
\[
 f=b^2-az,\qquad g=c^2-dz.
\]
They form a regular sequence in \(E\), with reduced zero locus \(D\)
and cycle \(2[D]\). One direct verification is as follows. On \(z\ne0\),
eliminating \(a,d\) gives \((bc-z^2)^2=0\), hence the rational-normal
ratios on the reduction; on \(z=0\), \(b=c=0,ad=0\) gives exactly
the endpoints. The homogeneous ideal has height two in the CM domain
\(E\), so the sequence is regular. Its intersection degree is eight,
whereas \(\deg D=4\); unmixedness gives the indicated multiplicity two.

For every \(u,v>0\), define the actual homogeneous ideal
\[
 I_{u,v}=(f^u)+g^vP.
 \tag{3}
\]
This is the basic-double-link pattern of
[Migliore–Nagel, Definition 2.1](https://www3.nd.edu/~jmiglior/MN7.pdf).
Its needed properties in this quadric coordinate ring follow directly,
without extending that paper's ambient hypotheses. Since
\((f^u):g^v=(f^u)\subset P\), multiplication by \(g^v\) gives
\[
 0\to(E/P)(-2v)\xrightarrow{\cdot g^v}E/I_{u,v}
 \to E/(f^u,g^v)\to0.
 \tag{4}
\]
Both end modules are CM of dimension two. The middle module is therefore
CM, and its ideal is saturated and unmixed. Its radical is \(P\): a
prime containing (3) either contains \(P\), or contains both \(f,g\),
whose radical is already \(P\). Thus \(W_{u,v}=\operatorname{Proj}E/I_{u,v}\)
is an actual ACM supported thickening, with
\[
 [W_{u,v}]=(1+2uv)[D],\qquad\deg W_{u,v}=4+8uv.
 \tag{5}
\]
These follow from (4) and the degree \(8uv\) of its CI quotient.
This source achieves actual ACM compatibility on Q3.

## 4. A uniform local algebra lemma: every higher-order containing section has type two

The generic failure has a more general form than the power source.

**Lemma.** Let \(K\) be any field, \(R=K[[x,y]]\), and
\(\mathfrak m=(x,y)\). Suppose \(h\in\mathfrak m^2\) and
\(h(0,y)\ne0\), with \(n=\operatorname{ord}_y h(0,y)\ge2\).
For every \(v\ge1\), the ideal
\[
 J=(h,x^{v+1},x^v y)=(h)+x^v\mathfrak m
 \tag{6}
\]
has height two, three minimal generators, colength \(nv+1\), and
Artinian CM type exactly two. In particular \(R/J\) is not Gorenstein.
There is no hypothesis that \(h\) is a power, or that \(y\nmid h\).

**Proof.** Write \(h=xA+yB\) with \(A,B\in\mathfrak m\), which is
possible because \(h\in\mathfrak m^2\). The matrix
\[
 \begin{pmatrix}
 0&x^v\\
 y&-A\\
 -x&-B
 \end{pmatrix}
 \tag{7}
\]
has signed maximal minors equal, up to harmless signs, to
\(h,x^{v+1},x^v y\). This ideal has height two: it contains
\(x^{v+1}\), and reduction of \(h\) modulo \(x\) is nonzero in
\(K[[y]]\). Hilbert–Burch therefore gives the exact free resolution
\[
 0\to R^2\to R^3\to R\to R/J\to0.
\]
All entries of (7), and of the generator map, lie in \(\mathfrak m\),
so this resolution is minimal. Hence the generator number is three
and the final free rank, equivalently the Artinian CM type, is two.

Since \(x\nmid h\), multiplication by \(x\) is injective on \(R/(h)\).
Cancellation modulo \(h\) gives \((J:x^v)=\mathfrak m\). Thus
\[
 0\to K\xrightarrow{1\mapsto x^v}R/J
 \to R/(h,x^v)\to0.
\]
The \(x\)-adic filtration of the last quotient has \(v\) successive
quotients \(R/(h,x)\), each of length \(n\), because \(x\) is regular
on \(R/(h)\). Its length is \(nv\), proving the formula.

For (3), work on \(a=1\), eliminate \(d=2bc-z^2\), and put
\(y=c-bz\). Direct substitution gives \(g=y^2-z^2f\). At the generic
point of \(D\), \(z\) is a unit; in the completed normal ring choose
\(x=g,y=c-bz\). Then \(f=z^{-2}(y^2-x)\), and
\[
 I_{u,v}R=(f^u,x^{v+1},x^v y).
\]
For \(u\ge2\), \(h=f^u\in\mathfrak m^2\) and
\(\operatorname{ord}_y h(0,y)=2u\). The lemma gives exact generic
type two and length \(1+2uv\). In particular the conjugate union is
not AG: its other branch is absent at this generic point, so attachment
at the two endpoints cannot repair the generic local algebra.

This also rules out any proposed supported basic double link whose
generic completed ideal has form (6), even when its containing section
is not a power of \(f\). It does not classify arbitrary supported
ideals, different multiplier ideals, or finite chains of operations.

For \(u=1\), the image ideal instead contains the nonzero quartic
\[
 N(f)=f\sigma(f)=b^4-a^2(2bc-ad).
\]
A CI image with support \(C\) would then have a defining degree at most
four, contradicting the factor-reduction consequence of
[STCI-R-0001](../results/quartic_carrier_exclusion.md).
Thus every positive-\((u,v)\) source (3) fails to yield a CI image or
AG conjugate union. Exchanging \(a,d\), \(b,c\), and \(f,g\) gives the
same conclusion. The generic type-two lemma is characteristic free;
the quartic exclusion used here is characteristic zero.

## 5. Descended factored sextics exclude every quadratic multiplier

**Low-degree equation lemma.** A scheme supported on \(C\) whose
homogeneous ideal contains a nonzero sextic all of whose irreducible
factors have degree at most four is not a complete intersection.

**Proof.** Suppose its CI degrees are \(5\le\alpha\le\beta\), using
[STCI-R-0001 and factor reduction](../results/quartic_carrier_exclusion.md#consequences-and-boundaries).
Every irreducible factor of either defining equation has degree at
least five, and Bézout gives \(4\mid\alpha\beta\). If \(\alpha\ge7\),
the ideal has no sextic. If \(\alpha=5\), divisibility forces
\(\beta\ge8\), and every sextic is a linear multiple of the first
generator, contrary to its factor degrees. If \(\alpha=6<\beta\),
the sextic is a scalar multiple of the first generator, with the same
contradiction. If \(\alpha=\beta=6\), a constant invertible change
of basis makes the sextic a defining generator, again contradicting
factor reduction. These exhaust the possibilities.

Now let \(I\subset E\) be homogeneous, with reduced scheme image \(C\),
and suppose \(GP\subset I\) for some nonzero \(G\in E_2\).
The invariant quadric \(q=bc-ad\) lies in \(P\cap S\). Hence
\[
 qN(G)=qG\sigma(G)\in I\cap S.
 \tag{8}
\]
This is nonzero because \(E\) is a domain, and is a sextic whose
irreducible factors have degree at most four: \(q\in S_2\) and
\(N(G)\in S_4\). The low-degree equation lemma excludes a CI image.
The conclusion persists after saturation and requires neither ACM,
Gorensteinness nor purity of \(E/I\).

In particular every supported basic double link \((F)+GP\) with a
quadratic multiplier fails, for every choice and degree of its
containing section \(F\). This statement does not treat a higher-degree
multiplier \(g^v\) as quadratic when \(v>1\); the generic lemma above
handles that power family separately. Formula (8) identifies the actual
descended equation that makes the restriction uniform.

## 6. Liaison addition gives an actual supported ACM source

The preceding power construction is not the only support-compatible
liaison input. For the smooth arithmetically Gorenstein threefold Q3,
let I_1,I_2 be saturated ideals of locally Cohen–Macaulay codimension-two
curves, and choose a regular pair F_i∈I_i of degrees d_i. Liaison addition
is the actual homogeneous ideal
\[
J=F_2I_1+F_1I_2.
\]
[Hartshorne–Migliore–Nagel, Definition 2.1 and Lemma 2.2](https://academicweb.nd.edu/~jmiglior/HMN.pdf)
give its saturation and the exact ideal sequence
\[
0\longrightarrow E(-d_1-d_2)
\xrightarrow{h\mapsto(F_1h,-F_2h)}
I_1(-d_2)\oplus I_2(-d_1)
\xrightarrow{(u,v)\mapsto F_2u+F_1v}J\longrightarrow0.
\tag{9}
\]
The kernel description also follows directly by cancellation of the
regular pair. At the level of support,
\(V(J)=V(I_1)\cup V(I_2)\cup V(F_1,F_2)\): a prime containing J
contains an input ideal, or else contains both multipliers. Thus both
input curves and the regular-pair intersection remain in the output. On \(Q_3\), \(H^1\) and \(H^2\) of every twist of
\(\mathcal O_{Q_3}\) vanish; sheafifying
(9) therefore gives the shifted direct sum of Rao modules
\[
M_J=M_{I_1}(-d_2)\oplus M_{I_2}(-d_1).
\tag{10}
\]
Thus adding a curve with a nonzero Rao module retains that defect as a
direct summand. This particular operation does not turn a deficient input
into an ACM output, including the reduced union \(D\cup\sigma D\)
when it is used as an input. It does allow two ACM inputs to give an ACM output.
Neither assertion prescribes the new scheme's reduced support.

### An explicit support-compatible pair

Use the two rational normal curves D and sigma(D) separately. Both are
ACM on Q3. With the already defined quadrics f=b²-az and g=c²-dz, put
\[
I_1=P,\quad I_2=\sigma P,\qquad
F_1=f,\quad F_2=g^3-4d^4f.
\]
These are actual homogeneous forms, of degrees two and six. On sigma(D),
whose parametrization has z=-s²t², one has
\[
f=2s^6t^2,\qquad g=2s^2t^6,
\]
so g³=4d⁴f and F_2∈sigma(P). Also
\[
(f,F_2)=(f,g^3).
\]
The earlier regular sequence (f,g) has sole reduced support D; replacing
g by g³ preserves regularity and support. Thus the liaison ideal
\[
\boxed{J=(g^3-4d^4f)P+f\,\sigma P}
\tag{11}
\]
is saturated and defines an actual ACM curve. Its support is exactly
D∪sigma(D). Indeed J is contained in both P and sigma(P). If a prime
containing J contained neither input ideal, it would contain F_2 and f,
hence rad(f,g³)=P, a contradiction. There are no other curve components.
Its ACMness follows either from (10), or from (9) and the depth lemma:
P and sigma(P) have depth three over the four-dimensional CM ring E,
so J has depth at least three and E/J is CM of dimension two.

This construction establishes the simultaneous feasibility of actual
support and ACMness **upstairs**. It does not assert that the two full
primary structures are conjugates of one another, or that the contracted
coordinate image in P3 is ACM, AG, or a complete intersection.

### Its invariant quartic survives primary extraction and conjugation

The first multiplier produces an immediate stronger-property gate:
\[
N(f)=f\sigma(f)\in f\sigma P\subset J.
\]
This is the same nonzero invariant quartic displayed in §4. Every
D-primary extraction Q_D of J contains J. Since sigma(N(f))=N(f), the
conjugate ideal sigma(Q_D) contains it as well. Consequently
\[
N(f)\in Q_D\cap\sigma(Q_D),
\]
and the coordinate image of that conjugate union has this quartic in its
homogeneous ideal. If the image were a supported CI, it would contradict
[R-0001 and its factor reduction](../results/quartic_carrier_exclusion.md).
The same argument applies to every addition of this pattern retaining
F_1=f, whatever admissible second form F_2 is used.

This excludes the displayed source as a direct supported CI construction
in characteristic zero. The quartic equation alone does **not** rule out
an ACM coordinate image with more than two defining generators. Nor is
this a theorem about arbitrary liaison additions, other multipliers,
chains of links, or all supported ACM thickenings.

### What Rao and N-type theorems do and do not construct

For curves on the smooth quadric threefold, the applicable Rao statement
concerns the **even Gorenstein liaison class**, up to twist. It does not
identify that class with a fixed-support locus or a CI-biliaison class.
[Hartshorne–Migliore–Nagel, §5, Example 5.5](https://academicweb.nd.edu/~jmiglior/HMN.pdf)
exhibits different CI-biliaison data with the same Rao module: a maximal
Cohen–Macaulay module and its compatible surjection remain part of the
presentation. Thus the direct-sum obstruction (10) is a statement about
this operation, and the Rao class is not a substitute for its equations,
conjugation, or ambient restriction maps.

[Casanellas–Drozd–Hartshorne, Proposition 3.4](https://arxiv.org/pdf/math/0307378)
starts with an N-type resolution on a normal AG ambient scheme and a
sequence
\[
0\to\mathcal E\to\mathcal N\to\mathcal N'\to0,
\]
where E is an **orientable rank-two ACM subsheaf** and N' is locally
Cohen–Macaulay of rank at least two. It uses sufficiently general sections
to obtain a scheme in the same even G-liaison class with a resolution
using N'. The output resolution is N-type only with the additional
condition \(H^1_*(\mathcal N'^{\vee})=0\). The theorem does not select the support D,
the conjugate partner, or the equation maps needed here. Its use as a
construction mechanism requires those actual hypotheses and choices;
removing a formal ACM summand or quoting a Rao class supplies none of them.

## 7. A height-two residual pattern already contains the support problem

[Batavia–Pandey–Walther, Theorems 5.1–5.2 and §2.4](https://arxiv.org/pdf/2610.25680v1)
construct residual intersections that are STCI in any characteristic.
Theorem 5.1 starts with a regular sequence of length n>1 in a Gorenstein
local ring and constructs s-residual intersections for s≥n in a polynomial
extension. Theorem 5.2 uses a generic height-three Gorenstein Pfaffian
ideal and a specialization preserving that input height, with s≥3.
These are existence theorems for their residual sources, not a conclusion
that every specialization has a prescribed irreducible projective support.

For a height-two output of the explicit Theorem 5.1 pattern, take s=n=2.
Writing the input as (u,v), its matrix and output ideal are
\[
X'=\begin{pmatrix}x&\lambda\\\lambda&0\end{pmatrix},
\qquad J=(xu+\lambda v,\lambda u,\lambda^2).
\]
Here the two linear combinations are X'(u,v)^t and the determinant adds
-lambda². In every ring, and after every substitution,
\[
\boxed{\sqrt J=\sqrt{(\lambda,xu)}}.
\tag{12}
\]
Indeed J⊂(lambda,xu), while lambda²∈J puts lambda in rad J and the
first generator then puts xu in rad J. This proves both radical
inclusions without a colon calculation or a genericity assertion.
Geometrically,
\[
V(\lambda,xu)=V(\lambda,x)\cup V(\lambda,u).
\tag{13}
\]

If lambda,x,u are nonzero positive-degree homogeneous forms in the
coordinate ring of P3 over an algebraically closed field, each branch of
(13) is nonempty and has dimension at least one. If their union has
support exactly the irreducible C0, each branch is a closed subset of C0
of dimension at least one, hence both already have support C0. Producing
such a specialization therefore already produces supported two-equation
pairs (lambda,x) and (lambda,u). The operation may change their transverse
scheme structures; it cannot remove an unwanted component of either
branch. This is an explicit support control, not a contradiction to the
positive residual-intersection theorem.

A nonzero linear lambda cannot contain the nondegenerate C0. Using
higher-degree entries requires actual homogeneous forms, including
\[
\deg x+\deg u=\deg\lambda+\deg v,
\]
and separate verification of their support. The universal radical
identity survives arbitrary substitution; the colon equality, height,
regularity and residual-intersection hypotheses of the source theorem
do not follow from it. The branch argument just given uses positive
degrees and nonzero entries; it is not an assertion about a substitution
with a unit or zero entry outside those hypotheses.

The source's regular homogeneous specializations preserve height because
the specializing sequence is regular on both the ambient ring and its
quotient: both dimensions fall by the same length. Accordingly the
height-three theorem, whose residual height is s≥3, does not produce a
codimension-two curve by such a specialization. An additional height-drop
map would require its own actual support and two-equation proof. This
leaves other residual constructions open.


## Classical residual operations on the skew-line link

This separate literature test concerns
[Hassanzadeh, Theorems 3.7, 3.16, Corollary 3.19 and Theorem 4.2](https://arxiv.org/html/2409.05705v2).
Return to characteristic zero and write
\[
q=ad-bc,\quad A_3=b^3-a^2c,\quad B_3=b^2d-ac^2,\quad C_3=bd^2-c^3,
\quad P=I_{C_0}=(q,A_3,B_3,C_3).
\]
Let \(I_D=(ac,ad,bc,bd)=(a,b)\cap(c,d)\) and
\(\mathfrak a=(q,B_3)\). These are two skew ruling lines on Q and
their actual link to C0:
\[
\mathfrak a:I_D=P,\qquad
(q,B_3)=(ac,ad,bc,bd)
\begin{pmatrix}0&-c\\1&0\\-1&0\\0&b\end{pmatrix}.                    \tag{14}
\]
In Segre coordinates \(a=xu,b=xv,c=yu,d=yv\), the cubic restricts to
\(xy(xv^3-yu^3)\): its divisor is the two lines plus C0 of class (1,3).
This proves the residual support and multiplicities in (14).

The actual outputs of the proposed operations are:

| Operation | Output | Failure |
| --- | --- | --- |
| Boundary determinant ideal | \(\mathfrak a+I_4(\Phi)=\mathfrak a\) | Retains both residual lines |
| Zeroth Fitting ideal of \(I_D/\mathfrak a\) | \(P\cap\mathfrak m^3\) | Adds only an embedded cone-vertex defect |
| Full Koszul–Fitting ideal | \(P\) | Returns the original non-ACM quartic |

The first row is Hassanzadeh's Theorem 4.2; the 4-by-2 matrix has no
4-by-4 minors. The last row follows from
[Bouça–Hassanzadeh, Proposition 5.9](https://arxiv.org/pdf/1810.05134)
with s=g=2. That equality does not assert that the quotient is CM.

For the middle row an exact presentation after eliminating bc is
\[
M=\begin{pmatrix}
d&b&0&0&-c\\
-c&-a&b&d&0\\
0&0&-a&-c&b
\end{pmatrix}.
\]
Its maximal minors, in column orders
123,124,125,134,135,145,234,235,245,345, are respectively
\[
aq,\ cq,\ -bq,\ dq,\ B_3,\ C_3,\ bq,\ A_3,\ B_3,\ -cq.
\]
They generate \((aq,bq,cq,dq,A_3,B_3,C_3)=P\cap\mathfrak m^3\).
The nonzero class of q is killed by \(\mathfrak m\), so this quotient
has depth zero; saturation recovers P. Its projective scheme is still
the reduced quartic, not a newly constructed thickening.

The theorem hypotheses fail for a visible reason. In the Koszul complex
on \((ac,ad,bc,bd)\), the cycle
\(\eta=bd\,e_1-bc\,e_2\) is a nonzero class in H1. In multidegree abcd,
the only boundary directions are \(\partial e_{14}\) and
\(\partial e_{23}\); their unavoidable e4 and e3 terms prevent a
boundary representation. With \(k_{ij}=\partial(e_i\wedge e_j)\),
\[
a\eta=-b k_{12},\quad
b\eta=-b k_{14}+b k_{23}+a k_{34},\quad
c\eta=-d k_{13}+c k_{23},\quad
d\eta=-d k_{14}+c k_{24}.
\]
Hence H1 has depth zero instead of the required sliding depth at least
one. At \(\mathfrak m\), \(Z_1\) has depth at least two; the sequence
\(0\to B_1\to Z_1\to H_1\to0\) forces depth \(B_1=1\).
Then \(0\to Z_2\to K_2\to B_1\to0\) gives depth \(Z_2=2\) and
projective dimension \(Z_2=2\), exceeding Theorem 3.16's bound one.
Thus the broader cycle hypothesis also fails. Theorem 3.7's s≥r
hypothesis already fails because 2<4.

Varying a proper linking pair while keeping this fixed skew-line source
does not change its failed depth conditions; ordinary direct CI linkage
also preserves ACM status. This is a source limitation, not an exclusion
of all residual constructions.


The exact skew-line source operations and their theorem-applicability limits were independently reconstructed. These are bounded source failures, not a classification of residual constructions. The [projected-thickening section obstruction](projected_thickening_section_defects.md) is a different failure of the actual downstairs homogeneous section ring.

<a id="6-what-these-mechanisms-leave-open"></a>

## 8. What has been realized, and which stronger properties fail

The basic-double-link power family and the explicit liaison addition
construct actual supported ACM schemes on Q3. Their operation formulas,
regular pairs and saturation arguments make the input realizable, rather
than an abstract module with desired numerical invariants. The
[projected-source calculation](projected_thickening_section_defects.md)
separately tests whether its specified actual upstairs sources remain ACM
downstairs; ACMness is not automatic under this projection.

Different failures here test different stronger requirements. The generic
type-two lemma prevents AG conjugate unions for its containing-section
pattern. The invariant quartic and factored sextic prevent supported CI
images in characteristic zero. Those low-degree equations do not by
themselves exclude an ACM image with additional generators. The BPW
height-two specialization retains both input branches, and the skew-line
residual operations retain their particular equations or depth defects.
None of these source-specific conclusions covers all liaison additions,
higher multipliers, finite chains, or all supported structures.

The canonical-boundary/Rao formula is one condition in two descriptions;
its conductor multiplication is owned by the
[quadratic-cover account](quadratic_covers_and_conductor_descent.md).
For that covering construction an AG conjugate union supplies a CI image,
but obtaining an actual supported ACM image is a distinct intermediate
problem. Module ranks, liaison-class membership and sheaf existence do
not select the embedded multiplication, compatible surjections, projection
sections or conjugate gluing required by either target. Genus from support
alone supplies no missing bound.

Thus the concrete outcomes are supported ACM sources and exact failure
mechanisms for the displayed attempts to achieve stronger descent. Other
actual sources and operations remain available for construction; an
unrestricted obstruction would need an additional theorem covering them.
No residual positivity or incompatible conductor capacity is asserted.

## Characteristic reach and independent review

The uniform local type-two lemma and BPW radical identity are
characteristic-free. The explicit two-branch Q3 liaison construction uses
a separated involution and the displayed equations in characteristic zero;
the same regular-pair and support calculation works when 2 is invertible.
Its forbidden-quartic conclusion uses the characteristic-zero carrier
exclusion and does not extend to positive characteristic, where a
[quartic carrier has a supported mate](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier).
The quoted liaison and N-type operations retain their ambient, field,
regularity and cohomology hypotheses; no arbitrary-characteristic extension
is inferred from their module notation.

Inherited independent reconstruction covers §§1–5 and the classical
skew-line operations at their stated scopes. The new liaison-addition and
BPW transfer reuses the independently reviewed frozen source, including
the corrected CDH hypotheses and explicit supported input. Independent integration and preservation review accepted the actual
liaison source, exact support and Rao sequence, invariant-quartic gate,
corrected CDH hypotheses, BPW radical/height scope, and preservation of the
existing proofs, with no unresolved material finding. Primary inspection checked HMN Definition2.1/Lemma2.2/Example5.5,
CDH Proposition3.4 and BPW Theorems5.1–5.2 for the exact applications above.
No new CAS execution or general operation classification is claimed.
