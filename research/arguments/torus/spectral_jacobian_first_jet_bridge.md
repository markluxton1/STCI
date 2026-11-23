# The spectral–Jacobian bridge and first-jet Macaulay pairing

**Status (2026-11-22):** new project-specific deductions from standard Grothendieck residue/graded Gorenstein duality, the accepted local Jacobian–socle lemma on main, and PR #173's spectral ideal-membership argument. **Pending independent mathematical review.** The argument does **not** prove universal moment vanishing or solve the STCI problem. Characteristic zero over algebraically closed \(k\).

## 1. Set-up and the two intrinsic quotient characters

Fix the monomial quartic
\[
 C=[s^4:s^3t:st^3:t^4]\subset Q_1=\{x_1x_2-x_0x_3=0\}
 \subset\mathbf P^3.
\]
It is the \((1,3)\) graph of \([s^3:t^3]\) on
\(Q_1=\mathbf P^1\times\mathbf P^1\), embedded via \(O(1,1)\).
On the dense coordinate torus, put
\[
 A=x_1x_2,\quad B=x_0x_3,\qquad
 U=x_0x_2^2,\quad V=x_1^2x_3,\qquad
 \xi=A/B,\quad\eta=U/V.
\]
On \(C_{u,v}=[s^4:s^3t:u st^3:v t^4]\),
\[
 \xi=u/v,\quad\eta=u^2/v,\qquad u=\eta/\xi,\quad v=\eta/\xi^2.
\]
The characters \((\xi,\eta)\) form an integral basis of the
character group of the quotient torus: exponent matrix
\(\begin{psmallmatrix}1&-1\\2&-1\end{psmallmatrix}\)
has determinant \(1\).

The quadric and cubic pencils are
\[
 Q_\xi=V(A-\xi B),\qquad R_\eta=V(U-\eta V).
\]
On \(Q_\xi\) use the Segre presentation
\([ac:ad:bc:bd/\xi]\). Then
\[
 R_\eta|_{Q_\xi}
  =ab\big(bc^3-(\eta/\xi)ad^3\big).
\]
Consequently, as divisors and as degree-six intersection cycles,
\[
 \tag{1} [Q_\xi\cap R_\eta]
 =[C_{\eta/\xi,\eta/\xi^2}]+[L_{01}]+[L_{23}],
 \quad L_{01}=V(x_0,x_1),\quad L_{23}=V(x_2,x_3).
\]
The two residual lines are the fixed endpoint trisecant rulings.
The entire one-dimensional dense-torus part of this intersection is
the single translated quartic. This is the **geometric**
reason that the pair \((\xi,\eta)\) gives complete transverse
coordinates: the first character specifies a quadric, the second a
cubic cutting the marked graph on that quadric.

## 2. Jacobian identity for *any* proper translated-cycle CI

Let \(F_a,G_b\) be homogeneous forms, \(J=(F,G)\) a height-two
complete intersection, and suppose
\[
 \tag{2}[Y]=\sum_i n_i[C_{u_i,v_i}],\qquad
 n_i>0,\quad ab=4m,\quad m=\sum_i n_i .
\]
Set \(M_{ij}=F_iG_j-F_jG_i\), where \(F_i=\partial_{x_i}F\).

**Proposition A (spectral–Jacobian identity).**
In the **actual** CI ring, including nilpotents,
\[
 \tag{3}\boxed{\Delta_Y:=A\,M_{12}-2B\,M_{03}=0\quad\text{in }S/J.}
\]
In particular \(\Delta_Y\in(F,G)\), with no invariant-ideal,
eigenform, generic normal-order or curvilinear hypothesis.

