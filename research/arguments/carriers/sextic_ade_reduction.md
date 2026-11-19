# ADE sextic pencils and quintic normal-carrier reductions

<a id="sextic-pairs-with-an-ade-pencil-carrier"></a>

## Sextic pairs with an ADE pencil carrier

**Independently reviewed reduction.** Fix \(C_0=[s^4:s^3t:st^3:t^4]\) in characteristic zero.
If a proper supported sextic pair has a general normal pencil carrier
with only rational double points, its canonical filtration satisfies
\[
 \boxed{L=\mathcal O_{\mathbf P^1}(-6),\qquad D_2=0.}
\]
Its saturated triple is therefore an embedded primitive triple of type
\(\mathcal O(-6)\). This leaves a restricted case; it does not imply
that every normal pencil carrier is ADE or exclude every sextic pair.

The [all-pair sextic reduction](sextic_pair_reduction.md) owns the normal
pencil, smoothness off the curve and saturated divisor profile. Retain
\(L=\mathcal O(-l)\), \(l\in\{5,6,7\}\), \(D_8=2T\), and
\(\deg T=4l-17\). The full first-symbol divisor of a general member
\(S\) has degree \(l+10\). Its mate cuts \(9C_0\), so local Cartier
indices divide nine. All singularities of \(S\) lie on \(C_0\).

## Marked local models and exact defects

