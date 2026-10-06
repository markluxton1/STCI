> **2026-10-06 CONSOLIDATION NOTICE:** This is a dated historical synthesis. For the authoritative current mathematical status, see [AUDITED_STATE_2026-10-06.md](AUDITED_STATE_2026-10-06.md). Where frontier language below conflicts with that file, the audited state controls.\n\n# Research Report: Set-Theoretic Complete Intersections of Space Curves

Cutoff: 2026-09-30

The durable proofs and exact hypotheses are in `RESEARCH_RECORD.md`; checked
sources are in `LITERATURE_LEDGER.md`. This report is the mathematical
synthesis at closeout, not a substitute for those two ledgers.

## Executive conclusion

The original problem was not solved.

Let \(k\) be algebraically closed and let \(C\subset\mathbf P^3_k\) be an
integral closed curve, with saturated homogeneous prime ideal \(I_C\). The
problem is whether there always exist two homogeneous forms \(F,G\) such that

\[
 V_+(F,G)=C,
 \qquad\text{equivalently}\qquad
 \sqrt{(F,G)^{\mathrm{sat}}}=I_C.
\]

The checked literature still treats this as open. The open status is already
witnessed over \(\mathbf C\), for smooth curves, by the smooth rational quartic

\[
 C_0=[s^4:s^3t:st^3:t^4].
\]

Eisenbud--Harris (2024) explicitly presents this example as open, and
Murayama's April 2026 notes retain the same status. Searches through
30 September 2026 found no unrestricted solution, no smooth complex
counterexample, and no resolution of \(C_0\). This is a dated literature
assessment, not a logical proof that no unindexed result exists.

The run nevertheless made substantial progress on the smooth rational-quartic
frontier:

- it proved structural statements for all smooth rational quartics, including
  the exact affine/projective boundary and low-multiplicity obstructions;
- it proved internally that every smooth rational quartic is an STCI in
  positive characteristic, by degrees \((3,4p)\);
- it eliminated primitive triples of conormal type \(O(-7)\) for every
  characteristic-zero smooth rational quartic;
- it reduced a hypothetical \((4,5)\) presentation to two exhaustive
  quasiprimitive types and excluded both for \(C_0\), proving that no
  characteristic-zero degree-\((4,5)\) presentation exists;
- it identified and repaired a gap in the purported universal ambient
  \((4,5)\) and mixed \((4,6)\) reductions: a quotient of proportional first
  normal forms can have poles at vertical order jumps; the finite
  seven-variable problem and the \(e\le3\) bound are therefore conditional
  regular-ratio results;
- it identified degree six as the first thick-carrier degree and closed large
  portions of the sextic and mixed \((4,6)\) branches;
- it strengthened the Hodge-index analysis: residual root multiplicities are
  forced to \([4]\) for split type \(d=0\), and to \([4]\) or \([2,2]\) for
  type \(d=1\); it further proved the residual-square normal form
  \(F=T^2+qK\), forced singularity at selected roots, and one exact
  totally-ramified endpoint exclusion, while retaining the mate scale \(k\)
  needed in torsion local class groups;
- it proved an explicit \((4,p)\) presentation of \(C_0\) in every prime
  characteristic \(p\ge7\), and an exact complement-morphism reformulation of
  the general STCI problem;
- it obtained an exact normalization--conductor criterion for carriers
  singular along the support, and extended the characteristic-zero
  Cartier-index compression to singular integral curves on generically
  regular carriers;
- it used the classical global Chow-resultant certificate, computed the exact
  10-term Chow quartic of \(C_0\), and proved that ordinary \(K_0\) sees only
  the Bezout divisibility condition;
- it used one Schubert-line pencil to exclude unconditional 13-dimensional
  quartic and 28-dimensional quintic carrier subspaces from every \((4,5)\)
  pair, and exhibited an irreducible pair that passes that pencil but fails
  its reversal, showing the limitation of a one-pencil test;
- it excluded common local-cohomology ancestors through multiplier degree
  three, produced a coprime nonconstant-ratio degree-four first-symbol family,
  and then excluded that entire explicit family at every direct-limit stage by
  a transition-compatible five-coefficient certificate.