**Proof.** Work at the generic point of a component \(C_{u_i,v_i}\),
in the affine chart \(x_0=1\), away from the endpoints.
Write \(x=x_1,y=x_2,z=x_3\); on its reduced curve
\[
 x=r,\quad y=u_i r^3,\quad z=v_i r^4.
\]
Because \(k\) has characteristic zero, \(z\) is an étale local
coordinate after a separable field extension. Take normal coordinates
\(X=x-x(z)\), \(Y'=y-y(z)\). The **local mixed-minor lemma**
in [contact Jacobians](contact_jacobians_and_hamiltonian_actions.md#the-actual-socle-and-a-projection-change-lemma)
says the Jacobian minors mixing \(z\) and \(X,Y'\)
vanish in the generic Artinian CI ring, while
\(M_{12}\) is a nonzero generator of its socle.
Returning to \(x,y,z\) yields, modulo \(J\),
\[
 M_{13}=-y'(z)M_{12},\qquad M_{23}=x'(z)M_{12}.
\]
Euler's identity for the two homogeneous equations gives
\[
 M_{03}=-xM_{13}-yM_{23}
       =(xy'-yx')M_{12}
       =\frac{u_i}{2v_i}M_{12}.
\]
Since \(A-q_iB\) vanishes on \(C_{u_i,v_i}\), it belongs to the
maximal ideal of this generic local CI. The socle is annihilated
by that maximal ideal. Hence \(A M_{12}=q_iB M_{12}
=2B M_{03}\) in its actual local ring.

A homogeneous complete intersection is Cohen–Macaulay, so has no
embedded associated primes. Its ring injects into the product
of its localizations at minimal primes. The identity holding in each
generic localization proves (3) globally. \(\square\)

**Interpretation.** The rational quotient character \(\eta\)
is constant along every translated curve. At a generically smooth
reduced component of any finite-projection CI,
\[
 \tag{4}
 \frac{d}{dz}\log\eta
 =2\frac{y'}y-2\frac{x'}x-\frac1z,\qquad
 2B\,M_{03}-A\,M_{12}
 =xy\,z\,M_{12}\frac{d}{dz}\log\eta .
\]
Formula (4) should be read on a suitable separable local splitting,
and modulo the scheme's socle. Thus (3) expresses the **infinitesimal
constancy of the cubic character** \(\eta\) on the generic
components. It is not an ordinary Poisson identity for one fixed
symplectic form when the quadric parameters \(q_i\) differ.

The [established main-branch Poisson identity](contact_jacobians_and_hamiltonian_actions.md#the-six-ambient-minors-different-and-contact-identity)
for *sole support* \(C=C_{1,1}\) is
\(M_{12}-2M_{03}\in(F,G)\).
Since \(A-B\) annihilates the generic socle and \(B\) is a
nonzerodivisor on that support, (3) specializes to that identity.
For an arbitrary arrangement, the componentwise contact forms
\(\omega_{q_i}\) differ; (3) is the correct **common identity**.
It need not imply a global Poisson-invariant defining ideal.

## 3. A direct algebraic recognition criterion for translated support

**Proposition B (spectral equation + Jacobian membership).**
Suppose \(J=(F_a,G_b)\) is a homogeneous proper CI with
\(Y\cap L=\varnothing\), where \(L=V(x_0,x_3)\). The following are
equivalent:

1. Every irreducible component of \(Y_{\rm red}\) is some
   \(C_{u_i,v_i}\) with \(u_i,v_i\ne0\).
2. There exists a nonzero homogeneous binary polynomial
   \(H(A,B)=c\prod_i(A-q_iB)^{e_i}\), with
   \(q_i\in k^\times\) and \(e_i>0\), such that
   \[
      \tag{5}H(x_1x_2,x_0x_3)\in(F,G),\qquad
       A M_{12}-2B M_{03}\in(F,G).
   \]

For implication \(1\Rightarrow2\), one may take
\(H=\prod_i(A-q_iB)^{n_i}\), where \(n_i\) are actual
generic multiplicities; this is the
[existing canonical spectral membership](chow_realization_moment_separation.md#11-the-two-extreme-mixed-coefficients-of-the-quadric-spectrum-equation)
combined with Proposition A.

**Proof of converse.**
The spectral equation forces every reduced component either into
\(Q_{q_i}\) for some \(q_i\in k^\times\), or into the
base locus \(V(A,B)\) of the quadric pencil. Any positive-dimensional
component of \(V(A,B)\) is one of four coordinate lines; all four
meet \(L\), contrary to \(Y\cap L=\varnothing\).
The same observation eliminates reduced components contained in
any coordinate hyperplane. Hence every component meets the dense
four-coordinate torus, and \(\xi\) is constant on it.

Since the center is disjoint, projection \([x_0:x_3]\) is finite
on \(Y\). On the generic point of each reduced component it is
separable. The Artinian local CI's relative Jacobian \(M_{12}\)
is a nonzero socle generator. Divide the second relation in (5)
**on that one-dimensional socle**, not in the whole CI ring.
The generic tangent-minor formula in the proof of Proposition A,
now for an arbitrary component \(D\), gives
\(2z(xy'-yx')-xy=0\) in its residue field.
By (4), \(d\eta/dz=0\), so characteristic zero implies
\(\eta\in k^\times\) is constant along \(D\).
The component lies in \(Q_\xi\cap R_\eta\), whose unique
dense-torus curve component is \(C_{\eta/\xi,\eta/\xi^2}\)
by (1). Thus \(D\) is that translated quartic.
The CI is pure, so there are no isolated additional projective
components. \(\square\)

This is a **recognition criterion** in actual homogeneous equations,
not a realization theorem: (5) already assumes a proper two-generated
ideal. It does not assert that every desired spectral divisor admits
such a pair. The condition \(H\in J\) by itself is too weak:
\(J=(Q_1,G)\) with general \(G\) avoids the projection center
but its curve is not a union of the marked translated quartics.
The second, Jacobian, condition is a genuinely separate test.

## 4. The first moment is a perfect residue pairing of first jets

Assume the hypotheses (2) again. Since \(Y\cap L=\varnothing\),
\[
 E=S/(F,G)\quad\text{is finite free of rank }ab
 \text{ over }T=k[x_0,x_3].
\]
Let \(\operatorname{Res}_{F,G}\) denote its **relative**
Grothendieck residue for the fiber variables \((x_1,x_2)\),
with orientation \(dx_1\wedge dx_2\). Write
\(J_{\rm fib}=M_{12}\). Standard complete-intersection duality gives
\[
 \tag{6}\operatorname{Tr}_{E/T}(h)
   =\operatorname{Res}_{F,G}(hM_{12}).
\]
The established translated-cycle trace identity is
\[
 \tag{7}\operatorname{Tr}_{E/T}(A)=4B\sum_i n_iq_i=4B M_1.
\]
Combining (3),(6),(7) and canceling \(B\) in the domain \(T\)
gives
\[
 \tag{8}\boxed{M_1=\tfrac12\operatorname{Res}_{F,G}(M_{03}).}
\]

Now expand the **actual** equations in the first normal
neighborhood of the disjoint line \(L\):
\[
 \tag{9}
 F=f_0(x,y)+x_0p(x,y)+x_3q(x,y)+O((x_0,x_3)^2),
\]
\[
 G=g_0(x,y)+x_0r(x,y)+x_3s(x,y)+O((x_0,x_3)^2),
\quad(x,y)=(x_1,x_2).
\]
Here \(\deg f_0=a,\deg g_0=b\);
\(\deg p=\deg q=a-1,\deg r=\deg s=b-1\).
The leading restrictions have no common zero in
\(\mathbf P^1_L\), so the binary Artin algebra
\[
 \mathscr A=k[x,y]/(f_0,g_0)
\]
is graded Gorenstein of length \(ab\), with socle degree
\(d=a+b-2\). In the relative homogeneous residue, a numerator
of total degree \(d\) has residue a homogeneous polynomial of
degree **zero** in \(T=k[x_0,x_3]\), hence a constant.
Relative residue commutes with base change to the origin
\((x_0,x_3)=(0,0)\), and there
\[
 M_{03}|_L=p\,s-q\,r.
\]
It follows that
\[
 \tag{10}
 \operatorname{Res}_{F,G}(M_{03})
 =\operatorname{Res}_{f_0,g_0}(p s-q r).
\]
The special case of Grothendieck residue base change and the
residue/Jacobian trace formula are established classical facts:
Cattani–Dickenstein–Sturmfels,
[*Computing Multidimensional Residues*](https://arxiv.org/abs/alg-geom/9404011);
see also the exact all-degree six-layer trace expansion already
proved [on PR #171](https://github.com/markluxton1/STCI/blob/codex/chow-polytope-realization/research/arguments/torus/fixed_surface_and_endpoint_algebras.md#7-the-first-trace-depends-only-on-two-lower-fiber-degree-layers).
The **special simplification from six to first layers** here uses
the translated-cycle Jacobian identity (3), not only the trace theorem.

**Corollary C (first-jet residue formula).**
For *every* characteristic-zero proper homogeneous translated-cycle
CI, without invariance,
\[
 \tag{11}\boxed{
 M_1=\frac12\,\operatorname{Res}_{f_0,g_0}(p s-q r).
 }
\]
It is equivalent to the universal first-moment conjecture to prove
that the scalar on the right vanishes for every actual pair
satisfying the complete support condition. This is not known.

The graded Gorenstein residue induces a **perfect pairing**
\[
 \mathscr A_{a-1}\times\mathscr A_{b-1}
 \longrightarrow k,\qquad ([h],[j])\mapsto
 \operatorname{Res}_{f_0,g_0}(hj),
\]
because \((a-1)+(b-1)=d\); both graded factors have
dimension \(\min(a,b)\). On
\[
 \mathcal V=\mathscr A_{a-1}\oplus\mathscr A_{b-1}
\]
this defines a nondegenerate alternating form
\[
 \tag{12}
 \Omega((p,r),(q,s))
   :=\operatorname{Res}_{f_0,g_0}(p s-q r).
\]
The two first normal derivatives of the original equations at
\(L\), in the \(x_0\) and \(x_3\) directions, determine the vectors
\(v_0=([p],[r])\) and \(v_3=([q],[s])\).
Therefore (11) is
\[
 \tag{13}\boxed{\Omega(v_0,v_3)=2M_1.}
\]
Thus **UM1 is an isotropy condition on the two first normal
equation jets along the disjoint line**, using Macaulay duality of
the binary CI \(f_0,g_0\). The residue form depends on the
chosen presentation/orientations; its **vanishing** is invariant
under allowed changes of CI generators. Indeed (8) identifies it
with a multiplication trace that depends only on \(J\).

**Scope and warning.** The entire translated-cycle hypothesis in
(11) is indispensable. For a general pair containing \(C\), the
first-jet pairing need not vanish. The first jets may be freely
changed while residual curves appear. Hence (13) is a sharp
*reduction of the desired identity*, not a proof that all such
jets are isotropic.

### Serre duality makes the pairing intrinsic to the disjoint line

The same form can be defined without mentioning an affine quotient
or a chosen monomial basis. Since \(f_0,g_0\) have no simultaneous
zero on the line \(L\simeq\mathbf P^1\), their Koszul complex on
\(L\), twisted by \(a+b-2\), is the short exact sequence
\[
 \tag{14}
 0\to\mathcal O_L(-2)\xrightarrow{(-g_0,f_0)}
 \mathcal O_L(b-2)\oplus\mathcal O_L(a-2)
 \xrightarrow{(f_0,g_0)}
 \mathcal O_L(a+b-2)\to0 .
\]
For \(a,b>0\), both middle summands have zero \(H^1\), so its
connecting homomorphism identifies
\[
 \mathscr A_{a+b-2}
 \simeq H^1(L,\mathcal O_L(-2))
 =H^1(L,\omega_L)\simeq k.
\]
The last arrow is the **Serre trace**, and with the usual
ordered Koszul orientation the resulting functional is the
Grothendieck residue of \((f_0,g_0)\).
Consequently,
\[
 \tag{15}
 \boxed{\ \Omega(v_0,v_3)
 =\operatorname{Tr}_L\!\big(\partial_{f_0,g_0}(ps-qr)\big)
 =2M_1\ } .
\]
Thus the conjectural vanishing can be stated as the vanishing of
a **canonical Serre-duality class on the line disjoint from the
quartic**, formed from the two actual first normal jets.
The line itself is the \((-1)\)-eigenspace line of the
osculating involution described in
[the intrinsic curve geometry](../curve/special_plane_and_line_sections.md#3-osculation-and-its-residual-involution).
This connects the geometric uniqueness of the projection center
to the Macaulay residue pairing. The class depends on the ordered
equation presentation and normal framing; its vanishing is intrinsic
to the corresponding CI and its distinguished center, by (8).

For fixed degrees \(a\le b\), the two dual factors
\(\mathscr A_{a-1}\), \(\mathscr A_{b-1}\) have dimension \(a\).
Hence the **critical symplectic space has dimension \(2a\) for all
mate degrees \(b\)**. This is a degree-uniform *dimension of the
trace detector at fixed smaller degree*, not a degree bound
or a classification of source realizations.

### An immediate wider sufficient vanishing condition

Within the full translated-cycle hypotheses, equation (11) gives
\(M_1=0\) whenever **either equation has vanishing first
normal layer** along the disjoint line, i.e. \(p=q=0\) or
\(r=s=0\). More generally it vanishes whenever the two normal
jet vectors span an isotropic plane in \((\mathcal V,\Omega)\).
These are all-degree sufficient conditions without any torus-invariance
assumption. The existence of a generator with such a vanishing jet
is **not** known for arbitrary Chow-matched pairs, and cannot be
inferred merely from the cycle or a torus-fixed initial ideal.

## 5. Two exact controls

**Invariant binomial example.** For
\[
 F=x_1^4-x_0^3x_3,\qquad
 G=x_2^4-x_0x_3^3,
\]
\(f_0=x^4,g_0=y^4,p=q=r=s=0\).
Also \(M_{12}=16x_1^3x_2^3\), \(M_{03}=8B^3\), and
\[
 A M_{12}-2B M_{03}
 =16(A^4-B^4)=16(x_2^4F+x_0^3x_3G).
\]
The four characteristic-zero translated components have \(M_1=0\).

**A proper containing pair with nonzero skew residue and residual
curves.** Let \(Q=x_0x_3-x_1x_2\) and take
\[
 F=x_1^4-x_0^3x_3+x_0Qx_1,\qquad
 G=x_2^4-x_0x_3^3+x_3Qx_2.
\]
Both contain \(C\), and \(Y\cap L=\varnothing\), since
\((f_0,g_0)=(x^4,y^4)\).
Their first jets are
\[
 p=-x^2y,\quad q=0,\quad r=0,\quad s=-xy^2,
\qquad ps-qr=x^3y^3.
\]
Thus
\(\operatorname{Res}_{x^4,y^4}(ps-qr)=1\neq0\).
At \([1:1:1:1]\in C\), their ambient gradients are
\((-2,3,-1,0)\) and \((0,-1,3,-2)\), linearly independent.
Hence \(C\) has generic multiplicity one and the pair has
residual degree twelve. The nonzero skew residue is therefore
perfectly compatible with merely **containing** the marked
quartic; the translated-cycle hypothesis in (11) cannot be
silently replaced by such containment.

### Why the obvious low-order spectral-coefficient test fails in high degree

The actual spectral equation has degree \(2m=ab/2\) and begins
\[
 H(A,B)=A^m-M_1A^{m-1}B+\cdots.
\]
As a section near the disjoint line \(L\), \(B=x_0x_3\)
has **normal order two**. The first coefficient that could
directly detect \(M_1\) is therefore the order-two term
\(-M_1 A^{m-1}x_0x_3\), whose fiber coefficient
\(A^{m-1}\) has degree \(2m-2=ab/2-2\).
But the Artin Gorenstein quotient
\(\mathscr A=k[x,y]/(f_0,g_0)\) has top degree
\(a+b-2\). Hence
\[
 \tag{16}
 \deg A^{m-1}-(a+b-2)
 =\frac{ab}{2}-a-b
 =\frac{(a-2)(b-2)-4}{2}.
\]
For \((a,b)=(4,4)\) this is zero: the first polar
coefficient is exactly in the socle degree, which helps explain
why the quartic case is exceptional. For \((6,6)\) it is
six: the same fiber coefficient is zero in
\(\mathscr A\) automatically, whatever the unknown value
of \(M_1\). Thus a **direct** order-two projection of the
spectral equation to the binary CI quotient cannot force
the universal isotropy relation in those higher degrees.
This does not show the full second-order *lifting problem*
is unobstructed: cofactor corrections and the coupled
Jacobian condition can carry further information.

This degree comparison is an all-degree **negative control**:
the first-jet moment formula (13) is sharp, but the global
constraint forcing its vanishing cannot generally be read
off just from the coefficient of \(A^{m-1}B\) in the
order-two spectral restriction. It must use genuine
joint equation compatibility.

### Direct test on a hypothetical sole-support CI

The [companion necessary-jet analysis](sole_support_first_jet_gate.md)
applies the already-proved main-branch sole-support Poisson theorem
\(M_{12}-2M_{03}\in(F,G)\) to the first normal
neighborhood of the disjoint line. It yields the exact
congruence
\[
 J(f_0,g_0)\equiv2(ps-qr)\pmod{(f_0,g_0)},
 \qquad
 \Omega(v_0,v_3)=\frac{ab}{2}=2m\neq0.
\]
This is the **STCI requirement**, not the conjectural
**moment-vanishing condition** on all translated-CI cycles.
In the graded binary CI's one-dimensional socle degree, the
congruence is equivalent to this scalar requirement.
For every \(a,b\ge4\) an explicit family of proper global
equations containing \(C\) realizes *every* scalar value
of \(\Omega\), including \(ab/2\), but retains a residual cycle
of degree \(ab-4\). Consequently no first-jet-only
contradiction results from the accepted Poisson theorem.
Moreover, the spectral power \(Q^m\in(F,G)\) for a hypothetical
STCI has **automatically zero truncation** modulo
\(I_L^{r_*}\), \(r_*=(a-2)(b-2)/2\), for all proper
degree-\((a,b)\) pairs avoiding \(L\). In the sextic
\((6,6)\) case this first nontrivial detection order is
eight. The global incidence may still impose indirect
restrictions on the first jets through its high-order
compatibility; that implication remains open.

### The same residue detects the first global spectral-power obstruction

The [direct STCI power/jet comparison](sole_support_first_jet_gate.md#the-first-power-obstruction-is-another-serre-duality-class)
identifies a second canonical use of the
**same** relative Grothendieck residue
\(\mathcal R_{F,G}:E\to k[x_0,x_3](-d)\),
\(d=a+b-2\).
For \(m=ab/4\), \(r_*=2m-d\),
the first potentially nontrivial
\(I_L\)-adic class of the **necessary**
power \(Q^m\) is exactly
\[
 \boxed{\mathcal R_{F,G}(Q^m)
       \in H^0(\mathbf P^1,\mathcal O(r_*)) .}
\]
More generally the map
\(H(A,B)\mapsto\mathcal R_{F,G}(H(A,B))\)
is linear on the full degree-\(m\)
homogeneous quadric-spectrum forms and
annihilates the spectrum of every actual
translated-cycle CI.
For a hypothetical STCI the two necessary
relative-residue values are
\[
 \mathcal R_{F,G}(M_{03})=ab/2
 \quad\text{and}\quad
 \mathcal R_{F,G}(Q^m)=0 .
\]
The first is a scalar encoding the first
normal jets; the second is a binary
form of degree \(r_*\) encoding
higher normal compatibility.
Both use \(H^1(L,\omega_L)\) via
the binary CI's Koszul sequence.
An exact restricted \((4,4)\) example
forces incompatible first and second
conditions \(\lambda\mu=8\) and \(4\);
no general implication is known.
The first spectral residue vanishing
is not sufficient for full membership
\(Q^m\in(F,G)\) or for sole support.

## 6. Cross-framework interpretation and the actual remaining gap

1. The **Segre/quadrics** viewpoint supplies \(\xi\), the spectral
   form \(H_\sigma(A,B)\) and the divisor of containing quadrics.
2. The **cubic scroll/conductor** viewpoint supplies the independent
   quotient coordinate \(\eta\); (1) explains its two fixed
   residual trisecant lines and the need to control boundary
   support.
3. The **Jacobian/Hamiltonian** viewpoint supplies the actual
   ring identity (3), which records infinitesimal constancy of
   \(\eta\) even when the CI ideal itself is not torus invariant.
4. The **finite-cover/residue** viewpoint converts this identity
   into the first-jet symplectic pairing (13), and therefore into
   the first moment of the quadric divisor.
5. The **global realization** problem is now to establish
   \(\Omega(v_0,v_3)=0\) whenever the actual pair satisfies
   the spectral membership and Jacobian support-recognition
   conditions (5). Those incidence conditions may constrain
   high-order terms; their first-jet images are not known to be
   isotropic. A proof must use joint global equations or a
   geometric restriction on their first jets. Merely invoking the
   perfect residue pairing, the coisotropic shape, or absence of
   residual boundary lines is not sufficient.

The new formulation does **not** identify the Artin residue
symplectic form \(\Omega\) with the ambient contact form
\(\omega_\xi\); they live on different spaces and are connected
only via the specific Jacobian and trace identities proved above.
It does **not** imply that the defining ideal is invariant,
that a limiting pair stays a CI, or that the reciprocal moment
vanishes. The existing invariant and exceptional non-invariant
quartic controls satisfy (13), as they must.

**Next mathematical test.** Compute the image in
\(\mathcal V^{\oplus2}\) of the *joint actual-equation locus*
defined by (5), retaining full properness and the complete
translated cycle, and ask whether that image is isotropic under
(12). Any proof must be degree uniform; a counterexample with
\(\Omega\ne0\) and conditions (5) would disprove universal
moment vanishing. The counterexample in section 5 satisfies
properness and containment but not (5).
