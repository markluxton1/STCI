# Split sextic geometry and multiplicity-six restrictions

This chapter retains exact structural restrictions for two different questions concerning the fixed characteristic-zero embedded quartic \(C_0=[s^4:s^3t:st^3:t^4]\): an integral sextic whose quadratic normal cone splits into two reduced content-free sections, with an arbitrary-degree hypothetical mate; and a degree-\((4,6)\) supported pair with generic curvilinear length six. They share saturated multiplicity and actual normal-source mechanisms, but their necessary data are not identified without proof.

The all-quartic-carrier theorem already excludes a characteristic-zero \((4,6)\) STCI. The seven-type calculation remains useful multiple-curve algebra; it is not a surviving actual degree-pair case. The split-sextic statements concern their exact carrier hypotheses and possible other mate degrees, not all sextic carriers. No unrestricted STCI conclusion follows.

Except for the explicitly characteristic-free singleton-normalization lemma and final local control, the split-carrier numerical and projection arguments below retain their characteristic-zero scope. The conormal splitting, divisions by two, actual source ranks and characteristic-zero geometric arguments are not silently transferred to characteristic two or three. The fixed curve does have a [quartic-carrier STCI in every positive characteristic](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier), which is a separate construction.

The [saturated Gorenstein pairing proof](MULTIPLICITY_MIXED46_AND_MF6.md#2026-10-05-mf6-pairing-audit) supplies the rank-six duality input; [the full primitive-triple obstruction](HIGHER_INITIAL_IDEALS_AND_EMBEDDED_THICKENINGS.md#primitive-triples-on-smooth-rational-quartics) is the stated exclusion input used in the last section. The exact first-normal source space is preserved below with its chosen balanced frame.

## A normalization obstruction for an integral thick sextic

<a id="p-019"></a>

There is a complementary obstruction for one integral thick carrier.  Let an
integral degree-\(a\) surface \(X\ne Q\) have generic normal order \(\mu\) along
\(C\).  Restricting to \(Q\) gives an effective residual class

\[
 (a,a)-\mu(1,3)=(a-\mu,a-3\mu),
\]

so \(a\ge3\mu\).  A thick sextic therefore has \(\mu=2\). This normalization obstruction works in every algebraically closed characteristic: the effective quadric restriction, normalization multiplicity formula (including residue-field degrees), projection formula and Cartier intersection integrality require neither separability nor balanced normal splitting.

Let \(\nu:S=X^\nu\to X\) be the normalization, write the components of
\((\nu^{-1}C)_{\mathrm{red}}\) as \(\Gamma_i\), and put
\(\delta_i=[k(\Gamma_i):k(C)]\).  At the generic point of \(C\), the
one-dimensional hypersurface local ring has multiplicity \(\mu\).  The
normalization multiplicity formula gives

\[
 \mu=\sum_i s_i\delta_i,
\]

with positive integers \(s_i\).  Hence for a sextic
\(\sum_i\delta_i\le2\).

Suppose the reduced inverse image is one irreducible Cartier curve \(\Gamma\)
of degree \(\delta\) over \(C\), and suppose a degree-\(b\) mate exists.
Pulling its Cartier divisor to the normalization gives

\[
 q\Gamma\sim b\widetilde H
\]

for some \(q>0\), where \(\widetilde H=\nu^*O_X(1)\).  Projection formula
gives

\[
 \widetilde H^2=a,\qquad \widetilde H\Gamma=4\delta.
\]

Intersecting the displayed equivalence first with \(\widetilde H\) and then
with \(\Gamma\) yields

\[
 \boxed{\Gamma^2=\frac{16\delta^2}{a}.}
\]

For \(a=6\), the multiplicity formula permits only \(\delta=1,2\), giving
\(8/3\) or \(32/3\).  This contradicts integrality of the self-intersection of
a Cartier curve.  Thus a thick sextic in a defining pair can survive this
argument only if the normalized preimage splits into two degree-one branches,
or its irreducible preimage is non-Cartier.  Those are genuine gaps: the
split-branch intersection equations have consistent integral numerical
solutions, so one cannot silently assume equal branch multiplicities or
iterate the same fractionality argument.

### P-020: the split-sextic branch has only two extreme numerical types

Let

\[
 \pi:B=\operatorname{Bl}_C\mathbf P^3\longrightarrow\mathbf P^3,
 \qquad E=\mathbf P(N_C^*)\simeq\mathbf P^1\times\mathbf P^1,
\]

and use the bidegree convention in which

\[
 H|_E=\mathcal O_E(4,0),\qquad
 \mathcal O_E(E)=\mathcal O_E(7,-1).
\]

An integral sextic of exact normal order two has strict transform
\(D\sim6H-2E\), and hence

\[
 D|_E\sim(10,2).
\]

Assume this divisor is the reduced sum of two distinct integral, content-free
sections, with no vertical component:

\[
 Z_1\sim(d,1),\qquad Z_2\sim(10-d,1).
\]

After exchanging them, take \(0\le d\le5\).  The no-vertical hypothesis makes
the blowdown of the normalized strict transform quasi-finite over the sextic;
the two curves \(\Gamma_i\) above \(Z_i\) are therefore exactly the two
divisorial branches over \(C\).  If a degree-\(b\) mate exists, its pullback to
the normalization has divisor

\[
 bH\sim m_1\Gamma_1+m_2\Gamma_2,
 \qquad m_1,m_2>0.
\]

This equality is an equality of Weil divisors with Cartier left side.  It may
be intersected with the Cartier divisors \(H\) and \(E\), even when the
individual branches are not Cartier.  The ambient blowup intersections are

\[
 H^2D=6,\qquad HED=8,
\]

and

\[
 H\Gamma_i=4,\qquad
 E\Gamma_1=7-d,\qquad E\Gamma_2=d-3.
\]

Consequently

\[
 m_1+m_2=\frac{3b}{2},
\]

\[
 (7-d)m_1+(d-3)m_2=8b.
\]

Put \(\Delta=m_1-m_2\).  Eliminating \(m_2\) gives

\[
 \Delta(5-d)=5b,
 \qquad
 \frac{m_2}{b}=\frac{5-3d}{4(5-d)}.
\]

The case \(d=5\) is impossible, and positivity of \(m_2\) leaves only

\[
 \boxed{d=0,\quad(m_1,m_2,b)=k(5,1,4)}
\]

or

\[
 \boxed{d=1,\quad(m_1,m_2,b)=k(11,1,8)}.
\]

This is a finite reduction, not yet an unconditional exclusion.  It becomes
an exclusion if the two branches are Cartier on the normalization.  Writing
\(z=\Gamma_1\Gamma_2\), one then has

\[
 \Gamma_1^2=7-d-z,\qquad
 \Gamma_2^2=d-3-z.
\]

Intersecting the mate divisor with each branch forces respectively

\[
 d=0:\quad z=\frac{19}{4},
 \qquad
 d=1:\quad z=\frac{17}{5},
\]

both impossible for Cartier-curve intersection numbers, which are integers also on the normal surface.  In particular, if
the first strict transform is smooth at the ten collision points, its branch
intersection is the ordinary value

\[
 Z_1Z_2=10,
\]

and the contradiction is immediate.

The qualification is essential.  On the normal local surface

\[
 xy=e^n,
\]

the two components of \((e=0)\) meet with Mumford intersection \(1/n\), not
one.  Thus normality alone does **not** imply \(z=10\); isolated local
class-group corrections are exactly the remaining split-sextic escape route.
The two forced values above quantify those corrections.  In transverse
\(A_{r-1}\) models they require total differents \(21/4\) and \(33/5\),
respectively.



### P-022: the actual thick-sextic first-normal image

For any characteristic-zero smooth rational quartic, the quadratic
first-normal map is

\[
 H^0(I_C^{(2)}(6))\longrightarrow
 H^0\bigl(C,\operatorname{Sym}^2N_C^*\otimes O_C(6)\bigr).
\]

P-017 gives a 23-dimensional source.  Its kernel is exactly
\(H^0(I_C^{(3)}(6))=kq^3\): restriction to the unique quadric would otherwise
give a section of \(O_Q(3,-3)\).  Thus its image \(W\) has dimension 22.
If \(U\) is the seven-dimensional first-normal image of cubics through \(C\),
then

\[
 W=\langle U\cdot U\rangle.
\]

For \(C_0\), in the balanced frame

\[
 z=x_1/x_0,\qquad a=x_2-z^3,\qquad b=x_3-z^4,
 \qquad \xi=b-\tfrac32za,\quad\eta=a,
\]

an exact row reduction gives eleven independent linear equations cutting out
\(W\subset H^0(O(10))^3\).  Writing a normal quadratic as

\[
 \alpha(z)\xi^2+\beta(z)\xi\eta+\gamma(z)\eta^2,
\]

the equations are

\[
\begin{aligned}
-\alpha_9+2\beta_{10}&=0,&-\beta_0+2\gamma_1&=0,\\
\alpha_0-2\beta_1+4\gamma_2&=0,
&-3\alpha_1+2\beta_2+4\gamma_3&=0,\\
\alpha_2-2\beta_3+4\gamma_4&=0,
&\alpha_3-2\beta_4+4\gamma_5&=0,\\
-\alpha_4+4\gamma_6&=0,
&\alpha_5-2\beta_6+4\gamma_7&=0,\\
\alpha_6-2\beta_7+4\gamma_8&=0,
&-\alpha_7-2\beta_8+12\gamma_9&=0,\\
\alpha_8-2\beta_9+4\gamma_{10}&=0.
\end{aligned}
\]

Solving them produces primitive split
quadratics

\[
 (p\xi+r\eta)(u\xi+v\eta)
\]

of every type \((d,1)+(10-d,1)\), \(0\le d\le5\).  Therefore the actual
ambient image, and not merely the complete space of normal quadratics, permits
all split types.

Exact affine representatives \((p,r),(u,v)\) for the two factors are:

\[
\begin{array}{c|c|c}
d&(p,r)&(u,v)\\\hline
0&(1,0)&(-z^{10}-2,-z)\\
1&(1,z)&(2+6z+2z^8,z+z^2+z^9)\\
2&(1,z^2)&(2+4z+24z^7,z+2z^2+z^5+2z^6+4z^7+12z^8)\\
3&(1,z^3)&(8-2z+8z^3+24z^5+8z^6,4z-3z^2+4z^6+4z^7)\\
4&(1,z^4)&(4+2z+12z^4+4z^5,2z+3z^2+2z^5+2z^6)\\
5&(z^5,1)&(-z^5,1).
\end{array}
\]

This also falsifies a tempting inference.  A square discriminant on the
exceptional divisor forces the *normal divisor* to split, but not the ambient
sextic.  Exact integral examples are

\[
 (A+x_3q)(A-x_3q)+q^3
\]

and

\[
 (A+x_3q)(2A+D)+q^3.
\]

The second has smooth first strict transform at all collisions of its two
normal sections.  Thus any later argument must use the mate, higher normal
coefficients, or normalization intersection theory; first-normal
factorization alone is insufficient.



### P-023: Hodge exclusion for squarefree split-sextic residuals

Retain the split/no-vertical hypotheses of P-020 and let \(S\) be the
normalization of the strict transform of the sextic.  Work on a resolution
\(\widetilde S\), using Mumford numerical pullbacks for the two branch curves.
Write

\[
 K_0=2H-E.
\]

This is the pullback of the adjunction class cut by the unique quadric; it
must not be silently identified with the canonical divisor of a singular
normalization or of its resolution.  The ambient intersections are

\[
 H^2=6,\quad HE=8,\quad E^2=4,
 \quad HK_0=4,\quad K_0^2=-4.
\]

For the low-degree branch \(\Gamma\) of type \((d,1)\), P-020 gives

\[
 K_0\Gamma=d+1,\qquad
 \Gamma^2=\begin{cases}9/4&d=0,\\13/5&d=1.\end{cases}
\]

Put

\[
 L=H+K_0,\qquad
 T=\Gamma^\#+\frac{d+1}{4}K_0,
\]

where \(\Gamma^\#\) is the numerical pullback.  Then \(L^2=10\),
\(LK_0=TK_0=0\), and equality holds in Hodge index:

\[
 (LT)^2=L^2T^2.
\]

Consequently

\[
 T\equiv\tfrac12L\quad(d=0),\qquad
 T\equiv\tfrac35L\quad(d=1).
\]

If the residual binary quartic is squarefree, the quadric section of \(K_0\)
is a sum of four pairwise-disjoint reduced ruling lines \(R_j\).  Each \(R_j\)
is Cartier on the normal surface, even if it passes through a singular point:
locally it is the only component of the reduced Cartier divisor through that
point.  Moreover

\[
 HR_j=1,\qquad K_0R_j=-1,\qquad LR_j=0.
\]

Intersecting the numerical proportionality with \(R_j\) yields

\[
 \Gamma R_j=\frac{d+1}{4},
\]

equal to \(1/4\) or \(1/2\), contrary to integrality of intersection with the
Cartier curve \(R_j\).  Hence neither surviving split type can have a
squarefree residual quartic.  This proof was independently audited for signs
and for the use of Hodge index on a resolution.  What remains is precisely the
highly non-squarefree residual locus; squarefreeness does not follow merely
from a reduced, content-free split first-normal divisor.

For \(C_0\), exact next-jet calculations are consistent with this boundary.
For every \(d=0\) factor, imposing both first-normal divisibility and vanishing
of the next normal coefficient makes the collision polynomial have affine
degree at most five and forces a square factor in the residual binary quartic.
A large \(d=1\) chart has the same behavior.  The full projective space of
\((1,1)\)-factors has not been eliminated.



### P-030: residual-root multiplicities in the split sextic cases

Assume the split/no-vertical hypotheses of P-020 and P-023.  Let
\(K_i\) be the full Cartier cluster lying over a distinct root of the residual
binary quartic, including its root multiplicity and every exceptional
component required by resolution, and let that multiplicity be \(\mu_i\).
The four total units satisfy \(\sum_i\mu_i=4\).

With \(K_0=2H-E\), the intersection identities on the resolved normalization
are

\[
 H\cdot K_i=\mu_i,\qquad E\cdot K_i=3\mu_i,\qquad
 K_0\cdot K_i=-\mu_i,\qquad L\cdot K_i=0.
\]

The same Hodge-index equality used in P-023, now applied to the full cluster
rather than to a reduced branch, forces the low-degree normalization branch
to meet \(K_i\) in

\[
 \Gamma_{\mathrm{low}}\cdot K_i=
 \begin{cases}
   \mu_i/4,&d=0,\\
   \mu_i/2,&d=1.
 \end{cases}
\]

The cluster \(K_i\) is the full Cartier divisor pulled back from the normalization, so it is orthogonal to every exceptional curve. Thus \(\Gamma_{\mathrm{low}}^\#\cdot K_i\) equals the intersection of the integral strict transform with that integral Cartier pullback, and is an integer. This does not assert that the rational numerical pullback \(\Gamma_{\mathrm{low}}^\#\) is integral or Cartier downstairs.  In the
\(d=0\) case every \(\mu_i\) is divisible by four, so the only partition is
\([4]\).  In the \(d=1\) case every \(\mu_i\) is even, leaving only
\([4]\) and \([2,2]\).  The conclusion concerns full Cartier clusters; it
must not be applied to only the reduced visible branch over a multiple root.

This removes the squarefree residual case already excluded in P-023 and all
partitions except the three displayed possibilities.  It does not yet exclude
the surviving multiple-root configurations.



## Clean split conductor: a branch exclusion and its stronger global model

<a id="p-027"></a>

This argument has two distinct scopes. Let \(X\subset\mathbf P^3_{\mathbf C}\)
be an integral sextic, generically nodal along the smooth rational quartic
\(C\), with smooth normalization \(\nu:S\to X\). Suppose the inverse image
of \(C\) consists of two branches \(\Gamma_1,\Gamma_2\), each mapping
isomorphically to \(C\), and
\[
 I_CO_S=O_S(-\Gamma_1-\Gamma_2).
\]
Assume the source conductor divisor is
\(\Delta=\Gamma_1+\Gamma_2+\Delta'\), with \(\Delta'\) disjoint from
both branches. Retain the reduced/content-free split first-normal divisor
\((d,1)+(10-d,1)\), with no vertical component, from the preceding
split-carrier calculation. These are sufficient for the branch exclusion.
Global invariants stated below additionally require \(\Delta'=0\).

The [source double-point/finite-duality formula of Kleiman–Lipman–Ulrich](https://www.math.purdue.edu/~jlipman/papers/2-point.pdf), applied to the finite normalization map into the smooth threefold, gives
\[
 K_S+\Delta=2H.
\]
Because \(\Delta'\) is disjoint from each branch, intersecting with
\(\Gamma_i\) and comparing smooth adjunction
\((K_S+\Gamma_i)\Gamma_i=-2\), with \(H\Gamma_i=4\), gives
\[
 \Gamma_1\Gamma_2=10.
\]
The clean ideal makes the lifted blowup divisor exactly
\(E=\Gamma_1+\Gamma_2\) on \(S\); the split first-normal degrees give
\(E\Gamma_1=7-d\) and \(E\Gamma_2=d-3\). Hence
\[
 \Gamma_1^2=-d-3,\qquad \Gamma_2^2=d-13.
\]
If a degree-\(b\) mate exists, then
\(bH\sim m_1\Gamma_1+m_2\Gamma_2\), with positive integral \(m_i\).
Intersecting with \(H\) gives \(m_1+m_2=3b/2\). Intersecting with the two
branches gives
\[
 4b=-(d+3)m_1+10m_2,
 \qquad4b=10m_1+(d-13)m_2.
\]
Eliminating \(m_i\) forces
\[
 d^2-10d-35=0,
\]
which has no integral solution \(0\le d\le5\). Equivalently, the forced
ratio is \(m_1/b=(9\pm\sqrt{15})/12\), not rational. Thus even additional
conductor components disjoint from the two branches do not rescue this
branch-intersection model.

For the stronger global numerical model, assume the **entire** source
conductor divisor is \(\Gamma_1+\Gamma_2\). Then
\(K_S+\Gamma_1+\Gamma_2=2H\) globally. The target conductor is exactly
\(I_C\): the pullback ideal is the source conductor, so \(I_C\) is
contained in the target conductor; conversely a conductor function vanishes
at the generic point of the integral reduced curve \(C\), and therefore
belongs to its prime ideal. The conductor square consequently gives
\[
 0\longrightarrow O_X\longrightarrow\nu_*O_S
 \longrightarrow O_C(-Z)\longrightarrow0,
 \qquad\operatorname{length}Z=10.
\]
Indeed, the two rational branches meet in the length-ten subscheme \(Z\).
Their union has structure sheaf consisting of pairs of branch functions
agreeing on \(Z\); modulo the diagonal \(O_C\), this is \(O_C(-Z)\).
Since \(\chi(O_X)=11\) for a sextic hypersurface,
\(\chi(O_C(-Z))=-9\), so \(\chi(O_S)=2\). Finite duality identifies
\(\nu_*\omega_S=I_C\otimes\omega_X=I_C(2)\). The quartic has its unique
containing quadric, so \(p_g(S)=h^0(I_C(2))=1\), and then \(q(S)=0\).
Finally
\[
 K_S^2=4H^2-4H(\Gamma_1+\Gamma_2)+(\Gamma_1+\Gamma_2)^2=-4,
 \qquad c_2(S)=12\chi(O_S)-K_S^2=28.
\]
These are the classical ordinary-sextic numbers. In the ordinary model the
degree-twenty discriminant has twenty pinch points, so its double conductor
cover is connected of genus nine and cannot be the two split rational
branches. That comparison uses the ordinary-model hypotheses.

The global numbers do not follow merely from absence of additional conductor
*meeting* the branches: disjoint extra conductor can change them. The branch
exclusion has the weaker disjointness scope proved above; the numerical
identities have the entire-conductor scope. Singular normalization, extra
conductor meeting a branch, or a finite-length factor in \(I_CO_S\) are genuine
escapes from this clean calculation. Nothing here excludes every integral
sextic carrier or constructs an STCI mate.

### P-041: torsion-corrected sharpening of the surviving split sextics

Retain the split, reduced, content-free, no-vertical hypotheses of P-020,
P-023, and P-030.  The only residual binary-quartic root partitions are
\([4]\) for \(d=0\), and \([4]\) or \([2,2]\) for \(d=1\).  Over an
algebraically closed characteristic-zero field every such quartic is a square.
Writing \(h\) for the equation of \(C\) on its unique quadric \(Q=(q=0)\),

\[
 F|_Q=h^2P_2^2=(hP_2)^2.
\]

The bidegree-\((3,3)\) form \(hP_2\) lifts to a cubic
\(T\in I_C(3)\).  Hence \(F-T^2=qK\) for a quartic \(K\), and locally
\((I_C^2:q)=I_C\) gives

\[
 \boxed{F=T^2+qK,\qquad T\in I_C(3),\quad K\in I_C(4).}
\]

Every residual root selected by the low first-normal branch is also met by
the high branch.  On the exceptional divisor the first strict transform has
equation \(\ell m=0\), so its differential vanishes along the exceptional
tangent directions at such a point.  On the strict transform of \(Q\), the
residual root has multiplicity at least two, so the differential vanishes
along those tangent directions as well.  These two divisors are transverse in
the smooth blowup; consequently the first strict transform is singular at
every selected residual-root point.

The mate relations must retain their common scale \(k>0\).  They imply

\[
\begin{array}{c|c|c}
d&(m_{\mathrm{low}},m_{\mathrm{high}},b)&
\text{Cartier multiple forced by the mate}\\\hline
0&k(5,1,4)&4k\Gamma_{\mathrm{low}},\\
1&k(11,1,8)&10k\Gamma_{\mathrm{low}}.
\end{array}
\]

One cannot cancel \(k\): local class groups may have torsion.  In an
independently established ordinary \(A_{\mu-1}\) model
\(xy=t^\mu\), a low branch of contact \(\alpha\) represents
\(\alpha\in\mathbb Z/\mu\), has local Mumford intersection
\(\alpha^2/\mu\), and contributes correction
\(\alpha(\mu-\alpha)/\mu\).  Thus a two-simple \(d=1,[4]\) allocation with
ordinary \(A_3\) germs forces only \(k\) even; it is not unconditionally
excluded.  This corrects the invalid stronger inference from
\(10k[\Gamma]=0\) to \(10[\Gamma]=0\).

There is one further exact exclusion for \(C_0\).  At a totally ramified
ruling, normalize \(d=1,[4]\) so the low factor restricts to \(z^2\).
In the balanced frame its global form is

\[
 (p_0-2z)\xi+\frac{p_0z}{2}\eta.
\]

Content freedom of this low section requires \(p_0\ne0\). Write the high factor as

\[
 u(z)\xi+\left(z^{10}+\frac z2u(z)\right)\eta.
\]

The eleven exact first-normal image equations force \(u_9=-2\) and
\(u_0=u_3=u_6=0\).  In particular both high coefficients are divisible by
\(z\), creating forbidden vertical content.  Coordinate reversal gives the
same conclusion at the other totally ramified ruling.  The general
\(d=0,[4]\), non-totally-ramified \(d=1,[4]\), and \(d=1,[2,2]\) loci remain
open.  The last locus genuinely contains a missed projective boundary at
first-normal order.  In the balanced frame with quadric direction
\(q_1=\xi+z\eta/2\), the content-free factors

\[
 \ell=\xi+\frac32z\eta,
 \qquad
 m=(1-3z^4+z^8)\xi+
   \left(\frac z2-\frac{z^5}{2}+\frac{z^9}{2}\right)\eta
\]

have evaluations \(z\) and \(z^5\) on \(q_1\).  Their product therefore has
the required boundary evaluation \(z^6\), homogeneously \(s^6t^6\), and its
quadratic coefficients

\[
 \alpha=z^8-3z^4+1,\qquad
 \beta=2z^9-5z^5+2z,\qquad
 \gamma=\frac34(z^{10}-z^6+z^2)
\]

satisfy all eleven P-022 image equations.  This is an exact, content-free
first-normal survivor, not an ambient integral sextic or an STCI pair.  It
shows why the \([2,2]\) boundary must remain in the search.  Unsaved
higher-jet samples supply only computational evidence.



### P-042: the necessary multiplicity-six types for a mixed \((4,6)\) pair

Let \(k\) be algebraically closed of characteristic zero and suppose
\(X=V(F_4,G_6)\) is supported set-theoretically on \(C_0\).  The forms have no
common surface factor, so \(X\) is a degree-24 lci curve of generic length six
over \(C_0\).  By P-011 the quartic has normal order one at the generic point.
In the completed transverse regular local ring it can therefore be taken as
one parameter; modulo it the other equation is a unit times the sixth power of
the remaining parameter.  Thus \(X\) is quasiprimitive.

Write the Bănică--Forster pieces as \(E_i=L^i(D_i)\), with \(D_1=0\).  For a
quasiprimitive multiplicity-six lci, the Gorenstein multiplication pairings

\[
 E_i\otimes E_{5-i}\longrightarrow E_5
\]

are isomorphisms.  The natural multiplication maps encode the inequalities
\(D_i+D_j\le D_{i+j}\).  The pairings give
\(D_4=D_5=D_2+D_3\), while \(2D_2\le D_4\) gives
\(0\le D_2\le D_3\).  The pieces therefore have the necessary form

\[
 O_C,\quad L,\quad L^2(D_2),\quad L^3(D_3),\quad
 L^4(D_2+D_3),\quad L^5(D_2+D_3).
\]

Put \(l=\deg L\) and \(d_i=\deg D_i\).  Since \(C_0\simeq\mathbf P^1\),
additivity of Euler characteristic gives

\[
 \chi(O_X)=6+15l+3(d_2+d_3).
\]

A \((4,6)\) complete intersection has

\[
 p_a(X)=1+\frac{24(4+6-4)}2=73,
 \qquad \chi(O_X)=-72,
\]

and hence

\[
 \boxed{5l+d_2+d_3=-26.}
\]

The first piece is a line-bundle quotient
\(O_{\mathbf P^1}(-7)^2\twoheadrightarrow L\), so \(l\ge-7\); effectivity
and the displayed equation give \(l\le-6\).  The eight raw numerical types are

\[
\begin{array}{c|c}
l&(d_2,d_3)\\\hline
-7&(0,9),(1,8),(2,7),(3,6),(4,5),\\
-6&(0,4),(1,3),(2,2).
\end{array}
\]

When \((l,d_2)=(-7,0)\), the canonical multiplicity-three member of the
filtration has pieces \(O,L,L^2\) and is a global primitive triple of type
\(O(-7)\), contrary to P-010.  Exactly seven necessary numerical types remain.
No existence or compatibility among these numerical candidates is asserted.

Finally, the quotient \(O(-7)^2\twoheadrightarrow O(l)\) is represented by a
basepoint-free pair of sections of degree

\[
 e=l+7\in\{0,1\}.
\]

This is precisely the horizontal degree in P-031.  In the nonregular branch,
P-031 gives \(1\le p\le8-e\), \(c=9-e-p\), and \(\deg Z=p+8\).  Therefore
only \(8+7=15\) of the former 36 coarse pole-divisor strata remain.  The seven
Bănică--Forster numerical types and the fifteen pole strata record different
necessary data; no unproved correspondence between them is being assumed.


## Further actual lifts and surviving limits

The [fixed ramified boundary and its larger chart](RESIDUAL_CYCLES_AND_SPLIT_CONFIGURATIONS.md#2026-10-05-split-sextic) construct actual sextic lifts and prove the all-mate exclusion for the specified fixed normal form; this does not exclude every first-normal survivor. The [nonramified quadruple-root and additional two-double-root charts](RESIDUAL_CYCLES_AND_SPLIT_CONFIGURATIONS.md#2026-10-05-split4-nonramified) retain the actual local models and their restrictions. In particular the first-normal boundary example above is a control of source compatibility, not an actual integral carrier or mate.

The numerical seven types in the final section are a coarse stage. The [corrected first-normal Fitting divisor and pole comparison](MULTIPLICITY_MIXED46_AND_MF6.md#2026-10-05-mixed46-poles) gives the stronger exact divisor relation \(A=D_3+\min(D_2,D_3-D_2)\) under its hypotheses. The distinction between that refined evidence, the earlier fifteen coarse pole strata, and actual realization must be retained. No uniform correspondence or realized configuration is inferred from the tables.


## A local control for the regular-ratio hypothesis

For any field and integer \(m\ge2\), in \(k[[t,u,v]]\) take
\(F=tu+v^m\), \(G=u\). Their ideal is exactly \((u,v^m)\), a
complete intersection with radical \((u,v)\), and the quotient is free of
rank \(m\) over \(k[[t]]\). Thus transverse length is constant even at
\(t=0\). The first-normal forms are \(tu\) and \(u\), with rational
quotient \(1/t\). Proper local complete intersection and constant length
therefore do not imply a regular quotient, and do not justify subtracting a
global multiple of one equation from the other. This formal local control
asserts no projective realization with prescribed degrees.


## Further higher-jet reduction

The [full two totally ramified-root reduction](SPLIT_SEXTIC_TWO_RAMIFIED_ROOTS.md) treats the entire stated two-root family, including the zero-polynomial stratum, and leaves an explicit one-parameter carrier line. It is distinct from the preceding first-normal and numerical restrictions.

## Consolidation review

Independent review reconstructed all preserved P019/P020/P022/P023/P027/P030/P041/P042 arguments, source coverage and characteristic boundaries, including the entire-conductor qualification for global invariants. The separate full two-ramified-root reduction was also independently reconstructed and accepted. The bounded proof clarifications in this account
were checked against the original arguments; no material preservation finding
remains. The claims retain their stated hypotheses.
