# Smooth marked image carriers and first-symbol transfer

**Scoped correctness review (2026-11-23, combined integration):** independently reconstructed SM1–SM4, the conic-order compression and first-symbol transfer. Inherited inputs are the actual two-blowup correspondence, local power–socle theorem and fixed-quartic low-degree exclusion.

Use the [two-blowup dictionary](blowup_residual_geometry.md#the-two-blowups-and-their-actual-global-section-dictionary) and [marked correspondence](blowup_residual_geometry.md#the-marked-correspondence-on-the-whole-equality-boundary) for the global setup. The local coordinates and ML formulas are owned by [marked-line geometry](marked_line_local_geometry.md#marked-coordinates-and-a-geometric-source-constraint); SC and FT formulas are owned by [finite transfer](first_graph_finite_transfer.md#socle-defects-on-the-two-presentations-of-the-first-graph). The conic-order requirement LC1 is in [strict-carrier Picard compression](strict_carrier_picard_compression.md#lefschetz-compression-on-ample-strict-carriers). This account owns the complementary smooth-image stratum and its first-symbol comparison.

### The opposite marked stratum: a smooth image carrier and a forced graph defect

There is a complementary exact comparison
which does not assume primitivity of the
graph at the marked point. Suppose the
image carrier \(U=(P=0)\) in the
\((3p,4q)\) edge is smooth at \(z\).
As in ML1 the marked ideals are
\(\Gamma=(x,y),\Delta=(t,y)\).
The trace \(P_\Gamma=t^{2p}\text{unit}\)
and \(\Delta\subset U\) force \(P_y(z)\ne0\).
The formal smooth surface is consequently
\(y=g(x,t)\) with \(g(x,0)=0\),
\(g(0,t)=t^{2p}u(t)\), \(u(0)\ne0\).
Write
\[
 g(x,t)=t^{2p}u(t)+xh(x,t),\quad h(x,0)=0.
\]
On the graph chart \(y=xv\) make the
regular coordinate change
\(v'=(v-h(x,t))/u(t)\). The strict
carrier and strict mate then give the
actual completed equations
\[
 P':\ xv'=t^{2p},\qquad
 W:\ (xv'-t^{2p},\ (v')^q).                             \tag{SM1}
\]
Indeed on the smooth image carrier the
mate is a unit times \(t^{2pq}\) at \(z\)
by sole support. Pull back and divide
by \(x^q\); the strict mate on \(P'\)
is a unit times \((v')^q\), since
\(t^{2pq}=x^q(v')^q\) there. The
unit remains a unit on the blowup.
No equality of arbitrary ambient
representatives before restricting to
the carrier is asserted.

Thus the smaller strict carrier is the
marked \(A_{2p-1}\) type, with first
symbol vanishing once and marked local
index \(2p\). The index follows either
from the standard end-marked \(A\)-chain
or directly from \(v'=0\) on \(P'\).
The completed graph algebra has basis
\[
 (v')^i t^j,\quad 0\le i<q,\quad0\le j<2p,
\]
over \(k[[x]]\). In the generic algebra
\(v'=t^{2p}/x\); the saturated layer
of order \(k\) therefore has generator
\(t^k/x^{\lfloor k/(2p)\rfloor}\), and
the free first generator is \(t\).
It follows that
\[
 \boxed{D_{W,k}(z)=\left\lfloor k/(2p)\right\rfloor,
 \quad D_{W,\rm top}(z)=q-1,\quad \xi=0.}                \tag{SM2}
\]
The whole image algebra is primitive at
\(z\), since \(U\) is smooth there.
This agrees with SC4: the modification
creates a graph defect despite the
primitive image, the opposite phenomenon
to ML7. In particular a mixed \((6,8)\)
pair in this lane has marked graph
defect exactly one (out of the total
seven) and the remaining six units of
defect are away from \(z\).

#### Compression of an actual image mate can preserve conic order in this lane

The conic-order requirement in LC1
and in the [K3 torsion compression](k3_marked_lattice.md#a-k3-marked-lattice-obstruction-to-the-primitive-graph-row) is
not automatic in general. But the
smooth marked stratum gives a direct
positive bridge at degree two.

**Claim (all \(p\ge2\)).** If \(U\) is
integral, smooth at the marked point
as above, and has an actual image mate
of degree two, i.e. a section \(H_2\)
of \(2M\) cutting precisely \(2p\Delta\)
on \(U\), then there is an actual
degree-four mate to the original
degree-\(3p\) carrier in \(\mathbf P^3\).
Consequently this entire class is
excluded in characteristic zero by
the all-mate low-degree exclusion.
A degree-one image mate is also
impossible, since its square supplies
one of degree two.

**Proof.** On the smooth marked surface
the image mate has local equation
\(t^{2p}\) times a unit. Thus an ambient
representative of its section has
\[
 H_2=t^{2p}a(x,t,y)+P b(x,t,y),\quad
 a(z)\ne0 .
\]
(The local equation \(t\) on \(U\)
cuts the smooth quintic.) Restrict
to the conic: its trace vanishes to
order at least \(2p\) at \(z\).
If \(p>2\) the trace is identically
zero since its degree on \(\Gamma\)
is four; if \(p=2\) it is proportional
to \(P|_\Gamma\), so subtract a
scalar multiple of \(P\) to kill it.
In either case obtain a degree-two
section \(H_2'\) containing \(\Gamma\),
with the same nonzero restriction to
\(U\). The now identically zero
trace forces the coefficient of \(P\)
at \(z\) in the displayed expression
for \(H_2'\) to be a unit:
on the conic divide by \(t^{2p}\)
and use \(a(z)\ne0\) and the nonzero
leading coefficient of \(P|_\Gamma\).
Therefore \(H'_{2,y}(z)\ne0\).
It has exact order one along the
conic, and its leading conic normal
form at \(z\) is nonzero.

The strict carrier of \(P\) meets
the exceptional ruled surface over
\(\Gamma\) only in the fiber at \(z\),
because the trace of \(P\) has exactly
that support. The strict \(H_2'\) meets
that fiber in a degree-one form
with the marked root and no whole
fiber. Off the exceptional divisor
their intersection has sole support
the punctured marked quintic, by the
actual image-mate hypothesis.
Purity of the strict CI now leaves
sole support exactly \(T\).
The degree-two section \(H'_2\) cannot
contain the anticanonical surface
\(\Sigma\), since it is smooth at
\(z\) whereas \(\Sigma\) is singular
along \(\Gamma\). Being of the same
class as \(\Sigma\), containment
would make it a scalar defining
section of \(\Sigma\).
Thus it gives an actual degree-four
form of order one along \(C\) by
the section dictionary (2), with
\((3k-2j,k-j)=(4,1)\) for \(k=2,j=1\).
The proper graph intersection
pushes to a proper sole-support
pair with the original degree-\(3p\)
carrier, which is impossible.
\(\square\)

For an integral generically regular
image carrier with the original
degree-\(2q\) mate, the ample
Lefschetz Kummer argument LC1
on \(V_5\), where
\(\operatorname{Pic}(V_5)=\mathbb Z M\),
gives exact minimal image mate
degree \(n=R/p\mid2q\), with \(R\)
the lcm of actual local almost-Cartier
indices along \(\Delta\).
The lift to \(V_5\) uses
\(H^1(V_5,\mathcal O((n-p)M))=0\)
when \(n-p\ge-1\) by Kodaira,
and in fact for every integer \(n-p\)
by Serre duality and Kodaira
(\(H^1\) is dual to \(H^2\) of
\((p-n-2)M\), which vanishes
when \(n-p\le-1\)).
The ample-carrier Picard argument
does not need normality away from
the marked curve. When the image
carrier is reducible, this
fixed-carrier version must instead
be applied componentwise with the
actual multiplicities.

By the claim, in the smooth
marked lane necessarily \(n>2\).
In particular for \(q=2\) one must
have \(n=4\) and \(R=4p\).
For the actual sextic \(p=2\)
the smaller image carrier is
integral by the independent
low-degree factor exclusion;
thus **if it is smooth at \(z\),
it has an actual index-eight
point elsewhere on \(\Delta\)**.
This condition does not assert
that an index-eight point has ADE
type. Nor does it transfer an
arbitrary compressed mate back
to the original problem: degree
two and smoothness at the marked
point are both used in the trace
cancellation and nonzero normal
form. All the deductions in this
section were covered by the scoped correctness review above.

### First-symbol transfer and the remaining mixed sextic strata

The conormal modification used in SC4
also transports the actual scalar first
symbols; it is not limited to the free
first normal layer. Assume generic
curvilinearity, and use \(Z,W\) and
\(\xi=0,1\) as in SC4. Write \(K_Z,K_W\)
for the saturated generic relation lines,
i.e. the kernels of the conormal bundle
surjections onto the two free first
normal quotients \(L_Z,L_W\). Along
the curve there are commutative short
exact sequences
\[
 0\to K_\bullet\to N_\bullet^\vee
     \to L_\bullet\to0.
\]
The ambient conormal map from image
to graph has determinant vanishing
once at \(z\); the quotient line
map has vanishing order \(\xi\).
Taking determinants in the diagram
shows that the kernel map has zero
order \(1-\xi\). This equality
retains the saturated relation lines,
not just their generic spans.

Denote by \(A_{P,Z},A_{S,Z}\) the
actual scalar first-symbol orders at
\(z\) of the image equations,
and by \(A_{P',W},A_{S',W}\) those
of the strict equations. For a
nonzero first symbol the formula is
\[
 \boxed{\begin{aligned}
 A_{P',W}&=A_{P,Z}+1-\xi,\\
 A_{S',W}&=A_{S,Z}+1-\xi-q .
 \end{aligned}}                                         \tag{SM3}
\]
In the first equation pullback
transports the symbol directly;
in the second the actual pullback
is \(x^q S'\). Restricting its
first normal symbol to the curve
multiplies by \(x^q\), because
\(S'\) vanishes on the curve.
Thus the exceptional division
must be subtracted, not ignored.
A generically zero first symbol
stays zero on either side (one
can use the convention infinite
order). The symbols and all
finite orders away from \(z\)
are unchanged.

The same proof is valid for any
finite same-support modification
coming from a blowup of a smooth
center meeting the support
transversely in this local chart,
when each actual equation is
divided by its prescribed
exceptional order \(e_i\).
Its general formula is
\(A_{i,+}=A_{i,-}+1-\xi-e_i\).
One must keep the actual generic
curvilinear support; this is not
a rule for arbitrary normal
symbols on different blowup
components.

In the surviving mixed
\((6,8;2,2)\) row we necessarily
have \(\ell_W=4\) and total
\(D_W=7\), with \(D_W(z)>0\)
by the marked-line obstruction.
The smaller first symbol is
nonzero by SC6, so its global
degree on \(W\) is \(7\).
For the image, \(\ell_Z=4+\xi\),
the total first-symbol order
of \(P\) is \(6+\xi\), and
the total image top defect is
\(6+7\xi\). SC4 and SM3 give
the following exact subdivision
at the mark:
\[
\begin{array}{c|c|c|c|c}
 &\xi &D_W(z)&D_Z(z)&A_{P',W}(z)\\\hline
 U\text{ smooth}&0&1&0&1\\
 U\text{ singular}&0&2,\ldots,7&D_W(z)-1&A_{P,Z}(z)+1\\
 U\text{ singular}&1&1,\ldots,7&D_W(z)+6&A_{P,Z}(z)
\end{array}                                             \tag{SM4}
\]
Here finite ranges are necessary
only. In the first row use SM1--SM2.
In the other rows \(P\) and \(S\)
are both singular at \(z\) (the
latter by its conic order), so
the image CI is nonprimitive and
its top defect positive. No
assertion of the realization
of a range endpoint is made.
In every row the graph and image
defects agree away from the mark.
The common first-symbol divisor
at the marked point on the graph
is exactly
\[
 1-\xi+\min(A_{P,Z},A_{S,Z}-q)
\]
using the infinity convention.
In particular in the smooth image
row it has multiplicity one,
and a general normal strict octic
replacement has marked index four
there: its scalar symbol has
order one, so it has an end-marked
A-type singularity by the
[reduced-symbol local calculation](../carriers/normal_carrier_divisor_geometry.md#reduced-common-first-normal-divisor-a-uniform-marked-ade-and-rank-test).
For its primitive local index
\(r\) one therefore has \(D_r=0\).
The local power--socle formula
with top defect one and \(A=1\)
now forces \(8/r-1=1\), hence
\(r=4\).
Outside that row the full
multiplicities of the common
symbol divisor remain to be
realized by the actual sections.

Thus the reduced resultant
condition SC2 now retains a
specified defect stratum and
first-symbol orders at \(z\),
rather than an arbitrary
degree-seven divisor. The
smooth image row also retains
the necessary actual index-eight
point *away* from \(z\) by the
conic-order compression above.
These are distinct requirements
on two presentations of the same
CI, not interchangeable local
indices. Independent reconstruction is recorded in the scoped review above.

