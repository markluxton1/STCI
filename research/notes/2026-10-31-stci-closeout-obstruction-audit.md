# Closeout audit: the actual quadric-residual obstruction in every degree margin

October 31, 2026. Reviewer: independent `obstruction_audit` lane. **Final
verdict: PASS with the literal ordinary-root and attachment hypotheses
below, including the nonempty dense-open statement in every full actual
source.** The component-slope necessary condition also passes on its
stated ordinary locus. These are independently reviewed **provisional**
claims; this audit does not promote a canonical result or alter the
unrestricted open question.

The source under review is
[the obstruction proposal](2026-10-30-stci-game-obstruction.md), §§2–4.
The [geometry review](2026-10-30-stci-game-geometry-review.md), §5,
already reviewed the critical degree \(a=3m\); its §6 left the extension
unreviewed. The present audit resolves that outstanding extension rather
than treating the source's final assertions as proof of completion.

## 1. Scope, accepted inputs, and completion evidence

Throughout, \(k\) is algebraically closed of characteristic zero,

\[
C=C_0=[s^4:s^3t:st^3:t^4],\qquad
Q=V(q),\quad q=x_0x_3-x_1x_2,
\]

and \(V_{a,m}=H^0(\mathbf P^3,\mathcal I_C^m(a))\), where powers are
sheaf powers, equivalently saturated homogeneous powers. Fix integers
\(m\ge1\), \(a\ge3m\). The mate degree \(b>0\) is unrestricted.

Accepted premises are the conormal splitting
[R-0020](../results/quartic_conormal_characteristic_jump.md),
\(N_C^*=\mathcal O(-7)^2\), and the quadric-flag description and
actual source calculation in the
[independent freedom audit](2026-10-28-stci-search-freedom-independent-audit.md).
Those inherited proofs and their finite controls were not rerun. The
actual divisor on \(Q\simeq\mathbf P^1\times\mathbf P^1\) has
\([C]=(1,3)\), while \(\mathcal O_{\mathbf P^3}(1)|_Q=(1,1)\).

The saved
[Macaulay2 control](../computations/stci_game_obstruction_2026_10_30.m2)
and its [output](../computations/stci_game_obstruction_2026_10_30.txt)
were inspected. The output reaches all four terminal markers, ending
in `GAME_OBSTRUCTION_GEOMETRIC_CONTROLS_PASS`. This completes the
displayed sextic identity control, not a computational proof of every
degree or an unrecorded normalization classification. No new large
calculation was needed or launched in this lane.

## 2. The theorem that passes

Let \(F\in V_{a,m}\) have exact ambient normal order \(m\), with
\(q\nmid F\). Assume:

1. Its **full** first-normal divisor on the exceptional ruled surface is
   reduced, horizontal, and irreducible. In particular, there is no
   vertical coefficient divisor; the binary form over \(k(C)\) is
   irreducible of degree \(m\). One must check this before saturating
   away vertical factors. A statement about the saturated horizontal
   factor alone does not meet this hypothesis.
2. The actual quadric restriction is \(\operatorname{div}_Q(F)=mC+T\),
   where \(T\) is reduced, has no component \(C\), and \(T\cap C\) is
   reduced and avoids the two parametrization endpoints.
3. At every point of \(T\cap C\), the attached root in the normal
   direction tangent to \(Q\) is simple. Equivalently for the local
   argument below, the strict-transform surface is regular at this
   root and \(T\) meets its inverse curve transversely there.

Then \(F\) has no sole-support homogeneous mate of any positive degree.
Global integrality of \(F\) need not be added: a hypothetical mate and
the irreducible first-normal form force it.

The theorem concerns genuine curves on \(V(F)\) and their finite
normalization, not vertical exceptional cycles interpreted as residual
components downstairs. It also does not identify ambient normal order
with intersection multiplicity of a pair.

### Normalization and all local attachments

If a hypothetical mate exists, every irreducible factor of \(F\)
contains \(C\). A factor not containing \(C\) would meet a positive-degree
mate in a projective curve, which cannot be contained in its finite
intersection with \(C\). A common surface factor already contradicts
sole support. Initial forms multiply over \(k(C)\); irreducibility and
reducedness of the full first form therefore force one global factor
with exponent one.

