# Prescribed singular carriers and residual curves through their singularities

Date: 2026-10-28. Branch: `codex/intersections-containing-quartic-2026-10-27`.
**Status: independently reviewed provisional research contribution; no
canonical promotion.** See the [independent
audit](2026-10-28-singular-carrier-audit.md). This is a construction and an interpretation of
containing intersections. It supplies no characteristic-zero STCI pair for
the fixed quartic.

The local blowup control in §4.1 and the explicit degree bound in §7 were
added after that cross-audit; they pass the separate root integration
addendum in the same audit.

## 1. Question, inputs, and contribution

Work over the complex numbers with the fixed smooth curve

\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3.
\]

What can a containing intersection look like when a chosen carrier has a
non-Cartier point on C? In particular, can high local Cartier index be
realized by actual homogeneous surfaces, and how does a residual curve
compensate for it?

Retrieval followed [INDEX](../INDEX.md), [MAP](../MAP.md), the
[arbitrary-degree synthesis](2026-10-27-arbitrary-degree-absorption-synthesis.md),
the [conductor continuation](2026-10-27-absorption-characteristic-conductor-interface.md),
and the exact scopes of [R-0002](../results/cartier_singleton_lift.md),
[R-0003](../results/fixed_carrier_conductor_criterion.md), and
[R-0034–35](../results/normal_carrier_index_socle.md). No accepted proof
was rerun. The all-degree Serre partial-transfer construction and the
twisted-cubic semi-invariant benchmark are inherited, not contributions
of this note.

The new project-specific synthesis has three concrete parts:

1. For every integer r>=2 and chosen P in C, actual sufficiently
   high-degree normal hypersurfaces containing C can be constructed with
   exactly one singular point, an A_(r-1) point at P, where C has local
   Cartier index exactly r.
2. On these carriers, actual high-degree mates realize mC plus a smooth
   integral residual for each 1<=m<r. The residual passes through P and
   cancels the nontrivial local divisor class. Its marked attachment has
   length one there, while attachment to the full thick primary component
   has length m.
3. A standard Noether–Lefschetz theorem computes the class groups of the
   very general members of this construction. It separates local
   index from the extra global divisor relation that a proposed
   sole-support construction would have to impose.

These are applications of known local singularity and linear-system
tools, not claims of literature novelty. The live literature check below
also found a new October 2026 theorem about very general surfaces
containing ordinary powers of I_C; its Picard-group conclusion must be
kept separate from almost-Cartier divisor questions.

## 2. The marked local construction

Use regular local coordinates (t,y,z) in the ambient smooth threefold
with C=(y,z), and prescribe

\[
 f_0=t y-z^r.                                             \tag{1}
\]

The carrier has an A_(r-1) singularity. At the generic point of C, t is
a unit and y=z^r/t, so the carrier is smooth there. In its completed local
ring R, put p=(y,z). The standard A-type class-group calculation gives

\[
 \operatorname{Cl}(R)=\mathbf Z/r,
 \qquad [C]=\pm1.                                        \tag{2}
\]

Thus the local Cartier index is r. The sign in identifying the generator
does not matter; below choose [C]=1. The natural map from the algebraic
local class group into the completed local class group is injective, so
the index computed in completion is also the algebraic local index.

### Stability retaining the marked curve

This is a statement about the pair, not just the unmarked singularity.
If

\[
 f=f_0+h,\qquad h\in(y,z)\cap(t,y,z)^{r+1},                \tag{3}
\]

then a formal change of coordinates preserving the ideal (y,z) changes
f, up to a unit, to (1). Here is a direct proof. Remove perturbation
monomials in increasing total degree. A monomial containing y can be
removed by changing t; a remaining monomial containing t has a z factor
because f belongs to (y,z), and can be removed by changing y by a multiple
of z. These changes preserve (y,z), have order at least two, and introduce
only higher-degree errors. The changes converge in the maximal-ideal
topology. The remaining series is ty-z^r times a one-variable unit in
the z^r term, which is absorbed into z using its r-th root. Characteristic
zero ensures that root exists. The resulting change still preserves
(y,z).

The same proof works after dividing f by a unit. Consequently a section
with local equation u*f_0+h, where u(P) is nonzero and
h belongs to (y,z)*(t,y,z)^r, has the required marked local type.

## 3. Global carriers with arbitrary prescribed local index

**Construction proposition.** Fix P in C and r>=2. There is a coherent
ideal sheaf I_B supported on C, equal to I_C away from P, such that for
every sufficiently large a a general member of
|H^0(I_B(a))| is an integral normal surface S of degree a, smooth away
from P, with completed marked pair (S,C) at P given by (1). In particular
the actual local Cartier index of C at P is r, and C is Cartier at every
other point of S.

**Proof.** In the local ring at P prescribe