The highest-value unresolved targets are now the seven necessary mixed
\((4,6)\) numerical types and their 15 nonregular pole strata, the surviving
split-sextic loci, and the remaining degree-four local-cohomology rank-one
pairs.  The unrestricted characteristic-zero status of \(C_0\) remains
open despite the new degree-\((4,5)\) theorem.

## 1. Current literature landscape

### General and smooth projective questions

The literature supports the following status through the cutoff:

- every projective space curve is cut out set-theoretically by at most three
  hypersurfaces (Kneser; related general bounds of Eisenbud--Evans);
- the unresolved issue in \(\mathbf P^3\) is arithmetic rank two versus three;
- no unconditional counterexample among smooth complex space curves is known;
- the smooth nondegenerate rational quartic is the first unresolved smooth
  example by degree;
- the general integral-curve problem remains open a fortiori.

Broad positive classes include plane curves, complete intersections, twisted
cubics, elliptic quartic complete intersections, and arithmetically
Cohen--Macaulay curves. These do not contain the rational quartic, which is not
linearly normal and not ACM.

Known negative results for rational quartics are degree- or carrier-specific.
Craighero and Craighero--Gattazzo exclude \((3,4)\), \((4,4)\), and ultimately
every cubic carrier in characteristic zero; Stagnaro gives the classical
global no-\((3,4)\) theorem; Ellia restricts primitive types; Jaffe restricts
pairs under hypotheses on common singularities; and Hartshorne--Polini rule
out ordinary-carrier configurations. None is an absolute non-STCI theorem.

### Why the affine theorem does not transfer

Forster's Theorem 5.2 states that every lci curve in affine space is an STCI,
building on Ferrand--Szpiro and Mohan Kumar. The 2026 published theorem of
Mandal--Zinna extends an affine result under conormal, \(K_0\), and ambient
freeness hypotheses. Their November 2025 arXiv v1 claims a much broader
three-dimensional affine theorem; that broad claim had not been located in a
peer-reviewed source at the cutoff.

None solves the projective question. Two formulations explain the failure:

1. the affine Ferrand construction produces a rank-two bundle which becomes
   free on affine space, while a projective pair requires a splitting as
   \(O(-a)\oplus O(-b)\);
2. after deleting a hyperplane, an affine radical pair homogenizes correctly
   exactly when its leading forms are relatively prime. Affine existence does
   not provide this boundary condition.

For \(C_0\), the natural affine chart is even a scheme-theoretic complete
intersection, but its homogenized generators acquire a common component at
infinity. Smoothness solves the local/affine problem and leaves the global
boundary and multiple-structure problem untouched.

### Positive characteristic

Hartshorne and Moh prove strong positive-characteristic theorems for monomial
curves and cuspidal projections; Cowsik--Nori proves every pure affine curve is
an STCI in positive characteristic. These do not settle arbitrary projective
curves. The universal projective problem remains open field by field.

The internal result P-012 is stronger for one smooth family: every smooth
rational quartic over an algebraically closed field of characteristic \(p>0\)
has an explicit \((3,4p)\) presentation. No theorem of that exact family-wide
scope was located. An independent in-run audit checked every hinge, including
the wild characteristic-two step, and found no mathematical gap. Because the
claim may be new, it still warrants ordinary external expert review before
circulation.

## 2. Why the smooth case was productive

Concentrating on smooth curves was mathematically advantageous without
replacing the general problem:

- one smooth counterexample would disprove the general assertion;
- a theorem for all smooth curves would itself be a major result;
- smoothness gives a rank-two conormal bundle, regular blowup, finite-flat
  transverse algebras, Bănică--Forster filtrations, and exact normal jets;
- \(C_0\) is explicit enough for exact symbolic calculation but is still a
  genuine open case.

The run also showed the limitation sharply. No carrier in a defining pair for
a smooth rational quartic can be smooth along the whole curve. The only
survivors use singular or non-Cartier behavior, often precisely where the
clean vector-bundle language stops. Smoothness makes the obstruction
accessible; it does not remove it.

The rational quartic remains the best intermediate target because it is the
smallest open smooth example and the next degree pair is now finite algebra. A
general all-smooth attack would currently discard this unusually strong
structure.

## 3. Main results proved in the run

### 3.1 Geometry, three equations, and carrier constraints

