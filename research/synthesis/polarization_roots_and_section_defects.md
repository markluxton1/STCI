# Polarization roots and section-extension defects

Let \(k\) be algebraically closed of characteristic zero, let
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\), and suppose that
\(Z=V(F_a,G_b)\) is a proper homogeneous CI with \(Z_{\rm red}=C\).
Write \(H=\mathcal O_Z(1)\), \(c=a+b-4\), and \(J=\ker(\mathcal O_Z\to\mathcal O_C)\).
These independently reviewed **provisional** deductions apply to every
such pair. They constrain a hypothetical pair without excluding or
constructing one. The exact issue is extension of the missing coordinate
through nilpotent structure, not the abstract rationality of the support.

**Review status (2026-10-31).** Independent mathematical and preservation review reconstructed this replacement and its explicit characteristic extensions. The varying-Hilbert-function local control, degree-four defect notation, and ribbon section calculation were checked in their corrected homes. No material finding remains unresolved within the stated scopes. These remain reviewed provisional deductions, with no canonical promotion; no computation or inherited certificate rerun was needed.

## A unique ample root, without a pencil

The characteristic-zero logarithm identifies \(1+J\) with the additive
sheaf \(J\). Constants lift to \(Z\), and \(H^2(Z,J)=0\), so the unit
sequence gives

\[
0\to H^1(Z,J)\to\operatorname{Pic}(Z)\to\operatorname{Pic}(C)=\mathbf Z\to0.
\tag{1}
\]

The kernel is a characteristic-zero vector space. Lift \(\mathcal O_{\mathbf P^1}(1)\)
to \(L_0\); the class \(HL_0^{-4}\) lies in the kernel, where it has a
unique fourth root. Thus there is a unique isomorphism class \(L\) with
\(L|_C=\mathcal O(1)\), \(L^4\simeq H\). The isomorphism \(L^4\simeq H\)
remains a choice. \(L\) is ample, since a positive power is ample.
Neither a nonzero section nor a two-section pencil follows.

## The full root algebra and its actual trace pairing

Choose the fourth-power identification and define

\[
A=\bigoplus_{n\in\mathbf Z}H^0(Z,L^n),\qquad
B=\bigoplus_{q\ge0}H^0(Z,H^q)=k[x_0,x_1,x_2,x_3]/(F,G).
\tag{2}
\]

The latter equality, including zero sections for \(q<0\), follows from
the homogeneous CI resolution. Give \(B_q\) degree \(4q\) inside \(A\),
so \(A^{(4)}=B\) with regrading. Negative-degree nilpotent sections in the
other congruence classes must not be discarded without proof.