\[
 I_{B,P}=(f_0)+\mathfrak m_P^r I_{C,P};                    \tag{4}
\]

away from P use I_B=I_C. The prescription is a coherent ideal: equivalently
take the inverse image in I_C of the submodule generated by f_0 in the
finite-length quotient I_C/(I_C I_P^r). Local coordinates can be chosen
algebraically, and the finite jet of f_0 determines this quotient
prescription. It is therefore not an instruction to algebraize an entire
unrelated formal surface.

For a large twist the ideal and the finite jet quotients needed here are
generated by global sections. A general member has a unit coefficient of
f_0 in (4), so §2 supplies the completed marked A_(r-1) pair at P.
Off C, Bertini applies to the base-point-free system. Along C minus P,
the first-normal evaluations generate the rank-two conormal bundle. A
general section of a generated rank-two bundle on this curve has no
zero: the incidence of a point and a vanishing section has codimension
two in the section space before the one-dimensional point is varied.
Thus S is smooth there too. An isolated A-type singularity is normal.
A reducible projective hypersurface has a curve of intersections between
its surface components, and a nonreduced hypersurface is singular along
a surface. The established singular locus excludes both, so S is
integral. This proves the proposition.

For a completely explicit coordinate source at the endpoint
P=[1:0:0:0], the affine chart x0=1 has

\[
 t=x_1,\quad y=x_2-x_1^3,\quad z=x_3-x_1^4.
\]

These are polynomial coordinates with C=(y,z); ty-z^r is an actual
polynomial in the ambient affine coordinates and can be homogenized.
The general large-degree perturbation in (4), rather than this one
homogenization alone, guarantees the asserted global smoothness.

Several points and indices can be prescribed by the same disjoint finite
jet construction. The one-point case already supplies arbitrary high
indices and is the scope used below.

## 4. Actual residual curves cancel local classes

On S let J_m=O_S(-mC) be the divisorial ideal, equivalently the symbolic
power p_C^(m). For 1<=m<=r its completed stalk at P is

\[
 \widehat{J_m}_P=(y,z^m).                                \tag{5}
\]

One can check (5) without guessing a primary decomposition. Its quotient
is k[[t,z]]/(z^m), which is (z)-primary and has generic C-length m;
localization at p_C is the ideal of valuation at least m. The ideal is
therefore precisely the symbolic power. The case m=r is principal on S
because z^r=ty.

For 1<=m<r consider first the exact local mate

\[
 g=y+z^m.
\]

Eliminating y gives the plane equation

\[
 (f_0,g)=(y+z^m,\ z^m(t+z^{r-m})).                       \tag{6}
\]

Thus its full C-primary component and residual component are

\[
 I_{T_m}=(y,z^m),\qquad
 I_D=(y+z^m,t+z^{r-m}).                                  \tag{7}
\]

The residual is smooth, parametrized by z, and meets C only at P in
this local germ. Exact attachment lengths are

\[
 \operatorname{length}(C\cap D)_P=1,
 \qquad \operatorname{length}(T_m\cap D)_P=m.             \tag{8}
\]

Indeed substitute the equations of D: I_C becomes (z), whereas I_T
becomes (z^m). No exceptional curve or reduction is used in this
calculation. These are actual downstairs components of the complete
intersection. The same conclusions hold for g=A*y+B*z^m with A,B units:
after eliminating y the residual factor has nonzero t derivative, and
the two ideals restrict to (z) and (z^m) on that smooth residual.

**Global mate proposition.** For each carrier of §3 and each fixed
1<=m<r, for every sufficiently large b a general section of J_m(b)
lifts to an actual homogeneous G_b. Its intersection with S has cycle

\[
 [V(F_a,G_b)]=m[C]+[D],\qquad \deg D=ab-4m,              \tag{9}
\]

where D is smooth integral and has the local behavior (8) at P.

**Proof.** A large twist of the coherent rank-one ideal J_m is generated
by global sections, including its two minimal completed generators in
(5). A general section has unit coefficients of both there. Thus (6)–(8)
hold with units. Away from P, J_m is the line bundle O_S(-mC). After
a further hyperplane twist its section system separates points and
tangent vectors on S minus P: multiply sections of a generated smaller
twist by ambient linear forms. Its map is birational onto a surface,
so the usual characteristic-zero Bertini irreducibility and smoothness
statements give a smooth integral residual off P. The local computation
shows that its closure is smooth at P as well.

The exact generic order is m; this is also visible in (6). The full
C-primary component is the scheme defined by J_m. Since S is a
hypersurface, H^1(P^3,O(b-a))=0 and every section of O_S(b) lifts to
an ambient homogeneous G_b. The section is nonzero on the integral
surface, so the ambient pair is proper. This proves (9) for actual
homogeneous equations, rather than just formal jets.

The class identity, valid for every proper mate with generic order m,
is