Every smooth nondegenerate rational quartic over an algebraically closed field,
in every characteristic, lies on a unique smooth quadric and has type
\((1,3)\) or \((3,1)\). It is cut out set-theoretically by that quadric and two
cubics, so its projective arithmetic rank is at most three.

The quadric cannot be one of a two-equation STCI pair: a degree-\(n\) surface
restricts to class \((n,n)\), never a positive multiple of \((1,3)\).
Adjunction and intersection theory also show that no member of a hypothetical
pair can be smooth along all of the quartic.

For a broad low-genus range, including every smooth rational curve of degree
at least three, the first normal forms of a defining pair must have a
nonconstant common factor after blowing up the curve. The proof supplies the
formerly missing flatness/resultant step. It is a first-stage theorem, not an
iteration theorem.

### 3.2 Exact affine/projective boundary

For a fixed hyperplane at infinity, a projective STCI pair is equivalent to an
affine radical pair whose leading forms are relatively prime. Saturation can
discard a boundary component after it appears, but cannot make the two
homogenized equations into a genuine projective pair. This is the exact point
at which the affine lci theorem stops.

### 3.3 Positive characteristic and constructibility

For \(C_0\), exact pairs were verified in characteristics \(2,3,5,7\), with a
cubic/quartic pair in characteristic three. The construction extends to all
smooth rational quartics in characteristic \(p>0\), yielding degrees
\((3,4p)\) through cuspidal projection and Frobenius descent. The necessary
exponents on the two cubic-cone normalization types were also shown sharp.
An independent audit confirmed the minima after repairing a coefficient
argument in the standard-cusp case: necessity requires three fixed-coordinate
cases and sometimes the \(z^{N-1}\), rather than constant, coefficient.

For any finite-type family and fixed degree pair \((a,b)\), the locus of fibers
admitting such a pair is constructible. Over a one-dimensional arithmetic base
with infinitely many closed points, such as a nonempty open subscheme of the
spectrum of a number ring, occurrence in infinitely many closed fibers is
equivalent to occurrence generically and at all but finitely many closed
fibers. This formulation must not be extended to an arbitrary localization:
a semilocal localization may have only finitely many closed points. The
positive-characteristic pairs have degree growing with \(p\); they do not
specialize to a bounded characteristic-zero pair.

For the explicit monomial quartic \(C_0\), the characteristic-\(p\)
construction can be sharpened when \(p\ge7\). Choose \(b,c>0\) with
\(3b+4c=p\) and \(a=p-b-c\). Then

\[
 x_0x_3^3-x_2^4,\qquad
 x_0^a x_2^b x_3^c-x_1^p
\]

cut out \(C_0\) set-theoretically, giving degrees \((4,p)\). Relative to the
internal uniform \((3,4p)\) construction, this lowers the second degree; it is
not asserted to improve a best published bound. This is a
positive-characteristic construction, not a bounded specialization route to
characteristic zero.

### 3.4 Primitive triples in characteristic zero

Every characteristic-zero smooth rational quartic has

\[
 N_C^*\simeq O(-7)^2.
\]

The Bănică--Forster obstruction to extending a primitive double of type
\(O(-7)\) to a triple was computed over the full moduli of smooth rational
quartics. Its six coordinates have no common zero. Hence no such embedded
primitive triple exists, and in particular no \((3,4)\) complete intersection
exists. The global \((3,4)\) consequence is classical; the stronger
formal-neighborhood exclusion was not located in prior literature.

### 3.5 The exact \((4,5)\) frontier

A hypothetical \((4,5)\) pair has multiplicity five. Degree-\(<6\) thick
carriers are impossible, so the multiple curve is quasiprimitive. The
Bănică--Forster/Boratyński filtration and Euler characteristic leave exactly

\[
 (\deg L,\deg D)=(-7,3)\quad\text{or}\quad(-6,1).
\]

For \(C_0\), the first type is excluded by an exact transition-jet
calculation: the unique epimorphic route reaches a nonzero class in
\(H^1(O(-9))\).

For the second type, the corrected dense chart reduces to one epimorphic
quadruple at

\[
 (r,s)=(0,-1/2).
\]

Using the actual moving coordinate \((z^3+a)/(z^4+b)\), its final obstruction
is

