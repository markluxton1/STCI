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
Their full degree-six equation spaces and first further contact condition
are computed below; higher extensions and sole support remain unresolved.

## Full sextic spaces and the first further contact equation

The [exact source-space computation](https://github.com/markluxton1/STCI/blob/9deae1cc7f4b008fb287d13bdb2776faa1e75bf5/research/computations/audit_sextic_triple_spaces_2026_10_31.py)
uses all ambient monomials and the accepted triple substitution
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
vanish; those conditions and properness have not been solved here.

The script uses exact rational arithmetic and
\(\mathbb Q(\sqrt{-2})\). Conjugation transports the complete algebraic
source and contact matrices to the other root, preserving the ranks.
An independent review reconstructed the substitution, global-source
coverage and contact sign, ran the exact calculation, and added a direct
rank-and-containment check for all twenty quartic-times-quadric products.
Run `PYTHONDONTWRITEBYTECODE=1 python3 research/computations/audit_sextic_triple_spaces_2026_10_31.py`.
This completes the stated linear calculation and first necessary contact
test; it does not exclude the remaining sextic pairs.

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
The retained exact source calculation gives
\[
 \dim K=
 \begin{cases}
 4&\text{principal orbit},\\
 3&\text{either algebraic orbit}.
 \end{cases}
\]
Equivalently, the first residual contact coefficient on the
second-order subsystem has ranks six and seven, respectively. These
are geometric filtration dimensions; their present numerical
verification is computational.

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

#### What the exact wedge computation adds

The retained [exact sextic audit](../../computations/audit_sextic_triple_spaces_2026_10_31.py)
computes the full exterior-square map and reports, for both orbit
types,
\[
 \operatorname{rank}\Omega_3=23,\qquad
 \dim\ker\Omega_3=328,\qquad
 \operatorname{im}\Omega_3=k[z]_{\le22}.
\]
This is a check of the **span of cubic-contact obstructions**, not
a count of geometric pencils. The different ranks of the joint
normal-jet maps, \(23\) for the principal orbit and \(24\) for the
algebraic orbit, are distinct invariants. The historical algebraic
joint-rank value \(26\) is incorrect. The exact-arithmetic output
was supplied from an execution of the retained script; its
implementation has not received an independent mathematical audit.

The geometric incidence argument above settles the existence of
proper cubic-contact pencils without relying on surjectivity of
\(\Omega_3\). It does **not** settle the higher-order equations,
generic transverse multiplicity nine, or sole support \(C\).
Those are the remaining substantive gates for a supported sextic pair.

## Necessary ADE arithmetic census for a normal quintic with direction degree one

The historical finite enumeration was **necessary-only**, not a geometric existence or exclusion proof. Its inputs are the smooth marked ADE pairs in Jaffe's classification, target quadratic defect `46/5`, total ADE rank at most `44`, and total marked order at most `12` for direction degree one (the auxiliary degree-zero option uses order at most `13`). For `A_n^k` it assigns rank `n`, marked order `k`, defect `k(n+1-k)/(n+1)`, and local index `(n+1)/gcd(n+1,k)`. For marked `D_n` vector/spin and `E_6,E_7` it uses the corresponding Jaffe table. It enumerates multisets with exact total defect `46/5`, pruning by the rank/order budgets and the upper bound `q <= nr*pr/(nr+pr)` on the remaining defect. Every surviving numerical row for direction degree one has **marked order exactly 12 and rank at least 40** (the looser degree-zero enumeration has order at least 12 and rank at least 32). The local-index lcm yields only a necessary mate divisibility `4*index/gcd(index,5)`. These numerical rows are not asserted to be realized by a normal quintic or by a global supported pair.


### Exact certificate: [audit_sextic_triple_spaces_2026_10_31.py](../../computations/audit_sextic_triple_spaces_2026_10_31.py)

The original python source is preserved in the linked file. Its computational conclusions retain the scope and limitations stated in the mathematical argument above.