\[
 [D]=b[H]-m[C]\quad\hbox{in }\operatorname{Cl}(S),
 \qquad [D]_P=-m\quad\hbox{in }\mathbf Z/r.               \tag{10}
\]

If r does not divide m, a residual divisor must pass through P: a
divisor missing P has trivial local class. Formula (7) realizes that
necessary cancellation by a smooth curve. If m=r a local supported
equation y already exists, and a general section of J_r(b) can have
residual avoiding P. Thus the change in attachment has a precise local
class-group meaning.

### 4.1. Integration control on the blowup graph

This is an exact local test of the actual-cycle dictionary in the
[two-projection note, §4](2026-10-28-blowup-residual-geometry.md), not a
new existence assertion. Take 2<=m<r and the literal local pair
(f_0,g)=(ty-z^r,y+z^m). Both equations have normal order one in I_C.
On the z-chart of Bl_C, write y=u*z. Their strict transforms are

\[
 \widetilde f=t u-z^{r-1},\qquad
 \widetilde g=u+z^{m-1}.
\]

Thus their actual scheme intersection is

\[
 W=V\bigl(u+z^{m-1},\ z^{m-1}(t+z^{r-m})\bigr).          \tag{10a}
\]

The component e=V(u,z), parametrized by t, lies in the exceptional
divisor and dominates C. Its generic multiplicity is m-1. The other
component is the strict transform of the actual residual D:

\[
 \widetilde D=V(u+z^{m-1},t+z^{r-m}),\qquad
 [W]=(m-1)[e]+[\widetilde D].                             \tag{10b}
\]

The primary component along e has ideal (u,z^{m-1}). Its scheme union
with the displayed residual is exactly W, since the two factors of the
plane equation after eliminating u are relatively prime. Thus the cycle
multiplicity in (10b) has a specified primary scheme behind it.

The other blowup chart has z=v*y and strict equations
t-y^{r-1}v^r and 1+y^{m-1}v^m. The second is a unit along the
exceptional divisor y=0. Hence no additional vertical exceptional fiber
occurs there. On the first chart the exceptional intersection is
supported on e and the one attachment point of the residual. There is
no extra vertical curve over P.

Pushing (10b) down gives (m-1)[C]+[D], precisely the graph formula
with generic intersection multiplicity m and normal orders (1,1).
The exceptional component measures thickness along C, while
\(\widetilde D\) is an actual residual curve. This control ties the
singular-carrier construction to the global graph interpretation
without inferring residual support from exceptional geometry.

## 5. Full-primary genus and the global attachment budget

For 1<=m<=r the primary curve T_m is primitive: locally it is contained
in a smooth surface and has ideal (y,z^m), including at P. The first
normal class of F has a simple common zero at P and no others. Its
saturation in N^*_(C/P3) is O_C(-a)(P). Using the accepted determinant
degree deg N^*=-14 (equivalently [R-0020](../results/quartic_conormal_characteristic_jump.md)),
for m>=2 the conormal line of C in T_m has degree

\[
 \ell=4a-15.
\]

The ordinary primitive layers have line bundles L^i, 0<=i<m, where
deg L=ell. Consequently

\[
 \deg T_m=4m,\qquad
 p_a(T_m)=1-m-\frac{m(m-1)}2(4a-15).                    \tag{11}
\]

This formula concerns the full scheme, not its rational reduced support.
For m=1 it is the direct identity p_a(C)=0, without introducing a
conormal line for C inside itself.
For the general residual constructed above, the standard linkage
attachment identity in the [reviewed October 27 attachment
note](2026-10-27-absorption-attachment-module.md) gives

\[
 \operatorname{length}(T_m\cap D)
 =m\bigl(4b+1+m(4a-15)\bigr).                           \tag{12}
\]

The local contribution m in (8) is part of this total. This is a new
test family for the inherited full-primary identity; it does not alter
that identity or identify full attachment with reduced attachment in
other families. For m=1, (12) recovers the familiar total boundary degree
4(a+b)-14.

## 6. What local index does and does not construct globally

The base scheme B of §3 has dimension one, reduced support C, and
embedding dimension at most two away from the one point P. For all
sufficiently large a, the hypotheses of Brevik–Nollet's base-locus
Noether–Lefschetz theorem hold. Hence for a **very general** complex S
in this particular system,

\[
 \operatorname{Cl}(S)=\mathbf Z[H]\oplus\mathbf Z[C].     \tag{13}
\]

Since P is the only singularity and C maps to a generator of its local
class group, the local-to-global Cartier sequence gives

\[
 \operatorname{Pic}(S)=\mathbf Z[H]\oplus\mathbf Z[rC].   \tag{14}
\]

