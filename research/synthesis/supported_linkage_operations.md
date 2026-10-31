# Supported linkage operations and their generic and descended equations

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
The deductions below are provisional, not a canonical STCI result.
The unrestricted characteristic-zero question remains open.

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
Global ACM compatibility has genuinely been achieved for this source.

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

## 6. What these mechanisms leave open

Actual supported ACM thickenings on the upstairs quadric threefold have been constructed, and their whole
positive-power source is excluded as a direct CI construction. The
local lemma also excludes all higher-order containing sections with the
specified generic basic-double-link ideal, and the norm argument
excludes every quadratic multiplier independently of its containing
section. These are bounded operation theorems, without an exhaustion
of supported thickenings, higher multipliers, or finite chains.

The canonical boundary/Rao comparison supplies one condition viewed in
two ways. Neither genus from support alone nor a repeated numerical
liaison comparison supplies the missing upper boundary budget. An
obstruction would need a genuinely independent comparison applying to
arbitrary pairs; an existence construction would need a different
operation retaining generic Gorenstein algebra and actual global
sections and conjugate attachment. Both remain live mathematical
possibilities. No stated vanishing, ACM property, liaison-class
membership or local compatibility proves STCI.

## Independent review and scope

Independent reconstruction checked the actual supported ACM source, Rao-boundary dependence, generic and descended-equation gates, and the stronger arbitrary-h local lemma via its minimal Hilbert-Burch resolution and regular-element length filtration. The scope is a bounded operation class, not an exhaustion of supported thickenings, higher multiplier ideals, or linkage chains.

The inherited mathematical inputs retain the scope and review evidence of their linked owners. No inherited CAS campaign was broadly rerun, and the unrestricted characteristic-zero STCI question remains open.

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
\begin{pmatrix}0&-c\\1&0\\-1&0\\0&b\end{pmatrix}.                    \tag{7}
\]
In Segre coordinates \(a=xu,b=xv,c=yu,d=yv\), the cubic restricts to
\(xy(xv^3-yu^3)\): its divisor is the two lines plus C0 of class (1,3).
This proves the residual support and multiplicities in (7).

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