Blow up \(C\). In local coordinates \(C=(u,q)\), \(Q=(q)\), use the
chart \(q=uz\). The strict-transform equation is

\[
f_m(t,1,z)+u h(t,u,z)=0.
\]

There is no entire exceptional fiber because the full symbol has no
vertical coefficient divisor. Thus the strict-transform map to \(V(F)\)
has finite fibers along \(C\), is proper, and is finite. Its finite
normalization is the normalization of \(V(F)\). The irreducible reduced
horizontal divisor gives its unique inverse curve \(\Gamma\), with
\(\deg(\Gamma\to C)=m\).

At an attachment \(z=0\), the assumed nonzero \(z\)-derivative makes
the strict transform regular, with local coordinates \(t,u\); its
inverse curve is \(u=0\). On \(Q\), the actual residual has equation

\[
f_m(t,1,0)+u h(t,u,0)=0.
\]

Reduced \(T\cap C\) means its derivative in the \(t\) direction is
nonzero. Hence \(T\) is regular there and \(u\) has order one on it.
This verifies the claimed normalization regularity and transverse
attachment from the stated simple-root and intersection hypotheses.
It does not require every other normal root over the same base point
to be simple. Away from \(C\), reducedness of \(T\) makes its generic
point smooth on the carrier, so its strict transform is birational to
the actual component on \(Q\).

Let \(\nu:S\to V(F)\) be the finite normalization and
\(H=\nu^*\mathcal O(1)\). A sole-support mate pulls back to

\[
\operatorname{div}(\nu^*G_b)=r\Gamma,\qquad r>0.
\]

At each regular attachment this section is a unit times \(u^r\),
so its restriction to \(T\) has order **exactly** \(r\). This is a
local divisor calculation, not an inference from equality of total
degrees. Finite normalization precludes additional exceptional curves
over isolated points of \(C\).

### The two equations and their geometric contradiction

The actual residual class is

\[
[T]=(a,a)-m(1,3)=(a-m,a-3m).
\]

Consequently

\[
\deg T=2a-4m,\qquad C\cdot T=4a-6m.
\]

Intersecting the mate divisor with \(H\), and then restricting it to
the normalization of every component of \(T\), gives respectively

\[
\boxed{ab=4mr},\qquad
\boxed{b(2a-4m)=r(4a-6m)}.
\]

The second identity includes every point of the actual \(T\cap C\):
there are no zeros elsewhere under sole support, and the preceding
local calculation gives all their orders. It remains valid when the
critical-degree residual consists of distinct ruling lines.

Eliminating \(r\) requires

\[
2a^2-7am+8m^2=0,
\]

but

\[
2a^2-7am+8m^2
=2(a-7m/4)^2+15m^2/8>0.
\]

Geometrically, sole support would make a hyperplane multiple
linearly equivalent to a multiple of the inverse curve. The actual
quadric residual measures those two divisors with an incompatible
ratio. If the normalization is regular along all of \(\Gamma\), one
may also write

\[
2H=\Gamma+\widetilde T,\quad
\Gamma^2=14m-4a,\quad
\det\begin{pmatrix}a&4m\\4m&14m-4a\end{pmatrix}
=-2(2a^2-7am+8m^2)<0.
\]

The test-curve proof itself needs regularity only at the attachments;
it does not silently assume that this global self-intersection is
defined for a non-Cartier curve elsewhere.

## 3. The dense-open assertion passes in the full actual source

Put \(a=3m+v\), \(v\ge0\). The full symbol lives on
\(P=\mathbf P^1_{\rm base}\times\mathbf P^1_{\rm direction}\) in

\[
\mathcal O_P(D,m),\qquad D=4a-7m=5m+4v>0.
\]

The following are separate nonempty open conditions on the same
irreducible vector space \(V_{a,m}\); their intersection is nonempty.
No independence of the conditions and no simultaneous arbitrary
choice of their values is assumed.