For \(0\le i<4\), the full section module
\(M_i=\bigoplus_{q\in\mathbf Z}H^0(Z,L^iH^q)\) is finite over \(B\):
the positive tail is finite by the section-module construction, and the
negative tail vanishes by Serre duality and Serre vanishing. Full section
modules have local cohomology \(H^0_{B_+}=H^1_{B_+}=0\) at the cone vertex;
this follows from the sheaf/section-module exact sequence, which does not
require reduction or normality ([Stacks, §28.29](https://stacks.math.columbia.edu/tag/01QG)).
Since \(\dim B=2\), these modules are maximal Cohen–Macaulay. Away from
the vertex they come from invertible sheaves on \(Z\). Hence \(A\) is a
finite CM \(B\)-algebra.

On the punctured cones the finite map is
\(L^{-1,\times}\to H^{-1,\times},\ z\mapsto z^4\), a finite étale
\(\mu_4\)-torsor even over the nonreduced base. The homogeneous functional
\(t=4\operatorname{pr}_{A^{\mu_4}}:A\to B\) gives the actual pairing

\[
A\longrightarrow\operatorname{Hom}_B(A,B),\quad
u\longmapsto(v\mapsto t(uv)). \tag{3}
\]

It is the perfect trace pairing off the vertex. Both modules are MCM
(the right side by duality over Gorenstein \(B\)); depth two extends
sections across the vertex. Thus (3) is globally an isomorphism. This
uses the pairing itself, rather than a reflexive-extension theorem
for a normal domain, whose hypotheses are unavailable here. In the
\(A\)-grading \(\omega_B=B(4c)\), so finite duality yields

\[
\omega_A=\operatorname{Hom}_B(A,\omega_B)=A(4c). \tag{4}
\]

The full root algebra is Gorenstein. This says neither that \(A\) is a
complete intersection nor that its reduction is CM or normal.

## The missing coordinate remains at the reduced cover vertex

Restriction to \(C\) has nilpotent kernel and identifies \(A_{\rm red}\)
with a subalgebra of \(k[s,t]\). For sufficiently large degrees restriction
is surjective, so its normalization is \(k[s,t]\) and
\(D=k[s,t]/A_{\rm red}\) has finite length. Exactness of \(\mu_4\)-invariants
or degreewise restriction gives

\[
(A_{\rm red})^{(4)}=B_{\rm red}=k[s^4,s^3t,st^3,t^4],\qquad
D_4=k\cdot s^2t^2,\quad D_{4q}=0\ (q\ne1). \tag{5}
\]

For \(q\ge2\), sums of \(q\) exponents from \(\{0,1,3,4\}\) fill
\(\{0,\ldots,4q\}\); \(q=2\) is direct and induction adds 0 through 4.
At degree four the sole absent exponent is two. This gives the complete
fourth-Veronese defect, not the dimensions of every other graded piece.

The affine reduced model \(\operatorname{Spec}A_{\rm red}\) retains \(D\)
at its vertex. Its puncture is the smooth punctured plane. Affinizing
that puncture or normalizing the affine model gives the plane and erases
\(D\). In particular global sections of the nonreduced punctured cover,
followed by reduction, need not agree with global sections after reduction.
More intrinsically, the exact restriction sequence gives

\[
D_n=\operatorname{im}\bigl[H^0(C,\mathcal O(n))
\longrightarrow H^1(Z,J\otimes L^n)\bigr]. \tag{6}
\]

This is a section-extension defect. It is not a residual curve or an
established attachment cost. Normal graded-domain cyclic-cover results,
such as [Tomari–Watanabe, §3](https://www.jstage.jst.go.jp/article/kodaimath1978/24/3/24_3_436/_pdf/-char/en),
do not remove this nilpotent/vertex issue.

There are exact restrictions on the reduced section images
\(V_i=\operatorname{im}[H^0(Z,L^i)\to H^0(C,\mathcal O(i))]\):

\[
V_1\in\{0,ks,kt\},\qquad \dim V_2\le1. \tag{7}
\]

Indeed \((\alpha s+\beta t)^4\in V_4\) has middle coefficient
\(6\alpha^2\beta^2=0\). A vector space contained in the union of two
coordinate axes lies in one axis. For binary quadratics multiplication
into \(V_4\) makes \(V_2\) totally isotropic for the nondegenerate pairing
\(\langle(a,b,c),(a',b',c')\rangle=ac'+bb'+ca'\). Its isotropic subspaces
have dimension at most one. Equivalently the allowed squares lie on a
smooth plane conic, containing no projective line. A nonzero reduced
section of \(L\) must vanish at a marked endpoint; no nonzero image is
forced, and (7) does not bound nilpotent sections.

## An actual Gorenstein root algebra with defective reduction

Use the [twisted-cubic supported CI](contact_jacobians_and_hamiltonian_actions.md#controls-and-the-precise-remaining-implication)
\(Z_T=V(y_0y_2-y_1^2,y_2^3-2y_1y_2y_3+y_0y_3^2)\). It is a primitive
double with nilradical \(\mathcal O_{\mathbf P^1}(-5)\) and
\(\omega_{Z_T}=\mathcal O_{Z_T}(1)\), a canonical genus-four ribbon in the
sense of [Bayer–Eisenbud, §§4–5](https://www.math.columbia.edu/~bayer/papers/Ribbons_BE95.pdf).
Its unique cubic polarization root \(M\) can be calculated directly.
On \(y_0=1\) let \(u=y_1,\varepsilon=y_3-u^3\), \(\varepsilon^2=0\);
on \(y_3=1\), let \(v=y_2,\eta=y_1-v^2\), \(\eta^2=0\). On overlap,

\[
v=u^{-1}-u^{-4}\varepsilon,\quad\eta=u^{-5}\varepsilon,\quad
m_\infty=(u+\tfrac13u^{-2}\varepsilon)m_0.
\]

A reduced section \(\sum_{j=0}^n a_jv^j\) of \(M^n\) requires on the
\(u\)-chart the nilpotent correction

\[
\varepsilon\sum_{j=0}^n a_j(n/3-j)u^{n-j-3}. \tag{8}
\]

Corrections from the \(u\)-chart have nonnegative exponents; those from
the \(v\)-chart have exponents at most \(n-5\). At \(n=1\) the two forbidden
exponents force both coefficients zero. At \(n=2\), only \(j=0,2\) fail
the exponent ranges, leaving one section. At \(n=3\) the sole intervening
exponent has multiplier zero. For \(n\ge4\), the two ranges cover every
integer. Consequently \(h^0(M)=0\), \(h^0(M^2)=1\), and restriction is
onto \(\mathcal O(n)\) for every \(n\ge3\). Negative degrees have neither
reduced nor nilpotent sections.

The reduced root algebra has normalization defect of dimension two in
each of degrees one and two and zero elsewhere. Its third-Veronese defect
is zero. Repeating (3)–(4) with three instead of four proves that the full
root algebra of this actual CI is CM and Gorenstein. Thus an ample root
without sections and a defective reduced cover coexist with sole support.
This control does **not** realize the quartic's nonzero invariant defect
\(D_4\), and leaves room for a further theorem about that precise defect.

## Characteristic boundaries of the root mechanism

The logarithmic vector-space description (1) is characteristic zero.
Nevertheless the unique fourth-root **class** and (2)–(6) extend to odd
characteristic under the same sole-support CI hypotheses. To see the
root assertion without a logarithm, filter the nilpotent unit sheaf
\(1+J\) by its powers. Each successive additive quotient has multiplication
by four invertible when \(p\ne2\), so fourth power is an automorphism of
\(1+J\) and of its cohomology. The unit sequence still gives a surjection
\(\operatorname{Pic}(Z)\to\operatorname{Pic}(C)\), and its kernel is
uniquely four-divisible; constants lift as before. The same root
construction follows. The section-module/depth proof is characteristic
free, and the fourth-power torsor and its trace pairing are étale/perfect
when four is invertible. Thus the Gorenstein conclusion survives for
odd \(p\); it does not obstruct positive-characteristic STCI existence.
The reduced fourth-Veronese defect calculation is also unchanged.

For (7), the \(V_1\) argument uses the coefficient six and therefore needs
\(p\ne2,3\); it supplies no coordinate-axis restriction in characteristic
three. The \(V_2\) nondegenerate-pairing bound works for odd \(p\), since
its matrix is nonsingular and a totally isotropic subspace in dimension
three has dimension at most one. In characteristic two fourth roots
need not be uniquely liftable, the displayed torsor is not étale, and
its degree-four trace is zero. This proof supplies no Gorenstein root
cover or section-image restriction in that case. The twisted-cubic
ribbon calculation is retained in characteristic zero: its coefficients
\(n/3-j\) use division by three and may acquire additional zeros after
reduction modulo a prime, so the exact section dimensions are not
asserted in positive characteristic. None of these boundaries amounts
to a general failure of finite duality in characteristic \(p\).

## Where a residual bound or construction would need more

For a proper intersection with cycle \(ab=4m+\deg R\), its \(C\)-primary
part still has the abstract Picard/root construction. But its full
hyperplane section ring need not equal its embedded coordinate ring,
and its dualizing sheaf need not be \(H^c\). Thus (2)–(4) do not transfer
without extra evidence. No inequality comparing the vertex defect \(D\)
with \(\deg R\) has been obtained. A defect on a cone vertex is not an
additional projective component.

For sole-support CIs, (4), (5), and (7) have not been proved incompatible.
A construction would require an actual nilpotent extension whose fourth
Veronese has the four specified generators and two regular-sequence
relations. An obstruction would require a theorem that forces a section
or extension those data forbid. The abstract root and finite-duality
mechanism alone supply neither. The [first-neighborhood control](section_defects_and_exceptional_cover_controls.md#the-specified-missing-coordinate-and-the-graph-normal-extension)
explains why even the original missing coordinate can consistently fail
to lift at every thick stage.