\[
 [-128z^{-1}]\ne0\quad\text{in }H^1(O(-12)).
\]

On the \(b_0=0\) boundary, the second-neighborhood rank equation is
\(1-8t^2+12t^4-72t^6=0\), and the next obstruction coordinate
\(-24t(36t^4+3t^2+1)\) is a unit on that scheme by an exact Bézout identity.
The corrected coordinate-reversing involution covers the corresponding
\(b_1=0,a_0\ne0\) locus.

The formerly missed corner \(a_0=b_1=0\) has precisely three rank-zero
parameters,

\[
 t=-\frac12,\qquad 12t^2+4t+3=0.
\]

At each, the raw second-neighborhood class is identically zero. A proposed
next quotient has \(\delta\in H^0(O(1))\), while its compatible correction is
a global section \(\gamma\in H^0(O(-3))\), hence \(\gamma=0\). Every nonzero
\(\delta\) has a zero; there the transverse ideal becomes
\((m\ell,m^2,\ell^3)\), whose quotient has basis
\(1,m,\ell,\ell^2\) and length four instead of three. The extension is
therefore non-epimorphic and nonflat. This closes type B.

Since the two numerical types were exhaustive, \(C_0\) has no
characteristic-zero degree-\((4,5)\) STCI presentation. Higher degree pairs
remain unresolved. A previous calculation which froze the quotient coordinate
at \(1/z\) was invalid and is not used.

An independent ambient calculation gives a complementary finite reduction
only on a regular-ratio sublocus.
The quartic first-normal image has rank 17 and equations

\[
 P_1=2Q_2,\qquad P_4=2Q_5,\qquad P_7=2Q_8.
\]

The quintic first-normal map is surjective with kernel \(qI_C(3)\) of dimension
seven. The two types correspond to gcd degrees nine and eight. If the quotient
of the two proportional first normal forms is regular, ambient linear
normalization gives

\[
 g_1=z^2f_1,
\]

where \(z^2\) is the unique missing linear-normality section. Contact order
five is then equality of ranks of an explicit seven-column matrix and its
augmentation. Exact minors exclude three one-parameter families in this
regular-ratio sublocus.

The regularity is not automatic. If the first normal forms are
\(f_1=hL,\ g_1=kL\), then \(k/h\) is a rational section and can have poles at
vertical order jumps. The local complete-intersection model

\[
 F=tu+v^5,\qquad G=u
\]

has radical \((u,v)\), constant transverse length five, and first-normal ratio
\(1/t\). It disproves the former universal subtraction step. The nonregular
vertical-divisor strata are nevertheless finite after canonical generator
reduction. Before the higher-neighborhood exclusion, type B split into seven
pole-length strata. The exact Fitting comparison later proves that the
first-normal common vertical divisor is \(A=2D\) scheme-theoretically,
collapsing them to the single counterfactual numerical stratum
\((c,p,\deg Z)=(2,6,10)\). This identity is independently useful, but the
separate formal-neighborhood argument above is what excludes the degree pair.

### 3.6 Thick sextics

For a smooth rational quartic,

\[
 h^0(I_C^{(2)}(6))=23,
\]

with an 18-dimensional \(q\)-divisible subspace and five-dimensional quotient
\(H^0(Q,O_Q(4,0))\). Degree six is the first non-\(q\)-divisible thick degree,
and integral sextics singular exactly along \(C_0\) exist.

Two non-\(q\)-divisible thick sextics cannot form a defining pair in
characteristic zero. For one thick sextic, an irreducible Cartier preimage of
the curve on the normalization is impossible. In the content-free split case,
any mate leaves only

\[
 d=0,\quad(m_1,m_2,b)=k(5,1,4),
\]

or

\[
 d=1,\quad(m_1,m_2,b)=k(11,1,8).
\]

Cartier branches exclude both. Normality alone does not: in the local model
\(xy=e^n\), Mumford branch intersection is \(1/n\), correcting an earlier
false shortcut.

The true first-normal image has dimension 22. For \(C_0\) it contains split
divisors of every type \(d=0,\ldots,5\), and an ambient sextic can be integral
despite split normal divisor and square discriminant. Thus the normal cone by
itself does not finish the problem.