The smooth marked rational-double-point classification in
[Jaffe, Theorem 4.1 and Propositions 5.2–5.3](https://arxiv.org/pdf/alg-geom/9410008)
lists \(A_{r-1}^{c}\), the two marked \(D\) families, \(E_{6,1}\)
and \(E_{7,1}\). The \(D\) and \(E_7\) indices are two or four,
which cannot divide nine. There is no smooth marked \(E_8\) case.
A smooth Cartier curve cannot pass through a singular hypersurface point:
quotienting an embedding-dimension-three surface ring by one equation
leaves embedding dimension at least two.

For \(A_{r-1}^{c}\), the first-symbol order is \(c\), with
\(1\le c\le r/2\), and the actual index is \(r/\gcd(r,c)\).
Use coordinates
\[
 S:(UV+t^r=0),\qquad C_0:(U,V)=(-t^{r-c},t^c).
\]
Since \(9C_0\) is Cartier, \(k=9c/r\) is an integer in
\(\{1,2,3,4\}\). The exact local divisor coefficients are
\[
 D_8=(k-1)c,\qquad T=\frac{(k-1)c}{2},\qquad
 D_2=\max\{0,3c-r\}.                                  \tag{1}
\]

For the socle formula, put \(v=V-t^c\) and let \(D\) be the axis
prime \((V,t)\). Then \(\operatorname{div}(v)=C_0+cD\) and
\(\operatorname{div}(V)=rD\). The rational function \(h=v^9/V^k\)
has divisor \(9C_0\), and is regular by normality. An actual local mate
differs from it by a unit. The reviewed
[local Jacobian/socle identity](normal_index_socle_and_torsion.md) gives
\[
 c+D_8=\operatorname{ord}_t((v^9/h)|_{C_0})
      =\operatorname{ord}_t(V^k|_{C_0})=kc.
\]
For the second defect, put \(u=U+t^{r-c}\). The carrier equation is
\(uv+t^cu-t^{r-c}v=0\), and its saturated first direction is
\(m=u-t^{r-2c}v\). Generically,
\[
 m=-t^{r-3c}v^2+O(v^3).
\]
The [actual-pole identification](sextic_pair_reduction.md#the-constant-direction-triple-and-its-actual-defects)
is local and does not require a constant global direction. It identifies
the second defect with the pole order of this quadratic coefficient,
proving (1).

The remaining non-\(A\) type \(E_{6,1}\) has first-symbol order two
and index three, with model
\[
 x^2-2xt^2-y^3=0,\qquad C_0:(x,y)=0.
\]
Here \(x\) cuts \(3C_0\), giving a primitive triple on the smooth
surface \(x=0\). Its primitive-index defect is zero. The local
power-socle formula gives \(D_8=4,T=2\), and its saturated triple has
\(D_2=0\).

The complete local numerical list is:

| Type | Parameters | First-symbol order | \(T\) | \(D_2\) | Root rank \(\rho\) |
|---|---|---:|---:|---:|---:|
| \(A\), \(k=1\) | \(r=9c\) | \(c\) | 0 | 0 | \(9c-1\) |
| \(A\), \(k=2\) | \(c=2h,r=9h\) | \(2h\) | \(h\) | 0 | \(9h-1\) |
| \(A\), \(k=3\) | \(r=3c\) | \(c\) | \(c\) | 0 | \(3c-1\) |
| \(A\), \(k=4\) | \(c=4h,r=9h\) | \(4h\) | \(6h\) | \(3h\) | \(9h-1\) |
| \(E_{6,1}\) | — | 2 | 2 | 0 | 6 |

All parameters are positive integers. The first row has no defect, hence
is locally primitive. For a general pencil member its singularities in
that locus are simple moving zeros, so \(c=1\). The inequalities below
also hold for every listed \(c\), without this refinement.

## The rank budget and the surviving row

An ADE sextic resolution has \(h^{1,1}=86\). Its negative-definite
exceptional root lattices are independent of the positive-square hyperplane
class, giving total root rank at most 85. This is also Jaffe's Lemma 11.3
specialized to degree six. No such bound is asserted here for arbitrary
normal singularities or in positive characteristic.

Every local row satisfies \(8c-\rho\le8T\). Summing over all
singularities, including moving ones, yields
\[
 \rho_{\rm total}\ge8(l+10)-8(4l-17)=216-24l.          \tag{2}
\]
For \(l=5\), this is 96, exceeding 85 and excluding the row.

For \(l=6\), a positive \(D_2\) requires a \(k=4\) point. The
budget \(\deg T=7\) permits only one, with \(h=1\). It consumes
first-symbol order four and \(T=6\), and contributes rank eight. The
other points have total first-symbol order twelve and \(T=1\), hence
rank at least 88 by the local inequality. Total rank would be at least
96, so \(D_2=0\).

For \(l=7\), the global triple obstruction requires \(D_2>0\).
The budget \(\deg T=11\) permits exactly one positive-second-defect
point, necessarily \(k=4,h=1\). Thus \(D_2=3[P]\). The reviewed
global actual-pole restrictions exclude this: axis directions have no
actual degree-three defect, and mixed directions require three distinct
points. This excludes the last row.

Only \(l=6,D_2=0\) remains. Its saturated triple has local basis
\(1,v,v^2\) with \(v^3=0\), so is primitive even at nonprimitive
points of the length-nine structure.

Independent reconstruction accepted the marked classification coverage,
actual-index restrictions, both defect formulas, the \(E_6\) contribution,
rank budget and all three row dispositions. Existing surface and triple
results were reused within their established scopes. The proof uses exact
formulas and inequalities rather than a finite search. The
\(\mathcal O(-6)\) primitive-triple case and non-ADE carriers remain open.

## Three remaining primitive-triple orbits

The surviving primitive triples have an existing complete classification.
The independently audited
[primitive-direction calculation](../normal-geometry/mf6_and_nonnormal_structures.md#independent-audit-and-all-degree-exclusion-of-primitive-e1-quartic-triples),
subsection “Every basepoint-free primitive triple direction,” uses only
the embedded curve, \(L=\mathcal O(-6)\), \(M=\mathcal O(-8)\),
and its quadratic transition class. Its four actual ambient torus orbits
are represented by
\[
 (A,B)=(1+z,-2-8z),\qquad
 (A,B)=(rz,1),\quad (2r+1)(12r^2+4r+3)=0.
\]
Here \(A,B\) describe the conormal quotient in the source's balanced
frame. The triple in each fixed direction is unique, since
\(H^0(\operatorname{Hom}(M,L^2))=H^0(\mathcal O(-4))=0\).
The classification has no quartic-ancestor hypothesis. The source's later
degree-four carrier exclusions do not transfer automatically to sextics.

The \(r=-1/2\) orbit is excluded for sextics directly. In the actual chart
\[
 x_0=1,\quad x_1=z,\quad x_2=z^3+V,\quad
 x_3=z^4+U+\tfrac32zV,
\]
the containing quadric is \(q=U+zV/2\). For
\((A,B)=(-z/2,1)\), the kernel direction \(BU-AV\) is exactly
\(q\). Its quadratic cocycle has the identically zero factor
\(2A+zB\), so the unique primitive correction is zero. The triple is
precisely the Cartier divisor \(3C_0\) on \(Q\).

A sextic containing it restricts to a section of
\[
 \mathcal O_Q(6,6)(-3C_0)=\mathcal O_Q(3,-3),
\]
which has no nonzero sections. Both sextics would therefore be divisible
by \(q\), contradicting properness. Only the principal orbit and the
two roots of \(12r^2+4r+3=0\) remain.

Independent reuse review checked the classification's complete curve-only
scope, the actual torus action, frame convention, unique triple, and
quadric restriction. These three orbits classify the remaining triples.
The next sections compute their full degree-six equation spaces and test
successive contact conditions.

## Full sextic spaces and the first further contact equation

The [intrinsic source proof](sextic_triple_intrinsic_contact.md) uses
the quadric flag, interpolation and the accepted triple substitution
\[
 U=Ay-T_0\gamma y^2,\qquad V=By+S_0\gamma y^2,
 \qquad AS_0+BT_0=1.
\]
For the principal orbit,
\((S_0,T_0,\gamma)=(4/3,1/6,96+192z)\); for the algebraic
orbits, \((S_0,T_0,\gamma)=(0,1,0)\).
Vanishing of every coefficient of \(y^0,y^1,y^2\) is exactly
containment of the triple. Its purity makes the dense affine calculation
sufficient for a global section: no nonzero image section can be supported
only at infinity.

It establishes the source dimensions, first-normal image and joint ranks
without monomial-source rank calculations. The quartic-multiple span and
unrestricted \(\Theta\) ranks remain retained computational diagnostics
from the [original exact source audit](https://github.com/markluxton1/STCI/blob/9deae1cc7f4b008fb287d13bdb2776faa1e75bf5/research/computations/audit_sextic_triple_spaces_2026_10_31.py).

| Exact quantity in characteristic zero | Principal orbit | Either algebraic orbit |
| --- | ---: | ---: |
| Dimension of containing quartics | 2 | 2 |
| Dimension of containing quintics | 11 | 11 |
| Dimension of containing sextics | 27 | 27 |
| Span of quartic-source multiples by quadrics | 20 | 20 |
| Additional sextic directions modulo that span | 7 | 7 |
| Rank of the first-normal map \(h\) | 17 | 17 |
| Rank of the cubic-contact map \(\Theta\) | 18 | 12 |
| Rank of the joint map \((h,\Theta)\) | 23 | 24 |

To define the last maps, use the linear coordinates
\(U=T_0m+Ay,\ V=-S_0m+By\). The relevant terms of a containing
sextic are
\[
 F=h_Fm+\gamma h_Fy^2+E_Fmy+K_Fy^3+\cdots,
 \qquad \Theta_F=\gamma E_F-K_F.
\]
The omitted terms do not affect the cubic coefficient after eliminating
\(m\), whose order along the triple is two. With
\(q'=m+\gamma y^2\), the expansion begins
\(F=h_Fq'-\Theta_Fy^3+\cdots\). If \(h_F\ne0\) generically,
eliminating \(q'\) from \(F,G\) leaves cubic coefficient
\[
 \frac{h_G\Theta_F-h_F\Theta_G}{h_F}.
\]
Thus a generically curvilinear supported sextic pair necessarily satisfies
\[
 \boxed{h_G\Theta_F-h_F\Theta_G\equiv0.}
\]
Otherwise its generic transverse length is three, instead of nine.
At least one first-normal coefficient is nonzero in the length-nine
curvilinear setting. The next coefficients through order eight must also
vanish.

The script uses exact rational arithmetic and
\(\mathbb Q(\sqrt{-2})\). Conjugation transports the complete algebraic
source and contact matrices to the other root, preserving the ranks.
An independent review reconstructed the substitution, global-source
coverage and contact sign, ran the exact calculation, and added a direct
rank-and-containment check for all twenty quartic-times-quadric products.
Run `PYTHONDONTWRITEBYTECODE=1 python3 research/computations/audit_sextic_triple_spaces_2026_10_31.py`.
These record the original linear checks. The source dimensions,
restricted images and determinant span below now have a separate
geometric proof; none excludes the remaining sextic pairs.

### Geometry of the cubic-contact incidence

Fix one of the three surviving embedded primitive triples
\(T_3\subset\mathbf P^3\), supported on \(C\), and let
\[
V=H^0(\mathbf P^3,\mathcal I_{T_3}(6)),\qquad \dim V=27.
\]
A pencil is a point of \(\operatorname{Gr}(2,V)\). Its members already
contain \(T_3\); the next condition asks whether their common
intersection has transverse contact beyond this prescribed triple.

At the generic point of \(C\), use a first normal equation \(q'\) and
a transverse parameter \(y\) so that a member of the linear system has
the form
\[
 F=h_Fq'-\Theta_Fy^3+\text{higher terms}.
\]
The first coefficient \(h_F\) is the *first-normal symbol* of the
carrier. The second, \(\Theta_F\), is its first residual contact
coefficient. Their values depend on the chosen frame, but the vanishing
of the determinant below is intrinsic: it expresses proportionality
of the two leading relations in the successive normal-jet quotient.

For a pencil \(\langle F,G\rangle\), the first residual obstruction is
\[
 \Omega_3(F\wedge G)=h_G\Theta_F-h_F\Theta_G.
\]
It is a section-valued Plücker equation, rather than an arbitrary
condition on the 351-dimensional vector space \(\bigwedge^2V\).
Its vanishing is necessary for the two surfaces to meet with contact
beyond the primitive triple when at least one first-normal symbol is
nonzero. The full length-nine condition requires further jet
compatibility through order eight.

#### The geometric kernel and its pencils

The first-normal symbol defines a map from the linear system to the
space of normal symbols. Its kernel consists of sextics that vanish to
second order along \(C\) *and* contain the chosen triple:
\[
 \ker h=V\cap H^0(\mathcal I_C^2(6)),\qquad \dim\ker h=10.
\]
Inside it lies the linear system
\[
 K=\ker(h,\Theta),
\]
whose members have both leading normal-jet coefficients zero.
The [intrinsic restricted-image proof](sextic_triple_intrinsic_contact.md#the-restricted-cubic-contact-image)
gives
\[
 \dim K=
 \begin{cases}
 4&\text{principal orbit},\\
 3&\text{either algebraic orbit}.
 \end{cases}
\]
Equivalently, the first residual contact coefficient on the
second-order subsystem has ranks six and seven, respectively. These
are geometric filtration dimensions, now proved by sparse quartic
interpolation and the quadric restriction flag.

Every pencil containing a nonzero member of \(K\) automatically
satisfies the cubic-contact equation: for \(G\in K\),
\(\Omega_3(F\wedge G)=0\) for every \(F\in V\).
Thus the cubic-contact locus contains the incidence of lines in
\(\mathbf P(V)\) meeting \(\mathbf P(K)\). This exhibits
*decomposable* solutions directly, without inferring them from the
rank of the map on the full exterior square.

#### No fixed surface and proper pencils

**Proposition.** For each surviving triple \(T_3\), the cubic-contact
incidence contains a pencil \(\langle F,G\rangle\) with
\[
 \gcd(F,G)=1,\qquad h_F\ne0.
\]
This is a proper intersection of two sextic surfaces, but its
intersection need not have sole support \(C\) or generic length nine.

**Proof.** We first show that the complete linear system
\(\mathbf P(V)\) has no fixed surface component. Let
\(q=x_0x_3-x_1x_2\) be the equation of the unique quadric \(Q\)
containing \(C\). Since \(q\in\mathcal I_C\), its cube vanishes on
every triple supported on \(C\), and \(q^3\in V\). Any fixed
irreducible surface component must therefore be \(Q\).

But \(Q\) does not contain any of the surviving triples as a
subscheme. Its generic first-normal direction is transverse to
their primitive direction. In the above frame, the first coefficient
of \(q\) is \(A+\frac z2B\), which is
\(1-4z^2\) in the principal orbit and
\((r+\frac12)z\) in an algebraic orbit; neither is identically
zero. (The excluded direction \(r=-1/2\) is the quadric triple.)

This transversality gives a useful restriction: if \(qH\) contains
\(T_3\) for a quartic \(H\), then \(H\) must vanish on \(C\).
Indeed, over \(k(C)\) the class of \(q\) in
\(k(C)[y]/(y^3)\) is a unit times \(y\), and
\(qH=0\) there forces the constant coefficient of \(H\) to vanish.
Consequently, if \(Q\) were fixed in \(\mathbf P(V)\), division by
\(q\) would inject \(V\) into \(H^0(\mathcal I_C(4))\).
But
\[
 h^0(\mathcal I_C(4))
 =h^0(\mathcal O_{\mathbf P^3}(4))-h^0(\mathcal O_C(4))
 =35-17=18<27=\dim V,
\]
using surjectivity of quartic restrictions: sums of four weights from
\(\{0,1,3,4\}\) cover every integer from \(0\) through \(16\).
No projective-normality assertion is needed.
Hence \(\mathbf P(V)\) has no fixed surface component.

Take any nonzero \(G\in K\). The divisors in \(\mathbf P(V)\)
sharing a component with \(V(G)\) form a finite union of proper
linear subsystems: one for each irreducible component of \(V(G)\).
The subsystem with zero first-normal symbol is also proper because
\(h\ne0\). Their complement is a nonempty Zariski-open subset of
\(\mathbf P(V)\). Choose \(F\) there. Then \(F,G\) have no common
surface component, \(h_F\ne0\), and their pencil satisfies
\(\Omega_3(F\wedge G)=0\). \(\square\)

#### The intrinsic determinant image

For all three triples, the
[generator-bundle determinant proof](sextic_triple_intrinsic_contact.md#regularity-and-a-reusable-determinant-span-lemma)
establishes
\[
 \operatorname{rank}\Omega_3=23,\qquad
 \dim\ker\Omega_3=328,\qquad
 \operatorname{im}\Omega_3=k[z]_{\le22}.
\]
This is a check of the **span of cubic-contact obstructions**, not
a count of geometric pencils. The different ranks of the joint
normal-jet maps, \(23\) for the principal orbit and \(24\) for the
algebraic orbit, are distinct invariants. The historical algebraic
joint-rank value \(26\) is incorrect. The proof uses the actual
rank-two generator bundle, surjectivity of the first-normal image,
the restricted contact image and 5-regularity; it requires no
exterior-square rank calculation. It independently establishes the
principal rank too, replacing its former supplied-execution limitation.

The same proof gives the
[mixed-degree determinant image](sextic_triple_intrinsic_contact.md#all-higher-equation-degrees)
for every \(a,b\ge5\) with \(a+b\ge11\), onto
\(H^0(\mathcal O_{\mathbf P^1}(4(a+b)-26))\). In equal degree
\(d\ge6\) the rank is \(8d-25\); the
[equal-quintic corner](sextic_triple_intrinsic_contact.md#the-equal-quintic-corner)
remains outside this proof. These remain first contact conditions through a
specified triple, not the higher-order compatibility of an actual
supported pair.

The geometric incidence argument above settles the existence of
proper cubic-contact pencils without relying on surjectivity of
\(\Omega_3\). The next test can be solved uniformly for pencils with
a quadric-divisible member.

### Torus weight blocks of the primitive-triple sources

Fix characteristic zero and retain the actual substitutions and contact
sign above. For an algebraic orbit put \(\alpha=\sqrt{-2}\),
\(r=(-1+2\alpha)/6\). Its dense-chart substitution is
\[
 x_1=z,\quad x_2=z^3+y,\quad
 x_3=z^4+(r+\tfrac32)zy+m.
\]
It is homogeneous with uncentered weights \(1,3,4\) on \(z,y,m\);
purity extends invariance to the global triple. Conjugation gives the
other algebraic orbit. The
[intrinsic source formula and filtration](sextic_triple_intrinsic_contact.md#regularity-and-a-reusable-determinant-span-lemma)
give the following profiles, without complete-source kernel matrices:

| Degree | Centered weights | Multiplicities |
| ---: | --- | --- |
| 4 | \(-4,4\) | \(1,1\) |
| 5 | \(-6,-5,-3,-2,-1,0,1,2,3,5,6\) | all one |
| 6 | \(-8,\ldots,8\) | \(1,1,1,1,2,2,2,2,3,2,2,2,2,1,1,1,1\) |

The quartic basis can be written
\[
 Q_-=(1-\alpha)x_0^2q-x_1(x_0^2x_2-x_1^3),\qquad
 Q_+=(1+\alpha)x_3^2q-x_2(x_1x_3^2-x_2^3).
\]
Its weights are \(-4,4\). Direct substitution, using
\((1-\alpha)(r+1/2)=1\), sends \(Q_-\) to
\((1-\alpha)m\) exactly. For a sextic of weight \(w\),
homogeneity gives
\[
 h_F=c_Fz^{w+8},\qquad \Theta_F=d_Fz^{w+3},
\]
with negative exponents interpreted as zero. Since the first-normal
image is all \(H^0(\mathcal O(16))\), subtracting its character
from the sextic source gives the ten-dimensional \(\ker h\) profile
\((1,1,1,1,2,1,1,1,1)\) at weights \(-4,\ldots,4\).
Its restricted contact image is all \(H^0(\mathcal O(6))\), of
weights \(-3,\ldots,3\). Subtracting again gives one joint-kernel
line at each of \(-4,0,4\), including \(qQ_-\) and \(qQ_+\).

The old endpoint coefficient relation also has a small direct proof.
For the quartic \(Q_+\), substitution gives
\[
 h_{Q_+}=(\alpha-1)z^8,\qquad
 \Theta_{Q_+}=\frac{4(\alpha-5)}{27}z^3.
\]
Thus their ratio is \(\lambda z^{-5}\), with
\(\lambda=(28+16\alpha)/81\). Multiplication by any ambient
form scales both coefficients by its restriction to \(C\), since
\(\gamma=0\) and \(Q_+\) has no pure terms of orders one or two.
For every weight \(4\le w\le8\), the degree-six source is exactly
the corresponding quadratic-multiple space of \(Q_+\): their
weight dimensions agree with the displayed profile (at weight four
both are two-dimensional). Consequently
\[
 [\Theta_F]_d=\lambda[h_F]_{d+5}\qquad(7\le d\le11).
\]
This proves the relation on the full source through a single quartic
identity and multiplication, replacing the old columnwise comparison.

The algebraic exterior-square source has weights \(-15,\ldots,15\).
Its weight-\(W\) determinant has output proportional to
\(z^{W+11}\). The intrinsic surjectivity onto
\(H^0(\mathcal O(22))\) therefore gives rank one in every block
\(-11\le W\le11\), and zero outside. This follows from the
equivariant determinant map and its proved image, without individually
checking 23 blocks. In the principal orbit the corresponding
[restricted image](sextic_triple_intrinsic_contact.md#the-restricted-cubic-contact-image)
is instead \(\{p\in k[z]_{\le6}:p(1/2)=0\}\), proved by
quadric restriction and two-point interpolation rather than an inferred
rank. These are necessary cubic-contact data, not the full
length-nine condition.

The older [exact refinement check](../torus/equation_pair_rank_and_weights.support/triple_profiles.py)
and [full source audit](../../computations/audit_sextic_triple_spaces_2026_10_31.py)
remain reproducibility checks of their recorded finite assertions. The
source, restricted-image and determinant statements above now have the
independently reviewed geometric proofs in the linked companion. The
unrestricted \(\Theta\) ranks and the quartic-times-quadric span in
the earlier table retain their computational evidence; those diagnostics
are not inputs to the new proof.

### Sharp length five for pencils with a quadric-divisible member

Fix one of the three surviving characteristic-zero triples \(T_3\) on
\(C=C_0\), and write \(V_d=H^0(\mathcal I_{T_3}(d))\). Let a proper
sextic pencil in \(V_6\) have a member \(F\) with \(h_F\ne0\). If
the pencil has a nonzero member divisible by the equation \(q\) of the
containing quadric, then its generic transverse length is at most five.
The bound is attained in each orbit. A length-nine pencil with a
first-order member through any of these triples must restrict injectively to
\(H^0(Q,\mathcal O_Q(6,6))\). The quadric divisor class already
forces residual support for a proper pencil with a quadric factor.
The uniform contact test determines the sharp residual degree in this
locus and gives actual pairs attaining it.

**Coverage and local reduction.** Work in \(k(C)[[q',y]]\), where
\(q'=m+\gamma y^2\) and \(T_3\) has ideal \((q',y^3)\). The equation
\(F\) defines a smooth transverse formal branch with \(y\) as parameter.
The restriction of \(q\) to this branch has order one by the quadric
transversality computed above. A quadric-divisible pencil member is
\(G=qP\) for a quartic \(P\). Since \(G\) vanishes on the triple,
\(P|_{F=0}\) has order at least two. In particular \(P\) vanishes on
\(C\), so \(G\) has normal order at least two and \(F,G\) span the
pencil. Length at least four requires
\(P|_{F=0}\) to have order at least three. Thus \(P\) vanishes on the
generic triple and belongs to \(V_4\) by purity of \(T_3\).

Every nonzero \(P\in V_4\) is irreducible. There is no form of degree
less than four vanishing on \(T_3\), since its multiples in degree four
would span at least four dimensions while \(\dim V_4=2\). In a
factorization of \(P\), a sole factor through \(C\), counted with
multiplicity, would itself contain \(T_3\) because the other factors
are units at its generic point. Two factors through \(C\) would both
have to be \(q\) up to scalars, whose square has order two on \(T_3\).
The first-normal map on \(V_4\) is injective, so \(P\) too defines a
smooth transverse formal branch. Additivity of order on the branch of
\(F\), followed by exchanging the two equations of the local
intersection \((F,P)\), gives
\[
m_C(F,qP)=1+\operatorname{length}\bigl(k(C)[[q',y]]/(F,P)\bigr)
         =1+\operatorname{ord}_y(F|_{P=0}).
\]

**Uniform restriction test.** For a member \(H\) of either source,
write its coefficients up to weight four in \(q',y\) of weights \(3,1\)
as \(h_Hq'-\Theta_H y^3+e_Hq'y+d_Hy^4\). Along \(P=0\),
\[
q'=\frac{\Theta_P}{h_P}y^3-
\frac{h_Pd_P+e_P\Theta_P}{h_P^2}y^4+O(y^5).
\]
Consequently the condition \(\operatorname{ord}_y(F|_{P=0})\ge5\)
is the simultaneous vanishing of the two polynomials
\[
\Theta_P h_F-h_P\Theta_F,\qquad
h_P^2d_F+\Theta_Ph_Pe_F-(h_Pd_P+e_P\Theta_P)h_F.
\]
Here clearing \(h_P\) takes place over \(k(C)\). Its zeros on \(C\)
do not remove parameters \([P]\) from the computation.

The [exact verifier](../../computations/verify_sextic_quadric_member_contact.py)
reconstructs the full characteristic-zero kernels in degrees four and six,
expands the actual homogeneous monomials in the displayed chart and takes
the coefficient rows of these two polynomials in \(z\). For
\(P=uP_0+vP_1\), the two row blocks have parameter degrees one and two.
Each kernel contains the ten-dimensional space of quadratic multiples of
\(P\), so rank (17\) suffices for equality. The verifier reduces this
matrix at the split prime \(107\) in the rational and quadratic coefficient
fields. At \([0:1]\) it checks a nonzero \(17\)-minor. On the affine
chart \([1:v]\) it computes two maximal minors by exact interpolation
through their degree bounds, with the following output.

| Orbit representative | Affine minor degrees | Affine gcd | Rank at infinity |
| --- | --- | --- | --- |
| Principal | 22, 15 | 1 | 17 |
| One root of \(12r^2+4r+3=0\) | 22, 0 | 1 | 17 |

The gcd check excludes rank drop over the algebraic closure of the residue
field. The rank-drop locus is closed on the projective parameter line over
the coefficient ring localized at the chosen prime. Its image in the
base is closed by properness. A nonempty characteristic-zero fiber would
therefore force a nonempty geometric special fiber. Conjugation gives the
result for the second algebraic orbit. Thus through order four the kernel
is exactly \(P\cdot H^0(\mathcal O_{\mathbf P^3}(2))\) for every
\([P]\). A proper pencil excludes these multiples, proving the length
bound. Independent review reconstructed the local reduction, expanded the
full equation bases in \((m,y)\) to check the corrected quartic coefficient,
and replayed the maximal-minor and parameter-coverage checks.

**Sharpness and residual support.** For any nonzero \(P\in V_4\), take
\(P'\) independent of \(P\) and set
\[
F=x_0^2P+qP',\qquad G=qP.
\]
Both sextics belong to \(V_6\) and \(h_F=(x_0^2|_C)h_P\) is nonzero.
Reducing \(F\) modulo \(q\) and \(P\) shows properness. The verifier
checks that the first-normal map of the quartic pencil has rank two and
its cubic determinant is nonzero in each orbit. The determinant scales
by a nonzero constant under a basis change, so \(P'|_{P=0}\) has
order three for every such choice. Consequently \(F|_{P=0}=qP'|_{P=0}\)
has order four, and \(m_C(F,G)=5\). The residual cycle has degree
\(36-4\cdot5=16\). It contains the divisor residual to \(C\) in
\(F|_Q\), of class \((5,3)\) and degree eight, and the residual
cycle of \(V(F,P)\), also of degree eight, with multiplicities added
if they share components.

Replay with
`python3 -B research/computations/verify_sextic_quadric_member_contact.py`.
This establishes a sharp contact bound in the locus of pencils with
dependent quadric restrictions. The higher contact problem for pencils
with independent restrictions, including the generic length-nine gate,
remains open. The use of the three triples in the sextic STCI reduction
requires the general-pencil ADE hypothesis.

## Necessary ADE arithmetic census for a normal quintic with direction degree one

The historical finite enumeration was **necessary-only**, not a geometric existence or exclusion proof. Its inputs are the smooth marked ADE pairs in Jaffe's classification, target quadratic defect `46/5`, total ADE rank at most `44`, and total marked order at most `12` for direction degree one (the auxiliary degree-zero option uses order at most `13`). For `A_n^k` it assigns rank `n`, marked order `k`, defect `k(n+1-k)/(n+1)`, and local index `(n+1)/gcd(n+1,k)`. For marked `D_n` vector/spin and `E_6,E_7` it uses the corresponding Jaffe table. It enumerates multisets with exact total defect `46/5`, pruning by the rank/order budgets and the upper bound `q <= nr*pr/(nr+pr)` on the remaining defect. Every surviving numerical row for direction degree one has **marked order exactly 12 and rank at least 40** (the looser degree-zero enumeration has order at least 12 and rank at least 32). The local-index lcm yields only a necessary mate divisibility `4*index/gcd(index,5)`. These numerical rows are not asserted to be realized by a normal quintic or by a global supported pair.


### Exact certificate: [audit_sextic_triple_spaces_2026_10_31.py](../../computations/audit_sextic_triple_spaces_2026_10_31.py)

The original python source is preserved in the linked file. Its computational conclusions retain the scope and limitations stated in the mathematical argument above.