Thus arbitrary prescribed local index and actual residual geometry are
available in a family whose very general global class group is explicit.
Even when n is divisible by r, the line bundle nC-bH remains nontrivial
for every positive n,b on these very general carriers. A sole-support
section on a normal integral carrier would require precisely a positive
relation n[C]=b[H]. Such a construction must therefore impose additional
global geometry beyond the chosen local singularity.

This is a statement about the specified very general family, not a
uniform exclusion of all high-index carriers. Special members can have
different class groups; determining actual effective class relations
there is a constructive question. The proof gives no degree threshold
for all possible STCI carriers, no conclusion for nonnormal carriers,
and no reason to aggregate this with R-0035 into an unrestricted theorem.

## 7. Primary literature checked live on 2026-10-28

* Brevik–Nollet, [*Noether–Lefschetz theorem with base locus*, arXiv
  0806.1243v3, Theorem 1.1](https://arxiv.org/pdf/0806.1243), inspected
  printed p. 2. Its assumptions include dimension at most one, embedding
  dimension at most two away from finitely many points, generation of
  I_B(a-1), and one further stated condition; here the sufficient option
  H^0(I_B(a-2)) nonzero holds for a large twist. The conclusion is for
  **very general complex** surfaces and computes their Weil class group.
  Equations (13)–(14) are an application, not a new Noether–Lefschetz
  theorem.
* Brevik–Nollet, [*Picard groups of normal surfaces*, J. Singularities 4
  (2012), 154–170](https://faculty.tcu.edu/snollet/research/brevik-nollet.pdf),
  inspected Method 1.2 and §2.1, especially Example 2.1. These explicitly
  retain the injection from the algebraic local class group into the
  completed one and the classes of the marked curves in A-type
  singularities. An unmarked analytic type alone does not identify the
  algebraic local class group or a particular divisor class.
* Brevik–Nollet, [*Noether–Lefschetz theory and surfaces containing a
  multiple curve*, Nagoya Math. J. 261 (2026), e54,
  DOI 10.1017/nmj.2026.10139](https://doi.org/10.1017/nmj.2026.10139),
  official full text inspected, published online **19 October 2026**.
  Theorem 1.1 concerns smooth complex threefold X with H^1(O_X)=0,
  smooth connected C, ordinary thickening I_Z=I_C^q with q>=2, and very
  general sufficiently high-degree Y containing Z. It proves
  Pic(X)→Pic(Y) is an isomorphism. In P3 this gives Pic(Y)=Z[H].
  These Y are nonnormal along C. The theorem computes line bundles;
  it does not say every Weil/almost-Cartier multiple of C is a line
  bundle, classify the full inverse support, or decide the STCI question.

For this fixed quartic the sufficient conditions in that paper's
Remark 1.2 give an explicit specialization: **q>=2 and d>=4q suffice**
for its very-general Picard conclusion in P3. Indeed I_C(3) is globally
generated: on the smooth containing quadric Q, C has bidegree (1,3), so
the quotient of I_C(3) by q_quadric*O(1) is O_Q(2,0), generated by its
three sections; the ambient lifting sequence has H^1(O(1))=0. Twisting
preserves generation, so I_C(floor(d/q)-1) is generated if d>=4q.
The other condition is

\[
 H^0\bigl(I_C^{q-1}(d-4)\bigr)\ne0.
\]

It holds because q_quadric^(q-1) has degree 2(q-1), and it can be
multiplied by a nonzero form of degree d-2q-2, which is nonnegative
in the stated range. Here q_quadric denotes the containing quadratic
equation, whereas q is the thickening exponent. The resulting
conclusion remains exactly Pic(Y)=Z[H] for a **very general** degree-d
surface containing I_C^q. This does not turn C into a Cartier divisor
on the nonnormal Y or compute its almost-Cartier divisor group.

The October 2026 paper reinforces a useful split in interpretation:
general carriers containing the reduced curve, general carriers with
prescribed isolated singularities, and general carriers containing an
ordinary thick neighborhood have different divisor theories. Passing
from one parameter space to another changes the mathematical question.

## 8. A bounded constructive next step

The present family realizes high index and fully controlled residual
gluing. Its next useful test is to prescribe a **global** relation at the
same time as the local models: choose a special normal carrier with a
known divisor presentation, identify C as a particular divisor rather
than merely an analytic branch, and compute whether nC-bH is trivial
with an actual section. Matrix factorizations or a finite cover could
present such a class relation, but no presentation is supplied here.

One must retain both outputs in any proposed test: the actual local
class cancellation of its residuals and the global class of those
residuals. Increasing r alone solves neither the global relation nor
homogeneous equation construction for a sole-support endpoint. The
residual family (6)–(12) remains useful independently of that endpoint.

Independent review should reconstruct the marked-coordinate stability,
the global finite-jet realization, symbolic ideal (5), the Bertini
argument for actual residuals, the primitive genus formula, and the
literal complex/very-general hypotheses in (13).