Using Mumford numerical pullbacks on a resolution, Hodge-index equality gives
a stronger multiplicity restriction. Group the full Cartier cluster over each
distinct root of the residual binary quartic, including its multiplicity and
all exceptional components. If the root has multiplicity \(\mu\),
proportionality forces the low branch to meet the cluster in \(\mu/4\) for
\(d=0\), or \(\mu/2\) for \(d=1\). Integrality leaves only the root partition
\([4]\) when \(d=0\), and \([4]\) or \([2,2]\) when \(d=1\). Thus the
squarefree case and all other partitions are closed, but these surviving
multiple-root configurations remain.

The surviving residual quartics are squares.  Consequently every carrier in
this split frontier has the exact ambient form

\[
 F=T^2+qK,\qquad T\in I_C(3),\quad K\in I_C(4).
\]

Every residual-root point selected by the low branch is singular on the first
strict transform.  The mate parameter must, however, be retained: it forces
only \(4k\Gamma_{\mathrm{low}}\) Cartier for \(d=0\), or
\(10k\Gamma_{\mathrm{low}}\) Cartier for \(d=1\).  Cancelling \(k\) is invalid
in a torsion local class group.  For example, a two-simple \(d=1,[4]\)
allocation with ordinary \(A_3\) germs merely forces \(k\) even.  It is not
unconditionally excluded.  For \(C_0\), the exact first-normal equations do
exclude a \(d=1,[4]\) root at either totally ramified ruling by forcing
vertical content.  A previously missed \(d=1,[2,2]\) boundary with residual
roots at the two ramified rulings has an exact content-free first-normal
survivor, so that locus cannot be discarded at this order.  The general
surviving loci remain open.

A separate conditional theorem closes the clean split-conductor model. If the
sextic normalization is smooth and

\[
 I_CO_S=O_S(-\Gamma_1-\Gamma_2)
\]

with no extra conductor component, the source double-point formula and
adjunction force \(\Gamma_1\Gamma_2=10\); the mate equations then have no
rational positive solution. This also gives
\(\chi=2,p_g=1,q=0,K^2=-4,c_2=28\). Singular normalization, extra conductor,
or point-supported noninvertibility are genuine unresolved loopholes.

### 3.7 The mixed \((4,6)\) pair

A hypothetical pair gives a quasiprimitive multiplicity-six lci.  Its
Bănică--Forster pieces necessarily are

\[
 O,L,L^2(D_2),L^3(D_3),L^4(D_2+D_3),L^5(D_2+D_3),
 \qquad 0\le D_2\le D_3.
\]

Writing \(l=\deg L\) and \(d_i=\deg D_i\), Gorenstein duality and
\(\chi(O_X)=-72\) give

\[
 5l+d_2+d_3=-26.
\]

The quotient \(O(-7)^2\twoheadrightarrow L\) forces \(l=-7\) or \(-6\).
There are eight raw numerical types; P-010 removes \((-7,0,9)\), leaving seven
necessary types.  No realization is asserted.

The horizontal degree is \(e=l+7\), so every actual pair has \(e=0\) or \(1\).
The earlier exact incidences at \(e=2,3\) remain useful first-normal controls,
but cannot extend to multiplicity-six lci curves.  In the nonregular branch,
P-031 now leaves exactly

\[
 e=0,\ 1\le p\le8;\qquad e=1,\ 1\le p\le7,
\]

for 15 coarse pole-divisor strata rather than 36.  Exact quadric intersection
gives residual excess-tangency budget \(4+p\), but does not itself contradict
any of those strata.

### 3.8 An exact complement reformulation

For every integral curve \(C\subset\mathbf P^3\), with
\(U=\mathbf P^3\setminus C\), the following are equivalent:

- \(C\) is an STCI;
- \(U\) admits a nonconstant morphism to \(\mathbf P^1\);
- some \(O_U(d)\), \(d>0\), is generated by two global sections.

One direction is the ratio of two equal-degree defining forms. Conversely,
codimension-two purity gives \(\operatorname{Pic}(U)\simeq\mathbf Z\), and
sections extend across \(C\); their projective common zero set is then exactly
\(C\). The graph closure is the corresponding Rees blowup, a hypersurface in
\(\mathbf P^3\times\mathbf P^1\). This formulation is exact but does not by
itself construct the morphism.