**Actual symbol basepoint freedom.** Cubic equations restrict in the
normal bundle to a generating subsystem of \(\mathcal O(5)^2\).
One can see this using \(q x_i\), together with the cubic residual
quadratics on \(Q\), which are basepoint free. Products of \(m\)
cubics, multiplied by degree-\(v\) ambient forms nonzero at a chosen
base point, generate \(\mathcal O_P(D,m)\) at each point. Thus the
**actual image** of the symbol map is basepoint free. It need not
be the full abstract section space.

**Smoothness and irreducibility of a general full root.**
Characteristic-zero basepoint-free Bertini applies. Here is a direct
version that avoids an unverified immersion hypothesis: the universal
incidence of a basepoint-free system over smooth projective \(P\) is
a vector bundle over \(P\), hence smooth. Its generic fiber over the
coefficient space is regular by localization, hence smooth over the
characteristic-zero function field. Properness of \(P\) makes the
image of the nonsmooth locus closed, so a nonempty open parameter
set has smooth fibers. For reference, the commonly linked
[Stacks §33.47](https://stacks.math.columbia.edu/tag/0FD4) gives an
immersion-based Bertini formulation; that extra hypothesis is not
being assumed here.

Künneth gives \(H^1(P,\mathcal O_P(-D,-m))=0\), since \(D,m>0\).
The divisor exact sequence therefore gives \(H^0(\mathcal O_Z)=k\).
It is connected, and a smooth connected curve is irreducible. Its
class has positive second coordinate, so it is horizontal; being
irreducible, it has no additional vertical divisor. Smoothness and
the nonzero class also give exact normal order \(m\).

**Complete actual residual restriction.** This surjectivity is checked,
not inferred from the larger abstract symbol target. Cubic residuals
span \(H^0(Q,\mathcal O_Q(2,0))\): the \(m=1,a=3\) quadric flag has
kernel \(qH^0(\mathcal O(1))\) and zero \(H^1(\mathcal O(1))\).
Their \(m\)-fold products span \(H^0(\mathcal O_Q(2m,0))\).
Ambient degree-\(v\) forms restrict onto
\(H^0(\mathcal O_Q(v,v))\), since \(Q\) is a Segre quadric.
Multiplication spans all of

\[
H^0(Q,\mathcal O_Q(2m+v,v)).
\]

Thus the actual restriction map from \(V_{a,m}\) is surjective onto
the complete residual system. For \(v>0\) this is very ample: its
general member is smooth irreducible, transverse to \(C\), and
avoids the two endpoints. For \(v=0\), a general binary degree-\(2m\)
form gives distinct ruling lines at nonzero finite ruling values.
The cubic map on \(C\) is unramified there in characteristic zero,
so all \(6m\) intersections are distinct and transverse.

**The required actual local jets.** At a point of the quadric-direction
section, choose a cubic \(A\) with nonzero symbol value. The forms

\[
A^m P_v,\qquad q A^{m-1}P_{v+1}
\]

have degree \(a\) and order at least \(m\); choose the ambient
\(P_v,P_{v+1}\) nonzero at that point. Their symbol value and vertical
derivative respectively give a nonzero value, and zero value with
nonzero derivative. Hence those two linear conditions are independent
on the actual coefficient source at every point. The incidence of
simultaneous vanishing has codimension two over a one-dimensional
projective section; its projection is a proper closed bad locus.
Avoiding it ensures that every attached root is simple. The preceding
local graph argument supplies all required normalization regularity.

These checks prove a nonempty dense open subset of each full
\(V_{a,m}\), \(a\ge3m\), excluded for every mate degree. They do
**not** prove exclusion of the special closed complement. Nor does
this argument assert that an arbitrary formal symbol algebraizes.

## 4. The broader component-slope condition also passes

Now assume the **full** root is horizontal and reduced but possibly
reducible, and retain the ordinary actual residual and attachment
hypotheses. Write its components as classes \((d_j,e_j)\), where

\[
e_j=\deg(Z_j\to C)>0,\quad
d_j=\deg(Z_j\to\mathbf P^1_{\rm direction})\ge0,
\quad \sum e_j=m,\quad\sum d_j=4a-7m.
\]

The quadric conormal \(\mathcal O(-8)\hookrightarrow\mathcal O(-7)^2\)
is a pair of linear forms with no simultaneous zero, so its direction
section is the graph of a degree-one map. Thus its intersection with
\(Z_j\) is \(e_j+d_j\). Under the ordinary hypotheses these are actual
simple attachments of \(T\) to the corresponding inverse curve, not
just an exceptional intersection count.

For a hypothetical mate let \(r_j>0\) be its inverse-curve orders.
If the carrier has several global factors, sole support forces every
factor to contain \(C\); reducedness of the full symbol forces every
factor exponent to be one. On the disjoint finite normalizations the
same degree calculations therefore remain valid after summing:

\[
ab=4\sum_j e_jr_j,\qquad
b(2a-4m)=\sum_j(e_j+d_j)r_j.
\]

They force

\[
\frac{\sum d_jr_j}{\sum e_jr_j}=7-\frac{16m}{a}.
\]

This ratio is an \(e_jr_j\)-weighted average of \(d_j/e_j\), so some
component must satisfy

\[
\boxed{d_j/e_j\le7-16m/a<7}.
\]

At \(a=3m\) the threshold is \(5/3\). A degree-one component then
has direction degree at most one. The ordinary full-root average
\((4a-7m)/m\) is strictly larger than the necessary weighted average,
by \(2(2a^2-7am+8m^2)/(am)>0\). This provides an independently
useful restriction beyond irreducible covers: all ordinary components
lying strictly above the threshold are excluded together. Existence
of a component below it is only a necessary condition, not a
construction or a sufficiency criterion.

## 5. What this closes, and what remains logically open

| Claim | Final audit status | Exact limitation |
|---|---|---|
| Single full horizontal reduced irreducible root, actual reduced residual, ordinary attachments | PASS for every \(a\ge3m\), every \(b>0\) | Saturated horizontal roots alone do not qualify |
| Dense-open exclusion in each full actual \(V_{a,m}\) | PASS | No coverage of the special closed complement is implied |
| Component-slope necessary condition | PASS on the full reduced horizontal ordinary locus | Does not survive removal of vertical factors without a new defect formula |
| Explicit sextic outside \(k[q,c_0,c_2]\) | Completed identity control; the test-curve theorem applies | Not a classification of all sextics |
| Universal exclusion of every possible STCI carrier | Unproved | Repeated roots, vertical defects, low-slope components and nonordinary attachments remain |

The strongest reusable mechanism is the comparison of a mate divisor
against **two actual curve classes**: hyperplane polarization and the
quadric residual. It broadens the non-existence program independently
of the currently proposed construction. The first unresolved general
implication is an attachment formula that remains valid after vertical
coefficient factors, repeated roots or defective attachments appear;
the displayed ordinary counts cannot be reused unchanged on that
boundary. A second independent interface is whether high contact can
be converted by actual homogeneous polynomial row operations to the
forced-quadric threshold; formal cancellation over \(k(C)\) does not
supply that globalization. The
[reviewed fixed-boundary theorem](2026-10-30-stci-game-quadric-boundary.md)
already explains why large higher-order lifting spaces may preserve
a genuine residual divisor.

For the existence side, an ordinary carrier in these full dense opens
is closed as a source in every mate degree. A surviving construction
must specify which hypothesis changes. The proposed elliptic
degree-eight double-lift has saturated horizontal data \((d,e)=(6,2)\)
and a degree-twelve vertical first-symbol factor, while the full
order-two symbol would have class \((18,2)\). Its horizontal slope
three equals \(7-16\cdot2/8\), but its full symbol is outside this
theorem. Thus this audit does not reject that five-parameter source
by genericity, by the slope condition, or by a smooth-root theorem
applied to the wrong divisor. Its fixed member's extra inverse points
are a separate all-mate obstruction; absorbing those points while
preserving the map and then proving conductor descent remains the
constructive challenge.

Recommended source reconciliation: link this final verdict from the
obstruction proposal and from §6 of the earlier geometry review, so
the historical pending-review wording is not mistaken for the current
status. Preserve the old proof and review paths. No canonical result
or question file was edited by this lane.