### 3.9 Local cohomology

For \(M=H^2_{I_{C_0}}(S)\), the explicit classes
\(u=xz/(qB)\) and \(v=yw/(qB)\) have no common homogeneous cyclic ancestor
with multipliers of degree at most three.  Any surviving equal-degree pair
has degree at least four, lies in \(I_{C_0}\), and has proportional first
conormal symbols.  The proof is all-stage: a finite-Laurent completion at
each zero of a restriction factor forces both multipliers into the curve
ideal, and the cubic rank-one locus consists only of scalar or
\(q\)-divisible pairs.

Degree four is genuinely different.  For every \(\lambda\ne0\),

\[
 F_\lambda=xA+\lambda y^2q,\qquad
 G_\lambda=yA+\lambda xzq
\]

are ambient-coprime quartics with first-symbol rows
\((1,\lambda t^2)\) and \((t,\lambda t^3)\).  Their ratio is nonconstant.
This disproves the shortcut that rank-one first symbols plus coprimality force
a common factor or constant ratio.  It does not, however, survive the global
direct-limit equations.  At every diagonal stage \(N\ge2\), two sparse
coefficient functionals annihilate the \((q^N,B^N)\) correction spaces and all
pairs \((F_\lambda h,G_\lambda h)\), but evaluate to \(-1\) on the target pair
representing \((u,v)\).  The identities are symbolic in \(N\), integral in
\(\lambda\), and compatible with multiplication by \(qB\).  Hence this entire
explicit family has no common ancestor at any stage.  Other degree-four
rank-one pairs remain open, and no non-quasi-cyclicity theorem has been
obtained.

### 3.10 Singular-support replacement

For an integral carrier \(X\) with normalization \(\nu:S\to X\), a mate is
equivalent to an effective Cartier divisor

\[
 A=\sum_i m_i\Gamma_i\sim bH
\]

supported on the reduced inverse image of \(C\), with every \(m_i>0\), whose
canonical section descends through the full conductor square. Equivalently,
its class in

\[
 H^0(X,(\nu_*O_S/O_X)\otimes O_X(b))
\]

must vanish. Linear equivalence on \(S\) alone is insufficient: in the
transverse cusp \(K[[t^2,t^3]]\subset K[[t]]\), the normalized section \(t\)
does not descend although \(t^2\) and \(t^3\) do. Every mate satisfies

\[
 ab=\deg(C)\sum_i m_i\delta_i.
\]

This criterion works for singular \(C\), singular normalization data, and
carriers singular generically along \(C\). It isolates the missing information
as conductor gluing.  More precisely, if
\(M_A=\nu_*O_S(-A)\) and \(I_A=O_X\cap M_A\) inside the total quotient sheaf,
then \(M_A/I_A\hookrightarrow\nu_*O_S/O_X\) is the conductor-supported
descent defect.  Normalized rank-one data without this intersection condition
are insufficient.

In characteristic zero, P-015 also extends unchanged to any integral,
possibly singular \(C\) when the minimum carrier is regular at the generic
point of \(C\). If \(d=\deg C\), then

\[
 eC\sim nH,\qquad n=de/a\ge a,\qquad e\ge a^2/d.
\]

Thus smoothness of the support was never needed for that branch; generic
regularity of the carrier is the real boundary.

### 3.11 Global Chow, K-theory, and graded-Gorenstein encodings

For forms \(F,G\) of degrees \(a,b\) without a common factor, restrict them to
the universal line over \(\operatorname{Gr}(2,4)\). The determinant of the
twisted pushed-forward Koszul complex is the binary resultant
\(R_{F,G}\), a section of \(O(ab)\). Since the complete intersection is pure,

\[
 V(F,G)_{\mathrm{red}}=C
 \quad\Longleftrightarrow\quad
 R_{F,G}=\lambda\operatorname{Ch}_C^{ab/\deg C}.
\]

This is a classical cycle-level reformulation, not an existence theorem, but
it is a global exact certificate independent of a first-normal frame. For
\(C_0\), the Chow form is an explicit 10-term Pluecker quartic, verified
symbolically against the full binary resultant. A \((4,5)\) pair must satisfy
\(R_{F,G}=\lambda\operatorname{Ch}_{C_0}^5\).

Restricting this identity to the line pencil

\[
 [x_0:x_1:x_2:x_3]=[\gamma U:0:V:\beta U]
\]

gives \(\operatorname{Ch}_{C_0}=-\beta\gamma^3\), so the restricted
resultant must be \(\mu\beta^5\gamma^{15}\). Exact linear algebra and
resultant order then exclude every quartic in

\[
 I_{C_0}(4)\cap(x_1,x_2x_3,x_3^2)_4
\]

and every quintic in

\[
 I_{C_0}(5)\cap(x_1,x_3^2,x_2^2x_3)_5;
\]

these vector spaces have dimensions 13 and 28.  After dividing the forced
\(\beta\)-factor, the specialized forms retain a common \(V\)-root of
multiplicity at least one or two, so the resultant has order at least six
rather than five.  The coordinate-reversed spaces are excluded as well.

One pencil is not exhaustive.  An explicit absolutely irreducible quartic and
quintic in the record have resultant exactly
\(-2\beta^5\gamma^{15}\) on this pencil, but zero resultant on the reversed
pencil because both restrictions share \(U\).  Thus the Chow route supplies
strong exact family exclusions and diagnostics, while the independent
multiple-structure proof supplies the full no-\((4,5)\) theorem.

The ordinary stable shadow is completely coarse:

\[
 K_0(\mathbf P^3\setminus C)
 \simeq\mathbf Z[u]/(u^3,\deg(C)u^2),
\]

and the class relation of a degree-\((a,b)\) Koszul pair is exactly
\(\deg(C)\mid ab\). This necessary condition is nowhere near sufficient and
does not rule out higher or unstable obstructions.

Finally, STCI is equivalent to existence of an \(I_C\)-primary height-two
graded Gorenstein ideal, or an arithmetically Gorenstein codimension-two
thickening. Hilbert--Burch makes such an ideal a two-generator complete
intersection. Merely local Gorensteinness is insufficient.

## 4. Failed approaches and lessons

The following should not be repeated without new information:

- ordinary local-cohomology vanishing and complement cohomology stop exactly
  at the bound compatible with two principal affine opens;
- Picard, Chow, and ordinary \(K_0\) retain only line-bundle degree and Bezout
  divisibility; the missing condition is unstable two-generation;
- the Rao module of the reduced curve is not an STCI obstruction;
- binomial arithmetic-rank results do not exclude arbitrary equations;
- saturation and naive homogenization do not solve the boundary problem;
- smooth or ordinary carriers omit the singular-along-\(C\) escape;
- first-normal factors do not imply ambient factorization;
- the actual sextic normal image permits every split type;
- first-normal \((4,6)\) incidence is nonempty in all regular-ratio classes;
- proportional first normal forms need not have a regular quotient, so neither
  global subtraction nor the lists \(g_1=z^2f_1\) and \(e\le3\) are universal;
- normality does not make split branches meet with ordinary intersection ten;
- a frozen quotient coordinate corrupts type-B transition jets;
- the archived claim of 24 independent approaches was behaviorally false:
  audit found about ten substantive representations, many cosmetic variants.

The recurring structural lesson is that the obstruction lives one level beyond
the visible first representation: at infinity rather than on the affine chart,
in higher jets rather than the first normal cone, in local class-group
corrections rather than ordinary intersections, and in compatible ancestors
rather than vanishing of local cohomology.

## 5. Archive assessment

The prior Math Automation repository was used only as a research archive. Its
useful contributions were candidate formulas, quartic generators, normal-
bundle leads, blowup numerics, and a map of attempted approaches. Every claim
promoted here was rederived, independently audited, or checked exactly.

Important corrections include:

- the root problem is general, while most archive work concerns only \(C_0\);
- architectural labels did not guarantee independent mathematical behavior;
- several conditional calculations had been described too broadly;
- the characteristic-two normal bundle differs from the characteristic-zero
  bundle;
- the split-sextic normality shortcut was false;
- the type-B frozen-coordinate calculation was false;
- first-normal success was repeatedly mistaken for higher-contact evidence.

The archive machinery itself was not extended.

## 6. Verification status

Fourteen exact SymPy verifiers are preserved in `research/computations`, plus
the mixed-degree verifier under `research/scratch/degree6`, for 15 executable
checks in total. They cover the explicit quartic equations, normal bundle,
primitive obstructions, positive-characteristic descent, degree-six spaces,
Chow form and pencil restrictions, the type-B dense/boundary/corner
certificates, the split \([2,2]\) boundary survivor, and the degree-four
local-cohomology counterfamily and all-stage certificate. The scratch
verifier remains conditional on the regular-ratio normalization. Their exact
scope and important assertion-to-prose boundaries are documented in
`computations/README.md`.

Exact calculation proves the identities encoded in a script; it does not prove
that chosen equations exhaust an unstated parameter space. Universal claims in
the record have separate geometric reductions or are explicitly labeled open.

## 7. Epistemic ledger

### KNOWN

- current open status through the dated literature search;
- the classical affine lci, ACM, rational-quartic degree exclusions, normal-
  bundle, multiple-structure, Jaffe, and almost-Cartier theorems cited in the
  literature ledger.

### PROVED HERE

- P-002 through P-043 in `RESEARCH_RECORD.md`, exactly with their stated
  hypotheses and status qualifiers;
- in particular, both \((4,5)\) quasiprimitive types are excluded, giving the
  degree-pair theorem P-040, but not a non-STCI theorem in all degrees;
- the residual-root partition restriction assumes the split/no-vertical setup;
  it leaves \([4]\) for \(d=0\) and \([4]\), \([2,2]\) for \(d=1\), and is not
  an exclusion of all thick sextics; P-041 adds a torsion-corrected sharpening.

### COMPUTATIONAL EVIDENCE

- modular failures of selected higher-degree local-cohomology ancestor systems;
- generic rank behavior outside the exact determinantal certificates;
- unsaved higher-jet samples on surviving split-sextic charts.

### CONJECTURAL

- the surviving \([4]\) and \([2,2]\) split-sextic loci are excluded by higher
  jets;
- the remaining degree-four rank-one local-cohomology pairs are obstructed at
  higher direct-limit order;
- \(C_0\) is not an STCI in characteristic zero in any degree pair.

### SPECULATIVE

- a higher-degree Hartshorne--Polini ancestor obstruction may prove
  non-quasi-cyclicity;
- control of Jaffe's type sequence might exclude a broad low-genus class, but
  positive characteristic shows that it must detect Frobenius.

## 8. Highest-value next work

1. Attack the seven necessary multiplicity-six Bănică--Forster types for a
   hypothetical \((4,6)\) pair and match them with the 15 viable pole strata.
2. Parameterize the nonregular order-\((1,1)\) branch of \((4,6)\), while
   separately imposing higher transverse jets in the two viable regular-ratio
   classes \(e=0,1\).
3. Analyze only the residual partitions \([4]\) for \(d=0\), and
   \([4]\), \([2,2]\) for \(d=1\), left by the strengthened Hodge argument.
4. Classify the remaining degree-four proportional first-conormal multiplier
   pairs; P-043 already excludes the explicit P-039 family at every stage.
5. Keep a separate general/singular-curve lane based on normalization,
   conductor, and almost-Cartier data; smooth success would not settle the
   original problem.

These tasks are independent enough for separate lanes, but the workstation
should use closed batches of at most seven read-only, nondelegating workers
plus the primary process, eight total, while monitoring aggregate memory.
The 64-process configuration is known unsafe and caused a crash. Each lane
must own a distinct representation and return proof-grade certificates rather
than cosmetic variants.

## Post-cutoff continuation pointer (2026-10-05)

This report's synthesis has a 2026-09-30 cutoff and is retained as a historical
closeout. A later characteristic-zero (e=2) quartic-carrier branch is
recorded in `RESEARCH_UPDATE_2026-10-05.md` and
`notes/2026-10-05-e2-full-obstruction.md`. It proves the ambient stabilizer
(mathbf G_mtimesmathbf Z/2), excludes the full (b=0) three-parameter
primitive-quadruple family, and independently regenerates the generic
four-parameter cubic obstruction. Importantly, the proposed universal
implication (Omega=0RightarrowDelta=0) is **FALSE**: an explicit
basepoint-free one-parameter family extends to a primitive quadruple. This is
not a quartic-carrier or STCI construction; it only shows that this first
nontrivial extension obstruction is insufficient.
